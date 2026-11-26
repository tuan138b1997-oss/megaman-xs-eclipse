from lib import *

THEME = dict(bg1=(30, 44, 66), bg2=(34, 40, 56), rock1=(92, 110, 120), rock2=(96, 100, 116))


def mine(x, y): return H('mine', x, y, 1, 1)


rooms = [
 Room('R1', 'Bến cảng', 0, 40, 50, 20, 2, [
   F((0, 8), (30, 8)), B(26, 8, 4, 12), F((30, 18), (50, 18)), H('water', 30, 10, 20, 8),
   X(31, 15.5, 'nước: trọng lực ×0.32'), E('S', 20, 7), E('D', 42, 5),
   PATH((1, 7), (29, 7), (34, 12), (49, 14))], '''
- **Mục đích:** giới thiệu **nước**: vào nước thì trọng lực nhẹ (×0.32), nhảy cao gấp khoảng 2.5 lần nhưng rơi chậm.
- **Địa hình:**
  - Cầu tàu bê tông dài 30 ô, mặt sàn ở y 48.
  - Cuối cầu tàu là mặt biển. Đáy biển ở y 58, nước sâu 8 ô.
  - Trên mặt nước có sóng nhấp nhô 1 ô (chỉ để nhìn, không đẩy).
- **Địch:**
  - 1 Sniper trên cầu tàu.
  - 1 Drone bay sát mặt nước, lao xuống khi người chơi nhảy xuống nước.
- **Trang trí:** cần cẩu bến, container, đèn hải đăng ở nền xa.'''),

 Room('R2', 'Hành lang ngập', 50, 40, 70, 20, 3, [
   B(0, 0, 70, 2), F((0, 18), (70, 18)), H('water', 0, 2, 70, 16), P(12, 7, 6), P(38, 6, 8),
   mine(22, 10), mine(30, 13), mine(54, 9), Z('current', 34, 11, 18, 6, 'dòng chảy → 60px/s'), AR(37, 15, 7, 0),
   E('D', 18, 12), E('D', 60, 12), E('R', 42, 5),
   PATH((0, 14), (10, 14), (14, 6), (18, 12), (33, 15), (52, 15), (69, 14)), ALT((33, 15), (40, 5))], '''
- **Mục đích:** luyện di chuyển dưới nước và né **thủy lôi**.
- **Địa hình:**
  - Hành lang căn cứ ngập hoàn toàn, dài 70 ô, trần ở y 42, đáy ở y 58.
  - 2 kệ cao sát trần (y 47 và y 46). Chỉ với tới được nhờ trọng lực nước.
- **Bẫy:**
  - **3 thủy lôi** trôi lơ lửng, nhấp nháy. Chạm hoặc bắn trúng thì nổ sau 1 giây, bán kính 2 ô. Bắn từ xa là an toàn.
  - **Dòng chảy ngang** đẩy sang phải 60px/giây ở nửa sau hành lang (có bọt khí chỉ hướng). Đi xuôi dòng nhanh hơn, nhưng dễ trôi vào thủy lôi.
- **Địch:** 2 Drone dạng cá máy, bơi zigzag.
- **Vật phẩm:** Reploid #1 trên kệ cao thứ hai.'''),

 Room('R3', 'Trụ thông khí', 120, 10, 20, 50, 4, [
   B(0, 0, 2, 42), B(0, 48, 20, 2), B(18, 14, 2, 34), B(2, 0, 16, 1), H('water', 2, 20, 16, 28),
   P(12, 40, 4), P(2, 32, 4), P(12, 24, 4), P(2, 14, 4), P(3, 4, 5), mine(9, 30), X(8, 19, 'mặt nước'),
   E('D', 9, 37), E('A', 5, 3), E('S', 4, 13),
   PATH((1, 46), (9, 46), (14, 39), (4, 31), (14, 23), (4, 13), (12, 9), (19.5, 9)),
   ALT((8, 21), (6, 5))], '''
- **Mục đích:** đoạn dọc đầu tiên, nửa dưới ngập nước, nửa trên là không khí.
- **Địa hình:**
  - Giếng rộng 16 ô, cao 48 ô (từ y 58 lên y 11).
  - Mặt nước ở y 30. Dưới mặt nước leo rất dễ (nhảy cao), lên khỏi mặt nước thì trọng lực trở lại bình thường: phải đá tường.
  - 4 kệ zigzag. Lối ra ở khe vách phải phía trên (y 15–24).
- **Địch:**
  - 1 Drone cá dưới nước.
  - 1 Sniper trên kệ cao nhất, bắn xuống khi người chơi vừa ra khỏi mặt nước.
- **Bẫy:** 1 thủy lôi ngay dưới mặt nước.
- **Lối phụ (Capsule Falcon Head):**
  - Kệ capsule nằm sát trần bên trái (x ≈ 124, y ≈ 14), cao hơn mọi kệ khác.
  - Mẹo: **nhảy từ dưới nước lên**. Nhảy ở mặt nước giữ được độ cao của nhảy dưới nước, vừa đủ với tới kệ.
  - Đá tường từ kệ cao nhất cũng không tới, nên người chơi phải hiểu cơ chế nước.'''),

 Room('MID', 'Tàu ngầm U-555', 140, 14, 40, 20, 5, [
   B(0, 0, 40, 1), B(0, 10, 1, 8), B(39, 0, 1, 14), F((0, 18), (40, 18)), H('water', 1, 8, 38, 10),
   E('M', 26, 13), X(3, 3, 'nước hạ 2 ô mỗi 1/3 máu'), PATH((1, 7), (8, 16), (38, 16))], '''
- **Đấu trường 38 ô**, nước ngập đến y 22 (sâu 10 ô).
- **Tàu ngầm U-555** bơi qua lại trong nước, chỉ nhô tháp chỉ huy lên mặt nước.
- **Đòn đánh:**
  - Bắn 2 ngư lôi đuổi theo chậm: bắn hạ được.
  - Thả 4 thủy lôi nổi lên từ từ.
  - Nhô lên húc theo đường cong khi người chơi đứng trên mặt nước.
- **Mực nước:** mỗi khi mất 1/3 máu, tàu xả van và nước hạ 2 ô. Nước càng thấp thì tàu càng lộ thân, nhưng người chơi mất khả năng nhảy cao.
- **Điểm yếu:** tháp chỉ huy (nhảy từ nước lên mà bắn).
- **Phần thưởng:** mở cửa phòng bơm. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Phòng bơm', 180, 14, 50, 24, 5, [
   B(0, 0, 50, 1), F((0, 18), (14, 18), (14, 22), (36, 22), (36, 18), (50, 18)), B(48, 9, 2, 9),
   H('water', 0, 6, 48, 16), P(3, 5, 6), P(40, 4, 6),
   E('C', 2, 17), E('K', 6, 4), E('K', 25, 21), E('T', 31, 21), E('B', 18, 21), E('S', 43, 3), E('R', 9, 17),
   X(15, 3, 'công tắc 1: rút nước'), X(16, 23, 'công tắc 2: bơm lại'),
   PATH((1, 17), (5, 6), (14, 12), (40, 5), (49.5, 5)), ALT((14, 12), (20, 21), (31, 21))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** câu đố **mực nước**: lúc thì cần nước để nhảy cao, lúc thì cần rút nước để xuống sâu.
- **Địa hình:**
  - Phòng 48 ô, giữa có một **bồn trũng** sâu 4 ô (x 194–216).
  - Cửa ra nằm cao ở vách phải (y 18–23). Chỉ với tới khi phòng còn ngập.
- **Cơ chế:**
  - **Công tắc 1** trên kệ cao bên trái: bắn vào thì bơm rút nước trong 3 giây, chỉ còn đọng trong bồn trũng.
  - **Công tắc 2** dưới đáy bồn: bắn vào thì nước dâng lại trong 3 giây.
- **Địch:**
  - 1 Brute dưới đáy bồn (chỉ lộ ra khi rút nước).
  - 1 Sniper ở kệ cửa ra.
- **Vật phẩm:** Reploid #2 ở đầu phòng.
- **Lối phụ (Sub-Tank):**
  - Đường chính không cần rút nước: cứ nhảy cao dưới nước rồi lên kệ cửa ra.
  - Muốn lấy **Sub-Tank** ở đáy bồn: bắn công tắc 1, xuống bồn, hạ Brute, lấy Sub-Tank, rồi bắn công tắc 2 để nước dâng lại mới ra được.'''),

 Room('R5', 'Ống hải lưu', 230, 10, 64, 18, 7, [
   B(0, 0, 28, 6), B(36, 0, 28, 6), B(28, 0, 8, 1), B(0, 6, 30, 2), B(34, 6, 30, 2), F((0, 16), (64, 16)),
   H('water', 0, 8, 64, 8), H('water', 30, 1, 4, 7), BAR(0, 8, 2, 8, 'trash'), X(2, 9, 'tua-bin'),
   H('spike', 12, 8, 6, 1), H('spike', 22, 15, 6, 1), H('spike', 40, 8, 8, 1), H('spike', 50, 15, 6, 1),
   mine(34, 12), mine(46, 11), Z('current', 2, 9, 60, 6, ''), AR(60, 12, -8, 0), AR(30, 13, -8, 0),
   X(6, 13.5, 'hút về tua-bin 60→90px/s'), E('D', 20, 11), E('D', 56, 11), E('H', 32, 3),
   PATH((1, 12), (63, 12)), ALT((30, 10), (32, 4))], '''
- **Mục đích:** cao trào của màn. Bơi ngược dòng hút mạnh dần trong một ống có san hô gai.
- **Cơ chế:**
  - **Tua-bin** ở đầu trái ống hút nước về phía nó: 60px/giây, tăng lên 90px/giây ở nửa sau ống.
  - Chạm tua-bin là mất mạng.
  - Đi sang phải nghĩa là đi ngược dòng: phải lướt liên tục, mỗi lần dừng là bị kéo lùi.
- **Địa hình:**
  - Ống dài 64 ô, cao 8 ô (y 18–26).
  - **San hô gai** mọc xen kẽ trên trần và dưới sàn. Nhảy quá cao (trọng lực nước) là chạm gai trần, nên phải nhảy thấp.
- **Bẫy:** 2 thủy lôi trôi theo dòng về phía người chơi.
- **Địch:** 2 Drone cá. Cá đầu tiên chặn giữa hai bụi gai.
- **Lối phụ (Heart Tank):**
  - Giữa ống có một **giếng đứng** đi lên (x 260–264). Trong giếng không có dòng hút.
  - Heart Tank ở đỉnh giếng. Giếng cũng là chỗ nghỉ duy nhất trong ống.
- **Giáp hỗ trợ:** Falcon lướt trên không xa hơn, vượt dòng dễ hơn.'''),

 Room('R6', 'Rãnh san hô', 294, 16, 26, 46, 6, [
   B(0, 0, 26, 2), B(0, 10, 2, 36), B(2, 10, 8, 1), B(24, 2, 2, 36), B(0, 44, 26, 2), H('water', 2, 2, 22, 42),
   H('spike', 2, 16, 9, 2), H('spike', 15, 22, 9, 2), H('spike', 2, 28, 9, 2), H('spike', 15, 34, 9, 2),
   Z('current', 3, 12, 20, 30, ''), AR(12, 14, 0, 4), X(4, 41, 'kéo xuống 40px/s'),
   E('C', 4, 9), E('R', 20, 21), E('D', 8, 24), E('S', 19, 33),
   PATH((3, 9), (13, 12), (13, 19), (11, 22), (11, 26), (13, 30), (13, 38), (25, 42))], '''
- **Checkpoint 2** ở đầu phòng (gờ đá ngay cửa ống).
- **Mục đích:** đi xuống có kiểm soát: rơi chậm trong nước nhưng bị dòng kéo xuống.
- **Địa hình:**
  - Rãnh đứng rộng 22 ô, sâu 34 ô (từ y 26 xuống y 60).
  - **4 mỏm san hô gai** chìa ra xen kẽ trái/phải.
- **Cơ chế:** dòng nước **kéo xuống 40px/giây**. Người chơi phải lái sang trái/phải để luồn giữa các mỏm gai. Thả tay là trôi thẳng vào gai.
- **Địch:**
  - 1 Drone cá giữa rãnh.
  - 1 Sniper đứng trên mỏm san hô cuối, bắn lên.
- **Vật phẩm:** Reploid #3 trên mặt phẳng của mỏm san hô thứ hai (mặt trên không có gai).
- **Lối ra:** khe vách phải ở đáy rãnh.'''),

 Room('R7', 'Cửa cống', 320, 48, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 12), (30, 12)), H('water', 0, 9, 30, 3), BAR(29, 2, 1, 7, 'door'), E('R', 14, 8),
   X(4, 4, 'năng lượng nhỏ'), PATH((1, 8), (28, 8))], '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss. Nước nông 3 ô.'''),

 Room('BOSS', 'Tidal Makkoeen', 350, 44, 32, 18, 6, [
   B(0, 0, 2, 16), B(30, 0, 2, 16), B(0, 0, 32, 1), F((0, 16), (32, 16)), H('water', 2, 10, 28, 6), E('*', 22, 9),
   X(4, 4, 'pha 2: nước dâng ngập sân'), PATH((3, 9), (29, 9))], '''
- **Đấu trường 28 ô**, nửa dưới ngập nước (sâu 6 ô). Hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (sóng thần, bắn băng, lướt trên mặt nước).
- **Pha 2** (dưới 50% HP):
  - **Nước dâng ngập toàn sân** trong 4 giây.
  - Người chơi nhảy cao hơn nhưng di chuyển chậm hơn. Makkoeen bơi nhanh gấp đôi.
  - Các khối băng Makkoeen bắn ra trôi lên trần, thành bệ tạm 5 giây.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Căn cứ đáy biển', en='Ocean Base', boss='Tidal Makkoeen', act='Act I · X5', theme=THEME, capsule='Falcon Head',
 subtitle='Area 1 (cảng và hành lang ngập): R1 → R2 → R3 (leo, nửa ngập) → Mini-boss U-555  |  Area 2 (đáy biển): R4 (bơm) → R5 (ống hút) → R6 (rãnh, đi xuống) → R7 → Boss',
 keep='Boss, capsule Falcon Head và sub-boss tàu ngầm U-555 vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Một căn cứ hải quân chìm dần dưới biển. Toàn màn xoay quanh **nước**: dưới nước thì nhảy cao, rơi chậm, nhưng dòng chảy và thủy lôi khó lường. Người chơi học cách tận dụng nước, rồi học cách điều khiển mực nước.',
 areas=['**Area 1 – Cảng và hành lang ngập:** bê tông, đèn xanh, bọt khí. Dạy trọng lực nước, thủy lôi, leo giếng nửa ngập.',
        '**Area 2 – Đáy biển:** ống thép, san hô gai, bóng tối xanh thẫm. Câu đố mực nước, ống hút ngược dòng, rãnh đi xuống.'],
 flow='lặn xuống → nhảy siêu cao dưới nước → leo giếng nửa ngập → đấu tàu ngầm → rút/bơm nước → bơi ngược dòng hút → luồn xuống rãnh gai → boss nước dâng',
 time='khoảng 6–8 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, màn Tidal Makkoeen:** căn cứ đáy biển, tàu ngầm làm sub-boss, capsule giáp trên hốc trần cần nhảy cao.',
       '**X (SNES) Launch Octopus / X3 Toxic Seahorse:** nhảy cao dưới nước làm cơ chế chính.',
       '**X4, màn Jet Stingray / X6 Metal Shark Player:** đoạn bị cuốn hoặc bị ép, phải di chuyển liên tục.',
       '**X8 16-bit demake / X Corrupted:** câu đố công tắc thay đổi địa hình; lối phụ đòi hiểu cơ chế thay vì chỉ kỹ năng.'],
 engine=['Vùng nước: trọng lực ×0.32, tốc độ rơi tối đa giảm, nhảy ở mặt nước giữ độ cao nhảy dưới nước.',
         'Mực nước thay đổi được theo công tắc (vùng nước có độ cao động).',
         'Dòng chảy: vùng đẩy theo hướng, tốc độ tăng dần theo vị trí.',
         'Thủy lôi: nổ chậm 1 giây khi chạm hoặc bị bắn, bán kính 2 ô.',
         'Tua-bin hút (vùng chết ở đầu ống).',
         'Mini-boss Tàu ngầm U-555 bơi trong nước, mực nước hạ theo máu.'],
 art=['**Tileset "Cảng" (Area 1):** 47 ô viền bê tông ướt, cầu tàu, hành lang căn cứ có cửa sổ tròn.',
      '**Tileset "Đáy biển" (Area 2):** 47 ô viền, ống thép, san hô gai (trần và sàn), đá rong.',
      '**Vật thể:** thủy lôi (3 khung nhấp nháy), tua-bin (4 khung), công tắc bơm (2 trạng thái), mặt nước động (4 khung), bọt khí.',
      '**Nền:** Area 1: biển đêm và hải đăng (2 lớp parallax). Area 2: tia sáng xuyên nước và đàn cá xa (2 lớp).'],
)
STAGE['rooms'] = rooms
