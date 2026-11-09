// SOTORINO build: src/ + content/ + ../images  ->  public/
// 使い方: node scripts/build.mjs   （Node.js 18以上。追加パッケージ不要）
import fs from 'node:fs'; import path from 'node:path'; import { fileURLToPath } from 'node:url';
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const P = (...a) => path.join(ROOT, ...a);
const IMAGES = process.env.SOTORINO_IMAGES || P('..', 'images');

// 1) JS bundle = 3ファイルを連結（画像は index.html / SSG 側の setImages で登録するので空で埋める）
const js = fs.readFileSync(P('src/bundle.src.js'), 'utf8').replace('__IMAGES__', '{}') + '\n' +
  fs.readFileSync(P('src/bundle.more.js'), 'utf8') + '\n' + fs.readFileSync(P('src/bundle.column.js'), 'utf8') + '\n' + fs.readFileSync(P('src/bundle.pages.js'), 'utf8');
if (/<\/script|<!--/i.test(js)) throw new Error('bundle に </script または <!-- が含まれています');
fs.writeFileSync(P('public/sotorino.js'), js);

// 2) CSS
fs.copyFileSync(P('src/sotorino.css'), P('public/sotorino.css'));

// 3) tokens.json -> tokens.css（CSSカスタムプロパティ）
const tok = JSON.parse(fs.readFileSync(P('src/tokens.json'), 'utf8'));
const out = [':root, [data-theme="light"] {'];
for (const t of tok.color.tokens) { const v = typeof t.value === 'string' ? t.value : t.value.light; const m = /^\{(.+)\}$/.exec(v); out.push(`  --${t.name}: ${m ? `var(--${m[1]})` : v};`); }
for (const t of tok.shadow.tokens) out.push(`  --${t.name}: ${t.value};`);
out.push('}', ':root {');
for (const fam of ['spacing', 'radius', 'size']) for (const t of tok[fam].tokens) out.push(`  --${t.name}: ${t.value};`);
for (const [k, v] of Object.entries(tok.type.families)) out.push(`  --font-${k}: ${v};`);
out.push('}');
fs.writeFileSync(P('public/tokens.css'), out.join('\n') + '\n');

