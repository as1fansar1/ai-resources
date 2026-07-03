# Top AI tools and workflows — last 30 days

Research date: 2026-07-03 08:38:16 EDT  
Window: 2026-06-03 to 2026-07-03  
Scope: AI tools and practical workflows relevant to coding agents/devtools, agent infrastructure, browser/computer-use agents, research/knowledge, design/media/content, business automation, open/local models, workspace agents, sales/GTM, and privacy/security.

## Executive summary

The last 30 days were dominated by four themes:

1. **Agents moved from single-chat tools to operating systems for work.** Claude Sonnet 5, Claude Tag, Notion External Agents, Perplexity Brain/Computer, and Runway Agent 2 all point toward persistent agents that sit inside Slack, docs, legal/research workflows, or creative pipelines.
2. **Coding-agent ecosystems are professionalizing.** Browser Use CLI 3.0, Vercel `skills`, Google `agents-cli`, Hugging Face Serge, vLLM Jobs, and cost/approval patterns from Simon Willison all show the same direction: reusable skills, review gates, browser control, cost telemetry, and safer sandboxes.
3. **Browser automation is becoming a first-class agent capability.** Browser Use, Microsoft Webwright, agent-browser, Cloudflare Worker demos, `shot-scraper video`, and Playwright-heavy debugging workflows make browser/computer-use agents a practical layer rather than a novelty.
4. **Media and design agents are shifting from generation to editable workflows.** Adobe Firefly AI Assistant, Runway Agent 2, Runway Aleph in Figma Weave, and Claude Code model-porting workflows emphasize iterative editing, campaign context, and reusable assets.

Bottom line for Asif: **try Browser Use CLI 3.0, Vercel Skills, Claude Code/Sonnet workflows with explicit plan-review-test loops, and Notion/Perplexity workspace-agent patterns. Monitor Claude Tag and Perplexity Brain until access/governance becomes clearer.**

## Scoring methodology

100-point rubric, computed as: recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance 10. Deductions were applied for single-source virality, unclear access, weak recent signal, immature repos, or high-permission workflows without a strong security story.

## Top ranked tools/workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | Claude Sonnet 5 + Claude Code / Claude Tag / Claude Science workflows | 98 | Try now / monitor access |
| 2 | Browser Use CLI 3.0 for browser-enabled coding agents | 96 | Try now |
| 3 | Claude Tag as a Slack-native async teammate | 91 | Monitor / pilot if available |
| 4 | OpenAI GPT-5.6 preview + ChatGPT Dreaming memory | 91 | Monitor / test if access granted |
| 5 | Vercel `skills` + reusable agent skill libraries | 90 | Try now |
| 6 | Agent loop engineering: plan → research → build → review → test | 89 | Try now |
| 7 | Perplexity Brain / Computer for research and legal workflows | 87 | Monitor / pilot carefully |
| 8 | Notion External Agents + AI Meeting Notes speaker labels | 87 | Try now if in Notion workspace |
| 9 | Adobe Firefly AI Assistant + upgraded creative studio | 84 | Try for creative teams |
| 10 | OmniRoute AI gateway / model-routing endpoint | 83 | Monitor / evaluate locally |
| 11 | Hugging Face Serge AI code review | 82 | Try now in low-risk repos |
| 12 | Runway Agent 2 + Aleph 2.0 in Figma Weave | 81 | Try for media/content workflows |
| 13 | Browser automation QA/media pipeline: Webwright, Playwright, shot-scraper | 81 | Try now for demos/QA |
| 14 | Hugging Face vLLM Jobs + `hf` CLI agent mode | 80 | Try for evals/local-model tests |
| 15 | Herdr / Orca multi-agent desktop and terminal orchestration | 79 | Monitor / try if running many agents |

## Detailed findings

### 1. Claude Sonnet 5 + Claude Code / Claude Tag / Claude Science workflows

Score: 98  
Category: Coding agents, workspace agents, scientific workbench  
Recommendation: Try now where available; monitor beta products.

Why it matters: Anthropic’s June launches make Claude less like a chatbot and more like a work substrate: stronger default model, coding-agent usage, Slack async tasks, and scientific compute workflows.

Evidence:
- Claude Sonnet 5 announcement, 2026-06-30: https://www.anthropic.com/news/claude-sonnet-5
- Claude Tag beta, 2026-06-23: https://www.anthropic.com/news/introducing-claude-tag
- Claude Science workbench beta, 2026-06-30: https://www.anthropic.com/news/claude-science-ai-workbench
- Latent Space coverage of Claude Tag, 2026-06-24: https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive

