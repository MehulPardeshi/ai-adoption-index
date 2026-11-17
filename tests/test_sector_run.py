"""Tests for the S&P 500 Financials run (#133): firm list, downloader, batch options, report, pilot sample.

Offline: SEC is replaced by a fake `get`, the model by the mock provider.
Run from the repo root:  python3 -m unittest tests.test_sector_run -v
"""
import csv
import json
import tempfile
import unittest
from pathlib import Path

from src.agent import config

config.PROVIDER = "mock"                       # never call DeepSeek from tests
config.CACHE_DIR = Path(tempfile.mkdtemp()) / "llm"

from src.agent import run_batch  # noqa: E402
from src.edgar import download_sec_filings as dl  # noqa: E402
from src.edgar import download_sector, float_corrections, make_firm_list  # noqa: E402
from src.eval import make_sector_pilot_sample as pilot  # noqa: E402
from src.index import sector_run_report  # noqa: E402

AI_USE = "In 2025 we deployed a generative AI assistant that our claims adjusters use for about 40,000 claims a month."
AI_RISK = "Artificial intelligence may be used by criminals to commit fraud, which could harm our business and results."
PLAIN = "Our net premiums written increased in 2025, driven by rate increases across most lines of business."


def html(*paras: str) -> str:
    return "<html><body>" + "".join(f"<p>{p}</p>" for p in paras) + "</body></html>"


