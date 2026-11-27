"""Bộ thiết kế màn chơi theo ô (chuẩn Lò Nham Thạch đã duyệt).

Hệ toạ độ: 1 ô = 32 px, y tăng xuống dưới, như levels/lo-nham-thach.level.json.
Một màn = danh sách phòng; mỗi phòng có hình học cục bộ (ô), đường đi chính (điểm chân nhân vật,
có nhãn kiểu di chuyển), lối bí mật, thực thể và ghi chú. Thư viện xếp phòng thành toạ độ toàn màn,
kiểm tra đường chính theo khả năng nhảy, vẽ sơ đồ, viết kịch bản và xuất JSON.
"""
import json, math, os
from PIL import Image, ImageDraw, ImageFont

# ---- chuẩn kích thước (khớp bản Unity / game web) ----
VIEW_W, VIEW_H = 20, 11.25        # khung hình 640×360 px
JUMP_UP = 2.5                      # gờ cao nhất trên đường chính (nhảy thường cao ~2.6 ô)
JUMP_FAR = 5                       # nhảy xa khi chạy (~5 ô)
DASH_FAR = 7                       # lướt + nhảy
CORR_H = 12                        # phòng hành lang: trần 0–1, nền trên y=10, đáy 12 → trong lòng 9 ô

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

ENT = {  # mã: (chữ, màu, tên, nhóm)
    'S': ('S', (255, 90, 90), 'Sniper', 'enemy'), 'D': ('D', (255, 160, 60), 'Drone', 'enemy'),
    'B': ('B', (230, 80, 80), 'Brute', 'enemy'), 'M': ('M', (255, 60, 130), 'Mini-boss', 'boss'),
    '*': ('★', (255, 70, 70), 'Boss', 'boss'), 'R': ('R', (120, 255, 140), 'Reploid cứu', 'item'),
    'H': ('H', (255, 120, 220), 'Heart Tank', 'item'), 'T': ('T', (120, 200, 255), 'Sub-Tank', 'item'),
    'A': ('A', (120, 230, 255), 'Capsule giáp', 'item'), 'C': ('⚑', (140, 255, 140), 'Checkpoint', 'item'),
    'V': ('V', (255, 230, 120), 'Ride Armor / Chaser', 'item'), 'K': ('K', (255, 255, 120), 'Công tắc', 'item'),
    'E': ('E', (255, 210, 120), 'Năng lượng lớn', 'item'),
}
PIT = {  # đáy hố: (màu, tên)
    'vuc': ((8, 8, 12), 'Vực (rơi = mất mạng)'), 'lava': ((255, 110, 30), 'Dung nham'),
    'gai': ((230, 230, 240), 'Gai'), 'nuoc': ((40, 110, 200), 'Nước sâu'), 'axit': ((120, 230, 60), 'Hồ axit'),
    'bun': ((110, 80, 50), 'Bùn (chậm)'), 'tuyet': ((220, 235, 245), 'Hố tuyết'),
}
LEDGE = {  # loại bệ: (màu, tên)
    'ke': ((215, 180, 120), 'Bệ / kệ'), 'move': ((120, 220, 255), 'Bệ di động'),
    'crumble': ((255, 150, 70), 'Bệ sập'), 'phase': ((200, 140, 255), 'Bệ 2 pha'),
    'cloud': ((235, 240, 255), 'Khối mây'), 'cable': ((170, 200, 120), 'Bệ treo cáp'),
    'log': ((160, 110, 60), 'Khúc gỗ trôi'), 'rotate': ((255, 200, 120), 'Bệ xoay'),
    'glass': ((170, 230, 255), 'Kính trơn'), 'thruster': ((255, 120, 120), 'Bệ phản lực'),
    'ghost': ((200, 200, 230), 'Bệ ảo ảnh'), 'flower': ((255, 140, 200), 'Bệ hoa nở/khép'),
    'mush': ((255, 120, 170), 'Nấm bật'), 'ice': ((200, 240, 255), 'Tảng băng trôi'),
}
ZONE = {  # vùng: (màu RGBA, tên)
    'wind': ((150, 200, 255, 60), 'Vùng gió'), 'water': ((40, 110, 220, 70), 'Nước'),
    'laser': ((255, 60, 60, 80), 'Tia laser'), 'light': ((255, 240, 120, 55), 'Đèn pha'),
    'rain': ((140, 255, 90, 45), 'Mưa axit'), 'slow': ((190, 120, 255, 55), 'Vùng chậm'),
    'grav': ((150, 90, 255, 60), 'Đảo trọng lực'), 'lavarise': ((255, 90, 30, 70), 'Dung nham dâng'),
    'current': ((60, 170, 220, 60), 'Dòng chảy'), 'dark': ((0, 0, 0, 120), 'Vùng tối'),
    'updraft': ((200, 255, 255, 55), 'Luồng khí nâng'), 'spark': ((255, 255, 120, 60), 'Sàn điện'),
    'crush': ((180, 180, 190, 70), 'Ép / nghiền'), 'fire': ((255, 140, 40, 70), 'Lửa'),
    'cold': ((200, 240, 255, 50), 'Gió tuyết'), 'avalanche': ((240, 250, 255, 70), 'Tuyết lở'),
}
THEME = {'intro': ((58, 52, 62), (150, 130, 110)), 'metal': ((52, 54, 64), (140, 140, 150)), 'water': ((26, 46, 74), (90, 140, 170)),
         'volt': ((48, 44, 30), (190, 170, 90)), 'nature': ((30, 48, 30), (110, 150, 90)), 'shadow': ((40, 30, 54), (120, 100, 150)),
         'wind': ((44, 56, 74), (170, 190, 210)), 'fire': ((56, 32, 28), (150, 100, 70)), 'ice': ((44, 60, 74), (190, 220, 235)),
         'core': ((54, 28, 48), (170, 110, 160))}
