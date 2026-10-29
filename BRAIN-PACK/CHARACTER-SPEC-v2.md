PROGRESS: complete. Verbatim copy of Salman's canonical character specification (received 2026-10-29). Replaces CHARACTER-SPEC-v1 (old copy in old/CHARACTER-SPEC-v1.before-character-v2.md). DO NOT EDIT THE TEXT BELOW; change only with Salman's say. The brain's working version of this spec is CHARACTER-BRAIN-v2.md; the build/replace discipline is CHARACTER-IMPLEMENTATION-PROTOCOL-v1.md.

STATUS: LOCKED by Salman (2026-10-29). Text-only spec: no image is needed or exists. It wins over the old look and over any brain preference.

---------------------------------------------------------------

PROJECT: CREATE A REUSABLE 3D STICKMAN CHARACTER FOR POV SHORT FILMS

PRIMARY OBJECTIVE

Create one complete, reusable, fully three-dimensional stickman character
using Three.js, suitable for high-quality animated short films rendered
through Remotion.

The character must be constructed from actual 3D geometry, not a flat
image, billboard, sprite, illustration, or collection of disconnected
2D shapes.

The design is a minimalist stick figure presented with the rendering
quality of a premium stylized animated movie.

The character has:
- A large, smooth, pale ivory spherical head.
- Two expressive, vertically oval black eyes.
- Small, expressive dark eyebrows.
- A small, subtle mouth.
- A very slim, charcoal-black stick body.
- Extremely thin, long, rounded stick-like arms and legs.
- Small pale ivory hands with simplified fingers.
- Chunky black sneakers with white soles and white laces.
- A compact black backpack worn on the back.
- One distinctive turquoise wristband on the character's anatomical
  left wrist.

The silhouette must remain unmistakably that of a stickman.

Do not transform the character into a human, robot, alien, animal,
superhero, toy soldier, or muscular cartoon character.

The character should feel clean, charming, expressive, slightly
quirky, and visually appealing. It must be capable of fitting into
comedy, horror, action, fantasy, emotional storytelling, and realistic
everyday situations within a stylized animated universe.

The same underlying character model must be used in every scene.


==================================================
1. COORDINATE SYSTEM AND MODEL DIMENSIONS
==================================================

Construct the character in a consistent local coordinate system.

- Y axis: vertical, pointing upward.
- Z axis: forward-facing direction.
- X axis: horizontal.
- Character's face points toward local +Z.
- Character's anatomical left is local +X.
- Character's anatomical right is local -X.
- The character stands on a floor at Y = 0.

When the character faces the camera directly from the front, the
turquoise wristband on its anatomical left wrist appears on the
viewer's right.

Use the following normalized measurements as the initial model
dimensions. Treat them as a consistent character-design specification,
not unrelated suggestions.

Total character height, from the floor to the top of the head:
approximately 4.0 world units.

HEAD
- Head center: approximately (0, 3.54, 0).
- Head width: approximately 0.94 units.
- Head height: approximately 0.94 units.
- Head depth: approximately 0.88–0.92 units.

TORSO AND NECK
- Shoulder level: approximately Y = 2.74.
- Pelvis level: approximately Y = 1.70.
- Torso length: approximately 1.04 units.
- Neck length: approximately 0.30 units, with slight overlap into
  the head and torso to avoid visible gaps.

ARMS
- Shoulder pivots: approximately X = ±0.20, Y = 2.72.
- Elbow level in a relaxed standing pose: approximately Y = 2.15.
- Wrist level in a relaxed standing pose: approximately Y = 1.72.
- Hands extend a little below the wrist joints.

LEGS
- Hip joints: approximately Y = 1.70.
- Knee joints in a relaxed neutral pose: approximately Y = 1.00.
- Ankle joints: approximately Y = 0.32.
- The legs must be long and slender.

FEET
- Shoe soles rest at Y = 0 in the standing pose.
- Shoe height: approximately 0.28–0.30 units.
- Shoe length: approximately 0.48–0.52 units.
- Shoe width: approximately 0.22–0.26 units.

These dimensions produce a tall, thin character with a relatively
large spherical head, a narrow torso, long limbs, and substantial
shoes.

Maintain these proportions consistently during all rotations,
animations, expressions, and camera changes.

Do not independently redesign the character for different camera views.


==================================================
2. OVERALL SILHOUETTE AND ANATOMY
==================================================

The body must follow the recognizable structure of a conventional
stickman.

The head is the largest visual feature.

The torso is narrow and almost line-like. It is not a broad chest,
human rib cage, or rounded human body.

The arms and legs are long, slender, cylindrical or capsule-like
segments. They must remain thin enough to preserve the classic
stick-figure silhouette.

