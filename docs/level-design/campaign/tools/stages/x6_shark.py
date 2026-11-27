from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x6_shark', 'Phòng thí nghiệm tái chế', 'Metal Shark Player', 'metal', 'Act II · X6', 'boss',
               'Nhà máy tái chế phế liệu. Trần máy ép toàn phòng hạ xuống theo nhịp (đèn đỏ báo trước), khối rác rơi theo làn từ băng tải trên cao. '
               'Giữa màn có Ride Armor để đục tường rác giấu capsule Shadow Foot. Đoạn tự cuộn gốc làm lại thành hầm tường ép đuổi chậm, người chơi tự chạy.',
               'X6 Metal Shark Player (tái chế), X3 Crush Crawfish? – X5 Grizzly (Ride Armor), X8 Earthrock Trilobite (bị đuổi).')
    st.refs = 'X6 Metal Shark Player (nhà máy tái chế, trần ép), X8 Earthrock Trilobite (bị vật lớn đuổi), X4 Ride Armor (đục tường).'
    st.capsule_short = 'Shadow Foot'
    st.mech = ['Trần ép toàn phòng', 'Khối rác rơi theo làn và lịch']
    A1, A2 = 'Area 1 · bãi phế liệu', 'Area 2 · bãi rác nén và hầm'

    r = R('R1', 'Bãi phế liệu', 3, 'Khối sắt rơi từ băng tải trên cao theo 3 làn (bóng đen báo trước 0.8 s). Núi phế liệu là bậc.', timing='khối rơi mỗi 1.5 s, luân phiên 3 làn')
    r.run(6, 'S').zone(4, 'crush', 'làn rơi', y0=1).step(-2, 6).zone(4, 'crush', 'làn rơi', y0=1).run(6, 'D').step(2, 6).run(6, 'R')
    st.add(r.done(), A1)

    r = R('R2', 'Hành lang máy ép', 5, 'Bốn trần máy ép thủy lực hạ toàn phòng theo nhịp lệch pha; hốc an toàn 2 ô giữa các máy. Brute đứng trong hốc.',
          timing='máy ép: chờ 1.6 s, ép 0.3 s, nâng 0.8 s; lệch pha 0.6 s')
    for i in range(4):
        r.zone(5, 'crush', f'máy ép {i + 1}', y0=1, ents=('B' if i == 1 else 'D' if i == 2 else '')).run(3)
    r.run(4, 'S R')
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Trạm Ride Armor', 5, 'Mini-boss: cần cẩu nam châm 45 HP ném khối sắt. Checkpoint 1 và Ride Armor Pod (X=3240 dữ liệu game).', w=26, boss='M',
                 note='cần cẩu 45 HP', timing='ném khối sắt mỗi 2 s', extra=lambda b: b.ent('C', -4).ent('V', -2, 0, 'Ride Armor Pod')), 'Mid')

    r = R('R3', 'Bãi rác nén', 5, 'Cưỡi Ride Armor đục hai tường rác. Tường thứ hai (X=4950) giấu khoang capsule Shadow Foot. Heart Tank trên núi rác phía trên.',
          timing='tường rác 12 HP, chỉ Ride Armor')
    r.run(6, 'S').breakwall(4).note('tường rác 1', 0, -5).run(8).breakwall(4).note('tường rác 2', 0, -5)
    r.secret((0, 0), (2, 0)).raw(('e', 'A', 2, 0, 'Shadow Foot (sau tường 2)')).run(6).pillar(3, 2)
    r.secret((-1, -2), (1, -4.5)).raw(('ledge', 0, -4.5, 3, 'ke'), ('e', 'H', 1.5, -4.5, 'núi rác')).run(6, 'B').run(4)
    st.add(r.done(), A2)

    r = R('R6', 'Hầm tường ép đuổi', 7, 'Cao trào: tường ép đuổi từ trái 120 px/s (chậm hơn tốc độ chạy) – không tự cuộn, người chơi tự chạy. Khối sắt chắn phải bắn vỡ (6 HP), '
          'hố 3 ô. Checkpoint 2 ở đầu hầm.', timing='tường ép 120 px/s; khối chắn 6 HP')
    r.ent('C', 2).run(4).zone(50, 'crush', '← tường ép đuổi 120 px/s', y0=1, walk=False).run(8, 'D').pillar(2, 2).run(6).gap(3).run(8, 'S').pillar(2, 2).run(10, 'D').run(4)
    st.add(r.done(), A2)

    r = R('R7', 'Lò nung', 2, 'Phòng nghỉ: Sub-Tank trên băng tải dừng, Reploid, cửa boss.')
    r.run(6, 'R').ent('T', 2, 0, 'băng tải dừng').run(6, 'R').run(6, 'D')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Metal Shark Player', 6, 'Boss lặn dưới nền phế liệu; khối sắt rơi từ trần.', w=30), 'Boss')
    st.areas = [('Area 1', 'bãi phế liệu, hành lang máy ép', ['R1', 'R2']), ('Mid', 'cần cẩu nam châm', ['MID']), ('Area 2', 'bãi rác nén, hầm tường ép', ['R3', 'R6', 'R7']),
                ('Boss', 'hố phế liệu', ['BOSS'])]
    st.secrets = [('Capsule Shadow Foot', 'R3', 'Ride Armor đục tường rác thứ 2.'), ('Heart Tank', 'R3', 'Núi rác phía trên.'), ('Sub-Tank', 'R7', 'Băng tải dừng.')]
    st.boss_info = {'arena': 'hố phế liệu 30×11 ô, nền cát sắt.', 'phase2': 'trần ép hạ 3 ô trong 2 s mỗi 10 s; boss lặn nhanh gấp đôi.'}
    st.engine = ['Trần ép toàn phòng theo nhịp', 'Khối rơi theo làn và lịch', 'Ride Armor đục tường rác', 'Tường ép đuổi (người chơi tự chạy)']
    st.art = ['Bãi phế liệu, núi sắt vụn', 'Trần máy ép thủy lực', 'Tường rác nén', 'Băng tải trên cao']
    return st
