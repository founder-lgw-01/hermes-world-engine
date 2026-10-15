---
production: sky-bridges-two-shot-trial
attempt: 1
stage: 05_compose
status: approved
generated: 2026-10-15T07:17:23.179897+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-2.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-1.md
  - stories/hermetic-gates/01-foundation-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/01-spec-1.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/01-spec-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, composition specification

Copy to `runs/studio/<production>/05-spec-N.md` after accepted inputs are ready.
Derive in this order. No instructions or tool call may introduce new intent.

## Source manifest
| Exact approved brief/record/clip/review path | SHA-256 | Role | Authoritative acceptance and filing evidence |
|---|---|---|---|
| `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md` | `d0488f7c40353077e3b0e72059e95cff56ec7c62e28d67ef8d42ba274c65323f` | Approved studio intake (`attempt: 2`, selecting `05_compose`) | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/00-composition-1.md` | `658da25f8e9281d0586abae252cb5fd7b98c2c86489e3b74dd0b6361e5166289` | Approved early composition brief | `status: approved`; Jordan desktop chat: “approve” |
| `stories/hermetic-gates/01-foundation-1.md` | `35f1676db0047addd3c0dbedbf940f1b6ba2229adcfcc77e5dca1ff6e34161dd` | Approved series foundation | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-sequence-1.md` | `04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab` | Approved sequence brief | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-storyboard-1.md` | `a7ab1bebede8d5fd559179cb3fdacd002df71d5c094b19d7ffddfe62183eb476` | Approved storyboard | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-continuity-1.md` | `620ceb8ebff65d141cd529b176060b431afd21d5dcb37c9f3e2fc92a7383b077` | Approved continuity baseline | `status: approved`; Jordan desktop chat: “approve” |
| `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` | `5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a` | Approved and accepted sequence review | `status: approved`, `verdict: accepted`; Jordan desktop chat: “accept, we're testing structure not specificity.” |
| `runs/motion/location-probes/manifest.md` | `aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d` | Accepted motion manifest | Rows 1 and 2 match exact clip hashes |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/01-spec-1.md` | `bdbe137fa8e12c282db672c847f3775d4a91443597c3b6282ed572ffcce1c5e3` | `shot-01` approved motion spec | `status: approved` |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` | `1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6` | `shot-01` accepted render record | `status: approved`, `verdict: accepted`; manifest row 1 |
| `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` | `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332` | `shot-01` accepted video (`5.041667s`, 121 frames) | Verified against `04-render-1.md` and `manifest.md` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/00-source-1.md` | `e6fbcd12646e616d4ce7c94f7f705453968f82ed3935443dec67c3f2468a2d66` | `shot-02` decoded-frame source sidecar | `status: approved`, `verdict: accepted` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/01-spec-1.md` | `1f1f1b9bd65db66e24f559acc90f71ce69a6df93c1180f16518742ad2018c5e3` | `shot-02` approved motion spec | `status: approved` |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` | `9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9` | `shot-02` accepted render record | `status: approved`, `verdict: accepted`; manifest row 2 |
| `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` | `292ce8c8f7a104677b8a95283c79ba974a601f6a3beccb595ab7c0b40dfcb8ed` | `shot-02` accepted video (`10.041667s`, 241 frames) | Verified against `04-render-1.md` and `manifest.md` |

For narrative work, name the accepted sequence review and its exact baseline
and clip versions. A standalone clip explicitly records narrative review as not
applicable; it still requires its own acceptance and filing.

## Brief
- Approved composition brief version: `runs/studio/sky-bridges-two-shot-trial/00-composition-1.md` (`attempt: 1`, `status: approved`, SHA-256 `658da25f8e9281d0586abae252cb5fd7b98c2c86489e3b74dd0b6361e5166289`), linked to `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md` (`attempt: 2`, `status: approved`, SHA-256 `d0488f7c40353077e3b0e72059e95cff56ec7c62e28d67ef8d42ba274c65323f`).
- Resolved choices and constraints; no independent override of brief intent: Cut-only silent assembly joining `shot-01` (`hermes-sky-bridges-destination-walk/04-video-1.mp4`) and `shot-02` (`hermes-sky-bridges-stride-continuation/04-video-1.mp4`) end-to-end without trimming, narration, music, sound effects, or on-screen text overlays.

## Timeline
| Order | Exact clip | Source in/out | Timeline start/end | Approved transition and evidence |
|---|---|---|---|---|
| 1 | `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4` (`shot-01`) | Frame `0` to `120` (`0.000000s` to `5.041667s`, 121 frames at `24/1` fps, untrimmed) | `0.000000s` to `5.041667s` (frames `0`–`120`) | Direct match-frame cut (`state-02` at `shot-01` frame `120` → `state-02` at `shot-02` frame `0`), approved in `02-continuity-1.md` (`620ceb8ebff65d141cd529b176060b431afd21d5dcb37c9f3e2fc92a7383b077`) and accepted in `02-review-1.md` (`5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a`). |
| 2 | `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4` (`shot-02`) | Frame `0` to `240` (`0.000000s` to `10.041667s`, 241 frames at `24/1` fps, untrimmed) | `5.041667s` to `15.083334s` (frames `121`–`361`, `362` total frames) | Sequence ends in active forward stride (`state-03`) without a fade, dissolve, or trim, per `02-sequence-1.md` (`04c054f32d58e797c685f2725efb622ba228b80445debb84d0c392e5aedce3ab`) and `00-composition-1.md` (`658da25f8e9281d0586abae252cb5fd7b98c2c86489e3b74dd0b6361e5166289`). |

Calculate from actual media. No invented durations or unapproved trimming.

## Finishing layers
| Requested voice/sound/text layer | Approved source or exact text | Permission evidence if needed | Timing/placement/safe area | Acceptance check |
|---|---|---|---|---|
| Voice / narration | `none` | not applicable | not applicable | `ffprobe` confirms zero audio streams (`audio: none`) in `05-final-1.mp4`. |
| Music / sound effects | `none` | not applicable | not applicable | `ffprobe` confirms zero audio streams (`audio: none`) in `05-final-1.mp4`. |
| On-screen text / titles / captions | `none` | not applicable | not applicable | Decoded frames confirm no added titles, captions, or overlays; preserves `world/style.md` exclusion of lettering. |

## Delivery
- Actual agreed container, dimensions/aspect, frame rate, audio and other checks:
  - Canonical output path: `runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`
  - Container: MP4 (`mov,mp4,m4a,3gp,3g2,mj2`)
  - Video codec / profile / pixel format: `h264` (`High`), `yuv420p`
  - Dimensions / aspect ratio: `1280x720` (`16:9`)
  - Frame rate / timebase: `24/1` fps, `1/12288` stream timebase
  - Frame count / duration: `362` frames (`15.083334s` container duration)
  - Audio streams: `none`

## At risk and acceptance
| Criterion | Observable evidence needed | Risk/guard | Reviewer and human gate |
|---|---|---|---|
| Assembly and pacing | `ffprobe` on `05-final-1.mp4` showing `362` frames (`15.083334s`), `24/1` fps, and decoded frames around the `5.041667s` cut (`frames 119, 120, 121, 122`). | Guard against unapproved trimming, frame drops, or timestamp discontinuities by using `ffmpeg -f concat -safe 0 -c copy` on the verified identical-stream MP4 inputs. | Hermes first review; Jordan final acceptance on `05-record-1.md`. |
| Adjacent-shot continuity across the cut | Decoded boundary sheet (`frames 118–123`) from `05-final-1.mp4` confirming `shot-01` frame `120` transitions directly to `shot-02` frame `0` (`frame 121` of assembled file). | Stream-copy preserves exact source pixels across the cut without recompression artifacts. Retained sequence notes from `02-review-1.md` (minor cloak/leg phase difference at the cut, `shot-02` gold-channel flare/bloom, and possible closing foot sliding) remain disclosed. | Hermes first review; Jordan final acceptance on `05-record-1.md`. |
| Final visual identity & style exclusions | Decoded opening (`frame 0`), cut boundary (`frames 120–121`), and closing (`frame 361`) frames from `05-final-1.mp4`. | Lossless `-c copy` performs zero pixel re-encoding, guaranteeing zero alteration to character/world identity or woodblock print texture and zero added text/overlays. | Hermes first review; Jordan final acceptance on `05-record-1.md`. |
| Requested voice/sound/text (`none`) | `ffprobe` stream inventory confirming `1` video stream and `0` audio/subtitle streams. | `-c copy` on two silent MP4 files introduces no audio or subtitle streams. | Hermes first review; Jordan final acceptance on `05-record-1.md`. |

## Execution instructions
- Named separately authorized execution route and readiness evidence:
  - Proposed route: Local host `ffmpeg` concat demuxer with lossless stream-copy (`ffmpeg -v error -f concat -safe 0 -i <scratch-concat-list.txt> -c copy -movflags +faststart -n runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`).
  - Readiness evidence: `ffprobe` verified both inputs share identical stream parameters (`codec_name=h264`, `profile=High`, `width=1280`, `height=720`, `pix_fmt=yuv420p`, `r_frame_rate=24/1`, `avg_frame_rate=24/1`, `time_base=1/12288`). Because `-c copy` copies compressed H.264 packets without decoding or encoding video frames, execution completes in `<0.1s` with negligible CPU usage and zero external spending.
- Allowed work and spending scope:
  - Zero external API calls, zero credits spent, and zero public uploads.
  - Requires explicit operator approval of both `05-spec-1.md` and this `ffmpeg -f concat ... -c copy` execution route before running.
- Instructions derived only from the sections above:
  1. Verify all 15 SHA-256 hashes and `status: approved` / `verdict: accepted` gates in **Source manifest** immediately before execution.
  2. Write a temporary concat list in `/opt/data/cache/scratch/sky-bridges-concat.txt` naming the exact absolute paths of `shot-01` (`04-video-1.mp4`) and `shot-02` (`04-video-1.mp4`) in order.
  3. Run `ffmpeg -v error -f concat -safe 0 -i /opt/data/cache/scratch/sky-bridges-concat.txt -c copy -movflags +faststart -n runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`.
  4. Verify `runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4` with `ffprobe`, compute its SHA-256 hash, inspect decoded opening/cut/closing frames, and write `runs/studio/sky-bridges-two-shot-trial/05-record-1.md` (`status: draft`, `verdict:` empty) for human acceptance.
- Stop before execution if a route, input approval or required check is missing.

## Open
- Blocking issues; an approved spec is not proof of an executed render:
  1. Awaiting human approval of `runs/studio/sky-bridges-two-shot-trial/05-spec-1.md` (`status: approved`) and explicit authorization to execute the lossless `ffmpeg -f concat -safe 0 -c copy` route to produce `runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`.
