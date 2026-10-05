# Spatial rules, setup-owned maps before coverage

Paths are workspace-relative. `00_setup/CONTEXT.md` alone writes spatial facts.
Use `_templates/spatial-map.md`; world record metadata follows
`_reference/world-routing-schema.md`.

## Entry and selection

Spatial-map mode needs an approved world and explicitly selected approved
location/module/character records. Select their explicit dependencies only.
If the world or required location does not exist, prepare it through setup
first. The approved intake/storyboard may name the requested coverage; it is
not a source of new geography. No downstream stage writes spatial canon.

Ask about named locations, relative placement, landmarks, entrances, routes,
barriers, staging space, available viewpoints and unknown dimensions. Existing
facts retain their source owner; the map cites exact versions. Every newly
established relationship is marked `stated` or `inferred` with provenance.
An unsupported connection/dimension is `unknown`, never a convenient guess.

## Map production and authority

Write a text layout, top-down diagram or an explicitly scoped image requirement
in the draft record. Diagrams derive from the listed facts; they cannot add
relationships or metric precision. A graphic is optional, not a prerequisite
to a useful approved map. Generation of a map image follows the existing image
brief/spec/render/acceptance path only with explicit approval.

Record which facts this map owns versus which it derives. Conflicts with
approved bibles/images are blockers: present them for a setup decision. Do not
silently move a landmark to match a new render. Future coverage validates
landmarks and geography together against the selected map version.

Approve all newly established spatial facts before dependent coverage or shot
specifications. Unresolved fields needed by the intended shots block approval;
unknown unused dimensions may remain explicitly out of scope with operator
agreement. Camera/staging space describes what is available, not the selected
shot camera or time-specific character/prop positions.

## Versioning and discovery

Write each new version at `world/environment/maps/<map>-N.md`. An approved map
is immutable; a revision gets a new version, prior-version source link and
impact assessment. It cannot supersede an approved location fact by itself:
resolve that fact through the owning setup record/decision first.

Do not edit an approved index, character bible or location in place to list or
fit the map. Select new approved records by explicit workspace-relative path;
index updates require their own setup revision. A map's depends_on references
approved world records only and stays acyclic. List downstream consumers in
revision-impact prose, never as world dependencies that form a cycle.

## Coverage handoff

The storyboard's coverage table owns needed forward/reverse/side/elevated views,
body turnarounds, head angles, expressions or prop states. This map owns spatial
facts, not a second reference to-do list. Each selected reference image is a
normal image run with its own brief, source manifest, review and filing; retain
its canonical run path instead of copying it into world records downstream.

Before reference production, require approved relevant facts and a selected
view/identity purpose. After production, inspect the actual reference against
its scoped map/bible. Reuse accepted references, preserve inherited deviations,
and request only coverage needed by intended shots. No technical guarantee of
cross-view consistency or adapter support follows from having a map.
