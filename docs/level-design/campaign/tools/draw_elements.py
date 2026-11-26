# Vẽ các element mới (pixel art) dùng chung cho 25 màn: assets/levels/common/el-*.png
# Mỗi sprite vẽ ở độ phân giải gốc (1 ô = 16px), game phóng ×2 khi vẽ. Ảnh nhiều khung xếp ngang.
# Chạy: python3 tools/draw_elements.py   (từ docs/level-design/campaign)
import os, json, math
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
OUT = os.path.join(REPO, 'assets', 'levels', 'common')
OUTLINE = (24, 18, 30, 255)


def img(w, h): return Image.new('RGBA', (w, h), (0, 0, 0, 0))


def sheet(frames):
    w, h = frames[0].size
    s = img(w * len(frames), h)
    for i, f in enumerate(frames): s.paste(f, (i * w, 0))
    return s


def outline(im):
    """Viền tối 1px quanh mọi pixel đặc (kiểu sprite PS)."""
    px = im.load(); w, h = im.size
    o = im.copy(); po = o.load()
    for y in range(h):
        for x in range(w):
            if px[x, y][3] == 0 and any(0 <= x + dx < w and 0 <= y + dy < h and px[x + dx, y + dy][3] > 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                po[x, y] = OUTLINE
    return o


def spike(col=((235, 238, 248), (170, 176, 196), (96, 100, 122)), base=(60, 62, 78)):
    im = img(16, 12); d = ImageDraw.Draw(im)
    d.rectangle([0, 9, 15, 11], fill=base + (255,))
    for cx in (4, 12):
        d.polygon([(cx - 4, 9), (cx, 0), (cx + 3, 9)], fill=col[1] + (255,))
        d.polygon([(cx - 4, 9), (cx, 0), (cx - 1, 9)], fill=col[0] + (255,))
        d.line([(cx + 1, 3), (cx + 3, 9)], fill=col[2] + (255,))
    return outline(im)


def thorn():
    im = img(16, 12); d = ImageDraw.Draw(im)
    d.ellipse([0, 5, 9, 12], fill=(70, 120, 60, 255)); d.ellipse([6, 4, 15, 12], fill=(56, 100, 52, 255))
    for x, y in ((2, 4), (6, 2), (10, 1), (13, 4), (4, 7), (11, 7)):
        d.polygon([(x - 1, y + 3), (x, y), (x + 1, y + 3)], fill=(232, 92, 168, 255))
        d.point((x, y), fill=(255, 190, 230, 255))
    return outline(im)


def mine(f):
    im = img(14, 14); d = ImageDraw.Draw(im)
    d.ellipse([2, 2, 11, 11], fill=(80, 86, 104, 255)); d.ellipse([3, 3, 8, 8], fill=(130, 138, 160, 255))
    for a in range(0, 360, 45):
        x, y = 7 + math.cos(math.radians(a)) * 6, 7 + math.sin(math.radians(a)) * 6
        d.point((round(x), round(y)), fill=(150, 156, 176, 255))
    d.rectangle([6, 6, 7, 7], fill=(255, 70, 70, 255) if f == 0 else (120, 20, 30, 255))
    return outline(im)


def elec(f):
    im = img(16, 8); d = ImageDraw.Draw(im)
    pts = [(0, 4)]
    for x in range(2, 17, 2): pts.append((x, 4 + ((x * 7 + f * 5) % 7) - 3))
    d.line(pts, fill=(255, 250, 170, 255), width=1)
    d.line([(p[0], p[1] + 1) for p in pts], fill=(255, 210, 60, 200), width=1)
    return im


def emitter():
    im = img(10, 8); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 9, 5], fill=(84, 90, 110, 255)); d.rectangle([1, 1, 8, 2], fill=(140, 146, 168, 255))
    d.rectangle([3, 5, 6, 7], fill=(255, 60, 70, 255)); d.point((4, 6), fill=(255, 200, 200, 255))
    return outline(im)


