# 00_intake, turn a request into an approved route and brief

One job: agree the deliverable, scope, reusable inputs and necessary preparation.

## Inputs
- Working: operator request and only explicitly selected asset records or a
  named previous intake for a revision; a request need not have approved assets.
- Reference: `../CONTEXT.md`, `../../_reference/studio-rules.md`,
  `../../_templates/studio-intake.md`; `../../_templates/composition-brief.md`
  only when finishing is selected. Read asset records, not entire run folders.

Do NOT load: unrelated productions, `../../world/interview.md`, all world
records, media-tool configuration, or `../../_reference/studio-extension-design.md`.

## Process
1. Ask “What are we building?” or confirm the already-stated deliverable. Use
   the route table in the parent contract. Ask relevant questions in small groups;
   explain options and record proposals separately from answers.
2. Write a new numbered intake from its template. Record outcome, purpose,
   accepted endpoint, selected/skipped work, roles, success criteria and scope.
   Classify existing assets by authoritative evidence, not filename or existence.
3. With missing assets, name preparation tasks and their owning contracts. A
   complete intake can approve preparation scope while those assets are missing;
   a downstream spec cannot consume missing or unapproved inputs.
4. If finishing is selected, draft the composition brief now. Store narration,
   timing and text-safe requirements there; intake points to it rather than
   restating them. This is planning, not execution of composition.
5. Present the complete brief and any early composition brief as a named review
   package. Ask approval of every artifact/version and allowed action. Keep
   `status: draft` until explicit approval, then record `status: approved` only.
6. Hand off only selected work using the shared rules. Do not run a missing
   preparation task or any paid/external step on the strength of this contract.

## Outputs
- `runs/studio/<production>/00-intake-N.md` — route, production purpose and scope.
- `runs/studio/<production>/00-composition-N.md` — only when finishing is selected.
  Paths are workspace-relative; N identifies a new immutable approved version.

## Human check
The operator can explain the next step, what is reused, what is missing and
what this approval permits. No unanswered scope blocker remains. Hermes is the
producer/first reviewer and Jordan the human approver unless explicitly
reassigned; self-review is not independent. Approved intake selects a route;
it does not approve future specifications, media outputs or publication.
