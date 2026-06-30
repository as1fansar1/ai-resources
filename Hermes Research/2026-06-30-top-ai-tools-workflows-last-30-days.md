# Top AI tools and workflows — last 30 days

Research date: 2026-06-30 08:00:36 EDT  
Window: 2026-05-31 to 2026-06-30  
Scope: AI tools and workflows across coding agents/devtools, agent infrastructure, browser/computer-use agents, research/knowledge workflows, design/media/content, business automation, open/local models, productivity/workspace agents, sales/GTM, privacy/security.

## Executive summary

The last 30 days were dominated by **agent workflows becoming operational systems** rather than chat demos. The highest-confidence trend is the convergence of coding agents, reusable skills/plugins, remote workspaces, and human approval gates: OpenAI Codex and Claude Code are both being positioned as cross-functional workhorses, not just developer assistants. A second major theme is **agent infrastructure**: multi-agent coding ADEs, browser-agent CLIs, MCP/skills discovery, memory layers, and security scanners are filling gaps exposed by real usage. A third theme is **enterprise workspace agents**: Microsoft, Anthropic, Google, and Perplexity are pushing agents into Slack, Microsoft 365, meetings, spreadsheets, local files, and SMB workflows.

Most actionable for Asif this week: continue using agentic coding/research workflows, add stricter memory/security conventions, and experiment with n8n/MCP automation only behind approval gates.

## Scoring methodology

100-point rubric: recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance 10. Deductions applied for single-source hype, preview-only access, weak adoption evidence, excessive permissions without a clear security story, and workflows that are demo-only.

## Top ranked tools/workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | OpenAI Codex Remote + role-specific plugins/Sites/skills | 98 | Try now |
| 2 | Claude Code dynamic workflows + skills/subagents | 97 | Try now |
| 3 | Multi-agent coding ADEs: Orca + herdr + Boxes.dev pattern | 89 | Try now with review gates |
| 4 | Browser agents: Webwright + agent-browser + TinyFish/Fuse | 85 | Monitor / pilot in sandbox |
| 5 | Microsoft Copilot Cowork + Work IQ APIs | 83 | Monitor for enterprise teams |
| 6 | Hugging Face Agentic Resource Discovery / Discover | 83 | Monitor / adopt conventions early |
| 7 | n8n + Claude/Codex MCP automation workflows | 81 | Try now for bounded automations |
| 8 | Agent memory/context: Hindsight + Redis/Mem0-style patterns | 81 | Try now carefully |
| 9 | Open/local coding models: North Mini Code + Ornith | 80 | Monitor / benchmark locally |
| 10 | Research loops: Claude `/deep-research` + Codex/Airtable loops | 79 | Try now |
| 11 | OpenAI GPT-5.6 preview / GPT-Rosalind | 79 | Monitor |
| 12 | Perplexity Personal Computer local/cloud agent | 78 | Monitor |
| 13 | Agent security/evals: Pluto AgentGuard + AgentBreak + Future AGI | 77 | Try for audit/checklists |
| 14 | Adobe/Runway/Figma media-agent pipelines | 76 | Monitor / try if content-heavy |
| 15 | Google Meet Gemini notes + Workspace productivity | 74 | Try if in Google Workspace |

## Top themes

1. **Agent work is moving from prompts to repeatable loops.** Claude dynamic workflows, Codex Remote, Codex skills, n8n agents, and scheduled issue-to-PR examples all emphasize recurring procedures with state, verification, and human approval.
2. **Coding agents are becoming multi-role operating systems.** Codex is expanding to analytics, sales, finance, creative production, product design, Sites, and remote workspaces; Claude Code is formalizing subagents, skills, and dynamic orchestration.
3. **Browser/computer-use is becoming infrastructure.** Webwright, Vercel agent-browser, TinyFish, Fuse Browser, and GenericAgent point to a practical stack for web tasks, testing, scraping, and form-filling — but with high security risk.
4. **MCP needs discovery and security.** Hugging Face Agentic Resource Discovery addresses finding tools; Pluto AgentGuard and AgentBreak address unsafe configs and agent attack paths.
5. **Open/local coding models are becoming agent-specific.** North Mini Code and Ornith explicitly target terminal/SWE-bench/scaffolded agent workflows, not just chat completion.

