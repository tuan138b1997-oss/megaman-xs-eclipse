# Xuất 26 màn sang project LDtk 1.5.3: levels/ldtk/<id>.ldtk (mỗi phòng = 1 Level, bố cục Free).
#   - Lớp Collision (IntGrid) theo quy ước chung: 1 đất đặc · 2 dốc 45° · 3 dốc 22.5° · 4 kệ một chiều ·
#     5 sàn vỡ · 6 băng chuyền · 7 tường nứt · 8 trần bám được · 9 dung nham/gai. Auto-rule phủ tile terrain-<theme>.
#   - Lớp Entities: bộ Entity dùng chung cho mọi màn, thuộc tính nằm trong Custom Fields.
# Nguồn: levels/data/<id>.json (25 màn) và levels/lo-nham-thach.level.json (x5_dinorex).
# Chạy: python3 tools/export_ldtk.py [id ...]   (từ docs/level-design/campaign); kiểm tra bằng JSON schema nếu có.
import os, sys, json, uuid, math, random
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
OUT = os.path.join(REPO, 'levels', 'ldtk')
from order import ORDER  # noqa: E402

G = 32
INTGRID = [(1, 'Solid', '#6b5a4e'), (2, 'Slope45', '#8a7460'), (3, 'Slope22', '#a08a70'), (4, 'OneWay', '#c8aa78'),
           (5, 'Crumble', '#d2864a'), (6, 'Conveyor', '#5a5e70'), (7, 'CrackedWall', '#9a7b9a'), (8, 'CeilingGrab', '#7aa0c8'),
           (9, 'LavaSpike', '#ff6e1e')]
F, I, B, S = 'Float', 'Int', 'Bool', 'String'
# (tên, màu, rộng, cao, co giãn, sprite trong atlas, các trường)
ENTITY_DEFS = [
    ('PlayerSpawn', '#63c74d', 32, 48, False, 'x-idle', []),
    ('Checkpoint', '#4fd08a', 32, 64, False, None, []),
    ('Enemy_Sniper', '#ff5a5a', 32, 48, False, 'sniper', []),
    ('Enemy_Drone', '#ffa03c', 32, 32, False, 'drone', []),
    ('Enemy_Brute', '#e65050', 40, 56, False, None, []),
    ('NPC_Reploid', '#78ff8c', 32, 48, False, 'rescue-0', [('id', S)]),
    ('Item_Capsule', '#78e6ff', 44, 70, False, None, [('id', S), ('armor', S), ('part', S)]),
    ('Item_HeartTank', '#ff78dc', 28, 28, False, None, [('id', S)]),
    ('Item_SubTank', '#78c8ff', 26, 30, False, None, [('id', S)]),
    ('Item_Orb', '#ffe080', 24, 24, False, 'el-orb', []),
    ('Hazard_Flame', '#ff9a3c', 32, 32, True, 'el-fireball', [('on', F), ('off', F), ('phase', F)]),
    ('Hazard_Press', '#e0b030', 64, 32, True, None, [('wait', F), ('slam', F), ('lift', F), ('phase', F), ('params', S)]),
    ('Hazard_LaserSweep', '#ff3c50', 32, 320, True, 'el-laser', [('speed', F), ('patrol', B), ('params', S)]),
    ('Hazard_ChaseWall', '#c8c8d2', 64, 320, True, None, [('look', S), ('speed', F), ('params', S)]),
    ('Hazard_RollingRock', '#c09070', 32, 32, True, None, [('interval', F), ('speed', F), ('maxSpeed', F)]),
    ('Hazard_Laser', '#ff3c50', 20, 64, True, 'el-laser', [('on', F), ('off', F), ('phase', F)]),
    ('Hazard_Elec', '#a8e8ff', 64, 16, True, 'el-elec', [('on', F), ('off', F), ('phase', F), ('column', B)]),
    ('Hazard_LavaColumn', '#ff6e1e', 32, 96, True, None, [('on', F), ('off', F), ('phase', F)]),
    ('Hazard_Steam', '#e6e6e6', 64, 32, True, None, [('on', F), ('off', F), ('phase', F), ('dir', I)]),
    ('Hazard_Mine', '#ff5050', 32, 32, False, 'el-mine', []),
    ('Hazard_Void', '#05060c', 64, 32, True, None, []),
    ('Hazard_Area', '#ff8040', 64, 32, True, None, [('kind', S)]),
    ('Slope', '#a08a70', 64, 32, True, None, [('dir', S), ('bottom', F)]),
    ('Moving_Minecart', '#9a7a58', 128, 32, True, None, [('count', I), ('speed', F), ('spanFrom', F), ('spanTo', F)]),
    ('Platform_Moving', '#78dcff', 96, 16, True, 'el-platform', [('axis', S), ('range', F)]),
    ('Platform_Lift', '#ffc85a', 96, 16, True, 'el-thruster', [('range', F)]),
    ('Platform_Phase', '#a0e6ff', 96, 16, True, 'el-holo', [('phase', S)]),
    ('Platform_Bounce', '#ff8cdc', 64, 16, True, 'el-bounce', [('power', F)]),
    ('Conveyor', '#5a5e70', 128, 16, True, None, [('speed', F)]),
    ('Zone_RisingMagma', '#ff6e1e', 128, 256, True, None, [('speedLow', F), ('speedHigh', F), ('stopY', F), ('params', S)]),
    ('Zone_GravityFlip', '#ff78dc', 128, 128, True, None, [('mode', S), ('label', S)]),
    ('Zone_Updraft', '#a0f0c8', 96, 256, True, None, [('power', F)]),
    ('Zone_Water', '#2a6ab8', 128, 128, True, None, []),
    ('Zone_Wind', '#d8f0ff', 128, 128, True, None, [('dx', F), ('dy', F), ('strength', F), ('label', S)]),
    ('Zone_Current', '#9fe6ff', 128, 128, True, None, [('dx', F), ('dy', F), ('strength', F), ('label', S)]),
    ('Zone_LowGravity', '#c8a0ff', 128, 128, True, None, [('scale', F)]),
    ('Zone_BlackHole', '#ff9ae8', 128, 128, True, None, [('pull', F)]),
    ('Zone_Slow', '#b08cff', 128, 128, True, None, [('label', S)]),
    ('Zone_Dark', '#281e3c', 128, 128, True, None, [('label', S)]),
    ('Zone_AcidRain', '#82dc3c', 128, 128, True, None, [('label', S)]),
    ('Zone_Alarm', '#ff5060', 128, 128, True, 'el-probe', [('label', S)]),
    ('Zone_Mud', '#73552d', 128, 64, True, None, []),
    ('Zone_Ice', '#b8e8ff', 128, 32, True, None, []),
    ('Zone_Electric', '#ffeb50', 128, 64, True, None, []),
    ('Switch', '#ffff78', 32, 32, False, 'el-switch', [('targets', S)]),
    ('Gate', '#d24a5a', 32, 96, True, 'el-gate', [('kind', S), ('id', S)]),
    ('Wall_Breakable', '#9a7b9a', 64, 64, True, 'el-wall-steel', [('breakBy', S), ('hp', I)]),
    ('Portal', '#bfe8ff', 45, 80, False, 'el-teleporter', [('id', S), ('to', S), ('rush', I), ('alt', B)]),
    ('Turret', '#ffb04a', 32, 32, False, 'el-turret', [('hp', I)]),
    ('Vehicle', '#ffe678', 70, 70, False, None, [('type', S)]),
    ('SubBoss', '#ff3c82', 110, 110, True, None, [('id', S), ('hp', I)]),
    ('BossGate', '#ff4646', 32, 128, True, None, [('boss', S)]),
]


