---
id: weekly-copilot-2025-39
title: "GTM Workspace (Copilot) Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

SalesOS/Copilot Executive Roundup -
[September 22nd - September 25th, 2025]

Executive Summary

Copilot Workspace rolled out to 100 additional users this week. The team is rapidly addressing
user feedback, which is centered around view creation, chat context, and chat latency. Users
speak highly of the email composer and company profiles. The team is also making
improvements to the first time user experience by adding manager/leader presets in addition to
AE/AM presets. The goal is for 100% of users to have a valuable first time user experience.

This Week's Progress

Key Momentum Areas

Copilot Workspace successfully activated 100 additional AEs and AMs on Wednesday,
generating substantial user feedback that's driving product improvements. The primary pain
points for users are 1) View creation 2) Chat context. Users provided feedback that the chat
beside a view refers to accounts and opportunities not present in the view. The team deployed a
fix Friday morning.

ZoomInfo Intent platform achieved significant competitive positioning wins through Harinath
Krishnamoorthy's completion of Multi AFS launch preparation and automated migration
experience design. The Multi AFS feature addresses enterprise customer requests for
expanded Account Fit Score capabilities, while the automated migration tool eliminates weeks
of manual onboarding when customers switch from 6sense/DemandBase, directly supporting
revenue growth targets against established competitors.

Admin Zero Experience progress continues through David Goulden's coordination with Tingting
on scoping documentation, though work was limited due to reduced availability this week. The
zero admin setup initiative remains essential for reducing onboarding time to 5 days and
accelerating time-to-value for new organizations, with next steps focused on domain ownership
alignment and broader team coordination.

Goals & Progress

Copilot Workspace: The goal is to have 100% of users to get a valuable first time experience.
This is the biggest determinant of whether a user will become a returning user. User feedback
reveals chat as the primary pain point, with users unable to get correct context about their
accounts, opportunities, and team hierarchies. The team deployed out-of-the-box views and
homepage artifacts with persona-specific routing for sales managers and leaders, though
latency concerns may require reverting to manual behavior.

ZoomInfo Intent: Harinath Krishnamoorthy completed comprehensive analysis for Multi AFS
launch, securing stakeholder alignment from VP of Sales on package strategy and coordinating
with Provisioning teams on technical implementation. The automated Intent migration
experience design received validation from teams managing competitive migrations, positioning
ZoomInfo ahead of 6sense/DemandBase in customer onboarding efficiency. Intent
Recommendation evaluation framework established baseline performance metrics, though gap
remains between technical precision and measurable customer success outcomes.

Admin Zero Experience: David Goulden reports no additional progress this week due to limited
working days, though Tingting advanced scoping documentation work. Admin Defined
Territories remains blocked on final UI positioning decisions for User Summary report and
securing design resources. Priority Accounts based on GTM data model faces continued
dependency on federated search work, with escalation from HPE/Juniper highlighting urgent
need for Account Team Member object relationships to drive user context.

Additional Initiatives: Ant Cuomo finalized Workspace demo flow for October 6th deployment,
implementing demo mode with row limits for performance and sensitive data redaction. Dylan
Halladay delivered draft requirements for Salesforce validation rule handling and kicked off
slides artifact development with Lars' team. Gabe Pirela continued email agent optimization
work and conducted MEDDPIC extraction pilot feedback sessions, while mobile V2
development progressed on core functionality with chat integration challenges identified.

Strategic Challenges

Copilot Workspace faces user experience friction with prospecting queries. Users consistently
attempt prospecting queries ("financial services companies, 500-1000 employees, East Coast")
but these have produced unreliable results. The second friction point occurs when a user
attempts to build views using chat. This produces subpar results when creating views (Need
more than 1 column added) and does not work for ZI views.

