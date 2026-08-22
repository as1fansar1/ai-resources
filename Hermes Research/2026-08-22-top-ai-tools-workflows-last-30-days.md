# Top AI tools and workflows — last 30 days

Research date: **2026-08-22 11:13:08 EDT (UTC-04:00)**
Window: **2026-07-23 11:13:08 EDT through 2026-08-22 11:13:08 EDT** (rolling preceding 30 days)
Scope: coding agents, browser/computer use, agent infrastructure, research, business automation, workspace agents, local/open models, observability, memory, and security.

## Executive summary

The clearest change in this window is that AI products are moving from single prompts to **persistent operating loops**. The strongest systems now combine a durable goal, isolated execution, event triggers, skills, scoped tools, memory, observability, and a reviewable artifact. The useful unit is no longer “the best model”; it is a controlled workflow that can resume, prove what it did, and stop before a consequential action.

Five signals matter most:

1. **Coding agents are becoming event-driven workers.** Claude Code added cross-session messaging, self-hosted cloud runners, worktree isolation, and safer execution defaults; Cursor added subscriptions, long-lived goals, prepared environments, isolated subagent VMs, and PR/CI follow-through.
2. **Browser automation is becoming a production API, but approval remains essential.** Anthropic made computer use, browser use, Skills API, and Files API generally available on August 20. Browser Use and Stagehand provide strong open-source momentum, but logged-in sessions still amplify prompt-injection and credential risks.
3. **Agents are becoming reusable organizational objects.** n8n Agents can be defined once, versioned, scheduled, connected to Slack/Telegram/Linear, called by workflows, and given workflows as tools. Confluence and Rovo apply the same pattern to governed knowledge work.
4. **Evidence and traces are first-class outputs.** Cloudflare Agent Tracing records models, tools, approvals, subagents, tokens, and costs. Hugging Face’s ICML reproduction project showed a stronger research pattern: agent-produced experiment, public logbook, independent judge, and human review.
5. **Local agents gained credible multimodal and latency options.** Meta Muse Glimmer brought a 30B Apache-2.0 multimodal agent model with day-zero llama.cpp/vLLM support; LFM2.5 DSpark reported large speculative-decoding gains, including lower function-call latency.

**Bottom line:** try event-driven coding on low-risk repositories, a reusable n8n agent inside a deterministic workflow shell, and end-to-end tracing now. Pilot browser and workspace writes only with isolated identities, explicit action gates, and receipts. Monitor new “agent OS” launches until they show independent reliability evidence.

## Scoring methodology

Scores use the requested 100-point rubric: **recency 15, momentum 20, source diversity 15, practical utility 20, workflow novelty 10, adoption evidence 10, strategic relevance to Asif 10**. Components are shown in that order. Totals were calculated programmatically.

Deductions are reflected for vendor-only benchmarks, preview/beta availability, single-source virality, broad permissions, missing independent outcomes, and claims that autonomy itself is a benefit. GitHub stars are live snapshots collected **August 22, 2026**; they are not 30-day star gains. GitHub `pushed_at` and release dates demonstrate activity, not quality.

## Top ranked tools/workflows

| Rank | Tool / workflow | Score | Recommendation |
|---:|---|---:|---|
| 1 | Claude Code multi-session planning → isolated worktree → tested PR | 96 | **Try now** |
| 2 | Cursor event subscription → long-lived goal → PR/CI follow-through | 94 | **Pilot now** |
| 3 | Supervised browser operations: files/skills → structured browser → receipt → approval | 94 | **Pilot carefully** |
| 4 | n8n reusable agent inside a deterministic workflow shell | 92 | **Try in preview on one internal process** |
| 5 | ChatGPT Work connected research → reviewed artifact | 92 | **Try now** |
| 6 | Agent experiment → public logbook → independent judge → human review | 91 | **Adopt for high-value claims** |
| 7 | Perplexity Agent API cited-research pipeline | 90 | **Try now / migrate Sonar** |
| 8 | Gemini 3.7 Flash planner + cheaper bounded workers | 89 | **Benchmark now** |
| 9 | Confluence Agents + Rovo MCP governed knowledge workflow | 88 | **Try now** |
| 10 | Cloudflare Agent Tracing → replay → regression/eval loop | 87 | **Try now** |
| 11 | Muse Glimmer local multimodal agent with llama.cpp/vLLM | 86 | **Benchmark locally** |
| 12 | Hermes Agent recurring research/operations with persistent job memory | 85 | **Try for recurring bounded work** |
| 13 | n8n + Bedrock AgentCore specialist team with actor-scoped memory | 84 | **Pilot on internal support** |
| 14 | GitHub Agentic Workflows scheduled task → final PR → CI/review | 83 | **Pilot in a low-risk repo** |
| 15 | `/wayfinder` map → tickets → parallel research/prototypes → reconciled plan | 82 | **Try on ambiguous projects** |

