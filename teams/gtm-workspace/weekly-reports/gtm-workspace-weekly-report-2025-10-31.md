---
id: weekly-copilot-2025-44
title: "GTM Workspace (Copilot) Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

SalesOS/Copilot Executive Roundup -
[Oct. 27, 2025 - October 30, 2025]

Executive Summary

Sean Walter is refocusing the December roadmap around three core themes following the GTM
data model pivot: features that deliver aha moments and help sell the product, platform narrative
connections (workbooks/GTM Datastore integration), and validated high-priority user feedback
addressing fundamental gaps. The shift toward GTM data model integration represents a
significant architectural decision that won't disrupt the roadmap substantially--a POC is feasible
for December that will enable view creation across different datasets, addressing current
limitations around data source joining. Meanwhile, the 2K limit workaround using recommended
filters is progressing toward Monday's release, though Sean expresses 60% confidence in the
November 3rd sales readiness milestone due to chat accuracy concerns and latency issues that
continue to erode user trust.

This Week's Progress

Key Momentum Areas

Copilot Workspace readiness advances despite architectural complexity. Sean Walter
completed a refocused December roadmap document based on GTM data model requirements,
user analytics, and consolidated feedback, organizing priorities around three coherent themes:
delivering aha moments that help sell the product, advancing the platform narrative through
workbooks and GTM Datastore connections, and addressing validated high-priority user
feedback on fundamental functionality gaps. The team confirmed with Andres that a GTM data
model proof-of-concept is feasible for December, which will enable users to create views based
on the GTM data model and join across different datasets--addressing significant limitations
around joining between data sources and reducing integration effort for new datasets.

ZoomInfo Intent work unblocks critical competitive capabilities. Hari Krishnamoorthy
discovered that 40% of customers who should be receiving Intent recommendations are not
getting them--approximately 1,246 out of 3,206 qualified customers--and escalated this
pipeline issue to the data science team for immediate investigation, with a review call scheduled
to determine root cause and next course of action. Hari completed technical discovery for
Account Level Intent in Copilot Workspace by identifying three integration approaches: manual
field addition to ZoomInfo section (available immediately), MCP server or sub-agent conversion
for agentic handoff, and direct view creation from Intent signals (highest customer value), with
Lars emphasizing the need for evaluation framework modeling and the GTM Studio team
confirming existing infrastructure can handle view creation once data flows into GTM Store.

Admin Zero Experience capabilities expand for Enterprise customers. David Goulden
finalized documentation for the bulk territory loader and completed info packs for Admin Defined
Territories, with some UI tweaks for admins being worked on in the coming week for GA
readiness. The team made progress testing GTM data model queries for Priority Accounts,
documenting migration paths, though work continues on determining how to federate that into
search and access it in other services, with a planned January target for moving existing
customers with rules set up to GTM data model queries.

Next best actions: Ant Cuomo completed a final round of evaluations on the next best actions
agent with over 10 internal sellers, concluding that NBA agent are giving accurate, credible
recommendations that reps are finding valuable. Next steps are to work towards short-term and
medium term platform integrations.

Goals & Progress

Copilot Workspace: Sean Walter reports 60% confidence in November 3rd sales readiness,
citing concerns about the 2K limit issue and chat accuracy problems including latency
complaints and incorrect data source selection, with the real test being how quickly the team
can fix these fundamental problems. Adam Severance confirmed that work on 2K limits,
recommended filters, and priority fields is green for Monday release in staging, though not yet
fully end-to-end testable in staging, with the team having made hard decisions about the
experience to land in the best possible place. The workspace is shifting focus from feature
additions to user experience quality, with Victor Oliveros emphasizing that chat, artifacts, and
views must improve markedly every week.

ZoomInfo Intent: Hari Krishnamoorthy conducted technical discovery for Account Level Intent
integration, identifying that if Intent data successfully flows into GTM Store, the Copilot
Workspace UI infrastructure can handle remaining view creation requirements, significantly
de-risking implementation. Hari is working on a value proposition document explaining why
customers would use Copilot Workspace instead of the Intent Tab and what additional value can
be provided through consolidation. The discovery of the 40% recommendation gap represents
both a challenge and an immediate addressable revenue opportunity once resolved.

