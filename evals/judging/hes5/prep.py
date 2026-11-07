"""Write the contestant inputs (text + genre only, no facts). Usage: prep.py [dev|locked] (dev -> runs/hes5/inputs, locked -> runs/locked/inputs). Prints counts only."""
import pathlib, re, sys
SPLIT = sys.argv[1] if len(sys.argv) > 1 else "dev"
E = pathlib.Path(__file__).resolve().parents[2]
out = E / "runs" / ("hes5" if SPLIT == "dev" else "locked") / "inputs"; out.mkdir(parents=True, exist_ok=True)
def parse(p):
    t = p.read_text(); m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    meta = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l)
    return meta, m.group(2).strip()
files = sorted((E / SPLIT / "texts").glob("*.md")) + sorted((E / SPLIT / "human").glob("*.md"))
for p in files:
    meta, body = parse(p)
    (out / p.name).write_text(f"Tipo de texto: {meta['genre']}\n\n{body}\n")
print(len(files), "inputs ->", out.relative_to(E))
