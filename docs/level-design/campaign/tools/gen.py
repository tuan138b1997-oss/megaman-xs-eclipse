import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from stages_act2 import STAGES
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
os.makedirs(OUT + '/maps', exist_ok=True)
FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
FT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
T = 6
THEME = {'intro': ((70, 62, 70), (150, 130, 110)), 'metal': ((60, 62, 72), (140, 140, 150)), 'water': ((30, 52, 80), (90, 140, 170)),
         'volt': ((52, 48, 30), (190, 170, 90)), 'nature': ((34, 52, 34), (110, 150, 90)), 'shadow': ((44, 34, 58), (120, 100, 150)),
         'wind': ((48, 62, 80), (170, 190, 210)), 'fire': ((60, 36, 30), (150, 100, 70)), 'ice': ((48, 66, 80), (190, 220, 235)),
         'core': ((58, 30, 52), (170, 110, 160))}
ICON = {'S': ('S', (255, 90, 90), 'Sniper'), 'D': ('D', (255, 160, 60), 'Drone'), 'B': ('B', (230, 80, 80), 'Brute'),
        'M': ('M', (255, 60, 130), 'Mini-boss'), '*': ('★', (255, 70, 70), 'Boss'), 'R': ('R', (120, 255, 140), 'Reploid'),
        'H': ('H', (255, 120, 220), 'Heart Tank'), 'T': ('T', (120, 200, 255), 'Sub-Tank'), 'A': ('A', (120, 230, 255), 'Capsule giáp'),
        'C': ('⚑', (140, 255, 140), 'Checkpoint'), 'V': ('V', (255, 230, 120), 'Ride Armor / Chaser'), 'K': ('K', (255, 255, 120), 'Công tắc')}
HAZ = (255, 120, 40)


def layout(rooms):
    x, floor, out, prev = 0, 40, [], None
    for r in rooms:
        code, name, w, h, d = r[:5]
        if code.endswith('b') and prev is not None:  # branch below the previous room
            px, py, pw, ph = prev
            rect = (px, py + ph + 2, w, h)
            out.append((r, rect)); continue
        if d in ('R', 'A'):
            rect = (x, floor - h, w, h); x += w
        elif d == 'U':
            rect = (x, floor - h, w, h); x += w; floor = floor - h + 14
        else:  # D
            rect = (x, floor - 14, w, h); x += w; floor = floor - 14 + h
        out.append((r, rect)); prev = rect
    ys = [rc[1] for _, rc in out]; miny = min(ys)
    return [(r, (rc[0], rc[1] - miny + 2, rc[2], rc[3])) for r, rc in out]


