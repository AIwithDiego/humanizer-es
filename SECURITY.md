# Security policy

## Reporting a vulnerability

Please report security issues privately: use [Report a vulnerability](https://github.com/AIwithDiego/humanizer-es/security/advisories/new) on GitHub, or email **diego@aiwithdiego.com**. Do not open a public issue or pull request for a vulnerability. Include the file, the line, and a reproduction.

Most relevant here: the optional second pass (step 5 of the skill) sends text to another model through Codex CLI. If you find a way for a pasted text to make that step run commands, read files or leak data, that's a security issue.

I'll acknowledge your report within 5 working days.

## Supported versions

Only the latest commit on `main` is supported.
