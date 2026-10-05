# 01_spec, brief to shot spec

1 job: turn 1 shot brief into 1 spec the render acts on: brief, characters in
frame, scene, camera, at risk, prompt. On a rerun, revise the last spec from
the drift notes.

## Inputs
- Working (this run): `../runs/<set>/<shot>/00-brief.md`, written by the
  operator or intake handoff from `../_templates/shot-brief.md`; complete brief
  approval is required before deriving the spec.
- Working (rerun): the highest-numbered `../runs/<set>/<shot>/02-render-N.md`,
  which says `verdict: drifted`
- Reference (every run): `../world/environment.md`, selected approved
  `../world/environment/` modules and visible location records,
  `../world/style.md`, `../world/characters/<name>.md` for each character the brief names,
  `../_reference/spec-rules.md`, `../_reference/drift-checklist.md` for its
  risk table
- Working (studio-linked only): the exact approved planning versions and state
  IDs named in the brief's Studio handoff, plus selected setup-approved maps.
  Apply `../_reference/studio-rules.md`; do not load other shots' prompts.

Do NOT load: `../world/interview.md`, the bible is the truth and the interview
is raw; any other shot under `../runs/<set>/`, shots do not inherit;
`../_reference/setup-interview.md` and `../_reference/bible-schema.md`, setup
material.

## Process
1. Refuse to derive a spec unless the completed brief and every bible/planning
   input it selects say `status: approved`. Missing preparation blocks the spec.
   Refuse if the brief names a character with no file in `../world/characters/`.
2. Read the brief. If a required field is empty, return to brief preparation,
   ask the operator and obtain complete brief approval before continuing. Surface
   delegated choices there; do not invent answers inside the derived spec.
3. Select the smallest needed environment dependency closure and candidate
   reference roles. Record each selected source path, role ID where relevant,
   and SHA-256 in **World-input manifest**, including the approved brief and
   selected Studio handoff inputs. Resolve camera/state conflicts upstream;
   finishing requirements guide framing, not generated overlay text. Then write the sections in the
   order `spec-rules.md` gives: Brief, Characters in frame, Scene, Camera, At
   risk, Prompt. Derive each section from the ones above it and nothing else.
4. Rerun: open the drift notes first. Name each drifted invariant under **At
   risk** with the change made to guard it. Number the new spec N+1.

## Outputs
- `../runs/<set>/<shot>/01-spec-N.md`, frontmatter: `set`, `shot`, `attempt`,
  `stage: 01_spec`, `status: draft`, `generated`, `sources`

## Human check
Read the spec top to bottom against the brief and the named bibles. Every
invariant under **At risk** is guarded in **Prompt** in words, and nothing in
**Prompt** contradicts a section above it. Changes return through this stage
as a revised draft/new attempt, not an edit to an approved body. The operator may
approve it by editing the file or by clear chat approval naming the spec; after
that approval, the agent records `status: approved` only.
