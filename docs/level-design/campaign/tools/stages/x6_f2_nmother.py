from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_f2_nmother', 'Phòng thí nghiệm Gate 1', 'Nightmare Mother', 'fire', 'Pháo đài X6', 'fortress',
               'Tầng 1 phòng thí nghiệm Gate: biển gai với bệ di động ngang, bệ xoay quanh trục, rồi trục thang máy có dung nham dâng liên tục tăng tốc '
               '(khó hơn giếng nham dâng của Lò Nham Thạch: không có kệ dừng).',
               'X6 Gate Lab 1, Lò Nham Thạch R6 (nham dâng), X2 Magna Centipede (bệ).')
    st.mech = ['Bệ di động ngang', 'Dung nham dâng liên tục có tăng tốc']
    A1, A2 = 'Area 1 · biển gai', 'Area 2 · trục thang máy'

    r = R('R1', 'Biển gai', 6, 'Bệ di động ngang/dọc trên sàn gai. Drone đứng chặn trên đường bay của bệ.', timing='bệ ±4 ô, chu kỳ 3 s', h=14)
    r.run(4, 'D').ledges(26, [(3, -1, 4), (11, -2, 4), (19, -1, 4)], kind='move', pit='gai', land=4).ent('D', -2).run(4, 'R')
    st.add(r.done(), A1)

    r = R('R2', 'Bệ xoay', 6, 'Bệ xoay quanh trục (1 vòng / 6 s), gai ở cả trên và dưới; đứng lâu ở đỉnh vòng là chạm gai trần.', timing='bệ xoay 1 vòng / 6 s', h=14)
    r.run(4, 'S').spikes(30, 'ceil', 1).ledges(24, [(3, -1, 3), (9, -2, 3), (15, -1, 3), (20, 0, 3)], kind='rotate', pit='gai', land=4).run(4, 'B R')
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Điểm dừng', 5, 'Mini-boss: lõi Nightmare lửa 45 HP. Checkpoint 1.', w=24, boss='M', note='lõi lửa 45 HP', timing='cầu lửa 4 hướng mỗi 2 s',
                 extra=lambda b: b.ent('C', -2)), 'Mid')

    s = Shaft('R3', 'Trục thang máy dung nham', 8, 'Cao trào: dung nham dâng 70→90 px/s, không có kệ dừng; gai trên vách trái. Kệ so le 2.5 ô, Drone bay ngang. '
              'Checkpoint 2 ở đáy trục.', w=14, h=40, timing='nham dâng 70→90 px/s, bắt đầu 1.5 s sau khi vào')
    s.ent('C', 5, 38).add(('zone', 2, 32, 12, 38, 'lavarise', 'nham dâng 70→90'), ('spikes', 2, 2.6, 20, 'wall')).climb(step=2.5, ents={3: 'D', 7: 'S', 10: 'R'})
    st.add(s.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước boss; Reploid cuối.')
    r.run(6, 'R').ent('E', 0, 0, 'trạm năng lượng lớn').run(10, 'D')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Nightmare Mother', 7, 'Khối Nightmare lơ lửng, 4 lõi nguyên tố đổi màu.', w=30), 'Boss')
    st.areas = [('Area 1', 'biển gai, bệ xoay', ['R1', 'R2']), ('Mid', 'lõi Nightmare lửa', ['MID']), ('Area 2', 'trục thang máy dung nham', ['R3', 'R7']),
                ('Boss', 'phòng lõi', ['BOSS'])]
    st.boss_info = {'attacks': 'Element Orbs (4 lõi nguyên tố), Cube Drop, Body Slam.', 'arena': '30×11 ô.', 'phase2': 'dung nham dâng 2 ô ở hai mép sân, lõi bắn đồng thời.'}
    st.engine = ['Bệ di động ngang/dọc', 'Bệ xoay quanh trục', 'Dung nham dâng không dừng, tăng tốc']
    st.art = ['Biển gai phòng thí nghiệm', 'Bệ xoay', 'Trục thang máy + dung nham']
    return st
