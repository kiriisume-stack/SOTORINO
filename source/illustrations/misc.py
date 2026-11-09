"""土地・メンテナンス・防災（No.121〜148）のイラスト。本文の記述だけを描く。"""
from scene import *
import math

OUT = {}
def out(name, d, alt): OUT[name] = (d, alt)


def base(title, sub, ratio='4:3', ba=None):
    d = D(ratio)
    if ba:
        w = d.tag(36, 30, ba, fill=WARN if ba == 'BEFORE' else GREEN, size=20); d.text(36 + w + 14, 58, title, 30, INK, 700)
    else:
        d.text(36, 60, title, 30, INK, 700)
    d.text(36, 98, sub, 19, '#4a4d46', 500)
    return d


def pbox(d, items):
    h = 40 + 36 * len(items) - 8; y = d.H - h - 24
    d.rect(30, y, d.W - 60, h, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12); points(d, 54, y + 38, items, 19, 36)


def drops(d, x, y, w, h, n=30, r=(3, 6)):
    for _ in range(n):
        xx, yy = x + d.rnd.uniform(0, w), y + d.rnd.uniform(0, h); rr = d.rnd.uniform(*r)
        d.path(f'M{xx},{yy-rr*1.6} q{rr},{rr*1.6} 0,{rr*2.4} q-{rr},-{rr*.8} 0,-{rr*2.4}z', fill=WATER, stroke=WATER_D, sw=1.2)


def mold_spots(d, x, y, w, h, n=40):
    for _ in range(n): d.circle(x + d.rnd.uniform(0, w), y + d.rnd.uniform(0, h), d.rnd.uniform(1.5, 4.5), fill=d.rnd.choice(['#2f3a2f', '#3a3a34', '#4b4f3e']), stroke='none', op=.85)


# ===================== 121 現地調査 =====================
def survey():
    s = 'tochi-kounyu-chuiten'
    d = base('境界標の有無を確認する', '敷地の角などに、境界を示す標識があるかを現地で確認')
    d.rect(80, 150, 800, 330, fill='#e8efe0', stroke='none'); d.line(80, 330, 880, 330, stroke=WARN, sw=3, dash='14 10')
    d.text(300, 260, '購入を検討している土地', 20, GREEN, 700, 'middle'); d.text(640, 260, '隣地', 20, '#6b6e66', 700, 'middle')
    d.line(480, 150, 480, 480, stroke=WARN, sw=3, dash='14 10')
    d.rect(450, 300, 60, 60, fill=CONC, stroke=LINE, sw=2.5); d.line(462, 330, 498, 330, stroke=WARN, sw=4); d.line(480, 312, 480, 348, stroke=WARN, sw=4)
    d.label(510, 330, '境界標（例：コンクリート杭）', 700, 420, anchor='middle', color=WARN)
    d.text(870, 470, '上から見たイメージ', 15, GREY, 500, 'end')
    pbox(d, ['+境界標の有無を現地で確認する', '+見つからない・記録と違う場合は、測量会社に相談'])
    out(f'{s}-01', d, '土地の現地調査：敷地の角にある境界標の有無を確認するイラスト')
    d = base('前面道路の幅を確認する', '接する道路の幅や、セットバックの必要性を確認')
    d.rect(80, 150, 800, 120, fill='#e8efe0', stroke='none'); d.text(480, 220, '敷地', 20, GREEN, 700, 'middle')
    d.rect(80, 270, 800, 160, fill=ROAD, stroke=GREY, sw=2); d.text(200, 360, '前面道路', 20, INK, 700, 'middle')
    d.rect(80, 430, 800, 50, fill='#eceae4', stroke='none'); d.text(480, 462, '向かいの敷地', 17, '#6b6e66', 600, 'middle')
    d.dim_v(560, 270, 430, '道路の幅を測る', right=True)
    d.rect(540, 262, 40, 16, fill='#e9b949', stroke='#a37d1c', sw=2, rx=4)
    d.text(870, 520 - 30, '上から見たイメージ', 15, GREY, 500, 'end')
    pbox(d, ['+道路の幅を確認（4m未満ならセットバックが必要な場合も）', '+交通量や騒音は、平日・休日、時間帯を変えて確認'])
    out(f'{s}-02', d, '土地の現地調査：前面道路の幅をメジャーで測って確認するイラスト')
    d = base('道路や隣地との高低差を確認する', '高低差や傾斜があると、造成や擁壁などの工事が必要になる場合も')
    G = 470; d.rect(0, G - 0, 300, 250, fill=ROAD, stroke='none'); d.line(0, G, 300, G, stroke=LINE, sw=2.5); d.text(150, G + 30, '道路', 18, INK, 700, 'middle')
    d.rect(300, G - 160, 600, 410, fill=SOIL, stroke='none'); d.line(300, G - 160, 900, G - 160, stroke=LINE, sw=2.5)
    d.rect(286, G - 170, 28, 170, fill=CONC, stroke=LINE, sw=2)
    for i in range(4): d.rect(220 - i * 0, G - 40 * (i + 1), 66, 40, fill='#d9d6cc', stroke=LINE, sw=1.5) if False else None
    d.dim_v(250, G - 160, G, '高低差', right=False)
    d.text(600, G - 100, '敷地', 20, INK, 700, 'middle'); d.label(300, G - 80, '擁壁・土留め', 450, 220, anchor='middle')
    d.text(900, G - 175, '横から見たイメージ', 15, GREY, 500, 'end')
    pbox(d, ['+道路・隣地との高低差、土地の傾斜を確認', '+日当たり・風通しは、時間帯を変えて複数回確認'])
    out(f'{s}-03', d, '土地の現地調査：道路と敷地の高低差や擁壁を確認するイラスト')


