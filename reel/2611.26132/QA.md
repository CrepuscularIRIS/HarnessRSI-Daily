# QA — 2611.26132 AdaObs

- 渲染：playwright chromium_headless_shell-1248，viewport 1720×1620，deviceScaleFactor 2。
- 产出：poster.pdf（1720×1620 单页）、poster.png（3440×3240）。
- 几何审计：0 溢出（overflow=[]）。
- 字体：PosterCN woff2 加载成功（fontLoaded=true），中文全部正常渲染。
- 墨带扫描：无塌陷空带（inkBandsEmpty=[]）。
- 目测核对（poster.png 实际打开检查）：浅米底三阶梯瀑布 + 左侧解耦双盒 + 三结果卡结构完整；L1/L2/L3 三级色带（teal/indigo/rust）清晰区分；66.4→73.7 主柱、双后端迁移哑铃、消融饼图无裁切无重叠；饼图已标"示意"（原文 Table 4 数值在缓存全文截断）。
- 版式与近三期及本期另两张不重复：浅底三阶梯瀑布（左窄右宽双列 + 底部三结果卡）在 017–019 无同类。
- 重做次数：0，一次通过。
- 结论：PASS，发布。
