from lib import Stage
from kit import R, Arena, Shaft, TwoTier


def build():
    st = Stage('x5_pegacion', 'Không quân', 'Spiral Pegacion', 'wind', 'Act I · X5', 'boss',
               'Chiến dịch trên không: nhảy giữa bốn chiến hạm đang bay. Gió giật theo lịch đẩy về mép boong; luồng khí nâng nối các hạm. '
               'Area 1: đường băng, hạm 1, tầng mây; mini-boss pháo đài hộ tống. Area 2: hạm 3 boong nghiêng, hạm 4 có capsule Gaea Body.',
               'X5 Spiral Pegacion (không quân), X2 Wire Sponge? không – X4 Storm Owl (chiến hạm), X8 Gigabolt Man-O-War (trên không).')
    st.refs = 'X5 Spiral Pegacion (không quân), X4 Storm Owl (chiến hạm bay), X8 Gigabolt Man-O-War (trên không).'
    st.capsule_short = 'Gaea Body'
    st.mech = ['Gió giật theo lịch', 'Luồng khí nâng']
    A1, A2 = 'Area 1 · đường băng và hạm 1', 'Area 2 · hạm 3–4'

    r = R('R1', 'Đường băng cất cánh', 2, 'Đường băng trên tàu sân bay; máy bay địch (Drone) cất cánh lao thấp theo đường băng. Gió ngang nhẹ.',
          timing='gió ngang −30 px/s', ceil=None)
    r.run(10, 'S').zone(16, 'wind', 'gió −30', y0=1, ents='D').run(6, 'S').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Chiến hạm 1', 3, 'Boong có tháp pháo; gió giật mỗi 5 s (cờ đỏ báo trước 1 s) đẩy 120 px/s về mép. Cuối hạm là quạt nâng đưa sang hạm 2.',
          timing='gió giật 120 px/s trong 1.5 s, mỗi 5 s; cờ báo trước 1 s', ceil=None, h=14)
    r.run(6, 'D').zone(14, 'wind', 'gió giật mỗi 5 s', y0=1, ents='S R').gap(3).run(6)
    r.special(10, 'updraft', -3, prims=[('pit', 0, 10, 'vuc'), ('zone', 2, -8, 8, 4, 'updraft', 'quạt nâng')], land=6)
    st.add(r.done(), A1)

    def top(t): t.run(6).gap(3).run(5, 'D').gap(4).run(6).gap(3).run(8)
    def bot(b): b.run(12, 'D').special(10, 'updraft', 0, prims=[('zone', 2, -8, 8, 0, 'updraft', '')], land=4).run(10)
    st.add(TwoTier('R3', 'Tầng mây', 4, 'Hai tầng mây: tầng trên là khối mây cứng trôi chậm (khe 3–4 ô), tầng dưới là lưới an toàn có luồng khí nâng đưa trở lại. '
                   'Rơi khỏi tầng dưới mới mất mạng.', top, bot, main='top', timing='mây trôi 30 px/s; luồng nâng 600 px/s'), A1)

    st.add(Arena('MID', 'Pháo đài hộ tống', 5, 'Mini-boss: pháo đài bay hộ tống 50 HP, bắn tên lửa bám và pháo quét. Checkpoint 1 và Heart Tank trên boong sau khi hạ '
                 '(dữ liệu game: X=3950).', w=30, boss='M', note='pháo đài 50 HP', timing='tên lửa bám mỗi 2.5 s',
                 extra=lambda b: b.ent('C', -4).ent('H', -2, 0, 'boong sau')), 'Mid')

    r = R('R4', 'Chiến hạm 3', 5, 'Boong nghiêng theo nhịp ±8° (nhân vật trượt nhẹ). Khối thép rơi từ cần cẩu. Brute canh giữa boong.',
          timing='boong nghiêng ±8° chu kỳ 4 s; khối rơi mỗi 2 s', ceil=None, h=14)
    r.run(6, 'S').slope(8, -1).slope(8, 1).run(6, 'B').gap(4).run(6, 'R').run(4)
    st.add(r.done(), A2)

    r = R('R5', 'Tầng mây cao', 7, 'Cao trào. Cưỡi luồng khí nâng lên boong trên cùng của hạm 4 giữa gió giật; khối mây cứng là bệ nghỉ. '
          'Capsule Gaea Body cuối boong trên; Sub-Tank ở khoang cánh. Checkpoint 2 trước luồng nâng.', timing='gió giật mỗi 4 s; luồng nâng 600 px/s',
          ceil=None, h=14)
    r.run(4).ent('C', 0).run(4, 'D').special(10, 'updraft', -3, prims=[('pit', 0, 10, 'vuc'), ('zone', 2, -8, 8, 4, 'updraft', 'luồng nâng')], land=4)
    r.ledges(18, [(3, -1, 3), (9, -2, 3), (14, -1, 3)], kind='cloud', land=4).ent('S', -2).run(6, 'D')
    r.secret((0, 0), (2, -4.5), (6, -4.5)).raw(('ledge', 1, -4.5, 6, 'ke'), ('e', 'A', 5, -4.5, 'Gaea Body (boong trên)'), ('e', 'T', 2, 0, 'khoang cánh')).run(6, 'R')
    st.add(r.done(), A2)

    r = R('R6', 'Cầu chỉ huy', 2, 'Phòng nghỉ: Reploid, cửa boss.')
    r.run(8, 'R').run(8)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Spiral Pegacion', 6, 'Đấu trên boong mở; gió xoáy đẩy về mép.', w=30), 'Boss')
    st.areas = [('Area 1', 'đường băng, hạm 1, tầng mây', ['R1', 'R2', 'R3']), ('Mid', 'pháo đài hộ tống', ['MID']),
                ('Area 2', 'hạm 3 boong nghiêng, hạm 4', ['R4', 'R5', 'R6']), ('Boss', 'boong mở', ['BOSS'])]
    st.secrets = [('Capsule Gaea Body', 'R5', 'Boong trên cùng hạm 4, cưỡi luồng nâng.'), ('Heart Tank', 'MID', 'Boong sau khi hạ pháo đài.'),
                  ('Sub-Tank', 'R5', 'Khoang cánh hạm 4.')]
    st.boss_info = {'arena': 'boong 30×11 ô không trần, hai mép boong là vực.', 'phase2': 'gió xoáy đổi chiều mỗi 4 s và mạnh gấp đôi; boong co lại 3 ô mỗi bên.'}
    st.engine = ['Gió giật theo lịch (cờ báo trước)', 'Luồng khí nâng', 'Khối mây cứng trôi', 'Boong nghiêng theo nhịp', 'Khối thép rơi từ cần cẩu']
    st.art = ['Boong chiến hạm, tháp pháo', 'Quạt nâng', 'Khối mây', 'Cờ báo gió', 'Nền trời + mây parallax']
    return st
