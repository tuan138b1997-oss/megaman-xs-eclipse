"""Sinh lại sơ đồ, kịch bản, JSON, README và ảnh tổng quan cho 25 màn.

  python3 tools/gen2.py            # tất cả
  python3 tools/gen2.py x5_grizzly # một màn
Chạy trong thư mục docs/level-design/campaign.
"""
import importlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import layout, check_stage, draw, write_doc, export_json, counts, ENT
from PIL import Image, ImageDraw, ImageFont

ORDER = ['intro', 'x5_grizzly', 'x5_makkoeen', 'x5_kraken', 'x5_hotarunicus', 'x5_rosered', 'x5_necrobat', 'x5_pegacion',
         'x5_f1_dynamo', 'x5_f2_shadow', 'x5_f3_rangda', 'x5_f4_sigma',
         'x6_turtloid', 'x6_sheldon', 'x6_mijinion', 'x6_yammark', 'x6_shark', 'x6_heatnix', 'x6_wolfang', 'x6_scaravich',
         'x6_f1_nzero', 'x6_f2_nmother', 'x6_f3_highmax', 'x6_f4_gate', 'x6_f5_bossrush']
GROUPS = [('Mở đầu và 7 màn boss X5 (Act I)', ORDER[:8]), ('4 màn pháo đài Zero Space (X5)', ORDER[8:12]),
          ('8 màn boss X6 (Act II)', ORDER[12:20]), ('5 màn pháo đài Gate Lab (X6)', ORDER[20:])]
HERE = os.path.dirname(os.path.abspath(__file__))
GAME = json.load(open(os.path.join(HERE, 'game_data.json'), encoding='utf-8'))


def build(sid):
    mod = importlib.import_module('stages.' + sid)
    st = mod.build()
    g = GAME.get(sid, {})
    if g.get('attacks') and not st.boss_info.get('attacks'): st.boss_info['attacks'] = g['attacks']
    if g.get('weak') and not st.boss_info.get('weak'): st.boss_info['weak'] = g['weak']
    if g.get('capsules') and not st.capsule: st.capsule = ' '.join(c.split(' 🎯')[0] for c in g['capsules'])[:900]
    layout(st)
    return st


def main(ids):
    os.makedirs('maps', exist_ok=True); os.makedirs('data', exist_ok=True)
    built, bad = {}, {}
    for sid in ids:
        st = build(sid)
        errs = check_stage(st)
        draw(st, f'maps/{sid}.png')
        write_doc(st, f'{sid}.md', f'maps/{sid}.png', errs)
        export_json(st, f'data/{sid}.level.json')
        built[sid] = st
        if errs: bad[sid] = errs
        print(f'{sid:16s} {int(st.W)}×{int(st.H)} ô  phòng {len(st.rooms)}  lỗi {len(errs)}')
    for sid, e in bad.items():
        print('\n' + sid); [print('  -', x) for x in e]
    if len(ids) == len(ORDER):
        readme(built); overview(built)
    return bad


