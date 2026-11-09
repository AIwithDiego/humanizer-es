# Third-party notices

## Ideas we built on (no code or wording copied)

The skill, the prompt and the checker are our own Spanish text. They build on ideas from these MIT-licensed projects:

- [blader/humanizer](https://github.com/blader/humanizer), © 2025 Siqi Chen: overall structure, ordering tells by strength, the workflow. Itself based on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop), © 2025 Hardik Pandya: false agency, vague claims.
- [ItsssssJack/SlopMonster](https://github.com/ItsssssJack/SlopMonster), © 2026 Jack Roberts: the second pass with another model; "a clean score is not good text".
- [omelyanchuk2593/humanizer-es](https://github.com/omelyanchuk2593/humanizer-es), © 2026 Ivan Omelianchuk: Spanish false positives. Its licence asks derivative works to credit it; we took ideas only, no wording.
- [alvaromieres9/humanizer-es](https://github.com/alvaromieres9/humanizer-es), [Milevan/humanizer-es](https://github.com/Milevan/humanizer-es), [madebydiego/humanizador](https://github.com/madebydiego/humanizador): the Spanish layer and the calque test.

## Copies included for the blind test

`evals/contestants/` holds frozen copies of the other skills, as of 6 Nov 2026, so the test can be rerun. Each folder keeps its own LICENSE (all MIT):

| Folder | Project | Copyright | Changes |
|---|---|---|---|
| `omel/` | omelyanchuk2593/humanizer-es | © 2026 Ivan Omelianchuk | none |
| `alvaro/` | alvaromieres9/humanizer-es | © 2026 Álvaro Fernández Otero | none |
| `madeby/` | madebydiego/humanizador | © 2026 Diego Fernandez | none |
| `blader/` | blader/humanizer | © 2025 Siqi Chen | **modified:** a second-pass step through Codex CLI added |

`evals/fixtures/human-omelyanchuk-clean.md` is a test text from omelyanchuk2593/humanizer-es (MIT, `evals/fixtures/LICENSE-omelyanchuk`).

## Texts we don't redistribute

Seven human-written control texts (Reddit posts, job ads, a shop's "about us" page, two news articles) are not included. `evals/human-sources.md` lists each source and the sha256 of the text we used; `evals/tools/fetch_human.py` gets them back.

## Name and logo

The AIwithDiego name and logo (in `docs/assets/social-preview-*.png`) are not covered by the MIT licence.
