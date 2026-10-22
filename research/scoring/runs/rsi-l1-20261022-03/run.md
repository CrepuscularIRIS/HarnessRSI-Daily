# run rsi-l1-20261022-03 — problem-core-v1.1 全量 L1（1597 篇）

- 触发：用户 2026-10-22 试点审后授权「跑」；范围=corpus 全部 1597 篇（含 689 篇 abstract-only，走 needs_material 排队），L2 预算=L1 篇数 20%（约 319 篇）+ 预算 10% 漏检抽查（随机种子届时记录）。
- 规则：research/scoring/，problem-core-v1.1。试点见 rsi-pilot-20261022-02/PILOT_REPORT.md。
- 执行：6.1 Sol（CC Agent model type sonnet）单席；4 并发滚动补位，额度允许升 6–8；L1 每批 20 篇，共 80 批。
- 材料：l1_materials/ 1597 篇（908 abstract_intro + 689 abstract；25 篇全文标题匹配失败降级摘要），自钉定缓存切出，零新增抓取。
- 卡片版本：patterns/ sha 汇总 343dc4a1c6b58e84（51 文件），run 内固定。
- Git HEAD：11af8044c3bef112c0497f18c19c01e4684fb23e
- 产物：batches/bNNN.jsonl（L1）→ L2 队列（high→medium，20% 截断）→ SELECTION → Opus 5.5 L3。
- 校验：check_record.py --stage L1 逐批；结构通过≠判断正确。
