# Top AI tools and workflows — last 30 days

Research date: 2026-06-03 16:31:33 CEST
Window: 2026-05-04 to 2026-06-03
Scope: AI tools, agent workflows, developer infrastructure, product launches, open/local models, research/productivity workflows, design/media/content, business automation, and GTM workflows relevant to Asif.

## Executive summary

The last 30 days were dominated by **agent workflow packaging** rather than isolated model launches. The strongest signals cluster around coding agents becoming scheduled/asynchronous workers, MCP becoming the default integration layer, browser/computer-use agents moving toward production reliability, and AI tools embedding into existing work surfaces like GitHub, Microsoft 365, Google Workspace, Runway, Canva, Slack, Telegram, and spreadsheets.

Top themes:

1. **Async coding agents are now the center of gravity.** Claude Code routines, Codex `/goal`, worktrees, subagents, MCP, skills, and verification loops showed the highest practical signal.
2. **MCP is moving from experiment to operating layer.** GitHub MCP Server, Runway MCP, n8n MCP, Zapier MCP, Playwright/Browser MCP, and many new context/memory projects reinforce MCP as the connector pattern to watch.
3. **Browser/computer-use workflows are becoming more operational.** Stagehand/Browserbase, Playwright MCP, Perplexity Computer, Vercel Agent Browser, and CDP MCP bridges show a trend toward verifiable browser automation rather than prompt-only browsing.
4. **Research workflows are converging around source discovery + grounded synthesis.** Perplexity + NotebookLM is still a practical, low-friction research loop with good practitioner evidence.
5. **Creative tools are turning into agent surfaces.** Runway Agent/MCP and Canva inside Gemini point toward assistants that create or edit final media assets inside existing creative systems.
6. **Local/small-model agent reliability is rising but still early.** Forge, smolagents, smallcode, MLX-code, and related projects are promising, but require validation and sandboxing.

## Scoring methodology

100-point rubric:

| Dimension | Weight |
|---|---:|
| Recency | 15 |
| Momentum | 20 |
| Source diversity | 15 |
| Practical utility | 20 |
| Workflow novelty | 10 |
| Adoption evidence | 10 |
| Strategic relevance to Asif | 10 |

Scores were computed with a calculator/script. Deductions were applied for single-source virality, unclear access, unverified upvotes, risky permissions, early-stage claims, and lack of concrete workflow evidence.

## Top ranked tools/workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | Claude Code routines + MCP + skills + team workflow | 99 | Try now |
| 2 | Codex `/goal` + coding-factory automations | 95 | Try now |
| 3 | GitHub MCP Server for coding agents | 93 | Try now |
| 4 | Anthropic Claude Opus 4.8 + dynamic workflows | 88 | Try now / monitor |
| 5 | Stagehand/Browserbase browser automation workflow | 88 | Try now |
| 6 | Runway Agent + Runway MCP video workflow | 86 | Try now if doing media |
| 7 | OpenAI GPT-5.5 Instant + ChatGPT spreadsheet workflows | 86 | Try now |
| 8 | Hugging Face smolagents MCP/code/web agents | 85 | Try now for prototypes |
| 9 | n8n + MCP + human-in-the-loop automation | 83 | Try now |
| 10 | Perplexity + NotebookLM research loop | 82 | Keep using |
| 11 | Forge local LLM tool-calling guardrails | 81 | Monitor / deep-dive |
| 12 | Microsoft Work IQ APIs + M365 Copilot redesign | 81 | Monitor for enterprise workflows |
| 13 | Perplexity Computer + Finance Search API | 80 | Monitor / try selectively |
| 14 | Google Workspace Gemini + Antigravity/Gemini Cloud bundle | 80 | Monitor |
| 15 | Claude for Small Business | 78 | Try for SMB ops pilots |

## Detailed findings

### 1. Claude Code routines + MCP + skills + team workflow

Score: 99
Category: Coding agents / productivity workspace agents
Recommendation: Try now

Why it matters: Claude Code is no longer just an interactive coding assistant. The strongest recent evidence points to a workflow where agents are configured with repo context, skills, hooks, MCP tools, browser verification, subagents, and scheduled or event-triggered routines that can open PRs or handle docs/CI/issue tasks.

