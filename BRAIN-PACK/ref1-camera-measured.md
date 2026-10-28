# Telekinesis - measured camera log (from mp4, 1280x720, 30fps)

Letterbox: 41 px black top + 41 px bottom (content 638 px tall, ~5.7% each).

Shots with net camera travel (|net| > 8 px or big zoom) - moves; rest = locked camera (net 0.0 px):

- frames 39-110 (1.30-3.67s): pan 0px, tilt -12px, zoom-index 22, peak 0.9px/f
- frames 887-955 (29.57-31.83s): pan -10px, tilt -0px, zoom-index -1, peak 0.8px/f
- frames 1909-1957 (63.63-65.23s): pan -80px, tilt 0px, zoom-index -1, peak 2.1px/f
- frames 1957-2081 (65.23-69.37s): pan 47px, tilt -1px, zoom-index 9, peak 0.5px/f
- frames 2147-2213 (71.57-73.77s): pan -182px, tilt 30px, zoom-index -0, peak 13.2px/f
- frames 2363-2545 (78.77-84.83s): pan -142px, tilt 0px, zoom-index -34, peak 4.2px/f
- frames 2545-2632 (84.83-87.73s): pan -0px, tilt -0px, zoom-index -274, peak 0.0px/f
- frames 3122-3163 (104.07-105.43s): pan 0px, tilt -0px, zoom-index 51, peak 0.0px/f
- frames 3163-3353 (105.43-111.77s): pan 0px, tilt 0px, zoom-index -64, peak 0.0px/f
- frames 3362-3415 (112.07-113.83s): pan -0px, tilt 0px, zoom-index -76, peak 0.1px/f
- frames 3697-3766 (123.23-125.53s): pan -24px, tilt -0px, zoom-index 6, peak 9.0px/f
- frames 3766-3813 (125.53-127.10s): pan -25px, tilt -0px, zoom-index -1, peak 9.2px/f
- frames 4103-4230 (136.77-141.00s): pan -0px, tilt -26px, zoom-index 19, peak 0.9px/f
- frames 4230-4284 (141.00-142.80s): pan -0px, tilt 53px, zoom-index -42, peak 2.8px/f
- frames 4284-4393 (142.80-146.43s): pan -8px, tilt -7px, zoom-index 60, peak 0.6px/f
- frames 4690-4841 (156.33-161.37s): pan 0px, tilt -33px, zoom-index -12, peak 1.5px/f
- frames 4841-4946 (161.37-164.87s): pan 0px, tilt -32px, zoom-index -52, peak 4.7px/f
- frames 5108-5126 (170.27-170.87s): pan -8px, tilt 0px, zoom-index -0, peak 4.8px/f
- frames 5461-5559 (182.03-185.30s): pan 0px, tilt 0px, zoom-index -43, peak 0.0px/f
- frames 6016-6198 (200.53-206.60s): pan -507px, tilt 2px, zoom-index -186, peak 3.9px/f
- frames 6366-6484 (212.20-216.13s): pan -11px, tilt -0px, zoom-index -10, peak 0.2px/f
- frames 6722-6842 (224.07-228.07s): pan -9px, tilt 88px, zoom-index -22, peak 3.6px/f
- frames 6842-7036 (228.07-234.53s): pan 0px, tilt 0px, zoom-index 47, peak 0.0px/f

Verdict: ~80% of shots have 0.0 px net motion = fully locked camera. Moves are rare, deliberate, ease-in-out; large values in effect shots (e.g. 6016-6198, 2363-2545) are in-frame motion (props/crowds), not camera.