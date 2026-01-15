---
id: weekly-copilot-2025-40
title: "GTM Workspace (Copilot) Weekly Report - October 03, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-10-03
updated: 2026-01-06
week_ending: 2025-10-03
reporting_period: "September 29-October 03, 2025"
tags: ["weekly-report", "Q42025"]
---

SalesOS/Copilot Executive Roundup -
[September 29, 2025 - October 3, 2025]

Executive Summary

Copilot Workspace launched successfully to the full GTM organization with 851 users logging in
within 24 hours, though the rollout exposed misalignment in LaunchDarkly configuration that
required manual one-by-one user additions throughout late Wednesday. Adam Severance
handled the scramble while new company and contact profiles advanced to engineering kickoff
with an estimated 140 dev days of work targeting mid-November delivery. The profiles will
showcase Next Best Actions agent, buyer engagement maps, and consolidated intelligence
signals exclusively for Workspace customers, positioning these as compelling differentiators for
upsells. Demo mode implementation for the October 6th showcase is complete and ready for
Monday release, though workbook-to-workspace demo flow still requires Workspace
configuration in the demo Salesforce instance.

This Week's Progress

Key Momentum Areas

Adam Severance coordinated the internal Workspace launch despite significant LaunchDarkly
configuration challenges, ultimately delivering a 500% increase in logins between Wednesday
and Thursday as the GTM organization gained access. The homepage artifacts are proving
accurate for end-users, with 7-8 sellers confirming their featured deals were both actively
worked and genuinely important, validating the routing logic improvements. Instrumentation
gaps remain as Amplitude reporting was configured for specific cohorts rather than dynamic
GTM team filtering, requiring AJ's team to develop new approaches for measuring the 851-user
influx engagement.

Harinath Krishnamoorthy validated Data Science team fixes that generated recommendations
for 1,200-1,300 additional customers beyond the previous 3,400 baseline, though
comprehensive quality evaluation remains incomplete. The topic migration prototype moved to
engineering handoff, but discovery revealed problematic fragmentation across at least three
separate teams building overlapping Intent recommendation agents in chatbot implementations.
Multi AFS and Intent Recommendation Phase 2 features are on track for October 21st launch
with LRT tickets completed and comprehensive test plans in development.

David Goulden's Admin Defined Territories work continues moving gradually through scoping
alignment with Tingting's team, while Mohan and Mark are building staging implementations for
workbook activation with defined territory routing. The team is exploring whether territories
should expose through query-based or tag-based models in Workspace, recognizing this won't
be immediately available at GA but requires thoughtful architecture decisions. Priority Accounts
based on GTM Data Model remains blocked on understanding real-time data access patterns,
as the current ZDP data structure requires daily snapshot views rather than immediate
availability.

Goals & Progress

Copilot Workspace: The September 26th internal launch delivered strong initial adoption with
851 GTM users logging in despite Wednesday's configuration challenges that Adam resolved
through manual additions. Engagement data from AJ shows solid activity though
instrumentation needs refinement to filter out product and engineering teams from GTM-specific
metrics. Homepage artifacts are hitting the mark for individual contributors and sales managers
(within hierarchy limitations), with workbooks-to-workspace connection experience scoped for
October 20th delivery bringing email sequencing plays to homepage cards. Views
improvements are queued including resizable columns, unified hovers, improved multi-field
filtering, and one-to-many fixes, though many P0/P1 bugs and the launch consumed bandwidth
that delayed this foundational work.

ZoomInfo Intent: Intent Recommendation saw a substantial 1,295 customer adoption jump in
week four following bug fixes, though Harinath's quality precision analysis remains incomplete to
confirm whether increased reach translates to improved value. The topic migration utility
prototype successfully deployed to staging and handed off to engineering, but uncovered
concerning duplication where Russell's team, the onboarding team, and the GTM team each
built similar crosswalk experiences independently. Multi AFS is tracking for October 21st beta
launch in ZIM with 800 customers providing testing ground before Copilot expansion, while
comprehensive test plans cover both Multi AFS and Intent Recommendation Phase 2 across
functional, integration, and user acceptance scenarios.

Admin Zero Experience: David's zero admin setup work is moving gradually through scope
alignment and domain ownership discussions with Tingting's team, constrained by the
abbreviated week due to Yom Kippur holidays. Defined Territories is progressing toward GA with
content pack enablement materials nearly complete, though questions remain about whether
the V1 homepage feed warrants immediate release or should wait for additional territory
capabilities. The team is prototyping territory routing for workbooks activation while exploring
MCP wrapper approaches to simplify API exposure, with User Summary screen designs still
requiring resource allocation and final UI positioning decisions.

Additional Initiatives: Dylan Halladay's slide artifacts work hit a fork requiring product direction
between Google Slides API (matching ZI Chat's corporate template approach but limited in
capability) versus PowerPoint implementation (more flexible but cannot render in-app and lacks
template access). Ant Cuomo's mobile V2 prototype achieved chat functionality in web view with
custom native Notes implementation, targeting end-of-October test flight with basic Pulse feed if
progress continues. Gabe Pirela's MEDDPICC extraction internal pilot kicked off via Slack
integration with test users enabled, though the focus shifted from quote extraction toward
note-style outputs based on early feedback.

Strategic Challenges

Workspace's first-time user experience requires substantial improvement despite successful
rollout, with chat context accuracy emerging as the top user complaint alongside high latency
and views usability gaps around Salesforce field complexity. Adam's team is addressing
instrumentation to properly track GTM-specific engagement without conflating product and
engineering usage, while the homepage artifact latency issues may stem from Anthropic service
problems or require Lars' deployment fixes. The challenge extends beyond bugs to fundamental
experience design, as the team hasn't yet delivered compelling aha moments that drive
sustained adoption beyond initial curiosity logins.

