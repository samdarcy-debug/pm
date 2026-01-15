---
id: weekly-semantic-data-2025-41
title: "Semantic Data Weekly Report - October 10, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-10-10
updated: 2026-01-06
week_ending: 2025-10-10
reporting_period: "October 6-10, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Semantic Data Team Executive Roundup - October 10, 2025**

## **Executive Summary**

Danny Pan\'s team established a clear path from current 24-hour refresh
cycles to 1-hour turnaround by the end of next week through ZDP copy
append mode implementation. The infrastructure work positions the team
to begin GTM store ingestion next week while Jon Seller\'s entity
resolution correction script reaches deployment readiness. Resource
constraints emerged as a significant headwind, with Christian
unavailable for evaluation support and DevOps returning to secondary
support status, creating velocity risks that require immediate
attention.

## **This Week\'s Progress**

### **Key Momentum Areas**

Danny Pan completed the technical design for ZDP copy append mode
migration, conducting detailed planning sessions with Ilho to map the
configuration changes needed on their side. The approach eliminates
dependency on ZDP releases and requires only directory cleanup on the
team\'s end before testing in stage environment. Early next week should
see the 4-hour refresh capability live, with batch embeddings work
following immediately after to reach the 1-hour target by week\'s end.

Jon Seller advanced the fragmented people correction script to
deployment-ready status after intensive code review cycles that
addressed data integrity risks. The script now processes week-long
batches in 20 minutes and outputs comprehensive analysis data to Google
Drive for validation. This foundational work clears the path for
confident tenant ingestion and establishes the pattern for ongoing data
quality improvements.

Matt Kowalczyk shipped Airflow Slack notifications to the team channel,
providing real-time visibility into pipeline execution. The
infrastructure orchestration layer continues maturing with progress on
ZDP copy implementation, though BigQuery permissions remain blocked.
Matt discovered Airflow\'s native secrets management capability,
providing a workaround for the Google Secrets access limitation and
unblocking immediate development needs.

### **Goals & Progress**

**Data Pipeline Performance**: The append mode architecture provides the
foundation for real-time ingestion through Kafka queue integration.
Rather than waiting for complete dataset snapshots, records flow
directly into tables with merge scripts resolving updates every 30
minutes. This creates a brief window where duplicate records appear in
queries, but vector search operations remain unaffected. The team
continues evaluating which retrieval patterns can tolerate the temporary
duplication versus those requiring immediate consistency. The parallel
track on batch embeddings optimization will compound these improvements,
delivering the full 1-hour refresh capability that enables meaningful
real-time use cases.

**Model Evaluation Quality**: Inga Isakov processed 7 of 10 target calls
in the Sonnet 4.5 versus 3.7 comparison, establishing that both models
exhibit similar hallucination patterns and entity miss rates. The
evaluation methodology involves listening to full recordings and
comparing extracted entities against both transcript and audio content,
providing ground truth validation. Her analysis surfaced a systematic
issue where both models fail to capture account information and call
participants despite their presence in recordings, leading to her
recommendation to hard-code these critical entities rather than relying
on extraction. The team recognizes that manual evaluation of 10
recordings per model iteration creates an unsustainable bottleneck,
requiring development of automated evaluation infrastructure to maintain
iteration velocity as the system scales.

**Entity Resolution Foundation**: Jon Seller\'s correction script
matured through multiple review cycles that systematically addressed the
substantial risk of making incorrect merges that could cascade into
larger data quality problems. The validation approach uses historical
problematic accounts as test cases, proving the correction logic handles
edge cases appropriately. The script\'s output provides audit trails and
candidate analysis that enable ongoing refinement. With Danny Pan
identifying a straightforward path forward in their offline discussion,
the first-phase fragmented people fix should complete early next week,
unblocking the broader entity resolution roadmap while establishing
confidence in the correction methodology.

### **Strategic Challenges**

Resource allocation constraints emerged as a material blocker this week,
with explicit instruction not to engage Christian for evaluation support
while DevOps support reverted to secondary tier following Jimmy\'s
reassignment. The team\'s current staffing cannot sustain both
infrastructure migrations and the intensive evaluation work required for
model improvements, creating a forced prioritization that delays either
data quality initiatives or architectural advancement. Inga\'s manual
evaluation of individual recordings provides essential validation but
cannot scale to the iteration frequency needed for rapid model
refinement, particularly as the team expands beyond the current
10-recording sample size.

