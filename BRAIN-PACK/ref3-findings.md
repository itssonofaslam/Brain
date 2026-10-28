# REF3 FINDINGS - "What If One Second Felt Like Ten" (406.38 s, 9753 f, 24 fps, 1280x720, letterbox 41+41 px - identical to ref2)

## 1. What is new vs ref1/ref2
1. **Camera is 94% locked** (137 of 145 shots >=0.5 s). Only 8 moves, all slow zoom-pushes/pull-backs of 2-5 s (zoom-idx 44-187), no pans/tilts at all. -> Rule: default = locked; the only move in a dialogue/HUD shot is a slow push (ease in-out, 3-5 s). Tail 360-406 s is end card, ignore.
2. **Cut rate**: 162 candidate cuts, avg 2.22 s per shot (faster than ref2). Dialogue scenes = alternating extreme close-up faces (head fills frame) with short wide re-establishing shots.
3. **HUD colour = state device** (the "grade switch" of this ref): at 236.2-236.4 s the counter "REACTION 10.0x" is TEAL (#83e2c3) and flips to CORAL RED (~#f0705a) at 10.1x. Same panel, same frame; only the digits recolour in one step. Meaning: teal = safe/normal, coral = past the limit. Brain use: any live number gets a threshold colour; flip on the exact frame the line is crossed.
4. **Real full-frame grade switches are rare**: only ONE verified (236.12 s, structure diff 0.01, blue (26,39,56)->(39,32,45) in 6 f: night-blue lab to warm plum when the counter goes red). Other 12 candidates are cuts or animation. So ref3 uses cuts + HUD colour more than grade swings.
5. **Dissolve used as continuity bridge between scenes of different size**: 187.5-188.0 s, face close-up (doctor with tablet) dissolves ~6 f into wide cockpit-sim room (3 screens with road, red chair, purple Number six). Shorter than ref2's 14-25 f; ok when the new shot has the same dark base.
6. **Punch-in to HUD (screen-in-screen) as a cut**: 235.8 wide lab with patient in chair -> 236.0 monitor fills frame (counter close-up). Same trick as ref2 board, now with a rounded monitor frame #1d3a63 and a blurred copy of the room behind it (room darkened to ~25%).
7. **Cockpit/POV sets**: three-panel road simulator (centre panel perspective road, side panels angled) = cheap 3D: draw road once with vanishing point, skew side panels. Sky #7383a7 -> #9dadcc is the only bright area, rest near-black.
8. **Black runs as rhythm at the end**: black strobe ~371-377 s and a 53-frame black run at 382.96 s around the fly/comparison facts (flicker = fly-vision metaphor: the form of the cut IS the content). Brain: when the content is about perception speed, strobe the frame at 2-4 f.
9. **Text-only card** ("IS ANY OF THIS REAL?" ~361 s) separates story from facts; facts section uses line-art diagrams (false-start diagram, F1 lights), macro fly with red eyes #bc2d2b and comparison bars, then end card "PART 3?" (yellow #f1bc39 / #efc854) with subscribe/bell/like and a row of 4 silhouettes.
10. **Title card "3 DAYS EARLIER"** = time-jump label; cream text on black, hard cut in/out, no dissolve.

## 2. Light and palette (see ref3-palette.md)
Opening: spotlight cone in void, #141015/#231c21. Hero accent red #c16556/#d04034. HUD teal #83e2c3/#7bf0c9, coral #f0705a. Door blue #81baea. Fight arena #0a0916 with red ring floor. Bedroom night + city window (321-353 s). Mean scene brightness (Lab L): lab/sim scenes 20-28, story scenes 9-13, end 3-5. Brightest block 200-220 s (sim sky). Dark-world rule holds: >50% of the video is L<13.
Colour-state map by 20 s: see ref3-colour-state-map.md.

## 3. Characters (new templates)
- Max (hero): red hoodie, black head, white eye marks.
- Doctor Lee: white coat, round glasses with spiral/cross marks, tablet.
- Number six: purple coat, white VR visor, ponytail.
- Fedora man: dark coat, round dark glasses (same as ref1/2 visitor).
- Jake (friend, phone call), Number five (shown as photo/polaroid ~345 s).
All remain: black round head, white marks, role by colour. Extreme close-up = head fills ~70% height, only eyes + 1 prop visible.

## 4. Scene kits seen (add to environment list)
Spotlight void (cold open), black car interior, test facility corridor, light-board room (HUD grid of buttons), tennis court, drone arena, lab with patient chair + window skyline (235 s), cockpit sim room (3 screens), jet cockpit POV (205 s), diner (225-233 s), fight arena with red floor ring (261-297 s), bedroom night with city window (321-353 s), phone UI (325 s), polaroid (345 s), eye macro with dial (357 s), fly macro.

## 5. Suspense/emotion structure (for script brain)
Cold open = the end state (bullet) -> "3 DAYS EARLIER" flashback -> recruit -> 3 tests escalating (board, tennis, drones) -> mentor reveal + rival (Number six) -> lesson (watch the trigger) -> cost (headaches, hunger) -> final exam vs the first one -> twist (burn-out, Number five) -> phone call quiet beat -> fact section -> open question -> CTA for Part 3. Humour beat after each pain beat ("Ow. Okay. That's... not fair.").

## 6. What I did NOT measure for ref3
Easing curves (counter tween, push-in profiles) - ref3 moves are too few/short; ref2 values stand. No new transition frame counts beyond: dissolve 6 f, grade flip 6 f, HUD recolour 1 f.

## CORRECTION (2026-10-27 error check)
Same-rule measurements across all 4 refs: mean shot 2.7 s (not 2.2), 133 cuts (not 162 candidates), locked 93%, near-black 63%, mean Lab L 14. See PATTERNS-LOG.md v2.
