"""図解（16:9）— 記事本文の内容と一致させること。数値は本文に書かれているものだけを使う。"""
from lib import *

OUT = {}
def out(name, d, alt): OUT[name] = (d, alt)


def box(d, x, y, w, h, title=None, fill=WHITE, stroke=GREY, tsize=24, tcolor=INK):
    d.rect(x, y, w, h, fill=fill, stroke=stroke, sw=2, rx=12)
    if title: d.text(x + w / 2, y + 40, title, tsize, tcolor, 700, 'middle')


def house(d, x, y, w=260, h=170, roof=70, fill='#f4f1ea'):
    d.poly([(x - 14, y), (x + w / 2, y - roof), (x + w + 14, y)], fill='#7d8a78', stroke=LINE, sw=2.5)
    d.rect(x, y, w, h, fill=fill, stroke=LINE, sw=2.5)
    d.rect(x + w * .38, y + h - 70, 50, 70, fill='#c9a06b', stroke=LINE, sw=2)


# ---------- 102 ヒートポンプとガス燃焼 ----------
def ecocute_gas():
    d = D('16:9'); d.header('エコキュートとガス給湯器の仕組みの違い', 'エコキュートは「空気の熱をくみ上げて」、ガス給湯器は「ガスを燃やして」お湯をつくります')
    box(d, 40, 130, 590, 540, 'エコキュート（電気・ヒートポンプ）', fill='#f3f7f0', stroke=GREEN, tcolor=GREEN)
    box(d, 650, 130, 590, 540, 'ガス給湯器', fill='#fbf4ec', stroke='#b8683a', tcolor='#8a4a22')
    # heat pump unit
    d.rect(80, 300, 200, 150, fill=WHITE, stroke=LINE, sw=2.5, rx=8); d.circle(150, 375, 48, fill='#e6ecef', stroke=LINE, sw=2)
    for k in range(3): d.line(150 - 30 + k * 30, 335, 150 - 30 + k * 30, 415, stroke=GREY, sw=2)
    d.text(180, 480, 'ヒートポンプユニット', 18, INK, 700, 'middle')
    for k in range(3): d.arrow(60, 250 + k * 30, 110, 300 + k * 20, color=WATER_D, sw=3, head=12)
    d.text(70, 232, '空気の熱', 18, WATER_D, 700)
    # tank
    d.rect(420, 230, 150, 330, fill=WHITE, stroke=LINE, sw=2.5, rx=40)
    d.rect(432, 290, 126, 258, fill='#f6c9a8', stroke='none', rx=30); d.text(495, 420, 'お湯を', 20, INK, 700, 'middle'); d.text(495, 448, 'ためる', 20, INK, 700, 'middle')
    d.text(495, 590, '貯湯タンク', 18, INK, 700, 'middle')
    d.arrow(285, 360, 415, 360, color=WARN, sw=4); d.text(350, 345, '熱を水へ', 17, WARN, 700, 'middle')
    d.arrow(570, 300, 618, 300, color=WARN, sw=4); d.text(560, 270, '給湯', 18, WARN, 700, 'end')
    d.mtext(70, 620, ['・電気でヒートポンプを動かし、空気の熱を利用', '・つくったお湯をタンクにためて使う（お湯切れの可能性あり）'], 17, '#4a4d46', 500)
    # gas
    d.rect(820, 250, 200, 280, fill=WHITE, stroke=LINE, sw=2.5, rx=10)
    d.path('M870,470 q15,-30 0,-55 q25,15 30,45 q10,-25 5,-50 q30,25 20,60z', fill='#f2a33a', stroke='#b86a1e', sw=2)
    d.rect(850, 300, 140, 60, fill='#e3e6e2', stroke=LINE, sw=2); d.text(920, 337, '熱交換器', 17, INK, 700, 'middle')
    d.text(920, 560, 'ガス給湯器', 18, INK, 700, 'middle')
    d.arrow(700, 500, 815, 500, color='#b8683a', sw=4); d.text(705, 485, 'ガス', 18, '#8a4a22', 700)
    d.arrow(700, 330, 845, 330, color=WATER_D, sw=4); d.text(705, 315, '水', 18, WATER_D, 700)
    d.arrow(995, 330, 1180, 330, color=WARN, sw=4); d.text(1090, 315, 'すぐにお湯', 18, WARN, 700, 'middle')
    d.mtext(680, 620, ['・ガスを燃やした熱で、水をその場で温める', '・タンクがいらず、お湯切れの心配が少ない'], 17, '#4a4d46', 500)
    out('ecocute-gas-hikaku-01', d, 'エコキュート（空気の熱を使うヒートポンプでお湯をつくりタンクにためる）とガス給湯器（ガスを燃やして水をその場で温める）の仕組みの比較図')


