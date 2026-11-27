from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_yammark', 'Khu Amazon', 'Commander Yammark', 'nature', 'Act II · X6', 'boss',
               'Rừng mưa Amazon. Area 1: bìa rừng, bờ sông với khúc gỗ trôi. Ngã ba ở mini-boss tách hai nhánh: nhánh trên tán cây có capsule Blade Foot, '
               'nhánh dưới hang có Heart Tank; hai nhánh nhập lại trước thác nước cao trào.',
               'X6 Commander Yammark (rừng Amazon), X4 Web Spider (rừng), X2 Wire Sponge (cây).')
    st.capsule_short = 'Blade Foot'
    st.mech = ['Khúc gỗ trôi', 'Bệ hoa nở/khép theo nhịp']
    A1, A2 = 'Area 1 · bìa rừng và sông', 'Area 2 · hai nhánh và thác'

    r = R('R1', 'Bìa rừng mưa', 2, 'Côn trùng máy (Drone) bay theo đàn; cây gãy làm cầu qua khe nhỏ.', ceil=None)
    r.run(8, 'D').gap(2).run(8, 'S').gap(3).run(8, 'D R').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Bờ sông', 3, 'Khúc gỗ trôi trên sông (về phải 60 px/s) làm bệ di động; Reploid trên tảng đá giữa sông.', timing='gỗ trôi +60 px/s', h=14, ceil=None)
    r.run(6, 'S').ledges(22, [(3, -1, 4), (11, -1, 4), (18, 0, 3)], kind='log', pit='nuoc', land=4).ent('R', -2).run(6)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Ngã ba', 5, 'Mini-boss: tổ chuồn chuồn máy 45 HP. Checkpoint 1 sau trận; ngã ba tách nhánh trên (tán cây) và nhánh dưới (hang).', w=26, boss='M',
                 note='tổ chuồn chuồn 45 HP', timing='thả 3 chuồn chuồn mỗi 4 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R3a', 'Nhánh trên: tán cây', 5, 'Lá lớn làm bệ nảy, bệ hoa nở/khép (2 s/2 s). Capsule Blade Foot ở X=4550 (dữ liệu game).', timing='hoa nở 2 s / khép 2 s', h=14, ceil=None)
    r.run(4, 'D').ledges(20, [(3, -1, 3), (9, -2, 3), (15, -1, 3)], kind='flower', land=4).ent('A', -2, 0, 'Blade Foot').run(6, 'S').run(4)
    st.add(r.done(), A2)

    b = R('R3b', 'Nhánh dưới: hang', 4, 'Hang tối với côn trùng phát sáng soi đường; Heart Tank cuối hang. Brute canh lối ra.', timing='vùng tối: chỉ thấy quanh côn trùng sáng')
    b.zone(20, 'dark', 'hang tối', y0=1, ents='B').ent('H', -2, 0, 'cuối hang').run(4)
    rb = b.done(); rb.branch = True
    st.add(rb, A2)

    r = R('R7', 'Thác nước', 7, 'Cao trào: hai nhánh nhập lại; leo bậc đá cạnh thác, nước đổ đẩy xuống ở các khe; khúc gỗ trôi xuống thác. Checkpoint 2.',
          timing='thác đẩy xuống 120 px/s trong khe; gỗ rơi mỗi 2 s', h=14, ceil=None)
    r.ent('C', 2).run(4, 'S').step(-2, 4).zone(3, 'current', 'thác', y0=1).step(-2, 4).ent('D', 2).zone(3, 'current', '', y0=1)
    r.step(-2, 4).ledges(14, [(3, 0, 3), (9, -1, 3)], kind='log', pit='nuoc', land=4).ent('R', -2).run(4, 'D')
    st.add(r.done(), A2)

    r = R('R4', 'Đền lá', 2, 'Hai nhánh hội tụ; Sub-Tank trên bàn thờ lá, Reploid, cửa boss.')
    r.run(6, 'R').ent('T', 2, 0, 'bàn thờ lá').run(6, 'S').run(6)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Commander Yammark', 6, 'Boss gọi 3 chuồn chuồn vệ tinh xoay quanh.', w=30), 'Boss')
    st.areas = [('Area 1', 'bìa rừng, bờ sông', ['R1', 'R2']), ('Mid', 'ngã ba', ['MID']), ('Area 2', 'nhánh trên/dưới, thác nước', ['R3a', 'R3b', 'R7', 'R4']),
                ('Boss', 'đền lá', ['BOSS'])]
    st.secrets = [('Capsule Blade Foot', 'R3a', 'Nhánh trên.'), ('Heart Tank', 'R3b', 'Cuối hang nhánh dưới.'), ('Sub-Tank', 'R4', 'Bàn thờ lá.')]
    st.boss_info = {'arena': 'đền lá 30×11 ô.', 'phase2': 'mưa rừng làm sàn trơn; chuồn chuồn vệ tinh tách ra lao thẳng.'}
    st.engine = ['Khúc gỗ trôi', 'Bệ hoa nở/khép', 'Ngã ba nhánh (camera theo nhánh)', 'Vùng tối có nguồn sáng di động', 'Thác nước đẩy xuống']
    st.art = ['Rừng mưa nhiều lớp', 'Khúc gỗ, sông', 'Hoa nở/khép', 'Hang tối + côn trùng sáng', 'Thác nước']
    return st
