---
production: sky-bridges-two-shot-trial
attempt: 1
stage: studio/00_intake
status: approved
generated: 2026-10-15T06:49:08.690371+00:00
sources:
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
---

# sky-bridges-two-shot-trial, intake and route

Copy to `runs/studio/<production>/00-intake-N.md`. Blank means unanswered;
`you choose` delegates a choice that Hermes surfaces before complete approval.
Use only the selected questions and outputs. This is not a status tracker.

## Outcome
- Deliverable: Storied animation
- Audience and purpose for this production: Internal operator/studio validation — prove multi-shot story planning and adjacent-clip continuity reconciliation on the two accepted sky-bridges clips before spending credits on new shots.
- What should the viewer understand or feel: A calm, deliberate threshold crossing — Hermes surveys the distant city, commits to the high causeway, and the bridge's warm-gold channels awaken in response to his stride.
- Accepted endpoint and observable result: For this trial scope, an accepted and approved sequence continuity review (`runs/studio/sky-bridges-two-shot-trial/02-review-1.md`) reconciling the two existing accepted sky-bridges clips (`hermes-sky-bridges-destination-walk` and `hermes-sky-bridges-stride-continuation`) against an approved series foundation (`stories/hermetic-gates/01-foundation-1.md`) and sequence baseline (`02-sequence-1.md`, `02-storyboard-1.md`, `02-continuity-1.md`); composition is deferred (`none`) for this trial and `05_compose` remains unexecuted without a separately authorized composition brief and adapter.

## Roles
- Producer: Hermes, unless explicitly reassigned.
- First reviewer: Hermes; not independent review.
- Human approver: Jordan, unless explicitly reassigned.
- Canonical-record/receiving responsibilities or explicit reassignments: Hermes drafts and reconciles canonical Markdown records under `stories/hermetic-gates/` and `runs/studio/sky-bridges-two-shot-trial/`; Jordan approves each stage gate.

## Selected route
- Selected contracts in execution order, including conditional preparation: `studio/00_intake/CONTEXT.md` → `studio/01_story/CONTEXT.md` → `studio/02_sequence/CONTEXT.md` (planning pass, reusing existing accepted clips without new image or video generation) → `studio/02_sequence/CONTEXT.md` (review pass on the two accepted clips).
- Skipped work and why: `00_setup`, `01_spec`, `02_render`, `03_file`, and `04_animate` new-shot production are skipped because both sky-bridges clips and their upstream records are already approved, accepted, and filed in `runs/motion/location-probes/manifest.md`. `05_compose/CONTEXT.md` and `00-composition-1.md` are skipped for this trial by operator selection (`approve reccomended` on stopping at `02-review-1.md` with `Composition brief path: none`).
- Existing handoff to resume, if any: none (new studio production record consuming existing accepted motion outputs).
- Composition brief path or none: none.

## Assets and preparation
| Need | Reusable exact artifact and authoritative acceptance evidence, or missing | Preparation task/owning contract | Expected output | Receiver |
|---|---|---|---|---|
| Shot 1 accepted clip (`hermes-sky-bridges-destination-walk`) | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` (`b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332`), `04-render-1.md` (`status: approved`, `verdict: accepted`), filed in `runs/motion/location-probes/manifest.md` | none (already accepted and filed; reuse unchanged) | Existing accepted 5s clip | `studio/02_sequence` |
| Shot 2 accepted clip (`hermes-sky-bridges-stride-continuation`) | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` (`292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed`), `04-render-1.md` (`status: approved`, `verdict: accepted`), filed in `runs/motion/location-probes/manifest.md` | none (already accepted and filed; reuse unchanged) | Existing accepted 10s continuation clip | `studio/02_sequence` |
| Series narrative foundation | missing (`stories/` has no approved foundation yet) | Create and approve `stories/hermetic-gates/01-foundation-1.md` via `studio/01_story/CONTEXT.md` | `stories/hermetic-gates/01-foundation-1.md` (`status: approved`) | `studio/02_sequence` |
| Sequence planning baseline (events, storyboard, continuity) | missing (`runs/studio/sky-bridges-two-shot-trial/` has no sequence baseline yet) | Create and approve `02-sequence-1.md`, `02-storyboard-1.md`, and `02-continuity-1.md` via `studio/02_sequence/CONTEXT.md` | Approved sequence/storyboard/continuity package | `studio/02_sequence` (review pass) |
| Composition brief and execution adapter | Deferred for this trial (`Composition brief path: none`); `05_compose/CONTEXT.md` also states no composition adapter is implemented by this extension | None in this trial scope; requires a revised intake + `00-composition-N.md` and separately authorized adapter if finishing is later requested | none | none |

