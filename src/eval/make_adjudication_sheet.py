"""Build the adjudication workbook: every round 1 and round 2 passage the raters disagreed on.

Shows each rater's labels and the passage text; the agreed columns are left blank for the raters.
No draft or agent labels, so they don't anchor the discussion.
Run from the repo root:  python3 -m src.eval.make_adjudication_sheet
"""
import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

BASE = Path("docs/part3-metrics")
RATERS = ["logan", "snehal", "yenchu"]
HEAD = ["round", "passage_id", "company", "form", "period", "passage", "source_url",
        *[f"{r}_{k}" for r in RATERS for k in ("evidence", "scenarios")],
        "agreed_evidence", "agreed_scenarios", "note"]


def read(path: Path) -> list:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    ws = Workbook().active
    ws.title = "Agree here"
    ws.append(HEAD)
    for round_no in (1, 2):
        folder = BASE / f"labeling_round_{round_no}"
        text = {r["passage_id"]: r for r in read(folder / "sample_passages.csv")}
        for d in read(folder / "disagreements.csv"):
            t = text[d["passage_id"]]
            ws.append([round_no, d["passage_id"], t["company"], t["form"], t["period"], t["passage"], t["source_url"],
                       *[d[f"{r}_{k}"] for r in RATERS for k in ("evidence", "scenarios")], "", "", ""])
    for c in ws[1]:
        c.font = Font(bold=True)
    for row in ws.iter_rows(min_row=2):
        row[5].alignment = Alignment(wrap_text=True, vertical="top")
        for c in row[-3:]:
            c.fill = PatternFill("solid", fgColor="FFF2CC")
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["F"].width = 90
    ws.freeze_panes = "C2"
    out = BASE / "adjudication" / "adjudication_sheet.xlsx"
    out.parent.mkdir(exist_ok=True)
    ws.parent.save(out)
    print(f"{ws.max_row - 1} passages -> {out}")


if __name__ == "__main__":
    main()
