# SOURCE — The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators

Read from: arXiv 2606.26294v3
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers. The paper prints no public code link (it mentions an anonymized supplementary zip), so the poster carries only the paper QR code.

Authors as printed in the PDF title block: Alex Iacob, Andrej Jovanović, William F. Shen (equal contribution), Daniel Burkhardt, Meghdad Kurmanji, Nurbek Tastan, Lorenzo Sani, Niccolò Alberto Elia Venanzi, Jiayi Nie, Ambroise Odonnat, Zeyu Cao, Bill Marino, Xinchi Qiu, Rika Antonova, Nicholas D. Lane. The poster header lists the first three and "et al. (15 authors)".

## Where the numbers come from (PDF page numbers)
- Mechanism: Sec. 3 (pp3-4), Sec. 4 (pp4-5), Algorithm 1 and App. B (pp18-19), App. F.2.1 and F.6.3 (pp35, 38).
- DeepSWE headline: Table 9 (p26), Table 7 (p23, GPT-6 Astra mean of four official attempts, 28 held-out tasks), Table 6 (p22, split 28/57/28 and search tokens to winner 587M vs 429M), Table 14 (p28), text on p6.
- DeepSWE reviewer audit: App. E.4 and Table 15 (pp30-31).
- Polyglot: Table 8 (p26, 71.7 vs 69.9), split sizes in App. C.6 / Table 4 (pp21-22, 166 test tasks), 1.35×–1.72× from the text and Fig. 3 caption (p6).
- Reward design: Table 1 (p6), App. C.8 (p24).
- Paper writing: Table 2 (p7), tokens in the same table; reviewer accuracy/acceptance (80% vs 88%) in Table 8 (p26); N = 100 papers per cell in App. C.7 (pp23-24).
- Proof writing: Table 3 (p7), per-grader scores Table 10 (p26), "without the RQGM grader" 4.03 / 4.08 / 3.60 in the Table 3 caption and App. D.1 (p26); Pass@7 values Table 3.
- Mechanism ablations: Table 11 (p27, Nemotron 3 Super, paper domain), Tables 12-13 (p27, Nemotron 3 Ultra, proof domain, 1,024-evaluation budget, App. C.4 p21).
- Number of headline runs: App. C.4 (p21), "There are eight headline runs: an RQGM and an HGM-H run in each of the coding, paper, and proof domains".
- Limitations: App. G (p39).
- Searched the full text (including the appendix) for contamination, leakage, repeated runs and seeds: only the reward-design experiment has several runs per arm (five searches per arm); no contamination or leakage test of the base models is described, only disjoint splits and "the held-out test split is never seen during search" (p5).

## ‡ numbers (computed by us)
- 1.37‡× = 587M / 429M, search tokens to the winning coder, RQGM vs HGM-H on DeepSWE (Table 6: 587.2M / 428.6M in Table 14).
- 5.2‡× = 221.8M / 42.5M, paper-writing specialist vs HGM-H writer (Table 2).
- 4.1‡× = 88.0M / 21.5M, proof specialist vs HGM-H prover (Table 3).
- 1.14‡× = 2876.8M / 2532.7M, full-run search tokens RQGM vs HGM-H on DeepSWE (Table 14).
- 2104.1M‡ = 2532.7M − 428.6M, tokens the HGM-H DeepSWE run spent after its winner was found (Table 14), during which the paper says it never found a better coder (p6).
- 1.76‡× = 37.9M / 21.5M, proof generalist vs HGM-H prover tokens (Table 3); the paper describes this comparison as "at matched search tokens".
- 7.1‡ points = 82.1 − 75.0 (DeepSWE, low effort).
- 0.059‡ = 0.365 − 0.306 (reward design, Table 1).
- Task-count readings of percentages (marked ‡ where used): DeepSWE has 28 held-out tasks, so 82.1% = 23/28, 75.0% = 21/28 (two tasks‡), 85.7% = 24/28 vs 82.1% = 23/28 and 83.0% (Astra mean of four attempts) = about one task; Polyglot has 166 held-out tasks, so 71.7% = 119/166 and 69.9% = 116/166 (three tasks‡); at high effort 85.7% vs 82.1% = 24/28 vs 23/28 (one task‡). These assume the percentages are exact task fractions and that each evolved coder ran once per task; the paper gives no counts, and if the evolved coders were run four times per task like the Astra reference, the same percentages would be counts out of 112 attempts.

