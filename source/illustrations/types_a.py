"""種類比較イラスト（外構・庭）— 3:2。本文の記述だけを根拠に、特徴を図とポイントで示す。"""
from scene import *

OUT = {}
def out(name, d, alt): OUT[name] = (d, alt)


def base(title, sub):
    d = D('3:2'); d.header(title, sub, 30); return d


def pbox(d, items, y=490, h=136):
    d.rect(30, y, 900, h, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12)
    points(d, 54, y + 40, items, 19, 36)


# ================= 6 オープン外構 / クローズ外構 =================
def open_close():
    s = 'open-gaikou-close-gaikou-chigai'
    for k, (title, sub) in enumerate((('オープン外構', '塀やフェンスで敷地を囲わない外構'), ('クローズ外構', '塀・フェンス・門扉で敷地全体を囲う外構'))):
        d = base(title, sub); G = 450
        d.rect(0, 120, 960, G - 120, fill=SKY, stroke='none'); ground(d, G)
        house(d, 400, G, 320, 200, 80)
        window_people(d, 475, 330); window_people(d, 645, 330)
        e = person(d, 110, G, 1.0)
        if k == 0:
            hedge(d, 300, G, 70, 40); hedge(d, 790, G, 90, 40); tree(d, 830, G, 210, 46)
            sight(d, e[0], e[1], 470, 320)
            d.label(330, G - 20, '囲いがなく開放的', 240, 170, anchor='middle')
            pbox(d, ['+開放的な見た目で、費用を抑えやすい', '+死角が少なく、見通しが良い', '-道路からの視線が入りやすく、侵入を防ぐ境界は弱い'])
        else:
            slat_fence(d, 290, G, 240, 170); slat_fence(d, 640, G, 240, 170)
            d.rect(530, G - 150, 110, 150, fill='#8a7a63', stroke=LINE, sw=2)
            for i in range(1, 6): d.line(530 + i * 18.3, G - 150, 530 + i * 18.3, G, stroke=LINE, sw=1.5)
            d.text(585, G + 30, '門扉', 18, INK, 700, 'middle')
            sight(d, e[0], e[1], 290, 322, blocked=True)
            d.label(410, G - 170, 'フェンス・門扉で囲う', 330, 160, anchor='middle')
            pbox(d, ['+プライバシーを確保しやすく、庭を自由に使いやすい', '+侵入しにくく、防犯性が高い', '-費用がかかりやすく、外から見えない死角ができる場合も'])
        d.text(940, G + 24, '正面から見たイメージ', 15, GREY, 500, 'end')
        out(f'{s}-{k+1:02d}', d, f'{title}の特徴を示すイラスト。' + ('塀やフェンスで囲わず開放的だが、道路からの視線は入りやすい' if k == 0 else 'フェンスと門扉で囲い、道路からの視線を遮る'))


# ================= 11 目隠しの方法 =================
def louver(d, x, y, w, h):
    for px in (x, x + w - 10): d.rect(px, y - h, 10, h, fill=METAL_D, stroke=LINE, sw=1.5)
    yy = y - h + 10
    while yy < y - 10:
        d.poly([(x + 10, yy), (x + w - 10, yy), (x + w - 10, yy + 12), (x + 10, yy + 12)], fill='#b9a07c', stroke=LINE, sw=1.2)
        d.line(x + 10, yy + 12, x + w - 10, yy + 12, stroke='#8a7350', sw=3); yy += 22


