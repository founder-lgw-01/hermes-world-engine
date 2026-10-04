---
set: location-probes
shot: hermes-sky-bridges-and-passages
attempt: 1
stage: 04_animate
status: approved
generated: 2026-10-03
sources:
  - 00-brief.md
  - runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md
---

# hermes-sky-bridges-and-passages, motion spec 1

## Source manifest
- Sidecar: `runs/location-probes/hermes-sky-bridges-and-passages/03-sidecar.md`, `status: draft` pending the operator's approval of this run
- Still: `runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png`
- Still sha256: `2456a2c196dea19335b28a0fbaec732c96241fab66e4d6b8f38e778ec02445b3`
- Still resolution: `1672×941`, effectively 16:9
- Render record verdict: `accepted`
- Style anchor: `world/style.md`, medium, look, exclusions, and aspect ratio are inherited unchanged from the still

## Brief
- The still: `location-probes` / `hermes-sky-bridges-and-passages`. [stated: the operator's direction, 2026-10-03]
- What moves: one completed stride and settle; chlamys trailing and lifting at
  the hem; tunic hem and belt pouches swaying behind the step; helmet and
  sandal wings quivering; the brazier at lower left flickering with a small
  moving reflection; cypress and distant foliage swaying lightly; the waterfalls
  still falling; the gold line in the paving pulsing once, faintly; clouds
  drifting very slowly. [chosen]
- The camera move: a very slow steady push forward along the road toward Hermes
  and the citadel, at walking pace, foreground columns drifting past the frame
  edges, horizon not tilting. [chosen]
- Duration: 5 seconds. [chosen; the model range is 4 to 30]
- What must not change: flat woodblock print throughout; face, jaw, build,
  proportions; undertunic and chlamys colour, no added trim; bridges grounded;
  gold confined to caduceus, banners, brazier, and shallow channels; banners
  fixed at left; no cut and no dissolve. [chosen]

### Why this still
Five images in this workspace carry `verdict: accepted`. Four were inspected
before this spec was written. This one was chosen because it is the only
accepted still that is simultaneously full-body on Hermes, mid-stride with
visible trailing fabric, and genuinely flat woodblock rather than dimensional
rendering:

| Accepted still | Character | Style read | Verdict as a first frame |
|---|---|---|---|
| **hermes-sky-bridges-and-passages** | Hermes, ~85 to 90% of frame height, mid-stride, cape trailing | flat engraved woodblock, grouped colour | **chosen** |
| hermes-gateway-risk-probe | Hermes, ~half frame height, standing, full body | flat woodblock | strong, but a static standing pose gives a video almost nothing to move |
| hermes-crystal-citadel | Hermes, ~90 to 95% of frame height, mid-stride, cape blowing right | flat engraved illustration | runner-up; reads slightly more tonally modelled |
| hermes-observatory-court | Hermes, ~three-quarters frame height, standing at an armillary sphere | **dimensional rendered realism** | rejected: the style fails at acceptance and a video will amplify it |
| hermes-aether-falls-and-islands | Hermes, ~80 to 85% of frame height, standing | **dimensional painterly realism** | rejected: same style failure |

## What moves
- **Hermes.** One stride forward, completing and settling within the shot. His
  weight moves forward rather than bracing. His expression, his gaze toward the
  citadel, and his grip on the caduceus do not change. [stated: brief; in range
  per `world/characters/hermes.md` pose and expression rows]
- **The chlamys.** Dark charcoal, trailing behind him and lifting slightly at
  the hem, then settling by the last frame. It does not change colour and gains
  no trim. [stated: brief; garment per the bible]
- **Tunic hem and belt pouches.** A small sway lagging behind the stride. [chosen]
- **Helmet wings and sandal wings.** A faint quiver. [chosen]
- **The caduceus.** Sways a few degrees with the stride and keeps its gold. It
  does not become a light source or spread glow. [chosen]
- **The brazier at lower left.** Flame flickers; a small warm reflection moves
  on the paving beside it. [chosen]
- **Vegetation.** Cypress and distant foliage sway lightly. [chosen]
- **The waterfalls.** Keep falling, at a steady rate. [chosen]
- **The gold route line.** Pulses once, faintly, along the paving and bridge
  trim. It does not brighten, spread, or change colour. [chosen]
- **The sky.** Clouds drift very slowly. The sunset's colour and direction do
  not change. [chosen]

## What holds
These are the invariants the temporal drift check is run against. Each is
copied from the bibles or is a fact the sidecar records about this still.

- **Style.** Flat woodblock line art and flat color blocking on matte aged
  parchment, for every frame. Not dimensional rendered realism at any point.
  [stated: world/style.md]
- **Face.** Angular and symmetrical, high cheekbones, strong square jaw, straight
  classical nose, clean-shaven, warm sun-baked bronze skin. The still's face is
  small; freckles, amber eye colour, nose shape, and jaw detail were accepted as
  `cannot see` at this scale, so they are guarded by saying the face stays
  exactly as the reference image rather than by describing new detail. [stated:
  sidecar, drift carried]
- **Hair.** Thick coarse curls spilling from under the winged helmet. The still
  reads brown rather than the bible's warm golden-brown with highlights; this
  is accepted drift and is held as-is, not corrected. [stated: sidecar]
- **Build.** Tall, statuesque, athletic and lean, broad defined shoulders. [stated: bible]
- **Wardrobe.** Charcoal-grey undertunic and dark-charcoal chlamys, leather
  harness and belt, bronze bracers and greaves, winged sandals, winged helmet.
  The undertunic reads slate-grey rather than charcoal-grey; accepted drift,
  held as-is. [stated: bible, sidecar]
- **Palette.** Charcoal, slate, antique sepia, ochre, bronze, and warm gold.
  No neon blue, cyan, magenta, vivid red, or grass green at any frame. [stated:
  world/style.md, palette-and-light.md]
- **Gold discipline.** Gold stays on the caduceus, the heraldic banners, the
  brazier, and the shallow carved route channels. It does not spread to the sky,
  the stone, the garments, or the water. Gold is the sole active-routing
  indicator. [stated: bible rules, brief]
- **Banners.** The heraldic caduceus/sunburst banners at the dark wall, left,
  stay present and in place. [stated: sidecar, accepted at acceptance]
- **Geography.** The viaducts stay fully grounded classical stone over solid
  ground. No floating terrain, no abyss, no energy conduits, no mechanical
  bridge structure. [stated: bible exclusions]
- **Framing.** The frame stays 16:9 and the horizon does not tilt. [stated:
  world/style.md, brief]
- **Continuity.** One continuous shot. No cut, no dissolve, no scene change. [stated: brief]

## Camera
- Duration: 5 seconds. Model range 4 to 30.
- Aspect ratio: 16:9. The still is effectively 16:9, so no reframe is needed.
- Resolution: 1080p. The still is 1672×941, so 1080p does not upscale.
- Motion: one camera move only — a very slow steady push forward along the road,
  at walking pace, toward Hermes and the citadel. The horizon does not tilt.
- Audio: not generated. This is a silent art shot, and generated audio would add
  a track the world does not own. [chosen]

## At risk
Temporal rows from `_reference/drift-checklist.md`, plus what this specific
camera move threatens.

- **A walking character.** At risk: face, proportions, limb length, gait. A
  video model animates a walk by rebuilding the legs each frame. Guard: the
  prompt says he completes one stride and settles, that his build and
  proportions are unchanged from the reference image, and that the stride's
  length does not change across the shot.
- **Trailing garment in motion.** At risk: wardrobe state, hair outline. The
  chlamys is the largest moving shape and is the first thing to gain trim or
  change colour. Guard: name it as the same dark charcoal chlamys, say it
  settles by the last frame without changing colour or gaining trim.
- **A camera push.** At risk: palette, light direction, medium, scale. A push
  is exactly how a flat illustration converts into a 3D render. Guard: say the
  medium does not change as the camera moves, that the last frame is the same
  flat woodblock print as the first, and that no dimension, smoothing, or
  rendered realism appears.
- **A camera move at all.** At risk: aspect ratio, framing horizon. Guard: say
  the frame stays 16:9 and the horizon does not tilt.
- **Route light and glow.** At risk: gold as the sole active-routing rule. Guard:
  say the gold line pulses once faintly and does not brighten or spread.
- **Duration.** At risk: world consistency. 5s is short, but the model will
  drift across it. Guard: say every element stays identical to the reference
  image for the whole shot.
- **Waterfalls and flame.** At risk: materials, palette. Guard: name the
  waterfall as falling water in the shared palette only, and the brazier as a
  small orange flame that does not grow.
- **The face the still cannot show.** At risk: the four lines accepted as
  `cannot see`. Guard: forbid invention rather than describe detail — say the
  face stays exactly as in the reference image and is not altered or made more
  detailed.
- **The accepted drift.** At risk: the slate undertunic and brown hair being
  "corrected" mid-shot, which would be a change from the first frame. Guard:
  say the clothing and hair keep the exact colours they have in the reference
  image and do not change during the shot.

## Prompt

A single continuous 5-second shot preserving exactly the flat ukiyo-e woodblock print style of the supplied reference image: bold dark contour linework, broad flat areas of unmodulated single colour, hard-edged shapes, visible aged-parchment grain, and no gradients, no volumetric shading, no atmospheric haze, no depth-of-field blur, and no rendered realism at any point, so the final frame looks like the same printed illustration as the first. The young man in the reference image completes one stride forward along the stone road and settles, his tall athletic lean body, broad shoulders, proportions, and stride length unchanged across the whole shot; his calm watchful expression and his gaze toward the distant city do not change, and his face stays exactly as in the reference image, not altered and not made more detailed. His dark charcoal chlamys trails behind him and lifts slightly at the hem, then settles by the final frame without changing colour and without gaining any trim; his tunic hem, his belt pouches, and the feathered wings on his helmet and sandals sway lightly; the gold caduceus in his hand bobs a few degrees with the step and keeps its colour without becoming a light source. All of his clothing and hair keep the exact colours they have in the reference image and do not change during the shot. The brazier flame at the lower left flickers gently and throws a small moving reflection on the paving without growing; the cypress trees and distant foliage sway lightly in a breeze; the waterfalls in the middle distance keep falling at a steady rate in the same muted palette; the gold line along the paving and bridge trim pulses once, faintly, without brightening, spreading, or changing colour; gold appears only on the caduceus, the heraldic banners at the left wall, the brazier, and the shallow route channels; and the clouds drift very slowly while the amber sunset colour and its direction stay the same. The grounded limestone viaducts, the ravine, the city, and the heraldic banners at the left wall all stay exactly where they are and nothing new enters the frame. The camera makes one move only: a very slow steady push forward along the road toward the man and the distant city, at walking pace, so the foreground columns drift past the frame edges while the horizon never tilts and the frame stays widescreen 16:9. The shot does not cut, does not dissolve, and does not change scene. No readable lettering, captions, logos, watermarks, user interface, code, screens, borders, neon blue, cyan, magenta, vivid red, grass green, science-fiction technology, crystals, floating terrain, or cosmic sky appear at any point.