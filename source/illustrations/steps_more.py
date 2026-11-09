"""Step illustrations: 砂利 / 花壇 / レンガ / ウッドデッキ / フェンス / 小道 / タイル / 物置 / ライト / 土の入れ替え / 段差 / 換気 / 保温材 / 人工芝のお手入れ"""
from lib import *
from steps_ground import GX, GW, GY, GH, section_label

OUT = {}
def out(name, d, alt): OUT[name] = (d, alt)
def base(n, title, sub=None):
    d = D('4:3'); d.step_header(n, title, sub); return d


def brick_wall(d, x, y, cols, rows, w=64, h=24, mortar=False):
    """running-bond wall exactly cols*w wide, bottom at y"""
    W = cols * w
    for r in range(rows):
        yy = y - (r + 1) * h
        cx = x - (w / 2 if r % 2 else 0)
        while cx < x + W - 0.5:
            x0 = max(cx, x); x1 = min(cx + w, x + W)
            d.rect(x0, yy, x1 - x0, h, fill=BRICK, stroke=BRICK_D, sw=2)
            cx += w


# ---------------- 砂利（No.35） ----------------
def gravel(slug):
    d = base(1, '雑草・石を取り除き、平らにする', '敷く範囲の雑草を根から抜き、地面をならします')
    d.soil(GX, GY, 420, GH, rough=True); d.weeds(GX + 30, GY, 4, 360); d.soil(GX + 420, GY, 420, GH); d.rake(GX + 720, GY - 2, 1, -28)
    d.arrow(GX + 360, GY - 120, GX + 480, GY - 120); d.text(GX + 420, GY - 136, '除草・整地', 20, GREEN, 700, 'middle'); section_label(d)
    out(f'{slug}-01', d, '砂利敷きの手順1：雑草を取り除き、地面を平らにする')
    d = base(2, '防草シートを敷き、ピンで留める', '継ぎ目は十分に重ねて固定します')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8)
    for x in range(GX + 60, GX + GW, 130): d.pin(x, GY - 8, 46)
    d.label(GX + 330, GY - 6, '防草シート', GX + 330, GY - 110, anchor='middle'); section_label(d)
    out(f'{slug}-02', d, '砂利敷きの手順2：防草シートを敷き、固定ピンで留める')
    d = base(3, '縁に枠材を設置する', 'レンガやエッジング材で砂利の流出を防ぎます')
    d.soil(GX, GY, GW, GH); d.sheet(GX + 60, GY, GW - 120, 8)
    for x in (GX + 20, GX + GW - 60):
        d.rect(x, GY - 50, 40, 90, fill=BRICK, stroke=BRICK_D, sw=2.5, rx=2)
    d.label(GX + 40, GY - 30, '枠材（レンガ・エッジング材など）', GX + 60, GY - 150)
    d.label(GX + GW - 40, GY - 30, '地面に少し埋めて固定', GX + GW - 60, GY - 100, anchor='end'); section_label(d)
    out(f'{slug}-03', d, '砂利敷きの手順3：敷く範囲の縁にレンガなどの枠材を設置する')
    d = base(4, '砂利を適切な厚みで敷く', 'シートが見えない程度の厚みを確保します（目安は数cm程度）')
    d.soil(GX, GY, GW, GH); d.sheet(GX + 60, GY, GW - 120, 8)
    for x in (GX + 20, GX + GW - 60): d.rect(x, GY - 50, 40, 90, fill=BRICK, stroke=BRICK_D, sw=2.5, rx=2)
    d.gravel_layer(GX + 60, GY - 44, GW - 120, 36)
    d.dim_v(GX + GW - 90, GY - 44, GY - 8, '', right=False); d.label(GX + GW - 90, GY - 30, '厚み：数cm程度が目安', GX + GW - 110, GY - 130, anchor='end')
    d.ng(GX + 80, GY - 150); d.text(GX + 115, GY - 142, '薄いと防草シートが見えやすい', 19, WARN, 700); section_label(d)
    out(f'{slug}-04', d, '砂利敷きの手順4：防草シートが見えない程度の厚みで砂利を敷く')
    d = base(5, 'レーキで均等にならす', '厚みが偏らないように全体を平らに整えます')
    d.soil(GX, GY, GW, GH); d.sheet(GX + 60, GY, GW - 120, 8)
    for x in (GX + 20, GX + GW - 60): d.rect(x, GY - 50, 40, 90, fill=BRICK, stroke=BRICK_D, sw=2.5, rx=2)
    d.gravel_layer(GX + 60, GY - 44, GW - 120, 36); d.rake(GX + 520, GY - 46, 1, -30)
    d.arrow(GX + 140, GY - 90, GX + 300, GY - 90); d.arrow(GX + 300, GY - 70, GX + 140, GY - 70); section_label(d)
    out(f'{slug}-05', d, '砂利敷きの手順5：レーキで砂利を均等にならして仕上げる')


