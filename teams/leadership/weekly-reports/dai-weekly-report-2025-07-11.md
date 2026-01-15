---
id: weekly-dai-2025-28
title: "DAI Weekly Report - July 11, 2025"
type: weekly-report
status: approved
team: dai
owner:
created: 2025-07-11
updated: 2026-01-06
week_ending: 2025-07-11
reporting_period: "July 7-11, 2025"
tags: ["weekly-report", "Q32025"]
---

Product DAI Executive Roundup - Monday
July 7th - Friday July 11th

Executive Summary

The team is executing but constrained by foundational blockers. Query layer dependencies
are paralyzing multiple critical workstreams including CRM enhancements, custom fields, and
dataset development. Meanwhile, GTM Plays has "too many cooks" with 12 people in planning
meetings but unclear ownership and timelines. AI Audiences finally has engineering resources
assigned and development beginning, but we're still in requirements stage for most datasets
rather than dev-ready work.

This Week's Progress

Key Momentum Areas

AI Audiences breakthrough with engineering assignment. Jagan returned and development
has officially begun on embedding chat into GTM Studio with ZI and GTM DM list building in
progress. First demo expected by end of week - a significant acceleration from design-only
work. Sneh's team consolidation across Brahm and Veronica's groups is creating clearer PM
ownership across domains.

Identity resolution hitting all-time highs. Brandon's team achieved visitor resolution at
all-time highs with core IP-to-company resolution up 11% via IP2Company 5x5 integration.
Added over 12 million supplemental emails to the system. The team is executing on
foundational improvements while planning next-generation capabilities.

Product Marketing engine delivering first full-scale monthly release. AJ's team successfully
executed the July MCR with implementation guides, PR FAQs, and a new company-wide
release communication strategy. This represents the first complete test of the new automated
content generation system replacing traditional PMM processes.

Goals & Progress

AI Audiences (Sneh): Development work officially started with assigned engineering team.
Meeting aggressive timeline targets with first demo expected by end of week. Team
consolidation creating clearer ownership with Tanvi on Workbooks core, Mohan on Activation via
Workflows, and Corina on global datasets integration.
Pre-Copilot Experience (Vinay): Phase 1 now in testing with QA team running test plans. All
pre-copilot work either in dev or ready for dev with no known blockers. Successfully managing
transition from Alex to Ant on Profiles and Top Contacts with comprehensive handover
documentation.

Context Engineering (Rowan): Taking over Bert's team while establishing vision for context
engineering at ZI. Created 2-pager positioning document and RFC for agentic core team
definitions. Planning work with Lars and Sean progressing well on milestone interdependencies
between Copilot 2, Sales Hub, and Workbooks.

Identity Graph Optimization (Brandon): Form-complete vs resolution dashboard operational
with qualitative and quantitative benchmarking in place. MAID-based identifier integration
underway with exploratory work on MAID:HEM:IP optimization. Team identified significant
enterprise opportunity for person resolution outside of signals.

Strategic Challenges

Query layer dependencies creating cascade failures. CRM enhancements, custom fields,
lookup fields, picklist values, and signals are all blocked by query layer issues. This is
preventing multiple teams from moving beyond requirements into development. The
dependency web is expanding - what started as individual feature blocks is now constraining
entire workstreams across datasets, CRM integration, and core functionality.

GTM Plays execution hampered by organizational confusion. Ali reported 12 people
showing up to planning meetings with "too many cooks in the kitchen" preventing
decision-making. While high-level requirements are clear and no technical red flags exist,
ownership clarity between Veronica (play use cases), Mark Frayle (workflows implementation),
and Adam's team (natural language interface) remains undefined. Timeline commitments are
vague.

Resource allocation decisions pending without clear planning process. Multiple team
members flagged uncertainty about staffing against most important initiatives. ZIM vs. Plays vs.
Data Agent resource allocation remains unclear. Agent platform specifically identified as
understaffed. The team is waiting for "planning" but no structured planning motion exists,
creating execution delays.

Strategic Insights

Key Learnings & Discoveries

Human-in-the-loop requires platform-level architecture. Ali identified that current notification
approaches hard-coded in Sales Hub or Copilot don't scale. The team needs a generic
notification service similar to Slack's actionable notifications that can be leveraged across any
product. This represents a fundamental platform requirement that impacts all agentic
capabilities.

Enterprise demand for person resolution exceeds current product scope. Brandon
discovered significant enterprise interest (Disney, Workday, insurance verticals) for
person-based resolution through APIs or core Websites offering rather than just through Copilot.
This suggests a much larger market opportunity than the current front-line seller focus allows.

Custom signals infrastructure has fundamental limitations. Vinay's investigation revealed
custom signals only work for accounts/contacts with standard fields, not the custom fields most
customers actually want to use. This requires global data model integration to support real
customer use cases - a much larger technical lift than anticipated.

Cross-Team Dependencies

Our work with Query layer engineering continues to be the critical bottleneck for multiple product
initiatives. The cascade effect from query dependencies is now impacting CRM enhancements,
custom fields, dataset development, and core signals functionality. Without resolution, teams are
stuck in requirements definition rather than development execution.

GTM Plays coordination between Veronica's team (use cases), Mark Frayle's team (workflows),
and Adam's team (agentic platform) needs executive-level ownership clarity. Current multi-team
approach is creating confusion rather than alignment.

Looking Ahead

Query layer resolution is the single highest priority for unblocking multiple workstreams.
Teams across AI Audiences, CRM integration, and custom signals cannot progress from
requirements to development without this foundation. Executive intervention needed to prioritize
engineering resources here.

GTM Plays requires immediate ownership and timeline clarity. The team has the technical
capability and general alignment on direction, but needs executive decision-making on resource
allocation and clear milestone commitments. The current "too many cooks" dynamic is
preventing execution velocity.

Resource planning cannot wait for formal planning process. With Agent platform
understaffed and unclear resource allocation between major initiatives, the team needs
immediate clarity on staffing decisions to maintain momentum through H2 goals. Current
execution is being constrained by organizational uncertainty rather than technical challenges.
