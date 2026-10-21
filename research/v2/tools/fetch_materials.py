"""Fetch version-pinned complete fulltext for v2.2 review runs.

Target layout (private, gitignored): research/fulltext/review-runs/<run_id>/materials/<paper_key>.txt
Public sidecar meta (tracked):        research/v2/runs/<run_id>/materials/<paper_key>.json

Order per paper: arXiv version-pinned HTML rendering (complete, appendix included) →
version-pinned PDF + pdftotext. Neither → meta records complete=false (needs_fulltext lead).
Pacing/429 handling comes from research/net.py (exit 75 on rate limit; rerun resumes).
Old cropped cache research/fulltext/<id>.txt is index-only and never used here.

Usage: python3 research/v2/tools/fetch_materials.py --run <run_id> --ids 2303.11366,2505.18524
       python3 research/v2/tools/fetch_materials.py --run <run_id> --ids-file path.txt
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from net import RateLimited, get  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
HTML_URL = "https://arxiv.org/html/{vid}"
PDF_URL = "https://arxiv.org/pdf/{vid}"
MAX_CHARS = 3_000_000
MIN_CHARS = 3_000  # below this the extraction is not a usable fulltext


def squash(text: str) -> str:
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in text.splitlines()]
    out, blank = [], 0
    for ln in lines:
        if ln:
            out.append(ln)
            blank = 0
        elif blank < 1:
            out.append("")
            blank += 1
    return "\n".join(out).strip()


def html_text(body: bytes) -> str:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(body, "html.parser")
    for tag in soup.select("script, style, nav, .ltx_page_footer, .ltx_bibliography"):
        tag.decompose()
    return squash(soup.get_text("\n"))


def pdf_text(body: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf", dir="/tmp", delete=False) as f:
        f.write(body)
        path = f.name
    try:
        out = subprocess.run(["pdftotext", "-q", "-enc", "UTF-8", path, "-"],
                             capture_output=True, timeout=180)
        return squash(out.stdout.decode("utf-8", "replace"))
    finally:
        Path(path).unlink(missing_ok=True)


def fetch_one(run_id: str, paper: dict, priv: Path, pub: Path, pdf_only: bool = False) -> dict:
    key, vid = paper["paper_key"], paper["version"]
    meta_path = pub / f"{key}.json"
    text_path = priv / f"{key}.txt"
    if meta_path.exists() and text_path.exists():
        old = json.loads(meta_path.read_text())
        if old.get("complete") and old.get("sha256") == hashlib.sha256(text_path.read_bytes()).hexdigest():
            old["skipped"] = True
            return old
    attempts = []
    sources = (("pdf", PDF_URL.format(vid=vid), pdf_text),) if pdf_only else (
        ("html", HTML_URL.format(vid=vid), html_text),
        ("pdf", PDF_URL.format(vid=vid), pdf_text))
    for method, url, conv in sources:
        try:
            body = get(url)
        except urllib.error.HTTPError as e:
            attempts.append({"method": method, "url": url, "http": e.code})
            continue
        text = conv(body)
        if len(text) < MIN_CHARS:
            attempts.append({"method": method, "url": url, "chars": len(text), "why": "too_short"})
            continue
        truncated = len(text) > MAX_CHARS
        text_path.write_text(text[:MAX_CHARS], encoding="utf-8")
        meta = {
            "paper_key": key, "arxiv": paper["arxiv"], "version": vid,
            "source_url": url, "method": method,
            "sha256": hashlib.sha256(text_path.read_bytes()).hexdigest(),
            "bytes": text_path.stat().st_size, "chars": min(len(text), MAX_CHARS),
            "complete": not truncated, "truncated": truncated,
            "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "attempts": attempts,
        }
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
        return meta
    meta = {
        "paper_key": key, "arxiv": paper["arxiv"], "version": vid,
        "source_url": None, "method": None, "sha256": None, "bytes": 0, "chars": 0,
        "complete": False, "truncated": False,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "attempts": attempts, "why": "no_complete_text",
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    return meta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--ids", default="")
    ap.add_argument("--ids-file", default="")
    ap.add_argument("--pdf-only", default="", help="comma ids to force PDF source (v2 re-pin)")
    args = ap.parse_args()
    repo = REPO
    run_dir = repo / "research/v2/runs" / args.run
    priv = repo / "research/fulltext/review-runs" / args.run / "materials"
    pub = run_dir / "materials"
    priv.mkdir(parents=True, exist_ok=True)
    pub.mkdir(parents=True, exist_ok=True)
    queue = {q["paper_key"]: q for q in map(json.loads, open(run_dir / "queue.jsonl"))}
    ids = [i for i in args.ids.split(",") if i]
    pdf_ids = {i for i in args.pdf_only.split(",") if i}
    if args.ids_file:
        ids += [i.strip() for i in open(repo / args.ids_file) if i.strip()]
    stats = {"complete": 0, "incomplete": 0, "skipped": 0}
    try:
        for key in ids:
            paper = queue.get(key) or {"paper_key": key, "arxiv": key, "version": key}
            meta = fetch_one(args.run, paper, priv, pub, pdf_only=(key in pdf_ids))
            if meta.get("skipped"):
                stats["skipped"] += 1
            elif meta["complete"]:
                stats["complete"] += 1
            else:
                stats["incomplete"] += 1
                print(f"INCOMPLETE {key}: {meta.get('why')} attempts={meta.get('attempts')}", file=sys.stderr)
    except RateLimited as e:
        print(f"RATE-LIMITED, rerun to resume: {e}", file=sys.stderr)
        print(json.dumps(stats))
        return 75
    print(json.dumps(stats))
    return 0


if __name__ == "__main__":
    sys.exit(main())
