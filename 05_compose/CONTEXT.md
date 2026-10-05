# 05_compose, specify finishing and review the assembled deliverable

One job: assemble accepted animation with only the requested finishing layers.
No composition adapter is implemented by this extension.

## Inputs
- Working: selected approved `runs/studio/<production>/00-intake-N.md` and
  `runs/studio/<production>/00-composition-N.md`; exact accepted clip files,
  their authoritative records and filing evidence.
- Narrative only: accepted `runs/studio/<production>/02-review-N.md` and the
  planning versions it reviewed. A standalone single clip skips this input.
- Review only: actual final export and evidence from a separately authorized
  execution route. A specification is not evidence that rendering happened.
- Reference: `../_reference/studio-rules.md`, `../_reference/composition-rules.md`,
  `../_reference/drift-checklist.md`, `../_templates/composition-spec.md`,
  `../_templates/composition-record.md`.

Do NOT load: raw world interviews, unrelated shots, credentials, provider
configuration or any unselected integration. No automatic adapter discovery.

## Process
1. If intake/finishing intent is missing, return to `../studio/00_intake/CONTEXT.md`
   to prepare those briefs, reusing the accepted clips without rerendering.
   Refuse spec derivation unless finishing is selected and both briefs say
   `status: approved`.
   Each consumed clip record must say `status: approved` and `verdict: accepted`;
   for a sequence require the same on its review. Verify exact files/hashes and
   ensure the review names these same clip and baseline versions.
2. Derive the composition spec in the order given by composition-rules: frozen
   sources, brief, timeline, selected finishing layers, delivery, risks/checks,
   execution instructions last. Do not generate voice or bake text into clips.
3. Present the spec for human approval with exact execution scope. If the brief
   changes, return to intake for a new version; preserve the accepted clips.
   Require the selected spec to say `status: approved` before any execution.
4. Stop before execution unless a separately authorized task has supplied an
   approved execution route and readiness evidence for it. Missing adapter,
   unapproved inputs, unresolved checks or missing spending permission are a
   halt, not permission to substitute a tool. Naming a tool is not verification.
5. Only after that separately authorized execution, inspect the actual final
   export against every selected criterion. Record actual file/hash, source
   versions, findings and review limitations; never synthesize a render receipt.
6. Leave the record draft and verdict empty for human review. After acceptance,
   record permitted approval metadata and retain the final file locally. Do
   not publish or infer final acceptance from individual clip acceptance.

## Outputs
- `runs/studio/<production>/05-spec-N.md` — derived assembly instructions.
- `runs/studio/<production>/05-record-N.md` — only after actual execution/review.
- `runs/studio/<production>/05-final-N.<ext>` — actual final export, never a stub.
  The record is its local filing/acceptance home; do not duplicate the media.

## Human check
Approve the spec and its allowed execution separately from final export
acceptance. Review clarity, pacing, identity, continuity and requested sound/text.
An uninspected requirement is not a pass. Final `status: approved` and
`verdict: accepted` require approval of the actual named export/version.
Publication requires its own authorization and verified receipt.
