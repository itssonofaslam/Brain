# FILE INDEX (stickman longs). Keep updated. All files are sent to Salman so nothing is lost.
Root: RESEARCH-CHECKLIST.md, telekinesis-notes.md, telekinesis-transcript.txt, telekinesis-cutlog.md, telekinesis-blueprint.md
video/ (ref1 mp4 measurements): scan1.csv, scan2.csv, cuts_auto.csv, telekinesis-camera-measured.md, audio-rms.csv, scan1.py, scan2.py
ref2/: ref2-notes.md, ref2-synthesis.md, ref2-style-block.txt, transcript.txt
Rule: every file created gets sent to him. Memory: /areas/cinematic-stickman-longs.md
MASTER-SPEC-v1.md (root): locked-in v1 spec of the whole look/motion/camera/effects/build. Update with each new reference.
video2/: ref2-mp4-findings.md, ref2-camera-measured.md, ref2-palette-and-bursts.md, ref2-easing-measured.md, easing.py, ref2-move-shots-montage.png, ref2-board-scene-52s.png, cuts_auto.csv, audio-rms.csv, scan1/2.csv/.py
FEEL-DEVICES-v1.md (root): feel devices + invention protocol + perception-grade analysis.
grade/: grade_scan.py, g1.csv (ref1 per-frame colour stats), g2.csv (ref2), grade_montage_a.png, grade_montage_b.png, ref2-colour-state-map.md

## video3/ (REF3 "What If One Second Felt Like Ten")
transcript.txt | scan1.csv scan2.csv g3.csv audio-rms.csv cuts_auto.csv | ref3-palette.md ref3-camera-measured.md ref3-colour-state-map.md ref3-findings.md | ref3-grade-switch-montage.png sheet1-7.png | scan1.py scan2.py grade_scan.py easing.py cam_summary.py grade_summary.py
MASTER-SPEC-v1.md section 15 = REF3 changes.
ref3-easing-measured.md easing3.py
PATTERNS-LOG.md (cross-video pattern table; add a column per new video)

## video4/ (REF4 500 IQ Disappear)
transcript.txt scan1.csv scan2.csv g4.csv audio-rms.csv cuts_auto.csv | ref4-findings.md ref4-palette.md ref4-camera-measured.md ref4-colour-state-map.md ref4-easing-measured.md ref4-grade-switch-montage.png sheet1-6.png | scan1.py scan2.py grade_scan.py cam_summary.py grade_summary.py easing3.py cuts.py palette.py
PATTERNS-LOG.md now has 4 columns + update section; MASTER-SPEC-v1.md section 16.

PATTERNS-LOG.md v2 (corrected, uniform metrics) | metrics_all.py metrics_all.json | easing_any.py video/easing-auto.md video2/easing-auto.md | check/hud_ref1_ref2.png | MASTER-SPEC-v1.md section 17 (corrections)
DEVICE-INVENTION-v2.md (script -> device engine + premium guardrails)
run_ref.sh (resumable one-command pipeline for a new reference: ./run_ref.sh videoN file.mp4)

## video5/ (REF5 gravity 24 min; joined.mp4 NOT sent = 209 MB, rebuild from the two source .mov files via list.txt + ffmpeg concat/scale)
ref5-findings.md ref5-pacing-by-block.md ref5-camera-measured.md ref5-colour-state-map.md ref5-palette.md ref5-easing-measured.md ref5-grade-switch-montage.png ref5-transcript.txt cuts_auto.csv audio-rms.csv scan1.csv scan2.csv g.csv sheet1-10.png | run_ref.sh (one-command resumable pipeline) | metrics_all.py now takes ref names (python3 metrics_all.py ref5)
PATTERNS-LOG.md has ref5 column + C0; MASTER-SPEC-v1.md section 19; BRAIN-PACK/ = key weight files.
SHOT-GRAMMAR-v1.md (when to use which shot: face XCU, object macro, wide, physics, backgrounds; labelling pass proposed)

## Labelling pass (new)
- SHOT-GRAMMAR-v2.md — real shot frequencies, sequencing, triggers, pace curve (supersedes v1 numbers)
- labelling/STATS.md — all computed tables; labelling/labels_ref1-5.csv (1,203 labels); labelling/refN_shots.json; CODEBOOK.md; stats.py, save.py, make_label_sheets.py; refN_sheetNN.png

## Angle + camera pass (new)
- SHOT-GRAMMAR-v3.md — angle/trick vocabulary, camera movement by shot type, story recipes, decision engine v3
- labelling/ANGLE-STATS.md, labelling/CAMERA-BY-SHOT-TYPE.md, labelling/angles_ref1-5.csv, camstats.py, angstats.py, save_ang.py

## Plugin fold-in (new)
- PLUGIN-FOLD-IN-v1.md (what we took, start values, decisions); PLUGIN-SOUND-PARKED.md (for the sound brain later); BRAIN-PACK/REF-PLUGIN-raw/ (their raw reference files, not our rules); _incoming-tutorial/TUTORIAL-REVIEW.md
- FLY-SHOTS-3D-v1.md (fly/3D shots: when, how, grammar)
- DIRECTOR-BRAIN-REQUIREMENTS.md (what Salman asked for the director brain, 2026-10-28)

