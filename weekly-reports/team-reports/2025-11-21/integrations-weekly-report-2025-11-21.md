---
id: weekly-integrations-2025-47
title: "Integrations Weekly Report - November 21, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-11-21
updated: 2026-01-06
week_ending: 2025-11-21
reporting_period: "November 17-21, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Integrations Team Executive Roundup - Week of Nov 17, 2025**

## **Executive Summary**

Sanyog Rai successfully deployed GTM Engagement sourced accounts to
staging and validated all open Workspace use cases against GTM
Engagement data via GraphQL. Prateek Paikray progressed the design
pattern for supporting multiple CRMs of the same vendor while meeting
with Agentforce-interested customers including Perficient, a Salesforce
implementation services provider - all representing significant progress
toward enterprise readiness. Andres Perez advanced the GTM Field Mapping
Agent to staging with a demo in the #producks Slack channel. These
achievements position us well for December 1st when the Workspaces
engineering team will begin production testing with GTMDM, validating
our engagement data model with real customer scenarios. However,
resource constraints across Osher\'s Integration ZDP team (now handling
double the responsibility with only 3-4 engineers) have pushed the
Custom Object to GTM Object integration from December to mid-January,
prompting escalation to Dominik and Nebo for additional engineering
support.

## **This Week\'s Progress**

### **Key Momentum Areas**

Sanyog completed all requirements for Workspaces use cases ahead of the
December 1st production testing milestone, with the engineering team
confirming readiness to validate GTMDM with engagement data. This
includes solving the complex challenge of linking engagements to
multiple CRM accounts - a capability the Workspaces team hadn\'t
previously understood but which unlocks accurate activity tracking
across enterprise account hierarchies. The work sets the foundation for
ServiceNow, IBM, Adobe, and HPE deployments in Q1.

Prateek advanced discussions with Perficient, a major Salesforce
reseller, who expressed strong interest in building customer solutions
using Agent Forge with ZoomInfo\'s Conversational Intelligence. While
they\'re specifically waiting for MCP integrations to become available,
this partnership could create a flywheel effect where Perficient becomes
both a customer and an advocate who packages ZoomInfo into their
standard Salesforce implementations. The Salesforce partner session has
been rescheduled to December 4th to continue exploring these
opportunities.

Andres published text for 23 data connectors built by Marc Frail, making
them visible on market.zoominfo.com alongside information about API
access and webhooks for partner-built integrations. Additionally, he met
with Typeform to explore integration opportunities - they already use
ZoomInfo data through OEM but can push form fill data back as content
interactions with virtual contact creation, adding another engagement
data source to the ecosystem.

### **Goals & Progress**

**Workspace Enterprise Enablement**: The team aligned on a unified
approach to serve ServiceNow, IBM, Adobe, and HPE customers through
Workspace by delivering GTM data model integration, account team object
permissions, ServiceNow CRM support, and data connector exports. Andres
is creating a project plan with Sarah Heritage to target delivery
between March and May, consolidating what were previously separate
customer requests into a single strategic initiative that will unlock
these major accounts.

**Vertical Dataset Integration**: Prateek completed alignment with
Integration ZDP and the Workbook team to understand frontend resource
requirements for vertical dataset integration in Audience. The team is
now waiting for Asaf to identify which frontend resource will support
this work, with the understanding that Rayee\'s team only has two
frontend engineers who are already committed to custom object work.
Separately, the engagement data share self-service feature that would
benefit both support and CX teams has been pushed to March at the
earliest.

**Platform Architecture Stability**: The Data Platform team reversed
their plan to migrate from BigQuery to Solar for GraphQL queries,
preserving stability and avoiding disruption to all integration queries.
This decision came after recognizing that Solar may not support
recursive org hierarchies or provide the same aggregate accuracy that
current use cases require. GraphQL will continue operating on BigQuery
for the foreseeable future, even as other data moves to federated
search, eliminating a major technical risk.

### **Strategic Challenges**

Osher\'s Integration ZDP team is operating at half capacity on new
feature development because they\'re spending the other half improving
the SIP worker to eliminate silent failures in the ingestion process.
The team previously had 5-6 engineers and also had the extract portion
of ETL handled by another team - now 3-4 engineers handle both
responsibilities. While they\'re doing excellent work and the ingestion
process has never been more reliable, this resource constraint has
delayed Custom Object to GTM Object integration from December to
mid-January. Andres escalated this to Dominik, who brought in Nebo to
explore adding engineering resources to the team.

