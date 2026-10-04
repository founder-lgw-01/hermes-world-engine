---
set: location-probes
shot: hermes-sky-bridges-destination-walk
stage: motion-brief
status: approved
generated: 2026-10-04T06:37:48.056800+00:00
sources: operator
---

# Hermes sky-bridges destination walk, video brief

Copy to `runs/motion/<set>/<shot>/00-brief.md`. Start with the intended outcome,
not a prompt. Hermes interviews in small groups, explains options and risks in
plain English, and records answers here. Blank means unanswered. `you choose`
delegates a choice that must be surfaced before approval.

## Outcome
Hermes walks away along the road toward the distant city. He surveys his destination, then looks along the road ahead. [operator answers]

## Reference and entry mode
- Mode: existing accepted still. No new image generation.
- Source set and shot: location-probes / hermes-sky-bridges-and-passages
- Approved sidecar: runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md
- New-scene handoff: not applicable.
- Accepted predecessor: runs/motion/location-probes/hermes-sky-bridges-and-passages/04-render-1.md; preserve original accepted video.

## Starting state
Source inspection: Hermes occupies the foreground left/centre. His body and advanced foot read as approaching the foreground; his head is already in right-facing profile toward the city. The paved road curves screen-right and into depth beside a parapet. Walking away therefore requires a body pivot, not merely continued steps. Facial microdetail becomes less visible as he recedes.

## Primary action
- Travel: away along the road toward the distant city at a measured walking pace. [operator-approved recommendation]
- Head and gaze: survey destination, then look along the road ahead. Starting angle and extent of turn require source inspection. [operator answer]
- Expression and props: calm attentive expression retained; no new gesture. Staff follows the steps without changing design. [proposed completion]

## Sequence
- Beginning: from the reference pose, Hermes surveys the city with a small visible head adjustment, then turns his body to align with the road. [proposed transition needed by source]
- Main action: measured steps diagonally screen-right and away along the visible paving; head aligns with the route ahead. Stay on the near stretch, not an instant arrival at the city. [proposed sequence]
- Ending: Hermes continues down the road as the clip ends; no stop or settle. [operator-approved recommendation]
Relative beats are targets, not guaranteed frame-accurate control.

## Secondary motion
Cloak and staff respond to the steps. Environment stays visually quiet; no emphasized secondary action. [operator-approved recommendation]

## Camera
Fixed camera; preserve reference framing with no follow, pan, push or zoom. Character travel and head movement are the primary visible changes. [operator-approved recommendation]

## What stays consistent
Retain identity, proportions, helmet, wardrobe, staff design, architecture, dusk palette and accepted print appearance. Inherit slate-grey undertunic, brown hair, and left-wall heraldic banners as accepted source facts. Allow head/gaze, body orientation, limbs, position and cloth to change; do not freeze pose or face angle.

## Delivery
- Duration: 5 seconds.
- Aspect ratio: 16:9.
- Resolution: 720p.
- Audio: false (silent).
- Upscale: false.
These delivery settings are operator-approved.
Resolve unsupported values before approval; no silent clamping or paid extras.

## Success checks
Proposed success checks:
- Visible body pivot aligns feet/torso with the paved route; no teleporting reversal.
- Alternating steps produce displacement screen-right and into depth, not walking in place or camera motion.
- A discernible head adjustment surveys the city, then head orientation follows the route; no eye-colour or freckle verification at this scale.
- Fixed camera and architecture remain stable.
- Hermes remains walking at the end.
- Identity, wardrobe, staff and accepted visual design remain consistent; feet stay on pavement without parapet clipping.

## Feasibility check
- Active tool: native video_generate. Read-back configuration: provider nous, model bytedance/seedance-2.5. Callable schema exposes image_url, duration 4–30, 16:9, 720p, audio and upscale. Backend compliance still requires output verification.
- Supported requests: single accepted image input and selected delivery fields. Fixed camera, walking and head turn are prompt requests, not deterministic controls.
- Uncertain requests and reference risks: source body faces foreground while requested travel recedes, requiring a pivot and invention of unseen rear surfaces. Staff/cape/feet can deform during rotation; parapet may occlude legs. Head already faces city, so surveying motion may be subtle. Five seconds must accommodate both pivot and steps.
- Unsupported requests and alternatives: separate environment/character fields absent from callable schema. No such input used. No precise frame-timing guarantee or fully visible distant route.
- Operator decisions needed: approve proposed pivot/sequence and success checks in this completed brief before spec derivation. No render approval inferred from delivery approval.
Resolve blockers and obtain brief approval before deriving the motion spec.
