"""FastAPI entrypoint for Insight2Spec."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    """Input contract for feedback analysis."""

    feedback: list[str] = Field(..., min_length=1, description="Raw user feedback snippets")
    context: str | None = Field(default=None, description="Optional product/background context")


class AnalyzeResponse(BaseModel):
    """Deterministic mock output contract for Insight2Spec."""

    mode: Literal["mock"]
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


def _build_mock_analysis(feedback_items: list[str]) -> AnalyzeResponse:
    """Create a stable, deterministic pseudo-analysis from feedback text."""
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
        mode="mock",
        summary=summary,
        themes=themes,
        opportunities=opportunities,
        prd_outline=prd_outline,
        experiments=experiments,
    )


def create_app() -> FastAPI:
    """Application factory for easier testing and future config injection."""
    app = FastAPI(title="Insight2Spec API", version="0.1.0")

    @app.get("/health")
    def health() -> dict[str, str]:
        """Lightweight liveness probe."""
        return {"status": "ok", "service": "insight2spec"}

    @app.post("/analyze", response_model=AnalyzeResponse)
    def analyze(payload: AnalyzeRequest) -> AnalyzeResponse:
        """Return a deterministic mock analysis (v0 contract for frontend integration)."""
        return _build_mock_analysis(payload.feedback)

    return app


app = create_app()
