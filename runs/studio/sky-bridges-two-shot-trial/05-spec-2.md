---
production: sky-bridges-two-shot-trial
attempt: 2
stage: 05_compose
status: approved
generated: 2026-10-15T07:55:16.309088+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-3.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-2.md
  - stories/hermetic-gates/01-foundation-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-2.md
  - runs/studio/sky-bridges-two-shot-trial/05-spec-1.md
  - runs/studio/sky-bridges-two-shot-trial/05-record-1.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/01-spec-1.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/01-spec-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, composition specification (attempt 2 — corrective post-processing & distant birds)

Copy to `runs/studio/<production>/05-spec-N.md` after accepted inputs are ready.
Derive in this order. No instructions or tool call may introduce new intent.

## Source manifest
| Exact approved brief/record/clip/review path | SHA-256 | Role | Authoritative acceptance and filing evidence |
|---|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-3.md` | `09e32cc033904c0d3e72cbedd84d4d3b1c77d379f8147e392f362f37160b2f43` | Approved studio intake (`attempt: 3`) | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/00-composition-2.md` | `77172c065be59cb0c8ea2b130d7a0626ae4c8bf3679b19b99ac89ed2d3228fff` | Approved corrective composition brief (`attempt: 2`) | `status: approved`; Jordan desktop chat: “approve” |
| `stories/hermetic-gates/01-foundation-1.md` | `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd` | Approved series foundation | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` | `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab` | Approved sequence brief | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` | `a7ab1bebede8d5fd559179cb3fdacd002df71d5c094b19d7ffddfe62183eb476` | Approved storyboard | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` | `620ceb8ebff65d141cd529b176060b431afd21d5dcb37c9f3e2fc92a7383b077` | Approved continuity baseline | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` | `5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a` | Prior accepted sequence review (`attempt: 1`, preserved) | `status: approved`, `verdict: accepted` |
| `runs/studio/sky-bridges-two-shot-trial/02-review-2.md` | `20d1d0234e561cc961989444af25138c6b24247e37e1a0339f2170e0228c2220` | Approved post-playback sequence review (`attempt: 2`) | `status: approved`, `verdict: accepted`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/05-spec-1.md` | `f4f085fbc0719462aeffd73a8b270b055a0a8193447b6e07dcb0d9d40f64df67` | Prior approved composition spec (`attempt: 1`, preserved) | `status: approved` |
| `runs/studio/sky-bridges-two-shot-trial/05-record-1.md` | `cc4c90327c60f009f9e356842ee71250b3a2c2ac52d86ad62ff2b11141fe092f` | Prior accepted export record (`attempt: 1`, preserved) | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/manifest.md` | `aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d` | Accepted motion manifest | Rows 1 and 2 match exact clip hashes |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/01-spec-1.md` | `bdbe137fa8e12c282db672c847f3775d4a91443597c3b6282ed572ffcce1c5e3` | `shot-01` approved motion spec | `status: approved` |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | `shot-01` accepted render record | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | `shot-01` accepted video (`5.041667s`, 121 frames) | Verified against `04-render-1.md` and `manifest.md` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md` | `e6fbcd12646e616d4ce7c94f7f705453968f82ed3935443dec67c3f2468a2d66` | `shot-02` decoded-frame source sidecar | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/01-spec-1.md` | `1f1f1b9bd65db66e24f559acc90f71ce69a6df93c1180f16518742ad2018c5e3` | `shot-02` approved motion spec | `status: approved` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | `shot-02` accepted render record | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | `shot-02` accepted video (`10.041667s`, 241 frames) | Verified against `04-render-1.md` and `manifest.md` |

For narrative work, name the accepted sequence review and its exact baseline
and clip versions. A standalone clip explicitly records narrative review as not
applicable; it still requires its own acceptance and filing.

## Brief
- Approved composition brief version: `runs/studio/sky-bridges-two-shot-trial/00-composition-2.md` (`attempt: 2`, `status: approved`, SHA-256 `77172c065be59cb0c8ea2b130d7a0626ae4c8bf3679b19b99ac89ed2d3228fff`), linked to `runs/studio/sky-bridges-two-shot-trial/00-intake-3.md` (`attempt: 3`, `status: approved`, SHA-256 `09e32cc033904c0d3e72cbedd84d4d3b1c77d379f8147e392f362f37160b2f43`).
- Resolved choices and constraints; no independent override of brief intent:
  1. Match `shot-02` luma/chroma to `shot-01`'s outgoing frame (`lutyuv=y=val*0.975+4.4:u=val+1.225:v=val-1.424`) and blend the splice with a `0.25s` (`6`-frame) cross-dissolve (`xfade=transition=fade:duration=0.25:offset=4.791667`).
  2. Accelerate `shot-02` by `12%` (`setpts=0.88*PTS,fps=24`, changing its duration from `10.041667s` / `241` frames to `8.833333s` / `212` frames) so its walking cadence aligns with `shot-01`'s outgoing stride.
  3. Composite a 2D woodblock-ink flock of 5 small birds gliding and gently flapping across the upper-right sky (`x=700..1180, y=70..210`, dark charcoal/sepia silhouette matching `world/style.md`).
  4. Keep `05-final-1.mp4` untouched and write the corrective export to `runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`.

## Timeline
| Order | Exact clip | Source in/out | Timeline start/end | Approved transition and evidence |
|---|---|---|---|---|
| 1 | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` (`shot-01`) | Frame `0` to `120` (`0.000000s` to `5.041667s`, `121` frames at `24/1` fps, `1.00x` speed) | `0.000000s` to `5.041667s` (overlaps `shot-02` during `4.791667s–5.041667s`) | `0.25s` (`6`-frame) `xfade=transition=fade:duration=0.25:offset=4.791667` into luma/chroma-matched and cadence-adjusted `shot-02`, approved in `00-composition-2.md` (`77172c065be59cb0c8ea2b130d7a0626ae4c8bf3679b19b99ac89ed2d3228fff`) and `02-review-2.md` (`20d1d0234e561cc961989444af25138c6b24247e37e1a0339f2170e0228c2220`). |
| 2 | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` (`shot-02`) | Frame `0` to `240` (`0.000000s` to `10.041667s` source, scaled by `setpts=0.88*PTS,fps=24` to `8.833333s` / `212` frames) | `4.791667s` to `13.625000s` (`327` total frames at `24/1` fps) | Continues in active forward stride through `13.625000s` (`frame 326`) with the 2D woodblock distant-birds sky layer active across `0.000000s–13.625000s`. |

Calculate from actual media. No invented durations or unapproved trimming.

## Finishing layers
| Requested voice/sound/text layer | Approved source or exact text | Permission evidence if needed | Timing/placement/safe area | Acceptance check |
|---|---|---|---|---|
| Luma/chroma exposure match + soft splice (`shot-02`) | `lutyuv=y=val*0.975+4.4:u=val+1.225:v=val-1.424` on `shot-02` + `xfade=transition=fade:duration=0.25:offset=4.791667` | Approved in `00-composition-2.md` and `02-review-2.md` | Applied across `shot-02` (`4.791667s–13.625000s`) | `ffprobe` `signalstats` across frames `114–124` (`4.75s–5.17s`) confirms smooth luma/chroma transition without the `1.83`-unit YAVG drop seen in `05-final-1.mp4`. |
| Cadence / pace alignment (`shot-02`) | `setpts=0.88*PTS,fps=24` (`1.136x` speed on `shot-02`) | Approved in `00-composition-2.md` and `02-review-2.md` | Applied across `shot-02` (`4.791667s–13.625000s`), yielding `327` total frames (`13.625s`) | `ffprobe` confirms `327` frames (`13.625s` at `24/1` fps) and faster step cadence in `shot-02`. |
| Ambient 2D woodblock distant-birds sky overlay | Procedurally generated RGBA overlay (`5` small matte charcoal-sepia woodblock V-silhouette birds gliding and gently flapping across the upper-right sky toward the distant city) | Approved in `00-composition-2.md` and `02-review-2.md` | Upper-right sky/ravine (`x=700..1180, y=70..210`) across `0.000000s–13.625000s`, staying clear of Hermes and left-side columns | Decoded frames and playback confirm visible, style-consistent distant birds gliding across the upper-right sky. |
| Voice / sound / on-screen text | `none` | not applicable | not applicable | `ffprobe` confirms zero audio/subtitle streams and zero text overlays. |

## Delivery
- Actual agreed container, dimensions/aspect, frame rate, audio and other checks:
  - Canonical output path: `runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`
  - Container: MP4 (`mov,mp4,m4a,3gp,3g2,mj2`)
  - Video codec / profile / pixel format: `h264` (`High`, `libx264 -crf 18 -preset veryfast`), `yuv420p`
  - Dimensions / aspect ratio: `1280x720` (`16:9`)
  - Frame rate: `24/1` fps
  - Frame count / duration: `327` frames (`13.625000s`)
  - Audio streams: `none`

## At risk and acceptance
| Criterion | Observable evidence needed | Risk/guard | Reviewer and human gate |
|---|---|---|---|
| Lighting & color continuity across the cut | `ffprobe` `signalstats` on `05-final-2.mp4` frames `114–124` (`4.75s–5.17s`) compared against `05-final-1.mp4`. | Guard against visible brightness/warmth step with `lutyuv` calibration (`YAVG ~105.1, UAVG ~109.1, VAVG ~142.9`) plus `0.25s` `xfade`. | Hermes first review; Jordan final acceptance on `05-record-2.md`. |
| Gait pace alignment | Measured duration (`13.625s`, `327` frames) and playback review of `shot-02` step cadence. | `setpts=0.88*PTS,fps=24` accelerates `shot-02` by `12%` without altering `shot-01`. | Hermes first review; Jordan final acceptance on `05-record-2.md`. |
| Distant birds woodblock consistency | Decoded contact sheet and crop of the upper-right sky showing the 5 birds gliding/flapping in matte charcoal-sepia ink tone (`#2d2622` / `rgba(45,38,34,0.82)`). | Keep bird scale small (`8–14px` wingspan) and matte charcoal-sepia so they read as part of the distant ukiyo-e sky, never crossing Hermes or the foreground columns. | Hermes first review; Jordan final acceptance on `05-record-2.md`. |
| Host CPU protection | Wall-clock time and thread cap (`nice -n 19`, `-threads 2`). | Restrict `ffmpeg` to `nice -n 19` and `-threads 2` so encoding `327` frames at `720p` completes in `~2–3s` without spiking the host CPU. | Hermes verifies runtime receipt in `05-record-2.md`. |

