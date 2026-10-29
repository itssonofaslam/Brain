PROGRESS: complete v1 (sections 1-13). Character replacement applied 2026-10-29 (hands with fingers, new head/face, backpack, wristband, leg length; original in old/PERFORMANCE-LAYER-v1.before-character-v2.md). Cinematic-intelligence upgrade applied 2026-10-29 (principles 1 and 5, new section 1a, sections 3, 4, 5, 6, 7, 9, 10, 13; original in old/). Next: Salman stress-test feedback.
# PERFORMANCE LAYER v1 (batch B5, 2026-10-28)
Purpose: how the stickman (and every other character) MOVES and ACTS, so the animation feels better than the competition (Salman's goal). Camera is separate (CAMERA-SHOTS-LIBRARY-v1.md). Look is separate (CHARACTER-BRAIN-v2.md). All times are at 24 fps; durations in frames (f). START values are tuned in stress tests.
Measured facts from the five references that this layer respects: no overshoot or bounce in any measured movement (0 of 213 reliable runs), element moves ease in-out (quad) 15-23 f, pops and entrances ease-out 5-18 f, fades 14-25 f, camera pushes linear or ease-in 2-5 s. The references' characters mostly hold poses; our edge is life and weight in the character. So: smooth, physical, never rubbery; settle without cartoon bounce.

## 1. PRINCIPLES (what makes it feel premium)
1. Stillness is a choice, not a failure. Idle life (section 3) is a quiet default, kept at the lowest level the shot needs and reduced or off in held, quiet, macro or deliberately frozen moments. Do not add blinking, breathing, bobbing, swaying or gestures just to make a shot feel alive (CINEMATIC-INTELLIGENCE section 12).
2. Weight: heavy things start slowly and stop with a settle; light things react fast.
3. Anticipation (a small opposite move before a big move: 4-8 f for big actions, 2-3 f for small) and follow-through (parts keep moving a few frames after the body stops), then settle.
4. Arcs: limbs and the head travel on curves, not straight lines.
5. Lead and lag: eyes move first, head 3-5 f later, torso 2-3 f after the head, feet last. This is the default order, not a law: surprise, a threat or a stylised beat may reverse it or move them together.
6. Ease in and out on everything; no linear moves except constant-speed cruising (and camera pushes measured linear).
7. Settling uses critically damped springs: reaches the target smoothly with at most about 2% overshoot on heavy impacts (landing). Stress-test whether Salman wants less.
8. Contact: feet planted do not slide; hands holding objects stay attached; shadows touch.
9. Appeal: poses read in silhouette (the ivory head is a bright ball on a thin dark stick body: keep arms away from the body line when gesturing so the silhouette reads).
10. Muted rule: the pose and face alone must tell the feeling.

## 1a. MOTION HIERARCHY AND COORDINATION (added 2026-10-29)
- At any moment name the PRIMARY action the viewer must read. It gets clear timing and composition. SECONDARY motion supports it. AMBIENT motion stays tiny or is dropped when it competes. Do not give every idle behaviour, prop and crowd member the same intensity; animate what serves the beat and what the framing can show.
- Performance and camera are planned together: a macro of a finger on a button needs only the hand and the button; a wide room-crossing needs the whole walk and a correct path. Check the needed action is visible in the chosen framing (CINEMATIC-INTELLIGENCE section 6).
- Infer only the connective movement the script strongly implies (turn to speak, step toward the door, a breath before a big line). Never add plot-changing actions, motives, dialogue or reactions; when unsure choose the conservative version.
- Gaze goes to a real target (person, object, door, sound source, a meaningful point); no staring into empty space when the scene gives a target. Two characters' eyelines and facing must match their positions; a look off-screen is answered in the next shot by what lies in that direction.
- Overlap is allowed when planned: eyes shift while the hand finishes, the head starts turning as steps slow, a sound begins before a reveal. Do not overlap incompatible states (the hand opens before the object can fall).
- Everything random-looking (blink timing, drift, crowd offsets) is seeded by the entity or shot id plus the frame (CINEMATIC-INTELLIGENCE section 8).
- Sound hooks: write foot-contact frames, door contacts, impacts as events with frame numbers; a footstep hook exists only on a real foot contact (CINEMATIC-INTELLIGENCE section 9).
- Turning toward a sound: the head (eyes first) turns to the real source position after that character's own reaction delay; eyes, then head, then torso if the source is far to the side; characters who could not hear it do not turn.
- Small corrective movements: after contact, a stumble, a surprise or a stop, add one small recovery (a half-step, a hand adjusting, shoulders resettling, a re-plant of the foot) over 4-8 f; do not repeat it as a tic. Context-appropriate reactions to others never make characters move in sync.

## 2. RIG CHANNELS (from CHARACTER-BRAIN-v2)
Body: pelvis position (x,y,z) + lean, torso lean and twist, shoulder lift x2, upper arm x2, elbow x2, wrist x2, finger pose x2 (relaxed, point, grip, open, wave; single fingers only in close shots), backpack follow (delayed spring), hip x2, knee x2, ankle x2, foot plant flags.
Head: yaw, pitch, roll (limits in CHARACTER-BRAIN section 6).
Face: brow height L/R, brow angle L/R, brow arch, eye openness L/R, eye look x/y (eyes slide over the head surface, up to about 5% of D), eyelid openness L/R (lid caps, blink, sleepy), mouth shape blend (calm, small o, wide O, down, flat, wobble, speak shapes), mouth width.
Hands have a palm, one thumb and four simple fingers (never mittens or gloves). Holding = fingers and thumb wrap the object and it attaches to the hand at an ATTACH frame; pressing and pushing use the palm, fingertips or forearm; pointing = arm extended with the index finger out and the other fingers curled; waving and open palm are available. Fingers stay in a relaxed, slightly curved rest pose unless the shot needs detail (far shots: hands are small pale shapes). The left wrist always carries the turquoise band.

## 3. IDLE LAYER (always on, even when he "stands still")
| element | behaviour | START values |
|---|---|---|
| breathing | torso scale and shoulder rise | torso height +1.2% at inhale, period 3.5-5 s (0.2-0.3 Hz); stronger when scared or running (period 1.2-2 s) |
| blink | both eyes close and open | every 3-6 s at seeded irregular intervals (not mechanical, not random per render); close 2 f, hold 1 f, open 3-4 f; sometimes double blink; blink at head turns and after big beats; fewer blinks under fear, then a rapid flutter; slow blinks (close 4 f, hold 3 f) in sadness or tiredness |
| eye micro-darts | eyes shift slightly | 2-5% of D every 0.8-2.5 s, with 3-4 f travel |
| head drift | tiny seeded sway | +-0.6 degrees yaw/pitch, slow noise |
| weight shift | change standing leg | every 4-9 s, pelvis sideways 1-2% of height, knee softens, 12-18 f ease in-out |
| finger squeeze / shoulder settle | tiny hand and shoulder changes | rare, 1-2 degrees |
Idle is hidden by bigger actions (blend out when an action starts, blend in after). Idle level follows the shot: normal in wide and medium holds, breath only in quiet held or close shots, off during a deliberate freeze or a shock beat, and only what the framing shows is animated.

## 4. HEAD AND FACE ACTING
- Head turn recipe: eyes move first; head follows 3-5 f later; torso follows 2-3 f after the head; a 30 degree turn takes 10-14 f, a 90 degree turn 16-22 f, ease in-out, critically damped settle. Add a blink during large turns.
- The face features turn with the head as one 3D assembly. The far eye foreshortens past about 50 degrees and is hidden by about 70-75 degrees; sides and back are plain ivory (CHARACTER-BRAIN section 3). So for beats where the expression matters keep turns within about 50-70 degrees toward the camera; use full side profile for posture beats (walking away, listening, looking up).
- "Face going sideways" (Salman's example): eyes dart to the side (5% of D), head yaw 25-40 degrees, a slight tilt (3-6 degrees), brows follow; the satin head catches a new highlight as it turns.
- Look-at: eyes lock onto the target within their limit (5% of D); beyond it the head turns; beyond about 40 degrees the torso turns too. The target decides the glance order (eyes, head, body); surprise or threat may synchronise or reverse it. The target must be a real thing at its real position (section 1a).
- Nod: pitch +8-14 degrees, 8-10 f down, 8-10 f up; shake: yaw +-10-18 degrees, 3 swings, 14-20 f; tilt for curiosity: roll 5-10 degrees; head down for shame or sadness: pitch 12-20 degrees, held; head up for awe: pitch -10-20 degrees.
- Double-take (shock): look away, 6 f pause, snap back with wide eyes (eye openness 1.2) and brows up, 4 f; brows lead the mouth by 1-2 f.
- Expression change: blend parameters over 4-10 f (quick for shock 3-4 f, slow for mood shift 12-24 f); never switch instantly except for a deliberate cut-in.
- Eye catchlight stays fixed to the light (on the side facing the key light, upper right if the light is flat) while the eyes move, so the eyes stay glossy and alive.
- Speaking and listening: see section 8.

## 5. LOCOMOTION (walk, run, stop, turn)
At 24 fps. Step length measured on the leg length (hip to floor = 1.70 model units, about 1.8 head units; the legs are long and thin, so steps read long and light).
| gait | full cycle (two steps) | step length | pelvis bob | arm swing | torso lean | notes |
|---|---|---|---|---|---|---|
| slow / sad walk | 30-34 f | 0.5 x leg | 0.8% of height | 8-12 deg | forward 2 deg, head down | drags feet slightly |
| normal walk | 24 f | 0.7 x leg | 1.2% | 18-22 deg | 2 deg | heel strike |
| brisk walk | 18-20 f | 0.8 x leg | 1.5% | 25 deg | 4 deg | |
| jog | 14-16 f | 1.0 x leg | 2.5% | 35 deg | 8 deg | |
| run | 11-13 f | 1.2 x leg | 3-4% | 45 deg | 12-18 deg | flight phase visible, arms bent |
| sneak | 32 f | 0.4 x leg | 1% | 5 deg | 5 deg, knees bent | glances |
| scared walk | 14-18 f | 0.5 x leg | 1.5% | small, shoulders up 8 deg | back lean | fast short steps, head turns |
| tired | 34-40 f | 0.5 x leg | 1.2% | limp | 5 deg | heavy plants |
- Speed on screen = step length x 2 / cycle seconds; the feet must be planted during stance (world speed of a planted foot = 0). The brain computes speed from the gait and the plate scale (WORLD-PROMPT-WRITER scale formula), never the other way round (no foot sliding).
- Arm swing opposite to legs; torso counter-twists 3 degrees (walk) to 8 degrees (run); head stays steadier than the pelvis (bob reduced 50%).
- Start: lean first, first step after 4-6 f; stop: last step plants, body settles over 8-12 f with a small lean back.
- Turning while walking: head and eyes lead by 4-6 f, then the body arcs round (not a pivot on the spot) unless he stops.
- Running toward camera: scale grows with distance; add camera push and H4 handheld (CAMERA-SHOTS-LIBRARY section 8).
- Hands: fingers stay loose and slightly curved in walking, tighter (not a clenched mitten) in running; the arms swing thin and straight-ish, the left wristband swings with the arm.
- Sneakers are chunky with thick off-white soles: toes lift slightly at the swing, heel plants first in walks, ball first in runs; the whole shoe rotates with the foot; soles never sink or float. The backpack lags the torso by about 2-4 frames and settles, subtle and deterministic.
- Foot-contact frames are events: write the frame of each foot-down from the gait table so shadow, dust, camera (foot follow) and sound hooks line up. Planted feet do not slide unless a slide or slip is the event.
- Also plan, coherently and without new numbers beyond the table: acceleration and deceleration at start and stop, a side-step (torso keeps facing the target), reversing direction (stop, plant, pivot, then go), stepping over or round an obstacle (look at it first, plan the path), and a change of speed (change the gait row, not the playback speed).

## 6. ACTION RECIPES (anticipation, action, follow-through, settle)
| action | anticipation | action | follow-through / settle |
|---|---|---|---|
| jump | crouch 6-8 f, arms back | launch 3 f; airtime = 2 x sqrt(2 x h x 1.1 / 9.8) s for a jump height h in character heights (a 0.3-height jump is about 12-13 f in the air) | land with knees bending 6 f, arms drop, settle 8-10 f, dust puff |
| fall / trip | arms flail 3 f | body rotation 10-18 f | impact, small bounce of limbs 4 f, still 6 f, then slow recovery |
| stumble | foot catch 2 f | lurch forward 6 f | catch step 4 f, straighten 12 f |
| sit down | knees bend, lean back 6 f | lower 10-14 f | settle 6 f, arms rest |
| stand up | lean forward 6 f | rise 12 f | balance 6 f |
| wave | arm lifts 8 f | 3-4 swings of 6 f each | lowers 8 f |
| point | arm lifts 6 f | hold 12-24 f, head and eyes lead | lowers 8 f |
| shrug | shoulders down 3 f | shoulders up 8-12 degrees 6 f, head tilt, brows up | hold 10 f, drop 6 f |
| pick up | knees bend, look at object 6 f | reach 8 f, fingers and thumb close around or under the object | rise 10 f, carry with weight lean |
| throw | wind-up back 8 f | forward 4 f | release, follow-through 6 f, settle |
| catch | eyes track, arms open 6 f | hands meet object 3 f | absorb with arms 6 f |
| push / pull | lean 6 f | steady force, feet dig in, slow movement | release and stagger 6 f |
| open door | reach 6 f | pull/push 10-14 f, step | pass through |
| climb | hand reach 8 f, foot lift 8 f alternating | pulls up 12 f per step | pause on rest |
| collapse / faint | sway 8 f | fold at knees 10 f | settle on ground 10 f |
| celebrate | arms rise 6 f | hands up (open or loosely closed), small bounce 12 f | settle |
| crouch / kneel | weight shifts back over the heels, eyes go to the target, knees begin to bend 4-6 f | lower with balance (a hand on the knee or the ground); a kneel puts one knee down after the lead foot | hold with a slight forward lean; rise by pushing through the legs, 10-12 f |
| lean (on a wall, table, rail) | step to the support, weight shifts toward it 6-8 f | shoulder or forearm meets the surface (a contact frame), the opposite leg relaxes | settle into the support; leave by pushing off first |
Hands: fingers and thumb grip by wrapping around handles or press with the palm; objects bigger than one hand are held against the body with both forearms.
PHASE TEMPLATE for any meaningful action (use the phases the beat needs; a tiny gesture needs few): 1 preparation/anticipation (attention, weight shift, reach) -> 2 initiation (a plausible leading part) -> 3 main action -> 4 contact/event frame (hand meets handle, foot lands, door reaches its stop, object caught or dropped) -> 5 follow-through -> 6 recovery and balance -> 7 secondary response (gaze, face, breath, a small adjustment that shows the result). Write the contact/event frame as an integer on the timeline.
Body mechanics: a far reach shifts weight and may use the opposite arm for balance; a push puts the palm or forearm on the door and passes force through arm and torso; a sudden stop does not freeze every part on the same frame; a jump has take-off, air and landing response. Causal chains for doors, drops and carrying: CINEMATIC-INTELLIGENCE section 5.


## 7. EMOTION ACTING (pose + face + tempo; the muted test must pass)
| feeling | posture and body | face | tempo / idle changes |
|---|---|---|---|
| calm | upright, relaxed shoulders, arms loose | calm brows, small soft mouth | normal idle, slow breath |
| fear | torso leans back, shoulders up 8-12 deg, arms pulled in, knees slightly bent | brows up inner ends up, eyes wide (1.15-1.2), small wobbly mouth | fast shallow breath, few blinks then a flutter, eye darts toward the threat, tiny tremble (0.5 degree at 8-10 Hz) |
| awe | head up 10-20 deg, arms slightly out, body still | brows high arched, eyes wide, round O | slow breath held, blinks rare, very slow sway |
| sadness | head down 12-20 deg, shoulders drop, arms hang | inner brow ends up and lowered, small down mouth | slow everything, slow blinks, long holds, sighing breath |
| joy | chest up, small bounce, arms open | raised brows, bright wide eyes, smile curve | quick, springy, more blinks, bounce 2-3% |
| anger | forward lean, shoulders square, hands tight | brows angled down toward nose, eyes narrowed 0.9, flat mouth | sharp fast moves, held tension, little idle sway |
| shock | freeze, small back jerk 2 f then still | eyes widest, brows jump, mouth open | stop idle for 6-12 f, then one big breath |
| determination | chest forward, feet set, head level | brows angled down, eyes steady, flat mouth | still body, slow deliberate moves |
| confusion | head tilt 8-12 deg, one shoulder up | one brow up, one lower, mouth small off-centre | eye darts between things, slow nod no |
| relief | exhale, shoulders drop 8 deg, torso sinks 2% | brows relax up, eyes close in a long blink, small smile | long exhale 20-30 f |
| exhaustion | slumped, head heavy, arms hang, knees soft | half-lidded eyes (0.75), flat mouth | slow, drift in and out, heavy plants |
| embarrassment | shoulders in, head down and turned away, hand rub | brows up inner, small wobbly smile | quick small movements, looks away and back |
| curiosity | lean toward the thing, head tilt, one arm slightly out | brows up, eyes bright, mouth small o | slow steps, head moves around the object |
| guarded | torso turned slightly away, arms close or crossed over the body, weight on the back foot | brows level or slightly lowered, eyes steady, mouth flat and small | few movements, slow blinks, watches without committing |
| hesitant | weight rocks between feet, a half-step forward then back, hand rises and stops | brows pinched up at the inner ends, eyes flick between target and exit, small mouth | stop-start tempo, pauses before moving, shallow breath |
| alert | upright and still, weight forward on the balls of the feet, head up | eyes wide, brows raised a little, mouth closed | idle drops to almost nothing, quick small head turns toward the source, held breath |
| ashamed | shoulders in, head low and turned away, arms close, small body | brows up at the inner ends and lowered lids, mouth small and down, gaze avoids the other character | slow, tries to take up less space, glances then looks away |
Rule: change at least two of (posture, face, tempo) when the feeling changes, so it reads at wide shot size too (posture and tempo) and at close shot size (face).
Expressions evolve: gaze, brows, mouth, head angle and posture change in small coordinated steps (never an abrupt pop except a deliberate cut-in) and never overplayed. Realisation = gaze fixes, movement briefly drops, face changes, then a decision starts. Fear = attention locks on the threat, posture stiffens or backs away. Relief = tension releases gradually (shoulders and hands settle, not an instant happy pose). Comedy = stillness, delayed reaction, a glance or a deadpan hold can beat large movement. Use only the channels in section 2; if the rig cannot show an expression, use the nearest supported one and log it in diag.

## 8. DIALOGUE ACTING
Words come from the script brain with timing (word timing file at 24 fps). The director acts them.
- Speaking: mouth driven by the syllable timing: three shapes (closed, small o, wide O) switching on syllable peaks, about 6-9 changes per second at normal speech, scaled by emphasis; mouth width follows vowel (wide for ee, narrow for oo). Stressed words add a head nod of 1-2 degrees, a brow lift of 1-2 f, and sometimes a small finger or shoulder move. The mouth always returns to the emotion's resting shape between phrases.
- Listening: tiny nods on the speaker's pauses, eyes on the speaker, a blink on the speaker's emphasis, one bigger reaction (brows, head tilt, step back) at the key line.
- Turn-taking: the listener begins to breathe in 6-10 f before speaking; a 4-8 f pause before an emotional reply; interrupting = overlap of 6-12 f.
- Gestures: raised closed hand (emphasis), open arm (explain), point, shrug, head shake; one gesture per sentence at most; arms are thin, so keep gestures away from the body line so they read in silhouette; use finger poses (point, open palm, wave) in medium and close shots.
- Eyelines: toward the other speaker, slightly off lens; fourth-wall look into the lens only for a deliberate beat.
- Narration-only shots: no mouth movement (the narrator is a voice); characters in the scene act without lip movement unless they are the speaker in a dialogue beat.
- Voice per character: constant narrator voice per channel; different character voices per video (sound brain later).

## 9. WEIGHT, PHYSICS AND CONTACT RULES
- Gravity: treat the character as about 1.1 m tall; use g = 9.8 m/s squared for thrown, fallen and jumping things; falling objects accelerate; thrown objects follow a parabola; light things (paper, leaves) use heavy drag.
- Bounce: small damped bounce only on hard hits (coefficient about 0.2-0.35); no cartoon bounce.
- Mass feel: heavy objects start slowly, stop slowly, shake the camera a little on impact; light objects react instantly.
- Contact: feet planted; hand-held objects follow the hand exactly; sitting bodies sag into chairs by 1-2%; shadows touch on contact and separate during jumps (shadow stays on the ground, smaller and fainter with height).
- Collisions: one fast frame of compression then a settle; dust and debris per EFFECTS section 11.
- Momentum: a runner who stops slides 2-4 f and leans back; a turning runner leans into the turn.
- Contact safeguards: hands meet the real handle or object; feet meet the floor at contact; objects never teleport between hands or surfaces; accessories (backpack, hat, bag) stay attached through every move; limbs do not pass through major solid props; characters do not overlap in impossible places. If the rig cannot achieve exact contact, use a stable approximation and choose a framing that does not expose the gap.

## 10. BACKGROUND PEOPLE AND CROWDS
- Same stickman design language (sphere head, slim body), lower detail with distance, always slightly blurred and darker; head in shadow.
- Variation: height (0.85-1.15), build, speed (walk cycles 20-30 f), outfit shapes, head tint; offset each person's cycle phase with a seeded value so nobody walks in sync.
- Behaviour: pedestrians avoid each other, walk in pairs or groups, stop to look at big events with a reaction delay of 0-20 f each (the closest react first), step back, point, run away.
- Individuals, not a mass: only people who could see or hear the event react; each reacts differently (glance, pause, step aside, turn, carry on) and at its own delay; far people react later or not at all; never everyone turning to one point on the same frame. Variation is seeded and staggered. Background people never steal attention from the main character or do anything the script contradicts; when the story does not need detail keep them restrained (simple loops, low cost) and do not claim a simulation.
- Crowds (stadium, protest, market): rows reacting in waves (delay proportional to distance), occasional flicker of phones or flags; distant figures are a simple loop.
- Never the same figure twice close together; never all moving at the same speed.

## 11. INVENTING PEOPLE, CREATURES AND OBJECTS IN OUR STYLE
Looks for people come from CHARACTER-CASTING-v1.md (read the script, strip the main's kit, cast kit, cast card, crowd tiers). This section keeps behaviour, creatures and props.
Protocol: role and story function -> silhouette (height, build, head size) -> head tint -> one costume piece in clean simple shapes -> one signature behaviour -> check beside the main character.
- People: doctor (coat shape, taller, calm slow moves), child (head about 30-35% of height, smaller, quick), elder (hunched, slow, dusky head tint, drooping brows), stranger (generic dark coat), athlete (lean, quick), soldier, worker, crowd member.
- Head tints differ: warm ivory (main, #F1E3D8), pale cool, tan, dusky brown; the main character alone has the exact spec design (ivory head, turquoise left wristband, black daypack, white-soled sneakers).
- Creatures: same stick-body language plus one distinctive feature (ears, tail, wings) built from soft rounded shapes with the same subtle rim light; a face on the head if they speak, otherwise two glossy oval eyes.
- Objects and props: bold simple shapes with real materials (glossy, matte, metal, glass), soft bevels, warm rim light, no tiny text or fine detail that would break at distance; scale correctly against the character (unit = his height, 4.0 model units).
- Check: would this fit next to the character on the sheet without looking from another film? If not, simplify or restyle.
- Log inventions in the video state file (name, look, behaviour) so they stay consistent across shots.

## 12. TIMING AND EASING QUICK TABLE (24 fps)
| move | frames | ease |
|---|---|---|
| small gesture | 8-14 | ease in-out quad |
| arm raise/lower | 6-10 | ease in-out |
| head turn 30 deg / 90 deg | 10-14 / 16-22 | ease in-out, damped settle |
| blink | 6-8 total | fast close, slower open |
| expression change | 4-10 (shock 3-4) | ease in-out |
| entrance / pop-in | 5-18 | ease-out |
| fade in/out | 14-25 | ease in-out |
| weight shift | 12-18 | ease in-out |
| step cycle | see section 5 | constant with planted feet |
| settle after stop | 8-12 | critically damped |
| start moving | lean 4-6 then step | ease-in |

## 13. STRESS TESTS, QA AND OPEN ITEMS
Stress tests for Salman (judged by eye in the first real render): idle life (does he feel alive standing still?), head turn with the far eye disappearing correctly, walk with no sliding, run toward camera, jump and land, fear to relief transition, dialogue between two characters, crowd reaction, hand and finger object interaction (holding, pointing, pushing), backpack follow, invented doctor next to the main character.
QA: Is stillness used on purpose, and is ambient motion kept below the primary action? Is the primary action visible in the framing? Is every random-looking motion seeded? Do contact frames exist for hand, foot and object events? Do eyes lead the head (unless the beat reverses it)? Feet planted? Any rubber or cartoon bounce? Does the pose read as a silhouette? Does the feeling read muted? Do background people differ and move out of sync? Do invented characters match the style?
Open items (need real animation tests, cannot be settled in text): exact walk timing feel on the tall thin proportions, how much settle overshoot Salman likes (0-2%), lip-sync amount, how the eye surfaces look at 60-90 degree turns in real 3D.
