import json
import unittest
from pathlib import Path

import pandas as pd
from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "src" / "dashboard" / "app.py"


class DashboardAppTests(unittest.TestCase):
    def test_dashboard_uses_consensus_scores_and_real_data_views(self):
        app = AppTest.from_file(str(APP_PATH)).run()

        self.assertFalse(app.exception)
        self.assertEqual(app.title[0].value, "AI Adoption Index | Financial Firms")
        self.assertEqual(
            [tab.label for tab in app.tabs],
            ["Sector Overview", "Company Scores", "About the Data"],
        )
        self.assertIn("80 of 277 passages", app.warning[0].value)
        self.assertIn("AI-draft labels", app.warning[0].value)
        self.assertFalse(any("Fictional" in tab.label for tab in app.tabs))

        year_selector = next(
            selector
            for selector in app.selectbox
            if selector.label == "Fiscal year for firm comparison"
        )
        self.assertEqual(list(year_selector.options), ["2023", "2024", "2025"])

        company_table = next(
            table.value
            for table in app.dataframe
            if "Ticker" in table.value.columns
        )
        self.assertNotIn(2026, company_table["Fiscal year"].tolist())
        citi_row = company_table.loc[company_table["Ticker"] == "C"].iloc[0]
        self.assertEqual(citi_row["AI Use Score"], 53)
        self.assertIn(
            "RISKM — Risk and finance models",
            citi_row["Scenarios with use"],
        )

        about_text = "\n".join(element.value for element in app.markdown)
        self.assertIn("company_scores_consensus.csv", about_text)
        self.assertIn("80 of 277 passages have human-agreed labels", about_text)
        self.assertIn("sector_index.csv", about_text)
        self.assertIn("Citigroup is a benchmark and is excluded", about_text)
        self.assertIn("does not provide passage-level drill-down", about_text)

        for key in (
            "score_help_ai_use_score",
            "score_help_readiness_score",
            "score_help_talk_ratio",
        ):
            self.assertTrue(any(button.key == key for button in app.button))

    def test_sector_overview_renders_equal_and_market_cap_weighted_series(self):
        app = AppTest.from_file(str(APP_PATH)).run()

        self.assertFalse(app.exception)
        self.assertIn(
            "not every financial-services firm or a standard market-sector index",
            "\n".join(element.value for element in app.markdown),
        )
        sector_chart = next(
            json.loads(chart.proto.spec)
            for chart in app.get("plotly_chart")
            if {
                trace.get("name")
                for trace in json.loads(chart.proto.spec).get("data", [])
            }
            == {
                "Equal-weighted (AI-EW)",
                "Market-cap-weighted (AI-CW)",
            }
        )
        traces = {trace["name"]: trace for trace in sector_chart["data"]}
        self.assertEqual(traces["Equal-weighted (AI-EW)"]["x"], [2023, 2024, 2025])
        self.assertEqual(traces["Equal-weighted (AI-EW)"]["y"], [4.0, 7.0, 11.2])
        self.assertEqual(traces["Market-cap-weighted (AI-CW)"]["y"], [3.2, 6.7, 8.0])

        sector_table = next(
            table.value
            for table in app.dataframe
            if "Firms in index" in table.value.columns
        )
        self.assertEqual(sector_table["Firms in index"].tolist(), [6, 6, 6])
        self.assertEqual(
            sector_table["Fiscal year"].tolist(),
            [2023, 2024, 2025],
        )
        for key in (
            "sector_help_fiscal_year",
            "sector_help_firms_in_index",
            "sector_help_equal_weighted_score",
            "sector_help_market_cap_weighted_score",
            "sector_help_public_float_usd",
        ):
            self.assertTrue(any(button.key == key for button in app.button))

    def test_sector_table_help_explains_the_selected_six_company_sample(self):
        app = AppTest.from_file(str(APP_PATH)).run()
        help_button = next(
            button
            for button in app.button
            if button.key == "sector_help_firms_in_index"
        )
        help_button.click()
        app.run()

        self.assertTrue(
            any(
                "JPMorgan Chase, Bank of America, Capital One" in info.value
                and "Citigroup is a benchmark and is excluded" in info.value
                for info in app.info
            )
        )

    def test_missing_company_year_remains_unavailable_in_table(self):
        app = AppTest.from_file(str(APP_PATH)).run()
        year_selector = next(
            selector
            for selector in app.selectbox
            if selector.label == "Fiscal year for firm comparison"
        )
        year_selector.set_value("2023")
        app.run()

        company_table = next(
            table.value
            for table in app.dataframe
            if "Ticker" in table.value.columns
        )
        citi_row = company_table.loc[company_table["Ticker"] == "C"].iloc[0]
        self.assertEqual(citi_row["Status"], "No score available")
        self.assertTrue(pd.isna(citi_row["AI Use Score"]))

    def test_metric_help_explains_score_definition_and_limitations(self):
        app = AppTest.from_file(str(APP_PATH)).run()
        help_button = next(
            button for button in app.button if button.key == "score_help_ai_use_score"
        )
        help_button.click()
        app.run()

        self.assertTrue(
            any(
                "3, 1, or 0.5" in info.value
                and "80 of 277 passages" in info.value
                for info in app.info
            )
        )


if __name__ == "__main__":
    unittest.main()
