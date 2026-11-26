# Nhập ngược project LDtk (levels/ldtk/<id>.ldtk) thành dữ liệu màn cho game: levels/data/<id>.json (+ all.js).
# Dùng sau khi chỉnh màn trong LDtk:  python3 tools/import_ldtk.py <id> [...]   (từ docs/level-design/campaign)
# Quy ước đọc: IntGrid Collision 1/7/8 -> khối đặc · 4 -> kệ · 5 -> sàn vỡ · 6 -> băng chuyền (tốc độ lấy từ entity Conveyor nếu có)
#              9 -> bẫy tĩnh (loại lấy từ entity Hazard_Area, không có thì theo chủ đề) · 2/3 -> dốc (từ entity Slope).
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
from export_levels import write_all  # noqa: E402

G = 32
DEFAULT_HAZ = {'fire': 'lava', 'nature': 'thorn'}


def runs(grid, W, H, vals):
    """Gộp ô thành hình chữ nhật: chạy ngang theo hàng rồi nối dọc các chạy giống nhau."""
    rects, open_ = [], {}
    for y in range(H + 1):
        row = []
        if y < H:
            x = 0
            while x < W:
                if grid[y * W + x] in vals:
                    x0 = x
                    while x < W and grid[y * W + x] in vals: x += 1
                    row.append((x0, x))
                else: x += 1
        nxt = {}
        for seg in row:
            if seg in open_: nxt[seg] = open_[seg]
            else: nxt[seg] = y
        for seg, y0 in open_.items():
            if seg not in nxt or nxt[seg] != y0: rects.append((seg[0], y0, seg[1] - seg[0], y - y0))
        open_ = {s: v for s, v in nxt.items()}
    return rects


def fv(e):
    return {f['__identifier']: f['__value'] for f in e['fieldInstances']}


