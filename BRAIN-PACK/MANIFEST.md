# BRAIN PACK MANIFEST (rebuilt 2026-10-28)
Everything the brain-building step needs. Read in this order.

## A. Start here (rules and specs)
1. MASTER-SPEC-v1.md — master spec, sections 0-24 (look, characters, camera, cuts, effects, colour, easing, text, per-reference changes, corrections, device invention, shot grammar, labelling, angles, plugin fold-in, fly shots)
2. FILE-INDEX.md — index of every file
3. PATTERNS-LOG.md — cross-video patterns (rule = 3+ videos, likely = 2, seen once = 1)
4. RESEARCH-CHECKLIST.md — Salman's research brief for every reference

## B. Brain logic (how the brain decides)
- SHOT-GRAMMAR-v1.md (decision engine) -> v2 (real frequencies) -> v3 (angles, tricks, camera movement, story recipes)
- DEVICE-INVENTION-v2.md and FEEL-DEVICES-v1.md (invent feel devices from the script)
- FLY-SHOTS-3D-v1.md (fly / depth-travel shots, dynamic)
- PLUGIN-FOLD-IN-v1.md (build protocol, beat splitter, rig vocabulary + invention rule, visual checklist, render planning, decisions on conflicts)
- PLUGIN-SOUND-PARKED.md (sound notes, for the sound brain later)

## C. Measured data per reference (ref1 Telekinesis, ref2 Reaction Time, ref3 One Second Felt Like Ten, ref4 500 IQ, ref5 Gravity film)
refN-notes/findings, camera-measured, colour-state-map, palette, easing, transcripts, ref2 style block and synthesis, ref5 pacing by block, metrics_all.json (uniform metrics for all five).

## D. Labelling and statistics
labelling/labels_ref1-5.csv (1,203 shot-size labels), angles_ref1-5.csv (angle/trick tags), refN_shots.json (shot start and length), stats.py, angstats.py, camstats.py, save.py, save_ang.py, make_label_sheets.py; STATS (SHOT-STATS.md), ANGLE-STATS.md, CAMERA-BY-SHOT-TYPE.md, LABEL-CODEBOOK.md.

## E. Scripts to repeat the measurements on a new video
scripts/: run_ref.sh (one-command resumable pipeline), scan1.py, scan2.py, cuts.py, cam_summary.py, easing3.py, easing_any.py, grade_scan.py, palette.py, metrics_all.py.

## F. Plugin reference (not our rules)
REF-PLUGIN-raw/ — the aiTrends plugin's raw reference files and engine code, kept for study.

## NOT in this zip (kept in the project folder, not needed to build the brain)
The reference mp4 files, per-frame CSVs (scan1/scan2/g*.csv), contact-sheet and montage images, the 5 labelling sheet zips (sent separately), the tutorial transcript and plugin originals (_incoming-tutorial/).

## Known gaps (open tests, not missing files)
No word-timing alignment of our references; fonts in the references unverified; parallax/real-3D check for city and stadium shots; sound brain, topic brain and script brain not built yet; Remotion render test T1-T5 pending (only when Salman says go).