# ===================== 127 地盤調査（SWS） =====================
def sws():
    s = 'jiban-chousa-hiyou'
    d = base('スウェーデン式サウンディング試験', '戸建て住宅で広く使われる、比較的簡易な地盤調査', '3:2')
    G = 300; d.rect(0, G, 960, 340, fill=SOIL, stroke='none'); d.line(0, G, 960, G, stroke=LINE, sw=2.5)
    d.rect(0, G + 120, 960, 60, fill=CLAY_ if False else '#a98f6a', stroke='none', op=.6) if False else None
    d.rect(0, G + 110, 960, 70, fill='#b39468', stroke='none'); d.text(940, G + 152, 'やわらかい層', 16, WARN, 700, 'end')
    x = 330
    d.line(x, 150, x, G + 220, stroke=METAL_D, sw=8)
    d.poly([(x - 10, G + 220), (x + 10, G + 220), (x, G + 250)], fill=METAL_D, stroke=LINE, sw=1.5)
    for k in range(4): d.line(x - 10, G + 200 + k * 8, x + 10, G + 204 + k * 8, stroke=LINE, sw=2)
    for i in range(4): d.rect(x - 50, 220 + i * 18, 100, 16, fill='#7d868b', stroke=LINE, sw=1.5, rx=3)
    d.rect(x - 70, 200, 140, 14, fill=METAL, stroke=LINE, sw=2, rx=4)
    d.curved_arrow(x - 80, 190, x, 170, x + 80, 190, color=GREEN)
    d.label(x + 50, 250, 'おもりを載せる', 560, 170, anchor='middle')
    d.label(x + 70, 205, 'ハンドルを回して貫入', 600, 240, anchor='middle', color=GREEN)
    d.label(x, G + 235, '先端にスクリュー', 580, G + 70, anchor='middle')
    d.text(560, G + 230, '沈み方や回転数から地盤の強さを推定', 18, INK, 700, 'middle')
    d.text(36, 620, '※ JISでは現在「スクリューウエイト貫入試験」の名称が使われています', 16, '#6b6e66', 500)
    out(f'{s}-01', d, 'スウェーデン式サウンディング試験の仕組みのイラスト。先端がスクリューのロッドにおもりを載せ、回転させて貫入させる')


