---
id: weekly-semantic-data-2025-37
title: "Semantic Data Weekly Report - September 12, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-09-12
updated: 2026-01-06
week_ending: 2025-09-12
reporting_period: "September 8-12, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Semantic Data Team Executive Roundup - September 8-12, 2025**

## **Executive Summary**

Jon Seller delivered a breakthrough in cost accounting infrastructure,
enabling precise forecasting of tenant onboarding costs before pipeline
execution - transforming our ability to make data-driven pricing and
capacity decisions. The team achieved critical milestones in pipeline
efficiency with 4 major concurrency improvements merged and a clear path
to 32x batch processing optimization. However, the Airflow integration
hit a Python version compatibility issue (3.11 vs 3.12) that Matt
Kowalczyk is actively resolving, while data access dependencies continue
to impact evaluation workflows.

## **This Week\'s Progress**

### **Key Momentum Areas**

Jon Seller\'s cost accounting framework represents a fundamental shift
in operational visibility - we can now predict token usage and costs for
any tenant before onboarding, with accurate tracking showing 27,000
embedding requests processed successfully on Wednesday. This capability
directly enables sales conversations with concrete cost-per-tenant
metrics and prevents budget surprises during large-scale onboarding
initiatives.

The concurrency improvements Jon deployed through 4 major PRs are
already showing results in production, with the system successfully
handling batch requests at 32x load during staging tests. Danny Pan
confirmed performance metrics remain strong even under this increased
load, validating our architectural approach to scaling.

Rowan Bailey\'s work on tenant brief generation identified a critical
optimization opportunity - the team discovered they were using Gemini
Flash 2.0 instead of 2.5, potentially leaving significant cost savings
and quality improvements on the table. The shift to batch processing
will reduce API calls from 27,000 individual requests to approximately
844 batched calls.

### **Goals & Progress**

**Pipeline Infrastructure**: Matt Kowalczyk successfully ported the
application to Python 3.11 with minimal changes - only 2 files required
type definition updates and all dependencies remained compatible. The
Airflow integration is progressing despite the version mismatch, with a
clear path forward that maintains security compliance while enabling
workflow orchestration.

**Cost Optimization**: Jon Seller completed the full cost accounting
implementation, delivering capabilities for tenant-level cost tracking,
date-range analysis, and pre-onboarding estimates. The system now
provides token counts for embeddings and full cost visibility across all
pipeline runs, with accurate accounting replacing previous
\"eyeballing\" approaches.

**Data Enrichment**: Inga Isakov and Jon evaluated product review
processing workflows while navigating G2 data access challenges. Danny
Pan secured commitment from the ingestion team that ZDB tables will be
available by end of day, unblocking the product reviews filter
functionality that\'s been stalled.

### **Strategic Challenges**

The Python version incompatibility between Airflow (3.11) and our
application (3.12) requires either backporting our code or finding
alternative deployment strategies. Matt identified the risk of security
concerns from DevOps about downgrading versions, though initial testing
shows all current packages are compatible with 3.11. The team needs to
decide between backporting, containerization, or accepting version
differences.

G2 data accessibility remains blocked due to GraphQL ID requirements
with no discovery mechanism. While the ingestion team committed to
creating the necessary tables in ZDB by today, Inga\'s evaluation work
has been delayed for multiple days. This impacts our ability to
incorporate product review signals into enrichment pipelines.

Budget constraints for Anthropic API usage are forcing immediate
decisions about rate limits and token allocations. Danny Pan is working
with finance to establish three tiers of usage - current needs, scaling
requirements, and steady-state operations - but the complexity of
backfill versus ongoing processing makes accurate forecasting
challenging.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Jon Seller\'s insight about \"the difference between eyeballing numbers
and doing actual accounting\" proved transformative - implementing
proper cost tracking revealed our actual usage patterns differ
significantly from estimates. The ability to switch models in the
evaluation framework and immediately see cost implications enables
data-driven model selection rather than performance-only decisions.

The team discovered that email data is now available for 8,000 tenants
while transcript data lags behind, fundamentally shifting our onboarding
strategy. Danny Pan identified that we\'ll have more tenants with email
access than transcripts, making email enrichment our primary value
driver rather than a secondary feature.

Performance testing revealed our embedding generation scales linearly
with request volume but handles batch processing efficiently. The
Wednesday spike of 27,000 requests processed successfully without
degradation proves our architecture can handle enterprise-scale loads
when properly configured.

### **Cross-Team Dependencies**

Our work with the ingestion team on G2 data availability remains
critical for enrichment quality. The promised ZDB table creation by end
of today will unblock product review integration, but continued delays
risk pushing our evaluation timeline further.

Integration with the IngenTech platform for offloading React agents and
embeddings requires coordination on model selection contracts. Danny Pan
noted that while React agents can move easily, embedding generation
needs careful planning due to model dependencies.

## **Looking Ahead**

Next week\'s primary focus shifts to implementing the batch processing
optimization that will reduce API calls by 32x while maintaining
response quality. Rowan Bailey will diagram enrichment pipelines for
each brief section, incorporating web research and user input
touchpoints.

The team will finalize the Airflow deployment strategy after reviewing
security implications with DevOps, while Jon Seller extends the cost
forecasting system to handle pre-onboarding estimates using GTM store
data instead of Chorus APIs. With G2 data tables expected today, Inga
can complete the product review evaluation that\'s been blocked all
week.

Danny Pan\'s completion of the Anthropic budget proposal and data
transfer configuration will establish our operational boundaries for Q4,
enabling aggressive tenant onboarding within defined cost parameters
while maintaining system stability.

*Source: Team 1-2-3 Operating Framework entries from September 8-12,
2025*
