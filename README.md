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

### `/analyze` Error Payload Examples (OpenRouter mode)

All `/analyze` failures use the same shape:

```json
{
  "detail": {
    "code": "machine_readable_code",
    "message": "Human-readable explanation"
  }
}
```

#### `500 openrouter_config_error`

When OpenRouter mode is enabled but required configuration is missing (for example, no `OPENROUTER_API_KEY`):

```json
{
  "detail": {
    "code": "openrouter_config_error",
    "message": "OpenRouter API key is not configured"
  }
}
```

#### `502 openrouter_request_error`

When the upstream provider returns a non-timeout request failure:

```json
{
  "detail": {
    "code": "openrouter_request_error",
    "message": "OpenRouter request failed: <provider error>"
  }
}
```

#### `502 openrouter_parse_error`

When provider output does not satisfy the expected JSON contract:

```json
{
  "detail": {
    "code": "openrouter_parse_error",
    "message": "Missing or invalid 'summary' in structured response"
  }
}
```

#### `504 openrouter_timeout`

When the OpenRouter request exceeds `OPENROUTER_TIMEOUT_SECONDS`:

```json
{
  "detail": {
    "code": "openrouter_timeout",
    "message": "OpenRouter request timed out"
  }
}
```

## Smoke Command

Use this before commits/nightly changes:

```bash
make smoke
```

`make smoke` runs targeted tests when pytest is available, otherwise falls back to `python3 -m compileall app tests`.
