---
set: processional-causeway
shot: causeway-stride
attempt: 4
stage: 02_render
status: approved
verdict: accepted
generated: 2026-10-15T13:29:23+00:00
sources:
  - runs/processional-causeway/causeway-stride/01-spec-4.md
  - runs/processional-causeway/causeway-stride/02-image-4.png
---

# causeway-stride, render 4

## Prompt as sent

Traditional Japanese woodblock-print (ukiyo-e) digital illustration on matte textured paper with an aged, speckled parchment finish, distinct carved dark-ink keyline contours, and flat opaque color blocking. A single continuous scene showing one single figure of Hermes—a tall, statuesque, athletic young adult man with broad shoulders, warm sun-baked bronze skin, a strong square jawline, straight classical nose, thick dark-brown brows, luminous amber eyes, freckles across the nose bridge and upper cheeks, and a clean-shaven face—seen in a straight-on full front view in the lower-left third of the frame striding forward along a broad ancient stone road, with calm attentive focus. Tight tousled warm golden-brown curls with sun-bleached highlights spill from under his antique-bronze winged helmet with a symmetrical pair of feathered side wings projecting outward from the left and right sides of the helmet. He wears his exact default outfit matching the supplied front-view character reference: a charcoal-grey heavy-linen knee-length undertunic with a weathered parchment-sepia hem edge, a dark-charcoal matte wool chlamys cloak pinned at one shoulder with an antique-gold clasp draping behind his shoulders, a worn brown-leather cross-body harness and belt with a brown-leather messenger pouch at his hip, and scratched antique-bronze light bracers and greaves. His legs are un-crossed and cleanly separated side-by-side in a straight-on front view with an open gap of flat limestone paving visible between his ankles, wearing weathered brown-leather sandals matching the supplied front-view footwear reference: one pale feathered wing projects outward to the left from the outer ankle of the left-side boot, one matching pale feathered wing projects outward to the right from the outer ankle of the right-side boot, and the inner ankles facing each other across the gap between his legs are completely smooth, bare brown leather and bronze with zero inner wings. His robust right hand holds his aged antique-bronze twin-serpent winged caduceus staff vertically at his side. Underfoot is the Processional Causeway: a broad road of large cracked rectangular matte limestone paving stones bordered on both sides by low weathered stone curbs with shallow unlit carved stone gutters along the inside base of each curb, fluted classical stone route markers, and creeping vines with oval and teardrop leaves, with a classical stone pavilion on a cypress-lined hill in the background. Clear dusk sky in flat stepped tones of antique sepia, slate grey, and warm amber with long hard-edged woodblock shadows; the stone roadbed and curb gutters are dormant matte limestone with no glowing lines, no gold rivers, and no light trails on the road. Framed full-body in a medium-wide 28mm view slightly below eye level in deep focus at 16:9 aspect ratio, rendered in unmodulated flat areas of opaque color and hard-edged ink lines with no gradient shading, no atmospheric haze, no depth-of-field blur, no 3D rendering, no red or blue garments, no wings between the ankles, no multiple figures, no readable lettering, no numerals, no watermarks, and no borders.

## Tool metadata

1. `model`: `gpt_image_2_5` (`variant: sunburst`) via `mcp__higgsfield__generate_image_batch` (job `a14a5b00-fcfa-4a92-b23e-5f82bb0ade09`, `0.25 credits`; conditioned on 3 single-panel front-only crops from the approved reference sheets: `bbd353f8-64b3-4ecb-93d8-2d80862eb684` (`hermes-body-turnaround.png` Panel 1 front), `d5632874-f35d-4fe9-90b4-85a24908bac8` (`hermes-sandals-turnaround.png` Panel 1 front), and `53c98173-300b-424e-b7d9-f44e55c4451f` (`hermes-props-sheet.png` Panel 1 dormant caduceus))
2. `request`: byte-for-byte match to `01-spec-4.md` **Prompt**
3. `aspect_ratio`: requested `16:9`, returned `16:9`
4. `resolution`: `1344x752`
5. `seed`: `not exposed`
6. `file`: `runs/processional-causeway/causeway-stride/02-image-4.png` (`PNG`, `2358918` bytes, `sha256:1bc5e53db713781d5a090752610a990aa9fe4c245555052f063516308d211252`)
7. `generated`: `2026-10-15T13:29:23+00:00`