ZoomInfo Intent platform needs clearer connection between technical performance and
customer success metrics. While Harinath Krishnamoorthy's AI evaluation framework
established precision benchmarks comparing OpenAI vs Gemini models, the evaluation lacks
direct ties to revenue impact or deal cycle acceleration. The 30+ sample evaluation provides
solid model selection foundation, but future iterations must incorporate customer engagement
rates, intent signal conversion, and sales velocity metrics to create comprehensive assessment
aligned with competitive positioning goals against 6sense and DemandBase.

Engineering resource constraints emerging as October 6th approaches, with Adam Severance
noting much less dev capacity available next week due to team member availability. The
combination of Anthropic performance issues, mobile team holiday schedules, and competing
priorities around homepage artifact latency creates timing pressures for critical improvements.
While the team has contingency plans to revert homepage artifacts to manual shortcuts if
performance doesn't improve, the broader challenge requires coordination between multiple
engineering teams for chat optimization and user experience fixes.

Strategic Insights

Key Learnings & Discoveries

Users find value in what we consider to be foundational use cases: View creation, prospecting
using natural language, and cross object insights. The team will focus on chat improvements,
Salesforce integration, user context accuracy, and fundamental prospecting query support. The
learning reinforces that premium AI experiences require excellence in core functionality before
advanced features.

Demo strategy insights from Ant Cuomo reveal that focusing on basic capabilities like email
composition resonates more strongly with users than complex features. Victor Oliveros noted
that ending demos with "write an email for me" consistently generates positive reactions, while
complex view creation attempts often fail due to latency. This suggests market positioning
should emphasize reliable, immediately useful AI assistance rather than cutting-edge
capabilities that perform inconsistently.

Revenue team validation that Intent remains critical differentiator in renewal and expansion
discussions. Victor Oliveros observed Intent being cited repeatedly as renewal driver in Tuna's
All Hands meeting, confirming the strategic value of Harinath Krishnamoorthy's Multi AFS and
migration automation work. This reinforces the importance of Intent query support in Copilot
Workspace as users inevitably progress from basic CRM management to advanced prospecting
workflows.

Cross-Team Dependencies

Our work with Engineering teams on chat latency optimization continues to be essential for
October 6th success. Adam Severance and Lars are coordinating sub-agent architecture
improvements and Anthropic performance optimizations, while Ryan Stevens develops
proof-of-concept for sensitive data redaction in chat responses. Specific support needed from
Lars and Praveen teams for mobile chat integration within web view containers.

Coordination with Provisioning team remains critical for Intent platform scalability. Harinath
Krishnamoorthy established clear timeline with Provisioning team for Intent Cluster limit
entitlement migration, enabling Enterprise customers to access 50 clusters while supporting
Custom Topic entitlements for monetization. This dependency management prevents
deployment bottlenecks while ensuring proper access controls for advanced features.
Looking Ahead

Primary focus shifts to addressing fundamental user experience gaps identified in the 100-user
rollout before broader Copilot Workspace deployment. The team will prioritize chat
improvements, with specific emphasis on prospecting query support and Salesforce context
accuracy that users expect as baseline functionality.

Key technical improvements target chat architecture optimization through sub-agent
implementation, starting with Gabe Pirela's email sub-agent as foundation for broader
orchestrator pattern. This approach should reduce latency by distributing reasoning across
specialized agents rather than single monolithic system, while Lars' team implements
mobile-friendly chat components for native app experience. Adam Severance continues
synthesizing user feedback for view functionality improvements, while Ant Cuomo finalizes
demo flows that showcase reliable capabilities rather than aspirational features.

Strategic preparation for post-October 6th expansion includes Harinath Krishnamoorthy's
completion of Intent platform enhancements that position ZoomInfo competitively against
6sense/DemandBase, while David Goulden advances Admin Zero Experience and Territory
management capabilities that reduce enterprise onboarding friction. The team maintains
confidence in delivering meaningful value through focused execution on core user needs rather
than feature breadth.

Source: Team SalesOS/Copilot Operating Framework entries from [September 22nd -
September 25th, 2025]
