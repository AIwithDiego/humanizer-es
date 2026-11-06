#!/usr/bin/env python3
"""Get the human control texts (h01-h07) back from their sources.

They are not in this repo because we don't hold the rights to them. Each stub in
evals/dev/human/ and evals/locked/human/ keeps the source URL and the sha256 of the
exact text we used.

  python3 evals/tools/fetch_human.py fetch          # downloads each archived page to evals/human-cache/
  python3 evals/tools/fetch_human.py check FILE...  # checks texts you extracted against the hashes

To rebuild a text: copy the post or article body from the downloaded page into the stub
(below its header, replacing the comment), following the notes in evals/human-sources.md
(links as plain text, news without image captions), then run `check` on the stub.
Known edits that the hashes include: h05 has the family surname replaced with [apellido];
h01 has a zero-width-space line dropped. Without those edits you'll get DIFF.
"""
import hashlib, pathlib, re, sys, urllib.request

E = pathlib.Path(__file__).resolve().parents[1]


def stubs():
    for p in sorted(E.glob("*/human/h0*.md")):
        head = p.read_text().split("---", 2)[1]
        meta = dict(re.findall(r"^(\w+): (.*)$", head, re.M))
        if "sha256" in meta:
            yield p, meta


def body(text):
    return text.split("---", 2)[2].strip() if text.startswith("---") else text.strip()


def fetch():
    cache = E / "human-cache"; cache.mkdir(exist_ok=True)
    for p, meta in stubs():
        url = (meta.get("evidence_url") or meta["source_url"]).split()[0]
        m = re.search(r"reddit\.com/r/\w+/comments/(\w+)", url)
        if m:  # reddit blocks scripts; the Arctic Shift archive serves the same post
            url = f"https://arctic-shift.photon-reddit.com/api/posts/ids?ids={m.group(1)}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "humanizer-es-eval"})
            with urllib.request.urlopen(req, timeout=60) as r:
                (cache / f"{p.stem}.html").write_bytes(r.read())
            print(f"ok   {p.stem}  {url}")
        except Exception as e:
            print(f"FAIL {p.stem}  {url}  ({e})")


def check(files):
    want = {p.stem: m["sha256"] for p, m in stubs()}
    ok = True
    for f in files:
        f = pathlib.Path(f); h = hashlib.sha256(body(f.read_text()).encode()).hexdigest()
        match = want.get(f.stem) == h
        ok &= match
        print(f"{'match' if match else 'DIFF '} {f}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    if sys.argv[1:2] == ["fetch"]: fetch()
    elif sys.argv[1:2] == ["check"]: check(sys.argv[2:])
    else: print(__doc__)
