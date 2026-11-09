"""住宅設備・リフォーム（No.101〜133）の種類・仕組み・症状イラスト（4:3／1:1）。本文の記述だけを描く。"""
from scene import *
import math

OUT = {}
def out(name, d, alt): OUT[name] = (d, alt)


def base(title, sub, ratio='4:3'):
    d = D(ratio); d.header(title, sub, 30); return d


def pbox(d, items, h=None):
    h = h or 40 + 36 * len(items) - 8
    y = d.H - h - 24
    d.rect(30, y, d.W - 60, h, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12)
    points(d, 54, y + 38, items, 19, 36)
    return y


def floor(d, y, x=0, w=None):
    w = w or d.W; d.rect(x, y, w, 10, fill='#c9b79a', stroke=LINE, sw=2)


# ===================== 101 エコキュートの交換サイン =====================
def ecocute_signs():
    s = 'ecocute-jumyou'
    def tank(d, x, y, h=330):
        d.rect(x, y, 170, h, fill='#eef0ec', stroke=LINE, sw=2.5, rx=14); d.rect(x + 20, y + 30, 130, 14, fill='#d9dcd3', stroke='none', rx=7)
        d.text(x + 85, y + h - 20, '貯湯タンク', 17, INK, 700, 'middle')
    def hp(d, x, y):
        d.rect(x, y, 230, 170, fill='#eef0ec', stroke=LINE, sw=2.5, rx=8); d.circle(x + 80, y + 85, 58, fill='#e2e6e3', stroke=LINE, sw=2)
        for k in range(4): d.line(x + 40 + k * 26, y + 40, x + 40 + k * 26, y + 130, stroke=GREY, sw=2)
        d.text(x + 115, y + 200, 'ヒートポンプユニット', 17, INK, 700, 'middle')
    # 1 エラー表示
    d = base('エラー表示が頻繁に出る', 'リモコンにエラー表示が繰り返し出るようになった')
    d.rect(300, 150, 360, 300, fill='#f3f1ea', stroke=LINE, sw=3, rx=24)
    d.rect(340, 190, 280, 140, fill='#1f2a24', stroke=LINE, sw=2, rx=8); d.text(480, 278, 'E-000', 54, '#ff8a70', 700, 'middle')
    d.text(480, 222, 'エラー', 20, '#ff8a70', 700, 'middle')
    for k in range(3): d.rect(350 + k * 95, 360, 75, 50, fill=WHITE, stroke=LINE, sw=2, rx=10)
    d.text(480, 482, '※ 表示の形式・コードは機種によって異なります', 16, GREY, 500, 'middle')
    pbox(d, ['-エラー表示が頻繁に出る', '-お湯の温度が設定より低い・お湯切れが早い', '+取扱説明書でエラー内容を確認し、早めに業者へ相談'])
    out(f'{s}-01', d, 'エコキュートの交換サイン：リモコンにエラー表示が頻繁に出るイラスト')
    # 2 水漏れ
    d = base('タンクや配管から水漏れがある', '放置すると床下や周囲への浸水被害が広がるおそれ')
    G = 520; ground(d, G, fill='#d3d5cf'); tank(d, 360, G - 340)
    for k in range(3): d.line(400 + k * 45, G, 400 + k * 45, G + 0, stroke=LINE)
    d.path(f'M530,{G-60} h80 v40', stroke=METAL_D, sw=10); d.path(f'M530,{G-100} h120 v80', stroke=METAL_D, sw=10)
    for k in range(4): d.path(f'M{606+k*3},{G-12+k*0} q4,10 0,16 q-6,-4 0,-16z', fill=WATER, stroke=WATER_D, sw=1.5)
    d.ellipse(600, G + 12, 90, 10, fill=WATER, stroke=WATER_D, sw=2)
    d.label(610, G - 20, '配管・タンクまわりの水漏れ', 700, 230, anchor='middle', color=WARN)
    pbox(d, ['-タンクや配管から水が漏れている', '-放置すると床下や周囲に浸水被害が広がる可能性', '+異常に気づいたら、早めに専門業者へ相談'])
    out(f'{s}-02', d, 'エコキュートの交換サイン：貯湯タンクの配管まわりから水漏れしているイラスト')
    # 3 異音
    d = base('ユニットから異音がする', 'タンクユニットやヒートポンプユニットから、普段と違う音がする')
    G = 520; ground(d, G, fill='#d3d5cf'); hp(d, 200, G - 220); tank(d, 560, G - 340)
    for k in range(3): d.path(f'M{450+k*22},{G-190-k*6} q18,30 0,60', stroke=WARN, sw=3)
    for k in range(3): d.path(f'M{750+k*22},{G-280-k*6} q18,30 0,60', stroke=WARN, sw=3)
    d.text(500, 230, 'ゴー', 30, WARN, 700, 'middle'); d.text(820, 200, 'カタカタ', 26, WARN, 700, 'middle')
    pbox(d, ['-ユニットから普段と違う音がする', '-電気代が以前より高い（効率の低下が考えられる）', '+部品の供給が終了している場合は、修理ではなく交換が必要'])
    out(f'{s}-03', d, 'エコキュートの交換サイン：ヒートポンプユニットや貯湯タンクから異音がするイラスト')


