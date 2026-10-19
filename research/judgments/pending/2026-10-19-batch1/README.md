# PENDING — 2026-10-19, first 115-paper batch

**Not published to the scoring board. Not a completed daily queue.**

The owner authorized this pending checkpoint on 2026-10-19. It preserves reviewed work while historical-source access is incomplete. `research/score.py` reads only `research/judgments/*.jsonl` (non-recursively), so this nested directory does not enter the board build. No scoring standard is changed.

## Coverage

- Original batch: 115 unique queue IDs; A **62**, B **42**, C **11**.
- `screen.jsonl`: 115 title/abstract screens. `signatures.jsonl`, `assignments.jsonl`, `judgments.jsonl`, `ids.txt`: 104 A/B papers, exact matching ID sets.
- New judgment quote/schema checks: **104 records, 0 problems**. Every non-unclear scored evidence claim is checked against the available prescribed extraction; missing extracted evidence stays unclear.
- Provisional top within this batch: **2610.13991, 80, ★★★, improver**. This is a pending calculation, not a published score.
- Latest pull, `a43020c`, expands `research/queue/2026-10-19.txt` to **332 IDs**. The additional **217 IDs have not been screened or judged in this checkpoint**. The queue stays active and is not moved to `done/`.

## Publication blockers

At the 06:05 UTC recovery checkpoint, 451 of 585 historical fulltext files were available and 134 were missing. Five fetches were explicitly refused with tunnel HTTP 403 and fell back to abstracts:

- 2602.04837
- 2606.23075
- 2606.24081
- 2606.24151
- 2606.26294

The fallback files cause **37 historical quote-validation failures**, listed in `historical_quote_failures.txt`. They are not valid replacements for the original source evidence. The five refused targets were not requested again. Fetching the other 134 IDs subsequently failed before execution because the approved execution environment could not start. The missing-ID list is a dated recovery snapshot, not a statement that those papers are inaccessible everywhere.

Full publication requires restored authorized source access or authentic original fulltext caches, plus processing the remaining 217 papers. Do not fabricate fulltext from judgment quotes, weaken historical judgments, alter validation standards, or publish a reduced historical board. The official 585-row scores, README board/gallery, and queue are unchanged by this pending commit.

## Other preserved work

- `triage.patch` preserves the original local 115-paper triage changes as an unapplied artifact. The official screen/signature/assignment files are not changed by this pending commit. Recheck deduplication before applying it.
- `pi-local-repair.md` preserves a diagnosis with code read at commit `58bc2861aa60f7720f5b994c9d4d31387fb63d43`; no reviewed code was run. Its symbolic finite-world limits are explicit. It is a draft, not a claim that the highest-scoring weekly-card requirement is complete.
- No paper fulltext, reviews, credentials, tokens, or downloaded source code are included.
- No suspected instruction injection was found in the reviewed paper text. Content discussing attacks was assessed as research data.

## Reel status

No posters or interpretations generated. Stage C requires all queued A/B scoring to be complete first. In addition, the required poster tooling was previously refused by a safety scan; it has not been retried, renamed, copied locally, or replaced to bypass that refusal. Do not execute an installer that disables approval or sandbox safeguards.

## Safe continuation

1. Re-read current repository standards; deduplicate this checkpoint against any work published since it was saved.
2. Restore permitted authentic source material and verify all historical records without skipped batches.
3. Process the remaining 217 IDs (and any later arrivals), then integrate the pending judgment files into the official dated batch only when complete.
4. Run the required signature, judgment, board, and card checks. Preserve all 585 existing board IDs, and do not mark this queue done early.
5. Publish authorized score/card changes with `git pull --rebase` before each push, no force-push, and verify remote contents.
6. Only after every queued scoring file is complete and the required tools are permitted, produce at most three exact-version, PDF-backed Reel assets and pass `check_reel.py`.
