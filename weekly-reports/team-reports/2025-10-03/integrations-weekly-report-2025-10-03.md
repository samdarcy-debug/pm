---
id: weekly-integrations-2025-40
title: "Integrations Weekly Report - October 03, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-10-03
updated: 2026-01-06
week_ending: 2025-10-03
reporting_period: "September 29-October 03, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Integrations Executive Roundup - Week of September 29, 2025**

## **Executive Summary**

Prateek completed Agentforce enablement ahead of Dreamforce and
development completion on the in-app Dataset Marketplace UI, scheduled
for staging release on Monday - additionally, delivered a demo for a new
(confidential) Agentforce feature with Salesforce which may be
highlighted in Dreamforce Keynote. Sanyog wrapping up requirements for
GTM Accounts and Account Team Roles created from Engagements, as well as
addressing issue where Chorus only logs meeting participants who speak -
additionally scoped work for importing new engagements and sequence
context from Outreach and Salesloft. Erica's roadmap continues to
execute, with 5,000 tenants importing from CRM every 1 hour into GTM DM,
with the remainder every 3 hours.

## **This Week\'s Progress**

### **Key Momentum Areas**

Prateek Paikray led the completion of all Agentforce training sessions
with solution consultants and account teams in preparation for
Dreamforce. The internal implementation team received dedicated support
sessions, and a new Agentforce support channel was established to handle
technical questions during onboarding. Internal sellers now have access
to release documentation and understand positioning, while Solution
Consultants are prepared to demo the solution.

The GTM Studio Dataset Marketplace achieved development completion this
week. Prateek\'s team successfully integrated the in-app UI with the
Dataset API, with staging release scheduled for Monday. This milestone
unblocks the Data Platform team to begin building the backend API for
data preview functionality, advancing our H2 goals for vertical
datasets.

Strong momentum has emerged around Dreamforce keynote opportunities. The
team is positioning to deliver and showcase a new (confidential)
Agentforce functionality live during the keynotes, with the primary
focus on building and delivering the Salesforce package by October 7th
to enable this showcase of Agentforce capabilities in Slack.

### **Goals & Progress**

**GTM AI Context Service & Vertical Datasets**: Training and enablement
work reached completion with Solution Consultants fully prepared to demo
the new solution. The in-app Dataset Marketplace UI integration is
complete and moves to staging Monday, successfully handing off backend
requirements for data preview functionality to the GTM Store team. This
progression directly supports H2 goals and ensures internal teams can
effectively position the solution at Dreamforce.

**GTM Studio Platform**: Andres Perez secured approval for the GTM
Studio PR in staging, advancing the auto-custom-field creation POC. This
work aims to reduce dependency on GTM Admins for GTM Studio success.
Development continues on creating POC functionality for
auto-custom-field creation from CRM page layouts using the Agentic
Platform.

**GTM Platform - GTM Accounts and Account Team Role from Engagements**:
Sanyog Rai completed requirements for Account and Account Team Role
creation, which will enable linking users to accounts based on
engagement data. Requirements are now documented and ready for
engineering review. The team also identified that while Chorus provides
recording participants, it omits those with non-speaking roles. New work
is planned to solve this for API recording imports as another lever to
move customers from bot recording.

### **Strategic Challenges**

Enterprise customers including Intuit and IBM are requesting MCP
integration with ZoomInfo, seeking flexibility to adopt either
Agentforce or their own agentic solutions. This represents significant
market demand but requires architectural decisions about how we support
multiple integration pathways while maintaining our strategic focus on
Agentforce.

The current Agentforce enrichment flow needs acceleration to close gaps
before Q4. Prateek identified that the enrichment flow was built outside
the platform export service and doesn\'t align with the new ZI API
infrastructure. Bringing the Context AI service into Agentforce and
adding visibility into credit charging based on agent actions will
reduce support questions around credit consumption and help sellers
better position Agentforce against the existing iframe solution.
Collaboration with Jessie Lindstrom\'s provisioning team is needed to
redesign the Agentforce SKU from tenant-level to user-seat-level to
ensure accurate usage tracking and prevent future abuse.

GTM DM testing continues revealing poorly documented pipeline behavior
in our Engagement ETL process, as evidenced first by Outlook integration
omitting future meetings and now by non-speaking participants dropped.
Fixing these behaviors to achieve the desired GTM DM end state is the
driver for delays in engagement roadmap delivery.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Enterprise demand for MCP integration signals that customers want
flexibility in their agentic solution architecture. Rather than being
locked into a single vendor\'s agent framework, sophisticated customers
like Intuit and IBM are asking for protocol-level integration that
allows them to choose their own agentic solutions while still leveraging
ZoomInfo data. This challenges the assumption that all enterprise
customers will adopt our Agentforce implementation and suggests we may
need a multi-pathway integration strategy.

The Agentforce SKU structure needs fundamental redesign to prevent abuse
and ensure accurate tracking. The current tenant-level approach doesn\'t
provide the granularity needed for proper usage attribution and credit
consumption visibility. Moving to user-seat-level SKUs will require
close collaboration with provisioning but will eliminate a future source
of customer confusion and support escalations.

Federated search's privacy rule behavior reveals the importance of the
GTM DM query respecting a decade of improvements, while also raising the
need to replicate some of these rules in GTM Config for non-ZI ID GTM
Accounts and Contacts.

### **Cross-Team Dependencies**

Collaboration with Jessie Lindstrom\'s provisioning team is essential
for redesigning the Agentforce SKU from tenant-level to user-seat-level.
This architectural change is necessary to ensure accurate usage tracking
and prevent future abuse as Agentforce scales. The timing is important
as we want this foundation in place before widespread customer adoption
creates migration challenges.

The Data Platform team is now unblocked to build the vertical dataset
backend API for data preview functionality following the UI integration
handoff. This cross-team workflow demonstrates successful coordination
between Prateek\'s integrations work and the GTM Store team\'s platform
capabilities.

## **Looking Ahead**

Primary focus shifts to delivering the Salesforce package by October 7th
to enable the Dreamforce demo. This represents a significant visibility
opportunity for the team\'s work and requires intense coordination with
the Salesforce team.

Sanyog will work with engineering to review the completed Account Team
Role requirements, moving the capability toward implementation. The team
has clear understanding of the engagement data limitations from Chorus
and can design around those constraints. Meanwhile, the backend work for
Dataset Marketplace data preview functionality begins with the GTM Store
team now that Prateek\'s UI integration is complete and moving to
staging.\
\
Andres will drive follow-up coordination from the roadmap onsite,
particularly around deprecation strategy for legacy products. These
conversations will shape how we minimize churn risk related work on
legacy products to help us move faster on GTM Studio, Workspace, and GTM
Context. Additionally, will pick the field mapping agent back up.

*Source: Team 1-2-3 Operating Framework entries from week of September
29, 2025*
