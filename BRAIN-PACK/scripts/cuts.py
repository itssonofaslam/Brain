import numpy as np
s=np.genfromtxt("scan1.csv",delimiter=",",names=True); d=s["diff"]; m=s["mean"]
out=[]
for i in range(2,len(d)-2):
    nb=np.r_[d[max(0,i-6):i-1],d[i+2:i+7]]
    if d[i]>8 and d[i]>3*(np.median(nb)+1) and d[i]>=d[i-1] and d[i]>=d[i+1]:
        out.append((i,i/24,d[i],m[i-1],m[i]))
np.savetxt("cuts_auto.csv",np.array(out),delimiter=",",header="frame,sec,diff,mean_before,mean_after",comments="",fmt="%.3f")
f=np.array([o[0] for o in out]); gaps=np.diff(f)/24
print(len(out),"cuts, mean shot %.2f s, median %.2f, <0.25s: %d"%(gaps.mean(),np.median(gaps),(gaps<0.25).sum()))
