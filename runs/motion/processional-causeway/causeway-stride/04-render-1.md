---
set: processional-causeway
shot: causeway-stride
attempt: 1
stage: 04_animate
status: approved
verdict: accepted
generated: 2026-10-15T13:37:00+00:00
sources:
  - runs/motion/processional-causeway/causeway-stride/01-spec-1.md
  - runs/processional-causeway/causeway-stride/03-sidecar.md
  - runs/processional-causeway/causeway-stride/02-image-4.png
  - runs/motion/processional-causeway/causeway-stride/04-video-1.mp4
---

# causeway-stride, motion render 1

## Prompt as sent

Animate the supplied reference image as one continuous five-second shot from a completely fixed camera. Hermes strides forward toward the foreground along the cracked limestone road at a steady pace of about two steps per second, maintaining his full-stride cadence right through the final frame with no slowing down, stopping, or settling in the final second. As he walks, he makes a slight, natural head turn toward the fluted stone route marker on screen-right and then aligns his calm, focused gaze forward again, while his dark-charcoal chlamys cloak billows lightly with his steps and his right hand carries the bronze twin-serpent winged caduceus coherently at his side.

On each planted footstep, a brief pulse of liquid warm-gold energy surges along the shallow carved stone gutters running strictly along the inside base of the left and right stone curbs bordering the road, easing back between steps while the entire center limestone roadbed remains unlit matte stone with no gold lines in the middle of the road.

Preserve the supplied character's exact visual design, proportions, square-jawed bronze face, golden-brown curls, antique-bronze winged helmet with symmetrical side wings, charcoal-grey undertunic with sepia hem edge, dark-charcoal cloak with gold clasp, brown leather cross-body harness and hip pouch, and bronze bracers and greaves. Keep his winged sandals symmetrical throughout every step: one pale feathered wing projecting outward from the outer ankle of the left boot and one matching pale feathered wing projecting outward from the outer ankle of the right boot, with completely smooth, wingless inner ankles between his legs—no inverted wings, no flipped anatomy, no mirrored limbs, and no wrong-side wing placement. Preserve the grounded stone causeway, curbs, cypress trees, hilltop temple, dusk palette, and traditional Japanese woodblock-print (ukiyo-e) illustration with dark ink keylines, flat color planes, and matte parchment texture, with no camera movement, no pan, no zoom, and no 3D realism.

## Tool metadata

- tool: native `video_generate`
- configured provider: `nous`
- configured model: `bytedance/seedance-2.5`
- returned provider: `fal`
- returned model: `seedance-2.5`
- returned endpoint: `bytedance/seedance-2.5/image-to-video`
- returned modality: `image`
- job ID / seed / cost: `not exposed`
- returned video URL: `https://v3b.fal.media/files/b/0aae7c44/ASGKJUFysMT6jYj3e_slS_video.mp4`
- source image: `runs/processional-causeway/causeway-stride/02-image-4.png` (`1344x752`, `sha256:1bc5e53db713781d5a090752610a990aa9fe4c245555052f063516308d211252`)
- source sidecar: `runs/processional-causeway/causeway-stride/03-sidecar.md` (`status: approved`, `verdict: accepted`)
- source URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3D12LhjI1GaOgTMnfV4aJLtt265/hf_20261015_132923_a14a5b00-fcfa-4a92-b23e-5f82bb0ade09.png` (anonymous HTTP 200 verified, exact SHA-256 match)
- duration requested: `5` seconds; returned: `5`; measured: `5.041667` seconds (`121` frames at `24/1` fps)
- aspect ratio requested: `16:9`; returned field: empty string; measured dimensions: `1282x718` (~16:9)
- resolution requested: `720p`; measured: `1282x718`
- audio requested: `false`; measured audio streams: none
- upscale requested: `false`; returned `upscaled`: `false`
- file: `runs/motion/processional-causeway/causeway-stride/04-video-1.mp4` (`2140736` bytes, `sha256:fa416253ee1017bb60daf754ad93c494f8e4ff56d52ca2cf7a3149884caea077`)
- generated: `2026-10-15T13:37:00+00:00`

## Visual consistency findings

Sampled review limits: inspected 6 decoded frames across the full 5.0-second clip (`frame 0` at `0.0s`, `frame 24` at `1.0s`, `frame 48` at `2.0s`, `frame 72` at `3.0s`, `frame 96` at `4.0s`, `frame 120` at `5.0s`) plus full-resolution inspection of the final frame (`frame 120`).

- **Paired sandal-wing symmetry & anti-inversion (`At risk`):** `holds` from `frame 0` (`0.0s`) through `frame 120` (`5.0s`) — each boot retains its single pale feathered wing projecting outward from its outer ankle (left boot wing on screen-left, right boot wing on screen-right), and the inner ankles facing the gap between his legs remain completely smooth and wingless across the entire walk cycle.
- **Curb-side gold energy confinement (`At risk`):** `holds` on center-roadbed cleanliness (`0.0s–5.0s`) — zero gold lines meander into the center limestone roadbed; warm-gold energy pulses run along the inside base of the stone curbs (strongest along the screen-right curb around `2.0s–4.0s`, with lighter warm-gold highlights on the left curb by `5.0s`).
- **Identity, helmet wings, and default charcoal wardrobe (`At risk`):** `holds` across `0.0s–5.0s` — symmetrical helmet side wings, square-jawed bronze face, golden-brown curls, charcoal-grey undertunic with sepia edge, dark-charcoal chlamys with gold clasp, brown leather cross-body harness and pouch, bronze bracers and greaves, and twin-serpent caduceus hold without color or geometry drift.
- **Medium and fixed camera (`At risk`):** `holds` across `0.0s–5.0s` — traditional ukiyo-e woodblock print look with dark ink keylines and flat color areas holds; background temple, cypress trees, and stone markers remain locked with no camera pan or zoom.

## Motion success findings

| Brief criterion | Finding | Timestamped evidence and limits |
|---|---|---|
| Continuous forward stride (~2 steps/second) | `holds` | Alternating forward steps advance Hermes toward the foreground across `0.0s`, `1.0s`, `2.0s`, `3.0s`, `4.0s`, and `5.0s` (`frames 0..120`). |
| Slight head turn toward screen-right marker and return forward | `holds` | Head turns slightly toward screen-right across `1.0s–3.0s` (`frames 24..72`) and aligns forward again by `4.0s–5.0s` (`frames 96..120`). |
| Continuing stride through final frame (no end-of-clip stop) | `holds` | At `5.0s` (`frame 120`), Hermes is still mid-stride with feet alternating rather than settling into a static two-foot stop. |
| Curb-base warm-gold energy pulses on footsteps (no center-road river) | `holds` (stronger on right curb than left curb) | Warm-gold pulse surges visibly along the inside base of the screen-right curb during `2.0s–4.0s` (`frames 48..96`) and highlights both curb edges by `5.0s` (`frame 120`), while the center limestone roadbed remains completely unlit stone. |
| Outer sandal-wing symmetry throughout walk | `holds` | Both outer sandal wings stay locked to the outside of the left and right ankles with zero inner-ankle wing flipping from `frame 0` to `frame 120`. |

## Drift notes

None on character anatomy, sandal-wing symmetry, wardrobe, or roadbed cleanliness. Note for operator playback review: the curb-side gold pulse is much more pronounced along the inside base of the screen-right curb (`2.0s–4.0s`) than on the screen-left curb, which is partially behind Hermes in the lower-left foreground. Leave verdict open for operator decision (`accept` or `drift`).