Practical workflow: Use Claude Code/Sonnet for repo tasks; define `plan.md`; delegate implementation; require review/test steps; for team tasks, tag Claude in Slack with scoped context; for scientific tasks, use the workbench to run analyses and produce auditable artifacts.

Best next step: Standardize a Claude Code project template with plan/review/test instructions, repo-specific rules, and an explicit approval policy for side effects.

### 2. Browser Use CLI 3.0 for browser-enabled coding agents

Score: 96  
Category: Browser/computer-use agents  
Recommendation: Try now.

Why it matters: Browser Use remains one of the clearest bridges between coding agents and real web apps. Its CLI direction makes it easier to give agents browser capability without custom Playwright glue.

Evidence:
- GitHub repo: https://github.com/browser-use/browser-use
- Release activity reported inside the window, including Browser Use CLI 3.0 around 2026-07-01 and repo push activity through 2026-07-02.

Practical workflow: Install Browser Use/CLI, connect to Claude Code/Codex/Cursor, and let the coding agent verify UI flows, inspect web apps, extract structured data, or automate repetitive browser tasks.

Best next step: Use it on one low-risk internal workflow: login-free website QA, screenshot comparison, or extraction from public pages.

### 3. Claude Tag as a Slack-native async teammate

Score: 91  
Category: Productivity/workspace agents  
Recommendation: Monitor; pilot only with tight permissions.

Why it matters: Slack is where work actually gets delegated. Claude Tag turns an agent into an addressable teammate that can follow threads, remember context, and run long tasks.

Evidence:
- Anthropic announcement, 2026-06-23: https://www.anthropic.com/news/introducing-claude-tag
- Latent Space summary, 2026-06-24: https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive

Practical workflow: In a project channel, tag Claude for bounded tasks: summarize decisions, chase metrics, draft PR notes, investigate support issues, or prepare a doc. Use channel-specific access and require human approval before external actions.

Best next step: Prepare a Slack-agent governance checklist: allowed channels, allowed tools, escalation rules, and audit logging.

### 4. OpenAI GPT-5.6 preview + ChatGPT Dreaming memory

Score: 91  
Category: Frontier models, memory, productivity  
Recommendation: Monitor; test if access is granted.

Why it matters: OpenAI’s recent signals emphasize both stronger models and more persistent memory. The practical implication is better long-running assistant behavior and more capable API/Codex workflows.

Evidence:
- GPT-5.6 Sol/Terra/Luna preview, 2026-06-26: https://openai.com/index/previewing-gpt-5-6-sol/
- ChatGPT Dreaming memory, 2026-06-04: https://openai.com/index/chatgpt-memory-dreaming/

Practical workflow: Use memory for ongoing personal/project context; use preview models for coding-agent benchmarking, eval tasks, and agent planning once API/Codex access is available.

Best next step: Keep a small benchmark suite for Asif’s recurring tasks so new model previews can be evaluated on real workflows rather than demos.

### 5. Vercel `skills` + reusable agent skill libraries

Score: 90  
Category: Agent infrastructure, coding agents  
Recommendation: Try now.

Why it matters: Skills are becoming the package manager for agents: portable instructions, checklists, scripts, and tool conventions that can be shared across Claude Code, Codex, Cursor, OpenCode, and other agents.

Evidence:
- Vercel `skills`: https://github.com/vercel-labs/skills
- Vercel `agent-skills`: https://github.com/vercel-labs/agent-skills
- GitHub Trending/search activity in late June and early July 2026.

Practical workflow: Install skills for React, Next.js, deployment, design review, or repo-specific conventions; require agents to load the relevant skill before performing specialized tasks.

Best next step: Create a small private skill pack for Asif’s preferred coding/research/reporting workflows.

### 6. Agent loop engineering: plan → research → build → review → test

Score: 89  
Category: Agent workflow design  
Recommendation: Try now.

Why it matters: The most reliable agent gains are not from a single product; they come from better loops. The pattern is to make the agent plan, gather context, implement, review independently, test, and only then summarize.

Evidence:
- Ben’s Bites, “designing the loop,” 2026-06-09: https://www.bensbites.com/p/hey-siri-meet-ai
- Simon Willison’s June Datasette Agent posts showing approval, edit, cost, and browser-debugging loops: https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/ and https://simonwillison.net/2026/Jun/9/agentsview-custom-model-price/

