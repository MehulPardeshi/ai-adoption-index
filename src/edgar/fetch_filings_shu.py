"""
fetch_filings.py — download 10-K / 10-Q primary documents from SEC EDGAR
for the AI Adoption Index proof of concept (Team 5, CMU 95-891).

Usage:
    python fetch_filings.py --out raw_filings --since 2024-01-01
    python fetch_filings.py --out raw_filings --manifest filings_manifest.csv   # re-download exactly the listed filings

What it does
  1. Pulls each firm's submissions index from data.sec.gov (all pages, not just "recent").
  2. Keeps 10-K and 10-Q filed on/after --since.
  3. For each filing, reads the accession folder's index.json and downloads EVERY
     primary-document part: <stem>.htm plus <stem>_d2.htm, _d3.htm ...
     (Wells Fargo splits its 10-K this way; a parser that takes only the first
     file misses the whole annual report body.)
  4. Writes raw HTML to  <out>/<TICKER>/<accession>/<file>.htm
     and a manifest CSV with filing date, period, accession and local paths.

Raw filings are NOT committed to the team repo (see ethics memo); only the
manifest and derived passages are.

SEC fair-access rules: identify yourself in the User-Agent and stay under
10 requests/second. https://www.sec.gov/os/accessing-edgar-data
"""
import argparse, csv, json, os, re, time
from pathlib import Path
import requests

FIRMS = {  # ticker: CIK (10 digits)
    "JPM": "0000019617",
    "BAC": "0000070858",
    "COF": "0000927628",
    "WFC": "0000072971",
    "SCHW": "0000316709",
    "PFG": "0001126328",
}
UA = os.environ.get("SEC_USER_AGENT", "CMU 95-891 Team 5 research shup@andrew.cmu.edu")
HEADERS = {"User-Agent": UA, "Accept-Encoding": "gzip, deflate"}
SLEEP = 0.15  # seconds between requests (~6-7 req/s)


def get(url, **kw):
    time.sleep(SLEEP)
    r = requests.get(url, headers=HEADERS, timeout=60, **kw)
    r.raise_for_status()
    return r


def list_filings(cik, since):
    """Yield dicts for every 10-K/10-Q filed on/after `since` (walks all submission pages)."""
    base = "https://data.sec.gov/submissions/"
    j = get(base + f"CIK{cik}.json").json()
    pages = [j["filings"]["recent"]]
    for p in j["filings"].get("files", []):
        if p["filingTo"] >= since:
            pages.append(get(base + p["name"]).json())
    for f in pages:
        for i in range(len(f["form"])):
            if f["form"][i] in ("10-K", "10-Q") and f["filingDate"][i] >= since:
                yield {
                    "form": f["form"][i],
                    "filed": f["filingDate"][i],
                    "period": f["reportDate"][i],
                    "accession": f["accessionNumber"][i],
                    "primary_doc": f["primaryDocument"][i],
                }


def primary_parts(cik, accession, primary_doc):
    """All parts of the primary document: stem.htm, stem_d2.htm, ... (sorted)."""
    folder = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/"
    idx = get(folder + "index.json").json()
    stem = re.sub(r"_d\d+$", "", re.sub(r"\.htm$", "", primary_doc, flags=re.I), flags=re.I)
    pat = re.compile("^" + re.escape(stem) + r"(_d\d+)?\.htm$", re.I)
    names = sorted(x["name"] for x in idx["directory"]["item"] if pat.match(x["name"]))
    return folder, names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="raw_filings")
    ap.add_argument("--since", default="2024-01-01")
    ap.add_argument("--manifest", help="existing filings_manifest.csv to re-download instead of querying EDGAR")
    ap.add_argument("--tickers", default=",".join(FIRMS))
    a = ap.parse_args()

    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    tickers = [t.strip().upper() for t in a.tickers.split(",")]

    rows = []
    if a.manifest:
        with open(a.manifest, newline="") as fh:
            for r in csv.DictReader(fh):
                if r["ticker"] in tickers:
                    rows.append({"ticker": r["ticker"], "cik": r["cik"], "form": r["form"], "filed": r["filed"],
                                 "period": r["period"], "accession": r["accession"], "primary_doc": r["primary_doc"]})
    else:
        for t in tickers:
            for f in list_filings(FIRMS[t], a.since):
                rows.append({"ticker": t, "cik": FIRMS[t], **f})
    rows.sort(key=lambda r: (r["ticker"], r["filed"]))
    print(f"{len(rows)} filings to fetch")

    manifest = []
    for r in rows:
        folder, names = primary_parts(r["cik"], r["accession"], r["primary_doc"])
        dest = out / r["ticker"] / r["accession"]
        dest.mkdir(parents=True, exist_ok=True)
        local = []
        for n in names:
            p = dest / n
            if not p.exists():
                p.write_bytes(get(folder + n).content)
            local.append(str(p))
        manifest.append({**r, "docs": "|".join(names), "local_paths": "|".join(local), "url": folder + r["primary_doc"]})
        print(f"{r['ticker']} {r['form']} {r['period']}  {len(names)} part(s)")

    with open(out / "download_manifest.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(manifest[0].keys()))
        w.writeheader(); w.writerows(manifest)
    print("manifest written to", out / "download_manifest.csv")


if __name__ == "__main__":
    main()
