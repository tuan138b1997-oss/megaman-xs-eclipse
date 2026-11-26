from kit import *

THEME = dict(bg1=(60, 34, 28), bg2=(50, 30, 30), rock1=(104, 72, 60), rock2=(96, 70, 66))
O = 6
s5, p5 = shaft_up(26, 58, n=5)
for i, g in enumerate(s5):
    if g[0] == 'plat': s5[i] = ('plat', 'thrust') + g[2:]

rooms = [
 Room('R1', 'Miệng núi', 0, O + 50, 44, 16, 2, [
   F((0, 12), (12, 12), None, (16, 12), (30, 12), None, (34, 12), (44, 12)), H('lava', 12, 12, 4, 4), H('lava', 30, 12, 4, 4),
   BAR(13, 4, 2, 8, 'lava'), X(10, 2.5, 'cột phun 1.5s / 3s'), E('S', 40, 11), E('D', 22, 4),
   PATH((1, 11), (11, 11), (14, 2.5), (17, 11), (29, 11), (32, 8), (35, 11), (43, 11))], '''
- **Mục đích:** giới thiệu **cột dung nham phun** từ hố: bật 1.5 giây, tắt 3 giây.
- **Địa hình:** sườn núi 44 ô, mặt đất ở y 68. 2 hố dung nham rộng 4 ô. Hố đầu có cột phun cao 8 ô.
- **Địch:** 1 Drone, 1 Sniper.
- **Trang trí:** đá bazan đen, khói, tro bay, trời đỏ.
- **Khác màn mẫu Lò Nham Thạch:** màn này là núi lửa tự nhiên, không phải nhà máy; cơ chế chính là bệ phản lực và vòng lửa Donut.'''),

 Room('R2', 'Hồ dung nham', 44, O + 50, 70, 18, 3, [
   F((0, 12), (6, 12)), F((64, 12), (70, 12)), H('lava', 6, 13, 58, 5), P(8, 12, 5, 'thrust'), P(36, 12, 5, 'thrust'),
   B(30, 10, 3, 8), E('W', 31.5, 6), X(24, 3, 'Donut #1: vòng lửa quay quanh trụ'), X(8, 15, 'bệ phản lực bay ngang 4s rồi chìm'),
   E('D', 20, 5), E('D', 52, 4), E('R', 67, 11),
   PATH((1, 11), (6, 11), (10, 11), (28, 11), (31, 9), (34, 11), (38, 11), (63, 11), (69, 11))], '''
- **Mục đích:** vượt hồ dung nham bằng **bệ phản lực**.
- **Địa hình:** hồ rộng 58 ô, chạm dung nham là mất mạng. Một trụ đá giữa hồ.
- **Cơ chế – bệ phản lực:**
  - Đứng lên thì bệ bay ngang sang phải 110px/giây trong 4 giây, rồi hết nhiên liệu và chìm dần.
  - Phải nhảy sang trụ đá rồi bệ thứ hai trước khi bệ dưới chân chìm.
- **Bẫy – Donut #1:** cỗ máy vòng lửa gắn trên trụ đá. 3 quả cầu lửa quay quanh trụ (bán kính 3 ô, 1 vòng mỗi 2 giây). Bắn hạ được bằng 8 phát hoặc 2 phát nạp đầy; hạ được thì trụ an toàn.
- **Địch:** 2 Drone.
- **Vật phẩm:** Reploid #1 ở bờ bên kia.'''),

 Room('R3', 'Hang đá nóng', 114, O + 50, 60, 16, 4, [
   B(0, 0, 60, 2), F((0, 12), (60, 12)), H('fire', 14, 2, 1, 2), H('fire', 30, 2, 1, 2), H('fire', 44, 2, 1, 2),
   X(12, 4.5, 'giọt dung nham rơi mỗi 2s'), P(48, 6, 8), E('B', 26, 11), E('S', 54, 11), E('T', 52, 5),
   PATH((1, 11), (59, 11)), ALT((44, 11), (47, 7), (52, 5))], '''
- **Mục đích:** đoạn trong hang, đổi nhịp. Nguy hiểm từ trên đầu.
- **Địa hình:** hang 60 ô, trần ở y 58, sàn ở y 68.
- **Bẫy:** 3 điểm nhỏ giọt dung nham từ trần, mỗi 2 giây một giọt. Chỗ giọt rơi xuống cháy 1 giây.
- **Địch:** 1 Brute giữa hang, 1 Sniper cuối hang.
- **Lối phụ (Sub-Tank):** gờ đá cao cuối hang (x ≈ 162, y ≈ 62). Đá tường vách hang lên, nhưng một điểm nhỏ giọt nằm ngay trên chỗ đá tường: canh nhịp.'''),

 Room('MID', 'Donut Nightmare lớn', 174, O + 48, 30, 18, 5, arena(30, 18, 14) + [E('M', 15, 6), X(4, 11, 'vòng lửa co giãn')], '''
- **Đấu trường 26 ô**, hai vách đá tường được.
- **Donut Nightmare lớn** lơ lửng giữa phòng, 6 quả cầu lửa quay quanh.
- **Đòn đánh:**
  - Vòng lửa **co lại và giãn ra** (bán kính 3 ↔ 9 ô). Lúc giãn hết cỡ thì chạm vách: phải lọt vào giữa hai quả cầu.
  - Bắn từng quả cầu lửa ra 4 hướng.
  - Lao sang một vách, kéo vòng lửa theo.
- **Điểm yếu:** lõi ở tâm. Bắn trúng được lúc vòng lửa giãn ra.
- **Phần thưởng:** mở đường xuống dòng dung nham. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Dòng bè đá', 204, O + 50, 56, 18, 5, [
   F((0, 12), (6, 12)), F((50, 12), (56, 12)), H('lava', 6, 13, 44, 5), AR(14, 16, 8, 0, 'current'),
   P(10, 12, 6, 'move'), P(26, 12, 6, 'move'), P(40, 12, 6, 'move'), BAR(22, 3, 2, 9, 'lava'),
   X(8, 15, 'bè bazan trôi theo dòng 60px/s'), E('C', 2, 11), E('R', 28, 11), E('D', 34, 5), E('S', 53, 11),
   PATH((1, 11), (6, 11), (13, 11), (29, 11), (43, 11), (55, 11))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đi trên **bè đá bazan** trôi theo dòng dung nham.
- **Địa hình:** dòng dung nham rộng 44 ô.
- **Cơ chế:** 3 bè đá trôi sang phải 60px/giây. Một cột phun ở giữa dòng (bật 1.5 giây, tắt 3 giây) chắn đường trôi: phải nhảy sang bè khác trước khi bè trôi vào cột.
- **Địch:** 1 Drone, 1 Sniper ở bờ bên kia.
- **Vật phẩm:** Reploid #2 trên bè thứ hai.'''),

 Room('R5', 'Trục núi lửa', 260, O + 6, 26, 58, 7, s5 + [
   SP('riser', x=2, w=22, bottom=56, stop=8, trigger=50, mode='step', step=4, rise=1, pause=5, look='lava'),
   H('lava', 2, 50, 22, 6), X(4, 48.5, 'dung nham dâng 4 ô mỗi 6s'), E('W', 13, 9), X(15, 8.5, 'Donut #3 chặn lối ra'),
   B(2, 3, 2, 5), CW(4, 3, 4), P(2, 8, 6), E('A', 3, 7), E('H', 22, 26), P(20, 27, 4),
   E('D', 10, 30), p5, ALT((14, 18), (5, 8)), ALT((19, 33), (22, 27))], '''
- **Mục đích:** cao trào của màn. Leo trục dọc lòng núi lửa trong khi dung nham **dâng từng bậc**.
- **Địa hình:**
  - Trục rộng 22 ô, cao 54 ô (từ y 68 lên y 13).
  - 5 bệ phản lực xếp zigzag. Đứng lên thì bệ bốc lên 4 ô rồi dừng; hai vách đá tường được.
- **Cơ chế – dung nham dâng theo bậc:**
  - Dung nham dâng **4 ô trong 1 giây, rồi đứng yên 5 giây**, lặp lại. Mặt đất rung trước mỗi lần dâng.
  - Khác giếng nham của màn mẫu (dâng liên tục): ở đây người chơi có nhịp nghỉ, nhưng bậc dâng nhanh nên đứng sai chỗ là chết ngay.
- **Bẫy – Donut #3:** cỗ máy vòng lửa chắn ngay lối ra trên đỉnh. Phải hạ nó (8 phát) trong lúc dung nham vẫn dâng.
- **Địch:** 1 Drone giữa trục.
- **Lối phụ (Heart Tank):** hốc ở vách phải giữa trục (x ≈ 282, y ≈ 38). Chỉ vào được lúc dung nham đang nghỉ.
- **Lối phụ (Capsule Shadow Arm):**
  - Góc trên trái có **khối sắt nứt** (x ≈ 264, y ≈ 19). Chỉ phá được bằng **Charge Saber** của Zero/Blade hoặc **đạn nạp đầy**.
  - Sau khối sắt là capsule Shadow Arm.
  - Dung nham dừng hẳn khi đã hạ Donut #3, nên quay lại phá khối sắt sau đó là an toàn.'''),

 Room('R6', 'Đỉnh miệng phun', 286, O + 3, 52, 14, 6, [
   F((0, 10), (52, 10)), BAR(12, 2, 2, 8, 'lava'), BAR(30, 2, 2, 8, 'lava'), Z('wind', 0, 0, 52, 10, 'khí nóng đẩy lên khi nhảy'),
   E('C', 2, 9), E('S', 46, 9), E('D', 22, 4), E('R', 40, 9), PATH((1, 9), (51, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: cột phun và luồng khí nóng.
- **Địa hình:** vành miệng núi lửa 52 ô, ngoài trời.
- **Cơ chế:**
  - 2 cột phun lệch pha (bật 1.5 giây, tắt 3 giây).
  - Luồng khí nóng bốc lên làm mỗi cú nhảy cao hơn 2 ô: dễ nhảy qua cột phun, nhưng cũng dễ bay vào tầm bắn của Drone.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #3 trước cửa phòng tạm.'''),

 rest('R7', 'Hang nghỉ', 338, O + 3, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Blaze Heatnix', 368, O + -1, 32, 18, 6, arena(32, 16, 14) + [H('lava', 2, 13.4, 3, 0.6), H('lava', 27, 13.4, 3, 0.6), E('*', 18, 6),
   X(5, 4, 'pha 2: nửa sân ngập nham')], '''
- **Đấu trường 28 ô**, hai vách đá tường được, hai góc có rãnh dung nham nhỏ.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Magma Blade, lao lửa, chim lửa).
- **Pha 2** (dưới 50% HP):
  - **Dung nham dâng ngập một nửa sân** (trái hoặc phải), đổi bên mỗi 10 giây.
  - Người chơi bị dồn vào nửa còn lại; Heatnix bay qua phần dung nham để tấn công.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Khu dung nham', en='Magma Area', boss='Blaze Heatnix', act='Act II · X6', theme=THEME, capsule='Shadow Arm',
 subtitle='Area 1 (sườn núi và hồ): R1 → R2 (bệ phản lực, Donut #1) → R3 (hang) → Mini-boss Donut lớn  |  Area 2 (lòng núi): R4 (bè đá) → R5 (trục, nham dâng theo bậc) → R6 → R7 → Boss',
 keep='Boss, capsule Shadow Arm, 3 cỗ máy vòng lửa Nightmare Donut, bệ phản lực, trục leo có dung nham dâng và khối sắt nứt vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Núi lửa tự nhiên bị virus Nightmare chiếm, khác hẳn nhà máy của màn mẫu Lò Nham Thạch. Màn này xoay quanh **những thứ trôi trên dung nham** (bệ phản lực, bè đá) và **vòng lửa Donut** chặn đường.',
 areas=['**Area 1 – Sườn núi và hồ (ngoài trời):** đá bazan đen, trời đỏ. Dạy cột phun, bệ phản lực bay ngang, Donut, hang nhỏ giọt.',
        '**Area 2 – Lòng núi:** đỏ rực, khói. Bè đá trôi theo dòng, trục leo có dung nham dâng từng bậc, vành miệng phun.'],
 flow='né cột phun → bay qua hồ trên bệ phản lực → hang nhỏ giọt → mini-boss vòng lửa co giãn → nhảy bè đá → leo trục khi nham dâng theo bậc → phá Donut chặn cửa → boss nửa sân ngập nham',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X6, màn Blaze Heatnix:** Nightmare Donut, bệ phản lực Thruster, trục leo dung nham, khối sắt phá bằng Charge Saber giấu capsule Shadow Arm.',
       '**X4, màn Magma Dragoon:** dung nham dâng buộc leo nhanh (ở đây đổi thành dâng theo bậc để khác màn mẫu).',
       '**X2, màn Flame Stag:** trục dọc lòng núi lửa.',
       '**X Corrupted:** chướng ngại vừa là bẫy vừa là mục tiêu (Donut chặn cửa phải phá).'],
 engine=['Cột dung nham phun theo nhịp.',
         'Bệ phản lực bay ngang có hết nhiên liệu; bệ phản lực bốc lên từng nấc.',
         'Bè đá trôi theo dòng.',
         'Dung nham dâng theo bậc (dâng nhanh, nghỉ, lặp lại), dừng khi hạ mục tiêu.',
         'Vòng lửa Donut: cầu lửa quay quanh tâm, phá được.',
         'Khối sắt nứt chỉ phá được bằng Charge Saber hoặc đạn nạp đầy.',
         'Luồng khí nóng tăng độ cao nhảy.',
         'Mini-boss Donut lớn có vòng lửa co giãn.'],
 art=['**Tileset "Sườn núi" (Area 1):** 47 ô viền bazan, hố dung nham, mạch nham trong đá.',
      '**Tileset "Lòng núi" (Area 2):** 47 ô viền đá đỏ, bè bazan, khối sắt nứt (2 trạng thái).',
      '**Vật thể:** cột phun (4 khung), bệ phản lực (lửa 3 khung), Donut (cầu lửa 4 khung), giọt nham, mặt dung nham động (4 khung).',
      '**Nền:** Area 1: núi lửa xa và trời đỏ (2 lớp parallax). Area 2: lòng núi và dòng nham xa (2 lớp).'],
)
STAGE['rooms'] = rooms
