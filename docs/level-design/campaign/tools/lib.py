# Bộ vẽ sơ đồ + sinh kịch bản cho các màn, theo chuẩn màn mẫu Lò Nham Thạch.
# Tọa độ: ô (1 ô = 32px trong game), gốc trên-trái thế giới, y tăng xuống dưới.
# Hình học trong phòng dùng tọa độ TƯƠNG ĐỐI so với góc trên-trái của phòng.
import os
from PIL import Image, ImageDraw, ImageFont

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FB = ImageFont.truetype(FONTB, 12)
FS = ImageFont.truetype(FONT, 10)
FT = ImageFont.truetype(FONTB, 15)
FI = ImageFont.truetype(FONTB, 10)
T = 5  # px mỗi ô trên sơ đồ

# ---------- hình học (hàm tạo) ----------
def F(*pts): return ('floor', pts)            # đường mặt đất, None = cắt đoạn (hố)
def C(*pts): return ('ceil', pts)             # đường trần
def B(x, y, w, h): return ('block', x, y, w, h)
def H(kind, x, y, w, h): return ('haz', kind, x, y, w, h)
def P(x, y, w, kind='shelf'): return ('plat', kind, x, y, w)   # kind: shelf|move|break|safe|bounce|thrust|holo
def CV(x, y, w, d): return ('conv', x, y, w, d)
def CW(x, y, h): return ('crack', x, y, h)
def BAR(x, y, w, h, col='lava'): return ('bar', col, x, y, w, h)
def Z(kind, x, y, w, h, label=''): return ('zone', kind, x, y, w, h, label)
def AR(x, y, dx, dy, col='wind'): return ('arrow', col, x, y, dx, dy)
def X(x, y, text): return ('text', x, y, text)
def E(code, x, y): return ('ent', code, x, y)
def PATH(*pts): return ('path', pts)
def ALT(*pts): return ('alt', pts)


def Room(code, name, x, y, w, h, diff, geo, text, area=1, kind=None):
    return dict(code=code, name=name, x=x, y=y, w=w, h=h, diff=diff, geo=geo, text=text.strip('\n'), area=area,
                kind=kind or ('boss' if code == 'BOSS' else 'mini' if code == 'MID' else None))

# ---------- màu ----------
HAZ = {'lava': (255, 110, 30), 'water': (40, 105, 190), 'spike': (215, 215, 230), 'elec': (255, 235, 80),
       'void': (8, 10, 18), 'thorn': (200, 60, 140), 'mud': (115, 85, 45), 'laser': (255, 50, 60),
       'acid': (130, 220, 60), 'ice': (170, 225, 255), 'snow': (235, 240, 250), 'fire': (255, 150, 40),
       'trash': (120, 110, 90), 'dark': (25, 15, 35), 'steam': (230, 230, 230), 'mine': (255, 80, 80)}
HAZ_NAME = {'lava': 'Dung nham', 'water': 'Nước', 'spike': 'Gai', 'elec': 'Điện', 'void': 'Vực (rơi = mất mạng)',
            'thorn': 'Bụi gai độc', 'mud': 'Bùn (làm chậm)', 'laser': 'Tia laser', 'acid': 'Axit', 'ice': 'Băng trơn',
            'snow': 'Tuyết', 'fire': 'Lửa', 'trash': 'Rác/khối nghiền', 'dark': 'Vùng tối', 'steam': 'Hơi nóng', 'mine': 'Thủy lôi / mìn'}
ZONE = {'wind': (150, 210, 255), 'slow': (190, 140, 255), 'water': (90, 160, 230), 'dark': (140, 110, 170),
        'grav': (255, 120, 220), 'current': (90, 200, 230), 'updraft': (160, 240, 200), 'alarm': (255, 90, 90),
        'rain': (130, 220, 60), 'elec': (255, 235, 80)}
