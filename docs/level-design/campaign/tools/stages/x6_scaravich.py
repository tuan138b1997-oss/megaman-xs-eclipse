from kit import *

THEME = dict(bg1=(46, 40, 34), bg2=(38, 34, 30), rock1=(140, 124, 96), rock2=(128, 112, 88))
s4, p4 = shaft_up(22, 48, n=4)


def light(x, y, w=5, h=8, lab=''): return Z('alarm', x, y, w, h, lab)


rooms = [
 Room('R1', 'Sảnh bảo tàng', 0, 50, 44, 14, 2, [
   B(0, 0, 44, 2), F((0, 10), (44, 10)), B(16, 7, 4, 3), light(26, 2, 5, 8, 'đèn pha'), AR(26, 5, 5, 0, 'alarm'),
   E('S', 40, 9), E('D', 8, 5), PATH((1, 9), (43, 9))], '''
- **Mục đích:** giới thiệu **đèn pha an ninh** trong lúc chưa có hậu quả nặng.
- **Địa hình:** sảnh 44 ô, trần ở y 52, sàn ở y 60. Một tủ trưng bày làm chỗ nấp.
- **Cơ chế – đèn pha:**
  - Đèn quét qua lại trên sàn (rộng 5 ô, 60px/giây).
  - Đứng trong vệt sáng 0.5 giây là **bị phát hiện**: còi báo động, cửa chớp hai đầu phòng sập xuống và 2 Drone an ninh bay ra. Hạ hết Drone thì cửa mở lại.
  - Nấp sau tủ trưng bày hoặc lướt qua nhanh thì không bị phát hiện.
- **Địch:** 1 Drone, 1 Sniper (không tính Drone an ninh sinh ra khi báo động).'''),

 Room('R2', 'Hành lang đèn pha', 44, 50, 70, 14, 3, [
   B(0, 0, 70, 2), F((0, 10), (70, 10)), B(10, 7, 4, 3), B(28, 7, 4, 3), B(46, 7, 4, 3), B(60, 7, 4, 3),
   light(16, 2), light(34, 2), light(52, 2), BAR(0, 2, 1, 8, 'door'), BAR(69, 2, 1, 8, 'door'), X(2, 3, 'cửa chớp sập khi báo động'),
   E('S', 66, 9), E('R', 42, 9), PATH((1, 9), (69, 9))], '''
- **Mục đích:** lẻn qua **3 đèn pha** quét lệch pha nhau.
- **Địa hình:** hành lang 70 ô, 4 tủ trưng bày làm chỗ nấp, cách nhau 18 ô.
- **Cơ chế:** đi từ tủ này sang tủ kia lúc vệt sáng vừa quét qua. Bị phát hiện thì cửa chớp sập, 2 Drone an ninh xuất hiện.
- **Địch:** 1 Sniper cuối hành lang.
- **Vật phẩm:** Reploid #1 sau tủ thứ ba.
- **Ghi chú:** bị phát hiện không mất mạng, chỉ tốn thời gian và máu. Người chơi giỏi đi qua không bị phát hiện lần nào.'''),

 Room('R3', 'Cụm phòng Cell 1', 114, 40, 50, 24, 4, [
   B(0, 0, 50, 1), B(0, 0, 2, 14), B(48, 1, 2, 13), F((0, 20), (50, 20)), B(10, 8, 40, 1), B(8, 1, 2, 8),
   light(24, 1, 5, 7, ''), E('G', 44, 19), E('G', 13, 7), E('H', 38, 7), E('D', 26, 14), E('S', 30, 19),
   X(36, 21.4, 'cổng P1'), X(11, 4.5, 'P2'), PATH((1, 19), (49, 19)), ALT((44, 19), (13, 7), (38, 7))], '''
- **Mục đích:** giới thiệu **cổng dịch chuyển** của cụm phòng triển lãm.
- **Địa hình:**
  - Phòng 2 tầng. Tầng dưới (y 60) là đường chính, đi thẳng sang phải.
  - Tầng trên (y 48) là phòng kho bảo tàng, không có lối đi bộ vào.
- **Cơ chế:** **cổng P1** cuối tầng dưới đưa lên **cổng P2** ở đầu tầng trên. Tầng trên có một đèn pha quét.
- **Địch:** 1 Drone, 1 Sniper ở tầng dưới.
- **Lối phụ (Heart Tank):** cuối tầng trên (x ≈ 152, y ≈ 47). Phải đi qua vệt đèn pha mà không bị phát hiện; bị phát hiện thì Heart Tank bị khóa trong lồng kính cho tới khi hạ hết Drone an ninh.'''),

 Room('R4', 'Giếng mái vòm', 164, 14, 22, 48, 4, s4 + [
   H('trash', 9, 22, 4, 2), X(4, 25, 'đèn chùm lắc 3s'), E('D', 11, 32), p4], '''
- **Mục đích:** đoạn dọc dưới mái vòm bảo tàng.
- **Địa hình:** giếng rộng 18 ô, cao 44 ô (từ y 60 lên y 21). 4 kệ zigzag.
- **Bẫy – đèn chùm:** một đèn chùm pha lê lắc qua lại giữa giếng (chu kỳ 3 giây). Đứng lên đèn chùm được, nhưng nó lắc mạnh dần.
- **Địch:** 1 Drone.'''),

 Room('MID', 'Đại cột Totem', 186, 7, 30, 16, 5, arena(30, 16, 14) + [BAR(12, 1, 6, 13, 'trash'), E('M', 15, 6), X(3, 10, '4 mặt totem')], '''
- **Đấu trường 26 ô**, hai vách đá tường được. Giữa sân là một **cột totem khổng lồ** cao từ sàn tới trần, chắn đôi đấu trường.
- **Đòn đánh:**
  - Totem có 4 mặt xếp chồng, mỗi mặt quay về một phía và bắn theo nhịp.
  - Mặt dưới cùng phun lửa sát sàn.
  - Totem thụt xuống sàn 2 giây rồi trồi lên (đứng trên chỗ nó trồi là bị hất lên trần).
- **Điểm yếu:** phá từng mặt từ dưới lên. Mỗi mặt bị phá thì totem thấp đi một nấc, đến khi nhảy qua được.
- **Phần thưởng:** mở đường vào khu triển lãm cổ. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Dốc đá lăn', 216, 9, 60, 14, 5, [
   B(0, 0, 60, 2), F((0, 12), (30, 12), (50, 7), (60, 7)), H('trash', 52, 5, 2, 2), AR(50, 5, -6, 3, 'alarm'),
   X(34, 4, 'đá lăn xuống mỗi 2.5s'), B(10, 9, 3, 3), E('C', 2, 11), E('B', 22, 11), E('S', 56, 6), E('R', 11, 8),
   PATH((1, 11), (30, 11), (50, 6), (59, 6))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** leo dốc ngược chiều **đá lăn**.
- **Địa hình:** hành lang 60 ô, đoạn sau là dốc 22.5° đi lên dài 20 ô.
- **Bẫy:** tảng đá tròn (tượng cổ vỡ) lăn từ đỉnh dốc xuống mỗi 2.5 giây, nhanh dần. Nhảy qua, hoặc bắn 4 phát cho vỡ. Đá lăn hết dốc thì đập vào bệ tượng đầu phòng và vỡ.
- **Địch:** 1 Brute giữa phòng (đá lăn hạ được nó), 1 Sniper trên đỉnh dốc.
- **Vật phẩm:** Reploid #2 nấp trên bệ tượng đầu phòng.'''),

 Room('R6', 'Cụm phòng Cell 2', 276, 0, 64, 26, 7, [
   B(0, 16, 8, 10), B(8, 24, 56, 2), B(16, 12, 32, 1), B(52, 4, 10, 1), B(62, 0, 2, 20), B(0, 0, 62, 1),
   H('spike', 22, 23, 22, 1), H('trash', 40, 10, 2, 2), H('trash', 30, 10, 2, 2), AR(46, 10.5, -6, 0, 'alarm'),
   light(18, 1, 5, 11, ''), light(34, 1, 5, 11, ''), E('G', 12, 23), E('G', 20, 11), E('A', 57, 3), E('D', 30, 5), E('D', 54, 14),
   X(10, 21, 'P3'), X(18, 9.6, 'P4'), X(24, 21.4, 'hố gai'),
   PATH((1, 15), (8, 15), (12, 23), (20, 11), (47, 11), (50, 23), (63.5, 23)), ALT((47, 11), (61, 8), (57, 3))], '''
- **Mục đích:** cao trào của màn. Kết hợp **cổng dịch chuyển, đèn pha và đá lăn** trong một phòng.
- **Địa hình:**
  - Tầng dưới (y 24) bị cắt bởi **hố gai** dài 22 ô, không nhảy qua được.
  - Cổng **P3** ở đầu tầng dưới đưa lên cổng **P4** trên ban công giữa (y 12).
  - Ban công dài 32 ô, có 2 đèn pha quét.
  - Đá lăn từ đầu phải ban công lăn sang trái mỗi 2 giây, đúng vào đường đi.
  - Cuối ban công nhảy xuống tầng dưới phía sau hố gai để ra cửa.
- **Cơ chế:** bị đèn pha phát hiện thì đá lăn nhanh gấp đôi và cửa ra sập lại tới khi hạ Drone an ninh.
- **Địch:** 2 Drone.
- **Lối phụ (Capsule Blade Arm):**
  - Hốc cao sát vách phải (x ≈ 333, y ≈ 3).
  - Từ cuối ban công, đá tường vách phải 3 lần lên hốc. Phải làm trước khi đá lăn tiếp theo tới.
- **Ghi chú:** phòng này cũng giữ cổng sang lối thay thế (Alt Path) theo dữ liệu game, đặt cạnh cổng P3.'''),

 Room('R7', 'Phòng Totem', 340, 12, 56, 14, 6, [
   B(0, 0, 56, 2), F((0, 10), (56, 10)), BAR(14, 4, 3, 6, 'trash'), BAR(28, 3, 3, 7, 'trash'), BAR(42, 5, 3, 5, 'trash'),
   X(12, 2.4, 'totem trồi/thụt 2s, lệch pha'), E('C', 2, 9), E('R', 22, 9), E('S', 52, 9), E('D', 36, 4), E('T', 29.5, 2.5),
   PATH((1, 9), (55, 9)), ALT((26, 9), (28, 3), (29.5, 2.5))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: **cột totem** trồi lên chặn đường rồi thụt xuống.
- **Địa hình:** phòng 56 ô, 3 cột totem.
- **Cơ chế:** mỗi cột trồi lên chặn kín 2 giây, thụt xuống 2 giây, lệch pha nhau. Đứng trên cột lúc nó trồi thì bị đẩy lên sát trần.
- **Địch:** 1 Drone, 1 Sniper cuối phòng.
- **Vật phẩm:** Reploid #3 giữa cột 1 và cột 2.
- **Lối phụ (Sub-Tank):** trên đỉnh cột totem thứ hai, lúc nó trồi lên cao nhất. Đứng lên cột lúc nó đang thụt rồi để nó đưa lên.'''),

 rest('R8', 'Phòng trưng bày cuối', 396, 12, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Ground Scaravich', 426, 8, 32, 16, 6, arena(32, 16, 14) + [light(8, 1, 5, 13, 'pha 2: tối, chỉ có đèn pha'), E('*', 22, 9)], '''
- **Đấu trường 28 ô**, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (lăn quả cầu đất, đào, nhảy).
- **Pha 2** (dưới 50% HP):
  - **Tắt đèn**, chỉ còn một đèn pha quét qua lại. Quả cầu đất chỉ thấy khi lăn vào vệt sáng.
  - Bị đèn pha chiếu vào thì Scaravich nhắm theo chính xác hơn.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Bảo tàng Trung tâm', en='Central Museum', boss='Ground Scaravich', act='Act II · X6', theme=THEME, capsule='Blade Arm',
 subtitle='Area 1 (sảnh và Cell 1): R1 → R2 (đèn pha) → R3 (cổng P1–P2, Heart Tank) → R4 (leo) → Mini-boss Totem  |  Area 2 (triển lãm cổ): R5 (đá lăn) → R6 (Cell 2: P3–P4) → R7 (totem) → R8 → Boss',
 keep='Boss, capsule Blade Arm, 5 đèn pha an ninh, 4 cổng dịch chuyển (Cell 1 và Cell 2), Đại cột Totem ở mid-gate, đá lăn và cổng Alt Path vẫn giữ; thêm 4 Reploid, Sub-Tank và thay địa hình. Heart Tank giữ ở Cell 1.',
 concept='Bảo tàng lịch sử ban đêm, hệ thống an ninh vẫn chạy. Màn này là **lẻn và giải đố**: tránh đèn pha, dùng cổng dịch chuyển giữa các phòng triển lãm, né đá lăn và totem cổ.',
 areas=['**Area 1 – Sảnh và Cell 1:** gỗ, đá cẩm thạch, ánh đèn vàng ấm. Dạy đèn pha, chỗ nấp, cổng dịch chuyển, leo giếng có đèn chùm.',
        '**Area 2 – Khu triển lãm cổ:** đá sa thạch, tượng Ai Cập và totem. Đá lăn, cụm cổng Cell 2, phòng totem trồi thụt.'],
 flow='nấp tránh đèn pha → lẻn qua hành lang → dịch chuyển lên kho lấy Heart Tank → leo dưới đèn chùm → phá cột totem → leo dốc đá lăn → giải cụm Cell 2 → vượt totem trồi thụt → boss trong bóng tối',
 time='khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X6, màn Ground Scaravich:** đèn pha an ninh, cụm cổng dịch chuyển Cell 1/Cell 2, Đại cột Totem, đá lăn, capsule Blade Arm.',
       '**X8, màn Dark Mantis:** đèn quét, bị phát hiện thì sinh thêm địch.',
       '**X5, màn mẫu Lò Nham Thạch (R2):** vật lăn theo dốc đuổi người chơi.',
       '**X Corrupted:** bị phát hiện không phạt mất mạng mà phạt thời gian và khóa vật phẩm.'],
 engine=['Đèn pha quét theo đường cố định; đứng trong vệt sáng 0.5 giây thì kích hoạt báo động (cửa chớp sập, sinh Drone an ninh, khóa vật phẩm).',
         'Cổng dịch chuyển theo cặp (P1–P2, P3–P4).',
         'Đá lăn theo dốc, phá được, gây sát thương cả địch.',
         'Đèn chùm lắc (bệ con lắc).',
         'Cột totem trồi/thụt theo nhịp, đẩy người chơi lên.',
         'Mini-boss Đại cột Totem: phá từng mặt từ dưới lên.'],
 art=['**Tileset "Sảnh bảo tàng" (Area 1):** 47 ô viền đá cẩm thạch và gỗ, tủ trưng bày, cửa chớp (2 trạng thái).',
      '**Tileset "Triển lãm cổ" (Area 2):** 47 ô viền sa thạch, dốc, bệ tượng.',
      '**Vật thể:** đèn pha (vệt sáng 3 khung), đèn chùm, cổng dịch chuyển (4 khung), đá lăn (4 khung), cột totem (4 mặt), lồng kính.',
      '**Nền:** Area 1: phòng trưng bày tối (2 lớp parallax). Area 2: tượng và kim tự tháp mô hình (2 lớp).'],
)
STAGE['rooms'] = rooms
