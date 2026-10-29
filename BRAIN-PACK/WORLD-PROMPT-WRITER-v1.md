PROGRESS: complete v1 (sections 1-12). Next: Salman stress-test feedback.
# WORLD PROMPT WRITER v1 (batch B2, 2026-10-28)
Job: for every shot the brain decides what WORLD the shot lives in, then writes the prompt Salman pastes into the image AI, then checks the picture he sends back. Worlds are STILL 3D-rendered images, deep focus (no blur), no letterbox, no character. The brain adds depth map, blur, bokeh, glow, parallax, grain, letterbox, and the real-3D character later.
Inputs: the beat text (what happens, emotion), the shot code from the camera library (B3), CHARACTER-BRAIN-v2.md, IMAGE-PROMPTS-v2.md, look-target/ stills.
Outputs: (1) a prompt block, (2) a Light Card, (3) a Plate Registry entry saved to the video's state file.

## 1. THE FIVE THINGS EVERY PLATE MUST GIVE THE BRAIN
1. A believable 3D place with clear near / middle / far layers (so the depth map is clean).
2. One dominant light source whose direction and colour are known (so the character's lights and shadow match).
3. An open ground area where the character can stand (a clear floor patch, road, field).
4. A known camera height and horizon (so the character's size is correct anywhere on the ground).
5. Premium render quality with a warm glow: bloom around lights, rim glow on edges, visible light rays where fitting.

## 2. WORLD BIBLE (per location) AND PLATE REGISTRY (per video)
World Bible = ONE locked paragraph describing a place in fixed words: architecture/style, materials, key objects and their positions, time of day, weather, light direction, light colour, palette feeling, mood. The first plate of a place is written from it; EVERY later angle of that place pastes the same paragraph verbatim plus the new camera line. Never paraphrase it. This is how places stay consistent.
Plate Registry (saved in the video state file as JSON lines, so a usage limit never loses it):
{"plate":"P03","place":"rain-street","angle":"low-wide","shot":"W","camera_height":"low 0.5m","horizon_pct":42,"light":"key from right-back, 2 o'clock, high, warm gold, hard glow","fill":"cool blue ambient","ground":{"x_pct":[30,70],"y_pct":[62,92],"reflective":"strong"},"foreground_objects":["lamp post left"],"atmosphere":"wet surfaces; rain streaks animated later","bible":"B-rain-street","file":"plate_P03.png","status":"prompted|received|checked|approved"}
Status flow: prompted -> received (Salman sent the image) -> checked (brain verified, Light Card filled from the real image) -> approved.

## 3. CHOOSING THE WORLD FROM THE STORY (dynamic, never from a fixed menu)
Ask in order:
1. What is the beat's feeling in one word (awe, dread, loneliness, joy, tension, wonder, relief, shock, calm)?
2. What is the TRUE place the script implies (a stadium, a bedroom, a lab, a street, a planet)? Real places feel real: keep them believable even if the story is a what-if.
3. Time of day and weather that carry the feeling (dawn = hope or loneliness, harsh noon = exposure, rain night = melancholy and wonder, fog = unease, golden hour = warmth, storm = threat, neon night = energy, overcast = flat reality, interior lamp light = intimacy).
4. Scale: how big is the place relative to him (tiny in a huge stadium = loneliness; tight room = pressure).
5. Palette: INVENT it per beat (rule from DIRECTOR-BRAIN-REQUIREMENTS: dynamic palettes, fictional (our purple/magenta family) or natural, always "our type" = cinematic, rich, with deep darks and a glowing accent). Describe it as a feeling in the prompt ("warm gold against deep blue shadows"), not as a list of hex codes. The brain keeps a per-video palette note so related beats echo each other and big moments contrast.
6. Variety check: do not reuse the same time-of-day + light + palette for three beats in a row unless the story asks; check the Plate Registry.
Salman said: do not name colours in prompts for the image AI; let the AI choose. Keep that: write mood, light direction and quality words; the AI picks colours. The brain still records the colours it actually got in the Light Card.

## 4. LIGHTING RECIPES (pick one per plate, then state it in the prompt)
Each recipe = light direction, quality, atmosphere, and how the character's rim light must match. Rim strength scale: weak about 0.3, strong at most about 0.7 (the spec wants a subtle rim; CHARACTER-BRAIN-v2 section 7).
| recipe | prompt words (direction + quality) | rim on character | good for |
|---|---|---|---|
| Backlit sunset | low sun behind the scene on the right, long soft shadows toward the camera, glowing haze, lens bloom | strong warm rim on right/top edges | loneliness, hope, endings |
| Rain night neon | wet ground reflecting lights, glowing signs, cool ambient, one warm dominant source on the right | warm rim from sign, cool rim from other side | wonder, melancholy, tension |
| Window light interior | one large window light from the side, dust floating in the beam, deep soft shadows | bright rim on window side | intimacy, thought, reveals |
| Overcast soft | big soft diffuse sky light from above, gentle shadows, muted glow | weak soft rim | calm, reality, awe at scale |
| Harsh noon | hard sun overhead, short sharp shadows, bright bounce from the ground | thin hard top rim | shock, exposure, heat |
| Cold fluorescent | flat cool overhead light, hard edges, faint hum of glow on glossy surfaces | cool thin rim | labs, offices, unease |
| Moonlight / night calm | one soft cool light from above behind, deep darks, faint warm accent far away | cool silver rim | quiet, dread, secrecy |
| Fire / candle | small warm flickering source near him, deep dark around, orange glow on surfaces | strong warm rim from the flame side | danger, intimacy |
| Storm / dramatic | hard shaft of light through gaps in dark clouds, strong contrast | bright sliver rim | threat, climax |
| Fantasy / impossible | glowing impossible source (portal, planet, energy), colour not from nature | rim takes the source colour | what-if wonder |
Always: ONE dominant source. A second weaker fill is allowed. Never flat ambient-only light (looks cheap) and never three equal sources (confuses the character's lighting).

## 5. PREMIUM RENDER AND GLOW WORDS (use in every plate prompt)
Quality block: "high-end 3D animated feature-film render, physically based materials, global illumination, ray-traced reflections, volumetric light, subtle film grain, rich micro-detail on surfaces". 
Glow block: "warm glowing light, soft bloom around bright lights, gentle halation, glowing rim light on edges, visible light rays through haze, floating dust particles" (adapt the temperature to the recipe).
Focus block (always): "everything in sharp focus from the nearest object to the farthest background, deep focus, no depth of field, no bokeh, no motion blur, no letterbox bars, no black bars, 16:9 widescreen landscape".
Exclusion block (always): "no people, no characters, no figures, no text, no logos, no watermark".
Why: sharp plates give the clean depth map; the brain then builds real camera blur, so closer shots get stronger blur and it can rack focus.

## 6. CHARACTER-READY PLATE RULES
- Ground area: ask for "an open, clear, level ground area in the [left third / middle third / right third] where a small figure can stand, with nothing standing there". Pick the third from the composition the shot needs (thirds rule; leading space in front of his gaze).
- Camera height, tilt and horizon: state BOTH the camera height ("camera very low near the ground", "eye-level", "high above") and the tilt ("level", "tilted slightly up", "tilted down"). The horizon row follows the TILT, not the height: level = horizon near the middle of the frame, tilted down = horizon high in the frame, tilted up = horizon low. Height decides how big things are relative to the horizon (scale formula below). The brain records horizon_pct from the received image.
- Scale formula (so he is the right size anywhere on the ground): figure height in pixels = (foot_y - horizon_y) x (character_height / camera_height). Use character_height 1.0 unit and camera_height in the same unit (low 0.5, eye 1.6, high 4.0, aerial 20). Foot_y = pixel row of his feet. So a figure standing nearer the camera (lower in frame) is bigger, and one on the horizon is tiny.
- Perspective match: his shoes touch the ground plane; shadow direction follows the Light Card; reflections only if the ground is reflective.
- Do not put important objects where he will stand.
- Occlusion: list foreground objects that can pass in front of him (lamp post, plants, railing); the brain splits these into a near layer using the depth map.

## 7. DEPTH-FRIENDLY RULES (so the depth map and parallax look clean)
Ask for: clear separate layers (near objects, mid objects, far backdrop), solid foreground objects with clean edges, a natural cinematic lens (about 35mm look, no fisheye, no extreme wide distortion), ground that visibly recedes to a horizon, atmospheric haze that grows with distance.
Avoid: large mirrors or glass walls that fool depth, thin foreground objects (wires, fences, grass blades close to camera) that tear under parallax, tilted horizon (tilt is applied later in Remotion so the perspective math stays valid), heavy fog that hides all layers, baked-in blur or bokeh, motion streaks.
Reflective floors are fine (wet street, polished floor): the depth map reads them as floor; the character reflection is added by the brain.

## 8. MASTER PROMPT TEMPLATE (the brain fills the slots)
[QUALITY BLOCK]. A 3D-rendered cinematic world, 16:9 widescreen landscape: [WORLD BIBLE paragraph, verbatim]. Camera: [shot size], [angle], [camera height], natural cinematic lens. Light: [dominant light recipe words, with direction in plain words]. [GLOW BLOCK]. Composition: [thirds / leading space]; [GROUND AREA sentence]. Foreground: [near objects]. Background life: [static small details]. Surfaces: [wet / dusty / clean]. [FOCUS BLOCK]. [EXCLUSION BLOCK]. Choose the colour palette yourself to match a feeling of [one-word feeling].
Rules:
- Every image prompt contains the 16:9 widescreen instruction (standing rule).
- Most important content first: place + camera, then light, then details.
- No colours named. Mood and light words only.
- Falling rain, dust, steam, birds, flickering lights are ANIMATED later in Remotion so they move and can pass in front of him. Default: ask for wet surfaces and glowing haze but "no falling rain streaks". Only for a still, non-moving shot may the brain allow baked particles.
- Keep prompts to about 120-200 words; the image AI follows short clear sentences better than long lists.
- The prompt block shown to Salman is plain text he can paste, plus one line telling him what to attach (reference plate) and what to name the file.

## 9. SAME-PLACE NEW ANGLES (by shot code from the camera library)
Template: "Same location as the attached reference image (plate [ID]): identical architecture, objects, materials, time of day, weather and palette. The light source stays in the same place in the world. New camera: [CAMERA LINE]. [FOCUS BLOCK] [EXCLUSION BLOCK] Leave open ground where the character can stand." (paste the World Bible paragraph too).
World compass rule: store the light in WORLD terms ("key light from the north-east, high") and give every plate a camera facing ("camera faces south-west"). The light's position relative to the camera for any new angle is then calculated, not guessed (a reverse angle puts a backlight in front, a side move puts it to the side). Update the Light Card for each plate.
| code | CAMERA LINE |
|---|---|
| W wide | wide establishing view, camera at [height], showing the whole place, small open ground area |
| M medium | medium view of the spot where the figure will stand, camera at [height], place visible behind |
| C close | tight view, distant background only, open space at the [left/right] third where a large head and shoulders will go |
| X extreme face | background only, as it would sit behind a face in extreme close-up: soft shapes of the place, light sources visible as bright points |
| O/H object or hand | extreme close detail of [object], rich surface texture, a hint of the place behind |
| D top-down | camera looking straight down at the ground from above |
| E empty plate | the place with nothing in it, no space reserved |
| L low angle | camera on the ground looking up, tall structures towering, dramatic perspective |
| V high angle | camera high above looking down at an angle over the place |
| S scale contrast | an enormous [thing] towering over a small open ground area |
| F foreground frame | a large solid object very close to the camera at the [left/right] edge framing the scene |
| R frame-in-frame | the scene seen through a doorway / window / arch in the foreground |
| P in-world POV | view from eye height as if seen through the character's eyes, no hands shown |
| K backlit silhouette | the strongest light source directly behind the open ground area, glowing haze, ground area in shadow |
| Z dutch | NOT requested from the image AI; tilt is applied later |
| reverse angle | the same place seen from the opposite side, 180 degrees turned |
| o/t over-shoulder, two-shot | background only; characters are placed in 3D by the brain |
| U UI/diagram, T text, B black | not plates |
Travelling wide shots and fly shots: follow FLY-SHOTS-3D-v1.md (needs a deep plate or several layered plates).

## 10. BAKED IN THE PLATE VS ANIMATED LATER
| baked into the image | added later by the brain |
|---|---|
| surfaces, wetness, reflections, glowing signs and windows, haze, god-rays, light and shadow, small static background details | blur and bokeh from the depth map, camera moves and parallax, rain streaks, drifting dust, steam, birds, flicker, passers-by that move, the character and his shadow and reflection, bloom and halation strength, grain, colour grade, letterbox bars |

## 11. WHEN SALMAN SENDS A PLATE: CHECK IT (plain-language verdict)
Check list:
1. Format: 16:9? No black bars? No text or logos? No people? Nothing blurred or shallow-focus?
2. Light: where is the dominant source (direction, height)? Colour? Matches the prompt? Fill present?
3. Horizon row (percent from top). Camera height looks like what was asked?
4. Ground area: open? Where (left/centre/right, y range)? Reflective?
5. Layers: near / mid / far readable? Any thin foreground clutter or glass that will break parallax?
6. Colours actually got: 3 dominant + 1 accent (hex), brightness range, any pure-black or clipped areas.
7. Consistency with the World Bible and previous plates of the same place.
Verdict format sent to Salman: "PLATE P03: OK" or "PLATE P03: REDO because [one plain reason], change the prompt by [one line]". Then the Light Card is written into the Plate Registry and status set to checked.
Redo rule: change only the wrong thing; keep the rest of the prompt identical.

## 12. WORKED EXAMPLES (to be used as stress-test cases)
Example A: tiny figure in an empty stadium at dawn (like look-target stadium).
Prompt: High-end 3D animated feature-film render, physically based materials, global illumination, volumetric light, subtle film grain. A 3D-rendered cinematic world, 16:9 widescreen landscape: an enormous empty sports stadium at sunrise, rows of empty seats curving around a vast worn concrete arena floor, a huge dark scoreboard on the right, city skyline far behind the rim. Camera: wide establishing view from low height at the edge of the seats, natural cinematic lens. Light: the low sun on the horizon at the back right, long soft shadows reaching toward the camera, glowing haze and lens bloom, warm glowing light with gentle halation and a glowing rim on edges. Composition: sun on the right third, an open clear level ground area in the middle third of the arena floor where a small figure can stand. Foreground: the backs of a few seats very close to the camera on the left. Surfaces: dry cracked concrete catching the glow. Everything in sharp focus from the nearest object to the farthest background, deep focus, no depth of field, no bokeh, no motion blur, no letterbox bars. No people, no characters, no text, no logos, no watermark. Choose the colour palette yourself to match a feeling of loneliness and quiet hope.
Light Card: key = low sun behind-right, warm, hard-glow; ground = middle third, y 62-90 percent; horizon about 62 percent; reflective = weak; foreground = seat backs left; character rim = strong warm from the right.
Example B: rain night street under a glowing sign (look-target rain street). Recipe: Rain night neon; dominant warm sign on the right wall, cool ambient; wet reflective ground; lamp post foreground left; no falling rain streaks (animated later); ground area centre-left.
Example C: quiet cafe interior at morning (look-target close-up background): Window light interior; large window left, dust in the beam, desks with cups and plants, warm glow; plate for X: background shapes only with bright window points.
Example D (what-if impossible): a giant ringed planet filling the sky above a calm desert at dusk. Recipe: Fantasy/impossible; source = the planet's glow; scale contrast S; ground area centre; the brain lets the planet colour drive his rim light.
