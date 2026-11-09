import json
import unittest
from pathlib import Path

import pandas as pd
from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "src" / "dashboard" / "app.py"


class DashboardAppTests(unittest.TestCase):
    def test_story_overview_shows_three_summary_items_and_secondary_details(self):
        app = AppTest.from_file(str(APP_PATH)).run()

        self.assertFalse(app.exception)
        story_metrics = [
            metric
            for metric in app.metric
            if metric.label in {"Fictional records", "Example areas"}
        ]
        self.assertEqual(
            [(metric.label, metric.value) for metric in story_metrics],
            [("Fictional records", "8"), ("Example areas", "5 of 5")],
        )
        self.assertFalse(
            any(
                metric.label.startswith("Demo stage")
                or metric.label == "Latest example period"
                for metric in app.metric
            )
        )

        stage_chart = next(
            json.loads(chart.proto.spec)
            for chart in app.get("plotly_chart")
            if {
                trace.get("name")
                for trace in json.loads(chart.proto.spec).get("data", [])
            }
            == {"Exploring", "Pilot", "In use"}
        )
        self.assertEqual(stage_chart["layout"]["barmode"], "stack")
        self.assertEqual(
            {
                trace["name"]: trace["x"][0]
                for trace in stage_chart["data"]
            },
            {"Exploring": 2, "Pilot": 3, "In use": 3},
        )

        details = next(
            expander for expander in app.expander
            if expander.label == "More Demo Details"
        )
        self.assertFalse(details.proto.expanded)
        details_text = "\n".join(markdown.value for markdown in details.markdown)
        self.assertIn("Latest fictional example period: **2026 Q3**", details_text)
        self.assertIn("Exploring: 2", details_text)
        self.assertIn("Pilot: 3", details_text)
        self.assertIn("In use: 3", details_text)

        visible_titles = "\n".join(element.value for element in app.markdown)
        self.assertIn("Stage mix", visible_titles)
        self.assertIn("Fictional Example Timeline", visible_titles)
        self.assertIn("Open a Fictional Use Case", visible_titles)
        self.assertTrue(any("Open" in button.label for button in app.button))

    def test_score_view_hides_partial_year_and_explains_data(self):
        app = AppTest.from_file(str(APP_PATH)).run()

        self.assertFalse(app.exception)
        self.assertEqual(app.title[0].value, "AI Adoption Index | SEC Pilot + Envisioned Demo")
        self.assertEqual(
            [tab.label for tab in app.tabs],
            [
                "SEC Pilot Scores",
                "Envisioned Firm Story",
                "Envisioned Comparison",
                "About the Data",
            ],
        )
        self.assertEqual(app.sidebar.selectbox, [])
        self.assertIn("Two Distinct Data Tracks.", app.warning[0].value)

        year_selector = next(
            selector
            for selector in app.selectbox
            if selector.label == "Fiscal year for firm comparison"
        )
        self.assertEqual(list(year_selector.options), ["2023", "2024", "2025"])

        scores_table = app.dataframe[0].value
        self.assertNotIn(2026, scores_table["Fiscal year"].tolist())
        self.assertIn(
            "RISKM — Risk and finance models",
            scores_table["Scenarios with use"].tolist(),
        )

        about_text = "\n".join(element.value for element in app.markdown)
        self.assertIn("10-K and 10-Q filing passages", about_text)
        self.assertIn("does not yet integrate the latest agreed human labels", about_text)
        self.assertIn(
            "FY2026 because source filings are only available through June 30, 2026",
            about_text,
        )

        for key in (
            "score_help_ai_use_score",
            "score_help_readiness_score",
            "score_help_talk_ratio",
        ):
            self.assertTrue(any(button.key == key for button in app.button))

        help_button = next(
            button for button in app.button if button.key == "score_help_ai_use_score"
        )
        help_button.click()
        app.run()
        self.assertTrue(
            any(
                "A preliminary 0–100 disclosure score" in info.value
                for info in app.info
            )
        )

        sector_selector = next(
            selector for selector in app.selectbox if selector.key == "story_sector"
        )
        company_selector = next(
            selector for selector in app.selectbox if selector.key == "story_company"
        )
        self.assertIn("Sector", sector_selector.label)
        self.assertEqual(len(company_selector.options), 7)
        sector_selector.set_value("Banks")
        app.run()
        company_selector = next(
            selector for selector in app.selectbox if selector.key == "story_company"
        )
        self.assertEqual(
            set(company_selector.options),
            {
                "JPMorgan Chase",
                "Bank of America",
                "Capital One",
                "Wells Fargo",
                "Citigroup",
            },
        )
        company_selector.set_value("Bank of America")
        app.run()
        self.assertIn("Bank of America", [item.value for item in app.subheader])
        self.assertEqual(app.sidebar.selectbox, [])

        year_selector = next(
            selector
            for selector in app.selectbox
            if selector.label == "Fiscal year for firm comparison"
        )
        year_selector.set_value("2023")
        app.run()
        scores_table = app.dataframe[0].value
        citi_row = scores_table.loc[scores_table["Ticker"] == "C"].iloc[0]
        self.assertEqual(citi_row["Status"], "No score available")
        self.assertTrue(pd.isna(citi_row["AI Use Score"]))


if __name__ == "__main__":
    unittest.main()
