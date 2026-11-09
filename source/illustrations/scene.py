"""共通の情景パーツ（立面・平面）。lib.D に関数として作用する。"""
from lib import *

SKY = '#eef3f4'; WALL = '#f4f1ea'; ROOF = '#7d8a78'; GLASS = '#cfe1ea'; ROAD = '#d3d5cf'; LAWN = '#a9c58a'; LAWN_D = '#7ea457'
LEAF = '#7fa36a'; LEAF_D = '#4f7a3a'; TRUNK = '#8a6a48'


def ground(d, y, x=0, w=None, fill='#e4ddcc'):
    w = w or d.W
    d.rect(x, y, w, d.H - y, fill=fill, stroke='none'); d.line(x, y, x + w, y, stroke=LINE, sw=2.5)


def house(d, x, y, w=300, h=200, roof=80, win=True, door=True):
    """立面の家（y は地面）"""
    d.poly([(x - 16, y - h), (x + w / 2, y - h - roof), (x + w + 16, y - h)], fill=ROOF, stroke=LINE, sw=2.5)
    d.rect(x, y - h, w, h, fill=WALL, stroke=LINE, sw=2.5)
    if win:
        d.rect(x + 30, y - h + 40, 90, 70, fill=GLASS, stroke=LINE, sw=2); d.line(x + 75, y - h + 40, x + 75, y - h + 110, stroke=LINE, sw=1.5)
        d.rect(x + w - 120, y - h + 40, 90, 70, fill=GLASS, stroke=LINE, sw=2); d.line(x + w - 75, y - h + 40, x + w - 75, y - h + 110, stroke=LINE, sw=1.5)
    if door: d.rect(x + w / 2 - 28, y - 96, 56, 96, fill='#c9a06b', stroke=LINE, sw=2)


def person(d, x, y, s=1.0, color='#6f7f8f'):
    """立っている人（y は足元）"""
    h = 150 * s
    d.circle(x, y - h + 16 * s, 16 * s, fill='#f2c9a5', stroke='#b5835c', sw=2)
    d.rect(x - 18 * s, y - h + 34 * s, 36 * s, 66 * s, fill=color, stroke=LINE, sw=2, rx=10 * s)
    d.rect(x - 15 * s, y - h + 96 * s, 12 * s, 54 * s, fill='#4a5560', stroke=LINE, sw=2, rx=4)
    d.rect(x + 3 * s, y - h + 96 * s, 12 * s, 54 * s, fill='#4a5560', stroke=LINE, sw=2, rx=4)
    return (x + 10 * s, y - h + 14 * s)  # 目の位置


def sight(d, x1, y1, x2, y2, blocked=False, color=None):
    color = color or (WARN if not blocked else GREY)
    d.line(x1, y1, x2, y2, stroke=color, sw=2.5, dash='10 8')
    if blocked: d.ng(x2, y2, 15)
    else: d.arrow(x2 - (x2 - x1) * .02, y2 - (y2 - y1) * .02, x2, y2, color=color, sw=2.5, head=14)


def tree(d, x, y, h=200, r=60, color=LEAF):
    d.rect(x - 8, y - h + r, 16, h - r, fill=TRUNK, stroke=LINE, sw=2)
    d.circle(x, y - h + r * .2, r, fill=color, stroke=LEAF_D, sw=2.5)
    d.circle(x - r * .6, y - h + r * .7, r * .6, fill=color, stroke=LEAF_D, sw=2.5)
    d.circle(x + r * .6, y - h + r * .7, r * .6, fill=color, stroke=LEAF_D, sw=2.5)


def hedge(d, x, y, w, h):
    n = max(2, int(w / 50))
    for i in range(n):
        cx = x + (i + .5) * w / n
        d.ellipse(cx, y - h / 2, w / n * .62, h / 2, fill=LEAF, stroke=LEAF_D, sw=2)
    d.rect(x + 4, y - h * .45, w - 8, h * .45, fill=LEAF, stroke='none')
    d.line(x, y, x + w, y, stroke=LINE, sw=2.5)


