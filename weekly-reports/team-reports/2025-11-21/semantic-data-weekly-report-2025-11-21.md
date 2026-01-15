---
id: weekly-semantic-data-2025-47
title: "Semantic Data Weekly Report - November 21, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-11-21
updated: 2026-01-06
week_ending: 2025-11-21
reporting_period: "November 17-21, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Semantic Data Team Executive Roundup - November 21, 2025**

## **Executive Summary**

The team reached a major milestone this week with the data ingestion job
successfully creating raw BigQuery tables from the GTM data store,
marking good progress of the first phase of the three-part semantic data
pipeline(ingestion). Jon Seller is now positioned to validate these
tables against current system outputs to ensure apples-to-apples
comparison before moving to the next stage. The accounts endpoint is
scheduled for release Monday, enabling QA and stakeholders to
self-service validate semantic data availability before querying.

**This Week\'s Progress**

### **Key Momentum Areas**

The data ingestion pipeline successfully completed its first major
phase, with the team extracting meetings, participants, participants
role,account and contacts table data from the GTM data store. Jon Seller
now needs validation against current system outputs to confirm data
point consistency. This foundation sets up the team to move forward with
entity extraction and embedding generation once validation completes.

Jun Wu advanced the embedding generation component by developing the
implementation using Vertex AI, which integrates seamlessly into the
three-part pipeline architecture. she confirmed the critical need to
maintain dimension consistency with the existing model and validated the
filtering logic for unprocessed fragments in the vector store. This work
positions the team to generate embeddings as soon as entity extraction
stabilizes.

Inga Isakov identified and is addressing a gap in company identification
by discovering missing ZI company IDs in the semantic data tables. She
has to develop a solution to backfill using Salesforce account IDs as a
bridge, which will resolve data completeness issues and enable proper
entity linking across systems. She\'s checking whether companies have
fragments in the database and will confirm findings to inform next
steps.

### **Goals & Progress**

**Data Pipeline Architecture**: The three-part pipeline is taking shape
with ingestion from GTM complete, entity extraction with relationships
in development, and embedding generation designed. Jon Seller is
reviewing the data flow codebase next week to validate all BigQuery SQL
queries and ensure they produce consistent outputs. Samuel Park is
focusing on the entity extraction data flow job using synchronous API
calls to move the middle layer forward.

**End-to-End Validation**: Jon Seller and Inga Isakov are preparing to
validate the complete data flow using sample ZoomInfo tenant data with
10 sample engagement recordings. This validation will confirm entity
accuracy across the pipeline and surface any issues before moving to
next stage. The team plans to connect Monday to review the data flow job
together if questions arise.

**Endpoint Development**: The accounts endpoint release Monday
represents a significant step toward stakeholder enablement, allowing QA
teams to validate semantic data availability for specific companies
before attempting queries. This self-service validation capability
addresses current requests from QA teams and reduces dependency on
engineering for data availability checks.

### **Strategic Challenges**

The team discovered that missing company IDs require a bridging strategy
using Salesforce data to maintain entity relationships. Inga Isakov is
implementing the solution by identifying missing ZI company IDs and
joining using SFDC IDs. While this adds complexity to the data flow, the
team has a clear path forward and expects to resolve this during
validation next week. The dependency on external ID mapping highlights
the importance of maintaining robust entity linking across systems.

CDC implementation timeline is compressed with Mike unavailable next
week, creating pressure to prioritize completion by Monday before moving
to production. The team recognized this constraint and is organizing
work to ensure the ingestion tables are validated and ready. This
represents a tight but achievable timeline given the current state of
the pipeline.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team uncovered a fundamental principle this week: relationships
between entities are not optional features but critical requirements for
semantic data ingestion from GTM datastore. This insight will reshape
how the team approaches data modeling and query design, ensuring
relationship information is preserved and accessible throughout the
pipeline.

The validation process revealed that comparing outputs requires careful
attention to ensure apples-to-apples comparisons between the new
pipeline and existing systems. Jon Seller recognized the need to
validate all BigQuery SQL queries systematically before moving forward.
This methodical approach will prevent downstream issues and build
confidence in the new data architecture.

### **Cross-Team Dependencies**

Our work with the QA team continues to be essential for validating
semantic data availability before wider deployment. The accounts
endpoint release addresses their immediate need for self-service data
validation for specific companies. This capability enables them to
verify data presence without engineering support, reducing friction and
accelerating their testing workflows. The team\'s responsiveness to QA
requirements demonstrates strong cross-functional collaboration.

## **Looking Ahead**

Next week focuses on validation and stabilization as the team moves from
building to verifying the complete data ingestion pipeline. With the
accounts endpoint launching Monday and CDC implementation targeted for
completion, the team is transitioning from construction to quality
assurance.

Jon Seller will lead validation of the ingestion tables against current
system outputs, ensuring data point consistency before production
deployment. Simultaneously, Jon and Inga Isakov will conduct end-to-end
pipeline validation using sample ZoomInfo tenant data with 10 sample
recordings to confirm entity accuracy. These parallel validation efforts
will surface any remaining data flow job data issues while building
confidence in the architecture. Samuel Park continues advancing the
extraction layer with synchronous API implementation, while Jun Wu
ensures embedding dimension consistency and filtering logic remain
aligned with existing models. The team plans to connect Monday to review
the data flow job collectively, enabling rapid problem-solving if
validation reveals unexpected issues.

*Source: Team 1-2-3 Operating Framework entries from November 17-21,
2025*
