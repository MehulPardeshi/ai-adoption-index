"""Check 3 against the team's agreed labels: does the agent label like the team?

The answer key is the consensus set (docs/part3-metrics/adjudication/consensus_labels.csv):
one agreed evidence level for each of the 80 passages people labeled (round 1: 50,
round 2: 30), settled by the raters on Nov 7-9. It replaces the "human majority" used
in the first check 3 (labeling_round_1/check3_agent.md), which left out 3-way splits.

The agent's prompt was tuned (Oct 23) on the 110 passages in agent_labels_v1.csv, so
passages in that file are reported separately as "tuning set"; everything else is
"unseen", the honest test. The AI-assisted draft labels (passage_labels_v0.csv), which
the dashboard's preliminary scores read, are scored on the same passages for reference.

Definitions (same as src/eval/irr.py):
  * use = D1 or D2; P, N and X are "no use"
  * overclaim  = the agent says use where the agreed label is no use (bar: <= 5%)
  * underclaim = the agent says no use where the agreed label is use
  * "without the guardrail" uses the model's own call (evidence_raw) before verify_label

Run from the repo root (after the agent has labeled the passages, see run_batch.py):
    python3 -m src.eval.check3_consensus
Writes docs/part3-metrics/check3_results.md and check3_differences.csv.
A missing agent-labels file is reported as "not run yet", so round 1 can be scored alone.
"""
import argparse
import csv
import json
from datetime import date
from pathlib import Path

from src.eval.irr import OVERCLAIM_TARGET, PROVISIONAL_TARGET, SCEN_LEVELS, cohen_kappa, jaccard, use

CONSENSUS = Path("docs/part3-metrics/adjudication/consensus_labels.csv")
TUNING = Path("data/processed/sec/agent_labels_v1.csv")
DRAFT = Path("data/processed/sec/passage_labels_v0.csv")
AGENT = [Path("data/processed/sec/agent_labels_sample.csv"),    # round 1 (Oct 27, #85)
         Path("data/processed/sec/agent_labels_round2.csv")]    # round 2 (#133)
RUN_INFO = [Path("data/processed/sec/agent_run_info_round2.json")]
OUT_MD = Path("docs/part3-metrics/check3_results.md")
OUT_CSV = Path("docs/part3-metrics/check3_differences.csv")
DIFF_FIELDS = ["passage_id", "round", "set", "kind", "agreed", "agreed_scenarios", "agent", "agent_scenarios",
               "confidence", "verify_status", "model_call", "draft", "quote"]


def read_csv(path: Path) -> list[dict]:
    with Path(path).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def load_consensus(path: Path = CONSENSUS) -> dict[str, dict]:
    return {r["passage_id"]: {"round": r["round"].strip(), "evidence": r["evidence"].strip().upper(),
                              "scenarios": r["scenarios"].strip()} for r in read_csv(path)}


def load_labels(paths: list[Path]) -> tuple[dict[str, dict], list[Path]]:
    """Agent (or draft) labels keyed by passage_id; returns the files that were found."""
    out, found = {}, []
    for p in paths:
        if not Path(p).exists():
            continue
        found.append(Path(p))
        for r in read_csv(p):
            out[r["passage_id"]] = {
                "evidence": r["evidence_v0"].strip().upper(), "scenarios": r.get("scenarios_v0", "").strip(),
                "confidence": r.get("confidence", ""), "verify_status": r.get("verify_status", ""),
                "raw": (r.get("evidence_raw") or r["evidence_v0"]).strip().upper(),
                "quote": r.get("quote", ""), "model": r.get("model", ""), "prompt_version": r.get("prompt_version", ""),
                "run_at": r.get("run_at", "")}
    return out, found


