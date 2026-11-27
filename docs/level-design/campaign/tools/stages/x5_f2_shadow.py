from lib import Stage
from kit import R, Arena, Shaft


def build():
    st = Stage('x5_f2_shadow', 'Zero Space 2', 'Shadow Devil', 'shadow', 'Pháo đài X5', 'fortress',
               'Toàn màn là vực không đáy; đường đi là chuỗi bệ hai pha và luồng khí nâng bật/tắt theo nhịp. '
               'Area 1: rìa vực và chuỗi hologram; Area 2: cầu bóng tối với bệ di động và luồng nâng thứ hai.',
               'X5 Zero Space 2 (bệ 2 pha), X2 X-Hunter base (bệ di động), X8 Gateway.')
    st.mech = ['Bệ 2 pha', 'Luồng khí nâng bật/tắt theo nhịp']
    A1, A2 = 'Area 1 · rìa vực', 'Area 2 · cầu bóng tối'

    r = R('R1', 'Rìa vực', 3, 'Bệ 2 pha đầu tiên đổi mỗi 2 s, có bệ cứng xen giữa để nghỉ.', timing='bệ 2 pha: 2 s / 2 s, nháy 0.5 s', h=14)
    r.run(6, 'S').ledges(20, [(3, -1, 3), (9, -1, 3), (15, 0, 3)], kind='phase', land=6).ent('R', -3)
    st.add(r.done(), A1)

    r = R('R2', 'Chuỗi hologram', 6, 'Mười bệ đổi pha liên tiếp; giữa chuỗi là luồng khí nâng (bật 3 s / tắt 2 s) để vượt khe lớn 10 ô.',
          timing='bệ 2 pha 2 s; luồng nâng bật 3 s / tắt 2 s', h=14)
    r.run(4).ledges(26, [(3, -1, 3), (8, -2, 3), (13, -1, 3), (18, -2, 3), (22, -1, 3)], kind='phase', land=3).ent('D', 0)
    r.special(10, 'updraft', -2, prims=[('pit', 0, 10, 'vuc'), ('zone', 2, -8, 8, 4, 'updraft', 'luồng nâng 3s/2s')], land=3)
    r.ledges(22, [(3, -1, 3), (8, 0, 3), (13, -1, 3), (18, 0, 3)], kind='phase', land=4).ent('D', -2).ent('R', -1)
    st.add(r.done(), A1)

    st.add(Arena('MID', 'Điểm dừng', 5, 'Mini-boss: khối thạch đen 45 HP chia làm 3 phần bay quanh. Checkpoint 1 sau trận.', w=24, boss='M', note='khối thạch 45 HP',
                 timing='3 khối lao theo thứ tự mỗi 2 s', extra=lambda b: b.ent('C', -2)), 'Mid')

    r = R('R3', 'Cầu bóng tối', 6, 'Bệ di động ngang trên vực, Drone ném bom xuống bệ. Sniper trên bệ cứng.', timing='bệ di động ±4 ô, 2.5 s; bom mỗi 2 s', h=14)
    r.run(4, 'S').ledges(24, [(3, -1, 4), (11, -1, 4), (19, 0, 4)], kind='move', land=4).ent('D', -2).run(4, 'S')
    st.add(r.done(), A2)

    r = R('R6', 'Luồng nâng 2', 8, 'Cao trào: luồng nâng đứt quãng + bệ 2 pha + Drone; nghỉ ở bệ cứng giữa. Checkpoint 2 ở bệ cứng.',
          timing='luồng nâng bật 2 s / tắt 2 s; bệ 2 pha 1.5 s', h=14)
    r.run(4).special(10, 'updraft', -2, prims=[('pit', 0, 10, 'vuc'), ('zone', 2, -8, 8, 4, 'updraft', 'luồng nâng 2s/2s')], land=4).ent('C', -2)
    r.ledges(22, [(3, -1, 3), (8, -2, 3), (13, -1, 3), (18, -1, 3)], kind='phase', land=4).ent('D', -2).ent('R', -1)
    r.special(10, 'updraft', 0, prims=[('pit', 0, 10, 'vuc'), ('zone', 2, -8, 8, 4, 'updraft', '')], land=6).ent('B', -3).ent('R', -1)
    st.add(r.done(), A2)

    r = R('R7', 'Trạm năng lượng', 2, 'Trạm năng lượng lớn trước boss.')
    r.run(6).ent('E', 0, 0, 'trạm năng lượng lớn').run(10)
    st.add(r.done(), A2)

    st.add(Arena('BOSS', 'Shadow Devil', 7, 'Khối thạch đen ghép lại thành boss; mắt đỏ là điểm yếu.', w=30), 'Boss')
    st.areas = [('Area 1', 'rìa vực, chuỗi hologram', ['R1', 'R2']), ('Mid', 'khối thạch đen', ['MID']), ('Area 2', 'cầu bóng tối, luồng nâng 2', ['R3', 'R6', 'R7']),
                ('Boss', 'đấu trường đen', ['BOSS'])]
    st.boss_info = {'attacks': 'Blob Rain (khối thạch rơi), Eye Beam (mắt đỏ bắn tia), Body Slam (ghép thân đè).',
                    'arena': '30×11 ô, sàn cứng.', 'phase2': 'sàn tách thành 3 bệ 2 pha; khối thạch rơi theo nhịp đổi pha.'}
    st.engine = ['Bệ 2 pha có nháy báo', 'Luồng khí nâng bật/tắt', 'Bệ di động ngang']
    st.art = ['Bệ hologram xanh/tím', 'Quạt nâng có đèn trạng thái', 'Nền vực không đáy']
    return st
