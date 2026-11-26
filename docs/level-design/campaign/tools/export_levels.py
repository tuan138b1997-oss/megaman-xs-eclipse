# Xuất 25 màn thiết kế (tools/stages/<id>.py) sang dữ liệu màn chơi được:
#   levels/data/<id>.json  — định dạng trung lập (tile 32px) cho Unity / engine khác
#   levels/data/all.js     — mọi màn gộp lại, gán vào LEVEL_DATA cho bản web
# Chạy: python3 tools/export_levels.py [id ...]   (từ docs/level-design/campaign)
import sys, os, json, importlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
OUT = os.path.join(REPO, 'levels', 'data')
from order import ORDER  # noqa: E402

src = open(os.path.join(REPO, 'campaign-data.js'), encoding='utf8').read()
BP = json.JSONDecoder().raw_decode(src[src.index('{'):])[0]
BPS = {s['id']: s for s in BP['stages']}

SUBS = {'x5_grizzly': 'truck', 'x5_makkoeen': 'submarine', 'x6_mijinion': 'illumina'}
CHASER = {'x5_kraken', 'x6_wolfang'}
TIMING = {'laser': (2.0, 1.0), 'elec': (1.5, 1.5), 'fire': (1.0, 2.5), 'lava': (1.5, 3.0), 'steam': (1.2, 1.6), 'trash': (None, None)}


def r1(v): return round(float(v), 2)


