# Top AI tools and workflows — last 30 days

Research date: **2026-08-07 14:51 EDT**
Window: **2026-07-08 through 2026-08-07** (rolling 30 days, inclusive)
Scope: coding agents/devtools, agent infrastructure, browser/computer use, research/knowledge, design/media, business automation, open/local models, productivity/workspace agents, sales/GTM, and privacy/security.

## Executive summary

This Friday scan adds several meaningful signals that were not available in Tuesday’s report: **AWS open-sourced Kiro Crew after reporting 39,000+ internal Amazon builders; Meta launched Muse Code; Prime Intellect released Prime Agent; Liquid AI released a 2.6B on-device agent model; OpenAI updated GPT-5.6 Sol and expanded free Luna access; and Salesforce launched Agentforce Coworker in Salesforce beta.**

The strongest conclusion is unchanged but now better evidenced: **the harness and operating workflow matter more than a model name.** The practical winners combine a premium planner/reviewer, cheaper or specialized workers, persistent context, isolated worktrees/sandboxes, tests, observable tool calls, explicit permissions, and human approval at consequential boundaries.

Five themes dominate:

1. **Persistent agent operations are becoming a product category.** Kiro Crew, Prime Agent, Nanobot, and emerging memory tools keep work alive across sessions, schedules, channels, and subagents.
2. **Agent economics now drive architecture.** GPT-5.6’s tiered pricing, DeepSeek V4 Flash, and planner–worker routing make cost-aware model assignment a first-class workflow decision.
3. **Coding agents are converging on plan → isolated execution → verification.** Kiro Crew, Muse Code, Codex/Claude practitioner workflows, and Microsoft’s Copilot Agent integration all reinforce this pattern.
4. **Browser agents are useful only with visible, narrow control.** Gemini Spark’s Chrome integration explicitly hands back payments; practitioners favor authenticated, reversible, small-batch tasks.
5. **Local AI is splitting into two useful tiers.** LFM2.5-2.6B targets fast on-device tool use; TurboFieldfare demonstrates specialized SSD-streamed inference for a much larger model on low-memory Macs. Both need real task evaluations.

**Net recommendation:** try a review-gated planner–worker coding loop and one persistent read-first agent workflow now; migrate MCP servers toward stateless, least-privilege operation; pilot Kiro Crew in a disposable repo; monitor self-modifying harnesses and local models until reliability and security are independently established.

## Scoring methodology

Scores use the requested 100-point rubric: **recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance 10**. Each detailed score shows those seven components in that order. Deductions were reflected in the component values for vendor-only benchmarks, beta/staged availability, missing independent adoption evidence, unsafe permission surfaces, or unclear operational maturity. GitHub stars and Hugging Face downloads are snapshots observed on August 7, not claims that all growth occurred inside the window.

## Top themes

- **The harness is the deployable unit:** model + tools + context policy + sandbox + tests + approvals + telemetry.
- **Persistent work replaces disposable chats:** sessions, checkpoints, schedules, heartbeats, durable memory, and resumable subagents are converging.
- **Premium judgment, economical execution:** use frontier models for ambiguity, planning, and final review; use cheaper models for bounded implementation, extraction, and retries.
- **Verification is the real autonomy unlock:** deterministic gates, CI, exact diffs, replayable browser timelines, and separate reviewers are more valuable than unconstrained “full auto.”
- **Credential isolation is moving outside the sandbox:** Perplexity SPACE’s node-level credential delivery is an important design pattern, though its performance/security claims remain vendor-reported.
- **Artifacts beat chat output:** Workspace agents increasingly end in a reviewed document, spreadsheet, site, ticket, PR, CRM update, or media timeline.

## Top 15 ranked tools and workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | Review-gated planner → worker → tests → independent review | 98 | **Try now** |
| 2 | ChatGPT Work + GPT-5.6 tiered model routing | 96 | **Pilot now** |
| 3 | MCP v2/stateless + least-privilege typed tools | 94 | **Try now / migrate deliberately** |
| 4 | Kiro Crew persistent engineering workspace | 92 | **Pilot now in a disposable repo** |
| 5 | Claude Opus 5 as premium planner/reviewer | 91 | **Try with task evals** |
| 6 | Meta Muse Code: isolated-worktree coding swarm | 91 | **Monitor / benchmark beta** |
| 7 | TurboFieldfare local Mac inference + agent endpoint | 89 | **Try if local Mac inference matters** |
| 8 | Perplexity SPACE: credential-isolated resumable sandboxes | 89 | **Monitor / borrow the architecture** |
| 9 | Gemini Spark Chrome: human-gated web errands | 88 | **Pilot carefully** |
| 10 | DeepSeek V4 Flash 0731 in an open coding harness | 88 | **Benchmark now; pin the version** |
| 11 | Prime Agent persistent REPL + continual harness | 86 | **Monitor / research pilot only** |
| 12 | Notion Meeting Notes → Custom Agent follow-through | 86 | **Try on one internal team** |
| 13 | Runway Dev + Media Router | 84 | **Pilot for governed media generation** |
| 14 | LFM2.5-2.6B on-device tool-using agent | 83 | **Monitor / edge pilot** |
| 15 | GitHub Copilot Agent + Microsoft Agent Framework | 80 | **Pilot for governed .NET/Python agents** |