def compare(ids: list[str], pred: dict, ref: dict) -> dict:
    """Agreement of `pred` with the agreed labels `ref` on `ids` (all must be in both)."""
    a = [pred[i]["evidence"] for i in ids]
    b = [ref[i]["evidence"] for i in ids]
    ua, ub = [use(x) for x in a], [use(y) for y in b]
    raw = [pred[i].get("raw", pred[i]["evidence"]) for i in ids]
    scen = [jaccard(pred[i]["scenarios"], ref[i]["scenarios"]) for i in ids
            if pred[i]["evidence"] in SCEN_LEVELS and ref[i]["evidence"] in SCEN_LEVELS and ref[i]["scenarios"]]
    return {
        "n": len(ids),
        "exact": sum(x == y for x, y in zip(a, b)),
        "kappa": cohen_kappa(a, b) if ids else float("nan"),
        "use_agree": sum(x == y for x, y in zip(ua, ub)),
        "use_kappa": cohen_kappa(ua, ub) if ids else float("nan"),
        "over": [i for i, x, y in zip(ids, ua, ub) if x == "USE" and y == "NO"],
        "under": [i for i, x, y in zip(ids, ua, ub) if x == "NO" and y == "USE"],
        "over_raw": [i for i, x, y in zip(ids, raw, ub) if use(x) == "USE" and y == "NO"],
        "held": [i for i in ids if pred[i].get("verify_status") == "needs_review"],
        "scen_jaccard": sum(scen) / len(scen) if scen else float("nan"),
        "scen_n": len(scen),
    }


def kind_of(agent: str, agreed: str) -> str:
    if use(agent) == "USE" and use(agreed) == "NO":
        return "overclaim"
    if use(agent) == "NO" and use(agreed) == "USE":
        return "underclaim"
    return "level differs"


def _pct(k: int, n: int) -> str:
    return f"{k}/{n} ({k / n:.0%})" if n else "–"


def _k(x: float) -> str:
    return "–" if x != x else f"{x:.2f}"


def row(label: str, m: dict, guard: bool = True) -> str:
    cells = [label, str(m["n"]), _pct(m["exact"], m["n"]), _k(m["kappa"]), _pct(m["use_agree"], m["n"]),
             _k(m["use_kappa"]), _pct(len(m["over"]), m["n"]), _pct(len(m["under"]), m["n"])]
    if guard:
        cells += [_pct(len(m["over_raw"]), m["n"]), str(len(m["held"]))]
    cells.append(_k(m["scen_jaccard"]) + (f" (n={m['scen_n']})" if m["scen_n"] else ""))
    return "| " + " | ".join(cells) + " |"


