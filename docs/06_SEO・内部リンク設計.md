# 06 SEO・内部リンク設計

SEOと内部リンクはこのサイトの最優先事項です。記事を増やすほど、記事同士が網の目のようにつながる構造にしています。

## 1. ページごとのメタ情報

| ページ | title | description | canonical | 構造化データ |
|---|---|---|---|---|
| コラム記事 | `{記事title}｜SOTORINO` | 記事の `metaDescription` | `/column/{slug}/` | Article ＋ BreadcrumbList ＋（FAQがあれば）FAQPage |
| コラム一覧 | `家まわりのコラム｜SOTORINO`（2ページ目以降は `コラム一覧（nページ目）｜SOTORINO`） | 固定文 | 各ページ自身 | BreadcrumbList。rel=prev/next |
| コラムカテゴリ | `{カテゴリ正式名}のコラム一覧｜SOTORINO` | カテゴリ説明の先頭110字 | 自身 | BreadcrumbList |
| サイトカテゴリ | `{カテゴリ名}の記事一覧｜SOTORINO` | カテゴリ紹介文 | 自身 | BreadcrumbList |
| トップ | `SOTORINO（ソトリノ）｜庭・外構・住まい・土地の情報メディア` | サイト紹介文 | / | WebSite ＋ Organization |
| 人工芝・特集記事・質問箱・連載・キャンペーン | 各ページ名＋`｜SOTORINO` | 固定文 | 自身 | BreadcrumbList |

すべてのページに付けるもの：`<html lang="ja">`、viewport、`og:type`（記事は article、それ以外は website）、`og:title`、`og:description`、`og:url`。記事には `og:image`（サムネイル）と `twitter:card=summary_large_image` も付けます。

### 記事の Article 構造化データ（実際の出力例）

```json
{
  "@context": "https://schema.org", "@type": "Article",
  "headline": "エコキュートの寿命は何年？交換時期のサインと費用の目安を解説",
  "description": "（metaDescription）",
  "datePublished": "2026-10-31", "dateModified": "2026-10-31",
  "image": ["https://sotorino.jp/img/col/ecocute-jumyou.jpg"],
  "author": {"@type": "Organization", "name": "SOTORINO編集部", "url": "https://sotorino.jp/about/"},
  "publisher": {"@type": "Organization", "name": "SOTORINO",
                "logo": {"@type": "ImageObject", "url": "https://sotorino.jp/img/logo.png"}},
  "mainEntityOfPage": "https://sotorino.jp/column/ecocute-jumyou/",
  "articleSection": "住宅設備（給湯・水まわり・省エネ）"
}
```

- BreadcrumbList：HOME → コラム → 記事名（最後の項目は `item` なし）
- FAQPage：記事データの `faq`（question/answer）から作る。画面のFAQと同じ内容にする
- JSON-LD の中の `<` は `<` に置き換えて出力（scriptタグ破損の防止）

### 公開前に直すこと
- `author.url` の `/about/`、`publisher.logo` の `/img/logo.png` は実在するURLにする（11 参照）。
- 監修者を立てる記事は、author に Person（氏名・資格）を追加する。

## 2. サイトマップと robots.txt

`dist/sitemap.xml`（196URL）

| 種類 | priority | lastmod |
|---|---|---|
| おすすめ記事（featured） | 0.9 | 記事の date |
| 通常の記事 | 0.6 | 記事の date |
| コラムカテゴリ・サイトカテゴリ | 0.8 | なし |
| コラム一覧 | 0.7 | なし |
| トップ 1.0／特集記事 0.9／人工芝 0.8／質問箱・連載・キャンペーン 0.4〜0.6 | — | なし |

`dist/robots.txt`：全許可＋サイトマップの場所。ページを静的書き出しに加えると、サイトマップにも自動で入ります（`urls` 配列に追加される）。

## 3. 画像と表示速度

