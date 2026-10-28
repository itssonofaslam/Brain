PROGRESS: complete v1 (sections 1-14). Next: Salman stress-test feedback.
# CAMERA AND SHOTS LIBRARY v1 (batch B3, 2026-10-28)
Purpose: the full cinematic vocabulary of camera angles, shot sizes, composition, movements and transitions, with WHEN and WHY to use each, and HOW to build it in Remotion from our plates (depth map parallax, real-3D character).
Relationship to measured rules: SHOT-GRAMMAR-v3.md and MASTER-SPEC-v1.md are MEASURED from five reference films and WIN any conflict. This library adds the wider cinema vocabulary (Salman: "we have real cinema knowledge"). Default stays: LOCKED camera, faces never move, 79% of cuts change size or angle, about 25% of shots carry an angle/trick, no overshoot or bounce. Every non-default choice needs a one-sentence reason (what feeling or what information it adds).
Numbers marked START are starting values to tune in stress tests.

## 1. SHOT SIZES (ladder) and our codes
| cinema name | our code | frame content | character height in frame |
|---|---|---|---|
| extreme wide / establishing | W (tiny, scale) | world is the subject; figure a dot | about 5% |
| wide / long shot | W | whole body small in the place | 15-25% |
| medium long (cowboy) | M | knees up | about 35-45% |
| medium | M | waist up | 45-60% |
| medium close-up | C | chest up | head about 45% of frame height |
| close-up | C | head and shoulders | head 55-70% |
| extreme close-up | X | eyes/face fill frame, or a part (m flag) | head 85-100% |
| insert / macro | O, H | an object or hand fills frame | no figure |
| top-down | D | camera straight down | varies |
| empty plate | E | place without figure | none |
Measured mix (all films): W25 / C23 / M18 / U10 / O8 / E5 / H4 / D3 / X2 / T1. Genre decides: film = more W and C; explainer = more U.

## 2. CAMERA ANGLES (where the camera sits and points)
- Eye-level (default, 75% of shots): honest, neutral, intimate. Use for dialogue and emotion.
- Low angle (L): camera below, looking up. Power, threat, awe, arrival; towers and city from street level. Plate: "camera on the ground looking up".
- High angle (V): camera above, looking down. Smallness, vulnerability, surveillance, a thing on a table, a plan.
- Top-down / bird's-eye (D): straight down. Maps, aerial flight, a trap, god's-eye view, ground patterns.
- Worm's-eye (extreme L): camera at ground level, figure towers. Rare; confrontation.
- Dutch tilt (Z): tilted horizon. 0.2% in references. At most once per film (crash, loss of balance, madness). Applied as a rotation in Remotion, never requested from the image AI.
- Over-the-shoulder (F/o): a foreground head or shoulder partly in the frame. Dialogue, voyeurism, depth. Foreground head is blurred, sharp subject beyond.
- Two-shot (t): both characters in frame, plain and locked: intimacy, relationship.
- Group shot: three or more, arranged in depth layers.
- POV (P): through the character's eyes; hands can enter the lens. Ability use, searching, fear.
- Reaction shot: close on a face watching something. Follows any big event within 1-2 shots.
- Insert / cutaway: a detail that explains (a phone, a clock, a footprint). Short, 1-2 s.
- Reverse angle: the opposite side of the same place. Use with the 180 degree rule.
- Master shot: wide covering the whole scene; return to it to reset the audience.
- Backlit silhouette (K): light behind, figure dark. Entrance, reveal, sunset ending, threat.
- Scale contrast (S): tiny figure vs huge element. Awe, loneliness, entering a new place.
- Frame-in-frame (R): scene through a window/door/arch/monitor. Being watched, a remote place brought close.
Rules from classic film grammar (use them, they are why shots feel professional):
- 180 degree rule: two people talking keep their screen sides (A left looking right, B right looking left); the camera stays on one side of the line between them; cross it only with a motivated move or a neutral shot.
- 30 degree rule: a cut within the same scene must change the angle by 30 degrees or the size by a clear step, or it looks like a jump.
- Eyeline match: the character looks toward where the next shot is; a look to the right is answered by a cut to what is to the right.
- Match cut: pair two shots by shape, motion or position (circle to circle, same screen position).
- Size = importance: closer = more important or more emotional. Do not waste close-ups on unimportant lines.
- Hold the establishing view long enough to read the place, then go closer.

