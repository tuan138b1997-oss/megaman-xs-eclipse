from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_f3_rangda', 'Zero Space 3', 'Rangda Bangda W', 'shadow', 'Pháo đài X5', 'fortress',
               'Biển gai trên sàn, vách và trần. Vùng đảo trọng lực cho phép đi trên trần qua biển gai. Capsule bí mật Ultimate Armor X5 '
               '(X) / Black Zero (Zero) nằm trong hốc trần của vùng đảo trọng lực.',
               'X5 Zero Space 3 (gai + trọng lực), X3 Gravity Beetle (đảo trọng lực), X1 Sigma stage (gai).')
    st.capsule_short = 'bí mật Black Zero / Ultimate Armor X5'
    st.mech = ['Vùng đảo trọng lực', 'Gai sàn/vách/trần']
    A1, A2 = 'Area 1 · hành lang gai', 'Area 2 · giếng xoay'

    r = R('R1', 'Hành lang gai', 4, 'Gai sàn rải rác 2–3 ô, kệ một chiều phía trên. Sniper trên kệ.', timing='gai: chết ngay khi chạm (trừ giáp miễn gai)')
    r.run(6).gap(2, 'gai').run(6, 'S').gap(3, 'gai').run(6, 'D').gap(3, 'gai').run(8, 'R').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Vùng đảo trọng lực', 6, 'Bước vào vùng tím: trọng lực đảo, đi trên trần qua biển gai dài 50 ô (1650 px theo dữ liệu game); gai trần có khe 3 ô. '
          'Hốc trần bí mật ở giữa: Secret Capsule.', timing='đảo trọng lực tức thời khi vào vùng tím; khe gai trần 3 ô')
    r.run(6).zone(50, 'grav', 'đảo trọng lực: đi trên trần', y0=1, walk=False)
    r.special(50, 'grav', 0, prims=[('pit', 0, 50, 'gai'), ('spikes', 0, 12, 1, 'ceil'), ('spikes', 15, 30, 1, 'ceil'), ('spikes', 33, 50, 1, 'ceil'),
                                     ('e', 'D', 10, -4), ('e', 'D', 32, -4), ('e', 'A', 24, -8.5, 'Secret Capsule (hốc trần)')], land=6)
    r.secret((-32, 0), (-32, -8.5), (-30, -8.5))
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Điểm dừng', 5, 'Mini-boss: mắt gai 45 HP bám trần, rơi xuống khi trúng đạn nạp. Checkpoint 1.', w=24, boss='M', note='mắt gai 45 HP',
                 timing='rơi gai mỗi 1.8 s', extra=lambda b: b.ent('C', -2).ent('R', -5)), 'Mid')

    s = Shaft('R4', 'Biển gai trọng lực ngược', 8, 'Cao trào: giếng trọng lực đổi chiều mỗi 3 s (đèn báo 1 s), gai hai bên vách; kệ so le ở cả hai chiều. '
              'Checkpoint 2 ở đáy giếng.', w=16, h=36, timing='trọng lực đổi chiều mỗi 3 s, báo trước 1 s')
    s.add(('zone', 2, 2, 14, 34, 'grav', 'trọng lực đổi chiều 3 s'), ('spikes', 2, 2.6, 22, 'wall'), ('spikes', 13.4, 14, 14, 'wall'))
    s.ent('C', 5, 34).climb(step=2.5, ents={2: 'D', 5: 'S', 8: 'R'})
    st.add(s.done(), A2)

    r = R('R5', 'Hành lang cuối', 6, 'Gai sàn + trần, khe 1.6 ô phải lướt; Brute chặn.', timing='')
    r.run(6, 'B').gap(3, 'gai').run(4).low(6, 1.6, 'khe gai: lướt').run(6, 'R').run(4)
    st.add(r.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước boss.')
    r.run(6).ent('E', 0, 0, 'trạm năng lượng lớn').run(10)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Rangda Bangda W', 7, 'Tường ép vào giữa; hai mắt và mũi là điểm yếu.', w=30), 'Boss')
    st.areas = [('Area 1', 'hành lang gai, vùng đảo trọng lực', ['R1', 'R2']), ('Mid', 'mắt gai', ['MID']),
                ('Area 2', 'giếng trọng lực đổi chiều', ['R4', 'R5', 'R7']), ('Boss', 'tường mặt quỷ', ['BOSS'])]
    st.secrets = [('Secret Capsule Ultimate X5 / Black Zero', 'R2', 'Hốc trần giữa vùng đảo trọng lực.')]
    st.boss_info = {'attacks': 'Eye Orbs (2 mắt bay bắn), Nose Dash (mũi lao), Wall Crush (tường ép).',
                    'arena': 'phòng 30×11 ô, hai vách ép vào.', 'phase2': 'vách ép vào 3 ô mỗi bên, mắt bắn chéo đồng thời.'}
    st.engine = ['Vùng đảo trọng lực', 'Giếng trọng lực đổi chiều theo nhịp', 'Gai sàn/vách/trần (chết ngay, giáp miễn)']
    st.art = ['Gai 3 hướng', 'Vùng tím đảo trọng lực', 'Đèn báo đổi trọng lực']
    return st
