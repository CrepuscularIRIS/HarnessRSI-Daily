// selection-021 渲染脚本（与 020 期 render_poster.py 同位）：渲染 2611.18883 海报并写审计
// 用法: node assets/render_poster.js （在 reel/2611.18883/ 下）
const { chromium } = require('/home/lingxufeng/.npm-global/lib/node_modules/@playwright/cli/node_modules/playwright');
(async () => {
  const W = 1680, H = 1560;
  const browser = await chromium.launch({ executablePath: '/home/lingxufeng/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell' });
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  await page.goto('file://' + __dirname + '/../poster.html');
  await page.waitForTimeout(1400);
  const audit = await page.evaluate((dim) => {
    const W = dim.W, H = dim.H, bad = [], noInk = [];
    document.querySelectorAll('main *').forEach(el => {
      if (el.children.length === 0 && el.textContent.trim()) {
        const r = el.getBoundingClientRect();
        if (r.bottom > H + 0.5 || r.right > W + 0.5 || r.left < -0.5 || r.top < -0.5) bad.push(el.tagName + '.' + el.className);
      }
    });
    for (let i = 0; i < 12; i++) {
      const y0 = Math.floor(H * i / 12), y1 = Math.floor(H * (i + 1) / 12);
      const els = [...document.elementsFromPoint(W / 2, (y0 + y1) / 2)];
      const dark = els.some(e => { const s = getComputedStyle(e); return s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== 'transparent'; });
      if (!dark) noInk.push(i);
    }
    return { bad, noInk, fontLoaded: document.fonts.check("16px PosterCN") };
  }, { W, H });
  await page.pdf({ path: __dirname + '/../poster.pdf', width: W + 'px', height: H + 'px', printBackground: true, pageRanges: '1' });
  await page.screenshot({ path: __dirname + '/../poster.png', clip: { x: 0, y: 0, width: W, height: H } });
  require('fs').writeFileSync(__dirname + '/render-check.json', JSON.stringify({ width: W, height: H, overflow: audit.bad, inkBandsEmpty: audit.noInk, fontLoaded: audit.fontLoaded, tool: 'playwright-1248' }, null, 2));
  console.log(JSON.stringify(audit));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