## 3. COMPOSITION
- Rule of thirds: place the character or eyes on a third line, the horizon on the lower or upper third, not dead centre (centre is for confrontation, shock, symmetry gags).
- Headroom: small gap above the head in medium shots; in close-ups the top of the head may be cropped slightly (the close-up still crops it).
- Lead room / look room: more space in front of where he looks or walks, less behind. Moving toward the empty side feels free; toward the crowded side feels pressured.
- Negative space: big empty area = loneliness, anticipation, dread.
- Leading lines: roads, rails, light beams, rows of seats pointing to him.
- Depth layering: foreground object + character + background = 3D feel; always try to have at least two layers.
- Symmetry: formal, eerie, powerful; one-point perspective for destiny or trap.
- Diagonals: tension and movement. Horizontals: calm. Verticals: power and confinement.
- Horizon height: low horizon = sky dominates, grand, hopeful or threatening; high horizon = ground dominates, small and trapped.
- Frame within frame, foreground blur, light pools: guide the eye to the face.
- Character placement by feeling: small and low in a huge frame = alone; large and central = confronting; at the edge = unsettled; with empty space ahead = hopeful.

## 4. CAMERA MOVEMENTS (what they mean and how we build them)
Default = locked (83% of references). Movement happens only for a reason. Build each from the plate depth map plus the 3D character.
| movement | feeling | build in Remotion | timing / easing (from references) | limit |
|---|---|---|---|---|
| push in (dolly in) | focus, tension, realisation | scale up whole stack about 4-8% with parallax (near layers grow faster) | 2-5 s, linear or ease-in (ref3), or ease-in-out cubic 2-3 s | within parallax budget |
| pull out (dolly out) | reveal context, isolation, end of section | reverse of push | 3-7 s, ease-out quad | within budget |
| pan (turn left/right) | look around, follow, reveal | horizontal drift of layers by depth, up to about 3% frame width, plus up to 2 degrees turn | 2-4 s, ease-in-out | over the budget = new plate or panoramic plate |
| tilt (up/down) | reveal height, awe, shame | vertical drift up to about 3% frame height | 2-4 s | same |
| truck / track (sideways) | follow a walker, travel | layers slide by depth, character walks in 3D | 3-6 s | needs a wide plate or layered plates |
| pedestal / crane up | arrival, ending, grandeur | vertical camera move: layers drift down, horizon lowers | 3-6 s | budget or fly-shot method |
| orbit / arc | importance, fascination, reveal | rotate around subject: small angle only (about 5-8 degrees) using depth + 3D character turn | 3-5 s | beyond that use two plates from different angles and a dissolve |
| follow / tracking behind | chase, journey | character walks, camera drifts with him; background scrolls | 2-5 s | needs wide or long plate |
| handheld | real, alive, urgent | see section 8 | continuous, strength by action | not on diagrams |
| rack focus | shift attention, realisation | change which depth plane is sharp (depth blur) | 12-24 frames, ease-in-out | needs a clean depth map |
| whip pan | energy, time jump, scene link | fast horizontal blur sweep covering a cut between two same-place plates | 6-10 frames | needs two plates |
| dolly zoom (vertigo) | dread, realisation, wrong | push on background while character stays the same size (or opposite) | 1.5-3 s | rare, once per film at most; faked with layer scaling |
| push-through | travel into new space | camera moves through a door/window frame layer into the next plate | 2-4 s | needs a frame layer plate |
| fly shots | space is the story | FLY-SHOTS-3D-v1.md | per that file | per that file |
Rules (measured): faces never move; place and diagram shots may drift or punch in; section ends pull out; moving shots are held longer (push 3.2 s, pull 4.0 s, locked 2.4 s); no overshoot or bounce on any camera move.

## 5. PARALLAX BUDGET (anti-stretch, from IMAGE-PROMPTS-v2)
- One plate: push-in up to about 8% scale, drift up to about 3% of frame width, turn up to about 2 degrees. Handheld translation counts toward the budget.
- Layers: split the plate into near / mid / far by depth; inpaint the area revealed behind each near layer; blend depth edges softly; never stretch triangles.
- More movement than the budget: (a) cut to a new plate of the same place, (b) dissolve between two plates, (c) fly-shot method, (d) a plate made for movement (a wide panoramic or tall plate; ask Salman for a bigger plate via the world prompt writer).
- Close shots on the character move the character in 3D more than the plate; keep the background drift small and let the blur hide it.

## 6. PLATE REQUIREMENTS PER SHOT (connect to WORLD-PROMPT-WRITER-v1.md)
| shot or move | plates needed |
|---|---|
| locked shot | 1 plate |
| push-in / pull-out / small pan / tilt | 1 plate, within budget |
| orbit beyond about 8 degrees, reverse angle, whip pan | 2 plates of the same place (same-place prompt) |
| truck/follow over a long distance, travelling wide | 1 extra-wide plate or 2-3 same-place plates in sequence |
| push-through | plate with a frame object (door, window) + plate beyond it |
| dialogue | master plate + reverse plate (and optional close-up backgrounds) |
| fly shot | per FLY-SHOTS-3D-v1.md (depth layers) |
| X extreme close-up | background-only plate (blur turns light sources into bokeh) |

