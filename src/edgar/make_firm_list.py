"""Build the firm list for the sector index: the S&P 500 Financials (#133, #134).

S&P's official constituent file is licensed, so we use a free public copy and record which
snapshot we used. The default source is the `datasets/s-and-p-500-companies` table on GitHub
(public domain, ODC-PDDL), which is rebuilt from Wikipedia's "List of S&P 500 companies" and
already carries each firm's GICS sub-industry and SEC CIK. Membership changes a few times a
year, so refresh the list before each yearly run and keep the date.

Each firm also gets a `firm_type`, the five groups we validate separately (Nov 10 plan: banks
are checked; pilot the other four before trusting their scores):

    bank                       Diversified Banks, Regional Banks
    insurer                    P&C, Life & Health, Multi-line, Reinsurance, Insurance Brokers,
                               Multi-Sector Holdings (Berkshire Hathaway, mostly insurance)
    asset_mgmt_broker          Asset Management & Custody Banks, Investment Banking & Brokerage
    payments_consumer_finance  Transaction & Payment Processing Services, Consumer Finance
    exchange_data              Financial Exchanges & Data

The seven proof-of-concept firms keep the company names of the first run, so their passages
build the same model prompt (and reuse the cached labels).

Run from the repo root:
    python3 -m src.edgar.make_firm_list                           # downloads the current table
    python3 -m src.edgar.make_firm_list --source constituents.csv --source-date 2026-11-05
Writes data/processed/sec/sp500_financials/firms.csv.
"""
import argparse
import csv
import io
from datetime import date
from pathlib import Path

SOURCE_URL = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv"
OUT = Path("data/processed/sec/sp500_financials/firms.csv")
FIELDS = ["ticker", "company", "cik", "gics_sub_industry", "firm_type", "poc_firm", "date_added",
          "source", "source_date"]

FIRM_TYPE = {
    "Diversified Banks": "bank",
    "Regional Banks": "bank",
    "Property & Casualty Insurance": "insurer",
    "Life & Health Insurance": "insurer",
    "Multi-line Insurance": "insurer",
    "Reinsurance": "insurer",
    "Insurance Brokers": "insurer",
    "Multi-Sector Holdings": "insurer",
    "Asset Management & Custody Banks": "asset_mgmt_broker",
    "Investment Banking & Brokerage": "asset_mgmt_broker",
    "Transaction & Payment Processing Services": "payments_consumer_finance",
    "Consumer Finance": "payments_consumer_finance",
    "Financial Exchanges & Data": "exchange_data",
}
# Names used in the first run (src/edgar/download_sec_filings.py); same name -> same prompt.
POC_NAMES = {"JPM": "JPMorgan Chase", "BAC": "Bank of America", "COF": "Capital One", "WFC": "Wells Fargo",
             "SCHW": "Charles Schwab", "PFG": "Principal Financial Group", "C": "Citigroup"}


def clean_name(name: str) -> str:
    """'Hartford (The)' -> 'The Hartford' (Wikipedia's sort form)."""
    name = " ".join(name.split())
    if name.endswith(" (The)"):
        name = "The " + name[: -len(" (The)")]
    return name


def build(rows: list[dict], source: str, source_date: str) -> list[dict]:
    out = []
    for r in rows:
        if r.get("GICS Sector", "").strip() != "Financials":
            continue
        ticker = r["Symbol"].strip().upper()
        sub = r["GICS Sub-Industry"].strip()
        out.append({
            "ticker": ticker,
            "company": POC_NAMES.get(ticker, clean_name(r["Security"])),
            "cik": f"{int(r['CIK']):010d}",
            "gics_sub_industry": sub,
            "firm_type": FIRM_TYPE.get(sub, "other"),
            "poc_firm": "yes" if ticker in POC_NAMES else "",
            "date_added": r.get("Date added", "").strip(),
            "source": source,
            "source_date": source_date,
        })
    out.sort(key=lambda r: r["ticker"])
    return out


def read_source(src: str) -> list[dict]:
    if src.startswith(("http://", "https://")):
        import requests
        r = requests.get(src, timeout=60, headers={"User-Agent": "CMU 95-891 Team 5 research"})
        r.raise_for_status()
        return list(csv.DictReader(io.StringIO(r.text)))
    with open(src, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build the S&P 500 Financials firm list.")
    ap.add_argument("--source", default=SOURCE_URL, help="constituents CSV: URL or local path")
    ap.add_argument("--source-date", default=None, help="date of the snapshot (default: today)")
    ap.add_argument("--source-label", default=None, help="how to cite the source in the file")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args(argv)

    label = a.source_label or ("github.com/datasets/s-and-p-500-companies (from Wikipedia)"
                               if a.source == SOURCE_URL else a.source)
    firms = build(read_source(a.source), label, a.source_date or date.today().isoformat())
    if not firms:
        print("No Financials rows found; is this the right file?")
        return 1
    other = [f["ticker"] for f in firms if f["firm_type"] == "other"]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(firms)
    counts = {}
    for f in firms:
        counts[f["firm_type"]] = counts.get(f["firm_type"], 0) + 1
    print(f"{len(firms)} Financials firms -> {out}")
    print("  " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    if other:
        print(f"  ! unknown GICS sub-industry, typed 'other': {', '.join(other)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
