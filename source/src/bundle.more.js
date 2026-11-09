(function () {
  'use strict';
  var S = window.Sotorino, esc = S.esc, href = S.href, icon = S.icon, img = S.img, media = S.media;
  function A(id) { return S.article(id); }
  function addArticles(list) { list.forEach(function (a) { if (!A(a.id)) S.data.articles.push(a); }); }

  /* ================= more content data ================= */
  addArticles([
    { id: 'trap-isshiki', cat: 'exterior', title: '見積もりの「一式」に要注意｜内訳の読み方', desc: '一式表記の項目は、追加費用の原因になりがち。', img: 'fence-design', date: '2026.10.27', path: '/exterior/trap/isshiki/', tags: ['外構', '見積もり'] },
    { id: 'trap-boundary', cat: 'exterior', title: '境界ギリギリのフェンスでお隣と気まずくならないために', desc: '設置位置と事前の声かけで防げるトラブル。', img: 'fence-privacy', date: '2026.10.19', path: '/exterior/trap/boundary/', tags: ['フェンス', '境界'] },
    { id: 'trap-hot-turf', cat: 'turf', title: '安い人工芝が真夏に熱くなる？素材と対策', desc: '表面温度が上がる理由と、選び方・使い方の工夫。', img: 'thumb-turf', date: '2026.10.15', path: '/garden/turf/hot/', tags: ['人工芝', '夏'] },
    { id: 'trap-drain', cat: 'exterior', title: '水はけを考えない土間コンクリートで庭が池に', desc: '勾配と排水計画の基本。', img: 'cat-carport', date: '2026.10.11', path: '/exterior/trap/drain/', tags: ['駐車場', '排水'] },
    { id: 'trap-subsidy', cat: 'money', title: '補助金は「着工前の申請」が条件のことが多い', desc: '申請のタイミングで使えなくなる前に確認すること。', img: 'thumb-subsidy', date: '2026.10.09', path: '/money/trap/subsidy-timing/', tags: ['補助金'] },
    { id: 'col-grow', cat: 'turf', title: '「芝、伸びてきました？」と聞かれる率、意外と高い説', desc: '人工芝職人が語る現場の本音 Vol.1', img: 'cat-garden', date: '2026.10.24', path: '/column/shiba/01/', tags: ['コラム', '人工芝'] },
    { id: 'col-gallery', cat: 'turf', title: '職人が一番緊張するのは、雨より“ご近所の見学ギャラリー”', desc: '人工芝職人が語る現場の本音 Vol.2', img: 'thumb-garden-care', date: '2026.10.17', path: '/column/shiba/02/', tags: ['コラム'] },
    { id: 'col-summer', cat: 'turf', title: '真夏の施工で学んだこと。人工芝の上で目玉焼きは焼けない（焼かないで）', desc: '人工芝職人が語る現場の本音 Vol.3', img: 'hero-03', date: '2026.10.10', path: '/column/shiba/03/', tags: ['コラム', '夏'] },
    { id: 'col-home', cat: 'turf', title: '職人の自宅の庭は人工芝なのか問題', desc: '人工芝職人が語る現場の本音 Vol.4', img: 'hero-01', date: '2026.10.03', path: '/column/shiba/04/', tags: ['コラム'] },
    { id: 'winter-outdoor', cat: 'life', title: '冬の庭アウトドアに欠かせないグッズ10選', desc: '焚き火台・ポータブル電源・デッキで使える防寒アイテム。', img: 'season-winter', date: '2026.10.28', path: '/feature/winter-outdoor/', tags: ['アウトドア', '冬'] },
    { id: 'year-end', cat: 'life', title: '年末の大掃除、庭はここだけやればOK', desc: '15分で終わる外まわり掃除チェックリスト。', img: 'thumb-garden-care', date: '2026.10.26', path: '/feature/year-end-cleaning/', tags: ['掃除', 'メンテナンス'] },
    { id: 'winter-turf', cat: 'turf', title: '冬の人工芝メンテナンス｜霜・落ち葉・雪の日の対策', desc: '寒い季節に気をつけたいポイント。', img: 'cat-garden', date: '2026.10.22', path: '/garden/turf/winter/', tags: ['人工芝', '冬'] }
  ]);
  S.data.campaigns = [
    { tag: 'CAMPAIGN', title: '秋のプレゼントキャンペーン', text: 'アンケートに答えて、ガーデングッズが当たる', until: '2026.11.30まで', img: 'season-camp', path: '/campaign/autumn-2026/' },
    { tag: 'SEASONAL', title: '冬の庭アウトドアに欠かせないグッズ10選', text: '焚き火台・ポータブル電源・防寒アイテム', img: 'season-winter', path: '/feature/winter-outdoor/' },
    { tag: 'SEASONAL', title: '年末の大掃除、庭はここだけやればOK', text: '15分で終わる外まわり掃除チェックリスト', img: 'photo-front-green', path: '/feature/year-end-cleaning/' }
  ];
  S.data.campaignNews = [
    { badge: '開催中', title: '秋のプレゼントキャンペーン', meta: '2026.11.30まで', path: '/campaign/autumn-2026/' },
    { badge: 'PR', title: '人工芝サンプル無料送付キャンペーン', meta: '数量限定', path: '/campaign/turf-sample/', pr: true },
    { badge: '特集', title: '冬の庭アウトドアグッズ10選', meta: '2026.10.28公開', path: '/feature/winter-outdoor/' }
  ];
  S.data.traps = ['trap-isshiki', 'trap-boundary', 'trap-hot-turf', 'trap-drain', 'trap-subsidy'];
  S.data.trapNotes = ['内訳のない「一式」は、あとから追加費用が出やすい。', '設置位置と声かけ一つで、ご近所トラブルは防げる。', '真夏の表面温度は想像以上。素材と色で差が出る。', '勾配と排水を決めずに打つと、雨のたびに水たまり。', '着工してから申請しても、対象外になる制度が多い。'];
  S.data.columns = [
    { id: 'col-grow', quote: '「芝、伸びてきました？」\nって、けっこう聞かれます。' },
    { id: 'col-gallery', quote: '雨より緊張するのは、\nご近所の見学ギャラリー。' },
    { id: 'col-summer', quote: '目玉焼きは焼けません。\n焼かないでください。' },
    { id: 'col-home', quote: 'うちの庭？\n…その話、長くなりますよ。' }
  ];
  S.data.videos = [
    { title: '人工芝ってどうやって敷く？ 3分でわかる手順', time: '3:12', img: 'video-turf', path: '/video/turf-howto/' },
    { title: '防草シートの重ね幅、正解は？', time: '2:45', img: 'video-sheet', path: '/video/weed-sheet/' },
    { title: 'カーポートの選び方 夜の見え方まで', time: '4:08', img: 'thumb-carport', path: '/video/carport-night/' },
    { title: '人工木ウッドデッキ ○年後のリアル', time: '5:30', img: 'video-deck', path: '/video/deck-1year/' }
  ];
  S.data.cases = [
    { img: 'hero-01', title: 'ウッドデッキと植栽で、リビングから続く庭に', spec: ['神奈川県', '約25㎡', '工期 約2週間'] },
    { img: 'hero-04', title: '雑草に悩んだ庭を、人工芝でお手入れ楽に', spec: ['東京都', '約30㎡', '工期 2日'] },
    { img: 'case-reform', title: '築30年のマンションを、明るいリビングにリフォーム', spec: ['埼玉県', '約70㎡', '工期 約1か月'] },
    { img: 'hero-03', title: 'ビルトインガレージと照明で魅せる外構', spec: ['千葉県', '約40㎡', '工期 約1週間'] },
    { img: 'case-entrance', title: '花壇とアプローチで、季節を楽しむ玄関まわり', spec: ['神奈川県', '約15㎡', '工期 4日'] },
    { img: 'fence-design', title: '低めのフェンスと植栽で開放的な境界に', spec: ['静岡県', '延長18m', '工期 3日'] }
  ];
  S.data.pickupProducts = [
    { img: 'thumb-turf', name: 'リアル人工芝ロール', note: '芝丈35mm・幅1m×10m', price: '¥8,980〜' },
    { img: 'prod-light', name: 'モダンライト（ポール型）', note: 'アプローチ・植栽に', price: '¥14,800' },
    { img: 'prod-mesh', name: 'DIY用 メッシュフェンス', note: '高さ800〜1200mm', price: '¥6,580〜' },
    { img: 'thumb-deliverybox', name: '据え置き型 宅配ボックス', note: '大容量・防水', price: '¥39,800' },
    { img: 'prod-camera', name: '屋外用 防犯カメラ', note: 'Wi-Fi・夜間撮影対応', price: '¥12,800' },
    { img: 'prod-stepstone', name: '敷石・飛び石', note: '天然石調・アプローチに', price: '¥1,580／枚' },
    { img: 'prod-shade', name: 'サンシェード', note: '3×4m・UVカット', price: '¥4,980' },
    { img: 'prod-bench', name: 'ガーデンベンチ', note: '人工木・3人掛け', price: '¥29,800' },
    { img: 'prod-shed', name: 'スチール物置', note: '引き戸・棚板付', price: '¥98,000〜' },
    { img: 'prod-planter', name: '大型プランター', note: 'セメント調・3サイズ', price: '¥7,980〜' },
    { img: 'prod-hose', name: 'ホースリール', note: '20m・散水ノズル付', price: '¥6,480' },
    { img: 'prod-faucet', name: '立水栓（水受け付）', note: '木目調ポール', price: '¥24,800〜' }
  ];
  S.data.areas = [
    { name: '北海道・東北', prefs: ['北海道', '宮城', '福島'] },
    { name: '関東', prefs: ['東京', '神奈川', '埼玉', '千葉', '茨城'] },
    { name: '中部', prefs: ['愛知', '静岡', '長野', '新潟'] },
    { name: '近畿', prefs: ['大阪', '兵庫', '京都', '奈良'] },
    { name: '中国・四国', prefs: ['広島', '岡山', '香川', '愛媛'] },
    { name: '九州・沖縄', prefs: ['福岡', '熊本', '鹿児島', '沖縄'] }
  ];
  S.data.keywords = ['人工芝 DIY', '目隠しフェンス', 'カーポート 価格', '防草シート', 'ウッドデッキ 人工木', '外構 費用', '駐車場 コンクリート', '外構 補助金', '宅配ボックス', '門扉', '砂利 敷き方', '庭 おしゃれ', '人工芝 犬', 'ベランダ 人工芝'];
  S.data.qaCats = [
    { id: 'turf', name: "人工芝", icon: 'sprout', items: [
      { q: "人工芝の下に防草シートは必要？", a: "雑草を抑えたい場合は敷くのがおすすめです。整地・転圧などの下地づくりとセットで考えましょう。", path: "/garden/turf/install/" },
      { q: "犬がいる家でも人工芝は使える？", a: "使えます。水はけの良い製品を選び、排泄物はこまめに取り除いて水で流すのがポイントです。", path: "/garden/turf/use/" },
      { q: "人工芝は何年くらいもつ？", a: "製品の品質や日当たり、使い方によって変わります。メーカーの耐候性の情報や保証内容を確認しましょう。", path: "/column/jinkoshiba-jumyou-nagamochi/" },
      { q: "人工芝と天然芝、結局どっちがいい？", a: "手入れの手間を減らしたいなら人工芝、自然の質感や初期費用の安さを重視するなら天然芝が向いています。", path: "/column/tennenshiba-jinkoshiba-dochira/" },
      { q: "人工芝の芝丈は何mmを選べばいい？", a: "見た目の自然さと踏み心地を重視するなら長め、掃除のしやすさや歩きやすさを重視するなら短めが目安です。用途に合わせて選びましょう。", path: "/column/jinkoshiba-shurui-erabikata/" },
      { q: "真夏の人工芝は熱くならない？", a: "日差しが当たると表面温度は上がります。散水や日よけで温度を下げる工夫や、素材の違いを知っておくと安心です。", path: "/garden/turf/hot/" },
      { q: "人工芝の上で子どもを遊ばせても大丈夫？", a: "多くの家庭で使われています。端のめくれや継ぎ目のつまずきがないよう施工し、夏場は表面温度に気をつけましょう。", path: "/garden/turf/use/" },
      { q: "ベランダに人工芝を敷くときの注意点は？", a: "排水口をふさがないこと、マンションの場合は管理規約を確認することが大切です。水はけの良いタイプを選びましょう。", path: "/garden/turf/use/" },
      { q: "人工芝はDIYでも敷ける？", a: "小さな面積ならDIYも可能です。仕上がりを左右するのは下地（除草・整地・転圧）なので、ここを丁寧に行いましょう。", path: "/column/jinkoshiba-diy-shikikata/" },
      { q: "人工芝を敷くと雑草は生えてこない？", a: "防草シートと組み合わせれば大幅に減らせますが、継ぎ目や端から生えることはあります。見つけたら早めに抜きましょう。", path: "/column/zassou-haenikui-niwa-method/" },
      { q: "人工芝にカビが生えることはある？", a: "芝そのものより、下地の水はけや湿気のこもりが原因で発生することがあります。落ち葉の除去と水洗いで予防しましょう。", path: "/column/jinkoshiba-kabi-gen-in-taisaku/" },
      { q: "人工芝のにおいが気になるときは？", a: "ペットの排泄物などが原因のことが多いです。水でしっかり流し、必要に応じてペット用の消臭剤を使いましょう。", path: "/garden/turf/care/" },
      { q: "人工芝の継ぎ目を目立たなくするには？", a: "芝目（芝の向き）をそろえ、専用の接着テープで隙間なくつなぐのが基本です。施工前に芝目の向きを確認しましょう。", path: "/column/jinkoshiba-diy-shikikata/" },
      { q: "人工芝は水はけが悪くならない？", a: "水抜き穴のある製品を選び、下地に水が流れる勾配をつけておけば、水たまりは起きにくくなります。", path: "/garden/turf/quality/" },
      { q: "人工芝の施工費用はどのくらい？", a: "面積・下地の状態・製品のグレードで変わります。下地づくりの費用が含まれているかを見積もりで確認しましょう。", path: "/column/jinkoshiba-sekou-hiyou-souba/" },
      { q: "安い人工芝と高い人工芝は何が違う？", a: "芝葉の密度や素材、耐候性、裏面の水抜き構造などが違います。サンプルで手触りや色味を確かめるのがおすすめです。", path: "/garden/turf/quality/" },
      { q: "人工芝の上でバーベキューはできる？", a: "火の粉や熱で溶けたり焦げたりするおそれがあります。火を使うときはタイルやコンクリートの上など、燃えにくい場所で行いましょう。", path: "/feature/winter-outdoor/" },
      { q: "冬の人工芝で気をつけることは？", a: "霜や雪の日は滑りやすいので無理に歩かず、落ち葉はこまめに取り除きましょう。", path: "/garden/turf/winter/" },
      { q: "人工芝の掃除はどのくらいの頻度でする？", a: "落ち葉やゴミはこまめに、ブラッシングや水洗いは汚れ具合に合わせて定期的に行うのが目安です。", path: "/garden/turf/care/" },
      { q: "人工芝を敷いたあと、端がめくれてきたら？", a: "固定ピンの追加や、見切り材で端を押さえることで直せる場合があります。下地が沈んでいる場合は補修が必要です。", path: "/garden/turf/care/" },
      { q: "人工芝の施工はどこに頼めばいい？", a: "人工芝の施工実績があり、下地づくりまで説明してくれる会社が安心です。見積もりの内訳を比べて選びましょう。", path: "/garden/turf/contractors/" } ] },
    { id: 'fence', name: "フェンス・外構", icon: 'house', items: [
      { q: "フェンスの高さはどう決める？", a: "「誰の、どこからの視線か」を実際に測って決めるのが失敗しないコツです。", path: "/exterior/fence/fence-guide/" },
      { q: "隣との境界にフェンスを立てるときの注意点は？", a: "境界線の確認と、どちらの敷地に設置するかの合意が大切です。", path: "/exterior/trap/boundary/" },
      { q: "古いブロック塀にフェンスを付けても大丈夫？", a: "強度の確認が必要です。高い目隠しフェンスは風の力を受けやすいため、施工会社に点検してもらいましょう。", path: "/exterior/fence/fence-guide/" },
      { q: "アルミフェンスと樹脂フェンス、どちらがいい？", a: "耐久性とデザインの豊富さならアルミ、木のような質感を重視するなら樹脂（人工木）が向いています。", path: "/column/alumi-fence-jushi-fence-chigai/" },
      { q: "目隠しフェンスで家の中が暗くならない？", a: "隙間のあるタイプやルーバー、高さを抑えたデザインを選べば、光や風を取り入れながら目隠しできます。", path: "/column/mekakushi-fence-erabikata/" },
      { q: "目隠しを強くしすぎると防犯面で問題はある？", a: "死角ができると、侵入者が隠れやすくなる場合があります。視線は遮りつつ見通しも残す、照明と組み合わせるなどの工夫が有効です。", path: "/column/bouhansei-takai-gaikou/" },
      { q: "オープン外構とクローズ外構、どちらがいい？", a: "開放感と費用を重視するならオープン、プライバシーと防犯を重視するならクローズが向いています。", path: "/column/open-gaikou-close-gaikou-chigai/" },
      { q: "セミクローズ外構ってどんなもの？", a: "敷地の一部だけを囲い、残りは開放的にするスタイルです。プライバシーと費用のバランスを取りたい方に選ばれています。", path: "/column/semi-close-gaikou-merit-demerit/" },
      { q: "外構とエクステリアは何が違う？", a: "ほぼ同じ意味で使われますが、外構は「構造物や工事」、エクステリアは「家の外まわり全体の空間」を指すことが多いです。", path: "/column/gaikou-exterior-chigai/" },
      { q: "新築の外構はいつから考え始めればいい？", a: "建物の間取りを決める段階から考え始めるのが理想です。駐車場や配管の位置は、建物の計画と関係するためです。", path: "/column/gaikou-koji-keikaku-timing/" },
      { q: "カーポートは片側支持と両側支持、どちらがいい？", a: "乗り降りのしやすさなら片側支持、強風や積雪への強さなら両側支持が向いています。地域の気候も考えて選びましょう。", path: "/column/carport-shurui-erabikata/" },
      { q: "カーポートの屋根材はどれがいい？", a: "明るさ重視ならポリカーボネート、夏の車内温度を抑えたいなら熱線遮断タイプやスチール屋根が向いています。", path: "/column/carport-yane-zairyou-chigai/" },
      { q: "門扉は開き戸と引き戸、どちらが使いやすい？", a: "前後にスペースがあれば開き戸、前後が狭い場所では引き戸や伸縮タイプが向いています。", path: "/column/mon-hi-shurui-erabikata/" },
      { q: "駐車場はコンクリートとインターロッキング、どちらがいい？", a: "耐久性と費用のバランスならコンクリート、デザイン性や部分補修のしやすさならインターロッキングが向いています。", path: "/column/concrete-interlocking-chigai/" },
      { q: "宅配ボックスはどこに置くのがいい？", a: "配達員が使いやすい玄関や門まわりで、道路から死角にならない場所が基本です。地面や壁にしっかり固定しましょう。", path: "/column/takuhaibox-kodate-erabikata/" },
      { q: "外構で後悔しやすいのはどんなところ？", a: "駐車場の広さ、照明やコンセントの不足、目隠しの高さなど、暮らし始めてから気づく点が多いです。", path: "/column/gaikou-koukai-point-10/" },
      { q: "フェンスが傾いてきたらどうする？", a: "多くは支柱の基礎の劣化や不足が原因です。軽度なら補強、傾きが大きければ基礎からの作り直しを検討します。", path: "/column/fence-katamuku-gen-in-shuuri/" },
      { q: "防犯に強い外構にするには？", a: "見通しの良さ、センサーライトなどの照明、防犯砂利など、侵入しにくく見つかりやすい環境をつくるのが基本です。", path: "/column/bouhansei-takai-gaikou/" },
      { q: "立水栓はどんな場所に付けると便利？", a: "洗車や庭の水やり、子どもの手洗いなど使う場面を考え、駐車場や庭の近くに設けると便利です。", path: "/column/rissuido-shurui-oshare-erabikata/" } ] },
    { id: 'cost', name: "費用・見積もり", icon: 'coins', items: [
      { q: "外構の見積もりは何社に頼むのがいい？", a: "比較のためには2〜3社が目安です。内訳がそろった見積もりで比べましょう。", path: "/exterior/exterior-flow/" },
      { q: "見積もりの「一式」は何を確認すればいい？", a: "何がどれだけ含まれるのか、数量と単価の内訳を出してもらうと比較しやすくなります。", path: "/exterior/trap/isshiki/" },
      { q: "DIYと業者施工、どちらが安い？", a: "材料費だけならDIYが安く済むことが多いですが、道具代や下地づくりの手間、仕上がりの差も含めて比べるのがおすすめです。", path: "/column/diy-gyousha-irai-dochira-otoku/" },
      { q: "外構工事の費用相場はどのくらい？", a: "工事の範囲（駐車場・フェンス・門まわり・庭など）と使う素材で大きく変わります。まず優先順位を決めると予算を立てやすくなります。", path: "/column/gaikou-koji-hiyou-souba/" },
      { q: "新築外構の予算はどう考えればいい？", a: "建物の予算とは別に、外構の予算をあらかじめ確保しておくのが安心です。必要な工事から優先して配分しましょう。", path: "/column/shinchiku-gaikou-yosan-kangaekata/" },
      { q: "外構工事の費用を安く抑えるコツは？", a: "工事を優先順位で分ける、素材のグレードを使い分ける、DIYできる部分を見極めるなどの方法があります。", path: "/column/gaikou-koji-hiyou-yasuku-houhou/" },
      { q: "見積もり後に追加費用が出ることはある？", a: "地中の障害物や残土処分、地盤の状態などで発生することがあります。追加になりうる項目を事前に確認しておきましょう。", path: "/column/gaikou-koji-tsuika-hiyou-case/" },
      { q: "相見積もりは失礼にならない？", a: "一般的に行われていることなので問題ありません。比較していることを伝えたうえで、同じ条件で見積もりを依頼しましょう。", path: "/column/gaikou-koji-mitsumori-kakunin/" },
      { q: "カーポートの設置費用はどのくらい？", a: "台数、構造（片側支持・両側支持など）、屋根材、基礎工事の内容で変わります。本体価格と工事費を分けて確認しましょう。", path: "/column/carport-setti-hiyou-souba/" },
      { q: "フェンスの設置費用はどのくらい？", a: "長さ・高さ・素材と、基礎（ブロックの有無）で変わります。メートルあたりの単価と基礎工事の費用を分けて確認しましょう。", path: "/column/fence-setti-hiyou-ikkura/" },
      { q: "駐車場をコンクリートにする費用は？", a: "面積に加えて、掘削・残土処分・下地の砕石・鉄筋などの費用がかかります。内訳を確認して比べましょう。", path: "/column/chushajou-concrete-hiyou/" },
      { q: "ウッドデッキの設置費用はどのくらい？", a: "広さ・高さと、天然木か人工木かによって変わります。将来の塗装などメンテナンス費用も含めて考えましょう。", path: "/column/wood-deck-setti-hiyou-souba/" },
      { q: "庭に砂利を敷く費用はどのくらい？", a: "砂利の種類と量、防草シートを敷くかどうかで変わります。DIYなら材料費中心に抑えられます。", path: "/column/niwa-jari-hiyou-souba/" },
      { q: "防草シートの施工費用はどのくらい？", a: "シートのグレードと面積、除草・整地の手間で変わります。下地処理の費用が含まれているかを確認しましょう。", path: "/column/bousou-sheet-sekou-hiyou/" },
      { q: "庭のリフォーム費用はどのくらい？", a: "既存の撤去や処分が必要かどうかで大きく変わります。撤去費や残土処分費が見積もりに入っているか確認しましょう。", path: "/column/niwa-reform-hiyou-souba/" },
      { q: "外構リフォームの費用相場は？", a: "駐車場の拡張、フェンスの交換、庭の作り替えなど、工事内容ごとに相場が異なります。工事ごとに分けて見積もりをとると比べやすくなります。", path: "/column/gaikou-reform-hiyou-souba/" },
      { q: "見積もりが予算オーバーしたらどうする？", a: "工事の優先順位を見直す、素材のグレードを調整する、工事を時期で分けるなどの方法があります。", path: "/column/reform-hiyou-osaeru/" },
      { q: "リフォームの支払い方法にはどんなものがある？", a: "現金払い、リフォームローン、住宅ローンへの組み込みなどがあります。金利・審査・手元資金への影響を比べて選びましょう。", path: "/column/reform-hiyou-shiharai-houhou/" },
      { q: "リフォームローンと住宅ローンの違いは？", a: "一般的に住宅ローンのほうが金利は低い傾向がありますが、審査や手続きの条件が異なります。", path: "/column/reform-loan-jutaku-loan-chigai/" },
      { q: "花壇の設置費用はどのくらい？", a: "大きさと素材（レンガ・ブロック・枕木など）で変わります。小さな花壇ならDIYで作る方も多いです。", path: "/column/kadan-setti-hiyou-kouji/" },
      { q: "人工芝の施工費用はどのくらい？", a: "面積・下地の状態・製品のグレードで変わります。下地づくりの費用が含まれているかを見積もりで確認しましょう。", path: "/column/jinkoshiba-sekou-hiyou-souba/" },
      { q: "見積もりで必ず確認したいことは？", a: "工事の範囲、数量と単価、撤去・処分費、保証やアフターサービスの内容を確認しましょう。", path: "/column/gaikou-koji-mitsumori-kakunin/" },
      { q: "中古住宅を買ってリフォームする場合の予算は？", a: "物件価格だけでなく、リフォーム費用・諸費用・予備費を含めた総額で考えるのが基本です。", path: "/column/chuuko-jutaku-reform-hiyou/" } ] },
    { id: 'money', name: "補助金・お金", icon: 'doc', items: [
      { q: "外構工事に使える補助金はある？", a: "自治体によっては、生け垣・緑化、ブロック塀の撤去などに補助制度があります。お住まいの自治体の制度を確認しましょう。", path: "/money/subsidy/" },
      { q: "補助金は工事が終わってから申請できる？", a: "多くの制度は着工前の申請が条件です。工事を始める前に、申請のタイミングを必ず確認しましょう。", path: "/money/trap/subsidy-timing/" },
      { q: "ブロック塀の撤去に補助金は出る？", a: "道路に面した危険なブロック塀の撤去に補助を出している自治体があります。条件は自治体ごとに異なります。", path: "/column/gaikou-reform-hojokin-joseikin/" },
      { q: "住宅省エネ2026キャンペーンとは？", a: "窓の断熱、高効率給湯器、省エネ住宅などを支援する国の補助事業の総称です。対象工事と条件は公式サイトで確認しましょう。", path: "/column/jutaku-shoene2026/" },
      { q: "窓の断熱リフォームに使える補助金は？", a: "国の「先進的窓リノベ2026事業」などが対象になる場合があります。申請は登録事業者が行う仕組みです。", path: "/column/sensenteki-mado-renovation2026/" },
      { q: "エコキュートの交換に補助金は使える？", a: "国の「給湯省エネ2026事業」で、登録された高効率給湯器が対象になる場合があります。最新の条件は公式サイトで確認しましょう。", path: "/column/kyuto-shoene2026/" },
      { q: "補助金は自分で申請するの？", a: "国の住宅省エネ関連の事業は、登録事業者（施工会社）が申請する仕組みが基本です。自治体の制度は本人申請のこともあります。", path: "/column/jutaku-shoene2026/" },
      { q: "国の補助金と自治体の補助金は併用できる？", a: "併用できる場合とできない場合があります。同じ工事への重複を認めない制度もあるため、それぞれの条件を確認しましょう。", path: "/column/reform-hojokin-jichitai/" },
      { q: "リフォーム補助金と減税は一緒に使える？", a: "制度によって扱いが異なります。補助金を受けた分を差し引いて計算する減税もあるため、事前に確認が必要です。", path: "/column/reform-hojokin-genzei-heiyou/" },
      { q: "自治体の補助金はどうやって探す？", a: "お住まいの市区町村のホームページで「住宅 リフォーム 補助」などと検索するか、窓口に問い合わせるのが確実です。", path: "/column/reform-hojokin-jichitai/" },
      { q: "補助金の予算がなくなることはある？", a: "あります。予算の上限に達すると受付が早めに終わる制度もあるため、早めの準備がおすすめです。", path: "/money/trap/subsidy-timing/" },
      { q: "火災保険で屋根や外壁の修理はできる？", a: "台風や雪など突発的な自然災害による損傷は対象になりやすい一方、経年劣化は一般的に対象外です。", path: "/column/kasai-hoken-shuuri/" },
      { q: "火災保険の申請で気をつけることは？", a: "損傷に気づいたら早めに写真で記録し、保険会社に連絡しましょう。申請には期限が設けられている場合があります。", path: "/column/kasai-hoken-shuuri/" },
      { q: "リフォームローンの審査で見られることは？", a: "収入や返済負担率、ほかの借入状況などが確認されるのが一般的です。条件は金融機関によって異なります。", path: "/column/reform-loan-jutaku-loan-chigai/" },
      { q: "太陽光発電と蓄電池はセットで入れるべき？", a: "昼に発電した電気を夜や停電時にも使いたいなら、蓄電池とのセットが向いています。費用と使い方のバランスで判断しましょう。", path: "/column/taiyoukou-chikudenchi-set/" },
      { q: "土地の価格はどうやって調べる？", a: "公示地価や路線価などの公的な指標と、周辺の取引事例を合わせて見るのが基本です。", path: "/realestate/land-value/" },
      { q: "生け垣をつくると補助金がもらえることはある？", a: "緑化の推進のために、生け垣の設置に補助を出している自治体があります。対象となる樹種や長さなどの条件を確認しましょう。", path: "/money/subsidy/" },
      { q: "補助金の対象になる施工会社の条件は？", a: "国の事業では、事務局に登録された事業者が施工・申請を行うことが条件です。依頼する前に登録の有無を確認しましょう。", path: "/column/sensenteki-mado-renovation2026/" },
      { q: "補助金をもらうと税金はかかる？", a: "個人の住宅に関する補助金の扱いは制度や状況によって異なります。気になる場合は税務署や税理士に確認しましょう。", path: "/column/reform-hojokin-genzei-heiyou/" },
      { q: "中古住宅の購入とリフォームで使える制度は？", a: "リフォーム向けの補助金や、住宅ローンへのリフォーム費用の組み込みなどがあります。購入前に資金計画を立てましょう。", path: "/column/chuuko-jutaku-reform-hiyou/" },
      { q: "補助金の情報はどこで確認するのが確実？", a: "国の制度は各事業の公式サイト、自治体の制度は市区町村のホームページが最も確実です。年度ごとに内容が変わる点に注意しましょう。", path: "/purpose/subsidy/" },
      { q: "リフォーム費用を分割で払うことはできる？", a: "リフォームローンや、施工会社が提携するローンを利用できる場合があります。金利と総支払額を確認しましょう。", path: "/column/reform-hiyou-shiharai-houhou/" } ] },
    { id: 'work', name: "工事・季節", icon: 'calendar', items: [
      { q: "冬でも外構工事はできる？", a: "多くの工事は可能です。コンクリートは気温によって固まり方が変わるため、養生期間に注意します。", path: "/exterior/winter-work/" },
      { q: "工事中、近所へのあいさつは必要？", a: "車両の出入りや音が出るため、着工前に一言伝えておくとトラブルを防げます。", path: "/exterior/exterior-flow/" },
      { q: "梅雨や台風の時期は避けたほうがいい？", a: "雨で工程が延びることがあります。余裕のあるスケジュールで計画しましょう。", path: "/exterior/exterior-flow/" },
      { q: "外構工事はどんな流れで進む？", a: "相談・現地調査・プランと見積もり・契約・着工・完成・引き渡しが一般的な流れです。", path: "/exterior/exterior-flow/" },
      { q: "外構工事の期間はどのくらい？", a: "工事の範囲によって大きく変わります。駐車場のコンクリートは養生期間も必要なため、使えるまでの日数も確認しましょう。", path: "/column/gaikou-koji-kiso/" },
      { q: "外構工事は新築の引き渡し前と後、どちらにする？", a: "引き渡し前にまとめて行う方法と、住んでから考える方法があります。駐車場など生活にすぐ必要な部分は早めに計画しましょう。", path: "/column/shinchiku-gaikou-kimeru-koto/" },
      { q: "コンクリートを打ったあと、いつから車を停められる？", a: "気温や配合によって変わります。施工会社から指示された養生期間を守りましょう。", path: "/column/chushajou-concrete-hiyou/" },
      { q: "水はけが悪い庭はどう直せばいい？", a: "原因は土壌・勾配・排水経路のいずれかであることが多いです。原因に合わせて土壌改良や勾配の調整、暗渠排水を検討します。", path: "/column/niwa-mizuhake-warui-gen-in/" },
      { q: "庭に水たまりができるのはなぜ？", a: "周囲より低い場所や、土が踏み固められて水を吸収しにくい場所で発生しやすくなります。", path: "/column/niwa-mizutamari-gen-in-taisaku/" },
      { q: "台風の前に庭でやっておくことは？", a: "飛ばされそうなものの片付け・固定と、排水口や雨どいのゴミの除去が基本です。", path: "/column/taifuu-taisaku-ie-niwa/" },
      { q: "大雨で駐車場が水浸しになるのはなぜ？", a: "短時間に大量の雨が降ると、排水口の処理能力を超えることがあります。排水口の清掃や増設を検討しましょう。", path: "/column/ooame-niwa-chushajou-mizubitashi/" },
      { q: "冬に水道管が凍らないようにするには？", a: "屋外の水道管や立水栓に保温材を巻くのが基本です。寒波の前には対策を済ませておきましょう。", path: "/column/suidoukan-touketsu-boushi/" },
      { q: "庭木の剪定はいつするのがいい？", a: "一般的に、落葉樹は葉が落ちた冬、常緑樹は花後や春〜初夏が目安です。樹種によって適期が異なります。", path: "/column/niwaki-sentei-jiki/" },
      { q: "庭の手入れは季節ごとに何をすればいい？", a: "春は植え付け、夏は水やりと雑草対策、秋は落ち葉掃除と台風対策、冬は落葉樹の剪定と凍結対策が基本です。", path: "/column/niwa-teire-nenkan-calendar/" },
      { q: "外構工事の前に確認しておくべきことは？", a: "敷地の境界、地中の配管、駐車する車のサイズ、家族の動線などを確認しておくと、計画がスムーズに進みます。", path: "/column/shinchiku-gaikou-kimeru-koto/" },
      { q: "土地を買う前に現地で見るべきところは？", a: "境界標、前面道路の幅、高低差、日当たりなどです。時間帯や曜日を変えて複数回見に行くのがおすすめです。", path: "/column/tochi-kounyu-chuiten/" },
      { q: "外構工事の失敗にはどんなものがある？", a: "駐車場が狭い、水はけが悪い、目隠しが足りないなどがよくある例です。完成後の暮らしを具体的に想像して計画しましょう。", path: "/column/gaikou-koji-shippai-taisho/" },
      { q: "工事後のメンテナンスは何をすればいい？", a: "素材ごとに必要な手入れが異なります。ウッドデッキの塗装、コンクリートのひび割れ確認など、定期的に点検しましょう。", path: "/column/gaikou-koji-ato-maintenance-ichiran/" } ] },
    { id: 'care', name: "お手入れ・DIY", icon: 'tool', items: [
      { q: "人工芝の掃除はどうすればいい？", a: "落ち葉やゴミはブロワーやほうきで取り、汚れは水で流すのが基本です。", path: "/garden/turf/care/" },
      { q: "冬の人工芝で気をつけることは？", a: "霜や雪の日は無理に歩かず、落ち葉はこまめに取り除きましょう。", path: "/garden/turf/winter/" },
      { q: "DIYで最初にそろえる道具は？", a: "作業内容によりますが、メジャー・カッター・スコップ・水平器があると多くの作業に対応できます。", path: "/column/diy-shoshinsha-kougu-ichiran/" },
      { q: "防草シートを敷くときのコツは？", a: "除草と整地を丁寧に行い、シートの重ね幅を十分にとって、固定ピンでしっかり留めるのが基本です。", path: "/column/bousou-sheet-shikikata-tejun/" },
      { q: "砂利を自分で敷くときの注意点は？", a: "下に防草シートを敷くこと、砂利の厚みを十分にとることが大切です。厚みが薄いとシートが露出しやすくなります。", path: "/column/jari-jibun-shikikata-chui/" },
      { q: "砂利を敷いたのに雑草が生えてくるのはなぜ？", a: "多くは防草シートの重ね不足、破れ、ずれが原因です。砂利の上に積もった土から生えることもあります。", path: "/column/jari-niwa-zassou-gen-in-taisaku/" },
      { q: "庭の雑草対策は何がいちばん効果的？", a: "庭の使い方によって変わります。緑を残すなら人工芝、費用を抑えるなら砂利、デザイン重視ならタイルなどの舗装が向いています。", path: "/column/niwa-zassou-taisaku-erabikata-guide/" },
      { q: "ウッドデッキの劣化を防ぐには？", a: "天然木は定期的な塗装、人工木は汚れの掃除が基本です。デッキの下の湿気や雑草にも気をつけましょう。", path: "/column/wood-deck-rekka-boushi/" },
      { q: "庭に苔が生えてきたらどうする？", a: "デッキブラシなどで取り除き、日当たり・風通し・水はけを改善すると再発を防ぎやすくなります。", path: "/column/niwa-koke-gen-in-jokyo/" },
      { q: "庭の虫を減らすにはどうすればいい？", a: "落ち葉やゴミの清掃、水たまりの解消、植栽の剪定で風通しを良くすることが基本です。", path: "/column/niwa-mushi-hassei-gen-in-taisaku/" },
      { q: "コンクリートのひび割れは補修すべき？", a: "細いひび割れは補修材で充填できます。幅が広い、段差があるなどの場合は専門業者に調査を依頼しましょう。", path: "/column/concrete-hibiware-gen-in-taisho/" },
      { q: "外壁のひび割れは放置しても大丈夫？", a: "幅の細い表面的なひびは比較的軽度ですが、幅が広いひびは雨水が入るおそれがあるため早めに点検しましょう。", path: "/column/gaiheki-hibiware-houchi/" },
      { q: "雨どいの掃除は自分でできる？", a: "はしごを使って手やブラシでゴミを取り除けます。高所作業に不安がある場合は無理をせず業者に依頼しましょう。", path: "/column/amadoi-souji/" },
      { q: "DIYで花壇を作るにはどうすればいい？", a: "場所と大きさを決め、レンガやブロックで枠を作り、土を入れて植え付けるのが基本の流れです。", path: "/column/diy-kadan-tsukurikata-renga/" },
      { q: "DIYで目隠しフェンスは設置できる？", a: "低めのものならDIYも可能ですが、高いフェンスは風の力を受けやすいため、基礎の強度に注意が必要です。", path: "/column/diy-mekakushi-fence-setti/" },
      { q: "DIYでウッドデッキは作れる？", a: "小さなものならDIYも可能です。束石の水平や強度が重要なので、広いデッキや高さのあるデッキは業者に依頼するのが安心です。", path: "/column/diy-wood-deck-tsukurikata/" },
      { q: "庭の土を入れ替えるにはどうすればいい？", a: "古い土を掘り出し、水はけの良い土や改良材を入れて整えます。量が多い場合は運搬と処分の方法も考えておきましょう。", path: "/column/niwa-tsuchi-irekae-houhou/" },
      { q: "ガーデンライトはDIYで付けられる？", a: "ソーラー式や低電圧（ローボルト）タイプならDIYでも取り付けやすいです。コンセントからの配線工事は資格が必要な場合があります。", path: "/column/diy-niwa-garden-light-setti/" },
      { q: "天然芝が部分的に枯れてしまったら？", a: "水やり、病害虫、踏圧のどれが原因かを観察しましょう。よく歩く場所は敷石で動線を分けると回復しやすくなります。", path: "/column/tennenshiba-kareru-gen-in-taisho/" },
      { q: "物置をDIYで設置するときの注意点は？", a: "地面を平らにして基礎ブロックで水平を出すこと、強風で倒れないよう転倒防止の対策をすることが大切です。", path: "/column/diy-niwa-monooki-setti/" },
      { q: "24時間換気の掃除はどこをすればいい？", a: "給気口のフィルターと換気扇まわりの掃除が基本です。フィルターの汚れ具合を見て定期的に掃除しましょう。", path: "/column/24jikan-kanki-souji/" },
      { q: "家の結露を減らすにはどうすればいい？", a: "換気で室内の湿度を下げることが基本です。根本的な対策としては、内窓の設置など窓の断熱性を高める方法があります。", path: "/column/ie-kekketsu-taisaku/" },
      { q: "室内のカビを防ぐコツは？", a: "換気、水滴の拭き取り、ホコリの掃除で、湿気・温度・栄養源のどれかを取り除くことが基本です。", path: "/column/shitsunai-kabi-taisaku/" },
      { q: "年末の大掃除で庭はどこをやればいい？", a: "落ち葉の掃除、排水口や雨どいの確認など、短時間でできるポイントに絞ると取り組みやすくなります。", path: "/feature/year-end-cleaning/" } ] }
  ];
  S.data.qa = [
    { q: '人工芝の下に防草シートは必要？', a: '雑草を抑えたいなら敷くのがおすすめ。下地の整え方とセットで考えます。', path: '/garden/turf/install/' },
    { q: '外構の見積もりは何社に頼むのがいい？', a: '比較のためには2〜3社が目安。内訳がそろった見積もりで比べましょう。', path: '/exterior/exterior-flow/' },
    { q: 'フェンスの高さはどう決める？', a: '「誰の、どこからの視線か」を実際に測って決めるのが失敗しないコツ。', path: '/exterior/fence/fence-guide/' },
    { q: '冬でも外構工事はできる？', a: '多くの工事は可能。コンクリートは気温による養生期間に注意します。', path: '/exterior/winter-work/' }
  ];

  /* ================= components ================= */
  S.CampaignBox = function (p) {
    var items = (p && p.items) || S.data.campaignNews;
    return '<section class="st-box st-camp" aria-labelledby="camp-t"><h2 class="st-box__title" id="camp-t">' + icon('calendar') + 'キャンペーン情報</h2><ul>' +
      items.map(function (c) { return '<li><a href="' + esc(href(c.path)) + '"' + (c.pr ? ' rel="sponsored"' : '') + '><span class="' + (c.pr ? 'st-pr' : 'st-camp__badge') + '">' + esc(c.badge) + '</span><span class="st-camp__title">' + esc(c.title) + '<small>' + esc(c.meta) + '</small></span>' + icon('chevR') + '</a></li>'; }).join('') + '</ul></section>';
  };
  S.KeywordCloud = function (p) {
    var k = (p && p.keywords) || S.data.keywords;
    return '<div class="st-kw"><p class="st-kw__title">' + icon('search') + '注目のキーワード</p><ul class="st-tags">' + k.map(function (t) { return '<li><a class="st-tag" href="' + esc(href('/search/?q=' + encodeURIComponent(t))) + '">' + esc(t) + '</a></li>'; }).join('') + '</ul></div>';
  };
  S.SeasonalBanners = function () {
    return '<ul class="st-season">' + S.data.campaigns.map(function (c, i) {
      return '<li class="' + (i === 0 ? 'is-main' : '') + '"><a class="st-season__item" href="' + esc(href(c.path)) + '">' + media(c.img, '', '32') + '<span class="st-season__body"><span class="st-season__tag">' + esc(c.tag) + '</span><span class="st-season__title">' + esc(c.title) + '</span><span class="st-season__text">' + esc(c.text) + '</span>' + (c.until ? '<span class="st-season__until">' + icon('calendar') + esc(c.until) + '</span>' : '') + '</span></a></li>';
    }).join('') + '</ul>';
  };
  var ART_PERSON = "<svg class=\"st-promo__art st-promo__art--person\" viewBox=\"0 0 220 240\" aria-hidden=\"true\" focusable=\"false\"><g class=\"st-burst\" stroke=\"#c89a32\" stroke-width=\"5\" stroke-linecap=\"round\"><path d=\"M110 10v18\"/><path d=\"M52 30l11 14\"/><path d=\"M168 30l-11 14\"/><path d=\"M22 74l17 6\"/><path d=\"M198 74l-17 6\"/></g><path d=\"M30 240c0-52 36-78 80-78s80 26 80 78z\" fill=\"#566b4f\"/><path d=\"M90 150h40v22c0 8-9 12-20 12s-20-4-20-12z\" fill=\"#4a5e44\"/><path d=\"M60 205c-22-16-26-40-14-62\" fill=\"none\" stroke=\"#566b4f\" stroke-width=\"20\" stroke-linecap=\"round\"/><path d=\"M160 205c22-16 26-40 14-62\" fill=\"none\" stroke=\"#566b4f\" stroke-width=\"20\" stroke-linecap=\"round\"/><circle cx=\"110\" cy=\"106\" r=\"54\" fill=\"#f2c9a5\"/><path d=\"M58 104c-6-44 22-62 52-62s60 18 52 62c-8-22-26-34-52-34s-44 12-52 34z\" fill=\"#3a2e26\"/><path d=\"M78 84q12-10 24-2M118 82q12-8 24 2\" fill=\"none\" stroke=\"#3a2e26\" stroke-width=\"4\" stroke-linecap=\"round\"/><circle cx=\"90\" cy=\"104\" r=\"12\" fill=\"#fff\"/><circle cx=\"130\" cy=\"104\" r=\"12\" fill=\"#fff\"/><circle cx=\"91\" cy=\"105\" r=\"5\" fill=\"#242722\"/><circle cx=\"129\" cy=\"105\" r=\"5\" fill=\"#242722\"/><ellipse cx=\"110\" cy=\"136\" rx=\"9\" ry=\"12\" fill=\"#7a2e22\"/><circle cx=\"74\" cy=\"124\" r=\"6\" fill=\"#e9a28c\" opacity=\".6\"/><circle cx=\"146\" cy=\"124\" r=\"6\" fill=\"#e9a28c\" opacity=\".6\"/><circle cx=\"50\" cy=\"138\" r=\"15\" fill=\"#f2c9a5\"/><circle cx=\"170\" cy=\"138\" r=\"15\" fill=\"#f2c9a5\"/><path d=\"M172 64c0 0-9 11-9 17a9 9 0 0 0 18 0c0-6-9-17-9-17z\" fill=\"#8fc4e8\"/><text x=\"186\" y=\"44\" font-size=\"42\" font-weight=\"900\" fill=\"#c89a32\" font-family=\"sans-serif\">!?</text></svg>";
  var ART_GRASS = "<svg class=\"st-promo__grass\" viewBox=\"0 0 640 70\" preserveAspectRatio=\"none\" aria-hidden=\"true\" focusable=\"false\"><path d=\"M0 70 Q9.5 42.400000000000006 14.5 24 Q7.833333333333334 47.0 9 70z\" fill=\"#9cc277\"/><path d=\"M5 70 Q12.5 52.0 13.0 40 Q12.333333333333334 55.0 19 70z\" fill=\"#6f9a52\"/><path d=\"M14 70 Q15.5 52.6 11.0 41 Q17.0 55.5 26 70z\" fill=\"#86b061\"/><path d=\"M19 70 Q23.0 38.2 21.5 17 Q23.5 43.5 30 70z\" fill=\"#6f9a52\"/><path d=\"M24 70 Q26.5 38.2 25.0 17 Q27.0 43.5 32 70z\" fill=\"#6f9a52\"/><path d=\"M33 70 Q34.5 52.6 30.0 41 Q36.0 55.5 45 70z\" fill=\"#9cc277\"/><path d=\"M39 70 Q44.5 53.2 44.0 42 Q44.666666666666664 56.0 51 70z\" fill=\"#86b061\"/><path d=\"M47 70 Q57.0 49.0 61.0 35 Q55.666666666666664 52.5 59 70z\" fill=\"#6f9a52\"/><path d=\"M54 70 Q58.5 47.8 59.0 33 Q58.333333333333336 51.5 62 70z\" fill=\"#86b061\"/><path d=\"M59 70 Q69.5 52.0 74.0 40 Q68.0 55.0 71 70z\" fill=\"#6f9a52\"/><path d=\"M65 70 Q71.5 35.800000000000004 71.5 13 Q71.5 41.5 78 70z\" fill=\"#9cc277\"/><path d=\"M73 70 Q76.5 37.0 75.0 15 Q77.0 42.5 83 70z\" fill=\"#5c8644\"/><path d=\"M79 70 Q86.0 45.400000000000006 89.0 29 Q85.0 49.5 87 70z\" fill=\"#5c8644\"/><path d=\"M87 70 Q93.0 41.8 92.5 23 Q93.16666666666667 46.5 100 70z\" fill=\"#9cc277\"/><path d=\"M96 70 Q97.5 52.0 95.0 40 Q98.33333333333333 55.0 104 70z\" fill=\"#9cc277\"/><path d=\"M103 70 Q104.0 49.0 99.5 35 Q105.5 52.5 114 70z\" fill=\"#9cc277\"/><path d=\"M108 70 Q117.5 42.400000000000006 122.0 24 Q116.0 47.0 118 70z\" fill=\"#5c8644\"/><path d=\"M116 70 Q119.0 37.0 118.0 15 Q119.33333333333333 42.5 124 70z\" fill=\"#6f9a52\"/><path d=\"M124 70 Q133.0 52.0 138.0 40 Q131.33333333333334 55.0 132 70z\" fill=\"#5c8644\"/><path d=\"M133 70 Q138.5 37.6 139.0 16 Q138.33333333333334 43.0 143 70z\" fill=\"#9cc277\"/><path d=\"M138 70 Q147.5 37.0 152.0 15 Q146.0 42.5 148 70z\" fill=\"#86b061\"/><path d=\"M143 70 Q146.5 35.800000000000004 146.0 13 Q146.66666666666666 41.5 151 70z\" fill=\"#86b061\"/><path d=\"M149 70 Q157.0 45.400000000000006 159.5 29 Q156.16666666666666 49.5 160 70z\" fill=\"#9cc277\"/><path d=\"M154 70 Q163.0 48.400000000000006 166.5 34 Q161.83333333333334 52.0 165 70z\" fill=\"#9cc277\"/><path d=\"M161 70 Q171.5 49.6 175.0 36 Q170.33333333333334 53.0 175 70z\" fill=\"#9cc277\"/><path d=\"M168 70 Q171.5 38.8 170.0 18 Q172.0 44.0 178 70z\" fill=\"#9cc277\"/><path d=\"M174 70 Q177.0 51.400000000000006 175.5 39 Q177.5 54.5 183 70z\" fill=\"#86b061\"/><path d=\"M180 70 Q184.5 54.4 183.5 44 Q184.83333333333334 57.0 191 70z\" fill=\"#86b061\"/><path d=\"M187 70 Q195.0 54.4 198.5 44 Q193.83333333333334 57.0 196 70z\" fill=\"#9cc277\"/><path d=\"M194 70 Q200.5 42.400000000000006 202.5 24 Q199.83333333333334 47.0 203 70z\" fill=\"#6f9a52\"/><path d=\"M203 70 Q209.5 39.400000000000006 210.5 19 Q209.16666666666666 44.5 214 70z\" fill=\"#9cc277\"/><path d=\"M208 70 Q210.0 36.4 205.5 14 Q211.5 42.0 221 70z\" fill=\"#9cc277\"/><path d=\"M214 70 Q216.0 52.0 213.5 40 Q216.83333333333334 55.0 223 70z\" fill=\"#9cc277\"/><path d=\"M219 70 Q221.5 41.8 218.0 23 Q222.66666666666666 46.5 231 70z\" fill=\"#6f9a52\"/><path d=\"M224 70 Q230.5 49.0 231.0 35 Q230.33333333333334 52.5 236 70z\" fill=\"#6f9a52\"/><path d=\"M233 70 Q241.5 53.8 246.0 43 Q240.0 56.5 241 70z\" fill=\"#86b061\"/><path d=\"M241 70 Q248.0 49.0 248.5 35 Q247.83333333333334 52.5 254 70z\" fill=\"#5c8644\"/><path d=\"M250 70 Q252.0 40.6 248.5 21 Q253.16666666666666 45.5 261 70z\" fill=\"#6f9a52\"/><path d=\"M258 70 Q263.0 37.0 262.5 15 Q263.1666666666667 42.5 269 70z\" fill=\"#9cc277\"/><path d=\"M263 70 Q266.0 49.0 265.0 35 Q266.3333333333333 52.5 271 70z\" fill=\"#5c8644\"/><path d=\"M271 70 Q275.0 48.400000000000006 273.0 34 Q275.6666666666667 52.0 283 70z\" fill=\"#6f9a52\"/><path d=\"M280 70 Q287.5 40.6 290.5 21 Q286.5 45.5 289 70z\" fill=\"#6f9a52\"/><path d=\"M287 70 Q296.5 51.400000000000006 299.5 39 Q295.5 54.5 300 70z\" fill=\"#5c8644\"/><path d=\"M294 70 Q302.5 48.400000000000006 306.0 34 Q301.3333333333333 52.0 304 70z\" fill=\"#86b061\"/><path d=\"M303 70 Q312.5 35.2 317.0 12 Q311.0 41.0 313 70z\" fill=\"#86b061\"/><path d=\"M309 70 Q314.5 45.400000000000006 313.0 29 Q315.0 49.5 323 70z\" fill=\"#9cc277\"/><path d=\"M315 70 Q315.0 35.800000000000004 310.0 13 Q316.6666666666667 41.5 325 70z\" fill=\"#6f9a52\"/><path d=\"M322 70 Q331.5 36.4 336.0 14 Q330.0 42.0 332 70z\" fill=\"#86b061\"/><path d=\"M329 70 Q336.5 37.6 337.0 16 Q336.3333333333333 43.0 343 70z\" fill=\"#5c8644\"/><path d=\"M334 70 Q340.5 46.0 343.0 30 Q339.6666666666667 50.0 342 70z\" fill=\"#86b061\"/><path d=\"M340 70 Q349.0 41.8 353.5 23 Q347.5 46.5 349 70z\" fill=\"#9cc277\"/><path d=\"M349 70 Q359.5 54.4 364.5 44 Q357.8333333333333 57.0 360 70z\" fill=\"#5c8644\"/><path d=\"M354 70 Q362.0 50.2 364.5 37 Q361.1666666666667 53.5 365 70z\" fill=\"#86b061\"/><path d=\"M360 70 Q363.0 38.2 359.0 17 Q364.3333333333333 43.5 374 70z\" fill=\"#5c8644\"/><path d=\"M368 70 Q371.0 37.0 368.5 15 Q371.8333333333333 42.5 379 70z\" fill=\"#6f9a52\"/><path d=\"M374 70 Q382.0 49.6 386.0 36 Q380.6666666666667 53.0 382 70z\" fill=\"#86b061\"/><path d=\"M382 70 Q388.5 49.0 389.0 35 Q388.3333333333333 52.5 394 70z\" fill=\"#9cc277\"/><path d=\"M388 70 Q397.0 49.6 402.0 36 Q395.3333333333333 53.0 396 70z\" fill=\"#6f9a52\"/><path d=\"M393 70 Q396.5 49.6 394.5 36 Q397.1666666666667 53.0 404 70z\" fill=\"#86b061\"/><path d=\"M398 70 Q405.5 44.8 408.5 28 Q404.5 49.0 407 70z\" fill=\"#5c8644\"/><path d=\"M404 70 Q406.0 42.400000000000006 403.0 24 Q407.0 47.0 414 70z\" fill=\"#9cc277\"/><path d=\"M409 70 Q417.5 41.2 420.5 22 Q416.5 46.0 420 70z\" fill=\"#9cc277\"/><path d=\"M415 70 Q423.0 49.0 425.0 35 Q422.3333333333333 52.5 427 70z\" fill=\"#6f9a52\"/><path d=\"M421 70 Q425.5 54.4 423.0 44 Q426.3333333333333 57.0 435 70z\" fill=\"#86b061\"/><path d=\"M427 70 Q436.5 36.4 440.0 14 Q435.3333333333333 42.0 439 70z\" fill=\"#6f9a52\"/><path d=\"M432 70 Q435.0 42.400000000000006 431.5 24 Q436.1666666666667 47.0 445 70z\" fill=\"#9cc277\"/><path d=\"M441 70 Q444.5 52.6 443.5 41 Q444.8333333333333 55.5 450 70z\" fill=\"#86b061\"/><path d=\"M446 70 Q455.5 50.8 459.0 38 Q454.3333333333333 54.0 458 70z\" fill=\"#9cc277\"/><path d=\"M451 70 Q461.0 52.0 465.5 40 Q459.5 55.0 462 70z\" fill=\"#5c8644\"/><path d=\"M460 70 Q466.5 35.2 468.5 12 Q465.8333333333333 41.0 469 70z\" fill=\"#5c8644\"/><path d=\"M469 70 Q478.0 36.4 481.0 14 Q477.0 42.0 481 70z\" fill=\"#86b061\"/><path d=\"M476 70 Q480.0 47.2 477.0 32 Q481.0 51.0 490 70z\" fill=\"#9cc277\"/><path d=\"M484 70 Q489.5 50.2 489.5 37 Q489.5 53.5 495 70z\" fill=\"#9cc277\"/><path d=\"M489 70 Q492.5 45.400000000000006 490.5 29 Q493.1666666666667 49.5 500 70z\" fill=\"#6f9a52\"/><path d=\"M496 70 Q508.0 50.2 513.0 37 Q506.3333333333333 53.5 510 70z\" fill=\"#86b061\"/><path d=\"M503 70 Q510.0 49.0 512.0 35 Q509.3333333333333 52.5 513 70z\" fill=\"#86b061\"/><path d=\"M509 70 Q512.0 50.8 509.5 38 Q512.8333333333334 54.0 520 70z\" fill=\"#9cc277\"/><path d=\"M515 70 Q524.5 48.400000000000006 527.5 34 Q523.5 52.0 528 70z\" fill=\"#9cc277\"/><path d=\"M523 70 Q529.0 41.8 529.5 23 Q528.8333333333334 46.5 534 70z\" fill=\"#86b061\"/><path d=\"M530 70 Q531.5 51.400000000000006 526.5 39 Q533.1666666666666 54.5 543 70z\" fill=\"#5c8644\"/><path d=\"M537 70 Q543.5 37.0 544.5 15 Q543.1666666666666 42.5 548 70z\" fill=\"#6f9a52\"/><path d=\"M544 70 Q546.5 43.6 543.0 26 Q547.6666666666666 48.0 556 70z\" fill=\"#6f9a52\"/><path d=\"M550 70 Q553.0 50.8 552.0 38 Q553.3333333333334 54.0 558 70z\" fill=\"#5c8644\"/><path d=\"M555 70 Q561.5 47.8 563.0 33 Q561.0 51.5 565 70z\" fill=\"#86b061\"/><path d=\"M562 70 Q566.5 39.400000000000006 566.5 19 Q566.5 44.5 571 70z\" fill=\"#9cc277\"/><path d=\"M567 70 Q572.5 44.2 574.0 27 Q572.0 48.5 575 70z\" fill=\"#86b061\"/><path d=\"M572 70 Q575.0 44.2 574.0 27 Q575.3333333333334 48.5 580 70z\" fill=\"#6f9a52\"/><path d=\"M577 70 Q577.5 46.0 574.0 30 Q578.6666666666666 50.0 585 70z\" fill=\"#5c8644\"/><path d=\"M585 70 Q589.0 54.4 588.0 44 Q589.3333333333334 57.0 595 70z\" fill=\"#9cc277\"/><path d=\"M594 70 Q594.5 49.6 591.0 36 Q595.6666666666666 53.0 602 70z\" fill=\"#86b061\"/><path d=\"M600 70 Q602.0 44.8 600.0 28 Q602.6666666666666 49.0 608 70z\" fill=\"#86b061\"/><path d=\"M607 70 Q612.5 43.0 612.0 25 Q612.6666666666666 47.5 619 70z\" fill=\"#86b061\"/><path d=\"M615 70 Q620.5 35.2 619.5 12 Q620.8333333333334 41.0 628 70z\" fill=\"#86b061\"/><path d=\"M622 70 Q622.0 53.8 617.0 43 Q623.6666666666666 56.5 632 70z\" fill=\"#6f9a52\"/><path d=\"M627 70 Q636.0 35.2 639.0 12 Q635.0 41.0 639 70z\" fill=\"#86b061\"/><path d=\"M635 70 Q645.5 45.400000000000006 650.5 29 Q643.8333333333334 49.5 646 70z\" fill=\"#6f9a52\"/></svg>";
  var ART_ROLL = "<svg class=\"st-promo__art st-promo__art--roll\" viewBox=\"0 0 200 140\" aria-hidden=\"true\" focusable=\"false\"><circle cx=\"160\" cy=\"34\" r=\"18\" fill=\"#f3d27a\"/><g stroke=\"#f3d27a\" stroke-width=\"4\" stroke-linecap=\"round\"><path d=\"M160 6v-4M160 66v4M132 34h-4M192 34h4M140 14l-3-3M180 54l3 3M180 14l3-3M140 54l-3 3\"/></g><path d=\"M30 118h120l20-16H50z\" fill=\"#86b061\"/><path d=\"M30 118h120v8H30z\" fill=\"#5c8644\"/><circle cx=\"44\" cy=\"104\" r=\"26\" fill=\"#6f9a52\"/><circle cx=\"44\" cy=\"104\" r=\"18\" fill=\"#8a6a44\"/><circle cx=\"44\" cy=\"104\" r=\"10\" fill=\"#a9865b\"/><circle cx=\"44\" cy=\"104\" r=\"4\" fill=\"#7a5c38\"/><g fill=\"#9cc277\"><path d=\"M60 102l3-10 3 10z\"/><path d=\"M78 102l3-12 3 12z\"/><path d=\"M96 102l3-9 3 9z\"/><path d=\"M114 102l3-11 3 11z\"/><path d=\"M132 102l3-9 3 9z\"/></g></svg>";
  S.TrapSection = function () {
    return '<a class="st-promo st-promo--trap" href="' + esc(href('/exterior/trap/')) + '"><span class="st-promo__bg" aria-hidden="true">' + img('promo-bg', '') + '</span><span class="st-promo__tape" aria-hidden="true"></span><span class="st-promo__text"><span class="st-trap__kicker">' + icon('alert') + '知らないと損する</span><span class="st-promo__title st-trap__title">外構工事の<em>罠</em>！？</span><span class="st-promo__lead">見積もり、境界、排水、補助金。あとから気づいても遅い5つの落とし穴を、テーマ別に解説しています。</span><span class="st-promo__go">特集を読む' + icon('arrow') + '</span></span>' + ART_PERSON + '</a>';
  };
  S.VideoGrid = function () {
    return '<ul class="st-videos">' + S.data.videos.map(function (v) { return '<li><a class="st-video" href="' + esc(href(v.path)) + '"><span class="st-media st-r-hero">' + img(v.img, '') + '<span class="st-video__play">' + icon('play') + '<span class="st-sr">動画を見る</span></span><span class="st-video__time">' + esc(v.time) + '</span></span><span class="st-video__title">' + esc(v.title) + '</span></a></li>'; }).join('') + '</ul>';
  };
  var ART_CRAFTSMAN = "<svg class=\"st-craftsman\" viewBox=\"0 0 120 120\" aria-hidden=\"true\" focusable=\"false\"><circle cx=\"60\" cy=\"60\" r=\"58\" fill=\"#fff\"/><clipPath id=\"cfc\"><circle cx=\"60\" cy=\"60\" r=\"58\"/></clipPath><g clip-path=\"url(#cfc)\"><path d=\"M14 124c0-28 20-42 46-42s46 14 46 42z\" fill=\"#566b4f\"/><path d=\"M48 84l12 14 12-14\" fill=\"none\" stroke=\"#eef1ea\" stroke-width=\"4\" stroke-linejoin=\"round\"/><rect x=\"52\" y=\"70\" width=\"16\" height=\"14\" rx=\"4\" fill=\"#e8b892\"/><circle cx=\"60\" cy=\"54\" r=\"24\" fill=\"#f2c9a5\"/><path d=\"M34 48c0-16 12-24 26-24s26 8 26 24z\" fill=\"#354536\"/><path d=\"M30 48h44c6 0 10 3 10 5H30z\" fill=\"#2a3829\"/><rect x=\"40\" y=\"36\" width=\"40\" height=\"5\" rx=\"2\" fill=\"#c89a32\"/><path d=\"M50 58q3-3 6 0M64 58q3-3 6 0\" fill=\"none\" stroke=\"#3a2e26\" stroke-width=\"2.6\" stroke-linecap=\"round\"/><path d=\"M52 66q8 7 16 0\" fill=\"none\" stroke=\"#7a2e22\" stroke-width=\"2.6\" stroke-linecap=\"round\"/><circle cx=\"46\" cy=\"64\" r=\"3.5\" fill=\"#e9a28c\" opacity=\".6\"/><circle cx=\"74\" cy=\"64\" r=\"3.5\" fill=\"#e9a28c\" opacity=\".6\"/><path d=\"M82 96h18v22H82z\" fill=\"#86b061\"/><path d=\"M82 96l3-7 3 7 3-8 3 8 3-7 3 7\" fill=\"#86b061\"/></g></svg>";
  S.CraftsmanColumn = function () {
    return '<a class="st-promo st-promo--column" href="' + esc(href('/column/shiba/')) + '"><span class="st-promo__text"><span class="st-column__series">連載コラム</span><span class="st-promo__title">人工芝職人が語る<br>現場の本音</span><span class="st-column__quote">「芝、伸びてきました？」って、けっこう聞かれます。</span><span class="st-promo__speaker">' + ART_CRAFTSMAN + '<span><b>人工芝職人</b><small>施工歴10年以上のベテラン</small></span></span><span class="st-promo__lead">何千㎡も芝を敷いてきた施工スタッフが、カタログには載らない現場の話をゆるっと語ります。</span><span class="st-promo__go">コラムを読む' + icon('arrow') + '</span></span>' + ART_GRASS + '</a>';
  };
  S.SeriesPage = function (kind) {
    var trap = kind === 'trap';
    var ids = trap ? S.data.traps : S.data.columns.map(function (c) { return c.id; });
    var title = trap ? '外構工事の罠！？' : '人工芝職人が語る現場の本音';
    var lead = trap ? '見積もり、境界、排水、補助金。あとから気づいても遅い落とし穴を、テーマ別に解説します。' : '何千㎡も芝を敷いてきた施工スタッフが、カタログには載らない現場の話をゆるっと語る連載コラムです。';
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: title }] }) +
      '<main id="main"><div class="st-container"><section class="st-cathero st-cathero--qa" aria-labelledby="sr-h"><div><p class="st-cathero__eyebrow">' + (trap ? 'SPECIAL' : 'COLUMN') + '</p><h1 class="st-cathero__title" id="sr-h">' + esc(title) + '</h1><p class="st-cathero__text">' + esc(lead) + '</p></div></section>' +
      '<div class="st-section"><div class="st-split"><section aria-label="記事一覧">' + S.LatestGrid({ items: ids, cols: 3, desc: true }) + '</section><aside class="st-side">' + S.Ranking({ mode: 'editor', id: 'sr-ed' }) + S.ConsultBox() + '</aside></div></div></div></main>' + S.Footer() + '</div>';
  };
  S.CaseGallery = function () {
    return '<div class="st-cases" tabindex="0" role="region" aria-label="施工例（横にスクロールできます）"><ul>' + S.data.cases.map(function (c) { return '<li><a href="' + esc(href('/cases/')) + '">' + media(c.img, c.title, '43') + '<span class="st-cases__title">' + esc(c.title) + '</span><span class="st-cases__spec">' + c.spec.map(esc).join(' ／ ') + '</span></a></li>'; }).join('') + '</ul></div><p class="st-cases__note">施工例は掲載施工会社の提供写真です（このデザインでは仮画像）。</p>';
  };
  S.PickupProducts = function () {
    return '<div class="st-pick"><p class="st-pick__disc">' + S.PRLabel() + '<span>このコーナーにはアフィリエイトリンクを含みます。価格は取得日時点の参考価格です（このデザインではサンプル価格）。</span></p><ul class="st-pick__list">' + S.data.pickupProducts.map(function (p) { return '<li><a href="' + esc(href('/products/pickup/')) + '" rel="sponsored">' + media(p.img, '', '11') + '<span class="st-pick__name">' + esc(p.name) + '</span><span class="st-pick__note">' + esc(p.note) + '</span><span class="st-pick__price">' + esc(p.price) + '</span></a></li>'; }).join('') + '</ul></div>';
  };
  S.AreaSearch = function () {
    return '<div class="st-area"><p class="st-area__title">' + icon('pin') + 'エリアから施工会社を探す</p><dl>' + S.data.areas.map(function (r) { return '<div><dt>' + esc(r.name) + '</dt><dd>' + r.prefs.map(function (p) { return '<a href="' + esc(href('/contractors/area/') + '#area-' + encodeURIComponent(p)) + '">' + esc(p) + '</a>'; }).join('') + '</dd></div>'; }).join('') + '</dl></div>';
  };
  S.QABox = function () {
    return '<p class="st-qa__intro">読者から寄せられた質問を、テーマ別にまとめています。</p><ul class="st-qacats">' + S.data.qaCats.map(function (c) { return '<li><a href="' + esc(href('/qa/' + c.id + '/')) + '"><span class="st-qacats__icon">' + icon(c.icon) + '</span><span class="st-qacats__name">' + esc(c.name) + '<small>' + c.items.length + '件の質問</small></span>' + icon('chevR') + '</a></li>'; }).join('') + '</ul>';
  };
  S.QAPage = function (catId) {
    var cats = S.data.qaCats, cur = cats.filter(function (c) { return c.id === catId; })[0] || cats[0];
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: '読者の質問箱', path: '/qa/' }, { name: cur.name }] }) +
      '<main id="main"><div class="st-container"><section class="st-cathero st-cathero--qa" aria-labelledby="qa-h"><div><p class="st-cathero__eyebrow">Q&amp;A</p><h1 class="st-cathero__title" id="qa-h">読者の質問箱</h1><p class="st-cathero__text">読者から寄せられた家まわりの質問に、編集部が答えます。くわしい解説は各記事へのリンクからどうぞ。</p>' +
      '<nav class="st-subnav" aria-label="質問のテーマ">' + cats.map(function (c) { return '<a href="' + esc(href('/qa/' + c.id + '/')) + '"' + (c === cur ? ' aria-current="page"' : '') + '>' + icon(c.icon) + esc(c.name) + '</a>'; }).join('') + '</nav></div></section>' +
      '<div class="st-section"><div class="st-split"><section aria-labelledby="qa-cat-t">' + S.SectionHeading({ title: cur.name + 'の質問', en: 'Questions', id: 'qa-cat-t' }) +
      S.FAQ({ items: cur.items.map(function (x) { return { q: x.q, a: esc(x.a) + (x.path ? ' <a class="st-a" href="' + esc(href(x.path)) + '">くわしく読む</a>' : '') }; }) }) +
      '<div class="st-note st-note--info" style="margin-top:28px"><p class="st-note__head">' + icon('chat') + '質問を送る</p><p>掲載してほしい質問は、お問い合わせフォームから受け付けています。すべての質問にはお答えできない場合があります。</p></div></section>' +
      '<aside class="st-side">' + S.Ranking({ mode: 'editor', id: 'qa-ed' }) + S.ConsultBox() + '</aside></div></div></div></main>' + S.Footer() + '</div>';
  };


  /* ================= カテゴリから探す（縦長パネル） ================= */
  S.data.catEn = { garden: 'GARDEN', exterior: 'EXTERIOR', carport: 'CARPORT', deck: 'WOOD DECK', equipment: 'EQUIPMENT', reform: 'REFORM', realestate: 'REAL ESTATE', money: 'MONEY', life: 'LIFE' };
  S.CategoryPanels = function () {
    return '<section class="st-section st-catpanel-sec" aria-labelledby="catp-t"><div class="st-sechead"><h2 class="st-sechead__title" id="catp-t">カテゴリから探す</h2><span class="st-sechead__en" aria-hidden="true">Category</span></div>' +
      '<ul class="st-catpanels">' + S.data.categories.map(function (c, i) {
        return '<li><a class="st-catpanel" href="' + esc(href(c.path)) + '">' + img(c.img, '') + '<span class="st-catpanel__shade"></span>' +
          '<span class="st-catpanel__no">' + ('0' + (i + 1)).slice(-2) + '</span><span class="st-catpanel__name">' + esc(c.name) + '</span>' +
          '<span class="st-catpanel__foot"><span class="st-catpanel__en">' + esc(S.data.catEn[c.id] || '') + '</span><span class="st-catpanel__sub">' + esc(c.sub) + '</span><span class="st-catpanel__go">' + icon('arrow') + '</span></span></a></li>';
      }).join('') + '</ul></section>';
  };
  S.HeroKeywords = function () {
    return '<div class="st-hero__kw"><span>よく読まれているキーワード</span><ul>' + S.data.keywords.slice(0, 6).map(function (t) { return '<li><a href="' + esc(href('/search/?q=' + encodeURIComponent(t))) + '">#' + esc(t) + '</a></li>'; }).join('') + '</ul></div>';
  };

  /* ================= 広告枠 =================
     S.config.ads = { 'home-infeed': '<ins …>広告コード</ins>', … } にコードを入れるとその枠に表示。
     コードが無い枠は、S.config.showAdSlots が true のときだけ「広告枠」の目印を表示（本番は何も出さない） */
  S.AdSlot = function (id, size) {
    var code = (S.config.ads || {})[id];
    if (code) return '<aside class="st-ad st-ad--' + (size || 'wide') + '" aria-label="広告" data-ad-slot="' + esc(id) + '"><span class="st-ad__label">広告</span>' + code + '</aside>';
    if (!S.config.showAdSlots) return '';
    return '<aside class="st-ad st-ad--' + (size || 'wide') + ' st-ad--empty" aria-label="広告枠" data-ad-slot="' + esc(id) + '"><span class="st-ad__label">広告</span><span class="st-ad__ph">広告枠（' + esc(id) + '）</span></aside>';
  };
  /* ================= ホームの新着記事（多め） ================= */
  /* ホームの新着記事：人工芝を先頭に、カテゴリが偏らないよう編集部で選んだ12本（存在しない記事は新しい順で補う） */
  S.data.homeLatest = ['/garden/turf/use/', '/column/gaikou-koji-tsuika-hiyou-case/', '/column/ecocute-jumyou/', '/exterior/deck/deck-ideas/',
    '/column/hatazaochi-merit-demerit/', '/column/jutaku-shoene2026/', '/column/jinkoshiba-jumyou-nagamochi/', '/column/kitchen-reform-hiyou/',
    '/column/niwa-zassou-taisaku-erabikata-guide/', '/column/takuhai-box-shurui-erabikata/', '/exterior/trap/boundary/', '/column/diy-gyousha-irai-dochira-otoku/'];
  S.HomeLatest = function (n) {
    n = n || 12;
    var l = S.refs ? S.refs(S.data.homeLatest) : [], seen = {};
    l.forEach(function (c) { seen[c.path] = 1; });
    (S.allCards ? S.allCards() : []).forEach(function (c) { if (l.length < n && !seen[c.path]) { seen[c.path] = 1; l.push(c); } });
    l = l.slice(0, n);
    if (!l.length) return S.LatestGrid({ cols: 3, items: S.data.latest.slice(0, 6), desc: true });
    var ad = S.AdSlot('home-infeed', 'infeed');
    return '<ul class="st-grid st-grid--3 st-home-new">' + l.map(function (a, i) { return (i === 6 && ad ? '<li class="st-home-new__ad">' + ad + '</li>' : '') + '<li>' + S.ArticleCard({ article: a, desc: true }) + '</li>'; }).join('') + '</ul>';
  };
  /* ================= これだけは知っておきたい基礎知識 ================= */
  S.data.basics = [
    { topic: '外構工事', img: 'photo-black-house-concrete', path: '/column/gaikou-koji-kiso/' },
    { topic: '庭づくり', img: 'photo-lawn-deck', path: '/column/niwazukuri-kiso-shoshinsha/' },
    { topic: '人工芝', img: 'photo-turf-dog', path: '/garden/turf/basics/' },
    { topic: 'フェンス', img: 'photo-fence', path: '/exterior/fence/fence-guide/' },
    { topic: 'カーポート', img: 'photo-carport', path: '/column/carport-shurui-erabikata/' },
    { topic: 'ウッドデッキ', img: 'photo-sea-deck', path: '/column/wood-deck-zairyou-shurui/' },
    { topic: '費用・見積もり', img: 'photo-house-dusk', path: '/column/gaikou-koji-hiyou-souba/' },
    { topic: 'DIY', img: 'photo-prod-stepstone', path: '/column/niwa-diy-dekiru-koto-20/' },
    { topic: '住宅設備', img: 'photo-interior-city', path: '/column/ecocute-gas-hikaku/' },
    { topic: 'リフォーム', img: 'photo-reform-living', path: '/column/reform-hiyou-osaeru/' },
    { topic: '土地選び', img: 'photo-hiraya-dusk', path: '/column/tochi-kounyu-chuiten/' },
    { topic: '補助金', img: 'photo-turf-approach', path: '/money/subsidy/' }
  ];
  S.BasicsSection = function () {
    var all = S.allCards ? S.allCards() : [], by = {};
    all.forEach(function (c) { by[c.path] = c; });
    S.data.articles.forEach(function (a) { if (!by[a.path]) by[a.path] = a; });
    var items = S.data.basics.map(function (b) { return { b: b, a: by[b.path] }; }).filter(function (x) { return x.a; });
    return '<section class="st-section st-basics" aria-labelledby="basics-t">' + S.SectionHeading({ title: 'これだけは知っておきたい基礎知識', en: 'Basics', more: '/column/category/basics/', id: 'basics-t' }) +
      '<p class="st-sechead__lead">はじめて調べる方は、まずここから。テーマごとに「最初に読んでほしい1本」を選びました。</p><ol class="st-basics__list">' +
      items.map(function (x, i) {
        return '<li><a class="st-basic" href="' + esc(href(x.a.path)) + '"><span class="st-basic__media">' + img(x.b.img || x.a.img, '') + '<span class="st-basic__topic"><small>基礎知識 ' + ('0' + (i + 1)).slice(-2) + '</small>' + esc(x.b.topic) + '</span></span><span class="st-basic__title">' + esc(x.a.title).replace('｜', '<br>') + '</span></a></li>';
      }).join('') + '</ol></section>';
  };
  /* ================= top page (extended) ================= */
  S.TopPage = function () {
    var H = S.SectionHeading;
    return '<div class="st">' + S.Header({ active: 'home' }) + '<main id="main" class="st-main--flush">' + S.HeroSlider() +
      '<div class="st-container">' + S.CategoryPanels() +
      '<section class="st-section st-top-feature st-band st-band--leaf" aria-labelledby="feat-t">' + S.FeatureGrid({ guide: true, heading: { title: '今、読まれている特集', en: 'Feature', more: '/feature/', id: 'feat-t' } }) + '</section>' +
      '<section class="st-section st-top-new st-band st-band--soft st-band--wave" aria-labelledby="new-t"><div class="st-split st-split--top"><div>' + H({ title: '新着記事', en: 'New articles', more: '/new/', id: 'new-t' }) + S.HomeLatest(12) + '<p class="st-home-new__more">' + S.Button({ href: '/new/', label: '新着記事をもっと見る' }) + '</p></div>' +
      '<div class="st-side st-side--top">' + S.Ranking({ id: 'top-rk' }) + S.AdSlot('home-side', 'side') + '</div></div>' +
      '<div class="st-subrow">' + S.KeywordCloud() + S.CTABanner({ title: 'DIYで叶える<br>理想の庭', text: '人工芝・防草シート・資材をまとめて比較', cta: '商品を見る', href: '/purpose/products/', img: 'photo-garden-dusk' }) + S.CampaignBox() + '</div></section>' +
      S.BasicsSection() +
      '<section class="st-section st-band st-band--sprig" aria-labelledby="season-t">' + H({ title: '季節の特集・キャンペーン', en: 'Seasonal', more: '/campaign/', id: 'season-t' }) + S.SeasonalBanners() + '</section>' +
      '<section class="st-section" aria-labelledby="col-h">' + H({ title: '知って得する読みもの', en: 'Column', more: '/column/', id: 'col-h' }) + '<p class="st-sechead__lead">家づくり・外構のプロだからこそ話せる、ちょっと得する豆知識とホンネの話。</p><div class="st-promos">' + S.TrapSection() + S.CraftsmanColumn() + '</div>' + (S.ColCatNav && S.colAll().length ? '<div class="st-top-colnav"><p class="st-top-colnav__lead">' + icon('book') + '外構・庭づくりコラム（' + S.colAll().length + '本）をカテゴリから探す</p>' + S.ColCatNav({ withAll: true }) + '</div>' : '') + '</section>' +
      '<section class="st-section st-band st-band--soft st-band--wave" aria-labelledby="pick-t">' + H({ title: '編集部ピックアップ商品', en: 'Pick up', more: S.config.affiliate ? '/products/pickup/' : null, id: 'pick-t' }) + S.PickupProducts() + '</section>' +
      '<section class="st-section st-band st-band--last"><div class="st-duo st-duo--even"><div aria-labelledby="qa-t" role="region">' + H({ title: '読者の質問箱', en: 'Q&A', more: '/qa/turf/', id: 'qa-t', level: 'h2' }) + S.QABox() + '</div>' +
      '<div role="region" aria-label="エリアから施工会社を探す">' + S.AreaSearch() + '</div></div></section>' +
      S.AdSlot('home-bottom', 'wide') +
      '</div>' + S.PurposeNav() + '</main>' + S.Footer() + '</div>';
  };

  /* ================= campaign page ================= */
  S.CampaignPage = function () {
    var prizes = [
      { img: 'thumb-garden-care', name: 'ガーデニングツール 5点セット', n: '10名様' },
      { img: 'cat-deck', name: 'アウトドアチェア 2脚セット', n: '5名様' },
      { img: 'thumb-turf', name: '人工芝 お試しマット（1㎡）', n: '20名様' }
    ];
    return '<div class="st">' + S.Header({ active: '' }) + S.Breadcrumb({ items: [{ name: 'ホーム', path: '/' }, { name: 'キャンペーン', path: '/campaign/' }, { name: '秋のプレゼントキャンペーン' }] }) +
      '<main id="main"><section class="st-cpn-hero">' + img('season-camp', '') + '<div class="st-container"><p class="st-season__tag">CAMPAIGN</p><h1 class="st-cpn-hero__title">秋のプレゼント<br>キャンペーン</h1><p class="st-cpn-hero__lead">かんたんなアンケートに答えて、庭時間が楽しくなるグッズを当てよう。</p><p class="st-cpn-hero__period">' + icon('calendar') + '応募期間：2026.10.01 〜 2026.11.30</p></div></section>' +
      '<div class="st-container">' + (S.images['campaign-flyer'] ? '<section class="st-section st-flyer" aria-labelledby="flyer-t">' + S.SectionHeading({ title: 'キャンペーンのご案内', en: 'Flyer', id: 'flyer-t' }) + '<figure class="st-flyer__fig"><a href="' + esc(S.images['campaign-flyer']) + '" target="_blank" rel="noopener"><img src="' + esc(S.images['campaign-flyer']) + '" alt="秋のプレゼントキャンペーンのチラシ。プレゼント内容と応募方法、応募期間（2026年10月1日〜11月30日）" loading="lazy" decoding="async"></a><figcaption>タップするとチラシを大きく表示できます</figcaption></figure></section>' : '') + '<section class="st-section" aria-labelledby="prize-t">' + S.SectionHeading({ title: 'プレゼント内容', en: 'Present', id: 'prize-t' }) +
      '<ul class="st-grid st-grid--3">' + prizes.map(function (p) { return '<li class="st-prize">' + media(p.img, p.name, '43') + '<p class="st-prize__n">' + esc(p.n) + '</p><p class="st-prize__name">' + esc(p.name) + '</p></li>'; }).join('') + '</ul></section>' +
      '<section class="st-section" aria-labelledby="how-t"><div class="st-split"><div>' + S.SectionHeading({ title: '応募方法', en: 'How to', id: 'how-t' }) +
      S.Steps({ items: [{ title: 'アンケートページを開く', desc: '下のボタンから、所要時間2分ほどのアンケートへ。' }, { title: '質問に答えて、希望のプレゼントを選ぶ', desc: '庭や外構についての簡単な質問です。' }, { title: '当選者にはメールでご連絡', desc: '応募締切後、2026年12月中旬までにご連絡します。' }] }) +
      '<div class="st-note st-note--info" style="margin-top:24px"><p class="st-note__head">' + icon('info') + 'ご応募の前に</p><p>このページはデザインサンプルです。実施時は、応募規約・個人情報の取り扱い・当選発表の方法を掲載します。</p></div>' +
      '<p style="margin-top:28px">' + S.Button({ href: '/campaign/autumn-2026/entry/', label: 'アンケートに回答して応募する', variant: 'accent' }) + '</p></div>' +
      '<aside class="st-side">' + S.CampaignBox() + S.Ranking({ mode: 'editor', id: 'cp-ed' }) + '</aside></div></section></div></main>' + S.Footer() + '</div>';
  };
})();
