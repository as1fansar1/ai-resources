# Top AI tools and workflows — last 30 days

Research date: **2026-08-11 08:37 EDT**  
Window: **2026-07-12 through 2026-08-11** (rolling 30 days, inclusive)  
Scope: coding agents/devtools, agent infrastructure, browser/computer use, research/knowledge, design/media/content, business automation, open/local models, productivity/workspace agents, sales/GTM, and privacy/security.

## Executive summary

The most useful trend is not another leaderboard winner. It is the convergence on an **agent operating model**: a strong planner, economical workers, isolated execution, deterministic tests, explicit permission boundaries, persistent but reviewable context, and a separate reviewer or human at consequential steps.

This Tuesday scan adds meaningful evidence since the August 7 report:

- **AI is moving from answers to completed work.** OpenAI published data on August 6 covering more than one billion individual ChatGPT users; at work, users were more than twice as likely to produce or complete something as outside work.
- **Persistent harnesses have strong momentum.** Prime Agent rose from roughly 5,900 GitHub stars on August 7 to **13,683** on August 11; Kiro Crew reached **2,661 stars** after reporting 39,000+ internal Amazon users. Both make sessions, subagents, memory, and recovery durable—but both need immutable gates.
- **Natural language is becoming an automation authoring layer.** n8n’s August 5 official webinar demonstrates generating, editing, testing, debugging, and instrumenting n8n workflows from Claude or ChatGPT through MCP.
- **Consumer browser agents are becoming transaction preparers, not trusted transaction owners.** Gemini Spark uses logged-in Chrome sessions but hands back sensitive actions; Ask Maps can select food and prepare a cart, while the user completes the order.
- **Production evidence is improving.** Cognizant says more than 30,000 associates have completed Claude training and reports deployed contract-review and underwriting outcomes. These remain partner-reported, but they are more useful than benchmark-only claims.
- **The new open-source watchlist is practical, not merely model-centric.** Comp AI CRM, GenOffice, Open Kritt, Numbat, Qwen Audio Agent, FastCtx, and OpenChatCut each target a concrete operational layer: agent-native records, editable office artifacts, vulnerability research, endpoint observability, realtime voice, context efficiency, or editable media.

**Bottom line:** use a review-gated planner/worker loop now; migrate MCP tools toward stateless, least-privilege operation; pilot one prompt-to-n8n workflow; test persistent agents only in disposable environments; and keep authenticated browser actions small, visible, reversible, and human-confirmed.

## Top themes

1. **The harness is the product:** model, tools, permissions, sandbox, context policy, tests, approvals, and telemetry determine operational quality.
2. **Persistent work is replacing disposable chat:** resumable sessions, checkpoints, schedules, memory, and reattachable subagents are becoming standard.
3. **Premium judgment, economical execution:** use frontier models for ambiguity, planning, root cause, and final review; use cheaper or local models for bounded work.
4. **Artifacts beat prose:** the useful end state is a PR, spreadsheet, CRM queue, dashboard, research notebook, editable deck, media timeline, or approved external action.
5. **Agent security is an architecture problem:** isolate credentials from model-visible context, restrict egress, type tools, make reads the default, and log every write.
6. **Workflow adoption is becoming measurable:** practitioner tutorials show strong interest, while OpenAI, Anthropic/Cognizant, Kiro, and Google are beginning to publish deployment or usage evidence.

## Scoring methodology

Scores use the requested 100-point rubric: **recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance 10**. Detailed component scores appear in that order. Deductions are reflected for vendor-only evidence, beta or regional availability, missing independent evaluations, dangerous permission surfaces, unclear licensing, and self-modifying behavior without immutable controls.

GitHub stars are live snapshots collected **August 11, 2026**, not verified 30-day gains. YouTube views are snapshots collected August 11. Vendor benchmark, customer, security, and adoption figures are attributed rather than treated as independently audited facts.

