"""SOTORINO illustration library — consistent, simple technical line art (SVG).
All drawings are composed from primitives here so style stays uniform.
"""
import math, random, html

INK = '#2f3b2f'; LINE = '#354536'; GREEN = '#566b4f'; SOFT = '#eef1ea'; BG = '#fbfaf6'
SOIL = '#c7a774'; SOIL_D = '#a1814f'; SAND = '#eadbb4'; SAND_D = '#cdb98a'; GRAVEL = '#b4b3ac'; GRAVEL_D = '#8e8d86'
SHEET = '#3b3f3a'; TURF = '#7ea457'; TURF_D = '#5d8a3c'; CONC = '#d3d5cf'; CONC_D = '#a9aca4'
BRICK = '#c0714a'; BRICK_D = '#94522f'; WOOD = '#cfa067'; WOOD_D = '#9c7240'; MORTAR = '#ddd8cb'; WATER = '#8cbfd8'; WATER_D = '#4f8fb0'
WARN = '#9a3e2e'; GOLD = '#c89a32'; WHITE = '#ffffff'; GREY = '#8f928a'; METAL = '#9aa3a8'; METAL_D = '#6c757a'
FONT = "'Noto Sans CJK JP','Noto Sans JP',sans-serif"

SIZES = {'4:3': (960, 720), '16:9': (1280, 720), '3:2': (960, 640), '1:1': (800, 800)}


def esc(t): return html.escape(str(t), quote=True)


def tw(t, size):
    """approximate rendered text width (Noto Sans CJK)"""
    w = 0
    for ch in str(t):
        o = ord(ch)
        if o < 0x2000: w += 0.58 if ch not in ' .,:;' else 0.3
        elif ch in '（）「」、。・：' : w += 1.0
        else: w += 1.0
    return w * size


