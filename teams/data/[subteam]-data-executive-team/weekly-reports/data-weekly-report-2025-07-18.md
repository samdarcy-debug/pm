---
id: weekly-data-2025-29
title: "Data Weekly Report - July 18, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-07-18
updated: 2026-01-06
week_ending: 2025-07-18
reporting_period: "July 14-18, 2025"
tags: ["weekly-report", "Q32025"]
---

Data Team Executive Roundup - Monday
July 14th - Thursday July 17th

Executive Summary

The Data Team delivered strong momentum this week with multiple high-impact
initiatives progressing, but critical infrastructure dependencies threaten to derail Q3
execution. The team achieved 90%+ completion rates on key goals including contractor
dataset delivery, mobile phone infusions, and compliance initiatives. However, a significant
blocker has emerged: 50% of contact phone and email source data is missing from BigQuery,
which could severely impact PTI's transition and our data quality metrics. This requires
immediate engineering leadership intervention to prevent disruption to multiple data pipelines
and customer-facing systems.

This Week's Progress

Key Momentum Areas

Contractor Dataset Success: The team successfully delivered the contractor cube with strong
early market signals, including several demos booked by the GTM team. This represents our
first major vertical dataset launch with proven demand validation, providing a template for future
dataset releases. The delivery included complete GTM materials, enablement sessions, and
prospect targeting integration into GTM Studio.

Mobile Data Expansion: Dana's team achieved 95% completion on the 10 million mobile
phone infusion from Statara, implementing enhanced QC and validation processes. The team is
targeting 6 million attached phones from this infusion, with comprehensive analysis of
non-attached numbers providing insights for process optimization. An additional 29 million
international phones are in progress from Datagma with improved API throughput.

Compliance and Infrastructure: Rob successfully restored cookie banners across all 15+
ZoomInfo domains, returning the organization to full regulatory compliance. The team also
identified and escalated critical Google Tag Manager issues affecting lead flow, with
recommendations for direct Google engineering consultation to resolve cookie loading
problems.

Goals & Progress
Data Assets Consolidation: Dow's initiative to create a unified internal roadmap view
progressed to 90% completion, consolidating multiple dataset development efforts into a single
trackable system. This includes pre-selling materials for upcoming datasets, enabling GTM
teams to validate customer requirements early in the development cycle and collect specific
attribute needs from sophisticated prospects.

Semantic Data Enhancement: Brandon Wilson's semantic data-enhanced signals project
achieved 80% completion with 15 additional signals sent to AMs for review. The team added
100 accounts with upcoming renewals to improve signal relevance and accuracy. Integration of
the re-ranker API endpoint is underway to optimize data relevance and reduce prompt service
calls.

Company Definition Implementation: Ethan's company definition work reached 50%
completion, with customer-facing materials being refined based on stakeholder feedback. The
definition has received strong positive reception from Anne's team, with eager anticipation for
database-wide rollout. Customer call scheduling and engineering requirements development are
next priorities.

Strategic Challenges

Critical Infrastructure Gap: A severe data availability issue has emerged where 50% of source
data for contact phone and email records are unavailable in BigQuery. This creates a
fundamental blocker for PTI's smooth transition from Snowflake, potentially impacting multiple
data pipelines and customer-facing systems. The root cause appears to be related to data
warehouse architecture decisions that separate 5x5 data (in Snowflake) from contact records (in
BigQuery), creating cross-platform query complexity.

Resource Allocation Pressure: The team is experiencing significant analysis resource
constraints, with Ethan and Jody both citing competing priorities and limited bandwidth. This
bottleneck affects multiple high-priority initiatives including company definition implementation,
H2 roadmap refinement, and customer validation processes. The team needs clearer
prioritization alignment and potential resource augmentation to maintain execution velocity.

Authentication and Platform Dependencies: Jody's agentic platform development faces
technical blockers with Google IAP authentication requirements for Person and Company
traceability APIs. While the team is working through codebase modifications, this represents a
pattern of platform dependencies that could slow innovation cycles and limit the team's ability to
deliver rapid prototypes and solutions.

Strategic Insights

Key Learnings & Discoveries
Vertical Dataset Go-to-Market Strategy: The contractor dataset launch revealed that vertical
datasets require a fundamentally different enablement approach than horizontal data products.
Success depends on high-touch, targeted engagement with strategic and enterprise sellers
(80/20 rule in effect), rather than broad-based marketing campaigns. This insight should inform
all future vertical dataset launches and resource allocation decisions.

Data Quality Impact Analysis: The team's enhanced QC processes for mobile phone infusions
are yielding valuable insights about attachment rates and quality optimization opportunities.
Early analysis suggests significant potential for improving data utilization efficiency, with
opportunities to "squeeze more juice" from existing data sources through better validation and
post-processing techniques.

Agentic Platform Potential: Despite authentication challenges, the agentic platform shows
promise for delivering "80% solutions" with significantly faster iteration cycles than traditional
development approaches. This represents a strategic capability that could accelerate the team's
ability to prototype and deliver value, reducing dependency on lengthy engineering cycles.

Cross-Team Dependencies

Our work with Engineering teams on infrastructure migrations requires urgent prioritization and
clear ownership assignment. The BigQuery transition affects multiple teams beyond Data, and
the current gaps in data availability threaten Q3 delivery commitments. We need immediate
engagement with PTI leadership to establish transition timelines and mitigation strategies.

The relationship with GTM teams continues to strengthen with positive early signals on
contractor dataset adoption. However, we need systematic tracking of seller engagement with
recommended accounts to ensure dataset investments translate to revenue outcomes.
Consider implementing automated reporting on GTM Studio usage patterns for vertical
datasets.

Looking Ahead

Q3 execution depends on resolving the BigQuery data availability crisis within the next
week to prevent cascading delays across multiple initiatives. The team has demonstrated
strong execution capability with 90%+ goal completion rates, but infrastructure dependencies
could derail progress without immediate intervention.

Next week's priorities center on three critical areas: completing the BigQuery migration solution
with engineering leadership, finalizing the restaurant dataset for GTM readiness, and
establishing clear H2 roadmap priorities to optimize resource allocation. The team's momentum
on semantic data enhancements and agentic platform development positions us well for
accelerated innovation cycles, provided we can resolve the foundational infrastructure
challenges.
The Data Team continues to demonstrate exceptional execution velocity and strategic thinking,
but success requires executive support in resolving cross-functional dependencies and ensuring
adequate resource allocation for high-impact initiatives.
