"""Assert-based self-check for merge_judgments (pure functions only; no repo state, no network).

Run: PYTHONPATH=research python3 research/test_merge_judgments.py
"""

from merge_judgments import merge_records, set_field


def seat(held="yes", held_q="we evaluate held-out tasks", level="retained", s1="yes", f1="no",
         ap1="no", mit="no"):
    return {"arxiv": "9999.00001", "title_zh": "题", "one_line": "a line", "one_line_zh": "一行", "version_read": "v1",
            "evidence": {"held_out": {"value": held, "quote": held_q},
                         "variance": {"value": "no", "quote": None}},
            "evidence_level": {"value": level, "quote": "retained artifact helps on new tasks"},
            "success": {"S1": {"value": s1, "quote": "the gate is trained end to end"}},
            "failure": {"F1": {"value": f1, "quote": None}},
            "ap1": {"value": ap1, "mitigated": mit, "quote": None}}


TEXT = "The gate is trained end to end. We evaluate held-out tasks. The retained artifact helps on new tasks."


def main() -> int:
    # 1. seats agree → value kept, quote from sol
    rec, c = merge_records(seat(), seat(), TEXT)
    assert rec["evidence"]["held_out"] == {"value": "yes", "quote": "we evaluate held-out tasks"}
    assert rec["success"]["S1"]["value"] == "yes" and not c, (rec, c)

    # 2. agree but sol's quote is not in the text → son55's quote used
    other = seat(held_q="a quote that appears nowhere in the text")
    son = seat()
    son["evidence"]["held_out"]["quote"] = "we evaluate held-out tasks"
    rec, c = merge_records(other, son, TEXT)
    assert rec["evidence"]["held_out"]["quote"] == "we evaluate held-out tasks", rec
    assert not c

    # 3. evidence disagree → placeholder unclear + conflict
    rec, c = merge_records(seat(held="yes"), seat(held="partial", held_q="partial support here"), TEXT)
    assert rec["evidence"]["held_out"]["value"] == "unclear"
    assert c[0]["field"] == "evidence.held_out" and not c[0]["must_arb"]
    assert c[0]["sol"]["value"] == "yes" and c[0]["son55"]["value"] == "partial"

    # 4. evidence_level disagree → unclear + conflict
    rec, c = merge_records(seat(level="retained"), seat(level="task"), TEXT)
    assert rec["evidence_level"]["value"] == "unclear" and c[0]["field"] == "evidence_level"

    # 5. ap1.value disagree → sol's value kept, must-arb
    rec, c = merge_records(seat(ap1="no"), seat(ap1="yes"), TEXT)
    assert rec["ap1"]["value"] == "no" and c[0]["field"] == "ap1.value" and c[0]["must_arb"]

    # 6. ap1.value agrees, mitigated disagrees → mitigated becomes unclear, not must-arb
    rec, c = merge_records(seat(mit="no"), seat(mit="yes"), TEXT)
    assert rec["ap1"]["mitigated"] == "unclear" and c[0]["field"] == "ap1.mitigated" and not c[0]["must_arb"]

    # 7. text fields always sol's; set_field reaches nested and ap1 paths
    s2 = seat()
    s2["title_zh"] = "错"
    rec, _ = merge_records(seat(), s2, TEXT)
    assert rec["title_zh"] == "题"
    r = seat()
    set_field(r, "success.S2", "yes", "a new span")
    assert r["success"]["S2"] == {"value": "yes", "quote": "a new span"}
    set_field(r, "ap1.value", "yes", "single-document loop")
    assert r["ap1"]["value"] == "yes" and r["ap1"]["quote"] == "single-document loop"

    print("test_merge_judgments: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
