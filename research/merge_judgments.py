"""Merge the two blind seats' judgments into one final record per paper (dual-seat design, 2026-10-21).

Seats (research/judge.py write them): research/judgments/passes/<B>.sol.jsonl (gpt-6.1-sol) and
<B>.son55.jsonl (claude-sonnet-5-5), both covering exactly ids_<B>.txt. Merge is item-level and deterministic:

- text fields (title_zh / one_line / one_line_zh / version_read): seat sol's, never flagged;
- evidence items, evidence_level, success/failure: same value → keep (quote from sol if it is in the
  full text, else son55's); different value → CONFLICT — placeholder `unclear` and a line in
  passes/<B>.conflicts.json;
- ap1: value conflict keeps sol's value and is marked must-arbitrate (`unclear` is not allowed there);
  mitigated conflict → placeholder `unclear`;
- conflicts are resolved by the arbiter seat (claude-opus-5-5): judge.py --arb writes passes/<B>.arb.jsonl,
  then `--apply-arb` overwrites the flagged fields and re-validates the whole batch.

The final research/judgments/<B>.jsonl is a single quote-backed record per paper, so `score.py build`
stays untouched and scores.jsonl remains reproducible from it.

Usage:
  PYTHONPATH=research python3 research/merge_judgments.py <B>              # merge → <B>.jsonl + conflicts.json
  PYTHONPATH=research python3 research/merge_judgments.py <B> --apply-arb # apply arb.jsonl → rewrite <B>.jsonl
"""

import json
import sys
from pathlib import Path

from check_evidence import FULLTEXT, squash
from score import check, context

R = Path("research")
SEATS = ("sol", "son55")


def quote_in(quote: str | None, hay: str | None) -> bool:
    return bool(quote) and hay is not None and squash(quote) in hay


def get(rec: dict, path: str):
    node = rec
    for part in path.split("."):
        node = node.get(part) if isinstance(node, dict) else None
    return node


def set_field(rec: dict, path: str, value, quote: str | None) -> None:
    """Set one judged field; ap1's value/mitigated/quote live flat in rec['ap1']."""
    if path.startswith("ap1."):
        rec["ap1"][path.split(".", 1)[1]] = value
        if quote:
            rec["ap1"]["quote"] = quote
        return
    parts = path.split(".")
    node = rec
    for p in parts[:-1]:
        node = node[p]
    node[parts[-1]] = {"value": value, **({"quote": quote} if quote else {})}


def merge_records(sol: dict, son55: dict, fulltext: str | None) -> tuple[dict, list[dict]]:
    """Pure merge of two seat records for one paper → (record, conflicts)."""
    rec, hay = json.loads(json.dumps(sol)), (squash(fulltext) if fulltext else None)
    conflicts = []

    def conflict(field: str, a: dict, b: dict, must_arb: bool) -> None:
        conflicts.append({"arxiv": sol["arxiv"], "field": field,
                          "sol": {"value": a.get("value"), "quote": a.get("quote")},
                          "son55": {"value": b.get("value"), "quote": b.get("quote")},
                          "must_arb": must_arb})

    paths = ([f"evidence.{k}" for k in sol["evidence"]] + ["evidence_level"]
             + [f"success.{k}" for k in sol["success"]] + [f"failure.{k}" for k in sol["failure"]])
    for path in paths:
        a, b = get(sol, path), get(son55, path)
        if not isinstance(a, dict) or not isinstance(b, dict):
            continue
        if a.get("value") == b.get("value"):
            q = a.get("quote") if quote_in(a.get("quote"), hay) else b.get("quote")
            set_field(rec, path, a["value"], q)
        else:
            conflict(path, a, b, must_arb=False)
            set_field(rec, path, "unclear", None)

    a, b = sol["ap1"], son55["ap1"]
    if a["value"] != b["value"]:  # no `unclear` for ap1.value: keep sol's, arbiter must decide
        conflict("ap1.value", {"value": a["value"], "quote": a.get("quote")},
                 {"value": b["value"], "quote": b.get("quote")}, must_arb=True)
    elif a.get("mitigated") != b.get("mitigated"):
        conflict("ap1.mitigated", {"value": a.get("mitigated")}, {"value": b.get("mitigated")}, must_arb=False)
        rec["ap1"]["mitigated"] = "unclear"
    return rec, conflicts


