from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_f5_bossrush', 'Phòng thí nghiệm cuối', '8 boss → Hell Sigma', 'core', 'Pháo đài X6', 'fortress',
               'Trục rơi đầy gai dẫn xuống băng chuyền đáy có trần gai, rồi trung tâm 8 cổng Boss Rush (đánh lại 8 boss Act II), cuối cùng là cầu thang Sigma '
               'và Hell Sigma.',
               'X6 Gate Lab 4, X5 Zero Space 4 (boss rush), X1 Sigma Palace (cầu thang).')
    st.mech = ['Băng chuyền và trần gai', 'Sảnh 8 cổng']
    A1, A2 = 'Area 1 · trục rơi và băng chuyền', 'Area 2 · Boss Rush và cầu thang Sigma'

    s = Shaft('R1', 'Trục rơi', 7, 'Rơi xuống trục 20 ô rộng: gai hai bên vách, gai nhô ra theo nhịp (đèn báo 0.6 s); lướt ngang trên không để né, kệ nghỉ so le.',
              w=20, h=44, up=False, timing='gai nhô 1 s mỗi 3 s, báo trước 0.6 s')
    s.add(('spikes', 2, 2.6, 22, 'wall'), ('spikes', 17.4, 18, 30, 'wall')).climb(step=3, ents={2: 'D', 6: 'R'})
    st.add(s.done(), A1)

    r = R('R2', 'Băng chuyền đáy', 6, 'Băng chuyền ngược + trần gai hạ thấp (khe 3 ô) + laser quét.', timing='băng −160 px/s; laser 180 px/s')
    r.run(4, 'S').raw(('block', 0, 1, 30, 6.5)).spikes(30, 'ceil', 6.5).belt(14, -160, 'D').run(4).belt(12, -160).run(4, 'R')
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Trung tâm Boss Rush', 6, 'Mini-boss: sảnh 8 cổng (2 hàng × 4), mỗi cổng đánh lại một boss Act II (tính là 1 mini-boss chuỗi). '
                 'Checkpoint 1 khi vào sảnh; hồi 12 HP sau mỗi trận.', w=30, boss='M', note='8 boss Act II', timing='hồi 12 HP + 100 WEP sau mỗi trận',
                 extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R3', 'Cầu thang Sigma', 8, 'Cao trào: cầu thang bậc 2 ô đi lên, virus Sigma đuổi, gai giữa các bậc, sàn sụp ở 3 bậc. Checkpoint 2 ở chân cầu thang.',
          timing='bậc sụp sau 1 s; virus bám 140 px/s')
    r.ent('C', 2).run(4, 'D').step(-2, 4).gap(2, 'gai', -2).step(-2, 4).ent('S', 2).gap(2, 'gai', -2).step(-2, 4).ent('R', 2).run(4, 'B')
    st.add(r.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước Hell Sigma; Reploid cuối.')
    r.run(6, 'R').ent('E', 0, 0, 'trạm năng lượng lớn').run(10, 'D')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Hell Sigma', 9, 'Ba pha: thân, đầu, lõi; sàn sụp và virus.', w=30), 'Boss')
    st.areas = [('Area 1', 'trục rơi, băng chuyền đáy', ['R1', 'R2']), ('Mid', 'sảnh 8 cổng Boss Rush', ['MID']), ('Area 2', 'cầu thang Sigma', ['R3', 'R7']),
                ('Boss', 'phòng Hell Sigma', ['BOSS'])]
    st.boss_info = {'attacks': 'Virus Rain, Hand Crush, Head Beam, Core Laser (3 pha).', 'arena': '30×11 ô, pha 3 sàn chỉ còn 3 bệ.',
                    'phase2': 'sàn sụp từng mảng còn 3 bệ, virus bay theo vòng; pha 3 lõi Sigma bắn laser quét toàn sân.'}
    st.engine = ['Gai nhô theo nhịp trong trục rơi', 'Trần gai hạ thấp', 'Sảnh 8 cổng Boss Rush (hồi máu giữa trận)', 'Cầu thang bậc sụp + virus đuổi']
    st.art = ['Trục rơi gai', 'Sảnh 8 cổng', 'Cầu thang Sigma', 'Hell Sigma (3 pha)']
    return st
