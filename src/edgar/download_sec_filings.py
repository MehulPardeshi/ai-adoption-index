#!/usr/bin/env python3
"""
Team 5 - SEC test-run data collection (owner: Yen-Chu, with Shu)

Downloads the 10-K and 10-Q filings whose period ends between --start and
--end (default: Q3 2024 to Q2 2026, 8 quarters) for the test-run companies,
saves the raw HTML and a plain-text copy, and pulls every paragraph that
mentions AI into an AI-passages file.

Run from the repo root:
    python3 src/edgar/download_sec_filings.py

Writes:
    data/raw/sec/html/, data/raw/sec/text/   full filings (gitignored, ~550 MB)
    data/interim/sec/ai_passages.csv         AI paragraphs, verbatim SEC text
    data/processed/sec/filings_inventory.csv one row per filing (no text)
    data/processed/sec/run_info.json         when and how the data was pulled

Needs: requests, beautifulsoup4   (pip3 install -r requirements.txt)

SEC fair-access rules: we send a User-Agent with a name + email and stay
well under 10 requests/second. Only public EDGAR filings are collected.
"""

import argparse
import csv
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Missing libraries. Run:  pip3 install requests beautifulsoup4")

# ---------------------------------------------------------------- settings
USER_AGENT = "CMU Team5 AI-Tracker research Yen-Chu Chen yenchuc2@andrew.cmu.edu"
COMPANIES = [  # ticker -> name (CIK is looked up from SEC's ticker file)
    # PoC companies decided 2026-10-04 (memory/09-decisions-log.md)
    ("JPM", "JPMorgan Chase"),
    ("BAC", "Bank of America"),
    ("COF", "Capital One"),
    ("WFC", "Wells Fargo"),
    ("SCHW", "Charles Schwab"),
    ("PFG", "Principal Financial Group"),
    # Kept as a comparison: Citigroup was in the first test run (Oct 17)
    ("C", "Citigroup"),
]
FORMS = {"10-K", "10-Q"}          # originals only; amendments (10-K/A) skipped
START = "2024-07-01"              # filings whose period ends in this window
END = "2026-06-30"                # (inclusive) - 8 quarters
EXTRA_EXHIBITS = ("EX-13",)       # some banks (e.g. Wells Fargo) put the
                                  # annual report text in Exhibit 13
PAUSE = 0.25                      # seconds between requests (<10 req/s)

# AI terms. "strong" = clearly about AI. Bare "AI" is matched as a whole
# word, case-sensitive, so words like "said"/"AIG" don't match.
STRONG_TERMS = [
    r"artificial intelligence", r"machine[- ]learning", r"generative AI",
    r"gen ?AI", r"large language models?", r"\bLLMs?\b", r"deep learning",
    r"neural networks?", r"natural language processing", r"\bNLP\b",
    r"chat ?bots?", r"\bcopilots?\b", r"agentic", r"AI agents?",
    r"predictive (?:analytics|models?)", r"computer vision",
]
AI_WORD = r"(?<![A-Za-z])AI(?![A-Za-z])"
WEAK_TERMS = [r"\bautomation\b", r"\balgorithm(?:s|ic)?\b", r"advanced analytics"]

STRONG_RE = re.compile("|".join(STRONG_TERMS), re.I)
AI_WORD_RE = re.compile(AI_WORD)  # case-sensitive on purpose
WEAK_RE = re.compile("|".join(WEAK_TERMS), re.I)

# Rough section labels so we know *where* in the report AI shows up
SECTION_RE = re.compile(
    r"^(item\s+1a\.?\s*risk factors|risk factors|item\s+1\.?\s*business|"
    r"item\s+7\.?\s*management|management['’]s discussion|"
    r"item\s+1c\.?\s*cybersecurity|cybersecurity|competition|"
    r"human capital|regulation|forward-looking statements|"
    r"technology|operational risk)",
    re.I,
)

# ---------------------------------------------------------------- helpers
session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate"})


def get(url, as_json=False):
    for attempt in range(4):
        time.sleep(PAUSE)
        r = session.get(url, timeout=60)
        if r.status_code == 200:
            return r.json() if as_json else r.text
        if r.status_code in (429, 503):
            time.sleep(2 ** attempt * 2)
            continue
        r.raise_for_status()
    raise RuntimeError(f"Gave up on {url}")


def ticker_to_cik():
    data = get("https://www.sec.gov/files/company_tickers.json", as_json=True)
    return {row["ticker"].upper(): int(row["cik_str"]) for row in data.values()}


def filings_in_window(cik, start, end):
    """10-K/10-Q filings whose period ends between start and end.
    Big banks file thousands of prospectuses, so the 'recent' block may
    hold only ~1 year. Older filings sit in extra pages (filings.files);
    keep reading pages until we are past the start of the window."""
    sub = get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", as_json=True)
    pages = [sub["filings"]["recent"]]
    older = [f["name"] for f in sub["filings"].get("files", [])]
    rows, seen = [], set()

    def collect(rec):
        for i, form in enumerate(rec["form"]):
            acc = rec["accessionNumber"][i]
            if form in FORMS and acc not in seen:
                seen.add(acc)
                rows.append({
                    "form": form,
                    "filing_date": rec["filingDate"][i],
                    "period": rec["reportDate"][i],
                    "accession": acc,
                    "primary_doc": rec["primaryDocument"][i],
                })

    def reached_start():
        return any(r["period"] < start for r in rows)

    collect(pages[0])
    while not reached_start() and older:
        collect(get("https://data.sec.gov/submissions/" + older.pop(0), as_json=True))
    rows = [r for r in rows if start <= r["period"] <= end]
    rows.sort(key=lambda r: r["period"], reverse=True)
    return rows


