from kit import *

THEME = dict(bg1=(44, 58, 76), bg2=(36, 48, 66), rock1=(176, 190, 208), rock2=(140, 156, 180))
s5, p5 = shaft_up(24, 52, n=5)

rooms = [
 Room('R1', 'Trạm cực', 0, 30, 40, 16, 2, [
   F((0, 12), (40, 12)), H('snow', 0, 11.6, 40, 0.4), E('V', 30, 11), E('S', 14, 11), X(26, 7, 'Ride Chaser'), PATH((1, 11), (39, 11))], '''
- **Mục đích:** lên **Ride Chaser** ở trạm nghiên cứu Bắc Cực.
- **Địa hình:** sân trạm 40 ô, mặt tuyết ở y 42.
- **Địch:** 1 Sniper chắn trước xe.
- **Ghi chú:** khác đường đua Nhà máy điện (đi ngang, chạy tự do), ở đây là **đổ dốc xuống**, có tuyết lở đuổi phía sau nên không được dừng lâu.'''),

 Room('R2', 'Dốc tuyết lở', 40, 30, 100, 30, 3, [
   SP('chaser', x=0, y=0, w=4, h=30, x1=100, trigger=3, speed0=240, speed1=240, look='snow'),
   F((0, 12), (26, 17), (28, 16)), H('void', 28, 18, 8, 12), F((36, 19), (70, 25), (72, 24)), H('void', 72, 26, 8, 4), F((80, 26), (100, 26)),
   AR(5, 6, 6, 2, 'alarm'), X(1, 2, 'tuyết lở đuổi'),
   H('trash', 48, 18, 2, 2), H('trash', 60, 21, 2, 2), X(46, 15, 'tảng băng lăn'),
   E('D', 32, 8), E('D', 76, 16), E('O', 30, 10), E('O', 74, 19),
   PATH((1, 11), (26, 16), (32, 11), (37, 18), (70, 24), (76, 19), (81, 25), (99, 25))], '''
- **Mục đích:** lao xuống dốc dài 100 ô trên Ride Chaser, **tuyết lở đuổi phía sau**.
- **Địa hình:**
  - Dốc đi xuống từ y 42 tới y 56, có 2 vực (rộng 8 ô) ở cuối hai đoạn dốc, nhảy qua bằng đà.
- **Cơ chế:**
  - **Tuyết lở** là một bức tường tuyết đuổi theo với tốc độ 240px/giây. Chậm hơn nó là bị vùi (mất mạng). Xe chạy tối đa 320px/giây, nên vẫn có khoảng dư để phanh một chút.
  - **Tảng băng lăn** từ trên dốc xuống chậm hơn xe: nhảy qua, hoặc bắn 2 phát cho vỡ.
- **Địch:** 2 Drone bay ngang tầm nhảy qua vực. Xe húc vỡ được.
- **Quả năng lượng:** 2 quả nằm trên đường bay qua vực, chỉ để thưởng (hồi năng lượng vũ khí).'''),

 Room('R3', 'Hồ băng mỏng', 140, 44, 60, 16, 4, [
   F((0, 12), (8, 12)), P(8, 12, 44, 'break'), H('water', 8, 13, 44, 3), F((52, 12), (60, 12)),
   X(10, 9.5, 'băng nứt sau 0.4s nếu xe đi chậm'), Z('alarm', 0, 0, 4, 12, ''), E('D', 24, 5), E('S', 56, 11), E('R', 54, 11),
   PATH((1, 11), (59, 11))], '''
- **Mục đích:** giữ tốc độ trên **mặt băng mỏng**.
- **Địa hình:** hồ băng rộng 44 ô, mặt băng ở y 56. Dưới là nước lạnh (rơi xuống là mất mạng).
- **Cơ chế:**
  - Đi nhanh (trên 200px/giây) thì băng chỉ nứt sau lưng xe.
  - Đi chậm thì băng vỡ 0.4 giây sau khi xe chạm.
  - Tuyết lở vẫn đuổi tới đầu hồ rồi dừng.
- **Địch:** 1 Drone giữa hồ, 1 Sniper ở bờ bên kia.
- **Vật phẩm:** Reploid #1 ở bờ bên kia, cạnh chỗ xuống xe (xe không qua được cửa phòng sau).'''),

 Room('MID', 'Gấu tuyết máy', 200, 42, 30, 16, 5, arena(30, 16, 14) + [H('ice', 2, 13.6, 26, 0.4), E('M', 15, 9), X(4, 4, 'sàn băng trơn')], '''
- **Đấu trường 26 ô**, sàn băng trơn, hai vách đá tường được.
- **Gấu tuyết máy** to bằng 3 ô, chạy và trượt trên băng.
- **Đòn đánh:**
  - Lao trượt ngang sân rồi đâm vào vách, làm rơi 3 cột băng nhọn từ trần.
  - Ném tảng tuyết lăn trên sàn.
  - Thổi hơi lạnh: trúng thì đóng băng 1 giây (bấm liên tục để thoát).
- **Điểm yếu:** lưng, sau mỗi lần đâm vách nó choáng 1.5 giây.
- **Phần thưởng:** mở cửa hang băng. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Hang băng trơn', 230, 44, 60, 14, 5, [
   B(0, 0, 60, 2), F((0, 12), (60, 12)), H('ice', 0, 11.6, 60, 0.4), H('ice', 14, 2, 1, 2), H('ice', 28, 2, 1, 2), H('ice', 40, 2, 1, 2),
   X(12, 4.5, 'cột băng rơi khi lại gần'), P(44, 5, 6), E('C', 2, 11), E('B', 22, 11), E('S', 54, 11), E('R', 34, 11), E('T', 47, 4),
   PATH((1, 11), (59, 11)), ALT((40, 11), (44, 6), (47, 4))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đi bộ trên sàn băng có quán tính, trong hang có cột băng rơi.
- **Địa hình:** hang 60 ô, sàn băng ở y 56, trần ở y 46.
- **Bẫy – cột băng:** 3 cột băng treo trần, rung khi người chơi lại gần trong 3 ô rồi rơi sau 0.5 giây. Trên sàn trơn khó dừng đúng chỗ.
- **Địch:** 1 Brute trượt trên băng (không dừng kịp nên đâm cả vào cột băng rơi), 1 Sniper.
- **Vật phẩm:** Reploid #2 giữa hang.
- **Lối phụ (Sub-Tank):** kệ băng trên cao (x ≈ 277, y ≈ 48), ngay dưới cột băng thứ ba. Phải làm cột băng rơi trước rồi mới lên.'''),

 Room('R5', 'Vách băng cao', 290, 6, 24, 52, 6, s5 + [
   H('ice', 2, 18, 2, 14), H('ice', 22, 30, 2, 14), Z('wind', 2, 12, 20, 14, 'bão tuyết thổi ngang 2s mỗi 6s'), AR(6, 20, 8, 0),
   P(2, 4, 5), B(2, 1, 1, 3), E('A', 4, 3), P(19, 34, 3), E('H', 20, 33), E('D', 12, 24), p5,
   ALT((5, 12), (3, 9), (4, 3)), ALT((17, 40), (20, 33))], '''
- **Mục đích:** đoạn dọc. Vách băng một phần **không bám được**, bão tuyết thổi ngang từng đợt.
- **Địa hình:**
  - Khe vách băng rộng 20 ô, cao 48 ô (từ y 56 lên y 9). 5 kệ băng zigzag.
  - Mảng băng láng trên vách (trái ở đoạn giữa, phải ở đoạn dưới): không đá tường được ở đó.
- **Cơ chế – bão tuyết:** gió thổi sang phải 100px/giây, 2 giây mỗi 6 giây, ở nửa trên. Đang đá tường vách trái mà gặp gió thì bị thổi bật ra.
- **Địch:** 1 Drone dạng chim cánh cụt bay.
- **Lối phụ (Capsule Blade Body):**
  - Kệ băng sát trần bên trái (x ≈ 292, y ≈ 10), cao hơn lối ra.
  - Bám vách trái ngay phía trên mảng băng láng, đá tường 2 lần lên kệ. Phải lên lúc không có gió.
- **Lối phụ (Heart Tank):** một gờ nhỏ ở vách phải (x ≈ 310, y ≈ 39), ngay trên mảng băng láng: nhảy chéo từ kệ thứ hai sang, không đá tường được.'''),

 Room('R6', 'Sông băng trôi', 314, 4, 70, 14, 7, [
   B(0, 0, 70, 2), H('spike', 0, 2, 70, 1), F((0, 10), (6, 10)), F((64, 10), (70, 10)), H('water', 6, 11, 58, 3),
   P(8, 9, 6, 'move'), P(20, 9, 6, 'move'), P(32, 9, 6, 'move'), P(44, 9, 6, 'move'), P(55, 9, 6, 'move'),
   AR(10, 12, 8, 0, 'current'), X(8, 4, 'trần gai cách mặt khối băng 3.5 ô'), E('D', 26, 5), E('D', 50, 5),
   PATH((1, 9), (6, 9), (11, 8), (23, 8), (35, 8), (47, 8), (58, 8), (69, 9))], '''
- **Mục đích:** cao trào của màn. Nhảy trên **khối băng trôi** dưới trần gai thấp.
- **Địa hình:**
  - Sông băng dài 58 ô dưới một hang có **trần phủ gai**, chỉ cách mặt khối băng 3.5 ô.
  - Rơi xuống nước là mất mạng.
- **Cơ chế:**
  - Khối băng trôi sang phải 50px/giây, mỗi khối rộng 6 ô.
  - Khối băng **trơn và nghiêng nhẹ** khi đứng ở mép, nên người chơi trượt ra mép.
  - Nhảy hết lực là chạm trần gai. Phải nhảy ngắn giữa các khối, nhất là khi khoảng cách giữa hai khối giãn ra.
- **Địch:** 2 Drone chim cánh cụt bay sát trần: bắn ngang, không cần nhảy.
- **Giáp hỗ trợ:** Shadow miễn gai (kể cả trần gai), nên đoạn này dễ hẳn.'''),

 Room('R7', 'Cổng sông băng', 384, 4, 50, 14, 6, [
   B(0, 0, 50, 2), F((0, 10), (50, 10)), H('ice', 0, 9.6, 50, 0.4), B(18, 7, 4, 3), B(32, 6, 4, 4),
   E('C', 2, 9), E('R', 26, 9), E('S', 46, 9), E('D', 40, 4), PATH((1, 9), (17, 9), (20, 6), (31, 9), (34, 5), (49, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: sàn băng trơn và bậc khối băng.
- **Địa hình:** hành lang 50 ô, sàn băng, 2 khối băng cao 3 và 4 ô.
- **Địch:** 1 Drone, 1 Sniper đứng sau khối băng thứ hai.
- **Vật phẩm:** Reploid #3 giữa hai khối băng.'''),

 rest('R8', 'Lều trạm', 434, 4, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Blizzard Wolfang', 464, 0, 32, 16, 6, arena(32, 16, 14, ceil=False) + [H('ice', 2, 13.6, 28, 0.4), Z('wind', 2, 0, 28, 13, 'pha 2: bão tuyết'), E('*', 20, 9)], '''
- **Đấu trường 28 ô**, sàn băng trơn, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Ice Burst, cào, nhảy vách).
- **Pha 2** (dưới 50% HP):
  - **Bão tuyết** thổi ngang, đổi chiều mỗi 6 giây.
  - Tầm nhìn giảm (tuyết bay), Wolfang lẩn vào bão rồi lao ra.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Bắc Cực', en='North Pole Area', boss='Blizzard Wolfang', act='Act II · X6', theme=THEME, capsule='Blade Body',
 subtitle='Area 1 (dốc và hồ, Ride Chaser): R1 → R2 (tuyết lở đuổi) → R3 (băng mỏng) → Mini-boss  |  Area 2 (hang và vách băng): R4 → R5 (leo vách) → R6 (khối băng dưới trần gai) → R7 → R8 → Boss',
 keep='Boss, capsule Blade Body, Ride Chaser trên dốc tuyết lở, sàn băng quán tính, vách băng cao và đoạn khối băng sát trần gai vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Trạm nghiên cứu Bắc Cực giữa bão tuyết. Nửa đầu là **lao dốc bằng Ride Chaser** trước tuyết lở, nửa sau là **đi bộ trên băng trơn** với vách không bám được và trần gai thấp.',
 areas=['**Area 1 – Dốc và hồ (ngoài trời):** trắng xanh, trời xám, tuyết bay. Ride Chaser đổ dốc, tuyết lở đuổi, hồ băng mỏng.',
        '**Area 2 – Hang và vách băng:** xanh băng, ánh lạnh. Sàn trơn, cột băng rơi, vách băng có bão, sông băng dưới trần gai.'],
 flow='lên xe → lao dốc trước tuyết lở → giữ tốc độ trên băng mỏng → mini-boss gấu tuyết → trượt trong hang có cột băng rơi → leo vách băng trong bão → nhảy khối băng dưới trần gai → boss trong bão tuyết',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X6, màn Blizzard Wolfang:** Ride Chaser trên dốc tuyết lở, vách băng cao giấu Blade Body, khối băng trôi sát trần gai.',
       '**X8 16-bit demake (màn Avalanche Yeti):** đoạn tự cuộn được làm lại thành đoạn chơi thường, lấy cảm hứng từ X2 Overdrive Ostrich.',
       '**X (SNES), màn Chill Penguin / X3, màn Blizzard Buffalo:** sàn băng quán tính, cột băng rơi.',
       '**X Corrupted:** giáp mở đường tắt rõ ràng (Shadow miễn trần gai).'],
 engine=['Ride Chaser đổ dốc; tường tuyết lở đuổi theo tốc độ cố định.',
         'Tảng băng lăn (vật thể lăn theo dốc, phá được).',
         'Mặt băng mỏng: vỡ theo tốc độ đi qua.',
         'Sàn băng quán tính; vách băng láng không đá tường được.',
         'Cột băng rơi khi người chơi lại gần.',
         'Bão tuyết: vùng gió theo nhịp, giảm tầm nhìn.',
         'Khối băng trôi trơn, nghiêng khi đứng ở mép.',
         'Mini-boss Gấu tuyết máy.'],
 art=['**Tileset "Dốc tuyết" (Area 1):** 47 ô viền tuyết, dốc tuyết, mặt băng mỏng (3 khung nứt).',
      '**Tileset "Hang băng" (Area 2):** 47 ô viền băng, mảng băng láng, trần gai băng.',
      '**Vật thể:** tuyết lở (4 khung), tảng băng lăn, cột băng (3 khung), khối băng trôi, bông tuyết bão (lớp phủ).',
      '**Nền:** Area 1: núi tuyết và cực quang (2 lớp parallax). Area 2: lòng sông băng xanh (2 lớp).'],
)
STAGE['rooms'] = rooms