# ---------------- 花壇（No.25 庭の花壇の作り方） ----------------
def kadan(slug):
    d = D('4:3'); d.step_header(1, '配置場所を決める', '日当たりと水はけを確認してから場所を決めます')
    d.rect(100, 160, 760, 470, fill='#e8efe0', stroke=GREEN, sw=2.5, rx=8)
    d.rect(100, 160, 120, 470, fill='#d9d5cc', stroke=GREY, sw=2); d.text(160, 400, '建物', 22, INK, 700, 'middle')
    d.circle(780, 230, 40, fill='#f6d36b', stroke='#c9a73a', sw=2.5); d.text(780, 300, '日当たり', 18, '#8a6d16', 700, 'middle')
    d.rect(420, 320, 260, 140, fill='none', stroke=WARN, sw=3, rx=6, dash='12 8'); d.text(550, 400, '花壇の予定地', 22, WARN, 700, 'middle')
    d.label(450, 460, '水たまりができない場所か', 300, 560); d.label(680, 330, '日が当たる時間を確認', 700, 520)
    d.note('上から見た配置のイメージ', 700)
    out(f'{slug}-01', d, '花壇づくりの手順1：日当たりと水はけを確認して花壇の場所を決める')
    d = base(2, '土を掘り、縁取りを設置する', 'レンガやブロックなどの縁取りを、少し埋めて固定します')
    d.soil(GX, GY, GW, GH); d.rect(GX + 200, GY, 440, 40, fill='#b38f5d', stroke=SOIL_D, sw=2)
    for x in (GX + 180, GX + 640): d.rect(x, GY - 60, 40, 100, fill=BRICK, stroke=BRICK_D, sw=2.5, rx=2)
    d.shovel(GX + 420, GY - 10, .9, -15); d.label(GX + 200, GY - 30, '縁取り（レンガ・ブロックなど）', GX + 120, GY - 150); section_label(d)
    out(f'{slug}-02', d, '花壇づくりの手順2：土を掘り、レンガやブロックなどの縁取りを設置する')
    d = base(3, '土壌を改良する', '腐葉土や肥料を混ぜて、水はけと水もちのよい土にします')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 180, GX + 640): d.rect(x, GY - 60, 40, 100, fill=BRICK, stroke=BRICK_D, sw=2.5, rx=2)
    d.rect(GX + 220, GY - 40, 420, 80, fill='#7a5a35', stroke='#5a4126', sw=2)
    for i in range(40): d.circle(GX + 230 + d.rnd.uniform(0, 400), GY - 30 + d.rnd.uniform(0, 64), 3, fill='#c7a774', stroke='none')
    d.rect(GX + 690, GY - 150, 120, 90, fill='#c9b48a', stroke=WOOD_D, sw=2.5, rx=6); d.text(GX + 750, GY - 98, '腐葉土', 20, INK, 700, 'middle')
    d.curved_arrow(GX + 690, GY - 110, GX + 600, GY - 160, GX + 520, GY - 60); section_label(d)
    out(f'{slug}-03', d, '花壇づくりの手順3：腐葉土や肥料を混ぜて土壌を改良する')
    d = base(4, '植物を植え付ける', '根鉢を崩しすぎないように植え、株元に土を寄せます')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 180, GX + 640): d.rect(x, GY - 60, 40, 100, fill=BRICK, stroke=BRICK_D, sw=2.5, rx=2)
    d.rect(GX + 220, GY - 40, 420, 80, fill='#7a5a35', stroke='#5a4126', sw=2)
    for i, cx in enumerate((GX + 300, GX + 430, GX + 560)):
        d.ellipse(cx, GY - 20, 32, 22, fill='#6b4a2b', stroke='#4b331d', sw=2)
        for k in range(5): d.path(f'M{cx},{GY-40} q{-30+k*15},-40 {-36+k*18},-70', stroke=TURF_D, sw=4)
        d.circle(cx - 20, GY - 112, 10, fill='#e98aa0', stroke='#b35a72', sw=2); d.circle(cx + 18, GY - 104, 10, fill='#f2c14e', stroke='#b38a1e', sw=2)
    d.label(GX + 300, GY - 10, '根鉢', GX + 120, GY - 150); section_label(d)
    out(f'{slug}-04', d, '花壇づくりの手順4：花苗を植え付ける')
    d = base(5, '水やり・手入れを行う', '植え付け後はたっぷり水を与え、その後は土の乾き具合を見て水やりします')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 180, GX + 640): d.rect(x, GY - 60, 40, 100, fill=BRICK, stroke=BRICK_D, sw=2.5, rx=2)
    d.rect(GX + 220, GY - 40, 420, 80, fill='#6a4b2c', stroke='#5a4126', sw=2)
    for cx in (GX + 300, GX + 430, GX + 560):
        for k in range(5): d.path(f'M{cx},{GY-40} q{-30+k*15},-40 {-36+k*18},-70', stroke=TURF_D, sw=4)
    d.water_can(GX + 600, GY - 170, 1.0); section_label(d)
    out(f'{slug}-05', d, '花壇づくりの手順5：植え付け後に水やりをする')


# ---------------- レンガ花壇（No.36 DIYで花壇を作る方法：空積み） ----------------
def kadan_renga(slug):
    d = D('4:3'); d.step_header(1, '位置と形を決め、印をつける', 'ひもや砂、スプレーなどで地面に線を引きます')
    d.rect(80, 160, 800, 470, fill='#d9c49a', stroke=SOIL_D, sw=2, rx=8)
    d.rect(260, 280, 440, 220, fill='none', stroke=WHITE, sw=5, rx=4, dash='16 10')
    for x, y in ((260, 280), (700, 280), (260, 500), (700, 500)):
        d.rect(x - 6, y - 26, 12, 30, fill=WOOD, stroke=WOOD_D, sw=2)
    d.label(480, 280, 'ひもや線で形を描く', 480, 220, anchor='middle'); d.label(260, 500, '角に杭を打つ', 180, 590); d.note('上から見たイメージ', 700)
    out(f'{slug}-01', d, 'レンガ花壇の手順1：花壇の位置と形を決め、地面に印をつける')
    d = base(2, '印に沿って溝を掘る', '深さはレンガの半分程度が目安です')
    d.soil(GX, GY, GW, GH); d.rect(GX + 200, GY, 90, 40, fill='#9c7f55', stroke=SOIL_D, sw=2); d.rect(GX + 560, GY, 90, 40, fill='#9c7f55', stroke=SOIL_D, sw=2)
    d.dim_v(GX + 300, GY, GY + 40, 'レンガの半分程度', right=True); d.shovel(GX + 420, GY - 20, .9, -15); section_label(d)
    out(f'{slug}-02', d, 'レンガ花壇の手順2：印に沿って、レンガの半分程度の深さの溝を掘る')
    d = base(3, '溝に砂を敷き、土台を安定させる', '砂を平らにならし、レンガががたつかないようにします')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 200, GX + 560): d.rect(x, GY, 90, 40, fill='#9c7f55', stroke=SOIL_D, sw=2); d.sand(x, GY + 18, 90, 22)
    d.level(GX + 150, GY - 6, 200); d.label(GX + 245, GY + 30, '砂（平らにならす）', GX + 380, GY - 120); section_label(d)
    out(f'{slug}-03', d, 'レンガ花壇の手順3：溝に砂を敷いて平らにし、土台を安定させる')
    d = base(4, 'レンガを並べて積む', '目地が上下でずれるよう、互い違いに積むと安定します')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 200, GX + 560): d.sand(x, GY + 18, 90, 22)
    brick_wall(d, GX + 200, GY + 18, 7, 3, w=64, h=26)
    d.label(GX + 330, GY - 40, '互い違いに積む', GX + 330, GY - 150, anchor='middle')
    d.note('※ 高く積むほど土の圧力で崩れやすくなります。高さを出す場合は補強やモルタルを検討します', 700)
    out(f'{slug}-04', d, 'レンガ花壇の手順4：レンガを互い違いに並べて積む')
    d = base(5, '内側に土を入れ、植物を植える', '底に排水のすき間を設けると根腐れを防ぎやすくなります')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 200, GX + 560): d.sand(x, GY + 18, 90, 22)
    brick_wall(d, GX + 200, GY + 18, 1, 3, w=64, h=26); brick_wall(d, GX + 584, GY + 18, 1, 3, w=64, h=26)
    d.rect(GX + 264, GY - 60, 320, 78, fill='#6a4b2c', stroke='#5a4126', sw=2)
    for cx in (GX + 330, GX + 424, GX + 518):
        for k in range(5): d.path(f'M{cx},{GY-60} q{-30+k*15},-40 {-36+k*18},-70', stroke=TURF_D, sw=4)
        d.circle(cx - 18, GY - 128, 9, fill='#e98aa0', stroke='#b35a72', sw=2)
    d.label(GX + 300, GY, '培養土', GX + 120, GY - 140); section_label(d)
    out(f'{slug}-05', d, 'レンガ花壇の手順5：花壇の内側に土を入れ、植物を植える')


