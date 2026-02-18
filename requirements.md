# Insight2Spec — Product Requirements

## 1) Product Overview
Insight2Spec helps product teams convert raw user feedback (tickets, reviews, support chats, call notes) into decision-ready product artifacts:
1. Theme clusters
2. Opportunity statements
3. Draft PRD sections
4. Experiment ideas

Primary user (v1): AI Product Manager / Product Manager (starting with Asif).

## 2) Product Goals
- Reduce time from raw feedback to usable product insight.
- Improve consistency and quality of synthesis.
- Produce artifacts that are immediately usable in PM workflows.
- Serve as a practical learning vehicle for AI PM skill development.

## 3) Non-Goals (v1)
- Full production-grade multi-tenant SaaS.
- Real-time collaboration.
- Deep BI dashboards.
- Automated source ingestion from every external tool.

## 4) Core User Stories
1. As a PM, I can submit a batch of raw feedback text and get top themes.
2. As a PM, I get 3+ opportunity statements tied to the themes.
3. As a PM, I get a draft PRD outline I can refine.
4. As a PM, I get experiment ideas for validation.
5. As a PM, I can save and revisit each run with inputs/outputs.

## 5) Functional Requirements

### FR-1: Feedback Input
- System accepts feedback input as plain text (copy/paste) in v1.
- Input includes optional metadata fields:
  - source (ticket/review/chat/etc.)
  - segment/persona
  - date range label
- Validation rules:
  - non-empty input
  - minimum and maximum character limits

### FR-2: Analyze Endpoint
- Provide `POST /analyze` endpoint.
- Request schema must be strict and validated.
- Response schema must be deterministic and versioned.
- Endpoint supports mock mode for deterministic local testing.

### FR-3: Theme Clustering
- Output includes a list of top themes with:
  - theme label
  - short description
  - evidence snippets (quotes)
  - confidence score (0-1)

### FR-4: Opportunity Statements
- Generate at least 3 opportunity statements.
- Each includes:
  - problem statement
  - target user
  - expected impact
  - supporting themes

### FR-5: PRD Draft Generation
- Generate draft PRD sections:
  - Problem
  - Goals
  - Non-goals
  - User stories
  - Success metrics
  - Risks
- Keep output editable and structured.

### FR-6: Experiment Ideas
- Generate 3–5 experiment ideas, each with:
  - hypothesis
  - test design
  - success metric
  - effort level (S/M/L)

### FR-7: Run History Storage
- Save every run to local JSON in `data/runs/`.
- Persist:
  - timestamp
  - input payload
  - model metadata
  - output payload
  - latency and error status

### FR-8: Model Provider Integration
- Use OpenRouter client abstraction for model calls.
- API keys loaded from environment variables.
- Timeouts and errors mapped to predictable app-level errors.

### FR-9: Health and Reliability Endpoints
- `GET /health` returns service liveness.
- Include basic readiness checks in future versions.

### FR-10: Testing
- Unit tests for:
  - request/response schemas
  - OpenRouter client behavior
  - core transformation/parsing utilities
- Smoke test path for quick confidence check.

## 6) Non-Functional Requirements

### NFR-1: Latency
- v1 target: p95 analyze response under 12s for moderate input.

### NFR-2: Cost Awareness
- Log model/call metadata for basic cost tracking.
- Keep prompt/output constrained and structured.

### NFR-3: Reliability
- Graceful failure responses with actionable error messages.
- No hard crashes on invalid user input.

### NFR-4: Security
- Secrets only via env vars; never committed to Git.
- Sanitize persisted run artifacts for sensitive data where possible.

### NFR-5: Maintainability
- Modular architecture (API routes, client layer, parsers, schemas).
- Clear error taxonomy and stable contracts.

## 7) API Contract Requirements (v1)

### `POST /analyze` request (minimum)
- `feedback_text` (string, required)
- `context` (object, optional)
- `mode` (enum: `mock | live`)

### `POST /analyze` response (minimum)
- `themes[]`
- `opportunities[]`
- `prd_draft` (object)
- `experiments[]`
- `meta`:
  - run_id
  - mode
  - model
  - duration_ms
  - timestamp

## 8) Quality Requirements (Output)
- Outputs must be:
  - specific (not generic fluff)
  - evidence-linked (tie back to input)
  - internally consistent (themes align with opportunities/PRD)
  - action-oriented for PM execution

## 9) Milestones

### Milestone A: Foundation (done/in progress)
- FastAPI app factory + `/health`
- OpenRouter client wrapper
- Initial tests

### Milestone B: Core Analyze MVP
- Strict `/analyze` schema
- Deterministic mock output
- JSON run persistence
- Initial parser for model outputs

### Milestone C: Usability + Evals
- Simple UI or CLI flow
- Golden-set eval harness
- Cost/latency logging

### Milestone D: PM Utility
- Prioritization scoring
- Better PRD drafting constraints
- Markdown export

## 10) Success Metrics (v1)
- Time-to-first-useful-output: < 3 minutes.
- At least 70% of outputs judged “usable with minor edits” by Asif.
- Daily/near-daily usage cadence sustained for 2+ weeks.
- One portfolio-grade case study generated from real runs.

## 11) Open Questions
- Best frontend mode for v1 (CLI vs lightweight web form)?
- Should prioritization score ship in v1.1 or v2?
- Should we add source-specific templates (support tickets vs reviews) early?

## 12) Implementation Constraints
- Keep scope tight for 5 hours/week cadence.
- Prioritize deterministic behavior and stable contracts over feature breadth.
- Build in small, shippable increments that can be demonstrated publicly.
