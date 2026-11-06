import json, sys, glob, collections
J = sys.argv[1]
key = json.load(open(f"{J}/key.json"))
names = {"A":"ours","B":"omelyanchuk","C":"alvaromieres9","D":"madebydiego","E":"blader (EN)"}
tot = collections.defaultdict(lambda: collections.Counter()); wins = collections.Counter(); ranks = collections.defaultdict(list)
per = collections.defaultdict(dict)
for f in sorted(glob.glob(f"{J}/judge*.json")):
    d = json.load(open(f))
    for n, v in d.items():
        m = key[n]
        for lab, s in v["scores"].items():
            c = m[lab]
            for k in ("human","faithful","useful"): tot[c][k] += s[k]
            tot[c]["n"] += 1
        for i, lab in enumerate(v["rank"]):
            ranks[m[lab]].append(i+1)
            per[n].setdefault(m[lab], []).append(i+1)
        wins[m[v["rank"][0]]] += 1
print(f"{'skill':16}{'human':>7}{'faith':>7}{'useful':>7}{'avgrank':>9}{'wins':>6}")
for c in sorted(tot, key=lambda c: sum(ranks[c])/len(ranks[c])):
    t = tot[c]; n = t["n"]
    print(f"{names[c]:16}{t['human']/n:7.1f}{t['faithful']/n:7.1f}{t['useful']/n:7.1f}{sum(ranks[c])/len(ranks[c]):9.2f}{wins[c]:6}")
print("\nper text avg rank:")
for n in sorted(per, key=int):
    print(n, {names[c][:6]: round(sum(r)/len(r),1) for c, r in sorted(per[n].items())})
