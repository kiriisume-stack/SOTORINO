"""庭のトラブル（No.87〜99）— 原因の図解とビフォーアフターのイラスト（3:2・断面中心）。
本文に書かれた原因・対策だけを描く。"""
from scene import *

OUT = {}
def out(name, d, alt): OUT[name] = (d, alt)

X, W, T, B = 40, 880, 330, 470   # 断面の左・幅・地表・下端
CLAY = '#b39468'; CLAY_D = '#8a6f4a'; GOOD = '#d2b37f'


def base(title, sub, ba=None):
    d = D('3:2')
    if ba:
        w = d.tag(36, 30, ba, fill=WARN if ba == 'BEFORE' else GREEN, size=20)
        d.text(36 + w + 14, 58, title, 30, INK, 700)
    else:
        d.text(36, 60, title, 30, INK, 700)
    d.text(36, 98, sub, 19, '#4a4d46', 500)
    return d


def pbox(d, items, y=496, h=128):
    d.rect(30, y, 900, h, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12)
    points(d, 54, y + 38, items, 19, 35)


def num(d, x, y, n, color=WARN):
    d.circle(x, y, 16, fill=color, stroke=WHITE, sw=2.5); d.text(x, y + 7, str(n), 19, WHITE, 700, 'middle')


def callout(d, px, py, n, t, tx, ty, color=WARN):
    d.line(px, py, tx, ty, stroke=color, sw=1.8); d.circle(px, py, 4.5, fill=color, stroke='none')
    w = tw(t, 18) + 50; bx = max(8, min(d.W - w - 8, tx - w / 2))
    d.rect(bx, ty - 17, w, 34, fill=WHITE, stroke=color, sw=1.6, rx=8)
    num(d, bx + 18, ty, n, color); d.text(bx + 38, ty + 7, t, 18, INK, 700)


def clay(d, x=X, w=W, y=T, h=None):
    h = h or B - y
    d.rect(x, y, w, h, fill=CLAY, stroke=CLAY_D, sw=2)
    for i in range(int(h / 14)): d.line(x + 6, y + 10 + i * 14, x + w - 6, y + 10 + i * 14, stroke=CLAY_D, sw=1.2, dash='22 10')


def good_soil(d, x=X, w=W, y=T, h=None):
    h = h or B - y
    d.rect(x, y, w, h, fill=GOOD, stroke=SOIL_D, sw=2)
    for _ in range(int(w * h / 220)):
        d.circle(x + d.rnd.uniform(4, w - 4), y + d.rnd.uniform(4, h - 4), d.rnd.uniform(1.2, 2.6), fill=d.rnd.choice(['#efe2c0', '#6b5134', '#efe2c0']), stroke='none')


def puddle(d, x, w, y=T, depth=14):
    d.path(f'M{x},{y} Q{x+w/2},{y+depth*1.6} {x+w},{y} Z', fill=WATER, stroke=WATER_D, sw=2, op=.9)
    d.line(x - 4, y, x + w + 4, y, stroke=WATER_D, sw=2.5)


def rain(d, x, w, y=135, n=14):
    for i in range(n):
        xx = x + i * w / n + (i % 2) * 10
        d.line(xx, y + (i % 3) * 14, xx - 6, y + 22 + (i % 3) * 14, stroke=WATER_D, sw=2)


def drain(d, x, clogged=False, y=T):
    """集水桝（断面）。x は左端"""
    d.rect(x, y, 60, 90, fill='#c9ccc6', stroke=CONC_D, sw=2.5); d.rect(x + 8, y, 44, 82, fill='#e9ece6', stroke=CONC_D, sw=1.5)
    for i in range(5): d.line(x + 4 + i * 13, y - 6, x + 4 + i * 13, y, stroke=METAL_D, sw=3)
    d.line(x, y - 6, x + 60, y - 6, stroke=METAL_D, sw=3)
    d.rect(x + 60, y + 54, 60, 16, fill='#c9ccc6', stroke=CONC_D, sw=2)
    if clogged:
        for i in range(5): d.ellipse(x + 8 + i * 11, y - 10 - (i % 2) * 4, 9, 5, fill='#b98b3c', stroke='#7d5a22', sw=1.5)


def flow(d, x1, y1, x2, y2, ok=True):
    d.arrow(x1, y1, x2, y2, color=WATER_D if ok else WARN, sw=3, head=13)


def ankyo(d, x, w=110, y=T + 20):
    d.rect(x, y, w, B - y - 10, fill='#dcdbd4', stroke=GRAVEL_D, sw=2)
    d.gravel_layer(x, y, w, B - y - 10, r=(5, 8))
    cx, cy = x + w / 2, B - 50
    d.circle(cx, cy, 22, fill='#e9ece6', stroke=METAL_D, sw=3)
    for a in range(6):
        import math
        d.circle(cx + 14 * math.cos(a), cy + 14 * math.sin(a), 2.5, fill=METAL_D, stroke='none')


def leaves(d, x, w, y=T, n=10):
    for i in range(n):
        xx = x + d.rnd.uniform(0, w); d.ellipse(xx, y - 4, d.rnd.uniform(7, 11), 4, fill=d.rnd.choice(['#b98b3c', '#a3601e', '#c9a35a']), stroke='#7d5a22', sw=1.2)


def mold(d, x, w, y, n=26):
    for _ in range(n):
        d.circle(x + d.rnd.uniform(0, w), y - d.rnd.uniform(4, 22), d.rnd.uniform(2, 5), fill=d.rnd.choice(['#2f3a2f', '#3f4a3a', '#5b5f44']), stroke='none', op=.85)


def shade(d, x, w, y0=120):
    d.poly([(x, y0), (x + w, y0), (x + w + 120, T), (x, T)], fill='#5b6670', stroke='none', op=.18)


def wall(d, x, w=90, y0=120, label='建物（北側）'):
    d.rect(x, y0, w, T - y0, fill=WALL, stroke=LINE, sw=2.5); d.text(x + w / 2, y0 + 40, label, 16, INK, 700, 'middle')


