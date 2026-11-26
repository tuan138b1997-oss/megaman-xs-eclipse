from kit import *

THEME = dict(bg1=(34, 50, 44), bg2=(44, 40, 36), rock1=(110, 104, 90), rock2=(120, 100, 80))
O = 10
s3, p3 = shaft_up(20, 50, n=4)

rooms = [
 Room('R1', 'Sân đền', 0, O + 40, 44, 16, 2, [
   F((0, 12), (44, 12)), Z('rain', 0, 0, 44, 12, 'mưa axit: 3s mưa / 7s tạnh'), B(10, 5, 7, 1), B(28, 5, 7, 1),
   X(10, 3.6, 'mái che'), E('S', 38, 11), E('D', 22, 4), PATH((1, 11), (43, 11))], '''
- **Mục đích:** giới thiệu **mưa axit**: trong lúc mưa, đứng ngoài trời mất 1 máu mỗi 0.5 giây.
- **Địa hình:** sân đá 44 ô, mặt đất ở y 62. 2 mái ngói nhô ra từ tường đền làm chỗ trú.
- **Cơ chế:**
  - Mưa 3 giây, tạnh 7 giây. Trời tối sầm và có tiếng sấm 1.5 giây trước mỗi đợt.
  - Đứng dưới mái che thì an toàn.
- **Địch:**
  - 1 Drone bay lượn giữa hai mái.
  - 1 Sniper cuối sân, không sợ mưa.
- **Trang trí:** đèn lồng đá, cổng torii đổ, rêu ăn mòn.'''),

 Room('R2', 'Hành lang mái che', 44, O + 40, 76, 16, 3, [
   F((0, 12), (76, 12)), Z('rain', 0, 0, 76, 12, ''), B(4, 5, 8, 1), B(22, 5, 8, 1), B(40, 5, 8, 1), B(58, 5, 8, 1),
   X(14, 3, 'khoảng hở 10 ô'), E('D', 18, 4), E('B', 34, 11), E('R', 44, 11), E('S', 70, 11), E('T', 62, 4),
   PATH((1, 11), (75, 11)), ALT((56, 11), (57, 6), (62, 4))], '''
- **Mục đích:** chạy giữa các chỗ trú theo nhịp mưa.
- **Địa hình:** hành lang 76 ô có **4 mái che** dài 8 ô, cách nhau 10 ô.
- **Cơ chế:** 7 giây tạnh vừa đủ chạy qua 1 khoảng hở và hạ 1 con địch. Dừng lại đánh lâu là bị mưa bắt ngoài trời.
- **Địch:**
  - 1 Drone ở khoảng hở thứ nhất.
  - 1 Brute đứng giữa khoảng hở thứ hai: chặn đường chạy.
  - 1 Sniper cuối hành lang.
- **Vật phẩm:** Reploid #1 dưới mái che thứ ba.
- **Lối phụ (Sub-Tank):** trên **nóc mái che thứ tư** (x ≈ 106, y ≈ 64). Đá tường cột đền bên cạnh để lên, nhưng nóc mái là ngoài trời: phải lên, lấy và xuống trong một lần tạnh.'''),

 Room('R3', 'Tháp chuông', 120, O + 4, 20, 50, 4, s3 + [
   Z('rain', 2, 1, 16, 20, 'mái thủng: mưa lọt'), H('spike', 2, 47, 16, 1), E('D', 10, 30), p3], '''
- **Mục đích:** đoạn dọc. Nửa dưới tháp có mái che, nửa trên mái thủng nên mưa lọt vào.
- **Địa hình:** tháp rộng 16 ô, cao 46 ô (từ y 62 lên y 15). 4 kệ zigzag, hai vách đá tường được.
- **Cơ chế:** nửa trên (20 ô) dính mưa. Phải chờ tạnh ở kệ thứ hai rồi leo một mạch lên đỉnh trong 7 giây.
- **Địch:** 1 Drone giữa tháp.
- **Bẫy:** đáy tháp là rãnh gai (rơi từ kệ thứ nhất là trúng).'''),

 Room('R4', 'Cổng đền', 140, O + 0, 56, 16, 4, [
   F((0, 12), (56, 12)), Z('rain', 0, 0, 56, 12, ''), P(6, 6, 6), P(30, 5, 6), BAR(22, 1, 1, 11, 'door'), BAR(46, 1, 1, 11, 'door'),
   B(14, 5, 6, 1), E('K', 9, 5), E('K', 33, 4), E('S', 40, 11), E('D', 28, 3), E('R', 36, 11),
   X(20, 13.3, 'cổng 1'), X(44, 13.3, 'cổng 2'), PATH((1, 11), (7, 5), (12, 11), (21, 11), (31, 4), (36, 11), (55, 11))], '''
- **Mục đích:** bắn công tắc mở cổng đền, trong khi vẫn phải canh mưa.
- **Địa hình:** sân trước đền 56 ô, 2 cổng gỗ đóng chặn đường.
- **Cơ chế:**
  - **Công tắc #1** trên kệ đá trước cổng 1, **công tắc #2** trên kệ trước cổng 2.
  - Bắn trúng thì cổng mở hẳn. Kệ công tắc không có mái che: lên bắn lúc trời tạnh.
- **Địch:**
  - 1 Drone canh kệ công tắc #2.
  - 1 Sniper sau cổng 2.
- **Vật phẩm:** Reploid #2 giữa hai cổng, dưới mái che.'''),

 Room('MID', 'Rùa đá canh đền', 196, O + 0, 30, 16, 5, arena(30, 16, 14) + [E('M', 15, 10), X(4, 4, 'mai rùa bật đạn thường')], '''
- **Đấu trường 26 ô**, có mái, hai vách đá tường được.
- **Rùa đá canh đền** bò qua lại, mai cứng phản lại đạn thường.
- **Đòn đánh:**
  - Rụt vào mai và lăn ngang sân: đá tường để né.
  - Phun 3 giọt axit theo đường cong, đọng lại thành vũng 2 giây.
  - Dậm chân làm rơi đá vụn từ trần.
- **Điểm yếu:** đầu thò ra sau mỗi lần lăn. Đạn nạp đầy làm lật mai 3 giây.
- **Phần thưởng:** mở cửa vào chính điện. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Chính điện hai tầng', 226, O + 0, 64, 28, 5, [
   B(0, 14, 20, 3), B(24, 14, 40, 3), F((0, 26), (64, 26)), B(30, 6, 26, 1), Z('rain', 30, 0, 26, 6, ''),
   H('spike', 26, 25, 16, 1), P(46, 22, 6), BAR(62, 17, 2, 9, 'door'),
   E('C', 2, 13), E('A', 50, 5), E('H', 49, 21), E('G', 58, 25), E('B', 14, 13), E('S', 58, 13), E('R', 40, 13),
   X(20, 13, 'lỗ sàn'), X(32, 4.5, 'mái tầng 2'), X(52, 22.5, 'cổng ác mộng'),
   PATH((1, 13), (19, 13), (25, 13), (63, 13)), ALT((26, 13), (28, 8), (32, 5), (50, 5)), ALT((22, 15), (22, 24), (44, 21), (49, 21)), ALT((52, 24), (58, 25))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** phòng có **3 tầng**: mái ngói ngoài trời (capsule), sàn chính điện (đường chính), hầm dưới sàn (Heart Tank và cổng ác mộng).
- **Địa hình:**
  - Sàn chính ở y 24, dài 64 ô. Một **lỗ sàn** 4 ô (x 246–250) rơi xuống hầm.
  - Hầm ở y 36, đáy phủ gai 16 ô, có một kệ đá cao.
  - Mái tầng 2 ở y 16, nằm ngoài trời nên dính mưa.
- **Địch:** 1 Brute đầu điện, 1 Sniper cuối điện.
- **Vật phẩm:** Reploid #3 giữa điện.
- **Lối phụ (Capsule Shadow Body):**
  - Đá tường cột đỡ mái lên **mái tầng 2**. Capsule nằm cuối mái (x ≈ 276, y ≈ 15).
  - Mái dài 26 ô ngoài trời mà chỉ có 7 giây tạnh: phải lên ngay khi vừa tạnh.
- **Lối phụ (Heart Tank):**
  - Thả xuống lỗ sàn, lướt-nhảy qua bãi gai tới kệ đá. Heart Tank trên kệ (x ≈ 275, y ≈ 31).
  - Giáp Shadow miễn gai nên đi bộ qua được.
- **Cổng ác mộng:** cuối hầm có cổng dịch chuyển sang lối thay thế đấu Nightmare Zero (theo dữ liệu game). Thoát hầm bằng cửa phải.'''),

 Room('R6', 'Hồ axit', 290, O + 0, 64, 18, 7, [
   F((0, 12), (8, 12)), F((56, 12), (64, 12)), H('acid', 8, 13, 48, 5), Z('rain', 0, 0, 64, 12, 'mưa 4s / tạnh 5s'),
   P(12, 12, 4, 'move'), P(22, 11, 4, 'move'), P(32, 12, 4, 'move'), P(42, 11, 4, 'move'), P(50, 12, 4, 'move'),
   B(21, 7, 6, 1), B(41, 7, 6, 1), X(10, 15, 'đá sen chìm 1s sau khi đứng'), E('D', 28, 4), E('D', 50, 4),
   PATH((1, 11), (8, 11), (14, 11), (24, 10), (34, 11), (44, 10), (52, 11), (63, 11))], '''
- **Mục đích:** cao trào của màn. Vượt hồ axit trên các phiến đá sen đang chìm, trong mưa dày hơn.
- **Địa hình:** hồ axit rộng 48 ô. Rơi xuống axit là mất mạng.
- **Cơ chế:**
  - **5 phiến đá sen** trôi nhẹ. Đứng lên thì 1 giây sau phiến chìm dần, 2 giây sau chìm hẳn rồi nổi lại sau 3 giây.
  - Mưa dày hơn: **mưa 4 giây, tạnh 5 giây**.
  - Chỉ có 2 mái che nhỏ trên phiến thứ hai và thứ tư. Trú ở đó thì phiến lại chìm.
  - Người chơi phải tính: chờ mưa trên phiến có mái nhưng không được đứng quá 2 giây.
- **Địch:** 2 Drone bay sát mặt hồ, bắn chéo lên.
- **Giáp hỗ trợ:** Shadow nhảy cao hơn; Blade lướt trên không xa hơn.'''),

 Room('R7', 'Điện thờ trong', 354, O + 2, 52, 14, 6, [
   B(0, 0, 52, 2), F((0, 10), (52, 10)), H('spike', 14, 9, 6, 1), H('spike', 32, 9, 6, 1), P(14, 6, 6, 'break'), P(32, 6, 6, 'break'),
   E('C', 2, 9), E('S', 46, 9), E('D', 26, 4), PATH((1, 9), (13, 9), (15, 5), (20, 9), (31, 9), (33, 5), (38, 9), (51, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp sau đoạn cao trào: gai sàn và sàn gỗ mục, không còn mưa (trong nhà).
- **Địa hình:** điện thờ 52 ô, 2 hố gai 6 ô. Trên mỗi hố là một tấm **ván gỗ mục**, đứng 0.5 giây thì gãy.
- **Địch:** 1 Drone giữa điện, 1 Sniper cuối điện.'''),

 rest('R8', 'Bậc đá', 406, O + 2, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Rainy Turtloid', 436, O + -2, 32, 18, 6, arena(32, 16, 14) + [
   Z('rain', 2, 1, 28, 13, 'pha 2: mưa liên tục'), B(4, 5, 6, 1), B(22, 5, 6, 1), E('*', 18, 9)], '''
- **Đấu trường 28 ô**, có 2 mái che nhỏ trên cao (đá tường lên được).
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Meteor Rain, xoay mai, bắn giọt).
- **Pha 2** (dưới 50% HP):
  - **Mưa axit liên tục**, chỉ tạnh 2 giây khi Turtloid rụt vào mai.
  - Người chơi phải đánh từ dưới mái che, hoặc chịu mất máu để tấn công.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Đền Inami', en='Inami Temple', boss='Rainy Turtloid', act='Act II · X6', theme=THEME, capsule='Shadow Body',
 subtitle='Area 1 (sân và tháp đền): R1 → R2 (mái che) → R3 (leo tháp) → R4 (công tắc cổng) → Mini-boss  |  Area 2 (trong đền): R5 (3 tầng) → R6 (hồ axit) → R7 → R8 → Boss',
 keep='Boss, capsule Shadow Body, mưa axit, mái che, 2 công tắc mở cổng và cổng dịch chuyển lối Nightmare Zero vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Ngôi đền cổ trên núi bị mây axit bao phủ. Cả màn là **trò chơi với nhịp mưa**: mỗi đợt tạnh là một cửa sổ thời gian để chạy, leo hoặc lấy bí mật.',
 areas=['**Area 1 – Sân và tháp đền (ngoài trời):** đá rêu, mây xanh lục. Dạy mưa axit, mái che, leo tháp trong mưa, bắn công tắc cổng.',
        '**Area 2 – Chính điện và hồ:** gỗ son, đèn lồng. Phòng 3 tầng có bí mật, hồ axit với đá sen chìm, điện thờ có ván mục.'],
 flow='trú mưa → chạy giữa mái che → leo tháp thủng mái → bắn công tắc mở cổng → mini-boss rùa đá → chọn tầng trong chính điện → vượt hồ axit → boss mưa liên tục',
 time='khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X6, màn Rainy Turtloid:** đền cổ, mưa axit định kỳ, mái che, capsule Shadow trên mái, cổng sang Nightmare Zero.',
       '**X4, màn Split Mushroom / X8, màn Dark Mantis:** cơ chế môi trường theo nhịp có báo trước.',
       '**X5, màn Spike Rosered:** bí mật nằm ở tầng khác với đường chính, chia phòng thành nhiều tầng.',
       '**X Corrupted:** buộc người chơi đánh đổi giữa an toàn (trú mưa) và tiến độ (đá sen chìm).'],
 engine=['Mưa axit theo nhịp, có báo trước; vùng mái che chặn mưa.',
         'Cổng mở bằng công tắc (vĩnh viễn).',
         'Phiến đá sen chìm khi đứng và nổi lại sau thời gian.',
         'Ván gỗ mục (sàn vỡ 0.5 giây).',
         'Cổng dịch chuyển sang lối Nightmare Zero (giữ theo dữ liệu game).',
         'Mini-boss Rùa đá canh đền: mai phản đạn thường.'],
 art=['**Tileset "Sân đền" (Area 1):** 47 ô viền đá rêu, mái ngói, cổng gỗ (2 trạng thái).',
      '**Tileset "Chính điện" (Area 2):** 47 ô viền gỗ son, ván mục (3 khung), hầm đá.',
      '**Vật thể:** hạt mưa axit (lớp phủ toàn màn hình, 4 khung), đá sen (3 khung chìm), đèn lồng, công tắc.',
      '**Nền:** Area 1: núi mây axit xanh lục (2 lớp parallax). Area 2: hành lang đền và tượng (2 lớp).'],
)
STAGE['rooms'] = rooms
