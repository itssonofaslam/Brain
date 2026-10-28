import numpy as np, cv2, json
A="/mnt/user-data/attachments/987209c0-ab8b-5474-a18c-0cc37c3a215a/"
R={"ref1":("video","b1e0adc9-What_IF_You_Could_Move_Things_With_Your_Mind.mp4"),
"ref2":("video2","eb1a3b93-What_If_Your_Reaction_Time_Was_10x_Faster.mp4"),
"ref3":("video3","ff400638-What_If_One_Second_Felt_Like_Ten.mp4"),
"ref4":("video4","cfc65b88-What_If_You_Used_500_IQ_to_Disappear.mp4"),
"ref5":("video5","/home/claude/stickman/video5/joined.mp4")}
import sys
ONLY=sys.argv[1:] 
out={}
for k,(d,v) in R.items():
    if ONLY and k not in ONLY: continue
    cap=cv2.VideoCapture(v if v.startswith("/") else A+v); fps=cap.get(5); N=int(cap.get(7))
    s=np.genfromtxt(d+"/scan1.csv",delimiter=",",names=True); df=s["diff"]; mean=s["mean"]
    n=len(df); sc=fps/24.0
    # cuts (same rule for all)
    cuts=[]
    for i in range(2,n-2):
        nb=np.r_[df[max(0,i-6):i-1],df[i+2:i+7]]
        if df[i]>8 and df[i]>3*(np.median(nb)+1) and df[i]>=df[i-1] and df[i]>=df[i+1]: cuts.append(i)
    gaps=np.diff(cuts)/fps
    real=gaps[gaps>=0.25]
    # camera locked share
    s2=np.genfromtxt(d+"/scan2.csv",delimiter=",",names=True)
    b=sorted(set([0]+cuts+[n])); lock=tot=0
    for a,e in zip(b[:-1],b[1:]):
        if e-a<12: continue
        seg=s2[a+2:e-1]
        if len(seg)<6: continue
        tot+=1
        px=seg["medx_px"].sum(); py=seg["medy_px"].sum(); z=(seg["zoomx_px"]+seg["zoomy_px"]).sum()
        if not(abs(px)>8 or abs(py)>8 or abs(z)>40): lock+=1
    # flash frames: brightness spike
    fl=[]
    if mean.max()>0:
        for i in range(12,n-12):
            ref=np.median(np.r_[mean[i-12:i-3],mean[i+4:i+13]])
            if mean[i]>1.5*ref+12: fl.append(i)
    runs=[];
    for f in fl:
        if runs and f-runs[-1][-1]<=1: runs[-1].append(f)
        else: runs.append([f])
    rl=[len(r) for r in runs if len(r)<=8]
    # letterbox + darkness over sampled frames
    dark=[];L=[];top=[];bot=[]
    dur=N/fps
    for t in np.arange(1,dur-1,2):
        cap.set(1,int(t*fps)); ok,f=cap.read()
        if not ok: break
        g=f.mean(2).mean(1)
        top.append(next((i for i in range(0,120) if g[i]>3),0)); bot.append(next((i for i in range(0,120) if g[719-i]>3),0))
        c=f[44:676]; lum=c.mean(2); dark.append((lum<35).mean())
        L.append(cv2.cvtColor(cv2.resize(c,(64,32)),cv2.COLOR_BGR2LAB)[:,:,0].mean()*100/255)
    out[k]=dict(fps=fps,frames=N,dur=round(dur,1),cuts=len(cuts),shots_real=len(real),mean_shot=round(float(real.mean()),2),median_shot=round(float(np.median(real)),2),
        sub025=int((gaps<0.25).sum()),locked=round(100*lock/tot),n_shots=tot,flash_runs=len(rl),flash_len_median=(float(np.median(rl)) if rl else None),
        flash_len_dist={int(x):int(c) for x,c in zip(*np.unique(rl,return_counts=True))} if rl else {},
        letterbox_top_median=int(np.median(top)),letterbox_bot_median=int(np.median(bot)),near_black_pct=round(100*float(np.mean(dark))),meanL=round(float(np.mean(L)),1))
    print(k,out[k],flush=True)
import os
old=json.load(open("metrics_all.json")) if os.path.exists("metrics_all.json") else {}
old.update(out); json.dump(old,open("metrics_all.json","w"),indent=1)