# ===================== 103 食洗機 =====================
def dishwasher():
    s = 'dishwasher-kouzuke'
    def counter(d, y=360):
        d.rect(80, y, 800, 26, fill='#e9e4d8', stroke=LINE, sw=2.5); d.rect(100, y + 26, 760, 220, fill='#f4f1ea', stroke=LINE, sw=2.5)
        d.rect(360, y - 6, 160, 20, fill='#c9ccc6', stroke=LINE, sw=2)  # sink rim
        d.path(f'M440,{y-6} v-90 q0,-20 30,-20 h40', stroke=METAL_D, sw=8)  # faucet
    for k in range(2):
        d = base(('ビルトイン型', '卓上型')[k], ('キッチンの収納部分に組み込んで設置するタイプ', 'キッチンカウンターの上に置いて使うタイプ')[k])
        d.add('<g transform="translate(0,-70)">'); counter(d)
        if k == 0:
            d.rect(560, 392, 240, 186, fill='#d6dade', stroke=LINE, sw=2.5, rx=4); d.rect(575, 404, 210, 20, fill='#b8bec3', stroke=LINE, sw=1.5)
            d.rect(640, 430, 80, 10, fill=METAL_D, stroke='none', rx=5); d.text(680, 520, '食洗機', 22, INK, 700, 'middle')
            for i in range(3): d.rect(130 + i * 140, 400, 120, 170, fill='#ede9df', stroke=LINE, sw=1.5)
            d.path('M600,560 q-40,0 -90,0 l-60,0', stroke=WATER_D, sw=4, dash='8 6'); d.text(470, 552, '給水・排水', 16, WATER_D, 700, 'middle')
            d.rect(820, 520, 30, 40, fill=WHITE, stroke=LINE, sw=2, rx=4); d.text(835, 600, '電源', 16, INK, 700, 'middle')
            d.label(680, 410, '収納スペースに組み込む', 700, 200, anchor='middle')
            d.add('</g>'); pbox(d, ['+見た目がすっきりする', '-工事の規模が大きい（給排水・電源の工事が必要な場合）', '-引っ越し時の持ち出しは基本的にできない'])
        else:
            d.rect(600, 220, 200, 140, fill='#d6dade', stroke=LINE, sw=2.5, rx=8); d.rect(615, 236, 170, 70, fill='#bfc6cc', stroke=LINE, sw=1.5, rx=4)
            d.text(700, 340, '食洗機', 20, INK, 700, 'middle')
            d.circle(470, 270, 10, fill='#e9b949', stroke=LINE, sw=2)
            d.path('M478,276 C540,300 560,320 600,320', stroke=WATER_D, sw=4); d.path('M600,345 C540,360 470,350 450,354', stroke=GREY, sw=4)
            d.label(470, 270, '分岐水栓（給水）', 300, 200, anchor='middle'); d.label(520, 352, '排水ホースでシンクへ', 300, 300, anchor='middle')
            d.add('</g>'); pbox(d, ['+工事が少なく済む場合が多い（賃貸でも比較的対応しやすい）', '+引っ越し時に持ち出しできる', '-カウンターのスペースを使う'])
        out(f'{s}-{k+1:02d}', d, ('ビルトイン型食洗機の設置イメージ。キッチン下の収納に組み込み、給排水と電源を接続', '卓上型食洗機の設置イメージ。カウンターに置き、分岐水栓から給水して排水ホースでシンクへ流す')[k])


# ===================== 105 トイレ =====================
def toilets():
    s = 'tankless-toilet-tank-hikaku'
    for k in range(2):
        d = base(('タンクレストイレ', 'タンク式トイレ')[k], ('水道の水圧を利用して、直接洗浄する仕組み', 'タンクに水をためてから洗浄する仕組み')[k])
        G = 500; floor(d, G); d.rect(780, 140, 30, G - 140, fill='#e8e2d6', stroke=LINE, sw=2)
        d.path(f'M500,{G} C490,{G-50} 470,{G-80} 440,{G-110} L720,{G-110} L740,{G} Z', fill=WHITE, stroke=LINE, sw=2.5)
        d.path(f'M380,{G-150} Q380,{G-104} 450,{G-100} L730,{G-100} L760,{G-150} Z', fill=WHITE, stroke=LINE, sw=2.5)
        d.rect(370, G - 168, 330, 18, fill='#f4f4f2', stroke=LINE, sw=2.5, rx=8)
        d.rect(680, G - 200 if k == 0 else G - 175, 100, 50 if k == 0 else 25, fill='#f1f1ef', stroke=LINE, sw=2.5, rx=10)
        d.path(f'M850,{G-60} h-40', stroke=METAL_D, sw=8)
        if k == 0:
            
            d.arrow(880, G - 60, 812, G - 60, color=WATER_D, sw=4); d.text(860, G - 80, '水道', 18, WATER_D, 700)
            d.arrow(690, G - 140, 520, G - 125, color=WATER_D, sw=3)
            d.label(730, G - 180, 'タンクがない（水道の水圧で洗浄）', 520, 180, anchor='middle')
            pbox(d, ['+すっきりしたデザインで、空間を広く見せやすい', '+タンク部分の掃除が不要', '-本体価格は高め／一定の水圧が必要／断水時は対応が難しい場合も'], 152)
        else:
            d.rect(660, G - 340, 120, 165, fill='#f1f1ef', stroke=LINE, sw=2.5, rx=10); d.rect(676, G - 310, 88, 100, fill=WATER, stroke='none', op=.6)
            d.text(720, G - 326, 'タンク', 18, INK, 700, 'middle')
            d.arrow(880, G - 60, 812, G - 60, color=WATER_D, sw=4); d.path(f'M790,{G-60} v-200 h-10', stroke=WATER_D, sw=3, dash='6 5')
            d.label(720, G - 260, 'タンクに水をためてから流す', 480, 180, anchor='middle')
            pbox(d, ['+価格を抑えやすい', '+断水時に手動で流せる場合がある', '-タンク部分のスペースと掃除が必要'], 152)
        out(f'{s}-{k+1:02d}', d, ('タンクレストイレを横から見たイラスト。水道の水圧で直接洗浄する', 'タンク式トイレを横から見たイラスト。タンクに水をためてから洗浄し、断水時は手動で流せる場合がある')[k])


