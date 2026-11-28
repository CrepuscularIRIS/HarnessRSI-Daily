# 2611.29807 · poster QA 记录

- 版式：1600×1680 "部署时间线 + 检测器矩阵 + 三刀"（顶部深色七节点部署时间线；中段四检测器对照表；三张成因切口卡；代价与证据强度双栏；底部边界卡）
- 渲染链：poster.html → Playwright chromium_headless_shell-1248（viewport=画布、deviceScaleFactor=2）→ poster.png / poster.pdf（@page 同尺寸、printBackground）
- 审计工件：assets/render-check.json（qa-geo / qa-extra）+ assets/qa_pixels.py 输出（qa-blank / 边距 / PDF 文本层）

## 检查项与结果（对实际渲染产物，终版）

| 检查项 | 脚本 / 方法 | 结果 |
|---|---|---|
| qa-geo 溢出/越界 | render_poster.js：main 内全部有 rect 的元素对四边判定（>0.5px）；main.scrollHeight | 0 处；scrollHeight 1680 = 画布 |
| qa-extra 文字裁切 | 叶文本节点 scrollWidth/Height > client+1 且自身 overflow≠visible | 0 处 |
| qa-extra 文字重叠 | 叶文本节点逐片段矩形（getClientRects）两两交叠（>2×2px） | 0 处 |
| qa-extra 字体 | document.fonts.check("16px PosterCN") + status=loaded；make_font.py 核对 HTML 全部字符均在本张子集字体 cmap 内（489 字形，缺字 0） | 通过 |
| qa-blank 空白带 | qa_pixels.py：对 poster.png 逐行扫描非背景像素，墨迹包围盒内部 ≥24px 的空带 | 0 条 |
| 像素级墨迹边距 | 同上，2× PNG 换算 CSS px | 左 54 / 上 50.5 / 右 54.5 / 下 63.5，墨迹行占比 87.6% |
| PDF 文本层 | pdftotext 抽取 | 2,790 字符，其中中文 1,523 字，可读 |
| 版式查重 | 与 018–021 十二种版式对比 | "横向部署时间线 + 检测器表 + 三切口卡"为 022 新版式；与 021 镜像双轴/四泳道/九宫矩阵、020 问题带管线/侵蚀曲线/三阶梯瀑布、019 双层机制带/纸面瀑布/蓝图矩阵、018 横向审计/暗底三权/纸面扇形均不同；与本期 2611.23068 的标尺三栏亦不同 |

## 迭代记录
- v1：qa-geo 捕获 4 个元素越界（.foot 底 1703.8 > 1680，内容总高 1768）；qa-extra 重叠报 2 条——核查为跨行行内元素的并集盒假阳性（getBoundingClientRect 对换行的 <b> 返回跨行并集），**脚本改为逐片段矩形比较**（同时回灌 2611.23068 复检，仍 0 处）。**一次重做**：收紧时间线节点高度、表格行距、切口卡与边界卡行距，main 底内边距 64→58。
- v2：qa-geo 0 处越界；scrollHeight 1681（1px 行盒余量，无元素越界），微调底内边距后重渲染。
- v3：全部检查项干净。
- v4（终版）：措辞收紧后重渲染——标题加限定"（5 域中 4 域 ≥ 一半）"、导语"被叫回就能修"→"被叫回后通常能修"（贴合摘要 "usually repair them once called"）；全部检查项仍干净（上表），不涉及版式重做。

## 状态

- 自动化 QA：**PASS**（程序化实检通过；一次重做后）
- 人工目验：**pending_visual_qa** —— 本次执行席（glm-5.4[1m]）无图像输入能力，以上为对实际渲染 PNG/PDF 的程序化检查（像素扫描 / DOM 几何 / 字体 cmap / 文本层），非人眼确认；发布请以本记录 + PNG 快速目验为准。
