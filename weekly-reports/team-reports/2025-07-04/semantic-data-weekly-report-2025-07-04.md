---
id: weekly-semantic-data-2025-27
title: "Semantic Data Weekly Report - July 04, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-07-04
updated: 2026-01-06
week_ending: 2025-07-04
reporting_period: "June 30-July 04, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Semantic Data Team Executive Roundup - June 30th - July 3rd 2025**

## **Executive Summary**

The Semantic Data Team successfully addressed critical data quality
issues while advancing key integration capabilities for the early access
program. We uncovered and fixed a deep attribution bug that could have
forced costly reruns at scale - catching this now saves significant
future technical debt. Most importantly, we\'ve secured ownership for
our evaluation framework through the agentic platform team, unblocking
our ability to measure and improve retrieval quality. With early access
customers already using GTM Studio, our immediate focus is enabling
multi-tenant support and completing the workbooks integration to deliver
the full semantic data experience.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Data Quality Breakthrough**: Jon Seller identified and fixed a
critical bug in meeting/person attribution that was causing data
variance issues. This proactive discovery prevents what could have been
catastrophic at scale - imagine having to rerun thousands of engagements
across multiple tenants. Jon\'s implementing comprehensive integration
tests to ensure this class of bugs never resurfaces.

**Enhanced Entity Extraction**: Inga Isakov\'s evaluation of iterative
email processing revealed we can capture 10-15% more entities compared
to processing entire threads at once. This finding directly improves the
richness of insights we can provide to sales teams, ensuring we don\'t
miss critical pain points or requirements mentioned across long email
threads.

**Evaluation Framework Secured**: Rowan Bailey successfully transitioned
ownership of the evaluation framework to Christian Pecora and the
agentic platform team. This critical handoff means we\'re no longer
flying blind on retrieval quality - Christian already has concrete ideas
for building a zero-to-one evaluation framework for our query
decomposition and re-ranking capabilities.

### **Goals & Progress**

**Entity Generation Testing** (Inga Isakov): Successfully evaluated 3
email thread samples comparing iterative vs. full-thread processing.
Initial results show 10-15% improvement in entity capture with iterative
approach. Currently at 60% complete with prompt refinements underway to
prevent duplicate entities and improve extraction quality.

**Search Agent Development** (Josh Mantovani): Built initial shallow
search service for the agentic platform using Brave API. Core
functionality complete but deployment blocked by procurement delays for
API key. Pivoted to exploring agent reasoning strategies that will be
critical for deep research capabilities. 70% complete pending API
access.

**Production Data Pipeline** (Jon Seller): Fixed critical attribution
bug and implementing integration tests to prevent recurrence. Ready to
process high-ACV account list (100k+ accounts) once testing completes.
Multi-tenant support implementation queued for next week. 40% complete
with significant progress on quality assurance.

### **Strategic Challenges**

**Multi-Tenant Architecture Gap**: Josh Mantovani identified that our
current internal tenant ID system won\'t work for external consumers.
Before we can scale to multiple early access customers, we need to
implement support for Zoom Info tenant IDs. This blocks our ability to
serve workbooks and other consumers who won\'t have access to our
internal ID mapping.

**ZDP Integration Missing**: We\'ve been processing data in GCP, but
workbooks needs it in ZDP (Zoom Data Platform). Josh highlighted that
even with automated pipeline triggers, we haven\'t built the connection
to transfer processed data where consumers need it. This creates a
manual bottleneck that will become unsustainable as we scale.

**Web Scraping Integration Delays**: Josh needs to leverage the web
scraping team\'s infrastructure for the search agent but hasn\'t
received responses from Andrew Harris. Given the massive scale of their
existing service, partnering with them could accelerate our deep
research capabilities significantly. Rowan will escalate to unblock this
cross-team collaboration.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Iterative Processing Superiority**: Inga\'s discovery that processing
emails iteratively captures 10-15% more entities fundamentally changes
our ingestion strategy. This isn\'t just about quantity - these
additional entities often represent nuanced pain points or requirements
that emerge through conversation flow, exactly the insights sales teams
need most.

**Early Bug Detection Saves Exponential Cost**: Jon\'s proactive bug
hunting revealed an attribution issue that would have multiplied in
impact with scale. At 10 tenants with thousands of engagements each, a
full data rerun would be technically and financially prohibitive. This
validates our strategy of being \"nimble while we can\" before scaling.

**Unified Evaluation Strategy Emerging**: The handoff to the agentic
platform team isn\'t just solving an ownership problem - it\'s creating
a unified approach to evaluating all agent capabilities. Christian\'s
vision for evaluating tool selection, query decomposition, and retrieval
quality will benefit the entire platform, not just semantic data.

### **Cross-Team Dependencies**

Our collaboration with the **Workbooks team** on API integration remains
critical but visibility is limited. We need confirmation on whether
they\'ll call our API in batch mode and their timeline for integration.
Without this coordination, early access customers won\'t experience the
full value of semantic data in their AI attributes.

The **Web Scraping team** has built infrastructure operating at
\"insane\" scale that could dramatically accelerate our search agent
capabilities. Despite their stated willingness to support (\"tell us
what you need\"), we\'re blocked on basic communication. Their existing
deep crawl capabilities could give us a significant competitive
advantage if we can establish the partnership.

## **Looking Ahead**

Next week\'s singular focus is unblocking multi-tenant support to serve
early access customers effectively. Jon will complete testing on
high-ACV accounts and implement Zoom Info tenant ID support, while Josh
builds the critical ZDP data transfer pipeline.

Inga will finalize the email processing evaluation and establish gold
standard benchmarks for our 10-15% improvement target. We\'ll also
solidify the workbooks integration plan with direct outreach to Tushar
to confirm batch processing requirements and timeline.

Most strategically, Rowan will frame our \"context engineering\"
vision - how we transform raw data into high-quality context for agent
consumption. This positioning will guide H2 planning and ensure we\'re
building not just a data service, but the semantic intelligence layer
that powers the entire GTM platform.

*Source: Team 1-2-3 Operating Framework entries from June 30 - July 3,
2025*
