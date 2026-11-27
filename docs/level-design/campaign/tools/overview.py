"""Ghép 25 sơ đồ trong maps/ thành tong-quan-25-man.png (3 cột, theo thứ tự trong README)."""
import os, re, sys
from PIL import Image, ImageDraw, ImageFont
root = sys.argv[1] if len(sys.argv) > 1 else '.'
order = re.findall(r'\]\((\w+)\.md\)', open(os.path.join(root, 'README.md'), encoding='utf-8').read())
FT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
CW, PAD, COLS = 740, 20, 3
tiles = []
for sid in order:
    im = Image.open(os.path.join(root, 'maps', sid + '.png')).convert('RGB')
    im = im.crop((0, 0, im.width, im.height - 150))                # bỏ phần chú giải
    s = min(CW / im.width, 1.0); tiles.append((sid, im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)))
rows = [tiles[i:i + COLS] for i in range(0, len(tiles), COLS)]
H = sum(max(t.height for _, t in r) + 40 for r in rows) + PAD
out = Image.new('RGB', (COLS * (CW + PAD) + PAD, H), (10, 12, 20)); d = ImageDraw.Draw(out); y = PAD; n = 0
for r in rows:
    for c, (sid, t) in enumerate(r):
        n += 1; x = PAD + c * (CW + PAD)
        d.text((x, y), f'{n}. {sid}', fill=(255, 230, 160), font=FT); out.paste(t, (x, y + 28))
    y += max(t.height for _, t in r) + 40
out.save(os.path.join(root, 'tong-quan-25-man.png'), optimize=True); print(out.size, len(tiles))
