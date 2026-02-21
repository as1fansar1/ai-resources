# Nightly Build Log

Add one entry per nightly run.

## Template
- Date:
- Built:
- Why this step:
- Key technical concepts:
- Files changed:
- Risks/limitations:
- Next step:

---

- Date: 2026-02-17
- Built: Initial FastAPI skeleton with application factory and `/health` endpoint, plus pinned runtime deps and a health endpoint test scaffold.
- Why this step: It is the top-priority item in `NEXT_STEPS.md` and creates a runnable API foundation for all upcoming LLM integration work.
- Key technical concepts:
  - FastAPI app factory (`create_app`) for easier testing and future config injection.
  - Liveness probe pattern via lightweight `/health` endpoint.
  - Dependency pinning (`requirements.txt`) to reduce environment drift.
  - Test-first API contract setup with `fastapi.testclient.TestClient`.
- Files changed:
  - `app/main.py`
  - `tests/test_health.py`
  - `requirements.txt`
- Risks/limitations:
  - Runtime test execution not performed yet because dependencies are not installed in this environment.
  - No startup config/env handling yet.
- Next step: Implement an OpenRouter client wrapper with clean interface, timeout handling, and basic error mapping.

- Date: 2026-02-17
- Built: Added a minimal OpenRouter client wrapper (`OpenRouterClient`) with env-based config loading, timeout/error mapping, and focused unit tests for success + failure paths.
- Why this step: It was the highest-priority remaining item and unlocks safe model-call plumbing before adding `/analyze`.
- Key technical concepts:
  - API client wrapper pattern to isolate third-party integration details.
  - Environment-driven secrets/config (`OPENROUTER_API_KEY`, timeout override).
  - Error taxonomy (`ConfigError`, `RequestError`, `TimeoutError`) so API routes can map failures cleanly.
  - Dependency injection in tests via monkeypatching `httpx.Client` to keep tests deterministic.
- Files changed:
  - `app/openrouter_client.py`
  - `tests/test_openrouter_client.py`
  - `requirements.txt`
- Risks/limitations:
  - Sanity check command `pytest -q` is currently blocked in this environment (`pytest: command not found`) until dependencies are installed.
  - Wrapper currently returns raw completion JSON; response normalization is not implemented yet.
- Next step: Add first `/analyze` endpoint with deterministic mock + response schema, then swap in OpenRouter behind the same contract.

- Date: 2026-02-18
- Built: Implemented first `/analyze` endpoint with explicit request/response schema and deterministic mock analysis logic, plus endpoint tests.
- Why this step: It was the top-priority item in `NEXT_STEPS.md` and creates a stable API contract Asif can build UI/client code against before real LLM wiring.
- Key technical concepts:
  - Pydantic request/response contracts (`AnalyzeRequest`, `AnalyzeResponse`) for predictable API behavior.
  - Deterministic mock generation via keyword-based theme detection so outputs are testable and reproducible.
  - Contract-first endpoint development to decouple product/API design from model integration timing.
  - Validation guardrails (`feedback` list must contain at least one item).
- Files changed:
  - `app/main.py`
  - `tests/test_analyze.py`
- Risks/limitations:
  - `/analyze` is still mock-only; it does not call OpenRouter yet.
  - `pytest -q` remains unavailable in this environment (`pytest: command not found`), so sanity check used `python3 -m compileall app tests`.
- Next step: Wire dependency installation + a one-command smoke test (`make smoke`) so tests can run reliably in nightly jobs.

- Date: 2026-02-19
- Built: Added a one-command smoke workflow via `Makefile` (`make smoke`) with dependency install wiring and environment-aware fallback, plus README setup guidance.
- Why this step: It was the highest-priority item in `NEXT_STEPS.md` and is foundational for fast, repeatable nightly validation as model integration complexity increases.
- Key technical concepts:
  - Build automation with `make` to standardize local/nightly run commands.
  - Progressive install strategy: try isolated `.venv` first, then fallback to user-site install.
  - Smoke-test scope control: run only core API contract checks (`tests/test_health.py`, `tests/test_analyze.py`) for speed.
  - Environment diagnostics as part of DX: documented apt prerequisites when Python packaging modules are missing.
- Files changed:
  - `Makefile`
  - `README.md`
  - `docs/NEXT_STEPS.md`
- Risks/limitations:
  - Current runtime remains blocked from fully executing `make smoke` because both `venv` bootstrap (`ensurepip`) and `pip` module are missing.
  - Until host prerequisites are installed, fallback sanity check remains `python3 -m compileall app tests`.
- Next step: Add OpenRouter response parser utility to safely extract assistant text from completion payload.

- Date: 2026-02-21
- Built: Added `extract_assistant_text` parser utility for OpenRouter completion payloads with strict error signaling, plus focused unit tests for plain text, content-block, and failure scenarios.
- Why this step: It was the highest-priority open item in `NEXT_STEPS.md` and is required before wiring `/analyze` to a live model response safely.
- Key technical concepts:
  - Response normalization layer to shield route code from provider payload shape changes.
  - Defensive parsing for mixed-content message blocks (`[{"type":"text", ...}]`).
  - Explicit parse errors (`OpenRouterParseError`) to keep downstream error mapping predictable.
  - Test-driven contract checks for happy path + malformed payloads.
- Files changed:
  - `app/openrouter_parser.py`
  - `tests/test_openrouter_parser.py`
  - `docs/NEXT_STEPS.md`
  - `docs/NIGHTLY_LOG.md`
- Risks/limitations:
  - Full pytest run remains blocked in this environment due to missing pytest binary/pip bootstrap in `.venv`; sanity check used `python3 -m compileall app tests`.
  - Parser currently extracts assistant text only; it does not normalize tool calls or metadata.
- Next step: Connect `/analyze` to OpenRouter behind the existing response contract, with mock fallback for local/dev mode.
