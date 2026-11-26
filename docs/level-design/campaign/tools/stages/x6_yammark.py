from kit import *

THEME = dict(bg1=(30, 50, 36), bg2=(26, 32, 34), rock1=(92, 86, 64), rock2=(80, 84, 88))
s3, p3 = shaft_up(24, 46, n=4)
for i, g in enumerate(s3):
    if g[0] == 'plat': s3[i] = ('plat', 'holo') + g[2:]

rooms = [
 Room('R1', 'Bờ sông', 0, 50, 44, 16, 2, [
   F((0, 12), (44, 12)), B(16, 9, 5, 3), E('S', 36, 11), E('D', 26, 5), X(3, 4, 'chuồn chuồn máy'), PATH((1, 11), (43, 11))], '''
- **Mục đích:** mở đầu trong rừng Amazon, làm quen **chuồn chuồn máy** (Drone bay đường sóng, có thể đổi hướng bất ngờ).
- **Địa hình:** bờ sông 44 ô, mặt đất ở y 62, một tảng đá thấp.
- **Địch:** 1 Drone chuồn chuồn, 1 Sniper cuối bờ.
- **Trang trí:** cây khổng lồ, dây leo, hoa máy phát sáng, sương mù sát mặt đất.'''),

 Room('R2', 'Sông gỗ trôi', 44, 50, 70, 18, 3, [
   F((0, 12), (6, 12)), F((64, 12), (70, 12)), H('water', 6, 13, 58, 5), AR(20, 16, 8, 0, 'current'),
   P(10, 12, 6, 'move'), P(24, 12, 6, 'move'), P(38, 12, 6, 'move'), P(52, 12, 6, 'move'),
   X(8, 16, 'dòng xiết: rơi xuống là bị cuốn'), E('D', 20, 5), E('D', 46, 4), E('R', 67, 11),
   PATH((1, 11), (6, 11), (13, 11), (27, 11), (41, 11), (55, 11), (69, 11))], '''
- **Mục đích:** nhảy trên **khúc gỗ trôi** xuôi dòng.
- **Địa hình:** sông rộng 58 ô. Rơi xuống nước là bị dòng xiết cuốn đi (mất mạng).
- **Cơ chế:**
  - 4 khúc gỗ trôi sang phải 70px/giây, sinh ra liên tục ở đầu sông.
  - Khúc gỗ chìm xuống nửa ô khi đứng lên, rồi nổi lại.
  - Đứng yên trên gỗ thì vẫn sang được bờ bên kia, nhưng chuồn chuồn sẽ lao vào.
- **Địch:** 2 Drone chuồn chuồn.
- **Vật phẩm:** Reploid #1 ở bờ bên kia.'''),

 Room('R3', 'Cây hoa nở', 114, 20, 24, 46, 4, s3 + [X(3, 40, 'hoa nở 3s / khép 2s'), E('D', 12, 20), p3], '''
- **Mục đích:** đoạn dọc. Leo trên các **bông hoa máy** nở và khép theo nhịp.
- **Địa hình:** khoảng trống giữa hai thân cây, rộng 20 ô, cao 42 ô (từ y 64 lên y 27).
- **Cơ chế – hoa nở:** 4 bông hoa làm bệ. Nở 3 giây (đứng được), khép 2 giây (rơi xuyên qua). Các bông lệch pha nhau từ dưới lên.
- **Địch:** 1 Drone chuồn chuồn.
- **Giáp hỗ trợ:** hai vách là thân cây, đá tường được: có thể bỏ qua hoa và leo thẳng.'''),

 Room('R4', 'Tán thấp', 138, 17, 50, 14, 4, [
   F((0, 10), (50, 10)), H('thorn', 18, 9, 6, 1), P(18, 5, 6), E('B', 32, 9), E('S', 46, 9), PATH((1, 9), (17, 9), (21, 4), (25, 9), (49, 9))], '''
- **Mục đích:** đoạn chạy ngắn trước mini-boss.
- **Địa hình:** tán cây thấp 50 ô, mặt cành ở y 27. Một bụi gai có cành ngang phía trên để nhảy qua.
- **Địch:** 1 Brute, 1 Sniper.'''),

 Room('MID', 'Bọ Nightmare chúa', 188, 13, 30, 16, 5, arena(30, 16, 14) + [E('M', 15, 5), X(4, 10, 'đẻ bọ con mỗi 6s')], '''
- **Đấu trường 26 ô** trong hốc cây, hai vách đá tường được.
- **Bọ Nightmare chúa** bám trên trần hốc cây.
- **Đòn đánh:**
  - Đẻ 3 bọ con mỗi 6 giây. Bọ con bò dọc sàn và vách.
  - Phun tơ: trúng thì chậm 50% trong 2 giây.
  - Rơi xuống đập sàn khi máu dưới một nửa.
- **Điểm yếu:** bụng, lộ ra lúc đẻ bọ con.
- **Phần thưởng:** mở lối vào ngã ba. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Ngã ba', 218, 5, 20, 40, 5, [
   B(0, 0, 20, 1), B(0, 0, 2, 15), B(0, 23, 2, 17), B(18, 1, 2, 4), B(18, 9, 2, 20), F((0, 38), (20, 38)), B(2, 22, 12, 1),
   P(12, 16, 5), P(4, 10, 5), H('spike', 2, 37, 16, 1),
   E('C', 4, 21), E('R', 14, 21), X(3, 24, 'sàn có lỗ: rơi xuống nhánh dưới'), B(18, 35, 2, 3),
   PATH((1, 21), (8, 21), (14, 15), (6, 9), (15, 5), (19.5, 4)), ALT((16, 23), (16, 33), (19.5, 34))], '''
- **Checkpoint 1** ở giữa phòng (sàn y 27).
- **Mục đích:** ngã ba chia màn làm **2 nhánh độc lập** dài khoảng 60 ô, gặp lại nhau ở thác nước (R7).
- **Địa hình:**
  - Hốc cây rộng 16 ô.
  - Đi lên (2 kệ, đá tường) ra **nhánh tán cây** ở y 10.
  - Rơi qua lỗ sàn bên phải xuống **nhánh hang** ở y 40.
- **Vật phẩm:** Reploid #2 cạnh checkpoint.
- **Ghi chú:** mỗi nhánh có một vật phẩm riêng. Muốn lấy cả hai thì đi một nhánh, chết hoặc quay lại checkpoint 1 rồi đi nhánh kia (vật phẩm đã lấy được giữ lại).'''),

 Room('R6', 'Nhánh tán cây', 238, 0, 60, 14, 6, [
   F((0, 10), (8, 10), None, (16, 10), (28, 10), None, (40, 10), (60, 10)), H('void', 8, 11, 8, 3), H('void', 28, 11, 12, 3),
   P(10, 6, 4, 'move'), P(31, 5, 5, 'move'), P(52, 3, 6), X(9, 3, 'dây leo đu'), E('D', 22, 4), E('D', 46, 5), E('A', 55, 2),
   PATH((1, 9), (8, 9), (12, 5), (17, 9), (28, 9), (33, 4), (41, 9), (59, 9)), ALT((48, 9), (51, 4), (55, 2))], '''
- **Nhánh trên.** Chạy trên các cành lớn ngoài trời, có 2 khe phải đu dây leo qua.
- **Địa hình:**
  - Cành ở y 10, dài 60 ô. 2 khe rộng 8 và 12 ô, rơi là mất mạng.
  - Mỗi khe có một **dây leo đu** qua lại (biên độ 4 ô, chu kỳ 3 giây). Bám vào thì đu theo, nhả nút để bay ra theo đà.
- **Địch:** 2 Drone chuồn chuồn.
- **Lối phụ (Capsule Blade Foot):** cuối nhánh có một nhánh cây cao (x ≈ 290, y ≈ 3). Đá tường thân cây ở cuối phòng để lên.'''),

 Room('R6b', 'Nhánh hang', 238, 30, 60, 14, 6, [
   B(0, 0, 60, 2), F((0, 10), (60, 10)), Z('dark', 6, 2, 46, 8, 'hang tối, nước nhỏ giọt'), H('spike', 20, 9, 8, 1),
   P(20, 5, 8, 'break'), P(40, 6, 6), E('B', 34, 9), E('H', 43, 5), PATH((1, 9), (19, 9), (22, 4), (28, 9), (59, 9)), ALT((36, 9), (40, 5), (43, 5))], '''
- **Nhánh dưới.** Hang ẩm, tối, trần thấp.
- **Địa hình:** hang 60 ô, sàn ở y 40, một hố gai có tấm đá mỏng phía trên (sập 0.5 giây sau khi đứng).
- **Cơ chế:** hang tối, chỉ thấy quanh X 6 ô. Giọt nước rơi từ trần chỉ làm hiệu ứng nhưng che tầm nhìn.
- **Địch:** 1 Brute giữa hang.
- **Lối phụ (Heart Tank):** trên một gờ đá ngay phía sau Brute (x ≈ 281, y ≈ 35). Phải hạ Brute rồi đá tường vách hang lên.'''),

 Room('R7', 'Thác nước', 298, 4, 26, 48, 7, [
   B(0, 0, 26, 1), B(0, 7, 2, 23), B(0, 37, 2, 11), B(2, 6, 6, 1), B(2, 36, 6, 1), B(0, 46, 26, 2),
   B(24, 1, 2, 15), B(24, 23, 2, 23), B(18, 22, 6, 1), Z('water', 10, 1, 6, 45, 'thác'), AR(13, 8, 0, 6, 'current'),
   H('trash', 11, 14, 3, 1), H('trash', 11, 30, 3, 1), X(16, 30, 'gỗ rơi theo thác 2s'),
   P(16, 14, 5), P(3, 18, 5), P(3, 28, 5), P(17, 30, 5), E('D', 8, 12), E('T', 13, 43),
   PATH((1, 5), (7, 5), (18, 13), (21, 21), (25.5, 21)), PATH((1, 35), (7, 35), (5, 27), (19, 29), (21, 21)),
   ALT((5, 27), (8, 38), (13, 43))], '''
- **Mục đích:** cao trào của màn. Hai nhánh gặp nhau ở một thác nước dọc. Nhánh trên phải đi xuống, nhánh dưới phải leo lên, cả hai tới cùng một cửa ra ở giữa vách phải (y 26).
- **Địa hình:** khe đá rộng 22 ô, cao 44 ô. Thác nước rộng 6 ô đổ thẳng giữa khe.
- **Cơ chế:**
  - **Đứng trong thác** thì bị đẩy xuống 120px/giây, không nhảy lên được.
  - **Khúc gỗ rơi theo thác** mỗi 2 giây: trúng là mất 1/4 máu và bị đẩy văng ra.
  - Đi qua thác phải lướt ngang thật nhanh, chọn lúc giữa hai khúc gỗ.
- **Địch:** 1 Drone chuồn chuồn.
- **Lối phụ (Sub-Tank):** **sau màn thác** ở đáy khe có một hốc (x ≈ 311, y ≈ 47). Thả người theo dòng thác xuống đáy là rơi thẳng vào hốc. Ra lại bằng cách đá vách trái.'''),

 Room('R8', 'Đền rừng', 324, 16, 52, 14, 6, [
   F((0, 10), (52, 10)), B(0, 0, 52, 2), P(14, 6, 6, 'holo'), P(30, 5, 6, 'holo'), H('thorn', 12, 9, 26, 1),
   E('C', 2, 9), E('R', 44, 9), E('S', 48, 9), E('D', 24, 4), PATH((1, 9), (11, 9), (16, 5), (31, 4), (40, 9), (51, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Mục đích:** kết hợp: bụi gai dưới, hoa nở/khép phía trên.
- **Địa hình:** sân đền đổ nát 52 ô, giữa là bãi gai 26 ô, chỉ có 2 bông hoa máy để bước qua (nở 3 giây, khép 2 giây).
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #3 cuối sân.'''),

 rest('R9', 'Cổng tổ', 376, 16, '''
- Phòng nghỉ trước boss: Reploid #4, nạp năng lượng nhỏ, cửa boss.'''),

 Room('BOSS', 'Commander Yammark', 406, 12, 32, 16, 6, arena(32, 16, 14, ceil=False) + [
   P(6, 6, 5, 'holo'), P(21, 6, 5, 'holo'), E('*', 16, 4), X(4, 10, 'pha 2: hoa khép, chuồn chuồn bảo vệ')], '''
- **Đấu trường 28 ô**, có 2 bông hoa máy làm bệ trên cao.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (chuồn chuồn hộ vệ, lao chéo, bắn đạn).
- **Pha 2** (dưới 50% HP):
  - Hoa nở/khép theo nhịp như R3 (nở 3 giây, khép 2 giây).
  - 3 chuồn chuồn hộ vệ bay vòng quanh Yammark, chắn đạn. Hạ chuồn chuồn trước rồi mới đánh boss.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Khu Amazon', en='Amazon Area', boss='Commander Yammark', act='Act II · X6', theme=THEME, capsule='Blade Foot',
 subtitle='Area 1 (sông và tán thấp): R1 → R2 (gỗ trôi) → R3 (hoa nở) → R4 → Mini-boss  |  Area 2: R5 ngã ba → R6 nhánh tán (capsule) hoặc R6b nhánh hang (Heart Tank) → R7 thác → R8 → R9 → Boss',
 keep='Boss, capsule Blade Foot, rừng tách 2 nhánh ở mid-checkpoint (nhánh trên: Blade Foot, nhánh dưới: Heart Tank) và bọ Nightmare vẫn giữ; thêm 4 Reploid, Sub-Tank và thay địa hình.',
 concept='Rừng Amazon nhiễm virus Nightmare. Điểm khác biệt là **màn tách đôi**: sau ngã ba người chơi chọn nhánh tán cây hoặc nhánh hang, mỗi nhánh giữ một vật phẩm, rồi hai nhánh gặp nhau ở thác nước.',
 areas=['**Area 1 – Sông và tán thấp:** xanh lá, sương, nắng lọt. Dạy gỗ trôi, hoa nở/khép, chuồn chuồn máy.',
        '**Area 2 – Hai nhánh và thác:** nhánh trên ngoài trời có dây leo đu, nhánh dưới là hang tối. Cả hai đổ về thác nước.'],
 flow='nhảy gỗ trôi qua sông → leo trên hoa nở → mini-boss bọ chúa → chọn nhánh ở ngã ba → đu dây leo hoặc lần trong hang tối → vượt thác có gỗ rơi → boss có chuồn chuồn hộ vệ',
 time='khoảng 6–7 phút lần đầu (một nhánh), khoảng 3 phút khi đã quen',
 refs=['**X6, màn Commander Yammark:** rừng tách 2 tầng ở mid-checkpoint, mỗi tầng một vật phẩm.',
       '**X (SNES), màn Sting Chameleon:** rừng có hang, lối phụ phía trên.',
       '**X8, màn Bamboo Pandamonium:** vật cản rơi theo nhịp trên đường leo.',
       '**X Corrupted:** nhiều đường đi cùng tới một điểm hội tụ, mỗi đường thưởng một thứ.'],
 engine=['Khúc gỗ trôi (bệ di động sinh liên tục, chìm nhẹ khi đứng). Nước chảy xiết: rơi là mất mạng.',
         'Bệ hoa nở/khép theo nhịp (bệ ẩn hiện).',
         'Dây leo đu: bám, đu theo con lắc, nhả để bay theo đà.',
         'Vùng thác nước đẩy xuống; vật rơi theo thác theo lịch.',
         'Vùng tối trong hang (tầm nhìn quanh X).',
         'Mini-boss Bọ Nightmare chúa đẻ bọ con.'],
 art=['**Tileset "Rừng Amazon" (Area 1):** 47 ô viền đất rừng, cành lớn, hoa máy (3 khung nở/khép), mặt sông (4 khung).',
      '**Tileset "Hang và thác" (Area 2):** 47 ô viền đá ẩm, thác nước (4 khung), dây leo.',
      '**Vật thể:** khúc gỗ, dây leo đu, bọ con, chuồn chuồn hộ vệ.',
      '**Nền:** Area 1: rừng xa và sương (2 lớp parallax). Area 2: vách hang và tia nắng xuyên thác (2 lớp).'],
)
STAGE['rooms'] = rooms
