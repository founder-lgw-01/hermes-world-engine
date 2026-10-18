---
set: gateway-pavilion
shot: hermes-pegasus-dispatch
attempt: 2
stage: 01_spec
status: approved
gate_mode: visual-only
generated: 2026-10-15T16:29:03.615144+00:00
sources:
  - runs/gateway-pavilion/hermes-pegasus-dispatch/00-brief.md
  - runs/gateway-pavilion/hermes-pegasus-dispatch/01-spec-1.md
  - runs/gateway-pavilion/hermes-pegasus-dispatch/02-render-1.md
  - world/environment.md
  - world/environment/core.md
  - world/environment/palette-and-light.md
  - world/environment/materials-and-wear.md
  - world/environment/forms-and-architecture.md
  - world/environment/locations/gateway-pavilion.md
  - world/style.md
  - world/characters/hermes.md
  - world/characters/pegasus.md
  - world/references/hermes-body-turnaround.md
  - world/references/hermes-body-turnaround.png
  - world/references/hermes-sandals-turnaround.md
  - world/references/hermes-sandals-turnaround.png
  - world/references/pegasus-body-turnaround.md
  - world/references/pegasus-body-turnaround.png
  - runs/gateway-pavilion/hermes-pegasus-dispatch/reference-crops/hermes-front.png
  - runs/gateway-pavilion/hermes-pegasus-dispatch/reference-crops/hermes-sandals-front.png
  - runs/gateway-pavilion/hermes-pegasus-dispatch/reference-crops/pegasus-right-profile-final-2.png
---

# hermes-pegasus-dispatch, spec 2

## 0. World-input manifest
| Path | Role / ID | SHA-256 |
|---|---|---|
| `runs/gateway-pavilion/hermes-pegasus-dispatch/00-brief.md` | Approved message-exchange setup brief | `e932ad53e2295bcc8f3ee93a0ae93506f87d70d3826913bd7b69e7bb5c73b046` |
| `runs/gateway-pavilion/hermes-pegasus-dispatch/01-spec-1.md` | Approved previous spec; revision provenance | `a19ec3421ce5851e158088ce0c13660a5c7e29b476e938e7f0c2af0cba0ab737` |
| `runs/gateway-pavilion/hermes-pegasus-dispatch/02-render-1.md` | Approved drift review; verdict drifted | `af01ad8a0bee93ee104beb164d6889d367ed45b031dfc89b9e3aae5dc8bdd41a` |
| `world/environment.md` | Environment index | `8b14aa19c190f8b3760811160e90ecc037d7a3079e5194f9a781d52f570f8d19` |
| `world/environment/core.md` | Shared core rules | `50c1917fa78d2fbf5757eada9859e058971e7959cdc42a919b275c2c39fcb11a` |
| `world/environment/palette-and-light.md` | Shared palette and light | `17d78431f39d55efa06fb55b9219ab31a2dbde9050140bfa863c89008d4736da` |
| `world/environment/materials-and-wear.md` | Shared materials and wear | `f90b2bd8d1cebbdc5119b9e7639a31b7b9064616df632db0f21060238be940b5` |
| `world/environment/forms-and-architecture.md` | Shared forms and architecture | `4db8eb6bef73f6658dd6152165e5136b7956520b1a2094651f915e29b9428ba5` |
| `world/environment/locations/gateway-pavilion.md` | Selected location: Gateway Pavilion | `579f67e244acebe967f0aa8991b8f3aa7010e417c83b284628e85a715044bbd0` |
| `world/style.md` | Style and camera defaults | `9032de573edefa30065f081f95ef60bd107935008c29fea21d30f6d8ca474ddc` |
| `world/characters/hermes.md` | Character bible: Hermes | `bff59cd47d8fc9cff55ad0af3049395b46910b8cdb3d4010419db0576c255d88` |
| `world/characters/pegasus.md` | Character bible: Pegasus | `510c0855caf1b14dcd210f22035157496dfe2697d717d10adf0e490b3511c868` |
| `world/references/hermes-body-turnaround.md` | #hermes-default-body-turnaround | `d1ac8bd12590851c2bcb736d71c8dd2882e90fb1bbc877a2b99dee3da8a32579` |
| `world/references/hermes-body-turnaround.png` | Approved source sheet: Panel 1 front | `a8d93020d3c56a4a5e37ef40c50abb8af87c4138fecd12af26d8e39b132b875e` |
| `world/references/hermes-sandals-turnaround.md` | #hermes-sandals-4-view | `1532758ea4aa24c7b0f40ab0584ec193df02b845f33db1d54184a03e364f33fa` |
| `world/references/hermes-sandals-turnaround.png` | Approved source sheet: Panel 1 front pair | `7bddb1f10633ec5e049d7ba1e3b96c42961cfca05583111f6c0681ffe27510dc` |
| `world/references/pegasus-body-turnaround.md` | #pegasus-default-body-turnaround | `a7f1940c68730586cdae805cf53c4141f7cbeceb81d55af6c5a2b6bafdb88aec` |
| `world/references/pegasus-body-turnaround.png` | Approved source sheet: Panel 3 right profile | `8cc2ca79b6323b2d1ea45645481fb2dd4ac2fb71d9a0bc49e8b0d5ea698e4b5d` |
| `runs/gateway-pavilion/hermes-pegasus-dispatch/reference-crops/hermes-front.png` | Actual conditioning image 1: crop [45,5,332,742] | `a69735884d78e7e8c872421140eab7f272697f8df630ce9628aebcab04bc2320` |
| `runs/gateway-pavilion/hermes-pegasus-dispatch/reference-crops/hermes-sandals-front.png` | Actual conditioning image 2: crop [20,70,362,640] | `57f0d68762fbcfb6d0e5167d165ef35234b2209f940a4116c1494e0581960405` |
| `runs/gateway-pavilion/hermes-pegasus-dispatch/reference-crops/pegasus-right-profile-final-2.png` | Actual conditioning image 3: crop [662,50,1062,675], margin-only cleanup | `05c0a4ec032bfb8bb16b8f17c64ac23521a60ffd992689f719747aee7c38cfc1` |

