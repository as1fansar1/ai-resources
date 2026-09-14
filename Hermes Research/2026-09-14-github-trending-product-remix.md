# GitHub trending repos + product remixes — last 7 days

**Research date:** 2026-09-14 12:01:04 EDT  
**Rolling window:** 2026-09-07 12:01 EDT through 2026-09-14 12:01 EDT  
**Scope:** GitHub repositories across AI and non-AI categories, ranked for current momentum, practical utility, and remix potential. Strategic preference: local-first/local-owned creator and AI products with explicit BYOK cloud integrations.

## Executive summary

This week produced five strong themes:

1. **Agent skills are becoming executable product infrastructure.** [Archify](https://github.com/tt-a1i/archify) led the captured weekly board with **24,227 stars this week**; [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) added **7,370**; [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) added **5,425**. The winning unit is increasingly a portable, testable workflow rather than another chat surface.
2. **Creator stacks are splitting into owned local production plus deliberate cloud escalation.** [VoiceStudio](https://github.com/debpalash/VoiceStudio) keeps voice, dubbing, transcription, and project assets local; [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) supports Ollama/Lemonade plus many BYOK providers; the image-prompt library supplies reusable visual protocols. This is unusually aligned with Asif's product thesis.
3. **Open-source vertical workbenches are attacking high-ARPU SaaS categories.** [OpenSEO](https://github.com/every-app/open-seo) is not merely a dashboard clone: it pairs self-hosting with a DataForSEO BYOK model and agent-facing MCP/skills. That pattern can transfer to research, media, forecasting, and operations.
4. **Local inference is becoming a swappable endpoint, not a separate hobby app.** [Magnitude](https://github.com/magnitudedev/magnitude) profiles hardware, recommends models, and plugs a local endpoint into existing agent harnesses. [FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi) attacks the opposite side—many user-owned cloud keys behind one endpoint. A hybrid policy router is the obvious remix.
5. **Non-AI projects still carry important primitives.** [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) combines public spatial data on a local browser globe; [Omarchy](https://github.com/omacom/omarchy) packages an opinionated owned workstation; the new [dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) repo shows intense demand for extending existing hardware, though its binary/proprietary-component boundary makes it a poor product foundation.

**Best near-term bet:** **Owned Explainer Studio**, combining OpenMAIC, VoiceStudio, Archify, and optional BYOK image generation into an editable project-folder workflow.  
**Best infrastructure bet:** **Model Boundary Desk**, combining Magnitude, FreeLLMAPI, tokentab, and tracecrate into a local routing, cost, and disclosure layer.  
**Best vertical bet:** **Evidence Course Lab**, combining Scientific Agent Skills, OpenMAIC, and Archify to turn evidence packs into cited, interactive learning artifacts.

## Method and scoring

### Evidence collected

- [GitHub Trending — this week](https://github.com/trending?since=weekly) and [today](https://github.com/trending?since=daily), captured September 14.
- Authenticated GitHub REST snapshots for repository totals, creation/push dates, releases, forks, issues, topics, and detected licenses.
- GitHub repository search for projects created during September 7–14 and for high-star projects pushed during the window.
- Official repository READMEs and release pages, including setup, security, provider, and license notes.
- Hacker News via the public Algolia API. A bounded scan of the newest 1,000 stories in the exact window found 89 GitHub-linked stories. Notable corroboration included [frank-386](https://news.ycombinator.com/item?id=49693613) at **163 points / 45 comments**, [OpenArch](https://news.ycombinator.com/item?id=49693384) at **117 / 28**, and [Kinesis](https://news.ycombinator.com/item?id=49695408) at **90 / 27** at capture time.

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

Scores were summed programmatically. Lower component scores serve as penalties for single-surface attention, no distinct release, unclear licensing, old projects merely resurfacing, demo-only scope, weak operational detail, or poor local-owned/BYOK fit. The scores are decision aids, not objective quality measurements.

### Reading the momentum numbers

- **“Stars this week/today”** comes from the rendered GitHub Trending page and is the best available directional growth signal.
- **Total stars/forks** come from an authenticated GitHub API snapshot taken immediately after the Trending capture.
- GitHub's rendered Trending totals and REST totals sometimes differed materially, likely because the surfaces refresh/index on different schedules. This report does **not** subtract one total from another or treat the difference as growth.
- GitHub does not expose an official historical star-count API. For search-only repos, a current total is not claimed as an exact seven-day gain.

## Top ranked repositories

| Rank | Repository | Score | In-window signal | Recommendation |
|---:|---|---:|---|---|
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | **95** | +24,227 weekly; pushed Sep 14 | **Try now / build around** |
| 2 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | **93** | +7,370 weekly; three releases Sep 10–11 | **Try now, pin versions** |
| 3 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **92** | +10,023 weekly; v1.0.2 Sep 13 | **Prototype a local/BYOK course** |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **90** | +3,902 weekly; v0.5.2 Sep 10 | **Try now; review AGPL/model terms** |
| 5 | [every-app/open-seo](https://github.com/every-app/open-seo) | **88** | +2,941 weekly; v0.1.8 Sep 12 | **Validate one BYOK workflow** |
| 6 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | **86** | +10,485 weekly; pushed Sep 14 | **Prototype; license check first** |
| 7 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | **85** | +3,122 weekly; pushed Sep 14 | **Use for learning/small-model experiments** |
| 8 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | **84** | +5,425 weekly; pushed Sep 11 | **Use as a pattern library, clear rights** |
| 9 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **84** | +3,194 weekly; v0.9.8–0.9.9 Sep 7–10 | **Monitor / personal experiments** |
| 10 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | **84** | +161 daily; five releases Sep 8–11 | **Try on one local machine** |
| 11 | [omacom/omarchy](https://github.com/omacom/omarchy) | **82** | +5,296 weekly; v4.0.3 Sep 8 | **Monitor / test on spare hardware** |
| 12 | [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) | **82** | Created Sep 8; 1,882 stars; formal artifacts | **Deep-dive, not an MVP base** |

## Detailed findings

### 1. Archify

- **Repository:** [tt-a1i/archify](https://github.com/tt-a1i/archify)
- **Category:** Agent skill / architecture-as-code / creator-developer tooling
- **Score:** **95** = 15 recency + 20 momentum + 12 source diversity + 19 utility + 10 novelty + 9 adoption + 10 strategic fit
- **Why it is trending:** GitHub displayed **24,227 stars this week**, by far the strongest weekly signal in the captured board.
- **Recent evidence:** Authenticated snapshot: **61,876 stars / 4,084 forks / 168 open issues**; pushed **September 14**. The latest tagged release, v2.16.0, predates the exact window (August 30), so the in-window evidence is Trending velocity and continued commits rather than a release event.
- **Core primitive:** Agents create typed JSON intermediate representations; Archify deterministically validates and compiles them into a portable HTML/SVG system map.
- **What you can do:** Generate architecture, workflow, sequence, data-flow, and lifecycle diagrams in Cursor, Claude Code, Codex, or OpenCode; validate source; trace routes/reach; export PNG/SVG or motion formats; keep one self-contained HTML artifact under version control.
- **Maturity/license:** MIT; public since April 2026. The README documents validators, examples, and multiple agent hosts. An optional fixed-manifest update check can be disabled. Diagram correctness still depends on the source facts supplied to the agent.
- **Verdict:** This week's strongest reusable primitive. It is more valuable as an explainability/evidence layer embedded in vertical workflows than as a standalone diagram clone.

### 2. Scientific Agent Skills

- **Repository:** [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- **Category:** Scientific workflows / agent skills
- **Score:** **93** = 15 + 18 + 12 + 20 + 9 + 9 + 10
- **Why it is trending:** GitHub displayed **7,370 stars this week**, and the project shipped [v2.67.0](https://github.com/K-Dense-AI/scientific-agent-skills/releases/tag/v2.67.0), [v2.68.0](https://github.com/K-Dense-AI/scientific-agent-skills/releases/tag/v2.68.0), and [v2.69.0](https://github.com/K-Dense-AI/scientific-agent-skills/releases/tag/v2.69.0) during September 10–11.
- **Recent evidence:** **44,895 stars / 4,069 forks / 10 open issues**; pushed September 14. The repo describes 165 validated skills and 100+ scientific databases.
- **Core primitive:** Portable, documented, test-backed skills for scientific packages, databases, evidence workflows, simulations, and communication.
- **What you can do:** Add literature retrieval, bioinformatics, chemistry, forecasting, statistical analysis, scientific figures, regulatory-evidence preparation, and other bounded workflows to a compatible agent. Pair with the separate K-Dense BYOK desktop app or any supported agent host.
- **Maturity/license:** Repository-level MIT, but the README explicitly warns that individual skills and wrapped data/package sources can have different licenses. Database skills need network access; package skills can work offline after installation. Pin tags/commits because release cadence is high.
- **Verdict:** A strong vertical capability catalog. Build a narrow evidence product around a few reviewed skills rather than installing the entire collection blindly.

### 3. OpenMAIC

- **Repository:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
- **Category:** Multi-agent education / interactive content studio
- **Score:** **92** = 15 + 19 + 11 + 19 + 10 + 9 + 9
- **Why it is trending:** GitHub displayed **10,023 stars this week**; [v1.0.2](https://github.com/THU-MAIC/OpenMAIC/releases/tag/v1.0.2) shipped September 13.
- **Recent evidence:** **36,749 stars / 5,811 forks / 266 open issues**; pushed September 14. The August v1 launch added a chat-first agent workbench, durable course sessions, session materials, and reusable skills; v1.0.2 provides a fresh in-window maintenance signal.
- **Core primitive:** A provider-neutral course generator/editor that turns topics and documents into slides, quizzes, simulations, project-based learning, narrated lessons, and multi-agent classroom interactions.
- **What you can do:** Self-host; upload documents/audio/video; use web search; generate and revise whole courses; export editable PPTX or interactive HTML; route stages across OpenAI, Anthropic, Gemini, Bedrock, DeepSeek, Ollama, Lemonade, and other providers.
- **Maturity/license:** MIT since v0.3.0; broad provider surface and a large issue count imply substantial integration complexity. Local Lemonade can supply LLM, image, TTS, and ASR without a key; many other capabilities require user-owned credentials and their providers' terms.
- **Verdict:** One of the best local/BYOK creator primitives this week. The wedge should be an owned course/project format and evidence quality—not “AI teachers” alone.

### 4. VoiceStudio

- **Repository:** [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- **Category:** Local voice, dubbing, transcription, and audiobook production
- **Score:** **90** = 15 + 17 + 11 + 20 + 9 + 8 + 10
- **Why it is trending:** GitHub displayed **3,902 stars this week** and [v0.5.2](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.2) shipped September 10.
- **Recent evidence:** **28,643 stars / 3,505 forks / 55 open issues**; pushed September 11.
- **Core primitive:** A local production engine and desktop UI spanning voice cloning/design, speech-to-speech, TTS, ASR, dubbing, diarization, dictation, batch queues, stories, and audiobooks.
- **What you can do:** Run on macOS, Windows, Linux, or Docker; keep voices/projects/settings/outputs on-device; access a local REST/SSE/WebSocket API, OpenAI-compatible audio API, or MCP server; opt into network-backed features explicitly.
- **Maturity/license:** Active beta. Application is AGPL-3.0; downloaded models retain upstream terms. Local workflows avoid accounts, API keys, subscriptions, and usage meters, but hardware support and model quality vary.
- **Verdict:** Excellent owned creator infrastructure. Validate voice-consent, model licenses, and distribution obligations before commercializing a derivative.

### 5. OpenSEO

- **Repository:** [every-app/open-seo](https://github.com/every-app/open-seo)
- **Category:** Self-hosted SEO / MCP-enabled vertical SaaS alternative
- **Score:** **88** = 15 + 16 + 11 + 19 + 9 + 8 + 10
- **Why it is trending:** GitHub displayed **2,941 stars this week**; [v0.1.8](https://github.com/every-app/open-seo/releases/tag/v0.1.8) shipped September 12.
- **Recent evidence:** **18,683 stars / 2,384 forks / 171 open issues**; pushed September 12.
- **Core primitive:** A user-controlled SEO workbench with keyword research, rank tracking, competitor/backlink analysis, audits, AI visibility, MCP, and agent skills.
- **What you can do:** Self-host via Docker or Cloudflare, bring a DataForSEO key, pay the upstream data provider directly, and let local agents query or automate focused SEO workflows.
- **Maturity/license:** MIT and pre-1.0. It is not fully offline: quality data depends on DataForSEO, its costs, quotas, and terms. Hosted service exists, but self-hosting and BYOK are first-class.
- **Verdict:** The clearest proof that “local-owned shell + explicit paid data key” can compete with subscription SaaS. Test one workflow and true unit economics before expanding.

### 6. God's Eye View

- **Repository:** [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)
- **Category:** Geospatial OSINT / 3D browser visualization
- **Score:** **86** = 15 + 19 + 10 + 17 + 10 + 8 + 7
- **Why it is trending:** GitHub displayed **10,485 stars this week**, the second-largest captured weekly gain.
- **Recent evidence:** **33,181 stars / 6,620 forks / 217 open issues**; pushed September 14. Latest tagged release was v0.1.1 on September 1, outside the exact window.
- **Core primitive:** A photorealistic CesiumJS globe layering public aircraft, ships, satellites, earthquakes, traffic, cameras, weather, and other spatial feeds, with optional voice control.
- **What you can do:** Run on localhost without an account or key using keyless map/data paths; add user-owned provider keys for richer imagery, places, polling, AIS, and OpenAI Realtime voice; create new data-layer modules.
- **Maturity/license:** GitHub API returned **NOASSERTION** for license. The README documents provider quotas, plaintext local key files, server-side credential brokering, SSRF protections, and browser-visible restrictions for map keys. OSINT data can be delayed, incomplete, or sensitive.
- **Verdict:** A compelling visualization substrate, but do not build commercially until code/data/provider licensing and responsible-use boundaries are explicit.

### 7. MiniMind

- **Repository:** [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
- **Category:** Small-model training and education
- **Score:** **85** = 15 + 15 + 9 + 19 + 8 + 10 + 9
- **Why it is trending:** GitHub displayed **3,122 stars this week** while the project continued active commits.
- **Recent evidence:** **61,051 stars / 7,937 forks / 64 open issues**; pushed September 14. No tagged release landed inside the exact window.
- **Core primitive:** A readable from-scratch PyTorch implementation and end-to-end training curriculum for a roughly 64M-parameter LLM, including tokenizer, pretraining, SFT, LoRA, preference/RL stages, tool use, agentic RL, distillation, evaluation, and serving.
- **What you can do:** Train or fine-tune a small model, inspect the entire stack, serve it behind an OpenAI-compatible endpoint, or export/use it with Ollama, llama.cpp, vLLM, and other runtimes.
- **Maturity/license:** Apache-2.0 code; public since 2024 with broad adoption. “Two hours” is scoped to a stated 3090/SFT configuration, not every full training path. Dataset and downstream model licenses require separate review.
- **Verdict:** Strong education and domain-small-model substrate; not a frontier-quality replacement. Best remixed into teaching, evaluation, or narrow private adaptation.

### 8. awesome-gpt-image-2

- **Repository:** [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)
- **Category:** Prompt-as-code / visual creator workflow
- **Score:** **84** = 15 + 17 + 9 + 17 + 9 + 8 + 9
- **Why it is trending:** GitHub displayed **5,425 stars this week**.
- **Recent evidence:** **31,839 stars / 3,074 forks / 32 open issues**; pushed September 11. No tagged releases.
- **Core primitive:** A structured visual prompt schema, 500+ reverse-engineered cases, 20+ templates, gallery, and installable agent skill covering interfaces, infographics, products, brands, photography, characters, and storyboards.
- **What you can do:** Reuse prompt components as versioned assets, feed an agent a style-selection skill, and build controllable batch image workflows rather than copying ad hoc prose prompts.
- **Maturity/license:** Repository code/content is marked MIT, but the README says many examples were inspired by public community sources and does not guarantee commercial rights to third-party material. Its hosted generator uses Supabase, Vercel, Stripe, and a relayed image API; the library itself can still be used locally.
- **Verdict:** Valuable as workflow research and internal pattern vocabulary. Build new, rights-cleared templates rather than reselling the collected gallery.

### 9. FreeLLMAPI

- **Repository:** [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)
- **Category:** Self-hosted multi-provider LLM gateway
- **Score:** **84** = 15 + 16 + 9 + 18 + 8 + 8 + 10
- **Why it is trending:** GitHub displayed **3,194 stars this week**; [v0.9.8](https://github.com/tashfeenahmed/freellmapi/releases/tag/v0.9.8) and [v0.9.9](https://github.com/tashfeenahmed/freellmapi/releases/tag/v0.9.9) shipped September 7 and 10.
- **Recent evidence:** **26,138 stars / 3,556 forks / 42 open issues**; pushed September 14.
- **Core primitive:** One local OpenAI/Anthropic/Gemini/Ollama-compatible endpoint over many user-owned provider keys, with routing, failover, rate accounting, encrypted keys, model profiles, and custom compatible endpoints.
- **What you can do:** Point coding agents and SDKs at one server, combine provider free tiers, add a local Ollama/llama.cpp/vLLM endpoint, and route chat/media/audio/embedding requests across a configured pool.
- **Maturity/license:** MIT, but the repository explicitly says **personal experimentation only** for the aggregated free-tier thesis. Free quotas, provider terms, model catalogs, reliability, and premium live-catalog dependencies can change. “7.4B tokens” is the maintainer's aggregate estimate, not an independently audited entitlement.
- **Verdict:** Good routing architecture and test bed; weak commercial thesis if it depends on harvesting free tiers. Remix the endpoint/policy idea, not the “free forever” promise.

### 10. Magnitude

- **Repository:** [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)
- **Category:** Local inference server / agent integration
- **Score:** **84** = 15 + 13 + 10 + 20 + 9 + 7 + 10
- **Why it is trending:** It appeared on the captured daily board with **161 stars today** and shipped five releases from September 8–11, including stable 0.0.12–0.0.14 and 0.0.15 alphas.
- **Recent evidence:** **4,487 stars / 338 forks / 27 open issues**; pushed September 13.
- **Core primitive:** Hardware profiling, model-fit recommendations, downloads, tuning, on-demand loading/unloading, and integration with existing agent harnesses.
- **What you can do:** Make local models available to Hermes, Codex, Claude Code, OpenCode, Pi, Cline, or a built-in harness without manually choosing quantization and runtime settings.
- **Maturity/license:** Apache-2.0; macOS/Linux with Windows via WSL. Very young version numbers and multiple alphas mean interfaces may move. Model licenses remain separate.
- **Verdict:** High strategic fit. Use it as the local side of a transparent local/BYOK escalation boundary.

### 11. Omarchy

- **Repository:** [omacom/omarchy](https://github.com/omacom/omarchy)
- **Category:** Opinionated Linux distribution / developer workstation
- **Score:** **82** = 15 + 17 + 10 + 17 + 7 + 9 + 7
- **Why it is trending:** GitHub displayed **5,296 stars this week** and [v4.0.3](https://github.com/omacom/omarchy/releases/tag/v4.0.3) shipped September 8.
- **Recent evidence:** **41,011 stars / 4,606 forks / 4,286 open issues**; pushed September 13.
- **Core primitive:** A curated, keyboard-driven Linux workstation with opinionated terminal, editor, browser, AI, development, clipboard, recording, dictation, snapshot, and theme workflows.
- **What you can do:** Stand up a reproducible owned workstation instead of assembling a distro configuration piecemeal; study its onboarding and coherent defaults as a product primitive.
- **Maturity/license:** MIT; active major-version product with very high issue volume. It is a whole-environment choice, not a library, and hardware/preferences vary.
- **Verdict:** Strong distribution/design signal. Better used as inspiration or an optional appliance image than as a dependency for a cross-platform creator product.

### 12. NavierStokesAndEuler

- **Repository:** [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler)
- **Category:** Formal mathematics / Lean proof artifacts
- **Score:** **82** = 15 + 16 + 13 + 16 + 10 + 7 + 5
- **Why it is trending:** Created September 8, the repo reached **1,882 stars / 193 forks** inside the window and links the formal artifacts to OpenAI's papers and announcement.
- **Recent evidence:** Created September 8; pushed September 10; zero open issues at snapshot.
- **Core primitive:** Lean 4 certificates/formalizations accompanying finite-time blowup results for Navier–Stokes and Euler equations, with reproducible `lake` build instructions and independent checking guidance.
- **What you can do:** Inspect, build, and independently check machine-verifiable mathematical artifacts rather than relying only on a narrative paper.
- **Maturity/license:** Apache-2.0; research artifact with just two listed contributions at capture. Formal checking establishes what is encoded, so reviewers must still examine whether definitions and statements match the intended theorem claims.
- **Verdict:** Strategically important evidence engineering, but not a direct 1–2 week product base. The remix opportunity is “proof/evidence packets” for narrower technical claims.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Portable agent skill | Archify | Largest weekly gain plus deterministic, portable output |
| Scientific workflow | Scientific Agent Skills | Broad skill catalog, current releases, tests, and BYOK companion |
| Interactive creator/education | OpenMAIC | Multi-format course output with local and BYOK providers |
| Local voice/media | VoiceStudio | Broad production workflow with local APIs and owned assets |
| Open vertical SaaS alternative | OpenSEO | Self-hosted shell plus explicit DataForSEO BYOK economics |
| Spatial/OSINT visualization | God's Eye View | Exceptional momentum and modular public-data layers |
| Small-model learning | MiniMind | End-to-end readable training stack with broad adoption |
| Prompt-as-code | awesome-gpt-image-2 | Structured, reusable visual protocols instead of prompt snippets |
| Multi-provider gateway | FreeLLMAPI | Broad client/protocol compatibility and user-owned keys |
| Local inference | Magnitude | Hardware-aware integration into existing agent harnesses |
| Owned workstation | Omarchy | Strongly coherent developer environment with major weekly momentum |
| Formal evidence | NavierStokesAndEuler | Machine-checkable research artifacts with a clear build path |

## Product remixes

### 1. Owned Explainer Studio — **BUILD**

- **Repos/capabilities remixed:** OpenMAIC + VoiceStudio + Archify + awesome-gpt-image-2.
- **One-liner:** A local project-folder studio that turns source material into an editable visual explainer, narrated lesson, or short course—with every cloud generation step explicitly BYOK.
- **Target user / JTBD:** Technical creator, consultant, or educator who wants repeatable explainers without locking source, voice, or final projects inside a SaaS.
- **Why now / trend thesis:** Four independent creator primitives trended simultaneously: course orchestration, local voice, verifiable diagrams, and prompt-as-code visuals.
- **MVP in 1–2 weeks:** Import one Markdown/PDF evidence pack; generate outline; create one Archify diagram; render a 5-slide HTML lesson in OpenMAIC; narrate locally in VoiceStudio; optional one-image BYOK call; save `project.yml`, prompts, assets, provider receipts, and exports.
- **Differentiation:** Editable source + provenance + provider choice, not one-click disposable content.
- **Local-first/BYOK:** Source, project state, audio, and exports remain local. Local models/voice are defaults; image or premium LLM calls require a user key and per-step approval.
- **Risks/unknowns:** AGPL boundary around VoiceStudio, third-party visual rights, PPTX/HTML fidelity, model quality, and voice consent.
- **Recommendation:** **Build first.**

### 2. Model Boundary Desk — **BUILD**

- **Repos/capabilities remixed:** Magnitude + FreeLLMAPI + [tokentab](https://github.com/crwdla/tokentab) + [tracecrate](https://github.com/FankChen/tracecrate).
- **One-liner:** A local control panel that routes each agent job to local or BYOK cloud models, shows the exact disclosure/cost boundary, and keeps comparable run traces.
- **Target user / JTBD:** Multi-agent power user who wants privacy and cost control without forcing every task strictly offline.
- **Why now / trend thesis:** Local inference, provider aggregation, spend inspection, and local trace analysis all gained momentum in the same week.
- **MVP in 1–2 weeks:** Support two harness logs; one Magnitude endpoint; two BYOK cloud providers; policy labels (`local-only`, `cloud-ok-redacted`, `cloud-ok-full`); preflight disclosure preview; per-job cost estimate; run comparison; Markdown receipt.
- **Differentiation:** A visible policy and evidence boundary instead of an opaque “smart router.”
- **Local-first/BYOK:** Configuration, logs, traces, policies, and default inference stay local; cloud credentials are user supplied and selected per task.
- **Risks/unknowns:** Token-price accuracy, prompt redaction leaks, provider feature mismatches, key storage, and upstream alpha churn.
- **Recommendation:** **Build a narrow two-provider version.**

### 3. Evidence Course Lab — **BUILD / VERTICALIZE**

- **Repos/capabilities remixed:** Scientific Agent Skills + OpenMAIC + Archify + optional NavierStokesAndEuler-style formal artifact pattern.
- **One-liner:** Turn a reviewed evidence folder into a cited, interactive mini-course whose claims link to sources, diagrams, computations, and machine-checkable artifacts.
- **Target user / JTBD:** Research educator, internal enablement team, or technical consultant converting complex evidence into teachable material.
- **Why now / trend thesis:** Scientific skills, course generation, and deterministic explanation artifacts all show strong independent momentum; formal proof artifacts raise the bar from plausible prose to checkable evidence.
- **MVP in 1–2 weeks:** Pick one non-clinical technical topic; ingest five sources; run two reviewed skills; create a claim ledger; generate three lesson pages, one quiz, and one Archify map; block uncited claims; export HTML + Markdown evidence pack.
- **Differentiation:** Claim-to-source traceability and editable owned artifacts, not generic AI course generation.
- **Local-first/BYOK:** Corpus and ledger local; user chooses local or BYOK models; outbound queries are logged.
- **Risks/unknowns:** Citation correctness, skill supply-chain trust, domain liability, source licensing, and evaluation burden.
- **Recommendation:** **Build for one narrow technical domain, not medicine first.**

### 4. OSINT Storyboard — **PROTOTYPE**

- **Repos/capabilities remixed:** God's Eye View + Archify + VoiceStudio.
- **One-liner:** A local spatial investigation notebook that turns selected public signals into a time-stamped map story, evidence diagram, and narrated briefing.
- **Target user / JTBD:** Journalist, researcher, emergency-planning analyst, or educator explaining a public event without surrendering the case file to a hosted platform.
- **Why now / trend thesis:** Spatial data aggregation and explainable artifact generation both saw exceptional weekly velocity.
- **MVP in 1–2 weeks:** One permitted event type; bookmark five observations; export GeoJSON + screenshots; generate one timeline/flow map; record local narration; include source timestamps and freshness warnings.
- **Differentiation:** Reproducible evidence packet, not a sensational “spy” interface.
- **Local-first/BYOK:** Case notes and media stay local; optional place/voice/model services use restricted user keys.
- **Risks/unknowns:** No detected repository license, provider/data terms, location privacy, stale feeds, dual-use abuse, and evidentiary overclaiming.
- **Recommendation:** **Prototype only after license and responsible-use review.**

### 5. Open Growth Room — **BUILD A NARROW WEDGE**

- **Repos/capabilities remixed:** OpenSEO + awesome-gpt-image-2 + VoiceStudio + Archify.
- **One-liner:** An owned campaign workspace that researches demand with BYOK data, produces rights-cleared assets locally, and records why each content decision was made.
- **Target user / JTBD:** Solo creator or small agency that wants Semrush-like evidence and repeatable production without another all-in-one subscription.
- **Why now / trend thesis:** Vertical BYOK data tools and reusable creator protocols are converging.
- **MVP in 1–2 weeks:** One domain; DataForSEO key; keyword cluster; competitor map; one content brief; one original thumbnail template; one local voice teaser; export an evidence-backed campaign folder.
- **Differentiation:** Research-to-asset lineage and source ownership, not mass auto-publishing.
- **Local-first/BYOK:** Briefs, assets, voice, and history local; SEO data and optional image/model calls use user keys.
- **Risks/unknowns:** DataForSEO cost, generated-content quality, image rights, search-engine policy changes, and temptation toward spam.
- **Recommendation:** **Build for one high-value deliverable; no auto-posting.**

### 6. Skill Flight Recorder — **BUILD AFTER THREAT MODEL**

- **Repos/capabilities remixed:** Scientific Agent Skills + Archify + Cursor plugins + JetBrains Go guidelines + tracecrate.
- **One-liner:** A local lab that installs a pinned agent skill into a disposable workspace, records every tool call, and outputs a behavior/permission map before the user trusts it.
- **Target user / JTBD:** Developer adopting third-party agent skills who needs more than a README and star count.
- **Why now / trend thesis:** Skills are surging faster than review, version pinning, and runtime evidence.
- **MVP in 1–2 weeks:** Import one skill; resolve license/provenance; static file/network/command inventory; run three fixtures with mock secrets; record trace; render Archify data-flow map; output pass/fail plus non-certification disclaimer.
- **Differentiation:** Reproducible behavior evidence rather than another skills marketplace.
- **Local-first/BYOK:** Tests and traces local; evaluator uses a local model or user-supplied provider key.
- **Risks/unknowns:** Sandbox escapes, incomplete fixtures, prompt injection, false confidence, and rapidly changing host semantics.
- **Recommendation:** **Threat-model first, then build a single-host proof.**

### 7. Tiny Model Academy — **BUILD AS EDUCATION, NOT INFRA**

- **Repos/capabilities remixed:** MiniMind + OpenMAIC + Archify + Magnitude.
- **One-liner:** A hands-on local course where learners train a tiny model, inspect each stage visually, serve it locally, and compare it with a BYOK frontier model.
- **Target user / JTBD:** Developer or student who uses LLM APIs but does not understand the model/training stack.
- **Why now / trend thesis:** Tiny trainable models and interactive agent-generated education both have strong adoption.
- **MVP in 1–2 weeks:** One three-hour path: tokenizer, tiny training run, SFT, evaluation, localhost endpoint; Archify pipeline map; OpenMAIC lesson and quiz; optional comparison call.
- **Differentiation:** Learners produce a working owned model and evidence, not merely watch videos.
- **Local-first/BYOK:** Core run local; optional cloud comparison requires a user key.
- **Risks/unknowns:** Hardware variance, long setup, dataset terms, oversimplification, and confusing educational success with model quality.
- **Recommendation:** **Build as a workshop kit.**

### 8. Forecast Narrative Notebook — **MONITOR / TECH SPIKE**

- **Repos/capabilities remixed:** TimesFM + Scientific Agent Skills + Archify + VoiceStudio.
- **One-liner:** A local notebook that turns a time series into a forecast, assumptions/uncertainty map, and narrated decision briefing.
- **Target user / JTBD:** Operator or analyst who needs an understandable forecast artifact rather than a naked chart.
- **Why now / trend thesis:** TimesFM re-entered Trending after its 3.0 multivariate/covariate update, while evidence and explanation tooling surged.
- **MVP in 1–2 weeks:** One public dataset; run baseline + TimesFM; backtest; visualize covariates and error; generate an Archify assumption map; local narration; export notebook and report.
- **Differentiation:** Reproducibility and uncertainty communication, not “AI predicts the future.”
- **Local-first/BYOK:** Data and analysis local; optional interpretation call is user-keyed.
- **Risks/unknowns:** TimesFM 3.0 weights are non-commercial/non-production despite Apache source; forecast misuse; compute requirements; weak domain baselines.
- **Recommendation:** **Spike with 2.5 or another commercially compatible model; do not productize 3.0 weights blindly.**

### 9. Creator Workstation Image — **MONITOR**

- **Repos/capabilities remixed:** Omarchy + Magnitude + VoiceStudio + OpenSEO.
- **One-liner:** A reproducible local creator/developer workstation with local inference, voice/media tools, and optional BYOK research connectors already wired together.
- **Target user / JTBD:** Technical creator who wants one owned machine rather than a dozen cloud dashboards and brittle setup guides.
- **Why now / trend thesis:** The opinionated workstation, local endpoint, media engine, and vertical BYOK tool all trended together.
- **MVP in 1–2 weeks:** Installation script or VM image—not a new distro—with pinned versions, health check, local dashboard, sample project, encrypted key setup, and uninstall/rollback.
- **Differentiation:** An integrated workflow appliance, not an app list.
- **Local-first/BYOK:** The workstation and project data are local; external services are optional user-keyed adapters.
- **Risks/unknowns:** Hardware/driver support, Omarchy churn, AGPL integration boundaries, maintenance burden, and support expectations.
- **Recommendation:** **Monitor; dogfood a script before shipping an image.**

### 10. Research Claim Packet — **DEEP-DIVE**

- **Repos/capabilities remixed:** NavierStokesAndEuler formal-artifact pattern + Scientific Agent Skills + Archify.
- **One-liner:** A standard local folder for a technical claim containing plain-language statement, definitions, sources, executable checks, dependency graph, and reviewer notes.
- **Target user / JTBD:** Research engineer publishing a claim that others should reproduce or challenge.
- **Why now / trend thesis:** Formal certificates drew rapid attention while agent-driven scientific workflows are mainstreaming.
- **MVP in 1–2 weeks:** Choose a modest algorithmic theorem or data result; define `CLAIM.md`, machine-readable manifest, runnable check, environment lockfile, Archify dependency map, and independent-review checklist.
- **Differentiation:** Productizes the evidence envelope, not theorem generation.
- **Local-first/BYOK:** Artifacts and checks local; optional explanation model is user-selected.
- **Risks/unknowns:** Formalization expertise, false equivalence between a passing check and the intended claim, and limited buyer urgency.
- **Recommendation:** **Deep-dive as an open standard experiment.**

### 11. Local Visual Protocol Registry — **BUILD QUICKLY**

- **Repos/capabilities remixed:** awesome-gpt-image-2 + Archify + [holo-card-studio](https://github.com/EverettFish/holo-card-studio) + [dream-loop](https://github.com/achimala/dream-loop).
- **One-liner:** A Git-native registry of original visual protocols, references, assets, render tests, and provider adapters for 2D/3D creator agents.
- **Target user / JTBD:** Design-engineering team that wants consistent AI-assisted visuals without hiding prompts and assets in vendor histories.
- **Why now / trend thesis:** Prompt-as-code, Blender/Three.js skills, and deterministic visual artifacts all spiked together.
- **MVP in 1–2 weeks:** Define one YAML/JSON schema; create ten original templates; local preview; one BYOK image adapter; one Blender/Three.js output; screenshot regression tests; license/provenance fields.
- **Differentiation:** Rights/provenance and reproducibility, not a scraped prompt gallery.
- **Local-first/BYOK:** Registry, references, and outputs local; generator adapters use user keys.
- **Risks/unknowns:** Visual evaluation, model drift, rights provenance, schema overdesign, and provider lock-in through prompt quirks.
- **Recommendation:** **Build a tiny registry for internal use.**

### 12. Legacy GPU Creator Booster — **IGNORE AS A PRODUCT; LEARN FROM DEMAND**

- **Repos/capabilities remixed:** dlssg_for_sm86 + VoiceStudio/Magnitude workload scheduling.
- **One-liner:** A local diagnostics layer that helps creators understand when older GPUs can safely accelerate supported media workflows.
- **Target user / JTBD:** RTX 30-series owner trying to extend hardware life.
- **Why now / trend thesis:** dlssg_for_sm86 amassed **2,662 stars** immediately after creation, showing demand for local hardware longevity.
- **MVP in 1–2 weeks:** Read-only hardware/driver inventory, benchmark runner, compatibility matrix, rollback plan, and links to upstream—not redistribution of proprietary binaries.
- **Differentiation:** Safety and evidence instead of unsupported performance promises.
- **Local-first/BYOK:** Entirely local diagnostics.
- **Risks/unknowns:** GitHub API detected no license, while README says GPLv3 source but proprietary NVIDIA runtime/kernels are not relicensed; anti-cheat risk, binary trust, driver breakage, and no Mac relevance.
- **Recommendation:** **Ignore as a commercial remix. Treat momentum as a hardware-ownership signal.**

## Top three product bets and first experiments

### Bet 1 — Owned Explainer Studio

**Rationale:** OpenMAIC, VoiceStudio, Archify, and the visual protocol library attack complementary stages of the same job. The durable moat is not generation; it is an editable, source-controlled project with provider receipts and the option to keep most work local.  
**First experiment:** In three days, turn one five-page technical source packet into a five-slide HTML lesson and 90-second narrated explainer. Require one validated diagram, local voice, and at most one BYOK image call. Proceed if a factual correction can be made and rerendered in under ten minutes, every external call appears in the manifest, and the project opens without the original app.

### Bet 2 — Model Boundary Desk

**Rationale:** It directly implements Asif's preferred architecture: local-first, not strictly offline; cloud-capable, but only through explicit user-owned keys and visible policies. Existing routers optimize availability; the wedge is disclosure, cost, and comparable evidence.  
**First experiment:** Route 20 real agent prompts—ten local, ten cloud-eligible—through one Magnitude endpoint and two BYOK APIs. Before each cloud call, show the exact payload and estimated cost; after each, save a trace. Proceed if policy classification is correct on at least 19/20, no local-only payload leaves the machine, and the added routing/approval overhead is under 15%.

### Bet 3 — Evidence Course Lab

**Rationale:** Scientific Agent Skills provides depth, OpenMAIC provides an interactive delivery surface, and Archify makes structure inspectable. A claim ledger gives the product a trust wedge that generic course generators lack.  
**First experiment:** Build a three-lesson module from five authoritative sources on one non-clinical technical topic. Have a second reviewer grade 30 generated claims for citation support. Proceed if at least 28/30 claims are directly supported, all unsupported claims are blocked or flagged, and the final HTML plus evidence folder is understandable without a hosted account.

## Try now / monitor / ignore

### Try now

- **Archify:** generate one real system map and inspect whether validation catches a deliberate broken reference.
- **OpenMAIC:** self-host a five-slide course using one local model and one explicit BYOK provider.
- **VoiceStudio:** produce one consented local narration and verify project/API portability.
- **Magnitude:** profile one machine and compare its recommended local model with the current local runtime choice.
- **OpenSEO:** run one DataForSEO-funded keyword/audit workflow and record true per-deliverable cost.

### Monitor

- **God's Eye View:** momentum is exceptional, but licensing and data/provider boundaries need clarification.
- **FreeLLMAPI:** watch provider-term compliance, signed catalog governance, and reliability; do not build a business on free-tier aggregation.
- **Magnitude:** high fit but very early versions and alpha releases.
- **OpenMAIC:** strong capability breadth; watch integration stability and issue burn-down.
- **New creator skills:** anything2explainer, holo-card-studio, dream-loop, and design-studio-ai show a fast-growing “skill as product” pattern.

### Ignore or de-prioritize this week

- **AI-detector bypass tools:** high stars do not overcome questionable educational/workplace use and adversarial incentives.
- **“Unlimited/free tokens” as the product promise:** provider terms, quotas, key security, and catalog churn make this a fragile commercial foundation.
- **Unlicensed binary proxy derivatives:** especially where proprietary runtimes or anti-cheat-sensitive injection are involved.
- **Another generic all-purpose agent workspace:** build a narrow creator, evidence, routing, or review job instead.
- **A scraped prompt marketplace:** the opportunity is original, rights-cleared, testable protocols—not repackaged examples.

## Rising but less proven

| Repository | Signal in/near window | Why watch | Main caveat |
|---|---|---|---|
| [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) | Created Sep 7; 2,662★ / 159 forks | Huge hardware-longevity demand | API `NOASSERTION`; proprietary components; binary/anti-cheat risk |
| [Edge0-AI/Edge0](https://github.com/Edge0-AI/Edge0) | Created Sep 8; 1,679★ / 132 forks; active Sep 14 | Rapid unexplained uptake | No API description; needs hands-on verification before recommending |
| [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | Created Sep 7; 1,521★ / 215 forks | Editable Blender + Three.js agent skill | License `NOASSERTION`; created before exact start by hours |
| [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | Created Sep 8; 1,298★ / 218 forks | Topic-to-Remotion narrated explainer skill | License `NOASSERTION`; quality and rights untested |
| [crwdla/tokentab](https://github.com/crwdla/tokentab) | Created Sep 7; 1,075★ / 212 forks | Local cost analysis across agent logs | Initial push only; pricing/model parsing can drift |
| [achimala/dream-loop](https://github.com/achimala/dream-loop) | Created Sep 7; 985★ / 113 forks | Blender + image generation + critic loop | Very new; asset rights and reproducibility |
| [sumimakito/Mac-Duo](https://github.com/sumimakito/Mac-Duo) | Created Sep 10; 848★ / 62 forks | Strong non-AI/macOS novelty | Narrow utility; 26 issues in four days |
| [gazijarin/itsgiving](https://github.com/gazijarin/itsgiving) | Created Sep 8; 838★ / 100 forks | Lightweight meeting-expression utility | One-day code signal; unclear durability |
| [qingjian-team/qingjian](https://github.com/qingjian-team/qingjian) | 506★; active Sep 14 | Offline pinyin IME plus language learning | GPL-3.0; locale-specific; early |
| [unstablebuild/rune](https://github.com/unstablebuild/rune) | Created Sep 10; 509★; active Sep 14 | Agent-oriented TUI/IDE/workspace manager | GPL-3.0; 65 issues; crowded category |
| [FankChen/tracecrate](https://github.com/FankChen/tracecrate) | Created Sep 10; 119★ | Excellent local-first observability fit | Very early; only four forks at snapshot |
| [anuj0456/OpenArch](https://github.com/anuj0456/OpenArch) | HN Sep 14: 117 points / 28 comments; 192★ | Readable implementations of modern LLM architectures | Discussion outruns repository adoption |
| [rh1tech/frank-386](https://github.com/rh1tech/frank-386) | HN Sep 14: 163 points / 45 comments; 122★ | Compelling non-AI RP2350 x86-emulation project | License `NOASSERTION`; niche hardware |
| [callbacked/kinesis](https://github.com/callbacked/kinesis) | HN Sep 14: 90 points / 27 comments; 41★ | Native Mac control from Meta Neural Band | Submitted 31 seconds after the exact cutoff; no detected license |
| [godot-pty/gpty](https://github.com/godot-pty/gpty) | HN Sep 11: 96 points / 49 comments; 64★ | Godot/Rust multi-PTY desktop experiment | HN interest much larger than repo adoption; GPL-3.0 |

## Overhyped / be careful

1. **Star velocity is attention, not product validation.** Several repos added thousands of stars while still pre-1.0, unlicensed, or minimally contributed.
2. **FreeLLMAPI's aggregate quota headline is not a durable entitlement.** The architecture is useful; the commercial promise is not independently verified and may conflict with provider limits or terms.
3. **God's Eye View has a dramatic “spy satellite” framing.** The practical primitive is public-data visualization. Avoid intelligence-quality claims and review every data source's terms/freshness.
4. **AI image example libraries carry rights ambiguity.** An MIT repository wrapper does not automatically grant commercial rights to every referenced prompt/image/source.
5. **TimesFM 3.0 is not commercially deployable under the current weight license.** Apache-2.0 covers source; the README says 3.0 pretrained weights are non-commercial/non-production.
6. **Binary modification tools deserve higher trust scrutiny than source libraries.** Code-signing, benchmarks, and stars do not eliminate proprietary-component, anti-cheat, malware, or rollback risk.
7. **Search results can be gamed.** Very new repos with hundreds of stars and forks but little independent discussion should be treated as unverified momentum until hands-on testing.

## Best workflow to keep doing weekly

1. Capture GitHub Trending weekly and daily at a fixed time.
2. Save authenticated REST metadata immediately afterward.
3. Search `created:` for the exact rolling window and separate **current totals** from **verified growth**.
4. Scan HN/Show HN using epoch boundaries; retain points/comments and story timestamps.
5. Require every top item to have an in-window signal, an official repo capability check, and a license note.
6. Track previous week's total snapshots locally to calculate reliable week-over-week star deltas rather than depending only on Trending.
7. Score two views separately next iteration: **market momentum** and **Asif strategic fit**. The combined score is useful, but separate axes would make contrarian high-fit bets such as tracecrate easier to see.
8. For remixes, insist on one concrete user job, an owned data/project format, explicit local/cloud boundaries, and a three-day falsifiable experiment.

## Raw candidate appendix

Metrics below are capture-time values. `+weekly`/`+today` are rendered GitHub Trending signals. Plain star counts for new/search/HN candidates are totals, not claimed growth.

| Candidate | Category | Momentum / date evidence | License note | Short take |
|---|---|---|---|---|
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | Diagram-as-code skill | +24,227 weekly; 61,876★ / 4,084 forks; Sep 14 push | MIT | Strongest weekly reusable primitive |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | Geospatial OSINT | +10,485 weekly; 33,181★ / 6,620 forks; Sep 14 push | `NOASSERTION` | Exceptional attention; verify license/data terms |
| [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | Interactive education | +10,023 weekly; 36,749★ / 5,811 forks; v1.0.2 Sep 13 | MIT | High-fit local/BYOK creator stack |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Scientific skills | +7,370 weekly; 44,895★ / 4,069 forks; releases Sep 10–11 | MIT repo; per-skill terms vary | Strong vertical skill ecosystem |
| [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | Visual prompt protocols | +5,425 weekly; 31,839★ / 3,074 forks; Sep 11 push | MIT wrapper; third-party rights vary | Useful patterns, not a rights-cleared catalog |
| [omacom/omarchy](https://github.com/omacom/omarchy) | Linux workstation | +5,296 weekly; 41,011★ / 4,606 forks; v4.0.3 Sep 8 | MIT | Coherent owned-workstation signal |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Local voice/media | +3,902 weekly; 28,643★ / 3,505 forks; v0.5.2 Sep 10 | AGPL-3.0; model terms vary | Best local creator engine |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | LLM gateway | +3,194 weekly; 26,138★ / 3,556 forks; v0.9.9 Sep 10 | MIT; personal-experiment warning | Good router, fragile free-tier thesis |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | Tiny LLM training | +3,122 weekly; 61,051★ / 7,937 forks; Sep 14 push | Apache-2.0 code | Excellent learning substrate |
| [every-app/open-seo](https://github.com/every-app/open-seo) | Self-hosted SEO | +2,941 weekly; 18,683★ / 2,384 forks; v0.1.8 Sep 12 | MIT | Strong BYOK vertical pattern |
| [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) | GPU compatibility | Created Sep 7; 2,662★ / 159 forks | API `NOASSERTION`; mixed components | Demand signal; high trust/legal risk |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | AI curriculum | +2,525 weekly; 54,541★ / 9,540 forks | MIT | Broad adoption; release just before exact start |
| [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | UI generation | +2,412 weekly; 78,798★ / 9,617 forks; Sep 9 push | MIT | Mature workflow resurfacing |
| [google-research/timesfm](https://github.com/google-research/timesfm) | Forecasting model | +2,324 weekly; 32,454★ / 3,109 forks; Sep 9 push | Apache source; 3.0 weights restricted | Important but commercial caveat |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Model modification | +2,146 weekly; 31,376★ / 3,512 forks | AGPL-3.0 | High attention; safety/quality risks |
| [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) | Formal proofs | Created Sep 8; 1,882★ / 193 forks | Apache-2.0 | Formal evidence pattern worth studying |
| [Edge0-AI/Edge0](https://github.com/Edge0-AI/Edge0) | AI / unclear | Created Sep 8; 1,679★ / 132 forks; active Sep 14 | Apache-2.0 | Momentum strong, capability not verified |
| [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | Blender/Three.js skill | 1,521★ / 215 forks; Sep 12 push | `NOASSERTION` | Editable 3D creator workflow |
| [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | Coding agent | +1,389 weekly; 33,271★ / 9,083 forks; Sep 12 push | `NOASSERTION` | Large audience, weak licensing clarity |
| [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | Explainer-video skill | Created Sep 8; 1,298★ / 218 forks | `NOASSERTION` | Strong remix fit, very new |
| [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | Coding guidelines | +1,213 weekly; 3,454★ / 111 forks; Sep 10 push | Apache-2.0 | Skills/guidelines as agent infrastructure |
| [cursor/plugins](https://github.com/cursor/plugins) | Plugin specification | +1,159 weekly; 7,700★ / 679 forks; Sep 14 push | No detected license | Distribution standard, not standalone product |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP directory | +1,130 weekly; 94,976★ / 16,138 forks | MIT | Discovery mature; evaluation is missing layer |
| [crwdla/tokentab](https://github.com/crwdla/tokentab) | Agent cost CLI | Created Sep 7; 1,075★ / 212 forks | MIT | High-fit local operations primitive |
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | C++ infrastructure | +993 weekly; +963 today; 25,771★ / 3,066 forks | MIT | Strong non-AI daily event, cause unclear |
| [achimala/dream-loop](https://github.com/achimala/dream-loop) | 3D creator skill | Created Sep 7; 985★ / 113 forks | MIT | Agent-critic visual loop |
| [majd/ipatool](https://github.com/majd/ipatool) | App Store CLI | +847 weekly; 11,209★ / 937 forks; v2.6.0 Sep 13 | MIT | Useful non-AI package/research utility |
| [sumimakito/Mac-Duo](https://github.com/sumimakito/Mac-Duo) | macOS utility | Created Sep 10; 848★ / 62 forks | Apache-2.0 | Novel local UX, narrow scope |
| [gazijarin/itsgiving](https://github.com/gazijarin/itsgiving) | Meeting utility | Created Sep 8; 838★ / 100 forks | MIT | Meme interaction; durability unclear |
| [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | Local inference | +161 today; 4,487★ / 338 forks; releases Sep 8–11 | Apache-2.0 | Best strategic local endpoint candidate |
| [anuj0456/OpenArch](https://github.com/anuj0456/OpenArch) | LLM education | HN Sep 14: 117 / 28; 192★ | MIT | Strong practitioner interest, early repo |
| [rh1tech/frank-386](https://github.com/rh1tech/frank-386) | Embedded/x86 emulation | HN Sep 14: 163 / 45; 122★ | `NOASSERTION` | Top HN-linked non-AI project |
| [FankChen/tracecrate](https://github.com/FankChen/tracecrate) | Agent observability | Created Sep 10; 119★ / 4 forks | MIT | High-fit but unproven local trace layer |
| [callbacked/kinesis](https://github.com/callbacked/kinesis) | Neural-band macOS input | HN Sep 14: 90 / 27; 41★ | No detected license | Strong discussion just after cutoff |
| [godot-pty/gpty](https://github.com/godot-pty/gpty) | Terminal multiplexer | HN Sep 11: 96 / 49; 64★ | GPL-3.0 | Interesting non-AI UX experiment |

## Sources and limitations

- **Time boundary:** The exact rolling window starts September 7 at 12:01 EDT (16:01 UTC). GitHub Trending's “weekly” page is not a documented exact rolling-window API; it is treated as directional evidence captured on September 14. A few weekly items had their last release/commit shortly before the exact boundary but still had an in-window Trending signal.
- **GitHub metric disagreement:** Rendered page totals and authenticated REST totals differed on several fast-moving repositories. Weekly/daily deltas are quoted only from Trending; totals are quoted only from REST; no synthetic growth was calculated from mismatched surfaces.
- **Search noise/manipulation:** GitHub search is vulnerable to copied repos, artificial stars/forks, misleading descriptions, and incomplete license detection. High-growth search-only candidates were not promoted without enough operational detail.
- **HN coverage:** The Algolia scan was bounded to the 1,000 newest stories in the exact window, not every story submitted during all seven days. Points/comments are capture-time values and can change. Kinesis's main HN submission occurred 31 seconds after the exact cutoff and is labeled accordingly.
- **Independent social evidence:** X/Twitter, LinkedIn, and Reddit were not systematically accessible or authenticated for this run. Product Hunt is not a useful primary source for repository momentum and was not used.
- **No download/usage verification:** Stars, forks, releases, issues, and discussion are proxies. This run did not install and benchmark every top repository.
- **License scope:** GitHub's detected license is repository-level only. Individual models, datasets, binaries, providers, examples, and skills may use different terms. `NOASSERTION` means no reliable license was detected, not that reuse is permitted.
- **Claims:** Maintainer claims such as scientist counts, free-token totals, benchmark rankings, supported languages, or performance improvements are identified as project claims unless independently corroborated.

---

*Prepared for Asif's weekly GitHub trends and product-remix review. Primary decision lens: owned local state, portable artifacts, explicit BYOK cloud boundaries, and a concrete experiment that can disprove the idea quickly.*