## 7. LENS LOOK AND BLUR (made from the depth map; closer shot = more background blur)
- Focus plane = the character (or the key object). Everything else blurs by its distance from that plane. Bright points in the blurred area become soft bokeh discs (round, slightly brighter at the edge for a premium look).
- Lens feel by shot size (START values, blur radius at 1080p for the farthest background; tune in stress tests): tiny wide 2-5 px; wide 4-8 px; medium 8-14 px; close 14-24 px; extreme close 24-40 px; macro 30-50 px. The look-target close-up background is heavily blurred: that is the extreme-close value.
- Wide lens feel (wide shots, S, L): deeper focus, strong perspective, less blur. Long lens feel (close-ups, X): compressed background (far layer scales slightly larger than near), strong blur.
- Foreground objects (F) are blurred more than the background when they are very close.
- Rack focus: move the focus plane between two things (character to object) over 12-24 frames, ease-in-out; use for realisation and reveals.
- Split focus: two planes sharp (character and a far object), blur between; rare, for tension.
- Bloom/halation: bright lights glow with a soft warm halo; strength follows the light recipe. Glow is applied to character and plate together.
- Chromatic fringe, lens flare, anamorphic streaks: tiny amounts only on the brightest lights; never on faces.

## 8. HANDHELD (noticeable, cinematic, strength follows the action) - Salman's requirement
Locked stays the DEFAULT camera. Handheld is an added option for real-life or action beats, mostly close-ups and medium shots, never on diagram, UI, text, or title shots.
Parameters (START values, 1080p; tune in tests):
| level | feel | position shake | roll | speed | use |
|---|---|---|---|---|---|
| H0 | locked | 0 | 0 | - | default, diagrams, calm, formal |
| H1 | breathing | 2-3 px | 0.15 deg | 0.3-0.6 Hz | tense listening, intimate close-up, held breath |
| H2 | gentle | 5-8 px | 0.4 deg | 0.8-1.2 Hz | dialogue, walking beside, quiet fear |
| H3 | active | 10-18 px | 0.8 deg | 1.5-2.5 Hz | hurrying, argument, rising panic |
| H4 | violent | 25-45 px | 1.5-2.5 deg | 3-5 Hz | running toward camera, chase, being hit, explosion nearby |
Rules:
- Strength follows the action: character running toward the camera = H4 plus a quick push; standing still in awe = H0 or H1. Decide per beat, change levels with a ramp of 12-30 frames, never snap.
- Noise is smooth (two-octave noise), not a sine wave, with slight sway on the vertical axis (breathing); add a rare tiny drift.
- Impact shake: an impulse of 15-40 px that decays over 12-24 frames (impact, stomp, explosion). No overshoot of the final settle position beyond the decay.
- Parallax coupling: shake is a camera move through the depth layers, so near layers shift more than far ones. That is what makes it feel 3D. It consumes parallax budget: keep H3-H4 on shots with generous plate margins (render the plate about 6-8% oversized).
- Focus breathing: a tiny blur change on H3-H4 sells realism (optional).
- The character's own motion is separate (performance layer); handheld never replaces his animation.
- Dialogue: H1-H2 in close-ups, slightly different noise on each speaker's shot so they do not match.
- Muted-understanding: handheld must support the story (urgency), not be decoration.

## 9. DIALOGUE COVERAGE (two or more characters talking)
Dialogue text is the script brain's job; the director must be able to stage it.
1. Establish: master two-shot (locked, plain) showing both, relative positions, the place.
2. Singles: close-up on the speaker, placed on the left or right third, looking toward the other with look room, background blurred, the other character's shoulder/head partly in the foreground (F) for depth.
3. Reaction: cut to the listener at the key words, not always the speaker; the face tells the story.
4. 180 degree line: A on the left looking right, B on the right looking left, in every shot of the scene.
5. Rhythm: cut when a line ends or on the listener's reaction; hold longer on emotional lines; do not cut every line; usual single holds 1.5-3.5 s (references: mean shot 1.9-3.2 s).
6. Eyelines: slight angle toward the other person, not into the lens (never into lens unless a deliberate fourth-wall beat).
7. Handheld H1-H2 optional on singles; two-shots stay locked.
8. Character turns: the 3D heads and torsos rotate toward the speaker; the head plate turn shows the black dome when turned past about 60 degrees, so mood in profile is carried by posture and hands.
9. Plates: master plate + reverse plate of the same place (same-place prompt), plus background-only plates for close-ups.
10. Voices: one constant narrator voice per channel; different voices for characters in each video (sound brain later).

