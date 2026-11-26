# Cắt sprite gốc X5/X6 trong assets/archive thành dải khung (element) cho game.
#   python3 tools/slice_archive.py index <sheet>   -> ảnh xem trước có đánh số từng khối (scratch)
#   python3 tools/slice_archive.py build           -> ghi assets/levels/common/el-*.png theo bảng ELEMENTS
import os, sys, json
from PIL import Image, ImageDraw
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
ARCH = os.path.join(REPO, 'assets', 'archive')
OUT = os.path.join(REPO, 'assets', 'levels', 'common')


def load(sheet):
    im = Image.open(os.path.join(ARCH, sheet)).convert('RGBA')
    a = np.array(im)
    if (a[..., 3] == 0).mean() < 0.05:  # nền đặc: lấy màu góc làm màu trong suốt
        bg = a[0, 0, :3]
        a[(a[..., :3] == bg).all(-1)] = 0
    return Image.fromarray(a)


def blobs(im, gap=2, min_area=12):
    a = np.array(im)[..., 3] > 0
    h, w = a.shape
    lab = np.zeros((h, w), int); n = 0; boxes = []
    for y in range(h):
        for x in range(w):
            if a[y, x] and not lab[y, x]:
                n += 1; st = [(y, x)]; lab[y, x] = n; x0 = x1 = x; y0 = y1 = y; cnt = 0
                while st:
                    cy, cx = st.pop(); cnt += 1
                    x0, x1, y0, y1 = min(x0, cx), max(x1, cx), min(y0, cy), max(y1, cy)
                    for dy in range(-gap, gap + 1):
                        for dx in range(-gap, gap + 1):
                            ny, nx = cy + dy, cx + dx
                            if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not lab[ny, nx]:
                                lab[ny, nx] = n; st.append((ny, nx))
                if cnt >= min_area: boxes.append((x0, y0, x1 + 1, y1 + 1))
    boxes.sort(key=lambda b: (b[1] // 12, b[0]))
    return boxes


def index(sheet, out):
    im = load(sheet); bx = blobs(im)
    k = 3 if im.width < 400 else 2
    pv = Image.new('RGBA', (im.width * k, im.height * k), (40, 44, 60, 255))
    pv.alpha_composite(im.resize(pv.size, Image.NEAREST)); d = ImageDraw.Draw(pv)
    for i, (x0, y0, x1, y1) in enumerate(bx):
        d.rectangle([x0 * k, y0 * k, x1 * k, y1 * k], outline=(255, 80, 80, 255)); d.text((x0 * k + 1, y0 * k + 1), str(i), fill=(255, 255, 0, 255))
    pv.save(out); print(sheet, im.size, len(bx), 'khối'); return bx


def strip(sheet, ids, pad_to=None, align='bottom'):
    """Ghép các khối đã chọn thành dải ngang, mọi khung cùng kích thước (canh đáy, giữa)."""
    im = load(sheet); bx = blobs(im)
    cr = [im.crop(bx[i]) for i in ids]
    w = max(c.width for c in cr); h = max(c.height for c in cr)
    if pad_to: w, h = max(w, pad_to[0]), max(h, pad_to[1])
    s = Image.new('RGBA', (w * len(cr), h), (0, 0, 0, 0))
    for i, c in enumerate(cr):
        y = h - c.height if align == 'bottom' else (h - c.height) // 2
        s.paste(c, (i * w + (w - c.width) // 2, y), c)
    return s


if __name__ == '__main__':
    if sys.argv[1] == 'index':
        index(sys.argv[2], sys.argv[3])


# ---------- bảng element: (tên, sheet, cách lấy) ----------
def crop(sheet, box, flip=False):
    c = load(sheet).crop(box)
    return c.transpose(Image.FLIP_TOP_BOTTOM) if flip else c


def boxes_strip(sheet, ids, gap=1, align='bottom'):
    im = load(sheet); bx = blobs(im, gap=gap)
    cr = [im.crop(bx[i]) for i in ids]
    w = max(c.width for c in cr); h = max(c.height for c in cr)
    s = Image.new('RGBA', (w * len(cr), h), (0, 0, 0, 0))
    for i, c in enumerate(cr):
        s.paste(c, (i * w + (w - c.width) // 2, h - c.height if align == 'bottom' else (h - c.height) // 2), c)
    return s


def fade(im, a):
    arr = np.array(im); arr[..., 3] = (arr[..., 3] * a).astype(np.uint8); return Image.fromarray(arr)


def hstack(frames):
    w = max(f.width for f in frames); h = max(f.height for f in frames)
    s = Image.new('RGBA', (w * len(frames), h), (0, 0, 0, 0))
    for i, f in enumerate(frames): s.paste(f, (i * w + (w - f.width) // 2, h - f.height), f)
    return s


def atlas_strip(name):
    meta = json.load(open(os.path.join(REPO, 'assets', 'atlas.json')))[name]
    im = Image.open(os.path.join(REPO, 'assets', name + '.png')).convert('RGBA')
    return hstack([im.crop((r['x'], r['y'], r['x'] + r['w'], r['y'] + r['h'])) for r in meta['rects']])


def thruster():
    plat = crop('x6/Misc/Misc/mmx6-platform.gif', (13, 20, 59, 40))
    big = crop('x6/Misc/Misc/mmx6_probe_8201-u_type.gif', (117, 20, 132, 50)).transpose(Image.FLIP_TOP_BOTTOM)
    fire = [big.resize((9, h), Image.NEAREST) for h in (16, 12, 14)]
    frames = []
    for i in range(3):
        f = Image.new('RGBA', (46, 36), (0, 0, 0, 0))
        for x in (9, 28): fl = fire[(i + x // 20) % 3]; f.paste(fl, (x, 18), fl)
        f.paste(plat, (0, 0), plat)
        frames.append(f)
    return hstack(frames)


def holo(sheet, box):
    top = crop(sheet, box)
    return hstack([top, fade(top, .35)])


def tint(im, rgb, keep=0.35):
    a = np.array(im).astype(float); lum = a[..., :3].mean(-1, keepdims=True) / 255
    a[..., :3] = a[..., :3] * keep + lum * np.array(rgb) * (1 - keep) * 1.25
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


ELEMENTS = {
    'el-spike': lambda: crop('x5/Misc/Misc/mmx5_spikeplat.gif', (13, 68, 77, 83), flip=True),
    'el-thorn': lambda: tint(crop('x5/Misc/Misc/mmx5_spikeplat.gif', (13, 68, 77, 83), flip=True), (230, 70, 170)),
    'el-spike-ceil': lambda: crop('x5/Misc/Misc/mmx5_spikeplat.gif', (13, 68, 77, 83)),
    'el-holo': lambda: holo('x6/Misc/Misc/mmx6_cyberblock.gif', (3, 4, 67, 24)),
    'el-holob': lambda: holo('x5/Misc/MiscBack/mmx5_cyberblock.gif', (44, 3, 92, 21)),
    'el-platform': lambda: crop('x6/Misc/Misc/mmx6-platform.gif', (13, 20, 59, 40)),
    'el-thruster': thruster,
    'el-crumble': lambda: crop('x5/Misc/MiscBack/mmx5_bridge.gif', (417, 95, 545, 127)),
    'el-gate': lambda: crop('x5/Misc/MiscBack/mmx5_destructabledoors.gif', (8, 29, 31, 101)),
    'el-orbgate': lambda: crop('x5/Misc/MiscBack/mmx5_energyspheres_door.gif', (188, 3, 220, 83)),
    'el-orb': lambda: boxes_strip('x5/Misc/MiscBack/mmx5_energyspheres_door.gif', [9, 10, 11, 12], align='center'),
    'el-switch': lambda: boxes_strip('x5/Misc/Misc/mmx5_trigger.gif', [0, 1, 2]),
    'el-teleporter': lambda: boxes_strip('x6/Misc/Misc/mmx6-teleporter.gif', [0, 1, 2]),
    'el-probe': lambda: boxes_strip('x6/Misc/Misc/mmx6_probe_8201-u_type.gif', [0, 1, 2]),
    'el-fireball': lambda: boxes_strip('x6/Misc/Misc/mmx6-fireball.gif', [0, 1, 2], align='center'),
    'el-mine': lambda: boxes_strip('x5/Enemy/mmx5_timebomb.gif', [0, 1, 2, 3, 4, 5], gap=2),
    'el-explode': lambda: boxes_strip('x5/Enemy/mmx5_timebomb.gif', [13, 14, 15, 16, 17], gap=2, align='center'),
    'el-turret': lambda: boxes_strip('x6/Enemy/mmx6-laser.gif', [0, 1, 2, 3, 4], gap=2, align='center'),
    'el-laser': lambda: crop('x5/Enemy/mmm-mmx5minilaser.gif', (80, 7, 100, 37)),
    'el-wall-steel': lambda: boxes_strip('x5/Misc/MiscBack/mmx5_destructablewalls.gif', [2]),
    'el-wall-stone': lambda: boxes_strip('x5/Misc/MiscBack/mmx5_v-block.gif', [0]),
    'el-ice': lambda: boxes_strip('x6/Misc/Misc/mmx6_invertediceblocks.gif', [0]),
    'el-elec': lambda: hstack([crop('x5/Enemy/mmm-mmx5minilaser.gif', (6 + i * 27.6, 44, 6 + (i + 1) * 27.6, 59)) for i in range(5)]),
}


def build(names=None):
    os.makedirs(OUT, exist_ok=True); made = {}
    for n, fn in ELEMENTS.items():
        if names and n not in names: continue
        im = fn(); im.save(os.path.join(OUT, n + '.png'), optimize=True); made[n] = im
        print(n, im.size)
    envp = os.path.join(REPO, 'assets', 'environments', 'environment.json')
    env = json.load(open(envp))
    for n in made: env['images'][n] = f'assets/levels/common/{n}.png'
    open(envp, 'w').write(json.dumps(env, ensure_ascii=False, separators=(',', ':')))
    return made


if __name__ == '__main__' and sys.argv[1] == 'build':
    made = build(sys.argv[2:] or None)
    W = 1100; pv = Image.new('RGBA', (W, 1400), (24, 28, 40, 255)); d = ImageDraw.Draw(pv); x = y = row = 0
    for n, im in made.items():
        big = im.resize((im.width * 2, im.height * 2), Image.NEAREST)
        if x + big.width > W: x = 0; y += row + 22; row = 0
        d.text((x, y), n, fill=(255, 225, 150, 255)); pv.alpha_composite(big, (x, y + 14)); x += big.width + 16; row = max(row, big.height + 14)
    pv.crop((0, 0, W, y + row + 6)).save(os.path.join(REPO, 'docs', 'level-design', 'campaign', 'elements-preview.png'))
