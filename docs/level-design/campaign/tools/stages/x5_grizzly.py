from lib import *

THEME = dict(bg1=(58, 46, 40), bg2=(44, 44, 54), rock1=(130, 120, 110), rock2=(110, 112, 124))


def car(x, w, top=4, floor=12):
    """Một toa: nóc ở y=top, sàn ở y=floor, hai vách đầu toa chừa cửa ở dưới."""
    return [B(x, top, w, 1), B(x, floor, w, 2), B(x, top, 1, 4), B(x + w - 1, top, 1, 4)]


rooms = [
 Room('R1', 'Sân ga', 0, 30, 40, 16, 2, [
   F((0, 12), (27, 12)), *car(28, 12), H('void', 27, 14, 1, 2), X(2, 6, 'tàu khởi hành sau 3s'),
   E('S', 20, 11), E('D', 33, 1.5), PATH((1, 11), (24, 11), (29, 3), (39, 3))], '''
- **Mục đích:** cho người chơi nhận ra "mình đang ở trên một đoàn tàu chạy".
- **Địa hình:**
  - Sân ga phẳng 27 ô, mặt sàn ở y 42.
  - Toa cuối đoàn đậu sát sân ga. Sau 3 giây kể từ khi vào phòng, còi hú và đoàn tàu chạy. Nền parallax bắt đầu trôi.
  - Nhảy lên nóc toa (cao 8 ô so với sân ga, đứng trên thùng hàng để với tới).
- **Địch:**
  - 1 Sniper trên sân ga.
  - 1 Drone bay ngang nóc toa.
- **Trang trí:** biển ga, đèn tín hiệu, cát bay.'''),

 Room('R2', 'Nóc toa 1–3', 40, 30, 84, 16, 3, [
   *car(0, 24), *car(28, 26), *car(58, 26), H('void', 24, 13, 4, 3), H('void', 54, 13, 4, 3),
   Z('wind', 0, 0, 84, 4, 'gió ngược −55px/s trên nóc'), AR(30, 2, -6, 0), AR(70, 2, -6, 0),
   E('S', 12, 11), E('R', 40, 11), E('S', 70, 11), E('D', 45, 2),
   PATH((1, 3), (23, 3), (26, 1.5), (29, 3), (53, 3), (56, 1.5), (59, 3), (83, 3)),
   ALT((2, 11), (23, 11)), ALT((30, 11), (52, 11))], '''
- **Mục đích:** dạy **hai tầng đường đi** của màn: nóc toa (nhanh nhưng có gió) và trong toa (không gió nhưng chật, có địch).
- **Địa hình:**
  - 3 toa dài 24–26 ô, giữa các toa là **khe 4 ô**. Rơi xuống đường ray là mất mạng.
  - Nóc toa ở y 34, sàn trong toa ở y 42, trần trong toa thấp (cao 7 ô).
  - Mỗi đầu toa có cửa để chui vào/ra.
- **Bẫy – gió ngược:** trên nóc toa, gió đẩy lùi 55px/giây. Lướt hoặc nhảy dài ngược gió ngắn đi rõ rệt, nên nhảy qua khe phải lấy đà.
- **Địch:**
  - 1 Sniper trong toa 1 và 1 trong toa 3, đứng ở cuối toa, bắn dọc hành lang.
  - 1 Drone trên nóc toa 2.
- **Vật phẩm:** Reploid #1 trong toa 2.'''),

 Room('R3', 'Khớp nối tách', 124, 30, 34, 16, 4, [
   *car(0, 14), *car(20, 14), H('void', 14, 13, 6, 3), X(13, 9, 'khe 0→6 ô'), X(13, 10.5, 'trong 6 giây'),
   Z('wind', 0, 0, 34, 4, 'gió ngược'), E('D', 17, 6), E('S', 30, 11),
   PATH((1, 3), (13, 3), (17, 1.5), (21, 3), (33, 3))], '''
- **Mục đích:** áp lực thời gian lần đầu.
- **Cơ chế – khớp nối tách:**
  - Khi người chơi bước lên toa trước khớp, khớp nối nổ chốt (có tiếng "cạch" và tia lửa).
  - Khe giữa hai toa **rộng dần từ 0 lên 6 ô trong 6 giây** (1 ô mỗi giây), toa phía sau tụt lại.
  - Qua sớm thì bước qua được; chậm hơn 4 giây thì phải lướt-nhảy; quá 6 giây thì không với tới, toa trôi về checkpoint (mất mạng).
- **Địch:**
  - 1 Drone lượn đúng trên khe: bắn ngay hoặc bỏ qua, không nên đứng đánh.
  - 1 Sniper trong toa sau.
- **Ghi chú:** trên nóc vẫn có gió ngược, nên cách an toàn là chui vào trong toa rồi chạy.'''),

 Room('R4', 'Toa cần cẩu', 158, 4, 18, 42, 4, [
   B(0, 38, 18, 4), B(0, 4, 2, 34), B(16, 10, 2, 28), B(0, 0, 18, 1),
   P(12, 32, 4), P(2, 25, 4), P(12, 18, 4), P(2, 11, 4), H('trash', 7, 21, 5, 2), X(5, 23.3, 'đối trọng lắc 3s'),
   P(13, 4, 4, 'move'), E('R', 4, 24), E('D', 9, 14),
   PATH((1, 37), (9, 37), (14, 31), (4, 24), (14, 17), (4, 10), (10, 6), (14, 3.5), (17.5, 3.5))], '''
- **Mục đích:** đoạn **leo dọc** duy nhất, cũng là đường vượt chỗ đoàn tàu bị đứt.
- **Địa hình:**
  - Toa chở cần cẩu có cột tháp cao 34 ô (từ y 42 lên y 8). Hai vách là khung giàn, đá tường được.
  - 4 kệ nghỉ zigzag cách nhau 7 ô.
  - Trên đỉnh có **móc cẩu chạy trên cáp**: đứng lên móc thì nó trượt sang phải với tốc độ 90px/giây, chở người chơi vượt khoảng trống giữa hai đoạn tàu rồi thả xuống toa sau.
- **Bẫy – đối trọng lắc:** khối đối trọng 5 ô lắc ngang giữa giếng, chu kỳ 3 giây. Ở giữa đường leo, phải chờ nó lắc qua.
- **Địch:** 1 Drone gần đỉnh.
- **Vật phẩm:** Reploid #2 trên kệ thứ hai, bị kẹt sau đối trọng.
- **Giáp hỗ trợ:** Gaea bám tường không trượt, dễ chờ nhịp đối trọng.'''),

 Room('MID', 'Xe tải bọc thép', 176, 30, 32, 16, 5, [
   B(0, 12, 32, 2), H('void', 0, 14, 32, 2), B(0, 6, 1, 6), B(31, 6, 1, 6), E('M', 24, 9),
   X(3, 8, 'toa sàn phẳng'), PATH((2, 11), (30, 11))], '''
- **Đấu trường là một toa sàn phẳng 30 ô**, hai đầu có thành chắn thấp (6 ô) để đá tường.
- **Xe tải bọc thép** chạy trên đường song song phía sau toa, nhảy lên toa để húc.
- **Đòn đánh:**
  - Bắn 2 quả đạn pháo theo đường vòng cung: đứng dưới điểm rơi thì bị trúng (có bóng báo trước).
  - Tăng tốc húc ngang từ đầu này sang đầu kia toa: đá tường lên thành chắn để né.
  - Thả 3 mìn lăn trên sàn.
- **Điểm yếu:** buồng lái lộ ra 2 giây sau mỗi cú húc.
- **Phần thưởng:** mở đường sang toa Ride Armor. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Toa Ride Armor', 208, 30, 54, 20, 5, [
   B(0, 4, 54, 1), B(0, 12, 40, 2), B(50, 12, 4, 2), P(40, 12, 10, 'break'), B(0, 4, 1, 4), B(53, 4, 1, 4),
   B(38, 18, 14, 2), B(38, 14, 1, 4), B(51, 14, 1, 4), H('void', 0, 18, 38, 2),
   CV(8, 11.4, 28, -1), CW(18, 7, 5), CW(30, 7, 5),
   E('C', 3, 11), E('V', 6, 11), E('B', 25, 11), E('R', 35, 11), E('A', 46, 17), E('T', 28, 3), E('S', 48, 11),
   X(40, 10.4, 'sàn nứt'), X(40, 15.5, 'khoang két'),
   PATH((2, 11), (52, 11)), ALT((42, 11), (44, 16)), ALT((23, 11), (24, 6), (27, 3))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** cưỡi **Ride Armor** trong khoang hàng, phá vật cản để tìm lối phụ.
- **Địa hình:**
  - Khoang hàng dài 54 ô, trần ở y 34, sàn ở y 42.
  - **Băng chuyền chạy ngược** (đẩy sang trái 80px/giây) dài 28 ô.
  - 2 **thùng thép** chắn đường. Chỉ Ride Armor đấm vỡ được; X đi bộ phải nhảy qua (sát trần, khó).
- **Địch:**
  - 1 Brute giữa băng chuyền.
  - 1 Sniper cuối khoang.
- **Vật phẩm:** Reploid #3 sau thùng thép thứ hai.
- **Lối phụ (Capsule Falcon Foot):**
  - Cuối khoang có đoạn **sàn thép nứt** 10 ô (x 248–258). Ride Armor nhảy rồi dậm xuống thì sàn vỡ.
  - Bên dưới là **khoang két** chứa capsule Falcon Foot.
  - Ride Armor không leo ra được: bỏ xe, đá tường vách khoang lên lại.
- **Lối phụ (Sub-Tank):** trèo lên thùng thép thứ nhất, đứng trên nóc thùng rồi nhảy lên **cửa sập nóc toa**. Sub-Tank nằm trên nóc, giữa gió.'''),

 Room('R6', 'Nóc toa đầu và hầm', 262, 30, 76, 16, 7, [
   *car(0, 24), *car(28, 24), *car(52, 24), H('void', 24, 13, 4, 3), H('void', 76 - 0, 13, 0, 3),
   B(6, 0, 14, 3), B(40, 0, 20, 3), Z('alarm', 6, 3, 14, 1, ''), Z('alarm', 40, 3, 20, 1, ''),
   X(6, 1, 'hầm: khe 1 ô'), X(40, 1, 'hầm 2'), P(30, 1.2, 4), E('H', 32, 0.3),
   Z('wind', 0, 4, 1, 0, ''), AR(26, 2, -6, 0), E('C', 2, 3), E('D', 24, 6), E('D', 64, 2), E('R', 66, 11),
   PATH((1, 3), (5, 3), (5, 11), (21, 11), (23, 3), (27, 3), (38, 3), (38, 11), (51, 11), (53, 11), (75, 3)),
   ALT((27, 3), (30, 0.8))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** cao trào của màn. Phải đọc cảnh báo và đổi tầng liên tục trong gió mạnh.
- **Cơ chế – hầm quét:**
  - Đoàn tàu chui qua **2 đường hầm** (dài 14 và 20 ô). Trong hầm, trần chỉ cách nóc toa 1 ô.
  - Đứng trên nóc khi tàu vào hầm là bị quét (mất 1/3 máu và rơi xuống khe).
  - Trước mỗi hầm 1.5 giây: đèn đỏ chớp, còi hú, chữ "TUNNEL".
  - Cách tránh: chui qua cửa đầu toa vào trong, hoặc nằm sát nóc toa và lướt liên tục (giáp Shadow có thể bò).
- **Gió:** mạnh nhất màn, −80px/giây trên nóc.
- **Địch:**
  - 1 Drone bay trong khe giữa hai toa đầu: buộc phải ra khỏi toa đúng lúc.
  - 1 Drone ở cuối phòng.
- **Vật phẩm:** Reploid #4 trong toa cuối.
- **Lối phụ (Heart Tank):**
  - Giữa hai hầm có **cột tín hiệu** ngang tầm nóc toa (x ≈ 292, y ≈ 31).
  - Phải nhảy lên nóc ngay khi tàu ra khỏi hầm 1 rồi nhảy với lên cột trước khi tàu chạy qua (cửa sổ khoảng 2 giây).
  - Giáp Falcon bay lên được bất kỳ lúc nào giữa hai hầm.'''),

 Room('R7', 'Toa chỉ huy', 338, 30, 30, 16, 2, [
   *car(0, 30), BAR(29, 5, 1, 7, 'door'), X(5, 9, 'năng lượng nhỏ'), E('K', 14, 10), PATH((2, 11), (28, 11))], '''
- Phòng nghỉ trước boss: một viên năng lượng nhỏ, cửa boss.
- Công tắc **thả toa** (tùy chọn): bắn vào thì toa phía sau tách ra, mở ngắn đường quay lại nếu chết ở boss.'''),

 Room('BOSS', 'Crescent Grizzly', 368, 28, 32, 18, 6, [
   B(0, 8, 32, 2), H('void', 0, 14, 32, 4), B(0, 10, 32, 4), E('*', 22, 5), Z('wind', 0, 0, 32, 8, 'gió ngang đổi chiều 6s'),
   AR(6, 4, 5, 0), AR(26, 4, -5, 0), PATH((2, 7), (30, 7))], '''
- **Đấu trường là nóc toa chỉ huy dài 32 ô**, không có vách. Rơi khỏi mép là mất mạng.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (lao vuốt, ném bánh xe, đào lên).
- **Pha 2** (dưới 50% HP):
  - **Gió ngang đổi chiều mỗi 6 giây** (mũi tên trên HUD báo trước 1 giây), đẩy 70px/giây về phía mép.
  - Grizzly lợi dụng gió để lao xa hơn.
  - Một đường hầm ngắn quét qua mỗi 20 giây: cả X và Grizzly phải nằm xuống. Grizzly cứng đờ 1 giây sau mỗi lần nằm, đó là lúc bắn.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Tàu bọc thép', en='Armored Train', boss='Crescent Grizzly', act='Act I · X5', theme=THEME, capsule='Falcon Foot',
 subtitle='Area 1 (sa mạc, nóc tàu): R1 → R2 → R3 → R4 (leo cần cẩu) → Mini-boss  |  Area 2 (khoang hàng và đầu tàu): R5 (Ride Armor) → R6 (hầm quét) → R7 → Boss',
 keep='Boss, capsule Falcon Foot, Ride Armor Pod và sub-boss xe bọc thép vẫn giữ; thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Một đoàn tàu bọc thép 8 toa lao qua sa mạc. Màn chơi có **hai tầng song song**: nóc toa (nhanh, có gió ngược) và trong toa (chật, có địch). Người chơi phải chuyển tầng liên tục, nhất là khi tàu chui hầm.',
 areas=['**Area 1 – Nóc tàu giữa sa mạc:** thép nóng, cát bay, nền trôi nhanh. Dạy gió ngược, khe giữa toa, khớp nối tách và leo cột cẩu.',
        '**Area 2 – Khoang hàng và đầu tàu:** trong nhà, ánh đèn vàng. Cưỡi Ride Armor phá vật cản, rồi cao trào là chạy trên nóc khi tàu chui hầm.'],
 flow='chạy trên nóc ngược gió → chui vào toa → đua với khớp nối tách → leo cần cẩu → đấu xe bọc thép → cưỡi Ride Armor → né hầm quét → boss giữa gió',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X5, màn Crescent Grizzly:** truy đuổi xe bọc thép, có Ride Armor phá vật cản, capsule giáp nằm sau vách cần sức mạnh.',
       '**X2, màn Overdrive Ostrich:** màn tốc độ trên sa mạc, nền trôi tạo cảm giác di chuyển.',
       '**X8, màn Earthrock Trilobite / Gigabolt Man-O-War:** đoàn tàu và vật thể lớn đuổi theo; bản 16-bit demake làm lại các đoạn tự cuộn thành màn chơi thường.',
       '**X Corrupted:** hai tầng đường đi song song, lối phụ cần đổi tầng đúng lúc.'],
 engine=['Nền parallax trôi liên tục để tạo cảm giác tàu chạy (thế giới đứng yên, chỉ nền và đường ray trôi).',
         'Vùng gió đẩy ngang có tốc độ chỉnh được, đổi chiều theo nhịp.',
         'Khớp nối tách: một đoạn toa trượt lùi theo thời gian sau khi người chơi kích hoạt.',
         'Hầm quét: khối trần chạy ngang qua nóc tàu theo lịch, có cảnh báo trước.',
         'Móc cẩu chạy trên cáp (bệ di động theo đường ray trên cao).',
         'Sàn nứt chỉ vỡ khi Ride Armor dậm; thùng thép chỉ Ride Armor đấm vỡ.',
         'Mini-boss Xe tải bọc thép chạy song song và nhảy lên toa.'],
 art=['**Tileset "Toa thép" (Area 1):** 47 ô viền thép tán đinh, nóc toa, đầu toa có cửa, khớp nối.',
      '**Tileset "Khoang hàng" (Area 2):** 47 ô viền, băng chuyền, thùng thép (2 trạng thái), sàn nứt (2 trạng thái).',
      '**Vật thể:** móc cẩu, đối trọng lắc, cột tín hiệu, khung hầm đi qua (khối trần lớn), cửa sập nóc toa.',
      '**Nền:** Area 1: sa mạc và núi đá trôi nhanh (2 lớp parallax). Area 2: vách khoang và đèn chớp qua cửa sổ (2 lớp).'],
)
STAGE['rooms'] = rooms
