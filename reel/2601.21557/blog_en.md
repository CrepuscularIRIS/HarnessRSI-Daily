# MCE: evolving how an agent builds context, not just the context it builds

*A Reel interpretation of [Meta Context Engineering via Agentic Skill Evolution, arXiv 2601.21557v2](https://arxiv.org/abs/2601.21557v2). Haoran Ye, Xuning He, Vincent Arak, Haonan Dong, Guojie Song · Peking University. HarnessRSI score 63, ★★.*

## What changes, and what is kept

MCE changes both a **context-engineering skill** and the **context artifact** that skill produces. Skills are not model weights or merely demonstration prompts: they are workspace folders of natural-language instructions, potentially executable scripts, context templates, validation protocols and retrieval logic. A base agent executes the skill to edit knowledge files and a Python query-to-context retrieval function. The inference model then receives that retrieved context in a one-shot call.

The default meta/base agentic model is MiniMax M2.1. DeepSeek V3.1 performs task inference and reflection; AEGIS instead uses Qwen3-8B for task inference. The base agent may call DeepSeek V3.1 and embedding utilities while engineering context. These LLMs are frozen.

The loop (Algorithm 1, pp5–6) starts with an empty skill history and empty context. The meta-agent inspects earlier skills, contexts, execution history and training/validation scores, then synthesizes a new skill through **agentic crossover**. The base agent warm-starts from the best previous context and learns from labelled training rollouts. The new context is evaluated on training and validation data; all trials enter the history, but only the context with the highest validation score survives as best-so-far. Tie-breaking is unspecified. Validation is therefore a selection set, not an independent test.

The reported metrics use task labels: accuracy/exact match, micro-F1 or F1. The paper does not specify an LLM answer-grading judge or a judge approval rule. LLM error analysis and context generation should not be confused with the numerical validation gate.

## Headline, with the right comparator

Offline Table 1 reports the following held-out results after five training epochs:

| Benchmark / metric | MCE | Strongest baseline in that column |
|---|---:|---:|
| FiNER accuracy (%) | 75.0 | 71.0 — ACE |
| USPTO-50k, reaction type supplied · accuracy (%) | 20.0 | 18.0 — ACE |
| Symptom2Disease accuracy (%) | 89.2 | 84.4 — ICL |
| LawBench charge prediction · micro-F1 | 0.70 | 0.69 — GEPA |
| AEGIS selected-category binary safety · F1 | 0.80 | 0.76 — GEPA |

MCE leads each offline column. The reported **89.1% average relative gain** is relative to the *base model*, not to the strongest baseline; ACE's analogous average is 70.7%. This is an average of benchmark-wise relative gains across different metrics, not pooled accuracy. Our reading is that USPTO's low base accuracy of 6.0% makes its relative improvement weigh heavily in that average despite a final accuracy of only 20.0%. Against the strongest baseline, LawBench is almost tied. Tables 1–4 give neither run/seed counts nor variance or confidence intervals; we cannot identify a seed, call them single-run results, or infer significance.

## Controls that matter

**Does skill evolution add anything beyond an autonomous coding agent?** On FiNER, offline Table 3 gives evolving skills 75.0, no skills 73.0, and a fixed skill 71.0; ACE is also 71.0. This supports an incremental benefit from evolving the learning procedure, but the mechanism ablation covers FiNER only and has no uncertainty estimate.

**Online is not skill evolution.** A fixed skill is generated from task specifications, then context updates follow sequential test instances; each instance is scored on its first inference. Full iterative skill evolution is not used online. Table 1 gives average relative gains of 74.1 for fixed-skill MCE and 71.3 without skills. Fixed skills help FiNER (68.0 vs 67.0) and USPTO (20.0 vs 18.0), but hurt Symptom2Disease (76.4 vs 76.9), LawBench (0.66 vs 0.70), and AEGIS (0.63 vs 0.68). The strongest positive contribution is USPTO; the average is not evidence of uniform skill benefit.

**What each baseline gets.** The paper states common initial context/prompt templates, datasets and sequential order, ground-truth labels when applicable, and training budgets no smaller than MCE's. Zero-shot uses the task prompt without learned context. ICL receives all training demonstrations that fit. MIPROv2 uses official DSPy `auto="heavy"`; GEPA uses the same preset and explicitly matches total rollouts. DC uses official cumulative mode. ACE uses official original parameters and up to five offline epochs, stopping for context-window overflow or a validation plateau. These are meaningful controls, but the paper does not give each baseline MCE's learned skills and file/code editing mechanism.

The FiNER model-swap control gives ACE MiniMax M2.1 as reflector and curator: final accuracy 67 versus 70 with DeepSeek V3.1, with longer context and earlier window-limit termination. This tests that specific substitution, not whether model knowledge can contribute anywhere in MCE.

**Selection and settings.** The train/validation/test roles are stated, and validation selects MCE's retained context and can stop ACE. The paper does not identify which split selected global defaults/hyperparameters, nor report per-baseline tuning-search trial budgets. Separately, numerical details not fully specified include generator-wide decoding temperature/output-token limits, actual batching/iteration counts beyond five epochs, and the numerical ACE plateau rule. Appendix E's utility-call temperature of zero is not a global generator decoding specification.

**Evolution cost.** FiNER training takes 1.9 hours for MCE versus 25.8 for ACE, a reported 13.6× speedup. MCE reaches 95% training accuracy at 450 rollouts; ACE peaks at 94% after 2169 (reported 4.8× fewer). MCE's count includes training and validation inference. These are FiNER training results, not test gains or a complete all-benchmark cost audit. Per-task dollar/token totals, optimizer-only cost breakdowns, repeated timing uncertainty and equal all-method total compute are not reported.

## Where improvement is thin, and what transfers

The LawBench offline margin, 0.70 versus GEPA's 0.69, is unaccompanied by uncertainty. USPTO remains difficult at 20.0% accuracy. The online skill-less variant wins the medical, legal and safety columns listed above.

Table 2 transfers **contexts**, not learned skills, from DeepSeek V3.1 to Llama3.3-70B, Qwen3-8B and Gemma3-4B on FiNER, Symptom2Disease and LawBench. For Gemma, MCE is only 65.0 versus ACE's 64.0 on FiNER; LawBench is 0.03 versus 0.00 (base 0.01), still near zero. The reported 172.6% average relative gain for Gemma must be read with those low denominators. USPTO transfer is excluded because of context length and invalid answers; AEGIS already uses a small generator. Cross-task skill transfer remains future work.

The authors caution (§5, pp10–11) that MCE may not offer advantages on reasoning-intensive tasks and may struggle with very long, complex rollout trajectories requiring fine-grained credit assignment. They position it as especially useful for domain-knowledge acquisition and pattern matching. These are stated limitations, not measured failures in those task regimes.

## Split story and leakage limits

Appendix A gives train/validation/test sizes of FiNER 200/100/100, USPTO 50/30/100, Symptom2Disease 200/50/212, LawBench 200/50/100, and AEGIS 400/128/140. FiNER is a restricted debt/credit subset; LawBench randomly samples the criminal charge prediction subtask, not the full suite. USPTO is reaction-type-conditioned single-step retrosynthesis: each question supplies product SMILES and the reaction type; sampling is stratified across reaction types and preserves original test membership; Symptom2Disease preserves its original test split, but the authors explicitly describe close train–test similarity. AEGIS evaluates binary safe/unsafe classification, with unsafe as the positive class. A guard model's category scores select the four worst-performing risk categories: Copyright_Trademark_Plagiarism, Political_Misinformation_Conspiracy, Unauthorized_Advice and Immoral_Unethical. Its test set contains 70 unsafe examples from those categories plus 70 randomly sampled safe examples. The split used for category selection is not identified; this is not unrestricted AEGIS or category-classification performance.

Skills and context can encode training cases or their close relatives: the appendix shows concrete examples and keyword-based routing learned from training mistakes. Scoped filesystem permissions and aggregate validation feedback constrain access, but the paper reports no empirical held-out-label, duplicate or near-duplicate audit. This is a limitation of the evidence, not a finding that leakage occurred.

## Our read

HarnessRSI **63 · ★★ · evidence level: improver**. The useful move is making the *context-learning procedure* editable and testing it against fixed/no-skill alternatives, with held-out offline evaluation and explicit GEPA rollout matching. Reports also include cross-model context transfer and a FiNER efficiency comparison. Missing evidence includes run/seed uncertainty, cross-task skill transfer, empirical leakage checks, complete tuning-search accounting and all-method total-compute parity. The FiNER ablation supports the meta-level idea; the online results show why a skill should not be assumed beneficial merely because it exists.
