# Top AI tools and workflows — last 30 days

Research date: 2026-06-29 11:27:24 EDT  
Window: 2026-05-30 to 2026-06-29  
Scope: AI tools, products, open-source projects, and practical workflows relevant to coding agents, agent infrastructure, research/knowledge work, creative production, business automation, local/open models, and AI operations.

## Executive summary

The strongest signal this month is not a single chatbot or model launch; it is the consolidation of **repeatable agent workflows**. The winners are systems that turn “vibe prompting” into reusable procedures: Codex Record & Replay skills, Claude Code dynamic workflows, MCP/skill discovery, AI-native knowledge bases, model routers, and agent memory layers.

Major themes:

1. **Reusable skills are becoming the unit of automation.** OpenAI Codex Record & Replay, Builder.io Skills, Cloudflare’s Security Audit Skill, Claude Code workflow tutorials, and HF Agentic Resource Discovery all point toward packaged, inspectable automation.
2. **Coding agents are moving from IDE helpers to operating systems.** Claude Code workflows, Codex plugins, ORG2, Omnigent, Vercel Eve, MiMo-Code, and Loop Engineering all emphasize orchestration, reviewability, isolation, and repeatable loops.
3. **MCP and discovery are turning into infrastructure, not novelty.** HF’s `ai-catalog.json` / Discover Tool, Adobe CX skills in Claude/Copilot, CodeSeek, CodexPro, Reference MCP, and OpenKnowledge all rely on discoverable external capabilities.
4. **Research and knowledge workflows are becoming agentic.** Perplexity Computer + Brain, Perplexity Search-as-Code, OpenKnowledge, NotebookLM’s code-enabled research workflow, and AI secretary patterns are increasingly practical.
5. **Creative/content tools now package whole workflows.** Runway Agent 2.0, Adobe Firefly Creative Agent, Canva AI updates, Claude Code content systems, and n8n video/social automations are moving beyond one-off asset generation.
6. **Open/local model work is still strategically important but less immediately plug-and-play.** North Mini Code, mlx-code, Gemma 4, DiffusionGemma, and OpenEnv are important for cost, privacy, and evaluation, but require more engineering judgment.

## Scoring methodology

100-point rubric used consistently:

| Dimension | Weight |
|---|---:|
| Recency | 15 |
| Momentum | 20 |
| Source diversity | 15 |
| Practical utility | 20 |
| Workflow novelty | 10 |
| Adoption evidence | 10 |
| Strategic relevance to Asif | 10 |

Deductions were applied for single-source virality, unclear availability, weak evidence of real adoption, excessive permissions without a security story, and demo-only products.

## Top ranked tools/workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | OpenAI Codex role/tool workflows + Record & Replay | 98 | Try now |
| 2 | Claude Code dynamic workflows + skills/MCP | 96 | Try now |
| 3 | Agentic resource discovery + Skills/MCP ecosystem | 92 | Try now / deep-dive |
| 4 | OpenKnowledge AI-native knowledge base | 89 | Try now |
| 5 | Perplexity Computer + Brain memory workflow | 88 | Monitor / try if eligible |
| 6 | Runway + Adobe creative agents for campaigns | 87 | Try now for content teams |
| 7 | Omnigent meta-agent harness | 86 | Monitor / prototype |
| 8 | Microsoft Copilot Cowork + Azure observability agents | 86 | Monitor for enterprise |
| 9 | OpenEnv agentic RL environment standard | 84 | Deep-dive / monitor |
| 10 | n8n AI ops/content/customer automation workflows | 81 | Try now |
| 11 | Weave Router model-routing proxy | 81 | Prototype cautiously |
| 12 | Hugging Face Serge AI PR reviewer | 78 | Try now for OSS repos |
| 13 | Local/open coding models and local agents | 78 | Monitor / prototype |
| 14 | Security and memory skills for coding agents | 78 | Try now cautiously |
| 15 | NotebookLM + Perplexity research loop | 77 | Try now |

## Detailed findings

### 1. OpenAI Codex role/tool workflows + Record & Replay

Score: 98  
Category: Coding agents, desktop automation, reusable skills  
Recommendation: Try now