# ===================== 106 IH / ガス =====================
def cookers():
    s = 'ih-gas-conro-hikaku'
    for k in range(2):
        d = base(('IHクッキングヒーター', 'ガスコンロ')[k], ('電磁誘導で、鍋そのものを発熱させる', 'ガスを燃やした火で、鍋を加熱する')[k])
        d.rect(140, 380, 680, 30, fill='#2e3236' if k == 0 else '#c9ccc6', stroke=LINE, sw=2.5, rx=4)
        d.rect(160, 410, 640, 150, fill='#f4f1ea', stroke=LINE, sw=2.5)
        d.path('M330,380 L330,300 Q330,280 350,280 L610,280 Q630,280 630,300 L630,380', fill='#9aa3a8', stroke=LINE, sw=2.5)
        d.rect(610, 300, 90, 16, fill=METAL_D, stroke=LINE, sw=2, rx=6)
        if k == 0:
            for r in range(5): d.ellipse(480, 430 + 0, 160 - r * 26, 14 - r * 2, fill='none', stroke='#e9b949', sw=3)
            for r in range(3): d.path(f'M{380+r*100},350 q10,-12 0,-24 q-10,-12 0,-24', stroke=WARN, sw=3)
            d.label(480, 400, 'フラットな天板（下にコイル）', 300, 210, anchor='middle'); d.label(560, 330, '鍋そのものが発熱', 700, 210, anchor='middle', color=WARN)
            pbox(d, ['+フラットで掃除がしやすい', '+火を使わないため安全性が高い', '-IH対応の鍋が必要／停電時は使用できない'])
        else:
            for x in (360, 600):
                d.line(x, 380, x, 350, stroke=LINE, sw=6)
            for i in range(9):
                fx = 380 + i * 25
                d.path(f'M{fx},378 q-8,-16 0,-30 q8,14 0,30z', fill='#4f8fd8', stroke='#2b5f9a', sw=1.5)
            d.label(360, 360, '五徳', 220, 230, anchor='middle'); d.label(480, 360, 'ガスの火で加熱', 700, 210, anchor='middle', color=WARN)
            pbox(d, ['+ほとんどの鍋が使える', '+停電時も使用できる場合がある（ガスの供給状況による）', '-五徳の掃除が必要／火の取り扱いに注意'])
        out(f'{s}-{k+1:02d}', d, ('IHクッキングヒーターの仕組みのイラスト。電磁誘導で鍋そのものが発熱する', 'ガスコンロの仕組みのイラスト。五徳の上の鍋をガスの火で加熱する')[k])