Evidence:

- Claude YouTube, **2026-05-20**: “Build a proactive agent workflow with Claude Code” — routine scheduling, GitHub/Slack/Drive connectors, PR automation; reported 129.7K views in search metadata. https://www.youtube.com/watch?v=eSP7PLTXNy8
- Claude YouTube, **2026-05-22**: “How we Claude Code” — CLAUDE.md, skills, hooks, subagents, verification and Playwright/browser checks; 34.4K views. https://www.youtube.com/watch?v=IlqJqcl8ONE
- Claude YouTube, May 2026: “Beyond the basics with Claude Code” — MCP, skills, auto mode, shared team configuration. https://www.youtube.com/watch?v=tuY2ChJIx48
- Simon Willison, **2026-05-06** and **2026-05-27**, highlighted Claude managed agents, routines, async PR workflows, and product-market fit for Claude Code/Codex. https://simonwillison.net/2026/May/6/code-w-claude-2026/ and https://simonwillison.net/2026/May/27/product-market-fit/

Practical workflow:

1. Add `CLAUDE.md` and project-specific standards.
2. Create skills/slash commands for recurring tasks.
3. Connect narrow MCP tools: GitHub, docs, browser/Playwright, issue tracker.
4. Run scheduled routines for docs gaps, CI failures, stale issues, or release-note drafts.
5. Use subagents for generator/reviewer patterns.
6. Require verification through tests, browser snapshots, or PR review before merge.

Best next step: Build one routine for this repo: “every Tuesday/Friday, scan open issues and recent commits, draft a PR or task list for missing docs/tests.”

### 2. Codex `/goal` + coding-factory automations

Score: 95
Category: Coding agents / asynchronous work agents
Recommendation: Try now

Why it matters: Codex `/goal` reframes agent work around durable milestones instead of chat turns. The evidence shows it can run for hours, maintain a task objective, and work across coding and non-coding cleanup tasks when given measurable completion criteria.

Evidence:

- OpenAI YouTube, **2026-05-21**: “Run long tasks in Codex using goals” — 33.2K views, 1.2K likes. https://www.youtube.com/watch?v=rgh0hMYPcd0
- How I AI / Claravo, May 2026: “I let Codex run for 6 hours. Here’s what happened” — reported 5h45m coding run, 3h52m email cleanup, about 6M tokens, inbox reduced from ~3,900 emails to 68 needing review. https://www.youtube.com/watch?v=2wLJl9A2CnA
- The Rundown AI, May 2026: “Set Up a Coding Factory With the New Codex App” — PRD, designer agent, feature threads, foreman reviewer, daily automations. https://app.therundown.ai/guides/set-up-a-coding-factory-with-the-new-codex-app

Practical workflow:

1. Convert desired work into a bounded goal with explicit done criteria.
2. Use spec/mockup artifacts for UI work.
3. Start one Codex thread per module or feature.
4. Use checkpoints/commits frequently.
5. Add a reviewer/foreman agent to inspect diffs and merge conflicts.
6. Let `/goal` run long, but stop at judgment points or permission boundaries.

Best next step: Use Codex `/goal` only for tasks with measurable success: test suite green, PR opened, emails categorized, Sentry issues closed, or localization files generated.

### 3. GitHub MCP Server for coding agents

Score: 93
Category: Agent infrastructure / MCP
Recommendation: Try now

Why it matters: GitHub MCP Server is the most important integration layer for repo-aware agents because it exposes the developer system of record: repositories, issues, PRs, Actions, releases, and security alerts.

Evidence:

- GitHub repo latest release **v1.1.2 on 2026-05-29**, last push **2026-06-03**. https://github.com/github/github-mcp-server
- Search-indexed GitHub metadata: about 30.4K stars, 4.3K forks, 140 contributors, 66 releases.

Practical workflow:

1. Connect Claude Code, Codex, Cursor, or another MCP client to GitHub MCP Server.
2. Start read-only, then add narrow write actions as needed.
3. Use toolsets for issues, PRs, Actions, releases, or security alerts.
4. Combine with routines/goals to triage issues, draft PRs, investigate failing CI, and generate release notes.

Best next step: Configure read-only GitHub MCP for research/triage, then create a separate write-scoped token for PR-only automation.

### 4. Anthropic Claude Opus 4.8 + dynamic workflows

Score: 88
Category: Model / agentic coding workflow
Recommendation: Try now for high-value coding; monitor access limits

Why it matters: Opus 4.8 and dynamic workflows strengthen the “multi-agent coding team” pattern: a lead agent can spawn specialized subagents and control effort depth for hard reasoning/coding tasks.

Evidence:

- Anthropic official launch, **2026-05-28**: Claude Opus 4.8, effort control, Claude Code dynamic workflows. https://www.anthropic.com/news/claude-opus-4-8
- HN and practitioner discussion in May around dynamic workflows, agent review/refinement loops, token costs, and human-question interfaces. https://news.ycombinator.com/item?id=48311705

Practical workflow:

1. Use high effort only for architecture, migrations, complex bugs, and review.
2. Use dynamic workflows to split work into researcher, implementer, tester, and reviewer agents.
3. Gate outputs through tests and human review.
4. Track cost and token usage separately from simple Claude Code tasks.

Best next step: Use Opus/dynamic workflows sparingly for high-leverage migrations, not routine edits.

### 5. Stagehand/Browserbase browser automation workflow

Score: 88
Category: Browser/computer-use agents
Recommendation: Try now

Why it matters: Browser automation is becoming practical when combined with deterministic controls, observability, session replay, structured extraction, and fallback from autonomous agents to explicit `act/extract/observe` calls.

Evidence:

- Stagehand docs and repo. https://docs.stagehand.dev/v3/basics/agent and https://github.com/browserbase/stagehand
- Search-indexed metadata: Stagehand about 22.9K stars, latest release **2026-05-28**.
- May 2026 comparison: Browser Use vs Stagehand vs Playwright MCP, with token/operational tradeoffs. https://fp8.co/articles/Browser-Use-vs-Stagehand-vs-Playwright-MCP-AI-Agent-Browser-Automation

Practical workflow:

1. Use Playwright/MCP where the task needs verifiable DOM interaction inside an existing coding agent.
2. Use Stagehand for structured extraction and reliable automation.
3. Use Browser Use for more autonomous multi-page flows.
4. Log sessions, screenshots, and extracted objects.
5. Do not grant browser agents sensitive accounts without scope limits.

Best next step: Prototype one browser workflow: competitor pricing extraction or lead form QA, with screenshots and structured JSON output.

### 6. Runway Agent + Runway MCP video workflow

Score: 86
Category: Design/media/content
Recommendation: Try now if media/content matters

Why it matters: Runway is turning generative video into an agentic production workflow. Runway Agent handles concept-to-finished-video flow, while Runway MCP lets other assistants trigger media generation from Claude, ChatGPT, Cursor, or MCP-compatible clients.

Evidence:

- Runway Agent, **2026-05-13**. https://runwayml.com/news/introducing-runway-agent
- Runway Aleph 2.0 + Edit Studio, **2026-05-21**. https://runwayml.com/news/introducing-aleph-2-and-edit-studio
- Runway MCP, **2026-05-27**. https://runwayml.com/news/mcp

Practical workflow:

1. Draft creative brief in Claude/ChatGPT.
2. Trigger Runway generation/editing via MCP or Runway Agent.
3. Generate story beats, scenes, voiceover/dialogue/music.
4. Review, edit, and export assets.
5. Use human approval for brand/legal accuracy.

Best next step: Try one short product explainer using Runway Agent plus manual brand review.

### 7. OpenAI GPT-5.5 Instant + ChatGPT spreadsheet workflows

Score: 86
Category: Productivity / model platform
Recommendation: Try now

Why it matters: The default ChatGPT model changed, and spreadsheet integrations became broadly useful for financial modeling, structured analysis, and everyday business workflows.

Evidence:

