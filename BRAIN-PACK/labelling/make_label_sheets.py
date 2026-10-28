import cv2,numpy as np,csv,sys,json,os
A="/mnt/user-data/attachments/987209c0-ab8b-5474-a18c-0cc37c3a215a/"
R={"ref1":("video","b1e0adc9-What_IF_You_Could_Move_Things_With_Your_Mind.mp4"),
"ref2":("video2","eb1a3b93-What_If_Your_Reaction_Time_Was_10x_Faster.mp4"),
"ref3":("video3","ff400638-What_If_One_Second_Felt_Like_Ten.mp4"),
"ref4":("video4","cfc65b88-What_If_You_Used_500_IQ_to_Disappear.mp4"),
"ref5":("video5","/home/claude/stickman/video5/joined.mp4")}
k=sys.argv[1]; d,v=R[k]
cap=cv2.VideoCapture(v if v.startswith("/") else A+v); fps=cap.get(5)
cuts=sorted(set([0]+[int(float(r["frame"])) for r in csv.DictReader(open(d+"/cuts_auto.csv"))]+[int(cap.get(7))]))
shots=[]
for a,e in zip(cuts[:-1],cuts[1:]):
    if (e-a)/fps>=0.5: shots.append((len(shots),round(a/fps,2),round((e-a)/fps,2)))
json.dump(shots,open("labelling/%s_shots.json"%k,"w"))
PER=30
for si in range(0,len(shots),PER):
    tiles=[]
    for idx,t,dur in shots[si:si+PER]:
        cap.set(1,int((t+dur/2)*fps)); ok,f=cap.read()
        f=cv2.resize(f,(256,144)) if ok else np.zeros((144,256,3),np.uint8)
        cv2.rectangle(f,(0,0),(46,20),(0,0,0),-1); cv2.putText(f,str(idx),(3,16),0,0.6,(0,255,255),2)
        tiles.append(f)
    while len(tiles)%6: tiles.append(np.zeros((144,256,3),np.uint8))
    rows=[np.hstack(tiles[i:i+6]) for i in range(0,len(tiles),6)]
    cv2.imwrite("labelling/%s_sheet%02d.png"%(k,si//PER+1),np.vstack(rows))
print(k,len(shots),"shots",(len(shots)+PER-1)//PER,"sheets")
