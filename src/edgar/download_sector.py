"""Download the sector firms' 10-Ks, pull their AI passages and their public float (#133, #134).

For every firm in data/processed/sec/sp500_financials/firms.csv (src/edgar/make_firm_list.py):
  1. read SEC's submissions file for its CIK; check the ticker is SEC's, note SEC's name and
     fiscal-year end
  2. pick the filings of --forms whose period ends between --start and --end (default: the
     10-Ks for FY2024 and FY2025, i.e. periods 2024-01-01 to 2025-12-31; FY = year the fiscal
     year ends, the same rule as the scores)
  3. download the primary document, every part of it (stem_d2.htm ...) and Exhibit 13, split it
     into paragraphs and keep the AI paragraphs, with the SAME rules as the first run
     (html_to_paragraphs, ai_hits and ai_passages from download_sec_filings.py), so the passages
     are comparable with the 7-firm data and check 1
  4. read the cover-page public float (dei:EntityPublicFloat) of each of those 10-Ks from SEC's
     free XBRL API, matched by accession number (it feeds the cap-weighted index)

The run is resumable: each filing's paragraphs are kept under data/raw/sec/sp500_financials/
(gitignored), and a rerun reads them instead of downloading again. A problem with one firm or
filing is written to the run log and the run goes on.

Run from the repo root (needs internet and a SEC User-Agent with a contact email, e.g.
SEC_USER_AGENT="CMU 95-891 Team 5 research you@andrew.cmu.edu" in .env):
    python3 -m src.edgar.download_sector                       # all firms, 10-K FY2024-FY2025
    python3 -m src.edgar.download_sector --tickers AFL,V --limit-filings 1   # smoke test
Writes:
    data/interim/sec/sp500_financials/ai_passages.csv          AI paragraphs, verbatim SEC text
    data/processed/sec/sp500_financials/filings_inventory.csv  one row per filing (no text)
    data/processed/sec/sp500_financials/public_float.csv       one row per 10-K
    data/processed/sec/sp500_financials/download_info.json     when, how, and every problem

SEC fair access: one request at a time with a pause (under 10 per second), User-Agent with an
email. Only public EDGAR data is collected.
"""
import argparse
import csv
import json
import os
import re
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

from src.edgar import download_sec_filings as dl

FIRMS = Path("data/processed/sec/sp500_financials/firms.csv")
RAW = Path("data/raw/sec/sp500_financials")
PASSAGES_OUT = Path("data/interim/sec/sp500_financials/ai_passages.csv")
INVENTORY_OUT = Path("data/processed/sec/sp500_financials/filings_inventory.csv")
FLOAT_OUT = Path("data/processed/sec/sp500_financials/public_float.csv")
INFO_OUT = Path("data/processed/sec/sp500_financials/download_info.json")
START, END = "2024-01-01", "2025-12-31"
PASSAGE_FIELDS = ["passage_id", "company", "ticker", "form", "period", "filing_date", "section_guess",
                  "matched_terms", "strength", "words", "passage", "source_url"]
INVENTORY_FIELDS = ["company", "ticker", "cik", "firm_type", "form", "filing_date", "period", "fiscal_year",
                    "accession", "primary_doc", "docs", "html_bytes", "paragraphs", "ai_passages", "url", "status"]
FLOAT_FIELDS = ["ticker", "cik", "fiscal_year", "as_of", "public_float_usd", "form", "filed", "accession", "source"]
ARCHIVES = "https://www.sec.gov/Archives/edgar/data/"
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")


def sec_ticker(t: str) -> str:
    """Our list writes class shares with a dot (BRK.B); SEC writes BRK-B."""
    return t.upper().replace(".", "-")


