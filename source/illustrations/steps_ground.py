"""Step illustrations for ground work (cross-section view): 防草シート / 人工芝 / 砂利 / 小道 / タイル / レンガ / 土の入れ替え"""
from lib import *

OUT = {}

def out(name, d, alt):
    OUT[name] = (d, alt)


def base(n, title, sub=None):
    d = D('4:3'); d.step_header(n, title, sub)
    return d

GX, GW, GY, GH = 60, 840, 440, 200  # ground x, width, top y, height


def section_label(d):
    return d.text(GX + GW, GY + GH + 30, '断面イメージ', 17, '#8f928a', 500, 'end')


# ======================= 防草シート（No.33 bousou-sheet-shikikata-tejun） =======================
def sheet_steps(slug):
    # 1 除草・石の除去
    d = base(1, '雑草・石を取り除く', '根まで抜き取り、石やゴミも取り除きます')
    d.soil(GX, GY, GW, GH, rough=True); d.weeds(GX + 40, GY, 7, 520); d.stones(GX + 600, GY + 2, 4, 200)
    d.label(GX + 150, GY + 20, '根から抜く', GX + 200, GY - 110)
    d.label(GX + 690, GY - 6, '石・ゴミも除去', GX + 690, GY - 110, anchor='middle')
    section_label(d); out(f'{slug}-01', d, '防草シートの手順1：雑草を根から抜き、石やゴミを取り除く様子の断面イラスト')
    # 2 整地
    d = base(2, '地面を平らにならす（整地）', 'でこぼこを均し、水が流れるようわずかな傾きをつけます')
    d.soil(GX, GY, GW, GH); d.rake(560, GY - 2, 1.0, -28)
    d.line(GX, GY - 40, GX + GW, GY - 40, stroke=GREY, sw=2, dash='8 8')
    d.text(GX + 10, GY - 52, '仕上がりの高さ', 18, '#6b6e66', 600)
    d.arrow(GX + 120, GY + 40, GX + 360, GY + 52, color=WATER_D, sw=3)
    d.text(GX + 130, GY + 86, '水の流れ（わずかな勾配）', 18, WATER_D, 700)
    section_label(d); out(f'{slug}-02', d, '防草シートの手順2：レーキで地面を平らにならし、水が流れる程度の傾きをつける')
    # 3 シートを敷く
    d = base(3, 'シートを端から広げる', 'たるみやシワができないように、端から順に広げます')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, 520, 8)
    # roll
    d.circle(GX + 560, GY - 28, 28, fill=SHEET, stroke='#222', sw=2); d.circle(GX + 560, GY - 28, 9, fill='#777', stroke='none')
    d.arrow(GX + 610, GY - 70, GX + 760, GY - 70, color=GREEN, sw=3)
    d.text(GX + 610, GY - 84, '広げる方向', 18, GREEN, 700)
    d.label(GX + 200, GY - 4, 'たるみ・シワを作らない', GX + 120, GY - 110)
    section_label(d); out(f'{slug}-03', d, '防草シートの手順3：シートを端からたるみがないように広げる')
    # 4 重ね幅
    d = base(4, '継ぎ目は十分に重ねる', '重ね幅は10〜15cm程度が目安（製品の指示に従う）')
    d.soil(GX, GY, GW, GH)
    d.sheet(GX, GY, 470, 8); d.rect(GX + 380, GY - 17, 460, 8, fill='#55594f', stroke='#55594f', sw=1)
    d.dim_h(GX + 380, GX + 470, GY - 60, '重ね幅 10〜15cm程度')
    d.rect(GX + 380, GY - 22, 90, 4, fill=GOLD, stroke='none')
    d.label(GX + 425, GY - 20, '専用テープで目張り', GX + 560, GY - 130)
    d.ng(GX + 20, 200); d.text(GX + 55, 208, '重ねが少ないと、すき間から雑草が出る', 19, WARN, 700)
    section_label(d); out(f'{slug}-04', d, '防草シートの手順4：継ぎ目を10〜15cm程度重ね、専用テープで目張りする')
    # 5 ピン固定
    d = base(5, '固定ピンで一定間隔に留める', '継ぎ目と外周は間隔をつめて固定します')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8)
    for i, x in enumerate(range(GX + 60, GX + GW, 120)): d.pin(x, GY - 8, 48)
    d.dim_h(GX + 60, GX + 180, GY - 70, 'ピンの間隔（製品の指示に従う）')
    d.hammer(GX + 700, GY - 120, -40)
    d.label(GX + 300, GY - 12, 'ピンの頭にも保護テープを貼ると安心', GX + 330, GY - 160, anchor='middle')
    section_label(d); out(f'{slug}-05', d, '防草シートの手順5：固定ピンを一定の間隔で打ち込み、シートを留める')
    # 6 表面材
    d = base(6, '必要に応じて表面材を敷く', '砂利や人工芝を重ねると、シートの劣化も防げます')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8)
    d.gravel_layer(GX, GY - 58, 400, 50)
    d.turf(GX + 440, GY - 8, 400)
    d.text(GX + 200, GY - 84, '砂利', 22, INK, 700, 'middle'); d.text(GX + 640, GY - 60, '人工芝', 22, INK, 700, 'middle')
    d.label(GX + 220, GY - 4, '防草シート', GX + 300, GY + 90)
    d.note(y=700, t='※ 表面材は必須ではありません。シートだけで使う場合は耐候性の高い製品を選びます')
    out(f'{slug}-06', d, '防草シートの手順6：シートの上に砂利や人工芝などの表面材を敷く')


