#!/bin/bash
# usage: run_ref.sh <dir e.g. video5> <mp4>   -- resumable: each step skips if its output exists
D=$1; V=$2; cd /home/claude/stickman; mkdir -p $D; S=/home/claude/stickman/video4
for f in scan1.py scan2.py grade_scan.py cuts.py cam_summary.py grade_summary.py palette.py easing3.py; do cp -n $S/$f $D/; done
cd $D; echo "$V" > V.txt
[ -s scan1.csv ] || python3 scan1.py "$V" > s1.log 2>&1 &
[ -s scan2.csv ] || python3 scan2.py "$V" > s2.log 2>&1 &
[ -s g.csv ] || python3 grade_scan.py "$V" g.csv > g.log 2>&1 &
[ -s audio-rms.csv ] || { ffmpeg -loglevel error -y -i "$V" -vn -ac 1 -ar 8000 -f f32le a.raw && python3 -c "
import numpy as np
a=np.fromfile('a.raw',dtype=np.float32);n=800
r=[np.sqrt((a[i:i+n]**2).mean()) for i in range(0,len(a)-n,n)]
np.savetxt('audio-rms.csv',np.array([(i/10,x) for i,x in enumerate(r)]),delimiter=',',header='t,rms',comments='',fmt='%.5f')"; } &
[ -s sheet1.png ] || ffmpeg -loglevel error -y -i "$V" -vf "fps=1/6,scale=320:-1,drawtext=text='%{pts\:hms}':x=6:y=6:fontcolor=white:fontsize=18:box=1:boxcolor=black@0.6,tile=5x5" sheet%d.png &
wait; echo "scans done"; python3 cuts.py; python3 cam_summary.py >/dev/null; sed -i 's/g4.csv/g.csv/' grade_summary.py; python3 grade_summary.py >/dev/null; python3 palette.py >/dev/null; echo "pipeline done" > DONE
