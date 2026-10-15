---
production: sky-bridges-two-shot-trial
attempt: 1
stage: studio/02_sequence
status: approved
generated: 2026-10-15T06:59:08.178017+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-1.md
  - stories/hermetic-gates/01-foundation-1.md
  - world/environment/locations/sky-bridges-and-passages.md
  - world/characters/hermes.md
---

# sky-bridges-two-shot-trial, sequence brief

Copy to `runs/studio/<production>/02-sequence-N.md`. Derive events only after
intake and the selected story foundation are approved. Do not specify shots yet.

## Approved intent
- Intake path/version (audience and purpose): `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` (`attempt: 1`, `status: approved`, SHA-256 `1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f`).
- Series foundation path/version: `stories/hermetic-gates/01-foundation-1.md` (`attempt: 1`, `status: approved`, SHA-256 `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd`).
- Observable story outcome: Across two continuous fixed-camera shots on the grounded limestone viaduct, Hermes turns from his initial foreground-facing posture toward the distant city route and strides deeper along the paved causeway while the carved warm-gold stone channels respond to his passage.
- Beginning / change / ending:
  - **Beginning:** Hermes stands/strides foreground-facing on the near stretch of the Sky-Bridges limestone causeway inside the parapet, looking toward the distant city at screen-right while the carved stone channels hold their baseline warm-gold luminosity.
  - **Change:** In Event 1 (`evt-01-commit-to-route`), Hermes pivots his feet, hips, and shoulders onto the rightward-curving road and walks away into depth along the near paving. In Event 2 (`evt-02-active-causeway-stride`), continuing immediately from that away-facing stride without resetting pose or camera, his footsteps along the stone paving trigger visible warm-gold surges in the carved causeway channels.
  - **Ending:** Hermes remains on the near paved viaduct inside the parapet, still striding forward away from the camera toward the distant city with no stop or final settle.

## Events
| Event ID | What happens | Characters/props required by exact record | Observable success |
|---|---|---|---|
| `evt-01-commit-to-route` | Hermes surveys the distant city, pivots naturally from his foreground-facing orientation onto the rightward-curving limestone viaduct, and begins walking away at a measured pace along the near paving inside the parapet. | `world/characters/hermes.md` (Hermes in default winged helmet, slate-grey/charcoal undertunic, dark cloak, bronze armor, winged sandals, carrying twin-serpent caduceus) | Clear body pivot from foreground-facing to rear/away-facing, net walking displacement screen-right and into depth on the near road, fixed camera, and continuing stride at the clip's end. |
| `evt-02-active-causeway-stride` | Continuing immediately from the end of `evt-01-commit-to-route` in the same fixed framing, Hermes strides further along the paved causeway while the carved warm-gold stone channels along the causeway edges surge in response to his passage and ease back between surges. | `world/characters/hermes.md` (same character/wardrobe and carried caduceus, now seen from rear/away-facing angle); `world/environment/locations/sky-bridges-and-passages.md` (carved warm-gold stone channels along the limestone viaduct) | Immediate continuation from the outgoing away-facing pose without a repeated pivot or scene cut, continued forward displacement along the near paving, visible warm-gold brightness surges in the existing carved channels, and a continuing stride at the end. |

## Spatial needs
- Selected locations/maps, by exact approved owner path: `world/environment/locations/sky-bridges-and-passages.md` (`status: approved`, SHA-256 `e6264ac973e032d2dd8e5dc678b2d6a3a6a2907ed9bb1ee80c871cf6e82c7010`) and the accepted reference scene `runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md` (`status: approved`).
- Missing/unknown geography to resolve through setup before dependent specs: none — both shots remain on the same near stretch of the approved Sky-Bridges viaduct from the same fixed camera position; no new spatial map or location record is required.
- Early composition requirements: none (`Composition brief path: none` in `00-intake-1.md`).

## Handoff
| Exact approved source/version | SHA-256 | Approval evidence |
|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` | `1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f` | `status: approved`; Jordan desktop chat: “approve” |
| `stories/hermetic-gates/01-foundation-1.md` | `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd` | `status: approved`; Jordan desktop chat: “approve” |
| `world/environment/locations/sky-bridges-and-passages.md` | `e6264ac973e032d2dd8e5dc678b2d6a3a6a2907ed9bb1ee80c871cf6e82c7010` | `status: approved` (`stage: 00_setup`, 2026-09-29) |
| `world/characters/hermes.md` | `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88` | `status: approved` (`stage: 00_setup`, 2026-09-29) |

- Receiver: Hermes (`studio/02_sequence` storyboard and continuity planning producer).
- Expected outputs and selected acceptance checks: `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` and `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` defining stable shot IDs (`shot-01`, `shot-02`), coverage mapping to the existing accepted clips, and canonical start/end continuity states (`state-01` through `state-03`).
- Reused inputs versus preparation tasks: Both shots reuse existing accepted motion clips in `runs/motion/location-probes/manifest.md`; no missing location setup or new asset generation is required.
- Revision impact and previous version, if applicable: First sequence brief (`attempt: 1`); no previous version.

## Open
- Blocking intent decisions: none. Ready for human review and approval of `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` before deriving `02-storyboard-1.md` and `02-continuity-1.md`.