# ---------------- レンガを敷く（No.37） ----------------
def renga_shiku(slug):
    d = base(1, '範囲を掘り、整地する', 'レンガの厚み＋砂の厚み分を掘り下げます')
    d.soil(GX, GY, GW, GH); d.rect(GX + 160, GY, 520, 60, fill='none', stroke=SOIL_D, sw=2, dash='8 6'); d.text(GX + 420, GY + 38, '掘り下げる', 20, SOIL_D, 700, 'middle')
    d.shovel(GX + 600, GY - 20, .9, -15); d.dim_v(GX + 700, GY, GY + 60, 'レンガ＋砂の厚み分', right=True); section_label(d)
    out(f'{slug}-01', d, 'レンガを敷く手順1：レンガと砂の厚みの分だけ地面を掘り、整地する')
    d = base(2, '砂を敷いて平らにならす', '水平器で確認しながら、砂を均一な厚みに整えます')
    d.soil(GX, GY, GW, GH); d.rect(GX + 160, GY, 520, 60, fill='#b8996a', stroke=SOIL_D, sw=2); d.sand(GX + 160, GY + 30, 520, 30)
    d.level(GX + 290, GY + 26, 260); d.label(GX + 220, GY + 46, '砂（下地）', GX + 120, GY - 120); section_label(d)
    out(f'{slug}-02', d, 'レンガを敷く手順2：掘った部分に砂を敷き、水平器で確認しながら平らにならす')
    d = D('4:3'); d.step_header(3, 'レンガを並べて敷く', 'すき間（目地）の幅をそろえて並べます')
    d.rect(120, 200, 720, 440, fill=SAND, stroke=SAND_D, sw=2, rx=6)
    for r in range(6):
        off = 0 if r % 2 == 0 else 50
        for c in range(7):
            x = 150 + c * 100 - off
            if x < 140 or x + 92 > 830: continue
            d.rect(x, 225 + r * 66, 92, 56, fill=BRICK, stroke=BRICK_D, sw=2, rx=2)
    d.label(346, 252, '目地の幅をそろえる', 346, 160, anchor='middle'); d.note('上から見たイメージ（馬踏み目地の例）', 700)
    out(f'{slug}-03', d, 'レンガを敷く手順3：目地の幅をそろえてレンガを並べる')
    d = base(4, 'すき間に砂を入れて固定する', 'ほうきで砂を目地に掃き込み、レンガを固定します')
    d.soil(GX, GY, GW, GH); d.sand(GX + 160, GY + 30, 520, 30)
    x = GX + 160
    while x + 64 <= GX + 680:
        d.rect(x, GY - 6, 64, 36, fill=BRICK, stroke=BRICK_D, sw=2); d.rect(x + 64, GY - 6, 8, 36, fill=SAND_D, stroke='none'); x += 72
    d.brush(GX + 600, GY - 30, -20, .8)
    d.label(GX + 232, GY + 6, '目地に砂を入れる', GX + 140, GY - 140); section_label(d)
    out(f'{slug}-04', d, 'レンガを敷く手順4：レンガのすき間に砂を掃き込んで固定する')


# ---------------- ウッドデッキ（No.38） ----------------
def deck(slug):
    def ground(d): d.soil(GX, GY + 60, GW, GH - 60)
    def stones(d):
        for x in (GX + 120, GX + 400, GX + 680): d.rect(x, GY + 30, 70, 40, fill=CONC, stroke=CONC_D, sw=2.5)
    def posts(d):
        for x in (GX + 140, GX + 420, GX + 700): d.rect(x, GY - 120, 30, 150, fill=WOOD, stroke=WOOD_D, sw=2.5)
    def joist(d): d.rect(GX + 100, GY - 150, 680, 30, fill='#b88850', stroke=WOOD_D, sw=2.5)
    d = base(1, '設置場所を決め、水平を確認する', '地面の高低差を測り、デッキの高さを決めます')
    ground(d); d.level(GX + 250, GY + 60, 300); d.line(GX, GY - 150, GX + GW, GY - 150, stroke=GREY, sw=2, dash='8 8')
    d.text(GX + 10, GY - 162, 'デッキの仕上がり高さ', 19, '#6b6e66', 700); section_label(d)
    out(f'{slug}-01', d, 'ウッドデッキDIYの手順1：設置場所の水平を確認し、デッキの高さを決める')
    d = base(2, '束石を配置して固定する', '水平器で確認しながら、すべての束石の高さをそろえます')
    ground(d); stones(d); d.level(GX + 110, GY + 30, 670)
    d.label(GX + 155, GY + 50, '束石（つかいし）', GX + 140, GY - 120); section_label(d)
    out(f'{slug}-02', d, 'ウッドデッキDIYの手順2：束石を並べ、水平器で高さをそろえて固定する')
    d = base(3, '支柱（束）を立てる', '束石の上に、垂直を確認しながら支柱を立てます')
    ground(d); stones(d); posts(d); d.label(GX + 155, GY - 60, '支柱（束）', GX + 260, GY - 160); section_label(d)
    out(f'{slug}-03', d, 'ウッドデッキDIYの手順3：束石の上に支柱を垂直に立てる')
    d = base(4, '根太（ねだ）を取り付ける', '根太はデッキ材を支える横材。間隔が広すぎるとたわみます')
    ground(d); stones(d); posts(d); joist(d)
    d.label(GX + 300, GY - 135, '根太', GX + 300, GY - 220, anchor='middle')
    d.note('※ 根太の間隔は、使うデッキ材の厚みとメーカーの指示に合わせます', 700)
    out(f'{slug}-04', d, 'ウッドデッキDIYの手順4：支柱に根太を取り付ける')
    d = base(5, 'デッキ材を根太の上に固定する', '板と板の間にすき間をあけ、ビスで留めます')
    ground(d); stones(d); posts(d); joist(d)
    x = GX + 100
    while x < GX + 760: d.rect(x, GY - 172, 52, 22, fill=WOOD, stroke=WOOD_D, sw=2); x += 58
    d.dim_h(GX + 152, GX + 158, GY - 190, 'すき間をあける'); section_label(d)
    out(f'{slug}-05', d, 'ウッドデッキDIYの手順5：デッキ材をすき間をあけて根太の上に固定する')
    d = base(6, '必要に応じて階段・幕板を付ける', '高さがある場合は、転落防止の手すりも検討します')
    ground(d); stones(d); posts(d); joist(d)
    d.rect(GX + 100, GY - 176, 680, 26, fill=WOOD, stroke=WOOD_D, sw=2.5)
    d.rect(GX + 100, GY - 150, 680, 120, fill='#d9b07a', stroke=WOOD_D, sw=2.5)
    d.rect(GX + 780, GY - 100, 70, 20, fill=WOOD, stroke=WOOD_D, sw=2.5); d.rect(GX + 840, GY - 100, 14, 160, fill=WOOD, stroke=WOOD_D, sw=2); d.rect(GX + 780, GY - 40, 110, 20, fill=WOOD, stroke=WOOD_D, sw=2.5); d.rect(GX + 876, GY - 40, 14, 100, fill=WOOD, stroke=WOOD_D, sw=2); d.rect(GX + 790, GY - 20, 14, 80, fill=WOOD, stroke=WOOD_D, sw=2)
    d.label(GX + 300, GY - 90, '幕板（側面の板）', GX + 240, GY - 250); d.label(GX + 830, GY - 90, '階段', GX + 800, GY - 250, anchor='middle'); section_label(d)
    out(f'{slug}-06', d, 'ウッドデッキDIYの手順6：必要に応じて幕板や階段を取り付ける')


