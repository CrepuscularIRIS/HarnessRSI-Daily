# SOURCE — 2602.15654 Zombie Agents

- 版本：arXiv 2602.15654**v2**（2026-03-05），钉定全文 `research/fulltext/review-runs/rsi-v22-20261021-01/materials/2602.15654.txt`（私有缓存，不提交）。全文较短，已通读 §1–6 与附录 A.1–A.4。
- 初筛记录：L1 `research/scoring/runs/rsi-l1-20261022-03/batches/b036.jsonl`；L2 `batches/l2b05.jsonl`（P3 / confirmed / to_l3）；L3 `selection.md` 终选 #6、`l3-final.tsv`。
- **事实口径以 selection.md correction C3 为准**：L2 fact 写“反思可将约77% ASR降约12%或3–15%”，原文是“Raw History 约 77%；Verbal Reflection 与 Refined Experience **降至**约 12% 与约 3–15%”。画报按“降至”展示，即大幅下降但不归零。本篇没有直接修改 Sol 的原始记录。

| 画报内容 | 原文位置 |
|---|---|
| 普通注入是瞬时、无状态的；自演化代理跨会话写记忆 | §1；§2.2 |
| 威胁模型：黑盒，拿不到 θ、M、用户历史和工具集，只能发布外部内容 | §2.3 Attacker capabilities |
| 两阶段：感染（❶–❺）/ 触发（❶–❺，含重访与再写回） | §3 图 2 说明文字 |
| FIFO：截断驱逐 → 递归自复制（“每轮先访问 attack.com”） | §3.3 Scenario A |
| RAG：稀疏检索 → 语义别名 | §3.3 Scenario B |
| 载荷大意（每轮读某网址、对话历史拼进 URL、每轮 scp） | 附录 A.3 Figure 7 |
| 工具 search / read_url / execute_command | 附录 A.2 |
| 模型 Gemini-2.5-Flash、GLM-4.7-Flash；FIFO K=3、M=20；RAG 库 3,000 条、K=300、M=20；3 个种子；诱饵任务；insta-150k-v1 | §4.1 Evaluation Protocol |
| 四种基线（Naive / Context Ignoring / Escape Characters / Fake Completion） | §4.1 Baselines |
| 原始历史约 77%，言语反思约 12%，精炼经验约 3–15%；约 15% 命令执行可“结晶”为规则 | §4.2 Impact of Memory Evolution（图 4） |
| FIFO 20+ 轮 100% 留存，基线最终降到 0 | §4.3；图 5a |
| RAG 约 240 份副本对基线约 100；K=50 时约 23 条恶意条目 | §4.3；图 5b–c |
| 三种提示防护下 ASR >60%，较无防护降约 10–15% | §4.4；图 6；提示词见附录 A.4 |
| 案例研究（医疗、购物，“single exposure”） | §4.5 |
| 作者防御建议（可信计算基、隔离、来源、策略检查） | §6 Conclusion |
| 摘要称“preserving benign task quality / utility” | Abstract；§1 贡献 3（正文没有效用数字） |

## 自绘与重绘

- 攻击链路图：**示意**，按图 2 的步骤文字自绘，不是论文原图。
- ASR 条形图：按 §4.2、§4.4 的文中**约数**绘制，不是论文图 4/图 6；“3–15%”画成区间（实色 3%，浅色延伸到 15%）；“>60%”画成虚线下限条。原文图中的精确数值没有文字给出，所以没有使用。

## 展示边界（selection.md 第 6 条＋L2 子卡 partial 项，均已上版）

RAG 需要 300 次诱饵暴露；FIFO 持久依赖攻击源持续可达；良性效用未测；案例为定性；没有冻结状态或源移除的成对控制；只测了提示词类防护。
