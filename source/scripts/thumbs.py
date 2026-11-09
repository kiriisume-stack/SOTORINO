import json
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
# コラムのサムネイル自動生成（1200x675で描画 → 960x540で保存）
# 使い方: python3 scripts/thumbs.py [slug ...]   （引数なし＝全記事。要 Pillow と Noto Sans/Serif CJK フォント）
import os,sys,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG=os.environ.get('SOTORINO_IMAGES',os.path.join(ROOT,'..','images'))
OUT=os.path.join(IMG,'04_column-thumbnails')
PH={os.path.basename(p)[:-4]:p for p in glob.glob(os.path.join(IMG,'01_photos','**','*.jpg'),recursive=True)}
A=json.load(open(os.path.join(ROOT,'content','columns.json')))
if len(sys.argv)>1: A=[a for a in A if a['slug'] in sys.argv[1:]]
BG={'basics':'photo-stone-dusk','garden':'photo-lawn-deck','diy':'photo-prod-stepstone','products':'photo-light','cost':'photo-house-day','trouble':'photo-white-deck','equipment':'photo-interior-city','reform':'photo-reform-living','realestate':'photo-hiraya-dusk','money':'photo-wood-balcony','lifestyle':'photo-front-green'}
W,H=1200,675
FD=os.environ.get('FONT_DIR','/usr/share/fonts/opentype/noto')  # Noto CJK（.ttc）の置き場所
FB=FD+'/NotoSansCJK-Bold.ttc'; FM=FD+'/NotoSansCJK-Medium.ttc'; FS=FD+'/NotoSerifCJK-SemiBold.ttc'
def jp(path,size): return ImageFont.truetype(path,size,index=0)  # index0 = JP in Noto CJK ttc
bgs={}
for k,p in BG.items():
    im=Image.open(PH[p]).convert('RGB')
    r=max(W/im.width,H/im.height); im=im.resize((int(im.width*r)+1,int(im.height*r)+1),Image.LANCZOS)
    im=im.crop(((im.width-W)//2,(im.height-H)//2,(im.width-W)//2+W,(im.height-H)//2+H))
    im=ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(1.2))).enhance(.95)
    # gradient overlay
    ov=Image.new('RGBA',(W,H)); d=ImageDraw.Draw(ov)
    for x in range(W):
        a=int(215*max(0,1-x/(W*1.05))**0.9)+25
        d.line([(x,0),(x,H)],fill=(22,30,23,min(235,a)))
    im=Image.alpha_composite(im.convert('RGBA'),ov)
    bgs[k]=im
NOSTART='、。？！）」』ー・…：'
import re
def kind(c):
    if '\u3040'<=c<='\u309f': return 'h'
    if '\u30a0'<=c<='\u30ff' or c=='ー': return 'k'
    if '\u4e00'<=c<='\u9fff' or c in '々〆': return 'K'
    if c.isascii() and c.isalnum(): return 'a'
    return 'p'
def tokens(t):
    out=[];cur=''
    for i,c in enumerate(t):
        cur+=c
        nx=t[i+1] if i+1<len(t) else ''
        if not nx: break
        a,b=kind(c),kind(nx)
        brk=False
        if c in '？！、。・：' : brk=True
        elif a=='h' and b in ('K','k','a') : brk=True
        elif a=='h' and c in 'はがをにでとのもへや' and b=='h' and nx not in 'るれてたしいっ': brk=False
        elif a in ('K','k','a') and b=='p' and nx in '（「': brk=True
        elif (a=='a' and b=='k') or (a=='k' and b=='a'): brk=True
        if brk: out.append(cur); cur=''
    if cur: out.append(cur)
    return out
def wrap(text,font,maxw,draw):
    lines=[];cur=''
    for tk in tokens(text):
        if draw.textlength(cur+tk,font=font)<=maxw or not cur: cur+=tk
        else: lines.append(cur); cur=tk
        if draw.textlength(cur,font=font)>maxw:
            # fallback hard wrap
            while draw.textlength(cur,font=font)>maxw:
                j=len(cur)
                while draw.textlength(cur[:j],font=font)>maxw: j-=1
                while j>1 and j<len(cur) and cur[j] in NOSTART: j-=1
                for b in range(j,max(1,j-7),-1):
                    if cur[b-1] in 'はがをにでとのも' and cur[b] not in NOSTART: j=b; break
                lines.append(cur[:j]); cur=cur[j:]
    if cur: lines.append(cur)
    return lines
def _old_wrap(text,font,maxw,draw):
    lines=[];cur=''
    i=0
    while i<len(text):
        ch=text[i]
        if draw.textlength(cur+ch,font=font)>maxw and cur:
            if ch in NOSTART: cur+=ch; i+=1; continue
            lines.append(cur); cur=''
        cur+=ch
        if ch in '？！' and i<len(text)-1 and draw.textlength(text[i+1:],font=font)<=maxw*1.9:
            lines.append(cur); cur=''
        i+=1
    if cur: lines.append(cur)
    return lines
for a in A:
    im=bgs[a['cat']].copy(); d=ImageDraw.Draw(im)
    # category pill
    pf=jp(FB,28); t=a['catName']; tw=d.textlength(t,font=pf)
    d.rounded_rectangle((64,64,64+tw+40,64+52),radius=8,fill=(86,107,79,255))
    d.text((84,70),t,font=pf,fill='white')
    # title
    size=66
    for size in (68,62,56,50):
        f=jp(FB,size); lines=wrap(a['title'],f,800,d)
        if len(lines)<=3: break
    lh=int(size*1.42); y=H//2-len(lines)*lh//2+10
    for ln in lines:
        d.text((64,y),ln,font=f,fill='white'); y+=lh
    d.rectangle((64,y+14,64+72,y+18),fill=(200,154,50,255))
    # footer mark
    mf=jp(FS,26); d.text((64,H-76),'SOTORINO  COLUMN',font=mf,fill=(255,255,255,210))
    nf=jp(FM,24); n=f'No.{a["id"]:03d}'; d.text((W-64-d.textlength(n,font=nf),H-74),n,font=nf,fill=(255,255,255,170))
    im.convert('RGB').resize((960,540),Image.LANCZOS).save(os.path.join(OUT,a['slug']+'.jpg'),quality=80,optimize=True,progressive=True)
print('done')