# ===================== 107 スマートキー =====================
def smartkeys():
    s = 'genkan-smartkey-kouzuke'
    data = [('後付けタイプ（サムターン回転型）', '既存の鍵の内側のつまみ（サムターン）に取り付けて、自動で施錠・解錠', ['+工事は基本的に不要で、費用を抑えやすい', '-既存の鍵の形状・サイズによっては対応しない', '+電池切れに備えて、物理鍵でも開けられるものを']),
            ('電子錠一体型', 'ドアの鍵部分そのものを電子錠に交換', ['+暗証番号・カードキーなど開け方を選べる', '-工事が必要な場合が多い', '-費用は高くなる傾向']),
            ('工事不要タイプ', '粘着テープなどで取り付け、既存の鍵の操作を自動化', ['+工事不要で取り付けやすい', '+賃貸でも検討しやすい（原状回復できるか確認）', '-ドアや鍵の形状によっては取り付けられない'])]
    for k, (title, sub, pts) in enumerate(data):
        d = base(title, sub)
        d.rect(300, 130, 360, 420, fill='#8a7a63', stroke=LINE, sw=3, rx=4); d.rect(320, 150, 320, 380, fill='#9c8b72', stroke='#6f6150', sw=1.5)
        d.text(480, 580, ('ドアの内側（室内側）', 'ドアの外側', 'ドアの内側（室内側）')[k], 16, GREY, 600, 'middle')
        d.rect(560, 290, 40, 120, fill=METAL, stroke=LINE, sw=2, rx=6)
        if k == 0:
            d.rect(520, 300, 110, 150, fill='#f3f1ea', stroke=LINE, sw=2.5, rx=14); d.circle(575, 360, 26, fill='#e3e6e2', stroke=LINE, sw=2)
            d.rect(568, 336, 14, 48, fill=METAL_D, stroke='none', rx=4)
            d.label(630, 360, 'サムターンの上にかぶせて取り付け', 760, 230, anchor='middle')
            d.curved_arrow(540, 330, 575, 300, 610, 330, color=GREEN)
        elif k == 1:
            d.rect(510, 260, 120, 210, fill='#2e3236', stroke=LINE, sw=2.5, rx=10)
            for r in range(4):
                for c in range(3): d.rect(528 + c * 30, 290 + r * 34, 24, 24, fill='#5b6670', stroke='none', rx=5)
            d.label(630, 360, '鍵部分を電子錠に交換', 770, 230, anchor='middle')
        else:
            d.rect(530, 300, 90, 130, fill='#f3f1ea', stroke=LINE, sw=2.5, rx=12)
            d.rect(530, 418, 90, 10, fill='#e9b949', stroke='#a37d1c', sw=1.5); d.rect(530, 300, 90, 8, fill='#e9b949', stroke='#a37d1c', sw=1.5)
            d.label(620, 424, '粘着テープなどで固定', 770, 470, anchor='middle')
            d.label(575, 360, '既存の鍵の操作を自動化', 770, 230, anchor='middle')
        for i, (ic, t) in enumerate((('スマホ', 'スマホ'), ('暗証番号', '暗証番号'), ('カード', 'カード'))):
            pass
        pbox(d, pts)
        out(f'{s}-{k+1:02d}', d, f'玄関スマートキー「{title}」の取り付けイメージ。{sub}')


# ===================== 108 宅配ボックス =====================
def boxes():
    s = 'takuhaibox-kodate-erabikata'
    data = [('据置型', '地面に置いて設置するタイプ', ['+工事不要で設置しやすい', '+容量の大きいものも選びやすい', '-持ち去り防止のため、地面などにしっかり固定']),
            ('埋込型（門柱一体型など）', '門柱に組み込んで設置するタイプ', ['+すっきりした見た目になる', '+郵便受けと一体になったものも多い', '-門柱の工事を伴う場合がある']),
            ('壁掛け型', '外壁などに取り付けるタイプ', ['+スペースが限られる場所でも設置しやすい', '-容量は小さめのものが多い', '-壁にしっかり固定する必要がある'])]
    for k, (title, sub, pts) in enumerate(data):
        d = base(title, sub); G = 500
        d.rect(0, 120, 960, G - 120, fill=SKY, stroke='none'); ground(d, G, fill='#d3d5cf')
        if k == 0:
            d.rect(560, 150, 400, G - 150, fill=WALL, stroke=LINE, sw=2.5); d.rect(640, G - 220, 110, 220, fill='#c9a06b', stroke=LINE, sw=2)
            d.rect(380, G - 230, 140, 230, fill='#4a5056', stroke=LINE, sw=2.5, rx=6); d.rect(395, G - 210, 110, 150, fill='#5b626a', stroke=LINE, sw=1.5, rx=4)
            d.rect(470, G - 180, 20, 30, fill='#e9b949', stroke=LINE, sw=1.5, rx=3)
            for x in (390, 510): d.line(x, G, x, G + 20, stroke=METAL_D, sw=4)
            d.label(450, G + 10, 'アンカー等で地面に固定', 250, 440, anchor='middle')
            d.label(450, G - 120, '宅配ボックス', 260, 200, anchor='middle')
        elif k == 1:
            d.rect(300, G - 330, 300, 330, fill='#d8d2c4', stroke=LINE, sw=2.5)
            d.rect(340, G - 300, 220, 60, fill='#4a5056', stroke=LINE, sw=2, rx=4); d.text(450, G - 262, '郵便受け', 17, WHITE, 700, 'middle')
            d.rect(340, G - 220, 220, 170, fill='#4a5056', stroke=LINE, sw=2, rx=4); d.text(450, G - 128, '宅配ボックス', 18, WHITE, 700, 'middle')
            d.rect(380, G - 360, 140, 30, fill='#e9e4d8', stroke=LINE, sw=2); d.text(450, G - 338, '表札', 15, INK, 700, 'middle')
            d.label(600, G - 150, '門柱に組み込む', 760, 220, anchor='middle')
        else:
            d.rect(0, 140, 960, G - 140, fill=WALL, stroke='none'); d.line(0, 140, 960, 140, stroke=LINE, sw=2)
            d.rect(380, G - 300, 180, 150, fill='#4a5056', stroke=LINE, sw=2.5, rx=6); d.rect(395, G - 285, 150, 90, fill='#5b626a', stroke=LINE, sw=1.5, rx=4)
            for (x, y) in ((392, G - 290), (548, G - 290), (392, G - 160), (548, G - 160)): d.circle(x, y, 4, fill=METAL, stroke=LINE, sw=1)
            d.label(560, G - 225, '外壁に固定', 760, 220, anchor='middle')
        pbox(d, pts)
        out(f'{s}-{k+1:02d}', d, f'戸建て用宅配ボックス「{title}」の設置イメージ。{sub}')


