---
id: weekly-integrations-2025-30
title: "Integrations Weekly Report - July 25, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-07-25
updated: 2026-01-06
week_ending: 2025-07-25
reporting_period: "July 21-25, 2025"
tags: ["weekly-report", "Q32025"]
---

Integrations Executive Roundup

Week of July 21, 2025

  Bottom Line: Andres Perez successfully launched API access for Copilot
  customers, enabling Salesloft and Outreach integrations that will drive upgrades
  and consumption across our 28,000 non-Copilot sales customers. Prateek
  Paikray's Salesforce AgentForce package is 85% complete despite authentication
  storage challenges, with the team targeting Tuesday delivery for our October
  Dreamforce showcase. This positions us to demonstrate real-time data activation
  capabilities to enterprise customers while creating a scalable model for future
  partner integrations.

 This Week's Progress

Key Momentum Areas

Andres Perez delivered the complete API for Copilot launch, shipping the press release and
enabling our internal sales team with targeted customer lists for Salesloft and Outreach
beta programs. This marks the first time our sales team received actionable account lists
rather than starting from zero, with Marcella Wong noting this as a significant improvement
in our go-to-market execution. The launch establishes our new partner integration model
where API access drives Copilot upgrades and increased consumption.
Sanyog Rai achieved 90% completion on getting engagement data into the GTM Data
Model, successfully pushing email and calendar data through the infrastructure pipeline.
Despite some testing issues discovered on stage, the team is working through final bugs
with engagement data expected in production between midweek and end of next week.
This foundational work enables the flow of provider ingestion data directly into our GTM
system.
The team demonstrated strong cross-functional collaboration, with Andres leveraging
Crossbeam data to identify mutual customers and provide sales teams with pre-qualified
prospect lists including Copilot status and enterprise indicators. This data-driven approach
to partner enablement shows how our integration capabilities can enhance internal sales
effectiveness beyond just customer-facing features.

Goals & Progress

 Salesforce AgentForce Integration: Prateek Paikray's team reached 85%
 completion on the managed package development, overcoming initial access issues
 that caused delays. The primary remaining challenge involves Salesforce's text field
 limitations for storing encrypted access tokens, which the team resolved by
 implementing a 15-field splitting solution recommended by Salesforce. While not ideal,
 this approach will enable security review passage and package submission by the
 August 15th deadline.

 Custom Field Infrastructure: Erica Fienman achieved 70% completion on custom
 field support, with testing revealing several bugs currently being addressed. The LRT
 information packet is due Tuesday, positioning this capability to unlock major blockers
 for early access customers who need to extend our GTM schema with their own
 custom fields surfaced in Workbooks.

 Partner API Ecosystem: The Copilot API launch creates a template for future partner
 integrations, with Zapier as the next priority to migrate to OAuth endpoints before
 customer complaints arise from increased awareness. This systematic approach to
 partner enablement will scale our integration capabilities while maintaining proper
 authentication and usage tracking.

Strategic Challenges

 Salesforce's authentication storage limitations forced an inelegant workaround where
 access tokens must be split across 15 separate fields before encryption and storage.
 While Salesforce indicated they have a bug on their end for the preferred OAuth flow,
 they haven't prioritized a fix, leaving Prateek's team to implement this temporary
 solution. The team plans to build proper service account user logic in v1 to eliminate
 per-user authentication requirements, but this adds complexity to the current timeline.
 The new API access model creates potential seat compression risks as partners like
 FreshWorks rebuild ZoomInfo UI functionality within their platforms, allowing multiple
 users to access data through a single integration. While this drives usage and puts
 pressure on our credit pricing model, it requires careful monitoring to ensure we're
 capturing appropriate value from enterprise customers who might circumvent
 individual seat purchases.

 Strategic Insights

Key Learnings & Discoveries

 Andres discovered that "Active Packages with ACV" provides the most accurate field
 for determining Copilot customers, enabling precise targeting for upgrade campaigns.
 This insight came from working with Crossbeam data and cross-referencing customer
 status, providing a reliable foundation for future partner enablement and sales
 targeting efforts.

 The team learned that providing pre-qualified prospect lists significantly improves
 sales team effectiveness, with this being the first time such targeted enablement was
 provided according to Marcella Wong. This approach of combining integration
 capabilities with sales intelligence creates compound value beyond just technical
 functionality.

 Sanyog's work revealed the importance of building buffer time into testing estimates,
 as engagement data integration uncovered unexpected issues during stage testing.
 This learning will inform future sprint planning and help set more realistic expectations
 for complex data pipeline work.

Cross-Team Dependencies

Our work with the Data Team on engagement table schema design continues to be critical
for GTM Data Model success. Sanyog coordinated with the team to review engagement
tables and address developer experience concerns around table joins and indexing,
ensuring the schema supports both contact-to-engagement and engagement-to-contact
query patterns that partners will need.
Collaboration with Lars on agent platform APIs remains essential for the AgentForce v1
version, where managed actions will point to new agentic platform endpoints rather than
current API-based implementations. This dependency will become critical as we move from
the current authentication-focused v0 to the full-featured v1 experience.

 Looking Ahead

Next week focuses on completing foundational deliverables while preparing for Q3 sprint
planning and H2 epic refinement.
Prateek will finalize the AgentForce package by Tuesday and begin grooming epics for ZI-
managed and custom-managed actions across Salesforce, HubSpot, and Dynamics.
Andres prioritizes migrating Zapier to OAuth endpoints before customer complaints arise
from the API announcement, while Erica completes custom field testing and the LRT
information packet. Sanyog targets engagement data production deployment between
midweek and week-end, establishing the foundation for provider data flow into GTM
systems. These deliverables position the team to demonstrate significant enterprise value
at Dreamforce while scaling our partner integration model across the ecosystem.
The team maintains strong momentum on strategic initiatives that directly impact revenue
growth through Copilot upgrades, enterprise customer retention through custom field
flexibility, and ecosystem expansion through standardized partner integration patterns.

      Source: Team 1-2-3 Operating Framework entries from July 21-25, 2025
