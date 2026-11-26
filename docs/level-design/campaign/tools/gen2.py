# Sinh sơ đồ PNG + kịch bản .md cho các màn đã viết lại theo chuẩn màn mẫu.
# Chạy: python3 tools/gen2.py [id ...]   (từ thư mục docs/level-design/campaign)
import sys, os, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import draw, write_md

ROOT = os.path.dirname(HERE)
ORDER = ['intro', 'x5_grizzly', 'x5_makkoeen', 'x5_kraken', 'x5_hotarunicus', 'x5_rosered', 'x5_necrobat', 'x5_pegacion',
         'x5_f1_dynamo', 'x5_f2_shadow', 'x5_f3_rangda', 'x5_f4_sigma',
         'x6_turtloid', 'x6_sheldon', 'x6_mijinion', 'x6_yammark', 'x6_shark', 'x6_heatnix', 'x6_wolfang', 'x6_scaravich',
         'x6_f1_nzero', 'x6_f2_nmother', 'x6_f3_highmax', 'x6_f4_gate', 'x6_f5_bossrush']
ids = sys.argv[1:] or [s for s in ORDER if os.path.exists(os.path.join(HERE, 'stages', s + '.py'))]
os.makedirs(os.path.join(ROOT, 'maps'), exist_ok=True)
for sid in ids:
    st = importlib.import_module('stages.' + sid).STAGE
    size = draw(st, os.path.join(ROOT, 'maps', sid + '.png'))
    write_md(sid, st, os.path.join(ROOT, sid + '.md'), 'maps/' + sid + '.png')
    print(sid, size)

