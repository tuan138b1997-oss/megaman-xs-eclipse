from lib import *

THEME = dict(bg1=(44, 58, 80), bg2=(40, 44, 58), rock1=(130, 136, 150), rock2=(112, 116, 132))

rooms = [
 Room('R1', 'Đường băng', 0, 40, 50, 16, 2, [
   F((0, 10), (46, 10)), H('void', 46, 10, 4, 6), Z('wind', 0, 0, 50, 10, 'gió nhẹ'), E('S', 30, 9), E('D', 40, 4),
   X(2, 5, 'mép tàu sân bay'), PATH((1, 9), (45, 9), (49.5, 11))], '''
- **Mục đích:** mở đầu trên **tàu sân bay đang bay** giữa trời. Rơi khỏi mép là mất mạng.
- **Địa hình:**
  - Đường băng dài 46 ô, mặt sàn ở y 50.
  - Cuối đường băng là mép tàu. Phải nhảy sang chiến hạm 1 ở thấp hơn một chút.
- **Địch:**
  - 1 Sniper giữa đường băng.
  - 1 Drone dạng máy bay nhỏ, bay vòng rồi bổ nhào.
- **Gió:** gió nhẹ, chỉ làm hiệu ứng (mây bay, cờ phần phật), không đẩy.
- **Trang trí:** máy bay đậu, đèn hiệu đường băng, mây trôi dưới chân.'''),

 Room('R2', 'Chiến hạm 1', 50, 38, 76, 18, 3, [
   F((0, 12), (32, 12)), H('void', 32, 12, 6, 6), F((38, 10), (76, 10)), B(14, 8, 4, 4), B(56, 6, 4, 4),
   Z('wind', 0, 0, 76, 10, 'gió giật ← 2s mỗi 5s'), AR(30, 4, -6, 0), AR(66, 3, -6, 0), X(32, 15, 'khe giữa 2 tàu'),
   E('S', 26, 11), E('S', 62, 5), E('D', 44, 4), E('R', 70, 9),
   PATH((1, 11), (13, 11), (16, 7), (19, 11), (31, 11), (35, 8), (39, 9), (55, 9), (58, 5), (61, 9), (75, 9))], '''
- **Mục đích:** dạy **gió giật**: gió không thổi liên tục mà giật từng đợt, phải đọc tín hiệu.
- **Địa hình:**
  - Boong chiến hạm 1 dài 32 ô, rồi khe 6 ô, rồi boong chiến hạm 2 cao hơn 2 ô.
  - Hai tháp pháo đã hỏng làm vật che chắn.
- **Bẫy – gió giật:**
  - Mỗi 5 giây có một đợt gió ngược thổi 2 giây, đẩy lùi 90px/giây.
  - Cờ trên cột buồm dựng thẳng 1 giây trước mỗi đợt.
  - Nhảy qua khe giữa hai tàu đúng lúc gió giật thì rơi.
- **Địch:**
  - 1 Sniper trên boong 1.
  - 1 Sniper trên nóc tháp pháo boong 2.
  - 1 Drone lượn trên khe.
- **Vật phẩm:** Reploid #1 cuối boong 2.'''),

 Room('R3', 'Thân tàu', 126, 12, 20, 38, 4, [
   B(0, 0, 2, 30), B(0, 36, 20, 2), B(18, 8, 2, 28), B(2, 0, 16, 1),
   P(12, 30, 4), P(2, 24, 4), P(12, 17, 4), P(2, 10, 4), H('trash', 8, 21, 4, 2), X(6, 23.3, 'quạt tản nhiệt'),
   E('D', 10, 13), PATH((1, 35), (9, 35), (14, 29), (4, 23), (14, 16), (4, 9), (11, 5), (19.5, 4))], '''
- **Mục đích:** đoạn dọc bên trong thân tàu, không gió: chỗ nghỉ nhịp giữa các boong.
- **Địa hình:** khoang thông gió rộng 16 ô, cao 34 ô (từ y 48 lên y 14). 4 kệ nghỉ.
- **Bẫy – quạt tản nhiệt:** quạt đặt ngang giữa khoang, cánh quay chạm là mất máu. Quạt dừng 1.5 giây mỗi 3 giây, chỉ lúc đó mới leo qua được.
- **Địch:** 1 Drone gần lối ra.
- **Lối ra:** cửa sập trên boong phía trên, mở ra khu quạt nâng khí.'''),

 Room('R4', 'Quạt nâng khí', 146, 4, 64, 24, 5, [
   F((0, 16), (8, 16)), F((56, 14), (64, 14)), H('void', 8, 18, 48, 6),
   Z('updraft', 12, 2, 6, 20, 'nâng 160px/s'), Z('updraft', 28, 2, 6, 20, ''), Z('updraft', 44, 2, 6, 20, ''),
   BAR(12, 22, 6, 1, 'trash'), BAR(28, 22, 6, 1, 'trash'), BAR(44, 22, 6, 1, 'trash'), P(28, 3, 6),
   AR(15, 20, 0, -6, 'updraft'), AR(31, 20, 0, -6, 'updraft'), AR(47, 20, 0, -6, 'updraft'),
   E('D', 22, 8), E('D', 40, 10), E('H', 31, 2),
   PATH((1, 15), (8, 15), (15, 12), (22, 13), (31, 11), (38, 12), (47, 10), (57, 13), (63, 13)), ALT((31, 11), (31, 3))], '''
- **Mục đích:** vượt khoảng không 48 ô bằng **luồng khí nâng**.
- **Địa hình:** bệ xuất phát và bệ đích, giữa là khoảng trời không đáy.
- **Cơ chế – quạt nâng khí:**
  - 3 quạt lớn thổi thẳng lên, nâng người chơi 160px/giây khi ở trong luồng.
  - Thả trôi trong luồng thì lơ lửng. Lướt ngang ra khỏi luồng thì rơi chậm dần sang luồng kế tiếp.
  - Khoảng cách giữa các luồng là 10 ô: phải lướt trên không mới tới.
- **Địch:** 2 Drone bay cắt ngang giữa các luồng. Bị bắn trúng giữa không trung là rơi khỏi luồng.
- **Lối phụ (Heart Tank):**
  - Luồng giữa nâng cao hơn hai luồng kia, lên tới một bệ nhỏ trên đỉnh (x ≈ 177, y ≈ 7).
  - Giữ nguyên trong luồng tới đỉnh thì đáp lên bệ, lấy Heart Tank.
  - Lên quá cao thì mất đà sang luồng thứ ba, phải rơi về luồng giữa rồi đi tiếp.'''),

 Room('MID', 'Pháo đài hộ tống', 210, 4, 32, 20, 5, [
   F((0, 14), (32, 14)), H('void', 0, 18, 32, 2), E('M', 22, 6), Z('wind', 0, 0, 32, 14, ''), X(3, 3, 'boong nhỏ, không vách'),
   PATH((1, 13), (31, 13))], '''
- **Đấu trường là boong một tàu hộ tống**, dài 32 ô, **không có vách**. Rơi là mất mạng.
- **Pháo đài hộ tống** bay sát bên phải boong, chỉ lộ tháp pháo và lõi động cơ.
- **Đòn đánh:**
  - Tháp pháo bắn loạt 3 đạn thẳng.
  - Thả 2 drone nhỏ bám theo người chơi.
  - Bật động cơ thổi gió ngang đẩy người chơi về mép trái (2 giây, có tiếng rú báo trước).
- **Điểm yếu:** lõi động cơ, chỉ mở khi đang thổi gió. Phải vừa chống gió vừa bắn.
- **Phần thưởng:** mở đường lên tầng mây. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Tầng mây', 242, 0, 70, 26, 7, [
   F((0, 18), (6, 18)), F((64, 16), (70, 16)), H('void', 6, 22, 58, 4),
   P(10, 16, 5, 'move'), P(20, 12, 5, 'move'), P(32, 15, 5, 'move'), P(44, 10, 5, 'move'), P(56, 13, 5, 'move'), P(38, 21, 4),
   Z('wind', 6, 0, 58, 21, 'gió ngang đổi chiều mỗi 4s'), AR(14, 3, 6, 0), AR(52, 3, -6, 0),
   E('C', 2, 17), E('D', 26, 5), E('D', 50, 4), E('S', 46, 9), E('T', 40, 20),
   PATH((1, 17), (6, 17), (12, 15), (22, 11), (34, 14), (46, 9), (58, 12), (65, 15), (69, 15)), ALT((34, 14), (40, 20))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** cao trào của màn. Nhảy trên các bệ bay trong gió đổi chiều.
- **Địa hình:** khoảng trời rộng 58 ô giữa hai boong, chỉ có **5 bệ bay** (rộng 5 ô).
- **Cơ chế:**
  - Bệ bay qua lại theo đường ngang 6 ô, mỗi bệ một tốc độ (60–100px/giây).
  - **Gió ngang đổi chiều mỗi 4 giây**, đẩy 70px/giây. Mũi tên trên HUD báo chiều gió sắp tới 1 giây trước.
  - Nhảy xuôi gió thì xa, nhảy ngược gió thì hụt.
- **Địch:**
  - 2 Drone bay vòng.
  - 1 Sniper đứng trên bệ bay thứ tư: phải hạ nó trước khi nhảy lên.
- **Lối phụ (Sub-Tank):**
  - Một bệ mây cứng nằm thấp dưới bệ thứ ba (x ≈ 280, y ≈ 21), gần sát vùng rơi.
  - Thả người xuống từ bệ thứ ba lúc gió đang thổi về phía bệ mây, rồi đá lên lại bệ thứ ba khi nó bay qua.
  - Giáp Falcon bay tự do: lấy an toàn.'''),

 Room('R6', 'Chiến hạm 4', 312, 2, 64, 18, 6, [
   F((0, 14), (64, 14)), H('void', 0, 16, 64, 2), Z('updraft', 54, 2, 5, 12, ''), P(48, 1, 8), E('A', 52, 0),
   X(4, 3, 'boong nghiêng 15° mỗi 4s'), AR(56, 12, 0, -8, 'updraft'),
   E('C', 2, 13), E('R', 18, 13), E('W', 24, 13), E('B', 30, 13), E('R', 36, 13), E('W', 44, 13), E('S', 60, 13),
   PATH((1, 13), (63, 13)), ALT((56, 13), (56, 2), (52, 0.5))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp mọi thứ: boong nghiêng, tháp pháo, gió, và luồng khí nâng cuối cùng.
- **Địa hình:**
  - Boong chiến hạm 4 dài 64 ô, mặt boong ở y 16.
  - **Boong nghiêng 15° sang trái mỗi 4 giây** (giữ nghiêng 1.5 giây rồi trở lại). Người chơi trượt xuống phía trái 100px/giây khi boong nghiêng.
- **Bẫy:** 2 **tháp pháo** trên boong, bắn đạn cong. Bắn hạ được bằng 4 viên đạn thường.
- **Địch:**
  - 1 Brute giữa boong: khi boong nghiêng nó trượt về phía người chơi.
  - 1 Sniper cuối boong.
- **Vật phẩm:** Reploid #2 và #3 trên boong.
- **Lối phụ (Capsule Gaea Body):**
  - Cuối boong có **luồng khí nâng** của ống xả động cơ, thổi lên bệ ăng-ten (x ≈ 360, y ≈ 3).
  - Luồng chỉ bật khi boong đang nghiêng. Đứng sẵn trong luồng thì bị trượt ra khỏi luồng, nên phải lướt vào đúng lúc boong bắt đầu nghiêng.'''),

 Room('R7', 'Cầu chỉ huy', 376, 4, 28, 14, 2, [
   B(0, 0, 28, 2), F((0, 12), (28, 12)), BAR(27, 2, 1, 10, 'door'), E('R', 13, 11), X(3, 5, 'năng lượng nhỏ'), PATH((1, 11), (26, 11))], '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss lên nóc tàu chỉ huy.'''),

 Room('BOSS', 'Spiral Pegacion', 404, 0, 32, 18, 6, [
   F((0, 16), (32, 16)), Z('wind', 0, 0, 32, 16, 'pha 2: gió đẩy ra mép'), E('*', 20, 6), AR(16, 8, 7, 0), AR(16, 10, -7, 0),
   PATH((1, 15), (31, 15))], '''
- **Đấu trường là nóc tàu chỉ huy dài 32 ô**, **không vách**, rơi là mất mạng.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (lốc xoáy, lao chéo, bão cánh).
- **Pha 2** (dưới 50% HP):
  - Pegacion bay vòng quanh tàu, tạo **gió đẩy ra mép**: luôn đẩy người chơi về phía mép gần hơn, 60px/giây.
  - Đứng giữa sân thì gió từ hai phía triệt tiêu: đây là chỗ an toàn, nhưng Pegacion hay lao vào đúng giữa.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Không quân', en='Reploid Air Force', boss='Spiral Pegacion', act='Act I · X5', theme=THEME, capsule='Gaea Body',
 subtitle='Area 1 (boong tàu và thân tàu): R1 → R2 (gió giật) → R3 (leo) → R4 (quạt nâng khí) → Mini-boss  |  Area 2 (tầng mây): R5 (bệ bay) → R6 (boong nghiêng) → R7 → Boss',
 keep='Boss, capsule Gaea Body, quạt nâng khí Updraft, bệ bay và sub-boss pháo đài hộ tống vẫn giữ; thêm 4 Reploid, Sub-Tank và thay địa hình. Heart Tank giữ trên đỉnh luồng khí nâng.',
 concept='Hạm đội không quân Reploid bay giữa tầng mây. Màn này là **gió**: gió giật, gió đổi chiều, luồng khí nâng. Không có vực có đáy: rơi là mất. Người chơi học đọc gió như đọc nhịp bẫy.',
 areas=['**Area 1 – Boong tàu và thân tàu:** trời xanh, thép xám, mây dưới chân. Dạy gió giật, nhảy giữa hai tàu, luồng khí nâng.',
        '**Area 2 – Tầng mây:** hoàng hôn, mây dày. Bệ bay trong gió đổi chiều, rồi boong nghiêng có luồng khí lên capsule.'],
 flow='chạy đường băng → nhảy giữa hai tàu trong gió giật → leo thân tàu → bay qua quạt nâng khí → mini-boss trên boong không vách → nhảy bệ bay trong gió đổi chiều → boong nghiêng → boss trên nóc tàu',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, màn Spiral Pegacion:** hạm đội bay, quạt nâng khí, pháo đài hộ tống làm sub-boss, capsule trên boong tàu cuối.',
       '**X (SNES), màn Storm Eagle:** đấu trường trên nóc tàu không vách, gió đẩy ra mép.',
       '**X6, màn Commander Yammark / X8, màn Gigabolt Man-O-War:** bệ bay theo đường cố định trên khoảng không.',
       '**X8 16-bit demake:** dựng lại đoạn bay trên tàu thành màn chơi thường, không tự cuộn.',
       '**X Corrupted:** luồng nâng chỉ bật theo nhịp của một cơ chế khác (boong nghiêng).'],
 engine=['Gió giật theo lịch (bật/tắt có tín hiệu báo trước), gió đổi chiều, gió đẩy ra mép.',
         'Luồng khí nâng: lực đẩy lên theo vùng, có thể bật/tắt theo điều kiện.',
         'Bệ bay qua lại theo đường cố định, mỗi bệ một tốc độ.',
         'Boong nghiêng theo nhịp: làm người chơi và địch trượt.',
         'Tháp pháo bắn đạn cong, phá được.',
         'Quạt tản nhiệt có nhịp quay/dừng.',
         'Mini-boss Pháo đài hộ tống bay cạnh boong.'],
 art=['**Tileset "Boong tàu" (Area 1):** 47 ô viền thép, mặt boong kẻ vạch, mép tàu, tháp pháo hỏng.',
      '**Tileset "Tầng mây" (Area 2):** 47 ô viền, bệ bay, mây cứng, ăng-ten.',
      '**Vật thể:** cờ báo gió (3 khung), quạt nâng khí (4 khung), quạt tản nhiệt, tháp pháo (3 khung), boong nghiêng.',
      '**Nền:** Area 1: trời xanh và tàu bay xa (2 lớp parallax). Area 2: biển mây hoàng hôn (2 lớp).'],
)
STAGE['rooms'] = rooms
