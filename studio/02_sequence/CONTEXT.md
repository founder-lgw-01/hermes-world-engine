# 02_sequence, plan a coherent sequence and reconcile its accepted clips

One job, two passes: plan spatial/state continuity, then verify actual continuity.

## Inputs
- Planning: selected approved intake and foundation, approved map/location
  records and operator answers; missing maps are explicit setup tasks.
- Review: the approved sequence/storyboard/continuity versions plus only the
  accepted, filed clip records and media named by that storyboard.
- Reference: `../../_reference/studio-rules.md`,
  `../../_templates/sequence-brief.md`, `../../_templates/storyboard.md`,
  `../../_templates/continuity.md`, `../../_templates/sequence-review.md`;
  `../../_reference/drift-checklist.md` for the review pass only.

Do NOT load: other productions, full character/location libraries, raw interviews,
provider configuration or `../../_reference/studio-extension-design.md`.

## Process
1. Require `status: approved` on the selected intake and foundation. Draft the
   sequence brief with particular events and observable story success checks;
   obtain its approval before deriving the shot-planning baseline.
2. Establish selected geography from setup-approved maps/records. Return new or
   conflicting spatial facts to `../../00_setup/CONTEXT.md`. Planning sketches
   are not approved geography and cannot enter a production specification.
3. Build the storyboard explicitly. Iterate composition intent, reference
   coverage and continuity together. Identify only the missing inputs required
   by intended views; approve preparation scope before generating those inputs.
4. Give every shot a stable ID, event link, start/end state IDs, selected map
   versions and exact still/motion brief targets. Approve the named storyboard
   and continuity package before individual shot production. Missing coverage
   may remain a named preparation task, but blocks that shot's specification.
5. Hand each shot to the existing image/motion contracts with its selected
   planning inputs and state IDs. Reuse accepted shots when suitable. Do not
   copy other shots' prompts or invent new world facts in this stage.
6. Review pass: require every selected clip record to carry `status: approved`
   and `verdict: accepted`, with manifest filing and unchanged source hashes.
   Observe actual start/end states with timestamps/evidence; compare adjacent
   shots and any explicitly approved transition against the baseline.
7. Mismatch or unknown required evidence blocks acceptance. Route the smallest
   change through the revision rules, retaining historical clip acceptance.
   Derive a new review after a changed clip or baseline; no silent substitutions.
8. Obtain human acceptance of the sequence review before composition. Then
   hand exact selected clips and the accepted review to `../../05_compose/CONTEXT.md`.

## Outputs
- `runs/studio/<production>/02-sequence-N.md` — particular events and story checks.
- `runs/studio/<production>/02-storyboard-N.md` — shot order/composition and coverage.
- `runs/studio/<production>/02-continuity-N.md` — canonical expected states/transitions.
- `runs/studio/<production>/02-review-N.md` — actual observations and reconciliation;
  starts draft with empty verdict; only accepted by the human after review.

## Human check
Approve the sequence brief, then the named planning baseline; these approvals
are not approval to render future shots. In the review pass, accepted clips alone
are insufficient: each required transition must hold or have an explicitly
approved revised intent. Record `status: approved` and `verdict: accepted` on the
review only after that human acceptance. Never fabricate observations or timestamps.
