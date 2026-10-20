"""DeepSeek client: pinned model, temperature 0, JSON mode, retries and an on-disk cache.

DeepSeek's API is OpenAI-compatible (POST /chat/completions), so we call it with `requests`
and need no extra SDK. Temperature 0 is not a determinism guarantee, so reproducibility
comes from the cache: the same model + prompt version + messages always return the cached reply.

Provider "mock" runs fully offline (tests, dry runs, machines without a key). Callers pass a
`mock` function that produces the reply; the mock never pretends to be DeepSeek in the outputs.
"""
import hashlib
import json
import time
from typing import Callable

import requests

from src.agent import config

USAGE = {"calls": 0, "cache_hits": 0, "prompt_tokens": 0, "cached_prompt_tokens": 0, "completion_tokens": 0}


def model_tag() -> str:
    if config.PROVIDER == "mock":
        return "mock (offline dry run, not an LLM)"
    return f"{config.MODEL}@{config.MODEL_SNAPSHOT}"


def _cache_key(payload: dict) -> str:
    blob = json.dumps({"v": config.PROMPT_VERSION, "p": config.PROVIDER, **payload}, sort_keys=True)
    return hashlib.sha256(blob.encode()).hexdigest()


def complete(messages: list[dict], *, tools: list[dict] | None = None, json_mode: bool = False,
             max_tokens: int = config.MAX_TOKENS_CLASSIFY, use_cache: bool = True,
             mock: Callable[[list[dict], list[dict] | None], dict] | None = None) -> dict:
    """One chat-completion call.

    Returns {"content": str|None, "tool_calls": [{"id","name","arguments"}], "cached": bool}.
    """
    payload = {"model": config.MODEL, "messages": messages, "temperature": config.TEMPERATURE,
               "max_tokens": max_tokens}
    if json_mode:
        payload["response_format"] = {"type": "json_object"}
    if tools:
        payload["tools"] = tools
        payload["tool_choice"] = "auto"

    key = _cache_key(payload)
    path = config.CACHE_DIR / f"{key}.json"
    if use_cache and path.exists():
        USAGE["cache_hits"] += 1
        return {**json.loads(path.read_text(encoding="utf-8")), "cached": True}

    if config.PROVIDER == "mock":
        if mock is None:
            raise RuntimeError("Provider is 'mock' but the caller supplied no mock function.")
        reply = mock(messages, tools)
    else:
        reply = _call_deepseek(payload)

    if use_cache:
        config.CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(reply, ensure_ascii=False), encoding="utf-8")
    return {**reply, "cached": False}


def _call_deepseek(payload: dict) -> dict:
    headers = {"Authorization": f"Bearer {config.api_key()}", "Content-Type": "application/json"}
    url = config.DEEPSEEK_BASE_URL.rstrip("/") + "/chat/completions"
    last = None
    for attempt in range(config.MAX_RETRIES + 1):
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=config.REQUEST_TIMEOUT)
            if r.status_code in (429, 500, 502, 503, 504):
                last = f"HTTP {r.status_code}: {r.text[:200]}"
                time.sleep(2 ** attempt * 2)
                continue
            r.raise_for_status()
            data = r.json()
            break
        except requests.RequestException as e:
            last = str(e)
            time.sleep(2 ** attempt * 2)
    else:
        raise RuntimeError(f"DeepSeek call failed after retries: {last}")

    USAGE["calls"] += 1
    u = data.get("usage", {})
    USAGE["prompt_tokens"] += u.get("prompt_tokens", 0)
    USAGE["cached_prompt_tokens"] += u.get("prompt_cache_hit_tokens", 0)
    USAGE["completion_tokens"] += u.get("completion_tokens", 0)

    msg = data["choices"][0]["message"]
    calls = [{"id": c["id"], "name": c["function"]["name"], "arguments": c["function"].get("arguments") or "{}"}
             for c in msg.get("tool_calls") or []]
    return {"content": msg.get("content"), "tool_calls": calls, "model_returned": data.get("model", "")}


def parse_json(text: str | None) -> dict:
    """Parse a JSON object from model text; tolerate code fences. Raises ValueError if impossible."""
    if not text:
        raise ValueError("empty model reply")
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        t = t[t.find("{"):]
    start, end = t.find("{"), t.rfind("}")
    if start < 0 or end < 0:
        raise ValueError(f"no JSON object in reply: {text[:120]!r}")
    return json.loads(t[start:end + 1])
