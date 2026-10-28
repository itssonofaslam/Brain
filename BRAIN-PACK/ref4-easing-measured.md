# REF4 measured easing (24 fps, auto-detected motion runs inside shots)

Method: runs of in-shot motion (scan1 diff) 8-40 f, progress p(t)=1-|f_t-f_end|/|f_0-f_end| on gray 192x76 inside the letterbox, best fit among standard curves. rmse<0.12 = reliable. t10/t50/t90 = frames to reach 10/50/90%.
Runs found: 59, measurable: 57, reliable fits: 39

## Distribution of best fits (reliable only)
- easeInOut2: 10 (26%)
- linear: 8 (21%)
- easeInOut3: 8 (21%)
- easeIn2: 7 (18%)
- easeOut2: 3 (8%)
- easeIn3: 2 (5%)
- easeOut3: 1 (3%)

## Median run length (frames) per curve
- easeIn2: median 37 f (1.54 s), n=7
- linear: median 23 f (0.96 s), n=8
- easeInOut2: median 20 f (0.83 s), n=10
- easeInOut3: median 17 f (0.71 s), n=8
- easeIn3: median 31 f (1.31 s), n=2
- easeOut2: median 19 f (0.79 s), n=3
- easeOut3: median 15 f (0.62 s), n=1

Overshoot (p>1.05) in 0 of 39 reliable runs.

## All reliable events
| frames | time s | len f | fit | rmse | t10 | t50 | t90 | overshoot |
|---|---|---|---|---|---|---|---|---|
| 409-446 | 17.04 | 37 | easeIn2 | 0.07 | 15 | 26 | 33 |  |
| 464-502 | 19.33 | 38 | linear | 0.04 | 6 | 18 | 35 |  |
| 916-933 | 38.17 | 17 | easeInOut2 | 0.04 | 4 | 8 | 13 |  |
| 1296-1312 | 54.00 | 16 | easeInOut3 | 0.12 | 8 | 9 | 10 |  |
| 1316-1338 | 54.83 | 22 | easeInOut2 | 0.10 | 6 | 13 | 16 |  |
| 1621-1644 | 67.54 | 23 | easeInOut2 | 0.05 | 7 | 13 | 18 |  |
| 1660-1678 | 69.17 | 18 | easeInOut3 | 0.02 | 6 | 9 | 13 |  |
| 1864-1878 | 77.67 | 14 | easeIn2 | 0.07 | 3 | 11 | 14 |  |
| 1882-1900 | 78.42 | 18 | linear | 0.09 | 5 | 11 | 18 |  |
| 1976-1995 | 82.33 | 19 | easeInOut2 | 0.03 | 5 | 10 | 15 |  |
| 2259-2281 | 94.12 | 22 | easeInOut3 | 0.04 | 6 | 11 | 16 |  |
| 2337-2357 | 97.38 | 20 | easeInOut2 | 0.09 | 4 | 9 | 15 |  |
| 2453-2480 | 102.21 | 27 | linear | 0.10 | 6 | 16 | 25 |  |
| 2535-2575 | 105.62 | 40 | easeIn3 | 0.10 | 22 | 30 | 35 |  |
| 2601-2639 | 108.38 | 38 | easeIn2 | 0.07 | 11 | 25 | 35 |  |
| 3064-3080 | 127.67 | 16 | easeInOut3 | 0.03 | 5 | 8 | 11 |  |
| 3461-3480 | 144.21 | 19 | linear | 0.07 | 4 | 11 | 18 |  |
| 4522-4542 | 188.42 | 20 | easeInOut3 | 0.02 | 7 | 11 | 15 |  |
| 4906-4947 | 204.42 | 41 | linear | 0.09 | 2 | 18 | 33 |  |
| 6085-6108 | 253.54 | 23 | linear | 0.07 | 6 | 13 | 21 |  |
| 6488-6503 | 270.33 | 15 | easeOut2 | 0.05 | 1 | 6 | 10 |  |
| 6526-6565 | 271.92 | 39 | easeInOut2 | 0.11 | 10 | 25 | 32 |  |
| 6716-6731 | 279.83 | 15 | easeOut3 | 0.06 | 1 | 4 | 9 |  |
| 6749-6766 | 281.21 | 17 | easeInOut2 | 0.08 | 3 | 7 | 14 |  |
| 6764-6784 | 281.83 | 20 | easeInOut2 | 0.09 | 4 | 9 | 14 |  |
| 7018-7041 | 292.42 | 23 | linear | 0.03 | 4 | 13 | 22 |  |
| 7181-7197 | 299.21 | 16 | easeInOut3 | 0.11 | 7 | 9 | 14 |  |
| 7494-7511 | 312.25 | 17 | linear | 0.10 | 4 | 7 | 16 |  |
| 7571-7615 | 315.46 | 44 | easeIn2 | 0.12 | 23 | 30 | 38 |  |
| 7810-7825 | 325.42 | 15 | easeInOut3 | 0.06 | 5 | 8 | 10 |  |
| 7852-7887 | 327.17 | 35 | easeOut2 | 0.05 | 4 | 9 | 25 |  |
| 8509-8529 | 354.54 | 20 | easeIn2 | 0.08 | 10 | 14 | 20 |  |
| 8583-8602 | 357.62 | 19 | easeOut2 | 0.07 | 3 | 7 | 13 |  |
| 9908-9928 | 412.83 | 20 | easeInOut2 | 0.10 | 4 | 9 | 14 |  |
| 10620-10661 | 442.50 | 41 | easeIn2 | 0.09 | 18 | 31 | 35 |  |
| 11104-11120 | 462.67 | 16 | easeIn2 | 0.08 | 5 | 11 | 15 |  |
| 11596-11620 | 483.17 | 24 | easeInOut3 | 0.07 | 7 | 11 | 17 |  |
| 11993-12016 | 499.71 | 23 | easeIn3 | 0.09 | 11 | 21 | 23 |  |
| 12108-12127 | 504.50 | 19 | easeInOut2 | 0.06 | 4 | 9 | 14 |  |