# ---------- 109 太陽光＋蓄電池 ----------
def solar():
    d = D('16:9'); d.header('太陽光発電＋蓄電池の電気の流れ', '昼に発電した電気を家で使い、余った分を蓄電池にためて夜や停電時に使えます')
    for i, (title, night) in enumerate((('昼（発電中）', False), ('夜・停電時', True))):
        x0 = 40 + i * 620
        box(d, x0, 130, 580, 540, title, fill='#eef3f8' if night else '#fbf8ec', stroke=GREY)
        house(d, x0 + 60, 330, 210, 200, 80)
        # panel
        d.poly([(x0 + 100, 316), (x0 + 185, 268), (x0 + 255, 300), (x0 + 170, 348)], fill='#3c5a7a', stroke='#22364b', sw=2)
        if not night:
            d.circle(x0 + 520, 220, 34, fill='#f6d36b', stroke='#c9a73a', sw=2)
            d.line(x0 + 490, 245, x0 + 250, 300, stroke='#e2b93b', sw=3, dash='8 8')
        else:
            d.path(f'M{x0+520},190 a34,34 0 1,0 30,50 a26,26 0 1,1 -30,-50z', fill='#e8e2b0', stroke='#b3a65a', sw=2)
        # battery
        d.rect(x0 + 400, 440, 90, 130, fill=WHITE, stroke=LINE, sw=2.5, rx=8); d.rect(x0 + 425, 430, 40, 12, fill=LINE, stroke=LINE, sw=1)
        lvl = 30 if night else 95
        d.rect(x0 + 410, 560 - lvl, 70, lvl, fill=GREEN, stroke='none', rx=4); d.text(x0 + 445, 598, '蓄電池', 18, INK, 700, 'middle')
        # grid
        d.line(x0 + 535, 300, x0 + 535, 600, stroke=GREY, sw=3); d.line(x0 + 515, 320, x0 + 555, 320, stroke=GREY, sw=3); d.text(x0 + 525, 630, '電力会社', 16, INK, 700, 'middle')
        if not night:
            d.arrow(x0 + 200, 360, x0 + 200, 420, color=GOLD, sw=4); d.text(x0 + 215, 400, '家で使う', 17, '#8a6d16', 700)
            d.arrow(x0 + 284, 505, x0 + 396, 505, color=GOLD, sw=4); d.text(x0 + 340, 492, '余りを充電', 15, '#8a6d16', 700, 'middle')
            d.arrow(x0 + 284, 400, x0 + 528, 380, color=GOLD, sw=3); d.text(x0 + 415, 372, '余りを売電', 16, '#8a6d16', 700, 'middle')
        else:
            d.arrow(x0 + 396, 505, x0 + 284, 505, color=GREEN, sw=4); d.text(x0 + 340, 492, '蓄電池から使う', 15, GREEN, 700, 'middle')
            d.arrow(x0 + 528, 400, x0 + 284, 420, color=GREY, sw=3); d.text(x0 + 415, 392, '足りない分は買電', 16, '#4a4d46', 700, 'middle')
    d.note('※ 停電時に使える範囲（家全体か一部の回路か）は、蓄電池の機種や設定によって異なります', 700)
    out('taiyoukou-chikudenchi-set-01', d, '太陽光発電と蓄電池の電気の流れ。昼は発電した電気を家で使い余りを充電・売電し、夜や停電時は蓄電池の電気を使う')