### Conditioning provenance
- Pass the three **actual conditioning images** above, never full multi-view sheets. All three selected crops were visually inspected before this spec was derived.
- Hermes body: source-space `[45,5,332,742]`, `287x737`; front view with two outer sandal wings and wingless inner ankles.
- Hermes footwear: source-space `[20,70,362,640]`, `342x570`; front matched pair, two outer wings total and wingless inner ankles.
- Pegasus: source-space `[662,50,1062,675]`, `400x625`; right-profile Panel 3. Remove only the adjacent panel's isolated wingtip in crop-space `[390,0,400,215]`, using blank original-sheet top border `[600,0,815,10]` rotated 90 degrees. No target anatomy, tack or pose is changed. Use `pegasus-right-profile-final-2.png`; earlier raw/cleanup trials are not generation inputs.
- Crops are run-local derivatives authorized by the approved reference-permission records, not new world canon. No write into `world/`.

## 1. Brief
- **Characters:** `hermes` and `pegasus`, using the approved bibles above.
- **Action:** preserve `00-brief.md`: Hermes stands front-facing in the left-center foreground with his left hand lightly near Pegasus's shoulder; Pegasus stands on the right in right-facing profile with raised wings and loaded folder saddlebags. Message-exchange identifies this loaded pre-exchange setup; no completed unloading/loading is added to the approved still brief.
- **Pose/expression:** Hermes's uncrossed front-facing legs are separated with clear stone between inner ankles; calm reassuring confidence, right hand holding the dormant caduceus vertically. Pegasus: calm noble alertness, upright arched neck, four grounded hooves, withers at Hermes's chest-to-shoulder height, head/upright ears above the whole winged helmet.
- **Wardrobe:** Hermes `default`, dormant antique-bronze caduceus; Pegasus `default`, energetic warm-gold Nordic/Viking saddle/chest band and worn brown-leather saddlebags loaded with cord-bound parchment folders.
- **Location:** Gateway Pavilion, `world/environment/locations/gateway-pavilion.md`.
- **Time/weather:** clear dusk, warm golden-amber distant-horizon sunlight, crisp long woodblock shadows.
- **Camera:** wide/medium-wide full-body two-shot, 16:9, 28mm full-frame equivalent, slightly below eye level, deep focus; both figures complete with helmet/wing headroom.
- **Revision:** previous approved review has `verdict: drifted`: extra inner wing on screen-right sandal; Pegasus head/ears below the helmet. Re-derive this attempt from the brief and these findings, not an appended old prompt.
- **Authorization:** Jordan's current request, “Using gate_mode: visual-only and single-panel reference crops from world/references/, let's build and render 01-spec-2.md”, authorizes intermediate Markdown approval and one requested render. No publication, animation, automatic rerender or future visual acceptance. Jordan retains the visual verdict.