# ===================== 112 在来浴室 / ユニットバス =====================
def baths():
    s = 'ofuro-reform-hiyou'
    for k in range(2):
        d = base(('在来浴室', 'ユニットバス')[k], ('タイルなどを使って現場でつくられた浴室', '壁・床・浴槽があらかじめ一体化した工場生産の浴室')[k])
        X0, Y0, W0, H0 = 200, 140, 560, 380
        if k == 0:
            for r in range(int(H0 / 30)):
                for c in range(int(W0 / 40)): d.rect(X0 + c * 40, Y0 + r * 30, 40, 30, fill='#dfe7ea', stroke='#a9b6bb', sw=1)
            d.rect(X0, Y0, W0, H0, fill='none', stroke=LINE, sw=3)
            d.rect(X0 + 300, Y0 + 210, 260, 170, fill='#cfe1ea', stroke=LINE, sw=2.5)
            d.rect(X0, Y0 + H0, W0, 30, fill='#9aa09a', stroke=LINE, sw=2); d.text(X0 + W0 / 2, Y0 + H0 + 21, '防水層・下地（現場で施工）', 16, WHITE, 700, 'middle')
            d.label(X0 + 120, Y0 + 100, 'タイル張りの壁', X0 - 40, Y0 + 30 - 10, anchor='middle')
            pts = ['-ユニットバスへの変更は、解体・防水工事が必要', '-工期が長めで、費用が高くなりやすい', '-解体時に下地の腐食が見つかり、追加費用が出ることも']
        else:
            d.rect(X0, Y0, W0, H0, fill='#f4f6f6', stroke=LINE, sw=3, rx=18)
            for c in range(1, 4): d.line(X0 + c * W0 / 4, Y0, X0 + c * W0 / 4, Y0 + H0 - 30, stroke='#d0d6d8', sw=2)
            d.path(f'M{X0+280},{Y0+H0-30} h{W0-300} q0,-150 -40,-160 h-{W0-340} q-20,10 -20,160z', fill='#cfe1ea', stroke=LINE, sw=2.5)
            d.rect(X0, Y0 + H0 - 30, W0, 30, fill='#e4e8ea', stroke=LINE, sw=2, rx=6)
            d.text(X0 + 140, Y0 + 200, '壁パネル', 18, INK, 700, 'middle'); d.text(X0 + 140, Y0 + H0 - 9, '床パネル', 16, INK, 700, 'middle'); d.text(X0 + 430, Y0 + 300, '浴槽', 18, INK, 700, 'middle')
            d.label(X0 + W0, Y0 + 30, '工場でつくった部材を組み立てる', X0 + W0 - 100, Y0 - 0 + 14 - 0, anchor='middle')
            pts = ['+ユニットバス→ユニットバスの交換は、工期が短め', '+費用を抑えやすい', '+グレードで断熱・保温性能やオプションが変わる']
        pbox(d, pts)
        out(f'{s}-{k+1:02d}', d, ('在来浴室のイラスト。タイル張りで、防水層や下地を現場で施工する', 'ユニットバスのイラスト。壁・床・浴槽が一体化した工場生産の浴室')[k])


