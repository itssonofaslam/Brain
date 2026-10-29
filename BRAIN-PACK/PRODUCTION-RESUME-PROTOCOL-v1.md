PROGRESS: complete v1 (sections 1-10). Cinematic-intelligence upgrade applied 2026-10-29 (sections 4, 6, 9; original in old/). Next: Salman stress-test feedback.
# PRODUCTION RESUME PROTOCOL v1 (batch B6, 2026-10-28)
Purpose: while PRODUCING a video (not building the brain), a usage limit, a compaction, a new chat, a wiped workspace or a dropped Colab session must never lose work or force a restart. Hardest rule (Salman): bullet proof. Everything lives in files and memory; the chat is disposable.
Facts this protocol respects: this workspace cannot run Remotion (npm blocked), so Claude writes the project files and Salman renders on Colab or his laptop; one render per video; frame = round(ms / 1000 x 24); chapters on one global frame clock (from the earlier explainer work); handoff note after each chapter; join-check stills.

## 1. THE FIVE LAWS
1. Nothing important lives only in chat. Every decision is written to a file within the same turn.
2. Write small: no single file write over about 150 lines; each file has a PROGRESS line at the top; each shot or section in a file ends with a DONE marker.
3. One STATE file per video (max 3 KB) says exactly what to do next. Read it first, always.
4. A pack zip of the whole video folder is rebuilt and SENT to Salman after every stage and every chapter. He is the backup.
5. A tiny mirror of STATE lives in memory (/areas/video-<slug>.md, max 2 KB), so even an empty workspace knows where to resume.

