"""Tests for #157: 10-Qs in the sector run land in the right fiscal year.

FY = the year the fiscal year ends. A 10-K belongs to the year of its period end; a 10-Q to the
fiscal year that ends on or after its period. For a firm whose year ends Sep 30 (Visa), the quarter
to Dec 31, 2024 is FY2025, not FY2024.

Offline: SEC is replaced by a fake `get`, the model by the mock provider.
Run from the repo root:  python3 -m unittest tests.test_tenq_fiscal_year -v
"""
import json
import tempfile
import unittest
from pathlib import Path

from src.agent import config

config.PROVIDER = "mock"                       # never call DeepSeek from tests
config.CACHE_DIR = Path(tempfile.mkdtemp()) / "llm"

from src.agent import run_batch, store  # noqa: E402
from src.edgar import download_sec_filings as dl  # noqa: E402
from src.edgar import download_sector  # noqa: E402
from src.edgar.download_sector import fiscal_year, fiscal_year_end  # noqa: E402
from src.index import apply_review, sector_index, sector_run_report  # noqa: E402
from src.index.score_companies import score  # noqa: E402

try:
    from tests.test_sector_run import read_csv, run_folder, write_csv
except ImportError:  # discovered with -s tests
    from test_sector_run import read_csv, run_folder, write_csv

AI_USE = "In fiscal 2025 we deployed an AI model that scores every card payment for fraud in real time."
PLAIN = "Payments volume grew in the quarter, driven by higher cross-border travel and card spending."


class FiscalYearRuleTests(unittest.TestCase):
    def test_ten_q_goes_to_the_fiscal_year_it_belongs_to(self):
        cases = [  # (form, period, year end, FY)
            ("10-Q", "2024-12-31", "0930", "2025"),   # Visa, BEN, RJF: Q1 of FY2025
            ("10-Q", "2025-06-30", "0930", "2025"),
            ("10-Q", "2025-12-31", "0930", "2026"),
            ("10-Q", "2024-11-30", "0831", "2025"),   # FactSet
            ("10-Q", "2025-05-31", "0831", "2025"),
            ("10-Q", "2023-09-30", "0630", "2024"),   # Jack Henry: FY2024 starts Jul 2023
            ("10-Q", "2024-03-31", "0630", "2024"),
            ("10-Q", "2025-09-30", "1231", "2025"),   # calendar year: always the period's year
            ("10-K", "2024-09-30", "0930", "2024"),   # a 10-K: the year of its period end
            ("10-K", "2025-12-31", "1231", "2025"),
        ]
        for form, period, fye, want in cases:
            with self.subTest(form=form, period=period, fye=fye):
                self.assertEqual(fiscal_year(form, period, fye), want)

    def test_year_end_from_the_latest_10k(self):
        filings = [{"form": "10-Q", "period": "2025-06-30"}, {"form": "10-K", "period": "2024-09-30"},
                   {"form": "10-K", "period": "2025-09-30"}]
        self.assertEqual(fiscal_year_end(filings, "1231"), "0930")        # the 10-Ks win over SEC's field
        self.assertEqual(fiscal_year_end([{"form": "10-Q", "period": "2025-06-30"}], "0831"), "0831")
        self.assertEqual(fiscal_year_end([], ""), "1231")

    def test_the_five_off_calendar_firms_in_the_76_firm_run(self):
        inv = read_csv(Path("data/processed/sec/sp500_financials/filings_inventory.csv"))
        fye = {t: fiscal_year_end([r for r in inv if r["ticker"] == t]) for t in {r["ticker"] for r in inv}}
        off = {t: v for t, v in fye.items() if v != "1231"}
        self.assertEqual(off, {"BEN": "0930", "FDS": "0831", "JKHY": "0630", "RJF": "0930", "V": "0930"})


class FakeVisa:
    """A tiny EDGAR for one firm whose year ends Sep 30: 10-Ks FY2023-FY2025 and 10-Qs either side."""
    CIK = 1403161

    def __init__(self):
        self.periods = [("10-K", "2023-09-30"), ("10-Q", "2023-06-30"), ("10-Q", "2023-12-31"), ("10-Q", "2024-03-31"),
                        ("10-Q", "2024-06-30"), ("10-K", "2024-09-30"), ("10-Q", "2024-12-31"), ("10-Q", "2025-03-31"),
                        ("10-Q", "2025-06-30"), ("10-K", "2025-09-30"), ("10-Q", "2025-12-31")]
        rec = {"form": [], "accessionNumber": [], "filingDate": [], "reportDate": [], "primaryDocument": []}
        self.pages = {}
        for i, (form, period) in enumerate(reversed(self.periods)):
            acc = f"0001403161-00-{i:06d}"
            doc = f"v-{period}-{form.lower()}.htm"
            rec["form"].append(form)
            rec["accessionNumber"].append(acc)
            rec["filingDate"].append(period)
            rec["reportDate"].append(period)
            rec["primaryDocument"].append(doc)
            text = AI_USE if (form, period) == ("10-Q", "2024-12-31") else PLAIN
            self.pages[f"https://www.sec.gov/Archives/edgar/data/{self.CIK}/{acc.replace('-', '')}/{doc}"] = \
                f"<html><body><p>{text}</p></body></html>"
            if form == "10-K":
                setattr(self, f"acc_{period[:4]}", acc)
        self.pages[f"https://data.sec.gov/submissions/CIK{self.CIK:010d}.json"] = {
            "name": "VISA INC.", "tickers": ["V"], "fiscalYearEnd": "0930", "filings": {"recent": rec, "files": []}}
        self.pages[f"https://data.sec.gov/api/xbrl/companyconcept/CIK{self.CIK:010d}/dei/EntityPublicFloat.json"] = {
            "units": {"USD": [{"end": "2024-03-31", "val": 400_000_000_000, "accn": self.acc_2024, "form": "10-K"},
                              {"end": "2025-03-31", "val": 500_000_000_000, "accn": self.acc_2025, "form": "10-K"}]}}

    def get(self, url, as_json=False):
        if url not in self.pages:  # e.g. the filing index pages: the downloader keeps the primary document
            raise RuntimeError(f"404 {url}")
        return self.pages[url]


class DownloaderTenQTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.firms = write_csv(self.tmp / "firms.csv", [
            {"ticker": "V", "company": "Visa", "cik": "0001403161", "gics_sub_industry": "Transaction & Payment Processing",
             "firm_type": "payments_consumer_finance", "poc_firm": "", "date_added": "", "source": "t",
             "source_date": "2026-11-05"}])
        self.real_get = dl.get
        dl.get = FakeVisa().get

    def tearDown(self):
        dl.get = self.real_get

    def run_once(self, forms):
        out = self.tmp / forms.replace(",", "_")
        rc = download_sector.main([
            "--firms", str(self.firms), "--forms", forms, "--raw-dir", str(self.tmp / "raw"),
            "--float-corrections", str(self.tmp / "none.csv"),
            "--passages-out", str(out / "p.csv"), "--inventory-out", str(out / "inv.csv"),
            "--float-out", str(out / "fl.csv"), "--info-out", str(out / "info.json")])
        self.assertEqual(rc, 0)
        return (read_csv(out / "p.csv"), read_csv(out / "inv.csv"), read_csv(out / "fl.csv"),
                json.loads((out / "info.json").read_text(encoding="utf-8")))

    def test_ten_qs_land_in_their_fiscal_year(self):
        passages, inv, floats, info = self.run_once("10-K,10-Q")
        self.assertEqual([(r["form"], r["period"], r["fiscal_year"]) for r in inv], [
            ("10-Q", "2023-12-31", "2024"),        # read although its period is before 2024-01-01
            ("10-Q", "2024-03-31", "2024"), ("10-Q", "2024-06-30", "2024"), ("10-K", "2024-09-30", "2024"),
            ("10-Q", "2024-12-31", "2025"),        # Q1 of FY2025, not FY2024
            ("10-Q", "2025-03-31", "2025"), ("10-Q", "2025-06-30", "2025"), ("10-K", "2025-09-30", "2025")])
        # FY2023 (10-K and its June 10-Q) and FY2026 (the Dec 2025 quarter) are left out
        self.assertEqual([(p["passage_id"], p["fiscal_year"]) for p in passages], [("V_2024-12-31_10-Q_00000", "2025")])
        self.assertEqual([(f["fiscal_year"], f["public_float_usd"]) for f in floats],
                         [("2024", "400000000000"), ("2025", "500000000000")])
        self.assertFalse([p for p in info["problems"] if p["where"] == "fiscal year"])  # 3 10-Qs a year is normal
        self.assertEqual(info["fiscal_years"], [2024, 2025])
        self.assertEqual(info["periods_read_from"], "2023-01-01")
        self.assertEqual(info["filings_in_next_fiscal_year"], 2)       # the two December quarters
        self.assertEqual(info["fiscal_year_end_not_december"], {"V": "0930"})

    def test_ten_k_only_run_is_unchanged(self):
        passages, inv, floats, info = self.run_once("10-K")
        self.assertEqual([(r["form"], r["period"], r["fiscal_year"]) for r in inv],
                         [("10-K", "2024-09-30", "2024"), ("10-K", "2025-09-30", "2025")])
        self.assertEqual(passages, [])
        self.assertEqual(info["periods_read_from"], "2024-01-01")


def label(pid, period, fy=None, ev="D1", scen="FRAUD", status="pass"):
    row = {"passage_id": pid, "company": "Visa", "ticker": "V", "form": pid.split("_")[2], "period": period,
           "topic_v0": "", "evidence_v0": ev, "scenarios_v0": scen, "coder": "", "coder_note": "", "source_url": "x",
           "quote": "q", "specific": "", "confidence": "0.9", "flags": "", "evidence_raw": ev, "scenarios_raw": scen,
           "verify_status": status, "verify_reason": "", "model": "m", "prompt_version": "classify-v1.5", "run_at": ""}
    if fy:
        row["fiscal_year"] = fy
    return row


