---
id: weekly-integrations-2025-43
title: "Integrations Weekly Report - October 24, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Integrations Executive Roundup - October 20, 2025**

## **Executive Summary**

Prateek Paikray shipped Data Preview functionality to staging this week,
completing the first milestone toward the November 10th GTM Studio
Catalog UI launch - additionally, implementing entitlement check to
support ZI Revenue Agent monetization so only \"ZI Revenue Agent\"
licensed users can access ZI data through Agentforce. Sanyog delivered
Account team role creation from Engagement data for all tenants and
partnered across app teams to confirm existing data solves priority use
cases. Andres Perez aligned with Rayee on the data connector publishing
pipeline launching by end of October and built a backlog of connectors
that Marc Frail will lead on building.

## **This Week\'s Progress**

### **Key Momentum Areas**

Prateek Paikray delivered the Data Catalog UI integration with Dataset
APIs and completed Data Preview functionality on staging, marking the
first milestone for the November 10th production release. This work
directly enables self-service data exploration for customers and
unblocks the GTM Studio Catalog experience. The engineering team also
implemented entitlement checks for Agent Force, meaning the solution can
now verify user licenses before responding---enabling monetization of
partner-built integrations beyond the initial use case.

Andres Perez completed WebSights content interaction event examples,
documenting what happens when someone visits a homepage, pricing page,
and completes a form with de-anonymization. This work, validated by the
Platform team, establishes the data model for website activity that will
flow into Copilot Workspace, Chat, GTM Studio, and Context. Andres
aligned with Rayee to ensure the publishing pipeline for managed data
connectors launches by end of October and built a prioritized backlog of
connectors that Marc Frail will lead on building, with 5 connectors
already in development for November.

Sanyog Rai\'s team deployed account team role creation for all tenants
with engagement data flowing and figured out the midterm backfill
approach, enabling 6 months of historical data to populate starting next
week. This improves account targeting data quality and moves engagement
usage forward for downstream teams. The meeting with Philip and Dominik
yesterday around tech and product leadership alignment also triggered
urgency on organizing engagement use cases, with Victor and Rakesh now
working to clarify what downstream teams can and cannot do with current
capabilities.

### **Goals & Progress**

**GTM Platform**: Sanyog Rai has account team role creation running for
all tenants, though currently only for accounts directly linked to
engagements rather than all participant-associated accounts. The midterm
backfill solution uses a workaround that required some development but
will enable 6 months of historical data to flow to all tenants starting
next week. Work continues on validating GraphQL queries for downstream
teams and organizing front-end updates for the Admin Portal, including
improved privacy processes and configuration management.

**Partnerships & GTM Studio**: Andres Perez completed WebSights content
interaction examples and received Platform team validation on the data
model for site visits and form completions. The remaining work for the
Content Interactions Upsert API has been ticketed and Andres aligned
with Rayee on launching the data connector publishing pipeline by end of
October. He built a prioritized backlog of managed data connectors for
November using Clay.com as inspiration, which Marc Frail will lead on
building. The team identified that existing native integrations
(Salesforce, sales engagement platforms) need data connector
functionality exposed so customers can extend actions using existing
authentication.

**Vertical Datasets**: Prateek Paikray\'s team delivered the Data
Catalog UI integration with GTM Store APIs and completed Data Preview
functionality, with minor enhancements pending. The team aligned with
the integration and GDP engineering teams to backfill GTM opportunity
data with legacy global opportunity fields, unblocking the ROI team\'s
migration to GTM data model. However, no opportunity history has been
explicitly migrated yet, pending confirmation of additional data point
requirements from the ROI team.

### **Strategic Challenges**

The most important vendors for managed data connectors are actually the
ones where we already have native integrations---Salesforce, Outreach,
Salesloft. Andres Perez identified that customers need the ability to
extend existing integrations by adding new endpoints while using current
authentication, such as enriching from a Salesforce page layout or
workbook. While Sanyog Rai\'s team is working to get more data through
the GTM data model from Outreach and Salesloft (targeted for
December/January work, ready by February), there\'s tension around
whether to expose raw data connector functionality now versus waiting
for the structured, clean solution. The path forward requires alignment
with Ray on exposing all uni actions as read-only data connectors for
existing integrations.

Sanyog Rai discovered a gap in how we handle engagements with multiple
companies. Through the orchestration service, there\'s a primary company
linked to each engagement based on backend logic, and we create account
team roles only for that primary company. In a partnership call scenario
with three different domains represented as three separate CRM accounts,
we would only link internal participants to one account currently. While
the team plans to link users to all relevant accounts in the future
(pending account creation work), this means we\'re missing potential
account relationship signals right now. The team is also grappling with
how to handle conference events (50+ participants) versus regular
meetings, with Andres suggesting content interactions with an \"attend\"
type might be the right model for providers like Netline who track
conference attendance data.