def section_note(d, t='断面イメージ'):
    d.text(X + W, B + 20, t, 15, GREY, 500, 'end')


# ===================== 87 水はけ =====================
def mizuhake():
    s = 'niwa-mizuhake-warui-gen-in'
    d = base('水はけが悪くなる3つの原因', '土壌の質・地面の勾配・排水経路のいずれかに問題があるケースが多い')
    clay(d, X, 560); d.soil(X + 560, T, W - 560, B - T)
    rain(d, X + 60, 700); puddle(d, X + 120, 320); drain(d, X + 700, clogged=True)
    d.line(X, T - 1, X + 690, T - 1, stroke=LINE, sw=2.5)
    callout(d, X + 300, T + 70, 1, '粘土質の土は水を通しにくい', X + 220, 250 - 0 + 170)
    callout(d, X + 280, T - 2, 2, '水が流れる勾配がない', X + 300, 200)
    callout(d, X + 730, T - 12, 3, '排水口の詰まり・不足', X + 720, 220)
    section_note(d)
    out(f'{s}-01', d, '庭の水はけが悪くなる3つの原因の図解。粘土質の土、勾配がない地面、排水口の詰まりや不足')
    # BEFORE
    d = base('水がたまり、なかなか引かない', '粘土質の土・平らな地面・詰まった排水口', 'BEFORE')
    clay(d); rain(d, X + 60, 700); puddle(d, X + 80, 560); drain(d, X + 700, clogged=True)
    flow(d, X + 360, T - 40, X + 360, T + 30, ok=False); d.text(X + 380, T + 20, '水がしみ込みにくい', 17, WARN, 700)
    section_note(d)
    pbox(d, ['-粘土質の土で、水が地中にしみ込みにくい', '-勾配がなく、水が流れていかない', '-排水口が落ち葉などで詰まっている'])
    out(f'{s}-02', d, '水はけが悪い庭のビフォー断面図。粘土質の土と平らな地面で水たまりができ、排水口も詰まっている')
    # AFTER
    d = base('水が地中と排水口へ流れる', '土壌改良・勾配の調整・排水口の清掃や暗渠排水', 'AFTER')
    d.poly([(X, T - 30), (X + 690, T), (X + 690, B), (X, B)], fill=GOOD, stroke=SOIL_D, sw=2)
    for _ in range(260): d.circle(X + d.rnd.uniform(6, 680), d.rnd.uniform(T + 4, B - 6), d.rnd.uniform(1.2, 2.4), fill=d.rnd.choice(['#efe2c0', '#6b5134']), stroke='none')
    d.soil(X + 690, T, W - 690, B - T); drain(d, X + 700)
    ankyo(d, X + 380, 100, T - 5)
    flow(d, X + 80, T - 50, X + 300, T - 26); flow(d, X + 460, T - 20, X + 690, T - 6)
    flow(d, X + 200, T - 10, X + 200, T + 60); d.text(X + 214, T + 54, '水がしみ込む', 17, WATER_D, 700)
    d.label(X + 120, T - 26, '盛り土で緩やかな勾配', X + 150, 180, anchor='middle', color=GREEN)
    d.label(X + 300, T + 90, '砂・有機物を混ぜて土壌改良', X + 200, 240 + 170, anchor='middle', color=GREEN)
    d.label(X + 430, T + 40, '暗渠排水', X + 520, 200, anchor='middle', color=GREEN)
    d.label(X + 730, T - 8, '排水口を清掃', X + 760, 250, anchor='middle', color=GREEN)
    section_note(d)
    pbox(d, ['+土壌改良（砂・有機物を混ぜる）で水を通しやすく', '+盛り土で勾配をつけ、排水口へ流す', '+排水口・配管の清掃、暗渠排水の設置（専門工事が必要な場合あり）'])
    out(f'{s}-03', d, '水はけを改善した庭のアフター断面図。土壌改良・勾配の調整・暗渠排水・排水口の清掃で水が流れる')


