---
id: weekly-product-bi-2025-47
title: "Product BI Weekly Report - November 21, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-11-21
updated: 2026-01-06
week_ending: 2025-11-21
reporting_period: "November 17-21, 2025"
tags: ["weekly-report", "Q42025"]
---

**Product BI Team Executive Roundup - Week of Nov 21, 2025**

**Executive Summary**

AI Action Credit reporting successfully completed its second week with
established reporting structure now being shared org-wide. Workspace
analytics achieved breakthrough with new user segmentation framework
enabling targeted activation strategies. Critical technical blockers
emerged around API data quality and currency reporting that require
cross-functional resolution.

**This Week\'s Progress**

**Key Momentum Areas**

**Workspace AI User Segmentation Framework Delivered** Phoebe built a
four-segment categorization model for active Workspace users based on
consistency of usage and AI credit consumption depth. This framework
enables targeted activation strategies, persona-level monitoring of user
movement between segments (tracking shifts to
high-usage/high-consistency behaviors), and cohort-level distribution
analysis. This positions us significantly ahead of where we were with
Copilot launch - we\'re building these insights proactively rather than
playing catch-up.

**AI Action Credit Reporting Structure Established** Completed second
iteration of weekly AI credit reporting with Nanxi. The format has been
approved and will be shared in the products channel moving forward,
creating consistent visibility into credit consumption patterns. Early
reporting infrastructure is successfully surfacing data quality issues
before external customer launch, validating the value of our proactive
dashboard work.

**2026 Ad Spend Forecasting Analysis Completed** Wrapped up initial 2026
ZIM performance goal discussions with Anwar and Ben. Identified critical
gap in international domain expansion benchmarking and surfaced currency
reporting discrepancy issue - all spend currently reported in USD
regardless of original currency, creating misalignment with finance
reports. This has been flagged to marketing leadership for Q1
resolution.

**Goals & Progress**

**\[Workspace Analytics\]**: User segmentation framework delivered and
ready for team review. Event naming governance issue identified and
escalation in progress with PM team to establish advance notice process
for instrumentation changes.

**\[AI Credit Reporting\]**: Weekly reporting cadence established.
Historical negative credits issue identified with SurveyMonkey data -
fix is scoped but not yet implemented. Continuing to flag anomalies as
we build confidence in data accuracy.

**\[2026 Planning\]**: Initial forecast complete pending Ben\'s finance
number confirmation. Expect 2026 targets to be lower than 2025 due to
absence of comparable major client spending without replication
strategy. International expansion variables remain unquantified.

**\[Infrastructure Development\]**: API usage analysis remains blocked
by engineering OOO (Adam out sick, following up next week). Microapp
exploration revealed significant data format and aggregation limitations
requiring structured dataset approach. Chatbot agent experiencing
timeout issues on 1000+ row exports.

**Unsolved Blockers & Why**

**API Usage Data Discrepancies - Critical Priority** Engineering
resource constraints have stalled all API analysis work. Adam was out
sick this week; expecting resolution when he returns next week. This
blocks downstream reporting dependent on reconciled request data and
impacts ability to validate credit consumption accuracy.

**Currency Reporting Alignment - Strategic Risk** Current USD-only
reporting creates discrepancies with finance reports and will become
critical as international domain expansion accelerates in 2026. Requires
data pipeline changes to preserve original currency and conversion
timestamp. Flagged to Ben and marketing leadership but no timeline for
resolution yet.

**Churn Cohort Data Quality - Resolved via Workaround** Multiple data
sources for contract end dates created inconsistency in Farrell\'s churn
analysis. Rather than continuing time-intensive reconciliation for
one-time report, obtained definitive cohort list directly from finance
team. This unblocks analysis but surfaces broader need for golden record
data governance.

**Event Naming Changes Breaking Reports - Governance Gap** Homepage
engagement event naming changed without advance notice to analytics
team, breaking multiple downstream reports. Following up with Ants on
both immediate fix (restoring naming + adding required event properties)
and process improvement to share instrumentation changes before
implementation.

**Key Learnings This Week**

**Early-stage reporting infrastructure validates investment** - Finding
data quality issues (negative credits, API discrepancies, currency
misalignment) before external launch demonstrates our proactive approach
is working. These discoveries happen because we have visibility, not
despite it.

**Workspace analytics ahead of historical benchmarks** - Building
segmentation frameworks and adoption tracking pre-launch puts us months
ahead of where we were with Copilot, when similar analysis came too late
to inform go-to-market strategy.

**Microapp limitations require structured data approach** - Agent
timeout issues and format constraints mean microapps work best with
pre-aggregated, clean datasets rather than raw query access. This
insight shapes how we should architect future self-service tools.

**Scene Set Next Week**

**Short Holiday Week - Focus on Foundation Building** With Victor out
and lighter meeting schedule around Thanksgiving, team will use
uninterrupted time for deeper work:

- **Nanxi**: AI credit investigation and Microapp exploration if API
  data becomes available. Tableau automation exploration for temporary
  reporting views.

- **Phoebe**: Workspace chat conversation analysis to identify question
  patterns by persona (what are AMs asking vs. AEs?). This supports
  product roadmap prioritization.

- **AJ**: Microapp creation hands-on learning using Workspace data as
  foundation. Share quadrant segmentation framework with Victor and
  Dominic for feedback. Continue workspace agent testing.

- **Eran**: Operationalize automated weekly GTM Workspace performance
  reporting with AE/AM engagement emphasis. Enrich Workspace data source
  with AI credits validation.

- **Christon**: Continue onboarding with Amplitude and Snowflake
  exploration, follow up on RevReady and Tableau access requests.

- **Ferrell**: Out of office all week

**Deliverable**: Next AI Action credit report will proceed as scheduled
despite short week (no manual corrections, report data as-is and flag
historical fix status).
