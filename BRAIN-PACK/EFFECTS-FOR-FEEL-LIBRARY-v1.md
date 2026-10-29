PROGRESS: complete v1 (sections 1-13). Cinematic-intelligence upgrade applied 2026-10-29 (sections 1, 4, 11, 13; original in old/). Next: Salman stress-test feedback.
# EFFECTS-FOR-FEEL LIBRARY v1 (batch B4, 2026-10-28)
Purpose: everything the director adds ON TOP of the plate and the character to create feel, realism and premium polish. The brain reasons per beat which effects to use, how strong, and when to stop. Principle (from FEEL-DEVICES-v1 and DEVICE-INVENTION-v2): effects are punctuation, not decoration; each effect needs a feeling it serves.
Numbers marked START are starting values to tune in stress tests (1080p).
Related: lens blur and handheld = CAMERA-SHOTS-LIBRARY-v1 sections 7-8. Feel devices (colour switch etc.) = FEEL-DEVICES-v1.md. Device invention from script = DEVICE-INVENTION-v2.md. Plates and light = WORLD-PROMPT-WRITER-v1.md. Character look = CHARACTER-BRAIN-v2.md.

## 1. EFFECT BUDGET AND ORDER OF OPERATIONS
Per shot choose: 1 grade state, 1 glow level, 1 atmosphere layer, 1-3 life elements (background), 0-1 foreground object, 0-1 feel device. More than that looks busy; fewer than that looks flat (except diagram/text shots). Every effect has a defined target, a feeling it serves and start and end frames (CINEMATIC-INTELLIGENCE section 1 purpose test); never add an effect just because it exists, and never describe an effect the renderer cannot do reliably: use a supported alternative or leave it out.
Render order (back to front, so everything sits in the same world):
1. Plate far layer (with depth blur and bokeh)
2. Background life (people, traffic, birds), blurred by their depth
3. Plate mid layer, atmosphere layer behind the character (haze, rain far, dust far)
4. Ground reflections and the character's shadow
5. Character (real 3D, lit by the Light Card) and his reflection
6. Atmosphere in front (rain near, dust near, steam)
7. Foreground objects (plate near layer or separate), heavily blurred when very close
8. Light effects (bloom, halation, rays, flares) over everything
9. Colour grade, vignette, grain
10. Text and HUD (own treatment, section 7)
11. Letterbox bars (always last)
Render cost tiers (laptop/Colab planning): heavy = depth blur and bokeh, volumetric rays, many particles; medium = bloom, reflections, motion blur; light = grade, vignette, grain, bars. If time is short, reduce heavy effects first.

## 2. COLOUR REASONING (dynamic palettes, "our type")
- Look target "our type": cinematic, rich deep darks, a glowing warm or cool accent, complementary contrast (warm light against cool shadow, or the reverse), saturated but not neon-flat, always some glow.
- Palette choice per beat: from the feeling (WORLD-PROMPT-WRITER section 3), natural OR fictional. Fictional palettes (our purple/magenta family, impossible greens, planet colours) are allowed for what-if worlds; natural palettes for real places. Do not mix families in one scene unless the story is about the clash.
- Per-video palette note (saved in the video state file): home palette (most scenes), 2-3 accent worlds, one "special" colour reserved for the biggest moment. Related beats echo each other; the big moment breaks the pattern.
- Colour roles: light colour (rim and key), shadow colour, accent (props, signs, the thing that matters), the character's colours stay fixed: ivory head and hands, charcoal body, turquoise left wristband, black daypack, black sneakers with off-white soles (never recoloured, only lit).
- Colour as story: warm = safe/human/hope; cool = alone/technical/threat; red/orange accent = danger or urgency; green-teal = unease or science; gold = wonder or reward; desaturation = numbness, slowed time; saturation burst = realisation. Switch rules in FEEL-DEVICES-v1 section A and B (snap 3-5 f, slow 14-25 f).
- Grade states (START): neutral = as the plate; warm push = +8-12% warmth, highlights toward gold; cool push = shadows toward blue/teal; desaturate = -25-40% saturation; contrast lift = S-curve; each state has numbers saved with its name so it can be restored.
- Repetition check: same palette and same light for 3 beats in a row only if the story stays in one moment.
- Never grade the character into a new colour: rim light, reflections and shadow only.

