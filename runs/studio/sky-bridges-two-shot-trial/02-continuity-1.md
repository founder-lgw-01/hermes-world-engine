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
  - world/characters/hermes.md
  - runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md
---

# sky-bridges-two-shot-trial, expected continuity baseline

Copy to `runs/studio/<production>/02-continuity-N.md`. Define each state once;
shots reference state IDs. Fixed geography belongs in the named spatial record.

## States
| State ID | Characters present and positions | Prop positions/counts | Activation/power/other relevant state | Canonical identity/map references |
|---|---|---|---|---|
| `state-01` | Hermes (1 character) on the near stretch of the Sky-Bridges limestone causeway inside the parapet, foreground-facing in stride with head oriented screen-right toward the distant city. | 1 twin-serpent winged caduceus held in hand; existing left-wall heraldic banners present in background. | Carved warm-gold channels along the causeway edges and corners at steady baseline dusk luminosity. | `world/characters/hermes.md` (`bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88`); `world/environment/locations/sky-bridges-and-passages.md` (`e6264ac973e032d2dd8e5dc678b2d6a3a6a2907ed9bb1ee80c871cf6e82c7010`); `runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md` (`9b0af53149e22e75fea88b9c6adfc1cca8d9cf3c12259bb255afd91f64215a02`). |
| `state-02` | Hermes (1 character) pivoted rear/away-facing, displaced diagonally screen-right and slightly deeper along the near stone paving inside the parapet, mid-stride with head aligned along the route ahead. | 1 twin-serpent winged caduceus carried with him (partly occluded by body/cloak in rear view); existing left-wall banners unchanged. | Carved warm-gold channels at baseline dusk luminosity prior to step-linked surges. | `world/characters/hermes.md`; `world/environment/locations/sky-bridges-and-passages.md`; `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md` (`e6fbcd12646e616d4ce7c94f7f705453968f82ed3935443dec67c3f2468a2d66`). |
| `state-03` | Hermes (1 character) still rear/away-facing, displaced further screen-right and deeper along the near paved viaduct inside the parapet (not yet arriving at the distant city), still striding forward without a final stop or settle. | 1 twin-serpent winged caduceus carried coherently (partly occluded in rear view); existing left-wall banners unchanged. | Carved warm-gold channels along the causeway edges have surged in brightness during his steps and eased back toward baseline intensity within the existing channel paths. | `world/characters/hermes.md`; `world/environment/locations/sky-bridges-and-passages.md`. |

Use only fields the sequence needs. Do not impose the example scene's folders,
five agents or power system on other productions. Unknown is not permission to
invent a value; a required unknown blocks approval.

## Shot transitions
| Shot ID | Start state ID | End state ID | Next shot ID | Intended change between shots | Transition approval |
|---|---|---|---|---|---|
| `shot-01` | `state-01` | `state-02` | `shot-02` | Direct continuous match-frame continuation (`state-02` → `state-02`): `shot-02` starts from the exact final decoded frame (`frame 120`, 5.0s) of `shot-01` in the same locked camera framing with no scene cut, camera jump, or pose reset. | Approved in `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` (`04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab`) and `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md` (`e6fbcd12646e616d4ce7c94f7f705453968f82ed3935443dec67c3f2468a2d66`). |
| `shot-02` | `state-02` | `state-03` | `none` | Sequence ends in active forward stride (`state-03`) on the near viaduct without a final settle. | Approved in `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` (`04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab`). |

Ordinary adjacent end/start states agree. An intentional discontinuity links
its approved event/transition. Shot order is owned by the storyboard, not this
table. These are expectations, not claims about generated media.

## Handoff
- Exact approved sequence and spatial input versions/hashes:
  - `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` (`status: approved`, SHA-256 `1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f`)
  - `stories/hermetic-gates/01-foundation-1.md` (`status: approved`, SHA-256 `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd`)
  - `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` (`status: approved`, SHA-256 `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab`)
  - `world/environment/locations/sky-bridges-and-passages.md` (`status: approved`, SHA-256 `e6264ac973e032d2dd8e5dc678b2d6a3a6a2907ed9bb1ee80c871cf6e82c7010`)
  - `world/characters/hermes.md` (`status: approved`, SHA-256 `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88`)
- Storyboard version proposed for the same review package: `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` (working sibling cross-reference; not hashed into this draft to avoid circular hash dependencies).
- Receiving shot producers and required observed success criteria: Hermes (`studio/02_sequence` review pass → `runs/studio/sky-bridges-two-shot-trial/02-review-1.md`), checking actual observed start/end states (`state-01` → `state-02` → `state-03`), the `shot-01` → `shot-02` boundary join, channel-pulse behavior, and foot contact against this baseline.
- Prior baseline and affected shot IDs for a revision: First continuity baseline (`attempt: 1`); no prior baseline.

## Open
- Unresolved required state or transition decisions: none. Ready for package approval alongside `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md`.
