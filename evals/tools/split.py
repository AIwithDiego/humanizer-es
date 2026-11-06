"""Assign briefs to dev / locked: one brief per genre in each, seeded so it can be re-derived."""
import json, random, pathlib
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent.parent
briefs = json.loads((HERE / "briefs.json").read_text())
rng = random.Random(20261106)
by_genre = defaultdict(list)
for b in briefs:
    by_genre[b["genre"]].append(b["id"])
split = {"dev": [], "locked": []}
for genre in sorted(by_genre):
    ids = sorted(by_genre[genre])
    rng.shuffle(ids)
    split["dev"].append(ids[0]); split["locked"].append(ids[1])
split = {k: sorted(v) for k, v in split.items()}
(HERE / "split.json").write_text(json.dumps(split, indent=1) + "\n")
print(json.dumps(split))

# Human controls (added once the pool existed): pairs of similar texts, one of each pair per side.
pairs = [("h01", "h02"), ("h03", "h04"), ("h06", "h07"), ("h05", "h08")]
hum = {"dev": [], "locked": []}
for p in pairs:
    p = list(p); rng.shuffle(p)
    hum["dev"].append(p[0]); hum["locked"].append(p[1])
split["human"] = {k: sorted(v) for k, v in hum.items()}
(HERE / "split.json").write_text(json.dumps(split, indent=1) + "\n")
print(json.dumps(split["human"]))
