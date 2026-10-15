---
production: sky-bridges-two-shot-trial
attempt: 1
stage: studio/02_sequence
status: approved
generated: 2026-10-15T07:01:44.737470+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-1.md
  - stories/hermetic-gates/01-foundation-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md
  - world/environment/locations/sky-bridges-and-passages.md
  - runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md
---

# sky-bridges-two-shot-trial, storyboard and required coverage

Copy to `runs/studio/<production>/02-storyboard-N.md`. Use stable shot IDs, not
filenames alone, to connect approved events, coverage, continuity and shot briefs.
This record owns shot order/composition intent; continuity owns changing states.

## Spatial baseline
| Exact approved map/location version | SHA-256 | Facts/available camera space used | Approval evidence |
|---|---|---|---|
| `world/environment/locations/sky-bridges-and-passages.md` | `e6264ac973e032d2dd8e5dc678b2d6a3a6a2907ed9bb1ee80c871cf6e82c7010` | Grounded limestone viaduct crossing ravines toward Crystal Citadel; weathered limestone bridge paving inside the parapet; warm-gold route light in shallow carved stone channels and thresholds. | `status: approved` (`stage: 00_setup`, 2026-09-29) |
| `runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md` | `9b0af53149e22e75fea88b9c6adfc1cca8d9cf3c12259bb255afd91f64215a02` | Approved wide 16:9 fixed-camera perspective on the near stretch of the viaduct curving screen-right into depth toward the distant city. | `status: approved` (`stage: 03_file`, filed in `runs/location-probes/manifest.md`) |

## Shots
| Order | Shot ID | Approved event ID | Composition intent | Map/view reference | Continuity shot/state reference | Still brief target | Motion brief target or none |
|---|---|---|---|---|---|---|---|
| 1 | `shot-01` | `evt-01-commit-to-route` | Fixed 16:9 wide/medium-wide frame (`cov-01`): Hermes starts in the foreground-left/center third, surveys the distant city at screen-right, pivots naturally away from the viewer, and walks diagonally screen-right into depth along the near stone paving inside the parapet. | `world/environment/locations/sky-bridges-and-passages.md`; `runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md` | `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` (`shot-01`: `state-01` → `state-02`) | `runs/location-probes/hermes-sky-bridges-and-passages/00-brief.md` (already completed and accepted) | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/00-brief.md` (already completed, accepted, and filed) |
| 2 | `shot-02` | `evt-02-active-causeway-stride` | Same locked 16:9 camera framing (`cov-02`, decoded final frame of `shot-01`): Hermes continues his away-facing stride diagonally screen-right into depth along the near paving while the carved warm-gold causeway channels surge in response to his footsteps. | `world/environment/locations/sky-bridges-and-passages.md`; `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md` | `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` (`shot-02`: `state-02` → `state-03`) | none (decoded-frame continuation via `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md`) | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-brief.md` (already completed, accepted, and filed) |

Image targets use `runs/<set>/<shot>/00-brief.md`; motion targets use
`runs/motion/<set>/<shot>/00-brief.md`. Their precise camera/action is approved
in those briefs; do not send a storyboard row directly to a render tool.

## Coverage and preparation
| Coverage ID | Needed by shot IDs | View/identity/prop purpose | Approved reusable record/path or missing | Preparation contract and output | Required approval/receiver |
|---|---|---|---|---|---|
| `cov-01` | `shot-01` | Starting 16:9 still of Hermes on the Sky-Bridges viaduct (`02-image-1.png`, SHA-256 `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3`) | `runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md` (`status: approved`) and `02-render-1.md` (`status: approved`, `verdict: accepted`) | none (reused unchanged) | Already approved; consumed by `shot-01` |
| `cov-02` | `shot-02` | Exact final decoded frame (`frame 120`, 5.0s) of `shot-01` (`00-source-frame.png`, SHA-256 `9525ddf63dd8d6008392dab6ce3196a418fdb322736bbcdb8653924c8d5217fe`) | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md` (`status: approved`, `verdict: accepted`) | none (reused unchanged) | Already approved; consumed by `shot-02` |

Select only required location directions, body/head/expression or prop views.
A planning baseline may name missing imagery; the individual spec waits for its
accepted inputs. Unknown required geography blocks the baseline until setup
resolves it. Do not replace an approved image just because filing is missing.

## Handoff
- Exact approved intake and sequence brief versions/hashes:
  - `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` (`status: approved`, SHA-256 `1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f`)
  - `stories/hermetic-gates/01-foundation-1.md` (`status: approved`, SHA-256 `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd`)
  - `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` (`status: approved`, SHA-256 `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab`)
- Named continuity baseline version to approve in the same package: `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` (working sibling cross-reference; not hashed into this draft to avoid circular hash dependencies).
- Named preparation scope and existing asset approval evidence: No missing coverage or new shot preparation required; both shots (`shot-01` and `shot-02`) are already accepted and filed in `runs/motion/location-probes/manifest.md` (SHA-256 `aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d`).
- Receiving shot producers, expected outputs and acceptance criteria: Hermes (`studio/02_sequence` review pass → `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` reconciling the two accepted clips against `02-storyboard-1.md` and `02-continuity-1.md`).
- Revision impact (which views/shots change and which remain valid): First storyboard (`attempt: 1`); existing accepted stills and motion clips remain valid and unchanged.

## Open
- Unresolved coverage/geography/shot-order decisions: none. Ready for package approval alongside `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md`.