MOVE = {None: 'đi', 'j': 'nhảy', 'dj': 'lướt-nhảy', 'wk': 'đá tường', 'drop': 'rơi xuống', 'ride': 'cưỡi xe',
        'swim': 'nước (nhảy cao)', 'fly': 'bay / giáp', 'grav': 'trọng lực đảo', 'updraft': 'luồng khí nâng',
        'cable': 'bệ cáp', 'lift': 'bệ di động', 'belt': 'băng chuyền', 'tele': 'cổng dịch chuyển', 'mush': 'nấm bật',
        'vine': 'dây leo đu', 'thruster': 'bệ phản lực', 'dash': 'lướt dưới khe thấp', 'slide': 'trượt dốc'}
SPECIAL = {'ride', 'swim', 'fly', 'grav', 'updraft', 'cable', 'lift', 'tele', 'mush', 'vine', 'thruster', 'slide'}


class Room:
    def __init__(self, code, name, kind, h, diff, desc, timing=''):
        self.code, self.name, self.kind, self.h, self.diff, self.desc, self.timing = code, name, kind, h, diff, desc, timing
        self.w = 0
        self.prims = []       # hình học / bẫy / thực thể (toạ độ cục bộ)
        self.path = []        # (x, y, tag)
        self.secret = []      # list các đoạn [(x, y), ...]
        self.entry = self.exit = None
        self.area = ''
        self.ox = self.oy = 0
        self.branch = False   # phòng nhánh vẽ dưới phòng trước

    # toạ độ toàn màn
    def G(self, x, y):
        return x + self.ox, y + self.oy


class Stage:
    def __init__(self, sid, title, boss, theme, act, kind, concept, refs):
        self.sid, self.title, self.boss, self.theme, self.act, self.kind = sid, title, boss, theme, act, kind
        self.concept, self.refs = concept, refs
        self.rooms, self.areas, self.secrets, self.engine, self.art = [], [], [], [], []
        self.boss_info = {}
        self.capsule = ''
        self.capsule_short = ''
        self.mech = []

    def add(self, room, area=None):
        if area: room.area = area
        self.rooms.append(room); return room


# =====================================================================================
# Xếp phòng
# =====================================================================================
def layout(st):
    x, yfloor, prev = 0, 0.0, None
    for r in st.rooms:
        if r.branch and prev is not None:
            r.ox, r.oy = prev.ox + (prev.w - r.w) / 2, prev.oy + prev.h + 3
            continue
        r.ox = x
        r.oy = yfloor - r.entry
        x += r.w
        yfloor = r.oy + r.exit
        prev = r
    miny = min(r.oy for r in st.rooms)
    for r in st.rooms: r.oy -= miny - 2
    st.W = max(r.ox + r.w for r in st.rooms) + 2
    st.H = max(r.oy + r.h for r in st.rooms) + 2


