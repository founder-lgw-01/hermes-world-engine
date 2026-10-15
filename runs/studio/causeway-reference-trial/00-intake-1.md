---
production: causeway-reference-trial
attempt: 1
stage: studio/00_intake
status: approved
generated: 2026-10-15
sources:
  - world/environment.md
  - world/environment/locations/processional-causeway.md
  - world/style.md
  - world/characters/hermes.md
  - world/references/hermes-body-turnaround.md
  - world/references/hermes-sandals-turnaround.md
  - world/references/hermes-props-sheet.md
---

# causeway-reference-trial, intake and route

## Outcome
- Deliverable: Single animated shot (new-scene mode: still image + 5s motion clip).
- Audience and purpose for this production: Jordan Shaw / Hermetic Gates studio verification of the new 4-view Hermes reference sheets (`hermes-body-turnaround.png`, `hermes-sandals-turnaround.png`, `hermes-props-sheet.png`) under `gate_mode: visual-only`.
- What should the viewer understand or feel: Hermes striding purposefully along the grounded Processional Causeway at dusk with an active warm-gold caduceus, displaying clean first-try sandal wing symmetry (one outer heel wing per sandal, smooth wingless inner ankles) and accurate default charcoal wardrobe colors.
- Accepted endpoint and observable result: Accepted and filed still (`runs/processional-causeway/causeway-stride/`) plus accepted and filed 5-second motion clip (`runs/motion/processional-causeway/causeway-stride/`).

## Roles
- Producer: Hermes.
- First reviewer: Hermes; not independent review.
- Human approver: Jordan.
- Canonical-record/receiving responsibilities or explicit reassignments: Hermes writes and hashes all intermediate Markdown records under `gate_mode: visual-only` and pauses at spend/publish and visual `MEDIA:` acceptance gates.

## Selected route
- Selected contracts in execution order, including conditional preparation: `studio/00_intake/CONTEXT.md` → `01_spec/CONTEXT.md` → `02_render/CONTEXT.md` (visual check) → `03_file/CONTEXT.md` → `04_animate/CONTEXT.md` (visual check and filing).
- Skipped work and why: `00_setup` (all world/location/character/reference records are already `status: approved`), `studio/01_story` and `studio/02_sequence` (single animated shot does not require multi-shot sequence reconciliation), `05_compose` (no finishing/audio/text overlay requested).
- Existing handoff to resume, if any: none.
- Composition brief path or none: none.

## Assets and preparation
| Need | Reusable exact artifact and authoritative acceptance evidence, or missing | Preparation task/owning contract | Expected output | Receiver |
|---|---|---|---|---|
| Character bible | `world/characters/hermes.md` (`status: approved`) | none | reused unchanged | `01_spec`, `04_animate` |
| Location & environment modules | `world/environment.md`, `world/environment/core.md`, `world/environment/palette-and-light.md`, `world/environment/materials-and-wear.md`, `world/environment/forms-and-architecture.md`, `world/environment/locations/processional-causeway.md` (`status: approved`) | none | reused unchanged | `01_spec`, `04_animate` |
| Multi-view character & prop reference sheets | `world/references/hermes-body-turnaround.md` + `.png`, `world/references/hermes-sandals-turnaround.md` + `.png`, `world/references/hermes-props-sheet.md` + `.png` (`status: approved`) | none | passed as 3 `reference_image_urls` / `image_references` | `01_spec`, `02_render` |
| Starting still image | missing (new-scene mode) | `01_spec` → `02_render` → `03_file` | `runs/processional-causeway/causeway-stride/02-image-1.png` + `03-sidecar.md` | `04_animate` |

