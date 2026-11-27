from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_f1_dynamo', 'Zero Space 1', 'Dynamo', 'shadow', 'Pháo đài X5', 'fortress',
               'Pháo đài Sigma tầng 1: các cụm laser quét toàn chiều cao hành lang, buộc người chơi chạy giữa các hốc trú trong sàn. '
               'Băng chuyền tốc độ cao làm khó canh nhịp. Area 1 làm quen, Area 2 phối hợp nhiều nhịp laser.',
               'X5 Zero Space 1 (laser quét), X6 Gate Lab (tia dọc), X3 Doppler stage 1.')
    st.mech = ['Laser quét toàn chiều cao', 'Hốc trú trong sàn']
    A1, A2 = 'Area 1 · cổng pháo đài', 'Area 2 · hành lang tử thần'

    def H(r):  # hốc trú: rãnh nằm 1.6 ô dưới mặt sàn (lướt vào, laser đi qua phía trên)
        r.raw(('zone', 0, -0.2, 3, 0.8, 'dark', '')).note('▼hốc trú', 0, -1.4)
        return r

    r = R('R1', 'Cổng pháo đài', 3, 'Laser quét #1 chậm (từ trái sang, 140 px/s). Ba hốc trú trong sàn gần nhau (cách 6 ô): nằm vào hốc khi tia đi qua.',
          timing='laser #1 140 px/s, còi báo 1 s trước khi quét')
    r.zone(30, 'laser', 'laser #1 quét →', y0=1, walk=False).run(6, 'S').run(6).run(6).run(6, 'R').run(6)
    st.add(r.done(), A1)

    r = R('R2', 'Hành lang băng chuyền', 5, 'Băng chuyền nhanh 200 px/s và laser #2–#3 quét ngược chiều nhau; hốc trú xa nhau 10 ô. Drone thả mìn lên băng chuyền.',
          timing='băng chuyền 200 px/s; laser #2 160 px/s →, #3 160 px/s ←')
    r.zone(40, 'laser', 'laser #2 → / #3 ←', y0=1, walk=False).belt(14, 200, 'D'); H(r).run(4).belt(14, 200, 'B'); H(r).run(8)
    st.add(r.done(), A1)

    s = Shaft('R3', 'Giếng tia', 5, 'Leo giếng trong khi laser quét dọc theo chiều cao (từ dưới lên, 100 px/s). Kệ có hốc trú phía sau vách.',
              w=14, h=30, timing='laser dọc quét lên 100 px/s mỗi 5 s')
    s.add(('zone', 2, 20, 12, 21, 'laser', 'laser quét lên')).climb(step=2.5, ents={4: 'D', 6: 'R'})
    st.add(s.done(), A1)

    st.add(Arena('MID', 'Điểm dừng', 5, 'Mini-boss: lõi laser 45 HP điều khiển 2 tia chéo. Checkpoint 1 sau trận.', w=24, boss='M', note='lõi laser 45 HP',
                 timing='2 tia chéo xoay 30°/s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R4', 'Hành lang cuối', 6, 'Laser #4–#5 nhịp khác nhau (3 s và 4.5 s). Khối chắn che hốc trú phải bắn vỡ trước (8 HP).',
          timing='laser #4 mỗi 3 s, #5 mỗi 4.5 s; khối chắn 8 HP')
    r.zone(40, 'laser', 'laser #4 / #5', y0=1, walk=False).run(8, 'S').pillar(2, 1).run(10, 'D').pillar(2, 1).run(10, 'R').run(4)
    st.add(r.done(), A2)

    r = R('R6', 'Hành lang tử thần', 8, 'Cao trào: ba laser phối hợp + băng chuyền ngược −160 px/s. Hốc trú chỉ đủ 1 lần tia qua, phải chạy liên tục. '
          'Checkpoint 2 ở đầu phòng.', timing='laser #6 2.5 s, #7 3.5 s, #8 4 s; băng chuyền −160 px/s')
    r.ent('C', 2).run(4).zone(44, 'laser', 'laser #6/#7/#8', y0=1, walk=False).belt(16, -160, 'S'); H(r).run(4).belt(16, -160, 'D'); H(r).run(8, 'R')
    st.add(r.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước boss (hồi đầy HP + WEP).')
    r.run(6).ent('E', 0, 0, 'trạm năng lượng lớn').run(10)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Dynamo', 7, 'Đấu trường trống; Dynamo ném boomerang và gọi mạch nước nóng.', w=30), 'Boss')
    st.areas = [('Area 1', 'làm quen laser + hốc trú', ['R1', 'R2', 'R3']), ('Mid', 'lõi laser', ['MID']),
                ('Area 2', 'phối hợp nhiều nhịp laser', ['R4', 'R6', 'R7']), ('Boss', 'đấu trường trống', ['BOSS'])]
    st.boss_info = {'attacks': 'Boomerang Saber (ném vòng cung), Geyser (mạch nước nóng từ sàn), Leap Slash (nhảy chém).',
                    'arena': 'đấu trường 30×11 ô trống.', 'phase2': 'laser quét từ pháo đài bật lại theo nhịp 6 s trong lúc đấu.'}
    st.engine = ['Laser quét toàn chiều cao + còi báo', 'Hốc trú trong sàn', 'Băng chuyền nhanh', 'Khối chắn bắn vỡ']
    st.art = ['Hành lang pháo đài Sigma', 'Đầu phát laser', 'Hốc trú có nắp', 'Băng chuyền tốc độ cao']
    return st
