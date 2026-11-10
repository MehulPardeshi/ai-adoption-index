"""Tests for check 3 against the agreed labels (offline, synthetic data).

Run from the repo root:  python3 -m unittest discover -s tests -v
"""
import csv
import tempfile
import unittest
from pathlib import Path

from src.eval import check3_consensus as c3

AGENT_HEADER = ["passage_id", "evidence_v0", "scenarios_v0", "confidence", "verify_status", "evidence_raw",
                "quote", "model", "prompt_version", "run_at"]


def write(path: Path, header: list[str], rows: list[list[str]]) -> Path:
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    return path


class Check3ConsensusTests(unittest.TestCase):
    def setUp(self):
        d = Path(tempfile.mkdtemp())
        self.consensus = c3.load_consensus(write(d / "cons.csv", ["passage_id", "round", "evidence", "scenarios", "source",
                                                                   "scenario_missing"], [
            ["A", "1", "D1", "ENT", "x", ""],     # agent D1 ENT: exact
            ["B", "1", "N", "", "x", ""],         # agent D1: overclaim
            ["C", "1", "D1", "RISKM", "x", ""],   # agent D2: level differs, not an overclaim
            ["D", "2", "D1", "OPS", "x", ""],     # agent N: underclaim
            ["E", "2", "N", "", "x", ""],         # held at N; model said D1: guardrail stopped an overclaim
            ["F", "2", "N", "", "x", ""],         # agent P: level differs (P is not use)
        ]))
        rows = [["A", "D1", "ENT", "0.8", "pass", "D1", "q", "m", "v1.5", "2026-10-27T10:00:00"],
                ["B", "D1", "ENT", "0.8", "pass", "D1", "q", "m", "v1.5", "2026-10-27T10:00:00"],
                ["C", "D2", "RISKM", "0.9", "pass", "D2", "q", "m", "v1.5", "2026-10-27T10:00:00"]]
        self.r1 = write(d / "r1.csv", AGENT_HEADER, rows)
        rows2 = [["D", "N", "", "0.8", "pass", "N", "q", "m", "v1.5", "2026-11-09T18:00:00"],
                 ["E", "N", "", "0.6", "needs_review", "D1", "q", "m", "v1.5", "2026-11-09T18:00:00"],
                 ["F", "P", "ENT", "0.7", "pass", "P", "q", "m", "v1.5", "2026-11-09T18:00:00"]]
        self.r2 = write(d / "r2.csv", AGENT_HEADER, rows2)
        self.missing = d / "nope.csv"

    def test_kinds_follow_irr_definitions(self):
        self.assertEqual(c3.kind_of("D1", "N"), "overclaim")
        self.assertEqual(c3.kind_of("D2", "D1"), "level differs")
        self.assertEqual(c3.kind_of("P", "N"), "level differs")
        self.assertEqual(c3.kind_of("N", "D1"), "underclaim")

    def test_compare_counts(self):
        agent, _ = c3.load_labels([self.r1, self.r2])
        m = c3.compare(list("ABCDEF"), agent, self.consensus)
        self.assertEqual((m["n"], m["exact"]), (6, 2))  # A, and E (held at N, agreed N)
        self.assertEqual(m["over"], ["B"])
        self.assertEqual(m["under"], ["D"])
        self.assertEqual(m["over_raw"], ["B", "E"])   # without the guardrail, E is an overclaim too
        self.assertEqual(m["held"], ["E"])

    def test_perfect_agreement_kappa_is_one(self):
        agent, _ = c3.load_labels([self.r1])
        m = c3.compare(["A"], agent, self.consensus)
        self.assertEqual((m["exact"], m["kappa"]), (1, 1.0))

    def test_report_marks_missing_round_and_splits_tuning(self):
        agent, found = c3.load_labels([self.r1, self.missing])
        self.assertEqual(found, [self.r1])
        md, diffs = c3.build(self.consensus, agent, tuning={"C"}, draft={}, agent_files=found, run_infos=[],
                             today="2026-11-09")
        self.assertIn("| Round 2 | 3 | *not run yet* |", md)
        self.assertIn("Round 1, **unseen**", md)
        self.assertEqual({d["passage_id"]: (d["kind"], d["set"]) for d in diffs},
                         {"B": ("overclaim", "unseen"), "C": ("level differs", "tuning")})

    def test_report_with_both_rounds(self):
        agent, found = c3.load_labels([self.r1, self.r2])
        info = {"labels_file": "r2.csv", "passages": 3, "usage": {"calls": 2, "cache_hits": 1}, "wall_seconds": 5.0}
        md, diffs = c3.build(self.consensus, agent, tuning=set(), draft={}, agent_files=found, run_infos=[info],
                             today="2026-11-09")
        self.assertIn("**All rounds, unseen**", md)
        self.assertIn("stopped an overclaim", md)
        self.assertIn("2 new model calls", md)
        self.assertEqual([d["passage_id"] for d in diffs], ["B", "D", "C", "F"])  # overclaims, underclaims, then level


if __name__ == "__main__":
    unittest.main()
