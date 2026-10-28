import json,csv,collections
refs=['ref1','ref2','ref3','ref4','ref5']
codes=list("WMCXOHUTDEB")
out=[];allrows=[]
D={}
for r in refs:
    sh=json.load(open(f'{r}_shots.json'))
    lab={int(a):b for a,b in csv.reader(open(f'labels_{r}.csv'))}
    rows=[]
    for i,s,d in sh:
        l=lab[i];c=l[0];fl=l.split('.',1)[1] if '.' in l else ''
        rows.append((i,s,d,c,fl))
    D[r]=rows;allrows+=[(r,)+x for x in rows]
def table(rows,name):
    n=len(rows);T=sum(x[2] for x in rows)
    s=f'\n### {name}  (shots {n}, {T/60:.1f} min)\n| code | shots % | time % | mean hold s |\n|---|---|---|---|\n'
    for c in codes:
        rr=[x for x in rows if x[3]==c]
        if rr: s+=f'| {c} | {100*len(rr)/n:.1f} | {100*sum(x[2] for x in rr)/T:.1f} | {sum(x[2] for x in rr)/len(rr):.2f} |\n'
    return s
md='# SHOT STATS from labelling (511+213+145+248+86 = 1203 shots)\n'
for r in refs: md+=table(D[r],r)
md+=table([x[1:] for x in allrows],'ALL VIDEOS')
# flags
allr=[x[1:] for x in allrows]
n=len(allr)
md+='\n### Flag frequency (all shots)\n'
for f in 'peotskm':
    k=sum(1 for x in allr if f in x[4]);md+=f'- {f}: {k} ({100*k/n:.1f}%)\n'
# new place -> what code
c=collections.Counter(x[3] for x in allr if 'p' in x[4]);tp=sum(c.values())
md+='\n### Shots flagged new-place (p): code split\n'+', '.join(f'{k} {100*v/tp:.0f}%' for k,v in c.most_common())+f' (n={tp})\n'
# emotional beats code split
c=collections.Counter(x[3] for x in allr if 'e' in x[4]);te=sum(c.values())
md+='\n### Emotional-beat (e) shots: code split\n'+', '.join(f'{k} {100*v/te:.0f}%' for k,v in c.most_common())+f' (n={te})\n'
# transitions (next code after X/C.e/O/W)
tr=collections.defaultdict(collections.Counter)
for r in refs:
    rows=D[r]
    for a,b in zip(rows,rows[1:]): tr[a[3]][b[3]]+=1
md+='\n### What follows each code (all videos, % of next shot)\n| after | '+' | '.join(codes)+' |\n|---|'+'---|'*len(codes)+'\n'
for a in codes:
    t=sum(tr[a].values())
    if t: md+=f'| {a} (n={t}) | '+' | '.join(f'{100*tr[a][b]/t:.0f}' for b in codes)+' |\n'
# run lengths of same code
rl=collections.Counter()
for r in refs:
    run=1
    for a,b in zip(D[r],D[r][1:]):
        if a[3]==b[3]: run+=1
        else: rl[min(run,8)]+=1;run=1
    rl[min(run,8)]+=1
md+='\n### Run length of same code in a row\n'+', '.join(f'{k}{"+" if k==8 else ""}: {rl[k]}' for k in sorted(rl))+'\n'
# gap between close faces (X or C.e) in ref5, by shots
for r in refs:
    pos=[i for i,x in enumerate(D[r]) if x[3]=='X' or (x[3]=='C' and 'e' in x[4])]
    g=[b-a for a,b in zip(pos,pos[1:])]
    if g: md+=f'\n{r}: face-emotion (X or C.e) count {len(pos)}, median gap {sorted(g)[len(g)//2]} shots, clusters (gap<=2) {100*sum(1 for x in g if x<=2)/len(g):.0f}%\n'
# ref5 per 4-min blocks
rows=D['ref5']
md+='\n### ref5 by 4-min block (share of shots)\n| block | W | M | C+X | O+H | U | D | E | n |\n|---|---|---|---|---|---|---|---|---|\n'
for b in range(6):
    rr=[x for x in rows if b*240<=x[1]<(b+1)*240]
    if not rr: continue
    k=lambda cs:100*sum(1 for x in rr if x[3] in cs)/len(rr)
    md+=f'| {b*4}-{b*4+4} | {k("W"):.0f} | {k("M"):.0f} | {k("CX"):.0f} | {k("OH"):.0f} | {k("U"):.0f} | {k("D"):.0f} | {k("E"):.0f} | {len(rr)} |\n'
# position: first/last shots
md+='\n### Opening and closing shot codes\n'
for r in refs: md+=f'- {r}: first 5 {"".join(x[3] for x in D[r][:5])}; last 5 {"".join(x[3] for x in D[r][-5:])}\n'
open('STATS.md','w').write(md);print(md)
