---
id: weekly-dai-2025-40
title: "DAI Weekly Report - October 03, 2025"
type: weekly-report
status: approved
team: dai
owner:
created: 2025-10-03
updated: 2026-01-06
week_ending: 2025-10-03
reporting_period: "September 29-October 03, 2025"
tags: ["weekly-report", "Q42025"]
---

DAI Executive Roundup - [Monday
September 29th - Friday October 3rd,
2025]

Executive Summary

The team achieved a significant breakthrough with the cross-product marketing content agent,
which Carl's team adopted organically and used to create workspace elevator pitches in 30
seconds. Victor shipped workspace to the full internal company (800+ users logged in within 36
hours, 70% created views), though chat reliability and view creation remain friction points
requiring rapid iteration. Sneh consolidated GTM Studio roadmaps across audiences, plays, and
data management with engineering kickoffs complete for all three swim lanes, targeting
November for audiences launch, January for plays, and Q1 end for data management.

This Week's Progress

Key Momentum Areas

AJ and the PMM team launched a cross-product asset creation agent covering Workspace,
Studio, and Context Service that marketing can use without bottlenecks. Carl's team received it
enthusiastically--Carl created a workspace elevator pitch in 30 seconds that was immediately
ready to use. The agent drew from 18 unique marketing users in its first week, with
overwhelmingly positive feedback demonstrating genuine organic adoption rather than forced
usage.

Victor expanded Workspace access to all internal employees this week, with over 800 users
logging in within the first 24-36 hours and 70% creating views. The team shipped critical
features including view sharing, leadership-specific homepage artifacts, out-of-the-box views for
managers and sales roles, and numerous quality-of-life improvements. Session recordings in
Datadog went live, enabling Victor, Sean, Phoebe, and AJ to conduct targeted watch parties and
rapidly identify user experience gaps.

Brandon's team completed entity integration planning for franchisee/franchisor locations,
companies, and contacts, with missing franchisor companies now live in the platform. The team
established flywheel partner metrics tracking new HEM-to-cookie mappings (currently
thousands per day from websites versus 20+ million from Sober email hash), top resolvable
contacts, and identifier density. Vendr signed on as a flywheel partner and will implement the
pixel across their pages while providing pricing research data for signal generation.
Goals & Progress

Workspace Internal Rollout: Victor and AJ are deepening understanding of workspace user
performance following the September 23rd cohort launch and the October 1st broader internal
rollout. Critical instrumentation for Slack chat messages is fixed, though additional event
properties like UserID on some events require resolution. The team identified three core value
pillars for measurement: users landing on home and getting prompt responses, users clicking
pre-made artifacts, and users creating/editing views. With relatively low user counts, the team is
leveraging Datadog session recordings for qualitative insights alongside quantitative metrics.

GTM Studio Roadmap Consolidation: Sneh completed consolidation of GTM Studio
roadmaps across audiences (workbooks), plays, and data management into a unified view with
clear swim lanes. Technical kickoffs occurred with engineering leads across all three areas. The
path forward targets November for audiences launch, January for plays market entry, and end of
Q1 for data management MVP. Clay compete content needs refinement before November
launch, including specific use cases, evaluation criteria, and objection handling for account
managers to coach against.

Dreamforce Readiness: Adam worked with Carl and Rowan to prepare sellers for Dreamforce,
creating training assets and talk tracks covering the two happy paths and three rough edges to
avoid. Live training and Claude onboarding sessions are scheduled for early next week. The
team finalized PMM and narrative packages for Context Service and AI credits, with Carl
receiving everything needed for seller enablement.

Strategic Challenges

Chat reliability in Workspace emerged as the primary user friction point, with users experiencing
context switching issues, incorrect account references, and latency problems. The challenge
stems from rapid feature additions creating whack-a-mole regression issues--each new
capability can trigger unexpected behavior elsewhere. Victor noted that regression testing all
production releases would slow velocity too much, so the team is evaluating targeted testing on
the top 5-10 use cases that go-to-market personas actually use. Adam emphasized that many
regressions trace back to architectural decisions around state management and context object
handling in the orchestrator agent.

Query and search capability constraints are blocking multiple GTM Studio enhancements
including CRM field enrichment, custom fields, lookup fields, picklist values, and signals
integration. The current approach for Studio to interact with data is not sustainable long-term.
Dominik flagged this as a recurring issue appearing for multiple weeks that requires
resolution--the team needs clarity on the data interface layer and query engine approach
(SOLR versus BigQuery) even if the full solution isn't built immediately.