# ---------------- 目隠しフェンス（No.39） ----------------
def fence(slug):
    def post(d, x, top=GY - 260, depth=GY + 70): d.rect(x - 12, top, 24, depth - top, fill=METAL, stroke=METAL_D, sw=2.5)
    d = base(1, '設置位置を決め、支柱の位置に印をつける', '境界を確認し、自分の敷地内に収まる位置にします')
    d.soil(GX, GY, GW, GH); d.line(GX + 120, GY - 260, GX + 120, GY + GH, stroke=WARN, sw=3, dash='10 8')
    d.text(GX + 130, GY - 266, '境界線', 20, WARN, 700)
    for x in (GX + 220, GX + 500, GX + 780): d.add(f'<path d="M{x-12},{GY} l12,-22 l12,22z" fill="{GOLD}" stroke="#8a6d16" stroke-width="2"/>')
    d.dim_h(GX + 220, GX + 500, GY - 80, '支柱の間隔（製品の指示に従う）'); d.label(GX + 220, GY - 12, '印', GX + 260, GY - 170); section_label(d)
    out(f'{slug}-01', d, '目隠しフェンスDIYの手順1：境界を確認し、支柱を立てる位置に印をつける')
    d = base(2, '支柱を立てる穴を掘る', '地中に配管や配線がないか、事前に確認します')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 220, GX + 500, GX + 780): d.rect(x - 40, GY, 80, 110, fill='#9c7f55', stroke=SOIL_D, sw=2)
    d.shovel(GX + 420, GY - 10, .9, -15); d.dim_v(GX + 560, GY, GY + 110, '深さは製品の指示に従う'); section_label(d)
    out(f'{slug}-02', d, '目隠しフェンスDIYの手順2：支柱を立てる穴を掘る')
    d = base(3, '支柱を垂直に立て、モルタルで固定する', '水平器を当てて、前後左右の垂直を確認します')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 220, GX + 500, GX + 780):
        d.rect(x - 40, GY, 80, 110, fill='#c9c4b6', stroke=CONC_D, sw=2); post(d, x)
    d.add(f'<g transform="translate({GX+512},{GY-120}) rotate(90)"><rect x="-100" y="-13" width="200" height="26" rx="4" fill="#f2d26b" stroke="#a8892a" stroke-width="2.5"/><rect x="-30" y="-8" width="60" height="16" rx="8" fill="#d9f0d0" stroke="#6d8a5a" stroke-width="2"/></g>')
    d.label(GX + 200, GY + 80, 'モルタル（または基礎ブロック）', GX + 40, GY + 175 - 10, anchor='start'); section_label(d)
    out(f'{slug}-03', d, '目隠しフェンスDIYの手順3：支柱を垂直に立て、モルタルで固定する')
    d = base(4, 'モルタルが固まるまで養生する', '固まるまでの期間は、製品や気温で異なります（数日程度）')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 220, GX + 500, GX + 780):
        d.rect(x - 40, GY, 80, 110, fill='#c9c4b6', stroke=CONC_D, sw=2); post(d, x)
        d.line(x, GY - 200, x - 90, GY, stroke=WOOD_D, sw=4); d.line(x, GY - 200, x + 90, GY, stroke=WOOD_D, sw=4)
    d.label(GX + 545, GY - 100, '仮の支えで固定', GX + 640, GY - 220, anchor='middle')
    d.ng(GX + 80, GY - 290 + 10); d.text(GX + 115, GY - 272, '固まる前に触らない・パネルを付けない', 19, WARN, 700); section_label(d)
    out(f'{slug}-04', d, '目隠しフェンスDIYの手順4：モルタルが固まるまで支柱を固定したまま養生する')
    d = base(5, 'フェンス本体（パネル）を取り付ける', '付属の金具で、支柱にパネルを固定します')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 220, GX + 500, GX + 780): d.rect(x - 40, GY, 80, 110, fill='#c9c4b6', stroke=CONC_D, sw=2); post(d, x)
    for x1, x2 in ((GX + 232, GX + 488), (GX + 512, GX + 768)):
        for i in range(8): d.rect(x1, GY - 250 + i * 28, x2 - x1, 20, fill='#7a6a58', stroke='#4e4337', sw=2)
    d.label(GX + 360, GY - 140, 'パネル', GX + 360, GY - 300 + 10, anchor='middle'); section_label(d)
    out(f'{slug}-05', d, '目隠しフェンスDIYの手順5：支柱にフェンスのパネルを取り付ける')


