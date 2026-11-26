from kit import *

THEME = dict(bg1=(36, 44, 60), bg2=(30, 32, 48), rock1=(120, 130, 150), rock2=(100, 108, 132))
s3, p3 = shaft_up(22, 50, n=4)


def beam(x, y, w, h): return H('laser', x, y, w, h)


rooms = [
 Room('R1', 'Sảnh kính', 0, 50, 44, 16, 2, [
   F((0, 12), (44, 12)), H('ice', 14, 11.6, 18, 0.4), X(14, 9.5, 'sàn kính trơn'), E('S', 38, 11), E('D', 8, 5),
   PATH((1, 11), (43, 11))], '''
- **Mục đích:** giới thiệu **sàn kính trơn**: có quán tính, dừng lại thì trượt thêm khoảng 2 ô.
- **Địa hình:** sảnh 44 ô, mặt sàn ở y 62. Đoạn giữa dài 18 ô là sàn kính.
- **Địch:**
  - 1 Drone ở đầu sảnh.
  - 1 Sniper ngay sau đoạn kính: lướt trên kính thì trượt thẳng vào tầm bắn của nó.
- **Trang trí:** vách kính, bể chứa mẫu vật, đèn trần xanh lạnh.'''),

 Room('R2', 'Hành lang gương', 44, 50, 70, 16, 3, [
   B(0, 0, 70, 2), F((0, 12), (70, 12)), B(4, 2, 2, 3), beam(6, 3.3, 14, 0.4), B(20, 2.5, 2, 2), beam(20.8, 4.5, 0.4, 7.5),
   B(40, 2, 2, 3), beam(42, 3.3, 10, 0.4), B(52, 2.5, 2, 2), beam(52.8, 4.5, 0.4, 7.5), H('ice', 28, 11.6, 10, 0.4),
   X(18, 1.4, 'gương 1'), X(50, 1.4, 'gương 2'), X(6, 6, 'bắn gương: xoay 90°'),
   E('D', 32, 5), E('R', 36, 11), E('S', 64, 11), PATH((1, 11), (69, 11))], '''
- **Mục đích:** dạy **gương xoay bằng đạn**: tia laser bắn ngang, chạm gương thì bẻ thẳng xuống, chắn đường.
- **Địa hình:** hành lang 70 ô, 2 bộ đầu phát + gương treo trần.
- **Cơ chế:**
  - Mỗi gương lúc đầu bẻ tia xuống sàn, tạo một cột laser chắn đường.
  - **Bắn gương 1 phát** thì gương xoay 90°, tia đi thẳng lên trần, mở đường trong **6 giây** rồi gương xoay lại.
  - Đạn nạp đầy xoay gương vĩnh viễn.
- **Địch:**
  - 1 Drone giữa hai bộ gương.
  - 1 Sniper cuối hành lang.
- **Vật phẩm:** Reploid #1 giữa hai cột laser, trên đoạn sàn kính.'''),

 Room('R3', 'Giếng bệ kính', 114, 14, 22, 50, 4, s3 + [
   H('ice', 2, 4, 2, 40), X(2.5, 30, 'vách kính trơn'), E('D', 11, 26), p3], '''
- **Mục đích:** đoạn dọc. Vách trái là kính trơn nên **không đá tường được**, chỉ vách phải bám được.
- **Địa hình:** giếng rộng 18 ô, cao 46 ô (từ y 62 lên y 16). 4 bệ kính zigzag.
- **Cơ chế:** đứng trên bệ kính cũng trượt. Nhảy từ bệ bên trái phải nhảy chéo thẳng sang vách phải rồi đá tường.
- **Địch:** 1 Drone giữa giếng.
- **Giáp hỗ trợ:** Blade lướt trên không 2 lần, dễ bù trượt.'''),

 Room('R4', 'Hành lang trần gai', 136, 12, 60, 12, 4, [
   B(0, 0, 60, 2), H('spike', 0, 2, 60, 1), F((0, 10), (60, 10)), B(20, 7, 6, 3), B(38, 7, 6, 3), P(48, 6, 5),
   X(2, 3.6, 'trần gai: nhảy cao là trúng'), E('K', 50, 5), E('S', 30, 9), E('B', 56, 9), E('R', 33, 9),
   PATH((1, 9), (19, 9), (21, 6), (25, 6), (27, 9), (37, 9), (39, 6), (43, 6), (45, 9), (59, 9))], '''
- **Mục đích:** áp lực trần thấp: không được nhảy hết lực.
- **Địa hình:**
  - Hành lang 60 ô, trần phủ gai ở y 15, sàn ở y 22. Khoảng trống chỉ 7 ô.
  - 2 khối thép cao 3 ô làm bậc. Nhảy hết lực từ trên khối là chạm gai trần.
  - Nhảy ngắn (nhả nút sớm) là kỹ năng chính của phòng.
- **Công tắc:** trên kệ cuối hành lang. Bắn vào thì mở cửa tầng trên của R5 (cần cho capsule).
- **Địch:**
  - 1 Sniper giữa hai khối.
  - 1 Brute cuối hành lang.
- **Vật phẩm:** Reploid #2 giữa hai khối.'''),

 Room('MID', 'Khiên gương', 196, 8, 30, 16, 5, arena(30, 16, 14) + [E('M', 15, 9), X(4, 4, 'khiên phản đạn về phía X')], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Khiên gương** là cỗ máy cầm tấm gương lớn, luôn xoay gương về phía người chơi.
- **Đòn đánh:**
  - Phản mọi viên đạn bắn thẳng vào gương về phía X.
  - Chiếu tia laser qua gương, quét nửa sân.
  - Lao húc bằng khiên.
- **Điểm yếu:** lưng. Đá tường qua đầu nó rồi bắn từ phía sau.
- **Phần thưởng:** mở cửa vào khu thí nghiệm. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Phòng thí nghiệm hai tầng', 226, 0, 66, 26, 5, [
   F((0, 22), (66, 22)), B(20, 10, 46, 1), H('ice', 20, 9.6, 30, 0.4), B(14, 11, 3, 11), BAR(20, 4, 1, 6, 'door'),
   Z('dark', 52, 4, 3, 6, 'tường giả'), B(55, 4, 1, 6), B(20, 3, 46, 1),
   E('C', 2, 21), E('B', 40, 21), E('S', 34, 9), E('R', 30, 21), E('A', 60, 9), E('G', 62, 21),
   X(56, 19, 'cổng Dynamo'), X(21, 1.6, 'cửa mở bằng công tắc R4'),
   PATH((1, 21), (65, 21)), ALT((13, 21), (15, 12), (19, 9), (50, 9), (60, 9))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** phòng hai tầng. Tầng dưới là đường chính, tầng trên giấu capsule sau **tường giả**.
- **Địa hình:**
  - Sàn chính ở y 22, dài 66 ô.
  - Tầng trên là sàn kính ở y 10, chạy từ x 246 tới hết phòng. Lối vào là một cửa ở x ≈ 246, chỉ mở khi đã bắn công tắc ở R4.
  - Cột thép cao 11 ô để đá tường lên tầng trên.
- **Địch:**
  - 1 Brute ở tầng dưới.
  - 1 Sniper ở tầng trên, bắn xuống qua sàn kính (đạn xuyên kính, người thì không).
- **Vật phẩm:** Reploid #3 ở tầng dưới.
- **Lối phụ (Capsule Shadow Head):**
  - Cuối tầng trên là một bức tường trông như vách thật, nhưng hơi nhấp nháy khi đứng sát.
  - Đi thẳng vào thì xuyên qua. Capsule nằm sau tường (x ≈ 286, y ≈ 9).
  - Quên bắn công tắc ở R4 thì cửa tầng trên đóng: phải quay lại.
- **Cổng Dynamo:** cuối tầng dưới có cổng sang lối thay thế đấu Dynamo (theo dữ liệu game).'''),

 Room('R6', 'Phòng phản xạ', 292, 4, 60, 22, 7, [
   F((0, 18), (6, 18)), F((54, 18), (60, 18)), H('void', 6, 20, 48, 2),
   P(10, 17, 5), P(20, 14, 5), P(30, 17, 5), P(40, 13, 5), P(48, 16, 5), P(28, 7, 5),
   H('ice', 10, 16.6, 5, 0.4), H('ice', 30, 16.6, 5, 0.4), H('ice', 48, 15.6, 5, 0.4),
   B(2, 2, 2, 2), beam(4, 2.8, 20, 0.4), B(24, 2, 2, 2), beam(24.8, 4, 0.4, 7), beam(25, 10.8, 18, 0.4), B(43, 10, 2, 2), beam(43.8, 12, 0.4, 8),
   X(8, 1, 'tia đổi đường mỗi 3s (2 kiểu)'), E('D', 16, 8), E('D', 50, 6), E('H', 30.5, 6),
   PATH((1, 17), (6, 17), (12, 16), (22, 13), (32, 16), (42, 12), (50, 15), (55, 17), (59, 17)), ALT((22, 13), (29, 6))], '''
- **Mục đích:** cao trào của màn. Nhảy trên bệ kính trơn qua vực, trong khi đường tia laser đổi liên tục.
- **Địa hình:** vực rộng 48 ô, 5 bệ kính (3 bệ trơn). Rơi là mất mạng.
- **Cơ chế – tia đổi đường:**
  - Một đầu phát ở góc trên trái, 2 gương tự xoay.
  - Mỗi 3 giây, gương đổi góc và tia chuyển giữa **2 kiểu đường đi**: kiểu A chắn bệ 2 và bệ 5, kiểu B chắn bệ 3 và bệ 4.
  - Đèn trên gương đổi màu 1 giây trước khi xoay.
  - Người chơi phải nhảy theo nhịp đổi kiểu. Bắn gương ở phòng này không có tác dụng.
- **Địch:** 2 Drone.
- **Lối phụ (Heart Tank):**
  - Một bệ nhỏ nằm cao giữa vực (x ≈ 320, y ≈ 11). Tia kiểu A đi ngay sát dưới nó.
  - Chỉ an toàn lúc tia ở kiểu B: nhảy từ bệ 2 lên, lấy Heart Tank, rồi xuống bệ 4 trước khi đổi kiểu.'''),

 Room('R7', 'Kho mẫu vật', 352, 12, 52, 14, 6, [
   B(0, 0, 52, 2), H('spike', 0, 2, 40, 1), F((0, 10), (52, 10)), H('ice', 8, 9.6, 26, 0.4), P(46, 7, 6), Z('dark', 44, 3, 2, 4, 'tường giả'),
   E('C', 2, 9), E('S', 40, 9), E('D', 24, 5), E('T', 50, 6),
   PATH((1, 9), (51, 9)), ALT((42, 9), (45, 5), (50, 6))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: trần gai, sàn kính trơn, tường giả.
- **Địa hình:** kho 52 ô, trần gai ở 40 ô đầu, sàn kính 26 ô ở giữa.
- **Địch:**
  - 1 Drone giữa kho.
  - 1 Sniper cuối đoạn kính: trượt vào nó là trúng đạn.
- **Lối phụ (Sub-Tank):** góc trên bên phải có một ô tường nhấp nháy giống ở R5. Đá tường vào thì xuyên qua, Sub-Tank trên kệ phía sau (x ≈ 402, y ≈ 18).'''),

 rest('R8', 'Cửa phòng giám đốc', 404, 12, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Shield Sheldon', 434, 8, 32, 16, 6, arena(32, 16, 14) + [
   B(8, 3, 2, 2), B(22, 3, 2, 2), X(5, 6, 'pha 2: 2 gương trần'), E('*', 18, 9)], '''
- **Đấu trường 28 ô**, kín, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (khiên phản đạn, Guard Shell, dịch chuyển).
- **Pha 2** (dưới 50% HP):
  - **2 gương trên trần** bật lên. Tia của Sheldon bắn vào gương sẽ dội xuống sân theo góc chéo.
  - Bắn gương thì gương xoay, có thể dội tia ngược vào Sheldon (gây sát thương lớn).
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Viện Laser', en='Laser Institute', boss='Shield Sheldon', act='Act II · X6', theme=THEME, capsule='Shadow Head',
 subtitle='Area 1 (sảnh và hành lang): R1 → R2 (gương) → R3 (leo, vách trơn) → R4 (trần gai, công tắc) → Mini-boss  |  Area 2 (khu thí nghiệm): R5 (tường giả) → R6 (phản xạ) → R7 → R8 → Boss',
 keep='Boss, capsule Shadow Head, sàn kính trơn, tia laser gương, tường giả, hành lang trần gai và cổng Dynamo vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Viện nghiên cứu quang học sau thảm họa Nightmare, sàn và vách bằng kính trơn. Khác màn Laser của X5 (bật/tắt bằng công tắc), ở đây người chơi **bẻ đường đi của tia** bằng gương, và học rằng **không phải bức tường nào cũng là thật**.',
 areas=['**Area 1 – Sảnh và hành lang:** kính trong, ánh xanh lạnh. Dạy sàn trơn, gương xoay bằng đạn, vách không bám được, trần gai.',
        '**Area 2 – Khu thí nghiệm:** tối hơn, nhiều tia đỏ. Tường giả, phòng phản xạ đổi đường tia, kho mẫu vật.'],
 flow='trượt trên kính → bắn gương mở đường → leo giếng một vách → nhảy ngắn dưới trần gai → mini-boss phản đạn → đi xuyên tường giả → nhảy theo nhịp tia đổi đường → boss có gương trần',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X6, màn Shield Sheldon:** viện laser, bệ kính trơn, tường giả giấu capsule Shadow Head, cổng sang Dynamo.',
       '**X5, màn Shining Hotarunicus:** công tắc quang học (ở đây đổi thành gương xoay để không lặp cơ chế).',
       '**X3, màn Crush Crawfish / X4, màn Frost Walrus:** sàn trơn có quán tính.',
       '**X Corrupted:** tường giả có dấu hiệu nhỏ (nhấp nháy khi đứng sát) để người chơi tinh ý tìm được.'],
 engine=['Sàn và vách kính trơn: quán tính khi đứng, không đá tường được trên vách kính.',
         'Tia laser đi theo đường gương: tính đường tia qua các gương, gương xoay bằng đạn hoặc tự xoay theo nhịp.',
         'Tường giả: ô Collision không chặn, nhấp nháy nhẹ khi người chơi đứng sát.',
         'Trần gai.',
         'Công tắc ở phòng này mở cửa ở phòng khác (liên kết theo id).',
         'Cổng dịch chuyển sang lối Dynamo (giữ theo dữ liệu game).',
         'Mini-boss Khiên gương phản đạn theo hướng.'],
 art=['**Tileset "Sảnh kính" (Area 1):** 47 ô viền kính và khung thép, sàn kính trơn (ánh phản chiếu), trần gai.',
      '**Tileset "Khu thí nghiệm" (Area 2):** 47 ô viền tối, ô tường giả (giống hệt tường thật + 2 khung nhấp nháy).',
      '**Vật thể:** đầu phát laser, gương (4 góc), tia laser (đoạn thẳng, 3 khung), bể mẫu vật.',
      '**Nền:** Area 1: phòng thí nghiệm kính (2 lớp parallax). Area 2: lưới laser mờ và tủ mẫu (2 lớp).'],
)
STAGE['rooms'] = rooms
