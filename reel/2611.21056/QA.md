# QA.md — 2611.21056（先探索，后整合）

视觉与几何 QA 记录。执行模型：glm-5.3（日班单席）；日期：2026-11-19。

## 流程

1. 首版画布 1800×1440：自动检查两处不合格——`textOverflow: DIV.children`（7 子代列过窄）与三个 `.num` 大数字 scrollHeight 裁切（中文降部）——判不合格，按一次重做处理。
2. 重做：`.fanrow` 列宽改为 150px/46px/1fr/56px/300px 固定分配（children 得到完整宽度），大数字统一加 line-height 与 padding-bottom；重渲染后溢出/裁切/横向溢出三项全空。
3. 二次墨量扫描发现 bands 7–9（y840–1200）ink≈0.002——`.strip` 三张 stat 卡因 flex:1 拉伸后内容置顶、卡内下方 350px 空白死区；同轮修复：`.stat` 改 justify-content:space-between + 行距加大，`.tline` 数据块沉底。重渲染后 bands 全部落在 0.016–0.211，无空白带（0.016 为标题-扇形图间隙）。
4. 最终几何（`assets/render-check.json`）：页面 1800×1440；lim 底与 footer 顶间隔 45px；溢出、裁切、横向溢出列表全空；字体 true。
5. 版式：纸面扇形展开图（父代→7 探索子代→整合后代横向谱系 → 三张数据卡 → 陶土色限制条）。与近三期及本期另两张（米色横向审计报告、暗底三权分立竖版）不重合。

## 结论

通过。编辑源：`poster.html`；交付：`poster.png`、`poster.pdf`、`SOURCE.md`、本文件。结构检查不等于科学验证。
