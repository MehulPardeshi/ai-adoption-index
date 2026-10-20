"""Chat mode: DeepSeek plans which tools to call, calls them, and answers with cited evidence.

    python3 -m src.agent.chat "How does JPMorgan use AI in FY2025, and how does it compare with Dong?"
    python3 -m src.agent.chat --no-guardrails "..."     # for the check 6 comparison
    python3 -m src.agent.chat --trace "..."             # print every tool call

With guardrails on: the guarded system prompt (scope, citation and injection rules) is used,
classify_passage output is always run through verify_label, and live EDGAR downloads are off.
"""
import argparse
import json
import re

from src.agent import config, llm, prompts, tools


def ask(question: str, guardrails: bool = True, trace: bool = False, max_steps: int = config.CHAT_MAX_STEPS) -> dict:
    """Answer one question. Returns {"answer", "steps": [{"tool", "args", "result"}]}."""
    system = prompts.CHAT_SYSTEM_GUARDED if guardrails else prompts.CHAT_SYSTEM_UNGUARDED
    messages = [{"role": "system", "content": system}, {"role": "user", "content": question}]
    steps = []
    for _ in range(max_steps):
        reply = llm.complete(messages, tools=tools.TOOL_SPECS, max_tokens=config.MAX_TOKENS_CHAT,
                             mock=lambda m, t: _mock_planner(question, m))
        calls = reply.get("tool_calls") or []
        if not calls:
            return {"answer": reply.get("content") or "", "steps": steps}
        messages.append({"role": "assistant", "content": reply.get("content") or "",
                         "tool_calls": [{"id": c["id"], "type": "function",
                                         "function": {"name": c["name"], "arguments": c["arguments"]}} for c in calls]})
        for c in calls:
            try:
                args = json.loads(c["arguments"] or "{}")
            except json.JSONDecodeError:
                args = {}
            result = tools.dispatch(c["name"], args, guardrails=guardrails)
            steps.append({"tool": c["name"], "args": args, "result": result})
            if trace:
                print(f"  -> {c['name']}({json.dumps(args)})")
            messages.append({"role": "tool", "tool_call_id": c["id"],
                             "content": json.dumps(result, ensure_ascii=False)[:12000]})
    return {"answer": "Stopped after the maximum number of tool steps without a final answer.", "steps": steps}


def _mock_planner(question: str, messages: list[dict]) -> dict:
    """Offline stand-in for DeepSeek's planning, to test the loop. Not a real agent."""
    done = [m for m in messages if m["role"] == "tool"]
    m = re.search(r"\b(JPM|BAC|COF|WFC|SCHW|PFG)\b", question.upper())
    names = {v.split()[0].upper(): k for k, v in tools.COMPANIES.items()}
    t = m.group(1) if m else next((k for n, k in names.items() if n in question.upper()), "JPM")
    y = int((re.search(r"20\d\d", question) or [2025])[0])
    plan = [("get_labels", {"ticker": t, "fiscal_year": y, "evidence": ["D2", "D1"]}),
            ("score_companies", {"tickers": [t], "fiscal_year": y}),
            ("lookup_baseline", {"ticker": t, "fiscal_year": 2023})]
    if len(done) < len(plan):
        name, args = plan[len(done)]
        return {"content": "", "tool_calls": [{"id": f"mock{len(done)}", "name": name, "arguments": json.dumps(args)}]}
    return {"content": f"[mock answer] Collected {len(done)} tool results for {t} FY{y}; a real run writes the answer here.",
            "tool_calls": []}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Ask the AI Adoption Index agent a question.")
    ap.add_argument("question")
    ap.add_argument("--no-guardrails", action="store_true")
    ap.add_argument("--trace", action="store_true", help="print each tool call")
    a = ap.parse_args(argv)
    out = ask(a.question, guardrails=not a.no_guardrails, trace=a.trace)
    print("\n" + out["answer"])
    print(f"\n({len(out['steps'])} tool calls; model {llm.model_tag()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
