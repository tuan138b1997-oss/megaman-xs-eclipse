from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_sheldon', 'Viện Laser', 'Shield Sheldon', 'shadow', 'Act II · X6', 'boss',
               'Viện nghiên cứu băng-laser: sàn và vách kính trơn (gia tốc thấp, trượt dài), tia laser đi theo đường gương, tường giả giấu đường lên tầng trên.',
               'X6 Shield Sheldon / Laser Institute, X5 Shining Hotarunicus, X2 Crystal Snail (kính).')
    st.capsule_short = 'Shadow Head'
    st.mech = ['Sàn và vách kính trơn', 'Tia laser đi theo đường gương']
    A1, A2 = 'Area 1 · sảnh kính', 'Area 2 · tầng thí nghiệm'

    r = R('R1', 'Sảnh kính', 3, 'Sàn kính trơn (gia tốc ×0.3, trượt 1.5 ô khi dừng). Gương chiếu laser chéo cố định.', timing='sàn trơn: gia tốc ×0.3')
    r.run(6, 'S').zone(16, 'laser', 'laser chéo', y0=3, ents='D').run(6).run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Phòng gương', 4, 'Bắn gương xoay 45° để đẩy tia về bộ thu, mở cửa X=2950 (dữ liệu game). Reploid trong lồng sau cửa.', timing='gương xoay 45° mỗi phát bắn')
    r.run(6).ent('K', 2, -3, 'gương xoay').zone(2, 'laser', 'cửa laser', y0=1).run(8, 'D').run(6, 'R').run(4)
    st.add(r.done(), A1)

    r = R('R3', 'Hành lang trần gai', 5, 'Trần gai thấp (khe 3 ô) + sàn trơn: nhảy cao là trúng gai. Brute trượt trên kính.', timing='khe trần 3 ô')
    r.run(4).raw(('block', 0, 1, 26, 6.5)).spikes(26, 'ceil', 6.5).run(10, 'B').gap(2, 'gai').run(10, 'D').run(4)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Phòng làm lạnh', 5, 'Mini-boss: tinh thể làm lạnh 45 HP phản đạn thường, chỉ đạn nạp xuyên. Checkpoint 1.', w=24, boss='M', note='tinh thể 45 HP',
                 timing='bắn băng tỏa 6 hướng mỗi 2 s', extra=lambda b: b.ent('C', -2).ent('S', -8)), 'Mid')

    s = Shaft('R4', 'Bệ kính cao', 7, 'Cao trào: leo bệ kính băng trơn (đứng lâu trượt khỏi mép), laser ngang đi theo gương ở hai tầng. '
              'Tường giả bên trái ở tầng trên (đi xuyên được) → capsule Shadow Head. Checkpoint 2 ở đáy.', w=16, h=36,
              timing='bệ kính trơn; laser gương bật 2 s / tắt 2 s')
    s.ent('C', 5, 34).add(('zone', 2, 24, 14, 25, 'laser', 'laser gương'), ('zone', 2, 14, 14, 15, 'laser', 'laser gương'))
    s.climb(step=2.5, kind='glass', ents={2: 'D', 6: 'D', 9: 'R'})
    s.add(('block', 0, 4, 2, 9), ('note', 2, 3, 'tường giả'), ('ledge', 2, 8, 3, 'ke'), ('e', 'A', 3.5, 8, 'Shadow Head')).secret((6, 10), (3.5, 8))
    st.add(s.done(), A2)

    r = R('R5', 'Phòng thí nghiệm', 5, 'Kính bảo vệ phản đạn thường; Heart Tank sau tấm kính phải bắn đạn nạp. Sub-Tank trên kệ thiết bị.', timing='kính bảo vệ 3 phát đạn nạp')
    r.run(6, 'S D').zone(2, 'laser', 'kính bảo vệ', y0=6).run(4).ent('H', 0, 0, 'sau kính').run(4, 'S').pillar(2, 2)
    r.secret((-1, -2), (1, -4.5)).raw(('ledge', 0, -4.5, 3, 'ke'), ('e', 'T', 1.5, -4.5, 'kệ thiết bị')).run(6, 'R').run(4, 'R')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Shield Sheldon', 6, 'Boss phản đạn bằng khiên; gương ở 4 góc làm đạn dội lại.', w=30), 'Boss')
    st.areas = [('Area 1', 'sảnh kính, phòng gương, hành lang trần gai', ['R1', 'R2', 'R3']), ('Mid', 'phòng làm lạnh', ['MID']),
                ('Area 2', 'bệ kính cao, phòng thí nghiệm', ['R4', 'R5']), ('Boss', 'phòng gương', ['BOSS'])]
    st.secrets = [('Capsule Shadow Head', 'R4', 'Đi xuyên tường giả tầng trên giếng.'), ('Heart Tank', 'R5', 'Bắn đạn nạp vỡ kính bảo vệ.'), ('Sub-Tank', 'R5', 'Kệ thiết bị.')]
    st.boss_info = {'arena': 'phòng 30×11 ô, gương ở 4 góc.', 'phase2': 'gương xoay theo nhịp 3 s: đạn dội theo góc mới; sàn kính trơn hơn.'}
    st.engine = ['Sàn/vách kính trơn', 'Laser theo đường gương, gương xoay bằng đạn', 'Tường giả đi xuyên', 'Kính bảo vệ cần đạn nạp']
    st.art = ['Sảnh kính băng', 'Gương xoay + bộ thu laser', 'Tường giả (cùng tileset)', 'Tấm kính bảo vệ']
    return st
