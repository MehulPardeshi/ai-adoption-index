"""Validated readers for consensus company scores and the sector index."""

import csv
from dataclasses import dataclass
import math
from pathlib import Path
from typing import Mapping, Sequence

from src.nlp.taxonomy_v0 import ALL_SCENARIOS


SCORES_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "processed"
    / "sec"
    / "company_scores_consensus.csv"
)

SECTOR_INDEX_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "processed"
    / "sec"
    / "sector_index.csv"
)

SCORE_COLUMNS = (
    "company",
    "ticker",
    "fiscal_year",
    "ai_use_score",
    "scenarios_with_use",
    "readiness_score",
    "talk_ratio_pct",
    "substantive_ai_passages",
)

SECTOR_INDEX_COLUMNS = (
    "fiscal_year",
    "n_firms",
    "ai_ew",
    "ai_cw",
    "total_public_float_usd",
    "firms",
)

FIRM_LABELS = {
    "JPM": "JPMorgan Chase",
    "BAC": "Bank of America",
    "COF": "Capital One",
    "WFC": "Wells Fargo",
    "C": "Citigroup",
    "SCHW": "Charles Schwab",
    "PFG": "Principal Financial Group",
}

SECTOR_FIRM_TICKERS = frozenset({"JPM", "BAC", "COF", "WFC", "SCHW", "PFG"})

PARTIAL_FISCAL_YEARS = frozenset({2026})

SCORE_METRIC_HELP = {
    "AI Use Score": (
        "A 0–100 disclosure score: for each use-case scenario, strongest "
        "specific deployed (D2), general deployed (D1), or planned (P) evidence is weighted "
        "3, 1, or 0.5; enterprise-wide (ENT) evidence can count once. The total is scaled "
        "by 33 and capped at 100. It measures scored disclosures, not verified firm-wide adoption. "
        "The current score file combines human-agreed labels for 80 of 277 passages with AI-draft labels."
    ),
    "Readiness Score": (
        "A 0–100 disclosure score for AI governance, talent, and investment "
        "enablers, using the same 3/1/0.5 weights for D2, D1, and P evidence and scaling "
        "the total by 9. "
        "It is not a comprehensive assessment of organizational readiness. The current score "
        "file combines human-agreed labels for 80 of 277 passages with AI-draft labels."
    ),
    "Talk Ratio (%)": (
        "The percentage of substantive AI passages labeled N (no evidence of the firm's own "
        "AI use, such as risk or regulation discussion) among all substantive AI passages "
        "(all labels except X, which is not substantive). A higher value means more passages "
        "lack evidence of the firm's own use; it does not measure total AI discussion volume."
    ),
}


@dataclass(frozen=True)
class CompanyYearScore:
    company: str
    ticker: str
    fiscal_year: int
    ai_use_score: int
    scenarios_with_use: tuple[str, ...]
    readiness_score: int
    talk_ratio_pct: int | None
    substantive_ai_passages: int


@dataclass(frozen=True)
class SectorYearIndex:
    fiscal_year: int
    n_firms: int
    ai_ew: float
    ai_cw: float
    total_public_float_usd: int
    firms: tuple[str, ...]


def _required_text(row: Mapping[str, str | None], column: str, line: int) -> str:
    value = row.get(column)
    if value is None or not value.strip():
        raise ValueError(f"line {line}: {column} must not be blank")
    return value.strip()


def _integer(
    row: Mapping[str, str | None],
    column: str,
    line: int,
    *,
    minimum: int,
    maximum: int | None = None,
) -> int:
    value = row.get(column)
    if value is None or not value.strip():
        raise ValueError(f"line {line}: {column} must not be blank")
    try:
        parsed = int(value)
    except ValueError as exc:
        raise ValueError(f"line {line}: {column} must be an integer") from exc
    if parsed < minimum or (maximum is not None and parsed > maximum):
        bounds = f"{minimum} or greater"
        if maximum is not None:
            bounds = f"between {minimum} and {maximum}"
        raise ValueError(f"line {line}: {column} must be {bounds}")
    return parsed


def _float(
    row: Mapping[str, str | None],
    column: str,
    line: int,
    *,
    minimum: float,
    maximum: float | None = None,
) -> float:
    value = row.get(column)
    if value is None or not value.strip():
        raise ValueError(f"line {line}: {column} must not be blank")
    try:
        parsed = float(value)
    except ValueError as exc:
        raise ValueError(f"line {line}: {column} must be a number") from exc
    if not math.isfinite(parsed):
        raise ValueError(f"line {line}: {column} must be finite")
    if parsed < minimum or (maximum is not None and parsed > maximum):
        bounds = f"{minimum} or greater"
        if maximum is not None:
            bounds = f"between {minimum} and {maximum}"
        raise ValueError(f"line {line}: {column} must be {bounds}")
    return parsed


def _optional_integer(
    row: Mapping[str, str | None],
    column: str,
    line: int,
    *,
    minimum: int,
    maximum: int | None = None,
) -> int | None:
    value = row.get(column)
    if value is None or not value.strip():
        return None
    return _integer(
        row,
        column,
        line,
        minimum=minimum,
        maximum=maximum,
    )


def complete_fiscal_year_scores(
    scores: Sequence[CompanyYearScore],
) -> tuple[CompanyYearScore, ...]:
    """Keep only score rows for fiscal years known to be complete in this pilot."""
    return tuple(
        score for score in scores if score.fiscal_year not in PARTIAL_FISCAL_YEARS
    )


