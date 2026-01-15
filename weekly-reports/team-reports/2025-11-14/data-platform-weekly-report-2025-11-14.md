---
id: weekly-data-platform-2025-46
title: "GTM Data Platform Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Data Platform Team Executive Roundup - Week of November 10, 2025**

## **Executive Summary**

By obtaining cross-team alignment to maintain BigQuery alongside Solr
through the GraphQL API to support the Dec 1st developer workshop, Marc
Delurgio, Linda Johannessen, and Menna Rashwan preserved momentum with
the apps teams and de-risked the December 31st deadline to have GQL
ready for apps teams, while establishing a clear migration path to Solr
as feature parity develops. The scope expansion adding Engagement data
mid-stream to Solr created immediate delivery pressure, but the team's
agile approach will meet commitments while building toward the
Solr-based solution.

## **This Week\'s Progress**

### **Key Momentum Areas**

The team obtained critical stakeholder alignment that clarified the
backend architecture strategy for the GraphQL API. The decision to
maintain BigQuery for first-party queries while using Solr for
cross-entity searches and traditional search operations removes a major
feasibility concern for the December 1st developer workshop. This
architectural flexibility means app developers can begin GraphQL
integration by December 1st using proven infrastructure while the team
continues building out Solr-based capabilities in parallel.

Menna Rashwan revised the Enterprise Search milestone plan to
incorporate Engagement data into the December 31st scope. While the team
identified that content interactions will likely miss the deadline due
to complexity, she established clear priorities with Linda\'s help:
ensuring existing CRM data works through Federated Search takes
precedence over new datasets, followed by engagement data for the core
workbooks use cases. The team is actively evaluating technical paths and
will scope down use cases based on feasibility assessments currently
underway.

### **Goals & Progress**

**Federated Search Integration**: The Search team developed a
comprehensive plan for bringing Engagement data into Solr with UUID
generation strategies and is evaluating approaches for deep object
traversals and aggregations. Menna Rashwan\'s team is working through
whether to implement real-time aggregations versus pre-aggregated data
patterns. The decision to use a shim based on the current Solr typespec
allows the team to meet delivery commitments, though this creates known
future rework once new Company and Contact schemas are finalized. Linda
Johannessen is coordinating closely with Menna\'s team on prioritizing
workbooks use cases and ensuring the required data is ready.

**Location Matching**: Moshik Levin completed the first draft of the
Regional HQ product brief and is preparing it for engineering review
next week. The team discovered that the existing \"domestic HQ\" flag in
company data doesn\'t reliably represent what customers need for
regional main office identification, particularly around mergers and
acquisitions. Moshik is scheduling a meeting with Marc Delurgio, Ethan,
and Cam to evaluate whether to fix the existing field or introduce a new
one, as adding yet another field could create customer confusion.

### **Strategic Challenges**

The mid-stream addition of Engagement data to the December 31st scope
created immediate planning pressure. While Menna Rashwan\'s team has
identified the high-level work chunks, significant evaluation remains
around data complexity and technical implementation paths. The team is
working through use case prioritization with limited time to finalize
decisions. Content interactions emerged as particularly challenging and
will likely be deferred past December, requiring stakeholder
communication about scope boundaries.

Schema alignment for Company and Contact data revealed more complexity
than initially expected. The decision to proceed with a shim-based
workaround using existing Solr fields enables the December 31st delivery
but creates known technical debt. Once Linda Johannessen and the data
producers finalize new schemas, there\'s risk of breaking changes that
require fundamental rework in how Federated Search integrates with
GraphQL. The team is scheduling data producer workshops to accelerate
schema finalization and minimize future disruption.

Cross-team coordination remains intensive with dependencies spanning
multiple engineering teams. The Enterprise Search work requires tight
synchronization between Menna\'s team and Linda\'s team on use case
definitions, schema specifications, and technical implementation
details. Upcoming meetings including a PII review for engagement data
and workbooks will help clarify priorities, though the compressed
timeline leaves little room for discovering additional complexity.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team learned that architectural flexibility provides more delivery
certainty than attempting perfect solutions under time pressure. The
multi-backend approach initially seemed like compromising on the
long-term vision, but Philip\'s support for using BigQuery where it
works well while building out Solr capabilities in parallel actually
accelerates both near-term delivery and long-term migration. This
pragmatic stance acknowledges current reality while maintaining
strategic direction.

Linda Johannessen\'s noted that the performance bottleneck isn\'t
BigQuery versus Solr for data access---it\'s the network transfer of
millions of IDs between systems. A query joining first and third-party
data took two to three seconds regardless of which platform hosted the
data. This finding validates the Federated Search strategy of keeping
third-party data in Solr to avoid expensive wire transfers, while
allowing first-party queries to use whichever backend performs best for
the specific use case.

### **Cross-Team Dependencies**

Work with the Search team on Federated Search integration continues to
be essential for enabling Workbooks to scale efficiently. Menna
Rashwan\'s team is actively engaged on the Engagement data pipeline and
UUID generation approach. The team is evaluating deep traversal patterns
and aggregation strategies that will determine query performance
characteristics. Linda Johannessen is working closely with Menna\'s team
to ensure prioritized use cases and required datasets are ready for
Workbooks to begin integration in January.

## **Looking Ahead**

Next week centers on finalizing Engagement data scope and completing
schema alignment work. Menna Rashwan will participate in the engagement
review with Randy and the workbooks team to understand detailed
requirements and establish use case priorities. This clarity is
essential for the team to determine what can realistically be delivered
by December 31st and what needs to be scoped out or phased.

Moshik Levin will kick off engineering work on the Regional HQ proof of
concept, with the product brief ready for team review. The meeting with
Marc Delurgio, Ethan, and Cam will determine whether to improve the
existing domestic HQ flag or introduce new fields, directly impacting
the technical approach. Marc Delurgio continues managing the unified
profile hiring pipeline with additional candidate interviews and case
study presentations scheduled. Linda Johannessen will continue working
with data producers on schema finalization and coordinating with
Menna\'s team on Federated Search integration priorities to keep both
Workspaces and Workbooks tracks moving forward.

*Source: Team 1-2-3 Operating Framework entries from week of November
10, 2025*