## 3. GLOW AND LIGHT EFFECTS (the "glowy look" of the close-up)
| effect | what it does | START values |
|---|---|---|
| bloom | soft glow around bright areas | threshold = brightest 5-8% of pixels, radius 40-90 px, strength 0.25-0.5; stronger for sunset, neon, windows |
| halation | thin warm/red halo bleeding at high-contrast edges | 0.15-0.3 strength, 6-14 px, warm tinted |
| rim glow on character | thin bright edge on the head, shoulders, arms, sneaker tops; keeps the black limbs readable | from Light Card, SUBTLE 0.3-0.7 (CHARACTER-BRAIN-v2 section 7); width 2-5 px at medium shot; may be 0 only when the light motivates it |
| light wrap | background light colour bleeding a little over the character's edges | 3-6 px, 15-30% of the background colour |
| light shafts / god-rays | beams through haze or windows | opacity 0.1-0.3, slow drift, behind and in front of him |
| lens flare | small streaks on the brightest source only | tiny; use only when the source is in frame; never on the face |
| dust motes | tiny particles catching light | 20-80 particles, depth-split, drift 5-20 px/s, glowing in beams only |
| flicker | light source brightness variation (neon, candle, fluorescent) | +-5-15% at 6-12 Hz, applied to the character's key light too so he flickers with the world |
| vignette | darkens the corners | 8-18% at edges |
| film grain | fine texture over everything including character | amplitude 2-4%, size 1-1.5 px, animated per frame |
Premium rule: glow must come from a visible source or a recognised light recipe; do not glow everything evenly.

## 4. ATMOSPHERE AND PARTICLES (animated in Remotion, depth-layered)
- Rain: far streaks (thin, many, faint), mid streaks, near streaks (few, bright, blurred); splash rings on the ground; reflections move with them; wetness already in the plate. Rain falls in front of AND behind the character, and catches the rim light.
- Haze/fog: 2-3 depth layers of soft noise, slow drift, tinted by the key light; thicker at distance.
- Dust/pollen/ash/snow/embers/leaves: per-mood particle sets; fall or float with a believable wind direction shared across the scene.
- Steam, smoke, breath clouds: soft noise sprites rising; colour from the light.
- Birds/insects/paper/trash blowing: occasional life elements.
- Wind: one wind vector per scene moves all of the above and cloth-like props the same way.
- Heat shimmer: tiny distortion above hot ground in noon shots.
Rules: particles obey depth (near ones blurred and larger); never uniform density; they respond to light (only lit particles glow).
Environment responds to action when it is motivated and visible (dust settles after an impact, curtains flutter in a breeze, foliage moves as he passes, a light changes after a switch, a monitor lights a nearby surface, rain affects a wet floor), and stays coherent with the world and the Light Card. Do not add environmental activity the described world does not have if it changes the tone or implies an event the script did not give; do not fill every shot with particles and motion.

