---
id: weekly-product-bi-2025-46
title: "Product BI Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

**Product BI Team Executive Roundup - Week of November 14, 2025**

**Executive Summary**

The team delivered the first AI action credit report this week, which
was received exceptionally well by leadership and demonstrated we\'re
ahead of expected progress on both usage reporting and financial
tracking. However, critical data quality issues emerged in the new API
table that require immediate engineering partnership to resolve before
reliable partner-level reporting can proceed. The team continues
advancing adoption analytics for Workspace and Workbook while preparing
to onboard a new team member next week.

**This Week\'s Progress**

**AI Action Credit Reporting Framework Established**

AJ Belen secured the first comprehensive AI action credit report with
Nanxi\'s support, connecting directly to PostgreSQL to enable live
reporting in Tableau. Leadership feedback confirmed the team is further
ahead than anticipated on both usage analytics and OPEX reporting,
largely due to strong partnership with Jesse on data infrastructure.
This positions the team well for the weekly cadence leadership requires,
though automation is needed to eliminate manual effort once data
migrates to Snowflake this sprint.

**Credit Consumption Patterns Identified Through Correlation Analysis**

Phoebe Mei completed correlation analysis revealing that credit
consumption is most strongly driven by chat depth and volume (number of
AI chats sent) rather than engagement metrics like chat days, view
engagement days, or artifact click days. This insight provides critical
direction for forecasting and understanding what truly drives AI credit
costs, enabling more accurate capacity planning and ROI modeling for the
CFA team\'s upcoming reporting needs.

**Churn Analysis Reveals Targeted Retention Opportunity**

Ferrell Tanuwidjaja\'s preliminary investigation into thin churn
identified approximately 300-332 accounts that churned over the last 12
months, with initial signals suggesting this is largely product churn
rather than complete account loss. Further refinement of the cohort
logic and analysis of usage/spending patterns prior to churn will help
identify specific behavioral indicators and inform retention strategies.

**Goals & Progress**

**\[AI Credits & Monetization\]**: Weekly AI action credit reporting
established with manual process; automation in progress as data migrates
to Snowflake this sprint per Jesse\'s timeline. Credit correlation
analysis completed, showing chat volume as primary driver. **Next
milestone**: Build automated reporting artifact in ZI Chat once
Snowflake pipeline is live, eliminating manual weekly effort.

**\[API Data Infrastructure\]**: Critical data quality issues discovered
in new API table - significant discrepancies between legacy and new
tables for the same API dataset (example: 500 accounts in new table vs
200 in old table for same month). New table also lacks credit
information, requiring complex three-way joins. **Blocker**: Requires
engineering partnership to investigate root cause and align data
sources. Nanxi connecting with engineering team today; Adam kept in loop
despite PTO.

**\[Adoption Analytics\]**: Workspace adoption reporting progressing
with CFA team collaboration to address instrumentation gaps for upcoming
ROI reporting. Workbook dashboard redesign completed and now in
storytelling refinement phase. Chatbot enhancement underway to
incorporate high-level engagement data for self-service analytics. **On
track** for continued iteration next week.

**\[2026 Planning & Team Growth\]**: Performance goal setting for 2026
initiated with Albert. New team member (Kristen) onboarding next week
with Ferrell as onboarding buddy, focusing on API dashboard work to
accelerate knowledge transfer and project continuity.

**\[Account Health Reporting\]**: Intentionally deprioritized after
discussion with Victor, Dominic, and Sanae confirmed minimal likelihood
of paid Workspace accounts before year-end, and all Studio accounts
remain promotional/beta status. Team capacity redirected to
higher-priority AI credit and API work until paid account base
materializes.

**Key Decisions & Blockers**

**Decision**: Deprioritize account health reporting with Mary, Whitney,
and Victor until paid accounts materialize, likely Q1 2026. This
redirects capacity to mission-critical AI credit reporting and API data
quality work.

**Critical Blocker**: API table discrepancies prevent reliable
partner-level reporting and require engineering resolution. The new
table was created specifically to capture partner attribution (per
Adam\'s requirements), but fundamental data quality issues make it
unusable until reconciled with legacy data source. This impacts ability
to deliver on partner-level API analytics that leadership has requested.

**Scene Set for Next Week**

Nanxi will align with engineering on API data resolution path and work
with Albert to finalize 2026 ZIM performance benchmarks and goals. The
team will onboard Kristen with Ferrell leading buddy support, focusing
on API dashboard knowledge transfer. Phoebe will continue refining
adoption metrics for both Workspace and Workbook while validating
chatbot outputs for accuracy. AJ will produce second weekly AI credit
report and coordinate with Jesse on Snowflake migration timeline to
transition from manual to automated reporting workflow.