ZONE_NAME = {'wind': 'Vùng gió', 'slow': 'Vùng làm chậm', 'water': 'Vùng ngập nước', 'dark': 'Vùng tối',
             'grav': 'Vùng hút / đổi trọng lực', 'current': 'Dòng chảy', 'updraft': 'Luồng khí nâng', 'alarm': 'Vùng đèn pha',
             'rain': 'Mưa axit', 'elec': 'Vùng điện'}
PLAT = {'shelf': ((205, 175, 125), 'Bệ / kệ'), 'move': ((120, 220, 255), 'Bệ di động'), 'break': ((230, 140, 80), 'Sàn vỡ / sập'),
        'safe': ((110, 240, 140), 'Kệ an toàn'), 'bounce': ((255, 140, 220), 'Bệ bật nhảy'), 'thrust': ((255, 200, 90), 'Bệ phản lực'),
        'holo': ((160, 230, 255), 'Bệ hologram ẩn hiện')}
ICON = {'S': ('S', (255, 90, 90), 'Sniper'), 'D': ('D', (255, 160, 60), 'Drone'), 'B': ('B', (230, 80, 80), 'Brute'),
        'M': ('M', (255, 60, 130), 'Mini-boss'), '*': ('★', (255, 70, 70), 'Boss'), 'R': ('R', (120, 255, 140), 'Reploid cứu'),
        'H': ('H', (255, 120, 220), 'Heart Tank'), 'T': ('T', (120, 200, 255), 'Sub-Tank'), 'A': ('A', (120, 230, 255), 'Capsule giáp'),
        'C': ('⚑', (140, 255, 140), 'Checkpoint'), 'V': ('V', (255, 230, 120), 'Ride Armor / Chaser'), 'K': ('K', (255, 255, 120), 'Công tắc'),
        'O': ('o', (255, 240, 160), 'Quả năng lượng'), 'G': ('G', (200, 200, 255), 'Cổng dịch chuyển'),
        'W': ('W', (255, 200, 80), 'Ống phun / tháp pháo')}
PATHC = (120, 230, 255)
ALTC = (255, 130, 220)


def _poly_from_line(pts, ox, oy, edge_y):
    segs, cur = [], []
    for p in pts:
        if p is None:
            if cur: segs.append(cur); cur = []
        else:
            cur.append(p)
    if cur: segs.append(cur)
    out = []
    for s in segs:
        poly = [((ox + x) * T, (oy + y) * T) for x, y in s]
        poly += [((ox + s[-1][0]) * T, edge_y), ((ox + s[0][0]) * T, edge_y)]
        out.append(poly)
    return out


def _arrow(d, x1, y1, x2, y2, col, w=2, dash=False):
    import math
    if dash:
        L = math.hypot(x2 - x1, y2 - y1); n = max(1, int(L / 8))
        for i in range(0, n, 2):
            a, b = i / n, min(1, (i + 1) / n)
            d.line([(x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)], fill=col, width=w)
    else:
        d.line([(x1, y1), (x2, y2)], fill=col, width=w)
    ang = math.atan2(y2 - y1, x2 - x1)
    s = 7
    d.polygon([(x2, y2), (x2 - s * math.cos(ang - .45), y2 - s * math.sin(ang - .45)),
               (x2 - s * math.cos(ang + .45), y2 - s * math.sin(ang + .45))], fill=col)


def _polyline(d, pts, ox, oy, col, dash=False):
    P2 = [((ox + x) * T, (oy + y) * T) for x, y in pts]
    for i in range(len(P2) - 1):
        (a, b), (c, e) = P2[i], P2[i + 1]
        if i == len(P2) - 2:
            _arrow(d, a, b, c, e, col, 2, dash)
        elif dash:
            _arrow(d, a, b, c, e, col, 2, True) if False else None
            import math
            L = math.hypot(c - a, e - b); n = max(1, int(L / 8))
            for k in range(0, n, 2):
                u, v = k / n, min(1, (k + 1) / n)
                d.line([(a + (c - a) * u, b + (e - b) * u), (a + (c - a) * v, b + (e - b) * v)], fill=col, width=2)
        else:
            d.line([(a, b), (c, e)], fill=col, width=2)