Resource coordination across the growing product surface area is creating execution friction.
The team identified a need for a single CRM writeback service to support both plays and data
management rather than multiple parallel implementations. Additionally, the volume of internal
feedback on Workspace from diverse roles (CSMs, managers, RevOps) is creating
noise--Dominik suggested focusing enablement specifically on AEs and AMs since CSM use
cases differ substantially and features aren't yet optimized for their workflows.

Strategic Insights

Key Learnings & Discoveries

Brandon's team validated a novel email generation approach suggested by Carlos, using
CookieSync partners to corroborate generated emails. When tested on 500K generated emails,
the team found 30K hits where partners had captured web activity with those hashed emails,
providing evidence the email was legitimate. This discovery highlights the broader flywheel
opportunity--while most identity partners capture consumer profiles, ZoomInfo has a real
opportunity to lead in capturing professional identities on the web. The team also achieved
all-time highs on visitor resolution rates this week.

The marketing content agent breakthrough revealed important principles about AI adoption:
shorter, more focused prompts with rich source materials perform better than lengthy
instructions, and organic adoption happens when tools genuinely solve pain points without
requiring behavior change. Victor noted this as one of the first examples where people naturally
chose to use an LLM without strong-arming or forcing functions. The key was meeting the team
where they already work rather than requiring new workflows.

Meghan's design team validated that chat should persist as an assistant throughout the
workspace experience rather than clearing on context changes. The solution requires visual
indicators when context shifts (similar to Cursor or Claude Code) where the chat acknowledges
"context changed" and shows what the user is now viewing. This maintains message history
while refreshing the user context state, avoiding confusion about whether chat is operating on a
specific view or across all views.

Cross-Team Dependencies

Ruby and the workflows team are finalizing plays infrastructure requirements following detailed
review sessions covering triggers, actions, CDC (change data capture), and Global Event Bus
integration. The team is targeting architectural decisions by end of day Tuesday, with
Wednesday as the outside timeline. This foundation is essential for bringing plays to market in
January and ensures the platform can support workflow execution with proper reporting through
the GTM Studio wrapper object.

Andres and the integrations team must collaborate with Sneh's data management and plays
teams to consolidate on a single CRM writeback service. This consolidation is non-negotiable
for plays functionality going forward and critical for data management capabilities. The current
fragmented approach across multiple teams creates duplication and maintenance challenges
that will compound as the product scales.
Looking Ahead

Next week focuses on three parallel tracks: workspace user analysis as the first full post-quarter
week provides real usage patterns, GTM Studio November launch preparation including Clay
compete enablement, and the Wednesday-Thursday offsite for roadmap alignment.

Victor and AJ will analyze the September 23rd cohort and October 1st broader rollout as both
groups move past end-of-quarter activities. The team will watch session recordings together,
define what "getting value" means for a user session in defensible terms, and establish
quantitative success measures for the workspace source of truth document. These metrics will
inform go/no-go decisions on expanding the user base versus improving quality. Sean and Lars
continue addressing chat reliability and latency through incremental breakthroughs, with view
creation via natural language using ZI and CRM data targeting later this week.

Sneh finalizes the GTM Studio sales motion targeting November launch, focusing especially on
Clay compete positioning. The team needs to complete the target account list where Clay
objections have been identified, finalize specific use cases showing how GTM Studio evaluates
against Clay, and prepare objection handling content for account managers. Additionally, the
team will enable paid POC discounting for the October transition period between early access
and formal POC customers. The consolidated roadmap positions audiences for November,
plays for January, and data management MVP for end of Q1.

The Wednesday-Thursday offsite brings together product and engineering leadership to align on
a unified 12-month roadmap with clear priorities and resourcing. The session will take a step
back for longer-term thinking while ensuring tight execution alignment across Copilot
Workspace, GTM Studio, and supporting infrastructure. Adam will finalize roadmap lockdown
deliverables including agentic layer requirements for Victor's initiatives, task and pulse system
specifications, and semantic data resourcing plans. The goal is to emerge with one roadmap,
clear priorities, and confidence heading into Q4.

Source: DAI Executives Operating Framework entries from [September 29, 2025 - October 3,
2025]