# ---------------- 小道（No.40 敷石） ----------------
def komichi(slug):
    def top(d):
        d.rect(80, 160, 800, 470, fill=TURF, stroke=TURF_D, sw=2, rx=8)
    d = D('4:3'); d.step_header(1, '経路を決め、幅と形を確認する', '人が歩く線を想定して、ゆるやかなカーブにします'); top(d)
    d.path('M200,600 C320,480 380,360 560,300 S760,200 800,180', stroke=WHITE, sw=70, op=.35)
    d.path('M200,600 C320,480 380,360 560,300 S760,200 800,180', stroke=WHITE, sw=4, dash='14 10')
    d.label(420, 400, '歩く線（経路）', 520, 520); d.note('上から見たイメージ', 700)
    out(f'{slug}-01', d, '小道づくりの手順1：小道の経路を決め、幅と形を確認する')
    d = base(2, '経路に沿って土を掘り、整地する', '敷石の厚み＋砂の厚み分を掘ります')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 120, GX + 380, GX + 640): d.rect(x, GY, 160, 50, fill='#9c7f55', stroke=SOIL_D, sw=2)
    d.shovel(GX + 330, GY - 20, .9, -15); section_label(d)
    out(f'{slug}-02', d, '小道づくりの手順2：敷石を置く位置の土を掘り、整地する')
    d = base(3, '砂を薄く敷いて平らにならす', '敷石が安定するよう、砂の表面を平らにします')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 120, GX + 380, GX + 640): d.rect(x, GY, 160, 50, fill='#9c7f55', stroke=SOIL_D, sw=2); d.sand(x, GY + 26, 160, 24)
    d.label(GX + 200, GY + 38, '砂', GX + 140, GY - 120); section_label(d)
    out(f'{slug}-03', d, '小道づくりの手順3：掘った部分に砂を薄く敷いて平らにならす')
    d = D('4:3'); d.step_header(4, '敷石を一定の間隔で配置する', '間隔は歩幅を目安にします'); top(d)
    pts = [(240, 560), (330, 470), (430, 390), (540, 330), (650, 280), (760, 230)]
    for i, (x, y) in enumerate(pts): d.ellipse(x, y, 58, 36, fill='#c9c6bd', stroke='#8e8b82', sw=2.5)
    d.dim_h(240, 330, 610, '歩幅を目安に', above=False); d.note('上から見たイメージ', 700)
    out(f'{slug}-04', d, '小道づくりの手順4：歩幅を目安に、敷石を一定の間隔で配置する')
    d = base(5, '周りに砂利や砂を入れて固定する', '敷石の周りを埋めて、がたつきを防ぎます')
    d.soil(GX, GY, GW, GH)
    for x in (GX + 120, GX + 380, GX + 640):
        d.sand(x, GY + 26, 160, 24); d.rect(x + 10, GY - 8, 140, 34, fill='#c9c6bd', stroke='#8e8b82', sw=2.5, rx=6)
    for x0, x1 in ((GX, GX + 120), (GX + 280, GX + 380), (GX + 540, GX + 640), (GX + 800, GX + GW)):
        d.gravel_layer(x0, GY - 8, x1 - x0, 30, r=(5, 8))
    d.label(GX + 330, GY + 6, '砂利で周りを埋める', GX + 330, GY - 120, anchor='middle'); section_label(d)
    out(f'{slug}-05', d, '小道づくりの手順5：敷石の周りに砂利や砂を入れて固定する')


# ---------------- タイル（No.41 砂敷き工法） ----------------
def tile(slug):
    d = base(1, '範囲を掘り、整地する', 'タイルの厚み＋砂の厚み分を掘り、平らにします')
    d.soil(GX, GY, GW, GH); d.rect(GX + 120, GY, 600, 56, fill='none', stroke=SOIL_D, sw=2, dash='8 6'); d.shovel(GX + 620, GY - 20, .9, -15); section_label(d)
    out(f'{slug}-01', d, 'タイル敷きの手順1：敷く範囲を掘り、整地する')
    d = base(2, '砂を敷いて転圧し、平らにならす', '水はけのため、わずかな傾きをつけます')
    d.soil(GX, GY, GW, GH); d.sand(GX + 120, GY + 20, 600, 36); d.tamper(GX + 420, GY + 20, .9)
    d.label(GX + 200, GY + 40, '砂（転圧する）', GX + 120, GY - 140); section_label(d)
    out(f'{slug}-02', d, 'タイル敷きの手順2：砂を敷いて転圧し、平らにならす')
    d = base(3, '水平を確認しながらタイルを配置する', 'わずかな傾き（水勾配）は保ちつつ、凹凸が出ないようにします')
    d.soil(GX, GY, GW, GH); d.sand(GX + 120, GY + 20, 600, 36)
    x = GX + 120
    while x + 90 <= GX + 720: d.rect(x, GY - 2, 90, 22, fill='#e2ddd2', stroke='#9e988a', sw=2); x += 100
    d.level(GX + 220, GY - 2, 300); section_label(d)
    out(f'{slug}-03', d, 'タイル敷きの手順3：水平器で確認しながらタイルを配置する')
    d = base(4, 'すき間に目地材を入れて固定する', '目砂や専用の目地材を入れ、タイルを固定します')
    d.soil(GX, GY, GW, GH); d.sand(GX + 120, GY + 20, 600, 36)
    x = GX + 120
    while x + 90 <= GX + 720: d.rect(x, GY - 2, 90, 22, fill='#e2ddd2', stroke='#9e988a', sw=2); d.rect(x + 90, GY - 2, 10, 22, fill=SAND_D, stroke='none'); x += 100
    d.brush(GX + 560, GY - 30, -20, .8); d.label(GX + 215, GY + 8, '目地（目砂・専用材）', GX + 140, GY - 140); section_label(d)
    out(f'{slug}-04', d, 'タイル敷きの手順4：タイルのすき間に目砂や専用材を入れて固定する')


