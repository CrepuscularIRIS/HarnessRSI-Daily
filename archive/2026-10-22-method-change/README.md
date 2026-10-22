# 2026-10-22 方式切换归档

用户决定停用 v2.2 双席打分流水线，改用新的打分方式（规格另行给出）。本目录集中归档：

## docs/
- `digest-pipeline.md` — 继承的 arXiv digest 抓取用法（对应工具一并归档）
- `START_CC.md` — 旧 claude-kimi 启动指令（对应已停用的 v2.2 流程）
- `RESET_2026-10-21.md` — 2026-10-21 重置事件记录（归档为历史；事件结论已并入 AGENTS.md）

## tools/
- `main.py`、`digest.py`、`llm.py`、`logger.py`、`rss.py` — 继承的候选抓取管线
- `test_digest.py`、`test_llm.py`、`test_net.py` — 上述工具的测试
- `keywords.json`、`config.example.json` — 抓取配置

保留未动：`skills/arxiv-fetch/`（独立插件）、卡片检查（check_cards.py + test_check_cards.py + cards/）、
`research/net.py` 与 v2 工具（stdlib/已有依赖即可运行）。

v2.2 run（rsi-v22-20261021-01）中断于 218/930 已处置；全部批次记录、队列与 930 篇钉定全文
（本地 gitignored）保留原位，供新方式复用。git 历史可完整恢复本目录任何文件。
