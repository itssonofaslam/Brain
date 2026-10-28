# SHOT GRAMMAR v1 - what to show, when, how close, with what physics and background (2026-10-27)
Source: contact sheets of all 5 references (every sheet viewed: ~45 sheets) + measured camera/pace/easing (PATTERNS-LOG.md). STATUS: the rules below are OBSERVED and consistent across videos, but the exact FREQUENCIES per shot size are NOT yet measured. I tried an automatic shot-size classifier (head-size detection) and checked it against frames: it mislabelled most shots (dark backgrounds, rim light), so I discarded those numbers. A labelling pass (I label one frame per shot) is the fix - see section 7.

## 1. THE DECISION ENGINE (run for every script sentence, before camera/device)
Ask in this order; the FIRST yes picks the shot.
1. NEW PLACE or new time? -> WIDE establishing, 3-5 s hold, tiny figure in a big set, one ambient loop (moon, steam, traffic lights), title tag if time jump. (ref5 sky city, ref4 apartment block, ref3 lab, ref2 stadium)
2. Does the sentence NAME an object that carries the fact/plot (phone, receipt, cake, ledger, teapot, key, photo, screen)? -> MACRO INSERT of that object filling 50-80% of frame, 1-3 s, hand enters if it is used (point/pour/knock/tap/hold). (ref4 receipt 2019, phone UNKNOWN, kettle 60 C; ref5 18 cake, teapot rings, plaque; ref3 button pad, bullet)
3. Is it a NUMBER/limit/rule/count? -> HUD punch-in or UI card (monitor fills frame), colour state at the threshold. (ref3 REACTION 10.0x, ref4 TARGET #30)
4. Is it an EMOTION beat the viewer must feel (fear, grief, shock, pride, relief, realisation, suspicion)? -> FACE EXTREME CLOSE-UP: head fills 60-100% of height, eyes/brows/mouth + tear drops, held 1.5-3 s (shock/notice) or 4-8 s (grief/love), NO zoom, no shake; then CUT to the cause or to a wide reaction. Never more than one XCU in a row; never XCU on exposition. (ref3 XCU face-offs, ref5 tears at 2:06, 8:30, 15:06, 16:30)
5. Is it DIALOGUE between two? -> shot / reverse shot: OTS with big blurred head in foreground (head 25-35% of frame) alternating with medium single; two-shot (both full height) when they act together or before a decision. Speaker's face stays on screen on the key line.
6. Is it ACTION/movement through space? -> medium/wide with a clear screen direction (left->right for "going forward"), 1-4 s; flying/falling = diagonal compositions, low or aerial angle, big pan only if the script says "chase/escape/whip" (ref5 230-242 s).
7. Is it a CONNECTION/plan/map/count? -> top-down or diagram: map, door circle, pin-board, funnel/Hollow rings, constellation of lines. (ref4, ref5 Hollow)
8. Otherwise -> MEDIUM single with idle micro-motion; vary angle from the previous shot.
Mandatory after any decision: new angle OR new size vs previous shot (no repeats), keep screen direction, put 1 micro-depth object, apply device engine (DEVICE-INVENTION-v2.md).

## 2. WHICH OBJECTS GET CLOSE-UPS (the brain's test)
An object earns a close-up only if (a) the script sentence is about it, OR (b) it will matter later (plant: pancake, plaque, receipt, pill, clock), OR (c) it changes state in this shot (lights up, fills, flips, breaks, glows). Otherwise it stays in the wide. Plant-and-payoff = close-up when planted (1-2 s, no emphasis) AND close-up again at payoff with a state change. Typical sizes: tiny objects fill the frame; hands show the action; the object stays sharp with a blurred foreground edge.

## 3. FACE CLOSE-UP RECIPE (measured visually, durations from cut gaps)
- Frame: head 60-100% height, hood/collar visible at the bottom, eyes slightly above centre, background blurred/dim, rim light on the lit side.
- Marks: round eyes with ring (shock), brows slanted down (angry), brows up-slanted + tear drops (grief), half lid (smug/sleepy), 'o' mouth (shock), small smile (relief). Blink = 2-3 frames; tear drop 6-8 frames fall.
- Timing: enter on a CUT; hold 1.5-3 s for reactions, up to 8 s for grief/love; exit on a cut to the cause (reveal) or a wide (aftermath). 1 XCU per 20-40 s in ref3; clustered at emotional peaks in ref5 (grief scenes 8:30, 14:30-16:40, 20:00-21:30).
- Rhythm rule: wide -> medium -> XCU ladder when approaching a feeling; XCU -> wide when releasing it.

## 4. PHYSICS (what the references really do; the brain should NOT simulate, it should SUGGEST)
- No squash/stretch, no bounce, no overshoot (0 of 213 measured runs). Everything eases: in-out 0.6-0.9 s; arrivals ease-out; attacks/falls ease-in 1-1.4 s; tickers linear.
- Weight is shown by POSTURE and CAMERA, not physics: heavy = slow single steps, both hands on rail, low camera, long hold, contact shadow wide and dark (ref5 stairs 0:42-0:48); light/low gravity = glide poses, capes, cloud sea below, tiny shadow, long arcs with ease-in-out (ref5 flight scenes); speed = ghost echo 2-3 copies at 25-40% + speed lines + ring ripple; impact = 1-2 f burst + ring 6-8 f; slow time = cool desaturated grade + slow approach.
- Falling/flying: figure drawn in 4-6 held key poses stretched along a diagonal path, cape/hair secondary motion of 1-3 px sway, no tumbling physics; objects glide on straight paths with a soft glow.
- Liquids/gas: kettle steam as rising soft shapes, teapot pour as a thin line with ring ripples in the cup; water = horizontal sun streaks, ring ripples on surface (ref5 lake).
- If the script's topic is physics itself (gravity, speed, mass): show it as a CONTRAST of two states side by side or one after another (Earth warm/heavy posture vs Vael cool/glide) and with a measurable label if needed (HUD number); do not animate real equations.
- Rule for invention: ask "what would a person feel and see if this force changed?" then choose posture, shadow, speed, easing and colour to show that; keep everything within the no-bounce rule.

## 5. BACKGROUNDS (what kinds exist and when each is chosen)
Kinds seen: (a) lit domestic interior (kitchen, bedroom, living room: warm wood/amber, light cones, objects on shelves, beams, stairs); (b) night exterior (street, rooftop, moonlit sky city: indigo/periwinkle, big and small moons, haze, lights on strings); (c) institutional/tech (lab, sim room, test arena, office, jail corridor: grey/navy/teal, screens, torches); (d) dark HUD/map space (navy-black with gold or teal line art: maps, folders, networks); (e) void/studio (spotlight cone on black, white void, text-only card); (f) macro/object plates (table top, phone screen, hands on a plain tone); (g) transition plates (clouds, white-out, dawn lake).
Choice rule: pick by (1) place in the script, (2) mood -> colour temperature (warm = safe/home/memory, cool periwinkle = wonder/other world, navy-black = tech/danger, brown-mauve = prison/old law, white = portal/clean/blank), (3) story function: HOME gets the most detailed set because it will be revisited (callback).
Every set = floor plane + 2 depth layers + one light source with a cone/pool + 1 ambient loop + contact shadows + foreground blur object. Re-use a set from 2-3 camera angles (wide, OTS, macro) instead of making new sets. New place not in the kit = invent: light source -> palette from mood table -> 3 depth layers -> ambient loop (MASTER-SPEC section 9).

## 6. CAN THE BRAIN INVENT ALL OF THIS? (honest status)
YES for: device choice, shot size choice, close-up objects, face close-up timing, physics presentation, backgrounds, colour, pace curve (rules above + PATTERNS-LOG + DEVICE-INVENTION-v2 are the brain's constraints).
PARTLY: exact shot-size frequencies per genre (see section 7), and how the narrator's words map to cut points (needs the word-timing file of a new video; the brain will place cuts on sentence/phrase boundaries and on the word that carries the claim; this is designed, not yet tested on a real timing file).
NOT YET TESTED: the Remotion code that implements all of this (no render test yet, by your plan).

## 7. NEXT TO MEASURE (if you say go)
Labelling pass: I tag one frame per shot (shot size, subject, new place?, emotional?) for all 5 videos from contact sheets of cut-midframes (~1,200 shots, about 50 sheets), then pair each shot with the transcript sentence (time-aligned) to get real frequencies: % close-ups per genre, how long before an XCU the emotion starts, which words trigger object inserts, average hold per size. Cost: large (many images). Do it in chunks per video, resumable, only on your word.