The new company and contact profiles face heavy dependencies on GTM Data Model and GTM
Store that will force technical debt decisions similar to current Workspace implementation
patterns. Ant needs to consume engagement data from Chorus pipeline rather than the model
due to availability gaps, while multiple profile features require data that either doesn't exist in
GTM Data Model or suffers from latency that makes features like Next Best Actions less
actionable. The Monday meeting with Victor, Andres, and Sarah will clarify which dependencies
can be resolved versus which require workarounds, but Dominic's push to use profiles as a
forcing function for GTM Data Model improvements suggests this is a broader platform issue
affecting multiple teams.

David's Priority Accounts work based on GTM Data Model hit blocking uncertainty about data
freshness, as ZDP data flows through snapshot views with daily cadence rather than real-time
availability. While account changes happen infrequently, customers expect immediate visibility
when they do occur, creating disproportionate noise when delays surface. Engineering hasn't
yet determined how to query GTM Data Model directly or whether missing snapshot views could
enable faster access, leaving work breakdown and dependency analysis stalled until the team
understands consumption patterns and whether this represents a fundamental platform
limitation or solvable configuration gap.

Strategic Insights

Key Learnings & Discoveries

Internal launch preparation would benefit from more structured planning, as the Wednesday
rollout chaos revealed gaps in cross-functional alignment around LaunchDarkly configuration,
error handling logic, and fallback procedures when automation fails. The number of users
reaching out with access errors created a "black eye" according to Adam, despite ultimately
delivering 851 successful logins. Future internal launches--which the roadmap indicates will be
frequent--need documented playbooks covering feature flag strategies, staged rollout
procedures, and support escalation paths to avoid requiring product managers to manually add
users one-by-one late into the evening.

Harinath's Intent work uncovered systemic fragmentation where multiple teams independently
built overlapping recommendation agents without visibility into each other's efforts. At least three
separate implementations exist for Intent topic recommendations and competitor keyword
crosswalks, representing duplicated engineering investment and creating inconsistent user
experiences depending on which entry point customers use. The lack of centralized governance
for AI agent development means feature requests get split across scattered systems rather than
strengthening unified capabilities, creating technical debt in the AI tooling layer that becomes
increasingly expensive to unwind over time.

The profiles dependency discussion revealed that data latency is a major offsite theme affecting
multiple workstreams, not just an isolated challenge. Victor's questioning about GTM Data
Model delays exposed that Ant's profiles work, David's Priority Accounts initiative, and the Next
Best Actions agent all face similar constraints around data freshness and availability. The
pattern suggests platform-level architectural decisions about batch processing versus real-time
data access are creating compound friction across product development, requiring executive
attention to determine whether investment in platform infrastructure changes would unlock
multiple teams simultaneously.

Cross-Team Dependencies

Our work with the Agentic Platform team on Next Best Actions, profiles, and the discovery agent
for mobile requires close coordination as Ant pressure-tests outputs against ZI Chat gold
standards using maximum context. Ryan Stevens and Lars Vedo remain key dependencies for
agent architecture and chat component support, with mobile work specifically blocked on Lars
and Praveen delivering chat in webview functionality. The agent builder tooling represents a
potential unlock for scalability, as the current manual process for NBA development doesn't
scale to the number of agents the team envisions building.

Coordination with GTM Data Model and Platform teams led by Andres became more urgent this
week, with Dominic explicitly suggesting profiles should serve as a forcing function to drive
platform improvements. Monday's meeting will catalog specific data gaps including engagement
feeds, account team relationships, and custom CRM fields that either don't exist in GTM Data
Model or suffer from latency issues. Sean's team also requires alignment on territory
implementation in Workspace beyond workbooks activation, particularly around whether
territories become queryable objects in chat and views or remain backend routing logic.

Looking Ahead

Next week's primary focus continues improving first-time user experience following the internal
Workspace launch, with instrumentation fixes enabling proper GTM engagement tracking and
views quality-of-life improvements addressing the multi-field filtering confusion that generates
multiple weekly support questions. Adam will advance homepage artifact logic for sales
managers now that hierarchy access is available, while defining next persona-specific FTUE
improvements based on early user feedback patterns.

The profiles team kicks off development Monday following Ant's design finalization with Katya
and Lindsey, though the 140 dev day estimate and mid-November target may require splitting
across the November 3rd and December 1st release trains pending Sarah Heritage's unified
roadmap publication. The Monday platform dependency meeting with Victor, Andres, and Sarah
will determine which profile features require GTM Data Model improvements versus technical
debt workarounds, directly influencing whether the team can deliver the full vision or needs
scope reduction. Simultaneously, Dylan will finalize slide artifact direction between Google
Slides API and PowerPoint approaches, with engineering ready to implement once product
requirements are confirmed.

Harinath completes Intent Recommendation quality evaluation to validate whether the 1,295
customer adoption surge represents genuine value improvement or just broader distribution of
recommendations. Multi AFS and Intent Recommendation Phase 2 move into comprehensive
testing against October 21st launch commitments, while the topic migration work needs
consolidation discussions with the other teams building overlapping crosswalk agents. David
continues Admin Defined Territories alignment on GA scope and packaging, recognizing that
workbooks routing requirements may influence final territory capabilities and whether bulk
upload approaches need simplification before broader rollout beyond beta customers.

Source: Team SalesOS/Copilot Operating Framework entries from [September 29, 2025 -
October 3, 2025]
