from kit import *

THEME = dict(bg1=(40, 24, 44), bg2=(30, 20, 40), rock1=(110, 80, 120), rock2=(96, 72, 118))
s2, p2 = shaft_up(24, 48, n=4)
s5, p5 = shaft_down(24, 44, n=4)

rooms = [
 Room('R1', 'Sảnh gai', 0, 40, 44, 16, 3, [
   F((0, 12), (44, 12)), H('spike', 10, 11, 6, 1), H('spike', 24, 11, 8, 1), B(18, 9, 3, 3),
   E('R', 4, 11), E('S', 40, 11), E('D', 28, 4), PATH((1, 11), (9, 11), (13, 7), (18, 8), (21, 8), (28, 6), (33, 11), (43, 11))], '''
- **Mục đích:** mở đầu pháo đài: **gai sàn dày đặc**, chạm gai là mất mạng (trừ giáp Shadow/Ultimate).
- **Địa hình:** sảnh 44 ô, mặt sàn ở y 60, 2 bãi gai (6 và 8 ô) cách nhau bởi một bệ đá.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #1 ở đầu sảnh.
- **Ghi chú:** pháo đài không có Heart Tank/Sub-Tank. Màn này giữ **capsule bí mật** Black Zero / Ultimate Armor X5 (theo dữ liệu game).'''),

 Room('R2', 'Tháp gai', 44, 6, 24, 48, 5, s2 + [
   H('spike', 2, 14, 1, 6), H('spike', 21, 26, 1, 6), H('spike', 2, 45, 20, 1), X(3, 21, 'mảng gai vách'), E('D', 12, 22), p2], '''
- **Mục đích:** leo dọc giữa **vách có mảng gai**.
- **Địa hình:** tháp rộng 20 ô, cao 44 ô (từ y 60 lên y 18). 4 kệ zigzag.
- **Bẫy:** mảng gai trên vách ở đúng chỗ đá tường thuận tay: phải đổi bên hoặc dùng kệ. Đáy tháp là rãnh gai.
- **Địch:** 1 Drone.'''),

 Room('R3', 'Hành lang mặt nạ', 68, 3, 56, 14, 5, [
   B(0, 0, 56, 2), F((0, 10), (56, 10)), E('W', 14, 3), E('W', 32, 3), E('W', 48, 3), H('laser', 14, 3.8, 0.4, 6), H('laser', 32, 3.8, 0.4, 6),
   H('spike', 20, 9, 6, 1), X(12, 1, 'mặt nạ trên tường: mắt bắn tia xuống 1s / 2s'), E('B', 40, 9), E('S', 52, 9), E('D', 26, 5), E('R', 36, 9),
   PATH((1, 9), (19, 9), (23, 6), (27, 9), (55, 9))], '''
- **Mục đích:** báo trước boss: **mặt nạ Rangda** gắn trên tường bắn tia từ mắt.
- **Địa hình:** hành lang 56 ô, trần ở y 13, sàn ở y 21, một bãi gai 6 ô.
- **Bẫy:** 3 mặt nạ, mắt bắn tia thẳng xuống sàn 1 giây mỗi 2 giây, lệch pha. Bắn vào mắt 3 phát thì mặt nạ tắt hẳn.
- **Địch:** 1 Drone, 1 Brute, 1 Sniper.
- **Vật phẩm:** Reploid #2 giữa mặt nạ 2 và 3.'''),

 Room('MID', 'Mặt nạ canh cổng', 124, -1, 30, 16, 6, arena(30, 16, 14) + [E('M', 15, 5), X(4, 10, 'mặt nạ trượt trên 4 vách')], '''
- **Đấu trường 26 ô**, kín.
- **Mặt nạ canh cổng** trượt vòng quanh 4 mặt đấu trường (sàn, vách, trần).
- **Đòn đánh:**
  - Bắn tia mắt thẳng góc với mặt nó đang bám.
  - Lao ngang qua sân khi đổi mặt.
- **Điểm yếu:** con mắt, chỉ mở khi mặt nạ dừng ở góc.
- **Phần thưởng:** mở đường vào biển gai. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Biển gai trọng lực ngược', 154, -5, 70, 26, 8, [
   F((0, 18), (8, 18)), F((62, 18), (70, 18)), H('spike', 8, 24, 54, 2), B(0, 4, 36, 2), B(44, 4, 26, 2),
   B(34, 0, 2, 4), B(44, 0, 2, 4), B(34, 0, 12, 1), Z('grav', 8, 6, 54, 17, 'vùng đảo trọng lực'),
   H('spike', 18, 6, 6, 1), B(50, 6, 3, 6), H('spike', 50, 11.4, 3, 0.6), X(48, 13, 'trụ tường'),
   E('K', 6, 17), E('C', 2, 17), E('D', 28, 14), E('D', 56, 10), E('A', 40, 2),
   X(9, 21, 'biển gai sàn dài 54 ô'),
   PATH((1, 17), (6, 17), (9, 7), (17, 7), (19, 9), (25, 7), (33, 7), (47, 7), (49, 14), (54, 14), (55, 7), (61, 9), (63, 17), (69, 17)),
   ALT((36, 7), (38, 5), (40, 2))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** cao trào của màn. **Đi lộn ngược trên trần** qua biển gai dài 54 ô (khoảng 1.700px).
- **Địa hình:** sàn là biển gai liền. Trần ở y 9 là đường đi duy nhất.
- **Cơ chế – đảo trọng lực:**
  - Bắn **công tắc** ở mép vực thì trọng lực trong vùng đảo ngược: người chơi "rơi" lên trần và đi trên trần.
  - Trần có một mảng gai 6 ô: nhảy (xuống dưới) qua nó.
  - **Trụ tường** treo từ trần chắn ngang (x ≈ 204–207). Phải bắn công tắc lần nữa (từ trên trần bắn được) để rơi xuống, lách dưới trụ, rồi đảo lại lên trần trước khi chạm biển gai. Có khoảng 0.8 giây.
  - Cuối vùng, trọng lực tự trở lại bình thường.
- **Địch:** 2 Drone, miễn đảo trọng lực.
- **Lối phụ (Capsule bí mật Black Zero / Ultimate Armor X5):**
  - Trên trần có một **hốc lõm lên** (x 188–198, y 3–9). Khi đang đi lộn ngược, hốc này là một cái "hố" trên đường đi.
  - "Rơi" vào hốc thì gặp capsule bí mật (x ≈ 194, y ≈ 5).
  - Điều kiện mở capsule giữ nguyên theo dữ liệu game.'''),

 Room('R5', 'Giếng đảo chiều', 224, 4, 24, 44, 6, s5 + [Z('grav', 2, 10, 20, 32, 'đảo chiều mỗi 4s'), E('R', 6, 24), E('D', 14, 20), E('S', 18, 34), p5], '''
- **Mục đích:** đoạn dọc đi xuống, nhưng **trọng lực tự đảo chiều mỗi 4 giây**.
- **Địa hình:** giếng rộng 20 ô, sâu 34 ô. 4 kệ zigzag.
- **Cơ chế:** khi trọng lực ngược, người chơi rơi lên. Phải đứng trên mặt **dưới** của kệ để chờ trọng lực đổi lại. Mặt dưới mỗi kệ được tô viền khác màu để dễ nhận ra.
- **Địch:** 1 Drone, 1 Sniper đứng trên kệ cuối (nó cũng bị đảo chiều).
- **Vật phẩm:** Reploid #3 trên kệ thứ hai.'''),

 Room('R6', 'Trạm nghỉ', 248, 36, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('C', 2, 9), E('R', 15, 9), X(4, 5, 'năng lượng LỚN'), PATH((1, 9), (28, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn**, cửa boss.'''),

 Room('BOSS', 'Rangda Bangda W', 278, 32, 32, 16, 7, arena(32, 16, 14) + [B(28, 1, 2, 13), E('*', 26, 6), Z('grav', 2, 1, 24, 13, 'pha 2: đảo trọng lực'),
   X(3, 3, 'vách mặt nạ bên phải')], '''
- **Đấu trường 28 ô**. Vách phải là **mặt nạ khổng lồ** (2 mắt, 1 mũi).
- **Pha 1** (100–50% HP): bộ chiêu hiện có (2 mắt bắn, mũi phun, tường khép lại).
- **Pha 2** (dưới 50% HP):
  - **Trọng lực đảo chiều mỗi 6 giây**: người chơi lúc đứng sàn, lúc đứng trần. Hai mắt đổi chỗ lên trên/xuống dưới theo.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Zero Space 3', en='Zero Space 3', boss='Rangda Bangda W', act='Pháo đài X5', theme=THEME, capsule='bí mật Black Zero / Ultimate Armor X5',
 subtitle='Area 1: R1 (gai) → R2 (tháp gai) → R3 (mặt nạ) → Mini-boss  |  Area 2: R4 (biển gai, đi trên trần, capsule bí mật) → R5 (giếng đảo chiều) → R6 trạm nghỉ → Boss',
 keep='Boss Rangda Bangda W, biển gai sàn, vùng đảo trọng lực, trụ tường và capsule bí mật Black Zero / Ultimate X5 vẫn giữ. Không có Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.',
 concept='Tầng thứ ba của không gian Zero. Sàn toàn gai, nên **trần trở thành sàn**: người chơi học đảo trọng lực để đi lộn ngược, và đó cũng là cách duy nhất để thấy hốc capsule bí mật.',
 areas=['**Area 1 – Tháp gai:** gai trên sàn và vách, mặt nạ Rangda trên tường.',
        '**Area 2 – Biển gai:** đi trên trần qua 54 ô gai, rồi giếng có trọng lực tự đảo chiều.'],
 flow='né gai sàn → leo tháp tránh mảng gai vách → tắt mắt mặt nạ → mini-boss mặt nạ → đảo trọng lực đi trên trần → lách dưới trụ tường → rơi vào hốc capsule bí mật → giếng đảo chiều → boss',
 time='khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen',
 refs=['**X5, Zero Space 3:** tháp né gai, vùng đảo trọng lực vượt biển gai 1.650px, trụ tường, capsule bí mật Black Zero / Ultimate.',
       '**X6, Gate Lab 3:** đảo trọng lực đi trên trần để lấy capsule bí mật.',
       '**X8, màn Gravity Antonion:** đảo trọng lực theo nhịp.',
       '**X Corrupted:** bí mật chỉ "nhìn thấy" khi đang dùng cơ chế chính (hốc trên trần thành hố khi đi lộn ngược).'],
 engine=['Vùng đảo trọng lực: bật/tắt bằng công tắc (bắn được từ trên trần), hoặc tự đảo theo nhịp.',
         'Gai sàn/vách/trần: chạm là mất mạng (giáp Shadow/Ultimate miễn theo dữ liệu game).',
         'Mặt nạ trên tường bắn tia theo nhịp, phá được.',
         'Mini-boss Mặt nạ canh cổng trượt quanh 4 mặt đấu trường.',
         'Boss có vùng đảo trọng lực theo nhịp ở pha 2.'],
 art=['**Tileset "Tháp gai":** 47 ô viền tím đen, gai sàn/vách/trần, kệ có mặt dưới tô viền.',
      '**Vật thể:** mặt nạ Rangda trên tường (mắt 3 khung), công tắc trọng lực, hiệu ứng đảo chiều (lớp phủ màn hình).',
      '**Nền:** không gian virus tím đỏ và mặt nạ khổng lồ mờ xa (2 lớp parallax).'],
)
for r in rooms:
    r['y'] += 8
STAGE['rooms'] = rooms
