---
production: sky-bridges-two-shot-trial
attempt: 2
stage: studio/00_intake
status: approved
generated: 2026-10-15T07:13:42.829649+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-1.md
  - stories/hermetic-gates/01-foundation-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
---

# sky-bridges-two-shot-trial, intake and route (attempt 2, adding composition)

Copy to `runs/studio/<production>/00-intake-N.md`. Blank means unanswered;
`you choose` delegates a choice that Hermes surfaces before complete approval.
Use only the selected questions and outputs. This is not a status tracker.

## Outcome
- Deliverable: Storied animation
- Audience and purpose for this production: Internal operator/studio validation — extend the accepted two-shot sequence trial (`02-review-1.md`) to test `05_compose/CONTEXT.md` specification and lossless assembly of the two accepted sky-bridges clips.
- What should the viewer understand or feel: A calm, deliberate threshold crossing — Hermes surveys the distant city, commits to the high causeway, and the bridge's warm-gold channels awaken in response to his stride across one continuous 15-second assembled sequence.
- Accepted endpoint and observable result: An approved composition specification (`runs/studio/sky-bridges-two-shot-trial/05-spec-1.md`) and, if the operator separately authorizes an execution route (e.g., lossless `ffmpeg -f concat` stream-copy), an inspected and accepted final export (`runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`) and record (`runs/studio/sky-bridges-two-shot-trial/05-record-1.md`).

## Roles
- Producer: Hermes, unless explicitly reassigned.
- First reviewer: Hermes; not independent review.
- Human approver: Jordan, unless explicitly reassigned.
- Canonical-record/receiving responsibilities or explicit reassignments: Hermes drafts and reconciles canonical Markdown records under `runs/studio/sky-bridges-two-shot-trial/`; Jordan approves each stage gate and any execution route.

## Selected route
- Selected contracts in execution order, including conditional preparation: `studio/00_intake/CONTEXT.md` (`00-intake-2.md` + `00-composition-1.md`) → reuse unchanged approved `stories/hermetic-gates/01-foundation-1.md`, `02-sequence-1.md`, `02-storyboard-1.md`, `02-continuity-1.md`, and accepted `02-review-1.md` → `05_compose/CONTEXT.md` (`05-spec-1.md`, then `05-final-1.mp4` + `05-record-1.md` only if an execution route is separately authorized).
- Skipped work and why: `00_setup`, `01_spec`, `02_render`, `03_file`, `04_animate`, `01_story`, and `02_sequence` regeneration are skipped because the foundation, sequence planning baseline, two motion clips, and `02-review-1.md` are already approved/accepted and unchanged.
- Existing handoff to resume, if any: Resume from accepted `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` (`status: approved`, `verdict: accepted`, SHA-256 `5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a`) into `05_compose/CONTEXT.md`.
- Composition brief path or none: `runs/studio/sky-bridges-two-shot-trial/00-composition-1.md`.
  Finishing requirements belong there, not in a duplicate list here.

## Assets and preparation
| Need | Reusable exact artifact and authoritative acceptance evidence, or missing | Preparation task/owning contract | Expected output | Receiver |
|---|---|---|---|---|
| Shot 1 accepted clip (`hermes-sky-bridges-destination-walk`) | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` (`b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332`), `04-render-1.md` (`status: approved`, `verdict: accepted`), filed in `runs/motion/location-probes/manifest.md` | none (reused unchanged) | Existing accepted 5.041667s clip | `05_compose` |
| Shot 2 accepted clip (`hermes-sky-bridges-stride-continuation`) | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` (`292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed`), `04-render-1.md` (`status: approved`, `verdict: accepted`), filed in `runs/motion/location-probes/manifest.md` | none (reused unchanged) | Existing accepted 10.041667s clip | `05_compose` |
| Accepted sequence review (`02-review-1.md`) | `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` (`5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a`, `status: approved`, `verdict: accepted`) | none (reused unchanged) | Accepted sequence reconciliation | `05_compose` |
| Early composition brief (`00-composition-1.md`) | Drafted in this review package (`runs/studio/sky-bridges-two-shot-trial/00-composition-1.md`) | Complete and approve `00-composition-1.md` in `studio/00_intake/CONTEXT.md` | `runs/studio/sky-bridges-two-shot-trial/00-composition-1.md` (`status: approved`) | `05_compose` |
| Composition execution route | Planned/unverified in default extension (`05_compose/CONTEXT.md` has no pre-wired adapter); local `ffmpeg` concat demuxer (`-f concat -safe 0 -c copy`) is verified available on host with matching H.264 1280x720 24fps streams | Requires explicit operator authorization at the `05-spec-1.md` gate before executing `05-final-1.mp4` | Separately authorized execution route for `05-spec-1.md` | `05_compose` |

