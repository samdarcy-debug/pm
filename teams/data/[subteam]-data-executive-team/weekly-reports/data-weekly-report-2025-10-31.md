---
id: weekly-data-2025-44
title: "Data Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

Data Executive Roundup - [Oct 27th, 2025
- October 30th, 2025]

Executive Summary

The team successfully positioned a Contributory Network Deal Cycle Analysis agent for board
demonstration, with Brandon Wilson completing full pipeline validation and achieving staging
deployment. This represents a tangible showcase of how customer data can power actionable
insights for sales leaders. Brandon Tucker is driving waterfall enrichment requirements to
address competitive gaps with Clay, planning a December launch of free supplemental data
enrichment that maintains quality standards while matching competitor features. Meanwhile,
Igor Kyrylenko expanded professional licenses coverage to 20 states with 11 fully standardized,
positioning FINRA data for productization with Wells Fargo showing early interest.

This Week's Progress

Key Momentum Areas

Brandon Wilson achieved a significant milestone by completing the deal cycle analysis agent
pipeline for the board meeting demonstration. The agent successfully answers complex
questions about tenant deal velocity and provides actionable benchmarks using normalized
Contributory Network opportunity data. After resolving data architecture challenges around the
GTM opportunity table structure, the team eliminated the need for GraphQL calls by properly
handling multi-row stage data, resulting in a more efficient and cost-effective solution that
processes 2 terabytes of data for eligible tenants.

Steve Hutchinson's team launched testing of Clickagy hashed email data as a validation source
for email generation, addressing a multi-year opportunity to leverage cookie-based email
evidence. The analysis will determine whether emails observed during web browsing provide
reliable signals of deliverability, potentially unlocking a high-volume feature for the data science
email generation model. Initial test design is complete with results expected by week's end, and
if successful, this could significantly expand international contact publishing and improve email
coverage across published profiles.

Igor Kyrylenko reached 20 states of professional licenses data acquisition with 11 states fully
processed in standardized format, demonstrating clear progress toward comprehensive national
coverage. The team simultaneously ingested FINRA data into Snowflake with views created for
both individual brokers and firms, positioning it for productization discussions. Working with
Peter and planning to engage Nick Marinaro, the team is preparing FINRA as a credible
alternative to PitchBook, with Wells Fargo expressing interest in using this data to identify
individual brokers and investors.

Goals & Progress

Contributory Network Deal Insights: Brandon Wilson completed full pipeline evaluation and
staging deployment of the deal cycle analysis agent, ready for board demonstration. The
solution leverages the GTM opportunity table directly rather than GraphQL, handling multi-row
stage data to provide complete opportunity timelines. Key learning revealed that opportunity
amounts and other fields previously thought to require GraphQL integration are available in the
opportunity table when properly aggregated, simplifying the architecture and reducing costs
associated with 2-terabyte data scans.

Waterfall Enrichment Strategy: Brandon Tucker documented comprehensive requirements for
waterfall enrichment capabilities, shared with John and the person data team for implementation
planning. The initiative aims to match Clay's supplemental enrichment features while
maintaining quality standards through PTI's 50-accuracy score construct. ByteMine data shows
exceptional promise with nearly 12 million mobile numbers available for US contacts lacking
mobiles, representing significant coverage expansion. The team plans to make this free to
customers, positioning it as a competitive differentiator that highlights ZoomInfo's commitment to
quality data over volume-only approaches.

Vertical Dataset Expansion: Igor Kyrylenko standardized 11 of 20 acquired professional
licenses states into unified layouts, accelerating future processing despite challenges from
states like Ohio with 11 different data formats. FINRA data reached production-ready status in
Snowflake with proper schema and views for investors and firms, advancing toward Wells Fargo
productization discussions. The team is collaborating with Sandeep's offshore resources to
accelerate additional state acquisitions and completed automation tooling for bulk email-based
data requests, pending final legal approval before deployment across multiple dataset types.

Board of Directors Data Product: Jody Roberts advanced requirements documentation for
board of directors and executive leadership data offerings, working to transition from manual
research-driven approaches to automated, scalable solutions. The team identified opportunities
to improve person profile classification accuracy and is exploring coverage gaps to determine
whether automated pipelines alone provide sufficient data or if custom list processing remains
necessary. Brandon Tucker raised important questions about comprehensive board coverage
per company, suggesting new crawling requirements and potential XVerum contributions to
ensure customers can reliably view full boards for target companies.

Company 3.0 Requirements: Ethan Young progressed on HQ address and location profiling
requirements documentation, with design decisions finalized and on track for end-of-week
completion. A significant technical advancement emerged from Company Master Enriched
endpoint work, where improved match service location matching logic can substantially benefit
person data by increasing location ID coverage for contacts. The team also successfully
redeployed the PDD pipeline with improved accuracy metrics, completing QA validation ahead
of board meeting and earnings reporting deadlines.

Strategic Challenges

