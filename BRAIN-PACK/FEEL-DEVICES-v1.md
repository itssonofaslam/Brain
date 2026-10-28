# FEEL DEVICES v1 - how the brain INVENTS feel (not just copies) - 2026-10-26
Answer to "can the brain invent things like the colour switch?": YES, only if it is taught the PRINCIPLE behind each device, not the device itself. A device = (feeling it creates) + (a lever on the image/edit) + (trigger moment) + (execution numbers) + (how it is masked/restored). The brain must run the INVENTION PROTOCOL below for every script beat that needs feel.

## A. INVENTION PROTOCOL (run per beat; write the answer in the shot plan)
1. What must the viewer FEEL here? (wonder / dread / relief / awe / loneliness / speed / slowness / pride / loss / humour / surprise)
2. Is this beat about perception (what the character senses), about the world (what is true), or about the audience (what we want them to notice)?
3. Pick 1-2 LEVERS (never more; effects are punctuation): colour grade | saturation | light source/brightness | vignette tightness | camera angle/scale | cut rate (faster/slower) | hold length | frame size (iris/letterbox) | depth of field | sound (implied) | silence | text/HUD | a ghost/echo | a tiny ambient object.
4. Define STATE A (normal) and STATE B (the feel state) in numbers (hex, % saturation, blur px, frame counts).
5. Choose the SWITCH style: snap (3-5 f) = shock/realisation; slow (14-25 f) = mood/time passing; masked (burst/flash/cut hides it) = impact.
6. Choose the RESTORE: usually a burst/cut back to state A at the decisive moment; unresolved = stay in B (loss/dread).
7. Check: is the same device already used 3+ times in 60 s? Then vary lever or stay still. Is it motivated by the story? If not, delete it.
8. Add ONE micro-depth object (fly/dust/bokeh/flicker) that fits the place.

## B. MEASURED DEVICE: PERCEPTION GRADE ("slowed time" colour switch) - ref2
What it is: the SAME shot/layout is shown in two grades. Normal = warm, full-saturation (hero hoodie #d8332f). Perception state = cool + desaturated + darker (hoodie turns pink-grey/mauve #b07a9a, sky grey-blue/navy, floor blue, lights stay bright). It means "the hero's brain is running 10x: world slows, he sees everything". 
Where (measured): ball approach 97.7-98.9 s cool -> BURST at the catch 98.9-99.0 -> warm; tennis 143.4-149.4 s cool -> flash burst 149.5 -> warm at 149.6 (hoodie goes from pink-grey to red); ruler 58.5-64.7 s neutral/grey -> orange warm in 4-5 frames (64.7-65.0) as the result lands (sleeve turns red, sky peach); baseball dusk -> navy at 169.4-169.8 (0.4 s) when the pitch is watched; night walk 75-78 cool -> snap warm at the cut 78.3; flowerpot 80-85.6 cool -> burst 85.8 -> warm; red-light 106-113 cool; gaming 119.8-134 cool -> dissolve.
How: a grade filter on the SCENE layers only (saturation x0.4-0.6, hue toward blue-violet, brightness -15%, vignette +10%); HUD/text stays untouched (the "160 km/h = 0.4 s" label stays cream on top of the navy). Characters are NOT recoloured: the grade does it. Light sources keep glowing (windows/floodlights stay bright) so the image keeps focus points.
Timing: switch to cool = 5-12 frames; back to warm = 4-5 frames and masked by a 1-2 frame radial burst or by a hard cut. Sometimes preceded by a held frame (nothing moves, then it snaps).
Why it feels premium: (1) it is meaning, not decoration: the audience learns the code in 20 s and then reads the hero's mental state from colour alone; (2) the snap-back at the burst is a release (tension -> payoff); (3) the same layout in two colours proves it is the same moment; (4) restraint: HUD and key lights stay stable so it never looks like a filter.
Map of every warm/cool segment of the whole video: ref2-colour-state-map.md (note: long cool blocks like 272-380 s are NIGHT/aftermath lighting, a second meaning = mood; the brain must keep these two meanings separate: "environment light" vs "perception grade").

## C. OTHER MEASURED DEVICES (principle -> recipe)
- SLOW-APPROACH (time dilation): a ball/fist/cable approaches over 24-40 frames in the cool grade while everything else holds. Lever: speed + grade. Recipe: object scale 3% -> 100% ease-in, background frozen except 1-2 px idle.
- DECISIVE-MOMENT BURST: 1-2 frame cream radial burst + ring ripple (6-8 f). Lever: flash. Marks catch/hit/save. Max once per 10-20 s or it becomes noise.
- FACE-FILL NOTICE: extreme close-up face (angry-sharp brows, eyes shift aside) 1.5-3 s held with a ring ripple, then CUT to the cause (floodlight, cable). Lever: scale. Feeling: "he noticed something".
- BLINDING LIGHT BRIDGE: a bright starburst (12-16 rays) used as the optical link between his eyes and the threat. Lever: light.
- EMPTY-FRAME BEAT: hero falls out of frame and an empty box/room holds 0.7 s (comedy). Lever: absence.
- HOLD = WEIGHT: sad/heavy beats are the LONGEST holds (3-5 s) with dim palette, wide aerial pull-back, and DIGITAL SILENCE (350-351 s). Lever: hold + silence + scale.
- SCREEN-IN-SCREEN: replay on stadium board, camera pushes until it fills the frame. Lever: frame. Feeling: "the world is watching".
- SHRINKING FRAME (iris to black ~24 f) before a hook/ending. Lever: frame.
- GHOST ECHO on fast limbs (2-3 copies 25-40%): speed without motion blur.
- SCORE FLIP / HUD COUNTER: numbers as drama (VICTORY x28->x30, 119:58->120:00, 0.20->0.29 s). Lever: text.
- AMBIENT LIFE: window flicker, crowd camera-flash specks, LED boards, steam, bokeh drift, birds, fly passing the lens. Lever: micro-depth.

## D. INVENTED PROPOSALS (not seen in refs; brain may use if the protocol says so) - label "proposal", test visually
- Fear/dread: slow vignette tighten (+25% over 40 f) + desaturate 30% + 1.02x creep zoom-in on the hero.
- Memory/flashback: sepia-peach grade + soft bloom + 8-12 px edge blur + gentle 1.5% scale drift.
- Realisation: hold still 8-12 frames, then snap a single cream rim-light on the face + colour returns.
- Loneliness: shrink hero to 5-8% of frame in a huge empty set + cool grade + long hold.
- Danger approaching off-screen: shadow shape or red light spill enters frame before the cause.
- Victory: warm grade +10% + crowd arms up loop + sun-disc rays brighten.
- Loss/grief: colour drains from hero's red to grey over 60 f while everything else stays.
RULE: a proposal must be motivated by the script line it sits on; log it in the shot plan with "device / lever / state A->B / switch / restore".

## E. FOR THE REMOTION BRAIN
Implement grade as a per-shot object { sat: 1, hueShift: 0, bright: 0, vignette: 0.5, tint: '#...'} tweened by the timeline; keep HUD outside the grade group. Bursts: component <Burst frames={2}/>. Store each shot's device list so the brain can audit for repetition.
