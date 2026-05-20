# GitHub trending repositories and remix ideas — May 17, 2026

Research date: 2026-05-17 22:57:47 +08
Window: GitHub Trending daily/weekly/monthly accessed May 17, 2026; supplemental GitHub API metadata for stars, forks, created/pushed dates.
Scope: Popular GitHub repositories lately, with emphasis on weekly/monthly trending repos and practical remix ideas.

## Major themes

1. Agent infrastructure is dominant: memory, skills, GUI/computer-use agents, terminal agents, routers, and agent QA.
2. “Skills” are becoming the package format for agents: small reusable operating procedures for coding agents.
3. AI media automation is hot: self-hosted image/video generation, automated short-video engines, and HTML-to-video rendering.
4. Vertical agents are emerging: finance, trading, OSINT, scientific/research workflows.
5. Developer tools remain durable: Bun and Pyrefly show continued appetite for faster runtimes/type checking.

## Top repositories reviewed

| Rank | Repository | Stars | What it is |
|---:|---|---:|---|
| 1 | CloakHQ/CloakBrowser | 13,279 | Stealth Chromium / Playwright replacement for browser automation. |
| 2 | rohitg00/agentmemory | 10,936 | Persistent memory server for coding agents via MCP/hooks/REST. |
| 3 | yikart/AiToEarn | 14,531 | AI content monetization/publishing automation platform. |
| 4 | anthropics/financial-services | 24,168 | Claude financial-services reference agents, skills, and connectors. |
| 5 | oven-sh/bun | 91,624 | Fast all-in-one JavaScript runtime/toolkit. |
| 6 | mattpocock/skills | 88,195 | Practical engineering skills for coding agents. |
| 7 | ruvnet/RuView | 58,951 | WiFi-based spatial sensing/vital-sign monitoring system. |
| 8 | bytedance/UI-TARS-desktop | 34,341 | Multimodal desktop/browser/computer-use agent stack. |
| 9 | apernet/hysteria | 21,032 | Fast censorship-resistant QUIC proxy. |
| 10 | decolua/9router | 11,410 | AI coding gateway/router across many model providers. |
| 11 | HKUDS/AI-Trader | 17,733 | Agent-native automated trading platform. |
| 12 | millionco/react-doctor | 9,870 | React code quality checker for agent-written React. |
| 13 | Hmbown/DeepSeek-TUI | 31,058 | Terminal coding agent for DeepSeek models. |
| 14 | facebook/pyrefly | 6,076 | Fast Python type checker and language server. |
| 15 | obra/superpowers | 194,796 | Agentic software-development methodology using composable skills. |
| 16 | Alishahryar1/free-claude-code | 25,144 | Anthropic-compatible proxy for Claude Code using alternate/local models. |
| 17 | multica-ai/andrej-karpathy-skills | 133,544 | CLAUDE.md guidelines based on Karpathy’s coding-agent critiques. |
| 18 | Fincept-Corporation/FinceptTerminal | 21,349 | Open finance/market analytics terminal. |
| 19 | AIDC-AI/Pixelle-Video | 17,695 | Fully automated AI short-video engine. |
| 20 | heygen-com/hyperframes | 18,899 | HTML-to-video rendering framework built for agents. |
| 21 | ComposioHQ/awesome-codex-skills | 10,184 | Curated Codex skills list. |
| 22 | soxoj/maigret | 29,097 | OSINT username search/dossier tool. |

## Detailed summaries

