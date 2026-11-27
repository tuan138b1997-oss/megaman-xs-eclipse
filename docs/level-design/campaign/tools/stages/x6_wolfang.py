from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_wolfang', 'Bắc Cực', 'Blizzard Wolfang', 'ice', 'Act II · X6', 'boss',
               'Area 1 là chặng Ride Chaser đổ dốc tuyết bị tuyết lở đuổi (người chơi tự lái, tuyết lở chậm hơn tốc độ tối đa). '
               'Area 2: vách băng cao trơn, hồ băng có băng nhọn rơi, sông băng trôi cao trào.',
               'X6 Blizzard Wolfang (Bắc Cực, Ride Chaser), X1 Chill Penguin (băng), X8 Avalanche Yeti (tuyết lở).')
    st.capsule_short = 'Blade Body'
    st.mech = ['Ride Chaser đổ dốc', 'Tảng băng lăn']
    A1, A2 = 'Area 1 · dốc tuyết', 'Area 2 · vách và hồ băng'

    r = R('R1', 'Trạm trượt', 1, 'Lên Ride Chaser (↑). Bảng: tuyết lở sẽ đuổi, giữ tốc độ.', ceil=None)
    r.run(6).ent('V', 2, 0, 'Ride Chaser').run(10, 'S').run(6)
    st.add(r.done(), A1)

    r = R('R2', 'Dốc tuyết lở', 5, 'Ride Chaser xuống dốc dài 130 ô; tuyết lở đuổi phía sau 300 px/s (xe tối đa 560 px/s). Nhảy qua khe băng, né cây thông đổ, '
          'tảng băng lăn ngược chiều. Reploid trên mỏm đá giữa dốc (dừng xe lấy).', timing='tuyết lở 300 px/s; tảng băng lăn mỗi 3 s', ceil=None, h=24)
    r.zone(20, 'avalanche', '← tuyết lở đuổi 300 px/s', y0=1, walk=False).slope(20, 3).ent('D', 0).special(8, 'ride', 0, prims=[('pit', 0, 8, 'tuyet')], land=6)
    r.slope(20, 3).run(6, 'R').special(10, 'ride', 1, prims=[('pit', 0, 10, 'tuyet')], land=6).slope(20, 3).ent('D', 0).run(10, 'S').run(4)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Trạm khí tượng', 5, 'Xuống xe. Mini-boss: radar khí tượng 45 HP bắn băng đá; checkpoint 1.', w=24, boss='M', note='radar 45 HP',
                 timing='băng đá 3 viên mỗi 2 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    s = Shaft('R3', 'Vách băng cao', 5, 'Bám tường băng X=3850 (trơn: trượt xuống nhanh hơn, đá tường vẫn được). Blade Body ở hốc cao bên trái (dữ liệu game).',
              w=14, h=32, timing='vách băng: trượt 180 px/s khi bám')
    s.climb(step=2.5, kind='ice', ents={2: 'D', 6: 'S'})
    s.add(('ledge', 3, 6, 4, 'ke'), ('e', 'A', 5, 6, 'Blade Body (hốc cao)')).secret((9, 10), (5, 6))
    st.add(s.done(), A2)

    r = R('R4', 'Hồ băng', 5, 'Sàn băng trơn, băng nhọn rơi từ trần theo nhịp (rung 0.6 s trước). Heart Tank trên tảng băng trôi giữa hồ.', timing='băng nhọn mỗi 2 s; sàn trơn ×0.3', h=14)
    r.run(6, 'S').ledges(16, [(3, -1, 4), (10, -1, 3)], kind='ice', pit='nuoc', land=4).ent('H', -10, -1, 'tảng băng trôi').run(6, 'B').run(4)
    st.add(r.done(), A2)

    r = R('R6', 'Sông băng trôi', 7, 'Cao trào: tảng băng trôi xuôi dòng (80 px/s) chìm dần khi đứng; tảng băng lăn từ thượng nguồn. Checkpoint 2 ở bờ đầu.',
          timing='tảng băng chìm sau 2 s; băng lăn mỗi 2.5 s', h=14, ceil=None)
    r.ent('C', 2).run(4, 'D').ledges(26, [(3, -1, 4), (10, -1, 4), (17, -2, 3), (22, -1, 3)], kind='ice', pit='nuoc', land=4).ent('R', -2)
    r.ledges(16, [(3, -1, 4), (10, -1, 3)], kind='ice', pit='nuoc', land=4).run(4, 'D')
    st.add(r.done(), A2)

    r = R('R5', 'Hang băng', 2, 'Phòng nghỉ: Sub-Tank trong khối băng (bắn vỡ), hai Reploid, cửa boss.')
    r.run(6, 'R').ent('T', 2, 0, 'khối băng').run(6, 'R').run(6, 'S')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Blizzard Wolfang', 6, 'Sàn đấu đóng băng dần (trơn); sói phóng băng.', w=30), 'Boss')
    st.areas = [('Area 1', 'trạm trượt, dốc tuyết lở', ['R1', 'R2']), ('Mid', 'trạm khí tượng', ['MID']), ('Area 2', 'vách băng, hồ băng, sông băng', ['R3', 'R4', 'R6', 'R5']),
                ('Boss', 'hang băng lớn', ['BOSS'])]
    st.secrets = [('Capsule Blade Body', 'R3', 'Hốc cao bên trái vách băng.'), ('Heart Tank', 'R4', 'Tảng băng trôi giữa hồ.'), ('Sub-Tank', 'R5', 'Bắn vỡ khối băng.')]
    st.boss_info = {'arena': 'hang băng 30×11 ô.', 'phase2': 'sàn đóng băng toàn phần (trơn ×0.2), băng nhọn rơi từ trần theo hàng.'}
    st.engine = ['Ride Chaser đổ dốc (người chơi tự lái)', 'Tuyết lở đuổi chậm hơn tốc độ tối đa', 'Tảng băng lăn', 'Vách băng trơn', 'Tảng băng trôi chìm dần']
    st.art = ['Dốc tuyết + cây thông đổ', 'Tuyết lở (mặt trước)', 'Vách băng', 'Tảng băng trôi', 'Ride Chaser (có sẵn)']
    return st
