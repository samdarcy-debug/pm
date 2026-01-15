---
id: weekly-semantic-data-2025-36
title: "Semantic Data Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Semantic Data Team Executive Roundup - September 5, 2025**

## **Executive Summary**

The Semantic Data team achieved a breakthrough milestone with MCP
integration enabling Claude Desktop to directly query semantic data -
objections, pain points, requirements, and first-party engagements -
demonstrating end-to-end value realization of the platform. However, a
critical performance degradation has reduced ETL processing speed by 93%
(from 30 to 2 records per minute) without any code changes, requiring
immediate DevOps intervention to restore processing capacity for the
early access cohort.

## **This Week\'s Progress**

### **Key Momentum Areas**

**MCP Integration Success**: Rowan Bailey\'s team demonstrated live
Claude Desktop integration with semantic data APIs, allowing natural
language queries about customer objections, pain points, and engagement
history - transforming theoretical infrastructure work into tangible
business value. The proof of concept chains multiple API calls
seamlessly, first resolving company names through ZI search service then
retrieving semantic insights.

**Airflow Orchestration Design**: Matt Kowalczyk drove consensus on the
Airflow implementation strategy for multi-tenant automation, completing
architectural decisions that will provide observability into processing
pipelines and enable tenant-level configuration for features like
multi-pass analysis and source selection. The team aligned on a POC
deployment approach for sandbox testing next week.

**Database Performance Root Cause Analysis**: Jon Seller isolated the
performance issues to database connection handling rather than Anthropic
API limits, successfully implementing semaphore tuning that eliminates
connection errors even with 20 concurrent connections. The fix positions
the team to restore full processing capacity once the underlying
infrastructure issue is resolved.

### **Goals & Progress**

**ETL Processing Pipeline**: Danny Pan\'s team processed all upcoming
cohort additions despite severe performance constraints, with only the
early access cohort remaining. Processing continues at reduced speed (2
records/minute vs 30 previously) while the team investigates the sudden
degradation that occurred around Labor Day without code changes. Silver
Fort kickoff scheduled for next week requires cherry-picking demo
accounts due to suspiciously low engagement counts (max 8 calls per
account).

**Data Quality & Observability**: Jon Seller migrated critical data
quality queries into the API layer, enabling rapid account diagnostics
without direct database connections. This automation will streamline
cost analysis and budget validation for customer onboarding while
providing immediate visibility into engagement data completeness.

**Context Layer Enhancement**: Rowan Bailey identified critical gaps in
account and person brief generation that impact agent performance,
proposing ontology modifications to support new data sources including
earnings call transcripts and product reviews. The unified ontology
approach will maintain source-agnostic graph structure rather than
creating separate schemas per data type.

### **Strategic Challenges**

The 93% performance degradation in ETL processing emerged without code
changes around September 2nd, suggesting infrastructure-level issues
beyond application control. Jimmy from DevOps has been engaged for
today\'s team time to investigate database connection behavior
differences between local Postgres and Cloud SQL. The issue appears
\"pseudo-permanent\" as stopping and restarting processes doesn\'t
restore original performance levels.

Customer data quality concerns emerged with Silver Fort showing
remarkably low engagement counts (highest account has only 8 calls over
365 days, costing just \$250 to process). Rowan is investigating whether
this reflects actual usage patterns or integration/recording issues with
their Gong instance, critical to address before next week\'s customer
kickoff call.

Resource allocation tension exists between completing in-flight early
access cohort processing and preparing for continuous new tenant
additions like Silver Fort. The team is managing this through bite-sized
processing chunks that allow quick pivots when fixes become available,
though this approach limits throughput efficiency.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The MCP demonstration validated the entire semantic data architecture by
showing end-to-end value delivery - from database pooling discussions to
actual salesperson emulation answering strategic questions about
customer relationships. This positions ZoomInfo to leverage Anthropic\'s
ecosystem for rapid capability expansion without building custom
integrations for each channel like Slack.

Cloud SQL behaves fundamentally differently from local Postgres
connections in ways that weren\'t apparent during development. Grant\'s
insights about Python concurrency and Postgres query analyzer tools
proved essential for diagnosis, highlighting the need for
production-like testing environments earlier in the development cycle.

The promise of MCP extends beyond current implementation - the ability
to chain ZI search service for company resolution before semantic data
queries suggests future potential for processing Slack Connect channels
as a new unstructured data source, creating a virtuous cycle where each
integration enhances the semantic graph\'s completeness.

### **Cross-Team Dependencies**

Collaboration with the GTM Store team on GraphQL integration continues
for product review data access, with Inga requiring training on their
query patterns. Danny has a dedicated session scheduled today with their
team members to accelerate knowledge transfer and ensure smooth data
pipeline integration.

DevOps support from Jimmy and infrastructure insights from Grant are
critical for resolving the database performance crisis. The team needs
immediate assistance understanding Cloud SQL connection behavior and
potentially provisioning dedicated test instances with stable data sets
to prevent the kind of shared-resource conflicts currently suspected.

## **Looking Ahead**

Next week\'s focus centers on three critical paths: implementing the
Airflow POC in sandbox to validate orchestration assumptions, resolving
the database performance degradation to restore full processing
capacity, and preparing for the Silver Fort customer kickoff with
carefully selected demo accounts.

Priority one is working with DevOps to either fix the current Cloud SQL
performance issues or architect around them with connection pooling
improvements. Priority two is Matt\'s Airflow POC deployment which will
unlock true multi-tenant automation with per-customer configuration.
Priority three is Rowan\'s ontology revision to support new data sources
while maintaining graph coherence.

The team remains confident in delivering value despite infrastructure
challenges, with the MCP breakthrough demonstrating that the
foundational semantic data platform is ready for production workloads
once the operational issues are resolved.

*Source: Team 1-2-3 Operating Framework entries from September 2-6,
2025*
