---
id: weekly-integrations-2025-44
title: "Integrations Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Integrations Team Executive Roundup - October 27, 2025**

## **Executive Summary**

Prateek Paikray successfully released the new Agentforce managed package
with entitlement tracking and completed Data Catalog UI integration with
the Global Dataset API, while organic customer interest from Flex.com,
Uber for Business, and FedEx validates market demand for the ZI Revenue
Agent. Sanyog Rai\'s systematic validation of engagements use cases is
identifying GraphQL and GTM Store issues before they impact downstream
teams, creating a quality gate that ensures platform reliability. Erica
Fienman's roadmap continued to execute with CRM importing every one hour
for all GTM DM tenants, and GTM DM backfill at 100% complete. Andres
Perez built foundational Auth-MS infrastructure within the Agentic
Platform that unblocks future vendor tool development and enables the
Auto-Custom-Field Agent to access user tokens and CRM configurations.

## **This Week\'s Progress**

### **Key Momentum Areas**

Sanyog Rai is validating engagements use cases for downstream teams by
systematically reviewing queries against actual platform capabilities.
His methodology of confirming queries through hands-on testing is
uncovering actionable issues with GraphQL and the GTM Store that would
have impacted teams relying on these capabilities, and the team has
already prioritized fixes based on his findings.

Prateek Paikray delivered the new Agentforce managed package with
entitlement tracking capabilities and successfully demoed the solution
to Engine and Salesforce teams to onboard Flex.com as a customer. He
held internal discussions with Account Management for Uber for Business
and FedEx to position Agentforce for their specific use cases,
demonstrating how organic inbound interest from mutual Salesforce
customers validates the market demand for agentic solutions and creates
opportunities for deeper collaboration.

Andres Perez built a reusable Auth-MS client within the Agentic Platform
that provides a standardized way for vendor tools to access user tokens
and connected integrations. This infrastructure work solves a
longstanding limitation that prevented building certain vendor tools in
the past, and his Auto-Custom-Field Agent can now create custom fields
on GTM Objects, retrieve field mappings between GTM and vendor objects,
and access Salesforce page layout information using authenticated user
tokens.

### **Goals & Progress**

**GTM Platform Vertical Datasets**: Prateek Paikray completed
integration of the Data Catalog UI with the new Global Dataset API
developed by the GTM Store team, enabling unified data preview
functionality across both internal and external marketplaces. He also
initiated Q4 planning with the Engineering team for multi-instance CRM
ingestion, which will allow customers to create workbooks directly from
CRM data across multiple instances of the same CRM system. His
collaboration with Lars and the Platform team defined the integration
approach between Agentforce and the ZoomInfo Agentic Platform to enable
unified Copilot Chat experiences within Salesforce.

**GTM Platform**: Sanyog Rai is working through priority engagements use
cases for downstream teams to validate what the platform can and cannot
currently support. His approach of reviewing use cases and confirming
queries has proven effective at identifying platform gaps early,
allowing the team to understand limitations and prioritize work to
address them before downstream teams encounter issues in production
environments.

**GTM Studio**: Andres Perez made substantial progress on the
Auto-Custom-Field Agent within the Agentic Platform, successfully
implementing six core capabilities including creating custom fields on
GTM Objects, retrieving current fields and field mappings, updating
mappings between GTM and vendor objects, and accessing Salesforce page
layout fields using authenticated user tokens. When the team identified
that the Agentic Platform lacked a standard mechanism for accessing user
tokens and integrations, they made the strategic decision to build the
Auth-MS client as foundational infrastructure. This work reduces the
burden on GTM Admins and enables self-service field configuration that
will accelerate GTM Studio adoption.

### **Strategic Challenges**

