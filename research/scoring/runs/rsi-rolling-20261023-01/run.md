# Rolling run rsi-rolling-20261023-01（HarnessRSI Daily 增量轮）

- 规则：problem-core-v1.1（PROBLEM_CORE / SOL_BATCH_PROMPT，2026-10-22 版）。
- 启动：2026-10-23 00:17 巡检班；Git HEAD 1730e104ec40947e5df3908b5c3bd7fde39e4f4f；patterns 卡片版本 5d46c9f。
- 输入：inbox/2026-10-22-0000.jsonl 12 篇新候选（arXiv API 元数据入库，corpus 1597→1609），材料位置 research/scoring/runs/rsi-rolling-20261023-01/l1_materials/。
- 模型：6.1 Sol（claude-kimi `sonnet` 槽 → gpt-6.1-sol），CC 内置 Subagent，单初评席；总控为 CC 会话。
- 批大小：增量小批（<20 篇/批允许，SOL_BATCH_PROMPT 起步值为批量场景）；并发 4（本班单批）。
- L2 预算（2026-10-27 增量轮声明修订，替代原 max(3, 20%×累计 L1) 上限——该默认在稳态小增量下会使 L2 永久饿死）：每班 = 本班 L1 产生的 to_l2 全部 + 上班遗留 high 队列最多 5 篇；漏检抽查名额 = 每班预算 10% 取整（0 则累计欠账，攒够 1 立即补抽），种子记入 l2-queue。token 不设硬额，逐批记录用量。
- 授权：用户 2026-10-23 会话授权的 6 小时巡检管线。
