# AI Resources

Research, experiments, and practical notes on AI agents, tools, models, and emerging workflows.

This repository is where I document what I am learning while building agentic systems, evaluating AI-enabled product workflows, and experimenting with Hermes Agent.

## What's inside

### [Hermes Research](./Hermes%20Research/)

Recurring research reports on:

- New AI tools and agent workflows
- GitHub projects with practical product potential
- Local-first and BYOK creator tools
- Agent skills, orchestration, evaluation, and security
- Product remix ideas based on emerging open-source projects

### [AI Business Workflows](./AI%20Business%20Workflows/)

A collection of practical AI and automation workflow ideas organized by publication date.

### [Learning](./learning/)

Hands-on learning material covering prompt contracts, structured outputs, acceptance criteria, failure modes, and production-minded AI product design.

### Insight2Spec API

A minimal FastAPI service that turns unstructured user feedback into structured product insights, including themes, opportunities, and experiments.

The API supports two modes:

- `mock` — deterministic local output with no LLM calls
- `openrouter` — live structured analysis through OpenRouter

## Run Insight2Spec locally

```bash
make bootstrap
make smoke
PYTHONPATH=. .venv/bin/uvicorn app.main:app --reload
```

### Environment variables

- `INSIGHT2SPEC_ANALYZE_MODE` — `mock` or `openrouter` (default: `mock`)
- `OPENROUTER_API_KEY` — required for `openrouter` mode
- `OPENROUTER_MODEL` — optional model override
- `OPENROUTER_TIMEOUT_SECONDS` — optional request timeout

### Quick API check

```bash
curl -s http://127.0.0.1:8000/health | jq

curl -s -X POST http://127.0.0.1:8000/analyze \
  -H 'Content-Type: application/json' \
  -d '{
    "feedback": [
      "Search is slow when catalog size grows",
      "Users want saved filters for repeat workflows"
    ]
  }' | jq
```

All API failures return a consistent machine-readable error contract. Run `make smoke` before committing changes.

## Research cadence

The Hermes research reports are published twice each week, on Tuesday and Friday mornings.
