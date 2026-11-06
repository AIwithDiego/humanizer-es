"""Generate the AI texts for HES-4: every brief once by GPT (codex) and once by Claude (API).

Writes evals/<split>/raw/<id>-<model>.md (the reply minus wrapper lines); tools/extract.py
then pulls out the one text a user would paste into evals/<split>/texts/. Prints only counts and paths, never text,
so a locked run can be done without anyone reading it.

Usage: python3 evals/tools/generate.py [--only dev|locked] [--model gpt|claude]
Needs ANTHROPIC_API_KEY in the environment and codex logged in.
"""
import argparse, json, os, pathlib, re, subprocess, sys, tempfile, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

EVALS = pathlib.Path(__file__).resolve().parent.parent
CLAUDE_MODEL = "claude-sonnet-5-5"
GPT_MODEL = "gpt-6-astra"

WRAP_HEAD = re.compile(r"^\s*(¡?claro|¡?por supuesto|aquí (tienes|te dejo|va)|te dejo|perfecto|¡?listo|acá (tienes|te dejo|va)|sure|here)\b.*$", re.I)
WRAP_TAIL = re.compile(r"^\s*(¿(quieres|te gustaría|prefieres|necesitas)|si (quieres|necesitas|me dices|prefieres|te sirve)|puedo (ajustar|adaptar|hacer)|también puedo|nota:|\*?\*?tip)", re.I)


def strip_wrapper(text: str) -> tuple[str, int]:
    lines = text.strip().splitlines()
    removed = 0
    while lines and (WRAP_HEAD.match(lines[0]) or lines[0].strip() in ("", "---", "```", "```text", "```markdown")):
        lines.pop(0); removed += 1
    while lines and (WRAP_TAIL.match(lines[-1]) or lines[-1].strip() in ("", "---", "```")):
        lines.pop(); removed += 1
    return "\n".join(lines).strip() + "\n", removed


def run_gpt(prompt: str) -> str:
    """Codex with a throwaway home: no AGENTS.md, memories, skills, apps or plugins."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        home, codex_home, cwd = tmp / "home", tmp / "codex", tmp / "cwd"
        for d in (home, codex_home, cwd):
            d.mkdir()
        (codex_home / "auth.json").symlink_to(pathlib.Path.home() / ".codex" / "auth.json")
        (codex_home / "config.toml").write_text(f'model = "{GPT_MODEL}"\nmodel_reasoning_effort = "medium"\n')
        out = tmp / "out.txt"
        env = {**os.environ, "HOME": str(home), "CODEX_HOME": str(codex_home)}
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only", "--ephemeral",
               "--disable", "apps", "--disable", "plugins", "--disable", "remote_plugin",
               "-o", str(out), prompt]
        subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, timeout=600, check=True)
        return out.read_text()


def run_claude(prompt: str) -> str:
    body = json.dumps({"model": CLAUDE_MODEL, "max_tokens": 2000,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
        "content-type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                data = json.load(r)
            return "".join(b.get("text", "") for b in data["content"])
        except Exception:
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


def job(split: str, brief: dict, model: str) -> str:
    path = EVALS / split / "raw" / f"{brief['id']}-{model}.md"
    if path.exists():
        return f"skip {path.relative_to(EVALS)}"
    raw = run_gpt(brief["prompt"]) if model == "gpt" else run_claude(brief["prompt"])
    text, removed = strip_wrapper(raw)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\nid: {brief['id']}\ngenre: {brief['genre']}\nsplit: {split}\n"
        f"source: {GPT_MODEL if model == 'gpt' else CLAUDE_MODEL}\n"
        f"prompt: {json.dumps(brief['prompt'], ensure_ascii=False)}\n"
        f"facts: {json.dumps(brief['facts'], ensure_ascii=False)}\n"
        f"wrapper_lines_stripped: {removed}\n---\n\n{text}")
    return f"ok   {path.relative_to(EVALS)} ({len(text.split())} words, {removed} wrapper lines)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["dev", "locked"])
    ap.add_argument("--model", choices=["gpt", "claude"])
    a = ap.parse_args()
    briefs = {b["id"]: b for b in json.loads((EVALS / "briefs.json").read_text())}
    split = json.loads((EVALS / "split.json").read_text())
    jobs = [(s, briefs[i], m) for s, ids in split.items() if s != "human" and a.only in (None, s)
            for i in ids for m in ("gpt", "claude") if a.model in (None, m)]
    failed = 0
    with ThreadPoolExecutor(6) as pool:
        for fut in [pool.submit(job, *j) for j in jobs]:
            try:
                print(fut.result(), flush=True)
            except Exception as e:
                failed += 1
                print(f"FAIL {type(e).__name__}: {str(e)[:200]}", flush=True)
    print(f"done: {len(jobs) - failed}/{len(jobs)}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
