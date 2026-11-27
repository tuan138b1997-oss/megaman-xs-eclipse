from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_f1_nzero', 'Không gian ác mộng', 'Nightmare Zero', 'shadow', 'Pháo đài X6', 'fortress',
               'Không gian nhiễu tối: tầm nhìn thu hẹp quanh nhân vật (bán kính 220 px), vệt đèn quét làm lộ bệ thật và làm bệ ảo ảnh tan. '
               'Bệ ảo ảnh và bệ thật phản ứng ngược nhau với vệt đèn. Cao trào là giếng hai chiều trọng lực.',
               'X6 Nightmare Zero stage, X5 Zero Space, X8 Dark Mantis (tối).')
    st.mech = ['Vùng tối nhiễu', 'Bệ ảo ảnh và bệ thật phản ứng ngược nhau với vệt đèn quét']
    A1, A2 = 'Area 1 · hành lang nhiễu', 'Area 2 · giếng hai chiều'

    r = R('R1', 'Hành lang nhiễu', 5, 'Tầm nhìn bán kính 220 px; bệ ảo ảnh (viền nhấp nháy) không đứng được. Khe 3 ô trên vực.', timing='tầm nhìn 220 px', h=14)
    r.zone(40, 'dark', 'tầm nhìn 220 px', y0=1, walk=False).run(6, 'D').ledges(16, [(3, -1, 3), (9, -1, 3)], kind='ghost', land=4).run(6, 'S').run(4, 'R')
    st.add(r.done(), A1)

    r = R('R2', 'Bệ nhấp nháy', 6, 'Bệ đổi pha trên vực; vệt đèn quét (2 s một vòng) làm lộ bệ thật – trong vệt đèn bệ ảo biến mất.', timing='đèn quét 2 s; bệ pha 1.5 s', h=14)
    r.run(4).zone(30, 'light', 'vệt đèn quét', y0=1, walk=False).ledges(26, [(3, -1, 3), (9, -2, 3), (15, -1, 3), (21, 0, 3)], kind='phase', land=4).ent('D', -2).run(4, 'R')
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Điểm dừng', 5, 'Mini-boss: bóng Nightmare 45 HP chỉ hiện trong vệt đèn. Checkpoint 1.', w=24, boss='M', note='bóng Nightmare 45 HP',
                 timing='hiện 2 s / ẩn 2 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R3', 'Đảo trọng lực', 6, 'Trọng lực đảo: đi trên trần, nhảy qua 3 cụm gai trần (mỗi cụm 3 ô); rơi khỏi vùng đảo là rơi xuống hố gai.', timing='', h=12)
    r.run(6, 'S R').special(30, 'grav', 0, prims=[('pit', 0, 30, 'gai'), ('zone', 0, -9, 30, 0, 'grav', 'đảo trọng lực'), ('spikes', 6, 9, -9, 'ceil'), ('spikes', 15, 18, -9, 'ceil'), ('spikes', 23, 26, -9, 'ceil'),
                                               ('e', 'D', 20, -4)], land=6)
    st.add(r.done(), A2)

    s = Shaft('R5', 'Giếng hai chiều', 8, 'Cao trào: giếng tối, nửa trái trọng lực thường, nửa phải đảo; bệ thật/ảo đổi theo vệt đèn. Checkpoint 2 ở đáy.', w=16, h=36,
              timing='vệt đèn quét dọc 3 s')
    s.ent('C', 5, 34).add(('zone', 8, 2, 14, 34, 'grav', 'nửa phải đảo trọng lực'), ('zone', 2, 2, 14, 34, 'dark', '')).climb(step=2.5, kind='ghost', ents={3: 'D', 6: 'R', 9: 'S'})
    st.add(s.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước boss.')
    r.run(6).ent('E', 0, 0, 'trạm năng lượng lớn').run(10)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Nightmare Zero', 7, 'Bản sao Zero dùng Genmu Zero; thắng để mở khóa Zero thật.', w=30), 'Boss')
    st.areas = [('Area 1', 'hành lang nhiễu, bệ nhấp nháy', ['R1', 'R2']), ('Mid', 'bóng Nightmare', ['MID']), ('Area 2', 'đảo trọng lực, giếng hai chiều', ['R3', 'R5', 'R7']),
                ('Boss', 'không gian tối', ['BOSS'])]
    st.boss_info = {'attacks': 'Genmu Zero (sóng kiếm), Shippuuga (lướt chém), Ground Quake (đấm đất).', 'arena': '30×11 ô tối.',
                    'phase2': 'tầm nhìn thu còn 160 px; Nightmare Zero xuất hiện từ bóng tối sau lưng.'}
    st.engine = ['Tầm nhìn giới hạn quanh nhân vật', 'Bệ ảo ảnh/thật phản ứng với vệt đèn', 'Đảo trọng lực theo nửa giếng']
    st.art = ['Không gian nhiễu tím đen', 'Bệ ảo ảnh (viền nhấp nháy)', 'Vệt đèn quét']
    return st