Privacy and compliance work surfaced an active board member complaint regarding notification
delivery to a guest email that had not received proper privacy notices. Suresh Putteti is
coordinating with legal to analyze the issue and understand gaps in the notification process,
which has implications for board of directors data handling more broadly. This reinforces the
need for robust data lineage and notification tracking as the team scales automated approaches
to leadership data collection and distribution.

Data architecture decisions around the GTM Store and GraphQL revealed gaps between
promised functionality and current implementation. Brandon Wilson discovered that GraphQL
lacks opportunity history views with stage progression data, requiring continued reliance on
direct table queries that scan terabytes of data. Steve Hutchinson previously escalated this gap,
and the team is creating opportunity history objects for GraphQL, but timing remains unclear.
This creates uncertainty around whether to build on GraphQL infrastructure or continue
optimizing direct data access patterns, with cost and maintainability implications for multiple
ongoing initiatives.

Board of directors data quality issues persist despite planned fixes, with Brandon Tucker
identifying that board member classifications remain in employment history rather than proper
board sections on person profiles. The team needs comprehensive queries to identify
misclassified records and validation of whether recent changes actually resolved the underlying
problems. Additionally, the path to comprehensive board coverage per company remains
unclear, requiring new crawling capabilities and potentially SEC filing integrations that aren't yet
scoped or resourced.

Strategic Insights

Key Learnings & Discoveries

The GTM opportunity table contains richer historical data than GraphQL when properly
structured, enabling full opportunity lifecycle analysis without expensive API calls. Brandon
Wilson learned that multiple rows per opportunity tracking stage progression provide complete
timelines that GraphQL's most-recent-record approach misses. This architectural insight
reduces costs substantially and suggests that GraphQL's value proposition around change data
capture and simplified access may not apply equally across all data types, particularly for
historical analysis requiring full audit trails.

Clickagy hashed email data presents a multi-year opportunity finally reaching production testing,
demonstrating how organizational priorities and technical complexity can delay high-value
integrations. Steve Hutchinson's analysis will validate whether cookie-based email observations
provide reliable deliverability signals, potentially unlocking massive coverage expansion. The
team learned that even well-performing data sources face non-technical hurdles including legal
frameworks and data storage considerations that must be resolved before scale
implementation.

Jody Roberts discovered that using ZI Chat with micro-apps to analyze Chorus calls across
large DaaS opportunities reveals unplanned dataset requests from top customers. This
agent-powered approach to surfacing customer needs identified over 20 potential dataset
opportunities not on current roadmaps, demonstrating how conversational AI can extract
strategic insights from existing interaction data. The insight suggests that modular approaches
to existing core data may unlock quick wins alongside the structured vertical dataset motion.

ByteMine integration quality exceeded expectations based on initial LinkedIn joins, showing
nearly 12 million mobile coverage opportunities for contacts currently lacking phone data.
Brandon Tucker noted this represents a significant portion of the 30 million US
LinkedIn-associated contacts without mobiles, making it a high-impact data source. The strong
match rates validate the decision to pursue ByteMine and suggest similar third-party data
integrations may merit acceleration when quality indicators are favorable.

Cross-Team Dependencies

GraphQL infrastructure development from the platform team remains essential for long-term
data architecture strategy, but current gaps require the data team to maintain dual approaches.
Brandon Wilson needs opportunity history views with stage progression, while person and
company data migration to Attribute Store depends on GraphQL supporting change data
capture consistently. The team should provide structured feedback to the GraphQL working
group about missing functionality and continue monitoring the opportunity history object
development timeline to plan migration paths.

Waterfall enrichment implementation requires coordination across PTI, platform, search, and
apps teams to execute by the December deadline Brandon Tucker established. The data team
has requirements documented and data indexed appropriately, but success depends on
cross-functional alignment around how to surface supplemental data, when to show enrichment
options, and how to handle accuracy scoring in the user interface. An off-site working session is
planned to compress development cycles, but realistic timeline assessment depends on other
teams' bandwidth and prioritization.

Looking Ahead

Next week focuses on translating this week's progress into customer-ready capabilities and
board demonstration materials. Brandon Wilson will build local pipeline infrastructure for the
deal cycle agent with full data composition and quality validation, setting the stage for
engineering handoff. The board demonstration represents a pivotal moment to showcase how
contributory network data powers actionable intelligence for sales leaders.
Brandon Tucker will document platform and apps requirements for waterfall enrichment,
detailing data location, accuracy implications, and display logic to enable the December launch
target. The requirements must address how 5x5 and ByteMine contacts appear only in
enrichment contexts while maintaining quality standards in search and other features.
Simultaneously, he'll work with Hazmic's team on shared services normalization and
classification needs as two additional engineering resources become available for that work.

Igor Kyrylenko will continue professional licenses acquisition and processing toward coverage
critical mass while advancing FINRA productization with customer-facing data points and
schema refinement. The automated acquisition tool for bulk email requests awaits final legal
approval before deployment across automotive dealerships and other verticals, representing a
significant acceleration of data collection capabilities. Success here validates the automation
investment and opens pathways for rapid expansion into new regulated industries where public
records provide comprehensive coverage.

Source: Data Executive Operating Framework entries from [Oct 27th, 2025 - October 30th,
2025]
