---
set: location-probes
shot: hermes-sky-bridges-and-passages
attempt: 3
stage: 02_render
status: approved
verdict: drifted
generated: 2026-10-15T09:38:51+00:00
sources:
  - 01-spec-3.md
  - 02-image-3.png
---

# Hermes at Sky-Bridges and Passages, render 3

## Prompt as sent

Edit the supplied image only at Hermes's boots/sandals to respect natural leg occlusion, keeping the entire rest of the illustration unchanged. Because his front leg steps across in front of his back ankle from this angle, the outer wing on the blocked side is naturally hidden behind his leg. Remove the inner wing located between his two boots/ankles completely so that only smooth leather boot/strap and stone paving appear between the legs, and keep only a single pale feathered heel wing on the outer unblocked side of the boot. Do not draw two wings on one boot and do not place any wing in the gap between his ankles. Preserve his exact pose, face, winged helmet, dark cloak, tunic, bronze greaves, twin-serpent caduceus, the grounded limestone viaduct, glowing warm-gold stone channels, columns, distant hilltop city, dusk sky, 16:9 framing, and traditional Japanese woodblock-print (ukiyo-e) line art and matte textured-paper finish unchanged.

## Tool metadata

- model: `gpt_image_2_5` (`variant: sunburst`)
- provider: `Higgsfield` (`mcp__higgsfield__generate_image`)
- job: `e551b907-7f55-4dae-8e49-452df327ecce`
- reference media ID: `95338f4c-2226-40cd-83ab-813510d08c95` (`runs/location-probes/hermes-sky-bridges-and-passages/02-image-1.png`)
- aspect ratio requested: `16:9`
- aspect ratio returned: `16:9`
- resolution: `1344×752`
- quality: `low` (`resolution: 1k`)
- seed: `not exposed`
- cost preflight: `0.25 credits`
- file: `02-image-3.png` (`PNG`)
- sha256: `08648044a534272fff7cfd7b830cb601eca24c3f5eed43e17024872fb16bc18f`
- generated: `2026-10-15T09:38:51+00:00`

### Host note, tool substitution
The host tool named in `_reference/host.md` (`image_generate`, model `openai/gpt-image-2.5-sunburst` via Nous Portal) returned `model_access` 404. Per `_reference/framing-and-scale.md`, the render fell back to `gpt_image_2_5` (`variant: sunburst`) via Higgsfield. `_reference/host.md` was not edited.

## Findings

- holds: grounded limestone viaducts, ravines, distant city, dusk sky, warm-gold carved stone channels, and 16:9 framing remain consistent with `02-image-1.png`.
- holds: Hermes's pose, silhouette, winged helmet, dark chlamys, harness, bronze bracers and greaves, and twin-serpent caduceus remain consistent.
- drifted: although `02-image-3.png` removes the extra outer wing on the far right of the front boot, it still retains a small feathered wing in the inner gap between the ankles rather than removing it completely.
- drifted: inherited from `02-image-1.png` — undertunic reads slate-grey rather than charcoal-grey, hair reads darker brown, and left-wall heraldic banners remain.
- cannot see: freckles, amber eye color, nose bridge, and square-jaw microdetail at this wide framing scale.

## Drift notes

Passing the full `02-image-1.png` as a reference image causes `gpt_image_2_5` to strongly preserve the existing bright silhouette in the gap between the ankles even when the prompt asks to remove it. Leave verdict open for operator review (`accept` or `drifted`).
