# Top AI tools and workflows — last 30 days

Research date: 2026-04-26 WITA  
Window: 2026-03-27 to 2026-04-26  
Scope: AI tools, agents, developer workflows, business/productivity workflows, open-source projects, model/tooling infrastructure, and creator workflows.

## Executive summary

The strongest trend is not “one more chatbot.” It is the packaging of AI into reusable, agentic workflows: skills, workspace agents, browser agents, coding agents, scheduled automations, memory systems, and tool-connected assistants.

Top themes:

1. **Coding agents are becoming operating systems.** Codex and Claude Code are expanding into skills, plugins, memory, MCP, browser/computer use, automations, and multi-agent workflows.
2. **Team/workspace agents are moving from demos to business workflows.** OpenAI Workspace Agents, Notion/Claude-style agents, and Slack/Perplexity-style work agents point toward shared agents embedded in company processes.
3. **Browser/computer-use agents are heating up.** Chrome AI Mode, Chrome skills, Chrome DevTools MCP, Browser Harness, Stagehand, and Perplexity Computer all indicate that “AI using the web/app for you” is a major category.
4. **Agent memory/context is a major bottleneck and opportunity.** claude-mem, MemPalace, LLM wikis, skills, and long-context models all address the same pain: keeping agents useful across sessions and large codebases.
5. **Design/image/video AI is now mainstream workflow tooling.** Claude Design, Canva AI, ChatGPT Images 2.0, Gemini image features, Google Vids/Veo, Runway, Sora, and ElevenLabs are increasingly practical content pipelines.
6. **Open/local models remain strategically important.** DeepSeek, Qwen, Gemma, GGUF packaging, Ollama/OpenRouter-style routing, and edge AI tooling are enabling lower-cost and local/private agent stacks.
7. **Automation stacks are converging.** n8n, Clay, Apollo, Lemlist, HubSpot, NotebookLM, Perplexity, ChatGPT, Claude, and coding agents are being wired together as practical business workflows.

## Scoring methodology

100-point score:

- Recency: 15
- Momentum: 20
- Source diversity: 15
- Practical utility: 20
- Workflow novelty: 10
- Adoption evidence: 10
- Strategic relevance: 10

Scores are directional, based on available evidence from official launches, GitHub/Hugging Face/HN signals, Product Hunt feed, newsletters/blogs, and YouTube/practitioner content. Some sources were blocked by bot protection, especially Product Hunt pages, Reddit, X/Twitter, LinkedIn, TLDR AI, and general search pages.

## Top 15 ranked tools/workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | Codex superapp / automations / skills | 95 | Try now |
| 2 | Claude Code + MCP + skills + memory workflows | 95 | Try now |
| 3 | Workspace/team agents in ChatGPT | 89 | Try now / monitor |
| 4 | Open/local model stack: DeepSeek, Qwen, Gemma, GGUF | 89 | Monitor + selectively test |
| 5 | Agent memory/context systems: claude-mem, MemPalace, LLM wiki | 89 | Try now for coding/research |
| 6 | Browser agents + Chrome/DevTools MCP | 87 | Try now if browser automation matters |
| 7 | AI design assistants: Claude Design + Canva | 86 | Try now for design/prototyping |
| 8 | Next-gen image generation/editing: ChatGPT Images 2.0 + Gemini | 84 | Try now for visual content |
| 9 | Business automation: n8n + agents | 83 | Try now for ops workflows |
| 10 | Research workflows: Gemini Deep Research, Perplexity + NotebookLM | 83 | Try now |
| 11 | Agent SDK/runtime/sandbox/observability | 83 | Monitor / use for production agents |
| 12 | Video/audio generation pipelines: Sora, Runway, ElevenLabs, Veo | 78 | Try for content production |
| 13 | Multimodal document intelligence: Markitdown, embeddings, PDFs | 77 | Try if doing RAG/docs |
| 14 | Privacy/security controls for agent workflows | 76 | Monitor; important for teams |
| 15 | Sales/GTM automation: Apollo + Clay + Claude + Lemlist + HubSpot | 75 | Try if doing outbound/GTM |

## 1. Codex superapp / automations / skills

Score: 95  
Category: coding agent, desktop/cloud agent, workflow automation  
Recommendation: **Try now**

Why it matters:

Codex is being positioned less like a narrow code assistant and more like a general work agent: coding, computer use, browsing, automations, schedules, plugins, and skills.