# ===================== 88 水たまり =====================
def mizutamari():
    s = 'niwa-mizutamari-gen-in-taisaku'
    d = base('水たまりができる主な原因', '周囲より低い場所と、水を吸収しにくい場所で発生しやすい')
    d.soil(X, T, W, B - T)
    d.path(f'M{X+60},{T} Q{X+170},{T+40} {X+280},{T} Z', fill=SOIL, stroke='none'); d.path(f'M{X+60},{T} Q{X+170},{T+40} {X+280},{T}', stroke=LINE, sw=2.5)
    d.path(f'M{X+70},{T+2} Q{X+170},{T+34} {X+270},{T+2} Z', fill=WATER, stroke=WATER_D, sw=2)
    d.rect(X + 330, T, 220, 40, fill=CLAY, stroke=CLAY_D, sw=1.5); d.compact_marks(X + 330, T - 4, 220); puddle(d, X + 350, 180)
    d.sheet(X + 600, T, 280, 6); d.gravel_layer(X + 600, T - 34, 280, 28); d.rect(X + 600, T, 280, 30, fill=CLAY, stroke=CLAY_D, sw=1.5)
    for i in range(4): d.ellipse(X + 640 + i * 60, T - 38, 22, 5, fill=WATER, stroke=WATER_D, sw=1.5)
    callout(d, X + 170, T + 20, 1, '周囲より低く、水が集まる', X + 180, 180)
    callout(d, X + 440, T + 20, 2, '踏み固められた硬い土', X + 450, 240)
    callout(d, X + 740, T + 14, 3, '砂利・人工芝の下地処理が不十分', X + 690, 180)
    d.text(X + W, T - 60, '④ 排水口から遠い場所も、水が抜けにくい', 17, WARN, 700, 'end')
    section_note(d)
    out(f'{s}-01', d, '庭に水たまりができる主な原因の図解。低い場所、踏み固められた土、砂利や人工芝の下地処理不足')
    d = base('一部だけ水たまりが残る', '低い場所や硬い土に水が集まり、抜けにくい', 'BEFORE')
    d.soil(X, T, W, B - T); d.path(f'M{X+200},{T} Q{X+400},{T+60} {X+600},{T} Z', fill=CLAY, stroke='none')
    d.compact_marks(X + 220, T + 4, 360); d.path(f'M{X+210},{T+2} Q{X+400},{T+50} {X+590},{T+2} Z', fill=WATER, stroke=WATER_D, sw=2)
    d.line(X, T, X + W, T, stroke=LINE, sw=2.5)
    d.label(X + 400, T + 20, '低い・硬い場所に水がたまる', X + 400, 200, anchor='middle', color=WARN)
    section_note(d)
    pbox(d, ['-地面が周囲より低く、水が集まりやすい', '-土が踏み固められて、水を吸収しにくい', '-放置すると根腐れや虫（ボウフラなど）の原因にも'])
    out(f'{s}-02', d, '水たまりができている庭のビフォー断面図。低く硬い場所に水が集まっている')
    d = base('高さを調整し、水はけの良い土に', '盛り土・土の入れ替え・排水経路の確保', 'AFTER')
    d.soil(X, T, W, B - T); good_soil(d, X + 200, 400, T, 90)
    d.poly([(X + 200, T), (X + 600, T), (X + 600, T - 6), (X + 200, T - 6)], fill=GOOD, stroke='none'); d.line(X, T, X + W, T, stroke=LINE, sw=2.5)
    drain(d, X + 780); flow(d, X + 300, T - 30, X + 760, T - 14); flow(d, X + 400, T + 10, X + 400, T + 70)
    d.label(X + 400, T + 40, '硬い土を掘り起こし、水はけの良い土に入れ替え', X + 380, 200, anchor='middle', color=GREEN)
    d.label(X + 800, T - 8, '排水口への経路', X + 790, 250, anchor='middle', color=GREEN)
    section_note(d)
    pbox(d, ['+水たまりができる場所に土を盛って高さを調整', '+硬くなった土を掘り起こし、水はけの良い土に入れ替え', '+排水口への経路を設ける（専門工事が必要な場合あり）'])
    out(f'{s}-03', d, '水たまり対策後の庭のアフター断面図。土を入れ替えて高さを調整し、排水口へ流れる経路をつくる')


# ===================== 89 人工芝のカビ =====================
def turf_mold():
    s = 'jinkoshiba-kabi-gen-in-taisaku'
    def turf_section(d, wet=True, sheet_ok=False):
        if wet: clay(d)
        else: d.soil(X, T, W, B - T)
        d.sheet(X, T, W, 6); d.turf(X, T - 6, W, 8, 26, 6)
        if not sheet_ok:
            for i in range(10): d.circle(X + 60 + i * 85, T + 14 + (i % 3) * 8, 4, fill=WATER, stroke=WATER_D, sw=1.2)
    d = base('人工芝にカビが生えやすい原因', '芝そのものより、下地の水はけと湿気のこもりが主な原因')
    wall(d, X, 100); shade(d, X + 100, 200); turf_section(d); leaves(d, X + 420, 200, T - 30, 12); mold(d, X + 140, 240, T - 6)
    callout(d, X + 400, T + 30, 1, '下地の水はけが悪く湿気がたまる', X + 470, 430 - 0 + 10)
    callout(d, X + 520, T - 34, 2, '落ち葉やゴミがたまり湿ったまま', X + 620, 200)
    callout(d, X + 240, T - 40, 3, '日当たりが悪く乾きにくい', X + 330, 150)
    d.text(X + W, T - 66, '④ 防草シートの施工が不十分で湿気が抜けにくい', 16, WARN, 700, 'end')
    section_note(d)
    out(f'{s}-01', d, '人工芝にカビが生えやすい原因の図解。下地の水はけ不良、落ち葉の堆積、日当たりの悪さ')
    d = base('日陰で湿り、黒い斑点が出ている', '落ち葉がたまり、下地にも湿気がこもった状態', 'BEFORE')
    wall(d, X, 100); tree(d, X + 820, T, 230, 70); shade(d, X + 100, 200); turf_section(d); leaves(d, X + 200, 560, T - 30, 22); mold(d, X + 140, 420, T - 6, 50)
    d.label(X + 300, T - 18, 'カビ（黒っぽい斑点）', X + 360, 170, anchor='middle', color=WARN)
    section_note(d)
    pbox(d, ['-落ち葉やゴミが表面にたまり、湿った状態が続く', '-日当たり・風通しが悪く、乾きにくい', '-下地の水はけが悪く、湿気がこもる'])
    out(f'{s}-02', d, '人工芝にカビが発生しているビフォーのイラスト。日陰で落ち葉がたまり、黒い斑点が出ている')
    d = base('清掃と風通しの改善で乾きやすく', '落ち葉の除去・水洗い・剪定・排水対策の見直し', 'AFTER')
    wall(d, X, 100); tree(d, X + 820, T, 230, 46); turf_section(d, wet=False, sheet_ok=True)
    d.hose_spray(X + 360, 250, X + 520, T - 20)
    for i in range(3): d.arrow(X + 620 + i * 20, 180 + i * 30, X + 520 + i * 20, 220 + i * 30, color=WATER_D, sw=2, head=10)
    d.label(X + 800, T - 190, '剪定して風通しを良く', X + 700, 150, anchor='middle', color=GREEN)
    d.label(X + 520, T - 14, '表面を水で洗い流す', X + 300, 180, anchor='middle', color=GREEN)
    section_note(d)
    pbox(d, ['+落ち葉やゴミを定期的に取り除き、水で洗い流す', '+周囲の植栽を剪定して、風通しを良くする', '+下地の水はけに問題があれば、排水対策を見直す'])
    out(f'{s}-03', d, '人工芝のカビ対策後のアフターイラスト。落ち葉を取り除いて水で洗い、剪定で風通しを良くする')


