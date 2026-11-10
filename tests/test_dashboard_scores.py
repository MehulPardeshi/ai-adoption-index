import csv
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from src.dashboard.score_data import (
    FIRM_LABELS,
    SCORES_FILE,
    SCORE_COLUMNS,
    SCORE_METRIC_HELP,
    SECTOR_INDEX_COLUMNS,
    SECTOR_INDEX_FILE,
    complete_fiscal_year_scores,
    complete_sector_index_years,
    format_scenario_code,
    load_company_scores,
    load_sector_index,
    validate_firm_labels,
)


class DashboardScoreDataTests(unittest.TestCase):
    def test_loads_consensus_scores_and_matches_dashboard_firms(self):
        scores = load_company_scores()
        validate_firm_labels(scores)

        self.assertEqual(SCORES_FILE.name, "company_scores_consensus.csv")
        self.assertEqual(len(scores), 26)
        self.assertEqual(
            len({(score.ticker, score.fiscal_year) for score in scores}),
            len(scores),
        )
        self.assertEqual({score.ticker for score in scores}, set(FIRM_LABELS))
        consensus_scores = {
            (score.ticker, score.fiscal_year): score.ai_use_score
            for score in scores
        }
        self.assertEqual(consensus_scores[("C", 2025)], 53)
        self.assertEqual(consensus_scores[("COF", 2025)], 20)
        self.assertEqual(consensus_scores[("PFG", 2025)], 18)

    def test_missing_company_years_remain_missing(self):
        scores = load_company_scores()
        score_keys = {(score.ticker, score.fiscal_year) for score in scores}

        self.assertNotIn(("C", 2023), score_keys)
        self.assertNotIn(("PFG", 2023), score_keys)
        self.assertIn(("C", 2024), score_keys)

    def test_partial_fiscal_year_is_hidden_without_removing_source_data(self):
        source_scores = load_company_scores()
        displayed_scores = complete_fiscal_year_scores(source_scores)

        self.assertIn(2026, {score.fiscal_year for score in source_scores})
        self.assertNotIn(2026, {score.fiscal_year for score in displayed_scores})
        self.assertEqual(
            {score.fiscal_year for score in displayed_scores},
            {2023, 2024, 2025},
        )

    def test_loads_sector_index_for_core_firms_and_both_weightings(self):
        rows = complete_sector_index_years(load_sector_index())

        self.assertEqual(SECTOR_INDEX_FILE.name, "sector_index.csv")
        self.assertEqual([row.fiscal_year for row in rows], [2023, 2024, 2025])
        self.assertTrue(all(row.n_firms == 6 for row in rows))
        self.assertEqual((rows[-1].ai_ew, rows[-1].ai_cw), (11.2, 8.0))
        self.assertNotIn("C", rows[-1].firms)

    def test_sector_index_loader_validates_weightings_and_partial_years(self):
        rows = [
            {
                "fiscal_year": "2025",
                "n_firms": "2",
                "ai_ew": "20.5",
                "ai_cw": "18.25",
                "total_public_float_usd": "500",
                "firms": "JPM BAC",
            },
            {
                "fiscal_year": "2026",
                "n_firms": "2",
                "ai_ew": "24",
                "ai_cw": "22",
                "total_public_float_usd": "600",
                "firms": "JPM BAC",
            },
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(
                Path(directory),
                "sector.csv",
                SECTOR_INDEX_COLUMNS,
                rows,
            )
            source_rows = load_sector_index(path)

        self.assertEqual(len(source_rows), 2)
        self.assertEqual([row.fiscal_year for row in complete_sector_index_years(source_rows)], [2025])
        self.assertEqual(source_rows[0].ai_cw, 18.25)
        self.assertEqual(source_rows[0].firms, ("JPM", "BAC"))

    def test_rejects_sector_index_when_firm_count_does_not_match(self):
        row = {
            "fiscal_year": "2025",
            "n_firms": "2",
            "ai_ew": "20",
            "ai_cw": "18",
            "total_public_float_usd": "500",
            "firms": "JPM",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(
                Path(directory),
                "sector.csv",
                SECTOR_INDEX_COLUMNS,
                [row],
            )
            with self.assertRaisesRegex(ValueError, "firms must contain 2 unique ticker"):
                load_sector_index(path)

    def test_sector_index_rejects_benchmark_company(self):
        row = {
            "fiscal_year": "2025",
            "n_firms": "1",
            "ai_ew": "20",
            "ai_cw": "18",
            "total_public_float_usd": "500",
            "firms": "C",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(
                Path(directory),
                "sector.csv",
                SECTOR_INDEX_COLUMNS,
                [row],
            )
            with self.assertRaisesRegex(ValueError, "non-core ticker"):
                load_sector_index(path)

    def test_scenario_codes_show_frozen_codebook_names(self):
        self.assertEqual(
            format_scenario_code("CX"),
            "CX — Customer service and digital assistants",
        )
        self.assertEqual(
            format_scenario_code("ENT"),
            "ENT — Enterprise-wide, area not named",
        )

    def test_unknown_scenario_codes_are_rejected(self):
        row = self._score_row()
        row["scenarios_with_use"] = "NOT_A_CODE"
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(
                Path(directory),
                "scores.csv",
                SCORE_COLUMNS,
                [row],
            )

            with self.assertRaisesRegex(ValueError, "unknown taxonomy scenario code"):
                load_company_scores(path)

    def test_score_metric_help_defines_each_metric_and_limit(self):
        self.assertEqual(
            set(SCORE_METRIC_HELP),
            {"AI Use Score", "Readiness Score", "Talk Ratio (%)"},
        )
        self.assertIn("not verified firm-wide adoption", SCORE_METRIC_HELP["AI Use Score"])
        self.assertIn("80 of 277 passages", SCORE_METRIC_HELP["AI Use Score"])
        self.assertIn("governance, talent, and investment", SCORE_METRIC_HELP["Readiness Score"])
        self.assertIn("percentage of substantive AI passages labeled N", SCORE_METRIC_HELP["Talk Ratio (%)"])

    def test_allows_blank_scenario_and_undefined_talk_ratio(self):
        row = self._score_row()
        row["scenarios_with_use"] = ""
        row["talk_ratio_pct"] = ""
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(
                Path(directory),
                "scores.csv",
                SCORE_COLUMNS,
                [row],
            )
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
        rows = [self._score_row(), self._score_row()]
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(
                Path(directory),
                "scores.csv",
                SCORE_COLUMNS,
                rows,
            )

            with self.assertRaisesRegex(ValueError, "duplicate score row"):
                load_company_scores(path)

    def test_rejects_invalid_scores(self):
        row = self._score_row()
        row["ai_use_score"] = "101"
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_csv(
                Path(directory),
                "scores.csv",
                SCORE_COLUMNS,
                [row],
            )

            with self.assertRaisesRegex(ValueError, "ai_use_score"):
                load_company_scores(path)

    def test_rejects_unknown_ticker_and_company_label_mismatch(self):
        scores = load_company_scores()
        with self.assertRaisesRegex(ValueError, "unknown ticker"):
            validate_firm_labels(
                (self._score_with_company_ticker(scores[0], "Unknown", "ZZZ"),)
            )
        with self.assertRaisesRegex(ValueError, "dashboard expects"):
            validate_firm_labels(
                (self._score_with_company_ticker(scores[0], "Wrong label"),)
            )

    @staticmethod
    def _score_row():
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
    def _write_csv(directory, filename, columns, rows):
        path = directory / filename
        with path.open("w", newline="", encoding="utf-8") as output:
            writer = csv.DictWriter(output, fieldnames=columns)
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
