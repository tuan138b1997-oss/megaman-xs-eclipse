from kit import *

THEME = dict(bg1=(52, 26, 44), bg2=(44, 20, 40), rock1=(130, 90, 120), rock2=(120, 80, 116))
s5, p5 = shaft_up(26, 46, n=5)
for i, g in enumerate(s5):
    if g[0] == 'plat': s5[i] = ('plat', 'move') + g[2:]

rooms = [
 Room('R1', 'Nền vỡ vụn', 0, 40, 50, 16, 4, [
   F((0, 12), (8, 12)), P(8, 12, 10, 'break'), F((18, 12), (24, 12)), P(24, 12, 12, 'break'), F((36, 12), (50, 12)),
   H('void', 8, 13, 10, 3), H('void', 24, 13, 12, 3), X(9, 9.6, 'sụp 0.4s'), E('D', 20, 5), E('S', 46, 11),
   PATH((1, 11), (49, 11))], '''
- **Mục đích:** bước vào lõi virus Sigma: **nền không gian vỡ vụn** dưới chân.
- **Địa hình:** 50 ô, mặt nền ở y 52. 2 đoạn nền vỡ (10 và 12 ô) sụp 0.4 giây sau khi đứng, rơi xuống vực.
- **Địch:** 1 Drone, 1 Sniper.
- **Ghi chú:** màn cuối Act I, ôn lại mọi cơ chế của Act I. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); hoàn thành màn mở khóa Act II.'''),

 Room('R2', 'Bệ lõi virus', 50, 36, 64, 22, 5, [
   F((0, 16), (6, 16)), F((58, 16), (64, 16)), H('void', 6, 20, 52, 2), P(10, 14, 5, 'move'), P(22, 10, 5, 'move'), P(34, 13, 5, 'move'), P(46, 9, 5, 'move'),
   Z('wind', 6, 0, 52, 20, 'gió giật (như Không quân)'), E('R', 36, 12), E('D', 28, 4), E('D', 52, 4),
   PATH((1, 15), (6, 15), (12, 13), (24, 9), (36, 12), (48, 8), (59, 15), (63, 15))], '''
- **Mục đích:** ôn **bệ di động** và **gió giật** của màn Không quân.
- **Địa hình:** vực 52 ô, 4 bệ lõi virus bay qua lại.
- **Cơ chế:** gió giật 2 giây mỗi 5 giây, đẩy ngược. Bệ bay theo đường chéo, không phải ngang.
- **Địch:** 2 Drone.
- **Vật phẩm:** Reploid #1 trên bệ thứ ba.'''),

 Room('R3', 'Hành lang ký ức', 114, 40, 70, 14, 6, [
   B(0, 0, 70, 2), F((0, 10), (70, 10)), Z('water', 4, 2, 16, 8, 'nước (Căn cứ đáy biển)'), BAR(26, 2, 0.8, 8, 'laser'),
   Z('slow', 32, 2, 14, 8, 'Time Zone'), H('trash', 36, 2, 2, 6), H('trash', 42, 4, 2, 6), H('elec', 52, 9.4, 8, 0.6),
   X(24, 0.6, 'laser 2s/1s'), X(52, 7.5, 'sàn điện'), E('B', 30, 9), E('S', 66, 9), E('R', 48, 9), PATH((1, 9), (69, 9))], '''
- **Mục đích:** hành lang **ký ức** ghép các đoạn ngắn của Act I.
- **Địa hình và cơ chế (theo thứ tự):**
  - Vùng nước (trọng lực ×0.32, như Căn cứ đáy biển).
  - Hàng rào laser 2 giây bật / 1 giây tắt (như Phòng thí nghiệm Laser).
  - Vùng Time Zone có búa lắc (như Đài thiên văn).
  - Sàn điện 1.5 giây / 1.5 giây (như Nhà máy điện).
- **Địch:** 1 Brute, 1 Sniper.
- **Vật phẩm:** Reploid #2 sau vùng Time Zone.'''),

 Room('MID', 'Phân thân Sigma', 184, 36, 30, 16, 6, arena(30, 16, 14) + [E('M', 15, 6), X(4, 10, '3 bóng ma lần lượt')], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Phân thân Sigma** là 3 bóng ma của Sigma xuất hiện lần lượt, mỗi bóng dùng một đòn.
- **Đòn đánh:**
  - Bóng 1: chém kiếm ngang sân.
  - Bóng 2: bắn tia từ trán.
  - Bóng 3: nhảy dội sàn tạo sóng xung kích.
- **Điểm yếu:** mỗi bóng chỉ nhận đòn khi đang ra đòn. Hạ đủ 3 bóng thì xong.
- **Phần thưởng:** mở vùng đảo trọng lực. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Vùng đảo trọng lực', 214, 36, 64, 22, 6, [
   F((0, 14), (8, 14)), F((56, 14), (64, 14)), H('void', 8, 20, 48, 2), B(8, 2, 48, 2), H('spike', 22, 4, 6, 1),
   Z('grav', 8, 4, 18, 16, 'đảo'), Z('grav', 38, 4, 18, 16, 'đảo'), B(26, 12, 12, 1), P(30, 11.6, 4, 'thrust'),
   E('C', 2, 13), E('R', 32, 11), E('D', 46, 10), E('S', 60, 13),
   PATH((1, 13), (8, 13), (10, 4.6), (21, 4.6), (24, 6), (27, 11), (37, 11), (40, 4.6), (54, 4.6), (57, 13), (63, 13))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** ôn **đảo trọng lực** của Zero Space 3, kết hợp tấm Boost.
- **Địa hình:** vực 48 ô. Trần liền phía trên, một cầu nhỏ giữa vực.
- **Cơ chế:**
  - Hai vùng đảo trọng lực cố định (không cần công tắc): vào vùng là rơi lên trần.
  - Giữa hai vùng là cầu nhỏ có tấm Boost: phải ra khỏi vùng đúng chỗ để rơi xuống cầu, rồi lướt Boost vào vùng sau.
  - Trần có một mảng gai.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #3 trên cầu giữa.'''),

 Room('R5', 'Trục lõi virus', 278, 10, 26, 46, 8, s5 + [
   Z('alarm', 9, 16, 8, 8, 'lõi bắn tia xoay'), BAR(12, 19, 2, 2, 'laser'), X(3, 40, 'bệ chạy vòng quanh lõi'), E('D', 6, 10), E('D', 20, 30), p5], '''
- **Mục đích:** cao trào của màn. Leo trục dọc trên các bệ chạy vòng quanh **lõi virus** đang bắn.
- **Địa hình:** trục rộng 22 ô, cao 42 ô (từ y 54 lên y 13). 5 bệ di động.
- **Cơ chế:**
  - Các bệ chạy vòng tròn quanh lõi virus ở giữa trục (bán kính 7 ô, mỗi vòng 8 giây).
  - **Lõi bắn tia quay** 1 vòng mỗi 4 giây. Tia dài tới vách, chỉ né được bằng cách nhảy qua đúng lúc.
  - Hai vách đá tường được, nhưng vách có vệt dữ liệu nhiễu ở nửa trên (đẩy ra 1 ô).
- **Địch:** 2 Drone.
- **Giáp hỗ trợ:** Falcon bay; Ultimate lướt Nova Strike xuyên tia.'''),

 Room('R6', 'Cổng quyết chiến', 304, 7, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('C', 2, 9), E('R', 15, 9), X(4, 5, 'năng lượng LỚN'), PATH((1, 9), (28, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước trận cuối Act I: Reploid #4, **nạp năng lượng lớn**, cổng Sigma.'''),

 Room('BOSS', 'Final Sigma W', 334, 3, 34, 18, 8, [
   F((0, 14), (34, 14)), P(2, 14, 6, 'break'), P(14, 14, 6, 'break'), P(26, 14, 6, 'break'), H('void', 0, 16, 34, 2),
   E('*', 17, 5), X(3, 2, 'pha 2: sàn sụp từng mảng'), PATH((1, 13), (33, 13))], '''
- **Đấu trường 34 ô**, không vách.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Final Sigma W khổng lồ, tay, mắt, tia).
- **Pha 2** (dưới 50% HP):
  - **Sàn sụp từng mảng**: 3 mảng (rộng 6 ô) lần lượt sụp 4 giây rồi dựng lại. Mảng sắp sụp nứt đỏ 1 giây trước.
  - Sigma nhắm đòn vào mảng sàn an toàn còn lại.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Zero Space Final', en='Zero Space Final', boss='Final Sigma W', act='Pháo đài X5', theme=THEME, capsule='',
 subtitle='Area 1: R1 (nền vỡ) → R2 (bệ lõi, gió) → R3 (ký ức Act I) → Mini-boss phân thân  |  Area 2: R4 (đảo trọng lực) → R5 (trục lõi virus) → R6 cổng → Boss',
 keep='Boss Final Sigma W, nền không gian vỡ vụn, bệ di chuyển lõi virus, vùng đảo trọng lực và cổng quyết chiến vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.',
 concept='Màn cuối Act I, **ôn tập mọi cơ chế** người chơi đã học: nền vỡ, bệ di động, gió, nước, laser, Time Zone, sàn điện, đảo trọng lực. Mỗi cơ chế xuất hiện ngắn, ghép nhau dày hơn.',
 areas=['**Area 1 – Rìa lõi virus:** hồng tím, mảnh vỡ trôi. Nền vỡ, bệ lõi trong gió, hành lang ký ức.',
        '**Area 2 – Lõi Sigma:** đỏ đậm, tia sáng. Đảo trọng lực có Boost, trục leo quanh lõi bắn tia.'],
 flow='chạy trên nền vỡ → bay bệ lõi trong gió → hành lang ký ức Act I → 3 bóng ma Sigma → đảo trọng lực qua vực → leo quanh lõi virus → boss sàn sụp',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, Zero Space Final:** hợp nhất cơ chế Act I, trọng lực biến thiên, bệ di chuyển, cổng quyết chiến Sigma.',
       '**X6, màn Gate Lab cuối:** ôn lại các màn trước bằng đoạn ngắn.',
       '**X8, màn Jakob Elevator / Sigma Palace:** leo quanh trục trung tâm.',
       '**X Corrupted:** pháo đài cuối ghép cơ chế của nhiều màn.'],
 engine=['Dùng lại toàn bộ đối tượng của Act I (nền vỡ, bệ di động, gió, nước, laser, Time Zone, sàn điện, đảo trọng lực).',
         'Bệ chạy vòng quanh một tâm trong trục dọc; lõi bắn tia quay.',
         'Mini-boss Phân thân Sigma (3 bóng lần lượt).',
         'Sàn boss sụp từng mảng theo lịch.'],
 art=['**Tileset "Lõi virus":** 47 ô viền hồng tím có mạch, nền vỡ (3 khung).',
      '**Vật thể:** bệ lõi virus, lõi bắn tia (4 khung), bóng ma Sigma, mảng sàn sụp.',
      '**Nền:** khối mảnh vỡ trôi và hình bóng Sigma mờ (2 lớp parallax).'],
)
for r in rooms:
    r['y'] += 4
STAGE['rooms'] = rooms
