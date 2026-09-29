# Bible schema, what a bible must contain

A bible is the 1 home for everything that must not change. `00_setup` writes
it from reference images and answers. Every shot reads only the records it
needs. Nothing else edits them. `world/environment.md` routes to modular world
records; `world/style.md` and `_templates/character-bible.md` carry their own
stable fields. This file says what each field means and how it is filled.

## Marking every trait

Every trait line ends with a mark and a source:

- `[stated: <source>]`: read straight from a reference image (`ref-03.png`) or
  an operator answer (`interview q7`). The source is named.
- `[inferred]`: the agent's own reading, not confirmed. The operator's check
  turns each of these into `stated` or strikes it.

A line with no mark is a defect. A trait written from memory, from a similar
character, or from what "usually" goes with the rest is not a trait.

## Invariant vs variable

**Invariant**: never changes between shots. If an image moves it, the shot
drifted. Written as a fact a person can check against an image.

**Variable**: allowed to change, inside a stated range. Expression, pose,
wardrobe state, held props. Each variable names its range, and what it may
never become.

The test for which list a trait belongs on: if 2 images differed only in this,
would they still read as the same character? Yes: variable. No: invariant.

## Character bible fields

1. **Identity**: name, role in the world, apparent age, 1 line of who they are.
2. **Silhouette**: what identifies them at distance with no face visible.
   Height band, build, posture, the hair and clothing outline. Invariant.
3. **Face**: shape, skin tone, eyes (color, shape, spacing), brows, nose,
   mouth, jaw, ears, marks (scars, moles, freckles). Invariant. Each on its own
   line, each marked.
4. **Hair**: color, length, texture, cut, how it falls, facial hair. Invariant
   unless the operator names a state under Variables.
5. **Build**: height relative to each other character by name, shoulders,
   limb length, weight, hands. Invariant.
6. **Signature features**: the 2 or 3 things a viewer would name first. Always
   present. Invariant.
7. **Wardrobe**: the default outfit, garment by garment, with color and
   material. Then named wardrobe states (`travel`, `formal`, `wet`), each a
   full list of what changes. Anything never worn.
8. **Variables**: expression range and what is out of character; pose range;
   props they may hold; wardrobe states allowed.
9. **Reference map**: each candidate companion role that evidences the
   character and which fields it may control.
10. **Open**: every `unknown` and every trait the images contradict each
    other on. The operator settles each line.

## Environment record fields

`world/environment.md` is an index, not a payload. Shared rules are separate
modules; each named location is a separate record. Both use the metadata in
`_reference/world-routing-schema.md`.

1. **Core module**: name, era or technology level, 1 line of what kind of
   place, world-wide exclusions, and reference precedence.
2. **Shared modules**: palette and lighting, materials, architecture, terrain,
   topology, or another narrowly owned rule set. Each states only its own facts.
3. **Location record**: what is there, architecture, detail/open space,
   boundaries, local light and palette behavior, and underfoot.
4. **Dependencies**: project-relative paths to shared rules required by the
   record. Never list adjacent locations merely because they connect in prose.
5. **Reference roles**: candidate companion-role pointers, not image attachments.
6. **Open**: unresolved facts and contradictions for the operator.

## Style rules fields

1. **Medium**: painted, photographic, rendered, drawn; the finish.
2. **Look**: the 5 or 6 words that describe every image in the set. Repeated
   in every prompt as the consistency anchor.
3. **Camera defaults**: lens, height, distance, depth of field, when a shot
   does not say.
4. **Aspect ratio**: 1 default, and the others allowed.
5. **Framing conventions**: headroom, where characters sit in frame, how much
   environment shows.
6. **Exclusions**: what no image contains, written as description for the
   prompt (`the image holds no lettering, no watermark, no frame border`).
7. **Open**.
