import json,csv,collections,os
refs=['ref1','ref2','ref3','ref4','ref5']
names={'L':'low angle (look up)','V':'high angle/looking down','D':'top-down (shot code D)','S':'scale contrast (tiny vs vast / giant)','F':'foreground-frame (OTS, bars, net, bokeh, blurred silhouette)','R':'frame-in-frame (window/screen/porthole/poster/face-detect box)','P':'POV / in-world camera (REC, cockpit, flashlight)','K':'backlit silhouette','Z':'dutch tilt'}
rows=[]
for r in refs:
    sh=json.load(open(f'{r}_shots.json'))
    lab={int(a):b for a,b in csv.reader(open(f'labels_{r}.csv'))}
    ang={int(a):b for a,b in csv.reader(open(f'angles_{r}.csv'))} if os.path.exists(f'angles_{r}.csv') else {}
    for i,s,d in sh:
        l=lab[i];c=l[0];fl=l.split('.',1)[1] if '.' in l else ''
        a=ang.get(i,'')
        if c=='D' and not a: a='D'
        rows.append(dict(r=r,i=i,s=s,d=d,c=c,fl=fl,a=a))
N=len(rows)
md=f'# ANGLE / FRAMING-TRICK STATS ({N} shots; default = eye-level, tagged only exceptions; D = top-down from shot code)\n\n## Share by video\n| angle | '+' | '.join(refs)+' | ALL |\n|---|'+'---|'*6+'\n'
tot=collections.Counter(x['r'] for x in rows)
for k in 'LVDSFRPKZ':
    cnt={r:sum(1 for x in rows if x['r']==r and k in x['a']) for r in refs}
    allc=sum(cnt.values())
    md+=f'| {k} {names[k].split(" (")[0]} | '+' | '.join(f'{100*cnt[r]/tot[r]:.0f}%' for r in refs)+f' | {100*allc/N:.1f}% ({allc}) |\n'
non=sum(1 for x in rows if x['a']=='' )
md+=f'\nShots with any non-default angle/trick: {100*(N-non)/N:.0f}%; plain eye-level: {100*non/N:.0f}%.\n'
# angle by shot code
md+='\n## Which shot sizes carry each trick (% of that trick)\n| trick | '+' | '.join('WMCXOHUTDEB')+' |\n|---|'+'---|'*11+'\n'
for k in 'LVDSFRPK':
    rr=[x for x in rows if k in x['a']]
    if rr:
        c=collections.Counter(x['c'] for x in rr)
        md+=f'| {k} (n={len(rr)}) | '+' | '.join(f'{100*c[q]/len(rr):.0f}' for q in 'WMCXOHUTDEB')+' |\n'
# share of each size that has a trick
md+='\n## Share of each shot size that carries any non-default angle/trick\n'
for q in 'WMCXOHUTDEB':
    rr=[x for x in rows if x['c']==q]
    if rr: md+=f'- {q}: {100*sum(1 for x in rr if x["a"])/len(rr):.0f}% (n={len(rr)})\n'
# by flags
md+='\n## Tricks vs story flags\n'
for f,nm in [('p','new place'),('e','emotional beat'),('s','action pose'),('t','two-shot'),('o','OTS')]:
    rr=[x for x in rows if f in x['fl']]
    c=collections.Counter(k for x in rr for k in x['a'])
    md+=f'- {nm} (n={len(rr)}): trick on {100*sum(1 for x in rr if x["a"])/len(rr):.0f}%; split: '+', '.join(f'{k} {v}' for k,v in c.most_common())+'\n'
# repeat rate: consecutive shots with identical (code,angle)
rep=0;tr=0;newang=0
for r in refs:
    rr=[x for x in rows if x['r']==r]
    for a,b in zip(rr,rr[1:]):
        tr+=1
        if (a['c'],a['a'])==(b['c'],b['a']): rep+=1
        if a['a']!=b['a']: newang+=1
md+=f'\n## Change at cut\n- consecutive shots with identical size+angle: {100*rep/tr:.0f}% (so {100-100*rep/tr:.0f}% of cuts change size or angle)\n- cuts where the angle/trick tag changes: {100*newang/tr:.0f}%\n'
# trick run lengths
runs=collections.Counter()
for r in refs:
    rr=[x for x in rows if x['r']==r];run=0
    for x in rr:
        if x['a'] and x['a']!='D': run+=1
        else:
            if run: runs[min(run,6)]+=1
            run=0
md+='- runs of consecutive tricked shots: '+', '.join(f'{k}: {v}' for k,v in sorted(runs.items()))+'\n'
# ref5 per 4-min block trick share
md+='\n## ref5 trick share by 4-min block\n| block | any | S | L | F | R | P | D |\n|---|---|---|---|---|---|---|---|\n'
rr5=[x for x in rows if x['r']=='ref5']
for b in range(6):
    z=[x for x in rr5 if b*240<=x['s']<(b+1)*240]
    if z: md+=f'| {4*b}-{4*b+4} | {100*sum(1 for x in z if x["a"])/len(z):.0f}% | '+' | '.join(f'{100*sum(1 for x in z if k in x["a"])/len(z):.0f}%' for k in 'SLFRPD')+' |\n'
# position: first 10% vs last 10%
md+='\n## Where tricks sit in the runtime (share of tricked shots in each tenth)\n'
for r in refs:
    rr=[x for x in rows if x['r']==r];T=rr[-1]['s']+rr[-1]['d']
    tenth=[0]*10;tt=[0]*10
    for x in rr:
        t=min(9,int(10*x['s']/T));tt[t]+=1
        if x['a']: tenth[t]+=1
    md+=f'- {r}: '+' '.join(f'{100*a/b:.0f}' if b else '-' for a,b in zip(tenth,tt))+'\n'
open('ANGLE-STATS.md','w').write(md);print(md)
