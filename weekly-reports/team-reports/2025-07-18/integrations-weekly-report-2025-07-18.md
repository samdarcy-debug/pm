---
id: weekly-integrations-2025-29
title: "Integrations Weekly Report - July 18, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-07-18
updated: 2026-01-06
week_ending: 2025-07-18
reporting_period: "July 14-18, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Integrations Team Executive Roundup**

Week of July 14, 2025

## **Executive Summary**

The Integrations team delivered exceptional progress across three
critical infrastructure initiatives this week. Sanyog Rai achieved a
major breakthrough in engagement table infrastructure, working through
final roadblocks ahead of processing email and calendar data with
participant and contact creation linked to CRM tables for
ZI-as-a-customer next week - though cross-timezone Engineering issues
(Israel and West Coast) contributed to the roadblocks not resolving
sooner. Erica Fienman architected the on-demand refresh solution with
Global Event Bus integration, positioning us to deliver real-time CRM
import to support Saleshub/Copilot V2. Prateek Paikray overcame
significant Salesforce authentication challenges and connected to the
new agentic platform from the Agentforce SFDC package.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Engagement Infrastructure Breakthrough:** Sanyog Rai made exceptional
progress finalizing the GTM Data Model engagement tables, identifying
and addressing the last roadblocks to enabling email and calendar data
flow from provider ingestion to GTM DM.

**On-Demand Refresh Architecture Excellence:** Erica Fienman delivered
outstanding work scoping the on-demand refresh capability, meeting with
Asaf\'s team and identifying Global Event Bus as the optimal trigger
mechanism. Her architectural approach enables real-time CRM data
synchronization within one minute of ZoomInfo exports, directly
supporting Sales Hub use cases while continuing to use GTM Data Model as
source of truth for 1st party data.

**Salesforce Integration Innovation:** Prateek Paikray demonstrated
exceptional problem-solving by navigating complex Salesforce
authentication roadblocks and package setup challenges. His successful
connection to the new agentic platform and exploration of MCP server
development for integration services positions us ahead of schedule for
building agents and custom actions, while establishing a clear v1 path
using individual user authentication.

### **Goals & Progress**

GTM Data Model Infrastructure: Sanyog Rai achieved 80% completion on
engagement table infrastructure, with the core functionality of
processing engagements and creating participants/contacts linked to CRM
tables now operational. His identification of testing infrastructure
improvements as a critical Q3 need demonstrates strategic thinking, with
plans to create specific epics for more robust testing environments.

On-Demand Refresh Solution: Erica Fienman reached 80% completion on
scoping the on-demand ingestion capability, successfully architecting
the Global Event Bus integration approach and creating detailed
documentation for team implementation. Her coordination with multiple
teams and clear path forward for POC development with export customers
shows exceptional project leadership.

Data Catalog Admin Portal: Prateek Paikray achieved 70% completion on
unified admin portal designs despite resource constraints, successfully
engaging Marina for mockup development and scheduling critical meetings
with Dow Jones to understand data registry processes. His multi-threaded
approach balancing Salesforce integration work with data catalog
advancement demonstrates excellent prioritization.

Managed Data Connectors: Andres Perez completed the SimilarWeb POC,
enabling immediate deployment to GTM Studio beta customers via feature
flag and establishing the foundation for managed data connector
capabilities that eliminate customer configuration overhead.

### **Strategic Challenges**

**Cross-Timezone Coordination Crisis:** Sanyog Rai identified a critical
bottleneck where time zone coordination between West Coast and Israel
teams is causing 4+ day delays on issues that should resolve in hours.
The domain field resolution issue exemplifies how 1-2 hours of daily
business overlap creates cascading delays across infrastructure work,
requiring executive attention to establish better asynchronous
collaboration processes.

**Testing Infrastructure Limitations:** Sanyog Rai discovered critical
weaknesses in testing infrastructure during engagement table validation,
including missing data in testing environments and SIP issues with
specific tenants. His strategic recommendation for Q3 testing
infrastructure improvements demonstrates forward-thinking approach to
preventing future blockers.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Prioritized Queue Architecture Innovation:** Erica Fienman discovered
that the on-demand refresh solution can leverage prioritized queue
concepts to support multiple use cases beyond Sales Hub, including
import mapping changes and conditional indexing. Her insight that
regular exports can validate the approach before Global Event Bus
integration shows exceptional technical judgment and risk mitigation
thinking.

**Salesforce Authentication Evolution Strategy:** Prateek Paikray
learned that Salesforce\'s security requirements are delaying service
account flows, leading him to architect a phased approach with
individual user authentication for v1 and service accounts for future
iterations. His connection to the agentic platform and MCP server
exploration positions us ahead of the framework development timeline.

**Infrastructure Dependency Mapping:** Sanyog Rai identified that
engagement table deployment depends on CDC processes from GTM Store to
ZDP tables, revealing the importance of maintaining single-source data
flow to prevent discrepancies. His insistence on proper architecture
over quick workarounds demonstrates strong technical leadership and
long-term thinking.

### **Cross-Team Dependencies**

Our work with the Global Event Bus team remains critical for Erica
Fienman\'s on-demand refresh capabilities, with timing coordination
essential as their availability extends to end of August. Erica\'s
upcoming meeting with Sean from Sales Hub will evaluate existing
solutions against our Global Event Bus approach to ensure optimal
architecture selection.

Sanyog Rai\'s coordination with Dor\'s team in Israel continues to be
essential for engagement table deployment, while his work with Maxim to
clarify ownership transitions ensures proper communication channels with
Asaf\'s Team 6. Prateek Paikray\'s collaboration with the data platform
team on registry processes will be crucial for data catalog success.

## **Looking Ahead**

Next week centers on three critical deliverables driven by our core team
members: Sanyog Rai\'s engagement table production deployment, Erica
Fienman\'s Sales Hub solution evaluation, and Prateek Paikray\'s data
catalog mockup advancement.

**Engagement Infrastructure Completion:** Sanyog Rai expects to achieve
ZoomInfo data population across multiple tenants despite current
infrastructure blockers, with his Q3 testing improvement epics providing
a roadmap for preventing similar delays. His systematic approach to
infrastructure challenges positions us for reliable production
deployment. **On-Demand Refresh Architecture Finalization:** Erica
Fienman will conduct the critical Sales Hub evaluation meeting to align
on the optimal technical approach, ensuring our Global Event Bus
architecture delivers maximum value while avoiding duplicate development
efforts. **Data Catalog Design Advancement:** Prateek Paikray will
review Marina\'s mockups and lead the Dow Jones session to establish
data registry ownership models, positioning the unified admin portal for
Q3 prioritization while continuing Salesforce integration progress.

The team\'s exceptional individual contributions this week demonstrate
strong technical leadership and strategic thinking. Success next week
depends on Sanyog\'s infrastructure deployment, Erica\'s architectural
alignment, and Prateek\'s design advancement, with cross-team
coordination improvements enabling accelerated delivery.
