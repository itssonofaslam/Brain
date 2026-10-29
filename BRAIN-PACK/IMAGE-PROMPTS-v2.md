# IMAGE PROMPTS v2 (2026-10-28)
Canonical character = the real 3D stickman of CHARACTER-SPEC-v2.md (built in Three.js, NOT generated as an image; the old look-target character with the face plate is retired 2026-10-29). The look-target stills now serve only as a WORLD/lighting look reference. Plates are made WITHOUT blur and WITHOUT letterbox: the brain adds depth map, blur, bokeh, glow and bars in Remotion.

## 1. CHARACTER SHEET (RETIRED prompt, 2026-10-29)
The old prompt described the retired chibi coin-head (white face, thick black rim, bold outlines) and must NOT be used. The character is no longer picked from an image: it is the real 3D model defined by CHARACTER-SPEC-v2.md. If a reference sheet image is ever wanted, write it from the spec text only, without redesigning: a clean 16:9 turnaround of one 3D stickman, plain neutral backdrop, soft studio light: smooth warm ivory spherical head with two tall glossy black oval eyes, thin dark eyebrows and a small mouth (no nose, ears or hair), thin charcoal-black neck and slim torso, long thin charcoal arms and legs, small ivory hands with thumb and four fingers, one turquoise wristband on the character's LEFT wrist, compact black backpack, chunky black sneakers with thick off-white soles and white laces; front, three-quarter, side and back views, identical model in every view, no thick outlines, no text.

## 2. WORLD PLATE (no character, no blur)
A 3D-rendered cinematic world, 16:9 widescreen landscape, high-end animated-film quality. [WORLD: describe place, time, weather]. Everything in sharp focus from the nearest object to the farthest background: deep focus, no depth of field, no bokeh, no motion blur, no letterbox bars. One dominant, clearly visible light source coming from [direction chosen by the brain], with a warm glowing quality: soft bloom around bright lights, gentle halation, glowing rim light on edges, visible light rays and floating dust or rain where fitting. Realistic perspective with clear foreground, midground and background layers, a few foreground objects close to the camera, and small background details. Leave an open, clear ground area in the middle third of the frame where a small character can stand. No people, no characters, no text. Choose the colour palette yourself to match the emotion of the moment, cohesive and cinematic.

## 3. SAME PLACE, NEW ANGLE
Same location as the attached reference image: identical architecture, objects, time of day, weather, light direction and colour palette. New camera: [angle and size chosen by the brain, e.g. low angle close to the ground, closer medium view, over-the-shoulder, top-down]. Everything in sharp focus, no depth of field, no bokeh, no letterbox bars. Leave open ground where the character can stand. No people, no characters, no text.

## 4. LIGHT CARD (the brain fills one per image, from the prompt it wrote, then checks the picture)
light direction (clock position + height), light colour, shadow softness, horizon height (% from top), camera height (low/eye/high), ground area (left/centre/right, how far), reflective ground (yes/no, how strong), atmosphere (rain/haze/dust), foreground objects that can pass in front of the character.

## 5. RULES THE BRAIN MUST FOLLOW
- Parallax budget (anti-stretch): small camera moves only. Push-in up to about 8 percent scale, sideways drift up to about 3 percent of frame width, turn up to about 2 degrees. Anything bigger = cut to a new angle plate (prompt 3), or use a fly-shot method from FLY-SHOTS-3D-v1.md.
- Depth edges are cut, not stretched: split the plate into near / middle / far layers, fill the gap behind each near layer (inpaint), blend edges softly.
- Blur is made from the depth map: closer shot = stronger background blur; rack focus allowed; bright lights turn into bokeh discs.
- Glow is added in Remotion (bloom + halation + rim light) on top of what the picture already has; the character gets the same glow as the world.
- The character is real 3D, lit by the Light Card, with contact shadow, reflection on glossy ground, and the same grain/atmosphere as the plate.