## Detailed findings

### 1. OpenAI Codex Remote + role-specific plugins/Sites/skills

Score: 98  
Category: Coding agents/devtools; productivity/workspace agents; business automation  
Recommendation: Try now

Why it matters: Codex is being reframed as a general work engine for developers and non-developers, with remote workspaces, mobile steering, plugins, Sites, and reusable skills.

Evidence:
- OpenAI, **2026-06-02**: Codex for every role/tool/workflow; cites **5M+ weekly Codex users** and non-developer growth. https://openai.com/index/codex-for-every-role-tool-workflow/
- OpenAI release notes, **2026-06-25**: Codex Remote GA across ChatGPT plans; DigitalOcean workspace plugin. https://openai.com/products/release-notes/
- OpenAI developers, **2026-06-23**: Mastering Codex Remote engineering workflow. https://developers.openai.com/blog/mastering-codex-remote-for-engineering
- Practitioner examples, **2026-06-17 to 2026-06-26**: Codex skills, Airtable/Reddit GTM loops, AgentCard purchasing, inbox/bookmark automation. https://www.rundown.ai/articles/google-s-nobel-winner-jumps-to-anthropic and https://www.bensbites.com/p/the-first-big-exit-in-ai

Practical workflow:
1. Create a Codex workspace per project or function.
2. Encode repetitive tasks as skills: research, Airtable updates, landing-page prototypes, code review, data dashboards.
3. Trigger work from mobile or schedule bounded prompts.
4. Require approval before purchases, production deploys, email sends, or destructive file changes.
5. Review diffs/artifacts, merge manually, and promote successful prompts into reusable skills.

Best next step: Build one Codex skill for a recurring Hermes/ai-resources task: ingest sources, draft README link, and open a branch/PR only.

### 2. Claude Code dynamic workflows + skills/subagents

Score: 97  
Category: Coding agents/devtools; research/knowledge workflows  
Recommendation: Try now

Why it matters: Claude Code is formalizing a powerful pattern: it can write orchestration harnesses, fan out subagents, verify/refute claims, and save successful procedures as reusable skills.

Evidence:
- Anthropic, **2026-06-02**: Dynamic workflows in Claude Code. https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
- Practitioner guide, **2026-06-03**: dynamic workflows and “100 agents” research decomposition. https://buildtolaunch.substack.com/p/claude-code-dynamic-workflows-guide
- Product discovery workflow, **2026-06-07**: 100 interviews, opportunity extraction, scoring, prototypes, smoke checks. https://www.productcompass.pm/p/claude-code-dynamic-workflows
- The Neuron, **2026-06-09**: Claude Code agent loops/routines/agent view. https://www.theneuron.ai/explainer-articles/claude-code-creators-boris-cherny-and-cat-wu-explain-how-to-use-agent-loops/

Practical workflow:
1. Ask Claude Code to write a harness for a bounded task such as “compare 20 competitors” or “audit this repo for risky MCP config.”
2. Let it split the task into subagents: collector, verifier, critic, synthesizer.
3. Persist only the workflow template and vetted outputs, not all raw memory.
4. Add explicit stop conditions, token budgets, and final evidence tables.

Best next step: Create a reusable `deep-research-with-refutation` skill for high-stakes market scans.

### 3. Multi-agent coding ADEs: Orca + herdr + Boxes.dev pattern

Score: 89  
Category: Coding agents/devtools; agent infrastructure  
Recommendation: Try now with review gates

Why it matters: The workflow is no longer “one agent in one terminal.” The emerging pattern is parallel agents in isolated worktrees/cloud machines with a human merge gate.

Evidence:
- stablyai/orca, active **2026-06-30**, release **2026-06-30**, ~9.4k stars. https://github.com/stablyai/orca
- herdr, release **2026-06-24**, active **2026-06-30**, ~8.7k stars. https://github.com/ogulcancelik/herdr
- Boxes.dev Show HN, approx **2026-06-10**, **105 points / 79 comments**. https://news.ycombinator.com/item?id=48399358
- gstack and wshobson/agents, active in June, show multi-role/multi-harness agent plugin stacks. https://github.com/garrytan/gstack and https://github.com/wshobson/agents

