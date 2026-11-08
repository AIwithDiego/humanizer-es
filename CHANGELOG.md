# Changelog

## v1.4.1 · 8 Nov 2026
- Checker catches "no solo X, creamos Y" with any verb, not only "es" (#2, thanks @X6M-Work).
- Checker catches a dangling gerund at the end of any sentence, not only at the end of the text (#3, thanks @X6M-Work).
- 20 everyday lines from Mexico, Argentina, Spain and Colombia must score clean, so the checker doesn't flag normal local Spanish (#4). 137 fixture checks in all.

## v1.4.0 · 8 Nov 2026
- First public release: a Claude Code skill and a paste-in prompt that rewrite AI-sounding Spanish without changing what it says.
- Ranked first against four other humanizers in a blind test (tested on v1.3), with Claude and GPT judges, who caught 0 invented facts in 180 verdicts.
- Text written by a person gets typo and punctuation fixes only.
- `deslop_es.py`: a checker for the most common AI tells in Spanish, with 113 fixture checks.
- Optional second pass with GPT, opt-in, isolated and read-only.