## 10. TRANSITIONS (camera and edit)
- Hard cut: default. Cut on action or on a look. 79% of cuts change size or angle.
- Match cut: same shape, position or motion carries across (a circle sun to a circle lamp).
- Dissolve: 6-14 frames, only at world crossings or time passing (measured 6-14 f).
- White-out / flash: 1-2 frames at a burst or a portal; 3.3 s white-out portal seen in the gravity film.
- Black strobe: 1-2 frame black flashes for facts or shocks (measured in ref3).
- Whip pan: 6-10 frames of horizontal blur between two plates of the same place; energy or time jump.
- Push-through: through a frame object into the next plate.
- Blur-into-blur: rack-focus out of one shot into the next shot's blur; soft emotional link.
- Fade to black: endings only (or a long time skip).
- J-cut / L-cut (audio leads or trails the picture): note for the sound brain.
- Colour grade switch as a feel device: see FEEL-DEVICES-v1.md.

## 11. DECISION ENGINE v4 (adds to SHOT-GRAMMAR v1-v3; order matters)
1. Beat in one sentence: what happens, what the viewer must feel, what the viewer must understand.
2. Size by SHOT-GRAMMAR v1/v2 (new place = wide 75%; emotion = close 75% / extreme 24%).
3. Angle: default eye-level; add one trick from section 2 only if the function matches; at most 3 tricks in a row; no repeated size+angle more than twice.
4. Composition: thirds, look room, depth layers; place him for the feeling (small = alone, large = confront).
5. Movement: locked by default; push for focus, pull to end, pan/tilt for place, handheld only if the beat is real-life/action; give the reason in one sentence.
6. Lens: set blur by shot size; choose focus plane; decide rack focus if attention shifts.
7. Light: pick from WORLD-PROMPT-WRITER lighting recipes; match rim light.
8. Plates: how many plates does this shot need (section 6)? Write the plate requests.
9. Transition in: how does this shot connect to the previous one (cut / match / dissolve)?
10. Muted test: could someone understand this shot with no sound? If not, add a visual cue (a prop, a gesture, a text card).
11. Variety test: compare with the last 5 shots; change at least one of size, angle, movement.
12. Log the decision (shot id, size, angle, move, handheld, plates, reason) to the video state file.

## 12. SHOT RECIPES BY FEELING (starting templates; the brain invents variations)
| feeling | size / angle | movement | handheld | blur / light |
|---|---|---|---|---|
| awe, scale | tiny wide, scale contrast S, low horizon | slow pull out or crane up | H0 | deep focus, large glow |
| loneliness | wide, small figure in negative space, lead room behind | locked or very slow pull | H0 | soft glow, long shadow |
| fear, dread | low angle or slightly high, tight, symmetrical corridors | slow push, sometimes dolly zoom once | H1-H2 | darker, cool rim |
| panic, chase | close/medium, behind-follow or run toward camera | push + shake | H3-H4 | heavy blur at edges, hot rim |
| realisation | medium to close, rack focus, face | slow push in | H0-H1 | focus pulls to the key object or the eyes |
| joy, relief | medium to wide, eye level, open space ahead | gentle crane or pull out | H1-H2 | warm bright glow |
| shock | cut straight to extreme close-up of eyes, then wide | locked, impact shake | impulse | white or black flash 1-2 f |
| power, threat | low angle, backlit silhouette K | slow push | H0 | strong backlight, rim |
| intimacy | two-shot, plain eye level, close singles | locked | H1 | warm soft light, window glow |
| mystery, secrecy | high angle or frame-in-frame R, shadows | slow drift | H1 | dark, shafts of light |
| decision, resolve | close, eyes, determined brows | slow push | H0-H1 | rim light brightens |
| ending, quiet | wide, K silhouette or S | slow pull out, fade | H0 | sunset or fade |

## 13. COMMON MISTAKES (stress-test checklist)
- Moving the camera with no reason; handheld on diagrams; too many tricks in a row.
- Crossing the 180 degree line in dialogue; cutting with no change of size/angle (jump cut).
- Centre-placing him every shot; no look room; no foreground/background layering.
- Camera moves bigger than the parallax budget (stretching) instead of a new plate.
- Blur the same for every shot size; face blurred when he should be sharp; focus plane on the wrong thing.
- Same light and same palette for many beats; rim light colour not matching the world light.
- Dutch tilt used more than once; dolly zoom more than once.
- Close-ups wasted on unimportant lines; no establishing view when a new place begins.

## 14. FILE LINKS
Measured rules: SHOT-GRAMMAR-v1/v2/v3.md, MASTER-SPEC-v1.md, labelling/*, CAMERA-BY-SHOT-TYPE.md. Plates: WORLD-PROMPT-WRITER-v1.md. Character: CHARACTER-BRAIN-v1.md. Effects: EFFECTS-FOR-FEEL-LIBRARY (B4). Movement of the character: PERFORMANCE-LAYER (B5). Fly shots: FLY-SHOTS-3D-v1.md. Requirements: DIRECTOR-BRAIN-REQUIREMENTS.md.