# ===================== 114 外壁の塗り替えサイン（1:1） =====================
def wall_signs():
    s = 'gaiheki-tosou-hiyou-souba'
    def wallpanel(d, x=80, y=150, w=640, h=420, col='#e6e1d6'):
        d.rect(x, y, w, h, fill=col, stroke=LINE, sw=2.5)
    data = ['色あせ・チョーキング', '外壁のひび割れ', 'コーキングの剥がれ・劣化', '塗膜の剥がれ・膨れ']
    for k, t in enumerate(data):
        d = D('1:1'); d.text(40, 66, '塗り替えサイン', 22, GREEN, 700); d.text(40, 112, t, 34, INK, 700)
        if k == 0:
            wallpanel(d, col='#ebe8e1'); d.rect(80, 150, 320, 420, fill='#d9cfbd', stroke='none'); d.text(240, 600, '元の色', 17, GREY, 600, 'middle'); d.text(560, 600, '色あせた部分', 17, GREY, 600, 'middle')
            d.person_hand(430, 400, -10)
            for _ in range(30): d.circle(d.rnd.uniform(440, 500), d.rnd.uniform(395, 425), 2.2, fill=WHITE, stroke='#c9c6bd', sw=.6)
            d.label(470, 410, '触ると白い粉がつく', 520, 300, anchor='middle', color=WARN)
        elif k == 1:
            wallpanel(d); d.path('M300,150 l20,60 l-16,50 l34,70 l-10,60 l28,80 l-12,100', stroke='#5f6467', sw=3)
            d.path('M560,300 l-40,60 l10,40', stroke='#5f6467', sw=2)
            d.label(330, 330, 'ひび割れ', 560, 220, anchor='middle', color=WARN)
        elif k == 2:
            wallpanel(d, w=290); d.rect(410, 150, 310, 420, fill='#e6e1d6', stroke=LINE, sw=2.5)
            d.rect(370, 150, 40, 420, fill='#bfbab0', stroke=LINE, sw=1.5)
            d.rect(372, 150, 36, 200, fill='#f0eee8', stroke='none'); d.path('M372,350 l8,40 l-6,40 l10,50 l-8,90', stroke='#5f6467', sw=2.5)
            d.rect(380, 380, 20, 190, fill='#e4e1da', stroke='#8f8b80', sw=1.5)
            d.label(390, 450, '目地のコーキングが剥がれ・痩せ', 400, 640 - 10, anchor='middle', color=WARN)
        else:
            wallpanel(d)
            for (x, y, r) in ((260, 300, 40), (480, 420, 30)): d.circle(x, y, r, fill='#f2efe8', stroke='#9e988a', sw=2); d.ellipse(x - r * .3, y - r * .3, r * .3, r * .2, fill=WHITE, stroke='none')
            d.path('M520,220 l60,-10 l20,40 l-30,30 l-50,-10z', fill='#cfc7b6', stroke='#8f8b80', sw=2)
            d.label(260, 300, '膨れ', 200, 640 - 10, anchor='middle', color=WARN); d.label(560, 240, '塗膜の剥がれ', 560, 640 - 10, anchor='middle', color=WARN)
        d.rect(40, 680, 720, 80, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=12)
        d.text(60, 728, 'このサインが見られたら、塗り替えを検討するタイミング', 20, INK, 700)
        out(f'{s}-{k+1:02d}', d, f'外壁の塗り替えサイン「{t}」のイラスト')


# ===================== 115 屋根の工法 =====================
def roofs():
    s = 'yane-reform-kouhou-hikaku'
    def slope(d, y_off=0):
        return lambda x: 520 - (x - 120) * .38 + y_off
    data = [('屋根塗装', '既存の屋根材の上に塗装し、防水性を回復させる', ['+屋根材自体の劣化が少ない（軽度の劣化）場合に', '+工期は短め', '+費用を抑えやすい']),
            ('カバー工法（重ね葺き）', '既存の屋根の上に、新しい屋根材を重ねて設置する', ['+中程度の劣化に', '+解体作業が少なく、工期を短縮しやすい', '+費用・工期は中程度']),
            ('葺き替え', '既存の屋根材を撤去し、新しい屋根材に入れ替える', ['+下地まで劣化している場合に', '+下地から補修できる', '-工期は長め、費用は高くなりやすい'])]
    for k, (title, sub, pts) in enumerate(data):
        d = base(title, sub)
        x0, x1 = 120, 840
        def band(off, th, fill, stroke, dash=None, op=1):
            pts_ = [(x0, 520 - off), (x1, 520 - off - (x1 - x0) * .38), (x1, 520 - off - (x1 - x0) * .38 - th), (x0, 520 - off - th)]
            d.poly(pts_, fill=fill, stroke=stroke, sw=2, op=op)
            if dash: d.path(f'M{x0},{520-off-th} L{x1},{520-off-(x1-x0)*.38-th}', stroke=stroke, sw=2, dash=dash)
        band(0, 22, '#d8c39a', WOOD_D)  # 野地板
        for i in range(6): d.rect(x0 + 30 + i * 125, 520 - (30 + i * 125) * .38, 22, 34, fill='#b88850', stroke=WOOD_D, sw=1.5)
        band(22, 6, '#3b3f3a', '#3b3f3a')  # ルーフィング
        if k == 0:
            band(28, 20, '#8d9497', LINE); band(48, 6, '#5d7d9a', '#3f5d78')
            d.label(500, 520 - 51 - (500 - x0) * .38, '塗装（新しい塗膜）', 600, 160, anchor='middle', color=GREEN)
            d.label(300, 520 - 38 - (300 - x0) * .38, '既存の屋根材', 250, 200, anchor='middle')
        elif k == 1:
            band(28, 20, '#8d9497', LINE); band(48, 6, '#3b3f3a', '#3b3f3a'); band(54, 18, '#5d7d9a', '#3f5d78')
            d.label(560, 520 - 63 - (560 - x0) * .38, '新しい屋根材', 650, 150, anchor='middle', color=GREEN)
            d.label(330, 520 - 38 - (330 - x0) * .38, '既存の屋根材（残す）', 260, 200, anchor='middle')
        else:
            band(28, 20, '#5d7d9a', '#3f5d78')
            d.label(500, 520 - 38 - (500 - x0) * .38, '新しい屋根材', 620, 160, anchor='middle', color=GREEN)
            for i in range(3): d.rect(560 + i * 60, 200 - i * 8, 50, 14, fill='#8d9497', stroke=LINE, sw=1.5, op=.7)
            d.text(620, 250, '既存の屋根材は撤去', 17, WARN, 700, 'middle')
            d.label(300, 520 - 11 - (300 - x0) * .38, '下地から補修できる', 240, 220, anchor='middle', color=GREEN)
        d.text(x1, 140, '断面イメージ', 15, GREY, 500, 'end')
        pbox(d, pts)
        out(f'{s}-{k+1:02d}', d, f'屋根リフォームの「{title}」の断面イラスト。{sub}')