def mekakushi():
    s = 'gaikou-mekakushi-method'
    data = [('目隠しフェンス', '最も一般的な方法。素材やデザインの種類が豊富', ['+遮る力が高い（高さ・板の間隔で調整できる）', '+メンテナンスが少ない', '+アルミ・樹脂・木目調など素材が豊富']),
            ('植栽（樹木・生垣）', '樹木や生垣で、自然な見た目の目隠しをつくる', ['+自然な見た目で、費用は低め〜中程度', '-成長して目隠しになるまで時間がかかる', '-定期的な剪定が必要']),
            ('目隠しスクリーン・ルーバー', '庭やテラスの一部に設置して、部分的に視線を遮る', ['+視線を遮りつつ、風や光を通しやすい', '+庭やテラスの一部だけに設置しやすい', '+メンテナンスが少ない']),
            ('塀（ブロック・コンクリートなど）', '壁で完全に視線を遮る方法', ['+視線を完全に遮ることができる', '-費用が高くなりやすい', '-圧迫感が出やすく、死角もできやすい'])]
    for k, (title, sub, pts) in enumerate(data):
        d = base(title, sub); G = 450
        d.rect(0, 120, 960, G - 120, fill=SKY, stroke='none'); ground(d, G)
        house(d, 560, G, 320, 200, 80, win=True); window_people(d, 635, 330)
        d.rect(500, G - 14, 60, 14, fill='#cfc7b6', stroke=LINE, sw=1.5)
        e = person(d, 100, G, 1.0); bx = 300
        if k == 0:
            slat_fence(d, bx, G, 170, 190); sight(d, e[0], e[1], bx, 318, blocked=True)
            d.label(bx + 170, G - 120, '板の間隔で透け具合を調整', bx + 260, 150, anchor='middle')
        elif k == 1:
            hedge(d, bx - 10, G, 190, 170); tree(d, bx + 150, G, 260, 50); sight(d, e[0], e[1], bx - 4, 322, blocked=True)
            d.label(bx + 150, G - 240, '成長に時間・剪定が必要', bx + 250, 150, anchor='middle')
        elif k == 2:
            louver(d, bx + 120, G, 130, 190); d.rect(bx + 260, G - 14, 230, 14, fill='#cfc7b6', stroke=LINE, sw=1.5); d.text(bx + 375, G - 22, 'テラス', 16, INK, 700, 'middle')
            sight(d, e[0], e[1], bx + 120, 322, blocked=True)
            # 断面の拡大
            cx, cy = bx + 10, 220; d.circle(cx, cy, 70, fill=WHITE, stroke=GREY, sw=2)
            for i in range(4): d.line(cx - 34, cy - 45 + i * 28, cx + 10, cy - 25 + i * 28, stroke='#8a7350', sw=6)
            d.arrow(cx - 62, cy - 4, cx + 62, cy + 2, color=WATER_D, sw=2.5, head=11); d.text(cx, cy + 92, '羽根の断面：風は通る', 16, WATER_D, 700, 'middle')
        else:
            block_wall(d, bx, G, 190, 190); sight(d, e[0], e[1], bx, 322, blocked=True)
            d.label(bx + 95, G - 190, '完全に遮るが圧迫感が出やすい', bx + 240, 150, anchor='middle')
        pbox(d, pts)
        d.text(940, G + 24, '横から見たイメージ', 15, GREY, 500, 'end')
        out(f'{s}-{k+1:02d}', d, f'目隠しの方法「{title}」のイラスト。道路からの視線を遮る様子と特徴')


# ================= 19 地面・舗装材 =================
def paving():
    s = 'niwa-jimen-housou-shurui'
    X, W, T = 60, 840, 320
    def soil(d, h=150): d.soil(X, T, W, h)
    items = []
    # 天然芝
    d = base('天然芝', '柔らかく自然な見た目。水やりや芝刈りなど定期的な手入れが必要'); soil(d)
    d.turf(X, T, W, 6, 34, 6, color='#86b45e', dark='#5f8f3d')
    for i in range(24): d.path(f'M{X+20+i*35},{T} q-4,20 2,38 M{X+32+i*35},{T} q5,16 0,30', stroke='#8a6a48', sw=1.6)
    d.label(X + 300, T - 20, '芝生（生きた植物）', X + 300, 190, anchor='middle'); d.label(X + 560, T + 26, '土に根を張る', X + 640, 190, anchor='middle')
    pbox(d, ['+柔らかく、遊び場や観賞用に向く', '+費用は低め', '-水やり・芝刈りなど手入れが多い']); items.append((d, '天然芝の断面イラスト。土に根を張る芝生で、水やりや芝刈りが必要'))
    # 人工芝
    d = base('人工芝', '手入れの手間が少なく、一年中緑を保てる'); soil(d); d.compact_marks(X, T, W)
    d.sheet(X, T, W, 7); d.turf(X, T - 7, W, 8, 30, 6)
    d.label(X + 260, T - 30, '人工芝', X + 200, 190, anchor='middle'); d.label(X + 520, T - 4, '防草シート', X + 520, 190, anchor='middle'); d.label(X + 760, T + 30, '整地・転圧した地面', X + 700, 260, anchor='middle')
    pbox(d, ['+一年中緑を保てる', '+長期的な手入れの負担を抑えられる', '-初期費用はかかる（費用感は中程度）']); items.append((d, '人工芝の断面イラスト。整地した地面に防草シートを敷き、その上に人工芝を敷く'))
    # 砂利
    d = base('砂利', '費用を抑えやすく、雑草対策にもなる'); soil(d); d.sheet(X, T, W, 7); d.gravel_layer(X, T - 57, W, 50)
    d.label(X + 260, T - 40, '砂利', X + 200, 190, anchor='middle'); d.label(X + 560, T - 4, '防草シート', X + 600, 190, anchor='middle')
    pbox(d, ['+費用を抑えやすい（雑草対策・通路向き）', '+手入れが少ない', '-防草シートの施工状況によって効果が変わる']); items.append((d, '砂利敷きの断面イラスト。防草シートの上に砂利を敷く'))
    # タイル・石材
    d = base('タイル・石材', 'デザイン性が高く、屋外リビングのような空間をつくりやすい'); soil(d, 170)
    d.gravel_layer(X, T - 40, W, 40, r=(5, 9), round_=False); d.rect(X, T - 100, W, 60, fill=CONC, stroke=CONC_D, sw=2)
    d.rect(X, T - 116, W, 16, fill=MORTAR, stroke='#b9b3a3', sw=1.5); d.tile_row(X, T - 116, W, 100, 18, 5)
    d.label(X + 160, T - 125, 'タイル・石材', X + 160, 170, anchor='middle'); d.label(X + 420, T - 108, 'モルタル', X + 420, 170, anchor='middle')
    d.label(X + 640, T - 70, 'コンクリート', X + 660, 170, anchor='middle'); d.label(X + 820, T - 20, '砕石', X + 840, 250, anchor='middle')
    d.text(X + W, T + 164, '断面の一例', 15, GREY, 500, 'end')
    pbox(d, ['+デザイン性が高く、くつろぎスペースに向く', '+手入れが少ない', '-費用は比較的高くなる傾向']); items.append((d, 'タイル・石材の舗装の断面イラスト（一例）。砕石・コンクリートの上にモルタルでタイルを張る'))
    # コンクリート・インターロッキング
    d = base('コンクリート・インターロッキング', '耐久性が高く、駐車スペースなど荷重がかかる場所にも向く'); soil(d)
    h = W / 2 - 10
    d.gravel_layer(X, T - 40, h, 40, r=(5, 9), round_=False); d.rect(X, T - 110, h, 70, fill=CONC, stroke=CONC_D, sw=2)
    d.line(X + 6, T - 76, X + h - 6, T - 76, stroke=METAL_D, sw=2.5, dash='14 8')
    d.gravel_layer(X + h + 20, T - 40, h, 40, r=(5, 9), round_=False); d.sand(X + h + 20, T - 66, h, 26)
    xx = X + h + 20
    while xx < X + W - 2: d.rect(xx, T - 126, 58, 60, fill='#c79a77' if int((xx - X) / 60) % 2 else '#b98966', stroke='#7d5a3e', sw=2, rx=3); xx += 60
    d.text(X + h / 2, T + 60, 'コンクリート', 22, INK, 700, 'middle'); d.text(X + h + 20 + h / 2, T + 60, 'インターロッキング', 22, INK, 700, 'middle')
    d.label(X + 200, T - 76, '鉄筋（ワイヤーメッシュ）', X + 200, 180, anchor='middle'); d.label(X + h + 300, T - 54, '砂', X + h + 300, 180, anchor='middle'); d.label(X + 120, T - 20, '砕石', X + 120, T + 110, anchor='middle')
    d.text(X + W, T + 164, '断面の一例', 15, GREY, 500, 'end')
    pbox(d, ['+耐久性が高い', '+駐車場や通路など、荷重がかかる場所に向く', '+手入れが少ない（費用感は中程度〜高め）']); items.append((d, 'コンクリート舗装とインターロッキング舗装の断面イラスト（一例）'))
    for i, (dd, a) in enumerate(items): out(f'{s}-{i+1:02d}', dd, a)


