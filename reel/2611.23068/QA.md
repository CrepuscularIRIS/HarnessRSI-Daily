# 2611.23068 · poster QA 记录

- 版式：1680×1600 "分辨率标尺 + 三栏"（顶部深色标尺带：σ_eval / 单次 SD / 已发表 IQR / σ_run 同一 pp 刻度；下接方法级·增益审计·候选级三栏；底部边界卡）
- 渲染链：poster.html → Playwright chromium_headless_shell-1248（viewport=画布、deviceScaleFactor=2）→ poster.png / poster.pdf（@page 同尺寸、printBackground）
- 审计工件：assets/render-check.json（qa-geo / qa-extra）+ assets/qa_pixels.py 输出（qa-blank / 边距 / PDF 文本层）

## 检查项与结果（对实际渲染产物，终版）

| 检查项 | 脚本 / 方法 | 结果 |
|---|---|---|
| qa-geo 溢出/越界 | render_poster.js：main 内全部有 rect 的元素对四边判定（>0.5px） | 0 处 |
| qa-extra 文字裁切 | 叶文本节点 scrollWidth/Height > client+1 且自身 overflow≠visible | 0 处 |
| qa-extra 文字重叠 | 叶文本节点两两 rect 交叠（>2×2px） | 0 处 |
| qa-extra 字体 | document.fonts.check("16px PosterCN") + status=loaded；make_font.py 核对 HTML 全部字符均在本张子集字体 cmap 内（439 字形，缺字 0） | 通过 |
| qa-blank 空白带 | qa_pixels.py：对 poster.png 逐行扫描非背景像素，墨迹包围盒内部 ≥24px 的空带 | 0 条 |
| 像素级墨迹边距 | 同上，2× PNG 换算 CSS px | 左 54 / 上 50.5 / 右 54.5 / 下 64.5，墨迹行占比 88.7% |
| PDF 文本层 | pdftotext 抽取 | 2,306 字符，其中中文 900 字，可读 |
| 版式查重 | 与 018–021 十二种版式对比 | "同刻度标尺带 + 三栏"为 022 新版式；与 021 镜像双轴/四泳道/九宫矩阵、020 问题带管线/侵蚀曲线/三阶梯瀑布、019 双层机制带/纸面瀑布/蓝图矩阵、018 横向审计/暗底三权/纸面扇形均不同 |

## 迭代记录
- v1：qa-geo 0 / qa-extra 重叠 0；qa-extra 裁切项报 8 条——均为 display:block 的 <b> 数字行盒（line-height 1.1/1.15）高于内容盒但 overflow 可见，判定为误报，脚本改为只在自身 overflow≠visible 时计裁切，并把行高调到 1.25。自查发现标尺条带位置未按 pp 线性映射（设计错误，非 QA 脚本捕获），重排标尺为 0–12.3pp 线性刻度。
- v2：qa-extra 捕获 1 处真实重叠——标尺右标签"SpreadsheetBench / OfficeQA / ALFWorld 的评估噪声"与"Terminal-Bench σ_eval 4.5"交叠 155.6×22px。**一次重做**：把 TB σ_eval 改为刻度轴下方标注（36.6% 处细线 + 轴下标签），去掉行内标签。
- v3（终版）：全部检查项干净（上表）。

## 状态

- 自动化 QA：**PASS**（程序化实检通过；一次重做后）
- 人工目验：**pending_visual_qa** —— 本次执行席（glm-5.4[1m]）无图像输入能力，以上为对实际渲染 PNG/PDF 的程序化检查（像素扫描 / DOM 几何 / 字体 cmap / 文本层），非人眼确认；发布请以本记录 + PNG 快速目验为准。