The shoulders are narrow. There are no broad shoulders, defined
muscles, thick upper arms, bulky thighs, or human anatomical masses.

The pelvis should not have a large independent volume. The narrow
torso transitions into the two slim legs through simple hip joints.

The body must be made from smooth, rounded 3D forms rather than
flat lines.

The limbs should have enough thickness to be visible in a 3D film
but must remain unmistakably stick-like.

Use overlapping geometry at the shoulders, elbows, wrists, hips,
knees, and ankles so that rotating the joints never reveals empty
gaps between body parts.

At the same time, avoid obvious spherical joints that make the
character look like a mechanical mannequin.

The final silhouette should read immediately as:

large round head,
thin neck,
slim vertical body,
long thin arms,
long thin legs,
oversized dark sneakers.

The design must still read clearly when viewed from a distance or
rendered as a dark silhouette against a bright background.


==================================================
3. HEAD GEOMETRY
==================================================

The head is a smooth, near-perfect sphere with a slightly warm ivory
color.

It is not a polygonal, triangular, cube-shaped, pointed, or angular head.

Its surface should be continuously smooth, with no visible seams,
facets, sculpted wrinkles, skin pores, or complicated texture.

Use a high-resolution sphere geometry with smooth normals.

The sphere may be very slightly taller than it is deep, but this
difference must be subtle. It should still look unmistakably round.

Suggested starting dimensions:
width 0.94,
height 0.94,
depth 0.90.

The head is attached to a very narrow charcoal-black neck.

The neck connects beneath the head and disappears naturally into
the underside of the spherical geometry.

Do not place a large neck inside the center of the face.

The head has:
- No hair.
- No ears.
- No nose.
- No beard.
- No mustache.
- No freckles.
- No visible skin pores.
- No helmet.
- No hat.
- No decorative markings.
- No external head accessories.

The front of the head contains only the eyes, eyebrows, and small
expressive mouth.

The rear of the head is a completely continuous, smooth ivory
surface with no facial features.

The left and right sides of the head remain smooth and rounded.

The head must look correct in front, profile, three-quarter, rear,
top, and low-angle views.

Do not attach facial features as a flat picture painted across the
sphere. Construct the features as actual 3D elements placed against
the curved surface of the head.

Facial elements should follow the curvature of the sphere and
remain properly attached when the head rotates.


==================================================
4. HEAD MATERIAL AND SURFACE QUALITY
==================================================

The head color is warm ivory-white rather than pure digital white.

Suggested base color:
#F1E3D8

The material is nonmetallic, smooth, and slightly satin-like.

Use a physically based material such as MeshStandardMaterial or
MeshPhysicalMaterial.

Suggested starting values:
metalness: 0.0
roughness: approximately 0.38–0.48

The head should receive soft highlights from the scene lighting.

The surface should not appear wet, chrome-like, glass-like, metallic,
or covered in a thick plastic gloss.

It should also not look like rough stone, unpainted wood, or fabric.

Use subtle lighting variation to describe the curvature of the sphere.

The same material must be used on the head throughout the project.

Lighting may change the apparent brightness naturally, but the
underlying base color must remain consistent.


==================================================
5. EYES: PRIMARY FACIAL FEATURE
==================================================

The character has exactly two eyes.

Each eye is a vertically oriented, smooth, glossy black oval.

The eyes are simple and highly readable from a distance.

They are not realistic human eyeballs. Do not add elaborate irises,
colored pupils, realistic veins, eyelids with anatomical complexity,
or detailed human eye anatomy.

Each eye has:
- A near-black main surface.
- An elongated oval silhouette.
- A subtle convex 3D shape.
- A small restrained light reflection or catchlight.
- A clean, polished finish.

Suggested initial dimensions for each eye:
width: approximately 0.10–0.13 units.
height: approximately 0.18–0.22 units.
depth: approximately 0.04–0.06 units.

The eyes are positioned symmetrically across the front of the head.

Their centers are approximately 0.15 units to the left and right
of the head's vertical centerline.

Place them slightly above the horizontal midpoint of the head.

The spacing should feel natural and friendly. The eyes should not
touch, overlap, or sit so far apart that the character looks strange.

Their positions should follow the curved surface of the head.

The inner edge of each eye should follow the same symmetrical
facial layout.

Because the head is spherical, the eyes may require slight outward
rotation to follow the surface.

The eye surfaces must not float noticeably away from the head.
They should sit close to the surface while remaining visible as
distinct 3D elements.

The eye geometry must be capable of supporting:
- Neutral gaze.
- Looking left.
- Looking right.
- Looking upward.
- Looking downward.
- Looking toward a nearby object.
- Wide-eyed surprise.
- Narrowed suspicious gaze.
- Sleepy half-closed eyes.
- Fearful, alert eyes.

