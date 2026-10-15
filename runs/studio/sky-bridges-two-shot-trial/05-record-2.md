---
production: sky-bridges-two-shot-trial
attempt: 2
stage: 05_compose
status: approved
verdict: drifted
generated: 2026-10-15T08:00:27.919720+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-3.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-2.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-2.md
  - runs/studio/sky-bridges-two-shot-trial/05-spec-2.md
  - runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4
---

# sky-bridges-two-shot-trial, final export review and local filing (attempt 2 — corrective post-processing & distant birds)

Copy to `runs/studio/<production>/05-record-N.md` only after actual authorized
execution. The canonical export is `runs/studio/<production>/05-final-2.mp4`.
Never create an empty or invented file to complete this record.

## Actual export
- Final file path: `runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`
- Final file SHA-256: `397db857dc162a4832c52a1c8436db4ff1de877091866b813578391235ea3054`
- Actual media properties and evidence:
  - File size: `3,330,642` bytes
  - Container (`ffprobe`): `mov,mp4,m4a,3gp,3g2,mj2`, duration `13.625000` seconds
  - Video stream (`index=0`): `h264` (`High`), `yuv420p`, `1280x720` (`16:9`), `r_frame_rate=24/1`, `avg_frame_rate=24/1`, `nb_frames=327`, stream duration `13.625000` seconds
  - Audio / subtitle streams: none (`1` stream total, `codec_type=video`)
- Exact approved composition spec version and SHA-256: `runs/studio/sky-bridges-two-shot-trial/05-spec-2.md` (`attempt: 2`, `status: approved`, SHA-256 `d2220b6b0f4af4b7516fd1d6959d6d3506fd373c7b8ca67392d2ca8893414456`)
- Actual execution route/receipt, with unavailable metadata explicitly unknown:
  - Operator authorization: Jordan desktop chat reply **“approve”** after review of `05-spec-2.md` and the CPU-throttled local `ffmpeg` execution route.
  - Pre-execution verification: All 18 SHA-256 hashes in `05-spec-2.md`'s **Source manifest** matched on disk prior to execution.
  - Overlay generation: `python3` stdlib generated `340` frames of `520x160` RGBA woodblock bird-flock silhouettes (`#2d2622` charcoal-sepia ink, `0.19s` elapsed).
  - Command executed: `nice -n 19 ffmpeg -y -v error -threads 2 -i runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-video-1.mp4 -i runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-video-1.mp4 -f rawvideo -pixel_format rgba -video_size 520x160 -framerate 24 -i /opt/data/cache/scratch/birds_520x160_24fps.rgba -filter_complex "[0:v]fps=24,settb=AVTB[v0];[1:v]lutyuv=y=val*0.975+4.4:u=val+1.225:v=val-1.424,setpts=0.88*PTS,fps=24,settb=AVTB[v1];[v0][v1]xfade=transition=fade:duration=0.25:offset=4.791667[vjoin];[vjoin][2:v]overlay=x=680:y=60:shortest=1,format=yuv420p[vout]" -map "[vout]" -c:v libx264 -profile:v high -crf 18 -preset veryfast -movflags +faststart runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`
  - Wall-clock encode time: `3.35` seconds on 2 `nice -n 19` threads ($0 cost, no host CPU spike).

