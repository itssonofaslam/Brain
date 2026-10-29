PROGRESS: sections 1-10 written (complete v1). Next: Salman stress-test feedback.
# CHARACTER BRAIN v1 (2026-10-28)
Source of truth: Salman's character sheet (look-target/character-sheet-v1.png) + close-up (look-target/target-2-face-closeup.png). Numbers measured from the sheet's front view (head diameter D = 168 px, total height 331 px). Accuracy about +/-10 percent: refine when the 3D model exists. CHARACTER IS LOCKED. This file only describes it more exactly and says how the brain uses it.

## 1. INVARIANTS (never change, in any shot)
1. Perfectly round head (true circle from the front, near-spherical in depth).
2. Head = black glossy sphere with a CREAM face plate set into the front, ringed by a thick glossy black rim.
3. Eyes = tall glossy black ovals, each with one bright highlight at the upper right.
4. Thin curved brows, small simple mouth. No nose, no ears, no hair, no pupils inside eyes.
5. Body = glossy near-black soft tubes: short torso, thick arms, round mitten fists, thick legs, big round shoes. No fingers, no clothes seams on the main character.
6. A warm glowing rim light always visible on the top/side edges (strength varies, never zero).
7. Bold outlines come from the black rim and the black body against the lit world; never thin sketchy lines.

## 2. PROPORTIONS (head diameter D = 1.0 head unit)
| part | size |
|---|---|
| total height | 1.97 head units (head about 51 percent of height) |
| torso (shoulder line to crotch) | about 0.41 |
| legs including shoes | about 0.56 |
| torso width | about 0.27 |
| arm (shoulder to fist) | about 0.54, tube thickness about 0.12 |
| fist | about 0.18 across, round, slightly squarish |
| leg tube thickness | about 0.16 each |
| shoe | about 0.31 wide, 0.18 tall, round toe, thick sole look |
| neck | none visible; head sits directly on the shoulders |

## 3. HEAD BUILD (for the 3D model)
- Black sphere, radius R = D/2.
- Face plate: a cream disc on the front, slightly domed like a cabochon, radius about 0.90 R. The black rim is the ring left around it: thickness about 5 percent of D, glossy, with a clearly visible highlight.
- Depth: head is nearly a sphere (depth about 90-95 percent of D). The plate sits flush with the rim at the front.
- Back of head: plain black glossy sphere. No face parts ever on the back.
- Turning: the plate turns with the head. Past about 60 degrees of turn the plate shows as an edge-on disc and the black dome fills the view. At 90 degrees (side view) the plate is a thin front disc on a black dome (see sheet side view). At 180 degrees only black.
- Face parts (eyes, brows, mouth) are separate meshes on the plate so the brain can animate them independently.

## 4. FACE LAYOUT (percent of D; measured from the front view)
- Brows: centre line about 25 percent down from the head top, each about 13 percent of D long, line about 1.5 percent of D thick, gently arched, about 7 percent of D above the eye.
- Eyes: centres about 51 percent down; each eye about 14 percent of D wide and 27 percent of D tall (tall oval); centre-to-centre distance about 39 percent of D, symmetric about the head centre.
- Highlight: one bright round spot about 25 percent of the eye width, at the upper right of each eye, same side on both eyes (light comes from upper right). A faint small second reflection is allowed.
- Mouth: centre about 79 percent down, small: calm shape about 12 percent of D wide and 6 percent tall.
- Eye area gets a faint soft shadow ring (eyes sit slightly into the plate).

## 5. EXPRESSIONS (parameters, so the brain can invent more)
Parameters: brow height, brow angle (inner end up = worried, inner end down = angry), brow arch, eye openness (scale of eye height, 0.85-1.2), eye-highlight shift, eye look direction (eye shifts inside the plate by up to about 6 percent of D), mouth shape, mouth width, head tilt.
Sheet expressions:
| expression | brows | eyes | mouth |
|---|---|---|---|
| calm | gentle arch, level | normal | small soft oval |
| afraid | raised, inner ends up | slightly bigger | wobbly open, uneven |
| amazed | high, strongly arched | wide | round O, bigger |
| sad | inner ends up, lowered | normal to slightly lowered | small downturned curve |
| determined | angled down toward the nose | slightly narrowed | flat thin line |
Inventing more (shy, smug, confused, tired, angry, relieved, crying...): combine the parameters; stay inside the vocabulary: brows + eye openness + mouth shape only. Never add tears, sweat, blush or new face parts unless a scene needs one and it is drawn in the same glossy style.

