# Top GitHub AI repositories — rolling 30-day window

Research date: 2026-06-03 16:31:33 CEST
Window: 2026-05-04 to 2026-06-03
Scope: GitHub repositories related to AI tools, AI agents, workflows, LLM apps, local AI, MCP, coding agents, evaluation/observability, RAG, inference, multimodal generation, and automation. Strategic lens: local-first/local-owned BYOK creator tools.

## Executive summary

The month’s highest GitHub momentum clustered around: (1) coding agents becoming infrastructure; (2) local inference and self-hosted AI UX; (3) MCP as the agent-tool control plane; (4) ComfyUI-centered creator workflows; and (5) observability, memory, routing, and context layers becoming mandatory for serious agentic products.

Most actionable stack for Asif this month: **Ollama + llama.cpp + Open WebUI/AnythingLLM + ComfyUI + Codex/opencode/Goose + Langfuse/TensorZero + narrowly scoped MCP servers**.

## Scoring methodology

100-point rubric: recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance to local-owned/BYOK creator tools 10. Deductions were applied for single-source hype, weak in-window evidence, excessive permissions, demo-only status, unclear workflow, or weak security story.

## Top ranked tools/workflows

| Rank | Repository / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | [openai/codex](https://github.com/openai/codex) | 97 | Try now |
| 2 | [ollama/ollama](https://github.com/ollama/ollama) | 96 | Try now |
| 3 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 96 | Try now |
| 4 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 96 | Try now |
| 5 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 94 | Try now |
| 6 | [langgenius/dify](https://github.com/langgenius/dify) | 92 | Try now |
| 7 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 91 | Try now |
| 8 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 90 | Try now |
| 9 | [cline/cline](https://github.com/cline/cline) | 88 | Try now |
| 10 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 88 | Try now |
| 11 | [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 88 | Try now |
| 12 | [mudler/LocalAI](https://github.com/mudler/LocalAI) | 88 | Try now |
| 13 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | 87 | Monitor / controlled trial |
| 14 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 85 | Try if GPU serving matters |
| 15 | [github/github-mcp-server](https://github.com/github/github-mcp-server) | 84 | Try with strict scopes |
| 16 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | 84 | Prototype |
| 17 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 83 | Try for autonomous dev tasks |
| 18 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | 83 | Try now |
| 19 | [langfuse/langfuse](https://github.com/langfuse/langfuse) | 81 | Try for eval/observability |
| 20 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | 80 | Prototype |

## Detailed findings

### 1. openai/codex
Score: 97  
Category: coding agent / terminal workflow  
Recommendation: Try now  
Repo: https://github.com/openai/codex

Why it matters: one of the highest-signal OSS coding-agent repos this month; useful reference for terminal agent UX, sandboxing, MCP/tool integration, remote execution, and multi-agent coding patterns.

Evidence: pushed 2026-06-03; `rust-v0.136.0` released 2026-06-01 (https://github.com/openai/codex/releases/tag/rust-v0.136.0); May v0.132-v0.136 release series; research found v0.136 compare with 108 commits / 33 contributors.

Momentum: ~88k stars, ~13k forks; very high issue/release velocity.

Workflow/use case: local repo + terminal coding agent + scoped tools + git checkpoints + optional MCP servers for issue-to-patch workflows.

Risks: OpenAI ecosystem dependency, rapid churn, tool/shell permissions require sandboxing and secrets hygiene.

Best next step: benchmark against opencode, Goose, Aider, and Cline on the same local repo task.

### 2. ollama/ollama
Score: 96  
Category: local AI runtime / model serving  
Recommendation: Try now  
Repo: https://github.com/ollama/ollama

Why it matters: default local model runner for many self-hosted stacks; highly relevant for local-first/BYOK products.

Evidence: pushed 2026-06-03; v0.30.2 prerelease 2026-06-03; v0.30.0 RC line 2026-05-13; architecture/news reference: https://aiforautomation.io/news/2026-05-14-ollama-v030-llamacpp-native-rewrite

Momentum: ~173k stars, ~16.4k forks; broad downstream use by Open WebUI, AnythingLLM, Dify-style workflows, local coding agents, and RAG apps.

Workflow/use case: install Ollama, pull local models, connect Open WebUI/AnythingLLM/Dify/coding agents to a local endpoint, route private work locally and optionally use BYOK cloud fallback.

Risks: local performance varies by hardware; RC churn; model licenses and hardware compatibility must be checked.

Best next step: standardize a baseline local stack: Ollama + Open WebUI + one coding agent + one RAG app.

### 3. ggml-org/llama.cpp
Score: 96  
Category: core local inference runtime  
Recommendation: Try now  
Repo: https://github.com/ggml-org/llama.cpp

Why it matters: foundational GGUF/local inference substrate for desktop apps and local model runners.

Evidence: releases through 2026-06-03 including b9491/b9490/b9489; ~478 commits since 2026-05-04; releases: https://github.com/ggml-org/llama.cpp/releases

Momentum: ~114k stars, ~19k forks; daily release cadence and wide ecosystem adoption.

Workflow/use case: use directly for local model experiments, embed in desktop/local apps, or treat as low-level substrate behind Ollama/LocalAI.

Risks: fast-moving low-level runtime; backend/model compatibility varies.

Best next step: track changes affecting Apple Silicon, GGUF, Ollama, and LocalAI.

### 4. Comfy-Org/ComfyUI
Score: 96  
Category: local multimodal creator pipeline  
Recommendation: Try now  
Repo: https://github.com/Comfy-Org/ComfyUI

Why it matters: strongest open local-owned creator substrate; graph workflows are becoming the practical standard for image/video/audio generation pipelines.

Evidence: v0.21.0 released 2026-05-11 (https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.21.0); v0.22.0 released 2026-05-20 (https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.22.0); blueprint update 2026-05-25 (https://github.com/Comfy-Org/ComfyUI/commit/04879a8113961cbc4e2ff20e9feeb737ba703f51); multi-GPU coverage: https://www.creativeainews.com/articles/comfyui-native-multi-gpu-work-units-2026/

Momentum: ~115k stars; active releases; strong LTX/Wan/Hunyuan/upscale/inpaint/custom-node ecosystem.

Workflow/use case: build repeatable local graphs for text-to-image, image-to-video, video inpaint/upscale, audio-video generation, and exportable workflow templates.

Risks: GPU/VRAM complexity; custom-node supply-chain risk; model-weight licenses vary.

Best next step: create a reusable local creator pack: ComfyUI + LTXVideo + LTX Director + Stable Audio 3 + preset workflows.

### 5. open-webui/open-webui
Score: 94  
Category: self-hosted AI interface / local AI cockpit  
Recommendation: Try now  
Repo: https://github.com/open-webui/open-webui

Why it matters: high-adoption self-hosted AI UX layer with chat, knowledge bases, tools, MCP, sync integrations, and local/cloud model routing.

Evidence: v0.9.6 released 2026-06-01 (https://github.com/open-webui/open-webui/releases/tag/v0.9.6); changelog: https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md; pushed 2026-06-02; ~395 commits since 2026-05-04.

Momentum: ~140k stars, ~20k forks.

Workflow/use case: run with Ollama/LocalAI/vLLM, connect knowledge bases and tools, and use as a front-end for local-owned personal/team AI.

Risks: broad permissions and feature surface; connector/RAG privacy risks; self-host upgrades need care.

Best next step: use as the default local AI front-end in an Ollama + AnythingLLM + RAGFlow comparison.

### 6. langgenius/dify
Score: 92  
Category: agentic workflow/app platform  
Recommendation: Try now  
Repo: https://github.com/langgenius/dify

Evidence: v1.14.1 on 2026-05-12 and v1.14.2 on 2026-05-19 (https://github.com/langgenius/dify/releases/tag/1.14.2); pushed 2026-06-03; ~480 commits since 2026-05-04; ~144k stars, ~22.6k forks.

Workflow/use case: low-code self-hosted AI apps combining RAG, tools, providers, forms, and workflow logic.

Risks: heavier platform; migrations/deployment complexity; not as purely local-first as Ollama/Open WebUI.

Best next step: build one BYOK creator workflow and compare with n8n + Open WebUI + scripts.

### 7. anomalyco/opencode
Score: 91  
Category: open coding agent  
Recommendation: Try now  
Repo: https://github.com/anomalyco/opencode

Evidence: release v1.15.13 on 2026-05-30; pushed 2026-06-03; ~169k stars, ~20k forks reported during research.

Workflow/use case: local/open alternative or complement to Codex/Claude Code with BYOK model providers and agent sessions.

Risks: org/name migration; large issue count; governance/license should be reviewed.

Best next step: run the same patching task in opencode, Codex, Goose, and Aider.

### 8. browser-use/browser-use
Score: 90  
Category: browser automation agent framework  
Recommendation: Try now  
Repo: https://github.com/browser-use/browser-use

Evidence: release 0.12.9 on 2026-05-26 (https://github.com/browser-use/browser-use/releases/tag/0.12.9); pushed 2026-06-01; ~96.7k stars, ~10.8k forks.

Workflow/use case: Python + Playwright browser agents with custom tools for research, QA, and repetitive web tasks.

Risks: captchas, anti-bot systems, site ToS, cookies/session leakage.

Best next step: prototype a local browser-agent workflow with artifacts/screenshots for auditability.

### 9. cline/cline
Score: 88  
Category: IDE/coding agent  
Recommendation: Try now  
Repo: https://github.com/cline/cline

Evidence: v3.86.2 on 2026-06-01; pushed 2026-06-03; ~62.7k stars, ~6.6k forks.

Workflow/use case: editor/CLI plan-edit-test loops with tool use and MCP context.

Risks: extension attack surface; permission prompts and tool execution need review.

Best next step: test on a narrow repo task with MCP/context integrations.

### 10. infiniflow/ragflow
Score: 88  
Category: RAG / document intelligence  
Recommendation: Try now  
Repo: https://github.com/infiniflow/ragflow

Evidence: v0.25.5 on 2026-05-20 and v0.25.6 on 2026-05-27; pushed 2026-06-03; ~529 commits since 2026-05-04; ~82k stars.

Workflow/use case: ingest PDFs/docs, parse/index them, and expose retrieval to local/self-hosted assistants.

Risks: large issue count; retrieval quality depends on ingestion/parsing/vector config.

Best next step: compare against AnythingLLM and Open WebUI KB on the same corpus.

### 11. Mintplex-Labs/anything-llm
Score: 88  
Category: local-first RAG/agent app  
Recommendation: Try now  
Repo: https://github.com/Mintplex-Labs/anything-llm

Evidence: v1.13.0 released 2026-05-26 (https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.13.0), adding hybrid model router, scheduled jobs, and memories; pushed 2026-06-03; ~61k stars.

Workflow/use case: local workspaces with docs, Ollama/cloud routing, memory, and scheduled tasks.

Risks: hybrid routing can leak data if rules are misconfigured.

Best next step: evaluate as a private personal AI workspace next to Open WebUI.

### 12. mudler/LocalAI
Score: 88  
Category: OpenAI-compatible local AI engine  
Recommendation: Try now  
Repo: https://github.com/mudler/LocalAI

Evidence: v4.3.0 on 2026-05-24, v4.3.5 on 2026-05-29; pushed 2026-06-03; ~46k-47k stars.

Workflow/use case: local OpenAI-compatible endpoint for text, vision, voice, image/video, and multi-backend apps.

Risks: many backends increase complexity; CPU-only performance can disappoint.

Best next step: compare against Ollama for multimodal creator workflows.

### 13. mem0ai/mem0
Score: 87  
Category: agent memory  
Recommendation: Monitor / controlled trial  
Repo: https://github.com/mem0ai/mem0

Evidence: Python SDK v2.0.4 on 2026-05-27, Node SDK v3.0.5 on 2026-05-27, opencode plugin v0.1.1 on 2026-05-28; pushed 2026-06-02; ~57k-58k stars.

Workflow/use case: durable user/project memory for agents.

Risks: memory privacy, provenance, deletion, poisoning, and hosted/local defaults need review.

Best next step: test local-only memory with export/delete controls.

### 14. vllm-project/vllm
Score: 85  
Category: high-throughput LLM serving  
Recommendation: Try if GPU serving matters  
Repo: https://github.com/vllm-project/vllm

Evidence: v0.20.1 on 2026-05-04, v0.20.2 on 2026-05-10, v0.21.0 on 2026-05-15; ~82k stars.

Workflow/use case: serve open models on private GPUs via OpenAI-compatible API and route through Dify/TensorZero/Langfuse.

Risks: GPU/Kubernetes complexity; tuning required.

Best next step: use when Ollama/LocalAI is too slow and GPU infra is available.

### 15. github/github-mcp-server
Score: 84  
Category: MCP / repo automation  
Recommendation: Try with strict scopes  
Repo: https://github.com/github/github-mcp-server

Evidence: v1.1.0 on 2026-05-28 and v1.1.2 on 2026-05-29; pushed 2026-06-03; The New Stack security scanning coverage 2026-05-07: https://thenewstack.io/github-mcp-security-scanning/

Workflow/use case: let agents inspect/manage issues, PRs, Actions, and repository state via MCP.

Risks: high-privilege token surface; prompt injection from issues/files; use least privilege.

Best next step: start read-only, then selectively enable write operations.

### 16. microsoft/Webwright
Score: 84  
Category: terminal-native web agent / reusable Playwright automation  
Recommendation: Prototype  
Repo: https://github.com/microsoft/Webwright

Evidence: public release 2026-05-04; Codex/Claude Code plugin manifests 2026-05-06; Task2UI mode 2026-05-11; external coverage 2026-05-25 (https://www.microsoft.com/en-us/research/articles/webwright-a-terminal-is-all-you-need-for-web-agents/ and https://winbuzzer.com/2026/05/25/microsoft-webwright-turns-web-agents-into-reusable-code-xcxwbn/).

Workflow/use case: agent writes/runs Playwright scripts and preserves reusable code, logs, and screenshots.

Risks: new project; web automation remains brittle; model-quality dependent.

Best next step: prototype one repeatable browser QA/research task.

### 17. OpenHands/OpenHands
Score: 83  
Category: autonomous software-development agent  
Recommendation: Try for autonomous dev tasks  
Repo: https://github.com/OpenHands/OpenHands

Evidence: pushed 2026-06-03; ~75.7k stars and ~9.6k forks.

Workflow/use case: assign coding tasks to an autonomous dev environment with sandboxed execution and repo operations.

Risks: heavier infrastructure; less lightweight/local-first than CLI agents.

Best next step: use as an autonomous-task benchmark.

### 18. aaif-goose/goose
Score: 83  
Category: extensible agent  
Recommendation: Try now  
Repo: https://github.com/aaif-goose/goose

Evidence: v1.36.0 on 2026-05-27; pushed 2026-06-03; ~46.3k stars.

Workflow/use case: install/execute/edit/test with an LLM agent connected to local tools and MCP servers.

Risks: tool permission model and governance move need review.

Best next step: test as open local-agent layer for repetitive dev/sysadmin tasks.

### 19. langfuse/langfuse
Score: 81  
Category: LLM observability/evals  
Recommendation: Try for eval/observability  
Repo: https://github.com/langfuse/langfuse

Evidence: v3.173.0 on 2026-05-08, v3.175.0 on 2026-05-21, v3.176.0 on 2026-05-28; pushed 2026-06-03; ~28k stars.

Workflow/use case: trace prompts, datasets, evals, latency, cost, and feedback in local/cloud hybrid apps.

Risks: observability stores sensitive prompts/docs; retention and redaction policy required.

Best next step: instrument one useful prototype before adding more automation.

### 20. zilliztech/claude-context
Score: 80  
Category: agent context / semantic code retrieval MCP  
Recommendation: Prototype  
Repo: https://github.com/zilliztech/claude-context

Evidence: pushed 2026-05-22; PRs on May 4/6/11; May trend article: https://www.askglitch.com/blog/top-5-trending-ai-github-repos-may-2026; ~11.7k stars.

Workflow/use case: index codebase and expose semantic retrieval to coding agents via MCP to reduce token waste.

Risks: vector DB setup; embedding privacy; retrieval quality must be tested.

Best next step: compare coding-agent performance with and without claude-context.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agent | openai/codex | Highest combined recency, adoption, and release velocity. |
| Local AI runtime | ollama/ollama | Best user-facing local runtime for BYOK/local-first stacks. |
| Core inference substrate | ggml-org/llama.cpp | Foundational local inference engine and GGUF ecosystem driver. |
| Local creator workflow | Comfy-Org/ComfyUI | Strongest open graph/pipeline substrate for image/video/audio workflows. |
| Self-hosted AI interface | open-webui/open-webui | Best local AI cockpit and knowledge/tool interface. |
| Workflow app platform | langgenius/dify | Strongest low-code app/RAG/agent workflow platform. |
| Browser automation | browser-use/browser-use | Highest adoption browser-agent framework. |
| RAG/document intelligence | infiniflow/ragflow | Strongest self-hosted document RAG signal this month. |
| Agent memory | mem0ai/mem0 | Fastest visible ecosystem integration across SDKs/plugins. |
| Observability/evals | langfuse/langfuse | Best practical open tracing/eval layer. |
| MCP repo automation | github/github-mcp-server | Official high-impact MCP server; must be scoped carefully. |
| Agent context retrieval | zilliztech/claude-context | High relevance to coding-agent quality. |

## Rising but less proven

- [mozilla-ai/cq](https://github.com/mozilla-ai/cq) — local SQLite MCP memory / “Stack Overflow for agents”; blog 2026-05-21 and HN signal; risks: poisoning/stale memory.
- [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) — LTX Director timeline for local video; v1.3.5 on 2026-05-19; GPL/single-maintainer risk.
- [Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) — LTX 2.3 local video workflows; heavy VRAM/model-license caveats.
- [prasenjeet-symon/ogcode](https://github.com/prasenjeet-symon/ogcode) — one-binary zero-cloud browser-native coding workbench; very early.
- [xintaofei/codeg](https://github.com/xintaofei/codeg) — multi-agent workspace aggregating Codex, Claude Code, Gemini CLI, OpenCode; complex security surface.
- [jonwiggins/optio](https://github.com/jonwiggins/optio) — ticket-to-PR Kubernetes coding-agent orchestration; operational/auto-merge risk.
- [bytedance/Bernini](https://github.com/bytedance/Bernini) — new video generation/editing framework; early research, multi-GPU/licensing validation needed.
- [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) — local computer-use agent with GUI/TUI; strong permission/sandboxing needs.
- [frane/vibesurfer](https://github.com/frane/vibesurfer) — lightweight browser daemon/MCP for local agents; tiny adoption.

## Overhyped / be careful

- **High-privilege MCP servers:** prompt injection can become real side effects; start read-only, pin versions, isolate credentials.
- **Single-source trending repos:** blog-only virality is a lead, not proof.
- **Auto-merge autonomous coding:** require branch protection, CI gates, and human review.
- **Browser/computer-use agents:** isolate browser profiles and avoid private sessions unless strictly needed.
- **Voice cloning/audio generation:** legal/consent/model-license risks.
- **ComfyUI custom-node sprawl:** pin versions and isolate environments.
- **Cloud-routed “local-first” apps:** verify routing rules and connector behavior before trusting privacy claims.

## Try-this-week shortlist

1. Ollama + Open WebUI + a llama.cpp/GGUF model baseline.
2. ComfyUI + ComfyUI-LTXVideo + LTX Director for one local video workflow.
3. Codex vs opencode vs Goose vs Aider on the same repo task.
4. RAGFlow vs AnythingLLM vs Open WebUI KB on the same document corpus.
5. Langfuse or TensorZero instrumentation for one prototype.
6. GitHub MCP Server in read-only mode.
7. Browser-use or Webwright for one auditable browser automation.

## Best workflow to keep doing this monthly

Pull GitHub search/API data for repos created or pushed in the last 30 days across `ai-agent`, `llm`, `mcp`, `rag`, `local-ai`, `inference`, `comfyui`, `coding-agent`, `evals`, `observability`, and `browser-agent`; merge with GitHub Trending, release feeds, HN Algolia/Show HN, Hugging Face/web references, and official blogs; dedupe repos/products; score with this rubric; separate try-now, rising-but-unproven, and overhyped; add a local-owned/BYOK creator-fit filter.

## Raw candidate appendix

| Candidate | Category | Window signal summary |
|---|---|---|
| openai/codex | Coding agent | Pushed 2026-06-03; rust-v0.136.0 release 2026-06-01; ~88k stars. |
| ollama/ollama | Local runtime | Pushed 2026-06-03; v0.30 prereleases in May/June; ~173k stars. |
| ggml-org/llama.cpp | Inference runtime | Daily releases through 2026-06-03; ~478 commits since 2026-05-04. |
| Comfy-Org/ComfyUI | Creator pipeline | v0.21.0 2026-05-11; v0.22.0 2026-05-20; blueprint updates 2026-05-25. |
| open-webui/open-webui | AI UX / KB | v0.9.6 2026-06-01; ~395 commits since 2026-05-04. |
| langgenius/dify | Workflow/app platform | v1.14.1 2026-05-12; v1.14.2 2026-05-19. |
| anomalyco/opencode | Coding agent | v1.15.13 2026-05-30; pushed 2026-06-03. |
| browser-use/browser-use | Browser agents | 0.12.9 2026-05-26; pushed 2026-06-01. |
| cline/cline | IDE/coding agent | v3.86.2 2026-06-01; pushed 2026-06-03. |
| infiniflow/ragflow | RAG | v0.25.5 2026-05-20; v0.25.6 2026-05-27. |
| Mintplex-Labs/anything-llm | Local-first app/RAG | v1.13.0 2026-05-26 with model router, scheduled jobs, memory. |
| mudler/LocalAI | Local API | v4.3.0 2026-05-24; v4.3.5 2026-05-29. |
| mem0ai/mem0 | Agent memory | SDK/plugin releases 2026-05-20 to 2026-05-28. |
| vllm-project/vllm | GPU serving | v0.20.1 2026-05-04; v0.20.2 2026-05-10; v0.21.0 2026-05-15. |
| github/github-mcp-server | MCP repo automation | v1.1.0 2026-05-28; v1.1.2 2026-05-29. |
| microsoft/Webwright | Browser/web agents | Public release 2026-05-04; Microsoft coverage 2026-05-25. |
| OpenHands/OpenHands | Autonomous dev agent | Pushed 2026-06-03; ~75k stars. |
| aaif-goose/goose | Extensible agent | v1.36.0 2026-05-27; pushed 2026-06-03. |
| langfuse/langfuse | Observability/evals | v3.173, v3.175, v3.176 releases in May. |
| zilliztech/claude-context | Context MCP | Pushed 2026-05-22; May PRs and trend-blog reference. |
| modelcontextprotocol/servers | MCP servers | Pushed 2026-05-30; canonical MCP server collection. |
| Aider-AI/aider | Coding agent | Pushed 2026-05-22. |
| continuedev/continue | AI devtool/checks | Pushed 2026-06-02. |
| RooCodeInc/Roo-Code | Multi-agent editor | v3.54.0 2026-05-15. |
| mozilla-ai/cq | Agent memory/MCP | Blog 2026-05-21; release cli/v0.10.0 2026-05-20. |
| idosal/git-mcp | GitHub docs MCP | Pushed 2026-05-08; HN Show HN reference. |
| WhatDreamsCost/WhatDreamsCost-ComfyUI | ComfyUI video workflow | v1.3.5 2026-05-19; tutorial/external coverage. |
| Lightricks/ComfyUI-LTXVideo | Video generation nodes | Last push 2026-05-11; LTX 2.3 workflows. |
| AIDC-AI/Pixelle-Video | Automated short video | May trend-blog/HF ecosystem signal. |
| microsoft/agent-framework | Agent framework | Python 1.6.0 2026-05-22; 1.7.0 2026-05-28. |
| tensorzero/tensorzero | Gateway/evals | 2026.5.0 release 2026-05-08. |
| sgl-project/sglang | LLM/VLM serving | v0.5.11 2026-05-05; v0.5.12 2026-05-16; v0.5.12.post1 2026-05-26. |
| kvcache-ai/Mooncake | KV cache/serving | v0.3.11 2026-05-21; pushed 2026-06-03. |
| gpustack/gpustack | GPU cluster manager | Pushed 2026-06-03; prerelease activity around 2026-05-30. |
| dyad-sh/dyad | Local AI app builder | Pushed 2026-06-03; release just before window 2026-04-29. |
| Fosowl/agenticSeek | Local autonomous agent | Pushed 2026-05-17; May external coverage. |
| PaddlePaddle/PaddleOCR | OCR/RAG ingestion | Pushed 2026-06-03. |
| containers/ramalama | Container-native serving | Pushed 2026-06-01. |
| bytedance/Bernini | Video generation/editing | Created 2026-05-29; inference/weights announced 2026-06-01. |
| Stability-AI/stable-audio-3 | Audio generation | Pushed 2026-05-29. |
| lsdefine/GenericAgent | Computer-use agent | v0.1.0 2026-05-15; GUI/TUI updates in May. |

## Limitations

- GitHub unauthenticated API rate limits were hit, so several stars/forks/issue counts are approximate and sourced from accessible GitHub snippets or web-indexed pages.
- GitHub Trending monthly is directional, not a precise rolling-window API.
- Reddit/X/LinkedIn were not relied on because scheduled jobs often lack authenticated access and bot friction is high.
- Product Hunt pages may be Cloudflare-protected; this report prioritized GitHub, releases, HN, Hugging Face/web-search-visible sources, and official blogs.
- Some external references predate the exact window but were used only as supporting validation when the repo also had in-window GitHub activity.
- Scores are comparative and practical, not absolute quality guarantees. Security, license, model-weight terms, and deployment complexity need repo-by-repo review before commercial use.
