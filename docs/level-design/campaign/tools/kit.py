"""Khối ghép phòng. Mỗi lệnh thêm hình học + đường đi chính tương ứng, để toạ độ luôn khớp nhau.

Phòng ngang (R / A): trần y 0–1, nền mặc định y=10, đáy y=12 → trong lòng 9 ô.
Phòng nhảy bệ: h=14 (vực sâu hơn). Phòng 2 tầng: dùng TwoTier (tầng trên nền y=9, tầng dưới y=18, h=19).
Giếng (U / D): Shaft, vách 2 ô hai bên, rộng 12–20 ô.
"""
from lib import Room


class R:
    def __init__(self, code, name, diff, desc, kind='R', h=12, floor=10, timing='', ceil=1, slab=False):
        self.r = Room(code, name, kind, h, diff, desc, timing)
        self.x, self.y = 0.0, float(floor)
        self.ceil, self.slab = ceil, slab
        self.r.entry = float(floor)
        self.r.path.append((0.0, float(floor), None))
        self.seg_start = 0.0

    # ---- nội bộ ----
    def _floor(self, x0, x1, y):
        if x1 <= x0: return
        if self.slab: self.r.prims.append(('block', x0, y, x1, y + 1))
        else: self.r.prims.append(('floor', x0, x1, y))

    def _p(self, x, y, tag=None):
        self.r.path.append((float(x), float(y), tag))

    # ---- địa hình cơ bản ----
    def run(self, n, ents=''):
        """Nền phẳng dài n ô. ents: chuỗi mã đặt đều trên đoạn (vd 'S D')."""
        x0 = self.x; self._floor(x0, x0 + n, self.y)
        codes = ents.split()
        for i, c in enumerate(codes):
            ex = x0 + n * (i + 1) / (len(codes) + 1)
            self.ent(c, ex - self.x)
        self.x += n; self._p(self.x, self.y); return self

    def gap(self, n, kind='vuc', dy=0, land=1):
        """Hố rộng n ô, nhảy qua; nền bên kia lệch dy (âm = cao hơn)."""
        if not self.slab: self.r.prims.append(('pit', self.x, self.x + n, kind))
        self.x += n; self.y += dy
        self._floor(self.x, self.x + land, self.y)
        self._p(self.x, self.y, 'j' if n <= 5 else 'dj')
        self.x += land; self._p(self.x, self.y); return self

    def step(self, dy, n=2):
        """Bậc lên (dy<0) hoặc xuống (dy>0), rồi đi tiếp n ô."""
        self.y += dy; self._floor(self.x, self.x + n, self.y)
        self._p(self.x, self.y, 'j' if dy < 0 else 'drop')
        self.x += n; self._p(self.x, self.y); return self

    def slope(self, n, dy):
        self.r.prims.append(('slope', self.x, self.y, self.x + n, self.y + dy))
        self.x += n; self.y += dy; self._p(self.x, self.y); return self

    def pillar(self, w, hgt, n_after=2):
        """Khối chắn trên nền: nhảy lên (≤2.5) và xuống."""
        self._floor(self.x, self.x + w + n_after, self.y)
        self.r.prims.append(('block', self.x, self.y - hgt, self.x + w, self.y))
        self._p(self.x, self.y - hgt, 'j'); self._p(self.x + w, self.y - hgt)
        self._p(self.x + w, self.y, 'drop'); self.x += w + n_after; self._p(self.x, self.y); return self

    def ledges(self, n, pts, kind='ke', pit='vuc', dy=0, land=2, tag='j'):
        """Vực rộng n ô, bắc cầu bằng bệ: pts = [(dx, dy_so_với_nền, rộng), ...] tính từ mép vực."""
        x0, y0 = self.x, self.y
        if not self.slab and pit: self.r.prims.append(('pit', x0, x0 + n, pit))
        for dx, ly, w in pts:
            self.r.prims.append(('ledge', x0 + dx, y0 + ly, w, kind))
            self._p(x0 + dx, y0 + ly, tag); self._p(x0 + dx + w, y0 + ly, 'lift' if kind in ('move', 'log', 'cable', 'cloud', 'thruster', 'ice', 'rotate') else None)
        self.x = x0 + n; self.y = y0 + dy
        self._floor(self.x, self.x + land, self.y); self._p(self.x, self.y, tag)
        self.x += land; self._p(self.x, self.y); return self

    def belt(self, n, speed, ents=''):
        self.r.prims.append(('belt', self.x, self.x + n, self.y, speed))
        x0 = self.x; self._floor(x0, x0 + n, self.y)
        for i, c in enumerate(ents.split()): self.r.prims.append(('e', c, x0 + n * (i + 1) / (len(ents.split()) + 1), self.y))
        self.x += n; self._p(self.x, self.y, 'belt'); return self

    def zone(self, n, kind, label='', y0=None, y1=None, ents='', walk=True):
        """Đoạn nền có vùng bẫy phủ lên (gió, mưa axit, đèn pha, laser...)."""
        top = self.ceil if (y0 is None and self.ceil) else (y0 if y0 is not None else self.y - 9)
        self.r.prims.append(('zone', self.x, top, self.x + n, self.y if y1 is None else y1, kind, label))
        return self.run(n, ents) if walk else self

    def spikes(self, n, side='floor', y=None):
        self.r.prims.append(('spikes', self.x, self.x + n, self.y if y is None else y, side)); return self

    def low(self, n, gap_h=1.6, label='khe thấp: lướt qua'):
        """Trần hạ thấp: chỉ còn khe gap_h ô, phải lướt."""
        self.r.prims.append(('block', self.x, (self.ceil or 0), self.x + n, self.y - gap_h))
        self._floor(self.x, self.x + n, self.y); self.note(label, 0, -gap_h - 1.2)
        self.x += n; self._p(self.x, self.y, 'dash'); return self

    def breakwall(self, hgt=4):
        self.r.prims.append(('wall_break', self.x, self.y - hgt, self.y)); return self

    def special(self, n, tag, dy=0, prims=(), floor=True, land=2):
        """Đoạn đi bằng cơ chế riêng (bơi, luồng khí, cáp, xe...). prims toạ độ tương đối với (x, y)."""
        for p in prims: self.r.prims.append(self._rel(p))
        self.x += n; self.y += dy
        if floor: self._floor(self.x, self.x + land, self.y)
        self._p(self.x, self.y, tag)
        if floor: self.x += land; self._p(self.x, self.y)
        return self

    def _rel(self, p):
        k = p[0]; X, Y = self.x, self.y
        if k in ('block',): return (k, X + p[1], Y + p[2], X + p[3], Y + p[4])
        if k == 'ledge': return (k, X + p[1], Y + p[2], p[3], p[4])
        if k == 'zone': return (k, X + p[1], Y + p[2], X + p[3], Y + p[4], p[5], p[6] if len(p) > 6 else '')
        if k == 'pit': return (k, X + p[1], X + p[2], p[3])
        if k == 'floor': return (k, X + p[1], X + p[2], Y + p[3])
        if k == 'spikes': return (k, X + p[1], X + p[2], Y + p[3], p[4])
        if k == 'e': return (k, p[1], X + p[2], Y + p[3]) + tuple(p[4:])
        if k == 'note': return (k, X + p[1], Y + p[2], p[3])
        return p

    def raw(self, *prims):
        for p in prims: self.r.prims.append(self._rel(p))
        return self

    # ---- thực thể / ghi chú / bí mật ----
    def ent(self, code, dx=0, dy=0, note=''):
        air = 3 if code == 'D' else 0
        self.r.prims.append(('e', code, self.x + dx, self.y + dy - air, note)); return self

    def note(self, text, dx=0, dy=-4):
        self.r.prims.append(('note', self.x + dx, self.y + dy, text)); return self

    def secret(self, *pts):
        """Lối bí mật: các điểm (dx, dy) tương đối với vị trí hiện tại."""
        self.r.secret.append([(self.x + dx, self.y + dy) for dx, dy in pts]); return self

    def done(self):
        r = self.r; r.w = self.x; r.exit = self.y
        if self.ceil: r.prims.insert(0, ('ceil', 0, r.w, self.ceil))
        return r


