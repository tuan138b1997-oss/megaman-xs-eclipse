from lib import Stage
from kit import R, Arena, Shaft, TwoTier


def build():
    st = Stage('x5_rosered', 'Rừng đột biến', 'Spike Rosered', 'nature', 'Act I · X5', 'boss',
               'Rừng nấm khổng lồ bị virus Sigma làm đột biến. Nấm bật đưa người chơi lên tầng tán; bụi gai độc mọc lại sau khi bị bắn. '
               'Area 1 có tầng nấm hai lối và dây leo đu qua vực; Area 2 là đầm lầy làm chậm và thân cây cổ thụ cao trào.',
               'X5 Spike Rosered (rừng), X3 Toxic Seahorse (đầm), X4 Web Spider (rừng hai tầng).')
    st.capsule_short = 'Gaea Foot'
    st.mech = ['Bụi gai độc', 'Nấm bật']
    A1, A2 = 'Area 1 · bìa rừng và tầng nấm', 'Area 2 · đầm lầy và cây cổ thụ'

    r = R('R1', 'Bìa rừng', 2, 'Nấm bật đầu tiên (bật lên 900 px/s ≈ 6 ô) dạy nảy lên kệ cao. Bụi gai độc 2 ô chặn đường, bắn tan nhưng mọc lại sau 4 s.',
          timing='nấm bật 900 px/s; bụi gai mọc lại 4 s', ceil=None)
    r.run(8, 'S').special(4, 'mush', -4, prims=[('ledge', 0, 0, 2, 'mush')], land=6).ent('D', 3).step(2, 4).spikes(2).run(6).gap(2, 'gai').run(8, 'S').run(4)
    st.add(r.done(), A1)

    def top(t): t.run(8, 'D').gap(3, 'vuc').run(6).gap(4, 'vuc').run(8, 'R').gap(3, 'vuc').run(10)
    def bot(b): b.run(10, 'B').spikes(4).run(8, 'D').run(10, 'S').run(10)
    st.add(TwoTier('R2', 'Tầng nấm', 3, 'Hai tầng song song: tầng dưới nhiều địch và gai dây leo, tầng trên ít địch nhưng nhiều khe 3–4 ô. Lối chính là tầng trên; '
                   'nấm bật ở đầu phòng nối hai tầng.', top, bot, main='top', timing='khe tầng trên 3–4 ô'), A1)

    r = R('R3', 'Dây leo đu', 4, 'Dây leo treo trên vực: giữ Space để bám, thả để bay theo đà. Ba dây cách nhau 6–7 ô. Drone tuần dưới dây.',
          timing='dây đu biên độ ±60°, chu kỳ 2.4 s', h=14)
    r.run(6).special(26, 'vine', 0, prims=[('pit', 0, 26, 'vuc'), ('note', 3, -7, 'dây leo ×3 (giữ Space)'), ('e', 'D', 12, -4)], land=4).run(10, 'S R').run(4)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Lõi dây leo', 5, 'Mini-boss: lõi dây leo với 3 bông hoa phun gai; phải bắn hoa theo thứ tự đỏ → vàng → tím (sai thứ tự hoa mọc lại). '
                 'Checkpoint 1 sau trận.', w=30, boss='M', note='3 hoa, mỗi hoa 15 HP', timing='hoa phun gai mỗi 1.6 s',
                 extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R5', 'Đầm lấy', 5, 'Bùn làm chậm 40% và không lướt được. Bệ gỗ nổi chìm dần sau 1.5 s đứng. Heart Tank trên gò đất cao giữa đầm (nhảy từ bệ gỗ).',
          timing='bùn: tốc độ ×0.6; bệ gỗ chìm sau 1.5 s, nổi lại sau 3 s', h=13)
    r.run(4, 'S').zone(8, 'slow', 'bùn ×0.6', y0=7, ents='B').ledges(14, [(3, -1, 3), (9, -1, 3)], kind='log', pit='bun', land=4)
    r.secret((-2, 0), (0, -4)).raw(('block', -1, -4, 2, 0), ('e', 'H', 0.5, -4, 'gò đất'))
    r.zone(8, 'slow', '', y0=7, ents='S').run(4).ent('C', -2)
    st.add(r.done(), A2)

    s = Shaft('R6', 'Thân cây cổ thụ', 7, 'Cao trào. Leo trong lòng thân cây: kệ nấm so le, gai dây leo mọc trên vách (đá tường chỉ ở vùng vỏ trơn). '
              'Tán cây trên cùng bên trái có capsule Gaea Foot; Sub-Tank trong hốc giữa.', w=16, h=44,
              timing='gai vách mọc lại 4 s sau khi bị bắn')
    s.add(('spikes', 2, 3, 30, 'wall'), ('spikes', 13, 14, 20, 'wall'))
    s.climb(step=2.5, kind='mush', ents={2: 'D', 6: 'S'})
    s.add(('ledge', 3, 6, 4, 'ke'), ('e', 'A', 5, 6, 'Gaea Foot (tán cây)'), ('ledge', 2, 22, 2, 'ke'), ('e', 'T', 3, 22, 'hốc giữa'))
    s.secret((10, 10), (5, 6)).secret((5.5, 24), (3, 22))
    st.add(s.done(), A2)

    r = R('R7', 'Vườn hoa', 2, 'Phòng nghỉ: năng lượng nhỏ, hai Reploid, cửa boss.')
    r.run(8, 'R').run(6, 'R').run(8)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Spike Rosered', 6, 'Sàn có bụi gai mọc lại sau 4 s; boss treo trên dây leo trần.', w=30), 'Boss')
    st.areas = [('Area 1', 'bìa rừng, tầng nấm, dây leo', ['R1', 'R2', 'R3']), ('Mid', 'lõi dây leo', ['MID']),
                ('Area 2', 'đầm lầy, thân cây cổ thụ', ['R5', 'R6', 'R7']), ('Boss', 'vườn gai', ['BOSS'])]
    st.secrets = [('Capsule Gaea Foot', 'R6', 'Tán cây trên cùng bên trái (Falcon bay hoặc nấm + lướt trên không).'),
                  ('Heart Tank', 'R5', 'Gò đất giữa đầm, nhảy từ bệ gỗ.'), ('Sub-Tank', 'R6', 'Hốc giữa thân cây.')]
    st.boss_info = {'arena': 'vườn 30×11 ô, dây leo trên trần cho boss treo.',
                    'phase2': 'bụi gai mọc kín 1/3 sân mỗi 8 s (luân phiên trái/giữa/phải), báo trước bằng nụ hoa.'}
    st.engine = ['Bụi gai độc mọc lại', 'Nấm bật', 'Dây leo đu (bám/thả)', 'Bùn làm chậm, cấm lướt', 'Bệ gỗ chìm dần']
    st.art = ['Nấm khổng lồ (bệ + nấm bật)', 'Bụi gai độc', 'Dây leo đu', 'Đầm bùn, bệ gỗ nổi', 'Lòng thân cây cổ thụ']
    return st
