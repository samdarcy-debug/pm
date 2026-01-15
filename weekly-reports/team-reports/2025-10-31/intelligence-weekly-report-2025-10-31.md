---
id: weekly-intelligence-2025-44
title: "Intelligence Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

Intelligence Team Executive Roundup -
[October 27, 2025 - October 31, 2025]

Executive Summary

The team is in the final stages of shipping the November 3rd release for Copilot Workspace with
slides, citations, recent Chorus engagements, and view creation via chat. However, three critical
issues demand immediate attention: costs are unsustainably high due to unoptimized context
and expensive models, performance is slower than acceptable, and semantic data coverage
gaps are creating user frustration. Lars Vedo and Ryan Stevens are leading the November 3rd
launch while managing technical debt from rapid prototyping, with Carlos Nunez stabilizing the
workbooks-semantic data integration that nearly derailed the release timeline. A decision was
also made to process all account's engagement data using the Semantic service so we can
close the gap on missing engagement data next week.

This Week's Progress

Key Momentum Areas

Lead by Dylan Halladay, slides functionality was enabled in production ahead of the board
meeting and rolling out to test users now. Additionally, inline citations for Semantic, Chorus, and
Salesforce sources are rolling out now. The new agent architecture with improved sub-agents is
being tested behind feature flags, enabling users to create views via chat and leverage
ZoomInfo data more effectively, setting up a strong foundation for the Monday release.

Carlos Nunez and the infrastructure team rescued the workbooks integration by implementing a
temporal solution for batch agent execution over an intense weekend sprint. After identifying
that bulk semantic data requests were consuming daily token limits, the team deployed
automated stops and improved logging, demonstrating the power of focused vertical squads to
ship critical functionality under pressure.

Derek Osgood pushed all M1 plays functionality into staging, with core orchestration, ZoomInfo,
email, and CRM tools now live and ready for QA. The team achieved clarity on cross-functional
dependencies after productive sessions in Bethesda and Waltham, positioning plays to support
both basic use cases and the more complex pulse activation scenarios that sales teams are
requesting.

Goals & Progress
Agentic Platform & Copilot Workspace: Lars Vedo's team is 95% complete on the November
3rd release, with slides in production, citations working for multiple sources, and the new agent
with sub-agents in testing. Target accounts bug fixed and email functionality opening in Gmail as
planned. Creating views via chat and improved ZoomInfo data integration are currently in testing
on staging. The team is managing scope carefully after learning that rapid prototyping created
maintenance overhead, with emailer requiring a rebuild and several "quick win" features from
earlier demos now requiring significant polish work.

Infrastructure & Semantic Data: Carlos Nunez stabilized the workbooks-to-semantic-data
pipeline after discovering that bulk requests were hitting Anthropic token limits. The
temporal-based batch execution system is now processing requests reliably for approximately
14,000 accounts with semantic data. The team identified that vector search alone doesn't serve
all semantic query types well, recognizing the need for a query router with both vector and text
search capabilities as a longer-term solution. Web search is working for bulk operations, and the
team plans to consolidate two separate web search paths into a single agent post-release.

Plays & GTM Intelligence: Derek Osgood completed all M1 plays functionality in staging,
including orchestration tools, ZoomInfo tool, email tool, and CRM tool. Andy Harjanto has been
assigned initial connector work for Global Event Bus and go-to-market store integration.
Srivatsa Marthi finalized the architecture for migrating signals into plays, determining that the
team can skip the temporary GSO integration and move directly to the end-state solution since
key CDC events will be available by Q4. Next week focuses on QA of tools and defining
requirements for filtering logic and GTM store attribute schemas.

Strategic Challenges

The team is experiencing "death by a thousand cuts" from maintaining too many
quickly-prototyped features that demonstrated well but weren't built for scale. Target accounts,
workbooks activation, and the emailer all required significant rework this week when moving
from demo to production-ready. This maintenance burden is compounded by the agentic team
supporting multiple product surfaces simultaneously, with Ryan Stevens and Josh White being
pulled across workbooks, workspace, and other initiatives. The lesson learned is clear: tighter
scope management and building for reliability from the start would prevent this technical debt
accumulation.

Three critical technical issues require immediate focus beyond the release. First, costs are
"crazy high" according to Lars, with unoptimized context, expensive models, and unnecessary
LLM calls driving unsustainable spend. Second, performance is lagging user expectations,
directly related to the cost issues through extra LLM calls and inefficient context handling. Third,
semantic data coverage is incomplete - users expect to chat about any engagement visible in
Chorus, but the current approach only uses semantic data, creating frustration. Hitting Chorus
directly would blow up context windows and require weeks of work, making comprehensive
semantic coverage the strongly preferred path forward.
Semantic data infrastructure needs urgent attention earlier than originally planned. Rowan
Bailey restructured the Q4 roadmap to address infrastructure demands from Copilot Workspace
alongside the original GTM Studio timeline. Three blockers emerged: uncertainty around
whether the GraphQL API delay affects MCP Gateway launch in mid-December, lack of
semantic data for expected accounts due to conservative cost-control filters that now cause
more friction than value, and confusion around admin portal migration paths as products
package together in unclear ways.