These changes must be achieved without replacing the entire head
with a different character model.

Keep the eye design recognizable in every expression.


==================================================
6. EYEBROWS
==================================================

Place two small, dark eyebrows above the eyes.

They should be subtle and simple, not thick, hairy, realistic, or
overly decorative.

Use smooth, curved geometry, such as a thin TubeGeometry curve,
or another clean 3D representation.

Their default appearance is understated.

Each eyebrow follows the local curvature of the front of the head.

The eyebrows should be visible enough in close-up shots to
communicate emotion but restrained enough not to dominate the face.

The eyebrows are independently adjustable through animation.

They must support:
- Neutral position.
- Slight upward movement.
- Raised eyebrows for surprise.
- Inward lowering for anger.
- Slanted positioning for suspicion.
- An uneven raised position for confusion.
- Relaxed, lowered positioning for sadness and sleepiness.

Avoid exaggerated bushy eyebrows or thick black facial markings.

Do not change their fundamental thickness, color, or basic design
between scenes.


==================================================
7. MOUTH AND FACIAL EXPRESSIONS
==================================================

The character has one small, subtle mouth placed below the eyes.

It is a simple dark shape, not realistic human lips.

The neutral mouth is small and understated, with a restrained
closed-mouth curve.

Use 3D geometry or a carefully shaped facial surface that follows
the front of the head.

The mouth must not look like a flat rectangular sticker floating
in front of the face.

The mouth should move with the head and remain positioned correctly
when the character rotates.

Create reusable mouth shapes or blendable mouth controls for
different emotional states.

Required expressions:

NEUTRAL
Small closed mouth, relaxed eyebrows, normally open eyes.

HAPPY
A gentle upward-curving smile, slightly raised eyebrows, lively eyes.

SAD
Small downward-curving mouth, softened eyebrows, slightly lowered gaze.

SURPRISED
Small round open mouth, raised eyebrows, widened eyes.

ANGRY
Tighter mouth, eyebrows angled inward and downward, focused gaze.

WORRIED
Small tense mouth, raised inner eyebrow areas, uncertain eye direction.

CONFUSED
Slightly uneven eyebrows, subtly angled head, small asymmetric mouth.

EXCITED
Open smiling mouth, raised eyebrows, bright, wide eyes.

SHY
Small restrained smile, slightly lowered gaze, subtle head tilt.

SLEEPY
Relaxed mouth, lowered brows, partially closed eyelids.

THINKING
Small closed mouth, eyes directed toward an imagined object or
upward, one eyebrow raised slightly.

SCARED
Wide eyes, lifted eyebrows, open mouth, head pulled slightly back.

LAUGHING
Open smiling mouth, narrowed joyful eyes, head and body moving
naturally with the laugh.

These expressions must be made from the same base head model.

Do not increase the size of the head to create surprise.
Do not replace the eyes with unrelated shapes.
Do not stretch the face until it looks like a different character.

Expression changes should be achieved through controlled movements
of the eyebrows, eyes, eyelids, mouth, and head.

If animated mouth shapes are used, keep their geometry clean and
stable to avoid flickering or intersections.

The character has no detailed teeth or realistic tongue unless a
particular animation genuinely requires a tiny visible interior
inside an open mouth.


==================================================
8. NECK AND TORSO
==================================================

The neck is a short, very thin, charcoal-black cylindrical or
capsule-shaped connection between the head and torso.

It must be narrow enough that the head remains visually dominant.

The torso is a slim, nearly vertical black stick-like body.

It is not a shirt, jacket, suit, human chest, or thick central mass.

Use a narrow capsule, tapered cylinder, or several overlapping
rounded segments to create a smooth silhouette.

The torso extends from the shoulder region down to the pelvis.

Suggested maximum torso width:
approximately 0.12–0.16 units.

The torso should remain thin from the front, side, and rear.

There should be no visible clothing, shirt collar, buttons, belt,
pockets, or muscular chest.

The character's base body material is charcoal-black.

Suggested base color:
#252629

Use a subtle nonmetallic finish with enough roughness to preserve
the matte, stylized appearance.

The body should receive lighting naturally and should not appear
as a featureless pure-black hole in every scene.

Do not over-light the torso until it looks grey or silver.

The narrow torso acts as the central structural connection between
the neck, both arms, and both legs.

Use overlapping geometry to conceal the top and bottom connections.


==================================================
9. ARMS AND ARTICULATED LIMBS
==================================================

The character has two long, slim arms.

Each arm consists of:
1. An upper-arm segment.
2. An elbow joint.
3. A forearm segment.
4. A wrist joint.
5. A small hand.

The arms are charcoal-black except for the pale ivory hands and
the turquoise wristband on the anatomical left wrist.