Admin Zero Experience: David Goulden finalized bulk territory loader documentation,
completed info packs for Admin Defined Territories release, and is putting together templates
with additional documentation, with final UI tweaks for admins being worked on for GA
readiness later in November. Work progressed on building an MCP interface to territories to
open them to agents, with ongoing refinement with the search team to determine how to
interface various system languages, since territories are currently stored in Ringlead rule syntax
and structure. Customers are expressing strong demand for opening territories into both
advanced search and workspaces.
Additional Initiatives: Gabe Pirela made progress refining email sequence requirements and
solution direction after meetings with GTM Studio team, Studio Plays team, and orchestration
teams, with updated requirements expected by end of week followed by a larger review session
to ensure all use cases are covered. Gabe completed design review for workspace meetings
(the Chorus convergence work), with design details expected by end of week and engineering
starting work on basics, though pulses will be key to pushing actions and updates to users
rather than having them find meeting or CRM update sections.

Strategic Challenges

Copilot Workspace faces fundamental chat reliability issues that threaten sales
readiness. Sean Walter expressed 60% confidence in November 3rd readiness, with primary
concerns around the 2K limit problem and chat feedback showing latency complaints and wrong
data source selection, noting the real test is how quickly these problems can be fixed. For
demos, Sean believes following a narrow path works reasonably well, but the biggest unknown
is chat reliability--citing an example where asking about preparing for an Adobe meeting
produced a good slideshow initially, but an hour later the same query didn't get proper context
and produced lower quality results, indicating issues with chat understanding hierarchies,
referencing recent data, and refining user questions. Adam Severance noted that chat-to-views
base functionality is live in staging but not good enough, with most issues stemming from the
prompt itself and the LLM not understanding how to navigate right use cases, requiring
significant time from the product team to improve the orchestrator layer's understanding of their
specific use case. The team needs chat to improve every single week, but current processes for
agent iteration and refinement are proving time-consuming.

GTM data model dependencies create cross-team coordination complexity and timeline
uncertainty. Sean Walter noted that GTM Config status has been quiet from his perspective
with limited understanding of direction and timing, despite roadmap line items, and that the team
needs to start driving requirements because users are providing feedback about missing context
like "why is it not knowing this about me or this about the company". Sean emphasized the team
needs a consolidated list of demands from the GTM data model across all team members, since
GTM data model is central to success of most initiatives and a unified view of asks would help
from a coherence perspective, impacting profile pages, views, chat, and other forward-looking
features. David Goulden raised concerns after speaking with designer Julia about GTM Config
work, noting they tend to design for net new customers but many existing customers won't go
through full setup--they've already half-configured the system--so the offering setup flow
designed as if starting new won't work well for the installed base. This architectural dependency
affects multiple workstreams and requires careful coordination to prevent downstream adoption
issues.

Territory and Priority Accounts features face technical integration blockers limiting
Enterprise customer capabilities. David Goulden indicated there are questions about how
territories stored in Ringlead rule syntax can be opened up and made accessible in other
places, requiring the team to figure out interfaces between various system languages.
Customers are providing feedback expecting territory recommendations to get smarter based on
companies they're turning down, but the recommendation engine doesn't currently incorporate
that feedback even though it's being stored, creating unmet expectations for adaptive learning
that emerge quickly in customer interactions. David noted that role-based rules for CRM
matching won't likely go away since GTM config won't always know what users have at any
given point in time, meaning a rule-matching interface will be needed to allow tuning, with UI
work kicked off but requiring integration with GTM config systems. The path forward requires
resolving how to make territories searchable objects while deciding whether to retrofit
capabilities back into current advanced search or make them available only in workspaces.

Strategic Insights

Key Learnings & Discoveries

User-level personalization emerges as critical unaccounted capability for chat
effectiveness. Sean Walter identified that basic user-level personalization, particularly for chat,
isn't accounted for in the current roadmap but needs urgent attention--users constantly ask "is
chat actually getting smarter, what does it know about me?" and the answer is nothing outside
conversation context, with the hypothesis that providing users basic ability to supply information
operating like a system prompt would massively impact performance, accuracy, and buy
significant goodwill. This insight connects directly to the chat reliability challenges and suggests
a foundational architecture gap rather than purely prompt engineering issues.