# ---------- 116 玄関ドア カバー工法の断面 ----------
def door_cover():
    d = D('16:9'); d.header('玄関ドア交換：カバー工法と壁を壊す工法', '上から見た断面イメージ。カバー工法は既存の枠を残し、その内側に新しい枠を取り付けます')
    for i, title in enumerate(('カバー工法', '壁を壊す工法')):
        x0 = 40 + i * 620
        box(d, x0, 130, 580, 470, title, fill=WHITE, stroke=GREEN if i == 0 else GREY, tcolor=GREEN if i == 0 else INK)
        # walls
        d.rect(x0 + 40, 300, 120, 120, fill='#e8e2d6', stroke=LINE, sw=2); d.rect(x0 + 420, 300, 120, 120, fill='#e8e2d6', stroke=LINE, sw=2)
        for xx in (x0 + 40, x0 + 420):
            for k in range(5): d.line(xx + k * 22, 300, xx + k * 22 + 20, 420, stroke='#cfc6b4', sw=1.5)
        if i == 0:
            d.rect(x0 + 160, 300, 24, 120, fill='#9aa3a8', stroke=LINE, sw=2); d.rect(x0 + 396, 300, 24, 120, fill='#9aa3a8', stroke=LINE, sw=2)
            d.rect(x0 + 184, 290, 22, 140, fill=GREEN, stroke=LINE, sw=2); d.rect(x0 + 374, 290, 22, 140, fill=GREEN, stroke=LINE, sw=2)
            d.rect(x0 + 206, 350, 168, 20, fill='#c9a06b', stroke=LINE, sw=2)
            d.label(x0 + 172, 310, '既存の枠（残す）', x0 + 120, 220)
            d.label(x0 + 195, 425, '新しい枠をかぶせる', x0 + 300, 555, anchor='middle')
            d.dim_h(x0 + 206, x0 + 374, 455, '開口がわずかに小さくなる', above=False)
        else:
            d.rect(x0 + 160, 300, 30, 120, fill='#e8e2d6', stroke=WARN, sw=2, dash='6 4'); d.rect(x0 + 390, 300, 30, 120, fill='#e8e2d6', stroke=WARN, sw=2, dash='6 4')
            d.rect(x0 + 160, 290, 22, 140, fill=GREEN, stroke=LINE, sw=2); d.rect(x0 + 398, 290, 22, 140, fill=GREEN, stroke=LINE, sw=2)
            d.rect(x0 + 182, 350, 216, 20, fill='#c9a06b', stroke=LINE, sw=2)
            d.label(x0 + 175, 300, '既存の枠を撤去し、壁を補修', x0 + 140, 220)
            d.label(x0 + 171, 425, '新しい枠', x0 + 220, 520)
    d.rect(40, 616, 1200, 60, fill=SOFT, stroke='none', rx=10)
    d.text(60, 655, 'カバー工法：工期が短く（1日程度の場合が多い）、費用を抑えやすい　／　壁を壊す工法：工期が長く、費用が高くなりやすい', 19, INK, 600)
    out('genkan-door-koukan-hiyou-01', d, '玄関ドア交換のカバー工法（既存の枠を残して内側に新しい枠を付ける）と、壁を壊す工法（既存の枠を撤去する）の断面比較図')


