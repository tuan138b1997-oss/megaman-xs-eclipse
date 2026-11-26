from kit import *

THEME = dict(bg1=(44, 44, 40), bg2=(40, 36, 34), rock1=(124, 118, 100), rock2=(116, 104, 92))
s3, p3 = shaft_down(24, 40, n=4)


def pits(xs, w=64, depth=2.5, pw=4):
    pts = [(0, 10)]
    for x in xs:
        pts += [(x, 10), (x, 10 + depth), (x + pw, 10 + depth), (x + pw, 10)]
    pts.append((w, 10))
    return F(*pts)


rooms = [
 Room('R1', 'Cổng nhà máy', 0, 50, 44, 14, 2, [
   B(0, 0, 44, 2), F((0, 10), (44, 10)), CV(14, 9.4, 16, 1), E('S', 38, 9), E('D', 8, 5), X(14, 7, 'băng chuyền rác'),
   PATH((1, 9), (43, 9))], '''
- **Mục đích:** mở đầu trong nhà máy tái chế. Giới thiệu băng chuyền rác và không khí ngột ngạt.
- **Địa hình:** cổng 44 ô, trần ở y 52, sàn ở y 60. Băng chuyền đẩy sang phải 80px/giây.
- **Địch:** 1 Drone dạng ruồi máy, 1 Sniper cuối phòng.
- **Trang trí:** núi rác ở nền, khối kim loại nén, đèn cảnh báo vàng-đen.'''),

 Room('R2', 'Trần ép 1', 44, 50, 64, 14, 3, [
   B(0, 0, 64, 2), BAR(0, 2, 64, 1.5, 'trash'), pits([10, 26, 42, 56]), X(2, 4.5, 'trần ép hạ xuống còn 1.5 ô mỗi 5s'),
   E('S', 44, 12), E('B', 34, 9), E('R', 28, 12), PATH((1, 9), (63, 9))], '''
- **Mục đích:** giới thiệu **trần ép toàn phòng**, khác với máy ép đơn lẻ.
- **Địa hình:**
  - Phòng 64 ô, sàn ở y 60. Có **4 hốc trú** sâu 2.5 ô, rộng 4 ô, cách nhau 12–16 ô.
- **Cơ chế – trần ép:**
  - Cả trần (sọc vàng-đen) hạ xuống chỉ còn cách sàn 1.5 ô, rồi nâng lên. Chu kỳ 5 giây: đứng yên 3.2 giây, hạ 0.8 giây, giữ 0.5 giây, nâng 0.5 giây.
  - Đứng trên sàn lúc trần hạ là mất mạng. Nằm trong hốc thì an toàn.
  - Đèn đỏ quay và còi hú 1 giây trước khi hạ.
- **Địch:**
  - 1 Brute giữa phòng: trần ép hạ cũng nghiền chết nó, nên có thể dụ nó.
  - 1 Sniper nằm sẵn trong hốc thứ ba: phải hạ nó mới vào hốc đó được.
- **Vật phẩm:** Reploid #1 trong hốc thứ hai.'''),

 Room('R3', 'Hố phế liệu', 108, 50, 24, 40, 4, s3 + [
   P(10, 16, 5, 'move'), X(10, 14.6, 'nam châm cẩu'), H('trash', 16, 26, 3, 3), X(14, 30, 'khối rác rơi 2.5s'), E('D', 12, 22), p3], '''
- **Mục đích:** đoạn dọc đi xuống, đổi nhịp sau phòng ép.
- **Địa hình:** hố rộng 20 ô, sâu 34 ô (từ y 60 xuống y 88). 4 kệ thép xếp zigzag.
- **Bẫy:**
  - **Khối rác nén** rơi từ miệng hố mỗi 2.5 giây, theo một trong 2 làn cố định. Bóng đổ trên kệ báo trước.
  - **Nam châm cẩu** chạy ngang giữa hố. Đứng lên được, nhưng nó hút giáp kim loại: đứng quá 2 giây thì bị kéo lên trên.
- **Địch:** 1 Drone ruồi.'''),

 Room('R4', 'Trần ép 2', 132, 78, 64, 14, 5, [
   B(0, 0, 64, 2), BAR(0, 2, 30, 1.5, 'trash'), BAR(34, 2, 30, 1.5, 'trash'), B(30, 2, 4, 6), pits([8, 20, 40, 52]),
   X(2, 4.5, 'trần A: 5s'), X(36, 4.5, 'trần B: 3.5s'), CV(42, 9.4, 18, -1),
   E('S', 56, 9), E('D', 24, 5), E('R', 10, 12), PATH((1, 9), (63, 9))], '''
- **Mục đích:** hai trần ép **lệch nhịp**, nên phải đọc hai đồng hồ cùng lúc.
- **Địa hình:**
  - Phòng 64 ô, sàn ở y 88. Một cột thép giữa phòng chia làm hai trần.
  - Mỗi nửa có 2 hốc trú.
- **Cơ chế:**
  - Trần A (nửa trái) chu kỳ 5 giây, trần B (nửa phải) chu kỳ 3.5 giây.
  - Dưới trần B có băng chuyền chạy ngược (đẩy sang trái 90px/giây), làm chậm đường chạy giữa hai hốc.
- **Địch:**
  - 1 Drone ruồi (không bị trần ép).
  - 1 Sniper cuối phòng, đứng trên đoạn an toàn.
- **Vật phẩm:** Reploid #2 trong hốc đầu tiên.'''),

 Room('MID', 'Máy ép chủ', 196, 74, 30, 16, 5, arena(30, 16, 14) + [E('M', 15, 4), BAR(2, 1, 26, 1, 'trash'), X(4, 10, 'trần hạ dần theo máu')], '''
- **Đấu trường 26 ô**, hai vách đá tường được.
- **Máy ép chủ** là khối ép khổng lồ gắn trên trần, có hai tay kẹp.
- **Đòn đánh:**
  - Đập xuống một nửa sân (trái hoặc phải), báo trước bằng bóng đổ 0.8 giây.
  - Hai tay kẹp quét ngang sát sàn: nhảy qua.
  - Mỗi lần mất 1/3 máu, **cả trần hạ xuống 2 ô**: đấu trường thấp dần, khó đá tường.
- **Điểm yếu:** lõi thủy lực lộ ra ở mặt dưới sau mỗi cú đập.
- **Phần thưởng:** mở bãi Ride Armor. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Bãi rác Ride Armor', 226, 72, 64, 18, 5, [
   B(0, 0, 64, 2), F((0, 16), (64, 16)), CW(18, 8, 8), CW(40, 8, 8), BAR(32, 2, 6, 3, 'trash'), BAR(46, 2, 6, 3, 'trash'),
   B(42, 4, 12, 1), P(56, 6, 6), X(31, 5.6, 'ép 1'), X(46, 5.6, 'ép 2'), X(42, 2.6, 'khoang trên'),
   E('C', 2, 15), E('V', 6, 15), E('B', 28, 15), E('R', 12, 15), E('A', 46, 3), E('T', 59, 5),
   PATH((1, 15), (63, 15)), ALT((40, 15), (42, 6), (46, 3)), ALT((52, 15), (56, 8), (59, 5))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** cưỡi Ride Armor đục xuyên **tường rác**.
- **Địa hình:**
  - Bãi rác 64 ô, sàn ở y 88. 2 bức tường rác nén cao 8 ô chắn hết đường.
  - X đi bộ không phá được tường rác: phải dùng Ride Armor (4 cú đấm mỗi tường).
  - Giữa hai tường có 2 máy ép nhỏ dập theo nhịp (chờ 1.5 giây, dập 0.3 giây), Ride Armor chịu được 2 cú.
- **Địch:** 1 Brute giữa bãi.
- **Vật phẩm:** Reploid #3 đầu bãi.
- **Lối phụ (Capsule Shadow Foot):**
  - Đấm vỡ **tường rác thứ hai** từ phía dưới thì lộ ra một khoang nhỏ phía trên, kẹp giữa 2 máy ép (x ≈ 268–280, y ≈ 74–76).
  - Nhảy Ride Armor lên đúng lúc hai máy ép cùng nâng lên. Capsule ở trong khoang.
- **Lối phụ (Sub-Tank):** kệ thép cuối bãi (x ≈ 282, y ≈ 78). Đứng trên Ride Armor nhảy lên rồi bật ra khỏi xe để với tới.'''),

 Room('R6', 'Hầm tường ép đuổi', 290, 76, 80, 14, 7, [
   B(0, 0, 80, 2), F((0, 12), (80, 12)), BAR(0, 2, 2, 10, 'trash'), AR(3, 7, 6, 0, 'alarm'), X(3, 3, 'tường ép 90 → 120px/s'),
   B(16, 2, 6, 6), B(34, 9, 4, 3), CV(42, 11.4, 14, -1), B(60, 2, 8, 7), B(72, 9, 3, 3), H('spike', 46, 11, 4, 1),
   P(26, 3, 4), E('D', 30, 7), E('D', 64, 10.6), E('H', 27.5, 2),
   PATH((3, 11), (15, 11), (19, 10.5), (33, 11), (36, 8), (39, 11), (45, 11), (48, 9), (59, 11), (64, 10.5), (71, 11), (73, 8), (79, 11)),
   ALT((24, 11), (26, 4), (28, 2))], '''
- **Mục đích:** cao trào của màn. Bị **tường ép đuổi** dọc một đường hầm dài 80 ô.
- **Cơ chế – tường ép đuổi:**
  - Khi người chơi bước vào, bức tường ép phía trái bắt đầu tiến sang phải 90px/giây, tăng lên 120px/giây ở nửa sau.
  - Bị kẹp giữa tường ép và vật cản là mất mạng.
  - Khác đoạn tự cuộn của X6 gốc: camera vẫn bám người chơi, người chơi được chạy nhanh hơn tường để tạo khoảng cách.
- **Vật cản:**
  - Trần thấp (khe 4 ô): phải lướt.
  - Khối thép thấp: nhảy qua.
  - Đoạn băng chuyền chạy ngược có gai ở giữa.
  - Khối rác cuối hầm, phải bắn 3 phát mới vỡ.
- **Địch:** 2 Drone ruồi, chỉ gây vướng: bắn hạ thì mất thời gian, lướt qua thì mất máu.
- **Lối phụ (Heart Tank):**
  - Một gờ cao trên trần ở x ≈ 316 (y ≈ 79), ngay sau khe trần thấp đầu tiên.
  - Lên lấy mất khoảng 1.5 giây: chỉ kịp nếu đã chạy nhanh từ đầu hầm. Giáp Blade lướt trên không giúp tiết kiệm thời gian.'''),

 Room('R7', 'Lò đốt', 370, 78, 50, 14, 6, [
   B(0, 0, 50, 2), F((0, 10), (50, 10)), H('fire', 12, 7, 3, 3), H('fire', 26, 7, 3, 3), H('fire', 38, 7, 3, 3), X(10, 4, 'lưới lửa phụt 1s mỗi 2.5s, lệch pha'),
   E('C', 2, 9), E('S', 46, 9), E('D', 32, 4), PATH((1, 9), (49, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: lửa theo nhịp sau đoạn bị đuổi, cho người chơi thở chậm lại.
- **Địa hình:** hành lang lò đốt 50 ô, sàn ở y 88.
- **Bẫy:** 3 lưới sàn phụt lửa cao 3 ô, phụt 1 giây mỗi 2.5 giây, lệch pha nhau.
- **Địch:** 1 Drone ruồi, 1 Sniper cuối hành lang.'''),

 rest('R8', 'Phòng điều khiển', 420, 78, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Metal Shark Player', 450, 74, 32, 16, 6, arena(32, 16, 14) + [BAR(2, 1, 28, 1, 'trash'), E('*', 18, 9), X(4, 4, 'pha 2: khối rác rơi')], '''
- **Đấu trường 28 ô**, hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (bơi trong rác, Metal Anchor, cắn).
- **Pha 2** (dưới 50% HP):
  - **Khối rác nén rơi từ trần** mỗi 4 giây (bóng đổ báo trước). Khối rơi xong nằm lại 6 giây làm vật cản, có thể đứng lên.
  - Metal Shark bơi dưới sàn và trồi lên dưới chân người chơi.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Phòng thí nghiệm tái chế', en='Recycle Lab', boss='Metal Shark Player', act='Act II · X6', theme=THEME, capsule='Shadow Foot',
 subtitle='Area 1 (dây chuyền ép): R1 → R2 (trần ép) → R3 (hố, đi xuống) → R4 (2 trần lệch nhịp) → Mini-boss  |  Area 2 (bãi rác): R5 (Ride Armor) → R6 (tường ép đuổi) → R7 → R8 → Boss',
 keep='Boss, capsule Shadow Foot, trần máy ép thủy lực có hốc trú, Ride Armor Pod và tường rác vẫn giữ; đoạn tự cuộn được làm lại thành tường ép đuổi (người chơi tự điều khiển); thêm 4 Reploid, Heart Tank, Sub-Tank và thay địa hình.',
 concept='Nhà máy tái chế nghiền mọi thứ thành khối kim loại. Cả màn là **cảm giác bị nghiền**: trần hạ xuống, rác rơi, tường ép đuổi theo. Người chơi phải tìm hốc trú và chạy theo nhịp máy.',
 areas=['**Area 1 – Dây chuyền ép:** vàng-đen cảnh báo, đèn quay đỏ. Dạy trần ép toàn phòng, hốc trú, rác rơi, hai trần lệch nhịp.',
        '**Area 2 – Bãi rác và hầm:** núi rác, ánh lửa lò đốt. Ride Armor phá tường rác, rồi bị tường ép đuổi dọc đường hầm.'],
 flow='trốn trần ép trong hốc → xuống hố rác → đọc hai trần lệch nhịp → mini-boss máy ép → cưỡi Ride Armor phá tường rác → chạy trước tường ép → lò đốt → boss có rác rơi',
 time='khoảng 6–7 phút lần đầu, khoảng 3 phút khi đã quen',
 refs=['**X6, màn Metal Shark Player:** trần máy ép thủy lực với hốc trú, Ride Armor phá tường rác giấu capsule Shadow Foot.',
       '**X5, màn Burn Dinorex / màn mẫu Lò Nham Thạch:** máy ép theo nhịp (ở đây mở rộng thành cả trần).',
       '**X8 16-bit demake:** đoạn tự cuộn làm lại thành đoạn người chơi tự điều khiển; ở đây là tường đuổi.',
       '**X Corrupted:** dùng bẫy môi trường để hạ địch (trần ép nghiền Brute).'],
 engine=['Trần ép toàn phòng: hạ/nâng theo lịch, giết mọi thứ không nằm trong hốc.',
         'Khối rác rơi theo làn và lịch; nam châm cẩu kéo người chơi lên.',
         'Tường rác chỉ Ride Armor phá được.',
         'Tường ép đuổi: chạy theo người chơi với tốc độ tăng dần, kẹp là chết.',
         'Lưới sàn phụt lửa theo nhịp.',
         'Mini-boss Máy ép chủ: trần đấu trường hạ dần theo máu.'],
 art=['**Tileset "Dây chuyền" (Area 1):** 47 ô viền thép sọc vàng-đen, trần ép, hốc trú, băng chuyền.',
      '**Tileset "Bãi rác" (Area 2):** 47 ô viền rác nén, tường rác (3 trạng thái vỡ), lưới lò đốt.',
      '**Vật thể:** khối rác nén, nam châm cẩu, tường ép đuổi (4 khung), lửa lò (4 khung), đèn quay.',
      '**Nền:** Area 1: dây chuyền và băng tải xa (2 lớp parallax). Area 2: núi rác và lò đốt (2 lớp).'],
)
STAGE['rooms'] = rooms