Practical workflow:
1. Spin up separate worktrees/boxes per issue.
2. Run different agents for implementation, tests, docs, and review.
3. Require all branches to produce diffs, logs, and reproduction commands.
4. Merge only after human review or CI-backed acceptance tests.

Best next step: Use this for low-risk repo maintenance, not credentials, billing, or production infra.

### 4. Browser agents: Webwright + agent-browser + TinyFish/Fuse

Score: 85  
Category: Browser/computer-use agents  
Recommendation: Monitor / pilot in sandbox

Why it matters: Browser use is one of the biggest unlocks for agents, but also one of the biggest risk surfaces.

Evidence:
- Microsoft Webwright, active **2026-06-03**, ~5.7k stars; script-generating browser agent. https://github.com/microsoft/Webwright
- Vercel Labs agent-browser, release **2026-06-26**, ~37.5k stars. https://github.com/vercel-labs/agent-browser
- TinyFish × n8n web-agent node, **2026-06-11**. https://www.tinyfish.ai/blog/tinyfish-n8n-web-agents-just-landed-in-your-workflow-canvas
- TinyFish webhooks, **2026-06-25**. https://www.tinyfish.ai/blog/how-to-use-tinyfish-webhooks
- Fuse Browser MCP, created **2026-06-01**, release **2026-06-13**. https://github.com/fusengine/fuse-browser

Practical workflow:
1. Run browser agents in a separate browser profile with no personal sessions.
2. Give one task at a time: extract structured data, test a flow, fill a non-sensitive form.
3. Use webhooks for completion rather than polling.
4. Require human confirmation for login, payment, booking, purchase, or data export.

Best next step: Pilot web extraction into a CSV/Notion database with throwaway credentials.

### 5. Microsoft Copilot Cowork + Work IQ APIs

Score: 83  
Category: Productivity/workspace agents; enterprise automation  
Recommendation: Monitor for enterprise teams

Why it matters: Microsoft is turning Copilot from assistant into long-running coworker grounded in Microsoft 365 work graph and governed APIs.

Evidence:
- Copilot Cowork GA, **2026-06-16**; preview used by more than half of Fortune 500. https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/
- Work IQ APIs, announced **2026-06-02**, GA **2026-06-16**. https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/
- Copilot in Excel finance skills, **2026-06-25**. https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/25/copilot-in-excel-built-for-the-era-of-frontier-finance/
- Azure Copilot Observability Agent GA, **2026-06-23**. https://blogs.microsoft.com/blog/2026/06/23/rethinking-cloud-operations-with-agentic-observability/

Practical workflow: Delegate bounded internal work such as variance analysis, incident triage, or M365 document synthesis; log tool calls; attach source documents; review final actions.

Best next step: Monitor pricing/governance; try only if already in Microsoft 365 Copilot ecosystem.

### 6. Hugging Face Agentic Resource Discovery / Discover

Score: 83  
Category: Agent infrastructure; MCP/tooling  
Recommendation: Monitor / adopt conventions early

Why it matters: Tool discovery is a missing primitive for agent ecosystems. HF’s draft standard makes tools, skills, MCP servers, Spaces, and A2A resources searchable at runtime.

Evidence:
- Hugging Face blog, **2026-06-17**. https://huggingface.co/blog/agentic-resource-discovery-launch
- Contributors include Microsoft, Google, GoDaddy, and Hugging Face.

Practical workflow: Publish an `ai-catalog.json` for internal skills/tools; let agents search approved internal capabilities before going to the open web.

Best next step: Create a private catalog for trusted Hermes/Codex/Claude skills and MCP servers.

### 7. n8n + Claude/Codex MCP automation workflows

Score: 81  
Category: Business automation; sales/GTM; agent infrastructure  
Recommendation: Try now for bounded automations

Why it matters: n8n is becoming a practical canvas for agents that need tools, memory, webhooks, and human-in-the-loop steps.

Evidence:
- n8n production AI playbook, **2026-06-09**. https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/
- Claude + n8n MCP tutorial, **2026-06-23**. https://www.youtube.com/watch?v=ct2ZTHNvnYo
- Claude Code generates n8n JSON, **2026-06-25**. https://www.youtube.com/shorts/hp6awxThU_I
- Issue-to-PR n8n/Claude pipeline, **2026-06-05**. https://www.youtube.com/watch?v=ZmIhbPwQteQ