# ---------- 118 床の重ね張りと張り替え ----------
def flooring():
    d = D('16:9'); d.header('フローリングの重ね張りと張り替えの違い', '断面イメージ。重ね張りは床が少し高くなり、張り替えは下地まで確認・補修できます')
    for i, title in enumerate(('重ね張り', '張り替え')):
        x0 = 40 + i * 620
        box(d, x0, 130, 580, 470, title, fill=WHITE, stroke=GREY)
        bx, bw = x0 + 50, 360; y = 520
        for k in range(3): d.rect(bx + 30 + k * 130, y - 40, 40, 40, fill='#b88850', stroke=WOOD_D, sw=2)
        d.text(bx + bw + 10, y - 14, '根太', 16, INK, 700)
        d.rect(bx, y - 64, bw, 24, fill='#d8c39a', stroke=WOOD_D, sw=2); d.text(bx + bw + 10, y - 46, '下地（合板）', 16, INK, 700)
        if i == 0:
            d.rect(bx, y - 84, bw, 20, fill='#a88a64', stroke=WOOD_D, sw=2); d.text(bx + bw + 10, y - 68, '既存の床', 16, INK, 700)
            d.rect(bx, y - 100, bw, 16, fill=WOOD, stroke=WOOD_D, sw=2); d.text(bx + bw + 10, y - 90, '新しい床材', 16, GREEN, 700)
            d.line(bx - 10, y - 84, bx + bw, y - 84, stroke=GREY, sw=1.5, dash='6 4')
            d.label(bx + 180, y - 100, '床がわずかに高くなる', bx + 180, 240, anchor='middle')
            d.text(x0 + 290, 580, '既存の床を撤去しない → 工期が短く、費用を抑えやすい', 17, '#4a4d46', 600, 'middle')
        else:
            d.rect(bx + 160, y - 64, 120, 24, fill='#e6d5ae', stroke=GREEN, sw=3); d.label(bx + 220, y - 52, '下地を確認・補修', bx + 220, 240, anchor='middle')
            d.rect(bx, y - 84, bw, 20, fill=WOOD, stroke=WOOD_D, sw=2); d.text(bx + bw + 10, y - 68, '新しい床材', 16, GREEN, 700)
            d.rect(bx + 40, 300, 150, 18, fill='#a88a64', stroke=WOOD_D, sw=2, dash='6 4'); d.text(bx + 115, 290, '既存の床は撤去', 16, WARN, 700, 'middle')
            d.text(x0 + 290, 580, '床鳴り・傾き・水漏れ跡がある場合に向く', 17, '#4a4d46', 600, 'middle')
    d.note('※ 重ね張りで床が高くなると、ドアの開閉に干渉する場合があります', 690)
    out('flooring-kasanebari-harikae-01', d, 'フローリングの重ね張り（既存の床の上に新しい床材を重ね床がわずかに高くなる）と張り替え（既存の床を撤去し下地を確認・補修）の断面比較図')


# ---------- 122 旗竿地 ----------
def hatazao():
    d = D('16:9'); d.header('旗竿地の形と通路幅', '上から見たイメージ。道路に接する細い通路（竿）の奥に、建物を建てる敷地（旗）があります')
    d.rect(80, 600, 1120, 80, fill='#d3d5cf', stroke=GREY, sw=2); d.text(640, 650, '道路', 22, INK, 700, 'middle')
    for x, w in ((80, 380), (620, 580)): d.rect(x, 150, w, 440, fill='#eceae4', stroke=GREY, sw=2)
    d.text(270, 380, '隣地', 20, '#6b6e66', 600, 'middle'); d.text(910, 470, '隣地', 20, '#6b6e66', 600, 'middle')
    d.poly([(470, 150), (1100, 150), (1100, 400), (610, 400), (610, 590), (470, 590)], fill='#e8efe0', stroke=GREEN, sw=3)
    d.rect(560, 200, 300, 160, fill='#f4f1ea', stroke=LINE, sw=2.5); d.text(710, 290, '建物', 22, INK, 700, 'middle')
    d.text(960, 280, '旗の部分（敷地）', 20, GREEN, 700, 'middle'); d.text(540, 500, '竿の部分', 18, GREEN, 700, 'middle'); d.text(540, 524, '（通路）', 18, GREEN, 700, 'middle')
    d.dim_h(470, 610, 575, '', above=True); d.label(540, 572, '道路に接する幅：原則2m以上（接道義務）', 640, 470, anchor='start')
    d.mtext(660, 520, ['・通路の長さに応じて、自治体の条例で', '　より広い幅が求められる場合があります', '・工事車両が入れる幅かも確認します'], 17, '#4a4d46', 500)
    out('hatazaochi-merit-demerit-01', d, '旗竿地の形の図。道路に接する細い通路（竿）の奥に敷地（旗）があり、道路に接する幅は原則2m以上必要')