Practical workflow: For every significant agent task, create `plan.md`; split into research/build/review/test; use a separate reviewer model/agent where possible; require command output or artifact verification before finalizing.

Best next step: Make this the default monthly recurring workflow for research and code tasks.

### 7. Perplexity Brain / Computer for research and legal workflows

Score: 87  
Category: Research/knowledge workflows  
Recommendation: Monitor; pilot carefully for non-critical research.

Why it matters: Perplexity is pushing toward self-improving, memory-backed research agents and domain-specific computer workflows, especially legal research.

Evidence:
- Perplexity Brain, 2026-06-18: https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents
- Computer for Counsel, 2026-06-24: https://www.perplexity.ai/hub/blog/introducing-computer-for-counsel

Practical workflow: Connect sources, build a context graph, let the agent improve recurring workflows overnight, and use it for research briefs or legal-document workflows with human review.

Best next step: Use it for a repeatable research brief, not for final legal/financial conclusions.

### 8. Notion External Agents + AI Meeting Notes speaker labels

Score: 87  
Category: Productivity/workspace agents  
Recommendation: Try now if Asif’s workspace is in Notion.

Why it matters: Notion is turning docs into an agent hub. External Agents starting with Claude and Cursor plus better meeting notes make workspace automation more concrete.

Evidence:
- Notion 3.6 release, 2026-07-01: https://www.notion.com/releases/2026-07-01

Practical workflow: Use Notion as the shared memory and task surface; connect Claude/Cursor for doc-to-code or ticket-to-code workflows; use speaker-labelled meeting notes to assign follow-ups.

Best next step: Pilot one Notion database where meeting notes automatically create tasks and link to agent follow-up prompts.

### 9. Adobe Firefly AI Assistant + upgraded creative studio

Score: 84  
Category: Design/media/content  
Recommendation: Try for creative/content teams.

Why it matters: Adobe’s direction is agentic creative operations across existing professional tools rather than standalone image generation.

Evidence:
- Adobe Firefly update, 2026-06-18: https://blog.adobe.com/en/publish/2026/06/18/adobe-firefly-introduces-new-agentic-capabilities-and-an-upgraded-creative-ai-studio-built-for-the-way-you-work

Practical workflow: Use Firefly Assistant inside Premiere, Photoshop, Illustrator, InDesign, or Frame.io to ideate, generate, edit, and maintain campaign style/context across assets.

Best next step: Test on one campaign concept with brand-review checkpoints.

### 10. OmniRoute AI gateway / model-routing endpoint

Score: 83  
Category: Agent infrastructure, model routing  
Recommendation: Monitor; evaluate locally before trusting production.

Why it matters: Agents increasingly need routing across models, providers, MCP tools, and fallback paths. OmniRoute packages that into a local endpoint for Claude Code, Codex, Cursor, Cline, and Copilot-style tools.

Evidence:
- GitHub repo: https://github.com/diegosouzapw/OmniRoute
- GitHub Trending/search activity around 2026-06-30 to 2026-07-01.

Practical workflow: Point coding agents at a single OpenAI/Anthropic-compatible endpoint; route planning, coding, cheap exploration, and fallback calls to different providers.

Best next step: Evaluate on non-sensitive tasks; inspect provider credentials, logs, compression behavior, and MCP permissions.

### 11. Hugging Face Serge AI code review

Score: 82  
Category: Coding agents/devtools  
Recommendation: Try now in low-risk repos.

Why it matters: Serge is an open-source, GitHub-native code-review agent that can use OpenAI-compatible endpoints including local/Hugging Face-routed models.

Evidence:
- HF blog, 2026-06-12: https://huggingface.co/blog/huggingface/serge
- GitHub repo: https://github.com/huggingface/serge

Practical workflow: Add `.ai/review-rules.md`, wire Serge via GitHub Action/App/web app, and have it review PRs before human approval.

Best next step: Enable it on a sandbox repo and compare its review comments against a human checklist.

### 12. Runway Agent 2 + Aleph 2.0 in Figma Weave

Score: 81  
Category: Design/media/content  
Recommendation: Try for content workflows.

Why it matters: Runway is moving from clip generation to campaign-aware creative agents and editable video/design workflows.

Evidence:
- Runway Agent 2, 2026-06-25: https://runwayml.com/news/introducing-agent-2
- Aleph 2 in Figma Weave, 2026-06-22: https://runwayml.com/news/aleph-2-in-figma-weave

