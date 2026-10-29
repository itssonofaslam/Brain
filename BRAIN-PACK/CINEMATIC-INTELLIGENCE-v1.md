PROGRESS: complete v1 (sections 1-16), 2026-10-29. Sections 14-16, the music lines in section 9 and the extra fields in section 11 were added the same day after two gap checks against the source file. Source: Brain_Cinematic_Intelligence_Complete.txt. Where this file disagrees with an older library, THIS FILE WINS (owner instruction 2026-10-29); the older sections were edited to match and the originals are in old/*.before-cinematic-upgrade.md.
# CINEMATIC INTELLIGENCE v1 (the coordinating layer: story, performance, space, camera, sound, time)
Purpose: make the director think like a coordinated film crew (director, cinematographer, editor, animator, technical director), not a shot-sequence generator. One scene is ONE system: narrative intent drives performance, staging, camera, sound and timing together. The brain plans first, validates, then writes the shot list and chapter code; the renderer only executes the validated plan.
Measured rules (SHOT-GRAMMAR v1-v3, MASTER-SPEC, letterbox, locked-camera default, no overshoot) stay. This file adds the reasoning on top and replaces any older rule that conflicts.

## 1. THE PURPOSE TEST AND THE PRIORITY LADDER
Ask of every important shot, move, gesture, reaction, effect, sound cue and cut (answer in one line in the shot reason; no long deliberation saved in files):
1. What story or emotion does it serve? 2. What does it show or hide? 3. Why is it better than the simpler option? 4. What must character, camera, world and sound do to make it work? 5. Start state, action, end state, timing? 6. Does it keep continuity with the shots before and after? 7. Can the renderer do it reliably (parallax budget, plates, rig channels)? 8. If removed, is the story less clear? If not, it is ornament: remove it.
Priority ladder (a lower item never overrides a higher one):
1. Script fidelity and story correctness. 2. Continuity and physical intelligibility. 3. Readability of the primary action. 4. Emotional and directorial intent. 5. Composition, camera movement, pace. 6. Atmosphere and optional flourish.
Locked camera, a plain cut, or an unembellished action is often the strongest choice. "Cinematic" never means constant movement.
Candidate check: for an important beat compare 2-3 treatments in your head, pick one, log only the decision label and reason.

## 2. DRAMATIC BEATS AND INTENT
A beat is a unit of meaning, not a sentence. Do not make one shot per sentence; do not expand a simple action into extra beats when pace is tight.
Beat parts (use only those the moment needs): setup/orientation, intention/preparation, action start, main action, impact/consequence, recognition, reaction, hesitation/decision, reveal, escalation, resolution/settling, transition into the next beat.
Intent (one PRIMARY per beat so camera and acting do not compete): establish geography, introduce a character, reveal a clue, show status/power, show an action clearly, build suspense, provoke a reaction, show vulnerability, deliver comedy, create intimacy, show scale, change expectation, move to the next beat.
Also note: what the audience must know now, what must stay hidden for now, desired distance (detached, intimate, involved, vulnerable, powerful, uncertain).

## 3. STAGING AND GEOGRAPHY (before coverage is chosen)
- For each place that needs it, write a one-line staging note in the video state: who stands where, doors/windows/furniture/props, paths, hazards, off-screen sources. Use our plate coordinates (x,y in percent of frame, ground y range from the Light Card; world "forward" = camera-facing direction of the master plate).
- Axis: for talk and directional action fix the line (180 degree rule). Crossing it needs a motivated move or a neutral shot.
- Screen direction: a mover keeps the same screen direction across cuts unless a neutral shot or a visible turn changes it.
- Eyelines: a character looks AT the real position of the person/object; reverse shots match the established setup; a look off-screen is answered by what is in that direction.
- Off-screen space: the world continues beyond the frame. A sound source, entrance or exit keeps one side (note it, e.g. "door = frame left, off-screen"); the next shot may not move it unless the camera moved.
- Never sacrifice clarity of geography for a dramatic angle.

## 4. WORLD STATE (objects remember what happened)
Track every important entity (character, door, held object, light, vehicle, chair) in the video STATE: id, place/plate, position (x,y,layer), attached-to (hand, ground, table), state (open/closed, held/on table, on/off, intact/broken), visible/occluded/off-screen, last event.
An event changes state; later shots obey it until another event reverses it. Cameras and cuts never reset objects. Each shot line lists the entities it uses and their state at the shot start (see section 11).
One copy of the state per video: the STATE file / state.json, not repeated in shot text.

## 5. CAUSE-AND-EFFECT CHAINS (event frames)
Write significant interactions as a chain with a frame for each link (frames inside the shot, integers on the global clock):
- Door: eyes to handle -> hand reaches -> CONTACT frame -> handle turns (if drawn) -> door rotates round its real hinge side -> arm/torso take the force -> door stops at its limit (small settle) -> hand releases or holds -> door STATE = open.
- Drop: hand opens at RELEASE frame -> object leaves the hand -> gravity fall (PERFORMANCE section 9) -> CONTACT with surface (sound hook, dust if heavy) -> rests at a new position -> STATE = on floor.
- Pick up / carry / release: look at object -> reach -> fingers wrap -> ATTACH frame (object follows the hand exactly) -> carry with weight lean -> RELEASE frame -> new parent.
- Reaction to sound/event: only characters who could see or hear it react, each after their own delay (section 8 of PERFORMANCE); direction of gaze = real source.
No full physics engine: use authored curves, simple contact checks, and the plate scale formula. If the rig cannot show exact contact, use a stable approximation and choose a framing that does not expose the gap.

## 6. PERFORMANCE AND CAMERA ARE PLANNED TOGETHER
- Choose the action and the framing at the same time, then check the required action is VISIBLE in that framing: a finger pressing a button in a macro needs only the hand and the button; a room crossing in a wide needs the full walk and a correct path.
- Primary action = clear timing and composition. Secondary motion supports it. Ambient motion stays tiny or is omitted when it competes (PERFORMANCE section 1a). Stillness is allowed and can be the point.
- Camera may start a few frames before the action (anticipation), a sound may precede a reveal, eyes move while the hand finishes: overlap is allowed when planned, never a collision of incompatible states (hand opens before the object can fall).
- Infer only the connective movement the script strongly implies (turning to speak, stepping toward a door). Never invent plot-changing actions, motives, dialogue or reactions. When unsure, choose the more conservative version.

## 7. ONE TIMELINE (frame units)
- 24 fps; every time is an integer frame on the global clock; convert seconds only with frame = round(ms / 1000 x 24).
- Range convention for ALL our files: start_f inclusive, end_f exclusive; the next shot starts at the previous end_f; length = end_f - start_f. Check shot boundaries for off-by-one errors.
- Every beat shares one timeline for: shot start/end, action start/end, contact/event frames, camera move start/end + easing, gaze and expression changes, object/door events, text on spoken word, sound cue frames, cut and transition points, deliberate overlaps.
- Shot length by need: action complexity, time to read a reveal or reaction, emotion, total runtime. A tiny insert can be 6-12 f; a quiet hold long. Not so short that the key information cannot be read; not longer than its value unless the awkwardness is intended (existing DIRECTOR-BRAIN limits still apply: no more than about 10 s without a new action or camera move).
- Easing by purpose: gentle in-out for considered moves; faster start for urgent or startled moves; controlled ease-out to settle the camera; hold for locked shots and pauses; gait cycles for walking. Measured rule stays: no overshoot or bounce on camera moves. A sharp profile is allowed for a startled turn, impact or comic stop but still without bounce.

## 8. DETERMINISM (chapters must render the same in any order)
- Frame N is a pure function of the plan and N. No wall-clock time, no animation loops outside the frame clock, no accumulation across frames, no unseeded randomness.
- Every random-looking thing (blinks, drift, handheld, particles, crowd offsets) uses a seed made from the entity or shot id plus the frame (or a precomputed table). Same shot id = same result in every render and every chunk.
- Seeking across a cut leaves no leftover transform from the previous shot; re-render adds no offset.
- Any simulation (falling, particles) is stepped from a known start state or precomputed, so any chunk can start at any frame.

## 9. SOUND HOOKS (the director marks WHEN; the sound brain, later, chooses WHAT)
Write each sound-relevant event as a hook in the shot line: {frame, cause, kind, intensity}. Kinds: footstep (foot contact frames from the gait), door creak/close, object impact, whoosh on a fast move, riser before a reveal, hit, UI/text pop, silence mark.
Rules: a hook exists only if the cause exists on screen at that frame (no footstep with no foot contact); do not stack more than two at one instant; silence is a choice, mark it; J-cut/L-cut = set audio_lead_f (sound begins before the cut) or audio_tail_f (sound continues after) on the cut; never place a cue that spoils a reveal or fights the mood; dialogue stays clear. Music is a cue too: it may drop away at a realization or come in on a decision, mark it as a hook (kind music-in / music-drop, frame, intensity); it must not start early enough to spoil a reveal, contradict the tone or bury dialogue; silence is not filled by default. If sound is not built yet, hooks stay in the shot list and nothing claims sync.

## 10. VALIDATE, REPAIR, FALL BACK (before any chapter code is written)
Validate the shot list (and state) for:
- missing ids or references (plate, entity, text, sound target); reversed or zero-length ranges; shots not contiguous; frames not integers;
- non-finite or out-of-range numbers (camera scale/drift beyond the parallax budget, blur, handheld level, angles);
- unsupported size/angle/move/effect codes or easing names; effects the renderer cannot do marked as executable;
- camera target or look target that is not an entity or plate point; required contact target (handle, hand, object) that cannot be resolved;
- contradictory state changes (door opened twice, object in two hands, character at two places);
- continuity breaks detectable from the data (object state jump, eyeline pointing away from its target, axis crossed with no neutral shot, screen direction flip);
- required action not visible in the chosen framing.
Repair (small, deterministic, logged): clamp numbers into the budget, snap frames to integers, extend a too-short shot, replace an unsupported code with the nearest supported one, swap in a locked camera, drop an optional effect. Never invent arbitrary coordinates or random camera moves.
If a plan cannot be repaired safely: use the safe fallback (locked camera, hard cut, simple wide or medium, no optional effects) and write a visible note in fixes.md / the shot "diag" field saying what was skipped and why. A failing optional enhancement never blocks a basic valid shot. Errors name the shot, entity, action and the rule broken.

## 11. SHOT-LIST FIELDS ADDED (all OPTIONAL; a line without them still renders with safe defaults)
Beat card adds: "intent" (primary intent from section 2), "hide" (what stays unknown), "distance" (detached|intimate|involved|vulnerable|powerful|uncertain), "stage" (staging note or id).
Shot line adds: "purpose" (one line), "events" [{"f":1240,"entity":"door1","event":"contact"}...], "state_in" {"door1":"closed","cup":"table"}, "state_out" {...}, "gaze" {"main":"door1"}, "camera_path" {"from":{...},"to":{...},"ease":"inout-quad","follow":"main:torso","lead_room":"12%"}, "sound_hooks" [{"f":1244,"cause":"door contact","kind":"impact","i":"mid"}], "audio_lead_f", "audio_tail_f", "overlap_f", "diag" (repair/fallback notes).
Defaults when missing: locked camera, no events, no gaze (idle), state unchanged, no hooks, no overlap.
More optional fields (only fields the renderer or the director really reads; never add a field the runtime ignores; refer to entities by id and never copy their transforms into shot text):
- Shot line: "framing_target" (entity or point that must be framed), "must_show" (props, hands, contact points that stay visible and uncropped), "focus" (sharp subject; optional rack target with start_f and end_f), "camera_path.bounds" (plate margin and obstacle limits), "camera_path.settle" (decay frames of the follow-through, deterministic), "actions" and "events" ids contained in the shot.
- Action track: {"entity", "type", "start_f", "end_f", "profile" or "pose_from/pose_to", "gaze", "expr_from/expr_to with frames", "contact_target", "path and speed" (locomotion), "support" (planted feet), "priority": primary|secondary|ambient}.
- Sound hook extras: "dur_f", "gain" (subtle|normal|big), "source" (entity id), "trigger" (the event that causes it).

## 12. ANTI-PATTERNS (check each shot list before sending)
- Camera moves, zooms, handheld, slow motion, close-ups or rack focus used as decoration or as a default after every line or reaction; shallow focus hiding essential information; every scene a sunset or every suspense scene blue.
- Same size/angle/move/transition repeated with no reason in adjacent shots (variation only when it clarifies; deliberate rhythm allowed).
- Confusing geography; a reaction with no cause; a whole crowd turning at the same instant; reacting to what they cannot see or hear.
- Animation noise: constant blinking, swaying, bobbing, gestures, background motion, camera jitter "to feel alive".
- Broken contact: floating hands, sliding planted feet, object detached from the hand, door turning round the wrong edge, props teleporting between shots, limbs through solid props, camera path through solid geometry.
- Unsupported complexity: every extra a full agent, every prop a physics object. Use the minimum reliable method.

## 13. NOT TAKEN INTO THE BRAIN (they are developer workflow, not film rules)
Repository reconnaissance and baseline, code-change safeguards, test runners and lint/build checks, documentation upkeep and the engineering final report from the instruction file. The film-relevant part of its review pass is section 16. Their intent is kept where it fits: validation and repair (section 10), determinism (section 8), honest reporting (DIRECTOR-BRAIN section 10), code checklist (PRODUCTION-RESUME section 6). Code is still written by the brain while producing a video; it is rendered by Salman.

## 14. PLANNING VERSUS EXECUTION (the boundary)
- The brain (Claude) interprets the script, proposes shots, picks motion profiles and plans emotional timing. The Remotion code only EXECUTES a validated plan, the same way every time.
- Never call a language model per frame. Never improvise a new camera pose for each frame. Prefer reusable actions, explicit keyframes, splines, deterministic curves and validated state transitions.
- Natural language carries meaning and human-readable notes (purpose, reason, diag). Transforms, timeline, interactions and execution live in structured data (shotlist.jsonl, state.json, chapter data). Essential behaviour is never left only in a descriptive paragraph.
- One ranking for the whole brain (section 1). No file may tell one stage to be minimalist and another to maximise movement; if two files disagree, apply the ladder and the precedence in DIRECTOR-BRAIN section 2 and log the conflict in ITERATION-LOG.md.
- Files keep a short decision label and reason, not long private deliberation.

## 15. BACKWARD COMPATIBILITY AND GRACEFUL FALLBACK
- Existing shot lines, beat cards, state files and chapter code stay valid. All new fields are optional with safe defaults (section 11); a scene never has to fill every new field.
- Do not silently reinterpret an old field with a new meaning: a new meaning gets a new optional field. The start_f inclusive / end_f exclusive convention (section 7) matches the earlier examples (start 1224, end 1272 = 48 frames); if any older file used an inclusive end, convert it and log the change.
- A needed schema change comes with a migration note in ITERATION-LOG.md and keeps both the old and new forms valid; ids, file names, chunk names and output formats do not change without need.
- If an old plan lacks advanced camera or performance data, keep the earlier behaviour or a conservative default (locked camera, hard cut, no optional effects).
- A failure in an optional enhancement never blocks a basic valid shot; diag says which enhancement was skipped and why (section 10).

## 16. REVIEW PASS (run as a skeptical editor who did not make the plan; before sending a shot list or chapter)
Ask, fix what fails, then re-check the affected shots:
- Is camera motion there only to look cinematic? Does every important move have a purpose and a bounded duration?
- Can each follow shot handle the start, the stop, a turn and a change of speed?
- Are natural character movements visible in the framing and timed well? Are gaze, head and body orientation coherent?
- Are hand/object, foot/floor and door/hinge contacts plausible where they matter? Are object states kept across cuts?
- Do secondary characters and crowds react only when they could see or hear the cause?
- Can camera motion, character motion, object events and sound hooks drift out of sync? Are all frames integers on the one timeline?
- Is every value deterministic under seeking and non-sequential rendering? Can any value be NaN, infinite, out of budget, or point at a missing target?
- Do fallbacks show in diag, rather than silently changing the story?
- Did the plan change anything unrelated, or delete valuable older instructions or knowledge? (When editing brain files, keep the original in old/ and diff it.)
- Do old inputs still work? Does the plan really reach the shot list and chapter code (nothing written but never used)?
- Did I run every check I say passed? Unrun means unverified, say so.