def holo(f):
    im = img(32, 6); d = ImageDraw.Draw(im)
    a = 230 if f == 0 else 110
    d.rectangle([0, 0, 31, 5], fill=(80, 200, 255, a // 3), outline=(170, 240, 255, a))
    for x in range(2, 31, 4): d.line([(x, 1), (x, 4)], fill=(150, 230, 255, a // 2))
    d.line([(1, 1), (30, 1)], fill=(230, 252, 255, a))
    return im


def holoB(f):
    im = holo(f); px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a: px[x, y] = (min(255, b), int(g * .6), 255, a)
    return im


def bounce():
    im = img(24, 12); d = ImageDraw.Draw(im)
    d.rectangle([10, 6, 13, 11], fill=(220, 210, 190, 255))
    d.ellipse([1, 0, 22, 9], fill=(214, 70, 150, 255)); d.ellipse([4, 1, 17, 5], fill=(255, 140, 205, 255))
    for x, y in ((5, 4), (11, 2), (17, 5)): d.ellipse([x, y, x + 2, y + 2], fill=(255, 240, 250, 255))
    return outline(im)


def thruster(f):
    im = img(32, 14); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 31, 4], fill=(110, 116, 136, 255)); d.rectangle([0, 0, 31, 1], fill=(170, 176, 196, 255))
    d.rectangle([4, 5, 9, 6], fill=(70, 74, 90, 255)); d.rectangle([22, 5, 27, 6], fill=(70, 74, 90, 255))
    fl = [7, 5, 6][f]
    for x0 in (5, 23):
        d.polygon([(x0, 7), (x0 + 4, 7), (x0 + 2, 7 + fl)], fill=(255, 160, 40, 255))
        d.polygon([(x0 + 1, 7), (x0 + 3, 7), (x0 + 2, 7 + fl - 2)], fill=(255, 240, 160, 255))
    return outline(im)


def turret(f):
    im = img(16, 16); d = ImageDraw.Draw(im)
    d.rectangle([2, 9, 13, 15], fill=(96, 100, 120, 255)); d.rectangle([3, 10, 12, 11], fill=(150, 156, 176, 255))
    d.ellipse([3, 3, 12, 12], fill=(130, 70, 60, 255)); d.ellipse([5, 5, 9, 9], fill=(255, 140, 60, 255) if f == 0 else (180, 60, 40, 255))
    d.rectangle([7, 0, 8, 4], fill=(70, 74, 90, 255))
    return outline(im)


def orb(f):
    im = img(12, 12); d = ImageDraw.Draw(im)
    r = [5, 4, 5, 6][f]
    d.ellipse([6 - r, 6 - r, 5 + r, 5 + r], fill=(255, 220, 90, 255)); d.ellipse([6 - r + 1, 6 - r + 1, 4, 4], fill=(255, 250, 210, 255))
    return outline(im)


def mud():
    im = img(16, 8); d = ImageDraw.Draw(im)
    d.rectangle([0, 1, 15, 7], fill=(104, 78, 44, 255))
    for x, y in ((2, 2), (7, 4), (12, 2)): d.ellipse([x, y, x + 2, y + 1], fill=(140, 110, 66, 255))
    d.line([(0, 1), (15, 1)], fill=(150, 120, 74, 255))
    return im


def water(f):
    im = img(32, 6); d = ImageDraw.Draw(im)
    pts = [(x, 2 + round(math.sin((x + f * 8) / 32 * 2 * math.pi) * 1.5)) for x in range(0, 33, 2)]
    d.polygon(pts + [(32, 6), (0, 6)], fill=(70, 150, 230, 170)); d.line(pts, fill=(200, 240, 255, 255))
    return im


def gate():
    im = img(16, 16); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 15, 15], fill=(180, 60, 70, 255))
    for y in range(-16, 16, 6): d.polygon([(0, y), (15, y + 8), (15, y + 11), (0, y + 3)], fill=(255, 210, 110, 255))
    d.rectangle([0, 0, 15, 15], outline=(90, 30, 40, 255))
    return im


def laser(f):
    im = img(6, 16); d = ImageDraw.Draw(im)
    d.rectangle([1, 0, 4, 15], fill=(255, 50, 70, 200)); d.rectangle([2, 0, 3, 15], fill=(255, 220, 220, 255))
    for y in range(f * 3 % 16, 16, 6): d.point((2, y), fill=(255, 255, 255, 255))
    return im


SPRITES = {
    'el-spike': spike(), 'el-thorn': thorn(), 'el-mine': sheet([mine(0), mine(1)]), 'el-elec': sheet([elec(f) for f in range(3)]),
    'el-emitter': emitter(), 'el-holo': sheet([holo(0), holo(1)]), 'el-holob': sheet([holoB(0), holoB(1)]), 'el-bounce': bounce(),
    'el-thruster': sheet([thruster(f) for f in range(3)]), 'el-turret': sheet([turret(0), turret(1)]), 'el-orb': sheet([orb(f) for f in range(4)]),
    'el-mud': mud(), 'el-water': sheet([water(f) for f in range(4)]), 'el-gate': gate(), 'el-laser': sheet([laser(f) for f in range(3)]),
}

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for n, im in SPRITES.items():
        im.save(os.path.join(OUT, n + '.png'), optimize=True)
    envp = os.path.join(REPO, 'assets', 'environments', 'environment.json')
    env = json.load(open(envp))
    for n in SPRITES: env['images'][n] = f'assets/levels/common/{n}.png'
    open(envp, 'w').write(json.dumps(env, ensure_ascii=False, separators=(',', ':')))
    # bảng xem trước phóng ×4
    pv = img(560, 30 + 44 * ((len(SPRITES) + 3) // 4)); d = ImageDraw.Draw(pv)
    pv.paste((18, 22, 34, 255), (0, 0, pv.width, pv.height))
    for i, (n, im) in enumerate(SPRITES.items()):
        x, y = 10 + (i % 4) * 138, 10 + (i // 4) * 44
        big = im.resize((im.width * 2, im.height * 2), Image.NEAREST)
        pv.alpha_composite(big.crop((0, 0, min(big.width, 120), big.height)), (x, y + 12))
        d.text((x, y), n, fill=(230, 220, 200, 255))
    pv.save(os.path.join(REPO, 'docs', 'level-design', 'campaign', 'elements-preview.png'))
    print(len(SPRITES), 'sprites')