## 2. Characters in frame
### Hermes — selected literal bible invariants
Source: `world/characters/hermes.md`. Wording is preserved; only heading depth is adapted.

#### Silhouette
- Height band: Tall and statuesque. [stated: interview q24]
- Build: Athletic/lean heroic figure. [stated: interview q31]
- Posture: Weightless, aerodynamic, and forward-moving; striding, bounding, or flying rather than flat-footed. [stated: interview q21]
- Hair outline: Short-to-medium curls spill from under headwear. [stated: interview q23]
- Clothing outline: Winged headwear and sandals, vertically carried caduceus, and shoulder-fastened chlamys billowing in motion. [stated: interview q21]

#### Face
- Shape: Angular, highly symmetrical, and high-cheekboned. [stated: interview q22]
- Skin tone: Warm sun-baked bronze. [stated: interview q22]
- Eyes (color, shape, spacing): Luminous amber/golden-orange eyes with piercing focused gaze; shape/spacing are unknown. [stated: interview q22]
- Brows: Thick dark-brown brows, relatively straight with a subtle arch. [stated: interview q22]
- Nose: Straight classical nose with narrow defined bridge and proportional tip. [stated: interview q22]
- Mouth: Full defined neutral lips with a distinct cupid’s bow and muted pink tone. [stated: interview q22]
- Jaw: Strong square jawline. [stated: interview q22]
- Ears: Unknown because helmet side pieces and curls obscure them. [stated: interview q22]
- Marks: Freckles across the nose bridge and upper cheeks; no visible scars or prominent moles. [stated: interview q22]

#### Hair
- Color: Warm golden-brown with lighter sun-bleached highlights. [stated: interview q23]
- Length: Short to medium, above the collar. [stated: interview q23]
- Texture: Thick, coarse, and highly curly. [stated: interview q23]
- Cut: Layered, wild, and naturally unkempt. [stated: interview q23]
- How it falls: Tight tousled curls spill from under the helmet across forehead, temples, and ears. [stated: interview q23]
- Facial hair: Clean-shaven. [stated: interview q23; interview q31]

#### Build
- Height against each other character, by name: Unknown until another character is added. [stated: interview q24]
- Shoulders: Broad and defined. [stated: interview q24]
- Limb length: Athletic, powerful, defined limbs; exact proportion is unknown. [stated: interview q24]
- Weight: Substantial lean weight; exact weight is unknown. [stated: interview q24]
- Hands: Large, robust hands capable of a firm caduceus grip. [stated: interview q24]

#### Signature features
1. Not specified while Hermes is the only character; do not invent a cross-state signature feature. [stated: interview q25]
2. Not specified while Hermes is the only character; do not invent a cross-state signature feature. [stated: interview q25]
3. Not specified while Hermes is the only character; do not invent a cross-state signature feature. [stated: interview q25]