Practical workflow: Give Agent 2 campaign/product/audience context; generate/revise ad concepts; use Aleph/Figma Weave to restyle objects/scenes and propagate edits through video clips.

Best next step: Use it for first-draft variants, not final brand-approved creative.

### 13. Browser automation QA/media pipeline: Webwright, Playwright, shot-scraper

Score: 81  
Category: Browser/computer-use agents, QA, demos  
Recommendation: Try now.

Why it matters: A practical agent should not only edit code; it should run the app, inspect the browser, and produce evidence. The June workflow evidence strongly supports this pattern.

Evidence:
- Microsoft Webwright repo: https://github.com/microsoft/Webwright
- Simon Willison on browser debugging with Claude, 2026-06-11: https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/
- `shot-scraper video`, 2026-06-30: https://simonwillison.net/2026/Jun/30/shot-scraper-video/

Practical workflow: Agent starts dev server, writes Playwright/shot-scraper storyboard, records video proof, and attaches it to the task summary.

Best next step: Add a “record a 30-second proof video” step to UI-related coding-agent tasks.

### 14. Hugging Face vLLM Jobs + `hf` CLI agent mode

Score: 80  
Category: Open/local models, developer infrastructure  
Recommendation: Try for evals and temporary inference.

Why it matters: HF is making its Hub and compute more agent-friendly: parseable CLI outputs, jobs, and quick OpenAI-compatible endpoints for vLLM.

Evidence:
- HF CLI for agents, 2026-06-04: https://huggingface.co/blog/hf-cli-for-agents
- vLLM on HF Jobs, 2026-06-26: https://huggingface.co/blog/vllm-jobs

Practical workflow: Ask an agent to inspect models/datasets/spaces using `hf`; spin up temporary vLLM endpoints for evals or demos; tear them down after tests.

Best next step: Use HF Jobs for a small model-eval batch rather than production serving.

### 15. Herdr / Orca multi-agent desktop and terminal orchestration

Score: 79  
Category: Coding agents/devtools  
Recommendation: Monitor; try if running multiple agents daily.

Why it matters: Once engineers use Claude Code, Codex, OpenCode, Cursor, and specialized agents together, orchestration UX becomes a real bottleneck. Herdr and Orca attack that problem.

Evidence:
- Herdr repo: https://github.com/ogulcancelik/herdr
- Orca repo: https://github.com/stablyai/orca
- GitHub Trending/search activity in late June and early July 2026.

Practical workflow: Run multiple coding agents in panes/worktrees; monitor state; reattach from SSH/mobile; compare outputs or delegate subtasks to separate agents.

Best next step: Try on one repo with two parallel agents: one builder and one reviewer.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agents/devtools | Claude Sonnet 5 + Claude Code workflows | Strongest blend of capability, adoption, and practical utility. |
| Agent infrastructure | Vercel `skills` | Most actionable way to make agent behavior portable and repeatable. |
| Browser/computer-use agents | Browser Use CLI 3.0 | Best momentum and immediate utility for browser tasks. |
| Research/knowledge | Perplexity Brain / Computer | Strong direction for persistent research agents, but access is early. |
| Design/media/content | Adobe Firefly AI Assistant | Best fit for professional creative workflows across existing tools. |
| Business automation | Claude + n8n MCP workflow generation | Useful but needs careful credential and production validation. |
| Open/local models | HF vLLM Jobs + `hf` CLI agent mode | Practical, agent-friendly path for temporary inference and Hub operations. |
| Productivity/workspace agents | Notion External Agents | Strong workspace integration and immediate team use cases. |
| Privacy/security/governance | Simon Willison approval/sandbox/cost patterns | Most practical safety pattern: tool approvals, sandboxing, and spend visibility. |

## Rising but less proven

- **Weave Router** — smart model routing for coding agents; promising cost claims but source-available rather than fully open-source and still needs broad validation. https://github.com/workweave/router
- **Google `agents-cli`** — useful lifecycle CLI and skills for Google Cloud agent deployment; strongest if already invested in Google Cloud/ADK. https://github.com/google/agents-cli
- **agent-browser** — token-efficient browser MCP server with intent-first actions; novel but early/small. https://github.com/dondai1234/agent-browser
- **codemcp** — meta-MCP gateway that compresses tool calls through generated Python; clever but security/sandboxing needs scrutiny. https://github.com/skymoore/codemcp
- **Rutherford MCP Server / TeamMCP** — multi-agent collaboration/consensus through MCP; interesting for agent teams but early. https://github.com/chapmanjw/rutherford-mcp-server and https://github.com/cookjohn/teammcp
- **North Mini Code** — open coding model for agentic SWE; promising model release, but requires harness/inference and independent validation. https://huggingface.co/blog/CohereLabs/introducing-north-mini-code
- **Product Hunt launches: Handit.ai, fileAI, Optibot, HeronAI** — good discovery signals, but Product Hunt dates/metrics were partially snippet-based and require deeper due diligence.

