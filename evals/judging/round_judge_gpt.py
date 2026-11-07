"""Run the three personas on GPT (Codex) for both packets; validate JSON into ROUND/judges/.
Prompts: evals/judging/hes5/prompts (fixed since HES-5).
Usage: python3 evals/judging/round_judge_gpt.py ROUND PACKET_DIR WORK_DIR
"""
import json, pathlib, subprocess, sys
J = pathlib.Path(__file__).resolve().parent; P = J / "hes5" / "prompts"; HERE = pathlib.Path(sys.argv[1]).resolve()
packets, work = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]); work.mkdir(parents=True, exist_ok=True)
common = (P / "common.md").read_text()
for persona in ("p1-editor", "p2-owner", "p3-copy"):
    for k in ("1", "2"):
        i = f"gpt-{persona.split('-')[0]}-{k}"
        (work / f"{i}.brief.txt").write_text((P / f"{persona}.md").read_text() + "\n" + common + "\nThe packet is in the stdin block.")
        (work / f"{i}.in.txt").write_text((packets / f"packet-{k}.md").read_text())
subprocess.run([sys.executable, str(J.parent / "tools/codex_batch.py"), str(work), "--effort", "high"])
(HERE / "judges").mkdir(exist_ok=True)
for o in sorted(work.glob("*.out.txt")):
    t = o.read_text(); t = t[t.find("{"): t.rfind("}") + 1]
    try:
        d = json.loads(t); assert all(len(v["rank"]) == 6 and len(v["scores"]) == 6 for v in d.values())
        (HERE / "judges" / o.name.replace(".out.txt", ".json")).write_text(json.dumps(d, ensure_ascii=False, indent=1))
        print("ok", o.name, len(d), "texts")
    except Exception as e:
        print("BAD", o.name, e)