## Execution instructions
- Named separately authorized execution route and readiness evidence:
  - Proposed route: Local `python3` stdlib generator writing a `520x160` 24fps RGBA rawvideo bird-flock stream (`/opt/data/cache/scratch/birds-overlay.mov` or piped rawvideo) followed by `nice -n 19 ffmpeg -threads 2` applying `lutyuv`, `setpts=0.88*PTS,fps=24`, `xfade=transition=fade:duration=0.25:offset=4.791667`, and `overlay=x=680:y=60` to write `runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`.
  - Readiness evidence: `python3` and `ffmpeg` (`libx264`, `lutyuv`, `setpts`, `xfade`, `overlay`) are verified present on host; `lutyuv` parameters were pre-tested with `ffprobe` `signalstats` on `shot-02` frame `0`.
- Allowed work and spending scope:
  - Zero external API calls, zero credits spent, zero public uploads, CPU-throttled (`nice -n 19`, `-threads 2`).
- Instructions derived only from the sections above:
  1. Verify all 18 SHA-256 hashes in **Source manifest** before execution.
  2. Generate the `327`-frame (`13.625s`, `24fps`) RGBA distant-bird flock animation in `/opt/data/cache/scratch/` using `python3` stdlib (`zlib`/`struct` or raw RGBA to `ffmpeg`).
  3. Run `nice -n 19 ffmpeg -threads 2` with the exact filtergraph above to write `runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`.
  4. Verify `05-final-2.mp4` with `ffprobe` and `signalstats`, inspect decoded frames with `vision_analyze`, display `05-final-2.mp4` inline in chat, and write `runs/studio/sky-bridges-two-shot-trial/05-record-2.md` (`status: draft`, `verdict:` empty).
- Stop before execution if a route, input approval or required check is missing.

## Open
- Blocking issues; an approved spec is not proof of an executed render:
  1. Awaiting human approval of `runs/studio/sky-bridges-two-shot-trial/05-spec-2.md` (`status: approved`) and explicit authorization to run the CPU-throttled `nice -n 19 ffmpeg -threads 2` execution route to generate `runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`.
