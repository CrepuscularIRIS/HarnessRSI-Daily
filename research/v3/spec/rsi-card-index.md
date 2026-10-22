# rsi：领域卡匹配索引

从现有卡片直接提取名称和操作签名，剔除录用/论文数量等统计；按需回原卡看适用条件和反例。它是检索入口，不替代完整卡片或原文证据。

| 主卡 ID | 名称 | 操作签名 |
|---|---|---|
| rsi:abstract_experience_into_guidance | Abstract Experience into Reusable Guidance | act and observe an outcome → reflect or contrast to abstract guidance → write / curate the guidance store → retrieve and inject into later tasks |
| rsi:amortize_improver_into_trained_policy | > **Boundary pattern** — involves weight updates (touches L1); listed because the harness-level part is load-bearing. | improver acts (write memory, edit artifact, design workflow) → measure downstream task outcome → credit the improver's action → update improver weights |
| rsi:attribute_and_patch_incumbent | Attribute Failures and Patch the Incumbent | execute and collect traces → diagnose and attribute failures to a component → propose a localized edit → re-validate on a disjoint split → replace the incumbent (or roll back) |
| rsi:coevolve_the_evaluator | Co-Evolve the Evaluator | observe policy outputs → expose evaluator blind spots → revise criteria/tests → validate against a trusted anchor → use as reward or acceptance gate |
| rsi:couple_context_and_weight_updates | > **Boundary pattern** — involves weight updates (touches L1); listed because the harness-level part is load-bearing. | adapt in context → collect experience-shaped rollouts → train weights on them → re-adapt context for the updated model |
| rsi:crystallize_executable_capability | Crystallize Solutions into Executable Capabilities | solve or practice a task → abstract the solution into parameterized code → execute/test to verify → register in the action space → compose on later tasks |
| rsi:diagnose_self_improvement | Diagnose Whether Self-Improvement Is Real | name the confound behind a rising evolution curve → build a matched, frozen, held-out, or adversarial condition that kills it → measure the isolated effect → report the failure mode as the finding |
| rsi:evidence_gated_retention | Gate Retention on Measured Evidence | propose a candidate entry or change → measure its marginal effect (paired, held-out, utility credit) → admit, demote, or roll back → keep provenance |
| rsi:index_experience_for_reuse | Index Raw Experience for Reuse | record episodes/cases → structure the store (index, hierarchy, graph, tiers) → retrieve relevant precedent when needed → adapt it and append the new outcome |
| rsi:make_the_improver_editable | Make the Improver Editable | improver proposes a change → apply it to the task agent and/or the improver → evaluate descendants → retain (incumbent or archive) → recurse |
| rsi:population_search_executable_fitness | Search a Population Against an Executable Fitness | sample parents from the population → LLM mutates / recombines → score with an executable fitness on a selection split → select (elite, frontier, quality-diversity) and archive → report on a disjoint split |
| rsi:search_agent_architecture | Search the Agent's Architecture | declare a design space of modules / topologies / workflow code → propose designs → execute and score them → retain, cache or adapt the structure that wins |
| rsi:self_generate_the_curriculum | > **Boundary pattern** — involves weight updates (touches L1); listed because the harness-level part is load-bearing. | estimate frontier or weakness → generate tasks/environments → verify solvability and difficulty independently of the generator → train the learner → re-estimate and regenerate |

主卡原文：`patterns/main/<id>.md`。子卡候选从主卡的 Sub-patterns 表中选择，按需读取 `patterns/sub/<id>.md`，输出 `rsi:<id>`。不把领域 Cxx 与 ResearchStudio Cxx 混用。
