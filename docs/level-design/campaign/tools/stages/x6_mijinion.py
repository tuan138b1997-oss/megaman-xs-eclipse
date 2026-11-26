from kit import *

THEME = dict(bg1=(46, 46, 54), bg2=(40, 36, 40), rock1=(126, 126, 136), rock2=(118, 106, 100))
s4, p4 = shaft_up(22, 50, n=4)


def cable(x, w, y=2): return BAR(x, y, w, 0.25, 'trash')


def reticle(x, y, lab='tâm ngắm'): return Z('alarm', x, y, 3, 3, lab)


rooms = [
 Room('R1', 'Bến vũ khí', 0, 50, 50, 16, 2, [
   F((0, 12), (50, 12)), B(18, 9, 4, 3), B(34, 9, 4, 3), reticle(26, 8), X(14, 3, 'Illumina ở nền: khóa mục tiêu 2s rồi bắn'),
   E('S', 44, 11), E('D', 10, 5), PATH((1, 11), (49, 11))], '''
- **Mục đích:** giới thiệu **tâm ngắm Illumina**. Phi thuyền khổng lồ ở nền xa khóa mục tiêu vào người chơi.
- **Cơ chế – tâm ngắm:**
  - Một vòng ngắm đỏ bám theo X, mất 2 giây để khóa (vòng thu nhỏ dần, tiếng bíp nhanh dần).
  - Khóa xong thì 0.5 giây sau một tia pháo bắn xuống đúng chỗ đó, rộng 3 ô.
  - Chạy đổi hướng hoặc lướt ra khỏi vòng là né được. Nấp sau thùng thép thì tâm ngắm mất dấu.
  - Chu kỳ 6 giây một lần.
- **Địa hình:** bến cảng 50 ô, mặt sàn ở y 62. 2 thùng thép làm chỗ nấp.
- **Địch:** 1 Drone đầu bến, 1 Sniper cuối bến.'''),

 Room('R2', 'Kho tên lửa', 50, 50, 70, 16, 3, [
   F((0, 12), (70, 12)), B(10, 8, 4, 4), B(26, 9, 6, 3), B(44, 8, 4, 4), B(58, 9, 4, 3), reticle(36, 7),
   X(10, 6.5, 'thùng bị pháo phá'), E('B', 38, 11), E('S', 64, 11), E('R', 21, 11), PATH((1, 11), (69, 11))], '''
- **Mục đích:** nấp và tiến lên trong khi tâm ngắm phá dần chỗ nấp.
- **Địa hình:** kho 70 ô, 4 chồng thùng làm vật che.
- **Cơ chế:** tia pháo của Illumina **phá được thùng**. Nấp quá lâu ở một chỗ thì mất chỗ nấp đó.
- **Địch:**
  - 1 Brute giữa kho.
  - 1 Sniper cuối kho.
- **Vật phẩm:** Reploid #1 sau chồng thùng thứ nhất.
- **Mẹo:** dụ tia pháo bắn trúng Brute: pháo gây sát thương cho cả địch.'''),

 Room('R3', 'Vực cáp 1', 120, 48, 60, 22, 4, [
   F((0, 14), (6, 14)), F((54, 12), (60, 12)), H('void', 6, 18, 48, 4), cable(6, 48),
   P(10, 12, 5, 'move'), P(22, 10, 5, 'move'), P(34, 12, 5, 'move'), P(44, 10, 5, 'move'), P(26, 16, 4),
   X(8, 0.6, 'cáp'), reticle(30, 4), E('D', 18, 5), E('D', 40, 4), E('H', 28, 15),
   PATH((1, 13), (6, 13), (12, 11), (24, 9), (36, 11), (46, 9), (55, 11), (59, 11)), ALT((24, 9), (28, 15))], '''
- **Mục đích:** lần đầu đi trên **bệ treo cáp** qua vực.
- **Địa hình:** vực rộng 48 ô, rơi là mất mạng. Một sợi cáp chạy ngang trên cao.
- **Cơ chế – bệ treo cáp:**
  - 4 bệ treo dưới cáp, trượt qua lại 6 ô và đung đưa nhẹ (lệch 1 ô).
  - Tâm ngắm vẫn hoạt động. Đứng yên trên bệ để chờ là bị khóa.
- **Địch:** 2 Drone.
- **Lối phụ (Heart Tank):**
  - Một gờ thép nhỏ dưới tầm bệ thứ hai, gần đáy vực (x ≈ 146, y ≈ 64).
  - Thả người từ bệ thứ hai xuống gờ và lấy Heart Tank.
  - Gờ không có vách để đá tường: phải chờ bệ thứ ba trượt tới gần rồi nhảy lên.'''),

 Room('R4', 'Tháp nạp đạn', 180, 12, 22, 50, 4, s4 + [
   H('elec', 2, 30, 18, 0.5), X(3, 31, 'băng tải đạn: dòng điện 1s/2s'), E('D', 11, 22), E('R', 4, 13), p4], '''
- **Mục đích:** đoạn dọc trong nhà, thoát khỏi tâm ngắm (không có tầm nhìn ra trời).
- **Địa hình:** tháp rộng 18 ô, cao 46 ô (từ y 60 lên y 14). 4 kệ zigzag.
- **Bẫy:** một băng tải đạn chạy ngang giữa tháp có dòng điện chạy dọc, bật 1 giây, tắt 2 giây.
- **Địch:** 1 Drone.
- **Vật phẩm:** Reploid #2 trên kệ cao nhất.'''),

 Room('MID', 'Lõi cáp Illumina', 202, 6, 30, 16, 5, arena(30, 16, 14) + [E('M', 15, 4), cable(2, 26, 2), X(4, 9, '4 cáp năng lượng nối lõi')], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Lõi cáp Illumina** treo giữa trần, nối với 4 sợi cáp năng lượng chạy xuống sàn.
- **Đòn đánh:**
  - Mỗi sợi cáp phóng điện theo thứ tự, cột điện rộng 2 ô.
  - Lõi bắn tia xuống theo tâm ngắm (như R1, nhưng khóa trong 1.5 giây).
- **Điểm yếu:** phá 4 sợi cáp (mỗi sợi 3 phát) thì lõi rơi xuống sàn 4 giây, lúc đó mới đánh lõi được.
- **Phần thưởng:** tắt tâm ngắm trong khu xưởng tiếp theo. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Xưởng lắp ráp', 232, 8, 64, 14, 5, [
   B(0, 0, 64, 2), F((0, 12), (64, 12)), CV(6, 11.4, 24, 1), CV(36, 11.4, 22, 1), H('trash', 16, 2, 4, 5), H('trash', 44, 2, 4, 5),
   P(50, 5, 6), P(38, 7, 4, 'move'), X(14, 7.5, 'tay ép 1.2s/0.3s'),
   E('C', 2, 11), E('B', 32, 11), E('S', 60, 11), E('R', 26, 11), E('T', 53, 4),
   PATH((1, 11), (63, 11)), ALT((34, 11), (39, 6), (53, 4))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** băng chuyền xuôi chiều kết hợp tay ép, trong nhà (không còn tâm ngắm).
- **Địa hình:** xưởng 64 ô, 2 đoạn băng chuyền đẩy sang phải 100px/giây.
- **Bẫy – tay ép:** 2 tay ép thủy lực trên băng chuyền: chờ 1.2 giây, đập 0.3 giây. Băng chuyền đẩy người chơi vào tay ép nên phải canh nhịp.
- **Địch:** 1 Brute giữa hai băng chuyền, 1 Sniper cuối xưởng.
- **Vật phẩm:** Reploid #3 cuối băng chuyền thứ nhất.
- **Lối phụ (Sub-Tank):** một cánh tay robot nâng hàng (bệ di động lên xuống) ở giữa xưởng. Đứng lên tay robot lúc nó lên cao nhất rồi nhảy sang kệ hàng phía trên (x ≈ 285, y ≈ 12).'''),

 Room('R6', 'Vực cáp lớn', 296, 4, 70, 24, 7, [
   F((0, 16), (6, 16)), F((64, 14), (70, 14)), H('void', 6, 22, 58, 2), cable(6, 58),
   P(9, 14, 4, 'move'), P(17, 11, 4, 'move'), P(25, 14, 4, 'move'), P(33, 10, 4, 'move'), P(41, 13, 4, 'move'), P(49, 9, 4, 'move'), P(57, 12, 4, 'move'),
   P(52, 3, 6), reticle(28, 4), reticle(46, 3, ''), X(8, 19, 'tâm ngắm khóa 1.5s, bắn 2 phát liền'),
   E('D', 22, 6), E('D', 44, 18), E('A', 55, 2),
   PATH((1, 15), (6, 15), (11, 13), (19, 10), (27, 13), (35, 9), (43, 12), (51, 8), (59, 11), (65, 13), (69, 13)), ALT((51, 8), (55, 2))], '''
- **Mục đích:** cao trào của màn. Vực cáp dài 58 ô (khoảng 1.850px) với 7 bệ cáp, tâm ngắm trở lại mạnh hơn.
- **Cơ chế:**
  - 7 bệ treo cáp trượt lệch pha nhau, tốc độ tăng dần từ bệ đầu tới bệ cuối.
  - **Tâm ngắm khóa nhanh hơn (1.5 giây) và bắn 2 phát liền.** Phải nhảy sang bệ khác ngay khi vòng ngắm bắt đầu thu nhỏ.
- **Địch:**
  - 1 Drone bay ngang tầm bệ thứ hai.
  - 1 Drone bay lên từ đáy vực.
- **Lối phụ (Capsule Blade Head):**
  - Một bệ thép cao gần cuối vực (x ≈ 348, y ≈ 7), cao hơn mọi bệ cáp.
  - Nhảy từ bệ cáp thứ sáu lúc nó trượt sang phải hết cỡ, rồi lướt trên không mới tới.
  - Giáp Blade lướt trên không 2 lần nên dễ hơn.'''),

 Room('R7', 'Phòng điều khiển pháo', 366, 8, 52, 14, 6, [
   F((0, 10), (52, 10)), B(12, 7, 4, 3), B(28, 7, 4, 3), B(40, 6, 4, 4), reticle(20, 4), reticle(36, 3, ''),
   E('C', 2, 9), E('S', 46, 9), PATH((1, 9), (51, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: tâm ngắm đôi, chỗ nấp ít dần.
- **Địa hình:** sân thượng 52 ô, ngoài trời, 3 bệ thép thấp làm chỗ nấp.
- **Cơ chế:** **2 tâm ngắm** cùng lúc, khóa lệch nhau 1 giây. Phải di chuyển liên tục giữa các chỗ nấp.
- **Địch:** 1 Sniper cuối sân thượng, đứng trên bệ cao.'''),

 rest('R8', 'Hầm chỉ huy', 418, 8, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Infinity Mijinion', 448, 4, 32, 16, 6, arena(32, 16, 14, ceil=False) + [reticle(14, 6, 'pha 2'), E('*', 22, 9)], '''
- **Đấu trường 28 ô**, mở trời, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (phân thân, Ground Dash, nhảy bật).
- **Pha 2** (dưới 50% HP):
  - **Tâm ngắm Illumina** trở lại, khóa vào người chơi mỗi 8 giây.
  - Tia pháo cũng xóa phân thân của Mijinion: dụ tâm ngắm vào đám phân thân là cách dọn sân nhanh.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Trung tâm vũ khí', en='Weapons Center', boss='Infinity Mijinion', act='Act II · X6', theme=THEME, capsule='Blade Head',
 subtitle='Area 1 (bến và kho, ngoài trời): R1 → R2 (nấp) → R3 (vực cáp) → R4 (leo tháp) → Mini-boss lõi cáp  |  Area 2 (xưởng và vực lớn): R5 → R6 (vực cáp lớn) → R7 → R8 → Boss',
 keep='Boss, capsule Blade Head, phi thuyền Illumina khóa mục tiêu, bệ dây cáp và lõi cáp ở mid-gate vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Căn cứ vũ khí nằm dưới bóng phi thuyền khổng lồ Illumina. Khi ở ngoài trời, người chơi **luôn bị ngắm bắn**. Cả màn xoay quanh việc di chuyển liên tục, dùng chỗ nấp và vượt vực trên bệ treo cáp.',
 areas=['**Area 1 – Bến và kho (ngoài trời):** thép xám, bầu trời có phi thuyền chiếm nửa nền. Dạy tâm ngắm, chỗ nấp bị phá, bệ treo cáp.',
        '**Area 2 – Xưởng và vực lớn:** trong xưởng có băng chuyền và tay ép, rồi ra vực cáp lớn với tâm ngắm bắn 2 phát.'],
 flow='né tâm ngắm → nấp sau thùng → đi cáp qua vực → leo tháp nạp đạn → phá lõi cáp → băng chuyền và tay ép → vực cáp lớn dưới hỏa lực → boss phân thân',
 time='khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X6, màn Infinity Mijinion:** phi thuyền Illumina ở nền khóa mục tiêu, bệ dây cáp trên vực, lõi cáp ở mid-gate.',
       '**X8, màn Gigabolt Man-O-War:** hỏa lực từ vật thể khổng lồ ở nền.',
       '**X5, màn Spiral Pegacion:** vượt vực trên bệ chạy theo đường cố định.',
       '**X Corrupted:** cơ chế gây nguy hiểm cũng dùng được để tấn công (dụ pháo bắn địch).'],
 engine=['Tâm ngắm bám người chơi, khóa theo thời gian, mất dấu khi nấp sau vật che; tia pháo phá vật che và gây sát thương cả địch.',
         'Bệ treo cáp: trượt dọc cáp và đung đưa.',
         'Tay ép thủy lực theo nhịp trên băng chuyền.',
         'Cánh tay robot nâng hàng (bệ lên xuống).',
         'Mini-boss Lõi cáp: phá 4 cáp thì lõi rơi.'],
 art=['**Tileset "Bến vũ khí" (Area 1):** 47 ô viền thép, thùng thép (3 trạng thái hư hại), cáp và bệ treo.',
      '**Tileset "Xưởng" (Area 2):** 47 ô viền, băng chuyền, tay ép (3 khung), kệ hàng.',
      '**Vật thể:** vòng tâm ngắm (4 khung thu nhỏ), tia pháo (3 khung), lõi cáp.',
      '**Nền:** Area 1: phi thuyền Illumina chiếm nửa trời (2 lớp parallax). Area 2: dây chuyền lắp ráp (2 lớp).'],
)
STAGE['rooms'] = rooms
