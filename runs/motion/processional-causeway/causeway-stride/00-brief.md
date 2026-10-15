---
set: processional-causeway
shot: causeway-stride
stage: motion-brief
status: approved
generated: 2026-10-15T13:34:00+00:00
sources:
  - runs/studio/causeway-reference-trial/00-intake-1.md
  - runs/processional-causeway/causeway-stride/03-sidecar.md
---

# causeway-stride, video brief

## Outcome
Hermes strides forward along the Processional Causeway at dusk at a steady cadence (~2 steps/second), turning his head slightly toward the route marker on screen-right while each planted step sends a brief pulse of liquid warm-gold energy along the shallow carved gutters at the inside base of the left and right stone curbs.

## Reference and entry mode
- Mode: existing accepted still (`runs/processional-causeway/causeway-stride/02-image-4.png`).
- Source set and shot: `processional-causeway` / `causeway-stride` (`attempt: 4`).
- Approved sidecar: `runs/processional-causeway/causeway-stride/03-sidecar.md` (`status: approved`, `verdict: accepted`).
- New-scene handoff, if needed: completed via `01-spec-4.md` → `02-render-4.md` → `03-sidecar.md`.

## Starting state
Hermes stands in a straight-on full front view in the lower-left third of the frame on the cracked rectangular limestone paving of the Processional Causeway, with symmetrical feathered helmet wings, charcoal-grey undertunic with sepia hem, dark-charcoal chlamys with gold clasp, brown leather cross-body harness and messenger pouch, bronze bracers and greaves, weathered brown-leather sandals with one pale feathered wing projecting outward from the outer ankle of each boot and smooth wingless inner ankles, and his antique-bronze twin-serpent winged caduceus held vertically in his right hand. The roadbed and the shallow carved stone gutters along the inside base of both stone curbs are dormant matte limestone.

## Primary action
- Travel: Hermes strides forward toward the foreground along the limestone road at a steady ~2 steps/second pace without slowing down in the final second.
- Head and gaze: Starts facing straight ahead in calm attentive focus, makes a slight turn toward the fluted stone route marker at screen-right, and returns his gaze forward along his path.
- Expression and props: Calm attentive focus holds; caduceus moves coherently in his right hand; each planted footstep sends a brief, confined pulse of liquid warm-gold energy along the carved gutters at the inside base of the left and right stone curbs (never meandering into the center roadbed).

## Sequence
- Beginning: Start immediately in forward stride from the supplied front-facing pose on the dormant stone road.
- Main action: Alternating forward steps (~2 steps/second) carry Hermes forward along the causeway while his head makes a slight turn toward the screen-right route marker and returns forward; on each footfall, liquid warm-gold energy pulses briefly along the inside base of the left and right stone curbs.
- Ending: Continue moving in full stride through the final frame (no end-of-clip stop or deceleration).

## Secondary motion
Light billowing of the dark-charcoal chlamys cloak with his stride, and confined warm-gold energy pulses along the inside base of both stone curbs on footfalls.

## Camera
Locked off (`16:9`, 28mm full-frame equivalent, deep focus, no pan, zoom, tilt, or cut).

## What stays consistent
- Identity, proportions, facial structure, golden-brown curls, antique-bronze winged helmet with symmetrical side wings.
- Default wardrobe: charcoal-grey undertunic with sepia hem, dark-charcoal chlamys with gold clasp, brown leather harness/belt/pouch, bronze bracers and greaves.
- Paired sandal-wing symmetry: exactly one pale feathered wing on the outer side of the left boot and one matching pale feathered wing on the outer side of the right boot, with smooth wingless inner ankles between the legs (no inverted wings, no flipped anatomy, no mirrored limbs, no wrong-side wing placement).
- Ukiyo-e woodblock print medium on aged speckled parchment.

## Delivery
- Duration: `5` seconds
- Aspect ratio: `16:9`
- Resolution: `720p`
- Audio: `false`
- Upscale: `false`

## Success checks
1. Continuous forward walking displacement at ~2 steps/second with no final-second stop.
2. Outer sandal wings remain on the outside of each ankle with smooth, wingless inner ankles throughout the stride.
3. Warm-gold energy pulses stay confined to the inside base of the left and right stone curbs, leaving the center roadbed unlit stone.
4. Locked camera and ukiyo-e woodblock print look hold from first frame to last.

## Feasibility check
- Active tool, configured provider/model, supported inputs/settings, evidence: Native `video_generate` (`nous` router → `bytedance/seedance-2.5` / `fal`), accepts HTTPS `image_url`, `duration: 5`, `aspect_ratio: 16:9`, `resolution: 720p`, `audio: false`, `upscale: false`.
- Supported requests: Single-image input (`image_url`), 5s duration, 16:9, 720p, locked camera, forward walk.
- Uncertain requests and reference risks: Step-synchronized curb-gutter pulses and exact wing symmetry during motion are prompt-guided targets on the video model, not deterministic guarantees.
- Unsupported requests and alternatives: None.
- Operator decisions needed: Authorize public hosting / `image_url` handoff and 1 video generation call.

## Studio handoff
- Approved intake and selected sequence/storyboard/continuity versions: `runs/studio/causeway-reference-trial/00-intake-1.md` (`sha256:f65f16ac6aa6c26718d012c9a171237d1a50619270265559bc4fdddb2a17c917`, `gate_mode: visual-only`).
- Shot/event IDs and expected start/end state IDs: standalone single animated shot.
- Selected approved map/reference paths and completed preparation: `runs/processional-causeway/causeway-stride/03-sidecar.md` (`sha256:407303a049d594bfe53a1ae65c9db18719eaa38d5a2a97c3b51be472e8c538cf`).
- Early composition brief link for pacing/framing, or none: none.
- Receiving producer, expected output and revision-impact notes: Hermes (`04_animate` → `runs/motion/processional-causeway/causeway-stride/01-spec-1.md`).
