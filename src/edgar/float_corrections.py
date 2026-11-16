"""Hand corrections to the public float, and a plausibility check (#134, cap-weighted index).

The public float comes from the cover-page tag dei:EntityPublicFloat in each 10-K
(download_sector.py). Two things can go wrong, both seen in the S&P 500 Financials run:
  * the tag is missing although the cover page states the number (S&P Global, FY2024)
  * the filer typed the wrong number (Ares, FY2025: about $327 million, a year after $25.5 billion)

Corrections live in data/processed/sec/sp500_financials/public_float_corrections.csv, one row per
firm-year with its source and a note: action "correct" replaces (or adds) the value, action "keep"
records that a flagged value was checked against the cover page and is right. download_sector.py
applies the file every time it writes public_float.csv, so a rerun never drops a correction.

check() flags a float that moved by more than x2.5 (or fell below 40%) from one year to the next,
or is under $1 billion (every S&P 500 member is far above that). A flag means: read the cover page.

Apply the corrections to the current file without downloading anything:
    python3 -m src.edgar.float_corrections
"""
import argparse
import csv
from pathlib import Path

DIR = Path("data/processed/sec/sp500_financials")
FLOATS = DIR / "public_float.csv"
CORRECTIONS = DIR / "public_float_corrections.csv"
INVENTORY = DIR / "filings_inventory.csv"
FLOAT_FIELDS = ["ticker", "cik", "fiscal_year", "as_of", "public_float_usd", "form", "filed", "accession", "source"]
MIN_FLOAT = 1e9
JUMP = (0.4, 2.5)


def read(path: Path) -> list[dict]:
    if not Path(path).exists():
        return []
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def apply(floats: list[dict], corrections: list[dict], inventory: list[dict]) -> tuple[list[dict], list[str]]:
    """floats with each correction applied (replaced or added); returns (rows, what was done)."""
    tenk = {(r["ticker"], r["fiscal_year"]): r for r in inventory if r["form"] == "10-K"}
    rows = {(r["ticker"], r["fiscal_year"]): dict(r) for r in floats}
    done = []
    for c in corrections:
        if c.get("action", "correct") != "correct":
            continue
        key = (c["ticker"], c["fiscal_year"])
        if key not in rows and key not in tenk:
            continue  # not in this run (e.g. a --tickers subset)
        old = rows.get(key)
        filing = tenk.get(key, {})
        new = {"ticker": c["ticker"], "cik": (old or filing).get("cik", ""), "fiscal_year": c["fiscal_year"],
               "as_of": c["as_of"], "public_float_usd": int(float(c["public_float_usd"])), "form": "10-K",
               "filed": (old or {}).get("filed") or filing.get("filing_date", ""),
               "accession": c.get("accession") or (old or filing).get("accession", ""),
               "source": f"correction: {c['source']}"}
        if old and str(old.get("public_float_usd")) == str(new["public_float_usd"]) and old.get("source") == new["source"]:
            continue  # already applied
        rows[key] = new
        was = f"tag {int(float(old['public_float_usd'])):,}" if old and not old.get("source", "").startswith("correction") \
            else ("not tagged" if not old else "earlier correction")
        done.append(f"{c['ticker']} FY{c['fiscal_year']}: {was} -> {new['public_float_usd']:,} ({c['source']})")
    out = sorted(rows.values(), key=lambda r: (r["ticker"], r["fiscal_year"]))
    return out, done


def check(floats: list[dict], corrections: list[dict] = ()) -> list[str]:
    """Floats worth a look at the cover page: tiny, or a big jump from the year before.
    Firm-years marked "keep" (checked) or corrected in the corrections file are not flagged again."""
    done = {(c["ticker"], c["fiscal_year"]) for c in corrections}
    by = {}
    for r in floats:
        by.setdefault(r["ticker"], {})[r["fiscal_year"]] = float(r["public_float_usd"])
    out = []
    for t, years in sorted(by.items()):
        for fy, v in sorted(years.items()):
            if (t, fy) in done:
                continue
            if v < MIN_FLOAT:
                out.append(f"{t} FY{fy}: public float ${v / 1e9:.2f}B, under $1B")
            prev = years.get(str(int(fy) - 1))
            if prev and not (JUMP[0] <= v / prev <= JUMP[1]):
                out.append(f"{t} FY{fy}: public float ${v / 1e9:.1f}B vs ${prev / 1e9:.1f}B the year before")
    return out


def write(path: Path, rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FLOAT_FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Apply the public-float corrections to public_float.csv (offline).")
    ap.add_argument("--floats", default=str(FLOATS))
    ap.add_argument("--corrections", default=str(CORRECTIONS))
    ap.add_argument("--inventory", default=str(INVENTORY))
    a = ap.parse_args(argv)
    corrections = read(Path(a.corrections))
    rows, done = apply(read(Path(a.floats)), corrections, read(Path(a.inventory)))
    write(Path(a.floats), rows)
    print(f"{len(done)} correction(s) applied -> {a.floats}")
    for d in done:
        print("  " + d)
    flags = check(rows, corrections)
    print(f"{len(flags)} float(s) to check" + (":" if flags else "."))
    for f in flags:
        print("  ! " + f)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
