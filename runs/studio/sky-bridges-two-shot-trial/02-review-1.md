---
production: sky-bridges-two-shot-trial
attempt: 1
stage: studio/02_sequence
status: approved
verdict: accepted
generated: 2026-10-15T07:04:05.806017+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-1.md
  - stories/hermetic-gates/01-foundation-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, observed sequence reconciliation

Copy to `runs/studio/<production>/02-review-N.md` only after selected clips are
accepted and filed. Do not populate observations from planned states or prompts.

## Baseline
| Exact approved intake/sequence/storyboard/continuity version | SHA-256 | Approval evidence |
|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` | `1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f` | `status: approved`; Jordan desktop chat: “approve” |
| `stories/hermetic-gates/01-foundation-1.md` | `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` | `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` | `a7ab1bebede8d5fd559179cb3fdacd002df71d5c094b19d7ffddfe62183eb476` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` | `620ceb8ebff65d141cd529b176060b431afd21d5dcb37c9f3e2fc92a7383b077` | `status: approved`; Jordan desktop chat: “approve” |

## Selected clips
| Shot ID | Clip path | Clip SHA-256 | Accepted record/version | Record SHA-256 | Spec and manifest filing evidence |
|---|---|---|---|---|---|
| `shot-01` | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` (`attempt: 1`, `status: approved`, `verdict: accepted`) | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | Spec `01-spec-1.md` (`bdbe137fa8e12c282db672c847f3775d4a91443597c3b6282ed572ffcce1c5e3`); filed in `runs/motion/location-probes/manifest.md` (`aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d`, row 1, `session 20261003_203006_dd142b`). |
| `shot-02` | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` (`attempt: 1`, `status: approved`, `verdict: accepted`) | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | Spec `01-spec-1.md` (`1f1f1b9bd65db66e24f559acc90f71ce69a6df93c1180f16518742ad2018c5e3`); source sidecar `00-source-1.md` (`e6fbcd12646e616d4ce7c94f7f705453968f82ed3935443dec67c3f2468a2d66`); filed in `runs/motion/location-probes/manifest.md` (`aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d`, row 2, Jordan desktop reply: “accept”). |

## Observed states
| Shot ID | Expected start/end state IDs | Observed start | Observed end | Timestamp/evidence | Result and limitations |
|---|---|---|---|---|---|
| `shot-01` | `state-01` → `state-02` | Frame 0 (0.0s): Hermes stands/strides foreground-facing on the near limestone viaduct inside the parapet with head oriented screen-right toward the distant city; 1 twin-serpent caduceus held; carved gold channels at baseline dusk luminosity; left-wall banners present. | Frame 120 (5.0s): Hermes has pivoted feet, hips, and shoulders to face away along the rightward-curving road, displaced diagonally screen-right and slightly deeper on the near paving; cloak trails, caduceus is carried (partly occluded in rear view), and legs remain in active stride (different foot/body placement across frames 96, 108, 120 at 4.0s, 4.5s, 5.0s). | `hermes-sky-bridges-destination-walk/04-render-1.md`: 2fps contact sheet plus decoded frames 0, 96, 108, 120 (0.0s, 4.0s, 4.5s, 5.0s at 24fps, 121 frames total). | `holds` on body pivot, primary travel, fixed camera, and continuing ending (`state-01` → `state-02`). `cannot see` on separate initial head-survey beat (merges with body pivot in samples), rear-view micro facial/staff/footwear detail, and continuous inter-sample foot contact. |
| `shot-02` | `state-02` → `state-03` | Frame 0 (0.0s): Begins from decoded frame 120 of `shot-01` (`00-source-frame.png`); Hermes is away-facing in stride on the near paving with matching scale, architecture, gold-channel geometry, and dusk exposure. Frames 6, 12, 24 (0.25s, 0.5s, 1.0s) continue away-facing steps without resetting pose or repeating the pivot. | Frame 240 (10.0s): Hermes remains rear/away-facing further along the near paved viaduct inside the parapet (not arriving at the distant city); quarter-second crops at frames 192–240 (8.0–10.0s) show changing left-foot placement through 9.75→10.0s rather than a two-foot settled stop; caduceus and cloak persist. | `hermes-sky-bridges-stride-continuation/04-render-1.md`: 21-sample overview (frames 0..240, 0.0–10.0s), join sheet (`shot-01` frames 108, 114, 120 at 4.5, 4.75, 5.0s → `shot-02` frames 0, 6, 12 at 0.0, 0.25, 0.5s), light detail (frames 48–96, 2.0–4.0s), and 360x400 closing crop (frames 192–240, 8.0–10.0s). | `holds` on opening join, continued forward travel, fixed camera, and continuing ending (`state-02` → `state-03`). **Observed deviations vs. `state-03` baseline:** (1) `drifted` on channel-pulse confinement/one-to-one step timing — near parapet channel develops a broad yellow-white flare at 2.75–4.0s (frames 66–96) blooming onto adjoining paving/parapet and a second broad bright interval around 7.5–8.5s, rather than confined one-pulse-per-step surges; (2) `cannot see` on continuous planted-foot contact — 8.0–10.0s crops show possible boot sliding/skating. |

