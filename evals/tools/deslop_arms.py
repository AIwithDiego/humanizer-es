"""Score the dev AI originals and each contestant's rewrites with tools/deslop_es.py.
Usage: python3 evals/tools/deslop_arms.py"""
import sys, pathlib, collections
R = pathlib.Path(__file__).resolve().parents[2]; sys.path.insert(0, str(R / "tools")); import deslop_es as d
E = R / "evals"; ids = [p.stem for p in sorted((E / "dev/texts").glob("*.md"))]
arms = {"AI original": "dev/texts", "v1.3 + 2nd": "runs/hes6-v13/A2", "v1.2 + 2nd": "runs/hes5/A2",
        "omelyanchuk": "runs/hes5/B", "alvaromieres9": "runs/hes5/C", "madebydiego": "runs/hes5/D",
        "blader + Codex": "runs/hes5/E", "prompt v1 GPT": "runs/hes7/Pg", "plain ask GPT": "runs/hes7/Qg",
        "prompt v1 Claude": "runs/hes7/Pc", "plain ask Claude": "runs/hes7/Qc",
        "prompt v2 GPT": "runs/hes10/Pg", "prompt v2 Claude": "runs/hes10/Pc"}
print(f"{'':18}{'avg':>6}{'clean':>8}  tells left (by rule)")
for a, p in arms.items():
    files = [E / p / f"{i}.md" for i in ids if (E / p / f"{i}.md").exists()]
    if not files: continue
    sc, labs = [], collections.Counter()
    for f in files:
        h = d.audit(f.read_text()); sc.append(d.score(h))
        labs.update(l.split(" (")[0] for k, v in h.items() if k != "notas" for l, _ in v)
    print(f"{a:18}{sum(sc)/len(sc):6.2f}{sc.count(5):5}/{len(sc)}  " + ", ".join(f"{l} {n}" for l, n in labs.most_common(5)))
