from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_f4_gate', 'Phòng thí nghiệm Gate 3', 'Gate', 'core', 'Pháo đài X6', 'fortress',
               'Vùng đảo trọng lực bật bằng công tắc ngụy trang giấu Secret Ultimate Armor trên trần biển gai. Hành lang tinh thể Nightmare nổ khi bị bắn; '
               'giếng tinh thể là cao trào. Đấu trường Gate có vực giữa sàn.',
               'X6 Gate Lab 3 (Ultimate Armor), X5 Zero Space 3 (đảo trọng lực), X8 Sigma Palace.')
    st.capsule_short = 'bí mật Ultimate Armor'
    st.mech = ['Tinh thể Nightmare', 'Vùng đảo trọng lực bật bằng công tắc ngụy trang']
    A1, A2 = 'Area 1 · trần biển gai', 'Area 2 · giếng tinh thể'

    r = R('R1', 'Biển gai trần', 6, 'Công tắc ngụy trang (viên gạch lệch màu) bật vùng đảo trọng lực X=1150; đi trên trần qua biển gai 36 ô. '
          'Secret Ultimate Armor ở hốc trần X=1850 (dữ liệu game). Đường chính đi dưới bằng chuỗi kệ.', timing='', h=14)
    r.run(6, 'D').ent('K', 0, -1, 'công tắc ngụy trang').ledges(30, [(3, -1, 3), (9, -2, 3), (15, -1, 3), (21, -2, 3), (26, -1, 2)], kind='ke', pit='gai', land=4)
    r.raw(('zone', -34, -12, -2, -4, 'grav', 'vùng đảo trọng lực (khi bật)'), ('e', 'A', -18, -12, 'Secret Ultimate Armor (hốc trần)'))
    r.secret((-34, 0), (-34, -12), (-18, -12)).run(4, 'R')
    st.add(r.done(), A1)

    r = R('R2', 'Hành lang tinh thể', 6, 'Tinh thể Nightmare nổ khi bị bắn (bán kính 3 ô, 6 sát thương); dùng nổ dây chuyền để diệt Brute.', timing='tinh thể nổ 0.4 s sau khi trúng')
    r.run(6, 'S').pillar(2, 1.5).run(6, 'B').pillar(2, 1.5).run(8, 'D R').run(4)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Điểm dừng', 5, 'Mini-boss: cụm tinh thể mẹ 45 HP. Checkpoint 1.', w=24, boss='M', note='tinh thể mẹ 45 HP', timing='tinh thể con nổ mỗi 2.5 s',
                 extra=lambda b: b.ent('C', -2)), 'Mid')

    s = Shaft('R5', 'Giếng tinh thể', 8, 'Cao trào: thang máy dữ liệu nâng chậm; tinh thể bám vách nổ dây chuyền, Drone bao quanh. Checkpoint 2 ở đáy.', w=16, h=38,
              timing='tinh thể vách nổ khi bị bắn hoặc chạm')
    s.ent('C', 5, 36).add(('spikes', 2, 2.6, 24, 'wall'), ('spikes', 13.4, 14, 14, 'wall')).climb(step=2.5, kind='move', ents={2: 'D', 6: 'D', 9: 'R'})
    st.add(s.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước boss; Reploid cuối.')
    r.run(6, 'R').ent('E', 0, 0, 'trạm năng lượng lớn').run(10, 'S')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Gate', 8, 'Sàn có vực giữa; Gate dùng quả cầu Nightmare.', w=30), 'Boss')
    st.areas = [('Area 1', 'trần biển gai, hành lang tinh thể', ['R1', 'R2']), ('Mid', 'tinh thể mẹ', ['MID']), ('Area 2', 'giếng tinh thể', ['R5', 'R7']),
                ('Boss', 'phòng Gate', ['BOSS'])]
    st.secrets = [('Secret Ultimate Armor', 'R1', 'Bật công tắc ngụy trang, đi trên trần tới hốc X=1850.')]
    st.boss_info = {'arena': '30×11 ô, vực 4 ô giữa sàn.', 'phase2': 'quả cầu Nightmare phải bắn vỡ để thành mảnh phản đòn (gate-fragment) – cách duy nhất gây sát thương.'}
    st.engine = ['Công tắc ngụy trang bật vùng đảo trọng lực', 'Tinh thể Nightmare nổ dây chuyền', 'Thang máy dữ liệu', 'Boss chỉ trúng bằng mảnh cầu phản đòn']
    st.art = ['Biển gai trần', 'Tinh thể Nightmare', 'Gạch công tắc ngụy trang']
    return st
