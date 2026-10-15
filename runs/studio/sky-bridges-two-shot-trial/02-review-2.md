---
production: sky-bridges-two-shot-trial
attempt: 2
stage: studio/02_sequence
status: approved
verdict: accepted
generated: 2026-10-15T07:28:11.000000+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-2.md
  - stories/hermetic-gates/01-foundation-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/studio/sky-bridges-two-shot-trial/05-record-1.md
  - runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, observed sequence reconciliation (attempt 2 — post-playback drift notes and next-pass routing)

Copy to `runs/studio/<production>/02-review-N.md` only after selected clips are
accepted and filed. Do not populate observations from planned states or prompts.

## Baseline
| Exact approved intake/sequence/storyboard/continuity version | SHA-256 | Approval evidence |
|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md` | `d0488f7c40353077e3b0e72059e95cff56ec7c62e28d67ef8d42ba274c65323f` | `status: approved`; Jordan desktop chat: “approve” |
| `stories/hermetic-gates/01-foundation-1.md` | `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` | `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` | `a7ab1bebede8d5fd559179cb3fdacd002df71d5c094b19d7ffddfe62183eb476` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` | `620ceb8ebff65d141cd529b176060b431afd21d5dcb37c9f3e2fc92a7383b077` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` | `5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a` | `status: approved`, `verdict: accepted`; preserved historical structural acceptance |
| `runs/studio/sky-bridges-two-shot-trial/05-record-1.md` | `cc4c90327c60f009f9e356842ee71250b3a2c2ac52d86ad62ff2b11141fe092f` | `status: approved`, `verdict: accepted`; preserved historical export acceptance |

## Selected clips
| Shot ID | Clip path | Clip SHA-256 | Accepted record/version | Record SHA-256 | Spec and manifest filing evidence |
|---|---|---|---|---|---|
| `shot-01` | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` (`attempt: 1`, `status: approved`, `verdict: accepted`) | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | Spec `01-spec-1.md` (`bdbe137fa8e12c282db672c847f3775d4a91443597c3b6282ed572ffcce1c5e3`); filed in `runs/motion/location-probes/manifest.md` (`aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d`, row 1) |
| `shot-02` | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` (`attempt: 1`, `status: approved`, `verdict: accepted`) | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | Spec `01-spec-1.md` (`1f1f1b9bd65db66e24f559acc90f71ce69a6df93c1180f16518742ad2018c5e3`); source sidecar `00-source-1.md` (`e6fbcd12646e616d4ce7c94f7f705453968f82ed3935443dec67c3f2468a2d66`); filed in `runs/motion/location-probes/manifest.md`, row 2 |

## Observed states
| Shot ID | Expected start/end state IDs | Observed start | Observed end | Timestamp/evidence | Result and limitations |
|---|---|---|---|---|---|
| `shot-01` | `state-01` → `state-02` | Frame 0 (`0.0s`): foreground-facing stride on near viaduct; baseline dusk lighting. | Frame 120 (`5.0s`): pivoted rear-facing in stride on near paving. | Full-playback operator review of `05-final-1.mp4` (`0.0s–5.04s`) plus `04-render-1.md`. | `drifted` on sandal heel-wing symmetry during rear-view motion (operator playback observation: 2 wings appear on one foot and 1 small wing on the other). |
| `shot-02` | `state-02` → `state-03` | Frame 0 (`0.0s` of `shot-02`, `5.04s` of `05-final-1.mp4`): starts from decoded frame 120 of `shot-01`, but develops a slight overall lighting shift and changed walking cadence relative to `shot-01`. | Frame 240 (`10.0s` of `shot-02`, `15.08s` of `05-final-1.mp4`): rear-facing stride deeper on the viaduct; background sky/ravine remains static. | Full-playback operator review of `05-final-1.mp4` (`5.04s–15.08s`) plus `04-render-1.md`. | `drifted` on: (1) slight lighting shift between `shot-01` and `shot-02`, (2) gait pace/cadence change between `shot-01` and `shot-02`, (3) sandal heel-wing asymmetry (`2 on 1 foot and 1 small on the other`), and (4) warm-gold channel flare/bloom (`2.75–4.0s`, `7.5–8.5s`). |

## Adjacent-shot reconciliation
| Outgoing shot | Incoming shot | States agree or approved transition | Actual evidence | Blocking mismatch/uncertainty or none |
|---|---|---|---|---|
| `shot-01` (`hermes-sky-bridges-destination-walk`) | `shot-02` (`hermes-sky-bridges-stride-continuation`) | Direct match-frame continuation (`state-02` → `state-02`) at `5.041667s` (`frame 120` → `frame 121`). | Operator playback inspection of `runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4` (`2581a6eb24e227aeb81d6642e4c29d8ad7791e583efaa106cd9b20977374e9d7`). | **Three observed continuity/specificity issues + one next-pass creative addition:**<br>1. **Slight lighting change between `shot-01` and `shot-02`** across the `5.04s` cut and during `shot-02`'s gold-channel surges.<br>2. **Gait pace change between `shot-01` and `shot-02`** (single decoded frame `00-source-frame.png` carries pose, not walking velocity/cadence).<br>3. **Footwear wing drift:** Hermes's sandals show `2 wings on 1 foot and 1 small wing on the other` during rear-view walking.<br>4. **Next-pass background motion recommendation:** Add ambient movement in the background (several birds flying in the distance), replacing the current *"Background motion remains quiet"* constraint. |

## Handoff
- Receiving composition producer and exact selected clip set: Preserves historical acceptance of `02-review-1.md` and `05-record-1.md` (`05-final-1.mp4`) for the structural pass. Any specificity pass routes upstream before a new `05_compose` attempt.
- Story success, identity/continuity checks and any review limitations: Operator playback review identified four concrete items that static 6-frame contact-sheet sampling did not fully resolve (cross-clip lighting shift, gait cadence change, asymmetrical sandal heel-wings, and static background needing distant birds).
- Revision impact and required upstream correction, if any (for post-playback operator drift notes or next-pass recommendations, open the next numbered `runs/studio/<production>/02-review-N.md` as `status: draft` and route each item to its owning contract while preserving the prior accepted review):
  1. **Slight lighting shift (`shot-01` vs. `shot-02`)** → **Can be mitigated without regenerating video** in `05_compose` (`05-spec-2.md`) using an `ffmpeg` eq/colorlevels/curves exposure-matching filter + short cross-dissolve or luma match across the cut, **or** upstream in `04_animate` by guarding global scene luminance against drift from `00-source-frame.png`.
  2. **Gait pace change (`shot-01` vs. `shot-02`)** → **Partially adjustable without regenerating video** via `05_compose` time-warping (`setpts` / optical-flow `minterpolate` on one clip to match step cadence), **or** upstream in `02-continuity-2.md` + `04_animate` (`01-spec-N.md`) by specifying explicit step count/cadence across the clip duration.
  3. **Sandal heel-wing drift (`2 on 1 foot and 1 small on the other`)** → **Requires video regeneration (or external frame-by-frame inpainting)** because it is baked into the generated pixels of the moving feet; routes to `04_animate` (`01-spec-N.md` **What holds** and **At risk**: *"exactly one matching pale feathered wing on the outer heel of each sandal—symmetrical left and right boots, never two wings on one foot"*).
  4. **Add background movement (`several birds flying in the distance`)** → **Can be composited in `05_compose` as a 2D animated overlay layer** over the upper-right sky/ravine without regenerating Hermes's walk, **or** routed upstream to `02-sequence-2.md` and `04_animate` (`00-brief.md` **Secondary motion**) to replace *"Background motion remains quiet"* when regenerating `shot-01`/`shot-02`.

## Open
- Required unresolved mismatches or uninspected evidence:
  1. Ready for operator approval (`status: approved`, `verdict: accepted`) as the sequence-reconciliation baseline authorizing `05_compose` (`05-spec-2.md`) to remediate items 1 (lighting shift), 2 (gait pace mismatch), and 4 (distant background birds) in post-production while explicitly deferring item 3 (sandal heel-wing asymmetry) to a future `04_animate` regeneration pass.

## Acceptance evidence
Acceptance is pending until the human decides on this exact review/version.
Status/verdict are authoritative; cite a real operator decision only if already
available when this record is derived. Later approval changes metadata only,
not observed findings. An accepted clip is not automatically an accepted sequence.