Rayee\'s team only has two frontend engineers, creating a bottleneck for
both the custom object work and Prateek\'s vertical dataset integration
needs. The last thing the team wants is to pull one of these two
engineers off custom object delivery to support vertical datasets, so
they\'re actively looking for frontend support from outside the
integrations organization. This frontend resource constraint is
compounding the backend engineering challenges and could impact multiple
Q1 deliverables if not addressed.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The Workspaces engineering team discovered they had no understanding of
how ZoomInfo links engagements to different CRM accounts, initially
reporting that they couldn\'t find any engagements for Google before
realizing they needed to check all Google entities (like \"Google
Incorporated\"). This revealed that even internal teams lack visibility
into the sophistication of our data model, particularly around account
hierarchies and duplicate management. The incident reinforces the urgent
need for Unified Profile - currently, connecting email creates GTM
contacts and accounts, then connecting CRM two days later creates
duplicates, a fundamental problem that will only worsen as Workspace
adoption grows.

Perficient\'s specific interest in MCP integrations indicates that
enterprise Salesforce resellers are thinking beyond basic data
integrations toward true agentic experiences. They want to build entire
agent-based solutions for their customers using Agent Forge with
Conversational Intelligence, suggesting there\'s a market for packaged,
deployment-ready solutions that combine ZoomInfo capabilities with
Salesforce Agentforce. This could represent a new channel strategy where
resellers become implementation partners who reduce friction for
enterprise buyers.

The team identified that CSM enablement in Workspace (and even AM
enablement) will require product usage data from Snowflake to be ETL\'d
into GTMDM. This data doesn\'t currently exist in a queryable format
alongside customer data, requiring a new product usage object that joins
product and contact objects. Adam Severance is driving this requirement
from the CSM perspective. Additionally, concepts like NPS should
potentially be treated as either engagements or their own sentiment
table - the GTM data model needs extension to support these customer
success use cases.

### **Cross-Team Dependencies**

Our work with the Data Platform team remains essential, though
communication gaps emerged when Sanyog discovered in an everyday meeting
that the Solar migration reversal hadn\'t been communicated to him
despite ongoing technical discussions. The team will continue querying
through GraphQL to BigQuery, but Sanyog needs to confirm in his next
meeting with the Data Platform team about the unified view of
engagements - the proposed solution to reduce joins across engagement
types. The team is also proposing an Account engagement roles collection
that would provide a direct connector between engagements and accounts,
eliminating the need to traverse through seven objects to answer
questions like \"how many meetings have we had with this account?\"

Frontend resource allocation from Asaf\'s organization will determine
timing for multiple initiatives. The Workbook and Integration ZDP teams
have outlined requirements, but until Asaf confirms which resource will
support vertical dataset integration, the team cannot finalize delivery
timelines with the GTM Store team. This dependency is compounded by
Rayee\'s team having only two frontend engineers already committed to
custom object work, making it impossible to support additional
initiatives internally.

## **Looking Ahead**

Next week\'s focus centers on three parallel tracks: Sanyog finalizing
requirements for engagements pushed through the Upsert API, Prateek
traveling to India while maintaining alignment for the December 4th
Salesforce session and completing UI grooming for multiple CRM
instances, and Andres creating the comprehensive project plan with Sarah
Heritage that unifies enterprise customer requirements.

The December 1st production testing milestone with Workspaces represents
a major validation point - the team will have real engineers using GTMDM
in a staging environment, discovering any gaps in the engagement data
model before broader rollout. MJ and Linda will join the Bethesda
working session that week alongside Sanyog, providing in-person support
to resolve issues quickly. Success here builds confidence for the
ServiceNow/IBM/Adobe/HPE timeline and demonstrates that the engagement
data architecture can handle enterprise complexity. Meanwhile, the
frontend resource decision from Asaf and the engineering resource
discussion with Dominik and Nebo will shape Q1 capacity and determine
which initiatives can accelerate versus which need timeline adjustments.

*Source: Team 1-2-3 Operating Framework entries from Nov 17-21, 2025*
