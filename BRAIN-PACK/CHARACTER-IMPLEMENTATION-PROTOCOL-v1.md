PROGRESS: complete v1 (sections 1-12). Written 2026-10-29 from Salman's file Brain_Character_Replacement_Instructions.pdf. TRAINING ONLY: nothing is built, rendered or run until Salman says build. This file is how the brain behaves when it is asked to put the character (CHARACTER-SPEC-v2.md) into a real Three.js / Remotion project, or to change it later.

## 0. WHEN THIS APPLIES
Whenever the task is to create, replace or change the character in code. It is a TARGETED character task, not a general upgrade. Authority: CHARACTER-SPEC-v2.md controls APPEARANCE; this file controls repository scope, safety, compatibility and verification. If they conflict, the spec wins on how he looks, this file wins on what files may be touched.

## 1. SCOPE
IN scope (only files whose direct job is the character): the character model/factory/component; its Three.js geometry; character-only materials; face construction; character-only clothing/accessories (backpack, wristband, sneakers); skeleton, joints, pivots, rig; character-level expression/gaze controls; default pose and proportions; character-only constants; character-only helpers; character tests/fixtures if the repo already has them.
OUT of scope (never touch): script parsing, shot selection, camera, editing, scene composition, environments and lighting systems, non-character objects, crowds/NPC systems (unless truly shared and no safe character-local option), audio, Remotion compositions/timing/rendering/export, global animation scheduling or timelines, physics, dependency versions, manifests, build/TS/lint/format config, unrelated bug fixes, refactors, renames, cleanup, optimisation, redesigns.
If an out-of-scope file seems necessary: first try to keep the public interface or add a character-local adapter. If impossible, leave the file unchanged, report the exact blocker and the smallest external change needed. Never claim full integration while a needed change is unmade.

## 2. INSPECT FIRST, DO NOT EDIT YET
1. Read the repo: language, framework, module system, test commands, code conventions.
2. Find the REAL creation entry point (the code that builds the rendered mesh/group), not just files named character or stickman. Never guess filenames, exports or signatures.
3. Trace imports and call sites: how it is instantiated and what callers expect.
4. Split character-only modules from shared utilities (do not edit shared utilities just because the character imports them).
5. Write down the public interface: factory name, parameters, return type, scene-graph assumptions, animation and expression controls, metadata, named mesh/joint references, origin, root orientation, scale, floor baseline, disposal behaviour.
6. Review existing character animations; keep what still fits the new anatomy and can live in character files.
7. Run existing tests, type checks, lint and build for a BASELINE; record pre-existing failures separately.
8. Make a short internal change plan and the list of files to modify. Then implement; do not stop at the plan unless a real blocker exists. Do not ask Salman for file names the repo can reveal.

## 3. SPEC TO CHECKLIST
Read CHARACTER-SPEC-v2.md fully. Turn it into a checklist: every feature, dimension, material, colour, accessory, side assignment, geometric constraint and prohibition (spec sections 1-26; CHARACTER-BRAIN-v2 has the working numbers). Exact values are the starting values unless the repo's coordinate system makes them invalid; then keep relative proportions and report the adjustment. Unspecified details: choose the simplest option consistent with the design (CHARACTER-BRAIN-v2 marks these (brain)). No image is needed and none may be demanded.

## 4. REPLACE, DO NOT ADD
One canonical character replaces the old design in the active path. Remove or replace old character-specific geometry, proportions, materials, face, accessories and constants inside in-scope files. No old design as default path, hidden fallback, alternate preset or accidental second character. Do not create a competing second implementation if the current one can be updated. Keep valid helpers (capsule builders, pivot connectors, material assignment) if they do not encode the old look. Do not delete other intentionally supported characters (NPCs); if entangled, isolate the new one inside the existing architecture. Do not delete research or user work.

