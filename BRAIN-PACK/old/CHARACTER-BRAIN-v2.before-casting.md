PROGRESS: complete v2 (sections 1-12). Written 2026-10-29 from CHARACTER-SPEC-v2.md (Salman's canonical text spec). Replaces CHARACTER-BRAIN-v1 (old copy in old/CHARACTER-BRAIN-v1.before-character-v2.md). Section numbers 3, 6, 7, 8, 9 are kept the same as v1 on purpose, so cross-references still work.
# CHARACTER BRAIN v2 (2026-10-29)
Source of truth: CHARACTER-SPEC-v2.md (verbatim, locked). This file turns it into what the brain uses per shot: invariants, numbers, rig channels, expressions, materials and light, scale by shot size, views, other characters, QA. Where this file and the spec differ, THE SPEC WINS; fix this file and log it. Numbers marked (brain) are start values the spec left open; the simplest choice consistent with the spec was taken. Building or replacing the code is CHARACTER-IMPLEMENTATION-PROTOCOL-v1.md.

## 1. INVARIANTS (never change, in any shot, in any scene)
1. One large, smooth, warm ivory SPHERICAL head (#F1E3D8, satin, non-metal). Near-perfect sphere; never egg, cube, pointed.
2. Exactly two vertically oval glossy near-black eyes (small catchlight each). Two thin dark eyebrows. One small subtle mouth. Features are real 3D elements on the curved surface, front only.
3. No nose, ears, hair, beard, mustache, freckles, helmet, hat, markings. Back and sides of the head are plain smooth ivory.
4. Slim charcoal-black neck (#252629), narrow almost line-like torso, two long thin arms, two long thin legs. Stick silhouette always: no broad shoulders, muscles, thick thighs, human chest, pelvis mass.
5. Small ivory hands with a palm, one thumb, four simple fingers, rounded tips (not cartoon gloves, no nails or veins).
6. ONE turquoise wristband (#1BB3C7) on the anatomical LEFT wrist (local +X). Never moves to the other wrist, never recoloured, resized or removed.
7. Chunky matching black sneakers: near-black upper, thick off-white sole, white/pale-grey laces, one small unbranded white side mark each, raised ankle collar.
8. One compact matte-black daypack worn on the back (local -Z), two narrow straps, one main compartment, small front pocket seam, zipper line. No text, logos, patches, keychains. Permanent unless the story shows him taking it off.
9. Fixed palette (section 7). Lighting changes brightness, never the base colours. Never recoloured to match a background.
10. NO thick outline around the model, no cel-shading, no low-poly facets, no photoreal skin or fabric noise. Smooth premium stylised 3D.
11. Proportions never change: no squash and stretch, no limb thickening, no limb length change, no head growth for surprise. Expressions move brows, eyes, lids, mouth and head only.
12. Same single 3D model from every angle and in every scene.
Orientation: Y up, face toward +Z, anatomical left = local +X, anatomical right = local -X, floor at Y = 0. Facing the camera, the wristband appears on the viewer's RIGHT. It never swaps with camera angle.

## 2. PROPORTIONS (model units; total height 4.0; head diameter 0.94 = 1 head unit HU)
| part | value |
|---|---|
| total height | 4.0 (about 4.26 HU; head is about 23.5 percent of height) |
| head | centre (0, 3.54, 0); width 0.94, height 0.94, depth 0.88-0.92 (start 0.90) |
| neck | about 0.30 long, thin, overlaps into head and torso |
| shoulder level / pivots | Y 2.74 / X +-0.20, Y 2.72 (shoulders much narrower than the head) |
| torso | Y 2.74 down to pelvis Y 1.70, length 1.04, max width 0.12-0.16 |
| arms (relaxed standing) | elbow Y about 2.15, wrist Y about 1.72, hand extends a little below; these are vertical drops in a slightly bent relaxed pose, so segment lengths are start values about upper 0.57, forearm 0.43-0.46 (brain); once chosen they never change. Radii: upper 0.045-0.055, fore 0.035-0.050 |
| legs | hip Y 1.70, knee about 1.00, ankle about 0.32, sole at 0; so leg (hip to floor) = 1.70 (42.5 percent of height). Radii: upper 0.045-0.055, lower 0.035-0.050; slight gap between legs |
| shoe | length 0.48-0.52, width 0.22-0.26, height 0.28-0.30, sole 0.06-0.08 thick |
| backpack | width 0.40-0.46, height 0.55-0.62, depth 0.16-0.22; centre about Y 2.30-2.40, behind the torso (-Z), hugging the back |
Silhouette read: large round head, thin neck, slim body, long thin arms, long thin legs, oversized dark sneakers; it must read as a dark silhouette from far away.
Scene scale: the scene scale formula uses character_height = 1.0 scene unit (WORLD-PROMPT-WRITER section 6); the model is scaled uniformly (4.0 model units = 1.0 scene unit) at the character's root. Never scale parts unevenly.
Step lengths, gait and "x leg" values in PERFORMANCE-LAYER use leg = 1.70 model units.

## 3. HEAD BUILD
- High-resolution smooth-normal sphere, radius about 0.47, depth very slightly less than width. One material (satin, section 7). No seams, no plate, no inset disc, no rim ring.
- Neck enters the underside of the sphere and disappears into it; it must never show inside the face and never poke through the front from a low angle.
- Eyes: each about 0.10-0.13 wide, 0.18-0.22 tall, 0.04-0.06 deep, convex, centres +-0.15 from the centreline (about 18.6 degrees each side on the sphere), slightly above the head's horizontal midpoint (brain: about +0.04 to +0.08 above head centre), tilted slightly outward to follow the surface, sitting close to the skin (no floating).
- Brows: thin tube curves (brain: about 0.28 above head centre, each about 0.14 long) following the curvature, understated, same thickness and colour always, independent L/R.
- Mouth: small dark shape below the eyes (brain: about 0.20-0.24 below head centre, calm width about 0.12-0.16) made of real geometry that follows the surface, never a flat sticker.
- Turning: everything on the front turns with the head as one assembly. Because the eyes sit about 18.6 degrees off the centreline, the FAR eye foreshortens hard past about 50 degrees and is hidden by about 70-75 degrees; the near eye is gone by about 110 degrees; from behind there is only the plain ivory sphere. At 90 degrees (profile) one eye and the brow edge are visible on the curve; the mouth is near the edge.
- Back of head: plain smooth ivory, never flat.

## 4. FACE LAYOUT (percent of head diameter 0.94, derived)
- Eye width about 11-14 percent, height about 19-23 percent, centre spacing about 32 percent. Eyes read at distance as two dark ovals on a bright ball.
- Eye look: the eye geometry slides over the sphere surface by a small amount (brain: up to about 0.05 units, roughly 5 percent of D) and keeps following the curvature; beyond that the head turns.
- Catchlight: one small restrained highlight per eye on the side facing the key light, the same spot on both eyes; default upper right if the light is flat. It stays fixed to the light while the eyes move (the eyes stay glossy and alive).
- Eyelids (brain): simple ivory lid caps (same material as the head) that slide down over the oval for blink, sleepy, laughing, suspicious. No anatomical eyelid detail. (Scaling the eye height is an allowed fallback if the rig cannot do lids.) Blink 3-4 frames closed-open; a slow blink 8-10 frames.

## 5. EXPRESSIONS (parameters, so the brain can invent more; all from the same head)
Parameters: brow height L/R, brow angle L/R (inner end up = worried, inner end down = angry), brow arch, eye openness L/R (0 closed, 1.0 neutral, up to 1.2 wide; lids), eye look x/y, mouth shape blend, mouth width, head tilt/pitch/yaw, small body support (lean, hands).
| expression | brows | eyes | mouth | head and body |
|---|---|---|---|---|
| neutral | relaxed, level | open 1.0 | small closed restrained curve | level |
| happy | slightly raised | lively, open 1.0-1.05 | gentle upward curve | slight lift |
| sad | softened, inner ends up, lowered | slightly lowered gaze, 0.9 | small downward curve | head down a little |
| surprised | raised high | widened 1.15-1.2 | small round open O | head back slightly, hands lift quickly |
| angry | inward and down | focused, narrowed 0.85-0.9 | tighter, flat | forward lean, tense |
| worried | inner ends raised | uncertain look, darting | small tense line | small shrink |
| confused | uneven (one up) | one slightly narrower, look aside | small asymmetric | head tilted |
| excited | raised | bright, wide 1.1-1.15 | open smile | bounce, hands up |
| shy | slightly up inner | lowered gaze | small restrained smile | slight tilt, turn away |
| sleepy | lowered, relaxed | lids half closed 0.4-0.6 | relaxed | head droops |
| thinking | one brow slightly raised | looks up or at an imagined object | small closed | tilt, hand near chin |
| scared | lifted | wide, alert 1.2, eyes dart | open | head pulled back, shrink |
| laughing | raised | narrowed joyful 0.5-0.7 | open smile | head and body move with the laugh |
Suspicious (extra): brows slanted, eyes narrowed 0.7-0.8, side look. Invent more (smug, relieved, tired, embarrassed) from the same parameters only. Never add tears, sweat, blush, teeth or tongue (a tiny dark interior in an open mouth only when an animation truly needs it). Blend over 4-10 frames, fast for shock, slow for mood (PERFORMANCE section 4). Mouth shapes stay clean and stable (no flicker, no intersections).

## 6. JOINTS AND LIMITS
Rig (hierarchy from the spec): CharacterRoot > Pelvis > Torso > Neck > Head (LeftEye, RightEye, LeftEyebrow, RightEyebrow, Mouth); Torso > LeftShoulder > UpperArm > Elbow > Forearm > Wrist > Hand (+ TurquoiseWristband on the LEFT wrist); RightShoulder ... RightHand (no band); Pelvis > LeftHip > UpperLeg > Knee > LowerLeg > Ankle > Sneaker; RightHip ... RightSneaker; Backpack follows the torso with a small delayed spring.
Joints: head (yaw, pitch, roll), neck small, shoulder x2 (multi-axis), elbow x2 (bend, small twist), wrist x2, finger groups per hand (relaxed curl, point, grip, open, wave; individual fingers when a close shot needs them), hip x2, knee x2, ankle x2, torso lean and twist.
Limits (START; keeps him solid, not rubber): elbow 0-140 degrees, knee 0-130, shoulder up to straight overhead, wrist about +-60, head turn +-100, nod +-40, torso lean +-25. Knees and elbows never bend backwards. Pivots sit at the joint, so limbs swing about the joint, not about their middle. Overlapping rounded geometry hides joint gaps; no big ball joints. Limbs keep constant length and thickness in every pose (no scaling to fake bends). Create once, animate transforms only (never rebuild per frame). Backpack: delayed by about 2-4 frames, tiny amplitude, a critically damped function of body motion; never floats off the back when running, jumping or bending.
Movement quality: PERFORMANCE-LAYER-v1.

## 7. MATERIALS AND LIGHT
| part | colour | finish (START) |
|---|---|---|
| head, hands | #F1E3D8 | non-metal, satin, roughness 0.38-0.48 (spec), soft highlights, never wet/chrome/glass/plastic |
| neck, torso, arms, legs | #252629 | subtle matte (brain: roughness about 0.55-0.7), enough definition to separate from dark backgrounds, never grey/silver, never a black hole |
| eyes | #080808 | glossy (brain: roughness about 0.1-0.2) with a small controlled catchlight |
| eyebrows, mouth | #080808 | matte-to-soft |
| sneaker upper | #191A1D | mostly matte synthetic |
| sneaker sole | #E7E3DD | matte rubber, layered edge, no tread |
| laces, side mark | #F0EFEB | matte |
| backpack | #141518 | matte fabric-like by clean geometry, no noisy texture |
| wristband | #1BB3C7 | slightly smoother than the body, restrained highlight, not metal, never emissive |
Light (spec section 25): soft key, gentle fill, SUBTLE rim light when appropriate; smooth lit-to-shade transitions; good anti-aliasing and shadows; no excessive bloom, harsh outlines, oversaturation or plastic shine.
- Rim light (decision H1, see section 11): kept as a default, now SUBTLE: strength 0.3-0.7 (not the old 0.6-1.0), thin, colour = the strongest back/side light. It may go to 0 only when the scene light motivates it (flat overcast, deliberate silhouette).
- Readability: the black limbs stay readable on light and dark backgrounds (fill or rim, never a flat black hole); the sole and laces stay distinct from the dark upper; the head stays at least about 35 percent brightness on expression beats; in silhouette shots the stick shape alone must read.
- Reflections: no chrome. Soft broad highlights on the satin head and the wristband, a catchlight in the eyes, only gentle sheen on matte parts. Reflection on a wet or glossy FLOOR is allowed (dimmer than the figure).
- Contact: soft contact shadow under the soles (soles touch Y = 0). Grain, haze and glow of the world apply over him last so he belongs in the picture.
- Grade never recolours him: only light colour, rim and shadow change his appearance.

## 8. SCALE BY SHOT SIZE (figure height as percent of frame height; head = about 23.5 percent of the figure)
| shot | figure in frame | what reads |
|---|---|---|
| tiny wide | about 5 percent | a bright ivory dot on a thin dark stick; silhouette; posture only |
| wide | 15-25 percent | ivory ball head, stick body, backpack and sneakers readable; eyes as dots |
| full / medium wide | 45-60 percent | whole body, face readable, wristband and sneakers visible |
| medium (waist up) | head about 30 percent of frame height | face, brows, mouth, hands; backpack straps |
| close (head and neck, shoulders) | head 55-70 percent of frame height | eyes, brows, mouth, catchlights |
| extreme close | head 85-100 percent, or eyes/mouth/hand/wristband only | catchlight, brow shape, satin surface, finger detail |
Because the head is only about a quarter of his height, a "full figure" shot shows a small face: for emotional beats prefer medium or closer; use full shots for posture, locomotion and scale. Simplify with distance; close-ups need the full-detail face and hands (fingers, wristband, sneaker laces for foot macros).

## 9. VIEWS AND ANGLES (one model rotated; never a separate drawing)
- Front: centred head over torso, two symmetric eyes, brows, mouth, thin neck, narrow torso, arms hanging at the sides, wristband on the viewer's right, two separated legs, matching sneakers flat and pointing forward; backpack mostly hidden (straps or side edges only).
- Three-quarter (30-45 degrees): sphere volume, both eyes with the near one more prominent, far eye foreshortened (not vanished), near and far arms at different depths, wristband when the left wrist is visible, rounded sneakers, backpack side/straps; near shoe larger only by perspective.
- Side (either): smooth sphere, one eye on the curve (far eye hidden), no nose or muzzle, narrow neck, thin torso, backpack projecting slightly behind, sneaker toes forward, heels toward -Z, thick soles, collars.
- Back: plain ivory hemisphere (no features, not flat), neck joining naturally, narrow torso, backpack centred on the upper-to-middle back with two straps over the shoulders, arms either side, black heels with the off-white sole wrapping round, legs thin and separated. Nothing added that is absent from the front.
- Top: round ivory upper hemisphere, eyes not on top, backpack footprint compact behind the torso, straps connected, sneakers with real volume.
- Low angle: head stays attached to the neck, eyes on the curve, underside of the head closed (no hollow, no loose geometry), neck never through the face, soles with real thickness; legs and torso keep their lengths (no stretch from perspective except true lens perspective).
Expression beats: keep the head within about 50-70 degrees of the camera so the face reads; use profile or back views for posture beats.

## 10. OTHER CHARACTERS AND CHECKLIST
Other people (doctor, stranger, friend, crowd): same stickman design language (spherical head with oval eyes, slim stick body, simple hands and shoes), but different height, build, head tint (warm ivory, pale cool, tan, dusky), one costume piece in the same clean style (coat, hat, scarf, glasses as simple shapes), maybe a different brow or eye shape. Crowd and background people: slightly blurred, simpler. The MAIN character alone has the exact spec: ivory head, charcoal body, turquoise left wristband, black daypack, white-soled sneakers; others must not have the turquoise band and must be distinguishable beside him. Children: head larger share of height (about 30-35 percent), smaller, quicker. Invention protocol: PERFORMANCE-LAYER section 11.
QA checklist (every stress test, every shot with him):
- Head a smooth sphere in this view? Ivory, not pure white or grey? Face only on the front? Features attached to the curve?
- Two oval eyes with catchlight, thin brows, small mouth? No nose, ears, hair?
- Body charcoal, torso narrow, limbs thin with constant length and thickness, no big ball joints?
- Hands with thumb and four fingers (not gloves, not mittens)? Wristband on the anatomical LEFT wrist (viewer's right when facing camera)?
- Backpack on the back, close, straps connected, never floating or missing without a story reason?
- Sneakers: dark upper, thick off-white sole, laces, side mark; soles on the floor?
- Subtle rim light matches the world's light; limbs readable; head at least about 35 percent bright; no thick outline?
- Expression readable at this shot size? Proportions unchanged (head about a quarter of the height)?

## 11. WHAT CHANGED FROM v1 AND DECISIONS TO CONFIRM
v1 (chibi coin-head: black glossy sphere with cream face plate and thick black rim, thick glossy black tubes, mitten fists, round shoes, no neck, head about half the height, warm rim light always, bold outlines) is REPLACED completely by this design (Salman, 2026-10-29). Removed on purpose: face plate and rim ring, glossy black body, mitten fists, no-neck, chibi proportions, bold outlines. Added: neck, fingers, wristband, backpack, sneaker detail, 13 spec expressions, backpack secondary motion.
Decisions the brain took where the spec and older rules met (Salman may overrule; logged as H1-H4 in ITERATION-LOG.md):
- H1 Rim light: spec says "subtle rim light when appropriate" while the earlier requirement said keep rim light. Taken: rim stays a default but subtle (0.3-0.7), droppable only with a motivated reason.
- H2 Outlines: old "bold outlines" rule dropped (spec forbids thick outlines).
- H3 Wet weather (proposal F3): droplets on a "glossy head" no longer fits (spec: head must not look wet). Needs Salman's say: weather as a light, temporary effect layer on a satin head, or none.
- H4 Eyelids and eye catchlight side: implementation choices taken (section 4), simplest consistent with the spec.

## 12. FILES
Spec: CHARACTER-SPEC-v2.md. Build/replace procedure: CHARACTER-IMPLEMENTATION-PROTOCOL-v1.md. Movement: PERFORMANCE-LAYER-v1.md. Camera: CAMERA-SHOTS-LIBRARY-v1.md. Light and plates: WORLD-PROMPT-WRITER-v1.md, EFFECTS-FOR-FEEL-LIBRARY-v1.md.