## 5. BACKGROUND LIFE (the world must feel alive)
Rule (Salman): background life such as a stranger passing, slightly blurred. Each wide/medium shot gets 1-3 life elements chosen to fit the place and keep the main subject clear.
Catalogue:
- People: passers-by silhouettes on a mid or far depth layer, walking at plausible speed (scale by the Light Card scale formula so their size matches distance), a different outfit shape per person, one carrying an umbrella in rain, a cyclist, a person on the phone. Same stickman design language (sphere head, slim body) but slightly blurred and darker, head in shadow. Never the same walk cycle twice in a row. Looks come from CHARACTER-CASTING-v1.md section 6 (tiers, seeded picks from a shared kit library, never the main's kit).
- Vehicles: slow cars with headlights, a bus passing, a train in the distance, bicycles.
- Animals: birds crossing sky, a pigeon on a railing, a dog far away.
- Place motion: flags, curtains, steam from vents, sign flicker, traffic lights changing, elevator doors, screens updating, water ripples, grass bending, flames.
- Light motion: car headlights sweeping across wet floor, a lighthouse sweep, clouds shadow moving, sun glints.
- Crowds (stadium, market): rows of small blurred figures in the stands with occasional movement (wave, flicker of cameras).
Placement: away from the character's face line; slow; lower contrast than the subject; their blur follows depth. In extreme close-ups life appears only as moving bokeh blobs and soft shapes.
No life in diagram (U), text (T) and macro (O/H) shots unless the story demands it.

## 6. FOREGROUND OBJECTS (motivated depth)
Rule (Salman): motivated blurred foreground objects (e.g. wooden pole). Motivated = the place would plausibly have it AND it serves the shot (frames him, hides a cut, adds depth, creates voyeurism, adds scale).
Catalogue by place: lamp post, railing, plant leaves, bar/cage lines, doorway edge, curtain, glass with droplets, chair back, fence, branch, steam, rubbish bin, bike rack, shelves, a person's shoulder or head (over-the-shoulder).
Rules: sits at the left or right edge, 8-25% of frame; strongly blurred (extreme-close blur values); slightly darker than the subject; may drift slowly with the camera (parallax); never covers the face or the key prop; remove it when it competes. Max one per shot (two for tense framing).

## 7. TEXT AND ON-SCREEN WORDS (style by feeling; the WORDS come from the script brain)
Types: title card, label (names a thing), caption (one idea), number/counter (stakes), in-world text (sign, screen, wall writing).
- Never ask the image AI to draw text in a plate (it misspells). All text is added in Remotion, as a 3D layer in the world (sits on a surface in perspective, obeys depth blur and focus) or as a screen layer (clean, always sharp).
- Font family by feeling:
  - clean modern sans: neutral, technical, explanation
  - tall condensed bold sans: urgency, impact, countdowns
  - elegant serif: awe, history, emotion, endings
  - handwritten: intimate, personal, memory
  - monospace: data, surveillance, system messages
  - rounded friendly sans: humour, lightness
  The brain picks one family per video as the home font and may switch for special moments; choose from fonts that are free and available in Remotion (font check is an open test).
- Colour: sample the plate area behind the text; choose light or dark text for contrast (minimum contrast ratio 4.5:1), take the accent colour from the video's palette; add a soft glow on dark backgrounds; never pure white on pure black unless it is the "stark" moment.
- Size (START): title 6-9% of frame height, label 3.5-5%, caption about 4%, counters 8-12%. Maximum about 7 words per card; one idea.
- Placement: inside the safe area between the letterbox bars, on a third line, away from the character's face and eyes; follow look room; do not cover the key prop; in-world text sits where a real sign would.
- Timing: appears on the spoken word from the timing file; holds long enough to read (about 3 words per second plus 0.4 s); exits with a 6-10 frame fade.
- Motion: fade, draw-on (14-25 f, ease-in-out), small slide up to 20 px (ease-out). No bounce, no overshoot (measured: none).
- Emphasis words: colour shift or glow pulse, not size jumps.

## 8. UNDERSTANDABLE WITH THE SOUND OFF (muted test)
Every beat must read without audio. Tools: expression and posture, a prop close-up, a number or icon, an arrow or highlight, a small inset, a symbolic change in light or colour, minimal text. Test: write one line per shot of what a muted viewer would conclude; if it differs from the intended meaning, add a cue. Do not repeat the narration word for word on screen; show what the narration cannot.

## 9. DIAGRAMS AND UI SHOTS IN OUR LOOK (the brain decides when, Salman: dynamic)
When the script explains how or why: choose between (a) glowing line diagram floating in 3D over a blurred plate, (b) a glass or holographic panel in the world, (c) a physical diagram in the place (blueprint, whiteboard, map) added as a 3D plane with perspective. One idea per panel. Strokes at least 4 px at 1080p, text at least 4% of frame height, accent colour from the palette, soft glow. Draw-on 14-25 frames, ease-in-out; punch-in (push) on 20% of such shots (measured). No handheld on diagrams. Keep the character in the world when possible (he points, looks) so diagrams do not feel like a different video.

## 10. SHADOWS, REFLECTIONS AND INTERACTIVE LIGHT (so he belongs in the picture, not slapped on)
- Shadow: direction from the Light Card; softness from the light size (hard sun = sharp, overcast = only a soft contact shadow); length from light height. Contact shadow under shoes always. A second, fainter shadow for a secondary light.
- Reflection on glossy ground: mirrored copy anchored at the shoes, sharp at contact and increasingly blurred with distance, dimmer than the figure, stronger at grazing angles (Fresnel), distorted by ripples or rain.
- Light response on him (no chrome): soft broad highlights from the real bright sources of the plate (signs, windows, sun) on the satin head and the wristband, a catchlight in the eyes, only gentle sheen on the matte charcoal limbs and backpack; moving lights sweep across him.
- Interactive light: walking through a shaft brightens him; stepping into shade darkens the rim; a neon sign tints the rim and the side of the head; flicker follows the source; a lit phone screen or flame casts coloured light on his face.
- Light wrap and ambient occlusion where he touches the ground; same haze and grain on him as on the world.
- Check: put him in the plate with all effects off, then on; if he still looks pasted, a shadow, reflection or light match is wrong.

## 11. MOTION EFFECTS AND PHYSICS
- Motion blur: 180 degree shutter on fast movers only: blur length about half of the per-frame displacement; never on slow moves; not a permanent smear.
- Slow motion / speed ramp: only when emphasis, perception or story rhythm calls for it (the references use it for approach and suspense), never on every impact. Write start frame, end frame, speed curve and mark the change as a sound hook so sound can follow the time change.
- Shake and impact response: only for a real event on screen, not for every dramatic line (CAMERA-SHOTS-LIBRARY section 8 for values).
- Vignette and lens distortion: only when the style and the moment justify them; keep faces undistorted. Bloom and glow stay restrained enough to protect detail. Colour and light shifts support the story and stay consistent across adjacent shots.
- Dust puffs on heavy footsteps and landings: 3-6 small soft puffs, 10-18 frames, colour from the ground and light.
- Impact: 1-2 frame bright burst, then a 6-10 frame ring and camera impulse (CAMERA-SHOTS-LIBRARY section 8).
- Falling and thrown things: gravity with slight drag and a small damped bounce (no cartoon bounce); heavier objects slower to start and land harder.
- Walking and running: heel strike, small vertical bob, weight transfer (detail in PERFORMANCE-LAYER, B5).
- No cartoon speed lines, no squash-and-stretch, no overshoot (measured: none in 213 runs). Motion eases in and out.

## 12. TRANSITION EFFECTS (numbers; the choice is in CAMERA-SHOTS-LIBRARY section 10)
Dissolve 6-14 f; flash 1-2 f (bloom x3 over 4 f for a white-out; 3.3 s only for the big portal moment); black strobe 1-2 f; whip pan 6-10 f with 40-60 px directional blur; blur-into-blur 8-12 f up to 30 px; fade to black 12-24 f at endings.

## 13. INVENTING NEW EFFECTS, GUARDRAILS, QA
- Invention: run the FEEL-DEVICES-v1 protocol (feeling, lever, state A/B, switch style, restore, repetition check). Label any new device "proposal" until Salman approves it in a stress test.
- Guardrails: motivated by the story; premium and realistic at the level of the look target (no clip-art stickers, no random lens flare); one new device at a time; the same device no more than 3 times in 60 s; if unsure, do less.
- QA checklist (stress tests): Does each effect have a target, a timeline and a story reason (would the story be less clear without it)? Does glow come from a visible source? Do shadows and reflections match the Light Card? Do particles obey depth? Is life in the background plausible and not distracting? Is any foreground object motivated? Does text read clearly, in the right style, away from the face? Is the story clear when muted? Is the order of operations respected (bars last)? Is anything heavy that could be lighter?
- Links: FEEL-DEVICES-v1.md, DEVICE-INVENTION-v2.md, CAMERA-SHOTS-LIBRARY-v1.md, WORLD-PROMPT-WRITER-v1.md, CHARACTER-BRAIN-v2.md, DIRECTOR-BRAIN-REQUIREMENTS.md.