# ---------------- 物置（No.44） ----------------
def monooki(slug):
    def blocks(d, xs=(GX + 200, GX + 400, GX + 600)):
        for x in xs: d.rect(x, GY - 40, 90, 60, fill=CONC, stroke=CONC_D, sw=2.5)
    d = D('4:3'); d.step_header(1, '設置場所を決め、周囲のスペースを確認する', '扉の開閉や、隣地境界・排水の流れも確認します')
    d.rect(100, 160, 760, 470, fill='#e8efe0', stroke=GREEN, sw=2.5, rx=8)
    d.rect(330, 300, 300, 160, fill='#cfd6d9', stroke=METAL_D, sw=2.5); d.text(480, 390, '物置', 24, INK, 700, 'middle')
    d.rect(330, 460, 300, 110, fill='none', stroke=WARN, sw=3, dash='10 8'); d.text(480, 525, '扉の開閉・出し入れのスペース', 18, WARN, 700, 'middle')
    d.line(130, 160, 130, 630, stroke=WARN, sw=3, dash='10 8'); d.text(140, 190, '境界', 19, WARN, 700)
    d.dim_h(130, 330, 280, '境界からの距離を確認'); d.note('上から見たイメージ', 700)
    out(f'{slug}-01', d, '物置設置の手順1：設置場所と扉の開閉スペース、境界からの距離を確認する')
    d = base(2, '地面を整地し、水平を確認する', '凹凸をなくし、締め固めておきます')
    d.soil(GX, GY, GW, GH); d.compact_marks(GX, GY, GW); d.level(GX + 270, GY, 300); section_label(d)
    out(f'{slug}-02', d, '物置設置の手順2：地面を整地して水平を確認する')
    d = base(3, '基礎（ブロック・土台）を設置する', 'コンクリートブロックや専用の土台を、物置の脚の位置に置きます')
    d.soil(GX, GY, GW, GH); blocks(d); d.label(GX + 245, GY - 20, '基礎ブロック', GX + 160, GY - 160); section_label(d)
    out(f'{slug}-03', d, '物置設置の手順3：物置の脚の位置に基礎ブロックを設置する')
    d = base(4, '基礎の水平を水平器で確認する', 'すべての基礎の高さがそろっているか確かめます')
    d.soil(GX, GY, GW, GH); blocks(d); d.level(GX + 190, GY - 40, 510); section_label(d)
    out(f'{slug}-04', d, '物置設置の手順4：水平器で基礎の高さがそろっているか確認する')
    d = base(5, '物置を組み立て、基礎の上に固定する', '強風に備え、転倒防止のアンカー固定も検討します')
    d.soil(GX, GY, GW, GH); blocks(d)
    d.rect(GX + 180, GY - 250, 530, 210, fill='#cfd6d9', stroke=METAL_D, sw=3); d.line(GX + 445, GY - 240, GX + 445, GY - 50, stroke=METAL_D, sw=2.5)
    d.rect(GX + 170, GY - 266, 550, 20, fill='#aab3b8', stroke=METAL_D, sw=2.5)
    d.line(GX + 190, GY - 40, GX + 110, GY + 70, stroke=GOLD, sw=5); d.rect(GX + 98, GY + 60, 24, 40, fill=METAL, stroke=METAL_D, sw=2)
    d.label(GX + 130, GY + 40, '転倒防止アンカー（推奨）', GX + 40, GY - 150); section_label(d)
    out(f'{slug}-05', d, '物置設置の手順5：物置を組み立てて基礎の上に設置し、固定する')


# ---------------- ガーデンライト（No.46 ソーラー式） ----------------
def light(slug):
    def lamp(d, x, on=False):
        d.rect(x - 4, GY - 120, 8, 150, fill='#555', stroke='#333', sw=2)
        d.rect(x - 26, GY - 160, 52, 44, fill='#3d3d3d', stroke='#222', sw=2, rx=6)
        d.rect(x - 24, GY - 168, 48, 10, fill='#4a6a8a', stroke='#2c4256', sw=2)
        if on:
            d.circle(x, GY - 138, 34, fill='#fff3b0', stroke='none', op=.7); d.circle(x, GY - 138, 14, fill='#ffe066', stroke='none')
    d = base(1, '日当たりのよい場所を選ぶ', '太陽光パネルに日が当たる時間で、点灯時間が変わります')
    d.soil(GX, GY + 30, GW, GH - 30); d.circle(GX + 720, 200, 50, fill='#f6d36b', stroke='#c9a73a', sw=2.5)
    for k in range(4): d.line(GX + 660 - k * 30, 250 + k * 10, GX + 420 - k * 30, GY - 40 + k * 10, stroke='#e9c454', sw=3, dash='10 10')
    d.rect(GX + 120, GY - 60, 220, 90, fill='#d9d5cc', stroke=GREY, sw=2); d.text(GX + 230, GY - 6, '建物の影', 18, INK, 700, 'middle')
    d.ok(GX + 450, GY - 30); d.ng(GX + 230, GY - 100); section_label(d)
    out(f'{slug}-01', d, 'ガーデンライト設置の手順1：太陽光パネルに日が当たる場所を選ぶ')
    d = base(2, '杭やスタンドを地面に挿す', '地面がかたい場合は、先に穴をあけてから挿します')
    d.soil(GX, GY + 30, GW, GH - 30)
    for x in (GX + 240, GX + 520): d.rect(x - 5, GY - 30, 10, 120, fill='#555', stroke='#333', sw=2); d.add(f'<path d="M{x-5},{GY+90} l5,16 l5,-16z" fill="#555"/>')
    d.arrow(GX + 240, GY - 130, GX + 240, GY - 50); d.label(GX + 520, GY + 60, '杭（地面に挿す）', GX + 620, GY - 120); section_label(d)
    out(f'{slug}-02', d, 'ガーデンライト設置の手順2：ライトの杭を地面に挿す')
    d = base(3, '本体を取り付け、点灯を確認する', '暗くなってから、明るさと照らす向きを確認します')
    d.bg = '#2e3a4a'; d.soil(GX, GY + 30, GW, GH - 30)
    for x in (GX + 200, GX + 440, GX + 680): lamp(d, x, True)
    d.el = [e.replace(f'fill="{INK}"', 'fill="#ffffff"').replace('fill="#4a4d46"', 'fill="#e6e9ee"') for e in d.el]
    out(f'{slug}-03', d, 'ガーデンライト設置の手順3：本体を取り付け、暗くなってから点灯を確認する')