class D:
    """A drawing: collects SVG elements."""
    def __init__(self, ratio='4:3', bg=BG):
        self.W, self.H = SIZES[ratio]; self.el = []; self.defs = []; self.bg = bg; self.ratio = ratio
        self.rnd = random.Random(7)

    def add(self, s): self.el.append(s); return self

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" width="{self.W}" height="{self.H}" font-family="{FONT}">'
                f'<defs>{"".join(self.defs)}</defs><rect width="{self.W}" height="{self.H}" fill="{self.bg}"/>' + ''.join(self.el) + '</svg>')

    # ---------- basic shapes ----------
    def rect(self, x, y, w, h, fill='none', stroke=LINE, sw=2.5, rx=0, op=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"{d}/>')

    def line(self, x1, y1, x2, y2, stroke=LINE, sw=2.5, dash=None, cap='round'):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')

    def path(self, d, fill='none', stroke=LINE, sw=2.5, op=1, join='round', dash=None):
        dd = f' stroke-dasharray="{dash}"' if dash else ''
        return self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="{join}" stroke-linecap="round" opacity="{op}"{dd}/>')

    def circle(self, cx, cy, r, fill='none', stroke=LINE, sw=2.5, op=1):
        return self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>')

    def ellipse(self, cx, cy, rx, ry, fill='none', stroke=LINE, sw=2.5, op=1):
        return self.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>')

    def poly(self, pts, fill='none', stroke=LINE, sw=2.5, op=1):
        p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        return self.add(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" opacity="{op}"/>')

    def text(self, x, y, t, size=24, fill=INK, weight=700, anchor='start', ls=0):
        return self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{esc(t)}</text>')

    def mtext(self, x, y, lines, size=22, fill=INK, weight=500, anchor='start', lh=1.45):
        for i, t in enumerate(lines): self.text(x, y + i * size * lh, t, size, fill, weight, anchor)
        return self

    # ---------- annotation ----------
    def label(self, x, y, t, tx, ty, size=20, anchor=None, color=INK, dot=True):
        """leader line from point (x,y) to a boxed label whose anchor is (tx,ty)"""
        anchor = anchor or ('start' if tx >= x else 'end')
        w = tw(t, size) + 22; h = size + 16
        bx = tx if anchor == 'start' else tx - w if anchor == 'end' else tx - w / 2
        bx = max(8, min(self.W - w - 8, bx)); by = ty - h / 2
        # leader to nearest box edge point
        ex = min(max(x, bx), bx + w); ey = by + h if y > by + h else by if y < by else y
        self.line(x, y, ex, ey, stroke=color, sw=1.8)
        if dot: self.circle(x, y, 4.5, fill=color, stroke='none')
        self.rect(bx, by, w, h, fill=WHITE, stroke=color, sw=1.6, rx=7)
        return self.text(bx + w / 2, by + h / 2 + size * .36, t, size, color, 700, 'middle')

    def tag(self, x, y, t, fill=GREEN, color=WHITE, size=20, pad=14):
        w = tw(t, size) + pad * 2
        self.rect(x, y, w, size + 16, fill=fill, stroke='none', rx=(size + 16) / 2)
        self.text(x + w / 2, y + size + 3, t, size, color, 700, 'middle'); return w

    def dim_h(self, x1, x2, y, t, color=WARN, size=20, above=True):
        self.line(x1, y, x2, y, stroke=color, sw=2)
        for x in (x1, x2): self.line(x, y - 9, x, y + 9, stroke=color, sw=2)
        self.path(f'M{x1+12},{y-6} L{x1},{y} L{x1+12},{y+6}', stroke=color, sw=2)
        self.path(f'M{x2-12},{y-6} L{x2},{y} L{x2-12},{y+6}', stroke=color, sw=2)
        return self.text((x1 + x2) / 2, y - 12 if above else y + size + 8, t, size, color, 700, 'middle')

    def dim_v(self, x, y1, y2, t, color=WARN, size=20, right=True):
        self.line(x, y1, x, y2, stroke=color, sw=2)
        for y in (y1, y2): self.line(x - 9, y, x + 9, y, stroke=color, sw=2)
        self.path(f'M{x-6},{y1+12} L{x},{y1} L{x+6},{y1+12}', stroke=color, sw=2)
        self.path(f'M{x-6},{y2-12} L{x},{y2} L{x+6},{y2-12}', stroke=color, sw=2)
        return self.text(x + 14 if right else x - 14, (y1 + y2) / 2 + 7, t, size, color, 700, 'start' if right else 'end')

    def arrow(self, x1, y1, x2, y2, color=GREEN, sw=4, head=16):
        a = math.atan2(y2 - y1, x2 - x1)
        self.line(x1, y1, x2 - math.cos(a) * 4, y2 - math.sin(a) * 4, stroke=color, sw=sw)
        p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45)); p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
        return self.poly([(x2, y2), p1, p2], fill=color, stroke=color, sw=1)

    def curved_arrow(self, x1, y1, cx, cy, x2, y2, color=GREEN, sw=3.5):
        self.path(f'M{x1},{y1} Q{cx},{cy} {x2},{y2}', stroke=color, sw=sw)
        a = math.atan2(y2 - cy, x2 - cx); h = 15
        return self.poly([(x2, y2), (x2 - h * math.cos(a - 0.45), y2 - h * math.sin(a - 0.45)), (x2 - h * math.cos(a + 0.45), y2 - h * math.sin(a + 0.45))], fill=color, stroke=color, sw=1)

    def ok(self, x, y, r=22):
        self.circle(x, y, r, fill=GREEN, stroke='none'); return self.path(f'M{x-10},{y} L{x-3},{y+8} L{x+11},{y-8}', stroke=WHITE, sw=4)

    def ng(self, x, y, r=22):
        self.circle(x, y, r, fill=WARN, stroke='none'); self.line(x - 8, y - 8, x + 8, y + 8, stroke=WHITE, sw=4); return self.line(x + 8, y - 8, x - 8, y + 8, stroke=WHITE, sw=4)

    # ---------- header for step / panel ----------
    def step_header(self, n, title, sub=None):
        w = self.tag(36, 30, f'STEP {n}', fill=GREEN, size=22) or (tw(f'STEP {n}', 22) + 28)
        self.text(36 + w + 16, 61, title, 32, INK, 700)
        if sub: self.text(36, 104, sub, 20, '#4a4d46', 500)
        return self

    def header(self, title, sub=None, size=32):
        self.text(36, 60, title, size, INK, 700)
        if sub: self.text(36, 98, sub, 20, '#4a4d46', 500)
        return self

    def note(self, t, y=None, size=19):
        y = y or self.H - 26
        return self.text(36, y, t, size, '#6b6e66', 500)

    # ---------- ground cross-section ----------
    def soil(self, x, y, w, h, rough=False, speck=True):
        if rough:
            pts = [(x, y)]
            n = int(w / 28)
            for i in range(1, n + 1):
                pts.append((x + w * i / n, y + self.rnd.uniform(-9, 9)))
            pts += [(x + w, y + h), (x, y + h)]
            self.poly(pts, fill=SOIL, stroke=SOIL_D, sw=2)
        else:
            self.rect(x, y, w, h, fill=SOIL, stroke=SOIL_D, sw=2)
        if speck:
            for _ in range(int(w * h / 900)):
                px, py = x + self.rnd.uniform(6, w - 6), y + self.rnd.uniform(14, h - 6)
                self.circle(px, py, self.rnd.uniform(1.4, 3.2), fill=SOIL_D, stroke='none', op=.55)
        return self

    def compact_marks(self, x, y, w):
        for i in range(int(w / 34)):
            xx = x + 14 + i * 34
            self.line(xx, y + 10, xx + 14, y + 10, stroke=SOIL_D, sw=2)
        return self

    def weeds(self, x, y, n=6, spread=None, color=TURF_D):
        spread = spread or n * 60
        for i in range(n):
            cx = x + (i + .5) * spread / n + self.rnd.uniform(-10, 10)
            hgt = self.rnd.uniform(26, 46)
            self.path(f'M{cx},{y} q-10,-{hgt*.5} -16,-{hgt}', stroke=color, sw=3)
            self.path(f'M{cx},{y} q2,-{hgt*.6} 2,-{hgt*1.05}', stroke=color, sw=3)
            self.path(f'M{cx},{y} q10,-{hgt*.4} 18,-{hgt*.8}', stroke=color, sw=3)
            # roots
            self.path(f'M{cx},{y} q-6,14 -10,26 M{cx},{y} q4,16 8,24', stroke=SOIL_D, sw=2)
        return self

    def stones(self, x, y, n=4, spread=300):
        for i in range(n):
            cx = x + self.rnd.uniform(0, spread); r = self.rnd.uniform(7, 13)
            self.ellipse(cx, y - r * .5, r * 1.3, r * .8, fill=GRAVEL, stroke=GRAVEL_D)
        return self

    def sand(self, x, y, w, h):
        self.rect(x, y, w, h, fill=SAND, stroke=SAND_D, sw=2)
        for _ in range(int(w * h / 260)):
            self.circle(x + self.rnd.uniform(4, w - 4), y + self.rnd.uniform(3, h - 3), 1.3, fill=SAND_D, stroke='none', op=.8)
        return self

    def gravel_layer(self, x, y, w, h, color=GRAVEL, dark=GRAVEL_D, r=(6, 11), round_=True):
        self.rect(x, y, w, h, fill='#dcdbd4', stroke=dark, sw=2)
        rows = max(1, int(h / (r[1] * 1.4)))
        for row in range(rows):
            cx = x + self.rnd.uniform(4, 12)
            while cx < x + w - 6:
                rr = self.rnd.uniform(*r)
                cy = y + h - (row + .55) * (h / rows)
                if round_: self.ellipse(cx, cy, rr, rr * .75, fill=color, stroke=dark, sw=1.6)
                else: self.poly([(cx - rr, cy + rr * .4), (cx - rr * .3, cy - rr * .8), (cx + rr, cy - rr * .3), (cx + rr * .6, cy + rr * .7)], fill=color, stroke=dark, sw=1.6)
                cx += rr * 2 + self.rnd.uniform(1, 4)
        return self

    def sheet(self, x, y, w, t=7, color=SHEET):
        return self.rect(x, y - t, w, t, fill=color, stroke=color, sw=1)

    def pin(self, x, y, depth=40, color=METAL_D):
        """U-pin seen in section: head on surface, legs into ground"""
        self.path(f'M{x-9},{y+depth} L{x-9},{y-4} L{x+9},{y-4} L{x+9},{y+depth}', stroke=color, sw=4, join='miter')
        return self

    def turf(self, x, y, w, base=8, blade=26, dense=7, color=TURF, dark=TURF_D):
        self.rect(x, y - base, w, base, fill='#4b5d3e', stroke='#4b5d3e', sw=1)
        i = 0; cx = x + 3
        while cx < x + w - 2:
            hh = blade * self.rnd.uniform(.8, 1.08); lean = self.rnd.uniform(-5, 5)
            self.path(f'M{cx:.1f},{y-base} q{lean*.3:.1f},-{hh*.5:.1f} {lean:.1f},-{hh:.1f}', stroke=color if i % 3 else dark, sw=2.6)
            cx += dense; i += 1
        return self

    def tile_row(self, x, y, w, tile_w=90, h=16, gap=6, fill='#e2ddd2', stroke='#9e988a'):
        cx = x
        while cx + tile_w <= x + w + 1:
            self.rect(cx, y - h, tile_w, h, fill=fill, stroke=stroke, sw=2, rx=2)
            cx += tile_w + gap
        return self

    def brick_side(self, x, y, w=72, h=26, fill=BRICK, stroke=BRICK_D):
        return self.rect(x, y, w, h, fill=fill, stroke=stroke, sw=2, rx=2)

    # ---------- tools ----------
    def shovel(self, x, y, s=1.0, ang=-20):
        g = f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
        g += f'<rect x="-5" y="-210" width="10" height="160" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5" rx="4"/>'
        g += f'<path d="M-22,-224 h44 v14 h-44z" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5"/>'
        g += f'<path d="M-24,-52 h48 v28 q0,30 -24,40 q-24,-10 -24,-40z" fill="{METAL}" stroke="{METAL_D}" stroke-width="2.5"/></g>'
        return self.add(g)

    def rake(self, x, y, s=1.0, ang=-30):
        g = f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
        g += f'<rect x="-5" y="-230" width="10" height="200" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5" rx="4"/>'
        g += f'<rect x="-50" y="-34" width="100" height="10" fill="{METAL}" stroke="{METAL_D}" stroke-width="2.5"/>'
        for i in range(9): g += f'<line x1="{-46+i*11.5}" y1="-24" x2="{-46+i*11.5}" y2="-6" stroke="{METAL_D}" stroke-width="3" stroke-linecap="round"/>'
        return self.add(g + '</g>')

    def tamper(self, x, y, s=1.0):
        g = f'<g transform="translate({x},{y}) scale({s})">'
        g += f'<rect x="-6" y="-200" width="12" height="180" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5" rx="4"/>'
        g += f'<rect x="-30" y="-212" width="60" height="14" rx="6" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5"/>'
        g += f'<rect x="-42" y="-22" width="84" height="22" fill="{METAL}" stroke="{METAL_D}" stroke-width="2.5" rx="3"/>'
        g += '</g>'
        self.add(g)
        for k in (-1, 1):
            self.path(f'M{x+k*58},{y-60} v28 M{x+k*70},{y-48} v16', stroke=GREEN, sw=3)
        return self.arrow(x + 90, y - 150, x + 90, y - 90, color=GREEN, sw=3)

    def level(self, x, y, w=260):
        self.rect(x, y - 26, w, 26, fill='#f2d26b', stroke='#a8892a', sw=2.5, rx=4)
        self.rect(x + w / 2 - 34, y - 21, 68, 16, fill='#d9f0d0', stroke='#6d8a5a', sw=2, rx=8)
        self.circle(x + w / 2, y - 13, 5, fill='#7fb36a', stroke='none')
        self.line(x + w / 2 - 12, y - 21, x + w / 2 - 12, y - 5, stroke='#6d8a5a', sw=1.5)
        return self.line(x + w / 2 + 12, y - 21, x + w / 2 + 12, y - 5, stroke='#6d8a5a', sw=1.5)

    def cutter(self, x, y, ang=-30, s=1.0):
        g = f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
        g += f'<rect x="-70" y="-14" width="110" height="28" rx="8" fill="#e9b949" stroke="#a37d1c" stroke-width="2.5"/>'
        g += f'<path d="M40,-10 L86,-2 L40,10z" fill="#d7dde0" stroke="{METAL_D}" stroke-width="2.5"/></g>'
        return self.add(g)

    def hammer(self, x, y, ang=-35, s=1.0):
        g = f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
        g += f'<rect x="-6" y="-10" width="12" height="130" rx="4" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5"/>'
        g += f'<rect x="-34" y="-34" width="68" height="28" rx="4" fill="{METAL}" stroke="{METAL_D}" stroke-width="2.5"/></g>'
        return self.add(g)

    def brush(self, x, y, ang=-25, s=1.0):
        g = f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
        g += f'<rect x="-5" y="-210" width="10" height="190" rx="4" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5"/>'
        g += f'<rect x="-60" y="-26" width="120" height="20" rx="5" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5"/>'
        for i in range(14): g += f'<line x1="{-56+i*8.5}" y1="-6" x2="{-56+i*8.5}" y2="12" stroke="#5b4a33" stroke-width="2.5" stroke-linecap="round"/>'
        return self.add(g + '</g>')

    def trowel(self, x, y, ang=20, s=1.0):
        g = f'<g transform="translate({x},{y}) rotate({ang}) scale({s})">'
        g += f'<path d="M-50,0 L40,-18 L40,18 z" fill="{METAL}" stroke="{METAL_D}" stroke-width="2.5"/>'
        g += f'<rect x="40" y="-6" width="60" height="12" rx="5" fill="{WOOD}" stroke="{WOOD_D}" stroke-width="2.5"/></g>'
        return self.add(g)

    def water_can(self, x, y, s=1.0):
        g = f'<g transform="translate({x},{y}) scale({s})">'
        g += f'<path d="M-50,-60 h80 v60 h-80z" fill="#9fc3a8" stroke="#4f7a5c" stroke-width="2.5"/>'
        g += f'<path d="M30,-50 L90,-90 M88,-96 l14,10" stroke="#4f7a5c" stroke-width="5" fill="none" stroke-linecap="round"/>'
        g += f'<path d="M-50,-50 q-30,0 -30,24 q0,22 30,22" fill="none" stroke="#4f7a5c" stroke-width="5"/></g>'
        self.add(g)
        for i in range(5): self.line(x + 100 * s + i * 7, y - 80 * s + i * 4, x + 108 * s + i * 7, y - 40 * s + i * 6, stroke=WATER_D, sw=2, dash='4 6')
        return self

    def hose_spray(self, x, y, tx, ty):
        """nozzle at (x,y) spraying toward (tx,ty)"""
        self.path(f'M{x+10},{y} q50,10 80,-30', stroke='#4f7a5c', sw=7)
        self.rect(x - 6, y - 12, 26, 22, fill='#e9b949', stroke='#a37d1c', sw=2, rx=5)
        for i in range(7):
            self.line(x - 8, y, tx - 120 + i * 40, ty + (i % 2) * 6, stroke=WATER_D, sw=2, dash='5 7')
        return self

    def person_hand(self, x, y, ang=0):
        return self.add(f'<g transform="translate({x},{y}) rotate({ang})"><path d="M0,0 q18,-6 34,0 l26,0 q8,0 8,8 q0,8 -8,8 l-22,0 l0,10 q0,16 -18,18 q-22,2 -24,-20z" fill="#f2c9a5" stroke="#b5835c" stroke-width="2.5"/></g>')


def wrap(svg):
    return svg


def save(d, path):
    open(path, 'w').write(d.svg())
