#!/usr/bin/env python3
"""Structure checks CI runs on every push: plugin manifests, the skill's front matter,
versions in sync, and no em or en dashes in the READMEs and changelog (the skill bans them)."""
import json, pathlib, re, sys

R = pathlib.Path(__file__).resolve().parents[1]
errors = []

market = json.loads((R / ".claude-plugin/marketplace.json").read_text())
plugin = json.loads((R / ".claude-plugin/plugin.json").read_text())
if [p["name"] for p in market["plugins"]] != [plugin["name"]]:
    errors.append("marketplace.json and plugin.json name different plugins")

skill = (R / "skills/humanizer-es/SKILL.md").read_text()
m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
if not m:
    errors.append("SKILL.md has no front matter")
else:
    fm = m.group(1)
    for key in ("name: humanizer-es", "description: ", "license: MIT"):
        if key not in fm:
            errors.append(f"SKILL.md front matter lacks '{key.strip()}'")
    v = re.search(r'version: "([\d.]+)"', fm)
    if not v or v.group(1) != plugin["version"]:
        errors.append(f"SKILL.md version {v and v.group(1)} != plugin.json {plugin['version']}")

for f in ("README.md", "README.es.md", "CHANGELOG.md"):  # prompt.md names the dashes it bans
    if re.search("[—–]", (R / f).read_text()):
        errors.append(f"{f} has an em or en dash")

if "Texto:" not in (R / "prompt.md").read_text():
    errors.append("prompt.md lost its 'Texto:' line")

print("\n".join(errors) or "structure ok")
sys.exit(1 if errors else 0)
