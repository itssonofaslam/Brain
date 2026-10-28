import numpy as np,json,csv,collections
dirs={'ref1':'video','ref2':'video2','ref3':'video3','ref4':'video4','ref5':'video5'}
rows=[]
for r,d in dirs.items():
    s=np.genfromtxt(f'{d}/scan2.csv',delimiter=',',names=True)
    sh=json.load(open(f'labelling/{r}_shots.json'))
    lab={int(a):b for a,b in csv.reader(open(f'labelling/labels_{r}.csv'))}
    for i,st,du in sh:
        a=int(round(st*24)); e=int(round((st+du)*24))
        seg=s[a+2:e-1]
        l=lab[i]; c=l[0]
        if len(seg)<6: kind='short';z=px=py=0
        else:
            px=seg['medx_px'].sum();py=seg['medy_px'].sum();z=(seg['zoomx_px']+seg['zoomy_px']).sum()
            if abs(z)>40 and abs(z)*1.0>(abs(px)+abs(py))*0.5: kind='push' if z>0 else 'pull'
            elif abs(px)>8 and abs(px)>=abs(py): kind='pan'
            elif abs(py)>8: kind='tilt'
            else: kind='locked'
        rows.append((r,i,c,l,kind,du,z,px,py))
json.dump(rows,open('labelling/camstats.json','w'))
kinds=['locked','push','pull','pan','tilt','short']
md='# Camera move by shot type (all 5 videos; shots<0.5s = short)\nsign assumption: zoom-idx >0 = push-in (zoom in), <0 = pull-out\n\n| code | n | locked% | push% | pull% | pan% | tilt% |\n|---|---|---|---|---|---|---|\n'
codes='WMCXOHUTDEB'
for c in codes:
    rr=[x for x in rows if x[2]==c and x[4]!='short']
    if not rr: continue
    k=collections.Counter(x[4] for x in rr)
    md+=f'| {c} | {len(rr)} | '+' | '.join(f'{100*k[q]/len(rr):.0f}' for q in kinds[:5])+' |\n'
rr=[x for x in rows if x[4]!='short'];k=collections.Counter(x[4] for x in rr)
md+=f'| ALL | {len(rr)} | '+' | '.join(f'{100*k[q]/len(rr):.0f}' for q in kinds[:5])+' |\n'
# by flag
md+='\n## by flag\n| flag | n | locked% | push% | pull% | pan% | tilt% |\n|---|---|---|---|---|---|---|\n'
for f in 'peotsk':
    rr=[x for x in rows if x[4]!='short' and f in (x[3].split('.',1)[1] if '.' in x[3] else '')]
    if rr:
        k=collections.Counter(x[4] for x in rr);md+=f'| {f} | {len(rr)} | '+' | '.join(f'{100*k[q]/len(rr):.0f}' for q in kinds[:5])+' |\n'
# mean hold of moving vs locked
for q in ['locked','push','pull','pan','tilt']:
    rr=[x[5] for x in rows if x[4]==q]
    if rr: md+=f'\n- mean hold {q}: {np.mean(rr):.2f}s (n={len(rr)})'
open('labelling/CAMERA-BY-SHOT-TYPE.md','w').write(md);print(md)
