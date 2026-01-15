---
id: weekly-product-bi-2025-44
title: "Product BI Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

**Product BI Team Executive Roundup - 10/31/25**

**Executive Summary**

The team achieved a critical milestone this week by launching the first
AI-powered self-service analytics agent in the ZIM Slack channel,
enabling stakeholders to get instant answers to common questions without
BI team intervention. This represents meaningful progress toward scaling
our support model. Simultaneously, the Workspace analytics foundation
strengthened significantly with the completion of a storytelling-driven
adoption dashboard ready for PM self-service ahead of the November 3rd
external rollout, while the account health reporting framework advanced
through cross-functional alignment on use-case-driven measurement. Next
week focuses on expanding Workspace engagement visibility through
chatbot integration while the API dashboard work resumes as engineering
completes data backfill.

**This Week\'s Progress**

**Key Momentum Areas**

**AI Agent Self-Service Launch in ZIM Channel**: Successfully deployed
the team\'s first AI-powered analytics agent to the ZIM Slack channel,
creating a scalable alternative to manual ad-hoc requests. The agent
supports two query modes: historical search across past channel
conversations for qualitative questions, and auto-query capabilities for
time-sensitive quantitative questions like customer counts on Copilot or
top Marketing OS spenders by impression/click metrics. Early testing
shows strong performance across multiple question types. Stakeholder
testing is now underway to collect feedback before expanding to other
analytics channels. Created comprehensive documentation for Confluence
to support future rollout. This directly reduces the team\'s reactive
support burden while improving stakeholder response time from hours to
seconds.

**Workspace Adoption Dashboard Redesign for PM Self-Service**:
Transformed the Workspace adoption dashboard from a raw data view into a
storytelling-driven experience that flows from overall usage to specific
feature adoption. The redesigned interface enables PMs and stakeholders
to independently understand adoption patterns without BI assistance.
User path analysis for AE and AAM segments (the primary target
customers) revealed that 40% initiate workspace chat directly from the
homepage, 23% navigate to view functionality, and 16% of chat users also
engage with views---demonstrating strong multi-feature engagement.
Dashboard is production-ready ahead of the November 3rd external user
launch, when Workspace becomes available as an Enterprise package
upgrade.

**Workspace Account Health Reporting Framework Development**:
Established foundational alignment with Mary, Whitney, and Victor on the
measurement approach for Copilot Workspace account health reporting. CX
will tag each account with a primary use case, creating the structure
for use-case-aligned reporting that mirrors how customer success teams
actually manage accounts. This user-centric framework ensures reporting
matches the mental models of GTM teams rather than imposing technical
taxonomies. The approach positions BI to deliver onboarding health
metrics and post-onboarding success indicators that directly support
account management decisions. Key challenge identified: determining the
aggregation logic for rolling up use-case-level metrics into
account-level health scores.

**Goals & Progress**

**\[Workspace Account Health Reporting\]**: Use-case framework alignment
complete with CX team. Next step requires designing the rollup
methodology that aggregates use-case-specific metrics into account-level
health indicators for both onboarding and post-onboarding phases.
Proposal documentation targeted for next week to establish reporting
standards before external accounts launch.

**\[Workspace Analytics & Self-Service\]**: Workspace engagement metrics
integration into the internal chatbot progressing with Eran securing
necessary database access permissions. Workbook dashboard cleanup
prioritized for next week to reduce complexity from current 20-tab
structure that creates navigation challenges for stakeholders. On track
to deliver comprehensive adoption reporting framework before external
launch.

**\[API Usage Dashboard\]**: Paused active development this week while
awaiting complete data backfill from engineering, but validated that
published data structure contains required fields for dashboard
requirements. Resume development next week now that structure review is
complete.

**\[AI Agent Expansion\]**: ZIM channel deployment complete and in user
testing phase. Pending Slack-Chat integration from AI Chat team before
broader rollout---integration will eliminate friction of navigating to
external chatbot link by keeping all interaction within Slack.
Identified constraint that integration-focused channels cannot be next
expansion target due to CDP data dependency (chatbot currently only
works with Snowflake data). Next expansion requires selecting a
Snowflake-heavy analytics channel.

**\[Marketing OS Churn Analysis\]**: Data foundation established this
week despite Ferrell\'s illness reducing capacity. Analysis will
quantify churn magnitude and identify contributing factors for product
team intervention. Next week continues analysis development and timeline
estimation.

**\[Core Engagement Analytics\]**: New requests emerging as additional
data becomes available on PM side. Ferrell evaluating data feasibility
and effort estimation for upcoming sprint planning.

**Unsolved Blockers & Why**

