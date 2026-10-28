# PATTERNS LOG v2 (cross-reference data points) - every video = one column, same genre or not
Rule: a feature becomes a LOCKED RULE only when it holds in >=3 videos; 2 videos = "likely"; 1 = "seen once". Spread (min-max) is kept so the brain knows the allowed RANGE, not just an average.
All numbers in section A come from ONE script run on all four mp4s (metrics_all.py -> metrics_all.json), so they are comparable. Corrections to earlier notes are listed in section C.

## A. Measured with identical method
| metric | ref1 Telekinesis | ref2 Reaction 10x | ref3 One Second | ref4 500 IQ Disappear | ref5 Gravity 5x weaker | pattern |
|---|---|---|---|---|---|---|
| length s | 265.9 | 432.9 | 406.5 | 515.9 | 1461.0 | 4.4-24 min; long-form (24 min) needs a pace curve |
| fps | 30 | 24 | 24 | 24 | 24 | use 24 |
| letterbox px top/bottom | 40 | 41 | 41 | 41 | 40 (360p x2) | LOCKED: 41 px each (5.7%) |
| cuts detected (same rule) | 79 | 223 | 133 | 269 | 512 | - |
| mean shot s (shots >=0.25 s) | 3.2 | 2.1 | 2.7 | 2.0 | 2.8 (2.2 -> 3.5 -> 2.9 across film) | range 2.0-3.2, mean 2.5; newest videos faster |
| median shot s | 3.3 | 2.0 | 2.2 | 1.5 | 2.5 | brain: vary 1-4 s, average ~2.3 |
| sub-0.25 s effect cuts | 1 | 20 | 2 | 15 | 1 | ref1/3 calmer, ref2/4 punchier |
| camera locked % of shots | 63* | 72 | 93 | 80 | 88 | LOCKED: majority locked (63-93, mean 77) |
| near-black pixels (lum<35) % | 49 | 37 | 63 | 42 | 5 | range 5-63, genre-specific (explainer/thriller dark, fantasy film bright) |
| mean Lab L (brightness 0-100) | 16 | 23 | 14 | 27 | 45 | range 14-45, mood-driven |
| flash runs (bright spike, <=8 f) | 4 (3-7 f @30fps) | 24 (1-2 f) | 2 (2 and 4 f) | 12 (mostly 4 f) | 4 (all 4 f) | bursts/flashes 1-4 f |
| overshoot/bounce in motion | 0 of 31 | 0 of 34 | 0 of 21 | 0 of 39 | 0 of 88 | LOCKED (4/4): NO bounce/overshoot anywhere |
| element-move best easing (reliable fits) | linear 42%, ease-in 26% | ease-in 26%, ease-out 21% | ease-in-out 43% | ease-in-out 47% | ease-in-out 48%, ease-in 33%, linear 15% | smooth, never springy; mix of linear glides, ease-in-out (0.6-0.9 s), ease-out arrivals |
*ref1 is 30 fps and its camera-motion threshold was calibrated on 24 fps, so 63% is a floor; earlier method gave ~80%. Treat ref1 as 63-80%.

## B. Observed (visual) features
| feature | ref1 | ref2 | ref3 | ref4 | pattern |
|---|---|---|---|---|---|---|
| characters: black round head + white face marks, role by colour | yes | yes | yes | yes | yes (+hair, capes, tears) | LOCKED 4/4 |
| hero colour | blue shirt | red hoodie | red hoodie | blue hoodie | red hoodie | red or blue hoodie hero |
| cold open on payoff/danger in first 10 s | yes | yes (fly) | yes (bullet) | yes (face + call) | yes (dream, grass, moon) | LOCKED 4/4 |
| title/premise card ~30-40 s | yes | yes (~35 s) | "3 DAYS EARLIER" flashback | "WHAT IF YOU HAD" | time tag at 24 s | likely 4/4, form varies |
| end = question + CTA | yes | yes | yes ("Part 3") | yes ("Part 3") | NO (THE END + fade) | LOCKED 4/4 |
| HUD number/bar changes colour at a threshold | bar blue -> RED when full (42 s blue 30%, 52 s red 100%) | not seen (cream digits) | teal -> coral at 10.1x | red row highlight on victim list | no HUD; plaque text flips VARREK -> ELARIN | LIKELY: ref1 + ref3 do the same flip |
| true full-frame grade switch | few | 25 shots (perception grade) | 1 | 0 (dissolves + object warm-up) | world colour change via dissolve (warm/cool) + white-out | story-dependent, NOT a rule |
| dissolve length | - | 14-25 f | ~6 f | 6-8 f | ~14 f world dissolve; white-out 3.3 s | two families: 6-8 f (night/day) vs 14-25 f (slow time jump) |
| surveillance/HUD "machine view" scenes | no | HUD stopwatch | HUD boards | heavy | none | grows over time |
| hand close-up (pour, point, hold phone) | no | few | few | many | some (teapot, hands) | rising |