# ===================== 91 天然芝が枯れる =====================
def lawn_dry():
    s = 'tennenshiba-kareru-gen-in-taisho'
    d = base('天然芝が枯れる主な原因', '水やり・病害虫・踏圧（ふみつけ）のいずれかが関わることが多い')
    for i, (t, sub) in enumerate((('水やりの問題', '不足で乾燥／過剰で根腐れ'), ('病害虫', '葉の変色・害虫の被害'), ('踏圧（ふみつけ）', '土が固くなり根が傷む'))):
        x = 40 + i * 300; d.rect(x, 140, 280, 340, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12)
        num(d, x + 30, 172, i + 1); d.text(x + 54, 180, t, 21, INK, 700)
        d.soil(x + 20, 360, 240, 90)
        if i == 0:
            d.turf(x + 20, 360, 120, 6, 26, 7, color='#c9b06a', dark='#a38a45')
            for k in range(5): d.line(x + 30 + k * 22, 380, x + 26 + k * 22, 396, stroke='#8a6a48', sw=1.6)
            d.turf(x + 140, 360, 120, 6, 26, 7, color='#9fae5d', dark='#77853f')
            d.rect(x + 140, 362, 120, 80, fill=WATER, stroke='none', op=.35)
            d.text(x + 80, 470 - 0, '乾燥', 16, WARN, 700, 'middle'); d.text(x + 200, 470, '水が多すぎ', 16, WARN, 700, 'middle')
            d.circle(x + 80, 260, 26, fill='#f6d36b', stroke='#c9a73a', sw=2); d.water_can(x + 210, 300, .5)
        elif i == 1:
            d.turf(x + 20, 360, 240, 6, 28, 7)
            for k in range(6): d.ellipse(x + 60 + k * 32, 340 - (k % 2) * 6, 12, 7, fill='#c9a35a', stroke='#8a6d16', sw=1.5, )
            d.ellipse(x + 160, 300, 16, 9, fill='#6b5a3a', stroke=LINE, sw=1.5); d.line(x + 150, 292, x + 140, 282, stroke=LINE, sw=1.5); d.line(x + 166, 292, x + 174, 282, stroke=LINE, sw=1.5)
            d.label(x + 92, 334, '葉が変色', x + 90, 240, anchor='middle', color=WARN)
        else:
            d.turf(x + 20, 360, 70, 6, 26, 7); d.turf(x + 190, 360, 70, 6, 26, 7)
            d.rect(x + 90, 352, 100, 8, fill='#b49a6a', stroke='none'); d.rect(x + 90, 360, 100, 40, fill=CLAY, stroke=CLAY_D, sw=1.5); d.compact_marks(x + 90, 358, 100)
            d.label(x + 140, 376, '固くなった土', x + 140, 240, anchor='middle', color=WARN)
        d.text(x + 140, 214, sub, 17, '#4a4d46', 600, 'middle')
    out(f'{s}-01', d, '天然芝が枯れる3つの原因の図解。水やりの不足や過剰、病害虫による変色、踏圧で固くなった土')
    d = base('よく歩く場所だけ芝が枯れている', '同じ場所を繰り返し歩き、土が固くなって根が傷んだ状態', 'BEFORE')
    G = 300; d.rect(40, 130, 880, 350, fill=LAWN, stroke=LAWN_D, sw=2, rx=10)
    d.path('M120,480 C260,380 360,330 520,300 S760,200 900,140 L920,140 L920,180 C780,230 640,330 540,350 S300,420 200,480 Z', fill='#c8b07a', stroke='#a38a45', sw=2)
    for i in range(7): d.ellipse(220 + i * 100, 420 - i * 42, 12, 18, fill='#7a6a52', stroke='none', op=.5)
    d.label(560, 330, '人が通る動線が枯れている', 700, 420, anchor='middle', color=WARN)
    d.text(910, 470, '上から見たイメージ', 15, GREY, 500, 'end')
    pbox(d, ['-同じ場所を繰り返し歩き、土が固くなっている', '-根が傷み、芝が部分的に枯れている', '-水やり不足や病害虫が重なると、さらに広がることも'])
    out(f'{s}-02', d, '天然芝が通り道だけ枯れているビフォーのイラスト。踏圧で土が固くなっている')
    d = base('敷石で動線を分け、芝を守る', '踏圧を分散させ、水やり・芝刈りも適切に管理', 'AFTER')
    d.rect(40, 130, 880, 350, fill=LAWN, stroke=LAWN_D, sw=2, rx=10)
    for i in range(8): d.rect(150 + i * 96, 410 - i * 36, 70, 44, fill='#d3d0c6', stroke='#8f8b80', sw=2, rx=12)
    d.label(342, 362, '敷石で動線を分ける', 260, 200, anchor='middle', color=GREEN)
    d.text(910, 470, '上から見たイメージ', 15, GREY, 500, 'end')
    pbox(d, ['+人の往来が多い場所に敷石を設置し、踏圧を分散', '+季節に応じた適切な水やりを行う', '+変色や異常は早めに対処し、芝刈りの頻度・高さを管理'])
    out(f'{s}-03', d, '天然芝の対策後のアフターイラスト。通り道に敷石を置いて踏圧を分散させ、芝が回復している')


