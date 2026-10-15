---
set: processional-causeway
shot: causeway-stride
attempt: 3
stage: 01_spec
status: approved
generated: 2026-10-15
sources:
  - runs/studio/causeway-reference-trial/00-intake-1.md
  - runs/processional-causeway/causeway-stride/00-brief.md
  - runs/processional-causeway/causeway-stride/02-render-2.md
  - world/environment.md
  - world/environment/core.md
  - world/environment/palette-and-light.md
  - world/environment/materials-and-wear.md
  - world/environment/forms-and-architecture.md
  - world/environment/locations/processional-causeway.md
  - world/style.md
  - world/characters/hermes.md
  - world/references/hermes-body-turnaround.md
  - world/references/hermes-body-turnaround.png
  - world/references/hermes-sandals-turnaround.md
  - world/references/hermes-sandals-turnaround.png
  - world/references/hermes-props-sheet.md
  - world/references/hermes-props-sheet.png
---

# causeway-stride, spec 3

## 0. World-input manifest
| Path | Role / ID | SHA-256 |
|---|---|---|
| `runs/studio/causeway-reference-trial/00-intake-1.md` | Studio intake (`gate_mode: visual-only`) | `f65f16ac6aa6c26718d012c9a171237d1a50619270265559bc4fdddb2a17c917` |
| `runs/processional-causeway/causeway-stride/00-brief.md` | Approved shot brief | `049b77d6ab34f149b2c97b5b522fa97d0d42c45f743ec8d43a7d7a4a0160e943` |
| `runs/processional-causeway/causeway-stride/02-render-2.md` | Prior render record (`verdict: drifted`) | `8892c52f49642e0456d0657f03a2150dbc50491c4c6720eb72727704efb9be75` |
| `world/environment.md` | Environment index | `8b14aa19c190f8b3760811160e90ecc037d7a3079e5194f9a781d52f570f8d19` |
| `world/environment/core.md` | Shared module: core world rules | `50c1917fa78d2fbf5757eada9859e058971e7959cdc42a919b275c2c39fcb11a` |
| `world/environment/palette-and-light.md` | Shared module: palette and light | `17d78431f39d55efa06fb55b9219ab31a2dbde9050140bfa863c89008d4736da` |
| `world/environment/materials-and-wear.md` | Shared module: materials and wear | `f90b2bd8d1cebbdc5119b9e7639a31b7b9064616df632db0f21060238be940b5` |
| `world/environment/forms-and-architecture.md` | Shared module: forms and architecture | `4db8eb6bef73f6658dd6152165e5136b7956520b1a2094651f915e29b9428ba5` |
| `world/environment/locations/processional-causeway.md` | Selected location: Processional Causeway | `c86a6f7532c3ae01db83f870b9d60e2e299e29489299cf4569581a3816cec4f0` |
| `world/style.md` | Style and camera defaults | `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc` |
| `world/characters/hermes.md` | Character bible: Hermes | `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88` |
| `world/references/hermes-body-turnaround.md` | `#hermes-default-body-turnaround` permission | `d1ac8bd12590851c2bcb736d71c8dd2882e90fb1bbc877a2b99dee3da8a32579` |
| `world/references/hermes-body-turnaround.png` | Reference image 1: 4-view body turnaround | `a8d93020d3c56a4a5e37ef40c50abb8af87c4138fecd12af26d8e39b132b875e` |
| `world/references/hermes-sandals-turnaround.md` | `#hermes-sandals-4-view` permission | `1532758ea4aa24c7b0f40ab0584ec193df02b845f33db1d54184a03e364f33fa` |
| `world/references/hermes-sandals-turnaround.png` | Reference image 2: 4-view sandals turnaround | `7bddb1f10633ec5e049d7ba1e3b96c42961cfca05583111f6c0681ffe27510dc` |
| `world/references/hermes-props-sheet.md` | `#hermes-canonical-props` permission | `38e9330b9253fd8b46bbb2466382fde4b82674cdcc541502444ba655b035f4eb` |
| `world/references/hermes-props-sheet.png` | Reference image 3: canonical props sheet | `1d043eeafdc28a530d91705d4ae2f1bbc1cee006a9808ed1dcbb474ef69d0b3e` |

