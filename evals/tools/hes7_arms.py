"""HES-7 arms: prompt.md vs a plain ask, each pasted into GPT (Codex) and Claude (API).

The message is what a user would paste: the instruction, then the text (no genre line).
Raw replies go to runs/hes7/<arm>/raw/; extract.py's verbatim check then pulls out the one
text a user would copy (prompt.md asks for a short "what I changed" note under it).

Usage: python3 evals/tools/hes7_arms.py [gen|extract] [--out runs/hes7] [--prompt prompt.md] [--arms Pg,Qg,Pc,Qc]
(needs ANTHROPIC_API_KEY, codex logged in)
"""
import argparse, json, pathlib, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generate, extract

E = pathlib.Path(__file__).resolve().parents[1]; ROOT = E.parent
OUT = E / "runs" / "hes7"
PLAIN = "Haz que este texto suene más humano, que no parezca escrito por una IA:\n\n"
ARMS = {"Pg": ("prompt", "gpt"), "Qg": ("plain", "gpt"), "Pc": ("prompt", "claude"), "Qc": ("plain", "claude")}


def message(kind, text):
    head = (ROOT / A.prompt).read_text().rstrip() + "\n\n" if kind == "prompt" else PLAIN
    return head + text


def inputs():
    for p in sorted((E / A.inputs).glob("*.md")):
        yield p.stem, p.read_text().split("\n", 2)[2].strip()  # drop "Tipo de texto:" line


def gen():
    jobs = [(arm, i, t) for arm in A.arms.split(",") for i, t in inputs()]
    def one(j):
        arm, i, t = j; kind, model = ARMS[arm]
        dst = OUT / arm / "raw" / f"{i}.md"
        if dst.exists(): return f"skip {arm}/{i}"
        msg = message(kind, t)
        try:
            reply = generate.run_gpt(msg) if model == "gpt" else claude(msg)
        except Exception as e:
            return f"FAIL {arm}/{i} {type(e).__name__}"
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(f"---\nprompt: {json.dumps(msg, ensure_ascii=False)}\n---\n\n{reply.strip()}\n")
        return f"ok   {arm}/{i}"
    with ThreadPoolExecutor(8) as pool:
        res = list(pool.map(one, jobs))
    print("\n".join(r for r in res if not r.startswith("ok")) or "all ok", f"\n{sum(r.startswith('ok') for r in res)} new")


def claude(msg):
    body = json.dumps({"model": generate.CLAUDE_MODEL, "max_tokens": 6000,
                       "messages": [{"role": "user", "content": msg}]}).encode()
    import os, urllib.request, time
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01", "content-type": "application/json"})
    for a in range(4):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.load(r)
            if d.get("stop_reason") == "max_tokens": raise RuntimeError("cut off")
            return "".join(b.get("text", "") for b in d["content"])
        except Exception:
            if a == 3: raise
            time.sleep(5 * (a + 1))


def ext():
    bad = 0
    for src in sorted(OUT.glob("*/raw/*.md")):
        dst = src.parent.parent / src.name
        if dst.exists(): continue
        _, front, raw = src.read_text().split("---\n", 2); raw = raw.strip()
        prompt = json.loads(front.splitlines()[0][8:])
        out = extract.call(extract.INSTRUCTION.format(prompt=prompt, raw=raw)).strip()
        raw_lines = {l.strip() for l in raw.splitlines()}
        missing = [l for l in out.splitlines() if l.strip() and l.strip() not in raw_lines]
        if missing or not out:
            bad += 1; print(f"REFUSED {src.relative_to(E)}"); continue
        dst.write_text(out + "\n")
    print("extract done, refused:", bad)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["gen", "extract"])
    ap.add_argument("--out", default="runs/hes7"); ap.add_argument("--prompt", default="prompt.md")
    ap.add_argument("--arms", default="Pg,Qg,Pc,Qc"); ap.add_argument("--inputs", default="runs/hes5/inputs"); A = ap.parse_args()
    OUT = E / A.out
    {"gen": gen, "extract": ext}[A.cmd]()
