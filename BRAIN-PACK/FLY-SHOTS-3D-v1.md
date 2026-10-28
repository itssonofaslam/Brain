# FLY SHOTS (3D / depth-travel shots) v1 — approved by Salman 2026-10-27: "we want it, dynamic, the brain should think"
A fly shot = the camera travels through or around a big space (push through a street, rise over clouds, orbit an arena, tilt up a tower) so the viewer feels depth and scale. Not a fixed quota: the brain decides from the script whether space itself is the story.

## 1. Two ways to build it (brain picks per shot)
A. Depth-layer fly (default, cheap, matches our references): painted layers at different depths (sky 0.1-0.2, far skyline 0.3-0.4, back wall 0.5-0.6, floor/props 0.8-0.9, hero 1.0, blurred foreground 1.5-1.8), camera path moves/zooms so layers slide at different speeds, plus drifting fog and particles and foreground objects passing for the feeling of travel. Works for: rising over clouds, push toward a city, pull out from a hero, tilt up towers.
B. True 3D scene (rare, only when the perspective itself must change): a simple low-poly flat-shaded scene in the same palette (buildings, towers, stadium bowl, ground, sky gradient, fog, one key light, bloom), the camera on a keyframed path or orbit, then the SAME colour grade, 41 px bars and grain as every other shot. Built with a three.js layer inside Remotion. Works for: orbit around an arena or table, fly down a street canyon, circle a floating city. Heavier to render (WebGL); to be timed in the Remotion test (T1-T5), only when Salman says go. Plugin note: no-GPU machines need software WebGL (slow); keep B shots few and short.
Rule: use A unless a real perspective change is needed for the story beat. Keep figures flat black with rim light even in B shots (flat sprite or tiny low-poly figure); keep palette tokens from the mood so the grade matches.

## 2. When the brain should use a fly shot (decision test)
Use when the sentence is about SPACE: (1) arriving in a new world or big place; (2) a scale reveal (how small the hero is, how big the thing is); (3) flight, fall, chase or long travel; (4) an overview of a route, city, arena, map-like geography; (5) a bridge between places or times (travel through to the next location); (6) a climax where the whole arena matters.
Do NOT use for dialogue, emotion/faces, diagrams and numbers (use UI shots), small rooms, quick action, or two beats in a row.
Guards: never in a shot under about 2 s; vary the move (orbit, fly-through, rise, descend, along-the-street; never the same move twice in a row); keep the horizon level unless the script is about falling or loss of balance; at most one fly shot per beat; never two within about 60 s unless they are one sequence (flight, arrival, chase: up to 3 in a row of 2-4 s); a fly shot is followed by a ground-level shot (medium or close of the hero) within 1-2 shots to land the viewer; keep the total small.
Budget guide (dynamic, not a quota): measured in our refs, shots where the camera really travels (wide/plate/top-down with push, pull, pan or tilt, held 3 s or more): ref1 about 2 per min, ref2 1.1, ref3 0.3, ref4 0.2, ref5 0.4 (the 24-min story film: 9 long travelling wides, e.g. the flight sequence and city canyon). So: story films about 0.3-0.6 per minute, hybrid explainers up to about 1 per minute, pure explainers rarely. Plugin's "about 1 per minute" is only an upper reference.

## 3. Camera grammar for fly shots (from our measurements)
- Hold 3-6.5 s (our travelling wides: pushes about 3.2 s, pulls about 4.0 s, ref1 pull-outs 5-6.5 s). Longer than the 2.4 s locked average, because travel needs time.
- Direction means: push = approach, tension, discovery; pull = reveal scale, end of a section, farewell; tilt = height (towers, falling, rising); pan = tour of a place; orbit = "the whole thing" (arena, table, floating city).
- Easing: no overshoot, no shake. Tension push = ease-in quad 4-5 s; neutral drift = linear 2-4 s; reveal move = ease-in-out cubic 2-3 s or ease-out quad 4-7 s.
- Pair with other tricks: scale contrast (tiny hero in vast frame) + top-down for aerial; low angle for towers; backlit silhouette at sunrise/sunset.
- Enter from a cut or a short dissolve (6-14 frames; 14 frames for world crossings), usually after an empty plate; leave to a hero close-up or medium.
- Atmosphere always: fog layer, drifting particles, blurred foreground passing; one key light; glows where light sources are.

## 4. Dynamic thinking steps for the brain (per sentence)
1. Does this sentence describe size, distance, height, travel or arrival? If no, stop.
2. Is it the first time we see this place, or the big moment of the scene? If no, a plain wide is enough.
3. Did a fly shot already happen in the last 60 s (outside a sequence)? If yes, use a plain wide with a slow push.
4. Pick A or B: B only if the beat needs the camera to circle or dive through real depth.
5. Choose direction by meaning (push, pull, tilt, pan, orbit), duration 3-6.5 s, hero landing shot after.
6. Log it (shot id, method, direction, duration, reason) in the shot file notes.
Examples: "You rise above the clouds" -> A, tilt up + clouds sliding, scale contrast. "The stadium holds eighty thousand" -> A or B orbit, once. "Your heart beats once" -> no. "The jetty is forty metres away" -> plain wide, no fly. "Two years later, a new city" -> arrival: plate, fly push, hero medium.

## 5. Reference examples in our five videos (for the brain to study)
ref5: city canyon shots 80, 82, 84, 85, 99 (looking up and down a street of towers), flight sequence 169-179, aerial 164 (tilt), 501 (aerial); ref2: stadium 144, 177, 182; ref1: pull-outs 35, 55, 84. Indices are shot numbers in labelling/refN_shots.json.

Placement: strongest one at a world change or story turning point, usually in the first third (arrival) and again near 60-80% of a long film.

## 6. Open tests
- Measure depth-dependent motion (near vs far layers) in ref5 city and flight shots and ref2 stadium shots to see which method the references use; include one Method A and one Method B sample in the Remotion test when Salman says go.
- Check whether our refs build the city canyon and stadium shots as real 3D or painted perspective (look for vanishing-point change over the shot). Either way the brain has both methods.
- Time one B shot in the Remotion test (software WebGL on Colab vs laptop).
