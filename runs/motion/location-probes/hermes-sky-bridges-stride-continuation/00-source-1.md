---
set: location-probes
shot: hermes-sky-bridges-stride-continuation
attempt: 1
stage: 04_animate
kind: decoded-frame-sidecar
status: approved
verdict: accepted
generated: 2026-10-04
sources:
  - 00-source-frame.png
  - ../hermes-sky-bridges-destination-walk/04-render-1.md
  - ../hermes-sky-bridges-destination-walk/04-video-1.mp4
  - ../manifest.md
---

# Stride continuation, decoded-frame source record 1

This is a draft sidecar for a real frame extracted from an accepted video,
not an image-generation receipt. The operator has accepted the pixels for reuse;
the current workflow does not yet declare this source-filing mode. This record
is not a ready motion input until the filing mode and this record are approved.

## Selected frame

- Image: `00-source-frame.png`.
- SHA-256: `9525ddf63dd8d6008392dab6ce3196a418fdb322736bbcdb8653924c8d5217fe`.
- Actual format and dimensions: PNG, 1280x720.
- Source frame: zero-based decoded frame 120, timestamp 5.0 seconds.
- Selection: exact final decoded frame of the accepted predecessor.
- Processing: decode to PNG only. No crop, resizing, interpolation, repainting
  or image generation. The frame has one retained home at the path above.

## Accepted predecessor and filing evidence

- Video: `../hermes-sky-bridges-destination-walk/04-video-1.mp4`.
- Video SHA-256: `b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332`.
- Authoritative render record:
  `../hermes-sky-bridges-destination-walk/04-render-1.md`.
- Verified predecessor record: `status: approved`, `verdict: accepted`.
- Accepted manifest: `../manifest.md`, row
  `hermes-sky-bridges-destination-walk`, attempt 1, matching the video hash.
- Measured source media: H.264, 1280x720, 24 fps, 121 decoded frames,
  container duration 5.041667 seconds, no audio stream.
- Existing accepted video, its render record and its manifest remain unchanged.

## Derivation evidence

The selected video hash and frame count were checked before extracting frame
120. The extraction used ffmpeg's `select=eq(n\,120)` with one output frame and
no scale/crop filter. The resulting PNG was visually inspected and retained
byte-for-byte at `00-source-frame.png`; its hash was rechecked after approval.

Reproduction command, with a new destination rather than overwriting the source:

```sh
ffmpeg -v error -i ../hermes-sky-bridges-destination-walk/04-video-1.mp4 -vf 'select=eq(n\,120)' -frames:v 1 -n <new-output.png>
```

Run relative to this source record's folder. Different decoders may encode PNG
bytes differently; the retained file and hash above are the approved input.
No image-generation prompt, model, job ID, seed or charge exists for this PNG.
Do not manufacture those fields from the predecessor's video-generation receipt.

## Source-frame acceptance evidence

Jordan replied **“approve”** to the desktop review asking:
**“Approve this 10-second brief and starting frame?”**
That review displayed the exact `00-source-frame.png` and `00-brief.md` for this
continuation. The frame hash above matches the displayed candidate. The same
approval allowed recording `status: approved` on the brief without changing its
body; its post-approval SHA-256 is
`7dc8ba97f931930ea84e4a4438df5896d7df6433b97a4e71094e296e7e111d27`.
No separate message ID was exposed in this desktop exchange.

This evidence accepts the frame as a source. It does not approve this newly
written sidecar, change the workflow contracts, authorize publication or permit
paid video generation.

## Appearance and review limits

The exact source pixels control appearance and starting pose. Preserve the
rear-facing character, current scale/position, dark cloak, partially occluded
staff, existing architecture, gold channel placement and accepted illustration.
Do not repair inherited colour deviations or invent facial/staff microdetail.

The single frame does not prove gait phase, velocity or footfall timing. Nearby
closing samples at 4.0, 4.5 and 5.0 seconds support ongoing travel, with sampled
review limitations. The continuation must be reviewed against actual adjacent
footage rather than assuming a matching frame guarantees a smooth join.

## Publication and execution boundary

- Public URL for this PNG: none.
- Public hosting permission: not granted by the brief/frame approval.
- Motion spec/render approval: not yet requested or granted.
- New video, assembly, commit or push: none for this continuation.

## Human check

Confirm the selected frame, predecessor provenance, source hashes and recorded
approval evidence. Approval of this record may change only its `status` and
`verdict` metadata. It does not authorize a new render or a public upload.
