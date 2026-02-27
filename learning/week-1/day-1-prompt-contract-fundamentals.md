# Day 1 Learning Material — Prompt Contract Fundamentals

## Objective (Today)
Learn how to design a **prompt contract** for an AI feature so outputs are reliable, testable, and useful for product decisions.

By the end of this learning block, you should be able to:
- define a clear role/task for the model,
- specify input constraints,
- specify output schema and acceptance criteria,
- identify top failure modes before implementation.

---

## 1) What is a Prompt Contract?
A prompt contract is a **product-level agreement** between your system and the model:

- **What the model should do** (task)
- **What input it receives** (input schema + constraints)
- **What output shape is required** (JSON schema)
- **What quality bar must be met** (acceptance checks)
- **What to do when things fail** (fallback/error behavior)

Think of it like an API contract for model behavior.

---

## 2) Why this matters for AI PM work
Without a prompt contract, teams get:
- inconsistent outputs,
- hallucinated fields,
- poor handoff to engineering,
- impossible-to-measure quality.

With a contract, you get:
- deterministic interface for downstream systems,
- measurable eval criteria,
- faster iteration (you know what failed),
- better trust in production.

---

## 3) Contract Structure You Should Use
Use this 6-part structure every time:

1. **User job-to-be-done**
2. **Model role + task framing**
3. **Input schema + hard constraints**
4. **Output schema + required keys**
5. **Acceptance criteria (quality checks)**
6. **Failure modes + fallback rules**

---

## 4) Example (Insight2Spec: feedback → themes/opportunities)

### 4.1 User job-to-be-done
“As a PM, I want messy user feedback converted into clear themes and opportunity statements so I can prioritize roadmap actions quickly.”

### 4.2 Role + task framing
- Role: senior product insights analyst
- Task: analyze feedback and return structured insights only
- Constraint: no extra prose outside JSON

### 4.3 Input schema (minimum)
```json
{
  "feedback": ["string"],
  "product_context": "string",
  "target_user": "string"
}
```

### 4.4 Output schema (minimum)
```json
{
  "themes": [
    {"name": "string", "evidence": ["string"], "confidence": 0.0}
  ],
  "opportunities": [
    {"statement": "string", "impact": "high|medium|low", "linked_themes": ["string"]}
  ],
  "missing_context": ["string"]
}
```

### 4.5 Acceptance checks
- Must return valid JSON.
- Must include at least 3 themes when input has sufficient signal.
- Every opportunity must map to at least one theme.
- Confidence values must be numeric and bounded.
- No claims without evidence snippets from input.

### 4.6 Failure modes
- Empty/invalid JSON
- Generic themes with no evidence
- Opportunities disconnected from themes
- Hallucinated product context
- Missing required keys

Fallback rule: return structured error and request clarifying context.

---

## 5) PM Lens: What to evaluate every iteration
For each run, evaluate:
- **Quality**: useful and specific?
- **Consistency**: same schema every time?
- **Actionability**: can PM act on it immediately?
- **Trust**: evidence-backed, low hallucination?
- **Cost/latency**: good enough for real workflow?

---

## 6) Common Mistakes to Avoid
- “Be helpful” prompts with no schema.
- Mixing multiple tasks in one prompt.
- Not defining edge-case behavior.
- Letting model output free-form text when systems need JSON.
- Shipping without acceptance criteria.

---

## 7) Quick Self-Test (5 mins)
Before build, answer:
1. What are the 3 required output keys for your feature?
2. What is one non-negotiable acceptance check?
3. What failure mode is highest risk in production?
4. What fallback response should happen on parse failure?

If you can answer these clearly, you’re ready for build.

---

## 8) Build Handoff (what you’ll do next)
After reading this, your build task is to create:
- `docs/prompt-contract-v1.md`

Must include:
- role + task framing
- input schema
- output schema
- 8 acceptance checks
- 5 failure modes

Keep it tight, concrete, and implementation-ready.