Practical workflow:
1. Build workflows with a visual n8n skeleton.
2. Let Claude/Codex generate nodes/JSON.
3. Add approval nodes before emails, CRM writes, PR creation, or purchases.
4. Store run logs and failure cases for evals.

Best next step: Automate one low-risk reporting workflow: source feed → extract → draft summary → approval → publish.

### 8. Agent memory/context: Hindsight + Redis/Mem0-style patterns

Score: 81  
Category: Agent memory/context  
Recommendation: Try now carefully

Why it matters: Durable memory is becoming a practical requirement for recurring agents, but it introduces poisoning, privacy, and stale-context risks.

Evidence:
- vectorize-io/hindsight, release **2026-06-18**, active **2026-06-30**, ~17.8k stars. https://github.com/vectorize-io/hindsight
- n8n + Redis persistent-memory Slack agent tutorial surfaced in June 2026. https://www.youtube.com/watch?v=U92JgQUy2wQ
- Multiple practitioner workflows in June rely on memory files, Airtable, Redis, or repo-local instructions.

Practical workflow: Store decisions, preferences, runbooks, and “known bad attempts”; avoid storing secrets; add expiration and manual pruning.

Best next step: Add a memory hygiene checklist to every long-running agent project.

### 9. Open/local coding models: North Mini Code + Ornith

Score: 80  
Category: Open/local models; coding agents  
Recommendation: Monitor / benchmark locally

Why it matters: Open models are increasingly trained and marketed for agentic coding, terminal use, scaffolds, and repo-scale tasks.

Evidence:
- CohereLabs North Mini Code on HF, **2026-06-09**. https://huggingface.co/blog/CohereLabs/introducing-north-mini-code
- Ornith 1.0, **2026-06-25**, MIT-licensed family; HF metadata showed June creation/modification and strong download signal. https://ornith.site/

Practical workflow: Run a local model against a fixed coding benchmark: small bug fix, refactor, test generation, docs update. Compare with hosted Codex/Claude on correctness, latency, and cost.

Best next step: Monitor independent benchmark replication before trusting headline claims.

### 10. Research loops: Claude `/deep-research` + Codex/Airtable loops

Score: 79  
Category: Research/knowledge workflows; sales/GTM  
Recommendation: Try now

Why it matters: The strongest practitioner workflow is a loop: collect sources, extract claims, refute/verify, synthesize, and save structured outputs.

Evidence:
- Anthropic dynamic workflows, **2026-06-02**. https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
- Product Compass product discovery loop, **2026-06-07**. https://www.productcompass.pm/p/claude-code-dynamic-workflows
- The Rundown Codex + Airtable business idea generator, **2026-06-22**. https://www.rundown.ai/articles/google-s-nobel-winner-jumps-to-anthropic

Practical workflow: Use agents to gather and dedupe evidence, but require citation URLs, dates, contradiction checks, and confidence levels before publishing.

Best next step: Convert this Hermes report into a recurring scorecard with stable candidate IDs.

### 11. OpenAI GPT-5.6 preview / GPT-Rosalind

Score: 79  
Category: Frontier models; specialized science agents  
Recommendation: Monitor

Why it matters: OpenAI signaled new frontier capability and specialized scientific workflows, but access is preview-limited.

Evidence:
- GPT-5.6 Sol/Terra/Luna preview, **2026-06-26**. https://openai.com/index/previewing-gpt-5-6-sol/
- GPT-Rosalind expanded research preview, **2026-06-03**. https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/
- OpenAI frontier models and Codex on AWS, **2026-06-01**. https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/

Practical workflow: Monitor for API access and pricing; prepare eval prompts for coding, research, and agentic tool use so the model can be tested immediately when available.

Best next step: Do not build production dependencies until broader availability and policy constraints are clear.

### 12. Perplexity Personal Computer local/cloud agent

Score: 78  
Category: Research/knowledge workflows; productivity/workspace agents; privacy  
Recommendation: Monitor

Why it matters: The proposed architecture routes work between local device and cloud agents, which could be valuable for privacy-sensitive research and SMB workflows.

