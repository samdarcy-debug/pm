---
id: weekly-data-2025-35
title: "Data Weekly Report - August 29, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-08-29
updated: 2026-01-06
week_ending: 2025-08-29
reporting_period: "August 25-29, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Core Data Executive Roundup - Week of 08/25-08/29**

## **Executive Summary**

Rituparna Das pushed 1 million new title classifications into
production. Simultaneously, our agent capabilities continue to progress
with Heather advancing Contributory Network driven agents and
prototyping a Benchmark Agent, while the team collaborates with
cross-team stakeholders to finalize the architecture design for CN data
to scale up new CN powered use cases for eligible customers. Jody
created an Org Chart agent prototype and drove the Data Insights Agent
to production for internal users. Peter Overman\'s investigation into
orphaned company profiles revealed an extraordinary URL opportunity -
38M websites with extracted company names from legacy crawlers and 61M
with URLs potentially identifying more opportunity for new companies,
with crawling planned already for immediate sampling.

## **This Week\'s Progress**

### **Key Momentum Areas**

Peter\'s systematic investigation delivered actionable results with 99
million total URLs identified: 38 million where legacy crawlers already
extracted company names and 61 million awaiting processing. With
crawling tickets ZD-61832 and AD-61835 deployed and analysis ticket
DEN-4045 scheduled for next week to assess match rates and yield
estimates, even a conservative 1% success rate would deliver nearly one
million net new companies for Cam\'s Q4 coverage targets.

The agent ecosystem achieved multiple breakthroughs across the team.
Jody drove the Data Insights Agent to production for internal
traceability API access while prototyping the Org Chart agent with
BigQuery connectivity. Heather advanced Contributory Network driven
agents and developed a Benchmark Agent prototype. Meanwhile, Cam
confirmed that Snowflake integration and scheduling capabilities will
arrive within two weeks, positioning the team to leverage these new
tools.

Rituparna\'s title classification deployment marks a major data quality
milestone, with the new database architecture processing 1 million
classifications while the team initiated weekend reprocessing for
associated contact IDs. The upcoming 5TB HEM-MAID migration from
Snowflake to BigQuery will identify common entities between our two
largest data sources, potentially unlocking millions more classified
roles pending FinOps cost approval.

### **Goals & Progress**

**Data Asset Expansion**: Peter completed the first draft schema for
Xverum LinkedIn company profiles with historical employee count samples
received for review, finalized H2 Data Pipelines roadmap materials for
Friday\'s session with leadership, and completed parking domain analysis
with research.

**Agent Development:** Reviewed and documented the available paths for
agent availability. Data team will follow-up with a working session with
the agent team to ensure proper understanding of established
architectural paradigms to help improve velocity. The team is
collaborating with cross-team stakeholders to finalize the architecture
design for CN data, with the goal to scale up new CN powered use cases
for the right eligible customers fast. Heather\'s work on Contributory
Network base ZI Chat agent addresses growing questions about data
ingestion status, while the upcoming chat agent will provide
self-service answers previously requiring PM intervention.

**Platform Modernization**: Cam achieved 50% progress documenting
Company 2.0 functionality despite zero existing DAP platform
documentation, requiring exhaustive knowledge transfer with Anatoly\'s
team. Magnus secured engineering manager and architect for shared
services with concrete demand from IBM, ServiceNow, and Workday, though
individual contributors remain unassigned and Michael Governale\'s
unexpected absence impacts timelines.

### **Strategic Challenges**

Legal\'s two-week negotiation standoff with Heather over AI data usage
permissions blocks the entire data sharing page revamp and downstream
agent deployment. Legal insists on narrow, case-specific permissions
while our competitive position requires broader umbrella coverage for
rapid iteration. Heather\'s escalation document to Brandon and Dominic
seeks executive intervention as Salesforce\'s mid-September flag
delivery approaches.

Resource constraints create cascading delays across initiatives. Hayden
sits at 25% progress on transparency API metrics Brandon expects
completed, blocked by Sam\'s unavailability and the Analysis team losing
permanent headcount. Will explore alternatives like using Ivan\'s
context generation model and Jody\'s LLM-based git repo analysis.

The Company 2.0 documentation crisis threatens M8 launch timing and our
ability to capitalize on Peter\'s URL discovery. Cam reports extreme
difficulty securing time with Anatoly\'s team, with every feature
requiring human explanation of undocumented functionality. Without clear
go/no-go criteria for feature continuity, we risk either delaying launch
or breaking critical customer workflows.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Peter\'s observation that we lack forensic capabilities for AI failures
represents a strategic blind spot beyond debugging. His proposed
sub-agent to log conversation metrics would reveal fill rates by query
type, identify critical metadata gaps, and map failure patterns to
customer segments. Without this observability, we\'re optimizing blind
while competitors could leapfrog us by better understanding their
performance gaps.

The agent platform\'s evolution revealed unexpected monetization
complexity requiring fundamental business model rethinking. John\'s
analysis of Global\'s technographics exposed our lack of systematic
coverage understanding - we\'ve accumulated features organically over
time without clear segmentation of which customer demographics we serve
well versus poorly. This prevents strategic data acquisition and leaves
us vulnerable to competitors who can target our weakest segments with
precision.

### **Cross-Team Dependencies**

Rachel\'s involvement analyzing address normalization across PII,
Company, and web data acquisition establishes a new collaboration model
for identifying best practices rather than duplicating efforts. Her
findings determine whether PII\'s existing API becomes the foundation or
requires ground-up development, directly impacting Magnus\'s 60-day
Company 3.0 support timeline.

The chat bot team\'s roadmap directly enables our agent strategy, with
scheduling capabilities and Snowflake integration arriving within two
weeks per Cam\'s morning discussion. Initial user-permission-based
database access provides immediate value while service roles develop,
though this creates security considerations for customer-facing
deployments.

The internal Salesforce team\'s mid-September account-level AI flag
remains a hard dependency for Heather\'s data sharing initiatives after
two months of delays.

## **Looking Ahead**

Peter will execute the phased URL analysis plan: analyzing 100K samples
of each cohort to measure match rates and projected yield (net new
company profiles, existing company attribute additions). In parallel,
Peter will review the [[parked domain
analysis]{.underline}](https://docs.google.com/document/d/1EkfTLtfOuXynUhbPOY8e_vTBiJsW_eAi-XldpisK0RM/edit?usp=sharing)
with relevant teams to decide treatment for the \~5MM estimated company
profiles with inactive websites.

Agent development accelerates with Jody cataloging all initiatives to
prevent duplication while building shared services agent prototypes. The
imminent Snowflake integration enables automated daily reports like
\"trending companies\" or \"coverage gap analysis\" - transforming
multi-week engineering projects into morning Slack messages. Heather\'s
Contributory Network and Benchmark agents will demonstrate customer
value while building the case for dedicated agent resources.

Critical decisions require resolution: Cam needs Company 2.0 feature
continuity framework finalized, Heather requires legal breakthrough for
agent deployment. Combined with Peter\'s URL recovery projections and
Rituparna\'s HEM-MAID migration timeline, these decisions determine
whether we achieve aggressive Q4 targets or require immediate
expectation management with market and leadership.

*Source: Core Data Team Operating Framework entries from 08/25-08/29*
