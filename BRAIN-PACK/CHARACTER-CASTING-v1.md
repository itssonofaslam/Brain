PROGRESS: complete v1 (sections 1-10). Written 2026-10-29 from Salman's instruction: crowd/NPCs must look different from the main character, and the brain must first read what the script says, then edit the base stickman into that person (doctor, girl, child...) in the same 3D style, never reusing the main character's kit. TRAINING ONLY: nothing is built or rendered. Numbers marked (brain) are start values to tune in stress tests.

## 1. THE IDEA IN ONE PARAGRAPH
Everybody in the world is the same SPECIES (the stickman body and face vocabulary from CHARACTER-SPEC-v2). The MAIN character is one INDIVIDUAL of that species, marked by a locked signature kit (turquoise left wristband, compact black daypack, chunky black sneakers with off-white soles and white laces, ivory head with charcoal body). Every other person is CAST from the script: the brain takes the base body, strips all of the main's signature kit, and dresses it with a different cast kit (height, build, head tint, hair/hat/glasses, clothes, footwear, props, accent colour). So a doctor looks like a doctor, a girl like a girl, a crowd like a crowd, in the same smooth 3D style, and the viewer can always find the hero.

## 2. THREE LAYERS (what may change and what may not)
A. SPECIES (all characters, always): smooth sphere head; two vertically oval glossy dark eyes with a catchlight; thin dark brows; one small mouth; NO nose, NO ears; thin stick limbs and neck; hands with thumb and four simple fingers; same rig and joint logic; smooth satin/matte materials; no thick outlines, no chrome, no photoreal texture; same lighting treatment (subtle rim, same grain and grade); constant limb length and thickness while moving. Expressions use the same parameters (CHARACTER-BRAIN-v2 section 5).
B. MAIN IDENTITY KIT (main only, locked): turquoise #1BB3C7 band on the anatomical LEFT wrist; compact black daypack (#141518); black sneakers with thick off-white soles, white laces, white side mark; ivory head #F1E3D8; charcoal body #252629; no extra clothes. Nobody else wears any of these. Turquoise (and near-turquoise teal/cyan) is reserved for him and for story-critical effects.
C. CAST KIT (everyone else, from the script): the slots in section 3. Free to change, inside the style limits in section 4.

