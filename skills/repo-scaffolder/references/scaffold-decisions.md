# Proportional scaffold decisions

Treat these as conditional options, not a file checklist.

| Project evidence or need | Smallest useful addition | Avoid |
| --- | --- | --- |
| New Python/FastAPI backend | `app/__init__.py`, runnable entry point, package config, one smoke test, documented run/check commands | empty layer directories |
| Existing Python/FastAPI backend without `app/` | initialize only `app/__init__.py`, clarify its role | moving working entry points without import/deploy verification |
| Existing `src/<package>` with established imports | keep it, initialize empty `app/` if missing, discuss migration if requested | wiring two competing entry points |
| Repeated repository-specific workflow | local skill with actionable steps and links | one skill per folder or generic global guidance copied locally |
| Important architecture decision | short ADR with rationale and consequences | retroactive fictional history |
| Separate backend/frontend/infra conventions | scoped `AGENTS.md` as needed | unconditional files for every subtree |
| Lint/typecheck/test tools already in use | shared, repeatable check command and matching CI | claiming success for uninstalled tools |
| RAG or agent behavior that can regress | small eval dataset, runner, explicit pass criteria | `evals/` with empty placeholder cases |

For new apps, keep the initial `README.md` concrete: setup, environment variables without real credentials, local run, and checks. Add docs when a newcomer cannot infer a consequential boundary from code and manifests. For existing apps, improve current docs rather than writing parallel versions.

Prefer an `app/` package for new FastAPI backends, but let the repository's packaging and deployment determine its exact entry point. For existing Python/FastAPI projects, initialize `app/__init__.py` if absent while keeping established `src/` code in place. A request to migrate justifies changing paths; update imports, tests, Docker/CI/start commands, and deployment together.

If a `project.yaml` or similar manifest has no generator or independent consumer, leave it out. If a project explicitly needs regeneration, define the schema, ownership, regeneration command, and which generated files must not be edited by hand. Do not establish two sources of truth.

Examples of a compact root `AGENTS.md`:

```md
# Repository guidance

- Source code: `app/`. Run: `python -m uvicorn app.main:app --reload`.
- Check: `python scripts/check.py`; CI runs the same command.
- For changes to persistence, read `docs/database.md` when present.
- Update affected docs and local skills only when their instructions become stale.
```

Only emit commands and paths that really exist and work in the target repository.
