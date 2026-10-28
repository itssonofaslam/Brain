import numpy as np, csv
FPS=24
s=np.genfromtxt("scan2.csv",delimiter=",",names=True)
cuts=[int(float(r["frame"])) for r in csv.DictReader(open("cuts_auto.csv"))]
N=len(s); b=[0]+cuts+[N]
b=sorted(set(b))
moves=[];locked=0;total=0
for a,e in zip(b[:-1],b[1:]):
    if e-a<12: continue
    total+=1
    seg=s[a+2:e-1]  # skip cut frames
    if len(seg)<6: continue
    px=seg["medx_px"].sum(); py=seg["medy_px"].sum()
    z=(seg["zoomx_px"]+seg["zoomy_px"]).sum()
    pk=np.hypot(seg["medx_px"],seg["medy_px"]).max()
    if abs(px)>8 or abs(py)>8 or abs(z)>40:
        moves.append((a,e,px,py,z,pk))
    else: locked+=1
out=["# REF5 measured camera (1280x720, 24 fps, %d frames, %.2f s)"%(N,N/FPS),
"Shots >=0.5 s analysed: %d. Locked: %d (%.0f%%). Moves: %d."%(total,locked,100*locked/total,len(moves)),
"","## Moves (net pan/tilt > 8 px or zoom-idx > 40)"]
for a,e,px,py,z,pk in moves:
    out.append("- frames %d-%d (%.2f-%.2fs, %.1fs): pan %.0fpx tilt %.0fpx zoom-idx %.0f peak %.1fpx/f"%(a,e,a/FPS,e/FPS,(e-a)/FPS,px,py,z,pk))
open("ref5-camera-measured.md","w").write("\n".join(out))
print("\n".join(out))