Front-end teams need better visibility into data sources within
workbooks and workspace. Dominik raised the need to clearly show where
data comes from by displaying provider logos (Google Calendar, Gong,
Zoom) stacked on activity records and workbook data. Andres demonstrated
that the necessary metadata exists in GraphQL queries (provider source,
recording source, conference source, calendar source), and logos are
stored in OptMS for the All Integrations page, but implementing this
requires coordination with the workbook team. A related challenge
emerged around Gmail versus Google branding, highlighting the need for
more granular source attribution.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Specific mapping exercises and deep requirement dives prevent downstream
issues that only surface later. Sanyog Rai emphasized this learning
after working through the account team role implementation and
discovering the multi-company engagement gap. The team\'s approach of
doing detailed walkthroughs---like Andres\'s WebSights example tracing
homepage visit → pricing page → form completion →
de-anonymization---reveals edge cases and missing functionality before
they become production problems. This methodology proved valuable again
when examining conference events versus meetings, leading to the
realization that a content interaction model may better serve
large-scale event tracking.

Product managers can and should build working prototypes with Klein that
connect to staging endpoints, with engineering taking over for
production hardening. Andres Perez explained that a PM should complete
the first version showing which endpoints are needed and the process
flow, getting it working against staging tenants. Engineering then
switches to production endpoints, ensures scalability, updates MCP tools
in the Agentic platform, and handles proper authentication token
management. Sanyog Rai initially raised concerns about PMs making live
configuration changes, but the team aligned on this being the right
boundary---PMs prototype functionality, engineers productionize it.
Andres has already demonstrated this with his integrations agent that
checks custom fields and creates new ones in staging Salesforce
environments.

The Agent Force launch at Dreamforce generated immediate enterprise
interest, with four customers (Engine, Gartner, TVSquared, and
Salesforce) expressing intent to explore the solution. Prateek Paikray
has meetings lined up for next week to walk through demos and answer
questions. The bigger unlock came from the entitlement check
implementation---completed just this week---which allows the team to
verify user licenses before Agent Force responds. This means any
partner-built integration can now be monetized, not just Agent Force
itself. The team can begin selling the solution officially once the new
package version publishes on Tuesday, with the entitlement scope
available for partner apps in staging now.

### **Cross-Team Dependencies**

Our work with the Data Platform team and Nebo\'s team experienced recent
friction that was resolved before the meeting with Philip and Dominik,
but that session highlighted a more fundamental need. Sanyog Rai has
blank spots in understanding use cases from downstream teams,
particularly around what engagement data capabilities are needed versus
what exists today. Victor and Rakesh (Sean\'s engineering partner, with
Sean out of office) are now actively gathering use cases to bring to
Sanyog\'s team. Once organized, Nebo indicated he can figure out
front-end resources if needed. This coordination is necessary for both
the querying aspect (ensuring all data can be accessed in views or
Copilot Chat) and front-end updates to the admin portal.

The sales engagement platform work crosses teams, with Sanyog Rai\'s
engineering resources working on getting more Outreach and Salesloft
data through the GTM data model. That work is scheduled for December and
January, targeting February availability on the Unified Roadmap.
However, this timeline creates tension with the managed data connectors
work, where exposing the ability to call Outreach directly to populate
workbook cells would unblock customers now. The question of whether to
ship the raw capability now or wait for the structured solution requires
alignment between Andres Perez, Sanyog Rai, and Ray, particularly around
the strategy for exposing existing uni actions as data connectors.

## **Looking Ahead**

Next week\'s primary focus shifts to organizing and validating
engagement data use cases for downstream teams, with Sanyog Rai aiming
to provide clear guidance on what\'s possible with current capabilities
versus what requires additional work. This clarity will inform Q4
planning and help prioritize front-end updates to the Admin Portal.

Andres Perez is picking up agent work, likely focusing on the privacy
agent and working closely with Sanyog Rai for an hour or two to align on
the approach. Success means PMs can build functional staging prototypes
using Klein while engineering takes over for production hardening.
Prateek Paikray\'s team enters Q4 planning with three key deliverables
for the January release: multi-CRM support for ingestion and export,
engagement data share capabilities for Snowflake and Databricks
(extending the November early access launch), and auto-publish
functionality for partner apps in the internal integrations marketplace.
The team also has four enterprise customer meetings scheduled to discuss
Agent Force, with the solution now ready for monetization following
Tuesday\'s package release. Marc Frail continues building from the
managed data connectors backlog that Andres created, with the publishing
pipeline launching by end of October and 5 connectors targeted for
November, though the team needs to resolve the question of exposing data
connector functionality for existing native integrations before
customers start requesting these capabilities.

*Source: Team 1-2-3 Operating Framework entries from October 20-24,
2025*
