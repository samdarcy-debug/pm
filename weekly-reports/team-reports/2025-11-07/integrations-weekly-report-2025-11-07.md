---
id: weekly-integrations-2025-45
title: "Integrations Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Integrations Team Executive Roundup - Week of Nov 3, 2025**

## **Executive Summary**

Nvidia\'s account team has expressed strong interest in integrating
their in-house \"Nvidia Sales Assistant\" with ZoomInfo through the MCP
server, seeking to consolidate more than forty sales tools and enhance
seller productivity. Andres Perez has identified a pattern of enterprise
escalations from \$10M+ ACV customers requiring what they consider
\"bare minimum\" functionality, highlighting an urgent need to deliver
GTM Data Model import and single-form export capabilities on GTM
Workspace and Studio. Meanwhile, Sanyog Rai continues validating
engagement queries from app teams to ensure downstream teams can
properly leverage engagement data from Chorus and other sources.

## **This Week\'s Progress**

### **Key Momentum Areas**

Prateek Paikray presented the vertical dataset demo during the GTM
Monthly Platform Review, showcasing how the new Data Catalog UI now
consumes the GTM Store API to improve dataset discoverability and data
preview experiences. The demo highlighted end-to-end functionality from
registry to dataset publishing, with coordinated testing scheduled
following minor backend data fixes to properly render datasets in the
UI.

Sanyog Rai continued validating engagement use cases for downstream
teams, finding and clearing use cases while working through bugs. This
work supports the broader effort to ensure engagement data from Chorus
and other sources (emails, meetings, content interactions, calls) can be
properly leveraged across the platform, which will be foundational as
ZoomInfo expands its direction around engagement data.

Andres Perez confirmed the plan to address the final blocker for the
Auto-Custom-Field Agent in staging, positioning it to automatically
create field mappings from CRM page layouts using the Agentic Platform.
This capability will significantly reduce the burden on GTM Admins for
the success of GTM Studio, though progress this week was limited by
competing priorities including WebSights-to-Plays design work,
ServiceNow and Adobe product roadmap escalations, and the ZI-on-ZI
Email/Calendar configuration rollout to all 3,600 employees.

### **Goals & Progress**

**GTM Platform**: Sanyog Rai is working with the Data Platform team to
validate what engagement use cases can and cannot be supported for
downstream teams, with prioritized work identified for gaps. However,
the team is navigating a transition to a different storage layer for the
GTM Store, which may impact the ability to run certain queries and
requires careful validation of existing functionality.

**Vertical Datasets**: Prateek Paikray coordinated end-to-end testing
from dataset registry to UI discoverability, successfully demonstrating
how vertical datasets appear in the Data Catalog during the GTM Monthly
Platform Review. Enhancement tickets have been created in Jira to
address gaps discovered during testing, with the work positioned to
improve how customers discover and preview GTM intelligence within their
workflows.

**GTM Studio**: Andres Perez is building the Auto-Custom-Field Agent to
automatically generate field mappings from CRM page layouts, reducing
manual configuration work for GTM Admins. The agent has a confirmed path
forward to address its final staging blocker, though execution has been
delayed by higher-priority customer escalations and platform-wide
initiatives that required immediate attention this week.

### **Strategic Challenges**

Prateek Paikray had to reschedule the Cloud Data Share to Databricks
demo from Friday to Monday due to deployment issues in the UNIE services
on staging. The engineering team has since confirmed that the updated
components are deployed and functioning, clearing the path for testing
the Export to Databricks flow via Bobsled from GTM Studio ahead of the
November early access release and December general availability.

Sanyog Rai\'s work on engagement use cases faces potential impact from
the ongoing migration to a different storage layer for the GTM Store.
The team needs to validate whether existing queries will continue to
function and identify any adjustments required, adding complexity to the
timeline for completing the engagement use case validation. Sanyog will
be out of office next week, which will pause progress on this
workstream.

