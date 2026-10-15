---
production: sky-bridges-two-shot-trial
attempt: 3
stage: 05_compose
status: approved
generated: 2026-10-15T08:17:27.944727+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-3.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-2.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-2.md
  - runs/studio/sky-bridges-two-shot-trial/05-spec-2.md
  - runs/studio/sky-bridges-two-shot-trial/05-record-2.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, composition specification (attempt 3 — stutter-free splice, 1.28x tail / 1.54x continuation pace, +1px stabilization, and distant birds)

Copy to `runs/studio/<production>/05-spec-N.md` after accepted inputs are ready.
Derive in this order. No instructions or tool call may introduce new intent.

## Source manifest
| Exact approved brief/record/clip/review path | SHA-256 | Role | Authoritative acceptance and filing evidence |
|---|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-3.md` | `09e32cc033904c0d3e72cbedd84d4d3b1c77d379f8147e392f362f37160b2f43` | Approved studio intake (`attempt: 3`) | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/00-composition-2.md` | `77172c065be59cb0c8ea2b130d7a0626ae4c8bf3679b19b99ac89ed2d3228fff` | Approved composition brief (`attempt: 2`) | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-review-2.md` | `20d1d0234e561cc961989444af25138c6b24247e37e1a0339f2170e0228c2220` | Approved sequence review (`attempt: 2`) | `status: approved`, `verdict: accepted` |
| `runs/studio/sky-bridges-two-shot-trial/05-spec-2.md` | `d2220b6b0f4af4b7516fd1d6959d6d3506fd373c7b8ca67392d2ca8893414456` | Superseded composition spec (`attempt: 2`) | `status: approved` |
| `runs/studio/sky-bridges-two-shot-trial/05-record-2.md` | `7a299fd2510e188f980c3660e924b9cef3d039e1d6c88765ce681cc609051643` | Rejected composition record (`attempt: 2`, `verdict: drifted` on 4–5s `xfade` stutter, slow `0.88*PTS` pace, and `1px` camera shift) | `status: approved`, `verdict: drifted` |
| `runs/motion/location-probes/manifest.md` | `aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d` | Accepted motion manifest | Rows 1 and 2 match exact clip hashes |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | `shot-01` accepted render record | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | `shot-01` accepted video (`5.041667s`, 121 frames) | Verified against `04-render-1.md` and `manifest.md` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md` | `e6fbcd12646e616d4ce7c94f7f705453968f82ed3935443dec67c3f2468a2d66` | `shot-02` decoded-frame source sidecar | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | `shot-02` accepted render record | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | `shot-02` accepted video (`10.041667s`, 241 frames) | Verified against `04-render-1.md` and `manifest.md` |

For narrative work, name the accepted sequence review and its exact baseline
and clip versions. A standalone clip explicitly records narrative review as not
applicable; it still requires its own acceptance and filing.

## Brief
- Approved composition brief version: `runs/studio/sky-bridges-two-shot-trial/00-composition-2.md` (`77172c065be59cb0c8ea2b130d7a0626ae4c8bf3679b19b99ac89ed2d3228fff`), refined from `05-record-2.md` drift feedback:
  1. Replace the `0.25s` `xfade` (which caused double-image ghosting/stutter on moving legs at `4.8s–5.0s`) with a clean direct concat cut, and accelerate `shot-01`'s decelerating tail (`frames 96–120`, `4.0s–5.0s`) by `1.28x` (`setpts=0.78*(PTS-STARTPTS)`).
  2. Accelerate `shot-02` by `1.54x` (`setpts=0.65*PTS,fps=24`) so its walking cadence matches `shot-01` without looking over-sped.
  3. Counter-shift `shot-02`'s `(-1px, -1px)` background camera drift via `pad=1284:724:1:1:color=black,crop=1280:720:0:0`.
  4. Retain the `lutyuv` exposure/chroma match and the 5 distant woodblock birds gliding across the upper-right sky.

