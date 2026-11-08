# How the images are made

Each image is an HTML page rendered in headless Chromium, so the text in them is real text, not generated pixels.

- `demo.html` draws the before/after animation; `render(t)` sets any moment of it. The after text is the skill's real output (v1.4) for the before text.
- `results.html` draws the results chart from the locked-set numbers in `evals/README.md`.
- `social.html` is the 1280×640 card for link previews. It expects the AIwithDiego logo as `logo-a.png`, which isn't in this repo.

```bash
npm i playwright-core
node shoot.js still "file://$PWD/results.html?lang=en" results-en.png 1440 900 2
node shoot.js frames "file://$PWD/demo.html?lang=en" frames 15
ffmpeg -framerate 15 -i frames/f%04d.png -vf "split[a][b];[a]palettegen=max_colors=160:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle" demo-en.gif
```

`shoot.js` looks for Playwright's Chromium in the macOS cache; change `EXE` for your system.