The arms should look like smooth, rounded stick limbs.

Suggested starting radii:
upper arms approximately 0.045–0.055 units.
forearms approximately 0.035–0.050 units.

The exact radii may vary slightly to prevent the silhouette from
looking mechanically uniform, but the arms must remain slender.

The arm segments should have rounded ends and overlap naturally
at the joints.

In the neutral standing pose:
- The shoulders are narrow.
- The upper arms descend naturally.
- The elbows are slightly bent or relaxed.
- The forearms angle gently inward or outward according to the pose.
- The hands hang around the hip or upper-thigh region.

The default arms should not be permanently spread sideways.

The character must be able to raise both arms overhead, point at
objects, wave, gesture while speaking, cross its arms, reach forward,
protect its face, carry an object, and move naturally while running.

Use a real joint hierarchy or an equivalent articulated rig.

The shoulder joints must support rotation in multiple directions.

The elbows should primarily bend and extend, with limited natural
rotation.

The wrists should allow a reasonable range of movement.

All joints must be animated smoothly.

Avoid visible gaps when the arms bend.

Avoid large spherical black shoulder or elbow balls.

Do not thicken the arms during movement.

Do not allow the character's arms to change length as a substitute
for proper joint animation.


==================================================
10. HANDS AND FINGERS
==================================================

The hands are pale ivory-white, matching the head's main color.

They are small, softly rounded, and stylized.

They are more detailed than the simple stick arms but much simpler
than realistic human hands.

Each hand consists of:
- One small palm.
- One short thumb.
- Four simplified fingers.
- Smooth, rounded fingertips.

Use simple capsule-like or rounded tapered finger geometry.

The fingers should be large enough to be identifiable in close-up
shots but remain proportional to the very slim arms.

Keep the palm compact.

Do not create muscular forearms, realistic veins, fingernails,
skin folds, wrinkles, or photographic skin detail.

The hands should not look like oversized cartoon gloves.

In a distant shot, the hands should read as small pale shapes at
the ends of the black arms.

In a close-up shot, the thumb and fingers should be distinguishable.

The wrist should connect cleanly to the palm.

Make the fingers individually articulatable if the animation
system requires detailed pointing, gripping, waving, or object use.

For simple animation, the fingers may remain in a relaxed,
slightly curved resting pose.

Do not make the fingers transparent or paper-thin.

Do not allow fingers to detach or deform unpredictably while posing.


==================================================
11. TURQUOISE WRISTBAND
==================================================

This is the character's signature color accent.

The turquoise wristband is worn on the anatomical LEFT wrist.

In the defined coordinate system, the anatomical left wrist is
located on local +X.

When the character faces the camera directly, the band appears
on the viewer's right side.

It must never accidentally switch wrists because the camera angle
changes.

The band is a compact, bright turquoise cuff that wraps completely
around the wrist.

Suggested base color:
#1BB3C7

The band is small and clearly visible against the charcoal arm.

Its shape is a simple rounded rectangular or softly curved cuff,
not a bulky watch.

Include one small pale detail or inset marking on the outer-facing
surface of the cuff.

The detail should remain simple, without text, logos, or a screen
filled with tiny graphics.

The cuff should follow the wrist's orientation.

It should remain attached to the wrist during all hand and arm
movements.

Use enough geometry to make the cuff visibly three-dimensional.

Its material may be slightly smoother than the body material,
but it must not look like polished metal.

The wristband is a permanent design feature.

Do not remove it, recolor it, enlarge it, or move it to the other
wrist in subsequent scenes.


==================================================
12. LEGS AND FEET
==================================================

The legs are long, thin, and charcoal-black.

Each leg has:
1. A hip joint.
2. An upper-leg segment.
3. A knee joint.
4. A lower-leg segment.
5. An ankle joint.
6. A sneaker.

The legs must remain narrow, like traditional stickman limbs.

Suggested starting radii:
upper legs approximately 0.045–0.055 units.
lower legs approximately 0.035–0.050 units.

There are no thick thighs, muscular calves, trousers, shorts,
knee pads, or realistic human leg anatomy.

The upper legs connect directly into the narrow pelvis area.

The knees should not have large visible spherical joints.

In the neutral stance, both legs extend down toward the floor
with natural, slight spacing between them.

They should not be fused into a single central column.

The character can stand with feet apart, stand with feet together,
walk, run, jump, squat, kneel, sit, stumble, and fall.

The hips and knees must be independently articulatable.

The ankles must support foot orientation and landing.

During movement, the legs must retain constant lengths.

Do not make the lower legs suddenly thicker or the knees larger
to exaggerate an action.


==================================================
13. SNEAKERS
==================================================