GTM data model integration unlocks compound value beyond immediate technical
benefits. The GTM data model proof-of-concept enables view creation by joining across
different datasets, which is particularly important given limitations around joining between data
sources and the work required to integrate any new data set, with Andres expressing high
enthusiasm to solve previously discussed gaps including write-backs and field access. For
Account Level Intent specifically, if data successfully flows into GTM Store, existing Copilot
Workspace infrastructure handles remaining view creation requirements, significantly de-risking
implementation and suggesting faster path to production than initially expected. The
architectural decision to prioritize GTM data model integration creates platform leverage that
accelerates multiple feature workstreams simultaneously.

Agent iteration velocity constraints threaten competitive product development pace. Ant
Cuomo noted that the entire process of iterating and refining agents is taking a long time, with
the account prioritization agent missing a merge and releases happening weekly, preventing the
team from getting agents out in production for evaluation, leading to discussions with Lars and
Ryan about improving the agent development process. Sean Walter emphasized that the
recommended filter approach for the 2K limit is useful in itself but doesn't solve the core problem
of seamlessly joining and filtering across data sources, with the algorithm behind
recommendations needing improvement. Victor Oliveros requested a write-up on agent iteration
challenges for product leadership, indicating this process constraint affects multiple teams and
requires systematic resolution.
Cross-Team Dependencies

Our work with the Agentic Platform team on chat improvements and agent development
continues to be critical for workspace reliability and feature velocity. Adam Severance has daily
calls with Eric and Tanmoy to improve chat-to-views functionality, with most issues stemming
from the prompt and LLM not understanding how to navigate right use cases, requiring
significant time from the product team to improve the orchestrator layer's understanding of the
specific use case. Additionally, chat lacks ability to assess the number of rows being output, so
the 2K limit creates problems--the team is moving forward with making that API available, and
chat will need to take iterative passes to understand row counts and follow required logic for
views to work properly. The dependency extends to mobile development, where Ant Cuomo
reported good progress with Lars and the mobile team on handling chat, determining that
investing in a scrappy web view isn't worthwhile given too many edge cases, instead pursuing a
headless design approach where a JavaScript controller dictates what gets rendered natively,
which can also be used in the new chrome extension.

Our collaboration with the GTM Data Model team has intensified around Priority Accounts and
workspace data access. David Goulden reported good progress testing GTM data model
queries for CRM data but noted it's unclear how to federate that into search or access it in other
services, with target January timeline for moving existing customer base with configured rules
over to GTM data model queries. Ant Cuomo is meeting with Andres and team to walk through
end-to-end profiles and GraphQL queries to get needed data, with the call scheduled to identify
any gaps. Cross-functional alignment is essential here as multiple product workstreams
(profiles, views, Intent integration, Priority Accounts) depend on consistent data access patterns
and query capabilities from this centralized system.

Looking Ahead

Next week's primary focus centers on validating November 3rd sales readiness while advancing
December architectural foundations. The team will conduct user experience walkthroughs of
Monday's release package before calling features green, with Sean, Adam, and Victor reviewing
what's shipping to ensure no surprises in the sales-ready milestone.

Top priorities include solidifying chat reliability and GTM data model integration paths.
Adam Severance emphasized the need to dedicate significant team time to improving the chat
prompt and overall orchestrator understanding, noting there are many fronts for improving chat
generally and chat-to-views specifically, requiring clarity on next steps and weekly improvement
cadence. Sean will compile consolidated GTM data model requirements and demands across
the team since it's central to most initiatives, providing unified visibility into asks that will impact
profiles, views, chat, and forward-looking features. Hari will work with engineering on high-level
plans and timelines for Account Level Intent in Workspace while developing the value
proposition for why customers should use Workspace over the Intent Tab. David will finalize
templates and prototypes showing where territories can be used in existing screens and
workspaces, while continuing Priority Accounts migration work. Gabe will review final designs
for workspace meetings and groom epics to start development November 1st as planned, while
finalizing email sequence requirements for larger team review.

We're moving from broad capability building to targeted experience refinement. The
architectural decisions around GTM data model integration and user-level personalization will
compound benefits across multiple features, but execution depends on resolving agent iteration
velocity constraints and chat reliability issues. With sales enablement starting November 3rd,
the team has limited runway to address fundamental experience gaps--success requires
ruthless prioritization of improvements that directly impact the narrow demo paths while building
sustainable foundations for post-launch iteration.

Source: Team SalesOS/Copilot Operating Framework entries from [Oct. 27, 2025 - Oct. 30,
2025]
