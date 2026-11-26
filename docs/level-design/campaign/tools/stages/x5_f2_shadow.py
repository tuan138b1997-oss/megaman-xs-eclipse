from kit import *

THEME = dict(bg1=(30, 24, 48), bg2=(24, 20, 42), rock1=(96, 80, 130), rock2=(88, 70, 124))


def A(x, y, w=4): return P(x, y, w, 'holo')      # pha A
def Bp(x, y, w=4): return P(x, y, w, 'holoB')    # pha B


rooms = [
 Room('R1', 'Bệ xuất phát', 0, 30, 40, 18, 3, [
   F((0, 12), (24, 12)), H('void', 24, 14, 16, 4), A(28, 11), Bp(34, 9), E('R', 10, 11), E('S', 20, 11),
   X(25, 6, 'A = viền, B = tím'), PATH((1, 11), (23, 11), (30, 10), (36, 8), (39.5, 8))], '''
- **Mục đích:** giới thiệu **bệ Cyber 2 pha**: bệ pha A và bệ pha B thay phiên nhau hiện.
- **Địa hình:** mỏm đá cuối cùng (24 ô) trước vực không đáy. Sau mỏm này, cả màn không có mặt đất.
- **Cơ chế – bệ 2 pha:**
  - Pha A hiện 2 giây thì pha B hiện 2 giây, luân phiên. Bệ sắp đổi pha thì chớp trắng 0.4 giây.
  - Trên sơ đồ: bệ viền rỗng là pha A, bệ tím đặc là pha B.
- **Địch:** 1 Sniper ở mép vực.
- **Vật phẩm:** Reploid #1 ở đầu mỏm đá.
- **Ghi chú:** pháo đài không có capsule, Heart Tank, Sub-Tank. Mang vũ khí Tri-Thunder để khắc chế mắt đỏ của Shadow Devil.'''),

 Room('R2', 'Vực pha A/B', 40, 26, 64, 22, 5, [
   H('void', 0, 20, 64, 2), A(4, 12), Bp(12, 10), A(20, 13), Bp(28, 9), A(36, 12), Bp(44, 10), A(52, 13), Bp(58, 11),
   E('D', 24, 4), E('D', 48, 5), PATH((1, 12), (6, 11), (14, 9), (22, 12), (30, 8), (38, 11), (46, 9), (54, 12), (60, 10), (63.5, 10))], '''
- **Mục đích:** chuỗi bệ 2 pha dài đầu tiên.
- **Địa hình:** vực không đáy dài 64 ô. 8 bệ xen kẽ A/B, cách nhau 8 ô.
- **Cơ chế:** mỗi cú nhảy phải rời bệ cũ trước khi nó tắt và đáp lên bệ mới đúng lúc nó hiện. Nhịp 2 giây đủ cho một cú nhảy và một nhịp nghỉ.
- **Địch:** 2 Drone. Bị bắn trúng giữa không trung là lỡ nhịp.'''),

 Room('R3', 'Luồng nâng 1', 104, 14, 40, 34, 5, [
   H('void', 0, 32, 40, 2), Z('updraft', 16, 2, 8, 30, 'luồng nâng 150px/s'), AR(20, 28, 0, -10, 'updraft'),
   A(4, 24), Bp(30, 6), A(34, 10), E('R', 36, 9), E('D', 10, 12),
   PATH((1, 24), (6, 23), (18, 20), (20, 6), (31, 5), (39.5, 5))], '''
- **Mục đích:** đi lên bằng **luồng khí nâng** giữa vực.
- **Địa hình:** khoảng không cao 30 ô, một luồng nâng rộng 8 ô ở giữa.
- **Cơ chế:** vào luồng thì bay lên 150px/giây. Lướt ngang ra khỏi luồng ở đúng độ cao để đáp lên bệ pha B phía trên phải.
- **Địch:** 1 Drone canh chân luồng.
- **Vật phẩm:** Reploid #2 trên bệ pha A cao nhất.'''),

 Room('R4', 'Chuỗi pha nhanh', 144, 14, 56, 22, 6, [
   H('void', 0, 20, 56, 2), A(4, 8), Bp(12, 10), A(20, 7), Bp(28, 10), A(36, 8), Bp(44, 6), A(51, 8),
   X(4, 15, 'nhịp 1.5s'), E('S', 46, 5), PATH((1, 7), (6, 7), (14, 9), (22, 6), (30, 9), (38, 7), (46, 5), (53, 7), (55.5, 7))], '''
- **Mục đích:** tăng nhịp: bệ đổi pha mỗi **1.5 giây**.
- **Địa hình:** 7 bệ trên vực 56 ô.
- **Cơ chế:** nhịp nhanh hơn nên không còn nhịp nghỉ. Một số bệ chỉ rộng 3 ô.
- **Địch:** 1 Sniper đứng trên bệ pha B thứ ba: bệ tắt thì nó rơi theo, nên có thể chờ thay vì bắn.'''),

 Room('MID', 'Mắt bóng tối', 200, 10, 34, 20, 6, [
   H('void', 0, 18, 34, 2), B(2, 12, 8, 1), B(13, 9, 8, 1), B(24, 12, 8, 1), E('M', 17, 3), X(2, 15, 'ba bệ cố định'),
   PATH((3, 11), (16, 8), (29, 11), (33.5, 11))], '''
- **Đấu trường trên 3 bệ cố định** giữa vực, không vách.
- **Mắt bóng tối** là một con mắt lớn lơ lửng, mảnh vỡ của Shadow Devil.
- **Đòn đánh:**
  - Bắn tia xuống một bệ, làm bệ đó tắt 3 giây.
  - Thả 4 khối bóng tối rơi chéo.
  - Nhìn chằm chằm: đứng trong tầm nhìn 1 giây là bị đẩy về phía mép.
- **Điểm yếu:** con ngươi đỏ (Tri-Thunder gây sát thương gấp đôi).
- **Phần thưởng:** mở trạm nghỉ giữa màn. Hạ không mất máu thì được thưởng Souls.'''),

 Room('R5', 'Vực ba tầng', 234, 6, 60, 28, 6, [
   H('void', 0, 26, 60, 2), B(0, 14, 6, 1), A(8, 20), Bp(16, 16), A(24, 12), Bp(32, 8), A(40, 12), Bp(48, 16), A(54, 20), B(56, 14, 4, 1),
   A(24, 22), Bp(40, 22), E('C', 2, 13), E('R', 26, 21), E('D', 30, 3), E('S', 42, 21),
   PATH((1, 13), (10, 19), (18, 15), (26, 11), (34, 7), (42, 11), (50, 15), (57, 13), (59.5, 13)), ALT((18, 15), (26, 21))], '''
- **Checkpoint 1** ở đầu phòng.
- **Mục đích:** đường đi hình vòng cung: lên đỉnh giữa vực rồi xuống bên kia.
- **Địa hình:** vực 60 ô, 7 bệ xếp thành vòng cung, thêm 2 bệ ở tầng thấp.
- **Cơ chế:** nhịp 2 giây. Tầng thấp an toàn hơn (bệ rộng hơn) nhưng có địch.
- **Địch:** 1 Drone trên đỉnh vòng cung, 1 Sniper ở tầng thấp.
- **Vật phẩm:** Reploid #3 ở tầng thấp.'''),

 Room('R6', 'Luồng nâng 2', 294, 0, 60, 36, 8, [
   H('void', 0, 34, 60, 2), B(0, 20, 6, 1), Z('updraft', 10, 2, 6, 32, ''), Z('updraft', 36, 2, 6, 32, ''),
   AR(13, 30, 0, -8, 'updraft'), AR(39, 30, 0, -8, 'updraft'), A(20, 10, 3), Bp(26, 14, 3), A(30, 8, 3), Bp(46, 12, 3), A(52, 6, 3), B(56, 6, 4, 1),
   X(8, 1, 'luồng bật 3s / tắt 2s'), E('D', 24, 22), E('D', 48, 22),
   PATH((1, 19), (6, 19), (13, 15), (14, 9), (21, 9), (27, 13), (31, 7), (38, 10), (40, 4), (47, 11), (53, 5), (59.5, 5))], '''
- **Mục đích:** cao trào của màn. **Luồng nâng bật/tắt** kết hợp bệ 2 pha nhỏ.
- **Địa hình:** vực 60 ô, cao 34 ô. 2 luồng nâng, 5 bệ rộng 3 ô.
- **Cơ chế:**
  - Luồng nâng bật 3 giây, tắt 2 giây. Đang bay mà luồng tắt là rơi.
  - Bệ 2 pha nhịp 2 giây, không khớp nhịp với luồng nâng: người chơi phải chờ cả hai thứ cùng thuận.
- **Địch:** 2 Drone canh chân luồng.
- **Giáp hỗ trợ:** Falcon bay tự do qua gần hết phòng.'''),

 Room('R7', 'Trạm nghỉ', 354, 2, 30, 14, 2, [
   F((0, 4), (30, 4)), BAR(29, 0, 1, 4, 'door'), E('C', 2, 3), E('R', 15, 3), X(4, 0.5, 'năng lượng LỚN'), PATH((1, 3), (28, 3))], '''
- **Checkpoint 2** ở đầu phòng.
- Bệ đá nổi duy nhất trong màn: Reploid #4, **nạp năng lượng lớn**, cửa boss.'''),

 Room('BOSS', 'Shadow Devil', 384, -4, 32, 18, 7, [
   F((0, 10), (32, 10)), H('void', 0, 16, 32, 2), E('*', 16, 3), X(3, 12, 'pha 2: sàn chia 2 pha'), PATH((1, 9), (31, 9))], '''
- **Đấu trường 32 ô** trên một bệ nổi, không vách.
- **Pha 1** (100–50% HP): bộ chiêu hiện có (tách khối, ghép lại, mắt đỏ bắn tia).
- **Pha 2** (dưới 50% HP):
  - **Sàn đấu trường chia thành 2 nửa pha A/B**, mỗi nửa hiện 3 giây.
  - Các khối của Shadow Devil rơi xuống đúng nửa đang hiện.
- Điểm yếu giữ nguyên theo dữ liệu game.'''),
]

