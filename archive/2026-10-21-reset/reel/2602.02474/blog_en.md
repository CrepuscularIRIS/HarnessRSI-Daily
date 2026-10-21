# MemSkill: an RL controller picks memory skills and an LLM designer rewrites them — the gain is real in direction, but there is no variance and no matched-compute control

*A Reel interpretation of [arXiv 2602.02474v2](https://arxiv.org/abs/2602.02474v2) (HarnessRSI Daily score 70, ★★★). Code: [ViktorAxelsen/MemSkill](https://github.com/ViktorAxelsen/MemSkill).*

## What the system changes about itself

MemSkill replaces the fixed memory operations of an LLM agent (add / update / delete / skip) with a **skill bank**: each skill is a short text guide with a description, a purpose, when to use it, how to apply it and constraints. Two things are learned or edited:

- a **controller** (three small MLPs) that, for each span of a conversation, scores every skill in the bank and picks a Top-K set; it is trained with PPO;
- the **skill bank itself**, edited by a fixed **designer** LLM. The paper does not name the designer model.

An executor LLM reads the span plus the selected skills and writes memory updates in one call. The base LLM's weights never change. The bank starts with four primitives: INSERT, UPDATE, DELETE, SKIP.

## The signal, and the keep/reject rule

1. The controller builds a memory bank for each training conversation. The memory is then used to answer that conversation's training questions, and the score (F1 or success rate) is the reward for PPO.
2. Failed questions go into a sliding hard-case buffer with their ground truth, prediction and failure count. Cases that are both low-reward and repeatedly failed rank highest; they are clustered and representatives are shown to the designer.
3. Every 100 training steps the designer analyses the cases and proposes at most 3 edits (refine a skill or add a new one). Delete and no-op skills are not evolved. Cases are ranked by a difficulty score; as printed (d = 1 - r x c) it falls as the failure count rises, which contradicts the text, so we rely on the text only.
4. Keep/reject: the system keeps a snapshot of the best skill bank (the paper does not say what happens to the controller weights on rollback). A cycle is scored by the mean reward over the last quarter of its training steps. If the score does not beat the best so far, the bank is rolled back to the best snapshot before the next evolution step; after a fixed patience (value not given) training stops and returns the best snapshot. After each update the controller is nudged toward the new skills for 50 steps.

The selection signal is therefore the training-split reward, not a held-out score.

## Headline result, as reported

Table 1: LLaMA-3.3-70B is the model MemSkill is trained on; Qwen3-Next-80B is transfer only (skills learned with LLaMA, no retraining). The eight baselines (No-Memory, CoN, ReadAgent, MemoryBank, A-MEM, Mem0, LangMem, MemoryOS) all retrieve up to 20 memory items, like MemSkill; No-Memory has no score on LoCoMo / LongMemEval ("-"). Each cell is one number; the paper reports no seeds or standard deviations. All L-J scores come from one judge model (gpt-oss-120b) with a 0 / 0.5 / 1 rubric (Appendix B.1, D). The paper never says what its LoCoMo validation split is used for.

| LLaMA-3.3-70B | MemSkill | Strongest baseline the paper reports |
|---|---|---|
| LoCoMo F1 / L-J | 44.21 / 53.82 | 41.39 (MemoryOS) / 51.95 (LightMem, Table 3 only; A-MEM 49.71 is the best in Table 1) |
| LongMemEval F1 / L-J (transfer) | 31.12 / 60.89 | 30.78 / 56.44 (CoN) |
| ALFWorld Seen / Unseen success | 77.14 / 83.58 | 75.00 (CoN) / 81.34 (Mem0) |

The paper's claim is the best LLM-judge score on LoCoMo and LongMemEval in each base-model block and the highest ALFWorld success rates. On Qwen (transfer): LoCoMo F1 42.08 and L-J 54.14 (best baselines 39.86 and 50.96), LongMemEval L-J 60.40 (46.20 for Mem0), ALFWorld Seen 85.71 and Unseen 76.87 (CoN in Table 1: 77.14 and 70.90; Expel in Table 4: 71.64 on Unseen). ALFWorld results use in-context demonstrations; without them (Table 5) MemSkill reaches 57.71 on LLaMA against 45.99 for LightMem. The 8 baselines are not all shown in every figure or table: the paper adds LightMem, AWM and ExpeL in some places (Tables 3 to 7).

## The controls that decide whether the gain is real

- **Ablation (Table 2, LoCoMo L-J, LLaMA / Qwen, single runs).** Full MemSkill 53.82 / 54.14. Random skill choice (w/o Ctrl) 48.43 / 42.84. Designer off, bank fixed to the four primitives (w/o Des) 46.50 / 36.15. Refine-only (no new skills) 47.45 / 48.88. Each component matters in the paper's numbers. On LLaMA, all three ablated variants fall below A-MEM (49.71) and LightMem (51.95); on Qwen, refine-only (48.88) is below CoN (50.96). The paper does not say whether the controller is retrained for each variant, or which split Table 2 is measured on (the full-model row equals Table 1, so probably the test split).
- **Transfer.** LongMemEval is evaluated with the LoCoMo-trained skill bank, but the validation split of LongMemEval is used to tune dataset-specific configurations (Appendix B.1), and the test sample is about 100 questions. HotpotQA (Figure 3, LLaMA L-J, skills from LoCoMo, 50 / 100 / 200 concatenated documents): with K = 7 skills MemSkill is above MemoryOS and A-MEM at all three lengths, by a wider margin at 200 documents. Only MemoryOS and A-MEM are shown; the paper calls them "the most competitive methods on conversational benchmarks in Table 1", but on LLaMA the conversational average of CoN (49.08) is above MemoryOS (44.24) and A-MEM (43.88), and CoN and LightMem are not shown. The bar values are in the figure only, so they are listed in SOURCE.md and on the poster.
- **Cost (Table 3, LoCoMo, runtime only).** At span size 512 (the default; the same 53.82 as Table 1) MemSkill uses 249K input tokens, 18K output tokens and 215 LLM calls; MemoryOS uses 1013K / 165K / 1288 calls (L-J 48.64), A-MEM 2850K / 362K / 1548 (49.71), LightMem 789K / 209K / 685 (51.95). The other span sizes score 53.14, 51.61, 48.11 and 50.46 (128, 256, 1024, 2048): the headline uses the best of five sizes swept on the same LoCoMo run, and the paper does not say how 512 was chosen. The paper states that learning and evolving the skill bank is a pre-deployment cost that is amortized and does not report it (only that training used A6000 GPUs).
- **Not controlled.** The paper does not say what training, tuning or evolution the baselines receive; no baseline tuning budget, matched-compute row or baseline variance is reported. The designer is compared with "no designer" and "refine-only", not with another memory-skill evolver (ExpeL and AWM appear as extra baselines in Tables 4 to 6, on ALFWorld / AppWorld only).

## Where the gain is absent or small

- **LongMemEval F1 on Qwen: MemSkill is not best.** 25.29 against 29.19 for CoN and 27.36 for Mem0 (its L-J is 60.40, well ahead). On LLaMA the F1 margin over CoN is 31.12 vs 30.78.
- **Thin margins elsewhere.** LoCoMo L-J on LLaMA is 53.82 vs 51.95 for LightMem (1.87‡; Table 3). ALFWorld Unseen on LLaMA is 83.58 vs 81.34 (Mem0); the paper gives no test sizes, but if the official 140 Seen / 134 Unseen tasks were used (our inference), the Seen (77.14 vs 75.00) and Unseen margins are 3 tasks each and Qwen Unseen (76.87 vs 71.64) is 7 tasks. On AppWorld with in-context demonstrations (LLaMA, average pass rate) MemSkill is 47.32, AWM 47.11, Mem0 47.03 and No-Memory 46.41; the paper itself notes the setting is "partially saturated". Without demonstrations it is 26.71 vs 25.42 for AWM (1.29‡; Mem0 24.32). On the 8B model (Table 7) the LoCoMo L-J is 27.23 vs 26.85 for LightMem.
- **HotpotQA depends on K.** With K = 3 (the training value) MemSkill is below both MemoryOS and A-MEM at 50 and at 200 documents (Figure 3 bar labels, listed in SOURCE.md); K = 5 at 50 documents is also below both (above both at 100 and 200). At 100 documents K = 3 is above K = 5, so "increasing K generally improves performance" is not monotone, and "consistently outperforms" holds for K = 7 only. The text does not say how K was chosen.
- **Wording of the ALFWorld margins.** Appendix A.1 says MemSkill beats "the strongest baseline LightMem by 5.53 points" (80.36 vs 74.83), and on Qwen "Expel by 7.61 points" (81.29 vs 73.68). Read as "strongest among the added baselines" these are right; in Table 1, Mem0 has an average of 77.82 on LLaMA and CoN 74.02 on Qwen, so the margins against the strongest baseline overall are 2.54‡ and 7.27‡.
- **Small test sets, no intervals.** LoCoMo is split by conversation (10 samples, 6/2/2), so the test set is about two conversations (roughly 400 questions at about 200 per conversation, before adversarial questions were removed; our inference). No confidence intervals or repeated runs are given.
- **Limitations section.** The paper's limitations paragraph covers privacy and deployment only.

## Our read

HarnessRSI score **70**, band ★★★, evidence level **improver**: the improvement mechanism itself (the designer; the controller) is ablated and compared, and skills trained on LoCoMo are tested on another benchmark, another dataset family and another base model. The paper reports held-out transfer, cross-task transfer, ablations and a runtime cost comparison. It does not report variance across seeds or runs, a matched-compute or matched-tuning comparison with baselines, the cost of training and evolving the skill bank, or a leakage test. The headline therefore rests on single-run numbers on small test sets, with a consistent direction across models and benchmarks and a few columns where it is absent.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
