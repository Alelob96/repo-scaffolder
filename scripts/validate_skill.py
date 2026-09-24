"""Validate the portable repo-scaffolder skill using only the standard library."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "repo-scaffolder"
MANIFEST = SKILL / "SKILL.md"


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.is_file():
        print(f"ERROR: missing {MANIFEST}", file=sys.stderr)
        return 1
    source = MANIFEST.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(?P<header>.*?)\n---\n", source, re.DOTALL)
    if match is None:
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        header = match.group("header")
        if not re.search(r"(?m)^name: repo-scaffolder$", header):
            errors.append("frontmatter name must be repo-scaffolder")
        if not re.search(r"(?m)^description: \S.+$", header):
            errors.append("frontmatter description is required")
    if len(source.splitlines()) > 500:
        errors.append("SKILL.md exceeds the 500-line limit")
    for required in (SKILL / "agents" / "openai.yaml", ROOT / "README.md", ROOT / "AGENTS.md"):
        if not required.is_file():
            errors.append(f"missing {required.relative_to(ROOT)}")
    linked = re.findall(r"\[[^]]+\]\((references/[^)]+\.md)\)", source)
    linked_paths = {SKILL / path for path in linked}
    for path in linked_paths:
        if not path.is_file():
            errors.append(f"missing linked reference: {path.relative_to(SKILL)}")
    references = set((SKILL / "references").glob("*.md"))
    for path in references - linked_paths:
        errors.append(f"unlinked reference: {path.name}")
    for path in references:
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty reference: {path.name}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in sorted(errors)), file=sys.stderr)
        return 1
    print(f"OK: repo-scaffolder skill, {len(references)} linked references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