def export(sid):
    st = importlib.import_module('stages.' + sid).STAGE
    bp = BPS[sid]
    rooms = st['rooms']
    mid = next((i for i, r in enumerate(rooms) if r['kind'] == 'mini'), len(rooms))
    boss = rooms[-1]
    assert boss['kind'] == 'boss', sid
    L = dict(name=st['title'], stage=sid, theme=bp['theme'], tileSize=32, rooms=[], checkpoints=[], solids=[], slopes=[], ledges=[],
             conveyors=[], hazards=[], zones=[], walls=[], switches=[], portals=[], enemies=[], items=[], turrets=[], vehicles=[], subBoss=None)
    caps = bp.get('capsules') or []
    hz_i = 0
    rescue_i = 0
    orb_room_codes = set()
    zone_mode_default = 'lowgrav' if sid == 'x5_necrobat' else 'flip'
    for ri, r in enumerate(rooms):
        ox, oy, area = r['x'], r['y'], (1 if ri < mid else 2)
        bottom, top = oy + r['h'], oy
        L['rooms'].append(dict(code=r['code'], name=r['name'], x=ox, y=oy, w=r['w'], h=r['h'], area=area, kind=r['kind'] or 'room', difficulty=r['diff']))
        geo = r['geo']
        arrows = [g for g in geo if g[0] == 'arrow']
        switches = sorted([g for g in geo if g[0] == 'ent' and g[1] == 'K'], key=lambda g: g[2])
        sw_index = {}
        for g in switches:
            sw_index[id(g)] = len(L['switches'])
            L['switches'].append(dict(x=r1(ox + g[2] - 0.5), y=r1(oy + g[3] - 0.5), targets=[]))

        def link_switch(x):
            left = [g for g in switches if g[2] < x]
            return sw_index[id(left[-1])] if left else None

        if any(g[0] == 'ent' and g[1] == 'O' for g in geo): orb_room_codes.add(r['code'])
        for g in geo:
            t = g[0]
            if t == 'floor':
                seg = []
                for p in list(g[1]) + [None]:
                    if p is None:
                        for (x0, y0), (x1, y1) in zip(seg, seg[1:]):
                            if x1 == x0: continue
                            if y0 == y1:
                                L['solids'].append(dict(x=r1(ox + x0), y=r1(oy + y0), w=r1(x1 - x0), h=r1(bottom - oy - y0), area=area))
                            else:
                                L['slopes'].append(dict(x0=r1(ox + x0), y0=r1(oy + y0), x1=r1(ox + x1), y1=r1(oy + y1), bottom=bottom, area=area))
                        seg = []
                    else:
                        seg.append(p)
            elif t == 'ceil':
                pts = [p for p in g[1] if p]
                for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
                    if x1 > x0: L['solids'].append(dict(x=r1(ox + x0), y=top, w=r1(x1 - x0), h=r1(max(y0, y1)), area=area))
            elif t == 'block':
                _, x, y, w, h = g
                if w > 0 and h > 0: L['solids'].append(dict(x=r1(ox + x), y=r1(oy + y), w=r1(w), h=r1(h), area=area))
            elif t == 'haz':
                _, k, x, y, w, h = g
                if h <= 0 or w <= 0: continue
                box = dict(x=r1(ox + x), y=r1(oy + y), w=r1(w), h=r1(h))
                if k in ('water', 'mud', 'dark', 'ice', 'snow'):
                    if k == 'snow': continue
                    L['zones'].append(dict(type=k, **box)); continue
                on, off = TIMING.get(k, (None, None))
                L['hazards'].append(dict(type={'spike': 'spike'}.get(k, k), **box, on=on, off=off, phase=r1((hz_i % 5) * 0.6)))
                hz_i += 1
            elif t == 'bar':
                _, k, x, y, w, h = g
                box = dict(x=r1(ox + x), y=r1(oy + y), w=r1(w), h=r1(h))
                if k == 'shelf': continue
                si = link_switch(x) if k in ('laser', 'elec', 'door') else None
                if si is not None:
                    L['walls'].append(dict(type='laser' if k in ('laser', 'elec') else 'gate', **box))
                    L['switches'][si]['targets'].append(len(L['walls']) - 1); continue
                if k == 'door':
                    if r['code'] in orb_room_codes or any(g2[0] == 'ent' and g2[1] == 'O' for g2 in geo):
                        L['walls'].append(dict(type='orbgate', **box))
                    continue  # cửa boss/cửa phòng: chỉ trang trí
                on, off = TIMING.get(k, (None, None))
                L['hazards'].append(dict(type=k, **box, on=on, off=off, phase=r1((hz_i % 5) * 0.6), column=True))
                hz_i += 1
            elif t == 'plat':
                _, k, x, y, w = g
                L['ledges'].append(dict(x=r1(ox + x), y=r1(oy + y), w=r1(w), kind=k, phase=r1((len(L['ledges']) % 4) * 0.7)))
            elif t == 'conv':
                _, x, y, w, d = g
                L['conveyors'].append(dict(x=r1(ox + x), y=r1(oy + y), w=r1(w), speed=110 * d))
            elif t == 'crack':
                _, x, y, h = g
                mech = any(g2[0] == 'ent' and g2[1] == 'V' for g2 in geo) and sid not in CHASER
                L['walls'].append(dict(type='steel' if mech else 'stone', x=r1(ox + x), y=r1(oy + y), w=2, h=r1(h)))
            elif t == 'zone':
                _, k, x, y, w, h, lab = g
                if w <= 0 or h <= 0: continue
                z = dict(type=k, x=r1(ox + x), y=r1(oy + y), w=r1(w), h=r1(h), label=lab)
                if k in ('wind', 'current'):
                    inside = [a for a in arrows if x - 1 <= a[2] <= x + w + 1 and y - 1 <= a[3] <= y + h + 1] or arrows
                    dx = sum(a[4] for a in inside); dy = sum(a[5] for a in inside)
                    if not inside: dx = -1
                    n = max(1e-6, (dx * dx + dy * dy) ** .5)
                    z.update(dx=r1(dx / n), dy=r1(dy / n), strength=70 if k == 'wind' else 90, cycle='giật' in lab or 'đổi chiều' in lab)
                if k == 'grav':
                    mode = 'well' if 'hút' in lab else 'flipcycle' if 'mỗi' in lab else zone_mode_default
                    if sid == 'x5_necrobat' and mode == 'flipcycle': mode = 'lowgrav'
                    z['type'] = mode
                L['zones'].append(z)
            elif t == 'ent':
                _, c, x, y = g
                X, Y = ox + x, oy + y
                if c in 'SDB':
                    typ = {'S': 'sniper', 'D': 'drone', 'B': 'brute'}[c]
                    L['enemies'].append(dict(type=typ, x=r1(X - 0.5), y=r1(Y + 1 if c != 'D' else Y + 0.5)))
                elif c == 'R':
                    L['items'].append(dict(type='rescue', id=f'{sid}:reploid:{rescue_i}', x=r1(X - 0.5), y=r1(Y + 1))); rescue_i += 1
                elif c == 'H':
                    L['items'].append(dict(type='relic', id=f'{sid}:heart', x=r1(X - 0.45), y=r1(Y + 0.9)))
                elif c == 'T':
                    L['items'].append(dict(type='tank', id=f'{sid}:tank', x=r1(X - 0.4), y=r1(Y + 0.95)))
                elif c == 'A':
                    for cp in caps:
                        L['items'].append(dict(type='capsule', id=f"{sid}:{cp['armor']}:{cp['part']}", armor=cp['armor'], part=cp['part'], x=r1(X - 0.7), y=r1(Y + 1)))
                elif c == 'O':
                    L['items'].append(dict(type='orb', x=r1(X - 0.25), y=r1(Y + 0.25)))
                elif c == 'C':
                    L['checkpoints'].append(dict(x=r1(X), y=r1(Y + 1)))
                elif c == 'V':
                    L['vehicles'].append(dict(type='chaser' if sid in CHASER else 'mech', x=r1(X - 1), y=r1(Y + 1)))
                elif c == 'G':
                    L['portals'].append(dict(x=r1(X - 0.7), y=r1(Y + 1), room=r['code']))
                elif c == 'W':
                    L['turrets'].append(dict(x=r1(X - 0.5), y=r1(Y - 0.5), hp=6))
                elif c == 'M':
                    L['subBoss'] = dict(id=SUBS.get(sid, 'donut'), x=r1(X - 2), y=r1(Y - 2), hp=45, room=r['code'],
                                        gate=dict(x=r1(ox + r['w'] - 2), y=r1(oy + 1), w=2, h=r1(r['h'] - 3)))
    # cổng dịch chuyển: ghép theo cặp trong từng phòng (P1→P2, P3→P4...). Màn cuối: 8 cổng boss rush.
    if sid == 'x6_f5_bossrush':
        for j, po in enumerate(L['portals']): po['rush'] = j
    else:
        by = {}
        for i, po in enumerate(L['portals']): by.setdefault(po['room'], []).append(i)
        for idx in by.values():
            for a, b in zip(idx[0::2], idx[1::2]):
                L['portals'][a]['to'] = b; L['portals'][b]['to'] = a
    # checkpoint đầu màn
    r0 = rooms[0]
    start_y = next((r0['y'] + p[1] for g in r0['geo'] if g[0] == 'floor' for p in g[1] if p), r0['y'] + r0['h'] - 2)
    L['checkpoints'].insert(0, dict(x=r0['x'] + 3, y=r1(start_y)))
    # boss
    bf = next((boss['y'] + p[1] for g in boss['geo'] if g[0] == 'floor' for p in g[1] if p), boss['y'] + boss['h'] - 2)
    L['width'] = boss['x'] + boss['w']
    L['height'] = max(r['y'] + r['h'] for r in rooms) + 2
    L['floorBoss'] = r1(bf)
    L['bossGateX'] = boss['x'] + 1
    L['areaMarks'] = [rooms[mid]['x'], rooms[min(mid + 1, len(rooms) - 1)]['x']]
    L['palette'] = {k: '#%02x%02x%02x' % v for k, v in st['theme'].items()}
    return L


def main(ids):
    os.makedirs(OUT, exist_ok=True)
    for sid in ids:
        L = export(sid)
        open(os.path.join(OUT, sid + '.json'), 'w', encoding='utf8').write(json.dumps(L, ensure_ascii=False, indent=1))
        print(sid, 'solids', len(L['solids']), 'ledges', len(L['ledges']), 'haz', len(L['hazards']), 'zones', len(L['zones']), 'w', L['width'], 'h', L['height'])


def write_all():
    parts = []
    for sid in ORDER:
        f = os.path.join(OUT, sid + '.json')
        if os.path.exists(f):
            parts.append(f"'{sid}':" + json.dumps(json.load(open(f, encoding='utf8')), ensure_ascii=False, separators=(',', ':')))
    open(os.path.join(OUT, 'all.js'), 'w', encoding='utf8').write(
        '// Sinh tự động bởi export_levels.py: dữ liệu mọi màn đã dựng, cho bản web.\n(window.LEVEL_DATA=window.LEVEL_DATA||{});Object.assign(window.LEVEL_DATA,{\n' + ',\n'.join(parts) + '\n});\n')
    print('all.js', len(parts), 'màn')


if __name__ == '__main__':
    main(sys.argv[1:] or ORDER)
    write_all()
