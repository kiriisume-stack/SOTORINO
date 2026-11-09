(function () {
  'use strict';
  var S = (window.Sotorino = window.Sotorino || {});

  /* ================= config & image registry ================= */
  S.config = S.config || {
    base: '#',            // '#' → hash links (design previews). Set '' in production.
    logoSrc: null,        // set to a logo image URL to replace the text wordmark
    siteName: 'SOTORINO',
    favoritesKey: 'sotorino:favorites',
    autoplayMs: 6500
  };
  // Every image is referenced by KEY. Swap all photos in one place: Sotorino.setImages({ 'hero-01': '/img/hero-01.jpg', ... })
  S.images = __IMAGES__;
  S.setImages = function (map) { for (var k in map) if (Object.prototype.hasOwnProperty.call(map, k)) S.images[k] = map[k]; };

  /* ================= helpers ================= */
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function href(p) { if (!p) return '#'; if (/^(https?:)?\/\//.test(p)) return p; return (S.config.base === '#' ? '#' : '') + p; }
  function attr(o) { var s = ''; for (var k in o) if (o[k] != null && o[k] !== false) s += ' ' + k + '="' + esc(o[k] === true ? '' : o[k]) + '"'; return s; }
  function cx() { return Array.prototype.filter.call(arguments, Boolean).join(' '); }
  S.esc = esc; S.href = href;

  var ICONS = {
    search: '<circle cx="11" cy="11" r="6.8"/><path d="M20 20l-4.2-4.2"/>',
    heart: '<path d="M12 20s-7.5-4.6-7.5-10.2A4.2 4.2 0 0 1 12 7.3a4.2 4.2 0 0 1 7.5 2.5C19.5 15.4 12 20 12 20z"/>',
    menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
    close: '<path d="M6 6l12 12M18 6L6 18"/>',
    arrow: '<path d="M4.5 12h15M13.5 6l6 6-6 6"/>',
    chevL: '<path d="M14.5 6l-6 6 6 6"/>',
    chevR: '<path d="M9.5 6l6 6-6 6"/>',
    chevD: '<path d="M6 9.5l6 6 6-6"/>',
    clock: '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    update: '<path d="M19.5 12a7.5 7.5 0 1 1-2.2-5.3"/><path d="M19.5 4.5v4h-4"/>',
    home: '<path d="M4 11l8-6.5 8 6.5"/><path d="M6.5 9.5V19h11V9.5"/>',
    check: '<path d="M5.5 12.5l4 4 9-9.5"/>',
    eye: '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
    lock: '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
    house: '<path d="M3.5 11.5L12 4.5l8.5 7"/><path d="M6 10v9.5h12V10"/><path d="M10 19.5v-5h4v5"/>',
    leaf: '<path d="M5 19c0-8.5 5.5-13.5 14.5-14 0 9-5.5 14-14.5 14z"/><path d="M5 19c3-4 6.5-7 10-9"/>',
    wind: '<path d="M3 8.5h10.5a2.8 2.8 0 1 0-2.8-2.8M3 15.5h14a3 3 0 1 1-3 3M3 12h7.5"/>',
    yen: '<path d="M7 4.5l5 7 5-7M12 11.5v8M8 12.5h8M8 15.5h8"/>',
    coins: '<ellipse cx="12" cy="6.5" rx="7" ry="2.7"/><path d="M5 6.5v5c0 1.5 3.1 2.7 7 2.7s7-1.2 7-2.7v-5M5 11.5v5.5c0 1.5 3.1 2.7 7 2.7s7-1.2 7-2.7v-5.5"/>',
    image: '<rect x="3.5" y="5" width="17" height="14" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M20.5 16l-5-5-8 8"/>',
    cart: '<path d="M3 4.5h2.3l2.2 10.5h10.3l2-7.5H6.4"/><circle cx="9.5" cy="19" r="1.4"/><circle cx="16.5" cy="19" r="1.4"/>',
    user: '<circle cx="12" cy="8.5" r="3.8"/><path d="M4.5 20c1.2-4 4-6 7.5-6s6.3 2 7.5 6"/>',
    doc: '<path d="M6.5 3.5h7.5l4 4v13h-11.5z"/><path d="M14 3.5v4h4M9.5 12h5.5M9.5 15.5h5.5"/>',
    alert: '<path d="M12 4.5l8.5 15h-17z"/><path d="M12 10v4M12 16.8v.2"/>',
    info: '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5M12 8v.2"/>',
    bulb: '<path d="M9.5 17.5h5M10.3 20.5h3.4M12 3.5a5.8 5.8 0 0 0-3.4 10.5c.6.5.9 1.1.9 1.8v.7h5v-.7c0-.7.3-1.3.9-1.8A5.8 5.8 0 0 0 12 3.5z"/>',
    link: '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    book: '<path d="M4 5.5c3-1.3 5.5-1.3 8 .6 2.5-1.9 5-1.9 8-.6V19c-3-1.3-5.5-1.3-8 .6-2.5-1.9-5-1.9-8-.6z"/><path d="M12 6.1v13.5"/>',
    pause: '<path d="M9 6.5v11M15 6.5v11"/>',
    play: '<path d="M8.5 6l10 6-10 6z"/>',
    pin: '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    shield: '<path d="M12 3.5l7 3v5.5c0 4.5-3 7.5-7 8.5-4-1-7-4-7-8.5V6.5z"/><path d="M9 12l2.2 2.2L15.5 10"/>',
    tool: '<path d="M14.7 6.3a4 4 0 0 0 5 5l-8.2 8.2a2.1 2.1 0 0 1-3-3z"/><path d="M14.7 6.3l2-2"/>',
    tag: '<path d="M3.5 12.5V4h8.5l8.5 8.5-8.5 8.5z"/><circle cx="8" cy="8.5" r="1.4"/>',
    calendar: '<rect x="4" y="5.5" width="16" height="14.5" rx="2"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/>',
    copy: '<rect x="8.5" y="8.5" width="11" height="11" rx="2"/><path d="M15.5 8.5v-3a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h3"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    minus: '<path d="M5 12h14"/>',
    share: '<circle cx="18" cy="5.5" r="2.5"/><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="18.5" r="2.5"/><path d="M8.2 10.8l7.6-4.1M8.2 13.2l7.6 4.1"/>',
    chat: '<path d="M4.5 5.5h15v10h-8l-4.5 3.5v-3.5h-2.5z"/>',
    sprout: '<path d="M12 20v-8"/><path d="M12 12c0-4-3-6.5-7-6.5 0 4 3 6.5 7 6.5zM12 14c0-3.5 2.6-5.5 6.5-5.5 0 3.5-2.6 5.5-6.5 5.5z"/>',
    ruler: '<rect x="3" y="8" width="18" height="8" rx="1.5"/><path d="M7 8v3M11 8v4M15 8v3M19 8v4"/>',
    drop: '<path d="M12 3.5s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    paw: '<circle cx="7" cy="9" r="1.8"/><circle cx="11" cy="6" r="1.8"/><circle cx="15.5" cy="7" r="1.8"/><circle cx="18" cy="11" r="1.8"/><path d="M8 16.5c0-2.5 2-4.5 4.5-4.5s4 2 4 4c0 2-1.5 3-3 3-1 0-1.5-.5-2.5-.5S9.5 19 9 19c-.6 0-1-1-1-2.5z"/>',
    layers: '<path d="M12 4l8.5 4.5L12 13 3.5 8.5z"/><path d="M3.5 12.5L12 17l8.5-4.5M3.5 16.5L12 21l8.5-4.5"/>',
    scale: '<path d="M12 4v16M6 20h12M5 8h14"/><path d="M5 8l-2.5 6a2.8 2.8 0 0 0 5 0zM19 8l-2.5 6a2.8 2.8 0 0 0 5 0z"/>'
  };
  function icon(name, cls) { return '<svg class="' + cx('st-ico', cls) + '" viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + (ICONS[name] || '') + '</svg>'; }
  S.icon = icon; S.iconNames = Object.keys(ICONS);

  // Image slot. Missing key → labelled placeholder so layouts never collapse.
  function img(key, alt, o) {
    o = o || {};
    var src = S.images[key] || (o.src || null);
    if (!src) return '<span class="st-img st-img--empty" role="img" aria-label="' + esc(alt || '') + '"><span>画像: ' + esc(key || '未設定') + '</span></span>';
    return '<img class="st-img" src="' + esc(src) + '" alt="' + esc(alt || '') + '"' + (o.eager ? ' fetchpriority="high"' : ' loading="lazy"') + ' decoding="async">';
  }
  function media(key, alt, ratio, cls) { return '<span class="' + cx('st-media', 'st-r-' + (ratio || '32'), cls) + '">' + img(key, alt) + '</span>'; }
  S.img = img; S.media = media;

  /* ================= data ================= */
  var TONE = { 'col-basics': 'outdoor', 'col-garden': 'outdoor', 'col-diy': 'life', 'col-products': 'home', 'col-cost': 'property', 'col-trouble': 'home', 'col-equipment': 'home', 'col-reform': 'home', 'col-realestate': 'property', 'col-money': 'property', 'col-lifestyle': 'life', garden: 'outdoor', turf: 'outdoor', exterior: 'outdoor', carport: 'outdoor', deck: 'outdoor', equipment: 'home', reform: 'home', realestate: 'property', money: 'property', life: 'life' };
  S.data = {
    nav: [
      { id: 'new', name: '新着記事', path: '/new/' },
      { id: 'column', name: 'コラム', path: '/column/' },
      { id: 'garden', name: '庭づくり', path: '/garden/' },
      { id: 'exterior', name: '外構・エクステリア', path: '/exterior/' },
      { id: 'equipment', name: '住宅設備', path: '/equipment/' },
      { id: 'reform', name: 'リフォーム', path: '/reform/' },
      { id: 'realestate', name: '不動産・土地', path: '/realestate/' },
      { id: 'money', name: 'お金・補助金', path: '/money/' },
      { id: 'life', name: '暮らしの知識', path: '/life/' },
      { id: 'video', name: '動画', path: '/video/' },
      { id: 'cases', name: '施工例', path: '/cases/' }
    ],
    categories: [
      { id: 'garden', name: '庭づくり', sub: 'ガーデニング・人工芝', img: 'cat-garden', path: '/garden/' },
      { id: 'exterior', name: '外構・エクステリア', sub: 'フェンス・門まわり', img: 'cat-exterior', path: '/exterior/' },
      { id: 'carport', name: '駐車場・カーポート', sub: '土間・コンクリート', img: 'cat-carport', path: '/exterior/carport/' },
      { id: 'deck', name: 'ウッドデッキ', sub: 'テラス・タイル', img: 'cat-deck', path: '/exterior/deck/' },
      { id: 'equipment', name: '住宅設備', sub: '門扉・照明・物置', img: 'cat-equipment', path: '/equipment/' },
      { id: 'reform', name: 'リフォーム', sub: '増改築・外壁', img: 'cat-reform', path: '/reform/' },
      { id: 'realestate', name: '不動産・土地', sub: '売却・購入・査定', img: 'cat-realestate', path: '/realestate/' },
      { id: 'money', name: 'お金・補助金', sub: '費用・ローン', img: 'cat-money', path: '/money/' },
      { id: 'life', name: '暮らしの知識', sub: 'メンテナンス・DIY', img: 'cat-life', path: '/life/' }
    ],
    catName: { garden: '庭づくり', turf: '人工芝', exterior: '外構・エクステリア', carport: '駐車場・カーポート', deck: 'ウッドデッキ', equipment: '住宅設備', reform: 'リフォーム', realestate: '不動産・土地', money: 'お金・補助金', life: '暮らしの知識' },
    articles: [
      { id: 'garden-guide', cat: 'garden', title: 'おしゃれな庭のつくり方｜実例と費用の完全ガイド', desc: '理想の庭を叶えるためのポイント、費用相場、失敗しない業者の選び方までわかりやすく解説。', img: 'feat-garden', date: '2026.10.25', path: '/garden/garden-guide/', tags: ['庭づくり', '費用', '実例'] },
      { id: 'exterior-flow', cat: 'exterior', title: '後悔しない外構工事の進め方｜費用と注意点を徹底解説', desc: '相談から完成までの流れと、見積もりで確認したい項目を整理。', img: 'feat-exterior', date: '2026.10.22', path: '/exterior/exterior-flow/', tags: ['外構', '費用', '業者選び'] },
      { id: 'land-check', cat: 'realestate', title: '土地を購入する前に確認すべき15のポイント！現地調査で見るべき項目', desc: '土地の購入前には、現地調査を含めた確認が欠かせません。チェックすべき15のポイントを解説します。', img: 'feat-land', date: '2026.10.20', path: '/column/tochi-kounyu-chuiten/', tags: ['土地', 'チェックリスト'] },
      { id: 'renovation', cat: 'reform', title: '中古住宅を購入してリフォームする費用はいくら？購入費用と工事費の考え方', desc: '中古住宅の購入とリフォームをセットで検討する場合、予算配分の考え方が重要です。費用の考え方を解説します。', img: 'cat-life', date: '2026.10.18', path: '/column/chuuko-jutaku-reform-hiyou/', tags: ['リフォーム', '実例'] },
      { id: 'turf-cost', cat: 'turf', title: '人工芝の施工費用と価格相場', desc: '人工芝の施工費用は、材料費だけでなく下地処理費も含めて考える必要があります。費用の内訳を解説します。', img: 'thumb-turf', date: '2026.10.26', path: '/column/jinkoshiba-sekou-hiyou-souba/', tags: ['人工芝', '費用', 'DIY'] },
      { id: 'fence-guide', cat: 'exterior', title: '失敗しないフェンスの選び方｜種類・費用・おしゃれな施工例まで徹底解説', desc: '目隠し・メッシュ・ルーバーなど種類別の特徴と、目的別の選び方。', img: 'article-fence-hero', date: '2026.10.20', updated: '2026.10.28', path: '/exterior/fence/fence-guide/', tags: ['フェンス', '目隠しフェンス', 'フェンス 費用', '境界', 'DIY'] },
      { id: 'fence-types', cat: 'exterior', title: 'フェンスの種類と特徴を徹底比較', desc: 'フェンスには素材やデザインによってさまざまな種類があります。代表的な種類と特徴を比較して解説します。', img: 'thumb-fence', date: '2026.10.24', path: '/column/fence-shurui-hikaku/', tags: ['フェンス', '目隠し'] },
      { id: 'carport-price', cat: 'carport', title: 'カーポートの設置費用と価格相場', desc: 'カーポートの設置費用は、商品代だけでなく基礎工事費や施工費も含めて考える必要があります。内訳を解説します。', img: 'thumb-carport', date: '2026.10.23', path: '/column/carport-setti-hiyou-souba/', tags: ['カーポート', '比較'] },
      { id: 'land-value', cat: 'realestate', title: '土地の査定方法と相場の調べ方', desc: '公的な価格指標の見方と、査定前に準備すること。', img: 'thumb-land', date: '2026.10.21', path: '/realestate/land-value/', tags: ['土地', '査定'] },
      { id: 'wall-paint', cat: 'reform', title: '外壁塗装の費用相場と塗り替え時期は？見積もりで確認すべきポイント', desc: '外壁塗装の費用は、塗料の種類や外壁の状態によって変わります。塗り替え時期の目安と費用の考え方を解説します。', img: 'thumb-paint', date: '2026.10.20', path: '/column/gaiheki-tosou-hiyou-souba/', tags: ['外壁', 'リフォーム'] },
      { id: 'subsidy', cat: 'money', title: '外構工事に使える補助金・助成金の調べ方', desc: '自治体の制度の探し方と、申請で注意したいこと。', img: 'thumb-subsidy', date: '2026.10.18', path: '/money/subsidy/', tags: ['補助金', '外構'] },
      { id: 'garden-care', cat: 'life', title: '庭の手入れは季節ごとに何をする？春夏秋冬の年間メンテナンスカレンダー', desc: '庭の手入れは季節によってやるべき作業が異なります。春夏秋冬の年間スケジュールを解説します。', img: 'thumb-garden-care', date: '2026.10.17', path: '/column/niwa-teire-nenkan-calendar/', tags: ['メンテナンス', '庭'] },
      { id: 'delivery-box', cat: 'equipment', title: '戸建て用宅配ボックスの選び方！設置場所・サイズ・防犯面の注意点', desc: '戸建てに宅配ボックスを設置する際の選び方を解説。設置場所・サイズ・防犯面のポイントを紹介します。', img: 'thumb-deliverybox', date: '2026.10.16', path: '/column/takuhaibox-kodate-erabikata/', tags: ['宅配ボックス', '住宅設備'] },
      { id: 'deck-ideas', cat: 'deck', title: 'おしゃれなウッドデッキの実例10選', desc: '天然木・人工木の違いと、使い方別のデザイン実例。', img: 'cat-deck', date: '2026.10.12', path: '/exterior/deck/deck-ideas/', tags: ['ウッドデッキ', '実例'] },
      { id: 'blind-fence', cat: 'exterior', title: '目隠しフェンスの選び方', desc: '目隠しフェンスを選ぶ際は、高さと素材のバランスが重要です。選び方のポイントを解説します。', img: 'fence-privacy', date: '2026.10.10', path: '/column/mekakushi-fence-erabikata/', tags: ['フェンス', '目隠し'] },
      { id: 'fence-cost', cat: 'exterior', title: 'フェンスの設置費用はいくら？', desc: 'フェンスの設置費用は、素材や長さ、高さによって変動します。費用が決まる仕組みを解説します。', img: 'fence-wind', date: '2026.10.08', path: '/column/fence-setti-hiyou-ikkura/', tags: ['フェンス', '費用'] },
      { id: 'fence-diy', cat: 'exterior', title: 'DIYで目隠しフェンスを設置する方法', desc: '目隠しフェンスはDIYでも設置可能ですが、支柱の固定が強度を左右します。設置の手順と注意点を解説します。', img: 'fence-security', date: '2026.10.05', path: '/column/diy-mekakushi-fence-setti/', tags: ['フェンス', 'DIY'] },
      { id: 'exterior-design', cat: 'exterior', title: '外構デザインをおしゃれにするポイント', desc: '外構をおしゃれに見せるには、色・素材・全体の統一感がポイントになります。デザインの質を高める具体的な工夫を解説します。', img: 'hero-02', date: '2026.10.02', path: '/column/gaikou-design-oshare-point/', tags: ['外構', '実例'] }
    ],
    features: ['garden-guide', 'exterior-flow', 'land-check', 'renovation'],
    latest: ['turf-cost', 'fence-types', 'carport-price', 'land-value', 'wall-paint', 'subsidy', 'garden-care', 'delivery-box'],
    // Ranking: only show when real analytics are connected. `source` is printed under the list.
    ranking: {
      source: 'アクセス解析の集計（サンプルデータ）',
      periods: [
        { id: 'week', name: '週間', items: ['turf-cost', 'exterior-design', 'carport-price', 'exterior-flow', 'land-check'] },
        { id: 'month', name: '月間', items: ['fence-guide', 'turf-cost', 'deck-ideas', 'carport-price', 'land-value'] },
        { id: 'year', name: '年間', items: ['turf-cost', 'fence-guide', 'garden-guide', 'subsidy', 'wall-paint'] }
      ]
    },
    editorsPick: ['garden-guide', 'fence-guide', 'turf-cost', 'subsidy'],
    heroSlides: [
      { img: 'hero-01', alt: '夕暮れのウッドデッキと人工芝の庭', article: 'garden-guide' },
      { img: 'hero-02', alt: '植栽と照明に彩られた住宅のエントランス', article: 'exterior-flow' },
      { img: 'hero-03', alt: '夕暮れに照明が灯るモダンな住宅とビルトインカーポート', article: 'carport-price' },
      { img: 'hero-04', alt: '黒い横格子フェンスと人工芝の庭', article: 'fence-guide' }
    ],
    purposes: [
      { id: 'cost', icon: 'coins', name: '費用相場を知りたい', sub: '工事・商品の価格目安', path: '/purpose/cost/' },
      { id: 'design', icon: 'image', name: 'デザインの実例を見たい', sub: '施工例・コーディネート', path: '/purpose/examples/' },
      { id: 'items', icon: 'cart', name: 'おすすめ商品を探したい', sub: 'DIY用品・資材の比較', path: '/purpose/products/' },
      { id: 'pro', icon: 'user', name: '業者を探したい', sub: '施工会社の比較・選び方', path: '/purpose/contractors/' },
      { id: 'subsidy', icon: 'doc', name: '補助金を調べたい', sub: '自治体の制度・申請', path: '/purpose/subsidy/' }
    ],
    // Pillar → cluster structure (人工芝 is the first specialty)
    turfGuide: {
      title: '人工芝の「知りたい」が、<br>ぜんぶわかる。',
      path: '/garden/turf/',
      text: '芝丈や密度の違いから、下地づくり、DIYと業者施工の費用比較、ペットや子どもとの使い方まで。テーマ別に体系立てて解説しています。',
      chapters: [
        { no: '01', name: '基礎知識・種類', desc: 'パイル形状・素材・裏面構造', path: '/garden/turf/basics/' },
        { no: '02', name: '性能・品質', desc: '水はけ・熱・肌触り・耐久性', path: '/garden/turf/quality/' },
        { no: '03', name: '下地づくり・施工方法', desc: '整地・転圧・防草シート', path: '/garden/turf/install/' },
        { no: '04', name: 'DIY・必要な道具', desc: '道具リストと手順', path: '/column/jinkoshiba-diy-shikikata/' },
        { no: '05', name: '費用・業者施工', desc: '面積別の費用の考え方', path: '/column/jinkoshiba-sekou-hiyou-souba/' },
        { no: '06', name: '用途別の選び方', desc: '犬・子ども・ベランダ・庭', path: '/garden/turf/use/' },
        { no: '07', name: 'メンテナンス・トラブル', desc: '掃除・補修・におい対策', path: '/garden/turf/care/' },
        { no: '08', name: '商品・メーカー比較', desc: '比較基準と選び方', path: '/column/jinkoshiba-shurui-erabikata/' },
        { no: '09', name: '施工会社の選び方', desc: '見積もりで確認すること', path: '/garden/turf/contractors/' }
      ]
    },
    fenceSeries: {
      name: 'フェンス完全ガイド', path: '/exterior/fence/',
      items: [
        { id: 'fence-guide', name: 'フェンスの選び方（総合ガイド）' },
        { id: 'fence-types', name: 'フェンスの種類と特徴' },
        { id: 'blind-fence', name: '目隠しフェンスのメリット・デメリット' },
        { id: 'fence-cost', name: 'フェンスの費用相場と工事の流れ' },
        { id: 'fence-diy', name: 'フェンスはDIYできる？' },
        { id: null, name: 'フェンスの高さの決め方', soon: true },
        { id: null, name: '境界フェンスとお隣トラブルの防ぎ方', soon: true }
      ]
    },
    footer: {
      about: 'SOTORINO（ソトリノ）は、庭・外構・住まい・土地まで、家まわりの「知りたい」を集めた情報メディアです。費用や選び方を、根拠と条件を添えてわかりやすくお届けします。',
      guides: [
        { name: '外構・庭づくりコラム', path: '/column/' },
        { name: '人工芝ガイド', path: '/garden/turf/' },
        { name: 'フェンス完全ガイド', path: '/exterior/fence/' },
        { name: 'はじめての外構工事', path: '/exterior/beginners/' },
        { name: '補助金の調べ方', path: '/money/subsidy/' },
        { name: '動画で見る', path: '/video/' },
        { name: '施工例ギャラリー', path: '/cases/' },
        { name: '読者の質問箱', path: '/qa/turf/' },
        { name: '用語集', path: '/glossary/' }
      ],
      site: [
        { name: '運営者情報', path: '/about/' },
        { name: '編集ポリシー', path: '/editorial-policy/' },
        { name: 'お問い合わせ', path: '/contact/' },
        { name: 'プライバシーポリシー', path: '/privacy/' },
        { name: '広告・アフィリエイトについて', path: '/ads-policy/' },
        { name: '免責事項', path: '/disclaimer/' }
      ]
    }
  };
  function A(id) { var l = S.data.articles; for (var i = 0; i < l.length; i++) if (l[i].id === id) return l[i]; return null; }
  S.article = A;

  /* ================= basics ================= */
  S.CategoryLabel = function (p) {
    var cat = typeof p === 'string' ? p : p.cat;
    var tone = TONE[cat] || 'outdoor';
    return '<span class="' + cx('st-label', tone !== 'outdoor' && 'st-label--' + tone) + '">' + esc(S.data.catName[cat] || cat) + '</span>';
  };
  S.PRLabel = function (p) { p = p || {}; return '<span class="' + cx('st-pr', p.dark && 'st-pr--dark') + '" title="広告・アフィリエイトを含みます">' + esc(p.text || 'PR') + '</span>'; };
  S.Date = function (p) {
    var s = '';
    if (p.date) s += '<span class="st-date">' + icon('clock') + '<time datetime="' + esc(p.date.replace(/\./g, '-')) + '">' + esc(p.date) + '</time></span>';
    if (p.updated) s += '<span class="st-date">' + icon('update') + '<span class="st-sr">更新日</span><time datetime="' + esc(p.updated.replace(/\./g, '-')) + '">' + esc(p.updated) + '</time></span>';
    return s;
  };
  S.Button = function (p) {
    var tag = p.href ? 'a' : 'button';
    return '<' + tag + attr({ class: cx('st-btn', 'st-btn--' + (p.variant || 'primary'), p.size === 'sm' && 'st-btn--sm', p.block && 'st-btn--block'), href: p.href ? href(p.href) : null, type: p.href ? null : 'button', rel: p.rel }) + '>' + (p.iconLeft ? icon(p.iconLeft) : '') + '<span>' + esc(p.label) + '</span>' + (p.arrow !== false ? icon('arrow') : '') + '</' + tag + '>';
  };
  S.More = function (p) { return '<a class="st-more" href="' + esc(href(p.href)) + '">' + esc(p.label || 'もっと見る') + icon('arrow') + (p.sr ? '<span class="st-sr">' + esc(p.sr) + '</span>' : '') + '</a>'; };
  S.Logo = function (p) {
    p = p || {};
    var inner = (S.config.logoSrc && !p.text) ? '<img src="' + esc(S.config.logoSrc) + '" alt="SOTORINO（ソトリノ）">' : '<span aria-hidden="true">SOTORINO</span><span class="st-sr">SOTORINO（ソトリノ）トップへ</span>';
    return '<a class="st-logo" href="' + esc(href('/')) + '"' + (p.current ? ' aria-current="page"' : '') + '>' + inner + '</a>';
  };
  S.TagList = function (p) { return '<ul class="st-tags" aria-label="タグ">' + p.tags.map(function (t) { return '<li><a class="st-tag" href="' + esc(href('/tag/' + encodeURIComponent(t) + '/')) + '">#' + esc(t) + '</a></li>'; }).join('') + '</ul>'; };

  /* ================= search ================= */
  S.Search = function (p) {
    p = p || {};
    var id = p.id || ('st-q-' + Math.random().toString(36).slice(2, 7));
    return '<form class="st-search" role="search" action="' + esc(href('/search/')) + '" data-st-search>' +
      '<label class="st-sr" for="' + id + '">サイト内の記事を検索</label>' +
      '<div class="st-search__field"><input id="' + id + '" name="q" type="search" autocomplete="off" placeholder="' + esc(p.placeholder || 'キーワードで記事を検索…') + '" aria-controls="' + id + '-panel" aria-expanded="false">' +
      '<button class="st-search__submit" type="submit" aria-label="検索する">' + icon('search') + '</button></div>' +
      '<div class="st-search__panel" id="' + id + '-panel" hidden></div></form>';
  };

  /* ================= header / drawer / footer ================= */
  S.Header = function (p) {
    p = p || {};
    var nav = S.data.nav.map(function (n) { return '<li><a href="' + esc(href(n.path)) + '"' + (p.active === n.id ? ' aria-current="page"' : '') + '>' + esc(n.name) + '</a></li>'; }).join('');
    return '<a class="st-skip" href="#main">本文へスキップ</a><header class="st-header" data-st-header><div class="st-container"><div class="st-header__top">' + S.Logo({ current: p.active === 'home' }) +
      S.Search({ id: 'st-q-head' }) +
      '<div class="st-header__actions">' +
      '<button class="st-iconbtn st-iconbtn--search" type="button" aria-expanded="false" data-st-search-toggle>' + icon('search') + '<span class="st-sr">検索を開く</span></button>' +
      '<div class="st-actions-wrap"><button class="st-iconbtn" type="button" aria-expanded="false" aria-controls="st-favpop" data-st-favbtn>' + icon('heart') + '<span class="st-iconbtn__label">お気に入り</span><span class="st-iconbtn__badge" data-st-favcount hidden>0</span></button>' +
      '<div class="st-pop" id="st-favpop" hidden data-st-favpop></div></div>' +
      '<button class="st-iconbtn" type="button" aria-expanded="false" aria-controls="st-drawer" data-st-drawer-open>' + icon('menu') + '<span class="st-iconbtn__label">メニュー</span><span class="st-sr">メニューを開く</span></button>' +
      '</div></div><nav class="st-nav" aria-label="カテゴリ"><ul>' + nav + '</ul></nav></div></header>' + S.Drawer();
  };
  S.Drawer = function () {
    var cats = S.data.categories.map(function (c) { return '<li><a href="' + esc(href(c.path)) + '">' + esc(c.name) + icon('chevR') + '</a></li>'; }).join('');
    var pur = S.data.purposes.map(function (x) { return '<li><a href="' + esc(href(x.path)) + '">' + icon(x.icon) + esc(x.name) + '</a></li>'; }).join('');
    return '<div class="st-drawer" id="st-drawer" hidden data-st-drawer><div class="st-drawer__scrim" data-st-drawer-close></div>' +
      '<div class="st-drawer__panel" role="dialog" aria-modal="true" aria-label="メニュー"><div class="st-drawer__head">' + S.Logo() +
      '<button class="st-iconbtn" type="button" data-st-drawer-close>' + icon('close') + '<span class="st-iconbtn__label">閉じる</span></button></div>' +
      S.Search({ id: 'st-q-drawer', placeholder: '例：人工芝 費用' }) +
      '<p class="st-drawer__title">CATEGORY</p><ul class="st-drawer__list"><li><a href="' + esc(href('/new/')) + '">新着記事' + icon('chevR') + '</a></li>' + cats + '</ul>' +
      '<p class="st-drawer__title">SEARCH BY PURPOSE</p><ul class="st-drawer__purpose">' + pur + '</ul>' +
      '<p class="st-drawer__title">GUIDE</p><ul class="st-drawer__list">' + S.data.footer.guides.map(function (g) { return '<li><a href="' + esc(href(g.path)) + '">' + esc(g.name) + icon('chevR') + '</a></li>'; }).join('') + '</ul>' +
      '</div></div>';
  };
  S.Footer = function () {
    var f = S.data.footer;
    function list(t, items) { return '<div><h2>' + t + '</h2><ul>' + items.map(function (i) { return '<li><a href="' + esc(href(i.path)) + '">' + esc(i.name) + '</a></li>'; }).join('') + '</ul></div>'; }
    return '<footer class="st-footer"><div class="st-container"><div class="st-footer__grid"><div class="st-footer__brand">' + S.Logo({ text: true }) + '<p class="st-footer__about">' + esc(f.about) + '</p></div>' +
      list('CATEGORY', S.data.categories).replace('<ul>', '<ul class="st-footer__cols">') + list('GUIDE', f.guides) + list('ABOUT', f.site) +
      '</div><div class="st-footer__bottom"><span>' + (S.config.affiliate ? '当サイトはアフィリエイトプログラムを利用しています。' : '') + '広告を含むコンテンツには「PR」と表示しています。</span><span>© SOTORINO</span></div></div></footer>';
  };

  /* ================= top page parts ================= */
  S.HeroSlider = function (p) {
    p = p || {};
    var slides = p.slides || S.data.heroSlides;
    var s = slides.map(function (sl, i) {
      return '<div class="' + cx('st-hero__slide', i === 0 && 'is-active') + '" data-st-slide' + (i ? ' aria-hidden="true"' : '') + '>' + img(sl.img, sl.alt, { eager: i === 0 }) + '</div>';
    }).join('');
        var dots = slides.map(function (sl, i) { return '<button class="st-hero__dot" type="button" data-st-dot="' + i + '" aria-label="' + (i + 1) + '枚目を表示"' + (i === 0 ? ' aria-current="true"' : '') + '></button>'; }).join('');
    return '<section class="st-hero" aria-roledescription="カルーセル" aria-label="ピックアップ" data-st-slider>' + s + '<div class="st-hero__shade"></div>' +
      '<div class="st-container st-hero__inner"><h1 class="st-hero__title">' + (p.title || '理想の<br>暮らしは、<br>外まわりから。') + '</h1>' +
      '<p class="st-hero__lead">' + (p.lead || '庭・外構・住まい・土地まで<br>家まわりの“知りたい”が見つかる<br>情報メディア「SOTORINO」') + '</p>' +
      S.Search({ id: 'st-q-hero', placeholder: '知りたいことを検索…（例：人工芝、カーポート、外構費用）' }) + (S.HeroKeywords ? S.HeroKeywords() : '') + '</div>' +
      '<button class="st-hero__arrow st-hero__arrow--prev" type="button" data-st-prev aria-label="前のスライド">' + icon('chevL') + '</button>' +
      '<button class="st-hero__arrow st-hero__arrow--next" type="button" data-st-next aria-label="次のスライド">' + icon('chevR') + '</button>' +
      '<div class="st-hero__ctrl"><div class="st-hero__dots">' + dots + '</div><span class="st-hero__count" aria-live="polite" data-st-count>01 / ' + ('0' + slides.length).slice(-2) + '</span>' +
      '<button class="st-hero__pause" type="button" data-st-pause aria-label="自動再生を停止">' + icon('pause') + '</button></div></section>';
  };
  S.CategoryTiles = function (p) {
    var cats = (p && p.categories) || S.data.categories;
    return '<nav aria-label="カテゴリから探す"><ul class="st-cats">' + cats.map(function (c) {
      return '<li><a class="st-cat" href="' + esc(href(c.path)) + '">' + media(c.img, '', '43') + '<span class="st-cat__name">' + esc(c.name) + '</span><span class="st-cat__sub">' + esc(c.sub) + '</span></a></li>';
    }).join('') + '</ul></nav>';
  };
  S.SectionHeading = function (p) {
    var tag = p.level || 'h2';
    return '<div class="' + cx('st-sechead', p.light && 'st-sechead--light') + '"><' + tag + ' class="st-sechead__title"' + (p.id ? ' id="' + esc(p.id) + '"' : '') + '>' + esc(p.title) + '</' + tag + '>' + (p.en ? '<span class="st-sechead__en" aria-hidden="true">' + esc(p.en) + '</span>' : '') + (p.more ? S.More({ href: p.more, sr: '：' + p.title }) : '') + '</div>';
  };
  S.ArticleCard = function (p) {
    var a = typeof p.article === 'string' ? A(p.article) : p.article;
    var v = p.variant || 'grid', h = p.headingLevel || 'h3';
    var title = '<' + h + ' class="st-card__title">' + esc(a.title).replace('｜', '<br>') + '</' + h + '>';
    if (v === 'feature') return '<a class="st-card st-card--feature" href="' + esc(href(a.path)) + '">' + media(a.img, '', 'hero') + '<div class="st-card__body">' + S.CategoryLabel(a.cat) + title + '<p class="st-card__desc">' + esc(a.desc) + '</p>' + S.Date(a) + '</div></a>';
    if (v === 'row') return '<a class="st-card st-card--row" href="' + esc(href(a.path)) + '"><span class="st-media st-r-row">' + img(a.img, '') + S.CategoryLabel(a.cat) + '</span><div>' + title + '<div class="st-card__date">' + S.Date(a) + '</div></div></a>';
    if (v === 'mini') return '<a class="st-card st-card--mini" href="' + esc(href(a.path)) + '">' + media(a.img, '', '43') + title + '</a>';
    return '<a class="st-card" href="' + esc(href(a.path)) + '">' + media(a.img, '', 'card') + '<div class="st-card__meta">' + S.CategoryLabel(a.cat) + '</div>' + title + (p.desc ? '<p class="st-card__desc">' + esc(a.desc) + '</p>' : '') + '<div class="st-card__date">' + S.Date({ date: a.date }) + '</div></a>';
  };
  /* PRバナー：S.config.prReady が false のあいだは、タップすると「準備中」ページへ（送客・アフィリエイトの準備が整ったら true に） */
  S.CTABanner = function (p) {
    p = p || {};
    var pr = p.sponsored !== false, to = pr && !S.config.prReady ? '/preparing/' : (p.href || '/contractors/estimate/');
    return '<a class="st-cta" href="' + esc(href(to)) + '"' + (pr && S.config.prReady ? ' rel="sponsored"' : '') + '>' + media(p.img || 'hero-04', '', '43') + (p.sponsored !== false ? '<span class="st-cta__pr">' + S.PRLabel({ dark: true }) + '</span>' : '') +
      '<span class="st-cta__body"><span class="st-cta__title">' + (p.title || '理想の外構を<br>プロとつくる') + '</span><span class="st-cta__text">' + esc(p.text || '外構工事の無料相談・一括見積もり') + '</span>' +
      '<span class="st-btn st-btn--accent st-btn--sm">' + esc(p.cta || '詳しく見る') + icon('arrow') + '</span></span></a>';
  };
  S.CatalogCard = function (p) {
    p = p || {};
    return '<div class="st-catalog"><div><p class="st-catalog__title">' + (p.title || 'カタログ請求で<br>理想の庭を見つける') + '</p>' + S.Button({ href: p.href || '/catalog/', label: p.cta || 'カタログをみる', variant: 'outline', size: 'sm' }) + '</div>' + media(p.img || 'cat-garden', '', '11') + '</div>';
  };
  S.FeatureGrid = function (p) {
    p = p || {};
    var ids = p.items || S.data.features;
    return '<div class="st-feature"><div class="st-feature__main">' + (p.heading ? S.SectionHeading(p.heading) : '') + '<div class="st-feature__body"><div>' + S.ArticleCard({ article: ids[0], variant: 'feature' }) + '</div>' +
      '<ul class="st-feature__list">' + ids.slice(1, 4).map(function (id) { return '<li>' + S.ArticleCard({ article: id, variant: 'row' }) + '</li>'; }).join('') + '</ul></div></div>' +
      '<aside class="st-feature__side" aria-label="外構の相談・資料請求・ガイド">' + S.CTABanner() + S.CatalogCard() + (p.guide ? S.GuideCard() : '') + '</aside></div>';
  };
  S.Ranking = function (p) {
    p = p || {};
    var r = p.ranking || S.data.ranking;
    var uid = p.id || 'rk';
    /* アクセス解析の実データが入るまで（S.config.rankingLive が false のあいだ）は、順位を付けず「編集部のおすすめ」として表示する */
    if (p.mode === 'editor' || !r || !S.config.rankingLive) {
      var ids = p.items || (r && r.periods && r.periods[0] ? r.periods[0].items.slice(0, p.limit || 5) : S.data.editorsPick);
      return '<section class="st-box" aria-labelledby="' + uid + '-t"><h2 class="st-box__title" id="' + uid + '-t">' + icon('leaf') + '編集部のおすすめ</h2><ul class="st-rank">' +
        ids.map(function (id) { var a = A(id); return '<li><a href="' + esc(href(a.path)) + '" style="grid-template-columns:64px 1fr">' + media(a.img, '', '11') + '<span class="st-rank__title">' + esc(a.title) + '</span></a></li>'; }).join('') + '</ul></section>';
    }
    var tabs = r.periods.length > 1 ? '<div class="st-tabs" role="tablist" aria-label="集計期間">' + r.periods.map(function (pr, i) { return '<button type="button" role="tab" id="' + uid + '-tab-' + pr.id + '" aria-controls="' + uid + '-p-' + pr.id + '" aria-selected="' + (i === 0) + '" tabindex="' + (i === 0 ? 0 : -1) + '">' + esc(pr.name) + '</button>'; }).join('') + '</div>' : '';
    var panels = r.periods.map(function (pr, i) {
      return '<ol role="tabpanel" id="' + uid + '-p-' + pr.id + '" aria-labelledby="' + uid + '-tab-' + pr.id + '"' + (i ? ' hidden' : '') + '>' + pr.items.slice(0, p.limit || 5).map(function (id, n) {
        var a = A(id);
        return '<li><a href="' + esc(href(a.path)) + '"><span class="' + cx('st-rank__no', n < 3 && 'st-rank__no--' + (n + 1)) + '"><span class="st-sr">' + (n + 1) + '位</span><span aria-hidden="true">' + (n + 1) + '</span></span>' + media(a.img, '', '11') + '<span class="st-rank__title">' + esc(a.title).replace('｜', '<br>') + '</span></a></li>';
      }).join('') + '</ol>';
    }).join('');
    return '<section class="st-box st-rank" aria-labelledby="' + uid + '-t" data-st-tabs><h2 class="st-box__title" id="' + uid + '-t">' + esc(p.title || '人気記事ランキング') + '</h2>' + tabs + panels + (r.source ? '<p class="st-box__note">集計：' + esc(r.source) + '</p>' : '') + '</section>';
  };
  S.GuideCard = function (p) {
    p = p || {};
    return '<a class="st-guide" href="' + esc(href(p.href || '/exterior/beginners/')) + '"><span class="st-guide__icon">' + icon('sprout') + '</span><span class="st-guide__title">' + (p.title || '初めての外構工事<br>まるわかりガイド') + '</span><span class="st-guide__go">' + icon('arrow') + '</span><span class="st-guide__text">' + esc(p.text || '基礎知識から費用、業者選びまで初心者向けにやさしく解説します。') + '</span></a>';
  };
  S.LatestGrid = function (p) {
    p = p || {};
    return '<ul class="' + cx('st-grid', p.cols === 3 && 'st-grid--3') + '">' + (p.items || S.data.latest).map(function (id) { return '<li>' + S.ArticleCard({ article: id, desc: p.desc }) + '</li>'; }).join('') + '</ul>';
  };
  S.PillarGuide = function (p) {
    var g = (p && p.guide) || S.data.turfGuide;
    return '<div class="st-pillar"><div class="st-pillar__lead"><span class="st-sechead__en">ARTIFICIAL TURF GUIDE</span><h2 class="st-pillar__title" id="pillar-t">' + g.title + '</h2><p class="st-pillar__text">' + esc(g.text) + '</p>' +
      S.Button({ href: g.path, label: '人工芝ガイドを見る' }) + '</div>' +
      '<ol class="st-chapters" aria-labelledby="pillar-t">' + g.chapters.map(function (c) { return '<li><a class="st-chapter" href="' + esc(href(c.path)) + '"><span class="st-chapter__no">' + c.no + '</span><span><span class="st-chapter__title">' + esc(c.name) + '</span><span class="st-chapter__desc">' + esc(c.desc) + '</span></span>' + icon('chevR') + '</a></li>'; }).join('') + '</ol></div>';
  };
  S.PurposeNav = function (p) {
    p = p || {};
    return '<section class="st-purpose" aria-labelledby="purpose-t">' + img(p.img || 'purpose-bg', '') + '<div class="st-container">' + S.SectionHeading({ title: '目的から探す', en: 'Search by purpose', light: true, id: 'purpose-t' }) +
      '<ul class="st-purpose__list">' + S.data.purposes.map(function (x) { return '<li><a class="st-purpose__item" href="' + esc(href(x.path)) + '">' + icon(x.icon) + '<span>' + esc(x.name) + '</span></a></li>'; }).join('') + '</ul></div></section>';
  };

  /* ================= article parts ================= */
  S.Breadcrumb = function (p) {
    var items = p.items, last = items.length - 1;
    return '<nav class="st-bc" aria-label="パンくずリスト"><div class="st-container"><ol itemscope itemtype="https://schema.org/BreadcrumbList">' + items.map(function (it, i) {
      var inner = i === last ? '<span aria-current="page" itemprop="name">' + esc(it.name) + '</span>' : '<a itemprop="item" href="' + esc(href(it.path)) + '">' + (i === 0 ? icon('home') : '') + '<span itemprop="name">' + esc(it.name) + '</span></a>';
      return '<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">' + inner + '<meta itemprop="position" content="' + (i + 1) + '"></li>';
    }).join('') + '</ol></div></nav>';
  };
  S.ShareBar = function (p) {
    var url = encodeURIComponent(p.url || 'https://sotorino.jp' + (p.path || '/')), t = encodeURIComponent(p.title || '');
    return '<div class="st-share"><div class="st-share__list"><span class="st-share__label">シェアする</span>' +
      '<a class="st-share__btn" target="_blank" rel="noopener" href="https://x.com/intent/post?url=' + url + '&text=' + t + '">X<span class="st-sr">でシェア（新しいタブ）</span></a>' +
      '<a class="st-share__btn" target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u=' + url + '">Facebook<span class="st-sr">でシェア（新しいタブ）</span></a>' +
      '<a class="st-share__btn" target="_blank" rel="noopener" href="https://social-plugins.line.me/lineit/share?url=' + url + '">LINE<span class="st-sr">で送る（新しいタブ）</span></a>' +
      '<button class="st-share__btn" type="button" data-st-copy="' + esc(decodeURIComponent(url)) + '">' + icon('link') + '<span>リンクをコピー</span></button>' +
      '<span class="st-live" role="status" data-st-copy-status></span></div>' +
      '<button class="st-share__btn st-fav" type="button" aria-pressed="false" data-st-fav="' + esc(p.id) + '">' + icon('heart') + '<span data-st-fav-text>お気に入りに追加</span></button></div>';
  };
  S.ArticleHeader = function (p) {
    var a = typeof p.article === 'string' ? A(p.article) : p.article;
    return '<header class="st-ahead"><div class="st-ahead__meta">' + S.CategoryLabel(a.cat) + S.Date({ date: a.date }) + (a.updated ? '<span class="st-date">' + icon('update') + '更新 <time datetime="' + a.updated.replace(/\./g, '-') + '">' + a.updated + '</time></span>' : '') + (p.pr ? S.PRLabel() : '') + '</div>' +
      '<h1 class="st-ahead__title">' + esc(a.title) + '</h1>' + (p.lead ? '<p class="st-ahead__lead">' + esc(p.lead) + '</p>' : '') +
      '<p class="st-ahead__byline">' + icon('user') + '<span>執筆：<a href="' + esc(href('/about/editors/')) + '">SOTORINO編集部</a></span></p>' +
      '<figure class="st-ahead__hero">' + media(a.img, p.heroAlt || '', 'hero') + (p.caption ? '<figcaption>' + esc(p.caption) + '</figcaption>' : '') + '</figure>' + S.ShareBar({ id: a.id, title: a.title, path: a.path }) + '</header>';
  };
  S.SummaryBox = function (p) { return '<section class="st-summary" aria-labelledby="sum-t"><h2 class="st-summary__title" id="sum-t">' + esc(p.title || 'この記事でわかること') + '</h2><ul>' + p.items.map(function (t) { return '<li>' + icon('check') + '<span>' + esc(t) + '</span></li>'; }).join('') + '</ul></section>'; };
  S.TableOfContents = function (p) {
    var items = p.items;
    return '<nav class="st-toc" aria-labelledby="toc-t" data-st-toc><div class="st-toc__head"><h2 class="st-toc__title" id="toc-t">目次</h2><button class="st-toc__toggle" type="button" aria-expanded="true" aria-controls="toc-list"><span data-st-toc-label>閉じる</span>' + icon('chevD') + '</button></div>' +
      '<ol id="toc-list">' + items.map(function (it, i) { return '<li><a href="#' + esc(it.id) + '"><span class="st-toc__no">' + ('0' + (i + 1)).slice(-2) + '</span><span>' + esc(it.text) + '</span></a>' + (it.children && it.children.length ? '<ol>' + it.children.map(function (c) { return '<li><a href="#' + esc(c.id) + '">' + esc(c.text) + '</a></li>'; }).join('') + '</ol>' : '') + '</li>'; }).join('') + '</ol></nav>';
  };
  S.IconFeatureGrid = function (p) { return '<ul class="st-icongrid">' + p.items.map(function (it) { return '<li class="st-icongrid__item">' + media(it.img, it.alt || '', '32') + '<h4 class="st-icongrid__head"><span class="st-icongrid__icon">' + icon(it.icon) + '</span>' + esc(it.title) + '</h4><p class="st-icongrid__desc">' + esc(it.desc) + '</p></li>'; }).join('') + '</ul>'; };
  S.TypeGrid = function (p) {
    return '<ul class="st-typegrid">' + p.items.map(function (it) {
      var body = media(it.img, it.alt || '', '52') + '<h4 class="st-typegrid__name">' + esc(it.name) + (it.path ? icon('chevR') : '') + '</h4><p class="st-typegrid__desc">' + esc(it.desc) + '</p>';
      return '<li>' + (it.path ? '<a href="' + esc(href(it.path)) + '">' + body + '</a>' : body) + '</li>';
    }).join('') + '</ul>';
  };
  S.CompareTable = function (p) {
    return '<div class="st-table"><p class="st-table__hint" aria-hidden="true">← 横にスクロールできます →</p><div class="st-table__scroll" tabindex="0" role="region" aria-label="' + esc(p.caption) + '"><table>' + (p.caption ? '<caption class="st-sr">' + esc(p.caption) + '</caption>' : '') +
      '<thead><tr>' + p.head.map(function (h) { return '<th scope="col">' + esc(h) + '</th>'; }).join('') + '</tr></thead><tbody>' +
      p.rows.map(function (r) { return '<tr' + (r.pick ? ' class="is-pick"' : '') + '><th scope="row">' + esc(r.cells[0]) + (r.pick ? '<br><span class="st-label" style="margin-top:4px">おすすめ</span>' : '') + '</th>' + r.cells.slice(1).map(function (c) { return '<td>' + String(c).replace(/^([◎○△×])\s?/, '<span class="st-table__mark">$1</span>') + '</td>'; }).join('') + '</tr>'; }).join('') +
      '</tbody></table></div>' + (p.note ? '<p class="st-table__note">' + p.note + '</p>' : '') + '</div>';
  };
  S.StatSummary = function (p) { return '<div class="st-stats">' + p.items.map(function (s) { return '<div class="st-stat"><p class="st-stat__label">' + esc(s.label) + '</p><p class="st-stat__value">' + esc(s.value) + (s.unit ? '<small>' + esc(s.unit) + '</small>' : '') + '</p>' + (s.note ? '<p class="st-stat__note">' + esc(s.note) + '</p>' : '') + '</div>'; }).join('') + '</div>'; };
  S.NoteBox = function (p) {
    var k = p.kind || 'point', ic = { point: 'bulb', caution: 'alert', info: 'info' }[k], ttl = p.title || { point: 'ポイント', caution: '注意', info: '補足' }[k];
    return '<aside class="' + cx('st-note', k !== 'point' && 'st-note--' + k) + '" aria-label="' + esc(ttl) + '"><p class="st-note__head">' + icon(ic) + esc(ttl) + '</p>' + (p.items ? '<ul class="st-ul">' + p.items.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>' : '<p>' + p.html + '</p>') + '</aside>';
  };
  S.Steps = function (p) { return '<ol class="st-steps">' + p.items.map(function (s, i) { return '<li><span class="st-steps__no" aria-hidden="true">' + (i + 1) + '</span><div><h4 class="st-steps__title"><span class="st-sr">ステップ' + (i + 1) + '：</span>' + esc(s.title) + (s.time ? '<span class="st-steps__time">' + esc(s.time) + '</span>' : '') + '</h4><p class="st-steps__desc">' + esc(s.desc) + '</p></div></li>'; }).join('') + '</ol>'; };
  S.ProsCons = function (p) {
    function col(k, t, items) { return '<div class="st-pc__col st-pc__col--' + k + '"><h4 class="st-pc__head">' + icon(k === 'pro' ? 'plus' : 'minus') + esc(t) + '</h4><ul>' + items.map(function (x) { return '<li>' + icon(k === 'pro' ? 'check' : 'minus') + '<span>' + esc(x) + '</span></li>'; }).join('') + '</ul></div>'; }
    return '<div class="st-pc">' + col('pro', p.proTitle || 'メリット', p.pros) + col('con', p.conTitle || 'デメリット', p.cons) + '</div>';
  };
  S.Checklist = function (p) {
    return '<div class="st-check" data-st-check><p class="st-check__head"><span>' + esc(p.title || 'チェックリスト') + '</span><span class="st-check__count" aria-live="polite" data-st-check-count>0 / ' + p.items.length + ' 確認済み</span></p><ul>' +
      p.items.map(function (it) { return '<li><label><input type="checkbox"><span>' + esc(it.text) + (it.sub ? '<small>' + esc(it.sub) + '</small>' : '') + '</span></label></li>'; }).join('') + '</ul></div>';
  };
  S.FAQ = function (p) { return '<div class="st-faq">' + p.items.map(function (q) { return '<details><summary><span class="st-faq__q" aria-hidden="true">Q</span><span>' + esc(q.q) + '</span>' + icon('chevD') + '</summary><div class="st-faq__body"><span class="st-faq__a" aria-hidden="true">A</span><p>' + q.a + '</p></div></details>'; }).join('') + '</div>'; };
  S.InlineRelated = function (p) {
    var a = typeof p.article === 'string' ? A(p.article) : p.article;
    return '<a class="st-also" href="' + esc(href(a.path)) + '"><span class="st-also__tag">' + icon('book') + esc(p.label || 'あわせて読みたい') + '</span>' + media(a.img, '', '32') + '<span><span class="st-also__title">' + esc(a.title) + '</span><span class="st-also__desc">' + esc(a.desc) + '</span></span>' + icon('chevR') + '</a>';
  };
  S.Gallery = function (p) { return '<div class="st-gallery">' + p.items.map(function (g) { return '<figure>' + media(g.img, g.alt || '', '32') + '<figcaption><p class="st-gallery__title">' + g.title + '</p><p class="st-gallery__spec">' + g.spec.map(function (s) { return '<span>' + esc(s) + '</span>'; }).join('') + '</p></figcaption></figure>'; }).join('') + '</div>'; };
  S.NextSteps = function (p) {
    var items = p.items || [
      { step: 'STEP 1', icon: 'coins', title: '費用をくわしく知る', desc: '本体・基礎・工事費の内訳と見積もりの見方。', path: '/column/fence-setti-hiyou-ikkura/', go: '費用相場を見る' },
      { step: 'STEP 2', icon: 'cart', title: 'DIYで設置したい', desc: '必要な道具と、DIY向きのフェンス商品を比較。', path: '/column/diy-mekakushi-fence-setti/', go: '商品と道具を見る' },
      { step: 'STEP 3', icon: 'user', title: 'プロに相談したい', desc: '施工会社の比較ポイントと無料見積もりの使い方。', path: '/purpose/contractors/', go: '業者の選び方を見る' }
    ];
    return '<ul class="st-next">' + items.map(function (n) { return '<li><a href="' + esc(href(n.path)) + '"><span class="st-next__step">' + esc(n.step) + '</span><span class="st-next__title">' + icon(n.icon) + esc(n.title) + '</span><span class="st-next__desc">' + esc(n.desc) + '</span><span class="st-next__go">' + esc(n.go) + icon('arrow') + '</span></a></li>'; }).join('') + '</ul>';
  };
  S.ProductCards = function (p) {
    return '<section class="st-products" aria-labelledby="prod-t"><div class="st-products__head"><h3 class="st-products__title" id="prod-t">' + esc(p.title || 'DIYで設置する方に：おすすめの商品') + '</h3>' + S.PRLabel() + '</div>' +
      '<p class="st-products__disc">このセクションにはアフィリエイトリンクを含みます。選定基準：' + esc(p.criteria || '編集部の比較基準（素材・耐候性・施工性・入手性）') + '。価格は取得日時点の参考価格です。</p>' +
      '<ul class="st-products__grid">' + p.items.map(function (it) {
        return '<li class="st-product">' + media(it.img, it.name, '43') + '<p class="st-product__name">' + esc(it.name) + '</p><p class="st-product__for">' + esc(it.forWhom) + '</p>' +
          '<dl class="st-product__spec">' + it.spec.map(function (s) { return '<dt>' + esc(s[0]) + '</dt><dd>' + esc(s[1]) + '</dd>'; }).join('') + '</dl>' +
          '<p class="st-product__price">' + esc(it.price) + '<small>' + esc(it.priceNote || '取得日：YYYY.MM.DD／最新価格は販売ページでご確認ください') + '</small></p>' +
          '<div class="st-product__shops">' + it.shops.map(function (s, i) { return '<a class="' + cx('st-btn st-btn--sm st-btn--block', i ? 'st-btn--outline' : 'st-btn--primary') + '" href="' + esc(s.href || '#') + '" rel="sponsored noopener" target="_blank">' + esc(s.name) + 'で見る' + icon('arrow') + '<span class="st-sr">（新しいタブ）</span></a>'; }).join('') + '</div></li>';
      }).join('') + '</ul></section>';
  };
  S.ContractorCTA = function (p) {
    p = p || {};
    return '<section class="st-pro" aria-labelledby="pro-t"><div><p class="st-pro__eyebrow">' + S.PRLabel({ dark: true }) + '<span>施工を依頼したい方へ</span></p><h3 class="st-pro__title" id="pro-t">' + esc(p.title || 'フェンス工事を、地域の施工会社に相談する') + '</h3><ul>' +
      (p.points || ['無料で複数社から見積もりを取れる', '対応エリア・得意な施工で比較できる', '相談だけでもOK・断りやすい仕組み']).map(function (t) { return '<li>' + icon('check') + esc(t) + '</li>'; }).join('') +
      '</ul></div><div class="st-pro__side">' + S.Button({ href: p.href || '/contractors/estimate/', label: p.cta || '無料見積もりを依頼する', variant: 'accent', rel: 'sponsored' }) + '<a class="st-a" href="' + esc(href('/contractors/criteria/')) + '">掲載基準・比較方法を見る</a></div></section>';
  };
  S.AuthorBox = function (p) {
    p = p || {};
    return '<section class="st-author" aria-label="執筆・監修"><span class="st-author__avatar" aria-hidden="true">' + esc(p.initial || 'S') + '</span><div><p class="st-author__role">' + esc(p.role || '執筆') + '</p><p class="st-author__name">' + esc(p.name || 'SOTORINO編集部') + '</p><p class="st-author__bio">' + esc(p.bio || '外構・庭づくり・住まいに関する情報を、根拠と条件を添えてわかりやすくお届けしています。') + '</p>' +
      '<p class="st-author__links"><a class="st-a" href="' + esc(href('/editorial-policy/')) + '">編集ポリシー</a><a class="st-a" href="' + esc(href('/about/supervisors/')) + '">監修者一覧</a></p>' +
      (p.sources ? '<div class="st-sources"><b>参考資料</b><br>' + p.sources.map(esc).join('<br>') + '</div>' : '') + '</div></section>';
  };
  S.TopicCluster = function (p) {
    p = p || {};
    var s = p.series || S.data.fenceSeries, cur = p.current, idx = 0;
    s.items.forEach(function (it, i) { if (it.id === cur) idx = i + 1; });
    return '<nav class="' + cx('st-cluster', p.compact && 'st-cluster--compact') + '" aria-labelledby="cl-' + (p.uid || 'a') + '"><div class="st-cluster__head">' + icon('layers') + '<div><p class="st-cluster__eyebrow">シリーズで読む</p><p class="st-cluster__title" id="cl-' + (p.uid || 'a') + '"><a href="' + esc(href(s.path)) + '">' + esc(s.name) + '</a></p></div>' + (idx ? '<span class="st-cluster__progress">' + idx + ' / ' + s.items.length + '</span>' : '') + '</div><ol>' +
      s.items.map(function (it, i) {
        var no = '<span class="st-cluster__no">' + ('0' + (i + 1)).slice(-2) + '</span>';
        if (it.id === cur) return '<li><span aria-current="page">' + no + '<span>' + esc(it.name) + '</span><span class="st-cluster__now">この記事</span></span></li>';
        if (!it.id) return '<li><span>' + no + '<span style="color:var(--muted-text)">' + esc(it.name) + '</span><span class="st-date">準備中</span></span></li>';
        var a = A(it.id); return '<li><a href="' + esc(href(a.path)) + '">' + no + '<span>' + esc(it.name) + '</span>' + icon('chevR') + '</a></li>';
      }).join('') + '</ol></nav>';
  };
  S.RelatedArticles = function (p) {
    return '<section class="st-block" aria-labelledby="' + (p.uid || 'rel') + '-t"><div class="st-endhead"><h2 id="' + (p.uid || 'rel') + '-t">' + esc(p.title || '関連記事') + '</h2>' + (p.more ? S.More({ href: p.more, label: p.moreLabel }) : '') + '</div>' +
      (p.list ? '<ul class="st-endlist">' + p.items.map(function (id) { var a = A(id); return '<li><a href="' + esc(href(a.path)) + '"><span>' + esc(a.title) + '</span>' + S.Date({ date: a.date }) + '</a></li>'; }).join('') + '</ul>'
        : '<ul class="st-grid st-grid--3">' + p.items.map(function (id) { return '<li>' + S.ArticleCard({ article: id }) + '</li>'; }).join('') + '</ul>') + '</section>';
  };
  S.SideList = function (p) { return '<section class="st-box" aria-labelledby="' + p.uid + '-t"><h2 class="st-box__title" id="' + p.uid + '-t">' + esc(p.title) + '</h2><ul class="st-sidelist">' + p.items.map(function (id) { var a = A(id); return '<li>' + S.ArticleCard({ article: a, variant: 'mini', headingLevel: 'span' }) + '</li>'; }).join('') + '</ul></section>'; };
  S.ConsultBox = function (p) {
    p = p || {};
    return '<section class="st-consult" aria-labelledby="cs-t"><p style="display:flex;gap:8px;align-items:center">' + S.PRLabel() + '</p><h2 class="st-consult__title" id="cs-t" style="margin-top:8px">' + (p.title || '外構のプロに<br>相談してみませんか？') + '</h2><ul>' +
      ['無料で複数社から見積もり', '地域の施工会社を比較', '相談だけでもOK'].map(function (t) { return '<li>' + icon('check') + t + '</li>'; }).join('') + '</ul>' + S.Button({ href: '/contractors/estimate/', label: '無料見積もりを依頼する', block: true, rel: 'sponsored' }) + '</section>';
  };
  S.MiniTOC = function (p) { return '<nav class="st-box st-minitoc-box" aria-label="この記事の目次（サイドバー）"><p class="st-box__title">' + icon('book') + '目次</p><ul class="st-minitoc">' + p.items.map(function (it) { return '<li><a href="#' + esc(it.id) + '" data-st-spy="' + esc(it.id) + '">' + esc(it.text) + '</a></li>'; }).join('') + '</ul></nav>'; };

  /* ================= article body (block renderer) ================= */
  S.ArticleBody = function (blocks) {
    return '<div class="st-body">' + blocks.map(function (b) {
      switch (b.type) {
        case 'h2': return '<h2 class="st-h2" id="' + esc(b.id) + '">' + esc(b.text) + '</h2>';
        case 'h3': return '<h3 class="st-h3" id="' + esc(b.id) + '">' + esc(b.text) + '</h3>';
        case 'p': return '<p>' + b.html + '</p>';
        case 'ul': return '<ul class="st-ul">' + b.items.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>';
        case 'iconFeatures': return S.IconFeatureGrid(b);
        case 'types': return S.TypeGrid(b);
        case 'table': return S.CompareTable(b);
        case 'stats': return S.StatSummary(b);
        case 'note': return S.NoteBox(b);
        case 'steps': return S.Steps(b);
        case 'proscons': return S.ProsCons(b);
        case 'checklist': return S.Checklist(b);
        case 'faq': return S.FAQ(b);
        case 'related': return S.InlineRelated(b);
        case 'gallery': return S.Gallery(b);
        case 'wrap': return '<section class="st-wrap" aria-labelledby="wrap-t"><h2 class="st-wrap__title" id="wrap-t">' + esc(b.title || 'まとめ') + '</h2><ul class="st-ul">' + b.items.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul></section>';
        case 'next': return S.NextSteps(b);
        case 'products': return S.ProductCards(b);
        case 'contractor': return S.ContractorCTA(b);
        case 'html': return b.html;
        default: return '';
      }
    }).join('') + '</div>';
  };
  S.tocFrom = function (blocks) {
    var out = [];
    blocks.forEach(function (b) { if (b.type === 'h2' && b.toc !== false) out.push({ id: b.id, text: b.text.replace(/^\d+\.\s*/, ''), children: [] }); else if (b.type === 'h3' && out.length) out[out.length - 1].children.push({ id: b.id, text: b.text }); });
    return out;
  };

  /* ================= sample article: fence guide ================= */
  S.data.fenceArticle = {
    id: 'fence-guide',
    lead: '目隠し・メッシュ・ルーバーなどフェンスの種類と特徴、費用の考え方、目的別の選び方をわかりやすく解説。おしゃれな施工例や、失敗しないためのチェックリストも紹介します。',
    heroAlt: '木目調の横格子フェンスと植栽のある住宅の外構',
    summary: ['フェンスの主な種類とそれぞれの特徴', '目的別（目隠し・防犯・デザイン）の選び方', '費用の内訳と、工事にかかる期間の目安', 'おしゃれな施工例と最近のトレンド', 'フェンス選びで失敗しないためのポイント'],
    blocks: [
      { type: 'h2', id: 'role', text: '1. フェンスの役割と選ぶ前に知っておきたいこと' },
      { type: 'p', html: 'フェンスは、敷地の境界を示すだけでなく、<strong>プライバシーの確保や防犯、街並みとの調和</strong>など、さまざまな役割を持つ外構アイテムです。まずは「何のために設置するのか」を整理し、ライフスタイルや家のデザインに合ったフェンスを選ぶことが大切です。' },
      { type: 'iconFeatures', items: [
        { img: 'fence-privacy', icon: 'eye', title: 'プライバシーの確保', desc: '外からの視線を遮り、快適な暮らしを実現。', alt: '木目調の目隠しフェンス' },
        { img: 'fence-security', icon: 'lock', title: '防犯性の向上', desc: '侵入を防ぎ、家族の安全を守る。', alt: 'スチール製のフェンスと門扉' },
        { img: 'fence-design', icon: 'house', title: 'デザイン性の向上', desc: '住まいの印象を高め、おしゃれな外観に。', alt: '植栽と調和したフェンスのある住宅' },
        { img: 'fence-wind', icon: 'wind', title: '風や騒音の軽減', desc: '風よけや騒音対策にも効果的。', alt: '隙間の少ない横板フェンス' }
      ] },
      { type: 'related', article: 'blind-fence' },
      { type: 'h2', id: 'types', text: '2. フェンスの種類と特徴' },
      { type: 'p', html: 'フェンスにはさまざまな種類があり、それぞれデザインや機能、価格が異なります。ここでは代表的なフェンスの種類と特徴を紹介します。気になる種類は、各記事でくわしく比較しています。' },
      { type: 'types', items: [
        { img: 'fencetype-blind', name: '目隠しフェンス', desc: 'プライバシーを重視したい方に。住宅街で人気の定番タイプ。', path: '/column/mekakushi-fence-erabikata/' },
        { img: 'fencetype-mesh', name: 'メッシュフェンス', desc: 'コストを抑えつつ開放感のあるフェンス。境界用におすすめ。', path: '/column/fence-shurui-hikaku/' },
        { img: 'fencetype-louver', name: 'ルーバーフェンス', desc: '視線を遮りながら風を通す。デザイン性と機能性を両立。', path: '/column/fence-shurui-hikaku/' },
        { img: 'fencetype-lattice', name: '縦格子フェンス', desc: 'スタイリッシュで和モダンな印象。和風の住宅にもよく合う。', path: '/column/fence-shurui-hikaku/' },
        { img: 'fencetype-bamboo', name: '竹垣風フェンス', desc: '和の雰囲気を演出できる。庭や和風住宅におすすめ。', path: '/column/fence-shurui-hikaku/' },
        { img: 'fencetype-cast', name: '鋳物フェンス', desc: 'ヨーロピアンなデザインで高級感。洋風住宅やおしゃれな外構に。', path: '/column/fence-shurui-hikaku/' }
      ] },
      { type: 'h2', id: 'purpose', text: '3. 目的別のおすすめフェンス' },
      { type: 'p', html: '同じ「目隠し」でも、リビング前の視線対策と、道路沿いの境界とでは適したフェンスが変わります。目的ごとの向き・不向きを比較しました。' },
      { type: 'table', caption: '目的別のフェンス比較', head: ['種類', '目隠し', '通風・採光', '防犯', '費用感', '向いている場所'], rows: [
        { cells: ['目隠しフェンス', '◎', '△ 隙間が少ない', '○', '中〜高', 'リビング前・浴室まわり'], pick: true },
        { cells: ['ルーバーフェンス', '○', '◎ 羽板の角度で調整', '○', '高', '庭・テラスの囲い'] },
        { cells: ['メッシュフェンス', '× 視線は通る', '◎', '△', '低', '隣地との境界・裏手'] },
        { cells: ['縦格子フェンス', '○ 角度により変化', '○', '○', '中', '道路沿い・アプローチ'] },
        { cells: ['鋳物フェンス', '×', '◎', '○ 高さ次第', '高', '門まわり・装飾'] }
      ], note: '◎：とても向いている　○：向いている　△：条件による　×：向いていない<br>※ 評価は編集部の比較基準による目安です。製品・高さ・設置条件によって異なります。' },
      { type: 'note', kind: 'point', title: '高さは「誰の、どこからの視線か」で決める', items: ['道路からの視線：地面から <strong>1.6〜1.8m前後</strong> が目安（敷地の高低差で変わります）', '室内に座ったときの視線：窓の位置と床の高さを基準に測る', '高くしすぎると圧迫感・日当たり・風圧の負担が増える'] },
      { type: 'h2', id: 'cost', text: '4. 費用相場と工事の流れ' },
      { type: 'p', html: 'フェンスの費用は、<strong>本体価格・基礎（ブロック）工事・施工費</strong>の合計で決まります。同じ長さでも、既存ブロックを使えるか、新たに基礎をつくるかで総額が大きく変わります。<a href="' + esc(href('/column/fence-setti-hiyou-ikkura/')) + '">費用の内訳と見積もりの見方</a>もあわせて確認してください。' },
      { type: 'stats', items: [
        { label: '本体価格の目安（1mあたり）', value: '◯〜◯', unit: '万円', note: '素材・高さによって変動' },
        { label: '工期の目安（10m程度）', value: '◯〜◯', unit: '日', note: '基礎工事の有無で変動' },
        { label: '見積もりで確認する項目', value: '6', unit: '項目', note: '本体・基礎・柱・処分費など' }
      ] },
      { type: 'note', kind: 'info', title: '数値の掲載ルール', html: '費用・耐用年数などの数値は、メーカー公表値や編集部の調査など<strong>出典と確認日</strong>を併記して掲載します（このデザインでは「◯」で仮置きしています）。' },
      { type: 'h3', id: 'cost-flow', text: '依頼から完成までの流れ' },
      { type: 'steps', items: [
        { title: '現地調査・ヒアリング', time: '1〜2週間', desc: '境界の位置、既存ブロックの状態、高さの希望を確認します。' },
        { title: 'プラン提案・見積もり', time: '1〜2週間', desc: '複数案を比較。本体・基礎・処分費が分かれているか確認しましょう。' },
        { title: '契約・近隣へのあいさつ', desc: '工事日程と車両の出入りを近隣に伝えておくとトラブルを防げます。' },
        { title: '施工・完成確認', time: '数日〜', desc: '柱のぐらつき、仕上がりの水平、扉の開閉を一緒に確認します。' }
      ] },
      { type: 'h2', id: 'examples', text: '5. おしゃれな施工例' },
      { type: 'p', html: '素材の色を建物のサッシや外壁に合わせると、まとまりのある外観になります。植栽と組み合わせて「隠しすぎない」のがおしゃれに見せるコツです。' },
      { type: 'gallery', items: [
        { img: 'thumb-fence', title: '黒の横格子フェンスで、人工芝の庭をすっきり囲う', spec: ['目隠しフェンス', '高さ1.8m', '施工例（提供：施工会社名）'], alt: '黒い横格子フェンスと人工芝の庭' },
        { img: 'fence-design', title: 'ブロックと植栽を組み合わせた開放的な境界', spec: ['縦格子＋植栽', '高さ1.2m', '施工例（提供：施工会社名）'], alt: '低めのフェンスと植栽の外構' }
      ] },
      { type: 'h2', id: 'tips', text: '6. フェンス選びで失敗しないポイント' },
      { type: 'proscons', proTitle: '目隠しフェンスを選ぶメリット', conTitle: '注意したいデメリット', pros: ['視線を気にせず庭やリビングで過ごせる', '外観の印象を大きく変えられる', '防犯・境界の意思表示になる'], cons: ['高さによっては圧迫感が出る', '風を受けやすく、基礎の強度が必要', '日当たり・風通しが悪くなる場合がある'] },
      { type: 'checklist', title: '発注前のチェックリスト', items: [
        { text: '境界線の位置を確認した', sub: '境界標・測量図で確認。お隣との共有か単独設置かも決めておく' },
        { text: '必要な高さを、実際の視線で測った' },
        { text: '既存ブロックの高さ・状態を確認した', sub: '古いブロックへの後付けは強度の確認が必要です' },
        { text: '風の強さ・積雪など地域の条件を確認した' },
        { text: '見積もりの内訳（本体・基礎・施工・処分）を比較した' }
      ] },
      { type: 'note', kind: 'caution', title: 'ブロック塀への後付けは要注意', html: '既存のブロック塀に高いフェンスを後付けすると、風の力で塀ごと倒れるおそれがあります。<a href="' + esc(href('/exterior/block-wall-safety/')) + '">ブロック塀の安全点検</a>を行い、必要に応じて施工会社に強度を確認してもらいましょう。' },
      { type: 'h2', id: 'faq', text: '7. よくある質問' },
      { type: 'faq', items: [
        { q: 'フェンスの高さに法律上の決まりはありますか？', a: 'フェンス単体の高さに一律の上限はありませんが、ブロック塀と組み合わせる場合は建築基準法の規定や自治体の条例が関係します。地域の条件は自治体や施工会社に確認してください。' },
        { q: 'お隣との境界にフェンスを立てるときの注意点は？', a: '境界線の確認と、どちらの敷地に設置するかの合意が大切です。<a class="st-a" href="' + esc(href('/exterior/fence/boundary/')) + '">境界フェンスとトラブルの防ぎ方</a>でくわしく解説しています。' },
        { q: 'DIYで設置することはできますか？', a: '低めのメッシュフェンスなどはDIYも可能ですが、目隠しフェンスのように風を受ける製品は基礎の強度が重要です。<a class="st-a" href="' + esc(href('/column/diy-mekakushi-fence-setti/')) + '">DIYの向き不向き</a>を確認しましょう。' }
      ] },
      { type: 'wrap', items: ['まずは「目隠し・防犯・デザイン」のどれを優先するかを決める', '高さは実際の視線で測り、圧迫感と風の負担も考える', '費用は本体だけでなく、基礎・施工・処分費まで含めて比較する', 'ブロックへの後付けや境界まわりは、プロに確認すると安心'] },
      { type: 'h2', id: 'next', text: '次に読みたい記事', toc: false },
      { type: 'next' },
      { type: 'products', items: [
        { img: 'fencetype-mesh', name: 'スチールメッシュフェンス（商品名）', forWhom: '境界をDIYで区切りたい方に。軽量で扱いやすい。', spec: [['高さ', '800〜1200mm'], ['素材', 'スチール'], ['施工', '独立基礎・ブロック']], price: '参考価格：◯◯円〜', shops: [{ name: 'Amazon' }, { name: '楽天市場' }] },
        { img: 'fencetype-blind', name: 'アルミ木目調 目隠しフェンス（商品名）', forWhom: '庭の一部をおしゃれに目隠ししたい方に。', spec: [['高さ', '1200〜1800mm'], ['素材', 'アルミ形材'], ['施工', 'ブロック推奨']], price: '参考価格：◯◯円〜', shops: [{ name: 'Amazon' }, { name: '楽天市場' }] },
        { img: 'fencetype-louver', name: 'ルーバーパネル（商品名）', forWhom: 'ベランダやテラスの一部を囲いたい方に。', spec: [['高さ', '900〜1800mm'], ['素材', '樹脂・アルミ'], ['施工', '置き型可']], price: '参考価格：◯◯円〜', shops: [{ name: 'Amazon' }, { name: '楽天市場' }] }
      ] },
      { type: 'contractor' }
    ]
  };

  /* ================= pages ================= */
  S.TopPage = function () {
    return '<div class="st">' + S.Header({ active: 'home' }) + '<main id="main" class="st-main--flush">' + S.HeroSlider() +
      '<div class="st-container">' + S.CategoryTiles() +
      '<section class="st-section st-top-feature" aria-labelledby="feat-t">' + S.FeatureGrid({ guide: true, heading: { title: '今、読まれている特集', en: 'Feature', more: '/feature/', id: 'feat-t' } }) + '</section>' +
      '<section class="st-section st-top-new" aria-labelledby="new-t"><div class="st-split st-split--top"><div>' + S.SectionHeading({ title: '新着記事', en: 'New articles', more: '/new/', id: 'new-t' }) + S.LatestGrid() + '</div>' +
      '<div class="st-side st-side--top">' + S.Ranking({ id: 'top-rk' }) + S.CTABanner({ title: 'DIYで叶える<br>理想の庭', text: '人工芝・防草シート・資材をまとめて比較', cta: '商品を見る', href: '/purpose/products/', img: 'photo-garden-dusk' }) + '</div></div></section></div>' +
      S.PurposeNav() + '</main>' + S.Footer() + '</div>';
  };
  S.ArticlePage = function (p) {
    p = p || {};
    var art = p.article || S.data.fenceArticle, a = A(art.id), toc = S.tocFrom(art.blocks);
    return '<div class="st">' + S.Header({ active: 'exterior' }) +
      S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: '外構・エクステリア', path: '/exterior/' }, { name: 'フェンス', path: '/exterior/fence/' }, { name: a.title }] }) +
      '<div class="st-container"><div class="st-article-wrap"><main id="main"><article>' +
      S.ArticleHeader({ article: a, lead: art.lead, heroAlt: art.heroAlt }) +
      '<div class="st-intro">' + S.SummaryBox({ items: art.summary }) + S.TableOfContents({ items: toc }) + '</div>' +
      S.ArticleBody(art.blocks) +
      '<div class="st-block">' + S.AuthorBox({ sources: ['・建築基準法施行令 第62条の8（補強コンクリートブロック造の塀）', '・各メーカー公表の製品仕様（確認日：YYYY.MM.DD）'] }) + '</div>' +
      '<div class="st-block">' + S.TagList({ tags: ['フェンス', '目隠しフェンス', 'フェンス 費用', '境界', 'DIY'] }) + '</div>' +
      '<div class="st-block">' + S.TopicCluster({ current: 'fence-guide', uid: 'main' }) + '</div>' +
      '</article>' +
      S.RelatedArticles({ title: '関連記事', items: ['fence-types', 'fence-cost', 'exterior-design'], uid: 'rel' }) +
      S.RelatedArticles({ title: '外構・エクステリアの新着記事', items: ['exterior-flow', 'blind-fence', 'fence-diy', 'carport-price', 'deck-ideas'], list: true, more: '/exterior/', moreLabel: '一覧を見る', uid: 'same' }) +
      '</main><aside class="st-side" aria-label="サイドバー">' +
      S.CTABanner({ title: '理想の外構を<br>プロとつくる', text: '外構工事の無料見積もりはこちら', cta: '無料で相談する', img: 'photo-black-house-light' }) +
      S.Ranking({ id: 'side-rk', limit: 5 }) +
      S.TopicCluster({ current: 'fence-guide', compact: true, uid: 'side' }) +
      S.SideList({ uid: 'srel', title: '関連記事', items: ['blind-fence', 'fence-cost', 'exterior-design', 'subsidy'] }) +
      S.ConsultBox() +
      '<div class="st-sticky">' + S.MiniTOC({ items: toc }) + '</div>' +
      '</aside></div></div>' + S.Footer() + '</div>';
  };
  S.CategoryPage = function () {
    var g = S.data.turfGuide;
    var topics = [
      { id: 'basics', name: '基礎知識・性能', more: '/garden/turf/basics/', items: ['/garden/turf/basics/', '/garden/turf/quality/', 'jinkoshiba-shurui-erabikata'] },
      { id: 'cost', name: '費用・施工・業者選び', more: '/garden/turf/contractors/', items: ['jinkoshiba-sekou-hiyou-souba', '/garden/turf/install/', '/garden/turf/contractors/'] },
      { id: 'use', name: '用途別の選び方・お手入れ', more: '/garden/turf/use/', items: ['/garden/turf/use/', '/garden/turf/care/', '/garden/turf/winter/'] }
    ];
    return '<div class="st">' + S.Header({ active: 'garden' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: '庭づくり', path: '/garden/' }, { name: '人工芝' }] }) +
      '<main id="main"><div class="st-container"><section class="st-cathero" aria-labelledby="cat-t"><div><p class="st-cathero__eyebrow">ARTIFICIAL TURF</p><h1 class="st-cathero__title" id="cat-t">人工芝</h1>' +
      '<p class="st-cathero__text">人工芝の種類や品質の見分け方、下地づくりから施工、DIYと業者依頼の費用比較、メンテナンスまで。はじめての方が「知る → 比べる → 選ぶ」まで迷わず進めるよう、テーマ別に整理しています。</p>' +
      '<nav class="st-subnav" aria-label="人工芝のテーマ">' + g.chapters.map(function (c) { return '<a href="' + esc(href(c.path)) + '">' + esc(c.name) + '</a>'; }).join('') + '</nav></div>' + media('thumb-turf', '芝生の庭と植栽', '43') + '</section>' +
      '<section class="st-section" aria-labelledby="jr-t">' + S.SectionHeading({ title: 'はじめての方へ', en: 'Start here', id: 'jr-t' }) +
      '<div class="st-journey">' + [
        ['STEP 1', '基礎を知る', '芝丈・密度・素材の違いと、品質を見分けるポイント。', ['人工芝の種類と選び方', '天然芝との違い'], '/garden/turf/basics/'],
        ['STEP 2', '比べる', '費用、DIYと業者施工、商品ごとの違いを比較。', ['人工芝の費用相場', 'DIYと業者施工の比較'], '/column/jinkoshiba-sekou-hiyou-souba/'],
        ['STEP 3', '選ぶ・相談する', '用途に合った商品選びと、施工会社への伝え方。', ['用途別の選び方', '施工会社の選び方'], '/garden/turf/use/']
      ].map(function (s) { return '<a href="' + esc(href(s[4])) + '"><span class="st-journey__step">' + s[0] + '</span><p class="st-journey__title">' + s[1] + '</p><p class="st-journey__desc">' + s[2] + '</p><span class="st-journey__links">' + s[3].map(function (l) { return '<span>' + icon('chevR') + esc(l) + '</span>'; }).join('') + '</span></a>'; }).join('') + '</div></section>' +
      '<div class="st-section"><div class="st-split"><div>' + topics.map(function (t) { return '<section class="st-topic" id="' + t.id + '" aria-labelledby="tp-' + t.id + '">' + S.SectionHeading({ title: t.name, more: t.more, id: 'tp-' + t.id }) + S.RefGrid(S.refs(t.items), { cols: 3, desc: true }) + '</section>'; }).join('') +
      '<section class="st-section" aria-labelledby="cmp-t">' + S.SectionHeading({ title: '比較して選ぶ', en: 'Compare', id: 'cmp-t' }) + '<div class="st-compare">' +
      '<a href="' + esc(href('/column/jinkoshiba-shurui-erabikata/')) + '"><span class="st-compare__icon">' + icon('scale') + '</span><span><b>人工芝 商品比較</b><small>芝丈・密度・裏面構造・価格を同じ基準で比較</small></span>' + icon('chevR') + '</a>' +
      '<a href="' + esc(href('/garden/turf/contractors/')) + '"><span class="st-compare__icon">' + icon('user') + '</span><span><b>人工芝の施工会社を比較</b><small>対応エリア・保証・見積もり条件を確認</small></span>' + icon('chevR') + '</a></div></section></div>' +
      '<div class="st-side">' + S.Ranking({ mode: 'editor', id: 'cat-ed', items: ['turf-cost', 'garden-guide', 'garden-care', 'deck-ideas'] }) + S.ConsultBox({ title: '人工芝の施工を<br>相談してみませんか？' }) + '</div></div></div>' +
      '</div></main>' + S.Footer() + '</div>';
  };

  /* ================= structured data helpers (for the real site) ================= */
  S.seo = {
    articleJsonLd: function (a, o) { o = o || {}; return { '@context': 'https://schema.org', '@type': 'Article', headline: a.title, description: a.desc, datePublished: a.date.replace(/\./g, '-'), dateModified: (a.updated || a.date).replace(/\./g, '-'), image: [o.imageUrl], author: { '@type': 'Organization', name: 'SOTORINO編集部', url: o.authorUrl }, publisher: { '@type': 'Organization', name: 'SOTORINO' }, mainEntityOfPage: o.url }; },
    faqJsonLd: function (items) { return { '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: items.map(function (q) { return { '@type': 'Question', name: q.q, acceptedAnswer: { '@type': 'Answer', text: q.a.replace(/<[^>]+>/g, '') } }; }) }; },
    breadcrumbJsonLd: function (items, origin) { return { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: items.map(function (it, i) { return { '@type': 'ListItem', position: i + 1, name: it.name, item: it.path ? (origin || '') + it.path : undefined }; }) }; }
  };

  /* ================= behaviour ================= */
  function store() {
    try { return JSON.parse(localStorage.getItem(S.config.favoritesKey) || '[]'); } catch (e) { return S._favMem || []; }
  }
  function save(list) { S._favMem = list; try { localStorage.setItem(S.config.favoritesKey, JSON.stringify(list)); } catch (e) { } }
  function $(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function hilite(text, q) { var t = esc(text); if (!q) return t; var i = text.toLowerCase().indexOf(q.toLowerCase()); if (i < 0) return t; return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length)); }
  S.searchArticles = function (q) {
    q = (q || '').trim().toLowerCase(); if (!q) return [];
    var terms = q.split(/\s+/);
    return S.data.articles.filter(function (a) {
      var hay = (a.title + ' ' + a.desc + ' ' + (a.tags || []).join(' ') + ' ' + (S.data.catName[a.cat] || '')).toLowerCase();
      return terms.every(function (t) { return hay.indexOf(t) > -1; });
    });
  };

  function bindSearch(form) {
    var input = form.querySelector('input'), panel = form.querySelector('.st-search__panel');
    function render() {
      var q = input.value.trim();
      if (!q) { panel.hidden = true; input.setAttribute('aria-expanded', 'false'); return; }
      var res = S.searchArticles(q).slice(0, 6);
      panel.innerHTML = '<p class="st-search__count" role="status">「' + esc(q) + '」の記事 ' + res.length + '件</p>' + (res.length ? '<ul>' + res.map(function (a) { return '<li><a class="st-search__item" href="' + esc(href(a.path)) + '">' + media(a.img, '', '43') + '<span>' + S.CategoryLabel(a.cat) + '<b>' + hilite(a.title, q.split(/\s+/)[0]) + '</b></span></a></li>'; }).join('') + '</ul>' : '<p class="st-search__empty">該当する記事が見つかりませんでした。キーワードを変えるか、<a class="st-a" href="' + esc(href('/new/')) + '">新着記事</a>からお探しください。</p>');
      panel.hidden = false; input.setAttribute('aria-expanded', 'true');
    }
    input.addEventListener('input', render);
    input.addEventListener('focus', function () { if (input.value) render(); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { var f = panel.querySelector('a'); if (f && !panel.hidden) { e.preventDefault(); f.focus(); } }
      if (e.key === 'Escape') { panel.hidden = true; input.setAttribute('aria-expanded', 'false'); }
    });
    panel.addEventListener('keydown', function (e) {
      var links = $(panel, 'a.st-search__item'), i = links.indexOf(document.activeElement);
      if (e.key === 'ArrowDown' && i < links.length - 1) { e.preventDefault(); links[i + 1].focus(); }
      if (e.key === 'ArrowUp') { e.preventDefault(); (i > 0 ? links[i - 1] : input).focus(); }
      if (e.key === 'Escape') { panel.hidden = true; input.focus(); }
    });
    form.addEventListener('focusout', function () { setTimeout(function () { if (!form.contains(document.activeElement)) { panel.hidden = true; input.setAttribute('aria-expanded', 'false'); } }, 0); });
    form.addEventListener('submit', function (e) { if (S.config.base === '#') { e.preventDefault(); render(); } });
  }

  function bindSlider(el) {
    var slides = $(el, '[data-st-slide]'), dots = $(el, '[data-st-dot]'), count = el.querySelector('[data-st-count]'), pick = el.querySelector('[data-st-pick]'), pickT = el.querySelector('[data-st-pick-title]'), pauseBtn = el.querySelector('[data-st-pause]');
    var cur = 0, timer = null, paused = reduce, hold = false, data = S.data.heroSlides;
    function go(i) {
      cur = (i + slides.length) % slides.length;
      slides.forEach(function (s, n) { s.classList.toggle('is-active', n === cur); if (n === cur) s.removeAttribute('aria-hidden'); else s.setAttribute('aria-hidden', 'true'); });
      dots.forEach(function (d, n) { if (n === cur) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); });
      count.textContent = ('0' + (cur + 1)).slice(-2) + ' / ' + ('0' + slides.length).slice(-2);
      var a = data[cur] && A(data[cur].article); if (a && pick) { pick.setAttribute('href', href(a.path)); pickT.textContent = a.title; }
    }
    function tick() { clearInterval(timer); if (!paused && !hold) timer = setInterval(function () { go(cur + 1); }, S.config.autoplayMs); }
    function setPaused(v) { paused = v; pauseBtn.innerHTML = icon(v ? 'play' : 'pause'); pauseBtn.setAttribute('aria-label', v ? '自動再生を開始' : '自動再生を停止'); tick(); }
    el.querySelector('[data-st-prev]').addEventListener('click', function () { go(cur - 1); tick(); });
    el.querySelector('[data-st-next]').addEventListener('click', function () { go(cur + 1); tick(); });
    dots.forEach(function (d) { d.addEventListener('click', function () { go(+d.getAttribute('data-st-dot')); tick(); }); });
    pauseBtn.addEventListener('click', function () { setPaused(!paused); });
    el.addEventListener('mouseenter', function () { hold = true; tick(); });
    el.addEventListener('mouseleave', function () { hold = false; tick(); });
    el.addEventListener('focusin', function () { hold = true; tick(); });
    el.addEventListener('focusout', function () { hold = false; tick(); });
    setPaused(paused);
  }

  function bindTabs(box) {
    var tabs = $(box, '[role="tab"]');
    function sel(t) {
      tabs.forEach(function (x) { var on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1; var p = box.querySelector('#' + x.getAttribute('aria-controls')); if (p) p.hidden = !on; });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { sel(t); });
      t.addEventListener('keydown', function (e) { var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null; if (n == null) return; e.preventDefault(); var nt = tabs[(n + tabs.length) % tabs.length]; sel(nt); nt.focus(); });
    });
  }

  function bindFavorites(root) {
    function refresh() {
      var list = store();
      $(root, '[data-st-fav]').forEach(function (b) { var on = list.indexOf(b.getAttribute('data-st-fav')) > -1; b.setAttribute('aria-pressed', on); var t = b.querySelector('[data-st-fav-text]'); if (t) t.textContent = on ? 'お気に入りに追加済み' : 'お気に入りに追加'; });
      $(root, '[data-st-favcount]').forEach(function (c) { c.textContent = list.length; c.hidden = !list.length; });
      $(root, '[data-st-favpop]').forEach(function (pop) {
        var items = list.map(A).filter(Boolean);
        pop.innerHTML = '<h2>お気に入りの記事</h2>' + (items.length ? '<ul>' + items.map(function (a) { return '<li><a href="' + esc(href(a.path)) + '">' + esc(a.title) + '</a></li>'; }).join('') + '</ul>' : '<p>まだありません。記事ページの「お気に入りに追加」から保存できます（この端末のブラウザに保存されます）。</p>');
      });
    }
    $(root, '[data-st-fav]').forEach(function (b) {
      b.addEventListener('click', function () { var id = b.getAttribute('data-st-fav'), l = store(), i = l.indexOf(id); if (i > -1) l.splice(i, 1); else l.unshift(id); save(l); refresh(); });
    });
    $(root, '[data-st-favbtn]').forEach(function (b) {
      var pop = document.getElementById(b.getAttribute('aria-controls'));
      b.addEventListener('click', function (e) { e.stopPropagation(); var open = pop.hidden; pop.hidden = !open; b.setAttribute('aria-expanded', open); });
      document.addEventListener('click', function (e) { if (!pop.hidden && !pop.contains(e.target)) { pop.hidden = true; b.setAttribute('aria-expanded', 'false'); } });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !pop.hidden) { pop.hidden = true; b.setAttribute('aria-expanded', 'false'); b.focus(); } });
    });
    refresh();
  }

  function bindDrawer(root) {
    var d = root.querySelector('[data-st-drawer]'), opener = root.querySelector('[data-st-drawer-open]');
    if (!d || !opener) return;
    function close() { d.hidden = true; opener.setAttribute('aria-expanded', 'false'); opener.focus(); }
    opener.addEventListener('click', function () { d.hidden = false; opener.setAttribute('aria-expanded', 'true'); var f = d.querySelector('input,button,a'); if (f) f.focus(); });
    $(d, '[data-st-drawer-close]').forEach(function (b) { b.addEventListener('click', close); });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') { var f = $(d, 'a,button,input').filter(function (x) { return x.offsetParent !== null; }); var first = f[0], last = f[f.length - 1]; if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); } else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); } }
    });
  }

  function bindToc(root) {
    $(root, '[data-st-toc]').forEach(function (t) {
      var btn = t.querySelector('.st-toc__toggle'), list = t.querySelector('#' + btn.getAttribute('aria-controls')), lab = t.querySelector('[data-st-toc-label]');
      btn.addEventListener('click', function () { var open = btn.getAttribute('aria-expanded') === 'true'; btn.setAttribute('aria-expanded', !open); list.hidden = open; lab.textContent = open ? '開く' : '閉じる'; });
    });
    var spies = $(root, '[data-st-spy]');
    if (spies.length && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) spies.forEach(function (s) { s.classList.toggle('is-current', s.getAttribute('data-st-spy') === e.target.id); }); }); }, { rootMargin: '-20% 0px -70% 0px' });
      spies.forEach(function (s) { var h = root.querySelector('#' + s.getAttribute('data-st-spy')); if (h) io.observe(h); });
    }
  }

  S.mount = function (root) {
    root = root || document;
    $(root, '[data-st-search]').forEach(bindSearch);
    $(root, '[data-st-slider]').forEach(bindSlider);
    $(root, '[data-st-tabs]').forEach(bindTabs);
    bindFavorites(root); bindDrawer(root); bindToc(root);
    $(root, '[data-st-search-toggle]').forEach(function (b) { b.addEventListener('click', function () { var h = b.closest('[data-st-header]'), open = !h.classList.contains('is-search-open'); h.classList.toggle('is-search-open', open); b.setAttribute('aria-expanded', open); if (open) h.querySelector('.st-header__top > .st-search input').focus(); }); });
    $(root, '[data-st-copy]').forEach(function (b) { b.addEventListener('click', function () { var st = b.parentNode.querySelector('[data-st-copy-status]'), url = b.getAttribute('data-st-copy'); function ok() { st.textContent = 'リンクをコピーしました'; setTimeout(function () { st.textContent = ''; }, 2400); } try { navigator.clipboard.writeText(url).then(ok, function () { st.textContent = 'コピーできませんでした：' + url; }); } catch (e) { st.textContent = url; } }); });
    $(root, '[data-st-check]').forEach(function (c) { var boxes = $(c, 'input'), out = c.querySelector('[data-st-check-count]'); boxes.forEach(function (x) { x.addEventListener('change', function () { out.textContent = boxes.filter(function (y) { return y.checked; }).length + ' / ' + boxes.length + ' 確認済み'; }); }); });
    $(root, 'a[href^="#"]').forEach(function (a) { var h = a.getAttribute('href'); if (/^#\//.test(h)) a.addEventListener('click', function (e) { e.preventDefault(); }); });
    return root;
  };
  S.render = function (el, html) { el.innerHTML = html; return S.mount(el); };
})();
