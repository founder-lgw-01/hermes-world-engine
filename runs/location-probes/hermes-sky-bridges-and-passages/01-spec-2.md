---
set: location-probes
shot: hermes-sky-bridges-and-passages
attempt: 2
stage: 01_spec
status: approved
generated: 2026-10-15T09:03:58.725810+00:00
sources:
  - runs/location-probes/hermes-sky-bridges-and-passages/00-brief.md
  - runs/location-probes/hermes-sky-bridges-and-passages/01-spec-1.md
  - runs/location-probes/hermes-sky-bridges-and-passages/02-render-1.md
  - runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png
  - runs/studio/sky-bridges-two-shot-trial/02-review-2.md
  - world/environment.md
  - world/style.md
  - world/characters/hermes.md
  - world/environment/locations/sky-bridges-and-passages.md
  - _reference/spec-rules.md
  - _reference/drift-checklist.md
---

# Hermes at Sky-Bridges and Passages, spec 2 (image-to-image footwear symmetry correction under `gate_mode: visual-only`)

## World-input manifest

- `runs/location-probes/hermes-sky-bridges-and-passages/00-brief.md` — `19edd1d847e4145466c0c782410685169812188c26b79d234afab037cdb8183e`
- `runs/location-probes/hermes-sky-bridges-and-passages/01-spec-1.md` — `a10d1f5722948af045bc2d4684a432f282785c3fcd6258a52e13c69516ce7349`
- `runs/location-probes/hermes-sky-bridges-and-passages/02-render-1.md` — `b56b0a5a53474b94b5b2d36d6f07383f842ce72c80c4edbd56430348f66cc65e`
- `runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png` — `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3`
- `runs/studio/sky-bridges-two-shot-trial/02-review-2.md` — `20d1d0234e561cc961989444af25138c6b24247e37e1a0339f2170e0228c2220`
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

## Brief

The approved brief is `runs/location-probes/hermes-sky-bridges-and-passages/00-brief.md`, updated with the sandal wing symmetry drift identified in `runs/studio/sky-bridges-two-shot-trial/02-review-2.md` (`2 wings on 1 foot and 1 small wing on the other`). Derived and approved under `gate_mode: visual-only` per Jordan's desktop direction (“Yes to both”).

## Characters in frame

Hermes is tall and statuesque with an athletic lean heroic build, broad defined shoulders, athletic powerful limbs, and large robust hands. His angular high-cheekboned face has a strong square jaw, straight classical nose, luminous amber-golden eyes, warm sun-baked bronze skin, freckles across the nose bridge and upper cheeks, and no facial hair. His short-to-medium thick coarse curls are warm golden-brown with lighter sun-bleached highlights. He wears the default outfit: antique-bronze winged helmet, charcoal-grey heavy-linen knee-length undertunic with parchment-sepia edge, dark-charcoal chlamys with antique-gold clasp, worn leather harness and belt, scratched bronze bracers and greaves, weathered brown-leather sandals with a symmetrical matching pair of pale feathered heel wings (exactly one outer heel/ankle wing on the left sandal and one matching outer heel/ankle wing of equal size on the right sandal, with no extra inner-ankle wing between the boots), and an aged gold/bronze twin-serpent winged caduceus.

## Scene

Hermes strides in calm attentive focus across a series of grounded limestone viaducts that cross ravines between mountain ridges and plazas, running from Gateway Pavilion toward Crystal Citadel. Underfoot is weathered limestone paving. Warm-gold route light appears only in shallow carved stone channels and gateway thresholds. The passage has no floating islands, abyss-edge world, energy conduits, or mechanical bridge structure. Dusk gives amber, orange, and gold long shadows.

## Camera

A full-body wide 16:9 scene at slightly below eye level with a 28mm full-frame-equivalent lens and deep focus, preserving the exact composition and framing of `02-image-1.png`.

## At risk

- **Sandal heel-wing symmetry (`02-review-2.md`):** In `02-image-1.png`, the right-side boot has two wings (an outer wing and an extra inner wing between the ankles) while the left-side boot has one smaller wing. Guard: pass `02-image-1.png` as `image_url` to `image_generate` and explicitly instruct the edit to remove the extra inner-ankle wing between the feet and make both sandals have one matching, equal-sized outer heel wing while keeping the rest of the illustration unchanged.
- **Scene and character preservation during image-to-image edit:** An image-to-image call can accidentally alter the composition, architecture, lighting, or ukiyo-e woodblock print texture. Guard: state that the pose, face, helmet, cloak, caduceus, limestone viaduct, parapet, distant city, dusk sky, and flat ukiyo-e woodblock-print linework must remain identical to the source image.

## Prompt

Edit the supplied image only at Hermes's winged sandals/boots to fix the wing asymmetry, keeping the entire rest of the illustration unchanged. On his feet, remove the extra inner wing that points downward into the gap between his two boots, and make the winged sandals a symmetrical matching pair: exactly one pale feathered wing on the outer side of the left boot and one matching pale feathered wing of the same size on the outer side of the right boot, with clean stone paving visible between his ankles. Preserve his exact pose, face, winged helmet, dark cloak, tunic, bronze greaves, twin-serpent caduceus, the grounded limestone viaduct, glowing warm-gold stone channels, columns, distant hilltop city, dusk sky, 16:9 framing, and traditional Japanese woodblock-print (ukiyo-e) line art and matte textured-paper finish unchanged.
