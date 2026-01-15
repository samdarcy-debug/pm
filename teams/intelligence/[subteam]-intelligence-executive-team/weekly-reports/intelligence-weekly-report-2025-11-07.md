---
id: weekly-intelligence-2025-45
title: "Intelligence Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

Intelligence Team Executive Roundup -
[November 3, 2025 - November 7, 2025]

Executive Summary

The team successfully launched M1 for GTM Studio and Copilot Workspace this week, with both
products now live in production. While the rollout went smoothly with no major incidents,
immediate focus has shifted to addressing cost optimization and agent accuracy issues that
emerged during early customer interactions. Ryan Stevens and Lars Vedo are leading efforts to
reduce LLM costs through prompt caching and architectural improvements, while
simultaneously working to decrease hallucination rates that currently affect approximately
one-third of chat interactions. The team demonstrated strong cross-functional collaboration with
design teams to unify chat experiences across products, and initial customer demos are
generating significant positive feedback despite some rough edges in the demo path.

This Week's Progress

Key Momentum Areas

The M1 milestone was successfully deployed to production on Friday, marking a significant
achievement for both GTM Studio and Copilot Workspace. Derek Osgood completed the tools
infrastructure with CRM, email, and ZoomInfo tools all functional in staging, while the underlying
workflow automation is now operational. The launch included the successful implementation of
AI credits flowing through the system, providing the team with baseline metrics on actual
customer usage patterns and credit consumption.

Cross-team design collaboration reached a new level of maturity this week. Lars Vedo worked
with design leadership to map all chat entry points across Sales OS and GTM Studio, proposing
unified patterns that are now moving into engineering implementation. The embedded chat
experience is visible in workspace staging environments, demonstrating tangible progress
toward a consistent user experience across the platform.

External validation came through a standout customer demo with True Context, where Victor
showcased the workspace artifact creation capabilities. The demo leveraged semantic data to
pull exact quotes from customer calls, directly addressing client pain points and generating
visible enthusiasm from prospects. This successful demo pattern is now being studied to identify
UI improvements and streamline the demo flow for broader sales team adoption.

Goals & Progress
Platform Launch & Stabilization: The team successfully toggled feature flags and deployed
the M1 release with both GTM Studio and Copilot Workspace now live in production. Derek
Osgood's tools wave completed with search, scrape, research, docs, spreadsheets, ZoomInfo
data, CRM, email, Slack, LinkedIn, and Outreach tools all QA'd and production-ready. Ryan
Stevens moved web search and email agents into batch UDP mode, enabling workbooks to call
an infinite number of cells for enrichment through a queue-based approach. The new agent
architecture supporting more accurate view creation with ZoomInfo and Salesforce columns is in
final testing, with deployment targeted for today to address one of the platform's biggest
accuracy gaps.

Cost & Performance Optimization: Lars Vedo and the engineering team are actively working
to address the cost concerns that have become a primary sales barrier. Josh implemented
prompt caching improvements currently in testing, with a PR ready for deployment. The team is
exploring advanced patterns including orchestrator architecture refinements to reduce context
passing between agents, which directly impacts both latency and cost. Ryan Stevens
emphasized the focus on cost reduction will yield latency improvements as a byproduct, with
initial efforts targeting the removal of unnecessary thinking tokens in React loops and reducing
average iteration counts from 3-4 down by at least one iteration. This work is critical as internal
feedback and sales team concerns indicate that credit costs are currently the biggest obstacle
to customer adoption.

Context Service & MCP Integration: Rowan Bailey completed the Q4 roadmap rework for
GTM Context, consolidating several months of conversations into a unified direction. The
updated microsite and proposed manifest for external MCP integration are now ready, with
documentation covering implementation paths from internal to external tools. A significant
technical milestone was achieved when ChatGPT was successfully connected as a third-party
orchestrator over the MCP, though side-by-side comparisons with Claude revealed completely
different interpretations of the same prompts. The team is now working to normalize the
experience across orchestrators through improved tool descriptions and will initiate the process
to get listed in OpenAI's directory next week. Lars Vedo's team also implemented a citation
pattern that MCP tools can now adopt, with Josh documenting the approach for broader team
adoption.

Strategic Challenges

Hallucination rates in Copilot chat are concerning, with Robyn Sablosky's testing revealing
approximately one in three interactions producing hallucinated responses. This accuracy issue
requires immediate attention as it directly impacts user trust and product reliability. The root
causes are being investigated through prompt analysis and access to LangSmith spaces, with
Carlos Nunez coordinating an effort to establish a replicable evaluation framework. The team
has smartly narrowed the initial scope to focus on reducing hallucinations as a measurable goal,
rather than the broader and harder-to-measure objective of "making the agent more intelligent."
Christian and the ML team are being brought in to establish KPIs around agent performance,
with clear metrics planned for tracking improvement over time.
The sales team's nervousness about value selling AI credits is creating friction in go-to-market
efforts. Rather than positioning the platform based on value delivered, the sales organization is
approaching conversations as cost reduction exercises, asking how to discount credits and
emphasize low pricing instead of demonstrating transformative capabilities. This mindset
represents a significant barrier to successful enterprise sales, as the team has built genuinely
impressive technology that generates visible excitement in demos. Adam Smith noted that while
cost optimization is important, the real issue is helping sales teams shift from defensive pricing
discussions to confident value demonstrations. The upcoming focus on cost reduction should
help address sales confidence, but cannot come at the expense of product quality or the
compelling user experience that currently generates strong customer reactions.

