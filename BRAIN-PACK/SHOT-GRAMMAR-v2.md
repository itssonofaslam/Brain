# SHOT-GRAMMAR v2 — from 1,203 hand-labelled shots (5 videos, 51 min)
Source: labelling/STATS.md (all tables). Labels are one frame per shot, tagged by me by eye (codebook in labelling/CODEBOOK.md). Caveat: single labeller, one frame per shot, so a shot that changes size mid-hold counts once. Transcript alignment NOT done (transcripts have no timestamps); rules below come from visual patterns plus script meaning noted earlier in SHOT-GRAMMAR-v1.

## 1. Real mix (all videos, % of shots / % of time)
W 25/28, C 23/24, M 18/18, U 10/11, O 8/7, E 5/4, H 4/2, D 3/3, X 2/1.5, T 1/1.6, B 0.5/0.3.
Rule of thumb: ~1/4 wide, ~1/4 close, ~1/5 medium, ~1/10 UI/diagram, remainder inserts (O+H+E+D+X ≈ 22%).

## 2. Genre profiles (the mix is NOT universal; brain must pick a profile from the topic)
- Narrative film (ref5, ref1): W 28-31, M 19-30, C 12-29, U 1-15. Face-heavy, few diagrams.
- Explainer/mechanism (ref4): U 32 (41% of time), O 17, E 11, W only 8.5. Almost no faces.
- Story-explainer hybrid (ref2, ref3): W 28, C 22-32, U 6-10, O 6-7.
Brain picks profile from script type: character story → film; "how X works" → explainer; mixed → hybrid.

## 3. Hold lengths (mean s)
W 2.8, C 2.6, M 2.6, U 2.7, O 2.3, E 2.3, D 2.3, H 1.4, X 1.7, B 1.3, T 4.0. Inserts (H, X, B) are shortest: 1-1.7 s. Titles longest. Outliers: ref3 object macros 6.5 s (a held reveal), title cards 7-8 s.

## 4. Sequencing (what follows what, all videos)
- After W: W 29, C 25, M 21 → wides chain; wide→close is the common step.
- After C: C 30 (face-reverse chains), W 28, M 19.
- After X (extreme face, n=26 only): W 27, C 27, M 15, X 12, O 12, E 8 — no strong rule; it never leads to U. (Earlier draft claimed X rarely leads to a wide; that was wrong, 27% do.)
- After O: O 20, U 14, W 16, C 18 — object macros chain into more objects/diagrams.
- After U: U 34 (diagrams chain strongly), W 16, M 18.
- After E (empty plate): E 22 — establishing plates chain in pairs/triples, then W/U.
- After B (black/flash): W 67 — you re-enter on a wide.
- Same code in a row: 1 shot 694 times, 2 shots 135, 3: 43, 4: 13, 5+: 10. So runs of 3+ of one size are rare (~5% of runs); cap same-size streaks at 3, and alternate size or angle.

## 5. Triggers (flags)
- New place (p, 8.8% of shots): 75% wide, 11% empty plate, 10% medium, 4% top-down. → New place opens on W (or E then W). Almost never a close.
- Emotional beat (e, 7.7%): 75% C, 24% X, 1% M. → Emotion = face close-up; escalate to X for the peak (X is ~1 in 4 emotion shots).
- Over-the-shoulder (o) 7.2%, two-shot (t) 8.5%, action pose (s) 6.2%, crowd (k) 1.5%. Dialogue scenes use t + o + C reverse; action uses W/M with s.
- Face-emotion spacing: ref5 has 58 (C.e or X) with median gap 5 shots, only 25% clustered (gap ≤2). So emotional close-ups are spread out, about every 5th shot, not blocked together; ref2 gap 7, ref3 gap 6. ref4 (explainer) has 3 in total.

## 6. Pace/shot-mix curve over a long film (ref5, 4-min blocks)
Shots per block: 110 → 91 → 83 → 68 → 77 → 82 (slowest at 12-16 min). Close-up share rises from 23% (0-4) to 44% (12-16) then eases to 30%; wide share falls 35 → 25 → 28. Object/hand inserts peak at 8-12 and 20-24 min (11-12%). Top-down/aerial spike at 16-20 (13%, the flight sequence). Brain rule: open wide-heavy, build to close-heavy at the emotional middle (≈50-65% of runtime), then return to wide and inserts for the ending.

## 7. Openings and endings
Openings: ref1 O O H W W (object first), ref2 W O C H H, ref3 W M O M M, ref4 C M E E E, ref5 B X E D C (black, extreme face, plate). Endings: ref1 …U W W T (end card), ref2 T T T T T (end cards), ref3 …X O O, ref4 …O M O T, ref5 W C W H E (a final empty plate). Pattern: first shot is rarely a plain wide of the hero; last 1-5 shots are text card in 3 of 5, an E plate in the film.

## 8. Decision engine v2 (use with v1)
1. Choose genre profile (§2) → target mix.
2. Per sentence: new place → W (+E before); emotion peak → C, strongest → X; named/planted object → O; hand action → H; number/limit/mechanism → U; plan/route → D; dialogue → t/o/C chain.
3. Enforce: max 3 same-size in a row; B only before a W re-entry (67% of the time a wide follows black).
4. Hold: W/M/C 2.3-3.1 s, inserts 1-1.7 s, titles 4-8 s; vary within ±30%.
5. Pace curve per §6 for any video over ~8 min.
