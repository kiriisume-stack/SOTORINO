"""レンダリング済みイラスト（PNG）と流用写真を images/08_body/ に配置し、alt.json を作る。
usage: python3 install.py <rendered_root>   （<root>/<module>/png/*.png と _alt.json）"""
import sys, os, glob, json, shutil, re
KIT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BODY = os.path.join(KIT, 'images', '08_body'); PH = os.path.join(KIT, 'images', '01_photos')
root = sys.argv[1]
# イラスト（.png）だけ作り直す。お客様から届いた写真（.jpg）はそのまま残す
old = json.load(open(os.path.join(BODY, 'alt.json'))) if os.path.exists(os.path.join(BODY, 'alt.json')) else {}
for f in glob.glob(BODY + '/*.png'): os.remove(f)
alts = {k: v for k, v in old.items() if not k.endswith('.png') and os.path.exists(os.path.join(BODY, k))}
for mod in sorted(glob.glob(root + '/*/png')):
    m = os.path.dirname(mod)
    a = json.load(open(m + '/svg/_alt.json')) if os.path.exists(m + '/svg/_alt.json') else {}
    for f in glob.glob(mod + '/*.png'):
        shutil.copy(f, BODY); alts[os.path.basename(f)] = a.get(os.path.basename(f), '')
# 既存の写真（サイトで使用中の素材）を流用する枠
REUSE = {
 'gaikou-design-shurui-01': ('scenes/photo-house-dusk.jpg', 'モダンスタイルの外構の例。直線的なデザインとモノトーンの色使い'),
 'gaikou-design-shurui-02': ('scenes/photo-front-green.jpg', 'ナチュラルスタイルの外構の例。木材と植栽を取り入れた柔らかい印象'),
 'oshare-niwa-idea-20-01': ('scenes/photo-stone-dusk.jpg', '石材と植栽を組み合わせた外構の例'),
 'oshare-niwa-idea-20-02': ('products/photo-prod-stepstone.jpg', '砂利と飛び石を組み合わせたアプローチの例'),
 'oshare-niwa-idea-20-06': ('scenes/photo-front-trees.jpg', '建物の前に樹木を配置した外構の例'),
 'oshare-niwa-idea-20-11': ('products/photo-prod-planter.jpg', 'プランターで植栽を取り入れた例'),
 'oshare-niwa-idea-20-16': ('products/photo-light.jpg', 'アプローチ沿いのガーデンライトの例'),
 'oshare-niwa-idea-20-17': ('products/photo-prod-bench.jpg', '庭に置いたガーデンベンチの例'),
 'diy-niwa-reform-idea-05': ('products/photo-light.jpg', 'ガーデンライトで夜の雰囲気を変えた例'),
 'diy-niwa-reform-idea-07': ('products/photo-prod-planter.jpg', '鉢植え・プランターで季節の植物を取り入れた例'),
 'gaikou-reform-hiyou-souba-01': ('scenes/photo-house-dusk.jpg', '駐車場まわりの外構のイメージ'),
 'gaikou-reform-hiyou-souba-02': ('scenes/photo-fence.jpg', '目隠しフェンスの外構のイメージ'),
 'gaikou-reform-hiyou-souba-03': ('scenes/photo-lawn-deck.jpg', '芝生とデッキのある庭のイメージ'),
 'gaikou-reform-hiyou-souba-04': ('scenes/photo-case-entrance.jpg', '植栽と石材を使ったアプローチのイメージ'),
 'garden-guide-01': ('scenes/photo-garden-dusk.jpg', 'デッキと芝生でくつろげる庭の例'),
 'garden-guide-02': ('products/photo-prod-stepstone.jpg', '飛び石で動線をつくったアプローチの例'),
 'garden-guide-03': ('scenes/photo-case-entrance.jpg', '植栽を取り入れたエントランスの例'),
 'garden-guide-04': ('products/photo-light.jpg', 'ガーデンライトで照らした夜の庭の例'),
 'deck-ideas-01': ('scenes/photo-sea-deck.jpg', '眺めを楽しむウッドデッキの例'),
 'deck-ideas-02': ('scenes/photo-lawn-deck.jpg', '芝生の庭とつながるウッドデッキの例'),
 'deck-ideas-03': ('scenes/photo-garden-dusk.jpg', '照明を仕込んで夜も使えるウッドデッキの例'),
}
for stem, (src, alt) in REUSE.items():
    shutil.copy(os.path.join(PH, src), os.path.join(BODY, stem + '.jpg')); alts[stem + '.jpg'] = alt
json.dump(alts, open(os.path.join(BODY, 'alt.json'), 'w'), ensure_ascii=False, indent=1)
print(len(alts), 'files installed')
