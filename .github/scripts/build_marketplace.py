"""Build individual Codex skills and topic bundles from the upstream library."""

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "nonprofit-skills-library" / "skills"
GENERATED = ROOT / "plugins" / "nonprofit-skills"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


TOPIC_NAMES = {
    "advocacy-policy": "Advocacy & Public Policy",
    "communications-marketing": "Communications & Marketing",
    "faith-based": "Faith-Based Organizations",
    "finance-operations": "Finance & Operations",
    "fundraising-development": "Fundraising & Development",
    "governance-compliance": "Governance & Compliance",
    "programs-impact": "Programs & Impact",
    "retail-operations": "Retail & Resale Operations",
    "strategy-growth": "Strategy & Growth",
    "technology-data": "Technology & Data",
    "volunteer-people": "Volunteer & People Management",
}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def validate_skill(source):
    if not re.fullmatch(r"nonprofit-[a-z0-9]+(?:-[a-z0-9]+)*", source.parent.name):
        raise ValueError(f"Invalid skill directory name: {source.parent}")
    if source.parent.is_symlink() or any(path.is_symlink() for path in source.parent.rglob("*")):
        raise ValueError(f"Symlinks are not supported in skill packages: {source.parent}")


def skill_title(source):
    markdown = source.read_text(encoding="utf-8-sig")
    heading = re.search(r"^# (.+)$", markdown, flags=re.MULTILINE)
    if heading:
        return heading.group(1).strip()
    return source.parent.name.removeprefix("nonprofit-").replace("-", " ").title()


def package_plugin(output, name, title, description, sources):
    plugin = output / name
    for source in sources:
        shutil.copytree(source.parent, plugin / "skills" / source.parent.name)
    shutil.copyfile(ROOT / "LICENSE", plugin / "LICENSE")
    write_json(plugin / "plugin.json", {
        "$schema": PLUGIN_SCHEMA,
        "name": name,
        "version": "0.1.0",
        "description": description,
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
    names = {source.parent.name for source in sources}
    if len(names) != len(sources):
        raise ValueError("Skill folder names must be unique across categories")

    topics = defaultdict(list)
    for source in sources:
        validate_skill(source)
        topics[source.parent.parent.name].append(source)

    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=GENERATED.parent) as temporary:
        packages = Path(temporary) / "packages"
        entries = []
        for topic, topic_sources in sorted(topics.items()):
            name = f"nonprofit-bundle-{topic}"
            if name in names:
                raise ValueError(f"A skill and a bundle share the name {name}")
            label = TOPIC_NAMES.get(topic, topic.replace("-", " ").title())
            count = len(topic_sources)
            noun = "skill" if count == 1 else "skills"
            entries.append(package_plugin(
                packages, name, f"{label} Bundle",
                f"Includes {count} nonprofit {noun} for {label}.", topic_sources,
            ))
        for source in sources:
            title = skill_title(source)
            entries.append(package_plugin(packages, source.parent.name, title, title, [source]))
        if GENERATED.exists():
            shutil.rmtree(GENERATED)
        packages.rename(GENERATED)

    MARKETPLACE.parent.mkdir(parents=True, exist_ok=True)
    write_json(MARKETPLACE, {
        "name": "nonprofit-skills-marketplace",
        "interface": {"displayName": "Nonprofit Skills Marketplace"},
        "plugins": entries,
    })
    print(f"Built {len(topics)} topic bundles and {len(sources)} individual plugins")


if __name__ == "__main__":
    main()
