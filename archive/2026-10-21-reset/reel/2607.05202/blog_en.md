# EvoAgentBench: only the benchmark's own reference improves all 24 cells, and 6 of those gains are inside the noise

*A Reel interpretation of [arXiv 2607.05202v1](https://arxiv.org/abs/2607.05202v1) (HarnessRSI Daily score 72, ★★★). Data: [EverMind-AI/EvoAgentBench](https://huggingface.co/datasets/EverMind-AI/EvoAgentBench).*

## What the benchmark measures, and what changes

EvoAgentBench is a benchmark, so nothing in it rewrites itself. It evaluates **self-evolution methods that turn past trajectories into external artifacts** (a case bank, a reasoning-memory pool, one evolved prompt, skill files) and then reuse them on new tasks. Model weights do not change. The artifact is built from the training split only (task prompts, verifier outcomes, the method's own rollouts); no test answers are available. There is no accept/reject rule inside the benchmark: an artifact is judged only by its **transfer gain**, the mean over held-out test tasks of (score with evolution − score of the no-evolution Vanilla agent).

The central design choice is "ability-supported yet instance-disjoint". The authors extract **Abilities** from agent traces (a trigger, a reusable procedure, a boundary and a role: Method, Guard or Workflow):

1. Run no-skill agents (Kimi-K2.5, GLM-5.1, DeepSeek-V3.2, two scaffolds, two runs each) on 2,605 source tasks from BrowseComp-Plus, SWE-Bench Verified, LiveCodeBench and GDPVal.
2. Claude Sonnet 4.6 reads each task's traces and ground-truth target and writes raw Ability cards (7,326 cards from 2,516 tasks).
3. Cards are merged into 170 canonical Ability families by embedding blocking, three LLM adjudicators and domain experts (unanimous pairs accepted; experts review every non-unanimous pair and split inconsistent groups).
4. Tasks that share a family form a graph (1,108 tasks); after community detection, a task enters the test split only if it shares an Ability with a training task in its own community (Section 3.2.5; the Appendix A.6 algorithm states the support condition without the community clause). The result is 528 training and 267 test tasks, with zero unsupported test tasks. Test tasks were also preferentially drawn where the no-evolution scores of the three construction backbones (Kimi, GLM, DeepSeek) left headroom, not the Qwen/Gemma evaluation baselines.

## Headline result, as reported

Six settings: two scaffolds (OpenClaw, Nanobot) times three backbones (Qwen3.5-27B, Qwen3.5-397B, Gemma-4-31B). Each cell is the mean of three runs per instance with a standard error. Four conditions are compared with Vanilla: Memento (retrieves the closest stored case), ReasoningBank (retrieves distilled strategies), GEPA (one evolved prompt for all tasks) and **Anchor Skill**, the benchmark's own Ability-grounded skills retrieved by the test task's curator-side Ability label. Anchor is explicitly "not a deployable method".

Average accuracy (%, four domains, both scaffolds) and gain over Vanilla (Table 3):

| Backbone | Vanilla | Memento | ReasoningBank | GEPA | Anchor |
|---|---|---|---|---|---|
| Qwen3.5-27B | 37.5 | 35.1 (−2.4) | 41.1 (+3.6) | 38.7 (+1.2) | 45.0 (+7.5) |
| Qwen3.5-397B | 49.2 | 50.7 (+1.5) | 51.6 (+2.4) | 52.7 (+3.5) | 59.7 (+10.5) |
| Gemma-4-31B | 36.7 | 36.0 (−0.7) | 37.1 (+0.4) | 42.4 (+5.7) | 42.5 (+5.8) |

The paper's headline: Anchor improves in all 24 backbone-domain-scaffold cells, while every automatic method has negative transfer in at least one. Anchor's skill content comes from construction backbones that are disjoint from the evaluation backbones, which the authors read as Ability content transferring across model families, and they say the gap "cannot be attributed to evaluation noise or task difficulty". With three runs on 56 to 86 tasks per domain and no significance test, note that 6‡ of Anchor's 24 gains are smaller than the cell's own SE (including +0.4 on Gemma-4-31B / OpenClaw / Algo). Anchor exceeds the best automatic method by +3.9 and +7.0 on the two Qwen backbones; on Gemma-4-31B GEPA nearly matches it.

## The controls that decide whether the gain is real

- **Matched environment.** Within a setting, tasks, MCP tools, timeouts, scoring and base agent configuration are identical across methods, and every evolution state is built from the training split before test evaluation starts. The paper says automatic methods learn from rollouts of the very scaffold-backbone pair used at test time, whereas Anchor's content comes from other backbones.
- **Repeats.** Three independent runs per instance, reported as mean ± SE (cell SEs range from 2.2 to 5.9 points). The paper does not state whether the evolution step itself is repeated, and reports no significance test.
- **Anchor is a diagnostic, not a competitor.** It uses curator-side extraction and the test task's Ability label for retrieval; the paper says so.
- **Different teachers.** Anchor's skills are written by Claude Sonnet 4.6, which reads the ground-truth target and the traces of three other backbones (Kimi, GLM, DeepSeek). The automatic methods learn from rollouts of the evaluated model itself, and some of those cells sit near the floor (Vanilla Web accuracy 8.7 to 13.3 for Qwen3.5-27B and Gemma-4-31B). Section 3.1 allows construction traces as training input, but no experiment gives them to the automatic methods. The authors argue the protocol, if anything, favours the automatic methods; still, the Anchor margin mixes content source, teacher access and routing, and the conclusion that the gap lies in "method-side extraction and routing" is an inference, since no experiment swaps routing or extraction between methods.
- **Cost.** The paper reports only test-time turn changes versus Vanilla (Table 4). It does not report the cost or compute of the evolution step; the only budget it states is a top-10 retrieval budget for skill- and case-based methods (Appendix A.6).
- **Split design and leakage.** The benchmark's claim is that an Ability-aware split makes transfer measurable; the paper does not compare it with a random split. Appendix B (Table 8) specifies an access-control protocol (no test answers, test traces or test raw cards reach the automatic methods or Anchor), but the paper reports no empirical leakage or near-duplicate test between test and training tasks.

## Where the gain is absent or small

- **Automatic methods are brittle at the cell level.** Negative cells out of 24: GEPA 4, ReasoningBank 6 (both from the paper) and Memento 7‡ (our count from Table 3); Anchor has 0. Memento's worst cell is Nanobot / Qwen3.5-27B / SWE, 45.8 → 9.5 (−36.3); the other seven Memento cells on that backbone are positive, so its −2.4 average comes from this one cell. GEPA has −12.3 on OpenClaw / Qwen3.5-27B / knowledge work; ReasoningBank has −10.9 on OpenClaw / Gemma-4-31B / Algo.
- **Many gains are inside the noise.** In 16‡, 11‡ and 14‡ of 24 cells the gain of Memento, ReasoningBank and GEPA is smaller than that cell's own SE (Anchor: 6‡); this compares each Δ with a single cell's SE, not with the SE of a difference. Test sets have 56 to 86 tasks per domain.
- **Anchor is not best everywhere.** An automatic method scores above Anchor in 3‡ of 24 cells: ReasoningBank 53.0 vs 49.4 (Nanobot / 27B / SWE), and GEPA 42.3 vs 32.7 and 37.5 vs 26.8 on Gemma-4-31B SWE. On Gemma-4-31B the average gain is +5.8 for Anchor and +5.7 for GEPA.
- **Cost does not follow accuracy.** Anchor lowers turn counts in four of six settings (down to −8.8%) but adds +7.6% and +32.7% on Gemma-4-31B; GEPA raises turns in four of six; on Gemma, Memento, GEPA and ReasoningBank all add double-digit overhead.
- **Limits stated by the authors.** Four text domains and three open-source construction backbones; one LLM extractor shapes the Ability vocabulary; absolute gains are specific to this headroom-selected split, not expected gains on random tasks; evaluation backbones may have seen the source benchmarks, which the authors argue shifts absolute scores, not the comparisons.

## Our read

HarnessRSI score **72**, band ★★★, evidence level **retained**: the retained artifacts (skills, cases, memory, a prompt) are compared with a no-evolution agent on held-out tasks. The paper reports a held-out split by construction, three runs per instance with standard errors, a fixed environment across methods, and a retained-artifact comparison of artifacts against Vanilla. It does not report evolved artifacts carried from one domain to another, the cost of the evolution step, a comparison of the improvement mechanisms themselves, or an empirical leakage test (it specifies an access-control protocol in Appendix B). Within-domain transfer to held-out tasks is the benchmark's own design (Table 1 marks it cross-task).

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