#### Wardrobe
Default outfit, garment by garment, color and material:
- Antique-bronze winged helmet with integrated feathered side wings. [stated: interview q26]
- Charcoal-grey heavy-linen, knee-length undertunic with weathered parchment-sepia edge. [stated: interview q26]
- Dark-charcoal wool or matte-linen chlamys, pinned at one shoulder with an antique-gold clasp. [stated: interview q26]
- Worn brown-leather cross-body harness and belt. [stated: interview q26]
- Scratched antique-bronze light bracers and greaves. [stated: interview q26]
- Weathered brown-leather sandals with pale feathered heel wings. [stated: interview q26]
- Aged gold/bronze twin-serpent winged caduceus, with warm-gold activation only during routing or gateway work. [stated: interview q26]

#### Shot variables and reference clarification
- Screen-left, front view, calm reassuring confidence, left hand near Pegasus's shoulder, right hand holding dormant vertical staff. Default outfit; allowed messenger pouch.
- Approved reference permissions specify one outer heel wing per sandal, wingless inner ankles. In this orthographic stance the far screen-left wing points toward the left frame edge and far screen-right wing toward the right edge; avoid anatomical-left/right ambiguity.
- Relative height uses the later approved Pegasus bible's named relationship; Hermes's historical unknown relative-height line does not override it.
- Freckles/iris details may be too small in wide framing; mark `cannot see` rather than claim verification.

### Pegasus — selected literal bible invariants
Source: `world/characters/pegasus.md`. Wording is preserved; only heading depth is adapted.

#### Silhouette
- Height band: Tall prime-adult winged stallion — withers (shoulder) at roughly chest-to-shoulder height on `hermes` (~15.2–16 hands), with head and upright ears rising above `hermes` when standing and a spread wingspan ~2.5–3x `hermes`’s height `[stated: interview q66]`
- Build: Deep muscular chest and shoulders, strong arched neck, lean athletic barrel, and slender tapering legs ending in dark hooves `[stated: pegasus-flight.png, interview q63, q66]`
- Posture: Noble, alert, and poised—either grounded with arched neck and pricked ears or rising/soaring in balanced aerial stride `[stated: pegasus-flight.png, interview q63, q71]`
- Hair outline: Soft loose mane strands along the upper neck crest, short wispy forelock between upright ears, and a full flowing tail reaching the hocks `[stated: pegasus-flight.png, interview q65]`
- Clothing outline: Massive shoulder-mounted multi-tiered feathered wings sweeping upward and outward from the withers, with a low-profile embroidered Viking tribal-tattooed saddle of golden energetic light and worn brown-leather folder saddlebags resting across the back and flanks in `default` state (`bare` state has no tack outline) `[stated: pegasus-flight.png, interview q63, q68, q69]`

#### Face
- Shape: Long, sculpted classical equine head with a straight facial profile and narrow nasal bridge `[stated: pegasus-flight.png, interview q64]`
- Skin tone: Pure white to pale parchment-silver coat over the head, transitioning to a dark slate-charcoal skin tone on the rounded muzzle `[stated: pegasus-flight.png, interview q64]`
- Eyes (color, shape, spacing): Small dark-brown/obsidian equine eyes set high and wide on the sides of the head `[stated: pegasus-flight.png, interview q64]`
- Brows: Subtle sculpted equine supraorbital brow ridges `[stated: pegasus-flight.png, interview q64]`
- Nose: Narrow straight nasal bridge ending in a rounded dark slate-charcoal muzzle with clearly defined dark nostrils `[stated: pegasus-flight.png, interview q64]`
- Mouth: Closed, composed dark slate-charcoal equine lips and chin, unbitted in `bare` state `[stated: pegasus-flight.png, interview q64]`
- Jaw: Cleanly modeled classical equine cheek and mandible without heavy draft-horse bulk `[stated: pegasus-flight.png, interview q64]`
- Ears: Upright, symmetrically pointed equine ears attentive to the route `[stated: pegasus-flight.png, interview q64]`
- Marks: None—pure white/pale silver-grey facial coat with dark slate-charcoal muzzle; heavy dark shading on viewer-right of `pegasus-flight.png` is directional shadow, not a permanent blaze, patch, or scar `[stated: pegasus-flight.png, interview q64, q73]`

