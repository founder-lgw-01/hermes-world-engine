# Motion rules, brief to motion spec

The approved video brief defines the outcome. The accepted still establishes
appearance. The spec translates both into a supported render request, not a
new creative outcome invented by the spec writer.

## Guided brief and feasibility

Use `_templates/motion-brief.md`. Ask missing questions in small groups; explain
choices without requiring the operator to know model terminology. Label proposed
choices, source facts, and operator answers separately. Blank is unanswered.

Before brief approval, inspect the chosen image, its approved sidecar, and the
active host schema/configuration. Classify requests as supported, uncertain, or
unsupported with evidence. Check visible head size, starting angle, road space,
travel direction, occlusion, unseen-body invention, and input/settings support.
Separate character/environment references require an exposed tool parameter;
a description mentioning references is not proof that the active schema accepts
them. Resolve unsupported settings and creative conflicts with the operator.
Supported input does not guarantee successful motion.

Existing-still mode never reopens acceptance or generates replacements. New-scene
mode starts with the video brief, then links a still brief into `01_spec`; follow
that stage's contract and approvals through rendering and filing, then return.
No motion spec/render proceeds without an accepted, approved, filed source.
An approved concept brief may await that source; rerun feasibility when it arrives
and obtain renewed brief approval if the intended action or delivery changes.

## Decoded-frame sources

Use this named mode inside `04_animate` to continue an accepted clip from one
of its actual frames. It produces no replacement artwork and no image-generation receipt.
Do not route a decoded frame through `01_spec`/`02_render` or invent their outputs.

1. Select the exact predecessor video, predecessor render record and
   predecessor manifest row. Require the render record to say `status: approved`
   and `verdict: accepted`; match the actual video SHA-256 to both record and row.
   Preserve the predecessor and its acceptance. Missing or mismatched evidence
   blocks extraction for use as an accepted continuation source.
2. Measure the source, record the zero-based decoded frame index and timestamp,
   and perform decode-only extraction. Inspect the actual PNG and nearby motion
   samples. Check whether the predecessor decelerates in its final second: if it
   slows down before the final frame, extract the earlier full-stride frame (and
   record that frame index as the outgoing splice point) rather than the
   decelerated final frame. Record its dimensions, format, frame SHA-256 and
   exact derivation. A crop, repaint, interpolation or other alteration is not
   this mode. Keep one home per PNG; later versions use new filenames, never
   overwrite an accepted frame. A matching image does not prove a continuous
   gait: state an explicit step cadence (steps per second) and locked exposure in
   the continuation brief/spec so the next generation does not default to a
   slower pace or shifted brightness.
3. Copy `_templates/motion-source.md` to
   `runs/motion/<set>/<shot>/00-source-N.md`. This source record is the derived
   frame's sidecar and filing home, not a second approval tracker. Record real
   source-frame acceptance evidence without inventing a prompt, job or charge.
   Present the exact image and completed sidecar for explicit approval; only
   then record `status: approved` and `verdict: accepted` metadata. Approval of
   the predecessor or a brief alone does not approve this new source record.
4. Before motion-spec derivation, require the brief and sidecar approved and
   the sidecar's verdict accepted. Recheck the predecessor record/manifest and
   actual hashes. Freeze the source record, PNG, predecessor video, predecessor
   render record and predecessor manifest in the spec after approval metadata
   is recorded. The manifest supplies filing evidence; its render record owns
   acceptance. Missing evidence, an unapproved input or a changed hash halts use.
5. The approved sidecar files this derived source; no generated-still manifest
   row is needed. After the new video is accepted, its normal motion-manifest
   row names this record in the existing **Source sidecar** column. Keep the
   normal generated-still filing path unchanged. Separate public hosting and
   spec/render approvals still apply; never infer them from source acceptance.

## Spec sections, in order

0. **Source manifest.** Approved brief and source sidecar or decoded-frame source record,
   source image SHA-256,
   selected approved world-record paths/hashes where needed, inherited deviations.
   For a decoded frame, also freeze the selected predecessor evidence above;
   the original still's sidecar cannot authorize the extracted frame's pixels.
   Freeze any **Studio handoff** intake/sequence/storyboard/continuity versions
   and selected maps with SHA-256 values after approval. Recheck those exact
   versions before rendering; state IDs reference continuity, not a second canon.
1. **Brief and feasibility.** Outcome and every brief field; resolved decisions,
   supported input/settings, uncertainties, and exact configured provider/model.
2. **What moves and sequence.** Primary travel, head/gaze, expression and props;
   beginning, main action, ending; then secondary motion. Define relative image
   directions and motion priorities. Do not add an unbriefed action.
3. **What holds.** Identity/design, wardrobe, world and medium; explicitly separate
   allowed changes in pose, gaze, expression and position from these invariants.
4. **Camera and delivery.** Locked off or one move; supported duration, aspect,
   resolution, audio and upscale. No silent extra processing.
5. **At risk and success checks.** Guards for threatened invariants plus an
   observable review criterion for every requested primary action and ending.
6. **Prompt.** Derived only from the preceding sections; sent unchanged after
   spec/render approval. Tool settings remain separate from prompt prose.

## Prompt discipline

Name the primary action positively and prominently, with beginning, main action,
and ending. One coherent shot; keep secondary motion subordinate. A locked camera
can isolate character-motion tests but is a choice, not a default.

Preserve identity and visual design, not a frozen pose. Never combine a requested
head turn with 'gaze never changes' or freeze all face pixels while asking for a
new view. Say facial structure, hair and helmet design remain consistent while
the approved head/gaze motion occurs. Do not demand 'everything identical' when
movement is the outcome. Hold accepted colour/style deviations as-is; do not
invent freckles or iris detail absent at source scale.

Inherit the source medium, lighting and palette; guard against 3D/realism drift
without suppressing intended motion. Reference the image as 'the supplied
reference image', never its path. Ending follows the brief: continuous travel
must not acquire an automatic settle. Camera, continuity and exclusions follow
the approved brief rather than a universal prohibition on scene changes.

## Review, variations and filing

Review visual consistency and motion success separately using the temporal
checklist. A consistent near-static clip may miss a walking criterion. Give
actual timestamps or measured frame indices, and disclose sampled-review limits.
The operator owns acceptance; do not relabel an accepted source/video as rejected.

Rejected attempt: derive the next numbered spec from drift notes and an approved
revised brief where intent changes. Preserve prior versions. Accepted-video
variation: use a new shot folder linked to the accepted predecessor; begin with a
new draft brief. Never rewrite an approved spec or brief to absorb new intent.
After video acceptance, file a relative-path row into `runs/motion/<set>/manifest.md`
using `_templates/motion-manifest.md`. Filing is local retention, not publishing.

For studio-linked work, finishing requirements may inform timing and framing;
voice, sound and accurate on-screen text are not baked into generated animation.
Accepted clips return to the sequence review when narrative, then composition
only when selected. Neither an individual clip's acceptance nor planned start/end
states prove actual adjacent-shot continuity.
