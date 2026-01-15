---
id: weekly-intelligence-2025-43
title: "Intelligence Weekly Report - October 24, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "Q42025"]
---

Intelligence Team Executive Roundup -
[October 20, 2025 - October 24, 2025]

Executive Summary

The team is now two weeks out from full sales enablement for ZoomInfo's agentic platform.
Following user feedback, Lars Vedo has a prioritized improvement list covering Chorus
engagements, ZI data views, source citations, and Salesforce customizations. Derek Osgood is
pushing to get the first 2-3 actual plays live in staging, which will enable concrete socialization
across teams and reduce abstract conversations about how plays should work. Meanwhile,
Srivatsa Marthi has begun critical architectural planning for signals migration--with strong
support from Andres and Brandon--that will modernize how signals feed into plays and create a
more flexible, efficient foundation for the platform going forward.

This Week's Progress

Key Momentum Areas

GTM Studio plays reached functional prototype stage. Derek Osgood built the first actual
plays in the 00 workspace using live tools, providing tangible examples the team can test and
refine. While staging deployment is delayed due to frontend resourcing constraints, having
working plays demonstrates the vision concretely and will accelerate alignment across teams
working on this initiative.

User feedback driving targeted improvements for Dreamforce. Sean and Adam collected
and prioritized seller feedback from the Copilot and Copilot Chat survey, identifying specific
accuracy and tool-calling issues. The team is staying focused on raising response quality rather
than adding new features, with new agent versions testing in staging today and production
releases planned for the coming days.

Signals architecture modernization gaining organizational support. Srivatsa secured
backing from Andres and Brandon for deprecating the current signals layer, with the plan to
have raw data sources feed directly into GTM Store. This architectural shift will eliminate
meaningful technical debt and create a more efficient system for how signals trigger plays and
provide context to agents.

Goals & Progress
GTM Studio: Derek is working to deploy the first 2-3 plays in staging with tools including search,
scrape, research, docs, spreadsheets, ZI Data, CRM, email, Slack, and LinkedIn capabilities.
Staging deployment is blocked on frontend resourcing (currently one developer), but tools are
being tested in the 00 workspace environment. The Global Event Bus integration looks
promising for trigger signals, though some gaps exist between currently available signals and
the plays wishlist that will need addressing through scoring and other mechanisms.

GTM Copilot Workspace: Lars has two weeks remaining to tune agents for ZoomInfo's internal
rollout. Following the user survey, priorities include adding Chorus engagements, enabling view
creation with ZI data, improving source citations, customizing for ZI's Salesforce configuration,
and fixing target accounts functionality. Ryan Stevens is coordinating to ship all remaining
projects by 11/3, setting up the following week for intensive agent accuracy tuning. The team is
balancing stability for 11/3 while testing new agent architecture in staging.

GTM AI Context Service: Rowan Bailey completed and shared a PRD for the Account Brief
team, detailing section-by-section breakdowns for the updated GTM Store schema, target
enrichment sections, and priority ordering for the next few months. This provides more granular
account context retrieval for agents and the context service MCP. Srivatsa is working through
open architectural questions around how plays should consume content outside GTM Store,
including scores, Workbooks, and buying groups.

Strategic Challenges

Frontend resourcing creating deployment bottlenecks. Derek's team has one frontend
developer working on 00 staging migration, which is taking longer than expected and putting the
December delivery timeline at risk. The team can likely move quickly on tools integration once
Andy Harganto is fully onboarded, but having a single developer creates fragility. Additional
frontend support would accelerate the critical path to getting plays socialized and tested in real
environments.

View creation reliability hampering user experience. Ryan Stevens and Lars identified
fundamental issues with how the agent creates views in Workspace--it evaluates field names
and filters but not actual data, leading to poor results when users ask for "top opportunities" or
similar queries. Additionally, Workbooks' default sort by create date means large queries return
essentially random subsets of results. Robyn documented that competitors like Ocean.io and
Clay have similar problems, creating an opportunity to differentiate if ZoomInfo can implement
intelligent ranking through APS or other scoring mechanisms.

