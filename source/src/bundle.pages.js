/* ================= content pages, hubs, forms, tags, glossary, routing ================= */
(function () {
  'use strict';
  var S = window.Sotorino, esc = S.esc, href = S.href, icon = S.icon, img = S.img, media = S.media;
  /* フォームの送信先。すべてのフォーム（お問い合わせ・見積もり依頼・カタログ請求・キャンペーン応募・サンプル申込み）が FormSubmit 経由で同じメールに届く。件名はフォームごとに pages.json の form.subject で分けている。
     FormSubmit の初回送信時に、送信先アドレスへ「有効化」のメールが届くので、リンクを押して有効化すること。
     有効化後に届くランダムな文字列（例：https://formsubmit.co/ajax/abc123...）に差し替えると、HTML上にメールアドレスが出なくなる。 */
  S.config.formEndpoints = S.config.formEndpoints || {};   // フォーム名ごとに送信先を分けたいときだけ使う（例：{ estimate: 'https://...' }）
  S.config.formEndpoint = S.config.formEndpoint || 'https://formsubmit.co/ajax/takaokashinnosuke01@gmail.com';   // 例：'https://formspree.io/f/xxxx'。空ならNetlify Forms互換のマークアップのみ
  S.config.siteOrigin = S.config.siteOrigin || 'https://sotorino.jp';
  S.colCats.forEach(function (c) { S.data.catName['col-' + c.key] = c.name; });

  /* ---------- data access ---------- */
  S.pgAll = function () { return window.SOTORINO_PAGES || []; };
  S.pgByPath = function (p) { var l = S.pgAll(); for (var i = 0; i < l.length; i++) if (l[i].path === p) return l[i]; return null; };
  S.pgCard = function (p) { return { id: p.path, cat: p.cat || 'life', title: p.title, desc: p.excerpt || p.description, img: p.img || ('page-' + p.key), date: p.date, path: p.path }; };
  var CATIMG = { garden: 'photo-lawn-deck', turf: 'photo-garden-dusk', exterior: 'photo-front-trees', carport: 'photo-carport', deck: 'photo-sea-deck', equipment: 'photo-interior-city', reform: 'photo-reform-living', realestate: 'photo-hiraya-dusk', money: 'photo-wood-balcony', life: 'photo-front-green' };
  /* ページ画像：images/07_pages/{key}.jpg があればそれ、なければカテゴリの写真（build.mjs が imgFile を決める） */
  S.pgRegister = function (base) {
    base = base == null ? 'img/' : base;
    var ex = window.SOTORINO_PAGE_EXTRA || {}; if (ex.flyer) S.images['campaign-flyer'] = base + ex.flyer;
    /* 専用画像が無いページは、カテゴリごとの写真の中からページごとに散らして使う（同じ写真が並ばないように） */
    var POOL = { turf: ['photo-turf-wide', 'photo-turf-dog', 'photo-turf-family', 'photo-turf-approach', 'photo-garden-dusk', 'photo-lawn-deck', 'body/niwa-zassou-taisaku-erabikata-guide-01'],
      garden: ['photo-lawn-deck', 'photo-front-green', 'photo-courtyard-deck', 'photo-courtyard-night', 'photo-garden-dusk', 'photo-prod-planter'],
      exterior: ['photo-front-trees', 'photo-stone-dusk', 'photo-case-entrance', 'photo-house-dusk', 'photo-black-house-light', 'photo-wamodern-sea', 'photo-black-house-concrete', 'photo-fence-wood-turf', 'body/fence-shurui-hikaku-02'],
      carport: ['photo-carport', 'photo-carport-white', 'photo-carport-stone', 'photo-black-house-concrete'], deck: ['photo-sea-deck', 'photo-living-deck', 'photo-white-deck', 'photo-courtyard-deck'],
      equipment: ['photo-interior-city', 'photo-interior-night', 'photo-study-light', 'photo-courtyard-night'], realestate: ['photo-hiraya-dusk', 'photo-house-day', 'photo-white-deck', 'photo-turf-approach'],
      money: ['photo-wood-balcony', 'photo-house-dusk', 'photo-house-day', 'photo-black-house-concrete'], life: ['photo-front-green', 'photo-season-autumn', 'photo-interior-city', 'photo-living-pendant', 'photo-cabin-stove'],
      reform: ['photo-reform-living', 'photo-interior-living', 'photo-wood-ceiling', 'photo-living-pendant', 'photo-cabin-stove', 'photo-study-light'] };
    /* カテゴリ内でページ順に1枚ずつずらして割り当てる（ハッシュだと隣どうしが同じ写真になりやすいため） */
    var seq = {};
    function pick(p) { var l = POOL[p.cat]; if (!l) return CATIMG[p.cat] || 'photo-house-day'; var n = seq[p.cat] = (seq[p.cat] || 0) + 1; return l[(n - 1) % l.length]; }
    S.pgAll().forEach(function (p) { if (p.key) S.images['page-' + p.key] = base + (p.imgFile || ((p.imgFallback || pick(p)) + '.jpg')); });
  };
  function pgImgAbs(p) { var v = S.images['page-' + p.key] || ''; return S.config.siteOrigin + '/' + v.replace(/^\//, ''); }
  /* ref: column slug / page path / column path / data.articles id → card object */
  S.ref = function (r) {
    if (!r) return null;
    if (typeof r === 'object') return r;
    if (r.charAt(0) === '/') {
      var p = S.pgByPath(r); if (p) return S.pgCard(p);
      var m = /^\/column\/([a-z0-9-]+)\/$/.exec(r); if (m && S.colBySlug(m[1])) return S.colCard(S.colBySlug(m[1]));
      var d = S.data.articles.filter(function (x) { return x.path === r; })[0]; return d || null;
    }
    var c = S.colBySlug(r); if (c) return S.colCard(c);
    return S.article(r);
  };
  function refs(list) { var seen = {}; return (list || []).map(S.ref).filter(function (x) { if (!x || seen[x.path]) return false; seen[x.path] = 1; return true; }); }
  S.refs = refs;
  function links(html) {
    return String(html || '')
      .replace(/\{\{col:([a-z0-9-]+)\}\}/g, function (_, s) { var t = S.colBySlug(s); return esc(href(t ? S.colPath(t) : '/column/')); })
      .replace(/\{\{p:([^}]+)\}\}/g, function (_, p) { return esc(href(p)); })
      .replace(/<a href="(\/[^"]*)"/g, function (_, p) { return '<a class="st-a" href="' + esc(href(p)) + '"'; });
  }
  S.pgLinks = links;
  function fill(html) { return html.replace(/［要記入：([^］]+)］/g, '<mark class="st-fill" title="公開前に記入してください">［要記入：$1］</mark>'); }

  /* plain body (info / hub intro): no question box, no answer box */
  function plainBody(html) {
    var n = 0, toc = [];
    var out = links(html).replace(/<h2>([\s\S]*?)<\/h2>/g, function (_, t) { var id = 'p' + (++n); toc.push({ id: id, text: t.replace(/<[^>]+>/g, '') }); return '<h2 class="st-h2" id="' + id + '">' + t + '</h2>'; })
      .replace(/<h3>/g, '<h3 class="st-h3">').replace(/<ul>/g, '<ul class="st-ul">').replace(/<ol>/g, '<ol class="st-olist">')
      .replace(/<table>([\s\S]*?)<\/table>/g, '<div class="st-table"><div class="st-table__scroll" tabindex="0" role="region" aria-label="表"><table>$1</table></div></div>')
      .replace(/__CHEV__/g, icon('chevD')).replace(/\x3c!--\/faq-->/g, '');
    out = out.replace(/<figure class="st-slot"([^>]*)><figcaption>([\s\S]*?)<\/figcaption><\/figure>/g, function (_, a, c) { return S.slotHTML(a, c); });
    return { html: '<div class="st-body st-body--col st-body--plain">' + fill(out) + '</div>', toc: toc };
  }
  S.pgPlainBody = plainBody;

  /* ---------- series (side box) ---------- */
  function series(key) {
    if (key === 'turf') return { name: '人工芝ガイド（全9章）', path: '/garden/turf/', items: S.data.turfGuide.chapters.map(function (c) { return { name: c.name, path: c.path }; }) };
    if (key === 'trap') return { name: '外構工事の罠！？', path: '/exterior/trap/', items: S.data.traps.map(function (id) { var a = S.article(id); return { name: a.title, path: a.path }; }) };
    if (key === 'shiba') return { name: '人工芝職人が語る現場の本音', path: '/column/shiba/', items: S.data.columns.map(function (c) { var a = S.article(c.id); return { name: a.title, path: a.path }; }) };
    if (key === 'fence') return { name: 'フェンス完全ガイド', path: '/exterior/fence/', items: S.data.fenceSeries.items.filter(function (i) { return i.id; }).map(function (i) { var a = S.article(i.id); return { name: i.name, path: a.path }; }) };
    if (key === 'beginner') return { name: 'はじめての外構工事', path: '/exterior/beginners/', items: [
      { name: 'はじめての外構工事（入門ガイド）', path: '/exterior/beginners/' }, { name: '後悔しない外構工事の進め方', path: '/exterior/exterior-flow/' },
      { name: '外構工事の費用相場', path: '/column/gaikou-koji-hiyou-souba/' }, { name: '見積もりで確認すべき項目', path: '/column/gaikou-koji-mitsumori-kakunin/' },
      { name: '施工会社の選び方', path: '/purpose/contractors/' }, { name: '外構・庭づくり用語集', path: '/glossary/' }] };
    return null;
  }
  function SeriesBox(key, cur) {
    var s = series(key); if (!s) return '';
    return '<nav class="st-box st-seriesbox" aria-label="' + esc(s.name) + '"><p class="st-box__title">' + icon('layers') + '<a href="' + esc(href(s.path)) + '">' + esc(s.name) + '</a></p><ol>' +
      s.items.map(function (it, i) { var no = '<span class="st-seriesbox__no">' + ('0' + (i + 1)).slice(-2) + '</span>'; return '<li>' + (it.path === cur ? '<span aria-current="page">' + no + esc(it.name) + '</span>' : '<a href="' + esc(href(it.path)) + '">' + no + esc(it.name) + '</a>') + '</li>'; }).join('') + '</ol></nav>';
  }
  S.SeriesBox = SeriesBox;

  function crumbs(p) { return [{ name: 'ホーム', path: '/' }].concat((p.crumbs || []).map(function (c) { return { name: c[0], path: c[1] }; })).concat([{ name: p.h1 || p.title }]); }
  function RefGrid(list, opt) { opt = opt || {}; return '<ul class="st-grid' + (opt.cols === 3 ? ' st-grid--3' : '') + ' st-colgrid">' + list.map(function (a) { return '<li>' + S.ArticleCard({ article: a, desc: opt.desc }) + '</li>'; }).join('') + '</ul>'; }
  function RefList(list) { return '<ol class="st-colindex">' + list.map(function (a, i) { return '<li><a href="' + esc(href(a.path)) + '"><span class="st-colindex__no">' + ('0' + (i + 1)).slice(-2) + '</span><span class="st-colindex__title">' + esc(a.title) + '<small>' + esc(a.desc || '') + '</small></span>' + icon('chevR') + '</a></li>'; }).join('') + '</ol>'; }
  S.RefGrid = RefGrid; S.RefList = RefList;
  function Hero(p, en) {
    return '<section class="st-colhero"><div class="st-container"><p class="st-cathero__eyebrow">' + esc(p.en || en) + '</p><h1 class="st-colhero__title">' + esc(p.h1 || p.title) + '</h1>' + (p.lead !== false ? '<p class="st-colhero__text">' + esc(p.lead || p.description) + '</p>' : '') + (p.heroNav || '') + '</div></section>';
  }
  function FeatList() { return S.colAll().filter(function (x) { return x.featured; }).slice(0, 4).map(S.colCard); }

  /* ---------- 商品カード（冬の庭アウトドア） ----------
     price：確認できた参考価格のみ記載。空欄は「販売ページで確認」と表示。
     販売サイトへのボタンは S.config.affiliate が true のときだけ表示（承認前はクリックさせない） */
  S.data.goodsChecked = '2026年11月4日';
  S.data.winterGoods = [
    { cat: '焚き火台', name: 'スノーピーク 焚火台M（ST-033R）', img: 'goods-winter-01.png', point: 'ステンレス製で丈夫な定番の焚き火台。2〜3人で囲むのにちょうどよいサイズです。', spec: ['サイズ：約350×350×248mm', '重量：約3.5kg', '収納ケース付き'], price: '17,160円', priceSrc: 'スノーピーク公式 楽天市場店', note: '地面への熱を防ぐベースプレートは別売り。タイルやコンクリートの上で使いましょう。', q: 'スノーピーク 焚火台M ST-033R' },
    { cat: 'ポータブル電源', name: 'Jackery ポータブル電源 1000 New', img: 'goods-winter-02.png', point: '電気毛布や照明、スマホの充電をまとめてまかなえる大容量タイプ。災害時の備えにもなります。', spec: ['容量：1070Wh', '定格出力：1500W', '重量：約10.8kg'], price: '', priceSrc: '', note: 'セールで価格が大きく変わる商品です。購入時に最新価格を確認してください。', q: 'Jackery ポータブル電源 1000 New' },
    { cat: '電気ブランケット', name: 'アイリスオーヤマ ヒートブランケット（HW-HBK）', img: 'goods-winter-03.png', point: 'USB給電で、ポータブル電源やモバイルバッテリーから使えるひざ掛けタイプ。', spec: ['サイズ：約100×70cm', '消費電力：10W', 'USB給電'], price: '', priceSrc: '', note: '屋外で使うときは、雨や結露で濡らさないよう注意しましょう。', q: 'アイリスオーヤマ ヒートブランケット HW-HBK' },
    { cat: 'ランタン・LEDライト', name: 'ゴールゼロ ライトハウス マイクロ フラッシュ', img: 'goods-winter-04.png', point: '手のひらサイズの充電式LEDランタン。テーブルの上や吊り下げで、やわらかい灯りをつくれます。', spec: ['明るさ：最大150ルーメン', '点灯時間：約7〜170時間', '重量：約87g・USB充電'], price: '', priceSrc: '', note: '隣家の窓に強い光が向かないよう、置き場所に配慮しましょう。', q: 'ゴールゼロ ライトハウス マイクロ フラッシュ' },
    { cat: 'アウトドアチェア', name: 'ヘリノックス チェアワン（1822221）', img: 'goods-winter-05.png', point: '軽くてコンパクトにたためる人気のチェア。座ると体を包み込むように支えてくれます。', spec: ['重量：約890g', '耐荷重：約145kg', '座面高：約35cm'], price: '14,300円', priceSrc: '楽天市場の最安値', note: '冬は座面が冷えやすいので、クッションやブランケットを併用すると快適です。', q: 'ヘリノックス チェアワン 1822221' },
    { cat: '防寒ブランケット（難燃）', name: 'オレゴニアンキャンパー ファイヤープルーフ ブランケット L', img: 'goods-winter-06.png', point: '表地・裏地に難燃加工を施したブランケット。焚き火のそばで使いやすい素材です。', spec: ['サイズ：約140×200cm', '素材：ポリエステル（難燃加工）', 'ひざ掛け・肩掛けに'], price: '', priceSrc: '', note: '「難燃」は燃え広がりにくいという意味で、燃えないわけではありません。火の粉に注意しましょう。', q: 'オレゴニアンキャンパー ファイヤープルーフ ブランケット L' },
    { cat: '保温ボトル・マグ', name: 'サーモス 山専用ボトル 0.5L（FFX-501）', img: 'goods-winter-07.png', point: '登山向けに作られた保温力の高いボトル。冬の庭で温かい飲み物を長く楽しめます。', spec: ['容量：0.5L', '保温効力：77℃以上（6時間）', '重量：約0.28kg'], price: '', priceSrc: '', note: '保温効力はメーカーの測定条件での値です。', q: 'サーモス 山専用ボトル FFX-501' },
    { cat: '屋外用ヒーター', name: 'イワタニ カセットガスストーブ マル暖（CB-STV-MRD）', img: 'goods-winter-08.png', point: '屋内外兼用のカセットガスストーブ。4つの安全装置を搭載し、天板でお湯も沸かせます。', spec: ['屋内外兼用', '連続燃焼：約1時間40分（メーカー実測）', '安全装置：4種類'], price: '49,800円', priceSrc: 'メーカー希望小売価格（税込）', note: '燃焼器具を囲いやテントの中で使うと一酸化炭素中毒の危険があります。取扱説明書に従いましょう。', q: 'イワタニ マル暖 CB-STV-MRD' },
    { cat: '防寒シューズ', name: 'ザ・ノース・フェイス ヌプシ ブーティ ウォータープルーフ（NF52272）', img: 'goods-winter-09.png', point: '保温性と防水性を備えた冬用ブーツ。夜の冷えやすい足元をしっかり守ります。', spec: ['防水仕様', '保温素材', 'ユニセックス'], price: '24,970円', priceSrc: 'ANAモールでの販売価格', note: 'サイズ感は試着か、メーカーのサイズ表で確認しましょう。', q: 'ノースフェイス ヌプシ ブーティ ウォータープルーフ NF52272' },
    { cat: '収納ボックス', name: 'リス トランクカーゴ 50L（TC-50S）', img: 'goods-winter-10.png', point: 'グッズをまとめて片付けられる、ふた付きの収納ボックス。ふたの上に座ることもできます。', spec: ['容量：50L', 'サイズ：約600×390×357mm', '耐荷重：約100kg'], price: '3,980円', priceSrc: 'リス公式 楽天市場店', note: '屋外に置きっぱなしにする場合は、日差しや雨による劣化に注意しましょう。', q: 'リス トランクカーゴ TC-50S' }
  ];
  S.ProductList = function (items) {
    var aff = !!S.config.affiliate, base = S.config.bodyImgBase == null ? 'img/body/' : S.config.bodyImgBase;
    return '<section class="st-goods" aria-labelledby="goods-t"><div class="st-goods__head"><h2 id="goods-t">編集部が選んだおすすめアイテム10選</h2>' + (aff ? S.PRLabel() : '') + '</div>' +
      '<p class="st-goods__lead">10のカテゴリから、使いやすさと安全性を基準に1つずつ選びました。価格は' + esc(S.data.goodsChecked) + '時点で確認できた参考価格です。最新の価格は販売ページで確認してください。</p><ol class="st-goods__list">' +
      items.map(function (g, i) {
        var shops = aff ? '<div class="st-goods__shops"><a class="st-btn st-btn--rakuten" href="https://search.rakuten.co.jp/search/mall/' + encodeURIComponent(g.q) + '/" target="_blank" rel="sponsored nofollow noopener">楽天市場で見る</a><a class="st-btn st-btn--amazon" href="https://www.amazon.co.jp/s?k=' + encodeURIComponent(g.q) + '" target="_blank" rel="sponsored nofollow noopener">Amazonで見る</a></div>' : '<p class="st-goods__soon">' + icon('info') + '販売サイトへのリンクは準備中です</p>';
        return '<li class="st-goods__item"><div class="st-goods__fig"><img src="' + esc(base + g.img) + '" alt="' + esc(g.cat + 'のイメージイラスト') + '" loading="lazy" decoding="async" width="400" height="400"><span class="st-goods__no">' + ('0' + (i + 1)).slice(-2) + '</span></div><div class="st-goods__body">' +
          '<p class="st-goods__cat">' + esc(g.cat) + '</p><h3 class="st-goods__name">' + esc(g.name) + '</h3><p class="st-goods__point">' + esc(g.point) + '</p><ul class="st-goods__spec">' + g.spec.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ul>' +
          '<p class="st-goods__price">' + (g.price ? '<span class="st-goods__yen">' + esc(g.price) + '</span><small>参考価格（税込）／' + esc(g.priceSrc) + '</small>' : '<span class="st-goods__yen st-goods__yen--none">価格は販売ページで確認</span>') + '</p>' +
          (g.note ? '<p class="st-goods__note">' + icon('alert') + esc(g.note) + '</p>' : '') + shops + '</div></li>';
      }).join('') + '</ol><p class="st-goods__disc">イラストは商品のイメージで、実際の製品の形・色とは異なります。商品の仕様は販売ページ・メーカーの公式情報で確認してください。</p></section>';
  };
  /* ---------- article-type page ---------- */
  S.ContentPage = function (p) {
    var body = links(p.body), vid = p.video && (String(p.video).match(/(?:v=|youtu\.be\/|embed\/)([\w-]{11})/) || [0, p.video])[1];
    if (vid) body = body.replace('<figure class="st-slot"', '<figure class="st-slot" data-video="' + vid + '"');
    var a = { id: p.num || 500, slug: p.key, cat: p.colCat || '', tags: p.tags || [], links: (p.links || []).filter(function (l) { return S.colBySlug(l); }), body: body, title: p.title };
    var b = S.colBody(a), rel = refs(p.links), relSame = rel.slice(0, 3), relMore = rel.slice(3, 9);
    if (relSame.length < 3 && p.colCat) relSame = relSame.concat(S.colAll().filter(function (x) { return x.cat === p.colCat; }).slice(0, 3 - relSame.length).map(S.colCard));
    var card = S.pgCard(p);
    return '<div class="st">' + S.Header({ active: p.nav || p.cat }) + S.Breadcrumb({ items: crumbs(p) }) +
      '<div class="st-container"><div class="st-article-wrap"><main id="main"><article>' +
      '<header class="st-ahead"><div class="st-ahead__meta">' + S.CategoryLabel(p.cat) + S.Date({ date: p.date, updated: p.updated }) + (p.pr ? S.PRLabel() : '') + '</div>' +
      '<h1 class="st-ahead__title">' + esc(p.h1 || p.title) + '</h1><p class="st-ahead__lead">' + esc(p.excerpt) + '</p>' +
      '<p class="st-ahead__byline">' + icon('user') + '<span>執筆：<a href="' + esc(href('/about/editors/')) + '">' + esc(p.author || 'SOTORINO編集部') + '</a></span></p>' +
      (p.noHero ? '' : '<figure class="st-ahead__hero"><span class="st-media st-r-hero">' + img(card.img, p.heroAlt || p.title, { eager: true }) + '</span></figure>') + S.ShareBar({ id: 'pg-' + p.key, title: p.title, path: p.path }) + '</header>' +
      (b.toc.length > 2 ? '<div class="st-intro st-intro--col">' + S.TableOfContents({ items: b.toc }) + '</div>' : '') + fill(b.html).replace(/<p[^>]*>\[\[products:winter\]\]<\/p>/, function () { return S.ProductList(S.data.winterGoods); }) +
      (p.tags && p.tags.length ? '<div class="st-block">' + S.TagList({ tags: p.tags }) + '</div>' : '') +
      (p.next ? '<div class="st-block">' + S.NextSteps({ items: p.next }) + '</div>' : '') +
      (p.sources && p.sources.length ? '<aside class="st-block st-sources" aria-label="参考情報・確認事項"><p class="st-sources__title">' + icon('info') + '参考情報・確認事項</p><ul>' + p.sources.map(function (x) { return '<li>' + links(esc(x)) + '</li>'; }).join('') + '</ul></aside>' : '') +
      '<div class="st-block">' + S.AuthorBox({ name: p.author || 'SOTORINO編集部', role: '執筆', initial: 'S', bio: '外構・庭づくり・住まいに関する情報を、根拠と条件を添えてわかりやすくお届けしています。' }) + '</div>' +
      '</article>' +
      (relSame.length ? '<section class="st-block" aria-labelledby="prel-t"><div class="st-endhead"><h2 id="prel-t">関連記事</h2></div>' + RefGrid(relSame, { cols: 3 }) + '</section>' : '') +
      (relMore.length ? '<section class="st-block" aria-labelledby="pmore-t"><div class="st-endhead"><h2 id="pmore-t">あわせて読みたい</h2></div><ul class="st-endlist">' + relMore.map(function (x) { return '<li><a href="' + esc(href(x.path)) + '"><span>' + esc(x.title) + '</span>' + S.CategoryLabel(x.cat) + '</a></li>'; }).join('') + '</ul></section>' : '') +
      '</main><aside class="st-side" aria-label="サイドバー">' +
      (p.series ? SeriesBox(p.series, p.path) : '') +
      S.CTABanner({ title: '理想の外構を<br>プロとつくる', text: '外構工事の無料見積もりはこちら', cta: '無料で相談する', img: 'photo-black-house-light' }) +
      '<section class="st-box" aria-labelledby="pf-t"><h2 class="st-box__title" id="pf-t">' + icon('leaf') + '編集部のおすすめ</h2><ul class="st-sidelist">' + FeatList().map(function (x) { return '<li>' + S.ArticleCard({ article: x, variant: 'mini', headingLevel: 'span' }) + '</li>'; }).join('') + '</ul></section>' +
      S.ConsultBox() + (b.toc.length > 2 ? '<div class="st-sticky">' + S.MiniTOC({ items: b.toc }) + '</div>' : '') +
      '</aside></div></div>' + S.Footer() + '</div>';
  };

  /* ---------- info page (about, policy …) ---------- */
  S.InfoPage = function (p) {
    var b = plainBody(p.body);
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: crumbs(p) }) + '<main id="main">' + Hero(p, 'ABOUT') +
      '<div class="st-container"><div class="st-info">' + (b.toc.length > 3 ? '<div class="st-intro st-intro--col">' + S.TableOfContents({ items: b.toc }) + '</div>' : '') + b.html +
      (p.updatedNote ? '<p class="st-info__date">' + esc(p.updatedNote) + '</p>' : '') +
      (p.links && p.links.length ? '<nav class="st-block" aria-labelledby="ir-t"><div class="st-endhead"><h2 id="ir-t">関連ページ</h2></div><ul class="st-endlist">' + refs(p.links).map(function (x) { return '<li><a href="' + esc(href(x.path)) + '"><span>' + esc(x.title) + '</span>' + icon('chevR') + '</a></li>'; }).join('') + '</ul></nav>' : '') +
      '</div></div></main>' + S.Footer() + '</div>';
  };

  /* ---------- hub page (purpose, guides, lists) ---------- */
  function section(s, i) {
    var items = s.items ? refs(s.items) : [];
    if (s.auto) items = autoList(s.auto).concat(items);
    if (s.limit) items = items.slice(0, s.limit);
    var inner = s.component ? S[s.component](s.props || {}) : s.html ? plainBody(s.html).html : (s.style === 'list' ? RefList(items) : RefGrid(items, { desc: true, cols: s.cols }));
    return '<section class="st-section' + (s.band ? ' st-band st-band--soft' : '') + '" id="' + esc(s.id || 'sec' + i) + '" aria-labelledby="hs' + i + '">' + S.SectionHeading({ title: s.title, en: s.en || 'Guide', more: s.more, id: 'hs' + i }) + (s.desc ? '<p class="st-hub__desc">' + esc(s.desc) + '</p>' : '') + inner + '</section>';
  }
  function autoList(q) {
    var l = S.colAll();
    if (q.cats) l = l.filter(function (a) { return q.cats.indexOf(a.cat) > -1; });
    if (q.kw) { var re = new RegExp(q.kw); l = l.filter(function (a) { return re.test(a.title); }); }
    if (q.siteCat) l = S.colForSiteCat(q.siteCat);
    if (q.featuredFirst) l = l.slice().sort(function (x, y) { return (y.featured ? 1 : 0) - (x.featured ? 1 : 0); });
    return l.map(S.colCard);
  }
  S.HubPage = function (p) {
    var b = p.body ? plainBody(p.body) : null, nav = '';
    if (p.sections && p.sections.length > 2) nav = '<nav class="st-colcats" aria-label="このページの内容"><ul>' + p.sections.map(function (s, i) { return '<li><a href="#' + esc(s.id || 'sec' + i) + '">' + icon(s.icon || 'book') + esc(s.title) + '</a></li>'; }).join('') + '</ul></nav>';
    return '<div class="st">' + S.Header({ active: p.nav || '' }) + S.Breadcrumb({ items: crumbs(p) }) + '<main id="main">' + Hero(Object.assign({}, p, { heroNav: nav }), 'GUIDE') +
      '<div class="st-container">' + (b ? '<section class="st-section"><div class="st-hub__intro">' + b.html + '</div></section>' : '') +
      (p.sections || []).map(section).join('') +
      '<section class="st-section st-band st-band--last" aria-labelledby="hc-t">' + S.SectionHeading({ title: 'カテゴリから探す', en: 'Category', id: 'hc-t' }) + S.ColCatCards() + '</section></div></main>' + S.Footer() + '</div>';
  };

  /* ---------- form page ---------- */
  function field(f, form) {
    var id = form + '-' + f.name, req = f.required ? ' required aria-required="true"' : '', lab = '<label class="st-form__label" for="' + id + '">' + esc(f.label) + (f.required ? '<span class="st-form__req">必須</span>' : '<span class="st-form__opt">任意</span>') + '</label>';
    var hint = f.hint ? '<p class="st-form__hint" id="' + id + '-h">' + esc(f.hint) + '</p>' : '', desc = f.hint ? ' aria-describedby="' + id + '-h"' : '';
    if (f.type === 'select') return '<div class="st-form__row">' + lab + hint + '<select class="st-form__input" id="' + id + '" name="' + esc(f.name) + '"' + req + desc + '><option value="">選択してください</option>' + f.options.map(function (o) { return '<option>' + esc(o) + '</option>'; }).join('') + '</select></div>';
    if (f.type === 'textarea') return '<div class="st-form__row">' + lab + hint + '<textarea class="st-form__input" id="' + id + '" name="' + esc(f.name) + '" rows="' + (f.rows || 6) + '"' + req + desc + (f.placeholder ? ' placeholder="' + esc(f.placeholder) + '"' : '') + '></textarea></div>';
    if (f.type === 'checks') return '<fieldset class="st-form__row st-form__checks"><legend class="st-form__label">' + esc(f.label) + (f.required ? '<span class="st-form__req">必須</span>' : '<span class="st-form__opt">任意</span>') + '</legend>' + hint + '<div>' + f.options.map(function (o, i) { return '<label><input type="checkbox" name="' + esc(f.name) + '" value="' + esc(o) + '">' + esc(o) + '</label>'; }).join('') + '</div></fieldset>';
    return '<div class="st-form__row">' + lab + hint + '<input class="st-form__input" id="' + id + '" name="' + esc(f.name) + '" type="' + (f.type || 'text') + '"' + req + desc + (f.autocomplete ? ' autocomplete="' + f.autocomplete + '"' : '') + (f.placeholder ? ' placeholder="' + esc(f.placeholder) + '"' : '') + '></div>';
  }
  S.FormPage = function (p) {
    var b = p.body ? plainBody(p.body) : null, f = p.form, name = f.name, ep = formEp(name);
    var form = '<form class="st-form" name="' + esc(name) + '" method="post" action="' + esc(ep.replace('/ajax/', '/')) + '" data-netlify="true" netlify-honeypot="bot-field" data-st-form>' +
      '<input type="hidden" name="form-name" value="' + esc(name) + '">' + (f.subject ? '<input type="hidden" name="_subject" value="' + esc(f.subject) + '"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">' : '') + '<p class="st-sr"><label>入力しないでください <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>' +
      f.fields.map(function (x) { return field(x, name); }).join('') +
      '<div class="st-form__row st-form__agree"><label><input type="checkbox" name="agree" value="同意する" required aria-required="true"><span><a class="st-a" href="' + esc(href('/privacy/')) + '" target="_blank" rel="noopener">プライバシーポリシー</a>に同意する</span><span class="st-form__req">必須</span></label></div>' +
      '<div class="st-form__submit">' + '<button class="st-btn st-btn--primary st-btn--block" type="submit">' + esc(f.submit || '送信する') + icon('arrow') + '</button></div>' +
      '<p class="st-form__status" role="status" aria-live="polite" data-st-form-status></p></form>';
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: crumbs(p) }) + '<main id="main">' + Hero(p, 'FORM') +
      '<div class="st-container"><div class="st-formwrap"><div class="st-formwrap__main">' + (b ? b.html : '') + form + '</div>' +
      '<aside class="st-formwrap__side">' + (p.side ? plainBody(p.side).html : '') + '</aside></div></div></main>' + S.Footer() + '</div>';
  };
  function formEp(name) { return (S.config.formEndpoints || {})[name] || S.config.formEndpoint || ''; }
  function bindForms(root) {
    Array.prototype.forEach.call((root || document).querySelectorAll('[data-st-form]'), function (form) {
      if (form._st) return; form._st = 1;
      form.addEventListener('submit', function (e) {
        var st = form.querySelector('[data-st-form-status]');
        if (!form.checkValidity()) return;
        var ep = formEp(form.getAttribute('name'));
        if (!ep && !/netlify/.test(location.hostname) && !S.config.netlifyForms) { e.preventDefault(); st.textContent = 'ただいまフォームの受付準備中です。恐れ入りますが、時間をおいて再度お試しください。'; return; }
        if (ep) {
          e.preventDefault();
          var bot = form.querySelector('[name="bot-field"]'); if (bot && bot.value) return;
          var fd = new FormData(form), data = {}; fd.forEach(function (v, k) { if (k === 'bot-field' || k === 'form-name') return; data[k] = data[k] ? data[k] + '、' + v : v; });
          st.textContent = '送信しています…';
          fetch(ep, { method: 'POST', body: JSON.stringify(data), headers: { 'Content-Type': 'application/json', Accept: 'application/json' } })
            .then(function (r) { if (!r.ok) throw 0; form.reset(); st.textContent = '送信しました。内容を確認のうえ、担当よりご連絡します。'; })
            .catch(function () { st.textContent = '送信できませんでした。通信環境をご確認のうえ、もう一度お試しください。'; });
        }
      });
    });
  }

  /* ---------- glossary ---------- */
  var ROWS = [['あ', 'あいうえおぁぃぅぇぉ'], ['か', 'かきくけこがぎぐげご'], ['さ', 'さしすせそざじずぜぞ'], ['た', 'たちつてとだぢづでどっ'], ['な', 'なにぬねの'], ['は', 'はひふへほばびぶべぼぱぴぷぺぽ'], ['ま', 'まみむめも'], ['や', 'やゆよゃゅょ'], ['ら', 'らりるれろ'], ['わ', 'わをん']];
  function rowOf(y) { var c = (y || '').charAt(0); for (var i = 0; i < ROWS.length; i++) if (ROWS[i][1].indexOf(c) > -1) return ROWS[i][0]; return 'A'; }
  S.GlossaryPage = function (p) {
    var groups = {}; p.terms.slice().sort(function (a, b) { return a.yomi < b.yomi ? -1 : 1; }).forEach(function (t) { var r = rowOf(t.yomi); (groups[r] = groups[r] || []).push(t); });
    var keys = ROWS.map(function (r) { return r[0]; }).filter(function (k) { return groups[k]; });
    var nav = '<nav class="st-gloss__nav" aria-label="五十音で探す"><ul>' + ROWS.map(function (r) { return '<li>' + (groups[r[0]] ? '<a href="#g-' + r[0] + '">' + r[0] + '</a>' : '<span aria-disabled="true">' + r[0] + '</span>') + '</li>'; }).join('') + '</ul></nav>';
    var body = keys.map(function (k) {
      return '<section class="st-gloss__group" aria-labelledby="g-' + k + '"><h2 class="st-gloss__head" id="g-' + k + '">' + k + '行</h2><dl class="st-gloss__list">' + groups[k].map(function (t) {
        return '<div class="st-gloss__item" id="' + esc(t.id) + '"><dt>' + esc(t.t) + '<small>' + esc(t.yomi) + '</small></dt><dd><p>' + links(esc(t.d)) + '</p>' + (t.link ? '<p class="st-gloss__more"><a class="st-a" href="' + esc(href(S.ref(t.link) ? S.ref(t.link).path : t.link)) + '">' + esc(t.linkText || (S.ref(t.link) ? S.ref(t.link).title : '関連記事')) + '</a></p>' : '') + '</dd></div>';
      }).join('') + '</dl></section>';
    }).join('');
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: crumbs(p) }) + '<main id="main">' + Hero(Object.assign({}, p, { heroNav: nav }), 'GLOSSARY') +
      '<div class="st-container"><div class="st-gloss">' + body + '</div></div></main>' + S.Footer() + '</div>';
  };

  /* ---------- tag / new / search / 404 ---------- */
  S.tagIndex = function () {
    if (S._tags) return S._tags; var m = {};
    function add(t, card) { if (!t) return; (m[t] = m[t] || []); if (!m[t].some(function (x) { return x.path === card.path; })) m[t].push(card); }
    S.colAll().forEach(function (a) { (a.tags || []).forEach(function (t) { add(t, S.colCard(a)); }); });
    S.pgAll().forEach(function (p) { (p.tags || []).forEach(function (t) { add(t, S.pgCard(p)); }); });
    S.data.articles.forEach(function (a) { (a.tags || []).forEach(function (t) { var r = S.ref(a.path) || a; add(t, r); }); });
    return (S._tags = m);
  };
  S.tagPath = function (t) { return '/tag/' + encodeURIComponent(t) + '/'; };
  S.TagPage = function (t) {
    var list = (S.tagIndex()[t] || []).slice().sort(function (a, b) { return a.date < b.date ? 1 : -1; });
    var others = Object.keys(S.tagIndex()).filter(function (x) { return x !== t && S.tagIndex()[x].length > 2; }).slice(0, 24);
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: 'タグ' }, { name: '#' + t }] }) + '<main id="main">' +
      Hero({ title: '#' + t + ' の記事一覧', lead: '「' + t + '」に関する記事を新しい順にまとめています（' + list.length + '件）。' }, 'TAG') +
      '<div class="st-container"><section class="st-section" aria-label="記事一覧">' + RefGrid(list, { desc: true }) + '</section>' +
      (others.length ? '<section class="st-section" aria-labelledby="to-t">' + S.SectionHeading({ title: 'ほかのタグ', en: 'Tags', id: 'to-t' }) + S.TagList({ tags: others }) + '</section>' : '') + '</div></main>' + S.Footer() + '</div>';
  };
  S.allCards = function () {
    var seen = {}, out = [];
    S.colAll().map(S.colCard).concat(S.pgAll().filter(function (p) { return p.kind === 'article'; }).map(S.pgCard)).forEach(function (c) { if (!seen[c.path]) { seen[c.path] = 1; out.push(c); } });
    return out.sort(function (a, b) { return a.date < b.date ? 1 : a.date > b.date ? -1 : 0; });
  };
  S.NewPage = function () {
    var l = S.allCards().slice(0, 36);
    return '<div class="st">' + S.Header({ active: 'new' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: '新着記事' }] }) + '<main id="main">' +
      Hero({ title: '新着記事', lead: '公開・更新した記事を新しい順に並べています。コラムの一覧はカテゴリ別にも探せます。', heroNav: S.ColCatNav({ withAll: true }) }, 'NEW ARTICLES') +
      '<div class="st-container"><section class="st-section" aria-label="新着記事">' + RefGrid(l.slice(0, 3), { cols: 3, desc: true }).replace(/loading="lazy"/g, 'fetchpriority="high"') + RefGrid(l.slice(3), { desc: true }) + '<p class="st-hub__more">' + S.Button({ href: '/column/page/2/', label: 'もっと見る（コラム一覧へ）', variant: 'outline' }) + '</p></section></div></main>' + S.Footer() + '</div>';
  };
  S.SearchPage = function () {
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: '検索結果' }] }) + '<main id="main">' +
      Hero({ title: 'サイト内検索', lead: 'キーワードを入れると、記事のタイトル・説明・タグから探します。' }, 'SEARCH') +
      '<div class="st-container"><section class="st-section"><div class="st-searchpage">' + S.Search({ id: 'st-q-page', placeholder: '例：人工芝 費用' }) + '</div><div data-st-searchresults></div></section></div></main>' + S.Footer() + '</div>';
  };
  S.NotFoundPage = function () {
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: 'ページが見つかりません' }] }) + '<main id="main">' +
      Hero({ title: 'ページが見つかりませんでした', lead: 'URLが変わったか、ページが削除された可能性があります。キーワードで検索するか、カテゴリからお探しください。' }, '404') +
      '<div class="st-container"><section class="st-section"><div class="st-searchpage">' + S.Search({ id: 'st-q-404' }) + '</div></section><section class="st-section" aria-labelledby="nf-t">' + S.SectionHeading({ title: 'よく読まれている記事', en: 'Pick up', id: 'nf-t' }) + RefGrid(FeatList()) + '</section>' +
      '<section class="st-section st-band st-band--last" aria-labelledby="nfc-t">' + S.SectionHeading({ title: 'カテゴリから探す', en: 'Category', id: 'nfc-t' }) + S.ColCatCards() + '</section></div></main>' + S.Footer() + '</div>';
  };
  function bindSearchPage(root) {
    var box = (root || document).querySelector('[data-st-searchresults]'); if (!box) return;
    var q = ''; try { q = new URLSearchParams(location.search).get('q') || ''; } catch (e) {}
    var inp = (root || document).querySelector('#st-q-page'); if (inp) inp.value = q;
    var res = q ? S.searchArticles(q) : [];
    box.innerHTML = q ? '<p class="st-hub__desc" role="status">「' + esc(q) + '」の検索結果：' + res.length + '件</p>' + (res.length ? RefGrid(res, { desc: true }) : '<p>該当する記事が見つかりませんでした。別のキーワードでお試しください。</p>') : '';
  }

  /* ---------- search: columns + pages + data (static pages use window.SOTORINO_SEARCH) ---------- */
  S.searchIndex = function () {
    var seen = {}, out = [];
    function add(c, tags) { if (!c || seen[c.path]) return; seen[c.path] = 1; out.push({ title: c.title, desc: c.desc || '', path: c.path, cat: c.cat, img: c.img, date: c.date, tags: tags || [] }); }
    S.colAll().forEach(function (a) { add(S.colCard(a), a.tags); });
    S.pgAll().forEach(function (p) { if (p.kind !== 'form' && !p.noindex) add(S.pgCard(p), p.tags); });
    S.data.articles.forEach(function (a) { add(S.ref(a.path) || a, a.tags); });
    return out;
  };
  S.searchArticles = function (q) {
    q = (q || '').trim().toLowerCase(); if (!q) return [];
    var terms = q.split(/\s+/), idx = window.SOTORINO_SEARCH || S.searchIndex(), im = window.SOTORINO_SEARCH_IMAGES || {};
    for (var k in im) if (!S.images[k]) S.images[k] = im[k];
    return idx.filter(function (a) { var hay = (a.title + ' ' + a.desc + ' ' + (a.tags || []).join(' ') + ' ' + (S.data.catName[a.cat] || '')).toLowerCase(); return terms.every(function (t) { return hay.indexOf(t) > -1; }); });
  };


  /* ---------- アフィリエイト（承認が下りるまで非公開） ----------
     S.config.affiliate = true にすると：トップのピックアップ商品・記事内の商品カード・/products/pickup/ が公開される。
     false（既定）の間は、商品へのリンクを一切出さず「2027年掲載予定」の予告だけを表示する。 */
  S.config.affiliate = !!S.config.affiliate;
  var _pick = S.PickupProducts, _cards = S.ProductCards;
  S.PickupComing = function (p) {
    p = p || {};
    var tiles = S.data.pickupProducts.slice(0, p.count || 6).map(function (x) { return '<li><span class="st-soon__tile">' + media(x.img, '', '11') + '<span class="st-soon__bar"></span><span class="st-soon__bar st-soon__bar--s"></span></span></li>'; }).join('');
    return '<div class="st-soon" role="note" aria-label="編集部ピックアップ商品は準備中です"><ul class="st-soon__grid" aria-hidden="true">' + tiles + '</ul>' +
      '<div class="st-soon__panel"><p class="st-soon__en">COMING 2027</p><p class="st-soon__title">' + icon('lock') + '編集部ピックアップ商品は<br class="st-br-sp">2027年に掲載予定です</p>' +
      '<p class="st-soon__text">庭・外構のDIYや暮らしに役立つ商品を、編集部の比較基準（素材・耐候性・施工のしやすさ・入手のしやすさ）で選んでご紹介します。公開まで今しばらくお待ちください。</p>' +
      '<p class="st-soon__links"><a class="st-a" href="' + esc(href('/purpose/products/')) + '">商品・素材の選び方の記事を読む</a></p></div></div>';
  };
  S.PickupProducts = function () { return S.config.affiliate ? _pick() : S.PickupComing(); };
  S.ProductCards = function (p) {
    if (S.config.affiliate) return _cards(p);
    return '<section class="st-soon st-soon--inline" role="note"><div class="st-soon__panel"><p class="st-soon__en">COMING 2027</p><p class="st-soon__title">' + icon('lock') + 'おすすめ商品の紹介は準備中です</p><p class="st-soon__text">商品の比較・紹介は2027年に掲載予定です。選び方のポイントは本文と<a class="st-a" href="' + esc(href('/purpose/products/')) + '">商品・素材の選び方</a>の記事でご確認いただけます。</p></div></section>';
  };
  S.PickupPage = function () {
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: 'おすすめ商品を探したい', path: '/purpose/products/' }, { name: '編集部ピックアップ商品' }] }) + '<main id="main">' +
      Hero({ title: '編集部ピックアップ商品', lead: '庭・外構のDIYや暮らしに役立つ商品を、編集部の比較基準で選びました。' }, 'PICK UP') +
      '<div class="st-container"><section class="st-section"><div class="st-hub__intro">' + plainBody('<h2>選定の基準</h2><p>素材、耐候性、施工のしやすさ、入手のしやすさの4つの基準で、編集部が比較して選んでいます。報酬の有無や金額によって、紹介の順番や評価を変えることはありません。価格は取得日時点の参考価格です。最新の価格と在庫は販売ページでご確認ください。</p><p>このページにはアフィリエイトリンクを含みます。詳しくは<a href="{{p:/ads-policy/}}">広告・アフィリエイトについて</a>をご覧ください。</p>').html + '</div></section>' +
      '<section class="st-section" aria-labelledby="pp-t">' + S.SectionHeading({ title: '商品一覧', en: 'Products', id: 'pp-t' }) + _pick() + '</section>' +
      '<section class="st-section" aria-labelledby="pp2-t">' + S.SectionHeading({ title: '商品・素材の選び方', en: 'Guide', id: 'pp2-t' }) + RefList(autoList({ cats: ['products'] })) + '</section></div></main>' + S.Footer() + '</div>';
  };
  var _mount = S.mount;
  S.mount = function (root) { var r = _mount(root); bindForms(root); bindSearchPage(root); return r; };

  /* ---------- routing (preview と静的書き出しで共通) ---------- */
  var catPaths = null;
  function cats() { if (catPaths) return catPaths; catPaths = {}; S.data.nav.concat(S.data.categories).forEach(function (c) { if (!catPaths[c.path]) catPaths[c.path] = c; }); return catPaths; }
  function bc(items) { var o = S.config.siteOrigin; return { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: items.map(function (it, i) { var x = { '@type': 'ListItem', position: i + 1, name: it[0] }; if (it[1]) x.item = o + it[1]; return x; }) }; }
  S.bcLd = bc;
  function pageLd(p) {
    var o = S.config.siteOrigin, ld = [bc([['HOME', '/']].concat(p.crumbs || []).concat([[p.h1 || p.title]]))];
    if (p.kind === 'article') ld.unshift({ '@context': 'https://schema.org', '@type': 'Article', headline: p.title, description: p.description, datePublished: p.date.replace(/\./g, '-'), dateModified: (p.updated || p.date).replace(/\./g, '-'), image: [pgImgAbs(p)], author: { '@type': 'Organization', name: 'SOTORINO編集部', url: o + '/about/editors/' }, publisher: { '@type': 'Organization', name: 'SOTORINO', logo: { '@type': 'ImageObject', url: o + '/img/logo.png' } }, mainEntityOfPage: o + p.path });
    if (p.faq && p.faq.length) ld.push({ '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: p.faq.map(function (q) { return { '@type': 'Question', name: q.q, acceptedAnswer: { '@type': 'Answer', text: q.a.replace(/<[^>]+>/g, '') } }; }) });
    if (p.kind === 'glossary') ld.push({ '@context': 'https://schema.org', '@type': 'DefinedTermSet', name: p.title, hasDefinedTerm: p.terms.map(function (t) { return { '@type': 'DefinedTerm', name: t.t, description: t.d, url: o + p.path + '#' + t.id }; }) });
    if (p.kind === 'info' && /about/.test(p.path)) ld.push({ '@context': 'https://schema.org', '@type': 'Organization', name: 'SOTORINO', url: o + '/', logo: o + '/img/logo.png' });
    return ld;
  }
  S.route = function (path) {
    var m, html, seo = null, o = S.config.siteOrigin, about = S.data.footer.about;
    function set(title, desc, ld, extra) { seo = Object.assign({ title: title, description: String(desc || '').replace(/<[^>]+>/g, ''), path: path, ld: ld || [] }, extra || {}); }
    if (path === '/') { html = S.TopPage(); set('SOTORINO（ソトリノ）｜庭・外構・住まい・土地の情報メディア', about, [{ '@context': 'https://schema.org', '@type': 'WebSite', name: 'SOTORINO', url: o + '/', inLanguage: 'ja', potentialAction: { '@type': 'SearchAction', target: o + '/search/?q={search_term_string}', 'query-input': 'required name=search_term_string' } }, { '@context': 'https://schema.org', '@type': 'Organization', name: 'SOTORINO', url: o + '/', logo: o + '/img/logo.png' }], { priority: '1.0' }); }
    else if (path === '/column/') { html = S.ColumnListPage(1); set('家まわりのコラム｜SOTORINO', '外構・庭づくり・DIYから、住宅設備、リフォーム、土地選び、補助金、季節のメンテナンスまで、家まわりの疑問に答えるコラム一覧です。', [bc([['HOME', '/'], ['コラム']])], { next: '/column/page/2/', priority: '0.7' }); }
    else if ((m = /^\/column\/page\/(\d+)\/$/.exec(path))) { var n = +m[1], tot = Math.ceil(S.colAll().length / 12); if (n < 2 || n > tot) return null; html = S.ColumnListPage(n); set('コラム一覧（' + n + 'ページ目）｜SOTORINO', '家まわりのコラム一覧（' + n + 'ページ目）。外構・庭づくり・DIY・住宅設備・リフォーム・土地・補助金・季節のメンテナンスまで、新しい順に記事を紹介しています。', [bc([['HOME', '/'], ['コラム', '/column/'], [n + 'ページ目']])], { prev: n > 2 ? '/column/page/' + (n - 1) + '/' : '/column/', next: n < tot ? '/column/page/' + (n + 1) + '/' : null, priority: '0.5' }); }
    else if ((m = /^\/column\/category\/([a-z]+)\/$/.exec(path))) { var c = S.colCats.filter(function (x) { return x.key === m[1]; })[0]; if (!c) return null; html = S.ColumnCategoryPage(c.key); set(c.full + 'のコラム一覧｜SOTORINO', c.desc.slice(0, 120), [bc([['HOME', '/'], ['コラム', '/column/'], [c.full]])], { priority: '0.8' }); }
    else if (path === '/column/shiba/') { html = S.SeriesPage('column'); set('人工芝職人が語る現場の本音｜SOTORINO', '何千㎡も芝を敷いてきた施工スタッフが、カタログには載らない現場の話を語る連載コラムです。', [bc([['HOME', '/'], ['コラム', '/column/'], ['人工芝職人が語る現場の本音']])], { priority: '0.5' }); }
    else if (path === '/exterior/trap/') { html = S.SeriesPage('trap'); set('外構工事の罠！？ あとから気づく落とし穴｜SOTORINO', '見積もり、境界、排水、補助金。あとから気づいても遅い外構工事の落とし穴をテーマ別に解説します。', [bc([['HOME', '/'], ['外構・エクステリア', '/exterior/'], ['外構工事の罠']])], { priority: '0.6' }); }
    else if ((m = /^\/column\/([a-z0-9-]+)\/$/.exec(path)) && S.colBySlug(m[1])) { var a = S.colBySlug(m[1]), cs = S.colSeo(a, o); html = S.ColumnArticlePage(a.slug); set(cs.title, cs.description, [cs.article, cs.breadcrumb].concat(cs.faq ? [cs.faq] : []), { og: 'article', image: '/img/col/' + a.slug + '.jpg', priority: a.featured ? '0.9' : '0.6', lastmod: a.date }); seo.title = cs.title; }
    else if (path === '/garden/turf/') { html = S.CategoryPage(); set('人工芝ガイド｜選び方・費用・施工・お手入れ｜SOTORINO', '人工芝の基礎知識から、性能・下地・DIY・費用・メンテナンス・業者選びまでを9章で体系的に解説する人工芝ガイドです。', [bc([['HOME', '/'], ['庭づくり', '/garden/'], ['人工芝']])], { priority: '0.8' }); }
    else if (path === '/exterior/fence/fence-guide/') { var fa = S.article('fence-guide'); html = S.ArticlePage(); set(fa.title + '｜SOTORINO', S.data.fenceArticle.lead, [bc([['HOME', '/'], ['外構・エクステリア', '/exterior/'], ['フェンス', '/exterior/fence/'], [fa.title]])], { og: 'article', priority: '0.9' }); }
    else if (path === '/qa/') { html = S.QAPage(); set('読者の質問箱｜SOTORINO', '人工芝・フェンス・費用・補助金・工事・お手入れについて、読者から寄せられた質問にテーマ別にお答えします。', [bc([['HOME', '/'], ['読者の質問箱']])], { priority: '0.6' }); }
    else if ((m = /^\/qa\/([a-z]+)\/$/.exec(path))) { var qc = S.data.qaCats.filter(function (x) { return x.id === m[1]; })[0]; if (!qc) return null; html = S.QAPage(qc.id); set(qc.name + 'の質問｜読者の質問箱｜SOTORINO', qc.name + 'について、読者から寄せられた質問と答えをまとめました。くわしく知りたい方は、各回答からテーマ別の解説記事もご覧いただけます。', [bc([['HOME', '/'], ['読者の質問箱', '/qa/'], [qc.name]]), { '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: qc.items.map(function (q) { return { '@type': 'Question', name: q.q, acceptedAnswer: { '@type': 'Answer', text: q.a } }; }) }], { priority: '0.5' }); }
    else if (path === '/campaign/autumn-2026/') { html = S.CampaignPage(); set('秋のプレゼントキャンペーン（2026年11月30日まで）｜SOTORINO', 'アンケートに答えて、ガーデングッズが当たる秋のプレゼントキャンペーン。応募方法・期間・注意事項のご案内です。', [bc([['HOME', '/'], ['キャンペーン', '/campaign/'], ['秋のプレゼントキャンペーン']])], { priority: '0.4' }); }
    else if (path === '/products/pickup/') { if (!S.config.affiliate) return null; html = S.PickupPage(); set('編集部ピックアップ商品｜SOTORINO', '庭・外構のDIYや暮らしに役立つ商品を、素材・耐候性・施工のしやすさ・入手のしやすさの基準で編集部が選んで紹介します。', [bc([['HOME', '/'], ['おすすめ商品を探したい', '/purpose/products/'], ['編集部ピックアップ商品']])], { priority: '0.5' }); }
    else if (path === '/new/') { html = S.NewPage(); set('新着記事｜SOTORINO', '庭・外構・住まい・土地・お金の新着記事一覧です。公開・更新した記事を新しい順に紹介し、カテゴリ別のコラム一覧にもご案内します。', [bc([['HOME', '/'], ['新着記事']])], { priority: '0.7' }); }
    else if (path === '/search/') { html = S.SearchPage(); set('サイト内検索｜SOTORINO', 'SOTORINOの記事をキーワードで検索できます。', [], { noindex: true }); }
    else if ((m = /^\/tag\/([^/]+)\/$/.exec(path))) { var t; try { t = decodeURIComponent(m[1]); } catch (e) { t = m[1]; } var tl = S.tagIndex()[t]; if (!tl) return null; html = S.TagPage(t); set('#' + t + ' の記事一覧｜SOTORINO', '「' + t + '」に関する記事の一覧です（' + tl.length + '件）。SOTORINOの庭・外構・住まいの記事から、このテーマの記事を新しい順にまとめています。', [bc([['HOME', '/'], ['#' + t]])], { noindex: tl.length < 2, priority: '0.3' }); }
    else if (S.pgByPath(path)) {
      var p = S.pgByPath(path);
      html = p.kind === 'article' ? S.ContentPage(p) : p.kind === 'info' ? S.InfoPage(p) : p.kind === 'form' ? S.FormPage(p) : p.kind === 'glossary' ? S.GlossaryPage(p) : S.HubPage(p);
      set(p.seoTitle || (p.title + '｜SOTORINO'), p.description, pageLd(p), { og: p.kind === 'article' ? 'article' : 'website', image: p.kind === 'article' ? '/' + (S.images['page-' + p.key] || '').replace(/^\//, '') : null, noindex: !!p.noindex, priority: p.priority || (p.kind === 'article' ? '0.7' : p.kind === 'hub' ? '0.7' : '0.3'), lastmod: p.updated || p.date });
    }
    else if (cats()[path] && S.siteCatRules[cats()[path].id]) { var sc = cats()[path]; html = S.SiteCategoryPage(sc); set(sc.name + 'の記事一覧｜SOTORINO', S.siteCatRules[sc.id].intro, [bc([['HOME', '/'], [sc.name]])], { priority: '0.8' }); }
    else return null;
    return { html: html, seo: seo };
  };
  /* すべての公開パス（静的書き出し・サイトマップ用） */
  S.allPaths = function () {
    var l = ['/', '/column/'], tot = Math.ceil(S.colAll().length / 12), i;
    for (i = 2; i <= tot; i++) l.push('/column/page/' + i + '/');
    S.colCats.forEach(function (c) { l.push(S.colCatPath(c.key)); });
    S.colAll().forEach(function (a) { l.push(S.colPath(a)); });
    Object.keys(cats()).forEach(function (p) { if (S.siteCatRules[cats()[p].id]) l.push(p); });
    l.push('/column/shiba/', '/exterior/trap/', '/garden/turf/', '/exterior/fence/fence-guide/', '/qa/', '/campaign/autumn-2026/', '/new/', '/search/');
    S.data.qaCats.forEach(function (c) { l.push('/qa/' + c.id + '/'); });
    S.pgAll().forEach(function (p) { l.push(p.path); });
    if (S.config.affiliate) l.push('/products/pickup/');
    Object.keys(S.tagIndex()).forEach(function (t) { l.push(S.tagPath(t)); });
    var seen = {}; return l.filter(function (p) { if (seen[p]) return false; seen[p] = 1; return true; });
  };
})();
