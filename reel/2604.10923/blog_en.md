# Mem²Evolve: two memories co-evolve — reusable capabilities and the experience that builds them

*A Reel interpretation of [arXiv 2604.10923v1](https://arxiv.org/abs/2604.10923v1) (HarnessRSI Daily score 65, ★★). No code link supplied for this Reel.*

## What the system changes about itself

Mem²Evolve retains **two linked memories**, not newly trained model weights. **Asset Memory** holds executable MCP tools and expert-agent specifications: roles, expertise, behavioural suggestions and available tools. **Experience Memory** holds implementation recipes and agent strategies distilled from successes and failures. Experience guides asset creation and execution; newly created assets generate further trajectories from which experience is distilled. That is the co-evolution: capabilities and experience, not a policy-weight update.

## The loop, and the keep/reject rule

1. Plan sub-tasks. Retrieve a top-matching expert and relevant tools from Asset Memory. If similarity does not clear a threshold, create the missing capability using relevant experience and web documentation.
2. Execute with ReAct and aggregate the answer. An LLM judge evaluates the task, trajectory and answer, producing success/failure and critique. The method explicitly assumes ground-truth labels are unavailable for backward evolution.
3. Admit a new asset when the task succeeds **and** the asset passes all tests synthesized by the LLM from its critique. Otherwise revise it using critique and failing tests, regenerate tests and repeat until validation passes. The paper specifies no retry cap, terminal discard rule or independent held-out regression test. This is a local admission check, not selection by later benchmark improvement.
4. Append lessons from successful and failed trajectories to Experience Memory. The paper does not specify a separate rejection rule for these memory items. Its templates preserve task context and outcomes; tool-memory entries include complete implementation code.

## Headline result, as reported

Using GPT-5-chat, Table 2 reports an eight-benchmark **average of 70.24**, against **63.78 for Alita**, **58.44 for AFLOW** and **51.71 for CoT**. The paper's 6.46%, 11.80% and 18.53% improvements are percentage-point differences, not relative percentage gains. This is an average of benchmark-level scores with **no reported variance, confidence interval or run count**; we cannot label it a single-run result or identify a best seed/checkpoint.

| Benchmark | Mem²Evolve | Strongest baseline in that column |
|---|---:|---|
| GAIA Total | 76.31 | 72.73 (Alita) |
| ALFWorld | 94.31 | 93.40 (AFLOW) |
| HotpotQA | 60.80 | 60.80 (AFLOW; tie) |
| 2WikiMultihopQA | 82.00 | 81.80 (Direct) |
| AIME24 | 76.70 | 70.00 (Alita) |
| AIME25 | 73.33 | 66.67 (Alita) |
| TravelPlanner | 59.25 | 59.14 (SwarmAgentic) |
| WebShop | 39.20 | 37.90 (AFLOW) |

Despite the main table's Pass@1 caption, Appendix B.2 specifies mixed metrics: exact match for QA, success rate for ALFWorld/WebShop, and a five-metric delivery/constraint average for TravelPlanner. Our arithmetic shows Mem²Evolve's GAIA Total matches the unweighted mean of its three difficulty-level scores; Alita's Total does not follow that same rule. A consistent GAIA aggregation rule is not specified, so this is unresolved, not something we correct. We retain the reported totals and do not interpret them as pooled item success rates. The eight-column average reconciles to the reported headline. OpenAI DeepResearch's GAIA result, 67.36, is imported from its original paper, not a same-backbone rerun.

## The controls that decide whether the gain is real

- **Component ablations (Tables 3 and 6).** Full system 70.24; without tool creation 59.96; without expert-agent creation 68.52; without tool memory 67.11; without agent memory 65.51. These support contributions from both memories and creation mechanisms, but have no reported variance or compute-matched alternatives.
- **Gain concentration matters (Table 6).** Removing tool creation drops GAIA from 76.31 to 21.69, AIME24 from 76.70 to 66.67, and AIME25 from 73.33 to 60.00. The same removal barely changes ALFWorld (94.31 to 94.10) or WebShop (39.20 to 39.05). Tool memory is likewise most helpful on GAIA/math: GAIA 76.31 versus 67.47 without it, but ALFWorld 94.31 versus 94.25 and WebShop 39.20 versus 39.15. Agent memory has a different profile: TravelPlanner 59.25 versus 49.36 without it, ALFWorld 94.31 versus 88.06. The average is not a uniform benefit everywhere.
- **Experience-guided generation (Table 4).** Mean first-pass tool validity rises from 53.1% to 72.4%; mean improvement iterations fall from 1.01 to 0.48. GAIA validity is 32.7% versus 51.0%, AIME24 64.9% versus 83.8%, AIME25 61.8% versus 82.4%. These are averages without reported uncertainty or generation sample counts. Fewer debugging iterations are an efficiency proxy, not measured end-to-end cost.
- **Retained-memory evaluation (§5.3, Figure 3).** The main table starts with no prior memory beyond web search. In the separate same-task study, memory is accumulated on a benchmark subset (25%‡ or 50%‡ in Figure 3), then tested on the remaining items. The authors report gains with diminishing returns. The remaining-set sizes, item/group split details and whether memory updates are frozen during evaluation are not stated.
- **Cross-task reuse (§5.4, Figure 4).** GAIA-derived memory initializes seven other benchmarks and improves over no initial memory, with results described as comparable to 25% in-domain initialization. This is one donor benchmark with the same reported backbone, not cross-model transfer. The study does not separately equalize the memory-accumulation budget or report error bars.
- **Baseline access and tuning.** The paper states that experience-centric frameworks and Mem²Evolve start from a minimal web-search configuration; tool-generative baselines can create tools. This is not uniform tool access across naive baselines: Direct is explicitly tool-free, CoT's search access is not established, and ReAct permits web search. Alita is not experience-free: Appendix B.1 describes its Promptist and Experience Pool, and says the experiments use OpenAlita because official code is unavailable. There is no controlled baseline-plus-Mem²Evolve-dual-memory/admission-loop comparison. Numerical retrieval defaults and the split used to select hyperparameters/defaults are not reported, nor are baseline tuning budgets. Do not infer that the baselines were weakened.
- **Leakage and cost.** The judge lacks ground truth, but that does not establish leakage-free memory: task contexts, outcomes and implementations can be retained, and same-benchmark relatives could remain across the subset/remainder split. We found no overlap/near-duplicate or web-search contamination audit in the full appendix. This is an unresolved risk, not evidence that leakage occurred. Tokens, dollars, wall-clock time and memory-accumulation/storage growth costs are not quantified; there is no matched-compute row.

## Where the gain is absent or small

HotpotQA ties AFLOW at **60.80**. 2Wiki's **82.00 versus 81.80** and TravelPlanner's **59.25 versus 59.14** are narrow differences with no uncertainty estimate, so their reliability is unresolved. The larger gaps to the strongest per-column baselines are on math and GAIA; the tool-creation ablation is dominated by these same benchmarks. All headline comparisons use one reported backbone. Full benchmark test sizes in Table 5 are 166 GAIA, 134 ALFWorld, 500 each QA benchmark, 30 each AIME, 1,000 TravelPlanner and 251 WebShop; they are not the remaining-set sizes of the initialized-memory experiment.

## Our read

HarnessRSI score **65**, band **★★**, evidence level **retained**. The stored judgment credits partial held-out evidence, cross-task reuse and retained-component ablations; variance, budget matching, optimizer cost, improver comparison and leakage guards remain unclear. The paper makes the two-way interaction concrete and checks tool-generation reliability, but does not show a budget-matched improvement of the improvement mechanism itself. Our reading is that the evidence supports reusable memory and task-dependent capability expansion, not a compute-controlled claim of increasingly better self-improvement. The score's code credit comes from the paper's availability claim; no repository was supplied or verified for this Reel (see SOURCE.md).
