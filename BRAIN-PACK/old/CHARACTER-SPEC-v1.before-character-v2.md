# CHARACTER SPEC v1 (2026-10-28) - from Salman's character sheet (look-target/character-sheet-v1.png)
Status: design = LOCKED unless Salman changes it. Proportions "by eye" from the sheet; refine when the 3D model is built.

## Head (the signature)
- Perfect round head. It is a COIN/BUTTON design: a black glossy sphere with a cream face plate set into the front, ringed by a thick glossy black rim. Side view = black dome with the face plate on the front edge; back view = plain black glossy sphere.
- Face plate: warm cream/off-white, smooth, very fine surface grain (leather-like). Keep the plate slightly inset so the black rim catches a glowing edge light.
- Rim thickness about 5-7 percent of head diameter.
- Head is about half the total height (chibi proportion, head about as tall as the whole body below it).

## Face
- Eyes: tall glossy black ovals with one bright highlight at the upper right of each eye. Each eye about 15 percent of face width and 24 percent of face height, centres about 43 percent of face width apart, sitting a little above the middle.
- Brows: thin curved dark lines above the eyes; the angle carries the emotion.
- Mouth: small simple dark mark, low on the face; shape changes with emotion (small o, wobbly, round o, down curve, flat line).
- Expressions seen on the sheet: calm, afraid, amazed, sad, determined.

## Body
- Glossy black, soft rounded tubes: short torso, thick arms with round mitten fists (no fingers), thick legs, big round shoes. All simple, no clothing seams.
- Material: glossy black with a warm rim light on the top and side edges; face plate is matte-soft.
- Walk and run poses are loose and bouncy; arms raised pose = fists up.

## Build notes for the 3D model (Three.js/Remotion)
- Head: black sphere + inset cream disc (slightly domed) + torus rim; eyes/brows/mouth as separate meshes so the brain can animate them (blink, brow raise, mouth shapes, eye darts).
- When the head turns, the face plate turns with it and the black dome shows (use this for micro-movements).
- Limbs: capsules with smooth joints; hands = spheres with a slight fist shape; feet = rounded ellipsoids.
- Material for black parts: clearcoat/gloss + environment reflection from the world plate; warm rim light always on.

## Resolved by Salman (2026-10-28 08:08)
1. Chunky chibi body from the sheet is RIGHT.
2. Follow the character sheet only. The all-black head from the rain-street still is NOT used. Face plate is always cream with black rim.
Design is final: CHARACTER LOCKED.
