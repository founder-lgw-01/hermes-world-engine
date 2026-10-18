---
set: gateway-pavilion
shot: hermes-pegasus-dispatch
attempt: 3
stage: 02_render
status: approved
verdict: accepted
gate_mode: visual-only
generated: 2026-10-16T01:47:29.634234+00:00
sources:
  - runs/gateway-pavilion/hermes-pegasus-dispatch/01-spec-3.md
  - runs/gateway-pavilion/hermes-pegasus-dispatch/02-image-3.png
  - runs/gateway-pavilion/hermes-pegasus-dispatch/02-tool-3.json
---

# hermes-pegasus-dispatch, render 3

## Prompt as sent

Digital illustration with traditional Japanese woodblock-print (ukiyo-e) stylization, distinct line art, and flat color blocking. Matte textured paper with an aged, speckled parchment background and vintage/antiqued character. One continuous narrative scene, not a sheet or collage. On the left stands one Hermes, a tall lean athletic young adult man with broad shoulders, warm bronze skin, angular high cheekbones, square jaw, straight classical nose, thick dark-brown brows, amber eyes, freckles across nose and upper cheeks, and a clean-shaven face. Short tight golden-brown curls emerge beneath an antique-bronze helmet with two pale feathered side wings. His expression is calmly reassuring. He wears a charcoal-grey knee-length linen undertunic with parchment-sepia edging, a dark-charcoal matte chlamys fastened at one shoulder with a gold clasp, worn brown-leather crossed harness and belt with a messenger pouch, two antique-bronze bracers and two greaves. His right hand holds the dormant bronze twin-serpent winged caduceus vertically at his side; his left hand rests lightly near his companion's shoulder. Match the frontal body and footwear references: torso, knees and feet face straight toward the viewer, feet uncrossed and separated. Exactly two pale sandal wings in total: one on the far screen-left outer heel pointing outward toward the left frame edge, one on the far screen-right outer heel pointing outward toward the right edge. Both inward-facing ankles have smooth brown leather straps and no feathers; clear stone is visible throughout the gap between the ankles.

On the right stands one Pegasus in a clean right-facing profile, a prime-adult athletic white-to-pale-silver winged stallion with a deep chest, strong arched upright neck, long straight equine facial profile, dark slate-charcoal muzzle and nostrils, small dark eyes, pointed attentive ears, loose pale mane and forelock, flowing hock-length tail, slender tapering legs and four compact dark hooves. Both figures stand on the same level terrace: the horse's withers reach the man's upper chest to shoulder, and its upright poll and ear tips rise above the man's winged helmet. Preserve natural equine proportions. Two massive shoulder-mounted feathered wings rise and spread above its back, drawn in grouped rows of pale coverts and long primaries. Across its back and chest is an embroidered Viking/Nordic knotwork saddle and integrated band made visibly of self-illuminated warm-gold energetic light: pale-gold center strokes inside crisp amber-gold outlines remain bright even on the shadow side, not brown-gold embossed metal or ordinary reflected highlights. This light stays confined to the knotwork; it does not tint skin, white coat, leather bags or paving and has no photographic bloom. Worn brown-leather dispatch saddlebags behind the wing roots carry rectilinear cord-bound parchment folders. It holds calmly steady beside the man; no completed folder transfer is depicted.

The Gateway Pavilion is a classical stone colonnade with a heavy triangular pediment and celestial-pattern reliefs, a few carved crack and vine marks, and large rectangular limestone paving blocks in charcoal, slate-grey and antique sepia. Clear dusk sunlight from the distant horizon forms sharply stepped amber/orange/gold sky bands and long crisp shadow shapes. The staff and stone paving are unlit; there are no glowing ground lines. A 28mm wide/medium-wide full-body two-shot, slightly below eye level, deep focus, in a wide 16:9 composition. Both complete figures fit with open stone below every foot and hoof, side space around the muzzle, tail and staff, and a clearly visible band of sky separating EVERY raised wingtip from the top frame edge. Make the entire scene a two-dimensional woodblock design: broad unmodulated flat opaque color shapes, sparse carved dark-ink keylines, grouped feathers and hard-edged stepped tones. No dense crosshatching, etched modeled shading, smooth gradients, painterly rendering, photographic lighting, volumetric haze, blur or 3D volume. No extra figures, extra limbs, extra wings, modern tack, metal bits, stirrup irons, neon blue, cyan, magenta, vivid red clothes, grass green, crystals, floating terrain, futuristic devices, readable lettering, numerals, logos, watermarks, borders or panel divisions.

