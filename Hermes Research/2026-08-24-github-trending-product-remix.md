# GitHub trending repos + product remixes — last 7 days

**Research date:** 2026-08-24 12:00:31 EDT  
**Rolling window:** 2026-08-17 12:00 EDT through 2026-08-24 12:00 EDT  
**Scope:** GitHub repositories across AI and non-AI categories, ranked for current momentum, practical utility, and remix potential. Strategic preference: local-first/local-owned creator and AI products with explicit BYOK cloud integrations.

## Executive summary

This week produced four unusually coherent signals:

1. **Owned, hybrid creator infrastructure is ready to compose.** [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) led the captured weekly board with **11,167 stars this week** and combines local deployment, local media, Ollama, and user-configured cloud providers. [oMLX](https://github.com/jundot/omlx) supplies a local OpenAI-compatible Apple-Silicon endpoint. The opportunity is not another cloud video generator; it is a source-controlled studio where cloud calls are deliberate BYOK escalations.
2. **Agent trust is becoming a product layer.** [Apache Maka](https://github.com/apache/maka) records agent activity as an append-only log; [OpenBot](https://github.com/CopilotKit/OpenBot) gives coworkers governed computers and records actions; [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) tests agent, skill, MCP, and model attack surfaces. A promising product wedge is approval, receipts, and replay—not more autonomy.
3. **Memory is separating from the agent vendor.** [OpenViking](https://github.com/volcengine/OpenViking), [ai-memory](https://github.com/akitaonrails/ai-memory), and [Cumora](https://github.com/yetone/cumora) treat context, handoffs, and agent collaboration as portable infrastructure. That aligns directly with Asif's local-owned/BYOK strategy.
4. **The strongest non-app event was Mojo becoming fully open source.** Modular's official August 18 announcement opened the compiler and toolchain under Apache-2.0 with LLVM exceptions, while the repository gained **2,176 weekly stars**. This is strategically important infrastructure, though less directly useful for a 1–2 week product MVP.

**Best near-term bet:** **Proofboard**, a local approval-and-receipt layer built from Maka + OpenBot, with oMLX or a user-selected cloud model behind an explicit boundary.  
**Best creator bet:** **Owned Shorts Foundry**, a local project-folder workflow around MoneyPrinterTurbo + oMLX.  
**Best durable moat:** **Handoff Rooms**, a human-editable, cross-agent memory and handoff product from ai-memory + Cumora + Maka.

## Method and scoring

### Evidence collected

- [GitHub Trending — this week](https://github.com/trending?since=weekly) and [today](https://github.com/trending?since=daily), captured August 24.
- Authenticated GitHub REST snapshots for repository totals, creation/push dates, releases, forks, issues, and license metadata.
- GitHub search for repositories created or pushed during the window.
- Official repository READMEs and release pages.
- Official in-window announcements, notably [Mojo is now open source](https://www.modular.com/blog/mojo-open-source) on August 18 and Docker's [GitHub Agentic Workflows sandbox report](https://www.docker.com/blog/running-ai-agents-in-github-actions-with-docker-sandboxes/) on August 21.
- Hacker News/Show HN via Algolia and individual discussions, including [OpenBot](https://news.ycombinator.com/item?id=49365575), [Proliferate](https://news.ycombinator.com/item?id=49390739), [Shoehorn](https://news.ycombinator.com/item?id=49346135), and [Speko Gateway](https://news.ycombinator.com/item?id=49332751).

### 100-point rubric

| Dimension | Weight |
|---|---:|
| Recency | 15 |
| Momentum | 20 |
| Source diversity | 15 |
| Practical utility | 20 |
| Workflow novelty | 10 |
| Adoption evidence | 10 |
| Strategic fit for Asif | 10 |

Scores were summed programmatically. Penalties are reflected in the dimensions for single-source attention, age without a distinct in-window event, unclear licensing, demo-only scope, weak practical workflow, or poor local-owned/BYOK fit. Scores are decision aids, not objective quality measurements.

## Top ranked repositories

| Rank | Repository | Score | In-window signal | Recommendation |
|---:|---|---:|---|---|
| 1 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **96** | +11,167 weekly; v1.3.5 Aug 22 | **Try now / build around** |
| 2 | [modular/modular](https://github.com/modular/modular) | **92** | +2,176 weekly; compiler/toolchain opened Aug 18 | **Deep-dive / monitor adoption** |
| 3 | [openai/codex](https://github.com/openai/codex) | **90** | +1,990 daily; 0.149.1 Aug 24 | **Use as an integration target** |
| 4 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | **89** | +3,799 weekly; v0.4.16 Aug 21 | **Evaluate; review AGPL boundary** |
| 5 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | **89** | +6,078 weekly; +1,102 daily; v0.7.10 Aug 23 | **Try now on supported hardware** |
| 6 | [yetone/cumora](https://github.com/yetone/cumora) | **89** | Created Aug 17; 3,027★; v0.2.2 Aug 24 | **Prototype, not production** |
| 7 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | **89** | Created Aug 17; 2,598★; v0.0.4 Aug 22; Show HN | **Prototype with strict permissions** |
| 8 | [jundot/omlx](https://github.com/jundot/omlx) | **88** | +1,671 weekly; v0.6.3rc2 Aug 20 | **Try now on Apple Silicon** |
| 9 | [apache/maka](https://github.com/apache/maka) | **88** | +859 weekly; +408 daily; v0.1.11 Aug 18 | **Build a narrow trust experiment** |
| 10 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **85** | +2,614 weekly; v1.31.1 Aug 23 | **Evaluate cross-agent handoff** |
| 11 | [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | **82** | +1,149 weekly; v4.5.2 Aug 17 | **Run against one real agent stack** |
| 12 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **72** | +8,295 weekly; pushed Aug 19 | **Use as a directory, not a product thesis** |

## Detailed findings

### 1. MoneyPrinterTurbo

- **Repository:** [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
- **Category:** Local/BYOK creator automation
- **Score:** **96** = 15 recency + 20 momentum + 12 source diversity + 20 utility + 9 novelty + 10 adoption + 10 strategic fit
- **Why it is trending:** It had the strongest captured app-level weekly velocity: GitHub displayed **11,167 stars this week**.
- **Recent evidence:** **115,811 stars / 17,589 forks** at the authenticated snapshot; pushed August 24; [v1.3.5](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.5) published August 22.
- **Core primitive:** Topic/script-to-short-video automation covering assets, voice, captions, music, and composition.
- **What you can do:** Run WebUI/API/CLI locally; use local media and Ollama; configure user-owned keys for multiple cloud model/media providers; package repeatable short-video jobs in Docker.
- **Maturity/license:** MIT; public since March 2024 and broadly adopted. Third-party media licenses, provider costs, platform terms, and spam incentives still need workflow-level controls.
- **Verdict:** The week's best creator primitive. Build a quality/provenance layer around it rather than a one-click content farm.

### 2. Modular / Mojo

- **Repository:** [modular/modular](https://github.com/modular/modular)
- **Category:** Programming language / AI systems infrastructure
- **Score:** **92** = 15 + 18 + 15 + 18 + 10 + 9 + 7
- **Why it is trending:** GitHub displayed **2,176 stars this week**, while an independent official event materially changed the project's openness.
- **Recent evidence:** Modular announced [“Mojo is now open source”](https://www.modular.com/blog/mojo-open-source) on **August 18**, opening the compiler, tooling, and language under Apache-2.0 with LLVM exceptions. Snapshot: **29,049 stars / 3,091 forks**; pushed August 24.
- **Core primitive:** A general-purpose language and compiler/runtime stack intended to span Python-like productivity and accelerator-aware systems performance.
- **What you can do:** Build the Mojo compiler from source, modify/test the standard library, and explore kernels or inference/runtime components without depending on a closed compiler.
- **Maturity/license:** Mojo reached 1.0 source stability, but the repo API returned `NOASSERTION`; the official announcement gives Apache-2.0 with LLVM exceptions. Component-level license review remains appropriate. Compiler/tooling contributions were not yet open at announcement time.
- **Verdict:** Strategically important, but a monitor/deep-dive rather than Asif's fastest product MVP.

### 3. Codex

- **Repository:** [openai/codex](https://github.com/openai/codex)
- **Category:** Terminal coding agent
- **Score:** **90** = 15 + 19 + 11 + 20 + 7 + 10 + 8
- **Why it is trending:** GitHub displayed **1,990 stars today**, the strongest daily coding-agent signal in the captured board.
- **Recent evidence:** **116,833 stars / 17,811 forks**; pushed August 24; [0.149.1](https://github.com/openai/codex/releases/tag/rust-v0.149.1) published August 24.
- **Core primitive:** A lightweight terminal agent that reads, edits, and executes against a working repository.
- **What you can do:** Use it as the worker behind local approval queues, repository maintenance, code generation, reviews, and reproducible agent evaluations.
- **Maturity/license:** Apache-2.0; large adoption and very active releases. Model/account/provider behavior sits outside the repository license, so it is best treated as one interchangeable worker behind a local control plane.
- **Verdict:** Integrate; do not make product identity depend on a single coding-agent vendor.

### 4. OpenViking

- **Repository:** [volcengine/OpenViking](https://github.com/volcengine/OpenViking)
- **Category:** Agent context database
- **Score:** **89** = 15 + 18 + 11 + 18 + 9 + 9 + 9
- **Why it is trending:** GitHub displayed **3,799 stars this week**, one of the largest agent-infrastructure gains.
- **Recent evidence:** **32,873 stars / 2,507 forks**; pushed August 24; [v0.4.16](https://github.com/volcengine/OpenViking/releases/tag/v0.4.16) published August 21.
- **Core primitive:** A unified context layer for agent memory, knowledge/RAG, and reusable skills, exposed through an inspectable virtual-filesystem concept.
- **What you can do:** Give agents durable, tiered context; inspect retrieval; separate long-lived knowledge from one vendor's chat history.
- **Maturity/license:** AGPL-3.0; early and fast-moving, with **507 open issues** in the snapshot. Hosted or embedded product use needs careful network-copyleft analysis.
- **Verdict:** Study the data model and test locally; do not casually embed it in a closed product.

### 5. OpenLogi

- **Repository:** [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)
- **Category:** Local-first hardware utility / non-AI
- **Score:** **89** = 15 + 19 + 11 + 18 + 8 + 9 + 9
- **Why it is trending:** GitHub displayed **6,078 stars this week** and **1,102 today**—a strong signal that local control can beat account-bound peripheral software.
- **Recent evidence:** **15,629 stars / 422 forks**; pushed August 24; [v0.7.10](https://github.com/AprilNEA/OpenLogi/releases/tag/v0.7.10) published August 23.
- **Core primitive:** Native Rust HID++ control for Logitech button remapping, DPI, and SmartShift without account or telemetry.
- **What you can do:** Replace a cloud/account-oriented peripheral utility and turn physical buttons into local workflow triggers.
- **Maturity/license:** Apache-2.0 and pre-1.0; **265 open issues** suggest substantial hardware/OS edge cases.
- **Verdict:** Try on supported devices. Its remix value is as a physical trigger for local creator/agent workflows.

### 6. Cumora

- **Repository:** [yetone/cumora](https://github.com/yetone/cumora)
- **Category:** Human/agent team collaboration
- **Score:** **89** = 15 + 17 + 11 + 18 + 10 + 8 + 10
- **Why it is trending:** It went from creation on **August 17** to **3,027 stars / 362 forks** in one week.
- **Recent evidence:** Created August 17; pushed August 24; [v0.2.2](https://github.com/yetone/cumora/releases/tag/v0.2.2) published August 24.
- **Core primitive:** Cross-platform chat, group, Kanban, and calendar surfaces where agents are first-class teammates.
- **What you can do:** Coordinate human and agent teammates using cloud agents or bring-your-own Claude Code/Codex-style brains.
- **Maturity/license:** MIT and extremely new. Access control, coordination semantics, hosted-data boundaries, and operational claims require hands-on validation.
- **Verdict:** High-fit prototype candidate; do not entrust production team data yet.

### 7. OpenBot

- **Repository:** [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)
- **Category:** Governed AI coworkers / computer-use agents
- **Score:** **89** = 15 + 16 + 13 + 18 + 10 + 7 + 10
- **Why it is trending:** Created August 17, it reached **2,598 stars / 302 forks** and received a [Show HN discussion](https://news.ycombinator.com/item?id=49365575) on August 19.
- **Recent evidence:** Pushed August 24; [v0.0.4](https://github.com/CopilotKit/OpenBot/releases/tag/v0.0.4) published August 22; the maintainer explicitly called it alpha in the HN thread.
- **Core primitive:** Each AI coworker gets a browser, files, and tools, while actions are decided before execution and recorded afterward; accepts AG-UI agents.
- **What you can do:** Prototype self-hosted research, browser, and file jobs with a visible action record rather than an opaque remote worker.
- **Maturity/license:** MIT, alpha, and young. Browser/file permissions, authentication defaults, secret isolation, and multi-user exposure require strong guardrails.
- **Verdict:** Excellent remix primitive for a controlled demo; unsafe as “turn on autonomy and forget it.”

### 8. oMLX

- **Repository:** [jundot/omlx](https://github.com/jundot/omlx)
- **Category:** Local Apple-Silicon inference
- **Score:** **88** = 15 + 16 + 11 + 19 + 9 + 8 + 10
- **Why it is trending:** GitHub displayed **1,671 stars this week** as local models shifted from standalone chat to a drop-in service layer.
- **Recent evidence:** **20,515 stars / 1,736 forks**; pushed August 24; [v0.6.3rc2](https://github.com/jundot/omlx/releases/tag/v0.6.3rc2) published August 20.
- **Core primitive:** OpenAI-compatible LLM/VLM/embedding/reranker serving with continuous batching and SSD-backed KV caching on Apple Silicon, managed from a macOS menu bar app.
- **What you can do:** Point compatible clients at a localhost endpoint; make local inference the default; explicitly escalate only selected jobs to a BYOK cloud provider.
- **Maturity/license:** Apache-2.0; young, fast-moving, macOS 15+/Apple-Silicon constrained, and showing **1,104 open issues** at snapshot.
- **Verdict:** The clearest local endpoint primitive for Asif's Mac-oriented hybrid product strategy.

### 9. Apache Maka

- **Repository:** [apache/maka](https://github.com/apache/maka)
- **Category:** Local-first agent workspace / audit log
- **Score:** **88** = 15 + 15 + 12 + 19 + 10 + 7 + 10
- **Why it is trending:** GitHub displayed **859 stars this week** and **408 today** for a trust-first architecture rather than a conventional chat UI.
- **Recent evidence:** **2,750 stars / 296 forks**; pushed August 24; [v0.1.11](https://github.com/apache/maka/releases/tag/v0.1.11) published August 18.
- **Core primitive:** An append-only log of model messages, tool calls/results, permission decisions, and termination events in a local-first agent workspace.
- **What you can do:** Connect cloud APIs, compatible gateways, or local models while keeping sessions/settings/run records local; replay or inspect how work happened.
- **Maturity/license:** Apache-2.0 and Apache Incubating; early. The documented local API-key vault is plaintext readable by the OS account, an explicit security tradeoff to address in any derivative.
- **Verdict:** Best trust/audit primitive in the weekly board; prototype a narrow approval layer.

### 10. ai-memory

- **Repository:** [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
- **Category:** Portable coding-agent memory
- **Score:** **85** = 15 + 17 + 10 + 17 + 9 + 7 + 10
- **Why it is trending:** GitHub displayed **2,614 stars this week** for a focused cross-vendor handoff problem.
- **Recent evidence:** **4,338 stars / 317 forks**; pushed August 24; [v1.31.1](https://github.com/akitaonrails/ai-memory/releases/tag/v1.31.1) published August 23.
- **Core primitive:** Long-term memory and handoff between coding-agent CLIs.
- **What you can do:** Preserve decisions and working state when switching between agent vendors rather than replaying entire chat histories.
- **Maturity/license:** MIT; created May 2026 and iterating rapidly. Sensitive-memory redaction, poisoning, staleness, and deletion behavior need evaluation.
- **Verdict:** High strategic fit; validate whether the handoff stays accurate on one real multi-agent project.

### 11. AI-Infra-Guard

- **Repository:** [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)
- **Category:** AI red teaming / agent security
- **Score:** **82** = 15 + 15 + 11 + 18 + 8 + 7 + 8
- **Why it is trending:** GitHub displayed **1,149 stars this week** as skill, MCP, and agent supply-chain risk became more concrete.
- **Recent evidence:** **5,729 stars / 537 forks**; pushed August 24; [v4.5.2](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.5.2) published August 17.
- **Core primitive:** Agent, skill, MCP, infrastructure, and jailbreak scanning/evaluation.
- **What you can do:** Put a security test gate in front of a skill registry, agent deployment, or BYOK workflow.
- **Maturity/license:** Apache-2.0; version 4.5.2 is more established than most new entrants, but scanner coverage and false-positive/false-negative rates were not independently benchmarked here.
- **Verdict:** Run against a real candidate stack; position results as evidence, not certification.

### 12. public-apis

- **Repository:** [public-apis/public-apis](https://github.com/public-apis/public-apis)
- **Category:** Developer resource / non-AI
- **Score:** **72** = 9 + 19 + 8 + 17 + 3 + 10 + 6
- **Why it is trending:** GitHub displayed **8,295 stars this week**, the second-largest weekly delta in the captured board.
- **Recent evidence:** **469,694 stars / 51,796 forks**; pushed August 19.
- **Core primitive:** A large curated catalog of free/public APIs.
- **What you can do:** Rapidly discover integration primitives for prototypes and create user-selectable connectors rather than inventing every data source.
- **Maturity/license:** MIT and mature since 2016. Individual APIs have their own authentication, limits, terms, quality, and availability.
- **Verdict:** Useful discovery substrate, but the weekly attention is not workflow novelty and should not drive a product by itself.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Local/BYOK creator workflow | MoneyPrinterTurbo | Highest app-level weekly velocity and explicit local/provider choice |
| Local inference | oMLX | OpenAI-compatible Apple-Silicon service layer, not merely a chat app |
| Agent trust/audit | Apache Maka | Append-only facts and permission decisions as a first-class primitive |
| Agent computer-use | OpenBot | Governed browser/files/tools with recorded actions |
| Portable memory | ai-memory | Focused cross-vendor handoff with strong weekly momentum |
| Structured context | OpenViking | Unifies memory, RAG, and skills; strong momentum, with AGPL caveat |
| Agent collaboration | Cumora | Explicit bring-your-own agent brains and unusually fast first-week uptake |
| AI security | AI-Infra-Guard | Broad agent/skill/MCP evaluation surface |
| Systems infrastructure | Modular / Mojo | A materially new open-source compiler/toolchain event |
| Local-first non-AI | OpenLogi | Strong privacy/ownership thesis with exceptional weekly momentum |
| Mature discovery resource | public-apis | Largest broad developer-resource signal; high utility, low novelty |

## Product remixes

### 1. Proofboard — **BUILD**

- **Repos/capabilities remixed:** Apache Maka + OpenBot + oMLX; optional Codex worker.
- **One-liner:** A local approval queue where agents propose browser/file/code actions, users approve immutable payloads, and every result becomes an exportable receipt.
- **Target user / JTBD:** Solo creator or small agency delegating computer work without surrendering credentials or losing accountability.
- **Why now / trend thesis:** Audit logs, governed coworkers, and local endpoints all trended together; trust is becoming a distinct product surface.
- **1–2 week MVP:** Local web/desktop app; one BYOK/local endpoint; one read-only browser or file task; propose → approve/reject → execute → append-only receipt; redacted Markdown/JSON export.
- **Differentiation:** Approval and evidence first, not “more autonomous coworkers.”
- **Local-first/BYOK:** Jobs, receipts, and key configuration remain local; oMLX is the default option and cloud execution requires an explicit user-supplied key.
- **Risks/unknowns:** Credential storage, prompt injection, replay semantics, action normalization, and alpha upstreams.
- **Recommendation:** **Build first.**

### 2. Owned Shorts Foundry — **BUILD**

- **Repos/capabilities remixed:** MoneyPrinterTurbo + oMLX + OpenLogi.
- **One-liner:** A source-controlled short-video studio where a physical trigger captures an idea, local AI drafts it, and only selected steps use BYOK cloud providers.
- **Target user / JTBD:** Technical creator who wants repeatable multi-format shorts without a SaaS project lock-in.
- **Why now / trend thesis:** The week's top creator workflow, local inference service, and local hardware utility create an end-to-end owned loop.
- **1–2 week MVP:** Project folder with brief/storyboard/assets/manifest; OpenLogi shortcut opens capture panel; oMLX creates a draft; MoneyPrinterTurbo renders one 30–60 second video; manifest records sources/providers/prompts.
- **Differentiation:** Editable source and provenance, not one-click disposable output.
- **Local-first/BYOK:** Assets, project state, and default drafting stay local; user opts into specific TTS/image/video/model providers with their own keys.
- **Risks/unknowns:** Media rights, platform spam incentives, provider cost, local hardware, and cross-provider reproducibility.
- **Recommendation:** **Build as a quality-focused creator tool, not an auto-posting bot.**

### 3. Handoff Rooms — **BUILD**

- **Repos/capabilities remixed:** ai-memory + Cumora + Apache Maka.
- **One-liner:** Human-readable project memory packets that can move between Codex, Claude Code, and local agents, with team discussion and an immutable handoff trail.
- **Target user / JTBD:** Multi-agent builder who loses decisions and context when changing tools or collaborators.
- **Why now / trend thesis:** Memory, BYOA collaboration, and auditability all have independent weekly momentum.
- **1–2 week MVP:** One local project folder; editable `HANDOFF.md` + JSON; goal/decisions/open questions/files/tests; adapters for two agents; Cumora-style card; Maka event for every import/export.
- **Differentiation:** The canonical state is user-owned and inspectable—not a hidden vendor memory.
- **Local-first/BYOK:** All memory stays local; each agent adapter uses the user's key/subscription or local endpoint.
- **Risks/unknowns:** Stale summaries, prompt injection in imported files, sensitive-memory leakage, and conflicting edits.
- **Recommendation:** **Build if Asif regularly switches agent harnesses.**

### 4. Context Firewall — **BUILD AFTER BENCHMARK**

- **Repos/capabilities remixed:** OpenViking + AI-Infra-Guard + oMLX.
- **One-liner:** A local context gateway that scans memories/skills, chooses the minimum relevant context, and requires policy approval before anything is sent to a cloud model.
- **Target user / JTBD:** Privacy-conscious agent user who needs durable context without blindly uploading an entire knowledge base.
- **Why now / trend thesis:** Context databases are growing faster than controls for poisoning, exfiltration, and selective disclosure.
- **1–2 week MVP:** Local folder/context ingest; risk scan; retrieval preview; redaction/allowlist; oMLX response; one explicit BYOK escalation; outbound request receipt.
- **Differentiation:** Visible policy at the local/cloud boundary, not opaque “smart context.”
- **Local-first/BYOK:** Storage, indexing, scanning, and default inference are local; cloud use is per request.
- **Risks/unknowns:** AGPL implications, security false negatives, retrieval quality, and data-model complexity.
- **Recommendation:** **Benchmark on a real private corpus before building a UI.**

### 5. Agent CI Foundry — **BUILD AS A DEVELOPER TOOL**

- **Repos/capabilities remixed:** GitHub `gh-aw` + AI-Infra-Guard + Codex.
- **One-liner:** Compile reviewable agent jobs into sandboxed CI, scan the task/tool surface, and emit only safe draft pull requests.
- **Target user / JTBD:** Maintainer who wants agent-assisted triage/fixes without giving a model unrestricted runner or repository access.
- **Why now / trend thesis:** Docker's August 21 report showed `gh-aw` agents running inside microVM sandboxes with network policy and safe outputs; agent security also trended.
- **1–2 week MVP:** One Markdown workflow; one Codex-compatible engine; preflight skill/MCP scan; restricted network; file allowlist; draft-PR output; human review.
- **Differentiation:** A tested policy template and evidence report, not another generic CI bot.
- **Local-first/BYOK:** Workflow definition and policy files live in the repo; user supplies provider credentials through existing CI secrets.
- **Risks/unknowns:** CI cost, sandbox availability, provider entitlements, secret injection, and false confidence in policy templates.
- **Recommendation:** **Build one opinionated workflow pack.**

### 6. Mojo Creator Engine — **MONITOR / TECH SPIKE**

- **Repos/capabilities remixed:** Modular/Mojo + MoneyPrinterTurbo + oMLX.
- **One-liner:** A local high-performance media preprocessing and model-serving core behind an owned creator pipeline.
- **Target user / JTBD:** Creator-tool developer who needs faster local transforms, batching, or accelerator-aware inference without a cloud processing tier.
- **Why now / trend thesis:** Mojo's compiler/toolchain is finally open while local creator and inference workflows are surging.
- **1–2 week MVP:** Replace one measurable Python bottleneck—caption layout, frame transform, or embedding batch—with Mojo; compare build complexity, latency, memory, and portability.
- **Differentiation:** Performance where it matters, not a wholesale rewrite or “built with Mojo” marketing layer.
- **Local-first/BYOK:** Processing stays on-device; cloud generation remains optional and user-keyed.
- **Risks/unknowns:** Toolchain churn, incomplete ecosystem, prebuilt compiler dependencies, and premature optimization.
- **Recommendation:** **Run a spike; do not commit to a rewrite.**

### 7. Skill Flight Simulator — **BUILD**

- **Repos/capabilities remixed:** AI-Infra-Guard + Apache Maka + `claude-plugins-community`/`cursor/plugins` as discovery inputs.
- **One-liner:** A local lab that executes agent skills against fixtures, permission mocks, and attack cases before users install them.
- **Target user / JTBD:** Developer or team that wants reusable skills without trusting arbitrary prompts/plugins.
- **Why now / trend thesis:** Plugin directories and security scanners appeared on the same Trending board; distribution is outrunning evaluation.
- **1–2 week MVP:** Import one skill folder; static permission inventory; five fixture tasks; mock tools; red-team prompt set; reproducible Maka trace; signed Markdown scorecard.
- **Differentiation:** Compatibility and safety receipts, not another marketplace.
- **Local-first/BYOK:** Fixtures and traces are local; user chooses a local model or supplies a compatible provider key.
- **Risks/unknowns:** Unlicensed plugin entries, incomplete mocks, benchmark gaming, and false assurance.
- **Recommendation:** **Build a small evaluator with explicit non-certification language.**

### 8. Physical Agent Desk — **PROTOTYPE**

- **Repos/capabilities remixed:** OpenLogi + NodeTerm + Cumora.
- **One-liner:** Mouse-button shortcuts create, pause, approve, or switch among visible local coding-agent sessions and team tasks.
- **Target user / JTBD:** Power user operating several local agents who wants tactile control and less terminal-window confusion.
- **Why now / trend thesis:** Local peripheral control, visual agent terminals, and BYOA collaboration all gained attention together.
- **1–2 week MVP:** Map three supported mouse buttons to “new task,” “pause all,” and “focus next approval”; display three tmux-backed sessions and one team task queue.
- **Differentiation:** Physical, local supervisory control rather than another chat tab.
- **Local-first/BYOK:** Terminals and task state stay local; agent sessions use existing user credentials.
- **Risks/unknowns:** NodeTerm's `NOASSERTION` license, device compatibility, accidental destructive shortcuts, and niche audience.
- **Recommendation:** **Prototype for personal use; do not productize until licensing is clear.**

### 9. Truthful Application Forge — **BUILD NARROWLY**

- **Repos/capabilities remixed:** ai-job-search + ai-memory + Apache Maka.
- **One-liner:** A local, evidence-only application assistant that remembers approved career facts and records every generated claim before export.
- **Target user / JTBD:** Technical freelancer or job seeker tailoring applications without uploading a full career history to a SaaS.
- **Why now / trend thesis:** `ai-job-search` had +378 stars today while portable memory and auditability also trended.
- **1–2 week MVP:** Local CV/portfolio corpus; one opportunity; requirement matching; claim-to-source citations; diff approval; Markdown export; no automated submission.
- **Differentiation:** Refuses unsupported claims and maintains a reusable owned evidence base.
- **Local-first/BYOK:** Source materials and memory local; user chooses local model or supplies their own provider credentials.
- **Risks/unknowns:** Employment-platform terms, bias, private data, fabricated claims, and over-automation.
- **Recommendation:** **Build with mandatory human-send and evidence gates.**

### 10. API Recipe Workbench — **BUILD QUICKLY**

- **Repos/capabilities remixed:** public-apis + Codex + Apache Maka.
- **One-liner:** Turn a public API into a local, inspectable automation recipe with credential scopes, sample data, tests, and an execution receipt.
- **Target user / JTBD:** Indie builder who wants integrations without committing to a cloud automation platform.
- **Why now / trend thesis:** Public API discovery saw exceptional attention while agent coding and audit logs are mainstreaming.
- **1–2 week MVP:** Select one API entry; inspect auth/terms manually; generate a typed client and one local workflow; test with fixtures; require approval before writes; export source and receipt.
- **Differentiation:** Produces owned code and explicit permission boundaries instead of a hosted connector dependency.
- **Local-first/BYOK:** Recipes, test data, and secrets remain local; any model call uses the user's chosen provider.
- **Risks/unknowns:** Stale directory entries, API terms/rate limits, generated-client bugs, and secret handling.
- **Recommendation:** **Build as a small CLI/template generator.**

### 11. Voice Boundary Box — **MONITOR / VALIDATE**

- **Repos/capabilities remixed:** Speko Gateway + oMLX + Apache Maka.
- **One-liner:** A local customer-side voice-AI data plane that keeps audio routing and audit receipts on the user's machine while allowing BYOK STT/LLM/TTS components.
- **Target user / JTBD:** Small service business testing voice automation without sending every call through one vertically integrated vendor.
- **Why now / trend thesis:** Speko's [Launch HN](https://news.ycombinator.com/item?id=49332751) reached **118 points / 69 comments**, and local serving/audit primitives are trending.
- **1–2 week MVP:** One consented test call; pluggable STT/LLM/TTS; local request log; latency/cost breakdown; no outbound dialing or production PII.
- **Differentiation:** Customer-side routing and evidence, not a hosted voice-agent builder.
- **Local-first/BYOK:** Gateway and logs local; providers selected and funded by the user.
- **Risks/unknowns:** The repo had only **6 stars / 3 forks** despite product-level HN attention; telephony compliance, latency, PII, and provider reliability.
- **Recommendation:** **Validate with synthetic calls; do not build production telephony yet.**

## Top three product bets and first experiments

### Bet 1 — Proofboard

**Rationale:** It combines three independent weekly signals—Maka's append-only facts, OpenBot's recorded computer actions, and oMLX's local endpoint—into a product whose wedge is user control. That is more defensible than another autonomous-agent chat surface.  
**First experiment:** In three days, wrap one read-only browser/file task with proposal, immutable approval payload, execution, redaction, and Markdown receipt. Run ten real tasks. Proceed if every external side effect is visible before execution, receipts are understandable in under 30 seconds, and the approval layer adds less than 20% time overhead.

### Bet 2 — Owned Shorts Foundry

**Rationale:** MoneyPrinterTurbo's exceptional weekly velocity validates the job, while oMLX and OpenLogi make the architecture distinctively local-owned. The product should sell reproducibility and editorial control—not volume.  
**First experiment:** Produce one 45-second technical explainer from a local project folder using a local draft and at most one BYOK cloud step. Change one factual claim and one brand token, then rerender. Proceed if the complete update takes under 10 minutes and every external asset/provider is visible in the manifest.

### Bet 3 — Handoff Rooms

**Rationale:** ai-memory, Cumora, and Maka attack the same pain from complementary angles: portability, collaboration, and history. A plain-file canonical state could outlive any single agent vendor.  
**First experiment:** Complete five coding tasks while alternating between two agent clients. After each switch, generate/import `HANDOFF.md`. Score missing decisions, repeated work, stale claims, and setup time. Proceed if handoffs eliminate at least half of repeated context explanation without introducing a critical false memory.

## Try now / monitor / ignore

### Try now

- **MoneyPrinterTurbo:** run one editorially controlled video project with local assets and explicit provider manifest.
- **oMLX:** expose one local OpenAI-compatible endpoint and compare latency/quality with a user-keyed cloud fallback.
- **Apache Maka:** inspect whether the append-only record is sufficient for a human-readable approval receipt.
- **OpenLogi:** validate supported-device reliability and map one harmless creator shortcut.
- **AI-Infra-Guard:** scan one real MCP/skill bundle and manually assess the findings.

### Monitor

- **Modular/Mojo:** watch compiler contribution policy, toolchain packaging, and independent production adoption after open sourcing.
- **OpenViking:** strong context architecture, but AGPL and operational complexity matter.
- **Cumora and OpenBot:** unusually fast uptake, but both are only one week old.
- **GitHub `gh-aw` + Docker Sandboxes:** compelling safety architecture; validate entitlement, CI cost, and runner availability.
- **Berd, Proliferate, Walgit, ThreeUI, and Shoehorn:** useful rising candidates described below.

### Ignore or de-prioritize this week

- **“Free token” routing as a product thesis:** attention around `free-claude-code` and `freellmapi` does not remove provider-terms, credential, reliability, or commercial-use risk.
- **A generic agent workspace clone:** the category is crowded. Build a narrow approval, handoff, or evidence job instead.
- **Auto-posting content farms:** MoneyPrinterTurbo's primitive is strong; undifferentiated volume generation has weak trust and platform risk.
- **Plugin marketplace clones without evaluation:** discovery is already abundant; security and reproducibility are the missing layers.

## Rising but less proven

| Repository | Window signal | Why it may matter | Main uncertainty |
|---|---|---|---|
| [block/berd](https://github.com/block/berd) | v0.6.2 Aug 18; 727★; official launch coverage | Local model-agnostic desktop agent workspace | New; outside PRs not accepted; differentiation vs. other workspaces |
| [github/gh-aw](https://github.com/github/gh-aw) | Docker sandbox report Aug 21; 4,990★; active Aug 24 | Markdown agent jobs compiled to controlled Actions workflows | CI entitlements/cost and operational complexity |
| [MengTo/threeui](https://github.com/MengTo/threeui) | Created Aug 21; 3,341★ / 324 forks | Login-free interactive Three.js component catalog | Four-day-old ecosystem and third-party asset terms |
| [tobi/walgit](https://github.com/tobi/walgit) | Created Aug 23; 848★ / 44 forks | Git forge with object storage as durable system of record | Brand new; compatibility and production durability |
| [proliferate-ai/proliferate](https://github.com/proliferate-ai/proliferate) | Show HN Aug 21: 45/16; release Aug 21 | Self-hostable multi-provider, multi-agent IDE/workflows | AGPL; young project with 94 open issues |
| [notactuallytreyanastasio/shoehorn](https://github.com/notactuallytreyanastasio/shoehorn) | Show HN Aug 18: 97/16; v0.3.0 Aug 19 | Cross-platform local model quantization GUI | 83★; very early quality/hardware coverage |
| [SpekoAI/gateway](https://github.com/SpekoAI/gateway) | Launch HN Aug 17: 118/69 | Local BYOK voice-AI data plane | Strong product discussion but only 6 repo stars |
| [eneskirca/nodeterm](https://github.com/eneskirca/nodeterm) | +496 weekly; v0.3.2 Aug 17 | Visual tmux-backed parallel-agent operations | `NOASSERTION` license and early maturity |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +378 daily; v1.6.0 Aug 19 | Concrete fork-and-own private workflow | Personal-data, employment-site, and Claude dependency risks |

## Overhyped or low-confidence

- **public-apis weekly virality:** **+8,295** is real, but the repository is a mature directory rather than a new capability. Do not mistake rediscovery for product innovation.
- **OpenBot/Cumora first-week counts:** impressive, but creation-date velocity is not retention, reliability, or secure production use.
- **`free-claude-code` / `freellmapi`:** daily Trending momentum is real; “free” positioning is not an endorsement of provider terms, key custody, abuse resistance, or commercial suitability.
- **OpenClaw:** very large adoption and active work, but GitHub metadata reported `NOASSERTION`; verify exact licensing and sandbox host tools before building on it.
- **Cursor plugins and NodeTerm:** GitHub exposed no clear SPDX license/`NOASSERTION`; do not assume reuse rights from public source visibility.
- **Huzzah:** the [Aug. 20 Show HN](https://news.ycombinator.com/item?id=49378768) reached 379 points / 209 comments, but the repo was a very new proof of concept with no detected license. Discussion quality does not establish reusable product maturity.
- **Maintainer benchmarks and security claims:** local-model speed, compression, scanner coverage, and sandbox guarantees need reproduction under the intended workload and threat model.

## Raw candidate appendix

The appendix deliberately exceeds the required 15 candidates. Counts are collection-time snapshots, not durable historical values.

| Candidate | Category | Window evidence | Snapshot / maturity note | Disposition |
|---|---|---|---|---|
| harry0703/MoneyPrinterTurbo | Creator AI | +11,167 weekly; v1.3.5 Aug 22 | 115.8k★; MIT | Top 1 |
| modular/modular | Systems/AI language | +2,176 weekly; compiler opened Aug 18 | 29.0k★; official Apache-2.0 + LLVM exceptions; API `NOASSERTION` | Top 2 |
| openai/codex | Coding agent | +1,990 daily; 0.149.1 Aug 24 | 116.8k★; Apache-2.0 | Top 3 |
| volcengine/OpenViking | Context DB | +3,799 weekly; v0.4.16 Aug 21 | 32.9k★; AGPL-3.0 | Top 4 |
| AprilNEA/OpenLogi | Local hardware utility | +6,078 weekly; v0.7.10 Aug 23 | 15.6k★; Apache-2.0; pre-1.0 | Top 5 |
| yetone/cumora | Agent collaboration | Created Aug 17; v0.2.2 Aug 24 | 3.0k★; MIT; very new | Top 6 |
| CopilotKit/OpenBot | Governed coworkers | Created Aug 17; Show HN Aug 19; v0.0.4 Aug 22 | 2.6k★; MIT; alpha | Top 7 |
| jundot/omlx | Local inference | +1,671 weekly; rc Aug 20 | 20.5k★; Apache-2.0 | Top 8 |
| apache/maka | Agent audit workspace | +859 weekly; v0.1.11 Aug 18 | 2.8k★; Apache Incubating | Top 9 |
| akitaonrails/ai-memory | Portable memory | +2,614 weekly; v1.31.1 Aug 23 | 4.3k★; MIT | Top 10 |
| Tencent/AI-Infra-Guard | Agent security | +1,149 weekly; v4.5.2 Aug 17 | 5.7k★; Apache-2.0 | Top 11 |
| public-apis/public-apis | API directory | +8,295 weekly; push Aug 19 | 469.7k★; MIT; mature | Top 12 / low novelty |
| NousResearch/hermes-agent | Agent platform | +899 daily; release Aug 21 | 235.6k★; MIT | Strong active candidate |
| basecamp/omarchy | Linux environment | +3,660 weekly; +1,055 daily | 29.8k★; MIT; v4 outside window | Non-AI monitor |
| makeplane/plane | Self-hosted work management | +268 daily; v1.4.2 Aug 23 | 57.8k★; AGPL-3.0 | Mature non-AI signal |
| cursor/plugins | Agent plugins | +1,761 weekly; push Aug 21 | 4.9k★; no license detected | License caution |
| anthropics/claude-plugins-community | Agent plugins | +406 weekly / +490 daily | 1.2k★; Apache-2.0 | Discovery input |
| eneskirca/nodeterm | Agent terminal UX | +496 weekly; v0.3.2 Aug 17 | 1.2k★; `NOASSERTION` | Monitor/license caution |
| MadsLorentzen/ai-job-search | Local application workflow | +378 daily; v1.6.0 Aug 19 | 33.7k★; MIT | Remix candidate |
| github/gh-aw | Agent CI | Docker post Aug 21; active Aug 24 | 5.0k★; MIT | Rising infrastructure |
| block/berd | Agent desktop | v0.6.2 Aug 18 | 727★; Apache-2.0 | Rising official launch |
| MengTo/threeui | 3D components | Created Aug 21 | 3.3k★; MIT | Rising non-AI/creator |
| tobi/walgit | Git forge | Created Aug 23 | 848★; MIT | Rising, very early |
| proliferate-ai/proliferate | Multi-agent IDE | Show HN Aug 21; release Aug 21 | 369★; AGPL-3.0 | Practitioner watch |
| notactuallytreyanastasio/shoehorn | Local model tool | Show HN Aug 18; v0.3.0 Aug 19 | 83★; MIT | Practitioner watch |
| SpekoAI/gateway | Voice AI data plane | Launch HN Aug 17: 118/69 | 6★; MIT | Product signal > repo signal |
| danielvaughn/hz | Pseudocode AI editor | Show HN Aug 20: 379/209 | Very new; no license detected | High discussion / low maturity |
| katiahayati/lucasartsifier | Game analysis | Show HN Aug 19: 161/97 | Niche non-AI; `NOASSERTION` | Interesting watch |
| alibaba/anolisa | Agent observability | Show HN Aug 21; active | Apache-2.0; sponsor-backed | Security/observability watch |
| dani-garcia/vaultwarden | Local-owned password manager | Daily Trending Aug 24 | Mature local-first benchmark | Category benchmark |

## Limitations

1. **Trending is a live snapshot, not a historical API.** GitHub's weekly page is the closest native rolling-week signal but may not align exactly with the 12:00 EDT boundaries. Daily counts represent August 24 only.
2. **Current totals change continuously.** Stars, forks, issues, and discussion counts were captured around noon EDT on August 24. Small differences between rendered pages and later API calls are normal.
3. **A push proves activity, not growth or quality.** `pushed_at` can reflect documentation, merges, automation, or maintenance; it is not a star-growth measure.
4. **Source diversity is uneven.** Modular, OpenBot, `gh-aw`, and several Show HN projects had independent in-window sources. Many Trending items had only GitHub/release evidence.
5. **Social coverage was incomplete.** X/Twitter and LinkedIn were not used because reliable logged-out metrics were unavailable. Reddit was not relied on. No inaccessible metrics are invented.
6. **Licenses need component-level verification.** Repository metadata can differ from file-level terms; models, datasets, fonts, plugins, hosted services, and generated assets may have separate licenses.
7. **Security and performance claims are not audits.** Scanner coverage, sandbox isolation, local-model speed, and compression/quality claims were not independently benchmarked for this report.
8. **New-repo virality is especially noisy.** Cumora, OpenBot, ThreeUI, Walgit, and other week-old projects lack retention and production evidence.
9. **GitHub search/API collection encountered unauthenticated rate limits in one research track.** Final top-candidate metadata was rechecked through authenticated `gh api`; incomplete candidates were omitted rather than guessed.

## Best workflow for next week's run

Persist a weekly snapshot ledger for 30–40 candidates: total stars/forks, Trending delta, latest release/tag/date, open issues, license metadata, and independent discussion signal. Comparing two authenticated snapshots will provide a more defensible week-over-week star delta than GitHub Trending alone and will distinguish one-day launch spikes from sustained adoption.