# ======================= 人工芝 DIY（No.34 jinkoshiba-diy-shikikata） =======================
def turf_diy(slug):
    d = base(1, '除草して地面を整地する', '雑草を根から取り、凹凸をなくして平らにします')
    d.soil(GX, GY, 420, GH, rough=True); d.weeds(GX + 30, GY, 4, 360)
    d.soil(GX + 420, GY, 420, GH); d.rake(GX + 720, GY - 2, 1, -28)
    d.arrow(GX + 360, 330, GX + 480, 330, color=GREEN, sw=4); d.text(GX + 420, 312, '除草・整地', 20, GREEN, 700, 'middle')
    section_label(d); out(f'{slug}-01', d, '人工芝DIYの手順1：雑草を取り除き、地面を平らに整地する')

    d = base(2, '防草シートを敷き、ピンで留める', '継ぎ目を重ね、外周と継ぎ目をピンで固定します')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8)
    for x in range(GX + 60, GX + GW, 130): d.pin(x, GY - 8, 46)
    d.label(GX + 330, GY - 6, '防草シート', GX + 330, GY - 110, anchor='middle'); d.label(GX + 580, GY + 20, '固定ピン（U字ピン）', GX + 640, GY + 110)
    section_label(d); out(f'{slug}-02', d, '人工芝DIYの手順2：防草シートを敷き、固定ピンで留める')

    d = base(3, '必要に応じて砂を敷き、転圧する', '薄く砂を敷いて表面を整え、しっかり締め固めます')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8); d.sand(GX, GY - 32, GW, 24)
    d.tamper(GX + 520, GY - 32, 1.0)
    d.label(GX + 200, GY - 20, '砂（薄く）', GX + 120, GY - 130)
    d.note(y=700, t='※ 砂を敷く位置（シートの上か下か）は、製品や下地の状態によって異なります')
    out(f'{slug}-03', d, '人工芝DIYの手順3：必要に応じて砂を薄く敷き、タンパーで転圧して地面を固める')

    d = D('4:3'); d.step_header(4, '敷く範囲に合わせてカットする', '裏面から、基布の目に沿ってカッターで切ります')
    # top view of turf roll back side
    d.rect(140, 200, 680, 380, fill='#e9e4d6', stroke='#9e988a', sw=2.5, rx=6)
    for i in range(1, 12): d.line(140 + i * 56.6, 200, 140 + i * 56.6, 580, stroke='#cfc8b6', sw=1.5)
    for i in range(1, 7): d.line(140, 200 + i * 54.3, 820, 200 + i * 54.3, stroke='#cfc8b6', sw=1.5)
    d.line(480, 190, 480, 590, stroke=WARN, sw=3, dash='12 8')
    d.cutter(500, 330, -80, 1.1)
    d.label(250, 260, '人工芝の裏面', 170, 160)
    d.label(480, 560, 'カットライン（基布の目に沿う）', 560, 640)
    d.note(y=700, t='※ 少し大きめに切り、敷いてから端を合わせると失敗しにくい')
    out(f'{slug}-04', d, '人工芝DIYの手順4：人工芝を裏返し、基布の目に沿ってカッターで切る')

    d = D('4:3'); d.step_header(5, '芝目をそろえて敷き、継ぎ目を合わせる', '毛の流れる向き（芝目）がそろわないと色が違って見えます')
    # top view two sheets with arrows
    for k, x in enumerate((110, 480)):
        d.rect(x, 190, 370, 400, fill=TURF, stroke=TURF_D, sw=2.5)
        for i in range(10):
            for j in range(9):
                xx = x + 18 + i * 36; yy = 210 + j * 44
                d.path(f'M{xx},{yy+16} l8,-14', stroke=TURF_D, sw=2.2)
    d.arrow(240, 420, 340, 420, color=WHITE, sw=5); d.arrow(610, 420, 710, 420, color=WHITE, sw=5)
    d.text(295, 470, '芝目', 22, WHITE, 700, 'middle'); d.text(660, 470, '芝目', 22, WHITE, 700, 'middle')
    d.line(480, 180, 480, 600, stroke=GOLD, sw=4, dash='10 8')
    d.label(480, GH, '継ぎ目はすき間なく突き合わせ', 560, 150)
    d.ok(120, 640); d.text(156, 648, '芝目の向きを同じ方向にそろえる', 21, GREEN, 700)
    out(f'{slug}-05', d, '人工芝DIYの手順5：芝目の向きをそろえて人工芝を並べ、継ぎ目を突き合わせる')

    d = base(6, 'ジョイントテープとピンで固定する', '継ぎ目の下にテープを敷いて接着し、外周をピンで留めます')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8)
    d.rect(GX + 330, GY - 14, 180, 6, fill=GOLD, stroke='none')
    d.turf(GX, GY - 14, 418); d.turf(GX + 422, GY - 14, 418)
    for x in (GX + 40, GX + 800): d.pin(x, GY - 14 - 8, 52)
    d.label(GX + 420, GY - 12, 'ジョイントテープ（裏で接着）', GX + 420, GY - 130, anchor='middle')
    d.label(GX + 40, GY - 26, 'U字ピン', GX + 80, GY + 110)
    d.label(GX + 800, GY - 26, '外周もピンで固定', GX + 790, GY + 110, anchor='end')
    section_label(d); out(f'{slug}-06', d, '人工芝DIYの手順6：継ぎ目をジョイントテープで接着し、外周をU字ピンで固定する')

    d = base(7, 'ブラッシングで芝を起こして整える', '芝目と逆方向にブラシをかけると、パイルが立ち上がります')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, GW, 8)
    d.turf(GX, GY - 8, 380, blade=14, dense=9)  # laid down
    d.turf(GX + 460, GY - 8, 380, blade=30)
    d.brush(GX + 430, GY - 60, -10, .9)
    d.text(GX + 190, GY - 70, 'ブラッシング前', 20, '#6b6e66', 700, 'middle'); d.text(GX + 650, GY - 78, 'ブラッシング後', 20, GREEN, 700, 'middle')
    section_label(d); out(f'{slug}-07', d, '人工芝DIYの手順7：ブラシで芝を起こして仕上げる')


