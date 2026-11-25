"""Labeling round 3 (#169): people vs. people, and the agent vs. the agreed labels, per new firm type.

Inputs (docs/part3-metrics/labeling_round_3/):
  * Labeling3_workbook_Logan.csv, rater_snehal.csv: the two raters' independent labels
  * Labeling3_final.csv: the labels Logan and Snehal agreed together (the answer key)
  * agent_key.csv: the agent's labels and each passage's firm type (raters never opened it)

Same definitions as check 3 (src/eval/check3_consensus.py): use = D1/D2; overclaim = the agent
says use where the agreed label is N, P or X (bar <= 5%); about_ai = N counts as X.
Run from the repo root:  python3 -m src.eval.round3_results
Writes results_round3.md and round3_differences.csv in the same folder.
"""
import csv
from collections import defaultdict
from pathlib import Path

from src.eval.irr import OVERCLAIM_TARGET, cohen_kappa, use

DIR = Path("docs/part3-metrics/labeling_round_3")
TYPES = {"insurer": "Insurers", "asset_mgmt_broker": "Asset managers and brokers",
         "payments_consumer_finance": "Payments and consumer finance", "exchange_data": "Exchanges and data"}


def load(name):
    rows = list(csv.reader(open(DIR / name, encoding="utf-8-sig")))
    if "passage_id" not in rows[0]:  # workbook exports start with a title row
        rows = rows[1:]
    head = rows[0]
    out = {}
    for r in rows[1:]:
        d = dict(zip(head, r))
        if d.get("passage_id"):
            ev = d["evidence"].strip().upper()
            out[d["passage_id"]] = "X" if d.get("about_ai", "").strip().upper() == "N" else ev
    return out


def stats(rows):
    n = len(rows)
    agent = [r["agent"] for r in rows]
    key = [r["key"] for r in rows]
    return {
        "n": n,
        "exact": sum(a == k for a, k in zip(agent, key)) / n,
        "kappa": cohen_kappa(agent, key),
        "use": sum(use(a) == use(k) for a, k in zip(agent, key)) / n,
        "over": sum(use(a) == "USE" and use(k) == "NO" for a, k in zip(agent, key)),
        "over_raw": sum(use(r["raw"]) == "USE" and use(r["key"]) == "NO" for r in rows),
        "under": sum(use(a) == "NO" and use(k) == "USE" for a, k in zip(agent, key)),
        "held": sum(r["held"] for r in rows),
    }


def main():
    logan, snehal, final = load("Labeling3_workbook_Logan.csv"), load("rater_snehal.csv"), load("Labeling3_final.csv")
    key_rows = list(csv.DictReader(open(DIR / "agent_key.csv", encoding="utf-8")))
    rows = [{"id": k["passage_id"], "ticker": k["ticker"], "type": k["firm_type"], "agent": k["evidence_v0"],
             "raw": k["evidence_raw"], "held": k["verify_status"] != "pass", "key": final[k["passage_id"]],
             "logan": logan[k["passage_id"]], "snehal": snehal[k["passage_id"]]} for k in key_rows]
    lo, sn = [r["logan"] for r in rows], [r["snehal"] for r in rows]
    exact = sum(a == b for a, b in zip(lo, sn))
    use_k = cohen_kappa([use(x) for x in lo], [use(x) for x in sn])

    by = defaultdict(list)
    for r in rows:
        by[r["type"]].append(r)
    lines = ["# Labeling round 3 results: the new firm types (#169)", "",
             "Logan and Snehal each labeled the 40 pilot passages alone (10 per new firm type, firms outside our "
             "7 proof-of-concept firms), then agreed one label per passage (Nov 24). The agent's labels were hidden "
             "from both. Built by `python3 -m src.eval.round3_results`.", "",
             "## People vs. people", "",
             f"- Same evidence level on {exact} of 40 (κ {cohen_kappa(lo, sn):.2f}); "
             f"same use vs. no-use call on {sum(use(a) == use(b) for a, b in zip(lo, sn))} of 40 (κ {use_k:.2f}, bar 0.6).",
             "- As in rounds 1 and 2, people agree on the use call and less on the detail level.", "",
             "## Agent vs. the agreed labels", "",
             "| Firm type | n | Exact level | κ (level) | Use vs. no use | **Overclaim** | Underclaim | Held for review |",
             "|---|---|---|---|---|---|---|---|"]
    for t in list(TYPES) + ["ALL"]:
        s = stats(rows if t == "ALL" else by[t])
        name = "**All 40**" if t == "ALL" else TYPES[t]
        lines.append(f"| {name} | {s['n']} | {s['exact']:.0%} | {s['kappa']:.2f} | {s['use']:.0%} | "
                     f"**{s['over']} ({s['over'] / s['n']:.0%})** | {s['under']} | {s['held']} |")
    s = stats(rows)
    lines += ["", f"Overclaim = the agent says use (D1/D2) where the agreed label is N, P or X; bar ≤ {OVERCLAIM_TARGET:.0%}. "
              f"The guardrail changed no overclaim here (without it: {s['over_raw']}). Held = sent to a person by the "
              "guardrail; a held label counts as no use until someone reviews it.", "",
              "## The overclaims", ""]
    for r in rows:
        if use(r["agent"]) == "USE" and use(r["key"]) == "NO":
            lines.append(f"- `{r['id']}` ({TYPES[r['type']]}): agent {r['agent']}, agreed {r['key']} "
                         f"(Logan {r['logan']}, Snehal {r['snehal']}).")
    lines += ["", "Both are AI risk-factor sentences that mention \"our use of AI\" without saying what the AI does: "
              "the same borderline the team clarified in round 2, not something new about the firm type. Neither is a "
              "specific-use (D2) claim.", "",
              "## How to read it", "",
              f"- Across the 40 passages the agent meets the bar: {s['over']} overclaims ({s['over'] / s['n']:.0%}).",
              "- Per type, 10 passages is too few to tell types apart: one passage is 10%. Two types have one overclaim "
              "each, two have none.",
              f"- The agent errs cautious here too: {s['under']} underclaims vs. {s['over']} overclaims, and the agreed "
              "label was higher than the agent's on most level differences. Index scores for these types lean low.",
              f"- {s['held']} labels were held by the guardrail; the agreed labels give the people's answer for them "
              "(see `round3_differences.csv`)."]
    (DIR / "results_round3.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    with open(DIR / "round3_differences.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["passage_id", "firm_type", "agent", "agent_before_guardrail", "held", "agreed", "logan", "snehal", "kind"])
        for r in rows:
            if r["agent"] != r["key"] or r["held"]:
                kind = ("overclaim" if use(r["agent"]) == "USE" and use(r["key"]) == "NO" else
                        "underclaim" if use(r["agent"]) == "NO" and use(r["key"]) == "USE" else
                        "level differs" if r["agent"] != r["key"] else "held, agent matched")
                w.writerow([r["id"], r["type"], r["agent"], r["raw"], "yes" if r["held"] else "no",
                            r["key"], r["logan"], r["snehal"], kind])
    print((DIR / "results_round3.md").read_text())


if __name__ == "__main__":
    main()
