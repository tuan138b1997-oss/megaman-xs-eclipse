from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_heatnix', 'Khu dung nham', 'Blaze Heatnix', 'fire', 'Act II · X6', 'boss',
               'Khu núi lửa hoạt động, dùng lại bộ element của Lò Nham Thạch (dung nham, cột lửa, đá lăn). Cỗ máy vòng lửa Nightmare Donut chặn đường; '
               'bệ phản lực bay ngang có hết nhiên liệu. Cao trào là trục núi lửa có dung nham dâng, capsule Shadow Arm ở đỉnh.',
               'X6 Blaze Heatnix (núi lửa), Lò Nham Thạch (màn mẫu), X2 Flame Stag (núi lửa leo dọc).')
    st.capsule_short = 'Shadow Arm'
    st.mech = ['Cột dung nham phun theo nhịp', 'Bệ phản lực bay ngang có hết nhiên liệu']
    A1, A2 = 'Area 1 · miệng hố và sông nham', 'Area 2 · trục núi lửa'

    r = R('R1', 'Miệng hố', 3, 'Mưa đá lửa nhỏ, hố nham. Bệ phản lực đầu tiên: đứng lên là bay ngang 6 ô rồi hết nhiên liệu (đèn đỏ 1 s trước khi tắt).',
          timing='bệ phản lực: bay 4 s rồi rơi; đá lửa mỗi 2 s', h=14)
    r.run(6, 'S').gap(3, 'lava').run(6, 'D S').ledges(12, [(3, -1, 4)], kind='thruster', pit='lava', land=4, tag='j').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Donut #1', 4, 'Cỗ máy vòng lửa Donut #1 (vật cản, 20 HP) bắn vòng lửa lan rộng; bệ phản lực hai bên. Reploid sau Donut.', timing='vòng lửa mỗi 2.5 s, lan 4 ô')
    r.run(6, 'B').zone(6, 'fire', 'Donut #1 vòng lửa', y0=3).run(6, 'R D').run(4)
    st.add(r.done(), A1)

    r = R('R3', 'Sông nham', 5, 'Bệ đá trôi trên sông nham (60 px/s), cột lửa phun theo nhịp ở ba điểm (bọt nham báo trước 0.6 s).',
          timing='bệ đá trôi 60 px/s; cột lửa 1.2 s mỗi 3.5 s', h=14)
    r.run(4, 'D').ledges(24, [(3, -1, 4), (11, -1, 4), (19, 0, 3)], kind='move', pit='lava', land=4).zone(3, 'fire', 'cột lửa', y0=3).run(6, 'D S')
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Hang mát', 5, 'Mini-boss: Nightmare Donut #2 (cỡ lớn, 45 HP) + đá lăn từ dốc. Checkpoint 1; Heart Tank trên gờ đá sau trận.', w=28, boss='M',
                 note='Donut #2 45 HP', timing='vòng lửa mỗi 2 s; đá lăn mỗi 4 s',
                 extra=lambda b: b.ent('C', -4).pillar(3, 2).ent('H', -2, -2, 'gờ đá')), 'Mid')

    s = Shaft('R5', 'Trục núi lửa', 7, 'Cao trào: trục leo X=5250 (dữ liệu game), dung nham dâng 55→75 px/s từ khi bước vào; Donut #3 (vật cản) ở giữa trục. '
              'Kệ đá so le, cột lửa phun ngang ở hai tầng. Capsule Shadow Arm ở đỉnh trục bên trái. Checkpoint 2 ở đáy.', w=18, h=48,
              timing='nham dâng 55→75 px/s, dừng 2 s ở kệ an toàn; cột lửa ngang 1 s mỗi 3 s')
    s.ent('C', 5, 46).add(('zone', 2, 40, 16, 46, 'lavarise', 'nham dâng'), ('zone', 2, 28, 16, 29, 'fire', 'cột lửa ngang'), ('zone', 2, 16, 16, 17, 'fire', 'cột lửa ngang'),
                          ('note', 8, 24, 'Donut #3'))
    s.climb(step=2.5, ents={3: 'D', 7: 'S', 11: 'R'})
    s.add(('ledge', 3, 6, 4, 'ke'), ('e', 'A', 5, 6, 'Shadow Arm (đỉnh trục)')).secret((12, 10), (5, 6))
    st.add(s.done(), A2)

    r = R('R6', 'Đỉnh núi', 2, 'Phòng nghỉ trên miệng núi lửa: Sub-Tank, hai Reploid, cửa boss.', ceil=None)
    r.run(6, 'R').ent('T', 2, 0, 'hốc đá').run(6, 'R').run(4, 'S').run(4)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Blaze Heatnix', 6, 'Đấu trường miệng núi lửa; Heatnix bay vòng.', w=30), 'Boss')
    st.areas = [('Area 1', 'miệng hố, Donut #1, sông nham', ['R1', 'R2', 'R3']), ('Mid', 'Donut #2', ['MID']), ('Area 2', 'trục núi lửa, đỉnh núi', ['R5', 'R6']),
                ('Boss', 'miệng núi lửa', ['BOSS'])]
    st.secrets = [('Capsule Shadow Arm', 'R5', 'Đỉnh trục bên trái (dùng Charge Saber phá đá chắn theo dữ liệu game).'), ('Heart Tank', 'MID', 'Gờ đá sau trận Donut #2.'),
                  ('Sub-Tank', 'R6', 'Hốc đá đỉnh núi.')]
    st.boss_info = {'arena': 'miệng núi lửa 30×11 ô.', 'phase2': 'dung nham lấp nửa dưới đấu trường (như boss Lò Nham Thạch: nham hai bên rộng ra), Heatnix bay hình số 8.'}
    st.engine = ['Bệ phản lực bay ngang có nhiên liệu', 'Cột lửa phun theo nhịp (dùng lại Lò Nham Thạch)', 'Nham dâng có kệ dừng', 'Nightmare Donut (vật cản bắn vòng lửa)']
    st.art = ['Dùng lại element Lò Nham Thạch: dung nham, thác nham, đá lăn', 'Bệ phản lực', 'Nightmare Donut', 'Trục núi lửa']
    return st