Why it matters: Codex is expanding from “write code” to **repeatable work automation** across roles, tools, desktop/browser actions, and plugin workflows. The most important new pattern is Record & Replay: demonstrate a workflow once, let Codex turn it into an editable skill, then rerun it with new inputs.

Evidence:
- OpenAI, “Codex for every role, tool, and workflow,” 2026-06-02: https://openai.com/index/codex-for-every-role-tool-workflow/
- OpenAI docs, “Record and replay”: https://developers.openai.com/codex/record-and-replay
- Ben’s Bites, “Record a skill,” 2026-06-23: https://www.bensbites.com/p/record-a-skill
- YouTube workflow examples: lead-list automation (2026-06-19) and YouTube upload skill (2026-06-18): https://www.youtube.com/watch?v=q6efNV3Txrw and https://www.youtube.com/watch?v=I2WK6zpnGNQ

Practical workflow:
1. Pick a repetitive Mac/browser workflow with stable UI and clear success criteria.
2. Record yourself doing it once in Codex.
3. Let Codex generate `SKILL.md` / automation instructions.
4. Edit the skill to remove secrets, add validation, and document expected inputs/outputs.
5. Replay on a new input; keep human approval before irreversible actions.

Best next step: Build one low-risk skill: “prepare weekly research brief,” “upload draft video privately,” or “create lead list draft,” then measure time saved.

### 2. Claude Code dynamic workflows + skills/MCP

Score: 96  
Category: Coding agents, orchestration, multi-agent workflow  
Recommendation: Try now

Why it matters: Claude Code usage is shifting from a single chat agent to **workflow-generated orchestration**: specs, scripts, subagents, clean contexts/worktrees, verifier agents, and reusable skills.

Evidence:
- YouTube, “Claude Code Dynamic Workflows,” 2026-06-05: https://www.youtube.com/watch?v=-m3QJKoQCgU
- YouTube, Boris Cherny workflow / Auto Mode playbook, 2026-06-20: https://www.youtube.com/watch?v=t9Adi80jYmo
- YouTube, dynamic workflows explainer, 2026-06-03: https://www.youtube.com/watch?v=PTpKj5t7xI8
- Ben’s Bites, “Opus 4.8,” 2026-06-02: https://www.bensbites.com/p/opus-48
- Builder.io Skills repo, created 2026-06-10, 2,884 stars / 151 forks at collection: https://github.com/BuilderIO/skills

Practical workflow:
1. Write a compact spec and acceptance tests before invoking the agent.
2. Ask Claude Code to “use a workflow” for complex work.
3. Let it generate a control script or task plan.
4. Split implementation into parallel agents/worktrees.
5. Run automated tests and verifier-agent review.
6. Merge only after human review.

Best next step: Standardize one internal `plan.md` / `acceptance.md` workflow and reuse it across Hermes/reporting tasks.

### 3. Agentic resource discovery + Skills/MCP ecosystem

Score: 92  
Category: Agent infrastructure, MCP, discovery, skills  
Recommendation: Try now / deep-dive

Why it matters: Agents need to discover tools safely and dynamically. HF’s Agentic Resource Discovery proposal and Discover Tool make Skills, ML apps, MCP servers, and A2A agents discoverable via a registry-like `ai-catalog.json`. This is the infrastructure layer that can connect Codex, Claude, desktop agents, and enterprise tools.

Evidence:
- Hugging Face, “Agentic Resource Discovery,” 2026-06-17: https://huggingface.co/blog/agentic-resource-discovery-launch
- Adobe CX skills available in Claude Enterprise and Microsoft 365 Copilot Cowork, 2026-06-22: https://news.adobe.com/news/2026/06/adobe-accelerates-agentic-ai-adoption
- CodeSeek MCP code intelligence, pushed 2026-06-29: https://github.com/CodeBendKit/codeseek
- CodexPro MCP coding agent, created 2026-06-16: https://github.com/rebel0789/codexpro

Practical workflow:
1. Maintain a curated internal catalog of approved MCP servers/skills.
2. Include trust metadata: owner, scopes, required tokens, data access, last reviewed date.
3. Let agents search only approved registries by default.
4. Use sandboxing and audit logs for newly discovered tools.