# ===================== 129 境界標（1:1） =====================
def markers():
    s = 'tochi-kyoukaisen-kakunin'
    data = [('コンクリート杭', '地面に埋め込まれたコンクリート製の杭'), ('金属プレート', 'ブロック塀や舗装面などに固定された金属の板'), ('金属鋲', 'コンクリート面などに打ち込まれた金属の鋲')]
    for k, (t, sub) in enumerate(data):
        d = D('1:1'); d.text(40, 66, '境界標の種類', 22, GREEN, 700); d.text(40, 114, t, 36, INK, 700); d.text(40, 156, sub, 19, '#4a4d46', 500)
        cx, cy = 400, 440
        if k == 0:
            d.rect(0, cy, 800, 260, fill=SOIL, stroke='none'); d.line(0, cy, 800, cy, stroke=LINE, sw=2.5)
            d.poly([(cx - 70, cy - 60), (cx + 70, cy - 60), (cx + 70, cy + 200), (cx - 70, cy + 200)], fill=CONC, stroke=LINE, sw=2.5)
            d.poly([(cx - 70, cy - 60), (cx + 70, cy - 60), (cx + 100, cy - 100), (cx - 40, cy - 100)], fill='#e3e5e0', stroke=LINE, sw=2.5)
            d.line(cx - 30, cy - 80, cx + 60, cy - 80, stroke=WARN, sw=5); d.line(cx + 15, cy - 95, cx + 15, cy - 65, stroke=WARN, sw=5)
            d.label(cx + 15, cy - 80, '頭部に十字などの印', 600, 260, anchor='middle', color=WARN)
        elif k == 1:
            d.rect(0, 200, 800, 460, fill=CONC, stroke='none')
            d.circle(cx, cy, 90, fill='#c9a85a', stroke='#8a6d16', sw=4); d.poly([(cx, cy - 50), (cx - 40, cy + 30), (cx + 40, cy + 30)], fill='#8a6d16', stroke='none')
            d.text(cx, cy + 70, '境界', 22, '#5a4510', 700, 'middle')
            d.label(cx, cy - 50, '矢印の先が境界点', 600, 260, anchor='middle', color=WARN)
        else:
            d.rect(0, 200, 800, 460, fill=CONC, stroke='none')
            d.circle(cx, cy, 34, fill='#b9bfc2', stroke=METAL_D, sw=4); d.line(cx - 20, cy, cx + 20, cy, stroke=LINE, sw=3); d.line(cx, cy - 20, cx, cy + 20, stroke=LINE, sw=3)
            d.label(cx, cy, '中心が境界点', 600, 300, anchor='middle', color=WARN)
        d.rect(40, 690, 720, 76, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12)
        d.text(60, 736, '見つからない・記録と違う場合は、測量会社に相談', 20, INK, 700)
        out(f'{s}-{k+1:02d}', d, f'境界標の種類「{t}」のイラスト。{sub}')


# ===================== 140 火災保険の被害例 =====================
def damage():
    s = 'kasai-hoken-shuuri'
    d = base('台風で屋根瓦がずれた・飛んだ', '風災：補償の対象になりやすいケース')
    d.poly([(120, 420), (480, 190), (840, 420)], fill='#8d9497', stroke=LINE, sw=3)
    for r in range(5):
        for c in range(12):
            t = (c + .5) / 12
            x = 120 + (840 - 120) * t; ytop = 190 + abs(x - 480) / 360 * 230
            yy = ytop + 18 + r * 40
            if yy < 420: d.rect(x - 26, yy - 12, 52, 26, fill='#6f777a', stroke=LINE, sw=1.2, rx=3)
    for i, (x, y, a) in enumerate(((560, 230, 25), (640, 190, -20), (720, 160, 40))): d.add(f'<g transform="rotate({a},{x},{y})"><rect x="{x-26}" y="{y-12}" width="52" height="26" rx="3" fill="#6f777a" stroke="{LINE}" stroke-width="1.5"/></g>')
    d.rect(520, 250, 52, 26, fill='#d8c39a', stroke=WARN, sw=2.5, dash='6 4')
    for i in range(3): d.arrow(60, 160 + i * 34, 220, 170 + i * 30, color=WATER_D, sw=3, head=12)
    d.text(60, 140, '台風・強風', 18, WATER_D, 700)
    d.rect(160, 420, 640, 110, fill=WALL, stroke=LINE, sw=2.5)
    d.label(546, 263, '瓦がずれ・飛散', 760, 300, anchor='middle', color=WARN)
    pbox(d, ['+台風や強風による被害は、風災として対象になりやすい', '+損傷に気づいたら、早めに写真で記録して保険会社へ連絡', '-経年劣化による損傷は、一般的に対象外'])
    out(f'{s}-01', d, '台風で屋根瓦がずれたり飛んだりした被害のイラスト（風災）')
    d = base('飛来物で外壁が破損した', '風災：補償の対象になりやすいケース')
    d.rect(200, 140, 560, 390, fill='#e6e1d6', stroke=LINE, sw=2.5)
    for i in range(1, 6): d.line(200, 140 + i * 65, 760, 140 + i * 65, stroke='#cfc8b8', sw=2)
    d.path('M430,270 l40,-10 l30,30 l-10,40 l-45,10 l-25,-30z', fill='#b9b09c', stroke=LINE, sw=2)
    for a in range(6): d.line(465, 300, 465 + 70 * math.cos(a), 300 + 70 * math.sin(a), stroke='#6f6a5c', sw=2)
    d.rect(560, 200, 70, 50, fill='#8a7a63', stroke=LINE, sw=2); d.arrow(700, 140, 600, 210, color=WARN, sw=3)
    d.label(465, 300, '外壁の破損', 300, 470, anchor='middle', color=WARN)
    pbox(d, ['+台風で飛んできた物による外壁の破損は、対象になりやすい', '-経年劣化によるひび・チョーキング・コーキングの剥がれは対象外になりやすい', '+補償内容・申請期限は契約によって異なるため確認を'])
    out(f'{s}-02', d, '台風で飛んできた物が当たって外壁が破損した被害のイラスト（風災）')


