# PLUGIN FOLD-IN v1 — what we took from the aiTrends 2D Studio plugin (approved by Salman 2026-10-27)
Rule: this file ADDS to our research; where it disagrees with our measurements (§8) OUR measurements win. Raw plugin files kept for reference in BRAIN-PACK/REF-PLUGIN-raw/. Everything marked START VALUE is a default to use until our own measurement says otherwise.

## 1. Build protocol (usage-limit proof)  [item 1]
- ONE master shot file owns all timing. Per shot: id, start, end, line (the spoken words), scene (one concrete sentence of the picture), set (location), bars, in (transition type + frames), sfx, amb, params, notes. Shots are contiguous (each end = next start, first starts at 0, last ends at voice length + about 1.5 s). Also music sections: start, end, mood, intensity.
- Build in batches of 8-12 shots. After each batch: render one still per shot into a contact sheet, LOOK at it, fix, then move on. Never start the full render before the sheets pass.
- Before the full render: render a 30 s preview (0-30 s, half scale), get approval.
- Determinism: scene code may not use random numbers or the clock. Use a seeded random function and the shot time t. (Remotion also needs this.)
- Resume rule: all state lives in files (shot file, cast file, set files, per-shot scene files, a progress note). A new chat reads the progress note and continues from the next unbuilt batch.
- If the user is away: take defaults, state what was assumed, continue.
- QC checklist per sheet: no missing or error frames; picture matches the line and the key action lands on the key word; characters readable (rim light, staged against a brighter area, not cut off); outfits and screen direction consistent in a scene; mostly dark with 1-3 bright accents; text short, inside safe area; max 3 consecutive shots of the same type; numbers match the narration.

## 2. Turning word timing into shots (beat splitter)  [item 2]
START VALUES (test against our refs before trusting): split at . ? ! : ; or a pause over 0.7 s; if a phrase is longer than 6.5 s split at a comma or and/but/then/so/because/while/when/until/which nearest the middle; merge fragments under 1.2 s into the previous beat; target about 3 s per beat; each shot starts 0.15 s BEFORE its phrase (range 0.1-0.2); picture continues 1.5 s after the last word. Then the brain edits the draft: fast action beats become several 0.8-2 s shots, dialogue or emotion holds 4-8 s, never over about 10 s without a new action or camera move, every new location opens with an establishing wide. Our own shot grammar (SHOT-GRAMMAR v1-v3) decides shot size and angle; this section only decides where the cuts fall.
OPEN TEST: check on our 5 refs whether cuts land before the matching words (needs word timing for the refs; not available yet).

## 3. Character rig vocabulary + invention rule  [item 3]
Base set (plugin, START VALUES):
- Figure: black circle head (radius 26 rig units), torso 15, limbs 11-13 with round caps, short foot stubs, no fingers except in insert close-ups. Near arm/leg pure ink, far arm/leg a dark purple-grey (TEST against refs). Rim light on every lit figure (width 4-5 at 1080p), direction points toward the light. Contact shadow under every figure; never floating.
- 11-point custom pose objects. Named poses: stand, relaxed, talk, explain, point, pointUp, wave, cheer, handsOnHead, crossArms, think, shrug, holdFront, phone, reach, sad, facepalm, ready, crouch, sit, sitBack, kneel, lie, dive, kick, jump, fall. Blend between poses about 0.3 s; idle figures breathe so nobody freezes.
- Expressions: neutral, smile, happy, joy, surprised, shocked, scared, worried, nervous, angry, determined, sad, cry, smirk, sleepy, thinking, confused, awe. Change them on the beat of the words. Blink every 2.5-4 s with a different period per character. Eyes can look toward a target. Only quoted character lines get talking mouths (with 2-3 faint rings); the narrator never lip-syncs.
- Motion: walk about 160 units/s, run about 420 units/s (phase speeds 0.9 and 1.6 cycles/s); speed-trail afterimages (about 4 copies) for super speed.
- Props: phone, ball, paper, cup, paddle, pointer, tablet, flashlight. Outfit slots: top (hoodie, labcoat, trench, jersey, tshirt, suit, dress, tracksuit), colour, legs, head item (cap, beanie, fedora, headband, visor, hood, ponytail, bun, curly, spiky), face item (glasses, sunglasses), gloves, number, kid (72% size).
- Cast rule: each recurring character gets exactly ONE strong signature colour item, never changed in the video; background people plain ink. Start-value palette: red-orange hoodie #d64a33, yellow cap #f2c21a, pink beanie #f29ac0, green cap #3fb950, blue tee #3a6ea5, purple tracksuit #8a5ad6, white labcoat + round glasses (scientist), black trench + fedora + sunglasses (mentor/antagonist).
INVENTION RULE (brain must go beyond the list, in the same style): when the script needs a pose, face, prop, outfit or character that is not listed, invent it by editing a copy of the nearest existing one, and test it with these checks: (a) it reads as a silhouette from a wide shot; (b) built only from the same parts (circle head, round-capped limbs, flat shapes, white eye and mouth marks); (c) character keeps one signature colour; (d) pose/expression change lands on a word; (e) the invention is logged (name, parent, reason) so it can be reused. Face and character invention also follows our measured style: black round head with white face marks, no outlines on faces beyond the reference look.

