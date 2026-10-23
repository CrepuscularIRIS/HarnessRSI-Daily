"""Fetch version-pinned fulltext for scoring runs (L2 material backfill).

Layout: private research/fulltext/review-runs/<run>/materials/<id>.txt (gitignored),
sidecar meta appended to research/scoring/runs/<run>/materials/<id>.json when the
run dir exists. HTML -> PDF fallback, 3s pacing, exit 75 on rate limit (rerun resumes).

Usage: python3 research/scoring/tools/fetch_fulltext.py --ids 2610.12345,... | --ids-file f.txt
"""

import argparse
import hashlib
import json
import sys
import tempfile
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
import importlib.util

REPO = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("net", REPO / "research/net.py")
net = importlib.util.module_from_spec(spec)
spec.loader.exec_module(net)
RateLimited, get = net.RateLimited, net.get

HTML_URL = "https://arxiv.org/html/{vid}"
PDF_URL = "https://arxiv.org/pdf/{vid}"
MAX_CHARS, MIN_CHARS = 3_000_000, 3_000


def squash(text: str) -> str:
    import re
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
    import subprocess
    with tempfile.NamedTemporaryFile(suffix=".pdf", dir="/tmp", delete=False) as f:
        f.write(body)
        path = f.name
    try:
        out = subprocess.run(["pdftotext", "-q", "-enc", "UTF-8", path, "-"],
                             capture_output=True, timeout=180)
        return squash(out.stdout.decode("utf-8", "replace"))
    finally:
        Path(path).unlink(missing_ok=True)


def fetch_one(aid: str, version: str, priv: Path, pub: Path | None) -> dict:
    text_path = priv / f"{aid}.txt"
    meta_path = pub / f"{aid}.json" if pub else None
    if meta_path and meta_path.exists() and text_path.exists():
        old = json.loads(meta_path.read_text())
        if old.get("complete") and old.get("sha256") == hashlib.sha256(text_path.read_bytes()).hexdigest():
            old["skipped"] = True
            return old
    attempts = []
    for method, url, conv in (("html", HTML_URL.format(vid=version), html_text),
                              ("pdf", PDF_URL.format(vid=version), pdf_text)):
        try:
            body = get(url)
        except urllib.error.HTTPError as e:
            attempts.append({"method": method, "http": e.code})
            continue
        text = conv(body)
        if len(text) < MIN_CHARS:
            attempts.append({"method": method, "chars": len(text), "why": "too_short"})
            continue
        truncated = len(text) > MAX_CHARS
        priv.mkdir(parents=True, exist_ok=True)
        text_path.write_text(text[:MAX_CHARS], encoding="utf-8")
        meta = {"paper_key": aid, "version": version, "source_url": url, "method": method,
                "sha256": hashlib.sha256(text_path.read_bytes()).hexdigest(),
                "chars": min(len(text), MAX_CHARS), "complete": not truncated,
                "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "attempts": attempts}
        if pub:
            pub.mkdir(parents=True, exist_ok=True)
            meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
        return meta
    return {"paper_key": aid, "complete": False, "attempts": attempts, "why": "no_complete_text"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default="")
    ap.add_argument("--ids-file", default="")
    args = ap.parse_args()
    corpus = {json.loads(l)["arxiv"]: json.loads(l) for l in open(REPO / "research/corpus.jsonl")}
    ids = [i for i in args.ids.split(",") if i]
    if args.ids_file:
        ids += [l.strip() for l in open(args.ids_file) if l.strip()]
    priv = REPO / "research/fulltext/review-runs/rsi-l1-20261022-03/materials"
    pub = REPO / "research/scoring/runs/rsi-l1-20261022-03/materials"
    ok = skipped = miss = 0
    try:
        for aid in ids:
            meta = fetch_one(aid, corpus[aid].get("latest_version") or aid, priv, pub)
            if meta.get("skipped"):
                skipped += 1
            elif meta.get("complete"):
                ok += 1
            else:
                miss += 1
                print(f"MISS {aid}: {meta.get('attempts')}", file=sys.stderr)
    except RateLimited as e:
        print(f"RATE-LIMITED, rerun to resume: {e}", file=sys.stderr)
        print(json.dumps({"complete": ok, "skipped": skipped, "incomplete": miss}))
        return 75
    print(json.dumps({"complete": ok, "skipped": skipped, "incomplete": miss}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