# ================= 24 タイルデッキ / ウッドデッキ =================
def decks():
    s = 'tile-deck-wood-deck-chigai'
    for k in range(2):
        G = 450
        d = base(('タイルデッキ', 'ウッドデッキ（人工木を含む）')[k], ('コンクリートの土台の上にタイルを張ったデッキ', '床板を束（支柱）と根太で支えるデッキ')[k])
        d.rect(0, 120, 960, G - 120, fill=SKY, stroke='none'); ground(d, G)
        d.rect(560, 150, 400, G - 150, fill=WALL, stroke=LINE, sw=2.5); d.rect(600, 220, 140, G - 120 - 220 + 120 - 60, fill=GLASS, stroke=LINE, sw=2)
        top = G - 70
        if k == 0:
            d.rect(200, top, 360, 70, fill=CONC, stroke=CONC_D, sw=2); d.rect(200, top - 14, 360, 14, fill=MORTAR, stroke='#b9b3a3', sw=1.5)
            d.tile_row(200, top - 14 + 0.01, 360, 70, 14, 2, fill='#d9cfc0', stroke='#8f8576')
            d.rect(140, G - 34, 60, 34, fill=CONC, stroke=CONC_D, sw=2); d.tile_row(140, G - 34, 60, 60, 10, 0, fill='#d9cfc0', stroke='#8f8576')
            d.label(300, top - 20, 'タイル仕上げ', 260, 170, anchor='middle'); d.label(420, top + 40, 'コンクリートの土台', 400, 250, anchor='middle')
            pbox(d, ['+耐久性が高く、色あせや劣化が少ない', '+水や汚れに強く、掃除がしやすい', '-直射日光の下では表面が熱くなりやすい素材もある'])
        else:
            for px in (230, 340, 450, 540):
                d.rect(px - 20, G - 16, 40, 16, fill=CONC, stroke=CONC_D, sw=2); d.rect(px - 8, top, 16, 54, fill=WOOD_D, stroke=LINE, sw=1.5)
            d.rect(200, top, 360, 14, fill='#b88850', stroke=LINE, sw=1.5)
            xx = 200
            while xx < 560: d.rect(xx, top - 16, 42, 16, fill=WOOD, stroke=WOOD_D, sw=1.5); xx += 45
            d.label(260, top - 16, '床板（天然木・人工木）', 230, 165, anchor='middle'); d.label(500, top + 7, '根太・大引', 450, 165, anchor='middle'); d.label(340, top + 30, '束（支柱）', 270, 250, anchor='middle'); d.label(450, G - 8, '束石', 450, 250, anchor='middle')
            pbox(d, ['+温かみのある質感で、ナチュラルな雰囲気になる', '-天然木は定期的な塗装や防腐処理が必要', '+人工木（樹脂木）はメンテナンスの手間が少ない'])
        d.text(940, G + 24, '横から見たイメージ', 15, GREY, 500, 'end')
        out(f'{s}-{k+1:02d}', d, ('タイルデッキの構造イラスト。コンクリートの土台の上にタイルを張る', 'ウッドデッキの構造イラスト。束石と束（支柱）で床板を支える')[k])


