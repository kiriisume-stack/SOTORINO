"""冬の庭アウトドア：商品カード用のイメージイラスト（1:1）。特定ブランドの形やロゴは描かない一般的な形。"""
from scene import *

OUT = {}
def out(n, d, a): OUT[n] = (d, a)

BGC = '#f3efe6'


def base():
    d = D('1:1', bg=BGC)
    d.ellipse(400, 640, 260, 34, fill='#e3ddcf', stroke='none')
    return d


def g1():  # 焚き火台（逆四角錐）
    d = base()
    d.poly([(200, 330), (600, 330), (440, 520), (360, 520)], fill='#c9cdd0', stroke=LINE, sw=4)
    d.poly([(200, 330), (600, 330), (560, 300), (240, 300)], fill='#e3e6e8', stroke=LINE, sw=4)
    for x, y in ((330, 560), (470, 560)): d.line(400, 520, x, 630, stroke=LINE, sw=8)
    for i in range(4): d.rect(300 + i * 50, 270 - (i % 2) * 14, 120, 26, fill='#a5764a', stroke=LINE, sw=3, rx=10)
    d.path('M360,280 q-30,-60 10,-110 q-5,50 30,60 q10,-50 40,-80 q10,70 -10,130z', fill='#f2a33a', stroke='#b86a1e', sw=3)
    out('goods-winter-01', d, '焚き火台のイメージイラスト')


def g2():  # ポータブル電源
    d = base()
    d.rect(200, 280, 400, 330, fill='#e9e5dc', stroke=LINE, sw=4, rx=30)
    d.rect(250, 230, 300, 60, fill='#d4cfc3', stroke=LINE, sw=4, rx=24); d.rect(290, 250, 220, 20, fill=BGC, stroke=LINE, sw=3, rx=10)
    d.rect(240, 330, 140, 90, fill='#1f2a24', stroke=LINE, sw=3, rx=8); d.text(310, 388, '85%', 34, '#9fe0a8', 700, 'middle')
    for i in range(3): d.rect(410 + i * 52, 340, 36, 50, fill='#3d4448', stroke=LINE, sw=2, rx=6)
    for i in range(2): d.circle(430 + i * 70, 460, 22, fill='#3d4448', stroke=LINE, sw=2)
    d.rect(240, 520, 320, 50, fill='#c7a774', stroke=LINE, sw=3, rx=10)
    out('goods-winter-02', d, 'ポータブル電源のイメージイラスト')


def g3():  # 電気ブランケット
    d = base()
    d.path('M180,300 q220,-60 440,0 l-30,300 q-190,40 -380,0z', fill='#c8b49a', stroke=LINE, sw=4)
    for i in range(5): d.path(f'M{205+i*80},300 q10,140 -10,290', stroke='#b59f82', sw=10)
    for i in range(3): d.path(f'M{300+i*90},430 q10,-14 0,-28 q-10,-14 0,-28', stroke=WARN, sw=4)
    d.rect(560, 470, 70, 40, fill='#3d4448', stroke=LINE, sw=3, rx=8); d.path('M630,490 q60,0 60,60 v40', stroke='#3d4448', sw=6)
    out('goods-winter-03', d, '電気ブランケット（ひざ掛けタイプ）のイメージイラスト')


def g4():  # ランタン
    d = base()
    d.circle(400, 400, 190, fill='#fff3c4', stroke='none', op=.7)
    d.rect(330, 300, 140, 230, fill='#f7e6a5', stroke=LINE, sw=4, rx=50)
    d.rect(330, 500, 140, 80, fill='#3d4448', stroke=LINE, sw=4, rx=16)
    d.path('M360,300 q40,-70 80,0', stroke=LINE, sw=6)
    d.circle(400, 410, 30, fill='#fffbe6', stroke='#e2b93b', sw=3)
    out('goods-winter-04', d, 'LEDランタンのイメージイラスト')


