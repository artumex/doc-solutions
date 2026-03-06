import os
import yaml

solutions_dir = "docs/solutions"
nav_entries = []

if os.path.exists(solutions_dir):
    for filename in sorted(os.listdir(solutions_dir)):
        if filename.endswith(".md"):
            label = filename.replace(".md", "").replace("-", " ").title()
            nav_entries.append({label: f"solutions/{filename}"})

with open("mkdocs.yml", "r") as f:
    config = yaml.safe_load(f)

config["nav"] = [
    {"Home": "docs/index.md"},
    {"Solutions": nav_entries},
    {"Tags": "docs/tags.md"},
]

with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, allow_unicode=True, sort_keys=False)

print(f"✅ Nav generated for {len(nav_entries)} solutions.")