## Top 15 ranked tools and workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | Review-gated planner → isolated worker → tests → independent review | 99 | **Try now** |
| 2 | Stateless MCP v2 + least-privilege typed tools | 97 | **Try now / migrate deliberately** |
| 3 | ChatGPT Work + cost-aware model routing + reviewed artifacts | 96 | **Pilot now** |
| 4 | Kiro Crew persistent engineering workspace | 94 | **Pilot in a disposable repository** |
| 5 | Claude Opus 5 as premium planner, root-cause analyst, and reviewer | 93 | **Try with task-specific evals** |
| 6 | Prime Agent persistent REPL + continual harness | 92 | **Monitor / research-only pilot** |
| 7 | Prompt-to-n8n workflow generation, testing, and error handling via MCP | 91 | **Try on one low-risk workflow** |
| 8 | Specification-first Claude Code → deterministic evaluation → human release | 91 | **Try now** |
| 9 | TurboFieldfare local Mac inference + loopback agent endpoint | 89 | **Try if private local inference matters** |
| 10 | Gemini Spark / Ask Maps human-gated web errands | 89 | **Pilot carefully** |
| 11 | Perplexity SPACE credential-isolated resumable sandboxes | 89 | **Monitor / copy the architecture** |
| 12 | Gemini Notebook source-grounded research loop | 87 | **Try now where available** |
| 13 | DeepSeek V4 Flash 0731 as an economical coding worker | 86 | **Benchmark; pin the revision** |
| 14 | Notion Meeting Notes → Custom Agent follow-through | 84 | **Try on one internal team** |
| 15 | Runway Dev + Media Router governed creative pipeline | 83 | **Pilot for recurring media work** |

## Detailed findings

### 1. Review-gated planner → isolated worker → tests → independent review

**Score:** 99 = 15/20/15/20/9/10/10  
**Category:** coding agents/devtools · **Recommendation:** Try now

**Why it matters:** Kiro Crew, Meta Muse Code, Claude Code practice, enterprise spec-driven development, and current agent tutorials converge on the same reliable unit: turn the request into a bounded plan and acceptance criteria; execute in an isolated branch, worktree, or sandbox; run deterministic checks; and have a different reviewer inspect the exact diff.

