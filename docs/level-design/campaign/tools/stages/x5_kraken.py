from lib import *

THEME = dict(bg1=(40, 40, 34), bg2=(36, 36, 52), rock1=(118, 112, 96), rock2=(100, 104, 120))

rooms = [
 Room('R1', 'Ga Ride Chaser', 0, 40, 30, 14, 2, [
   F((0, 10), (30, 10)), E('V', 20, 9), E('S', 8, 9), X(14, 6, 'lên xe'), PATH((1, 9), (29, 9))], '''
- **Mục đích:** lên **Ride Chaser** (mô-tô bay). Ở phòng này xe đứng yên cho người chơi làm quen nút.
- **Địa hình:** sàn phẳng 30 ô, mặt đất ở y 50. Xe đậu ở x ≈ 20.
- **Địch:** 1 Sniper đứng chắn trước xe (hạ bằng chân trước khi lên xe).
- **Ghi chú điều khiển:**
  - Ride Chaser **không tự chạy**: người chơi tự tăng tốc, phanh và lùi.
  - Đây là khác biệt chính so với X5 gốc, học theo cách bản X8 16-bit demake làm lại các đoạn tự cuộn.
  - Tốc độ tối đa 320px/giây, nhảy dốc thì bay xa theo tốc độ.'''),

 Room('R2', 'Đường đua cao thế', 30, 38, 100, 16, 3, [
   F((0, 12), (20, 12), (27, 8), (30, 8), None, (38, 12), (58, 12), (65, 7), (68, 7), None, (78, 12), (100, 12)),
   H('void', 30, 12, 8, 4), H('void', 68, 12, 10, 4), P(12, 11.6, 4, 'thrust'), P(50, 11.6, 4, 'thrust'),
   BAR(44, 4, 1, 8, 'elec'), BAR(88, 4, 1, 8, 'elec'), X(40, 3, 'cột điện 1s/2s'), X(10, 9.5, 'boost'),
   E('O', 24, 5), E('O', 34, 3), E('O', 56, 9), E('O', 73, 1), E('D', 52, 4), E('S', 92, 11),
   PATH((1, 11), (20, 11), (28, 7), (34, 4), (39, 11), (58, 11), (66, 6), (73, 2), (79, 11), (99, 11))], '''
- **Mục đích:** cảm giác tốc độ. Dạy **dốc nhảy**, **tấm boost** và **cột điện theo nhịp**.
- **Địa hình:**
  - Đường đua 100 ô, mặt đường ở y 50.
  - 2 dốc nhảy dẫn tới 2 vực (rộng 8 và 10 ô). Phải đủ tốc độ mới bay qua.
  - Tấm **boost** trước mỗi dốc: chạy qua thì tốc độ vọt lên tối đa trong 1.5 giây.
- **Bẫy – cột điện:** 2 cột phóng điện chắn ngang đường, bật 1 giây, tắt 2 giây. Canh tốc độ để qua lúc tắt, hoặc phanh chờ.
- **Quả năng lượng:** 4 trong tổng số 8 quả nằm ở phòng này. 2 quả ở đỉnh quỹ đạo bay của dốc: chỉ lấy được khi bay qua đúng tốc độ tối đa.
- **Địch:**
  - 1 Drone bay thấp sau tấm boost thứ hai: xe húc vỡ được.
  - 1 Sniper cuối đường.'''),

 Room('R3', 'Cầu sập', 130, 38, 80, 18, 4, [
   F((0, 12), (10, 12)), P(10, 12, 20, 'break'), H('void', 10, 13, 20, 5), F((30, 12), (40, 12), (46, 8), (48, 8)),
   H('void', 48, 12, 10, 6), P(58, 11, 14, 'break'), H('void', 58, 12, 14, 6), F((72, 12), (80, 12)), BAR(78, 4, 1, 8, 'door'),
   X(12, 10, 'sập 0.6s sau khi xe qua'), X(60, 15, 'cầu sập 2'), E('O', 20, 9), E('O', 38, 9), E('O', 53, 3), E('O', 66, 8),
   E('D', 26, 4), E('D', 62, 4), E('R', 75, 11), E('T', 79.5, 11), X(70, 3, 'cửa mở khi đủ 8 quả'),
   PATH((1, 11), (29, 11), (40, 11), (47, 7), (53, 4), (59, 10), (77, 11)), ALT((77, 11), (79.5, 11))], '''
- **Mục đích:** đoạn tốc độ thử thách. Không được dừng.
- **Địa hình:**
  - 2 **cầu sập**: mỗi mảnh cầu rơi 0.6 giây sau khi xe chạy qua. Dừng giữa cầu là rơi theo.
  - 1 dốc nhảy giữa hai cầu, vực rộng 10 ô.
- **Địch:** 2 Drone bay ngang tầm nhảy. Bắn trước khi lên dốc hoặc lượn qua dưới.
- **Vật phẩm:** Reploid #1 trên bệ cuối, ngay trước cửa.
- **Lối phụ (Sub-Tank):**
  - **Cửa năng lượng** cuối phòng chỉ mở khi đã nhặt đủ **8 quả năng lượng** ở R2 và R3. Sau cửa là Sub-Tank.
  - Lỡ quả nào thì phải quay xe chạy lại (xe lùi được). Đó là lý do đường đua không tự cuộn.'''),

 Room('MID', 'Trạm ngắt điện', 210, 36, 30, 18, 5, [
   F((0, 14), (30, 14)), B(0, 0, 2, 14), B(28, 0, 2, 14), B(0, 0, 30, 1), E('M', 15, 6), H('elec', 2, 13.4, 26, 0.6),
   X(4, 10, '4 cánh tay điện quay'), PATH((3, 13), (27, 13))], '''
- **Đấu trường 26 ô**, kín. Ride Chaser dừng ở cửa: người chơi đánh bằng chân.
- **Lõi biến áp** treo giữa phòng, có 4 cánh tay phóng điện quay chậm quanh lõi (90° mỗi 2 giây).
- **Đòn đánh:**
  - Cánh tay quét theo vòng tròn: luồn qua khe giữa hai cánh.
  - Sàn nhiễm điện 1.5 giây sau mỗi vòng quay (có tia lửa báo trước): đá tường lên vách mà chờ.
- **Điểm yếu:** lõi mở nắp 2 giây sau khi sàn hết điện.
- **Phần thưởng:** ngắt điện khu sau để mở Area 2. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Sàn điện', 240, 40, 60, 14, 5, [
   F((0, 10), (60, 10)), H('elec', 8, 9.4, 6, 0.6), H('elec', 20, 9.4, 6, 0.6), H('elec', 32, 9.4, 6, 0.6), H('elec', 44, 9.4, 6, 0.6),
   BAR(26, 0, 1, 4, 'elec'), B(0, 0, 60, 2), X(8, 7, 'tấm điện 1.5s / 1.5s, lệch pha'),
   E('C', 2, 9), E('B', 30, 9), E('S', 54, 9), E('D', 40, 4), E('R', 17, 9),
   PATH((1, 9), (59, 9))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** né theo nhịp trên sàn. Đây cũng là lần đổi không gian: từ đường đua ngoài trời vào trong nhà máy.
- **Địa hình:**
  - Hành lang 60 ô, trần thấp (cao 8 ô).
  - **4 tấm sàn điện** dài 6 ô, bật 1.5 giây, tắt 1.5 giây, lệch pha nhau thành một làn sóng.
  - Giữa các tấm có ô sàn an toàn rộng 6 ô.
- **Địch:**
  - 1 Brute đứng trên ô an toàn giữa phòng: phải hạ nó mà không bước lên tấm điện.
  - 1 Sniper cuối phòng, 1 Drone bay trên tấm điện thứ tư.
- **Vật phẩm:** Reploid #2 giữa hai tấm điện đầu.'''),

 Room('R5', 'Tháp tụ điện', 300, 4, 30, 50, 7, [
   B(0, 0, 2, 36), B(0, 46, 30, 4), B(22, 10, 8, 14), B(22, 28, 8, 18), B(2, 0, 28, 1),
   P(10, 40, 4, 'thrust'), P(4, 32, 4, 'thrust'), P(14, 22, 4, 'thrust'), P(6, 14, 4, 'thrust'), P(2, 5, 5),
   H('elec', 2, 29, 20, 0.6), H('elec', 2, 12, 20, 0.6), X(3, 30, 'hồ quang 1s/2s'),
   E('A', 4, 4), E('H', 27, 26), E('D', 16, 34), E('D', 12, 9),
   PATH((1, 45), (11, 45), (12, 39), (6, 31), (16, 21), (8, 13), (14, 7), (29.5, 6)),
   ALT((16, 21), (22, 26), (27, 26)), ALT((8, 13), (5, 4))], '''
- **Mục đích:** cao trào của màn. Leo dọc bằng **bệ phản lực** và đá tường giữa các tia hồ quang.
- **Địa hình:**
  - Tháp rộng 20 ô, cao 46 ô (từ y 50 lên y 5).
  - Vách trái leo được suốt chiều cao. Vách phải có một hốc ở giữa.
- **Cơ chế – bệ phản lực:**
  - 4 bệ, đứng lên thì bệ bốc lên với tốc độ 80px/giây trong 3 giây, rồi tắt máy và rơi về chỗ cũ.
  - Phải nhảy sang bệ tiếp theo trước khi bệ dưới chân tắt máy.
- **Bẫy – hồ quang:** 2 tia điện nối hai vách, bật 1 giây, tắt 2 giây. Bệ phản lực bay xuyên qua tia, nên phải canh lúc đứng lên bệ.
- **Địch:** 2 Drone, chỉ để gây áp lực.
- **Lối phụ (Heart Tank):** **hốc ở vách phải** (x ≈ 324–330, y ≈ 28–32). Nhảy từ bệ phản lực thứ ba khi nó lên ngang hốc, lướt trên không vào.
- **Lối phụ (Capsule Falcon Arm):**
  - Kệ nhỏ sát trần bên trái (x ≈ 302, y ≈ 9), cao hơn lối ra.
  - Nhảy từ bệ phản lực thứ tư ở điểm cao nhất, đá vách trái 2 lần mới tới.
  - Giáp Gaea bám tường nên dễ; giáp thường phải canh rất chuẩn.'''),

 Room('R6', 'Hành lang cáp', 330, 4, 60, 14, 6, [
   B(0, 0, 60, 2), F((0, 10), (60, 10)), P(10, 4, 6), P(32, 4, 6), BAR(20, 2, 1, 8, 'elec'), BAR(42, 2, 1, 8, 'elec'),
   E('K', 14, 3), E('K', 36, 3), E('C', 2, 9), E('R', 28, 9), E('S', 52, 9), E('D', 48, 5),
   X(21, 6, 'tường điện'), PATH((1, 9), (11, 6), (14, 4), (19, 9), (33, 4), (41, 9), (59, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: bắn công tắc trên cao, né địch, đi qua tường điện.
- **Địa hình:**
  - Hành lang 60 ô, trần ở y 6, sàn ở y 14.
  - **2 tường điện** chắn ngang hết chiều cao. Mỗi tường có một **công tắc** trên kệ cao phía trước nó.
- **Cơ chế:** bắn công tắc thì tường điện tắt trong **4 giây** rồi bật lại. Phải lên kệ, bắn, nhảy xuống và chạy qua kịp.
- **Địch:**
  - 1 Sniper sau tường thứ hai, bắn xuyên qua tường điện.
  - 1 Drone giữa hai tường.
- **Vật phẩm:** Reploid #3 giữa hai tường điện.'''),

 Room('R7', 'Cổng', 390, 4, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('R', 14, 9), X(4, 5, 'năng lượng nhỏ'), PATH((1, 9), (28, 9))], '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Volt Kraken', 420, 0, 32, 18, 6, [
   B(0, 0, 2, 16), B(30, 0, 2, 16), B(0, 0, 32, 1), F((0, 16), (32, 16)), H('water', 2, 13, 28, 3), E('*', 20, 6),
   X(4, 3, 'pha 2: nước nhiễm điện'), PATH((3, 12), (29, 12))], '''
- **Đấu trường 28 ô**, sàn ngập nước nông 3 ô. Hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (đạn điện, lao xúc tu, thả mực).
- **Pha 2** (dưới 50% HP):
  - Kraken phóng điện xuống nước mỗi 6 giây: **toàn bộ mặt nước nhiễm điện 1.5 giây** (nước chớp vàng 1 giây trước).
  - Lúc đó phải ở trên không: nhảy, đá tường, hoặc đứng trên vách.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Nhà máy điện', en='Energy Plant', boss='Volt Kraken', act='Act I · X5', theme=THEME, capsule='Falcon Arm',
 subtitle='Area 1 (đường đua ngoài trời): R1 → R2 → R3 (Ride Chaser, 8 quả năng lượng) → Mini-boss  |  Area 2 (nhà máy): R4 → R5 (leo tháp) → R6 → R7 → Boss',
 keep='Boss, capsule Falcon Arm, đoạn Ride Chaser và trạm ngắt điện (mid-gate) vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Nhà máy điện cao thế giữa đồng hoang. Nửa đầu là **đua Ride Chaser** qua dốc nhảy và cầu sập, nửa sau là **leo tháp tụ điện** bằng bệ phản lực. Cả màn chung một nhịp: điện bật/tắt theo chu kỳ.',
 areas=['**Area 1 – Đường đua cao thế (ngoài trời):** cột điện, trời giông, chớp xa. Tốc độ, dốc nhảy, nhặt quả năng lượng.',
        '**Area 2 – Nhà máy (trong nhà):** thép xám, đèn vàng, tia lửa. Sàn điện theo nhịp, tháp leo dọc, tường điện có công tắc.'],
 flow='lên xe → đua qua dốc và cột điện → cầu sập phía sau bánh xe → mini-boss biến áp → né sàn điện → leo tháp bằng bệ phản lực → bắn công tắc tường điện → boss nước nhiễm điện',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, màn Volt Kraken:** mở đầu bằng đoạn Ride Chaser có 8 quả năng lượng mở cửa ở cuối.',
       '**X8 16-bit demake:** làm lại các đoạn tự cuộn thành màn chơi thường; ở đây Ride Chaser chạy tự do, lùi lại được.',
       '**X4, màn Jet Stingray / X2, màn Overdrive Ostrich:** đường đua có dốc nhảy và vực.',
       '**X6, màn Commander Yammark / X8, màn Gigabolt Man-O-War:** bệ và sàn bật/tắt theo nhịp, đọc nhịp từ xa.',
       '**X Corrupted:** lối phụ đặt trên đường bay của cơ chế chính (Heart Tank chỉ với tới từ bệ phản lực).'],
 engine=['Ride Chaser chạy tự do: tăng tốc, phanh, lùi, nhảy theo dốc. Không tự cuộn.',
         'Tấm boost, dốc nhảy, cầu sập sau khi xe qua.',
         'Cửa đếm vật phẩm (mở khi nhặt đủ 8 quả năng lượng).',
         'Sàn điện và cột điện theo nhịp, lệch pha.',
         'Bệ phản lực: bốc lên khi đứng, tắt sau 3 giây, rơi về chỗ cũ.',
         'Tường điện bật/tắt bằng công tắc có hẹn giờ.',
         'Mini-boss Lõi biến áp có cánh tay quay.'],
 art=['**Tileset "Đường đua" (Area 1):** 47 ô viền đất đá, mặt đường nhựa, dốc nhảy, mảnh cầu sập (3 khung).',
      '**Tileset "Nhà máy" (Area 2):** 47 ô viền thép, tấm sàn điện (2 trạng thái), vách tháp tụ điện.',
      '**Vật thể:** quả năng lượng (4 khung), cột điện, tia hồ quang (4 khung), bệ phản lực (lửa 3 khung), tường điện, công tắc.',
      '**Nền:** Area 1: đồng hoang và cột cao thế dưới trời giông (2 lớp parallax). Area 2: tua-bin và cuộn dây khổng lồ (2 lớp).'],
)
STAGE['rooms'] = rooms
