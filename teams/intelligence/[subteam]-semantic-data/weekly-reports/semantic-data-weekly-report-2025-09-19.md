---
id: weekly-semantic-data-2025-38
title: "Semantic Data Weekly Report - September 19, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-09-19
updated: 2026-01-06
week_ending: 2025-09-19
reporting_period: "September 15-19, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Semantic Data Team Executive Roundup - September 19, 2025**

## **Executive Summary**

Jon discovered and fixed a critical bug causing 6x LLM overcalling in
email processing, immediately reducing token costs from 20,000+ to
expected ranges. With authentication PRs landing next week, the pipeline
achieves production-ready cost attribution per tenant. Meanwhile, sales
adoption of semantic data in workbooks drove Rowan to push for batch
processing implementation---a strategic move that delivers 50% cost
reduction while enabling ZoomInfo to expand historical data coverage
from 6 months to 1 year for all prospects and customers.

## **This Week\'s Progress**

### **Key Momentum Areas**

Jon\'s cost optimization breakthrough emerged from a systematic test
script processing 10,000 email threads with Inga, revealing not just
accurate pricing but two core concurrency bugs in the ETL pipeline. The
fragment handling bug alone was inflating costs by 600% through
redundant LLM calls, now fixed with fast, accurate ingestion restored.
This positions the team to deliver production-grade cost tracking within
days.

Matt\'s Airflow implementation reached deployment readiness after
performance validation confirmed suitability for expected tenant scale.
The DAG architecture for incremental and backfill processing creates the
foundation for automated data pipelines, with SBX deployment targeted
for next week pending DevOps coordination on the dev environment setup.

Rowan\'s strategic pivot redirected Inga from G2 reviews to earnings
call transcripts after analysis revealed reviews average under 100 words
versus earnings calls\' 15-30 minutes of dense strategic content. This
shift aligns perfectly with the pipeline\'s semantic compression
strengths while addressing the 2,000-word account brief payloads
currently overwhelming context windows in production.

### **Goals & Progress**

**Cost Infrastructure**: Jon achieved complete cost transparency for
email and meeting processing through the test harness, fixing the 6x
overcalling bug that was masking true operational costs. The three
remaining authentication PRs will enable per-tenant cost attribution,
completing the commercial viability requirements. With embeddings
integration as the final piece, full pipeline cost tracking arrives next
week.

**Orchestration Platform**: Matt progressed Airflow from architecture
design through performance validation to DAG implementation in a single
sprint. Following productive discussions with Danny on tenant scaling
requirements, the team confirmed Airflow\'s capability to handle
projected growth. The platform now awaits DevOps deployment to begin
automating the currently manual ingestion workflows.

**Data Quality & Sources**: Inga completed thread processing
calculations while developing ontology-based prompts for structured data
extraction. The pivot from G2 reviews to earnings calls represents a
200x increase in processable content per record, directly addressing the
semantic compression use case. Initial methodology for earnings call
analysis launches immediately.

### **Strategic Challenges**

DevOps deployment delays for Airflow in dev environment risk pushing
back automation timeline, though Matt\'s proactive escalation through
Danny and potential direct engagement should resolve within days. The
team needs clarity on deployment schedule to maintain momentum toward
automated tenant onboarding at scale.

GTM store identifier complexity blocks Danny\'s progress on unifying
multiple record IDs into single system-of-record entities. While
requiring only an hour of focused analysis to resolve, this
architectural decision impacts downstream data flow and needs immediate
attention to prevent cascading delays.

Batch processing absence forces ZoomInfo to pay full price for semantic
data processing even as sales teams dramatically increase usage through
workbooks and workspaces. With initial tenant ingestion requiring 6+
months of historical data and ongoing processing accumulating rapidly,
the 50% cost savings from batch mode transitions from nice-to-have to
critical requirement.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The fragment handling bug discovery revealed how architectural
assumptions about LLM calling patterns can exponentially inflate
costs---Jon\'s fix dropping token usage from 20,000 to expected ranges
proves the value of systematic cost analysis. This finding likely
impacts other teams building LLM pipelines who may have similar
multiplicative inefficiencies hiding in their code.

Earnings calls emerged as the optimal initial data source for semantic
compression after Inga and Rowan\'s analysis showed G2 reviews\' sub-100
word format defeats the pipeline\'s purpose. The 200x content density
difference validates focusing engineering effort on sources that
actually require semantic compression rather than forcing all data types
through the same pipeline.

Sales team adoption patterns from Henry and other executives querying
their upcoming meetings revealed immediate product-market fit for
semantic-powered meeting preparation. Rowan\'s demo showing calendar
integration with historical interaction analysis proves the pipeline
delivers tangible business value beyond theoretical
capabilities---though privacy considerations around executive email
access require careful governance.

### **Cross-Team Dependencies**

Our integration with DevOps for Airflow deployment requires escalation
to maintain next week\'s automation timeline. Matt\'s coordination
through semantic-dev DevOps channel, potentially with Rowan\'s support,
aims to unlock the blocker preventing DAG deployment in development
environment.

The authentication implementation crossing Jon\'s pipeline work with
platform identity services reaches completion through three remaining
PRs, enabling the critical capability to attribute costs per tenant
rather than globally to ZoomInfo. This unlocks commercial viability for
external customer billing through AI credits.

## **Looking Ahead**

Authentication completion next week transforms the pipeline from
internal tool to commercial product, with per-tenant cost attribution
enabling AI credit billing models. Jon\'s three PRs represent the final
technical barrier to production readiness.

Batch processing implementation becomes the team\'s next major focus,
offering 50% cost reduction while enabling expanded historical coverage
from 6 to 12 months. With Danny and Jon\'s February groundwork plus
Matt\'s Airflow orchestration, the technical path is clear---execution
determines whether ZoomInfo can afford to scale semantic data across its
customer base. Inga\'s earnings call methodology will prove the
pipeline\'s value on high-density content while the team builds toward
the Q4 target of automated multi-tenant operations at scale.

*Source: Team 1-2-3 Operating Framework entries from September 16-19,
2025*
