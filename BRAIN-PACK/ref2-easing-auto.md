# AUTO (same method as ref3, ref4) measured easing (24 fps, auto-detected motion runs inside shots)

Method: runs of in-shot motion (scan1 diff) 8-40 f, progress p(t)=1-|f_t-f_end|/|f_0-f_end| on gray 192x76 inside the letterbox, best fit among standard curves. rmse<0.12 = reliable. t10/t50/t90 = frames to reach 10/50/90%.
Runs found: 46, measurable: 45, reliable fits: 34

## Distribution of best fits (reliable only)
- easeIn2: 9 (26%)
- easeOut2: 7 (21%)
- easeInOut2: 5 (15%)
- easeInOut3: 5 (15%)
- linear: 5 (15%)
- easeIn3: 3 (9%)

## Median run length (frames) per curve
- easeIn2: median 30 f (1.25 s), n=9
- easeOut2: median 17 f (0.71 s), n=7
- easeInOut2: median 22 f (0.92 s), n=5
- easeInOut3: median 16 f (0.67 s), n=5
- linear: median 30 f (1.25 s), n=5
- easeIn3: median 22 f (0.92 s), n=3

Overshoot (p>1.05) in 0 of 34 reliable runs.

## All reliable events
| frames | time s | len f | fit | rmse | t10 | t50 | t90 | overshoot |
|---|---|---|---|---|---|---|---|---|
| 25-55 | 1.04 | 30 | easeIn2 | 0.07 | 8 | 20 | 28 |  |
| 209-225 | 8.71 | 16 | easeOut2 | 0.10 | 3 | 7 | 11 |  |
| 1027-1052 | 42.79 | 25 | easeInOut2 | 0.07 | 7 | 14 | 23 |  |
| 1054-1086 | 43.92 | 32 | easeIn2 | 0.08 | 16 | 22 | 32 |  |
| 1082-1109 | 45.08 | 27 | easeInOut3 | 0.03 | 10 | 14 | 20 |  |
| 1674-1721 | 69.75 | 47 | linear | 0.10 | 10 | 28 | 41 |  |
| 2091-2107 | 87.12 | 16 | easeInOut3 | 0.09 | 6 | 9 | 15 |  |
| 3057-3075 | 127.38 | 18 | easeIn2 | 0.08 | 5 | 12 | 18 |  |
| 3207-3229 | 133.62 | 22 | easeInOut2 | 0.04 | 6 | 11 | 16 |  |
| 3744-3763 | 156.00 | 19 | easeOut2 | 0.07 | 3 | 7 | 13 |  |
| 4361-4400 | 181.71 | 39 | easeIn2 | 0.11 | 18 | 29 | 34 |  |
| 4442-4460 | 185.08 | 18 | easeInOut2 | 0.07 | 5 | 11 | 13 |  |
| 4458-4480 | 185.75 | 22 | easeInOut2 | 0.07 | 7 | 9 | 16 |  |
| 4666-4690 | 194.42 | 24 | linear | 0.10 | 3 | 7 | 24 |  |
| 4775-4797 | 198.96 | 22 | easeIn2 | 0.11 | 8 | 13 | 22 |  |
| 4992-5015 | 208.00 | 23 | easeOut2 | 0.10 | 4 | 9 | 14 |  |
| 5126-5146 | 213.58 | 20 | easeIn2 | 0.05 | 5 | 14 | 20 |  |
| 5688-5729 | 237.00 | 41 | easeOut2 | 0.05 | 4 | 14 | 31 |  |
| 5804-5834 | 241.83 | 30 | linear | 0.07 | 3 | 11 | 24 |  |
| 6377-6393 | 265.71 | 16 | easeOut2 | 0.09 | 2 | 7 | 13 |  |
| 7251-7284 | 302.12 | 33 | easeIn2 | 0.12 | 11 | 21 | 27 |  |
| 7519-7541 | 313.29 | 22 | linear | 0.07 | 5 | 13 | 21 |  |
| 7805-7838 | 325.21 | 33 | easeIn2 | 0.04 | 12 | 25 | 33 |  |
| 8316-8331 | 346.50 | 15 | easeInOut3 | 0.07 | 6 | 9 | 12 |  |
| 8672-8689 | 361.33 | 17 | easeIn2 | 0.09 | 2 | 11 | 17 |  |
| 9076-9093 | 378.17 | 17 | easeOut2 | 0.12 | 3 | 7 | 13 |  |
| 9290-9305 | 387.08 | 15 | easeInOut3 | 0.05 | 5 | 8 | 10 |  |
| 9306-9322 | 387.75 | 16 | easeInOut3 | 0.06 | 6 | 9 | 11 |  |
| 9583-9624 | 399.29 | 41 | easeIn3 | 0.06 | 21 | 33 | 40 |  |
| 9684-9703 | 403.50 | 19 | easeInOut2 | 0.11 | 5 | 9 | 19 |  |
| 9918-9940 | 413.25 | 22 | easeIn3 | 0.11 | 15 | 18 | 20 |  |
| 10043-10080 | 418.46 | 37 | linear | 0.04 | 7 | 20 | 34 |  |
| 10219-10237 | 425.79 | 18 | easeIn3 | 0.08 | 10 | 12 | 18 |  |
| 10362-10378 | 431.75 | 16 | easeOut2 | 0.09 | 2 | 7 | 10 |  |