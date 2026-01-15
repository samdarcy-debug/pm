---
id: weekly-gtm-studio-2025-31
title: "GTM Studio Weekly Report - August 01, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-08-01
updated: 2026-01-06
week_ending: 2025-08-01
reporting_period: "July 28-August 01, 2025"
tags: ["weekly-report", "Q32025"]
---

# **GTM Studio Roundup - 07/28/2025**

## **Executive Summary**

**GTM Studio September GA is locked and loaded.** Engineering milestones
are finalized and committed, with key foundational pieces like Plays
architecture alignment, signal-based workbooks design completion, and AI
audience building capabilities all converging toward our September
launch. The cross-functional coordination between Platform (Workflows)
and GTM Studio (Play wrapper objects) has been resolved, creating a
clear path forward for execution. Early Access customers like Brex are
providing strong validation signals, while ROI Analytics moves toward GA
readiness with 8-10 customer-driven enhancements identified.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Plays Architecture Progress**: Veronica, Carlos Nunez, Ali Sadat, Marc
Frail, Noam, and Imesh achieved critical alignment on Tuesday, getting
closer to resolving the platform vs app definition confusion that had
been creating friction. Platform will fully own Workflows execution,
while GTM Studio owns the wrapper object connecting Workflows to
Workbooks, reporting, and state management. Getting closer to
architectural clarity removes a major blocker and enables parallel
development streams.

**Signal-Based Workbooks Foundation Complete**: Tanvi Vaidya delivered
100% completion on establishing design and requirements framework, with
Figma designs ready for Monday engineering review. Internal feedback
revealed users need aggregated views from initial release rather than
raw data alone, fundamentally shaping our approach to data presentation
strategy and ensuring higher user adoption from launch.

**Customer Validation Accelerating**: Jagannath Ramesh reports Brex
providing positive feedback on Workbooks core use cases, with growing
demand for additional team training highlighting the product\'s value
expansion potential. The AI audience building capabilities now support
enrichment across ZI fields and CRM data within artifacts, demonstrating
meaningful progress toward GA readiness.

### **Goals & Progress**

**Plays Development**: Architecture alignment achieved with 80% goal
completion by Veronica Hudson. PRD refinement continues with Carlos
Nunez on engineering proposal/scoping, while Neha Pareek reached 90%
completion on triggers/actions mapping, creating prioritized P1 events
list and cross-team coordination structure with Workflows, Scoring, and
Agentic teams.

**ROI Analytics GA Preparation**: Brahm Kohli identified 8-10
customer-driven enhancements critical for GA readiness, though progress
sits at 50% due to HubSpot opportunity data health issues requiring
Platform/Integrations support. Arun V advanced edge case handling with
15+ scenarios addressed, while ROI Analytics BETA program summary awaits
final review with Dominik and James Roth.

**AI Data Management Strategy**: Ash Lauricella achieved 85% completion
incorporating stakeholder feedback from Brandon Tucker, Anne Fajkus,
Vinny Parisi, and Coleman into prototype iterations. Usage definitions
aligned with analytics engineering team, with steel thread narratives
resonating strongly with internal stakeholders despite needing clearer
definition of AI magic vs user control balance.

### **Strategic Challenges**

**Navigation Release Delayed to September**: The comprehensive new
navigation rollout for SalesOS, Marketing, and Copilot customers
requires more extensive enablement preparation than initially scoped.
Neha Pareek reports the Enablement team needs additional time for
cross-functional coordination affecting all customer segments,
highlighting our tendency to underestimate multi-product impact scope.

**Integration Dependencies Creating Bottlenecks**: Multiple workstreams
face integration complexity. Mohan Sun discovered Hasura GraphQL layer
issues pushing Partner Data query API to end of October, while HubSpot
opportunity data health problems block ROI Analytics progress for
affected customers. These technical dependencies require more
Platform/Integrations engineering support than currently allocated.

**Resource Allocation Across Expanding Scope**: With GTM Studio GA
approaching, team members are juggling multiple high-priority
initiatives. Brahm Kohli needs clearer PM capacity allocation for GTM
Data Management, while Tanvi Vaidya deferred bug backlog cleanup to
focus on core GA deliverables, indicating potential technical debt
accumulation as we prioritize launch readiness.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Platform Integration Complexity Underestimated**: Our Partner Data
initiative revealed significant architectural challenges with Hasura not
functioning as expected for GraphQL layer support. Corina Soto\'s team
learned this is expected for first-time platform builds across ZDP,
APIs, and Query Builder, but standardizing the approach will enable
scaling for all future partner data integrations.

**User Experience Expectations Higher Than Anticipated**: Tanvi
Vaidya\'s signal-based workbooks research showed users need aggregated
views immediately rather than accepting raw data presentation. This
insight challenges our assumption about progressive capability release
and suggests users expect sophisticated data manipulation from day one,
influencing our entire data presentation strategy.

**Customer Success Driving Feature Expansion**: Jagannath Ramesh
observed Brex and other Early Access customers requesting additional
team training, indicating Workbooks\' value extends beyond individual
users to team-wide adoption patterns. This suggests our go-to-market
approach should emphasize organizational capability building rather than
individual user onboarding.

### **Cross-Team Dependencies**

Our coordination with Platform team on Workflows execution continues to
be critical for Plays success. Marc Frail\'s team owns the underlying
workflow engine while we manage the business logic layer, requiring
ongoing technical alignment on triggers, actions, and data flow. The
Tuesday architecture meeting resolved ownership questions, but
implementation details need continued collaboration.

Integration engineering support has become a bottleneck across multiple
initiatives. Both ROI Analytics (HubSpot data health) and Partner Data
(query API delays) require more Platform team bandwidth than currently
available, potentially impacting our September GA timeline if not
addressed through resource reallocation or priority adjustment.

## **Looking Ahead**

**September GA execution is our singular focus**, with engineering
milestones committed and clear delivery paths established across all
major workstreams.

**Top priorities center on execution quality over feature expansion**.
Veronica will finalize the Plays PRD (with a review being scheduled for
the week of 8/11) and architecture proposal with Carlos Nunez, while
Tanvi moves signal-based workbooks through design review and engineering
validation. Brahm needs immediate Platform support resolution for ROI
Analytics blockers, and Ash will complete AI Data Management prototype
validation with recorded demos and business case prioritization. Each
workstream has clear next steps and identified collaborators, with the
biggest risk being integration engineering bandwidth constraints that
require leadership attention for resource allocation adjustments.

**The convergence of customer validation, technical foundation
completion, and cross-team alignment positions us strongly for September
delivery**, assuming we can resolve Platform dependencies and maintain
execution discipline across all parallel development streams.

*Source: GTM Studio Team Operating Framework entries from 7/28/2025*
