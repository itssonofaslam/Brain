# DEVICE INVENTION v2 - brain invents devices FROM THE SCRIPT, inside the references' perspective and premium level (2026-10-27)
Builds on FEEL-DEVICES-v1.md (colour-grade protocol). v1 invents FEEL; v2 invents a VISUAL DEVICE for any script line, and checks it against the premium guardrails measured from 4 references (PATTERNS-LOG.md).

## 1. Principle the references all follow (measured, 4/4)
Every device in the refs is the script's own idea made visible, never decoration:
- invisible tech -> draw what the MACHINE reads (ref4: infrared pen = face-box on a head full of jittering dots + constellation lines, "FACE DETECTED - NOT IDENTIFIED").
- a limit -> colour flips on the exact frame it is crossed (ref1 bar blue -> red when full; ref3 counter teal -> coral at 10.1x).
- a count/list ("29 heroes before you") -> a wall of items that are crossed out one by one, the last one is the hero (ref4 pin-board).
- a plan/metaphor ("12 doors, one empty room") -> a diagram that IS the plot (ref4 door circle, all lines converge on one room).
- a perception change ("time slows") -> the whole scene colour state changes (ref2 cool/desaturated), snaps back on the payoff burst.
- time passing / jump -> title tag ("3 DAYS EARLIER", "7:40 A.M.", "NIGHT 2") + dissolve or black frame.
- danger/being watched -> corner brackets, REC dot, timecode, torch beam, green tint (ref4 surveillance).
- a clue -> object warms from white to cream, background stays black (ref4 receipt "2019").
- a number as drama -> big HUD digits in a rounded monitor; punch-in cut from the room to the screen (ref3).
- a fact about the real world -> change visual language: line-art diagram / macro insert (fly) / text-only card (ref3 "IS ANY OF THIS REAL?").
So: DEVICE = script claim -> show the hidden thing -> at the decisive frame change one lever.