## Tool metadata

1. `model`: returned `openai/gpt-image-2.5-sunburst`; `provider: openrouter`; `endpoint: images` through native Hermes `image_generate` and the enabled default-profile adapter. No Nous/Higgsfield substitution. Request/job ID and provider-side generation ID: `not exposed`.
2. `request`: byte-for-byte approved spec **Prompt**, `4326` characters, `sha256:214ea38dde58c7b9f444ec6fe5024956e7738bae71c675ebafaa86e8022e0a7c`. Frozen spec `sha256:9347c42265f46c44de3017de1be2f44b1e77827e3c7c15d76af19c95b4d229e6`; all 22 manifest hashes and required Markdown approvals passed before submission. Returned tool prompt is retained in `02-tool-3.json`. Exactly three pose-matched local reference crops were passed, no base image; returned `reference_images_used: 3`, `modality: image`.
3. `aspect_ratio`: requested native `landscape`; returned `aspect_ratio: landscape`, `exact_aspect_ratio: 16:9`; actual decoded raster `1536x864`, and `width * 9 == height * 16` is true. The repaired adapter's exact ratio was exercised by a real render; no aspect omission warning returned.
4. `resolution`: actual `1536x864`. Quality, pixel size, resolution tier, seed and image-count overrides were not set; no high/xhigh/max tier, extra image, paid upscale or post-crop was added. Provider-selected quality/tier: `not exposed`.
5. `seed`: `not exposed`.
6. `file`: `runs/gateway-pavilion/hermes-pegasus-dispatch/02-image-3.png`, decoded `PNG`, `2968263` bytes, `sha256:41b092435c14d6302a3b1881f6b2ac2df679a01dfda8c8f7bb725b485c2ad70f`. Pillow integrity check passed; saved copy SHA-256 exactly matches native cache output `/opt/data/cache/generated/images/openrouter_openai_gpt-image-2_5-sunburst_20261015_184705_92fdab4d.png`.
7. `generated`: provider-side generation/completion timestamp `not exposed`. Cache file modification time converted to UTC: `2026-10-16T01:47:05.218271+00:00`; artifact observed/copied/validated: `2026-10-16T01:47:29.634234+00:00` (frontmatter record time, not an invented provider generation timestamp).

### Spend, route and review receipts
- Explicit approval: Jordan's “next step approved,” following the offered build of spec 3 and one OpenRouter render, under the existing visual-only gate. One real image request submitted; no billable probe, automatic retry or fallback.
- Native selected route has no cost-quote capability; disclosed before submission. Actual returned usage reports `cost_usd: 0.050794`, `total_tokens: 3732`. This is provider-reported usage cost, not a separately reconciled account debit. No Higgsfield quote is borrowed for this request.
- Native dispatch was non-billably checked before rendering: profile-local adapter, correct pinned model, landscape → 16:9 and no quality/size default changes. Returned live metadata now confirms OpenRouter / Sunburst / images, three references and exact 16:9.
- Reference images are the exact three frozen run-local derivatives in the spec, not full sheets and not the previous rendered image. No new upload/public hosting was required for the native local-path inputs.
- Review: full frame; ankle `[330,690,605,850]`; complete head comparison `[350,60,1290,370]`; tack/contact `[600,250,1180,610]`; original-top clearance `[500,0,1140,300]`; contextual medium `[250,230,1280,735]`; legs/hooves `[600,645,1190,855]`; Hermes identity/contact context `[250,100,850,675]`.
- Prior-review correction: attempt 2's head-height and clipping statements were overstated or unresolved on contextual reinspection. Spec 3 records that correction without rewriting the previous generated body; this render is judged against actual landmarks rather than inheriting those assertions.

## Findings

