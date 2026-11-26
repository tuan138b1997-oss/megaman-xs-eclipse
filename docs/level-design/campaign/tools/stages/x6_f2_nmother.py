from kit import *

THEME = dict(bg1=(54, 30, 30), bg2=(50, 28, 26), rock1=(120, 90, 90), rock2=(110, 80, 76))
s5, p5 = shaft_up(26, 58, n=5)
for i, g in enumerate(s5):
    if g[0] == 'plat': s5[i] = ('plat', 'move') + g[2:]

rooms = [
 Room('R1', 'Phòng gai', 0, 40, 50, 14, 4, [
   B(0, 0, 50, 2), F((0, 10), (50, 10)), H('spike', 6, 9, 8, 1), H('spike', 18, 9, 10, 1), H('spike', 32, 9, 10, 1),
   E('R', 3, 9), E('S', 46, 9), E('D', 24, 5), PATH((1, 9), (5, 9), (10, 6), (15, 9), (17, 9), (23, 5), (29, 9), (31, 9), (37, 5), (43, 9), (49, 9))], '''
- **Mục đích:** tầng 1 phòng thí nghiệm Gate: **gai sàn dày**, chỉ chừa ô an toàn 2–4 ô.
- **Địa hình:** phòng 50 ô, trần ở y 42, sàn ở y 50. 3 bãi gai dài 8–10 ô.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #1 ở đầu phòng.
- **Ghi chú:** dữ liệu game khuyên mặc trọn bộ Blade hoặc Shadow (Shadow miễn gai). Không có capsule/Heart Tank/Sub-Tank.'''),

 Room('R2', 'Bệ di động trên gai', 50, 36, 64, 18, 5, [
   F((0, 14), (6, 14)), F((58, 14), (64, 14)), H('spike', 6, 16, 52, 2), P(10, 12, 5, 'move'), P(22, 6, 5, 'move'), P(34, 10, 5, 'move'), P(46, 5, 5, 'move'),
   AR(24, 12, 0, -5, 'wind'), AR(48, 10, 0, -4, 'wind'), X(8, 2, 'bệ ngang và bệ dọc xen kẽ'), E('D', 30, 3), E('D', 52, 12),
   PATH((1, 13), (6, 13), (12, 11), (24, 5), (36, 9), (48, 4), (59, 13), (63, 13))], '''
- **Mục đích:** **bệ di động** cả ngang lẫn dọc trên một hố gai dài 52 ô.
- **Cơ chế:** bệ 1 và 3 chạy ngang 6 ô; bệ 2 và 4 chạy lên xuống 6 ô. Nhảy từ bệ ngang sang bệ dọc phải canh cả hai chuyển động.
- **Địch:** 2 Drone: một bay cao, một bay sát gai.'''),

 Room('R3', 'Băng chuyền gai', 114, 40, 56, 14, 5, [
   B(0, 0, 56, 2), F((0, 10), (56, 10)), CV(8, 9.4, 18, 1), H('spike', 26, 6, 1, 4), CV(30, 9.4, 18, -1), H('spike', 29, 2, 1, 2),
   B(20, 5, 4, 1), B(40, 5, 4, 1), X(10, 7.5, 'băng chuyền đẩy vào vách gai'), E('B', 36, 9), E('R', 52, 9),
   PATH((1, 9), (19, 9), (22, 4), (27, 4.6), (31, 9), (39, 9), (42, 4), (45, 9), (55, 9))], '''
- **Mục đích:** băng chuyền **đẩy người chơi vào vách gai** ở giữa phòng.
- **Địa hình:** phòng 56 ô. Giữa phòng có một vách gai thấp (cao 4 ô) mà hai băng chuyền đều đẩy về phía nó.
- **Cơ chế:** băng chuyền 120px/giây. Phải nhảy lên kệ trên cao ngay trước vách gai, rồi nhảy qua.
- **Địch:** 1 Brute trên băng chuyền thứ hai (bị đẩy về phía vách gai theo người chơi).
- **Vật phẩm:** Reploid #2 cuối phòng.'''),

 Room('MID', 'Lõi cảnh vệ', 170, 36, 30, 16, 6, arena(30, 16, 14) + [H('spike', 2, 1, 26, 1), E('M', 15, 7), X(4, 11, 'lõi + 4 khối gai bay')], '''
- **Đấu trường 26 ô**, kín, trần phủ gai.
- **Lõi cảnh vệ** lơ lửng giữa phòng, điều khiển 4 khối gai bay.
- **Đòn đánh:**
  - Khối gai bay theo hình vuông quanh sân.
  - Khối gai lao thẳng về phía người chơi, cắm vào vách 2 giây (đứng lên được, làm bệ).
- **Điểm yếu:** lõi, chỉ hở khi ít nhất 2 khối gai đang cắm vào vách.
- **Phần thưởng:** mở cầu bệ chéo. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Cầu bệ chéo', 200, 36, 60, 18, 6, [
   F((0, 14), (6, 14)), F((54, 14), (60, 14)), H('spike', 6, 16, 48, 2), P(10, 12, 5, 'move'), P(20, 8, 5, 'move'), P(30, 12, 5, 'move'), P(40, 7, 5, 'move'),
   X(8, 2, 'bệ chạy chéo 45°'), E('C', 2, 13), E('R', 32, 11), E('S', 57, 13), E('D', 46, 3),
   PATH((1, 13), (6, 13), (12, 11), (22, 7), (32, 11), (42, 6), (55, 13), (59, 13))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** bệ chạy **chéo 45°** trên hố gai.
- **Cơ chế:** mỗi bệ chạy chéo lên-xuống 5 ô. Đáp lên bệ đang đi xuống thì có cảm giác "hụt chân".
- **Địch:** 1 Drone, 1 Sniper ở mép bên kia.
- **Vật phẩm:** Reploid #3 trên bệ thứ ba.'''),

 Room('R5', 'Trục thang máy dung nham', 260, -6, 26, 58, 8, s5 + [
   H('lava', 2, 52, 22, 4), AR(13, 52, 0, -4, 'alarm'), X(4, 50.5, 'dung nham dâng 60 → 80px/s'), X(3, 6, 'thang máy chạy lên 70px/s'),
   E('D', 10, 30), E('D', 18, 14), p5], '''
- **Mục đích:** cao trào của màn. Trục dọc 600px: **thang máy** chạy lên chậm hơn **dung nham dâng**.
- **Địa hình:** trục rộng 22 ô, cao 54 ô (từ y 66 lên y 13). 5 thang máy nhỏ.
- **Cơ chế:**
  - Dung nham dâng 60px/giây, tăng lên 80px/giây ở nửa trên.
  - Thang máy tự chạy lên 70px/giây rồi dừng ở đỉnh hành trình (6 ô) và quay xuống.
  - Đứng yên trên thang máy thì sớm muộn bị dung nham đuổi kịp. Phải nhảy sang thang máy kế tiếp, cao hơn, đúng lúc nó đang ở đáy hành trình.
  - Khác Lò Nham Thạch (kệ cố định) và Khu dung nham (dâng theo bậc): ở đây mọi điểm đứng đều di chuyển.
- **Địch:** 2 Drone.'''),

 Room('R6', 'Trạm nghỉ', 286, -9, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('C', 2, 9), E('R', 15, 9), X(4, 5, 'năng lượng LỚN'), PATH((1, 9), (28, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn**, cửa boss.'''),

 Room('BOSS', 'Nightmare Mother', 316, -13, 32, 16, 7, arena(32, 16, 14) + [H('spike', 2, 13, 4, 1), H('spike', 26, 13, 4, 1), E('*', 18, 6), X(4, 3, 'pha 2: gai lan vào giữa')], '''
- **Đấu trường 28 ô**, kín, hai góc sàn có gai.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (lõi trung tâm, 2 khối phụ, bắn Nightmare).
- **Pha 2** (dưới 50% HP):
  - **Gai sàn lan dần vào giữa** mỗi 10 giây (mỗi lần thêm 2 ô mỗi bên), tối đa còn 12 ô sàn an toàn.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Phòng thí nghiệm Gate 1', en="Gate's Secret Lab 1", boss='Nightmare Mother', act='Pháo đài X6', theme=THEME, capsule='',
 subtitle='Area 1: R1 (gai sàn) → R2 (bệ ngang/dọc) → R3 (băng chuyền gai) → Mini-boss  |  Area 2: R4 (bệ chéo) → R5 (thang máy, dung nham dâng) → R6 trạm → Boss',
 keep='Boss Nightmare Mother, sàn gai dày đặc, bệ di động dọc/ngang, trục leo dọc có dung nham dâng vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.',
 concept='Tầng 1 phòng thí nghiệm bí mật của Gate. Đây là **màn của các bệ di động trên gai**: ngang, dọc, chéo, rồi thang máy chạy đua với dung nham.',
 areas=['**Area 1 – Phòng thí nghiệm đỏ:** gai khắp nơi, đèn đỏ. Gai sàn, bệ ngang/dọc, băng chuyền đẩy vào gai.',
        '**Area 2 – Lò dưới phòng thí nghiệm:** bệ chéo, rồi trục thang máy với dung nham dâng.'],
 flow='nhảy qua bãi gai → bệ ngang/dọc → băng chuyền đẩy vào vách gai → mini-boss khối gai bay → bệ chéo → đua với dung nham trên thang máy → boss',
 time='khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen',
 refs=['**X6, Gate Lab 1:** gai sàn dày đặc, bệ di động dọc/ngang, trục leo 600px với dung nham dâng.',
       '**X4, màn Magma Dragoon:** dung nham dâng.',
       '**X2, màn X-Hunter / X3, màn Doppler 1:** bệ di động trên gai trong pháo đài.',
       '**X Corrupted:** dùng lại cơ chế cũ (dung nham dâng) với điểm đứng di động để thành thử thách mới.'],
 engine=['Bệ di động ngang, dọc và chéo; thang máy tự chạy lên rồi quay xuống.',
         'Dung nham dâng liên tục có tăng tốc.',
         'Băng chuyền và vách gai.',
         'Mini-boss Lõi cảnh vệ: khối gai bay cắm vào vách làm bệ tạm.',
         'Gai sàn lan dần trong trận boss.'],
 art=['**Tileset "Gate Lab":** 47 ô viền kim loại đỏ có đèn, gai, băng chuyền.',
      '**Vật thể:** bệ di động (3 loại), thang máy, khối gai bay, mặt dung nham (4 khung).',
      '**Nền:** ống nghiệm Nightmare và máy móc của Gate (2 lớp parallax).'],
)
for r in rooms:
    r['y'] += 16
STAGE['rooms'] = rooms
