from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_kraken', 'Nhà máy điện', 'Volt Kraken', 'volt', 'Act I · X5', 'boss',
               'Nhà máy điện ven biển. Area 1 là chặng Ride Chaser người chơi tự điều khiển tốc độ (không tự cuộn) xuyên đường băng điện '
               'và cầu sập; Area 2 xuống xe, leo tháp tụ điện bằng bệ phản lực và đá tường, qua phòng cuộn dây có sàn điện theo nhịp.',
               'X5 Volt Kraken (nhà máy điện, Ride Chaser), X4 Jet Stingray (chặng xe), X2 Wheel Gator (tháp).')
    st.capsule_short = 'Falcon Arm'
    st.mech = ['Ride Chaser chạy tự do', 'Tấm boost']
    A1, A2 = 'Area 1 · chặng Ride Chaser', 'Area 2 · tháp và lõi nhà máy'

    r = R('R1', 'Bãi xuất phát', 1, 'Lên Ride Chaser (↑). Bảng hướng dẫn: giữ → tăng tốc, Space nhảy xe, Z bắn. Xe có thể dừng và lùi.', ceil=None)
    r.run(6).ent('V', 2, 0, 'Ride Chaser').run(14, 'S').run(6)
    st.add(r.done(), A1)

    r = R('R2', 'Đường băng điện', 4, 'Ride Chaser: hai dốc nhảy, cột điện phóng hồ quang ngang (bật 1 s / tắt 2 s, có tia lửa báo trước), Drone lao từ phía sau. '
          'Tấm boost trên mặt đường tăng tốc lên 820 px/s để nhảy khe rộng.', timing='hồ quang: bật 1 s / tắt 2 s, báo trước 0.5 s; boost 820 px/s trong 1.5 s', ceil=None)
    r.run(20, 'D').zone(6, 'spark', 'hồ quang', y0=6).slope(10, -3).special(10, 'ride', 3, prims=[('pit', 0, 10, 'vuc')], land=6)
    r.run(14, 'S D').note('tấm boost', 0, -2).zone(6, 'spark', 'hồ quang', y0=6).run(10, 'R').special(12, 'ride', 0, prims=[('pit', 0, 12, 'vuc')], land=6)
    r.run(20, 'D').run(6)
    st.add(r.done(), A1)

    r = R('R3', 'Cầu sập', 5, 'Ride Chaser trên cầu treo: mặt cầu sập dần sau lưng khi xe đã đi qua (sập 1.5 s sau khi bánh xe rời khỏi). Không tự cuộn: '
          'đứng yên quá lâu trên một nhịp cầu thì nhịp đó sập. Cuối cầu nhảy vào cổng nhà máy.', timing='nhịp cầu sập 1.5 s sau khi rời; đứng yên 3 s trên một nhịp thì sập', ceil=None)
    r.run(10).ledges(40, [(0, 0, 8), (10, 0, 8), (20, -1, 8), (30, 0, 8)], kind='crumble', tag='ride', land=4).ent('D', -2).run(10)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Trạm biến áp', 5, 'Xuống xe. Mini-boss: máy biến áp canh gác 45 HP phóng 3 tia sét chạy dọc sàn và vách. Hạ xong: checkpoint 1. '
                 'Heart Tank trên nóc trạm: nhảy từ bệ máy cuối sân lên gờ mái.', w=26, boss='M', note='máy biến áp 45 HP',
                 timing='3 tia sét dọc sàn mỗi 2.2 s', extra=lambda b: b.ent('C', -3).ent('R', -11)
                 .raw(('block', -9, -2, -7, 0), ('ledge', -7, -4.4, 2, 'ke'), ('e', 'H', -6, -4.4, 'nóc trạm')).secret((-8, -2), (-6, -4.4))), 'Mid')

    s = Shaft('R4', 'Tháp tụ điện', 7, 'Cao trào. Tháp 20 ô rộng: bệ phản lực bật/tắt theo nhịp (đứng trên bệ đang tắt sẽ rơi), tia điện quét ngang mỗi 10 ô '
              '(báo trước bằng tia lửa ở hai đầu). Falcon Arm ở đỉnh tháp bên trái (dữ liệu game).', w=20, h=44,
              timing='bệ phản lực: bật 2 s / tắt 1 s; tia điện quét ngang 2 s một lần, báo trước 0.6 s')
    s.add(('zone', 2, 30, 18, 31, 'spark', 'tia quét'), ('zone', 2, 18, 18, 19, 'spark', 'tia quét'))
    s.climb(step=2.5, kind='thruster', ents={3: 'S', 7: 'D', 12: 'D'})
    s.add(('ledge', 3, 6, 4, 'ke'), ('e', 'A', 5, 6, 'Falcon Arm (đỉnh tháp)')).secret((10, 10), (5, 6))
    st.add(s.done(), A2)

    r = R('R5', 'Phòng cuộn dây', 5, 'Sàn nhiễm điện bật/tắt theo nhịp 1.2 s (vạch vàng sáng báo trước). Đứng trên cuộn dây (khối cách điện) để chờ. '
          'Reploid kẹt giữa hai cuộn dây. Checkpoint 2 ở đầu phòng.', timing='sàn điện: bật 1.2 s / tắt 1.2 s; sát thương 4')
    r.ent('C', 2).run(4).zone(8, 'spark', 'sàn điện 1.2 s', y0=8, ents='S').pillar(3, 2).zone(10, 'spark', '', y0=8, ents='B R').pillar(3, 2)
    r.zone(8, 'spark', '', y0=8, ents='D').run(6)
    st.add(r.done(), A2)

    r = R('R6', 'Hành lang lõi', 2, 'Phòng nghỉ: Sub-Tank trong hốc tường (bắn vỡ nắp), Reploid, cửa boss.')
    r.run(6, 'R').run(4).ent('T', 0, -3, 'hốc tường').raw(('ledge', -1, -3, 3, 'ke')).run(10)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Volt Kraken', 6, 'Đấu trường có 4 cột thu sét ở hai bên.', w=30), 'Boss')
    st.areas = [('Area 1', 'chặng Ride Chaser tự điều khiển', ['R1', 'R2', 'R3']), ('Mid', 'trạm biến áp', ['MID']),
                ('Area 2', 'tháp tụ điện, phòng cuộn dây', ['R4', 'R5', 'R6']), ('Boss', 'sân cột thu sét', ['BOSS'])]
    st.secrets = [('Capsule Falcon Arm', 'R4', 'Kệ đỉnh tháp bên trái.'), ('Heart Tank', 'MID', 'Đá tường lên nóc trạm biến áp.'),
                  ('Sub-Tank', 'R6', 'Bắn vỡ nắp hốc tường.')]
    st.boss_info = {'arena': 'sân 30×11 ô, 4 cột thu sét (2 mỗi bên) cao 3 ô làm vật che.',
                    'phase2': 'Kraken nạp điện cho các cột: cột phóng hồ quang nối nhau theo nhịp 2 s, chia sân thành ô an toàn.'}
    st.engine = ['Ride Chaser chạy tự do (người chơi chỉnh tốc độ, có lùi)', 'Tấm boost', 'Hồ quang theo nhịp', 'Nhịp cầu sập sau khi rời',
                 'Bệ phản lực bật/tắt', 'Sàn điện theo nhịp']
    st.art = ['Đường băng nhà máy, cột điện', 'Cầu treo + nhịp cầu sập', 'Tháp tụ điện, bệ phản lực', 'Cuộn dây cách điện', 'Ride Chaser (có sẵn: bike)']
    return st