### At risk — image evidence, before character details
- **Global visual grammar:** `holds` for broad flat color areas, firm ink contours, matte parchment and stepped landscape shapes. `drifted: localized modeled gray shading remains on the muzzle/neck/belly/legs, arms/knees and guards; the tunic retains dense fold/hatch strokes.` Full frame plus `[250,230,1280,735]` distinguish those local departures from allowed feather outlines and paper grain; the whole image is not described as photographic or uniformly densely engraved.
- **Energetic gold tack:** `drifted: gold knotwork is present but reads as ordinary flat golden ornament rather than clearly self-lit light-shaped center strokes.` `[600,250,1180,610]` assesses this within the flat-print medium without requiring photographic bloom. No emitted-light state is confirmed merely from its gold color.
- **Head relationship:** `holds` for upright ear tips above Hermes's topmost helmet wings. `cannot see: the poll appears approximately level with or slightly below those tips, so the stronger requested poll-clearance is not established.` Both complete heads and helmet/ear tips are retained in `[350,60,1290,370]`; the horse's low muzzle is not used as a height-failure test.
- **Withers scale:** `cannot see: the near wing and tack obscure the withers contour.` Do not assert chest/shoulder height from a hidden landmark. Hooves occupy a common paved terrace plane; this does not independently prove withers height.
- **Full-wing frame clearance:** `holds` — the highest upper feather outlines are around original y=52, with visible original-frame clearance in `[500,0,1140,300]`; they are not cropped by the delivered top edge. `drifted: the requested open-sky band above all tips is not present; pediment/stone reliefs fill the gap.` Architectural overlap behind the wing is not anatomical clipping.
- **Paired sandal wings:** `holds` — mandatory dedicated crop `[330,690,605,850]` resolves exactly one pale wing on the outer screen-left heel and one on the outer screen-right heel; inner ankles have brown straps and no extra feathers. Two outer wings total, no third inner wing.
- **Profile anatomy / hoof count:** `holds` — one right-facing equine head with dark muzzle and four separate tapering legs ending in compact dark hooves on stone, checked in `[600,645,1190,855]`. `cannot see: both complete wing roots/far wing geometry are not independently established behind the near layered wing.`
- **Conditioning / figure count:** `holds` — one frontal Hermes and one right-profile Pegasus, no multi-view sheet layout or duplicate figures. Returned native tool metadata explicitly reports three references used.
- **Skin, wardrobe and local palette:** `holds` for bronze skin, charcoal/grey default clothes, brown leather, bronze guards and pale coat. `drifted: Hermes's hair reads very dark brown/black rather than the bible's warm golden-brown with sun-bleached highlights`, confirmed in contextual identity crop `[250,100,850,675]`.
- **Small faces / hidden details:** `cannot see: exact irises, freckles, fine lip shape and far-side tack cannot be reliably checked at this scale.` Preserve those limits instead of claiming all face invariants hold.
- **API / raster geometry:** `holds` — actual returned provider/model/endpoint are `openrouter` / `openai/gpt-image-2.5-sunburst` / `images`; returned `exact_aspect_ratio: 16:9`; decoded PNG is `1536x864` and satisfies `width * 9 == height * 16`. No corrective crop, resize or retouch.