Best next step: Create a small approved-tool registry for Asif’s AI workflows: GitHub, browser, research, docs, local filesystem, and content publishing.

### 4. OpenKnowledge AI-native knowledge base

Score: 89  
Category: Research/knowledge workspace, agent memory, documentation  
Recommendation: Try now

Why it matters: OpenKnowledge combines markdown, RAG, git/CRDT collaboration, MCPs, skills, and integrations with Claude/Codex/Cursor. It is a strong example of knowledge bases becoming **agent workspaces**, not just document stores.

Evidence:
- GitHub repo, created 2026-06-03 / pushed 2026-06-29, 1,519 stars / 67 forks at collection: https://github.com/inkeep/open-knowledge
- Hacker News Show HN, 2026-06-25, 376 points / 172 comments reported by collection.

Practical workflow:
1. Store project docs and research as markdown.
2. Let coding/research agents read/write structured notes.
3. Use MCP/RAG for retrieval.
4. Keep git history for review and rollback.
5. Use skills for recurring research, coding, and documentation patterns.

Best next step: Pilot it against one research corpus or agent-project wiki before moving production knowledge.

### 5. Perplexity Computer + Brain memory workflow

Score: 88  
Category: Research agents, desktop automation, memory  
Recommendation: Monitor / try if eligible

Why it matters: Perplexity is combining desktop/browser automation with self-improving memory. Brain builds an internal graph of work, reviews it overnight, and updates future task context. This directly addresses recurring-agent context drift.

Evidence:
- Perplexity Brain, 2026-06-18: https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents
- Perplexity Personal Computer for Windows, 2026-06-03: https://www.perplexity.ai/hub/blog/personal-computer-is-coming-to-windows
- Practitioner workflow: Perplexity Agent API + Search-as-Code, 2026-06-10: https://www.youtube.com/watch?v=DPS2VDMAYo0
- Perplexity Search-as-Code research, 2026-06-01: https://research.perplexity.ai/articles/rethinking-search-as-code-generation

Practical workflow:
1. Use Perplexity for research tasks requiring citations and web breadth.
2. Let Brain remember recurring sources, corrections, and task preferences.
3. Export important findings into a durable markdown/git knowledge base.
4. Verify citations and avoid letting memory become an unreviewed source of truth.

Best next step: Monitor availability; test on recurring competitive research or AI-trends collection if accessible.

### 6. Runway + Adobe creative agents for campaigns

Score: 87  
Category: Design/media/content production  
Recommendation: Try now for content teams

Why it matters: Creative AI is shifting from one-off generation to **campaign construction**: ads, edits, variants, analytics, and production timelines.

Evidence:
- Runway Agent 2.0, 2026-06-25: https://runwayml.com/news/introducing-agent-2
- Runway Studio update, 2026-06-18: https://runwayml.com/changelog
- Runway Aleph 2.0 in Figma Weave, 2026-06-22: https://runwayml.com/news/aleph-2-in-figma-weave
- Adobe Firefly Creative Agent expansion, 2026-06-18: https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion

Practical workflow:
1. Start from a campaign brief and audience.
2. Generate ad/storyboard/video variants.
3. Use Firefly/Adobe or Runway agents to iterate assets.
4. Keep human brand/legal review in the loop.
5. Publish only after provenance/disclosure checks.

Best next step: Use for campaign ideation and drafts; do not fully automate public publishing yet.

### 7. Omnigent meta-agent harness

Score: 86  
Category: Agent infrastructure, harness orchestration  
Recommendation: Monitor / prototype

Why it matters: Omnigent is a meta-harness for orchestrating Claude Code, Codex, Cursor, Pi, custom agents, policies, sandboxing, and collaboration. The high star velocity suggests strong demand for neutral control planes over many agents.

Evidence:
- GitHub repo, created 2026-06-11 / pushed 2026-06-29, 5,421 stars / 691 forks at collection: https://github.com/omnigent-ai/omnigent

Practical workflow:
1. Register multiple agent backends.
2. Define policies and sandbox boundaries.
3. Route tasks by strength and cost.
4. Use shared artifacts and review gates.

