---
id: weekly-intelligence-2025-42
title: "Intelligence Weekly Report - October 17, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-10-17
updated: 2026-01-06
week_ending: 2025-10-17
reporting_period: "October 13-17, 2025"
tags: ["weekly-report", "Q42025"]
---

Intelligence Team Executive Roundup -
October 13-17, 2025

Executive Summary

Dreamforce delivered strong validation of the team's AI strategy--customer feedback was
overwhelmingly positive, with the Claude/MCP demo landing especially well as competitive
differentiation. Market assessment revealed ZoomInfo is on par with Salesforce in agentic
capabilities, with most competitors significantly behind. The team successfully maintained
platform stability during the conference while Ryan Stevens executed a midnight code migration
to apps gateway, preventing potential domain-poisoning issues. Now focus shifts to three critical
architectural improvements: migrating to a more efficient signals architecture, restructuring
account briefs to solve context window limitations, and resolving web research quality issues
that surfaced in production testing.

This Week's Progress

Key Momentum Areas

Dreamforce execution demonstrated platform maturity. Ryan Stevens and the engineering
team maintained zero production incidents during the conference despite high-stakes demos,
successfully migrated the entire platform behind apps gateway at midnight before the event to
mitigate ISP-dependent SSL issues affecting Dominic's ability to demo. Adam noted feedback
from Dominic and Victor showed customers immediately understood the value proposition, with
the Claude integration serving as the key differentiator when customers asked "what if I have
my own agentic platform?"

No-code agent builder approaching launch with Vivek's team providing unexpected
leverage. Lars Vedo reported the builder is ahead of schedule and nearly ready for
staging/production, with Mayank executing well on implementation. Ryan Stevens observed this
partnership is "so much leverage" by having Vivek handle evangelization and onboarding while
Lars focuses on core platform work. Internal users will be able to build agents and artifacts
within weeks, expanding platform adoption across the organization.

Plays infrastructure reaching first deployment milestone with core tools migrated. Derek
Osgood successfully deployed a base version of DoubleO and Plays to staging, with all
migration work on existing core tools in flight and expected complete by early next week.
ZoomInfo tools should be live today. Derek discovered that approximately half of known
infrastructure issues were actually just poorly written tool descriptions rather than architectural
problems--a valuable lesson about the outsized importance of tool documentation quality.

Goals & Progress

GTM AI Context Service: Rowan Bailey drafted comprehensive PRD breaking down account
brief requirements section-by-section for the updated GTM Store schema, shared with Nilesh for
pre-review before broader distribution to Carlos and the data model team. This work addresses
the critical context window problem where current monolithic briefs blow up agent context after
querying just 4-5 accounts. The PRD establishes clear enrichment flows for each brief section,
building on successful offerings work Carlos's team completed ahead of Dreamforce. Next
phase will tackle person briefs, then tenant/user briefs incorporating first-party data for truly
personalized ICP-driven outreach. Separately, Srivatsa Marthi initiated conversations on signals
architecture migration with both consumers (Snee, Copilot team) and producers (Steve's team,
S2A team), finding surprisingly good early alignment on moving toward a cleaner architecture
where signals become a wrapper rather than a full pipeline.

GTM Studio Core & Plays: Derek Osgood advanced DoubleO tool migration faster than
expected, with staging deployment complete and QA underway on all core tools. Discovered
Andrew Reasonfield's GTM team building entire agentic outbound/inbound workflow but trying
to force it into chat tools due to lack of awareness about Plays capabilities--highlighting the
need for better socialization around when to build tools vs agents vs workflows. Derek
successfully aligned them as "customer zero" for Plays, turning a potential architectural
mismatch into an ideal early use case. The team is 0% worried about December steel threads
assuming the base platform goes live, with only signals/CDC/EventBus integration and a few
additional tools (Outreach, SalesLoft MCPs) remaining as potential risks.

GTM Copilot Workspace: Lars Vedo updated the Q4 roadmap in Jira with detailed epics but
did not publish the shareable backlog version as firefighting took precedence. Identified clarity
gaps around new artifacts (engagement timeline) and the December item for enabling users to
create artifacts, requiring sync with Sean's team. The agent platform's production stability during
Dreamforce validated months of grinding through improvements since April's initial dopamine-hit
demos--Adam credited the team's willingness to "run the gauntlet" of making things work at
scale versus giving up like most companies do.

