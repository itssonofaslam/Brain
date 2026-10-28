PROGRESS: complete v1. Round 1 next (STRESS-ROUND-01.md). Feedback log: ITERATION-LOG.md.
# STRESS TESTS v1 (batch B8, 2026-10-28)
Purpose: find where the brain is weak BEFORE a real video, in the cheapest way, then fix the brain files (iteration) until Salman is satisfied. Salman is the eyes.
Test fixtures (the short scripts below) are written only to test the director. They are not the script brain.

## 1. THE FOUR KINDS OF TEST
A. PAPER TEST (needs nothing from Salman): the brain runs the full procedure (DIRECTOR-BRAIN section 6) on a fixture and outputs the beat cards, shot lines, plate prompts, Light Cards, character performance notes, effect lists, text styles. Salman reads and judges; he can also paste the plate prompts into his image AI to see if the plates come out character-ready and in the look-target style.
B. PLATE TEST (needs Salman's images): Salman generates plates from the brain's prompts; the brain checks them (WORLD-PROMPT-WRITER section 11), writes verdicts and Light Cards, and rewrites prompts that missed. Measures prompt quality.
C. COMPOSITING TEST (needs a render; only when Salman says go): the real-3D character, depth map, parallax, blur, glow and shadows in Remotion with his plates. Measures whether the whole method looks like the look target. This is the Remotion test T1-T5 of the earlier plan.
D. RESUME TEST (limit-proofing): stop mid-task on purpose; start a NEW chat with only the memory and the zips; the brain must continue exactly. Run once on the brain build and once on a mini video.

## 2. SCENARIOS (fixtures)
Each has: input lines, what the brain must show, pass criteria.
| id | fixture | tests | pass if |
|---|---|---|---|
| S1 | "At dawn he walks alone into a stadium so big it swallows him." | arrival, scale contrast, K or S, slow pull, tiny-figure scale, plate prompt with open ground, life (birds), loneliness light | wide first, figure about 5%, one dominant sun, light card complete, locked camera, muted meaning clear |
| S2 | "Rain hammers the street. He looks up at a sign glowing like a second moon." | rain night neon recipe, animated rain (not baked), foreground pole, passer-by, reflection on wet ground, rim colour match | rain in plate prompt = "no streaks", animated layers listed, reflection and rim from the sign, life and foreground motivated |
| S3 | "Then he understood. Everything he knew was wrong." | emotional X close-up, rack focus, background-only plate, expression acting, handheld H0-H1 | extreme close-up, bokeh from lights, eyes/brows/mouth parameters given, no cheap effect |
| S4 | "Footsteps behind him. He ran. They ran faster." | walk to run, run toward camera, H4, motion blur, impact shake, several short shots | cuts 0.8-2 s, gait numbers from the table, planted feet, handheld ramp, camera reasons |
| S5 | "'Are you sure?' the doctor asked. 'No,' he whispered." | dialogue coverage, 180 degree line, reverse plate, speaker and listener acting, invented doctor | master + singles + reaction, correct screen sides, mouth timing from word timing, doctor invented in our style |
| S6 | "The sky split open and a planet the size of the horizon rose above the desert." | fantasy lighting, impossible light source, S shot, fly-shot decision, new plate request | light from the planet drives rim colour; decision whether fly shot (with reason); parallax budget respected |
| S7 | "Your reaction time is 0.25 seconds. A pro's is 0.15." | numbers on screen on the spoken word, diagram/UI, text style, muted test | numbers appear on the words, text font/colour by feeling and away from the face, diagram in our look, no handheld |
| S8 | "Fifty thousand people held their breath." | crowd, background people variation, reaction delays, blurred layers | varied heights and speeds, out-of-sync cycles, closest react first, character still the focus |
| S9 | "Time slowed. Every raindrop hung in the air." | invented feel device (slowed time), grade switch, particles hanging, snap restore | protocol FEEL-DEVICES followed, state A/B numbers, restore moment, one device only |
| S10 | "By night he was somewhere else entirely." | time/world jump transition, dissolve vs whip, same-place or new plate | transition chosen with reason, grade switch numbers, plates needed listed |
| S11 | "He sat on the edge of it all and watched the sun go down. Quiet." | ending, K silhouette, slow pull, fade, peace | wide silhouette, locked or H0, fade 12-24 f, bars on |
| S12 | edge cases: (a) a 20 s monologue; (b) three beats under 1 s; (c) indoor room with no visible ground area; (d) a night scene with no light source; (e) a request that breaks a rule (dutch tilt three times; character recoloured red) | robustness | brain splits/holds correctly, fixes the plate problem, refuses or flags the rule break with a reason and an alternative |
Round order: Round 1 = S1, S2, S3 (paper tests). Round 2 = S4, S5, S7. Round 3 = S6, S8, S9, S10, S11, S12. Plate test for S1-S3 after Round 1. Composite test only when Salman says go.

## 3. SCORING SHEET (Salman, plain words; 1 = bad, 5 = great; write one line if below 4)
1. Story clear with the sound off?
2. Does it feel like our look target (premium, glowy, 3D)?
3. Shot variety and rhythm: not boring, not messy?
4. Camera choices make sense (not moving for no reason)?
5. Light and mood fit the feeling? Would the plate prompts give the right picture?
6. Does the character belong in the world (shadow, reflection, rim light)?
7. Does the world feel alive (background life, atmosphere)?
8. Is the acting believable (face, posture, walking)?
9. Are the prompts clear enough to copy and paste?
10. Anything cheap, random, or copied from others?
Then one decision per note: KEEP / FIX in the brain (all videos) / this test only.

## 4. ITERATION RULES
- Each note goes into ITERATION-LOG.md (id, date, test, Salman's words, sorted type, file and section to change, status).
- Brain-wide fixes: write the fix as a proposal, show it in two lines, wait for "build"; then edit the brain file, bump its version note, log, rebuild and send the pack.
- After each fix rerun the failing scenario; the log records pass/fail.
- A scenario passes when Salman scores 4 or 5 on all ten lines. The brain is "fine for us" when S1-S12 pass and the composite test matches the look target to his eye.
- Keep every old version of changed files in BRAIN-PACK/old/ so nothing is lost.

## 5. RESUME TEST PROCEDURE (limit-proofing check)
1. Mid-task (for example, halfway through Round 2), Salman opens a NEW chat and writes: "Continue the stickman brain. Read memory."
2. The brain must: read /areas/stickman-build-state.md, BUILD-STATE.md, ITERATION-LOG.md, state its position in one line, and continue with the next undone item without asking him to repeat anything.
3. Pass if nothing is repeated, nothing is lost, and no question is needed except for missing files (then he attaches the zip).
