# Character World Engine, the selected line

New studio work starts with “What are we building?” in `studio/CONTEXT.md`:
image, character, world/location, single animated shot or storied animation.
Intake selects only required work. Reuse approved inputs; missing assets are
explicit approval-gated preparation. Existing direct image/motion entry points
and all historical output paths remain valid; no run migration is required.

The image line remains brief → spec → render/review → filing. Motion starts in
`04_animate` with its draft brief and existing production checks; new-scene work
returns through the still line, while accepted-image work never forces a rerender.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| `studio/00_intake/CONTEXT.md` | guided intake and route | request, selected records | approved-scope intake and optional early composition brief | selected endpoint, preparation, roles and allowed actions |
| `studio/01_story/CONTEXT.md` | select/create series foundation, narrative only | approved intake and selected world facts | selected approved foundation version | reusable rules, not unapproved canon |
| `studio/02_sequence/CONTEXT.md` | sequence planning, then actual clip reconciliation | approved foundation/intake; accepted clips for review | sequence, storyboard/coverage, continuity, review | planning baseline, then observed adjacent-shot continuity |
| `00_setup` | interview, then write modular world records and bibles; once per world, once per added character | answers, `world/references/` | environment index, selected modules/locations, style, characters, reference permissions | confirm every `inferred` line against an image |
| `01_spec` | brief to frozen world-input manifest, spec, and prompt | `runs/<set>/<shot>/00-brief.md` | `runs/<set>/<shot>/01-spec-N.md` | every risk is guarded in the prompt |
| `02_render` | verify frozen inputs, send prompt, save image, check drift | approved spec and manifest | `runs/<set>/<shot>/02-image-N.<ext>`, `runs/<set>/<shot>/02-render-N.md` | walk the drift checklist; write the verdict |
| `03_file` | file the accepted image into its set | the record with `verdict: accepted` | `runs/<set>/<shot>/03-sidecar.md`, 1 line in `runs/<set>/manifest.md` | read the sidecar's prompt against the record |
| `04_animate` | brief, assess feasibility, specify, render, review, file motion | approved video brief and source sidecar before spec/render | `runs/motion/<set>/<shot>/00-brief.md`, `01-spec-N.md`, `04-video-N.<ext>`, `04-render-N.md`; accepted rows in `runs/motion/<set>/manifest.md` | approve brief, then spec/render; judge consistency and motion success, then accept |
| `05_compose/CONTEXT.md` | specify finishing and review actual final export | accepted clips, composition brief, sequence review when narrative | composition spec; final record/export only after separately authorized execution | spec/execution scope, then final-piece acceptance |

Each stage's contract is the `CONTEXT.md` in its folder. Setup also owns new
locations and versioned spatial maps. No composition adapter is implemented by
this extension: its contract stops before execution without a separately
authorized ready route. A `verdict: drifted`
sends the shot back to `01_spec`, which writes attempt N+1 from the drift
notes. Motion drift stays in `04_animate`, which writes the next numbered
`01-spec-N.md` under `runs/motion/`. Every attempt keeps its files.

Factory (stable, every run): `_reference/`, `_templates/`, and `world/` once approved
Product (new each run): `runs/<set>/<shot>/`, numbered by the stage that wrote each file
Studio output naming and shared gates: `_reference/studio-rules.md`. Production
records use `runs/studio/<production>/`; reusable foundations use `stories/<series>/`.

## Status is whatever exists

A stage is complete when its output file carries `status: approved` in its
frontmatter. Approval is a human decision: the operator may edit the file or
give clear approval in chat that names the reviewed output or scope. After that
explicit approval, the agent may record only the approval metadata (`status`,
and a render record's `verdict`) without changing the generated body.

A stage refuses to derive/execute its output until its declared inputs are
approved and applicable acceptance/filing checks pass. Dependencies follow the
selected route, not the numerically preceding folder. Intake and authorized
setup interviews can begin without assets; incomplete drafts are not approved.
Status lives in the artifacts, not a tracker, board or separate state file.

## Frontmatter

Every shot output begins with `set`, `shot`, `attempt`, `stage`, `status`
(`draft` | `approved`; you flip it), `generated`, `sources`. A setup output
carries `world` instead of the first 3. Modular routing records additionally
carry `kind`, `scope`, `depends_on`, and `reference_roles`. A render record adds
`verdict`.
Studio records use `production` or `series` instead of `set`/`shot`; new templates
start draft. Missing fields and uninspected required evidence never imply approval.

## Every output is an edit surface

Each stage writes a plain file for human review. Request changes at that surface;
the owning stage derives the revised draft or next numbered attempt. Approved
generated bodies remain intact, and old approvals do not transfer to replacements.
After explicit approval, the agent records only permitted approval metadata.
Related ready artifacts may be reviewed together by exact path/version; a package
does not preapprove future outputs or authorize publishing.

## Naming

Folders are `NN_kebab-case` where order matters. Renaming reorders the line,
and that is the point. Files are kebab-case. A `_prefix` means *about the
workspace, not of the work*, the way `_reference/` holds the rules and never the
output.

Slugs are lowercase, no spaces, no punctuation. Every output carries the slug of
the thing it belongs to.