Evidence:

- OpenAI: “Codex for almost everything” — https://openai.com/index/codex-for-almost-everything
- OpenAI Academy: “What is Codex?” — https://openai.com/academy/what-is-codex
- OpenAI Academy: “Codex automations” — https://openai.com/academy/codex-automations
- OpenAI Academy: “Codex plugins and skills” — https://openai.com/academy/codex-plugins-and-skills
- Latent Space: “GPT 5.5 and OpenAI Codex Superapp” — https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp

Practical workflow:

- Use Codex for repo tasks, reviews, debugging, refactors, scheduled checks, recurring summaries, and app/browser tasks.
- Package repeated actions as skills/plugins.
- Use scheduled automations for weekly reports, monitoring, QA, or research collection.

Best next step:

Test a simple recurring Codex/Hermes workflow: “Every Friday, summarize the top changes in my main project and suggest next actions.”

## 2. Claude Code + MCP + skills + memory workflows

Score: 95  
Category: AI coding, project automation, agentic development  
Recommendation: **Try now**

Why it matters:

Claude Code remains one of the strongest practical agentic coding workflows. The momentum is around surrounding it with MCP servers, skills, hooks, memory, project instructions, and multi-agent handoffs.

Evidence:

- YouTube: Tech With Tim, “FULL Claude Code Tutorial for Beginners in 2026” — https://www.youtube.com/watch?v=qYqIhX9hTQk
- YouTube: Michele Torti, Claude Code masterclass — https://www.youtube.com/watch?v=fQgJ7qXlyDE
- YouTube: Chase AI, Claude Code skills/plugins stack — https://www.youtube.com/watch?v=KjEFy5wjFQg
- GitHub: claude-mem — https://github.com/thedotmack/claude-mem
- Simon Willison on recent Claude Code quality/pricing/context reports — https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/

Practical workflow:

- Put project conventions in `CLAUDE.md` / skill files.
- Add MCP for GitHub, browser/devtools, docs, databases, or cloud tools.
- Use memory/context plugins for multi-day coding continuity.
- Split work across specialized subagents: planner, implementer, reviewer, tester.

Best next step:

Set up one repo with a clean Claude/Codex-compatible workflow: project instructions, coding standards, test commands, review checklist, and memory file.

## 3. Workspace/team agents in ChatGPT

Score: 89  
Category: team productivity, business agents  
Recommendation: **Try now / monitor**

Why it matters:

This is the clearest move toward shared internal agents that can live inside a business workspace, connect tools, and automate recurring team work.

Evidence:

- OpenAI: “Introducing workspace agents in ChatGPT” — https://openai.com/index/introducing-workspace-agents-in-chatgpt/
- OpenAI Academy: Workspace agents — https://openai.com/academy/workspace-agents
- YouTube: Rob The AI Guy on 24/7 ChatGPT agents — https://www.youtube.com/watch?v=rTjgoy1W_i4
- YouTube: Corey McClain on ChatGPT Agent Builder productivity agents — https://www.youtube.com/watch?v=iPAnsMTZckw

Practical workflows:

- Weekly team report agent
- Lead qualification agent
- Product-feedback triage agent
- Vendor-risk research agent
- IT/request review agent

Best next step:

Create one workspace agent with a narrow scope: “review inbound leads and prepare a daily qualification summary.”

## 4. Open/local model stack: DeepSeek, Qwen, Gemma, GGUF

Score: 89  
Category: open models, local AI, agent backends  
Recommendation: **Monitor + selectively test**

Why it matters:

Open/local models are becoming viable backends for agents, long-context workflows, private data processing, edge devices, and cost-sensitive automation.

Evidence:

- Hugging Face: DeepSeek-V4 — https://huggingface.co/blog/deepseekv4
- Latent Space: DeepSeek V4 — https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and
- Simon Willison: DeepSeek V4 — https://simonwillison.net/2026/Apr/24/deepseek-v4/
- Simon Willison: Qwen3.6-27B — https://simonwillison.net/2026/Apr/22/qwen36-27b/
- Hugging Face: Gemma 4 — https://huggingface.co/blog/gemma4
- Hugging Face: Unsloth Qwen GGUF model signal — https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF

Practical workflow:

- Use hosted frontier models for hard reasoning.
- Use local/open models for privacy, batch classification, summarization, draft generation, and tool-calling experiments.
- Route by task using OpenRouter/Ollama/LLM gateway style tools.