# ===================== 117 / 132 窓 =====================
def window_section(d, k):
    """k=0 内窓, 1 窓交換（カバー工法）。上から見た断面"""
    Y = 330
    d.rect(80, Y - 60, 200, 120, fill='#e8e2d6', stroke=LINE, sw=2); d.rect(680, Y - 60, 200, 120, fill='#e8e2d6', stroke=LINE, sw=2)
    d.text(480, 200, '屋外', 20, '#6b6e66', 700, 'middle'); d.text(480, 500, '室内', 20, '#6b6e66', 700, 'middle')
    if k == 0:
        d.rect(280, Y - 40, 400, 20, fill=GLASS, stroke=LINE, sw=2); d.rect(280, Y - 50, 16, 40, fill=METAL_D, stroke=LINE, sw=1.5); d.rect(664, Y - 50, 16, 40, fill=METAL_D, stroke=LINE, sw=1.5)
        d.rect(280, Y + 30, 400, 20, fill=GLASS, stroke=LINE, sw=2); d.rect(280, Y + 22, 16, 36, fill='#f3f1ea', stroke=LINE, sw=1.5); d.rect(664, Y + 22, 16, 36, fill='#f3f1ea', stroke=LINE, sw=1.5)
        d.rect(300, Y - 18, 360, 46, fill='#dff0f7', stroke='none', op=.6); d.text(480, Y + 12, '空気層', 18, WATER_D, 700, 'middle')
        d.label(620, Y - 30, '既存の窓（外窓）', 760, 230, anchor='middle'); d.label(620, Y + 40, '内窓（追加する窓）', 760, 440, anchor='middle', color=GREEN)
    else:
        d.rect(280, Y - 20, 400, 22, fill=GLASS, stroke=LINE, sw=2)
        for x in (280, 662): d.rect(x, Y - 40, 18, 60, fill='#9aa3a8', stroke=LINE, sw=1.5)
        for x in (298, 640): d.rect(x, Y - 46, 22, 72, fill=GREEN, stroke=LINE, sw=1.5)
        d.rect(320, Y - 16, 320, 16, fill='#cfe1ea', stroke=LINE, sw=1.5); d.line(320, Y - 8, 640, Y - 8, stroke=WATER_D, sw=1.5, dash='6 4')
        d.label(289, Y - 40, '既存の枠', 200, 230, anchor='middle'); d.label(651, Y - 40, '新しい高断熱サッシ', 760, 230, anchor='middle', color=GREEN)
        d.text(480, Y + 80, '既存の枠に新しい枠をかぶせる＝壁を壊さずに交換できる場合がある', 17, INK, 600, 'middle')


def windows():
    s = 'mado-dannetsu-reform-hiyou'
    for k in range(2):
        d = base(('内窓の設置', '窓交換（カバー工法）')[k], ('既存の窓の内側に、もう1枚窓を追加する', 'サッシ全体を高断熱性能のものに交換する')[k])
        window_section(d, k); d.text(880, 532, '上から見た断面イメージ', 15, GREY, 500, 'end')
        pbox(d, (['+窓と窓の間の空気層が断熱に役立つ（実質的に二重窓）', '+工事が比較的簡単で、費用を抑えやすい', '+国の補助事業の対象になることが多い'],
                 ['+サッシ全体を高断熱のものに交換できる', '+カバー工法なら壁を壊さずに交換できる場合がある', '-工事の規模は中程度、費用は中程度〜高め'])[k])
        out(f'{s}-{k+1:02d}', d, ('内窓の設置を上から見た断面図。既存の窓の内側に窓を追加し、間の空気層で断熱する', '窓交換（カバー工法）を上から見た断面図。既存の枠に新しい高断熱サッシをかぶせる')[k])
    s = 'sensenteki-mado-renovation2026'
    d = base('内窓の設置', '既存の窓の内側に新しい窓を取り付ける工事（補助の対象）')
    window_section(d, 0); d.text(880, 532, '上から見た断面イメージ', 15, GREY, 500, 'end')
    pbox(d, ['+比較的短時間で施工しやすい', '+補助額は窓の性能区分とサイズで決まる', '+申請は工事を行う登録事業者が行う'])
    out(f'{s}-01', d, '先進的窓リノベ事業の対象となる内窓の設置を上から見た断面図')
    d = base('補助の対象となる主な窓工事', '先進的窓リノベ2026事業（窓の断熱性能を高める工事）')
    items = [('内窓の設置', '既存の窓の内側に追加'), ('外窓の交換', 'カバー工法・はつり工法'), ('ガラスの交換', '断熱性の高いガラスへ')]
    for i, (t, sub) in enumerate(items):
        x = 50 + i * 295; d.rect(x, 140, 270, 360, fill=WHITE, stroke='#d9dcd3', sw=1.5, rx=14)
        d.rect(x + 55, 190, 160, 180, fill=GLASS, stroke=LINE, sw=2.5); d.line(x + 135, 190, x + 135, 370, stroke=LINE, sw=2)
        if i == 0: d.rect(x + 40, 178, 190, 204, fill='none', stroke=GREEN, sw=5, rx=4)
        elif i == 1: d.rect(x + 55, 190, 160, 180, fill='none', stroke=GREEN, sw=7)
        else: d.rect(x + 63, 198, 64, 164, fill='#bfe0c9', stroke=GREEN, sw=3); d.rect(x + 143, 198, 64, 164, fill='#bfe0c9', stroke=GREEN, sw=3)
        d.text(x + 135, 420, t, 22, INK, 700, 'middle'); d.text(x + 135, 456, sub, 16, '#4a4d46', 600, 'middle')
    pbox(d, ['+これらと同時に行う高断熱ドアへの交換が対象になる場合も（単独は対象外の場合あり）', '+補助額・条件は年度で変わるため、公式サイトで確認'])
    out(f'{s}-02', d, '先進的窓リノベ2026事業の対象となる主な窓工事（内窓の設置・外窓の交換・ガラスの交換）')


