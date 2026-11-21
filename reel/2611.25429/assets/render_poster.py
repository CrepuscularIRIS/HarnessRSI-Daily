#!/usr/bin/env python3
"""Render poster.html -> poster.pdf + poster.png for a reel dir.

Usage: python3 render_poster.py <reel_dir> <width> <height>
Writes poster.pdf, poster.png, and assets/render-check.json (geometry audit).
"""
import json, sys, pathlib

from playwright.sync_api import sync_playwright

reel = pathlib.Path(sys.argv[1]).resolve()
W, H = int(sys.argv[2]), int(sys.argv[3])

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/home/lingxufeng/.cache/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-linux64/chrome-headless-shell")
    page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    page.goto(f"file://{reel}/poster.html")
    page.wait_for_timeout(400)
    page.wait_for_function("document.fonts.status === 'loaded'")
    page.emulate_media(media="print")

    # geometry audit: leaf elements beyond canvas
    overflow = page.evaluate(
        """() => {
        const bad = [];
        const isLeaf = el => ![...el.children].some(c => c.offsetParent !== null || c.getClientRects().length);
        for (const el of document.querySelectorAll('main *')) {
            if (!el.getClientRects().length) continue;
            const r = el.getBoundingClientRect();
            if (r.width === 0 && r.height === 0) continue;
            if (!isLeaf(el)) continue;
            const overB = r.bottom - %d, overR = r.right - %d;
            if (overB > 1 || overR > 1) bad.push({tag: el.tagName, cls: el.className.baseVal !== undefined ? String(el.className.baseVal) : String(el.className || ''), text: (el.textContent || '').trim().slice(0, 40), bottom: Math.round(r.bottom), right: Math.round(r.right)});
        }
        return bad;
    }"""
        % (H, W)
    )

    # ink-band scan: any full-width horizontal band of the PNG with zero ink?
    # (approximated in-page: check no main-row block has collapsed height)
    inkBandsEmpty = page.evaluate(
        """() => {
        const bands = [];
        for (const el of document.querySelectorAll('main > *')) {
            const r = el.getBoundingClientRect();
            if (r.height > 2) bands.push(Math.round(r.height));
        }
        return bands.filter(h => h < 4);  // suspiciously flat top-level rows
    }"""
    )

    page.pdf(path=str(reel / "poster.pdf"), width=f"{W}px", height=f"{H}px", print_background=True, page_ranges="1")
    page.screenshot(path=str(reel / "poster.png"), full_page=True)
    font_loaded = page.evaluate("document.fonts.check('20px PosterCN')")

    check = {"width": W, "height": H, "overflow": overflow, "inkBandsEmpty": inkBandsEmpty, "fontLoaded": font_loaded, "tool": "playwright-1248"}
    (reel / "assets").mkdir(exist_ok=True)
    (reel / "assets" / "render-check.json").write_text(json.dumps(check, ensure_ascii=False, indent=1))
    print(json.dumps(check, ensure_ascii=False))
    browser.close()
