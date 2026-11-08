# humanizer-es

[Español](README.es.md)

**Make AI-written Spanish sound like you, without changing what it says.**

Ranked first against four other humanizers in a blind test judged by Claude and GPT. The judges caught 0 invented facts in 180 verdicts.

<sub>A live project by [AIwithDiego](https://www.aiwithdiego.com): researched, built, tested, and still improving with your feedback. Need this for your team? [Talk to me](https://www.aiwithdiego.com).</sub>

<p align="center"><img src="docs/demo-en.gif" alt="Animation: a scan line flags seven AI tells in an Instagram caption written by ChatGPT, the tells burst away, and the four facts (bakery name, 6:00, the three breads, the address) glide into the rewritten text. The checker score goes from 2/5 to 5/5." width="760"></p>

```text
/plugin marketplace add AIwithDiego/humanizer-es
/plugin install humanizer-es@humanizer-es
```

**Works with:** Claude Code (skill) · ChatGPT, Claude.ai and any chat ([`prompt.md`](prompt.md)) · any terminal (the checker)

**On this page:** [The problem](#the-problem) · [Why it matters](#why-it-matters) · [Research](#research) · [Approach](#approach) · [What you get](#what-you-get) · [How we tested](#how-we-tested) · [Results](#results) · [What's next](#whats-next) · [Send feedback](#send-feedback)

## The problem

More and more Spanish is drafted by ChatGPT and Claude: client emails, Instagram captions, job posts, LinkedIn updates. Readers spot it fast. Spanish AI text has its own tells, and most of them aren't the English ones:

- **Calques from English:** "es importante destacar que", "en el mundo actual", Title Case En Los Títulos.
- **Grammar and rhythm:** dangling gerunds ("…, garantizando frescura"), triads everywhere, questions that answer themselves.
- **The wrong Spanish:** vosotros and Spain phrasing in an email from a shop in Santiago.
- **Theatre:** "no solo X, creamos Y", empty praise, "¡Te leo en los comentarios!".

The usual fix, "make it sound more human", makes it worse. In our test, a plain ask to ChatGPT or Claude invented or changed facts in about 4 of every 10 verdicts.

## Why it matters

A text that sounds like AI costs trust: the client wonders whether anyone read their email. But a humanizer that invents costs more. A rewrite that adds an apology the business never made, or "we loved the proposal" when nobody said so, can't go to a client. For a small business, the fact is the whole point of the message: the hour, the price, the address.

So the bar for this project was two things at once: sound like a person, and change nothing that's true.

## Research

Before writing a line of the skill:

- **What already exists.** We found four Spanish humanizers on GitHub. We froze three of them, plus the English one we used before, exactly as published, to test them fairly later. ([`evals/contestants/`](evals/contestants/))
- **What AI Spanish looks like.** We started from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and blader/humanizer's framework, then catalogued the Spanish tells and ranked them by strength: some are enough on their own, others count only in clusters. ([`skills/humanizer-es/SKILL.md`](skills/humanizer-es/SKILL.md))
- **What a person sounds like.** We collected texts Chileans wrote before ChatGPT existed (forum posts, job ads, a pastry shop's "about us", local news) as controls. A good humanizer should leave them almost untouched. ([`evals/human-sources.md`](evals/human-sources.md))

## Approach

Four rules shape every rewrite:

1. **Decide who wrote it first.** If no AI tell shows up, the text is a person's: fix clear typos and stop.
2. **Fix by deleting, not decorating.** Cut the tell. If that leaves a gap, fill it with a fact already in the text. If there's none, simplify.
3. **Never add a fact.** No new names, numbers, apologies, promises or flourishes. Keep the same scope and the same strength.
4. **Neutral Spanish that reads right in Chile.** Tú and ustedes; no vosotros, no voseo.

## What you get

| | What it is | Where |
|---|---|---|
| **The skill** | Full workflow for Claude Code: tells ranked by strength, a draft, a self-audit, an optional second pass by GPT | [`skills/humanizer-es/`](skills/humanizer-es/SKILL.md) |
| **The paste-in prompt** | One prompt for ChatGPT, Claude.ai or any chat | [`prompt.md`](prompt.md) |
| **The checker** | `deslop-es`: regex checker for Spanish AI tells. Free, offline, scores 1 to 5 | [`tools/deslop_es.py`](tools/deslop_es.py) |
| **The evidence** | Every brief, text, version, judge prompt and verdict | [`evals/`](evals/README.md) |

Quick start:

1. In Claude Code, run the two lines above.
2. Paste a Spanish text and ask Claude to humanize it, or type `/humanizer-es`.
3. Copy the version on top. Under it, a note on what changed.

No Claude Code? Paste [`prompt.md`](prompt.md) into ChatGPT or Claude.ai, then your text after "Texto:". Checker: `python3 tools/deslop_es.py --text "tu texto"`.

## How we tested

<p align="center"><img src="docs/how-we-tested-en.png" alt="How we tested, in six steps: 30 briefs in 15 genres; 60 AI texts, one by GPT and one by Claude per brief, plus 8 texts people wrote before ChatGPT; 2 sets, dev for tuning and locked, opened once; 6 versions per text, each humanizer run as it ships; 3 judge personas, each as a Claude and a GPT judge, labels shuffled; result, first of 6 with 0 invented facts in 180 verdicts. Below: 137 automated checker tests in CI, manual testing by Diego on his own texts, 9 test rounds with the first 3 retired." width="760"></p>

- **Automated.** The checker has 137 fixture tests. CI runs them on every pull request, with a plugin structure check and a secret scan.
- **Blind evals.** 9 rounds. Judges never see who wrote what, and judges from two model families score every version, because a model judging alone favours its own style.
- **Manual.** Diego tested it on his own texts, outside the test sets.
- **Honest about the test.** We retired our first three rounds because we had written those texts ourselves. The headline number comes from a locked set nobody read while tuning.

## Results

<p align="center"><img src="docs/results-en.png" alt="Average rank, lower is better: humanizer-es 2.44, humanizer-es with a GPT pass 2.48, blader/humanizer 3.22, alvaromieres9 3.97, madebydiego 4.35, omelyanchuk2593 4.53. Facts invented or changed, out of 180 verdicts: humanizer-es 0, omelyanchuk2593 12, blader 14, alvaromieres9 27, madebydiego 36." width="760"></p>

30 AI-written texts and 4 written by people, none used for tuning; each humanizer ran as it ships. Tested on v1.3; v1.4 only adds typo fixes on text a person wrote, checked on the dev set and not re-judged. The paste-in prompt beats a plain "make it sound human" by about two ranks. Everything, verdict by verdict: [`evals/`](evals/README.md).

## What it won't do

- Add facts, apologies, promises or personality that aren't in your text.
- Rewrite text a person wrote. It fixes typos and stops.
- Promise to beat AI detectors. It edits for readers.
- Send your text to another model without asking.

Please don't use it to hide AI use where you have to declare it (coursework, research, journalism).

---

## Decisions

| Choice | Why | Trade-off |
|---|---|---|
| Never add a fact, even to sound more human | A humanizer that invents can't be trusted with a client email | Less colourful than alvaromieres9, which judges sometimes found more Chilean |
| A skill and a paste-in prompt | Most people who write in Spanish use ChatGPT, not Claude Code | The prompt has fewer checks and no second pass |
| Judges from two model families | A model judging alone favours its own style | Twice the cost, and the families disagree on the GPT second pass, so it stays optional |
| A locked test set, opened once | So the headline number isn't tuned to the test | It's spent; the next claim needs new texts |
| A regex checker, no model | Free, instant, offline, runs in CI | Misses tells of tone: 12 of 30 AI texts scored clean |

## How this was built

Built by Diego Bauer with Claude Code. I set the bar (beat the Spanish humanizers out there, blind, without inventing), made the calls on variant, privacy and what counts as a fact, and tested it on my own texts. Claude wrote most of the skill, the checker and the test scripts. Before release, an AI security review covered the second pass (prompt injection, data sent to OpenAI) and what we could publish under each licence.

## What I learned

- **A model can't see its own habits.** The first paste-in prompt left GPT's text almost untouched: GPT often decided its own text "ya suena humano". The fix was to decide first who wrote it, and edit AI text even when it looks correct.
- **Inventing is the real failure, not sounding robotic.** v1.2 changed or invented facts in 21 verdicts on the dev set; v1.3 in 3, and in 0 of 180 on the locked set. Rules like "keep descriptors, cut empty praise" and "same scope, same strength" did more than any list of banned words.
- **Judges disagree by family.** Claude judges preferred our version without the GPT pass; GPT judges preferred it with. Testing with one family would have given us a confident wrong answer.
- **Leaving human text alone isn't enough.** Judges ranked a competitor first on human texts because it fixed typos. v1.4 fixes clear typos and nothing else.
- **We retired our first three test rounds** because we had written the texts ourselves. The test since uses real briefs, texts from GPT and Claude, and texts people wrote before ChatGPT.

## What's next

- **The checker, tuned by readers.** The first three issues are fixed, two of them by an outside contributor. Next: tells you report, and fixtures from more countries (Peru, Venezuela, Uruguay…).
- **A new blind round** on fresh texts, to judge v1.4 and whatever your feedback changes.

## Send feedback

This is a live project. Every report that a rewrite changed a fact, missed a tell or sounded off feeds the next version.

- **A rewrite went wrong:** [open an issue](https://github.com/AIwithDiego/humanizer-es/issues/new?template=rewrite.yml) (swap real names and numbers for made-up ones).
- **An idea or a quick note:** [share feedback](https://github.com/AIwithDiego/humanizer-es/issues/new?template=feedback.yml).
- **Rather not use GitHub?** Send a DM on Instagram to [@ai_with_diego](https://www.instagram.com/ai_with_diego/) or email diego@aiwithdiego.com.

Pull requests are welcome too, especially false alarms from the checker on normal Spanish from your country. See [CONTRIBUTING.md](CONTRIBUTING.md). Security issues: [SECURITY.md](SECURITY.md).

## Credits

Built on ideas from [blader/humanizer](https://github.com/blader/humanizer), [stop-slop](https://github.com/hardikpandya/stop-slop), [SlopMonster](https://github.com/ItsssssJack/SlopMonster) and the Spanish humanizers by [omelyanchuk2593](https://github.com/omelyanchuk2593/humanizer-es), [alvaromieres9](https://github.com/alvaromieres9/humanizer-es), [Milevan](https://github.com/Milevan/humanizer-es) and [madebydiego](https://github.com/madebydiego/humanizador). Details in [THIRD-PARTY.md](THIRD-PARTY.md).

## License

MIT · Made in Dublin by [Diego Bauer](https://www.aiwithdiego.com) · [LinkedIn](https://www.linkedin.com/in/diego-bauer-domeyko/)
