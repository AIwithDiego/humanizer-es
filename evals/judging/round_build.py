"""Blind judging packets for the dev set. Six versions per text, labels shuffled per text.

ROUND/config.json: {"split": "dev"|"locked" (default dev), "arms": {"A2": "runs/hes5/A2", ...}, "names": {...}, "seed": 20261107}.
Writes packet-1.md / packet-2.md (17 texts each) to OUT (outside the repo while judging,
so judges can't reach key.json) and key.json in ROUND.
Usage: python3 evals/judging/round_build.py ROUND OUT
"""
import json, pathlib, random, re, sys
E = pathlib.Path(__file__).resolve().parents[1]; HERE = pathlib.Path(sys.argv[1]).resolve()
OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
CFG = json.load(open(HERE / "config.json")); ARMS = list(CFG["arms"])
PATH = {a: E / p for a, p in CFG["arms"].items()}
def parse(p):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", p.read_text(), re.S)
    meta = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l)
    return meta, m.group(2).strip()
SPLIT = CFG.get("split", "dev")
srcs = sorted((E / SPLIT / "texts").glob("*.md")) + sorted((E / SPLIT / "human").glob("*.md"))
rng = random.Random(CFG.get("seed", 20261107)); key = {}; blocks = []
missing = [f"{a}/{p.name}" for p in srcs for a in ARMS if not (PATH[a] / p.name).exists()]
if missing: sys.exit(f"missing outputs: {missing}")
for n, p in enumerate(srcs, 1):
    meta, body = parse(p); facts = json.loads(meta["facts"]) if meta["facts"].startswith('"') else meta["facts"]
    order = ARMS[:]; rng.shuffle(order)
    key[str(n)] = {"file": p.stem, **{f"V{i+1}": a for i, a in enumerate(order)}}
    b = [f"# Text {n}\n\nGenre: {meta['genre']}\n\n### ORIGINAL\n\n{body}\n\nFacts: {facts}\n"]
    for i, a in enumerate(order):
        b.append(f"### V{i+1}\n\n{(PATH[a] / p.name).read_text().strip()}\n")
    blocks.append("\n".join(b))
half = (len(blocks) + 1) // 2
(OUT / "packet-1.md").write_text("\n\n".join(blocks[:half]))
(OUT / "packet-2.md").write_text("\n\n".join(blocks[half:]))
json.dump(key, open(HERE / "key.json", "w"), indent=1)
print(f"{len(blocks)} texts, packets in {OUT}, key.json written")