Best next step:

Benchmark one local/open model against your actual tasks: summarization, coding review, browser-research extraction, and structured JSON output.

## 5. Agent memory/context systems

Score: 89  
Category: agent infrastructure, coding/research continuity  
Recommendation: **Try now for coding/research**

Why it matters:

Almost every serious agent workflow hits the same wall: context resets, huge repos, repeated instructions, and lost decisions. Memory systems and LLM-maintained wikis are a direct answer.

Evidence:

- GitHub: claude-mem — https://github.com/thedotmack/claude-mem
- GitHub: MemPalace — https://github.com/MemPalace/mempalace
- HN: “Karpathy-style LLM wiki your agents maintain” — https://news.ycombinator.com/item?id=47899844
- GitHub: microsoft/markitdown as ingestion layer — https://github.com/microsoft/markitdown

Practical workflow:

- Capture session summaries automatically.
- Store stable facts in project memory.
- Maintain an LLM wiki in Markdown/Git.
- Use retrieval to inject only relevant past context.

Best next step:

Create a project `docs/ai-memory/` or `llm-wiki/` with: architecture, decisions, commands, glossary, active issues, and testing notes.

## 6. Browser agents + Chrome/DevTools MCP

Score: 87  
Category: browser automation, computer-use agents, MCP  
Recommendation: **Try now if browser automation matters**

Why it matters:

The browser is where most real-world work happens. Browser agents are moving from demos to practical SDKs and harnesses, especially when paired with MCP and devtools access.

Evidence:

- Chrome DevTools MCP — https://github.com/ChromeDevTools/chrome-devtools-mcp
- Browser Harness — https://github.com/browser-use/browser-harness
- HN: Browser Harness Show HN — https://news.ycombinator.com/item?id=47890841
- Browserbase Stagehand — https://github.com/browserbase/stagehand
- Google: AI Mode in Chrome — https://blog.google/products-and-platforms/products/search/ai-mode-chrome/
- Google: Skills in Chrome — https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/
- Hugging Face: HoloTab AI browser companion — https://huggingface.co/blog/Hcompany/holotab

Practical workflow:

- Give agents browser/devtools access for QA, form-filling, scraping, monitoring, and debugging.
- Use browser automation for repeatable research tasks and web-app testing.

Best next step:

Try Chrome DevTools MCP or Stagehand on one web QA task: “open app, reproduce bug, inspect console/network, propose fix.”

## 7. AI design assistants: Claude Design + Canva

Score: 86  
Category: design, prototyping, marketing  
Recommendation: **Try now**

Why it matters:

Design assistants are moving from “generate a pretty image” to “collaborate on usable design artifacts”: slides, one-pagers, landing pages, prototypes, brand assets, and Canva-editable outputs.

Evidence:

- Anthropic: Claude Design — https://www.anthropic.com/news/claude-design-anthropic-labs
- Canva + Claude Design — https://www.canva.com/newsroom/news/canva-claude-design/
- Canva AI 2.0 — https://www.canva.com/newsroom/news/canva-create-2026-ai/
- Ben’s Bites: Claude design coverage — https://www.bensbites.com/p/thats-my-designer-claude

Practical workflow:

- Ask AI to draft a landing page, product one-pager, slide deck, or brand concept.
- Export/edit in Canva.
- Use human review for brand polish.

Best next step:

Use Claude Design/Canva for one concrete asset: “landing page for an AI workflow report service.”

## 8. Next-gen image generation/editing

Score: 84  
Category: image generation, marketing creative  
Recommendation: **Try now for visual content**

Why it matters:

Image generation is becoming more useful for production work: better text rendering, editing, personalized imagery, and integration into chat/design workflows.

Evidence:

- OpenAI: ChatGPT Images 2.0 — https://openai.com/index/introducing-chatgpt-images-2-0/
- Simon Willison: GPT image testing — https://simonwillison.net/2026/Apr/21/gpt-image-2/
- Google Gemini personalized images — https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence-nano-banana/
- Ben’s Bites image coverage — https://www.bensbites.com/p/chatgpts-nano-banana

Practical workflow:

- Generate campaign mockups.
- Create social thumbnails.
- Iterate brand variants.
- Generate diagrams/visual explanations.

Best next step:

Make a reusable prompt template for product screenshots, thumbnails, and launch graphics.

## 9. Business automation: n8n + agents

