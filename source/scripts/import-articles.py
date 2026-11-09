"""記事JSON（カテゴリ単位の入稿ファイル）を content/columns.json に取り込む。

使い方:
  python3 scripts/import-articles.py 入稿ファイル1.json [入稿ファイル2.json ...]

入稿ファイルの形式（これまでの category*.json と同じ）:
  { "category": "住宅設備",
    "articles": [ { "id": 101, "slug": "ecocute-jumyou", "seoTitle": "...", "metaDescription": "...",
                    "excerpt": "...", "mainKeyword": "...", "relatedKeywords": [...],
                    "internalLinkCandidates": ["slug", ...], "body": "<h2>…</h2><p>…</p>…",
                    "faq": [{"question": "...", "answer": "..."}], "sources": ["..."],
                    "imageSlots": [ {"after": "基礎知識", "label": "図解：…", "n": 1, "kind": "diagram", "ratio": "16:9"} ] } ] }
  - imageSlots は任意。after に書いたH2見出しの直後（最初の段落の後）に画像枠を入れる。
    kind = photo / gallery / steps / beforeafter / diagram
  - 同じ id の記事がすでにあれば上書き、なければ追加。
  - カテゴリ名 → キーの対応は CAT（下）に追加する。新カテゴリは src/bundle.column.js の S.colCats にも追加すること。
"""
import json, re, sys, os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, 'content', 'columns.json')
CAT = {'外構の基礎知識': 'basics', '庭・ガーデニング': 'garden', 'DIY・自分でできる施工': 'diy', '商品・素材・設備': 'products',
       '費用・相場': 'cost', 'トラブル・メンテナンス': 'trouble', '住宅設備': 'equipment', 'リフォーム': 'reform',
       '不動産・土地': 'realestate', 'お金・補助金': 'money', 'くらしの知識': 'lifestyle'}
FEATURED = set()          # 「よく読まれている」に出したい記事IDをここに
cols = json.load(open(DB))
byid = {a['id']: a for a in cols}
new = []
for f in sys.argv[1:]:
    d = json.load(open(f))
    for a in d['articles']: a['category'] = d['category']; new.append(a)
slugs = {a['slug'] for a in cols} | {a['slug'] for a in new}
titles = {a['slug']: a.get('seoTitle') or a['title'] for a in cols + new}
def find_slug(name):
    for s, t in titles.items():
        if t.startswith(name) or name in t: return s
def slot(label, ratio='3:2', n=1, kind='photo'):
    return f'<figure class="st-slot" data-kind="{kind}" data-n="{n}" data-ratio="{ratio}"><figcaption>{label}</figcaption></figure>'
today = datetime.date.today().strftime('%Y.%m.%d')
for a in new:
    key = CAT[a['category']]
    a['title'] = a.pop('seoTitle', a.get('title')); a['cat'] = key; a['catName'] = a['category']
    a['date'] = byid.get(a['id'], {}).get('date', today)
    a['featured'] = a['id'] in FEATURED or byid.get(a['id'], {}).get('featured', False)
    a['tags'] = [a['mainKeyword']] + a.get('relatedKeywords', [])[:3]
    a['links'] = [s for s in a.get('internalLinkCandidates', []) if s in slugs]
    b = a['body']
    m = re.search(r'<h2>よくある質問</h2>((?:<p><strong>Q\..*?</p>)+)', b)
    if m:
        items = ''.join(f'<details><summary><span class="st-faq__q" aria-hidden="true">Q</span><span>{q}</span>__CHEV__</summary><div class="st-faq__body"><span class="st-faq__a" aria-hidden="true">A</span><p>{x}</p></div></details>'
                        for q, x in re.findall(r'<p><strong>Q\.\s*(.*?)</strong><br>A\.\s*(.*?)</p>', m.group(1)))
        b = b[:m.start()] + '<h2>よくある質問</h2><div class="st-faq">' + items + '</div><!--/faq-->' + b[m.end():]
    def lk(mm):
        s = find_slug(mm.group(2))
        return f'{mm.group(1)}<a href="{{{{col:{s}}}}}">「{mm.group(2)}」</a>' if s else mm.group(0)
    b = re.sub(r'(関連記事|別記事)「(.*?)」', lk, b)
    a['slots'] = []
    for s in a.pop('imageSlots', []):
        mm = re.search(r'<h2>' + re.escape(s['after']) + r'[^<]*</h2>(<p>.*?</p>)?', b)
        if not mm: print('  見出しが見つかりません:', a['id'], s['after']); continue
        b = b[:mm.end()] + slot(s['label'], s.get('ratio', '3:2'), s.get('n', 1), s.get('kind', 'photo')) + b[mm.end():]
        a['slots'].append(s['label'] + (f"×{s['n']}" if s.get('n', 1) > 1 else ''))
    a['body'] = b
    a.pop('category', None)
    byid[a['id']] = a
out = sorted(byid.values(), key=lambda x: x['id'])
json.dump(out, open(DB, 'w'), ensure_ascii=False)
print(f'{len(new)}本を取り込み → 合計 {len(out)}本。次に npm run build（サムネは npm run thumbs）')
