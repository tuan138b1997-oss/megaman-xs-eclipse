from kit import *

THEME = dict(bg1=(44, 28, 48), bg2=(38, 24, 44), rock1=(116, 96, 126), rock2=(104, 86, 120))


def small(x, y, w=2): return P(x, y, w)


rooms = [
 Room('R1', 'Mép vực gai', 0, 40, 40, 18, 4, [
   F((0, 12), (30, 12)), H('spike', 30, 16, 10, 2), small(34, 11), E('R', 4, 11), E('S', 24, 11),
   X(30, 14.6, 'vực gai'), PATH((1, 11), (29, 11), (35, 10), (39.5, 10))], '''
- **Mục đích:** tầng 2 phòng thí nghiệm Gate: thử thách **nhảy chính xác** khó nhất game bắt đầu.
- **Địa hình:** mỏm sàn 30 ô, sau đó là **vực gai** kéo dài gần hết màn.
- **Địch:** 1 Sniper ở mép vực.
- **Vật phẩm:** Reploid #1 ở đầu mỏm.
- **Ghi chú:** dữ liệu game khuyên dùng Charge Saber của Blade Armor để làm choáng giáp High Max. Không có capsule/Heart Tank/Sub-Tank.'''),

 Room('R2', 'Chuỗi bệ nhỏ 1', 40, 36, 64, 22, 6, [
   H('spike', 0, 20, 64, 2), small(4, 15), small(14, 12), small(24, 14), small(34, 10), small(44, 13), small(54, 11), B(60, 14, 4, 1),
   X(4, 18, 'bệ 2 ô, cách 10 ô'), E('D', 28, 4), E('D', 50, 5), PATH((1, 14), (5, 14), (15, 11), (25, 13), (35, 9), (45, 12), (55, 10), (61, 13), (63.5, 13))], '''
- **Mục đích:** chuỗi **bệ nhỏ 2 ô** cách nhau 10 ô trên vực gai.
- **Cơ chế:** khoảng cách 10 ô vừa đủ cho một cú lướt-nhảy. Nhảy thường không tới.
- **Địch:** 2 Drone ở khoảng giữa các bệ: bị bắn trúng là rơi. Hạ chúng từ bệ trước rồi mới nhảy.'''),

 Room('R3', 'Laser quét dọc', 104, 36, 60, 22, 6, [
   H('spike', 0, 20, 60, 2), B(0, 14, 2, 1), small(8, 14), small(18, 11), small(28, 13), small(38, 10), small(48, 12), B(56, 14, 4, 1),
   BAR(14, 1, 0.8, 19, 'laser'), BAR(40, 1, 0.8, 19, 'laser'), AR(15, 3, 6, 0, 'alarm'), AR(41, 3, -6, 0, 'alarm'),
   X(16, 1, 'tia dọc chạy ngang 80px/s'), E('R', 29, 12), E('D', 44, 4), PATH((1, 13), (9, 13), (19, 10), (29, 12), (39, 9), (49, 11), (57, 13), (59.5, 13))], '''
- **Mục đích:** bệ nhỏ cộng **tia laser dọc chạy ngang**.
- **Cơ chế:** 2 tia laser cao hết phòng chạy qua lại ngược chiều nhau, 80px/giây. Tia đi qua bệ nào thì bệ đó không đứng được lúc ấy. Phải nhảy theo khoảng trống giữa hai tia.
- **Địch:** 1 Drone.
- **Vật phẩm:** Reploid #2 trên bệ thứ ba.'''),

 Room('MID', 'Khối giáp Nightmare', 164, 36, 32, 20, 6, [
   H('spike', 0, 18, 32, 2), B(2, 12, 8, 1), B(12, 9, 8, 1), B(22, 12, 8, 1), E('M', 16, 4), X(2, 15, 'ba bệ trên vực gai'), PATH((3, 11), (16, 8), (29, 11), (31.5, 11))], '''
- **Đấu trường là 3 bệ** trên vực gai.
- **Khối giáp Nightmare** là phiên bản nhỏ của High Max, giáp bất khả xâm phạm.
- **Đòn đánh:**
  - Bắn quả cầu năng lượng chậm, nảy giữa các bệ.
  - Dịch chuyển sang bệ khác và đập xuống bệ đó (bệ rung, người đứng trên bị nảy lên).
- **Điểm yếu:** chỉ nhận sát thương sau khi bị **làm choáng** bằng đạn nạp đầy hoặc Charge Saber. Đây là bài học trước trận High Max.
- **Phần thưởng:** mở khu totem. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Bệ totem', 196, 36, 60, 22, 7, [
   H('spike', 0, 20, 60, 2), B(0, 14, 4, 1), small(10, 14, 4), small(22, 11, 4), small(34, 13, 4), small(46, 10, 4), B(56, 14, 4, 1),
   BAR(23, 4, 2, 7, 'trash'), BAR(47, 3, 2, 7, 'trash'), X(20, 2.5, 'totem trồi chặn bệ 2s / thụt 2s'),
   E('C', 2, 13), E('S', 35, 12), E('R', 58, 13), PATH((1, 13), (12, 13), (24, 10), (36, 12), (48, 9), (57, 13), (59.5, 13))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** **cột totem chặn bệ**: totem trồi lên ngay trên bệ nhảy.
- **Cơ chế:** 2 bệ có totem. Totem trồi chiếm hết bệ 2 giây, thụt 2 giây. Đáp lên bệ lúc totem sắp trồi là bị hất văng.
- **Địch:** 1 Sniper đứng trên bệ không có totem.
- **Vật phẩm:** Reploid #3 ở mỏm bên kia.'''),

 Room('R5', 'Chuỗi bệ nhỏ 2', 256, 36, 70, 22, 8, [
   H('spike', 0, 20, 70, 2), B(0, 14, 4, 1), small(10, 13), small(20, 10), small(30, 13, 4), small(40, 9), small(50, 12), small(60, 10), B(66, 14, 4, 1),
   BAR(25, 1, 0.8, 19, 'laser'), BAR(31, 4, 2, 9, 'trash'), BAR(55, 1, 0.8, 19, 'laser'), E('D', 16, 4), E('D', 46, 4),
   PATH((1, 13), (11, 12), (21, 9), (32, 12), (41, 8), (51, 11), (61, 9), (67, 13), (69.5, 13))], '''
- **Mục đích:** cao trào của màn. Ghép tất cả: bệ 2 ô, laser chạy ngang, totem chặn bệ, Drone.
- **Địa hình:** vực gai 70 ô, 6 bệ nhỏ.
- **Cơ chế:** 2 tia laser dọc, 1 totem trên bệ giữa. Nhịp của laser và totem không khớp nhau.
- **Địch:** 2 Drone.
- **Giáp hỗ trợ:** Shadow miễn gai nên rơi xuống vực không mất mạng (vẫn phải leo lên). Ultimate lướt Nova Strike xuyên totem.'''),

 Room('R6', 'Trạm nghỉ', 326, 40, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('C', 2, 9), E('R', 15, 9), X(4, 5, 'năng lượng LỚN'), PATH((1, 9), (28, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn**, cửa boss.'''),

 Room('BOSS', 'High Max', 356, 36, 32, 16, 7, arena(32, 16, 14) + [E('*', 20, 8), X(4, 4, 'pha 2: 4 khối giáp bay quanh')], '''
- **Đấu trường 28 ô**, kín, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (giáp bất khả xâm phạm, cầu năng lượng, dịch chuyển). Phải làm choáng bằng Charge Saber/đạn nạp đầy rồi mới gây sát thương (theo dữ liệu game).
- **Pha 2** (dưới 50% HP):
  - **4 khối giáp** bay quanh High Max, chặn đạn. Một khối bị phá thì 4 giây sau mọc lại.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Phòng thí nghiệm Gate 2', en="Gate's Secret Lab 2", boss='High Max', act='Pháo đài X6', theme=THEME, capsule='',
 subtitle='Area 1: R1 → R2 (bệ nhỏ) → R3 (laser dọc) → Mini-boss khối giáp  |  Area 2: R4 (totem chặn bệ) → R5 (tổng hợp) → R6 trạm → Boss',
 keep='Boss High Max, vực gai toàn khu, chuỗi bệ nhỏ lơ lửng, 2 cột totem chặn bệ và tia laser quét dọc vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.',
 concept='Tầng 2 phòng thí nghiệm Gate: **màn nhảy chính xác** khó nhất. Gần như toàn màn là vực gai với bệ chỉ rộng 2 ô.',
 areas=['**Area 1 – Vực gai trên:** bệ nhỏ, laser dọc chạy ngang.',
        '**Area 2 – Vực gai dưới:** totem trồi chặn bệ, rồi đoạn tổng hợp mọi thứ.'],
 flow='lướt-nhảy giữa bệ 2 ô → canh khe giữa 2 tia laser → làm choáng khối giáp → né totem trồi → đoạn tổng hợp → High Max',
 time='khoảng 5–7 phút lần đầu (nhiều lần chết), khoảng 2.5 phút khi đã quen',
 refs=['**X6, Gate Lab 2:** vực gai, 10 bệ nhỏ, 2 totem chặn bệ, laser quét dọc, High Max cần Charge Saber.',
       '**X (SNES), màn Sigma 2:** chuỗi bệ nhỏ trên gai.',
       '**X6, màn Ground Scaravich:** totem trồi/thụt.',
       '**X Corrupted:** mini-boss dạy trước cách hạ boss (làm choáng rồi mới đánh).'],
 engine=['Bệ nhỏ 2 ô; vực gai toàn màn.',
         'Tia laser dọc chạy ngang.',
         'Totem trồi/thụt trên bệ, hất văng người chơi.',
         'Trạng thái "giáp bất khả xâm phạm" chỉ hở khi bị làm choáng.',
         'Mini-boss Khối giáp Nightmare.'],
 art=['**Tileset "Gate Lab 2":** 47 ô viền tím, bệ nhỏ 2 ô, vực gai.',
      '**Vật thể:** tia laser dọc (3 khung), totem (3 khung trồi), khối giáp bay.',
      '**Nền:** hành lang phòng thí nghiệm tím và ống năng lượng (2 lớp parallax).'],
)
STAGE['rooms'] = rooms
