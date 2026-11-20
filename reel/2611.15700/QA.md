# QA — 2611.15700 AskALCF

- 渲染工具：Playwright chromium_headless_shell-1248，viewport 1240×1840，deviceScaleFactor 2（PNG 2480×3680）。
- 版式：竖版纸面瀑布对照 1240×1840——米纸底；上「900→309」前后双柱对照+去向五格，中 16 臂接受/拒绝横条+三级阶梯，下规则树 vs judge 分歧流+null 虚线对照框+限制条。与近六期版式（含 018 台账竖版 1600×2380）不同：本张以「前后瀑布对照 + 漏斗横条」为主体、更窄（1240 宽）、段落化纵向流。
- 首版渲染 2026-11-20：几何审计（叶元素 bottom≤1840、right≤1240、无横向溢出）**零违规**；字体 PosterCN 加载 true；12 横带墨量扫描全部非空。
- 目测检查（poster.png，2480×3680）：瀑布双列红/蓝 slab 与中缝 delta 箭头正常；去向五格数字对齐；16 臂横条 9+3+4 比例正确；阶梯三格 108/120/123 递进；分歧流 from→to 行完整；null 框与红色限制条无重叠；footer 来源行完整。
- 重做次数：0（首版通过）。
- 结论：**通过**。render-check.json 见 assets/render-check.json。
