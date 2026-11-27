from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('intro', 'Cao tốc Neo Arcadia', '1D-1000 → High Max', 'intro', 'Mở đầu', 'intro',
               'Màn dạy chơi trên cao tốc đổ nát hai tầng lúc hoàng hôn. Mỗi phòng dạy đúng một kỹ năng theo thứ tự: chạy-bắn, nhảy hố, '
               'đá tường, lướt, cưỡi Ride Armor. Bảng chỉ dẫn nút hiện khi bước vào vùng dạy. Kết thúc bằng nhện 1D-1000, sau đó High Max đáp xuống.',
               'X4/X5 intro (mỗi đoạn dạy 1 kỹ năng, boss lớn), X8 intro (màn thẳng, không gimmick nặng), Mega Man X1 intro (cao tốc).')
    st.capsule_short = 'Fourth Armor (bộ đầy đủ)'
    st.mech = ['Bảng chỉ dẫn nút hiện theo vùng', 'Hố "dạy chơi" (rơi mất máu, không chết)']
    A1, A2 = 'Area 1 · cao tốc tầng dưới', 'Area 2 · tầng trên và hầm'

    r = R('R1', 'Làn đường sập', 1, 'Đường thẳng an toàn. Bảng 1: ←→ chạy, Z bắn. Hai khối bê tông thấp (1.5 ô) dạy nhảy; Sniper đứng sau khối thứ hai.',
          timing='bảng chỉ dẫn hiện 3 s khi bước vào vùng', ceil=None)
    r.run(4).note('bảng: ←→ chạy · Z bắn', 0, -5).run(8).pillar(2, 1.5).run(8, 'S').pillar(3, 1.5).run(10, 'S').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Cầu vượt gãy', 2, 'Hai hố nhỏ trên cầu gãy (2 và 3 ô). Rơi xuống chỉ mất 4 HP và bị đặt lại mép hố (hố dạy chơi). '
          'Drone bay ngang dạy bắn chéo. Reploid đầu tiên ở cuối cầu.', timing='hố dạy chơi: rơi = −4 HP, đặt lại mép', ceil=None)
    r.run(10).note('bảng: Space nhảy', 0, -5).gap(2, 'vuc').run(10, 'D').gap(3, 'vuc').run(8).step(-2, 6).run(6, 'R').run(4)
    st.add(r.done(), A1)

    s = Shaft('R3', 'Trụ cầu', 2, 'Giếng giữa hai trụ cầu, dạy đá tường: bảng chỉ dẫn "giữ → vào tường + Space". Kệ nghỉ mỗi 2.5 ô cho người chưa quen; '
              'Drone tuần ở giữa.', w=14, h=28, timing='bảng: giữ hướng vào tường + Space để đá tường')
    s.wallkick(26, 20, 'left').climb(step=2.5, ents={4: 'D'}, start=26)
    s.note('đá tường', 2.5, 22)
    st.add(s.done(), A1)

    r = R('R4', 'Tầng trên cao tốc', 3, 'Cao trào Area 1. Ô tô cháy là vật che (lửa trên nóc xe 1 ô). Brute chặn giữa đường; biển báo treo thấp (khe 1.6 ô) '
          'dạy lướt. Checkpoint 1 ở cuối phòng.', timing='lửa xe bùng 1 s mỗi 3 s; khe biển báo 1.6 ô')
    r.run(6, 'S').pillar(4, 2).run(6).zone(4, 'fire', 'lửa xe', y0=7).run(4, 'B').note('bảng: C lướt', 0, -5).low(6, 1.6, 'biển báo: lướt')
    r.run(8, 'D').ent('C', 6).run(8)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Trạm kiểm soát', 3, 'Mini-boss nhỏ: tháp pháo kiểm soát 30 HP, bắn đạn thẳng và thả Drone. Dạy đứng ngoài đường đạn rồi bắn.',
                 w=24, boss='M', note='tháp pháo 30 HP', timing='đạn thẳng mỗi 1.5 s; thả 1 Drone mỗi 6 s (không tính vào đếm)'), 'Mid')

    r = R('R5', 'Bãi Ride Armor', 3, 'Ride Armor Pod đậu đầu phòng (bảng: lên xe bằng ↑). Cưỡi xe đấm vỡ tường bê tông → bậc lên tầng 2 có capsule Fourth Armor '
          '(cả bộ, theo dữ liệu game: X=3880). Đi bộ vẫn qua được phòng bằng đường dưới.', timing='tường bê tông 12 HP, chỉ Ride Armor phá được')
    r.run(4).ent('V', 2, 0, 'Ride Armor Pod').run(8).breakwall(4).note('tường bê tông', 0, -5).run(6, 'S')
    r.secret((-6, 0), (-6, -2.5), (-2, -5), (2, -5)).raw(('ledge', -6, -2.5, 3, 'ke'), ('ledge', -3, -5, 6, 'ke'), ('e', 'A', 1, -5, 'Fourth Armor (bộ đầy đủ)'))
    r.run(10, 'R').run(6)
    st.add(r.done(), A2)

    r = R('R6', 'Đường hầm đèn vàng', 3, 'Hầm tối, đèn trần chớp vàng (tối 1 s / sáng 2 s). Drone lao từ hai đầu. Heart Tank trong khe thông gió phía trên: '
          'lướt-nhảy từ khối chắn lên khe. Checkpoint 2 giữa hầm.', timing='đèn: tối 1 s / sáng 2 s; Drone lao 420 px/s')
    r.zone(12, 'dark', 'đèn chớp', y0=1, ents='D').ent('C', -2).pillar(3, 2).secret((-1, -2), (3, -6.5), (6, -6.5)).raw(('ledge', 2, -6.5, 6, 'ke'), ('e', 'H', 5, -6.5, 'khe thông gió'))
    r.zone(14, 'dark', '', y0=1, ents='D R').run(6)
    st.add(r.done(), A2)

    r = R('R7', 'Lối ra cao tốc', 2, 'Phòng nghỉ trước boss: Sub-Tank trên biển chỉ đường (nhảy từ khối), Reploid cuối, cửa boss.', timing='')
    r.run(6).pillar(2, 2).secret((-1, -2), (1, -4.5)).raw(('ledge', 0, -4.5, 3, 'ke'), ('e', 'T', 1.5, -4.5, 'trên biển chỉ đường')).run(6, 'R').run(6)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', '1D-1000 / High Max', 3, 'Nhện 1D-1000 bám trần và hai tường, thả bom; hạ nó xong High Max đáp xuống (không thắng được, chuyển cảnh).', w=30),
           'Boss')
    st.areas = [('Area 1', 'cao tốc tầng dưới, dạy chạy-bắn, nhảy, đá tường, lướt', ['R1', 'R2', 'R3', 'R4']), ('Mid', 'tháp pháo kiểm soát', ['MID']),
                ('Area 2', 'tầng trên, Ride Armor, hầm tối', ['R5', 'R6', 'R7']), ('Boss', 'nhện 1D-1000 → High Max', ['BOSS'])]
    st.secrets = [('Capsule Fourth Armor', 'R5', 'Ride Armor đấm vỡ tường bê tông, leo 2 kệ lên tầng 2.'),
                  ('Heart Tank', 'R6', 'Lướt-nhảy từ khối chắn lên khe thông gió.'), ('Sub-Tank', 'R7', 'Nhảy từ khối lên biển chỉ đường.')]
    st.boss_info = {'attacks': '1D-1000: thả bom từ trần, bò dọc tường, bắn laser quét sàn. High Max: chuyển cảnh, không thể thắng.',
                    'arena': 'sân cao tốc 30×11 ô có trần (cầu vượt) cho nhện bám.',
                    'phase2': 'nhện rơi khỏi trần, bò sàn và tung bom chùm; mặt cầu nứt 2 ô ở giữa (hố dạy chơi).'}
    st.engine = ['Bảng chỉ dẫn nút theo vùng', 'Hố dạy chơi (rơi mất máu, đặt lại mép)', 'Ride Armor phá tường bê tông', 'Vùng tối đèn chớp']
    st.art = ['Cao tốc đổ nát (tileset intro), ô tô cháy, biển báo treo', 'Trụ cầu bê tông', 'Ride Armor Pod (có sẵn: mech)', 'Bảng chỉ dẫn nút (UI)']
    return st
