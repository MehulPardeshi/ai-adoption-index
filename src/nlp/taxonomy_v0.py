"""Taxonomy v0 codebook + label checker (DRAFT - not team-approved yet).

Proposed by Yen-Chu from the SEC test run; see
docs/part2-taxonomy/sec_test_run_taxonomy_v0_DRAFT.md. The use-case scenario
list is the merge point for Shu's list. Nothing here is final until the team
votes and logs it in memory/09-decisions-log.md.

Check the draft labels (AI-assisted, see
data/processed/sec/passage_labels_v0.csv) against the extracted passages (run from repo root):
    python3 -m src.nlp.taxonomy_v0
"""
import csv
import sys
from pathlib import Path

PASSAGES = Path("data/interim/sec/ai_passages.csv")
LABELS = Path("data/processed/sec/passage_labels_v0.csv")

# Label A: where AI is used (only for passages with evidence D2 / D1 / P)
SCENARIOS = {
    "CX": "Customer service and digital assistants",
    "ADV": "Advice, wealth and retirement guidance",
    "CREDIT": "Credit decisions, underwriting and pricing",
    "RISKM": "Risk and finance models",
    "FRAUD": "Fraud and financial crime (AML, KYC)",
    "SURV": "Compliance and trade surveillance",
    "CYBER": "Cyber defense",
    "DEV": "Software engineering",
    "PROD": "Employee productivity and knowledge tools",
    "OPS": "Operations, data and regulatory reporting",
    "MKT": "Markets and trading",
}
OTHER_SCENARIOS = {"ENT": "Enterprise-wide, area not named"}
ENABLERS = {
    "GOV": "AI governance and leadership",
    "TALENT": "AI training and talent",
    "INVEST": "AI investment and M&A",
}
ALL_SCENARIOS = {**SCENARIOS, **OTHER_SCENARIOS, **ENABLERS}

# Label B: is it real use or just talk?
EVIDENCE = {
    "D2": "Deployed, specific: names a tool, use case, metric, body, role or date",
    "D1": "Deployed, general: says the company uses/governs AI, no specifics",
    "P": "Planned: the company says it intends or expects to use AI",
    "N": "No evidence of own use: risk, threat, trend or regulation talk",
    "X": "Not substantive: definition, acronym list, heading",
}
EVIDENCE_WEIGHT = {"D2": 3.0, "D1": 1.0, "P": 0.5, "N": 0.0}

# Label C: what the passage is about (context for a risk view)
TOPICS = {
    "USE": "The company describes using AI in its business",
    "GOV": "AI oversight: committees, policies, model-risk review, AI roles",
    "WORK": "AI training, skills, displacement, hiring",
    "RISK-OWN": "Risk from the company's own or vendors' AI going wrong",
    "THREAT": "Outsiders using AI against the company (cyber, fraud, deepfakes)",
    "COMP": "Competitors or new entrants using AI; disintermediation",
    "REG": "AI laws and compliance",
    "MACRO": "AI as a credit or sector risk",
    "DEAL": "AI-related acquisition or investment",
    "BOILER": "AI only named inside a generic list",
    "DEF": "Definition, acronym list or heading",
}


def read(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def check_labels(passages_path=PASSAGES, labels_path=LABELS):
    """Return a list of problems (empty = labels are complete and valid)."""
    problems = []
    labels = read(labels_path)
    for r in labels:
        pid = r["passage_id"]
        if r["topic_v0"] not in TOPICS:
            problems.append(f"{pid}: unknown topic {r['topic_v0']!r}")
        if r["evidence_v0"] not in EVIDENCE:
            problems.append(f"{pid}: unknown evidence level {r['evidence_v0']!r}")
        scen = [s for s in r["scenarios_v0"].split(";") if s]
        for s in scen:
            if s not in ALL_SCENARIOS:
                problems.append(f"{pid}: unknown scenario {s!r}")
        shows_use = r["evidence_v0"] in ("D2", "D1", "P")
        if shows_use and not scen:
            problems.append(f"{pid}: {r['evidence_v0']} needs at least one scenario")
        if not shows_use and scen:
            problems.append(f"{pid}: {r['evidence_v0']} should have no scenario")
    if Path(passages_path).exists():
        labeled = {r["passage_id"] for r in labels}
        passage_ids = {r["passage_id"] for r in read(passages_path)}
        for pid in sorted(passage_ids - labeled):
            problems.append(f"{pid}: passage has no label yet")
        for pid in sorted(labeled - passage_ids):
            problems.append(f"{pid}: label has no matching passage (rerun the download?)")
    return problems


if __name__ == "__main__":
    found = check_labels()
    for p in found:
        print(p)
    print(f"{len(found)} problem(s)")
    sys.exit(1 if found else 0)
