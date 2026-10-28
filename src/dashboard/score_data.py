"""Validated reader for the preliminary annual SEC company score file."""

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


SCORES_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "processed"
    / "sec"
    / "company_scores_v0.csv"
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


def load_company_scores(path: Path = SCORES_FILE) -> tuple[CompanyYearScore, ...]:
    """Load and validate annual company scores; never fills missing years with zero."""
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
            scores.append(
                CompanyYearScore(
                    company=company,
                    ticker=ticker,
                    fiscal_year=fiscal_year,
                    ai_use_score=ai_use_score,
                    scenarios_with_use=tuple(scenarios.split()),
                    readiness_score=readiness_score,
                    talk_ratio_pct=talk_ratio_pct,
                    substantive_ai_passages=substantive_ai_passages,
                )
            )

    if not scores:
        raise ValueError("score CSV contains no company-year rows")
    return tuple(sorted(scores, key=lambda score: (score.ticker, score.fiscal_year)))


def validate_firm_labels(
    scores: Sequence[CompanyYearScore],
    firms: Sequence[Mapping[str, str]],
) -> None:
    """Ensure every score ticker maps to the dashboard's firm selector labels."""
    labels = {firm["ticker"]: firm["company"] for firm in firms}
    for score in scores:
        expected_company = labels.get(score.ticker)
        if expected_company is None:
            raise ValueError(f"score file contains unknown ticker {score.ticker}")
        if expected_company != score.company:
            raise ValueError(
                f"{score.ticker} is labeled {score.company!r} in the score file; "
                f"dashboard expects {expected_company!r}"
            )
