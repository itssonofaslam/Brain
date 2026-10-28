import cv2,numpy as np
V=open("V.txt").read().strip(); cap=cv2.VideoCapture(V)
def hexc(c): return "#%02x%02x%02x"%tuple(int(x) for x in c[::-1])
L=["# REF5 palette (k-means k=5 on frames every 2 s inside the letterbox, grouped by 120 s block)",""]
allpix=[]; dark=0; n=0
blocks={}
for t in range(1,1455,4):
    cap.set(1,t*24); ok,f=cap.read()
    if not ok: break
    s=cv2.resize(f[44:676],(96,48),interpolation=cv2.INTER_AREA)
    px=s.reshape(-1,3).astype(np.float32)
    lum=px.mean(1); dark+=(lum<35).mean(); n+=1
    blocks.setdefault(t//120,[]).append(px[::3])
    allpix.append(px[::6])
L.append("Share of pixels with luminance <35 (near-black), averaged over frames: %.0f%%  (ref3 was >50%%)"%(100*dark/n)); L.append("")
crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,1.0)
for b,v in sorted(blocks.items()):
    X=np.vstack(v); _,lab,cen=cv2.kmeans(X,6,None,crit,3,cv2.KMEANS_PP_CENTERS)
    cnt=np.bincount(lab.ravel(),minlength=6); o=np.argsort(-cnt)
    L.append("- %3d-%3ds: "%(b*120,b*120+120)+" ".join("%s(%d%%)"%(hexc(cen[i]),100*cnt[i]/cnt.sum()) for i in o))
X=np.vstack(allpix); _,lab,cen=cv2.kmeans(X,10,None,crit,3,cv2.KMEANS_PP_CENTERS)
cnt=np.bincount(lab.ravel(),minlength=10); o=np.argsort(-cnt)
L+=["","## Whole-video top colours",", ".join("%s %d%%"%(hexc(cen[i]),100*cnt[i]/cnt.sum()) for i in o)]
open("ref5-palette.md","w").write("\n".join(L)); print("\n".join(L))
