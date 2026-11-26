from kit import *

THEME = dict(bg1=(36, 26, 52), bg2=(30, 22, 46), rock1=(96, 80, 130), rock2=(88, 70, 124))
s3, p3 = shaft_up(22, 46, n=4)
for i, g in enumerate(s3):
    if g[0] == 'plat': s3[i] = ('plat', 'holo') + g[2:]


def sweep(x, h=12, y=1): return BAR(x, y, 0.8, h, 'laser')


def pits(xs, w, depth=2.5, pw=4, fy=12):
    pts = [(0, fy)]
    for x in xs:
        pts += [(x, fy), (x, fy + depth), (x + pw, fy + depth), (x + pw, fy)]
    pts.append((w, fy))
    return F(*pts)


rooms = [
 Room('R1', 'Cổng virus', 0, 40, 44, 16, 3, [
   F((0, 12), (44, 12)), B(16, 8, 4, 4), E('S', 38, 11), E('D', 26, 4), X(2, 3, 'nền dữ liệu nhiễu'), PATH((1, 11), (15, 11), (18, 7), (21, 11), (43, 11))], '''
- **Mục đích:** bước vào không gian virus Zero. Không có phần dạy: pháo đài giả định người chơi đã thạo.
- **Địa hình:** nền dữ liệu 44 ô, mặt sàn ở y 52, một **khối Cyberblock** cao 4 ô.
- **Địch:** 1 Drone, 1 Sniper.
- **Trang trí:** lưới mã nhị phân trôi, khối pixel vỡ, màu tím-xanh nhiễu.
- **Ghi chú:** màn pháo đài không có capsule, Heart Tank hay Sub-Tank. Bù lại có 4 Reploid và trạm nạp năng lượng lớn. Nên dùng giáp Falcon hoặc Fourth để lướt qua các cụm laser.'''),

 Room('R2', 'Laser quét 1', 44, 40, 64, 16, 4, [
   SP('sweep', x=0, y=1, w=.8, h=11, x1=63, speed=140, interval=6, phase=0, look='laser'),
   pits([12, 28, 44], 64), sweep(4), AR(5, 6, 6, 0, 'alarm'), X(6, 2, 'cụm laser 1–2: quét trái → phải, 140px/s, mỗi 6s'),
   E('R', 30, 14), E('D', 36, 5), E('S', 58, 11), PATH((1, 11), (63, 11))], '''
- **Mục đích:** giới thiệu **cụm laser tử thần**: một bức tường laser cao hết màn hình quét ngang.
- **Địa hình:** hành lang 64 ô, 3 **hốc trú** sâu 2.5 ô trong sàn, cách nhau 16 ô.
- **Cơ chế:**
  - Laser sinh ra ở mép trái, quét sang phải 140px/giây, mỗi 6 giây một lần (cụm 1 rồi cụm 2).
  - Chạm laser là mất 1/2 máu. Nằm trong hốc thì laser quét qua đầu.
  - Đèn đỏ ở mép trái nháy 1 giây trước khi laser xuất hiện.
- **Địch:** 1 Drone, 1 Sniper. Laser **không** gây sát thương cho địch.
- **Vật phẩm:** Reploid #1 trong hốc thứ hai.'''),

 Room('R3', 'Trục Cyberblock', 108, 10, 22, 46, 5, s3 + [X(3, 40, 'khối hiện 2s / ẩn 1s'), E('D', 11, 20), p3], '''
- **Mục đích:** đoạn dọc trên các **Cyberblock** nhấp nháy.
- **Địa hình:** trục rộng 18 ô, cao 42 ô (từ y 54 lên y 17). 4 Cyberblock làm bệ.
- **Cơ chế:** khối hiện 2 giây, ẩn 1 giây. Hai vách đá tường được, nhưng có vệt dữ liệu nhiễu: chạm vào thì bị đẩy ra 1 ô (không mất máu).
- **Địch:** 1 Drone.'''),

 Room('R4', 'Băng chuyền Boost', 130, 10, 64, 14, 5, [
   SP('chaser', x=0, y=2, w=1, h=10, x1=64, trigger=2, speed0=160, speed1=160, look='laser'),
   B(0, 0, 64, 2), F((0, 12), (64, 12)), CV(6, 11.4, 20, 1), CV(38, 11.4, 20, 1), P(28, 11.6, 4, 'thrust'), sweep(2, 10, 2),
   AR(3, 6, 6, 0, 'alarm'), X(4, 3, 'cụm laser 3 đuổi theo 160px/s'), B(32, 8, 3, 4), E('B', 50, 11),
   PATH((1, 11), (31, 11), (33, 7), (36, 11), (63, 11))], '''
- **Mục đích:** chạy nhanh hơn laser nhờ **băng chuyền xuôi chiều** và **tấm Boost**.
- **Địa hình:** hành lang 64 ô, trần ở y 12, sàn ở y 22.
- **Cơ chế:**
  - Cụm laser 3 **đuổi theo** người chơi 160px/giây ngay khi vào phòng.
  - Băng chuyền đẩy sang phải 100px/giây. Tấm Boost cho tốc độ tối đa 1.5 giây.
  - Một Cyberblock chắn giữa đường: nhảy qua mất đà, lướt-nhảy thì giữ đà.
  - Không có hốc trú: phải chạy tới cửa phòng sau (laser dừng ở cửa).
- **Địch:** 1 Brute cuối phòng, đứng ngay trên băng chuyền.'''),

 Room('MID', 'Lõi tường lửa', 194, 8, 30, 16, 5, arena(30, 16, 14) + [E('M', 15, 6), X(4, 10, 'khiên lục giác xoay')], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Lõi tường lửa** là khối lục giác lơ lửng, bao quanh bởi 6 tấm khiên dữ liệu xoay.
- **Đòn đánh:**
  - Bắn tia quét ngang hết sân (giống cụm laser thu nhỏ): nhảy lên vách.
  - Ném tấm khiên ra như đĩa bay rồi thu về.
- **Điểm yếu:** lõi trống khi một tấm khiên vừa bay ra.
- **Phần thưởng:** mở cửa khu laser đôi. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Laser quét đôi', 224, 10, 64, 16, 6, [
   SP('sweep', x=0, y=1, w=.8, h=11, x1=63, speed=140, interval=7, phase=0, look='laser'), SP('sweep', x=63, y=1, w=.8, h=11, x1=0, speed=140, interval=7, phase=0, look='laser'),
   pits([8, 22, 36, 50], 64, fy=12), sweep(2), sweep(61), AR(3, 6, 5, 0, 'alarm'), AR(61, 6, -5, 0, 'alarm'),
   X(10, 2, 'cụm 4 quét → và cụm 5 quét ← cùng lúc'), E('C', 2, 11), E('R', 38, 14), E('S', 30, 11), E('D', 46, 5),
   PATH((1, 11), (63, 11))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** hai laser quét **ngược chiều nhau** cùng lúc.
- **Địa hình:** hành lang 64 ô, 4 hốc trú.
- **Cơ chế:**
  - Cụm 4 quét từ trái, cụm 5 quét từ phải, gặp nhau ở giữa phòng. Chu kỳ 7 giây.
  - Một số lần hai laser gặp nhau **ngay trên một hốc**: đó là hốc duy nhất an toàn với cả hai lần quét.
  - Người chơi phải đọc vị trí giao nhau để chọn hốc.
- **Địch:** 1 Sniper, 1 Drone.
- **Vật phẩm:** Reploid #2 trong hốc thứ ba.'''),

 Room('R6', 'Hành lang tử thần', 288, 10, 80, 14, 8, [
   SP('chaser', x=0, y=2, w=1, h=10, x1=80, trigger=2, speed0=130, speed1=170, look='laser'),
   B(0, 0, 80, 2), F((0, 12), (80, 12)), sweep(1, 10, 2), AR(2, 6, 6, 0, 'alarm'), CV(6, 11.4, 16, 1), P(24, 11.6, 4, 'thrust'),
   B(30, 8, 3, 4), B(42, 2, 6, 6), CV(50, 11.4, 12, -1), P(64, 11.6, 4, 'thrust'), B(70, 9, 3, 3), H('void', 56, 12, 4, 2),
   X(6, 3, 'cụm laser 6 đuổi 130 → 170px/s, không hốc trú'), E('D', 36, 5), E('R', 76, 11),
   PATH((1, 11), (29, 11), (31, 7), (34, 11), (41, 11), (45, 10.5), (55, 11), (58, 9), (69, 11), (71, 8), (79, 11))], '''
- **Mục đích:** cao trào của màn. Chạy trước **cụm laser 6** suốt 80 ô, không có chỗ trú.
- **Cơ chế:**
  - Laser đuổi theo 130px/giây, tăng lên 170px/giây ở nửa sau.
  - 2 tấm Boost, 1 đoạn băng chuyền xuôi và 1 đoạn **băng chuyền ngược** (đẩy lùi 90px/giây) ngay trước một hố nhỏ.
  - Cyberblock thấp (nhảy) và Cyberblock treo (lướt dưới) xen kẽ.
- **Địch:** 1 Drone. Đứng lại bắn nó là bị laser bắt kịp: phải lướt qua.
- **Vật phẩm:** Reploid #3 ngay cửa ra. Chạy tới đây là an toàn.
- **Giáp hỗ trợ:** Falcon lướt trên không xa; Fourth lơ lửng qua hố.'''),

 Room('R7', 'Trạm nạp', 368, 10, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 12), (30, 12)), BAR(29, 2, 1, 10, 'door'), E('C', 2, 11), E('R', 15, 11), X(4, 6, 'năng lượng LỚN'), PATH((1, 11), (28, 11))], '''
- **Checkpoint 2** ở đầu phòng.
- Phòng nghỉ trước boss: Reploid #4, **nạp năng lượng lớn** (đầy máu), cửa boss.'''),

 Room('BOSS', 'Dynamo', 398, 8, 32, 16, 7, arena(32, 16, 14) + [E('*', 20, 9), sweep(3, 12, 2), X(5, 4, 'pha 2: laser quét nền')], '''
- **Đấu trường 28 ô**, kín, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (ném lưỡi đôi, chém, hồi máu bằng mảnh năng lượng).
- **Pha 2** (dưới 50% HP):
  - **Cụm laser quét nền** chạy ngang sân mỗi 8 giây. Dynamo nhảy qua và đánh người chơi đúng lúc phải né laser.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Zero Space 1', en='Zero Space 1', boss='Dynamo', act='Pháo đài X5', theme=THEME, capsule='',
 subtitle='Area 1: R1 → R2 (laser quét, hốc trú) → R3 (Cyberblock, leo) → R4 (Boost, laser đuổi) → Mini-boss  |  Area 2: R5 (laser đôi) → R6 (hành lang tử thần) → R7 trạm nạp → Boss',
 keep='Boss Dynamo, 6 cụm laser tử thần, trụ Cyberblock, bệ Boost và băng chuyền vẫn giữ. Màn pháo đài không có capsule, Heart Tank, Sub-Tank (theo dữ liệu game); thêm 4 Reploid và trạm nạp lớn.',
 concept='Lối vào không gian virus Zero. Toàn màn xoay quanh **6 cụm laser tử thần** quét ngang: đầu tiên trốn trong hốc, rồi chạy nhanh hơn laser, cuối cùng là chạy liên tục không chỗ trú.',
 areas=['**Area 1 – Cổng virus:** tím-xanh nhiễu, lưới mã. Laser quét có hốc trú, Cyberblock nhấp nháy, laser đuổi có Boost.',
        '**Area 2 – Lõi không gian:** tối hơn, laser đỏ rực. Laser đôi ngược chiều, rồi hành lang tử thần dài 80 ô.'],
 flow='nằm hốc tránh laser → leo Cyberblock → chạy Boost trước laser → mini-boss lõi tường lửa → chọn hốc giữa hai laser ngược chiều → chạy hết hành lang tử thần → boss',
 time='khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen',
 refs=['**X5, Zero Space 1:** cụm laser tử thần quét toàn màn, hốc trú ẩn, khuyên dùng Falcon/Fourth.',
       '**X6, màn Gate Lab:** tường nguy hiểm đuổi theo người chơi.',
       '**X8 16-bit demake:** đoạn đuổi do người chơi tự điều khiển, camera bám người chơi.',
       '**X Corrupted:** pháo đài kết hợp nhiều cơ chế đã học, không dạy lại.'],
 engine=['Laser quét toàn chiều cao: chạy theo lịch hoặc đuổi theo người chơi; không gây sát thương cho địch.',
         'Hốc trú trong sàn (laser đi qua phía trên).',
         'Cyberblock nhấp nháy (bệ ẩn hiện) và Cyberblock cố định.',
         'Tấm Boost, băng chuyền xuôi/ngược.',
         'Vệt dữ liệu nhiễu trên vách đẩy người chơi ra.',
         'Mini-boss Lõi tường lửa có khiên xoay.'],
 art=['**Tileset "Không gian virus" (Area 1):** 47 ô viền lưới dữ liệu tím, hốc trú, Cyberblock (3 khung).',
      '**Tileset "Lõi" (Area 2):** 47 ô viền tối có mạch đỏ.',
      '**Vật thể:** tường laser (4 khung), đèn báo, tấm Boost, băng chuyền dữ liệu.',
      '**Nền:** mã nhị phân trôi và khối pixel vỡ (2 lớp parallax cho cả màn).'],
)
STAGE['rooms'] = rooms
