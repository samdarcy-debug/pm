---
id: weekly-product-bi-2025-43
title: "Product BI Weekly Report - October 24, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "Q42025"]
---

**Product BI Team Executive Roundup - Week of October 20, 2025**

**Executive Summary**

The team is on track for the Workspace V2 external launch on November
3rd with all data requirements documented and PM alignment secured,
though a concerning utilization trend has emerged that warrants
attention. Weekly Workspace utilization dropped from 36% to 29%,
primarily driven by AE and AM users showing reduced engagement with
views and chat features. Meanwhile, Eran successfully deployed six
Copilot setup metrics into the production chatbot, and Nanxi\'s AI agent
testing in Slack shows promise for scaling self-service analytics,
though API data delays continue to push back planned analysis work.

**This Week\'s Progress**

**Key Momentum Areas**

Eran delivered the team\'s first production chatbot metrics, enabling
account managers to query Copilot setup status, seat utilization, and
targeting data directly through conversational interface. The
implementation required building Snowflake tables and navigating
approval processes, and Eran is documenting the end-to-end workflow so
the full team can contribute additional metrics going forward.

Nanxi advanced the CI Chat Slack integration to eliminate the current
friction where users must click through to a separate interface. Early
testing of the AI agent shows it correctly answers straightforward
questions about customer spend and access patterns when working with
Snowflake tables, with comprehensive documentation now in place for
others to replicate the process across additional Slack channels.

The team conducted cross-functional session recordings with Gabe, Adam,
Victor, and Phoebe that surfaced valuable insights about user behavior
beyond what instrumentation captures. These sessions revealed how users
actually struggle with features in practice and highlighted gaps between
what the team measures and what drives real adoption.

**Goals & Progress**

**Workspace V2 Launch Preparation**: Phoebe completed documentation of
all data requirements for the November 3rd external launch and aligned
timelines with the PM team. She connected with the surveys team to tie
engagement data back to qualitative user feedback, creating a fuller
picture of feature performance. Work continues on setting up the
Workspace chatbot template with Eran to make high-level adoption metrics
accessible to cross-functional teams.

**Analytics Infrastructure & Chatbot Automation**: The team deployed six
production metrics covering Copilot setup factors and account targeting,
with plans to shift focus to Workspace adoption metrics next week. Nanxi
created reusable documentation for the full analytics automation
workflow and is testing the AI agent\'s ability to handle increasingly
complex queries across more data tables before expanding to additional
high-traffic Slack channels.

**Data Pipeline Modernization**: Ferrell is working through the
integration data source migration from legacy tables to the new data
model, though the swap is taking longer than expected. The new source
has incomplete historical data and different granularity, requiring the
team to identify the exact cutoff point and determine how to preserve
old data as a flat file while transitioning forward. The Integration
team is aligned on the path forward despite the timing push.

**Strategic Challenges**

API usage data remains unavailable due to engineering delays, with the
timeline now pushed to end of this week or potentially next week. This
blocks Nanxi\'s primary workstream on API dashboard development and
usage analysis, forcing her to redirect capacity to Slack automation
work while waiting for the data pipeline to stabilize. The team needs
engineering support to deliver the clean dataset and enable stakeholder
participation in chatbot testing.

Workspace instrumentation has gaps that limit the team\'s ability to
understand the full user journey. While front-end event tracking exists
for key features, backend reporting is missing which prevents robust
chat-level analytics. Most of the complete instrumentation won\'t be
available until after the 11/3 launch given other work the team is
prioritizing, creating a window where early adoption insights will be
incomplete.

The data source migration for integration reports uncovered
misalignments between old and new sources, including missing historical
data and different volume patterns. Since core engagement metrics use a
four-week rolling window, losing historical data would create reporting
gaps. The team needs to coordinate with the Integration team on
preserving the legacy source while moving forward, adding complexity to
what was expected to be a straightforward swap.

**Strategic Insights**

**Key Learnings & Discoveries**

Phoebe discovered that 60% of internal users have engaged with Workspace
at least once since launch, but weekly utilization fell from 36% to 29%,
with AE and AM users driving most of the decline. Their utilization
dropped from 49% to 38% to 32% over three weeks. Analysis of the view
funnel shows significant drop-off: only 40% of users who open a view
make any modification like filtering or sorting, suggesting potential UX
issues with view design or unclear next actions.

The team is questioning whether view modifications actually matter for
driving desired outcomes. If users who modify views engage with chat at
similar rates to those who don\'t modify, then the drop-off may not be
concerning. Phoebe has the data to run this analysis and will determine
whether view engagement is truly a leading indicator of valuable chat
interactions or if it\'s a surface-level metric.

Chat response time emerged as a potential friction point, with median
time from message send to response at 1 minute 12 seconds. This feels
notably slower than consumer experiences with ChatGPT and Claude, which
condition users to expect sub-60-second responses. For a product
targeting busy sales and account management workflows, response latency
could significantly impact perceived value and adoption momentum.

Session recordings proved more valuable than anticipated, revealing user
struggles and behavior patterns that instrumentation doesn\'t capture.
The cross-functional perspective with product and engineering team
members watching together created shared understanding of where features
fall short in practice. The team plans to continue these sessions even
if it means using dedicated co-pilot time slots to force the priority.

**Cross-Team Dependencies**

Amplitude announced that all event data is now accessible via MCP (Model
Context Protocol) for chatbot integrations. This could enable the team
to bring Workspace and Studio front-end events more comprehensively into
the internal chatbot, reducing manual analysis requests and improving
self-service capabilities. Someone needs to connect with Jack to explore
whether the current chatbot implementation can leverage this new
Amplitude integration.

The Integration team\'s urgency to deprecate the old data source is
creating pressure on Ferrell\'s migration work, though both teams are
now aligned on the need to preserve historical data while transitioning
forward. The next monthly report will be the trigger point for fully
swapping to the new source after confirming the old source is archived
appropriately.

**Looking Ahead**

AJ is prioritizing getting alignment with Mary, Victor, and Whitney on
how to measure account health and success for Workspace accounts. This
framework will define not just what metrics matter but how field teams
operationalize them in their workflows. Phoebe and AJ will take a first
pass early in the week and bring a proposal to Thursday\'s meeting,
anticipating that the discussion will immediately focus on team
operationalization rather than metric selection.

A new strategic priority is emerging around agent credit consumption
tracking. The team will assign an analyst (likely Farrell or Nanxi given
their backgrounds with workflow credits and credit pacing) to own
visibility into how much customers are spending across different agents
in the ecosystem. This work will become increasingly important as agent
usage scales and influences renewal and expansion conversations.

Nanxi will either resume API usage analysis if engineering delivers the
dataset this week, or expand the Slack automation pilot to another
high-visibility channel. The team continues balancing planned roadmap
work with the reality of upstream data dependencies, maintaining
momentum through documentation and process improvements that will pay
dividends when blocked workstreams unblock.

*Source: Team 1-2-3 Operating Framework entries from October 24-27,
2025*