## 4. Visual ingredient checklist  [item 4]
Light and value (START VALUES): one key light per shot, shown and spilled (glow, floor pool, light cone, god rays); 60-75% of the frame dark mid-tones with 1-3 bright accents; stage the black figures in front of the brightest area; windows are the signature element; atmosphere in nearly every shot (dust indoors, rain at night, drops for time-stop, stars, lens streak, fog). Take every colour from the mood or style tokens, never hard-coded, so a grade change re-themes the video.
Depth layers (parallax factor): sky 0.1-0.2, skyline/hills 0.3-0.4, back wall 0.5-0.6, floor/props 0.8-0.9, characters 1.0, blurred foreground 1.5-1.8 (blur 8-14). Most medium shots should have something soft in the foreground (glass, plant, railing, crowd heads, another character's shoulder). Extend walls, floors and skies beyond the frame so camera moves never show edges.
Eight lighting moods (START VALUES):
| mood | sky (top to bottom) | key | rim | wall | floor | dark | practical |
|---|---|---|---|---|---|---|---|
| day | #8fb0d8, #cfdcea, #efe3d2 | #fff3dc | #fff1d6 | #8d8496 | #5f5866 | #2f2a36 | #ffe2a8 |
| golden | #6b5a8e, #e89a6a, #f9d49c | #ffcf8f | #ffc68a | #5a3a34 | #45302a | #2a1814 | #ffe7b0 |
| dusk | #3d3360, #8a5a86, #e8956b, #f7cf98 | #ffc68a | #ffc68a | #4a3646 | #3d2c38 | #231a27 | #ffd59a |
| night | #0b1028, #1d2550, #3a3570 | #c9d4ff | #a9b8ff | #262a46 | #1b1e33 | #0f1122 | #ffb860 |
| storm | #141a33, #2a3358, #3d4670 | #dfe6ff | #cfd9ff | #2b3150 | #1c2238 | #0d1020 | #bcd0ff |
| interiorWarm | #c98a74, #f2b585, #f7cf98 | #ffd59a | #ffcf8f | #4f3a40 | #3a2a2e | #21171c | #ffd28a |
| interiorCool | #2a3560, #5a6aa0 | #cbd6ff | #b8c6ff | #2e3150 | #22243a | #121426 | #9fe0ff |
| void | #0a0e1a, #121a2e | #ffffff | #8fb8e8 | #121a2e | #0d1322 | #070a12 | #ffd47e |
Grade presets (START VALUES, ours measured per ref win): dusk = contrast 1.0, sat 1.0, vignette 0.55, grain 0.055, bloom 0.55; midnight = contrast 1.06, sat 0.8, cool lift, vignette 0.65, grain 0.06; golden = sat 1.18, warm gain, vignette 0.45; neon = contrast 1.15, sat 1.4, vignette 0.7; storybook = contrast 0.92, lifted pastel, vignette 0.3, grain 0.07.
Effects list to draw from: rain, drops, dust, snow, stars, fog, sun, moon, godRays, lightCone, pool, lensStreak, sparkle, lightning, speedLines, rings, skyline, hills, clouds, tree, pine, lampPost, windowFrame, facade, door, chair, stool, counter, screen, bed, clock, floorLines, crowd.
On-screen graphics list: titleCard, bigLine (question or chapter line), badge (corner multiplier or day counter), readout (label + value), callout (leader-line label), dimension (arrowed measure), dataCard (title, counter, curve drawing on), compareBars, meter, blueprint diagram + line figures, speech bubble, endScreen, captions. Text rules: at most 1-2 short labels at once; sentences only for title, question, end screen; graphics appear on the spoken word and leave before the cut. Colours: gold for key numbers, coral for alarming values, cream for labels, blueprint blue for diagrams. Fonts (UNVERIFIED against refs): Fredoka Bold caps titles, Nunito Black labels, Playfair Display Black Italic end question.
Shot-type list with plugin proportions is NOT adopted (see §8); our proportions are in SHOT-GRAMMAR v2/v3.

## 5. Sound  [item 5, PARKED]
Discussed when we build the sound brain. Raw plugin sound notes saved untouched as BRAIN-PACK/PLUGIN-SOUND-PARKED.md (36 SFX names, 11 music moods, ambience beds, ducking and loudness numbers, placement conventions). Do not use yet.

## 6. Render time planning at 1080p  [item 6]
Plugin's own measurement: about 2 frames per second at 720p on a 2-thread CPU; 1080p about 2x slower (about 1 fps); 4K about 8x; a modern 8-core desktop 3-5x faster; GPU helps 3D shots. Use only as a rough guide for our Colab vs laptop test (run only when Salman says go): 3 min at 24 fps = 4,320 frames, about 72 min at 1 fps; 8 min = 11,520 frames, about 3.2 h; 24 min = 34,560 frames, about 9.6 h. Remotion's speed is not the same engine; the test will replace these guesses.

## 7. Story flow and numbers on screen  [item 7]
Flow: cold-open hook (often a frozen dramatic moment) -> title card -> normal life and discovery -> escalation with concrete numbers -> the cost or twist -> climax -> resolution -> "is any of this real?" science segment (blueprint diagrams) -> end screen with a question and subscribe call. Every number or measurement the narrator says appears on screen, animated on the spoken word. Abstract lines become a visual metaphor, diagram or close-up reaction. Keep the narration untouched; each shot illustrates the words spoken while it is on screen. Our own structure findings (cold open, pace curve, end card or THE END) still govern.

## 8. Conflicts: decisions (Salman, 2026-10-27)
- Camera: OURS. 83% locked, faces never move; moves only where our data says (push-ins on diagrams, pans/tilts on places and action, pull-outs to end sections).
- Pop-in animation: OURS. No overshoot or bounce; smooth ease-out, 0 of 213 measured.
- Giant face (extreme close-up): OURS, but DYNAMIC. No fixed percentage. The brain decides from the script: use an extreme face only at an emotional peak (realisation, grief, fear, decision, a big "you" moment) where the face carries the meaning; skip it for plain information, action, transitions and diagrams. Guide from data: extreme face 0-4% of shots per video (ref1 0, ref2 2.8, ref3 4.1, ref4 0, ref5 2.7), a plain close-up (C) is the normal emotional shot (23% overall), emotional beats are about 8% of shots and are spread out (median gap 5 shots, only 25% back-to-back). Cap about 5% per video; a story-heavy film may go higher only if the script has that many real peaks; an explainer may use none.
- Wide shots: OURS (25% of shots, 75% of new-place shots).
- Also OURS: shot rate, letterbox 41 px (2:1), dissolve lengths, genre profiles, pace curve, angle/trick vocabulary.

## 9. Not taken (Salman agreed)
Topic finder, title formats, script/niche engines, fact bank rules, voiceover-safe text rules; Claude Code and plugin install mechanics; Whisper and ElevenLabs tooling; 9:16 vertical rules; the five style presets as a menu. (3D flying shots were first skipped, then ADDED by Salman the same day: see section 10.)

## 10. 3D flying shot (added by Salman 2026-10-27: "we want it, but dynamic, the brain should think")
The full rules now live in FLY-SHOTS-3D-v1.md (when the brain uses it, when it skips, Method A layered 2.5D default / Method B real Three.js only when needed, camera grammar from our measurements, thinking steps, open tests). That file is the single source; this section is only a pointer.
