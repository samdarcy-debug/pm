---
id: weekly-copilot-2025-43
title: "GTM Workspace (Copilot) Weekly Report - October 24, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "Q42025"]
---

SalesOS/Copilot Executive Roundup -
[Oct. 20, 2025 - October 23, 2025]

Executive Summary

Copilot Workspace shipped critical workbook-to-workspace functionality to production this week,
completing a major milestone for migrating legacy workflows. Sean Walter is leading a quality
assessment framework ahead of November 3rd release, identifying chat stability and view
performance as top priorities that need attention. Meanwhile, Gabe Pirela confirmed
dependencies for outreach integration--a frequently requested feature that was a friction point
in V1--with development starting next week targeting fast-follow to 11.3 release.

This Week's Progress

Key Momentum Areas

Copilot Workspace achieved a significant technical milestone with workbook-to-workspace
activation going live in production. Adam Severance confirmed the end-to-end flow is
operational and faster than previous iterations, with artifact generation notably improved. This
unlocks the ability to demonstrate seamless migration from legacy workbooks during executive
demos, supporting the positioning that Workspace represents evolution rather than disruption
for existing workflows.

ZoomInfo Intent launched Multi AFS and Intent Recommendation Phase 2 to production in ZIM
this week. Harinath Krishnamoorthy validated both features are live and stable, though
discovered an entitlement conflict for customers holding both Copilot and ZIM seats that
requires platform-level resolution. The team is working with provisioning to deliver a proper API
for determining AFS limits at the organizational level rather than user level, eliminating admin
confusion about configuration capabilities.

Admin Zero Experience work was deliberately paused by David Goulden given uncertainty
about scope and ownership with Tingting's team handling broader offerings setup. While this
removes immediate November pressure, it reflects strategic alignment that Workspace will
inevitably need admin screens but rushing artificial deadlines without organizational readiness
creates downstream problems. David is instead focusing Admin Defined Territories toward GA in
November with final UI tweaks for user summary reports.

Goals & Progress
Copilot Workspace: Sean Walter established a quality go/no-go framework identifying four
must-have elements for November 3rd: chat accuracy on core AEAM use cases, reliable view
creation from chat using CRM and ZoomInfo data, views improvements for quality of life and
polish, and first-time user experience optimization. Adam Severance's user survey at 75
respondents reveals users rate chat accuracy and speed as neutral, indicating improvement
needed before wide release. Dylan Halladay made substantial progress on slides artifact with
working PDF download and basic templates, targeting early November internal release before
customer rollout.

ZoomInfo Intent: Harinath completed validation testing for Intent Recommendation Phase 2
and Multi AFS in production, achieving the October 21st launch target. Demo instance
configuration remains blocked pending provisioning team resolution of package setup through
fullbox2 system. The team scheduled three enterprise customer interviews next week to gather
feedback on intent recommendation quality, continuing the validation approach of testing with
real customer scenarios before broader rollout.

Admin Zero Experience: Work formally deferred this week as David Goulden confirmed with
Victor that artificial rushing of admin portal features without clear organizational alignment on
scope and ownership creates more problems than it solves. The team will revisit in 2-4 weeks
as Workspace admin requirements become clearer through actual usage patterns. Meanwhile,
admin-defined territories continues toward November GA with user summary reports and
territory assignment UI refinements in development.

Additional Initiatives: Gabe Pirela made critical progress on send via Outreach functionality by
identifying the full dependency chain--contacts must first exist in Outreach before sending,
requiring export flow implementation. Rather than just adding a send button, the team scoped
the complete workflow including contact verification and sequence addition. Ant Cuomo's Next
Best Actions agent reached production with improved engagement context from GTM data
store, though the account prioritization agent missed Monday's release and should deploy by
end of week.

Strategic Challenges

Copilot Workspace faces a compound challenge around chat-to-views accuracy that Sean
Walter flagged as the top priority for November 3rd. The team is seeing inconsistent results
when users ask chat to create views, particularly when mixing CRM and ZoomInfo data. Adam
Severance is building out golden query examples to train the orchestrator agent, but the
underlying issue stems from limited documentation on the GTM data model's GraphQL
endpoint. This creates a scenario where the product technically works but doesn't reliably
deliver on the core promise of natural language view creation, which multiple sales leaders
identified as their primary blocker to running their business in Workspace.