def list_filings(cik: int, start: str, end: str, forms: set[str]) -> tuple[dict, list[dict]]:
    """SEC's submissions file for one CIK: (metadata, filings of `forms` with period in [start, end]).
    Big filers keep only ~1 year in 'recent'; older filings sit in extra pages, read until past start."""
    sub = dl.get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", as_json=True)
    meta = {"sec_name": sub.get("name", ""), "sec_tickers": sub.get("tickers") or [],
            "fiscal_year_end": sub.get("fiscalYearEnd") or ""}
    pages = [sub["filings"]["recent"]]
    older = [f["name"] for f in sub["filings"].get("files", [])]
    rows, seen = [], set()

    def collect(rec):
        for i, form in enumerate(rec["form"]):
            acc = rec["accessionNumber"][i]
            if form in forms and acc not in seen:
                seen.add(acc)
                rows.append({"form": form, "filing_date": rec["filingDate"][i], "period": rec["reportDate"][i],
                             "accession": acc, "primary_doc": rec["primaryDocument"][i]})

    collect(pages[0])
    while older and not any(r["period"] and r["period"] < start for r in rows):
        collect(dl.get("https://data.sec.gov/submissions/" + older.pop(0), as_json=True))
    rows = [r for r in rows if r["period"] and start <= r["period"] <= end]
    rows.sort(key=lambda r: (r["period"], r["form"]))
    return meta, rows


def filing_docs(cik: int, accession: str, form: str, primary_doc: str) -> list[tuple[str, str]]:
    """Documents to read for one filing: the primary document first, then (in the index page's
    order) Exhibit 13 and any other part of the primary document (stem_d2.htm, or a second
    document typed as the form). Wells Fargo puts its annual report body in such a part."""
    acc = accession.replace("-", "")
    docs = [(primary_doc, form)]
    try:
        soup = dl.BeautifulSoup(dl.get(f"{ARCHIVES}{cik}/{acc}/{accession}-index.htm"), "html.parser")
    except Exception:  # no index page: keep the primary document only
        return docs
    stem = re.sub(r"(_d\d+)?\.html?$", "", primary_doc, flags=re.I)
    part = re.compile("^" + re.escape(stem) + r"(_d\d+)?\.html?$", re.I)
    for tr in soup.select("table.tableFile tr"):
        tds = tr.find_all("td")
        if len(tds) < 4:
            continue
        link = tds[2].find("a")
        if not link:
            continue
        name = link.get_text(strip=True).split()[0]
        doc_type = tds[3].get_text(strip=True)
        if not name.lower().endswith((".htm", ".html")) or any(name == d for d, _ in docs):
            continue
        if doc_type.startswith(dl.EXTRA_EXHIBITS) or doc_type == form or part.match(name):
            docs.append((name, doc_type))
    return docs


def read_filing(firm: dict, f: dict, raw_dir: Path, keep_html: bool) -> dict:
    """Paragraphs of one filing, from the local copy if a previous run saved it."""
    stem = f"{firm['ticker']}_{f['period']}_{f['form']}"
    local = raw_dir / firm["ticker"] / f"{stem}.json"
    if local.exists():
        saved = json.loads(local.read_text(encoding="utf-8"))
        if saved.get("accession") == f["accession"]:
            return saved | {"from_cache": True}
    cik = int(firm["cik"])
    base = f"{ARCHIVES}{cik}/{f['accession'].replace('-', '')}/"
    docs = filing_docs(cik, f["accession"], f["form"], f["primary_doc"])
    paras, size = [], 0
    for doc_name, doc_type in docs:
        html = dl.get(base + doc_name)
        size += len(html)
        if keep_html:
            (raw_dir / firm["ticker"]).mkdir(parents=True, exist_ok=True)
            (raw_dir / firm["ticker"] / f"{stem}__{doc_name}").write_text(html, encoding="utf-8")
        paras += [[p, doc_name] for p in dl.html_to_paragraphs(html)]
    saved = {"accession": f["accession"], "base": base, "docs": [d for d, _ in docs], "html_bytes": size,
             "paragraphs": paras}
    local.parent.mkdir(parents=True, exist_ok=True)
    tmp = local.with_suffix(".tmp")
    tmp.write_text(json.dumps(saved, ensure_ascii=False), encoding="utf-8")
    tmp.replace(local)
    return saved | {"from_cache": False}


