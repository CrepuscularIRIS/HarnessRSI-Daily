"""Mechanical check for one v3 Sol batch (SCORE_SPEC §5/§6, controller-only).

Verifies ID one-to-one mapping, required fields, rating ranges, screen_score
arithmetic, evidence/reason counts, and status/total consistency. Structure
pass is not scientific validation.

Usage: python3 research/v3/tools/check_batch.py --run rsi-v3-20261022-01 --batch b001
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
W = {"G": 15, "M": 20, "X": 20, "E": 45}
STATUSES = {"scored", "needs_material", "out_of_scope"}
CLAIM_TYPES = {"system_method", "component_training", "evaluation_resource", "theory_analysis"}
SUPPORT = {"supported_in_material", "scoped", "unresolved", "contradicted"}
EV_LEVELS = {"task", "retained", "improver", "unknown"}
PSTAT = {"matched", "outside_taxonomy", "uncertain"}


def check(run: str, batch: str) -> list[str]:
    errs = []
    bdir = REPO / "research/v3/runs" / run / "batches"
    tsv = bdir / f"{batch}-inputs.tsv"
    out = bdir / f"{batch}.jsonl"
    want = [l.split("\t") for l in tsv.read_text().splitlines()[1:] if l.strip()]
    want_ids = [r[0] for r in want]
    titles = {r[0]: r[3] for r in want}
    if len(set(want_ids)) != len(want_ids):
        errs.append("inputs.tsv has duplicate paper ids")
    if not out.exists():
        return [f"missing output {out.name}"]

    got = {}
    for n, line in enumerate(open(out), 1):
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"line {n}: invalid JSON ({e})")
            continue
        pid = d.get("paper_id")
        if pid in got:
            errs.append(f"line {n}: duplicate paper {pid}")
        got[pid] = d
        for f in ("version", "source_url", "material_level", "status", "claim_type",
                  "move", "gap", "patterns", "ratings", "reasons", "evidence",
                  "claim_support", "evidence_level", "caveat"):
            if f not in d:
                errs.append(f"line {n} ({pid}): missing field {f}")
        if d.get("status") not in STATUSES:
            errs.append(f"line {n} ({pid}): bad status {d.get('status')}")
        if d.get("claim_type") not in CLAIM_TYPES:
            errs.append(f"line {n} ({pid}): bad claim_type")
        if d.get("claim_support") not in SUPPORT:
            errs.append(f"line {n} ({pid}): bad claim_support")
        if d.get("evidence_level") not in EV_LEVELS:
            errs.append(f"line {n} ({pid}): bad evidence_level")
        r = d.get("ratings") or {}
        for ax in ("G", "M", "X", "E"):
            v = r.get(ax)
            if v is not None and (not isinstance(v, int) or not 0 <= v <= 4):
                errs.append(f"line {n} ({pid}): rating {ax}={v} out of range")
        pat = d.get("patterns") or {}
        if pat.get("status") not in PSTAT:
            errs.append(f"line {n} ({pid}): bad patterns.status")
        ev = d.get("evidence") or []
        if not 1 <= len(ev) <= 3:
            errs.append(f"line {n} ({pid}): evidence count {len(ev)} not in 1..3")
        if not isinstance(d.get("reasons"), dict) or set(d.get("reasons") or {}) != set(W):
            errs.append(f"line {n} ({pid}): reasons must have exactly G/M/X/E")
        if d.get("status") == "scored":
            if any(r.get(ax) is None for ax in W):
                errs.append(f"line {n} ({pid}): scored but has null rating")
                continue
            expect = sum(W[a] * r[a] for a in W) / 4
            got_s = d.get("screen_score")
            if got_s is None or abs(got_s - expect) > 0.051:
                errs.append(f"line {n} ({pid}): screen_score {got_s} != {expect}")
        else:
            if d.get("screen_score") is not None:
                errs.append(f"line {n} ({pid}): {d.get('status')} but screen_score not null")

    missing = set(want_ids) - set(got)
    extra = set(got) - set(want_ids)
    if missing:
        errs.append(f"missing papers: {sorted(missing)}")
    if extra:
        errs.append(f"extra papers: {sorted(extra)}")
    for pid in set(got) & set(want_ids):
        if got[pid].get("material_level") not in ("full", "core", "abstract"):
            errs.append(f"{pid}: bad material_level")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--batch", required=True)
    args = ap.parse_args()
    errs = check(args.run, args.batch)
    if errs:
        print(f"FAIL {args.batch}: {len(errs)} error(s)")
        for e in errs:
            print("  -", e)
        return 1
    print(f"OK {args.batch}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
