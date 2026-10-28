# REF2 mp4 FINDINGS (measured, 2026-10-26) - CORRECTS my earlier "same flat family" verdict
Format: 1280x720, **24 fps** (not 30), 10,389 frames, 432.79 s, H.264 ~375 kbps + AAC 44.1k stereo. Letterbox 41 px top + 41 px bottom (identical to ref1; content 638 px).
=> Remotion for ref2-style: fps = 24 (cheaper to render: 20% fewer frames).

## Look verdict (after seeing real frames, see ref2-move-shots-montage.png)
HYBRID: (a) ENVIRONMENTS are perspective-correct stylised 3D-looking sets (goal frame + net in true perspective, pitch lines converging, building facade changes from flat front to side-walls-visible as camera pulls back, floor planes, depth blur), (b) CHARACTERS are flat black stick figures with thin light outline + soft dark contact-shadow ellipse on the ground, (c) CROWDS = rows of flat stick-figure sprites with arm-wave loops + camera-flash sparkle specks, (d) 2D overlays (HUD, title, score card, bursts, rings).
Parallax test (optical flow in 6 horizontal bands during moves): bands move at DIFFERENT speeds (e.g. track pan: top band -263 px vs bottom -3 px; title push: sky 0 px vs ground -145 px) = real depth-dependent motion, not a flat slide. So ref2 uses a true 3D camera over 3D-ish sets (or multi-plane with real perspective). For us: either three.js scenes (@remotion/three) with flat-shaded geometry + 2D sprite characters, OR layered 2.5D with per-layer speed (cheaper) for pans/tilts, and hard cuts for big perspective changes.

## Camera
263 candidate cut/effect frames (avg 1.6 s incl. effects; real shots mostly 1-4 s). 213 shots >= 0.5 s: 164 locked (77%), 49 with camera/in-frame motion. Real camera moves listed in ref2-camera-measured.md (title tilt/pull-back 34.5-39.9, slow zoom-out aerial 366-372.7 (zoom-idx -920 = big), slow tilt 348-355, pan along pitch 325-329, roll etc.). More camera movement than ref1 (ref1 ~20 shots had moves; ref2 ~49) = the "upgrade to 3D camera" he suspected.

## Effects frames found by brightness
Black frames: 418.04-418.12 (3 frames) and 422.17-422.50 (12 frames = 0.5 s fade to black before end card). White flash frames (>200 mean): 31.67, 236.54 (bleach), 429.21.

## Audio
Median -16.1 dBFS RMS, loudest -8.7. Digital near-silence (< -80 dB) at 350.0-351.0 s (the empty aerial stadium after the rescue = deliberate silence beat) and low points at 86-86.5, 62, 200, 230, 235, 281, 379.5, 399 s. Per-0.5 s levels in audio-rms.csv.

## TODO next (measured): easing curves of entrances/pops, palette sampling per scene (hex), per-shot cut classification (cut vs dissolve vs fade), exact burst frame counts at 24 fps, crowd loop timing, shadow geometry.

## BOARD / DIAGRAM SEGMENT (found by Salman's hint, verified in mp4) 52.2-56.9 s
Screen-on-the-lab-wall: dark navy blueprint grid panel (#0f1a2e with faint grid lines #1c2c45) framed by purple wall margins; green status dot top-left (#3fbf6a); flat-schematic runners (ghost grey runner top lane = normal person, red hero bottom lane = fast), start line + finish zig-zag bar (white blocks), progress bars left (grey vs gold #c8923a), arrows (white / orange) pop in, "=" sign pops in, then a wooden POINTER STICK (orange-brown #b5733a) slides in diagonally from bottom-right to point at the diagram (54-56 s). Right half of previous frame wipes black at 52.0 (panel wipe) into the board. Ends with hard cut at ~56.9 to lab two-shot (hero angry face reaching, examiner raising arm, sun behind window). Uses: explain a mechanism as a simplified animated diagram INSIDE the 3D world (screen on wall), same stick characters in flat schematic form.

## MICRO-DEPTH LIST (the "little things" that add depth) - noticed so far
- Foreground blurred object drifts through frame (fly at 2.9-3.8 s flies left out of focus; blurred head edge enters left).
- Bokeh discs in macro shots; sun disc + god-rays; steam wisps rising from cup.
- Window lamp flicker, crowd camera-flash specks, LED ad-board flicker, floodlight bloom pulse, sparkles twinkling at ball.
- Birds as tiny V dots in sunset sky; tree silhouettes sway; moon glow.
- Light spill: window grid light on floor, spotlight cone, gobo patches (arched windows / blinds).
- Held-pose idle: 1-2 px breathing, head tilt, blink swap (2-3 frames).
- Big out-of-focus character in OTS foreground, scene sharp behind.
- Ground contact shadow ellipse + reflection on floors.
- Dust/spark particles in light shafts.
RULE FOR THE BRAIN: every shot must contain at least 1 foreground depth element (blurred), 1 ambient motion loop, 1 light source that spills; inventor brain decides which per location (e.g. door glow in daylight, birds in a sunset sky, steam in a cafe).