# ===================== 141 結露 =====================
def kekketsu():
    s = 'ie-kekketsu-taisaku'
    d = base('窓（とくに単板ガラスのアルミサッシ）', '暖かく湿った室内の空気が、冷たいガラスに触れて水滴になる')
    d.rect(200, 140, 560, 400, fill='#9aa3a8', stroke=LINE, sw=3); d.rect(220, 160, 250, 360, fill=GLASS, stroke=LINE, sw=2); d.rect(490, 160, 250, 360, fill=GLASS, stroke=LINE, sw=2)
    drops(d, 230, 170, 230, 340, 60); drops(d, 500, 170, 230, 340, 60); d.rect(200, 520, 560, 20, fill=WATER, stroke=WATER_D, sw=1.5, op=.7)
    d.label(740, 530, '下枠に水がたまる', 860, 300, anchor='middle', color=WARN)
    pbox(d, ['+換気で室内の湿度を下げる（24時間換気は止めない）', '+内窓の設置など、窓の断熱性能を高める'])
    out(f'{s}-01', d, '窓ガラスに結露が発生し、下枠に水がたまっているイラスト')
    d = base('外壁に面した部屋の隅', '熱が伝わりやすく、温度が下がりやすい場所')
    d.poly([(300, 130), (480, 200), (480, 560), (300, 520)], fill='#efece4', stroke=LINE, sw=2.5); d.poly([(480, 200), (760, 130), (760, 520), (480, 560)], fill='#f6f3ec', stroke=LINE, sw=2.5)
    drops(d, 440, 220, 70, 320, 30, (2.5, 4.5)); mold_spots(d, 450, 470, 60, 80, 30)
    d.rect(560, 380, 160, 160, fill='#c9a06b', stroke=LINE, sw=2); d.text(640, 470, '家具', 18, INK, 700, 'middle')
    d.label(480, 400, '部屋の隅に結露', 240, 300, anchor='middle', color=WARN)
    pbox(d, ['+家具を壁から少し離し、空気の流れをつくる', '+除湿機や換気扇を活用する'])
    out(f'{s}-02', d, '外壁に面した部屋の隅に結露が発生しているイラスト')
    d = base('押入れ・クローゼットの奥', '空気が動かず、湿気がこもりやすい場所')
    d.rect(200, 130, 560, 420, fill='#e8e2d6', stroke=LINE, sw=3); d.line(200, 330, 760, 330, stroke=LINE, sw=4)
    for i, c in enumerate(('#c9b79a', '#b9c7d0', '#d6c2c0')): d.rect(240 + i * 160, 200, 140, 120, fill=c, stroke=LINE, sw=2, rx=10)
    drops(d, 220, 140, 520, 50, 20, (2.5, 4)); mold_spots(d, 220, 340, 520, 40, 40)
    d.label(480, 160, '奥の壁に結露', 700, 600 - 20, anchor='middle', color=WARN) if False else d.label(740, 165, '奥の壁に結露', 820, 120 + 0, anchor='middle', color=WARN)
    pbox(d, ['+すのこを敷くなどして通気性を確保する', '+ときどき扉を開けて換気する'])
    out(f'{s}-03', d, '押入れ・クローゼットの奥の壁に結露が発生しているイラスト')


