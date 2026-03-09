import os
import yaml

solutions_dir = "docs/solutions"
nav_entries = []

if os.path.exists(solutions_dir):
    for filename in sorted(os.listdir(solutions_dir)):
        if filename.endswith(".md"):
            label = filename.replace(".md", "").replace("-", " ").title()
            nav_entries.append({label: f"solutions/{filename}"})

with open("mkdocs.yml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Always include Home and Tags; Solutions section only if entries exist
nav = [{"Home": "index.md"}]
if nav_entries:
    nav.append({"Solutions": nav_entries})
else:
    nav.append({"Solutions": "solutions/_empty.md"})
nav.append({"Tags": "tags.md"})

config["nav"] = nav

with open("mkdocs.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, allow_unicode=True, sort_keys=False)

print(f"✅ Nav generated for {len(nav_entries)} solutions.")