def import_one(sid):
    d = json.load(open(os.path.join(REPO, 'levels', 'ldtk', sid + '.ldtk'), encoding='utf8'))
    old_p = os.path.join(REPO, 'levels', 'data', sid + '.json')
    old = json.load(open(old_p, encoding='utf8')) if os.path.exists(old_p) else {}
    theme = old.get('theme') or d['defs']['tilesets'][0]['identifier'].split('_')[-1].lower()
    L = dict(name=old.get('name', sid), stage=sid, theme=theme, tileSize=G, rooms=[], checkpoints=[], solids=[], slopes=[], ledges=[], conveyors=[],
             hazards=[], zones=[], walls=[], switches=[], portals=[], enemies=[], items=[], turrets=[], vehicles=[], subBoss=None, palette=old.get('palette', {}), specials=[])
    gates, switches, portals = {}, [], []
    boss = None
    for lv in d['levels']:
        f = fv(lv); rx, ry = lv['worldX'] // G, lv['worldY'] // G; W, H = lv['pxWid'] // G, lv['pxHei'] // G
        code = f.get('code') or lv['identifier']
        kind = 'boss' if code == 'BOSS' else 'mini' if code == 'MID' else 'room'
        area = f.get('area') or 1
        L['rooms'].append(dict(code=code, name=old.get('rooms') and next((r['name'] for r in old['rooms'] if r['code'] == code), code) or code,
                               x=rx, y=ry, w=W, h=H, area=area, kind=kind, difficulty=f.get('difficulty')))
        ents = [e for li in lv['layerInstances'] if li['__type'] == 'Entities' for e in li['entityInstances']]
        col = next(li for li in lv['layerInstances'] if li['__identifier'] == 'Collision')
        g = col['intGridCsv']
        for x, y, w, h in runs(g, W, H, {1, 7, 8}):
            L['solids'].append(dict(x=rx + x, y=ry + y, w=w, h=h, area=area))
        for v, kind_ in ((4, 'shelf'), (5, 'break')):
            for x, y, w, h in runs(g, W, H, {v}):
                for k in range(h): L['ledges'].append(dict(x=rx + x, y=ry + y + k, w=w, kind=kind_))
        hz_areas = []
        for e in ents:
            n = e['__identifier']; F = fv(e)
            X, Y, EW, EH = rx + e['px'][0] / G, ry + e['px'][1] / G, e['width'] / G, e['height'] / G
            box = dict(x=round(X, 2), y=round(Y, 2), w=round(EW, 2), h=round(EH, 2))
            if n == 'PlayerSpawn': L['checkpoints'].insert(0, dict(x=round(X, 2), y=round(Y + 1.5, 2)))
            elif n == 'Checkpoint': L['checkpoints'].append(dict(x=round(X + .5, 2), y=round(Y + 2, 2)))
            elif n.startswith('Enemy_'):
                t = n[6:].lower(); L['enemies'].append(dict(type=t, x=round(X, 2), y=round(Y + (1 if t == 'drone' else 1.5), 2)))
            elif n == 'NPC_Reploid': L['items'].append(dict(type='rescue', id=F.get('id'), x=round(X, 2), y=round(Y + 1.5, 2)))
            elif n == 'Item_Capsule': L['items'].append(dict(type='capsule', id=F.get('id'), armor=F.get('armor'), part=F.get('part'), x=round(X, 2), y=round(Y + 2.2, 2)))
            elif n == 'Item_HeartTank': L['items'].append(dict(type='relic', id=F.get('id') or f'{sid}:heart', x=round(X, 2), y=round(Y + .9, 2)))
            elif n == 'Item_SubTank': L['items'].append(dict(type='tank', id=F.get('id') or f'{sid}:tank', x=round(X, 2), y=round(Y + .95, 2)))
            elif n == 'Item_Orb': L['items'].append(dict(type='orb', x=round(X, 2), y=round(Y, 2)))
            elif n in ('Hazard_Flame', 'Hazard_Laser', 'Hazard_Elec', 'Hazard_Steam', 'Hazard_LavaColumn'):
                t = {'Hazard_Flame': 'fire', 'Hazard_Laser': 'laser', 'Hazard_Elec': 'elec', 'Hazard_Steam': 'steam', 'Hazard_LavaColumn': 'lava'}[n]
                h = dict(type=t, **box, on=F.get('on'), off=F.get('off'), phase=F.get('phase') or 0)
                if n == 'Hazard_LavaColumn' or F.get('column'): h['column'] = True
                L['hazards'].append(h)
            elif n in ('Hazard_Press', 'Hazard_ChaseWall', 'Zone_RisingMagma') and F.get('params'):
                sp = json.loads(F['params']); sp.update({k: box[k] for k in ('x', 'w') if k in sp}); L['specials'].append(sp)
            elif n == 'Hazard_Press': L['hazards'].append(dict(type='trash', **box, on=None, off=None, phase=F.get('phase') or 0))
            elif n == 'Hazard_Mine': L['hazards'].append(dict(type='mine', x=round(X, 2), y=round(Y, 2), w=1, h=1, on=None, off=None, phase=0))
            elif n == 'Hazard_Void': L['hazards'].append(dict(type='void', **box, on=None, off=None, phase=0))
            elif n == 'Hazard_Area': hz_areas.append(dict(type=F.get('kind') or 'spike', **box))
            elif n == 'Slope':
                up = F.get('dir') != 'down'; bot = F.get('bottom') or (Y + EH + 4)
                L['slopes'].append(dict(x0=box['x'], y0=round(Y + EH if up else Y, 2), x1=round(X + EW, 2), y1=round(Y if up else Y + EH, 2), bottom=bot, area=area))
            elif n.startswith('Zone_'):
                t = {'Zone_Water': 'water', 'Zone_Wind': 'wind', 'Zone_Current': 'current', 'Zone_Updraft': 'updraft', 'Zone_LowGravity': 'lowgrav',
                     'Zone_BlackHole': 'well', 'Zone_Slow': 'slow', 'Zone_Dark': 'dark', 'Zone_AcidRain': 'rain', 'Zone_Alarm': 'alarm', 'Zone_Mud': 'mud',
                     'Zone_Ice': 'ice', 'Zone_Electric': 'elec', 'Zone_GravityFlip': F.get('mode') or 'flip'}.get(n)
                if t: L['zones'].append(dict(type=t, **box, label=F.get('label') or '', dx=F.get('dx') or 0, dy=F.get('dy') or 0, strength=F.get('strength') or 70))
            elif n.startswith('Platform_'):
                k = {'Platform_Moving': 'move', 'Platform_Lift': 'thrust', 'Platform_Bounce': 'bounce'}.get(n) or ('holoB' if F.get('phase') == 'B' else 'holo')
                L['ledges'].append(dict(x=box['x'], y=box['y'], w=box['w'], kind=k))
            elif n == 'Conveyor': L['conveyors'].append(dict(x=box['x'], y=box['y'], w=box['w'], speed=F.get('speed') or 110))
            elif n == 'Wall_Breakable': L['walls'].append(dict(type='steel' if F.get('breakBy') == 'rideArmor' else 'stone', **box))
            elif n == 'Gate':
                if F.get('kind') == 'subBoss': gates['__sub__'] = box
                else: gates[F.get('id')] = len(L['walls']); L['walls'].append(dict(type=F.get('kind') or 'gate', **box))
            elif n == 'Switch': switches.append((box, F.get('targets') or ''))
            elif n == 'Portal': portals.append((box, F.get('id'), F.get('to'), F.get('rush'), code, F.get('alt')))
            elif n == 'Turret': L['turrets'].append(dict(x=box['x'], y=box['y'], hp=F.get('hp') or 6))
            elif n == 'Vehicle': L['vehicles'].append(dict(type='chaser' if F.get('type') == 'rideChaser' else 'mech', x=box['x'], y=round(Y + 2.2, 2)))
            elif n == 'SubBoss': L['subBoss'] = dict(id=F.get('id') or 'donut', x=box['x'], y=box['y'], hp=F.get('hp') or 45, room=code)
            elif n == 'BossGate': boss = dict(x=box['x'], floor=round(Y + EH, 2), room=(rx, ry, W, H))
        for a in hz_areas: L['hazards'].append(dict(**a, on=None, off=None, phase=0))
        covered = lambda cx, cy: any(a['x'] <= cx < a['x'] + a['w'] and a['y'] <= cy < a['y'] + a['h'] for a in hz_areas)
        for x, y, w, h in runs(g, W, H, {9}):
            if not covered(rx + x + .5, ry + y + .5):
                L['hazards'].append(dict(type=DEFAULT_HAZ.get(theme, 'spike'), x=rx + x, y=ry + y, w=w, h=h, on=None, off=None, phase=0))
    for box, tg in switches:
        L['switches'].append(dict(x=box['x'], y=box['y'], targets=[gates[t] for t in tg.split(',') if t in gates]))
    ids = {pid: i for i, (_, pid, _, _, _, _) in enumerate(portals)}
    for box, pid, to, rush, room, alt in portals:
        po = dict(x=box['x'], y=round(box['y'] + 2.5, 2), room=room)
        if rush is not None: po['rush'] = rush
        if to in ids: po['to'] = ids[to]
        if alt: po['alt'] = True
        L['portals'].append(po)
    if L['subBoss'] and '__sub__' in gates: L['subBoss']['gate'] = gates['__sub__']
    rooms = L['rooms']; br = rooms[-1]
    L['width'] = br['x'] + br['w']; L['height'] = max(r['y'] + r['h'] for r in rooms) + 2
    L['floorBoss'] = boss['floor'] if boss else br['y'] + br['h'] - 2
    L['bossGateX'] = boss['x'] if boss else br['x'] + 1
    mid = next((i for i, r in enumerate(rooms) if r['kind'] == 'mini'), len(rooms) - 1)
    L['areaMarks'] = [rooms[mid]['x'], rooms[min(mid + 1, len(rooms) - 1)]['x']]
    json.dump(L, open(os.path.join(REPO, 'levels', 'data', sid + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(sid, 'solids', len(L['solids']), 'ledges', len(L['ledges']), 'haz', len(L['hazards']), 'zones', len(L['zones']), 'ents', len(L['enemies']) + len(L['items']))


if __name__ == '__main__':
    ids = sys.argv[1:]
    if not ids: print('Dùng: python3 tools/import_ldtk.py <id> [...]'); sys.exit(1)
    for sid in ids:
        if sid == 'x5_dinorex': print('x5_dinorex: Lò Nham Thạch dùng builder riêng (levels/lo-nham-thach.js), chưa nhập ngược.'); continue
        import_one(sid)
    write_all()