# =====================================================================================
# Bề mặt đứng được + kiểm tra đường chính
# =====================================================================================
def surfaces(r):
    out = []  # (x0, x1, y0, y1) – đoạn thẳng (y theo x)
    for p in r.prims:
        k = p[0]
        if k == 'floor': out.append((p[1], p[2], p[3], p[3]))
        elif k == 'block': out.append((p[1], p[3], p[2], p[2]))
        elif k == 'slope': out.append((p[1], p[3], p[2], p[4]))
        elif k == 'ledge': out.append((p[1], p[1] + p[3], p[2], p[2]))
        elif k == 'belt': out.append((p[1], p[2], p[3], p[3]))
    return out


def surf_y(surfs, x):
    ys = []
    for x0, x1, y0, y1 in surfs:
        if x0 - 1e-6 <= x <= x1 + 1e-6:
            ys.append(y0 + (y1 - y0) * ((x - x0) / (x1 - x0) if x1 != x0 else 0))
    return ys


def check_room(r):
    errs = []
    S = surfaces(r)
    for i in range(1, len(r.path)):
        (ax, ay, _), (bx, by, tag) = r.path[i - 1], r.path[i]
        dx, rise = abs(bx - ax), ay - by
        if tag in SPECIAL or tag == 'dash':
            continue
        if tag is None or tag == 'belt':
            # đi bộ: phải có nền liên tục giữa hai điểm (cùng độ cao hoặc dốc)
            n = max(2, int(dx * 2))
            for k in range(n + 1):
                xx = ax + (bx - ax) * k / n
                yy = ay + (by - ay) * k / n
                if not any(abs(y - yy) < .35 for y in surf_y(S, xx)):
                    errs.append(f'{r.code}: đi bộ qua chỗ không có nền tại x={xx:.1f}, y={yy:.1f}'); break
        elif tag == 'j':
            if rise > JUMP_UP + 1e-6: errs.append(f'{r.code}: nhảy lên {rise:.1f} ô (> {JUMP_UP}) tại x={ax:.1f}')
            if dx > JUMP_FAR + 1e-6: errs.append(f'{r.code}: nhảy xa {dx:.1f} ô (> {JUMP_FAR}) tại x={ax:.1f}')
        elif tag == 'dj':
            if rise > JUMP_UP + 1e-6: errs.append(f'{r.code}: lướt-nhảy lên {rise:.1f} ô tại x={ax:.1f}')
            if dx > DASH_FAR + 1e-6: errs.append(f'{r.code}: lướt-nhảy xa {dx:.1f} ô (> {DASH_FAR}) tại x={ax:.1f}')
        elif tag == 'wk':
            walls = [p for p in r.prims if p[0] == 'block' and (abs(p[1] - bx) < 2.5 or abs(p[3] - bx) < 2.5)] + \
                    ([1] if bx <= 3 or bx >= r.w - 3 else [])
            if not walls: errs.append(f'{r.code}: đá tường nhưng không có vách gần x={bx:.1f}')
        elif tag == 'drop':
            if rise > 1e-6: errs.append(f'{r.code}: "rơi" nhưng lại đi lên tại x={ax:.1f}')
        # điểm đến phải là nền (trừ các kiểu đặc biệt)
        if tag in (None, 'j', 'dj', 'drop', 'belt') and not any(abs(y - by) < .35 for y in surf_y(S, bx)):
            errs.append(f'{r.code}: điểm ({bx:.1f}, {by:.1f}) không đứng trên nền')
    return errs


def counts(st):
    c = {}
    for r in st.rooms:
        for p in r.prims:
            if p[0] == 'e': c[p[1]] = c.get(p[1], 0) + 1
    return c