## Overhyped / be careful

- **Autonomous Slack/workspace agents without governance.** Claude Tag and Notion External Agents are powerful, but channel permissions, auditability, and approval rules matter more than demos.
- **Model routers/gateways that handle all credentials.** OmniRoute-style tools can be useful, but they become a sensitive control plane. Inspect logs, credential storage, provider policies, and prompt-compression behavior.
- **Generated n8n/business automations.** Great for drafts; risky if credentials, payment actions, email sends, or CRM writes are enabled without review.
- **Creative AI outputs used as final brand/legal assets.** Adobe/Runway are excellent for iteration; final usage still needs brand, rights, and compliance review.
- **Single-source Product Hunt virality.** PH launches are useful for discovery but not enough to prove adoption.

## Try-this-week shortlist

1. **Install Browser Use CLI** and run a browser QA/extraction workflow on a low-risk site.
2. **Create a reusable agent skill pack** for Asif’s recurring research/reporting/coding workflows.
3. **Add a plan-review-test loop** to Claude Code/Codex tasks, including mandatory verification artifacts.
4. **Pilot Hugging Face Serge** on a sandbox GitHub repo with `.ai/review-rules.md`.
5. **Record proof videos for UI tasks** with Playwright or `shot-scraper video`.

## Best workflow to keep doing this monthly

Use a recurring “research agent swarm” pattern:

1. Split collection into developer/open-source, product launches, practitioner workflows, and newsletters/official blogs.
2. Require each track to return candidates with URLs, dates, momentum, and workflow utility.
3. Deduplicate by workflow, not by product name.
4. Score with the same 100-point rubric.
5. Publish the report to GitHub and append links in `Hermes Research/README.md`.
6. Maintain a small “try this week” backlog so the report drives action, not just awareness.

## Raw candidate appendix

Developer/open-source candidates reviewed: Browser Use CLI 3.0, Herdr, Orca, OmniRoute, Vercel `skills`, Google `agents-cli`, Weave Router, Adrafinil, agent-browser, codemcp, claude-code-codex-subagents, claude-codex-bridge, Rutherford MCP Server, TeamMCP, Microsoft Webwright, mlx-code, Hugging Face Serge, North Mini Code, HF CLI agent mode, Vercel agent-skills.

Product/commercial candidates reviewed: OpenAI GPT-5.6 preview, ChatGPT Dreaming memory, Claude Sonnet 5, Claude Tag, Claude Science, Google Ask Ad Manager, Google June Pixel Drop Gemini tools, Adobe Firefly AI Assistant, Perplexity Brain, Perplexity Computer for Counsel, Notion External Agents/AI Meeting Notes, Runway Agent 2, Runway Aleph 2 in Figma Weave, Hugging Face Serge, HF vLLM Jobs, HF Agentic Resource Discovery, Handit.ai, fileAI, Optibot, HeronAI.

Practitioner/workflow candidates reviewed: Claude + n8n MCP workflow generation, Claude Tag Slack workflows, Databricks Omnigent-style agent harness, Codex Plugins/Sites, agent loop engineering, nested Claude subagents, Datasette Agent sandbox/edit/approval patterns, AgentsView cost observability, Cloudflare WAF tuning with Claude Code, Datasette Apps, temporary Cloudflare Workers deployments, Claude Code model-porting to ONNX/WebGPU, MDN browser-compat SQLite data pipeline, `shot-scraper video`, AI coding-agent spend caps.

## Limitations

- GitHub Trending historical evidence was partly collected from search/trending digests rather than an official precise rolling-window API; treat it as directional momentum.
- Product Hunt pages were partially accessible via search snippets; some launch dates were relative (“launched this week”) and upvote/point counts were incomplete.
- Reddit, X/Twitter, and LinkedIn were not used as primary evidence because of likely access and authentication friction.
- Several 2026 launches are previews/betas with limited access; recommendations distinguish “try now” from “monitor.”
- Some metrics such as star counts and Product Hunt points are snapshots and may change quickly.
