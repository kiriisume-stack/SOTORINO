# 02 情報設計（サイトマップ・URL・ルーティング）

## 1. サイトマップ

```
/                                   トップ
├─ /column/                         コラム一覧（12件／ページ）
│   ├─ /column/page/{n}/            コラム一覧 n ページ目（2〜13）
│   ├─ /column/category/{key}/      コラムカテゴリ（ピラー）×11
│   ├─ /column/{slug}/              コラム記事 ×150
│   └─ /column/shiba/               連載「人工芝職人が語る現場の本音」（シリーズページ）
├─ /garden/                         サイトカテゴリ：庭づくり
│   └─ /garden/turf/                人工芝カテゴリ（特集型カテゴリページ）
├─ /exterior/                       サイトカテゴリ：外構・エクステリア
│   ├─ /exterior/carport/           サイトカテゴリ：駐車場・カーポート
│   ├─ /exterior/deck/              サイトカテゴリ：ウッドデッキ
│   ├─ /exterior/fence/fence-guide/ 特集記事「失敗しないフェンスの選び方」
│   └─ /exterior/trap/              連載「外構の落とし穴」（シリーズページ）
├─ /equipment/                      サイトカテゴリ：住宅設備
├─ /reform/                         サイトカテゴリ：リフォーム
├─ /realestate/                     サイトカテゴリ：不動産・土地
├─ /money/                          サイトカテゴリ：お金・補助金
├─ /life/                           サイトカテゴリ：暮らしの知識
├─ /qa/  /qa/{cat}/                 読者の質問箱（6カテゴリ）
├─ /campaign/autumn-2026/           キャンペーンページ
├─ /purpose/{cost,examples,products,contractors,subsidy}/  目的別まとめ
├─ /exterior/fence/ /exterior/beginners/ /money/subsidy/   ガイド
├─ /garden/turf/{basics,quality,install,use,care,contractors,winter,hot}/  人工芝ガイドの章
├─ /new/ /search/ /tag/{タグ}/ /glossary/ /cases/ /video/ /feature/ /campaign/
├─ /contractors/estimate/ /contractors/area/ /contractors/criteria/ /contact/ /catalog/  フォーム・送客
└─ /about/ /about/editors/ /about/supervisors/ /editorial-policy/ /privacy/ /ads-policy/ /disclaimer/  運営情報
```

## 2. ページの種類と実装状況

| テンプレート | URL | 関数 | 静的書き出し | 画面キャプチャ |
|---|---|---|---|---|
| トップ | `/` | `S.TopPage()` | 済 | 01_top |
| コラム一覧 | `/column/`, `/column/page/{n}/` | `S.ColumnListPage(n)` | 済 | 02_column-list |
| コラムカテゴリ | `/column/category/{key}/` | `S.ColumnCategoryPage(key)` | 済 | 03_column-category |
| コラム記事 | `/column/{slug}/` | `S.ColumnArticlePage(slug)` | 済 | 04_column-article |
| サイトカテゴリ（ハブ） | `/garden/` など9件 | `S.SiteCategoryPage(cat)` | 済 | 05_site-category-hub |
| 特集型カテゴリ | `/garden/turf/` | `S.CategoryPage()` | 済 | 06_turf-category |
| 特集記事（ブロック形式） | `/exterior/fence/fence-guide/` | `S.ArticlePage()` | 済 | 07_feature-article |
| 質問箱 | `/qa/`, `/qa/{cat}/` | `S.QAPage(cat)` | 済 | 08_qa |
| 連載シリーズ | `/exterior/trap/`, `/column/shiba/` | `S.SeriesPage('trap'｜'column')` | 済 | 09_series-trap |
| キャンペーン | `/campaign/autumn-2026/` | `S.CampaignPage()` | 済 | 10_campaign |

すべてのテンプレートが `scripts/ssg.cjs` で静的HTMLになります（合計196ページ）。

2026年11月3日に、リンク先として必要だったページ（ガイド記事・目的別まとめ・運営情報・フォーム・用語集・タグ・新着・検索・404）をすべて追加しました。全539ページ、サイト内のリンク切れは0件です（12章）。

## 3. URLのルール

- すべて小文字の英数字とハイフン。末尾は必ず `/`（ディレクトリ＋`index.html` で配信）。
- コラム記事は **入稿データの `slug` をそのまま** 使う（例：`/column/ecocute-jumyou/`）。公開後は変更しない。変える必要があるときは旧URLから301リダイレクトを設定する。
- コラムカテゴリのキーは英語の短い語（`basics` `garden` `diy` `products` `cost` `trouble` `equipment` `reform` `realestate` `money` `lifestyle`）。
- ページ送りは `/column/page/2/`。1ページ目は `/column/`（`/column/page/1/` は作らない）。
- パンくず：HOME ＞ コラム ＞ 記事名。カテゴリページは HOME ＞ コラム ＞ カテゴリ名。