## Findings
| Brief/spec criterion | Actual observation and timestamp/evidence | Result | Limitations or unresolved issue |
|---|---|---|---|
| 1. Lighting & color continuity across the cut (`4.75s–5.17s`) | `ffprobe` `signalstats` across frames `114–124` shows the abrupt `1.83`-unit luma drop and `+1.77` saturation jump from `05-final-1.mp4` (`frame 120: Y=105.57, V=143.51, SAT=24.03` → `frame 121: Y=103.74, V=144.93, SAT=25.80`) is eliminated in `05-final-2.mp4` (`frame 120: Y=105.42, V=143.04, SAT=23.82` → `frame 121: Y=105.14, V=142.87, SAT=23.85`). `vision_analyze` on the 6-frame contact sheet confirms no visible brightness or color jump across the `0.25s` cross-dissolve. | `holds` | `shot-02`'s localized mid-clip channel-flare bloom on the near parapet (`~7.1s–8.2s` in the accelerated timeline) remains softened slightly by `lutyuv` (`0.975*Y`) but is still present in the source pixels. |
| 2. Walking pace (cadence) alignment (`setpts=0.88*PTS`) | `ffprobe` confirms total duration is `13.625000s` (`327` frames at `24/1` fps), accelerating `shot-02` by `12%` (`1.136x`) from `10.04s` to `8.83s` so step cadence aligns closer to `shot-01`'s outgoing stride. | `holds` | Uniform clip time-scaling aligns overall step tempo; it does not alter the subtle foot-sliding artifact in the final seconds of `shot-02`. |
| 3. Ambient background movement (`5` distant woodblock birds) | `vision_analyze` on the `1.0s`, `6.0s`, and `11.0s` sky crops (`520x200` at `x=680, y=60`) and the full-frame contact sheet confirms 5 small matte charcoal-sepia woodblock-ink birds gliding and gently flapping left-to-right across the orange sunset sky toward the distant city (`left of sun at 1.0s` → `passing above sun at 6.0s` → `approaching distant city at 11.0s`). | `holds` | 2D procedural woodblock layer composited in `05_compose`; does not require regenerating the base video. |
| 4. Delivery format, dimensions, frame rate, and silent audio | `ffprobe` verifies `h264` (`High`), `yuv420p`, `1280x720` (`16:9`), `24/1` fps, `327` frames, `13.625000s`, and `0` audio/subtitle streams. | `holds` | None. |
| 5. Unchanged character-pixel boundary (sandal heel-wings) | Rear-view sandal heel-wing asymmetry (`2 wings on 1 foot and 1 small wing on the other`) remains unchanged in the moving character pixels. | `drifted` (inherited from `shot-01`/`shot-02` source clips; deferred by design in `00-intake-3.md` / `02-review-2.md`) | Confirms the exact boundary: `05_compose` resolves exposure/color seams, clip cadence, cut smoothing, and ambient sky layers, whereas character-part geometry baked into moving limbs requires `04_animate` regeneration (or a rear-facing starting still). |

Review purpose/clarity, identity, continuity, pacing and selected audio/text.
Source clip acceptance alone is not evidence that the finished piece succeeds.

## Drift notes
- What needs a new composition attempt or an upstream shot/intent revision:
  - **Resolved in `05_compose` (`05-final-2.mp4`):** Cross-shot lighting/color jump (`ΔY` reduced from `-1.83` to `-0.28`; `ΔSAT` reduced from `+1.77` to `+0.03`), `shot-02` walking cadence (`+12%` pace match + `0.25s` `xfade`), and distant background bird movement (`5` woodblock birds gliding across the upper-right sky).
  - **Requires upstream `04_animate` / `01_spec` if a future regeneration pass is commissioned:** Rear-view sandal heel-wing symmetry (`2 on 1 foot and 1 small on the other`) and strict one-pulse-per-step confinement of the near parapet gold channel.
- Preserved sources and smallest affected scope: `05-final-1.mp4`, `05-record-1.md`, `02-review-1.md`, and both source clips in `runs/motion/location-probes/` remain untouched on disk.

## Acceptance evidence
Acceptance is pending until the human decides on this exact final export and
record version. Status/verdict are authoritative. Cite actual approval evidence
already supplied when deriving a record; do not invent a future receipt or
rewrite the findings after acceptance. Later approval changes metadata only.

## Local filing boundary
This record names the single final export and its source versions. Acceptance
completes local filing only; publication needs separate authorization and a
verified receipt. No automatic uploads or replacement of accepted source clips.
