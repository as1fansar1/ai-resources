"""FastAPI entrypoint for Insight2Spec."""

from __future__ import annotations

import os
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.openrouter_client import (
    OpenRouterClient,
    OpenRouterConfigError,
    OpenRouterRequestError,
    OpenRouterTimeoutError,
)
from app.openrouter_parser import OpenRouterParseError, extract_assistant_text


class AnalyzeRequest(BaseModel):
    feedback: list[str] = Field(..., min_length=1, description="Raw user feedback snippets")
    context: str | None = Field(default=None, description="Optional product/background context")


class AnalyzeResponse(BaseModel):
    mode: Literal["mock", "openrouter"]
    summary: str
    themes: list[str]
    opportunities: list[str]
    prd_outline: list[str]
    experiments: list[str]


_THEME_KEYWORDS: dict[str, tuple[str, ...]] = {
    "Onboarding Friction": ("onboard", "setup", "signup", "start"),
    "Reliability Issues": ("crash", "bug", "error", "slow", "latency", "fail"),
    "Pricing Confusion": ("price", "pricing", "plan", "cost", "expensive"),
    "Missing Integrations": ("integrat", "slack", "zapier", "api", "export"),
}


def _build_mock_analysis(feedback_items: list[str], *, mode: Literal["mock", "openrouter"] = "mock") -> AnalyzeResponse:
    feedback_blob = " ".join(feedback_items).lower()

    matched_themes = [
        theme
        for theme, keywords in _THEME_KEYWORDS.items()
        if any(keyword in feedback_blob for keyword in keywords)
    ]

    themes = matched_themes or ["General UX Feedback"]
    opportunities = [f"Improve {theme.lower()} with clearer product guidance" for theme in themes[:3]]

    prd_outline = [
        "Problem statement and target persona",
        "Current user journey pain points",
        "Proposed feature changes",
        "Success metrics and rollout plan",
    ]

    experiments = [
        "A/B test onboarding checklist completion",
        "Track support-ticket volume before/after release",
    ]

    summary = (
        f"Analyzed {len(feedback_items)} feedback item(s). "
        f"Detected {len(themes)} theme(s): {', '.join(themes)}."
    )

    return AnalyzeResponse(
        mode=mode,
        summary=summary,
        themes=themes,
        opportunities=opportunities,
        prd_outline=prd_outline,
        experiments=experiments,
    )


def _build_openrouter_prompt(payload: AnalyzeRequest) -> str:
    context = f"\nContext: {payload.context}" if payload.context else ""
    feedback_lines = "\n".join(f"- {item}" for item in payload.feedback)
    return (
        "Summarize these feedback notes and return concise plain text with top insights."
        f"{context}\nFeedback:\n{feedback_lines}"
    )


def _raise_openrouter_http_error(error: Exception) -> None:
    if isinstance(error, OpenRouterConfigError):
        raise HTTPException(
            status_code=500,
            detail={
                "code": "openrouter_config_error",
                "message": str(error),
            },
        ) from error

    if isinstance(error, OpenRouterTimeoutError):
        raise HTTPException(
            status_code=504,
            detail={
                "code": "openrouter_timeout",
                "message": str(error),
            },
        ) from error

    if isinstance(error, OpenRouterRequestError):
        raise HTTPException(
            status_code=502,
            detail={
                "code": "openrouter_request_error",
                "message": str(error),
            },
        ) from error

    if isinstance(error, OpenRouterParseError):
        raise HTTPException(
            status_code=502,
            detail={
                "code": "openrouter_parse_error",
                "message": str(error),
            },
        ) from error


def _analyze_with_openrouter(payload: AnalyzeRequest) -> AnalyzeResponse:
    client = OpenRouterClient.from_env()
    completion = client.complete_json(
        model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
        system_prompt="You are a product analyst. Be concise and concrete.",
        user_prompt=_build_openrouter_prompt(payload),
    )
    summary = extract_assistant_text(completion)

    result = _build_mock_analysis(payload.feedback, mode="openrouter")
    return result.model_copy(update={"summary": summary})


def create_app() -> FastAPI:
    app = FastAPI(title="Insight2Spec API", version="0.1.0")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "insight2spec"}

    @app.post("/analyze", response_model=AnalyzeResponse)
    def analyze(payload: AnalyzeRequest) -> AnalyzeResponse:
        if os.getenv("INSIGHT2SPEC_ANALYZE_MODE", "mock").lower() != "openrouter":
            return _build_mock_analysis(payload.feedback)

        try:
            return _analyze_with_openrouter(payload)
        except (OpenRouterConfigError, OpenRouterTimeoutError, OpenRouterRequestError, OpenRouterParseError) as error:
            _raise_openrouter_http_error(error)

    return app


app = create_app()