# ===================== 133 給湯省エネ 対象機器 =====================
def kyuto():
    s = 'kyuto-shoene2026'
    data = [('エコキュート', 'ヒートポンプ給湯機：空気の熱でお湯をつくり、タンクにためる'),
            ('ハイブリッド給湯機', 'ヒートポンプとガス給湯器を組み合わせた給湯機'),
            ('エネファーム（家庭用燃料電池）', 'ガスから取り出した水素で発電し、その熱でお湯もつくる')]
    for k, (title, sub) in enumerate(data):
        d = base(title, sub); G = 520; ground(d, G, fill='#d3d5cf')
        def unit(x, w, h, label, fan=False):
            d.rect(x, G - h, w, h, fill='#eef0ec', stroke=LINE, sw=2.5, rx=10)
            if fan: d.circle(x + w / 2 - 20, G - h / 2, min(w, h) * .3, fill='#e2e6e3', stroke=LINE, sw=2)
            d.text(x + w / 2, G + 34, label, 17, INK, 700, 'middle')
        if k == 0:
            unit(160, 240, 170, 'ヒートポンプユニット', True); unit(520, 170, 330, '貯湯タンク')
            d.arrow(405, G - 90, 515, G - 90, color=WARN, sw=4); d.text(460, G - 104, 'お湯', 16, WARN, 700, 'middle')
            for i in range(3): d.arrow(70, 260 + i * 34, 150, 290 + i * 26, color=WATER_D, sw=3, head=12)
            d.text(70, 240, '空気の熱', 17, WATER_D, 700)
            pts = ['+電気で空気の熱をくみ上げ、効率よくお湯をつくる', '+事務局に登録された型番の機種が対象']
        elif k == 1:
            unit(130, 220, 160, 'ヒートポンプ', True); unit(420, 150, 280, 'タンク'); unit(640, 140, 200, 'ガス給湯器')
            d.path(f'M690,{G-60} q12,-26 0,-46 q22,12 24,40 q8,-20 4,-40 q24,20 16,46z', fill='#f2a33a', stroke='#b86a1e', sw=2)
            d.arrow(355, G - 80, 415, G - 80, color=WARN, sw=4); d.arrow(575, G - 140, 635, G - 140, color=WARN, sw=4)
            d.text(480, 180, '2つの熱源を組み合わせる', 20, GREEN, 700, 'middle')
            pts = ['+ヒートポンプとガスの2つの熱源でお湯をつくる', '+事務局に登録された型番の機種が対象']
        else:
            unit(180, 220, 300, '燃料電池ユニット'); unit(520, 180, 300, '貯湯ユニット')
            d.text(290, G - 160, 'H₂', 40, '#4f8fb0', 700, 'middle')
            d.arrow(80, G - 60, 175, G - 60, color='#b8683a', sw=4); d.text(80, G - 76, 'ガス', 17, '#8a4a22', 700)
            d.path(f'M290,{G-300} l-24,46 h22 l-18,44', stroke=GOLD, sw=5); d.text(330, G - 320, '発電', 20, '#8a6d16', 700)
            d.arrow(405, G - 120, 515, G - 120, color=WARN, sw=4); d.text(460, G - 134, '発電時の熱', 15, WARN, 700, 'middle')
            pts = ['+つくった電気を家で使い、発電時の熱でお湯もつくる', '+事務局に登録された型番の機種が対象']
        pbox(d, pts)
        out(f'{s}-{k+1:02d}', d, f'給湯省エネ2026事業の対象機器「{title}」の仕組みのイラスト。{sub}')


if __name__ == '__main__':
    import sys, os, json
    for f in (ecocute_signs, dishwasher, toilets, cookers, smartkeys, boxes, baths, wall_signs, roofs, windows, kyuto): f()
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