# ===================== 92 フェンスの傾き =====================
def fence_tilt():
    s = 'fence-katamuku-gen-in-shuuri'
    def post(d, x, ang=0, base_ok=True, deep=60):
        import math
        a = math.radians(ang); L = 210
        x2 = x + math.sin(a) * L; y2 = T - math.cos(a) * L
        d.line(x, T + deep - 10, x2, y2, stroke=METAL_D, sw=14, cap='butt')
        return x2, y2
    d = base('フェンスが傾く主な原因', 'フェンス本体より、支柱を支える基礎の劣化・不足が原因のことが多い')
    d.soil(X, T, W, B - T, rough=False)
    d.rect(X + 260, T, 120, 50, fill='#c9ccc6', stroke=CONC_D, sw=2)
    for k in range(3): d.path(f'M{X+280+k*30},{T+4} l8,16 l-6,12 l10,16', stroke='#5f6467', sw=2)
    x2, y2 = post(d, X + 320, 12, deep=40)
    for i in range(6): d.line(X + 320 + (x2 - X - 320) * (i + 1) / 7 - 120, T - 30 - i * 30, X + 320 + (x2 - X - 320) * (i + 1) / 7 + 120, T - 30 - i * 30 + 10, stroke='#6a6e70', sw=8)
    for i in range(3): d.arrow(X + 40, 180 + i * 50, X + 180, 190 + i * 50, color=WATER_D, sw=3, head=12)
    d.text(X + 30, 165, '強風・積雪', 17, WATER_D, 700)
    d.rect(X + 560, T, 120, 30, fill='#c9ccc6', stroke=CONC_D, sw=2); d.line(X + 620, T + 20, X + 620, T - 200, stroke=METAL_D, sw=14, cap='butt')
    d.rect(X + 560, T + 30, 120, 110, fill='#d9c7a3', stroke=SOIL_D, sw=1.5, dash='6 4'); d.arrow(X + 700, T - 10, X + 700, T + 40, color=WARN, sw=3, head=12)
    callout(d, X + 300, T + 30, 1, '基礎（モルタル）の劣化', X + 260, 430 + 10)
    callout(d, X + 360, T + 50, 2, '基礎の深さ・量が不十分', X + 520, 400)
    callout(d, X + 120, 240, 3, '想定以上の負荷', X + 100, 290)
    callout(d, X + 640, T + 80, 4, '軟弱な地盤で支柱が沈む', X + 700, 440)
    section_note(d)
    out(f'{s}-01', d, 'フェンスが傾く主な原因の図解。基礎の劣化、基礎の深さ不足、強風や積雪の負荷、軟弱な地盤')
    d = base('支柱が傾き、基礎にひびが入っている', '支柱を支える基礎が劣化・不足した状態', 'BEFORE')
    d.soil(X, T, W, B - T); d.rect(X + 380, T, 120, 40, fill='#c9ccc6', stroke=CONC_D, sw=2)
    for k in range(3): d.path(f'M{X+400+k*30},{T+4} l8,14 l-6,10 l10,10', stroke='#5f6467', sw=2)
    x2, y2 = post(d, X + 440, 14, deep=30)
    for i in range(6): d.line(X + 440 + (x2 - X - 440) * (i + 1) / 7 - 150, T - 30 - i * 30, X + 440 + (x2 - X - 440) * (i + 1) / 7 + 150, T - 30 - i * 30 + 12, stroke='#6a6e70', sw=8)
    d.line(X + 440, T - 210, X + 440, T, stroke=GREY, sw=2, dash='8 6'); d.text(X + 300, T - 196, '本来の位置', 15, GREY, 600)
    d.label(X + 470, T + 18, '基礎のひび割れ・浅い基礎', X + 650, 440, anchor='middle', color=WARN)
    section_note(d)
    pbox(d, ['-支柱が傾き、フェンス全体が倒れかけている', '-基礎（モルタル）が劣化し、ひびが入っている', '-基礎が浅く、支柱を支えきれていない'], y=500, h=124)
    out(f'{s}-02', d, 'フェンスが傾いているビフォーの断面イラスト。基礎にひびが入り、支柱が傾いている')
    d = base('基礎から作り直し、支柱をまっすぐに', '傾きが大きい場合は、支柱を抜いて基礎から作り直す', 'AFTER')
    d.soil(X, T, W, B - T); d.rect(X + 370, T, 140, 110, fill='#c9ccc6', stroke=CONC_D, sw=2)
    d.line(X + 440, T + 90, X + 440, T - 200, stroke=METAL_D, sw=14, cap='butt')
    for i in range(6): d.line(X + 290, T - 30 - i * 30, X + 590, T - 30 - i * 30, stroke='#6a6e70', sw=8)
    d.level(X + 600, T - 120, 120); d.text(X + 660, T - 160, '垂直を確認', 16, GREEN, 700, 'middle')
    d.dim_v(X + 540, T, T + 110, '', right=True); d.label(X + 520, T + 70, '十分な深さ・量の基礎', X + 720, 430, anchor='middle', color=GREEN)
    section_note(d)
    pbox(d, ['+軽度の傾き：支柱まわりを補強（モルタルの追加など）', '+傾きが大きい：支柱を一度抜き、基礎から作り直す', '+地盤に問題がある場合は、地盤改良を含めて専門業者に相談'], y=500, h=124)
    out(f'{s}-03', d, 'フェンスの傾きを修理したアフターの断面イラスト。十分な深さの基礎で支柱を垂直に固定')


