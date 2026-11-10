import unittest

from src.index.sector_index import build


class SectorIndexTest(unittest.TestCase):
    def test_ew_cw_and_missing_rules(self):
        scores = [{"ticker": "A", "fiscal_year": "2025", "ai_use_score": "30"},
                  {"ticker": "B", "fiscal_year": "2025", "ai_use_score": "10"}]
        floats = [{"ticker": t, "fiscal_year": "2025", "public_float_usd": v} for t, v in (("A", "500"), ("B", "200"), ("C", "100"))]
        floats.append({"ticker": "A", "fiscal_year": "2024", "public_float_usd": "400"})
        inventory = [{"ticker": t, "period": "2025-12-31", "form": "10-K"} for t in "ABC"]
        inventory.append({"ticker": "A", "period": "2024-12-31", "form": "10-K"})
        index, firms = build(scores, floats, inventory)
        self.assertEqual([r["fiscal_year"] for r in index], ["2025"])   # 2024 not scored at all -> skipped
        r = index[0]
        self.assertEqual(r["n_firms"], 3)                                # C has a 10-K but no AI passage -> 0
        self.assertEqual(r["ai_ew"], round(40 / 3, 1))
        self.assertEqual(r["ai_cw"], round((30 * 500 + 10 * 200) / 800, 1))
        self.assertAlmostEqual(sum(f["cw_weight_pct"] for f in firms), 100.0)


if __name__ == "__main__":
    unittest.main()