# ================= 54 カーポートの構造 =================
def car_front(d, cx, y, w=180):
    h = w * .62
    d.path(f'M{cx-w/2},{y-18} L{cx-w/2},{y-h*.55} Q{cx-w/2+6},{y-h*.62} {cx-w*.38},{y-h*.64} L{cx-w*.3},{y-h} L{cx+w*.3},{y-h} L{cx+w*.38},{y-h*.64} Q{cx+w/2-6},{y-h*.62} {cx+w/2},{y-h*.55} L{cx+w/2},{y-18} Z', fill='#9fb0bf', stroke=LINE, sw=2.5)
    d.poly([(cx - w * .27, y - h * .96), (cx + w * .27, y - h * .96), (cx + w * .34, y - h * .66), (cx - w * .34, y - h * .66)], fill=GLASS, stroke=LINE, sw=2)
    for sx in (-1, 1): d.rect(cx + sx * w * .36 - 16, y - 22, 32, 22, fill='#3d4448', stroke=LINE, sw=2, rx=4)


def carports():
    s = 'carport-shurui-erabikata'; G = 450; RY = 220
    data = [('片側支持タイプ', '柱が片側だけにあるカーポート', ['+車の乗り降りの際に、柱が邪魔になりにくい', '-構造的な安定性は、両側支持よりやや低い']),
            ('両側支持タイプ', '柱が両側にあるカーポート', ['+構造的な安定性が高い', '+強風・積雪地域に向いている傾向', '-柱が乗り降りに干渉する場合がある']),
            ('後方支持タイプ', '柱を建物側や奥に配置するカーポート', ['+前面の見た目がすっきりする', '+乗り降りがしやすい', '-安定性は設置条件による'])]
    for k, (title, sub, pts) in enumerate(data):
        d = base(title, sub); d.rect(0, 120, 960, G - 120, fill=SKY, stroke='none'); ground(d, G, fill=ROAD)
        if k < 2:
            if k == 0:
                d.rect(250, RY - 6, 520, 18, fill='#c5d5de', stroke=LINE, sw=2.5); d.rect(250, RY, 20, G - RY, fill=METAL_D, stroke=LINE, sw=2)
                d.path(f'M270,{RY+12} L320,{RY+12} L270,{RY+60}z', fill=METAL, stroke=LINE, sw=2)
                car_front(d, 520, G, 220)
                d.arrow(660, 340, 760, 340, color=GREEN, sw=4); d.text(770, 330, '柱がなく', 18, GREEN, 700); d.text(770, 356, '乗り降りしやすい', 18, GREEN, 700)
                d.label(260, 300, '柱は片側だけ', 150, 180, anchor='middle')
            else:
                d.rect(170, RY - 6, 620, 18, fill='#c5d5de', stroke=LINE, sw=2.5)
                for px in (170, 770): d.rect(px, RY, 20, G - RY, fill=METAL_D, stroke=LINE, sw=2)
                car_front(d, 380, G, 190); car_front(d, 590, G, 190)
                d.label(180, 300, '柱が両側にある', 120, 170, anchor='middle'); d.label(780, 300, '柱が両側にある', 860, 170, anchor='middle')
            d.text(940, G + 24, '正面から見たイメージ', 15, GREY, 500, 'end')
        else:
            d.rect(780, 150, 180, G - 150, fill=WALL, stroke=LINE, sw=2.5)
            d.poly([(220, RY + 20), (760, RY - 10), (760, RY + 8), (220, RY + 36)], fill='#c5d5de', stroke=LINE, sw=2.5)
            d.rect(740, RY - 4, 20, G - RY + 4, fill=METAL_D, stroke=LINE, sw=2); d.path(f'M740,{RY+14} L690,{RY+16} L740,{RY+70}z', fill=METAL, stroke=LINE, sw=2)
            car_side(d, 300, G, 380)
            d.label(750, 330, '柱は奥（建物側）', 600, 296, anchor='middle'); d.label(240, RY + 30, '前面に柱がない', 200, 170, anchor='middle')
            d.text(30, G + 24, '横から見たイメージ', 15, GREY, 500)
        pbox(d, pts)
        out(f'{s}-{k+1:02d}', d, f'カーポートの{title}の構造イラスト。' + sub)