Andres Perez identified a concerning pattern: large enterprise customers
with \$10M+ ACV are experiencing low adoption or considering churn due
to functionality gaps they consider table stakes. Adobe is experiencing
low adoption and churning Chorus because ZoomInfo cannot match their
account ownership model, while ServiceNow on SOM CRM would not be able
to use any ZoomInfo applications without proper support. The underlying
issue is that while Platform already supports these capabilities, the
App teams cannot yet deliver them, creating an urgent need to prioritize
GTM Data Model import and a unified export solution on both GTM
Workspace and Studio.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Sanyog Rai reinforced an important operating principle: always be ready
for a major pivot at ZoomInfo. The unexpected shift to a different
storage layer for the GTM Store exemplifies how technical foundations
can change rapidly, requiring the team to maintain flexibility in
approach while ensuring customer-facing functionality remains stable
through transitions.

Prateek Paikray discovered through exploratory calls with True Context
and Medius Group that ZoomInfo needs to position the Revenue Agent for
Salesforce Agentforce thoughtfully to avoid confusion with existing
products. The team is framing Agentforce as an additional intelligence
access channel rather than a competing solution---best suited for
customers whose AI strategy centers on enabling sellers directly within
Salesforce, marrying ZoomInfo\'s GTM intelligence with their in-house
Salesforce agentic solutions to ensure alignment rather than overlap in
their workflow strategy.

Andres Perez learned that ZoomInfo continues to receive escalations from
enterprise customers for what they perceive as bare minimum
functionality---supporting new CRM vendors like ServiceNow\'s SOM,
handling the Account Team Member object in Salesforce, or determining
proper duplicate check flows. Without the ability to support both GTM
Data Model import and a single form of export on GTM Workspace and
Studio, the alternative is demonstrable: low adoption and churn from
strategic accounts that represent tens of millions in ACV, with Adobe
and ServiceNow serving as concrete examples of this risk materializing.

### **Cross-Team Dependencies**

Our work with Rowan\'s team on the MCP tools roadmap continues to be
important for extending capabilities into Agentforce. Prateek Paikray
shared feedback from Nvidia\'s account team emphasizing their initiative
to consolidate more than forty sales tools, and their interest in
connecting their in-house sales assistant with ZoomInfo via the MCP
server represents a meaningful validation of the MCP integration
strategy. The team needs continued coordination with Rowan\'s group to
define the roadmap for introducing new agentic functionality within the
Salesforce ecosystem.

Andres Perez identified the Data Platform team as necessary for enabling
the engagement use cases that Sanyog Rai is validating, while also
noting the need for closer collaboration with the Search team and
Engineering on scoping multi-instance CRM support for workbook creation.
Additionally, the volume of customer support escalations from high-value
accounts (Zoom Video, IOA) and partnership conversations (Outreach,
InformaTechTarget) is consuming bandwidth that should be directed toward
product development, suggesting a need for better escalation triage or
additional support resources.

## **Looking Ahead**

Next week focuses on preparing for December releases while advancing the
strategic integration initiatives that position ZoomInfo\'s intelligence
within customer AI and data workflows.

Prateek Paikray will prepare detailed implementation guides for Cloud
Data Share using the AI Marketing Engine to streamline content creation
and ensure consistency across product documentation for the December
release. He will also meet with Engineering to scope the technical work
required to support multiple CRM instances for workbook creation,
following this week\'s discussion with the Search team, defining key
milestones, dependencies, and deliverables to guide the implementation
plan. These efforts advance both the Vertical Datasets and Cloud Data
Share initiatives while laying groundwork for expanding CRM flexibility.

Andres Perez will prioritize the Auto-Custom-Field Agent again, working
to resolve the final staging blocker and move toward production
readiness. Success here would materially reduce the configuration burden
on GTM Admins and demonstrate the Agentic Platform\'s ability to
automate complex CRM mapping workflows---capabilities that become
increasingly important as the enterprise customer escalations highlight
the need for more sophisticated CRM support across multiple vendors and
configurations.

With Sanyog Rai out of office, the engagement use cases work will pause,
but the team maintains confidence in delivering value across the
Agentforce integration, vertical datasets, and Cloud Data Share
initiatives while addressing the enterprise customer requirements that
emerged as a strategic priority this week.

*Source: Team 1-2-3 Operating Framework entries from week of Nov 3,
2025*
