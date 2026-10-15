---
production: sky-bridges-two-shot-trial
attempt: 1
stage: studio/00_intake
status: approved
generated: 2026-10-15T07:13:42.829649+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
---

# sky-bridges-two-shot-trial, early composition brief

Copy to `runs/studio/<production>/00-composition-N.md` only when finishing is
selected. This can inform early shot planning; it does not execute composition.

## Outcome link
- Intake version owning purpose/audience: `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md` (working sibling cross-reference in the same review package; not hashed here to avoid circular hash dependencies).
- Finished deliverable and selected finishing scope: Cut-only silent assembly (`runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`) joining the two accepted sky-bridges clips (`shot-01` then `shot-02`) end-to-end without trimming, voice, music, sound effects, or on-screen text overlays.

## Voice and sound
- Narration requested, exact script or approved script source, or none: none.
- Supplied voice/audio source and permissions, or explicitly needed preparation: none.
- Music/effects requested, intended purpose, source/permission or none: none.
- Pacing or timing constraints that shots must accommodate: Preserve full untrimmed durations of both accepted clips (`shot-01`: `5.041667s` / 121 frames; `shot-02`: `10.041667s` / 241 frames; combined `15.083334s` / 362 frames at 24fps).

## On-screen text
- Exact titles/captions or approved text source, or none: none.
- Language, appearance, readability and safe-area requirements: none (preserves `world/style.md` exclusion of lettering/captions/overlays and permits lossless stream-copy without pixel re-encoding).

## Delivery
- Required format/aspect/dimensions/frame rate/audio and any accessibility checks: MP4 container, H.264 High profile (`yuv420p`), `1280x720` (`16:9`), `24 fps` (`24/1`), `362` frames (`15.083334s`), no audio streams (`audio: none`), direct cut at `shot-01` frame 120 → `shot-02` frame 0 without trimming.
- Observable final acceptance criteria:
  1. `ffprobe` confirms H.264 `1280x720`, `24/1` fps, `362` frames (`~15.083334s`), and no audio stream on `runs/studio/sky-bridges-two-shot-trial/05-final-1.mp4`.
  2. Sampled/decoded frame verification across the assembled file confirms `shot-01` (0.0s–5.0s) transitions cleanly into `shot-02` (5.04s–15.08s) at the cut boundary without corrupt frames, aspect/style changes, or unapproved trims.

## Handoff
- Exact approved sources and decision evidence:
  - `runs/studio/sky-bridges-two-shot-trial/00-intake-1.md` (`1ba4c0b51a6d030b71f17934925237d81ead1767df1447b17ea1c859b721872f`, `status: approved`)
  - `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` (`5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a`, `status: approved`, `verdict: accepted`)
  - `runs/motion/location-probes/manifest.md` (`aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d`)
  - `runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md` (`1edb38d60ea03d6017bbd4d30e694b2258bb34ca86d7322b0e0a2d02ebd5ddf6`, `status: approved`, `verdict: accepted`)
  - `runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md` (`9f44625dbfff611ca658dcf1d9a22e2b8d7004b2bae17e6fc6cce946d51f89e9`, `status: approved`, `verdict: accepted`)
- Receiving composition producer: Hermes (`05_compose/CONTEXT.md` → `runs/studio/sky-bridges-two-shot-trial/05-spec-1.md`).
- Earlier framing/timing implications (not baked into generated animation): Both clips are already generated and accepted (`5.041667s` + `10.041667s` = `15.083334s` total at 24fps, 1280x720, silent); no re-rendering of source clips.
- Execution route: unselected/unverified until separately authorized at `05_compose`. (Candidate low-CPU route for silent cut-only assembly: local `ffmpeg -f concat -safe 0 -c copy` lossless stream-copy with zero video re-encoding.)
- Revision impact and prior version, if any: First composition brief (`attempt: 1`); no prior version.

## Open
- Unanswered finishing intent or delivery questions: none. All finishing choices resolved via operator selection (`approve reccomended`). Ready for package approval alongside `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md`.

No voice, sound, text generation or assembly is authorized by this template.
Finish execution waits for accepted animation and the composition-stage gates.