Score: 83  
Category: automation, operations, agencies  
Recommendation: **Try now for ops workflows**

Why it matters:

n8n remains a practical bridge between AI models and business systems. The trend is toward agentic automations that combine LLMs, CRMs, Slack/email, databases, and human approvals.

Evidence:

- n8n IDE/workflow video — https://www.youtube.com/watch?v=YqWCBW1VrBc
- Nate Herk business AI workflows — https://www.youtube.com/watch?v=Y3PcRp5RFzk

Practical workflow:

- Intake → classify → enrich → draft response → human approve → update CRM/database → send report.

Best next step:

Build one n8n workflow for inbound leads or research monitoring.

## 10. Research workflows: Gemini Deep Research, Perplexity + NotebookLM

Score: 83  
Category: research, knowledge work  
Recommendation: **Try now**

Why it matters:

Research workflows are becoming multi-tool loops: web research, source collection, NotebookLM/source-grounded synthesis, Claude/ChatGPT analysis, and final report generation.

Evidence:

- Google Gemini Deep Research Max — https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/
- OpenAI Academy: ChatGPT for research — https://openai.com/academy/research
- Perplexity + NotebookLM practitioner workflow — https://www.youtube.com/watch?v=9gISKHTF0co
- NotebookLM agency workflow — https://www.youtube.com/watch?v=inWMKofp5Y0

Practical workflow:

- Perplexity/Gemini finds sources.
- NotebookLM grounds synthesis in uploaded sources.
- Claude/ChatGPT structures the final report.
- Store reusable notes in a wiki or memory layer.

Best next step:

Use this exact report as a seed for a recurring AI-trends research loop.

## Category winners

### Coding agents and devtools

1. Codex superapp / automations / skills
2. Claude Code + MCP + memory
3. Qwen Code / open-source terminal coding agents
4. Chrome DevTools MCP
5. Archon / deterministic AI coding harnesses

### Agent infrastructure

1. Agent memory/context systems
2. Agent SDK/runtime/sandbox/observability
3. Browser agents / computer-use harnesses
4. LLM gateways and routing
5. Privacy/redaction/sandbox controls

### Research and knowledge workflows

1. Gemini Deep Research
2. Perplexity + NotebookLM
3. Agent-maintained LLM wiki
4. Markitdown/document-to-Markdown ingestion
5. Multimodal document embeddings/rerankers

### Design/media/content

1. Claude Design + Canva
2. ChatGPT Images 2.0
3. Gemini image personalization
4. Google Vids / Veo
5. Sora + ElevenLabs + Runway style pipelines

### Business operations

1. Workspace/team agents
2. n8n + agents
3. Perplexity Computer in Slack
4. Sales/GTM automation with Apollo/Clay/Claude/Lemlist/HubSpot
5. Function-specific copilots for operations, sales, marketing, finance, healthcare

## Rising but less proven

- Browser Harness — strong recent HN/GitHub signal, but still early.
- MemPalace — huge claimed GitHub momentum, but needs hands-on verification.
- Clawdi / BAND / “home for all agents” style Product Hunt launches — interesting category but unclear adoption.
- Emotional intelligence AI for live calls — useful sales niche, but needs trust/privacy scrutiny.
- LifeOS / personal-introduction agents — novel, but unclear durability.

## Overhyped / be careful

- Generic “AI agent platform” launches without clear integrations or real workflows.
- Products that require broad email/drive/browser permissions but do not explain security boundaries.
- Viral demos that only work on toy examples.
- Long-context model claims without cost/latency/retrieval benchmarks.
- AI video/content pipelines that generate low-quality commodity content at scale.

## Try-this-week shortlist

1. **Set up a coding-agent workflow** with Claude Code or Codex: project instructions, skills, memory, test commands, review checklist.
2. **Build one recurring research agent**: collect AI tool launches weekly, dedupe candidates, output Telegram digest.
3. **Try browser automation** with Chrome DevTools MCP or Stagehand on a real QA/research task.
4. **Create a small LLM wiki** for one active project so agents have durable context.
5. **Prototype one business automation** in n8n: inbound lead triage, research monitoring, or content pipeline.

## Best workflow to keep doing this monthly

Recommended recurring process:

1. Gather candidates from:
   - GitHub Trending monthly
   - Hugging Face trending
   - HN Show HN / AI posts
   - Product Hunt AI feed
   - OpenAI/Anthropic/Google/Meta/HF blogs
   - Latent Space, Ben’s Bites, Rundown AI, Simon Willison
   - YouTube practitioner searches