def write_csv(path: Path, rows: list[dict]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return path


def read_csv(path: Path) -> list[dict]:
    with Path(path).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


class FirmListTests(unittest.TestCase):
    def test_keeps_financials_and_types_them(self):
        rows = [
            {"Symbol": "HIG", "Security": "Hartford (The)", "GICS Sector": "Financials",
             "GICS Sub-Industry": "Property & Casualty Insurance", "Date added": "1957-03-04", "CIK": "874766"},
            {"Symbol": "SCHW", "Security": "Charles Schwab Corporation", "GICS Sector": "Financials",
             "GICS Sub-Industry": "Investment Banking & Brokerage", "Date added": "1997-06-02", "CIK": "316709"},
            {"Symbol": "XYZ", "Security": "Block, Inc.", "GICS Sector": "Financials",
             "GICS Sub-Industry": "Transaction & Payment Processing Services", "Date added": "2025-07-23", "CIK": "1512673"},
            {"Symbol": "NEW", "Security": "Newco", "GICS Sector": "Financials",
             "GICS Sub-Industry": "Something New", "Date added": "", "CIK": "1"},
            {"Symbol": "MMM", "Security": "3M", "GICS Sector": "Industrials",
             "GICS Sub-Industry": "Industrial Conglomerates", "Date added": "1957-03-04", "CIK": "66740"},
        ]
        out = {r["ticker"]: r for r in make_firm_list.build(rows, "test list", "2026-11-05")}
        self.assertEqual(sorted(out), ["HIG", "NEW", "SCHW", "XYZ"])
        self.assertEqual(out["HIG"]["company"], "The Hartford")
        self.assertEqual(out["HIG"]["cik"], "0000874766")
        self.assertEqual(out["SCHW"]["company"], "Charles Schwab")  # first-run name, so the prompt matches
        self.assertEqual(out["SCHW"]["poc_firm"], "yes")
        self.assertEqual(out["XYZ"]["firm_type"], "payments_consumer_finance")
        self.assertEqual(out["NEW"]["firm_type"], "other")

    def test_committed_list(self):
        firms = read_csv(Path("data/processed/sec/sp500_financials/firms.csv"))
        self.assertGreaterEqual(len(firms), 70)
        self.assertEqual(len({f["ticker"] for f in firms}), len(firms))
        self.assertTrue(all(len(f["cik"]) == 10 and f["cik"].isdigit() for f in firms))
        self.assertTrue(all(f["firm_type"] in make_firm_list.FIRM_TYPE.values() for f in firms))
        self.assertEqual({f["ticker"] for f in firms if f["poc_firm"] == "yes"}, set(make_firm_list.POC_NAMES))


class AiPassagesTests(unittest.TestCase):
    def test_same_rules_as_first_run(self):
        paras = [("Item 1A. Risk Factors", "a.htm"), (AI_RISK, "a.htm"), ("AI", "a.htm"), (PLAIN, "a.htm"),
                 (AI_RISK, "b.htm"), (AI_USE, "b.htm")]
        out = dl.ai_passages(paras, "HIG_2025-12-31_10-K", "The Hartford", "HIG", "10-K", "2025-12-31", "2026-02-20",
                             "https://x/")
        self.assertEqual([p["passage_id"] for p in out], ["HIG_2025-12-31_10-K_00001", "HIG_2025-12-31_10-K_00005"])
        self.assertEqual(out[0]["section_guess"], "Item 1A. Risk Factors")
        self.assertEqual(out[1]["source_url"], "https://x/b.htm")   # the repeat in b.htm was dropped, not the new one
        self.assertEqual(out[1]["strength"], "strong")


class FakeSEC:
    """Serves a tiny EDGAR: one insurer (HIG) with two 10-Ks, one with an Exhibit 13, and its public float."""

    def __init__(self):
        self.calls = []
        acc24, acc25 = "0000874766-25-000010", "0000874766-26-000010"
        self.pages = {
            "https://data.sec.gov/submissions/CIK0000874766.json": {
                "name": "HARTFORD INSURANCE GROUP, INC.", "tickers": ["HIG"], "fiscalYearEnd": "1231",
                "filings": {"recent": {
                    "form": ["10-Q", "10-K", "10-K/A", "10-K", "10-K"],
                    "accessionNumber": ["0000874766-26-000020", acc25, "0000874766-25-000099", acc24, "0000874766-24-000010"],
                    "filingDate": ["2026-04-28", "2026-02-20", "2025-03-30", "2025-02-21", "2024-02-23"],
                    "reportDate": ["2026-03-31", "2025-12-31", "2024-12-31", "2024-12-31", "2023-12-31"],
                    "primaryDocument": ["hig-q1.htm", "hig-20251231.htm", "hig-a.htm", "hig-20241231.htm", "hig-2023.htm"]},
                    "files": []}},
            f"https://www.sec.gov/Archives/edgar/data/874766/{acc25.replace('-', '')}/{acc25}-index.htm":
                self.index([("hig-20251231.htm iXBRL", "10-K"), ("hig-ex13.htm", "EX-13"), ("hig-ex21.htm", "EX-21"),
                            ("hig-20251231_d2.htm", "GRAPHIC")]),
            f"https://www.sec.gov/Archives/edgar/data/874766/{acc25.replace('-', '')}/hig-20251231.htm": html(PLAIN, AI_RISK),
            f"https://www.sec.gov/Archives/edgar/data/874766/{acc25.replace('-', '')}/hig-ex13.htm": html(AI_USE),
            f"https://www.sec.gov/Archives/edgar/data/874766/{acc25.replace('-', '')}/hig-20251231_d2.htm": html(PLAIN),
            f"https://www.sec.gov/Archives/edgar/data/874766/{acc24.replace('-', '')}/{acc24}-index.htm":
                self.index([("hig-20241231.htm", "10-K")]),
            f"https://www.sec.gov/Archives/edgar/data/874766/{acc24.replace('-', '')}/hig-20241231.htm": html(AI_RISK, PLAIN),
            "https://data.sec.gov/api/xbrl/companyconcept/CIK0000874766/dei/EntityPublicFloat.json": {"units": {"USD": [
                {"end": "2024-06-30", "val": 29000000000, "accn": acc24, "fy": 2024, "fp": "FY", "form": "10-K", "filed": "2025-02-21"},
                {"end": "2025-06-30", "val": 35000000000, "accn": acc25, "fy": 2025, "fp": "FY", "form": "10-K", "filed": "2026-02-20"},
            ]}},
        }

    @staticmethod
    def index(rows):
        trs = "".join(f"<tr><td>{i}</td><td>doc</td><td><a href='x'>{n}</a></td><td>{t}</td><td>1</td></tr>"
                      for i, (n, t) in enumerate(rows, 1))
        return f"<table class='tableFile'><tr><th>Seq</th></tr>{trs}</table>"

    def get(self, url, as_json=False):
        self.calls.append(url)
        if url not in self.pages:
            raise RuntimeError(f"404 {url}")
        return self.pages[url]


class DownloaderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.firms = write_csv(self.tmp / "firms.csv", [
            {"ticker": "HIG", "company": "The Hartford", "cik": "0000874766", "gics_sub_industry": "Property & Casualty Insurance",
             "firm_type": "insurer", "poc_firm": "", "date_added": "", "source": "t", "source_date": "2026-11-05"},
            {"ticker": "BRK.B", "company": "Berkshire Hathaway", "cik": "0001067983", "gics_sub_industry": "Multi-Sector Holdings",
             "firm_type": "insurer", "poc_firm": "", "date_added": "", "source": "t", "source_date": "2026-11-05"}])
        self.fake = FakeSEC()
        self.real_get = dl.get
        dl.get = self.fake.get

    def tearDown(self):
        dl.get = self.real_get

    def run_once(self, corrections=None):
        out = self.tmp / "out"
        rc = download_sector.main([
            "--firms", str(self.firms), "--raw-dir", str(self.tmp / "raw"),
            "--float-corrections", str(corrections or self.tmp / "no_corrections.csv"),
            "--passages-out", str(out / "p.csv"), "--inventory-out", str(out / "inv.csv"),
            "--float-out", str(out / "fl.csv"), "--info-out", str(out / "info.json")])
        self.assertEqual(rc, 0)
        return (read_csv(out / "p.csv"), read_csv(out / "inv.csv"), read_csv(out / "fl.csv"),
                json.loads((out / "info.json").read_text(encoding="utf-8")))

    def test_end_to_end(self):
        passages, inv, floats, info = self.run_once()
        # 10-Ks for FY2024 and FY2025 only (not the 10-K/A, the 10-Q, or FY2023)
        self.assertEqual([(r["form"], r["fiscal_year"]) for r in inv], [("10-K", "2024"), ("10-K", "2025")])
        fy25 = inv[1]
        self.assertEqual(fy25["docs"], "hig-20251231.htm | hig-ex13.htm | hig-20251231_d2.htm")  # EX-13 + part, no EX-21
        self.assertEqual(fy25["ai_passages"], "2")
        self.assertEqual({p["passage_id"] for p in passages},
                         {"HIG_2024-12-31_10-K_00000", "HIG_2025-12-31_10-K_00001", "HIG_2025-12-31_10-K_00002"})
        use = [p for p in passages if p["passage"] == AI_USE][0]
        self.assertTrue(use["source_url"].endswith("/hig-ex13.htm"))
        self.assertEqual([(f["fiscal_year"], f["public_float_usd"], f["as_of"]) for f in floats],
                         [("2024", "29000000000", "2024-06-30"), ("2025", "35000000000", "2025-06-30")])
        # Berkshire's CIK isn't on the fake EDGAR: logged, run goes on
        self.assertTrue(any(p["ticker"] == "BRK.B" and p["where"] == "submissions" for p in info["problems"]))
        self.assertNotIn("@", info["user_agent"])

    def test_rerun_reads_saved_copies(self):
        first = self.run_once()
        self.fake.calls.clear()
        second = self.run_once()
        self.assertEqual(first[0], second[0])
        self.assertFalse([u for u in self.fake.calls if u.endswith(".htm")])  # no document downloaded again
        self.assertTrue(all(r["status"] == "ok (saved copy)" for r in second[1]))

    def test_float_corrections_applied_on_every_run(self):
        corr = write_csv(self.tmp / "corr.csv", [
            {"ticker": "HIG", "fiscal_year": "2024", "action": "correct", "public_float_usd": "30000000000",
             "as_of": "2024-06-30", "accession": "", "source": "cover page text", "note": "test"},
            {"ticker": "SPGI", "fiscal_year": "2024", "action": "correct", "public_float_usd": "1",
             "as_of": "2024-06-30", "accession": "", "source": "x", "note": "not in this run"}])
        floats, info = self.run_once(corr)[2], self.run_once(corr)[3]
        self.assertEqual([(f["ticker"], f["fiscal_year"], f["public_float_usd"]) for f in floats],
                         [("HIG", "2024", "30000000000"), ("HIG", "2025", "35000000000")])  # SPGI not added
        self.assertTrue(floats[0]["source"].startswith("correction: cover page text"))
        # each download starts from the tag again, so each run re-applies the correction (and logs it)
        self.assertEqual(len(info["public_float_corrections"]), 1)
        self.assertIn("HIG FY2024: tag 29,000,000,000 -> 30,000,000,000", info["public_float_corrections"][0])

    def test_ticker_check(self):
        self.fake.pages["https://data.sec.gov/submissions/CIK0000874766.json"]["tickers"] = ["XXX"]
        info = self.run_once()[3]
        self.assertTrue(any(p["ticker"] == "HIG" and p["where"] == "ticker check" for p in info["problems"]))


def make_passages(path: Path) -> Path:
    rows = []
    for t, co in (("HIG", "The Hartford"), ("V", "Visa")):
        for i, txt in enumerate((AI_USE, AI_RISK)):
            rows.append({"passage_id": f"{t}_2025-12-31_10-K_{i:05d}", "company": co, "ticker": t, "form": "10-K",
                         "period": "2025-12-31", "filing_date": "2026-02-20", "section_guess": "", "matched_terms": "ai",
                         "strength": "strong", "words": len(txt.split()), "passage": txt, "source_url": "https://x"})
    return write_csv(path, rows)


class BatchOptionsTests(unittest.TestCase):
    def test_passages_file_and_workers(self):
        tmp = Path(tempfile.mkdtemp())
        src = make_passages(tmp / "p.csv")
        before = config.PASSAGES
        try:
            outs = {}
            for w in (1, 3):
                rc = run_batch.main(["--passages", str(src), "--workers", str(w), "--labels-out", str(tmp / f"l{w}.csv"),
                                     "--scores-out", str(tmp / f"s{w}.csv"), "--run-info-out", str(tmp / f"i{w}.json")])
                self.assertEqual(rc, 0)
                outs[w] = [{k: v for k, v in r.items() if k != "run_at"} for r in read_csv(tmp / f"l{w}.csv")]
            self.assertEqual(outs[1], outs[3])  # same labels, same order
            self.assertEqual([r["passage_id"] for r in outs[3]], [r["passage_id"] for r in read_csv(src)])
            info = json.loads((tmp / "i3.json").read_text(encoding="utf-8"))
            self.assertEqual((info["workers"], info["passages"]), (3, 4))
            self.assertTrue(info["passages_file"].endswith("p.csv"))
        finally:
            config.PASSAGES = before

    def test_passages_needs_output_paths(self):
        with self.assertRaises(SystemExit):
            run_batch.main(["--passages", "x.csv"])


def run_folder(tmp: Path) -> Path:
    """A finished run in miniature: firms, inventory, labels, scores, floats."""
    d = tmp / "run"
    firms = []
    for t, ty, poc in (("JPM", "bank", "yes"), ("HIG", "insurer", ""), ("AFL", "insurer", ""), ("V", "payments_consumer_finance", ""),
                       ("CME", "exchange_data", ""), ("BLK", "asset_mgmt_broker", "")):
        firms.append({"ticker": t, "company": t, "cik": "0000000001", "gics_sub_industry": "x", "firm_type": ty,
                      "poc_firm": poc, "date_added": "", "source": "test list", "source_date": "2026-11-05"})
    write_csv(d / "firms.csv", firms)
    inv, labels, passages, floats = [], [], [], []
    for f in firms:
        t = f["ticker"]
        for fy in ("2024", "2025"):
            inv.append({"company": t, "ticker": t, "cik": "1", "firm_type": f["firm_type"], "form": "10-K",
                        "filing_date": "", "period": f"{fy}-12-31", "fiscal_year": fy, "accession": "", "primary_doc": "",
                        "docs": "", "html_bytes": 1, "paragraphs": 1, "ai_passages": 12, "url": "", "status": "ok"})
            floats.append({"ticker": t, "cik": "1", "fiscal_year": fy, "as_of": f"{fy}-06-30", "public_float_usd": 100,
                           "form": "10-K", "filed": "", "accession": "", "source": ""})
            for i in range(12):
                ev = "D1" if i < 3 else "P" if i == 3 else "X" if i == 4 else "N"
                pid = f"{t}_{fy}-12-31_10-K_{i:05d}"
                status = "needs_review" if i == 5 else "pass"
                labels.append({"passage_id": pid, "company": t, "ticker": t, "form": "10-K", "period": f"{fy}-12-31",
                               "topic_v0": "", "evidence_v0": ev, "scenarios_v0": "OPS" if ev in ("D1", "P") else "",
                               "coder": "", "coder_note": "", "source_url": "https://x", "quote": "q", "specific": "",
                               "confidence": "0.9", "flags": "", "evidence_raw": "D1" if status == "needs_review" else ev,
                               "scenarios_raw": "", "verify_status": status, "verify_reason": "", "model": "m",
                               "prompt_version": "classify-v1.5", "run_at": ""})
                passages.append({"passage_id": pid, "company": t, "ticker": t, "form": "10-K", "period": f"{fy}-12-31",
                                 "filing_date": "", "section_guess": "", "matched_terms": "ai", "strength": "strong",
                                 "words": 5, "passage": f"{t} {fy} passage {i} about AI.", "source_url": "https://x"})
    write_csv(d / "filings_inventory.csv", inv)
    write_csv(d / "public_float.csv", floats)
    write_csv(d / "agent_labels.csv", labels)
    write_csv(tmp / "passages.csv", passages)
    from src.index.score_companies import score
    write_csv(d / "agent_scores.csv", score(labels))
    (d / "agent_run_info.json").write_text(json.dumps({"model": "m", "prompt_version": "classify-v1.5", "workers": 6,
                                                       "usage": {"calls": 10, "prompt_tokens": 1_000_000,
                                                                 "cached_prompt_tokens": 800_000, "completion_tokens": 100_000}}))
    (d / "download_info.json").write_text(json.dumps({"forms": ["10-K"], "window": ["2024-01-01", "2025-12-31"],
                                                      "fiscal_year_end_not_december": {"BRO": "0119"},
                                                      "problems": [{"ticker": "AFL", "where": "public float", "problem": "x"}]}))
    return d


class FloatCorrectionTests(unittest.TestCase):
    def setUp(self):
        self.floats = [{"ticker": "A", "cik": "1", "fiscal_year": "2024", "as_of": "2024-06-30", "public_float_usd": "25500000000",
                        "form": "10-K", "filed": "2025-02-27", "accession": "a24", "source": "tag"},
                       {"ticker": "A", "cik": "1", "fiscal_year": "2025", "as_of": "2025-06-30", "public_float_usd": "326653262",
                        "form": "10-K", "filed": "2026-02-25", "accession": "a25", "source": "tag"},
                       {"ticker": "B", "cik": "2", "fiscal_year": "2024", "as_of": "2024-06-30", "public_float_usd": "50000000000",
                        "form": "10-K", "filed": "", "accession": "b24", "source": "tag"},
                       {"ticker": "B", "cik": "2", "fiscal_year": "2025", "as_of": "2025-06-30", "public_float_usd": "135000000000",
                        "form": "10-K", "filed": "", "accession": "b25", "source": "tag"}]
        self.inv = [{"ticker": "C", "fiscal_year": "2024", "form": "10-K", "cik": "3", "filing_date": "2025-02-11",
                     "accession": "c24"}]

    def test_check_flags_tiny_and_jumps(self):
        flags = float_corrections.check(self.floats)
        self.assertTrue(any(f.startswith("A FY2025") and "under $1B" in f for f in flags))
        self.assertTrue(any(f.startswith("B FY2025") for f in flags))           # x2.7
        keep = [{"ticker": "B", "fiscal_year": "2025", "action": "keep"}]
        self.assertFalse(any(f.startswith("B ") for f in float_corrections.check(self.floats, keep)))

    def test_apply_replaces_adds_and_is_idempotent(self):
        corr = [{"ticker": "A", "fiscal_year": "2025", "action": "correct", "public_float_usd": "32665326200",
                 "as_of": "2025-06-30", "accession": "", "source": "estimate", "note": ""},
                {"ticker": "C", "fiscal_year": "2024", "action": "correct", "public_float_usd": "139600000000",
                 "as_of": "2024-06-30", "accession": "", "source": "cover page", "note": ""},
                {"ticker": "B", "fiscal_year": "2025", "action": "keep", "public_float_usd": "", "as_of": "",
                 "accession": "", "source": "checked", "note": ""}]
        rows, done = float_corrections.apply(self.floats, corr, self.inv)
        got = {(r["ticker"], r["fiscal_year"]): r for r in rows}
        self.assertEqual(int(got[("A", "2025")]["public_float_usd"]), 32665326200)
        self.assertEqual(got[("A", "2025")]["accession"], "a25")                 # kept from the tagged row
        self.assertEqual((got[("C", "2024")]["accession"], got[("C", "2024")]["filed"]), ("c24", "2025-02-11"))
        self.assertEqual(got[("B", "2025")]["public_float_usd"], "135000000000")  # keep = unchanged
        self.assertEqual(len(done), 2)
        again, done2 = float_corrections.apply([{k: str(v) for k, v in r.items()} for r in rows], corr, self.inv)
        self.assertEqual(done2, [])


class ReportTests(unittest.TestCase):
    def test_report_and_review_queue(self):
        tmp = Path(tempfile.mkdtemp())
        d = run_folder(tmp)
        md, queue = sector_run_report.build(d, tmp / "passages.csv", today="2026-11-15")
        for heading in ("## Coverage by firm type", "## Agent labels by firm type", "## AI Use Scores by firm type",
                        "## Sector index preview", "## Run facts"):
            self.assertIn(heading, md)
        self.assertEqual(len(queue), 12)                      # one held label per firm-year
        self.assertTrue(all(q["passage"] for q in queue))
        self.assertIn("about **$0.09**", md)                  # 0.8M x 0.003 + 0.2M x 0.15 + 0.1M x 0.60 = $0.092
        self.assertIn("AFL [public float]", md)
        self.assertNotIn("Fiscal years not ending in December", md)  # from the periods, not SEC's fiscalYearEnd
        self.assertIn("· enablers:", md)


    def test_run_facts_cover_every_pass(self):
        tmp = Path(tempfile.mkdtemp())
        d = run_folder(tmp)
        same = {"model": "m", "prompt_version": "classify-v1.5", "passages": 24, "workers": 6}
        first = {**same, "run_at": "r1", "wall_seconds": 100.0,
                 "usage": {"calls": 10, "cache_hits": 0, "prompt_tokens": 1_000_000, "cached_prompt_tokens": 800_000,
                           "completion_tokens": 100_000, "truncated": 2}}
        last = {**same, "run_at": "r2", "wall_seconds": 20.0,
                "usage": {"calls": 2, "cache_hits": 10, "prompt_tokens": 1_000_000, "cached_prompt_tokens": 0,
                          "completion_tokens": 100_000, "truncated": 0}}
        (d / "agent_run_info.json").write_text(json.dumps(run_batch.add_earlier_passes(last, first)))
        md, _ = sector_run_report.build(d, tmp / "passages.csv", today="2026-11-15")
        self.assertIn("24 passages in 2 passes", md)
        self.assertIn("12 model calls and 120.0 s in all", md)
        self.assertIn("2 in earlier passes (retried), 0 in the last", md)
        self.assertIn("Pass 1, run r1: 10 new model calls", md)
        self.assertIn("about **$0.30**", md)  # both passes: $0.092 + 1M x 0.15 + 0.1M x 0.60 = $0.302


class PilotSampleTests(unittest.TestCase):
    def test_blind_sample_per_new_type(self):
        tmp = Path(tempfile.mkdtemp())
        d = run_folder(tmp)
        sample, key = pilot.build(read_csv(d / "firms.csv"), read_csv(tmp / "passages.csv"), read_csv(d / "agent_labels.csv"))
        types = {k["firm_type"] for k in key}
        self.assertEqual(types, set(pilot.NEW_TYPES))         # banks (JPM) left out
        self.assertNotIn("JPM", {k["ticker"] for k in key})
        self.assertNotIn("X", {k["evidence_v0"] for k in key})
        for t in pilot.NEW_TYPES:
            ks = [k for k in key if k["firm_type"] == t]
            self.assertLessEqual(len(ks), pilot.PER_TYPE)
            for tk in {k["ticker"] for k in ks}:
                self.assertLessEqual(sum(k["ticker"] == tk for k in ks), pilot.MAX_PER_FIRM)
        self.assertEqual(set(sample[0]), set(pilot.SAMPLE_FIELDS))   # no label columns for raters
        again = pilot.build(read_csv(d / "firms.csv"), read_csv(tmp / "passages.csv"), read_csv(d / "agent_labels.csv"))
        self.assertEqual(sample, again[0])                    # fixed seed


if __name__ == "__main__":
    unittest.main()
