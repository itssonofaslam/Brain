import cv2,numpy as np,csv,collections
import sys
D,V,fps=sys.argv[1],sys.argv[2],float(sys.argv[3])
s1=np.genfromtxt(D+"/scan1.csv",delimiter=",",names=True)
cuts=sorted(set([0]+[int(float(r["frame"])) for r in csv.DictReader(open(D+"/cuts_auto.csv"))]+[len(s1)]))
cuts_set=set(cuts)
d=s1["diff"]
cands={"linear":lambda u:u,"easeIn2":lambda u:u*u,"easeIn3":lambda u:u**3,"easeOut2":lambda u:1-(1-u)**2,"easeOut3":lambda u:1-(1-u)**3,
"easeInOut2":lambda u:np.where(u<.5,2*u*u,1-(-2*u+2)**2/2),"easeInOut3":lambda u:np.where(u<.5,4*u**3,1-(-2*u+2)**3/2),"step":lambda u:(u>0.5).astype(float)}
# find motion runs inside shots
runs=[]
for a,e in zip(cuts[:-1],cuts[1:]):
    if e-a<40: continue
    i=a+4
    while i<e-6:
        if d[i]>0.6:
            j=i
            while j<e-3 and d[j]>0.35: j+=1
            n=j-i
            if 8<=n<=40 and (j+8<e): runs.append((max(i-3,a+2),min(j+4,e-2)))
            i=j+3
        else: i+=1
print("runs",len(runs))
cap=cv2.VideoCapture(V)
def frames(a,b):
    cap.set(1,a); out=[]
    for _ in range(a,b+1):
        ok,f=cap.read()
        if not ok: break
        out.append(cv2.resize(cv2.cvtColor(f[44:676],cv2.COLOR_BGR2GRAY),(192,76)).astype(np.float32))
    return out
rows=[]
for a,b in runs:
    F=frames(a,b)
    if len(F)<8: continue
    d0=np.abs(F[0]-F[-1]).mean()
    if d0<1.5: continue
    p=np.clip(np.array([1-np.abs(f-F[-1]).mean()/d0 for f in F]),0,1.2)
    u=np.linspace(0,1,len(F)); best=None
    for k,fn in cands.items():
        e=np.sqrt(((p-fn(u))**2).mean())
        if best is None or e<best[1]: best=(k,e)
    t=lambda th:int(np.where(p>=th)[0][0]) if (p>=th).any() else -1
    rows.append((a,b,best[0],best[1],t(.1),t(.5),t(.9),p.max()>1.05))
good=[r for r in rows if r[3]<0.12]
cnt=collections.Counter(r[2] for r in good)
L=["# REF4 measured easing (24 fps, auto-detected motion runs inside shots)","",
"Method: runs of in-shot motion (scan1 diff) 8-40 f, progress p(t)=1-|f_t-f_end|/|f_0-f_end| on gray 192x76 inside the letterbox, best fit among standard curves. rmse<0.12 = reliable. t10/t50/t90 = frames to reach 10/50/90%.",
"Runs found: %d, measurable: %d, reliable fits: %d"%(len(runs),len(rows),len(good)),"",
"## Distribution of best fits (reliable only)"]
for k,v in cnt.most_common(): L.append("- %s: %d (%.0f%%)"%(k,v,100*v/max(1,len(good))))
dur=collections.defaultdict(list)
for r in good: dur[r[2]].append(r[1]-r[0])
L+=["","## Median run length (frames) per curve"]
for k,v in dur.items(): L.append("- %s: median %d f (%.2f s), n=%d"%(k,np.median(v),np.median(v)/fps,len(v)))
ov=sum(1 for r in good if r[7]); L.append("\nOvershoot (p>1.05) in %d of %d reliable runs."%(ov,len(good)))
L+=["","## All reliable events","| frames | time s | len f | fit | rmse | t10 | t50 | t90 | overshoot |","|---|---|---|---|---|---|---|---|---|"]
for r in good: L.append("| %d-%d | %.2f | %d | %s | %.2f | %d | %d | %d | %s |"%(r[0],r[1],r[0]/fps,r[1]-r[0],r[2],r[3],r[4],r[5],r[6],"yes" if r[7] else ""))
open(D+"/easing-auto.md","w").write("\n".join(L)); print("\n".join(L[:20]))
