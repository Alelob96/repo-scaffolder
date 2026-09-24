# Runnable quality gates

The verification entry point should reflect installed tools and the project's real risk. Keep commands independent of the agent: a person and CI should be able to run them unchanged.

1. Identify existing package manager, lockfile, formatter, linter, type checker, test runner, and CI workflow. Preserve existing working conventions.
2. For new Python projects, choose a small compatible tool set only as needed, such as Ruff plus pytest. Add type checking if useful and configured for the actual code. Pin versions through the project's normal dependency and lockfile workflow, not a stale skill template.
3. If a unified `scripts/check.py`, `make check`, or equivalent clarifies usage, have it fail with a nonzero exit code when a command fails, and have CI invoke it. If the repo already has a clean single check command, use it instead of wrapping it.
4. If a check requires external credentials, live infrastructure, paid services, or a container runtime, separate it from fast local checks and document its prerequisites. CI should never pass merely because required tools or tests were silently skipped.
5. Validate generated CI syntax and trigger paths; run local commands that can run here. Do not introduce placeholder jobs that claim to verify nonexistent tests.

For repository-specific constraints, tests or static checks are useful when they catch an actual likely regression: dependency direction, absence of direct DB use in handlers, schema compatibility, or accidental cross-tenant access. Avoid architecture tests that duplicate static imports or freeze filenames without protecting behavior.

For agentic work, select a few realistic cases with expected outcomes and measurable failure conditions: tool selection, evidence use, abstention, permissions, stop bounds, or cost budget. Keep private data out of eval fixtures and make live-model evaluation opt-in when it consumes money or depends on credentials. Report run conditions and variance, not a fabricated deterministic pass.

When introducing a new quality gate in an existing repo, measure its baseline and fix failures attributable to this change. For substantial legacy debt, configure a transparent scoped gate or document the baseline; do not silently reformat the whole codebase or weaken a check until it goes green.
