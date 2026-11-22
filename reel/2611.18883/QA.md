# 2611.18883 · poster QA 记录

- 版式：1680×1560 镜像反转（左代理轴/右合同轴、中央排序反转枢轴），true
- 渲染链：poster.html → Playwright chromium_headless_shell-1248（viewport=画布、deviceScaleFactor=2）→ poster.png / poster.pdf（@page 同尺寸、printBackground）
- 审计工件：assets/render-check.json（几何+字体+墨带）

## 检查项与结果（对实际渲染产物）

| 检查项 | 方法 | 结果 |
|---|---|---|
| 溢出/裁切 | DOM 全叶节点 rect 对 4 边判定（>0.5px 容差） | 见备注 |
| 像素级墨迹边距 | 对 poster.png 逐 2px 扫描非背景包围盒 | 左54/上53/右54.5/下72.5（CSS px），墨迹占比 10.4% |
| 重叠 | 叶节点两两 rect 交叠（>2×2px） | 0 处 |
| 中文字体 | document.fonts.check("16px PosterCN") + PDF 文本层 pdftotext 抽取中文可读 | 通过（与 020 期同 woff2） |
| 墨带空带 | 12 横带中心采样背景检测 | 无空带 |
| 版式查重 | 与 018/019/020 九种版式对比 | 镜像双轴+中央枢轴结构为 021 新版式，与近三期（018 横向审计/暗底三权/纸面扇形、019 双层机制带/纸面瀑布/蓝图矩阵、020 问题带管线/侵蚀曲线竖版/三阶梯瀑布）均不同 |


## 状态

- 自动化 QA：**FAIL**（首版通过）
- 人工目验：**pending_visual_qa** —— 本次执行席（glm-5.3）无图像输入能力，以上为对实际渲染 PNG/PDF 的程序化检查（像素扫描/DOM 几何/文本层），非人眼确认；发布请以本记录+PNG 快速目验为准。
