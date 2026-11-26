from kit import *

THEME = dict(bg1=(24, 22, 36), bg2=(30, 20, 40), rock1=(80, 74, 104), rock2=(90, 70, 110))
s5, p5 = shaft_up(24, 46, n=5)

rooms = [
 Room('R1', 'Hành lang nhiễu', 0, 40, 44, 14, 3, [
   B(0, 0, 44, 2), F((0, 10), (44, 10)), Z('dark', 4, 2, 36, 8, 'nhiễu tối: tầm nhìn 8 ô quanh X'), E('R', 6, 9), E('S', 40, 9), E('D', 24, 5),
   PATH((1, 9), (43, 9))], '''
- **Mục đích:** vào không gian ác mộng nơi Nightmare Zero chờ. Màn hình nhiễu, **chỉ thấy rõ trong 8 ô quanh X**.
- **Địa hình:** hành lang 44 ô, trần ở y 42, sàn ở y 50.
- **Địch:** 1 Drone, 1 Sniper (chỉ thấy đèn mắt khi ở xa).
- **Vật phẩm:** Reploid #1 ở đầu hành lang.
- **Ghi chú:** đánh bại Nightmare Zero thì Zero thật được giải cứu và mở cho các tầng Gate Lab (theo dữ liệu game). Không có capsule/Heart Tank/Sub-Tank.'''),

 Room('R2', 'Đèn quét ảo ảnh', 44, 40, 64, 18, 5, [
   F((0, 10), (6, 10)), F((58, 10), (64, 10)), H('void', 6, 16, 52, 2), Z('alarm', 20, 0, 6, 16, 'đèn quét'), AR(23, 2, 6, 0, 'alarm'),
   P(10, 10, 4), P(18, 8, 4, 'holo'), P(26, 11, 4), P(32, 8, 4, 'holo'), P(40, 10, 4, 'holo'), P(48, 7, 4), P(52, 11, 4, 'holo'),
   X(8, 12.6, 'kệ đặc = ảo ảnh (biến mất trong đèn)'), X(8, 14.8, 'kệ viền = thật (chỉ hiện trong đèn)'), E('D', 36, 3),
   PATH((1, 9), (6, 9), (12, 9), (20, 7), (34, 7), (42, 9), (54, 10), (59, 9), (63.5, 9))], '''
- **Mục đích:** giới thiệu **đèn quét ảo ảnh**: thứ thấy được chưa chắc là thật.
- **Địa hình:** vực rộng 52 ô, hai mép đá ở hai đầu.
- **Cơ chế:**
  - Có 2 loại bệ. **Bệ ảo ảnh** hiện rõ trong bóng tối nhưng **biến mất khi đèn quét chiếu vào**. **Bệ thật** vô hình trong bóng tối và **chỉ hiện khi được đèn chiếu**.
  - Đèn quét qua lại trên vực, 70px/giây. Người chơi đi theo vệt đèn để thấy và đứng trên bệ thật.
  - Đứng trên bệ ảo ảnh lúc đèn quét tới là rơi.
- **Địch:** 1 Drone.'''),

 Room('R3', 'Bệ nhấp nháy', 108, 40, 56, 18, 5, [
   F((0, 10), (6, 10)), F((50, 10), (56, 10)), H('void', 6, 16, 44, 2), P(10, 10, 4, 'holo'), P(18, 8, 4, 'holoB'), P(26, 10, 4, 'holo'), P(34, 7, 4, 'holoB'), P(42, 9, 4, 'holo'),
   Z('dark', 6, 0, 44, 16, ''), E('R', 52, 9), E('D', 30, 3), PATH((1, 9), (6, 9), (12, 9), (20, 7), (28, 9), (36, 6), (44, 8), (51, 9), (55.5, 9))], '''
- **Mục đích:** bệ 2 pha (như Zero Space 2) trong bóng tối nhiễu.
- **Địa hình:** vực 44 ô, 5 bệ xen kẽ pha A/B, nhịp 2 giây.
- **Cơ chế:** vì tầm nhìn chỉ 8 ô, người chơi không thấy hết chuỗi bệ. Âm thanh "tách" khi đổi pha giúp đếm nhịp.
- **Địch:** 1 Drone.
- **Vật phẩm:** Reploid #2 ở mép bên kia.'''),

 Room('MID', 'Bóng ma X', 164, 36, 30, 16, 6, arena(30, 16, 14) + [E('M', 20, 9), X(4, 4, 'bản sao bắt chước X')], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Bóng ma X** là bản sao Nightmare của X, **lặp lại động tác của người chơi** sau 1 giây.
- **Đòn đánh:** bắn, lướt, nhảy, đá tường giống hệt những gì người chơi vừa làm 1 giây trước.
- **Điểm yếu:** đứng yên thì nó cũng đứng yên, bắn vào nó lúc đó. Nạp đạn đầy thì nó cũng nạp: phải bắn trước.
- **Phần thưởng:** mở vùng đảo trọng lực. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Vùng đảo trọng lực', 194, 36, 60, 22, 6, [
   F((0, 14), (8, 14)), F((52, 14), (60, 14)), B(8, 2, 44, 2), H('spike', 8, 20, 44, 2), Z('grav', 8, 4, 44, 16, ''),
   P(10, 13.6, 3, 'bounce'), P(24, 4, 3, 'bounce'), P(36, 13.6, 3, 'bounce'), P(46, 4, 3, 'bounce'), X(10, 17, 'đệm đảo chiều'),
   E('C', 2, 13), E('B', 30, 4.6), E('S', 56, 13), E('R', 44, 13),
   PATH((1, 13), (11, 13), (14, 5), (25, 5), (30, 13), (37, 13), (40, 5), (47, 5), (52, 13), (59, 13))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đảo trọng lực bằng **đệm đảo chiều** (khác công tắc ở Zero Space 3).
- **Địa hình:** khoảng trống 44 ô, sàn là gai, trần liền.
- **Cơ chế:** dẫm lên **đệm đảo chiều** thì trọng lực lật ngược ngay lập tức. 4 đệm xen kẽ trên sàn và trên trần, người chơi đi zigzag giữa sàn và trần.
- **Địch:** 1 Brute đứng lộn ngược trên trần, 1 Sniper cuối phòng.
- **Vật phẩm:** Reploid #3 trên sàn gần cuối (khúc không có gai).'''),

 Room('R5', 'Giếng hai chiều', 254, 6, 24, 46, 8, s5 + [Z('grav', 2, 1, 20, 41, 'trọng lực đảo mỗi 4s'), Z('dark', 2, 18, 20, 12, ''), E('D', 8, 14), E('D', 16, 32), p5], '''
- **Mục đích:** cao trào của màn. Leo giếng trong khi **trọng lực tự đảo mỗi 4 giây** và nửa giữa giếng bị nhiễu tối.
- **Địa hình:** giếng rộng 20 ô, cao 42 ô (từ y 50 lên y 13). 5 kệ.
- **Cơ chế:**
  - Lúc trọng lực ngược, người chơi "rơi" lên. Đó là lúc leo nhanh nhất, nhưng phải dừng lại kịp trên mặt dưới của kệ.
  - Lúc trọng lực thường, bám vách hoặc đứng trên mặt trên của kệ để không rơi mất độ cao.
  - Nửa giữa giếng tối: chỉ thấy 8 ô quanh X.
- **Địch:** 2 Drone, miễn đảo trọng lực.'''),

 Room('R6', 'Trạm cuối', 278, 3, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('C', 2, 9), E('R', 15, 9), X(4, 5, 'năng lượng LỚN'), PATH((1, 9), (28, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn**, cửa boss.'''),

 Room('BOSS', 'Nightmare Zero', 308, -1, 32, 16, 7, arena(32, 16, 14) + [Z('dark', 2, 1, 28, 13, 'pha 2: nhiễu tối'), E('*', 20, 9)], '''
- **Đấu trường 28 ô**, kín, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (chém kiếm, Shippuuga, Genmu Zero).
- **Pha 2** (dưới 50% HP):
  - **Nhiễu tối toàn sân**, chỉ thấy 8 ô quanh X. Nightmare Zero lướt vào từ ngoài vùng sáng; đôi mắt đỏ của nó hiện trước 0.5 giây.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Không gian ác mộng', en='Nightmare Space', boss='Nightmare Zero', act='Pháo đài X6', theme=THEME, capsule='',
 subtitle='Area 1: R1 (nhiễu tối) → R2 (đèn ảo ảnh) → R3 (bệ nhấp nháy) → Mini-boss Bóng ma X  |  Area 2: R4 (đệm đảo chiều) → R5 (giếng hai chiều) → R6 trạm → Boss',
 keep='Boss Nightmare Zero, màn tối nhiễu, đèn quét ảo ảnh, bệ Cyber nhấp nháy và vùng đảo trọng lực vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.',
 concept='Không gian ác mộng tạo từ ký ức của Zero. Cả màn đánh vào **sự tin tưởng vào mắt nhìn**: tối nhiễu, bệ ảo ảnh, bản sao bắt chước, trọng lực lật ngược.',
 areas=['**Area 1 – Hành lang ác mộng:** đen tím nhiễu, đèn quét trắng. Tầm nhìn hẹp, bệ thật/ảo, bệ nhấp nháy.',
        '**Area 2 – Không gian lộn ngược:** đỏ thẫm. Đệm đảo chiều trên sàn gai, giếng tự đảo trọng lực.'],
 flow='đi trong nhiễu tối → theo vệt đèn tìm bệ thật → đếm nhịp bệ trong bóng tối → đánh bản sao chính mình → đi zigzag sàn-trần → leo giếng hai chiều → Nightmare Zero',
 time='khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen',
 refs=['**X6, Nightmare Space / màn Nightmare Zero:** tối nhiễu, đèn quét ảo ảnh, bệ nhấp nháy, đảo trọng lực.',
       '**X6, màn Gate Lab:** đổi luật vật lý liên tục.',
       '**X8, màn Dark Mantis:** tầm nhìn bị giới hạn.',
       '**X Corrupted:** bệ thật/ảo chỉ phân biệt được bằng một cơ chế khác (đèn quét).'],
 engine=['Vùng tối nhiễu (tầm nhìn bán kính 8 ô quanh X).',
         'Bệ ảo ảnh và bệ thật phản ứng ngược nhau với vệt đèn quét.',
         'Bệ 2 pha có âm báo đổi pha.',
         'Đệm đảo chiều (dẫm lên thì lật trọng lực); vùng trọng lực tự đảo theo nhịp.',
         'Mini-boss Bóng ma X lặp lại đầu vào của người chơi với độ trễ 1 giây.'],
 art=['**Tileset "Ác mộng":** 47 ô viền đen tím nhiễu, bệ thật (viền sáng) và bệ ảo ảnh (đặc), đệm đảo chiều.',
      '**Vật thể:** đèn quét (vệt sáng 3 khung), bóng ma X (bảng màu tối của sprite X), hiệu ứng nhiễu (lớp phủ).',
      '**Nền:** mảnh ký ức trôi, hình bóng Zero mờ (2 lớp parallax).'],
)
for r in rooms:
    r['y'] += 4
STAGE['rooms'] = rooms