Best next step: Prototype with non-sensitive repos only; evaluate security model before serious adoption.

### 8. Microsoft Copilot Cowork + Azure observability agents

Score: 86  
Category: Enterprise agents, productivity/workspace, AI ops  
Recommendation: Monitor for enterprise

Why it matters: Microsoft is productizing workplace agents and observability agents, making AI coworkers and agentic cloud operations more mainstream in large organizations.

Evidence:
- Microsoft Copilot Cowork GA, 2026-06-16: https://blogs.microsoft.com/blog/2026/06/16/achieving-success-with-ai/
- Azure Copilot Observability Agent GA, 2026-06-23: https://blogs.microsoft.com/blog/2026/06/23/rethinking-cloud-operations-with-agentic-observability/
- Adobe CX skills in Microsoft 365 Copilot Cowork, 2026-06-22: https://news.adobe.com/news/2026/06/adobe-accelerates-agentic-ai-adoption

Practical workflow:
1. Identify repeatable Microsoft 365 / Azure operational workflows.
2. Delegate low-risk multi-step tasks to Cowork.
3. Use observability agents for incident triage/correlation.
4. Keep cost and permission auditing strict.

Best next step: If in Microsoft 365/Azure environments, test on read-heavy workflows first.

### 9. OpenEnv agentic RL environment standard

Score: 84  
Category: Evaluation, training environments, agentic RL  
Recommendation: Deep-dive / monitor

Why it matters: As agents move from chat to action, environment standards matter. OpenEnv aims to standardize interfaces among harnesses, deployable terminal/browser/MCP environments, and trainers.

Evidence:
- Hugging Face blog, 2026-06-08: https://huggingface.co/blog/openenv-agentic-rl
- GitHub repo pushed 2026-06-29; 2,370 stars / 403 forks at collection.

Practical workflow:
1. Define task environments with explicit tools and rewards.
2. Run agents in repeatable browser/terminal/MCP contexts.
3. Compare harnesses and model policies objectively.
4. Use results to tune agent workflows, not just benchmark models.

Best next step: Track standardization; use ideas for internal eval harnesses even if not adopting immediately.

### 10. n8n AI ops/content/customer automation workflows

Score: 81  
Category: Business automation, AI ops, content, customer support  
Recommendation: Try now

Why it matters: n8n remains one of the most practical places to wire AI agents into real systems: Slack, Gmail, Airtable, Redis memory, Telegram, YouTube/TikTok, CSV analytics, error handlers, and human approval nodes.

Evidence:
- Slack + Redis persistent-memory agent tutorial: https://www.youtube.com/watch?v=U92JgQUy2wQ
- Self-healing n8n workflow repair agent, 2026-06-15: https://www.youtube.com/watch?v=RGuKOIWNr78
- n8n CSV analytics agent, 2026-06-07: https://www.youtube.com/watch?v=5wa9AUeTsA8
- n8n video generation + publishing, 2026-06-24: https://www.youtube.com/watch?v=DsGma1tf1fg

Practical workflow:
1. Trigger from Slack, schedule, webhook, or Telegram.
2. Use an AI Agent node with tools and memory.
3. Pull context from CRM/docs/spreadsheets.
4. Draft output.
5. Add human approval before email, publishing, or workflow patching.
6. Log outcomes for future memory/evaluation.

Best next step: Build one human-in-the-loop assistant: Slack request → research/CRM lookup → Gmail draft → approval.

### 11. Weave Router model-routing proxy

Score: 81  
Category: Model routing, cost optimization, agent infrastructure  
Recommendation: Prototype cautiously

Why it matters: Agents are expensive. Weave Router offers an OpenAI/Anthropic-compatible endpoint for routing prompts to cheaper/faster or stronger models, which is highly relevant to Claude/Codex/Cursor-style workflows.

Evidence:
- GitHub repo pushed 2026-06-29; 582 stars / 26 forks: https://github.com/workweave/router
- HN Show HN, 2026-06-26, 212 points / 112 comments reported by collection.

Practical workflow:
1. Place router between agent client and model providers.
2. Route simple calls to cheaper models.
3. Escalate hard tasks to frontier models.
4. Monitor failure cases and privacy implications.

