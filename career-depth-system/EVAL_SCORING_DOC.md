# Eval Rubric / Scoring Doc

Purpose: evaluate generated artifacts — especially AI workflow research write-ups, summaries, briefs, and content drafts — in a way that is repeatable, explicit, and useful for publish decisions.

Owner: Asif  
Operator: Ubuntu

---

## Why this exists

We do not want to judge outputs by vibe alone.

This scoring doc exists to answer 3 questions:

1. **Is this artifact actually good?**
2. **Is this artifact better than the previous version?**
3. **Should this artifact be published, edited, or rejected?**

The goal is not academic rigor. The goal is practical quality control.

---

## Default evaluation modes

### 1. Single-artifact scoring
Use when evaluating one output on its own.

Examples:
- a Wednesday workflow report
- a LinkedIn draft
- a summary doc
- a prompt/system spec

### 2. Pairwise comparison
Use when comparing:
- old version vs new version
- baseline pipeline vs improved pipeline
- prompt A vs prompt B
- pre-eval output vs post-eval output

### 3. Publish gate
Use when deciding whether something should be:
- published automatically
- published with edits
- held back for review

---

## Core scoring dimensions

Score each dimension from **1 to 5**.

### 1. Topic fidelity
How tightly does the artifact match the intended topic/task?

- **1** = mostly off-topic or confused
- **2** = partially on-topic but drifts badly
- **3** = broadly on-topic but generic
- **4** = clearly aligned and mostly focused
- **5** = tightly aligned, no meaningful drift

### 2. Source quality / grounding
How well grounded is the output in credible source material or evidence?

- **1** = unsupported, junky, irrelevant, or fabricated feeling
- **2** = weak grounding, low-quality or mismatched sources
- **3** = usable but vendor-heavy / mixed quality / shallow evidence
- **4** = good grounding with relevant evidence and caveats
- **5** = strong, credible, well-matched evidence with limitations clearly acknowledged

### 3. Specificity
How concrete is the output?

- **1** = buzzwords and vague claims
- **2** = some specifics but mostly fluff
- **3** = mixed; some practical details, still generic in places
- **4** = concrete, practical, implementation-aware
- **5** = highly specific, operational, and clearly actionable

### 4. First-pilot quality
How good is the “best first step” or recommended first implementation?

- **1** = no credible first move
- **2** = unrealistic or too broad
- **3** = plausible but weakly scoped
- **4** = realistic first pilot with sensible boundaries
- **5** = excellent first pilot with clear scope, logic, and measurable outcome

### 5. Operational usefulness
Could someone actually use this artifact to do work?

- **1** = mostly useless in practice
- **2** = interesting but not operational
- **3** = somewhat useful summary, still requires major interpretation
- **4** = useful working artifact with clear practical value
- **5** = directly usable for execution, planning, or decision-making

### 6. Style / fit
How well does it fit the intended medium or repo style?

- **1** = wrong tone/structure for the target destination
- **2** = awkward fit, poor structure, or generic voice
- **3** = acceptable but bland or inconsistent
- **4** = strong fit for the target style
- **5** = highly aligned with the desired format, tone, and standard

---

## Optional advanced dimensions

Use these only when needed.

### 7. Novelty / insight
Does the artifact contain real insight, or is it obvious/regurgitated?

### 8. Comparison quality
If this is a comparative artifact, does it compare options meaningfully?

### 9. Constraint handling
Did the output respect the explicit rules, boundaries, and required sections?

### 10. Evidence-to-claim discipline
Do the claims stay proportional to the evidence, or does it overclaim?

---

## Score interpretation

### Base score
With the 6 core dimensions, max score = **30**.

### Decision thresholds
- **27–30** → **Publish**
- **22–26** → **Publish with edits**
- **21 or below** → **Reject / require review**

---

## Hard-fail conditions

Even if the score looks acceptable, reject if any of these are true:

- obvious topic mismatch
- obviously irrelevant links or evidence
- broken markdown / missing required structure
- no credible first use case / next step
- major hallucinated claim presented as fact
- evidence is too weak for the certainty level of the writing

---

## Pairwise comparison method

When comparing **old vs new**, score both independently first.
Then answer:

1. Which one is more grounded?
2. Which one is more specific?
3. Which one is more useful operationally?
4. Which one is more publishable?
5. Why?

### Pairwise verdict labels
- **New clearly better**
- **New somewhat better**
- **Roughly equal**
- **Old somewhat better**
- **Old clearly better**

### Pairwise comment format
Use this short structure:

- **Winner:**
- **Why it won:**
- **What is still weak:**
- **What the next iteration should improve:**

---

## Recommended evaluation output format

```json
{
  "scores": {
    "topic_fidelity": 4,
    "source_quality": 3,
    "specificity": 4,
    "pilot_quality": 4,
    "operational_usefulness": 4,
    "style_fit": 4
  },
  "total": 23,
  "verdict": "publish-with-edits",
  "hard_fail": false,
  "reasons": [
    "source set is still vendor-heavy",
    "good first pilot but KPI section could be sharper"
  ]
}
```

---

## Recommended pairwise output format

```json
{
  "old_total": 18,
  "new_total": 24,
  "winner": "new",
  "strength_delta": {
    "grounding": "+2",
    "specificity": "+1",
    "usefulness": "+2"
  },
  "verdict": "new somewhat better",
  "why": [
    "new version is more grounded in evidence",
    "new version has a more realistic first pilot",
    "new version still needs stronger source quality"
  ]
}
```

---

## Heuristics for our current workflow reports

For `AI Business Workflows` write-ups, apply these practical rules:

### Good signs
- names a realistic workflow, not just a generic AI capability
- includes approval/guardrail logic where needed
- recommends a believable first pilot
- KPIs are measurable, not decorative
- acknowledges when evidence is vendor-heavy
- source links look relevant to the weekday topic

### Bad signs
- “AI will transform everything” language
- generic use cases that fit any function
- source list with obvious junk or loose relevance
- first pilot too broad or too magical
- claims that go beyond the source quality

---

## Current blind spots in our evaluator

This doc is a living scoring standard. Right now the evaluator is still too generous in some places.

Known weak spots:
- not enough penalty for polished-but-generic writing
- not enough domain weighting for source trust
- not enough punishment for vendor-blog overreliance
- not enough reward for transcript-backed or evidence-bundle-backed claims

So: use the numeric score, but still apply judgment.

---

## Working principle

This is not a beauty contest.

The right question is:

> Would a smart operator actually trust and use this artifact?

If not, the score should reflect that.