Evidence:
- Perplexity “data center moves to your machine,” **2026-06-02**. https://www.perplexity.ai/hub/blog/the-data-center-moves-to-your-machine
- Personal Computer for Windows, **2026-06-03**. https://www.perplexity.ai/hub/blog/personal-computer-is-coming-to-windows
- Main Street AI Accelerator, **2026-06-04**, $25M credits program. https://www.perplexity.ai/hub/blog/perplexity-computer-for-growing-businesses

Practical workflow: Use local inference for file/email summarization, cloud for web/reasoning-heavy tasks, and explicit routing rules for sensitive data.

Best next step: Revisit after July rollout and independent privacy/security reviews.

### 13. Agent security/evals: Pluto AgentGuard + AgentBreak + Future AGI

Score: 77  
Category: Privacy/security; evals/observability  
Recommendation: Try for audit/checklists

Why it matters: As MCP and browser agents proliferate, config scanning, workflow attack modeling, and eval traces become mandatory.

Evidence:
- Pluto AgentGuard release **2026-06-26** and DEV analysis of 1,200 MCP configs, **2026-06-25**. https://dev.to/ad_0846/i-scanned-1200-mcp-configs-from-github-heres-what-i-found-45b3 and https://github.com/arpitha-dhanapathi/pluto-aguard
- AgentBreak created **2026-06-25**, release **2026-06-28**. https://github.com/JaleedAhmad/Agentbreak
- Future AGI release **2026-06-23**, active **2026-06-30**. https://github.com/future-agi/future-agi

Practical workflow: Scan MCP configs for secrets, dangerous servers, auth gaps, insecure transport, missing HITL, and risky source-to-sink chains before enabling an agent.

Best next step: Add MCP/agent config security checks to the monthly workflow.

### 14. Adobe/Runway/Figma media-agent pipelines

Score: 76  
Category: Design/media/content  
Recommendation: Monitor / try if content-heavy

Why it matters: Creative AI is shifting from one-off image/video generation to multi-step assistants embedded in design and marketing workflows.

Evidence:
- Adobe Creative Agent expansion, **2026-06-18**. https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion
- Adobe + Disney Imagineering Firefly Foundry, **2026-06-16**. https://news.adobe.com/news/2026/06/adobe-and-disney-imagineering-collaborate
- Runway Agent 2.0, **2026-06-25**. https://runwayml.com/news/introducing-agent-2
- Runway Aleph 2.0 in Figma Weave, **2026-06-22**. https://runwayml.com/news/aleph-2-in-figma-weave
- Runway Seed Audio 1.0, **2026-06-29**. https://runwayml.com/changelog

Practical workflow: Brief → storyboard → generate/edit assets → localize variations → evaluate performance → feed winning ads back into the prompt/style system.

Best next step: Use only for marketing experiments until provenance/licensing controls are clear.

### 15. Google Meet Gemini notes + Workspace productivity

Score: 74  
Category: Productivity/workspace agents  
Recommendation: Try if in Google Workspace

Why it matters: Meeting notes and follow-ups are low-risk, high-frequency tasks where AI can save time immediately.

Evidence:
- Google Meet “Take notes for me,” **2026-06-29**. https://blog.google/products-and-platforms/products/workspace/take-notes-for-me/
- Google Cloud AI June recap, **2026-06-02**. https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month

Practical workflow: Turn on Gemini notes for recurring meetings, send summaries to Docs, extract action items, and route those into a task system.

Best next step: Use for internal meetings first; check participant notification and retention settings.

## Category winners

- Coding agents/devtools: **OpenAI Codex Remote + plugins/skills**
- Agent infrastructure: **Claude Code dynamic workflows** and **Hugging Face Agentic Resource Discovery**
- Browser/computer-use agents: **Microsoft Webwright / Vercel agent-browser pattern**
- Research/knowledge workflows: **Claude dynamic research loops with refutation**
- Design/media/content: **Runway Agent 2.0 + Aleph/Figma workflow**
- Business automation: **n8n + Claude/Codex MCP**
- Open/local models: **North Mini Code + Ornith**
- Productivity/workspace agents: **Microsoft Copilot Cowork**
- Sales/GTM: **Codex + Airtable/Reddit idea and prototype loop**
- Privacy/security: **Pluto AgentGuard / AgentBreak / Future AGI stack**

