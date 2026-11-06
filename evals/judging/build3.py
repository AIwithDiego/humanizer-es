import re, random, json, sys
import pathlib; E = str(pathlib.Path(__file__).resolve().parents[1]); out = sys.argv[1]
def split(path):
    t = open(path).read(); parts = re.split(r'^## (\d+)\s*$', t, flags=re.M)
    return {int(parts[i]): parts[i+1].strip() for i in range(1, len(parts), 2)}
def srcs(path):
    t = open(path).read(); parts = re.split(r'^## (\d+) · .*$', t, flags=re.M)
    return {int(parts[i]): parts[i+1].strip() for i in range(1, len(parts), 2)}
orig = srcs(f"{E}/inputs-holdout2.md")
r1 = {}
r2 = {k: split(f"{E}/runs/r3/{k}.md") for k in "ABCDE"}
def get(c, n): return r2[c][n]
rng = random.Random(2126); key = {}; packet = []
for n in range(21, 27):
    order = list("ABCDE"); rng.shuffle(order); key[n] = {f"V{i+1}": c for i, c in enumerate(order)}
    packet.append(f"# Text {n}\n\n### ORIGINAL (with facts line)\n\n{orig[n]}\n")
    for i, c in enumerate(order): packet.append(f"### V{i+1}\n\n{get(c, n)}\n")
open(f"{out}/packet.md", "w").write("\n".join(packet)); json.dump(key, open(f"{out}/key.json", "w"), indent=1)
print("ok")
