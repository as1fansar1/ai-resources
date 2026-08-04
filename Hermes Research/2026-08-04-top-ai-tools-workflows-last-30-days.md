# Top AI tools and workflows — last 30 days

Research date: **2026-08-04 08:00:40 EDT**
Window: **2026-07-05 through 2026-08-04** (rolling 30 days)
Scope: coding agents/devtools, agent infrastructure, browser/computer use, research/knowledge, design/media, business automation, open/local models, workspace agents, sales/GTM, and privacy/security.

## Executive summary

The most important change since the July 31 report is not another frontier model. It is the **July 28 MCP 2.0/stateless revision**, followed by an immediate compatibility wave in the MCP Python SDK, GitHub MCP Server, gateways, and practitioner-built clients. The practical implication is that MCP is becoming simpler to deploy and easier to constrain than a general-purpose shell with unrestricted internet access.

Four themes dominate the rolling window:

1. **The agent harness is the product.** Durable context, scoped tools, sandboxes, tests, traces, approval gates, and an independent reviewer matter more than model leaderboard position.
2. **Agents are moving from chat to finished artifacts.** ChatGPT Work, Notion post-meeting triggers, NotebookLM agentic research, Canva Code 2.0, and Runway Dev all turn goals or source material into documents, apps, tickets, or media pipelines.
3. **Controlled autonomy is winning.** The most credible browser and coding patterns validate one item first, use small batches, keep writes narrow, and retain human review for external or irreversible actions.
4. **Routing is spreading beyond text.** Teams are routing premium planners versus cheaper workers, while Runway applies cost/quality/latency routing to image, video, and audio generation.

**Net recommendation:** try MCP 2.0 migration and a review-gated coding loop now; pilot artifact-producing workspace agents on read-first workflows; monitor open frontier models and consumer computer-use agents until serving cost, permissions, and reliability are clearer.

## Scoring methodology

Scores use the requested 100-point rubric: **recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance 10**. Scores were calculated from the component values shown below. Deductions were applied for vendor-only claims, beta or phased availability, unsafe permission models, unclear licensing, and missing independent adoption evidence. GitHub stars/downloads are a current snapshot, not a 30-day growth claim.

## Top themes

- **MCP reset:** stateless HTTP, protocol negotiation, smaller response surfaces, and official server upgrades make typed tools more operationally attractive.
- **Plan–execute–verify loops:** the best coding workflow remains a written specification, small bounded implementation, automated checks, exact diff review, and deliberate memory updates.
- **Context compression:** codebase graphs and selective tool-response fields reduce repeated repository scans and keep agents within useful context budgets.
- **Forkable execution:** checkpointing a prepared sandbox and forking parallel attempts is emerging as a practical agent architecture.
- **Event-driven workspace agents:** meeting summaries, Slack bug reports, schedules, and connected-app changes are becoming triggers—not just context.
- **Editable generation:** Canva and Runway emphasize reviewable, reusable, brand-controlled outputs rather than one-shot generation.

## Top 15 ranked tools and workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | MCP Python SDK v2 + stateless, least-privilege tools | 96 | **Try now / migrate deliberately** |
| 2 | Hermes Agent v0.20 grounded research + artifacts + webhooks/A2A | 95 | **Try now** |
| 3 | Review-gated coding: spec → plan → small change → tests → diff | 94 | **Try now** |
| 4 | ChatGPT Work: connected context → finished business artifact | 93 | **Pilot now** |
| 5 | Claude Opus 5 as premium planner/reviewer | 92 | **Try now with task evals** |
| 6 | codebase-memory-mcp for structural repository context | 91 | **Try on a large repo** |
| 7 | OpenCode as an open, provider-flexible coding harness | 90 | **Try now** |
| 8 | E2B checkpoint-and-fork sandboxes for parallel agent attempts | 90 | **Pilot now** |
| 9 | GitHub MCP Server with selective fields and scoped writes | 89 | **Try now** |
| 10 | Validated browser automation: visible Playwright/browser-use + small batches | 89 | **Pilot carefully** |
| 11 | Canva Code 2.0: prompt/HTML → visual edit → stakeholder review | 88 | **Try now** |
| 12 | Runway Dev + Media Router for governed media pipelines | 87 | **Pilot now** |
| 13 | Notion AI Meeting Notes → Custom Agent follow-through | 87 | **Try on one team** |
| 14 | NotebookLM agentic, source-grounded research loop | 86 | **Pilot if available** |
| 15 | Kimi K3 long-context multimodal open-weight backend | 84 | **Monitor / benchmark** |