## Rising but less proven

- **Oak** — Git alternative designed for agents; Show HN **2026-06-22**, 215 HN points. Promising but early and incomplete. https://oak.space/oak/oak
- **BeamWeaver** — Elixir/OTP-native agent framework; Show HN **2026-06-19**, release **2026-06-29**. Interesting for fault-tolerant agents. https://github.com/caudena/beam_weaver
- **NanoBot** — large-star personal agent with memory/MCP/WebUI, active **2026-06-30**. Needs security review. https://github.com/HKUDS/NanoBot
- **GenericAgent** — local computer-control agent, release **2026-06-26**. Powerful but high-risk permissions. https://github.com/lsdefine/GenericAgent
- **GitAgent** — “agent as repo” portable spec, active **2026-06-29**. Adoption uncertain. https://github.com/open-gitagent/gitagent
- **code-review-graph** — local-first code intelligence graph/MCP, release **2026-06-10**. Useful if graph quality holds. https://github.com/tirth8205/code-review-graph
- **Serge AI code review** — HF open-source PR reviewer, **2026-06-12**. https://huggingface.co/blog/huggingface/serge
- **NVIDIA Cosmos 3 on Hugging Face** — physical AI model release, **2026-06-01**. High compute burden. https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai

## Overhyped / be careful

- **Preview-only frontier models**: GPT-5.6 and GPT-Rosalind may be strategically important but are limited-access; do not over-index until public availability, pricing, and evals are clear.
- **Stealth/browser automation tools**: agent-browser/Fuse/TinyFish-style flows can violate site terms or leak session data if used casually.
- **Autonomous issue-to-PR or self-merging loops**: useful for bounded bugs, dangerous without tests, branch isolation, and human merge gates.
- **Memory layers**: persistent agent memory can preserve bad assumptions, secrets, and prompt-injection artifacts.
- **Creative-agent marketing claims**: Adobe/Runway demos are compelling, but production licensing/provenance and brand safety still need human review.

## Try-this-week shortlist

1. **Codex skill for recurring research ops**: source scan → evidence table → draft report section → human approve.
2. **Claude Code dynamic research harness**: collector, verifier, critic, synthesizer subagents with citations.
3. **n8n bounded automation**: RSS/Product Hunt/HN feed → candidate extraction → Slack/Telegram approval → Notion/Airtable row.
4. **Browser-agent sandbox**: web extraction only, no personal cookies, no purchases/logins.
5. **Agent security checklist**: scan MCP configs, approve tools, set memory retention, require HITL for external side effects.

## Best workflow to keep doing this monthly

Use a stable two-pass pipeline:

1. **Collector agents**: GitHub/HF/HN, official product blogs, practitioner tutorials/newsletters.
2. **Normalizer**: dedupe by product/workflow, assign categories, extract dates/metrics.
3. **Verifier**: check every top item has an in-window primary source.
4. **Scorer**: apply the same 100-point rubric and record dimension scores.
5. **Publisher**: save to `.hermes/reports/`, copy to `Hermes Research/`, update README, commit/push, verify GitHub URLs.
6. **Memory update**: track recurring candidates to distinguish genuinely new momentum from repeated hype.

## Raw candidate appendix

### Developer/open-source candidates