def check_stage(st):
    errs = []
    for r in st.rooms: errs += check_room(r)
    # nối phòng: điểm cuối phòng trước và điểm đầu phòng sau phải liền nhau
    main = [r for r in st.rooms if not r.branch]
    for a, b in zip(main, main[1:]):
        if not a.path or not b.path: continue
        ax, ay = a.G(*a.path[-1][:2]); bx, by = b.G(*b.path[0][:2])
        if abs(ax - bx) > 1.01 or abs(ay - by) > .51:
            errs.append(f'nối {a.code}→{b.code}: ({ax:.1f},{ay:.1f}) ≠ ({bx:.1f},{by:.1f})')
    c = counts(st)
    en = c.get('S', 0) + c.get('D', 0) + c.get('B', 0)
    lo, hi = (7, 10) if st.kind == 'fortress' else (6, 10) if st.kind == 'intro' else (11, 14)
    if not lo <= en <= hi: errs.append(f'số kẻ địch thường {en} (chuẩn {lo}–{hi})')
    need = {'C': 2, 'M': 1, '*': 1, 'R': 4}
    if st.kind != 'fortress': need.update({'H': 1, 'T': 1})
    else:
        need.update({'H': 0, 'T': 0})
        if c.get('E', 0) < 1: errs.append('màn pháo đài thiếu trạm năng lượng lớn trước boss')
    for k, v in need.items():
        if c.get(k, 0) != v: errs.append(f'{ENT[k][2]}: {c.get(k, 0)} (chuẩn {v})')
    peak = max(r.diff for r in st.rooms if r.code != 'BOSS')
    want = 8 if st.kind == 'fortress' else 3 if st.kind == 'intro' else 7
    if peak != want: errs.append(f'đỉnh độ khó {peak} (chuẩn {want})')
    return errs


# =====================================================================================
# Vẽ sơ đồ
# =====================================================================================
T = 9  # px mỗi ô trên sơ đồ