# ===================== 94 苔 =====================
def koke():
    s = 'niwa-koke-gen-in-jokyo'
    def moss(d, x, w):
        for _ in range(int(w / 6)):
            xx = x + d.rnd.uniform(0, w); d.ellipse(xx, T - 3, d.rnd.uniform(6, 12), d.rnd.uniform(3, 6), fill=d.rnd.choice(['#6f8f3e', '#5d7d34', '#86a24c']), stroke='none')
    d = base('日陰で湿った地面に苔が広がる', '建物の北側など、日当たり・水はけ・風通しが悪い場所', 'BEFORE')
    wall(d, X, 110); shade(d, X + 110, 280); tree(d, X + 560, T, 190, 56); hedge(d, X + 640, T, 220, 120)
    clay(d, X + 110, W - 110); moss(d, X + 120, 440); d.rect(X + 300, T - 8, 160, 8, fill='#cfcbbf', stroke='#8f8b80', sw=1.5); moss(d, X + 300, 160)
    for i in range(8): d.circle(X + 140 + i * 50, T + 16, 3.5, fill=WATER, stroke=WATER_D, sw=1)
    d.label(X + 260, T - 4, '苔', X + 240, 200, anchor='middle', color=WARN)
    d.label(X + 700, T - 80, '植栽が密集し風が通らない', X + 650, 150, anchor='middle', color=WARN)
    section_note(d)
    pbox(d, ['-建物の北側など、日当たりが少ない', '-水はけが悪く、地面が常に湿っている', '-風通しが悪く、湿気がこもりやすい'])
    out(f'{s}-01', d, '庭に苔が生えているビフォーのイラスト。建物の北側の日陰で、湿った地面に苔が広がる')
    d = base('苔を除去し、生えにくい環境に', 'こすり落とす・除去剤・高圧洗浄と、環境の改善', 'AFTER')
    wall(d, X, 110); tree(d, X + 560, T, 190, 44); hedge(d, X + 650, T, 200, 70)
    d.soil(X + 110, T, W - 110, B - T); d.sheet(X + 110, T, 330, 6); d.gravel_layer(X + 110, T - 40, 330, 34)
    d.rect(X + 460, T - 8, 160, 8, fill='#cfcbbf', stroke='#8f8b80', sw=1.5); d.brush(X + 540, T - 12, -20, .7)
    for i in range(3): d.arrow(X + 860 - i * 10, 170 + i * 30, X + 760 - i * 10, 200 + i * 30, color=WATER_D, sw=2, head=10)
    d.label(X + 240, T - 30, '苔が生えにくい砂利に', X + 250, 200, anchor='middle', color=GREEN)
    d.label(X + 560, T - 150, '剪定で日当たり・風通しを改善', X + 640, 150, anchor='middle', color=GREEN)
    d.label(X + 500, T - 8, 'デッキブラシでこする', X + 470, 260, anchor='middle', color=GREEN)
    section_note(d)
    pbox(d, ['+デッキブラシでこすり落とす・専用の除去剤・高圧洗浄（素材に注意）', '+植栽を剪定し、日当たりと風通しを改善', '+水はけを改善し、苔が生えやすい場所は砂利などを検討'])
    out(f'{s}-02', d, '苔を除去したアフターのイラスト。デッキブラシで除去し、剪定と砂利敷きで再発を防ぐ')


# ===================== 95 虫 =====================
def mushi():
    s = 'niwa-mushi-hassei-gen-in-taisaku'
    def bugs(d, x, y, n=10, spread=200):
        for _ in range(n):
            bx, by = x + d.rnd.uniform(0, spread), y + d.rnd.uniform(0, 120)
            d.ellipse(bx, by, 4, 2.5, fill='#3f3f3a', stroke='none'); d.line(bx - 6, by - 4, bx - 1, by - 1, stroke='#3f3f3a', sw=1.2); d.line(bx + 6, by - 4, bx + 1, by - 1, stroke='#3f3f3a', sw=1.2)
    d = base('虫が集まりやすい庭', '湿気・落ち葉やゴミ・水たまりが虫を引き寄せる', 'BEFORE')
    d.rect(0, 120, 960, T - 120, fill=SKY, stroke='none'); ground(d, T, fill=SOIL)
    hedge(d, X + 20, T, 260, 130); tree(d, X + 180, T, 180, 50); leaves(d, X + 300, 220, T, 26); puddle(d, X + 560, 160)
    d.rect(X + 780, T - 80, 70, 80, fill='#7d8a78', stroke=LINE, sw=2, rx=6); d.ellipse(X + 815, T - 84, 40, 8, fill='#cfcbbf', stroke=LINE, sw=1.5)
    for i in range(4): d.ellipse(X + 790 + i * 16, T - 4, 7, 4, fill='#c9a35a', stroke='#8a6d16', sw=1)
    bugs(d, X + 60, 170, 14); bugs(d, X + 320, 220, 8, 160); bugs(d, X + 560, 210, 8, 160); bugs(d, X + 760, 170, 8, 120)
    d.label(X + 150, T - 100, '密集した植栽（風通しが悪い）', X + 200, 140, anchor='middle', color=WARN)
    d.label(X + 410, T - 4, '落ち葉・ゴミ', X + 420, 260, anchor='middle', color=WARN)
    d.label(X + 640, T + 6, '水たまり', X + 640, 400, anchor='middle', color=WARN)
    d.label(X + 815, T - 40, '生ゴミの放置', X + 800, 400, anchor='middle', color=WARN)
    pbox(d, ['-落ち葉やゴミ、生ゴミがたまっている', '-水はけが悪く、水たまりができる', '-植栽が密集し、風通しが悪い'])
    out(f'{s}-01', d, '虫が発生しやすい庭のビフォーのイラスト。密集した植栽、落ち葉、水たまり、生ゴミに虫が集まる')
    d = base('清掃と水はけ改善で、虫が発生しにくく', '落ち葉の清掃・水たまりの解消・剪定・ゴミ置き場の清潔', 'AFTER')
    d.rect(0, 120, 960, T - 120, fill=SKY, stroke='none'); ground(d, T, fill=SOIL)
    hedge(d, X + 20, T, 200, 90); tree(d, X + 180, T, 180, 40)
    d.rect(X + 780, T - 80, 70, 80, fill='#7d8a78', stroke=LINE, sw=2, rx=6); d.rect(X + 774, T - 90, 82, 12, fill='#5d6a58', stroke=LINE, sw=2, rx=4)
    d.rake(X + 420, T - 2, .8, -25)
    for i in range(3): d.arrow(X + 330, 170 + i * 30, X + 180, 190 + i * 30, color=WATER_D, sw=2, head=10)
    d.label(X + 180, T - 170, '剪定で風通しを良く', X + 200, 140, anchor='middle', color=GREEN)
    d.label(X + 420, T - 6, '落ち葉を定期的に清掃', X + 460, 260, anchor='middle', color=GREEN)
    d.label(X + 640, T - 2, '水たまりをなくす', X + 640, 400, anchor='middle', color=GREEN)
    d.label(X + 815, T - 84, 'ふた付きで清潔に', X + 800, 230, anchor='middle', color=GREEN)
    pbox(d, ['+落ち葉やゴミを定期的に清掃する', '+水はけを改善し、水たまりをなくす', '+植栽を剪定して風通しを良くし、ゴミ置き場を清潔に保つ'])
    out(f'{s}-02', d, '虫対策後の庭のアフターのイラスト。落ち葉の清掃、剪定、水たまりの解消、ふた付きのゴミ箱')


