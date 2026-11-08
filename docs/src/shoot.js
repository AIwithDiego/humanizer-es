// node shoot.js still <html> <out.png> <w> <h> [scale]
// node shoot.js frames <html> <outdir> <fps>
const { chromium } = require("playwright-core");
const EXE = process.env.HOME + "/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell";
(async () => {
  const [mode, url, out, a, b, c] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: EXE });
  if (mode === "still") {
    const page = await browser.newPage({ viewport: { width: +a, height: +b }, deviceScaleFactor: +(c || 2) });
    await page.goto(url); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(400);
    const el = await page.$("#cap");
    await (el || page).screenshot({ path: out, ...(el ? {} : { fullPage: false }) });
  } else {
    const fps = +a;
    const page = await browser.newPage({ viewport: { width: 1200, height: 675 }, deviceScaleFactor: 1 });
    await page.goto(url); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(400);
    const dur = await page.evaluate(() => window.DURATION);
    const n = Math.round(dur * fps);
    for (let i = 0; i < n; i++) {
      await page.evaluate(t => window.render(t), i / fps);
      await page.screenshot({ path: `${out}/f${String(i).padStart(4, "0")}.png` });
    }
  }
  await browser.close();
})();