## 3. CAST KIT SLOTS
| slot | options (simple smooth shapes, same material language) |
|---|---|
| height | 0.55-1.2 of the main's height (child 0.55-0.7, teen 0.8-0.95, adult 0.95-1.1, tall 1.1-1.2) (brain) |
| build | slim (like main), average (limbs up to about 1.25x radius), stocky (up to about 1.5x; still clearly stick limbs, never muscle) (brain) |
| head | scale 0.9-1.15 of main's head; tint from section 5 |
| head extras | hair shape (bob, ponytail, bun, short, curly puff, bald cap, white wisp for elders), hat, cap, headband, hood, glasses (simple round or square frames), bow |
| neck | scarf, collar, tie, stethoscope |
| torso | coat, lab coat, suit jacket, dress, vest, apron, uniform, hoodie; hugging the stick body, slim volume (torso layer up to about 2x the main's torso width, coats may hang to the thigh) (brain) |
| legs | trousers tube, skirt/dress hem, shorts (only if story needs); legs stay thin below |
| feet | plain shoes, boots, loafers, sandals, heels, slippers, rain boots, bare rounded stubs; NEVER the main's sneaker design |
| hands | bare ivory/tinted hands; gloves (simple), held prop |
| back/side | satchel, handbag, briefcase, tool bag; NEVER a compact black daypack of the main's shape or colour (if the story needs a backpack on someone else, change shape and colour, e.g. a grey rolled pack) |
| accent colour | one costume accent per person (not turquoise) |
| props | what the role needs (clipboard, mug, phone, wrench, umbrella) |
| signature behaviour | one habit (doctor: slow calm moves; child: quick bounces; elder: slow, hunched) (PERFORMANCE section 11) |

## 4. STYLE LIMITS FOR EVERY CAST KIT (so the world stays one world)
- Clothes and hair are smooth, simplified, rounded forms, matte or satin; no cloth folds, fibres, prints, text, logos (a flat simple badge is allowed if the story needs it); no thick outlines; no chrome or glossy plastic.
- Keep the stick read: head clearly the biggest feature, thin neck, thin arms and legs visible below sleeves and hems; clothing never hides the joints so animation still reads; sleeves up to about 1.6x arm radius (brain).
- The face vocabulary never changes (no nose, ears, lashes, mouth shapes of another style). Age or gender is shown with hair shape, clothing silhouette, height, posture and movement, never by redrawing the face.
- Same material treatment, same lighting, same rim logic as the main; head and hands stay readable (head at least about 35 percent bright on expression beats).
- Costume pieces attach to rig slots (head, neck, torso, hips, feet, hands, back) and follow their parents; no floating pieces, no gaps; deterministic (frame-driven) secondary motion only (hair sway, coat hem) and tiny.
- Few signifiers beat many: 2-3 readable pieces per person (silhouette first, colour second, prop third). Do not stack stereotypes.

## 5. COLOUR RULES FOR CAST
- Head tints (brain; the species look stays ivory-satin, only the tone varies): warm tan #D9B99B, light brown #B98B6B, deep brown #8A5E43, pale rose #EBCFC4, olive #CDB48F, dusky #A9917F, pale cool #E8E1DD. Nobody near the main uses exactly #F1E3D8 (far crowd silhouettes excepted).
- Body/costume colours: muted and slightly desaturated (about 50 percent saturation at most), chosen from the scene palette so the world stays cohesive: slate, dull mustard, olive, brick, dusty blue, plum, warm grey, off-white (doctor coat), charcoal. One accent per person. Story-critical items may be bright (a red hoodie, a yellow raincoat) only when the story needs the eye to go there.
- Never turquoise, teal or cyan on cast, so his wristband and the look of the hero stay unique. Never the main's exact black-and-white sneaker look.
- Colours are fixed per cast id (continuity); lighting changes brightness only.

## 6. CROWDS AND BACKGROUND PEOPLE (not clones, not the hero)
Rules: base species body, NO main signature kit, varied but cheap.
| tier | distance | what varies |
|---|---|---|
| T1 far | tiny, silhouette | height 0.85-1.15, build, one costume shape (coat/dress/hat), muted colour; faces not drawn if under about 3 percent of frame height |
| T2 mid | small to medium, blurred | + head tint, hair/hat, shoes shape, one accent colour, one prop in some |
| T3 near/featured | readable | full cast card (section 7); gets its own behaviour and reactions |
Mechanics: every crowd member = species + a seeded pick from a SMALL shared kit library (heads, hair, coats, hems, shoes, props, colours), so geometry and materials are reused (instancing, no per-frame creation); the pick, walk phase and reaction delay are seeded from the person's id (deterministic: same frame, same result); never two identical neighbours; never all the same speed (PERFORMANCE section 9-10). Cap distinct looks per scene (about 12-20 for T1-T2) and recycle with different colours and phases. Background people never copy the hero's silhouette, never carry his daypack, never wear turquoise, never steal attention. Crowd detail follows the shot size and the blur (CHARACTER-BRAIN-v2 section 8).

## 7. THE CAST CARD (one per named or featured person; saved in the video's characters-invented.md, reused every time that person appears)
{"cast":"c01","name":"Dr Reed","source":"b014 'the doctor says...'","role":"doctor","read":"calm authority","height":1.08,"build":"slim","head":{"scale":1.0,"tint":"#D9B99B"},"head_extras":["round glasses"],"neck":["stethoscope"],"torso":"white lab coat, knee length, slim","legs":"dark trousers tube","feet":"plain black shoes","hands":"bare","back":null,"accent":"#9DB5C4","props":["clipboard"],"behaviour":"slow calm moves, small nods","voice_note":null,"not_main":"no turquoise, no daypack, no sneakers, no wristband","state":"default","first_shot":"s0042"}
Continuity: the card never changes between shots unless the script changes it (a state change gets its own frame and reason: takes off coat, puts on hat). Check every new shot against the card.

## 8. HOW THE BRAIN THINKS ABOUT A CHARACTER THE SCRIPT ASKS FOR (do these in order, per beat)
1. READ THE SCRIPT FIRST. Who is this person? Take only what the script says or the story clearly needs: role/job, age, gender if stated, status, mood, place, era, what they DO in this beat, who they talk to. If the script is silent, choose plain and neutral. Never contradict the script, never add backstory the script did not give.
2. WHAT MUST THE VIEWER GET WITH THE SOUND OFF? One-line "read" (muted test): "a calm doctor", "a scared little girl", "a bored crowd". The read must work at the planned shot size and distance (silhouette first).
3. IS IT THE MAIN OR SOMEONE ELSE? Another person = cast. The main stays himself (section 9). Name every person in the beat's "who" list with a cast id.
4. START FROM THE BASE BODY and STRIP the main's signature kit completely (wristband, daypack, sneakers, his colours).
5. PICK 2-3 SIGNIFIERS in this order: silhouette (height, build, head scale, hair/hat, coat or dress shape), colour (head tint + one accent), prop/behaviour. Doctor: lab coat + stethoscope or glasses + calm slow moves. Girl: hair shape (ponytail, bob, bow) + dress or skirt silhouette + different shoes + shorter height if a child. Elder: white hair wisp, hunch, cane, slow. Guard: cap + uniform jacket + upright stance. Stranger: generic coat in a muted colour.
6. BUILD IT IN THE SAME STYLE (section 4): smooth, simple, same materials, stick limbs visible, no outlines.
7. DISTINGUISH FROM THE MAIN: side-by-side test in the planned shot: different silhouette AND different colour AND none of his kit; in a crowd he must be findable by his turquoise band and daypack alone.
8. WRITE THE CAST CARD and the muted line; reuse the card for every later appearance.
9. STAGE IT: height difference and eyelines (CAMERA-SHOTS-LIBRARY sections 3 and 9: a smaller person is looked down on, a taller one up), who is left and right (180 degree line), who is speaking (head turn, mouth, a slight gesture; mouth shapes per PERFORMANCE section 8), accent colours so a muted viewer can follow a two-person dialogue.
10. VALIDATE (section 10) before the shot goes into the shot list.

## 9. WHEN THE MAIN CHARACTER IS ALSO PLAYING A ROLE
- The script asks for a DIFFERENT person (doctor, girl, stranger): cast a new person (section 8). The main is NOT edited into them and keeps his full kit in the same scene (he is "our character" talking to "the doctor").
- The script says the MAIN does something in a role (he is the doctor, he wears a costume, he disguises himself): keep the main's anchors (ivory head, face vocabulary, hands, the turquoise LEFT wristband, his proportions) and put the costume ON TOP as cast-kit pieces; the sleeve stops above the wrist so the band stays visible; sneakers stay unless the script changes them. The daypack may be off only with a story reason shown on screen once (taken off, left in a locker) and a state flag (backpack:off) that holds until it is put back. Say in the card: "main in costume".
- A transformation or flashback (younger him): treat as a story event with before/after states; keep the identity anchors; OPEN: ask Salman how a younger self should look (see section 10).

## 10. VALIDATION CHECKLIST AND ANTI-PATTERNS
Checklist (every cast person, every shot): Does the script support this look? Species rules kept (sphere head, two oval eyes, brows, small mouth, no nose or ears, stick limbs, fingers)? None of the main's kit (turquoise or teal, daypack, sneaker design, wristband)? Different silhouette from the main at this shot size? 2-3 signifiers, readable muted? Style kept (smooth, matte/satin, no outlines, no chrome)? Limbs and joints still readable and animatable? Colours from the scene palette and fixed by the card? Same card as last time? Crowd members varied, seeded, reusing the shared kit library?
Anti-patterns: crowd made of identical clones; crowd with his daypack or turquoise band; cast characters that look like the main minus accessories; a doctor made by editing the main (he disappears from the scene); redrawing the face (nose, ears, lashes) to show gender or age; stereotypes stacked on one person; clothing that hides the stick limbs; costumes in a different render style; changing a person's look between shots without a script reason; per-frame random variation; spending detail on far people who are 2 percent of the frame.
Open decisions for Salman: (a) may other people's head tints differ from the main's ivory, or should every head stay ivory #F1E3D8 with only costume changes? (b) hair shapes on cast: allowed here (the no-hair rule applies to the main only); (c) younger/older versions of the main; (d) whether a featured speaking character may carry a small reserved accent (e.g. doctor's coat) that is never used on the main.

## 11. CODE NOTE (for when Salman says build; see CHARACTER-IMPLEMENTATION-PROTOCOL-v1)
Keep ONE character factory and ONE rig. Add an optional cast parameter (a cast card) whose DEFAULT is the main character, so every existing caller keeps working. The main's wristband, daypack and sneakers are parts that the cast card turns on or off or replaces; cast kits are extra parts attached to the same rig slots. Never a second competing character implementation. The crowd/NPC scene system itself is out of scope for the character task unless it is genuinely shared: report the smallest needed change instead of editing it.
