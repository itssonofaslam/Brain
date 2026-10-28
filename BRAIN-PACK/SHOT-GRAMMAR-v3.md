# SHOT-GRAMMAR v3 — camera angles, framing tricks, camera movement, story-through-camera
Builds on v1 (decision engine) and v2 (shot-size frequencies). Data: 1,203 shots, 5 videos. Tables: labelling/ANGLE-STATS.md, labelling/CAMERA-BY-SHOT-TYPE.md. Angle codes: labelling/angles_refN.csv (exceptions only; untagged = eye-level).

## 0. Honest limits
Angle/trick tags were assigned by eye from contact sheets, exceptions only. Ref5 tags came from my read of its sheets; its over-the-shoulder shots are carried by the earlier "o" flag, so the foreground-frame (F) count for ref5 is understated. Story function below is inferred from what each shot shows plus the script meaning I read earlier, not from timestamped transcripts. Treat percentages as ±5 points.

## 1. When does the camera angle change? (measured)
- 79% of cuts change shot size or angle; only 21% repeat the same size+angle (mostly close-up reverse chains and diagram chains).
- 75% of shots are plain eye-level; 25% carry a non-default angle or framing trick. 108 of 172 trick runs are a single shot, max run seen is 6; rule: one trick shot at a time, at most 3 in a row.
- Tricks cluster on inserts and openings: top-down 100% of D shots; object macros 42%, hand shots 38%, empty plates 32%, close-ups 23%, wide 20%, medium 21%, UI 12%.
- New place: 32% of new-place shots carry a trick, and the trick is almost always scale contrast (S, 23 of 34).
- Emotional beats are mostly plain: only 11% tricked; the face does the work. Two-shots only 7% tricked (intimacy = plain, locked).

## 2. The angle / trick vocabulary (what each is, measured use, what it means in the story)
| code | share of all shots | carried by | story function (use it for) |
|---|---|---|---|
| S scale contrast (tiny figure vs vast set/moon, or one giant element) | 4.6% | 62% wide | awe, isolation, "how small we are", entering a world; the standard place-arrival or ending shot |
| L low angle (looking up at figure/legs) | 2.9% | 49% medium | power, threat, arrival ("legs walking in"), looming antagonist, towers/city seen from street level |
| V high angle looking down + D top-down | 2.3% + 1.7% | V: 57% objects; D: 100% top-down | surveillance, a thing on a table, trap or plan, map; in the film D is flight/aerial (12% of shots at 16-20 min) |
| F foreground frame (over-the-shoulder, bars, net, railing, bokeh or blurred silhouette in front) | 7.6% (understated in ref5) | 55% close-up | dialogue, voyeurism, depth/3D feel; 45 of 87 OTS shots; caged/imprisoned look when the foreground is bars |
| R frame-in-frame (window, porthole, monitor, poster, face-detect box) | 2.8% | 32% UI, 18% empty plates | being watched, a viewing device, "the world beyond"; used to bring a remote place into the room |
| P POV or in-world camera (REC overlay, cockpit, flashlight, hands into lens) | 1.8% | 36% hand shots | subjective ability use, surveillance, searching |
| K backlit silhouette | 1.3% | 25% wide, 25% empty plates | entrance, reveal, sunrise/sunset ending, threat |
| Z dutch tilt | 0.2% (2 shots) | — | almost never; reserve for one crash or loss-of-balance moment per film |

## 3. Camera movement (measured on all 1,203 shots)
- Locked 83%, push-in 6%, pull-out 5%, pan 3%, tilt 2%. Moving shots are held longer (push 3.2 s, pull 4.0 s, locked 2.4 s).
- By shot type: close-ups 94% locked, emotional beats 95%, over-the-shoulder 97%, two-shots 89%; diagram/UI shots push in 20% of the time (the punch-in), empty plates push in 12%, new-place shots move 31% (pans, tilts, pushes, pulls), action shots move 28%, title cards pull out 25%, hand shots pull out 10%.
- Rule: faces never move; place and diagram shots may drift or punch in; end of a section pulls out. (Zoom sign assumes positive = push-in.)

## 4. Story-through-camera recipes (sequences that recur; use as templates, then invent)
1. Arrival in a world: empty plate (E, optional push-in) → wide with scale contrast (S) → medium/low angle of the figure → close-up reaction. Seen: ref5 opening and every world change, ref1 city plate.
2. Emotion building: plain close-ups, an over-the-shoulder with foreground head (F), then an extreme close-up (X) at the peak, then release to a wide or a close-up (after X: wide 27%, close 27%, medium 15%, another X 12%, object 12%; n=26, so weak evidence). Seen: ref5 grief and sacrifice sequences, ref3 monitor reveal.
3. Threat/power: low-angle medium (L), backlit silhouette (K), foreground-framed reverse. Seen: ref3 hat man, ref2 boxing ring, ref5 guardians.
4. Surveillance/knowledge: frame-in-frame (R) on a monitor, then POV/REC (P), then top-down object (V), then a diagram (U), chained 3-5 times. Seen: ref4 throughout.
5. Wonder/escape: top-down aerial (D) + scale contrast (S) + action poses (s), longer holds. Seen: ref5 flight and portal sequences.
6. Intimacy/dialogue: plain eye-level two-shot (locked), alternate close-ups with foreground head (OTS), no tricks. Seen: ref5 kitchen and benches, ref2 stoop.
7. Imprisonment/pressure: shots through bars or a net (F), eye-level, locked, reverse shots. Seen: ref5 prison.

## 5. Decision engine v3 (add to v1 and v2)
1. For each beat pick the shot size by v1/v2.
2. Then pick one trick from §2 only if the beat's function matches; otherwise leave eye-level. Target about 25% tricked overall (ref2 and ref3 run higher through foreground framing; the film runs ~15-19% per block; explainers lean on V, R and P instead).
3. Never repeat the same size+angle more than twice; never run more than 3 tricks in a row; vary the trick (no S, S, S).
4. Movement: lock faces; push in on diagrams and key objects; pull out to end sections; pans and tilts only for place and action.
5. Place the strongest tricks (S, D) at world changes and at the 60-80% mark in a long film; keep the opening slot for a plate or extreme close-up, then a scale-contrast wide.