## Notes
- The poster chart for DeepSWE/Polyglot plots Table 9 and Table 8 values. The poster table "Search tokens to winner" uses Table 6 (DeepSWE), Table 2 (paper writer) and Table 3 (proof). For the paper-writing and proof rows the paper reports tokens at which each best-belief agent was found; the 44.6M / 37.9M generalist rows are the ones the paper calls matched-token comparisons ("at matched search tokens" for the writer; the proof generalist "performs similarly to the HGM-H at matched search tokens").
- The RQGM proof generalist has exactly the same Table 3 scores as the HGM-H prover (3.73, 51.7%, 45.0%); we report this as an observation.
- Abstract/intro wording "matches HGM-H at equal search cost" (Fig. 1 caption) vs Table 6 winner tokens (587M vs 429M): we report both neutrally, using the table values.
- No coding-domain ablation (reviewer off, evaluator replacement off) was found in the paper; Appendix D.2 covers the paper and proof domains only.
- The DeepSWE "number of attempts" for the evolved coders is not stated (the official verifier grades the committed patch); only the GPT-6 Astra reference is described as a mean of four attempts.
- Per-grader Table 10: the specialist's Pass@7 trails the static IMO25 prover under ProofAutoGrader (40.0 vs 55.0) and the HGM-H grader (45.0 vs 55.0), and leads only under the RQGM grader (60.0 vs 55.0); not all of this is on the poster.
- Fig. 6 (grader at "3× lower search cost") gives its accuracy values only in the figure; we quote the text claim and no figure values.

- Revisions after independent fact-check: the replacement rule is stated with the pool term (App. F.2.1 and F.6.3: p+/2 + p-/4 + pool rejection/4), noting that the Fig. 9 caption says only anchor evidence enters the gate; the writer and prover are selected per epoch by the system's own frozen evaluators and scored post hoc by external panels (Sec. 4, "Costs and reporting", p5); "eight headline runs" (App. C.4) is quoted verbatim and noted as six arms for three domains (eight if Polyglot and DeepSWE count as two coding domains); the 32% (held-out human papers, Table 8) vs 29–31% (RQGM writer papers, Table 2) acceptance comparison is stated in that order; the DeepSWE meta-agent ran at high effort and the task agents at low effort in both arms (Sec. 4, p5); the held-out APReS reviewer accuracies (Table 8: HGM-H 88%, RQGM specialist 84%, RQGM generalist 84%, adversarial 80%) are all stated.
- DeepSWE attribution: the winner (587M tokens) was generated after three of 11 reviewer replacements (App. E.4), when the seated reviewer was one of those that Table 15 shows accept 81.8%–100.0% of failing patches; the HGM-H chain also adopted "coder may add new regression tests" (Table 19, third node; App. E.5 text). The paper's abstract credits the code-review signal; there is no coding-domain ablation, so we say the attribution is not shown.
- Anchor rises on DeepSWE (0.03 to 0.48) are on the anchor that replacement selects on (with the pool term), so they are expected by construction (Prop. 7 and Remark 1, p37-38); Remark 1 itself is stated for a slot without a pool.

## Judgment notes
Our judgment (research/judgments, HarnessRSI score 70, evidence level improver) is broadly consistent with the full paper. Two points are worth a reader's attention, no judgment file was edited:
- `budget_matched: yes` rests on the paper's "matched search tokens" statement. The full paper shows this holds only for some rows: DeepSWE winner tokens are 587M (RQGM) vs 429M (HGM-H), the paper-writing specialist uses 221.8M vs 42.5M, and the proof specialist 88.0M vs 21.5M; the generalists (44.6M, 37.9M) are closer to matched. The HGM-H DeepSWE run was longer: it continued to 2532.7M tokens (RQGM full run 2876.8M) without a better coder, but no held-out score at exactly matched tokens is reported. Treat as partial.
- `retained_ablation: unclear` — Appendix D.2 (Tables 11-13) does report mechanism ablations (replacement, adversarial pool, erasure) for the paper and proof domains, with Nemotron models and a smaller budget than the headline runs, mostly with overlapping intervals; none for coding. `variance: unclear` is consistent: headline arms are single runs.