def complete_sector_index_years(
    rows: Sequence[SectorYearIndex],
) -> tuple[SectorYearIndex, ...]:
    """Keep only sector index rows for fiscal years known to be complete."""
    return tuple(
        row for row in rows if row.fiscal_year not in PARTIAL_FISCAL_YEARS
    )


def format_scenario_code(code: str) -> str:
    """Return a scenario code with its frozen codebook label."""
    try:
        description = ALL_SCENARIOS[code]
    except KeyError as exc:
        raise ValueError(f"unknown taxonomy scenario code {code!r}") from exc
    return f"{code} — {description}"


def load_company_scores(path: Path = SCORES_FILE) -> tuple[CompanyYearScore, ...]:
    """Load consensus annual scores; never fills missing company-years with zero."""
    with path.open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None:
            raise ValueError("score CSV is missing its header row")
        missing_columns = set(SCORE_COLUMNS) - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(
                f"score CSV is missing required columns: {', '.join(sorted(missing_columns))}"
            )

        scores = []
        seen_keys = set()
        for line, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"line {line}: row contains more values than the header")

            company = _required_text(row, "company", line)
            ticker = _required_text(row, "ticker", line)
            fiscal_year = _integer(row, "fiscal_year", line, minimum=1900)
            ai_use_score = _integer(row, "ai_use_score", line, minimum=0, maximum=100)
            readiness_score = _integer(
                row, "readiness_score", line, minimum=0, maximum=100
            )
            talk_ratio_pct = _optional_integer(
                row,
                "talk_ratio_pct",
                line,
                minimum=0,
                maximum=100,
            )
            substantive_ai_passages = _integer(
                row, "substantive_ai_passages", line, minimum=0
            )
            key = (ticker, fiscal_year)
            if key in seen_keys:
                raise ValueError(
                    f"line {line}: duplicate score row for {ticker} {fiscal_year}"
                )
            seen_keys.add(key)

            scenarios = _required_text(row, "scenarios_with_use", line) if row.get(
                "scenarios_with_use"
            ) else ""
            scenario_codes = tuple(scenarios.split())
            unknown_codes = sorted(set(scenario_codes) - set(ALL_SCENARIOS))
            if unknown_codes:
                raise ValueError(
                    f"line {line}: unknown taxonomy scenario code(s): "
                    f"{', '.join(unknown_codes)}"
                )
            scores.append(
                CompanyYearScore(
                    company=company,
                    ticker=ticker,
                    fiscal_year=fiscal_year,
                    ai_use_score=ai_use_score,
                    scenarios_with_use=scenario_codes,
                    readiness_score=readiness_score,
                    talk_ratio_pct=talk_ratio_pct,
                    substantive_ai_passages=substantive_ai_passages,
                )
            )

    if not scores:
        raise ValueError("score CSV contains no company-year rows")
    return tuple(sorted(scores, key=lambda score: (score.ticker, score.fiscal_year)))


def load_sector_index(path: Path = SECTOR_INDEX_FILE) -> tuple[SectorYearIndex, ...]:
    """Load and validate the equal- and cap-weighted sector index."""
    with path.open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None:
            raise ValueError("sector index CSV is missing its header row")
        missing_columns = set(SECTOR_INDEX_COLUMNS) - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(
                "sector index CSV is missing required columns: "
                f"{', '.join(sorted(missing_columns))}"
            )

        rows = []
        seen_years = set()
        for line, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(
                    f"line {line}: row contains more values than the header"
                )

            fiscal_year = _integer(row, "fiscal_year", line, minimum=1900)
            if fiscal_year in seen_years:
                raise ValueError(
                    f"line {line}: duplicate sector index row for {fiscal_year}"
                )
            seen_years.add(fiscal_year)

            n_firms = _integer(row, "n_firms", line, minimum=1)
            firms = tuple(_required_text(row, "firms", line).split())
            if len(firms) != n_firms or len(set(firms)) != n_firms:
                raise ValueError(
                    f"line {line}: firms must contain {n_firms} unique ticker(s)"
                )
            non_core_firms = sorted(set(firms) - SECTOR_FIRM_TICKERS)
            if non_core_firms:
                raise ValueError(
                    f"line {line}: sector index includes non-core ticker(s): "
                    f"{', '.join(non_core_firms)}"
                )
            rows.append(
                SectorYearIndex(
                    fiscal_year=fiscal_year,
                    n_firms=n_firms,
                    ai_ew=_float(row, "ai_ew", line, minimum=0, maximum=100),
                    ai_cw=_float(row, "ai_cw", line, minimum=0, maximum=100),
                    total_public_float_usd=_integer(
                        row, "total_public_float_usd", line, minimum=1
                    ),
                    firms=firms,
                )
            )

    if not rows:
        raise ValueError("sector index CSV contains no fiscal-year rows")
    return tuple(sorted(rows, key=lambda row: row.fiscal_year))


def validate_firm_labels(
    scores: Sequence[CompanyYearScore],
    firm_labels: Mapping[str, str] = FIRM_LABELS,
) -> None:
    """Ensure every score ticker maps to the dashboard's firm selector labels."""
    for score in scores:
        expected_company = firm_labels.get(score.ticker)
        if expected_company is None:
            raise ValueError(f"score file contains unknown ticker {score.ticker}")
        if expected_company != score.company:
            raise ValueError(
                f"{score.ticker} is labeled {score.company!r} in the score file; "
                f"dashboard expects {expected_company!r}"
            )
