# MC-EvoBench: in Minecraft, stored experience showed no stable transfer for the one method tested

*A Reel interpretation of [arXiv 2610.13829v1](https://arxiv.org/abs/2610.13829v1) (HarnessRSI Daily score 74, ★★★). Code: [xzw-ustc/mc-bench-open-source](https://github.com/xzw-ustc/mc-bench-open-source).*

This paper is a benchmark and an audit, not a new self-improving agent. It asks one question: when an embodied agent does better after gaining experience, is that a reusable capability, or a changed world state, extra source interaction, or luck? For the one method it tests, the paper reports "no stable transfer", with wide five-seed intervals.

## What changes, and what counts as a kept gain

The agent under test (the "reference method") is the JARVIS-1 online extension: a text planner drives a released low-level controller, and after each stage a reflection step writes one sentence of advice into a JSON memory. Each record holds the instruction, the proposed plan, the prompts actually dispatched, the stage status, a visible-state summary and the advice. Retrieval uses token-set Jaccard similarity (plus 0.15 for a successful record), up to four records condition the next plan, and the latest 256 records are kept. The paper describes no filter on which records are written. The kept artifact is this memory; weights do not change.

The benchmark supplies the keep rule for *claims*. A gain counts as experience-driven only if it appears after the target world and inventory are reset, only the declared artifact crosses the source-target boundary, and matched controls rule out alternatives:

- **No-prior**: the base agent with empty memory.
- **Related**: memory from a source task with the same dependency pattern but a different end object or tool.
- **Unrelated**: memory from collection tasks outside the target's production chain.
- **Shuffled**: memory from the related tasks in reversed order.

Source exposure is matched in environment steps within each family (900, 2,250 and 3,600). Verification uses stage-level predicates read from the game state, giving three metrics: TSR (fraction of planned stages passed), WGP (weighted graph progress; Figure 2 labels it "World Goal Progress") and VMP (verified milestone progress). The catalog has 80 tasks, 111 states, 369 typed edges and 19 chains (12 primary evaluation chains and 7 calibration or probe chains).

## Headline results, as reported

**Direct capability (Table 2, 12 primary chains, three seeds per configuration; no SDs given).** Controller-based agents clearly beat planner-backed variants. Average TSR/WGP/VMP in percent: STEVE-1 8.4/6.4/25.5, JARVIS-1 controller-only 7.5/5.5/25.0, Optimus-1 controller-only 8.1/6.1/25.4. The no-op baseline and the GPT-planned JARVIS-1 sit at the same floor (1.5/0.6/0.0). Among the planner-backed rows of Table 2 (planners are shown as logos; the text names DeepSeek for the highest TSR) the best average TSR is 2.8 for JARVIS-1 and 4.9 for Optimus-1. Caveats on this table: it has 17 rows while the text and appendix speak of nine direct configurations with a single planner (gpt-5.6-sol), and Table F9 lists 513 planned units of which 505 gave valid reports, so some cells average two seeds.

**Paired transfer (Table 3, five agent seeds, one fixed world seed).** Target TSR for no-prior / related / unrelated / shuffled:

| Probe | No-prior | Related | Unrelated | Shuffled |
|---|---|---|---|---|
| Wood species (2 stages) | 0.400 | 0.400 | 0.200 | 0.500 |
| Wooden tool (5 stages) | 0.320 | 0.200 | 0.160 | 0.240 |
| Stone tool (8 stages) | 0.150 | 0.050 | 0.025 | 0.075 |

On TSR, related experience does not exceed no-prior on any probe (equal on wood species; lower on the two tool probes). On wood species the related WGP is 0.400 against 0.360 for no-prior (+0.040, the only positive related-minus-no-prior change in Table 4); VMP is equal. On the two tool probes the related point estimates are lower than no-prior on all three metrics (stone tool: TSR 0.050, WGP 0.021, VMP 0.200 versus 0.150, 0.082, 0.533), but the paper gives no interval for these differences; an interval we recomputed from the Table D3 per-seed TSR values includes zero for both probes (wooden tool [-0.40‡, 0.16‡], stone tool [-0.23‡, 0.03‡]), so "lower" means a point estimate within noise. Related TSR is above the unrelated control on all three probes (0.400 vs 0.200, 0.200 vs 0.160, 0.050 vs 0.025) and below the shuffled control on all three.

## The controls that decide whether a gain is real

- **Control-adjusted contrast (Table 4).** GATG = related minus the mean of unrelated and shuffled. On TSR it is 0.050 for wood species, 0.000 for wooden tool and 0.000 for stone tool; the largest value anywhere is 0.060 (wood-species WGP). Every 95% Student-t interval in Table 4 (these are intervals for GATG) includes zero; the wood-species TSR interval is [-0.723, 0.823].
- **One seed carries the only positive contrast.** The wood-species GATG of +0.050 is driven by a single seed (+1.0) and falls to -0.19 without it (Fig. 3, Table D3). Per-seed related-minus-no-prior TSR on wood species runs from -1.000 to 1.000.
- **Shuffled control.** On wood species the shuffled source scores at least as high as the related one on TSR and WGP (0.500 versus 0.400 TSR).
- **Matched exposure is not matched computation (Table 5).** Environment steps are equal, but episodes, planner calls and outcomes differ. The paper says related is the only condition with nonzero source TSR (0.100, 0.080, 0.150) and that it accounts for 34 of the 41 passed records; the "passed" counts look stage-level (for example, termination counts exceed episode counts in the related rows) and two unrelated rows list passed=6 and passed=1 with Source TSR 0.000, so read these counts with care. On the two longer probes related sources use more planner calls (wooden tool 14.80 versus 12.00 and 10.00; stone tool 24.80 ± 4.60 versus 16.40 and 16.00); on wood species they do not (4.40 versus 5.80 and 4.00). The paper says this extra experience yielded no target gain. Table 5 reports source-side cost only; target-side planner calls and tokens are said to be recorded but are not tabulated.
- **Failure-stage audit of the direct matrix (Fig. 3a, Table F10; not the paired probes).** Of 42 reports per configuration that include wood collection, the three controller variants bring 20-23 to plank crafting, at most 14 to sticks and at most 2 to the crafting table, and none of those that reached the crafting-table stage passed it (0/2, 0/1, 0/1). The Optimus-3 action path never passes the initial wood stage. Full chains pass in only 3/57, 2/57 and 1/57 reports; note that the 57 reports per configuration cover all 19 chains, including the 7 calibration or probe chains, while Table 2 covers the 12 primary chains.

## Where the gain is absent, or cannot be judged

- **No stable transfer gain.** On TSR, related is not above no-prior on any probe; the one positive related-minus-no-prior change is wood-species WGP (+0.040). Related is also not above the shuffled control on any probe. The wood-species GATG rests on one seed.
- **The paired probes sit near a low execution floor.** The transfer agent is itself planner-backed, and the paper's own direct matrix puts planner-backed variants at 1.5 to 4.9 average TSR. Stone-tool TSR is 0.150 even for no-prior (per-seed values in Table D3 are 0.125 in four seeds and 0.250 in one, i.e. one stage of eight). The authors say the probes "should be read against its low execution floor".
- **Small experiment.** One reference method, three probe pairs, five seeds, one public world seed (31), one environment profile per family. The paper states the conclusions are limited to the tested agents, probes, seeds and budgets, and that gains under a different agent, artifact, task distribution or source budget are not ruled out. Retention and composition are not tested.
- **Internal inconsistencies.** Table 5 lists passed=6 for the unrelated wood-species source and passed=1 for the unrelated stone-tool source while both have Source TSR 0.000; the paper does not explain this. Table 2 shows five planner variants per family, while the appendix describes nine configurations with a single planner.

## Our read

HarnessRSI score **74**, band ★★★, evidence level **task**: no retained artifact helped on data not used to create it, so the paper does not reach the "retained" level, and the score rates the rigor of the audit rather than a measured improvement. The paper reports a reset-world evaluation (artifact-only transfer, but the same public world seed 31, spawn and resource layout as the source), related, unrelated, shuffled and no-prior controls, five seeds with 95% intervals, and source-side cost. It does not report matched computation (steps are matched; planner calls differ), a comparison across several improvement methods, or a leakage test beyond the protocol design. Only one transfer method was tested, so the null result applies to that method under these budgets.

*Numbers marked ‡ were computed by us; see SOURCE.md.*
