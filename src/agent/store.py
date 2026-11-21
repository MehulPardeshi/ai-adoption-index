"""Read-only access to the team's data files. The unit everywhere is one passage (passage_id);
scores are per company (ticker) per fiscal year (first four characters of the filing period)."""
import csv
from functools import lru_cache
from pathlib import Path

from src.agent import config


def fiscal_year(period: str) -> int:
    """FY = year of the period end. Right for every 10-K and for firms whose year ends in December;
    for the 10-Qs of other firms (e.g. Visa, September) use row_fiscal_year."""
    return int(str(period)[:4])


def row_fiscal_year(row: dict) -> int:
    """A filing's, passage's or label's fiscal year: its fiscal_year column when it has one (the sector
    downloader writes it, so Visa's quarter to Dec 31, 2024 is FY2025, #157), else the period's year."""
    return int(row.get("fiscal_year") or fiscal_year(row["period"]))


def read_csv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def passages(path: str | None = None) -> tuple[dict, ...]:
    """The passage store: config.PASSAGES unless a path is given. run_batch --passages points
    config.PASSAGES at another file (e.g. the S&P 500 Financials run); it is read at call time."""
    return _load(str(path or config.PASSAGES))


def passage_index(path: str | None = None) -> dict[str, dict]:
    return _index(str(path or config.PASSAGES))


@lru_cache(maxsize=4)
def _load(path: str) -> tuple[dict, ...]:
    return tuple(read_csv(Path(path)))


@lru_cache(maxsize=4)
def _index(path: str) -> dict[str, dict]:
    return {r["passage_id"]: r for r in _load(path)}


def get_passage(passage_id: str) -> dict | None:
    return passage_index().get(passage_id)


def ticker_of(passage_id: str) -> str:
    """passage_id is <TICKER>_<period>_<form>_<idx>, e.g. JPM_2025-12-31_10-K_00500."""
    return passage_id.split("_", 1)[0]


def select_passages(tickers=None, fiscal_years=None, forms=None, ids=None) -> list[dict]:
    """Filter the passage store. Every argument is optional; None means 'all'."""
    tickers = {t.upper() for t in tickers} if tickers else None
    years = {int(y) for y in fiscal_years} if fiscal_years else None
    forms = {f.upper() for f in forms} if forms else None
    ids = set(ids) if ids else None
    out = []
    for r in passages():
        if tickers and r["ticker"].upper() not in tickers:
            continue
        if years and row_fiscal_year(r) not in years:
            continue
        if forms and r["form"].upper() not in forms:
            continue
        if ids and r["passage_id"] not in ids:
            continue
        out.append(r)
    return out
