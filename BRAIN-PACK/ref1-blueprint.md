# TELEKINESIS: WHAT IT REALLY IS + HOW WE REBUILD IT IN ONE REMOTION RENDER
(Based on all 70 PDF pages. Evidence level: look = high, motion = medium (10 fps sheets), camera = low-medium. Not yet verified against the video file.)

## 1. WHAT THE VIDEO REALLY IS
A 4:25 narrated "what if" story told as LAYERED 2D MOTION GRAPHICS with a cinematic grade. Not rendered 3D. It is built from:
1. Static scene kits (bedroom, street, stage, news desk, diner, court, apartment exterior, skyline, dark infographic space) made of flat shapes + soft gradients.
2. One tiny cast of identical-style figures (black glossy circle head, white face marks, solid torso, thin limbs), colour-coded by role.
3. Props with a cyan glow when telekinetic.
4. Overlays: labels, HUD bar, graphs, chalkboard, cheque, stamp, lower-third, phone frames, UI end card.
5. A small effect vocabulary (radial burst, halo, float-up, glide, label pop, draw-on, grid multiply, spotlight fade, white-out, wipe).
6. A hard-cut edit with about 75 cuts, locked camera, and black letterbox bars.
7. A grade: vignette, bloom/glow, foreground blur blobs, bokeh discs, atmospheric haze, slight grain.
WHY IT FEELS 3D: light cones, rim light on heads, glow, blurred foreground, bokeh, depth layers, haze, and small smooth object motion. None of this needs a 3D engine.

## 2. LAYER STACK (back to front) FOR EVERY SHOT
 1 sky gradient (purple -> orange near horizon)
 2 far skyline silhouette (flat rects, tiny gold windows, 2 tones)
 3 near buildings/wall/room geometry (flat, slightly lighter)
 4 floor plane (dark gradient) + warm light pools (soft radial gradients)
 5 mid props (bed, desk, lamp, car, pedestal, desk, booth)
 6 characters (rig) incl. rim light
 7 telekinetic props with cyan halo
 8 light cones (triangle + vertical gradient + blur)
 9 foreground blur blobs / bokeh discs (large circles, blur 20-40 px, low opacity)
10 haze (large soft gradient overlay)
11 vignette
12 HUD/labels/graphs
13 letterbox bars (about 11% top and bottom)
14 optional light grain
Each shot = a small "kit" component + a list of timed events. Kits are reused (bedroom appears about 12 times).

## 3. CHARACTER RIG (code)
Parts: head circle (r about 0.085 of frame height), rim-light arc (pale stroke on lit side), eyes (2 small white dots or arcs), brows (arcs, angle by emotion), mouth (small arc: smile/flat/open/strained), neck stub, torso (trapezoid, role colour), upper arm + forearm (thin rounded lines, 2 joints each: shoulder + elbow), hand (small black mitten), upper leg + shin, shoes optional.
Expressions (swap, not tween, for clarity; 2-4 frame cross-fade OK): neutral, startled, worried, strained, determined (closed-eye arcs), smile, asleep, hungry.
Poses: stand, point (arm out), raise-both-arms, reach, hold-head, sit-on-bed, lie (bed/couch), sit-at-table, walk (4-frame cycle, slow), float (legs dangling, small sway), hold box, hold phone, throw.
Variants by script: hair (ponytail, bun, cap/helmet, none), height, width, age (hunch + cane), outfit colour, accessories (tie, backpack), zombie/other.
Crowds: same head with random colour/pose offsets, rows with depth scale, smile marks.
Rim light: a 2 px light arc on the side facing the key light (warm window or cyan prop) = the "premium" cue.

## 4. ENVIRONMENT KITS
Bedroom (4-pane window with sunset + skyline, bed, nightstand with clock/cup/books, desk, lamp, wall art circle); Street (row of houses with gold windows, car, rail line, rain streaks); Stage (dark gradient, 4-6 cones, big blue ring outline, oval platform glow, pedestal, truss + lamps, audience silhouette rows at bottom, 300 label); News desk (blue desk, monitor, lower-third); Diner (red booth strip, counter, fries); Court (fence, hoop, skyline); Apartment exterior (blocks, warm door, lamp bokeh); Skyline wide (many small windows twinkling); Info space (dark blue gradient + panels); History stage (olive-gold tint + long table); Camera grid (3x3 tiles); End card (text + row of mini characters + UI buttons).
Palette tokens: purple dusk #3a2a5a-#7a4f8a, orange glow #f0a060, navy #101428, hero blue #2f6bff, friend green #3fa860 + yellow #f2c230, crush pink #e8567a, cyan glow #5fd8ff, red danger #e0343c, cream text #f3e6c8, olive-gold #6b5a2a.