# ================= 55 カーポートの屋根材 =================
def roofs():
    s = 'carport-yane-zairyou-chigai'; G = 450; RY = 250
    data = [('ポリカーボネート（熱線遮断タイプ）', '光を通しながら、紫外線や熱をある程度カットする', '#a9c3d6', .55, 2, ['+採光性が高い', '+遮熱性が比較的高い（紫外線や熱をある程度カット）', '+広く使われている屋根材']),
            ('ポリカーボネート（クリアタイプ）', '採光性が高く、明るい駐車スペースをつくりやすい', '#dff0f7', .35, 5, ['+採光性が非常に高い', '-遮熱性は熱線遮断タイプより劣る場合がある', '+駐車スペースが明るい']),
            ('スチール・アルミ製の屋根材', '遮光性・耐久性が高い', '#8e979c', 1, 0, ['+遮光性・耐久性が高い（日差しを遮る）', '-光を取り込みにくい', '-駐車スペースが暗くなりやすい'])]
    for k, (title, sub, col, op, nlight, pts) in enumerate(data):
        d = base(title, sub); d.rect(0, 120, 960, G - 120, fill=SKY, stroke='none'); ground(d, G, fill=ROAD)
        d.circle(100, 170, 34, fill='#f6d36b', stroke='#c9a73a', sw=2)
        # rays
        for i in range(5):
            x0 = 150 + i * 30; x1 = 300 + i * 110
            d.line(x0, 190, x1, RY - 4, stroke='#e2b93b', sw=3, dash='8 6')
            if i < (4 if k == 0 else nlight): d.line(x1, RY + 14, x1 + 70, G - 120, stroke='#e2b93b', sw=3, dash='8 6')
        if k == 2:
            d.poly([(250, G), (820, G), (820, G - 8), (250, G - 8)], fill='#7d868b', stroke='none', op=.35)
        else:
            d.rect(260, G - 10, 540, 10, fill='#f6e6a6' if k == 1 else '#f1e8c6', stroke='none')
        d.rect(250, RY, 580, 14, fill=col, stroke=LINE, sw=2.5, op=1)
        d.rect(250, RY + 14, 20, G - RY - 14, fill=METAL_D, stroke=LINE, sw=2)
        car_side(d, 380, G, 360)
        # heat
        hx = 760; d.text(hx + 55, 178, '熱', 20, WARN, 700, 'middle')
        d.path(f'M{hx+40},{RY-60} q10,10 0,20 q-10,10 0,20', stroke=WARN, sw=3)
        d.path(f'M{hx+70},{RY-60} q10,10 0,20 q-10,10 0,20', stroke=WARN, sw=3)
        if k == 1: d.path(f'M{hx+55},{RY+30} q10,10 0,20 q-10,10 0,20', stroke=WARN, sw=3); d.text(hx + 55, RY + 100, '熱も通りやすい', 16, WARN, 700, 'middle')
        elif k == 0: d.text(hx + 55, RY + 50, 'ある程度カット', 16, WARN, 700, 'middle')
        else: d.text(hx + 55, RY + 50, '日差しを遮る', 16, WARN, 700, 'middle')
        d.label(400, RY + 7, '屋根材', 420, 175, anchor='middle')
        pbox(d, pts)
        out(f'{s}-{k+1:02d}', d, f'カーポートの屋根材「{title}」のイラスト。{sub}')


# ================= 59 砂利の種類 =================
def gravels():
    s = 'niwa-jari-shurui-tokuchou'
    data = [('白玉砂利', '白くて丸みのある砂利。明るい印象の庭をつくりやすい', ['#f4f2ec'], 'round', ['+明るく上品な印象になる', '+人気が高い種類', '+音（防犯効果）は標準的']),
            ('化粧砂利', '色や形にこだわった装飾用の砂利。デザイン性を重視する場所に', ['#c9b79a', '#9a8f84', '#e2d6c2', '#b48b6a', '#7d8a78'], 'mix', ['+デザイン性が高い', '+色や形状を選べる', '+音（防犯効果）は種類による']),
            ('防犯砂利', '踏むと大きな音が出るよう加工された砂利', ['#8e9497', '#a3a9ab', '#767c80'], 'flat', ['+踏むと大きな音が出やすい', '+玄関まわりなど、防犯目的で使われる', '+見た目の印象は標準的']),
            ('自然石（砕石など）', '角のある形の砂利。価格を抑えやすい', ['#b4b3ac', '#a19f97', '#c4c2ba'], 'angular', ['+ナチュラルな印象', '+価格を比較的抑えやすい', '+駐車場の下地などにも使われる'])]
    for k, (title, sub, cols, shape, pts) in enumerate(data):
        d = base(title, sub); rnd = d.rnd
        x0, y0, w, h = 60, 140, 520, 320
        d.rect(x0, y0, w, h, fill='#dcdbd4', stroke=GREY, sw=2, rx=10)
        d.add(f'<clipPath id="c{k}"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="10"/></clipPath><g clip-path="url(#c{k})">')
        yy = y0 - 10
        while yy < y0 + h + 20:
            xx = x0 - 10 + rnd.uniform(0, 14)
            while xx < x0 + w + 20:
                r = rnd.uniform(13, 20) if shape != 'mix' else rnd.uniform(9, 22); c = rnd.choice(cols)
                if shape in ('round', 'mix') and (shape == 'round' or rnd.random() < .6):
                    d.ellipse(xx, yy, r, r * .78, fill=c, stroke='#9a978c', sw=1.5)
                elif shape == 'flat':
                    d.poly([(xx - r, yy), (xx - r * .4, yy - r * .6), (xx + r * .8, yy - r * .4), (xx + r, yy + r * .3), (xx - r * .2, yy + r * .6)], fill=c, stroke='#5f6467', sw=1.5)
                    d.circle(xx + rnd.uniform(-4, 4), yy, 2.2, fill='#5f6467', stroke='none')
                else:
                    d.poly([(xx - r, yy + r * .3), (xx - r * .5, yy - r * .7), (xx + r * .7, yy - r * .5), (xx + r, yy + r * .2), (xx + r * .1, yy + r * .7)], fill=c, stroke='#7d7b74', sw=1.5)
                xx += r * 1.9
            yy += 26
        d.add('</g>')
        d.text(x0 + w / 2, y0 + h + 30, '上から見たイメージ（粒の大きさ・色は製品によって異なります）', 15, GREY, 500, 'middle')
        # 右：特徴アイコン
        ix = 620
        if k == 2:
            d.path(f'M{ix+90},300 l60,0 q20,0 20,-20 l0,-60 l-40,0 l0,40 l-40,0 q-14,0 -14,20z', fill='#5a6670', stroke=LINE, sw=2)
            for i in range(3): d.path(f'M{ix+200+i*22},{250-i*6} q16,30 0,60', stroke=WARN, sw=3)
            d.text(ix + 150, 360, 'ジャリッ', 26, WARN, 700, 'middle'); d.text(ix + 150, 396, '踏むと大きな音', 19, INK, 700, 'middle')
        elif k == 3:
            d.text(ix + 150, 230, '角のある形', 22, INK, 700, 'middle')
            d.poly([(ix + 90, 320), (ix + 120, 270), (ix + 190, 280), (ix + 210, 330), (ix + 150, 350)], fill='#b4b3ac', stroke=LINE, sw=2.5)
        elif k == 0:
            d.text(ix + 150, 230, '丸みのある白い粒', 22, INK, 700, 'middle'); d.ellipse(ix + 150, 310, 60, 44, fill='#f4f2ec', stroke=LINE, sw=2.5)
        else:
            d.text(ix + 150, 230, '色・形がさまざま', 22, INK, 700, 'middle')
            for i, c in enumerate(cols[:4]): d.ellipse(ix + 80 + i * 46, 310 + (i % 2) * 12, 22, 17, fill=c, stroke=LINE, sw=2)
        pbox(d, pts, y=500, h=126)
        out(f'{s}-{k+1:02d}', d, f'{title}のイラスト。{sub}')


