# REF3 measured easing (24 fps, auto-detected motion runs inside shots)

Method: runs of in-shot motion (scan1 diff) 8-40 f, progress p(t)=1-|f_t-f_end|/|f_0-f_end| on gray 192x76 inside the letterbox, best fit among standard curves. rmse<0.12 = reliable. t10/t50/t90 = frames to reach 10/50/90%.
Runs found: 25, measurable: 25, reliable fits: 21

## Distribution of best fits (reliable only)
- easeInOut2: 9 (43%)
- easeIn3: 4 (19%)
- easeIn2: 4 (19%)
- linear: 2 (10%)
- easeOut2: 2 (10%)

## Median run length (frames) per curve
- easeInOut2: median 20 f (0.83 s), n=9
- easeIn3: median 30 f (1.27 s), n=4
- easeIn2: median 26 f (1.08 s), n=4
- linear: median 18 f (0.75 s), n=2
- easeOut2: median 18 f (0.75 s), n=2

Overshoot (p>1.05) in 0 of 21 reliable runs.

## All reliable events
| frames | time s | len f | fit | rmse | t10 | t50 | t90 | overshoot |
|---|---|---|---|---|---|---|---|---|
| 1789-1809 | 74.54 | 20 | easeInOut2 | 0.10 | 4 | 12 | 19 |  |
| 2283-2309 | 95.12 | 26 | easeIn3 | 0.09 | 14 | 24 | 26 |  |
| 2684-2705 | 111.83 | 21 | easeIn2 | 0.11 | 5 | 14 | 17 |  |
| 4496-4517 | 187.33 | 21 | easeInOut2 | 0.04 | 6 | 11 | 16 |  |
| 4540-4561 | 189.17 | 21 | linear | 0.06 | 4 | 12 | 20 |  |
| 4962-4990 | 206.75 | 28 | easeInOut2 | 0.11 | 8 | 19 | 22 |  |
| 5351-5368 | 222.96 | 17 | easeOut2 | 0.06 | 2 | 7 | 11 |  |
| 5482-5497 | 228.42 | 15 | linear | 0.05 | 3 | 7 | 14 |  |
| 5932-5955 | 247.17 | 23 | easeInOut2 | 0.11 | 5 | 15 | 18 |  |
| 6243-6278 | 260.12 | 35 | easeIn3 | 0.09 | 11 | 26 | 31 |  |
| 6290-6335 | 262.08 | 45 | easeIn3 | 0.08 | 25 | 32 | 44 |  |
| 6425-6452 | 267.71 | 27 | easeIn2 | 0.11 | 4 | 19 | 22 |  |
| 6637-6652 | 276.54 | 15 | easeInOut2 | 0.07 | 4 | 9 | 15 |  |
| 6656-6676 | 277.33 | 20 | easeInOut2 | 0.08 | 6 | 12 | 17 |  |
| 6968-6994 | 290.33 | 26 | easeIn3 | 0.09 | 15 | 20 | 23 |  |
| 7239-7264 | 301.62 | 25 | easeIn2 | 0.11 | 11 | 17 | 21 |  |
| 7666-7684 | 319.42 | 18 | easeInOut2 | 0.11 | 3 | 8 | 12 |  |
| 8696-8715 | 362.33 | 19 | easeOut2 | 0.08 | 3 | 7 | 12 |  |
| 9063-9080 | 377.62 | 17 | easeInOut2 | 0.11 | 3 | 8 | 12 |  |
| 9182-9198 | 382.58 | 16 | easeInOut2 | 0.03 | 5 | 8 | 12 |  |
| 9253-9285 | 385.54 | 32 | easeIn2 | 0.08 | 4 | 25 | 32 |  |

## Camera zoom/push easing (cumulative zoom flow, scan2)

| frames | len s | fit | rmse | t10 | t50 | t90 |
|---|---|---|---|---|---|---|
| 119-165 | 1.9 | linear | 0.06 | 3 | 18 | 36 |
| 1158-1287 | 5.4 | easeIn2 | 0.14 | 71 | 89 | 105 |
| 3321-3396 | 3.1 | linear | 0.06 | 6 | 30 | 61 |
| 4474-4588 | 4.8 | easeInOut2 | 0.12 | 30 | 36 | 80 |
| 4758-4860 | 4.2 | linear | 0.03 | 6 | 49 | 85 |
| 5013-5057 | 1.8 | easeIn2 | 0.11 | 5 | 26 | 39 |
| 7722-7818 | 4.0 | easeIn3 | 0.07 | 22 | 76 | 89 |
## DISTILLED RULES (ref3)
- Only 25 in-shot motion runs exist in 406 s (the video is mostly held poses + cuts); 21 fit reliably, no overshoot/bounce anywhere (0 of 21).
- Typical element move: ease-in-out quad, 15-23 f (0.6-0.9 s) - 43% of runs. Accelerating exits/attacks (jets, strikes, drones; ease-in quad/cubic) 23-35 f, 19% each for in2/in3. Decelerating arrivals (ease-out quad) 17-19 f. Linear 15-18 f only for ticking/scrolling things.
- Camera pushes are LINEAR (slow constant push, 1.8-4.2 s) in 3 of 7 moves, ease-in-out or ease-in in the rest (long pushes 4-5 s start slow: t50 at ~65% of duration = ease-in quad/cubic, building tension). Brain: tension push = ease-in quad over 4-5 s; neutral drift = linear 2-4 s.
- Counter/HUD tween: stepwise number change, no eased count-up measured.
- Compared with ref2: ref2 used ease-out for entrances (5-18 f) and ease-in-out cubic for camera; ref3 keeps entrances short and adds linear/ease-in pushes. Both: no overshoot.
