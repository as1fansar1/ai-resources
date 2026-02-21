"""Utilities for normalizing OpenRouter completion payloads."""

from __future__ import annotations

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
