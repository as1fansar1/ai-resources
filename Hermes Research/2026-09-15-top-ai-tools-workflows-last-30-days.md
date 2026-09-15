# Top AI tools and workflows — last 30 days

Research date: **2026-09-15 08:05:56 EDT (UTC-04:00)**
Window: **2026-08-16 08:05:56 EDT through 2026-09-15 08:05:56 EDT** (rolling preceding 30 days)
Scope: coding and cloud agents, business automation, research/evaluation, workspace and voice agents, open/local AI, observability, credential isolation, and agent security.

## Executive summary

The month’s strongest development is a shift from “an LLM with tools” to an **operated agent system**: a maintained harness, isolated compute, explicit capabilities, durable state, evidence-producing outputs, policy that the agent cannot override, and a reviewer or deterministic check before consequential action.

Five themes dominate:

1. **The harness is now a first-class product.** OpenAI exposed the Codex harness as Agents API; GitHub expanded Agent Host permissions and tool-using code review; Claude Code, Hermes, n8n, and GitHub Agentic Workflows continued shipping rapidly. Models still matter, but context, recovery, sandboxing, identity, and verification increasingly decide real task success.
2. **Verification is becoming more concrete.** Terminal-Bench-Science grades artifacts with reproducible tests, while GitHub Copilot’s review agents can run builds and targeted scripts. The practical standard is no longer “the agent said it worked,” but a diff, test, trace, dashboard, or source ledger that another process can inspect.
3. **Authority, not intelligence, is the binding safety question.** September disclosures described agents escaping weak containment or reaching real third-party systems. GitHub’s centrally managed permissions, OneCLI’s credential surrogation, Geiger’s exposure inventory, and Meta’s separate Sentinel control plane all point toward capability-based controls outside the model.
4. **Agents are moving into high-value work surfaces.** ChatGPT’s Data agent connects governed semantic layers to evidence-backed dashboards; Gemini Live/Spark turns voice requests into scheduled Workspace tasks; domain products package trusted finance and healthcare data rather than relying on arbitrary web retrieval.
5. **Local AI needs full-harness evaluation.** Practitioner experiments showed that quantization, templates, attention backends, tensor parallelism, and runtime settings can change tool-call correctness even with the same weights. Test the complete local stack on real trajectories, not three prompts or tokens-per-second alone.

**Bottom line:** try review-gated coding, deterministic-shell automation, recurring verified operations, and source-grounded data analysis now. Pilot managed cloud-agent APIs and credential gateways on low-risk tasks. Monitor Meta Muse and other broad personal agents until independent privacy, security, and completion evidence catches up with their authority.

## Scoring methodology

The requested 100-point rubric was applied in this order: **recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance to Asif 10**. Component totals were calculated programmatically. Scores reward in-window releases, independent evidence, concrete jobs-to-be-done, inspectable output, adoption signals, and fit for coding/automation/research. Deductions were applied for preview status, vendor-only benchmarks, broad permissions, unverified adoption claims, and serious security uncertainty.

GitHub stars and forks are live snapshots collected **September 15, 2026**, not 30-day gains. Repository pushes and releases establish recent activity, not reliability. Product Hunt’s accessible Atom feed was used for discovery; direct leaderboard/upvote coverage was incomplete.

## Top ranked tools/workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | Claude Fable 5.1 + Claude Code: spec → implementation → tests → clean review | 98 | **Try now** |
| 2 | OpenAI Agents API: durable sandbox → bounded subagents → evidence artifact | 97 | **Pilot now** |
| 3 | GitHub Copilot: centrally managed permissions → agent change → tool-using review | 97 | **Try/pilot now** |
| 4 | n8n: deterministic trigger/credentials/retries around one AI decision | 95 | **Try now** |
| 5 | Terminal-Bench-Science: real task → artifact → reproducible grader → human interpretation | 94 | **Adopt the pattern** |
| 6 | GPT-6 Astra: high-ambiguity planner/reviewer inside least privilege | 94 | **Benchmark carefully** |
| 7 | Hermes: recurring goal → bounded research/action → verified artifact | 93 | **Keep using** |
| 8 | ChatGPT Data agent: semantic layer → evidence → dashboard → approved action | 91 | **Pilot with read-only data** |
| 9 | GitHub Agentic Workflows: read broadly → safe-output PR → CI/review | 90 | **Pilot in a low-risk repo** |
| 10 | Gemini Live + Spark: voice intent → long-running Workspace task → review | 88 | **Pilot on reversible work** |
| 11 | Meta Muse: dedicated VM + Sentinel + user approval for personal operations | 87 | **Monitor / tightly limit** |
| 12 | OneCLI: agent placeholder credential → policy gateway → scoped API call | 87 | **Security review, then pilot** |
| 13 | Gemini 3.5 Transcribe: speech → structured transcript → deterministic downstream action | 87 | **Benchmark now** |
| 14 | Local LLM runtime-fidelity loop: pin stack → replay trajectories → compare tool correctness | 85 | **Adopt before local migration** |
| 15 | Geiger: inventory agent surface → diff drift → remove or sandbox capabilities | 85 | **Try as a preflight** |