# ---------- 123 角地と中間地 ----------
def kadochi():
    d = D('16:9'); d.header('角地と中間地の違い', '角地は2方向が道路に面し、日当たりや開放感に優れる一方、道路からの視線も2方向から入ります')
    for i, title in enumerate(('角地', '中間地')):
        x0 = 40 + i * 620
        box(d, x0, 130, 580, 560, title, fill=WHITE, stroke=GREY)
        # roads
        d.rect(x0 + 40, 560, 500, 70, fill='#d3d5cf', stroke=GREY, sw=2); d.text(x0 + 290, 603, '道路', 20, INK, 700, 'middle')
        if i == 0:
            d.rect(x0 + 40, 190, 70, 370, fill='#d3d5cf', stroke=GREY, sw=2); d.text(x0 + 75, 380, '道路', 20, INK, 700, 'middle')
            lot = (x0 + 110, 190, 300, 370); d.rect(*lot, fill='#e8efe0', stroke=GREEN, sw=3)
            d.rect(x0 + 410, 190, 130, 370, fill='#eceae4', stroke=GREY, sw=2); d.text(x0 + 475, 380, '隣地', 18, '#6b6e66', 600, 'middle')
            d.rect(x0 + 180, 260, 170, 200, fill='#f4f1ea', stroke=LINE, sw=2.5)
            d.arrow(x0 + 60, 250, x0 + 170, 300, color=GOLD, sw=4); d.arrow(x0 + 260, 620, x0 + 260, 470, color=GOLD, sw=4)
            d.text(x0 + 240, 520, '採光・通風が2方向から', 16, '#8a6d16', 700, 'middle')
            d.ng(x0 + 150, 225, 16); d.ng(x0 + 380, 520, 16); d.text(x0 + 380, 495, '視線も2方向', 15, WARN, 700, 'middle')
        else:
            d.rect(x0 + 40, 190, 140, 370, fill='#eceae4', stroke=GREY, sw=2); d.rect(x0 + 400, 190, 140, 370, fill='#eceae4', stroke=GREY, sw=2)
            d.text(x0 + 110, 380, '隣地', 18, '#6b6e66', 600, 'middle'); d.text(x0 + 470, 380, '隣地', 18, '#6b6e66', 600, 'middle')
            d.rect(x0 + 180, 190, 220, 370, fill='#e8efe0', stroke=GREEN, sw=3); d.rect(x0 + 210, 260, 160, 200, fill='#f4f1ea', stroke=LINE, sw=2.5)
            d.arrow(x0 + 290, 620, x0 + 290, 470, color=GOLD, sw=4); d.text(x0 + 290, 520, '道路に面するのは1方向', 16, '#8a6d16', 700, 'middle')
    d.text(40, 712, '※ 角地の建ぺい率の緩和は、自治体の条例や角地の条件（角度・道路の幅など）によって適用の有無が異なります', 17, '#6b6e66', 500)
    out('kadochi-merit-demerit-01', d, '角地（2方向が道路に面し採光と視線が2方向）と中間地（道路に面するのは1方向）を上から見た比較図')


# ---------- 124 建ぺい率・容積率 ----------
def kenpei():
    d = D('16:9'); d.header('建ぺい率・容積率の計算例', '敷地面積100㎡、建ぺい率60％・容積率200％の土地の場合')
    box(d, 40, 130, 590, 540, '建ぺい率：建物を真上から見た面積の上限', fill='#f3f7f0', stroke=GREEN, tsize=21, tcolor=GREEN)
    d.rect(140, 220, 300, 300, fill='#e8efe0', stroke=GREEN, sw=3); d.text(290, 545, '敷地面積 100㎡', 20, INK, 700, 'middle')
    d.rect(170, 250, 180, 200, fill='#f6c9a8', stroke=LINE, sw=2.5); d.text(260, 345, '建築面積', 20, INK, 700, 'middle'); d.text(260, 375, '最大60㎡', 22, WARN, 700, 'middle')
    d.text(470, 300, '上から見た図', 16, '#6b6e66', 600)
    d.rect(60, 590, 550, 60, fill=WHITE, stroke=GREY, sw=1.5, rx=8); d.text(335, 628, '建ぺい率 ＝ 建築面積 ÷ 敷地面積 × 100', 20, INK, 700, 'middle')
    box(d, 650, 130, 590, 540, '容積率：各階の床面積の合計の上限', fill='#fbf4ec', stroke='#b8683a', tsize=21, tcolor='#8a4a22')
    d.line(700, 520, 1180, 520, stroke=LINE, sw=3)
    d.rect(760, 400, 240, 120, fill='#f6c9a8', stroke=LINE, sw=2.5); d.text(880, 468, '1階 60㎡', 20, INK, 700, 'middle')
    d.rect(760, 280, 240, 120, fill='#f6c9a8', stroke=LINE, sw=2.5); d.text(880, 348, '2階 60㎡', 20, INK, 700, 'middle')
    d.mtext(1020, 330, ['延床面積', '120㎡'], 20, INK, 700); d.mtext(1020, 410, ['上限 200㎡', '以内なのでOK'], 18, GREEN, 700)
    d.text(880, 555, '横から見た図（2階建ての例）', 16, '#6b6e66', 600, 'middle')
    d.rect(670, 590, 550, 60, fill=WHITE, stroke=GREY, sw=1.5, rx=8); d.text(945, 628, '容積率 ＝ 延床面積 ÷ 敷地面積 × 100', 20, INK, 700, 'middle')
    d.note('※ 容積率は前面道路の幅によって、指定された数値より低く制限される場合があります', 700)
    out('kenpeiritsu-yousekiritsu-01', d, '建ぺい率と容積率の計算例。敷地100㎡・建ぺい率60％なら建築面積は最大60㎡、容積率200％なら延床面積は最大200㎡（2階建てで各60㎡なら延床120㎡）')