// 本文の画像枠：images/08_body/{slug}-{連番}.(jpg|png|webp|svg) があれば、その枠に自動で画像を入れる
//   images/08_body/alt.json に {"ファイル名": "代替テキスト"} を書くと alt に使う
const BODY = path.join(IMAGES, '08_body');
const bodyFiles = fs.existsSync(BODY) ? new Set(fs.readdirSync(BODY)) : new Set();
const bodyAlt = fs.existsSync(path.join(BODY, 'alt.json')) ? JSON.parse(fs.readFileSync(path.join(BODY, 'alt.json'), 'utf8')) : {};
let bodyHit = 0;
function findBody(stem) { for (const e of ['.jpg', '.png', '.webp', '.svg']) if (bodyFiles.has(stem + e)) return stem + e; return ''; }
function injectBody(slug, body) {
  let seq = 0;
  return String(body).replace(/<figure class="st-slot"([^>]*)>/g, (m, attrs) => {
    const kind = (attrs.match(/data-kind="([^"]+)"/) || [])[1] || 'photo', n = +((attrs.match(/data-n="(\d+)"/) || [])[1] || 1);
    const cells = kind === 'photo' || kind === 'diagram' ? 1 : Math.min(n, kind === 'beforeafter' ? 2 : 8), names = [];
    for (let i = 0; i < n; i++) { seq++; const f = findBody(`${slug}-${String(seq).padStart(2, '0')}`); names.push(i < cells ? f : ''); }
    if (!names.some(Boolean)) return m;
    bodyHit += names.filter(Boolean).length;
    const alts = names.map(f => (bodyAlt[f] || '').replace(/[|"<>]/g, ''));
    return `<figure class="st-slot"${attrs} data-imgs="${names.join(',')}" data-alts="${alts.join('|')}">`;
  });
}
// 4) 記事データ columns.json -> columns.js
const cols = JSON.parse(fs.readFileSync(P('content/columns.json'), 'utf8'));
const keep = ['id', 'slug', 'title', 'metaDescription', 'excerpt', 'body', 'cat', 'catName', 'date', 'featured', 'tags', 'slots', 'links', 'faq', 'sources'];
const slim = cols.map(a => Object.fromEntries(keep.filter(k => k in a).map(k => [k, k === 'body' ? injectBody(a.slug, a[k]) : a[k]])));
const cjs = 'window.SOTORINO_COLUMNS = ' + JSON.stringify(slim) + ';\n';
if (/<\/script/i.test(cjs)) throw new Error('記事本文に </script が含まれています');
fs.writeFileSync(P('public/columns.js'), cjs);

// 5) 画像を public/img/ にフラットにコピー（コラムのサムネは public/img/col/）
const copyDir = (src, dst, flat) => { if (!fs.existsSync(src)) return 0; let n = 0; fs.mkdirSync(dst, { recursive: true });
  for (const e of fs.readdirSync(src, { withFileTypes: true })) { const s = path.join(src, e.name);
    if (e.isDirectory()) n += copyDir(s, flat ? dst : path.join(dst, e.name), flat);
    else if (/\.(jpe?g|png|webp|svg)$/i.test(e.name)) { fs.copyFileSync(s, path.join(dst, e.name)); n++; } } return n; };
let n = 0;
for (const d of ['01_photos', '02_tentative-in-use', '03_logo']) n += copyDir(path.join(IMAGES, d), P('public/img'), true);
n += copyDir(path.join(IMAGES, '04_column-thumbnails'), P('public/img/col'), true);
// 6) 固定ページ・ガイド記事 content/pages.json -> pages.js（専用画像 images/07_pages/{key}.jpg があればそれを使う）
const pages = JSON.parse(fs.readFileSync(P('content/pages.json'), 'utf8'));
const PIMG = path.join(IMAGES, '07_pages');
for (const p of pages) { if (fs.existsSync(path.join(PIMG, p.key + '.jpg'))) p.imgFile = 'page/' + p.key + '.jpg'; if (p.body) p.body = injectBody(p.key, p.body); }
n += copyDir(BODY, P('public/img/body'), true);
n += copyDir(PIMG, P('public/img/page'), true);
const extra = {}; for (const e of ['.jpg', '.png', '.webp']) if (fs.existsSync(path.join(PIMG, 'campaign-autumn-flyer' + e))) extra.flyer = 'page/campaign-autumn-flyer' + e;
const pjs = 'window.SOTORINO_PAGES = ' + JSON.stringify(pages) + ';\nwindow.SOTORINO_PAGE_EXTRA = ' + JSON.stringify(extra) + ';\n';
if (/<\/script/i.test(pjs)) throw new Error('pages.json に </script が含まれています');
fs.writeFileSync(P('public/pages.js'), pjs);

// 7) 検索用インデックス（静的ページでも全記事を検索できるように）
{
  const { createRequire } = await import('node:module'); const require = createRequire(import.meta.url);
  global.window = { matchMedia: () => ({ matches: false }) };
  for (const f of ['columns.js', 'pages.js', 'sotorino.js']) { delete require.cache[P('public', f)]; require(P('public', f)); }
  const S = global.window.Sotorino; S.colRegister('/img/col/'); S.pgRegister('/img/');
  const html = fs.readFileSync(P('public/index.html'), 'utf8'); const m = html.match(/S\.setImages\((\{.*?\})\);/s);
  if (m) { const im = JSON.parse(m[1]); for (const k in im) im[k] = '/' + im[k]; S.setImages(im); }
  const idx = S.searchIndex().map(x => ({ title: x.title, desc: x.desc, path: x.path, cat: x.cat, img: x.img, date: x.date, tags: x.tags }));
  const imgs = {}; idx.forEach(x => { if (S.images[x.img]) imgs[x.img] = S.images[x.img]; });
  fs.writeFileSync(P('public/search.js'), 'window.SOTORINO_SEARCH = ' + JSON.stringify(idx) + ';\nwindow.SOTORINO_SEARCH_IMAGES = ' + JSON.stringify(imgs) + ';\n');
  console.log(`本文画像: ${bodyHit}枚を配置`);
  console.log(`search index: ${idx.length}件 / pages ${pages.length}本`);
}
console.log(`build OK: sotorino.js ${(js.length / 1024) | 0}KB / columns ${cols.length}本 / 画像 ${n}枚 -> public/`);
