---
set: location-probes
shot: hermes-sky-bridges-destination-walk
attempt: 1
stage: 04_animate
status: approved
verdict: accepted
generated: 2026-10-04T06:53:21.365221+00:00
sources:
  - 01-spec-1.md
  - 04-video-1.mp4
---

# Hermes destination walk, motion render 1

## Prompt as sent

Animate the supplied reference image as one continuous shot with a fixed camera. Hermes first makes a small but clearly visible head adjustment to survey the distant city at screen-right. From his foreground-facing stride, he then pivots his feet, hips and shoulders naturally toward the road's rightward curve and away from the viewer. He walks at a measured pace diagonally screen-right and into depth along the visible near stone paving, with alternating steps producing clear displacement relative to the road. His head turns to align with the route ahead. Keep him on the near stretch inside the parapet, not arriving at the distant city. He continues walking as the shot ends; no stop or final settle.

Keep his calm attentive expression. The cloak responds naturally to his turn and steps, and his staff moves coherently with him without intersecting his body or the pavement. Background motion remains quiet so the head adjustment, body pivot and walking are readable. Maintain continuous foot contact without sliding, teleporting, duplicated limbs or clipping through the parapet.

Preserve the supplied character's identity, facial structure, proportions, hair and winged helmet design, slate-grey tunic, dark cloak, leather fittings, bronze armour, winged sandals and twin-serpent staff. Allow his head direction, gaze, body orientation, limb poses, position and cloth shapes to change with the action; do not freeze his starting pose. Retain the brown hair and existing heraldic banners as shown. Preserve the grounded architecture, paving, parapet, ravine and distant city, dusk palette, route lights, distinct contours, flat colour blocking and matte textured-paper illustration. No photographic, three-dimensional or painterly makeover, no new scene elements, captions or overlays. The camera remains completely fixed with the same framing and perspective: no pan, zoom, push, follow or cut.

## Tool metadata
- tool: video_generate
- configured provider: nous
- configured model: bytedance/seedance-2.5
- returned provider: fal
- returned model: seedance-2.5
- returned endpoint: bytedance/seedance-2.5/image-to-video
- job: not exposed
- returned video URL: https://v3b.fal.media/files/b/0aacff21/4qz-tdubfpQOi-50MFqhH_video.mp4
- source image: runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png
- source SHA-256: 2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3
- source URL: https://raw.githubusercontent.com/founder-lgw-01/hermes-video-assets/main/hermes-sky-bridges-and-passages.png
- reference verification: anonymous HTTP 200 and exact source hash match; all five manifest input hashes matched before submission
- media_id: not applicable
- audio / upscale requested: false / false; returned upscaled: false
- duration requested: 5 seconds; tool returned: 5; measured: 5.041667 seconds
- aspect requested: 16:9; tool returned empty string; measured dimensions establish 16:9
- resolution requested: 720p; measured: 1280x720
- codec / frame rate / frames: h264 / 24 fps / 121
- audio streams measured: none
- file: 04-video-1.mp4
- SHA-256: b69881409c54eef5352d7b62fb7aaa65d712e336b0d5145f8f5fee33d7143332
- size: 1434494 bytes

## Visual consistency findings
Inspection method and limits: video_analyze failed because its current provider
rejects video_url. No analysis-provider change made. Fallback sampled inspection:
2fps contact sheet plus exact decoded frames 0,96,108,120 (0,4,4.5,5 seconds).
Opening and final frames included; no claim of exhaustive gait/contact review.

- holds: sampled architecture, road, city, dusk palette and background framing
  stay consistent through the turn and travel.
- holds: broad helmet/cloak/tunic/armour/character design remains recognizable.
- cannot see: micro facial identity from rear/wide view; staff ornament partly
  occluded by cloak and body in closing samples.
- uncertain: footwear and staff detail appear simplified in rear views, but
  viewpoint, occlusion and sample resolution prevent a definite costume-change
  conclusion. Original accepted still is not re-evaluated.

## Motion success findings
| Brief criterion | Finding | Timestamped evidence |
|---|---|---|
| Natural body pivot | holds in samples | 0s foreground-facing; early contact-sheet samples show side view then rear view; back-facing by middle of clip. Inter-frame smoothness not exhaustively checked. |
| Primary travel | holds in samples | Rear-facing character shifts screen-right relative to paving during latter contact-sheet samples; 4,4.5,5s exact frames show incremental displacement and changed leg poses. Depth recession modest. |
| Head survey then route alignment | cannot see full independent survey | Early samples show head rotating screen-right and later aligned away; cannot reliably distinguish separate surveying adjustment from the body pivot. |
| Fixed camera | holds in samples | Columns, city, sun and paving remain stable across sheet and 0–5s boundary frames. |
| Continuing ending | holds with sampling limits | Different feet/body placement at 4,4.5,5s supports continued travel, rather than a frozen ending; uninterrupted final gait not proven. |
| Pavement contact / no clipping | cannot see continuous contact | Samples keep figure on near road, without evident parapet intersection; foot sliding between samples unverified. |
| Staff/cloak/design continuity | holds broadly; detail cannot see | Cloak rotates/trails and staff stays present; rear-view ornamentation/footwear detail obscured or simplified. |

## Acceptance and filing
- Operator approval evidence: pending; spec/render authorization was 'approve the spec', not video acceptance.
- Manifest: not filed; awaiting video acceptance.

## Drift notes
The clear body turn and net travel are stronger than a near-static clip. The
separate initial head survey is not verified by sampled evidence. Rear-view
footwear/staff detail may simplify; review actual playback for foot contact,
prop continuity and the final walking beat before acceptance. No automatic retry.