## 1. Brief
- **Characters in frame:** `hermes` (`world/characters/hermes.md`).
- **Action:** Hermes strides rightward up the gently rising Processional Causeway while carrying his active warm-gold twin-serpent winged caduceus in his right hand.
- **Pose and expression:** Full-body rightward profile stride where the **trailing left leg (on image-left, farther from the camera)** shows its camera-facing **inner ankle** completely smooth and wingless, and the **leading right leg (on image-right, closer to the camera)** shows its single pale feathered wing attached directly to its camera-facing **outer ankle strap**, fanning backward behind the heel.
- **Wardrobe state:** `default`.
- **Location:** `world/environment/locations/processional-causeway.md` (Processional Causeway), with deterministic warm-gold energy lines running strictly along the **inside base of both stone curbs** (left curb and right curb) rather than meandering through the center of the roadbed.
- **Time of day and weather:** Clear dusk with amber, orange, and gold horizon light and long hard-edged woodblock shadows.
- **Camera:** Full body in medium-wide framing (16:9, 28mm full-frame equivalent, deep focus).
- **Execution method for Attempt 3 (Option 1 — Deterministic Region Targeting & Curb-Line Pass on `02-image-2.png`):**
  1. **Isolate & Inpaint / Region Transfer on Boots:** Erase the misplaced inner-ankle wing from the trailing left leg (`x=340..412, y=548..652`) and composite the canonical pale feathered wing onto the camera-facing **outer ankle strap** of the leading right leg (`dest=(510, 566)`, `-8°` alignment), so the right foot has its wing on the outside and the left foot has zero wing on the inside.
  2. **Deterministic Curb-Side Gold Energy Lines:** Erase the drifted meandering gold line down the middle of the roadbed (`y=250..751`) back to clean matte limestone paving, and draw two deterministic perspective-tapered warm-gold energy channels (`#f8cc62` core, `#704a24` carved stone groove edge, `#e8ac48` subtle curb-base glow) strictly along the **inside base of both stone curbs** (`left_curb_pts` and `right_curb_pts`), with proper depth occlusion behind Hermes's legs and visible across the open stone gap between his ankles.

## 2. Characters in frame
Same invariants and variables as `01-spec-2.md`, with true anatomical/screen-space depth sorting enforced:
- **Trailing left foot (image-left, farther from camera):** Camera-facing surface is the **inner ankle** → completely smooth brown leather and bronze greave, zero wing.
- **Leading right foot (image-right, closer to camera):** Camera-facing surface is the **outer ankle** → single pale feathered wing attached to the outer ankle strap and fanning backward behind the heel.

## 3. Scene
Same Processional Causeway scene as `01-spec-2.md`, with active warm-gold route channels fixed deterministically along the **inside edges of the left and right stone curbs** rather than left to freehand prompt meandering down the center of the road.

## 4. Camera
16:9 (`1344x752`), 28mm full-frame equivalent, slightly below eye level, deep focus.

## 5. At risk
| The shot has | At risk | Guard / Deterministic Fix |
|---|---|---|
| 2D depth-flipping ambiguity on striding legs (`02-render-2.md` drift) | Model confuses anatomical left/right with screen-space left/right, placing the wing on the inside of the far (left) foot and omitting the wing on the outside of the near (right) foot | **Deterministic region targeting:** isolate the boot region on `02-image-2.png`, erase the inner wing on the trailing left boot (`x=340..412, y=548..652`), and attach the canonical pale feathered wing directly to the camera-facing outer ankle strap of the leading right boot (`dest=(510, 566)`). |
| Freehand prompt drift on active gold route channels (`02-render-2.md` drift) | Model draws a meandering gold line down the middle of the roadbed instead of locking channels to the curb edges | **Deterministic post-render prop/feature pass:** strip the meandering center-road gold line (`y=250..751`) to clean limestone paving and render two perspective-locked warm-gold channels along the inside base of the left and right stone curbs (`left_curb_pts`, `right_curb_pts`) with leg occlusion. |

## 6. Prompt
Deterministic local region repair + curb-line pass executed on `runs/processional-causeway/causeway-stride/02-image-2.png` (`sha256:ab48b8150edc34cff1351483be7c4def6eaacca5f817359a963fd554090a112b`) producing `runs/processional-causeway/causeway-stride/02-image-3.png` (`sha256:8eebb3c47e344d2cfbec97db3ab1731c97879dfaeace40ecd034a3ec69db4432`).
