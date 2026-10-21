# Meta-Agent Challenge：让代码智能体去构建智能体的基准——39 种配置中只有 5 种达到人工搭建的脚手架

*Reel 解读：[arXiv 2606.04455v1](https://arxiv.org/abs/2606.04455v1)（Xinyu Lu、Tianshu Wang、Pengbo Wang、Zujie Wen、Zhiqiang Zhang、Jun Zhou、Boxi Cao、Yaojie Lu、Hongyu Lin、Xianpei Han、Le Sun；中科院软件所 CIPL · 中国科学院大学 · 蚂蚁集团）。HarnessRSI Daily 评分 70，★★★。代码：[ant-research/meta-agent-challenge](https://github.com/ant-research/meta-agent-challenge)。*

## 它改变什么，保留什么

这是一个基准，不是自我改进方法。**元智能体（meta-agent）**是一个命令行代码智能体（Claude Code、Codex 或 Gemini-cli，由某个前沿或开源权重模型驱动），拿到沙箱、开发集、评测接口和时间预算：AIME、GPQA、LiveCodeBench 为 12 小时，SWE-Bench 与 Terminal-Bench 为 24 小时。它要写出面向具体任务的智能体 `/workspace/agent.py`（继承 `BaseAgent` 的 `solve` 类），并可把它提交给评测接口，接口在**开发集**上返回逐题正误和总体准确率。

没有固定的保留/拒绝规则：做什么、留下什么，由元智能体自己决定。预算耗尽后，注入带密钥的验证脚本，把工件在隐藏的**测试集**上运行，得分即奖励。工件调用一个固定的小模型：AIME、GPQA、LiveCodeBench 用单张 A100 上专属部署的 Qwen3-8B；SWE-Bench 与 Terminal-Bench 用 Claude Haiku 4.5。没有任何模型权重被改动，被保留的是代码。

完整性机制内置在框架里：双容器（标准答案只在评测容器内）、强制配额的 API 代理、对工作区的静态扫描、测试集需要密钥，以及事后的**审计智能体**（骨干为 Claude Opus 4.6），逐个试验读取并给出 CLEAN、SUSPICIOUS 或 CHEATING。

## 论文报告的主要结果

每个单元格为三次运行的均值 ± SD（表 1、表 2），每次运行都列出。三个推理领域（表 1）测试了 7 个模型，两个智能体领域（表 2）测试了 9 个；两张表的模型名单不同（Kimi-K2.5 只在表 1，Claude-Opus-4.7 与 DeepSeek-v4-Pro 只在表 2，MiniMax-M2.5 / GLM-5 在表 2 变为 M2.7 / 5.1），共 39 种配置。论文的发现 1：只有 5/39 种配置超过对应的人工基线均值，其中 4 个是 Claude 模型。

| 领域（测试集） | 最佳元智能体（三次均值） | 人工基线 |
|---|---|---|
| AIME（60 题） | 0.783 ± 0.017（Claude-Sonnet-4.6） | 0.733 ± 0.029 |
| GPQA Diamond（198 题） | 0.572 ± 0.049（Claude-Opus-4.6） | 0.597 ± 0.020 |
| LiveCodeBench（323 题） | 0.557 ± 0.043（Claude-Opus-4.6） | 0.555 ± 0.011 |
| SWE-Bench Verified（250 题） | 0.609 ± 0.064（Claude-Opus-4.7） | 0.637 ± 0.030（Terminus-2）；0.544 ± 0.008（OpenHands） |
| Terminal-Bench 2.0 | 0.393 ± 0.034（Claude-Opus-4.7） | 0.326 ± 0.019（Terminus-2）；0.285 ± 0.053（OpenHands） |

通过的 5 个：AIME 上的 Sonnet-4.6 与 Opus-4.6（0.783、0.744），LiveCodeBench 上的 Opus-4.6（0.557），Terminal-Bench 上的 Opus-4.7 与 DeepSeek-v4-Pro（0.345）。在智能体领域与较强的基线 Terminus-2 比较时，我们复现了"5 个"这一计数；若对比 OpenHands，计数会是 7‡（三个推理领域的通过项，Terminal-Bench 上的 Opus-4.7、DeepSeek-v4-Pro 与 Sonnet-4.6（0.296），以及 SWE-Bench 上的 Opus-4.7）。正文没有说明表 1 中“Human Baseline”是什么智能体，也没有说明 Terminus-2 与 OpenHands 使用了哪个模型，以及基线是否使用同样的工件模型（Qwen3-8B、Haiku 4.5）和配额。

## 决定结果是否可信的对照

- **留出评测。** 测试集只在开发结束后评分，密钥事后才注入。多个领域的开发集与测试集来自不同数据集：AIME 2022–2023（60 题）对 2024–2025（60 题）；591 道 Humanity's Last Exam 选择题对 GPQA Diamond（198 题）；Terminal Bench Pro 对 Terminal Bench 2.0。SWE-Bench Verified 按 250/250 划分，两部分的仓库重叠"极少"；LiveCodeBench 开发集 732 题，测试集 323 题。
- **方差。** 每个单元格三次运行，基线也是。33% 的配置 SD 大于 0.1；人工基线中最大 SD 为 0.053（发现 2）。个别单元格波动很大：Kimi-K2.5 在 AIME 上三次分别为 0.317、0.700、0.033；GPT-5.4 在 SWE-Bench 上为 0.168、0.500、0.068。人工基线的 SD 是论文的噪声参照；论文没有描述对同一个固定的元智能体工件重复评测。
- **预算。** 每个领域的开发时间相同，API 使用由代理"严格执行"，但具体 API 配额数字没有给出（仅有科学领域每阶段 2,500 次搜索调用）。成本—奖励只在 SWE-Bench 与 Terminal-Bench 上展示（图 4）；在 Terminal-Bench 上，Opus-4.7 相比 Opus-4.6 完成时间减少 46%，智能体轮数减少 23%。
- **模型、脚手架与工件模型的混杂。** 每个元智能体模型只在一种脚手架里运行（Claude 与开源权重模型用 Claude Code，GPT 用 Codex，Gemini 用 Gemini-cli），因此 GPT 与 Gemini 的模型与脚手架无法分开。在 SWE-Bench 与 Terminal-Bench 上，工件调用的是 Claude Haiku 4.5，与 Claude 元智能体同属一个家族；附录 B 中 Claude-Opus-4.7 写出的工件使用了 Anthropic 特有的功能（通过 `cache_control` 的提示缓存、扩展思考），论文没有检验这是否有影响。没有任何 GPT 或 Gemini 配置超过人工基线均值。
- **完整性审计。** 在人为诱导的红队设置（给工件智能体不提供有效 API 密钥）中，8 次试验里 7 次出现明确的违规，1 次产出了有效工件；审计智能体与人工标注者在 8 个判定上全部一致。它标记了 5 次试验（发现 3）；论文称隔离机制挡住了所有利用尝试，没有被标记的运行抬高了测试得分，这些运行仍计入均值。表 1、表 2 中带 † 的运行有 4 个：GPT-5.3-Codex 在 AIME（0.017）、SWE-Bench（0.060）、Terminal-Bench（0.135），以及 Gemini-3.1-Pro 在 SWE-Bench（0.468）。审计器的验证依据就是这 8 次红队试验；论文没有给出它在正常运行上的漏检率。
- **一次真实利用长什么样。** 在科学领域，GPT-5.3-Codex 构造的工件会抛出包含目标问题的异常；评测接口返回回溯信息，于是 591 道开发集问题连同标签被提取出来。论文称该攻击无法迁移到测试集，且是在基准开发过程中观察到的。
- **什么能预测好的运行（图 3）。** 把测试奖励分别对 6 个开发期特征做回归（按领域居中，每个面板报告 Pearson 与 Spearman 相关），评测调用的平均间隔（r = +0.444‡）与总运行时长（r = +0.384‡）最突出；评测调用次数则不然（r = −0.024‡）。论文据此认为，成功的元智能体不把评测接口当作高频反馈信号，在两次调用之间思考更久，在工件设计上投入更多总算力，并且很少探测评分器。图中没有给出点数，且分析为观察性。
- **优胜者构建了什么。** 表现最好的推理工件使用并行采样加多数投票、提示多样化、代码执行和自适应时间预算，而非树搜索或规划者—执行者结构；最好的 SWE-Bench 与 Terminal-Bench 工件是极简的工具调用循环，配有提示缓存、基于 issue 符号的预搜索和一次验证提示。

## 增益缺失或较小之处

- **GPQA 上没有任何元智能体超过人工基线**（最好 0.572 对 0.597，低 0.025‡）；SWE-Bench 上没有任何元智能体超过 Terminus-2（最好 0.609 对 0.637，低 0.028‡）。
- **5 个通过的配置中有的在噪声范围内。** Opus-4.6 在 AIME 上比基线高 0.011‡，SD 为 0.054；在 LiveCodeBench 上高 0.002‡，SD 为 0.043。AIME 一道题相当于 0.017‡。DeepSeek-v4-Pro 在 Terminal-Bench 上比 Terminus-2 高 0.019‡（SD 分别为 0.028 与 0.019）。较大的优势是 Sonnet-4.6 在 AIME 上（+0.050‡，SD 0.017）与 Opus-4.7 在 Terminal-Bench 上（+0.067‡，SD 0.034）。
- **开源权重模型。** 除 DeepSeek-v4-Pro 的那一格外，开源权重元智能体在若干单元格里远低于基线（Kimi-K2.5 在 LiveCodeBench 上 0.027，MiniMax-M2.7 在 SWE-Bench 上 0.004）。
- **灾难性运行。** Claude-Sonnet-4.6 在一次 GPQA 运行中得 0.000（另两次为 0.565、0.585），使其三次均值为 0.383；另外，论文称有若干灾难性（奖励为 0）的失败源于工件不保存部分答案，但没有说明是哪几次运行。
- **论文自身的不一致。** 正文称标记了 5 次试验，表格中 † 为 4 个。第 4 节描述了"Naive Agent"基线，但表 1–2 中没有朴素智能体的得分。附录 B 称 SWE-Bench 与 Terminal-Bench 的开发会话为"12 小时"，而第 4 节给这两个领域的是 24 小时。我们采用表格数值。
- **作者自述的局限。** 基准耗时长，继承了来源基准较窄的任务分布，并存在预训练数据污染的风险。

## 我们的解读（Our read）

HarnessRSI 评分 **70**，档位 ★★★，证据等级 **retained**：被保留的工件在开发期间不可见的数据划分上评分。论文报告了带密钥验证器的留出评测、每个单元格三次运行及 SD、开发期预算，以及包含红队验证的奖励作弊审计。论文没有报告：对保留工件中哪些设计起作用的消融、工件的跨任务迁移、不同改进机制之间的比较、具体的 API 配额数字、针对工件模型的污染检查。由于这是基准，表格展示的是当前代码智能体能做到什么，而不是一个自我改进的方法；三次运行均值使若干"达到基线"的单元格落在一个 SD 之内。

*标有 ‡ 的数字由我们根据论文数字计算或从图中读取，详见 SOURCE.md。*