Best next step: Test on synthetic/non-sensitive workloads and compare quality/cost before production.

### 12. Hugging Face Serge AI PR reviewer

Score: 78  
Category: Code review, repository automation  
Recommendation: Try now for OSS repos

Why it matters: Serge is a GitHub-native PR reviewer using repo-owned rules and OpenAI-compatible models. This is a practical, scoped agent use case with immediate value.

Evidence:
- Hugging Face Serge blog, 2026-06-12: https://huggingface.co/blog/huggingface/serge

Practical workflow:
1. Install Serge on a repo.
2. Encode project review rules.
3. Let Serge comment on PRs.
4. Treat output as triage, not approval.
5. Feed repeated misses back into rule files.

Best next step: Try on a low-risk open-source or internal repo with mandatory human review.

### 13. Local/open coding models and local agents

Score: 78  
Category: Local AI, open models, coding agents  
Recommendation: Monitor / prototype

Why it matters: Local and open coding agents are not beating the best cloud stacks for every task, but they are strategically important for cost control, privacy, and customization.

Evidence:
- North Mini Code, 2026-06-09: https://huggingface.co/blog/CohereLabs/introducing-north-mini-code
- mlx-code, 2026-06-06: https://huggingface.co/blog/JosefAlbers/mlx-code
- Google Gemma 4 12B developer guide, 2026-06-03: https://developers.googleblog.com/en/gemma-4-12b-the-developer-guide/
- Google DiffusionGemma, 2026-06-10: https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/
- Godcoder local-first coding agent, created 2026-06-27: https://github.com/eli-labz/Godcoder

Practical workflow:
1. Use local agents for code search, refactors, and private repo exploration.
2. Keep frontier models for high-risk architecture and complex debugging.
3. Benchmark on a fixed task set before switching.

Best next step: Keep a local coding-agent benchmark; test MLX/local tools on Apple hardware.

### 14. Security and memory skills for coding agents

Score: 78  
Category: Security, memory, agent operations  
Recommendation: Try now cautiously

Why it matters: As agents act more autonomously, security review, durable memory, and operational utilities become must-have layers.

Evidence:
- Cloudflare Security Audit Skill, created 2026-06-18, 1,759 stars / 106 forks: https://github.com/cloudflare/security-audit-skill
- brain.md, created 2026-06-18, 96 stars: https://github.com/mindmuxai/brain.md
- Reference MCP session search, created 2026-06-29: https://github.com/kuberwastaken/reference
- Adrafinil macOS keep-awake utility, HN Show HN 2026-06-27: https://github.com/kageroumado/adrafinil

Practical workflow:
1. Add a security-audit skill as a required review gate.
2. Store durable project memory in plain files with reviewable diffs.
3. Avoid sharing cross-agent session history without clear privacy rules.
4. Use ops utilities for long-running agents only when logs and kill switches exist.

Best next step: Use file-based memory and security review skills; hold off on cross-session sharing until trust controls are clear.

### 15. NotebookLM + Perplexity research loop

Score: 77  
Category: Research, knowledge synthesis, report generation  
Recommendation: Try now

Why it matters: The best research workflows now combine web discovery, source-grounded notebooks, code execution, and agentic summarization rather than relying on a single chat transcript.

Evidence:
- NotebookLM better research / code-enabled workflow, June 2026: https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/
- Perplexity Search-as-Code, 2026-06-01: https://research.perplexity.ai/articles/rethinking-search-as-code-generation
- Claude + NotebookLM no-code workflow tutorial, 2026-06-23: https://www.youtube.com/watch?v=8tOfGkddPNM

Practical workflow:
1. Discover sources with Perplexity/Search-as-Code.
2. Store source PDFs/URLs/notes in NotebookLM or markdown.
3. Run code for data cleaning/analysis where possible.
4. Export charts, spreadsheets, briefs, and slide drafts.
5. Verify citations manually before publishing.