- OpenAI GPT-5.5 Instant, **2026-05-05**. https://openai.com/index/gpt-5-5-instant/
- ChatGPT for Excel & Google Sheets GA update, **2026-05-05**. https://openai.com/index/chatgpt-for-excel/
- Personal Finance in ChatGPT preview, **2026-05-15**. https://openai.com/index/personal-finance-chatgpt/
- OpenAI frontier models and Codex on AWS, **2026-06-01**. https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/

Practical workflow:

1. Use ChatGPT spreadsheet add-ins for formula generation, model review, scenario summaries, and data cleanup.
2. Keep finance/account access read-only where possible.
3. Use API/AWS availability for enterprise deployment evaluation.

Best next step: Test ChatGPT in Sheets/Excel on one weekly metrics dashboard and compare against manual analysis.

### 8. Hugging Face smolagents MCP/code/web agents

Score: 85
Category: Agent framework / local and hosted model workflows
Recommendation: Try now for prototypes

Why it matters: smolagents provides a lightweight path to code agents, tool-calling agents, web agents, MCP tools, and sandboxed execution using local or hosted models.

Evidence:

- GitHub repo release **v1.26.0 on 2026-05-29**, last push **2026-06-02**. https://github.com/huggingface/smolagents
- Search-indexed metadata: about 27.7K stars, 2.6K forks, 210 contributors.

Practical workflow:

1. Start with `CodeAgent` or `ToolCallingAgent`.
2. Add MCP tools for external systems.
3. Run code execution in Docker/E2B/Modal/Blaxel rather than host shell.
4. Compare local and hosted models for cost/latency.

Best next step: Prototype a small research or data-cleanup agent with sandboxed execution.

### 9. n8n + MCP + human-in-the-loop automation

Score: 83
Category: Business automation
Recommendation: Try now

Why it matters: n8n is becoming an AI automation backend that coding agents can inspect and modify. The strongest workflow pattern pairs visual automation, MCP, and explicit human approval gates.

Evidence:

- May 2026 YouTube: n8n official MCP syncing Next.js UI with n8n backend automations. https://www.youtube.com/watch?v=RdftvD0wj_8
- May 2026 YouTube: n8n human-in-the-loop content pipeline challenge. https://www.youtube.com/watch?v=VnrmpRgDXd4
- The Rundown AI Automations course updated May 2026. https://app.therundown.ai/courses/ai-automations-course

Practical workflow:

1. Build automation visually in n8n.
2. Expose n8n through MCP to Claude/Codex.
3. Use AI agents for classification, drafting, enrichment, or routing.
4. Require human approve/revise/reject before external sends or posts.
5. Log decisions to Google Sheets/Airtable/CRM.

Best next step: Build one HITL workflow for lead intake or content approval.

### 10. Perplexity + NotebookLM research loop

Score: 82
Category: Research/knowledge workflow
Recommendation: Keep using

Why it matters: This is still one of the best practical research loops: Perplexity finds fresh sources, the user curates them, NotebookLM synthesizes from a controlled corpus, and Perplexity is used again for counter-evidence or freshness checks.

Evidence:

- May 2026 YouTube: “This NotebookLM + Perplexity Workflow Will Cut Your Research Time by 50%.” https://www.youtube.com/watch?v=27AxmEh3qEA
- May 2026 Medium: live research session with Perplexity + NotebookLM. https://medium.com/@ayeshha2398/i-ran-a-live-research-session-with-perplexity-notebooklm-heres-what-actually-happened-a9bb8f60a335

Practical workflow:

1. Define the research question.
2. Run 5-7 Perplexity queries.
3. Manually vet and select sources.
4. Import to NotebookLM.
5. Ask for synthesis, gaps, and counterarguments.
6. Return to Perplexity for missing or opposing sources.
7. Write the final answer with both tools closed.

Best next step: Use this as the default deep-research loop for market scans and strategy memos.

### 11. Forge local LLM tool-calling guardrails

Score: 81
Category: Agent infrastructure / local AI
Recommendation: Monitor / deep-dive

