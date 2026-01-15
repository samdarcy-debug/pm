---
id: weekly-gtm-studio-2025-40
title: "GTM Studio Weekly Report - October 03, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-10-03
updated: 2026-01-06
week_ending: 2025-10-03
reporting_period: "September 29-October 03, 2025"
tags: ["weekly-report", "Q42025"]
---

GTM Studio Executive Roundup -
September 29 - October 3, 2025

Executive Summary

The team made critical progress toward GTM Studio's soft launch while managing necessary
scope adjustments post-Dreamforce. Brahm consolidated roadmaps across ROI, Data
Management, and GTM Config, establishing clear execution paths. The Data Health Scan
prototype generated strong validation from account managers, with clear potential for new
RingLead revenue. However, job posting operators required last-minute architecture changes
that delayed the September 30th target, now launching October 1st behind a feature flag for
controlled rollout.

This Week's Progress

Key Momentum Areas

Arun delivered working prototypes for both Workbooks and Workspace ROI analytics, providing
the foundation for demonstrating platform value to customers. The GTM Data Model migration
reached 90%+ tenant coverage with under 10% variance in closed-won opportunity data,
removing a critical GA blocker. Brahm coordinated successful ROI conversations with enterprise
accounts, with Indeed moving from $1M ACV to $5M TCV multi-year deal based directly on ROI
insights.

Corina expanded the Data Health Scan from 600 to 3,700 customers and activated the first
account managers to use it in RingLead upsell conversations. Early feedback confirms AMs can
identify meaningful data quality issues that create natural expansion opportunities. The team
also completed Enrich Premium Plus requirements for HubSpot and Microsoft Dynamics,
positioning M2 for delivery in October and November.

Jagannath's team delivered semantic enrichment to production and completed AI Emailer
integration, with both capabilities validated in customer conversations. The shift from semantic
search endpoints to the Data Model approach, following Adam Smith's recommendation,
provides a faster path to production-quality results. However, deep research enrichment
remains slow and requires optimization before broader rollout.

Goals & Progress
ROI Analytics (M3): The team finalized metrics and insights for both Workbooks and
Workspace ROI, with Arun building a working prototype that demonstrates the full customer
journey. The ROI Assistant launched to production but encountered entitlement bugs affecting
non-Copilot customers, which the team resolved with Lars and the platform team. Multi-currency
support requirements are defined, with the team exploring a CFA-owned conversion service
since platform support has lower priority.

Data Management (M1-M3): Milestone 1 achieved strong validation with account managers
using the Data Health Scan PDF to identify upsell opportunities with customers who have CRM
synced but no RingLead. Corina is working with specific AMs on high-value accounts like Palo
Alto Networks rather than batch-processing all 3,700 customers. Milestone 2 engineering work
is underway for RingLead expansion features, targeting October/November releases with
enablement documentation complete. Milestone 3 requirements are drafted for building the Data
Health Scan directly into GTM Studio.

AI Audience Building: Internal testing with 15 users revealed that enrichment capabilities via
the agent work well, but the overall audience building flow needs UX improvements before
broader rollout. The team is implementing better CRM query handling and backup options when
the Data Model returns poor responses. Semantic enrichment is functional end-to-end but faces
scalability constraints that prevent large workbook processing. Grant, the developer previously
working on semantic, is returning to the project which should help resolve these limitations.

GTM Config: M1 and M2 engineering work remains on track, with zero-config data targeted for
next week to enable quality validation. Tingting completed value messaging copy for the agent
and created a research plan for phase 1 customer validation sessions scheduled with internal
teams (OM/TIM) for the week of October 13th. The team is working with Tomer to break down
development work into Jira epics following the holidays, establishing a clear execution path for
the config agent prototype.

Strategic Challenges

Job posting launched to production behind a feature flag on October 1st rather than September
30th due to operator logic inconsistencies. Corina, Tanvi, and Ash discovered that each feature
area (signals, CRM, job posting) had slightly different operator implementations causing bugs.
The team made the decision to rebuild all operator logic from scratch with consistent handling
across data types, which Alex and the engineering team estimate will complete by mid-October.
The short-term workaround removes unsupported operators, allowing internal demos while
preventing the migration headaches that would come from releasing inconsistent logic to
customers.

