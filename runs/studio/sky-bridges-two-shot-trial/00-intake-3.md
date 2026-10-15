---
production: sky-bridges-two-shot-trial
attempt: 3
stage: studio/00_intake
status: approved
generated: 2026-10-15T07:52:26.077194+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-2.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-1.md
  - stories/hermetic-gates/01-foundation-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-2.md
  - runs/studio/sky-bridges-two-shot-trial/05-record-1.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
---

# sky-bridges-two-shot-trial, intake and route (attempt 3 — compose-stage corrective finishing pass)

Copy to `runs/studio/<production>/00-intake-N.md`. Blank means unanswered;
`you choose` delegates a choice that Hermes surfaces before complete approval.
Use only the selected questions and outputs. This is not a status tracker.

## Outcome
- Deliverable: Storied animation
- Audience and purpose for this production: Internal operator/studio validation — test how much post-playback continuity and ambient-motion correction `05_compose` can achieve on the two existing accepted sky-bridges clips without spending credits to regenerate video.
- What should the viewer understand or feel: A calm, deliberate threshold crossing — Hermes surveys the distant city, commits to the high causeway, and strides forward under a living dusk sky with distant birds flying across the ravine, with matched exposure/color, matched walking cadence, and a smooth cut between shots.
- Accepted endpoint and observable result: An approved composition specification (`runs/studio/sky-bridges-two-shot-trial/05-spec-2.md`) and, after separately authorized low-CPU execution, an inspected final export (`runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`) and review record (`runs/studio/sky-bridges-two-shot-trial/05-record-2.md`) demonstrating luma/chroma matching, cadence alignment, soft cut transition, and a 2D woodblock distant-birds sky layer.

## Roles
- Producer: Hermes, unless explicitly reassigned.
- First reviewer: Hermes; not independent review.
- Human approver: Jordan, unless explicitly reassigned.
- Canonical-record/receiving responsibilities or explicit reassignments: Hermes drafts and reconciles canonical Markdown records under `runs/studio/sky-bridges-two-shot-trial/`; Jordan approves each stage gate and the execution route.

## Selected route
- Selected contracts in execution order, including conditional preparation: `studio/00_intake/CONTEXT.md` (`00-intake-3.md` + `00-composition-2.md`) → `studio/02_sequence/CONTEXT.md` (approve `02-review-2.md` routing the compose-fixable items to `05_compose` while deferring sandal heel-wing regeneration) → `05_compose/CONTEXT.md` (`05-spec-2.md` → `05-final-2.mp4` + `05-record-2.md`).
- Skipped work and why: `00_setup`, `01_spec`, `02_render`, `03_file`, `04_animate`, and `01_story` are skipped because this pass intentionally tests what `05_compose` can fix on the existing accepted clips without regenerating video.
- Existing handoff to resume, if any: Resume from `runs/studio/sky-bridges-two-shot-trial/02-review-2.md` into `05_compose/CONTEXT.md`.
- Composition brief path or none: `runs/studio/sky-bridges-two-shot-trial/00-composition-2.md`.
  Finishing requirements belong there, not in a duplicate list here.

## Assets and preparation
| Need | Reusable exact artifact and authoritative acceptance evidence, or missing | Preparation task/owning contract | Expected output | Receiver |
|---|---|---|---|---|
| Shot 1 accepted clip (`hermes-sky-bridges-destination-walk`) | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` (`b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332`), `04-render-1.md` (`status: approved`, `verdict: accepted`), filed in `runs/motion/location-probes/manifest.md` | none (reused unchanged) | Existing accepted 5.041667s clip | `05_compose` |
| Shot 2 accepted clip (`hermes-sky-bridges-stride-continuation`) | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` (`292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed`), `04-render-1.md` (`status: approved`, `verdict: accepted`), filed in `runs/motion/location-probes/manifest.md` | none (reused unchanged) | Existing accepted 10.041667s clip | `05_compose` |
| Sequence review routing (`02-review-2.md`) | `runs/studio/sky-bridges-two-shot-trial/02-review-2.md` (drafted with the four post-playback notes) | Approve `02-review-2.md` in this review package (`status: approved`, `verdict: accepted` for compose-stage remediation scope) | Approved `02-review-2.md` | `05_compose` |
| Revised composition brief (`00-composition-2.md`) | Drafted in this review package (`runs/studio/sky-bridges-two-shot-trial/00-composition-2.md`) | Approve `00-composition-2.md` in `studio/00_intake/CONTEXT.md` | Approved `00-composition-2.md` | `05_compose` |
| Low-CPU `ffmpeg` + 2D overlay composition route | Local `python3` (stdlib RGBA generator for woodblock bird-flock overlay) + `nice -n 19 ffmpeg -threads 2` (`lutyuv` luma/chroma match, `setpts` cadence match, `xfade` 0.25s cut smoothing, and `overlay` for distant birds) | Requires explicit operator approval at the `05-spec-2.md` gate before executing `05-final-2.mp4` | `runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4` | `05_compose` |