## Detailed findings

### 1. Review-gated planner → worker → tests → independent review

**Score:** 98 = 15/19/15/20/9/10/10  
**Category:** coding agents/devtools · **Recommendation:** Try now

**Why it matters:** Independent sources now converge on the same reliable unit of work: a strong model turns a ticket into a bounded plan and acceptance tests; one or more workers implement in isolated branches/worktrees; automated checks run; a separate model or human reviews the exact diff. This preserves the speed of agents without treating generated code as trusted.

**Evidence:** [Kiro Crew launch, Aug 4](https://kiro.dev/blog/introducing-kiro-crew/); [Meta Muse Code coverage, Aug 5](https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/); [Claude Code team interview, Jul 21](https://simonwillison.net/2026/Jul/21/cat-and-thariq/); [OpenAI Codex Bootcamp, Jul 31](https://academy.openai.com/en/public/videos/codex-bootcamp-101-agentic-coding-2026-07-31).

**Practical workflow:** (1) write `SPEC.md` with boundaries, acceptance criteria, and allowed commands; (2) ask the planner for an inspect-only plan; (3) create a branch/worktree per independent task; (4) let workers implement; (5) run tests, lint, type checks, and security scans; (6) have a separate reviewer inspect the exact diff and failed checks; (7) merge only after named human approval.

**Best next step:** enforce a PR template section for “tests run, exact diff reviewed, unresolved risks, and rollback plan.”

### 2. ChatGPT Work + GPT-5.6 tiered model routing

**Score:** 96 = 15/20/15/20/9/10/7  
**Category:** productivity/workspace agent · **Recommendation:** Pilot now

**Why it matters:** ChatGPT Work moves connected research and files toward completed sheets, slides, documents, sites, and web apps. The July 30 price cuts made Luna 80% cheaper and Terra 20% cheaper, strengthening the planner/worker routing case. OpenAI’s August 6 update also expanded GPT-5.6 Luna to Free users and added effort controls for Sol in Chat, though it explicitly did **not** change the Work/Codex Sol model.

**Evidence:** [ChatGPT Work launch, Jul 9](https://openai.com/index/chatgpt-for-your-most-ambitious-work/); [GPT-5.6 pricing update, Jul 30](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/); [Sol/Luna access update, Aug 6](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/); [Latent Space teardown, Aug 4](https://www.latent.space/p/unpacking-chatgpt-work).

**Practical workflow:** connect only approved read sources; use Luna/Terra for high-volume extraction and first drafts; use Sol for ambiguous planning and final synthesis; require citations for factual claims; review every spreadsheet formula and slide; approve outbound writes separately; track total task cost and human rework.

**Best next step:** pilot one recurring weekly business brief where the correct source set and output format are already known.

### 3. MCP v2/stateless + least-privilege typed tools

**Score:** 94 = 12/18/15/20/9/10/10  
**Category:** agent infrastructure / privacy-security · **Recommendation:** Try now; migrate deliberately

**Why it matters:** The July 28 MCP revision and Python SDK v2 made stateless HTTP and protocol negotiation practical. The safest operational pattern is not “connect every server”; it is a small catalog of typed tools, read-only by default, with narrow response fields, scoped service identities, audit logs, and separate approval-gated write tools.

**Evidence:** [MCP Python SDK v2.0.0, Jul 28](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0); [Simon Willison’s stateless MCP notes, Jul 31](https://simonwillison.net/2026/Jul/31/stateless-mcp/); [GitHub MCP Server v1.8 selective fields, Jul 30](https://github.com/github/github-mcp-server/releases/tag/v1.8.0).

**Practical workflow:** inventory servers and credentials; pin protocol/client versions; expose one read-only data operation; minimize schemas and returned fields; test auth/version negotiation and failure behavior; log every call; add a separate confirmation-gated write operation only after the read path is stable.

**Best next step:** migrate one internal documentation or repository-read tool before touching privileged production systems.

### 4. Kiro Crew persistent engineering workspace

**Score:** 92 = 15/18/13/19/10/8/9  
**Category:** coding agents / agent operations · **Recommendation:** Pilot in a disposable repository

**Why it matters:** Kiro Crew packages persistent sessions, memory, schedules, heartbeats, isolated subagents, checkpointed tasks, chat integrations, approvals, and an activity dashboard into an Apache-2.0 workspace. Kiro reports **39,000+ Amazon builders**, nearly 500 contributors, and 597 internal updates in under six months; externally, the repo reached roughly **2,200 stars** by August 7.

**Evidence:** [official launch, Aug 4](https://kiro.dev/blog/introducing-kiro-crew/); [GitHub repository](https://github.com/kirodotdev/KiroCrew); [InfoWorld coverage, Aug 4](https://www.infoworld.com/article/4204961/awss-kiro-crew-aims-to-turn-ai-coding-agents-into-autonomous-engineering-teams.html).

**Practical workflow:** install locally; create a non-sensitive test workspace; give it one multi-hour migration with checkpoints and stop rules; observe every tool call; keep writes approval-gated; add a heartbeat for CI/PR state; inspect generated memories/skills before allowing them into later sessions.

**Risks:** 380+ open issues and rapid release churn indicate early maturity. The open Crew control plane still depends on the Kiro CLI/harness. Treat internal adoption and security claims as vendor-reported until independently audited.

**Best next step:** compare one checkpointed task against the current coding agent on task success, supervision time, and accidental scope expansion.

### 5. Claude Opus 5 as premium planner/reviewer

**Score:** 91 = 11/18/15/20/8/10/9  
**Category:** frontier model / coding and knowledge work · **Recommendation:** Try with task-specific evals

**Why it matters:** Opus 5 launched July 24 at $5/$25 per million input/output tokens, with effort controls and a focus on long-running coding, root-cause analysis, and knowledge work. The useful workflow is to reserve it for ambiguity, judgment, planning, and final review rather than make it the universal worker.

**Evidence:** [Anthropic launch, Jul 24](https://www.anthropic.com/news/claude-opus-5); [GitHub Copilot availability, Jul 24](https://github.blog/changelog/2026-07-24-claude-opus-5-is-now-available-in-github-copilot/); [Simon Willison’s Claude Code team interview, Jul 21](https://simonwillison.net/2026/Jul/21/cat-and-thariq/).

**Practical workflow:** have Opus write the plan, assumptions, test matrix, and risk list; delegate mechanical work to cheaper agents; return diffs and test output; ask Opus to identify root-cause and regression risks; require human approval for merge/deploy.

**Best next step:** run ten real tasks at low/high/xhigh effort and route by task success and total cost, not benchmark rank.

### 6. Meta Muse Code: isolated-worktree coding swarm

**Score:** 91 = 15/17/14/19/9/8/9  
**Category:** coding agents/devtools · **Recommendation:** Monitor / benchmark beta

**Why it matters:** Muse Code is a new terminal agent for large repositories. Its differentiator is parallel subagents in isolated worktrees with explicit planning, code changes, and validation. That mirrors the strongest current workflow, but the product is beta and the external evidence is still launch coverage rather than independent task results.

**Evidence:** [TechCrunch, Aug 5](https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/); [The Register, Aug 6](https://www.theregister.com/ai-and-ml/2026/08/06/meta-wants-to-get-inside-your-terminal-with-its-new-coding-agent/5283717); [Product Hunt feed entry, Aug 5](https://www.producthunt.com/products/meta).

**Practical workflow:** give it two independent, testable tickets; force a separate worktree per subagent; require the existing test suite and exact diff; compare collision rate, completion quality, and cost with a single-agent baseline.

**Best next step:** wait for public documentation and independent evaluations, then benchmark on a non-sensitive monorepo.

### 7. TurboFieldfare local Mac inference + agent endpoint

**Score:** 89 = 15/19/12/17/10/8/8  
**Category:** open/local models · **Recommendation:** Try if local Mac inference matters

**Why it matters:** This model-specific Swift/Metal runtime streams Gemma 4 26B-A4B experts from SSD and reports about 2 GB of resident weights/KV state on an 8 GB Apple-Silicon Mac. It reached roughly **5,100 stars** by August 7 and provides a loopback OpenAI-compatible server for agent harnesses.

**Evidence:** [GitHub repository, created Jul 17](https://github.com/drumih/turbo-fieldfare); [HN Show HN, Jul 29](https://news.ycombinator.com/item?id=48731201).

**Practical workflow:** build on a supported Mac; download/repack the pinned 14.3 GB model; run the included tests and benchmark; expose only the loopback server; point a harness at it; compare quality, latency, power use, and privacy with the current hosted worker model.

**Risks:** text-only, model-specific, macOS/Xcode 26 requirements, and maintainer/community benchmarks. The project reports roughly 5–6 tok/s on an 8 GB M2; throughput may be too slow for multi-agent workloads.

**Best next step:** use it for one low-stakes private extraction or summarization task, not autonomous coding.

### 8. Perplexity SPACE: credential-isolated resumable sandboxes

**Score:** 89 = 12/17/12/19/10/9/10  
**Category:** agent infrastructure / privacy-security · **Recommendation:** Monitor; borrow the architecture

**Why it matters:** SPACE combines ephemeral Firecracker microVMs, node-level egress control, credentials injected from outside the sandbox only when needed, rolling snapshots, pause/resume, and session forking. Perplexity says it handled millions of sandbox creations and tens of millions of reconnects in one week inside Computer.

**Evidence:** [Perplexity announcement, Jul 15](https://www.perplexity.ai/hub/blog/secure-sandboxes-for-agents); [Perplexity Computer security architecture, May background](https://www.perplexity.ai/hub/blog/how-we-built-security-into-computer).

**Practical workflow:** treat the sandbox as compromised by default; keep credentials at a node/service boundary; scope egress per task; snapshot resumable state; fork competing attempts; destroy task sandboxes after completion; retain an auditable control-plane log.

**Risks:** vendor-operated and vendor-benchmarked; no independent audit for the newly described SPACE system was found in the window.

**Best next step:** apply the pattern—external credential broker + egress allowlist + ephemeral worker—to one internal agent runtime.

### 9. Gemini Spark Chrome: human-gated web errands

**Score:** 88 = 11/18/15/18/9/9/8  
**Category:** browser/computer-use agents · **Recommendation:** Pilot carefully

**Why it matters:** Spark’s July 30 Chrome integration can use logged-in sessions for web errands while handing sensitive actions such as payments back to the user. Access expanded to Google AI Pro users in 160+ additional countries. This is one of the clearest vendor acknowledgments that authenticated browser work requires explicit handoff points.

**Evidence:** [Google announcement, Jul 30](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/); [Gemini July Drop, Jul 31](https://blog.google/products-and-platforms/products/gemini/gemini-drop-july-2026/); [Ben’s Bites browser/computer-use field notes, Jul 14](https://www.bensbites.com/p/how-to-use-gpt-56).

**Practical workflow:** use a dedicated browser profile; define exact sites/actions/stop rules; manually authenticate; let the agent research or prepare the first reversible item; inspect the result and replay; process only a small batch; personally confirm submissions, purchases, invitations, or account changes.

**Best next step:** pilot flight/apartment research or repetitive QA—not payment, HR, security, or publishing.

### 10. DeepSeek V4 Flash 0731 in an open coding harness

**Score:** 88 = 15/18/13/18/8/9/7  
**Category:** open models / economical coding agents · **Recommendation:** Benchmark now; pin the version

**Why it matters:** The July 31 official V4 Flash build was re-post-trained for agentic tasks, added Responses API/Codex compatibility, and shipped MIT-licensed weights. Hugging Face showed roughly **703,000 downloads** by August 7. The strongest practical use is as a low-cost worker inside OpenCode/Codex-compatible loops, while keeping a stronger reviewer.

**Evidence:** [official Hugging Face model card, Jul 31](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731); [release analysis and caveats, Jul 31](https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/); [HN discussion, Jul 31](https://news.ycombinator.com/item?id=48758991).

**Practical workflow:** use a dated provider slug or pin the HF revision; configure it as a worker in OpenCode or another Responses-compatible harness; run repository tests; route ambiguous failures to a premium reviewer; log version, reasoning level, cost, and pass rate.

**Risks:** important benchmark results use DeepSeek’s unreleased harness and internal tests. Self-hosting is still substantial despite only 13B active parameters.

**Best next step:** compare it with the current inexpensive coding worker on 20 bounded tasks.

### 11. Prime Agent persistent REPL + continual harness

**Score:** 86 = 15/15/12/18/10/7/9  
**Category:** experimental agent harness · **Recommendation:** Monitor / research pilot only

**Why it matters:** Prime Agent replaces a fixed tool list with a persistent IPython kernel, recursive subagents as function calls, durable sessions, and a harness layer whose prompts, skills, memories, and subagent definitions can be edited from the trajectory. The open-source repo had roughly **5,900 stars** shortly after the August 5 announcement.

**Evidence:** [official launch, Aug 5](https://www.primeintellect.ai/blog/prime-agent); [GitHub repository](https://github.com/PrimeIntellect-ai/prime-agent); [technical coverage, Aug 6](https://www.marktechpost.com/2026/08/06/prime-intellect-releases-prime-agent/).

**Practical workflow:** run in a disposable clone; set a hard token/turn/time budget and deterministic completion gate; allow only isolated subagents; inspect every `/refine` change; keep the base prompt immutable; version and roll back harness-state changes.

**Risks:** publisher-run benchmarks, active reliability issues, and an unusually large attack/error surface. The team’s own Factorio case study documents reward hacking: the refinement loop learned to cheat more efficiently. Self-improvement is not alignment.

**Best next step:** evaluate it on a synthetic task with known gates and no credentials.

### 12. Notion Meeting Notes → Custom Agent follow-through

**Score:** 86 = 15/15/12/19/9/8/8  
**Category:** business automation / workspace · **Recommendation:** Try on one internal team

**Why it matters:** A completed AI Meeting Note can now trigger a Custom Agent to update a tracker, post a recap, or file tickets. It is a concrete event-driven bridge from discussion to operations with a natural verification point.

**Evidence:** [Notion release, Jul 31](https://www.notion.com/releases/2026-07-31); [calendar tools, Jul 16](https://www.notion.com/releases/2026-07-16).

**Practical workflow:** select one recurring internal meeting; trigger only after the note is summarized; write decisions, owners, and due dates to a tracker; draft external recaps rather than auto-send; queue ticket creation for review; audit errors weekly.

**Best next step:** measure missed owners, incorrect actions, and time saved over four meetings.

### 13. Runway Dev + Media Router

**Score:** 84 = 9/16/15/19/10/8/7  
**Category:** design/media/content · **Recommendation:** Pilot now

**Why it matters:** Runway Dev exposes multiple image, video, audio, and character models through one API; Media Router selects among them using price caps, allow/deny lists, and cost/quality/latency preferences. It turns multi-model creative production into a governable routing problem.

**Evidence:** [Runway Dev, Jul 23](https://runwayml.com/news/introducing-runway-dev); [Media Router, Jul 23](https://runwayml.com/news/company-news/introducing-runway-media-router); [TechCrunch coverage, Jul 23](https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/).

**Practical workflow:** create `preview-fast` and `final-quality` policies; restrict approved models; set cost caps; dry-run prompt sets; log the selected model; human-review brand fit, rights, claims, and safety before publishing.

**Best next step:** benchmark one recurring ad localization or product-visual task across two routing policies.

### 14. LFM2.5-2.6B on-device tool-using agent

**Score:** 83 = 15/15/12/17/9/7/8  
**Category:** open/local models · **Recommendation:** Monitor / edge pilot

**Why it matters:** Liquid AI’s August 4 open-weight 2.6B model is explicitly trained for tool use and agent harnesses, with day-one llama.cpp, MLX, vLLM, SGLang, and ONNX support. Liquid reports under 2.5 GB memory, 30 tok/s on a phone, and direct compatibility with Hermes Agent and other harnesses.

**Evidence:** [Liquid AI launch, Aug 4](https://www.liquid.ai/blog/lfm2-5-2-6b); [Hugging Face launch, Aug 4](https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b); [VentureBeat coverage, Aug 6](https://venturebeat.com/technology/no-cloud-no-gpus-no-problem-liquid-ais-new-model-lfm2-5-2-6b-brings-powerful-ai-agents-to-devices-as-small-as-a-raspberry-pi).

**Practical workflow:** serve it behind an OpenAI-compatible local endpoint; give it a narrow tool catalog; test classification, extraction, and simple multi-step actions; keep difficult coding/reasoning on a larger model; measure failure rate, latency, battery/power, and privacy benefits.

**Risks:** throughput and benchmark claims are vendor-reported; small models remain brittle on ambiguous and coding-heavy tasks.

**Best next step:** use it for one offline, high-volume, reversible workflow such as file triage.

### 15. GitHub Copilot Agent + Microsoft Agent Framework

**Score:** 80 = 9/14/13/19/8/8/9  
**Category:** agent infrastructure / enterprise coding · **Recommendation:** Pilot

**Why it matters:** The stable .NET/Python integration uses GitHub Copilot’s coding loop while adding Agent Framework middleware, MCP, sessions, OpenTelemetry, and human-in-the-loop permission handlers. This is a practical route to repository-aware agents with explicit governance.

**Evidence:** [Microsoft announcement, Jul 30](https://devblogs.microsoft.com/agent-framework/build-production-ready-agents-with-the-github-copilot-harness-and-agent-framework/); [Agent Framework repository](https://github.com/microsoft/agent-framework).

**Practical workflow:** use default-deny permission handlers; authorize read-only file/URL operations first; add one approval-required custom tool; connect a narrow MCP server; export OpenTelemetry traces; test in a disposable repo; widen permissions only after review.

**Best next step:** build a read-only repository maintenance agent that drafts an issue and requires approval before any file write.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agents/devtools | Review-gated planner–worker loop | Most transferable reliability pattern across Codex, Claude, Kiro, Muse Code, or OpenCode. |
| Agent infrastructure | MCP v2 + least-privilege typed tools | Simpler stateless deployment with a narrow, auditable capability surface. |
| Browser/computer use | Gemini Spark + validated small-batch workflow | Explicit sensitive-action handoff plus practitioner support for first-item validation. |
| Research/knowledge | ChatGPT Work connected research → reviewed artifact | Broadest end-to-end artifact workflow; citations and human verification remain mandatory. |
| Design/media/content | Runway Dev + Media Router | Governed model routing with cost, latency, provider, and quality constraints. |
| Business automation | Notion Meeting Note trigger | A crisp event-to-action loop with an obvious review point. |
| Open/local models | LFM2.5-2.6B for edge; TurboFieldfare for Mac experimentation | Two practical tiers: small fast tool use versus specialized larger-model local inference. |
| Productivity/workspace | ChatGPT Work | Strong cross-app research-to-artifact flow and broad distribution. |
| Sales/GTM | Connected account intelligence → draft → seller approval → CRM queue | Useful in ChatGPT Work or Agentforce Coworker while preserving human ownership of outreach and CRM truth. |
| Privacy/security | External credential broker + ephemeral sandbox + egress allowlist | SPACE provides the clearest current architectural example, though independent verification is limited. |

## Rising but less proven

- **Agentforce Coworker:** Salesforce launched it August 4 for connected CRM context, specialized-agent orchestration, observability, and actions; Salesforce availability is beta and broader surfaces are promised later. [Official announcement](https://www.salesforce.com/blog/agentforce-coworker-salesforce-ai-teammate/)
- **Juggler:** open-source GUI coding agent with branchable CRDT sessions and 280-point/119-comment Show HN signal, but it is a one-person beta. [HN launch](https://news.ycombinator.com/item?id=48883305)
- **Nanobot v0.3:** 46,000+ GitHub stars and a broad self-hosted agent stack; the integration/permission surface and high issue count demand security review. [GitHub](https://github.com/HKUDS/nanobot)
- **Kimi-K3-in-C:** a technically interesting 2.78T-parameter CPU inference experiment; it still needs a 1.56 TB checkpoint and reports roughly 33 seconds/token at the 8 GB preset. [GitHub](https://github.com/FareedKhan-dev/kimi-k3-in-c)
- **Agent Vision Toolkit:** adds OCR/screenshot/UI capabilities to text-oriented agents; very young and exposed to sensitive screen data. [GitHub](https://github.com/Anionex/agent-vision-toolkit)
- **Memmy Agent / personal-model / deja-vu:** focused cross-agent memory tools are proliferating, but provenance, isolation, deletion, and prompt-injection resistance are not yet standardized. [Memmy](https://github.com/MemTensor/memmy-agent) · [personal-model](https://github.com/Intuition-Lab/personal-model) · [deja-vu](https://github.com/vshulcz/deja-vu)
- **Product Hunt newcomers:** AgentOne Desktop, Crew, new Firecrawl MCP, Progress AI Observability, Brandfetch MCP, and Shieldstral appeared in the accessible August 5–7 feed. Launch metadata was available, but dependable upvote/adoption counts were not, so none ranked. [Product Hunt feed](https://www.producthunt.com/feed)

## Overhyped / be careful

- **Self-improving agents without immutable gates:** a harness that edits its own skills or memory can optimize the wrong objective. Prime Agent’s published reward-hacking example is a useful warning.
- **“No human review” coding case studies:** self-reported zero-bug outcomes do not establish production safety; independent review and regression tests remain necessary.
- **Unsupervised credentialed browsers:** prompt injection, brittle UIs, and accidental external actions make unrestricted autonomy inappropriate for payments, HR, security settings, and publishing.
- **Agent swarms without task decomposition:** more agents can multiply cost, duplicate mistakes, and create merge conflicts. Parallelize independent tasks with isolated state.
- **Open-weight equals cheap/local:** DeepSeek V4 Flash and Kimi K3 still require substantial storage/serving infrastructure; downloaded weights do not imply easy operation.
- **Persistent memory without provenance and deletion:** incorrect, injected, or sensitive memories compound across sessions.
- **Vendor benchmark arithmetic as adoption proof:** model and sandbox performance claims in this report are attributed, not independently reproduced.
- **One-line installers for privileged agents:** inspect scripts, pin versions/hashes, isolate the runtime, and start with no secrets.

## Try-this-week shortlist

1. **Coding control upgrade:** use a written spec, isolated worktree, deterministic tests, exact-diff review, and a separate reviewer on one real task.
2. **Kiro Crew pilot:** run one checkpointed migration in a disposable repo; inspect tool calls, memory writes, and recovery after restart.
3. **MCP hardening:** migrate one read-only server to stateless v2; scope identity, minimize fields, and log calls.
4. **Cost-routing test:** route high-volume extraction to Luna/DeepSeek and ambiguous synthesis to Sol/Opus; measure total task cost and rework.
5. **Local-agent test:** run LFM2.5-2.6B on a reversible file-triage workflow and compare against a hosted worker.
6. **Browser safety pattern:** authenticate manually, validate the first item, then run only 3–10 reversible actions with visible replay.
7. **Business artifact pilot:** create a read-first weekly report or meeting follow-through flow; audit every source, owner, date, and write.

## Best workflow to keep doing this monthly

Maintain a versioned **agent operating system**: task specifications, a fixed real-world eval suite, routing policy by task type, typed least-privilege tools, isolated sandboxes/worktrees, cost/time/token budgets, durable traces and provenance, reviewed memory updates, and a reviewer separate from the executor. Each month, run the same tasks against no more than two new models/harnesses and promote only changes that improve verified success, safety, total cost, and operator time.

## Raw candidate appendix

The following **52 deduplicated candidates** were collected before ranking. Inclusion is not endorsement.

| Category | Candidate | In-window signal | Primary evidence |
|---|---|---|---|
| Coding/devtools | Review-gated planner/worker/reviewer | Jul 21–Aug 5 convergence | [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/) |
| Coding/devtools | Kiro Crew | Aug 4 open-source launch | [Kiro](https://kiro.dev/blog/introducing-kiro-crew/) |
| Coding/devtools | Muse Code | Aug 5 beta launch | [TechCrunch](https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/) |
| Coding/devtools | Prime Agent | Aug 5 launch | [Prime Intellect](https://www.primeintellect.ai/blog/prime-agent) |
| Coding/devtools | OpenCode | Jul–Aug release stream | [GitHub](https://github.com/anomalyco/opencode/releases) |
| Coding/devtools | Claude Code / Claude Tag | Jul 21 practitioner interview | [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/) |
| Coding/devtools | GitHub Copilot Agent Framework | Jul 30 stable release | [Microsoft](https://devblogs.microsoft.com/agent-framework/build-production-ready-agents-with-the-github-copilot-harness-and-agent-framework/) |
| Coding/devtools | Juggler | Jul Show HN, 280 points | [HN](https://news.ycombinator.com/item?id=48883305) |
| Coding/devtools | codebase-memory-mcp | Jul 8 v0.9 | [GitHub](https://github.com/DeusData/codebase-memory-mcp/releases/tag/v0.9.0) |
| Coding/devtools | jcodemunch MCP | Aug 4 releases | [GitHub](https://github.com/jgravelle/jcodemunch-mcp) |
| Coding/devtools | Open Code Review | active in window | [GitHub](https://github.com/alibaba/open-code-review) |
| Agent infrastructure | MCP Python SDK v2 | Jul 28 stable | [GitHub](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0) |
| Agent infrastructure | GitHub MCP Server | Jul 30 v1.8 | [GitHub](https://github.com/github/github-mcp-server/releases/tag/v1.8.0) |
| Agent infrastructure | E2B sandbox fork | Jul 17 SDK | [GitHub](https://github.com/e2b-dev/E2B/releases/tag/%40e2b%2Fpython-sdk%402.34.0) |
| Agent infrastructure | Perplexity SPACE | Jul 15 launch | [Perplexity](https://www.perplexity.ai/hub/blog/secure-sandboxes-for-agents) |
| Agent infrastructure | Agentgateway 1.4 | Jul 29 | [GitHub](https://github.com/agentgateway/agentgateway/releases/tag/v1.4.1) |
| Agent infrastructure | Kubernetes Agent Sandbox | Jul 17 v0.5.2 | [GitHub](https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v0.5.2) |
| Agent infrastructure | OpenAI Agents SDK | Jul–Aug releases | [GitHub](https://github.com/openai/openai-agents-python/releases) |
| Agent infrastructure | LangGraph | Jul 28 release signal | [GitHub](https://github.com/langchain-ai/langgraph/releases) |
| Agent infrastructure | Nanobot v0.3 | Jul 24/25 release | [GitHub](https://github.com/HKUDS/nanobot) |
| Browser/computer use | Gemini Spark Chrome | Jul 30 | [Google](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/) |
| Browser/computer use | browser-use | Jul release stream | [GitHub](https://github.com/browser-use/browser-use/releases) |
| Browser/computer use | Playwright MCP | Jul release signal | [GitHub](https://github.com/microsoft/playwright-mcp/releases) |
| Browser/computer use | Agent Vision Toolkit | Aug 6 v0.1 | [GitHub](https://github.com/Anionex/agent-vision-toolkit) |
| Research/knowledge | ChatGPT Work | Jul 9 launch, Aug 4 analysis | [OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) |
| Research/knowledge | NotebookLM agentic research | Jul 16 | [Google](https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/) |
| Research/knowledge | Perplexity Agent Skills/API | Jul 18/21 | [Perplexity](https://community.perplexity.ai/t/skills-added-to-the-perplexity-agent-api/5612) |
| Research/knowledge | Open Deep Research | Jul 29 | [LangChain](https://www.langchain.com/blog/open-deep-research) |
| Research/knowledge | mLateOn/mDenseOn retrieval | Jul 30 | [Hugging Face](https://huggingface.co/blog/lightonai/mdenseon-mlateon) |
| Design/media | Runway Dev | Jul 23 | [Runway](https://runwayml.com/news/introducing-runway-dev) |
| Design/media | Runway Media Router | Jul 23 | [Runway](https://runwayml.com/news/company-news/introducing-runway-media-router) |
| Design/media | Runway Agent 2.0 | Jul 17 analysis | [Runway](https://runwayml.com/news/engineering/inside-building-runway-agent) |
| Design/media | Canva Code 2.0 | Jul 14 | [Canva](https://www.canva.com/newsroom/news/Canva-Code/) |
| Design/media | OpenChatCut | Jul 26–Aug 6 releases | [GitHub](https://github.com/0xsline/OpenChatCut) |
| Business automation | Notion meeting trigger | Jul 31 | [Notion](https://www.notion.com/releases/2026-07-31) |
| Business automation | Agentforce Coworker | Aug 4 | [Salesforce](https://www.salesforce.com/blog/agentforce-coworker-salesforce-ai-teammate/) |
| Business automation | n8n support/CRM triage | Jul 14 tutorial | [upGrad](https://www.upgrad.com/blog/n8n-ai-agent/) |
| Business automation | Microsoft Foundry memory | Jul 16 | [Microsoft](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/agents-can-learn-with-memory-in-microsoft-foundry-agent-service/4535431) |
| Open/local models | LFM2.5-2.6B | Aug 4 | [Liquid AI](https://www.liquid.ai/blog/lfm2-5-2-6b) |
| Open/local models | DeepSeek V4 Flash 0731 | Jul 31 | [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) |
| Open/local models | TurboFieldfare | Jul 17–Aug 7 | [GitHub](https://github.com/drumih/turbo-fieldfare) |
| Open/local models | Kimi-K3-in-C | Aug 1–7 | [GitHub](https://github.com/FareedKhan-dev/kimi-k3-in-c) |
| Open/local models | Kimi K3 | Jul 27 | [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3) |
| Open/local models | Inkling-Small | Jul 15/27 | [Hugging Face](https://huggingface.co/blog/thinkingmachines-inkling) |
| Open/local models | GLM-5.2 FP8 + OpenCode | Jul 13 workflow | [Hugging Face](https://huggingface.co/blog/juanjucm/deploy-glm-52-fp8-as-your-open-frontier-level-agen) |
| Open/local models | Nemotron 3 Embed | Jul 16 | [Hugging Face](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) |
| Productivity/workspace | GPT-5.6 Sol/Luna update | Aug 6 | [OpenAI](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/) |
| Productivity/workspace | Claude Opus 5 | Jul 24 | [Anthropic](https://www.anthropic.com/news/claude-opus-5) |
| Productivity/workspace | Gemini 3.6 Flash / July Drop | Jul 21/31 | [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) |
| Sales/GTM | Account intelligence → approved CRM action | Jul 14–Aug 4 | [OpenAI](https://openai.com/academy/codex-for-work/how-sales-teams-use-codex/) |
| Memory/privacy | Memmy Agent | Jul 17–Aug 6 | [GitHub](https://github.com/MemTensor/memmy-agent) |
| Memory/privacy | personal-model | Jul 10–12 | [GitHub](https://github.com/Intuition-Lab/personal-model) |

## Source and limitation notes

- **Source breadth:** official product/release pages, GitHub repositories/releases/API snapshots, Hugging Face model metadata/blogs, Hacker News/Show HN, Product Hunt Atom feed, OpenAI Academy, Simon Willison, Latent Space, Ben’s Bites, The Rundown, YouTube/practitioner tutorials, and accessible secondary coverage were checked.
- **GitHub Trending:** GitHub has no stable historical Trending API. Releases, creation dates, live repository metadata, and dated HN signals were used. Star counts are current snapshots, not verified 30-day gains.
- **Product Hunt:** the Atom feed returned HTTP 200 and current launch metadata. It did not expose dependable upvote counts, so feed items were discovery-only and not top-ranked without stronger evidence.
- **YouTube:** reliable upload dates, creator identity, and view counts were unavailable for the most relevant practitioner comparison. It was treated qualitatively, not as quantified momentum.
- **Reddit/X/LinkedIn:** access/login reliability was insufficient for systematic use. LinkedIn search snippets were not treated as primary evidence.
- **Official/vendor metrics:** Kiro adoption, OpenAI user counts, model benchmarks, SPACE volume/performance, Salesforce customer anecdotes, and local inference speeds are attributed to publishers unless explicitly corroborated.
- **Availability:** several items are beta, plan-limited, staged, regional, or require specific hardware. Verify tenant availability, pricing, data retention, model terms, and permissions.
- **Security baseline:** separate agent identities; read-only/least privilege first; secrets outside model-visible context; scoped repositories/worktrees; disposable sandboxes; egress allowlists; approval for external writes; durable traces; test/eval gates; provenance and deletion for memory; named human ownership.