Best next step: Use this exact pattern for future Hermes Research runs: discovery → source notebook → scored markdown report → GitHub archive.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agents/devtools | Codex + Claude Code workflows | Best mix of adoption, practicality, and repeatable automation |
| Agent infrastructure | Agentic Resource Discovery / MCP ecosystem | Most strategic connective tissue across tools |
| Browser/computer-use agents | Codex Record & Replay | Teach-by-demonstration is immediately understandable |
| Research/knowledge workflows | OpenKnowledge + Perplexity Brain | Strongest move toward durable agent memory and source-grounded work |
| Design/media/content | Runway Agent 2.0 + Adobe Firefly Creative Agent | Closest to full campaign workflows |
| Business automation | n8n AI workflows | Most practical for Slack/Gmail/CRM/approval loops |
| Open/local models | North Mini Code / mlx-code / Gemma 4 | Important for private and lower-cost coding workflows |
| Productivity/workspace agents | Microsoft Copilot Cowork | Strong enterprise distribution |
| Sales/GTM | Codex Record & Replay lead-list + AI GTM pipeline | Promising, but needs compliance/human review |
| Privacy/security | Cloudflare Security Audit Skill | Clear need and strong early GitHub momentum |

## Rising but less proven

- **MiMo-Code** — 11,036 GitHub stars / 1,068 forks; strong momentum, but practical workflow maturity needs validation. https://github.com/XiaomiMiMo/MiMo-Code
- **Vercel Eve** — new agent framework with 2,906 stars; monitor API stability. https://github.com/vercel/eve
- **ORG2** — open-source Cursor-style agent IDE with reviewability/control; AGPL may constrain commercial use. https://github.com/yorgai/ORG2
- **Loop Engineering / Loopy** — useful methodology and workflow libraries, but quality depends on maintained patterns. https://github.com/cobusgreyling/loop-engineering and https://github.com/Forward-Future/loopy
- **dao-code** — DeepSeek-V4 terminal coding agent with MCP/skills/hooks; model-specific. https://github.com/tigicion/dao-code
- **Agent Harness Generator** — useful for teams building custom harnesses; still early. https://github.com/ruvnet/agent-harness-generator
- **CUGA Apps / IBM CUGA** — promising enterprise harness abstraction; likely heavy for small teams. https://huggingface.co/blog/ibm-research/cuga-apps
- **Tencent EdgeOne Makers / Goldfish / Gobo** — Product Hunt-visible launches, but evidence was mostly from secondary launch pages and needs direct validation.

## Overhyped / be careful

- **Fully autonomous content/video publishing.** n8n + Veo/Runway/YouTube/TikTok workflows are useful for drafts, but public posting should keep human approval due to quality, disclosure, copyright, and brand risks.
- **Cross-agent memory/session search.** Reference MCP and similar tools are interesting but need strong privacy and permission controls.
- **Model routers in sensitive workflows.** Cost savings are attractive, but proxy layers introduce privacy, debugging, and routing-quality risks.
- **Single-source GitHub star spikes.** MiMo-Code, Omnigent, Vercel Eve, Builder.io Skills, and similar repos have strong momentum but may be immature.
- **Enterprise agent suites.** Microsoft/Adobe/Copilot integrations are strategically important, but access, pricing, and admin configuration can slow adoption.

## Try-this-week shortlist

1. **Build one Codex Record & Replay skill** for a low-risk repetitive task.
2. **Create a Claude Code workflow template** with `plan.md`, acceptance criteria, subagent/verifier steps, and test gates.
3. **Set up a small MCP/skills registry** documenting approved tools, scopes, and review dates.
4. **Pilot n8n Slack → research/CRM → Gmail draft → approval** for one business process.
5. **Try OpenKnowledge or a markdown/git knowledge base** as durable agent memory for recurring research reports.
6. **Add a security-audit skill/reviewer** to agent-generated code workflows.

## Best workflow to keep doing this monthly

Use a repeatable research pipeline:

1. Pull candidates from GitHub/HF/HN/Product Hunt/official blogs/newsletters/YouTube.
2. Store raw candidates in a markdown or structured JSON appendix.
3. Deduplicate by workflow, not product name.
4. Score with the same 100-point rubric.
5. Publish the report to GitHub.
6. Convert the top 3–5 into experiments with owner, success metric, and review date.