def exhibit_docs(cik, accession):
    """Return [(filename, type)] of extra exhibits we want from the index page."""
    acc = accession.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{accession}-index.htm"
    soup = BeautifulSoup(get(url), "html.parser")
    out = []
    for tr in soup.select("table.tableFile tr"):
        tds = tr.find_all("td")
        if len(tds) >= 4:
            doc_type = tds[3].get_text(strip=True)
            link = tds[2].find("a")
            if link and doc_type.startswith(EXTRA_EXHIBITS):
                name = link.get_text(strip=True).split()[0]
                if name.lower().endswith((".htm", ".html")):
                    out.append((name, doc_type))
    return out


def html_to_paragraphs(html):
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "ix:header"]):
        t.decompose()
    # Inline-XBRL filings put each paragraph in its own <p>/<div>
    blocks = []
    for el in soup.find_all(["p", "div", "td", "li"]):
        if el.find(["p", "div", "td", "li", "table"]):
            continue  # only leaf-ish blocks, avoid duplicates
        txt = " ".join(el.get_text(" ", strip=True).split())
        if txt:
            blocks.append(txt)
    # merge consecutive tiny fragments (split spans) into paragraphs
    paras, buf = [], ""
    for b in blocks:
        if (len(buf) < 200 and buf and not buf.endswith((".", ":", ";"))
                and not SECTION_RE.match(buf) and not SECTION_RE.match(b)):
            buf += " " + b
        else:
            if buf:
                paras.append(buf)
            buf = b
    if buf:
        paras.append(buf)
    return paras


def ai_hits(text):
    strong = {m.group(0).lower() for m in STRONG_RE.finditer(text)}
    if AI_WORD_RE.search(text):
        strong.add("ai")
    weak = {m.group(0).lower() for m in WEAK_RE.finditer(text)}
    return strong, weak


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data", help="data folder (repo's data/)")
    ap.add_argument("--start", default=START, help="first period end, YYYY-MM-DD")
    ap.add_argument("--end", default=END, help="last period end, YYYY-MM-DD")
    ap.add_argument("--include-weak", action="store_true",
                    help="also keep passages that only say automation/algorithm")
    args = ap.parse_args()

    data = Path(args.data)
    raw_html, raw_text = data / "raw/sec/html", data / "raw/sec/text"
    interim, processed = data / "interim/sec", data / "processed/sec"
    for d in (raw_html, raw_text, interim, processed):
        d.mkdir(parents=True, exist_ok=True)

    print("Looking up company CIKs ...")
    ciks = ticker_to_cik()

    inventory, passages = [], []
    for ticker, name in COMPANIES:
        cik = ciks[ticker]
        print(f"\n{name} ({ticker}, CIK {cik})")
        for f in filings_in_window(cik, args.start, args.end):
            acc = f["accession"].replace("-", "")
            base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/"
            docs = [(f["primary_doc"], f["form"])]
            try:
                docs += exhibit_docs(cik, f["accession"])
            except Exception as e:  # index page missing is not fatal
                print(f"   (couldn't read exhibit index: {e})")

            stem = f"{ticker}_{f['period']}_{f['form']}"
            all_paras, size = [], 0
            for doc_name, doc_type in docs:
                html = get(base + doc_name)
                size += len(html)
                tag = "" if doc_type == f["form"] else "_" + doc_type.replace("-", "")
                (raw_html / f"{stem}{tag}.htm").write_text(html, encoding="utf-8")
                for p in html_to_paragraphs(html):
                    all_paras.append((p, doc_name))

            (raw_text / f"{stem}.txt").write_text(
                "\n\n".join(p for p, _ in all_paras), encoding="utf-8")

            section, n_ai, seen_text = "", 0, set()
            for idx, (p, doc_name) in enumerate(all_paras):
                if len(p) < 160 and SECTION_RE.match(p):
                    section = p[:80]
                strong, weak = ai_hits(p)
                if not strong and not (args.include_weak and weak):
                    continue
                if len(p) < 40:     # table-of-contents crumbs etc.
                    continue
                if p in seen_text:  # same text twice in one filing
                    continue
                seen_text.add(p)
                n_ai += 1
                passages.append({
                    "passage_id": f"{stem}_{idx:05d}",
                    "company": name, "ticker": ticker, "form": f["form"],
                    "period": f["period"], "filing_date": f["filing_date"],
                    "section_guess": section, "matched_terms": "; ".join(sorted(strong | weak)),
                    "strength": "strong" if strong else "weak",
                    "words": len(p.split()), "passage": p,
                    "source_url": base + doc_name,
                })

            inventory.append({
                "company": name, "ticker": ticker, "cik": cik, **f,
                "docs": " | ".join(d for d, _ in docs), "html_bytes": size,
                "paragraphs": len(all_paras), "ai_passages": n_ai,
                "url": base + f["primary_doc"],
            })
            print(f"   {f['form']:5} period {f['period']}  filed {f['filing_date']}"
                  f"  -> {n_ai:3d} AI passages")

    def write_csv(path, rows):
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    write_csv(processed / "filings_inventory.csv", inventory)
    write_csv(interim / "ai_passages.csv", passages)
    (processed / "run_info.json").write_text(json.dumps({
        "run_at": datetime.now().isoformat(timespec="seconds"),
        "filings": len(inventory), "ai_passages": len(passages),
        "user_agent": USER_AGENT, "window": [args.start, args.end],
        "companies": [t for t, _ in COMPANIES],
        "strong_terms": STRONG_TERMS + [AI_WORD], "weak_terms": WEAK_TERMS,
    }, indent=2))
    print(f"\nDone: {len(inventory)} filings, {len(passages)} AI passages -> {data}/")


if __name__ == "__main__":
    main()
