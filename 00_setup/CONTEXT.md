# 00_setup, interview the operator, then write the bibles

1 job: turn reference images and the operator's answers into the bibles every
shot reads. Runs once per world. Runs again in character mode for each
character added later, and in location-resolution mode for each named draft
location that needs its unresolved facts replaced before use.

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
- Reference (every run): `../_reference/setup-interview.md`,
  `../_reference/bible-schema.md`, `../_templates/character-bible.md`, and
  `../_templates/location.md` for location-resolution mode

Do NOT load: any shot under `../runs/<set>/`, shots are downstream;
`../_reference/spec-rules.md` and `../_reference/drift-checklist.md`, they read
bibles and never write them.

## Process
1. World mode: refuse to run if `../world/environment.md` says
   `status: approved`; this folder holds 1 world. Character mode: refuse
   unless it does. Location-resolution mode: refuse unless the named location
   says `status: draft`; an approved location requires a new world setup run.
2. Ask every question in `setup-interview.md`, in its order, a few at a time.
   World mode asks all of them; character mode asks the character section only.
   Location-resolution mode asks only the target record's unresolved or
   unknown fields, a few at a time. Write nothing until the applicable
   questions are answered.
3. Fill `../world/interview.md` with every question and its answer. Character
   mode appends a section for the new character. Location-resolution mode
   appends a dated section naming the location and every resolution answer.
4. Fill `../world/environment.md` as a short index. Create each shared rule
   module from `environment-module.md`, each named location from `location.md`,
   and each governed image companion from `reference-permission.md`. Fill
   `../world/style.md` in place. For each character, copy
   `character-bible.md` to `../world/characters/<name>.md` and fill it.
   Every field comes from an image or an answer, marked `stated` or `inferred`
   as `bible-schema.md` defines. Leave no field blank: write `unknown` and list
   it under **Open**.
5. Character mode: state the new character's height and build against each
   existing character, by name. Location-resolution mode: rewrite only the
   named draft location record from `location.md`; retain only facts supported
   by the operator's answers or its approved dependencies.

## Outputs
- `../world/interview.md`, `../world/environment.md`, selected
  `../world/environment/**/*.md`, `../world/style.md`,
  `../world/characters/<name>.md`, and reference companions. Routing records
  use the metadata in `_reference/world-routing-schema.md`.

## Human check
Open each bible beside the images in `../world/references/`. For every line
marked `inferred`, confirm it against an image or rewrite it; strike any line an
image contradicts; answer or strike every line under **Open**. The operator may
approve the reviewed files by editing them or by clear chat approval naming the
scope; after that approval, the agent records `status: approved` on each named
file only.