## Detailed findings

### 1. Claude Fable 5.1 + Claude Code: spec → implementation → tests → clean review

**Score:** 98 = 15/20/15/20/9/9/10
**Category:** coding agents / AI-native SDLC · **Recommendation:** Try now

**Why it matters:** Anthropic launched Fable 5.1 and restricted-access Mythos 5.1 on September 1. Anthropic reports Fable 5.1 at 55.8% on Terminal-Bench 4.0, 52.6% on Terminal-Bench-Science 0.1, and roughly 25% lower typical workload cost than Fable 5 because of cheaper cache reads; treat these as vendor results until reproduced. Distribution and ecosystem signals are strong: GitHub added Fable 5.1 to Copilot on September 4, while `anthropics/claude-code` had **145,123 stars**, **23,157 forks**, and v2.1.272 on September 15.

**Evidence:** [Anthropic launch, Sep 1](https://www.anthropic.com/claude-fable-and-mythos-5-1) · [Copilot model rollout, Sep 4](https://github.blog/changelog/2026-09-04-github-copilot-weekly-releases-august-31/) · [Claude Code v2.1.272, Sep 15](https://github.com/anthropics/claude-code/releases/tag/v2.1.272) · [verification beyond line review, Aug 22](https://simonwillison.net/2026/Aug/22/more-than-just-code-review/)

**Practical workflow:** write a short spec and acceptance tests; isolate work in a branch/worktree; let the agent implement and run checks; require a second clean-context pass to challenge the diff and rerun targeted tests; merge manually. Preserve corrections as versioned project instructions instead of repeating them in chat.

**Best next step:** compare Fable 5.1 with the current default on ten representative repository tasks, recording accepted-result cost, review corrections, test failures, and cycle time.

### 2. OpenAI Agents API: durable sandbox → bounded subagents → evidence artifact

**Score:** 97 = 15/19/15/20/10/8/10
**Category:** managed agent infrastructure · **Recommendation:** Pilot now

**Why it matters:** OpenAI’s September 10 public beta exposes the maintained Codex harness through an API: durable sessions, context management, skills, hosted or bring-your-own environments, MCP, vaults, asynchronous operation, and bounded subagent concurrency. Customer statements on the launch page report improvements such as 4× lower latency, 60% lower cost per case, and 86% fewer failed responses, but these are selected testimonials rather than audited studies. `openai/codex` had **124,314 stars**, **19,200 forks**, and same-day development activity on September 15.

**Evidence:** [Agents API launch, Sep 10](https://openai.com/index/introducing-the-agents-api/) · [Codex repository](https://github.com/openai/codex) · [Product Hunt feed listing, Sep 15](https://www.producthunt.com/feed)

**Practical workflow:** define one narrow objective; choose a sandbox with only required files and egress; mount capability/skill directories; cap subagents and spend; write findings, commands, evidence, and unresolved risks to `/workspace/outputs`; have deterministic checks or a human accept the artifact before any external write.

**Best next step:** migrate one read-only incident investigation or research workflow and compare completion rate, latency, cost, and recoverability with the current harness.

### 3. GitHub Copilot: centrally managed permissions → agent change → tool-using review

**Score:** 97 = 15/19/15/20/9/9/10
**Category:** collaborative coding / governance · **Recommendation:** Try or pilot now

**Why it matters:** On September 9 GitHub made centrally managed agent permissions generally available for shell commands, file operations, and network domains; user settings and saved approvals cannot weaken them. On September 11 Copilot code review gained shell-backed validation behind the agent firewall and an ensemble reviewer. GitHub reports 47% more addressed high-severity comments and about 8% lower review cost in its experiments. On September 4, content exclusions reached Copilot app/CLI and Agent Merge entered preview.

**Evidence:** [managed permissions, Sep 9](https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations/) · [tool-using ensemble review, Sep 11](https://github.blog/changelog/2026-09-11-auto-resolution-and-analysis-updates-in-copilot-code-review/) · [content exclusions and Agent Merge, Sep 4](https://github.blog/changelog/2026-09-04-github-copilot-weekly-releases-august-31/) · [VS Code agent adoption metrics, Sep 11](https://github.blog/changelog/2026-09-11-add-vs-code-agents-to-copilot-usage-metrics/)

**Practical workflow:** centrally block production domains and sensitive paths; allow required repository reads and sandboxed test commands; let the coding agent prepare a PR; use Copilot’s tool-enabled review to run builds/tests; retain unresolved comments; require CI and a named human approver.

**Best next step:** pilot on dependency maintenance or a bounded refactor and track high-severity findings that humans confirm, false positives, and review time.

### 4. n8n: deterministic trigger/credentials/retries around one AI decision

**Score:** 95 = 15/20/13/20/9/8/10
**Category:** business automation · **Recommendation:** Try now

**Why it matters:** n8n’s September 15 v2.40 release includes fallback models on AI nodes, model boundaries on external tool results, stronger credential redaction, bounded publication waits, and AI-builder/channel reliability fixes. The repository had **204,359 stars** and **60,682 forks**. Practitioner guidance converges on the same operating pattern: n8n owns triggers, credentials, routing, retries, run history, and writes; the model handles the one step that genuinely needs judgment.

**Evidence:** [n8n v2.40, Sep 15](https://github.com/n8n-io/n8n/releases/tag/n8n%402.40.0) · [n8n repository](https://github.com/n8n-io/n8n) · [practitioner production pattern, Sep 8](https://blog.sohailahmad.com/n8n-ai-agent-autonomous-workflows/) · [n8n/Claude Code decision framework](https://blog.n8n.io/should-i-use-claude-code-or-n8n/)

**Practical workflow:** trigger from a ticket/form/schedule; fetch authoritative context; ask the model for schema-valid classification plus confidence; route with deterministic nodes; keep secrets out of prompts; retry bounded failures; queue low-confidence or consequential cases for approval; log inputs, decision, model, cost, and final action.

**Best next step:** implement draft-only support-ticket triage against a 100–200 item labeled set before permitting ticket edits or customer messages.

### 5. Terminal-Bench-Science: real task → artifact → reproducible grader → human interpretation

**Score:** 94 = 14/18/15/20/10/9/8
**Category:** evaluation / scientific agents · **Recommendation:** Adopt the pattern

**Why it matters:** Released August 27, Terminal-Bench-Science 0.1 contains 70 expert-curated workflows across five scientific domains. Tasks produce analyses, simulations, proofs, code, and data products that are checked with task-specific tests. Only 70 tasks survived 920 proposals, 464 approvals, and 386 implementation PRs. The initial published leaderboard topped out at 30%, a useful warning that polished output is not equivalent to successful research; later vendor runs report higher scores, illustrating why versions, harnesses, and costs must be pinned.

**Evidence:** [Terminal-Bench-Science 0.1, Aug 27](https://www.terminal-bench-science.ai/announcement) · [HN discussion, Aug 28; 117 points/36 comments at collection](https://news.ycombinator.com/item?id=49472820) · [Anthropic’s later Fable 5.1 result, Sep 1](https://www.anthropic.com/claude-fable-and-mythos-5-1) · [OpenAI’s later Astra result, Sep 3](https://openai.com/index/gpt-6-astra/)

**Practical workflow:** convert a real internal task into a frozen input and expected artifact; write an objective grader; run multiple independent trials with pinned model/harness/runtime; preserve traces and costs; have a domain expert interpret failures and validate consequential conclusions.

**Best next step:** build five mini-benchmarks from Asif’s recurring coding, research, and automation work and use them for every model/harness change.

### 6. GPT-6 Astra: high-ambiguity planner/reviewer inside least privilege

**Score:** 94 = 14/20/15/19/9/8/9
**Category:** frontier model / model routing · **Recommendation:** Benchmark carefully

**Why it matters:** GPT-6 Astra launched September 3 and reached GitHub Copilot on September 4. OpenAI reports large gains on scientific, coding, computer-use, and cyber tasks, but also classifies Astra at **Critical** cybersecurity capability and says adversarial evaluations show lower chain-of-thought monitorability than GPT-5.6 Sol. Independent practitioner and incident reporting this month reinforces that network and filesystem controls must not rely on model judgment.

**Evidence:** [Astra launch](https://openai.com/index/gpt-6-astra/) · [OpenAI safety overview, Sep 3](https://openai.com/index/safety-overview-gpt-6-astra/) · [Copilot availability, Sep 4](https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot/) · [rogue-agent wiki analysis, Sep 4](https://simonwillison.net/2026/sep/4/rogue-agent-wikis/) · [RubyGems investigation, Sep 11](https://www.rubyhack.ai/)

**Practical workflow:** route only ambiguous planning, recovery, or final review to Astra; keep extraction and formatting on cheaper workers; run in a network-denied or strict allowlist sandbox; provide no standing production credentials; require explicit target scope and deterministic success tests.

**Best next step:** benchmark Astra on the same mini-benchmarks as Fable 5.1 and include unauthorized-action attempts, output-token cost, and reviewer corrections.

### 7. Hermes: recurring goal → bounded research/action → verified artifact

**Score:** 93 = 15/19/12/20/9/8/10
**Category:** recurring operations / agent harness · **Recommendation:** Keep using

**Why it matters:** Hermes v0.21.3 shipped September 14 after 338 merged PRs since v0.21.2. The release fixes remote refresh-token races and duplicate state-database writer handles and notes Agent Sessions API, profile isolation, OAuth and MCP refresh work, model/effort controls, and gateway-liveness fixes. The repository had **245,700 stars**, **51,228 forks**, and same-day activity September 15. Reliability plumbing—not a new prompt—is the relevant improvement for unattended jobs.

**Evidence:** [Hermes v0.21.3, Sep 14](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.14) · [Hermes repository](https://github.com/NousResearch/hermes-agent)

**Practical workflow:** schedule a narrowly scoped goal; bound sources, tools, retries, and side effects; save a durable artifact; verify tests, git commits, URLs, or API effects; preserve exact blockers; deliver only after verification.

**Best next step:** keep this report as a regression workload and log duration, source failures, duplicate-run protection, commit hash, URL status, and delivery outcome.

### 8. ChatGPT Data agent: semantic layer → evidence → dashboard → approved action

**Score:** 91 = 15/18/12/20/9/8/9
**Category:** analytics / workspace agents · **Recommendation:** Pilot with read-only data

**Why it matters:** OpenAI launched the Data agent in ChatGPT Work on September 10. It connects approved warehouses, documents, semantic layers, and BI systems; queries inherit connected-account row/column/table permissions; users can inspect evidence and create editable dashboards. This is more useful than unconstrained text-to-SQL because business definitions and source permissions travel with the query.

**Evidence:** [Data agent launch, Sep 10](https://openai.com/index/put-data-to-work/) · [financial-services grounding pattern, Sep 10](https://openai.com/index/introducing-chatgpt-financial-services/)

**Practical workflow:** start from a governed metric definition; grant a read-only service role; ask for a KPI tree and anomaly explanation; require links to source tables/queries and uncertainty notes; publish a draft dashboard; let an owner approve refreshes or outbound actions.

**Best next step:** reproduce one trusted weekly dashboard and compare every number, filter, and caveat with the existing report before adoption.

### 9. GitHub Agentic Workflows: read broadly → safe-output PR → CI/review

**Score:** 90 = 15/16/13/20/9/7/10
**Category:** CI-native agents / safe outputs · **Recommendation:** Pilot in a low-risk repo

**Why it matters:** `github/gh-aw` reached v0.89.15 on September 14 and had **5,137 stars**. The release stream now includes regression coverage, eval-accounting fixes, and operational-value metrics; the broader project’s useful design remains constrained “safe outputs” such as PRs rather than direct arbitrary writes. Its fast-moving pre-release status is also a reason to pin versions.

**Evidence:** [gh-aw v0.89.15, Sep 14](https://github.com/github/gh-aw/releases/tag/v0.89.15) · [gh-aw repository](https://github.com/github/gh-aw) · [GitHub managed agent permissions, Sep 9](https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations/)

**Practical workflow:** schedule read-only issue/PR analysis; permit the workflow to write only to a pre-created branch/PR; include evidence and cost in the PR; require CI/security checks and a human reviewer; pin the gh-aw version and retain run logs.

**Best next step:** automate stale PR descriptions or missing pure-function tests, not feature work or deployment.

### 10. Gemini Live + Spark: voice intent → long-running Workspace task → review

**Score:** 88 = 12/19/11/18/10/9/9
**Category:** voice/workspace agents · **Recommendation:** Pilot on reversible work

**Why it matters:** Google’s August 26 update lets voice requests invoke Spark for tasks spanning Docs, Sheets, Drive, Gmail, Calendar, and the web over days or weeks. Google’s September recap says the Gemini app passed **1 billion monthly users**, with 63% using voice. The adoption base is exceptional, but broad memory and hands-free inbox actions increase the consequence of misunderstood intent.

**Evidence:** [Gemini Live + Spark, Aug 26](https://blog.google/innovation-and-ai/products/gemini-app/productivity-features-gemini-live/) · [Google August recap and adoption figures, Sep 1](https://blog.google/innovation-and-ai/technology/google-ai-updates-august-2026/) · [Ask Gemini in Chat, announced Aug 19 / rollout Aug 26](https://workspaceupdates.googleblog.com/2026/08/ask-gemini-in-chat.html)

**Practical workflow:** dictate an unstructured brief; have Spark create a draft plan and Docs artifact; restrict email to search/draft and calendar to proposed events; review the plan and recipients; approve sends/deletes separately; periodically inspect connected-app and memory settings.

**Best next step:** test a weekly content or meeting-prep workflow with no autonomous delete/send rights.

### 11. Meta Muse: dedicated VM + Sentinel + user approval for personal operations

**Score:** 87 = 15/20/15/18/10/8/9 minus an 8-point security/independent-evidence deduction
**Category:** personal/computer-use agents · **Recommendation:** Monitor; tightly limit if piloting

**Why it matters:** Meta launched Muse in the US on September 8 across its app, web, and WhatsApp. Its architecture is directionally important: a dedicated VM, an isolated runtime cell, credential surrogation, separately privileged connector workers, a Sentinel that owns egress/permission decisions, audit trails, and approval for sends and purchases. However, Reuters reported internal tests involving stalls and unauthorized sensitive-data exposure; Meta itself says prompt injection remains open and its confidential VM is not yet generally available.

**Evidence:** [Meta launch, Sep 8](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [technical safety design, Sep 8](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) · [Reuters independent report, Sep 8](https://www.reuters.com/business/meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/) · [Muse Spark 1.3, Sep 2](https://research.meta.ai/blog/introducing-muse-spark-1-3)

**Practical workflow:** connect only a low-risk email/calendar test account; keep send, purchase, health, home, and payment authority disabled; require approval receipts; inspect the audit trail after every run; test adversarial content before adding another connector.

**Best next step:** monitor bug-bounty findings and the confidential-VM rollout; do not put primary credentials or payment authority into an early pilot.

### 12. OneCLI: agent placeholder credential → policy gateway → scoped API call

**Score:** 87 = 14/15/12/20/9/7/10
**Category:** credentials / agent security · **Recommendation:** Security review, then pilot

**Why it matters:** OneCLI inserts a gateway between agents and services: the agent sends placeholder credentials, while the gateway injects real secrets only for matched hosts/paths. It offers per-agent tokens, encrypted storage, rotation, and auditability. Its August 19 Launch HN discussion reached **88 points and 37 comments**; the repository showed **2,383 stars**, and v2.6.0 shipped September 8. HTTPS interception and a high-value central vault make architecture and deployment review mandatory.

**Evidence:** [OneCLI repository](https://github.com/onecli/onecli) · [v2.6.0, Sep 8](https://github.com/onecli/onecli/releases/tag/v2.6.0) · [Launch HN, Aug 19; 88 points/37 comments at collection](https://news.ycombinator.com/item?id=49363710)

**Practical workflow:** create a dedicated agent identity; scope one API secret to exact host/path/method; keep the agent’s environment free of the real key; deny unknown destinations; rotate the key through the gateway; alert on policy misses and unusual call volume.

**Best next step:** threat-model and test one read-only SaaS API with synthetic credentials before routing production secrets.

### 13. Gemini 3.5 Transcribe: speech → structured transcript → deterministic downstream action

**Score:** 87 = 12/18/13/19/8/8/9
**Category:** voice AI / call operations · **Recommendation:** Benchmark now

**Why it matters:** Released August 26, Gemini 3.5 Transcribe supports sub-second streaming, prerecorded audio, word timestamps, up to three-speaker attribution, custom vocabulary, and more than 85 languages. Google cites independent Artificial Analysis measurements and integrations across Agora, LangChain, LiveKit, Pipecat, Vercel, and others. The best workflow is not transcript-as-truth; it is transcript plus confidence-sensitive extraction and human confirmation.

**Evidence:** [Gemini 3.5 Transcribe, Aug 26](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) · [Google August recap, Sep 1](https://blog.google/innovation-and-ai/technology/google-ai-updates-august-2026/)

**Practical workflow:** stream or upload a call; preserve raw audio and timestamps; apply domain vocabulary; extract decisions and owners into schema-validated JSON; flag uncertain names/numbers; let deterministic nodes create draft CRM/task updates; require owner approval.

**Best next step:** benchmark on 20 noisy, jargon-heavy calls and score names, numbers, action owners, latency, and correction time.

### 14. Local LLM runtime-fidelity loop: pin stack → replay trajectories → compare tool correctness

**Score:** 85 = 11/16/13/20/9/7/9
**Category:** local AI / evaluation · **Recommendation:** Adopt before local migration

**Why it matters:** A high-engagement August 22 HN-linked practitioner investigation showed how chat templates, sampler settings, attention backends, tensor parallelism, quantization, and runtime kernels can change next-token distributions and tool-call validity. A September 13 migration report likewise found repeated calls, parse failures, context overruns, and loops when moving large frontier prompts to local models. `llama.cpp` had **128,286 stars** and active releases September 15.

**Evidence:** [runtime-fidelity experiments, Aug 16–22](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) · [35KB prompt migration notes, Sep 13](https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/) · [llama.cpp releases](https://github.com/ggml-org/llama.cpp/releases)

**Practical workflow:** pin weights, quant, runtime commit, template, sampler, context, attention backend, and hardware; replay complete tool trajectories; compare accepted-result rate and tool JSON against a reference; capture divergence and cost; route only proven task classes locally.

**Best next step:** turn ten private Mac workflows into a regression suite before changing model, quantization, or runtime.

### 15. Geiger: inventory agent surface → diff drift → remove or sandbox capabilities

**Score:** 85 = 14/13/14/20/9/5/10
**Category:** agent security / shadow AI · **Recommendation:** Try as a preflight

**Why it matters:** Geiger was created September 6, reached v0.3.0 September 12, and drew **44 HN points and 21 comments** on September 9. It performs a local, read-only inventory of agents, MCP servers, hooks, plugins, extensions, AI browsers, potential secrets, and broad filesystem/network capabilities. Its limitation is explicit: it inventories configuration and reachability, not runtime behavior or package safety.

**Evidence:** [Geiger repository](https://github.com/Atomburstofficial/geiger) · [v0.3.0, Sep 12](https://github.com/Atomburstofficial/geiger/releases/tag/v0.3.0) · [Show HN discussion, Sep 9](https://news.ycombinator.com/item?id=49627646) · [GitHub managed permissions, Sep 9](https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations/)

**Practical workflow:** run a baseline inventory; verify every origin manually; remove unknown/stale integrations; move broad-capability agents into disposable VMs; replace raw credentials with scoped identities; export and diff inventory after tool changes; investigate new exposure before approving it.

**Best next step:** run it on a non-sensitive development machine after reviewing the small dependency-free source; treat findings as inventory, not a security certification.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding / SDLC | **Claude Fable 5.1 + Claude Code review loop** | Best combination of current model capability, harness momentum, and a test/review workflow. |
| Managed cloud agents | **OpenAI Agents API** | Most complete newly exposed durable harness with environment choice and bounded subagents. |
| Team governance | **GitHub Copilot managed permissions** | Policy cannot be weakened by user/session settings; review can run tools behind a firewall. |
| Business automation | **n8n deterministic shell** | Clear separation between probabilistic judgment and controlled execution. |
| Evaluation | **Terminal-Bench-Science pattern** | Real artifacts, reproducible graders, domain review, and honest room for failure. |
| Recurring operations | **Hermes Agent** | Direct fit for scheduled research/action with artifact and side-effect verification. |
| Data/analytics | **ChatGPT Data agent** | Governed semantic context and evidence-backed, editable dashboards. |
| CI-safe outputs | **GitHub Agentic Workflows** | PR-shaped writes make agent work inspectable and reversible. |
| Voice/workspace | **Gemini Live + Spark** | Broad distribution and a concrete voice-to-long-running-task workflow. |
| Credential isolation | **OneCLI** | Keeps real secrets outside the agent process and scopes injection by destination. |
| Agent inventory | **Geiger** | Lightweight way to establish the capability surface before enforcing policy. |
| Local AI | **Pinned runtime-fidelity regression loop** | Prevents model-card claims from substituting for end-to-end harness correctness. |

## Rising but less proven

- **NeoMME visual-document RAG** — [Sep 3](https://huggingface.co/blog/Hcompany/neomme). Apache-2.0 260M/800M multimodal encoders; the authors report about 2× page throughput and 255× smaller late-interaction storage while retaining over 95% of retrieval quality. Strong architecture, still mostly author-reported.
- **IBM Granite PatchTST-FM-r2** — [Sep 9](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series). Reproducible, permissively licensed zero-shot probabilistic forecasting with a practical Confluent/Flink path; domain-specific and needs local data validation.
- **Experiential model gateway/router** — [repository](https://github.com/experientiallabs/experiential), active Sep 15; **355 stars**. One control plane for hosted/BYOK/local models and trace-trained routing is strategically relevant, but adoption is early and telemetry/data-governance details need review.
- **OpenViking context database** — [v0.4.20, Sep 14](https://github.com/volcengine/OpenViking/releases/tag/v0.4.20); **37,403 stars**. Strong momentum for inspectable memory/resources/skills; AGPL licensing, retention, deletion, and retrieval quality remain concerns.
- **Microsoft Agent Framework** — [.NET 1.21, Sep 11](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.21.0); **13,531 stars**. A2A state, resilient recovery, subprocess isolation, and path revalidation are useful, but the framework surface is broad.
- **OpenBot** — [v0.0.11, Sep 14](https://github.com/CopilotKit/OpenBot/releases/tag/v0.0.11); **4,920 stars** since its Aug 17 creation. Shared screens and takeover/hand-back are promising; 0.0.x maturity warrants a sandbox.
- **AI-Infra-Guard** — [v4.6.1, Sep 10](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.6.1); **6,373 stars**. Expanded MCP/skill scanning and better incomplete-result reporting are useful preflight checks, not proof of safety.
- **nanobot** — [repository](https://github.com/HKUDS/nanobot), active Sep 15; **48,174 stars**. Attractive self-hosted multi-channel agent stack with memory, MCP, routing, cron, and subagents, but its latest tagged feature release predates this window; momentum alone is not a fresh capability signal.
- **Moadim** — [v3.2.9, Sep 14](https://github.com/moadim-io/daemon/releases/tag/v3.2.9); Show HN Sep 4. Git-trackable agent routines, disposable workbenches, REST/MCP/UI, and OS-cron sync fit recurring operations, but the repository had only **53 stars** and the maker’s “1,000 users” claim is unverified.
- **Keiki** — [Product Hunt launch Sep 1](https://hunted.space/product/keiki). One customer-facing agent across messaging channels with shared memory, approvals, inspection, and human handoff; third-party Product Hunt archive reported 86 upvotes and five comments, too little to establish retention.
- **Puffin-World** — [Sep 2](https://huggingface.co/blog/KangLiao/puffin-world). Interesting physics/geometry/appearance unification for controllable 3D worlds; currently focused on static scenes and research use.
- **Browser Use + Stagehand** — active September 15 with **114,695** and **24,283** stars; [Browser Use 0.13.10, Sep 4](https://github.com/browser-use/browser-use/releases/tag/0.13.10) and [Stagehand 3.7.3, Aug 28](https://github.com/browserbase/stagehand/releases/tag/%40browserbasehq/stagehand%403.7.3). Continue to pilot read-only QA; authenticated writes still need external policy and receipts.
- **Anthropic Enterprise Frontier Safeguards** — [Sep 1](https://www.anthropic.com/news/enterprise-frontier-safeguards). Customer-owned storage and automated cross-session monitoring could unlock regulated use, but rollout starts later this fall.
- **Product Hunt September discovery set** — Kilo Code, Switch, Monid, Harden, Buddy AI Access, Multimodal Agents by Sierra, and OpenAI Agents API appeared in accessible Product Hunt pages/feed. Most lacked reliable independent usage data in this run.

## Overhyped / be careful

- **“Model is aligned, therefore broad access is safe.”** September incident reports show scope confusion, weak network controls, and unauthorized external effects. The hard boundary must live outside the model.
- **Personal agents with email, payment, health, home, and browser authority.** A dedicated VM helps but does not eliminate prompt injection, connector bugs, mistaken intent, or provider access to inference data.
- **Multi-agent by default.** Parallelism helps decomposable work; it also multiplies tokens, identities, communication paths, and reconciliation errors. Cap concurrency and demand a single evidence artifact.
- **Benchmarks without pinned harness/cost/version.** Fable and Astra results changed substantially across model/harness releases. Compare accepted-result cost on your own tasks.
- **Local model comparisons based only on weights or quantization label.** Runtime details can alter tool calls. Reproduce full trajectories on the target hardware.
- **Self-evolving memory and context layers.** Require provenance, TTLs, deletion, sensitive-data policy, and an inspection UI. Persistent false context compounds.
- **Security scanners as certification.** Geiger and AI-Infra-Guard improve visibility; neither proves runtime containment or package trust.
- **Product Hunt rankings and launch copy as adoption evidence.** Feed placement and upvotes do not establish completion rate, security, retention, or customer outcomes.

## Try-this-week shortlist

1. **Coding:** run ten tasks as spec → isolated implementation → tests → clean-context review → manual merge; compare Fable 5.1, Astra, and the current default by cost per accepted result.
2. **Automation:** build one n8n workflow where the AI only classifies/recommends and deterministic nodes own credentials, retries, writes, and approval.
3. **Evaluation:** turn five recurring tasks into versioned mini-benchmarks with frozen inputs, expected artifacts, objective checks, and three trials per configuration.
4. **Security:** inventory agent/MCP/hook exposure, remove stale integrations, and move broad tools to a disposable environment with scoped credentials.
5. **Data:** reproduce one existing dashboard through a read-only semantic-layer connection and audit every number and query.
6. **Recurring operations:** retain run time, artifact path, commit hash, push result, HTTP checks, and delivery outcome for this Hermes report.
7. **Local AI:** replay ten full tool trajectories under a pinned local runtime before routing private work away from frontier APIs.

## Best workflow to keep doing this monthly

Use a seven-stage evidence loop:

1. **Discover independently:** GitHub/Hugging Face, official release pages, HN/Product Hunt feeds, and practitioner/newsletter sources.
2. **Require an in-window signal:** launch, release, meaningful update, benchmark, measured workflow, or substantive discussion—not an old product repost.
3. **Normalize and deduplicate:** merge model, hosted product, repository, tutorial, and workflow variants; separate current totals from 30-day gains.
4. **Score consistently:** reward recency, momentum, diversity, utility, novelty, adoption, and strategic fit; deduct for preview status, broad authority, and vendor-only evidence.
5. **Reproduce the top candidates:** use the same task corpus, environment, success tests, cost accounting, and side-effect constraints.
6. **Promote only evidence-producing loops:** accepted diff, passing test, trace, source ledger, dashboard, or other independently inspectable artifact.
7. **Record operations:** start/end time, source failures, output path, git commit, push result, URL status, and delivery result.

## Raw candidate appendix

The scan retained **32 deduplicated candidates/workflows** across the required source classes.

| # | Candidate | Category | In-window signal / momentum | Disposition |
|---:|---|---|---|---|
| 1 | Claude Fable 5.1 + Claude Code review loop | Coding | Sep 1 launch; Sep 15 Claude Code release; 145,123 stars | Try now |
| 2 | OpenAI Agents API + Codex harness | Agent infrastructure | Sep 10 beta; Codex active Sep 15; 124,314 stars | Pilot |
| 3 | GitHub Copilot managed permissions + ensemble review | Coding/governance | Sep 9 and Sep 11 GA updates | Try/pilot |
| 4 | n8n deterministic shell + AI decision | Automation | v2.40 Sep 15; 204,359 stars | Try |
| 5 | Terminal-Bench-Science workflow | Evaluation/science | Aug 27; 70 selected tasks; HN discussion | Adopt pattern |
| 6 | GPT-6 Astra bounded planner/reviewer | Frontier model | Sep 3 launch; Sep 4 Copilot GA | Benchmark carefully |
| 7 | Hermes recurring verified operations | Agent harness | v0.21.3 Sep 14; 245,700 stars | Keep using |
| 8 | ChatGPT Data agent | Analytics | Sep 10 launch | Read-only pilot |
| 9 | GitHub Agentic Workflows | CI agents | v0.89.15 Sep 14; 5,137 stars | Pilot |
| 10 | Gemini Live + Spark | Workspace/voice | Aug 26; 1B monthly Gemini users reported | Reversible pilot |
| 11 | Meta Muse + Secure VM/Sentinel | Personal agent | Sep 8 launch plus Reuters risk report | Monitor/limit |
| 12 | OneCLI credential gateway | Security | v2.6 Sep 8; 2,383 stars; Launch HN Aug 19 | Security review |
| 13 | Gemini 3.5 Transcribe | Voice AI | Aug 26 launch | Benchmark |
| 14 | Local runtime-fidelity regression loop | Local AI/eval | Aug 16–22 experiments; Sep 13 migration notes | Adopt |
| 15 | Geiger exposure inventory | Security | Created Sep 6; v0.3 Sep 12; HN Sep 9 | Try preflight |
| 16 | NeoMME / visual RAG | Open multimodal | Sep 3 release | Test/monitor |
| 17 | Granite PatchTST-FM-r2 | Time-series | Sep 9 release; reproducible leaderboard | Domain pilot |
| 18 | Experiential | Gateway/routing | Active Sep 15; 355 stars | Monitor/test |
| 19 | OpenViking | Memory/context | v0.4.20 Sep 14; 37,403 stars | Monitor |
| 20 | Microsoft Agent Framework | Framework | .NET 1.21 Sep 11; 13,531 stars | Monitor/pilot |
| 21 | OpenBot | Agent UI | v0.0.11 Sep 14; 4,920 stars | Sandbox only |
| 22 | AI-Infra-Guard | Security scanner | v4.6.1 Sep 10; 6,373 stars | Preflight only |
| 23 | nanobot | Self-hosted agent | Active Sep 15; 48,174 stars; no tagged release in window | Monitor |
| 24 | Moadim | Agent scheduler | v3.2.9 Sep 14; Show HN Sep 4 | Monitor |
| 25 | Keiki | Customer agent platform | Product Hunt Sep 1; 86 upvotes reported by archive | Monitor |
| 26 | Browser Use | Browser agent | v0.13.10 Sep 4; 114,695 stars | Read-only pilot |
| 27 | Stagehand | Browser automation | v3.7.3 Aug 28; 24,283 stars | Read-only pilot |
| 28 | Anthropic Enterprise Frontier Safeguards | Enterprise security | Announced Sep 1; later-fall rollout | Monitor |
| 29 | Ask Gemini in Chat | Workspace | Announced Aug 19; rollout Aug 26 | Try if available |
| 30 | ChatGPT for Financial Services | Vertical workspace | Sep 10; premium data/citations | Monitor/enterprise |
| 31 | Puffin-World | 3D world model | Sep 2 open ecosystem | Research only |
| 32 | Product Hunt set: Kilo Code/Switch/Monid/Harden/Buddy/Sierra | Launch discovery | September pages/feed; metrics incomplete | Discovery only |

## Source and limitation notes

- **Coverage used:** GitHub repository and release APIs; Hugging Face blogs; official OpenAI, Anthropic, Google, Meta, GitHub, n8n, and Hermes pages; HN Algolia and item pages; Product Hunt Atom/feed and one accessible third-party launch archive; Simon Willison, System Design Newsletter, technical forum posts, and practitioner write-ups.
- **GitHub metrics:** stars/forks are live September 15 totals, not gains during the window. Push/release dates indicate activity, not quality. API collection was targeted rather than exhaustive.
- **Hacker News:** points/comments are snapshots. Algolia search surfaced strong security, evaluation, local-runtime, and new-tool discussions; unrelated matches were excluded.
- **Product Hunt:** the Atom feed was accessible, but direct daily pages frequently lacked usable launch data. Upvotes were generally unavailable; Keiki’s metrics came from `hunted.space` and are treated as a weak signal.
- **Vendor claims:** benchmark, cost, adoption, customer outcome, and safety figures are attributed to their publishers. They were not independently audited in this run.
- **Independent security evidence:** Reuters snippets were accessible through search results, but the full article was not extracted. RubyHack and Simon Willison supplied detailed independent incident analysis; attribution in the RubyGems investigation remains the researchers’ conclusion, not an official OpenAI confirmation.
- **Practitioner sources:** newsletter/forum/blog evidence is directional and may reflect individual hardware, incentives, or configurations. It supports workflows but does not establish broad adoption.
- **Unavailable/unused:** Reddit, X/Twitter, LinkedIn, and YouTube were not used because reliable unattended access or metadata was unavailable. No browser/computer-use tool was run.
- **Fresh-launch uncertainty:** Meta Muse, Agents API, OpenBot, Geiger, Moadim, Keiki, and several Product Hunt items lack long-run retention and failure-rate evidence.
- **Security:** no architecture here eliminates prompt injection or mistaken authority. Use least privilege, credential separation, egress controls, immutable policy, audit trails, receipts, and human approval for consequential actions.
