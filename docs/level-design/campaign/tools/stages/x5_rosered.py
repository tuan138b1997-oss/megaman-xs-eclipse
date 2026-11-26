from lib import *

THEME = dict(bg1=(30, 46, 34), bg2=(36, 34, 30), rock1=(96, 82, 62), rock2=(112, 86, 60))

rooms = [
 Room('R1', 'Bìa rừng', 0, 40, 44, 16, 2, [
   F((0, 12), (14, 12), (18, 10), (30, 10), (34, 12), (44, 12)), H('thorn', 22, 9, 4, 1), X(19, 6, 'bụi gai độc'),
   E('S', 36, 11), E('D', 10, 5), PATH((1, 11), (14, 11), (20, 9), (22, 7), (27, 7), (30, 9), (43, 11))], '''
- **Mục đích:** giới thiệu **bụi gai độc**: chạm là mất máu và bị nhiễm độc (mất thêm 1 máu mỗi giây trong 3 giây).
- **Địa hình:**
  - Bìa rừng 44 ô, đất mấp mô, mặt đất ở y 52 và y 50.
  - Một gò đất có bụi gai ở giữa: nhảy qua, không có cách khác.
- **Địch:**
  - 1 Drone dạng ong máy, bay theo đường sóng.
  - 1 Sniper ở chân gò.
- **Trang trí:** cây máy gãy, dây cáp như dây leo, nấm phát sáng nhỏ.'''),

 Room('R2', 'Rừng nấm hai tầng', 44, 30, 80, 26, 3, [
   F((0, 22), (80, 22)), H('thorn', 10, 21, 18, 1), H('thorn', 34, 21, 18, 1), H('thorn', 58, 21, 12, 1),
   P(6, 21, 3, 'bounce'), P(30, 21, 3, 'bounce'), P(54, 21, 3, 'bounce'), P(10, 8, 14), P(34, 9, 14), P(58, 8, 14),
   X(4, 23.4, 'nấm bật 8 ô'), E('D', 20, 4), E('S', 40, 8), E('B', 46, 20.4), E('R', 66, 7),
   PATH((1, 21), (7, 20), (10, 7), (24, 7), (31, 20), (34, 8), (48, 8), (55, 20), (58, 7), (72, 7), (79, 21)),
   ALT((24, 7), (28, 21), (52, 21))], '''
- **Mục đích:** dạy **nấm bật nhảy** và chọn tầng: dưới đất toàn gai, trên tán cây an toàn hơn nhưng có địch.
- **Địa hình:**
  - Rừng 80 ô. Mặt đất ở y 52 gần như phủ kín bụi gai độc, chỉ chừa chỗ mọc nấm.
  - **3 cây nấm bật**: đáp lên thì bật cao 8 ô. Giữ NHẢY khi đáp thì bật 10 ô.
  - Tầng tán cây là 3 cành ngang dài 14 ô ở y 38–39.
- **Địch:**
  - 1 Drone ong ở đầu tầng tán.
  - 1 Sniper đứng trên cành thứ hai.
  - 1 Brute đứng giữa bãi gai dưới đất (miễn gai).
- **Vật phẩm:** Reploid #1 trên cành cuối.
- **Ghi chú:** đi dưới đất bằng giáp Shadow (miễn gai) là đường tắt.'''),

 Room('R3', 'Đầm bùn', 124, 40, 52, 16, 4, [
   F((0, 10), (8, 10), (8, 12), (44, 12), (44, 10), (52, 10)), H('mud', 8, 10, 36, 2), P(16, 9, 4, 'move'), P(30, 9, 4, 'move'),
   X(10, 14, 'bùn: tốc độ ×0.5, nhảy thấp'), X(15, 7, 'khúc gỗ trôi'),
   E('D', 26, 4), E('S', 48, 9), PATH((1, 9), (8, 9), (17, 8), (31, 8), (44, 9), (51, 9))], '''
- **Mục đích:** đổi nhịp chậm lại. Bùn làm người chơi chậm hẳn, buộc phải dùng vật nổi.
- **Địa hình:**
  - Đầm dài 36 ô (x 132–168). Mặt bùn ở y 50.
  - Đứng trong bùn: tốc độ chạy ×0.5, độ cao nhảy ×0.6, không lướt được.
  - **2 khúc gỗ trôi** qua lại trên mặt bùn (60px/giây). Đứng trên gỗ thì di chuyển bình thường.
- **Địch:**
  - 1 Drone ong bay thấp, lao vào khi người chơi kẹt trong bùn.
  - 1 Sniper ở bờ bên kia.
- **Giáp hỗ trợ:** Falcon lướt trên không qua hết đầm.'''),

 Room('MID', 'Dây leo khổng lồ', 176, 36, 30, 16, 5, [
   F((0, 14), (30, 14)), B(0, 0, 2, 14), B(28, 0, 2, 14), B(0, 0, 30, 1), H('thorn', 2, 1, 26, 1), E('M', 15, 5),
   X(4, 10, 'hoa lõi mở 2s'), PATH((3, 13), (27, 13))], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được. Trần phủ gai.
- **Dây leo khổng lồ** có bông hoa lõi treo từ trần, 4 dây roi mọc từ sàn.
- **Đòn đánh:**
  - Dây roi trồi lên từ sàn ở chỗ người chơi đứng (đất nứt báo trước 0.6 giây).
  - Hoa phun 5 hạt độc hình quạt.
  - Hai dây roi quét ngang từ hai vách: phải nhảy qua đúng lúc.
- **Điểm yếu:** hoa lõi mở cánh 2 giây sau mỗi đợt phun hạt.
- **Phần thưởng:** mở lối xuống khu rễ cây. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Rễ cây', 206, 40, 26, 40, 5, [
   B(0, 0, 26, 2), B(0, 12, 2, 28), B(2, 12, 8, 1), B(24, 2, 2, 30), B(0, 38, 26, 2),
   P(14, 18, 8), P(4, 24, 8), P(14, 30, 8), H('thorn', 22, 12, 2, 6), H('thorn', 2, 26, 2, 6), H('thorn', 8, 37, 4, 1),
   E('C', 4, 11), E('R', 18, 17), E('D', 12, 28), E('T', 4, 37),
   PATH((3, 11), (12, 12), (16, 17), (10, 20), (8, 23), (18, 26), (18, 29), (24, 34), (25.5, 35)),
   ALT((8, 23), (4, 36))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đi xuống qua mạng rễ cây, đổi không gian sang dưới lòng đất.
- **Địa hình:**
  - Hố rễ rộng 22 ô, sâu 26 ô (từ y 52 xuống y 78).
  - 3 rễ ngang làm bậc, xếp zigzag.
  - Hai vách có mảng gai độc ở chỗ người chơi hay đá tường.
- **Địch:** 1 Drone ong dưới đáy hố.
- **Vật phẩm:** Reploid #2 trên rễ đầu tiên.
- **Lối phụ (Sub-Tank):**
  - Ở góc trái đáy hố, sau một bụi gai thấp.
  - Thả người thẳng từ rễ thứ hai xuống thì rơi trúng gai. Phải nhảy ra khỏi rễ, bám vách trái **phía dưới** mảng gai rồi trượt xuống.'''),

 Room('R5', 'Thân cây cổ thụ', 232, 14, 30, 66, 7, [
   B(0, 0, 4, 34), B(0, 38, 4, 26), B(0, 64, 30, 2), B(28, 8, 2, 56), B(4, 0, 26, 1),
   P(18, 56, 8), P(4, 48, 8), P(18, 40, 8), P(4, 32, 8), P(18, 24, 8), P(4, 16, 8), P(12, 9, 5, 'move'), P(5, 4, 5),
   H('thorn', 26, 44, 2, 6), H('thorn', 4, 26, 2, 6), H('thorn', 12, 40, 6, 1), H('thorn', 12, 24, 6, 1),
   X(13, 41.5, 'gai thò/thụt 2s'), E('H', 2, 36), E('A', 7, 3), E('D', 14, 50), E('D', 16, 20),
   PATH((1, 62), (12, 62), (22, 55), (8, 47), (22, 39), (8, 31), (22, 23), (8, 15), (14, 8), (22, 5), (29.5, 5)),
   ALT((8, 31), (5, 36), (2, 36)), ALT((14, 8), (8, 3))], '''
- **Mục đích:** cao trào của màn. Leo thân cây cao 60 ô (gấp hơn 3 lần chiều cao màn hình).
- **Địa hình:**
  - Lòng thân cây rộng 24 ô, từ đáy y 78 lên đỉnh y 15.
  - 6 cành ngang xếp zigzag cách nhau 8 ô.
  - Hai vách là vỏ cây, đá tường được, trừ các mảng gai.
- **Bẫy – gai thò thụt:**
  - Đầu trong của cành thứ ba và thứ năm có gai thò ra 2 giây rồi thụt vào 2 giây.
  - Mảng gai cố định trên vách ở đúng chỗ đá tường thuận tay nhất: buộc người chơi đổi bên.
- **Địch:** 2 Drone ong bay vòng trong lòng cây.
- **Lối phụ (Heart Tank):**
  - **Hốc trong vỏ cây** ở vách trái (x ≈ 232–236, y ≈ 52).
  - Nằm ngay dưới mảng gai trên vách: phải đá tường từ dưới lên rồi lướt ngang vào hốc, không được chạm gai.
- **Lối phụ (Capsule Gaea Foot):**
  - Trên đỉnh có **bệ lá di động** chạy ngang. Đứng trên bệ lá, nhảy sang kệ nhỏ sát vỏ cây bên trái (x ≈ 237, y ≈ 18).
  - Giáp Falcon bay thẳng lên được.'''),

 Room('R6', 'Tán cây', 262, 10, 66, 14, 6, [
   F((0, 12), (10, 12), None, (16, 11), (28, 11), None, (34, 12), (48, 12), None, (54, 11), (66, 11)),
   P(10, 12, 6, 'break'), P(48, 12, 6, 'break'), P(28, 11, 6, 'break'), H('void', 10, 13, 6, 1), H('void', 28, 12, 6, 2), H('void', 48, 13, 6, 1),
   X(10, 9.5, 'lá rụng 0.5s'), E('C', 2, 11), E('D', 22, 5), E('R', 40, 11), E('D', 58, 5), E('S', 62, 10),
   PATH((1, 11), (65, 10))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** tốc độ trên cao. Không được dừng trên lá.
- **Địa hình:**
  - Lối đi trên các cành lớn ở y 21–22, dài 66 ô. Dưới là khoảng không xuống tận đất rừng (rơi là mất mạng).
  - **3 đoạn lá rụng** nối các cành: đứng lên thì sau 0.5 giây lá rơi.
- **Địch:**
  - 2 Drone ong bay ngang tầm nhảy, ngay trên đoạn lá.
  - 1 Sniper ở cuối.
- **Vật phẩm:** Reploid #3 trên cành giữa.'''),

 Room('R7', 'Vườn hoa', 328, 10, 30, 14, 2, [
   F((0, 11), (30, 11)), BAR(29, 2, 1, 9, 'door'), E('R', 14, 10), X(4, 5, 'năng lượng nhỏ'), PATH((1, 10), (28, 10))], '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss. Vườn hoa máy yên tĩnh.'''),

 Room('BOSS', 'Spike Rosered', 358, 6, 32, 18, 6, [
   B(0, 0, 2, 15), B(30, 0, 2, 15), B(0, 0, 32, 1), F((0, 15), (32, 15)), H('thorn', 2, 1, 1, 10), H('thorn', 29, 1, 1, 10),
   E('*', 20, 8), X(5, 4, 'pha 2: dây gai bò trên sàn'), PATH((3, 14), (29, 14))], '''
- **Đấu trường 28 ô**. Hai vách phủ dây gai ở nửa trên: đá tường được ở nửa dưới thôi.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (bóng gai, bám trần, roi dây leo).
- **Pha 2** (dưới 50% HP):
  - Dây gai bò dọc sàn từ một vách sang vách kia, che 1/3 sàn, đổi bên mỗi 8 giây.
  - Rosered bám lên trần thường xuyên hơn.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Rừng đột biến', en='Mutant Jungle', boss='Spike Rosered', act='Act I · X5', theme=THEME, capsule='Gaea Foot',
 subtitle='Area 1 (rừng nấm và đầm): R1 → R2 (nấm bật) → R3 (bùn) → Mini-boss  |  Area 2 (rễ và thân cây): R4 (đi xuống) → R5 (leo thân cây) → R6 (tán cây) → R7 → Boss',
 keep='Boss, capsule Gaea Foot, nấm bật nhảy và sub-boss Dây leo vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Khu rừng máy móc đột biến mọc trùm lên một căn cứ bỏ hoang. Mặt đất là của gai độc, nên người chơi luôn phải tìm đường ở tầng trên: nấm bật, khúc gỗ, cành cây. Cao trào là leo lòng một cây cổ thụ khổng lồ.',
 areas=['**Area 1 – Rừng nấm và đầm (ngoài trời):** xanh rêu, nắng lọt qua tán. Dạy gai độc, nấm bật, bùn làm chậm.',
        '**Area 2 – Rễ và thân cây:** nâu tối, nấm phát sáng. Đi xuống hố rễ, leo thân cây 60 ô, rồi chạy trên tán.'],
 flow='né gai → bật nấm lên tán → lội bùn trên khúc gỗ → mini-boss dây leo → xuống hố rễ → leo thân cây cổ thụ → chạy trên lá rụng → boss',
 time='khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, màn Spike Rosered:** rừng máy, nấm bật, capsule Gaea trên tán cây cổ thụ.',
       '**X6, màn Commander Yammark:** rừng có hai tầng đường đi.',
       '**X8, màn Bamboo Pandamonium:** leo dọc dài với vật cản mọc ra theo nhịp.',
       '**X4, màn Web Spider:** rừng rậm, đi theo cành cây trên cao.',
       '**X Corrupted:** đặt bí mật ngay dưới mảng nguy hiểm để thưởng cho người hiểu cách đá tường.'],
 engine=['Bụi gai độc: sát thương + nhiễm độc theo thời gian (giáp Shadow miễn).',
         'Nấm bật: bật cao cố định, giữ NHẢY thì cao hơn.',
         'Vùng bùn: giảm tốc độ, độ cao nhảy, khóa lướt.',
         'Khúc gỗ trôi (bệ di động trên mặt bùn).',
         'Gai thò thụt theo nhịp trên cành.',
         'Sàn lá rụng (sàn vỡ 0.5 giây).',
         'Mini-boss Dây leo khổng lồ: roi trồi từ sàn theo vị trí người chơi.'],
 art=['**Tileset "Rừng máy" (Area 1):** 47 ô viền đất rêu, rễ máy, bụi gai (2 khung), nấm bật (3 khung), mặt bùn (4 khung).',
      '**Tileset "Thân cây" (Area 2):** 47 ô viền vỏ cây, cành ngang, gai thò thụt (3 khung), lá rụng (3 khung).',
      '**Vật thể:** khúc gỗ, bệ lá, hoa lõi mini-boss.',
      '**Nền:** Area 1: tán rừng xa và nắng lọt (2 lớp parallax). Area 2: lòng cây và nấm phát sáng (2 lớp).'],
)
STAGE['rooms'] = rooms