## 6. JOINTS AND LIMITS
Joints: head (turn, tilt, nod), shoulder x2, elbow x2, hip x2, knee x2, ankle x2 (wrists are fists: only a small rotation). Torso can lean and twist a little.
Limits (keep him cute and solid, no rubber): elbow 0-140 degrees, knee 0-130, shoulder up to straight overhead, head turn to +/-100, nod +/-40, torso lean +/-25. Knees and elbows never bend backwards. Limbs keep constant thickness (no squash and stretch, matches measured references: no overshoot, no bounce). Movement quality rules live in the performance layer (B5).

## 7. MATERIALS AND LIGHT
- Body and rim: glossy near-black, warm tint (about #0a0704), clearcoat, low roughness. It reflects the world: bright spots and colours of the scene show as soft highlights on arms, shoes, head rim. Highlights roll along curves, never flat white blobs.
- Face plate: matte-soft cream with fine leather-like grain. Reference tones: lit about #e5d6c8, mid about #c8af9c, shadow about #998476 (these shift with scene light colour; keep the plate a warm light neutral, never pure white, never grey).
- Rim light: always from the strongest light behind or beside him. Colour = that light's colour (warm gold in sunset/window light, cool blue in rain/night with neon). Thin bright glow on head rim top/side, shoulders and shoe tops. Strength 0.6-1.0.
- Face readability rule: even in dark scenes the plate stays at least about 35 percent brightness so the face can be read; the body may fall into silhouette.
- Contact: soft contact shadow under shoes; on wet or glossy floors add a blurred mirror reflection (dimmer than the real figure).
- Same grain, haze, rain and glow as the world is applied over him last, so he belongs in the picture.

## 8. SCALE BY SHOT SIZE (how big he is in frame, measured from the look-target stills)
| shot | figure height in frame | notes |
|---|---|---|
| tiny wide (stadium still) | about 5 percent | face plate reads as a small light dot; can be silhouette; no face detail |
| wide | 15-25 percent | face parts readable only as dots; show posture |
| medium | 45-60 percent | face readable, rim light visible |
| close | head 55-70 percent of frame height | eyes, brows, mouth clear |
| extreme close | head 85-100 percent (close-up still) | fine plate grain, eye highlights, rim glow, tiny dust glints |
Simplify with distance: far = silhouette plus plate dot; near = full detail. Close-ups need the higher-resolution face detail.

## 9. VIEWS AND ANGLES
- Front: plate and face fully visible, symmetric.
- Three-quarter: plate turned about 35 degrees, far eye closer to the rim, black dome visible on one side.
- Side: thin plate edge in front of the black dome; face parts nearly edge-on; show mood through posture, not the face.
- Back: plain black sphere, plain black back and shoes; mood only through posture.
- Top-down: round black dome with the plate edge peeking; shoes round.
- Low angle: head looks bigger and the plate tilts up; keep rim visible.
Camera angle choices come from the camera library (B3); this file only guarantees the look from each side.

## 10. OTHER CHARACTERS AND CHECKLIST
Other people (doctor, stranger, friend, crowd): same coin-head design language, same glossy body, but different: height, build, plate tint (warm cream, pale cool, tan, dusky), one costume piece in the same glossy/soft style (coat, hat, scarf, glasses as simple shapes), maybe a different eye shape or brow style. Crowd and background people: slightly blurred silhouettes with plate in shadow. Main character is always the only one with the exact sheet design and no extra clothing unless the story changes him.
QA checklist (stress tests):
- Head perfectly round? Plate cream, not white or grey? Rim thick and glossy?
- Eyes tall ovals with upper-right highlight? Brows thin and clear?
- Body glossy near-black, fists round, shoes big and round, no fingers?
- Rim light present and matches the world's light colour? Face still readable?
- Contact shadow and reflection present? Grain/haze applied last?
- Expression readable at this shot size? Proportions unchanged (head about half the height)?
