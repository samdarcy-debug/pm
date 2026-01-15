---
id: weekly-product-bi-2025-42
title: "Product BI Weekly Report - October 17, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-10-17
updated: 2026-01-06
week_ending: 2025-10-17
reporting_period: "October 13-17, 2025"
tags: ["weekly-report", "Q42025"]
---

**Product BI Team Executive Roundup - Week of 10/17/2025**

**Executive Summary**

Session recordings are now the highest priority for understanding
Workspace users ahead of the November 3rd release, but capacity
constraints prevented progress this week due to Dreamforce and product
team bandwidth. The team pivoted productively---Phoebe successfully
instrumented key Workspace features (chat, view sharing, quick search)
despite discovering significant data quality issues, while Nanxi
advanced the ZI Agent for Slack channels after pausing API work. Two
infrastructure issues need immediate attention: the CDP-to-Snowflake
connection has broken (affecting multiple dashboards), and the CRM data
source deprecation requires urgent migration by Ferrell.

**This Week\'s Progress**

**Key Momentum Areas**

Phoebe completed instrumentation for the core Workspace features that
will drive the November 3rd release readiness, including chat location
tracking, view sharing, and quick search functionality. This positions
the team to validate adoption patterns and identify UX improvements
post-launch. However, she uncovered instrumentation problems---including
instances where 100 events fire on a single page load---that AJ
escalated to Sean and will address with Victor to ensure reliable
reporting.

Nanxi made meaningful progress on the ZI Agent for Slack channels after
pausing the API dashboard project in alignment with Adam. She created a
test channel and discovered that while qualitative questions
(documentation, links) can be answered from historical Slack messages,
quantitative questions (ad spend, top performers) require live data
integration. She\'s now working with the ZI Marketing team to implement
their specific datasets and will coordinate with Jack on the Slack
integration process to move toward a production-ready solution.

Ferrell delivered the taxonomy work for Workspace alongside Inbal, then
pivoted to address the urgent CRM data source deprecation. He\'s
collaborating with Linda and Andrews to migrate to the new source and
has refined the Active Integrations dashboard with improved taxonomy and
enriched general events. The dashboard is nearly complete, though the
large data volume is slowing refresh cycles during testing.

**Goals & Progress**

**Workspace Analytics & Instrumentation**: Phoebe advanced
instrumentation for November 3rd launch readiness by successfully
tracking chat, view sharing, and quick search events. Inbal created
comprehensive taxonomy for Workspace search and profile features to
prevent future instrumentation gaps. These efforts support a data-driven
launch strategy, though discovered instrumentation bugs---such as
excessive event firing---will need resolution before reporting is fully
reliable. Inbal will be out of office next week.

**ZI Agent Development**: Nanxi paused API dashboard work this week per
alignment with Adam to avoid redundant effort while waiting for new
data. She shifted focus to the ZI Agent, setting up a test channel and
identifying that quantitative questions require real-time data feeds
rather than just historical Slack searches. Next steps include meeting
with Jack on Slack integration capabilities, implementing ZI Marketing
datasets, and gathering stakeholder feedback from sales, product
marketing, and CSM teams to validate the solution.

**Chatbot & Semantic Data Layer**: Eran continued building
production-ready data flows to bring account setup data directly into
Snowflake for natural language querying through the chatbot. He\'s
working with Nier and the data engineering team to productionize these
pipelines and establish the semantic data layer that will enable
self-serve analytics across the organization. This infrastructure work
is foundational for reducing BI team ticket volume.

**Strategic Challenges**

The CDP-to-Snowflake connection that enables automatic dashboard
refreshes has broken, forcing manual data updates across multiple
dashboards that rely on CDP data. Ferrell investigated with Arsin
initially assuming it was a Tableau issue, but Tableau confirmed the
problem is on the company\'s side---Nanxi can no longer even access the
custom query field when connecting via service account. Igor is aware,
but if Ferrell and Arsin cannot resolve this by early next week, further
escalation will be necessary since manual refreshes are not sustainable.

Session recordings represent a more valuable learning opportunity than
analytics for understanding Workspace users right now, but capacity
constraints on both the BI team and product team prevented progress this
week. Dreamforce and the November 3rd launch push consumed product
stakeholder availability (Adam, Sean, Victor). AJ and Phoebe must
prioritize this next week despite competing demands, as the qualitative
insights will be harder to capture post-release when user behaviors
stabilize.

