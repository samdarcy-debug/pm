---
id: weekly-dai-2025-46
title: "DAI Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: dai
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

DAI Executive Roundup - [Monday
November 10, 2025 - Friday November 14,
2025]

Executive Summary

Studio and Workspace officially launched as Tier 1 products last week with strong sales
momentum, generating significant pipeline through the studio-to-workspace activation demo.
However, maintaining this momentum requires rapid product improvements as the sales team
encounters expected headwinds around AI credits pricing and workspace feature gaps. The
team is executing a two-pronged strategy: delivering tangible November/December
improvements to sustain seller confidence while building the foundational orchestration
architecture that will power differentiated experiences in plays and pulses.

This Week's Progress

Key Momentum Areas

Victor and Sneh's launch execution drove substantial early traction, with Alex Lazerovich's team
building meaningful pipeline off the studio-to-workspace integration in just the first week. The
sales team conducted the platform demo with Antuna's RNG organization and Rob Lauderman's
strategic leaders, receiving positive sentiment that while products are early, the rapid
improvement trajectory is encouraging. Brett and the team delivered the first Voice of Customer
report analyzing two weeks of sales conversations, providing an objective data foundation that
sales leadership can reference when prioritizing product decisions and objection handling.

Adam made progress unblocking the agent orchestration roadmap challenge between Studio
plays and Workspace long-running tasks, identifying a path forward that reprioritizes the A2A
message broker work. The engineering team secured additional resourcing in today's meeting,
which will prevent the work from seizing up while product-level alignment continues over the
next few weeks. This architectural decision positions the team to consolidate what were
previously separate implementations for bulk email campaigns, multi-agent tasks, and plays into
a unified orchestration system.

Ali and the engineering team established a viable path forward on the GraphQL backend
architecture dilemma between Solr and BigQuery. The team can continue using BigQuery for
engagements while Najet and Brian work through mapping scalars and operators to support the
metadata-driven model in Solr. This approach prevents the team from boxing themselves into
an architecture that won't scale while maintaining forward progress on workspace enrichment
capabilities.

Goals & Progress

Product Launch Momentum: Studio and Workspace launched as Tier 1 products with the
studio-to-workspace activation serving as the most differentiated demo in the portfolio. The next
two product releases on November 18 and December 1 are positioned as make-or-break
moments for winning over sales team confidence. Victor is balancing the December 1st bulk
email delay against the strategic decision to build on long-term orchestration architecture rather
than a hacky solution, recognizing that the time delta between approaches isn't substantial and
the right architecture will free up development resources across multiple roadmap items.

Sales Enablement and Field Readiness: The team completed comprehensive enablement
sessions covering GTM Studio foundations, Workspace capabilities, competitive landscape, and
demo deep dives. Solutions consultants are equipped to run demos in production, and VPs
each have dedicated workbooks they're activating with their reps. The first AI Action Credit
report went out tracking early consumption patterns across nine accounts, all currently on the
Studio side, establishing baseline reporting that will evolve as workspace adoption scales and
more cohorts come online.

Platform Architecture and Infrastructure: Brandon's team made strong progress preparing for
the waterfall onsite, completing design reviews and beginning dataset onboarding acceleration
work that adds three new datasets from a schema perspective. The team is documenting the
onboarding process by walking the GitHub dataset through end-to-end to identify gaps and
democratize knowledge beyond a few individuals. Jody highlighted that Clay's primary
advantage currently is waterfall, positioning the upcoming work as directly addressing the main
competitive threat with superior pricing and data quality.

Strategic Challenges

The backend architecture decision for GraphQL and query capabilities created friction this week
when the limitation between Solr and BigQuery became apparent Friday morning. While the
team established a path forward using BigQuery for engagements temporarily, Ali raised
concerns about time pressure forcing a decision that boxes the architecture into an approach
that won't work long-term. The question of how to balance immediate delivery needs against
scalable architecture remains, though Andres suggested continuing with what works while
figuring out the right solution in parallel.

Workspace is experiencing chat reliability issues that are eroding trust with internal users, with
some reporting that data is frequently incorrect or chat pulls wrong accounts for their role. Victor
noted that 60-70% of users always or often double-check data in Salesforce, and response
times are rated slower than acceptable by the majority. These quality issues, combined with
users hitting the 2000 row limit and difficulty finding relevant fields, require dedicated focus on
user experience improvements to prevent the internal perception challenges that plagued
SalesOS adoption.