def public_floats(cik: int, tenks: list[dict]) -> tuple[list[dict], list[str]]:
    """Cover-page public float for each of our 10-Ks, matched by accession number."""
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/dei/EntityPublicFloat.json"
    facts = dl.get(url, as_json=True).get("units", {}).get("USD", [])
    rows, problems = [], []
    for f in tenks:
        hits = [x for x in facts if x.get("accn") == f["accession"]]
        values = sorted({x["val"] for x in hits})
        if not hits:
            problems.append(f"{f['period']} 10-K {f['accession']}: no public float tagged")
            continue
        if len(values) > 1:
            problems.append(f"{f['period']} 10-K: {len(values)} different public floats {values}; kept the largest")
        best = max(hits, key=lambda x: (x["val"], x.get("end", "")))
        rows.append({"cik": f"{cik:010d}", "fiscal_year": f["period"][:4], "as_of": best.get("end", ""),
                     "public_float_usd": int(best["val"]), "form": best.get("form", ""), "filed": best.get("filed", ""),
                     "accession": f["accession"], "source": url})
    return rows, problems


def _plain_console() -> None:
    """Never crash on a character the console can't show (Windows, output to a file)."""
    try:
        import sys
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass


def read_csv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main(argv=None) -> int:
    _plain_console()
    ap = argparse.ArgumentParser(description="Download the sector firms' 10-Ks, AI passages and public float.")
    ap.add_argument("--firms", default=str(FIRMS), help="firm list CSV (make_firm_list.py)")
    ap.add_argument("--tickers", help="only these tickers, comma-separated (default: all in the list)")
    ap.add_argument("--forms", default="10-K", help="10-K (default; Julie, Nov 10) or 10-K,10-Q")
    ap.add_argument("--start", default=START, help="first period end, YYYY-MM-DD")
    ap.add_argument("--end", default=END, help="last period end, YYYY-MM-DD")
    ap.add_argument("--limit-filings", type=int, help="at most N filings per firm (smoke test)")
    ap.add_argument("--keep-html", action="store_true", help="also save the raw HTML (several GB)")
    ap.add_argument("--raw-dir", default=str(RAW))
    ap.add_argument("--passages-out", default=str(PASSAGES_OUT))
    ap.add_argument("--inventory-out", default=str(INVENTORY_OUT))
    ap.add_argument("--float-out", default=str(FLOAT_OUT))
    ap.add_argument("--info-out", default=str(INFO_OUT))
    a = ap.parse_args(argv)

    try:  # SEC_USER_AGENT from .env, same as the agent's live EDGAR tool
        from src.agent import config as agent_config
        agent_config.load_dotenv()
    except Exception:
        pass
    ua = os.environ.get("SEC_USER_AGENT") or dl.USER_AGENT
    dl.session.headers["User-Agent"] = ua
    forms = {x.strip().upper() for x in a.forms.split(",") if x.strip()}
    firms = read_csv(Path(a.firms))
    if a.tickers:
        want = {t.strip().upper() for t in a.tickers.split(",")}
        firms = [f for f in firms if f["ticker"].upper() in want]
    raw_dir = Path(a.raw_dir)
    t0 = time.monotonic()
    print(f"{len(firms)} firms, forms {sorted(forms)}, periods {a.start} to {a.end}")

    passages, inventory, floats, problems, firm_meta = [], [], [], [], {}
    for n, firm in enumerate(firms, 1):
        t, cik = firm["ticker"], int(firm["cik"])
        try:
            meta, filings = list_filings(cik, a.start, a.end, forms)
        except Exception as e:
            problems.append({"ticker": t, "where": "submissions", "problem": str(e)[:300]})
            print(f"[{n}/{len(firms)}] {t}: ERROR could not read SEC submissions ({e})")
            continue
        firm_meta[t] = meta
        if sec_ticker(t) not in {x.upper() for x in meta["sec_tickers"]}:
            problems.append({"ticker": t, "where": "ticker check",
                             "problem": f"CIK {cik} is '{meta['sec_name']}' with tickers {meta['sec_tickers']}"})
        if a.limit_filings:
            filings = filings[-a.limit_filings:]
        years = Counter((f["form"], f["period"][:4]) for f in filings)
        for (form, fy), k in years.items():
            if k > 1:
                problems.append({"ticker": t, "where": "fiscal year", "problem": f"{k} {form}s with periods in {fy}"})
        if "10-K" in forms:
            have = {f["period"][:4] for f in filings if f["form"] == "10-K"}
            for fy in range(int(a.start[:4]), int(a.end[:4]) + 1):
                if str(fy) not in have and not a.limit_filings:
                    problems.append({"ticker": t, "where": "10-K", "problem": f"no 10-K with a period in {fy}"})
        line = []
        for f in filings:
            stem = f"{t}_{f['period']}_{f['form']}"
            row = {"company": firm["company"], "ticker": t, "cik": firm["cik"], "firm_type": firm["firm_type"],
                   **f, "fiscal_year": f["period"][:4], "url": f"{ARCHIVES}{cik}/{f['accession'].replace('-', '')}/{f['primary_doc']}"}
            try:
                got = read_filing(firm, f, raw_dir, a.keep_html)
            except Exception as e:
                problems.append({"ticker": t, "where": f"{f['form']} {f['period']}", "problem": str(e)[:300]})
                inventory.append(row | {"status": f"error: {str(e)[:120]}"})
                line.append(f"{f['form']} {f['period']} ERROR")
                continue
            found = dl.ai_passages([tuple(p) for p in got["paragraphs"]], stem, firm["company"], t, f["form"],
                                   f["period"], f["filing_date"], got["base"])
            passages += found
            inventory.append(row | {"docs": " | ".join(got["docs"]), "html_bytes": got["html_bytes"],
                                    "paragraphs": len(got["paragraphs"]), "ai_passages": len(found),
                                    "status": "ok (saved copy)" if got["from_cache"] else "ok"})
            line.append(f"{f['form']} {f['period']}: {len(found)}")
        tenks = [f for f in filings if f["form"] == "10-K"]
        if tenks:
            try:
                fl, pf = public_floats(cik, tenks)
                floats += [r | {"ticker": t} for r in fl]
                problems += [{"ticker": t, "where": "public float", "problem": p} for p in pf]
            except Exception as e:
                problems.append({"ticker": t, "where": "public float", "problem": str(e)[:300]})
        print(f"[{n}/{len(firms)}] {t:6} {'; '.join(line) or 'no filings in the window'}")

    write_csv(Path(a.passages_out), passages, PASSAGE_FIELDS)
    write_csv(Path(a.inventory_out), inventory, INVENTORY_FIELDS)
    write_csv(Path(a.float_out), floats, FLOAT_FIELDS)
    off_calendar = {t: m["fiscal_year_end"] for t, m in firm_meta.items() if m["fiscal_year_end"] not in ("", "1231")}
    info = {"run_at": datetime.now().isoformat(timespec="seconds"), "wall_seconds": round(time.monotonic() - t0, 1),
            "firms_file": a.firms, "firms": len(firms), "forms": sorted(forms), "window": [a.start, a.end],
            "filings": len(inventory), "filings_ok": sum(r["status"].startswith("ok") for r in inventory),
            "ai_passages": len(passages), "public_floats": len(floats),
            "user_agent": EMAIL_RE.sub("<email>", ua),
            "search_rules": "download_sec_filings.py: html_to_paragraphs, ai_hits (strong terms only), ai_passages",
            "fiscal_year_rule": "year of the period end; firms whose fiscal year doesn't end in December are listed",
            "fiscal_year_end_not_december": off_calendar,
            "problems": problems}
    Path(a.info_out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.info_out).write_text(json.dumps(info, indent=2), encoding="utf-8")

    print(f"\n{info['filings_ok']}/{len(inventory)} filings read, {len(passages)} AI passages, "
          f"{len(floats)} public floats, {len(problems)} problems, {info['wall_seconds']} s")
    for p in problems:
        print(f"  ! {p['ticker']} [{p['where']}] {p['problem']}")
    print(f"-> {a.passages_out}\n-> {a.inventory_out}\n-> {a.float_out}\n-> {a.info_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