## Detailed findings

### 1. MCP Python SDK v2 + stateless, least-privilege tools

**Score:** 96 = 15/18/15/20/9/9/10
**Category:** agent infrastructure / security · **Recommendation:** Try now; pin and migrate deliberately

**Why it matters:** Stable v2 shipped July 28 alongside the 2026-07-28 MCP revision. Stateless requests reduce server complexity, while protocol negotiation and typed, minimal tools offer a more auditable alternative to unrestricted shell-and-network access. The repository had **23,884 stars** at research time.

**Evidence:** [stable v2 release, Jul 28](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0); [v2 RC and migration details, Jul 27](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0rc1); [Simon Willison’s stateless MCP implementation notes, Jul 31](https://simonwillison.net/2026/Jul/31/stateless-mcp/).

**Practical workflow:** (1) inventory current MCP clients/servers and dependency pins; (2) expose only narrow typed operations—read-only first; (3) migrate in a branch using the official guide; (4) test stdio and HTTP, auth, schemas, version negotiation, and response limits; (5) log tool calls; (6) add writes as separate confirmation-gated tools.

**Best next step:** run one stateless read-only server against a non-sensitive Datasette or internal documentation source before migrating privileged servers.

### 2. Hermes Agent v0.20 grounded research + artifacts + webhooks/A2A

**Score:** 95 = 15/19/14/20/8/9/10
**Category:** coding/research agent platform · **Recommendation:** Try now

**Why it matters:** The August 3 “Herald” release combines grounded citations and fact-checking, sandboxed desktop artifacts, signed outbound webhooks, A2A v1.0, stronger CLI project context, and mid-turn steering. That is a credible shift from chat agent to integrated workbench. GitHub showed **225,218 stars** and **43,697 forks** at research time.

**Evidence:** [Hermes Agent v0.20.0, Aug 3](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3); [v0.19.1 infrastructure release, Jul 30](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.30); [repository](https://github.com/NousResearch/hermes-agent).

**Practical workflow:** create a versioned research brief; collect and verify citations; render the result as an artifact; emit a signed completion webhook to a downstream system; let A2A or a subagent handle an independent task; use mid-turn redirect rather than restarting when priorities change.

**Best next step:** benchmark grounded-citation mode on one recurring report against the existing manual citation-check process.

### 3. Review-gated coding: spec → plan → small change → tests → diff

**Score:** 94 = 14/18/15/20/9/9/9
**Category:** coding workflow · **Recommendation:** Try now

**Why it matters:** Practitioner sources converge on bounded loops rather than one-shot autonomy. Anthropic reports its internal Claude Tag lands **65% of product-engineering PRs**, but critical changes still receive manual review. OpenAI published a Codex agentic-coding bootcamp on July 31.

**Evidence:** [OpenAI Codex Bootcamp, Jul 31](https://academy.openai.com/en/public/videos/codex-bootcamp-101-agentic-coding-2026-07-31); [Claude Code team interview, Jul 21](https://simonwillison.net/2026/Jul/21/cat-and-thariq/); [Ben’s Bites field notes, Jul 14](https://www.bensbites.com/p/how-to-use-gpt-56).

**Practical workflow:** put commands, boundaries, and acceptance criteria in `AGENTS.md`/`SPEC.md`; request an inspect-only plan; authorize one cohesive change; run tests/lint; inspect the exact diff; use a separate reviewer for risky changes; store repeated corrections as concise project instructions.

**Best next step:** add an explicit “tests run + exact diff + unresolved risks” section to every agent-generated PR.

### 4. ChatGPT Work: connected context → finished business artifact

**Score:** 93 = 13/19/15/20/9/9/8
**Category:** productivity/workspace agent · **Recommendation:** Pilot now

**Why it matters:** ChatGPT Work can stay with multi-hour tasks, use connected files/apps, and produce sheets, slides, documents, sites, and web apps. OpenAI reports more than **5 million weekly Codex users**, including more than **1 million** using it outside conventional programming; treat those as vendor metrics.

**Evidence:** [OpenAI launch, Jul 9](https://openai.com/index/chatgpt-for-your-most-ambitious-work/); [Reuters/CNA coverage, Jul 9](https://www.channelnewsasia.com/business/openai-launches-chatgpt-work-deepening-race-workplace-ai-tools-6244621); [The Rundown workflow coverage, Jul 10](https://www.therundown.ai/p/openai-sends-gpt-5-6-to-work).

**Practical workflow:** connect only approved read sources; give a known job such as a month-end variance pack or campaign brief; require citations/source links for analysis; review generated sheets/slides; approve any send/update action separately; track spend and rework.

**Best next step:** pilot a read-first weekly business report where the human already knows the expected numbers and format.

### 5. Claude Opus 5 as premium planner/reviewer

**Score:** 92 = 12/18/15/20/8/10/9
**Category:** frontier model / coding and knowledge work · **Recommendation:** Try with task-specific evals

**Why it matters:** Opus 5 launched July 24 with explicit effort controls and broad Claude/API/Copilot distribution. The practical pattern is not “use the most expensive model everywhere,” but give it planning, ambiguous judgment, root-cause analysis, and final review while cheaper workers perform bounded execution.

**Evidence:** [Anthropic announcement, Jul 24](https://www.anthropic.com/news/claude-opus-5); [GitHub Copilot availability, Jul 24](https://github.blog/changelog/2026-07-24-claude-opus-5-is-now-available-in-github-copilot/); [Artificial Analysis coverage](https://artificialanalysis.ai/articles/opus-5).

**Practical workflow:** have Opus create the spec, decision log, risk list, and verification checklist; delegate mechanical coding or browsing; return artifacts and test output; let Opus inspect the diff/results; escalate only failed checks and true ambiguities.

**Best next step:** compare low/high/xhigh effort on ten real tasks and select routes by task success and total cost—not benchmark rank.

### 6. codebase-memory-mcp for structural repository context

**Score:** 91 = 13/17/14/19/8/10/10
**Category:** coding agents / memory · **Recommendation:** Try on a large repository

**Why it matters:** v0.9.0 added Windows support, large-repository indexing resilience, memory-safety improvements, and broader extraction correctness. Current evidence showed **37,388 stars**, plus substantial binary-download counts. A structural graph can replace repeated full-repo scans with targeted queries about definitions, callers, routes, and architecture.

**Evidence:** [v0.9.0, Jul 8](https://github.com/DeusData/codebase-memory-mcp/releases/tag/v0.9.0); [repository](https://github.com/DeusData/codebase-memory-mcp); [July trending analysis](https://www.analyticsvidhya.com/blog/2026/07/trending-ai-github-repositories/).

**Practical workflow:** index a representative large repo; ask the coding agent for architecture/caller/route queries before edits; compare context use and answer accuracy against baseline file search; refresh the graph in CI or before sessions; invalidate on parser/index failures.

**Best next step:** measure retrieval accuracy and token use on five known architectural questions before making it default.

### 7. OpenCode as an open, provider-flexible coding harness

**Score:** 90 = 15/18/12/19/7/10/9
**Category:** coding agents/devtools · **Recommendation:** Try now

**Why it matters:** OpenCode maintained a dense release cadence through August 4 and had **193,155 stars** at research time. Its value is an open, BYOK/provider-flexible harness for implementation/test loops and as a reference point against proprietary coding agents.

**Evidence:** [OpenCode releases](https://github.com/anomalyco/opencode/releases); [v1.18.8, Jul 28](https://github.com/anomalyco/opencode/releases/tag/v1.18.8); [repository](https://github.com/anomalyco/opencode).

**Practical workflow:** run in a branch or worktree; supply a project instruction file and allowed commands; select models by task; require tests and exact diffs; use CI and code-owner review before merge.

**Best next step:** run the same five repository tasks in OpenCode and the current default agent, then compare success, cost, regressions, and supervision time.

### 8. E2B checkpoint-and-fork sandboxes

**Score:** 90 = 13/15/15/19/10/9/9
**Category:** agent infrastructure / sandboxes · **Recommendation:** Pilot now

**Why it matters:** The July 17 Python SDK added `sandbox.fork()`, checkpointing a running environment and creating multiple independent forks. This makes parallel agent attempts practical without repeatedly rebuilding dependencies and state.

**Evidence:** [E2B Python SDK 2.34.0, Jul 17](https://github.com/e2b-dev/E2B/releases/tag/%40e2b%2Fpython-sdk%402.34.0); [E2B releases](https://github.com/e2b-dev/E2B/releases); [repository](https://github.com/e2b-dev/E2B).

**Practical workflow:** prepare one clean sandbox; install dependencies and tests; checkpoint; fork two or three bounded approaches; run identical acceptance checks; select the passing diff; discard all forks and secrets after the job.

**Best next step:** use forks for a flaky bug or migration where two implementation strategies can be evaluated by the same test suite.

### 9. GitHub MCP Server with selective fields and scoped writes

**Score:** 89 = 15/16/15/18/7/9/9
**Category:** developer workflow / MCP · **Recommendation:** Try now

**Why it matters:** v1.8.0 added a `fields` parameter so models can request only needed response fields, reducing context waste. v1.7 added GitHub App server-to-server authentication and lockdown improvements. The v1.8 assets showed thousands of platform downloads, while the repo had **31,948 stars**.

**Evidence:** [v1.8.0, Jul 30](https://github.com/github/github-mcp-server/releases/tag/v1.8.0); [v1.7.0, Jul 23](https://github.com/github/github-mcp-server/releases/tag/v1.7.0); [repository](https://github.com/github/github-mcp-server).

**Practical workflow:** use a dedicated GitHub App; grant access only to required repos; default to read tools and selective fields; expose draft-issue/PR writes separately; require confirmation for updates, merges, project changes, or releases; retain audit logs.

**Best next step:** replace a broad personal token with a repo-scoped GitHub App in one agent workflow.

### 10. Validated browser automation: visible Playwright/browser-use + small batches

**Score:** 89 = 13/18/15/19/7/10/7
**Category:** browser/computer-use agents · **Recommendation:** Pilot carefully

**Why it matters:** Browser-use shipped four July releases and had **107,821 stars**; the official Playwright MCP gives structured, visible browser control. Practitioner guidance converges on a safer norm: define an SOP, manually authenticate, validate the first item, then run only a small batch.

**Evidence:** [browser-use v0.13.7, Jul 27](https://github.com/browser-use/browser-use/releases/tag/0.13.7); [Playwright MCP](https://github.com/microsoft/playwright-mcp); [Ben’s Bites computer-use notes, Jul 14](https://www.bensbites.com/p/how-to-use-gpt-56).

**Practical workflow:** use a disposable browser profile/account; open a visible browser; authenticate manually; give exact page/action/stop rules; complete one item; inspect it; process 3–10 more; require confirmation for submissions, purchases, permission changes, or publication.

**Best next step:** automate a reversible QA or reporting task—not payments, HR, or account administration.

### 11. Canva Code 2.0: prompt/HTML → visual edit → stakeholder review

**Score:** 88 = 12/18/15/19/9/9/6
**Category:** design/media/content · **Recommendation:** Try now

**Why it matters:** Canva Code 2.0 turns prompts, templates, or imported HTML into interactive sites/apps that non-developers can edit visually. Canva reports **265 million monthly users** and more than **6 million sites** created with Canva Code; these are company metrics but indicate strong distribution.

**Evidence:** [Canva launch, Jul 14](https://www.canva.com/newsroom/news/Canva-Code/); [VentureBeat coverage](https://venturebeat.com/technology/canva-launches-code-2-0-offering-ai-website-building-to-every-user-including-free-accounts).

**Practical workflow:** generate a campaign landing page, calculator, or demo; apply Brand Kit and direct visual edits; review collaboratively; publish only after accessibility, analytics, security, privacy, and backend checks.

**Best next step:** create one interactive campaign prototype and measure stakeholder-edit time versus the current design/development handoff.

### 12. Runway Dev + Media Router

**Score:** 87 = 12/16/15/19/10/8/7
**Category:** media infrastructure · **Recommendation:** Pilot now

**Why it matters:** Runway Dev offers a unified API for first- and third-party image/video/audio/character models; Media Router selects among them using price caps, allow/deny lists, and cost/quality/latency preferences. Dry runs expose the selected model before spending.

**Evidence:** [Runway Dev, Jul 23](https://runwayml.com/news/introducing-runway-dev); [Media Router, Jul 23](https://runwayml.com/news/company-news/introducing-runway-media-router); [TechCrunch coverage](https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/).

**Practical workflow:** define `preview-fast` and `final-quality` configs; set approved providers and price caps; dry-run a benchmark prompt set; route drafts and finals separately; log chosen models; perform human brand, relevance, rights, and safety review.

**Best next step:** benchmark one recurring ad-localization or product-visual task across two router policies.

### 13. Notion AI Meeting Notes → Custom Agent follow-through

**Score:** 87 = 15/15/12/19/9/8/9
**Category:** business automation / workspace · **Recommendation:** Try on one team

**Why it matters:** As of July 31, a summarized AI Meeting Note can trigger a Custom Agent to update a tracker, post a recap, or create tickets. This is a concrete event-driven handoff from conversation to operations.

**Evidence:** [Notion release, Jul 31](https://www.notion.com/releases/2026-07-31); [calendar tools, Jul 16](https://www.notion.com/releases/2026-07-16).

**Practical workflow:** select one recurring internal meeting; trigger only after summary completion; write decisions/owners into a tracker; draft—rather than immediately send—external recaps; queue ticket creation for review; audit errors weekly.

**Best next step:** begin with internal project-status updates and measure missed/incorrect actions for four meetings before widening scope.

### 14. NotebookLM agentic, source-grounded research

**Score:** 86 = 13/16/12/20/9/8/8
**Category:** research/knowledge workflow · **Recommendation:** Pilot if available

**Why it matters:** Google’s July 16 update adds agentic chat and a secure cloud computer for code/analysis, while retaining NotebookLM’s source-centered workflow. It is well suited to research that starts with a bounded corpus and must end in inspectable citations and artifacts.

**Evidence:** [Google NotebookLM research update, Jul 16](https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/); [Gemini July Drop, Jul 31](https://blog.google/products-and-platforms/products/gemini/gemini-drop-july-2026/).

**Practical workflow:** define the question and date range; upload/collect the approved corpus; let the agent organize sources and run analysis; inspect citations and generated code/artifacts; independently verify decisive claims; publish from a single reviewed draft.

**Best next step:** compare it with the current Perplexity/NotebookLM research loop on a question with a known answer and known source set.

### 15. Kimi K3 long-context multimodal open-weight backend

**Score:** 84 = 15/15/13/17/9/8/7
**Category:** open/local models · **Recommendation:** Monitor / benchmark

**Why it matters:** Kimi K3 appeared July 27 with native vision, a reported one-million-token context window, and an MoE architecture. Hugging Face showed **1,125,935 downloads in the prior month** and **9,954 likes** at research time—substantial momentum for a new open-weight release.

**Evidence:** [Hugging Face model card](https://huggingface.co/moonshotai/Kimi-K3); [paper record, Jul 27](https://huggingface.co/papers/2607.24653); [Simon Willison’s Kimi K3 analysis, Jul 21](https://simonwillison.net/2026/Jul/21/kimi-k3/).

**Practical workflow:** use a hosted compatible endpoint or properly sized serving stack; benchmark long-document, visual, coding, and tool-use tasks against the incumbent; measure quality, latency, total serving cost, and license fit; keep fallback routing.

**Best next step:** monitor unless there is a clear long-context/private-deployment need—the total model size makes “local” impractical for most individuals.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agents/devtools | Review-gated coding loop | Most transferable route to reliable delivery across Claude, Codex, Hermes, or OpenCode. |
| Agent infrastructure | MCP v2 + least-privilege tools | Simpler stateless deployment and a more auditable capability surface. |
| Browser/computer use | Visible Playwright/browser-use small-batch workflow | Structured inspection plus human authentication and first-item validation. |
| Research/knowledge | NotebookLM agentic source loop | Strong corpus grounding and artifact/code capability, subject to plan availability. |
| Design/media/content | Runway Dev + Media Router | Operationalizes multi-model creative work with explicit constraints and dry runs. |
| Business automation | Notion meeting-summary trigger | Clear event-to-action loop with a natural review point. |
| Open/local models | Kimi K3 | Strongest current momentum, but hardware and licensing keep it in benchmark/monitor status. |
| Productivity/workspace | ChatGPT Work | Broadest finished-artifact workflow and cross-surface distribution. |
| Sales/GTM | Research → qualify → draft → approval → CRM queue | High upside while preserving human control over outreach and CRM truth. |
| Privacy/security | E2B forked sandboxes + scoped identity | Practical isolation pattern; Kubernetes Agent Sandbox wins for governed multi-tenant deployments. |

## Rising but less proven

- **agentgateway 1.4:** centralized MCP/LLM routing, OAuth, policy, and cost control are strategically useful, but the gateway becomes critical security infrastructure. [v1.4.1, Jul 29](https://github.com/agentgateway/agentgateway/releases/tag/v1.4.1)
- **Kubernetes Agent Sandbox:** promising CRD-based, warm-pool isolation with gVisor examples; operational complexity remains high. [v0.5.2, Jul 17](https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v0.5.2)
- **Arize Phoenix 19.x:** rapid July release cadence and strong open observability stack; validate schema stability and telemetry redaction. [v19.10.0, Jul 28](https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v19.10.0)
- **Langfuse v4:** self-hosted search, monitoring, and faster APIs are useful, but traces often contain secrets and personal data. [v4.0.0, Jul 29](https://github.com/langfuse/langfuse/releases/tag/v4.0.0)
- **OfficeCLI:** one binary for agent-native Word/Excel/PowerPoint editing is compelling; fidelity and formula/macro handling need regression tests. [releases](https://github.com/iOfficeAI/OfficeCLI/releases)
- **NVIDIA Nemotron 3 Embed:** attractive open retrieval/model-memory option with vendor-reported RTEB strength; reindexing and domain evaluation are required. [HF launch, Jul 16](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb)
- **mLateOn/mDenseOn:** compact multilingual/code retrieval models with an open recipe; late interaction increases indexing and serving cost. [HF launch, Jul 30](https://huggingface.co/blog/lightonai/mdenseon-mlateon)
- **Persistent lead/researcher/maker rooms:** visible handoffs beat hidden swarms, but tutorial interest is ahead of measured production evidence. [Rundown, Jul 30](https://www.therundown.ai/p/openai-escaped-ai-claims-another-victim)

## Overhyped / be careful

- **Unsupervised credentialed browser agents:** prompt injection, incorrect clicks, and account lockouts make unrestricted autonomy inappropriate for payments, HR, security settings, or publishing.
- **“Agent team” demos without evals:** more agents can increase cost, duplicated work, and coordination failure. Parallelize independent collection—not final synthesis.
- **Fully automated content factories:** queueing and reconciliation are useful; high-volume low-quality publishing, rights problems, and platform-policy violations are not.
- **Open-weight = local/private:** a million-token context and downloadable weights do not make a 2.8T-parameter model cheap to serve or commercially unrestricted.
- **Vibe-coded production apps:** visual editing is not a substitute for accessibility, authentication, data protection, observability, payments, and backend review.
- **Single-vendor sandbox/security claims:** use them as defense-in-depth, not as proof against egress, prompt injection, or privileged-tool abuse.
- **Persistent agent memory without hygiene:** incorrect or sensitive memories compound over time; memory needs provenance, retention rules, review, and deletion.

## Try-this-week shortlist

1. **MCP migration trial:** move one read-only internal data tool to MCP v2; test negotiation, schemas, logs, and least privilege.
2. **Coding control upgrade:** add `SPEC.md`, acceptance tests, narrow command permissions, exact-diff review, and a separate reviewer to one repository task.
3. **Context trial:** benchmark codebase-memory-mcp on five known architecture questions and compare context use with ordinary file search.
4. **Forked sandbox experiment:** prepare one E2B environment, fork two implementation approaches, and select only the version that passes the same test suite.
5. **Business artifact pilot:** run ChatGPT Work or NotebookLM on a read-first weekly report and verify every decisive number/source before distribution.
6. **Browser safety pattern:** automate one reversible 3–10 item batch in visible Playwright, validating the first item manually.
7. **Creative routing test:** compare `preview-fast` and `final-quality` policies for one Runway media job, including cost and human acceptance.

## Best workflow to keep doing this monthly

Maintain an **evidence-backed agent operating system**: a versioned brief and project memory, stable task/eval suite, explicit model-routing policy, typed least-privilege tools, disposable sandboxes, budgets and timeouts, logs/provenance, and a reviewer separate from the executor. Each month, rerun the same real tasks against the top two new tools/models and promote only changes that improve task success, safety, cost, and operator time.

## Raw candidate appendix

The following **56 deduplicated candidates** were collected before ranking. A candidate may be a tool, model, or workflow; inclusion is not an endorsement.

| Category | Candidate | In-window signal | Primary evidence |
|---|---|---|---|
| Coding/devtools | Hermes Agent v0.20 | Aug 3 release | [GitHub](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3) |
| Coding/devtools | OpenCode | Jul 20–Aug 4 release stream | [GitHub](https://github.com/anomalyco/opencode/releases) |
| Coding/devtools | Claude Code | Jul 19/25 releases | [GitHub](https://github.com/anthropics/claude-code/releases) |
| Coding/devtools | Review-gated Codex loop | Jul 31 bootcamp | [OpenAI Academy](https://academy.openai.com/en/public/videos/codex-bootcamp-101-agentic-coding-2026-07-31) |
| Coding/devtools | Claude Tag Slack bug-to-PR | Jul 21 interview | [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/) |
| Coding/devtools | codebase-memory-mcp | Jul 8 v0.9 | [GitHub](https://github.com/DeusData/codebase-memory-mcp/releases/tag/v0.9.0) |
| Coding/devtools | OfficeCLI | July release train | [GitHub](https://github.com/iOfficeAI/OfficeCLI/releases) |
| Coding/devtools | Mobile screenshot-to-PR | Jul 6 tutorial | [The Rundown](https://www.therundown.ai/p/meta-sizes-up-gpt-5-5-with-watermelon) |
| Agent infrastructure | MCP Python SDK v2 | Jul 28 stable | [GitHub](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0) |
| Agent infrastructure | GitHub MCP Server | Jul 23/30 releases | [GitHub](https://github.com/github/github-mcp-server/releases/tag/v1.8.0) |
| Agent infrastructure | agentgateway | Jul 27/29 releases | [GitHub](https://github.com/agentgateway/agentgateway/releases/tag/v1.4.1) |
| Agent infrastructure | OpenAI Agents SDK | Jul 27–Aug 4 releases | [GitHub](https://github.com/openai/openai-agents-python/releases) |
| Agent infrastructure | LangGraph | Jul 6/28 releases | [GitHub](https://github.com/langchain-ai/langgraph/releases) |
| Agent infrastructure | DeerFlow 2.0 | Jul 9 BoxLite benchmark work | [GitHub](https://github.com/bytedance/deer-flow) |
| Agent infrastructure | E2B sandbox fork | Jul 17 SDK release | [GitHub](https://github.com/e2b-dev/E2B/releases/tag/%40e2b%2Fpython-sdk%402.34.0) |
| Agent infrastructure | Kubernetes Agent Sandbox | Jul 17 v0.5.2 | [GitHub](https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v0.5.2) |
| Agent infrastructure | OpenClaw | Jul 13–Aug 1 releases | [GitHub](https://github.com/openclaw/openclaw/releases) |
| Browser/computer use | browser-use | Jul 11–27 releases | [GitHub](https://github.com/browser-use/browser-use/releases) |
| Browser/computer use | Playwright MCP | Jul 9 release signal | [GitHub](https://github.com/microsoft/playwright-mcp/releases) |
| Browser/computer use | Codex validated click-batch | Jul 14 practitioner signal | [Ben’s Bites](https://www.bensbites.com/p/how-to-use-gpt-56) |
| Browser/computer use | Gemini Spark Chrome | Jul 30 update | [Google](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/) |
| Browser/computer use | Record/replay narrow desktop task | Jul 14/27 coverage | [The Rundown](https://www.therundown.ai/p/anthropic-opus-5-surprise) |
| Research/knowledge | NotebookLM agentic research | Jul 16 update | [Google](https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/) |
| Research/knowledge | Perplexity Agent API | Jul 21 migration guidance | [Perplexity](https://community.perplexity.ai/t/your-sonar-workload-runs-better-on-agent-api/5634) |
| Research/knowledge | Perplexity Agent Skills | Jul 18 announcement | [Perplexity](https://community.perplexity.ai/t/skills-added-to-the-perplexity-agent-api/5612) |
| Research/knowledge | Open Deep Research | Jul 29 update | [LangChain](https://www.langchain.com/blog/open-deep-research) |
| Research/knowledge | OpenResearcher offline loop | Jul 20 coverage | [How AI Works](https://howaiworks.ai/blog/tiger-ai-lab-openresearcher-open-source) |
| Research/knowledge | Read-only connected-app weekly report | July practitioner guide | [The Rundown](https://app.therundown.ai/guides/build-automated-business-reports-with-ai-works-with-google-analytics-youtube-shopify-and-more) |
| Design/media/content | Canva Code 2.0 | Jul 14 launch | [Canva](https://www.canva.com/newsroom/news/Canva-Code/) |
| Design/media/content | Runway Dev | Jul 23 launch | [Runway](https://runwayml.com/news/introducing-runway-dev) |
| Design/media/content | Runway Media Router | Jul 23 launch | [Runway](https://runwayml.com/news/company-news/introducing-runway-media-router) |
| Design/media/content | Runway Agent 2.0 | Jul 17 post | [Runway](https://runwayml.com/news/engineering/inside-building-runway-agent) |
| Design/media/content | Meta Muse Image | Jul 7 launch | [Meta](https://about.fb.com/news/2026/07/introducing-muse-image-meta-ai/) |
| Design/media/content | GPT-Live / ChatGPT Voice | Jul 8/31 updates | [OpenAI](https://openai.com/index/introducing-gpt-live/) |
| Design/media/content | Claude Code + Remotion | Jul 15 practitioner guide | [Satura](https://saturaai.com/blog/claude-code-remotion-for-youtube-automation-lean-stock-footage-workflow-5n_zjq) |
| Design/media/content | Queue-first content factory | July implementation report | [DEV](https://dev.to/nextools/building-a-content-factory-with-claude-code-remotion-415h) |
| Business automation | Notion meeting-to-agent trigger | Jul 31 release | [Notion](https://www.notion.com/releases/2026-07-31) |
| Business automation | Claude M365 write tools | Jul 7 release notes | [Anthropic](https://docs.anthropic.com/en/release-notes/claude-apps) |
| Business automation | Microsoft Foundry procedural memory | Jul 16 update | [Microsoft](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/agents-can-learn-with-memory-in-microsoft-foundry-agent-service/4535431) |
| Business automation | n8n bounded email/CRM route | Jul 23 guide | [Leland](https://www.joinleland.com/library/a/n8n-ai-agent) |
| Business automation | Multi-agent SEO audit | Jul 23 guide | [The Rundown](https://www.therundown.ai/p/openai-cyber-test-escapes-the-lab) |
| Open/local models | Kimi K3 | Jul 27 release | [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3) |
| Open/local models | Aether-7B-5Attn | Jul 19 launch | [Hugging Face](https://huggingface.co/blog/FINAL-Bench/opensource-llm) |
| Open/local models | mLateOn/mDenseOn | Jul 30 launch | [Hugging Face](https://huggingface.co/blog/lightonai/mdenseon-mlateon) |
| Open/local models | Nemotron 3 Embed | Jul 16 launch | [Hugging Face](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) |
| Open/local models | Inkling-Small | Jul 15 launch | [Hugging Face](https://huggingface.co/blog/thinkingmachines-inkling) |
| Open/local models | NanoColibri-Instruct | Jul 29 launch | [Hugging Face](https://huggingface.co/blog/vovaRL/hybernation-models-blog) |
| Productivity/workspace | ChatGPT Work | Jul 9 launch | [OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) |
| Productivity/workspace | M365 Copilot GPT-5.6 | Jul 9 availability | [Microsoft](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/available-today-openai%E2%80%99s-gpt-5-6-in-microsoft-365-copilot/4533152) |
| Productivity/workspace | Claude Cowork remote sessions | Jul 7 release notes | [Anthropic](https://docs.anthropic.com/en/release-notes/claude-apps) |
| Productivity/workspace | Gemini July Drop | Jul 31 | [Google](https://blog.google/products-and-platforms/products/gemini/gemini-drop-july-2026/) |
| Productivity/workspace | Adobe Acrobat in WhatsApp | Jul 22 | [Adobe](https://blog.adobe.com/en/publish/2026/07/22/acrobat-brings-powerful-pdf-workflows-to-whatsapp) |
| Sales/GTM | Research→qualify→draft→CRM queue | Jul 16 pattern | [Airbyte](https://airbyte.com/agentic-data/gtm-agents) |
| Sales/GTM | ChatGPT Work lead-review system | Jul 9 case study | [OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) |
| Privacy/security | Arize Phoenix observability | Jul 23–31 releases | [GitHub](https://github.com/Arize-ai/phoenix/releases) |
| Privacy/security | Langfuse v4 | Jul 29/31 releases | [GitHub](https://github.com/langfuse/langfuse/releases) |

## Source and limitation notes

- **Source breadth:** official product/release pages, GitHub/API and release assets, Hugging Face model metadata/blogs, Hacker News/Show HN discovery, OpenAI Academy, Simon Willison, Ben’s Bites, The Rundown, and accessible secondary coverage were checked.
- **GitHub Trending:** “monthly” is directional rather than a precise rolling-window API. This report uses dated releases/commits plus current repository metrics; it does not claim that all current stars were added during the window.
- **Product Hunt:** accessible pages/results did not yield dependable July–August 2026 launch dates or upvote counts. No Product Hunt candidate was ranked rather than fabricating metrics.
- **YouTube:** publication dates/view counts were usually unavailable. The one verified first-party signal was OpenAI Academy’s July 31 Codex Bootcamp recording with **281 views** at research time; YouTube was treated as qualitative evidence.
- **Social:** Reddit, X, and LinkedIn were not used as primary evidence because access/login reliability was insufficient. Hacker News results with unverified dates were not used as top-item evidence.
- **Vendor metrics:** user counts, benchmark wins, performance improvements, and enterprise production claims are attributed to vendors unless independently corroborated. They should be validated in a scoped pilot.
- **Availability:** several features are regional, plan-limited, staged, beta, or enterprise-only. Verify pricing, data handling, permissions, retention, and actual tenant availability.
- **Security baseline:** use separate agent identities, least privilege/read-only first, scoped repos/worktrees, secrets outside prompt context, approval before external writes or consequential actions, durable logs, test/eval gates, and a named human owner.
