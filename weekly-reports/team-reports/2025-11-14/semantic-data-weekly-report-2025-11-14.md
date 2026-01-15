---
id: weekly-semantic-data-2025-46
title: "Semantic Data Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Semantic Data Team Executive Roundup - November 14, 2025**

## **Executive Summary**

The team identified a significant data retrieval gap: approximately 8%
of processed accounts (2,000-2,500 of 35,000) lack ZoomInfo company IDs,
rendering their semantic data invisible to downstream consumers despite
successful processing. This stems from upstream Chorus ingestion issues
where transcripts arrive with Chorus IDs but without the corresponding
ZoomInfo company mappings. The team has documented the complete
debugging flow and is coordinating with the Chorus team to resolve the
ID resolution pipeline. Concurrently, Jon is automating quality
validation scripts to prevent similar issues from surfacing late, while
Jun\'s onboarding accelerates the team\'s capacity for parallel
investigation work.

## **This Week\'s Progress**

### **Key Momentum Areas**

Jon advanced pipeline observability by documenting and preparing to
automate the quality validation scripts that currently run manually.
These scripts check person-fragment matching, engagement completeness,
and semantic data readiness across accounts. Moving them into Airflow
will provide continuous visibility into data quality rather than
point-in-time manual checks.

Rowan constructed a quick flow mapping the complete path from Chorus
recording to semantic data retrieval, establishing a systematic
framework for debugging customer "semantic coverage" issues. The
flowchart identifies five distinct failure modes: missing source data,
processing errors, 90-day lookback boundaries, ID type mismatches, and
the newly discovered ZoomInfo company ID gaps.

Jun\'s environment setup accelerated through streamlined Docker
container deployment. Jon resolved the historical Zscaler connectivity
barriers, enabling full local development without AWS SSH workarounds.
The team can now onboard new members in hours rather than days, with Jun
positioned to contribute to testing and validation work immediately.

### **Goals & Progress**

**Quality Metrics & Validation Infrastructure**: Jon has developed
validation scripts that verify ontology compliance, relationship
deduplication, and entity completeness at extraction time. The LLM
validation layer logs warnings when extraction fails ontology
constraints, ensuring only conformant data reaches the graph. The
immediate focus shifts to automating these validations in Airflow for
continuous monitoring rather than reactive investigation.

**ID Resolution & Data Accessibility**: The team discovered that 8% of
accounts with processed semantic data cannot be retrieved by the agent
because Chorus ingestion doesn\'t populate ZoomInfo company IDs.
Investigation revealed these accounts have valid Chorus IDs and
Salesforce IDs but lack the primary identifier used by Copilot,
workbooks, and other downstream consumers. This requires coordination
with the Chorus team to understand their company ID resolution process.

**Team Capability & Development Velocity**: The local development
environment now supports full pipeline testing through Docker containers
with MyPi, code formatting, and database hooks. Team members can
validate specific engagements and recordings locally before PR
deployment. Inga is testing pipeline errors directly, while Jun received
environment variables and access keys to begin API testing and fragment
analysis.

### **Strategic Challenges**

The ZoomInfo company ID gap affects data discoverability in a way
that\'s invisible to standard pipeline monitoring. Customers can see
engagements in Chorus but receive empty responses from the semantic data
agent, creating confusion about system functionality. Root cause
analysis points to the Chorus-side ingestion process, where Salesforce
account IDs should consistently map to ZoomInfo company IDs but don\'t.
Venkata questioned whether processing transcripts without company IDs
serves any purpose if the data becomes unretrievable, highlighting the
need for upstream validation before processing resources are consumed.

Debugging complexity multiplies when failures can occur at five distinct
stages, each requiring different diagnostic approaches. The team lacks a
unified view of where accounts sit in the processing pipeline, making it
difficult to quickly answer whether an account has processable data,
whether processing succeeded, and whether extraction met quality
thresholds. The accounts endpoint enhancement will address this by
surfacing semantic data readiness status directly, but coordinating this
visibility across teams remains a gap.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team validated that quality controls exist at the right
architectural layer---LLM extraction output gets validated against the
ontology before any storage occurs, with non-conformant entities and
relationships logged but not persisted. This prevents garbage data from
polluting the graph, though it doesn\'t solve the upstream ID resolution
problem. The validation scripts Jon maintains already check engagement
completeness and person-fragment matching; automating them will shift
the team from reactive investigation to proactive quality monitoring.

The 90-day lookback window creates a class of \"false negative\"
scenarios where customers query accounts with legitimate engagements
that predate the processing window. This isn\'t a bug but a design
constraint that needs better communication to downstream consumers.
Combined with the ID resolution issues, customers face two distinct
reasons for \"no data found\" responses that appear identical on the
surface but require completely different remediation paths.

Local development capability emerged as a force multiplier for team
productivity. The six-month period when Jon worked exclusively through
AWS SSH highlighted how infrastructure friction compounds across a team.
Now that Zscaler connectivity works and Docker containers standardize
the setup, new team members can validate changes locally within their
first day, reducing iteration cycles and preventing environment-specific
surprises in production.

### **Cross-Team Dependencies**

Our work with the Chorus team on ZoomInfo company ID resolution
determines whether the 2,500 accounts with missing IDs become accessible
or require reprocessing. The ingestion pipeline should consistently map
Salesforce account IDs to ZoomInfo company IDs, but the current 8%
failure rate suggests either gaps in Chorus\'s enrichment logic or data
quality issues in their source systems. We need their team to
investigate why certain accounts arrive with Chorus IDs and Salesforce
IDs but no ZoomInfo company ID, and whether backfilling is possible
without full reprocessing.

The Workbooks team depends on clear error messaging when semantic data
queries fail. Currently they see empty results without context about
whether the account lacks engagements entirely, has engagements outside
the 90-day window, or has been processed but can\'t be retrieved due to
ID mismatches. Enhanced status endpoints will help, but this requires
alignment on what information Workbooks needs to handle these scenarios
gracefully in their user experience.

## **Looking Ahead**

The immediate priority centers on making data quality and processing
status transparent rather than opaque. Jon will move quality validation
scripts into Airflow for continuous monitoring, providing baseline
metrics on fill rates, relationship quality, and processing success
rates across tenants. This transforms quality from \"something we check
when there\'s a problem\" to \"something we track continuously.\"

Resolving the ZoomInfo company ID gap requires coordination with Chorus
to understand their enrichment process and determine whether backfilling
is feasible. If backfilling isn\'t possible, we\'ll need to add
validation that prevents processing transcripts without company IDs,
since that data becomes effectively unusable by downstream consumers.
The investigation should complete next week so we can decide between
remediation strategies: reprocess with better ID mapping, build
alternative retrieval paths, or implement upstream validation to stop
the problem at ingestion.

Jun\'s ramp continues with local testing of specific API endpoints and
fragment queries. As she builds familiarity with the codebase and
validation approaches, the team gains parallel investigation capacity
for the various edge cases surfacing in production. The Docker
environment and Inga\'s testing framework provide a clear path for her
to contribute to quality validation immediately while building deeper
system understanding.