# ===================== 142 カビ =====================
def kabi():
    s = 'shitsunai-kabi-taisaku'
    d = base('お風呂・洗面所', '湿気がこもりやすく、カビが発生しやすい')
    for r in range(13):
        for c in range(14): d.rect(200 + c * 40, 130 + r * 30, 40, 30, fill='#e4ebee', stroke='#b6c2c7', sw=1)
    d.rect(200, 130, 560, 390, fill='none', stroke=LINE, sw=3)
    mold_spots(d, 200, 470, 560, 46, 80); mold_spots(d, 200, 130, 30, 380, 30)
    d.label(400, 495, '床や目地のカビ', 300, 120 + 60, anchor='middle', color=WARN)
    pbox(d, ['+使用後に換気扇を回す', '+壁や床の水滴を拭き取る'])
    out(f'{s}-01', d, '浴室の床や目地にカビが発生しているイラスト')
    d = base('窓まわり', '結露が発生しやすく、ゴムパッキンや窓枠にカビが出やすい')
    d.rect(200, 140, 560, 380, fill='#9aa3a8', stroke=LINE, sw=3); d.rect(225, 165, 245, 330, fill=GLASS, stroke='#2f3433', sw=6); d.rect(490, 165, 245, 330, fill=GLASS, stroke='#2f3433', sw=6)
    mold_spots(d, 225, 480, 510, 20, 70); drops(d, 240, 300, 480, 160, 30)
    d.label(400, 488, 'パッキン・窓枠のカビ', 640, 590 - 0 - 30, anchor='middle', color=WARN)
    pbox(d, ['+結露対策（換気・内窓の設置など）を行う', '+結露を見つけたら早めに拭き取る'])
    out(f'{s}-02', d, '窓のゴムパッキンや窓枠にカビが発生しているイラスト')
    d = base('エアコン内部', 'フィルターやドレンパンにカビが発生しやすい')
    d.rect(180, 170, 600, 200, fill='#f3f4f2', stroke=LINE, sw=3, rx=26); d.rect(200, 300, 560, 50, fill='#d9dcd6', stroke=LINE, sw=2, rx=8)
    for i in range(14): d.line(220 + i * 38, 200, 220 + i * 38, 290, stroke='#c9ccc6', sw=4)
    mold_spots(d, 220, 200, 520, 90, 50); mold_spots(d, 220, 315, 520, 25, 40)
    d.label(500, 250, 'フィルター', 720, 450, anchor='middle', color=WARN); d.label(300, 330, '吹き出し口・ドレンパン付近', 300, 450, anchor='middle', color=WARN)
    pbox(d, ['+フィルターを定期的に清掃する', '+必要に応じて内部洗浄を行う'])
    out(f'{s}-03', d, 'エアコン内部のフィルターや吹き出し口付近にカビが発生しているイラスト')


# ===================== 143 台風前のチェック（1:1） =====================
def typhoon():
    s = 'taifuu-taisaku-ie-niwa'
    data = ['植木鉢を室内・物置へ移動', '物干し竿を外す・固定する', '排水口・雨どいのゴミを除去', '窓に養生テープを貼る']
    for k, t in enumerate(data):
        d = D('1:1'); d.text(40, 66, '台風前のチェック', 22, GREEN, 700); d.text(40, 116, t, 34, INK, 700)
        if k == 0:
            d.rect(0, 560, 800, 120, fill='#d3d5cf', stroke='none'); d.rect(480, 200, 300, 360, fill=WALL, stroke=LINE, sw=2.5); d.rect(560, 300, 140, 260, fill='#c9a06b', stroke=LINE, sw=2)
            for i in range(3):
                x = 120 + i * 110; d.path(f'M{x-34},500 h68 l-10,60 h-48z', fill='#c0714a', stroke=LINE, sw=2); d.circle(x, 470, 34, fill=LEAF, stroke=LEAF_D, sw=2)
            d.arrow(400, 460, 550, 460, color=GREEN, sw=5); d.text(475, 440, '中へ', 20, GREEN, 700, 'middle')
        elif k == 1:
            d.rect(0, 560, 800, 120, fill='#d3d5cf', stroke='none')
            for x in (180, 620): d.line(x, 560, x, 280, stroke=METAL_D, sw=10); d.line(x - 40, 300, x + 40, 300, stroke=METAL_D, sw=6)
            d.line(160, 296, 640, 296, stroke=METAL, sw=10); d.arrow(500, 340, 500, 470, color=GREEN, sw=4)
            d.line(200, 520, 600, 520, stroke=METAL, sw=10); d.text(400, 500, '外して低い位置に置く', 20, GREEN, 700, 'middle')
        elif k == 2:
            d.rect(0, 400, 800, 280, fill=CONC, stroke='none')
            d.rect(220, 420, 360, 90, fill='#9aa3a8', stroke=LINE, sw=3)
            for i in range(17): d.line(232 + i * 20, 424, 232 + i * 20, 506, stroke=LINE, sw=3)
            for i in range(9): d.ellipse(260 + i * 34, 440 + (i % 2) * 30, 18, 8, fill='#b98b3c', stroke='#7d5a22', sw=1.5)
            d.text(400, 600, 'グレーチング（格子状のふた）の落ち葉を除去', 20, INK, 700, 'middle')
        else:
            d.rect(160, 200, 480, 420, fill='#9aa3a8', stroke=LINE, sw=3); d.rect(180, 220, 440, 380, fill=GLASS, stroke=LINE, sw=2)
            for (a, b) in (((180, 220), (620, 600)), ((620, 220), (180, 600))):
                d.line(a[0], a[1], b[0], b[1], stroke='#7fb36a', sw=26, cap='butt')
            d.text(400, 660, '割れたときの飛散を減らす目的', 20, INK, 700, 'middle')
        d.rect(40, 690, 720, 76, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12)
        d.text(60, 736, '強風で飛ばされるものと、水がたまる場所を事前に確認', 20, INK, 700)
        out(f'{s}-{k+1:02d}', d, f'台風前のチェック「{t}」のイラスト')


