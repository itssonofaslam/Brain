# IMAGE PROMPTS v2 (2026-10-28)
Look target = look-target/ (3 stills). Canonical character = the close-up (white round face, thick black rim, glossy black eyes with highlight, thin brows, small mouth, thin black limbs). Plates are made WITHOUT blur and WITHOUT letterbox: the brain adds depth map, blur, bokeh, glow and bars in Remotion.

## 1. CHARACTER SHEET (use the close-up image as the attached reference)
Use the attached image as the exact character reference. Extract only the stickman and create a clean 16:9 character design sheet of this same character, without redesigning it. Keep identical: the perfectly round head (a true circle), the smooth glossy white face with its thick black outer rim, the glossy black eyes with a bright highlight, the thin curved eyebrows, the small mouth, the fine surface texture of the face, the soft glowing rim light. Since the reference shows only the head and shoulders, build the body to match it: thin black tube-like limbs and a thin black torso, round hands, round feet, same bold outlines and same glossy material. Show front view, three-quarter view, side view and back view at full body, then five expressions (calm, afraid, amazed, sad, determined) as head close-ups, then four poses (standing, walking, running, arms raised). Plain neutral studio backdrop, soft cinematic lighting with a warm glowing rim light, real 3D render quality, the character identical in every view. No text, no labels.

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
