from kit import *

THEME = dict(bg1=(50, 30, 46), bg2=(44, 26, 42), rock1=(126, 96, 120), rock2=(116, 86, 114))
s5, p5 = shaft_up(24, 48, n=5)


def crystal(x, y): return H('mine', x, y, 1, 1)


rooms = [
 Room('R1', 'Sảnh Gate', 0, 40, 36, 14, 4, [
   B(0, 0, 36, 2), F((0, 10), (36, 10)), crystal(18, 8), E('R', 4, 9), E('S', 32, 9), X(14, 6, 'tinh thể Nightmare'), PATH((1, 9), (35, 9))], '''
- **Mục đích:** tầng 3 phòng thí nghiệm Gate. Giới thiệu **tinh thể Nightmare**: bắn hoặc chạm thì nổ sau 0.5 giây, bán kính 2 ô.
- **Địa hình:** sảnh 36 ô, trần ở y 42, sàn ở y 50.
- **Địch:** 1 Sniper. Dụ nó tới gần tinh thể rồi bắn tinh thể.
- **Vật phẩm:** Reploid #1 ở đầu sảnh.
- **Ghi chú:** màn này giữ **capsule bí mật Ultimate Armor** (theo dữ liệu game). Không có Heart Tank/Sub-Tank.'''),

 Room('R2', 'Biển gai trần', 36, 34, 60, 24, 6, [
   F((0, 16), (8, 16)), F((52, 16), (60, 16)), H('spike', 8, 22, 44, 2), B(0, 0, 60, 2), H('spike', 18, 2, 6, 1),
   Z('grav', 8, 2, 44, 20, 'vùng đảo trọng lực (công tắc)'), P(14, 15, 4, 'move'), P(26, 13, 4, 'move'), P(38, 15, 4, 'move'),
   E('K', 6, 15), E('A', 34, 2.6), E('D', 22, 8), E('D', 44, 8),
   PATH((1, 15), (8, 15), (16, 14), (28, 12), (40, 14), (53, 15), (59.5, 15)), ALT((6, 15), (10, 2.6), (17, 2.6), (21, 4.5), (25, 2.6), (34, 2.6))], '''
- **Mục đích:** đường chính đi trên **bệ di động** qua biển gai. **Lối bí mật** là đi lộn ngược trên trần.
- **Địa hình:** biển gai 44 ô. 3 bệ di động ở giữa chiều cao. Trần liền, có một mảng gai 6 ô.
- **Đường chính:** nhảy qua 3 bệ di động (chạy ngang 6 ô, chu kỳ 3 giây).
- **Lối phụ (Capsule bí mật Ultimate Armor):**
  - Ở mép vực có một **công tắc trọng lực** gắn trên vách, trông giống đèn trang trí. Bắn vào thì trọng lực trong vùng đảo ngược.
  - Đi lộn ngược trên trần, nhảy (xuống dưới) qua mảng gai trần, tới capsule ở giữa trần (x ≈ 70, y ≈ 41).
  - Bắn công tắc lần nữa (bắn được từ trên trần) để trở lại bình thường, rơi xuống bệ di động.
  - Điều kiện mở capsule giữ nguyên theo dữ liệu game.
- **Địch:** 2 Drone, miễn đảo trọng lực.'''),

 Room('R3', 'Phòng tinh thể', 96, 40, 56, 14, 6, [
   B(0, 0, 56, 2), F((0, 10), (56, 10)), B(20, 2, 4, 6), crystal(19, 8), crystal(25, 8), B(40, 6, 4, 4), crystal(39, 8), crystal(42, 5),
   X(18, 11.4, 'khối chắn: nổ tinh thể để phá'), E('B', 32, 9), E('R', 48, 9), E('D', 12, 5),
   PATH((1, 9), (18, 9), (25, 9), (38, 9), (45, 9), (55, 9))], '''
- **Mục đích:** dùng tinh thể nổ để **phá khối chắn**.
- **Địa hình:** phòng 56 ô, 2 khối chắn đường. Cạnh mỗi khối có tinh thể.
- **Cơ chế:** bắn tinh thể rồi lùi ra 2 ô. Vụ nổ phá khối chắn. Nổ lan: một tinh thể nổ làm tinh thể gần đó (trong 3 ô) nổ theo sau 0.3 giây.
- **Địch:** 1 Drone, 1 Brute giữa hai khối chắn.
- **Vật phẩm:** Reploid #2 cuối phòng.'''),

 Room('MID', 'Tinh thể mẹ', 152, 36, 30, 16, 6, arena(30, 16, 14) + [E('M', 15, 6), crystal(6, 10), crystal(23, 10), X(4, 3, 'mọc tinh thể con quanh sân')], '''
- **Đấu trường 26 ô**, kín, hai vách đá tường được.
- **Tinh thể mẹ** treo giữa trần, mọc tinh thể con trên sàn và vách.
- **Đòn đánh:**
  - Mọc 3 tinh thể con ở chỗ người chơi vừa đứng (1 giây sau).
  - Phát sóng làm mọi tinh thể con nổ cùng lúc.
- **Điểm yếu:** chỉ bị thương bởi vụ nổ của tinh thể con ngay dưới nó. Dụ nó mọc tinh thể giữa sân rồi bắn.
- **Phần thưởng:** mở hành lang tinh thể. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R4', 'Hành lang tinh thể', 182, 40, 60, 14, 6, [
   B(0, 0, 60, 2), F((0, 10), (60, 10)), crystal(14, 8), crystal(17, 8), crystal(30, 3), crystal(33, 3), crystal(44, 8), crystal(47, 8),
   X(12, 6, 'tinh thể mọc lại sau 4s'), E('C', 2, 9), E('S', 56, 9), E('D', 38, 5), E('R', 24, 9), PATH((1, 9), (59, 9))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** di chuyển giữa các cụm tinh thể **mọc lại**.
- **Cơ chế:** cụm tinh thể nổ xong thì mọc lại sau 4 giây. Phải kích nổ từ xa rồi chạy qua trước khi nó mọc lại. Cụm trên trần rơi xuống khi nổ.
- **Địch:** 1 Drone, 1 Sniper.
- **Vật phẩm:** Reploid #3 giữa hành lang.'''),

 Room('R5', 'Giếng tinh thể', 242, 4, 24, 48, 8, s5 + [
   crystal(2.5, 30), crystal(20.5, 22), crystal(2.5, 14), crystal(11, 34), crystal(12, 18), X(3, 42, 'chuỗi nổ dây chuyền từ đáy lên mỗi 8s'),
   E('D', 8, 24), E('D', 16, 10), p5], '''
- **Mục đích:** cao trào của màn. Leo giếng trong khi **chuỗi tinh thể nổ dây chuyền** từ đáy lên.
- **Địa hình:** giếng rộng 20 ô, cao 44 ô (từ y 50 lên y 7). 5 kệ, tinh thể bám trên vách và giữa giếng.
- **Cơ chế:**
  - Mỗi 8 giây một vụ nổ ở đáy giếng, lan lên theo các tinh thể (mỗi bước 0.3 giây).
  - Đứng cạnh tinh thể khi sóng nổ tới là mất 1/3 máu và bị đẩy văng.
  - Người chơi có thể chủ động bắn nổ tinh thể phía trên để "cắt" chuỗi, tạo vùng an toàn.
- **Địch:** 2 Drone.'''),

 Room('R6', 'Trạm hồi máu', 266, 1, 30, 14, 2, [
   B(0, 0, 30, 2), F((0, 10), (30, 10)), BAR(29, 2, 1, 8, 'door'), E('C', 2, 9), E('R', 15, 9), X(4, 5, 'hồi máu ĐẦY'), PATH((1, 9), (28, 9))], '''
- **Checkpoint 2** ở đầu phòng.
- **Trạm hồi máu đầy** trước phòng Gate (theo dữ liệu game): Reploid #4, hồi đầy máu và năng lượng vũ khí.'''),

 Room('BOSS', 'Gate', 296, -3, 34, 18, 7, [
   F((0, 14), (10, 14)), F((24, 14), (34, 14)), H('void', 10, 15, 14, 3), P(12, 9, 3), P(16, 6, 3), P(20, 9, 3), B(0, 0, 2, 14), B(32, 0, 2, 14),
   E('*', 17, 3), X(10, 16, 'vực giữa sàn'), PATH((3, 13), (13, 8), (17, 5), (21, 8), (31, 13))], '''
- **Đấu trường 30 ô có vực thẳm giữa sàn** (rộng 14 ô) và **3 bệ lơ lửng** phía trên vực (theo dữ liệu game). Hai vách đá tường được.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (tinh thể Nightmare, bắn chùm, dịch chuyển).
- **Pha 2** (dưới 50% HP):
  - Gate bắn tinh thể lên 3 bệ: bệ có tinh thể nổ thì tắt 3 giây.
  - Người chơi phải nhảy qua vực bằng các bệ còn lại để đuổi theo Gate.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Phòng thí nghiệm Gate 3', en="Gate's Secret Lab 3", boss='Gate', act='Pháo đài X6', theme=THEME, capsule='bí mật Ultimate Armor',
 subtitle='Area 1: R1 → R2 (biển gai, lối trần có capsule bí mật) → R3 (tinh thể) → Mini-boss  |  Area 2: R4 → R5 (giếng nổ dây chuyền) → R6 hồi máu → Boss (vực giữa sàn)',
 keep='Boss Gate, vùng đảo trọng lực giấu capsule bí mật Ultimate Armor, tinh thể Nightmare nổ, trạm hồi máu đầy và đấu trường có vực giữa sàn + 3 bệ nổi vẫn giữ. Không có Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss.',
 concept='Tầng 3, phòng riêng của Gate. Màn xoay quanh **tinh thể Nightmare nổ dây chuyền**: vừa là bẫy vừa là công cụ phá đường. Lối trần bí mật ở đầu màn giữ capsule Ultimate Armor.',
 areas=['**Area 1 – Phòng thí nghiệm:** hồng tím, tinh thể phát sáng. Biển gai có lối trần bí mật, phòng tinh thể phá khối chắn.',
        '**Area 2 – Lõi phòng Gate:** hành lang tinh thể mọc lại, giếng nổ dây chuyền, trạm hồi máu.'],
 flow='kích nổ tinh thể → chọn bệ di động hoặc đảo trọng lực lên trần lấy capsule → nổ tinh thể phá khối chắn → mini-boss tinh thể mẹ → hành lang tinh thể mọc lại → leo giếng nổ dây chuyền → Gate',
 time='khoảng 5–6 phút lần đầu, khoảng 2.5 phút khi đã quen',
 refs=['**X6, Gate Lab 3:** vùng đảo trọng lực trên biển gai giấu capsule Ultimate Armor, trạm hồi máu, đấu trường có vực + 3 bệ.',
       '**X5, Zero Space 3:** đi lộn ngược trên trần lấy capsule bí mật (ở đây là lối phụ, còn đường chính dùng bệ di động).',
       '**X3, màn Doppler:** vật nổ phá vật cản.',
       '**X Corrupted:** công tắc bí mật ngụy trang thành đồ trang trí.'],
 engine=['Tinh thể Nightmare: nổ khi bị bắn/chạm, nổ lan trong bán kính, mọc lại theo thời gian; phá được khối chắn.',
         'Vùng đảo trọng lực bật bằng công tắc ngụy trang.',
         'Bệ di động trên biển gai.',
         'Trạm hồi máu đầy.',
         'Mini-boss Tinh thể mẹ (chỉ bị thương bởi vụ nổ).',
         'Đấu trường có vực giữa và 3 bệ có thể tắt.'],
 art=['**Tileset "Phòng Gate":** 47 ô viền hồng tím, khối chắn phá được (2 trạng thái).',
      '**Vật thể:** tinh thể Nightmare (3 khung + nổ 4 khung), công tắc ngụy trang, bệ nổi đấu trường.',
      '**Nền:** ống nuôi Nightmare và màn hình nghiên cứu của Gate (2 lớp parallax).'],
)
for r in rooms:
    r['y'] += 4
STAGE['rooms'] = rooms
