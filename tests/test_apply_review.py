"""Tests for the human-review step (#170): apply_review and keeping reviews across report reruns.

Run from the repo root:  python3 -m unittest tests.test_apply_review -v
"""
import csv
import tempfile
import unittest
from pathlib import Path

from src.index import apply_review, sector_run_report


def lab(pid, ev="N", scen="", status="pass", ticker="AAA", period="2025-12-31"):
    return {"passage_id": pid, "company": "Alpha", "ticker": ticker, "form": "10-K", "period": period,
            "evidence_v0": ev, "scenarios_v0": scen, "verify_status": status, "verify_reason": "ok",
            "coder": "agent", "coder_note": ""}


def rev(pid, ev="", scen="", who="Shu", note=""):
    return {"passage_id": pid, "review_evidence": ev, "review_scenarios": scen, "reviewer": who, "review_note": note}


class ApplyReviewTest(unittest.TestCase):
    def setUp(self):
        self.labels = [lab("p1", "D1", "OPS"),
                       lab("p2", status="needs_review"),
                       lab("p3", status="needs_review"),
                       lab("p4", status="needs_review")]

    def test_valid_review_changes_label_and_score(self):
        out, counts, problems = apply_review.apply(self.labels, [rev("p2", "D2", "FRAUD", note="named tool")])
        self.assertEqual(problems, [])
        self.assertEqual(counts, {"held": 3, "reviewed": 1, "still_held": 2})
        p2 = next(r for r in out if r["passage_id"] == "p2")
        self.assertEqual((p2["evidence_v0"], p2["scenarios_v0"], p2["verify_status"], p2["coder"]),
                         ("D2", "FRAUD", "human_reviewed", "Shu"))
        before = apply_review.score(self.labels)[0]["ai_use_score"]
        after = apply_review.score(out)[0]["ai_use_score"]
        self.assertGreater(after, before)

    def test_blank_review_leaves_label_held(self):
        out, counts, problems = apply_review.apply(self.labels, [rev("p2"), rev("p3", who="")])
        self.assertEqual(out, self.labels)
        self.assertEqual(counts["reviewed"], 0)
        self.assertEqual(problems, [])

    def test_invalid_reviews_are_reported_not_applied(self):
        queue = [rev("p2", "D3", "OPS"), rev("p3", "D1", ""), rev("p4", "N", "OPS"), rev("zz", "N")]
        out, counts, problems = apply_review.apply(self.labels, queue)
        self.assertEqual(out, self.labels)
        self.assertEqual(counts["reviewed"], 0)
        self.assertEqual(len(problems), 4)
        self.assertTrue(any("needs at least one area" in p for p in problems))
        self.assertTrue(any("not in the labels file" in p for p in problems))

    def test_missing_reviewer_is_a_problem(self):
        _, counts, problems = apply_review.apply(self.labels, [rev("p2", "N", "", who=" ")])
        self.assertEqual(counts["reviewed"], 0)
        self.assertIn("reviewer name missing", problems[0])

    def test_only_held_rows_can_be_overridden(self):
        out, counts, _ = apply_review.apply(self.labels, [rev("p1", "N", "")])
        self.assertEqual(out[0]["evidence_v0"], "D1")
        self.assertEqual(counts["reviewed"], 0)

    def test_main_never_overwrites_agent_labels(self):
        d = Path(tempfile.mkdtemp())
        p = d / "labels.csv"
        apply_review.write(p, self.labels)
        apply_review.write(d / "q.csv", [rev("p2", "P", "OPS")])
        self.assertEqual(apply_review.main(["--labels", str(p), "--queue", str(d / "q.csv"),
                                            "--labels-out", str(p), "--scores-out", str(d / "s.csv")]), 2)
        rc = apply_review.main(["--labels", str(p), "--queue", str(d / "q.csv"),
                                "--labels-out", str(d / "out.csv"), "--scores-out", str(d / "s.csv")])
        self.assertEqual(rc, 0)
        self.assertEqual(apply_review.read(p), self.labels)
        self.assertEqual(apply_review.read(d / "out.csv")[1]["verify_status"], "human_reviewed")


class KeepReviewsTest(unittest.TestCase):
    def test_report_rerun_keeps_filled_reviews(self):
        d = Path(tempfile.mkdtemp())
        path = d / "review_queue.csv"
        with path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=sector_run_report.REVIEW_FIELDS, extrasaction="ignore")
            w.writeheader()
            w.writerow({"passage_id": "p2", "review_evidence": "D1", "review_scenarios": "OPS",
                        "reviewer": "Yen-Chu", "review_note": "clear use"})
        fresh = [{"passage_id": "p2", "review_evidence": "", "review_scenarios": "", "reviewer": "", "review_note": ""},
                 {"passage_id": "p9", "review_evidence": "", "review_scenarios": "", "reviewer": "", "review_note": ""}]
        kept = sector_run_report.keep_reviews(fresh, path)
        self.assertEqual((kept[0]["review_evidence"], kept[0]["reviewer"]), ("D1", "Yen-Chu"))
        self.assertEqual(kept[1]["review_evidence"], "")

    def test_no_existing_file(self):
        q = [{"passage_id": "p1", "review_evidence": ""}]
        self.assertEqual(sector_run_report.keep_reviews(q, Path(tempfile.mkdtemp()) / "none.csv"), q)


if __name__ == "__main__":
    unittest.main()