Strategic Challenges

Web research quality degraded severely after vendor switch, threatening workbooks
integration. Josh built an effective deep research agent using Brave for SERP functionality, but
when the team switched to Melifera (assumed to be a proper supported vendor), performance
collapsed. Jagan's test of 4,000 workbook records saw 75% of agents complete but only 10%
produce remotely good results. Rowan noted this isn't surprising given lack of dedicated
investment, but blocking if left unresolved. Carlos and James are now testing Perplexity against
Google Gen AI Search with 1,000-run sample size comparisons--Philip provided clear guidance
to prioritize best output regardless of partnership considerations. This work should complete this
week with demo of results for broader team review.

SSL and domain issues created red-alert situation during Dreamforce. Ant encountered
SSL errors on Friday, then Dominic hit the same issue--critical since Dominic needed to demo
throughout the conference. Root cause appears ISP-dependent with one ZoomInfo domain
poisoned. Ryan Stevens executed emergency midnight migration moving everything behind
apps gateway, a project that would normally take a week but the team compressed to half a day
under pressure of potential Henry escalation. While the move was successful, it highlighted
infrastructure fragility and the team's reactive rather than proactive approach to foundational
reliability work.

Limited actionable feedback from GTM reps on Context Service testing ahead of
Dreamforce. Rowan ran a training session Monday and set up feedback channels, shared
video and cheat sheet, scheduled testing and office hours--but received minimal rep
engagement. Reps are legitimately slammed with Dreamforce prep, but this pattern of low
internal user feedback prevents iterating on the product before external exposure. Rowan plans
to actively chase feedback at the start of next week now that Dreamforce pressure has lifted,
focusing on specific questions: did users understand what it was immediately, what specific
questions did they have, what confused them. The team needs structured feedback
mechanisms that don't rely on busy sellers volunteering input.

Strategic Insights

Key Learnings & Discoveries

Market assessment from Dreamforce revealed surprising competitive position. Dominic
shared that many companies aren't nearly as far along with agents and AI as
expected--ZoomInfo appears on par with Salesforce and ahead of most others. Adam theorized
this stems from Dominic's April decision to "rebuild our entire application" rather than
incremental feature additions, a risk few vendors were willing to take. Ryan Stevens
emphasized the team's willingness to "grind it out" beyond the easy initial wins separates those
who ship from those who abandon agentic efforts--noting they got all dopamine hits in the first 4
weeks then spent April through October just improving, improving, improving without flashy new
demos. This creates sustainable competitive moat if the team maintains execution discipline.

Tool descriptions emerged as the highest-leverage infrastructure investment. Derek's
investigation of known DoubleO issues revealed approximately 50% were actually just poorly
written tool descriptions for L1 infrastructure tools rather than architectural problems requiring
rebuilds. The automated builder experience issues Vikas built under less direct oversight all
stemmed from inadequate tool documentation versus tools for customer-facing features that
Sumov built with robust descriptions. This pattern reinforces the criticality of comprehensive tool
descriptions--they're not just helpful documentation but core to agent reliability and
performance. The team should establish tool description standards and review processes
before building new capabilities.

Temporal adoption for async agent execution solves scale challenges and establishes
architectural pattern. Cy's decision to make semantic data agent fully async with
Temporal-backed job queue for workbooks integration moves beyond solving an immediate
scale problem to establishing infrastructure the broader platform can adopt. Ryan Stevens noted
Fabio's team moving this direction as well, creating healthy convergence. The durability and
built-in work queue makes this suitable for all workbooks-connected agents and potentially the
foundation for plays execution engine Adam, Ryan, and Frank have discussed for months.
First-to-implement semantic data provides real-world validation before broader rollout.

Cross-Team Dependencies

