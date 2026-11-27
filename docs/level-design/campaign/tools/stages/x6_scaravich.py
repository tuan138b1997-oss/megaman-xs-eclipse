from lib import Stage
from kit import R, Arena, Shaft, TwoTier


def build():
    st = Stage('x6_scaravich', 'Bảo tàng Trung tâm', 'Ground Scaravich', 'metal', 'Act II · X6', 'boss',
               'Bảo tàng ban đêm: đèn pha an ninh quét theo đường cố định; bị phát hiện thì cửa phòng sập khóa và gọi 2 lính. '
               'Giữa màn là Đại cột Totem chặn đường. Area 2 có hai cụm phòng nối bằng cổng dịch chuyển theo cặp.',
               'X6 Ground Scaravich / Central Museum, X8 Dark Mantis (lén lút), X4 Split Mushroom.')
    st.capsule_short = 'Blade Arm'
    st.mech = ['Đèn pha quét theo đường cố định', 'Cổng dịch chuyển theo cặp']
    A1, A2 = 'Area 1 · sảnh trưng bày', 'Area 2 · cụm phòng Cell'

    r = R('R1', 'Sảnh trưng bày', 3, 'Đèn pha quét đầu tiên (vệt vàng qua lại 6 ô). Bị phát hiện → cửa sập 6 s + 2 Drone báo động (không tính vào đếm).',
          timing='đèn quét 2.5 s một chiều; báo động khóa cửa 6 s')
    r.run(6, 'S').zone(8, 'light', 'đèn pha quét', y0=1).pillar(2, 2).run(6, 'D').zone(8, 'light', 'đèn pha quét', y0=1).run(4)
    st.add(r.done(), A1)

    def top(t): t.run(6, 'D').gap(3).run(8, 'R').gap(3).run(10)
    def bot(b): b.zone(14, 'light', 'đèn pha chéo', y0=10).run(16, 'S')
    st.add(TwoTier('R2', 'Phòng hóa thạch', 4, 'Hai tầng: tầng trên đi trên khung xương khủng long (khe 3 ô), tầng dưới sàn bảo tàng có đèn pha chéo. Lối chính tầng trên.',
                   top, bot, main='top', timing='đèn pha chéo 3 s'), A1)

    st.add(Arena('MID', 'Đại cột Totem', 5, 'Mini-boss: Đại cột Totem 45 HP, mỗi tầng mặt bắn đạn khác nhau; phá từ dưới lên. Checkpoint 1.', w=26, boss='M',
                 note='Totem 45 HP (3 tầng)', timing='mỗi tầng bắn 1.5 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R3', 'Cụm phòng Cell 1', 4, 'Bốn cổng dịch chuyển theo cặp nối hai cụm phòng; mỗi phòng một tủ trưng bày (Heart Tank ở một tủ). Đèn pha trong mỗi phòng.',
          timing='cổng hồi 1 s')
    r.run(6, 'D').special(4, 'tele', 0, prims=[('note', 0, -5, 'cổng A→B')], land=8).ent('H', 2, 0, 'tủ trưng bày').zone(8, 'light', 'đèn pha', y0=1, ents='S')
    r.special(4, 'tele', 0, prims=[('note', 0, -5, 'cổng C→D')], land=6).run(4, 'S R')
    st.add(r.done(), A2)

    r = R('R6', 'Cụm phòng Cell 2', 7, 'Cao trào: đèn pha phối hợp ba vệt + cổng dịch chuyển; bị phát hiện là khóa phòng với Brute. Hốc cao có capsule Blade Arm '
          '(X=4840 dữ liệu game); Sub-Tank qua cổng phụ. Checkpoint 2.', timing='3 đèn quét lệch pha 1 s')
    r.ent('C', 2).run(4).zone(10, 'light', 'đèn ×3', y0=1, ents='B').pillar(3, 2)
    r.secret((-1, -2), (1, -4.5)).raw(('ledge', 0, -4.5, 4, 'ke'), ('e', 'A', 2, -4.5, 'Blade Arm (hốc cao)'))
    r.zone(10, 'light', '', y0=1, ents='D').special(4, 'tele', 0, prims=[('note', 0, -5, 'cổng E→F')], land=6).ent('T', -2, 0, 'phòng kín').run(6, 'S').run(4)
    st.add(r.done(), A2)

    r = R('R7', 'Kho lưu trữ', 2, 'Phòng nghỉ: hai Reploid, cửa boss.')
    r.run(6, 'R').run(6, 'R').run(6, 'D')
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Ground Scaravich', 6, 'Bọ hung lăn tảng đá khổng lồ; cổng dịch chuyển trong đấu trường.', w=30), 'Boss')
    st.areas = [('Area 1', 'sảnh, phòng hóa thạch', ['R1', 'R2']), ('Mid', 'Đại cột Totem', ['MID']), ('Area 2', 'cụm phòng Cell 1–2', ['R3', 'R6', 'R7']),
                ('Boss', 'kho tàng', ['BOSS'])]
    st.secrets = [('Capsule Blade Arm', 'R6', 'Hốc cao Cell 2.'), ('Heart Tank', 'R3', 'Tủ trưng bày qua cổng A→B.'), ('Sub-Tank', 'R6', 'Phòng kín qua cổng E→F.')]
    st.boss_info = {'arena': 'kho 30×11 ô, 2 cổng dịch chuyển hai góc.', 'phase2': 'tảng đá to gấp đôi và đi qua cổng dịch chuyển ra phía sau người chơi.'}
    st.engine = ['Đèn pha quét theo đường cố định, phát hiện → khóa phòng', 'Cổng dịch chuyển theo cặp', 'Đại cột Totem nhiều tầng']
    st.art = ['Bảo tàng ban đêm, tủ trưng bày', 'Khung xương khủng long (bệ)', 'Đèn pha an ninh', 'Cổng dịch chuyển', 'Cột Totem']
    return st