## 5. BUILD RULES
- Real reusable Three.js geometry in a THREE.Group (or the repo's equivalent): never a sprite, billboard, flat plane, screenshot or image texture. Use existing geometry/material utilities and libraries; add no dependency.
- Use the repo's established global coordinate convention. Inside the character module define the local system from the spec (Y up, face +Z, left = +X, floor Y = 0) and convert at the root if the project differs; never change global conventions or unrelated scene logic.
- Orientation: verify front, rear, left, right, top, low and three-quarter with the SAME model. Anatomical left is not viewer-left; the wristband stays on anatomical left as he turns; backpack stays on -Z; front of face stays structurally consistent.
- Rig: stable pivots placed to match the geometry; parts attached to intended parents; head, eyes, brows, mouth, hands, wristband, backpack and shoes follow their parents; limb lengths preserved; soles aligned to the ground in neutral pose; overlapping rounded geometry at joints; accessories do not intersect the body badly.
- Geometry hygiene: no accidental double transforms or parent changes, no non-uniform scaling that distorts the head or limbs (unless the spec says so), no parts at wrong depth, no floating face elements, no zero-length segments, no NaN/Infinity transforms, no geometry or materials created per frame, reuse geometry and materials, dispose only what the character owns (never shared resources), no leaked listeners or subscriptions.
- Determinism: frame-driven only (useCurrentFrame/interpolate/spring); no random per-frame values, wall-clock time, timers or autonomous render loops; any secondary motion (backpack, idle) is seeded or a function of the frame. Same frame, same pose.
- Build once, animate transforms; do not add a new global expression scheduler; do not edit story or camera logic.

## 6. PRESERVE THE INTEGRATION CONTRACT
Keep the existing exports, parameters, return type, root object, attachment behaviour, valid animation entry points, expression/gaze controls, named references, origin, scale, floor baseline and disposal behaviour. Do not rename symbols or change signatures to make things prettier. Trace usages before removing any mesh name, joint, property or callback. If the new anatomy differs, add a compatibility mapping INSIDE the character files. If compatibility cannot be kept inside the allowed files, stop short and name the smallest follow-up change. Where the old rig had mitten fists, a face plate or no neck, keep old control names working by mapping them onto the new parts (e.g. fist closing = finger curl; plate eye offsets = eye surface offsets).

## 7. VERIFY (never claim a check that was not run)
A. Static: type-check, lint of modified files, character tests, tests that instantiate the character, build/import check; compare with the baseline and state which failures are pre-existing.
B. Instantiation: same entry point as before; correct type and root structure; required meshes, materials and accessories exist; references and controls reachable; root transform and baseline right; no external asset needed.
C. Visual (only if the repo has a safe preview path; if not, say so and do the strongest non-visual checks): the SAME model from front, front three-quarter, left, right, rear, rear three-quarter, top and low angle; neutral pose and representative poses (neutral, walking, running, jumping, sitting, waving, pointing, surprised, thinking, scared). Check: recognisably the stickman; head spherical in every view; proportions match the spec; features attached to the curve; clean rear head; wristband on the correct anatomical side; backpack on the back, not floating or badly intersecting; shoes keep shape and stay attached; soles contact the floor; joints show no gaps; limbs keep length; nothing missing, inverted, detached or malformed; no old geometry left.
D. Regression: API fits the old contract; unrelated video generation behaviour unchanged. Never edit the composition, camera, scene generation, parser or scheduler to make a test pass.
E. Diff review: read the full diff of every changed file; every file in scope; no formatting churn, debug code, temporary preview code, unused imports, abandoned implementations or old default path; the new character is the active default; restore any out-of-scope changes made by tools (never discard pre-existing user work).

## 8. ERROR PREVENTION
No broad search-and-replace across the repo. No rename/delete of shared exports without tracing callers. No edits to unrelated files to make this easier. No standalone demo disconnected from the production path. No unused character files declared complete. No old and new design active together. No design change to compensate for a camera or environment issue, and no camera or scene change to compensate for a character geometry issue (fix the character itself). No hidden failing tests, no suppressed errors. No new libraries or manifest edits. No nondeterminism. No deleting or overwriting user changes. No claim of guaranteed zero errors. Use small steps; validate after each; diagnose causes instead of layering workarounds.

## 9. SEQUENCE
Phase 1 locate and understand (path, call sites, names, baseline, minimal file set) -> Phase 2 spec to checklist (map each requirement to code; list old-vs-new conflicts) -> Phase 3 replace in place (head, face, neck, torso, limbs, hands, wristband, sneakers, backpack, pivots; keep API and compatible controls) -> Phase 4 validate (instantiate, tests/types/lint/build, previews if possible, multiple views and poses) -> Phase 5 review scope and regression (full diff) -> Phase 6 report.

## 10. FINAL REPORT (honest, short, plain English)
Files changed and why; how each part of the spec was implemented; any adjustments to the spec's numbers; checks actually run and their results (pre-existing failures separate); checks that could not run and why; remaining limitations; out-of-scope integration needs with the minimal action required. Never say visual verification happened unless it did.

## 11. ACCEPTANCE (all must hold, else do not declare success)
Repo inspected before edits; active creation path located and modified; spec reflected in real 3D construction; old appearance gone from the active default; no duplicate or fallback old design; real reusable 3D geometry; proportions, face, materials, accessories and left/right match the spec; one model works from every view; rig and compatible animation controls still work; public interface preserved where possible; only approved character files modified; relevant checks run and reported accurately; final diff has no unrelated changes; every unverified item and blocker disclosed. If a criterion cannot be met: finish the safe work, say what remains, why, and the minimal next step.

## 11b. CAST PARAMETER
Other people share the same factory and rig through an optional cast card whose default is the main (CHARACTER-CASTING-v1 section 11). Never a second competing character implementation; the crowd/NPC scene system is out of scope unless truly shared.

## 12. HOW THIS CONNECTS TO THE BRAIN
Look and numbers: CHARACTER-BRAIN-v2.md. Verbatim spec: CHARACTER-SPEC-v2.md. Movement: PERFORMANCE-LAYER-v1.md. Determinism and validation habits: CINEMATIC-INTELLIGENCE-v1.md sections 8 and 10. Limit safety while building: PRODUCTION-RESUME-PROTOCOL-v1.md. Any conflict found goes to ITERATION-LOG.md and to Salman.
