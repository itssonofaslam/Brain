import cv2,numpy as np,sys
V=sys.argv[1]; out=sys.argv[2]
cap=cv2.VideoCapture(V); rows=[]; i=0; prev=None
while True:
    ok,f=cap.read()
    if not ok: break
    s=cv2.resize(f[44:676],(64,32),interpolation=cv2.INTER_AREA).astype(np.float32)  # BGR
    m=s.reshape(-1,3).mean(0)  # B,G,R
    lab=cv2.cvtColor(s/255.0,cv2.COLOR_BGR2LAB).reshape(-1,3).mean(0)
    n=s/(m+1e-3)   # grade-normalised structure
    ds=0 if prev is None else float(np.abs(n-prev).mean()*100)
    rows.append((i,m[2],m[1],m[0],lab[0],lab[1],lab[2],ds)); prev=n; i+=1
np.savetxt(out,np.array(rows),delimiter=",",header="frame,R,G,B,L,a,b,struct",comments="",fmt="%.3f")
print("frames",i)