## 2. VIDEO FOLDER (per video; slug = short-name-yyyymmdd)
/home/claude/stickman/videos/<slug>/
- STATE.md (live status, next action, open items, decisions; max 3 KB)
- script.txt (from the script brain) and timing.json (word timing, ms)
- palette-note.md (per-video palette and recurring devices)
- shotlist.jsonl (one JSON line per shot: id, start frame, end frame, beat, size, angle, move, handheld level, lens/blur, light recipe, plate id, effects, transition, text, reason, status)
- plates/registry.jsonl (WORLD-PROMPT-WRITER plate registry), plates/P01.png ... (Salman's images), plates/depth/P01.png (depth maps), plates/lightcards.md
- characters-invented.md (every invented person, creature, prop with look and behaviour)
- chapters/ch01.tsx ... plus ch01.handoff.md for each (chapter code and its handoff note)
- render/chunks.json (render chunk list and status), render/chunk_000.mp4 ...
- checks/ (join-check stills, test frames)
- fixes.md (every fix Salman asks for, sorted brain-wide vs this-video-only)
- VIDEO-PACK-<slug>.zip (rebuilt after each stage; sent)
IDs are stable and never reused: shots s0001..., plates P01..., chapters ch01..., chunks c000...

## 3. STAGES (each stage ends with: update STATE, update memory mirror, rebuild zip, send)
S0 Intake: script + timing file arrive; save both; compute duration and frame count; write STATE.
S1 Shot plan: build shotlist.jsonl in sections of at most 30 shots (about 1 minute). After each section: mark section DONE in STATE. Use CAMERA-SHOTS-LIBRARY decision engine v4; record the reason per shot.
S2 Plate requests: from the shot list, group shots by place, write the world bibles and plate prompts (WORLD-PROMPT-WRITER). Output a "PLATE REQUEST SHEET" for Salman (plate id, prompt, what to attach, file name). He generates images at his own pace (asynchronous); STATE shows which plates are received.
S3 Plate check: for each received plate, run the check, fill the Light Card, mark checked or ask for a redo; create depth maps (tool decided in the Remotion test: Colab depth model). Progress per plate in registry.
S4 Chapter code: one chapter = about 20-30 shots or about 60 seconds, whichever is smaller; one file per chapter (under about 400 lines), importing shared brain components and the global frame clock. After each chapter: write chNN.handoff.md (what is built, which shots, which plates, which components, known issues, next chapter's first frame), run the code checklist (section 6), update STATE, send chapter + handoff + pack.
S5 Join check: for every chapter boundary and every plate change, specify a still frame to render (Salman renders them with one command), compare light, grade, character size.
S6 Render in chunks (section 5).
S7 Review: Salman is the eyes; every note goes to fixes.md and is sorted: brain-wide fix (goes into the brain files, applies to all videos) or this-video-only fix. Do not apply until he says build.
S8 Final: full render check, final pack, close the video in memory.

## 4. STATE.md TEMPLATE (max 3 KB)
```
VIDEO: <slug>   TITLE: <working title>   FPS: 24   LENGTH: <s> / <frames>
STAGE: S<n> <name>   LAST UPDATED: <date time>
NEXT ACTION (one line, exact): <e.g. "write shots s0031-s0060 into shotlist.jsonl">
DONE: S0 yes | S1 sections 1-3 of 8 | S2 no | ...
PLATES: received P01 P02 | checked P01 | missing P03...
CHAPTERS: ch01 done | ch02 in progress (shots s0021-s0043 done, s0044 next)
RENDER: chunks 0-4 done, 5 failed (reason)
OPEN QUESTIONS FOR SALMAN: ...
DECISIONS THIS VIDEO: ...
ENTITY STATE: see state.json (per entity: id, place, attached-to, state, visible, last event); keep the long list out of STATE.md
```
Memory mirror /areas/video-<slug>.md: 6-10 lines copied from the top of STATE.md (stage, next action, folder, plate status, where the pack zip is).

## 5. RENDER IN CHUNKS (Colab or laptop; one final video, but safe)
- The chapters are one composition on one global clock. Rendering is done in chunks of about 600 frames (25 s at 24 fps) using Remotion's frame-range render (--frames=a-b), each to its own file chunk_cNNN.mp4 with identical settings (codec, CRF, size). Chunks are recorded in render/chunks.json with start frame, end frame, status (todo, running, done, failed), file size and checksum.
- A resume script skips chunks whose file exists, has the expected frame count and non-zero size; it renders only missing or failed ones.
- After all chunks are done: concatenate with ffmpeg (stream copy, no re-encode), mix the audio once, then verify frame count and duration. The audio track is added after the picture, so a sound change never forces a picture render.
- Colab disconnects: files go to Google Drive (mounted) after each chunk; the notebook starts with "mount Drive, read chunks.json, continue".
- Laptop (i7-4600U, 8 GB): lower concurrency (2), PNG-free pipeline, same chunk method; if time is short the heavy effects (depth blur, volumetric rays, particles) are reduced first (EFFECTS section 1 cost tiers).
- One render per video remains the goal: chunking is only a safety net, with identical settings so the join is invisible. Chunk boundaries avoid cuts with transitions (start a chunk on a hard cut where possible).

## 6. CODE CHECKLIST BEFORE SENDING A CHAPTER (cannot be run here, so be strict)
- Imports exist in the project; no placeholder text; every component prop is typed.
- All times derive from frames on the global clock (start_f inclusive, end_f exclusive). Frame N depends only on the plan and N: no wall-clock time, requestAnimationFrame, setInterval, unseeded Math.random, or state carried from the previous frame; every random-looking value is seeded from the entity or shot id plus the frame (CINEMATIC-INTELLIGENCE section 8). Seeking across a cut leaves no stale transform; any simulation is stepped from a known state or precomputed so any chunk can start anywhere.
- Run the validation list (CINEMATIC-INTELLIGENCE section 10) over shotlist.jsonl and state.json before writing a chapter; every repair or fallback is noted in diag, never silent.
- Plates referenced by id exist in the registry; depth maps present; effects within the budget.
- No file over about 400 lines; no inline giant data (data goes to JSON).
- A tiny smoke test composition (1 shot) exists so Salman can test a chapter before the whole run.
- Known risks listed in the handoff note.
When Salman reports an error, record it in fixes.md with the cause and the fix, then fix the file and resend only the changed file.

## 7. WHEN THE LIMIT HITS (or the chat is compacted or replaced)
Because of the five laws nothing is lost. Recovery steps:
1. Read memory /areas/video-<slug>.md (and /areas/stickman-build-state.md for the brain status).
2. If the workspace folder exists: read STATE.md; continue at NEXT ACTION. If a file shows PROGRESS partial, continue from the last DONE marker.
3. If the workspace is empty or new: ask Salman to attach VIDEO-PACK-<slug>.zip and BRAIN-PACK-all-files.zip; unzip into /home/claude/stickman/; then step 2.
4. Do not re-read everything: read STATE.md, the last handoff, and only the files for the next action (token thrift).
5. Say one line to Salman: where we are and what happens next.
Resume prompt Salman can paste in any new chat: "Continue video <slug>. Read memory and STATE.md and carry on."

## 8. TOKEN THRIFT RULES (so limits come later)
- Short replies; no recaps of finished work; send only changed files.
- Never re-read big files or all plates; read STATE and the next action's inputs.
- Build in chapter-sized steps; the brain files are read once per session in their summary form (a 1-page BRAIN-CHEATSHEET will be generated in B7).
- Images: look at a plate once when it arrives, record the Light Card, do not reopen it.
- Large outputs (shot lists, prompts) are written to files, not printed in chat.

## 9. FAILURE TABLE
| failure | recovery |
|---|---|
| limit mid shot-list | continue from last DONE shot id in shotlist.jsonl |
| limit mid chapter | chapter file has DONE markers per shot; continue; handoff note written at start with the plan |
| limit mid plate requests | registry has status; resend the request sheet for missing plates |
| workspace wiped | attach the two zips; STATE and memory restore the position |
| memory file conflict | re-read, merge, retry; never overwrite another surface's lines |
| render chunk failed | chunks.json marks it failed; rerun only that chunk; check memory/CPU; reduce concurrency |
| Colab disconnected | remount Drive, read chunks.json, continue |
| Salman changes his mind late | log in fixes.md, mark affected shots/chapters "dirty" in STATE, redo only those |
| plate unsuitable | redo prompt; only the dirty shots rebuild |
| error from his render | record, fix, resend the changed file only |
| shot line fails validation | repair deterministically (clamp, snap, swap code); if not safe use the locked/plain fallback and write a diag note; never change the story silently |
| old shot line lacks the new optional fields | safe defaults (CINEMATIC-INTELLIGENCE section 11); do not rewrite old lines |
| object state contradiction between shots | fix state.json, mark the affected shots "dirty", redo only those |

## 10. ALSO USED FOR BRAIN BUILDING
The same laws apply to the brain build (BUILD-STATE.md and /areas/stickman-build-state.md). Production state files are separate from brain files so a video never changes the brain; brain-wide fixes from a video go into the brain files only when Salman says build.