GTM Config must balance the ambitious January timeline with the actual scope required for
meaningful customer impact. The original plan to ship by January has too many integration
dependencies that require engineering estimates. Tingting is working to rescope the work for an
initial prototype, allowing for customer learning and improvements rather than a single large
release.
The Dreamforce demo tenant is ready with data prepared, but the team faces a gap in
demonstrating conversation intelligence use cases without access to real conversation data.
Jagannath is exploring whether to create a synthetic data agent that generates realistic-looking
responses for demo purposes. This highlights a broader challenge in preparing compelling
demos when certain data types aren't available in test environments.

Strategic Insights

Key Learnings & Discoveries

The onsite meetings provided crucial validation that the product phasing makes sense, but
revealed the team needs to shift from feature development mindset to defining clear sales
motions for each release. For both AI Audience Building and Data Management, the "what we're
releasing when" needs much more specificity around customer segments, demo environments,
and go-to-market plays. The feedback emphasized moving from milestone completion to
release readiness.

Henry's suggestion to bring ROI conversations forward into the onboarding process rather than
waiting for renewal discussions could significantly improve CRM connection and data sharing
enablement rates. The team is partnering with the onboarding team to build value narratives
around ROI, GTM Config, and Data Health Scan that make integration setup feel essential from
day one rather than an afterthought.

The Data Health Scan work is revealing an opportunity to embed the motion into a
product-driven play. Rather than manually running scans and coordinating with AMs, the team
should work toward automatically identifying high-value opportunities where health scans show
meaningful issues, then proactively triggering outreach. This would scale the motion beyond
what manual coordination allows while validating the play execution framework.

Cross-Team Dependencies

Mohan is coordinating Copilot activation development across four engineering teams
(workbook, route, copilot, emailer), targeting October 20th as the earliest production date. The
workspace emailer experience for multi-template use cases remains undefined and needs
Adam, Gabe, and Sean's alignment. Additionally, the team discovered that GTM Studio uses
Angular while DoubleO uses React, requiring a decision on frontend approach for
customer-facing milestones beyond M1.

Platform team dependencies continue to impact multiple workstreams. The GraphQL
proof-of-concept from Sean's team is needed to unblock the workbook shared view approach for
Copilot. GTM Data Model API availability is critical for engagement data (emails/meetings/calls),
with Linda coordinating timeline. The Query API for partner data won't be ready until end of
October, affecting the broader platform approach for job posting and other datasets beyond the
September M8 scope.
Looking Ahead

Next week, the team focuses on closing out the September release items while maintaining
momentum on October priorities. Critical paths include completing job posting QA once
operators are updated, expanding Data Health Scan enablement with more AMs, and finalizing
AI Data Management M4/M5 requirements through daily working sessions with engineering.

The consolidated roadmap work positions the team well for 2026 planning discussions. With
clear phases defined across Audiences, Plays, and Data Management, the focus shifts to
specific release definitions, customer segments, and sales motions for each milestone. Brahm
will work with Arun on GA readiness materials for ROI, and continue Data Health Scan narrative
refinement with Corina.

GTM Config moves into validation mode, with zero-config data evaluation happening next week
and customer feedback sessions beginning October 13th with internal OM/TIM teams. Tingting
will work with Tomer to finalize Jira epic breakdowns and continue refining design prototypes
based on early feedback. The team remains focused on demonstrating a working proof of
concept within four weeks rather than overcommitting to the January timeline, allowing for rapid
iteration and course correction based on real customer validation.

The team returns from the successful onsite with strong alignment on direction and clear next
steps. The shift from feature development to release planning, combined with embedding value
narratives earlier in the customer journey, sets up the soft launch for success. The next six
weeks through mid-October will determine whether the team can deliver on the promise of
integrated GTM capabilities that differentiate in the market against Clay, Common Room, and
UnifyGTM.

Source: GTM Studio Operating Framework entries from September 29 - October 3, 2025
