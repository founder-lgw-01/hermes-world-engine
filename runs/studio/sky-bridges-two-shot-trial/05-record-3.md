---
production: sky-bridges-two-shot-trial
attempt: 3
stage: 05_compose
status: approved
verdict: accepted
generated: 2026-10-15T08:17:27.944727+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-3.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-2.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-2.md
  - runs/studio/sky-bridges-two-shot-trial/05-spec-3.md
  - runs/studio/sky-bridges-two-shot-trial/05-final-3.mp4
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, final export review and local filing (attempt 3 — stutter-free splice, 1.28x/1.54x pace, +1px stabilization, and distant birds)

Copy to `runs/studio/<production>/05-record-N.md` only after actual authorized
execution. The canonical export is `runs/studio/<production>/05-final-3.mp4`.
Never create an empty or invented file to complete this record.

## Actual export
- Final file path: `runs/studio/sky-bridges-two-shot-trial/05-final-3.mp4`
- Final file SHA-256: `a50aa72e8952eb7b4a2e5d15a2f69cc3531c91dcb4976f71e76be6f0fc5edfc6`
- Actual media properties and evidence:
  - File size: `3,176,111` bytes
  - Container (`ffprobe`): `mov,mp4,m4a,3gp,3g2,mj2`, duration `11.375000` seconds
  - Video stream (`index=0`): `h264` (`High`), `yuv420p`, `1280x720` (`16:9`), `r_frame_rate=24/1`, `avg_frame_rate=24/1`, `nb_frames=273`, stream duration `11.375000` seconds
  - Audio / subtitle streams: none (`1` stream total, `codec_type=video`)
- Exact approved composition spec version and SHA-256: `runs/studio/sky-bridges-two-shot-trial/05-spec-3.md` (`attempt: 3`, `status: approved`, SHA-256 `395a1c361c31f3946788e9f581916c8a1d2fe5f59c1946b17bddd7fb6628c4b5`)
- Actual execution route/receipt, with unavailable metadata explicitly unknown:
  - Command executed: `nice -n 19 ffmpeg -y -v error -threads 2 -i runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4 -i runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4 -f rawvideo -pixel_format rgba -video_size 520x160 -framerate 24 -i /opt/data/cache/scratch/birds_520x160_24fps.rgba -filter_complex "[0:v]split=2[v0a][v0b];[v0a]trim=start_frame=0:end_frame=96,setpts=PTS-STARTPTS[v0_fast];[v0b]trim=start_frame=96:end_frame=121,setpts=0.78*(PTS-STARTPTS)[v0_tail];[v0_fast][v0_tail]concat=n=2:v=1:a=0,fps=24,settb=AVTB[v0_fixed];[1:v]lutyuv=y=val*0.975+4.4:u=val+1.225:v=val-1.424,pad=1284:724:1:1:color=black,crop=1280:720:0:0,setpts=0.65*PTS,fps=24,settb=AVTB[v1_fixed];[v0_fixed][v1_fixed]concat=n=2:v=1:a=0,fps=24,settb=AVTB[vjoined];[vjoined][2:v]overlay=x=680:y=60:shortest=1,format=yuv420p[vout]" -map "[vout]" -c:v libx264 -profile:v high -crf 18 -preset veryfast -movflags +faststart runs/studio/sky-bridges-two-shot-trial/05-final-3.mp4`
  - Wall-clock encode time: `2.97` seconds on 2 `nice -n 19` threads ($0 cost).

## Findings
| Brief/spec criterion | Actual observation and timestamp/evidence | Result | Limitations or unresolved issue |
|---|---|---|---|
| 1. Stutter-free cut & lighting match (`4.0s–5.0s`) | Removing `xfade` and accelerating `shot-01` frames `96–120` by `1.28x` (`0.78*PTS`) eliminates the `4.8s–5.0s` double-image ghosting and pre-cut deceleration while `lutyuv` preserves the matched exposure across the `4.83s` splice. | `holds` | Accepted for test scope. |
| 2. Balanced walking pace (`1.54x` on `shot-02`) | `shot-02` at `setpts=0.65*PTS` (`1.54x`, total sequence `11.375s` / `273` frames) resolves the slow-motion drop of `05-final-2.mp4` (`1.13x`) without the over-sped look of the `2.22x` (`0.45*PTS`) probe. | `holds` | Accepted by operator (“good enough for our test”). |
| 3. Camera drift stabilization (`+1px, +1px` on `shot-02`) | `pad=1284:724:1:1,crop=1280:720:0:0` counteracts `shot-02`'s `(-1px, -1px)` landmark shift across the cut. | `holds` | Sub-pixel warps internal to `shot-02` remain minor. |
| 4. Ambient distant birds (`5` woodblock silhouettes) | 5 matte charcoal-sepia woodblock birds glide across the upper-right sky (`0.0s–11.375s`). | `holds` | None. |
| 5. Sandal heel-wing asymmetry (`2 on 1 foot, 1 small on the other`) | Confirmed present in the upstream starting still (`runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png`) and inherited by both motion clips. | `drifted` (upstream still/motion origin) | Requires upstream guard in `01_spec` / `02_render` / `04_animate` on future shots. |

Review purpose/clarity, identity, continuity, pacing and selected audio/text.
Source clip acceptance alone is not evidence that the finished piece succeeds.

## Drift notes
- What needs a new composition attempt or an upstream shot/intent revision:
  - Accepted for this compose test (`verdict: accepted`). Future shots must catch paired-appendage symmetry (such as sandal heel-wings), end-of-clip deceleration, continuation cadence, and camera micro-drift upstream in `01_spec`, `02_render`, and `04_animate`.
- Preserved sources and smallest affected scope: `05-final-1.mp4` (`attempt: 1`), `05-final-2.mp4` (`attempt: 2`), and all upstream clips/records remain preserved.

## Acceptance evidence
Operator desktop reply after viewing the `11.375s` (`1.54x`) export:
**“good enough for our test. I need to make sure we can fix this upstream better next time”**.

## Local filing boundary
This record names the single final export (`05-final-3.mp4`) and its source versions. Acceptance
completes local filing only; publication needs separate authorization and a
verified receipt. No automatic uploads or replacement of accepted source clips.
