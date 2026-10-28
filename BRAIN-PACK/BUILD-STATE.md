# BUILD STATE - cinematic stickman director brain (READ THIS FIRST AFTER ANY LIMIT / NEW CHAT)
Last updated: 2026-10-28 08:20. Owner: Salman (he is the eyes; he runs stress tests and gives feedback).

## RESUME PROTOCOL (do exactly this)
1. Read memory file /areas/stickman-build-state.md (always current) and /areas/cinematic-stickman-longs.md.
2. If /home/claude/stickman/ exists: read this file + FILE-INDEX.md. If it is EMPTY or missing: ask Salman to attach BRAIN-PACK-all-files.zip (he has every file) and unzip it into /home/claude/stickman/.
3. Find the first batch below that is not DONE. Open its file; if the file exists but is unfinished, read it and continue from the last finished section (every file has a PROGRESS line at the top).
4. Never restart a finished batch. Never delete research. Quality over speed.

## SAVE RULES (while building)
- Build each file in sections; after EVERY section write it to disk and update the PROGRESS line at the top of that file.
- After EVERY finished batch: (a) update this file, (b) update memory /areas/stickman-build-state.md, (c) copy file into BRAIN-PACK/, update FILE-INDEX.md, rebuild BRAIN-PACK-all-files.zip, (d) SEND the file(s) to Salman.
- Salman's decisions go into memory the same turn he says them.

## LOCKED INPUTS (do not re-ask)
Character = CHARACTER-SPEC-v1.md (locked). Look target = look-target/. Prompts = IMAGE-PROMPTS-v2.md. Requirements = DIRECTOR-BRAIN-REQUIREMENTS.md (sections 1-10). Strategy = STRATEGY-DECISIONS-v1.md. Cinematography = SHOT-GRAMMAR-v3.md + MASTER-SPEC-v1.md (letterbox bars, locked camera default, all measured rules stay).
Method: worlds = still 3D renders WITHOUT blur made by Salman; brain makes depth map, blur, bokeh, glow, parallax, letterbox; character is real 3D lit by a Light Card; anti-stretch parallax budget; new angle = new image of the same place.

## BATCHES (status: TODO / IN PROGRESS / DONE)
- B0 Resume infrastructure (this file + memory mirror): DONE
- B1 CHARACTER-BRAIN-v1.md (full detail of how the stickman looks, scales, emotes): DONE 2026-10-28 (movement rules go in B5)
- B2 WORLD-PROMPT-WRITER-v1.md (brain writes world + same-place-angle prompts, light card, plate checks): DONE 2026-10-28
- B3 CAMERA-SHOTS-LIBRARY-v1.md (all cinematic angles/shots, when and why): DONE 2026-10-28
- B4 EFFECTS-FOR-FEEL-LIBRARY-v1.md (blur, handheld, glow, bokeh, colour reasoning, transitions, foreground/background life, text style): DONE 2026-10-28
- B5 PERFORMANCE-LAYER-v1.md (micro-movements, walking/running/physics, dialogue shots, crowd/background people, inventing people/objects in our style): DONE 2026-10-28
- B6 PRODUCTION-RESUME-PROTOCOL-v1.md (limit-proofing while PRODUCING videos: per-video state file, shot list JSON, chunked render, resume steps): DONE 2026-10-28
- B7 DIRECTOR-BRAIN-v1.md (joins everything; decision engine; muted-understanding rule): DONE 2026-10-28 (+ BRAIN-CHEATSHEET-v1.md)
- B8 STRESS-TESTS-v1.md (scenario list + scoring sheet for Salman to judge): DONE 2026-10-28
- Then: iterate from Salman's stress-test feedback (log in ITERATION-LOG.md). Round 1 = S1,S2,S3 (STRESS-ROUND-01.md): DONE, sent, WAITING for Salman's feedback and plates P01,P03,P06; proposals F2-F4 await his 'build'
- Later (not now): compositing test with Salman's empty worlds; Remotion test T1-T5 only when he says go; sound brain; topic brain; script brain.