Megan identified that designers aren't consistently working closely enough with engineers,
requiring product managers to serve as the middleman to ensure designs are implemented
correctly. This process gap is creating quality issues and slowing down the team's ability to ship
polished experiences. The team is working to shift designers toward direct collaboration with
engineers and taking more ownership of visual quality assurance, reducing the burden on
product management while improving implementation fidelity.

Strategic Insights

Key Learnings & Discoveries

The revenue leader persona presents an interesting product positioning challenge, as even top
revenue leaders struggle with Studio's complexity despite showing some success. Victor and
Sneh identified that workspace is the more natural environment for these leaders to work, but
this requires critical decisions around guardrails to prevent them from burning AI credits at the
same magnitude as Studio power users. The team is aligned philosophically that leaders want
to use the same tools their sellers use, making workspace audience-building capabilities
inevitable regardless of product strategy.

Dominik surfaced that real-time events integration represents significant untapped value,
particularly as website signals currently operate on a 24-hour delay. With the global event bus
and change data capture infrastructure now in place, integrating this into workspace could
deliver a major capability jump. The team validated that IBM specifically needs real-time website
resolution, and many flywheel partners require this functionality, driving Mark Farrell's current
work to hook this up via webhook. The vision is that someone visiting a site triggers a play
within a minute that surfaces to sellers.

The Voice of Customer analysis revealed that the studio-to-workspace activation naturally leads
sellers to frame the push to sales as "plays" even though the current product doesn't fully
support this mental model. View publishing solves some use cases but doesn't deliver the tasks
and to-dos that sellers expect from true play automation. This gap between sales narrative and
product capability creates pressure to accelerate plays delivery while being very clear about
which use cases the current workspace activation actually addresses.

Cross-Team Dependencies

The orchestration architecture work that Adam, Derek, and Karthik are driving has significant
implications across Victor and Sneh's product dependencies. The team scheduled a Friday
review with Nebo, Carlos, and Sneh to align everyone on the consolidated approach, which will
clarify the UX design requirements and scope of work. Sean will be added to the prioritization
sessions to ensure workspace requirements are properly represented. This unified direction
should eliminate double work between bulk email systems, task queue implementations, and
plays activation while accelerating overall delivery.

Ali and the platform team's GraphQL interface work directly impacts Victor's go-to-market data
model integration deliverables. The team is still working through the implications with Nebo,
Rakesh, and Sean as they evaluate how the Solr backend decisions affect integration timelines.
Brandon's waterfall enrichment work similarly depends on clear data integration patterns and
the GTM attribute store roadmap, requiring continued alignment between data teams and
product teams on priorities and sequencing.

Looking Ahead

Next week centers on the waterfall onsite in Bethesda where Brandon, Sneh, and their teams
will converge on audiences, plays, and waterfall architecture. This working session aims to solve
several foundational problems around audience building as a set of tasks, API access for
external tools like Cursor, and the integration of real-time data triggers. The team will focus on
making these systems work end-to-end rather than treating them as separate planning
exercises.

Victor is pushing aggressively to increase workspace demo volume by spreading examples of
successful demos across the company and conducting a blitz on workspace-solo presentations
versus the studio expansion motion that has dominated early sales conversations.
Simultaneously, the team is working to deliver a workspace pulse feed as a bridge to the full
plays-powered solution, building it in a way that can incorporate pulses from plays when ready.
This interim approach balances the need to show sales momentum now while not compromising
the longer-term architecture that will truly differentiate the product.

The team continues balancing rapid iteration velocity with the need for stability, as Mary's
feedback about moving too fast highlights the importance of over-communication through
release notes and automated updates. Brett is working to solve the communication challenge
without slowing down product improvement speed. With aggressive goals through the end of the
year and teams running hot in a productive way, the focus remains on maintaining momentum
while solving the orchestration, architecture, and quality challenges that will determine Q4
success.

Source: DAI Executives Operating Framework entries from [Monday November 10, 2025 -
Friday November 14, 2025]