STAGE = dict(
 title='Zero Space 2', en='Zero Space 2', boss='Shadow Devil', act='Pháo đài X5', theme=THEME, capsule='',
 subtitle='Area 1: R1 → R2 (bệ 2 pha) → R3 (luồng nâng) → R4 (pha nhanh) → Mini-boss  |  Area 2: R5 (vòng cung) → R6 (luồng nâng bật/tắt) → R7 trạm nghỉ → Boss',
 keep='Boss Shadow Devil, vực không đáy toàn màn, bệ Cyber nhấp nháy 2 pha, 2 luồng khí nâng và trạm nghỉ giữa màn vẫn giữ. Không có capsule/Heart Tank/Sub-Tank (theo dữ liệu game); thêm 4 Reploid, 1 mini-boss và trạm nạp lớn.',
 concept='Thử thách nhảy chính xác: **cả màn là vực không đáy**. Người chơi chỉ có bệ Cyber 2 pha và luồng khí nâng. Không có địch mạnh, nhưng mỗi lần lỡ nhịp là mất mạng.',
 areas=['**Area 1 – Vực đầu:** bệ 2 pha nhịp 2 giây, luồng nâng, rồi nhịp 1.5 giây.',
        '**Area 2 – Vực sâu:** vòng cung 3 tầng, luồng nâng bật/tắt lệch nhịp với bệ.'],
 flow='học nhịp A/B → chuỗi 8 bệ → bay luồng nâng → nhịp nhanh → mini-boss trên 3 bệ → vòng cung → luồng nâng bật/tắt → boss trên sàn 2 pha',
 time='khoảng 5–7 phút lần đầu (nhiều lần chết), khoảng 2.5 phút khi đã quen',
 refs=['**X5, Zero Space 2:** vực không đáy toàn màn, 10 bệ Cyber nhấp nháy 2 pha, 2 luồng khí nâng, trạm nghỉ ở mid-gate.',
       '**X4, màn Cyber Peacock:** bệ dữ liệu ẩn hiện trong không gian mạng.',
       '**X5, màn Spiral Pegacion:** luồng khí nâng giữa vực.',
       '**X Corrupted:** hai nhịp không khớp nhau buộc người chơi chờ thời điểm cả hai cùng thuận.'],
 engine=['Bệ 2 pha: nhóm A và nhóm B luân phiên hiện, có chớp báo trước, nhịp chỉnh được theo phòng.',
         'Luồng khí nâng có thể bật/tắt theo nhịp.',
         'Vực không đáy toàn màn (camera khóa trong từng phòng).',
         'Mini-boss Mắt bóng tối: làm tắt bệ, đẩy người chơi.',
         'Sàn boss chia 2 pha.'],
 art=['**Tileset "Vực Cyber":** bệ Cyber pha A (viền sáng) và pha B (đặc), 3 khung mỗi loại (hiện, chớp, ẩn).',
      '**Vật thể:** luồng khí nâng (4 khung), mắt bóng tối, bệ đá nổi trạm nghỉ.',
      '**Nền:** vực tím sâu, tinh vân dữ liệu (2 lớp parallax).'],
)
for r in rooms:
    r['y'] += 6
STAGE['rooms'] = rooms
