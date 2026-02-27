# 6-Month Technical Depth Plan — Week 1 & 2 (Daily Execution)

Owner: Asif  
Coach/Operator: Claw  
Daily timebox: 70 minutes (25 learn + 35 build + 10 reflect)

## Rules
- Ship one artifact daily (file, commit, test, or eval sheet update).
- No zero days: if blocked, do a 15-minute minimum shippable slice.
- End each day with one sentence: what improved + what’s next.

---

## Week 1 — Prompt Contracts + Structured Outputs

### Day 1 (Mon)
**Focus:** Prompt contract fundamentals  
**Task:** Create `docs/prompt-contract-v1.md` for one feature (`feedback -> themes/opportunities`).  
**Artifact:** `docs/prompt-contract-v1.md` with role, input, constraints, output keys, failure modes.

### Day 2 (Tue)
**Focus:** Input/output schema design  
**Task:** Define strict JSON schemas for request + response.  
**Artifact:** `docs/feature-schema-v1.md` with required fields + validation rules.

### Day 3 (Wed)
**Focus:** Acceptance criteria  
**Task:** Write 8 acceptance checks for output quality.  
**Artifact:** `docs/acceptance-checks-v1.md` + pass/fail template table.

### Day 4 (Thu)
**Focus:** Failure taxonomy  
**Task:** Document top 10 failure types (hallucination, missing fields, weak actionability, etc.).  
**Artifact:** `docs/failure-taxonomy-v1.md` with mitigation for each.

### Day 5 (Fri)
**Focus:** Eval-ready test set  
**Task:** Create 10 realistic test cases for one feature.  
**Artifact:** `evals/feature-x/test_cases.json` (or update `ai-eval-lab` suite).

### Day 6 (Sat)
**Focus:** Baseline scoring pass  
**Task:** Score all 10 cases with rubric.  
**Artifact:** `baseline_results.csv` + summary in `report.md`.

### Day 7 (Sun)
**Focus:** Weekly synthesis  
**Task:** Review all artifacts and pick top 2 recurring failures.  
**Artifact:** `docs/WEEK_1_REVIEW.md` with: wins, gaps, next-week priorities.

---

## Week 2 — API + Reliability + Eval Loop

### Day 8 (Mon)
**Focus:** Endpoint contract  
**Task:** Define `/analyze` request/response contract clearly in docs.  
**Artifact:** `docs/api-contract-analyze-v1.md`.

### Day 9 (Tue)
**Focus:** Error contracts  
**Task:** Add/verify structured error schema (`500/502/504`) and examples.  
**Artifact:** `docs/error-contract-v1.md` + curl samples.

### Day 10 (Wed)
**Focus:** Manual verification workflow  
**Task:** Create 2-minute test flow (`/health`, `/analyze mock`, `/analyze live`).  
**Artifact:** `docs/manual-verification.md`.

### Day 11 (Thu)
**Focus:** Eval iteration  
**Task:** Run baseline on 10 cases, apply one fix, re-test failed cases.  
**Artifact:** `improved_results.csv` + delta summary.

### Day 12 (Fri)
**Focus:** Quality decisioning  
**Task:** Define ship/iterate/hold decision thresholds.  
**Artifact:** `docs/decision-rules-v1.md`.

### Day 13 (Sat)
**Focus:** Reliability hardening  
**Task:** Add one guardrail and one fallback rule.  
**Artifact:** `docs/guardrails-fallbacks-v1.md` + implementation note in nightly log.

### Day 14 (Sun)
**Focus:** Week 2 review + next sprint plan  
**Task:** Score progress on 6 dimensions: schema, eval, API, reliability, shipping, clarity.  
**Artifact:** `docs/WEEK_2_REVIEW.md` + Week 3 target.

---

## How Claw will support daily
- Generate your daily sprint prompt at 9:00 Bali.
- Review your shipped artifact against rubric.
- Give one improvement target for next day.
- Enforce EOD accountability at 20:00 Bali.
- Keep all artifacts pushed to GitHub.

## Weekly success target (Week 1-2)
- 12+ shipped artifacts
- 1 complete eval loop (baseline + improved)
- 1 stable API contract with explicit error handling
- 1 recruiter/client-ready proof pack from real outputs