# ---------------- 土の入れ替え（No.47） ----------------
def soil_change(slug):
    d = base(1, '既存の土を掘り出す', 'スコップで掘り、手押し車で運びます')
    d.soil(GX, GY, GW, GH); d.rect(GX + 160, GY, 520, 90, fill='#9c7f55', stroke=SOIL_D, sw=2); d.shovel(GX + 420, GY + 20, .9, -15)
    d.rect(GX + 720, GY - 90, 120, 60, fill='#6c8a99', stroke='#3f5866', sw=2.5, rx=6); d.circle(GX + 750, GY - 20, 18, fill='#555', stroke='#333', sw=2)
    d.text(GX + 780, GY - 110, '手押し車', 18, INK, 700, 'middle'); section_label(d)
    out(f'{slug}-01', d, '土の入れ替えの手順1：スコップで既存の土を掘り出す')
    d = D('4:3'); d.step_header(2, '掘り出した土の状態を確認する', '粘土質か、石が多いかを確かめ、入れる土を決めます')
    for i, (t, col, desc) in enumerate((('粘土質', '#9a7b57', '水はけが悪い・固まりやすい'), ('石・根が多い', '#b19b78', 'ふるいで取り除く'), ('砂っぽい', '#d8c69c', '水もちが悪い'))):
        x = 90 + i * 270
        d.rect(x, 200, 240, 260, fill=WHITE, stroke=GREY, sw=2, rx=10)
        d.ellipse(x + 120, 320, 90, 60, fill=col, stroke=SOIL_D, sw=2.5)
        if i == 1:
            for k in range(6): d.ellipse(x + 70 + k * 18, 310 + (k % 2) * 20, 9, 7, fill=GRAVEL, stroke=GRAVEL_D, sw=1.5)
        d.text(x + 120, 420, t, 22, INK, 700, 'middle'); d.text(x + 120, 500, desc, 17, '#4a4d46', 500, 'middle')
    d.note('※ 状態に合わせて、培養土や改良材の種類と量を決めます', 700)
    out(f'{slug}-02', d, '土の入れ替えの手順2：掘り出した土が粘土質か、石が多いかなどを確認する')
    d = base(3, '新しい土を入れる', '培養土や改良用の土を、少しずつ入れて均します')
    d.soil(GX, GY, GW, GH); d.rect(GX + 160, GY, 520, 90, fill='#6a4b2c', stroke='#5a4126', sw=2)
    d.rect(GX + 640, GY - 150, 150, 100, fill='#7b9a5a', stroke='#4f6a35', sw=2.5, rx=8); d.text(GX + 715, GY - 92, '培養土', 20, WHITE, 700, 'middle')
    d.curved_arrow(GX + 640, GY - 110, GX + 520, GY - 160, GX + 440, GY - 20); section_label(d)
    out(f'{slug}-03', d, '土の入れ替えの手順3：培養土などの新しい土を入れる')
    d = base(4, '腐葉土や堆肥を混ぜ込む', 'スコップで全体をよく混ぜ、ふかふかの土にします')
    d.soil(GX, GY, GW, GH); d.rect(GX + 160, GY, 520, 90, fill='#6a4b2c', stroke='#5a4126', sw=2)
    for i in range(60): d.circle(GX + 170 + d.rnd.uniform(0, 500), GY + 8 + d.rnd.uniform(0, 74), 3.2, fill='#3d2a18', stroke='none')
    d.shovel(GX + 420, GY + 10, .9, 15); d.label(GX + 250, GY + 40, '腐葉土・堆肥', GX + 120, GY - 140); section_label(d)
    out(f'{slug}-04', d, '土の入れ替えの手順4：腐葉土や堆肥を混ぜ込む')
    d = base(5, '植え付け前に土をなじませる', '水をまいて数日おくと、土が落ち着いて植え付けやすくなります')
    d.soil(GX, GY, GW, GH); d.rect(GX + 160, GY, 520, 90, fill='#5d4127', stroke='#5a4126', sw=2); d.water_can(GX + 560, GY - 150, 1.0)
    d.note('※ なじませる期間の目安は、使う土や改良材の表示に従います', 700)
    out(f'{slug}-05', d, '土の入れ替えの手順5：水をまいて土をなじませてから植え付ける')