Prateek Paikray identified a dataset attribute standardization gap in
the GTM Store where different datasets use inconsistent naming
conventions (for example, \"creditorzicompanyid\" in LoanStatements
versus \"zoominfo_company_id\" in GTM Account dataset). This lack of
standardization increases the development effort required to train
Agentforce and other AI agents consistently across datasets, creating
technical debt that will compound as more vertical datasets are added.
Establishing governance standards or abstraction layers could
significantly reduce ongoing integration complexity and accelerate agent
training across the platform.

Andres Perez encountered authentication issues when attempting to
upgrade the Auth-MS client within the Agentic Platform to retrieve the
CRM user for import connections. The API swagger documentation isn\'t
providing clear authentication guidance, which has led to a planned
session with Ilan on Monday to resolve the technical approach. Once this
authentication pattern is established, the Agentic Platform will have a
repeatable pattern for accessing user tokens that can be applied to
expanding CRM coverage beyond Salesforce to HubSpot and Microsoft
Dynamics.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Sanyog Rai discovered that methodically reviewing engagements use cases
against actual GraphQL queries is an effective quality assurance
mechanism for the GTM Store. This approach catches platform issues
before they impact downstream teams and provides concrete prioritization
data about which limitations matter most for real-world use cases. The
pattern of validating platform capabilities through actual use case
testing could be applied to other platform validation efforts to improve
release quality and reduce downstream friction.

Prateek Paikray observed growing organic interest in the ZoomInfo
Revenue Agent from mutual Salesforce customers, indicating strong market
validation for the Agentforce solution. This inbound demand from
enterprise customers like Flex.com, Uber for Business, and FedEx
suggests the solution is addressing real pain points and creates
leverage for expanding the partnership with Salesforce beyond initial
accounts. The pattern of interest from large enterprise customers
indicates the agentic approach scales to complex use cases and positions
ZoomInfo as a strategic Salesforce partner.

Andres Perez\'s work on the Agentic Platform revealed that the platform
lacked a unified way to access user tokens and integration
configurations, which explained why certain vendor tools had been
challenging to build in previous attempts. Rather than creating one-off
solutions for the Auto-Custom-Field Agent, the team made the strategic
decision to build proper infrastructure through the Auth-MS client, with
plans to incorporate the new Integration Config Service as the single
source of truth for settings and connection status. This architectural
improvement will accelerate future agent development across the Agentic
Platform and reduce technical debt.

### **Cross-Team Dependencies**

Our collaboration with the Engineering team on multi-CRM ingestion and
Cloud DataShare for Engagement is advancing with Q4 planning now
underway and epics created in JIRA for execution. The work with Lars and
the Platform team to define Agentforce integration with the ZoomInfo
Agentic Platform is progressing well, with alignment on the technical
approach to enable unified Copilot Chat across Salesforce and Slack.
Prateek Paikray is coordinating with Rowan\'s team next week to review
the MCP tools roadmap and ensure alignment between Agentforce
capabilities and the broader Agentic Platform strategy, which will
inform how new agentic functionality can extend to Agentforce
implementations.

## **Looking Ahead**

Next week focuses on completing validation work for engagements,
demonstrating the vertical dataset experience to stakeholders, and
expanding Agentic Platform CRM coverage. The team is positioned to move
from infrastructure building and validation to broader platform
enablement and customer demonstrations.

Prateek Paikray will conduct end-to-end testing of the Data Catalog from
dataset registry through UI discoverability to validate the vertical
dataset experience, record a vertical dataset demo for the upcoming GTM
Monthly Platform Review to showcase progress and functionality, test the
Export to Databricks via Bobsled functionality for Cloud Data Share, and
meet with Rowan\'s team to review the MCP tools roadmap and align on how
these capabilities can extend to Agentforce. Sanyog Rai will complete
his review of priority engagements use cases, providing a clear picture
of platform readiness and known limitations for downstream teams. Andres
Perez will resolve the Auth-MS authentication approach with Ilan on
Monday and then expand the CRM tool within the Agentic Platform to
support retrieving page layout fields for HubSpot and Microsoft Dynamics
in addition to Salesforce.

The team\'s progress on engagements validation, Agentforce customer
traction, and Agentic Platform infrastructure positions us well to
accelerate agent capabilities, vertical dataset adoption, and multi-CRM
support in the coming weeks.

*Source: Team 1-2-3 Operating Framework entries from October 27-31,
2025*
