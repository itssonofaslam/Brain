import math, subprocess, sys
W,H=1600,900
EGG="M0,-52 C22,-52 40,-22 40,10 C40,38 22,52 0,52 C-22,52 -40,38 -40,10 C-40,-22 -22,-52 0,-52 Z"
POSES={
 'stand':dict(S=(0,-150),Hp=(0,-92),hd=0,L=[(-28,-112),(-32,-74)],R=[(28,-112),(32,-74)],LL=[(-12,-48),(-16,0)],RL=[(12,-48),(16,0)],emo='calm'),
 'run':dict(S=(26,-146),Hp=(0,-92),hd=12,L=[(0,-112),(-34,-92)],R=[(48,-128),(78,-108)],LL=[(28,-62),(58,-42)],RL=[(-12,-50),(-42,0)],emo='alarm'),
 'wow':dict(S=(0,-150),Hp=(0,-92),hd=-6,L=[(-42,-172),(-54,-218)],R=[(42,-172),(58,-218)],LL=[(-20,-48),(-30,0)],RL=[(20,-48),(30,0)],emo='awe'),
}
def P(pts): return "M"+" L".join(f"{x},{y}" for x,y in pts)
def parts(p):
    S,Hp=p['S'],p['Hp']
    sh_l=(S[0]-16,S[1]+8); sh_r=(S[0]+16,S[1]+8)
    arms=[[sh_l]+p['L'],[sh_r]+p['R']]
    legs=[[(Hp[0]-8,Hp[1])]+p['LL'],[(Hp[0]+8,Hp[1])]+p['RL']]
    head=(S[0]+p['hd']*0.4,S[1]-62)
    return arms,legs,head
def face(p,col='#15101a',emo='calm',hi=True):
    e=p['emo']
    s=f'<ellipse cx="-14" cy="6" rx="5.5" ry="8" fill="{col}"/><ellipse cx="14" cy="6" rx="5.5" ry="8" fill="{col}"/>'
    if hi: s+='<circle cx="-12" cy="3" r="2" fill="#fff"/><circle cx="16" cy="3" r="2" fill="#fff"/>'
    if e=='calm': s+=f'<path d="M-8,28 Q0,33 8,28" stroke="{col}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    if e=='alarm': s+=f'<path d="M-22,-8 L-8,-3 M22,-8 L8,-3" stroke="{col}" stroke-width="3.5" stroke-linecap="round"/><ellipse cx="0" cy="30" rx="6" ry="8" fill="{col}"/>'
    if e=='awe': s+=f'<path d="M-22,-10 Q-14,-18 -6,-10 M22,-10 Q14,-18 6,-10" stroke="{col}" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="0" cy="30" rx="8" ry="10" fill="{col}"/>'
    return s
def tuft(col,w=4): return f'<path d="M-4,-52 Q-10,-70 -16,-72 M0,-52 Q0,-74 2,-80 M4,-52 Q12,-68 20,-68" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round"/>'
def wrap(x,y,s,inner,extra=''): return f'<g transform="translate({x},{y}) scale({s})" {extra}>{inner}</g>'
def lim(pts,w,col,dx=0,dy=0,f=''): 
    pp=[(a+dx,b+dy) for a,b in pts]
    return f'<path d="{P(pp)}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round" {f}/>'
def bars(label):
    return f'<rect x="0" y="0" width="{W}" height="51" fill="#000"/><rect x="0" y="{H-51}" width="{W}" height="51" fill="#000"/><text x="24" y="{H-18}" fill="#bbb" font-family="Arial" font-size="20">{label}</text>'