## Detailed findings

### 1. Claude Code multi-session planning → isolated worktree → tested PR

**Score:** 96 = 15/20/14/20/9/9/9
**Category:** coding agents · **Recommendation:** Try now

**Why it matters:** Claude Code’s August stream turned parallel sessions into a more coherent engineering system. Sessions can message each other without copying full histories; cloud sessions can run on self-hosted infrastructure; `/fork` uses a separate worktree; background sessions can commit and push; worktree boundaries now cover Bash and git redirects. The repository had **142,393 stars** and was pushed on August 22 at collection.

**Evidence:** [Week 32 product notes, Aug 3–7](https://code.claude.com/docs/en/whats-new/2026-w32) · [cross-session messaging HN discussion, Aug 8](https://code.claude.com/docs/en/cross-session-messaging) · [v2.1.240, Aug 22](https://github.com/anthropics/claude-code/releases/tag/v2.1.240) · [session-practice discussion, Aug 14](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions)

**Practical workflow:** assign one session architecture and acceptance criteria; give implementation and test sessions separate worktrees; pass only decisions and changed contracts between sessions; have a clean-context reviewer inspect the diff; run CI/security checks; merge manually.

**Best next step:** use this on one contained refactor and measure review corrections, conflicts, test failures, and elapsed time versus one long session.

### 2. Cursor event subscription → long-lived goal → PR/CI follow-through

**Score:** 94 = 15/18/13/20/10/8/10
**Category:** coding agents / developer operations · **Recommendation:** Pilot now

**Why it matters:** Cursor’s August 19 release lets cloud agents subscribe to PRs, Slack threads, and schedules; `/goal` holds a long-lived objective; subagents run on isolated VMs; and follow-up steering waits for tool boundaries rather than interrupting mid-action. August 13 prepared builds reduce environment setup, while Origin’s August 17 beta puts code, PRs, reviews, and agents in one surface.

**Evidence:** [Cursor changelog, Aug 13, 17, and 19](https://cursor.com/changelog) · [Origin listed in August Product Hunt ranking](https://hunted.space/top-products/monthly/2026/August)

**Practical workflow:** subscribe an agent to a flaky-test PR; give it `/goal make CI green without changing public behavior`; pin a review skill as a custom mode; let isolated subagents reproduce failures; require a human review before merge and keep deployment outside scope.

**Best next step:** pilot on test stabilization or dependency maintenance, not feature work with unclear product intent.

### 3. Supervised browser operations: files/skills → structured browser → receipt → approval

**Score:** 94 = 15/19/14/19/9/9/9
**Category:** browser/computer-use agents · **Recommendation:** Pilot carefully

**Why it matters:** On August 20 Anthropic made computer use, browser use, Skills API, and Files API generally available. The browser tool combines page structure with visual operation and supports multiple actions per turn. Browser Use had **110,091 stars** with an August 16 release; Stagehand had **24,020 stars** and was pushed August 22. This is a strong convergence around structured observation plus deterministic steps, not pixel-only clicking.

**Evidence:** [Claude production-agent APIs, Aug 20](https://claude.com/blog/computer-use-skills-api-files-api) · [Browser Use 0.13.8, Aug 16](https://github.com/browser-use/browser-use/releases/tag/0.13.8) · [Stagehand repository, active Aug 22](https://github.com/browserbase/stagehand) · [Docker agent sandboxes HN discussion, Aug 10](https://www.docker.com/products/docker-sandboxes/)

**Practical workflow:** upload the intake file once; attach a versioned procedure skill; use a fresh browser identity restricted to named domains; extract/prepare before acting; capture screenshots, fields, and confirmations; stop before submit, publish, payment, deletion, or customer impact; obtain explicit approval.

**Best next step:** automate read-only QA or form preparation before allowing any authenticated write.

### 4. n8n reusable agent inside a deterministic workflow shell

**Score:** 92 = 14/19/13/20/9/8/9
**Category:** business automation · **Recommendation:** Try in preview on one internal process

**Why it matters:** n8n Agents are reusable, publishable objects with tools, skills, knowledge, memory, channels, schedules, and subagents. The same agent can be messaged from Slack/Telegram/Linear, run on a schedule, call existing workflows, or be called by a workflow. n8n had **201,639 GitHub stars** and shipped a stable release August 21.

**Evidence:** [n8n Agents launch, Aug 5; updates through Aug 20](https://community.n8n.io/t/introducing-n8n-agents-a-new-way-to-build-agents-you-set-up-once-and-use-anywhere/306323) · [approval-first practitioner guide reviewed Aug 7](https://christopheralarcon.com/blog/n8n-ai-agent-tutorial) · [n8n GitHub](https://github.com/n8n-io/n8n)

**Practical workflow:** keep triggers, credentials, retries, logging, and risky writes in deterministic n8n nodes; give the agent one scoped decision and a small tool set; require structured output; route low-confidence or consequential actions to approval; publish only after replaying real test cases.

**Best next step:** build a daily unassigned-ticket triage that posts recommendations to Slack but cannot edit or message customers.

### 5. ChatGPT Work connected research → reviewed artifact

**Score:** 92 = 13/18/14/20/9/9/9
**Category:** research / productivity · **Recommendation:** Try now

**Why it matters:** Practitioner analysis shows ChatGPT Work combining connected context, scheduling, browser use, plugins, skills, files, and cloud execution into finished artifacts. OpenAI’s August 21 GPT-5.6 Sol price reduction improves the economics of long research runs. The durable pattern is source systems → cited analysis → editable report/sheet/deck → human review.

**Evidence:** [Latent Space hands-on reconstruction, Aug 4](https://www.latent.space/p/unpacking-chatgpt-work) · [OpenAI GPT-5.6 page updated Aug 21](https://openai.com/index/gpt-5-6/) · [education workflow plugins, Aug 4](https://openai.com/index/learn-teach-chatgpt-work-codex/)

**Practical workflow:** define a recurring brief and output template; connect only required read scopes; require claim-level citations and a source ledger; verify calculations and quoted text; approve sharing separately; retain corrections as a versioned skill rather than an ever-growing prompt.

**Best next step:** produce one weekly competitor brief and score unsupported claims, source quality, human edits, cost, and delivery time.

### 6. Agent experiment → public logbook → independent judge → human review

**Score:** 91 = 14/17/15/19/9/9/8
**Category:** research / evaluation · **Recommendation:** Adopt for high-value claims

**Why it matters:** Hugging Face’s ICML challenge produced **6,816 logbooks across 2,226 papers**, judged **35,908 claims**, launched **2,962 jobs**, and involved **1,221 people**. Every run could retain code, artifacts, and traces. The judge treated each agent’s self-assessment as untrusted, and conflicting results were escalated rather than averaged away.

**Evidence:** [Hugging Face results, Aug 13](https://huggingface.co/blog/icml-2026-open-reproductions)

**Practical workflow:** decompose a claim into executable checks; let an agent write and run the experiment; freeze environment, code, logs, artifacts, costs, and trace; have a separate model judge each claim; send contested or consequential conclusions to a domain expert.

**Best next step:** apply this to one vendor benchmark or internal ROI claim before making an architecture or purchasing decision.

### 7. Perplexity Agent API cited-research pipeline

**Score:** 90 = 14/17/13/19/9/8/10
**Category:** research infrastructure · **Recommendation:** Try now; migrate Sonar

**Why it matters:** The August 13 Agent API combines web search, URL fetch, code sandboxing, MCP, finance search, and people search through one endpoint and six presets. Existing Sonar tiers retire on **September 27, 2026**, creating an actionable migration deadline.

**Evidence:** [official Agent API launch, Aug 13](https://www.perplexity.ai/hub/blog/agent-api-one-place-to-build-with-llms-the-web-and-agents) · [practitioner MCP research architecture, Aug 10](https://newsletter.systemdesign.one/p/how-to-build-an-ai-research-agent-with-mcp)

**Practical workflow:** map Sonar tier to preset; decompose the brief; retrieve primary sources; use code for structured comparison; synthesize with claim-level citations; run a separate citation verifier; cap retrieval steps, tool calls, latency, and spend.

**Best next step:** migrate one Sonar workload in staging and compare source coverage, citation correctness, cost, and latency.

### 8. Gemini 3.7 Flash planner + cheaper bounded workers

**Score:** 89 = 15/17/11/19/8/9/10
**Category:** models / agent routing · **Recommendation:** Benchmark now

**Why it matters:** Released August 13, Gemini 3.7 Flash targets coding and agents at an introductory **$0.75/M input and $3.75/M output tokens** through year-end. Google reports sizable gains over 3.6 Flash on software, document, and automation benchmarks, and deployed it into Gemini Spark across more than 160 countries.

**Evidence:** [official launch, Aug 13](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) · [Managed Agents hooks, budgets, and schedules, Jul 28](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/)

**Practical workflow:** route ambiguous planning and recovery to 3.7 Flash; route extraction/classification to a cheaper worker; enforce sandbox hooks and total-token budgets; log per-tool-loop success; escalate only defined failures.

**Best next step:** run a 100-task evaluation from Asif’s real research and automation workloads before changing defaults.

### 9. Confluence Agents + Rovo MCP governed knowledge workflow

**Score:** 88 = 13/16/12/19/8/10/10
**Category:** workspace agents · **Recommendation:** Try now

**Why it matters:** Confluence agents can create, edit, comment, label, set status, and create whiteboards/databases in the live workspace or through Rovo MCP. Atlassian reports **more than 5 million invocations per month** and **200,000 customer hours saved in February**. Existing permissions, agent analytics, stale-edit rejection, and version history provide stronger governance than copied context in chat.

**Evidence:** [Atlassian launch and usage disclosure, Aug 10](https://www.atlassian.com/blog/confluence/new-agents-in-confluence)

**Practical workflow:** have an agent draft release notes from merged PRs; preserve sources and ownership; reject stale writes; inspect agent reads/writes in analytics; require a named owner to approve publishing or public sharing.

**Best next step:** begin with reversible internal release notes or onboarding FAQs.

### 10. Cloudflare Agent Tracing → replay → regression/eval loop

**Score:** 87 = 13/15/13/20/8/8/10
**Category:** observability · **Recommendation:** Try now

**Why it matters:** Agent tracing records model calls, tool executions, approvals, subagents, tokens, costs, and infrastructure spans. Session replay exposes failures hidden behind HTTP 200 responses. OpenTelemetry export supports a portable evaluation loop.

**Evidence:** [Cloudflare Agents and tracing, Aug 4](https://blog.cloudflare.com/agents-on-cloudflare/)

**Practical workflow:** trace a bounded production-like agent; turn off sensitive message/tool payload capture where needed; label the expected tool and approval sequence; replay failures; create regression cases; monitor retries, unsafe write attempts, latency, and cost.

**Best next step:** instrument one agent before expanding its permissions. Note that tracing moves into Workers Observability pricing October 1.

### 11. Muse Glimmer local multimodal agent with llama.cpp/vLLM

**Score:** 86 = 14/18/14/17/8/8/7
**Category:** local/open models · **Recommendation:** Benchmark locally

**Why it matters:** Meta’s Muse Glimmer is a 30B Apache-2.0 multimodal model for local agent workflows with day-zero Transformers, llama.cpp, and vLLM support. Its launch drew **1,208 HN points and 639 comments**. Hugging Face showed about **518,000 model downloads** for the primary 30B entry at extraction.

**Evidence:** [Hugging Face launch, Aug 10](https://huggingface.co/blog/muse-glimmer) · [Meta launch discussion on HN, Aug 10](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) · [llama.cpp current release stream](https://github.com/ggml-org/llama.cpp/releases)

**Practical workflow:** pin the model hash and runtime; bind the endpoint locally; evaluate document/screenshot understanding and tool-call JSON; delegate privacy-sensitive extraction or first-pass review; retain a frontier model for difficult planning and escalation.

**Best next step:** benchmark on ten private document and UI tasks using the exact quantization and hardware intended for production.

### 12. Hermes Agent recurring research/operations with persistent job memory

**Score:** 85 = 15/18/10/18/9/7/8
**Category:** agent harness / recurring operations · **Recommendation:** Try for recurring bounded work

**Why it matters:** Hermes Agent v0.20.5 was published August 21 and rolls up about **323 PRs** since v0.20.4, including runtime stall guards, update verification receipts, worktree management, and cron jobs with persistent memory and per-job reasoning effort. The repository had **234,260 stars** and was pushed August 22 at collection.

**Evidence:** [v0.20.5 release, published Aug 21](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.19) · [GitHub repository](https://github.com/NousResearch/hermes-agent)

**Practical workflow:** define a narrow scheduled job with bounded sources and tools; retain only useful job memory; write an auditable artifact; verify side effects such as commits and URLs; surface exact blockers instead of retrying indefinitely.

**Best next step:** keep this research cron as the proving workload and track completion, duration, duplicate runs, publication verification, and delivery failures.

### 13. n8n + Bedrock AgentCore specialist team with actor-scoped memory

**Score:** 84 = 15/13/13/18/9/7/9
**Category:** customer operations / multi-agent · **Recommendation:** Pilot on internal support

**Why it matters:** An August 20 n8n/AWS workflow shows a concrete four-agent support team sharing one AgentCore harness and memory scoped by actor/session. n8n owns trigger, routing, and reply; AgentCore owns isolated execution and durable memory. Tools can be granted per invocation rather than permanently attached to every specialist.

**Evidence:** [n8n/AWS implementation guide, Aug 20](https://blog.n8n.io/node-spotlight-amazon-bedrock-agentcore/)

**Practical workflow:** classify a ticket; route to one specialist; pass a stable customer/account actor ID; give only the tool required for that invocation; draft a response; require support review; set retention and deletion rules for memory.

**Best next step:** test on an internal help channel with synthetic customer identifiers and no outbound customer messaging.

### 14. GitHub Agentic Workflows scheduled task → final PR → CI/review

**Score:** 83 = 15/12/13/18/8/8/9
**Category:** CI-native coding agents · **Recommendation:** Pilot in a low-risk repo

**Why it matters:** `github/gh-aw` continues to harden secret redaction, artifact roots, URL logging, diagnostics, and read-only-until-final-PR behavior. The August 10 PureLock example ran scheduled coverage work three times, stayed read-only until the final PR, and produced tests for review. v0.87.4 shipped August 22.

**Evidence:** [weekly update, Aug 10](https://github.github.com/gh-aw/blog/2026-08-10-weekly-update/) · [v0.87.4, Aug 22](https://github.com/github/gh-aw/releases/tag/v0.87.4) · [repository](https://github.com/github/gh-aw)

**Practical workflow:** schedule missing-test discovery; keep analysis read-only; permit writes only on a dedicated branch at the final stage; run CI and security checks; require a named reviewer; merge manually.

**Best next step:** automate pure-function test gaps or dependency documentation before broader code changes.

### 15. `/wayfinder` map → tickets → parallel research/prototypes → reconciled plan

**Score:** 82 = 15/15/12/17/10/6/7
**Category:** planning / skills · **Recommendation:** Try on ambiguous projects

**Why it matters:** `/wayfinder` treats an unclear project as a map that evolves through research, prototype, decision, and human-task tickets. Each child receives a bounded ticket plus enough shared map context; findings return to the map. This is a useful context-engineering pattern for greenfield work where one giant specification would be premature.

**Evidence:** [Latent Space practitioner interview and example, Aug 20](https://www.latent.space/p/wayfinder-skill)

**Practical workflow:** write the known goal and constraints; create explicit research/prototype/human tickets; run bounded sessions in parallel; update a single decision map with evidence and confidence; reconcile conflicts before generating implementation tickets.

**Best next step:** use it to plan one ambiguous product or course and compare decision quality with a single-session planning prompt.

## Category winners

| Category | Winner | Why |
|---|---|---|
| Coding agents | **Claude Code multi-session/worktree workflow** | Best combined isolation, communication, review, and live adoption evidence. |
| Developer operations | **Cursor event-driven goal loop** | Strongest new trigger-to-PR/CI operating model. |
| Browser/computer use | **Supervised structured-browser stack** | Production API maturity plus major open-source momentum; still human-gated. |
| Business automation | **n8n reusable agent in deterministic workflow** | Clear boundary between agent judgment and controlled automation. |
| Research | **Agent experiment → logbook → judge → human** | Best evidence-preserving workflow and strongest large-scale real run. |
| Research API | **Perplexity Agent API** | Broad current-web capability with an immediate Sonar migration path. |
| Workspace agents | **Confluence Agents + Rovo MCP** | Live governed context, reversible edits, analytics, and disclosed usage. |
| Observability | **Cloudflare Agent Tracing** | Captures the agent operations conventional app telemetry misses. |
| Open/local models | **Muse Glimmer + llama.cpp/vLLM** | Multimodal, agent-oriented, Apache-2.0, and day-zero serving support. |
| Recurring operations | **Hermes Agent** | Persistent cron memory, stall guards, verification receipts, and direct strategic fit. |

## Rising but less proven

- **LFM2.5 DSpark** — [Aug 20](https://huggingface.co/blog/LiquidAI/lfm25-dspark). Vendor reports up to 3.18× GPU throughput, 2.87× on-device, and 57% lower function-call latency for the 2.6B model. Reproduce on the target Mac and task.
- **Docker Sandboxes** — [HN, Aug 10](https://www.docker.com/products/docker-sandboxes/), 694 points/396 comments. Strong demand for disposable agent environments; evaluate host isolation, credentials, networking, and cleanup rather than assuming “container” means safe.
- **qm multiplayer agent harness** — [GitHub/HN, Jul 31](https://github.com/yc-software/qm), 682 HN points/164 comments. Compelling team metaphor, but needs evidence on merge conflicts, supervision load, and cost.
- **Prime Agent v0.8.0** — [Aug 21](https://github.com/PrimeIntellect-ai/prime-agent/releases/tag/v0.8.0), 17,823 stars. Persistent/self-improving harness remains strategically interesting; use only in disposable clones with cost and stop limits.
- **Agent-native CRM (`trycompai/crm`)** — [created Jul 31](https://github.com/trycompai/crm), 8,793 stars. Fast open-source momentum; customer-data permissions and write controls need scrutiny.
- **GenOffice** — [created Jul 31](https://github.com/genspark-ai/genoffice), 3,476 stars. Open office artifact workflow is useful; validate document fidelity and macro/external-link safety.
- **OpenBot** — [created Aug 17](https://github.com/CopilotKit/OpenBot), 2,261 stars. Per-agent computers and action previews are promising, but independent completion and security evidence is early.
- **AgentENV** — [pushed Aug 21](https://github.com/kvcache-ai/AgentENV), 3,274 stars. Distributed agent environments matter as concurrency grows; operational isolation evidence is still limited.
- **MCP Memory** — [Show HN, Aug 13](https://github.com/fellowgeek/mcp-memory), 70 points/36 comments. Local OKF/SQLite memory is practical; stale decisions and sensitive retention remain unresolved.
- **mcptoon** — [Show HN, Aug 11](https://github.com/activeing123/mcptoon), 73 points/49 comments. Token-efficient progressive tool discovery is the right direction, but the 99.9% claim needs independent benchmarking.

## Overhyped / be careful

- **“Always on” without bounded authority:** persistence multiplies both utility and error. A long-lived goal needs time, token, domain, write, and stop limits.
- **Unsupervised logged-in browser agents:** browser structure improves targeting, not trust. Viewed pages can inject instructions; authenticated profiles increase blast radius.
- **Agent OS products ranked only by Product Hunt:** August’s leaderboard contains many “approval-first,” “stop babysitting,” and “self-driving” claims, but rank/upvotes do not establish completion, security, or retention quality.
- **Autonomous CRM, refunds, publishing, or production writes:** draft and recommend first. Separate approval and use identities that technically cannot perform forbidden actions.
- **Self-improving playbooks without versioning:** persistent learning can preserve mistakes and make runs irreproducible. Diff, review, and pin every policy change.
- **Vendor benchmark multipliers:** GPT-5.6, Gemini 3.7, Muse Glimmer, and LFM2.5 numbers are useful hypotheses. Evaluate the complete harness on real tasks.
- **Phone/SMS-verification MCP servers:** convenient demos create abuse, account-takeover, privacy, and terms-of-service risk. Ignore unless there is a legitimate, contractually reviewed use case.

## Try-this-week shortlist

1. **Coding:** run one Claude Code or Cursor task as planner → isolated implementer → clean-context reviewer → CI → manual merge.
2. **Automation:** create one n8n agent that recommends actions but leaves credentials, retries, and writes in deterministic nodes with approval.
3. **Research:** migrate one Sonar request to Perplexity Agent API and perform a separate citation audit.
4. **Reliability:** instrument one agent end to end with traces, payload redaction, replay, and a regression test derived from a real failure.
5. **Local AI:** benchmark Muse Glimmer or LFM2.5 on ten private extraction/tool-call tasks using the intended Mac/runtime.

## Best workflow to keep doing this monthly

Use a five-stage evidence loop:

1. **Discover independently:** GitHub/Hugging Face, official releases, HN/Product Hunt feeds, and practitioner/newsletter sources.
2. **Verify the window:** require an in-window launch, release, push, measured workflow, or substantive discussion; exclude old products merely reposted.
3. **Normalize and score:** merge product/repo/tutorial variants; separate live totals from 30-day gains; attribute vendor claims.
4. **Reproduce the top five:** keep prompts, source ledger, tools, traces, artifacts, cost, errors, and human corrections.
5. **Decide:** classify try now, monitor, or ignore based on the reproduced workflow and permission model—not launch language.

For this unattended cron, also retain run start/end, output path, git commit, push result, HTTP verification, and delivery status so “slow,” “stalled,” and “failed” are distinguishable.

## Raw candidate appendix

The scan retained **31 deduplicated candidates/workflows** across the required source classes.

| # | Candidate | Category | Recent evidence / momentum | Disposition |
|---:|---|---|---|---|
| 1 | Claude Code multi-session/worktree flow | Coding | Week 32; v2.1.240 Aug 22; 142,393 stars | Try now |
| 2 | Cursor subscriptions + `/goal` + isolated subagents | Coding/ops | Changelog Aug 19 | Pilot |
| 3 | Claude computer/browser + Skills/Files APIs | Browser agents | GA Aug 20 | Pilot carefully |
| 4 | Browser Use | Browser agents | 0.13.8 Aug 16; 110,091 stars | Controlled pilot |
| 5 | Stagehand | Browser automation | Pushed Aug 22; 24,020 stars | Controlled pilot |
| 6 | n8n reusable Agents | Automation | Launch Aug 5; active updates Aug 20 | Try in preview |
| 7 | ChatGPT Work connected artifacts | Research/productivity | Practitioner analysis Aug 4; GPT-5.6 update Aug 21 | Try now |
| 8 | Perplexity Agent API | Research API | Launch Aug 13; Sonar retires Sep 27 | Try/migrate |
| 9 | Gemini 3.7 Flash + Spark | Model/agents | Launch Aug 13 | Benchmark |
| 10 | Confluence Agents + Rovo MCP | Workspace | Aug 10; 5M monthly invocations reported | Try now |
| 11 | Cloudflare Agent Tracing | Observability | Aug 4 | Try now |
| 12 | ICML Open Reproductions workflow | Research/eval | Results Aug 13; 6,816 logbooks | Adopt pattern |
| 13 | Muse Glimmer | Local multimodal | Aug 10; 1,208 HN points; ~518K HF downloads shown | Benchmark |
| 14 | Hermes Agent | Agent harness | v0.20.5 published Aug 21; 234,260 stars | Try recurring work |
| 15 | n8n + Bedrock AgentCore specialists | Multi-agent support | Implementation guide Aug 20 | Pilot |
| 16 | GitHub Agentic Workflows | CI agents | Weekly update Aug 10; v0.87.4 Aug 22 | Pilot |
| 17 | `/wayfinder` skill | Planning | Practitioner workflow Aug 20 | Try/monitor |
| 18 | LFM2.5 DSpark | Local inference | Aug 20; vendor speed results | Benchmark |
| 19 | LFM2.5-2.6B | Local agent model | Aug 4 | Benchmark |
| 20 | Docker Sandboxes | Agent security | HN Aug 10, 694 points/396 comments | Evaluate |
| 21 | qm multiplayer harness | Agent orchestration | HN Jul 31, 682 points/164 comments | Monitor |
| 22 | Prime Agent | Persistent agent | v0.8.0 Aug 21; 17,823 stars | Sandbox only |
| 23 | FastMCP | MCP framework | 4.0 beta Aug 14; 27,331 stars | Test with pins |
| 24 | MCP Inspector | MCP testing | 2.3.0 Aug 19; 10,723 stars | Try now |
| 25 | mcptoon | MCP CLI | Show HN Aug 11, 73 points/49 comments | Monitor |
| 26 | MCP Memory | Agent memory | Show HN Aug 13, 70 points/36 comments | Monitor |
| 27 | Comp AI CRM | Agent-native CRM | Created Jul 31; 8,793 stars | Security review |
| 28 | GenOffice | Office artifacts | Created Jul 31; 3,476 stars | Monitor/test |
| 29 | AgentENV | Distributed environments | Pushed Aug 21; 3,274 stars | Monitor |
| 30 | OpenBot | AI coworkers | Created Aug 17; 2,261 stars | Monitor |
| 31 | LongHorizon-Harness | Computer use | Created Aug 4; 869 stars | Monitor |

## Source and limitation notes

- **Source coverage:** authenticated GitHub API/release pages; Hugging Face blogs/model metadata; official OpenAI, Anthropic, Google, Cursor, Atlassian, Perplexity, Cloudflare, n8n, and GitHub pages; HN Algolia; Product Hunt ranking fallback; Latent Space and accessible practitioner guides.
- **GitHub:** stars/forks are live August 22 totals, not window gains. Search was limited to targeted queries; no claim is made that the appendix is exhaustive.
- **Product Hunt:** the direct product pages did not provide reliable in-window launch details. A Hunted Space monthly mirror was used directionally; Product Hunt items without stronger evidence were not promoted into the top 15 solely on rank.
- **HN:** points/comments are snapshots from the Algolia API on August 22 and may continue changing.
- **Hugging Face:** model download counts and reactions are live page metadata, not unique users or production deployments.
- **Reddit, X/Twitter, LinkedIn, and YouTube:** not used as ranking evidence because direct access, login, or reliable date/view metadata was insufficient in this bounded run.
- **Vendor claims:** performance, cost, usage, and customer outcomes are attributed and not treated as independently audited. Source-diversity/adoption scores were reduced where appropriate.
- **Availability:** several products are previews, staged rollouts, paid-plan features, or region-limited. Verify tenant access and contract terms.
- **Security:** no browser/computer-use tools were run during this research. Browser-agent recommendations are based on release evidence and public workflow reports, not a fresh execution benchmark.