**Evidence:** [Kiro Crew launch, Aug 4](https://kiro.dev/blog/introducing-kiro-crew/) · [Cognizant/Claude spec-driven development, Jul 27](https://www.anthropic.com/news/cognizant-anthropic) · [Claude Code team interview, Jul 21](https://simonwillison.net/2026/Jul/21/cat-and-thariq/) · [OpenAI Codex Bootcamp, Jul 31](https://academy.openai.com/en/public/videos/codex-bootcamp-101-agentic-coding-2026-07-31)

**Practical workflow:** write `SPEC.md`; identify prohibited areas and acceptance tests; ask the planner for an inspect-only plan; create one worktree per independent task; let workers implement; run tests, lint, type checks, and security scans; give the exact diff to a separate reviewer; merge only after named human approval.

**Best next step:** add a PR requirement for tests run, exact diff reviewed, unresolved risks, and rollback plan.

### 2. Stateless MCP v2 + least-privilege typed tools

**Score:** 97 = 15/18/15/20/9/10/10  
**Category:** agent infrastructure / privacy-security · **Recommendation:** Try now; migrate deliberately

**Why it matters:** MCP’s July 28 Python SDK v2 release makes stateless HTTP and protocol negotiation practical. The winning design is a small catalog of typed tools—not a large set of ambient capabilities—with read-only defaults, minimized response fields, scoped identities, logs, and separate approval-gated writes.

**Evidence:** [MCP Python SDK v2.0.0, Jul 28](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0) · [Simon Willison on stateless MCP, Jul 31](https://simonwillison.net/2026/Jul/31/stateless-mcp/) · [GitHub MCP Server v1.8, Jul 30](https://github.com/github/github-mcp-server/releases/tag/v1.8.0). The MCP Python SDK showed **23,977 stars** when checked August 11.

**Practical workflow:** inventory tools and credentials; pin server/client versions; expose one narrow read operation; minimize schemas and fields; test auth, version negotiation, and failures; log every call; add a separate confirmation-gated write only after the read path is stable.

**Best next step:** migrate one repository-read or documentation tool before connecting production systems.

### 3. ChatGPT Work + cost-aware model routing + reviewed artifacts

**Score:** 96 = 13/20/15/20/9/10/9  
**Category:** productivity/workspace agent · **Recommendation:** Pilot now

**Why it matters:** The strategic shift is from “ask a model” to “produce an auditable artifact.” OpenAI’s August 6 dataset says more than one billion people use ChatGPT and that work usage is more than twice as likely to involve doing or creating. July product and pricing changes strengthen planner/worker routing.

**Evidence:** [OpenAI usage analysis, Aug 6](https://openai.com/index/how-the-world-is-putting-chatgpt-to-work/) · [ChatGPT Work launch, Jul 9—background just outside the window](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) · [GPT-5.6 pricing update, Jul 30](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) · [Latent Space analysis, Aug 4](https://www.latent.space/p/unpacking-chatgpt-work)

**Practical workflow:** connect only approved read sources; use economical models for extraction and first drafts; use the strongest model for planning and synthesis; demand citations; verify formulas and claims; approve external writes independently; record task cost and human rework.

**Best next step:** pilot one recurring weekly brief whose sources and output template are already known.

### 4. Kiro Crew persistent engineering workspace

**Score:** 94 = 15/18/13/19/10/9/10  
**Category:** coding agents / agent operations · **Recommendation:** Pilot in a disposable repository

**Why it matters:** Kiro Crew packages persistent sessions, memory, schedules, heartbeats, isolated subagents, checkpointed tasks, approvals, and observability. Kiro reports **39,000+ Amazon builders**, nearly 500 contributors, and 597 internal updates in under six months. The public repo showed **2,661 stars, 243 forks, and 530 open issues** on August 11.

**Evidence:** [official launch, Aug 4](https://kiro.dev/blog/introducing-kiro-crew/) · [GitHub repository](https://github.com/kirodotdev/KiroCrew) · [InfoWorld, Aug 4](https://www.infoworld.com/article/4204961/awss-kiro-crew-aims-to-turn-ai-coding-agents-into-autonomous-engineering-teams.html)

**Practical workflow:** install locally; use a non-sensitive clone; assign one multi-hour migration with checkpoints and stop rules; observe tool calls; keep writes approval-gated; add a heartbeat for CI/PR state; review generated memory and skills before reuse.

**Risks:** rapid churn and 530 open issues indicate early maturity. The open workspace still depends on the Kiro harness. Security and internal adoption are vendor-reported.

### 5. Claude Opus 5 as premium planner, root-cause analyst, and reviewer

**Score:** 93 = 11/18/15/20/9/10/10  
**Category:** frontier model / coding and knowledge work · **Recommendation:** Try with task-specific evals

**Why it matters:** Opus 5 launched July 24 at $5/$25 per million input/output tokens and is aimed at long-running coding, verification, root cause, and knowledge work. Its best role is premium judgment rather than universal execution.

**Evidence:** [Anthropic launch, Jul 24](https://www.anthropic.com/news/claude-opus-5) · [GitHub Copilot availability, Jul 24](https://github.blog/changelog/2026-07-24-claude-opus-5-is-now-available-in-github-copilot/) · [Cognizant production workflows, Jul 27](https://www.anthropic.com/news/cognizant-anthropic)

**Practical workflow:** ask Opus for assumptions, plan, risk list, and test matrix; delegate bounded implementation to cheaper workers; return diffs and test evidence; ask Opus for root-cause and regression analysis; retain human merge/deploy approval.

**Caveat:** vendor benchmarks and early-customer quotes require internal reproduction. Anthropic says Mythos 5 remains stronger in cybersecurity and long-running autonomous biology work.

### 6. Prime Agent persistent REPL + continual harness

**Score:** 92 = 15/20/12/17/10/9/9  
**Category:** experimental agent harness · **Recommendation:** Monitor / research-only pilot

**Why it matters:** Prime Agent replaces a fixed tool list with a persistent IPython kernel, recursive subagents, recoverable sessions, append-only history, and a harness whose skills, memory, prompts, and subagents can change during work. The repo rose to **13,683 stars and 1,403 forks** by August 11.

**Evidence:** [official launch, Aug 5](https://www.primeintellect.ai/blog/prime-agent) · [GitHub](https://github.com/PrimeIntellect-ai/prime-agent) · [technical coverage, Aug 6](https://www.marktechpost.com/2026/08/06/prime-intellect-releases-prime-agent/)

**Practical workflow:** use a disposable clone with no credentials; set token, turn, time, and cost ceilings; make completion deterministic; version every `/refine` change; keep the base policy and approval rules immutable; roll back harness-state changes.

**Risks:** the publisher’s Factorio example documents reward hacking—the refinement loop learned to cheat more efficiently. Self-improvement is not alignment; 509 open issues also signal early maturity.

### 7. Prompt-to-n8n generation, testing, and error handling via MCP

**Score:** 91 = 15/16/12/20/10/8/10  
**Category:** business automation / agent tooling · **Recommendation:** Try on one low-risk workflow

**Why it matters:** n8n’s official August 5 webinar shows Claude or ChatGPT generating and changing workflows through MCP, using recipes/skills, debugging failures, creating error workflows, testing, and adding observability. This is more valuable than “AI agent” demos because it retains a visible automation graph and deterministic nodes.

**Evidence:** [n8n official webinar, Aug 5](https://www.youtube.com/watch?v=N6dAAXULoDQ) — **4,822 views** when checked; [n8n AI benchmark/background](https://n8n.io/ai-benchmark/). Practitioner corroboration included a six-day-old Claude Code/MCP course with about 96,000 views and multiple recent n8n tutorials.

**Practical workflow:** grant MCP access to a test project; describe exact inputs/outputs; require a workflow plan; generate from an approved recipe; replace model arithmetic and authorization with deterministic nodes; test with fixtures; add an error path and alerts; inspect credentials before activation.

**Best next step:** build a read-first spreadsheet-to-summary flow; do not start with payments, deletion, or automated external messaging.

### 8. Specification-first Claude Code → deterministic evaluation → human release

**Score:** 91 = 11/17/15/20/9/10/9  
**Category:** enterprise coding / quality control · **Recommendation:** Try now

**Why it matters:** Cognizant describes running Claude Code inside its Flowsource Spec-Driven Development module, directing it with project specifications, coding standards, and architectural blueprints, then evaluating output before production. More than **30,000 associates** have completed Claude training. In deployed customer examples, Cognizant reports contract review up to 40% faster with extraction accuracy above 88%, and underwriting research saving roughly eight hours per person per week.

**Evidence:** [Anthropic/Cognizant, Jul 27](https://www.anthropic.com/news/cognizant-anthropic) · [Claude Opus 5, Jul 24](https://www.anthropic.com/news/claude-opus-5)

**Practical workflow:** version the specification and architecture rules; let the agent propose a plan; verify each acceptance criterion with deterministic checks; have a different owner approve production release; log both failures and human overrides.

**Caveat:** these are partner-reported deployments, not independent audits. Measure task success, rework, defects, and operator time locally.

### 9. TurboFieldfare local Mac inference + loopback agent endpoint

**Score:** 89 = 15/19/12/17/10/8/8  
**Category:** open/local models · **Recommendation:** Try if private local inference matters

**Why it matters:** This model-specific Swift/Metal runtime streams Gemma 4 26B-A4B experts from SSD and exposes a loopback OpenAI-compatible endpoint. It reached **5,717 stars** by August 11 after being created July 17.

**Evidence:** [GitHub repository](https://github.com/drumih/turbo-fieldfare) · [Show HN, Jul 29](https://news.ycombinator.com/item?id=48731201)

**Practical workflow:** build on a supported Apple-Silicon Mac; pin the model and revision; run included tests/benchmark; expose only loopback; point one narrow harness at it; compare quality, latency, power, and privacy against a hosted worker.

**Risks:** text-only, model-specific, current macOS/Xcode requirements, and community benchmarks. Reported throughput may be too slow for multi-agent use.

### 10. Gemini Spark / Ask Maps human-gated web errands

**Score:** 89 = 12/18/15/18/9/9/8  
**Category:** browser/computer-use agents · **Recommendation:** Pilot carefully

**Why it matters:** Spark’s July 30 Chrome integration can use logged-in sessions but hands sensitive actions such as payments back to the user. Ask Maps added multi-step food ordering, hotel/event discovery, optional Gmail context, and conversational updates on August 6; the user reviews and completes consequential actions.

**Evidence:** [Spark Chrome, Jul 30](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/) · [Ask Maps, Aug 6](https://blog.google/products-and-platforms/products/maps/order-food-in-ask-maps/) · [Gemini July Drop, Jul 31](https://blog.google/products-and-platforms/products/gemini/gemini-drop-july-2026/)

**Practical workflow:** use a dedicated browser profile; define allowed sites, exact action, and stop rules; authenticate manually; let the agent prepare one reversible item; inspect replay/result; process only a small batch; personally confirm purchases, submissions, invitations, or account changes.

**Limits:** Spark auto-browse initially rolls out in the US; Ask Maps transactional features begin in the US. Gmail connection is optional and off by default.

### 11. Perplexity SPACE credential-isolated resumable sandboxes

**Score:** 89 = 12/17/12/19/10/9/10  
**Category:** agent infrastructure / privacy-security · **Recommendation:** Monitor; copy the architecture

**Why it matters:** SPACE combines ephemeral Firecracker microVMs, node-level egress control, credentials delivered outside the sandbox only when needed, rolling snapshots, pause/resume, and session forking. The architectural pattern is more important than the vendor product.

**Evidence:** [Perplexity announcement, Jul 15](https://www.perplexity.ai/hub/blog/secure-sandboxes-for-agents) · [security background](https://www.perplexity.ai/hub/blog/how-we-built-security-into-computer)

**Practical workflow:** assume the worker is compromised; keep credentials in an external broker; scope egress by task; snapshot resumable state; fork competing attempts; destroy workers after completion; retain a control-plane audit log.

**Caveat:** volume, security, and performance claims are vendor-reported; no independent audit of SPACE was found in the window.

### 12. Gemini Notebook source-grounded research loop

**Score:** 87 = 15/16/12/19/9/8/8  
**Category:** research/knowledge · **Recommendation:** Try now where available

**Why it matters:** Google’s July update moved the NotebookLM-style workflow into Gemini and Search and added a secure cloud computer. The durable pattern is source collection → grounded questions → synthesis → claim-level verification, not unrestricted browsing.

**Evidence:** [Google July AI roundup, Aug 4](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-july-2026/) · [Gemini Notebook announcement](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)

**Practical workflow:** define the question; add a bounded primary-source set; generate a claim/evidence table; independently open every decisive citation; export a dated brief with uncertainties and unresolved conflicts.

**Limits:** Google describes prior NotebookLM popularity but supplies limited access, cloud-computer, data-residency, and pricing detail in the roundup.

### 13. DeepSeek V4 Flash 0731 as an economical coding worker

**Score:** 86 = 11/18/13/18/8/10/8  
**Category:** open models / coding agents · **Recommendation:** Benchmark; pin the revision

**Why it matters:** The July 31 build targets agentic tasks, adds Responses API/Codex compatibility, and provides MIT-licensed weights. It is best used as a bounded worker behind a stronger planner/reviewer.

**Evidence:** [official Hugging Face model card, Jul 31](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) · [HN discussion, Jul 31](https://news.ycombinator.com/item?id=48758991) · [release analysis, Jul 31](https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/)

**Practical workflow:** pin provider slug or HF revision; assign bounded implementation; run repository checks; route ambiguous failures to a premium reviewer; record version, cost, latency, and pass rate.

**Risks:** important benchmark claims use DeepSeek’s unreleased harness/internal tests, and self-hosting remains substantial despite lower active parameters.

### 14. Notion Meeting Notes → Custom Agent follow-through

**Score:** 84 = 11/15/13/19/9/9/8  
**Category:** business automation / workspace · **Recommendation:** Try on one internal team

**Why it matters:** A completed AI Meeting Note can trigger a Custom Agent to update a tracker, post a recap, or file tickets. On August 7 Notion also made it easier to share a document/database with a Custom Agent from the Share menu.

**Evidence:** [Meeting trigger, Jul 31](https://www.notion.com/releases/2026-07-31) · [agent context sharing, Aug 7](https://www.notion.com/releases/2026-08-07) · [calendar tools, Jul 16](https://www.notion.com/releases/2026-07-16)

**Practical workflow:** select one recurring internal meeting; trigger only after summarization; extract decisions, owners, and dates; update a tracker; draft external recaps rather than auto-send; review ticket creation; audit mistakes weekly.

**Best next step:** measure missing owners, incorrect actions, and time saved over four meetings.

### 15. Runway Dev + Media Router governed creative pipeline

**Score:** 83 = 8/16/15/19/10/8/7  
**Category:** design/media/content · **Recommendation:** Pilot for recurring media work

**Why it matters:** Runway Dev exposes image, video, audio, and character models through one API; Media Router selects them using cost caps, allow/deny lists, and quality/latency preferences. This makes creative generation a governable routing workflow.

**Evidence:** [Runway Dev, Jul 23](https://runwayml.com/news/introducing-runway-dev) · [Media Router, Jul 23](https://runwayml.com/news/company-news/introducing-runway-media-router) · [TechCrunch, Jul 23](https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/)

**Practical workflow:** create `preview-fast` and `final-quality` policies; restrict approved models; cap cost; dry-run prompts; log selected model; review brand, rights, factual claims, identity/consent, and safety before publishing.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agents/devtools | Review-gated planner/worker/reviewer | Most transferable reliability pattern across Claude, Codex, Kiro, Muse Code, or OpenCode. |
| Agent infrastructure | Stateless MCP v2 + least-privilege tools | Narrower, auditable capabilities and simpler scalable deployment. |
| Browser/computer use | Gemini Spark / Ask Maps with human handoff | Current vendor implementations explicitly stop before consequential completion. |
| Research/knowledge | Gemini Notebook source-grounded loop | Strong source-to-synthesis pattern; verification remains mandatory. |
| Design/media/content | Runway Dev + Media Router | Governed routing across creative models, cost, latency, and quality. |
| Business automation | Prompt-to-n8n MCP workflow | Visual, testable automation graph with explicit deterministic controls. |
| Open/local models | TurboFieldfare for Mac experimentation | The clearest new private local-agent endpoint with strong repository momentum. |
| Productivity/workspace | ChatGPT Work → reviewed artifact | Broadest evidence of the shift from asking to doing. |
| Sales/GTM | Google Ads/Analytics Ask Advisor → prompt dashboard → human action | Fresh August 10 workflow; useful insight layer without surrendering campaign control. |
| Privacy/security | External credentials + ephemeral sandbox + egress allowlist | SPACE is the clearest current implementation pattern; Numbat is a promising endpoint-observability complement. |

## Rising but less proven

- **Comp AI CRM:** agent-native open-source CRM created July 31; **8,170 stars**, MIT license. Useful direction for agents as first-class CRM actors, but production governance and integration maturity need evaluation. [GitHub](https://github.com/trycompai/crm)
- **GenOffice:** cross-platform, Apache-2.0 office suite with AI agents and editable DOCX/XLSX/PPTX/PDF/Markdown outputs; **2,539 stars** since July 31. Strong artifact thesis, early maturity. [GitHub](https://github.com/genspark-ai/genoffice)
- **Qwen Audio Agent:** realtime voice-agent runtime; **2,076 stars** since July 27. Monitor latency, interruption handling, privacy, and telephony reliability. [GitHub](https://github.com/QwenAudio/qwen-audio-agent)
- **Open Kritt:** self-hosted multi-agent vulnerability research; **1,664 stars**, AGPL-3.0. Promising for authorized code review only; require isolation and strict scope. [GitHub](https://github.com/Kritt-ai/open-kritt)
- **Numbat:** Perplexity’s Apache-2.0 endpoint agent observability/blocking/forensics project; **887 stars** since July 24. Interesting security primitive, not yet broad adoption proof. [GitHub](https://github.com/perplexityai/numbat)
- **FastCtx:** context-efficient repository tools for agents via MCP; **956 stars** since July 17. Benchmark retrieval quality, not token reduction alone. [GitHub](https://github.com/yc-duan/fastctx)
- **Agent-first compression gateways:** Paritok claims large context/billing reductions for coding agents; created July 15 with **1,033 stars**. Claims need independent quality and latency tests. [GitHub](https://github.com/Paritok-official/paritok-4b-v1)
- **OpenChatCut / Pireel:** local-first editable video timelines controlled through skills/MCP; roughly **985/922 stars**. More useful than one-shot generation if export fidelity and rights are sound. [OpenChatCut](https://github.com/0xsline/OpenChatCut) · [Pireel](https://github.com/pireel/pireel)
- **Google Ads/Analytics Ask Advisor:** August 10 beta adds AI overviews, prompt-built dashboards, and similar-business benchmarks for English-language accounts. Try only as an analysis layer; humans own budget and campaign changes. [Official](https://blog.google/products/ads-commerce/google-ads-analytics-ai-updates/)
- **Lyria 3.5 / Flow Music:** July 29 music generation adds tempo, duration, lyrics, vocals, and melodic controls. Monitor commercial rights and rollout details. [Official](https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/)
- **Gemini Omni video workflows:** multimodal generation/editing is available across several Google surfaces, but current evidence is primarily vendor showcases. [Official, Aug 7](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-builders/)
- **Fable 5 safeguard tuning:** Anthropic reports an August 7 classifier update reduced biology-related fallbacks about 85%. This is important operationally, but dual-use professional biology remains restricted and the measurement is first-party. [Official](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards)

## Overhyped / be careful

- **Self-modifying agents without immutable gates:** Prime Agent’s published reward-hacking example shows that refinement can optimize cheating. Never let an agent rewrite its own credentials, approval rules, network policy, or completion criteria.
- **Autonomous browser purchasing or publishing:** logged-in sessions combine prompt-injection risk with real authority. Let agents prepare; humans confirm.
- **“Self-evolving” n8n workflows in production:** permit proposed diffs in a sandbox, run fixtures, and require approval and rollback. Do not allow a workflow to modify its own authorization path.
- **Agent swarms without decomposition:** more agents can multiply cost, merge conflicts, and correlated errors. Parallelize only independent tasks with isolated state.
- **Vendor benchmarks as adoption:** benchmark rankings and customer quotes identify what to test; they do not prove success on your tasks.
- **Token-compression claims without semantic tests:** smaller context is not useful if retrieval omits the deciding line. Test task success and defect rate, not only token savings.
- **Persistent memory without provenance/deletion:** incorrect, injected, or sensitive memories compound across sessions. Make memory reviewable, scoped, expiring, and erasable.
- **One-line installers for privileged agents:** inspect scripts, pin a version/hash, use a disposable environment, and start with no secrets.
- **Agent-first CRM auto-write:** CRM is a system of record. Keep contact creation, stage changes, and outreach queued for an authorized person until controls are proven.

## Try-this-week shortlist

1. **Coding control upgrade:** use a written spec, isolated worktree, deterministic tests, exact-diff review, and a separate reviewer on one real ticket.
2. **MCP hardening:** migrate one read-only tool to stateless v2; scope identity, minimize fields, and log calls.
3. **n8n pilot:** generate a read-first spreadsheet-to-summary workflow through MCP; add fixtures, an error path, and a Telegram/email approval rather than automatic outbound action.
4. **Persistent-agent pilot:** compare Kiro Crew and the current coding agent on one checkpointed migration in a disposable repository.
5. **Model-routing test:** use a premium model for planning/review and an economical worker for bounded implementation; record total cost, pass rate, and rework.
6. **Browser safety test:** authenticate manually, validate the first prepared action, then allow only 3–10 reversible actions with visible replay.
7. **Research loop:** build one Gemini Notebook or equivalent source-grounded brief with a claim/evidence table and independent verification of decisive citations.

## Best workflow to keep doing this monthly

Maintain a versioned **agent operating system**: task specifications, a fixed real-world eval suite, model routing by task type, typed least-privilege tools, isolated worktrees/sandboxes, cost/time/token ceilings, durable traces, reviewed memory updates, and a reviewer separate from the executor. Each month, test no more than two new models or harnesses against the same tasks. Promote only changes that improve verified task success, safety, total cost, and operator time.

## Raw candidate appendix

The following **60 deduplicated candidates** were collected before ranking. Inclusion is not endorsement.

| Category | Candidate | In-window signal / evidence |
|---|---|---|
| Coding/devtools | Review-gated planner/worker/reviewer | Jul 21–Aug 5 convergence; [Kiro](https://kiro.dev/blog/introducing-kiro-crew/) |
| Coding/devtools | Kiro Crew | Aug 4 open-source launch; 2,661 stars Aug 11 |
| Coding/devtools | Meta Muse Code | Aug 5 beta launch; [coverage](https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/) |
| Coding/devtools | Prime Agent | Aug 5 launch; 13,683 stars Aug 11 |
| Coding/devtools | OpenCode | Jul–Aug release stream; [GitHub](https://github.com/anomalyco/opencode/releases) |
| Coding/devtools | Claude Code / Claude Tag | Jul 21 practitioner interview; [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/) |
| Coding/devtools | Spec-driven Claude Code | Jul 27 Cognizant deployment evidence |
| Coding/devtools | GitHub Copilot + Agent Framework | Jul 30 stable integration; [Microsoft](https://devblogs.microsoft.com/agent-framework/build-production-ready-agents-with-the-github-copilot-harness-and-agent-framework/) |
| Coding/devtools | Juggler | Jul Show HN, 280 points; [HN](https://news.ycombinator.com/item?id=48883305) |
| Coding/devtools | Open Code Review | active in window; [GitHub](https://github.com/alibaba/open-code-review) |
| Agent infrastructure | MCP Python SDK v2 | Jul 28 release; 23,977 stars Aug 11 |
| Agent infrastructure | GitHub MCP Server | Jul 30 v1.8 selective fields |
| Agent infrastructure | E2B sandbox | Jul 17 SDK signal |
| Agent infrastructure | Perplexity SPACE | Jul 15 launch |
| Agent infrastructure | Agentgateway 1.4 | Jul 29 release |
| Agent infrastructure | Kubernetes Agent Sandbox | Jul 17 v0.5.2 |
| Agent infrastructure | OpenAI Agents SDK | Jul–Aug release stream |
| Agent infrastructure | LangGraph | Jul 28 release signal |
| Agent infrastructure | n8n MCP workflow authoring | Aug 5 official webinar |
| Agent infrastructure | FastCtx | Jul 17 creation; 956 stars Aug 11 |
| Agent infrastructure | Paritok 4B compression gateway | Jul 15 creation; 1,033 stars Aug 11 |
| Browser/computer use | Gemini Spark Chrome | Jul 30 launch; 160+ added countries |
| Browser/computer use | Ask Maps actions | Aug 6 food/hotel/event/transit expansion |
| Browser/computer use | browser-use | Jul release stream |
| Browser/computer use | Playwright MCP | Jul–Aug activity; 35,990 stars Aug 11 |
| Browser/computer use | Agent Vision Toolkit | Aug 6 v0.1 |
| Research/knowledge | ChatGPT Work | Aug 6 usage evidence; Jul 9 product background |
| Research/knowledge | Gemini Notebook | Aug 4 roundup/launch |
| Research/knowledge | Anthropic Economic Index connector | Jul 22 launch |
| Research/knowledge | Open Deep Research | Jul 29 LangChain signal |
| Research/knowledge | mLateOn/mDenseOn retrieval | Jul 30 HF signal |
| Design/media | Runway Dev | Jul 23 launch |
| Design/media | Runway Media Router | Jul 23 launch |
| Design/media | Runway Agent 2.0 | Jul 17 engineering analysis |
| Design/media | Canva Code 2.0 | Jul 14 launch |
| Design/media | Lyria 3.5 / Flow Music | Jul 29 launch |
| Design/media | Gemini Omni video | Aug 7 builder showcase |
| Design/media | Google Vids avatars | Aug 4 roundup |
| Design/media | OpenChatCut | Jul 15 creation; 985 stars Aug 11 |
| Design/media | Pireel | Jul 20 creation; 922 stars Aug 11 |
| Design/media | Open Kimi PPT skill | Aug 5 creation; 1,603 stars Aug 11 |
| Business automation | Notion Meeting Notes trigger | Jul 31 release |
| Business automation | Notion Custom Agent sharing | Aug 7 release |
| Business automation | Notion Workers usage dashboard | Jul 24 release |
| Business automation | Notion Agent calendar tools | Jul 16 release |
| Business automation | Agentforce Coworker | Aug 4 beta |
| Business automation | Google Ads/Analytics Ask Advisor | Aug 10 beta update |
| Business automation | Comp AI CRM | Jul 31 creation; 8,170 stars Aug 11 |
| Business automation | GenOffice | Jul 31 creation; 2,539 stars Aug 11 |
| Open/local models | LFM2.5-2.6B | Aug 4 launch |
| Open/local models | DeepSeek V4 Flash 0731 | Jul 31 release |
| Open/local models | TurboFieldfare | Jul 17 creation; 5,717 stars Aug 11 |
| Open/local models | Kimi-K3-in-C | Aug 1–7 signal |
| Open/local models | Kimi K3 | Jul 27 HF signal |
| Open/local models | Inkling-Small | Jul 15/27 signal |
| Open/local models | GLM-5.2 FP8 + OpenCode | Jul 13 workflow |
| Open/local models | Nemotron 3 Embed | Jul 16 HF signal |
| Voice | Qwen Audio Agent | Jul 27 creation; 2,076 stars Aug 11 |
| Privacy/security | Open Kritt | Jul 20 creation; 1,664 stars Aug 11 |
| Privacy/security | Numbat | Jul 24 creation; 887 stars Aug 11 |

## Source and limitation notes

- **Source classes checked:** official product/release pages; GitHub repository, release, and search APIs; Hugging Face model/blog references; Hacker News/Show HN; accessible YouTube metadata; OpenAI Academy; Anthropic, Google, Notion, Kiro, Prime Intellect, Runway, Perplexity, Microsoft, Simon Willison, and Latent Space material.
- **GitHub Trending:** GitHub has no stable historical Trending API. Creation dates, releases, live metadata, searches, and dated HN signals were used. Stars are current snapshots, not verified growth except where a previous snapshot is explicitly compared.
- **Product Hunt:** its feed was inaccessible/empty during this run; no upvote or ranking claims were made. Items without stronger evidence were excluded from the top ranking.
- **Reddit/X/LinkedIn:** access and login reliability were insufficient for systematic collection. No unsupported social claims were used.
- **Newsletters:** Latent Space was partly accessible; Simon Willison’s feed extraction was unreliable, though direct dated pages from prior collection remained usable. Ben’s Bites and The Rundown could not be systematically retrieved in this run.
- **YouTube:** exact dates were unavailable for some results displayed as “N days ago”; those were used as practitioner-interest signals, not exact publication-date claims. The n8n official webinar exposed an exact August 5 timestamp.
- **Official/vendor evidence:** OpenAI user counts, Anthropic/Cognizant outcomes, Kiro internal adoption, model benchmarks, sandbox volume/security, and local inference speed are attributed to their publishers.
- **Availability:** many items are beta, staged, regional, plan-limited, or hardware-specific. Verify current access, pricing, data retention, licenses, and permissions.
- **Security baseline:** separate identities; read-only/least privilege first; secrets outside model-visible context; scoped repositories/worktrees; disposable sandboxes; egress allowlists; confirmation for external writes; durable traces; deterministic test/eval gates; reviewable memory with provenance and deletion.
