---
id: weekly-intelligence-2025-41
title: "Intelligence Weekly Report - October 10, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-10-10
updated: 2026-01-06
week_ending: 2025-10-10
reporting_period: "October 6-10, 2025"
tags: ["weekly-report", "Q42025"]
---

Intelligence Team Executive Roundup -
[October 6, 2025 - October 10, 2025]

Executive Summary

Dreamforce is live next week, and the team successfully enabled ~30 GTM reps with Context
Service access, training materials, and feedback channels. While limited rep feedback came
through pre-event, systems are stress-tested and ready. Concurrently, the team stabilized
Copilot Workspace for high-visibility demos with several critical bug fixes deployed, though a
few issues with target accounts, HTML artifacts, and home-to-chat loading remain under
investigation. The broader strategic shift is taking shape: custom signals are moving into the
plays infrastructure where they belong, and there's growing alignment to deprecate the legacy
signals/insights layer that's accumulating technical debt without delivering proportional value.

This Week's Progress

Key Momentum Areas

Rowan Bailey orchestrated full Dreamforce readiness by running training sessions, establishing
a feedback Slack channel, creating cheat sheets and demo videos, and hosting office hours for
30+ reps. The most valuable insight came from watching reps test beyond the steel
thread--combining ZoomInfo account research with Claude's web search to enrich deals with
industry context proved particularly powerful when prompts specified tool execution order. Lars
Vedo and Ryan Stevens pushed through stabilization work on Copilot Workspace, shipping
batches of improvements while testing Sonnet 4.5 (which is performing well) and addressing
latency issues with Vertex that add roughly 2 seconds per failed call before fallback to
Anthropic.

Derek Osgood achieved a breakthrough on DoubleO integration, getting a basic version live in
staging and clearing up months of circular conversations with the workflows team. The path
forward is now clear: DoubleO becomes the base framework for all workflow capabilities, with
workflows components becoming the actions used by agents, and a shared triggers layer built
on custom signals. Integration will be smoother than expected--the first version simply swaps in
existing OpenAI tools as-is before gradually moving to hybrid MCP tools.

Robyn finalized Lookalikes API is now available for the top 100K most-requested companies,
providing reps with fast candidate generation and similarity results to enrich targeting and
segmentation efforts. Next steps to work with the Workbooks team for integration planned for
Jan 12 release.
Srivatsa Marthi made critical architectural progress on signal configuration after connecting with
Derek. The realization: custom signals should live within the plays infrastructure rather than as
standalone config, since any logic on top of raw data belongs in the play engine. This
crystallized a larger strategic insight--the entire signals and insights layer needs deprecation.
Built for the old Copilot world, it's now just adding complexity without sufficient value, and every
month without migration accumulates more debt.

Goals & Progress

Dreamforce Launch Preparation: Rowan Bailey completed rep enablement with training
sessions, feedback channels, cheat sheets, video walkthroughs, and testing office hours.
Approximately 24 of 30 reps are fully activated and ready to demo GTM Context Service via
Claude. Authentication issues (header size problems from oversized cookies/tokens) were
resolved by extending header limits. The team is maintaining standby support throughout the
event with one final office hours session Monday before the Tuesday launch.

Copilot Workspace Stabilization: Lars Vedo and team focused on zero-regression
deployment, shipping incremental improvements while holding major updates. Current blockers
include unreliable target account pulls, non-interactive HTML artifacts, and occasional
home-to-chat loading failures. The team layered in Salesforce integration improvements to give
agents better context on user hierarchy, recent activity, and custom fields. Sonnet 4.5 testing
shows strong results with updated prompts, though Vertex latency issues (roughly 2-second
delay per 429 error before Anthropic fallback) require tuning to avoid compounding across
multi-call turns.

DoubleO Integration & Tool Migration: Derek Osgood deployed a basic version of DoubleO in
ZoomInfo staging (tools not yet enabled) and aligned with workflows team on integration
architecture. All existing core tools have been triaged and updated with new descriptions and
refined logic. The integration path leverages existing OpenAI tooling initially, then gradually
migrates to hybrid MCP tools that read from GTM Store and write directly to APIs. Key missing
MCP capabilities like Salesforce object association are documented, with teams erring toward
restriction to avoid instance corruption. Primary blocker remains engineering resourcing, though
leadership committed to resolution by week's end.

Strategic Challenges

The APS integration into Workbooks hit architectural friction that requires redesigning the
approach. Since Workbooks streams data via events without default sorting, records appear in
arbitrary creation order rather than ranked by relevance--problematic for demos and actual
usage where sellers expect to see the best prospects first. Applying sorts during streaming
creates jarring UX, and waiting until completion to sort via APS defeats the real-time
experience. The team is exploring solutions like default sortable columns users can apply
post-load, or async operations for CSV uploads where default sorts can be pre-applied. This
connects to a broader realization that Workbooks' tight coupling to its current architecture may
be too inflexible for frontline seller workflows.
Engineering resource allocation remains the persistent blocker across multiple initiatives.
Derek's DoubleO work has only one dedicated engineer (Sumont), Robyn's roadmap is stalled
awaiting clarity on which applications will adopt lookalike MCPs and where UX resources are
allocated, and the broader team is stretching across Dreamforce, Copilot stabilization, and H2
planning simultaneously. Leadership acknowledged an approximately 2:1 ratio of roadmap to
available PM and engineering capacity. Philip has a goal to complete all engineering resource
shifts by end of week to support the locked-down roadmap, with an ask for 11 engineers
(including frontend) for DoubleO. The team needs dedicated squads that can move with the
velocity of semantic data and agentic teams rather than traditional program management
cycles.

