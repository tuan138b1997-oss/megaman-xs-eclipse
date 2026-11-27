from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_turtloid', 'Đền Inami', 'Rainy Turtloid', 'nature', 'Act II · X6', 'boss',
               'Ngôi đền cổ dưới mưa axit xanh: mưa đến theo đợt (8 s mưa / 6 s tạnh), đứng ngoài mưa mất 1 HP mỗi 0.5 s; mái che trụ đá là chỗ trú. '
               'Area 1: cổng đền, sân đá, bậc đền với công tắc mở cổng. Area 2: mái đền có capsule Shadow Body, hành lang tượng phun axit, hồ axit cao trào.',
               'X6 Rainy Turtloid / Inami Temple (mưa axit), X4 Web Spider (rừng/đền), X8 Bamboo Pandamonium.')
    st.capsule_short = 'Shadow Body'
    st.mech = ['Mưa axit theo nhịp', 'Cổng mở bằng công tắc']
    A1, A2 = 'Area 1 · sân đền', 'Area 2 · mái đền và hồ axit'

    def roof(r, n=4):
        r.raw(('block', 0, -5, n, -4)).note('mái che', 0, -6)
        return r

    r = R('R1', 'Cổng đền', 3, 'Mưa axit bắt đầu; mái che đầu tiên dạy cách trú (bảng: đứng dưới mái khi trời mưa).', timing='mưa 8 s / tạnh 6 s; 1 HP mỗi 0.5 s khi dính mưa', ceil=None)
    r.run(6); roof(r).run(4).zone(14, 'rain', 'mưa axit 8s/6s', y0=1, ents='S D'); roof(r).run(4).run(6)
    st.add(r.done(), A1)

    r = R('R2', 'Sân đá', 4, 'Sân rộng 40 ô giữa các mái che cách nhau 8–10 ô: phải chạy hết quãng trong 6 s tạnh. Nightmare Virus bay chậm (Drone). Reploid dưới mái thứ 3.',
          timing='khoảng cách mái che 8–10 ô (chạy 250 px/s ≈ 1.2 s)', ceil=None)
    roof(r).run(4).zone(8, 'rain', '', y0=1, ents='D'); roof(r).run(4).zone(10, 'rain', '', y0=1, ents='S'); roof(r).run(4, 'R').zone(8, 'rain', '', y0=1, ents='D').run(4)
    st.add(r.done(), A1)

    s = Shaft('R3', 'Bậc đền', 4, 'Leo bậc đá có mái hiên che mưa từng tầng; công tắc #1 trên bậc giữa mở cổng đền phía trên.', w=14, h=28,
              timing='mưa rơi trong giếng; mái hiên che từng kệ')
    s.add(('zone', 2, 1, 12, 26, 'rain', 'mưa'), ('e', 'K', 10, 15, 'công tắc #1')).climb(step=2.5, ents={1: 'S', 4: 'D'})
    st.add(s.done(), A1)

    st.add(Arena('MID', 'Chính điện', 5, 'Trong nhà, hết mưa. Mini-boss: tượng hộ pháp 45 HP phun axit vòng cung. Checkpoint 1 sau trận.', w=26, boss='M',
                 note='tượng hộ pháp 45 HP', timing='phun axit vòng cung mỗi 2 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R4', 'Mái đền', 5, 'Đi trên mái tầng 2: capsule Shadow Body (X=3820 trong dữ liệu game) ở mái cao phía trên Heart Tank. Ngói trơn ở mép mái.',
          timing='mưa 8 s / tạnh 6 s', ceil=None)
    r.run(6, 'D').zone(10, 'rain', '', y0=1).pillar(3, 2).run(4).ent('H', 0, 0, 'dưới mái cao')
    r.secret((0, 0), (0, -2.5), (3, -5)).raw(('ledge', -1, -2.5, 3, 'ke'), ('ledge', 2, -5, 4, 'ke'), ('e', 'A', 4, -5, 'Shadow Body (mái cao)'))
    r.run(8, 'S').run(4)
    st.add(r.done(), A2)

    r = R('R5', 'Hành lang tượng', 5, 'Tượng đá hai bên phun axit theo nhịp lệch pha (vệt xanh báo trước). Cổng Alt Path (nhánh Nightmare Zero) ở giữa hành lang. '
          'Checkpoint 2 ở cuối.', timing='tượng phun 1 s mỗi 3 s, lệch pha 1.5 s')
    r.run(6, 'B').zone(4, 'rain', 'tượng phun', y0=4).run(4).note('cổng Alt Path → Nightmare Zero', 0, -6).zone(4, 'rain', 'tượng phun', y0=4).run(6, 'R').ent('C', 0).run(4)
    st.add(r.done(), A2)

    r = R('R6', 'Hồ axit', 7, 'Cao trào: hồ axit với lá sen nổi (chìm sau 1.5 s), mưa đổ liên tục ở nửa sau. Sub-Tank dưới mặt hồ ở vũng cạn (lướt xuống lấy rồi nhảy lên).',
          timing='lá sen chìm sau 1.5 s; mưa liên tục; axit 4 sát thương', h=14, ceil=None)
    r.run(4, 'D').ledges(22, [(3, -1, 3), (9, 0, 3), (15, -1, 3)], kind='log', pit='axit', land=4).ent('T', -2, 1, 'vũng cạn dưới mặt hồ')
    r.zone(18, 'rain', 'mưa liên tục', y0=1, walk=False).ledges(18, [(3, -1, 3), (9, -1, 3), (14, 0, 2)], kind='log', pit='axit', land=4).ent('R', -2).run(4, 'S')
    st.add(r.done(), A2)

    r = R('R7', 'Hồ sen', 2, 'Phòng nghỉ trong nhà thủy tạ: Reploid cuối, cửa boss.')
    r.run(8, 'R').run(8)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Rainy Turtloid', 6, 'Mưa axit theo đợt trong đấu trường; mai rùa phản đạn khi thu mình.', w=30), 'Boss')
    st.areas = [('Area 1', 'cổng, sân đá, bậc đền', ['R1', 'R2', 'R3']), ('Mid', 'chính điện', ['MID']), ('Area 2', 'mái đền, hành lang tượng, hồ axit', ['R4', 'R5', 'R6', 'R7']),
                ('Boss', 'sân đền', ['BOSS'])]
    st.secrets = [('Capsule Shadow Body', 'R4', 'Mái tầng cao phía trên Heart Tank.'), ('Heart Tank', 'R4', 'Dưới mái cao.'), ('Sub-Tank', 'R6', 'Vũng cạn dưới mặt hồ.'),
                  ('Alt Path Nightmare Zero', 'R5', 'Cổng giữa hành lang tượng.')]
    st.boss_info = {'arena': 'sân 30×11 ô có 2 mái che nhỏ.', 'phase2': 'mưa không tạnh; mái che sụp lần lượt (báo trước bằng vết nứt).'}
    st.engine = ['Mưa axit theo đợt, sát thương theo thời gian', 'Mái che an toàn', 'Tượng phun axit theo nhịp', 'Lá sen chìm dần', 'Cổng nhánh Alt Path']
    st.art = ['Đền Inami: mái ngói, trụ đá, tượng hộ pháp', 'Mưa axit xanh (hạt + vệt)', 'Hồ axit + lá sen']
    return st