The character wears two matching black sneakers.

The sneakers are chunkier than the narrow legs, creating the
character's characteristic footwear silhouette.

They are stylized high-top or ankle-height sneakers with rounded,
slightly exaggerated proportions.

Each shoe includes:

UPPER
- Dark charcoal or near-black material.
- Smooth synthetic or rubberized appearance.
- Rounded toe box.
- Slightly raised ankle collar.
- Clean construction.
- No realistic dirt, damage, or worn fabric.

SOLE
- Thick, clearly visible off-white rubber sole.
- Rounded silhouette around the front toe and heel.
- Approximately 0.06–0.08 units thick.
- Slightly wider than the upper.
- A subtly layered edge, without complicated tread detail.

LACES
- White or very pale grey.
- A small series of clearly visible laces across the top.
- Simple curved or flattened lacing geometry.
- No oversized bows or decorative laces.

SIDE DETAIL
- One small white diagonal stripe or abstract curved mark
  on each outer side.
- The mark is decorative and unbranded.
- It must not reproduce a real company logo.

SHAPE
- Approximate length: 0.48–0.52 units.
- Approximate width: 0.22–0.26 units.
- Approximate total height: 0.28–0.30 units.

The toe of each sneaker points forward along local +Z.

The heel points toward local -Z.

The two shoes face forward in a relaxed standing pose.

The shoes should be matching but mirrored naturally for the
left and right feet.

The ankle should connect into the top of the shoe without a
visible hole.

During walking and running, the entire shoe rotates with the
foot and remains correctly attached to the ankle.

The soles should contact the floor naturally.

Avoid floating shoes, sinking soles, detached feet, or shoes
that rotate independently of the legs.

Preserve the same shoe design and color in every scene.


==================================================
14. BACKPACK
==================================================

The character carries a compact black backpack worn on the back.

It is a permanent accessory in the standard design.

The backpack is not a large hiking bag, school bag with bright
graphics, or military backpack.

It is a simple, modern, compact daypack with rounded corners.

Suggested dimensions:
width approximately 0.40–0.46 units.
height approximately 0.55–0.62 units.
depth approximately 0.16–0.22 units.

Place the backpack behind the torso on local -Z.

Center it roughly around the upper-to-middle torso, approximately
Y = 2.30–2.40, adjusting the final location to fit the silhouette.

The backpack should be visible from rear and three-quarter views.

From the direct front view, only the shoulder straps or small
side edges may be visible where appropriate.

BAG SHAPE
- Compact rounded rectangular outline.
- Slightly curved front and back surfaces.
- Softly rounded corners.
- Black or very dark charcoal material.
- A restrained matte finish.

DETAILS
- One main compartment.
- One smaller front pocket or subtle front pocket seam.
- A simple zipper line.
- Two narrow black shoulder straps.
- Optional tiny zipper pulls, kept dark and understated.

Do not add text, lettering, colorful patches, bright logos,
keychains, or unnecessary decorations.

The straps must follow the shoulders naturally and remain visually
connected to the backpack.

The bag should fit closely to the back without intersecting
deeply through the torso.

It must not float away from the character when running, jumping,
or bending.

For animation, the backpack can have a slight delayed response to
body acceleration, but its motion must remain controlled and subtle.

The backpack's dimensions and design must remain consistent
across every camera angle and scene.


==================================================
15. COMPLETE COLOR PALETTE
==================================================

Use a compact, deliberate color palette.

HEAD AND HANDS
Warm ivory-white.
Suggested base color: #F1E3D8.

TORSO, NECK, ARMS, AND LEGS
Dark charcoal-black.
Suggested base color: #252629.

EYES, MOUTH, AND EYEBROWS
Near-black.
Suggested base color: #080808.

SNEAKER UPPER
Near-black charcoal.
Suggested base color: #191A1D.

SNEAKER SOLE
Warm off-white.
Suggested base color: #E7E3DD.

SNEAKER LACES AND SIDE MARK
Off-white or pale grey.
Suggested base color: #F0EFEB.

BACKPACK
Deep matte black.
Suggested base color: #141518.

WRISTBAND
Bright, clean turquoise.
Suggested base color: #1BB3C7.

Small variations in brightness may result naturally from the
lighting, but the underlying base colors remain fixed.

Do not randomly recolor the character to match the background.

Do not add clothing colors or extra accessories that are not
part of this specification.


==================================================
16. MATERIALS AND RENDERING STYLE
==================================================

The entire character must use premium stylized 3D rendering.

The finish should look like a polished animated feature film,
not a photorealistic human, an inexpensive mobile-game model,
a flat illustration, or a rough prototype.

Use smooth shading and appropriate physically based materials.

Suggested material treatment:

HEAD AND HANDS
Nonmetallic, soft satin finish.
Smooth highlights and gentle shading.

BLACK LIMBS
Subtle matte finish.
Enough surface definition to distinguish the limbs from dark
backgrounds.

EYES
Glossy black with small controlled highlights.

SHOES
Mostly matte synthetic material, with slightly different material
responses for the upper, laces, and rubber sole.

BACKPACK
Matte fabric-like visual treatment, implemented with clean
geometry and subtle surface definition rather than a noisy texture.

WRISTBAND
Slightly smoother turquoise material, with a restrained highlight.

Do not add heavy scratches, pores, hair, fabric fibers, grime,
or photorealistic surface noise.

Do not use thick outlines around the complete model.

Do not turn the character into a cel-shaded comic illustration.

Do not use low-poly faceting for the standard version.

The standard character uses smooth, continuous surfaces.

The overall result should remain deliberately stylized, simple,
clean, and suitable for premium animated-film cinematography.


==================================================
17. FRONT VIEW
==================================================

When seen directly from the front, the character faces local +Z.

The camera sees:
- A centered, large ivory spherical head.
- Two symmetrical dark oval eyes.
- Small dark eyebrows.
- A subtle mouth beneath the eyes.
- A very thin black neck.
- A narrow charcoal torso.
- Two long, thin arms hanging naturally at the sides.
- Two pale ivory hands.
- A turquoise wristband on the viewer's right.
- Two long, slim black legs.
- Two matching black sneakers with white soles and laces.

The backpack should be mostly hidden behind the torso.

The head must be centered over the torso.

The arms should not be attached unnaturally high or low.

The legs should be separated enough that the silhouette reads
as two distinct legs.

The shoes should sit flat on the floor and point forward.

The pose should feel relaxed and balanced.

The eye spacing, head scale, shoe size, and limb thickness must
match the proportions specified above.


==================================================
18. THREE-QUARTER FRONT VIEW
==================================================

Rotate the SAME character model approximately 30–45 degrees.

Do not construct a different version of the face.

The viewer should see:
- The spherical volume of the head.
- Both eyes, with the nearer eye appearing slightly more prominent.
- The smooth curvature of the head.
- The slim torso.
- The near and far arms at different apparent depths.
- The turquoise wristband when the left wrist is visible.
- The rounded depth of both sneakers.
- Part of the backpack's side or shoulder straps when the angle
  permits it.

The far eye should become naturally foreshortened, not disappear
because the face is incorrectly constructed as a flat image.

The head, eyes, nose-free facial surface, and mouth should all
rotate together as a coherent 3D assembly.

The near shoe should appear slightly larger than the far shoe
because of perspective, not because the model uses different
shoe dimensions.


==================================================
19. LEFT AND RIGHT SIDE VIEWS
==================================================

Create the side views by rotating the same 3D model.

Do not make separate side-profile artwork.

From either side:
- The head remains a smooth sphere.
- The visible eye follows the curvature of the head.
- The far eye becomes hidden naturally behind the head.
- The nose-free face has no protruding nose or muzzle.
- The neck is narrow.
- The torso is a thin vertical form.
- The arms and legs retain their slim cylindrical proportions.
- The backpack projects slightly behind the torso.
- The sneakers clearly show their rounded toes, thick soles,
  and modest raised ankle collars.

The front of the face points toward +Z.

The heel of each sneaker is toward -Z.

The backpack sits behind the torso toward -Z.

The wristband wraps around the anatomical left wrist. Its visible
position in the image depends on the viewing direction.

Do not move the wristband to the opposite anatomical wrist merely
because the character is seen from the other side.


==================================================
20. REAR VIEW
==================================================

The rear view is the same model rotated approximately 180 degrees.

The back hemisphere of the head is entirely smooth and ivory-white.

There are no eyes, eyebrows, mouth, hair, ears, markings, or
decorations on the back of the head.

The neck connects naturally to the rear of the head.

The torso remains charcoal-black and narrow.

The rear view must show the compact black backpack clearly.

The backpack occupies the center of the upper-to-middle back.

Its two straps connect naturally over the shoulder area.

The bag has a simple rounded rectangular silhouette and a small
front pocket or zipper detail.

The arms hang on either side of the backpack.

The back of both shoes is black with an off-white sole wrapping
around the heel.

The legs remain thin, separated, and symmetrical in a neutral pose.

Do not add extra straps, large compartments, logos, colored
patterns, or accessories that are absent from the front view.

Do not make the rear of the head flat.


==================================================
21. TOP AND LOW-ANGLE VIEWS
==================================================

TOP VIEW

The head must remain spherical when viewed from above.

The viewer should see the smooth upper hemisphere, with no hair
or attached objects.