# ================= 62 コンクリート / インターロッキング =================
def conc_inter():
    s = 'concrete-interlocking-chigai'
    for k in range(2):
        d = base(('コンクリート舗装', 'インターロッキング')[k], ('コンクリートを流し込んで固める舗装', 'ブロックを組み合わせて敷き詰める舗装')[k])
        # 上面
        x0, y0, w, h = 60, 140, 400, 300
        if k == 0:
            d.rect(x0, y0, w, h, fill=CONC, stroke=CONC_D, sw=2, rx=4)
            for t in (x0 + w / 2,): d.line(t, y0, t, y0 + h, stroke=CONC_D, sw=4)
            d.path(f'M{x0+250},{y0+40} l20,40 l-14,30 l26,50', stroke='#5f6467', sw=2.5)
            d.label(x0 + 268, y0 + 100, 'ひび割れ', x0 + 330, y0 + 30 + 0, anchor='start')
        else:
            d.rect(x0, y0, w, h, fill='#d8b89a', stroke='#7d5a3e', sw=2, rx=4)
            cols = ['#c79a77', '#b98966', '#d6ae8a', '#a87c5c']
            for r in range(int(h / 30)):
                for c in range(int(w / 60) + 1):
                    xx = x0 + c * 60 - (30 if r % 2 else 0)
                    xa, xb = max(x0, xx), min(x0 + w, xx + 60)
                    if xb - xa > 4: d.rect(xa, y0 + r * 30, xb - xa, 30, fill=cols[(r * 3 + c) % 4], stroke='#7d5a3e', sw=1.5)
            d.rect(x0 + 180, y0 + 120, 60, 30, fill='#efe6da', stroke=WARN, sw=2.5, dash='6 4')
            d.arrow(x0 + 210, y0 + 135, x0 + 300, y0 + 60, color=WARN, sw=3); d.text(x0 + 310, y0 + 54, 'その部分だけ', 17, WARN, 700); d.text(x0 + 310, y0 + 76, '交換しやすい', 17, WARN, 700)
        d.text(x0 + w / 2, y0 + h + 28, '上から見たイメージ', 15, GREY, 500, 'middle')
        # 断面
        X, W, T = 520, 380, 330
        d.soil(X, T, W, 80)
        d.gravel_layer(X, T - 36, W, 36, r=(5, 8), round_=False)
        if k == 0:
            d.rect(X, T - 100, W, 64, fill=CONC, stroke=CONC_D, sw=2); d.line(X + 6, T - 68, X + W - 6, T - 68, stroke=METAL_D, sw=2.5, dash='12 8')
            d.label(X + 100, T - 68, '鉄筋（ワイヤーメッシュ）', X + 190, 170, anchor='middle'); d.label(X + 300, T - 90, 'コンクリート', X + 300, 230, anchor='middle')
        else:
            d.sand(X, T - 60, W, 24)
            xx = X
            while xx < X + W - 2: d.rect(xx, T - 112, 58, 52, fill='#c79a77', stroke='#7d5a3e', sw=2, rx=3); xx += 60
            d.label(X + 90, T - 112, 'ブロック', X + 90, 180, anchor='middle'); d.label(X + 300, T - 48, '砂', X + 320, 240, anchor='middle')
        d.label(X + W - 40, T - 18, '砕石', X + W - 60, T + 50, anchor='middle')
        d.text(X + W / 2, T + 104, '断面の一例', 15, GREY, 500, 'middle')
        pbox(d, (['+耐久性が高く、荷重のかかる駐車場にも適している', '-ひび割れが起きると、部分的な補修が難しい場合がある', '-デザインの幅は比較的限られる（色や仕上げの工夫は可能）'],
                 ['+ブロックの組み合わせで、デザインパターンが豊富', '+一部が破損しても、その部分だけ交換しやすい', '-施工に手間がかかり、費用が高くなる場合がある'])[k], y=500, h=126)
        out(f'{s}-{k+1:02d}', d, ('コンクリート舗装のイラスト。上から見た様子と断面（砕石・鉄筋入りコンクリート）', 'インターロッキングのイラスト。ブロックを組み合わせた上面と断面（砕石・砂・ブロック）')[k])