The CRM data source deprecation creates time pressure for Ferrell to
complete migration to the new source. The data\'s size and complexity
mean that refreshing and testing changes takes considerable time, which
is extending the timeline. He\'s making steady progress with Linda and
Andrews but needs to complete this work promptly to avoid service
disruption for teams relying on CRM-based reporting.

**Strategic Insights**

**Key Learnings & Discoveries**

Phoebe\'s instrumentation work revealed that over 50% of internal users
are now engaging with Workspace, showing steady multi-week growth at 62%
week-over-week and 22% week-over-three. However, view sharing remains
minimal---only 17 users have shared a view since October 12---suggesting
an opportunity to better communicate this feature\'s value in future
onboarding or team communications. Chat activity is concentrated on the
Homepage at 67%, while Quick Search shows low engagement with only 10%
of users who open the search bar actually executing a search, indicating
users may not understand what\'s searchable. Updating placeholder text
to clarify scope (e.g., \"Search companies, contacts, or
recommendations\") could improve adoption.

Nanxi\'s exploration of the ZI Agent revealed that most Slack channel
questions are quantitative and time-sensitive, requiring access to
current data rather than historical conversations. This fundamentally
changes the technical approach---simply searching past Slack messages
won\'t deliver value. The team needs to implement live datasets specific
to each channel\'s needs. For the ZI Marketing pilot, this means
connecting ad spend data, campaign performance, and other marketing
metrics. The learning is that each channel will require custom data
integration based on the questions its members typically ask, making
this more complex than initially expected but also more valuable when
properly implemented.

Ferrell\'s work on the Active Integrations dashboard uncovered that the
new ZDP table for engagement imports needs careful alignment with
existing CRM import tables in terms of granularity and field
definitions. Getting this data architecture right now will prevent
reporting inconsistencies down the road. The team is documenting the
setup and implementation steps to enable broader adoption of this
pattern across other analytics channels.

**Cross-Team Dependencies**

Our work with the product and engineering teams on instrumentation
remains essential for delivering reliable Workspace analytics ahead of
November 3rd. AJ escalated the instrumentation issues to Sean, and the
team will connect with Victor to work through resolution. The basic
telemetry framework needs to separate \"main\" feature instrumentation
stories from other development work to ensure analytics isn\'t
perpetually delayed or compromised by competing engineering priorities.

The ZI Agent work depends on Jack\'s completion of the Slack integration
and his guidance on data implementation approaches. Nanxi will sync with
him next week to understand what\'s changed in the integration process
and determine whether the ZI chatbot\'s existing data sources can be
leveraged or if channel-specific datasets require separate
implementation. Clear technical guidance here will determine whether
this work scales efficiently across multiple Slack channels.

Ferrell needs continued support from Arsin and Igor to resolve the CDP
connection issue. The data engineering team shared an update about the
Tableau MCP server feature that could be relevant for the team\'s future
direction---potentially moving away from Tableau toward chatbot-native
dashboards. Ferrell will spend a few hours exploring this with the
engineer who shared the update to assess implications for the team\'s
tooling strategy.

**Looking Ahead**

Next week\'s top priority is session recordings with Phoebe and product
stakeholders to extract qualitative insights about Workspace usage
patterns before the November 3rd external launch. This work has been
delayed but cannot wait longer---the team needs to understand how users
are actually experiencing the product, especially given the
instrumentation issues that make quantitative analysis less reliable
right now.

Nanxi will connect with Jack early in the week to align on Slack
integration status and data implementation strategy for the ZI Agent.
Depending on when the API data becomes available from the engineering
team---originally expected early this week---she\'ll either begin
validating data relationships and building the API dashboard, or
continue advancing the ZI Agent with stakeholder testing. Ferrell must
complete the CRM data source migration and resolve the CDP-Snowflake
connection issue, escalating if necessary. He\'ll also spend a few hours
exploring the Tableau MCP server capability to inform the team\'s
strategic direction on dashboard tooling. Eran will continue
productionizing the semantic data layer work with the engineering team.

The team is well-positioned to deliver value across multiple fronts,
with clear ownership and next steps on each initiative. The
infrastructure challenges are being addressed systematically, and the
focus on qualitative insights through session recordings will complement
the instrumentation improvements to build a complete picture of
Workspace adoption.

*Source: Team 1-2-3 Operating Framework entries from week of 10/17/2025*