## 2. DEVICE ENGINE (run for every script sentence that is not a plain action)
1. CLAIM: write the sentence's one idea in 8 words.
2. HIDDEN THING: what in that idea cannot be seen in a plain shot? (a number, a feeling, a rule, a machine's view, time, a count, a connection, a risk.)
3. SHOWN AS: pick the translation pattern from section 1 (machine view / threshold colour / crossed-out wall / diagram-is-plot / colour state / time tag / surveillance overlay / object warm-up / HUD punch-in / language change). If none fits, INVENT: ask "what would the object look like if it were a screen, a map, a light, a colour, a list, or a counter?"
4. LEVER: choose ONE primary lever (colour, light, scale/angle, cut rate, hold, frame, text/HUD, sound-implied, object state) + at most one secondary.
5. STATES: A (before) and B (after) in numbers: hex, %, blur px, frame counts (use the tables in PATTERNS-LOG section A and MASTER-SPEC section 6).
6. DECISIVE FRAME: the exact word/ms in the timing file where the change lands (the word that carries the claim).
7. RESTORE or HOLD: restore at a burst/cut (release) or hold in B (loss/dread).
8. LOG: write one line in the shot plan: `device | claim | hidden thing | lever | A->B | frame | restore`.
9. REPEAT CHECK: same device max 3 times per 60 s; vary the lever or stay still.
10. GUARDRAIL CHECK (section 3). Fail any = redesign, do not ship.

## 3. PREMIUM GUARDRAILS (a device is accepted only if ALL pass; every number measured)
PERSPECTIVE / CAMERA
- Camera stays LOCKED unless the device needs a move; moves are slow eased pushes/pull-backs 2-12 s (ease-in for tension 3.6-5 s, ease-out for reveal 3.8-7 s, linear for neutral drift 2-4 s), whip pan only on a hard reveal (<=3.3 s). Never handheld, never shake, never fly-through.
- Wide -> close is a CUT, never a continuous zoom. Keep screen direction across cuts. Every cut gives a NEW angle/size (no jump cuts of the same framing).
- Sets are perspective-correct (vanishing point, floor plane, converging lines); parallax layers move at different speeds when the camera moves (0.1/0.4/0.7/1.0/1.3). Flat UI cards/HUD sit in screen space.
- Shot sizes to use: wide establishing, medium two-shot, OTS with big blurred foreground head, extreme close-up face, macro insert (hand, phone, cup, fly), top-down, low angle, tiny figure in huge space.
FEEL / MOTION
- NO overshoot, no bounce, no elastic anywhere (0 of 125 measured runs). Element moves: ease-in-out 15-23 f (0.6-0.9 s), arrivals ease-out 17-19 f, attacks ease-in 23-35 f, linear only for tickers/scrolls/glides.
- Impact burst 1-2 f at 24 fps (flash up to 4 f); ring ripple 6-8 f; dissolve 6-8 f (night/day) or 14-25 f (slow time jump); fade to black 12-14 f; grade snap 4-6 f; HUD recolour 1 f.
- Effects are punctuation: a burst at most once per 10-20 s; hard cuts are >90% of transitions.
LOOK
- 41 px letterbox always (also over title/end cards); 24 fps; hero = round black head + white face marks, role by colour (red or blue hoodie hero); no new face styles.
- Dark-leaning grade (mean Lab L 14-27, near-black 37-63%) with lit exceptions; ONE accent colour family per scene (gold line art on navy; teal/coral on HUD; red for danger). HUD/text is never graded.
- Depth: every shot has one micro-depth element (fly/dust/bokeh/flicker/steam/blurred foreground passer). Rim light on the lit side, contact shadow ellipse under feet, vignette.
- Text: cream/gold bold condensed caps with soft glow; tags small and grey in corners; HUD rounded monitor with glow edge; no more than 2 text styles per scene.
PACE
- Average shot 2.0-3.2 s (target ~2.3), spread 1-4 s; held beats 3-5 s for emotion; a device lasts as long as the script line, never longer than 2x it.
STORY MOTIVATION
- The device must change what the viewer understands or feels at that word. If you cannot name the claim it shows, delete it.

## 4. WHAT "DIFFERENT SCRIPT -> NEW DEVICE" LOOKS LIKE (labelled PROPOSALS, same engine)
| script line | hidden thing | invented device | lever | A -> B | restore |
|---|---|---|---|---|---|
| "A virus spreads silently through a city" | spread over time | dark city map, houses light up red one by one, counter bottom-right climbing, colour flips from teal to coral at 10% infected | colour + counter + map | map teal -> coral | hold in B (dread) |
| "You can't lie to a lie detector" | pulse/stress | split screen: calm face left, face right with a pulse line; line spikes, border turns coral on the answer word | HUD colour + split frame | border teal -> coral 1 f | cut to wide |
| "He saved for twenty years" | time + cost | a jar on a shelf; calendar pages flip behind it, jar level rises in steps, warm light dims each page | object state + light | jar 5% -> 100%, light 100% -> 60% | hold |
| "No one noticed the mistake" | something missing | same wide shot twice; second time one item is gone, ring ripple around the empty spot (empty-frame beat) | absence + ripple | item present -> absent | hold 2 s |
| "Gravity was twice as strong" | weight | hero's shadow ellipse doubles, floor line sags 6 px, props drop with ease-in, camera pushes ease-in 4 s | shadow + ease-in | normal -> heavy | burst on release |
| "Everyone forgot his name" | fading identity | pin-board photos each lose colour to grey as lines are crossed; hero photo last | wall + colour drain | colour -> grey over 60 f | hold, no restore |
| "She heard it before anyone" | hearing | ring ripples radiate from an off-screen source, the rest of the frame freezes | ripple + freeze | normal -> frozen except rings | cut |
RULE: proposals are labelled "proposal" in the shot plan, tested on a 5-second sample, and kept only if they pass section 3.

## 5. HOW THE BRAIN KEEPS "THE SAME PREMIUM" (continuity of taste)
1. Always read PATTERNS-LOG.md locked rules first, then FEEL-DEVICES-v1.md, then this file.
2. Every new device must be a recombination of a measured translation pattern (section 1) or a labelled proposal with a stated reason; no free decoration.
3. Write the device line in the shot plan before writing Remotion code, so repetition and guardrails can be audited by scanning the plan.
4. After each finished video, add its devices as a new column in PATTERNS-LOG.md (feeds the next one).
5. When a reference is added: extract its devices with the same engine (claim -> hidden thing -> lever) and append them to section 1.

## 6. NEXT TO FILL (from references, later)
Sound-implied cues per device (silence, riser, hit) once the sound-design brain exists; render cost per device (blur layers max 2-3 per shot).