# ===================== 144 排水口・グレーチング =====================
def grating():
    s = 'ooame-niwa-chushajou-mizubitashi'
    for k in range(2):
        d = base(('落ち葉やゴミで詰まった排水口', 'ゴミを取り除くと、水が排水口へ流れる')[k], ('大雨のとき、処理しきれずに水があふれやすい', '大雨の前、台風の前にも清掃しておく')[k])
        G = 360; d.rect(0, G, 960, 250, fill=CONC, stroke='none'); d.line(0, G, 960, G, stroke=LINE, sw=2.5)
        d.rect(400, G, 160, 140, fill='#c9ccc6', stroke=CONC_D, sw=2.5); d.rect(415, G, 130, 130, fill='#e9ece6', stroke=CONC_D, sw=1.5)
        for i in range(9): d.line(404 + i * 19, G - 8, 404 + i * 19, G, stroke=METAL_D, sw=4)
        d.line(400, G - 8, 560, G - 8, stroke=METAL_D, sw=4)
        if k == 0:
            for i in range(10): d.ellipse(410 + i * 15, G - 14 - (i % 3) * 4, 12, 6, fill='#b98b3c', stroke='#7d5a22', sw=1.5)
            d.path(f'M80,{G} Q300,{G-36} 400,{G-30} L560,{G-30} Q700,{G-36} 880,{G}Z', fill=WATER, stroke=WATER_D, sw=2, op=.85)
            d.label(480, G - 18, 'グレーチングが詰まっている', 480, 200, anchor='middle', color=WARN)
        else:
            d.arrow(120, G - 14, 390, G - 10, color=WATER_D, sw=4); d.arrow(840, G - 14, 570, G - 10, color=WATER_D, sw=4)
            d.arrow(480, G + 10, 480, G + 100, color=WATER_D, sw=4)
            d.label(480, G - 8, '格子のすき間が開いている', 480, 200, anchor='middle', color=GREEN)
        d.text(940, G + 220, '断面イメージ', 15, GREY, 500, 'end')
        pbox(d, (['-排水口・グレーチングにゴミがたまっている', '-コンクリートなど水を通さない舗装は、水が地面に浸透しない'],
                 ['+排水口やグレーチングのゴミを定期的に取り除く', '+毎回深刻な場合は、排水口の増設や透水性舗装を検討'])[k])
        out(f'{s}-{k+1:02d}', d, ('落ち葉で詰まった排水口のグレーチングと、あふれた雨水の断面イラスト', 'ゴミを取り除いた排水口に雨水が流れ込む断面イラスト')[k])