## Raw candidate appendix

| Candidate | Type/category | Evidence date/signals | URL |
|---|---|---|---|
| OpenAI Codex role/tool workflows | Product/workflow | 2026-06-02; 5M+ weekly active users cited by source collection | https://openai.com/index/codex-for-every-role-tool-workflow/ |
| Codex Record & Replay | Desktop/browser automation | 2026-06-18/23 practitioner coverage | https://developers.openai.com/codex/record-and-replay |
| Claude Code dynamic workflows | Coding workflow | YouTube 2026-06-03/05/20; newsletter 2026-06-02 | https://www.youtube.com/watch?v=PTpKj5t7xI8 |
| Builder.io Skills | Skills library | Created 2026-06-10; 2,884 stars | https://github.com/BuilderIO/skills |
| Cloudflare Security Audit Skill | Security skill | Created 2026-06-18; 1,759 stars | https://github.com/cloudflare/security-audit-skill |
| HF Agentic Resource Discovery | Agent infra | 2026-06-17 official blog | https://huggingface.co/blog/agentic-resource-discovery-launch |
| OpenKnowledge | Knowledge base | Created 2026-06-03; HN 2026-06-25; 1,519 stars | https://github.com/inkeep/open-knowledge |
| Perplexity Brain | Agent memory | 2026-06-18 official blog | https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents |
| Perplexity Personal Computer for Windows | Desktop agent | 2026-06-03 official blog | https://www.perplexity.ai/hub/blog/personal-computer-is-coming-to-windows |
| Perplexity Search-as-Code | Research infra | 2026-06-01 research article | https://research.perplexity.ai/articles/rethinking-search-as-code-generation |
| Runway Agent 2.0 | Creative agent | 2026-06-25 official launch | https://runwayml.com/news/introducing-agent-2 |
| Runway Studio update | Video workflow | 2026-06-18 changelog | https://runwayml.com/changelog |
| Runway Aleph 2.0 in Figma Weave | AI video/design | 2026-06-22 official post | https://runwayml.com/news/aleph-2-in-figma-weave |
| Adobe Firefly Creative Agent expansion | Creative agent | 2026-06-18 official news | https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion |
| Adobe CX skills and MCP servers | Enterprise CX agents | 2026-06-22 official news | https://news.adobe.com/news/2026/06/adobe-accelerates-agentic-ai-adoption |
| Microsoft Copilot Cowork GA | Enterprise agents | 2026-06-16 official blog | https://blogs.microsoft.com/blog/2026/06/16/achieving-success-with-ai/ |
| Azure Copilot Observability Agent | AI ops | 2026-06-23 official blog | https://blogs.microsoft.com/blog/2026/06/23/rethinking-cloud-operations-with-agentic-observability/ |
| Omnigent | Meta-agent harness | Created 2026-06-11; 5,421 stars | https://github.com/omnigent-ai/omnigent |
| MiMo-Code | Coding agent/model project | Created 2026-06-10; 11,036 stars | https://github.com/XiaomiMiMo/MiMo-Code |
| Vercel Eve | Agent framework | Created 2026-06-16; 2,906 stars | https://github.com/vercel/eve |
| ORG2 | Agent IDE | Created 2026-06-01; 1,338 stars | https://github.com/yorgai/ORG2 |
| Loop Engineering | Agent methodology/toolkit | Created 2026-06-09; 3,925 stars | https://github.com/cobusgreyling/loop-engineering |
| Loopy | Workflow/skill library | Created 2026-06-12; 2,122 stars | https://github.com/Forward-Future/loopy |
| CodeSeek | Code intelligence/MCP | Pushed 2026-06-29; 415 stars | https://github.com/CodeBendKit/codeseek |
| dao-code | Terminal coding agent | Created 2026-06-08; 550 stars | https://github.com/tigicion/dao-code |
| CodexPro | MCP coding agent | Created 2026-06-16; 1,024 stars | https://github.com/rebel0789/codexpro |
| Agent Harness Generator | Agent scaffolding | Created 2026-06-13; 344 stars | https://github.com/ruvnet/agent-harness-generator |
| Godcoder | Local-first coding agent | Created 2026-06-27; 250 stars | https://github.com/eli-labz/Godcoder |
| Weave Router | Model routing | HN 2026-06-26; 582 stars | https://github.com/workweave/router |
| brain.md | File-based agent memory | Created 2026-06-18; 96 stars | https://github.com/mindmuxai/brain.md |
| Reference MCP | Session search MCP | Created 2026-06-29 | https://github.com/kuberwastaken/reference |
| Adrafinil | Agent ops utility | HN 2026-06-27; 249 stars | https://github.com/kageroumado/adrafinil |
| North Mini Code | Open coding model | HF blog 2026-06-09 | https://huggingface.co/blog/CohereLabs/introducing-north-mini-code |
| mlx-code | Local coding agent | HF blog 2026-06-06 | https://huggingface.co/blog/JosefAlbers/mlx-code |
| OpenEnv | Agentic RL environment | HF blog 2026-06-08; 2,370 stars | https://huggingface.co/blog/openenv-agentic-rl |
| CUGA Apps | Enterprise agent harness | HF/IBM blog 2026-06-23 | https://huggingface.co/blog/ibm-research/cuga-apps |
| HF Serge | AI PR reviewer | HF blog 2026-06-12 | https://huggingface.co/blog/huggingface/serge |
| Google Gemma 4 12B | Local/open model | 2026-06-03 developer blog | https://developers.googleblog.com/en/gemma-4-12b-the-developer-guide/ |
| Google DiffusionGemma | Experimental model | 2026-06-10 developer blog | https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/ |
| OpenAI GPT-5.6 preview | Frontier model | 2026-06-26 official preview | https://openai.com/index/previewing-gpt-5-6-sol/ |
| ChatGPT Dreaming memory | Personal AI memory | 2026-06-04 official blog | https://openai.com/index/chatgpt-memory-dreaming/ |
| Anthropic Claude Tag | Slack/team agent | 2026-06-23 official news | https://www.anthropic.com/news/introducing-claude-tag |
| Anthropic Claude Fable/Mythos 5 | Frontier/cyber model | 2026-06-09; access update 2026-06-12 | https://www.anthropic.com/news/claude-fable-5-mythos-5 |
| Canva AI 2.0 / Create 2026 | Creative productivity | June 2026 | https://www.canva.com/newsroom/news/canva-create-2026-ai/ |
| n8n persistent-memory Slack agent | Business automation | Recent tutorial | https://www.youtube.com/watch?v=U92JgQUy2wQ |
| n8n self-healing workflow repair | AI ops | 2026-06-15 tutorial | https://www.youtube.com/watch?v=RGuKOIWNr78 |
| NotebookLM research workflow | Research/code analysis | June 2026 Google blog | https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/ |
| AI GTM/outreach agent pipeline | Sales/GTM | 2026-06-10 tutorial; 3.1K views | https://www.youtube.com/watch?v=rGdR1KC6O2s |
| The Rundown AI secretary | Productivity workflow | Accessible guide | https://app.therundown.ai/guides/build-an-ai-secretary-that-finds-open-action-items-and-plans-your-day-works-with-slack-gmail-calendar |
| Ben’s Bites Record a skill | Newsletter evidence | 2026-06-23 | https://www.bensbites.com/p/record-a-skill |
| Latent Space / AINews automation primitives | Newsletter evidence | 2026-06-19 | https://www.latent.space/p/ainews-glm-gpt-glm-52-passes-vibe |

## Limitations

- Product Hunt direct discovery was partially inconsistent; Hunted.space and accessible product pages were used where direct Product Hunt pages/feed were incomplete.
- Reddit was not materially accessible/useful during this run; no Reddit-only claims are included.
- X/Twitter and LinkedIn were not used as primary evidence because login/bot friction usually reduces reliability.
- YouTube metrics were taken from accessible search/extraction snippets and may change quickly.
- GitHub stars/forks are point-in-time momentum signals collected during the run, not long-term adoption proof.
- Some official launch pages may be staged/preview/limited-access products; recommendations distinguish try-now from monitor.
- The report ranks workflows and practical utility, not raw model benchmark performance.
