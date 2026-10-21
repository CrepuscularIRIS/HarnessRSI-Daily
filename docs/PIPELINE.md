# Pipeline — how a paper gets from "someone mentioned it" to the board

Distilled from the run that built this repo (research/PIPELINE.md is that run's log). Every step names its input,
output, who does it, and the check that must pass. Deterministic steps are scripts; judgment steps are LLM work whose
output is validated by a script before anything is published.

```
Grok bot ──▶ inbox/YYYY-MM-DD.jsonl
                 │
                 ▼  (D) research/ingest.py            dedup, arXiv metadata → corpus.jsonl, HF code links (Grok)
            research/queue/YYYY-MM-DD.txt  ──▶ 本地打分 session (dual-model blind panel)
                 │
                 ▼  (L) 1 screen      research/SCREEN_RUBRIC.md      → research/screen.jsonl        tier A/B/C
                 ▼  (L) 2 signature   research/SIGNATURE_SCHEMA.md   → research/signatures.jsonl    (A/B only)
                 ▼  (L) 3 assign      research/patterns/taxonomy_view.json → research/patterns/assignments.jsonl
                 ▼  (L) 4 judge ×2    research/SCORE_SPEC.md         → research/judgments/<date>.{sol,opus}.jsonl  (two blind models)
                 ▼  (D) 5 score       research/score.py build        → research/scores.jsonl (average; Δ>10 or band mismatch → judgments/DUAL_FLAGS.md)
                 ▼  (D) 6 board       research/build_board.py        → papers/README.md, README top-30
                 ▼  (D) 7 checks      see "Check suite"              → commit
```
(D) = deterministic script · (L) = LLM judgment, validated by a script

## Steps

| # | Step | Who | Input → output | Validation (must pass) |
|---|---|---|---|---|
| 0 | Collect candidates | Grok bot | web/arXiv/HF/GitHub/X → `inbox/YYYY-MM-DD.jsonl` | `inbox/README.md` format |
| 1 | Ingest + queue | Grok bot (script) | inbox → `corpus.jsonl`, `fulltext/<id>.txt`, `hf_meta.jsonl` | prints remaining LLM steps |
| 2 | Screen | 打分 session | title+abstract → `screen.jsonl` row (tier, level, kind, evolved) | enums per `SCREEN_RUBRIC.md` |
| 3 | Signature (A/B) | 打分 session | full text → `signatures.jsonl` row | `python3 research/check_signatures.py <file> <ids>` |
| 4 | Assign pattern | 打分 session | signature + `taxonomy_view.json` → `assignments.jsonl` row (sub, secondary_main, fit) | sub id exists; no outcome labels used |
| 5 | Judge ×2 (blind) | 两个盲 subagent（gpt-6.1-sol、claude-opus-5-5） | full text + `conditions.json[main]` + main/sub cards → one judgment row per model in `<date>.{sol,opus}.jsonl` | `PYTHONPATH=research python3 research/score.py check <file> <ids>` for both files (quotes verified against the full text) |
| 6 | Score | script | the two models' judgments → averaged `scores.jsonl`; disagreements → `judgments/DUAL_FLAGS.md` | `score.py build` reports 0 skipped |
| 7 | Board | 打分 session (script) | scores → `papers/README.md`, README block | — |
| 8 | Diagnosis card (optional, top new A papers) | 打分 session | `cards/_TEMPLATE.md` | `python3 check_cards.py` |

## Check suite (run before every commit)

```bash
python3 test_check_cards.py && python3 check_cards.py
PYTHONPATH=research python3 research/score.py check research/judgments/<today>.jsonl research/judgments/ids_<today>.txt
PYTHONPATH=research python3 research/score.py build && python3 research/build_board.py
PYTHONPATH=research python3 research/build_bundles.py && python3 research/check_patterns.py   # only if cards changed
```

## Periodic work

| Cadence | Task | How |
|---|---|---|
| daily | steps 1–7 for the day's inbox | one commit `daily: YYYY-MM-DD (A×n, B×m)` |
| weekly | diagnosis cards for the week's top 1–3 new A papers; refresh `python3 research/contrast.py` | commit `weekly: …` |
| monthly or on model change | calibration: re-judge 3 gold papers into `/tmp/cal.jsonl`, run `PYTHONPATH=research python3 research/calibrate.py /tmp/cal.jsonl` | FLAG → stop publishing scores, ask a human |
| monthly | taxonomy health: share of new papers with `fit: low`; if > 30%, propose (do not apply) a taxonomy revision | issue for a human |
| when OpenReview quota allows | fetch ICLR reviews for the contrast set, ≤ 400 requests/hour | `research/fetch_reviews.py` |

## Data rules that cost us rework (keep them)

- **Outcome labels never reach a judging or assigning model.** Strip venue headers from PDFs; never pass `openreview.jsonl` labels into prompts.
- **Rejected papers are mostly abstract-only.** Never compare accepted vs rejected work on evidence or limitations — only on mechanism.
- **Dedup across sources by fuzzy title** (`contrast.or_duplicates`); the arXiv id is canonical.
- **Code availability comes from data, not from a truncated text** (`score.code_sources`: anchors → arXiv comment → HF Papers).
- **OpenReview authenticated quota is 500 requests per sliding hour.** Never loop retries; honor `Retry-After`.
- **Local only, never committed:** `research/fulltext/`, `research/reviews/`, `research/patterns/bundles/`, credentials.
- Pattern cards never name a paper; diagnosis cards (`cards/`) do, and must cite versions and SHAs.
