"""Utilities for normalizing OpenRouter completion payloads."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from typing import Any


class OpenRouterParseError(ValueError):
    """Raised when assistant text cannot be extracted from a completion payload."""


def _extract_text_from_content_block(content: Any) -> str | None:
    """Handle OpenAI-style mixed content blocks.

    Supported examples:
    - "plain text"
    - [{"type": "text", "text": "..."}, ...]
    """
    if isinstance(content, str):
        text = content.strip()
        return text or None

    if isinstance(content, list):
        chunks: list[str] = []
        for block in content:
            if not isinstance(block, Mapping):
                continue
            if block.get("type") != "text":
                continue
            value = block.get("text")
            if isinstance(value, str) and value.strip():
                chunks.append(value.strip())

        if chunks:
            return "\n".join(chunks)

    return None


def extract_assistant_text(payload: Mapping[str, Any]) -> str:
    """Extract the first assistant message text from an OpenRouter completion payload."""
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        raise OpenRouterParseError("OpenRouter payload missing non-empty 'choices'")

    for choice in choices:
        if not isinstance(choice, Mapping):
            continue

        message = choice.get("message")
        if not isinstance(message, Mapping):
            continue

        content = message.get("content")
        text = _extract_text_from_content_block(content)
        if text:
            return text

    raise OpenRouterParseError("No assistant text content found in OpenRouter payload")


def _coerce_string_list(value: Any, *, field_name: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise OpenRouterParseError(f"Structured analysis field '{field_name}' must be a non-empty list")

    normalized: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise OpenRouterParseError(f"Structured analysis field '{field_name}' must contain non-empty strings")
        normalized.append(item.strip())

    return normalized


def _extract_json_object(raw_text: str) -> Mapping[str, Any]:
    text = raw_text.strip()
    fenced_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if fenced_match:
        text = fenced_match.group(1).strip()

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as error:
        raise OpenRouterParseError("Structured analysis must be valid JSON") from error

    if not isinstance(parsed, Mapping):
        raise OpenRouterParseError("Structured analysis JSON must be an object")

    return parsed


def extract_structured_analysis(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Extract and validate a structured product analysis JSON object from assistant output."""
    raw_text = extract_assistant_text(payload)
    parsed = _extract_json_object(raw_text)

    summary = parsed.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        raise OpenRouterParseError("Structured analysis field 'summary' must be a non-empty string")

    themes = _coerce_string_list(parsed.get("themes"), field_name="themes")
    opportunities = _coerce_string_list(parsed.get("opportunities"), field_name="opportunities")
    experiments = _coerce_string_list(parsed.get("experiments"), field_name="experiments")

    prd_outline_raw = parsed.get("prd_outline", [])
    prd_outline = _coerce_string_list(prd_outline_raw, field_name="prd_outline") if prd_outline_raw else []

    return {
        "summary": summary.strip(),
        "themes": themes,
        "opportunities": opportunities,
        "experiments": experiments,
        "prd_outline": prd_outline,
    }
