# Reverse-engineering pipeline state (unattended run, started 2026-10-18)

Goal: Harness-level RSI analogue of ResearchStudio's 15+31 pattern cards, built from the corpus,
then push the repo to GitHub as a **PUBLIC** repo `CrepuscularIRIS/HarnessRSI-Daily` (owner instruction, 2026-10-18).

Each wake-up: check background tasks/agents → do the first unchecked step whose inputs exist → tick it here → commit.
Never re-launch work that is still running. Commit after every step (`git log` is the audit trail).

## Done
- [x] 1 corpus 1,198 papers (research/corpus.jsonl)
- [x] 2 screening A 400 / B 185 (research/screen.jsonl)
- [x] 3 signatures 585 A/B (research/signatures.jsonl; evidence fields there are NOT trusted)
- [x] 4 taxonomy draft 13 main / 36 sub (research/patterns/taxonomy.json, assignments.jsonl); IRR main κ=0.84
- [x] 5 quote-grounded evidence, 200 labeled corpus papers (research/evidence_corpus.jsonl)
- [x] 6 OpenReview ICLR 2025-27 pull + screening: 193 A/B (research/screen_or.jsonl, or_ab_ids.txt)

## Remaining
- [~] 7 SKIPPED 16:2x (3 attempts; only 28/268 fetched — OpenReview 500 req/h quota kept exhausted; left for maintenance) (FALLBACK: if still 429 after 3 attempts, mark step 7 and 11 as skipped and write cards without review notes; leave a TODO panel) reviews for 268 ICLR forums → research/reviews/ (local only). Fetcher stops on 429; rerun FROM REPO ROOT `PYTHONPATH=research python3 research/fetch_reviews.py --env ~/competitor/ResearchStudio/ResearchStudio-Idea/.env` until it prints "done" (429 at 18:xx on 10-18: account throttled after PDF retries; wait ≥40 min between attempts).
- [x] 8 signatures for the 193 OR papers from abstract + full text if present (research/fulltext/or_*.txt) — NOT from reviews (reviews must not shape the signature). Output research/signatures_or.jsonl, validated by check_signatures.py. Evidence fields there stay "unclear".
- [x] 9 assign the 193 OR papers to the taxonomy (one agent, taxonomy_view.json only, no labels) → research/patterns/assignments_or.jsonl
- [x] 10 (script ready: `python3 research/contrast.py`) contrast stats → research/patterns/contrast.json + contrast.md: per main / sub pattern n_accept, n_reject(reject+withdrawn), p_accept, Δ vs base rate; 2-way compositions (primary main + secondary_main) with n≥15 and Δ≤−12pp → anti-pattern candidates; evidence-item rates accept vs reject (corpus 200). Script: research/contrast.py (deterministic).
- [~] 11 SKIPPED (depends on 7; main cards carry a 'Reviewer expectations — pending' panel built from the quote-grounded evidence audit instead) review distillation per main pattern (13 agents max, Opus): read reviews of that pattern's accepted vs rejected papers → paraphrased success conditions / failure modes / accept-vs-reject gap / reviewer expectations. No paper ids, no verbatim review text. → research/patterns/review_notes/<main_id>.md
- [x] 12 (12a DONE: 36 sub cards, guard clean; 12b main cards: dispatched after step-11 skip) write cards (Opus): `patterns/main/<id>.md` (13) in RS card structure + `patterns/sub/Hxx.md` (36) + `patterns/overview.md` + `patterns/anti-patterns.md`. Every quantitative claim must come from contrast.json. Mark the 3 weight-training main patterns as "boundary (touches L1)".
- [x] 13 (README drafted; re-check after cards) README rewrite (project, structure, method, credits: base code yang3kc/daily_arxiv_digest MIT; method inspired by ResearchStudio-Idea; lists used as corpus sources), check no secrets (`grep -rI "OPENREVIEW_PASS=" .`), run `python3 test_check_cards.py && python3 check_cards.py`.
- [ ] 14 pre-publish scrub, then create PUBLIC GitHub repo CrepuscularIRIS/HarnessRSI-Daily, add remote, push main. Then delete the cron job and report.
  Scrub before push: (a) research/openreview_pull.jsonl — drop `abstract` from all `pending` (ICLR 2027 in-review) rows; (b) no review text, no full text, no secrets in the tree (`git ls-files | grep -E "fulltext/|reviews/"` empty); (c) cards/patterns never name a rejected/withdrawn paper. History contains the 2027 abstracts from earlier commits → rewrite is NOT allowed by MAINTAINING rules, so instead squash: publish a fresh orphan branch `main` built from the scrubbed tree (local history kept on branch `dev-history`, not pushed).

## Notes / decisions
- Outcome labels never shown to extraction or assignment agents (headers stripped; venue removed).
- OpenReview rate limits are strict: PDF endpoint 429'd the whole account; do not loop retries.
- Full texts and reviews stay local (research/fulltext/, research/reviews/ are gitignored).

- 2026-10-18 data-source artifact found: rejected members are mostly abstract-only OpenReview records (151/193 empty limitations vs 0/585). All cards now compare outcomes on mechanism only; guard + grep verified.
- 6 arXiv/OpenReview duplicates canonicalized to arXiv ids (contrast.or_duplicates).
