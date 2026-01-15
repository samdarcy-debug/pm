---
id: weekly-semantic-data-2025-30
title: "Semantic Data Weekly Report - July 25, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-07-25
updated: 2026-01-06
week_ending: 2025-07-25
reporting_period: "July 21-25, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Semantic Data Team Executive Roundup - July 25, 2025**

## **Executive Summary**

The Semantic Data Team successfully processed 25,000 high-ACV accounts
this week while solving critical database scaling issues that were
blocking the pipeline. Josh Mantovani identified and fixed a one-line
environment setup bug that was plaguing the agentic platform---a
breakthrough that unblocks platform development. The team is now
positioned to enable multi-tenant support next week, with authentication
and orchestration work ready to begin.

## **This Week\'s Progress**

### **Key Momentum Areas**

Rowan Bailey drove strategic alignment on H2 Planning, securing
agreement from data science teams on goals and epics for transitioning
from rigid heuristic systems to dynamic ML models. The new account fit
and in-market scoring models will update by tenant, representing a
significant maturation in organizational capabilities. This positions us
to better serve both prospecting and account management use cases.

Jon Seller solved critical database connection scaling issues that were
blocking the high-ACV account pipeline, enabling the team to process 90
days of data for 25,000 accounts. The fix allows the full pipeline to
run at scale in the dev environment with minimal errors, where it
previously would \"blow up.\" This unblocks the path to multi-tenant
support and positions us for rapid customer onboarding.

The momentum score initiative was successfully kicked off with two
productive meetings, addressing a critical gap in helping AEs and AMs
prioritize their active deals. Unlike account fit scores for
prospecting, momentum scoring will tell sellers which of their 20 active
opportunities are trending toward closure versus those needing revival.
This directly supports our strategic shift toward selling to AEs and AMs
through the platform.

### **Goals & Progress**

**Data Pipeline & Infrastructure**: Jon Seller achieved 90% completion
on high-ACV account processing (25,000 of \~27,500 accounts), solving
core database connection issues that were causing pipeline failures. The
correction script for fragment processing mismatches is ready to run
over the weekend, addressing data quality issues reported by support.
Multi-tenant PR is complete pending passive login integration.

**Extraction Quality & Evaluation**: Inga Isakov completed 5 email
thread evaluations, uncovering critical edge cases including LLM
hallucination issues where ABC was incorrectly extracted as an entity in
Disney/ESPN communications despite no mention in the source data. This
finding highlights the importance of controlling general knowledge
injection in our extraction pipeline. Weekend work will complete the
remaining evaluations and begin data source analysis.

**Memory Service & Agentic Platform**: Josh Mantovani\'s breakthrough
fix for the environment setup issue unblocks agentic platform
development after weeks of troubleshooting. The Memory service project
was successfully kicked off with Grant, Asher, and Eric, establishing
the actions log concept for tracking high-value copilot interactions.
Josh will lead this implementation starting next week.

### **Strategic Challenges**

Authentication complexity for multi-tenant support is creating
networking challenges between GCP and dev containers, preventing Jon
from completing the passive login integration. The team is exploring
local setup workarounds to maintain momentum on multi-tenant delivery.
Resolution requires either DevOps support to fix networking or
completion of local environment setup as a temporary measure.

Data source prioritization remains unresolved, with stakeholders pushing
for job posting data integration despite fundamental misalignment with
our current extraction pipeline. Rowan correctly identified that job
postings require different ontology and processing than interpersonal
communications. The team needs executive alignment on whether to build a
separate pipeline for structured data sources or focus on expanding
interpersonal communication sources first.

Grant\'s availability for orchestration RFC review was blocked by
agentic demo priorities, delaying critical architectural decisions for
the scalable pipeline. While the demo takes precedence, this pushes
orchestration design discussions to next week, potentially impacting our
ability to handle dynamic account filtering and priority queuing for the
growing pipeline demands.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The LLM hallucination discovery by Inga reveals a critical vulnerability
in our extraction pipeline where models inject general knowledge even
when explicitly processing isolated email threads. The ABC/Disney/ESPN
case demonstrates that our current approach allows unwanted entity
associations based on real-world relationships rather than document
content. This finding will drive prompt engineering improvements and
stricter context controls.

Josh and Rowan\'s analysis confirmed that our current pipeline
architecture is fundamentally incompatible with structured data sources
like job postings. The extraction ontology designed for interpersonal
communications produces \"garbage\" when applied to job listings. This
validates the need for multiple pipeline architectures rather than
forcing all data through a single processing model.

The database scaling solution reveals that half the pipeline issues
stemmed from misunderstanding Google Cloud Proxy connection patterns
rather than code problems. Jon\'s deep investigation into connection
pooling and error patterns provides a template for avoiding similar
scaling issues as we onboard new tenants and increase data volumes.

### **Cross-Team Dependencies**

Our work with Data Science on the momentum score and enhanced scoring
models requires tight coordination as they begin model development. The
success of these initiatives depends on clear API contracts and data
availability timelines from our pipeline. Weekly syncs with Arash and
Nilesh will be critical to ensure model requirements align with our
extraction capabilities.

The Memory service implementation requires close collaboration with
Grant\'s team on the agentic platform, though his demo commitments are
limiting availability. Josh\'s leadership on this project will need to
balance independence with necessary architectural alignment once Grant
becomes available next week.

## **Looking Ahead**

Next week\'s primary focus is enabling multi-tenant authentication to
unblock customer onboarding, with Jon working through networking issues
while preparing the orchestration RFC for dynamic pipeline management.
This positions us to handle multiple customers while maintaining data
isolation and quality.

The team will complete extraction evaluations and begin detailed scoping
of new data sources, with particular attention to the job posting
question that requires executive alignment on strategic direction.
Inga\'s analysis will inform whether we pursue a separate structured
data pipeline or double down on interpersonal communication sources that
align with our current architecture.

Josh will lead Memory service implementation while the broader team
reviews orchestration patterns for scalable pipeline management. Success
requires balancing immediate multi-tenant needs with longer-term
architectural decisions that will determine our ability to scale to
dozens of customers and data sources.

*Source: Team 1-2-3 Operating Framework entries from July 21-25, 2025*
