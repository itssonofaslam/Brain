import sys,csv,os,json
k=sys.argv[1]; items=sys.argv[2].split()
f="labels_%s.csv"%k; have={}
if os.path.exists(f): have={int(r[0]):r[1] for r in csv.reader(open(f))}
for it in items:
    i,c=it.split(":"); have[int(i)]=c
w=csv.writer(open(f,"w")); [w.writerow([i,have[i]]) for i in sorted(have)]
n=len(json.load(open("%s_shots.json"%k)))
print(k,len(have),"of",n,"labelled; missing:",[i for i in range(n) if i not in have][:5])