Our work with the Platform team on MCP gateway and API requirements is now clearly
scoped after Adam's conversation with Ali establishing ownership boundaries. Rowan's team
owns what gets published, roadmap, product marketing narrative, release cadence, and sales
enablement for the Context Service MCP. Ali's team owns gateway implementation and working
with Frank on technical infrastructure. Rowan needs to drive this as a formal program with RLI
to eliminate ongoing confusion about who decides what gets published when, especially critical
as multiple teams want to expose capabilities externally and the platform team has concrete API
requirements for every MCP tool. The working group should meet weekly with clear RACI until
launch.

Coordination with Carlos's team on GTM Config and offerings enrichment continues to
accelerate with strong results. The Gemini-based enrichment of offerings sections ahead of
Dreamforce showed huge quality uplift in context about products, positioning, solutions, and
pain points. Rowan's PRD for account brief sections builds directly on this success to extend the
pattern to other brief components. However, Rowan flagged that downstream consumption of
these enriched sections (like Intent team assigning topics at offering level) doesn't have clear
owners or timelines. The team has the UI before applications can consume the data--a helpful
forcing function but requires active coordination to ensure value reaches end users beyond just
Copilot/MCP access.

Derek's engagement with Andrew Reasonfield's GTM squad surfaced broader
organizational gap in understanding when to build tools, agents, or workflows. They're
attempting to force entire agentic outbound and inbound workflows into ZoomInfo chat tools
simply from not knowing Plays exists and what it enables. Derek used this as opportunity to
onboard them as customer zero, but the pattern suggests PMM gap Adam acknowledged. The
team should create unified messaging and documentation framework for ZI Labs and other
teams on how to work with agents, context, and plays, including guidance for forward-deployed
engineers supporting custom customer configurations. Christine to schedule hour ideation
session with Adam, Derek, Lars, and Rowan.
Looking Ahead

The team enters a critical phase of architectural improvements while maintaining Dreamforce
momentum--three parallel workstreams will shape the platform's next evolution.

Signals migration planning advances this week with Srivatsa driving alignment across
consumers (Snee, Copilot team, David) and producers (Steve's team, S2A team, Andres for
GTM Store implications). Early conversations suggest better reception than expected, though
devil will be in details of signal-by-signal migration paths. The new architecture treats signals as
lightweight wrappers over raw data in GTM Store rather than heavyweight pipelines producing
derived insights--more efficient, more flexible, and eliminating debt accumulation. Srivatsa
transferred to Derek's team since signals-as-play-triggers makes organizational sense, focusing
his roadmap on events, custom signals, and triggering mechanisms. Key meeting Thursday to
lock in direction and sequence.

Account brief restructuring moves from PRD to implementation as Rowan works with Nilesh,
Carlos, and the GTM Store team on schema updates and enrichment pipelines. Success here
unblocks agent context scalability--current monolithic briefs crash orchestrator context after 4-5
accounts, severely limiting batch operations like "which of these 1,000 accounts use Slack?"
The section-by-section approach enables mixing search-based retrieval (for technographic
queries) with full context injection (for complex reasoning), giving agents the right level of detail
for each use case. Rowan also needs to finalize MCP gateway API requirements and ownership
model with platform team per Adam's directive, driving this as formal program rather than ad
hoc coordination.

Web research quality fixes are urgent given poor Melifera results blocking workbooks
integration at scale. Carlos and James complete Perplexity vs Google Gen AI Search testing
this week with 1,000-run comparison demo, then team decides vendor and implements. The
broader learning is to build orchestration wrappers around swappable tools rather than tight
coupling to specific vendors--enables rapid iteration based on quality and cost. Rowan framed
this correctly as "deep research is an agent orchestrating tools" where tools can be Perplexity,
Google, WebQA, or semantic data depending on the use case. Once vendor selected, Josh can
restore the agent to previous quality levels and unblock workbooks team waiting on async
integration.

Advanced Scoring & Recs. Partnered with Sneh and Rowan to align on APS integration into
Workbooks. Current advanced search limitations mean scoring must happen downstream. A full
architecture review across models for both applications and agents is scheduled for next week
to figure out how to build the best models given limitations in advanced search. Worked with
Tanvi on Smart Sort as a potential unifying layer to bring APS, AFS, and IMS ranking into
Workbooks. Also mocked up the Momentum Model here and reviewed early experimentation on
oppty headwinds and tailwinds.
Source: Team Intelligence Operating Framework entries from October 13-17, 2025
