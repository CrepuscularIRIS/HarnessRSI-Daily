#!/usr/bin/env python3
"""Subset Noto Sans CJK SC (TTC face 2) to the glyphs used in poster.html -> assets/fonts/poster.woff2,
then verify every character in the HTML text is covered by the subset (qa-extra: 字体/缺字).
Usage: python3 make_font.py <reel_dir>
"""
import re, sys, subprocess, pathlib, html as htmlmod
from fontTools.ttLib import TTFont

reel = pathlib.Path(sys.argv[1]).resolve()
src = (reel / "poster.html").read_text(encoding="utf-8")
# strip <style>...</style> and tags, keep text; also include title
text = re.sub(r"<style>.*?</style>", "", src, flags=re.S)
text = re.sub(r"<[^>]+>", "", text)
text = htmlmod.unescape(text)
chars = set(text)
# always include ASCII printable + common typographic punctuation
chars |= set(chr(c) for c in range(0x20, 0x7F))
chars |= set("·—→←↑↓≥≤±×÷−–…†‡§¶（）「」『』“”‘’、。，：；！？％°±√≈≠∞")
chars |= set("0123456789")
unicodes = ",".join(f"U+{ord(c):04X}" for c in sorted(chars) if ord(c) >= 0x20 and not c.isspace())
out = reel / "assets" / "fonts" / "poster.woff2"
out.parent.mkdir(parents=True, exist_ok=True)
cmd = ["pyftsubset", "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
       f"--font-number=2", f"--unicodes={unicodes}", "--flavor=woff2",
       "--layout-features=*", "--no-hinting", f"--output-file={out}"]
subprocess.run(cmd, check=True)
f = TTFont(out)
cmap = f.getBestCmap()
doc_chars = set(text)
missing = sorted(c for c in doc_chars if not c.isspace() and ord(c) not in cmap)
print({"glyphs": len(cmap), "bytes": out.stat().st_size, "missing": len(missing), "missing_chars": "".join(missing)})
sys.exit(1 if missing else 0)