The eyes should not appear on the top of the head.

The backpack should have a clear, compact footprint behind the torso.

The shoulder straps should remain physically connected.

The shoes should retain their real 3D volume and recognizable shape.

LOW-ANGLE VIEW

The head should remain attached to the neck.

The eye geometry should remain attached to the curved face.

The underside of the head may reveal the lower spherical curvature
but must not expose disconnected geometry or a hollow interior.

The neck must not poke through the front of the face.

The shoe soles should appear to have real thickness.

The legs and torso must maintain their designed lengths.

The character should not stretch, become distorted, or change into
a different silhouette when viewed from low or high angles.


==================================================
22. CHARACTER RIG AND HIERARCHY
==================================================

Build a reusable articulated character rig.

A suitable logical hierarchy is:

CharacterRoot
  Pelvis
    Torso
      Neck
        Head
          LeftEye
          RightEye
          LeftEyebrow
          RightEyebrow
          Mouth

      LeftShoulder
        LeftUpperArm
          LeftElbow
            LeftForearm
              LeftWrist
                LeftHand
                TurquoiseWristband

      RightShoulder
        RightUpperArm
          RightElbow
            RightForearm
              RightWrist
                RightHand

    LeftHip
      LeftUpperLeg
        LeftKnee
          LeftLowerLeg
            LeftAnkle
              LeftSneaker

    RightHip
      RightUpperLeg
        RightKnee
          RightLowerLeg
            RightAnkle
              RightSneaker

  Backpack

This is a logical structure; the implementation may use a more
appropriate scene graph or skeletal arrangement.

The backpack must follow the torso with controlled secondary motion.

The head must be able to rotate independently of the torso within
a natural animated range.

The arms and legs must be independently articulatable.

The wrists, hands, and sneakers must remain attached to their
corresponding limb joints.

Use stable pivot positions at shoulders, elbows, hips, and knees.

The limbs should be modeled or positioned relative to their pivots
so that rotation happens around the joints, rather than rotating a
long cylinder around its center accidentally.

Do not use uncontrolled scaling to simulate bending.

Do not rebuild the entire model during every animation frame.

Create the model once and animate its transforms.


==================================================
23. ANIMATION DESIGN
==================================================

The character is designed for animated narrative short films.

Required basic actions include:

- Neutral standing.
- Idle breathing.
- Looking around.
- Head tilting.
- Walking.
- Running.
- Jumping.
- Landing.
- Sitting.
- Standing up.
- Leaning against a wall.
- Waving.
- Pointing.
- Reaching for an object.
- Holding an object.
- Looking surprised.
- Looking frightened.
- Thinking.
- Laughing.
- Reacting to a sudden event.

The body language must remain readable even when the character
has little or no dialogue.

Walking should use coordinated arm and leg movement.

Running should include a forward lean, faster alternating leg
movement, counter-rotating arms, and natural head stabilization.

Jumping should include a clear anticipation phase, takeoff,
airborne phase, and landing.

Landing should involve slight knee bending and controlled settling.

A surprised reaction may include widened eyes, raised eyebrows,
a brief backward movement of the head, and a quick lift of the hands.

A thinking pose may include a head tilt, a hand near the chin,
and an upward gaze.

Do not animate every body part independently without coordination.

Use coherent keyframed movement or procedural animation to ensure
the complete character appears to act as one connected body.

Avoid excessive wobbling, uncontrolled rubber-like deformation,
limb stretching, and robotic snapping.

The base geometry and overall proportions must not change during
any of these actions.


==================================================
24. THREE.JS AND REMOTION IMPLEMENTATION
==================================================

Construct the character as a reusable Three.js component or factory
that returns a THREE.Group containing the entire model.

Use real meshes for:
- Head.
- Eyes.
- Eyebrows.
- Mouth.
- Neck.
- Torso.
- Arms.
- Hands and fingers.
- Legs.
- Shoes.
- Wristband.
- Backpack.

Capsules, smooth cylinders, spheres, and custom rounded geometry
are suitable building blocks.

Do not substitute the model with an image texture or a single
flat plane.

Use consistent local coordinates and a well-defined root transform.

Use proper material assignment and smooth normals.

Use reasonable geometry complexity to maintain visual quality
without creating unnecessary polygon counts.

Ensure the model can be scaled, positioned, and rotated as one
complete character.

Expose animation controls or a character animation interface
for expressions, poses, movement, and gaze direction.

REMOTION REQUIREMENTS

When rendered through Remotion, all animation must be deterministic
and driven by the current video frame.

Use Remotion's frame-based animation approach, such as useCurrentFrame,
interpolate, spring, and appropriate frame timing utilities.