## 5. EFFECT LIBRARY (starting values; tune by eye)
- Radial burst: 24-40 thin white lines from a point, length grows 0 -> 60% frame, opacity 1 -> 0, 5-8 frames, ease-out. Used at: pen 3.8, bulb 37.4, hoop 73.3, snap 155.8, brain 243.0.
- Cyan halo: duplicate prop, blur 6-12 px, cyan, opacity 0.7, add soft pulse (+-8%) at 1 Hz.
- Float-up: ease-in-out 30-40 frames, up 25-35% of frame, then sway +-4 px and +-2 deg.
- Glide/translate: ease-in-out over 20-30 frames, slight rotate (rotation 0 -> 80 deg over 80 frames for the pen).
- Label pop: scale 0.85 -> 1.04 -> 1.0 and opacity 0 -> 1 in 6-8 frames.
- HUD bar: width tween 0 -> value over event duration, ease-out, stays on screen between shots in the same sequence.
- Draw-on: stroke-dashoffset animation, chalk lines 0.2-0.4 s per stroke; graph curve draws over 2.5 s.
- Typing text: letters appear at 2-3 frame intervals (TELEKINESIS).
- Grid multiply: 1 -> 2 -> 3 -> 6 -> 20 -> 40 tiles over 2 s, with particles drifting.
- Spotlight fade-in: cones fade in one by one 3-5 frames apart.
- White-out: brightness to white over 2-3 frames, hold 15-20 frames, hard cut.
- Stamp slam: scale 1.8 -> 1.0 with rotation -8 deg over 6 frames + small bounce; red, rough texture.
- Lower-third slide: from left, 8-10 frames, ease-out.
- Fade to/from black: 6-12 frames.
- Wipe (panel): hard-edged vertical mask sweeping 6-8 frames.
- Slow zoom on card: 1.0 -> 1.25 over 1.5 s, ease-in-out.
- Bokeh drift: 8-14 discs, speed 3-8 px/s, blur 18-30 px.

## 6. HOW THE FULL VIDEO IS BUILT (one render)
Files: timeline.ts (list of shots), kits/ (scene kits), rig/ (Character.tsx + poses.ts + faces.ts), fx/ (Burst, Halo, FloatUp, Glide, LabelPop, HudBar, DrawOn, GridMultiply, SpotFade, WhiteOut, Stamp, LowerThird), grade/ (Letterbox, Vignette, Haze, Grain, Bokeh), Root.tsx (one composition: full video length).
Flow: (1) he gives script + voiceover + timing file (word ms). (2) The brain converts every beat to a SHOT: {id, startWord, endWord, kit, camera: locked|zoom|tilt, cast, poses, events: [{type, anchorWord, offsetFrames, params}]}. (3) timeline.ts is generated with frames = round(ms/33.333). (4) Remotion renders the whole video in one pass; any shot's frames are derived from the global clock so cuts land exactly on the word.
Cut rule from the reference: cut on narrative change (not on every noun); average shot 3.5 s; holds 5-7 s for number/emotion beats; use fade-to-black for time jumps (night -> day, sleep, end of act) and fade-to-white for physical overload.

## 7. FEEL ENGINEERING (how to match the strong feel)
Scale contrast (hero is about 1/6 frame height), rising-stakes ladder, a personal victim (child), irony shot (cameras on wrong object), darkness + silence beat after the climax, face close-ups with bokeh, colour as meaning, comedy to release tension, bookend ending. Write each script beat with: emotion, scale, colour, hold time, effect, sound cue.

## 8. WHAT CODE CAN DO AND WHAT TO WATCH
- All of the above is vector/CSS/SVG; no AI images needed. If we later want a painted look, backgrounds can be AI plates behind the same rig.
- Heavy items: many blurred layers (glow, bokeh, haze) are slow to render. Mitigation: pre-bake glow sprites as PNG, limit to 2-3 blur layers per shot, concurrency 2.
- Render time: 7,975 frames at about 1.5-3 s per frame = about 3.3-6.6 hours for a 4:25 video on his laptop (needs a real test; blur and size change it). Plan: render in one pass but use still checks first.
- Resolution: reference is only 910x512; we can render 1920x1080 (letterboxed content area about 1920x846 if we keep their bars).
- Unknowns: exact easing curves, exact glow colours, whether tiny parallax exists. Fix with the mp4 file if he can upload it.

## 9. TEST ORDER (when he says build)
T1: bedroom kit + hero rig + pen float with halo + burst (matches 0-6 s). Compare frame by frame.
T2: stage kit with cones, ring, audience, 300 label (matches 137-141 s).
T3: face close-up with bokeh + expression swaps (148-152 s).
T4: white-out + black + glowing lamp (181-185 s).
T5: grid multiply + labels (84-87 s).
Then lock the master style description and the code settings together.