def uid_gen():
    n = [200]
    def nx(): n[0] += 1; return n[0]
    return nx


def iid(): return str(uuid.uuid4())


def field_def(name, typ, uid):
    return {'identifier': name, 'doc': None, '__type': typ, 'uid': uid, 'type': 'F_' + typ, 'isArray': False, 'canBeNull': True,
            'arrayMinLength': None, 'arrayMaxLength': None, 'editorDisplayMode': 'NameAndValue', 'editorDisplayScale': 1,
            'editorDisplayPos': 'Above', 'editorLinkStyle': 'StraightArrow', 'editorDisplayColor': None, 'editorAlwaysShow': False,
            'editorShowInWorld': True, 'editorCutLongValues': True, 'editorTextSuffix': None, 'editorTextPrefix': None,
            'useForSmartColor': False, 'exportToToc': False, 'searchable': False, 'min': None, 'max': None, 'regex': None,
            'acceptFileTypes': None, 'defaultOverride': None, 'textLanguageMode': None, 'symmetricalRef': False, 'autoChainRef': False,
            'allowOutOfLevelRef': True, 'allowedRefs': 'OnlySame', 'allowedRefsEntityUid': None, 'allowedRefTags': [], 'tilesetUid': None}


# ---------- atlas ảnh cho Entity (khung đầu của từng sprite) ----------
def build_atlas():
    meta = json.load(open(os.path.join(REPO, 'assets', 'atlas.json')))
    env = json.load(open(os.path.join(REPO, 'assets', 'environments', 'environment.json')))['images']
    frames = {}
    for e in ENTITY_DEFS:
        n = e[5]
        if not n: continue
        if n in meta:
            r = meta[n]['rects'][0]; im = Image.open(os.path.join(REPO, 'assets', n + '.png')).convert('RGBA').crop((r['x'], r['y'], r['x'] + r['w'], r['y'] + r['h']))
        elif n in env:
            im = Image.open(os.path.join(REPO, env[n])).convert('RGBA')
            nf = {'el-orb': 4, 'el-fireball': 3, 'el-elec': 5, 'el-mine': 6, 'el-thruster': 3, 'el-holo': 2, 'el-switch': 3, 'el-teleporter': 3, 'el-turret': 5, 'el-probe': 3}.get(n, 1)
            im = im.crop((0, 0, im.width // nf, im.height))
        else: continue
        frames[n] = im
    W = 512; x = y = row = 0; rects = {}
    for n, im in frames.items():
        if x + im.width > W: x = 0; y += row + 2; row = 0
        rects[n] = (x, y, im.width, im.height); x += im.width + 2; row = max(row, im.height)
    H = ((y + row + 31) // 32) * 32
    sheet = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for n, (x, y, w, h) in rects.items(): sheet.paste(frames[n], (x, y))
    os.makedirs(os.path.join(REPO, 'assets', 'levels', 'ldtk'), exist_ok=True)
    sheet.save(os.path.join(REPO, 'assets', 'levels', 'ldtk', 'entity-icons.png'))
    return rects, (W, H)


# ---------- Lò Nham Thạch: đổi định dạng riêng sang định dạng chung ----------
def adapt_dinorex():
    d = json.load(open(os.path.join(REPO, 'levels', 'lo-nham-thach.level.json'), encoding='utf8'))
    L = dict(name='Lò Nham Thạch', stage='x5_dinorex', theme='fire', width=d['width'], height=d['height'], floorBoss=d['floorBoss'],
             bossGateX=d['bossGateX'], rooms=[], checkpoints=d['checkpoints'], solids=[], slopes=d['slopes'], ledges=[], conveyors=[],
             hazards=[], zones=[], walls=[], switches=[], portals=[], enemies=d['enemies'], items=[], turrets=[], vehicles=[], subBoss=None, extra=[])
    for r in d['rooms']:
        L['rooms'].append(dict(code=r['name'].split()[0], name=r['name'], x=r['x'], y=r['y'], w=r['w'], h=r['h'], kind='boss' if r['name'] == 'BOSS' else 'mini' if 'MINI' in r['name'] else 'room'))
    for s in d['solids']:
        b = {k: s[k] for k in 'xywh'}
        if s['type'] == 'cracked': L['walls'].append(dict(type='stone', **b))
        elif s['type'] == 'gate': L['walls'].append(dict(type='gate', **b))
        else:
            L['solids'].append(dict(area=2 if s.get('area') == 'steel' else 1, **b))
            if s['type'] == 'conveyor': L['conveyors'].append(dict(x=s['x'], y=s['y'], w=s['w'], speed=-120))
    for o in d['oneWay']:
        L['ledges'].append(dict(x=o['x'], y=o['y'], w=o['w'], kind={'ledge': 'shelf', 'cart': 'cart', 'crumble': 'break', 'safe': 'safe'}[o['type']]))
    for l in d['lava']: L['hazards'].append(dict(type='lava', x=l['x'], y=l['y'], w=l['w'], h=l['h']))
    for v in d['vents']: L['hazards'].append(dict(type='steam', x=v['x'], y=v['y'], w=v['w'], h=v['h'], on=v['on'], off=v['off'], phase=v['phase'], dir=v.get('dir')))
    for f in d['lavaFalls']: L['hazards'].append(dict(type='lava', column=True, x=f['x'], y=f['y'], w=f['w'], h=f['h'], on=f['on'], off=f['off'], phase=f['phase']))
    for p in d['presses']: L['hazards'].append(dict(type='trash', x=p['x'], y=p['top'], w=p['w'], h=round(p['low'] - p['top'], 2), wait=p['cycle']['wait'], slam=p['cycle']['slam'], lift=p['cycle']['lift'], phase=p['phase']))
    for it in d['items']:
        L['items'].append({k: v for k, v in it.items() if v is not None})
    c = d['carts']; L['extra'].append(('Moving_Minecart', dict(x=c['spanX'][0], y=c['y'] - 1, w=c['w'], h=1, count=c['count'], speed=c['speed'], spanFrom=c['spanX'][0], spanTo=c['spanX'][1])))
    b = d['boulders']; L['extra'].append(('Hazard_RollingRock', dict(x=b['lineFromX'], y=52 - 1.4, w=1.4, h=1.4, interval=b['interval'], speed=b['startSpeed'], maxSpeed=b['maxSpeed'])))
    r = d['risingLava']; L['extra'].append(('Zone_RisingMagma', dict(x=r['x'], y=r['stop'], w=r['w'], h=r['bottom'] - r['stop'], speedLow=r['speedLow'], speedHigh=r['speedHigh'], stopY=r['stop'])))
    sb = d['subBoss'][0] if isinstance(d['subBoss'], list) else d['subBoss']; L['subBoss'] = dict(id=sb['id'], x=sb['x'], y=sb['y'], hp=sb['hp'])
    return L


# ---------- dựng project ----------
def build_project(L, atlas_rects, atlas_size):
    nx = uid_gen(); theme = L['theme']
    terrain = f"../../assets/environments/terrain-{theme}.png"
    timg = Image.open(os.path.join(REPO, 'assets', 'environments', f'terrain-{theme}.png'))
    TS_T, TS_E = 1, 2
    tilesets = [
        {'__cWid': timg.width // G, '__cHei': timg.height // G, 'identifier': f'Terrain_{theme.capitalize()}', 'uid': TS_T, 'relPath': terrain,
         'embedAtlas': None, 'pxWid': timg.width, 'pxHei': timg.height, 'tileGridSize': G, 'spacing': 0, 'padding': 0, 'tags': [],
         'tagsSourceEnumUid': None, 'enumTags': [], 'customData': [], 'savedSelections': [], 'cachedPixelData': None},
        {'__cWid': atlas_size[0] // G, '__cHei': atlas_size[1] // G, 'identifier': 'Entity_Icons', 'uid': TS_E, 'relPath': '../../assets/levels/ldtk/entity-icons.png',
         'embedAtlas': None, 'pxWid': atlas_size[0], 'pxHei': atlas_size[1], 'tileGridSize': G, 'spacing': 0, 'padding': 0, 'tags': [],
         'tagsSourceEnumUid': None, 'enumTags': [], 'customData': [], 'savedSelections': [], 'cachedPixelData': None}]
    # auto-rule: ô đất (1, 2, 3, 7, 8) lấy tile terrain theo vị trí modulo -> mặt texture liền mạch như trong game
    cw = timg.width // G; ch = timg.height // G
    rules = []
    for v in (1, 2, 3, 7, 8):
        for j in range(ch):
            for i in range(cw):
                rules.append({'uid': nx(), 'active': True, 'size': 1, 'tileRectsIds': [[j * cw + i]], 'alpha': 1, 'chance': 1, 'breakOnMatch': True,
                              'pattern': [v], 'flipX': False, 'flipY': False, 'xModulo': cw, 'yModulo': ch, 'xOffset': i, 'yOffset': j,
                              'tileXOffset': 0, 'tileYOffset': 0, 'tileRandomXMin': 0, 'tileRandomXMax': 0, 'tileRandomYMin': 0, 'tileRandomYMax': 0,
                              'checker': 'None', 'tileMode': 'Single', 'pivotX': 0, 'pivotY': 0, 'outOfBoundsValue': None, 'invalidated': False,
                              'perlinActive': False, 'perlinSeed': 1, 'perlinScale': 0.2, 'perlinOctaves': 2, '_v': v, '_i': i, '_j': j})
    group = {'uid': nx(), 'name': 'Terrain', 'color': None, 'icon': None, 'active': True, 'isOptional': False, 'usesWizard': False,
             'requiredBiomeValues': [], 'biomeRequirementMode': 0, 'collapsed': True, 'rules': rules}
    LAYER_ENT, LAYER_COL = nx(), nx()
    base_layer = dict(doc=None, gridSize=G, guideGridWid=0, guideGridHei=0, displayOpacity=1, inactiveOpacity=0.6, hideInList=False,
                      hideFieldsWhenInactive=True, canSelectWhenInactive=True, renderInWorldView=True, pxOffsetX=0, pxOffsetY=0,
                      parallaxFactorX=0, parallaxFactorY=0, parallaxScaling=True, requiredTags=[], excludedTags=[], autoTilesKilledByOtherLayerUid=None,
                      uiFilterTags=[], useAsyncRender=False, intGridValues=[], intGridValuesGroups=[], autoRuleGroups=[], autoSourceLayerDefUid=None,
                      tilesetDefUid=None, tilePivotX=0, tilePivotY=0, biomeFieldUid=None)
    layers = [
        {**base_layer, '__type': 'Entities', 'identifier': 'Entities', 'type': 'Entities', 'uid': LAYER_ENT, 'uiColor': '#ffe080'},
        {**base_layer, '__type': 'IntGrid', 'identifier': 'Collision', 'type': 'IntGrid', 'uid': LAYER_COL, 'uiColor': '#e4a672',
         'intGridValues': [{'value': v, 'identifier': n, 'color': c, 'tile': None, 'groupUid': 0} for v, n, c in INTGRID],
         'autoRuleGroups': [{**group, 'rules': [{k: v for k, v in r.items() if not k.startswith('_')} for r in rules]}], 'tilesetDefUid': TS_T}]
    edefs = {}; entities = []
    for name, color, w, h, rez, spr, fields in ENTITY_DEFS:
        fd = [field_def(fn, ft, nx()) for fn, ft in fields]
        tr = None
        if spr and spr in atlas_rects:
            x, y, tw, th = atlas_rects[spr]; tr = {'tilesetUid': TS_E, 'x': x, 'y': y, 'w': tw, 'h': th}
        e = {'identifier': name, 'uid': nx(), 'tags': [name.split('_')[0]], 'exportToToc': False, 'allowOutOfBounds': False, 'doc': None,
             'width': w, 'height': h, 'resizableX': rez, 'resizableY': rez, 'minWidth': None, 'maxWidth': None, 'minHeight': None, 'maxHeight': None,
             'keepAspectRatio': False, 'tileOpacity': 1, 'fillOpacity': 0.35 if rez else 0.08, 'lineOpacity': 1, 'hollow': False, 'color': color,
             'renderMode': 'Tile' if tr and not rez else 'Rectangle', 'showName': True, 'tilesetId': TS_E if tr else None,
             'tileRenderMode': 'Repeat' if rez else 'FitInside', 'tileRect': tr, 'uiTileRect': None, 'nineSliceBorders': [],
             'maxCount': 1 if name == 'PlayerSpawn' else 0, 'limitScope': 'PerWorld', 'limitBehavior': 'MoveLastOne',
             'pivotX': 0, 'pivotY': 0, 'fieldDefs': fd}
        entities.append(e); edefs[name] = e
    defs = {'layers': layers, 'entities': entities, 'tilesets': tilesets, 'enums': [], 'externalEnums': [], 'levelFields': [
        field_def('code', S, nx()), field_def('difficulty', I, nx()), field_def('area', I, nx())]}
    lvl_fields = {f['identifier']: f for f in defs['levelFields']}

    # ---- gom mọi phần tử vào phòng chứa nó ----
    rooms = L['rooms']
    def room_of(x, y):
        best = None
        for i, r in enumerate(rooms):
            if r['x'] <= x < r['x'] + r['w'] and r['y'] <= y < r['y'] + r['h']:
                if best is None or rooms[best]['w'] * rooms[best]['h'] > r['w'] * r['h']: best = i
        if best is None:
            best = min(range(len(rooms)), key=lambda i: abs(rooms[i]['x'] + rooms[i]['w'] / 2 - x) + abs(rooms[i]['y'] + rooms[i]['h'] / 2 - y))
        return best
    ents = [[] for _ in rooms]

    def add(name, x, y, w=None, h=None, **fv):
        e = edefs[name]
        cx, cy = (x + (w or e['width'] / G) / 2), (y + (h or e['height'] / G) / 2)
        ri = room_of(cx, cy); r = rooms[ri]
        W_ = round((w * G) if w else e['width']); H_ = round((h * G) if h else e['height'])
        px = [round((x - r['x']) * G), round((y - r['y']) * G)]
        px[0] = max(0, min(px[0], r['w'] * G - 1)); px[1] = max(0, min(px[1], r['h'] * G - 1))
        fi = []
        for f in e['fieldDefs']:
            v = fv.get(f['identifier'])
            if v is not None:
                v = {F: float, I: int, B: bool, S: str}[f['__type']](v)
            fi.append({'__identifier': f['identifier'], '__type': f['__type'], '__value': v, '__tile': None, 'defUid': f['uid'],
                       'realEditorValues': [] if v is None else [{'id': {F: 'V_Float', I: 'V_Int', B: 'V_Bool', S: 'V_String'}[f['__type']], 'params': [v]}]})
        ents[ri].append({'__identifier': name, '__grid': [px[0] // G, px[1] // G], '__pivot': [0, 0], '__tags': e['tags'], '__tile': e['tileRect'],
                         '__smartColor': e['color'], 'iid': iid(), 'width': W_, 'height': H_, 'defUid': e['uid'], 'px': px, 'fieldInstances': fi,
                         '__worldX': round(x * G), '__worldY': round(y * G)})

    c0 = L['checkpoints'][0]; add('PlayerSpawn', c0['x'], c0['y'] - 1.5)
    for c in L['checkpoints'][1:]: add('Checkpoint', c['x'] - .5, c['y'] - 2)
    for e in L['enemies']:
        add({'sniper': 'Enemy_Sniper', 'drone': 'Enemy_Drone', 'brute': 'Enemy_Brute'}[e['type']], e['x'], e['y'] - (1 if e['type'] == 'drone' else 1.5))
    for it in L['items']:
        t = it['type']
        if t == 'rescue': add('NPC_Reploid', it['x'], it['y'] - 1.5, id=it.get('id'))
        elif t == 'capsule': add('Item_Capsule', it['x'], it['y'] - 2.2, id=it.get('id'), armor=it.get('armor'), part=it.get('part'))
        elif t == 'relic': add('Item_HeartTank', it['x'], it['y'] - .9, id=it.get('id'))
        elif t == 'tank': add('Item_SubTank', it['x'], it['y'] - .95, id=it.get('id'))
        elif t == 'orb': add('Item_Orb', it['x'], it['y'])
    for h in L['hazards']:
        t = h['type']; b = dict(x=h['x'], y=h['y'], w=max(h['w'], .5), h=max(h['h'], .5))
        if t == 'fire': add('Hazard_Flame', **b, on=h.get('on'), off=h.get('off'), phase=h.get('phase'))
        elif t == 'trash': add('Hazard_Press', **b, wait=h.get('wait'), slam=h.get('slam'), lift=h.get('lift'), phase=h.get('phase'))
        elif t == 'laser': add('Hazard_Laser', **b, on=h.get('on'), off=h.get('off'), phase=h.get('phase'))
        elif t == 'elec': add('Hazard_Elec', **b, on=h.get('on'), off=h.get('off'), phase=h.get('phase'), column=bool(h.get('column')))
        elif t == 'steam': add('Hazard_Steam', **b, on=h.get('on'), off=h.get('off'), phase=h.get('phase'), dir=h.get('dir') or 0)
        elif t == 'mine': add('Hazard_Mine', h['x'], h['y'])
        elif t == 'void': add('Hazard_Void', **b)
        elif t == 'lava' and h.get('column'): add('Hazard_LavaColumn', **b, on=h.get('on'), off=h.get('off'), phase=h.get('phase'))
        elif t in ('lava', 'spike', 'thorn', 'acid'): add('Hazard_Area', **b, kind=t)
    for sl in L['slopes']:
        x0, x1 = min(sl['x0'], sl['x1']), max(sl['x0'], sl['x1']); y0, y1 = min(sl['y0'], sl['y1']), max(sl['y0'], sl['y1'])
        up = (sl['y1'] < sl['y0']) == (sl['x1'] > sl['x0'])
        add('Slope', x0, y0, x1 - x0, max(.5, y1 - y0), dir='up' if up else 'down', bottom=sl['bottom'])
    ZMAP = {'water': 'Zone_Water', 'wind': 'Zone_Wind', 'current': 'Zone_Current', 'updraft': 'Zone_Updraft', 'flip': 'Zone_GravityFlip',
            'flipcycle': 'Zone_GravityFlip', 'lowgrav': 'Zone_LowGravity', 'well': 'Zone_BlackHole', 'slow': 'Zone_Slow', 'dark': 'Zone_Dark',
            'rain': 'Zone_AcidRain', 'alarm': 'Zone_Alarm', 'mud': 'Zone_Mud', 'ice': 'Zone_Ice', 'elec': 'Zone_Electric'}
    for z in L['zones']:
        n = ZMAP.get(z['type'])
        if not n: continue
        b = dict(x=z['x'], y=z['y'], w=z['w'], h=z['h'])
        add(n, **b, dx=z.get('dx'), dy=z.get('dy'), strength=z.get('strength'), label=z.get('label') or None,
            mode=z['type'] if n == 'Zone_GravityFlip' else None, scale=.42 if n == 'Zone_LowGravity' else None,
            pull=80 if n == 'Zone_BlackHole' else None, power=160 if n == 'Zone_Updraft' else None)
    for l in L['ledges']:
        k = l['kind']; b = dict(x=l['x'], y=l['y'], w=l['w'], h=.5)
        if k == 'move': add('Platform_Moving', **b, axis='x', range=3)
        elif k == 'thrust': add('Platform_Lift', **b, range=3)
        elif k in ('holo', 'holoB'): add('Platform_Phase', **b, phase='A' if k == 'holo' else 'B')
        elif k == 'bounce': add('Platform_Bounce', **b, power=900)
    for c in L['conveyors']: add('Conveyor', c['x'], c['y'], c['w'], .5, speed=c['speed'])
    wall_ids = {}
    for i, w in enumerate(L['walls']):
        if w['type'] in ('stone', 'steel'):
            add('Wall_Breakable', w['x'], w['y'], w['w'], w['h'], breakBy='chargeShot' if w['type'] == 'stone' else 'rideArmor', hp=16 if w['type'] == 'stone' else 24)
        else:
            wall_ids[i] = f'gate{i}'; add('Gate', w['x'], w['y'], max(w['w'], .5), w['h'], kind=w['type'], id=f'gate{i}')
    for s in L['switches']:
        add('Switch', s['x'], s['y'], targets=','.join(wall_ids.get(t, str(t)) for t in s['targets']))
    for i, po in enumerate(L['portals']):
        add('Portal', po['x'], po['y'] - 2.5, id=f'portal{i}', to=(f"portal{po['to']}" if po.get('to') is not None else None), rush=po.get('rush'), alt=po.get('alt'))
    for t in L['turrets']: add('Turret', t['x'], t['y'], hp=t['hp'])
    for v in L['vehicles']: add('Vehicle', v['x'], v['y'] - 2.2, type={'mech': 'rideArmor', 'chaser': 'rideChaser'}[v['type']])
    if L.get('subBoss'):
        sb = L['subBoss']; add('SubBoss', sb['x'], sb['y'], 110 / G, 110 / G, id=sb['id'], hp=sb['hp'])
        if sb.get('gate'): g = sb['gate']; add('Gate', g['x'], g['y'], g['w'], g['h'], kind='subBoss', id='subBossGate')
    add('BossGate', L['bossGateX'], L['floorBoss'] - 4, 1, 4, boss=L['stage'])
    for sp in L.get('specials', []):
        prm = json.dumps(sp, ensure_ascii=False)
        if sp['type'] == 'crusher': add('Hazard_Press', sp['x'], sp['y'], sp['w'], sp['h'], wait=sp['wait'], slam=sp['slam'], lift=sp['lift'], phase=sp['phase'], params=prm)
        elif sp['type'] == 'chaser': add('Hazard_ChaseWall', sp['x'], sp['y'], sp['w'], sp['h'], look=sp.get('look'), speed=sp.get('speed0'), params=prm)
        elif sp['type'] == 'sweep':
            x0, x1 = min(sp['x'], sp['x1']), max(sp['x'], sp['x1']) + sp['w']
            add('Hazard_LaserSweep', x0, sp['y'], x1 - x0, sp['h'], speed=sp['speed'], patrol=bool(sp.get('patrol')), params=prm)
        elif sp['type'] == 'riser': add('Zone_RisingMagma', sp['x'], sp['stop'], sp['w'], sp['bottom'] - sp['stop'], stopY=sp['stop'], params=prm)
    for name, b in L.get('extra', []):
        add(name, **b)

    # ---- IntGrid theo từng phòng ----
    def raster(r):
        W_, H_ = r['w'], r['h']; g = [0] * (W_ * H_)
        def put(x0, y0, x1, y1, v, only_empty=False):
            for cy in range(max(0, math.floor(y0 - r['y'])), min(H_, math.ceil(y1 - r['y']))):
                for cx in range(max(0, math.floor(x0 - r['x'])), min(W_, math.ceil(x1 - r['x']))):
                    if not only_empty or g[cy * W_ + cx] == 0: g[cy * W_ + cx] = v
        for s in L['solids']: put(s['x'], s['y'], s['x'] + s['w'], s['y'] + s['h'], 1)
        for sl in L['slopes']:
            k = abs(sl['y1'] - sl['y0']) / max(1e-6, abs(sl['x1'] - sl['x0'])); val = 2 if k >= .75 else 3
            for cx in range(W_):
                X = r['x'] + cx + .5
                if not (min(sl['x0'], sl['x1']) <= X <= max(sl['x0'], sl['x1'])): continue
                Y = sl['y0'] + (sl['y1'] - sl['y0']) * (X - sl['x0']) / (sl['x1'] - sl['x0'])
                for cy in range(H_):
                    top, bot = r['y'] + cy, r['y'] + cy + 1
                    if bot > Y and top < sl['bottom']:
                        g[cy * W_ + cx] = val if top < Y + 1 and top <= Y else 1
        for l in L['ledges']:
            if l['kind'] in ('shelf', 'safe', 'cart'): put(l['x'], l['y'], l['x'] + l['w'], l['y'] + .5, 4)
            elif l['kind'] == 'break': put(l['x'], l['y'], l['x'] + l['w'], l['y'] + .5, 5)
        for c in L['conveyors']: put(c['x'], c['y'], c['x'] + c['w'], c['y'] + .5, 6)
        for w in L['walls']:
            if w['type'] in ('stone', 'steel'): put(w['x'], w['y'], w['x'] + w['w'], w['y'] + w['h'], 7)
        for h in L['hazards']:
            if h['type'] in ('lava', 'spike', 'thorn', 'acid') and not h.get('column'): put(h['x'], h['y'], h['x'] + h['w'], h['y'] + h['h'], 9)
        for z in L['zones']:  # trần bám được: ô đặc ngay trên vùng đảo trọng lực
            if z['type'] in ('flip', 'flipcycle'):
                for cx in range(W_):
                    X = r['x'] + cx + .5
                    if not (z['x'] <= X < z['x'] + z['w']): continue
                    cy = math.floor(z['y'] - r['y']) - 1
                    if 0 <= cy < H_ and g[cy * W_ + cx] == 1: g[cy * W_ + cx] = 8
        return g

    rule_for = {}
    for r_ in rules: rule_for[(r_['_v'], r_['_i'], r_['_j'])] = r_['uid']
    levels = []
    for ri, r in enumerate(rooms):
        g = raster(r); W_, H_ = r['w'], r['h']
        auto = []
        for cy in range(H_):
            for cx in range(W_):
                v = g[cy * W_ + cx]
                if v in (1, 2, 3, 7, 8):
                    i, j = cx % cw, cy % ch
                    auto.append({'px': [cx * G, cy * G], 'src': [i * G, j * G], 'f': 0, 't': j * cw + i, 'd': [rule_for[(v, i, j)], cy * W_ + cx], 'a': 1})
        lid = ri
        def layer_inst(ldef, **kw):
            return {'__identifier': ldef['identifier'], '__type': ldef['__type'], '__cWid': W_, '__cHei': H_, '__gridSize': G, '__opacity': 1,
                    '__pxTotalOffsetX': 0, '__pxTotalOffsetY': 0, '__tilesetDefUid': ldef['tilesetDefUid'],
                    '__tilesetRelPath': terrain if ldef['tilesetDefUid'] == TS_T else None, 'iid': iid(), 'levelId': lid, 'layerDefUid': ldef['uid'],
                    'pxOffsetX': 0, 'pxOffsetY': 0, 'visible': True, 'optionalRules': [], 'intGridCsv': [], 'autoLayerTiles': [], 'seed': random.randint(1, 9999999),
                    'overrideTilesetUid': None, 'gridTiles': [], 'entityInstances': [], **kw}
        code = r.get('code', r['name'].split()[0])
        ident = ('L%02d_' % ri) + ''.join(ch_ if ch_.isalnum() else '_' for ch_ in code)
        fi = [{'__identifier': 'code', '__type': S, '__value': code, '__tile': None, 'defUid': lvl_fields['code']['uid'], 'realEditorValues': [{'id': 'V_String', 'params': [code]}]},
              {'__identifier': 'difficulty', '__type': I, '__value': r.get('difficulty'), '__tile': None, 'defUid': lvl_fields['difficulty']['uid'], 'realEditorValues': [] if r.get('difficulty') is None else [{'id': 'V_Int', 'params': [r['difficulty']]}]},
              {'__identifier': 'area', '__type': I, '__value': r.get('area'), '__tile': None, 'defUid': lvl_fields['area']['uid'], 'realEditorValues': [] if r.get('area') is None else [{'id': 'V_Int', 'params': [r['area']]}]}]
        bg = (L.get('palette') or {}).get('bg2' if r.get('area') == 2 else 'bg1', '#2a2230')
        if r.get('kind') == 'boss': bg = '#4e1c28'
        elif r.get('kind') == 'mini': bg = '#421e34'
        levels.append({'identifier': ident, 'iid': iid(), 'uid': lid, 'worldX': r['x'] * G, 'worldY': r['y'] * G, 'worldDepth': 0,
                       'pxWid': W_ * G, 'pxHei': H_ * G, '__bgColor': bg, 'bgColor': bg, 'useAutoIdentifier': False, 'bgRelPath': None, 'bgPos': None,
                       'bgPivotX': 0.5, 'bgPivotY': 0.5, '__smartColor': '#adadb5', '__bgPos': None, 'externalRelPath': None, 'fieldInstances': fi,
                       'layerInstances': [layer_inst(layers[0], entityInstances=ents[ri]), layer_inst(layers[1], intGridCsv=g, autoLayerTiles=auto)],
                       '__neighbours': []})
    # láng giềng (chạm cạnh)
    for a, ra in enumerate(rooms):
        for b, rb in enumerate(rooms):
            if a == b: continue
            if ra['x'] + ra['w'] == rb['x'] and ra['y'] < rb['y'] + rb['h'] and rb['y'] < ra['y'] + ra['h']: levels[a]['__neighbours'].append({'levelIid': levels[b]['iid'], 'dir': 'e'})
            if rb['x'] + rb['w'] == ra['x'] and ra['y'] < rb['y'] + rb['h'] and rb['y'] < ra['y'] + ra['h']: levels[a]['__neighbours'].append({'levelIid': levels[b]['iid'], 'dir': 'w'})
    proj = {'__header__': {'fileType': 'LDtk Project JSON', 'app': 'LDtk', 'doc': 'https://ldtk.io/json', 'schema': 'https://ldtk.io/files/JSON_SCHEMA.json',
                           'appAuthor': "Sebastien 'deepnight' Benard", 'appVersion': '1.5.3', 'url': 'https://ldtk.io'},
            'iid': iid(), 'jsonVersion': '1.5.3', 'appBuildId': 473703, 'nextUid': nx() + 1, 'identifierStyle': 'Free', 'toc': [],
            'worldLayout': 'Free', 'worldGridWidth': 256, 'worldGridHeight': 256, 'defaultLevelWidth': 960, 'defaultLevelHeight': 544,
            'defaultPivotX': 0, 'defaultPivotY': 0, 'defaultGridSize': G, 'defaultEntityWidth': G, 'defaultEntityHeight': G,
            'bgColor': '#14121e', 'defaultLevelBgColor': '#2a2230', 'minifyJson': False, 'externalLevels': False, 'exportTiled': False,
            'simplifiedExport': False, 'imageExportMode': 'None', 'exportLevelBg': True, 'pngFilePattern': None, 'backupOnSave': False,
            'backupLimit': 10, 'backupRelPath': None, 'levelNamePattern': '%world_Level_%idx',
            'tutorialDesc': f"{L['name']} ({L['stage']}) — sinh tự động từ thiết kế màn. Collision: 1 đặc · 2 dốc 45° · 3 dốc 22.5° · 4 kệ một chiều · 5 sàn vỡ · 6 băng chuyền · 7 tường nứt · 8 trần bám · 9 dung nham/gai.",
            'customCommands': [], 'flags': [], 'defs': defs, 'levels': levels, 'worlds': [], 'dummyWorldIid': iid()}
    return proj


def main(ids):
    os.makedirs(OUT, exist_ok=True)
    rects, size = build_atlas()
    schema = None
    sp = os.environ.get('LDTK_SCHEMA')
    if sp and os.path.exists(sp):
        import jsonschema
        sc = json.load(open(sp)); schema = sc
    for sid in ids:
        L = adapt_dinorex() if sid == 'x5_dinorex' else json.load(open(os.path.join(REPO, 'levels', 'data', sid + '.json'), encoding='utf8'))
        proj = build_project(L, rects, size)
        if schema:
            import jsonschema
            v = jsonschema.Draft7Validator({**schema, '$ref': '#/LdtkJsonRoot'})
            errs = list(v.iter_errors(proj))
            print(sid, 'schema lỗi:', len(errs), *(f"\n   {'/'.join(map(str, e.absolute_path))}: {e.message[:140]}" for e in errs[:6]))
        open(os.path.join(OUT, sid + '.ldtk'), 'w', encoding='utf8').write(json.dumps(proj, ensure_ascii=False, separators=(',', ':')))
        n_e = sum(len(l['layerInstances'][0]['entityInstances']) for l in proj['levels'])
        print(sid, len(proj['levels']), 'level ·', n_e, 'entity')


if __name__ == '__main__':
    ids = sys.argv[1:] or (['x5_dinorex'] + [s for s in ORDER if os.path.exists(os.path.join(REPO, 'levels', 'data', s + '.json'))])
    main(ids)
