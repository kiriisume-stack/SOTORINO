(function () {
  'use strict';
  var S = window.Sotorino, esc = S.esc, href = S.href, icon = S.icon, img = S.img, media = S.media;

  /* ================= column data ================= */
  S.colCats = [
    { key: 'basics', name: '外構の基礎知識', full: '外構・エクステリアの基礎知識', icon: 'book', img: 'photo-stone-dusk',
      desc: '外構工事とは何か、どんな種類があり、どの順番で考えればいいのか。オープン外構とクローズ外構の違い、目隠しや防犯、動線設計まで、計画を始める前に押さえておきたい基本をまとめています。' },
    { key: 'garden', name: '庭・ガーデニング', full: '庭・ガーデニング', icon: 'sprout', img: 'photo-courtyard-night',
      desc: '庭の用途の決め方から、地面材・人工芝・砂利・ウッドデッキの選び方、シンボルツリーや花壇、ガーデンライトまで。暮らしに合った庭をつくるためのアイデアと考え方を紹介します。' },
    { key: 'diy', name: 'DIY・自分でできる施工', full: 'DIY・自分でできる施工', icon: 'tool', img: 'photo-prod-stepstone',
      desc: '防草シートや人工芝、砂利、花壇、ウッドデッキなど、自分でできる外構DIYの手順と注意点。DIYで対応できる範囲と、専門業者に任せたほうがよい工事の見分け方も解説します。' },
    { key: 'products', name: '商品・素材・設備', full: '外構商品・素材・設備', icon: 'layers', img: 'photo-light',
      desc: 'フェンス、カーポート、人工芝、防草シート、砂利、タイル、門扉、ポスト、宅配ボックスまで。外構で使う商品と素材の種類・特徴・選び方を比較して整理しています。' },
    { key: 'cost', name: '費用・相場', full: '費用・相場・リフォーム', icon: 'coins', img: 'photo-house-day',
      desc: '外構工事や人工芝、フェンス、カーポート、駐車場の費用がどう決まるのか。見積もりで確認すべき項目、費用を抑える方法、追加費用や補助金の調べ方までお金の話をまとめています。' },
    { key: 'trouble', name: 'トラブル・メンテナンス', full: 'トラブル・メンテナンス', icon: 'shield', img: 'photo-white-deck',
      desc: '雑草、水はけ、水たまり、カビ、苔、虫、フェンスの傾きやコンクリートのひび割れまで。外構でよくあるトラブルの原因と対処法、完成後のメンテナンス方法を解説します。' },
    { key: 'equipment', name: '住宅設備', full: '住宅設備（給湯・水まわり・省エネ）', icon: 'drop', img: 'photo-study-light',
      desc: 'エコキュートや給湯器、食洗機、トイレ、IHコンロ、スマートキー、宅配ボックス、太陽光・蓄電池まで。家の設備の寿命、交換時期、選び方と費用の目安をまとめています。' },
    { key: 'reform', name: 'リフォーム', full: 'リフォーム（内装・外装・外構）', icon: 'house', img: 'photo-interior-living',
      desc: 'キッチン・浴室・トイレの水まわりから、外壁・屋根塗装、玄関ドア、窓、床、全面リフォーム、外構リフォームまで。費用相場と工期、業者選びで失敗しないための考え方を解説します。' },
    { key: 'realestate', name: '不動産・土地', full: '不動産・土地選び', icon: 'pin', img: 'photo-hiraya-dusk',
      desc: '土地選びのチェックポイント、旗竿地・角地の特徴、建ぺい率・容積率、接道義務、セットバック、地盤、境界、ハザードマップまで。家を建てる前・買う前に知っておきたい基礎知識です。' },
    { key: 'money', name: 'お金・補助金', full: 'お金・補助金・税金', icon: 'yen', img: 'photo-wood-balcony',
      desc: '住宅省エネの補助金、窓リフォームや給湯器の支援制度、リフォームローン、減税、火災保険、外構工事の支払い方法まで。家まわりのお金を損しないための制度と手続きの基本をまとめています。' },
    { key: 'lifestyle', name: 'くらしの知識', full: 'くらしの知識（季節・メンテナンス）', icon: 'calendar', img: 'photo-front-green',
      desc: '結露・カビ対策、台風前の備え、排水口の掃除、庭木の剪定、外壁のひび、雨どい、凍結防止、年間メンテナンスまで。季節ごとに家を長持ちさせる暮らしの知恵を紹介します。' },
  ];
  S.colCat = function (k) { for (var i = 0; i < S.colCats.length; i++) if (S.colCats[i].key === k) return S.colCats[i]; return S.colCats[0]; };
  S.colAll = function () { return window.SOTORINO_COLUMNS || []; };
  S.colBySlug = function (slug) { var l = S.colAll(); for (var i = 0; i < l.length; i++) if (l[i].slug === slug) return l[i]; return null; };
  S.colPath = function (a) { return '/column/' + a.slug + '/'; };
  S.colCatPath = function (k) { return '/column/category/' + k + '/'; };
  S.colPagePath = function (n) { return n <= 1 ? '/column/' : '/column/page/' + n + '/'; };
  S.colThumbBase = 'img/col/';
  S.colCard = function (a) { return { id: 'col' + a.id, cat: 'col-' + a.cat, title: a.title, desc: a.excerpt, img: 'col-' + a.slug, date: a.date, path: S.colPath(a) }; };
  S.colRegister = function (base) {
    if (base != null) S.colThumbBase = base;
    S.colCats.forEach(function (c) { S.data.catName['col-' + c.key] = c.name; });
    S.colAll().forEach(function (a) { if (!S.images['col-' + a.slug]) S.images['col-' + a.slug] = S.colThumbBase + a.slug + '.jpg'; });
  };

  /* ================= related (same category + shared keywords) ================= */
  S.colRelated = function (a) {
    var all = S.colAll(), same = all.filter(function (x) { return x.cat === a.cat && x.id !== a.id; });
    same.sort(function (x, y) {
      var sx = (x.tags || []).filter(function (t) { return (a.tags || []).indexOf(t) > -1; }).length, sy = (y.tags || []).filter(function (t) { return (a.tags || []).indexOf(t) > -1; }).length;
      return (sy - sx) || (Math.abs(x.id - a.id) - Math.abs(y.id - a.id));
    });
    var cross = all.filter(function (x) { return x.cat !== a.cat && (x.tags || []).some(function (t) { return (a.tags || []).indexOf(t) > -1; }); })
      .sort(function (x, y) { return (y.tags.filter(function (t) { return a.tags.indexOf(t) > -1; }).length) - (x.tags.filter(function (t) { return a.tags.indexOf(t) > -1; }).length); });
    var linked = (a.links || []).map(S.colBySlug).filter(Boolean);
    var lsame = linked.filter(function (x) { return x.cat === a.cat; }), lcross = linked.filter(function (x) { return x.cat !== a.cat; });
    function uniq(l) { var seen = {}; return l.filter(function (x) { if (seen[x.id]) return false; seen[x.id] = 1; return true; }); }
    return { same: uniq(lsame.concat(same)).slice(0, 4), cross: uniq(lcross.concat(cross)).filter(function (x) { return x.cat !== a.cat; }).slice(0, 4), linked: linked };
  };

  /* ================= body transform (de-templated headings, image slots) ================= */
  var LABELS = {
    intro: ['こんな疑問に', 'はじめに', 'よくある悩み', 'この記事のテーマ'],
    answer: ['先に結論', 'この記事の答え', '結論から言うと', 'ひとことで言うと'],
    wrap: ['まとめ', 'この記事のおさらい', '要点のおさらい', 'ポイントのふり返り'],
    caution: ['注意', '気をつけたい点', '見落としがち', 'チェック'],
    compare: ['比較', '一覧で比べる', '違いを整理', '比べてみる'],
    basic: ['基礎知識', 'まず知っておきたい', '仕組みを知る', '基本をおさえる'],
    detail: ['くわしく解説', '詳しく見る', '深掘り', 'ポイント解説'],
    judge: ['判断の基準', '選び方の目安', 'どう決める？', '比べて選ぶ'],
    faq: ['よくある質問', 'Q&A', '気になる疑問', 'みんなの疑問']
  };
  function pick(kind, id) { var l = LABELS[kind]; return l[id % l.length]; }
  function strip(h) { return h.replace(/<[^>]+>/g, ''); }
  function slotHTML(attrs, cap) {
    var kind = (attrs.match(/data-kind="([^"]+)"/) || [])[1] || 'photo', n = +((attrs.match(/data-n="(\d+)"/) || [])[1] || 1), ratio = ((attrs.match(/data-ratio="([^"]+)"/) || [])[1] || '3:2').replace(':', ' / ');
    var cells = kind === 'photo' || kind === 'diagram' ? 1 : Math.min(n, kind === 'beforeafter' ? 2 : 8), out = '', shown = 0;
    var vid = (attrs.match(/data-video="([^"]+)"/) || [])[1];
    if (vid) return '<figure class="st-imgslot st-imgslot--video"><div class="st-video-embed"><iframe src="https://www.youtube-nocookie.com/embed/' + esc(vid) + '" title="' + esc(cap.replace(/^動画：/, '')) + '" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></figure>';
    var imgs = ((attrs.match(/data-imgs="([^"]*)"/) || [])[1] || '').split(','), alts = ((attrs.match(/data-alts="([^"]*)"/) || [])[1] || '').split('|');
    var base = S.config.bodyImgBase == null ? 'img/body/' : S.config.bodyImgBase, show = !!S.config.showSlots, lab, ill;
    for (var i = 0; i < cells; i++) {
      lab = kind === 'steps' ? '工程 ' + (i + 1) : kind === 'beforeafter' ? (i ? 'AFTER' : 'BEFORE') : '';
      if (imgs[i]) {
        ill = /\.(png|svg)$/.test(imgs[i]); shown++;
        out += '<span class="st-imgslot__cell st-imgslot__cell--img' + (ill ? ' st-imgslot__cell--ill' : '') + '" style="aspect-ratio:' + ratio + '">' + (ill ? '<a href="' + esc(base + imgs[i]) + '" target="_blank" rel="noopener" aria-label="図を拡大して表示">' : '') + '<img src="' + esc(base + imgs[i]) + '" alt="' + esc(alts[i] || (cap + (lab ? '（' + lab + '）' : n > 1 ? '（' + (i + 1) + '）' : ''))) + '" loading="lazy" decoding="async">' + (ill ? '</a>' : '') + (lab && !ill ? '<span class="st-imgslot__tag">' + lab + '</span>' : '') + '</span>';
        continue;
      }
      if (!show) continue;
      shown++;
      out += '<span class="st-imgslot__cell" style="aspect-ratio:' + ratio + '">' + icon('image') + '<span>' + (kind === 'steps' ? '工程 ' + (i + 1) : kind === 'beforeafter' ? (i ? 'AFTER' : 'BEFORE') : kind === 'gallery' ? '写真 ' + (i + 1) : kind === 'diagram' ? '図解を準備中' : '画像を準備中') + '</span></span>';
    }
    if (!shown) return '';
    var done = imgs.filter(Boolean).length, allIll = done && imgs.filter(Boolean).every(function (f) { return /\.(png|svg)$/.test(f); });
    var capText = (done && !show) ? cap.replace(/^(図解|手順写真|写真)[：:]\s*/, '').replace(/写真/g, allIll ? '' : '写真').replace(/[（(]\d+枚[）)]|（ビフォーアフター推奨）|[：:]\s*写真\d+点（ギャラリー）|（\d+パターン）|（施工例・製品写真）|（施工例）/g, '').trim() : cap;
    return '<figure class="st-imgslot st-imgslot--' + kind + (done ? ' st-imgslot--filled' : '') + (allIll ? ' st-imgslot--ill' : '') + '" data-cells="' + shown + '"><div class="st-imgslot__grid">' + out + '</div>' + (allIll ? '' : '<figcaption>' + icon('image') + esc(capText) + '</figcaption>') + '</figure>';
  }

  S.slotHTML = slotHTML;
  S.colBody = function (a) {
    var re = /(<h2>[\s\S]*?<\/h2>|<h3>[\s\S]*?<\/h3>|<p>[\s\S]*?<\/p>|<ul>[\s\S]*?<\/ul>|<ol>[\s\S]*?<\/ol>|<table>[\s\S]*?<\/table>|<figure class="st-slot"[^>]*>[\s\S]*?<\/figure>|<div class="st-faq">[\s\S]*?<\/div>\x3c!--\/faq-->)/g;
    var body = a.body.replace(/\{\{col:([a-z0-9-]+)\}\}/g, function (_, sl) { var t = S.colBySlug(sl); return esc(href(t ? S.colPath(t) : '/column/')); }).replace(/__CHEV__/g, icon('chevD')).replace(/<a href="\/column\//g, '<a class="st-a" href="/column/').replace(/<a href="#/g, '<a class="st-a" href="#');
    var parts = body.match(re) || [], out = [], toc = [], h2n = 0, h3n = 0, inWrap = false, relInserted = false, rel = S.colRelated(a);
    function insertRel() {
      if (relInserted || !rel.same[0]) return; relInserted = true;
      out.push(S.InlineRelated({ article: S.colCard(rel.same[0]), label: 'あわせて読みたい' }));
    }
    parts.forEach(function (p, idx) {
      var m;
      if ((m = /^<h2>([\s\S]*?)<\/h2>$/.exec(p))) {
        var t = strip(m[1]), id = 's' + (++h2n);
        if (inWrap) { out.push('</section>'); inWrap = false; }
        if (h2n === 1) { out.push('<div class="st-qhead"><span class="st-qhead__label">' + icon('chat') + esc(pick('intro', a.id)) + '</span><h2 class="st-qhead__title" id="' + id + '">' + esc(t) + '</h2></div>'); toc.push({ id: id, text: t }); return; }
        if (/^結論[：:]/.test(t)) { var tt = t.replace(/^結論[：:]\s*/, ''); out.push('<section class="st-answer" aria-labelledby="' + id + '"><p class="st-answer__label">' + icon('bulb') + esc(pick('answer', a.id)) + '</p><h2 class="st-answer__title" id="' + id + '">' + esc(tt) + '</h2>'); inWrap = true; toc.push({ id: id, text: pick('answer', a.id) + '：' + tt }); return; }
        if (/^まとめ/.test(t)) { insertRel(); out.push('<section class="st-wrap st-wrap--col" aria-labelledby="' + id + '"><h2 class="st-wrap__title" id="' + id + '">' + esc(pick('wrap', a.id)) + '</h2>'); inWrap = true; toc.push({ id: id, text: pick('wrap', a.id) }); return; }
        var mod = '', lab = '', pm;
        if (/^よくある質問/.test(t)) { out.push('<h2 class="st-h2 st-h2--faq" id="' + id + '"><span class="st-h2__tag">' + icon('chat') + esc(pick('faq', a.id)) + '</span>' + esc(t === 'よくある質問' ? '気になる疑問に答えます' : t) + '</h2>'); toc.push({ id: id, text: 'よくある質問' }); return; }
        if ((pm = /^(基礎知識|詳細解説|比較・判断基準)[：:]\s*(.+)$/.exec(t))) {
          var k = pm[1] === '基礎知識' ? 'basic' : pm[1] === '詳細解説' ? 'detail' : 'judge';
          out.push('<h2 class="st-h2 st-h2--' + k + '" id="' + id + '"><span class="st-h2__tag">' + icon(k === 'basic' ? 'book' : k === 'detail' ? 'search' : 'scale') + esc(pick(k, a.id + h2n)) + '</span>' + esc(pm[2]) + '</h2>');
          toc.push({ id: id, text: pm[2] }); return;
        }
        if (t === '注意点') t = pick('caution', a.id + 1) === '注意' ? '注意しておきたいこと' : '失敗しないための注意点';
        if (t === '比較・判断基準') t = '比較と判断の基準';
        if (/注意|リスク|失敗|後悔/.test(t)) { mod = 'caution'; lab = pick('caution', a.id); insertRel(); }
        else if (/比較|違い/.test(t) || /^<table>/.test(parts[idx + 1] || '') || /^<table>/.test(parts[idx + 2] || '')) { mod = 'compare'; lab = pick('compare', a.id); }
        out.push('<h2 class="st-h2' + (mod ? ' st-h2--' + mod : '') + '" id="' + id + '">' + (lab ? '<span class="st-h2__tag">' + icon(mod === 'caution' ? 'alert' : 'scale') + esc(lab) + '</span>' : '') + esc(t) + '</h2>');
        toc.push({ id: id, text: t });
        return;
      }
      if ((m = /^<h3>([\s\S]*?)<\/h3>$/.exec(p))) { var hid = 'h' + (++h3n); out.push('<h3 class="st-h3" id="' + hid + '">' + m[1] + '</h3>'); if (toc.length) (toc[toc.length - 1].children = toc[toc.length - 1].children || []).push({ id: hid, text: strip(m[1]) }); return; }
      if (/^<ul>/.test(p)) { out.push(p.replace('<ul>', '<ul class="st-ul">')); return; }
      if (/^<ol>/.test(p)) { out.push(p.replace('<ol>', '<ol class="st-olist">')); return; }
      if (/^<table>/.test(p)) { out.push('<div class="st-table"><p class="st-table__hint" aria-hidden="true">← 横にスクロールできます →</p><div class="st-table__scroll" tabindex="0" role="region" aria-label="比較表">' + p + '</div></div>'); return; }
      if (/^<div class="st-faq">/.test(p)) { out.push(p.replace('\x3c!--/faq-->', '')); return; }
      if ((m = /^<figure class="st-slot"([^>]*)><figcaption>([\s\S]*?)<\/figcaption><\/figure>$/.exec(p))) { out.push(slotHTML(m[1], m[2])); return; }
      out.push(p);
    });
    if (inWrap) out.push('</section>');
    return { html: '<div class="st-body st-body--col">' + out.join('') + '</div>', toc: toc };
  };

  /* ================= SEO helpers ================= */
  S.colSeo = function (a, origin) {
    origin = origin || 'https://sotorino.jp';
    var url = origin + S.colPath(a), d = a.date.replace(/\./g, '-');
    return {
      title: a.title + '｜SOTORINO',
      description: a.metaDescription,
      url: url,
      image: origin + '/' + S.colThumbBase.replace(/^\//, '') + a.slug + '.jpg',
      article: { '@context': 'https://schema.org', '@type': 'Article', headline: a.title, description: a.metaDescription, datePublished: d, dateModified: d, image: [origin + '/img/col/' + a.slug + '.jpg'], author: { '@type': 'Organization', name: 'SOTORINO編集部', url: origin + '/about/' }, publisher: { '@type': 'Organization', name: 'SOTORINO', logo: { '@type': 'ImageObject', url: origin + '/img/logo.png' } }, mainEntityOfPage: url, articleSection: S.colCat(a.cat).full },
      faq: (a.faq && a.faq.length) ? { '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: a.faq.map(function (q) { return { '@type': 'Question', name: q.question, acceptedAnswer: { '@type': 'Answer', text: q.answer } }; }) } : null,
      breadcrumb: { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: [{ '@type': 'ListItem', position: 1, name: 'HOME', item: origin + '/' }, { '@type': 'ListItem', position: 2, name: 'コラム', item: origin + '/column/' }, { '@type': 'ListItem', position: 3, name: a.title }] }
    };
  };

  /* ================= parts ================= */
  S.ColCatNav = function (p) {
    p = p || {}; var all = S.colAll();
    return '<nav class="st-colcats" aria-label="コラムのカテゴリ"><ul>' + (p.withAll ? '<li><a href="' + esc(href('/column/')) + '"' + (!p.current ? ' aria-current="page"' : '') + '>' + icon('book') + 'すべて<small>' + all.length + '</small></a></li>' : '') +
      S.colCats.map(function (c) { var n = all.filter(function (a) { return a.cat === c.key; }).length; return '<li><a href="' + esc(href(S.colCatPath(c.key))) + '"' + (p.current === c.key ? ' aria-current="page"' : '') + '>' + icon(c.icon) + esc(c.name) + '<small>' + n + '</small></a></li>'; }).join('') + '</ul></nav>';
  };
  S.ColGrid = function (list, opt) { opt = opt || {}; return '<ul class="st-grid' + (opt.cols === 3 ? ' st-grid--3' : '') + ' st-colgrid">' + list.map(function (a, i) { var html = S.ArticleCard({ article: S.colCard(a), desc: opt.desc }); if (opt.eager && i < (opt.eager || 0)) html = html.replace('loading="lazy"', 'fetchpriority="high"'); return '<li>' + html + '</li>'; }).join('') + '</ul>'; };
  S.Pagination = function (cur, total) {
    if (total <= 1) return '';
    var o = '<nav class="st-pager" aria-label="ページ送り"><ul>';
    if (cur > 1) o += '<li><a href="' + esc(href(S.colPagePath(cur - 1))) + '" rel="prev">' + icon('chevL') + '<span>前へ</span></a></li>';
    for (var i = 1; i <= total; i++) o += '<li><a href="' + esc(href(S.colPagePath(i))) + '"' + (i === cur ? ' aria-current="page"' : '') + '>' + i + '</a></li>';
    if (cur < total) o += '<li><a href="' + esc(href(S.colPagePath(cur + 1))) + '" rel="next"><span>次へ</span>' + icon('chevR') + '</a></li>';
    return o + '</ul></nav>';
  };
  S.ColHero = function (p) {
    return '<section class="st-colhero"><div class="st-container"><p class="st-cathero__eyebrow">' + esc(p.en || 'COLUMN') + '</p><h1 class="st-colhero__title">' + esc(p.title) + '</h1><p class="st-colhero__text">' + esc(p.text) + '</p>' + (p.nav || '') + '</div></section>';
  };

  /* ================= pages ================= */
  var PER = 12;
  S.ColumnListPage = function (page) {
    var all = S.colAll().slice().sort(function (a, b) { return b.date < a.date ? -1 : b.date > a.date ? 1 : b.id - a.id; });
    var total = Math.ceil(all.length / PER), cur = Math.min(Math.max(1, page || 1), total), list = all.slice((cur - 1) * PER, cur * PER);
    var feat = S.colAll().filter(function (a) { return a.featured; }).slice(0, 4);
    return '<div class="st">' + S.Header({ active: 'column' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: 'コラム' + (cur > 1 ? '（' + cur + 'ページ目）' : '') }] }) + '<main id="main">' +
      S.ColHero({ title: '家まわりのコラム', text: '外構・庭づくり・DIYから、住宅設備、リフォーム、土地選び、補助金やお金、季節のメンテナンスまで。家まわりの「知りたい」を' + S.colAll().length + '本の記事で解説しています。', nav: S.ColCatNav({ withAll: true }) }) +
      '<div class="st-container">' + (cur === 1 ? '<section class="st-section" aria-labelledby="cf-t">' + S.SectionHeading({ title: 'よく読まれているコラム', en: 'Pick up', id: 'cf-t' }) + S.ColGrid(feat, { eager: 4 }) + '</section>' : '') +
      '<section class="st-section" aria-labelledby="cl-t">' + S.SectionHeading({ title: cur === 1 ? '新着コラム' : 'コラム一覧（' + cur + '/' + total + 'ページ）', en: 'Latest', id: 'cl-t' }) + S.ColGrid(list, { desc: true, eager: cur === 1 ? 0 : 4 }) + S.Pagination(cur, total) + '</section>' +
      '<section class="st-section st-band st-band--last" aria-labelledby="cc-t">' + S.SectionHeading({ title: 'カテゴリから探す', en: 'Category', id: 'cc-t' }) + S.ColCatCards() + '</section></div></main>' + S.Footer() + '</div>';
  };
  S.ColCatCards = function () {
    var all = S.colAll();
    return '<ul class="st-colcatcards">' + S.colCats.map(function (c) {
      var n = all.filter(function (a) { return a.cat === c.key; }).length;
      return '<li><a href="' + esc(href(S.colCatPath(c.key))) + '">' + media(c.img, '', '32') + '<span class="st-colcatcards__body"><span class="st-colcatcards__name">' + icon(c.icon) + esc(c.full) + '</span><span class="st-colcatcards__desc">' + esc(c.desc.slice(0, 54)) + '…</span><span class="st-colcatcards__n">' + n + '本の記事' + icon('arrow') + '</span></span></a></li>';
    }).join('') + '</ul>';
  };
  S.ColumnCategoryPage = function (key) {
    var c = S.colCat(key), list = S.colAll().filter(function (a) { return a.cat === c.key; });
    var start = list.filter(function (a) { return a.featured; }).concat(list).filter(function (a, i, arr) { return arr.indexOf(a) === i; }).slice(0, 3);
    return '<div class="st">' + S.Header({ active: 'column' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: 'コラム', path: '/column/' }, { name: c.full }] }) + '<main id="main">' +
      S.ColHero({ en: 'CATEGORY', title: c.full, text: c.desc, nav: S.ColCatNav({ withAll: true, current: c.key }) }) +
      '<div class="st-container"><section class="st-section" aria-labelledby="cs-t">' + S.SectionHeading({ title: 'まずはここから', en: 'Start here', id: 'cs-t' }) + S.ColGrid(start, { cols: 3, desc: true, eager: 3 }) + '</section>' +
      '<section class="st-section" aria-labelledby="ca-t">' + S.SectionHeading({ title: c.name + 'の記事一覧（' + list.length + '本）', en: 'All articles', id: 'ca-t' }) +
      '<ol class="st-colindex">' + list.map(function (a) { return '<li><a href="' + esc(href(S.colPath(a))) + '"><span class="st-colindex__no">' + ('00' + a.id).slice(-3) + '</span><span class="st-colindex__title">' + esc(a.title) + '<small>' + esc(a.excerpt) + '</small></span>' + icon('chevR') + '</a></li>'; }).join('') + '</ol></section>' +
      '<section class="st-section st-band st-band--last" aria-labelledby="co-t">' + S.SectionHeading({ title: 'ほかのカテゴリ', en: 'Category', id: 'co-t' }) + S.ColCatCards() + '</section></div></main>' + S.Footer() + '</div>';
  };
  var NEXT2 = {
    _: { step: 'NEXT', icon: 'coins', title: '費用の考え方を知る', desc: '費用が決まる仕組みと、見積もりで確認すべき項目。', path: '/column/gaikou-koji-hiyou-souba/', go: '費用の記事を読む' },
    equipment: { step: 'NEXT', icon: 'yen', title: '設備交換の補助金を確認', desc: '給湯器・窓などの省エネ設備は補助の対象になることも。', path: '/column/kyuto-shoene2026/', go: '補助金の記事を読む' },
    reform: { step: 'NEXT', icon: 'yen', title: '補助金・減税を確認する', desc: 'リフォームで使える国と自治体の制度をまとめました。', path: '/column/jutaku-shoene2026/', go: '補助金の記事を読む' },
    realestate: { step: 'NEXT', icon: 'alert', title: '購入前のチェックリスト', desc: '現地調査で見るべき15のポイントを確認しましょう。', path: '/column/tochi-kounyu-chuiten/', go: 'チェック項目を見る' },
    money: { step: 'NEXT', icon: 'house', title: 'リフォーム費用の相場を知る', desc: '補助金を使う前に、工事ごとの費用感をつかみましょう。', path: '/column/kitchen-reform-hiyou/', go: '費用の記事を読む' },
    lifestyle: { step: 'NEXT', icon: 'calendar', title: '年間の手入れを計画する', desc: '春夏秋冬に何をすればいいか、カレンダーで確認。', path: '/column/niwa-teire-nenkan-calendar/', go: 'カレンダーを見る' }
  };
  S.ColumnArticlePage = function (slug) {
    var a = S.colBySlug(slug); if (!a) return S.ColumnListPage(1);
    var c = S.colCat(a.cat), b = S.colBody(a), rel = S.colRelated(a), card = S.colCard(a);
    var catList = S.colAll().filter(function (x) { return x.cat === a.cat; });
    var feat = S.colAll().filter(function (x) { return x.featured && x.id !== a.id; }).slice(0, 4);
    return '<div class="st">' + S.Header({ active: 'column' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: 'コラム', path: '/column/' }, { name: a.title }] }) +
      '<div class="st-container"><div class="st-article-wrap"><main id="main"><article>' +
      '<header class="st-ahead"><div class="st-ahead__meta"><a class="st-colcat-link" href="' + esc(href(S.colCatPath(c.key))) + '">' + S.CategoryLabel('col-' + a.cat) + '</a>' + S.Date({ date: a.date }) + '</div>' +
      '<h1 class="st-ahead__title">' + esc(a.title) + '</h1><p class="st-ahead__lead">' + esc(a.excerpt) + '</p>' +
      '<p class="st-ahead__byline">' + icon('user') + '<span>執筆：<a href="' + esc(href('/about/editors/')) + '">SOTORINO編集部</a></span></p>' +
      '<figure class="st-ahead__hero"><span class="st-media st-r-hero">' + img('col-' + a.slug, a.title, { eager: true }) + '</span></figure>' + S.ShareBar({ id: 'col' + a.id, title: a.title, path: S.colPath(a) }) + '</header>' +
      (b.toc.length > 2 ? '<div class="st-intro st-intro--col">' + S.TableOfContents({ items: b.toc }) + '</div>' : '') + b.html +
      (a.tags && a.tags.length ? '<div class="st-block">' + S.TagList({ tags: a.tags }) + '</div>' : '') +
      '<div class="st-block">' + S.NextSteps({ items: [
        { step: 'NEXT', icon: 'book', title: c.name + 'の記事をもっと読む', desc: c.desc.slice(0, 40) + '…', path: S.colCatPath(c.key), go: 'カテゴリを見る' },
        (NEXT2[a.cat] || NEXT2._),
        { step: 'NEXT', icon: 'user', title: 'プロに相談したい', desc: '施工会社の比較ポイントと無料見積もりの使い方。', path: '/purpose/contractors/', go: '業者の選び方を見る' }] }) + '</div>' +
      (a.sources && a.sources.length ? '<aside class="st-block st-sources" aria-label="参考情報・確認事項"><p class="st-sources__title">' + icon('info') + '参考情報・確認事項</p><ul>' + a.sources.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul></aside>' : '') +
      '<div class="st-block">' + S.AuthorBox({ name: 'SOTORINO編集部', role: '執筆', initial: 'S', bio: '外構・庭づくり・住まいに関する情報を、根拠と条件を添えてわかりやすくお届けしています。※ 監修者を立てる記事は、監修者の資格と確認範囲を掲載します。' }) + '</div>' +
      '</article>' +
      '<section class="st-block" aria-labelledby="crel-t"><div class="st-endhead"><h2 id="crel-t">関連記事</h2>' + S.More({ href: S.colCatPath(c.key), label: c.name + 'の記事一覧' }) + '</div>' + S.ColGrid(rel.same.slice(0, 3), { cols: 3 }) + '</section>' +
      (rel.cross.length ? '<section class="st-block" aria-labelledby="cx-t"><div class="st-endhead"><h2 id="cx-t">ほかのカテゴリの関連記事</h2></div><ul class="st-endlist">' + rel.cross.map(function (x) { return '<li><a href="' + esc(href(S.colPath(x))) + '"><span>' + esc(x.title) + '</span>' + S.CategoryLabel('col-' + x.cat) + '</a></li>'; }).join('') + '</ul></section>' : '') +
      '</main><aside class="st-side" aria-label="サイドバー">' +
      S.CTABanner({ title: '理想の外構を<br>プロとつくる', text: '外構工事の無料見積もりはこちら', cta: '無料で相談する', img: 'photo-black-house-light' }) +
      '<section class="st-box" aria-labelledby="sc-t"><h2 class="st-box__title" id="sc-t">' + icon('layers') + esc(c.name) + '</h2><ul class="st-sidecol">' + catList.slice(0, 15).map(function (x) { return '<li><a href="' + esc(href(S.colPath(x))) + '"' + (x.id === a.id ? ' aria-current="page"' : '') + '>' + esc(x.title) + '</a></li>'; }).join('') + '</ul>' + S.More({ href: S.colCatPath(c.key), label: 'すべて見る' }) + '</section>' +
      '<section class="st-box" aria-labelledby="sf-t"><h2 class="st-box__title" id="sf-t">' + icon('leaf') + '編集部のおすすめ</h2><ul class="st-sidelist">' + feat.map(function (x) { return '<li>' + S.ArticleCard({ article: S.colCard(x), variant: 'mini', headingLevel: 'span' }) + '</li>'; }).join('') + '</ul></section>' +
      S.ConsultBox() + (b.toc.length > 2 ? '<div class="st-sticky">' + S.MiniTOC({ items: b.toc }) + '</div>' : '') +
      '</aside></div></div>' + S.Footer() + '</div>';
  };
})();

