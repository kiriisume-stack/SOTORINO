// 静的書き出し: public/ の部品で全ページを HTML にして dist/ へ（本文入り・通常のURL・sitemap.xml・robots.txt・404.html）
// 使い方: node scripts/build.mjs && node scripts/ssg.cjs   （ドメイン変更: SITE_ORIGIN=https://example.com）
const fs = require('fs'), path = require('path');
global.window = { matchMedia: () => ({ matches: false }) }; global.document = undefined;
require('../public/columns.js'); require('../public/pages.js'); require('../public/sotorino.js');
const S = window.Sotorino, ORIGIN = process.env.SITE_ORIGIN || 'https://sotorino.jp', OUT = path.join(__dirname, '../dist');
const FORM = process.env.FORM_ENDPOINT || '';
const AFF = process.env.AFFILIATE === '1';   // アフィリエイト承認後に AFFILIATE=1 で書き出すと、商品ページ・商品カードが公開される
S.config.base = ''; S.config.bodyImgBase = '/img/body/'; S.config.siteOrigin = ORIGIN; if (FORM) S.config.formEndpoint = FORM; S.config.affiliate = AFF; S.config.prReady = process.env.PR_READY === '1'; S.config.logoSrc = '/img/logo.png';
/* 広告：content/ads.json（枠ID → 広告コード）があれば表示。AD_SLOTS=1 でコード未設定の枠に目印を表示 */
const ADS = fs.existsSync(path.join(__dirname, '..', 'content', 'ads.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'content', 'ads.json'), 'utf8')) : {};
S.config.ads = ADS; S.config.showAdSlots = process.env.AD_SLOTS === '1';
S.colRegister('/img/col/'); S.pgRegister('/img/');
const idx = fs.readFileSync(path.join(__dirname, '../public/index.html'), 'utf8');
const imgs = JSON.parse(idx.match(/S\.setImages\((\{.*?\})\);/s)[1]); for (const k in imgs) imgs[k] = '/' + imgs[k]; S.setImages(imgs);
const HAS = f => fs.existsSync(path.join(__dirname, '../public/img', f));
const OGP = HAS('ogp-default.jpg') ? '/img/ogp-default.jpg' : '/img/photo-house-dusk.jpg';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
/* アクセス解析・サーチコンソール：content/site.json（または環境変数 GA_ID / GSC_VERIFY）に値を入れると、全ページの<head>に入る。空なら何も出さない */
const SITE = fs.existsSync(path.join(__dirname, '..', 'content', 'site.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'content', 'site.json'), 'utf8')) : {};
const GA_ID = (process.env.GA_ID || SITE.gaId || '').trim(), GSC = (process.env.GSC_VERIFY || SITE.gscVerification || '').trim();
if (GA_ID && !/^G-[A-Z0-9]+$/.test(GA_ID)) throw new Error('GA_ID は「G-」で始まる測定IDを入れてください: ' + GA_ID);
const ANALYTICS = (GSC ? `<meta name="google-site-verification" content="${esc(GSC)}">` : '') + (GA_ID ? `<script async src="https://www.googletagmanager.com/gtag/js?id=${GA_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','${GA_ID}');</script>` : '');

function page(html, seo) {
  const url = ORIGIN + seo.path, img = ORIGIN + (seo.image || OGP);
  return `<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
${ANALYTICS}<title>${esc(seo.title)}</title><meta name="description" content="${esc(seo.description)}"><link rel="canonical" href="${url}">
${seo.noindex ? '<meta name="robots" content="noindex,follow">' : ''}${seo.prev ? `<link rel="prev" href="${ORIGIN + seo.prev}">` : ''}${seo.next ? `<link rel="next" href="${ORIGIN + seo.next}">` : ''}
<meta property="og:site_name" content="SOTORINO"><meta property="og:locale" content="ja_JP"><meta property="og:type" content="${seo.og === 'article' ? 'article' : 'website'}"><meta property="og:title" content="${esc(seo.title)}"><meta property="og:description" content="${esc(seo.description)}"><meta property="og:url" content="${url}"><meta property="og:image" content="${img}"><meta name="twitter:card" content="summary_large_image">
${HAS('favicon.png') ? '<link rel="icon" href="/img/favicon.png">' : ''}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="/assets/tokens.css"><link rel="stylesheet" href="/assets/sotorino.css">
${seo.ld && seo.ld.length ? `<script type="application/ld+json">${JSON.stringify(seo.ld).replace(/</g, '\\u003c')}</script>` : ''}
</head><body>${html}<script src="/assets/search.js" defer></script><script src="/assets/sotorino.js" defer></script><script>addEventListener('DOMContentLoaded',function(){Sotorino.config.base='';Sotorino.config.bodyImgBase='/img/body/';Sotorino.config.formEndpoint=${JSON.stringify(FORM)};Sotorino.config.affiliate=${AFF};Sotorino.mount(document)})</script></body></html>`;
}
function write(rel, html) { const f = path.join(OUT, decodeURIComponent(rel), 'index.html'); fs.mkdirSync(path.dirname(f), { recursive: true }); fs.writeFileSync(f, html); }
fs.rmSync(OUT, { recursive: true, force: true });

const urls = [], miss = [];
for (const p of S.allPaths()) {
  const r = S.route(p);
  if (!r) { miss.push(p); continue; }
  write(p, page(r.html, r.seo));
  if (!r.seo.noindex) urls.push([p, r.seo.priority || '0.5', r.seo.lastmod]);
}
// 404
fs.writeFileSync(path.join(OUT, '404.html'), page(S.NotFoundPage(), { title: 'ページが見つかりません｜SOTORINO', description: 'お探しのページは見つかりませんでした。', path: '/404.html', noindex: true, ld: [] }));
// sitemap / robots
const enc = u => u.split('/').map(seg => /^[\x00-\x7f]*$/.test(seg) ? seg : encodeURIComponent(decodeURIComponent(seg))).join('/');
fs.writeFileSync(path.join(OUT, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
  urls.map(([u, pr, d]) => `  <url><loc>${ORIGIN}${enc(u)}</loc>${d ? `<lastmod>${d.replace(/\./g, '-')}</lastmod>` : ''}<priority>${pr}</priority></url>`).join('\n') + '\n</urlset>\n');
fs.writeFileSync(path.join(OUT, 'robots.txt'), `User-agent: *\nAllow: /\nDisallow: /search/\nSitemap: ${ORIGIN}/sitemap.xml\n`);
// assets & images
const cp = (a, b) => { fs.mkdirSync(path.dirname(b), { recursive: true }); fs.copyFileSync(a, b); };
for (const f of ['sotorino.css', 'sotorino.js', 'tokens.css', 'search.js']) cp(path.join(__dirname, '../public', f), path.join(OUT, 'assets', f));
fs.cpSync(path.join(__dirname, '../public/img'), path.join(OUT, 'img'), { recursive: true });
console.log('pages', S.allPaths().length - miss.length, '/ sitemap', urls.length, miss.length ? '/ 未出力 ' + miss.join(' ') : '', '-> dist/');