#### Hair
- Color: Pure white to pale silver-grey mane, forelock, and tail `[stated: pegasus-flight.png, interview q65]`
- Length: Short wispy forelock, medium-length neck mane, and full hock-length tail `[stated: pegasus-flight.png, interview q65]`
- Texture: Soft, fine, wind-lifted equine hair rendered in grouped woodblock-print strand masses `[stated: pegasus-flight.png, interview q11, q65]`
- Cut: Natural, unbraided, and uncropped `[stated: pegasus-flight.png, interview q65]`
- How it falls: Forelock wisps lightly over the upper forehead; mane parts and lifts loosely along the arched neck crest; tail flows cleanly behind the croup down to the hocks `[stated: pegasus-flight.png, interview q65]`
- Facial hair: Clean equine muzzle with no heavy fetlock feathering or draft-horse bearding `[stated: pegasus-flight.png, interview q64]`

#### Build
- Height against each other character, by name: Withers (shoulder) sit at roughly chest-to-shoulder height on `hermes` (~15.2–16 hands), while Pegasus’s head and upright ears rise above `hermes`’s winged helmet when standing side by side; spread wingspan reaches ~2.5–3x `hermes`’s standing height `[stated: interview q66]`
- Shoulders: Broad, deep, powerfully muscled equine chest and withers engineered to anchor the massive wing roots `[stated: pegasus-flight.png, interview q66]`
- Limb length: Long, slender, tapering equine forelegs and hindlegs with clean cannon bones and pasterns `[stated: pegasus-flight.png, interview q66]`
- Weight: Substantial lean athletic stallion mass balanced for effortless aerial lift `[stated: pegasus-flight.png, interview q66]`
- Hands: Equine hooves—four compact, well-formed dark charcoal-grey to black hooves (no cloven hooves, paws, or talons) `[stated: pegasus-flight.png, interview q66]`

#### Signature features
1. Massive shoulder-mounted multi-tiered feathered wings (long outer primary flight feathers with two or more graduated inner rows of coverts in white and pale silver-grey) `[stated: pegasus-flight.png, interview q67]`
2. Pure white / pale parchment-silver coat contrasted with a dark slate-charcoal muzzle and four dark charcoal-grey hooves `[stated: pegasus-flight.png, interview q67]`
3. Embroidered Viking tribal-tattooed saddle appearing as golden energetic light across the back, paired with worn brown-leather saddlebags sized to carry Hermes’s cord-bound folders `[stated: interview q67, q68]`

#### Wardrobe
Default outfit, garment by garment, color and material:
- `default`:
  - Saddle: Embroidered Viking tribal-tattooed saddle across the back and upper flanks whose intricate knotwork and tribal motifs appear as luminous warm-gold energetic light (`#f8cc62` / `#e8ac48` in the world palette) `[stated: interview q4, q68]`
  - Saddlebags: Worn brown-leather dispatch saddlebags resting on both flanks behind the wing roots, structured to hold Hermes’s rectilinear cord-bound parchment folders and codices `[stated: interview q68, q72]`
  - Head/neck: Unbitted or minimal warm-gold energetic knotwork throat/chest band integrated with the saddle so the head and dark muzzle remain clean `[stated: pegasus-flight.png, interview q68, q69]`

#### Shot variables
- Screen-right, right-facing profile, default loaded tack, calm noble alertness, four hooves grounded, both shoulder wings raised.
- Upright arched neck puts head and ears above the entire helmet including feather tips. Shared ground line, no perspective shrinkage.
- Far-side saddlebag and wing attachment may be naturally occluded; do not force a second bag across the near flank.
- No new exact cargo count or lid-state is invented; preserve the approved loaded brief.