def build(consensus: dict, agent: dict, tuning: set, draft: dict, agent_files: list[Path],
          run_infos: list[dict], today: str | None = None) -> tuple[str, list[dict]]:
    """Return the markdown report and the per-passage difference rows."""
    today = today or date.today().isoformat()
    rounds = sorted({c["round"] for c in consensus.values()})
    by_round = {r: [i for i, c in consensus.items() if c["round"] == r] for r in rounds}
    have = {r: [i for i in ids if i in agent] for r, ids in by_round.items()}
    missing = {r: [i for i in ids if i not in agent] for r, ids in by_round.items()}

    head = ("| Passages | n | Exact level | κ (level) | Use vs. no use | κ (use) | **Overclaim** | Underclaim "
            "| Overclaim without guardrail | Held for review | Scenario overlap |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|")
    lines, scored = [], []
    for r in rounds:
        if not have[r]:
            lines.append(f"| Round {r} | {len(by_round[r])} | *not run yet* |" + " |" * 8)
            continue
        unseen = [i for i in have[r] if i not in tuning]
        tuned = [i for i in have[r] if i in tuning]
        lines.append(row(f"Round {r}, **unseen**", compare(unseen, agent, consensus)))
        lines.append(row(f"Round {r}, tuning set", compare(tuned, agent, consensus)))
        scored += have[r]
    if len([r for r in rounds if have[r]]) > 1:
        unseen_all = [i for i in scored if i not in tuning]
        lines.append(row("**All rounds, unseen**", compare(unseen_all, agent, consensus)))
        lines.append(row("All rounds, all passages", compare(scored, agent, consensus)))

    dhead = ("| Passages | n | Exact level | κ (level) | Use vs. no use | κ (use) | Overclaim | Underclaim "
             "| Scenario overlap |\n|---|---|---|---|---|---|---|---|---|")
    dlines = []
    for r in rounds:
        ids = [i for i in by_round[r] if i in draft]
        dlines.append(row(f"Round {r}", compare(ids, draft, consensus), guard=False))
    all_draft = [i for i in consensus if i in draft]
    dlines.append(row("All rounds", compare(all_draft, draft, consensus), guard=False))
    same = [i for i in scored if i in draft]
    if same and len(same) != len(all_draft):
        dlines.append(row("Same passages as the agent", compare(same, draft, consensus), guard=False))

    diffs = []
    for i in scored:
        a, c = agent[i], consensus[i]
        if a["evidence"] == c["evidence"]:
            continue
        diffs.append({"passage_id": i, "round": c["round"], "set": "tuning" if i in tuning else "unseen",
                      "kind": kind_of(a["evidence"], c["evidence"]), "agreed": c["evidence"],
                      "agreed_scenarios": c["scenarios"], "agent": a["evidence"], "agent_scenarios": a["scenarios"],
                      "confidence": a["confidence"], "verify_status": a["verify_status"], "model_call": a["raw"],
                      "draft": draft.get(i, {}).get("evidence", ""), "quote": a["quote"]})
    order = {"overclaim": 0, "underclaim": 1, "level differs": 2}
    diffs.sort(key=lambda d: (order[d["kind"]], d["set"] != "unseen", d["round"], d["passage_id"]))

    held = [i for i in scored if agent[i]["verify_status"] == "needs_review"]
    runs = sorted({(agent[i]["model"], agent[i]["prompt_version"], agent[i]["run_at"][:10]) for i in scored})

    md = [f"# Check 3: the agent vs. the team's agreed labels",
          "",
          f"> **Generated** {today} by `python3 -m src.eval.check3_consensus` (rerun it after any new agent run). "
          f"**Answer key:** [`consensus_labels.csv`](adjudication/consensus_labels.csv), the evidence level the raters agreed "
          f"for each of the {len(consensus)} passages people labeled ("
          + ", ".join(f"round {r}: {len(by_round[r])}" for r in rounds) + ").",
          "> **Agent labels:** " + (", ".join(f"[`{p.name}`](../../{p.as_posix()})" for p in agent_files) or "none yet")
          + ". " + "; ".join(f"{m or '?'}, prompt `{v or '?'}`, run {d or '?'}" for m, v, d in runs)
          + ". Guardrails on.",
          f"> **Tuning set:** the {len(tuning)} passages in [`agent_labels_v1.csv`](../../{TUNING.as_posix()}) the prompt "
          "was tuned on (Oct 23). **Unseen** = the rest, the honest test.",
          ""]
    for r in rounds:
        if missing[r] and have[r]:
            md.append(f"> ⚠️ Round {r}: {len(missing[r])} of {len(by_round[r])} passages have no agent label and are "
                      f"left out: {', '.join(missing[r][:5])}{' …' if len(missing[r]) > 5 else ''}")
    md += ["## Agent vs. agreed labels", "", head, *lines, "",
           f"**Overclaim** = the agent says use (D1/D2) where the agreed label is N, P or X; bar ≤ {OVERCLAIM_TARGET:.0%}. "
           f"**Underclaim** = the reverse. κ = Cohen's kappa (bar ≥ {PROVISIONAL_TARGET:.2f}); on small groups read it as a "
           "direction only. *Overclaim without guardrail* scores the model's own call before `verify_label`. "
           "*Scenario overlap* = mean Jaccard of the area codes where both sides gave D2/D1/P.",
           "",
           "## The draft labels on the same passages (what the dashboard's preliminary scores read)",
           "", dhead, *dlines, "",
           "## Where the guardrail mattered", ""]
    if held:
        md += ["| passage_id | Round | Set | Model's call | Confidence | Agreed | Effect |", "|---|---|---|---|---|---|---|"]
        for i in held:
            a, c = agent[i], consensus[i]
            eff = ("stopped an overclaim" if use(a["raw"]) == "USE" and use(c["evidence"]) == "NO"
                   else "held a correct use (now an underclaim)" if use(a["raw"]) == "USE" else "no effect on use")
            md.append(f"| {i} | {c['round']} | {'tuning' if i in tuning else 'unseen'} | {a['raw']} | {a['confidence']} "
                      f"| {c['evidence']} | {eff} |")
    else:
        md.append("No label was held for review.")
    md += ["", f"## Every difference from the agreed label ({len(diffs)})", "",
           f"Also in [`{OUT_CSV.name}`]({OUT_CSV.name}), with the agent's quote.", ""]
    if diffs:
        md += ["| passage_id | Round | Set | Kind | Agent | Confidence | Guardrail | Agreed | Draft |",
               "|---|---|---|---|---|---|---|---|---|"]
        for d in diffs:
            ag = d["agent"] + (f" {d['agent_scenarios']}" if d["agent_scenarios"] else "")
            agr = d["agreed"] + (f" {d['agreed_scenarios']}" if d["agreed_scenarios"] else "")
            md.append(f"| {d['passage_id']} | {d['round']} | {d['set']} | {d['kind']} | {ag} | {d['confidence']} "
                      f"| {d['verify_status']} | {agr} | {d['draft']} |")
    if run_infos:
        md += ["", "## Run facts", ""]
        for ri in run_infos:
            u = ri.get("usage", {})
            md.append(f"- `{ri.get('labels_file', '?')}`: {ri.get('passages', '?')} passages, run {ri.get('run_at', '?')}, "
                      f"{ri.get('model', '?')}, prompt `{ri.get('prompt_version', '?')}`; {u.get('calls', '?')} new model calls, "
                      f"{u.get('cache_hits', '?')} from the cache; tokens in {u.get('prompt_tokens', '?')} "
                      f"(cached {u.get('cached_prompt_tokens', '?')}), out {u.get('completion_tokens', '?')}"
                      + (f"; {ri['wall_seconds']} s" if "wall_seconds" in ri else "") + ".")
    md += ["", "## Notes",
           "- Round 2's 30 passages were picked on purpose to be hard (the rule questions from round 1), so its numbers "
           "are expected to be lower than round 1's ([round 2 results](labeling_round_2/results_round2.md)).",
           "- The first check 3 compared the agent with the **human majority** (96% on 25 unseen passages, "
           "[report](labeling_round_1/check3_agent.md)). The agreed labels are stricter: they cover all passages, "
           "including the 3-way splits the majority left out.",
           "- Temperature 0 is not fully deterministic: a fresh run can move a label near the 0.70 threshold "
           "(round 1 overclaim was 0–2% across two runs). Cached answers make a rerun from the same machine identical."]
    return "\n".join(md) + "\n", diffs


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check 3: the agent vs. the team's agreed labels.")
    ap.add_argument("--agent-labels", nargs="+", default=[str(p) for p in AGENT], help="agent label CSVs")
    ap.add_argument("--run-info", nargs="*", default=[str(p) for p in RUN_INFO], help="run_batch --run-info-out JSONs")
    ap.add_argument("--consensus", default=str(CONSENSUS))
    ap.add_argument("--out-md", default=str(OUT_MD))
    ap.add_argument("--out-csv", default=str(OUT_CSV))
    a = ap.parse_args(argv)

    consensus = load_consensus(Path(a.consensus))
    agent, found = load_labels([Path(p) for p in a.agent_labels])
    tuning = {r["passage_id"] for r in read_csv(TUNING)}
    draft, _ = load_labels([DRAFT])
    infos = [json.loads(Path(p).read_text(encoding="utf-8")) for p in a.run_info if Path(p).exists()]
    md, diffs = build(consensus, agent, tuning, draft, found, infos)

    Path(a.out_md).write_text(md, encoding="utf-8")
    with Path(a.out_csv).open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=DIFF_FIELDS)
        w.writeheader()
        w.writerows(diffs)
    print(md)
    print(f"-> {a.out_md}\n-> {a.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
