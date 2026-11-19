# QA.md — 2611.15309（自洽权分给谁）

视觉与几何 QA 记录。执行模型：glm-5.3（日班单席）；日期：2026-11-19。

## 流程

1. 首版画布 1500×1800：几何与裁切检查全过（无溢出、无裁切、字体 true），但墨量扫描 band 10（y1500–1650）light=0.000——`.lim` 限制框（底 1488）与 footer（顶 1749）之间 260px 纯背景空白死区——判不合格，按一次重做处理。
2. 重做：`.tri` 与 `.exp` 设 flex 拉伸、`.exp` 内容 justify-content:center、`.col`/`.lim` 增大内距与行距，`.lim` 加 margin-bottom 避开 footer（首调 1756 vs 1749 重叠 −7px → margin-bottom 52px 后 gap 45px）。
3. 最终几何（`assets/render-check.json`）：页面 1500×1800；header 底 293 / tri 底 873 / exp 底 1612 / lim 底 1704 / footer 顶 1749；溢出、裁切、横向溢出列表全空；字体 true。
4. 12 横带墨量扫描（暗底亮墨口径 light>110）：0.016–0.101，无空白带。
5. 版式：暗底三权分立竖版（三平栏 govern/propose/judge 各配 owner 与对照 → 裁判可见性六行对照表 → 双代码案例 → 虚线限制框）。与近三期及本期另两张（米色横向审计报告、纸面扇形展开）不重合。

## 结论

通过。编辑源：`poster.html`；交付：`poster.png`、`poster.pdf`、`SOURCE.md`、本文件。结构检查不等于科学验证。
