from lib import *

THEME = dict(bg1=(34, 28, 52), bg2=(24, 22, 44), rock1=(100, 92, 124), rock2=(86, 80, 116))

rooms = [
 Room('R1', 'Sảnh đài thiên văn', 0, 50, 40, 14, 2, [
   B(0, 0, 40, 2), F((0, 10), (40, 10)), E('S', 30, 9), E('D', 14, 5), X(3, 7, 'mô hình hành tinh'),
   PATH((1, 9), (39, 9))], '''
- **Mục đích:** mở đầu yên tĩnh. Ánh sao chiếu trên trần báo hiệu chủ đề vũ trụ.
- **Địa hình:** sảnh 40 ô, trần ở y 52, sàn ở y 60.
- **Địch:**
  - 1 Drone dạng dơi máy, bay vòng rồi lao xuống.
  - 1 Sniper cuối sảnh.
- **Trang trí:** mô hình hành tinh treo trần, kính viễn vọng, bảng chiêm tinh.'''),

 Room('R2', 'Phòng chiếu sao', 40, 44, 64, 20, 3, [
   F((0, 16), (8, 16)), F((56, 16), (64, 16)), H('void', 8, 16, 48, 4), Z('grav', 0, 0, 64, 16, 'trọng lực ×0.42'),
   P(12, 13, 5, 'move'), P(24, 9, 5, 'move'), P(36, 12, 5, 'move'), P(46, 8, 5, 'move'),
   E('D', 30, 4), E('D', 52, 4), E('R', 26, 8),
   PATH((1, 15), (8, 15), (14, 12), (26, 8), (38, 11), (48, 7), (57, 15), (63, 15))], '''
- **Mục đích:** giới thiệu **trọng lực thấp** (×0.42): nhảy cao và xa hơn, nhưng rơi chậm nên dễ bị bắn.
- **Địa hình:**
  - Mái vòm chiếu sao dài 64 ô. Giữa phòng là vực rộng 48 ô.
  - **4 bệ thiên thể** trôi theo quỹ đạo elip nhỏ (bán kính 2–3 ô, chu kỳ 4 giây).
  - Bệ trôi chậm nên dễ đáp, nhưng phải tính hướng trôi.
- **Địch:** 2 Drone dơi. Trong trọng lực thấp, bị bắn trúng thì bị đẩy lùi xa hơn bình thường.
- **Vật phẩm:** Reploid #1 trên bệ thứ hai.'''),

 Room('R3', 'Vùng Time Zone', 104, 48, 52, 16, 4, [
   B(0, 0, 52, 2), F((0, 12), (52, 12)), Z('slow', 14, 2, 24, 10, 'Time Zone ×0.5'),
   H('trash', 18, 2, 2, 7), H('trash', 26, 5, 2, 7), H('trash', 34, 2, 2, 7), X(17, 10.5, 'búa lắc nhanh'),
   E('S', 30, 11), E('D', 46, 5), PATH((1, 11), (51, 11))], '''
- **Mục đích:** giới thiệu **vùng làm chậm** (Time Zone). Bên trong vùng, mọi thứ chậm còn một nửa, kể cả người chơi.
- **Địa hình:** hành lang 52 ô, trần ở y 50, sàn ở y 60.
- **Bẫy – búa lắc:**
  - 3 búa lắc từ trần xuống, rất nhanh (chu kỳ 0.8 giây). Bên ngoài vùng làm chậm thì gần như không qua được.
  - Vùng Time Zone phủ đúng đoạn búa: búa chậm còn chu kỳ 1.6 giây, đủ để luồn qua.
- **Địch:**
  - 1 Sniper đứng trong vùng: đạn của nó chậm nên dễ né, nhưng người chơi cũng chậm.
  - 1 Drone ngoài vùng ở cuối hành lang.
- **Mẹo:** đạn của X bay ra khỏi vùng thì nhanh lại. Đứng trong vùng bắn ra ngoài là lợi thế.'''),

 Room('R4', 'Đỉnh đài', 156, 16, 22, 46, 4, [
   B(0, 0, 2, 36), B(0, 44, 22, 2), B(20, 8, 2, 36), B(2, 0, 18, 1), Z('grav', 2, 1, 18, 43, ''),
   P(12, 37, 5, 'move'), P(4, 29, 5, 'move'), P(13, 21, 5, 'move'), P(5, 13, 5, 'move'), P(2, 4, 5),
   X(3, 40, 'trọng lực ×0.42'), E('A', 4, 3), E('D', 11, 25),
   PATH((1, 43), (10, 43), (14, 36), (6, 28), (15, 20), (7, 12), (14, 6), (21.5, 5)), ALT((7, 12), (5, 3))], '''
- **Mục đích:** đoạn dọc trong trọng lực thấp. Leo bằng bệ quỹ đạo thay vì đá tường.
- **Địa hình:**
  - Giếng rộng 18 ô, cao 43 ô (từ y 60 lên y 17).
  - 4 bệ thiên thể trôi lên xuống 3 ô, chu kỳ 3 giây.
  - Vách đá tường được, nhưng trọng lực thấp làm mỗi cú đá tường bay xa ra khỏi vách: khó leo thẳng hơn bình thường.
- **Địch:** 1 Drone dơi.
- **Lối phụ (Capsule Gaea Head):**
  - Kệ capsule sát trần bên trái (x ≈ 158, y ≈ 20), cao hơn lối ra.
  - Đứng trên bệ thứ tư lúc nó lên cao nhất rồi nhảy hết lực: trọng lực thấp vừa đủ đưa lên tới kệ.
  - Nhảy lúc bệ đang xuống là thiếu khoảng 2 ô.'''),

 Room('MID', 'Người gác cổng', 178, 12, 30, 16, 5, [
   B(0, 0, 30, 1), B(0, 0, 2, 4), B(28, 0, 2, 12), F((0, 12), (30, 12)), E('M', 18, 5), E('G', 6, 6), E('G', 24, 6),
   X(4, 9.5, 'dịch chuyển giữa 2 cổng'), PATH((1, 11), (27, 11))], '''
- **Đấu trường 26 ô**, hai cổng dịch chuyển lơ lửng ở hai bên.
- **Người gác cổng** là một khối cầu tinh vân, dịch chuyển qua lại giữa hai cổng.
- **Đòn đánh:**
  - Hiện ra từ một cổng và bắn chùm 6 sao theo vòng tròn.
  - Mở hố đen nhỏ 2 giây giữa sân, hút người chơi về tâm (đá tường ra vách để chống lại).
  - Chui vào một cổng, ra ở cổng kia và lao ngang.
- **Điểm yếu:** chỉ trúng đạn trong 1 giây ngay khi vừa ra khỏi cổng.
- **Phần thưởng:** mở cửa vào khu cổng dịch chuyển. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Mê cung cổng', 208, 12, 56, 16, 5, [
   B(0, 0, 56, 2), F((0, 12), (56, 12)), B(18, 2, 2, 10), B(38, 2, 2, 10), B(20, 6, 18, 1),
   E('G', 14, 11), E('G', 22, 11), E('G', 34, 11), E('G', 42, 11), E('G', 24, 5),
   E('C', 2, 11), E('R', 30, 11), E('B', 48, 11), E('T', 32, 4),
   X(10, 8, 'cổng xanh → xanh'), X(30, 3, 'cổng tím: vòng về đầu'),
   PATH((1, 11), (13, 11)), PATH((23, 11), (33, 11)), PATH((43, 11), (55, 11)), ALT((24, 5), (32, 4))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** câu đố nhẹ bằng **cổng dịch chuyển**, đồng thời là chỗ nghỉ sau mini-boss.
- **Địa hình:** 3 buồng nối nhau, ngăn bởi 2 vách kín. Chỉ đi qua được bằng cổng.
- **Cơ chế:**
  - Cổng cùng màu nối với nhau. Cổng xanh ở buồng 1 dẫn sang buồng 2, cổng xanh ở buồng 2 dẫn sang buồng 3.
  - **Cổng tím** ở buồng 2 trông giống lối đi tiếp, nhưng đưa về đầu phòng.
  - Đi qua cổng giữ nguyên tốc độ và hướng: lao vào cổng bằng lướt thì ra khỏi cổng vẫn lướt.
- **Địch:** 1 Brute ở buồng 3.
- **Vật phẩm:** Reploid #2 ở buồng 2.
- **Lối phụ (Sub-Tank):** buồng 2 có gác lửng phía trên, chỉ vào được bằng cách lướt vào cổng tím từ trên cao thì ra ở cửa gác lửng.'''),

 Room('R6', 'Quỹ đạo hố đen', 264, 4, 60, 30, 7, [
   F((0, 20), (6, 20)), F((54, 20), (60, 20)), H('void', 6, 28, 48, 2), Z('grav', 18, 6, 24, 20, 'hút về tâm 80px/s'),
   H('void', 28, 14, 4, 4), P(12, 16, 4, 'move'), P(22, 8, 4, 'move'), P(36, 8, 4, 'move'), P(44, 16, 4, 'move'), P(28, 24, 4, 'move'),
   X(26, 18.5, 'hố đen'), E('D', 20, 3), E('D', 48, 4), E('H', 30, 23),
   PATH((1, 19), (6, 19), (13, 15), (23, 7), (37, 7), (45, 15), (55, 19), (59, 19)), ALT((45, 15), (32, 23))], '''
- **Mục đích:** cao trào của màn. Đi vòng quanh một **hố đen** đang hút người chơi vào.
- **Địa hình:**
  - Phòng mô phỏng vũ trụ rộng 60 ô, cao 26 ô. Không có sàn giữa hai bệ đầu và cuối.
  - **5 bệ quỹ đạo** quay quanh hố đen theo vòng tròn bán kính 9 ô, ngược chiều kim đồng hồ, mỗi vòng 12 giây.
- **Cơ chế – hố đen:**
  - Hút mọi thứ về tâm, lực **80px/giây** ở rìa vùng, mạnh dần khi lại gần.
  - Chạm lõi là mất mạng.
  - Người chơi phải đi qua nửa trên của quỹ đạo, nhảy theo hướng bệ đang trôi.
  - Đạn bay qua vùng hút cũng bị bẻ cong.
- **Địch:** 2 Drone dơi. Dơi miễn lực hút.
- **Lối phụ (Heart Tank):**
  - Nằm trên bệ quỹ đạo thấp nhất, ngay dưới hố đen (x ≈ 294, y ≈ 27). Bệ này đi qua nửa dưới, nơi lực hút kéo người chơi lên phía lõi.
  - Nhảy xuống bệ đúng lúc nó đi qua đáy, lấy Heart Tank, rồi lướt ra ngoài theo hướng tiếp tuyến.
  - Giáp Gaea nặng hơn, ít bị hút hơn.'''),

 Room('R7', 'Hành lang tinh vân', 324, 14, 50, 14, 6, [
   B(0, 0, 50, 2), F((0, 10), (50, 10)), Z('dark', 10, 2, 30, 8, 'tối 1.5s mỗi 4s'), P(18, 6, 6), P(30, 5, 6),
   E('C', 2, 9), E('R', 24, 9), E('S', 44, 9), E('D', 34, 3), PATH((1, 9), (49, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: tối từng đợt, trọng lực thường trở lại (đổi cảm giác sau cả màn trọng lực thấp).
- **Địa hình:** hành lang 50 ô, 2 kệ treo giữa.
- **Cơ chế – mạch tối:** đèn tắt 1.5 giây mỗi 4 giây. Lúc tối chỉ thấy đường viền kệ và đèn mắt địch.
- **Địch:**
  - 1 Drone dơi, chỉ tấn công lúc tối.
  - 1 Sniper cuối hành lang.
- **Vật phẩm:** Reploid #3 giữa hành lang.'''),

 Room('R8', 'Cửa đài quan sát', 374, 14, 26, 14, 2, [
   B(0, 0, 26, 2), F((0, 10), (26, 10)), BAR(25, 2, 1, 8, 'door'), E('R', 12, 9), X(3, 4, 'năng lượng nhỏ'), PATH((1, 9), (24, 9))], '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Dark Necrobat', 400, 10, 32, 18, 6, [
   B(0, 0, 2, 14), B(30, 0, 2, 14), B(0, 0, 32, 1), F((0, 14), (32, 14)), Z('grav', 2, 1, 28, 13, ''), E('*', 20, 5),
   X(4, 10, 'trọng lực ×0.42'), PATH((3, 13), (29, 13))], '''
- **Đấu trường 28 ô** dưới mái vòm, trọng lực thấp ×0.42.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (dơi con, sóng âm, hút máu).
- **Pha 2** (dưới 50% HP):
  - **Dark Hold:** định thân người chơi 1 giây (màn hình đảo màu báo trước 0.5 giây).
  - Mái vòm tắt đèn từng đợt như R7, Necrobat chỉ hiện bóng.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Đài thiên văn', en='Planetarium', boss='Dark Necrobat', act='Act I · X5', theme=THEME, capsule='Gaea Head',
 subtitle='Area 1 (đài thiên văn): R1 → R2 (trọng lực thấp) → R3 (Time Zone) → R4 (leo) → Mini-boss  |  Area 2 (mô phỏng vũ trụ): R5 (cổng) → R6 (hố đen) → R7 → R8 → Boss',
 keep='Boss, capsule Gaea Head, trọng lực thấp 0.42, vùng Time Zone và cổng dịch chuyển vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Một đài thiên văn đang chạy mô phỏng vũ trụ. Màn này **đổi luật vật lý**: trọng lực thấp, thời gian chậm, cổng dịch chuyển, rồi hố đen hút người chơi về tâm.',
 areas=['**Area 1 – Đài thiên văn:** tím đậm, đèn sao, đồng thau. Dạy trọng lực thấp, vùng làm chậm, leo bằng bệ quỹ đạo.',
        '**Area 2 – Phòng mô phỏng vũ trụ:** đen, tinh vân, lưới tọa độ. Cổng dịch chuyển, hố đen, đèn tắt từng đợt.'],
 flow='nhảy bổng trong trọng lực thấp → luồn búa trong vùng làm chậm → leo bằng bệ quỹ đạo → mini-boss dịch chuyển → giải mê cung cổng → vòng quanh hố đen → hành lang tối → boss',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, màn Dark Necrobat:** đài thiên văn, trọng lực thấp, capsule Gaea Head trên bệ cao.',
       '**X4, màn Split Mushroom / X8, màn Dark Mantis:** vùng tối theo nhịp, địch chỉ tấn công lúc tối.',
       '**X6, màn Infinity Mijinion:** vật thể bay theo quỹ đạo quanh tâm.',
       '**X8, màn Gravity Antonion:** đổi luật vật lý làm cơ chế chính của màn.',
       '**X Corrupted:** cổng dịch chuyển giữ nguyên quán tính, dùng để mở lối phụ.'],
 engine=['Vùng trọng lực tùy chỉnh (hệ số theo vùng).',
         'Vùng làm chậm thời gian: chậm người chơi, địch, bẫy và đạn bên trong vùng.',
         'Bệ quỹ đạo: di chuyển theo vòng tròn hoặc elip quanh một tâm.',
         'Cổng dịch chuyển theo cặp màu, giữ nguyên vận tốc.',
         'Hố đen: lực hút về tâm tăng theo khoảng cách, bẻ cong đạn.',
         'Mạch tối theo nhịp; Dark Hold định thân người chơi.',
         'Mini-boss Người gác cổng.'],
 art=['**Tileset "Đài thiên văn" (Area 1):** 47 ô viền đá tím, đồng thau, mái vòm.',
      '**Tileset "Mô phỏng vũ trụ" (Area 2):** 47 ô viền đen có lưới tọa độ phát sáng.',
      '**Vật thể:** bệ thiên thể (4 khung xoay), búa lắc, cổng dịch chuyển (2 màu, 4 khung), hố đen (4 khung), vùng Time Zone (viền sáng).',
      '**Nền:** Area 1: bầu trời sao chiếu trên mái vòm (2 lớp parallax). Area 2: tinh vân và thiên hà xa (2 lớp).'],
)
STAGE['rooms'] = rooms
