# Khuôn dựng sẵn cho các loại phòng lặp lại (giếng leo, giếng xuống, đấu trường, phòng nghỉ).
from lib import *


def shaft_up(w, h, entry=8, exit_h=8, n=4, first='right'):
    """Giếng leo: vào ở đáy bên trái (khe cao `entry`), ra ở đỉnh bên phải (khe cao `exit_h`).
    Trả về (geo, path)."""
    geo = [B(0, 0, 2, h - 2 - entry), B(0, h - 2, w, 2), B(w - 2, exit_h + 1, 2, h - 3 - exit_h), B(2, 0, w - 2, 1)]
    step = (h - 6 - exit_h) / (n + 0.5)
    pts = [(1, h - 3), (w / 2, h - 3)]
    for i in range(n):
        y = round(h - 2 - (i + 1) * step)
        right = (i % 2 == 0) == (first == 'right')
        x = w - 7 if right else 2
        geo.append(P(x, y, 5))
        pts.append((x + 2.5, y - 1))
    pts += [(w / 2, exit_h - 2), (w - 0.5, exit_h - 1)]
    return geo, PATH(*pts)


def shaft_down(w, h, entry=8, exit_h=7, n=4):
    """Giếng xuống: vào ở đỉnh bên trái, ra ở đáy bên phải."""
    geo = [B(0, 0, w, 1), B(0, entry + 1, 2, h - entry - 1), B(2, entry + 1, 7, 1), B(w - 2, 0, 2, h - 2 - exit_h), B(0, h - 2, w, 2)]
    step = (h - entry - 6) / (n + 0.5)
    pts = [(1, entry), (6, entry)]
    for i in range(n):
        y = round(entry + 2 + (i + 1) * step)
        x = w - 9 if i % 2 == 0 else 3
        geo.append(P(x, y, 6))
        pts.append((x + 3, y - 1))
    pts += [(w - 4, h - 3), (w - 0.5, h - 3)]
    return geo, PATH(*pts)


def arena(w=30, h=16, floor=14, walls=True, ceil=True):
    g = [F((0, floor), (w, floor))]
    if walls: g += [B(0, 0, 2, floor), B(w - 2, 0, 2, floor)]
    if ceil: g += [B(0, 0, w, 1)]
    g.append(PATH((3, floor - 1), (w - 3, floor - 1)))
    return g


def rest(code, name, x, y, text, w=30, h=14, reploid=True, refill='năng lượng nhỏ'):
    g = [B(0, 0, w, 2), F((0, 10), (w, 10)), BAR(w - 1, 2, 1, 8, 'door'), X(3, 5, refill), PATH((1, 9), (w - 2, 9))]
    if reploid: g.append(E('R', w // 2, 9))
    return Room(code, name, x, y, w, h, 2, g, text)


def stage(**kw):
    rooms = kw.pop('rooms')
    kw['rooms'] = rooms
    kw.setdefault('table_extra', [])
    return kw
