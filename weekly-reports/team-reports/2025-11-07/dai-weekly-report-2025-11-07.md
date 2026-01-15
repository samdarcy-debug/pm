---
id: weekly-dai-2025-45
title: "DAI Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: dai
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

DAI Executive Roundup - [Monday
November 3, 2025 - Friday November 7,
2025]

## Executive Summary

GTM Workspace and GTM Studio achieved sales-ready and customer-ready status on
November 3rd, marking a pivotal milestone with 1,000+ sellers now actively demoing to
customers. Early signals are promising: Alex Lazerovich's team generated approximately $1.7M
in pipeline from a single prospecting day, and the platform demo is fundamentally shifting how
customers perceive ZoomInfo--from a thin data wrapper to a comprehensive GTM platform.
However, the team faces immediate challenges around field enablement gaps, particularly on AI
credit positioning where sellers understand mechanics but lack confident talk tracks for
customer conversations. The week revealed the business is consuming ~140,000 AI credits
weekly ($7,000/week or $350,000 annualized), demonstrating proof of concept but requiring
urgent focus on credit consumption reporting and change management to align the organization
around this new North Star metric.

## This Week's Progress

### Key Momentum Areas

Victor Oliveros and Sneh Kakileti led their teams through the successful November 3rd launch
of sales-ready and customer-ready GTM Workspace and Studio products. The platform demo
resonates strongly with customers, with sellers reporting that ZoomInfo is "no longer just a thin
app wrapper around the data moat" but a comprehensive platform solution. Solution consultants
have already booked 47 demos for November, with 8 quotes currently outstanding, indicating
strong early traction in the field.

Adam Smith advanced critical infrastructure work by mapping out the pulses and message
broker roadmap for November delivery, while simultaneously addressing latency and
optimization concerns that are directly impacting user experience. The team identified
low-hanging fruit for immediate performance improvements while planning longer-term
infrastructure investments, ensuring both near-term wins and sustainable scaling.

Brandon Tucker made progress on waterfall enrichment capabilities, with business email
enrichment nearly complete in Solr and mobile phone data work underway. The team identified
a path to add approximately 100 million contacts to support improved match rates, though
longer-term Solr capacity planning remains a focus area for the upcoming data team onsite.

## Goals & Progress

GTM Workspace & Studio Launch: Victor Oliveros and Sneh Kakileti successfully delivered
the November 3rd sales-ready and customer-ready milestone after months of intensive work
from product, engineering, and design teams. The field is now actively demoing to customers
with visible momentum--Alex Lazerovich's prospecting day generated ~$1.7M in pipeline, and
sellers consistently report that customers see the next-generation ZoomInfo vision. November
priorities focus on studio-to-workspace integration improvements, next-generation artifacts
based on sales use cases, and visible product enhancements to maintain field confidence
through the inevitable wins and losses of early customer adoption.

AI Credits Infrastructure & Adoption: AJ Belen and the team finalized customer-facing AI
action credit assets for both economic buyers and end users, completing the foundation for
go-to-market motions. However, a critical gap emerged: while sellers understand the nuts and
bolts of packaging through enablement sessions from Adam Smith, Mark Harris, and Jesse
Lindstrom, they lack confident talk tracks, objection handling, and simulation-based practice for
actual customer conversations. Internal ZoomInfo usage demonstrates the model's
potential--consuming ~140,000 AI credits weekly ($350K annualized), which would rank as a
top 1,000 customer--but systematic change management and reporting infrastructure are
needed to drive this as the company's primary growth metric.

Platform Infrastructure & Performance: Adam Smith worked with engineering leadership to
advance November roadmap items including the A2A message broker for pulses, though
resourcing gaps require resolution with Carlos Nunez and Derek in the coming week. The team
identified efficiency and optimization as critical for addressing latency concerns--a one-for-one
correlation exists between inference optimization and speed. Ryan Stevens and Lars are
tackling low-hanging fruit while the team evaluates whether to resource additional work through
Nebo's team for artifacts, enabling parallel execution streams rather than bottlenecking on the
core agentic team.

## Strategic Challenges

The team identified significant enablement gaps around AI action credits that go beyond asset
creation. While foundational understanding exists through recent training sessions, sellers lack
the offensive positioning, confident talk tracks, and objection handling capabilities needed for
customer conversations. The current approach is overly defensive--focused on concerns about
overspending and refund requests rather than selling the transformative value. This gap
requires more than documentation; it needs role-playing simulations, team meeting practice,
and top-down messaging from sales leadership showing aggressive customer conversations
about AI credits, similar to how enterprise software companies transitioned to subscription
models.
Resource allocation and team overlap emerged as a concern across multiple workstreams.
Dominik Facher noted that multiple engineering teams and PMs are effectively working on
similar problems in different directions, particularly around plays and automation capabilities.
This creates inefficiency and potential for duplicated effort. The team needs to rationalize
resource allocation and ensure clear swim lanes, especially as they transition from chasing
individual roadmap items to building sustainable platform primitives.