# ---------- 125 接道義務 ----------
def setsudo():
    d = D('16:9'); d.header('接道義務：幅4m以上の道路に2m以上接する', '建築基準法の原則。上から見たイメージ')
    for i, (title, ok_) in enumerate((('建築できる（原則）', True), ('建築できない（無接道地など）', False))):
        x0 = 40 + i * 620
        box(d, x0, 130, 580, 540, title, fill=WHITE, stroke=GREEN if ok_ else WARN, tcolor=GREEN if ok_ else WARN)
        d.rect(x0 + 40, 540, 500, 90, fill='#d3d5cf', stroke=GREY, sw=2); d.text(x0 + 290, 595, '道路（幅4m以上）', 20, INK, 700, 'middle')
        d.dim_v(x0 + 520, 540, 630, '', right=False)
        if ok_:
            d.rect(x0 + 140, 220, 300, 320, fill='#e8efe0', stroke=GREEN, sw=3); d.rect(x0 + 200, 280, 180, 160, fill='#f4f1ea', stroke=LINE, sw=2.5)
            d.dim_h(x0 + 140, x0 + 440, 520, '道路に接する長さ 2m以上', above=True)
        else:
            d.rect(x0 + 140, 220, 300, 230, fill='#f6e9e4', stroke=WARN, sw=3); d.rect(x0 + 140, 450, 300, 90, fill='#eceae4', stroke=GREY, sw=2)
            d.text(x0 + 290, 500, '他人の土地', 18, '#6b6e66', 600, 'middle'); d.text(x0 + 290, 340, '道路に接していない', 20, WARN, 700, 'middle')
    d.note('※ 道路の幅が4m未満の場合は、セットバックにより条件を満たせる場合があります', 700)
    out('setsudo-gimu-01', d, '接道義務の図。敷地が幅4m以上の道路に2m以上接していれば原則建築でき、道路に接していない土地は原則建築できない')


# ---------- 126 セットバック ----------
def setback():
    d = D('16:9'); d.header('セットバック：道路の中心線から2m後退する', '幅4m未満の道路（2項道路）に接する土地の場合。上から見たイメージ')
    d.rect(80, 480, 1120, 150, fill='#d3d5cf', stroke=GREY, sw=2); d.text(100, 615, '現在の道路（幅4m未満）', 20, INK, 700)
    d.line(80, 555, 1200, 555, stroke=WHITE, sw=4, dash='20 14'); d.text(1190, 545, '道路の中心線', 18, '#4a4d46', 700, 'end')
    d.rect(240, 150, 560, 330, fill='#e8efe0', stroke=GREEN, sw=3)
    d.rect(240, 420, 560, 60, fill='#f3d9cf', stroke=WARN, sw=2.5)
    for k in range(18): d.line(250 + k * 30, 478, 330 + k * 30, 422, stroke=WARN, sw=1.5)
    d.line(240, 420, 800, 420, stroke=WARN, sw=3, dash='12 8')
    d.dim_v(830, 420, 555, '道路の中心線から2m', right=True)
    d.rect(370, 210, 300, 170, fill='#f4f1ea', stroke=LINE, sw=2.5); d.text(520, 300, '建物', 22, INK, 700, 'middle')
    d.label(700, 450, 'セットバック部分', 880, 230, anchor='start', color=WARN); d.mtext(880, 290, ['道路とみなされ、', '建物や塀は建てられない', '（敷地面積から除かれる', '　場合があります）'], 19, '#4a4d46', 600)
    d.text(250, 180, '敷地', 20, GREEN, 700)
    d.note('※ 向かい側が川や崖などの場合は、扱いが異なります。必要な後退距離は自治体で確認します', 700)
    out('setback-toha-01', d, 'セットバックの図。幅4m未満の道路に接する土地では、道路の中心線から2m後退した線までが道路とみなされ、その部分には建物や塀を建てられない')