# ===================== 97 コンクリートのひび割れ =====================
def crack():
    s = 'concrete-hibiware-gen-in-taisho'
    for k in range(2):
        d = base(('細いひび割れが入っている', '補修材で充填して補修')[k], ('乾燥収縮による軽微なひび割れの例', '軽微なひび割れは、専用の補修材で充填する')[k], ('BEFORE', 'AFTER')[k])
        d.rect(60, 140, 420, 300, fill=CONC, stroke=CONC_D, sw=2, rx=4)
        p = 'M200,140 l18,50 l-12,40 l26,60 l-8,50 l20,60 l-6,40'
        d.path(p, stroke='#5f6467' if k == 0 else '#9aa09a', sw=3 if k == 0 else 6)
        if k: d.path(p, stroke='#b9bdb6', sw=3)
        d.text(270, 466, '上から見たイメージ', 15, GREY, 500, 'middle')
        # 断面
        sx, sy = 540, 260; d.rect(sx, sy, 360, 100, fill=CONC, stroke=CONC_D, sw=2); d.gravel_layer(sx, sy + 100, 360, 40, r=(5, 8), round_=False)
        d.path(f'M{sx+180},{sy} l-6,24 l8,22 l-4,20', stroke='#5f6467', sw=3)
        if k: d.poly([(sx + 172, sy), (sx + 188, sy), (sx + 182, sy + 30), (sx + 176, sy + 30)], fill='#9aa09a', stroke=LINE, sw=1.5)
        d.label(sx + 178, sy + 10, ('表面のひび割れ', '補修材で充填')[k], sx + 180, 200, anchor='middle', color=(WARN, GREEN)[k])
        d.text(sx + 180, sy + 170, '断面イメージ', 15, GREY, 500, 'middle')
        if k: d.trowel(380, 300, 20, .8)
        pbox(d, (['-乾燥収縮によるひび割れは、強度への影響が少ないことが多い', '-幅が広い・段差がある場合は、構造的な問題の可能性', '-構造的な問題が疑われる場合は、専門業者に調査を依頼'],
                 ['+軽微なひび割れ：専用の補修材で充填する', '+構造的な問題が疑われる場合は、専門業者が下地から補修', '+ひびの幅や段差の有無を確認してから判断する'])[k])
        out(f'{s}-{k+1:02d}', d, ('コンクリートの細いひび割れのビフォーのイラスト（上から見た図と断面）', 'コンクリートのひび割れを補修材で充填したアフターのイラスト')[k])


# ===================== 98 砂利の庭の雑草 =====================
def jari_weeds():
    s = 'jari-niwa-zassou-gen-in-taisaku'
    d = base('砂利の庭に雑草が生える主な原因', '最大の要因は、砂利の下に敷いた防草シートの施工状態')
    d.soil(X, T, W, B - T)
    d.sheet(X, T, 200, 6); d.sheet(X + 210, T, 230, 6); d.sheet(X + 460, T, 150, 6); d.sheet(X + 650, T, 230, 6)
    d.gravel_layer(X, T - 46, 600, 40); d.gravel_layer(X + 600, T - 24, 280, 18)
    d.rect(X + 600, T - 6, 50, 6, fill=SOIL, stroke='none'); d.rect(X + 440, T - 6, 20, 6, fill=SOIL, stroke='none')
    d.weeds(X + 192, T - 46, 1, 30); d.weeds(X + 440, T - 46, 1, 20); d.weeds(X + 615, T - 24, 1, 30)
    d.rect(X + 300, T - 54, 120, 8, fill=SOIL_D, stroke='none', op=.8); d.weeds(X + 340, T - 54, 2, 60)
    callout(d, X + 205, T - 4, 1, 'シートの重ね幅が不足', X + 160, 410 + 20)
    callout(d, X + 450, T - 4, 2, 'ピンの間隔が広くずれた', X + 450, 455)
    callout(d, X + 625, T - 20, 3, '砂利が薄くシートが露出', X + 740, 430)
    callout(d, X + 360, T - 58, 4, '砂利の上に積もった土で発芽', X + 330, 200)
    d.text(X + W, 170, '⑤ 経年でシートが劣化し、破れることも', 16, WARN, 700, 'end')
    section_note(d)
    out(f'{s}-01', d, '砂利の庭に雑草が生える原因の図解。防草シートの重ね幅不足、ずれ、砂利の薄さ、砂利の上に積もった土')
    d = base('砂利のすき間から雑草が生えている', '防草シートの重ね不足・破れ・ずれから雑草が出ている', 'BEFORE')
    d.soil(X, T, W, B - T); d.sheet(X, T, 380, 6); d.sheet(X + 420, T, 460, 6); d.rect(X + 380, T - 6, 40, 6, fill=SOIL, stroke='none')
    d.gravel_layer(X, T - 30, W, 24)
    d.weeds(X + 360, T - 30, 3, 80); d.weeds(X + 640, T - 30, 2, 60); d.rect(X + 620, T - 36, 120, 6, fill=SOIL_D, stroke='none', op=.8)
    d.label(X + 400, T - 4, 'シートのすき間', X + 400, 430 + 10, anchor='middle', color=WARN)
    d.label(X + 680, T - 34, '積もった土', X + 760, 200, anchor='middle', color=WARN)
    section_note(d)
    pbox(d, ['-シートの重ね部分が不足し、すき間から雑草が出る', '-砂利が薄く、シートが露出・劣化している', '-砂利の上に積もった土やゴミで、種が発芽している'])
    out(f'{s}-02', d, '砂利の庭に雑草が生えているビフォーの断面図。シートのすき間や積もった土から雑草が出ている')
    d = base('シートを補修し、砂利の厚みを確保', 'シートの状態を確認・補修し、積もった土やゴミを除去', 'AFTER')
    d.soil(X, T, W, B - T); d.sheet(X, T, 470, 6); d.rect(X + 380, T - 13, 300, 7, fill='#4a4f49', stroke=SHEET, sw=1); d.sheet(X + 400, T, 480, 6)
    for px in (X + 100, X + 300, X + 520, X + 720): d.pin(px, T - 6, 30)
    d.gravel_layer(X, T - 56, W, 43)
    d.dim_h(X + 380, X + 680, T + 50, '十分な重ね幅', above=False, color=GREEN)
    d.dim_v(X + W - 30, T - 56, T - 13, '', right=False, color=GREEN); d.label(X + W - 30, T - 34, '十分な砂利の厚み', X + 720, 200, anchor='middle', color=GREEN)
    section_note(d)
    pbox(d, ['+砂利をめくってシートの状態を確認し、破れ・ずれを補修・交換', '+砂利の厚みを見直し、十分な厚みを確保', '+砂利の上に積もった土やゴミを定期的に除去'])
    out(f'{s}-03', d, '砂利の庭の雑草対策後のアフター断面図。防草シートを十分に重ねてピンで固定し、砂利の厚みを確保')


