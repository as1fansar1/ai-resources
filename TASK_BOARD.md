# AI PM Task Board

Last updated: 2026-02-19 (UTC)

## Legend
- **Status:** Backlog | In Progress | Blocked | Done
- **Assignee:** Asif | Claw

## In Progress
| ID | Task | Status | Assignee | Priority | Notes |
|---|---|---|---|---|---|
| T-001 | Implement `/analyze` endpoint with strict schema | In Progress | Claw | P0 | Contract implemented; mock behavior in place; needs live model wiring + test run |
| T-002 | Add dependency install + one-command smoke test | In Progress | Claw | P0 | `pytest` missing in runtime; add repeatable `make smoke`/script |
| T-003 | Wire `/analyze` from mock to OpenRouter client | In Progress | Claw | P0 | Keep same request/response contract |
| T-004 | Complete daily AI PM sprint artifact (today) | In Progress | Asif | P0 | File: `AI-PM-Sprint-Day-<date>-feature-brief-generator.md` |

## Backlog
| ID | Task | Status | Assignee | Priority | Notes |
|---|---|---|---|---|---|
| T-005 | Add OpenRouter response parser utility | Backlog | Claw | P1 | Safe extraction of assistant text from payload |
| T-006 | Add run persistence for analyze runs (`data/runs/`) | Backlog | Claw | P1 | Include request, response, meta |
| T-007 | Build simple input/output UI or CLI | Backlog | Claw | P1 | Depends on stable `/analyze` live path |
| T-008 | Add basic eval harness (golden examples) | Backlog | Claw | P1 | Quality scoring loop for prompt iterations |
| T-009 | Add cost + latency logging | Backlog | Claw | P2 | Track model usage by run |
| T-010 | Portfolio case-study draft from build logs | Backlog | Asif | P1 | Collaborator-facing proof of work |
| T-011 | Finish setup for Tavily API key | Backlog | Asif | P1 | Required for tavily-search runtime |
| T-012 | Finalize Moltbook claim status | Backlog | Asif | P2 | Account currently pending claim previously |
| T-013 | Review and optionally force-install flagged skills | Backlog | Asif + Claw | P2 | `self-improving-agent`, `agent-browser`, `tdd-guide` |

## Blocked
| ID | Task | Status | Assignee | Priority | Blocker |
|---|---|---|---|---|---|
| T-014 | Create GitHub Project board (kanban) | Blocked | Claw | P1 | GitHub token missing scopes: `project`, `read:project` |

## Done
| ID | Task | Status | Assignee | Priority | Notes |
|---|---|---|---|---|---|
| T-015 | Create and publish `requirements.md` | Done | Claw | P0 | Pushed to `main` |
| T-016 | Create public GitHub repo for AI PM Lab | Done | Claw | P0 | https://github.com/as1fansar1/ai-pm-lab |
| T-017 | Configure daily sprint + nightly build cron routines | Done | Claw | P0 | Morning/evening accountability loops active |

## Operating Rules (from now on)
1. Any new task is added here immediately with owner + status.
2. Any status change is updated here in the same work session.
3. Completed tasks move to **Done** with one-line outcome.
4. Blockers must include exact unblock condition.