## 3. Scene
- Classical Gateway Pavilion: heavy stone pediment with intricate celestial-pattern carvings, fluted columns, classical gateway architecture; immediate structure is important. No invented connected routes or exact portal placement.
- Massive weathered rectangular limestone blocks, aged mechanical fractures, creeping vines and wear. Matte stone in charcoal/slate/antique-sepia; worn brown leather, scratched/patinated antique bronze, aged parchment folders.
- Clear dusk, distant-horizon amber/orange/gold sunlight and long hard-edged print shadows. Natural dusk gold is not a second active routing effect.
- Selected saddle/chest band alone is active warm gold; no tint spread to skin/coat/paving. Caduceus and ground remain dormant; no ground-energy river.
- Digital illustration with traditional Japanese woodblock-print (ukiyo-e) stylization, distinct line art, and flat color blocking. Matte textured paper with an aged, speckled parchment background and vintage/antiqued character. Flat opaque unmodulated planes, carved keylines, stepped tones; no gradients, modeled volume, painterly realism, photographic lighting/haze/blur or 3D.
- One man, one horse, no duplicated panels/extra limbs/wings. No readable text, numerals, logos, watermarks, borders, collage, UI, futuristic devices/materials, crystals, floating terrain, modern tack, metal bit, stirrup irons or forbidden vivid colors. Default charcoal clothes, not ceremonial red.

## 4. Camera
- Brief-specified: 28mm full-frame equivalent, slightly below eye level, wide/medium-wide full-body two-shot, deep focus, 16:9.
- Left-center Hermes and right Pegasus stand on the same level terrace. Retain head-to-toe / hoof-to-wingtip, headroom and pavilion context. No face-microdetail verification promise at this scale.
- Match frontal Hermes and right-profile Pegasus crops; no twisted pelvis or crossed/overlapping ankles.
- Native parameter `aspect_ratio: landscape`; 16:9 also in prompt. Record actual returned dimensions and any omitted aspect setting literally; do not equate a ratio label with exact pixel geometry.

## 5. At risk
| Threat | Invariant / prior drift | Guard in prompt, conditioning and review |
|---|---|---|
| Paired footwear | Two outer heel wings; screen-right had a third inner wing | Exactly two total at far screen-left/right outer heels, smooth inner straps and clear featherless gap; dedicated frontal footwear crop; mandatory ankle-region review. |
| Relative scale | Pegasus head/ears were below helmet | Same ground line, no distance shrinkage, high upright arched neck, head/ears above entire helmet including feather tips. Do not substitute wing height for head height. |
| Sheet leakage | One figure per named character | Three single-panel crops; one continuous narrative scene, no sheets/collage/panel divisions. |
| Profile anatomy | Straight nasal bridge, dark muzzle, four dark hooves, tiered shoulder wings | Explicit equine profile/coat contrast and four distinct hooves; right-profile reference; inspect wing roots separately from feather layers. |
| Tack / feature swapping | Nordic energetic saddle, brown loaded bags; staff/pouch on Hermes only | Explicit individual assignments and loaded cord-bound folders, no modern tack/bit/stirrups; record far-side occlusion honestly. |
| Wide full bodies | Proportions, hands, extremity cropping, small face | Tall lean broad-shouldered man, muscular athletic stallion, complete figures and wingtips. Freckles/irises `cannot see` if unresolved. |
| Dusk / active gold | Bronze skin, pale coat, charcoal cloth; localized energetic gold | Flat long dusk shadows, gold confined to tack, dormant caduceus/stone, no tint spill. |
| Global medium | Ukiyo-e, flat planes, keylines, matte parchment | Literal medium anchor and positive unmodulated-plane grammar; exclude gradients, modeled volume, painterly/photo/3D effects. |