# ===================== 146 剪定 =====================
def pruning():
    s = 'niwaki-sentei-jiki'
    d = base('剪定に使う主な道具', '太い枝には専用の道具を使い、切り口には癒合剤を塗る場合も')
    items = [('剪定ばさみ', 0), ('剪定ノコギリ', 1), ('癒合剤', 2)]
    for i, (t, k) in enumerate(items):
        x = 50 + i * 295; d.rect(x, 140, 270, 340, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=14); cx = x + 135
        if k == 0:
            d.add(f'<g transform="rotate(-30,{cx},300)"><path d="M{cx-10},300 l-12,-110 q12,-8 20,4z" fill="{METAL}" stroke="{LINE}" stroke-width="2"/><path d="M{cx+10},300 l12,-110 q-12,-8 -20,4z" fill="#c9cfd2" stroke="{LINE}" stroke-width="2"/><rect x="{cx-30}" y="300" width="22" height="110" rx="10" fill="{WARN}" stroke="{LINE}" stroke-width="2"/><rect x="{cx+8}" y="300" width="22" height="110" rx="10" fill="{WARN}" stroke="{LINE}" stroke-width="2"/></g>')
        elif k == 1:
            d.add(f'<g transform="rotate(-30,{cx},300)"><path d="M{cx-14},180 L{cx+14},180 L{cx+14},330 L{cx-14},330 Z" fill="{METAL}" stroke="{LINE}" stroke-width="2"/></g>')
            d.add(f'<g transform="rotate(-30,{cx},300)">' + ''.join(f'<path d="M{cx-14},{185+j*12} l-8,6 l8,6" fill="none" stroke="{LINE}" stroke-width="1.5"/>' for j in range(12)) + f'<rect x="{cx-16}" y="330" width="32" height="90" rx="10" fill="{WOOD}" stroke="{LINE}" stroke-width="2"/></g>')
        else:
            d.rect(cx - 30, 230, 60, 140, fill='#7d8a78', stroke=LINE, sw=2, rx=8); d.rect(cx - 16, 200, 32, 32, fill='#e9e4d8', stroke=LINE, sw=2, rx=4)
            d.text(cx, 310, '癒合剤', 16, WHITE, 700, 'middle')
        d.text(cx, 450, t, 22, INK, 700, 'middle')
    pbox(d, ['+高所の剪定は転落のリスクがあるため無理をしない', '+電線や隣地にかかる枝は、トラブルを避けるため慎重に'])
    out(f'{s}-01', d, '庭木の剪定に使う主な道具（剪定ばさみ・剪定ノコギリ・癒合剤）のイラスト')
    for k in range(2):
        d = base(('剪定前', '剪定後')[k], ('枝が密集し、風通し・日当たりが悪い', '密集した枝を減らし、樹形を整える')[k])
        G = 500; ground(d, G, fill=SOIL); X0 = 480
        d.path(f'M{X0-14},{G} L{X0-10},{G-170} L{X0+10},{G-170} L{X0+14},{G}z', fill=TRUNK, stroke=LINE, sw=2)
        rnd = d.rnd
        brs = [(-1, 200, 260), (1, 210, 250), (-1, 260, 200), (1, 270, 200), (0, 300, 180), (-1, 230, 160), (1, 240, 150), (-1, 300, 110), (1, 300, 110)]
        for i, (sgn, L, ang) in enumerate(brs):
            if k == 1 and i in (5, 6, 7, 8): continue
            x1 = X0 + sgn * L * .55; y1 = G - 170 - L * .55 * (1 if sgn == 0 else .8)
            d.line(X0, G - 170 + (i % 3) * 20, x1, y1, stroke=TRUNK, sw=8 - i * .4)
            d.circle(x1, y1, 60 if k == 0 else 48, fill=LEAF if k == 0 else '#8fb37a', stroke=LEAF_D, sw=2, op=.95)
        if k == 0:
            for _ in range(40): d.line(X0 + rnd.uniform(-200, 200), G - rnd.uniform(220, 380), X0 + rnd.uniform(-200, 200), G - rnd.uniform(220, 380), stroke=TRUNK, sw=2)
            d.label(X0 + 160, G - 280, '枝が混み合っている', 800, 180, anchor='middle', color=WARN)
        else:
            for (x, y) in ((X0 - 120, G - 260), (X0 + 130, G - 250)): d.circle(x, y, 8, fill='#e6d5ae', stroke=LINE, sw=2)
            d.label(X0 - 120, G - 260, '切り口', 200, 180, anchor='middle', color=GREEN)
            for i in range(3): d.arrow(120, 300 + i * 30, 340, 300 + i * 30, color=WATER_D, sw=2.5, head=11)
            d.text(120, 280, '風が通る', 17, WATER_D, 700)
        pbox(d, (['-風通し・日当たりが悪く、病害虫が発生しやすい', '+落葉樹は葉が落ちた休眠期（冬）、常緑樹は花後や春〜初夏が目安'],
                 ['+風通し・日当たりが改善し、病害虫の予防に', '+花を咲かせる木は、花芽の時期と重ならないよう確認'])[k])
        out(f'{s}-{k+2:02d}', d, ('剪定前の庭木のイラスト。枝が密集して風通しが悪い', '剪定後の庭木のイラスト。混み合った枝を減らして風が通る')[k])


