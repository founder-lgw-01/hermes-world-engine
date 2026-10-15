---
production: sky-bridges-two-shot-trial
attempt: 1
stage: 05_compose
status: approved
verdict: accepted
generated: 2026-10-15T07:19:45.210349+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-2.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/studio/sky-bridges-two-shot-trial/05-spec-1.md
  - runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, final export review and local filing

Copy to `runs/studio/<production>/05-record-N.md` only after actual authorized
execution. The canonical export is `runs/studio/<production>/05-final-1.mp4`.
Never create an empty or invented file to complete this record.

## Actual export
- Final file path: `runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`
- Final file SHA-256: `2581a6eb24e227aeb81d6642e4c29d8ad7791e583efaa106cd9b20977374e9d7`
- Actual media properties and evidence:
  - File size: `3,029,621` bytes
  - Container (`ffprobe`): `mov,mp4,m4a,3gp,3g2,mj2`, duration `15.083333` seconds
  - Video stream (`index=0`): `h264` (`High`), `yuv420p`, `1280x720` (`16:9`), `r_frame_rate=24/1`, `avg_frame_rate=24/1`, `nb_frames=362`, stream duration `15.083333` seconds
  - Audio / subtitle streams: none (`1` stream total, `codec_type=video`)
- Exact approved composition spec version and SHA-256: `runs/studio/sky-bridges-two-shot-trial/05-spec-1.md` (`attempt: 1`, `status: approved`, SHA-256 `f4f085fbc0719462aeffd73a8b270b055a0a8193447b6e07dcb0d9d40f64df67`)
- Actual execution route/receipt, with unavailable metadata explicitly unknown:
  - Operator authorization: Jordan desktop chat reply **“approve”** after review of `05-spec-1.md` and the proposed lossless `ffmpeg -f concat` execution route.
  - Pre-execution verification: All 15 SHA-256 hashes in `05-spec-1.md`'s **Source manifest** matched on disk prior to execution.
  - Command executed: `ffmpeg -v error -f concat -safe 0 -i /opt/data/cache/scratch/sky-bridges-concat.txt -c copy -movflags +faststart -n runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`
  - Wall-clock execution time: `0.2893` seconds (lossless H.264 stream-copy, zero video decoding/re-encoding, $0 cost).
  - External job ID / cloud receipt: not applicable (local stream-copy execution).

## Findings
| Brief/spec criterion | Actual observation and timestamp/evidence | Result | Limitations or unresolved issue |
|---|---|---|---|
| Delivery format, dimensions, frame rate, and duration | `ffprobe` on `05-final-1.mp4` reports `h264` (`High`), `yuv420p`, `1280x720` (`16:9`), `24/1` fps, `362` frames (`121` + `241`), `15.083333s` duration, `3,029,621` bytes. | `holds` | None. |
| Assembly and cut boundary (`shot-01` frame `120` → `shot-02` frame `0`) | Decoded 3x2 contact sheet from `05-final-1.mp4` at frames `0` (`0.00s`), `119` (`4.96s`), `120` (`5.00s`, end of `shot-01`), `121` (`5.04s`, start of `shot-02`), `122` (`5.08s`), and `361` (`15.04s`, final frame) inspected via `vision_analyze`. Frame `120` and frame `121` align in composition, character pose/position, and lighting across the `5.041667s` splice without frame corruption or jump cuts. | `holds` | Sampled boundary inspection plus stream-copy byte preservation; inherits the minor cloak/leg phase difference noted in `02-review-1.md`. |
| Story sequence clarity and ending | Frame `0` shows Hermes foreground-facing on the viaduct; by frames `119–122` he has pivoted away-facing along the road; by frame `361` (`15.04s`) he has progressed deeper along the near paved causeway toward the distant city while remaining in stride. | `holds` | Inherits the previously accepted `shot-02` gold-channel flare/bloom (`2.75–4.0s`, `7.5–8.5s` within `shot-02`, corresponding to `~7.79–9.04s` and `~12.54–13.54s` in the assembled timeline) and possible closing foot sliding from `02-review-1.md`. |
| Final visual identity and style exclusions | `-c copy` altered zero video packets; `vision_analyze` on the 6 decoded frames from `05-final-1.mp4` confirms 16:9 framing, character silhouette/wardrobe, viaduct architecture, and zero added text, captions, watermarks, or overlays. | `holds` | Rear-view micro facial/staff/footwear detail remains occluded (`cannot see`), as recorded in `02-review-1.md`. |
| Requested voice/sound/text (`none`) | `ffprobe` confirms only stream `index=0` (`codec_type=video`) exists; zero audio or subtitle streams are present. | `holds` | None (`audio: none` was requested). |

Review purpose/clarity, identity, continuity, pacing and selected audio/text.
Source clip acceptance alone is not evidence that the finished piece succeeds.

## Drift notes
- What needs a new composition attempt or an upstream shot/intent revision: No composition-stage drift was introduced; lossless stream-copy preserved the exact accepted pixels and timing of `shot-01` and `shot-02`. The retained upstream findings in `shot-02` (gold-channel flare/bloom and possible closing foot sliding) remain documented for future prompt/shot-specificity work if a revision is later commissioned.
- Preserved sources and smallest affected scope: Both source clips (`hermes-sky-bridges-destination-walk/04-video-1.mp4` and `hermes-sky-bridges-stride-continuation/04-video-1.mp4`), their render records, `runs/motion/location-probes/manifest.md`, and `02-review-1.md` remain unchanged.

## Acceptance evidence
Acceptance is pending until the human decides on this exact final export and
record version. Status/verdict are authoritative. Cite actual approval evidence
already supplied when deriving a record; do not invent a future receipt or
rewrite the findings after acceptance. Later approval changes metadata only.

## Local filing boundary
This record names the single final export and its source versions. Acceptance
completes local filing only; publication needs separate authorization and a
verified receipt. No automatic uploads or replacement of accepted source clips.