- Oak — https://oak.space/oak/oak — Show HN **2026-06-22**, 215 points.
- BeamWeaver — https://github.com/caudena/beam_weaver — Show HN **2026-06-19**, release **2026-06-29**.
- NanoBot — https://github.com/HKUDS/NanoBot — active **2026-06-30**, release **2026-06-23**, ~44.8k stars.
- Microsoft Webwright — https://github.com/microsoft/Webwright — active **2026-06-03**, ~5.7k stars.
- GenericAgent — https://github.com/lsdefine/GenericAgent — release **2026-06-26**, active **2026-06-30**.
- GitAgent — https://github.com/open-gitagent/gitagent — active **2026-06-29**.
- Orca — https://github.com/stablyai/orca — release **2026-06-30**, ~9.4k stars.
- herdr — https://github.com/ogulcancelik/herdr — release **2026-06-24**, ~8.7k stars.
- jcode — https://github.com/1jehuang/jcode — release **2026-06-28**, ~8k stars.
- deer-flow — https://github.com/bytedance/deer-flow — release **2026-06-25**, ~75.5k stars.
- Hindsight — https://github.com/vectorize-io/hindsight — release **2026-06-18**, ~17.8k stars.
- Vercel agent-browser — https://github.com/vercel-labs/agent-browser — release **2026-06-26**, ~37.5k stars.
- dondai1234/agent-browser — https://github.com/dondai1234/agent-browser — created **2026-06-19**, release **2026-06-27**.
- Fuse Browser — https://github.com/fusengine/fuse-browser — created **2026-06-01**, release **2026-06-13**.
- design.md — https://github.com/google-labs-code/design.md — release **2026-06-15**, ~23.5k stars.
- gstack — https://github.com/garrytan/gstack — active **2026-06-25**, large GitHub momentum.
- wshobson/agents — https://github.com/wshobson/agents — active **2026-06-29**.
- NemoClaw — https://github.com/NVIDIA/NemoClaw — active **2026-06-30**.
- code-review-graph — https://github.com/tirth8205/code-review-graph — release **2026-06-10**.
- HF Agentic Resource Discovery — https://huggingface.co/blog/agentic-resource-discovery-launch — **2026-06-17**.
- North Mini Code — https://huggingface.co/blog/CohereLabs/introducing-north-mini-code — **2026-06-09**.
- Ornith 1.0 — https://ornith.site/ — **2026-06-25**.
- Pluto AgentGuard — https://github.com/arpitha-dhanapathi/pluto-aguard — release **2026-06-26**.
- Future AGI — https://github.com/future-agi/future-agi — release **2026-06-23**.
- AgentBreak — https://github.com/JaleedAhmad/Agentbreak — created **2026-06-25**, release **2026-06-28**.

### Product/commercial candidates

- OpenAI GPT-5.6 preview — https://openai.com/index/previewing-gpt-5-6-sol/ — **2026-06-26**.
- OpenAI Codex for every role — https://openai.com/index/codex-for-every-role-tool-workflow/ — **2026-06-02**.
- OpenAI on AWS — https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/ — **2026-06-01**.
- GPT-Rosalind — https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/ — **2026-06-03**.
- Codex Remote/DigitalOcean plugin — https://openai.com/products/release-notes/ — **2026-06-25**.
- Anthropic Claude Fable/Mythos launch/suspension — https://www.anthropic.com/news/claude-fable-5-mythos-5 — **2026-06-09/12**.
- Anthropic Claude Tag beta — https://www.anthropic.com/news/introducing-claude-tag — **2026-06-23**.
- Anthropic + TCS — https://www.anthropic.com/news/tcs-anthropic-partnership — **2026-06-12**.
- Google Cloud AI June recap — https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month — **2026-06-02**.
- Google Meet notes — https://blog.google/products-and-platforms/products/workspace/take-notes-for-me/ — **2026-06-29**.
- Microsoft Copilot Cowork — https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ — **2026-06-16**.
- Microsoft Work IQ APIs — https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/ — **2026-06-02/16**.
- Microsoft Copilot Excel finance — https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/25/copilot-in-excel-built-for-the-era-of-frontier-finance/ — **2026-06-25**.
- Azure Copilot Observability — https://blogs.microsoft.com/blog/2026/06/23/rethinking-cloud-operations-with-agentic-observability/ — **2026-06-23**.
- Adobe Creative Agent expansion — https://news.adobe.com/news/2026/06/adobe-unveils-major-expansion — **2026-06-18**.
- Adobe + Disney Firefly Foundry — https://news.adobe.com/news/2026/06/adobe-and-disney-imagineering-collaborate — **2026-06-16**.
- Perplexity Personal Computer — https://www.perplexity.ai/hub/blog/the-data-center-moves-to-your-machine — **2026-06-02**.
- Perplexity PC for Windows — https://www.perplexity.ai/hub/blog/personal-computer-is-coming-to-windows — **2026-06-03**.
- Perplexity Main Street Accelerator — https://www.perplexity.ai/hub/blog/perplexity-computer-for-growing-businesses — **2026-06-04**.
- Runway Agent 2.0 — https://runwayml.com/news/introducing-agent-2 — **2026-06-25**.
- Runway Aleph 2.0 in Figma Weave — https://runwayml.com/news/aleph-2-in-figma-weave — **2026-06-22**.
- Runway Seed Audio 1.0 — https://runwayml.com/changelog — **2026-06-29**.
- HF Serge — https://huggingface.co/blog/huggingface/serge — **2026-06-12**.
- NVIDIA Cosmos 3 — https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai — **2026-06-01**.

