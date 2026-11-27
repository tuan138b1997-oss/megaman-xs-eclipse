from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_mijinion', 'Trung tâm vũ khí', 'Infinity Mijinion', 'metal', 'Act II · X6', 'boss',
               'Trung tâm thử vũ khí ở Tây Úc. Siêu phi thuyền Illumina lượn trên trời, vòng ngắm bám người chơi rồi bắn xuống (vòng chuyển đỏ đậm 1 s trước). '
               'Giữa màn là mini-boss lõi cáp Illumina; Area 2 là vực lớn với bệ treo cáp đung đưa.',
               'X6 Infinity Mijinion / Weapon Center, X8 Optic Sunflower? – X5 bệ cáp, X2 Crystal Snail.')
    st.refs = 'X6 Infinity Mijinion / Weapon Center (vòng ngắm Illumina), X4 Split Mushroom (bệ treo), X8 Avalanche Yeti (vực lớn).'
    st.capsule_short = 'Blade Head'
    st.mech = ['Tâm ngắm bám người chơi', 'Bệ treo cáp']
    A1, A2 = 'Area 1 · bãi thử', 'Area 2 · vực cáp'

    def cover(r, n=4):
        r.raw(('block', 0, -4.5, n, -3.5)).note('mái che', 0, -5.5)
        return r

    r = R('R1', 'Bãi thử', 3, 'Illumina lượn trên trời; vòng ngắm đỏ bám theo, đỏ đậm 1 s rồi bắn. Đứng dưới mái che khi vòng đỏ đậm.', timing='vòng ngắm bám 180 px/s; bắn sau 1 s đỏ đậm', ceil=None)
    r.run(6, 'S'); cover(r).run(4).run(10, 'D'); cover(r).run(4).run(8, 'S').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Khu chứa', 4, 'Thùng vũ khí phát nổ khi bị bắn (bán kính 3 ô) – dùng để diệt Brute. Reploid sau dãy thùng.', timing='thùng nổ bán kính 3 ô, 8 sát thương')
    r.run(6, 'D').pillar(2, 2).run(6, 'B').pillar(2, 2).run(6, 'S R').run(4)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Lõi cáp Illumina', 5, 'Mini-boss: phá 3 lõi cáp neo Illumina (mỗi lõi 15 HP) trong khi vòng ngắm vẫn bám. Checkpoint 1.', w=30, boss='M',
                 note='3 lõi cáp × 15 HP', timing='vòng ngắm bắn mỗi 3 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R3', 'Vực cáp lớn', 7, 'Cao trào: 7 bệ treo cáp đung đưa trên vực; bắn đứt cáp thì bệ rơi (đừng bắn nhầm). Drone bay giữa vực. Checkpoint 2 trên bệ cứng giữa.',
          timing='bệ cáp đung đưa ±2 ô, chu kỳ 3 s', h=14, ceil=None)
    r.run(4, 'D').ledges(22, [(3, -1, 3), (9, -2, 3), (15, -1, 3), (19, 0, 2)], kind='cable', land=4).ent('C', -2)
    r.ledges(20, [(3, -1, 3), (9, -2, 3), (15, -1, 3)], kind='cable', land=4).ent('D', -2).run(4, 'S R')
    st.add(r.done(), A2)

    r = R('R4', 'Bệ cáp cuối', 5, 'Capsule Blade Head trên bệ cáp cuối (X=5020 dữ liệu game); Heart Tank trên giàn treo phía trên. Sniper trên giàn.', timing='', h=14, ceil=None)
    r.run(6, 'S').ledges(14, [(3, -1, 3), (9, -1, 3)], kind='cable', land=4).ent('A', -2, 0, 'Blade Head')
    r.secret((0, 0), (2, -4.5)).raw(('ledge', 1, -4.5, 4, 'ke'), ('e', 'H', 3, -4.5, 'giàn treo')).run(6, 'B').run(4)
    st.add(r.done(), A2)

    r = R('R5', 'Hầm thử nghiệm', 3, 'Phòng nghỉ: Sub-Tank trong tủ vũ khí, Reploid, cửa boss.')
    r.run(6, 'R').ent('T', 2, 0, 'tủ vũ khí').run(6, 'R').run(6)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Infinity Mijinion', 6, 'Boss nhân bản khi trúng đạn thường; diệt bản gốc bằng đạn nạp.', w=30), 'Boss')
    st.areas = [('Area 1', 'bãi thử, khu chứa', ['R1', 'R2']), ('Mid', 'lõi cáp Illumina', ['MID']), ('Area 2', 'vực cáp, bệ cáp cuối', ['R3', 'R4', 'R5']),
                ('Boss', 'hầm thử', ['BOSS'])]
    st.secrets = [('Capsule Blade Head', 'R4', 'Bệ cáp cuối.'), ('Heart Tank', 'R4', 'Giàn treo phía trên.'), ('Sub-Tank', 'R5', 'Tủ vũ khí.')]
    st.boss_info = {'arena': 'hầm 30×11 ô.', 'phase2': 'bản sao không biến mất sau 5 s mà tồn tại tới khi trúng; vòng ngắm Illumina bật lại trong đấu trường.'}
    st.engine = ['Vòng ngắm bám người chơi + bắn trễ', 'Mái che chặn đạn trên cao', 'Thùng nổ', 'Bệ treo cáp đung đưa, bắn đứt cáp']
    st.art = ['Bãi thử vũ khí sa mạc', 'Vòng ngắm Illumina', 'Thùng vũ khí', 'Bệ treo cáp + cáp']
    return st