## Handoff
| Exact input path/version | Role in this request | SHA-256 when approved and selected | Authoritative approval evidence |
|---|---|---|---|
| `world/environment.md` | Environment index | `8b14aa19c190f8b3760811160e90ecc037d7a3079e5194f9a781d52f570f8d19` | `status: approved` |
| `world/environment/core.md` | Core world rules | `50c1917fa78d2fbf5757eada9859e058971e7959cdc42a919b275c2c39fcb11a` | `status: approved` |
| `world/environment/palette-and-light.md` | Palette and light rules | `17d78431f39d55efa06fb55b9219ab31a2dbde9050140bfa863c89008d4736da` | `status: approved` |
| `world/environment/materials-and-wear.md` | Material and wear rules | `f90b2bd8d1cebbdc5119b9e7639a31b7b9064616df632db0f21060238be940b5` | `status: approved` |
| `world/environment/forms-and-architecture.md` | Forms and architecture rules | `4db8eb6bef73f6658dd6152165e5136b7956520b1a2094651f915e29b9428ba5` | `status: approved` |
| `world/environment/locations/processional-causeway.md` | Selected location record | `c86a6f7532c3ae01db83f870b9d60e2e299e29489299cf4569581a3816cec4f0` | `status: approved` |
| `world/style.md` | Style and camera rules | `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc` | `status: approved` |
| `world/characters/hermes.md` | Character bible | `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88` | `status: approved` |
| `world/references/hermes-body-turnaround.md` | Full-body 4-view reference permission | `d1ac8bd12590851c2bcb736d71c8dd2882e90fb1bbc877a2b99dee3da8a32579` | `status: approved` |
| `world/references/hermes-sandals-turnaround.md` | Sandals 4-view reference permission | `1532758ea4aa24c7b0f40ab0584ec193df02b845f33db1d54184a03e364f33fa` | `status: approved` |
| `world/references/hermes-props-sheet.md` | Canonical props reference permission | `38e9330b9253fd8b46bbb2466382fde4b82674cdcc541502444ba655b035f4eb` | `status: approved` |

- Receiving producer and expected output: Hermes (`01_spec` → `runs/processional-causeway/causeway-stride/00-brief.md` and `01-spec-1.md`, then `04_animate` draft brief `runs/motion/processional-causeway/causeway-stride/00-brief.md`).
- Checks completed / remaining uncertainty: All upstream world, character, location, and reference permission records are verified `status: approved` with matching SHA-256 hashes.
- Prerequisites required before the next specification: None for `01_spec`; `04_animate` spec requires accepted and filed still from `02_render`/`03_file`.
- Revision impact, superseded intake if any, and why reuse remains valid: First intake (`00-intake-1.md`) for `causeway-reference-trial`.

## Acceptance criteria
| Selected deliverable/check | Observable evidence required | Human decision needed |
|---|---|---|
| Starting still (`02-render-1.md`) | Ukiyo-e woodblock print style on aged parchment; Hermes in default charcoal undertunic and dark-charcoal chlamys; un-crossed stride showing 1 outer heel wing per sandal and smooth wingless inner ankles; active warm-gold caduceus in right hand; Processional Causeway at dusk. | Visual acceptance (`verdict: accepted` \| `drifted`) on `MEDIA:` still. |
| Animated clip (`04-render-1.md`) | 5s, 16:9, 720p continuous forward stride at ~2 steps/sec without end-of-clip stop, turning head toward glowing route marker ahead while preserving wardrobe and sandal wing symmetry. | Visual acceptance (`verdict: accepted` \| `drifted`) on `MEDIA:` video. |

## Approval scope
- Gate mode (`strict` | `visual-only`): `visual-only`
- Named artifact versions in this review package: `runs/studio/causeway-reference-trial/00-intake-1.md`, `runs/processional-causeway/causeway-stride/00-brief.md`, `runs/processional-causeway/causeway-stride/01-spec-1.md`.
- Actions this approval permits: Auto-advance intermediate Markdown artifacts (`00-intake-1.md`, `00-brief.md`, `01-spec-1.md`) with `status: approved` under `gate_mode: visual-only` (`approved visual only`, 2026-10-15).
- Separate approvals still required (spec/production, results, final acceptance): Spend/publish gate before paid generation or public image hosting, and visual `MEDIA:` acceptance gates on `02-render-1.md` and `04-render-1.md`.
- Spending or publication: Pauses at spend preflight unless explicitly authorized.

## Open
- Unanswered scope questions and blocking decisions: None.
