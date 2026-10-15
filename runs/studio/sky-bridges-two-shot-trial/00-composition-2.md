---
production: sky-bridges-two-shot-trial
attempt: 2
stage: studio/00_intake
status: approved
generated: 2026-10-15T07:52:26.077194+00:00
sources:
  - runs/studio/sky-bridges-two-shot-trial/00-intake-2.md
  - runs/studio/sky-bridges-two-shot-trial/00-composition-1.md
  - runs/studio/sky-bridges-two-shot-trial/02-review-1.md
  - runs/studio/sky-bridges-two-shot-trial/05-record-1.md
  - runs/motion/location-probes/manifest.md
  - runs/motion/location-probes/hermes-sky-bridges-destination-walk/04-render-1.md
  - runs/motion/location-probes/hermes-sky-bridges-stride-continuation/04-render-1.md
---

# sky-bridges-two-shot-trial, early composition brief (attempt 2 — corrective post-processing and distant-birds layer)

Copy to `runs/studio/<production>/00-composition-N.md` only when finishing is
selected. This can inform early shot planning; it does not execute composition.

## Outcome link
- Intake version owning purpose/audience: `runs/studio/sky-bridges-two-shot-trial/00-intake-3.md` (working sibling cross-reference in the same review package; not hashed here to avoid circular hash dependencies).
- Finished deliverable and selected finishing scope: Corrective silent assembly (`runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`) applying three `05_compose` post-processing fixes to the existing accepted sky-bridges clips while preserving `05-final-1.mp4` for comparison:
  1. **Lighting/color match + soft splice:** Match `shot-02` luma/chroma to `shot-01`'s outgoing frame (`lutyuv=y=val*0.975+4.4:u=val+1.225:v=val-1.424`) and blend the `shot-01` → `shot-02` boundary with a `0.25s` (`6`-frame) cross-dissolve (`xfade`) to eliminate the visible exposure/gait step at `5.0s`.
  2. **Walking pace (cadence) alignment:** Slightly accelerate `shot-02` by `12%` (`setpts=0.88*PTS` at `24/1` fps, trimming duration from `10.04s` to `~8.84s`) so Hermes's slower step cadence in `shot-02` matches his brisker post-pivot stride at the end of `shot-01`.
  3. **Ambient background movement (distant birds):** Composite a subtle 2D woodblock-ink flock of 5 small birds gliding and gently flapping high across the upper-right dusk sky toward the distant city (`x=700..1180, y=70..210`, dark charcoal/sepia silhouette matching `world/style.md`).

## Voice and sound
- Narration requested, exact script or approved script source, or none: none.
- Supplied voice/audio source and permissions, or explicitly needed preparation: none.
- Music/effects requested, intended purpose, source/permission or none: none.
- Pacing or timing constraints that shots must accommodate: `shot-01` plays at `1.00x` (`5.041667s`); `shot-02` plays at `1.136x` (`setpts=0.88*PTS`, `~8.836s`); with a `0.25s` cross-dissolve at `4.791667s`, total assembled duration is `~13.625s` (`327` frames at `24/1` fps).

## On-screen text
- Exact titles/captions or approved text source, or none: none.
- Language, appearance, readability and safe-area requirements: none (no lettering/captions; the only overlay layer is the non-text woodblock bird flock in the upper-right sky).

## Delivery
- Required format/aspect/dimensions/frame rate/audio and any accessibility checks: MP4 container (`runs/studio/sky-bridges-two-shot-trial/05-final-2.mp4`), H.264 High profile (`yuv420p`, `crf 18`), `1280x720` (`16:9`), `24/1` fps, silent (`audio: none`).
- Observable final acceptance criteria:
  1. `ffprobe` + `signalstats` confirm `shot-02`'s opening luma/chroma matches `shot-01`'s outgoing luma/chroma within `<0.6` YAVG/UAVG/VAVG units and transitions smoothly across the `0.25s` cross-dissolve.
  2. `shot-02` pace is visibly brisker (`setpts=0.88*PTS`), reducing the cadence drop after the cut.
  3. Decoded frames and playback confirm the distant bird flock glides across the upper-right sky toward the distant city in matte charcoal-sepia woodblock tone without crossing in front of Hermes or violating `world/style.md`.
  4. Honest boundary disclosure: sandal heel-wing asymmetry (`2 on 1 foot, 1 small on the other`) remains unchanged because it is baked into the character's moving feet and requires `04_animate` regeneration rather than `05_compose`.

## Handoff
- Exact approved sources and decision evidence:
  - `runs/studio/sky-bridges-two-shot-trial/00-intake-2.md` (`d0488f7c40353077e3b0e72059e95cff56ec7c62e28d67ef8d42ba274c65323f`, `status: approved`)
  - `runs/studio/sky-bridges-two-shot-trial/00-composition-1.md` (`658da25f8e9281d0586abae252cb5fd7b98c2c86489e3b74dd0b6361e5166289`, `status: approved`)
  - `runs/studio/sky-bridges-two-shot-trial/02-review-1.md` (`5d325f899c06b39ab4d5d2d873570e2badde751e86b3d93fe1d67053badc7e0a`, `status: approved`, `verdict: accepted`)
  - `runs/studio/sky-bridges-two-shot-trial/05-record-1.md` (`cc4c90327c60f009f9e356842ee71250b3a2c2ac52d86ad62ff2b11141fe092f`, `status: approved`, `verdict: accepted`)
  - `runs/motion/location-probes/manifest.md` (`aa3434295f5be6bd291720befe3520570fcb3895368d41420d562337f27a538d`)
- Receiving composition producer: Hermes (`05_compose/CONTEXT.md` → `runs/studio/sky-bridges-two-shot-trial/05-spec-2.md`).
- Earlier framing/timing implications (not baked into generated animation): Reuses the existing accepted clips without re-rendering them.
- Execution route: CPU-throttled local `nice -n 19 ffmpeg -threads 2` consuming the two accepted MP4s and a procedurally generated RGBA bird-flock overlay stream (awaits separate approval at `05-spec-2.md`).
- Revision impact and prior version, if any: Supersedes `00-composition-1.md` (`attempt: 1`) while preserving `05-spec-1.md`, `05-final-1.mp4`, and `05-record-1.md`.

## Open
- Unanswered finishing intent or delivery questions: none. Ready for package approval alongside `00-intake-3.md` and `02-review-2.md`.

No voice, sound, text generation or assembly is authorized by this template.
Finish execution waits for accepted animation and the composition-stage gates.
