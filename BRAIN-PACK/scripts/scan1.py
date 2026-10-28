import cv2, numpy as np, csv, sys
import sys; V=sys.argv[1]
cap=cv2.VideoCapture(V)
prev=None; rows=[]; i=0
win=np.hanning(160)[None,:]*np.hanning(90)[:,None]
while True:
    ok,f=cap.read()
    if not ok: break
    g=cv2.cvtColor(cv2.resize(f,(160,90),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2GRAY).astype(np.float32)
    small=cv2.resize(f,(32,18),interpolation=cv2.INTER_AREA)
    mean=g.mean()
    if prev is None:
        rows.append((i,0,0,0,0,mean)); 
    else:
        d=np.abs(g-prev).mean()
        (dx,dy),resp=cv2.phaseCorrelate(prev*win,g*win)
        rows.append((i,round(float(d),3),round(float(dx),3),round(float(dy),3),round(float(resp),3),round(float(mean),2)))
    prev=g; i+=1
np.savetxt("scan1.csv",np.array(rows),delimiter=",",header="frame,diff,dx,dy,resp,mean",comments="",fmt="%.3f")
print("frames",i)