Accepted-but-unfiled is a filing task. Missing inputs do not authorize generation.
Distinguish supplied/verified evidence, requires preparation and planned/unverified
capabilities; no provider probing in intake.

## Handoff
| Exact input path/version | Role in this request | SHA-256 when approved and selected | Authoritative approval evidence |
|---|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` | Prior approved intake (`attempt: 1`, preserved) | `1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f` | `status: approved`; Jordan desktop chat: “approve” |
| `stories/hermetic-gates/01-foundation-1.md` | Approved series foundation | `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` | Approved sequence brief | `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` | Approved storyboard | `a7ab1bebede8d5fd559179cb3fdacd002df71d5c094b19d7ffddfe62183eb476` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` | Approved continuity baseline | `620ceb8ebff65d141cd529b176060b431afd21d5dcb37c9f3e2fc92a7383b077` | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` | Approved and accepted sequence review | `5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a` | `status: approved`, `verdict: accepted`; Jordan desktop chat: “accept, we're testing structure not specificity.” |
| `runs/motion/location-probes/manifest.md` | Accepted motion manifest | `aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d` | Retained manifest rows for both sky-bridges shots |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` | Shot 1 authoritative render record | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | Shot 1 accepted video | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | Verified against `04-render-1.md` and `manifest.md` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` | Shot 2 authoritative render record | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | Shot 2 accepted video | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | Verified against `04-render-1.md` and `manifest.md` |

- Receiving producer and expected output: Hermes (`05_compose/CONTEXT.md` → `runs/studio/sky-bridges-two-shot-trial/05-spec-1.md`).
- Checks completed / remaining uncertainty: All upstream story, sequence, storyboard, continuity, sequence-review, and clip hashes/statuses verified. Sibling `00-composition-1.md` is linked by exact path without reciprocal hashing.
- Prerequisites required before the next specification: Operator answers to the open finishing choices in `00-composition-1.md` and explicit package approval of `00-intake-2.md` + `00-composition-1.md`.
- Revision impact, superseded intake if any, and why reuse remains valid: Supersedes `00-intake-1.md` (`1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f`) only by adding `00-composition-1.md` and `05_compose` to the selected route. Because audience, purpose, story events, shot order, continuity states, and clip selections are unchanged, `01-foundation-1.md`, `02-sequence-1.md`, `02-storyboard-1.md`, `02-continuity-1.md`, and `02-review-1.md` remain valid and are reused unchanged per `_reference/studio-rules.md` (`Revision impact`).

## Acceptance criteria
| Selected deliverable/check | Observable evidence required | Human decision needed |
|---|---|---|
| Composition specification (`05-spec-1.md`) | Complete frozen source manifest (including post-approval hashes of `00-intake-2.md`, `00-composition-1.md`, and `02-review-1.md`), exact measured timeline (`0.000000s`–`15.083334s`), selected finishing layers, delivery criteria, and execution instructions | Jordan approves `05-spec-1.md` and any authorized execution route |
| Final assembled export and review (`05-final-1.mp4`, `05-record-1.md`) | Only after separately authorized execution: measured `ffprobe` container/stream properties, SHA-256 hash, and visual/continuity inspection across the assembled 15.083334s MP4 | Jordan accepts (`status: approved`, `verdict: accepted`) or rejects `05-record-1.md` |

## Approval scope
- Named artifact versions in this review package: `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md` (`attempt: 2`) and `runs/studio/sky-bridges-two-shot-trial/00-composition-1.md` (`attempt: 1`).
- Actions this approval permits: Marking `00-intake-2.md` and `00-composition-1.md` `status: approved` and deriving `runs/studio/sky-bridges-two-shot-trial/05-spec-1.md` (`status: draft`).
- Separate approvals still required (spec/production, results, final acceptance): Approval of `05-spec-1.md` and explicit authorization of the execution route before running `ffmpeg` to write `05-final-1.mp4`; then final human acceptance of `05-record-1.md`.
- Spending or publication: none unless separately and explicitly authorized.

## Open
- Unanswered scope questions and blocking decisions: none. All finishing choices in `00-composition-1.md` resolved via operator selection (`approve reccomended`). Ready for package approval of `00-intake-2.md` and `00-composition-1.md`.
