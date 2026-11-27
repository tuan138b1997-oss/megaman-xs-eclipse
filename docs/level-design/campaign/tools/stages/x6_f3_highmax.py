from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_f3_highmax', 'Phòng thí nghiệm Gate 2', 'High Max', 'core', 'Pháo đài X6', 'fortress',
               'Vực gai toàn khu vực: chuỗi bệ nhỏ 2 ô có cột Totem chặn (phá mới đứng được), băng chuyền chạy dưới tia laser dọc chạy ngang. '
               'Cao trào ở chuỗi bệ nhỏ thứ hai.',
               'X6 Gate Lab 2, X5 Zero Space 2 (bệ nhỏ), X1 Sigma stage.')
    st.mech = ['Bệ nhỏ 2 ô', 'Tia laser dọc chạy ngang']
    A1, A2 = 'Area 1 · chuỗi bệ nhỏ', 'Area 2 · tháp totem'

    r = R('R1', 'Bệ nhỏ', 6, 'Bệ 2×1 ô trên vực gai; cột Totem trên bệ (6 HP) phải phá mới đứng được.', timing='Totem bắn 1 viên mỗi 2 s', h=14)
    r.run(4, 'D').ledges(24, [(3, -1, 2), (8, -2, 2), (13, -1, 2), (18, -1, 2)], kind='ke', pit='gai', land=4).note('cột Totem trên mỗi bệ', -20, -6).run(4, 'R')
    st.add(r.done(), A1)

    r = R('R2', 'Băng chuyền laser', 6, 'Băng chuyền chạy nhanh 180 px/s dưới tia laser dọc chạy ngang (vạch đỏ trên sàn báo vị trí).', timing='laser dọc 200 px/s; băng 180 px/s')
    r.run(4, 'S').zone(30, 'laser', 'laser dọc chạy ngang', y0=1, walk=False).belt(14, 180, 'D').run(4).belt(12, -180).run(4, 'R')
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Điểm dừng', 5, 'Mini-boss: Totem chủ 45 HP. Checkpoint 1.', w=24, boss='M', note='Totem chủ 45 HP', timing='3 tầng bắn luân phiên',
                 extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R5', 'Chuỗi bệ nhỏ 2', 8, 'Cao trào: bệ nhỏ 2 ô + Totem + laser dọc chạy ngang qua chuỗi; Drone bay giữa. Checkpoint 2 ở bệ cứng đầu.', timing='laser 220 px/s', h=14)
    r.ent('C', 2).run(4).zone(30, 'laser', 'laser dọc', y0=1, walk=False).ledges(26, [(3, -1, 2), (8, -2, 2), (13, -1, 2), (18, -2, 2), (23, -1, 2)], kind='ke', pit='gai', land=4)
    r.ent('D', -2).run(4, 'S R')
    st.add(r.done(), A2)

    s = Shaft('R6', 'Tháp totem', 7, 'Leo giữa các totem bắn đạn ngang.', w=14, h=28, timing='totem bắn mỗi 1.8 s')
    s.climb(step=2.5, ents={2: 'D', 5: 'R'})
    st.add(s.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước boss.')
    r.run(6).ent('E', 0, 0, 'trạm năng lượng lớn').run(10, 'B')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'High Max', 7, 'Khiên bất khả xâm phạm; dùng Charge Saber của Blade (giữ ↑ rồi thả) để làm choáng.', w=30), 'Boss')
    st.areas = [('Area 1', 'bệ nhỏ, băng chuyền laser', ['R1', 'R2']), ('Mid', 'Totem chủ', ['MID']), ('Area 2', 'chuỗi bệ nhỏ 2, tháp totem', ['R5', 'R6', 'R7']),
                ('Boss', 'phòng High Max', ['BOSS'])]
    st.boss_info = {'attacks': 'Orb Barrage, Shield (bất khả xâm phạm trừ khi choáng), Teleport.', 'arena': '30×11 ô.',
                    'phase2': 'High Max tạo 2 khiên quỹ đạo; chỉ choáng được khi cả hai khiên ở phía sau.'}
    st.engine = ['Bệ nhỏ có Totem chặn', 'Laser dọc chạy ngang', 'Băng chuyền nhanh', 'Boss cần làm choáng bằng Charge Saber']
    st.art = ['Bệ nhỏ 2 ô', 'Cột Totem', 'Laser dọc']
    return st