Accepted-but-unfiled is a filing task. Missing inputs do not authorize generation.
Distinguish supplied/verified evidence, requires preparation and planned/unverified
capabilities; no provider probing in intake.

## Handoff
| Exact input path/version | Role in this request | SHA-256 when approved and selected | Authoritative approval evidence |
|---|---|---|---|
| `runs/motion/location-probes/manifest.md` | Accepted motion manifest | `aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d` | Retained manifest rows for both sky-bridges shots |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` | Shot 1 authoritative render record | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | Frontmatter `status: approved`, `verdict: accepted`; manifest row 1 (`session 20261003_203006_dd142b`) |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | Shot 1 accepted video | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | Verified against `04-render-1.md` and `manifest.md` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` | Shot 2 authoritative render record | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | Frontmatter `status: approved`, `verdict: accepted`; manifest row 2 (Jordan desktop reply: “accept”) |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | Shot 2 accepted video | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | Verified against `04-render-1.md` and `manifest.md` |

- Receiving producer and expected output: Hermes (`studio/01_story` → `stories/hermetic-gates/01-foundation-1.md`, then `studio/02_sequence`).
- Checks completed / remaining uncertainty: Verified `status: approved`, `verdict: accepted`, and exact SHA-256 hashes on both motion render records, both MP4 files, and `runs/motion/location-probes/manifest.md`. Shot 2's render record retains known drift notes (longer gold flares/bloom at 2.75–4.0s and 7.5–8.5s, and possible closing foot sliding) to be evaluated in `02-review-1.md`.
- Prerequisites required before the next specification: Explicit approval of this completed `00-intake-1.md` review package; then approval of `stories/hermetic-gates/01-foundation-1.md` before `02_sequence`.
- Revision impact, superseded intake if any, and why reuse remains valid: First intake (`attempt: 1`); no superseded intake. Existing clips are reused unchanged without re-rendering.

## Acceptance criteria
| Selected deliverable/check | Observable evidence required | Human decision needed |
|---|---|---|
| Series narrative foundation (`stories/hermetic-gates/01-foundation-1.md`) | Reusable series rules, genre/exclusions, and recurring conflict aligned with approved world records without duplicating or mutating `world/` | Jordan approves `stories/hermetic-gates/01-foundation-1.md` |
| Sequence planning baseline (`02-sequence-1.md`, `02-storyboard-1.md`, `02-continuity-1.md`) | Named events, two-shot order, coverage check, and canonical start/end continuity states for Shot 1 and Shot 2 | Jordan approves `02-sequence-1.md` and the `02-storyboard-1.md` + `02-continuity-1.md` package |
| Adjacent two-shot continuity reconciliation (`02-review-1.md`) | Observed start/end states and timestamps across Shot 1 (`04-video-1.mp4`, 5s) → Shot 2 (`04-video-1.mp4`, 10s), explicitly addressing the Shot 1→2 pose/exposure join, Shot 2 gold-channel bloom, and foot-contact continuity against the approved continuity baseline | Jordan approves and accepts (`status: approved`, `verdict: accepted`) or requests changes on `02-review-1.md` |

## Approval scope
- Named artifact versions in this review package: `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` (`attempt: 1`).
- Actions this approval permits: Marking `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` `status: approved` and handing off to `studio/01_story/CONTEXT.md` to draft `stories/hermetic-gates/01-foundation-1.md`.
- Separate approvals still required (spec/production, results, final acceptance): Series foundation (`stories/hermetic-gates/01-foundation-1.md`), sequence brief (`02-sequence-1.md`), storyboard/continuity baseline (`02-storyboard-1.md`, `02-continuity-1.md`), and actual sequence review (`02-review-1.md`).
- Spending or publication: none unless separately and explicitly authorized.

## Open
- Unanswered scope questions and blocking decisions: none. All intake scope questions resolved via operator selection (`approve reccomended`). Ready for package approval of `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md`.