# ================= 67 門扉 =================
def gates():
    s = 'mon-hi-shurui-erabikata'
    data = [('開き戸タイプ', '最も一般的な門扉。開閉時に前後のスペースが必要', ['+最も一般的で、デザインが豊富', '-開閉時に前後のスペースが必要', '-通行人や駐車している車と干渉しないか確認が必要']),
            ('引き戸タイプ', '横にスライドして開閉する門扉', ['+前後のスペースが限られる場所に向く', '+開閉がスムーズ', '-扉を引き込む横方向のスペースが必要']),
            ('伸縮タイプ', 'アコーディオンのように伸び縮みする門扉', ['+比較的少ないスペースで設置しやすい', '+広い開口にも対応しやすい', '-開閉にやや手間がかかる場合がある'])]
    for k, (title, sub, pts) in enumerate(data):
        d = base(title, sub)
        # 平面図
        x0, y0, w, h = 60, 140, 840, 320
        d.rect(x0, y0, w, h, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=10)
        d.text(x0 + 16, y0 + 30, '上から見たイメージ', 15, GREY, 500)
        wy = y0 + 205
        d.rect(x0 + 20, wy - 10, 220, 20, fill=CONC, stroke=CONC_D, sw=2); d.rect(x0 + w - 240, wy - 10, 220, 20, fill=CONC, stroke=CONC_D, sw=2)
        d.text(x0 + 130, wy + 50, '敷地の外（道路側）', 16, '#6b6e66', 600, 'middle'); d.text(x0 + 130, wy - 30, '敷地の中', 16, '#6b6e66', 600, 'middle')
        gx0, gx1 = x0 + 240, x0 + w - 240  # 開口 360
        for gx in (gx0, gx1): d.rect(gx - 8, wy - 14, 16, 28, fill=METAL_D, stroke=LINE, sw=2)
        if k == 0:
            r = (gx1 - gx0) / 2
            d.path(f'M{gx0},{wy} L{gx0},{wy-r} A{r},{r} 0 0,1 {gx0+r},{wy}z', fill='#f3d9cf', stroke='none', op=.8)
            d.path(f'M{gx1},{wy} L{gx1},{wy-r} A{r},{r} 0 0,0 {gx1-r},{wy}z', fill='#f3d9cf', stroke='none', op=.8)
            d.path(f'M{gx0+r},{wy} A{r},{r} 0 0,0 {gx0},{wy-r}', stroke=WARN, sw=2, dash='8 6'); d.path(f'M{gx1-r},{wy} A{r},{r} 0 0,1 {gx1},{wy-r}', stroke=WARN, sw=2, dash='8 6')
            d.rect(gx0, wy - r, 10, r, fill='#8a7a63', stroke=LINE, sw=2); d.rect(gx1 - 10, wy - r, 10, r, fill='#8a7a63', stroke=LINE, sw=2)
            d.text(gx0 + r, wy - r - 10, '扉が回転するスペースが必要', 18, WARN, 700, 'middle')
            d.text(gx0 + r, wy + 50, '※ 外開きの場合は、道路側にスペースが必要', 16, '#6b6e66', 600, 'middle')
        elif k == 1:
            d.rect(gx0 + 4, wy - 34, gx1 - gx0 - 8, 12, fill='#8a7a63', stroke=LINE, sw=2)
            d.rect(x0 + w - 240, wy - 52, 220, 30, fill='#f3d9cf', stroke='none', op=.9)
            d.arrow(gx0 + 200, wy - 70, gx1 + 160, wy - 70, color=WARN, sw=3)
            d.label(x0 + w - 130, wy - 37, '扉を引き込むスペース', x0 + w - 130, y0 + 40, anchor='middle', color=WARN)
            d.line(gx0, wy - 22, x0 + w - 20, wy - 22, stroke=GREY, sw=2, dash='6 4'); d.text(gx0 + 180, wy + 40, 'レール・ガイドに沿って横にスライド', 16, '#6b6e66', 600, 'middle')
        else:
            for i in range(10):
                xx = gx0 + 6 + i * 9
                d.line(xx, wy - 14, xx + 9, wy + 14 if i % 2 else wy - 14, stroke='#6c757a', sw=2)
            d.path(' '.join(f'{"M" if i == 0 else "L"}{gx0+6+i*9},{wy-14 if i%2==0 else wy+14}' for i in range(12)), stroke=LINE, sw=3)
            d.rect(gx0 + 4, wy - 34, 106, 20, fill='#f3d9cf', stroke='none')
            d.label(gx0 + 55, wy - 24, 'たたむと小さくまとまる', gx0 + 160, y0 + 40, anchor='middle', color=WARN)
            d.arrow(gx0 + 120, wy, gx1 - 20, wy, color=GREEN, sw=3); d.text((gx0 + gx1) / 2 + 40, wy + 40, '伸ばして閉じる', 17, GREEN, 700, 'middle')
        pbox(d, pts, y=486, h=136)
        out(f'{s}-{k+1:02d}', d, f'門扉の{title}を上から見たイラスト。{sub}')


