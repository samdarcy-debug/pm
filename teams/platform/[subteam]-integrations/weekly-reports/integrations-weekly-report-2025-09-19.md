---
id: weekly-integrations-2025-38
title: "Integrations Weekly Report - September 19, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-09-19
updated: 2026-01-06
week_ending: 2025-09-19
reporting_period: "September 15-19, 2025"
tags: ["weekly-report", "Q32025"]
---

![ZoomInfo Logo](media/image1.png){width="0.6944444444444444in"
height="0.6944444444444444in"}

# **Integrations Team Executive Roundup**

Week of September 15, 2025

## **Executive Summary**

Prateek Paikray delivered vertical dataset preview functionality for GTM
Studio, now live in staging and ready for backend API integration next
week - in addition, continued intensive Agentforce testing ahead of
Dreamforce to mitigate Salesforce's weekly breaking changes to their
platform APIs.. Meanwhile, Sanyog Rai worked with Agentic/Copilot
Workspace team to get Meeting information directly from GTM DM as the
first consumer in addition to drafting requirements for auto-creating
GTM Accounts from engagements in GTM DM. Andres Perez advanced the CRM
Field Mapping Agent POC to reduce dependence on admin config.

## **This Week\'s Progress**

### **Key Momentum Areas**

Prateek Paikray completed the vertical dataset preview functionality for
the internal marketplace, delivering a working solution using mock data
that\'s now available in the GTMS staging org behind a feature flag.
This achievement sets the stage for the GTM store team to integrate with
backend APIs next week, moving the data marketplace closer to production
readiness.

Sanyog Rai completed the requirements document for account creation
through engagements, with Majed\'s review showing no issues. This
foundational work opens the path for managing engagements from customers
who provide engagement data but haven\'t connected their CRMs, expanding
our platform\'s reach and utility.

The team discovered an unexpected win when Rowan\'s team began using the
GTM data model for Copilot V2 and Workspace chatbot functionality
without any prodding from the Integrations team. This validates the GTM
data architecture and demonstrates organic adoption, with Upcoming
meeting responses in Copilot Workspace now sourced from GTM engagements
using GraphQL queries.

### **Goals & Progress**

**AgentForce Integration**: Prateek continues intensive testing with the
engineering team, addressing functionality issues caused by
Salesforce\'s weekly platform updates. Despite challenges with prompts
that previously worked now giving random responses or invoking wrong
APIs, the team remains on track for Dreamforce readiness with a new beta
package deployed to the demo instance.

**GTM Studio & Solutions for ROI / Advanced Search**: Andres progressed
on the auto-mapping agent POC, working with Lars to access the MCP
server and building direct Salesforce calls to handle page layout
limitations. Monday\'s rollout of Erica's recent releases via a new
feature flag and entitlement will give all GTM Studio customers access
to import rules, custom field creation, and field mapping on CRM
connections, with the new feature flag ready for ROI and Advanced Search
customers who have long-asked for support to swap CRM filter fields.

**Data Platform Enhancement**: The team addressed the GTM Contacts
created from engagements issue, confirming they\'re currently only in
Bigtable and not yet pushed to GTM tables in BigQuery. Maied is working
on timeline clarification while the team continues building on the
foundation that\'s attracting downstream adoption.

### **Strategic Challenges**

Agent Force entitlement checks cannot be performed using the new partner
OAuth flow through the Developer Portal, requiring coordination with
Adam and Vinod to identify a solution before the Dreamforce launch. This
represents a platform-level constraint rather than a team execution
issue, but needs resolution for broader customer access.

Calendar complexity for Outlook integration continues to exceed
expectations, with Sanyog finding the processing more challenging than
anticipated. However, the team has adopted a pragmatic approach: \"Take
what we can and move forward, keep adding as things become available,\"
allowing them to maintain momentum on recordings development using the
stronger email foundation.

Legacy data architecture is creating cost challenges, with tenant data
deletion operations costing \$20,000 per run due to historical raw
sources that store every value change. The raw chorus table alone
contains 3 petabytes of data, suggesting potential savings of
\$5,000-\$10,000 by dropping unused legacy tables as customers migrate
to GTM tables and APIs.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The Copilot Insights API became available on the new OAuth Enterprise
API infrastructure in staging, with production release scheduled for
September 22nd. This creates an integration opportunity with Agent Force
for early October, potentially expanding the solution\'s data access
capabilities just as it reaches broader market availability.

Communication gaps across teams emerged as a pattern, with team
leadership knowledge not always reaching all team members. The discovery
that some data platform team members were unaware of contact creation
from GTM engagements highlights the need for broader information
sharing, while assumptions about integration inclusion in onboarding
launch buttons created unnecessary friction.

The organic adoption of GTM data model by Rowan and Lars\' team
represents validation of the platform architecture and demonstrates that
well-designed systems can drive usage without active promotion. This
first downstream customer success using GraphQL for GTM store access
provides a golden demonstration opportunity for other products.

### **Cross-Team Dependencies**

Our collaboration with the GTM store team on dataset preview
functionality continues to be essential for marketplace completion. With
UI work finished by Prateek, next week\'s focus shifts to backend API
integration once they\'re enabled, requiring close coordination to
ensure seamless functionality transition.

Workbook team coordination remains necessary as they continue using
deprecated GTM fields for core functionality. The team successfully
navigated recent changes through testing with Sunita, confirming that
lookup functionality works correctly with the proper field
implementations while maintaining backward compatibility during the
transition.

## **Looking Ahead**

Next week centers on Agent Force readiness and expanding testing access,
with Prateek creating sandbox users for SC testing while resolving
package issues on the demo org with Salesforce\'s team.

Andres targets completing the end-to-end auto-mapping agent demo,
stringing together the nine required endpoints to showcase reduced GTM
admin overhead. Sanyog advances recordings development by leveraging the
completed email foundation while continuing parallel work on Outlook
calendar integration. The team will also explore the new Context AI
Service APIs, requiring 2-3 weeks to understand responses and integrate
with existing LWC components, positioning for subsequent version
enhancements that could significantly expand agent capabilities.

With Monday\'s GTM Studio release enabling import rules across
Salesforce, HubSpot, and upcoming Dynamics support, the team is
well-positioned to demonstrate compound value across multiple product
lines while maintaining the momentum that\'s already attracting organic
adoption from other teams.

*Source: Team 1-2-3 Operating Framework entries from September 15-19,
2025*
