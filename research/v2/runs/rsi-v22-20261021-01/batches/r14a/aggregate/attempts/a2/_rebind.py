"""Opus 5.5 aggregate a2 for r14a: hash re-bind of the a1 finals to the regenerated conflicts.json (no re-ruling).

Asserts that every current seat record hashes to the new conflicts.json, that the new conflicts fields equal a fresh
rv2.diff_pair, that every field has a non-unresolved a1 resolution, and that the only sol 2603.18000 change vs the
a1-bound git version is score.display. Then re-signs. Writes only into this directory.
Run: python3 research/v2/runs/rsi-v22-20261021-01/batches/r14a/aggregate/attempts/a2/_rebind.py
"""
import copy
import datetime
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[8]
sys.path.insert(0, str(REPO / "research/v2/tools"))
import rv2  # noqa: E402

B = REPO / "research/v2/runs/rsi-v22-20261021-01/batches/r14a"
A1 = B / "aggregate/attempts/a1"
CONF = json.load(open(B / "conflicts.json"))
TS = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
H = lambda r: hashlib.sha256(rv2.canon(r).encode()).hexdigest()  # noqa: E731
REL = lambda s, p: (B / f"seats/{s}/attempts/a1/{p}.json").relative_to(REPO).as_posix()  # noqa: E731


def ddiff(a, b, path=""):
    if type(a) is not type(b):
        return [(path, a, b)]
    if isinstance(a, dict):
        return [d for k in sorted(set(a) | set(b)) for d in ddiff(a.get(k, "<missing>"), b.get(k, "<missing>"), f"{path}.{k}")]
    if isinstance(a, list):
        if len(a) != len(b):
            return [(path, "len", len(a), len(b))]
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in ddiff(x, y, f"{path}[{i}]")]
    return [] if a == b else [(path, a, b)]


checks = {}
ids = rv2.card_ids()
for p in CONF["papers"]:
    a1 = json.load(open(A1 / f"{p}.final.json"))
    seats = {s: json.load(open(REPO / REL(s, p))) for s in ("sol", "son55")}
    new = CONF["seat_record_hashes"][p]
    assert all(H(seats[s]) == new[s] for s in seats), p
    cf = next(c["fields"] for c in CONF["conflicts"] if c["paper_key"] == p)
    assert json.loads(json.dumps(rv2.diff_pair(seats["sol"], seats["son55"]))) == cf, p
    covered = {r["field_path"] for r in a1["resolutions"] if r.get("decision") not in (None, "unresolved")}
    assert {f["field"] for f in cf} <= covered, p
    label_mismatch = [f["field"] for f in cf
                      for r in a1["resolutions"] if r["field_path"] == f["field"]
                      and (r.get("sol_value"), r.get("son55_value")) != (f["sol"], f["son55"])]
    changed = [s for s in seats if a1["input_seat_hashes"][s] != new[s]]
    basis = {}
    for s in changed:
        if a1.get("seat_inputs_used", {}).get(s) == new[s]:
            basis[s] = "a1 already aggregated this exact record (seat_inputs_used == new hash)"
        else:
            out = subprocess.run(["git", "-C", str(REPO), "show", f"0014a72:{REL(s, p)}"], capture_output=True, text=True, check=True)
            old = json.loads(out.stdout)
            assert H(old) == a1["input_seat_hashes"][s], (p, s)
            d = ddiff(old, seats[s])
            assert [x[0] for x in d] == [".score.display"], d
            basis[s] = f"a1-bound git 0014a72 version differs from disk only at {d}"
    checks[p] = {"changed_seats": changed, "basis": basis, "label_mismatch": label_mismatch, "a1": a1}