## Adjacent-shot reconciliation
| Outgoing shot | Incoming shot | States agree or approved transition | Actual evidence | Blocking mismatch/uncertainty or none |
|---|---|---|---|---|
| `shot-01` (`hermes-sky-bridges-destination-walk`) | `shot-02` (`hermes-sky-bridges-stride-continuation`) | Direct match-frame continuation (`state-02` at `shot-01` 5.0s → `state-02` at `shot-02` 0.0s) in locked 16:9 camera framing. | Join sheet comparing `shot-01` frames 108, 114, 120 (4.5s, 4.75s, 5.0s) with `shot-02` frames 0, 6, 12 (0.0s, 0.25s, 0.5s), plus `00-source-1.md` (`frame 120` PNG SHA-256 `9525ddf63dd8d6008392dab6ce3196a418fdb322736bbcdb8653924c8d5217fe`). Pose, character scale, parapet/viaduct landmarks, channel geometry, and exposure align across the cut, and `shot-02` continues forward without repeating the turn. | **Adjacent cut (`shot-01` → `shot-02`):** Minor cloak/leg phase difference across 5.0s → 0.0–0.25s; no camera jump, character pop, or pose reset. **Within `shot-02` (`state-02` → `state-03`):** Broad warm-gold channel flare/bloom at 2.75–4.0s and 7.5–8.5s (vs. strictly confined per-step pulses in `state-03`) and possible closing foot sliding at 8.0–10.0s. Requires human decision whether to accept the two-shot sequence with these retained deviations or require an upstream revision. |

## Handoff
- Receiving composition producer and exact selected clip set: None for this trial scope (`Composition brief path: none` in `00-intake-1.md`). If composition is later authorized in a revised intake, the exact clip set is `shot-01` (`runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4`, SHA-256 `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332`) and `shot-02` (`runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4`, SHA-256 `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed`).
- Story success, identity/continuity checks and any review limitations: Both approved story events (`evt-01-commit-to-route` and `evt-02-active-causeway-stride`) are visibly accomplished in order from a fixed camera with consistent character silhouette, wardrobe, and woodblock-illustrated viaduct environment. Review is based on decoded frame sheets (not native `video_analyze`, which was unsupported by the provider) and retains the known `shot-02` gold-channel flare/bloom (2.75–4.0s, 7.5–8.5s) and possible 8.0–10.0s foot sliding.
- Revision impact and required upstream correction, if any: Historical acceptance of `shot-01` and `shot-02` in `runs/motion/location-probes/manifest.md` remains intact. No automatic regeneration is triggered.

## Open
- Required unresolved mismatches or uninspected evidence:
  1. Operator verdict on `02-review-1.md`: accept this two-shot sequence with the disclosed `shot-02` channel flare/bloom (2.75–4.0s, 7.5–8.5s), minor 5.0s→0.0s gait-phase seam, and possible 8.0–10.0s foot sliding (`status: approved`, `verdict: accepted`), or reject/revise (`verdict: drifted`) to commission a new `shot-02` variation or revised continuity baseline.

## Acceptance evidence
Acceptance is pending until the human decides on this exact review/version.
Status/verdict are authoritative; cite a real operator decision only if already
available when this record is derived. Later approval changes metadata only,
not observed findings. An accepted clip is not automatically an accepted sequence.
