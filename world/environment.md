---
world: hermetic-gates
kind: environment-index
stage: 00_setup
status: approved
generated: 2026-09-29
scope: Selective-loading index; no environment facts live here.
depends_on: []
reference_roles: []
sources:
  - world/interview.md
---

# Hermetic Gates, environment index

## Shared modules
- `world/environment/core.md` — world identity, technology framing, and exclusions. [stated: interview q1-q3, q9]
- `world/environment/palette-and-light.md` — palette, daily light, and weather. [stated: interview q4, q8]
- `world/environment/materials-and-wear.md` — material and aging rules. [stated: interview q5]
- `world/environment/forms-and-architecture.md` — recurring shapes, architecture, plants, and magical vehicles. [stated: interview q6]

## Locations
- `world/environment/locations/gateway-pavilion.md` — approved foreground temple/courtyard. [stated: interview q7]
- `world/environment/locations/observatory-court.md` — approved circular observatory platform. [stated: interview q7]
- `world/environment/locations/crystal-citadel.md` — unresolved; do not use before its excluded elements are replaced. [stated: interview q7, q9, q10]
- `world/environment/locations/sky-bridges-and-passages.md` — unresolved; do not use before its excluded elements are replaced. [stated: interview q7, q9, q10]
- `world/environment/locations/aether-falls-and-islands.md` — unresolved; do not use before floating-island geography is replaced. [stated: interview q7, q9, q10]
- `world/environment/locations/archive-cloister.md` — draft roofed retrieval and handoff space beside Gateway Pavilion. [stated: operator-approved location details, 2026-09-30]
- `world/environment/locations/processional-causeway.md` — draft open-air civic route from Gateway Pavilion to Hall of Sealed Routes. [stated: operator-approved location details, 2026-09-30]
- `world/environment/locations/hall-of-sealed-routes.md` — draft enclosed controlled-threshold hall. [stated: operator-approved location details, 2026-09-30]
- `world/environment/locations/rooted-index-garden.md` — draft open-air terrace of tended knowledge growth, linking Archive Cloister to Aether Falls. [stated: operator-approved location details, 2026-09-30]
- `world/environment/locations/sunken-relay-forum.md` — draft open-air civic relay forum between the Causeway, Observatory Court, and Hall. [stated: operator-approved location details, 2026-09-30]

## Load for one shot
1. Read this index, `world/style.md`, and only named character records.
2. Select only shared modules and visible locations required by the brief.
3. Load each selected record’s explicit dependency closure.
4. Select the smallest compatible candidate reference roles; record selected paths, role IDs, and hashes in the shot spec.