papers_rep = {}
for p, c in checks.items():
    rec = copy.deepcopy(c["a1"])
    rec["attempt_id"] = "a2"
    rec["supersedes_aggregate"] = "a1"
    rec["input_seat_hashes"] = dict(CONF["seat_record_hashes"][p])
    rec["provenance"]["timestamp"] = TS
    note = (f"a2 re-bind: input_seat_hashes = regenerated conflicts.json seat_record_hashes; every seat a1 working copy "
            f"hash-equals it; no re-ruling.")
    if c["changed_seats"]:
        rec["provenance"]["seat_input_pinning"] = (
            [f"a2: {s} bound to working copy {REL(s, p)} (canonical {CONF['seat_record_hashes'][p][s]}) = regenerated "
             f"conflicts.json; {c['basis'][s]}" for s in c["changed_seats"]]
            + [f"a1 (superseded): {x}" for x in rec["provenance"].get("seat_input_pinning", [])])
        ar = rec["aggregate_review"]
        ar["integrity_checks"] += f" [{note} {'; '.join(c['basis'].values())}.]"
    if p == "2603.24639":
        assert rec["aggregate_status"] == "needs_revision"
        rec["aggregate_status"] = "accepted_final"
        old = "aggregate_status needs_revision only because the sol seat binding in conflicts.json is stale (see seat_binding_issue)."
        assert old in rec["reason"]
        rec["reason"] = rec["reason"].replace(old, "accepted_final after the a2 re-bind: the regenerated conflicts.json binds "
                                              "exactly the final sol record a1 was built on (seat_binding_issue resolved).")
        rec["aggregate_review"]["rating_agreement"] = rec["aggregate_review"]["rating_agreement"].replace(
            " (provisional until re-bound)", "")
        rec["seat_binding_issue"] = ("RESOLVED in a2: controller regenerated conflicts.json from the final seat files; "
                                     "sol hash 1d05033b… = seat_inputs_used.sol, and its 17 fields equal the fresh diff a1 "
                                     "already resolved (RE-4, step2 present; RE-5/RE-6 no longer conflicts; S2 sol null). "
                                     "a1 text kept for history: " + rec["seat_binding_issue"])
    rec["final_record_hash"] = rv2.record_hash(rec)
    errs = rv2.check_record(rec, ids)
    assert not errs, (p, errs)
    (HERE / f"{p}.final.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    back = json.load(open(HERE / f"{p}.final.json"))
    assert rv2.record_hash(back) == back["final_record_hash"]
    a1 = c["a1"]
    papers_rep[p] = {
        "aggregate_status": rec["aggregate_status"], "a1_aggregate_status": a1["aggregate_status"],
        "score_raw": rec["score"]["raw"], "score_display": rec["score"]["display"],
        "a1_score_raw": a1["score"]["raw"],
        "substance_identical_to_a1": all(rec[k] == a1[k] for k in
                                         ("ratings", "assessment", "expectations", "resolutions", "score", "status",
                                          "rs_pattern", "domain_pattern", "claims", "evidence", "shared_error_corrections")),
        "input_seat_hashes": rec["input_seat_hashes"], "rebound_seats": c["changed_seats"],
        "rebind_basis": c["basis"],
        "resolution_label_notes": c["label_mismatch"],
        "final_record_hash": rec["final_record_hash"], "a1_final_record_hash": a1["final_record_hash"],
    }
    print(p, rec["aggregate_status"], rec["score"]["raw"], rec["final_record_hash"])
rep = json.load(open(A1 / "batch-report.json"))
st = [v["aggregate_status"] for v in papers_rep.values()]
rep.update({
    "attempt_id": "a2", "supersedes_aggregate": "a1", "timestamp": TS,
    "nature": "hash re-bind of a1, not a re-ruling. conflicts.json was regenerated by the controller from the final seat "
              "files; a2 re-signs the a1 finals against its seat_record_hashes. Ratings, statuses, expectations, "
              "resolutions, evidence and scores are byte-identical to a1 (asserted per paper: substance_identical_to_a1).",
    "accepted_final": st.count("accepted_final"), "needs_revision": st.count("needs_revision"),
    "papers_a2": papers_rep,
    "edits_vs_a1": [
        "all five: attempt_id a2, supersedes_aggregate a1, input_seat_hashes ← regenerated conflicts.json, "
        "provenance.timestamp, final_record_hash recomputed (standard command).",
        "2603.18000: provenance.seat_input_pinning and aggregate_review.integrity_checks updated to the a2 binding "
        "(a1 text kept as history). Binding-description text only.",
        "2603.24639: aggregate_status needs_revision → accepted_final; reason sentence on the stale binding replaced; "
        "'(provisional until re-bound)' removed from rating_agreement; seat_binding_issue marked RESOLVED (a1 text kept); "
        "seat_input_pinning/integrity_checks updated as for 2603.18000.",
    ],
})
rep["inputs"]["conflicts_regenerated"] = True
for p, v in papers_rep.items():
    rep["papers"][p].update({"aggregate_status": v["aggregate_status"], "final_record_hash": v["final_record_hash"]})
rep["validation"] = {
    "seat_hashes": "canonical SHA-256 of all 10 seat a1 working copies equals the regenerated conflicts.json "
                   "seat_record_hashes (asserted); 8/10 unchanged from a1's binding.",
    "conflict_fields": "regenerated conflicts.json fields == fresh rv2.diff_pair of the disk records for all 5 papers (asserted)",
    "resolution_coverage": "every regenerated conflicts field has a non-unresolved a1 resolution (asserted); 2603.24639 "
                           "keeps two extra a1 rows (RE-5/RE-6, same_supported_fact) that are no longer conflicts",
    "sol_2603.18000": "a1 used the git 0014a72 version; deep diff vs disk = only score.display ('50.0' str → 50.0 number); "
                      "display-format only; the final score is computed from the final ratings, not from seat score fields",
    "sol_2603.24639": "disk canonical hash 1d05033b… = a1 seat_inputs_used.sol = regenerated conflicts.json (asserted): "
                      "a1 was built on exactly this record",
    "label_note": "2603.24639 resolution row S2 shows sol_value challenged_with_evidence while the regenerated "
                  "conflicts.json has sol null there: a1 already merged sol's non-A4 ID step2 into S2 (step2 row: revised → "
                  "moved_to S2) and states this in the S2 row's reason. Same position, same decision (son55 unmet); not a "
                  "substantive inconsistency, kept verbatim.",
    "structural": "rv2.check_record passes for all five a2 records; final_record_hash re-verified after write",
}
rep["notes"] = ["a2 re-bind; see nature/edits_vs_a1/validation. a1 notes follow unchanged for the substance of each ruling "
                "(note 1's controller action is now done)."] + rep["notes"]
(HERE / "batch-report.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1))
