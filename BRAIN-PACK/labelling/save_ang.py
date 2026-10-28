import sys,csv,os
ref=sys.argv[1];fn=f'angles_{ref}.csv'
d={}
if os.path.exists(fn):
    for a,b in csv.reader(open(fn)): d[int(a)]=b
for p in sys.argv[2].split():
    a,b=p.split(':');d[int(a)]=b
open(fn,'w').write(''.join(f'{k},{v}\n' for k,v in sorted(d.items())));print(ref,len(d),'tagged')
