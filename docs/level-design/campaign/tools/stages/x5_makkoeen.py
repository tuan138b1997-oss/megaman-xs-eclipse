from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_makkoeen', 'Căn cứ đáy biển', 'Tidal Makkoeen', 'water', 'Act I · X5', 'boss',
               'Căn cứ chìm dưới biển. Trong nước trọng lực còn 0.32: nhảy cao gần 3 lần, rơi chậm. Area 1 đi từ bến cảng xuống hành lang ngập '
               'và leo trụ thông khí; mini-boss tàu ngầm U-555. Area 2 có phòng bơm rút nước (mất nhảy cao để mở lối dưới đáy), '
               'ống hải lưu hút về tua-bin và rãnh san hô đi xuống.',
               'X5 Tidal Makkoeen (căn cứ đáy biển), X1 Launch Octopus (dưới nước), X6 Rainy Turtloid (công tắc mực nước).')
    st.capsule_short = 'Falcon Head'
    st.mech = ['Vùng nước (trọng lực 0.32)', 'Mực nước thay đổi theo công tắc']
    A1, A2 = 'Area 1 · cảng và hành lang ngập', 'Area 2 · đáy biển'

    r = R('R1', 'Bến cảng', 2, 'Trên mặt nước, sàn gỗ cảng. Sóng đẩy nhẹ người chơi về trái ở mép bến. Bậc xuống mặt nước dạy cảm giác trọng lực nhẹ.',
          timing='sóng đẩy −30 px/s ở mép bến', ceil=None)
    r.run(10, 'S').run(6).step(2, 6).zone(10, 'water', 'nước: trọng lực ×0.32', y0=7, ents='D').run(4)
    st.add(r.done(), A1)

    r = R('R2', 'Hành lang ngập', 3, 'Ngập hoàn toàn. Dòng chảy ngang →60 px/s giúp nhảy xa. Kệ trên trần chỉ với tới nhờ nhảy nước. Cá máy (Drone nước) bơi zigzag. '
          'Reploid trên kệ giữa.', timing='dòng chảy +60 px/s; nhảy trong nước cao ~7 ô', h=14)
    r.zone(70, 'water', '', y0=1, y1=14, walk=False)
    r.run(8).zone(14, 'current', 'dòng chảy → 60 px/s', y0=4, ents='D').special(10, 'swim', -4, prims=[('ledge', 3, -4, 4, 'ke'), ('e', 'R', 5, -4)], land=4)
    r.step(4, 8).run(8, 'S D').special(10, 'swim', 0, prims=[('pit', 0, 10, 'gai')]).run(6)
    st.add(r.done(), A1)

    s = Shaft('R3', 'Trụ thông khí', 4, 'Giếng nước dọc: trọng lực nhẹ giúp đá tường lên trụ X≈2350 (dữ liệu game). Mặt nước ở giữa giếng; phía trên khô, '
              'kệ so le 2.5 ô. Capsule Falcon Head trong hốc trần bên trái: nhảy nước từ kệ cao nhất.', w=14, h=32,
              timing='mặt nước ở y giữa giếng; trên mặt nước trọng lực bình thường')
    s.add(('zone', 2, 16, 12, 30, 'water', 'nước'))
    s.climb(step=2.5, ents={2: 'S', 5: 'D'})
    s.add(('block', 2, 6, 5, 7), ('e', 'A', 3.5, 6, 'Falcon Head (hốc trần)')).secret((5.5, 12.5), (3.5, 6))
    st.add(s.done(), A1)

    st.add(Arena('MID', 'Tàu ngầm U-555', 5, 'Mini-boss: tàu ngầm U-555 nổi giữa hầm, phóng ngư lôi bám đuổi. Mỗi lần mất 1/3 máu, nước hạ 2 ô để lộ lõi. '
                 'Checkpoint 1 sau trận.', w=30, boss='M', note='U-555 50 HP', timing='ngư lôi mỗi 2 s; nước hạ 2 ô mỗi 1/3 máu',
                 extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R4', 'Phòng bơm', 5, 'Hai công tắc bơm. Bắn công tắc 1: rút nước → lộ lối dưới đáy có Sub-Tank nhưng mất nhảy cao (kệ trên không tới được). '
          'Bắn công tắc 2: bơm lại. Đường chính: đi khi nước rút, Brute đứng ở đáy.', timing='rút/bơm mất 3 s; nước rút: trọng lực bình thường', h=14)
    r.run(4).ent('K', 2, 0, 'công tắc 1: rút nước').run(6).step(2, 10, ).ent('B', 5).run(4).ent('T', 2, 0, 'đáy lộ ra khi rút nước').run(6)
    r.ent('K', 0, 0, 'công tắc 2: bơm lại').step(-2, 4).step(-2, 8).ent('S', 4).run(4)
    r.secret((-12, 0), (-12, -6), (-4, -6)).raw(('ledge', -13, -6, 6, 'ke'), ('note', -13, -7.5, 'kệ cao: cần nước đầy'))
    st.add(r.done(), A2)

    r = R('R5', 'Ống hải lưu', 7, 'Cao trào. Ống nước dài hút về tua-bin bên phải (dòng −60→−90 px/s tăng dần). Gai trần ở ba đoạn: nhảy nước quá cao là trúng. '
          'Hai đoạn vực gai dưới đáy. Heart Tank trong hốc trên trần sau tua-bin cánh 1 (dừng được bằng cách bắn tua-bin).',
          timing='dòng hút về phải 60→90 px/s; tua-bin dừng 3 s khi trúng 3 phát', h=12)
    r.zone(60, 'water', '', y0=1, y1=12, walk=False)
    r.spikes(12, 'ceil', 3).zone(14, 'current', 'hút về tua-bin →', y0=4, ents='D S').gap(4, 'gai').spikes(10, 'ceil', 3).run(10, 'D')
    r.ent('C', -3).secret((-2, 0), (-2, -6.5), (1, -6.5)).raw(('ledge', -3, -6.5, 5, 'ke'), ('e', 'H', -1, -6.5, 'hốc trần'))
    r.gap(5, 'gai').run(8, 'B').run(4)
    st.add(r.done(), A2)

    s = Shaft('R6', 'Rãnh san hô', 6, 'Đi xuống rãnh san hô: kệ san hô so le, gai san hô hai bên vách, dòng kéo xuống 40 px/s. Reploid kẹt trên kệ giữa.',
              w=14, h=30, up=False, timing='dòng kéo xuống 40 px/s')
    s.add(('zone', 2, 1, 12, 28, 'water', 'nước'), ('spikes', 2, 2.6, 20, 'wall')).climb(step=3, ents={3: 'R', 5: 'S'})
    st.add(s.done(), A2)

    r = R('R7', 'Cửa cống', 2, 'Phòng nghỉ trong cống khô: năng lượng nhỏ, Reploid cuối, cửa boss.')
    r.run(8, 'R R').run(10)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Tidal Makkoeen', 6, 'Đấu trường nửa ngập: Makkoeen trượt trên mặt nước, lặn né đạn.', w=30), 'Boss')
    st.areas = [('Area 1', 'cảng và hành lang ngập', ['R1', 'R2', 'R3']), ('Mid', 'tàu ngầm U-555', ['MID']),
                ('Area 2', 'đáy biển: bơm, ống hải lưu, rãnh san hô', ['R4', 'R5', 'R6', 'R7']), ('Boss', 'đấu trường nửa ngập', ['BOSS'])]
    st.secrets = [('Capsule Falcon Head', 'R3', 'Nhảy nước từ kệ cao nhất vào hốc trần bên trái giếng.'),
                  ('Sub-Tank', 'R4', 'Rút nước bằng công tắc 1, đáy phòng lộ ra.'), ('Heart Tank', 'R5', 'Bắn dừng tua-bin, nhảy nước lên hốc trần.')]
    st.boss_info = {'arena': 'hồ 30×11 ô, nước ngập nửa dưới (trọng lực nhẹ dưới mặt nước).',
                    'phase2': 'nước dâng ngập toàn sân: cả trận chuyển sang trọng lực nhẹ, Makkoeen lướt liên tục.'}
    st.engine = ['Vùng nước: trọng lực 0.32, nhảy cao', 'Mực nước thay đổi theo công tắc (3 s)', 'Dòng chảy đẩy/hút', 'Tua-bin dừng khi trúng đạn']
    st.art = ['Bến cảng gỗ, ống thép rỉ', 'Bề mặt nước động + bọt', 'Công tắc bơm', 'Tua-bin', 'Kệ san hô + gai san hô', 'Tàu ngầm U-555 (có sẵn: submarine)']
    return st
