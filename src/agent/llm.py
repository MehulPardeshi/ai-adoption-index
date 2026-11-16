"""DeepSeek client: pinned model, temperature 0, JSON mode, retries and an on-disk cache.

DeepSeek's API is OpenAI-compatible (POST /chat/completions), so we call it with `requests`
and need no extra SDK. Temperature 0 is not a determinism guarantee, so reproducibility
comes from the cache: the same model + prompt version + messages always return the cached reply.

Provider "mock" runs fully offline (tests, dry runs, machines without a key). Callers pass a
`mock` function that produces the reply; the mock never pretends to be DeepSeek in the outputs.
"""
import hashlib
import json
import os
import threading
import time
from typing import Callable

import requests

from src.agent import config

USAGE = {"calls": 0, "cache_hits": 0, "prompt_tokens": 0, "cached_prompt_tokens": 0, "completion_tokens": 0,
         "reasoning_tokens": 0, "truncated": 0}
_LOCK = threading.Lock()  # run_batch --workers calls the model from several threads


def _add(**counts) -> None:
    with _LOCK:
        for k, v in counts.items():
            USAGE[k] += v


def reset_usage() -> None:
    """Zero the counters, so a caller can report the usage of one run."""
    with _LOCK:
        for k in USAGE:
            USAGE[k] = 0


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
        _add(cache_hits=1)
        return {**json.loads(path.read_text(encoding="utf-8")), "cached": True}

    if config.PROVIDER == "mock":
        if mock is None:
            raise RuntimeError("Provider is 'mock' but the caller supplied no mock function.")
        reply = mock(messages, tools)
    else:
        reply = _call_deepseek(payload)

    # A reply cut off by max_tokens, or with neither text nor tool calls, is not cached, so a rerun retries it.
    complete_reply = reply.get("finish_reason") != "length" and (reply.get("content") or reply.get("tool_calls"))
    if use_cache and complete_reply:
        tmp = path.with_name(f"{path.stem}.{os.getpid()}.{threading.get_ident()}.tmp")
        try:
            config.CACHE_DIR.mkdir(parents=True, exist_ok=True)
            tmp.write_text(json.dumps(reply, ensure_ascii=False), encoding="utf-8")
            os.replace(tmp, path)  # atomic: a reader never sees half a file
        except OSError:  # e.g. a Windows file lock; costs one repeat call on a rerun, never the label
            try:
                tmp.unlink(missing_ok=True)
            except OSError:
                pass
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

    u = data.get("usage", {})
    choice = data["choices"][0]
    msg = choice["message"]
    _add(calls=1, prompt_tokens=u.get("prompt_tokens", 0), cached_prompt_tokens=u.get("prompt_cache_hit_tokens", 0),
         completion_tokens=u.get("completion_tokens", 0),
         reasoning_tokens=(u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0),
         truncated=int(choice.get("finish_reason") == "length"))
    calls = [{"id": c["id"], "name": c["function"]["name"], "arguments": c["function"].get("arguments") or "{}"}
             for c in msg.get("tool_calls") or []]
    return {"content": msg.get("content"), "tool_calls": calls, "model_returned": data.get("model", ""),
            "finish_reason": choice.get("finish_reason", "")}


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
