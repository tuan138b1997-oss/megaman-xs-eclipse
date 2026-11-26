from kit import *

THEME = dict(bg1=(52, 24, 36), bg2=(40, 22, 40), rock1=(130, 90, 104), rock2=(118, 86, 110))
s2, p2 = shaft_down(24, 46, n=4)

rooms = [
 Room('R1', 'Hành lang bẫy gai', 0, 40, 64, 14, 5, [
   B(0, 0, 64, 2), H('spike', 20, 2, 10, 1), F((0, 10), (64, 10)), CV(6, 9.4, 18, 1), H('spike', 24, 9, 4, 1), CV(34, 9.4, 18, 1), H('spike', 52, 9, 4, 1),
   E('R', 3, 9), E('S', 60, 9), E('D', 40, 5), PATH((1, 9), (23, 9), (26, 6), (29, 9), (51, 9), (54, 6), (57, 9), (63, 9))], '''
- **Mục đích:** màn cuối cùng. Mở đầu bằng **băng chuyền đẩy vào gai**, có trần gai thấp ở chỗ phải nhảy.
- **Địa hình:** hành lang 64 ô, 2 băng chuyền xuôi chiều (110px/giây), mỗi băng chuyền kết thúc bằng một hố gai.
- **Cơ chế:** băng chuyền làm cú nhảy dài hơn. Ở hố gai đầu có trần gai ngay trên: nhảy hết lực là trúng.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #1 ở đầu hành lang.
- **Ghi chú:** dữ liệu game khuyên dùng Ultimate Armor hoặc Black Zero. Không có capsule/Heart Tank/Sub-Tank.'''),

 Room('R2', 'Trục rơi bẫy gai', 64, 40, 24, 46, 6, s2 + [
   H('spike', 2, 18, 1.5, 4), H('spike', 20.5, 26, 1.5, 4), H('spike', 2, 34, 1.5, 4), X(3, 16.5, 'gai thò ra 1s / 2s'), E('D', 12, 22), p2], '''
- **Mục đích:** đi xuống trục có **gai thò ra từ vách** theo nhịp.
- **Địa hình:** trục rộng 20 ô, sâu 36 ô (từ y 50 xuống y 84). 4 kệ zigzag.
- **Cơ chế:** 3 mảng gai trên vách thò ra 3 ô trong 1 giây, thụt 2 giây. Rơi ngang qua lúc gai thò là mất mạng.
- **Địch:** 1 Drone.'''),

 Room('R3', 'Bệ di chuyển', 88, 70, 60, 18, 6, [
   F((0, 14), (6, 14)), F((54, 14), (60, 14)), H('spike', 6, 16, 48, 2), P(10, 12, 5, 'move'), P(22, 9, 5, 'move'), P(34, 12, 5, 'move'), P(44, 8, 5, 'move'),
   H('spike', 0, 0, 60, 1), E('B', 3, 13), E('R', 57, 13), E('D', 30, 4), PATH((1, 13), (6, 13), (12, 11), (24, 8), (36, 11), (46, 7), (55, 13), (59.5, 13))], '''
- **Mục đích:** bệ di động trên gai, dưới trần gai.
- **Địa hình:** hố gai 48 ô, trần gai. 4 bệ chạy ngang và chéo.
- **Địch:** 1 Brute đứng chặn ngay mép đầu, 1 Drone.
- **Vật phẩm:** Reploid #2 ở mép bên kia.'''),

 Room('MID', 'Cảnh vệ cuối', 148, 70, 30, 16, 6, arena(30, 16, 14) + [E('M', 15, 6), X(4, 10, 'ghép từ mảnh 8 boss')], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Cảnh vệ cuối** là cỗ máy ghép từ mảnh của 8 boss, đổi đòn theo từng 1/4 máu:
  - 100–75%: mưa giọt (Turtloid). 75–50%: khiên phản đạn (Sheldon).
  - 50–25%: lăn cầu đất (Scaravich). 25–0%: lao lửa (Heatnix).
- **Điểm yếu:** vũ khí khắc chế đúng đòn đang dùng gây sát thương gấp đôi.
- **Phần thưởng:** mở Trung tâm 8 cổng. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Trung tâm 8 cổng', 178, 64, 64, 22, 7, [
   F((0, 20), (64, 20)), B(0, 0, 64, 1), B(10, 10, 44, 1), P(4, 14, 5), P(55, 14, 5), BAR(62, 1, 2, 19, 'door'),
   E('G', 8, 19), E('G', 20, 19), E('G', 44, 19), E('G', 56, 19), E('G', 14, 9), E('G', 26, 9), E('G', 38, 9), E('G', 50, 9),
   E('C', 2, 19), E('R', 32, 19), X(20, 3, '8 cổng → 8 trận đấu lại'), X(50, 21.4, 'cửa mở khi đủ 8'),
   PATH((1, 19), (6, 13), (12, 9.6), (52, 9.6), (58, 13), (61.5, 19))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** **boss rush**: đấu lại 8 boss Act II (theo dữ liệu game).
- **Địa hình:** sảnh 2 tầng. 4 cổng ở tầng dưới, 4 cổng trên ban công tầng trên.
- **Cơ chế:**
  - Mỗi cổng dẫn tới đấu trường của một boss: Rainy Turtloid, Shield Sheldon, Infinity Mijinion, Commander Yammark, Metal Shark Player, Blaze Heatnix, Blizzard Wolfang, Ground Scaravich.
  - Đánh xong thì trở về sảnh, cổng đó tắt sáng. Chọn thứ tự tùy ý.
  - Đấu trường trong boss rush là **bản pha 2** của mỗi boss (cơ chế môi trường đã thiết kế ở từng màn), nhưng máu boss chỉ còn 60%.
  - Đủ 8 trận thì cửa cuối sảnh mở.
- **Vật phẩm:** Reploid #3 giữa sảnh.'''),

 Room('R5', 'Trạm hồi máu', 242, 74, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('C', 2, 9), E('R', 15, 9), X(4, 5, 'hồi máu ĐẦY'), PATH((1, 9), (28, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Hồi máu giữa trận** (theo dữ liệu game): Reploid #4, hồi đầy máu và năng lượng vũ khí.'''),

 Room('R6', 'Cầu thang Sigma', 272, 52, 56, 32, 8, [
   F((0, 32), (0, 32)), B(0, 30, 8, 2), P(10, 27, 6, 'break'), P(18, 23, 6, 'break'), P(26, 19, 6, 'break'), P(34, 15, 6, 'break'), P(42, 11, 6, 'break'), B(50, 8, 6, 24),
   H('void', 8, 30, 42, 2), AR(4, 26, 6, -3, 'alarm'), X(10, 30.4, 'bậc sụp 0.6s, sụp đuổi từ dưới lên'), E('D', 22, 10), E('D', 38, 6), E('S', 52, 7),
   PATH((1, 29), (8, 29), (13, 26), (21, 22), (29, 18), (37, 14), (45, 10), (51, 7), (55.5, 7))], '''
- **Mục đích:** cao trào cuối cùng. **Cầu thang dẫn lên cửa Hell Sigma sụp dần** phía sau người chơi.
- **Địa hình:** 5 bậc thang lơ lửng đi lên, rộng 6 ô, mỗi bậc cao hơn 4 ô.
- **Cơ chế:**
  - Đứng lên bậc nào thì bậc đó sụp sau 0.6 giây.
  - Ngoài ra, các bậc **sụp lần lượt từ dưới lên** mỗi 1.5 giây kể từ khi bước vào phòng, dù có đứng hay không.
  - Vực không đáy bên dưới.
- **Địch:** 2 Drone chắn ngang đường nhảy, 1 Sniper trên chiếu nghỉ cuối.'''),

 Room('BOSS', 'Hell Sigma', 328, 54, 34, 18, 8, [
   F((0, 6), (34, 6)), H('void', 0, 14, 34, 4), B(0, 6, 34, 8), E('*', 24, 2), X(3, 9, 'pha 2: sàn vỡ từ hai mép vào'), PATH((1, 5), (33, 5))], '''
- **Đấu trường 34 ô** trên đỉnh tháp, không vách.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (Hell Sigma khổng lồ, tay kiếm, tia).
- **Pha 2** (dưới 50% HP):
  - **Sàn vỡ dần từ hai mép vào**, mỗi 12 giây mất 2 ô mỗi bên, tối đa còn 18 ô.
  - Tay của Sigma bám vào mép sàn còn lại và đập.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Phòng thí nghiệm cuối', en='Final Lab', boss='8 boss → Hell Sigma', act='Pháo đài X6', theme=THEME, capsule='',
 subtitle='Area 1: R1 (băng chuyền gai) → R2 (trục rơi, gai thò) → R3 (bệ di chuyển) → Mini-boss  |  Area 2: R4 (trung tâm 8 cổng, boss rush) → R5 hồi máu → R6 (cầu thang sụp) → Hell Sigma',
 keep='Boss Hell Sigma, hành lang bẫy gai và băng chuyền, trục rơi, bệ di chuyển, Trung tâm 8 cổng dịch chuyển boss rush và hồi máu giữa trận vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss.',
 concept='Màn cuối cùng của chiến dịch. Đoạn đầu là bẫy gai kiểu pháo đài cổ điển, giữa là **boss rush 8 cổng**, cuối là **cầu thang sụp** dẫn lên Hell Sigma.',
 areas=['**Area 1 – Hầm bẫy:** đỏ đen, gai khắp nơi. Băng chuyền gai, trục rơi gai thò, bệ dưới trần gai.',
        '**Area 2 – Đỉnh tháp:** sảnh 8 cổng, trạm hồi máu, cầu thang sụp, đấu trường trên đỉnh.'],
 flow='băng chuyền đẩy vào gai → rơi qua trục gai thò → bệ dưới trần gai → cảnh vệ ghép 8 boss → boss rush 8 cổng → hồi máu → chạy lên cầu thang sụp → Hell Sigma',
 time='khoảng 12–15 phút lần đầu (gồm boss rush), khoảng 7 phút khi đã quen',
 refs=['**X6, Final Lab:** hành lang bẫy gai, băng chuyền, trung tâm 8 cổng boss rush, hồi máu, Hell Sigma.',
       '**X (SNES) / X2, pháo đài Sigma:** sảnh dịch chuyển boss rush.',
       '**X8, màn Jakob Elevator:** đoạn đi lên trước trận cuối.',
       '**X Corrupted:** boss rush dùng lại cơ chế môi trường của từng màn.'],
 engine=['Băng chuyền và trần gai; gai thò từ vách theo nhịp.',
         'Sảnh 8 cổng: theo dõi boss đã hạ, mở cửa khi đủ 8; đấu trường boss rush dùng lại cơ chế pha 2 của từng màn.',
         'Bậc thang sụp khi đứng và sụp theo lịch từ dưới lên.',
         'Mini-boss Cảnh vệ cuối đổi đòn theo máu.',
         'Sàn boss vỡ dần từ hai mép.'],
 art=['**Tileset "Pháo đài cuối":** 47 ô viền đỏ đen, gai, băng chuyền, bậc thang lơ lửng (3 khung sụp).',
      '**Vật thể:** 8 cổng dịch chuyển có biểu tượng từng boss (sáng/tắt), gai thò (3 khung).',
      '**Nền:** đỉnh tháp giữa trời đỏ và hình bóng Sigma (2 lớp parallax).'],
)
STAGE['rooms'] = rooms
