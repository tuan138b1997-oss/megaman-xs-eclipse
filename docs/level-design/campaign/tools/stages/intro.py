from lib import *

THEME = dict(bg1=(46, 40, 52), bg2=(38, 40, 54), rock1=(112, 96, 88), rock2=(92, 96, 110))

rooms = [
 Room('R1', 'Làn đường sập', 0, 40, 52, 14, 1, [
   F((0, 10), (52, 10)), B(14, 8, 3, 2), B(30, 7, 4, 3),
   X(1, 6, 'START'), X(5, 3, 'bảng: NHẢY'), X(19, 3, 'bảng: BẮN'),
   E('S', 32, 6), E('S', 46, 9), PATH((2, 9), (13, 9), (15, 7), (29, 6), (35, 6), (51, 9))], '''
- **Mục đích:** dạy chạy, nhảy, bắn. Không có chỗ nào chết được.
- **Địa hình:**
  - Mặt đường phẳng 52 ô, mặt đất ở y 50.
  - 2 khối bê tông thấp (cao 2 và 3 ô) để dạy nhảy lên vật cản.
  - Bảng chỉ dẫn nút hiện ngay trên đầu nhân vật khi đi ngang (NHẢY, rồi BẮN).
- **Địch:**
  - 1 Sniper đứng trên khối bê tông thứ hai, bắn thẳng, chậm: dạy bắn đáp trả.
  - 1 Sniper cuối phòng, đứng ngang tầm.
- **Trang trí:** xe bỏ hoang, cột đèn đổ, khói xa ở nền, trời hoàng hôn.'''),

 Room('R2', 'Cầu vượt gãy', 52, 40, 64, 18, 2, [
   B(0, 10, 14, 2), B(18, 10, 18, 2), B(40, 10, 24, 2), B(8, 12, 2, 6), B(28, 12, 2, 6), B(52, 12, 2, 6),
   H('void', 0, 17, 64, 1), H('void', 14, 10, 4, 1), H('void', 36, 10, 4, 1), P(30, 15, 5),
   X(14, 7, 'hố gãy'), X(36, 7, 'hố gãy'), X(30, 16.2, 'gờ dưới cầu'),
   E('D', 38, 4), E('S', 50, 9), E('R', 61, 9), E('T', 33, 14),
   PATH((1, 9), (13, 9), (16, 7), (19, 9), (35, 9), (38, 7), (41, 9), (63, 9)),
   ALT((36.5, 10), (36.5, 13), (34, 14)), X(40, 15, 'đá trụ cầu leo lại')], '''
- **Mục đích:** dạy nhảy qua hố và bắn chéo khi đang nhảy.
- **Địa hình:**
  - Mặt cầu gãy làm 3 đoạn, giữa là **2 hố rộng 4 ô**.
  - Rơi vào hố gãy thì mất 2 máu và được đặt lại ở mép, không mất mạng (màn dạy chơi).
  - Ba trụ cầu đỡ bên dưới. Đáy phòng là vực thật (y 57), chỉ rơi được nếu cố ý đi xuống gầm cầu.
- **Địch:**
  - 1 Drone bay lượn đúng trên hố thứ hai: buộc phải bắn trước khi nhảy hoặc bắn chéo khi đang trên không.
  - 1 Sniper cuối cầu.
- **Vật phẩm:** Reploid #1 ở cuối cầu.
- **Lối phụ (Sub-Tank):**
  - Ở hố thứ hai, thả người bám vách trái của hố rồi trượt xuống gờ hẹp dưới gầm cầu (x ≈ 82, y ≈ 55).
  - Sub-Tank nằm trên gờ. Đá tường vào trụ cầu để leo lại lên mặt cầu.
  - Đây là bài học đầu tiên về "lối phụ nằm ngoài tầm nhìn".'''),

 Room('R3', 'Trụ cầu', 116, 16, 18, 42, 2, [
   B(0, 0, 2, 32), B(0, 36, 18, 6), B(16, 8, 2, 28), B(2, 0, 16, 1),
   P(2, 30, 4), P(12, 23, 4), P(2, 16, 4), P(12, 9, 4),
   E('D', 9, 20), X(3, 37.5, 'đá tường ↑'),
   PATH((1, 35), (9, 35), (14, 30), (4, 23), (14, 16), (4, 9), (10, 5), (17.5, 5))], '''
- **Mục đích:** đoạn dọc ngắn đầu tiên, dạy **đá tường**.
- **Địa hình:**
  - Giếng rộng 14 ô kẹp giữa hai trụ bê tông, cao 36 ô (từ y 52 lên y 20).
  - 4 kệ nghỉ xếp zigzag cách nhau 7 ô. Người mới cứ nhảy kệ, người quen đá tường thẳng lên.
  - Bảng chỉ dẫn "giữ hướng vào vách + NHẢY" hiện khi chạm vách lần đầu.
- **Địch:** 1 Drone giữa giếng, bay chậm qua lại.
- **Lối ra:** khe phía trên vách phải (y 17–24), dẫn ra tầng trên cao tốc.'''),

 Room('R4', 'Tầng trên cao tốc', 134, 10, 70, 14, 3, [
   F((0, 12), (70, 12)), B(12, 10, 5, 2), H('fire', 13, 8, 3, 2), B(34, 10, 5, 2), H('fire', 35, 8, 3, 2),
   B(46, 0, 3, 10), X(44, 10.4, 'khe 2 ô'), E('C', 3, 11), E('B', 26, 11), E('R', 41, 11), E('S', 56, 11), E('D', 62, 5),
   PATH((2, 11), (11, 11), (14, 6), (18, 11), (33, 11), (36, 6), (40, 11), (45, 11.4), (50, 11.4), (69, 11))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** dạy **lướt** (dash), cả lướt để vượt nhanh lẫn lướt để chui qua khe thấp.
- **Địa hình:**
  - Mặt đường thẳng 70 ô ở y 22.
  - 2 xe cháy làm vật cản. Lửa trên nóc xe bùng 1.0 giây rồi tắt 2.0 giây: nhảy qua lúc lửa tắt, hoặc lướt nhảy cho xa.
  - **Biển báo sập** treo thấp ở x ≈ 180, chỉ chừa khe cao 2 ô. Đứng thẳng không qua được, phải lướt.
- **Địch:**
  - 1 Brute đứng giữa hai xe cháy: chắn đường, phải bắn 4 phát hoặc nạp đạn.
  - 1 Sniper sau biển báo.
  - 1 Drone bay cao cuối phòng.
- **Vật phẩm:** Reploid #2 sau xe cháy thứ hai.'''),

 Room('R5', 'Bãi Ride Armor', 204, 2, 44, 22, 3, [
   F((0, 20), (44, 20)), B(10, 17, 4, 3), B(14, 14, 4, 6), B(18, 11, 26, 2),
   CW(30, 4, 7), E('V', 4, 19), E('A', 38, 9), E('B', 26, 19),
   X(18, 9.6, 'tầng 2'), X(31, 2.5, 'tường nứt'),
   PATH((2, 19), (43, 19)), ALT((5, 18), (12, 16), (16, 13), (22, 10), (29, 10)), ALT((33, 10), (37, 10))], '''
- **Mục đích:** lần đầu cưỡi **Ride Armor** và mở lối phụ bằng sức mạnh của nó.
- **Địa hình:**
  - Bãi đậu xe 2 tầng. Tầng dưới (y 22) là đường chính, tầng trên (y 13) là sàn bê tông vỡ.
  - Bậc thang khối bê tông cao 3 và 6 ô dẫn lên tầng 2. Ride Armor nhảy được bậc này, X đi bộ cũng lên được.
  - Ride Armor Pod đậu sẵn đầu phòng (x ≈ 208).
- **Địch:** 1 Brute ở tầng dưới. Ride Armor đấm 1 phát là hạ: cho người chơi cảm giác mạnh.
- **Lối phụ (Capsule Fourth Armor):**
  - **Tường bê tông nứt** ở tầng 2 (x ≈ 234). Chỉ Ride Armor đấm vỡ được (3 cú).
  - Sau tường là buồng nhỏ chứa capsule Fourth Armor (bộ đầy đủ).
  - Ride Armor không qua được cửa sang phòng sau: phải xuống xe ở cuối phòng.'''),

 Room('MID', 'Trực thăng tuần tra', 248, 8, 30, 16, 4, [
   F((0, 14), (30, 14)), B(0, 0, 2, 14), B(28, 0, 2, 14), E('M', 15, 4), X(9, 7, 'bay ngang + thả bom'),
   PATH((3, 13), (27, 13))], '''
- **Đấu trường phẳng 26 ô**, hai vách để đá tường lên tầm bắn.
- **Trực thăng tuần tra** bay ngang phía trên, đổi hướng ở hai vách.
- **Đòn đánh:**
  - Thả 3 quả bom thành hàng: chạy qua khe giữa các quả.
  - Hạ thấp càng quét ngang sàn (báo trước bằng đèn đỏ 1 giây): nhảy hoặc đá tường để né.
- **Điểm yếu:** cánh quạt chỉ trúng khi đá tường lên ngang tầm. Dạy rằng đá tường cũng là cách tấn công.
- **Phần thưởng:** mở cửa vào hầm. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R6', 'Đường hầm đèn vàng', 278, 12, 62, 12, 3, [
   F((0, 10), (62, 10)), B(0, 0, 40, 3), B(40, 0, 14, 1), B(54, 0, 8, 3), B(42, 2, 12, 1), Z('dark', 8, 3, 28, 7, 'đèn chớp 2s/1s'),
   E('C', 3, 9), E('D', 16, 6), E('D', 46, 6), E('R', 30, 9), E('H', 51, 1.6),
   PATH((2, 9), (61, 9)), ALT((38, 9), (41, 4), (41, 1.6), (49, 1.6))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** áp lực nhẹ trong không gian kín, chuẩn bị tinh thần cho boss.
- **Địa hình:**
  - Hầm thẳng 62 ô, trần thấp (cao 7 ô).
  - Đoạn giữa có đèn trần chớp: sáng 2 giây, tối 1 giây. Lúc tối chỉ thấy đèn mắt địch.
- **Địch:** 2 Drone lao vào từ hai đầu hầm theo đường chéo.
- **Vật phẩm:** Reploid #3 giữa hầm.
- **Lối phụ (Heart Tank):**
  - **Khe thông gió** trên trần ở x ≈ 318. Đứng dưới khe, lướt rồi nhảy (lướt-nhảy cao hơn nhảy thường) để bám vào miệng khe.
  - Trong ống thông gió phải bò ngang 10 ô, Heart Tank ở cuối ống.
  - Giáp Fourth (lơ lửng) vào khe dễ hơn.'''),

 Room('R7', 'Lối ra cao tốc', 340, 12, 30, 12, 2, [
   F((0, 10), (30, 10)), B(0, 0, 30, 3), BAR(29, 3, 1, 7, 'door'), E('R', 14, 9), X(20, 5, 'năng lượng nhỏ'),
   PATH((1, 9), (28, 9))], '''
- Phòng nghỉ trước boss: Reploid #4, một viên năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', '1D-1000 / High Max', 370, 4, 32, 20, 5, [
   F((0, 18), (32, 18)), B(0, 0, 2, 18), B(30, 0, 2, 18), B(0, 0, 32, 2), E('*', 16, 4),
   X(4, 8, 'nhện bám trần + 2 vách'), PATH((3, 17), (29, 17))], '''
- **Đấu trường 26 ô**, kín bốn phía. Trần và hai vách là nơi nhện 1D-1000 bò.
- **Pha 1** (100–50% HP):
  - Nhện bò dọc trần, thả bom nhện rơi thẳng.
  - Bò xuống một vách rồi lao ngang sàn: nhảy qua hoặc đá tường vách đối diện.
- **Pha 2** (dưới 50% HP):
  - Nhện giật đứt dây cáp trần, 3 đoạn cáp điện rơi xuống sàn thành vùng điện 2 giây.
  - Tốc độ bò tăng 30%.
- **Kết thúc:** hạ 1D-1000 thì High Max đáp xuống giữa sân. Trận này **không thể thắng**: sau 20 giây hoặc khi X còn 1/4 máu thì chuyển cảnh.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Cao tốc Neo Arcadia', en='Neo Arcadia Highway — Intro', boss='1D-1000 → High Max', act='Mở đầu', theme=THEME,
 capsule='Fourth Armor (bộ đầy đủ)',
 subtitle='Area 1 (ngoài trời): R1 → R2 → R3 (leo dọc) → R4 → R5 (Ride Armor) → Mini-boss  |  Area 2 (trong hầm): R6 → R7 → Boss',
 keep='Boss 1D-1000 → High Max, capsule Fourth Armor và Ride Armor Pod giữ nguyên; thêm 4 Reploid, 1 Heart Tank, 1 Sub-Tank và thay toàn bộ địa hình.',
 concept='Cao tốc trên cao của Neo Arcadia bị đánh sập lúc hoàng hôn. Đây là màn dạy chơi: **mỗi phòng dạy đúng một kỹ năng** và cho thử ngay trong vùng an toàn trước khi dùng thật.',
 areas=['**Area 1 – Cao tốc (ngoài trời):** bê tông, cột đèn đổ, trời cam. Dạy chạy, bắn, nhảy hố, đá tường, lướt, rồi cưỡi Ride Armor.',
        '**Area 2 – Hầm (trong nhà):** hầm tối đèn vàng. Ôn lại mọi thứ trong không gian chật, có bí mật trên trần.'],
 flow='chạy ngang → nhảy hố → leo dọc lần đầu → lướt qua khe → cưỡi Ride Armor phá tường → hầm tối → boss nhện bám trần',
 time='khoảng 4–5 phút lần đầu, khoảng 2 phút khi đã quen',
 refs=['**X4 / X5, màn mở đầu:** mỗi đoạn dạy một kỹ năng, boss kích thước lớn, kết thúc bằng trận không thể thắng để dẫn truyện.',
       '**X8, màn mở đầu (Noah\'s Park):** màn "thẳng", không có cơ chế nặng; vật thể lớn cháy nổ làm vật cản.',
       '**X8 16-bit demake:** cùng bố cục mở đầu nhưng làm lại dạng 2D thuần, có bí mật dưới gầm cầu.',
       '**Mega Man X (SNES), màn cao tốc:** cầu sập, mặt đường làm sàn chính. Chỉ lấy nhịp dạy kỹ năng, không chép bố cục.'],
 engine=['Bảng chỉ dẫn nút hiện theo vùng (Entity `Tutorial` có chữ và nút).',
         'Hố "dạy chơi": rơi thì mất 2 máu và đặt lại ở mép thay vì mất mạng (cờ `softPit` trên vùng).',
         'Ride Armor Pod: lên/xuống xe, đấm, nhảy thấp. Xe không qua được cửa phòng.',
         'Tường nứt chỉ Ride Armor phá được (thuộc tính `breakBy: rideArmor`).',
         'Đèn trần chớp theo nhịp làm tối khung hình.',
         'Mini-boss Trực thăng tuần tra; boss nhện bò trên trần và vách (di chuyển theo viền đấu trường).'],
 art=['**Tileset "Cao tốc" (Area 1):** 47 ô viền bê tông, mặt đường kẻ vạch, mép gãy có cốt thép, trụ cầu.',
      '**Tileset "Hầm" (Area 2):** 47 ô viền, ô đèn vàng, ô ống thông gió.',
      '**Vật thể:** xe cháy (lửa 4 khung), biển báo sập, khối bê tông, tường nứt (2 trạng thái), cửa boss.',
      '**Nền:** Area 1: thành phố hoàng hôn và khói (2 lớp parallax). Area 2: vách hầm và quạt thông gió (2 lớp).'],
)
STAGE['rooms'] = rooms