Accepted-but-unfiled is a filing task. Missing inputs do not authorize generation.
Distinguish supplied/verified evidence, requires preparation and planned/unverified
capabilities; no provider probing in intake.

## Handoff
| Exact input path/version | Role in this request | SHA-256 when approved and selected | Authoritative approval evidence |
|---|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md` | Prior approved intake (`attempt: 2`, preserved) | `d0488f7c40353077e3b0e72059e95cff56ec7c62e28d67ef8d42ba274c65323f` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/00-composition-1.md` | Prior approved composition brief (`attempt: 1`, preserved) | `658da25f8e9281d0586abae252cb5fd7b98c2c86489e3b74dd0b6361e5166289` | `status: approved`; Jordan desktop chat: “approve” |
| `stories/hermetic-gates/01-foundation-1.md` | Approved series foundation | `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` | Approved sequence brief | `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` | Approved storyboard | `a7ab1bebede8d5fd559179cb3fdacd002df71d5c094b19d7ffddfe62183eb476` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` | Approved continuity baseline | `620ceb8ebff65d141cd529b176060b431afd21d5dcb37c9f3e2fc92a7383b077` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` | Prior accepted sequence review (`attempt: 1`, preserved) | `5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a` | `status: approved`, `verdict: accepted` |
| `runs/studio/sky-bridges-two-shot-trial/05-record-1.md` | Prior accepted export record (`attempt: 1`, preserved) | `cc4c90327c60f009f9e356842ee71250b3a2c2ac52d86ad62ff2b11141fe092f` | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/manifest.md` | Accepted motion manifest | `aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d` | Retained manifest rows for both sky-bridges shots |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` | Shot 1 authoritative render record | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | Shot 1 accepted video | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | Verified against `04-render-1.md` and `manifest.md` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` | Shot 2 authoritative render record | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | Shot 2 accepted video | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | Verified against `04-render-1.md` and `manifest.md` |

- Receiving producer and expected output: Hermes (`05_compose/CONTEXT.md` → `runs/studio/sky-bridges-two-shot-trial/05-spec-2.md`).
- Checks completed / remaining uncertainty: Measured exact YUV signalstats across `shot-01` and `shot-02` (`shot-01` frame 120: `YAVG=105.57, UAVG=109.37, VAVG=143.51, SATAVG=24.03`; `shot-02` frame 0: `YAVG=103.74, UAVG=108.14, VAVG=144.93, SATAVG=25.80`) and verified that `lutyuv=y=val*0.975+4.4:u=val+1.225:v=val-1.424` aligns `shot-02` frame 0 to `YAVG=105.08, UAVG=109.14, VAVG=142.93, SATAVG=23.94`. Sandal heel-wing asymmetry (`2 on 1 foot, 1 small on the other`) is baked into source pixels and remains deferred to upstream `04_animate` regeneration.
- Prerequisites required before the next specification: Package approval of `00-intake-3.md`, `00-composition-2.md`, and `02-review-2.md`.
- Revision impact, superseded intake if any, and why reuse remains valid: Supersedes `00-intake-2.md` and `00-composition-1.md` while preserving `05-spec-1.md`, `05-final-1.mp4`, and `05-record-1.md` untouched for side-by-side comparison.

## Acceptance criteria
| Selected deliverable/check | Observable evidence required | Human decision needed |
|---|---|---|
| Corrective composition specification (`05-spec-2.md`) | Complete frozen source manifest, exact filter/timeline math for luma/chroma matching, cadence adjustment, `0.25s` cross-dissolve, and distant-birds 2D woodblock overlay | Jordan approves `05-spec-2.md` and the CPU-throttled `nice -n 19 ffmpeg -threads 2` execution route |
| Corrective final export and review (`05-final-2.mp4`, `05-record-2.md`) | `ffprobe` + `signalstats` luma/chroma verification across the cut plus decoded contact-sheet inspection showing the distant birds and smooth transition | Jordan reviews `05-final-2.mp4` against `05-final-1.mp4` and decides on `05-record-2.md` |

## Approval scope
- Named artifact versions in this review package:
  - `runs/studio/sky-bridges-two-shot-trial/00-intake-3.md` (`attempt: 3`)
  - `runs/studio/sky-bridges-two-shot-trial/00-composition-2.md` (`attempt: 2`)
  - `runs/studio/sky-bridges-two-shot-trial/02-review-2.md` (`attempt: 2`)
- Actions this approval permits: Marking `00-intake-3.md`, `00-composition-2.md`, and `02-review-2.md` (`verdict: accepted` for compose-stage remediation routing) `status: approved`, then deriving `runs/studio/sky-bridges-two-shot-trial/05-spec-2.md`.
- Separate approvals still required (spec/production, results, final acceptance): Approval of `05-spec-2.md` and its CPU-throttled local `ffmpeg` execution route before generating `05-final-2.mp4`; then human acceptance of `05-record-2.md`.
- Spending or publication: none unless separately and explicitly authorized.

## Open
- Unanswered scope questions and blocking decisions: none. Ready for package approval of `00-intake-3.md`, `00-composition-2.md`, and `02-review-2.md`.