Why it matters: Forge tackles a real bottleneck: getting smaller/local/open models to use tools reliably through retries, structured workflows, context handling, and proxy compatibility.

Evidence:

- Show HN **2026-05-19**: 687 points / 252 comments in collected HN metadata.
- GitHub release **v0.7.0 on 2026-05-22** and maintainer discussion around v0.7.1 adding Claude Code proxy. https://github.com/antoinezambelli/forge

Practical workflow:

1. Put Forge between local/open models and tool-calling agents.
2. Use proxy mode or Python `WorkflowRunner`.
3. Track retries, rescue parsing, and eval dashboards.
4. Compare against direct model tool calls.

Best next step: Deep-dive only after validating its claims on one local model and one tool-heavy task.

### 12. Microsoft Work IQ APIs + M365 Copilot redesign

Score: 81
Category: Productivity/workspace agents
Recommendation: Monitor for enterprise workflows

Why it matters: Microsoft is giving developers and enterprise agents more structured access to Microsoft 365 context while improving Copilot’s UI and performance.

Evidence:

- Microsoft 365 Copilot redesign, **2026-05-28**. https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/
- Work IQ APIs announcement, **2026-06-02**. https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/

Practical workflow:

1. Use Copilot as the in-app assistant for documents, mail, meetings, and enterprise search.
2. Evaluate Work IQ APIs for custom agents over Microsoft 365 context.
3. Add governance through admin dashboards and Copilot Credits controls.

Best next step: Monitor until GA/access is clear, then test one internal knowledge agent.

### 13. Perplexity Computer + Finance Search API

Score: 80
Category: Productivity / research / finance agents
Recommendation: Monitor / try selectively

Why it matters: Perplexity is embedding an AI worker into Microsoft Office surfaces and adding finance-specific retrieval to its Agent API.

Evidence:

- Perplexity Finance Search in Agent API, **2026-05-06**. https://www.perplexity.ai/hub/blog/introducing-finance-search-in-the-agent-api
- Perplexity Computer in Word, Excel, PowerPoint, Outlook, **2026-05-28**. https://www.perplexity.ai/hub/blog/computer-comes-to-word-excel-powerpoint-and-outlook

Practical workflow:

1. Use Perplexity Computer for Office document/spreadsheet/presentation/email tasks.
2. Use Finance Search API for cited market/financial data inside agents.
3. Validate finance outputs manually and record citations.

Best next step: Try it for investment/market research memos, not autonomous finance decisions.

### 14. Google Workspace Gemini + Antigravity/Gemini Cloud bundle

Score: 80
Category: Productivity/workspace agents and developer tools
Recommendation: Monitor

Why it matters: Google shipped broad Workspace Gemini updates while I/O positioned Gemini 3.5 Flash, Gemini Omni, Antigravity 2.0, Gemini Spark, and image tools as a full enterprise/developer AI stack.

Evidence:

- Google Workspace May Drop, **2026-05-28**. https://workspace.google.com/blog/product-announcements/may-workspace-drops
- Google I/O Cloud AI innovations, **2026-05-19**. https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud
- Nano Banana 2 / Nano Banana Pro GA, **2026-05-29**. https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-and-nano-banana-pro-are-generally-available

Practical workflow:

1. Use Gemini in Sheets to structure raw data and detect anomalies.
2. Use Gemini in Slides/Docs/Vids for business content generation.
3. Monitor Antigravity 2.0 for coding-agent orchestration if Google Cloud is part of the stack.

Best next step: Test Gemini in Sheets against a real messy dataset.

### 15. Claude for Small Business

Score: 78
Category: Business automation / SMB workflows
Recommendation: Try for SMB ops pilots

Why it matters: Anthropic packaged Claude around concrete SMB jobs: invoicing, payroll, month-close, docs, campaigns, DocuSign, Canva, HubSpot, Google Workspace, Microsoft 365, PayPal, and QuickBooks.

Evidence:

- Anthropic official launch, **2026-05-13**. https://www.anthropic.com/news/claude-for-small-business

Practical workflow:

1. Connect one or two business systems, not all at once.
2. Start with drafts and reconciliation summaries.
3. Require approval before sends, postings, payments, or customer-facing changes.