def _overlap(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def draw(st, out_png):
    rooms = st['rooms']
    pad = 3
    minx = min(r['x'] for r in rooms) - pad; miny = min(r['y'] for r in rooms) - pad - 12
    maxx = max(r['x'] + r['w'] for r in rooms) + pad; maxy = max(r['y'] + r['h'] for r in rooms) + pad
    W, Hh = (maxx - minx) * T, (maxy - miny) * T
    th = st['theme']
    img = Image.new('RGB', (max(W + 140, 1100), Hh + 175), (14, 18, 30))
    d = ImageDraw.Draw(img, 'RGBA')
    used = {'haz': set(), 'zone': set(), 'plat': set(), 'ent': set(), 'conv': False, 'crack': False, 'alt': False}
    labels = []
    # pass 1: rooms + geometry
    for r in rooms:
        ox, oy = r['x'] - minx, r['y'] - miny
        X0, Y0, X1, Y1 = ox * T, oy * T, (ox + r['w']) * T, (oy + r['h']) * T
        bg = th['bg%d' % r['area']]
        if r['kind'] == 'boss': bg = (78, 28, 40)
        elif r['kind'] == 'mini': bg = (66, 30, 52)
        d.rectangle([X0, Y0, X1, Y1], fill=bg)
        rock = th['rock%d' % r['area']]
        for g in r['geo']:
            t = g[0]
            if t == 'floor':
                for poly in _poly_from_line(g[1], ox, oy, Y1): d.polygon(poly, fill=rock)
            elif t == 'ceil':
                for poly in _poly_from_line(g[1], ox, oy, Y0): d.polygon(poly, fill=rock)
            elif t == 'block':
                _, x, y, w, h = g; d.rectangle([(ox + x) * T, (oy + y) * T, (ox + x + w) * T - 1, (oy + y + h) * T - 1], fill=rock)
            elif t == 'zone':
                _, k, x, y, w, h, lab = g; c = ZONE[k]; used['zone'].add(k)
                d.rectangle([(ox + x) * T, (oy + y) * T, (ox + x + w) * T, (oy + y + h) * T], fill=c + (40,), outline=c + (150,))
                if lab: d.text(((ox + x) * T + 3, (oy + y) * T + 2), lab, fill=c, font=FS)
    for r in rooms:
        ox, oy = r['x'] - minx, r['y'] - miny
        for g in r['geo']:
            t = g[0]
            if t == 'haz':
                _, k, x, y, w, h = g; used['haz'].add(k); c = HAZ[k]
                a, b, c2, e = (ox + x) * T, (oy + y) * T, (ox + x + w) * T, (oy + y + h) * T
                if k == 'spike' or k == 'thorn':
                    d.rectangle([a, b + 2, c2, e], fill=(60, 60, 70) if k == 'spike' else (90, 30, 60))
                    n = max(1, int((c2 - a) / 6))
                    for i in range(n):
                        sx = a + (c2 - a) * i / n; sw = (c2 - a) / n
                        d.polygon([(sx, e), (sx + sw / 2, b), (sx + sw, e)], fill=c)
                elif k == 'water':
                    d.rectangle([a, b, c2, e], fill=c + (150,)); d.line([(a, b), (c2, b)], fill=(140, 200, 255), width=2)
                elif k == 'laser':
                    d.rectangle([a, b, c2, e], fill=c + (170,))
                elif k == 'mine':
                    d.ellipse([a - 2, b - 2, c2 + 2, e + 2], fill=c, outline=(255, 220, 220))
                elif k == 'void':
                    d.rectangle([a, b, c2, e], fill=c)
                    d.text((a + 2, e - 12), '▼', fill=(120, 120, 140), font=FS)
                else:
                    d.rectangle([a, b, c2, e], fill=c)
            elif t == 'bar':
                _, k, x, y, w, h = g; c = HAZ.get(k, (170, 170, 190)) if k in HAZ else (170, 170, 190); used['haz'].add(k) if k in HAZ else None
                d.rectangle([(ox + x) * T, (oy + y) * T, (ox + x + w) * T, (oy + y + h) * T], fill=c)
            elif t == 'plat':
                _, k, x, y, w = g; used['plat'].add(k); c = PLAT[k][0]
                a, b, c2 = (ox + x) * T, (oy + y) * T, (ox + x + w) * T
                if k == 'holo':
                    d.rectangle([a, b, c2, b + 3], outline=c, width=1)
                else:
                    d.rectangle([a, b, c2, b + 3], fill=c)
                if k == 'move': d.text((c2 + 1, b - 5), '↔', fill=c, font=FS)
                if k == 'break':
                    for i in range(int(a), int(c2), 6): d.line([(i, b), (i + 3, b + 3)], fill=(40, 20, 10))
            elif t == 'conv':
                _, x, y, w, dr = g; used['conv'] = True
                a, b, c2 = (ox + x) * T, (oy + y) * T, (ox + x + w) * T
                d.rectangle([a, b, c2, b + 4], fill=(90, 95, 110))
                for i in range(int(a) + 4, int(c2) - 4, 14):
                    d.text((i, b - 12), '←' if dr < 0 else '→', fill=(255, 210, 90), font=FS)
            elif t == 'crack':
                _, x, y, h = g; used['crack'] = True
                a, b = (ox + x) * T, (oy + y) * T
                d.rectangle([a, b, a + 2 * T, b + h * T], fill=(150, 130, 110))
                for i in range(int(h * T / 6)):
                    d.line([(a + (2 if i % 2 else 8), b + i * 6), (a + (8 if i % 2 else 2), b + i * 6 + 6)], fill=(50, 30, 20), width=2)
            elif t == 'arrow':
                _, k, x, y, dx, dy = g; c = ZONE.get(k, (220, 220, 220))
                _arrow(d, (ox + x) * T, (oy + y) * T, (ox + x + dx) * T, (oy + y + dy) * T, c, 2)
            elif t == 'path':
                _polyline(d, g[1], ox, oy, PATHC)
            elif t == 'alt':
                used['alt'] = True; _polyline(d, g[1], ox, oy, ALTC, dash=True)
    # pass 2: text + entities + labels on top
    for r in rooms:
        ox, oy = r['x'] - minx, r['y'] - miny
        for g in r['geo']:
            if g[0] == 'text':
                _, x, y, s = g
                d.text(((ox + x) * T, (oy + y) * T), s, fill=(235, 225, 210), font=FS)
            elif g[0] == 'ent':
                _, c, x, y = g; used['ent'].add(c)
                cx, cy = (ox + x) * T, (oy + y) * T; t_, col, _ = ICON[c]
                rr = 7 if c != 'O' else 4
                d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col, outline=(0, 0, 0))
                if c != 'O':
                    tw = d.textlength(t_, font=FI); d.text((cx - tw / 2, cy - 6), t_, fill=(0, 0, 0), font=FI)
    for r in rooms:
        ox, oy = r['x'] - minx, r['y'] - miny
        X0, Y0, X1, Y1 = ox * T, oy * T, (ox + r['w']) * T, (oy + r['h']) * T
        d.rectangle([X0, Y0, X1, Y1], outline=(150, 150, 170))
        title = f"{r['code']} {r['name']}"
        sub = f"độ khó {r['diff']}" if r['code'] != 'BOSS' else 'boss'
        tw = max(d.textlength(title, font=FB), d.textlength(sub, font=FS)) + 6
        rects = [((r2['x'] - minx) * T, (r2['y'] - miny) * T, (r2['x'] - minx + r2['w']) * T, (r2['y'] - miny + r2['h']) * T)
                 for r2 in rooms if r2 is not r]
        lx = X0 + 1
        cands = [Y0 - 30 - k * 30 for k in range(6)] + [Y0 + 2 + k * 10 for k in range(30)]
        box = None
        opts = [(ly, dx) for ly in cands[:6] for dx in (0, 60, 130, 200) if dx + tw < max(r['w'] * T, tw + 1) + 40] + [(ly, 0) for ly in cands[6:]]
        for ly, dx in opts:
            b = [lx - 1 + dx, ly, lx + tw + dx, ly + 28]
            if b[1] < 0: continue
            if any(_overlap(b, o) for o in labels) or any(_overlap(b, o) for o in rects): continue
            box = b; break
        if box is None: box = [lx - 1, Y0 + 2, lx + tw, Y0 + 30]
        ly = box[1]; lx = box[0] + 1
        if box[3] <= Y0:
            d.line([(lx + 3, box[3]), (lx + 3, Y0)], fill=(150, 150, 170))
        labels.append(box)
        d.rectangle(box, fill=(10, 12, 22, 200))
        d.text((lx, ly), title, fill=(255, 225, 150), font=FB)
        d.text((lx, ly + 14), sub, fill=(200, 200, 215), font=FS)
    # legend
    y0 = Hh + 10
    d.text((12, y0), f"{st['title'].upper()} · Boss: {st['boss']} · {st['act']} · 1 ô = 32px · khung hình 30×17 ô · tổng ~{maxx - minx - 2 * pad}×{maxy - miny - 2 * pad - 12} ô",
           fill=(255, 225, 150), font=FT)
    d.text((12, y0 + 20), st['subtitle'], fill=(200, 200, 210), font=FS)
    items = []
    for c in ICON:
        if c in used['ent']: items.append(('ent', c))
    for k in sorted(used['haz']): items.append(('haz', k))
    for k in sorted(used['zone']): items.append(('zone', k))
    for k in PLAT:
        if k in used['plat']: items.append(('plat', k))
    if used['conv']: items.append(('conv', None))
    if used['crack']: items.append(('crack', None))
    items.append(('path', None))
    if used['alt']: items.append(('alt', None))
    for i, (t, k) in enumerate(items):
        x = 12 + (i % 7) * 175; y = y0 + 42 + (i // 7) * 22
        if t == 'ent':
            tt, col, n = ICON[k]; d.ellipse([x, y, x + 14, y + 14], fill=col)
            tw = d.textlength(tt, font=FI); d.text((x + 7 - tw / 2, y + 1), tt, fill=(0, 0, 0), font=FI)
        elif t == 'haz':
            d.rectangle([x, y, x + 14, y + 14], fill=HAZ[k]); n = HAZ_NAME[k]
        elif t == 'zone':
            c = ZONE[k]; d.rectangle([x, y, x + 14, y + 14], fill=c + (70,), outline=c); n = ZONE_NAME[k]
        elif t == 'plat':
            c, n = PLAT[k]; d.rectangle([x, y + 5, x + 14, y + 9], fill=c)
        elif t == 'conv':
            d.rectangle([x, y + 5, x + 14, y + 9], fill=(90, 95, 110)); n = 'Băng chuyền'
        elif t == 'crack':
            d.rectangle([x + 3, y, x + 11, y + 14], fill=(150, 130, 110)); n = 'Tường nứt (phá được)'
        elif t == 'path':
            d.line([(x, y + 7), (x + 14, y + 7)], fill=PATHC, width=2); n = 'Đường chính'
        elif t == 'alt':
            d.line([(x, y + 7), (x + 5, y + 7)], fill=ALTC, width=2); d.line([(x + 9, y + 7), (x + 14, y + 7)], fill=ALTC, width=2); n = 'Lối bí mật'
        d.text((x + 20, y + 1), n, fill=(220, 220, 225), font=FS)
    img.save(out_png, optimize=True)
    return img.size


# ---------- kịch bản ----------
ITEM_ORDER = ['S', 'D', 'B', 'W', 'M', 'R', 'H', 'T', 'A', 'V', 'K', 'G', 'C']


def write_md(sid, st, out_md, map_rel):
    rooms = st['rooms']
    L = [f"# Màn: {st['title'].upper()} ({st['en']} — Boss {st['boss']})", '',
         f"Bản thiết kế để duyệt trước khi dựng. Sơ đồ: `{map_rel}`.",
         f"Màn này thay cho `{sid}` hiện tại. {st['keep']}", '', '![Sơ đồ](' + map_rel + ')', '', '---', '',
         '## 0. Công cụ và quy ước', '',
         'Dùng chung với màn mẫu (`../lo-nham-thach-kich-ban.md`, mục 0): LDtk dựng bản đồ, Pixelorama vẽ tile, Krita vẽ nền parallax. '
         '1 ô = 32px, khung hình 30×17 ô, các lớp `Collision` / `Tiles` / `Decor` / `Foreground` / `Entities`.']
    if st.get('conv_extra'): L += ['', st['conv_extra']]
    L += ['', '---', '', '## 1. Ý tưởng tổng', '', st['concept'], '']
    for a in st['areas']: L.append(f"- {a}")
    L += [f"- **Điểm nhấn trải nghiệm:** {st['flow']}",
          f"- **Đường cong độ khó:** {' → '.join(('(mini-boss)' if r['kind'] == 'mini' else 'boss' if r['kind'] == 'boss' else str(r['diff'])) for r in rooms)} (thang 10).",
          f"- **Thời lượng mục tiêu:** {st['time']}.", '', 'Các mẫu thiết kế tham khảo (không chép bản đồ gốc):', '']
    for rf in st['refs']: L.append(f"- {rf}")
    L += ['', '---', '', '## 2. Kịch bản từng phòng', '', 'Tọa độ tính theo ô, gốc (0,0) ở góc trên trái thế giới, y tăng xuống dưới.', '']
    for r in rooms:
        head = r['code'] if r['code'] in ('BOSS', 'MID') else r['code']
        nm = 'Mini-boss – ' + r['name'] if r['kind'] == 'mini' else ('BOSS – ' + r['name'] if r['kind'] == 'boss' else f"{head} – {r['name']}")
        coord = f"x {r['x']}–{r['x'] + r['w']}, y {r['y']}–{r['y'] + r['h']}"
        dif = '' if r['kind'] == 'boss' else f" · độ khó {r['diff']}"
        L += [f"### {nm} ({coord}){dif}", r['text'], '']
    # bảng
    L += ['---', '', '## 3. Bảng vật phẩm và kẻ địch', '', '| Loại | Số lượng | Vị trí |', '|---|---|---|']
    cnt = {}
    for r in rooms:
        for g in r['geo']:
            if g[0] == 'ent' and g[1] != 'O':
                cnt.setdefault(g[1], {}); cnt[g[1]][r['code']] = cnt[g[1]].get(r['code'], 0) + 1
    names = dict(ICON); names['C'] = ('', '', 'Checkpoint'); names['A'] = ('', '', 'Capsule ' + st['capsule'])
    for c in ITEM_ORDER:
        if c not in cnt: continue
        n = sum(cnt[c].values())
        pos = ', '.join(f"{k}" + (f" ×{v}" if v > 1 else '') for k, v in cnt[c].items())
        L.append(f"| {names[c][2]} | {n} | {pos} |")
    for extra in st.get('table_extra', []): L.append(extra)
    ne = sum(sum(cnt.get(c, {}).values()) for c in 'SDB')
    L += ['', f"Tổng {ne} kẻ địch thường (bản cũ: 20 con xếp đều), đặt có chủ đích theo mục đích từng phòng.", '',
          '---', '', '## 4. Những gì engine cần bổ sung', '']
    for i, m in enumerate(st['engine'], 1): L.append(f"{i}. {m}")
    L += ['', '## 5. Danh sách hình cần vẽ', '']
    for a in st['art']: L.append(f"- {a}")
    L += ['', '**Hướng phối hợp:** như màn mẫu — dựng bằng khối màu tạm theo sơ đồ để chơi thử, chốt cảm giác rồi mới thay tile thật.', '']
    open(out_md, 'w').write('\n'.join(L))
