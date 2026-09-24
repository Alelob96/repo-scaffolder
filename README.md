# repo-scaffolder

An English-language Agent Skill for bootstrapping new repositories and strengthening existing ones. It inspects the codebase, asks only consequential unanswered questions, and adds proportional source structure, agent guidance, checks, docs, CI, and evals where useful. For new Python/FastAPI projects it starts with an `app/` package.

## Contents

```text
repo-scaffolder/
├── skills/repo-scaffolder/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── scripts/validate_skill.py
└── .github/workflows/validate.yml
```

## Install

```bash
npx skills add Alelob96/repo-scaffolder --skill repo-scaffolder
```

To install into an agent's global scope, append `-g`. To select Codex or Claude Code specifically, use the agent option supported by the installed `skills` CLI. From a local checkout, run `npx skills add ./repo-scaffolder --skill repo-scaffolder` from the parent directory.

This repository contains the **portable skill**. When invoked on a target project, the skill decides which project-local files to create under that project's `app/`, `.agents/skills/`, `docs/`, `scripts/`, and CI paths. It does not copy this repo's layout into every project.

## Validate

```bash
python scripts/validate_skill.py
```

## License

MIT. See [LICENSE](LICENSE).
