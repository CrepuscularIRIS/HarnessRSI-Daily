// selection-022 渲染脚本：渲染 2611.23068 海报并写审计（qa-geo 溢出/越界 · qa-extra 裁切/重叠/字体 · 墨带）
// 用法: node assets/render_poster.js （在 reel/2611.23068/ 下）
const { chromium } = require('/home/lingxufeng/.npm-global/lib/node_modules/@playwright/cli/node_modules/playwright');
(async () => {
  const W = 1680, H = 1600;
  const browser = await chromium.launch({ executablePath: '/home/lingxufeng/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell' });
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  await page.goto('file://' + __dirname + '/../poster.html');
  await page.waitForTimeout(600);
  await page.waitForFunction("document.fonts.status === 'loaded'");
  await page.waitForTimeout(600);
  const audit = await page.evaluate((dim) => {
    const W = dim.W, H = dim.H;
    const overflow = [], clipped = [], texts = [];
    const leafText = el => el.children.length === 0 && el.textContent.trim().length > 0;
    document.querySelectorAll('main *').forEach(el => {
      if (!el.getClientRects().length) return;
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) return;
      const name = el.tagName + '.' + String(el.className || '');
      // qa-geo: any element beyond canvas
      if (r.bottom > H + 0.5 || r.right > W + 0.5 || r.left < -0.5 || r.top < -0.5) overflow.push({ el: name, l: +r.left.toFixed(1), t: +r.top.toFixed(1), r: +r.right.toFixed(1), b: +r.bottom.toFixed(1) });
      if (leafText(el)) {
        // qa-extra: text clipped by its own box
        const cs = getComputedStyle(el);
        if ((el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1) && cs.overflow !== 'visible') clipped.push({ el: name, text: el.textContent.trim().slice(0, 30), sw: el.scrollWidth, cw: el.clientWidth, sh: el.scrollHeight, ch: el.clientHeight, overflow: cs.overflow });
        // 用 clientRects 的逐片段矩形（行内元素跨行时 getBoundingClientRect 是并集盒，会产生假重叠）
        const frags = [...el.getClientRects()].filter(fr => fr.width > 0 && fr.height > 0).map(fr => ({ l: fr.left, t: fr.top, r: fr.right, b: fr.bottom }));
        texts.push({ el: name, text: el.textContent.trim().slice(0, 30), frags });
      }
    });
    // qa-extra: pairwise overlap of text leaves (> 2x2 px). Skip pairs where one is inside a bar/track (ancestor has overflow hidden) vs its sibling label: we only flag when both are pure text leaves.
    const overlaps = [];
    for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
      const a = texts[i], b = texts[j];
      // 同一父元素内的相邻行内片段共享行盒是正常排版，跳过同一 textContent 父节点下的兄弟
      if (a.el === b.el) continue;
      let best = null;
      for (const fa of a.frags) for (const fb of b.frags) {
        const ix = Math.min(fa.r, fb.r) - Math.max(fa.l, fb.l), iy = Math.min(fa.b, fb.b) - Math.max(fa.t, fb.t);
        if (ix > 2 && iy > 2 && (!best || ix * iy > best.ix * best.iy)) best = { ix: +ix.toFixed(1), iy: +iy.toFixed(1) };
      }
      if (best) overlaps.push({ a: a.text, b: b.text, ...best });
    }
    // qa-blank 在真实像素上做：见 assets/qa_pixels.py（空带/边距/墨迹占比）
    const fontLoaded = document.fonts.check("16px PosterCN") && document.fonts.status === 'loaded';
    const docH = document.querySelector('main').scrollHeight;
    return { overflow, clipped, overlaps, fontLoaded, mainScrollH: docH };
  }, { W, H });
  await page.pdf({ path: __dirname + '/../poster.pdf', width: W + 'px', height: H + 'px', printBackground: true, pageRanges: '1' });
  await page.screenshot({ path: __dirname + '/../poster.png', clip: { x: 0, y: 0, width: W, height: H } });
  const out = { width: W, height: H, qa_geo_overflow: audit.overflow, qa_extra_clipped: audit.clipped, qa_extra_overlaps: audit.overlaps, qa_extra_fontLoaded: audit.fontLoaded, qa_blank_emptyBands: audit.noInk, mainScrollHeight: audit.mainScrollH, tool: 'playwright-chromium_headless_shell-1248' };
  require('fs').writeFileSync(__dirname + '/render-check.json', JSON.stringify(out, null, 2));
  console.log(JSON.stringify(out));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