2. Normalize names and merge duplicates.
3. Require at least one recent signal and preferably two independent sources.
4. Score using the 100-point rubric.
5. Produce:
   - Top 10 overall
   - Top 3 per category
   - Try/monitor/ignore recommendations
   - Source appendix
6. Deliver to Telegram monthly.

## Raw candidate appendix

Selected raw candidates collected during research:

- NousResearch/hermes-agent — https://github.com/NousResearch/hermes-agent
- forrestchang/andrej-karpathy-skills — https://github.com/forrestchang/andrej-karpathy-skills
- thedotmack/claude-mem — https://github.com/thedotmack/claude-mem
- microsoft/markitdown — https://github.com/microsoft/markitdown
- rtk-ai/rtk — https://github.com/rtk-ai/rtk
- shareAI-lab/learn-claude-code — https://github.com/shareAI-lab/learn-claude-code
- microsoft/VibeVoice — https://github.com/microsoft/VibeVoice
- ChromeDevTools/chrome-devtools-mcp — https://github.com/ChromeDevTools/chrome-devtools-mcp
- coleam00/Archon — https://github.com/coleam00/Archon
- browser-use/browser-harness — https://github.com/browser-use/browser-harness
- h4ckf0r0day/obscura — https://github.com/h4ckf0r0day/obscura
- MemPalace/mempalace — https://github.com/MemPalace/mempalace
- JackChen-me/open-multi-agent — https://github.com/JackChen-me/open-multi-agent
- QwenLM/qwen-code — https://github.com/QwenLM/qwen-code
- google-ai-edge/gallery — https://github.com/google-ai-edge/gallery
- google-ai-edge/LiteRT-LM — https://github.com/google-ai-edge/LiteRT-LM
- lsdefine/GenericAgent — https://github.com/lsdefine/GenericAgent
- TencentCloud/CubeSandbox — https://github.com/TencentCloud/CubeSandbox
- diegosouzapw/OmniRoute — https://github.com/diegosouzapw/OmniRoute
- graykode/abtop — https://github.com/graykode/abtop
- browserbase/stagehand — https://github.com/browserbase/stagehand
- OpenAI GPT-5.5 — https://openai.com/index/introducing-gpt-5-5/
- OpenAI Workspace Agents — https://openai.com/index/introducing-workspace-agents-in-chatgpt/
- ChatGPT Images 2.0 — https://openai.com/index/introducing-chatgpt-images-2-0/
- OpenAI WebSockets in Responses API — https://openai.com/index/speeding-up-agentic-workflows-with-websockets/
- Claude Opus 4.7 — https://www.anthropic.com/news/claude-opus-4-7
- Claude Design — https://www.anthropic.com/news/claude-design-anthropic-labs
- Canva AI 2.0 — https://www.canva.com/newsroom/news/canva-create-2026-ai/
- Gemini Embedding 2 — https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2-generally-available/
- Gemini Deep Research Max — https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/
- Perplexity Computer in Slack — https://www.perplexity.ai/hub/hub/blog/computer-in-slack-from-shared-context-to-finished-work
- Adobe CX Enterprise Coworker — https://news.adobe.com/news/2026/04/adobe-unveils-cx-enterprise-coworker
- Notion custom agents / AI Autofill — https://www.notion.com/releases
- Runway Fund / Builders — https://runwayml.com/news/news/introducing-runway-fund
- Product Hunt: Inrō AI — https://www.producthunt.com/products/inro
- Product Hunt: Architecto — https://www.producthunt.com/products/architecto
- Product Hunt: Genspark for Excel — https://www.producthunt.com/products/genspark-for-excel
- Product Hunt: BAND — https://www.producthunt.com/products/band
- Product Hunt: Bansi AI — https://www.producthunt.com/products/bansi

## Limitations

- Reddit, X/Twitter, LinkedIn, TLDR AI, and some Product Hunt pages were blocked or partially inaccessible from the research environment.
- Product Hunt upvote counts were not available because web pages were Cloudflare-blocked; the Atom feed was used for launch discovery.
- GitHub Trending monthly is not a precise rolling 30-day API, but it is a useful momentum signal when accessed on the research date.
- Some GitHub star counts reported by source pages should be treated as directional until independently verified.
