#!/usr/bin/env python3
"""qa-blank / 像素级墨迹审计：读 poster.png（2x），算非背景墨迹包围盒边距、墨迹占比、内部空带；并用 pdftotext 抽 PDF 文本层中文。
Usage: python3 qa_pixels.py <reel_dir> <css_width> <css_height> <bg_hex>
"""
import sys, pathlib, subprocess
from PIL import Image
reel = pathlib.Path(sys.argv[1]).resolve(); W = int(sys.argv[2]); H = int(sys.argv[3]); bg = sys.argv[4].lstrip('#')
br, bgc, bb = int(bg[0:2],16), int(bg[2:4],16), int(bg[4:6],16)
im = Image.open(reel/'poster.png').convert('RGB'); s = im.width / W
px = im.load()
def ink(x, y):
    r, g, b = px[x, y]; return abs(r-br) + abs(g-bgc) + abs(b-bb) > 24
w, h = im.size
rows = [False]*h; cols = [False]*w
for y in range(h):
    for x in range(0, w, 2):
        if ink(x, y): rows[y] = True; cols[x] = True
# refine cols by full scan on ink rows
for x in range(w):
    if not cols[x]:
        for y in range(0, h, 4):
            if rows[y] and ink(x, y): cols[x] = True; break
top = rows.index(True)/s; bottom = (h - rows[::-1].index(True) - 1)/s
left = cols.index(True)/s; right = (w - cols[::-1].index(True) - 1)/s
ink_ratio = sum(rows)/h
# empty runs strictly inside ink bbox
inner = rows[int(top*s)+1:int(bottom*s)]
runs = []; cur = 0
for v in inner:
    if not v: cur += 1
    else:
        if cur: runs.append(cur/s)
        cur = 0
if cur: runs.append(cur/s)
empty = [round(r,1) for r in runs if r >= 24]
txt = subprocess.run(['pdftotext', str(reel/'poster.pdf'), '-'], capture_output=True, text=True).stdout
cjk = sum(1 for c in txt if '\u4e00' <= c <= '\u9fff')
print({'margins_css_px': {'left': round(left,1), 'top': round(top,1), 'right': round(W-right,1), 'bottom': round(H-bottom,1)},
       'ink_ratio': round(ink_ratio,3), 'empty_bands_inside_ink_ge24px': empty, 'pdf_text_chars': len(txt), 'pdf_cjk_chars': cjk})
