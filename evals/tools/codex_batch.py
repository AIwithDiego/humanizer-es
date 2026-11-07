"""Run Codex (GPT) on many texts at once, isolated from any personal setup.

For each <id>.brief.txt in DIR (the prompt) with a matching <id>.in.txt (sent on stdin),
writes <id>.out.txt. Existing outputs are skipped. Prints one status line per id.

Usage: python3 evals/tools/codex_batch.py DIR [--workers 6] [--effort medium]
"""
import argparse, os, pathlib, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

GPT_MODEL = "gpt-6-astra"


def run(brief: str, stdin: str, effort: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        home, codex_home, cwd = tmp / "home", tmp / "codex", tmp / "cwd"
        for d in (home, codex_home, cwd):
            d.mkdir()
        (codex_home / "auth.json").symlink_to(pathlib.Path.home() / ".codex" / "auth.json")
        (codex_home / "config.toml").write_text(f'model = "{GPT_MODEL}"\nmodel_reasoning_effort = "{effort}"\n')
        out = tmp / "out.txt"
        env = {**os.environ, "HOME": str(home), "CODEX_HOME": str(codex_home)}
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only", "--ephemeral",
               "--disable", "apps", "--disable", "plugins", "--disable", "remote_plugin", "-o", str(out), brief]
        subprocess.run(cmd, cwd=cwd, env=env, input=stdin, text=True, capture_output=True, timeout=900, check=True)
        return out.read_text()


def job(d: pathlib.Path, i: str, effort: str) -> str:
    dst = d / f"{i}.out.txt"
    if dst.exists() and dst.stat().st_size:
        return f"skip {i}"
    err = "empty output"
    for attempt in range(2):
        try:
            txt = run((d / f"{i}.brief.txt").read_text(), (d / f"{i}.in.txt").read_text(), effort)
            if txt.strip():
                dst.write_text(txt)
                return f"ok   {i}"
        except Exception as e:
            err = f"{type(e).__name__}: {str(e)[:150]}"
    return f"FAIL {i} {err}"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("dir"); ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--effort", default="medium"); a = ap.parse_args()
    d = pathlib.Path(a.dir)
    ids = sorted(p.name[:-len(".brief.txt")] for p in d.glob("*.brief.txt"))
    with ThreadPoolExecutor(a.workers) as pool:
        res = list(pool.map(lambda i: job(d, i, a.effort), ids))
    for r in res: print(r)
    bad = sum(r.startswith("FAIL") for r in res)
    print(f"done: {len(ids) - bad}/{len(ids)}"); sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
