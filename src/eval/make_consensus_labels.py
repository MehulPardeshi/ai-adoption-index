"""Build the human consensus labels from rounds 1 and 2, and a label file for check 4.

Consensus = the raters' own labels: passages where all three gave the same evidence level keep it
(scenarios: those at least 2 of 3 raters chose); evidence disagreements take the labels the three
raters agreed on Nov 7 (adjudication sheet, "Sorted for meeting" tab). No AI labels.

Outputs:
  docs/part3-metrics/adjudication/consensus_labels.csv     the 80 human-labeled passages
  docs/part3-metrics/adjudication/labels_v0_plus_consensus.csv
      the v0 draft labels with these 80 replaced by the consensus, for
      python3 -m src.eval.check4_sensitivity --labels <that file>
Run from the repo root:  python3 -m src.eval.make_consensus_labels
"""
import csv
from pathlib import Path

from openpyxl import load_workbook

from src.nlp.taxonomy_v0 import LABELS

BASE = Path("docs/part3-metrics")
ADJ = BASE / "adjudication"
SHEET = ADJ / "adjudication_sorted_yenchu.xlsx"
RATERS = ["logan", "snehal", "yenchu"]
NEEDS_SCENARIO = {"D2", "D1", "P"}


def read(path: Path) -> list:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def norm(s) -> str:
    return ";".join(sorted({x.strip() for x in str(s or "").replace(",", ";").split(";") if x.strip()}))


def main() -> None:
    ws = load_workbook(SHEET, data_only=True)["Sorted for meeting"]
    rows = list(ws.iter_rows(values_only=True))
    head = rows[0]
    agreed = {r[head.index("passage_id")]: (r[head.index("agreed_evidence")], norm(r[head.index("agreed_scenarios")]))
              for r in rows[1:] if r[head.index("passage_id")]}

    out = []
    for rnd in (1, 2):
        folder = BASE / f"labeling_round_{rnd}"
        raters = {name: {r["passage_id"]: r for r in read(folder / f"rater_{name}.csv")} for name in RATERS}
        for pid in raters["logan"]:
            if pid in agreed:
                ev, sc = agreed[pid]
                source = "adjudicated Nov 7"
            else:
                evs = {raters[n][pid]["evidence"] for n in RATERS}
                if len(evs) != 1:
                    raise SystemExit(f"{pid}: raters differ on evidence but it isn't on the adjudication sheet")
                ev = evs.pop()
                # The sheet lists evidence disagreements only. Scenarios: keep each one at least 2 of 3 raters chose.
                votes = [s for n in RATERS for s in norm(raters[n][pid]["scenarios"]).split(";") if s]
                sc = ";".join(sorted(s for s in set(votes) if votes.count(s) >= 2))
                source = "unanimous" if len({norm(raters[n][pid]["scenarios"]) for n in RATERS}) == 1 \
                    else "unanimous evidence, scenarios by 2-of-3"
            out.append({"passage_id": pid, "round": rnd, "evidence": ev, "scenarios": sc, "source": source,
                        "scenario_missing": "yes" if ev in NEEDS_SCENARIO and not sc else ""})

    with (ADJ / "consensus_labels.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)

    cons = {r["passage_id"]: r for r in out}
    labels = read(LABELS)
    replaced = 0
    for r in labels:
        c = cons.get(r["passage_id"])
        if c:
            r["evidence_v0"], r["scenarios_v0"] = c["evidence"], c["scenarios"]
            r["coder"], r["coder_note"] = f"human consensus ({c['source']})", ""
            replaced += 1
    with (ADJ / "labels_v0_plus_consensus.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(labels[0]))
        w.writeheader()
        w.writerows(labels)

    missing = [r["passage_id"] for r in out if r["scenario_missing"]]
    print(f"{len(out)} consensus passages ({sum(r['source'] == 'unanimous' for r in out)} unanimous, "
          f"{sum(r['source'].startswith('unanimous evidence') for r in out)} same evidence with scenarios by 2-of-3, "
          f"{len(agreed)} adjudicated); {replaced} replaced in the v0 labels.")
    print(f"Scenario still missing for {len(missing)}: {', '.join(missing)}")


if __name__ == "__main__":
    main()