/* ================= site categories ⇄ columns ================= */
(function () {
  'use strict';
  var S = window.Sotorino, esc = S.esc, href = S.href, icon = S.icon, media = S.media;
  // Each site category: keyword rules on the column title (and a fallback by column category).
  S.siteCatRules = {
    garden:     { kw: /庭|芝|花壇|植物|低木|シンボルツリー|ガーデン|雑草|防草|苔|虫|ペット|小道|土(?!地)|砂利|レンガ|舗装材|地面/, cats: ['garden'],
                  intro: '人工芝・天然芝、花壇、植栽、砂利、雑草対策まで。暮らしに合う庭をつくるための記事をまとめました。' },
    exterior:   { kw: /外構|エクステリア|フェンス|目隠し|塀|ブロック|門扉|ポスト|アプローチ|タイル|レンガ|舗装|オープン|クローズ|防犯|プライバシー|動線|施工事例|境界/, cats: ['basics'],
                  intro: 'フェンス・目隠し・門まわり・舗装など外構全般の基礎知識と選び方、費用や失敗例までをまとめました。' },
    carport:    { kw: /カーポート|駐車場|コンクリート|インターロッキング/, cats: [],
                  intro: 'カーポートの種類と屋根材、駐車場のコンクリート・インターロッキング、費用とひび割れ対策の記事です。' },
    deck:       { kw: /デッキ|テラス/, cats: [],
                  intro: '天然木・人工木・タイルデッキの違い、DIYでの作り方、設置費用、劣化を防ぐメンテナンスの記事です。' },
    equipment:  { kw: /宅配ボックス|立水栓|物置|ガーデンライト|ポスト|門扉|照明|給湯|エコキュート|食洗機|浴室乾燥|トイレ|コンロ|スマートキー|太陽光|蓄電池|換気/, cats: ['equipment'],
                  intro: 'エコキュート・給湯器・食洗機・トイレなどの住宅設備から、宅配ボックス・立水栓・ガーデンライトなど外まわりの設備まで。寿命や交換時期、選び方と費用の記事をまとめました。' },
    reform:     { kw: /リフォーム|入れ替え|段差|交換|張り替え|修理|塗装|建て替え/, cats: ['reform'],
                  intro: 'キッチン・浴室・トイレの水まわり、外壁・屋根塗装、玄関ドアや窓、外構のリフォームまで。費用相場と工事内容、失敗しない進め方の記事をまとめました。' },
    realestate: { kw: /新築|土地|地盤|境界|旗竿|角地|建ぺい|容積|接道|セットバック|ハザード|古家|中古住宅/, cats: ['realestate'],
                  intro: '土地選びのチェックポイント、旗竿地・角地、建ぺい率や接道義務、地盤・境界・ハザードマップ、新築時の外構計画まで。家を建てる・買う前に読みたい記事です。' },
    money:      { kw: /予算|見積もり|補助金|助成金|お得|安く|抑え|ローン|減税|保険|支払い|キャンペーン/, cats: ['cost', 'money'],
                  intro: '住宅省エネの補助金、自治体の助成制度、リフォームローンや減税、火災保険、外構・リフォームの費用相場と見積もりの見方まで。家まわりのお金の記事をまとめました。' },
    life:       { kw: /メンテナンス|DIY|工具|寿命|長持ち|劣化|カビ|苔|虫|水はけ|水たまり|水浸し|ぬかるむ|枯れる|ひび割れ|傾く|失敗|結露|台風|剪定|雨どい|凍結|掃除|手入れ/, cats: ['diy', 'trouble', 'lifestyle'],
                  intro: '結露・カビ・台風・凍結など季節の備え、庭木の剪定や雨どい掃除、DIYの手順、トラブルの対処と年間メンテナンスまで。暮らしの知恵をまとめました。' }
  };
  S.colSiteCats = function (a) {
    var out = [];
    for (var k in S.siteCatRules) { var r = S.siteCatRules[k]; if (r.kw.test(a.title) || r.cats.indexOf(a.cat) > -1) out.push(k); }
    return out;
  };
  S.colForSiteCat = function (id) {
    var list = S.colAll().filter(function (a) { return S.colSiteCats(a).indexOf(id) > -1; });
    var r = S.siteCatRules[id];
    // titles that match the keywords come first, then fallbacks; featured first within each
    return list.sort(function (x, y) { var tx = (r.cats.indexOf(x.cat) > -1 ? 0 : 1) + (r.kw.test(x.title) ? 0 : 1), ty = (r.cats.indexOf(y.cat) > -1 ? 0 : 1) + (r.kw.test(y.title) ? 0 : 1); return (tx - ty) || ((y.featured ? 1 : 0) - (x.featured ? 1 : 0)) || (x.id - y.id); });
  };
  S.SiteCategoryPage = function (c) {
    var r = S.siteCatRules[c.id], cols = r ? S.colForSiteCat(c.id) : [];
    var own = S.data.articles.filter(function (a) { return a.cat === c.id || (c.id === 'garden' && a.cat === 'turf') || (c.id === 'exterior' && (a.cat === 'carport' || a.cat === 'deck')); }).map(function (a) { return a.id; });
    var byCol = {}; cols.forEach(function (a) { (byCol[a.cat] = byCol[a.cat] || []).push(a); });
    var groups = S.colCats.filter(function (cc) { return byCol[cc.key]; }); if (r) groups.sort(function (x, y) { return (r.cats.indexOf(x.key) > -1 ? 0 : 1) - (r.cats.indexOf(y.key) > -1 ? 0 : 1); });
    var img = (S.data.categories.filter(function (x) { return x.id === c.id; })[0] || {}).img;
    return '<div class="st">' + S.Header({ active: c.id }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: c.name }] }) + '<main id="main">' +
      '<section class="st-colhero"><div class="st-container st-sitecat__hero"><div><p class="st-cathero__eyebrow">CATEGORY</p><h1 class="st-colhero__title">' + esc(c.name) + '</h1><p class="st-colhero__text">' + esc(r ? r.intro : '') + '</p>' +
      (groups.length ? '<nav class="st-colcats" aria-label="このカテゴリのテーマ"><ul>' + groups.map(function (g) { return '<li><a href="#sc-' + g.key + '">' + icon(g.icon) + esc(g.name) + '<small>' + byCol[g.key].length + '</small></a></li>'; }).join('') + '</ul></nav>' : '') + '</div>' +
      (img ? '<div class="st-sitecat__img">' + media(img, '', '43') + '</div>' : '') + '</div></section>' +
      '<div class="st-container">' +
      (own.length ? '<section class="st-section" aria-labelledby="so-t">' + S.SectionHeading({ title: '特集・新着記事', en: 'Feature', id: 'so-t' }) + S.LatestGrid({ items: own, desc: true }) + '</section>' : '') +
      (cols.length ? '<section class="st-section" aria-labelledby="sk-t">' + S.SectionHeading({ title: 'まずはここから', en: 'Start here', id: 'sk-t' }) + S.ColGrid(cols.slice(0, 4), { desc: true }) + '</section>' +
        groups.map(function (g) {
          return '<section class="st-section st-sitecat__group" id="sc-' + g.key + '" aria-labelledby="sg-' + g.key + '">' + S.SectionHeading({ title: g.name, en: 'Column', more: S.colCatPath(g.key), id: 'sg-' + g.key }) +
            '<ol class="st-colindex">' + byCol[g.key].map(function (a) { return '<li><a href="' + esc(href(S.colPath(a))) + '"><span class="st-colindex__no">' + ('00' + a.id).slice(-3) + '</span><span class="st-colindex__title">' + esc(a.title) + '<small>' + esc(a.excerpt) + '</small></span>' + icon('chevR') + '</a></li>'; }).join('') + '</ol></section>';
        }).join('') : '<p class="st-section">このカテゴリのコラムは準備中です。</p>') +
      '<section class="st-section st-band st-band--last" aria-labelledby="sx-t">' + S.SectionHeading({ title: 'コラムをカテゴリから探す', en: 'Column', more: '/column/', id: 'sx-t' }) + S.ColCatCards() + '</section>' +
      '</div></main>' + S.Footer() + '</div>';
  };
})();
