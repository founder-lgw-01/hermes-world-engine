---
set: location-probes
shot: hermes-sky-bridges-and-passages
attempt: 3
stage: 01_spec
status: approved
generated: 2026-10-15T09:37:43.749179+00:00
sources:
  - runs/location-probes/hermes-sky-bridges-and-passages/00-brief.md
  - runs/location-probes/hermes-sky-bridges-and-passages/01-spec-2.md
  - runs/location-probes/hermes-sky-bridges-and-passages/02-render-2.md
  - runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png
  - world/environment.md
  - world/style.md
  - world/characters/hermes.md
  - world/environment/locations/sky-bridges-and-passages.md
  - _reference/spec-rules.md
  - _reference/drift-checklist.md
---

# Hermes at Sky-Bridges and Passages, spec 3 (occlusion-aware sandal wing correction under `gate_mode: visual-only`)

## World-input manifest

- `runs/location-probes/hermes-sky-bridges-and-passages/00-brief.md` — `19edd1d847e4145466c0c782410685169812188c26b79d234afab037cdb8183e`
- `runs/location-probes/hermes-sky-bridges-and-passages/01-spec-2.md` — `fb54e94499ecbe4ad073d8141dbcf9e2171f44156536dabab4eb72905ed5b85a`
- `runs/location-probes/hermes-sky-bridges-and-passages/02-render-2.md` — `5a376ab29d0c8b0828d9bc13f2ede85fc8d6651361995828bfbf18179aa06028`
- `runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png` — `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3`
- `world/environment.md` — `8b14aa19c190f8b3760811160e90ecc037d7a3079e5194f9a781d52f570f8d19`
- `world/style.md` — `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc`
- `world/characters/hermes.md` — `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88`
- `world/environment/core.md` — `50c1917fa78d2fbf5757eada9859e058971e7959cdc42a919b275c2c39fcb11a`
- `world/environment/palette-and-light.md` — `17d78431f39d55efa06fb55b9219ab31a2dbde9050140bfa863c89008d4736da`
- `world/environment/materials-and-wear.md` — `f90b2bd8d1cebbdc5119b9e7639a31b7b9064616df632db0f21060238be940b5`
- `world/environment/forms-and-architecture.md` — `4db8eb6bef73f6658dd6152165e5136b7956520b1a2094651f915e29b9428ba5`
- `world/references/hermes-face.md` — role `hermes-default-face`, `4c9836c8b46ec2f179256cfb51376e31097be3a12737f1e12f303e400475a0e9`
- `world/references/hermes-face.webp` — selected reference image, `bc9fc04ee5ef9c01673af2bf8db05c11f38a9f1f7c480a924185d84ce9d0d4e4`
- `world/environment/locations/sky-bridges-and-passages.md` — `e6264ac973e032d2dd8e5dc678b2d6a3a6a2907ed9bb1ee80c871cf6e82c7010`
- `_reference/drift-checklist.md` — `e25f5c7e5ed0c9166c8b3ff97a1f4015b9aa4107ab98bb9d0d35a19b6045613c`

## Brief

Derived from `02-render-2.md` (`verdict: drifted`) and Jordan's occlusion diagnosis (“drifted and to be precise from this angle, I don't think we would even see the other wing if it was on the other side due to the right leg blocking; yes 1 more”) under `gate_mode: visual-only`.

## Characters in frame

Hermes is tall and statuesque with an athletic lean heroic build, broad defined shoulders, athletic powerful limbs, and large robust hands. He wears the default outfit including scratched antique-bronze greaves and weathered brown-leather sandals with pale feathered heel wings on the outer heel only. From this 3/4 walking angle where his forward right leg crosses in front of his rear ankle, only the outer wing on the unoccluded side is visible, while the opposite outer wing is naturally occluded behind the crossing leg; no wing is drawn in the inner gap between his boots.

## Scene

Hermes strides in calm attentive focus across grounded limestone viaducts running from Gateway Pavilion toward Crystal Citadel. Underfoot is weathered limestone paving with warm-gold route light in shallow carved stone channels.

## Camera

A full-body wide 16:9 scene at slightly below eye level with a 28mm full-frame-equivalent lens and deep focus, preserving the exact composition and framing of `02-image-1.png`.

## At risk

- **Occlusion of far-side sandal wing (`02-render-2.md`):** Asking for two visible symmetrical wings forced the model to place a wing between the ankles where the front leg blocks the rear boot's outer side. Guard: instruct the edit to remove all wing shapes from the inner gap between the two boots and from the occluded inner ankle, leaving only the single outer heel wing on the outside edge of the boot while the other boot's outer wing remains naturally hidden behind the crossing leg.
- **Scene preservation:** Keep the entire rest of `02-image-1.png` unchanged.

## Prompt

Edit the supplied image only at Hermes's boots/sandals to respect natural leg occlusion, keeping the entire rest of the illustration unchanged. Because his front leg steps across in front of his back ankle from this angle, the outer wing on the blocked side is naturally hidden behind his leg. Remove the inner wing located between his two boots/ankles completely so that only smooth leather boot/strap and stone paving appear between the legs, and keep only a single pale feathered heel wing on the outer unblocked side of the boot. Do not draw two wings on one boot and do not place any wing in the gap between his ankles. Preserve his exact pose, face, winged helmet, dark cloak, tunic, bronze greaves, twin-serpent caduceus, the grounded limestone viaduct, glowing warm-gold stone channels, columns, distant hilltop city, dusk sky, 16:9 framing, and traditional Japanese woodblock-print (ukiyo-e) line art and matte textured-paper finish unchanged.