Do not base cinematic animation on uncontrolled wall-clock time,
random per-frame values, or an autonomous animation loop that
produces different results for the same rendered frame.

The same frame must always produce the same character pose.

This is essential for consistent video rendering and seeking.

If randomness is used for secondary motion, use deterministic,
seeded values or precomputed animation curves.

Ensure every animated parameter is derived consistently from
the current frame and the defined animation timeline.

Avoid rebuilding geometries or materials on every frame.

Keep the character definition separate from scene-specific logic.

The same character should be reusable in multiple scenes,
locations, lighting setups, and camera positions.

A change in environment must not change the character's anatomy,
face, outfit, proportions, or accessory placement.


==================================================
25. RENDERING AND LIGHTING
==================================================

The character should look like a polished stylized animated-film
model when rendered at high resolution.

Use soft key lighting, gentle fill light, and a subtle rim light
when appropriate.

The large ivory head should receive attractive, smooth highlights.

The black limbs must remain readable against both light and dark
environments.

The turquoise wristband should be visible as a small accent without
becoming excessively bright or emissive.

The white shoe soles and laces should remain clearly distinguishable
from the dark shoe uppers.

The backpack should retain its shape and pocket details when lit.

Use high-quality anti-aliasing and suitable shadow settings.

Use smooth transitions between lit and shaded portions of the model.

Avoid excessive bloom, harsh outlines, oversaturated colors,
plastic shine, or photographic skin effects.

The goal is premium stylized 3D animation, not photorealism.

The environment may be colorful, detailed, cinematic, or atmospheric,
but the character's design remains stable.


==================================================
26. ABSOLUTE CONSISTENCY RULES
==================================================

The following features must remain fixed across all scenes.

1. One large, smooth, warm ivory spherical head.
2. Exactly two vertically oval black eyes.
3. Two small dark eyebrows.
4. One small expressive mouth.
5. No nose, ears, hair, beard, or mustache.
6. One slim charcoal-black neck.
7. One narrow charcoal-black torso.
8. Two long, thin charcoal-black arms.
9. Two long, thin charcoal-black legs.
10. Small ivory hands with simplified fingers.
11. One turquoise band on the anatomical left wrist.
12. One compact black backpack worn on the back.
13. Two matching black sneakers with off-white soles.
14. White or pale-grey sneaker laces.
15. A simple, unbranded white side detail on each sneaker.
16. The same head size and shape in every scene.
17. The same eye proportions and facial layout.
18. The same limb thickness and body proportions.
19. The same shoe design and backpack dimensions.
20. The same underlying 3D model from every viewing angle.

Do not invent new clothes or accessories.

Do not introduce facial hair, hairstyles, ears, a nose, muscular
anatomy, a human torso, or alien features.

Do not make the character look drastically different in different
lighting conditions.

Do not create a new head whenever the expression changes.

Do not switch the wristband between wrists.

Do not remove the backpack in one camera view and restore it in
another, unless a particular story explicitly requires an
on-screen action that removes it.

Do not alter the character's fundamental appearance between scenes.

Camera angle, pose, perspective, lighting, and facial expression
may change. The identity of the underlying character must not.


==================================================
27. FINAL QUALITY CHECK
==================================================

Before considering the model complete, render the SAME model in
the following views:

A. Straight-on front view.
B. Front three-quarter view.
C. Left-side profile.
D. Right-side profile.
E. Straight-on rear view.
F. Rear three-quarter view.
G. Top view.
H. Low-angle view.

Also render the following poses:

A. Neutral standing.
B. Walking.
C. Running.
D. Jumping.
E. Sitting.
F. Waving.
G. Pointing.
H. Surprised.
I. Thinking.
J. Scared.

Verify the following:

- The head is spherical in every view.
- The face is attached to the curved head surface.
- No facial element floats or becomes detached.
- The torso remains slim.
- The arms and legs retain their lengths.
- The joints do not reveal gaps.
- The wristband remains on the anatomical left wrist.
- The backpack remains attached to the back.
- Both sneakers retain their shape and orientation.
- The soles contact the floor during standing.
- The character remains recognizably the same in every pose.

IMPORTANT:
All turnaround images and animation tests must be produced from
the same underlying 3D model. Do not create separate approximate
models for the individual views.

The completed deliverable is a reusable 3D character asset,
not merely a character sheet image.

FINAL DESIGN INTENT:

A minimalist, premium-quality, stylized 3D stickman with a smooth
ivory spherical head, expressive black oval eyes, a narrow black
stick body, thin articulated limbs, ivory hands, black sneakers,
a compact black backpack, and one turquoise wristband on the
anatomical left wrist.

The character is simple enough to recognize instantly, detailed
enough to look excellent in close-up shots, and flexible enough to
carry an entire series of cinematic POV short films.