# ===================== 99 ぬかるみ =====================
def nukarumi():
    s = 'niwa-tsuchi-nukarumu-gen-in-kaizen'
    d = base('庭の土がぬかるむ主な原因', '水はけの悪さ（排水不良）と、水を含みやすい土質の組み合わせ')
    clay(d); rain(d, X + 80, 640); drain(d, X + 760, clogged=True)
    d.line(X, T, X + 750, T, stroke=LINE, sw=2.5)
    for i in range(6): d.ellipse(X + 160 + i * 70, T - 2, 18, 6, fill='#8a6f4a', stroke='none', op=.7)
    d.compact_marks(X + 140, T + 2, 440)
    callout(d, X + 120, T + 80, 1, '粘土質で水を吸収しにくい', X + 180, 445)
    callout(d, X + 600, T - 2, 2, '勾配がなく水がたまる', X + 600, 230)
    callout(d, X + 780, T - 12, 3, '排水経路の不足・詰まり', X + 760, 180)
    callout(d, X + 300, T + 6, 4, '踏み固められて水を通さない', X + 300, 210)
    section_note(d)
    out(f'{s}-01', d, '庭の土がぬかるむ原因の図解。粘土質の土、勾配がない地面、排水経路の不足、踏み固められた土')
    d = base('雨のあと、土がぬかるんで歩きにくい', '水を含みやすい土に、雨水がたまったまま', 'BEFORE')
    clay(d); puddle(d, X + 100, 260, depth=10); puddle(d, X + 480, 200, depth=10)
    for i in range(7): d.ellipse(X + 120 + i * 100, T - 2, 20, 7, fill='#6b5134', stroke='none', op=.7)
    person(d, X + 420, T, .9)
    d.label(X + 600, T - 4, 'ぬかるみ・水たまり', X + 700, 220, anchor='middle', color=WARN)
    section_note(d)
    pbox(d, ['-粘土質の土が水を吸収しにくい', '-勾配がなく、排水経路も不足している', '-歩くたびに土が固まり、さらに水を通しにくくなる'])
    out(f'{s}-02', d, '雨のあとにぬかるんだ庭のビフォーのイラスト。粘土質の土に水がたまり歩きにくい')
    d = base('土壌改良と歩行面の確保で、ぬかるみにくく', '土壌改良・勾配・砂利や敷石・排水経路の見直し', 'AFTER')
    d.poly([(X, T - 24), (X + 760, T), (X + 760, B), (X, B)], fill=GOOD, stroke=SOIL_D, sw=2)
    for _ in range(240): d.circle(X + d.rnd.uniform(6, 750), d.rnd.uniform(T + 4, B - 6), d.rnd.uniform(1.2, 2.4), fill=d.rnd.choice(['#efe2c0', '#6b5134']), stroke='none')
    drain(d, X + 770); ankyo(d, X + 560, 90, T - 4)
    for i in range(4): d.rect(X + 80 + i * 110, T - 22 + i * 3.2 - 12, 80, 14, fill='#d3d0c6', stroke='#8f8b80', sw=2, rx=5)
    flow(d, X + 60, T - 60, X + 520, T - 40); flow(d, X + 680, T - 12, X + 760, T - 6)
    d.label(X + 240, T - 22, '敷石で歩行面を確保', X + 230, 200, anchor='middle', color=GREEN)
    d.label(X + 300, T + 90, '砂・有機物を混ぜて土壌改良', X + 240, 440, anchor='middle', color=GREEN)
    d.label(X + 605, T + 50, '暗渠排水', X + 640, 200, anchor='middle', color=GREEN)
    section_note(d)
    pbox(d, ['+土壌改良（砂や有機物を混ぜ込む）で水はけを改善', '+盛り土で勾配をつけ、水が流れる経路をつくる', '+砂利や敷石で歩行面を確保し、必要に応じて暗渠排水を検討'])
    out(f'{s}-03', d, 'ぬかるみを改善したアフターの断面図。土壌改良、勾配、敷石、暗渠排水で水が流れる')


if __name__ == '__main__':
    import sys, os, json
    for f in (mizuhake, mizutamari, turf_mold, lawn_dry, fence_tilt, koke, mushi, crack, jari_weeds, nukarumi): f()
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