**Backend Event Instrumentation for Workspace Key Events**: Account
health reporting capabilities limited by reliance on frontend
(Amplitude) instrumentation only. Backend event logging would enable
significantly deeper and more reliable insights into user behavior
patterns, particularly for technical actions that may not fire frontend
events consistently. R&D timeline for creating backend data tables
currently targets early December, which creates a measurement gap during
the critical initial onboarding period for external accounts. Risk: May
need to retrofit reporting logic once backend data becomes available.

**Slack-Chat Integration Timing**: Full AI agent rollout to additional
channels blocked pending completion of Slack-Chat sync from AI Chat
team. Current workflow requires users to click external link to access
chatbot, creating friction that reduces adoption likelihood. Integration
will enable seamless question-asking directly in Slack channels. Nanxi
coordinating with AJ on timing for broader rollout once integration
completes. Workaround identified: can begin expansion to
Snowflake-focused channels while integration completes.

**CDP Data Access for Integration Channels**: Cannot deploy AI agent to
integration-focused analytics channels because their data resides in
CDP, which the chatbot doesn\'t currently support. This eliminates
several high-value expansion candidates. No immediate workaround;
requires either chatbot CDP connectivity or data pipeline changes.

**CRM Data Source Migration Complexity**: Import data transfer from
legacy to new CRM source encountering unexpected technical complexity,
requiring iterative problem-solving with CDP team. Delays may cascade to
downstream analytics that depend on this data. Migration scope proving
larger than initial assessment. Ferrell working with CDP team to
resolve.

**Limited Access to Airtable and Jenkins**: Eran\'s limited access to
Airtable and Jenkins causing minor dependencies on the Data team for
certain development tasks, though not currently blocking major
deliverables.

**Key Learnings This Week**

Learned that effective AI agent performance requires sophisticated
prompt engineering tailored to different question types---adjusting
phrasing and context logic differently for historical retrieval versus
real-time quantitative queries significantly improved accuracy. Nanxi
documented these patterns for future channel expansions. The agent\'s
ability to handle time-sensitive spending analysis questions (e.g.,
\"who spent the most in the last 7 days\") demonstrates particular value
for questions that previously required lengthy manual analysis.

User behavior data revealed unexpected insight about Workspace adoption
patterns: the strong crossover between chat and view usage (16% of chat
users also engage with views) suggests these features create
complementary value rather than competing for attention. After landing
on the homepage, most AE and AAM users either initiate a chat (40%) or
open a view (23%), showing that these are the primary entry points. This
finding should inform product prioritization and marketing messaging for
the November 3rd external launch.

Dashboard complexity threshold identified: 20-tab workbooks overwhelm
stakeholders and defeat self-service goals regardless of data quality.
Phoebe prioritizing ruthless scope reduction for the Workbook cleanup to
create clearer information architecture. Future dashboard design should
address navigation challenges during initial build rather than
post-launch.

CX team\'s use-case framework for managing Workspace accounts provides a
valuable blueprint for structuring analytics---aligning reporting to
customer-facing use cases rather than technical feature taxonomies
creates more actionable insights for GTM teams. This user-centric
approach should inform future reporting design across other products.

Eran learned to work more independently with Git, DBT, and semantic
models---tools that clearly represent the future of analytics and data
delivery at the company. This technical upskilling reduces dependencies
and improves team agility.

**Scene Set Next Week**

**AJ Belen**: Document proposal for use-case-level to account-level
health metric rollup methodology, establishing the reporting framework
for both onboarding and post-onboarding phases. Socialize approach with
Mary, Whitney, and Victor to validate it supports their account
management workflows before external Workspace accounts launch.

**Phoebe Mei**: Push Workspace engagement metrics into internal chatbot
for real-time querying, enabling stakeholders to ask adoption questions
conversationally. Execute Workbook dashboard cleanup to reduce
complexity and improve self-service experience. Collaborate with Eran on
database access provisioning and front-end event instrumentation
requests for PM and engineering teams.

**Nanxi Ge**: Resume API dashboard development now that data structure
validation is complete, building query framework and establishing core
visualizations. Finalize AI agent documentation upload to Confluence and
continue collecting stakeholder feedback from ZIM channel testing.
Coordinate with engineering on data backfill timeline.

**Ferrell**: Continue Marketing OS churn analysis development, moving
from data foundation to identifying churn patterns and quantifying
impact for product team. Directly test churn analysis ideas targeting
the approximately 783 customers affected. Evaluate feasibility and
timeline for new Core engagement analytics requests. Discuss and
prioritize integration engagement import metric development with
stakeholders, including identifying which fields from new GTM tables
should be used in Core Engagement tables.

**Eran Dayan**: Complete Workspace Utilization table for chatbot
integration, finishing database access setup. Focus on productionizing
the utilization semantic model and validating chatbot accuracy for
utilization-related questions.

*Source: Team 1-2-3 Operating Framework entries from 10/31/2025*
