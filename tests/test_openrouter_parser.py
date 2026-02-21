import pytest

from app.openrouter_parser import OpenRouterParseError, extract_assistant_text


def test_extract_assistant_text_from_plain_content() -> None:
    payload = {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Here is your summary.",
                }
            }
        ]
    }

    assert extract_assistant_text(payload) == "Here is your summary."


def test_extract_assistant_text_from_content_blocks() -> None:
    payload = {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": [
                        {"type": "reasoning", "text": "hidden"},
                        {"type": "text", "text": "Line one"},
                        {"type": "text", "text": "Line two"},
                    ],
                }
            }
        ]
    }

    assert extract_assistant_text(payload) == "Line one\nLine two"


def test_extract_assistant_text_skips_invalid_choices() -> None:
    payload = {
        "choices": [
            {"message": {"content": "   "}},
            {"message": {"content": "Final usable answer"}},
        ]
    }

    assert extract_assistant_text(payload) == "Final usable answer"


def test_extract_assistant_text_raises_on_missing_choices() -> None:
    with pytest.raises(OpenRouterParseError):
        extract_assistant_text({})


def test_extract_assistant_text_raises_when_no_text_found() -> None:
    payload = {
        "choices": [
            {
                "message": {
                    "content": [
                        {"type": "tool_call", "name": "search"},
                    ]
                }
            }
        ]
    }

    with pytest.raises(OpenRouterParseError):
        extract_assistant_text(payload)
