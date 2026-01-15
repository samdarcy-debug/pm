---
id: weekly-integrations-2025-42
title: "Integrations Weekly Report - October 17, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-10-17
updated: 2026-01-06
week_ending: 2025-10-17
reporting_period: "October 13-17, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Integrations Executive Roundup - Week of October 13, 2025**

## **Executive Summary**

Agentforce is now live in ZoomInfo\'s Salesforce demo org, enabling
internal sellers to demonstrate the solution ahead of the October 28th
GA launch. Prateek Paikray completed package updates and knowledge
center articles while coordinating with RevOps to provision necessary
SKUs. Sanyog Rai is deploying account team role creation and recording
data across all tenants next week, completing foundational engagement
data relationships that enable downstream features like priority
accounts and activity feeds. A data quality issue discovered this week
highlights platform monitoring gaps: the ziUserId field broke in
September after an accidental metadata change, only caught through
chance investigation by David Wheeler.

## **This Week\'s Progress**

### **Key Momentum Areas**

Prateek Paikray achieved full alignment with the GTM Store and
Integration Engineering teams on the technical approach for dataset
preview functionality, unblocking the V1 marketplace release. The
Integration team will build an interim preview service calling specific
record IDs to showcase sample data, with plans to transition to workbook
creation in early 2026. This approach balances speed to market with
long-term architectural goals.

Sanyog Rai prepared account team role creation for deployment across all
tenants next week, completing a key piece of the engagement data model.
When a GTM user participates in an engagement linked to an account, the
system will now automatically create the relationship, enabling
downstream features like priority accounts and activity feeds. This
works today for customers with CRM connections and will extend to
non-CRM customers once account creation is complete.

Andres Perez advanced the custom field agent despite technical setbacks,
discovering that the Global Mapping API is the correct endpoint for
field creation rather than the GTM Store API directly. While environment
issues blocked final testing, this agent addresses real pain points as
more GTM Studio customers onboard---manually creating 10+ custom fields
through the UI is becoming unsustainable for the GTM Admin workflow.

### **Goals & Progress**

**GTM AI Context Service**: Prateek Paikray enabled Agentforce for demo
purposes and enhanced export logic to handle duplicate CRM records
intelligently. The system now updates the correct record based on
context---updating only the matched record when invoked from an
operations page, but updating the specific record when working from a
contact page. The Login team is exposing the Entitlement API externally,
which will enable verification that tenants have proper SKUs before
activating features.

**GTM Studio**: Andres Perez made progress on the custom field creation
agent, switching to the Global Mapping API approach after learning it
auto-copies field definitions to GTM Store with appropriate tagging for
downstream usage. While computer environment issues blocked completion
this week, the need continues to surface from app teams who require
easier field mapping configuration. Sanyog Rai is planning improvements
to user management and privacy controls for engagements, having drafted
requirements that need validation with dependent teams.

**Data Infrastructure**: Sanyog Rai confirmed that new GTM Store tables
require manual tickets to push data to BigQuery and verify
relationships---an unexpected discovery that affects development
velocity. The BigQuery sync runs once daily at 8 AM, meaning engagement
data isn\'t queryable in certain ways (sorts, filters) for up to 24
hours after being written to Bigtable, though direct key-value lookups
work in real-time. The team is meeting next week with Hanan\'s team to
establish efficient backfill processes for engagement data.

### **Strategic Challenges**

The ziUserId field has been broken in GTM Store since September 2nd
after an engineer accidentally changed its data type from number to
string. This blocked all updates to the field, but the issue went
undetected because it\'s a \"silent bug\"---no errors were thrown, just
missing data. The problem only surfaced when David Wheeler happened to
investigate while Andres was asking about GTM Store API usage for an
unrelated project. This reveals insufficient monitoring and controls
around production metadata changes, particularly the ability to change
data types on live attributes.