class ScoringTests(unittest.TestCase):
    def test_score_uses_the_fiscal_year_column(self):
        rows = score([label("V_2024-12-31_10-Q_00000", "2024-12-31", fy="2025"),
                      label("V_2024-09-30_10-K_00001", "2024-09-30", fy="2024", ev="N", scen="")])
        self.assertEqual({(r["fiscal_year"], r["ai_use_score"]) for r in rows}, {("2024", 0), ("2025", 3)})

    def test_without_the_column_the_period_year_still_counts(self):  # the 7-firm labels
        rows = score([label("V_2024-12-31_10-Q_00000", "2024-12-31")])
        self.assertEqual([r["fiscal_year"] for r in rows], ["2024"])

    def test_batch_carries_the_fiscal_year_to_labels_and_scores(self):
        tmp = Path(tempfile.mkdtemp())
        src = write_csv(tmp / "p.csv", [{
            "passage_id": "V_2024-12-31_10-Q_00000", "company": "Visa", "ticker": "V", "form": "10-Q",
            "period": "2024-12-31", "fiscal_year": "2025", "filing_date": "2025-01-30", "section_guess": "",
            "matched_terms": "ai", "strength": "strong", "words": len(AI_USE.split()), "passage": AI_USE,
            "source_url": "https://x"}])
        before = config.PASSAGES
        try:
            rc = run_batch.main(["--passages", str(src), "--labels-out", str(tmp / "l.csv"),
                                 "--scores-out", str(tmp / "s.csv"), "--run-info-out", str(tmp / "i.json")])
            self.assertEqual(rc, 0)
            labels = read_csv(tmp / "l.csv")
            self.assertEqual(list(labels[0])[-1], "fiscal_year")      # last, so the v0 columns stay first
            self.assertEqual(labels[0]["fiscal_year"], "2025")
            self.assertEqual([s["fiscal_year"] for s in read_csv(tmp / "s.csv")], ["2025"])
            self.assertEqual([r["passage_id"] for r in store.select_passages(fiscal_years=[2025])],
                             ["V_2024-12-31_10-Q_00000"])
            self.assertEqual(store.select_passages(fiscal_years=[2024]), [])
        finally:
            config.PASSAGES = before

    def test_human_review_keeps_the_fiscal_year(self):
        labels = [label("V_2024-12-31_10-Q_00000", "2024-12-31", fy="2025", ev="N", scen="", status="needs_review")]
        labels[0].update(evidence_raw="D1", scenarios_raw="FRAUD")
        queue = [{"passage_id": "V_2024-12-31_10-Q_00000", "review_evidence": "D1", "review_scenarios": "FRAUD",
                  "reviewer": "Shu", "review_note": ""}]
        out, counts, problems = apply_review.apply(labels, queue)
        self.assertEqual((counts["reviewed"], problems), (1, []))
        self.assertEqual([(r["fiscal_year"], r["ai_use_score"]) for r in score(out)], [("2025", 3)])

    def test_index_reads_the_inventory_fiscal_year(self):
        inv = [{"ticker": "V", "form": "10-K", "period": "2025-09-30", "fiscal_year": "2025"},
               {"ticker": "V", "form": "10-Q", "period": "2024-12-31", "fiscal_year": "2025"}]
        floats = [{"ticker": "V", "fiscal_year": "2025", "public_float_usd": "100"}]
        index, _ = sector_index.build([{"ticker": "V", "fiscal_year": "2025", "ai_use_score": "3"}], floats, inv)
        self.assertEqual([(r["fiscal_year"], r["n_firms"], r["ai_ew"]) for r in index], [("2025", 1, 3.0)])


class ReportTests(unittest.TestCase):
    def test_report_shows_ten_qs_when_the_run_has_them(self):
        tmp = Path(tempfile.mkdtemp())
        d = run_folder(tmp)
        inv = read_csv(d / "filings_inventory.csv")
        inv.append(dict(inv[0], form="10-Q", period="2025-03-31", fiscal_year="2025"))
        write_csv(d / "filings_inventory.csv", inv)
        info = json.loads((d / "download_info.json").read_text(encoding="utf-8"))
        info.update(forms=["10-K", "10-Q"], fiscal_year_end_not_december={"V": "0930"})
        (d / "download_info.json").write_text(json.dumps(info), encoding="utf-8")
        md, _ = sector_run_report.build(d, tmp / "passages.csv", today="2026-11-21")
        self.assertIn("a 10-Q counts in the fiscal year it belongs to", md)
        self.assertIn("| 10-Qs | AI passages (10-K / 10-Q) |", md)
        self.assertNotIn("with periods 2024-01-01", md)
        self.assertIn("this run includes the 10-Qs", md)
        self.assertIn("agent's 10-K and 10-Q scores", md)

    def test_ten_k_only_report_is_unchanged(self):
        tmp = Path(tempfile.mkdtemp())
        md, _ = sector_run_report.build(run_folder(tmp), tmp / "passages.csv", today="2026-11-21")
        self.assertIn("with periods 2024-01-01 to 2025-12-31", md)
        self.assertNotIn("| 10-Qs |", md)
        self.assertIn("this run is 10-K only", md)


if __name__ == "__main__":
    unittest.main()
