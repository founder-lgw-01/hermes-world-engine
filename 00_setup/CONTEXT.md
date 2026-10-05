# 00_setup, interview the operator, then write the bibles

1 job: turn reference images and the operator's answers into the bibles every
shot reads. Runs once per world. Runs again in character mode for each
character added later, and in location-resolution mode for each named draft
location that needs its unresolved facts replaced before use.
New-location mode adds a missing location without changing approved records.
Spatial-map mode writes versioned geography/layout through the same setup gate.

## Inputs
- Working (this run): the operator's answers, given in chat; the images in
  `../world/references/`; the blank `../world/environment.md`,
  `../world/style.md`, `../world/interview.md`, and the templates for modules,
  locations, and reference permissions
- Working (character mode): `../world/environment.md`, `../world/style.md`,
  every file in `../world/characters/`, for relative scale and shared wardrobe
- Working (location-resolution mode): `../world/environment.md`, the named
  draft `../world/environment/locations/<location>.md`, and only its explicit
  dependency closure; the operator's answers replace its unresolved facts.
- Working (new-location/spatial-map mode): approved world/style and selected
  approved location/module records with their explicit dependency closure;
  operator answers and the named studio intake/coverage requirement only.
- Reference (every run): `../_reference/setup-interview.md`,
  `../_reference/bible-schema.md`, `../_templates/character-bible.md`, and
  `../_templates/location.md` for location modes. Spatial-map mode uses
  `../_reference/spatial-rules.md`, `../_templates/spatial-map.md`, and
  `../_reference/world-routing-schema.md` instead of character questions.

Do NOT load: individual shot folders under `../runs/<set>/` or `../runs/motion/`,
shots are downstream; the named studio requirement is the only planning input;
`../_reference/spec-rules.md` and `../_reference/drift-checklist.md`, they read
bibles and never write them.

## Process
1. World mode: refuse to run if `../world/environment.md` says
   `status: approved`; this folder holds 1 world. Character mode: refuse
   unless it does. Location-resolution mode: refuse unless the named location
   says `status: draft`; an approved location requires a new world setup run.
   New-location/spatial-map modes require an approved world and never overwrite
   approved records or an existing target. Map revisions use a new numbered file.
2. Ask every question in `setup-interview.md`, in its order, a few at a time.
   World mode asks all of them; character mode asks the character section only.
   Location-resolution mode asks only the target record's unresolved or
   unknown fields, a few at a time. Write nothing until the applicable
   questions are answered.
   New-location mode asks the location template's applicable fields; spatial-map
   mode follows the selected geography questions in spatial-rules. Neither
   mode invents an unresolved connection, dimension or source fact.
3. Fill `../world/interview.md` with every question and its answer. Character
   mode appends a section for the new character. Location-resolution mode
   appends a dated section naming the location and every resolution answer.
4. World mode only: fill `../world/environment.md` as a short index. Create each shared rule
   module from `environment-module.md`, each named location from `location.md`,
   and each governed image companion from `reference-permission.md`. Fill
   `../world/style.md` in place. For each character, copy
   `character-bible.md` to `../world/characters/<name>.md` and fill it.
   Every field comes from an image or an answer, marked `stated` or `inferred`
   as `bible-schema.md` defines. Leave no field blank: write `unknown` and list
   it under **Open**.
   Character mode writes only the new character and interview addition, not
   approved environment/style records. Never overwrite an approved character.
5. Character mode: state the new character's height and build against each
   existing character, by name. Location-resolution mode: rewrite only the
   named draft location record from `location.md`; retain only facts supported
   by the operator's answers or its approved dependencies.
6. New-location mode writes the new named location from its template and records
   the answers; spatial-map mode writes a new version from spatial-map.md with
   provenance, owned/derived facts and revision impact. Do not edit an approved
   index to list them: new records can be selected by explicit path. A conflicting
   approved fact must be resolved through its owning setup record/decision first.
7. Approve facts before selected visual coverage. Coverage/reference images use
   the existing image stages with separate briefs/spec approvals and acceptance;
   scope or map approval never authorizes generation automatically.

## Outputs
- `../world/interview.md`, `../world/environment.md`, selected
  `../world/environment/**/*.md`, `../world/style.md`,
  `../world/characters/<name>.md`, and reference companions. Routing records
  use the metadata in `_reference/world-routing-schema.md`.
- New-location mode: a new `../world/environment/locations/<location>.md`.
- Spatial-map mode: `../world/environment/maps/<map>-N.md`; no in-place changes
  to approved maps, index entries, bibles or downstream shot records.

## Human check
Open each bible beside the images in `../world/references/`. For every line
marked `inferred`, confirm it against an image or rewrite it; strike any line an
image contradicts; answer or strike every line under **Open**. The operator may
approve the reviewed files by editing them or by clear chat approval naming the
scope; after that approval, the agent records `status: approved` on each named
file only.