- **CloakBrowser**: browser automation infrastructure focused on passing bot/fingerprint checks; relevant to AI web agents and scraping, but risky/abuse-prone.
- **agentmemory**: shared long-term memory layer for coding agents; solves repeated context setup and cross-agent recall.
- **AiToEarn**: all-in-one AI content creation, distribution, and monetization workflow for creators/solo companies.
- **Anthropic financial-services**: domain-specific reference implementation for analyst workflows with human review.
- **Bun**: mature fast JS runtime/bundler/test runner; trending due broad developer utility, not just AI.
- **mattpocock/skills**: field-tested coding-agent skills; trend confirms skills are the new agent plugin layer.
- **RuView**: privacy-preserving sensing using WiFi signals; ambitious hardware/software edge-AI project.
- **UI-TARS Desktop**: open multimodal agent stack for GUI, browser, and desktop operation.
- **Hysteria**: proxy/networking tool; useful infra, but not AI-specific.
- **9router**: LLM gateway for coding tools, routing Claude/Codex/Cursor/etc. to many providers.
- **AI-Trader / FinceptTerminal**: finance is becoming a strong vertical for agent workflows.
- **react-doctor / pyrefly**: quality gates around agent-written code are gaining momentum.
- **DeepSeek-TUI / free-claude-code**: demand for terminal agents powered by cheaper/local/alternate models.
- **Pixelle-Video / hyperframes / Open-Generative-AI**: agent-ready video generation and rendering pipelines.
- **Maigret / Shadowbroker**: OSINT aggregation plus agent analysis is trending; strong ethical/privacy caveats.

## Remix ideas

1. **Agent App Store for Skills + Memory**
   - Combine agentmemory + mattpocock/skills + superpowers + awesome-codex-skills.
   - Product: install, version, rate, audit, and share agent skills across Claude Code, Codex, Cursor, Hermes.
   - Differentiator: every skill stores success/failure telemetry in memory and improves over time.

2. **AI QA Firewall for Agent-Written Frontends**
   - Combine react-doctor + UI-TARS + browser automation.
   - Product: before an agent commits UI code, it opens the app, checks React anti-patterns, runs visual flows, and files a fix plan.
   - Target: teams using coding agents for React/Next.js.

3. **Personal Research Analyst OS**
   - Combine agentmemory + financial-services-style vertical agents + Pyrefly/Bun quality gates.
   - Product: a private analyst agent that remembers sources, builds models, cites prior work, and exports memos.
   - Start with finance, then clone for legal, healthcare ops, or market research.

4. **Agent-Native Content Factory**
   - Combine AiToEarn + Pixelle-Video + hyperframes + Open-Generative-AI.
   - Product: one prompt becomes a script, visual plan, generated clips, HTML motion graphics, subtitles, and scheduled posts.
   - Safer angle: brand-approved templates and review queue instead of spam automation.

5. **Local/Low-Cost Coding Agent Router with Governance**
   - Combine 9router + free-claude-code + DeepSeek-TUI + agentmemory.
   - Product: route tasks to cheap/local models, remember what worked, enforce spend limits, and escalate hard tasks to premium models.
   - Useful for solo devs and small teams with token-budget pain.

6. **OSINT-to-Briefing Agent**
   - Combine Maigret/Shadowbroker concepts + agentmemory + human-review workflows.
   - Product: ingest public signals, dedupe, score confidence, produce citation-backed briefings.
   - Important: position for journalists/security researchers with privacy and legality guardrails.

7. **Agent-Readable CLI Wrappers for Everything**
   - Inspired by CLI-Anything + UI-TARS.
   - Product: convert GUI/web apps into predictable CLI/MCP interfaces so agents stop clicking around blindly.
   - Monetization: hosted connectors for business apps.

8. **Compliance-First Vertical Agent Templates**
   - Inspired by Anthropic financial-services.
   - Product: reference agents for regulated workflows: audit trails, citations, human approval, red-team checklists.
   - Verticals: finance, insurance, tax, procurement, medical admin.

## Try-now shortlist

- For your own agent workflow: **agentmemory**, **mattpocock/skills**, **superpowers**, **react-doctor**.
- For product ideas: **agent-native skill registry**, **frontend QA firewall**, **agent content factory**.
- For monitoring only: **CloakBrowser**, **OSINT aggregation tools**, **AI trading agents** due abuse/compliance risks.

## Limitations

- GitHub Trending is directional, not a precise rolling-window API.
- Stars/forks were fetched via GitHub API at research time and can change quickly.
- Some repositories have inflated-looking star counts or sensitive use cases; popularity does not imply quality or safety.