## Findings

### At risk
- **Single-panel front-only reference conditioning:** `holds` — passing only Panel 1 (front view) of the body and sandal sheets prevented cross-panel front/back mixing.
- **Sandal-wing symmetry and inner-ankle clearance (front view):** `holds` — the screen-left boot has 1 pale feathered wing projecting outward to the left from its outer ankle; the screen-right boot has 1 matching pale feathered wing projecting outward to the right from its outer ankle; the inner ankles facing the gap between his legs are completely smooth and free of inner wings.
- **Roadbed and curb gutters (no glowing gold lines at still origination):** `holds` — the cracked rectangular limestone roadbed of the Processional Causeway is completely free of meandering gold rivers or light trails, with low weathered stone curbs and shallow unlit carved gutters bordering both sides of the road.
- **Woodblock-print medium and default charcoal wardrobe:** `holds` — 2D ukiyo-e woodblock print on aged speckled parchment with dark-ink keyline contours; charcoal-grey undertunic with weathered parchment-sepia hem edge and dark-charcoal chlamys with antique-gold clasp hold cleanly.

### Character (`world/characters/hermes.md`)
1. **Silhouette:** `holds` — tall, statuesque, athletic front-facing stride with winged helmet, winged sandals, billowing chlamys, and vertically carried caduceus.
2. **Face:** `holds` — angular symmetrical face, warm sun-baked bronze skin, square jawline, straight classical nose, thick dark-brown brows, luminous amber eyes, clean-shaven; `cannot see: tiny nose-bridge freckles at full-body framing`.
3. **Hair:** `holds` — short-to-medium thick curly warm golden-brown hair with lighter highlights spilling from under the helmet above the collar.
4. **Build:** `holds` — broad shoulders, athletic limbs, robust right hand gripping the caduceus.
5. **Signature features:** `holds` — none invented.
6. **Wardrobe:**
   - Antique-bronze winged helmet with symmetrical feathered side wings: `holds`.
   - Charcoal-grey heavy-linen knee-length undertunic with weathered parchment-sepia edge: `holds`.
   - Dark-charcoal wool/matte-linen chlamys with antique-gold clasp: `holds`.
   - Worn brown-leather cross-body harness, belt, and messenger pouch: `holds`.
   - Scratched antique-bronze light bracers and greaves: `holds`.
   - Weathered brown-leather sandals with pale feathered heel wings: `holds` — symmetrical outer wings projecting left and right from the outer ankles, smooth wingless inner ankles between the legs.
   - Aged gold/bronze twin-serpent winged caduceus (dormant metallic state): `holds`.
7. **Variables in range:** `holds` — calm attentive focus, front-facing stride, default wardrobe, dormant caduceus and pouch.

### Environment (`world/environment/locations/processional-causeway.md` + shared modules)
9. **Location:** `holds` — broad gently rising stone road with low stone curbs and unlit curb-base gutters on both sides, fluted route markers, creeping vines, and cracked rectangular limestone paving.
10. **Palette:** `holds` — charcoal, slate grey, and antique sepia dominant palette with warm amber dusk horizon.
11. **Materials:** `holds` — cracked limestone slabs, weathered stone curbs/markers, creeping vines, forged bronze, matte linen/wool.
12. **Light:** `holds` — dusk amber/gold horizon light and long woodblock shadows; road channels remain dormant stone in the still.
13. **Never appears:** `holds` — no neon, cyan, magenta, vivid red, grass green, sci-fi tech, crystals, floating islands, or stray road glow.
14. **Style:** `holds` — 16:9 (`1344x752`) ukiyo-e woodblock print on aged speckled parchment; no lettering, numerals, watermarks, or borders.

## Drift notes

None. Origination succeeded on the first try once conditioned on single-panel front-only reference crops (`ref_body_front.png`, `ref_sandals_front.png`, `ref_caduceus_dormant.png`) with active road glow excluded from the still prompt. Ready for operator visual review (`accept` or `drift`).