## 4. カテゴリ体系（2層）

カテゴリは役割の違う2種類があります。

### 4-1. コラムカテゴリ（記事の所属先。1記事に1つ）

| キー | 表示名 | 正式名（ページ見出し） | 本数 | 記事ID |
|---|---|---|---|---|
| basics | 外構の基礎知識 | 外構・エクステリアの基礎知識 | 15 | 1〜15 |
| garden | 庭・ガーデニング | 庭・ガーデニング | 15 | 16〜30 |
| diy | DIY・自分でできる施工 | DIY・自分でできる施工 | 20 | 31〜50 |
| products | 商品・素材・設備 | 外構商品・素材・設備 | 20 | 51〜70 |
| cost | 費用・相場 | 費用・相場・リフォーム | 15 | 71〜85 |
| trouble | トラブル・メンテナンス | トラブル・メンテナンス | 15 | 86〜100 |
| equipment | 住宅設備 | 住宅設備（給湯・水まわり・省エネ） | 10 | 101〜110 |
| reform | リフォーム | リフォーム（内装・外装・外構） | 10 | 111〜120 |
| realestate | 不動産・土地 | 不動産・土地選び | 10 | 121〜130 |
| money | お金・補助金 | お金・補助金・税金 | 10 | 131〜140 |
| lifestyle | くらしの知識 | くらしの知識（季節・メンテナンス） | 10 | 141〜150 |

### 4-2. サイトカテゴリ（上部メニュー。1記事が複数に載る）

上部メニューのカテゴリを開くと、関連するコラムが自動で集まります。どのコラムを載せるかは次の2つの条件のどちらかで決まります（`S.siteCatRules`、データは `data/site-category-rules.json`）。

1. 記事のコラムカテゴリが「対応コラムカテゴリ」に含まれる
2. 記事タイトルが「キーワード」の正規表現に一致する

| ID | URL | 表示名 | 対応コラムカテゴリ | 掲載数 |
|---|---|---|---|---|
| garden | /garden/ | 庭づくり | garden | 58 |
| exterior | /exterior/ | 外構・エクステリア | basics | 42 |
| carport | /exterior/carport/ | 駐車場・カーポート | （キーワードのみ） | 9 |
| deck | /exterior/deck/ | ウッドデッキ | （キーワードのみ） | 6 |
| equipment | /equipment/ | 住宅設備 | equipment | 23 |
| reform | /reform/ | リフォーム | reform | 26 |
| realestate | /realestate/ | 不動産・土地 | realestate | 13 |
| money | /money/ | お金・補助金 | cost, money | 29 |
| life | /life/ | 暮らしの知識 | diy, trouble, lifestyle | 50 |

150本すべてが、少なくとも1つのサイトカテゴリに載っています。記事を追加したら `node -e` の確認スクリプト（10 参照）で「どこにも載らない記事」がないか確認してください。

並び順は「対応コラムカテゴリに属し、かつキーワードにも一致」→「どちらか一方」の順です。同じ順位の中では、おすすめ記事（featured）を先にし、その後は記事IDの小さい順に並べます。

### 4-3. グローバルナビ（上部メニューの並び）

新着記事 ／ コラム ／ 庭づくり ／ 外構・エクステリア ／ 住宅設備 ／ リフォーム ／ 不動産・土地 ／ お金・補助金 ／ 暮らしの知識

スマホでは横スクロールのメニューと、右上のハンバーガーで開くドロワーの両方で表示します。

### 4-4. 目的別の入口（PurposeNav）

| 目的 | URL（未制作） |
|---|---|
| 費用相場を知りたい | /purpose/cost/ |
| デザインの実例を見たい | /purpose/examples/ |
| おすすめ商品を探したい | /purpose/products/ |
| 業者を探したい | /purpose/contractors/ |
| 補助金を調べたい | /purpose/subsidy/ |

## 5. ルーティング

### 公開版（dist/）
ページごとに `/{path}/index.html` が置かれた普通の静的サイトです。サーバー側の設定は不要です。

### プレビュー版（public/index.html）
1枚のHTMLの中で、`#/column/ecocute-jumyou/` のようなハッシュでページを切り替えます。`S.config.base = '#'` のときは、部品が出力するリンクがすべて `#/...` になります。公開版では `S.config.base = ''` にして通常のパスに戻します（`ssg.cjs` で設定済み）。

ルーティングの判定順（`public/index.html` の `render()`）：

1. `/` → TopPage
2. 特集記事・人工芝カテゴリ・キャンペーン・質問箱・連載
3. `/column/` → 一覧、`/column/page/{n}/` → 一覧n、`/column/category/{key}/` → カテゴリ、`/column/{slug}/` → 記事
4. `S.data.articles` に同じパスがあれば準備中ページ（タイトルと関連記事）
5. サイトカテゴリのパス → SiteCategoryPage
6. それ以外 → 「このページは準備中です」
