"""Paths, model settings and guardrail thresholds for the agent. One place to change them."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_dotenv(path: Path = ROOT / ".env") -> None:
    """Read KEY=VALUE lines from .env into os.environ (no extra dependency). Existing vars win."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


# Load .env before the settings below read os.environ, so DEEPSEEK_MODEL etc. in .env take effect.
load_dotenv()

# ---- inputs (existing team data; not written by the agent) ----
PASSAGES = ROOT / "data/interim/sec/ai_passages.csv"            # Yen-Chu's SEC run, verbatim passages
INVENTORY = ROOT / "data/processed/sec/filings_inventory.csv"    # one row per filing
DRAFT_LABELS = ROOT / "data/processed/sec/passage_labels_v0.csv" # AI-assisted draft labels (check 3 preview)
DONG_BASELINE = ROOT / "data/processed/sec/shu_run/dong_baseline_6firms.csv"
RAW_TEXT = ROOT / "data/raw/sec/text"                            # full filings as text (gitignored, optional)
REDTEAM_CASES = ROOT / "docs/part3-metrics/guardrail_redteam_cases.csv"

# ---- outputs ----
AGENT_LABELS = ROOT / "data/processed/sec/agent_labels_v1.csv"
AGENT_LABELS_NOGUARD = ROOT / "data/processed/sec/agent_labels_v1_noguard.csv"
AGENT_SCORES = ROOT / "data/processed/sec/agent_scores_v1.csv"
AGENT_RUN_INFO = ROOT / "data/processed/sec/agent_run_info.json"
REDTEAM_RESULTS = ROOT / "data/processed/agent/redteam_results_v1.csv"
CACHE_DIR = ROOT / "data/cache/llm"                              # gitignored

# ---- model ----
PROVIDER = os.environ.get("AGENT_LLM_PROVIDER", "deepseek")      # "deepseek" or "mock" (offline tests)
DEEPSEEK_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-flash")       # pin the snapshot in MODEL_SNAPSHOT
MODEL_SNAPSHOT = os.environ.get("DEEPSEEK_MODEL_SNAPSHOT", "DeepSeek-V4.1-Flash-1017")
TEMPERATURE = 0.0
# deepseek-flash thinks before it answers, and its reasoning tokens count toward max_tokens.
# 500 cut off 13 of 90 replies in the first run (Oct 23), so leave plenty of room.
MAX_TOKENS_CLASSIFY = 4000
MAX_TOKENS_CHAT = 4000
REQUEST_TIMEOUT = 60
MAX_RETRIES = 3

# ---- prompt / guardrail ----
PROMPT_VERSION = "classify-v1.0"
MIN_CONFIDENCE = 0.70        # below this, a label goes to human review and is not scored
CHAT_MAX_STEPS = 8           # function-calling rounds per question
PASSAGE_MAX_CHARS = 6000     # longest SEC passage is ~3.9k chars


def api_key() -> str:
    load_dotenv()
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("LLM_API_KEY")
    if not key:
        raise RuntimeError("No DeepSeek key. Put DEEPSEEK_API_KEY=... in .env (see .env.example), "
                           "or run with AGENT_LLM_PROVIDER=mock for an offline dry run.")
    return key
