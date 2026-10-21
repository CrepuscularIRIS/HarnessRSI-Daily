# One recipe, many harnesses: portable discipline, but not a portable native ceiling

*A Reel interpretation of **One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models**, by Siqi Yang, Qianlan Yang, Yu-Xiong Wang, Saurabh Pujar and Martin Hirzel. Read: [arXiv 2608.10178v1](https://arxiv.org/abs/2608.10178v1). HarnessRSI Daily score **64**, band ★★. No verified code link supplied for this Reel.*

## What the system changes about itself

TRIAGE keeps the model weights fixed and edits the **harness**: prompt templates, workflow hooks, lessons memory and shell tools. It holds the evolution recipe fixed across eight programming languages and three models on Multi-SWE-Bench. **The recipe is shared; the concrete harness is re-derived separately for each language/model cell.** This is not one finished harness that wins everywhere.

Each cell starts from the same minimal ReAct seed: a short prompt, one shell tool, empty hooks and memory. The task policy, rollout analyzer and evolve agent use the same underlying model in the main grid. The analyzer reads failed trajectories, submitted patches, test outputs, grader-stage evidence and budget traces. Typed diagnoses advise which slot to edit; the evolve agent writes a contract naming the intended repair and the instances expected to improve or regress. Memory is capped at 12 entries of 400 characters, with instance-specific tokens rejected. The artifacts mainly encode behavioral discipline, not newly invented tools.

## The loop, and the keep/reject rule

- Smoke-test edits before use; malformed edits leave the old contents in place. Edit at most two components per round.
- Re-run the **evolution split** to evaluate the whole checkpoint and the contract's predictions. Selection uses the solve score minus **2.0** times the fraction of previously solved instances now lost.
- Rollback is not immediate: Appendix A.4 tolerates a dip of **0.12**, reverts after two non-improving rounds, or after a catastrophic drop of **0.25**.
- After three rounds, ship the best checkpoint selected on the evolution split, falling back to the seed if nothing matches it. **This seed floor applies to selection data, not to the held-out test.** Verification hooks encourage testing; they do not prohibit submission.

For the worked C++/Haiku example, the evolution scores are **10.0 → 62.5 → 72.5 → 72.5**; the second-round checkpoint is shipped. A contract can be judged confirmed without every prediction being met: Appendix A.7 records one named fix confirmed and four missed. The paper also leaves a routing detail unresolved: A.2 says `wrong_fix` is deliberately not routed, while Table 2 lists it under verification/boundary routing. We do not infer which behavior ran.

## Headline result, as reported

The **stated protocol** randomly samples **20** evolution instances and a disjoint held-out split of **50** per language. However, the rollout totals in Appendix I.1 and Table 9 do not reconcile with the stated full grid and rollout repetitions; actual per-cell evaluation coverage cannot be verified from the PDF. The metric, **mean_solve@3**, averages the solve rate over three independent rollouts per instance; it is not the probability that any of three attempts succeeds. There is **one evolution run per cell**, not three evolution seeds. The headline is the evolution-selected checkpoint's test score.

**Table 3, held-out mean_solve (%). Each cell below is seed / unmodified mini-SWE-agent / TRIAGE.**

| Language | Claude Haiku 4.5 | GPT-5-mini | DeepSeek-V4-Flash |
|---|---|---|---|
| C++ | 12.9 / 61.9 / **87.1** | 22.9 / 27.6 / **27.1** | 34.3 / 60.0 / **65.7** |
| Java | 2.9 / 51.4 / **82.9** | 22.9 / 16.2 / **28.6** | 24.3 / 35.7 / **54.3** |
| C | 30.0 / 75.0 / **81.7** | 28.3 / 46.7 / **36.7** | 38.3 / 65.0 / **65.0** |
| JavaScript | 31.5 / 68.5 / **75.9** | 33.3 / 37.0 / **31.5** | 38.9 / 46.3 / **59.3** |
| TypeScript | 34.6 / 65.4 / **86.5** | 46.2 / 36.5 / **44.2** | 44.2 / 65.4 / **63.5** |
| Rust | 11.1 / 31.5 / **72.2** | 24.1 / 31.5 / **20.4** | 18.5 / 44.4 / **35.2** |
| Go | 13.0 / 25.9 / **37.0** | 22.2 / 27.8 / **22.2** | 18.5 / 27.8 / **33.3** |
| Python | 75.0 / 72.6 / **73.2** | 67.9 / 65.5 / **67.9** | 73.2 / 71.4 / **66.1** |

The large improvements concentrate in **Haiku outside Python**, especially Java and C++, and in non-Python DeepSeek cells. They do not extend uniformly to GPT-5-mini. Beating the bare seed also does not mean beating the manual scaffold: DeepSeek loses to mini-SWE-agent on TypeScript, Rust and Python, and ties it on C.

## The controls that decide whether the gain is real

**Uncertainty is not evolution-run replication.** Table 4 gives resample uncertainty for seed and TRIAGE, plus paired changes. Haiku Java is **2.9 ± 2.0 → 82.9 ± 6.1**, with paired gain **80.0 ± 6.9**. DeepSeek Rust has paired gain **16.7 ± 9.6**, with **z = 1.73**, clearing the paper's single-star threshold of **1.64**, not its **1.96** threshold. No GPT-5-mini cell reaches significance (**|z| < 1.3**). Table 4 supplies no mini-SWE-agent uncertainty. These are not confidence intervals over repeated harness searches.

**What each baseline receives.** The minimal seed has task text, submission protocol and a bash tool, but deliberately no build/test/verification/diff-scope guidance. Mini-SWE-agent runs unmodified at its released configuration. Both have the same containers, grader and per-rollout limits as TRIAGE: **80 steps and $1.5**. Neither static baseline receives TRIAGE's evolution, edit contracts or checkpoint gate. The paper reports no baseline tuning budget beyond that configuration description. Checkpoints are selected on the evolution split; it does not state a split used to tune the fixed defaults or hyperparameters. Appendix H explicitly says there is no total-compute-matched baseline spending the evolution budget on extra inference rollouts, no stronger static scaffold, and no head-to-head comparison with other harness optimizers.

**Mechanism evidence is mostly diagnostic.** Of **256** recovered held-out instances, **88%** had a detected seed-side defect: **81%** touched a test path, a further **7%** broke the test build without doing so (Table 6). These post-hoc associations cover only measured defects, not the full space of recoverable failures. Much of the recovery concerns a benchmark-specific convention: editing a test file can collide with the grader's hidden gold test patch. The paper acknowledges that absolute gains partly reflect learning this protocol. The pooled gain/defect correlation is **0.81**, but only **0.12** within GPT-5-mini; the pooled relationship is driven by the models that gain.

**Ablations are narrow.** With DeepSeek as the Go task policy, meta-drivers GPT-OSS-20B, DeepSeek and Claude Sonnet 4.6 score **34.2, 33.3 and 35.6**, versus seed **18.5** (Table 7). This single-cell comparison reports averages over three rollouts, with no variance/CI in the table. It supports driver sensitivity being modest here, not routing or contracts being independently causal. Those components, the gate and two-axis editing are not separately ablated. In the separate duplicate-code task-family probe, a preinstalled tool gives **9.3** versus **22.2** without it, from seed **11.1** (Table 8; no variance/CI). That selected-family result is not the main-grid C++/Haiku result of **87.1**.

**Costs include the data-generating loop.** Appendix I reports metered meta-model spend **$256** separately from **$3,667** of rollout spend. Table 9 lists aggregate categories, not matched per-harness bills: main grid **$1,415**, mini-SWE-agent **$357**, transfer **$1,088**, universal distillation **$615**. Matching rollout ceilings is not matching realized spend or total optimization budgets. The source-harness evolution and all-language distillation work must not be treated as free transfer. **Evaluation accounting remains unresolved:** Appendix I.1 attributes **2,820** held-out rollouts to scoring all three arms at k=3 across the grid; Table 9 repeats that count and separately lists **1,606** mini-SWE-agent rollouts. Neither count reconciles with the stated complete-grid protocol. We retain the reported scores, but cannot verify executed per-cell coverage from the PDF and do not infer a cause.

## What transfers, and what must be learned again

There are distinct experiments, not one generic transfer claim:

1. **Recipe reuse:** independently re-evolve prompt/hooks/memory/tools for every language/model cell, using its own evolution tasks and diagnoses.
2. **Full-harness transplant:** carry a source-language harness **unchanged**, with no target adaptation, onto another language's held-out instances. The task model is always DeepSeek-V4-Flash. The native comparator was separately evolved for that target.
3. **Universal distillation:** the meta-model merges evolved memories from **all languages** into ten generic memory-only rules, stripping concrete build commands, test paths and file-layout conventions. Deploy that same artifact unchanged, **evaluated with DeepSeek-V4-Flash only** (§4.5). It is not leave-one-language-out: the pool includes target-language evolution experience.

Retention is **ρ = (transferred score − seed score) / (native score − seed score)**; it is a fraction of native *gain*, not a solve rate. Section 4.6 reports positive transfer in **18/20** pairs, with **14/20** below native and mean retention **0.63**, without per-pair variance/CI. The source/target pattern matters: C++→TypeScript **1.50**, Java→TypeScript **1.40**, Go→TypeScript **1.30** exceed native point estimates; JavaScript→C++ is **1.32**, but JavaScript→TypeScript is **−2.30**, below even the seed. Go→JavaScript is also negative (**−0.09‡**, Figure 7 label). Native is therefore a reference, not an absolute ceiling.

For the universal memory, **with DeepSeek-V4-Flash only**, Section 4.5 reports JavaScript **1.13** and Go **1.08**, described as statistically indistinguishable from native, against Java **0.68**, C++ **0.65** and TypeScript **0.48**. The paper does not supply the corresponding numerical intervals there. Native evolution is better on those latter targets; universal rules recover only part of their native gains. Concept overlap is **0.55** for Haiku and **0.57** for DeepSeek, versus ecosystem-token overlap **0.12** and **0.14**. The content analysis includes only their positive-gain, non-Python cells; automated LLM tags and lexical markers limit interpretation. The broad prose claim that every harness is **20–40%** ecosystem-specific has an unresolved exception: Table 5 gives Haiku JavaScript **18%**.

**Transfer leakage and budgets.** Appendix B.1 says the held-out instances never propose, score or select edits, and all variants reuse the same target test set. The memory token filter is a further guard. However, the paper does not report a cross-language source-evolution/target-test instance or repository-overlap audit, so those statements do not establish cross-language separation; we are not claiming leakage occurred. Native searches share the stated rounds and rollout ceilings, but per-harness realized cost matching and a matched-total-budget transplant/distillation comparison are not reported.

## Where the gain is absent or small

- **GPT-5-mini:** even its largest positive seed comparison, C **28.3 → 36.7**, is not significant under Table 4's thresholds (**8.3 ± 6.8**, **z = 1.22**); mini-SWE-agent reaches **46.7** there. Other tasks have zero or negative seed changes. The paper identifies this null region post hoc.
- **Python:** Haiku **75.0 → 73.2**, GPT-5-mini **67.9 → 67.9**, DeepSeek **73.2 → 66.1**. Do not summarize all as exact ties: Table 4 gives DeepSeek's paired **−7.1 ± 4.2**, **z = −1.69**, a single-star negative under the paper's threshold, although the main text calls Python a null region.
- **Novel operational knowledge:** the planted-fact probe fails to learn its specific remedy: control **78.3 → 76.1**, error-surfaced condition **76.1 → 71.7**, both described as within noise. This supports a narrower reading—recalling and installing discipline—not demonstrated discovery of new environment-specific facts.
- **Scope:** repository repair, small random within-language splits, three evolution rounds, one search run per cell. Longer-horizon behavior and evolution-seed stability remain untested.

## Our read

HarnessRSI score **64**, band ★★, evidence level **retained**. The retained harnesses are tested on disjoint instances and their portability is measured, but diagnostic routing, contracts and selection are not independently isolated. **Reports:** held-out evaluation, cross-language reuse/distillation, rollout/resample uncertainty, a driver ablation, negative probes and optimizer/rollout cost accounting. **Does not report:** independent evolution-seed variance, matched total-compute baselines, per-pair transfer uncertainty, separate routing/contract/gate ablations or a cross-language leakage audit.

The existing b12 judgment leaves optimizer cost unclear; the full appendix does report it. Its variance “no” should be read as no repeated evolution runs, not no uncertainty evidence at all. We leave the score and judgment files unchanged and document the qualification in SOURCE.md.

*‡ marks a value read from a figure label, not computed here; see SOURCE.md. All poster visuals are our own; no paper figures are reproduced.*
