---
set:
shot:
attempt:
stage: 04_animate
kind: decoded-frame-sidecar
status: draft
verdict:
generated:
sources:
---

# <shot>, decoded-frame source record <attempt>

Copy to `runs/motion/<set>/<shot>/00-source-N.md` only for the decoded-frame
mode in `_reference/motion-rules.md`. This sidecar files one extracted PNG;
there is no image-generation receipt. A copied template is not approved.
Keep an accepted record intact; revisions use a new record and new image path.

## Selected frame

- Image path, relative to this record:
- Frame SHA-256:
- Actual format and dimensions:
- Source frame: zero-based decoded frame index and measured timestamp:
- Why this frame was selected:
- Processing: decode only; no crop, resize, interpolation or repainting.

## Accepted predecessor and filing evidence

- Predecessor video path and measured SHA-256:
- Authoritative predecessor render record path and observed status/verdict:
- Accepted motion-manifest path and exact matching shot/attempt/hash row:
- Measured frame rate/timebase, frame count, duration, dimensions and audio:

Read the actual records and media. A filename or the presence of an MP4 is not
acceptance, and an accepted video does not automatically approve an extracted PNG.

## Derivation evidence

- Exact extraction command/settings and working directory:
- Verification that the retained PNG is the selected decoded frame:
- Actual file hash/format/dimensions and inspection method:

No image-generation prompt, model, job, seed or charge applies to decoding.
For variable-frame-rate footage retain decoded timestamps, not a guessed rate.

## Source-frame acceptance evidence

- Exact human approval identifying the image/version, or pending:
- Approval scope and record review evidence, or pending:

Image acceptance and approval of this sidecar may be grouped when both are
presented. Never preapprove a future record or transfer acceptance to new pixels.

## Appearance and review limits

- Visible starting pose, direction, scale, framing and route space:
- Inherited accepted appearance/deviations and obscured detail:
- Nearby sampled frames and what they establish, with timestamps:
- Motion/join uncertainties that a single frame cannot establish:

## Publication and execution boundary

- Public source URL and verified publication evidence, or none:
- Public hosting approval, or not granted:
- Motion-spec/render approval remains separate.

Do not duplicate the media or upload it automatically. Public hosting of the
predecessor's earlier source image does not authorize publishing this PNG.

## Human check

Review the exact frame, provenance, hashes and declared limitations. After
explicit approval of the completed record and frame, change only `status` to
`approved` and `verdict` to `accepted`. Record later evidence in the consuming
spec rather than rewriting this body. The approved sidecar is the local filing
home; it does not replace any separate publication, spec/render or video gate.
