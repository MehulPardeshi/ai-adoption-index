import csv
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from src.dashboard.mock_data import FIRMS
from src.dashboard.score_data import (
    SCORE_COLUMNS,
    load_company_scores,
    validate_firm_labels,
)


class DashboardScoreDataTests(unittest.TestCase):
    def test_loads_current_scores_and_matches_dashboard_firms(self):
        scores = load_company_scores()
        validate_firm_labels(scores, FIRMS)

        self.assertEqual(len(scores), 26)
        self.assertEqual(
            len({(score.ticker, score.fiscal_year) for score in scores}),
            len(scores),
        )
        self.assertEqual(
            {score.ticker for score in scores},
            {firm["ticker"] for firm in FIRMS},
        )

    def test_missing_company_years_remain_missing(self):
        scores = load_company_scores()
        score_keys = {(score.ticker, score.fiscal_year) for score in scores}

        self.assertNotIn(("C", 2023), score_keys)
        self.assertNotIn(("PFG", 2023), score_keys)
        self.assertIn(("C", 2024), score_keys)

    def test_allows_blank_scenario_and_undefined_talk_ratio(self):
        row = {
            "company": "Test Company",
            "ticker": "TST",
            "fiscal_year": "2025",
            "ai_use_score": "0",
            "scenarios_with_use": "",
            "readiness_score": "0",
            "talk_ratio_pct": "",
            "substantive_ai_passages": "0",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(Path(directory), [row])
            score = load_company_scores(path)[0]

        self.assertEqual(score.scenarios_with_use, ())
        self.assertIsNone(score.talk_ratio_pct)

    def test_rejects_missing_required_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scores.csv"
            path.write_text("company,ticker\nTest Company,TST\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "missing required columns"):
                load_company_scores(path)

    def test_rejects_duplicate_company_year_rows(self):
        rows = [self._row(), self._row()]
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(Path(directory), rows)

            with self.assertRaisesRegex(ValueError, "duplicate score row"):
                load_company_scores(path)

    def test_rejects_invalid_scores(self):
        row = self._row()
        row["ai_use_score"] = "101"
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(Path(directory), [row])

            with self.assertRaisesRegex(ValueError, "ai_use_score"):
                load_company_scores(path)

    def test_rejects_unknown_ticker_and_company_label_mismatch(self):
        scores = load_company_scores()
        with self.assertRaisesRegex(ValueError, "unknown ticker"):
            validate_firm_labels(
                (self._score_with_company_ticker(scores[0], "Unknown", "ZZZ"),),
                FIRMS,
            )
        with self.assertRaisesRegex(ValueError, "dashboard expects"):
            validate_firm_labels(
                (self._score_with_company_ticker(scores[0], "Wrong label"),),
                FIRMS,
            )

    @staticmethod
    def _row():
        return {
            "company": "Test Company",
            "ticker": "TST",
            "fiscal_year": "2025",
            "ai_use_score": "1",
            "scenarios_with_use": "ENT",
            "readiness_score": "0",
            "talk_ratio_pct": "50",
            "substantive_ai_passages": "2",
        }

    @staticmethod
    def _write_csv(directory, rows):
        path = directory / "scores.csv"
        with path.open("w", newline="", encoding="utf-8") as output:
            writer = csv.DictWriter(output, fieldnames=SCORE_COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        return path

    @staticmethod
    def _score_with_company_ticker(score, company, ticker=None):
        return replace(
            score,
            company=company,
            ticker=ticker if ticker is not None else score.ticker,
        )


if __name__ == "__main__":
    unittest.main()
