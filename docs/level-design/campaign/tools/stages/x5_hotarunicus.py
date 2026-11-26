from lib import *

THEME = dict(bg1=(34, 40, 52), bg2=(28, 30, 46), rock1=(104, 112, 128), rock2=(88, 92, 116))


def laser(x, y, h): return BAR(x, y, 0.8, h, 'laser')


rooms = [
 Room('R1', 'Sảnh viện', 0, 30, 44, 14, 2, [
   B(0, 0, 44, 2), F((0, 10), (44, 10)), laser(20, 2, 8), X(15, 3, 'hàng rào laser 2s bật / 1s tắt'),
   E('S', 32, 9), E('D', 10, 5), PATH((1, 9), (43, 9))], '''
- **Mục đích:** giới thiệu **tia laser đỏ**: chạm là mất 1/4 máu và bị đẩy lùi.
- **Địa hình:** sảnh 44 ô, trần ở y 32, sàn ở y 40.
- **Bẫy:** 1 hàng rào laser chắn hết chiều cao, bật 2 giây, tắt 1 giây. Có tiếng "vù" khi sắp bật.
- **Địch:**
  - 1 Drone bay trước hàng rào.
  - 1 Sniper sau hàng rào: bắn được xuyên qua laser, nhưng người chơi thì không.
- **Trang trí:** ống nghiệm, màn hình chạy chữ, đèn trắng lạnh.'''),

 Room('R2', 'Khoang quang học 1', 44, 30, 52, 14, 3, [
   B(0, 0, 52, 2), F((0, 10), (52, 10)), B(12, 4, 2, 6), P(16, 5, 6), laser(36, 2, 8),
   X(25, 7, 'gương'), X(30, 3, 'tia chỉ tắt khi bắn công tắc'),
   E('K', 19, 4), E('R', 6, 9), E('D', 28, 4), E('S', 46, 9),
   PATH((1, 9), (11, 9), (13, 3.5), (18, 4), (24, 9), (51, 9))], '''
- **Mục đích:** dạy **công tắc quang học**: bắn vào công tắc thì tường laser liên quan tắt hẳn.
- **Địa hình:**
  - Khoang 52 ô. Tường laser đỏ ở x ≈ 80 chắn đường, **không có nhịp tắt**.
  - Công tắc nằm trên kệ cao (y 35), phía trên một cột thấp. Đá tường cột để lên.
  - Một tấm gương xoay giữa phòng hắt tia laser của Sniper đi lệch: đứng đúng chỗ thì đạn địch bật lại phía nó.
- **Địch:**
  - 1 Drone canh kệ công tắc.
  - 1 Sniper sau tường laser.
- **Vật phẩm:** Reploid #1 ở đầu khoang.'''),

 Room('R3', 'Giếng quang học', 96, 4, 20, 40, 4, [
   B(0, 0, 2, 30), B(0, 38, 20, 2), B(18, 8, 2, 30), B(2, 0, 16, 1),
   P(12, 32, 4), P(2, 26, 4), P(12, 14, 4), P(2, 8, 4), H('laser', 3, 19.7, 14, 0.6), X(4, 21, 'tia xoay 90°/giây'),
   E('D', 10, 30),
   PATH((1, 36), (9, 36), (14, 31), (4, 25), (10, 22), (14, 13), (4, 7), (12, 4), (19.5, 4))], '''
- **Mục đích:** đoạn dọc, né **tia laser xoay**.
- **Địa hình:** giếng rộng 16 ô, cao 34 ô (từ y 42 lên y 8). 4 kệ nghỉ.
- **Bẫy – tia xoay:**
  - Một đầu phát laser ở tâm giếng (y ≈ 24) phóng tia dài 7 ô, quay 90° mỗi giây.
  - Leo qua tầng giữa phải canh lúc tia nằm dọc. Đá tường sát vách thì tia không với tới được, nhưng vách đối diện thì có.
- **Địch:** 1 Drone đầu giếng.
- **Giáp hỗ trợ:** Gaea bám tường, đứng chờ tia quay qua dễ hơn.'''),

 Room('R4', 'Khoang quang học 2', 116, 0, 56, 16, 4, [
   B(0, 0, 44, 2), B(44, 0, 12, 1), B(44, 4, 12, 1), B(55, 1, 1, 3), F((0, 12), (56, 12)),
   P(10, 7, 6), B(30, 6, 4, 6), laser(22, 2, 10), laser(42, 2, 10), BAR(44, 1, 0.6, 3, 'laser'),
   E('K', 13, 6), E('K', 32, 5), E('A', 50, 3), E('R', 27, 11), E('S', 52, 11), E('B', 36, 11),
   X(45, 5.4, 'buồng kín'),
   PATH((1, 11), (11, 6), (14, 6), (21, 11), (29, 11), (31, 5), (41, 11), (55, 11)), ALT((33, 5), (40, 3), (45, 2.5), (50, 2.5))], '''
- **Mục đích:** câu đố 2 lớp laser, và capsule giáp nằm trong buồng kín.
- **Địa hình:**
  - Khoang 56 ô, 2 tường laser chắn đường (x ≈ 138 và x ≈ 158).
  - **Công tắc #1** trên kệ cao trước tường 1. **Công tắc #2** trên nóc một khối thép giữa hai tường.
  - Phía trên góc phải là **buồng kín** (x 160–172, y 1–4), cửa buồng cũng là một tia laser.
- **Cơ chế:** bắn công tắc #2 thì tắt cả tường 2 **và** cửa buồng kín, nhưng chỉ trong **5 giây**. Bắn công tắc #1 thì tường 1 tắt hẳn.
- **Địch:**
  - 1 Brute giữa hai tường.
  - 1 Sniper cuối khoang.
- **Vật phẩm:** Reploid #2 sau tường 1.
- **Lối phụ (Capsule Falcon Body):**
  - Đứng trên khối thép, bắn công tắc #2, rồi nhảy và **lướt trên không** sang trái vào buồng kín trước khi cửa laser bật lại.
  - Nhảy thường không tới, nên bắt buộc phải lướt trên không.'''),

 Room('MID', 'Mắt Laser', 172, 0, 30, 16, 5, [
   B(0, 0, 30, 2), B(0, 2, 2, 10), B(28, 2, 2, 10), F((0, 12), (30, 12)), BAR(2, 2, 26, 0.5, 'shelf'), E('M', 15, 4),
   X(4, 8, 'mắt chạy trên ray trần'), PATH((3, 11), (27, 11))], '''
- **Đấu trường 26 ô**, kín. Trần có một đường ray chạy suốt chiều ngang.
- **Mắt Laser** chạy trên ray trần.
- **Đòn đánh:**
  - Quét tia laser thẳng xuống, chạy theo người chơi chậm hơn một nhịp: chạy liên tục là né được.
  - Bắn 3 tia chéo hình quạt.
  - Dừng giữa ray và quét cả sàn (đèn đỏ báo trước 1 giây): đá tường lên vách để né.
- **Điểm yếu:** con ngươi mở ra sau mỗi lần quét sàn.
- **Phần thưởng:** mở cửa vào khu hologram. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Vực hologram', 202, 0, 64, 20, 7, [
   B(0, 0, 64, 1), F((0, 12), (6, 12)), F((58, 12), (64, 12)), H('void', 6, 12, 52, 8),
   P(10, 11, 4, 'holo'), P(20, 9, 4, 'holo'), P(30, 11, 4, 'holo'), P(40, 8, 4, 'holo'), P(50, 10, 4, 'holo'), P(35, 3, 3, 'holo'),
   X(8, 15, 'bệ hiện 2s / ẩn 1s, lần lượt từ trái sang phải'), X(26, 4, 'bệ 6 ẩn'),
   E('C', 2, 11), E('D', 25, 4), E('D', 46, 4), E('H', 36.5, 2),
   PATH((1, 11), (6, 11), (12, 10), (22, 8), (32, 10), (42, 7), (52, 9), (63, 11)), ALT((32, 10), (36, 2.5))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** cao trào của màn. Đi qua vực không đáy chỉ trên các bệ hologram nhấp nháy.
- **Địa hình:** vực rộng 52 ô (khoảng 1.660px), không có sàn. Rơi là mất mạng.
- **Cơ chế – bệ hologram:**
  - 5 bệ, mỗi bệ **hiện 2 giây, ẩn 1 giây**.
  - Các bệ bật lần lượt từ trái sang phải thành một làn sóng: đi đúng nhịp thì luôn có bệ dưới chân.
  - 0.3 giây trước khi ẩn, bệ chớp trắng.
- **Địch:** 2 Drone. Đạn của chúng không đẩy lùi, nhưng buộc người chơi phải nhảy lệch nhịp.
- **Lối phụ (Heart Tank):**
  - Có **bệ thứ 6 ẩn** phía trên bệ 3 (x ≈ 237, y ≈ 3). Bệ này chỉ hiện trong lúc bệ 3 đang ẩn.
  - Phải nhảy từ bệ 3 ngay lúc nó tắt, đáp lên bệ 6, lấy Heart Tank, rồi rơi xuống bệ 4.
  - Giáp Falcon bay ngang qua được cả vực.'''),

 Room('R6', 'Băng chuyền tốc cao', 266, 0, 60, 16, 6, [
   B(0, 0, 60, 2), F((0, 12), (26, 12), None, (30, 12), (60, 12)), B(0, 15, 60, 1), B(0, 12, 26, 1),
   CV(4, 11.4, 22, 1), CV(32, 11.4, 22, 1), BAR(18, 2, 0.6, 10, 'laser'), BAR(44, 2, 0.6, 10, 'laser'),
   AR(14, 5, 6, 0, 'alarm'), AR(40, 5, 6, 0, 'alarm'), X(15, 3, 'cổng quét chạy ngang'),
   E('C', 2, 11), E('R', 29, 11), E('B', 36, 11), E('S', 55, 11), E('T', 40, 14),
   PATH((1, 11), (59, 11)), ALT((28, 11), (28, 14), (40, 14))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** băng chuyền **xuôi chiều** (đẩy sang phải 140px/giây) làm người chơi đi quá nhanh, trong khi phải né cổng quét.
- **Địa hình:** hành lang 60 ô, 2 đoạn băng chuyền dài 22 ô.
- **Bẫy – cổng quét laser:**
  - 2 tia laser đứng chạy ngang qua lại trên mỗi đoạn băng chuyền, 100px/giây.
  - Băng chuyền đẩy người chơi lao vào tia. Phải nhảy qua tia (tia chỉ cao 10 ô, trần thấp nên nhảy sát) hoặc chạy ngược băng chuyền để giữ khoảng cách.
- **Địch:**
  - 1 Brute đứng cuối băng chuyền thứ hai: băng chuyền đẩy người chơi vào nó.
  - 1 Sniper cuối phòng.
- **Vật phẩm:** Reploid #3 giữa hai đoạn băng chuyền.
- **Lối phụ (Sub-Tank):** giữa hai đoạn băng chuyền có khe 4 ô rơi xuống **ống kỹ thuật** dưới sàn. Sub-Tank ở giữa ống. Cuối ống có thang lên lại.'''),

 Room('R7', 'Phòng tối', 326, 0, 30, 16, 2, [
   B(0, 0, 30, 2), F((0, 12), (30, 12)), Z('dark', 2, 2, 26, 10, ''), BAR(29, 2, 1, 10, 'door'), E('R', 14, 11),
   X(4, 5, 'đom đóm phát sáng chỉ đường'), PATH((1, 11), (28, 11))], '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.
- Phòng tối hoàn toàn, chỉ có đàn đom đóm máy bay chậm làm đèn. Báo hiệu cơ chế của trận boss.'''),

 Room('BOSS', 'Shining Hotarunicus', 356, 0, 32, 16, 6, [
   B(0, 0, 2, 12), B(30, 0, 2, 12), B(0, 0, 32, 1), F((0, 12), (32, 12)), Z('dark', 2, 1, 28, 11, ''), E('*', 20, 5),
   X(4, 3, 'pha 2: tắt đèn'), PATH((3, 11), (29, 11))], '''
- **Đấu trường 28 ô**, kín, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (tia laser, đạn sáng, phân thân).
- **Pha 2** (dưới 50% HP):
  - **Tắt đèn toàn sân.** Chỉ thấy boss khi nó phát sáng trước mỗi đòn (0.8 giây) và quầng sáng nhỏ quanh X.
  - Đạn nạp đầy của X chiếu sáng đường bay của nó.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Phòng thí nghiệm Laser', en='Laser Institute', boss='Shining Hotarunicus', act='Act I · X5', theme=THEME, capsule='Falcon Body',
 subtitle='Area 1 (viện nghiên cứu): R1 → R2 → R3 (leo, tia xoay) → R4 (2 lớp laser) → Mini-boss  |  Area 2 (khu thử nghiệm): R5 (vực hologram) → R6 → R7 → Boss',
 keep='Boss, capsule Falcon Body, công tắc quang học, tường laser và bệ hologram vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Viện nghiên cứu quang học đang chạy thử nghiệm. Màn này là **câu đố ánh sáng**: tường laser chặn đường cho tới khi bắn đúng công tắc, rồi tới vực không đáy chỉ có bệ hologram nhấp nháy.',
 areas=['**Area 1 – Viện nghiên cứu:** trắng lạnh, kính, màn hình. Dạy tường laser theo nhịp, công tắc quang học, tia xoay.',
        '**Area 2 – Khu thử nghiệm:** tối, ánh xanh hologram. Cao trào là vực hologram, rồi băng chuyền có cổng quét.'],
 flow='né hàng rào laser → bắn công tắc mở đường → leo giếng có tia xoay → giải câu đố 2 lớp laser → mini-boss trên ray trần → vượt vực hologram → băng chuyền xuôi chiều → boss trong bóng tối',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, màn Shining Hotarunicus:** công tắc quang học, tường laser, capsule giáp trong buồng kín cần lướt trên không.',
       '**X4, màn Web Spider / X6, màn Shield Sheldon:** bệ ẩn hiện và gương phản xạ.',
       '**X8, màn Optic Sunflower:** viện quang học, ánh sáng làm cơ chế chính. Bản 16-bit demake được khen nhiều nhất ở màn này.',
       '**X Corrupted:** bệ bí mật chỉ hiện khi bệ khác ẩn (đọc ngược nhịp của cơ chế chính).'],
 engine=['Tia laser: tường đứng có nhịp bật/tắt, hoặc chỉ tắt bằng công tắc (có hẹn giờ hoặc vĩnh viễn).',
         'Công tắc quang học: bắn trúng thì bật một nhóm đối tượng theo id.',
         'Tia laser xoay quanh tâm.',
         'Bệ hologram: hiện/ẩn theo nhịp, lệch pha theo thứ tự; bệ ẩn chỉ hiện khi bệ khác ẩn.',
         'Cổng quét laser chạy ngang.',
         'Vùng tối: che khung hình, chỉ chừa quầng sáng quanh X và vật phát sáng.',
         'Mini-boss Mắt Laser chạy trên ray trần.'],
 art=['**Tileset "Viện" (Area 1):** 47 ô viền thép trắng, kính, khung màn hình.',
      '**Tileset "Khu thử nghiệm" (Area 2):** 47 ô viền tối, ô lưới kỹ thuật, ống kỹ thuật dưới sàn.',
      '**Vật thể:** đầu phát laser (tường và xoay, 4 khung), công tắc quang học (2 trạng thái), gương, bệ hologram (3 khung: hiện, chớp, ẩn), cổng quét.',
      '**Nền:** Area 1: phòng thí nghiệm kính và ống nghiệm (2 lớp parallax). Area 2: lưới hologram và đom đóm máy (2 lớp).'],
)
STAGE['rooms'] = rooms