# ---------- README + ảnh tổng quan (chỉ khi sinh toàn bộ) ----------
if not sys.argv[1:]:
    from PIL import Image, ImageDraw
    from lib import FT
    groups = [('Mở đầu và 7 màn boss X5 (Act I)', ORDER[:8]), ('4 màn pháo đài Zero Space (X5)', ORDER[8:12]),
              ('8 màn boss X6 (Act II)', ORDER[12:20]), ('5 màn pháo đài Gate Lab (X6)', ORDER[20:])]
    L = ['# Kịch bản & sơ đồ toàn chiến dịch', '',
         'Màn mẫu đã duyệt: **Lò Nham Thạch** (`x5_dinorex`), xem `../lo-nham-thach-kich-ban.md`. '
         '25 màn còn lại được viết lại theo đúng chuẩn đó: sơ đồ có địa hình theo ô (nền, dốc, hố, giếng dọc, kệ, bẫy, đường đi chính, lối bí mật), '
         'kịch bản từng phòng có tọa độ và thông số nhịp, bảng vật phẩm/kẻ địch, phần engine cần bổ sung và danh sách hình cần vẽ.', '',
         '![Tổng quan 25 màn](tong-quan-25-man.png)', '',
         '## Quy ước chung', '',
         '- Mỗi màn có **2 Area**, **1 mini-boss** giữa màn, **2 checkpoint**, **4 Reploid**, 11–14 kẻ địch thường ở màn boss, 7–10 ở màn pháo đài (Sniper / Drone / Brute), đặt có chủ đích.',
         '- Màn boss: thêm **1 Heart Tank, 1 Sub-Tank** và capsule giáp đúng theo dữ liệu game. Đường cong độ khó đỉnh 7/10 ở đoạn cao trào.',
         '- Màn pháo đài: không có Heart Tank/Sub-Tank (như dòng X gốc), có trạm nạp năng lượng lớn trước boss; chỉ Zero Space 3 và Gate Lab 3 có capsule bí mật theo dữ liệu game. Đỉnh độ khó 8/10.',
         '- Mọi bẫy chết ngay đều có báo trước; không có đoạn tự cuộn bắt buộc (các đoạn tự cuộn gốc được làm lại thành đoạn đuổi do người chơi tự điều khiển, như bản X8 16-bit demake).',
         '- Boss giữ bộ chiêu và điểm yếu theo dữ liệu game; pha 2 (dưới 50% HP) thêm một thay đổi môi trường gắn với cơ chế của màn.', '']
    for gname, ids_ in groups:
        L += [f'## {gname}', '', '| Màn | Boss | Capsule | Cơ chế chính | Cao trào | Bí mật |', '|---|---|---|---|---|---|']
        for sid in ids_:
            st = importlib.import_module('stages.' + sid).STAGE
            rs = st['rooms']
            top = max((r for r in rs if r['kind'] is None), key=lambda r: r['diff'])
            ents = [g[1] for r in rs for g in r['geo'] if g[0] == 'ent']
            sec = ', '.join(n for c, n in (('A', 'capsule'), ('H', 'Heart Tank'), ('T', 'Sub-Tank')) if c in ents) or '—'
            mech = '; '.join(m.split(':')[0].split('(')[0].split(';')[0].split(',')[0].strip().rstrip('.') for m in st['engine'][:2])
            L.append(f"| [{st['title']}]({sid}.md) | {st['boss']} | {st['capsule'] or '—'} | {mech} | {top['code']} {top['name']} ({top['diff']}) | {sec} |")
        L.append('')
    L += ['## Công cụ', '',
          '- Dữ liệu từng màn: `tools/stages/<id>.py` (phòng, hình học theo ô, thực thể, đường đi, kịch bản).',
          '- Bộ vẽ sơ đồ và sinh kịch bản: `tools/lib.py`; khuôn phòng lặp lại: `tools/kit.py`.',
          '- Chạy `python3 tools/gen2.py` trong thư mục này để sinh lại toàn bộ sơ đồ, kịch bản, README và ảnh tổng quan; `python3 tools/gen2.py <id>` để sinh một màn.', '',
          '## Nguồn tham khảo', '',
          'Không xem được video YouTube; các trang wiki/FAQ chi tiết (StrategyWiki, Fandom, FAQ PDF) bị chặn mạng trong môi trường làm việc. '
          'Thiết kế dựa trên dữ liệu dự án (`campaign-data.js`: boss, capsule, cơ chế từng màn) và thông tin tóm tắt về các màn của X4/X5/X6/X8, bản X8 16-bit demake và X Corrupted. Bố cục là tự thiết kế, không chép bản đồ gốc.', '',
          '- [Mega Man X5 – Mega Man Wiki](https://megamanwiki.com/wiki/Mega_Man_X5), [Runaway Truck Stage](https://megamanwiki.com/wiki/Runaway_Truck_Stage), [Laser Institute Stage](https://megamanwiki.com/wiki/Laser_Institute_Stage), [Planetarium Stage](https://megamanwiki.com/wiki/Planetarium_Stage), [Reploid Air Force Stage](https://megamanwiki.com/wiki/Reploid_Air_Force_Stage), [Jungle Stage (X5)](https://megaman.fandom.com/wiki/Jungle_Stage_(Mega_Man_X5))',
          '- [Mega Man X6 – Mega Man Wiki](https://megamanwiki.com/wiki/Mega_Man_X6), [Weapon Center](https://megaman.fandom.com/wiki/Weapon_Center), [List of Heart Tank locations](https://megaman.fandom.com/wiki/List_of_Heart_Tank_locations)',
          '- [Mega Man X8 16-bit demake – Time Extension](https://www.timeextension.com/news/2024/09/mega-man-x8-has-just-got-a-free-16-bit-fan-demake), [Destructoid](https://www.destructoid.com/you-can-now-play-the-mega-man-x8-fan-demake/), [Rockman Corner](https://www.rockman-corner.com/2024/01/fan-made-mega-man-x8-16-bit-demake-gets.html)',
          '- [Mega Man X Corrupted – TV Tropes](https://www.tvtropes.org/pmwiki/pmwiki.php/VideoGame/MegaManXCorrupted), [Mega Man X8 – TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/MegaManX8)', '']
    open(os.path.join(ROOT, 'README.md'), 'w').write('\n'.join(L))
    # ảnh tổng quan: 25 sơ đồ thu nhỏ (chỉ phần bản đồ, bỏ chú thích), 1 cột
    W = 1400; parts = []
    for sid in ORDER:
        im = Image.open(os.path.join(ROOT, 'maps', sid + '.png')).convert('RGB')
        im = im.crop((0, 0, im.width, im.height - 175))
        s = W / im.width; parts.append((sid, im.resize((W, int(im.height * s)))))
    H = sum(p.height + 26 for _, p in parts) + 50
    sheet = Image.new('RGB', (W, H), (14, 18, 30)); d = ImageDraw.Draw(sheet)
    d.text((10, 10), 'TỔNG QUAN 25 MÀN (sơ đồ thu nhỏ, xem bản đầy đủ trong maps/)', fill=(255, 225, 150), font=FT)
    y = 46
    for sid, p in parts:
        st = importlib.import_module('stages.' + sid).STAGE
        d.text((10, y), f"{st['title']} · {st['boss']} · {st['act']}", fill=(220, 220, 230), font=FT); y += 22
        sheet.paste(p, (0, y)); y += p.height + 4
    sheet.save(os.path.join(ROOT, 'tong-quan-25-man.png'), optimize=True)
    print('README + tổng quan')