- 最初の画面に見える画像（記事のアイキャッチ、一覧の先頭カード）は `fetchpriority="high"`、それ以外は `loading="lazy"`。
- 画像には内容を説明する alt。カードのサムネイルのように隣にタイトルがあるものは空の alt。
- 本文の文字はすべてHTMLに入っている（JSを切っても読める）。
- ページ固有のJSはなく、共通の `sotorino.js`（約140KB、gzip後は約49KB）を `defer` で読み込むだけ（静的ページでは記事データ `columns.js` は読み込まない）。

## 4. 内部リンクの設計

### 4-1. 階層（ピラー＆クラスター）

```
トップ
 ├─ サイトカテゴリ（9）……… 上部メニュー。テーマ横断のハブ
 │    └─ コラムを自動で集約（02 の 4-2）
 ├─ コラム一覧 → コラムカテゴリ（11）……… ピラーページ
 │                 └─ コラム記事（150）……… クラスター
 └─ 特集型カテゴリ（人工芝）→ ピラーガイド9章 → 個別記事
```

どの記事からも、パンくず・カテゴリラベル・サイドバーの同カテゴリ一覧・「次のステップ」の4つの経路で上の階層に戻れます。

### 4-2. 記事1本から出ていくリンク

| 場所 | 本数 | 決め方 |
|---|---|---|
| 本文中のテキストリンク | 入稿データ次第（150本中10か所） | 本文の「関連記事『〇〇』」「別記事『〇〇』」をタイトルで照合してリンク化 |
| あわせて読みたい（本文中） | 1 | 関連記事 same の1本目。注意系の見出しの前、なければまとめの前 |
| 次のステップ | 3 | 同カテゴリ一覧／カテゴリ別の次の一手（04参照）／施工会社の選び方 |
| 関連記事（記事末） | 3 | same の上位3本 |
| ほかのカテゴリの関連記事 | 最大4 | cross |
| サイドバー：同カテゴリの記事 | 最大15 | 同カテゴリを記事ID順 |
| サイドバー：編集部のおすすめ | 4 | featured |
| タグ | 0〜4 | 101〜150は mainKeyword＋関連キーワード3つ。1〜100は入稿時のタグ（0〜4個） |
| パンくず・カテゴリラベル | 3 | — |

### 4-3. 関連記事の決め方（colRelated）

```
入力：記事 a

linked  = a.links（入稿データの内部リンク候補のうち、実在するスラッグ）
same    = 同じコラムカテゴリの他の記事を、
          (1) a とのタグの重なりが多い順 → (2) 記事IDが近い順 に並べる
cross   = 別カテゴリの記事のうち、a とタグが1つ以上重なるものを、重なりが多い順に並べる

結果.same  = [linked のうち同カテゴリ] + same     の重複を除いた先頭4本
結果.cross = [linked のうち別カテゴリ] + cross    の重複を除いた先頭4本
```

入稿データで指定した内部リンク候補（`internalLinkCandidates`）が必ず最優先で出ます。指定がない記事でも、同じカテゴリから3〜4本、タグが重なる他カテゴリの記事が自動で入ります（要件R5）。

### 4-4. サイトカテゴリへの載せ方
02 の 4-2 のとおり、コラムカテゴリとタイトルのキーワードで判定します。1本の記事が複数のハブに載るため、テーマ横断のリンクが自然に増えます（例：「外構リフォームの費用相場」は リフォーム／お金・補助金／外構 の3つに載る）。

### 4-5. ページ送り
一覧は `<a href="/column/page/2/">` の本物のリンク（要件R7）。前後ページには `rel="prev"`／`rel="next"`。全ページ番号を並べるので、どの一覧ページからも全ページに1クリックで行けます。

## 5. コンテンツ面のルール

- 1記事1テーマ。同じ内容の記事を量産しない。似たテーマはどちらかに統合して301リダイレクト。
- 公開日と更新日を分けて持つ。更新日は内容を見直したときだけ変える。
- 補助金・制度の記事（131〜135など）は年度で内容が変わるので、年1回見直して `dateModified` を更新する。
- 広告・アフィリエイトのリンクは `rel="sponsored"`、枠には「PR」表記。広告契約でランキングや評価を変えない。