## C0. UPDATE after ref5 (5 videos, 2026-10-27)
- BIGGEST CHANGE: ref5 is a 24-min story FILM, bright (near-black 5%, mean L 45). So "dark-leaning world" is genre-specific: explainers/thrillers 37-63% near-black; fantasy film 5%. Brain rule: set darkness from the script's mood (dark HUD/thriller vs warm/lavender fantasy), always keep one accent family and rim light.
- Locked after 5: 40-41 px bars; 24 fps; no overshoot (0 of 213 reliable runs); locked-camera majority (63-93%); cold open; hero black head + white face marks; red or blue hoodie hero; hard cuts dominate.
- NOT locked: end-card CTA (4 of 5; films end on THE END); "Part N" CTA (3 of 5); HUD threshold colour (2 of 5).
- Shot length range now 2.0-3.2 s; long-form needs a pace curve (fast open, slow emotional middle 3-3.5 s with 6-10 s holds, tighter climax).
- Dissolve families: 6-8 f (ref3/4), 14 f (ref5, world crossings), 14-25 f (ref2). White-out portal 3.3 s (ref5, once).
- Callback/payoff devices (planted prop or phrase flipped at the end) appear in ref5 and ref4 (receipt/photo); use when script allows.

## C. Corrections to earlier notes (error check 2026-10-27)
1. "Dark world: 50%+ of every frame near-black" (MASTER-SPEC section 1) was too strong. Measured near-black share is 37-63% (mean 48%). Rule becomes: dark-leaning (mean Lab L 14-27), brightest scenes (white voids, lit day rooms) exist in every video.
2. ref3 mean shot length "2.2 s" came from a looser cut rule; same-rule value is 2.7 s. ref1 "2.8" -> 3.2 s. ref2 "2.0" -> 2.1 s.
3. ref3 cut count 162 was candidate cuts incl. effects; same-rule count = 133.
4. ref1 letterbox 41 px: re-measured 40 px (rows 0-39) - within rounding; use 41 as in ref2-4.
5. ref4 near-black 40% earlier (k-means sample) vs 42% here (all-sample method) - use 42.
6. "Overshoot" and HUD cells that were "?" are now filled (sections A and B).
7. Flash length at 30 fps (ref1) is 3-7 frames = 0.10-0.23 s; at 24 fps (ref2) it is 1-2 f = 0.04-0.08 s. Time-wise a burst lasts 0.04-0.17 s. Use 1-2 f at 24 fps for impact bursts, up to 4 f for flashes.

## D. Locked rules after 4 videos (brain must obey)
Letterbox 41 px; 24 fps; mostly locked camera; no bounce/overshoot; black head + white face marks; cold open on payoff/danger; end card question + CTA; hero in red/blue hoodie; dark-leaning grade with lit exceptions; hard cuts dominate, avg shot ~2-3 s with 1-4 s spread.
Likely rules (2-3 videos): HUD threshold colour flip; short 6-8 f dissolves for day/night; Part-N CTA.
Seen once / story-driven: grade switches, object warm-up, surveillance overlay, machine-view split screen.

## E. How to add video N
Run metrics_all.py with the new mp4 added to R (needs scan1.csv/scan2.csv from scan1.py/scan2.py), add a column, re-judge each pattern cell, log corrections here.