GRAIN=lambda o,m='multiply',f='0.8':f'<filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="{f}" numOctaves="2" seed="4"/><feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 {o} 0"/></filter>'
def svg(defs,body,label,extra=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>{defs}</defs>{body}{extra}{bars(label)}</svg>'
PLACE=[('stand',430,800,1.75),('run',930,730,1.3),('wow',1300,680,1.0)]

# ---------- 1 CLAY ----------
def clay():
    defs='''<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b2a42"/><stop offset="1" stop-color="#241826"/></linearGradient>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3f4a"/><stop offset="1" stop-color="#2d1c27"/></linearGradient>
    <radialGradient id="hg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#ffd9b3"/><stop offset=".5" stop-color="#e59b6b"/><stop offset="1" stop-color="#9c5a3c"/></radialGradient>
    <radialGradient id="win" cx=".5" cy=".5" r=".7"><stop offset="0" stop-color="#ffe2a8"/><stop offset="1" stop-color="#ffb35c"/></radialGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffd68a" stop-opacity=".35"/><stop offset="1" stop-color="#ffd68a" stop-opacity="0"/></linearGradient>
    <filter id="soft"><feGaussianBlur stdDeviation="3"/></filter><filter id="bl"><feGaussianBlur stdDeviation="16"/></filter><filter id="bl2"><feGaussianBlur stdDeviation="6"/></filter>'''+GRAIN(.22)
    b='<rect width="1600" height="900" fill="url(#wall)"/><rect y="640" width="1600" height="260" fill="url(#floor)"/>'
    b+='<rect x="1080" y="150" width="300" height="260" rx="14" fill="url(#win)"/><path d="M1080,410 L1380,410 L1000,760 L560,760Z" fill="url(#beam)"/>'
    b+='<g filter="url(#bl2)"><rect x="620" y="470" width="120" height="180" rx="26" fill="#6b4a63"/><circle cx="760" cy="540" r="60" fill="#7a5568"/></g>'
    for i,(k,x,y,s) in enumerate(PLACE):
        p=POSES[k]; arms,legs,head=parts(p)
        sh=f'<ellipse cx="{p["Hp"][0]}" cy="2" rx="62" ry="12" fill="#000" opacity=".4" filter="url(#soft)"/>'
        def clay_line(pts,w):
            return lim(pts,w+3,'#7a4430',2,3)+lim(pts,w,'#d98b5c')+lim(pts,w*.35,'#ffd9b3',-w*.18,-w*.2,'filter="url(#soft)" opacity=".9"')
        body=''
        for L in legs: body+=clay_line(L,20)
        body+=clay_line([(p['Hp'][0],p['Hp'][1]),(p['S'][0],p['S'][1]+8)],48)
        for A in arms: body+=clay_line(A,17)
        hx,hy=head
        body+=f'<g transform="translate({hx},{hy}) rotate({p["hd"]})"><path d="{EGG}" fill="url(#hg)"/>{tuft("#7a4430",5)}{face(p,"#2a1a20")}</g>'
        b+=wrap(x,y,s,sh+body)
    b+='<rect x="30" y="0" width="90" height="900" fill="#8a5a3a" filter="url(#bl)" opacity=".85"/>'
    return svg(defs,b,'STYLE 1 - CLAY FIGURE (matte clay shading, egg head, soft studio light, grain)','<rect width="1600" height="900" filter="url(#gr)" opacity="1" style="mix-blend-mode:multiply"/>')

# ---------- 2 PAPER CUT ----------
def paper():
    defs='''<filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="7"/></filter>
    <filter id="ds" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="6" dy="9" stdDeviation="5" flood-color="#000" flood-opacity=".55"/></filter>
    <filter id="ds2" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="3" dy="5" stdDeviation="2.5" flood-color="#000" flood-opacity=".6"/></filter>
    <filter id="fib"><feTurbulence type="fractalNoise" baseFrequency=".9 .12" numOctaves="3" seed="8"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .5 -.1"/></filter>
    <filter id="bl"><feGaussianBlur stdDeviation="14"/></filter>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2a4a"/><stop offset="1" stop-color="#3d5a80"/></linearGradient>'''
    b='<rect width="1600" height="900" fill="url(#sky)"/>'
    b+='<g filter="url(#ds)"><circle cx="1180" cy="260" r="110" fill="#f4d58d" filter="url(#rough)"/></g>'
    b+='<g filter="url(#ds)"><path d="M0,520 Q250,380 520,470 T1040,430 T1600,480 L1600,900 L0,900Z" fill="#2d4a6b" filter="url(#rough)"/></g>'
    b+='<g filter="url(#ds)"><path d="M0,600 Q300,500 640,580 T1250,540 T1600,590 L1600,900 L0,900Z" fill="#355f73" filter="url(#rough)"/></g>'
    b+='<g filter="url(#ds)"><path d="M0,690 Q400,630 800,680 T1600,670 L1600,900 L0,900Z" fill="#c76b4a" filter="url(#rough)"/></g>'
    for k,x,y,s in PLACE:
        p=POSES[k]; arms,legs,head=parts(p)
        body=''
        for L in legs: body+=lim(L,20,'#f3ead7')
        body+=lim([(p['Hp'][0],p['Hp'][1]),(p['S'][0],p['S'][1]+8)],48,'#f3ead7')
        for A in arms: body+=lim(A,17,'#f3ead7')
        hx,hy=head
        body+=f'<g transform="translate({hx},{hy}) rotate({p["hd"]})"><path d="{EGG}" fill="#f3ead7"/>{tuft("#e08a3c",7)}{face(p,"#1d1a24",hi=False)}</g>'
        b+=wrap(x,y,s,f'<g filter="url(#ds2)"><g filter="url(#rough)">{body}</g></g>')
    b+='<g filter="url(#ds)"><path d="M0,830 Q200,790 420,830 T900,820 T1600,835 L1600,900 L0,900Z" fill="#1a1626" filter="url(#rough)"/></g>'
    b+='<rect x="30" y="0" width="90" height="900" fill="#1a1626" filter="url(#bl)" opacity=".9"/>'
    return svg(defs,b,'STYLE 2 - PAPER-CUT DIORAMA (layered paper, real shadows between layers, fibre)','<rect width="1600" height="900" filter="url(#fib)" opacity=".5" style="mix-blend-mode:overlay"/>')

# ---------- 3 TOON NOODLE ----------
def toon():
    defs='''<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b2350"/><stop offset=".62" stop-color="#4b3a86"/><stop offset=".62" stop-color="#e9b86a"/><stop offset="1" stop-color="#c98f45"/></linearGradient>
    <filter id="bl"><feGaussianBlur stdDeviation="14"/></filter><filter id="bl2"><feGaussianBlur stdDeviation="5"/></filter>'''+GRAIN(.18,f='1.2')
    b='<rect width="1600" height="900" fill="url(#bg)"/>'
    b+='<g stroke="#120d24" stroke-width="7" stroke-linejoin="round"><rect x="1080" y="140" width="320" height="270" fill="#ffe08f"/><path d="M1240,140V410M1080,275H1400" fill="none"/></g>'
    b+='<g filter="url(#bl2)"><rect x="620" y="470" width="130" height="170" rx="14" fill="#6a56b0" stroke="#120d24" stroke-width="7"/></g>'
    for k,x,y,s in PLACE:
        p=POSES[k]; arms,legs,head=parts(p)
        O='#120d24'; B='#7fb7ff'; Sh='#4a7fd0'; Hi='#d4ebff'
        def tl(pts,w):
            return lim(pts,w+12,O)+lim(pts,w,B)+lim(pts,w*.5,Sh,w*.22,w*.25)+lim(pts,w*.18,Hi,-w*.2,-w*.22)
        body=f'<ellipse cx="{p["Hp"][0]}" cy="3" rx="58" ry="10" fill="#7a4a1a" opacity=".6"/>'
        for L in legs: body+=tl(L,20)
        body+=tl([(p['Hp'][0],p['Hp'][1]),(p['S'][0],p['S'][1]+8)],48)
        for A in arms: body+=tl(A,17)
        hx,hy=head
        body+=f'<g transform="translate({hx},{hy}) rotate({p["hd"]})"><path d="{EGG}" fill="{O}" stroke="{O}" stroke-width="10" stroke-linejoin="round"/><path d="{EGG}" fill="{B}"/><path d="M40,10 C40,38 22,52 0,52 C-22,52 -40,38 -40,10 C-30,34 8,40 40,10Z" fill="{Sh}"/><path d="M-30,-22 C-26,-34 -14,-42 -4,-44" stroke="{Hi}" stroke-width="7" fill="none" stroke-linecap="round"/>{tuft(O,8)}{face(p,O)}</g>'
        b+=wrap(x,y,s,body)
    b+='<rect x="30" y="0" width="90" height="900" fill="#120d24" filter="url(#bl)" opacity=".9"/>'
    return svg(defs,b,'STYLE 3 - TOON 3D NOODLE (ink outline, two-tone cel shading; real 3D version would rotate)','<rect width="1600" height="900" filter="url(#gr)" style="mix-blend-mode:multiply"/>')

# ---------- 4 GLASS LANTERN ----------
def lantern():
    defs='''<radialGradient id="bg" cx=".5" cy=".45" r=".8"><stop offset="0" stop-color="#1d1a3a"/><stop offset="1" stop-color="#07060f"/></radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="core"><feGaussianBlur stdDeviation="14"/></filter><filter id="bl"><feGaussianBlur stdDeviation="16"/></filter><filter id="bl2"><feGaussianBlur stdDeviation="5"/></filter>'''
    cols={'calm':('#ffc46b','#ffe9c2'),'alarm':('#ff5a5a','#ffd0c8'),'awe':('#5fd8ff','#d6f6ff')}
    b='<rect width="1600" height="900" fill="url(#bg)"/><rect y="700" width="1600" height="200" fill="#0b0a18"/>'
    b+='<g filter="url(#bl2)" opacity=".5">'+''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>' for cx,cy,r,c in [(300,300,26,'#ff9a5c'),(720,230,18,'#5fd8ff'),(1450,330,30,'#a56bff'),(1100,160,16,'#ff9a5c'),(160,520,20,'#5fd8ff')])+'</g>'
    for k,x,y,s in PLACE:
        p=POSES[k]; arms,legs,head=parts(p); c,cc=cols[p['emo']]
        def gl(pts,w): return lim(pts,w+4,c,0,0,'opacity=".35"')+lim(pts,w,c,0,0,'opacity=".18"')+lim(pts,w*.3,cc,0,0,'opacity=".75"')
        def fig():
            s_=''
            for L in legs: s_+=gl(L,20)
            s_+=gl([(p['Hp'][0],p['Hp'][1]),(p['S'][0],p['S'][1]+8)],48)
            for A in arms: s_+=gl(A,17)
            hx,hy=head
            s_+=f'<g transform="translate({hx},{hy}) rotate({p["hd"]})"><path d="{EGG}" fill="{c}" fill-opacity=".22" stroke="{cc}" stroke-width="3"/><ellipse cx="0" cy="8" rx="22" ry="26" fill="{cc}" opacity=".85" filter="url(#core)"/>{tuft(cc,4)}{face(p,"#0a0814",hi=False)}</g>'
            s_+=f'<ellipse cx="{p["Hp"][0]*.5+p["S"][0]*.5}" cy="-118" rx="14" ry="26" fill="{cc}" opacity=".95" filter="url(#core)"/>'
            return s_
        ref=f'<g transform="translate(0,0) scale(1,-1)" opacity=".18">{fig()}</g>'
        b+=wrap(x,y,s,ref+f'<g filter="url(#glow)">{fig()}</g>')
    b+='<rect x="30" y="0" width="90" height="900" fill="#3a2a6a" filter="url(#bl)" opacity=".6"/>'
    return svg(defs,b,'STYLE 4 - GLASS LANTERN (translucent figure, inner light = emotion: amber calm / red alarm / cyan awe)')

# ---------- 5 CHARCOAL ----------
def charcoal():
    defs='''<filter id="ch"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="3" seed="2" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="5"/></filter>
    <filter id="ch2"><feTurbulence type="fractalNoise" baseFrequency=".08" numOctaves="3" seed="9" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="6"/></filter>
    <filter id="sm"><feGaussianBlur stdDeviation="9"/></filter><filter id="bl"><feGaussianBlur stdDeviation="15"/></filter>
    <filter id="pap"><feTurbulence type="fractalNoise" baseFrequency=".6" numOctaves="4" seed="5"/><feColorMatrix values="0 0 0 0 .2  0 0 0 0 .18  0 0 0 0 .15  0 0 0 .55 -.12"/></filter>'''
    b='<rect width="1600" height="900" fill="#d9d3c3"/>'
    b+='<g filter="url(#sm)" opacity=".35"><ellipse cx="1240" cy="250" rx="220" ry="150" fill="#fff6d8"/></g>'
    b+='<g filter="url(#ch)" stroke="#2b2824" stroke-width="5" fill="none" stroke-linecap="round" opacity=".85"><path d="M1080,150 H1390 V410 H1080Z M1235,150 V410 M1080,280 H1390"/><path d="M0,640 H1600" stroke-width="4"/><path d="M600,640 V480 H760 V640"/></g>'
    b+='<g filter="url(#sm)" opacity=".4" fill="#2b2824"><rect x="0" y="650" width="1600" height="30"/></g>'
    for k,x,y,s in PLACE:
        p=POSES[k]; arms,legs,head=parts(p)
        sm=f'<ellipse cx="{p["Hp"][0]+20}" cy="4" rx="70" ry="12" fill="#2b2824" opacity=".35" filter="url(#sm)"/>'
        def cl(pts,w): return lim(pts,3.6,'#2b2824')+lim(pts,3,'#2b2824',2.2,-1.5,'opacity=".6"')
        body=''
        for L in legs: body+=cl(L,0)
        body+=f'<path d="{P([(p["Hp"][0]-18,p["Hp"][1]),(p["S"][0]-20,p["S"][1]+10),(p["S"][0]+20,p["S"][1]+10),(p["Hp"][0]+18,p["Hp"][1])])}Z" fill="#2b2824" fill-opacity=".1" stroke="#2b2824" stroke-width="3.6" stroke-linejoin="round"/>'
        body+=''.join(f'<path d="M{p["Hp"][0]+10+i*5},{p["Hp"][1]-4} L{p["S"][0]+14+i*5-8},{p["S"][1]+16}" stroke="#2b2824" stroke-width="1.6" opacity=".5"/>' for i in range(4))
        for A in arms: body+=cl(A,0)
        hx,hy=head
        body+=f'<g transform="translate({hx},{hy}) rotate({p["hd"]})"><path d="{EGG}" fill="#efe9d8" stroke="#2b2824" stroke-width="3.6"/><path d="{EGG}" fill="none" stroke="#2b2824" stroke-width="2.6" opacity=".55" transform="translate(3,-2)"/><path d="M20,-30 Q38,0 26,36 M14,-34 Q32,0 20,40" stroke="#2b2824" stroke-width="1.8" opacity=".5" fill="none"/>{tuft("#2b2824",3.6)}{face(p,"#2b2824",hi=False)}</g>'
        b+=wrap(x,y,s,sm+f'<g filter="url(#ch2)">{body}</g>')
    b+='<rect x="30" y="0" width="90" height="900" fill="#2b2824" filter="url(#bl)" opacity=".8"/>'
    return svg(defs,b,'STYLE 5 - CHARCOAL PUPPET (rough charcoal lines, hand wobble, grainy paper)','<rect width="1600" height="900" filter="url(#pap)"/>')

import os
out=os.path.dirname(os.path.abspath(__file__))
styles={'1-clay':clay,'2-paper-cut':paper,'3-toon-noodle':toon,'4-glass-lantern':lantern,'5-charcoal':charcoal}
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    br=pw.chromium.launch(); pg=br.new_page(viewport={'width':W,'height':H})
    for n,f in styles.items():
        s=f(); open(f'{out}/style-{n}.svg','w').write(s)
        pg.set_content(f'<body style="margin:0;background:#000">{s}</body>'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{out}/style-{n}.png')
    br.close()
print('ok')
