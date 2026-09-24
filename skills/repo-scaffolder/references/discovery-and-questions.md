# Discovery and focused questions

## Inspect before asking

Check the working tree and the instructions applying to the target. Sample the project files relevant to the request: `pyproject.toml`, lockfiles, `package.json`, `Dockerfile`, compose files, `app/` or `src/`, tests, CI, deployment files, `README.md`, `docs/`, `.agents/skills/`, and local verification scripts. Inspect code to distinguish intended architecture from merely empty directories. On an existing repo, record the current entry point, import path, test command, deployment command, and uncommitted changes before changing them.

Build a small internal decision table:

| Decision | Evidence | Status | Impact if wrong |
| --- | --- | --- | --- |
| Runtime and framework | User / manifest / source | known / inferred / unknown | imports and tooling |
| Source layout | imports / build / deployment | known / inferred / unknown | migration and packaging |
| Data and identity | code / requirements | known / inferred / unknown | data model and security |
| Delivery target | pipeline / user | known / inferred / unknown | deployment and CI |
| Verification | scripts / CI / tests | known / inferred / unknown | runnable checks |

Do not create this table as a file unless the user needs it. An existing repository can be inconsistent: report the mismatch instead of pretending a README overrides running code.

## Decide whether to ask

Ask when **both** conditions hold: the answer is absent or contradictory, and choosing incorrectly would cause substantial rework, unsafe defaults, or a different externally visible behavior. Group at most a few high-impact questions; use a recommended default and explain its tradeoff. Continue independent inspection while awaiting an answer if possible.

Examples:

- “FastAPI API with documents” and no persistence plan: ask whether documents live in object storage, a database, or both before generating persistence code.
- Authentication or tenancy not specified for sensitive resources: ask who may access them and whether the project already has an identity provider.
- User asks for CI but repo has no hosting provider or existing CI: ask only if choosing a provider is necessary; otherwise create a local check script and defer CI.
- User says only “improve this repo”: inspect first, implement clearly justified reversible improvements, and ask about architecture only if changes would conflict with a real convention.
- Do **not** ask about formatter line length, a module filename, or naming that can be inferred or chosen safely.

When answers are unavailable, write the portions that remain valid, call out the unresolved decision, and avoid scaffolding dependent components. Never treat elapsed time as approval.
