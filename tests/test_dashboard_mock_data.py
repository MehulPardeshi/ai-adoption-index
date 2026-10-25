import unittest
from collections import Counter

from src.dashboard.mock_data import (
    DEMO_AREAS,
    DEMO_STAGES,
    FIRMS,
    USE_CASES,
    compare_timeline,
    compare_use_cases,
    get_firms,
    get_use_cases,
    summarize_use_cases,
)


class DashboardMockDataTests(unittest.TestCase):
    def test_cohort_matches_six_core_firms_and_citigroup_benchmark(self):
        self.assertEqual(len(get_firms()), 7)
        core_tickers = {
            firm["ticker"] for firm in FIRMS if firm.get("cohort") != "Benchmark"
        }
        benchmark_firms = [
            firm for firm in FIRMS if firm.get("cohort") == "Benchmark"
        ]

        self.assertEqual(core_tickers, {"JPM", "BAC", "COF", "WFC", "SCHW", "PFG"})
        self.assertEqual([firm["ticker"] for firm in benchmark_firms], ["C"])
        self.assertEqual(benchmark_firms[0]["company"], "Citigroup")

    def test_every_firm_has_eight_complete_fictional_records(self):
        self.assertEqual(len(USE_CASES), len(FIRMS) * 8)
        self.assertEqual(len({record["id"] for record in USE_CASES}), len(USE_CASES))
        known_tickers = {firm["ticker"] for firm in FIRMS}
        for record in USE_CASES:
            self.assertIn(record["ticker"], known_tickers)
            self.assertIn(record["area"], DEMO_AREAS)
            self.assertIn(record["stage"], DEMO_STAGES)
            for field in ("quarter", "title", "summary", "detail"):
                self.assertTrue(record[field])
        for ticker in known_tickers:
            records = get_use_cases(ticker)
            self.assertEqual(len(records), 8)
            self.assertEqual({record["area"] for record in records}, set(DEMO_AREAS))

    def test_selected_firm_records_are_filtered_and_copied(self):
        records = get_use_cases("BAC")

        self.assertEqual(len(records), 8)
        self.assertEqual({record["ticker"] for record in records}, {"BAC"})
        records[0]["title"] = "Changed by caller"
        self.assertNotEqual(get_use_cases("BAC")[0]["title"], "Changed by caller")

    def test_summary_is_derived_from_firm_records(self):
        records = get_use_cases("JPM")
        summary = summarize_use_cases("JPM")
        expected_stages = Counter(record["stage"] for record in records)

        self.assertEqual(summary["record_count"], len(records))
        self.assertEqual(summary["area_count"], len({record["area"] for record in records}))
        self.assertEqual(summary["stage_counts"], dict(expected_stages))
        self.assertEqual(
            summary["latest_record"]["quarter"],
            max(record["quarter"] for record in records),
        )

    def test_comparison_summarizes_the_same_mock_records(self):
        rows = compare_use_cases(["BAC", "COF"])

        self.assertEqual({row["ticker"] for row in rows}, {"BAC", "COF"})
        for row in rows:
            records = get_use_cases(row["ticker"])
            self.assertEqual(row["examples"], len(records))
            self.assertEqual(
                sum(row["stage_counts"].values()),
                len(records),
            )
            self.assertEqual(
                sum(row["area_counts"].values()),
                len(records),
            )

    def test_timeline_is_chronological_and_counts_selected_fixture_records(self):
        tickers = ["BAC", "COF"]
        rows = compare_timeline(tickers)
        quarters = list(dict.fromkeys(row["quarter"] for row in rows))
        self.assertEqual(
            quarters,
            sorted(
                quarters,
                key=lambda quarter: (
                    int(quarter.split()[0]),
                    int(quarter.split()[1][1:]),
                ),
            ),
        )

        for ticker in tickers:
            firm_rows = [row for row in rows if row["ticker"] == ticker]
            counts = [row["cumulative_examples"] for row in firm_rows]
            self.assertEqual(counts, sorted(counts))
            self.assertEqual(counts[-1], len(get_use_cases(ticker)))

        first_firm_counts = [
            row["cumulative_examples"] for row in rows if row["ticker"] == tickers[0]
        ]
        second_firm_counts = [
            row["cumulative_examples"] for row in rows if row["ticker"] == tickers[1]
        ]
        self.assertNotEqual(first_firm_counts, second_firm_counts)
        self.assertEqual(
            {row["ticker"] for row in rows},
            set(tickers),
        )

    def test_unknown_firm_has_no_records_or_summary(self):
        self.assertEqual(get_use_cases("UNKNOWN"), [])
        summary = summarize_use_cases("UNKNOWN")
        self.assertEqual(summary["record_count"], 0)
        self.assertIsNone(summary["latest_record"])


if __name__ == "__main__":
    unittest.main()