def g5():  # アウトドアチェア
    d = base()
    for (x1, y1, x2, y2) in ((250, 620, 520, 360), (550, 620, 280, 360), (300, 620, 330, 300), (500, 620, 470, 300)):
        d.line(x1, y1, x2, y2, stroke='#3d4448', sw=10)
    d.path('M260,330 q140,90 280,0 l-20,160 q-120,50 -240,0z', fill='#566b4f', stroke=LINE, sw=4)
    d.path('M300,300 q100,40 200,0 l0,-140 q-100,30 -200,0z', fill='#6f8566', stroke=LINE, sw=4)
    out('goods-winter-05', d, '折りたたみアウトドアチェアのイメージイラスト')


def g6():  # 難燃ブランケット
    d = base()
    d.path('M170,360 q230,-80 460,0 l-20,230 q-210,50 -420,0z', fill='#a8b39a', stroke=LINE, sw=4)
    d.path('M170,360 q230,-80 460,0 l-20,40 q-210,-60 -420,0z', fill='#bdc7b0', stroke=LINE, sw=3)
    for i in range(8): d.circle(260 + i * 40, 250 - (i % 3) * 30, 6, fill='#f2a33a', stroke='none')
    d.rect(520, 460, 110, 60, fill=WHITE, stroke=LINE, sw=3, rx=8); d.text(575, 500, '難燃', 26, WARN, 700, 'middle')
    out('goods-winter-06', d, '焚き火のそばで使える難燃ブランケットのイメージイラスト')


def g7():  # 保温ボトル
    d = base()
    d.rect(340, 230, 120, 380, fill='#5d6a58', stroke=LINE, sw=4, rx=36)
    d.rect(330, 200, 140, 70, fill='#3d4448', stroke=LINE, sw=4, rx=16)
    d.rect(355, 330, 90, 140, fill='#6f7f6a', stroke='none', rx=20)
    for i in range(3): d.path(f'M{370+i*30},180 q12,-20 0,-40 q-12,-20 0,-40', stroke='#b9b3a3', sw=5)
    out('goods-winter-07', d, '保温ボトルのイメージイラスト')


def g8():  # 屋外用ヒーター（丸形）
    d = base()
    d.circle(400, 390, 200, fill='#fbe3c4', stroke='none', op=.6)
    d.rect(300, 480, 200, 120, fill='#3d4448', stroke=LINE, sw=4, rx=16)
    d.circle(400, 380, 130, fill='#e9e5dc', stroke=LINE, sw=5)
    d.circle(400, 380, 90, fill='#f2a33a', stroke='#b86a1e', sw=4)
    for i in range(6): d.line(310 + i * 36, 300, 310 + i * 36, 460, stroke='#3d4448', sw=3)
    out('goods-winter-08', d, '屋外でも使えるカセットガスヒーターのイメージイラスト')


def g9():  # 防寒シューズ
    d = base()
    for k, dx in enumerate((0, 210)):
        x = 190 + dx
        d.path(f'M{x},300 h120 v220 q60,10 80,50 v40 h-230 v-60z', fill='#3d4448' if k else '#566b4f', stroke=LINE, sw=4)
        d.rect(x - 10, 590, 240, 30, fill='#c9b79a', stroke=LINE, sw=4, rx=10)
        d.rect(x - 6, 290, 132, 40, fill='#e9e5dc', stroke=LINE, sw=3, rx=10)
    out('goods-winter-09', d, '防寒シューズのイメージイラスト')


def g10():  # 収納ボックス
    d = base()
    d.poly([(190, 340), (610, 340), (590, 610), (210, 610)], fill='#7d8a78', stroke=LINE, sw=4)
    d.rect(170, 300, 460, 56, fill='#6f7a6a', stroke=LINE, sw=4, rx=10)
    d.rect(330, 400, 140, 50, fill='#6a7565', stroke=LINE, sw=3, rx=8)
    for x in (230, 520): d.rect(x, 316, 50, 24, fill='#5b6656', stroke=LINE, sw=2, rx=6)
    out('goods-winter-10', d, 'ふた付き収納ボックスのイメージイラスト')


if __name__ == '__main__':
    import sys, os, json
    for f in (g1, g2, g3, g4, g5, g6, g7, g8, g9, g10): f()
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
