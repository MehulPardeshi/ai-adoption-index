"""Evaluation check 6 (course requirement #7): run Mehul's red-team cases with and without guardrails.

    python3 -m src.agent.redteam                 # all 20 cases, both modes
    python3 -m src.agent.redteam --cases RT01,RT08

Routing per case (from guardrail_redteam_cases.csv):
  - "Model output to verify: {...}"   -> verify_label only (RT08, RT09); off = the claim passes unchecked
  - "Classify this passage[ for X].", "Passage: '...'", "Transcript excerpt: '...'"
                                      -> classify_passage (+ verify_label when on)
  - any other request                 -> chat agent, with the passage attached when there is one
Writes data/processed/agent/redteam_results_v1.csv. Judging pass/fail against
expected_with_guardrails is done by the team (Mehul), not by this script.
"""
import argparse
import json
import re

from src.agent import chat, config, llm, store, tools

FIELDS = ["case_id", "category", "mode", "route", "evidence_raw", "evidence", "scenarios", "quote",
          "verify_status", "verify_reason", "flags", "answer", "expected_with_guardrails", "model"]


def _quoted(s: str, key: str) -> str | None:
    m = re.search(key + r"\s*'(.+?)'(?:\s|$|\.|\])", s, re.S)
    return m.group(1) if m else None


def parse_case(c: dict) -> dict:
    """Turn one CSV row into a runnable input: passage text, request, optional model output to verify."""
    inp = c["input"]
    rec = store.get_passage(c["passage_id"]) if c["passage_id"] else None
    text = rec["passage"] if rec else (_quoted(inp, "Passage:") or _quoted(inp, "Transcript excerpt:"))
    if rec and "real+injection" in c["input_type"]:
        inj = re.search(r"appended line:\]\s*'(.+)'", inp)
        text = rec["passage"] + "\n" + (inj.group(1) if inj else "")
    claim = None
    m = re.search(r"Model output to verify:\s*\{evidence:\s*(\w+),\s*quote:\s*'(.+?)'\}", inp)
    if m:
        claim = {"evidence": m.group(1), "scenarios": ["ENT"] if m.group(1) != "N" else [], "topic": "USE",
                 "quote": m.group(2), "specific": m.group(2) if m.group(1) == "D2" else None, "confidence": 0.9}
    who = re.search(r"Classify this passage for (.+?)\.", inp)
    return {"text": text, "company": rec["company"] if rec else "Example Bank", "passage_id": c["passage_id"] or None,
            "request": inp, "claim": claim, "requested_company": who.group(1) if who else None,
            "classify_only": inp.strip().startswith(("Classify this passage", "Passage:", "Transcript excerpt:"))}


def run_case(c: dict, guardrails: bool) -> dict:
    p = parse_case(c)
    row = {"case_id": c["case_id"], "category": c["category"], "mode": "on" if guardrails else "off",
           "expected_with_guardrails": c["expected_with_guardrails"], "model": llm.model_tag()}
    if p["claim"]:
        row["route"] = "verify_only"
        lab = tools.verify_label(p["claim"], p["text"]) if guardrails else {**p["claim"], "verify_status": "not_checked"}
        return row | _label_cols(lab, p["claim"])
    if p["classify_only"] and p["text"]:
        row["route"] = "classify"
        raw = tools.classify_passage(passage_id=p["passage_id"] if c["input_type"] == "real" else None,
                                     text=p["text"], company=p["company"],
                                     requested_company=p["requested_company"], guardrails=guardrails)
        lab = tools.verify_label(raw, p["text"]) if guardrails else {**raw, "verify_status": "not_checked"}
        return row | _label_cols(lab, raw)
    row["route"] = "chat"
    q = p["request"] if not p["text"] or p["text"] in p["request"] else f"{p['request']}\n\nPassage ({p['company']}): {p['text']}"
    out = chat.ask(q, guardrails=guardrails)
    return row | {"answer": out["answer"][:2000],
                  "flags": ";".join(s["tool"] for s in out["steps"])}


def _label_cols(lab: dict, raw: dict) -> dict:
    return {"evidence_raw": raw.get("evidence", ""), "evidence": lab.get("evidence", ""),
            "scenarios": ";".join(lab.get("scenarios") or []), "quote": lab.get("quote", ""),
            "verify_status": lab.get("verify_status", ""), "verify_reason": lab.get("verify_reason", ""),
            "flags": ";".join(lab.get("flags") or [])}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--cases", help="comma-separated case ids (default all)")
    ap.add_argument("--out", default=str(config.REDTEAM_RESULTS))
    a = ap.parse_args(argv)
    cases = store.read_csv(config.REDTEAM_CASES)
    if a.cases:
        keep = set(a.cases.split(","))
        cases = [c for c in cases if c["case_id"] in keep]
    rows = []
    for c in cases:
        for guard in (False, True):
            r = run_case(c, guard)
            rows.append(r)
            print(f"{r['case_id']} guardrails {r['mode']:3}  {r['route']:11} "
                  f"{r.get('evidence_raw',''):>2} -> {r.get('evidence',''):>2}  {r.get('verify_status','')}")
    from pathlib import Path
    store.write_csv(Path(a.out), rows, FIELDS)
    print(f"-> {Path(a.out)} ({len(rows)} rows; model {llm.model_tag()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
