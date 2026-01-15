---
id: weekly-product-bi-2025-40
title: "Product BI Weekly Report - October 03, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-10-03
updated: 2026-01-06
week_ending: 2025-10-03
reporting_period: "September 29-October 03, 2025"
tags: ["weekly-report", "Q42025"]
---

**Product BI Team Executive Roundup - Week of October 3, 2025**

**Executive Summary**

AJ\'s team successfully resolved a user ID bug blocking chat-level
analytics for Copilot Workspace\'s internal AE/AM rollout and secured
Datadog session recordings---both now enabling deeper behavioral
analysis starting next week. Nanxi completed full alignment with
stakeholders on API data infrastructure, with dashboard delivery
targeted for her return from PTO. The team is advancing on multiple
fronts with Workspace V2 instrumentation fixes, Studio event taxonomy
standardization, and an integration table migration that requires
careful coordination with Andreas.

**This Week\'s Progress**

**Key Momentum Areas**

AJ and Phoebe fixed the user ID bug that was preventing chat message
reporting at the user level, unblocking a key analytics capability for
understanding how internal GTM users engage with Workspace. Session
recordings are now available in Datadog, and the team plans a viewing
party with Victor and Sean post-offsite to analyze user behavior and
discuss product implications.

Nanxi completed a comprehensive investigation of API data
infrastructure, aligning with stakeholders and engineers on data
definitions, availability, structure, and known issues. She created
documentation explaining how the API works and the logging architecture,
with clear expectations set for what can be delivered now versus what\'s
deferred to future phases.

Ferrell and Imball made progress on the GTM Studio event instrumentation
audit, with Ferrell managing taxonomy review, identifying unimplemented
events, and working directly with engineers on implementation and
testing. Phoebe is conducting a parallel taxonomy review with Sean on
Monday for the Copilot side, creating a standardized approach across
both products.

**Goals & Progress**

**Workspace V2 Analytics**: AJ drafted a first version of account health
metrics for Workspace and Studio accounts, which needs iteration with
product owners Snee and Victor, plus alignment with Mary and Whitney.
The team is treating next week as a fresh baseline for usage analysis
since end-of-quarter activity this week may have skewed behavior
patterns. AJ emphasized the importance of deepening user behavior
understanding as the product moves from internal GTM users toward
external customer launch.

**API Dashboard & Infrastructure**: Nanxi\'s investigation revealed more
complexity than anticipated in the API data, but she systematically
worked through data definitions, structure, and availability issues with
stakeholders. Dashboard wiring has started, though the actual dashboard
build is pushed to after her PTO next week, with completion targeted for
the week she returns. Adam indicated interest in additional Phase 2
dashboard features that require pulling data from MongoDB (not currently
in Snowflake or CDP), which will need engineer support from Igor.

**Event Taxonomy & Instrumentation**: Ferrell is systematically working
through GTM Studio events, documenting taxonomy, and coordinating with
engineers on implementation. Imball is handling the Copilot side. The
team identified lingering instrumentation gaps that require ongoing
engineering cleanup efforts---this is standard technical debt work
rather than a roadblock. Phoebe\'s Monday session with Sean will
establish the standard taxonomy for Workspace events, with pending
alignment before beginning a recurring viewing series for session
recordings.

**Strategic Challenges**

The integration table deprecation requires careful migration work since
the new table structure uses different field names and organization than
the current one. Ferrell needs focused time with Andreas to map fields
correctly and ensure no disruption to active integration tracking
metrics. While there\'s no significant business benefit from the new
table (it still requires the same complex joins and is actually larger),
the move aligns with broader data model standardization efforts.

Amplitude session recordings still have unresolved issues, so the team
is using Datadog as a workaround for Workspace. This creates some
fragmentation in tooling, though AJ secured the Datadog implementation
with Guy (an engineer) specifically for this use case. The team should
monitor whether Amplitude issues get resolved or if the Datadog approach
becomes the standard.

**Strategic Insights**

**Key Learnings & Discoveries**

Nanxi highlighted that clear documentation with visual diagrams
significantly accelerates alignment, especially with non-technical
stakeholders like Adam. When explaining data granularity gaps and why
certain metrics aren\'t available, showing a structural diagram made the
constraints immediately comprehensible versus trying to explain in
prose. She\'s incorporating these diagrams into documentation for future
maintainability, noting how difficult it was to understand previous
queries without this visual context.

AJ observed that end-of-quarter timing artificially inflated this
week\'s usage metrics, making it less representative of steady-state
behavior. Next week will provide a cleaner baseline for understanding
actual Workspace usage patterns among internal AEs and AMs before
external customer rollout.

**Cross-Team Dependencies**

The team needs focused support from Andreas for the integration table
migration field mapping exercise---probably 20-30 minutes of dedicated
time. Since Ferrell and Eran have holiday time next week and the week
after, this coordination may shift timing slightly but shouldn\'t block
other work.

Session recording analysis next week depends on Victor and Sean\'s
availability post-offsite. The team is coordinating a viewing party
format where all four can watch recordings together and discuss product
implications in real time.

**Looking Ahead**

Next week focuses on three parallel streams: deepening Workspace
behavioral analysis through session recording review and account health
metric iteration, completing the API dashboard post-Nanxi\'s return, and
continuing systematic event taxonomy cleanup across both Workspace and
Studio.

AJ will iterate on the Workspace/Studio account health draft with
product owners and GTM leadership, refining how success metrics connect
to renewal predictions and product adoption. The session recording
viewing party will provide qualitative insights to complement
quantitative event data, helping identify friction points and
opportunities. Ferrell continues taxonomy work and should coordinate
with Andreas on integration table migration when schedules align. Nanxi
returns from PTO with API dashboard completion as the primary goal,
aiming to close out the request entirely by the following week.

The team maintains good momentum across instrumentation fixes,
infrastructure alignment, and cross-functional coordination. The user ID
bug resolution and Datadog session recordings represent meaningful
unblocks for Workspace analytics depth.

*Source: Team 1-2-3 Operating Framework entries from October 3, 2025*
