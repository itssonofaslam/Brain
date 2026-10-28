# AUTO (same method as ref3, ref4) measured easing (24 fps, auto-detected motion runs inside shots)

Method: runs of in-shot motion (scan1 diff) 8-40 f, progress p(t)=1-|f_t-f_end|/|f_0-f_end| on gray 192x76 inside the letterbox, best fit among standard curves. rmse<0.12 = reliable. t10/t50/t90 = frames to reach 10/50/90%.
Runs found: 40, measurable: 36, reliable fits: 31

## Distribution of best fits (reliable only)
- linear: 13 (42%)
- easeIn2: 8 (26%)
- easeInOut2: 6 (19%)
- easeIn3: 2 (6%)
- easeInOut3: 1 (3%)
- easeOut2: 1 (3%)

## Median run length (frames) per curve
- easeInOut2: median 17 f (0.58 s), n=6
- linear: median 25 f (0.83 s), n=13
- easeInOut3: median 17 f (0.57 s), n=1
- easeOut2: median 14 f (0.47 s), n=1
- easeIn2: median 21 f (0.70 s), n=8
- easeIn3: median 17 f (0.57 s), n=2

Overshoot (p>1.05) in 0 of 31 reliable runs.

## All reliable events
| frames | time s | len f | fit | rmse | t10 | t50 | t90 | overshoot |
|---|---|---|---|---|---|---|---|---|
| 57-101 | 1.90 | 44 | easeInOut2 | 0.03 | 9 | 22 | 38 |  |
| 112-149 | 3.73 | 37 | linear | 0.03 | 3 | 19 | 34 |  |
| 259-276 | 8.63 | 17 | easeInOut2 | 0.04 | 4 | 8 | 13 |  |
| 277-308 | 9.23 | 31 | linear | 0.10 | 8 | 19 | 28 |  |
| 475-491 | 15.83 | 16 | linear | 0.07 | 3 | 9 | 15 |  |
| 521-538 | 17.37 | 17 | easeInOut3 | 0.05 | 6 | 8 | 14 |  |
| 650-668 | 21.67 | 18 | easeInOut2 | 0.05 | 5 | 10 | 15 |  |
| 957-971 | 31.90 | 14 | easeOut2 | 0.08 | 2 | 5 | 8 |  |
| 1085-1111 | 36.17 | 26 | linear | 0.06 | 3 | 11 | 24 |  |
| 1118-1133 | 37.27 | 15 | easeInOut2 | 0.06 | 2 | 7 | 14 |  |
| 1220-1237 | 40.67 | 17 | easeInOut2 | 0.08 | 5 | 10 | 16 |  |
| 1304-1339 | 43.47 | 35 | linear | 0.08 | 6 | 19 | 35 |  |
| 1959-1980 | 65.30 | 21 | easeIn2 | 0.07 | 5 | 14 | 21 |  |
| 2159-2203 | 71.97 | 44 | easeIn2 | 0.10 | 18 | 29 | 37 |  |
| 3551-3567 | 118.37 | 16 | easeIn3 | 0.11 | 11 | 13 | 16 |  |
| 3585-3603 | 119.50 | 18 | easeIn3 | 0.06 | 8 | 14 | 18 |  |
| 3616-3637 | 120.53 | 21 | easeIn2 | 0.08 | 4 | 16 | 21 |  |
| 3951-3969 | 131.70 | 18 | linear | 0.06 | 2 | 12 | 17 |  |
| 4149-4189 | 138.30 | 40 | linear | 0.10 | 3 | 13 | 35 |  |
| 4395-4415 | 146.50 | 20 | easeIn2 | 0.06 | 6 | 13 | 20 |  |
| 4790-4821 | 159.67 | 31 | linear | 0.03 | 5 | 17 | 28 |  |
| 5260-5280 | 175.33 | 20 | easeIn2 | 0.11 | 2 | 13 | 20 |  |
| 5277-5298 | 175.90 | 21 | easeIn2 | 0.08 | 7 | 11 | 20 |  |
| 5296-5313 | 176.53 | 17 | linear | 0.07 | 3 | 9 | 17 |  |
| 5311-5327 | 177.03 | 16 | linear | 0.09 | 3 | 9 | 16 |  |
| 5500-5543 | 183.33 | 43 | easeIn2 | 0.06 | 9 | 30 | 41 |  |
| 5692-5709 | 189.73 | 17 | easeIn2 | 0.04 | 5 | 12 | 17 |  |
| 5878-5897 | 195.93 | 19 | easeInOut2 | 0.04 | 5 | 10 | 15 |  |
| 6331-6346 | 211.03 | 15 | linear | 0.05 | 2 | 8 | 14 |  |
| 6426-6448 | 214.20 | 22 | linear | 0.07 | 4 | 13 | 21 |  |
| 7866-7891 | 262.20 | 25 | linear | 0.04 | 4 | 13 | 24 |  |