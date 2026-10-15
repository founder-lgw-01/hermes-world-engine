---
set: processional-causeway
shot: causeway-stride
attempt: 1
stage: 04_animate
status: approved
generated: 2026-10-15T13:34:30+00:00
sources:
  - runs/studio/causeway-reference-trial/00-intake-1.md
  - runs/motion/processional-causeway/causeway-stride/00-brief.md
  - runs/processional-causeway/causeway-stride/03-sidecar.md
  - runs/processional-causeway/causeway-stride/02-render-4.md
  - runs/processional-causeway/causeway-stride/02-image-4.png
  - runs/processional-causeway/manifest.md
  - world/style.md
  - world/characters/hermes.md
  - world/environment/locations/processional-causeway.md
---

# causeway-stride, motion spec 1

## 0. Source manifest
| Selected input or filing evidence | SHA-256 |
|---|---|
| `runs/studio/causeway-reference-trial/00-intake-1.md` | `f65f16ac6aa6c26718d012c9a171237d1a50619270265559bc4fdddb2a17c917` |
| `runs/motion/processional-causeway/causeway-stride/00-brief.md` | `cc8ffd743dd44c225e4776a23c022f5490ea00f6d1952a2d6bca51c1b1cd03c4` |
| `runs/processional-causeway/causeway-stride/03-sidecar.md` | `407303a049d594bfe53a1ae65c9db18719eaa38d5a2a97c3b51be472e8c538cf` |
| `runs/processional-causeway/causeway-stride/02-render-4.md` | `a9c8435e1c310affb05145717efc6ce69d39b492dd86812f24b12ddd37467a0e` |
| `runs/processional-causeway/causeway-stride/02-image-4.png` | `1bc5e53db713781d5a090752610a990aa9fe4c245555052f063516308d211252` |
| `runs/processional-causeway/manifest.md` | `794b17fd74481fd44f5b15b0c14ae7bba435ddc6028ad97dfdf46e10533f2169` |
| `world/style.md` | `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc` |
| `world/characters/hermes.md` | `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88` |
| `world/environment/locations/processional-causeway.md` | `c86a6f7532c3ae01db83f870b9d60e2e299e29489299cf4569581a3816cec4f0` |

## 1. Brief and feasibility
- **Outcome:** Hermes strides forward along the Processional Causeway at ~2 steps/second in a straight-on front view, turning his head slightly toward the route marker at screen-right and back forward while each planted step sends a brief pulse of liquid warm-gold energy along the shallow carved gutters at the inside base of the left and right stone curbs.
- **Configured route:** Native `video_generate` (`nous` router → `bytedance/seedance-2.5` / `fal`), `duration: 5`, `aspect_ratio: 16:9`, `resolution: 720p`, `audio: false`, `upscale: false`.
- **Source image (`image_url`):** Requires public HTTPS URL whose bytes match `02-image-4.png` (`sha256:1bc5e53db713781d5a090752610a990aa9fe4c245555052f063516308d211252`).

## 2. What moves and sequence
- **Beginning:** Start immediately in forward stride from the supplied front-facing pose.
- **Main action:** Alternating forward steps (~2 steps/second) carry Hermes toward the foreground along the limestone road; he makes a slight head turn toward the fluted stone route marker at screen-right and returns his gaze forward; each planted footstep sends a brief, confined pulse of liquid warm-gold energy along the shallow carved gutters at the inside base of the left and right stone curbs.
- **Ending:** Continue moving in full stride through the final frame without slowing down or stopping in the final second.
- **Secondary motion:** Dark-charcoal chlamys cloak billows lightly with his stride; caduceus moves coherently in his right hand.

## 3. What holds
- **Identity & Wardrobe:** Preserve Hermes's facial structure, golden-brown curls, antique-bronze winged helmet with symmetrical feathered side wings, charcoal-grey undertunic with weathered sepia hem edge, dark-charcoal chlamys with gold shoulder clasp, brown leather cross-body harness and messenger pouch, bronze bracers and greaves, and twin-serpent winged caduceus.
- **Sandal-Wing Symmetry & Anti-Inversion:** Preserve one pale feathered wing projecting outward from the outer ankle of the left boot and one matching pale feathered wing projecting outward from the outer ankle of the right boot, with smooth, wingless inner ankles between the legs—no inverted wings, no flipped anatomy, no mirrored limbs, and no wrong-side wing placement.
- **Curb-Side Gold Energy Confinement:** Liquid warm-gold pulses stay strictly inside the shallow gutters along the inside base of the left and right stone curbs; the center limestone roadbed remains unlit stone with no meandering center-road gold river.
- **Style & Medium:** Traditional Japanese woodblock-print (ukiyo-e) illustration on aged speckled parchment with distinct dark-ink keyline contours and flat opaque color areas.

## 4. Camera and delivery
- Fixed locked-off camera (`16:9`, `720p`, `duration: 5`, `audio: false`, `upscale: false`, no pan, zoom, push, or cut).

## 5. At risk and success checks
| Requested outcome / risk | Guard and observable review criterion |
|---|---|
| Walking cadence & end-of-clip deceleration | State explicit ~2 steps/second forward stride and require no slowing down or stopping in the final second; verify continuous stride through final frame. |
| Paired sandal-wing symmetry / depth inversion | State outward-projecting outer-ankle wings on both boots, smooth wingless inner ankles between the legs, and explicit anti-inversion guards (no inverted wings, no flipped anatomy, no mirrored limbs, no wrong-side wing placement). |
| Curb-gutter liquid gold pulses | State that brief warm-gold energy pulses run strictly along the inside base of the left and right stone curbs on footfalls while the center limestone roadbed remains unlit stone. |
| Ukiyo-e medium & locked camera | State fixed camera and flat 2D woodblock print finish with dark ink keylines; no 3D/photorealistic makeover. |

## 6. Prompt
Animate the supplied reference image as one continuous five-second shot from a completely fixed camera. Hermes strides forward toward the foreground along the cracked limestone road at a steady pace of about two steps per second, maintaining his full-stride cadence right through the final frame with no slowing down, stopping, or settling in the final second. As he walks, he makes a slight, natural head turn toward the fluted stone route marker on screen-right and then aligns his calm, focused gaze forward again, while his dark-charcoal chlamys cloak billows lightly with his steps and his right hand carries the bronze twin-serpent winged caduceus coherently at his side.

On each planted footstep, a brief pulse of liquid warm-gold energy surges along the shallow carved stone gutters running strictly along the inside base of the left and right stone curbs bordering the road, easing back between steps while the entire center limestone roadbed remains unlit matte stone with no gold lines in the middle of the road.

Preserve the supplied character's exact visual design, proportions, square-jawed bronze face, golden-brown curls, antique-bronze winged helmet with symmetrical side wings, charcoal-grey undertunic with sepia hem edge, dark-charcoal cloak with gold clasp, brown leather cross-body harness and hip pouch, and bronze bracers and greaves. Keep his winged sandals symmetrical throughout every step: one pale feathered wing projecting outward from the outer ankle of the left boot and one matching pale feathered wing projecting outward from the outer ankle of the right boot, with completely smooth, wingless inner ankles between his legs—no inverted wings, no flipped anatomy, no mirrored limbs, and no wrong-side wing placement. Preserve the grounded stone causeway, curbs, cypress trees, hilltop temple, dusk palette, and traditional Japanese woodblock-print (ukiyo-e) illustration with dark ink keylines, flat color planes, and matte parchment texture, with no camera movement, no pan, no zoom, and no 3D realism.
