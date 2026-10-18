# HarnessRSI Daily

A research radar for **harness-level recursive self-improvement (RSI)**: systems that improve their own
*non-weight* components — prompts, skills, tools, workflows, memory, agent code, evaluators — from their own
execution feedback, and keep those changes for later tasks.

Lists of such papers already exist (e.g. [awesome-rsi](https://github.com/lobehub/awesome-rsi)). This repo goes
the other way: **depth over breadth**. It asks of each paper *what exactly improves, how the change is accepted,
and whether the evidence shows a real, retained improvement* — and it maps the field into recurring research
patterns, learned from the corpus itself.

> 中文简介：专门追踪「非权重层面的递归自我改进」（Harness RSI）。不做又一个论文列表，而是对每篇论文判定
> 它改了什么、怎么决定保留、证据是否真的支持"留存下来的提升"；并从语料中逆向归纳出 Harness 版的研究模式卡。

## What is here

| Path | What |
|---|---|
| [`cards/`](cards/) | Per-paper **diagnosis cards** (GEPA, RRSI, Harness² so far): mechanism, author-reported evidence, our diagnosis (held-out, budget, leakage, strongest rebuttal), code check at a pinned SHA |
| [`patterns/`](patterns/) | **Harness pattern cards** — start at [overview](patterns/overview.md): 13 [main patterns](patterns/main/) and 36 [sub-patterns](patterns/sub/) induced from the corpus, with accept-vs-reject contrast from ICLR, plus [anti-patterns](patterns/anti-patterns.md) |
| [`docs/EVIDENCE.md`](docs/EVIDENCE.md) | Scope (tier A/B), and the task / retained / improver evidence levels |
| [`docs/MAINTAINING.md`](docs/MAINTAINING.md) | Daily maintenance rules for the maintainer agent and humans |
| [`research/`](research/) | The reproducible pipeline and its data (see below) |
| `main.py`, `src/` | Daily arXiv fetch + LLM relevance scoring, inherited from [daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) ([usage](docs/digest-pipeline.md)); topics set in `config.example.json`, keywords in `keywords.json` |

## How the pattern cards were built

The method mirrors how [ResearchStudio-Idea](https://github.com/microsoft/ResearchStudio) derived its ideation patterns
(signature extraction → pattern discovery → operational cards), adapted to harness RSI:

1. **Corpus.** Every arXiv paper cited by 7 public RSI / self-evolving-agent lists, plus anchor works: **1,198 papers**
   (`research/corpus.jsonl`). Lists contribute arXiv ids only.
2. **Screening** from abstracts into tier A (a harness-level self-improvement loop), B (a component usable inside one),
   C (out of scope, incl. weight-level self-improvement): **A 400 / B 185**.
3. **Contrast set.** Curated lists hold few rejected papers, so all ICLR 2025–2026 submissions matching harness-RSI
   terms were pulled from OpenReview — **including 406 rejected and 222 withdrawn** — and screened the same way (193 A/B).
4. **Signatures.** For each A/B paper: the problem, the assumption it drops, an operational signature, the
   load-bearing mechanism, what is evolved, how candidates are proposed, selected and retained.
5. **Pattern induction** over 585 signatures, with outcome labels withheld: **13 main patterns / 36 sub-patterns**.
   An independent re-assignment of 120 papers agreed on the main pattern 86% of the time (Cohen's κ = 0.84).
6. **Quote-grounded evidence** for 200 outcome-labeled papers: every non-"unclear" judgment carries a verbatim
   quote, mechanically checked against the paper text (`research/check_evidence.py`).
7. **Contrast.** Accept rates per pattern within ICLR 2025–2026 (base rate 35%), `research/patterns/contrast.md`.
8. **Cards** distilled from the above. Cards never name a paper; `research/check_patterns.py` verifies every count and Δ against `contrast.json` and greps for member titles.

The strongest finding: **single-document critique-and-rewrite (H10)** is accepted at ICLR far below base (17% vs 34%, n=30) — the only signal whose CI excludes the base rate in every view. For most other patterns, *membership* does not predict acceptance; *execution* does (see each card's "accepted vs rejected gap").

Pipeline state and decisions: [`research/PIPELINE.md`](research/PIPELINE.md).

## Caveats

- Screening, signatures and assignments are LLM-produced. Inter-rater agreement measures how clear the taxonomy is
  *given* the signatures, not whether the signatures are right.
- Acceptance is not quality, and n is small: read the confidence intervals in `contrast.md` before believing a Δ.
- Rejected papers come mostly from OpenReview and were read from abstracts only; evidence and limitations are therefore
  not comparable across outcomes, and cards compare accepted vs rejected work on mechanism only.
- ICLR reviews could not be fetched in this run (OpenReview rate limits); each main card's "Reviewer expectations"
  panel is derived from the quote-grounded evidence audit and is marked pending.
- Paper full texts were used locally and are not redistributed here. ICLR 2027 in-review submissions appear as ids and
  titles only.

## Credits and license

MIT (see [LICENSE](LICENSE)), inherited from [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest).
Corpus seed lists: lobehub/awesome-rsi, ANative-Lab/Awesome-Self-Evolving-Agents, XMUDeepLIT/Awesome-Self-Evolving-Agents,
selfimproving-agent/Awesome-Self-Improving-Agents, wkqdzkd/Awesome-Reliable-Self-Evolving-Agents,
EvoMap/awesome-agent-evolution, iSEngLab/Awesome-Self-Evolving-Coding-Agents. Outcome labels from OpenReview.