Best next step: Pilot on invoice chasing, monthly close prep, or campaign-draft workflows.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agents/devtools | Claude Code routines + Codex `/goal` | Most practical evidence for async, scheduled, and long-running work. |
| Agent infrastructure | GitHub MCP Server | Canonical repo/PR/issues/Actions bridge for agents. |
| Browser/computer-use agents | Stagehand/Browserbase | Best mix of automation, extraction, observability, and production posture. |
| Research/knowledge workflows | Perplexity + NotebookLM | Simple, grounded, repeatable research loop. |
| Design/media/content | Runway Agent + Runway MCP | Agentic video creation and MCP integration are strong practical shifts. |
| Business automation | n8n + MCP + HITL | Strong fit for client-facing automations with approval gates. |
| Open/local models | smolagents + Forge | smolagents for building; Forge for reliability guardrails. |
| Productivity/workspace agents | Microsoft Work IQ / M365 Copilot and Google Workspace Gemini | Enterprise work surfaces are becoming agent platforms. |
| Sales/GTM | Zapier MCP + Claude lead qualifier; Exa + Claude Code GTM workflow | Concrete lead qualification/enrichment workflows with narrow tool scopes. |
| Privacy/security | ccglass and LiteLLM Agent Platform | Useful early signs for traffic inspection and sandboxed coding-agent runs. |

## Rising but less proven

- **Superset** — parallel coding-agent worktree manager; HN launch **2026-05-22**, search-indexed ~11.4K stars. Promising for managing multiple Claude/Codex/OpenCode agents, but maturity/license/open issues need review. https://github.com/superset-sh/superset
- **Vercel Agent Browser** — browser automation skill/CLI; release **v0.27.1 on 2026-06-01**, strong stars. Needs hands-on security and reliability testing. https://github.com/vercel-labs/agent-browser
- **OpenSquilla** — token-efficient AI agent/MCP; created **2026-05-06**, search-indexed ~2.6K stars. Claims need validation. https://github.com/opensquilla/opensquilla
- **smallcode** — coding agent optimized for small/local LLMs; created **2026-05-18**, ~1.7K stars. Benchmark claims need scrutiny. https://github.com/Doorman11991/smallcode
- **Statewright** — state-machine guardrails for agents/MCP; release **v1 on 2026-05-20**. Interesting control layer, but licensing/patent and harness maturity need review. https://github.com/statewright/statewright
- **AtomicMemory / Memdex / Unabyss** — personal or agent memory layers. Useful direction, but data security and actual recall quality remain unproven.
- **Skill-creator** — MCP/OpenAPI/GraphQL-to-CLI adapter; useful integration pattern, early-stage. https://github.com/sandiiarov/skill-creator
- **DeepSWE / Open Agent Leaderboard** — agent evals are needed, but benchmark methodology and relevance must be checked before over-indexing. https://huggingface.co/blog/ibm-research/open-agent-leaderboard

## Overhyped / be careful

- **Single-source Product Hunt launches with big upvote counts.** Product Hunt access was blocked; several counts came from third-party roundups and should be treated as unverified discovery, not adoption.
- **Full-access long-running agents.** Codex `/goal`, Claude routines, browser agents, and Zapier/n8n MCP workflows can do real work, but broad permissions are dangerous. Use least-privilege tokens, checkpoints, and human approvals.
- **Local/small-model coding-agent benchmark claims.** Forge, smallcode, MLX-code, and similar projects are strategically important but need reproducible tests before use in production.
- **“AI worker inside everything” announcements.** Perplexity Computer, M365 Copilot, Google Workspace Gemini, and Claude for Small Business are valuable, but enterprise permissions, rollout status, data boundaries, and reliability will determine usefulness.
- **Media agents creating final content.** Runway Agent and Claude/HyperFrames-style workflows are impressive, but brand/legal/human creative review remains mandatory.

## Try-this-week shortlist

