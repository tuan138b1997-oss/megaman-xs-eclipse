from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_grizzly', 'Tàu bọc thép', 'Crescent Grizzly', 'metal', 'Act I · X5', 'boss',
               'Đoàn tàu bọc thép 8 toa lao qua sa mạc. Area 1 chạy trên nóc toa trong gió ngược, nhảy qua các khớp nối đang tách; '
               'Area 2 chui vào khoang hàng có băng chuyền, cưỡi Ride Armor đục vách toa 6 lấy Falcon Foot, rồi lên nóc đầu tàu né các hầm đá.',
               'X5 Crescent Grizzly (tàu bọc thép), X8 Earthrock Trilobite (bị vật lớn đuổi), X2 Overdrive Ostrich (tốc độ, nền trôi).')
    st.capsule_short = 'Falcon Foot'
    st.mech = ['Gió ngược trên nóc toa', 'Khớp nối toa tách theo thời gian']
    A1, A2 = 'Area 1 · nóc tàu', 'Area 2 · khoang hàng và đầu tàu'

    r = R('R1', 'Sân ga', 2, 'Tàu khởi hành sau 3 giây: sân ga đứng yên, nền parallax bắt đầu trôi. Dạy nhảy lên thùng hàng và bắn Sniper đứng trên nóc toa đầu.',
          timing='tàu khởi hành sau 3 s; nền parallax trôi 240 px/s', ceil=None)
    r.run(8).note('tàu khởi hành sau 3 s', 1, -5).run(6, 'S').pillar(3, 2).run(6).step(-2, 8).ent('D', 3).run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Nóc toa 1–3', 3, 'Gió ngược −55 px/s trên nóc. Ba khớp nối có khe 2–3 ô; Sniper ở cuối mỗi toa. Thùng hàng là vật che đạn.',
          timing='gió ngược −55 px/s (chạy còn 195 px/s); khe khớp nối 2–3 ô', ceil=None)
    r.zone(16, 'wind', '← gió −55 px/s', y0=1, ents='S').gap(2).zone(14, 'wind', '', y0=1, ents='D')
    r.pillar(2, 2).gap(3).zone(12, 'wind', '', y0=1, ents='S R').gap(2).run(6)
    st.add(r.done(), A1)

    r = R('R3', 'Khớp nối tách', 4, 'Đứng gần khớp nối 6 s thì khe mở rộng dần từ 0 lên 6 ô (đèn đỏ chớp 1 s trước khi mở). '
          'Khe đã mở quá 5 ô phải lướt-nhảy. Drone bay ngang thả bom đúng khe.',
          timing='khe 0→6 ô trong 6 s, chớp đỏ 1 s trước khi mở; Drone thả bom mỗi 2.5 s', ceil=None)
    r.run(8, 'S').note('khe 0→6 ô / 6 s', 0, -4).gap(4).run(6).ent('D', 0).gap(5).run(8).gap(3).run(4)
    st.add(r.done(), A1)

    s = Shaft('R4', 'Toa cần cẩu', 4, 'Toa chở cần cẩu: leo lên đỉnh cần cẩu bằng các bệ hàng treo (lắc nhẹ theo tàu). '
              'Reploid bị kẹt ở bệ giữa. Từ đỉnh cần cẩu nhìn thấy đầu máy phía trước.', w=14, h=30,
              timing='bệ treo lắc ±0.5 ô theo nhịp 2 s')
    s.climb(step=2.5, kind='cable', ents={3: 'R', 6: 'D'})
    st.add(s.done(), A1)

    st.add(Arena('MID', 'Xe tải bọc thép', 5, 'Mini-boss: xe tải (truck) chạy song song trên toa sàn phẳng, bắn pháo cong và lao húc. '
                 'Hạ xong: checkpoint 1 và cửa Area 2 mở.', w=30, boss='M', note='truck 45 HP',
                 timing='pháo cong mỗi 1.8 s; húc ngang mỗi 6 s (cảnh báo khói 1 s)',
                 extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R5', 'Toa Ride Armor', 5, 'Khoang hàng: băng chuyền đẩy ngược −80 px/s. Ride Armor Pod ở đầu toa; cưỡi nó đấm vỡ vách thép nứt ở toa 6 '
          '→ khoang kín có capsule Falcon Foot. Sub-Tank trên kệ hàng cao.', timing='băng chuyền −80 px/s; vách nứt 16 HP (chỉ Ride Armor phá được)')
    r.run(6).ent('V', 3, 0, 'Ride Armor Pod').run(2).belt(14, -80, 'B').breakwall(4).note('vách nứt', 0, -5).run(4)
    r.secret((-4, 0), (-4, 1.5), (2, 1.5)).belt(10, -80, 'S').pillar(2, 2).run(3).ent('T', 0, -2.5)
    r.raw(('ledge', -1, -2.5, 3, 'ke')).run(8, 'D').run(4)
    r.raw(('e', 'A', -18, 1.5, 'Falcon Foot (khoang kín dưới sàn)'), ('block', -20, 0, -14, 2))
    st.add(r.done(), A2)

    r = R('R6', 'Nóc toa đầu và hầm', 7, 'Cao trào. Gió mạnh −90 px/s; hai hầm đá quét qua nóc: trần hạ còn 1.6 ô, phải lướt sát nóc trước khi hầm tới '
          '(đèn đỏ + tiếng còi 1.5 s). Khe khớp nối 4 ô giữa hai hầm. Heart Tank trên nóc ống khói thấp giữa hai hầm.',
          timing='gió −90 px/s; hầm tới mỗi 8 s, cảnh báo 1.5 s; khe 4 ô', ceil=None)
    r.zone(10, 'wind', '← gió −90 px/s', y0=1, ents='S').ent('C', -4).low(8, 1.6, 'hầm 1: lướt').run(4).gap(4).run(6, 'D')
    r.secret((-3, 0), (-3, -2.5), (-1, -2.5)).raw(('block', -3, -2.5, -1, 0), ('e', 'H', -2, -2.5, 'trên ống khói'))
    r.low(8, 1.6, 'hầm 2: lướt').zone(10, 'wind', '', y0=1, ents='B').run(4)
    st.add(r.done(), A2)

    r = R('R7', 'Toa chỉ huy', 2, 'Phòng nghỉ trong toa chỉ huy: năng lượng nhỏ, Reploid cuối, cửa boss.', timing='')
    r.run(6, 'R').run(6).ent('R', 0).run(8)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Crescent Grizzly', 6, 'Đấu trên nóc toa chỉ huy dài 30 ô, có gió ngang đổi chiều mỗi 6 s.', w=30,
                 timing='gió ngang ±60 px/s, đổi chiều mỗi 6 s'), 'Boss')

    st.areas = [('Area 1', 'sa mạc, nóc tàu, gió ngược', ['R1', 'R2', 'R3', 'R4']), ('Mid', 'mini-boss xe tải bọc thép', ['MID']),
                ('Area 2', 'khoang hàng và đầu tàu', ['R5', 'R6', 'R7']), ('Boss', 'nóc toa chỉ huy', ['BOSS'])]
    st.secrets = [('Capsule Falcon Foot', 'R5', 'Cưỡi Ride Armor đấm vỡ vách nứt toa 6, rơi vào khoang kín dưới sàn.'),
                  ('Heart Tank', 'R6', 'Đá tường lên nóc ống khói giữa hai hầm.'), ('Sub-Tank', 'R5', 'Kệ hàng cao sau đoạn băng chuyền thứ hai.')]
    st.boss_info = {'arena': 'nóc toa 30×11 ô, không trần (bầu trời), hai đầu là mép toa (rơi = mất máu, không chết).',
                    'phase2': 'gió ngang mạnh gấp đôi và tàu chui hầm: trần hạ còn 4 ô trong 3 s mỗi 12 s, Grizzly đào xuống sàn tránh.'}
    st.engine = ['Nền parallax trôi liên tục để tạo cảm giác tàu chạy', 'Vùng gió đẩy ngang có tốc độ chỉnh được',
                 'Khớp nối tách theo thời gian (khe rộng dần, có cảnh báo)', 'Hầm quét: khối trần hạ theo lịch + cảnh báo',
                 'Ride Armor phá vách nứt (breakable_blocks)', 'Băng chuyền đẩy ngược']
    st.art = ['Nóc toa và khớp nối (tileset metal, 2 biến thể)', 'Thùng hàng che đạn', 'Cần cẩu và bệ hàng treo', 'Miệng hầm đá + đèn cảnh báo',
              'Ống khói đầu tàu', 'Xe tải bọc thép (mini-boss, có sẵn: truck)', 'Nền sa mạc parallax 3 lớp']
    return st