The Pulses initiative reveals organizational alignment gaps, with multiple teams developing
parallel solutions without a unified architecture. Derek Osgood is working on event-based
triggers through the Blaze system, Robyn Sablosky received requirements for a
recommendation engine to surface daily insights, and various product teams are
conceptualizing Pulses differently across Copilot Workspace, GTM Studio, and other surfaces.
Adam Smith identified that the A2A message broker architecture documented six months ago
for the Workflows product redesign needs to be pulled forward and unified across these efforts.
Without consolidation, the team risks building four different versions of Pulses that don't
integrate well, creating fragmented experiences and technical debt. This requires immediate
leadership attention to align all stakeholders on a single pulse system architecture that serves
as the foundation for all implementations.

Strategic Insights

Key Learnings & Discoveries

The launch week provided critical real-world validation of the platform under actual customer
load. The AI credits system exercised successfully, revealing baseline usage patterns that
inform future optimization efforts. More importantly, the team gained concrete understanding of
where the product excels and where it struggles. The demo path with True Context
demonstrated the platform's ability to deliver genuine wow moments when properly
orchestrated, with artifact creation and semantic data integration creating tangible value that
prospects immediately recognize. However, Victor had to work around several UI friction points
to achieve this result, highlighting specific areas requiring polish rather than wholesale changes.

Third-party orchestrator integration revealed important insights about architectural flexibility.
When ChatGPT was connected as an external MCP orchestrator alongside Claude, the two
systems interpreted identical prompts completely differently and presented results in distinct
formats. This discovery validates the team's early architectural decision to provide abstraction
layers rather than tightly coupling to specific LLM behaviors. The challenge now is finding
middle-ground clarity in tool descriptions that work well across multiple orchestrators without
over-optimizing for any single one. This learning also reinforces that MCP tools should align to
conceptual jobs the AI performs rather than REST API-style object structures, requiring a shift in
how the team thinks about tool design.

Carlos Nunez's work on evaluation frameworks highlighted the importance of scoping problems
precisely. Ryan Stevens' proposal to focus specifically on reducing hallucinations rather than
broadly "improving intelligence" provides a measurable, actionable target. This approach of
reducing complex AI improvement challenges to specific, quantifiable metrics represents a
methodology the team should apply to other optimization efforts. The pattern of starting with
narrowly defined goals, establishing clear measurement, and iterating based on data will be
crucial as the platform scales and handles increasingly diverse customer use cases.

Cross-Team Dependencies

Collaboration with Carlos Nunez's platform teams has been essential for progress this week.
The front-end engineering resources Carlos helped provision are now picking up Human in the
Loop work and embedded chat kit implementation. Brett's contribution as a PM supporting the
semantic data and agentic platform work proved invaluable, with Ryan Stevens emphasizing
that the launch wouldn't have been possible without this support. The design team collaboration
on unifying chat experiences across products demonstrated effective cross-functional work, with
clear alignment on entry points, embedding patterns, and shared UI components now moving
into implementation.

The GTM Data Store team relationship requires ongoing attention, particularly around the
company data model for config data and the new offerings concept being introduced. Carlos
Nunez noted some holdups in reaching agreement on schemas, which is blocking the GTM
Config UX work even though Tomer has end-to-end screens ready. A demo is planned for
November 15th, but will write to a local database until the data model alignment is resolved.
This dependency could delay downstream consumers of account briefs and offerings from
testing the new objects in their applications, suggesting the need for a focused alignment
session with Linda, Majed, and the GTM Store leadership.

Looking Ahead

The immediate priority for next week is getting the new agent with improved view creation
capabilities deployed to production, which addresses one of the platform's most significant
accuracy gaps. Simultaneously, the cost optimization work must continue with urgency, as sales
team confidence depends on demonstrating manageable credit consumption patterns. Lars
Vedo and Ryan Stevens will balance these two critical paths while ensuring no regressions in
the production environment that could undermine early customer trust.

Derek Osgood will shift focus to AI credits implementation in the Double-Zero workspace, with
Ryan Stevens offering to pair program on a simple pattern that should integrate cleanly. Rowan
Bailey will turn attention to GTM Config loose threads, working with Aadhi to finalize design
patterns for one-to-many mappings and other configuration challenges. The team will also
initiate the OpenAI directory listing process for the MCP integration, leveraging Dominic's
existing partnership conversations to smooth the path if needed.

Srivatsa Marthi will finalize November stories for the triggers system, getting both front-end and
back-end teams fully implementing toward the early December launch. The discussion with
Carlos Nunez and Derek Osgood around aggregation at the play level versus GTM Store level
needs resolution to avoid duplicated effort. Carlos will continue advancing the semantic data
service backend roadmap for GCP migration while working with the team to establish replicable
tests ensuring consistency as models change. The new office hours ritual Lars Vedo is
establishing for platform builders should help accelerate adoption across the broader
engineering organization as more teams begin leveraging the agentic capabilities.

Source: Team Intelligence Operating Framework entries from [November 3, 2025 - November 7,
2025], Monday standup transcript (November 3), and Friday DAI meeting transcript (November
7)
