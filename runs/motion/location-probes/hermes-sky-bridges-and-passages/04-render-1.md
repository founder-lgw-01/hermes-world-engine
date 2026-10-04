---
set: location-probes
shot: hermes-sky-bridges-and-passages
attempt: 1
stage: 04_animate
status: approved
verdict: accepted
generated: 2026-10-04T06:09:14+00:00
sources:
  - 01-spec-1.md
  - ../../../location-probes/hermes-sky-bridges-and-passages/03-sidecar.md
  - 04-video-1.mp4
---

# Sky bridges, motion render 1

## Prompt as sent

A single continuous 5-second shot preserving exactly the flat ukiyo-e woodblock print style of the supplied reference image: bold dark contour linework, broad flat areas of unmodulated single colour, hard-edged shapes, visible aged-parchment grain, and no gradients, no volumetric shading, no atmospheric haze, no depth-of-field blur, and no rendered realism at any point, so the final frame looks like the same printed illustration as the first. The young man in the reference image completes one stride forward along the stone road and settles, his tall athletic lean body, broad shoulders, proportions, and stride length unchanged across the whole shot; his calm watchful expression and his gaze toward the distant city do not change, and his face stays exactly as in the reference image, not altered and not made more detailed. His dark charcoal chlamys trails behind him and lifts slightly at the hem, then settles by the final frame without changing colour and without gaining any trim; his tunic hem, his belt pouches, and the feathered wings on his helmet and sandals sway lightly; the gold caduceus in his hand bobs a few degrees with the step and keeps its colour without becoming a light source. All of his clothing and hair keep the exact colours they have in the reference image and do not change during the shot. The brazier flame at the lower left flickers gently and throws a small moving reflection on the paving without growing; the cypress trees and distant foliage sway lightly in a breeze; the waterfalls in the middle distance keep falling at a steady rate in the same muted palette; the gold line along the paving and bridge trim pulses once, faintly, without brightening, spreading, or changing colour; gold appears only on the caduceus, the heraldic banners at the left wall, the brazier, and the shallow route channels; and the clouds drift very slowly while the amber sunset colour and its direction stay the same. The grounded limestone viaducts, the ravine, the city, and the heraldic banners at the left wall all stay exactly where they are and nothing new enters the frame. The camera makes one move only: a very slow steady push forward along the road toward the man and the distant city, at walking pace, so the foreground columns drift past the frame edges while the horizon never tilts and the frame stays widescreen 16:9. The shot does not cut, does not dissolve, and does not change scene. No readable lettering, captions, logos, watermarks, user interface, code, screens, borders, neon blue, cyan, magenta, vivid red, grass green, science-fiction technology, crystals, floating terrain, or cosmic sky appear at any point.

## Tool metadata
- tool: native `video_generate`
- configured provider: `nous`
- returned provider: `fal`
- model: `seedance-2.5`
- endpoint: `bytedance/seedance-2.5/image-to-video`
- job ID / seed / cost: not exposed
- source URL: https://raw.githubusercontent.com/founder-lgw-01/hermes-video-assets/main/hermes-sky-bridges-and-passages.png
- source SHA-256: `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3`
- media_id: not applicable; native tool consumes HTTPS image URL
- duration requested: 5 seconds; measured: 5.041667 seconds
- aspect requested: 16:9; returned field: empty; measured dimensions: 1280x720
- resolution: 720p; approved spec requested 1080p, but active tool schema only supports 480p/720p. Render used highest native setting without an extra paid upscale.
- audio requested: false; ffprobe confirms no audio stream
- upscale: false
- codec: H.264; frame rate: 24 fps; frame count: 121
- file: `04-video-1.mp4`; bytes: 1933971
- SHA-256: `8cf0f789cf6ac8ab263942bb15fe52014caeeffb869fa93d159b60d87f21d4c0`
- returned URL: https://v3b.fal.media/files/b/0aacfe25/heeLRBN0K5N-3Qhimbjya_video.mp4

## Findings

Inspection method: ffprobe verifies actual media properties. `video_analyze` failed because its configured analysis provider does not accept video input. Fallback: ffmpeg contact sheet at approximately 0, 1, 2, 3, and 4 seconds, inspected using `vision_analyze`. This is sampled visual review, not exhaustive frame-by-frame review.

- holds: engraved contour linework and antique print texture persist across sampled frames; no observed photorealistic/3D transition.
- holds: character build, hair and costume read remain broadly stable across samples; no major costume replacement or added trim.
- cannot see: freckles, iris colour, subtle jaw detail and fine hand anatomy cannot be verified at contact-sheet scale.
- cannot see: requested complete stride then settle is not clearly established; sampled motion reads near-static with minor weight/limb shifts. Not a verified walking cycle.
- holds: cloak/tunic/staff contours vary modestly without major transformation.
- cannot see: final cloak settle is not verified; sampled frames stop around 4 seconds.
- cannot see: requested slow forward camera push is not clearly demonstrable; slight registration shifts do not establish a dolly direction.
- holds: horizon and grounded viaduct/city geometry remain stable across samples.
- holds: existing warm gold treatment remains consistent; no observed major spread/change of colour.
- cannot see: exact single faint route pulse, waterfall motion, cloud drift and flame flicker cannot be established from sparse samples.
- holds: no new readable text, characters or objects observed in samples; original banners retained.
- holds: measured 16:9, approximately five seconds, silent output.
- drifted: output resolution is 720p rather than approved 1080p specification, due to active native tool constraint.

## Drift notes

Operator review required. Watch actual video to judge whether the subtle motion satisfies the intended stride and forward push. Do not rerender automatically. Existing still acceptance is unchanged. Verdict remains empty until operator accepts or rejects the video. Public GitHub asset remains published under its separate approval; no Cloudflare resources were created.