# ===================== 147 外壁のひび割れ種類 =====================
def cracks():
    s = 'gaiheki-hibiware-houchi'
    data = [('ヘアークラック', '幅0.3mm程度以下の細いひび。表面的な塗膜の劣化によるものが多い', 2, ['+比較的軽度', '+定期的に観察し、必要に応じて補修']),
            ('構造クラック', '幅0.3mmを超える、建物の構造的な動きによるひび', 7, ['-雨水が侵入し、内部の木材や鉄筋の劣化を進める', '-早めに専門業者に調査を依頼'])]
    for k, (t, sub, sw, pts) in enumerate(data):
        d = base(t, sub)
        d.rect(80, 140, 480, 380, fill='#e6e1d6', stroke=LINE, sw=2.5)
        p = 'M200,140 l30,70 l-20,60 l40,80 l-14,60 l26,110' if k else 'M220,200 l20,40 l-10,30 l26,40 M380,300 l16,30 l-8,26'
        d.path(p, stroke='#5f6467', sw=sw)
        # 断面
        sx = 620; d.rect(sx, 160, 120, 340, fill='#d9d3c4', stroke=LINE, sw=2); d.rect(sx, 160, 14, 340, fill='#e6e1d6', stroke=LINE, sw=1.5)
        if k == 0: d.poly([(sx, 300), (sx + 12, 304), (sx, 308)], fill='#5f6467', stroke='none'); d.label(sx + 8, 304, '表面（塗膜）だけ', 820, 240, anchor='middle', color=WARN)
        else:
            d.poly([(sx, 290), (sx + 90, 318), (sx, 330)], fill='#5f6467', stroke='none')
            for i in range(3): d.path(f'M{sx-40+i*8},{300+i*8} q20,4 40,10', stroke=WATER_D, sw=2.5)
            d.label(sx + 60, 312, '内部まで達する', 830, 240, anchor='middle', color=WARN); d.text(sx - 50, 280, '雨水', 16, WATER_D, 700)
        d.text(680, 530, '断面イメージ', 15, GREY, 500, 'middle')
        pbox(d, pts + ['+実際の危険度は、専門家の診断で判断する'])
        out(f'{s}-{k+1:02d}', d, f'外壁の{t}のイラスト。{sub}')


# ===================== 148 雨どい BA =====================
def gutter():
    s = 'amadoi-souji'
    for k in range(2):
        d = base(('落ち葉で詰まり、雨水があふれる', '掃除して、雨水が縦どいへ流れる')[k], ('詰まった部分から水があふれ、外壁を傷める可能性', 'ゴミ取りネットを付けると、詰まりの予防に')[k], ba=('BEFORE', 'AFTER')[k])
        d.rect(140, 260, 680, 300, fill=WALL, stroke=LINE, sw=2.5)
        d.poly([(100, 260), (860, 260), (860, 200), (100, 150)], fill='#7d8a78', stroke=LINE, sw=2.5)
        d.path('M120,262 h700 q0,40 -40,40 h-620 q-40,0 -40,-40z', fill='#cfd3d0', stroke=LINE, sw=2.5)
        d.rect(780, 300, 26, 260, fill='#cfd3d0', stroke=LINE, sw=2.5)
        if k == 0:
            for i in range(16): d.ellipse(300 + i * 26, 268 + (i % 2) * 4, 13, 6, fill=d.rnd.choice(['#b98b3c', '#a3601e', '#7d8a5a']), stroke='#7d5a22', sw=1.2)
            for i in range(5): d.path(f'M{340+i*60},300 q-6,40 0,90', stroke=WATER_D, sw=3)
            d.ellipse(480, 440, 140, 60, fill='#cfc4ad', stroke='none', op=.7)
            d.label(500, 272, '落ち葉・ゴミの詰まり', 500, 160 - 30 + 0, anchor='middle', color=WARN) if False else d.label(500, 272, '落ち葉・ゴミの詰まり', 600, 130, anchor='middle', color=WARN)
            d.label(480, 440, '外壁を傷める', 300, 500, anchor='middle', color=WARN)
        else:
            for i in range(28): d.line(130 + i * 24, 262, 140 + i * 24, 278, stroke='#6c757a', sw=1.5)
            d.line(122, 264, 818, 264, stroke='#6c757a', sw=2)
            d.arrow(300, 285, 760, 285, color=WATER_D, sw=3); d.arrow(793, 320, 793, 520, color=WATER_D, sw=3)
            d.label(400, 266, 'ゴミ取りネット', 400, 130, anchor='middle', color=GREEN)
        pbox(d, (['-雨水があふれて外壁を傷める', '-重さや劣化で雨どいが歪む・外れることも', '-溢れた水が隙間から侵入し、雨漏りの原因にも'],
                 ['+はしごを使い、手やブラシでゴミを取り除く', '+ゴミ取りネットで詰まりを予防', '+高所作業に不安があれば、専門業者に依頼'])[k])
        out(f'{s}-{k+1:02d}', d, ('落ち葉で詰まった雨どいから雨水があふれているビフォーのイラスト', '掃除してゴミ取りネットを付けた雨どいに雨水が流れるアフターのイラスト')[k])


if __name__ == '__main__':
    import sys, os, json
    for f in (survey, sws, markers, damage, kekketsu, kabi, typhoon, grating, pruning, cracks, gutter): f()
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
