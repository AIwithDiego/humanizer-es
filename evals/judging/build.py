import re, random, json, sys
runs = sys.argv[1]; out = sys.argv[2]; inputs = sys.argv[3]
def split(path):
    t = open(path).read()
    parts = re.split(r'^## (\d+)\s*$', t, flags=re.M)
    return {int(parts[i]): parts[i+1].strip() for i in range(1, len(parts), 2)}
src = open(inputs).read()
srcparts = re.split(r'^## (\d+) · .*$', src, flags=re.M)
orig = {int(srcparts[i]): srcparts[i+1].strip() for i in range(1, len(srcparts), 2)}
cont = {k: split(f"{runs}/{k}.md") for k in "ABCDE"}
rng = random.Random(611)
key = {}; packet = []
for n in range(1, 10):
    order = list("ABCDE"); rng.shuffle(order)
    key[n] = {f"V{i+1}": c for i, c in enumerate(order)}
    packet.append(f"# Text {n}\n\n### ORIGINAL (with facts line)\n\n{orig[n]}\n")
    for i, c in enumerate(order):
        packet.append(f"### V{i+1}\n\n{cont[c].get(n, '(missing)')}\n")
open(f"{out}/packet.md", "w").write("\n".join(packet))
json.dump(key, open(f"{out}/key.json", "w"), indent=1)
print("ok", {k: len(v) for k, v in cont.items()})
