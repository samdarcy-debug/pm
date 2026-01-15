---
id: weekly-integrations-2025-33
title: "Integrations Weekly Report - August 15, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-08-15
updated: 2026-01-06
week_ending: 2025-08-15
reporting_period: "August 11-15, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Integrations Executive Roundup - Week of August 11, 2025**

## **Executive Summary**

Executive Summary: The team delivered critical infrastructure milestones
this week with Prateek Paikray completing dataset marketplace
requirements handoff to engineering, with a target of the second week of
September to have this feature delivered. Prateek also met with a few
enterprise customers and ISV Partner, Altify, to understand their use
case for integrating agent-to-agent interactions which will help
influence the V2 version of Agentforce. Sanyog was able to onboard 10
email/calendar data integration tenants in production, with the goal of
90% of customers being onboarded next week. Erica Fienman finalized the
CRM connection banner designs and landing page content to address the
2,000+ customers experiencing connector issues, which represents a
significant opportunity to boost Advanced Sync adoption metrics. Andres
Perez finalized and shared the software vendor requirements with the
Partnerfleet team for the market.zoominfo.com revamp. We're now awaiting
their timeline to launch the first generic listing and scale to 10,000
listings, which will drive SEO, improve CX efficiency, and boost partner
and vendor-to-customer revenue attribution.

## **This Week\'s Progress**

### **Key Momentum Areas**

Dataset Marketplace Foundation Complete: Prateek successfully handed off
finalized requirements and designs to the engineering team for the
custom dataset marketplace within Workbook. Engineering has created Jira
user stories and established a delivery timeline targeting the second
week of September, providing a clear path forward for H2 data activation
capabilities.

GTM Data Model Production Milestone: Sanyog achieved email and calendar
data integration in the GTM store for ZoomInfo\'s internal tenant,
marking the first production deployment. The team is now positioned to
gradually expand to 90% of tenants, with ZDP integration scheduled for
completion by end of week.

Strategic Partnership Breakthrough: Andres secured commitment from
Workato that they can update their ZoomInfo integration without
requiring customer migration work. This eliminates a major friction
point for mutual customers and OEM partners like Reltio, significantly
accelerating our partner onboarding capabilities.

### **Goals & Progress**

CRM Connection Recovery Initiative: Erica completed banner system
designs and landing page content to address connector failures affecting
approximately 2,000 customers. The solution includes A/B testing
capabilities to optimize admin notification formats and direct pathways
for issue resolution. Implementation planning with Vignesh is scheduled
for next week, positioning this initiative to significantly impact
Advanced Sync adoption metrics.

Agentforce Enterprise Validation: Prateek engaged with enterprise
customers including Red Hat and ADP who expressed interest in testing
Agentforce integration. The team also met with Altify, a Salesforce ISV
partner and ZoomInfo customer, to understand agent-to-agent interaction
use cases for account and opportunity management planning, informing V2
development priorities.

Custom Fields & Conditional Indexing: Both features are production-ready
with David Wheeler conducting comprehensive testing across all field
types. The internal sales team onboarding is scheduled for Monday,
providing crucial validation before broader customer beta rollout.
Feature flags and entitlements are being finalized to support controlled
release.

## **Strategic Challenges**

Third-Party Integration Testing Infrastructure: Sanyog\'s team
encountered testing issues with calendar integrations that blocked
tenant expansion midweek. The discovery highlighted insufficient testing
infrastructure for third-party integrations not used internally at
ZoomInfo, particularly Outlook. While early detection prevented
larger-scale issues, this gap poses risks to expansion timelines and
requires investment in comprehensive testing capabilities.

Token Refresh Complexity: The CRM connector issues affecting 2,000+
customers stem from fundamental challenges with OAuth token management
when Salesforce admins change passwords or leave organizations. While
the banner system addresses immediate notification needs, the underlying
technical challenge of maintaining persistent connections across
credential changes remains a systemic issue requiring ongoing attention.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Partner Integration Acceleration: The Workato breakthrough demonstrates
that established integration partners can update their ZoomInfo
connections without customer migration work. This discovery
fundamentally changes our partner onboarding strategy, allowing us to
prioritize partnerships with vendors who can seamlessly update
integrations, reducing time-to-market and customer friction.

Enterprise Agentforce Demand Validation: Direct engagement with Red Hat,
ADP, and Altify confirmed strong enterprise interest in AI-powered CRM
integrations. Altify\'s specific use case around agent-to-agent
interactions for account planning provides a clear direction for V2
development, focusing on Copilot API integration and enhanced chat
capabilities.

Internal Sales Team as Beta Validators: The positive reception from
ZoomInfo\'s internal sales team regarding conditional indexing
functionality, particularly their preference over Salesforce\'s
approach, validates our user experience design decisions. This internal
validation provides confidence for broader customer rollout and
demonstrates the competitive advantage of our implementation.

### **Cross-Team Dependencies**

Our work with the Partner Fleet team on marketplace requirements is
critical for Q4 execution. Andres is finalizing the project plan to get
their agreement on revamping market.zoominfo.com with 10,000 generic
listings and dataset integration capabilities. The Marketing team\'s
parallel work on custom dataset enrichment flows requires coordination
with Prateek to avoid duplication of efforts, with alignment meetings
scheduled to clarify the relationship between job posting datasets and
custom dataset pages.

## **Looking Ahead**

Next week focuses on converting completed designs and requirements into
production deployments. Erica will finalize CRM banner implementation
timelines with Vignesh while launching internal sales team beta testing
for conditional indexing and custom fields. Sanyog will expand
email/calendar integration to 90% of tenants, contingent on resolving
the testing infrastructure gaps identified this week.

The Agentforce V2 definition becomes a priority for Prateek,
incorporating Copilot API integration for Account Summary and chat-based
signals based on enterprise customer feedback. Andres will secure
Partner Fleet commitment to the marketplace project plan, establishing
clear timelines for generic listing creation and dataset integration
capabilities. Success metrics include confirmed implementation dates
from Partner Fleet and validated testing infrastructure improvements
from the platform team.

The convergence of these initiatives positions the team to deliver
significant adoption metric improvements in September. With 2,000+
customers potentially recovering from connector issues, expanded GTM
data model coverage, and validated custom field capabilities, the
compound effect should create measurable business impact while
establishing foundation capabilities for Q4 marketplace and Agentforce
expansion.

*Source: Team 1-2-3 Operating Framework entries from August 11-15, 2025*
