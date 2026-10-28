# REF2 measured easing (progress curves from frame differences, 24 fps)

Method: p(t)=1-|f_t-f_end|/|f_0-f_end| on grayscale 192x76 inside the letterbox; best-fit among standard curves. t10/t50/t90 = frames to reach 10/50/90% progress. rmse = fit error (>0.12 = window probably contains a cut or mixed motion, treat as rough).

| event | window s | frames | best fit | rmse | t10 | t50 | t90 | note |
|---|---|---|---|---|---|---|---|---|
| hero arm raise | 5.4-5.83 | 11 | easeInOut2 | 0.19 | 4 | 4 | 7 |  |
| ring on fist grows | 5.83-6.25 | 11 | easeIn3 | 0.21 | 9 | 9 | 10 |  |
| cup hand sweeps in | 12.5-12.95 | 12 | easeOut3 | 0.09 | 1 | 2 | 5 |  |
| cup ring grows | 13.5-13.95 | 12 | easeOut2 | 0.14 | 3 | 5 | 7 |  |
| thrower slides in (yellow cap) | 95.33-96.3 | 24 | easeIn3 | 0.17 | 13 | 22 | 23 |  |
| label 'normal 30cm' fades in | 61.0-61.8 | 20 | easeIn3 | 0.33 | 19 | 19 | 19 |  |
| title line2 grows | 36.9-37.8 | 22 | easeOut3 | 0.13 | 1 | 2 | 17 |  |
| HUD 160km/h appears | 167.9-168.6 | 17 | easeIn2 | 0.14 | 2 | 13 | 16 |  |
| grade flip warm->cool baseball | 169.4-169.9 | 13 | easeOut2 | 0.16 | 3 | 5 | 5 |  |
| grade warm orange ruler | 64.7-65.05 | 9 | easeOut3 | 0.06 | 1 | 2 | 4 |  |
| flip card 20->21 | 155.7-156.5 | 20 | easeIn3 | 0.05 | 10 | 16 | 19 |  |
| fade to black before end card | 422.0-422.55 | 14 | easeOut2 | 0.17 | 4 | 4 | 12 |  |
| end card text builds | 423.0-424.4 | 35 | easeIn2 | 0.08 | 9 | 21 | 34 |  |
| iris shrink to black | 417.0-418.0 | 25 | easeIn3 | 0.20 | 20 | 22 | 24 |  |
| crossfade dusk->night street | 117.6-118.6 | 25 | easeIn2 | 0.12 | 3 | 20 | 24 |  |
| crossfade boxing->pitch | 208.0-208.9 | 23 | easeOut2 | 0.10 | 4 | 9 | 14 |  |
| crossfade track->bedroom | 272.1-273.1 | 25 | linear | 0.14 | 3 | 18 | 24 |  |
| angry face eye shift | 311.5-312.5 | 25 | easeIn3 | 0.34 | 24 | 24 | 24 |  |
| hero arm out (345.8-346.2) | 345.7-346.3 | 15 | easeIn3 | 0.17 | 12 | 13 | 14 |  |
| subscribe pill pop | 429.8-430.3 | 13 | easeIn3 | 0.06 | 5 | 10 | 12 |  |

## Camera move easing (cumulative optical flow, scan2)

| move | frames | best fit | rmse | t10 | t50 | t90 |
|---|---|---|---|---|---|---|
| title tilt/pull-back | 71 | easeInOut3 | 0.06 | 26 | 34 | 44 |
| aerial zoom-out | 160 | easeOut2 | 0.08 | 22 | 47 | 124 |
| pan along pitch | 96 | easeOut2 | 0.08 | 8 | 17 | 59 |
| slow tilt aerial | 178 | easeIn3 | 0.13 | 112 | 131 | 150 |
| pan 69-75s | 133 | easeIn3 | 0.20 | 89 | 119 | 123 |
| tilt 301-304 | 53 | easeInOut3 | 0.06 | 18 | 27 | 31 |
| pan 308.8-310.8 | 48 | easeOut2 | 0.06 | 4 | 16 | 35 |
## READ THIS: rules distilled (reliable ones; windows with rmse > 0.15 are rough because my window timing was only ±0.1 s)
- OBJECT ENTRANCE / SWEEP / RING GROW = EASE-OUT (fast start, soft landing): hand sweep reaches 90% in 5 frames (0.21 s); ring 7 frames; title line grows 17 frames. Use cubic ease-out, 5-18 frames. No overshoot/bounce seen in these.
- POSE CHANGES (arm raise) = ~7 frames to 90%, nearly a pop (ease-in-out quad); most pose changes are 2-4 frames steps.
- SLIDE-IN of a character (thrower) ~ 20-24 frames (0.9-1.0 s); starts slow, arrives at the end (measured as ease-in on a window that includes the hold; treat as ease-in-out cubic 20 frames).
- FADES / CROSS-DISSOLVES = 14-25 frames (0.6-1.0 s), roughly linear to ease-out. Fade to black before end card ~12-14 frames. Iris-shrink ~24 frames.
- GRADE (colour) TWEENS = FAST 4-5 frames (0.2 s) ease-out (ruler orange 4 frames; baseball warm->navy 5 frames). It reads as a switch, not a slow fade.
- FLIP CARD = ease-in (accelerating) over ~19 frames; text/UI pops (subscribe pill) ~12 frames.
- CAMERA MOVES: title tilt/pull-back = ease-in-out cubic, 71 frames (3 s); pitch pan = ease-out quad, 96 frames (4 s, 90% by frame 59); aerial zoom-out = ease-out quad over 160 frames (6.7 s); tilt 301-304 = ease-in-out cubic 53 frames. Rule: short moves (2-3 s) ease-in-out cubic; long slow moves (4-7 s) ease-out quad. Never linear, never bounce.
- IDLE: held shots still move 1-2 px (breathing/head tilt) so nothing is frozen dead.
