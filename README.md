# Insight2Spec API

Minimal FastAPI service for turning user feedback into product insights.

## Quickstart (Local)

```bash
cd /home/ubuntu/.openclaw/workspace/projects/ai-resources
make bootstrap
make smoke
```

Run the API:

```bash
PYTHONPATH=. .venv/bin/uvicorn app.main:app --reload
```

## Quickstart (Dev Container)

1. Open this folder in VS Code.
2. Run **Dev Containers: Reopen in Container**.
3. Wait for post-create setup (`python3-pip`, `python3.12-venv`, `make bootstrap`).
4. Run:

```bash
make smoke
PYTHONPATH=. .venv/bin/uvicorn app.main:app --reload
```

## Analyze Modes

`/analyze` supports two modes via `INSIGHT2SPEC_ANALYZE_MODE`:

- `mock` (default): deterministic local output, no LLM calls.
- `openrouter`: live LLM call through OpenRouter.

Example:

```bash
export INSIGHT2SPEC_ANALYZE_MODE=openrouter
```

## Environment Variables

- `INSIGHT2SPEC_ANALYZE_MODE` — `mock` or `openrouter` (default: `mock`)
- `OPENROUTER_API_KEY` — required for `openrouter` mode
- `OPENROUTER_MODEL` — optional model override (default: `openai/gpt-4o-mini`)
- `OPENROUTER_TIMEOUT_SECONDS` — optional request timeout override

## Quick API Check (curl)

After starting the server (`PYTHONPATH=. .venv/bin/uvicorn app.main:app --reload`), run:

```bash
# 1) Health
curl -s http://127.0.0.1:8000/health | jq

# 2) Analyze (default mock mode)
curl -s -X POST http://127.0.0.1:8000/analyze \
  -H 'Content-Type: application/json' \
  -d '{
    "feedback": [
      "Search is slow when catalog size grows",
      "Users want saved filters for repeat workflows"
    ]
  }' | jq
```

Expected quick checks:
- `/health` returns `{ "status": "ok" }`
- `/analyze` returns non-empty `summary` plus arrays for `themes`, `opportunities`, and `experiments`

## Smoke Command

Use this before commits/nightly changes:

```bash
make smoke
```

`make smoke` runs targeted tests when pytest is available, otherwise falls back to `python3 -m compileall app tests`.