## Camera zoom/push easing (cumulative zoom flow, scan2)

| frames | len s | fit | rmse | t10 | t50 | t90 |
|---|---|---|---|---|---|---|
| 111-185 | 3.1 | easeInOut3 | 0.16 | 29 | 40 | 43 |
| 275-369 | 3.9 | easeIn3 | 0.09 | 46 | 76 | 85 |
| 1294-1358 | 2.7 | easeOut3 | 0.39 | 1 | 3 | 8 |
| 3058-3208 | 6.2 | step | 1.90 | 78 | 79 | 80 |
| 4712-4825 | 4.7 | easeIn3 | 0.65 | 97 | 104 | 109 |
| 5375-5545 | 7.1 | easeOut2 | 0.10 | 26 | 32 | 106 |
| 5703-5843 | 5.8 | easeInOut3 | 0.35 | 54 | 56 | 58 |
| 6059-6210 | 6.3 | easeIn3 | 0.15 | 95 | 109 | 123 |
| 6244-6334 | 3.8 | easeOut2 | 0.11 | 6 | 26 | 44 |
| 6399-6486 | 3.6 | easeIn2 | 0.10 | 24 | 50 | 77 |
| 8340-8408 | 2.8 | easeInOut3 | 0.32 | 27 | 27 | 28 |
| 9203-9277 | 3.1 | easeOut2 | 0.22 | 24 | 27 | 29 |
| 10558-10684 | 5.2 | easeIn2 | 0.21 | 70 | 78 | 86 |
| 10863-11000 | 5.7 | easeIn3 | 0.15 | 98 | 108 | 119 |
| 11594-11674 | 3.3 | easeOut3 | 0.27 | 2 | 5 | 7 |
| 11962-12032 | 2.9 | easeIn2 | 0.10 | 10 | 41 | 59 |
## DISTILLED RULES (ref4)
- 59 in-shot motion runs (ref3 had 25) - ref4 animates more inside shots. 39 reliable fits. Overshoot 0 of 39..
- Element moves: ease-in-out (quad or cubic) 47% at 17-20 f (0.7-0.8 s); linear 21% at ~23 f (scrolling lists, ticking, strokes); ease-in quad 18% at ~37 f (slow build-up before action); ease-out 11% at ~19 f.
- Camera (reliable only, rmse<0.12): tension pushes ease-in (quad/cubic) 3.6-3.9 s; settle/reveal moves ease-out quad 3.8-7.1 s (fast start, long glide). Same split as ref3: ease-in = tension, ease-out = reveal.
- Noisy camera rows (rmse>0.15) are cuts or HUD content mixed in; ignored.
