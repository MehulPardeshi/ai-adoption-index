"""AI Adoption Index agent (owner: Shu Pu).

Labels AI passages from SEC filings with an LLM (DeepSeek), checks every label
with a rule-based guardrail, and rolls the labels up into company scores.

Design: docs/part6-agent/agent_design.md
Entry points (run from the repo root):
    python3 -m src.agent.run_batch     label passages -> agent_labels_v1.csv, agent_scores_v1.csv
    python3 -m src.agent.chat "..."    ask a question; DeepSeek plans and calls the tools
    python3 -m src.agent.redteam       guardrail test set, with vs. without guardrails
"""
