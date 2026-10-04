---
set: location-probes
shot: hermes-sky-bridges-destination-walk
attempt: 1
stage: 04_animate
status: approved
generated: 2026-10-04T06:43:54.543837+00:00
sources:
  - 00-brief.md
  - ../../../location-probes/hermes-sky-bridges-and-passages/03-sidecar.md
  - ../../../../world/style.md
---

# Hermes destination walk, motion spec 1

## Source manifest
Paths below are workspace-relative. Hashes captured after brief approval.

| Approved input | SHA-256 |
|---|---|
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/00-brief.md` | `5d58432489f94e7de7bbf232e505292e1a5c3114b9094cb7e6ac7ebcb5fc68d2` |
| `runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md` | `9b0af53149e22e75fea88b9c6adfc1cca8d9cf3c12259bb255afd91f64215a02` |
| `runs/location-probes/hermes-sky-bridges-and-passages/02-render-1.md` | `b56b0a5a53474b94b5b2d36d6f07383f842ce72c80c4edbd56430348f66cc65e` |
| `runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png` | `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3` |
| `world/style.md` | `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc` |

Entry mode: existing accepted still; no new images. The accepted predecessor is
`runs/motion/location-probes/hermes-sky-bridges-and-passages/04-render-1.md`;
this new variation does not alter it. Source render is approved and accepted;
sidecar is approved. Inherited source deviations: slate-grey undertunic, brown
hair, left-wall heraldic caduceus/sunburst banners. Facial microdetail was not
verifiable at source scale. No additional world modules are selected: this is
motion within the supplied scene, not a newly designed location.

## Brief and feasibility
Approved completed brief: `00-brief.md`, approved by operator's chat 'approve'
after the completed pivot/sequence proposal. Earlier recommendations approved
fixed camera, measured pace, continuing ending, and delivery settings.

Outcome: Hermes departs toward the distant city, surveys it, then looks along
his road ahead. Starting image shows a foreground-facing stride and right-facing
head already cityward. The road curves screen-right into depth beside a parapet.
He must pivot his body before receding, not reverse instantly.

Use native `video_generate`; configured provider `nous`, model
`bytedance/seedance-2.5`, confirmed by configuration read-back during brief
feasibility. Current callable schema exposes one `image_url` and all requested
delivery settings. Model is host configuration, not a tool-call argument.
Reference URL must be anonymously fetched and matched to the manifest image hash
before rendering; use the existing approved publication if still verified.

Supported: single-image input, requested duration/aspect/resolution/audio/upscale
fields. Walking, pivot, head adjustment and locked camera are prompt requests,
not deterministic controls. Uncertain: unseen rear-view invention, staff/cape
rotation, foot contact, parapet occlusion, subtle head motion, and fitting both
pivot and travel into five seconds. Separate character/environment inputs are
absent from the callable schema and are not used. No frame-exact timing or
arrival at the distant city is promised. Approved brief resolves these risks
by requesting only near-road travel and a small visible surveying adjustment.

## What moves and sequence
Primary priority: visible head adjustment, coherent body pivot, then actual
walking displacement along the road. Secondary motion must not substitute for
these actions.

- Beginning: from the supplied pose, a small discernible head adjustment surveys
  the distant city. Feet, hips and shoulders then pivot toward the road's
  screen-right curve and away from the viewer, with continuous body motion.
- Main action: measured alternating steps take Hermes diagonally screen-right
  and into depth on the visible near paving. His head aligns with the route
  ahead. He does not instantly arrive at the far city.
- Ending: continue walking as the shot ends; no stopping or final settle.
- Expression/props: calm attentive expression; no new gesture. Staff follows
  the walking motion without design change or intersection with his body.
- Secondary: cloak responds to pivot and steps; background remains quiet.

These are relative beats, not a frame-timed choreography guarantee.

## What holds
Keep the supplied character's identity, proportions, facial structure, hair and
winged helmet design, slate-grey tunic, dark cloak, leather fittings, bronze
armour, sandals and twin-serpent staff. Preserve accepted brown hair and banners;
do not repair source deviations or invent readable freckles/iris detail.

Maintain grounded stone architecture, paving, parapet, ravine, city silhouette,
dusk palette, route lights and the accepted illustration's distinct contours,
flat colour blocking and matte textured-paper appearance. No new scene elements
or makeover into photographic/3D/painterly rendering.

Allowed changes: head/gaze direction, body orientation, limb pose, character
position and apparent scale as he recedes, cloth shape and staff orientation.
Preserve identity and design, not frozen facial pixels or starting pose.

## Camera and delivery
Locked camera retaining reference framing, perspective and deep focus; no pan,
follow, push, zoom or cut. Character stays on the visible near road.

Tool settings supplied separately from prompt:
- duration: 5
- aspect_ratio: 16:9
- resolution: 720p
- audio: false
- upscale: false
- image_url: verified public HTTPS URL of the manifest image

Verify returned dimensions, duration and audio streams rather than assuming
requested settings applied. No added paid processing or model change.

## At risk and success checks
| Risk / requested outcome | Guard and observable review criterion |
|---|---|
| Head motion suppressed | Visible head adjustment surveying city, then orientation along road; no claim about tiny eye detail |
| Direction reversal | Continuous feet/hips/shoulders pivot onto road; no pop or teleport |
| Static walk cycle | Alternating steps plus screen-right/depth displacement relative to fixed paving |
| Staff/cape/body deformation | Consistent design and coherent rotation; no duplicated limbs, staff or cape |
| Foot sliding / parapet clipping | Feet track paved surface; route stays inside parapet rather than across ravine |
| Camera motion confused with travel | Architecture stays stable; no pan, follow or zoom |
| Wrong ending | Still walking at end; no imposed settle |
| Identity / wardrobe / style drift | Accepted design, colours, contours and matte print appearance stay consistent |

Review visual consistency separately from motion success. Report actual
video timestamps/frame indices for every criterion, with `holds`, `drifted`,
or `cannot see`. Disclose sample-review limits. Operator owns final acceptance;
no filing to accepted manifest until the video is accepted.

## Prompt
Animate the supplied reference image as one continuous shot with a fixed camera. Hermes first makes a small but clearly visible head adjustment to survey the distant city at screen-right. From his foreground-facing stride, he then pivots his feet, hips and shoulders naturally toward the road's rightward curve and away from the viewer. He walks at a measured pace diagonally screen-right and into depth along the visible near stone paving, with alternating steps producing clear displacement relative to the road. His head turns to align with the route ahead. Keep him on the near stretch inside the parapet, not arriving at the distant city. He continues walking as the shot ends; no stop or final settle.

Keep his calm attentive expression. The cloak responds naturally to his turn and steps, and his staff moves coherently with him without intersecting his body or the pavement. Background motion remains quiet so the head adjustment, body pivot and walking are readable. Maintain continuous foot contact without sliding, teleporting, duplicated limbs or clipping through the parapet.

Preserve the supplied character's identity, facial structure, proportions, hair and winged helmet design, slate-grey tunic, dark cloak, leather fittings, bronze armour, winged sandals and twin-serpent staff. Allow his head direction, gaze, body orientation, limb poses, position and cloth shapes to change with the action; do not freeze his starting pose. Retain the brown hair and existing heraldic banners as shown. Preserve the grounded architecture, paving, parapet, ravine and distant city, dusk palette, route lights, distinct contours, flat colour blocking and matte textured-paper illustration. No photographic, three-dimensional or painterly makeover, no new scene elements, captions or overlays. The camera remains completely fixed with the same framing and perspective: no pan, zoom, push, follow or cut.
