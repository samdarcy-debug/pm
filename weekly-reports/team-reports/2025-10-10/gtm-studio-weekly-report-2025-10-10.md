---
id: weekly-gtm-studio-2025-41
title: "GTM Studio Weekly Report - October 10, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-10-10
updated: 2026-01-06
week_ending: 2025-10-10
reporting_period: "October 6-10, 2025"
tags: ["weekly-report", "Q42025"]
---

GTM Studio Executive Roundup - [October
6, 2025 - October 9, 2025]

Executive Summary

The team made critical progress toward November 3rd launch readiness across all core
workstreams this week. Jagannath Ramesh and team completed agentic release planning and
enablement materials, while Arun V enabled self-serve analytics in Pre-Prod with 5 AMs/CSMs.
Ash Lauricella and Corina Soto advanced AI Data Management by kicking off M4/M5 working
sessions with engineering and launching Data Health Scan prototype, with strong traction from
Strat, Enterprise and Mid-Market leadership teams. Design resource constraints remain a
blocker for agentic UX improvements, and GTM data model historical opportunity data gaps
could delay ROI GA.

This Week's Progress

Key Momentum Areas

Launch readiness accelerated significantly with Jagannath completing release materials for
November, finalizing AI credit realignment designs with the team, and shipping the side chat
experience to production. The agentic capabilities roadmap now has clear definition with Run
Columns from Chat in staging and semantic enrichment refinements underway, positioning the
team to deliver paying SKUs in November.

ROI analytics reached a major milestone as Arun secured sign-off from the Copilot V2 team and
successfully enabled self-serve analytics for 5 AMs/CSMs in Pre-Prod environment. Early
feedback shows AMs and CSMs are responding well to the self-serve analytics agent for
engagement-related queries, validating the upsell opportunity being primarily seat-based with
ROI as the key unlock for customer conversations.

Data Management generated exceptional field demand, with Corina distributing 1,400 Data
Health Scans to account managers and completing the design and engineering kickoff for
bringing DHS into GTM Studio. The team received strong validation from Dakota, Alex
Lazerowich, and Rob Lotterman's Enterprise teams, plus organic interest from Steve Lincoln's
Mid-Market team, signaling this could be a significant Q4 upsell driver.

Goals & Progress
Launch Readiness & Agentic Capabilities: Jagannath made substantial progress on
November launch materials completing roughly 80% of release readiness work. AI credit
realignment designs were finalized after cross-team alignment sessions, with dev work
resuming and targeting October 20th delivery (may slip). Studio side chat experience
improvements deployed to production for Dreamforce readiness.

ROI Analytics & Self-Serve Capabilities: Arun advanced Studio and Workspace ROI analytics
designs and product requirements defined for Workbook and Workspace ROI tracking. The
self-serve analytics prototype showed strong results in Pre-Prod with 5 AMs/CSMs, who
validated the agent effectively handles most engagement queries. The team is now working to
finalize AI credit reduction alignment before broader rollout.

Data Management: Ash progressed M4 and M5 requirements documentation while kicking off
working sessions with engineering to accelerate architecture planning and research. The team
identified key dependencies with GTM Data Model and initiated conversations with Andres and
Prateek's teams. RingLead usage analysis work with Chad's analytics team began to inform
strategic roadmap prioritization decisions. Corina successfully held the design and engineering
kickoff meeting for bringing Data Health Scan into GTM Studio (M3), establishing clear
dependencies and development paths. For M1, the team worked with 20+ AMs and is actively
working with Alex Lazerowich's team and Rob Lotterman's team on targeted customer
meetings. M2 work on Enrich Premium Plus for HubSpot and MS Dynamics continues with QA
and enablement material development for November release.

GTM Config Validation: Tingting Wu prepared GTM 0 Config formats for customer feedback
sessions starting next week, achieving alignment with design and research teams on a
two-track validation approach covering both content quality and UX flow. The team reached out
to 11 customers for Zero Config feedback with 4 awaiting scheduling confirmation, while design
prototypes neared completion and front-end discussions progressed on API and data contracts.

Workbook Core & Signals: Tanvi drafted learning memos and product briefs while advancing
critical engineering reviews on queue requirements, cell error states, and signals parity work.
Requirements and designs for queuing were updated and validated with the engineering team
to ensure these priority items move forward without implementation delays. A signals parity
discussion was scheduled and resulted in a decision to wait for GraphQL completion while
enhancing existing intent and scoops signals to output full signal data.

Strategic Challenges