# ================= 69 ブロック =================
def blocks():
    s = 'gaikou-block-shurui-tokuchou'
    data = [('普通コンクリートブロック', '塀の基礎や土留めなど、構造的な役割を担う部分に使う', ['+基礎・土留めなど構造的な役割を担う', '+表面はシンプルな仕上げ（デザイン性は低い）', '-見える部分は化粧ブロックなどで仕上げることが多い']),
            ('化粧ブロック', '表面に模様やテクスチャーを施したブロック', ['+デザイン性が高い', '+塀やアプローチなど、見える部分に使う', '+色や表面の仕上げを選べる']),
            ('擬石ブロック', '自然石のような見た目を再現したブロック', ['+ナチュラルな印象をつくりやすい', '+花壇や装飾に使われる', '+デザイン性が高い（自然な印象）'])]
    for k, (title, sub, pts) in enumerate(data):
        d = base(title, sub); G = 440
        d.rect(0, 120, 960, G - 120, fill=SKY, stroke='none'); ground(d, G)
        if k == 0:
            block_wall(d, 120, G, 560, 228, 120, 57)
            for r in range(4):
                for c in range(5):
                    xx = 120 + c * 120 - (60 if r % 2 else 0)
                    if 120 <= xx and xx + 120 <= 680: pass
            d.label(400, G - 120, '表面はシンプル', 800, 200, anchor='middle')
            d.add('')
            # 単体の図
            bx, by = 740, 300
            d.rect(bx, by, 150, 75, fill=CONC, stroke=LINE, sw=2.5); d.rect(bx + 16, by + 16, 50, 43, fill='#bfc1bb', stroke=CONC_D, sw=2); d.rect(bx + 84, by + 16, 50, 43, fill='#bfc1bb', stroke=CONC_D, sw=2)
            d.text(bx + 75, by + 105, '空洞のあるブロック', 16, INK, 700, 'middle')
        elif k == 1:
            for r in range(4):
                for c in range(6):
                    xx = 120 + c * 120 - (60 if r % 2 else 0); xa, xb = max(120, xx), min(680, xx + 120)
                    if xb - xa < 4: continue
                    y = G - (r + 1) * 57
                    d.rect(xa, y, xb - xa, 57, fill='#e3d6c2', stroke='#a8977c', sw=1.8)
                    for t in range(4): d.line(xa + 6, y + 10 + t * 12, xb - 6, y + 10 + t * 12, stroke='#c9b89c', sw=2)
            d.rect(120, G - 228, 560, 228, fill='none', stroke=LINE, sw=2.5)
            d.label(400, G - 150, '表面に模様・テクスチャー', 800, 200, anchor='middle')
        else:
            rnd = d.rnd
            for r in range(3):
                xx = 160 + (r % 2) * 30
                while xx < 640:
                    w = rnd.uniform(70, 110); y = G - (r + 1) * 56
                    pts_ = [(xx + 4, y + 6), (xx + w * .4, y + 2), (xx + w - 4, y + 5), (xx + w - 2, y + 50), (xx + w * .5, y + 54), (xx + 3, y + 51)]
                    d.poly(pts_, fill=rnd.choice(['#cdbfa6', '#bfae92', '#d8cbb4', '#b6a68a']), stroke='#7d6f58', sw=2); xx += w + 4
            d.add('')
            for i in range(5): d.circle(250 + i * 90, G - 182, 22, fill=LEAF, stroke=LEAF_D, sw=2)
            d.label(330, G - 90, '自然石のような見た目', 800, 200, anchor='middle'); d.text(400, G - 220, '花壇の例', 17, INK, 700, 'middle')
        pbox(d, pts, y=486, h=136)
        out(f'{s}-{k+1:02d}', d, f'{title}のイラスト。{sub}')


if __name__ == '__main__':
    import sys, os, json
    for f in (open_close, mekakushi, paving, decks, carports, roofs, gravels, conc_inter, gates, blocks): f()
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