Chorus Data Share is consuming disproportionate time relative to its
remaining lifespan. Customer success teams are escalating questions from
high-ACV customers, but investigations reveal confusion between Chorus
data sharing and Chorus mapping issues. In one recent example, the
customer\'s actual problem was unlinked records (a mapping issue) rather
than data availability. Sanyog Rai is pushing back on requests for
additional documentation explaining use cases, noting that customers
demanded this capability but now require hand-holding on why they need
it. With the legacy Chorus share expected to sunset in 3-4 months once
Prateek\'s vertical datasets work completes, the team needs to time-box
support efforts appropriately.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Custom field creation should use the Global Mapping API rather than
direct GTM Store API calls, even though this seems counterintuitive. The
reason: Global Mapping API automatically tags fields with metadata about
appropriate usage contexts (workbooks, specific features), whereas
direct GTM Store creation requires manual tagging. This reflects the
current fragmented state where not all systems use GTM Store as the
source of truth, requiring workarounds to ensure proper field
classification. Andres suspects this isn\'t the end state but
acknowledges it\'s acceptable for now given system constraints.

The account AI summary scope exposed via partner apps supports both read
(GET) and \"ask a question\" (POST) capabilities, which wasn\'t
immediately obvious from documentation. This opens possibilities for
Agentforce to use natural language queries against account summaries
rather than parsing structured response sections. Prateek had been
extracting specific sections (like buying committee) from full
responses, but could instead ask targeted questions to retrieve that
information directly, reducing parsing complexity.

BigQuery access patterns create a 24-hour lag for certain engagement
data queries, which will impact customer experience. While Bigtable has
real-time data and supports direct key-value lookups, complex queries
requiring sorts or filters must wait for the daily 8 AM sync to
BigQuery. For use cases like \"who visited my website in the last 10
minutes,\" the data exists but isn\'t queryable in the expected way. The
team is investigating whether CDC (Change Data Capture) could enable
near-real-time BigQuery updates, particularly for high-volume streaming
data like website engagements.

### **Cross-Team Dependencies**

The Data Platform team requires manual coordination for each new GTM
Store namespace to ensure data flows to BigQuery with proper
relationships. This wasn\'t automatically happening, despite assumptions
that new tables would inherit existing pipelines. Each addition now
requires explicit tickets and verification, adding friction to
development velocity. The team needs the Data Platform group to automate
this process and increase sync frequency beyond daily updates.

The API and Login teams are collaborating on exposing the Entitlement
API externally, which will unblock not just Agentforce but other partner
app features requiring SKU verification. This work is expected to
complete this week, enabling Prateek to publish the updated Salesforce
package before the October 28th launch. The API team\'s willingness to
make this available for broader use beyond Agentforce demonstrates good
cross-team leverage.

## **Looking Ahead**

Next week\'s primary focus is advancing vertical datasets to
production-ready state while establishing operational foundations for
engagement data at scale. Prateek Paikray will work with engineering to
get dataset preview functionality operational in staging and complete
the opportunity history schema to unblock ROI team migrations to GTM.
He\'ll also create LRT tickets for Snowflake and Databricks data share
releases planned for November as early access features.

Sanyog Rai will deploy account team role creation across all tenants and
meet with Hanan\'s team to establish efficient backfill processes---a
requirement as engagement data volumes reach hundreds of millions of
records. He\'ll continue validating GraphQL queries with downstream
teams like Workbooks while organizing admin portal updates for metrics,
configuration, and privacy improvements. For November\'s data cloud
shares, the team will mark Databricks as early access with full
documentation ready, positioning for GA in December once Liard completes
testing.

Andres Perez will continue custom field agent development in parallel
with other priorities, as the need persists from Ash and other Studio
implementation teams. Resolving environment configuration issues remains
the immediate blocker, followed by authentication troubleshooting for
the staging Global Mapping endpoint. While progress has been slower than
desired due to technical challenges, the agent represents meaningful
value for GTM Admins managing multiple customer onboardings.

*Source: Team 1-2-3 Operating Framework entries from October 13-17,
2025*