Design resource constraints are blocking critical agentic UX improvements that are essential for
November launch. Jagannath needs designer support from Meghan Cartlidge's team for two key
areas: the AI Data Agent enrichment configuration experience (showing how agent-built
prompts and configurations work) and the full-page Studio Chat experience (starter prompts,
capability explanations, and onboarding flow). Without these resources assigned this week, the
team risks shipping agentic capabilities with suboptimal user experience that could impact early
adoption.
GTM data model missing historical opportunity data will require to delay picking the ROI GA
timeline, currently targeted for mid-December. The platform team discovered certain historical
opportunity datasets are absent from GTM Data Model, which would cause pipeline progression
metrics to show zeros for many customers. While the data exists in legacy tables, Andres and
Asaf's teams need to determine how to backfill into new GTM DM tables. Additionally, the
Agentic Chat powering the CFA FAQ Agent has been removed from the dashboard because the
chat interface isn't loading properly. For certain CSMs, the interface fails to load for the same
user on the same tenant, and the load times out intermittently. Raised the concerns with Agentic
Chat team (Lars).

Signals parity and data onboarding continues to create friction with each new dataset requiring
custom integration work. The team scheduled alignment discussions but faces a broader
systemic issue where app teams end up program managing data integrations that should be
owned by platform. Customer confusion around signal variations across product areas (raw
signals vs recommended signals vs SalesOS) is creating trust issues, as seen when customers
compare website spike signals and buyer ID signals and find unexpected discrepancies.

Strategic Insights

Key Learnings & Discoveries

Customer usage patterns revealed through Early Access calls show users attempting full-sheet
analysis with AI Data Agent beyond its designed scope, requesting capabilities like "prioritize all
companies" and "export to Salesforce." This validates the team's hypothesis about needing an
overarching orchestration agent and suggests current AI Data Agent positioning needs clearer
boundaries and expectations to prevent user frustration when capabilities fall short.

Signal data inconsistency across product surfaces is eroding customer trust based on multiple
customer feedback sessions this week. When customers add website spikes and website buyer
ID signals simultaneously, they expect data correlation but instead see populated buyer IDs with
empty spike data for the same companies, creating "is this a bug?" questions. This highlights
both an education gap and a product consistency problem requiring the data catalog work Sneh,
Brahm, and Sri discussed, plus potentially signal-specific guidance within product flows.

Early Access deep dive with 22 customers (soon 27) revealed only 4 are truly healthy with clear
value realization, while 3 additional accounts see tremendous potential but are blocked solely
on activation to sellers. This "last mile" activation gap represents both a near-term conversion
blocker and validates the strategic importance of Mohan's Copilot activation work. The
remaining accounts need consultative support on use case ideation, revealing a critical gap in
templates and self-service onboarding that must be addressed for scale.

Data Health Scan is generating unexpected organic demand beyond Enterprise, with
Mid-Market (Steve Lincoln) teams proactively requesting to participate after seeing Enterprise
traction. This suggests the business case for Data Management could be larger, with potential
to drive both retention plays and cross-sell/upsell opportunities across all segments. The team
received particularly strong validation from Lazer's staff and Rob Lotterman.

Cross-Team Dependencies

Engineering resource allocation for AI Data Management M4/M5 requires alignment with Imesh
Wijewardena and Hanan Baranes on DevOps and QA gaps. While core engineering teams
understand the mid-January dev complete target for MVP, resourcing gaps in critical functions
could derail timelines, and Tushar Goel's team needs to move post-September Workbook
priorities forward to maintain delivery momentum.

Design team capacity is stretched critically thin across GTM Studio initiatives, with Jagannath
blocked on agentic UX improvements and multiple teams waiting for Meghan Cartlidge's group
to assign resources. Brahm secured Yoav for Data Management design work, but the broader
design pipeline for agent experiences, full-page chat, and configuration displays remains
under-resourced relative to November launch needs.

Looking Ahead

Next week represents a critical inflection point as the team shifts from planning to execution on
November 3rd launch deliverables while maintaining Dreamforce readiness. Top priorities
include finalizing agentic release scope and timeline commitments, securing design resources
for UX-critical features, and locking engineering capacity for Data Management M4/M5
(foundational data management capabilities in Studio) with clear resourcing plans.

The team will focus on three key workstreams that can accelerate launch readiness: (1) Arun
continuing self-serve analytics enablement with more AMs/CSMs while finalizing workspace ROI
prototype, (2) Ash and Corina completing engineering kickoffs for Data Management with firm
resource commitments and delivery timelines, and (3) Tingting conducting customer validation
sessions on GTM Config to validate zero-config quality and UX flows. (4) Jagannath's focus
next week is on Dreamforce demo as he will be attending the event live. (5) Tanvi's focus next
week will be continuing PRD reviews with the engineering team for December deliverables and
doing a deep dive into the solution for making "find contacts" feature more dynamic. (6) Mohan
following through on Workbook-to-Copilot activation to ensure cross-team delivery and
conducting PRD and design reviews to kick off GTM Studio-to-DoubleO plays activation
discoveries.

Field enablement becomes paramount with Sneh driving Clay competitive positioning and
objection handling content to sales readiness, while the team refines the target account list of
customers with Clay mentions for focused outreach. Success depends on resolving design
resource bottlenecks this week, achieving GTM data model clarity on historical opportunity data,
and maintaining momentum on Data Health Scan adoption with 10-15 high-fit accounts
receiving targeted AM support.
Source: GTM Studio Operating Framework entries from October 6, 2025 - October 9, 2025