def Arena(code, name, diff, desc, w=30, boss='*', note='', h=12, timing='', extra=None):
    b = R(code, name, diff, desc, kind='A', h=h, timing=timing)
    b.run(w / 2 - 1).ent(boss, 0, 0, note).run(w / 2 + 1)
    if extra: extra(b)
    return b.done()


class Shaft:
    """Giếng dọc. up=True: vào ở đáy bên trái, ra ở đỉnh bên phải. up=False: ngược lại (đi xuống)."""

    def __init__(self, code, name, diff, desc, w=16, h=40, up=True, exit_floor=10, timing=''):
        self.r = Room(code, name, 'U' if up else 'D', h, diff, desc, timing)
        self.r.w = w; self.w, self.h, self.up = w, h, up
        bottom = h - 2
        if up:
            self.r.entry, self.r.exit = bottom, exit_floor
            self.r.prims += [('floor', 0, w, bottom), ('block', 0, 0, 2, bottom - 9), ('block', w - 2, exit_floor, w, bottom),
                             ('ceil', 0, w, 1), ('block', w - 5, exit_floor, w - 2, exit_floor + 1)]
            self.r.path.append((0.0, float(bottom), None)); self.cx, self.cy = 4.0, float(bottom)
            self.r.path.append((4.0, float(bottom), None))
        else:
            self.r.entry, self.r.exit = exit_floor, bottom
            self.r.prims += [('floor', 0, w, bottom), ('block', 0, exit_floor, 2, bottom), ('block', w - 2, 0, w, bottom - 9),
                             ('ceil', 0, w, 1), ('block', 2, exit_floor, 5, exit_floor + 1)]
            self.r.path.append((0.0, float(exit_floor), None)); self.cx, self.cy = 5.0, float(exit_floor)
            self.r.path.append((5.0, float(exit_floor), None))

    def climb(self, step=2.5, kind='ke', w=3, top=None, ents=None, tag='j', start=None):
        """Kệ so le cách nhau `step` ô theo chiều dọc. Lên: bắt đầu sát mép vào (trái), kết thúc sát lối ra (phải);
        giếng rộng thêm cột giữa để mọi cú nhảy ngang ≤ 5 ô."""
        r, W = self.r, self.w
        L, Rr = 4.0, W - 3.0 - w
        C = (L + Rr) / 2
        cols = [L, Rr] if W <= 15 else [L, C, Rr, C]
        ents = dict(ents or {})
        cen = lambda x: x + w / 2
        if self.up:
            ys, y = [], (self.cy if start is None else start) - step
            stop = (top if top is not None else r.exit) + .01
            while y > stop: ys.append(y); y -= step
            placed = []
            for i, y in enumerate(ys): placed.append((cols[i % len(cols)], y))
            goal = W - 4.0
            while placed and abs(goal - cen(placed[-1][0])) > 5:   # ghép thêm kệ cùng độ cao về phía lối ra
                x0, y0 = placed[-1]; nx = min(Rr, x0 + 5)
                if nx <= x0: break
                placed.append((nx, y0))
            prev_y = None
            for i, (x, y) in enumerate(placed):
                r.prims.append(('ledge', x, y, w, kind)); r.path.append((cen(x), y, tag if y != prev_y else 'j'))
                if i in ents: r.prims.append(('e', ents[i], cen(x), y - (3 if ents[i] == 'D' else 0), ''))
                prev_y = y
            r.path.append((goal, float(r.exit), tag)); r.path.append((float(W), float(r.exit), None))
        else:
            y, i = self.cy + step, 0
            colsd = [Rr, L] if W <= 15 else [C, Rr, C, L]
            while y < self.h - 2 - step * .5:
                x = colsd[i % len(colsd)]
                r.prims.append(('ledge', x, y, w, kind)); r.path.append((cen(x), y, 'drop'))
                if i in ents: r.prims.append(('e', ents[i], cen(x), y - (3 if ents[i] == 'D' else 0), ''))
                y += step; i += 1
            r.path.append((W - 3.0, float(self.h - 2), 'drop')); r.path.append((float(W), float(self.h - 2), None))
        return self

    def wallkick(self, y_from, y_to, side='left', ents=None):
        """Đoạn leo bằng đá tường dọc vách (đường chính)."""
        x = 2.4 if side == 'left' else self.w - 2.4
        r = self.r
        r.path.append((x, y_from, 'wk')); r.path.append((x, y_to, 'wk'))
        return self

    def add(self, *prims):
        self.r.prims += list(prims); return self

    def ent(self, code, x, y, note=''):
        self.r.prims.append(('e', code, x, y, note)); return self

    def note(self, text, x, y):
        self.r.prims.append(('note', x, y, text)); return self

    def secret(self, *pts):
        self.r.secret.append(list(pts)); return self

    def done(self):
        return self.r


def TwoTier(code, name, diff, desc, build_top, build_bottom, main='top', timing=''):
    """Phòng 2 tầng (h=19): tầng trên nền y=9 (sàn mỏng), tầng dưới nền y=18. Lối chính theo `main`,
    tầng kia vẽ như lối phụ/bí mật."""
    top = R(code, name, diff, desc, h=19, floor=9, slab=True, timing=timing)
    bot = R(code, name, diff, desc, h=19, floor=18)
    build_top(top); build_bottom(bot)
    a, b = top.done(), bot.done()
    if a.w != b.w:
        if a.w < b.w: top.run(b.w - a.w); a = top.done()
        else: bot.run(a.w - b.w); b = bot.done()
    m, o = (a, b) if main == 'top' else (b, a)
    m.prims = [p for p in a.prims if p[0] != 'ceil'] + [p for p in b.prims if p[0] != 'ceil'] + [('ceil', 0, a.w, 1)]
    m.secret = m.secret + o.secret + [[(x, y) for x, y, _ in o.path]]
    m.h = 19
    return m