### Hermes — bible checklist, top to bottom
1. **Silhouette:** `holds` — tall/athletic frontal figure, broad shoulders, visible curly hair, winged helmet/sandals, chlamys and upright staff. Stationary stance follows the approved brief and threshold pose range; it is not a new traversal action.
2. **Face shape / skin / jaw:** `holds` — warm bronze skin, angular fairly square jaw, clean-shaven face in `[250,100,850,675]`. `cannot see: exact symmetry and cheekbone microstructure are not established.`
3. **Eyes / brows:** `cannot see: precise luminous amber iris color, eye spacing and fine brow shape are not resolved`; canonically unknown eye spacing is not invented.
4. **Nose / mouth:** `holds` for a straight classical nose at coarse scale; `cannot see: precise tip/bridge proportions, cupid's bow, muted lip color and full lip shape are too small.`
5. **Ears / marks:** `cannot see: helmet/curls hide ear form, and freckles or tiny scars/moles cannot be checked.` Ear shape is canonically unknown; no new marks are invented.
6. **Hair color:** `drifted: curls read very dark brown/black, not visibly warm golden-brown with sun-bleached highlights.`
7. **Hair form / facial hair:** `holds` — short curly hair beneath helmet and clean-shaven presentation; `cannot see: coarse strand texture and exact rear fall/highlight pattern are not resolved.`
8. **Build:** `holds` for broad defined shoulders and lean athletic limbs; `cannot see: exact hand size, finger anatomy and detailed limb proportions are not established.` No invented weight or precise dimensions.
9. **Signature list:** the bible intentionally specifies no cross-state signature set. No additional signature invariant is invented; recognizable garments/props are checked below.
10. **Helmet:** `holds` — bronze helmet with two visible feathered side wings in the focused identity crop; `cannot see: exact integration and wear microdetail are unresolved.`
11. **Tunic:** `holds` — charcoal-grey knee-length tunic with sepia edge. `drifted` on dense local fold/hatch texture versus this attempt's unmodulated-flat-fill guard; garment identity itself remains intact.
12. **Chlamys / clasp:** `holds` — dark matte cloak with gold shoulder clasp, no ceremonial red. `cannot see: exact wool-versus-linen weave cannot be identified.`
13. **Harness / belt / pouch:** `holds` — brown crossed harness, belt and allowed brown hip pouch.
14. **Bracers / greaves:** `holds` — bronze forearm guards and paired bronze greaves; `cannot see: exact scratch and patina details are not independently verifiable.`
15. **Sandals:** `holds` — brown straps, open toes and exactly one pale outer heel wing per sandal, inner ankles wingless, confirmed by dedicated ankle crop.
16. **Caduceus:** `holds` — staff on screen-left held upright, twin winding snakes and winged top resolved in `[250,100,850,675]`; no visible activation glow and no replacement weapon.
17. **Expression / interaction:** `holds` — calm attentive/reassuring expression, free arm extended to light contact near the horse's upper body/wing. `cannot see: exact shoulder-versus-upper-back contact point is partly obscured by the wing/tack.` The narrow tack crop suggested back/saddle contact while the broader contextual crop places it near the upper back/shoulder and not visibly on the saddle; retain the anatomical uncertainty rather than assert a new confirmed contact defect.
18. **Action scope / exclusions:** `holds` — the approved loaded standing setup, not a completed object transfer; no combat, modern/futuristic interface, tactical or superhero clothes, panic or exaggerated comedy.

### Pegasus — bible checklist, top to bottom
19. **Silhouette / posture:** `holds` — one adult athletic winged stallion in right profile with arched neck, upright ears and raised tiered feathers. `cannot see: withers-to-chest scale is obscured; far-side wingspan and both roots are not established.` Ear tips rise above the helmet; strict poll clearance remains uncertain as noted above.
20. **Face form / muzzle:** `holds` — long straight equine profile, dark slate-charcoal muzzle and visible nostril; pale head without a permanent dark blaze/patch. Directional gray shading is not recorded as a permanent marking.
21. **Eyes / mouth / jaw:** `holds` for small dark side eye and closed composed equine mouth at coarse scale; `cannot see: exact dark-brown/obsidian iris, brow ridges, lip/chin microstructure and mandible proportions are not resolved.`
22. **Ears:** `holds` — attentive pointed ears; `cannot see: precise far-ear symmetry is limited by profile overlap.`
23. **Mane / forelock / tail:** `holds` — pale loose mane/forelock and flowing white-silver tail ending around hock height, with no braids/cropping or heavy draft-horse feathering. `cannot see: fine hair texture is not independently verified.`
24. **Build / legs:** `holds` — substantial athletic equine torso and four separate slender legs with four compact dark, non-cloven hooves. No fused/duplicated lower legs, paws or talons in `[600,645,1190,855]`.
25. **Signature 1 / shoulder wings:** `holds` for visible massive raised multi-tier feather silhouette with long primaries and graduated coverts; `cannot see: far wing and complete paired-root attachment are hidden by the near wing/body.` All visible upper tips fit inside the actual frame.
26. **Signature 2 / coat contrast:** `holds` — pale white/silver-cream coat and hair contrasted with dark muzzle and hooves; some local tonal modeling remains a style deviation, not a new coat marking.
27. **Signature 3 / energetic saddle:** `drifted: the correct gold knotwork motif exists, but its self-illuminated energetic appearance is not established; it reads as ordinary ornament.`
28. **Default tack / cargo:** `holds` for the visible brown-leather loaded saddlebag with rectilinear folder edges and cord-like ties. `cannot see: far-side bag is naturally occluded and cannot be counted.` No exact inventory or unapproved lid-state is asserted.
29. **Head/neck band:** `holds` for integrated gold-patterned band and no visible metal bit; `drifted` on the energetic-light state for the same reason as the saddle. No modern equestrian saddle/stirrup irons, nylon, plate barding, spikes or neon/mechanical attachments.
30. **Expression / allowed action:** `holds` — calm steady ground stance, not panic, exhaustion, vicious aggression, cartoon grimace or mechanical motion. The image does not prove an exchange of folders.