def readme(B):
    L = ['# Kịch bản & sơ đồ toàn chiến dịch', '',
         'Màn mẫu đã duyệt: **Lò Nham Thạch** (`x5_dinorex`), xem `../lo-nham-thach-kich-ban.md`. 25 màn còn lại được thiết kế theo đúng chuẩn đó: '
         'sơ đồ có địa hình theo ô (nền, dốc, hố, giếng dọc, kệ, bẫy, đường đi chính, lối bí mật), kịch bản từng phòng có tọa độ và thông số nhịp, '
         'bảng vật phẩm/kẻ địch, phần engine cần bổ sung, danh sách hình cần vẽ và dữ liệu JSON (`data/<id>.level.json`).', '',
         '![Tổng quan 25 màn](tong-quan-25-man.png)', '', '## Quy ước chung', '',
         '- **Kích thước (chuẩn đã duyệt):** khung hình 640×360 px = 20×11.25 ô; hành lang trần 1 ô + trong lòng 9 ô, trần luôn nằm trong khung; '
         'phòng nhảy bệ 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô.',
         '- **Nhảy:** X nhảy cao ~2.6 ô, xa ~5 ô. Trên đường chính gờ ≤ 2.5 ô, nhảy xa ≤ 5 ô, lướt-nhảy ≤ 7 ô; mọi đường chính được **kiểm tra tự động** (`tools/lib.py`).',
         '- Mỗi màn có **2 Area**, **1 mini-boss** giữa màn, **2 checkpoint**, **4 Reploid**, 11–14 kẻ địch thường ở màn boss, 7–10 ở màn pháo đài (Sniper / Drone / Brute), đặt có chủ đích.',
         '- Màn boss: thêm **1 Heart Tank, 1 Sub-Tank** và capsule giáp đúng theo dữ liệu game. Đỉnh độ khó 7/10 ở đoạn cao trào.',
         '- Màn pháo đài: không có Heart Tank/Sub-Tank (như dòng X gốc), có trạm năng lượng lớn trước boss; chỉ Zero Space 3 và Gate Lab 3 có capsule bí mật. Đỉnh độ khó 8/10.',
         '- Mọi bẫy chết ngay đều có báo trước; không có đoạn tự cuộn bắt buộc (đoạn tự cuộn gốc làm lại thành đoạn đuổi do người chơi điều khiển).',
         '- Boss giữ bộ chiêu và điểm yếu theo dữ liệu game; pha 2 (dưới 50% HP) thêm một thay đổi môi trường gắn với cơ chế của màn.', '']
    for title, ids in GROUPS:
        L += [f'## {title}', '', '| Màn | Boss | Capsule | Cơ chế chính | Cao trào | Bí mật |', '|---|---|---|---|---|---|']
        for sid in ids:
            st = B[sid]; peak = max((r for r in st.rooms if r.code != 'BOSS'), key=lambda r: r.diff)
            c = counts(st)
            sec = ', '.join(x for x, k in (('capsule', 'A'), ('Heart Tank', 'H'), ('Sub-Tank', 'T')) if c.get(k)) or '—'
            L.append(f'| [{st.title}]({sid}.md) | {st.boss} | {st.capsule_short or "—"} | {"; ".join(st.mech)} | {peak.code} {peak.name} ({peak.diff}) | {sec} |')
        L.append('')
    L += ['## Công cụ', '', '- Dữ liệu từng màn: `tools/stages/<id>.py` (phòng ghép từ khối, thực thể, đường đi, kịch bản).',
          '- Thư viện: `tools/lib.py` (xếp phòng, kiểm tra đường chính, vẽ sơ đồ, viết kịch bản, xuất JSON); khối phòng: `tools/kit.py`.',
          '- `python3 tools/gen2.py` trong thư mục này sinh lại toàn bộ sơ đồ, kịch bản, JSON, README và ảnh tổng quan; `python3 tools/gen2.py <id>` sinh một màn.',
          '- Dữ liệu boss/capsule lấy từ `campaign-data.js` vào `tools/game_data.json`.', '']
    src = open(os.path.join(HERE, 'sources.md'), encoding='utf-8').read() if os.path.exists(os.path.join(HERE, 'sources.md')) else ''
    open('README.md', 'w', encoding='utf-8').write('\n'.join(L) + ('\n' + src if src else ''))


def overview(B):
    ft = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
    CW = 1500; tiles = []
    for i, sid in enumerate(ORDER):
        im = Image.open(f'maps/{sid}.png').convert('RGB'); im = im.crop((0, 0, im.width, im.height - 150))
        s = min(CW / im.width, 1); tiles.append((f'{i + 1}. {B[sid].title} · {B[sid].boss}', im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)))
    H = sum(t.height + 40 for _, t in tiles) + 60
    out = Image.new('RGB', (CW + 40, H), (10, 12, 20)); d = ImageDraw.Draw(out)
    d.text((20, 14), 'TỔNG QUAN 25 MÀN (sơ đồ thu nhỏ, xem bản đầy đủ trong maps/)', fill=(255, 230, 160), font=ft); y = 52
    for name, t in tiles:
        d.text((20, y), name, fill=(255, 230, 160), font=ft); out.paste(t, (20, y + 30)); y += t.height + 40
    out.save('tong-quan-25-man.png', optimize=True)


if __name__ == '__main__':
    ids = sys.argv[1:] or ORDER
    bad = main(ids)
    sys.exit(1 if bad else 0)