1. **Set up GitHub MCP Server read-only** for repo triage and PR/issue summaries.
2. **Create one Claude Code routine** for a recurring repo task: docs gaps, stale issues, release notes, or failing CI investigation.
3. **Run one Codex `/goal` task** with strict done criteria and checkpoints.
4. **Prototype a Stagehand or Playwright MCP browser workflow** for a simple extraction/QA task.
5. **Build one n8n HITL workflow** where AI drafts/classifies and a human approves before external action.
6. **Use Perplexity + NotebookLM** for the next deep research memo.
7. **Trial Runway MCP/Agent** for one short video or marketing asset if content production is on the roadmap.

## Best workflow to keep doing this monthly

Use a four-track research pipeline:

1. **Developer/open-source:** GitHub Trending/search/API, Hugging Face, HN Show HN, new repos created/pushed inside the window.
2. **Product/commercial:** official product blogs, changelogs, Product Hunt feed or secondary PH summaries if blocked.
3. **Practitioner/workflow:** YouTube metadata, newsletters, Simon Willison, Latent Space, Ben’s Bites, The Rundown, HN discussions.
4. **Synthesis:** deduplicate into workflows, score with the same 100-point rubric, and mark recommendations as try now / monitor / ignore.

For Asif, keep weighting strategic relevance toward: coding agents, MCP, browser automation, research workflows, business automation, and GTM systems.

## Raw candidate appendix