## Timeline
| Order | Exact clip | Source in/out | Timeline start/end | Approved transition and evidence |
|---|---|---|---|---|
| 1a | `hermes-sky-bridges-destination-walk/04-video-1.mp4` (`shot-01` main body) | Frames `0`–`95` (`0.000000s`–`4.000000s`, `96` frames at `1.00x`) | `0.000000s`–`4.000000s` (frames `0`–`95`) | Continuous into `shot-01` tail (`1b`). |
| 1b | `hermes-sky-bridges-destination-walk/04-video-1.mp4` (`shot-01` tail) | Frames `96`–`120` (`4.000000s`–`5.041667s` source, scaled by `setpts=0.78*(PTS-STARTPTS)` to `20` frames / `0.833333s`) | `4.000000s`–`4.833333s` (frames `96`–`115`) | Direct match-frame concat cut into luma/chroma-matched, `+1px` stabilized, `1.54x`-paced `shot-02`. |
| 2 | `hermes-sky-bridges-stride-continuation/04-video-1.mp4` (`shot-02`) | Frames `0`–`240` (`0.000000s`–`10.041667s` source, scaled by `setpts=0.65*PTS,fps=24` to `157` frames / `6.541667s`) | `4.833333s`–`11.375000s` (frames `116`–`272`, `273` total frames) | Ends in active forward stride at `11.375000s` (`frame 272`). |

Calculate from actual media. No invented durations or unapproved trimming.

## Finishing layers
| Requested voice/sound/text layer | Approved source or exact text | Permission evidence if needed | Timing/placement/safe area | Acceptance check |
|---|---|---|---|---|
| Luma/chroma match + `+1px` camera stabilization (`shot-02`) | `lutyuv=y=val*0.975+4.4:u=val+1.225:v=val-1.424,pad=1284:724:1:1:color=black,crop=1280:720:0:0` | Approved in `00-composition-2.md` and operator feedback on `05-record-2.md` | Applied across `shot-02` (`4.833333s–11.375000s`) | Smooth cut without `xfade` ghosting or `1px` architectural jump. |
| Two-stage pace curve (`1.28x` on `shot-01` tail, `1.54x` on `shot-02`) | `setpts=0.78*(PTS-STARTPTS)` on `shot-01` frames `96–120`; `setpts=0.65*PTS` on `shot-02` | Operator acceptance: “good enough for our test.” | Yields `273` frames (`11.375000s` at `24/1` fps) | Natural stride cadence across the `4.83s` splice. |
| Ambient 2D woodblock distant-birds sky overlay | 5 small matte charcoal-sepia (`#2d2622`) woodblock birds gliding across upper-right sky | Approved in `00-composition-2.md` | Upper-right sky (`x=680..1200, y=60..220`) across `0.000000s–11.375000s` | Visible, style-consistent distant birds. |

## Delivery
- Actual agreed container, dimensions/aspect, frame rate, audio and other checks:
  - Canonical output path: `runs/studio/sky-bridges-two-shot-trial/05-final-3.mp4`
  - Container: MP4 (`mov,mp4,m4a,3gp,3g2,mj2`), `1280x720` (`16:9`), `h264` (`High`), `yuv420p`, `24/1` fps, `273` frames (`11.375000s`), `audio: none`.

## At risk and acceptance
| Criterion | Observable evidence needed | Risk/guard | Reviewer and human gate |
|---|---|---|---|
| Stutter-free cut & balanced gait pace | Playback and `ffprobe` (`273` frames, `11.375000s`) confirming direct concat splice with `1.28x` tail / `1.54x` continuation pace. | Remove `xfade` ghosting; use `0.78*PTS` / `0.65*PTS` instead of `0.45*PTS`. | Accepted by Jordan after preview playback (“good enough for our test”). |

## Execution instructions
- Named separately authorized execution route and readiness evidence:
  - Executed via CPU-throttled `nice -n 19 ffmpeg -threads 2` (`2.97s` elapsed) and retained at `runs/studio/sky-bridges-two-shot-trial/05-final-3.mp4` (`a50aa72e8952eb7b4a2e5d15a2f69cc3531c91dcb4976f71e76be6f0fc5edfc6`).

## Open
- Blocking issues; an approved spec is not proof of an executed render: none.