Context service and semantic data scalability concerns emerging. Carlos Nunez flagged
that scaling the semantic service to hundreds of customers will cost millions annually.
Workbooks is generating excessive agentic platform calls requiring request queue
implementation. Meanwhile, there's organizational uncertainty about the value proposition for
embedding scores like account priority into applications, with no clear urgency from Workbooks
and Workspace teams despite the technical work being largely complete.
Strategic Insights

Key Learnings & Discoveries

Signals deprecation timing reveals broader architectural debt. The enthusiastic support
Srivatsa received from multiple leaders for deprecating the signals layer suggests the team was
late in proposing this change. The current architecture creates "meaningful debt with every
passing month" as stated in the operating documents. Moving to a model where raw data
sources feed directly into GTM Store, with processing logic living in plays rather than a separate
signals layer, will provide the flexibility needed for custom insights and play triggers while
eliminating redundant systems.

Product naming and architecture misalignment creating confusion. The team discussion
revealed significant confusion between Workbooks (a database for RevOps to build complex
lists) and Workspace (a simpler execution layer for frontline sellers). Ryan Stevens noted that
even product people struggle to keep them straight, despite the mental model making logical
sense. The underlying architecture diverges sharply--Workbooks uses arbitrary advanced
search queries snapshotted into tables, while Workspace dynamically queries Salesforce with
ZoomInfo column enrichment. This disconnect between user expectations and implementation
reality poses product strategy risks.

Email sequencing can and should live in plays. Derek's conversation with Gabe confirmed
that doing sequences outside structured tools like Outreach should just be implemented as
plays. The team has waiting mechanisms, email sending capabilities, and tracking--the main
gap is exit criteria for sequences (like pulling people out when they reply). Ryan noted this is
trivial to add with LLMs. Rather than building standalone sequencing infrastructure, using plays
as the execution layer provides a cleaner architecture and avoids duplicating capabilities.

Cross-Team Dependencies

Our work with the Workbooks team on agentic integration remains critical for GTM
Studio adoption. The team needs alignment on how plays consume data and provision work to
sellers. Snee's team is designing how workbooks get pushed to reps via the "activate" button,
creating views that sellers can execute through Workspace chat. However, scalability concerns
around agentic platform calls require implementing request queuing to throttle volume.
Additionally, the Workbooks team needs to handle tokens and cost tracking as they integrate
semantic data and other inference-heavy capabilities.

Platform teams (GTM Data Model, RBAC, Integrations) are blocking Copilot V2 progress.
Sean Walter has repeatedly flagged that sharing, collaboration, and real-time CRM sync
capabilities require commitments from dependent teams. Without these foundations, the
Intelligence team risks building temporary solutions internally that create technical debt. The
upcoming API Gateway work and GraphQL tooling for unified profile data should help, but
explicit prioritization from leadership would accelerate these critical integrations.
Looking Ahead

The next two weeks are all about ZI sales enablement. Lars and Ryan Stevens will focus on
stability, accuracy improvements, and agent tuning rather than new features.

Derek will continue pushing plays into staging with all available tools, working to
demonstrate concrete value and socialize the execution model broadly. Getting even basic plays
running will shift conversations from theoretical to practical and help identify remaining tool gaps
and architectural needs.

Srivatsa will drive alignment on signals migration architecture, working with Platform
(Linda, Majed), S2A (Brian C.), and other teams to answer open questions about how plays
consume scores, buying groups, and other non-GTM-Store content. The team will also plan the
specific migration path to get from current state to target architecture while supporting
immediate use cases, potentially consuming directly from GSO in the short term even if that's
not the long-term solution. Rowan will focus on getting the MCP gateway, auth, entitlements,
and RBAC clear for the Context Service to go live with potentially sensitive sources like
engagements and semantic data.

Source: Team Intelligence Operating Framework entries from [October 20, 2025 - October 24,
2025]
