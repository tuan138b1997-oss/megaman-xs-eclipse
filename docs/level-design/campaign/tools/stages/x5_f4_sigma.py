from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_f4_sigma', 'Zero Space Final', 'Final Sigma W', 'core', 'Pháo đài X5', 'fortress',
               'Màn cuối Act I gom các đối tượng đã gặp: bệ di động trên vực + laser, giếng trọng lực, virus Sigma đuổi theo, '
               'rồi trục lõi virus với bệ chạy vòng quanh tâm. Kết thúc ở phòng quyết chiến Sigma.',
               'X5 Zero Space 4 (tổng hợp), X1 Sigma (đấu cuối), X8 Jakob elevator.')
    st.mech = ['Dùng lại đối tượng của Act I', 'Bệ chạy vòng quanh tâm trong trục dọc']
    A1, A2 = 'Area 1 · tổng hợp', 'Area 2 · trục lõi virus'

    r = R('R1', 'Tổng hợp 1', 5, 'Bệ di động trên vực + laser quét (nhắc Zero Space 1–2).', timing='laser 160 px/s; bệ ±3 ô', h=14)
    r.run(4, 'S').ledges(22, [(3, -1, 4), (11, -1, 4), (18, 0, 3)], kind='move', land=4).zone(10, 'laser', 'laser quét', y0=1, ents='D').ent('R', -1)
    st.add(r.done(), A1)

    s = Shaft('R2', 'Tổng hợp 2', 6, 'Giếng trọng lực biến thiên + gai (nhắc Zero Space 3).', w=14, h=30, timing='trọng lực ×0.6 ↔ ×1.4 mỗi 3 s')
    s.add(('zone', 2, 2, 12, 28, 'grav', 'trọng lực biến thiên'), ('spikes', 2, 2.6, 18, 'wall')).climb(step=2.5, ents={3: 'D', 6: 'R'})
    st.add(s.done(), A1)

    st.add(Arena('MID', 'Cổng quyết chiến', 5, 'Mini-boss: cổng virus 45 HP sinh virus Sigma. Checkpoint 1.', w=24, boss='M', note='cổng virus 45 HP',
                 timing='sinh virus mỗi 3 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R3', 'Hành lang Sigma', 6, 'Virus Sigma bay theo người chơi (chậm 120 px/s, bắn tan được), vùng làm chậm ở giữa.', timing='virus bám 120 px/s')
    r.run(8, 'D').zone(12, 'slow', 'vùng chậm', y0=1, ents='S').run(8, 'B R').run(4)
    st.add(r.done(), A2)

    s = Shaft('R5', 'Trục lõi virus', 8, 'Cao trào: trục dọc rộng 20 ô, bệ chạy vòng quanh lõi ở tâm (bán kính 6 ô, 1 vòng / 8 s); virus bay ra từ lõi. '
              'Checkpoint 2 ở đáy trục.', w=20, h=40, timing='bệ quay 1 vòng / 8 s; virus mỗi 2.5 s')
    s.ent('C', 6, 38).add(('zone', 8, 14, 12, 18, 'spark', 'lõi virus')).climb(step=2.5, kind='rotate', ents={3: 'D', 8: 'R', 11: 'R'})
    st.add(s.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước phòng quyết chiến.')
    r.run(6).ent('E', 0, 0, 'trạm năng lượng lớn').run(10)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Final Sigma W', 8, 'Hai pha: thân Sigma rồi đầu Sigma khổng lồ.', w=30), 'Boss')
    st.areas = [('Area 1', 'tổng hợp các đối tượng Act I', ['R1', 'R2']), ('Mid', 'cổng virus', ['MID']),
                ('Area 2', 'hành lang Sigma, trục lõi virus', ['R3', 'R5', 'R7']), ('Boss', 'phòng quyết chiến', ['BOSS'])]
    st.boss_info = {'attacks': 'Virus Swarm, Cube Drop, Sigma Beam (đầu khổng lồ), Ground Slam.',
                    'arena': '30×11 ô; pha 2 đầu Sigma chiếm nửa phải.', 'phase2': 'sàn sụp từng mảng 3 ô theo thứ tự trái→phải, báo trước bằng vết nứt.'}
    st.engine = ['Bệ chạy vòng quanh tâm', 'Trọng lực biến thiên theo nhịp', 'Virus bám đuổi', 'Sàn sụp theo mảng trong trận boss']
    st.art = ['Lõi virus Sigma', 'Bệ quay quanh lõi', 'Mảng sàn sụp']
    return st