### Practitioner/workflow candidates

- Claude + n8n MCP tutorial — https://www.youtube.com/watch?v=ct2ZTHNvnYo — **2026-06-23**, 739 views / 49 likes.
- Claude Code generates n8n JSON — https://www.youtube.com/shorts/hp6awxThU_I — **2026-06-25**, 1.3k views / 39 likes.
- Claude Opus + n8n issue-to-PR pipeline — https://www.youtube.com/watch?v=ZmIhbPwQteQ — **2026-06-05**.
- n8n production AI playbook — https://blog.n8n.io/production-ai-playbook-complex-agent-patterns/ — **2026-06-09**.
- n8n persistent memory Slack agent — https://www.youtube.com/watch?v=U92JgQUy2wQ — June signal, low views.
- n8n CSV/reporting agent — https://www.youtube.com/watch?v=5wa9AUeTsA8 — **2026-06-07**.
- n8n Shopify → Notion + Slack — https://www.youtube.com/watch?v=epqyVCngZsk — **2026-06-02**.
- n8n Veo/social pipeline — https://www.youtube.com/watch?v=DsGma1tf1fg — June signal.
- TinyFish × n8n node — https://www.tinyfish.ai/blog/tinyfish-n8n-web-agents-just-landed-in-your-workflow-canvas — **2026-06-11**.
- TinyFish webhooks — https://www.tinyfish.ai/blog/how-to-use-tinyfish-webhooks — **2026-06-25**.
- Codex record a skill — https://www.youtube.com/watch?v=q6efNV3Txrw — **2026-06-19**.
- Codex + Claude marketing workflow/evals — https://www.youtube.com/watch?v=vnrLWWcR8vY — **2026-06-17**, 970 views.
- Codex engineering workflow — https://www.youtube.com/watch?v=wX_Bt0Nt9VQ — **2026-06-07**.
- Codex Remote engineering — https://developers.openai.com/blog/mastering-codex-remote-for-engineering — **2026-06-23**.
- Codex + Airtable idea generator — https://www.rundown.ai/articles/google-s-nobel-winner-jumps-to-anthropic — **2026-06-22**.
- Codex AgentCard purchase — https://www.therundown.ai/p/white-house-reins-in-openai-gpt-5-6 — **2026-06-26**.
- Ben’s Bites Codex inbox/bookmarks/memory — https://www.bensbites.com/p/the-first-big-exit-in-ai — **2026-06-18**.
- Ben’s Bites tiny tools with Codex — https://www.bensbites.com/p/build-tools-to-build-more — **2026-06-04**.
- Claude dynamic workflows — https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code — **2026-06-02**.
- Product Compass Claude product discovery — https://www.productcompass.pm/p/claude-code-dynamic-workflows — **2026-06-07**.
- Boxes.dev Show HN — https://news.ycombinator.com/item?id=48399358 — approx **2026-06-10**, 105 points / 79 comments.
- DEV Codex consensus loop — https://dev.to/nwnwnw413/codex-fixing-codex-a-consensus-loop-that-argues-judges-and-merges-its-own-prs-11bh — **2026-06-22**.

## Limitations

- GitHub Trending monthly is directional, not a precise rolling-window API; repo created/pushed/release dates were used where available.
- Product Hunt direct pages/search were partially noisy/blocked; a June 27 digest provided some upvote signals, but Product Hunt was not used as a primary ranking source.
- Reddit, X/Twitter, and LinkedIn were not reliably accessible, so practitioner evidence came mainly from YouTube, HN, newsletters, official blogs, and developer posts.
- Some YouTube results exposed views/likes; others exposed only publication dates or summaries.
- Several official product claims are vendor-provided and should be independently validated before production use.
- Some high-star GitHub repos may have promotional momentum; security and license review is required before installing agent plugins/MCP servers.
