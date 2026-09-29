# 02_render, send the prompt, save the image, check drift

1 job: turn 1 approved spec into 1 image and 1 render record holding the drift
findings, per character.

## Inputs
- Working (this run): the highest-numbered `../runs/<set>/<shot>/01-spec-N.md`
  (requires `status: approved`)
- Reference (every run): the spec's frozen **World-input manifest**,
  `../_reference/drift-checklist.md`, `../_reference/host.md`

Do NOT load: `../world/interview.md`; `../world/style.md` and
`../_reference/spec-rules.md`, the prompt is fixed at this point;
`../_reference/setup-interview.md`; any other shot under `../runs/<set>/`.

## Process
1. Refuse to run unless the spec says `status: approved`.
2. Verify every manifest input is still approved and has the recorded SHA-256;
   refuse if any changed. Send the spec's **Prompt** section, unchanged, to the
   image tool `host.md` names. Save the result as
   `../runs/<set>/<shot>/02-image-N.<ext>`, N
   matching the spec.
3. Write the render record: the prompt as sent, then every metadata field
   `host.md` lists, `not exposed` where the tool returns none.
4. Walk `drift-checklist.md` against the image: the spec's **At risk** items
   first, then every invariant of each named character, then the environment.
   Write 1 finding per line: `holds`, `drifted: <what moved>`, or
   `cannot see: <why>`.
5. Leave `verdict:` empty. The operator writes it.

## Outputs
- `../runs/<set>/<shot>/02-image-N.<ext>`
- `../runs/<set>/<shot>/02-render-N.md`, frontmatter: `set`, `shot`, `attempt`,
  `stage: 02_render`, `status: draft`, `verdict` (empty | `accepted` |
  `drifted`), `generated`, `sources`; body: **Prompt as sent**,
  **Tool metadata**, **Findings**, **Drift notes**

## Human check
Put the image beside the spec and its selected frozen inputs, and walk the drift
checklist line by line, **At risk** items first. The operator may accept or
reject the render by editing the record or by clear chat approval naming it;
after that approval, the agent records `verdict: accepted` and `status:
approved`, or records `verdict: drifted` with the operator's drift notes and
starts `01_spec` again.