Product hierarchy and ML prioritization needs leadership alignment before Robyn can move
forward effectively. There's significant pushback from engineering on creating all algorithms as
MCPs for chat, and uncertainty about whether structured product hierarchy remains a priority
after Carlos flagged it as at-risk for deprioritization. The team needs roadmap review and
prioritization clarity with new engineering leadership, particularly around Workbooks ranking
expectations and how APS should integrate with Workspace insights versus standalone
recommendations work.

Strategic Insights

Key Learnings & Discoveries

The team identified a fundamental architectural shift that should reshape H2 priorities: custom
signals and the broader signals/insights layer need migration into the plays infrastructure.
Srivatsa's conversations with Derek revealed that any "logic on top of raw data" belongs in the
play engine rather than as standalone services. This isn't just a technical refactoring--the entire
signals and insights layer was designed for the old Copilot paradigm and now adds complexity
without proportional value. Every month without migration accumulates debt as more
consumers (including Copilot V1 which won't deprecate soon) remain dependent on the old
system. The migration path is complex but necessary, and leadership appears receptive since it
aligns with broader appetite for deprecating maintenance-heavy systems that don't deliver 10x
outcomes.

Office hours sessions with Dreamforce reps surfaced valuable prompt engineering patterns that
the team should codify. When users specified tool execution order--running ZoomInfo account
research first, then enriching with Claude's web research for industry context--the combined
output quality jumped significantly. This suggests the system would benefit from more explicit
guidance on multi-tool orchestration strategies, potentially as prompt templates or suggested
workflows. The reps' natural tendency to push beyond the steel thread also revealed use cases
(meeting prep combining account research with semantic data, competitive landscape analysis)
that should inform the Context Service roadmap once the event wraps.
Vertex latency patterns are adding measurable drag to the user experience that will compound
at scale. Each 429 error costs roughly 2 seconds before fallback to Anthropic, so a turn
requiring 5 LLM calls can add 10 seconds of pure wait time from retry logic. The team is
investigating whether this is a Vertex reliability issue or a configuration problem on the ZoomInfo
side, but regardless, the Cloudflare AI Gateway should address this class of problem through
better load balancing and failover. Ryan Stevens is coordinating with Benny's team to ensure
proper evaluation this month rather than rushing to meet an arbitrary October 15th deadline that
was never realistic given vendor procurement timelines.

Cross-Team Dependencies

Workbooks integration requires deeper architectural alignment before the team can deliver on AI
capabilities that leadership is pitching to customers. The streaming event architecture that
makes Workbooks feel fast creates fundamental conflicts with ranked results from APS, credit
forecasting UX, and semantic data integration.

The resource allocation conversation with Philip and Dominic needs resolution by Monday to
unblock DoubleO delivery for December. Derek requires a dedicated squad of engineers (the
11-person ask includes frontend) that can operate with the autonomy and velocity of semantic
data and agentic teams rather than traditional program management. Adam proposed giving
Derek and Karthik a subset of engineers to "run like we run semantic data" and just push
through for December, but this requires Sarah Heritage to lock down the roadmap first. The
dependency chain is clear: roadmap locked  Philip shifts resources by week's end  Derek
gets focused squad  December delivery becomes achievable.

Looking Ahead

Next week is Dreamforce execution mode with the team maintaining standby support for the 30
reps demoing Context Service. Rowan is running one final office hours Monday before the
Tuesday event, then shifting focus to collecting structured feedback and identifying quick wins
versus longer-term improvements. The engineering team will monitor system performance
under real load and tune alerts accordingly.

The more strategic focus shifts to H2 planning and architectural cleanup. Srivatsa is
documenting the signals/insights deprecation plan to free up engineering attention and reduce
system complexity--work that should get strong leadership support given the broader push to
reduce maintenance burden. Derek will kick off in earnest once engineering resources are
allocated, starting with first batch of tools live by Tuesday and spinning up plays in staging to
identify tool gaps. Robyn needs roadmap alignment meetings to clarify ML/agent prioritization
and get engineering commitment on MCP strategies.

Across the team, the November 3rd go-live date for Workspace and Copilot sales enablement is
the forcing function. All reps should be trained and actively pitching by then, which means the
next three weeks are about polish, stability, and rep enablement rather than new features. The
team proved this week they can ship incremental value while maintaining stability for
high-visibility demos--that discipline needs to carry through October while the deeper
architectural work (plays, signals migration, DoubleO) progresses in parallel.

Source: Team Intelligence Operating Framework entries from [October 6, 2025 - October 10,
2025]
