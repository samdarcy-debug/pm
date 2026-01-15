---
id: weekly-copilot-2025-36
title: "GTM Workspace (Copilot) Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

SalesOS/Copilot Executive Roundup -
[September 2nd - September 4th, 2025]

Executive Summary

Critical path decisions needed immediately: Our Multi-AFS enterprise feature validation is
complete and ready for coordinated rollout with Advanced Search, while Intent Topic AI
Recommendation automation achieved 75% completion with production deployment scheduled
for customer-facing demos next week.

This Week's Progress

Key Momentum Areas

Harinath Krishnamoorthy successfully completed comprehensive Launch Release Tracking
(LRT) documentation for September's three-feature release, including HubSpot CRM integration
for Prioritize Package that addresses 45+ customer requests, plus Account Fit Score date
filtering and smart retry mechanisms. The systematic approach reduced typical release
preparation time while ensuring all stakeholder materials (PRFAQ, Video Loop, guides) are
production-ready.

Adam Severance advanced GTM Copilot first-time user experience to 80% completion, with
Vignesh from Team 50 investigating multiple technical implementation paths for homepage
artifacts. The team resolved core architectural decisions around artifact generation and
identified API requirements for seamless Salesforce opportunity integration, positioning us for
immediate September delivery pending executive direction.

Ant Cuomo achieved breakthrough results with Next Best Action agent testing, where Dell
account rep Jason Sherman rated ZI Chat outputs A- for immediate executability and the new
agentic platform agent reached near-parity performance after iterative prompt engineering. This
validates our enterprise-grade intelligence capabilities and establishes the foundation for scaled
internal beta testing with account managers.

Goals & Progress

Multi-AFS Enterprise Capabilities: Harinath completed validation testing across ZIM Audience
creation with engineering teams, confirming data consistency within 95% accuracy thresholds
and coordinating synchronized deployment with Adam's Advanced Search filter implementation.
This unlocks enterprise customers' ability to target multiple product lines with distinct ICP
definitions, addressing long-standing mid-market and enterprise segmentation requirements.

Intent Topic Migration & Automation: Phase 3 Intent Topic AI Recommendation development
reached 75% completion with comprehensive PRD finalization and AI prototype design work
completed with Sivaramasubbu M. The automated keyword-to-topic migration system will
eliminate manual onboarding friction while enabling seamless transition from legacy intent
targeting to ZoomInfo's Topic-based approach, reducing customer time-to-value from weeks to
days.

GTMC Profiles & Next Best Actions: Ant Cuomo progressed profile designs to 80% with focus
on UX simplification over UI complexity, making signals, intent, and websites accessible to new
users through intelligent summaries and educational context. Mobile V2 framework achieved
consensus as new GTMC-powered app with authentication and backend integration planned,
while the mobile team secured sprint capacity for foundational development starting next week.

Strategic Challenges

Admin Defined Territories faces workflow ownership complications where inactive trial users or
admin-only license holders break the automated territory activation system, causing end users
to receive incomplete whitespace recommendation results. David Goulden identified that
territory routing is critical for Workbooks V2 activation, requiring resolution of user management
dependencies with workflow teams before GA release can proceed. The challenge reveals
broader system architecture gaps in handling license transitions and user role changes.

Priority Accounts migration to GTM Data Model encounters coordination bottlenecks as search
engineering teams expect search PMs to define integration specifications, but key personnel
(Mena) remain unavailable for two weeks while Adam Severance ramps up on unfamiliar
territory. David Goulden's testing of new GraphQL tooling yielded limited success, highlighting
the need for clearer technical ownership and timeline alignment between search and platform
teams.

Advanced Search vision development requires immediate prioritization trade-offs as Adam
Severance shifts focus from onboarding product review to advanced search architecture,
recognizing that 40K SalesOS users won't migrate to GTMC without solving core search use
cases. This strategic pivot demands executive alignment on resource allocation and timeline
expectations for both near-term migration needs and long-term search experience evolution.

Strategic Insights

Key Learnings & Discoveries

Production quality analysis of Intent Topic AI recommendations revealed critical gaps in QA
processes, with multiple bugs (ML-4258, ML-4257, ZOO-159382) reaching customer
environments undetected, including unauthorized platform runs and incorrect scheduling
frequencies. Harinath's customer-first investigation approach using real enterprise account data
(Brex, Monday.com, Twilio, Freshworks) proved more effective than traditional testing,
suggesting we need systematic customer data validation integrated into development
workflows.

Cross-functional architecture discussions exposed the tension between agile development
speed and enterprise complexity, particularly in territory management and CRM integration
patterns. David Goulden's conversations with Ringlead teams revealed that even specialists in
Salesforce integration avoid automated territory imports due to data model complexity and
customer maintenance challenges, indicating our manual configuration approach may be
strategically sound despite customer requests for automation.

AI agent development maturity reached practical deployment readiness, with Ant Cuomo's
systematic comparison between ZI Chat and agentic platform outputs demonstrating
measurable quality parity for enterprise accounts. The Dell validation session with Jason
Sherman proved that prompt engineering iteration can achieve A- grade results, establishing
our capability to deliver actionable intelligence at scale while identifying specific improvement
areas (contact accuracy, NBA relevance).

Cross-Team Dependencies

Our coordination with Advanced Search team on Multi-AFS deployment continues progressing
through Adam's integration work, though synchronized rollout scheduling requires additional
refinement between ZIM and Advanced Search components. The dependency highlights our
growing capability to deliver unified cross-platform experiences while managing technical
complexity through careful staging and validation approaches.

Territory routing integration with Workbooks activation presents both opportunity and complexity,
as Veronica's broader forum discussions this week aimed to resolve ownership gaps that have
persisted across multiple teams. The coordination challenge reflects the natural evolution
toward more sophisticated workflow automation, requiring clear decision-making frameworks
and technical ownership models to support enterprise customer needs.

Looking Ahead

Next week focuses on executing immediate decisions while advancing strategic initiatives that
position us for Q4 momentum, particularly around GTM Copilot launch readiness and Multi-AFS
enterprise rollout.

Critical path items demand immediate resolution: Adam's GTM Copilot homepage strategy
requires executive approval today to maintain September timeline integrity, while Harinath
prepares customer-facing demo environments for sales team enablement on September
releases. Ant's NBA agent expansion to broader AM testing groups and David's territory routing
solution documentation will establish foundation for October workbook activation capabilities.
The week's success depends on resolving current architectural decisions quickly while
maintaining quality standards across all customer-facing deliverables.

Long-term strategic positioning advances through Adam's advanced search vision development,
with design brainstorms scheduled to synthesize extensive UXR insights into actionable
migration pathways for 40K SalesOS users. Our growing confidence in AI agent capabilities,
validated through real customer feedback and measurable quality improvements, supports
aggressive expansion of intelligent automation across the platform while ensuring
enterprise-grade reliability and accuracy.

Source: Team SalesOS/Copilot Operating Framework entries from [September 2nd - September
4th, 2025]
