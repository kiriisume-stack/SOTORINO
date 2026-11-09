// データの整合チェック（npm run build のあとに実行）: node scripts/check.cjs
const fs=require('fs'),path=require('path');
global.window={matchMedia:()=>({matches:false})};
require('../public/columns.js');require('../public/sotorino.js');
const S=window.Sotorino, all=S.colAll(), errs=[], warns=[];
const cats=new Set(S.colCats.map(c=>c.key));
const seen={slug:{},title:{},id:{}};
for(const a of all){
  for(const k of ['id','slug','title']){ if(seen[k][a[k]]) errs.push(`${k} が重複: ${a[k]}`); seen[k][a[k]]=1; }
  if(!/^[a-z0-9-]+$/.test(a.slug)) errs.push(`slug に使えない文字: ${a.slug}`);
  if(!cats.has(a.cat)) errs.push(`未定義のカテゴリ ${a.cat}: No.${a.id}`);
  if(!a.metaDescription) errs.push(`metaDescription なし: No.${a.id}`);
  if(!/^\d{4}\.\d{2}\.\d{2}$/.test(a.date)) errs.push(`date の形式: No.${a.id} ${a.date}`);
  for(const l of a.links||[]) if(!S.colBySlug(l)) errs.push(`links のスラッグが存在しない: No.${a.id} → ${l}`);
  for(const m of a.body.matchAll(/\{\{col:([^}]+)\}\}/g)) if(!S.colBySlug(m[1])) errs.push(`本文リンク先が存在しない: No.${a.id} → ${m[1]}`);
  if(!S.colSiteCats(a).length) warns.push(`どのサイトカテゴリにも載らない: No.${a.id} ${a.title}`);
  if(!fs.existsSync(path.join(__dirname,'../public/img/col',a.slug+'.jpg'))) warns.push(`サムネイルなし: ${a.slug}.jpg（npm run thumbs）`);
  const h=S.ColumnArticlePage(a.slug); if(/__CHEV__|\{\{col:|undefined/.test(h)) errs.push(`表示に未変換の文字: No.${a.id}`);
}
const keys=new Set(Object.keys(S.images));
console.log(`記事 ${all.length}本 / カテゴリ ${cats.size} / featured ${all.filter(a=>a.featured).length}本 / 画像枠 ${all.reduce((n,a)=>n+(a.body.match(/class="st-slot"/g)||[]).length,0)}か所`);
warns.forEach(w=>console.log('注意:',w)); errs.forEach(e=>console.log('エラー:',e));
console.log(errs.length?`NG（エラー ${errs.length}件）`:'OK'); process.exit(errs.length?1:0);