def draw_stage(sid, st):
    L = layout(st['rooms'])
    W = max(rc[0] + rc[2] for _, rc in L) + 2
    H = max(rc[1] + rc[3] for _, rc in L) + 2
    bg, rock = THEME[st['theme']]
    img = Image.new('RGB', (max(W * T + 120, 900), H * T + 190), (14, 18, 30)); d = ImageDraw.Draw(img)
    for (code, name, w, h, dr, diff, desc, icons, haz), (x, y, ww, hh) in L:
        X, Y, X2, Y2 = x * T, y * T, (x + ww) * T, (y + hh) * T
        col = (90, 30, 50) if code in ('BOSS',) else (70, 40, 60) if code == 'MID' and 'M' in icons else bg
        d.rectangle([X, Y, X2, Y2], fill=col, outline=(130, 130, 150))
        if dr in ('R', 'A'):
            d.rectangle([X, Y2 - 3 * T, X2, Y2], fill=rock)
        else:
            d.rectangle([X, Y, X + 2 * T, Y2], fill=rock); d.rectangle([X2 - 2 * T, Y, X2, Y2], fill=rock)
            if dr == 'U': d.rectangle([X, Y2 - 2 * T, X2, Y2], fill=rock)
        tx = X + (2 * T + 4 if dr in ('U', 'D') else 4)
        d.text((tx, Y + 3), f'{code} {name}', fill=(255, 230, 160), font=FB)
        d.text((tx, Y + 19), f'độ khó {diff}', fill=(200, 200, 210), font=FS)
        if haz:
            d.text((tx, Y + 33), '⚠ ' + haz, fill=HAZ, font=FS)
        gl = [c for c in icons.split() if c in ICON]
        n = len(gl)
        for i, c in enumerate(gl):
            t, ic, _ = ICON[c]
            if dr in ('U', 'D'):
                cx = X + (ww * T) / 2 + (-18 if i % 2 else 18); cy = Y + 60 + (hh * T - 100) * (i + 1) / (n + 1)
            else:
                cx = X + (ww * T) * (i + 1) / (n + 1); cy = Y2 - 3 * T - 16 - (22 if c in 'DH' else 0)
            d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=ic); d.text((cx - 5, cy - 7), t, fill=(0, 0, 0), font=FS)
        ac = (120, 230, 255)
        if dr in ('R', 'A'):
            yy = Y2 - 3 * T - 4; d.line([(X + 6, yy), (X2 - 8, yy)], fill=ac, width=2); d.polygon([(X2 - 4, yy), (X2 - 12, yy - 5), (X2 - 12, yy + 5)], fill=ac)
        elif dr == 'U':
            xx = (X + X2) / 2; d.line([(xx, Y2 - 14), (xx, Y + 50)], fill=ac, width=2); d.polygon([(xx, Y + 44), (xx - 5, Y + 54), (xx + 5, Y + 54)], fill=ac)
        else:
            xx = (X + X2) / 2; d.line([(xx, Y + 50), (xx, Y2 - 20)], fill=ac, width=2); d.polygon([(xx, Y2 - 12), (xx - 5, Y2 - 22), (xx + 5, Y2 - 22)], fill=ac)
    y0 = H * T + 12
    d.text((12, y0), f"{st['title'].upper()} · Boss: {st['boss']} · chủ đề {st['theme']} · {st['act']}", fill=(255, 230, 160), font=FT)
    for i, (k, (t, c, n)) in enumerate(ICON.items()):
        x = 12 + (i % 6) * 150; y = y0 + 34 + (i // 6) * 24
        d.ellipse([x, y, x + 16, y + 16], fill=c); d.text((x + 4, y + 2), t, fill=(0, 0, 0), font=FS); d.text((x + 22, y + 2), n, fill=(220, 220, 220), font=FS)
    d.text((12, y0 + 90), '→ đường chính · ⚠ bẫy chính của phòng · nền tối = khung phòng, dải sáng = sàn/vách · 1 ô = 32px trong game',
           fill=(200, 200, 200), font=FS)
    img.save(f"{OUT}/maps/{sid}.png", optimize=True)
    return img.size


def write_doc(sid, st, size):
    rooms = st['rooms']
    tiles = sum(r[2] for r in rooms if not r[0].endswith('b'))
    lines = [f"# {st['title']} — Boss {st['boss']}", '',
             f"`{sid}` · chủ đề `{st['theme']}` · {st['act']} · tổng chiều ngang khoảng {tiles} ô ({tiles * 32}px)", '',
             f"![Sơ đồ](maps/{sid}.png)", '', '## Ý tưởng', st['concept'], '', '## Tham khảo', st['refs'], '',
             '## Nhịp màn', ' → '.join(f"{r[0]} ({r[5]})" for r in rooms), '', '## Kịch bản từng phòng', '']
    for code, name, w, h, dr, diff, desc, icons, haz in rooms:
        kind = {'R': 'đi ngang', 'U': 'leo dọc', 'D': 'đi xuống', 'A': 'đấu trường'}[dr]
        ent = ', '.join(ICON[c][2] for c in icons.split() if c in ICON)
        lines += [f"### {code} – {name} ({w}×{h} ô, {kind}) · độ khó {diff}", desc]
        if haz: lines.append(f"- **Bẫy:** {haz}")
        if ent: lines.append(f"- **Đặt trong phòng:** {ent}")
        lines.append('')
    if st['secrets']:
        lines += ['## Bí mật và vật phẩm', '| Vật phẩm | Phòng | Cách lấy |', '|---|---|---|']
        lines += [f"| {a} | {b} | {c} |" for a, b, c in st['secrets']]
        lines.append('')
    lines += ['## Cơ chế mới cần engine', *[f'- {m}' for m in st['newMech']], '', '## Hình ảnh / element', st['art'], '']
    open(f"{OUT}/{sid}.md", 'w').write('\n'.join(lines))


order = list(STAGES.keys())
for sid in order:
    sz = draw_stage(sid, STAGES[sid]); write_doc(sid, STAGES[sid], sz); print(sid, sz)

# campaign overview
idx = ['# Kịch bản & sơ đồ toàn chiến dịch', '',
       'Màn mẫu đã duyệt: **Lò Nham Thạch** (`x5_dinorex`) — xem `lo-nham-thach-kich-ban.md`. 25 màn còn lại dùng cùng khung: phòng có mục đích rõ, mỗi màn 1 cơ chế chính + 1 phụ, đoạn dọc, checkpoint giữa, bí mật cần giáp/kỹ năng.', '',
       '## Danh sách màn', '| Màn | Boss | Chủ đề | Cơ chế chính | Độ khó cao nhất | Bí mật |', '|---|---|---|---|---|---|']
idx.insert(5, '')
for sid in order:
    st = STAGES[sid]; mx = max(r[5] for r in st['rooms'] if r[0] != 'BOSS')
    idx.append(f"| [{st['title']}]({sid}.md) | {st['boss']} | {st['theme']} | {', '.join(st['newMech'][:2])} | {mx} | {len(st['secrets'])} |")
idx += ['', '## Giáp / kỹ năng mở bí mật', '| Màn | Bí mật | Cách lấy |', '|---|---|---|']
for sid in order:
    for a, b, c in STAGES[sid]['secrets']:
        if 'Capsule' in a or 'Secret' in a: idx.append(f"| {STAGES[sid]['title']} | {a} ({b}) | {c} |")
open(f"{OUT}/README.md", 'w').write('\n'.join(idx) + '\n')
print('done', len(order))
