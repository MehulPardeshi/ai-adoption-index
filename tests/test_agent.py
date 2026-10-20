"""Tests for the agent (offline; no API key needed).

Run from the repo root:  python3 -m unittest discover -s tests -v
"""
import csv
import inspect
import tempfile
import unittest
from pathlib import Path

from src.agent import config

config.PROVIDER = "mock"                       # never call DeepSeek from tests
config.CACHE_DIR = Path(tempfile.mkdtemp()) / "llm"

from src.agent import run_batch, tools  # noqa: E402
from src.agent.verify import quote_in_source, verify_label  # noqa: E402

SRC = ("In 2025 we deployed a generative AI assistant to our call-center agents; "
       "it is now used by about 4,000 agents. We also use AI across our operations.")


def lab(**kw):
    base = {"evidence": "D1", "scenarios": ["ENT"], "topic": "USE",
            "quote": "We also use AI across our operations.", "specific": None, "confidence": 0.9, "flags": []}
    return base | kw


class VerifyLabelTests(unittest.TestCase):
    def test_clean_d1_passes(self):
        out = verify_label(lab(), SRC)
        self.assertEqual((out["evidence"], out["verify_status"]), ("D1", "pass"))

    def test_quote_not_in_source_goes_to_review(self):  # red-team RT08
        out = verify_label(lab(quote="We use AI to detect fraud."), SRC)
        self.assertEqual((out["evidence"], out["scenarios"], out["verify_status"]), ("N", [], "needs_review"))
        self.assertEqual(out["evidence_raw"], "D1")

    def test_tampered_number_goes_to_review(self):  # red-team RT09
        src = "Our virtual assistant handled about 2 million customer chats in 2025."
        out = verify_label(lab(evidence="D2", scenarios=["CX"], quote="handled about 20 million customer chats",
                               specific="20 million"), src)
        self.assertEqual(out["verify_status"], "needs_review")

    def test_d2_with_specific_passes(self):  # red-team RT18
        out = verify_label(lab(evidence="D2", scenarios=["CX"], quote="it is now used by about 4,000 agents",
                               specific="about 4,000 agents"), SRC)
        self.assertEqual((out["evidence"], out["verify_status"]), ("D2", "pass"))

    def test_d2_without_specific_drops_to_d1(self):
        out = verify_label(lab(evidence="D2", specific=None), SRC)
        self.assertEqual((out["evidence"], out["verify_status"]), ("D1", "downgraded"))

    def test_d2_generic_specific_drops_to_d1(self):
        out = verify_label(lab(evidence="D2", specific="AI"), SRC)
        self.assertEqual(out["evidence"], "D1")

    def test_d2_specific_outside_quote_drops_to_d1(self):
        out = verify_label(lab(evidence="D2", specific="4,000 agents"), SRC)
        self.assertEqual(out["evidence"], "D1")

    def test_low_confidence_goes_to_review(self):
        out = verify_label(lab(confidence=0.5), SRC)
        self.assertEqual((out["evidence"], out["verify_status"]), ("N", "needs_review"))

    def test_n_scenarios_are_removed(self):
        out = verify_label(lab(evidence="N", scenarios=["FRAUD"], quote=""), SRC)
        self.assertEqual((out["scenarios"], out["verify_status"]), ([], "downgraded"))

    def test_unknown_codes_go_to_review(self):
        self.assertEqual(verify_label(lab(evidence="D3"), SRC)["verify_status"], "needs_review")
        self.assertEqual(verify_label(lab(scenarios=["MAGIC"]), SRC)["verify_status"], "needs_review")

    def test_use_without_scenario_goes_to_review(self):
        self.assertEqual(verify_label(lab(scenarios=[]), SRC)["verify_status"], "needs_review")

    def test_company_mismatch_blocks_use(self):  # red-team RT14
        out = verify_label(lab(flags=["company_mismatch"]), SRC)
        self.assertEqual((out["evidence"], out["verify_status"]), ("N", "needs_review"))

    def test_quote_matching_tolerates_typography_only(self):
        self.assertTrue(quote_in_source("We  also use AI across our operations.", SRC))
        self.assertTrue(quote_in_source("we deployed a generative AI assistant ... used by about 4,000 agents", SRC))
        self.assertFalse(quote_in_source("used by about 4,000 agents ... we deployed a generative AI assistant", SRC))
        self.assertFalse(quote_in_source("AI", SRC))


class ToolTests(unittest.TestCase):
    def test_specs_match_functions(self):
        names = [s["function"]["name"] for s in tools.TOOL_SPECS]
        self.assertEqual(sorted(names), sorted(tools.FUNCTIONS))
        self.assertGreaterEqual(len(names), 5)  # course requirement #3
        for s in tools.TOOL_SPECS:
            params = inspect.signature(tools.FUNCTIONS[s["function"]["name"]]).parameters
            for p in list(s["function"]["parameters"]["properties"]) + s["function"]["parameters"]["required"]:
                self.assertIn(p, params, f"{s['function']['name']}: schema param {p} missing in function")
            self.assertTrue(tools.FUNCTIONS[s["function"]["name"]].__doc__)

    def test_lookup_baseline(self):
        jpm = tools.lookup_baseline("JPM", 2023)
        self.assertTrue(jpm["available"])
        self.assertAlmostEqual(jpm["ai_intensity_all"], 0.0913, places=3)
        self.assertEqual(jpm["filing_date"][:4], "2024")
        self.assertIn("Exhibit 13", tools.lookup_baseline("WFC", 2023)["note"])
        self.assertFalse(tools.lookup_baseline("JPM", 2025)["available"])

    def test_find_ai_passages_granularity(self):
        n = sum(tools.find_ai_passages(t, 2025, forms=["10-K"])["count"] for t in ["JPM", "BAC", "COF", "WFC", "SCHW", "PFG"])
        self.assertEqual(n, 90)  # the Oct 28 target set
        self.assertIn("error", tools.find_ai_passages("XYZ", 2025))

    def test_fetch_sec_filings_local(self):
        out = tools.fetch_sec_filings("JPM", 2025, forms=["10-K"])
        self.assertEqual([f["form"] for f in out["filings"]], ["10-K"])

    def test_dispatch_enforces_verify_and_blocks_live(self):
        out = tools.dispatch("classify_passage", {"text": "We use artificial intelligence across our operations.",
                                                  "company": "Example Bank"}, guardrails=True)
        self.assertIn("verify_status", out)
        self.assertNotIn("source", tools.dispatch("fetch_sec_filings", {"ticker": "JPM", "fiscal_year": 2025, "live": True}))
        self.assertIn("error", tools.dispatch("no_such_tool", {}))


class BatchContractTests(unittest.TestCase):
    def test_output_matches_v0_columns_and_scores(self):
        d = Path(tempfile.mkdtemp())
        rc = run_batch.main(["--tickers", "WFC", "--year", "2025", "--forms", "10-K",
                             "--labels-out", str(d / "l.csv"), "--scores-out", str(d / "s.csv")])
        self.assertEqual(rc, 0)
        with open(d / "l.csv", encoding="utf-8") as fh:
            header = next(csv.reader(fh))
        with open(config.DRAFT_LABELS, encoding="utf-8") as fh:
            v0 = next(csv.reader(fh))
        self.assertEqual(header[: len(v0)], v0)  # irr.py and score_companies read it unchanged
        with open(d / "s.csv", encoding="utf-8") as fh:
            scores = list(csv.DictReader(fh))
        self.assertEqual([(r["ticker"], r["fiscal_year"]) for r in scores], [("WFC", "2025")])


if __name__ == "__main__":
    unittest.main()
