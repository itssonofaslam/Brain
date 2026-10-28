import cv2, numpy as np
import sys; V=sys.argv[1]
cap=cv2.VideoCapture(V)
prev=None; rows=[]; i=0
H,W=180,320
ys,xs=np.mgrid[0:H,0:W]
xc=(xs-W/2)/(W/2); yc=(ys-H/2)/(H/2)
# bar detection on first frame
while True:
    ok,f=cap.read()
    if not ok: break
    if i==0:
        pass
    g=cv2.cvtColor(cv2.resize(f,(W,H),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2GRAY)
    if prev is not None:
        fl=cv2.calcOpticalFlowFarneback(prev,g,None,0.5,3,15,3,5,1.2,0)
        # exclude letterbox bars (top/bottom 12%)
        sl=slice(int(H*0.13),int(H*0.87))
        fx=fl[sl,:,0]; fy=fl[sl,:,1]
        mx=float(np.median(fx)); my=float(np.median(fy))
        # fraction of pixels moving > 0.3 px (320 scale)
        mag=np.hypot(fx,fy); frac=float((mag>0.3).mean())
        # zoom estimate: regress flow on position (affine radial)
        X=xc[sl,:].ravel(); Y=yc[sl,:].ravel()
        zx=float(np.polyfit(X,fx.ravel(),1)[0]); zy=float(np.polyfit(Y,fy.ravel(),1)[0])
        rows.append((i,mx*4,my*4,frac,zx*4,zy*4))  # *4 -> 1280 px
    else:
        rows.append((i,0,0,0,0,0))
    prev=g; i+=1
np.savetxt("scan2.csv",np.array(rows),delimiter=",",header="frame,medx_px,medy_px,movingfrac,zoomx_px,zoomy_px",comments="",fmt="%.4f")
print("done",i)