# ---------------- 段差の解消（No.48 ステップ） ----------------
def dansa(slug):
    Y0 = GY - 160; R = 160 / 3; T = 120  # riser, tread
    def ground(d):
        d.poly([(GX, Y0), (GX + 300, Y0), (GX + 300, GY), (GX + GW, GY), (GX + GW, GY + GH), (GX, GY + GH)], fill=SOIL, stroke=SOIL_D, sw=2)
    def fill(d):  # 盛り土（ステップの下）
        d.poly([(GX + 300, Y0 + R), (GX + 300 + T, Y0 + R), (GX + 300 + T, Y0 + 2 * R), (GX + 300 + 2 * T, Y0 + 2 * R), (GX + 300 + 2 * T, GY), (GX + 300, GY)], fill='#b8996a', stroke=SOIL_D, sw=2)
    def treads(d, marks=False):
        for k in range(2):
            x = GX + 300 + k * T; y = Y0 + (k + 1) * R
            d.rect(x, y - 26, T, 26, fill=WOOD, stroke=WOOD_D, sw=2.5)
            if marks: d.compact_marks(x, y, T)
    d = base(1, '段差の高さを測る', 'メジャーで、上の地面から下の地面までを測ります')
    ground(d); d.dim_v(GX + 330, Y0, GY, '段差の高さ'); section_label(d)
    out(f'{slug}-01', d, '段差解消の手順1：段差の高さを測る')
    d = base(2, '必要な段数を決める', '段差を等分して、1段の高さと奥行きをそろえます')
    ground(d)
    pts = [(GX + 300, Y0), (GX + 300, Y0 + R), (GX + 300 + T, Y0 + R), (GX + 300 + T, Y0 + 2 * R), (GX + 300 + 2 * T, Y0 + 2 * R), (GX + 300 + 2 * T, GY)]
    d.path('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts), stroke=WARN, sw=3, dash='10 6')
    d.dim_v(GX + 300 + 2 * T + 30, Y0 + 2 * R, GY, '1段の高さ（そろえる）'); d.dim_h(GX + 300 + T, GX + 300 + 2 * T, Y0 - 40, '奥行き（そろえる）'); section_label(d)
    out(f'{slug}-02', d, '段差解消の手順2：段差を等分し、1段の高さと奥行きをそろえて計画する')
    d = base(3, '枕木やブロックでステップを作る', '必要に応じて土を盛り、計画した高さで材料を据えます')
    ground(d); fill(d); treads(d)
    d.label(GX + 360, Y0 + R - 13, '枕木（またはブロック）', GX + 460, Y0 - 60)
    d.label(GX + 420, GY - 30, '盛り土', GX + 640, GY - 120); section_label(d)
    out(f'{slug}-03', d, '段差解消の手順3：土を盛り、枕木やブロックでステップを作る')
    d = base(4, 'ステップの位置を固定する', '下をしっかり突き固め、ぐらつかないように固定します')
    ground(d); fill(d); treads(d, True)
    d.ok(GX + 560, Y0 - 40); d.text(GX + 590, Y0 - 32, '段の高さがそろっている', 19, GREEN, 700)
    d.note('※ 雨で滑りやすい素材は避け、滑り止めのある材料を選びます', 700)
    out(f'{slug}-04', d, '段差解消の手順4：ステップの下を突き固め、ぐらつかないように固定する')


# ---------------- 24時間換気（No.110） ----------------
def kanki(slug):
    def wall(d):
        d.rect(80, 150, 360, 500, fill='#f1eee6', stroke=GREY, sw=2)
    d = D('4:3'); d.step_header(1, 'カバーを外す', '給気口のカバーを回す・引くなど、機種の方法で外します')
    wall(d); d.circle(260, 400, 90, fill=WHITE, stroke=GREY, sw=3); d.circle(260, 400, 60, fill='#e8e8e3', stroke=GREY, sw=2)
    d.curved_arrow(380, 300, 460, 360, 380, 470, color=GREEN)
    d.circle(650, 400, 90, fill=WHITE, stroke=GREY, sw=3); d.text(650, 408, 'カバー', 22, INK, 700, 'middle')
    d.note('※ 外し方は機種によって異なります。取扱説明書を確認してください', 700)
    out(f'{slug}-01', d, '換気口の掃除手順1：給気口のカバーを外す')
    d = D('4:3'); d.step_header(2, 'フィルターのホコリを取る', '掃除機で吸い取るか、水洗いできる機種は水洗いします')
    d.circle(320, 400, 130, fill='#eceae2', stroke=GREY, sw=3)
    for i in range(30): d.circle(320 + d.rnd.uniform(-100, 100), 400 + d.rnd.uniform(-100, 100), 5, fill='#b9b4a6', stroke='none')
    d.rect(520, 300, 260, 40, fill='#8a9aa3', stroke=METAL_D, sw=2.5, rx=8); d.rect(470, 310, 60, 20, fill='#5f6e76', stroke=METAL_D, sw=2.5, rx=4)
    d.text(650, 380, '掃除機で吸う', 20, INK, 700, 'middle')
    d.note('※ 水洗いの可否は機種によります。洗ったらしっかり乾かします', 700)
    out(f'{slug}-02', d, '換気口の掃除手順2：フィルターのホコリを掃除機で吸い取る')
    d = D('4:3'); d.step_header(3, 'カバーを拭いて元に戻す', '汚れが落ちない場合や劣化している場合は、フィルターを交換します')
    wall(d); d.circle(260, 400, 90, fill=WHITE, stroke=GREY, sw=3); d.circle(260, 400, 60, fill=WHITE, stroke=GREY, sw=2)
    d.ok(380, 300); d.rect(560, 300, 220, 160, fill=WHITE, stroke=GREY, sw=2, rx=10); d.text(670, 370, '交換用フィルター', 19, INK, 700, 'middle'); d.text(670, 405, '（メーカー推奨の時期に）', 16, '#4a4d46', 500, 'middle')
    out(f'{slug}-03', d, '換気口の掃除手順3：カバーを拭いて元に戻す。必要に応じてフィルターを交換する')


# ---------------- 保温材の巻き方（No.149） ----------------
def hoon(slug):
    def pipe(d, y=380):
        d.rect(100, y - 18, 760, 36, fill=METAL, stroke=METAL_D, sw=2.5, rx=18)
    d = D('4:3'); d.step_header(1, '露出している配管を確認する', '屋外の立水栓や、北側など日が当たらない配管が要注意です')
    pipe(d); d.label(300, 380, '保温材がない露出部分', 300, 250, anchor='middle'); d.ng(560, 250)
    out(f'{slug}-01', d, '凍結防止の手順1：保温材が巻かれていない露出した配管を確認する')
    d = D('4:3'); d.step_header(2, '保温材を配管にかぶせる', '配管の太さに合った筒状の保温材を、すき間なくかぶせます')
    pipe(d); d.rect(240, 336, 420, 88, fill='#d9dfe3', stroke='#8a979e', sw=2.5, rx=40)
    d.line(240, 336, 660, 336, stroke='#8a979e', sw=2.5); d.dim_h(240, 660, 300, 'すき間なく覆う')
    out(f'{slug}-02', d, '凍結防止の手順2：筒状の保温材を配管にすき間なくかぶせる')
    d = D('4:3'); d.step_header(3, 'テープを巻いて固定する', '重ねながら巻き、雨水が入らないようにします')
    pipe(d); d.rect(240, 336, 420, 88, fill='#d9dfe3', stroke='#8a979e', sw=2.5, rx=40)
    for i in range(12): d.add(f'<path d="M{250+i*34},{336} l20,88" stroke="#4a6a8a" stroke-width="10" opacity=".85"/>')
    d.label(450, 420, '保温テープを重ねて巻く', 450, 540, anchor='middle')
    out(f'{slug}-03', d, '凍結防止の手順3：保温テープを重ねながら巻いて固定する')


# ---------------- 人工芝のお手入れ（ページ turf-care） ----------------
def turf_care(slug):
    d = base(1, '落ち葉・ゴミを取る', '熊手やブロワーで、表面のゴミを集めます')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8); d.turf(GX, GY - 8, GW)
    for i in range(10): d.ellipse(GX + 60 + i * 70, GY - 40 - (i % 3) * 6, 18, 8, fill='#c98b3c', stroke='#8a5a1e', sw=1.5)
    d.rake(GX + 640, GY - 40, 1, -30); section_label(d)
    out(f'{slug}-01', d, '人工芝のお手入れ1：熊手で落ち葉やゴミを取り除く')
    d = base(2, 'ブラッシングで芝を起こす', '芝目と逆方向にブラシをかけます')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8); d.turf(GX, GY - 8, 380, blade=14, dense=9); d.turf(GX + 460, GY - 8, 380, blade=30)
    d.brush(GX + 430, GY - 60, -10, .9); section_label(d)
    out(f'{slug}-02', d, '人工芝のお手入れ2：ブラシで寝てしまった芝を起こす')
    d = base(3, '水で汚れを流す', '砂ぼこりや花粉、ペットの汚れをホースで洗い流します')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8); d.turf(GX, GY - 8, GW)
    d.hose_spray(GX + 660, GY - 150, GX + 300, GY - 40)
    for x in range(GX + 120, GX + 600, 90): d.arrow(x, GY + 10, x, GY + 60, color=WATER_D, sw=2.5, head=10)
    d.label(GX + 300, GY + 40, '水は下地へ抜ける', GX + 140, GY - 140); section_label(d)
    out(f'{slug}-03', d, '人工芝のお手入れ3：ホースで水をかけて汚れを流す')


if __name__ == '__main__':
    import sys, os, json
    gravel('jari-jibun-shikikata-chui'); kadan('niwa-kadan-tsukurikata'); kadan_renga('diy-kadan-tsukurikata-renga'); renga_shiku('renga-niwazukuri-diy')
    deck('diy-wood-deck-tsukurikata'); fence('diy-mekakushi-fence-setti'); komichi('diy-niwa-komichi-tsukurikata'); tile('diy-niwa-tile-shikikata')
    monooki('diy-niwa-monooki-setti'); light('diy-niwa-garden-light-setti'); soil_change('niwa-tsuchi-irekae-houhou'); dansa('diy-niwa-dansa-kaishou')
    kanki('24jikan-kanki-souji'); hoon('suidoukan-touketsu-boushi'); turf_care('turf-care')
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