# ---------- 131 住宅省エネ2026 4事業 ----------
def shoene():
    d = D('16:9'); d.header('住宅省エネ2026キャンペーン：4つの補助事業', '検討している工事から、関係する事業を確認します')
    items = [('先進的窓リノベ2026事業', '窓の断熱リフォーム', '内窓の設置、窓の交換など', '#e3eef5', WATER_D),
             ('給湯省エネ2026事業', '高効率給湯器の導入', 'エコキュートなど', '#fbeee2', '#b8683a'),
             ('みらいエコ住宅2026事業', '断熱改修・エコ住宅設備など', '新築・リフォームの両方が対象', '#eef3e8', GREEN),
             ('賃貸集合給湯省エネ2026事業', '賃貸住宅の給湯器交換', '賃貸集合住宅が対象', '#f1edf6', '#6b5a8a')]
    for i, (name, work, sub, bg, c) in enumerate(items):
        x = 40 + (i % 2) * 610; y = 130 + (i // 2) * 250
        d.rect(x, y, 590, 230, fill=bg, stroke=c, sw=2.5, rx=14)
        d.text(x + 30, y + 52, name, 26, c, 700)
        d.text(x + 30, y + 112, '対象の工事', 17, '#6b6e66', 600); d.text(x + 30, y + 148, work, 24, INK, 700); d.text(x + 30, y + 188, sub, 18, '#4a4d46', 500)
    d.rect(40, 640, 1200, 60, fill=WHITE, stroke=GREY, sw=1.5, rx=10)
    d.text(60, 678, '申請は登録事業者が行うのが基本。補助額・条件・期間は公式サイト（jutaku-shoene2026.mlit.go.jp）で最新情報を確認', 18, INK, 600)
    out('jutaku-shoene2026-01', d, '住宅省エネ2026キャンペーンを構成する4つの補助事業（先進的窓リノベ、給湯省エネ、みらいエコ住宅、賃貸集合給湯省エネ）と対象工事の早見表')


# ---------- 136 支払い方法 ----------
def shiharai():
    d = D('16:9'); d.header('リフォーム費用の支払い方法の比較', '金利・審査・手元資金への影響の違い')
    cols = [('現金払い', '#f3f7f0', GREEN), ('リフォームローン', '#fbf4ec', '#b8683a'), ('住宅ローンへの組み込み', '#eef3f8', WATER_D)]
    rows = [('金利負担', ('なし', '発生する', '発生する')), ('審査', ('不要', '必要', '必要')), ('手元資金への影響', ('大きい', '小さい', '小さい'))]
    d.rect(40, 130, 1200, 70, fill=WHITE, stroke='none')
    for j, (t, bg, c) in enumerate(cols):
        x = 300 + j * 313; d.rect(x, 130, 300, 70, fill=c, stroke='none', rx=10); d.text(x + 150, 175, t, 24, WHITE, 700, 'middle')
    good = {('金利負担', 0), ('審査', 0), ('手元資金への影響', 1), ('手元資金への影響', 2)}
    for i, (r, vals) in enumerate(rows):
        y = 215 + i * 125
        d.rect(40, y, 250, 110, fill=SOFT, stroke='none', rx=10); d.text(165, y + 64, r, 22, INK, 700, 'middle')
        for j, v in enumerate(vals):
            x = 300 + j * 313; d.rect(x, y, 300, 110, fill=cols[j][1], stroke='none', rx=10)
            d.text(x + 150, y + 66, v, 26, INK, 700, 'middle')
            (d.ok if (r, j) in good else d.ng)(x + 50, y + 55, 16)
    d.note('※ 一般的に住宅ローンの方が金利が低い傾向がありますが、審査や手続きの条件が異なります', 650)
    d.note('※ 現金で払う場合も、急な出費に備えて一定の資金を残しておきましょう', 690)
    out('reform-hiyou-shiharai-houhou-01', d, 'リフォーム費用の支払い方法の比較表。現金払いは金利・審査なしだが手元資金への影響が大きく、リフォームローンと住宅ローンへの組み込みは金利と審査があるが手元資金への影響は小さい')


# ---------- 139 中古住宅＋リフォームの費用内訳 ----------
def chuuko():
    d = D('16:9'); d.header('中古住宅＋リフォームの予算は「3つ＋予備」で考える', '物件価格だけでなく、総額で資金計画を立てます（割合はイメージ）')
    parts = [('購入費用', '物件価格・仲介手数料・登記費用など', 520, '#f6c9a8'), ('リフォーム費用', '水回り・内装・断熱改修など', 360, '#cfe0c3'),
             ('諸費用', 'ローン手数料・火災保険料・引っ越し費用など', 160, '#d9e3ee'), ('予備費', '想定外の補修に備える', 120, '#efe6c8')]
    x = 60; y = 250
    for name, sub, w, c in parts:
        d.rect(x, y, w, 120, fill=c, stroke=LINE, sw=2.5); d.text(x + w / 2, y + 70, name, 22 if w > 140 else 19, INK, 700, 'middle'); x += w
    d.dim_h(60, x, 210, '総額で予算を考える')
    yy = 430
    for i, (name, sub, w, c) in enumerate(parts):
        d.rect(60, yy + i * 58, 26, 26, fill=c, stroke=LINE, sw=2); d.text(100, yy + i * 58 + 21, f'{name}：{sub}', 20, INK, 600)
    d.note('※ 内見だけでは見えない構造・配管の劣化が見つかることがあるため、予算には余裕を持たせます', 700)
    out('chuuko-jutaku-reform-hiyou-01', d, '中古住宅を購入してリフォームする場合の予算の内訳図。購入費用・リフォーム費用・諸費用に予備費を加えた総額で考える')


# ---------- 150 年間カレンダー ----------
def calendar():
    d = D('16:9'); d.header('庭の年間メンテナンスカレンダー', '成長期（春〜夏）と休眠期（冬）で作業を切り替えます。地域の気候に合わせて調整してください')
    seasons = [('春', '#f6dfe4', '#b35a72', ['植え付け・種まき', '施肥', '常緑樹の剪定|（花後など）', '防草シートの点検']),
               ('夏', '#e2efd8', '#4f7a3a', ['水やり（頻度を増やす）', '雑草の除去', '害虫・病気のチェック', '人工芝・砂利のゴミ除去']),
               ('秋', '#f6e4cc', '#a3601e', ['落ち葉の掃除', '花壇の植え替え', '台風対策|（鉢の移動・排水確認）', '来年に向けた土の準備']),
               ('冬', '#dfe7f0', '#3f6a8f', ['落葉樹の剪定（休眠期）', '霜・雪対策', '水道管・立水栓の|凍結対策', '来春の計画の見直し'])]
    for i, (s, bg, c, items) in enumerate(seasons):
        x = 40 + i * 305
        d.rect(x, 130, 290, 560, fill=bg, stroke='none', rx=14)
        d.circle(x + 145, 205, 46, fill=c, stroke='none'); d.text(x + 145, 220, s, 40, WHITE, 700, 'middle')
        for k, t in enumerate(items):
            yy = 300 + k * 92
            d.rect(x + 18, yy, 254, 76, fill=WHITE, stroke='none', rx=10)
            lines = t.split('|')
            for li, ln in enumerate(lines): d.text(x + 145, yy + 34 + li * 26 - (12 if len(lines) > 1 else -4), ln, 19, INK, 700, 'middle')
    out('niwa-teire-nenkan-calendar-01', d, '庭の年間メンテナンスカレンダー。春は植え付けと施肥、夏は水やりと雑草対策、秋は落ち葉掃除と台風対策、冬は落葉樹の剪定と凍結対策')


if __name__ == '__main__':
    import sys, os, json
    for f in (ecocute_gas, solar, door_cover, flooring, hatazao, kadochi, kenpei, setsudo, setback, shoene, shiharai, chuuko, calendar): f()
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
