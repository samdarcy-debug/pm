---
id: weekly-semantic-data-2025-39
title: "Semantic Data Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Semantic Data Team Executive Roundup - September 26, 2025**

## **Executive Summary**

The team identified significant gains that can be achieved with token
optimization for email processing, reducing costs by over 50% through
entity detection filtering with spaCy. However, achieving sub-hour data
latency for Copilot Workspace users remains blocked by DAG deployment
permissions and embedding generation speed. With actual users now
testing workflows in production, the 12-48 hour lag between meetings and
queryability is becoming a critical visibility issue that needs
resolution by end of October for early access rollout.

## **This Week\'s Progress**

### **Key Momentum Areas**

Jon Seller identified significant cost optimization for email
processing, implementing spaCy-based entity detection that reduces token
usage from 4,000+ to approximately 1,800 tokens per engagement while
maintaining data quality. This directly addresses scalability concerns
as we prepare for broader tenant onboarding.

Inga Isakov\'s comparative analysis of processing approaches revealed
that the iterative method doubles entity extraction (from 158 to 308
entities), though with notable duplication in persons and next steps
categories. This data provides the empirical foundation needed to
optimize our extraction pipeline.

Matt Kowalczyk successfully deployed Airflow infrastructure to staging
and production environments, establishing the orchestration layer
critical for achieving our latency targets. While permission blockers
remain, the infrastructure foundation is now in place.

### **Goals & Progress**

**Email Processing Optimization**: Jon\'s implementation of entity
detection filtering is complete and ready for production deployment. The
combination of signature cleaning, graph optimization, and spaCy
filtering creates a comprehensive cost reduction strategy that maintains
extraction quality while dramatically reducing computational overhead.

**Entity Extraction Validation**: Inga is midway through validating
entity extraction accuracy across both processing approaches. Initial
findings show the iterative approach captures significantly more
entities, though determining which entities provide actual value
requires completing the full 10-thread analysis.

**Orchestration Infrastructure**: Airflow deployment reached staging and
production environments, but remains blocked from operational use due to
DAG deployment permissions. Matt is actively engaging with DevOps to
resolve access restrictions that prevent the team from pushing DAG
updates without CICD integration.

### **Strategic Challenges**

The inability to deploy DAGs to staging and production environments
blocks our path to automated batch processing and orchestrated
pipelines. DevOps maintains a policy restricting human access to these
environments, but without CICD integration for Airflow, we have no
mechanism to deploy or update DAGs. Matt is pursuing exemptions or
alternative approaches with Jimmy from DevOps.

Embedding generation speed remains the primary bottleneck for achieving
sub-hour latency targets. Danny Pan confirmed that while processing
ZoomInfo tenant alone could meet the one-hour target, expanding to all
tenants pushes beyond that threshold without batch optimization. This
creates a fundamental tension between our event-driven architecture
goals and batch processing requirements.

The 12-48 hour lag between engagement completion and data queryability
is becoming increasingly visible as Copilot Workspace users attempt
real-world workflows. Rowan Bailey emphasized that reps preparing for
next-day meetings are finding the system lacks their most recent
engagement data, creating a poor user experience that will become
critical as we approach early access launch.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Entity detection with spaCy proves highly effective for filtering
low-value emails, though Jon\'s discovery that it primarily detects
person, org, and product entities suggests opportunity for enrichment
with additional entity types. The ability to discard contentless emails
like scheduling confirmations while preserving substantive communication
validates this preprocessing approach.

The architectural tension between batch processing efficiency and
event-driven responsiveness requires a tiered approach. Danny\'s insight
that batch processing works against event-driven pipelines led to
discussion of implementing both \"fast lane\" processing for priority
customers and batch processing for standard SLA customers, potentially
creating a differentiated pricing model.

GTM Store\'s existing API-to-Kafka infrastructure, confirmed by Danny to
be managed by Michael Kaufman, provides an unexpected acceleration path
for our output pipeline. Rather than building custom integration, we can
leverage their existing event streaming architecture once we complete
the schema translation layer.

### **Cross-Team Dependencies**

Our collaboration with the ZDP team on engagement data format remains
critical for achieving latency targets. While Jeffrey is adapting to our
required Conversations V1 endpoint format, we await sample data to
confirm compatibility before proceeding with integration.

The DevOps team\'s infrastructure policies are creating friction with
our operational needs. Without temporary exemptions for DAG deployment
or expedited CICD integration, our ability to iterate on orchestration
workflows remains severely constrained, potentially pushing our latency
improvements into November rather than October.

## **Looking Ahead**

Next week\'s primary focus centers on unblocking orchestration
capabilities and implementing batch embeddings to accelerate processing
throughput. Matt will escalate the DAG deployment permissions issue with
DevOps while Danny completes the batch embeddings PR and begins
integration with the now-available Airflow infrastructure on dev.

The team will initiate schema translation work for GTM Store
integration, with Jon coordinating with Michael Kaufman once the
translation layer design is complete. This parallel track ensures we can
immediately leverage the Kafka pipeline once embeddings generation is
optimized.

Success next week means having orchestration operational on dev with
batch embeddings running through Airflow DAGs, while also establishing a
clear path forward on permissions that doesn\'t require waiting for full
CICD implementation. The team\'s ability to deliver sub-hour latency for
early access customers depends on resolving these foundational blockers
within the next two weeks.

*Source: Team 1-2-3 Operating Framework entries from September 20-26,
2025*
