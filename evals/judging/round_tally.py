"""Tally a judging round: Claude judges, GPT judges and combined; AI texts and human controls apart.

Reads ROUND/config.json, ROUND/key.json and ROUND/judges/<family>-<persona>-<packet>.json.
Usage: python3 evals/judging/round_tally.py ROUND
"""
import collections, difflib, glob, json, pathlib, re, sys
E = pathlib.Path(__file__).resolve().parents[1]; HERE = pathlib.Path(sys.argv[1]).resolve()
CFG = json.load(open(HERE / "config.json"))
key = json.load(open(HERE / "key.json"))
NAMES = CFG["names"]
verdicts = []  # (family, text_no, arm, scores, rank)
for f in sorted(glob.glob(str(HERE / "judges" / "*.json"))):
    fam = pathlib.Path(f).name.split("-")[0]
    for n, v in json.load(open(f)).items():
        m = key[n]
        shared = sum(sc["faithful"] <= 5 for sc in v["scores"].values()) >= len(NAMES) - 1  # the original's gap, not the skill's
        for pos, lab in enumerate(v["rank"], 1):
            verdicts.append((fam, n, m[lab], {**v["scores"][lab], "shared": shared}, pos))

def table(rows, title):
    agg = collections.defaultdict(lambda: collections.defaultdict(list))
    for fam, n, arm, s, pos in rows:
        for k in ("human", "faithful", "useful"): agg[arm][k].append(s[k])
        agg[arm]["rank"].append(pos); agg[arm]["win"].append(pos == 1); agg[arm]["err"].append(s["faithful"] <= 5); agg[arm]["own"].append(s["faithful"] <= 5 and not s["shared"])
    print(f"\n{title}  ({len(rows) // len(NAMES)} verdicts)")
    print(f"{'skill':22}{'human':>7}{'faith':>7}{'useful':>7}{'rank':>7}{'wins':>6}{'fact err':>10}{'own err':>9}")
    for arm in sorted(agg, key=lambda a: sum(agg[a]["rank"]) / len(agg[a]["rank"])):
        a = agg[arm]; avg = lambda k: sum(a[k]) / len(a[k])
        print(f"{NAMES[arm]:22}{avg('human'):7.1f}{avg('faithful'):7.1f}{avg('useful'):7.1f}{avg('rank'):7.2f}"
              f"{sum(a['win']):6}{sum(a['err']):6}/{len(a['err'])}{sum(a['own']):6}/{len(a['own'])}")

is_h = lambda n: key[n]["file"].startswith("h")
for fam in ("claude", "gpt", None):
    sel = [r for r in verdicts if fam in (None, r[0])]
    label = {"claude": "CLAUDE JUDGES", "gpt": "GPT JUDGES", None: "COMBINED"}[fam]
    table([r for r in sel if not is_h(r[1])], f"{label} · AI texts")
    table([r for r in sel if is_h(r[1])], f"{label} · human controls")

print("\nHuman controls, how much of the original survives (difflib ratio, 1.00 = untouched):")
inputs = E / CFG.get("inputs", "runs/hes5/inputs")
for h in sorted({key[n]["file"] for n in key if is_h(n)}):
    orig = inputs.joinpath(h + ".md").read_text().split("\n", 2)[2]
    row = {a: difflib.SequenceMatcher(None, orig, (E / CFG["arms"][a] / f"{h}.md").read_text()).ratio() for a in NAMES}
    print(h, "  ".join(f"{NAMES[a][:10]} {r:.3f}" for a, r in row.items()))
