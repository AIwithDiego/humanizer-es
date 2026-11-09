# How the images are made

Each image is an HTML page rendered in headless Chromium, so the text in them is real text, not generated pixels.

- `demo.html` draws the motion demo (scan, tells burst, facts glide into the rewrite); `render(t)` sets any moment of it. The after text is the skill's real output (v1.4) for the before text.
- `how-we-tested.html` draws the test pipeline diagram.
- `results.html` draws the results chart from the locked-set numbers in `evals/README.md`.
- `social.html` is the 1280×640 card for link previews.
- `how_it_works.py` writes `../how-it-works-en.svg` and `../how-it-works-es.svg` (plain SVG, no browser needed).

```bash
python3 how_it_works.py
npm i playwright-core
node shoot.js still "file://$PWD/results.html?lang=en" ../assets/results-en.png 1440 900 2
node shoot.js still "file://$PWD/how-we-tested.html?lang=en" ../assets/how-we-tested-en.png 1200 700 2
node shoot.js frames "file://$PWD/demo.html?lang=en" frames 20
ffmpeg -framerate 20 -i frames/f%04d.png -vf "scale=960:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle" ../assets/demo-en.gif
```

`shoot.js` looks for Playwright's Chromium in the macOS cache; change `EXE` for your system.