| Candidate | Category | Recent evidence/date | Recommendation |
|---|---|---|---|
| Claude Code routines | Coding/productivity | YouTube 2026-05-20 | Try now |
| Anthropic internal Claude Code setup | Coding workflow | YouTube 2026-05-22 | Try now |
| Claude Code MCP/skills/auto mode | Coding workflow | YouTube May 2026 | Try now |
| Codex `/goal` | Coding/work agents | OpenAI YouTube 2026-05-21 | Try now |
| Codex long-run cleanup workflows | Productivity/coding | Practitioner YouTube May 2026 | Try selectively |
| Codex coding factory | Coding workflow | The Rundown May 2026 | Try selectively |
| GitHub MCP Server | MCP/devtools | Release 2026-05-29, push 2026-06-03 | Try now |
| smolagents | Agent framework | Release 2026-05-29 | Try now |
| Stagehand/Browserbase | Browser agents | Release 2026-05-28 | Try now |
| Vercel Agent Browser | Browser agents | Release 2026-06-01 | Monitor |
| Forge | Local agent infra | Show HN 2026-05-19, release 2026-05-22 | Monitor/deep-dive |
| Statewright | Agent guardrails | Release 2026-05-20 | Monitor |
| Superset | Coding-agent manager | HN 2026-05-22 | Monitor |
| OpenSquilla | Agent/MCP | Created 2026-05-06 | Monitor |
| smallcode | Coding agent | Created 2026-05-18 | Monitor |
| ktx | Data/analytics context | Created 2026-05-10 | Monitor |
| wesight | Desktop AI workspace | Created 2026-05-07 | Monitor |
| DeepSeek-Code-Whale | Coding agent | Created 2026-05-06 | Monitor |
| LiteLLM Agent Platform | Sandboxed coding agents | Created 2026-05-07 | Monitor |
| deep-swe | Agent eval | Created 2026-05-15 | Monitor |
| ccglass | Agent traffic proxy | Created 2026-05-22 | Monitor |
| skill-creator | MCP/API adapter | Created 2026-05-21 | Monitor |
| AtomicMemory | Agent memory | Created 2026-05-18 | Monitor |
| cdp-bridge-mcp | Browser MCP | Created 2026-05-07 | Monitor |
| browseruse-agent-bench | Browser-agent eval | Created 2026-05-09 | Monitor |
| Paseo | Coding-agent UI | HN 2026-06-02 | Monitor |
| Komi-learn | Agent memory/self-improvement | HN 2026-05-31 | Monitor |
| Open Agent Leaderboard | Agent eval | HF blog 2026-05-18 | Monitor |
| Agent traces as memory | Agent memory workflow | HF blog 2026-05-19 | Try selectively |
| MLX-code | Local Mac coding agent | HF blog 2026-05-10 | Monitor |
| Organon | Scientific agent skills | HF blog 2026-05-05 | Monitor |
| Agent Factory 3 | Agentic RL framework | HF article 2026-05-12 | Monitor |
| OpenAI GPT-5.5 Instant | Model/productivity | OpenAI 2026-05-05 | Try now |
| ChatGPT for Excel/Sheets | Spreadsheet workflow | OpenAI 2026-05-05 | Try now |
| ChatGPT Ads self-serve | Marketing | OpenAI 2026-05-05 | Monitor |
| Personal Finance in ChatGPT | Finance/productivity | OpenAI 2026-05-15 | Monitor |
| OpenAI models/Codex on AWS | Enterprise platform | OpenAI 2026-06-01 | Monitor |
| Claude for Small Business | SMB ops | Anthropic 2026-05-13 | Try selectively |
| Claude Opus 4.8 + dynamic workflows | Coding agents | Anthropic 2026-05-28 | Try/monitor |
| M365 Copilot redesign | Workspace agents | Microsoft 2026-05-28 | Monitor |
| Work IQ APIs | Enterprise agents | Microsoft 2026-06-02 | Monitor |
| Google Workspace Gemini May Drop | Productivity | Google 2026-05-28 | Try if Workspace user |
| Google I/O Cloud AI bundle | Developer/platform | Google 2026-05-19 | Monitor |
| Nano Banana 2/Pro | Image generation | Google 2026-05-29 | Monitor |
| Runway Agent | Media/content | Runway 2026-05-13 | Try |
| Runway Aleph 2/Edit Studio | Media editing | Runway 2026-05-21 | Try |
| Runway MCP | MCP/media | Runway 2026-05-27 | Try |
| Perplexity Computer | Office productivity | Perplexity 2026-05-28 | Monitor |
| Perplexity Finance Search API | Finance agents | Perplexity 2026-05-06 | Try selectively |
| Canva Connected App for Gemini | Design/workspace | Syndicated Canva release 2026-05-19 | Monitor |
| IBM Granite Embedding R2 | Open model/retrieval | HF blog May 2026 | Monitor |
| JetBrains Mellum2 | Code/text MoE | HF blog May 2026 | Monitor |
| Zapier MCP + Claude lead qualifier | Sales/GTM | YouTube May 2026 | Try with narrow scopes |
| Exa + Claude Code GTM workflow | Sales/GTM | YouTube 2026-05-18 | Try selectively |
| Perplexity + NotebookLM | Research | YouTube/Medium May 2026 | Keep using |
| Claude/HyperFrames/ElevenLabs video pipeline | Content | Substack 2026-05-31 | Try if creator workflow |
| n8n content pipeline | Automation/content | YouTube 2026-05-24 | Try pattern |
| Product Hunt Brew | Marketing | PH roundup 2026-05-28 | Monitor |
| Product Hunt Unabyss | Memory/MCP | PH roundup 2026-05-28 | Monitor |
| Product Hunt Databox MCP | Business data/MCP | PH roundup 2026-06-02 | Monitor |
| Product Hunt Bond | GTM | PH roundup 2026-05-28 | Monitor |
| Product Hunt Mintlify Workflows | Knowledge base | PH roundup 2026-05-28 | Monitor |
| Product Hunt Memdex | Local encrypted memory | PH roundup 2026-05-28 | Monitor |

## Limitations

- Product Hunt pages/feed were blocked or inaccessible in this run, so Product Hunt upvotes were gathered from search-indexed pages and third-party weekly roundups. Treat those counts as unverified.
- GitHub unauthenticated API hit rate limits during collection. Some repo star/push/release data came from search-indexed GitHub metadata rather than direct fresh API calls.
- Reddit was not meaningfully accessible; no Reddit evidence is claimed.
- YouTube search metadata exposed views/likes/dates for many videos but not reliable comment counts.
- Some official pages, notably Canva/Notion-related pages, returned extraction errors; secondary syndicated sources were used only when dates were clear.
- This report ranks workflows by evidence and usefulness, not by exhaustive hands-on testing. Before production use, validate permissions, reliability, cost, and data security.