def load_passes(batch: str) -> dict[str, dict[str, dict]]:
    ids = set((R / f"judgments/ids_{batch}.txt").read_text().split())
    by = {}
    for seat in SEATS:
        p = R / f"judgments/passes/{batch}.{seat}.jsonl"
        if not p.exists():
            sys.exit(f"missing {p}")
        recs = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
        if {r["arxiv"] for r in recs} != ids:
            sys.exit(f"{p.name}: covers {len(recs)} of {len(ids)} ids — run the seat to completion first")
        by[seat] = {r["arxiv"]: r for r in recs}
    return by


def fulltext_for(aid: str) -> str | None:
    p = FULLTEXT / f"{aid.replace(':', '_')}.txt"
    return p.read_text(encoding="utf-8") if p.exists() else None


def main(argv: list[str]) -> int:
    batch = argv[0]
    final_path = R / f"judgments/{batch}.jsonl"
    conflicts_path = R / f"judgments/passes/{batch}.conflicts.json"
    main_of, cond = context()

    if "--apply-arb" in argv:
        decisions = json.loads((R / f"judgments/passes/{batch}.arb.jsonl").read_text())["decisions"]
        records = {r["arxiv"]: r for r in (json.loads(l) for l in final_path.read_text(encoding="utf-8").splitlines() if l.strip())}
        conflicted = json.loads(conflicts_path.read_text())["conflicts"]
        by_aid = {}
        for d in decisions:
            rec = records.get(d["arxiv"])
            if rec is None:
                sys.exit(f"arb decision for {d['arxiv']}, not in batch")
            if not any(c["field"] == item["field"] and c["arxiv"] == d["arxiv"] for c in conflicted for item in d["items"]):
                sys.exit(f"{d['arxiv']} {d['items'][0]['field']}: arb decides a field that was not in conflict")
            hay = squash(fulltext_for(d["arxiv"]) or "")
            for item in d["items"]:
                if item.get("quote") and squash(item["quote"]) not in hay:
                    sys.exit(f"{d['arxiv']} {item['field']}: arb quote not in full text")
                set_field(rec, item["field"], item["value"], item.get("quote"))
            by_aid[d["arxiv"]] = True
        unresolved = sorted({c["arxiv"] for c in conflicted if c["must_arb"]} - set(by_aid))
        errs = [e for aid, rec in sorted(records.items()) for e in check(rec, main_of, cond)]
        if errs:
            print("\n".join(errs))
            return 1
        final_path.write_text("".join(json.dumps(records[a], ensure_ascii=False) + "\n" for a in sorted(records)))
        print(f"applied arb for {len(by_aid)} papers; must-arb unresolved: {unresolved or 'none'}")
        return 0

    by = load_passes(batch)
    ids = set(by["sol"])
    records, conflicts = {}, []
    for aid in sorted(ids):
        rec, c = merge_records(by["sol"][aid], by["son55"][aid], fulltext_for(aid))
        records[aid] = rec
        conflicts += c
    errs = [e for aid, rec in sorted(records.items()) for e in check(rec, main_of, cond, verify_quotes=False)]
    if errs:  # the placeholder merge must already be structurally valid
        print("\n".join(errs))
        return 1
    final_path.write_text("".join(json.dumps(records[a], ensure_ascii=False) + "\n" for a in sorted(records)))
    conflicts_path.write_text(json.dumps({"batch": batch, "conflicts": conflicts}, ensure_ascii=False, indent=1) + "\n")
    print(f"merged {len(records)} papers → {final_path.name}; {len(conflicts)} conflicts "
          f"({sum(c['must_arb'] for c in conflicts)} must-arb) → {conflicts_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