Strategic Insights

Key Learnings & Discoveries

The weekend war room approach proved its value when Carlos Nunez's team and platform
members worked vertically to solve the workbooks-semantic data integration crisis. What
Jagannath initially estimated as weeks of work was completed in two days through focused
collaboration without competing meetings. The tradeoff is clear: vertical squads sacrifice
platform-wide alignment for shipping speed, which is acceptable when closely monitored to
prevent teams from diverging into incompatible directions. Ryan Stevens and Lars Vedo's
"power move" of forming temporary vertical teams delivers product to users most efficiently,
even if it limits broader platform work.

Carlos Nunez discovered that bulk semantic data requests can consume the entire daily
Anthropic token limit, exposing gaps in observability and automated safeguards. The team is
now implementing better logging and automatic stops to prevent one bulk operation from
starving all agents of tokens. Additionally, vector search alone proved insufficient for all
semantic query types - the team identified the need for a query router that can choose between
vector search and traditional text search depending on the query, similar to production-scale
retrieval systems. These infrastructure learnings highlight the gap between prototype and
production-ready systems.

Robyn Sablosky's updates:

     Lookalike Accounts, now covering the entire ZoomInfo universe of accounts with an
         API-called approach for the long tail. The team validated that API calls are infrequent
         enough for the bottom 20% of accounts that real-time neural network scoring is
         cost-effective.

     Three new MCPs for ranking algorithms (Account Priority Score, Lookalikes
         Accounts, Lookalike Contacts) went live in staging for AI chat testing, allowing the
         team to experiment with whether algorithms work better as standalone tools or combined
         with other capabilities.

     Robyn submitted designs to the Workbooks team for how to use Scoring + Lookalike
         Algorithms in their product

     IMS to be released next week: The In-Market Score (IMS) shows which accounts are
         actively showing interest in a company based on real-time behaviors and external
         signals. It combines data such The In-Market Score (IMS) shows which accounts are
         actively showing interest in a company based on real-time behaviors and external
         activity. It combines data from multiple sources -- including CRM opportunities,
         engagements, user usage data, S2A signals, WebSights, G2 and TrustRadius
         activity, account-level intent, Scoops, and Account Recommender vector
         candidates -- into one unified score.as intent, website visits, contact engagement, and
         company activity into one score that indicates how likely an account is to be interested
         right now.

Cross-Team Dependencies

Work with the GTM Data Model team, particularly Majed and Linda, is critical for finalizing signal
namespaces in GTM Store. Srivatsa Marthi discovered the current unified namespace approach
doesn't align with the architecture needed for plays, requiring each signal type to have its own
namespace. The Global Event Bus dependency with Mark Frail is tracking to approximately one
week from completion, allowing the team to skip temporary GSO integration and build the
permanent solution directly. Platform team coordination around inference proxy, prompt store,
and BYOK continues to be a strategic dependency that affects both agentic and semantic data
capabilities.

The Context Service work crosses multiple teams as Rowan Bailey works with Ali's organization
on MCP Gateway, Vinod and Imesh on GraphQL API timeline, and the GTM Config team on
defining packages and access patterns. The freemium/ZI Lite program is 80% complete
leveraging earlier PLG work, positioned to let users try ZoomInfo's MCP tools in Claude and
ChatGPT before becoming full customers. Derek Osgood's plays initiative depends on front-end
React resources that are scarce company-wide, creating a constraint on the next wave of
features. The team needs dedicated design resourcing commitments from Sean Walter's group
to maintain momentum.

Looking Ahead

The November 3rd release on Monday represents a major milestone, but the team immediately
shifts focus to three priorities: cost optimization, performance improvements, and expanding
semantic data coverage. Lars Vedo and Ryan Stevens will lead agentic tuning and fast-follows
including email sending, notes as a data source, and Outreach integration.

Derek Osgood's team spends next week on comprehensive QA of all tools in staging before
rolling out the first plays to internal users. Srivatsa Marthi finalizes filtering requirements for
Andy Harjanto to begin connector implementation while updating GTM Store attribute schemas.
Carlos Nunez consolidates the dual web search paths into a single robust agent and works with
Rowan Bailey to prioritize semantic data infrastructure improvements. The team must balance
shipping new features with addressing the underlying technical debt and cost issues before they
become unsustainable.
Looking further ahead, the pulses use cases from Ant's team require more complex trigger
combinations than initially planned - triggers with filters and time-based conditions. Ryan
McMaster explores mobile experiences for frontline sellers while Derek Osgood scopes
sequencing tooling to track exit criteria for plays acting as sequence orchestrators. The vision is
coming together for end-to-end GTM intelligence from plays to pulses to frontline execution, but
communicating this new product architecture will require sustained effort across the organization
as it represents an entirely new way of thinking about how products connect.

Source: Team Intelligence Operating Framework entries from [October 27, 2025 - October 31,
2025]
