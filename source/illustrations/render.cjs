// SVG → PNG（Noto CJK フォントで描画を固定するため PNG に書き出す）
// 使い方: node illustrations/render.cjs <svgディレクトリ> <出力ディレクトリ>
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const files = fs.readdirSync(src).filter(f => f.endsWith('.svg'));
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1.25 });
  for (const f of files) {
    const svg = fs.readFileSync(path.join(src, f), 'utf8');
    const m = svg.match(/viewBox="0 0 (\d+) (\d+)"/); const w = +m[1], h = +m[2];
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    await p.screenshot({ path: path.join(out, f.replace(/\.svg$/, '.png')), clip: { x: 0, y: 0, width: w, height: h } });
  }
  await b.close(); console.log('rendered', files.length);
})();