def draw(st, path):
    fb, fs, ft = ImageFont.truetype(FONTB, 12), ImageFont.truetype(FONT, 10), ImageFont.truetype(FONTB, 16)
    bg, rock = THEME[st.theme]
    legend_h = 150
    TOP = 40
    img = Image.new('RGBA', (int(st.W * T) + 20, int(st.H * T) + legend_h + TOP), (12, 15, 26, 255))
    d = ImageDraw.Draw(img, 'RGBA')
    over = Image.new('RGBA', img.size, (0, 0, 0, 0)); od = ImageDraw.Draw(over)   # lớp vùng bán trong suốt
    used = {'ent': set(), 'pit': set(), 'ledge': set(), 'zone': set(), 'misc': set()}
    P = lambda r, x, y: (10 + (x + r.ox) * T, TOP + (y + r.oy) * T)

    for r in st.rooms:
        x0, y0 = P(r, 0, 0); x1, y1 = P(r, r.w, r.h)
        col = (88, 30, 50) if r.code == 'BOSS' else (70, 40, 62) if r.code == 'MID' else bg
        d.rectangle([x0, y0, x1, y1], fill=col + (255,), outline=(120, 120, 140))
    for r in st.rooms:
        for p in r.prims:
            k = p[0]
            if k in ('floor', 'ceil', 'block'):
                if k == 'floor': a, b = P(r, p[1], p[3]), P(r, p[2], r.h)
                elif k == 'ceil': a, b = P(r, p[1], 0), P(r, p[2], p[3])
                else: a, b = P(r, p[1], p[2]), P(r, p[3], p[4])
                d.rectangle([a, b], fill=rock + (255,))
            elif k == 'slope':
                pts = [P(r, p[1], p[2]), P(r, p[3], p[4]), P(r, p[3], r.h), P(r, p[1], r.h)]
                d.polygon(pts, fill=rock + (255,))
            elif k == 'pit':
                c, _ = PIT[p[3]]; used['pit'].add(p[3])
                a, b = P(r, p[1], r.h - 1), P(r, p[2], r.h)
                d.rectangle([a, b], fill=c + (255,))
                if p[3] == 'gai':
                    for xx in range(int(a[0]), int(b[0]) - 3, 6): d.polygon([(xx, b[1]), (xx + 3, a[1]), (xx + 6, b[1])], fill=(235, 235, 245))
                if p[3] == 'vuc': d.text((a[0] + 2, a[1] - 1), '▼', fill=(200, 60, 60), font=fs)
            elif k == 'spikes':
                used['pit'].add('gai'); x_0, x_1, yy, side = p[1], p[2], p[3], p[4]
                a, b = P(r, x_0, yy), P(r, x_1, yy)
                for xx in range(int(a[0]), int(b[0]) - 3, 6):
                    tip = a[1] - 6 if side == 'floor' else a[1] + 6
                    d.polygon([(xx, a[1]), (xx + 3, tip), (xx + 6, a[1])], fill=(235, 235, 245))
            elif k == 'zone':
                c, _ = ZONE[p[5]]; used['zone'].add(p[5])
                a, b = P(r, p[1], p[2]), P(r, p[3], p[4]); od.rectangle([a, b], fill=c, outline=c[:3] + (170,))
                if len(p) > 6 and p[6]: od.text((a[0] + 3, a[1] + 2), p[6], fill=(230, 240, 255, 255), font=fs)
            elif k == 'belt':
                used['misc'].add('belt'); a, b = P(r, p[1], p[3]), P(r, p[2], p[3])
                d.rectangle([a[0], a[1] - 3, b[0], a[1]], fill=(110, 110, 120))
                arrow = '←' if p[4] < 0 else '→'
                for xx in range(int(a[0]) + 4, int(b[0]) - 8, 40): d.text((xx, a[1] - 15), arrow, fill=(255, 220, 140), font=fs)
            elif k == 'wall_break':
                used['misc'].add('break'); a, b = P(r, p[1], p[2]), P(r, p[1] + 1, p[3])
                d.rectangle([a, b], fill=(150, 120, 90)); d.line([a, b], fill=(60, 40, 30), width=2)
        pass
    img.alpha_composite(over); d = ImageDraw.Draw(img, 'RGBA')
    for r in st.rooms:
        for p in r.prims:
            if p[0] == 'ledge':
                c, _ = LEDGE[p[4]]; used['ledge'].add(p[4])
                a, b = P(r, p[1], p[2]), P(r, p[1] + p[3], p[2])
                d.rectangle([a[0], a[1], b[0], a[1] + 4], fill=c + (255,))
    # đường đi
    for r in st.rooms:
        pts = [P(r, x, y - .55) for x, y, _ in r.path]
        for i in range(1, len(pts)):
            tag = r.path[i][2]
            col = (120, 230, 255) if tag not in SPECIAL else (255, 230, 120)
            d.line([pts[i - 1], pts[i]], fill=col, width=2)
        if len(pts) > 1:
            (ax, ay), (bx, by) = pts[-2], pts[-1]; ang = math.atan2(by - ay, bx - ax)
            d.polygon([(bx, by), (bx - 8 * math.cos(ang - .45), by - 8 * math.sin(ang - .45)), (bx - 8 * math.cos(ang + .45), by - 8 * math.sin(ang + .45))], fill=(120, 230, 255))
        for seg in r.secret:
            sp = [P(r, x, y - .55) for x, y in seg]
            for i in range(1, len(sp)):
                (ax, ay), (bx, by) = sp[i - 1], sp[i]; L = max(1, math.hypot(bx - ax, by - ay))
                for t0 in range(0, int(L), 8):
                    t1 = min(L, t0 + 5)
                    d.line([(ax + (bx - ax) * t0 / L, ay + (by - ay) * t0 / L), (ax + (bx - ax) * t1 / L, ay + (by - ay) * t1 / L)], fill=(255, 120, 200), width=2)
    # thực thể + ghi chú + nhãn phòng
    for r in st.rooms:
        x0, y0 = P(r, 0, 0)
        d.text((x0 + 3, y0 - 28), f'{r.code} {r.name}', fill=(255, 230, 160), font=fb)
        d.text((x0 + 3, y0 - 14), f'độ khó {r.diff} · {r.w:g}×{r.h:g}', fill=(200, 200, 210), font=fs)
        for p in r.prims:
            if p[0] == 'e':
                t, c, _, _ = ENT[p[1]]; used['ent'].add(p[1])
                cx, cy = P(r, p[2], p[3] - .9)
                d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=c + (255,)); d.text((cx - 4, cy - 6), t, fill=(0, 0, 0), font=fs)
            elif p[0] == 'note':
                a = P(r, p[1], p[2]); d.text(a, p[3], fill=(225, 225, 235), font=fs)
    # khung hình chuẩn ở phòng đầu
    r0 = st.rooms[0]; vx, vy = P(r0, 1, r0.h - VIEW_H)
    d.rectangle([vx, vy, vx + VIEW_W * T, vy + VIEW_H * T], outline=(255, 255, 255, 230), width=2)
    d.text((vx + 3, vy + 2), '1 màn hình 20×11.25 ô', fill=(255, 255, 255), font=fs)
    # tiêu đề + chú giải (chỉ những gì có trong màn)
    y0 = TOP + int(st.H * T) + 8
    d.text((10, y0), f'{st.title.upper()} · Boss: {st.boss} · {st.act} · 1 ô = 32px · khung hình 20×11.25 ô · tổng ~{int(st.W)}×{int(st.H)} ô', fill=(255, 230, 160), font=ft)
    d.text((10, y0 + 22), ' | '.join(f'{a}: {" → ".join(c)}' for a, _, c in st.areas), fill=(200, 200, 210), font=fs)
    items = [(ENT[k][1], ENT[k][2], 'ent', ENT[k][0]) for k in ENT if k in used['ent']]
    items += [(PIT[k][0], PIT[k][1], 'box', '') for k in PIT if k in used['pit']]
    items += [(LEDGE[k][0], LEDGE[k][1], 'bar', '') for k in LEDGE if k in used['ledge']]
    items += [(ZONE[k][0][:3], ZONE[k][1], 'box', '') for k in ZONE if k in used['zone']]
    if 'belt' in used['misc']: items.append(((110, 110, 120), 'Băng chuyền', 'bar', ''))
    if 'break' in used['misc']: items.append(((150, 120, 90), 'Tường phá được', 'box', ''))
    items += [((120, 230, 255), 'Đường chính', 'line', ''), ((255, 230, 120), 'Đoạn cơ chế đặc biệt', 'line', ''), ((255, 120, 200), 'Lối bí mật', 'dash', '')]
    for i, (c, n, kind, t) in enumerate(items):
        x = 10 + (i % 7) * 175; y = y0 + 44 + (i // 7) * 20
        if kind == 'ent': d.ellipse([x, y, x + 14, y + 14], fill=c); d.text((x + 3, y + 1), t, fill=(0, 0, 0), font=fs)
        elif kind == 'box': d.rectangle([x, y + 2, x + 14, y + 14], fill=c)
        elif kind == 'bar': d.rectangle([x, y + 6, x + 14, y + 10], fill=c)
        elif kind == 'line': d.line([x, y + 8, x + 14, y + 8], fill=c, width=2)
        else: d.line([x, y + 8, x + 5, y + 8], fill=c, width=2); d.line([x + 9, y + 8, x + 14, y + 8], fill=c, width=2)
        d.text((x + 20, y + 1), n, fill=(220, 220, 220), font=fs)
    img.convert('RGB').save(path, optimize=True)
    return img.size


# =====================================================================================
# Kịch bản (markdown)
# =====================================================================================
STANDARD = ('Khung hình 640×360 px = 20×11.25 ô. Hành lang: trần 1 ô, trong lòng 9 ô, khối trần luôn nằm trong khung; '
            'phòng nhảy bệ/vực/nước 11 ô; phòng 2 tầng 17 ô; đấu trường cao 11 ô, rộng 20–30 ô; giếng rộng 12–20 ô. '
            f'X nhảy cao ~2.6 ô, xa ~5 ô: trên đường chính gờ ≤ {JUMP_UP} ô, nhảy xa ≤ {JUMP_FAR} ô (lướt-nhảy ≤ {DASH_FAR} ô); '
            'cao/xa hơn chỉ bằng đá tường, giáp hoặc cơ chế của màn, và dùng cho bí mật.')


def fmt(v):
    return f'{v:g}'


def describe_geometry(r):
    out = []
    for p in r.prims:
        k = p[0]
        gx = lambda x: fmt(x + r.ox)
        gy = lambda y: fmt(y + r.oy)
        if k == 'pit': out.append(f'hố {PIT[p[3]][1].lower()} x {gx(p[1])}–{gx(p[2])} (rộng {fmt(p[2] - p[1])} ô)')
        elif k == 'ledge': out.append(f'{LEDGE[p[4]][1].lower()} x {gx(p[1])}–{gx(p[1] + p[3])}, y {gy(p[2])}')
        elif k == 'slope': out.append(f'dốc x {gx(p[1])}–{gx(p[3])} (y {gy(p[2])}→{gy(p[4])})')
        elif k == 'zone': out.append(f'{ZONE[p[5]][1].lower()} x {gx(p[1])}–{gx(p[3])}, y {gy(p[2])}–{gy(p[4])}' + (f' ({p[6]})' if len(p) > 6 and p[6] else ''))
        elif k == 'belt': out.append(f'băng chuyền x {gx(p[1])}–{gx(p[2])} ({p[4]:+g} px/s)')
        elif k == 'wall_break': out.append(f'tường phá được x {gx(p[1])}, y {gy(p[2])}–{gy(p[3])}')
        elif k == 'spikes': out.append(f'gai {"trần" if p[4] == "ceil" else "sàn"} x {gx(p[1])}–{gx(p[2])}')
        elif k == 'block' and p[4] - p[2] <= 4 and p[3] - p[1] <= 6: out.append(f'khối x {gx(p[1])}–{gx(p[3])}, y {gy(p[2])}–{gy(p[4])}')
    return out


def write_doc(st, path, map_rel, errs):
    c = counts(st)
    L = [f'# {st.title} — Boss {st.boss}', '',
         f'`{st.sid}` · chủ đề `{st.theme}` · {st.act} · tổng ~{int(st.W)}×{int(st.H)} ô ({int(st.W) * 32}×{int(st.H) * 32} px)', '',
         f'![Sơ đồ]({map_rel})', '', '## Ý tưởng', st.concept, '', '## Tham khảo', st.refs, '',
         '## Chuẩn kích thước', STANDARD, '', '## Cấu trúc', '']
    for a, desc, codes in st.areas: L.append(f'- **{a}** ({" → ".join(codes)}): {desc}')
    L += ['', '## Nhịp màn (độ khó)', ' → '.join(f'{r.code} ({r.diff})' for r in st.rooms), '', '## Kịch bản từng phòng', '']
    kinds = {'R': 'đi ngang', 'U': 'leo dọc', 'D': 'đi xuống', 'A': 'đấu trường'}
    for r in st.rooms:
        fx0, fy0 = r.G(0, r.entry); fx1, fy1 = r.G(r.w, r.exit)
        L.append(f'### {r.code} – {r.name} · {kinds[r.kind]} · độ khó {r.diff}')
        L.append(f'*x {fmt(r.ox)}–{fmt(r.ox + r.w)}, y {fmt(r.oy)}–{fmt(r.oy + r.h)} ({fmt(r.w)}×{fmt(r.h)} ô) · vào ở sàn y {fmt(fy0)}, ra ở sàn y {fmt(fy1)}*' + (f' · {r.area}' if r.area else ''))
        L.append(''); L.append(r.desc)
        if r.timing: L.append(f'- **Thông số:** {r.timing}')
        geo = describe_geometry(r)
        if geo: L.append('- **Địa hình:** ' + '; '.join(geo))
        ents = [f'{ENT[p[1]][2]} ({fmt(p[2] + r.ox)}, {fmt(p[3] + r.oy)})' + (f' – {p[4]}' if len(p) > 4 and p[4] else '') for p in r.prims if p[0] == 'e']
        if ents: L.append('- **Thực thể:** ' + '; '.join(ents))
        moves = sorted({MOVE.get(t, t) for _, _, t in r.path[1:] if t})
        if moves: L.append('- **Đường chính dùng:** ' + ', '.join(moves))
        if r.secret: L.append('- **Lối bí mật:** ' + '; '.join(' → '.join(f'({fmt(x + r.ox)}, {fmt(y + r.oy)})' for x, y in s) for s in r.secret))
        L.append('')
    # bảng
    L += ['## Bảng kẻ địch và vật phẩm', '', '| Loại | Phòng | x | y | Ghi chú |', '|---|---|---|---|---|']
    for r in st.rooms:
        for p in r.prims:
            if p[0] == 'e': L.append(f'| {ENT[p[1]][2]} | {r.code} | {fmt(p[2] + r.ox)} | {fmt(p[3] + r.oy)} | {p[4] if len(p) > 4 else ""} |')
    en = c.get('S', 0) + c.get('D', 0) + c.get('B', 0)
    L += ['', f'Tổng: {en} kẻ địch thường (Sniper {c.get("S", 0)}, Drone {c.get("D", 0)}, Brute {c.get("B", 0)}), '
          f'{c.get("R", 0)} Reploid, {c.get("C", 0)} checkpoint, Heart Tank {c.get("H", 0)}, Sub-Tank {c.get("T", 0)}, capsule {c.get("A", 0)}.', '']
    if st.capsule: L += ['## Capsule theo dữ liệu game', st.capsule, '']
    if st.secrets:
        L += ['## Bí mật', '| Vật phẩm | Phòng | Cách lấy |', '|---|---|---|'] + [f'| {a} | {b} | {c_} |' for a, b, c_ in st.secrets] + ['']
    b = st.boss_info
    if b:
        L += ['## Boss', f'**{st.boss}**' + (f' · điểm yếu: {b["weak"]}' if b.get('weak') else '')]
        if b.get('attacks'): L.append(f'- **Bộ chiêu (dữ liệu game):** {b["attacks"]}')
        if b.get('arena'): L.append(f'- **Đấu trường:** {b["arena"]}')
        if b.get('phase2'): L.append(f'- **Pha 2 (dưới 50% HP):** {b["phase2"]}')
        L.append('')
    L += ['## Engine cần bổ sung'] + [f'- {e}' for e in st.engine] + ['', '## Hình cần vẽ'] + [f'- {a}' for a in st.art] + ['']
    L += ['## Kiểm tra tự động', f'Đường chính đã được kiểm tra theo khả năng nhảy (gờ ≤ {JUMP_UP} ô, nhảy xa ≤ {JUMP_FAR} ô, lướt-nhảy ≤ {DASH_FAR} ô, '
          'đi bộ phải có nền) và theo quy ước số lượng.', '']
    L.append('**Kết quả: đạt.**' if not errs else '**Còn lỗi:**\n' + '\n'.join(f'- {e}' for e in errs))
    open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


# =====================================================================================
# Xuất JSON (cùng kiểu dữ liệu với levels/lo-nham-thach.level.json)
# =====================================================================================
def export_json(st, path):
    J = dict(name=st.title, stage=st.sid, tileSize=32, width=st.W, height=st.H, rooms=[], solids=[], oneWay=[], slopes=[],
             hazards=[], zones=[], belts=[], breakables=[], enemies=[], items=[], path=[])
    for r in st.rooms:
        J['rooms'].append(dict(name=f'{r.code} {r.name}', x=r.ox, y=r.oy, w=r.w, h=r.h, kind=r.kind, difficulty=r.diff, area=r.area))
        for p in r.prims:
            k = p[0]; G = r.G
            if k == 'floor': x, y = G(p[1], p[3]); J['solids'].append(dict(x=x, y=y, w=p[2] - p[1], h=r.h - p[3]))
            elif k == 'ceil': x, y = G(p[1], 0); J['solids'].append(dict(x=x, y=y, w=p[2] - p[1], h=p[3]))
            elif k == 'block': x, y = G(p[1], p[2]); J['solids'].append(dict(x=x, y=y, w=p[3] - p[1], h=p[4] - p[2]))
            elif k == 'slope': x0, y0 = G(p[1], p[2]); x1, y1 = G(p[3], p[4]); J['slopes'].append(dict(x0=x0, y0=y0, x1=x1, y1=y1, bottom=r.oy + r.h))
            elif k == 'ledge': x, y = G(p[1], p[2]); J['oneWay'].append(dict(x=x, y=y, w=p[3], h=.5, type=p[4]))
            elif k == 'pit': x, y = G(p[1], r.h - 1); J['hazards'].append(dict(type=p[3], x=x, y=y, w=p[2] - p[1], h=1))
            elif k == 'spikes': x, y = G(p[1], p[3]); J['hazards'].append(dict(type='gai', side=p[4], x=x, y=y, w=p[2] - p[1], h=.5))
            elif k == 'zone': x, y = G(p[1], p[2]); J['zones'].append(dict(type=p[5], x=x, y=y, w=p[3] - p[1], h=p[4] - p[2], label=p[6] if len(p) > 6 else ''))
            elif k == 'belt': x, y = G(p[1], p[3]); J['belts'].append(dict(x=x, y=y, w=p[2] - p[1], speed=p[4]))
            elif k == 'wall_break': x, y = G(p[1], p[2]); J['breakables'].append(dict(x=x, y=y, w=1, h=p[3] - p[2]))
            elif k == 'e':
                x, y = G(p[2], p[3]); o = dict(type=p[1], name=ENT[p[1]][2], x=x, y=y, room=r.code, note=p[4] if len(p) > 4 else '')
                (J['enemies'] if ENT[p[1]][3] in ('enemy', 'boss') else J['items']).append(o)
        J['path'] += [dict(x=G(x, y)[0], y=G(x, y)[1], move=t or 'walk') for x, y, t in r.path]
    json.dump(J, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