ZoomInfo Intent discovered an architectural issue where AFS limit checks operate at user-level
rather than platform-level, creating confusion for customers with both Copilot and ZIM seats.
While Harinath is working with provisioning to build a proper platform-level API, this reveals a
broader pattern where entitlement logic was built for single-product customers and breaks down
as the portfolio converges. The team needs a systematic review of entitlement architecture to
prevent similar issues as more features span multiple products.

Admin work is revealing scope ambiguity across teams, with David Goulden, Tingting's team,
and the GoToMarket Studio group all touching admin-related surfaces without clear domain
ownership. Victor and David agreed to defer zero admin setup until this organizational alignment
happens, but the underlying challenge remains: as Workspace scales, customers will need
robust admin capabilities for user management, territory configuration, and feature entitlements.
The decision to pause is pragmatic, but we need a dedicated owner to drive the admin strategy
forward before GA.

Strategic Insights

Key Learnings & Discoveries

The user survey Adam Severance launched revealed that while 75 respondents feel Workspace
has improved their workflows, they rate chat accuracy and speed as neutral--a concerning
signal for our primary differentiation point. The qualitative feedback frequently references ZI
Chat, confirming we'll always be compared against the bespoke tool regardless of Workspace's
broader capabilities. The insight here is that views-plus-chat only creates differentiation if they
work seamlessly together; mediocre chat performance undermines the entire value proposition
even when views are solid.

Dylan Halladay's exploration of slides artifact implementation uncovered a critical tradeoff:
Google Slides API approach offers better rendering but has limited functionality, while PPTX
approach provides more control but can't render in-app without download. Ryan Stevens and
Lars are pushing to release behind a feature flag this week for internal testing, demonstrating
the value of getting working prototypes in front of users quickly even if not customer-ready. The
lesson is that perfect shouldn't be the enemy of good enough for internal validation.

Ant Cuomo's work on pulses revealed that defining default pulse types requires cross-team
alignment on what constitutes a pulse versus other notification types. The team met with Derek
from the 00 team and identified that pulses need clear definitions, types, and phasing before the
infrastructure work can proceed effectively. This highlights how seemingly simple features
require significant upfront design work to prevent scope creep and misaligned expectations
across engineering teams.

Cross-Team Dependencies

Our work with the agentic platform team on Next Best Actions continues to be essential for
profile quality in the December 3rd release. Ant Cuomo identified that the current agent
evaluation process is too slow--agents must be pushed to production before meaningful testing
can occur on real data. The team needs better guidance on tool selection and context
configuration, as Ant discovered he was pulling engagement data from the wrong source
initially. The agentic platform is powerful but the developer experience for product managers
iterating on prompts and configurations needs improvement to support the pace of
experimentation required.

Adam Severance's views work depends heavily on the GTM data model team's GraphQL
endpoint documentation, which currently has minimal data taxonomy and implementation
guidance. This creates downstream problems where the views team must reverse-engineer how
to properly query for engagement data, account team objects, and other CRM fields. Andres
and the platform team are supportive but stretched thin, suggesting we may need dedicated API
documentation resources to unblock multiple product teams consuming GTM data model
simultaneously.

Looking Ahead

The team is laser-focused on November 3rd release readiness, with Sean Walter's quality
framework providing the checkpoint criteria. Chat accuracy on core AEAM use cases is the
single most important element--if we can't reliably answer basic CRM questions, nothing else
matters. Adam Severance is finalizing golden query examples for the orchestrator agent by end
of day today, enabling Ryan Stevens' team to tune the model before Monday's release of
chat-to-views improvements.

Gabe Pirela kicks off send via Outreach development next week, targeting completion in 1-2
weeks as fast-follow to 11.3. This addresses one of the most frequently requested features from
the sales team and removes a major friction point from V1. Dylan Halladay aims to have slides
artifact ready for internal testing by early November, giving the sales team time to provide
feedback before any customer release. Ant Cuomo is finalizing mobile prototype by tomorrow
and meeting with the chat team to align on dependencies for webview approach.

The strategic priority for the next two weeks is ruthless focus on November 3rd must-haves
while preventing scope creep on nice-to-haves. Sean's quality framework provides the forcing
function to make tough tradeoff decisions. We're building a product that can win in market, but
only if we nail the fundamentals of chat accuracy, view reliability, and first-time user experience.
Everything else is secondary until those foundations are solid.

Source: Team SalesOS/Copilot Operating Framework entries from [Oct. 20, 2025 - Oct. 23,
2025]