- STRATEGY-DECISIONS-v1.md: 2026-10-28 decisions (skin change only, new niche, own 3D-ish look, animation-quality suggestion). In BRAIN-PACK.

- style-previews/: make_previews.py + style-1..5 PNG/SVG, 2026-10-28 still previews of 5 candidate looks (clay, paper-cut, toon noodle, glass lantern, charcoal), same egg-head character, 3 poses, letterbox, blurred foreground pole.

- [OLD LOOK, retired 2026-10-29, history only] style-previews/style-6-real3d.png + real3d/ (render3d.html, shoot.py): 2026-10-28 real 3D test still, own WebGL ray-marching shader (three.js download blocked). Glossy black head with white face marks, real lights, soft shadows, camera blur.

- STYLE-PROMPT-IMAGE-v1.md: image-generation prompts (master, close-up, character sheet) that chose the OLD look. SUPERSEDED for the character 2026-10-29. In BRAIN-PACK.

- look-target/: [world/lighting reference only now; its character is retired] Salman's chosen LOOK TARGET (3 AI-generated stills from the image prompt: stadium wide, face close-up, rain street). Round black/white-face stickman, bold outline, real 3D lighting, cinema blur. Not in zip (images).

- IMAGE-PROMPTS-v2.md: (character-sheet prompt RETIRED 2026-10-29, see CHARACTER-SPEC-v2) world plate prompt (no blur), same-place-new-angle prompt, light card, anti-stretch rules. DIRECTOR-BRAIN-REQUIREMENTS.md section 10 = look lock. Both in BRAIN-PACK.

- CHARACTER-SPEC-v2.md: LOCKED canonical 3D stickman, Salman's text spec VERBATIM (2026-10-29; no image exists or is needed). Replaces CHARACTER-SPEC-v1 (old/CHARACTER-SPEC-v1.before-character-v2.md).

- CHARACTER-IMPLEMENTATION-PROTOCOL-v1.md: how the brain puts the character into a real Three.js/Remotion repo (scope, inspect first, replace not add, API contract, rig, determinism, verification with 8 views and 10 poses, diff review, honest report). From Salman's replacement brief PDF. Training only until he says build.

- BUILD-STATE.md: resume protocol + batch status (READ FIRST after a limit). CHARACTER-BRAIN-v2.md: B1/B10 working character file (invariants, proportions, head/face, 13 expressions, rig and limits, materials and light, scale by shot size, views, QA; replaces v1).

- WORLD-PROMPT-WRITER-v1.md: B2 world prompt writer (world bible, plate registry, lighting recipes, scale formula, angle prompts by shot code, plate check, examples).

- CAMERA-SHOTS-LIBRARY-v1.md: B3 full cinematic vocabulary (sizes, angles, composition, movements with Remotion build, parallax budget, plates per shot, lens/blur, handheld levels, dialogue coverage, transitions, decision engine v4, recipes by feeling).

- EFFECTS-FOR-FEEL-LIBRARY-v1.md: B4 effects (order of operations, colour reasoning, glow, atmosphere, background life, foreground objects, text, muted test, diagrams, shadows/reflections, motion effects, transitions, invention rules).

- PERFORMANCE-LAYER-v1.md: B5 character movement (principles, rig channels, idle, head/face acting, locomotion, action recipes, emotion acting, dialogue acting, physics, crowds, inventing people/objects, timing table).

- PRODUCTION-RESUME-PROTOCOL-v1.md: B6 limit-proofing while producing videos (five laws, video folder, stages S0-S8, STATE template, chunked render, code checklist, recovery, token thrift, failure table).

- DIRECTOR-BRAIN-v1.md: B7 director procedure joining all files (file map, frame, locked defaults, beat card, per-beat procedure, beat types, budgets, invention, honesty, quality bar). BRAIN-CHEATSHEET-v1.md: one-page summary read first each session.

- STRESS-TESTS-v1.md: B8 four kinds of test, scenarios S1-S12, scoring sheet, iteration and resume-test rules. ITERATION-LOG.md: feedback log.

- STRESS-ROUND-01.md + STRESS-ROUND-01-shotlist.jsonl: first paper test S1-S3 with plate prompts P01-P07, plate request sheet, findings F1-F5. WORLD-PROMPT-WRITER-v1 horizon rule corrected (old copy in BRAIN-PACK/old/).

- CINEMATIC-INTELLIGENCE-v1.md (2026-10-29): coordinating layer from the owner's instruction file: purpose test, priority ladder, dramatic beats/intent, staging, world state, event chains, one timeline, determinism, sound hooks, validation/repair/fallback, optional shot-list fields, anti-patterns. Wins over older library rules. Edited files keep originals in old/*.before-cinematic-upgrade.md: DIRECTOR-BRAIN-v1, CAMERA-SHOTS-LIBRARY-v1, PERFORMANCE-LAYER-v1, EFFECTS-FOR-FEEL-LIBRARY-v1, PRODUCTION-RESUME-PROTOCOL-v1, BRAIN-CHEATSHEET-v1, MASTER-SPEC-v1 (section 25), ITERATION-LOG, FILE-INDEX, MANIFEST, 00-START-HERE-INDEX, BUILD-STATE.
