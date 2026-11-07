"""Pull out the one text a user would paste from each raw reply (raw/ -> texts/).

Chat models often answer with two versions, a title, tips or keyword lists. A user copies
one text. A small model picks it out verbatim; this script then checks that every line it
returned exists word for word in the raw reply, and refuses the extraction otherwise.
Prints only counts and paths, never text, so the locked set stays unread.

Usage: python3 evals/tools/extract.py [--only dev|locked]
"""
import argparse, json, os, pathlib, sys, time, urllib.request

EVALS = pathlib.Path(__file__).resolve().parent.parent
MODEL = "claude-haiku-5-5"
INSTRUCTION = """Below, between <reply> tags, is a chatbot's answer to this request from a user:
<request>{prompt}</request>

The user will copy one text from it and use it. Return exactly that text, copied verbatim:
- If there are several versions or options, take the first full one.
- Leave out option labels ("Versión corta:", "Opción 1", "Respuesta sugerida:"), tips, advice to the user, keyword lists, notes about the text, and separators.
- Keep everything that belongs to the text itself, including a subject line, greeting, signature, placeholders like [Tu nombre], emojis, hashtags and markdown, exactly as written.
- Do not fix, shorten, reorder or add anything. Output only the text, nothing before or after.

<reply>
{raw}
</reply>"""


def call(prompt: str) -> str:
    body = json.dumps({"model": MODEL, "max_tokens": 4000,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
        "content-type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return "".join(b.get("text", "") for b in json.load(r)["content"])
        except Exception:
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


def split_front(md: str) -> tuple[str, str]:
    _, front, body = md.split("---\n", 2)
    return front, body.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["dev", "locked"])
    a = ap.parse_args()
    bad = 0
    for split in ("dev", "locked"):
        if a.only not in (None, split):
            continue
        for src in sorted((EVALS / split / "raw").glob("*.md")):
            dst = EVALS / split / "texts" / src.name
            if dst.exists():
                continue
            front, raw = split_front(src.read_text())
            prompt = json.loads(next(l for l in front.splitlines() if l.startswith("prompt: "))[8:])
            out = call(INSTRUCTION.format(prompt=prompt, raw=raw)).strip()
            raw_lines = {l.strip() for l in raw.splitlines()}
            missing = [l for l in out.splitlines() if l.strip() and l.strip() not in raw_lines]
            if missing or not out:
                bad += 1
                print(f"REFUSED {src.relative_to(EVALS)}: {len(missing)} lines not verbatim")
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            front = front.replace("wrapper_lines_stripped:", "raw_wrapper_lines_stripped:")
            dst.write_text(f"---\n{front}extracted_from: raw/{src.name}\n---\n\n{out}\n")
            kept = len(out.split()) / max(1, len(raw.split()))
            print(f"ok      {dst.relative_to(EVALS)} ({len(out.split())} words, {kept:.0%} of raw)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
