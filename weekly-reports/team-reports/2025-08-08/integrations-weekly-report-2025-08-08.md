---
id: weekly-integrations-2025-32
title: "Integrations Weekly Report - August 08, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-08-08
updated: 2026-01-06
week_ending: 2025-08-08
reporting_period: "August 4-8, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Integrations Executive Roundup - Week of August 4, 2025**

## **Executive Summary**

Sanyog Rai successfully onboarded Email data into GTM Data Model for
ZI-on-ZI (targeting 90%+ tenant populated by end of next week) in
addition to refining the overall [[engagement
architecture]{.underline}](https://docs.google.com/document/d/1ngHDuBc_ySro9_1S1PQTT6uSnfAt1lsUsgPDmzUmYF4/edit?tab=t.0)
in partnership with engineering. Prateek Paikray advanced the Salesforce
Agentforce package into the security review stage as the team starts
beta testing with customers next week in addition to progressing designs
for Custom Data Sets and revealing a [[demo of Snowflake Data Shares via
Boblsed]{.underline}](https://zoominfo.slack.com/archives/C01NA8B3R28/p1754487127270669).
Erica Fienman got aligned with the Copilot V2 team to prioritize
Event-based CRM Import in September to avoid derailing in-flight
projects including 3-hour import frequency, mapping custom fields as GTM
records, and migrating the last wave of customers off legacy CRM import
pipelines. Andres Perez worked with Legal and Partnerships to draft a
new generic Connector Agreement that has been sent to Clari for
signature.

## **This Week\'s Progress**

### **Key Momentum Areas**

GTM Data Model Email Integration: Sanyog Rai achieved a critical
milestone by successfully onboarding email data into GTM Data Model for
ZI-on-ZI, with production deployment now stable and targeting 90%+
tenant population by end of next week. This foundational work enables
downstream application teams to leverage email engagement data directly
from GTM DM (via GraphQL API in testing) while establishing the
architecture framework for broader engagement data integration.

Salesforce Agentforce Advancement: Prateek Paikray successfully advanced
the Salesforce Agentforce managed package into the security review
stage, positioning the team to begin beta testing with enterprise
customers next week. Simultaneously, he progressed designs for Custom
Data Sets marketplace, positioning us to deliver on our H2 goal.

Strategic Project Alignment: Erica Fienman secured critical alignment
with the Copilot V2 team to prioritize Event-based CRM Import work for
September, protecting in-flight engineering initiatives including 3-hour
import frequency, custom field mapping as GTM records, and the final
migration wave off legacy CRM import pipelines. This strategic
sequencing prevents context switching for engineering while ensuring
November GA release timeline remains achievable.

### **Goals & Progress**

Partner Ecosystem Scaling: Andres Perez collaborated with Legal and
Partnerships to draft a new generic Connector Agreement that
standardizes partner onboarding processes, with the agreement now sent
to Clari for signature. This replaces the previous approach where
partners were only agreeing to our Customer T&Cs on the public intake
form.

Legacy System Migration: Erica's two new features for GTM DM CRM import
(Conditional Importing and Custom GTM DM fields) are in testing and will
together solve the Advanced Search requirements that prevented migration
of over a thousand ZI tenants from the legacy import pipeline. Once
these customers are migrated, their data will flow to Contributory
Network, improve the Northstar "Active Integrations" metric, and the
pipeline will be deprecated.

Engagement Architecture Refinement: Sanyog Rai led engagement
architecture discussions with engineering teams, identifying critical
gaps between current functionality and end-state product requirements.
These sessions established clear technical requirements for scaling
engagement data processing and laid groundwork for enhanced site visitor
resolution capabilities.

## **Strategic Challenges**

Customer Integration Experience: The team continues to address recurring
customer onboarding issues where executives discover personal activity
in their engagement feeds, leading to integration shutdowns and data
deletion requests. Sanyog Rai is developing a comprehensive solution
including privacy agents that automatically populate ignore/block lists
with C-level executives and will support the admin launch button
requiring admin approval before data ingestion begins.

Technical Infrastructure Dependencies: While GTM Store deployment is
progressing well, the team identified that current IP-based visitor
resolution approaches need enhancement with cookie storage and user
agent string processing for accurate individual identification. This
discovery through meetings with Brett Elliot and Matt Barnes will
require architectural adjustments to support advanced site visitor
resolution services.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Partner API Access Framework: Andres Perez established the complete
technical framework for partner API access, learning that the system
requires OAuth app scopes tied to endpoints, customer entitlements to
those scopes, and LaunchDarkly flags controlling data access with 403
responses for unauthorized customers. This creates a clear path for beta
endpoint management and enables controlled partner integration scaling.

Marketplace Scalability Validation: The team validated through
Partnerfleet that supporting up to 10,000 generic partner listings is
both technically feasible and economically advantageous at no
incremental cost. This approach will drive SEO benefits, reduce customer
support volume for integration questions, and create opportunities for
partner referrals and revenue sharing programs.

IP resolution to Individuals: Sanyog identified that IP address
information alone is not enough to resolve individuals, prompting a new
set of attributes to ensure engagement data persists cookie information
for ZoomInfo, or vendors like Marketo, to resolve real-time or batch.

### **Cross-Team Dependencies**

Our collaboration with the ZDP team on real-time ingestion capabilities
continues to progress, with Erica Fienman securing agreement that export
functionality can be strategically deferred to September. The Workflow
team remains essential for manual export capabilities, with Mark
confirming that opportunity updates are already supported from the
workbooks implementation.

Coordination with the Chorus team revealed ongoing user management
service integration needs, with the team identifying that consolidating
Chorus users into the platform user management service will prevent data
ingestion issues when ZoomInfo seats are removed. This integration
aligns with the broader platform consolidation strategy.

## **Looking Ahead**

Next week focuses on scaling production deployments, initiating customer
beta programs, and executing strategic partnership agreements.

Sanyog Rai will complete the expansion to 90%+ tenant coverage for email
data in GTM Data Model, enabling widespread access to engagement data
for downstream applications. Prateek Paikray will begin beta testing the
Salesforce Agentforce package with enterprise customers including ADP
and Redshift, while finalizing Custom Data Sets marketplace designs with
the engineering team. Erica Fienman will continue scoping September\'s
Event-based CRM Import work while ensuring in-flight projects maintain
momentum. Andres Perez will execute the Partnerfleet marketplace revamp
and advance partner API testing as connector agreements are finalized.

These coordinated efforts position the team to deliver significant value
across customer experience, partner ecosystem growth, and data
infrastructure modernization while maintaining clear focus on the
November Copilot v2 release timeline.

*Source: Team 1-2-3 Operating Framework entries from August 4-8, 2025*