def slat_fence(d, x, y, w, h, gap=6, slat=18, color='#6a6e70', post=METAL_D):
    yy = y - h + 6
    while yy + slat <= y - 6:
        d.rect(x, yy, w, slat, fill=color, stroke=LINE, sw=1.5); yy += slat + gap
    for px in (x, x + w - 10): d.rect(px, y - h, 10, h, fill=post, stroke=LINE, sw=1.5)


def block_wall(d, x, y, w, h, bw=78, bh=38, fill=CONC, stroke=CONC_D):
    rows = int(h / bh)
    for r in range(rows):
        off = 0 if r % 2 == 0 else -bw / 2
        xx = x + off
        while xx < x + w:
            x0 = max(x, xx); x1 = min(x + w, xx + bw)
            d.rect(x0, y - (r + 1) * bh, x1 - x0, bh, fill=fill, stroke=stroke, sw=1.8)
            xx += bw
    d.rect(x, y - rows * bh, w, rows * bh, fill='none', stroke=LINE, sw=2.5)


def car_side(d, x, y, w=300, color='#9fb0bf', facing=1):
    """横から見た車（y は地面、x は左端）"""
    h = w * .32
    p = f'M{x+w*.04},{y-h*.28} L{x+w*.04},{y-h*.62} Q{x+w*.06},{y-h*.72} {x+w*.2},{y-h*.74} L{x+w*.3},{y-h*.76} L{x+w*.42},{y-h} L{x+w*.74},{y-h} L{x+w*.86},{y-h*.74} Q{x+w*.97},{y-h*.7} {x+w*.97},{y-h*.5} L{x+w*.97},{y-h*.28} Z'
    if facing < 0:
        p = p  # 対称性は描画上問題にならないため簡略化
    d.path(p, fill=color, stroke=LINE, sw=2.5)
    d.poly([(x + w * .34, y - h * .76), (x + w * .44, y - h * .95), (x + w * .57, y - h * .95), (x + w * .57, y - h * .76)], fill=GLASS, stroke=LINE, sw=2)
    d.poly([(x + w * .61, y - h * .76), (x + w * .61, y - h * .95), (x + w * .72, y - h * .95), (x + w * .82, y - h * .76)], fill=GLASS, stroke=LINE, sw=2)
    for cx in (x + w * .24, x + w * .78):
        d.circle(cx, y - h * .22, h * .22, fill='#3d4448', stroke=LINE, sw=2); d.circle(cx, y - h * .22, h * .09, fill=METAL, stroke='none')


def car_top(d, x, y, w=120, l=240, color='#9fb0bf'):
    """上から見た車（x,y は左上、縦向き）"""
    d.rect(x, y, w, l, fill=color, stroke=LINE, sw=2.5, rx=26)
    d.rect(x + 14, y + l * .25, w - 28, l * .18, fill=GLASS, stroke=LINE, sw=2, rx=8)
    d.rect(x + 14, y + l * .7, w - 28, l * .12, fill=GLASS, stroke=LINE, sw=2, rx=8)


def window_people(d, x, y):
    """窓の中の人影（室内のプライバシーを表す）"""
    d.circle(x, y, 10, fill='#7d8790', stroke='none'); d.rect(x - 14, y + 10, 28, 26, fill='#7d8790', stroke='none', rx=8)


def panel_title(d, x, y, w, t, color=GREEN):
    d.rect(x, y, w, 40, fill=color, stroke='none', rx=8); d.text(x + w / 2, y + 28, t, 21, WHITE, 700, 'middle')


def points(d, x, y, items, size=19, gap=34, w=None):
    """箇条書き（● 色付き：good=緑 / bad=赤）"""
    for i, it in enumerate(items):
        good = not it.startswith('-'); t = it.lstrip('+-')
        d.circle(x + 8, y + i * gap - size * .35, 6, fill=GREEN if good else WARN, stroke='none')
        d.text(x + 24, y + i * gap, t, size, INK, 600)
