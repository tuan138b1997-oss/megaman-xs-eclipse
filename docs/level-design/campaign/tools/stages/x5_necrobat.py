from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_necrobat', 'Đài thiên văn', 'Dark Necrobat', 'shadow', 'Act I · X5', 'boss',
               'Đài thiên văn bỏ hoang trong đêm. Vùng trọng lực tùy chỉnh (0.42) cho nhảy cao và rơi chậm; vùng làm chậm thời gian tím '
               'làm chậm mọi thứ kể cả đạn địch. Area 1 lên đỉnh đài; Area 2 qua hành lang cổng và vòm sao băng, cao trào ở quỹ đạo hố đen.',
               'X5 Dark Necrobat (đài thiên văn), X3 Gravity Beetle (trọng lực), X8 Dark Mantis (bóng tối).')
    st.capsule_short = 'Gaea Head'
    st.mech = ['Vùng trọng lực tùy chỉnh', 'Vùng làm chậm thời gian']
    A1, A2 = 'Area 1 · lên đỉnh đài', 'Area 2 · vòm sao'

    r = R('R1', 'Sân đài', 2, 'Sân ngoài trời trong vùng trọng lực 0.42: nhảy cao ~6 ô, rơi chậm. Dơi máy (Drone) bay theo đàn 2 con.',
          timing='trọng lực ×0.42 trong vùng tím nhạt', ceil=None)
    r.run(6).zone(16, 'grav', 'trọng lực ×0.42', y0=1, ents='D D').special(8, 'fly', -4, prims=[('pit', 0, 8, 'vuc')], land=8).run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Vòm kính', 3, 'Khối nổi trôi chậm làm bệ trên vực; Time Zone tím ở giữa làm chậm mọi thứ ×0.5 (kể cả đạn Sniper) – dùng nó để qua khe.',
          timing='khối nổi trôi 40 px/s; Time Zone ×0.5', h=14)
    r.run(6, 'S').ledges(20, [(3, -1, 3), (9, -2, 3), (15, -1, 3)], kind='move', land=4).zone(8, 'slow', 'Time Zone ×0.5', y0=1, ents='R D').run(4)
    st.add(r.done(), A1)

    s = Shaft('R3', 'Phòng kính viễn vọng', 4, 'Leo dọc ống kính khổng lồ đang xoay chậm; thấu kính sáng đẩy lùi 2 ô khi chạm (vùng vàng).',
              w=14, h=30, timing='thấu kính đẩy lùi 2 ô; ống kính xoay 1 vòng / 20 s')
    s.add(('zone', 2, 14, 12, 16, 'light', 'thấu kính đẩy lùi')).climb(step=2.5, ents={2: 'D', 6: 'S'})
    st.add(s.done(), A1)

    r = R('R4', 'Đỉnh đài', 5, 'Cuối Area 1: bệ trôi + Time Zone. Capsule Gaea Head và Heart Tank ở đỉnh vòm phía trên (nhảy trọng lực nhẹ từ bệ trôi). '
          'Brute giữ lối ra.', timing='trọng lực ×0.42 phía trên vòm', h=14)
    r.run(6).ledges(16, [(3, -1, 3), (9, -1, 3)], kind='move', land=4).zone(6, 'grav', 'trọng lực ×0.42', y0=1)
    r.secret((-3, 0), (-3, -6), (0, -6)).raw(('ledge', -4, -6, 6, 'ke'), ('e', 'A', -2, -6, 'Gaea Head'), ('e', 'H', 1, -6, 'đỉnh vòm'))
    r.run(6, 'B').run(4)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Phòng điều khiển', 5, 'Mini-boss: cỗ máy chiếu sao 45 HP, bắn chòm sao đạn theo hình; tắt đèn khi trúng. Checkpoint 1 sau trận.',
                 w=24, boss='M', note='máy chiếu sao 45 HP', timing='chòm sao 6 đạn mỗi 2.2 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R5', 'Hành lang cổng', 5, 'Bốn cổng dịch chuyển theo cặp nối hai đoạn hành lang; một cổng phụ dẫn vào phòng kín có Sub-Tank. Sniper canh mỗi đầu cổng.',
          timing='cổng dịch chuyển tức thời, hồi 1 s')
    r.run(8, 'S').special(4, 'tele', 0, prims=[('note', 0, -5, 'cổng A→B')], land=8).ent('D', 2).run(6, 'S')
    r.secret((0, 0), (0, -6), (4, -6)).raw(('ledge', -1, -6, 6, 'ke'), ('e', 'T', 3, -6, 'phòng kín qua cổng phụ'))
    r.special(4, 'tele', 0, prims=[('note', 0, -5, 'cổng C→D')], land=8).ent('R', 0).run(4).ent('C', 0)
    st.add(r.done(), A2)

    r = R('R6', 'Quỹ đạo hố đen', 7, 'Cao trào. Vòm kính vỡ: thiên thạch rơi theo nhịp (bóng báo trước 0.8 s); bệ trôi quanh một hố đen hút nhẹ về giữa. '
          'Vực sâu bên dưới.', timing='hố đen hút 50 px/s về tâm; thiên thạch mỗi 1.2 s', h=14)
    r.run(6, 'B').ledges(24, [(3, -1, 3), (9, -2, 3), (15, -2, 3), (20, -1, 3)], kind='move', land=4).ent('D', -2)
    r.ledges(14, [(3, -1, 3), (9, -1, 3)], kind='move', land=4).ent('R', -2).run(6, 'D')
    st.add(r.done(), A2)

    r = R('R7', 'Cửa mái vòm', 2, 'Phòng nghỉ trước boss: Reploid cuối, cửa boss.')
    r.run(8, 'R').run(8)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Dark Necrobat', 6, 'Sân trọng lực nhẹ; dơi con hút máu khi bám người.', w=30), 'Boss')
    st.areas = [('Area 1', 'sân đài, vòm kính, kính viễn vọng, đỉnh đài', ['R1', 'R2', 'R3', 'R4']), ('Mid', 'máy chiếu sao', ['MID']),
                ('Area 2', 'hành lang cổng, quỹ đạo hố đen', ['R5', 'R6', 'R7']), ('Boss', 'vòm tối', ['BOSS'])]
    st.secrets = [('Capsule Gaea Head', 'R4', 'Đỉnh vòm, nhảy trọng lực nhẹ từ bệ trôi.'), ('Heart Tank', 'R4', 'Cạnh capsule trên đỉnh vòm.'),
                  ('Sub-Tank', 'R5', 'Phòng kín qua cổng phụ.')]
    st.boss_info = {'arena': 'vòm 30×11 ô trọng lực ×0.42.', 'phase2': 'trần mở ra, hố đen nhỏ ở giữa sân hút người chơi; Necrobat gọi đàn dơi theo vòng.'}
    st.engine = ['Vùng trọng lực tùy chỉnh', 'Vùng làm chậm thời gian (ảnh hưởng đạn địch)', 'Khối nổi trôi', 'Thấu kính đẩy lùi', 'Cổng dịch chuyển theo cặp', 'Hố đen hút về tâm']
    st.art = ['Đài thiên văn, vòm kính vỡ', 'Kính viễn vọng khổng lồ', 'Khối nổi', 'Cổng dịch chuyển', 'Thiên thạch + bóng báo trước', 'Hố đen']
    return st