Data management infrastructure faces scaling challenges as the team accelerates dataset
onboarding for GTM Studio. Brandon Tucker discovered that while processes are documented,
they require too many handoffs and deep expertise across multiple teams. For the vision of
dozens to hundreds of datasets next year, the team must templatize and democratize these
processes rather than relying on manual coordination and specialized knowledge. The
upcoming data team onsite will focus on converting this from a planning session to a working
hackathon to address these bottlenecks.

## Strategic Insights

### Key Learnings & Discoveries

The platform demo's success reveals a fundamental shift in customer perception. When
executed well, customers begin pitching the vision back to the team rather than raising
objections, and pricing conversations naturally emerge as a next step rather than a barrier. This
validates the strategic bet on unified platform positioning over point solutions. However, Victor
Oliveros observed that Workspace is evolving into half productivity app and half micro-app
delivery channel--views serve as the data source, and artifacts built on top create the "aha
moments" where customers' eyes light up. This insight should guide January roadmap
prioritization.

The conversational intelligence opportunity with semantic data emerged as a major
monetization path through discussions between Adam Smith and Sneh Kakileti. Rather than
explaining bike processing to customers, the team can package semantic capabilities as tiered
conversational intelligence features in Studio, creating a clearer value proposition and revenue
model. This represents a significant unlock for driving both product adoption and credit
consumption.

Competitive positioning crystallized around two primary threats: Clay and Gong. Brandon
Tucker's partnership work on DMV and other data sources provides answers to Clay, and the
team has high confidence in delivering a convincing Clay response by January. However, Gong
represents a more significant challenge--they lead in mindshare despite product shortcomings,
and customers consistently cite that "reps like it, but it's expensive." Victor Oliveros assessed
the current gap as Gong having A-minus offerings on conversational intelligence and action
layer while ZoomInfo has C-minus, requiring urgent catch-up work on both capabilities.

## Cross-Team Dependencies
Platform infrastructure work led by Adam Smith, Ali Sadat, and engineering teams continues to
be foundational for both Workspace and Studio delivery. The team must resolve resourcing for
the A2A message broker and pulses work by engaging Carlos Nunez and Derek, while also
ensuring clear ownership of the conversational intelligence roadmap now that Adam Smith has
taken over Bert Lui's team. The feed experience from Copilot V1 demos exceptionally well but is
missing from Workspace, creating an immediate dependency that requires bridging
work--potentially through pre-generated artifacts for each user--before the full pulses vision
delivers in January or February.

Enablement and GTM leadership engagement remains critical for successful market adoption.
AJ Belen identified that while foundational training exists, Gabe Sweet's enablement team lacks
a structured plan for talk track development, objection handling, and simulation-based practice.
This requires top-down intervention from sales leaders like Breyers and Tuna, potentially
including video examples of aggressive customer conversations, to shift the field from defensive
to offensive positioning on AI credits.

## Looking Ahead

The immediate priority for the week of November 10th centers on maintaining field confidence
through rapid iteration on user experience improvements and quick wins. Both Victor Oliveros
and Sneh Kakileti identified specific, high-impact improvements--filterable views, display
optimizations, Studio-to-Workspace activation flows--that can ship quickly to demonstrate
product momentum. These small changes compound to create meaningful sentiment shifts with
the sales organization.

Credit consumption must become the organizational North Star, requiring several coordinated
efforts. AJ Belen will deliver the first weekly credit consumption report showing both aggregate
consumption and cohort-based analysis by entitlement start date. Adam Smith will lead R&D
all-hands enablement on how credits work and the platform's future app store model where
anyone can ship agents, plays, or services in a credit-driven marketplace. Dominik Facher
emphasized the urgency of this mindset shift--every person in the organization should wake up
knowing how many credits were consumed the previous week, with 2026 operating cadence
and focus working backwards from exponential credit growth.

The team must address the "feed gap" between current Workspace capabilities and customer
expectations set by Copilot V1. Victor Oliveros, Adam Smith, and Sneh Kakileti will explore
bridging solutions--potentially pre-generated artifacts for each user that surface prioritized
actions and insights--while the full pulses vision remains on track for January/February delivery.
This work unlocks the platform story of consolidating scattered tools and attention into a single,
prioritized workflow. Parallel efforts on conversational intelligence positioning, Gong competitive
capabilities, and infrastructure optimization will position the team to accelerate through Q4 and
into the critical planning window for 2026.
Source: DAI Executives Operating Framework entries from [Monday November 3, 2025 - Friday
November 7, 2025]
