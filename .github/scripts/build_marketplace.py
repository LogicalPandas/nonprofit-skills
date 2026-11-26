"""Build one Codex marketplace entry and plugin package per upstream skill."""

import json
import re
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "nonprofit-skills-library" / "skills"
GENERATED = ROOT / "plugins" / "nonprofit-skills"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def package_skill(source, output):
    name = source.parent.name
    if not re.fullmatch(r"nonprofit-[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError(f"Invalid skill directory name: {source.parent}")
    if source.parent.is_symlink() or any(path.is_symlink() for path in source.parent.rglob("*")):
        raise ValueError(f"Symlinks are not supported in skill packages: {source.parent}")

    title = name.removeprefix("nonprofit-").replace("-", " ").title()
    markdown = source.read_text(encoding="utf-8-sig")
    heading = re.search(r"^# (.+)$", markdown, flags=re.MULTILINE)
    if heading:
        title = heading.group(1).strip()

    plugin = output / name
    shutil.copytree(source.parent, plugin / "skills" / name)
    shutil.copyfile(ROOT / "LICENSE", plugin / "LICENSE")
    write_json(plugin / "plugin.json", {
        "$schema": PLUGIN_SCHEMA,
        "name": name,
        "version": "0.1.0",
        "description": title,
        "license": "MIT",
        "extensions": {"com.openai": {"interface": {"displayName": title}}},
    })
    return {
        "name": name,
        "source": {"source": "local", "path": f"./plugins/nonprofit-skills/{name}"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }


def main():
    sources = sorted(SKILLS.glob("*/*/SKILL.md"))
    if not sources:
        raise ValueError(f"No skill folders found in {SKILLS}")
    names = [source.parent.name for source in sources]
    if len(names) != len(set(names)):
        raise ValueError("Skill folder names must be unique across categories")

    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=GENERATED.parent) as temporary:
        packages = Path(temporary) / "packages"
        entries = [package_skill(source, packages) for source in sources]
        if GENERATED.exists():
            shutil.rmtree(GENERATED)
        packages.rename(GENERATED)

    MARKETPLACE.parent.mkdir(parents=True, exist_ok=True)
    write_json(MARKETPLACE, {
        "name": "nonprofit-skills-marketplace",
        "interface": {"displayName": "Nonprofit Skills Marketplace"},
        "plugins": entries,
    })
    print(f"Built {len(entries)} marketplace entries")


if __name__ == "__main__":
    main()