### Environment / style / delivery
31. **Location:** `holds` — Gateway Pavilion's classical stone colonnade, heavy celestial-pattern pediment, vines and large rectangular paving blocks. Celestial relief decoration is permitted architecture, not a prohibited cosmic sky. Background landforms are not promoted to new named geography.
32. **Palette:** `holds` — charcoal/slate/sepia, bronze/brown, pale cream-silver, warm dusk gold/orange; no conspicuous neon/cyan/magenta/vivid red/grass-green intrusion.
33. **Materials:** `holds` at coarse scale for stone, bronze, worn leather, parchment and matte cloth; `cannot see: exact weave/alloy chemistry is not image-verifiable.` The decorative gold's material read does not prove active power.
34. **Light / weather:** `holds` — clear warm dusk from the low horizon, long outlined shadows and no active road-energy river; dormant staff and stone. `drifted: local smooth modeled shading remains against the requested flat-plane treatment.` No obvious gold spill across skin or coat.
35. **Global medium:** `holds` for broad flat-print composition and matte texture; `drifted` in the named local modeled/hatch areas. Feather boundaries alone and paper grain are not used as evidence of dense engraving.
36. **Framing:** `holds` — complete man, four hooves, visible wing tips and margins inside the original frame; `drifted: pediment, not open sky, occupies the above-wing clearance.` The latter is a prompt-specific background mismatch, not a clipped wing.
37. **Camera / exclusions:** `holds` for wide two-shot and readable deep scene; `cannot see: exact 28mm focal length cannot be measured from the illustration.` No readable lettering, numerals, watermark, logos, border, panel divisions, UI, modern devices, crystals or floating terrain observed.
38. **File / ratio:** `holds` — genuine decoded PNG, `1536x864`, exact 16:9, byte-for-byte copy of the native result. No downstream pixel repair or upscaling.

## Drift notes
1. **Held:** paired outer sandal wings and wingless inner ankles; four dark hooves; full visible upper-wing frame clearance; exact 16:9 delivery through the requested OpenRouter Sunburst route.
2. **Remaining confirmed issue:** saddle/chest knotwork reads as golden ornament rather than clearly luminous energetic light.
3. **Style:** global broad color-plane composition holds, but localized modeled shading and dense tunic hatch/fold texture remain. Do not exaggerate this into a uniformly photographic or fully engraved image.
4. **New character drift:** Hermes's curls read very dark brown/black rather than warm golden-brown with lighter highlights.
5. **Prompt-specific framing mismatch:** upper wings clear the image edge, but the pediment fills the gap instead of the requested sky band. This is not clipping.
6. **Cannot see / unresolved:** strict poll-above-helmet clearance, hidden withers relationship, exact shoulder/upper-back contact, far wing root/bag, exact irises and freckles. No failure is inferred from the horse's long muzzle hanging below helmet level.
7. **Scope:** the approved static loaded setup is preserved; no completed folder transfer, animation or publication is claimed. Further action changes need their own approved brief.

## Handoff / human review
- `status: draft`, verdict blank. Jordan decides `accepted` or `drifted`; no automatic rerender or filing.
- TUI delivery: the actual image's absolute path is supplied for opening, because this interface does not intercept `MEDIA:` attachments.
- Renderer integration is now exercised by one real generation, not just a mock test. This does not imply that all visual constraints passed.
