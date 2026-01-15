---
id: weekly-product-bi-2025-38
title: "Product BI Weekly Report - September 19, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-09-19
updated: 2026-01-06
week_ending: 2025-09-19
reporting_period: "September 15-19, 2025"
tags: ["weekly-report", "Q32025"]
---

**Product BI Team Executive Roundup - September 19, 2025**

**Executive Summary**

Copilot Workspace (V2) launched to 100+ internal GTM users this week
with external customer rollout planned for early October. AJ Belan and
Phoebe Mei identified a P0 instrumentation bug blocking user ID capture
in Amplitude, which engineering is actively resolving. The team has
strong momentum on renewal predictions, API usage analysis, and
partnership metrics while navigating expected data architecture
challenges with Coors integrations.

**This Week\'s Progress**

**Key Momentum Areas**

AJ Belan finalized renewal prediction scoring analysis with Phoebe Mei
ahead of the October 18th ELT meeting, establishing a foundation for
account health reporting that can be efficiently updated as new data
becomes available. This positions leadership with data-driven insights
for strategic account discussions.

Phoebe Mei delivered comprehensive Workspace adoption tracking
implementation, identifying event tracking gaps and working directly
with engineering to resolve the user ID instrumentation issue. Her
proactive debugging ensures the team will have clean analytics once the
external rollout begins in October.

Nanxi Ge successfully aligned all stakeholders on request prioritization
without pushback, including partnerships with Albert, Xuxian, and
pending Ali alignment. This strategic coordination enables the team to
focus resources on high-impact initiatives like API usage analysis and
partnership network development.

**Goals & Progress**

**Copilot Workspace Analytics**: Phoebe Mei implemented tracking
infrastructure for the internal rollout to 100+ GTM users, with
expansion planned next week and external customer access starting early
October. The P0 user ID bug is actively being resolved with engineering
support, clearing the path for comprehensive adoption and engagement
analysis.

**Account Health & Renewals**: AJ Belan completed renewal prediction
score analysis supporting the October 18th ELT presentation, with
streamlined update processes established for future iterations. The
analysis identifies large C and D tier accounts requiring attention,
providing actionable insights for account management.

**Integration & API Analytics**: Ferrell Tanuwidjaja and Eran Dayan are
building unified data sources combining frontend and backend workspace
data while advancing API usage analysis. The team discovered valuable
insights about GTM table consolidation requirements and semantic layer
development for more accurate business logic representation.

**Strategic Challenges**

Coors integration historical data remains difficult to access due to the
product\'s separate data architecture from acquisition, with accuracy
concerns between settings and import tables. Nanxi Ge is working with
data engineering to leverage CDP import tables as the most reliable
source, though this requires complex multi-table joins for comprehensive
analysis.

Amplitude event archiving capabilities are unclear despite admin access,
with Ferrell awaiting support resolution on whether certain event types
can be properly archived. This impacts cleanup efforts but doesn\'t
block current workspace tracking implementation.

The Israel team will have limited availability next week (only
Thursday-Friday) due to Rosh Hashanah, which may affect integration
metrics development timeline but has been factored into project
planning.

**Strategic Insights**

**Key Learnings & Discoveries**

Partnership network initiative revealed an interesting contribution
model where the company exchanges site visitor intelligence with
partners for enhanced customer targeting. This creates a data-rich
environment for measuring partner value through visitor quality,
conversion rates, and mutual referral effectiveness, though data won\'t
be available until mid-to-late October.

API usage analysis uncovered previously unexplored data sources that
could provide deeper insights into product utilization patterns. This
discovery positions the team to deliver more comprehensive usage
analytics than initially scoped, potentially revealing optimization
opportunities across the platform.

Workspace rollout feedback collection through enablement forms shows
limited initial volume (only 3 entries) but establishes qualitative
feedback infrastructure to complement quantitative Amplitude data. This
dual approach will provide richer user experience insights as adoption
scales.

**Cross-Team Dependencies**

Our work with engineering on the Workspace P0 instrumentation bug is
moving efficiently, with Phoebe Mei actively participating in resolution
threads. The quick engineering response demonstrates strong
collaboration for launch-related analytics needs.

Data engineering coordination with Linda on new CDP table structures
will require combining multiple object tables (accounts, users,
opportunities) rather than unified views. While not ideal
architecturally, this approach is understood and planned for in upcoming
integration analysis work.

**Looking Ahead**

Next week focuses on scaling Workspace analytics capabilities as
internal rollout expands and external customer access begins, with
particular emphasis on early adoption patterns and user experience
insights.

Phoebe Mei will continue analyzing early Workspace adoption once the
user ID issue resolves, enabling detailed AE and AEM usage path analysis
with drop-off identification. Ferrell will join the tracking
implementation effort with full tool access configured. Meanwhile, Nanxi
Ge begins two-week API usage data exploration while maintaining chatbot
development momentum with Jack through weekly or bi-weekly sync
establishment.

The team is well-positioned to provide comprehensive Workspace launch
analytics, deliver actionable renewal insights to ELT, and advance
partnership measurement strategy development as data becomes available
in Q4.

*Source: Team 1-2-3 Operating Framework entries from September 15-19,
2025*