Matt Kowalczyk remains blocked on BigQuery permissions required for ZDP
copy operations, with DevOps response times extending development
cycles. While workarounds exist for some infrastructure needs---such as
Airflow\'s native secrets management replacing Google Secrets
access---the fundamental permissions for data access operations require
DevOps intervention. The team discovered that requesting Yasin directly
for secret injection bypasses some approval delays, though this tactical
solution doesn\'t address the broader permissions architecture that
continues creating friction across multiple workstreams.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The append mode architecture investigation revealed that GTM store\'s
BigQuery backend currently lacks vector search support because they\'re
routing all queries through GraphQL. This creates a potential
intermediate state where the team maintains dual write paths---pushing
data to both ZDB and GTM store---until GTM store can support vector
operations on their BigQuery instance. Danny Pan\'s analysis identified
that regardless of the final GTM store integration approach, the team
will require vector search capabilities in BigQuery for the foreseeable
future, making the append mode optimization valuable independent of the
broader architectural evolution.

Inga\'s systematic evaluation process exposed that entity extraction
failures often occur for the most fundamental data elements---the
companies and people actually participating in conversations. Both
Sonnet 4.5 and 3.7 models miss these entities with surprising frequency
despite their explicit presence in transcripts and audio. This pattern
suggests that additional prompt engineering or structural changes to how
participant metadata flows into the extraction process could yield more
significant quality improvements than model version upgrades. The
recommendation to hard-code account and participant information
acknowledges that some context shouldn\'t require extraction at all,
particularly when it\'s available as structured metadata from the source
systems.

Matt\'s investigation into secrets management revealed organizational
infrastructure patterns that aren\'t immediately obvious---ZDP Airflow
uses Google Secrets despite the team lacking direct access, DevOps
directs teams toward Keyless integration without addressing the
authentication bootstrap problem, and Airflow contains native
capabilities that duplicate external services. These discoveries
highlight the importance of exploring platform features thoroughly
before introducing additional integration points, as the team often has
more capability at hand than the recommended workflow patterns suggest.

### **Cross-Team Dependencies**

The team\'s work with GTM store engineering on schema finalization and
append mode configuration creates a critical dependency for achieving
the targeted refresh performance. Ilho\'s responsiveness this week
enabled rapid progress on the technical design, and the configuration
change coordination scheduled for early next week will determine whether
the 4-hour refresh target ships on schedule. Jon received the GraphQL
documentation needed to begin GTM store ingestion implementation,
removing the information blocker that previously prevented starting this
architectural shift.

DevOps relationships require strengthening given the team\'s increased
infrastructure needs. The secondary support tier status creates
unpredictable delays on permissions, deployments, and configuration
changes that compound across multiple team members\' work. While
tactical workarounds like direct Yasin engagement for specific requests
provide temporary relief, the team needs restored primary support tier
access to maintain the velocity required for their current roadmap
commitments.

## **Looking Ahead**

Next week represents a pivotal shift from infrastructure preparation to
production deployment, with three parallel tracks advancing
simultaneously. Danny Pan will push the append mode implementation
through stage testing and into production, delivering the 4-hour refresh
capability while immediately beginning batch embeddings optimization
work to reach the 1-hour target. Jon Seller transitions from entity
resolution cleanup to GTM store ingestion implementation now that he has
the necessary GraphQL documentation, establishing the foundation for
deprecating Chorus API dependencies.

The team welcomes Sai to the roster with an onboarding session scheduled
before Monday\'s kickoff call. Rowan will provide historical context and
current state overview to accelerate his integration into the team\'s
workflow. Inga will complete her remaining 3 call evaluations while the
team develops the automated evaluation infrastructure needed to scale
beyond manual processes. Matt continues advancing the orchestration
layer with log tracing support and context manager fixes alongside
Danny\'s work to configure production ETL runs in Airflow.

The fragmented people correction script ships early in the week
following Jon and Danny\'s offline resolution of the validation
approach, clearing the way for confident tenant ingestion. Email
engagement functionality awaits only the Gemini key provisioning in
Achilles, which Segev typically handles during Sunday maintenance
windows. The convergence of these workstreams---faster refresh cycles,
GTM store ingestion, cleaned entity data, and email engagement
support---compounds into a materially improved data foundation that
enables the next phase of product capabilities.

*Source: Team 1-2-3 Operating Framework entries from October 6-10, 2025*
