# 2611.23219 · poster QA 记录

- 版式：1700×1500 横版三联画（① 只给原语：蓝；② 自己组出的学习程序：绿，含示意倒 U 曲线；③ 证据：琥珀，代际差 / GEPA / 跨模型 / 迁移 / 工具消融）+ 底部边界卡
- 渲染链：poster.html → Playwright chromium_headless_shell-1248（viewport=画布、deviceScaleFactor=2）→ poster.png / poster.pdf（@page 同尺寸、printBackground）
- 审计工件：assets/render-check.json（qa-geo / qa-extra）+ assets/qa_pixels.py 输出（qa-blank / 边距 / PDF 文本层）

## 检查项与结果（对实际渲染产物，终版 = 首版）

| 检查项 | 脚本 / 方法 | 结果 |
|---|---|---|
| qa-geo 溢出/越界 | render_poster.js：main 内全部有 rect 的元素对四边判定（>0.5px）；main.scrollHeight | 0 处；scrollHeight 1500 = 画布 |
| qa-extra 文字裁切 | 叶文本节点 scrollWidth/Height > client+1 且自身 overflow≠visible | 0 处 |
| qa-extra 文字重叠 | 叶文本节点逐片段矩形（getClientRects）两两交叠（>2×2px） | 0 处 |
| qa-extra 字体 | document.fonts.check("16px PosterCN") + status=loaded；make_font.py 核对 HTML 全部字符均在本张子集字体 cmap 内（474 字形，缺字 0） | 通过 |
| qa-blank 空白带 | qa_pixels.py：对 poster.png 逐行扫描非背景像素，墨迹包围盒内部 ≥24px 的空带 | 0 条 |
| 像素级墨迹边距 | 同上，2× PNG 换算 CSS px | 左 54 / 上 48.5 / 右 54.5 / 下 56.5，墨迹行占比 90.1% |
| PDF 文本层 | pdftotext 抽取 | 2,658 字符，其中中文 943 字，可读 |
| 版式查重 | 与 018–021 十二种版式及本期前两张对比 | "横版三联画（给定 / 涌现 / 证据）"为 022 新版式；与 021 镜像双轴/四泳道/九宫矩阵、020 问题带管线/侵蚀曲线/三阶梯瀑布、019 双层机制带/纸面瀑布/蓝图矩阵、018 横向审计/暗底三权/纸面扇形、以及本期 2611.23068 的标尺三栏、2611.29807 的时间线+矩阵均不同 |

## 迭代记录
- v1（终版）：首版渲染全部检查项干净，未重做。

## 状态

- 自动化 QA：**PASS**（程序化实检通过；首版）
- 人工目验：**pending_visual_qa** —— 本次执行席（glm-5.4[1m]）无图像输入能力，以上为对实际渲染 PNG/PDF 的程序化检查（像素扫描 / DOM 几何 / 字体 cmap / 文本层），非人眼确认；发布请以本记录 + PNG 快速目验为准。