## 6. Prompt
Digital illustration with traditional Japanese woodblock-print (ukiyo-e) stylization, distinct line art, and flat color blocking. Matte textured paper with an aged, speckled parchment background and vintage/antiqued character. A single continuous narrative scene, not a reference sheet, showing exactly one Hermes on the left and one Pegasus on the right, fully visible on the same level stone terrace. The man is tall, statuesque, lean and athletic, with broad shoulders, large robust hands, warm sun-baked bronze skin, a square jaw, straight classical nose, thick dark-brown brows, amber-golden eyes, freckles across nose and upper cheeks, and a clean-shaven face. Short warm golden-brown tight curls spill from an antique-bronze helmet with exactly two feathered side wings. He faces the viewer straight on with calm reassuring confidence, wearing a charcoal-grey heavy-linen knee-length undertunic with weathered parchment-sepia edging, dark-charcoal matte chlamys pinned at one shoulder with an antique-gold clasp, worn brown-leather cross-body harness and belt with a messenger pouch, and scratched antique-bronze bracers and greaves. His right hand holds a dormant aged-bronze twin-serpent winged caduceus upright at his side; his left hand rests lightly near the horse's shoulder. Match the supplied frontal body and footwear images. Both feet face directly toward the viewer, uncrossed and clearly separated. There are exactly two pale feathered sandal wings in total: one attached to the far screen-left outer heel, projecting toward the left frame edge, and one attached to the far screen-right outer heel, projecting toward the right frame edge. Both inward-facing ankles have only smooth brown-leather straps; the entire stone gap between the ankles is clear and contains no feathers, no small inner wing, and no third sandal wing.

The winged stallion matches the single supplied right-facing profile: pure white to pale parchment-silver coat, a long classical equine head with straight narrow nasal bridge, dark slate-charcoal muzzle and nostrils, small dark obsidian equine eyes, upright pointed ears, loose white-silver neck mane and short forelock, full hock-length flowing tail, deep muscular chest, athletic barrel and slender tapering legs with four distinct dark charcoal hooves. It stands immediately beside the man on the same ground line, not behind him or farther away. Its withers reach the man's upper chest to shoulder; its arched neck is held tall and upright, keeping a clean right-facing profile, so its head and pointed ears rise clearly ABOVE THE TOP OF THE MAN'S ENTIRE WINGED HELMET, including the helmet feather tips. A massive pair of shoulder-mounted, multi-tiered white and pale-silver feathered wings rises above its back, with long outer primaries and graduated inner coverts; all wingtips remain inside the frame. Its low-profile embroidered Viking/Nordic knotwork saddle and integrated chest band appear as warm-gold energetic light, confined to the tack without tinting skin, coat or paving. Worn brown-leather dispatch saddlebags rest behind the wing roots and carry rectilinear cord-bound parchment folders. This is a calm loaded pre-exchange setup, not a completed unloading or transfer.

The Gateway Pavilion surrounds them with classical fluted stone columns and a heavy triangular stone pediment bearing intricate celestial-pattern carvings, creeping vines and aged fractured stone. Underfoot are massive weathered rectangular limestone blocks in matte charcoal, slate-grey and antique-sepia tones, with no glowing ground lines. Clear dusk sunlight comes from the distant horizon in amber, orange and gold, with long hard-edged woodblock shadow shapes. A wide/medium-wide full-body two-shot, 28mm full-frame equivalent, slightly below eye level, deep focus, showing the man head-to-toe and the horse hoof-to-wingtip with clear headroom. The image uses unmodulated flat opaque color planes, carved dark-ink keyline contours and stepped tones, not smooth gradients, modeled volume, painterly realism, photographic lighting, volumetric haze, depth-of-field blur or 3D rendering. There are no extra figures, no extra limbs or wings, no modern tack, no metal bit or stirrup irons, no vivid red garments, no neon blue, cyan, magenta, grass green, crystals, floating terrain, futuristic devices, readable lettering, numerals, logos, watermark, border, collage or panel divisions. Wide 16:9 composition.