# ======================= 人工芝の下地づくり（ページ turf-install） =======================
def turf_install(slug):
    d = base(1, '除草・根の除去', '根が残ると、防草シートを押し上げることがあります')
    d.soil(GX, GY, GW, GH, rough=True); d.weeds(GX + 40, GY, 8, 760)
    d.label(GX + 300, GY + 20, '根まで取り除く', GX + 360, GY - 110); section_label(d)
    out(f'{slug}-01', d, '人工芝の下地づくり1：雑草を根から取り除く')
    d = base(2, 'すき取り・整地', '仕上がりの高さを決め、余分な土を取って平らにします')
    d.soil(GX, GY, GW, GH); d.rect(GX, GY - 34, GW, 34, fill='none', stroke=SOIL_D, sw=2, dash='6 6')
    d.text(GX + 20, GY - 44, '取り除く土', 19, SOIL_D, 700)
    d.line(GX, GY, GX + GW, GY + 14, stroke=WATER_D, sw=2, dash='10 6')
    d.text(GX + GW - 10, GY + 44, '建物側から外側へ、わずかな勾配', 18, WATER_D, 700, 'end')
    d.shovel(GX + 640, GY - 30, .9, -25); section_label(d)
    out(f'{slug}-02', d, '人工芝の下地づくり2：仕上がりの高さに合わせて土をすき取り、整地する')
    d = base(3, '転圧（締め固め）', 'タンパーやプレートコンパクターで地面を締め固めます')
    d.soil(GX, GY, GW, GH); d.compact_marks(GX, GY, GW); d.tamper(GX + 420, GY, 1.0)
    d.label(GX + 150, GY + 10, 'やわらかいままだと、歩いた跡が沈む', GX + 40, GY - 150); section_label(d)
    out(f'{slug}-03', d, '人工芝の下地づくり3：タンパーで地面を締め固める')
    d = base(4, '防草シートを敷く', '継ぎ目は重ねて固定し、端までしっかり覆います')
    d.soil(GX, GY, GW, GH); d.sheet(GX, GY, 470, 8); d.rect(GX + 380, GY - 16, 460, 8, fill='#55594f', stroke='none')
    for x in (GX + 60, GX + 220, GX + 425, GX + 620, GX + 800): d.pin(x, GY - 8, 44)
    d.dim_h(GX + 380, GX + 470, GY - 60, '継ぎ目は十分に重ねる'); section_label(d)
    out(f'{slug}-04', d, '人工芝の下地づくり4：防草シートを継ぎ目を重ねて敷き、ピンで固定する')
    d = base(5, '人工芝の敷設・固定', '芝目をそろえて敷き、ジョイントテープとU字ピンで固定します')
    d.soil(GX, GY, GW, GH); d.compact_marks(GX, GY, GW); d.sheet(GX, GY, GW, 8)
    d.turf(GX, GY - 8, GW)
    for x in (GX + 40, GX + 420, GX + 800): d.pin(x, GY - 16, 50)
    for i, (t, y) in enumerate((('人工芝', GY - 30), ('防草シート', GY - 4), ('転圧した地面', GY + 60))):
        d.label(GX + 260 + i * 230, y, t, GX + 230 + i * 250, GY - 150, anchor='middle')
    section_label(d)
    out(f'{slug}-05', d, '人工芝の下地づくり5：人工芝を敷いて固定した完成断面（人工芝・防草シート・転圧した地面）')


if __name__ == '__main__':
    import sys, os, json
    sheet_steps('bousou-sheet-shikikata-tejun'); turf_diy('jinkoshiba-diy-shikikata'); turf_install('turf-install')
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); alts = {}
    for k, (d, a) in OUT.items(): save(d, f'{od}/{k}.svg'); alts[k + '.png'] = a
    json.dump(alts, open(f'{od}/_alt.json', 'w'), ensure_ascii=False, indent=1); print(len(OUT))
