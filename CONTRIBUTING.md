# Contributing

Thanks for taking a look.

- **A rewrite went wrong or the checker got it wrong:** open an issue with the template. A short text that shows it helps most.
- **Checker rules:** every rule needs a line it must catch and a line of normal Spanish it must leave alone, in `tools/test_deslop_es.py`. The second line matters more: a rule that flags ordinary Chilean Spanish does more harm than a missed tell.
- **The skill and the prompt:** changes are tuned on the dev set only (`evals/dev`). If a change could move the results, say so in the PR and we rerun the test.
- **Before opening a PR:** run `python3 tools/test_deslop_es.py` and `python3 scripts/check.py`, and make sure CI is green.
- **Spanish:** neutral, with tú and ustedes. No em dashes in anything we ship.
- **Security issues:** never in public. See [SECURITY.md](SECURITY.md).

I answer issues within a few days.
