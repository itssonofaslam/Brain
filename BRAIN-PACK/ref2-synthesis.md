# REF2 SYNTHESIS (Reaction Time 10x, 432.8 s) - from 148 pages. Written 2026-10-26. Measured values from PDF thumbnails (910x512 source), not yet from mp4.

## 0. Honest verdict on "3D"
The dossier says "true 3D". My read of the frames: SAME FAMILY as ref1 = flat black-cutout characters on painted/gradient environment plates with heavy blur, bokeh, rim light, vignette, glow. Evidence: characters are flat silhouettes with thin cream outline, poses change in steps (held 0.1-0.3 s per pose), backgrounds do not change perspective when characters move, camera mostly LOCKED; the few "moves" are slow pans, a slow roll (dutch) and slow zooms that a layered 2D comp can fake. The "3D" feeling = depth cues (below), not geometry. To be certain I need the mp4 (parallax test: do near/far layers shift at different speeds?).
=> Conclusion for build: Remotion 2.5D layered comp can reproduce it. Real 3D (three.js) is NOT required.

## 1. How depth/"3D feel" is faked (the recipe)
1. Warm rim light: thin 2-3 px cream/peach outline (#f2c9a0) ONLY on the side facing the light source; black body. Cool scenes: pale blue rim (#9fd0ff).
2. Atmospheric gradient plates: sky/background = vertical gradient + soft haze band at horizon; distant layers desaturated and blurred, near layers darker.
3. Foreground blur: big out-of-focus character head/hand/hedge on one edge of frame (OTS shots), gaussian ~12-20 px, + circular BOKEH discs (soft 20-60 px circles, 10-30% opacity, peach/pink in dusk, white in night) in macro inserts.
4. Light sources drawn as real things: window grids glowing amber (#f6b45e), sun disc with radial rays behind head, floodlight towers (white dot grids) with starburst flare, spotlight CONE (soft triangle, additive) in boxing, window-blind/arched-window GOBO light patches on floor (parallelograms), headlight beams.
5. Contact shadows: dark soft ellipse under feet/props; floors with faint reflection.
6. Camera-angle variety by cuts: wide / OTS / extreme close face / top-down / low ground / aerial = the "cinematic" sense, each shot is a NEW still layout, not a moving camera.
7. Depth of field changes between cuts (macro sharp subject vs blurred bg), and 'rack focus' = cut/dissolve to blurred version (e.g. 162 s arched windows blur).
8. Heavy vignette (corners 40-60% darker) + subtle grade per scene.
9. Light/colour per mood: see palette. Grade flips mid-shot (warm->cool navy in baseball 169.6 s; red hoodie becomes mauve #b07a9a in night shots).

## 2. Palette (hex, starting values)
- Dusk street: sky #7a4f8a -> #e8a07a; sun glow #fff1c9; window amber #f6b45e / #e8933a; building dark plum #2a1a38; awning red #b8323c + cream #f3e6c8.
- Night street: sky #1b1740 -> #3a2a6a; moon #e8e6ff; lamp cone #ffcf8a (alpha .35); window amber #f2a24a; pavement #14102a.
- Hero: head #0a0a0f (matte black), eye/brow/mouth #ffffff, hoodie red #d8332f (zip/seam #ffffff or #7a1a1a), trousers #14121c, shoes #0c0c10 w/ sole #cfcfd6; rim #f2c9a0. Night-grade hoodie #b07a9a.
- Friend/yellow cap: #f2c230 (cap/head), jacket dark. Examiner: white coat #f4f4f8, round glasses ring #e8e8ee. Green accent kid/opponent #3fbf6a. Visitor: black coat/fedora #0e0e14, glasses frame #6d7280, reflection bars #9fd0ff.
- Gaming room: bg #1d1040 / #5a2fa0 purple, RGB keys #ff3fd0 / #2ee6ff, monitor #2a60ff glow.
- Tennis hall / boxing: near-black brown #0b0508, warm gold spot #f2c27a, arched windows #f0a878 over #3a2230; boxing glove brown #8a5a3a.
- Baseball/football dusk: #5a2a7a -> #d86a8a sky, field green #2f6b3a / #1f4a2a, floodlight white #ffffff. Baseball night grade navy #0e1a3a / #1c2f66.
- Stadium night: stands #3a3270 w/ light dots, pitch #1f6b4a -> #2a8a5a, rays #ffffff alpha .5, cyan fill #5fb8e8.
- HUD text: cream #fff1c9 with glow #ffd88a, dark outline #1a0f2a. VICTORY text #ffd23a. Score card cream #f3e6c8 w/ dark digits #1a1a1a, board brown #5a3a2a.
- End card: bg #140a28 -> #2a0f2e w/ red glow #b02a3a; Subscribe pill #e02a2a, white text.

## 3. Letterbox
Thin black bars top and bottom (~6-7% each: about 15 px top/bottom in a 512-tall frame; to be measured exactly on the mp4). Present for the whole video incl. end card. (Ref1: 41 px of 720 = 5.7%.) => use ~6% unless mp4 measurement says otherwise; ASK for mp4.

## 4. Effects catalogue (with frame facts)
- RADIAL BURST: full-frame cream/white with ~40-60 thin black lines radiating from centre (centre may glow pink/orange), 3-4 frames (ramp 1f, peak 1-2f, fade 1f, sometimes pale grey last frame). Used at every catch/hit/save: 12.43, 85.8, 99.0, 139.9, 176.1, 222.5, 229.4, 295.7, 300.7, 322.3.
- SPEED RING: thin white circle (2 px) appears at the object, scales ~10->50+ px over 6-8 frames, fades; sometimes 2 concentric (310.9 face, 176.3 bat, 13.5 cup, 5.8 fist, 145.1 face).
- WHITE FLASH DIP: 1-4 frames full cream/light grey fading (6.27, 63.47, 31.7, 339.2).
- BLACK FRAME: 1 frame pure black at some cuts (95.1, 102.2, 107.4, 151.4, 228.1, 296.4, 330.93) and blur-through-black smear 4-7 frames (95.07-95.3, 330.87-330.97).
- GHOST ECHO: 2-3 translucent copies (25-40%) offset behind fast limbs/head (boxing 185-188, run 414).
- SPEED LINES: 3-5 thin red/pink horizontal lines across frame (337.7-338.5, 389.1).
- PARTICLES: square confetti (VICTORY, 5 colours), sparks (cable snap, random per-frame dots), sparkle ✦ at ball, sparkle dots twinkle around ball 2-3 frame cycle, crowd camera-flash specks, LED ad-board flicker, window lamp flicker.
- LIGHT: starburst flare (floodlight) with 12-16 rays + bloom pulse; sun disc w/ rays; spotlight cone.
- FLIP CARD score: 20->21 flip ~12-15 frames, black hand reaches in to flip.
- Bars chart infographic: panel with red block splitting into horizontal bars growing left->right over ~25 frames; red title line.
- Label text: appears with fade/scale in 3-8 frames, cream bold glow; HUD stopwatch counts (0.20 s -> 0.29 s) every 3-9 frames.
- Title: line 1 small -> line 2 grows; gold-cream gradient letters w/ dark offset shadow; camera pushes up into sun bloom for transition.
- End card: text builds word by word, icons pop in, subscribe pill pops w/ bell, cursor arm clicks, ring ripple on click; fade to dark at 432.2.
- Screen-in-screen: replay shown on stadium board / cinema screen; camera pushes to fill = transition.

## 5. Transitions (by frequency)
HARD CUT >90%. Others: cross-dissolve 0.3-0.8 s ONLY for location/time jumps (boxing->pitch 208.3; dusk->night street 117.7-118.5; track->bedroom 272.1-273.0; hall->dark); fade to black 0.3-0.4 s before end card (422.2) and at the end; fade FROM black at start (0.0); shrinking-frame iris-to-black (417-418); panel wipe (52.0: right half goes black); bleach-to-white (236.6-237.4) into screen-in-screen; colour-grade flip mid-shot; blur smear.
Cut rhythm: avg shot 3-4 s, action bursts 0.1-0.3 s pose changes with 1-3 s holds around them; emotional beats 3-5 s holds (bedroom boredom, stadium aerial, hero at desk).

## 6. Camera (real moves found)
Locked >90%. Moves: slow lateral pan 326-327.9; slow roll/dutch 78.6-80.3 (house) & 108.4-114.4 (intersection) & 317.7-320.2 (housing); slow push into sun bloom 39.4-40; slow zoom-in on boxing ring 182-184.8; slow zoom-out aerial 368-370; camera tilts down on phone scene 93.8-95.2 (cut-based: torso->legs); drift on night facade during title. Everything else = cuts between angles. Never handheld shake.
Angles used: wide establishing, medium two-shot, OTS with big blurred foreground head, extreme close face (circle fills frame), macro prop insert (fly, cup, ruler, ball, glasses), top-down/overhead, low ground-level, dutch/diagonal, aerial stadium, back-of-head view toward goal, tiny silhouette in huge space (isolation).

## 7. Characters & animation (limited animation, key-pose driven)
- Rig: black circle head, white capsule eyes (+ slanted brow line for anger), white arc mouth/smile, white zipper line; slim torso; 2-segment limbs; mitten hands; gloves yellow for keeper.
- Expressions: neutral (2 dots), smile arcs, 'o' shock (round eyes + 'o' mouth), angry-sharp (slanted brows + bar mouth), half-lidded smug, worried, blink = swap eye shape for 2-3 frames.
- Motion: poses HELD; pose swaps every 1-3 frames only in action; entrances = slide in from frame edge with ease-out 15-20 frames; arm raise 4-6 frames pop; walk cycle ~16 frames/step looped; leg swing 4-8 poses; dive = 4-6 key poses stretched horizontal; ball flights = dot/scale changes per frame, ball approach slow-mo 40 frames. Idle micro-motion (breathing 1-2 px, head tilt) on every held shot so nothing is dead.
- Outfit logic: hero red hoodie (red goalie kit + yellow gloves in football; mauve under night grade); NPCs identified by head/cap colour only: yellow cap (friend/thrower/kicker), green cap (coach/opponent/kid), white coat + round glasses (examiner), fedora+long coat+dark glasses (visitor), pink/zebra stripe runner.

## 8. Environments & ambient life
Kits: night street/townhouse facade (windows, door, steps, moon, lamp cone), cafe (awning stripes, round table, planter), lab/room w/ big window skyline, gaming room (purple, monitors, RGB keyboard, posters), arched-window hall (tennis), baseball field (floodlight towers), boxing ring (single lamp), football pitch (goal, net crosshatch, sunset), track, bedroom, stadium (bowl, stands as dotted texture, scoreboard, rig), black car, end-card void.
Ambient life: window lamps flicker, moon glow, crowd flash specks, LED boards, steam from cup, bokeh drift, light-shaft twinkle, birds/V dots in sky, slowly pulsing bloom, tree silhouettes. Brain rule: every light source must be a visible object + glow + light spill on floor; every location needs 1-2 ambient loops.

## 9. Structure/suspense/emotion (script)
Cold open demonstration (fly) -> escalating examples -> premise/title at ~35 s (after 35 s of hook) -> mechanism explained w/ diagram/labels -> stakes escalation by domain -> cost beat (boredom) -> climactic dilemma (ball or boy) -> quiet reflective aftermath -> twist hook (black car) -> viewer question + CTA. Suspense cues: slow-motion approach, wide->close cuts, silence-like long holds, numbers on screen, clock ticks (119:58...), angry-sharp face = noticing threat, blinding light = bridge to threat. Humour: smug half-lidded face, shocked 'o' mouths, "VICTORY x30", false start. Emotion palette shifts: warm = comfort/ordinary, purple = wonder, blue night = danger/loneliness, gold spot = tension.

## 10. Build implications (Remotion)
1:1 reproducible with: layered SVG/Canvas plates + gradients + blur filters (bake), rim-light outline, rig with pose keyframes (stepped, no tween except entrances/ease), effect library above, per-shot colour grade, vignette, letterbox, text/HUD, flip card, end-card UI. Hard cuts = Sequence boundaries. Biggest cost: ~60+ unique environments/angles (each a layered plate). Plan: environment kits + camera-angle presets; macro/close-up shots reuse the same plates scaled + blurred.
