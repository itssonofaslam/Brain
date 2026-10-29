# MASTER SPEC v1 (cinematic stickman longs) - 2026-10-26
Built from ref1 (Telekinesis, 265.8 s, 30 fps) + ref2 (Reaction Time 10x, 432.8 s, 24 fps). Measured values come from the mp4s. Update after every new reference (append "REF3 changes" etc). Source files: see FILE-INDEX.md.

## 0. Output format
1280x720, **24 fps** (ref2 = newest; cheaper render), 16:9. Letterbox: 41 px solid black top + 41 px bottom, always on, incl. title/end card. Content area 1280x638. One Remotion composition for the whole video; timeline generated from the word-timing file (frame = round(ms/1000*24)).

## 1. What the look IS (one paragraph the brain must internalise)
A dark-leaning plum/indigo world (37-63% of pixels near-black across 4 videos, mean ~48%, e.g. #1b0f16-#20121b; see PATTERNS-LOG.md section C) where only the story-relevant things glow: amber windows, a red hoodie, cream text, a cyan/white effect. Characters are flat matte-black stick figures (big round head, white graphic face marks, slim limbs) with a thin light rim on the side facing the light and a soft contact-shadow under their feet. Environments are perspective-correct sets (floor planes, converging lines, depth blur) so a locked camera still feels 3D. Depth comes from: rim light, atmospheric haze, foreground blur objects, bokeh, light spill on floors, vignette, and a fresh camera angle on every cut. Motion is limited animation: held key poses with pops and eases, idle micro-motion, effects only at decisive moments.

## 2. Layer stack (back to front, per shot)
1 sky/backdrop gradient (+ sun/moon disc with radial rays when relevant)
2 far skyline / far set silhouettes, desaturated + blurred 2-6 px
3 mid set (building facade / stands / walls) with window glow
4 floor plane with perspective lines, light pools, reflections (alpha .1-.2)
5 props (tables, goal, ring ropes...) with contact shadows
6 characters (rig) + contact shadow ellipse (black .35-.5 alpha, blur 6-10 px, squashed 3:1)
7 key-prop effects (halo/ring/trail/ghost echo)
8 light overlays: window gobo patches, spotlight cone (additive), floodlight starburst, haze
9 NEAR-CAMERA DEPTH PASSERS (see 8): big blurred foreground object/head/hedge/fly/petal/dust, blur 12-20 px
10 grade (per-shot colour tint), vignette (corners -40 to -60%), optional grain
11 HUD/text/graphics (screen space) 12 letterbox bars.

## 3. Camera
- ~77% of shots fully locked. A "move" is a deliberate eased drift, never shake, never handheld.
- Moves: tilt/pull-back reveal (3 s, ease-in-out cubic), slow pan (4 s ease-out quad), slow zoom-out aerial (5-7 s ease-out quad), slow roll/dutch (2-3 s), push into sun bloom. Parallax must be real: far layers move less than near (ratio ~1:4 sky:ground observed; implement per-layer speed multipliers 0.1/0.4/0.7/1.0/1.3).
- Shot size/angle vocabulary: wide establishing; medium two-shot; OTS with big blurred foreground head; extreme close-up face (head fills frame); macro insert (fly, cup, ruler, ball, glasses); top-down/overhead; low ground-level; dutch diagonal; aerial; back-of-head toward goal; tiny figure in huge space (isolation).
- Rule: wide -> close is a CUT, never a continuous zoom. Keep screen direction across cuts.

## 4. Cuts, transitions, pace
- HARD CUT >90%. Average shot 3-4 s; action bursts 0.1-0.3 s pose steps then 1-3 s hold; emotional beats 3-5 s hold.
- Impact punctuation: radial speed-line burst = 1-2 frames (3 max) full cream frame with ~50 black lines; ring ripple 6-8 frames; white flash 1-3 frames; 1 black frame at some cuts; blur-through-black smear 4-7 frames.
- Soft transitions ONLY for time/place jumps: cross-dissolve 14-25 frames; fade to black 12-14 frames (before end card/ending); iris shrink ~24 frames; bleach-to-white 12 frames into screen-in-screen; panel wipe; colour-grade flip in 4-5 frames mid-shot.
- Screen-in-screen: replay on a stadium board/cinema screen, camera pushes until the screen fills = transition.

## 5. Character rig
- Head: black circle (#0a0a0f), radius ~ 1/6 body height x1.2 (large). Face marks white: capsule eyes, slanted brow bar (angry), arc mouth (smile), bar mouth, 'o' mouth (shock). Blink = swap eye shape 2-3 frames. No nose/hair strands.
- Body: slim trapezoid torso in role colour; arms 2 segments (shoulder, elbow) with mitten hands; legs 2 segments; shoes dark with pale sole edge. Thin rim line on lit side only (#f2c9a0 warm / #9fd0ff cool), 2-3 px.
- Role by colour/silhouette, not face: hero red hoodie #d8332f; friend/thrower/kicker yellow cap #f2c230; coach/opponent/kid green cap #3fbf6a; examiner white coat #f4f4f8 + round glasses; visitor fedora + long black coat + dark round glasses; keeper = hero in red kit + yellow gloves. Under night grade red becomes mauve #b07a9a (grade does it, not a new asset).
- Expressions: neutral, smile, smug half-lid, shock 'o', angry-sharp, worried, sleepy half-closed, eyes-shift (look aside).
- Animation: key poses HELD; pose swap every 2-4 frames only in action; walk cycle ~16 frames per step looped; arm raise ~7 frames; dive = 4-6 key poses stretched horizontal; entrance slide-in ~20-24 frames from frame edge; idle: 1-2 px breathing + head tilt on every held shot. Fast limbs get 2-3 ghost echoes (25-40% alpha).
- Crowds: rows of flat stick sprites, 2-frame arm-wave loops, random camera-flash specks.

## 6. Effects library (measured, 24 fps)
radial burst 1-2 f | ring ripple 6-8 f (r 10->50+ px, 2 px line, fade) | white flash dip 1-3 f | black frame 1 f | smear 4-7 f | ghost echo 2-3 copies | speed lines 3-5 thin red lines 12-24 f | sparks: per-frame random dots 20-40 f | sparkle dots twinkle 2-3 f cycle | starburst flare 12-16 rays + bloom pulse | window gobo parallelograms | spotlight cone | bokeh discs 20-60 px | flip card ease-in 19 f | bar-chart panel bars grow 25 f | HUD stopwatch tick every 3-9 f | text: fade+scale 3-8 f (ease-out) | colour tween 4-5 f | end card: words build, icons pop 12 f, cursor clicks pill, ring ripple.

## 7. Colour tokens (hex, from measured frames)
bg darks: #1b0f16 #20121b #2b1823 #11070c(boxing) #0c0c10; night blue: #121734 #1f2945 #3e4e79; stadium: #2f3c47 #465162; gaming: #282443 #3e3866 #5e4c8f #9372c5
warm lights: amber #f6b45e #d4a16c #c17d51; sun #f8e9d7/#fff1c9; spot gold #f2c27a
dusk sky: #6a5276 #987192 #d6ab94; purple #5a2a7a->#d86a8a
accent: hero red #d8332f/#d04335; yellow #f2c230; green #3fbf6a/#68ae6b; cyan reflection #9fd0ff; HUD cream #fff1c9; VICTORY #efdb8a; end card red #db241b on #160b1d.
Mood grade: warm = comfort/ordinary; purple = wonder; blue night = danger/loneliness; gold spot = tension; desaturated grey = clinical test (ruler).

## 8. Micro-depth rule ("little things") - brain must ADD these itself
Every shot gets at least ONE of: foreground blurred passer (fly/bee/petal/leaf/dust/bird silhouette crossing at 15-20 px blur), bokeh discs, light flicker (window lamp, LED board), crowd flash specks, steam/breath/smoke wisps, birds V-dots in sky, swaying tree silhouette, hair-cloth sway, floor light pulse, slow bloom pulse. Opening of ref2: fly foreground blurred flies away. Ask: "what would be in this place that is moving or glowing that nobody mentions?"

## 9. Environment kits (reusable)
night townhouse street (moon, lamp cone, steps, car), cafe (striped awning, round table), lab/room w/ skyline window, gaming room, arched-window hall, baseball field + floodlight towers, boxing ring + one lamp, football pitch + goal + net crosshatch, running track, bedroom, stadium bowl (stands dotted texture, scoreboard, rig), black car, void end card. New location the script needs = brain INVENTS: choose light source -> choose palette from section 7 mood -> list 3 depth layers -> add 2 ambient loops -> place contact shadows.

## 10. Text/graphics
Title: 2 lines, bold condensed sans, gold-cream gradient #fff1c9->#f2c27a, dark offset shadow, glow; builds line 1 small then line 2 larger; camera drifts under it. HUD labels: cream bold small caps with glow, thin measurement bracket. Score digits: flip card cream #f3e6c8 on brown board. Infographic panel: dark screen-in-screen, red block -> bars. End card: question text builds word by word, icon row, red pill Subscribe with bell, silhouette row, fade to dark.

## 11. Story structure the script brain should mirror
cold-open demo (0-9 s) -> escalating examples -> title/premise at ~35 s -> mechanism with diagram/labels -> stakes escalation across domains -> cost beat (slow, dim, held) -> climactic dilemma w/ two simultaneous paths -> long-hold aftermath -> twist hook -> viewer question + CTA. Suspense = slow-motion approach + wide->close cuts + numbers/clock + held silence (350-351 s digital silence). Humour = smug half-lid, shock 'o', absurd results (21:0, x30).

## 12. Build architecture (when approved)
timeline.ts (from word timing) | kits/ (environment components) | rig/ (Character with poses/expressions) | fx/ (burst, ring, flash, ghost, sparks, flare) | camera/ (per-layer parallax, ease helpers) | grade/ (tint, vignette, letterbox) | text/ | Root.tsx one composition. Heavy blur/glow: bake sprites, max 2-3 blur layers per shot, concurrency 2.

## 13. Open items (refine with more mp4s)
Easing of walk cycles & dive poses; crowd loop timing; shadow geometry numbers; how scripts map to shot lists; sound design (later, from audio-rms.csv); render speed test (Colab vs laptop); explainer-board segments (ref2 52-57 s blueprint grid + pointer; ref1 draw-on strokes) need one more example.

## 14. FEEL DEVICES + INVENTION PROTOCOL (added 2026-10-26)
See FEEL-DEVICES-v1.md. Colour grade is a STORY DEVICE (perception grade: cool/desaturated = slowed time, snap to warm on a 1-2 frame burst). The brain must run the invention protocol (feeling -> lever -> state A/B -> switch -> restore -> repetition check) for every beat that needs feel, and may use clearly-labelled proposals.

## 15. REF3 changes (2026-10-26) - ref3 = "What If One Second Felt Like Ten", 406 s, 24 fps, same letterbox
- Camera default is LOCKED even more (94%); moves only = slow push/pull 2-5 s, no pans. Avg shot 2.2 s in dialogue-heavy stories.
- Add **threshold colour** device: live HUD numbers flip teal #83e2c3 -> coral #f0705a on the frame a limit is crossed.
- Add **punch-in to monitor** cut (room darkens to ~25% behind a rounded screen #1d3a63).
- Short dissolve 6 f is OK when both shots share a dark base.
- New kits: spotlight void, cockpit 3-panel road sim, jet cockpit POV, diner, fight arena (red floor ring), bedroom night with window, phone UI, polaroid, eye macro, fly macro, text-only card, "3 DAYS EARLIER" title card, "PART N?" end card (yellow #f1bc39).
- Form-follows-content: perception-speed facts get a black-frame strobe (2-4 f).
- New characters: Doctor Lee, Number six, Jake, Number five (see video3/ref3-findings.md).
- REF3 easing (video3/ref3-easing-measured.md): element moves ease-in-out quad 15-23 f; arrivals ease-out quad 17-19 f; attacks/exits ease-in quad/cubic 23-35 f; NO overshoot or bounce in 21 of 21 reliable runs; camera tension push = ease-in quad 4-5 s, neutral drift = linear 2-4 s.

## 16. REF4 changes (2026-10-26) - "500 IQ to Disappear", 516 s, 24 fps, letterbox 40-41
- Not always dark: mix dark HUD world with lit tan/cream day rooms (see PATTERNS-LOG.md update). Faster cuts (mean 1.9 s). 80% locked, slow pushes common (6-12 s), occasional whip pan.
- New kits: surveillance overlay (corner brackets, REC, timecode, body-cam), hacker HUD map (dark navy + gold line art), UI cards (phone call, social post, search bar with cursor, folders, ledger, ticker), pin-board counter (30 photos, red X), door-circle diagram, hand close-ups (pour, point, knock), day/night apartment kit, elderly-victim kitchen, prison/evidence card, newspaper-phone.
- Devices: object warm-up (clue activates), night->morning dissolve with time tag, machine-view split screen (draw what the machine "reads").
- Easing: ease-in = tension push (3.6-3.9 s), ease-out = reveal glide (3.8-7.1 s); element moves ease-in-out 0.7-0.8 s; see video4/ref4-easing-measured.md.

## 17. ERROR-CHECK CORRECTIONS (2026-10-27): see PATTERNS-LOG.md v2 section C. Key: near-black share is 37-63% not '50%+'; mean shot 2.0-3.2 s; NO overshoot in any of 4 videos (0/125 reliable runs); HUD threshold colour flip seen in ref1 (bar blue->red) and ref3 (teal->coral).

## 18. DEVICE INVENTION v2 (2026-10-27): brain invents devices from the script claim (see DEVICE-INVENTION-v2.md): claim -> hidden thing -> lever -> A/B states -> decisive frame -> restore -> log, and every device must pass the premium guardrails (locked/eased camera, new angle each cut, no overshoot, 41 px bars, burst 1-2 f, one accent family, micro-depth, motivated by the script).

## 19. REF5 changes (2026-10-27) - "Gravity 5x weaker", 24:21 story film (see video5/ref5-findings.md, PATTERNS-LOG.md C0)
- Darkness is genre-specific (near-black 5% here). World = colour temperature (Earth warm amber, other world periwinkle/indigo); two-moon sky clock for countdown; richer characters (hair, capes, tears, orange rim); subtitle pill only for key lines; world-crossing dissolve 14 f with matched object; portal white-out 3.3 s once; callback/payoff props (pancake, wall plaque flip VARREK -> ELARIN); weight shown by posture/camera height.
- Long-form pace curve: 2.2 s open -> 3.5 s emotional middle (6-10 s holds) -> 2.9 s climax -> long calm last shot; no CTA end card for films (THE END + fade).

## 20. SHOT GRAMMAR (2026-10-27): see SHOT-GRAMMAR-v1.md - decision engine for shot size (wide / object macro / HUD / face XCU / OTS dialogue / action / diagram), object close-up test (named, planted, or changing state), face close-up recipe, physics = suggested by posture/shadow/easing never simulated, background kinds and choice rule. Frequencies per shot size NOT yet measured (automatic classifier failed validation; labelling pass proposed).

## 21. Labelling pass results
1,203 shots hand-tagged across 5 videos. See SHOT-GRAMMAR-v2.md and labelling/STATS.md. Key: mix W25/C23/M18/U10/O8; genre decides the mix; new place→wide 75%; emotion→close 75% / extreme 24%; runs of 3+ same size rare; close-up share peaks mid-film.

## 22. Angle and camera pass
SHOT-GRAMMAR-v3.md: 25% of shots carry a non-default angle/trick (S scale 4.6, F foreground 7.6, L low 2.9, V/D high 4, R frame-in-frame 2.8, P POV 1.8, K backlit 1.3, Z 0.2); 79% of cuts change size or angle; camera locked 83% (faces 94-97%, diagrams push in 20%); seven story recipes.

## 23. Plugin fold-in (2026-10-27)
PLUGIN-FOLD-IN-v1.md: build protocol, beat splitter start values, rig vocabulary + invention rule, visual ingredient checklist, render time planning (1080p), story flow. Sound parked (PLUGIN-SOUND-PARKED.md). Decisions: our measurements win on camera, pop-in, wide shots; extreme face is dynamic (script decides, cap about 5%).
- 2026-10-27 addendum to section 23: 3D flying shot ADDED (PLUGIN-FOLD-IN-v1.md section 10): dynamic, brain decides from script (arrival, big space, journey, flight; never faces/dialogue/diagrams), Method A layered 2.5D default, Method B real Three.js only when needed, unverified, test later.

## 24. Fly shots (3D / depth travel)
FLY-SHOTS-3D-v1.md: dynamic, brain decides when space is the story; method A depth-layer fly (default), method B true 3D (rare); camera grammar from our travelling wides; measured 0.2-2 per min across refs.
