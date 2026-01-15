---
id: weekly-integrations-2025-39
title: "Integrations Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Integrations Executive Roundup - September 22, 2025**

## **Executive Summary**

Prateek and team finalized the Agentforce demo recording, trained
Solution Consultants, and armed the team with marketing assets for the
October 14th launch - additionally, secured customer interest from
Intuit (MCP integration), ADP (prospecting focus), and MasterCard
(analytics use case), while resolving Demo org Salesforce licensing
roadblocks through contract amendments. Sanyog defined requirements for
importing Salesloft and Outreach activity data. However, quality
assurance gaps arising from poor development environments (Chorus ETL)
and lack of production testing as Eng teams face churned resources and
eliminated QA/PMM roles demand more time from Product Managers.

## **This Week\'s Progress**

### **Key Momentum Areas**

Agentforce achieved major launch readiness with Prateek Paikray
completing the demo recording alongside Ryan Stevens and equipping the
revenue enablement team with all marketing assets. Solution Consultants
received hands-on training and the team resolved Salesforce demo org
licensing issues through contract amendments, enabling internal sellers
to access the solution.

Customer validation accelerated with three enterprise demos this week.
Intuit expressed strong interest in Agentforce with MCP integration
capabilities, ADP showed openness despite not prioritizing Copilot, and
MasterCard revealed compelling analytics use cases for their complex
multi-CRM environment serving 100+ subsidiaries.

Technical infrastructure progressed as Sanyog Rai completed requirements
documentation for sales engagement data ingestion from Outreach and
Salesloft partners. Recording and transcript data became available in
production for select tenants, with calendar data now accessible across
all customers.

### **Goals & Progress**

**Agentforce Launch Preparation**: Marketing assets finalized with
creative team making final edits to the demo recording. Dataset API
development completed with engineering alignment on integrating
Marketplace UI to showcase vertical datasets dynamically. Prateek
Paikray coordinated testing sessions with Implementation teams and
Solution Consultants while ensuring the latest managed package version
will be installed in sandbox environments.

**GTM Studio Agent Development**: Andres Perez submitted a pull request
for the field mapping agent, currently under Ryan Stevens\' review for
staging deployment. The POC aims to reduce GTM Admin workload by
enabling auto-custom-field creation from CRM page layouts through the
agentic platform.

**Data Platform Expansion**: Sales engagement data requirements
documentation completed by Sanyog Rai, awaiting engineering review
scheduled for early next week. This initiative brings partner data from
Outreach and Salesloft into the platform, expanding available datasets
for customer use cases.

### **Strategic Challenges**

Resource constraints are reaching a breaking point as teams absorb
responsibilities from eliminated PMM and QA functions without new tools
or processes to handle increased workloads. Engineering teams have lost
personnel with limited backfill capability, yet expectations remain to
maintain accelerated shipping schedules and handle production testing
that previously had dedicated support.

Testing environment limitations compound quality issues as Sanyog Rai
identified gaps in staging data coverage across different CRM platforms
like Dynamics, HubSpot, and Outlook. The lack of comprehensive staging
environments forces teams to discover integration issues in production,
creating customer-facing problems and eroding confidence in automated
testing systems.

Tier 1 product release for Agentforce highlights confusion across
Marketing, Sales and CX stakeholders with new PMM Engine. Different
templates requested by Carl and a gap in identifying how onboarding
needs to change (e.g. Salesforce processes for onboarding native apps)
shows additional stakeholders need to be educated and consulted for
feedback on PMM Engine.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Customer demand patterns revealed interesting divergences from expected
adoption paths. Intuit\'s preference for MCP integration over managed
packages suggests enterprise customers may prioritize protocol-based
connections for greater flexibility. ADP\'s willingness to explore
Agentforce without Copilot indicates potential market expansion
opportunities beyond current platform requirements.

Enterprise complexity requirements exceed current platform capabilities
as demonstrated by MasterCard\'s multi-CRM scenario. Their need to
aggregate engagement data across many subsidiary CRM instances
represents a sophisticated use case requiring product roadmap evolution
to support multiple CRM instance connections and cross-system analytics.

### **Cross-Team Dependencies**

Engineering review capacity remains the bottleneck for sales engagement
data requirements, with Sanyog Rai awaiting feedback on documentation
that could unlock partner integrations. The extended review cycles
impact customer-facing features and limit the team\'s ability to respond
to market opportunities requiring enhanced data connectivity.

Revenue enablement collaboration proved effective as Prateek Paikray
successfully equipped internal sellers with Agentforce materials and
training. This partnership model could be replicated for other product
launches, though it requires continued coordination to ensure messaging
alignment between product capabilities and sales positioning.

## **Looking Ahead**

Next week focuses on production deployment of the field mapping agent
behind feature flags while completing Agentforce entitlement check
implementation through engineering POC work. Prateek will conduct final
testing sessions with Solution Consultants and Implementation teams to
ensure launch readiness.

The path forward for new releases requires addressing quality assurance
systematically rather than relying on individual responsiveness to
production issues. Either engineering resources need expansion or
product roadmap pacing must align with available testing capacity to
maintain customer trust in platform reliability.

*Source: Team 1-2-3 Operating Framework entries from September 22-26,
2025*
