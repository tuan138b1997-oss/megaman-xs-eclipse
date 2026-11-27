from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_hotarunicus', 'Phòng thí nghiệm Laser', 'Shining Hotarunicus', 'volt', 'Act I · X5', 'boss',
               'Viện nghiên cứu quang học. Area 1: tia laser chặn lối, ba công tắc quang học tắt từng cửa laser, gương xoay đổi hướng tia. '
               'Area 2: vực hologram với bệ hai pha và dây chuyền thấu kính.',
               'X5 Shining Hotarunicus (viện laser), X6 Shield Sheldon (gương), X4 Cyber Peacock (thế giới ảo).')
    st.capsule_short = 'Falcon Body'
    st.mech = ['Tia laser', 'Công tắc quang học']
    A1, A2 = 'Area 1 · khoang quang học', 'Area 2 · hologram'

    r = R('R1', 'Sảnh viện', 2, 'Tia laser dọc quét chậm qua sảnh (sang phải 2 s, về 2 s). Dạy canh nhịp: đứng sau vách kính chờ tia qua.',
          timing='laser quét 160 px/s, có vạch đỏ báo vị trí trên sàn')
    r.run(6, 'S').zone(16, 'laser', 'laser quét ↔', y0=1).pillar(2, 2).run(8, 'D S').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Khoang quang học #1', 3, 'Cửa laser đứng chặn giữa khoang. Bắn công tắc #1 (trên kệ) để tắt. Gương xoay ở góc: bắn gương đổi hướng tia sang trái, '
          'tia đốt Sniper đứng sau cửa.', timing='cửa laser tắt vĩnh viễn khi công tắc trúng')
    r.run(6).pillar(2, 2).raw(('e', 'K', 1, -2, 'công tắc #1')).run(4, 'S').zone(2, 'laser', 'cửa laser', y0=1).run(10, 'R').run(4)
    st.add(r.done(), A1)

    s = Shaft('R3', 'Khoang quang học #2', 4, 'Leo bệ cao; công tắc #2 ở kệ giữa. Tia laser ngang ở tầng trên chỉ tắt khi công tắc #2 trúng. '
              'Buồng kín phía trên bên trái có capsule Falcon Body (dữ liệu game: X=2150).', w=14, h=30, timing='laser ngang tầng trên tắt khi công tắc #2 trúng')
    s.add(('zone', 2, 12, 12, 13, 'laser', 'laser'), ('e', 'K', 5.5, 20, 'công tắc #2'))
    s.climb(step=2.5, ents={2: 'D'})
    s.add(('ledge', 3, 6, 4, 'ke'), ('e', 'A', 5, 6, 'Falcon Body')).secret((10, 10), (5, 6))
    st.add(s.done(), A1)

    r = R('R4', 'Khoang quang học #3', 5, 'Hai tia quét ngang song song; công tắc #3 chỉ bắn trúng khi đứng trong vùng an toàn giữa hai tia. '
          'Heart Tank sau cửa laser phụ (mở bằng công tắc #3).', timing='2 tia quét cách nhau 3 ô, chu kỳ 3 s')
    r.run(6).zone(12, 'laser', 'tia quét ×2', y0=3, ents='D').ent('K', 0, -3, 'công tắc #3').pillar(2, 2).run(6, 'S')
    r.secret((0, 0), (4, 0)).raw(('e', 'H', 3, 0, 'sau cửa laser phụ'), ('zone', 1, -4, 2, 0, 'laser', '')).run(6)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Lõi quang học', 5, 'Mini-boss: lõi quang học 45 HP xoay 4 gương, bắn tia phản xạ. Checkpoint 1 sau trận.', w=24, boss='M',
                 note='lõi 45 HP', timing='tia phản xạ mỗi 2 s, đổi góc gương mỗi 4 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R5', 'Vực hologram', 7, 'Cao trào. Vực sâu với bệ hologram hai pha (xanh/tím đổi mỗi 2 s, nháy 0.5 s trước khi tắt). Băng chuyền hai đầu. '
          'Drone bay qua vực. Checkpoint 2 giữa vực trên bệ cứng.', timing='bệ 2 pha: 2 s xanh / 2 s tím, nháy 0.5 s', h=14)
    r.belt(6, 80).ledges(22, [(3, -1, 3), (8, -2, 3), (13, -1, 3), (18, 0, 3)], kind='phase', land=4).ent('C', -2).ent('D', -2)
    r.ledges(22, [(3, -2, 3), (8, -1, 3), (13, -2, 3), (18, -1, 3)], kind='phase', land=3).ent('R', -1).belt(6, -80).run(4, 'D')
    st.add(r.done(), A2)

    r = R('R6', 'Dây chuyền thấu kính', 5, 'Hai băng chuyền chạy ngược chiều, thấu kính rơi từ trần (bóng tròn báo trước 0.8 s). Sub-Tank trên kệ băng chuyền trên.',
          timing='thấu kính rơi mỗi 1.5 s; băng chuyền ±100 px/s')
    r.belt(12, 100, 'S').belt(12, -100, 'B').pillar(2, 2).secret((-1, -2), (1, -4.5)).raw(('ledge', 0, -4.5, 4, 'ke'), ('e', 'T', 2, -4.5, 'kệ băng chuyền trên'))
    r.run(8, 'R').run(4, 'R').run(4)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Shining Hotarunicus', 6, 'Đấu trường tối; gương ở hai góc phản xạ đạn của người chơi.', w=30), 'Boss')
    st.areas = [('Area 1', '3 khoang quang học', ['R1', 'R2', 'R3', 'R4']), ('Mid', 'lõi quang học', ['MID']),
                ('Area 2', 'vực hologram, dây chuyền thấu kính', ['R5', 'R6']), ('Boss', 'đấu trường tối', ['BOSS'])]
    st.secrets = [('Capsule Falcon Body', 'R3', 'Buồng kín sau tầng laser, mở bằng công tắc #2.'), ('Heart Tank', 'R4', 'Sau cửa laser phụ mở bằng công tắc #3.'),
                  ('Sub-Tank', 'R6', 'Kệ băng chuyền trên.')]
    st.boss_info = {'arena': 'phòng tối 30×11 ô, 2 gương góc phản xạ đạn.',
                    'phase2': 'đèn tắt hẳn, chỉ còn vệt sáng của boss và các phân thân ánh sáng; gương xoay theo nhịp 3 s.'}
    st.engine = ['Tia laser quét/cố định, tắt bằng công tắc', 'Công tắc quang học (bắn)', 'Gương xoay đổi hướng tia', 'Bệ hologram 2 pha', 'Thấu kính rơi theo lịch']
    st.art = ['Vách kính viện, sàn kim loại sáng', 'Cửa laser + công tắc quang học', 'Gương xoay', 'Bệ hologram xanh/tím', 'Thấu kính']
    return st
