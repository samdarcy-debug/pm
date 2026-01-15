---
id: weekly-intelligence-2025-40
title: "Intelligence Weekly Report - October 03, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-10-03
updated: 2026-01-06
week_ending: 2025-10-03
reporting_period: "September 29-October 03, 2025"
tags: ["weekly-report", "Q42025"]
---

Intelligence Team Executive Roundup -
[September 29 - October 3, 2025]

Executive Summary

The team is on track for the October 6th Copilot Workspace release with AI credits
implemented, Vertex enabled for faster performance, and a stable release candidate locked
down. However, the parallel push for Dreamforce readiness is creating tension--we're
managing two critical deliveries simultaneously, and the team is stretched thin balancing
production stability with demo polish. Key technical wins this week include resolving MCP
integration issues that caused outages and getting the redaction system working for demos. The
workflows versus plays architectural debate consumed significant cycles but should resolve
Monday with engineering leadership input.

This Week's Progress

Key Momentum Areas

Ryan Stevens and Lars Vedo shipped a release candidate for Copilot Workspace with AI credits
fully implemented and tested end-to-end, marking a major milestone toward the October 6th
launch. The team successfully enabled Vertex, which delivers noticeably faster performance
than previous infrastructure, and implemented a demo mode toggle that allows salespeople to
switch between redacted and full data views without disrupting their workflow.

Rowan Bailey made strong progress preparing the external MCP for Dreamforce, pivoting from
a complex ReAct agent wrapper approach to simpler, more reliable tool sets organized around
specific jobs to be done. This pragmatic decision freed up the entire next week for testing and
rep enablement rather than continuing to build unproven architecture. The team validated this
approach through steel thread testing and will onboard 50 reps on Monday.

Carlos Nunez and Rowan Bailey demonstrated a successful experiment enriching product
offerings data using Google grounding, processing 10,000 companies for under $100 in 30
minutes using BigQuery ML with Gemini Flash 2.5. The quality of the enriched offerings data
looks promising and opens up opportunities for competitor relationships, complementary
technology mappings, and improved company core data.

Goals & Progress
Copilot Workspace Release Readiness: Lars Vedo achieved approximately 80% completion
on the production release, with AI credits implemented, Vertex enabled for performance gains,
and the WebSight MCP added for broader data access. A few regressions surfaced around view
context retention and HTML artifact scrolling, but these are tracked for immediate resolution.
The team also implemented self-hosted LangSmith and resolved critical stability issues with
MCP integrations that were causing platform downtime. Sonnet 4.5 testing revealed the model
needs additional prompt tuning for consistent tool selection, which the team will address through
a full agent restack planned for next week.

MCP Tools and Context Service: Rowan Bailey completed roughly 90% of the MCP tooling
preparation for Dreamforce, making the strategic decision to deprioritize wrapping tools in ReAct
agents in favor of better-defined tool descriptions and prompt templates. Testing revealed that
tool descriptions benefit significantly from detailed information about underlying data sources
and appropriate use cases for each parameter. The promotion path from internal tools to
external MCP is now established behind feature flags, enabling the team to equip Dreamforce
demo reps with production access to new capabilities without exposing them to all tenants.

GTM Store Connector and Signal Development: Srivatsa Marthi reached 90% completion on
the architectural design for the GSO to GTM Store connector, with only a couple minor open
items remaining. This connector unblocks the team from building MCP tooling that makes raw
signal data available for agents. During planning discussions with Adam Smith and Rowan
Bailey, Sri identified opportunities to refocus on new signal development including down-funnel
signals, signals based on the absence of events, and contributory network-based
signals--areas that haven't received attention in recent months but align well with the emerging
"Pulses" roadmap concept.

Strategic Challenges

Derek Osgood spent most of the week navigating circular conversations with the Workflows
team about architectural alignment between Workflows and the new Plays system for DoubleO.
The core tension is that the existing Workflows execution engine has fundamental limitations--it
runs on Google Workflows requiring JSON object creation before execution, preventing dynamic
graph navigation and supervisory agent patterns. Carlos Nunez confirmed that while Workflows'
actions and triggers can be reused, the orchestration layer needs to be replaced entirely.
Dominic escalated this Monday with a mandate for engineering leadership to resolve it as an
engineering problem by end of day, which should provide clarity and let Derek move forward
with DoubleO integration work.

Ryan Stevens identified that the new Sonnet 4.5 model, while 2-3x faster than previous
versions, isn't consistently selecting tools correctly with current prompts and is exhibiting higher
hallucination rates. The team discovered this stems partly from extended thinking requiring a
temperature of 1, which introduces more variance by definition. The plan is to restack the entire
agent architecture to enable granular temperature control at the sub-agent level, allowing the
main conversation agent to use lower temperatures while specialized agents like the emailer
can operate with extended thinking where needed. This architectural work is essential for the
quality bar required for customer launch.

The team is managing competing priorities between October 6th production release and
Dreamforce demo readiness, with both initiatives requiring high-quality delivery simultaneously.
Ryan McMaster's name came up repeatedly during the R&D leadership offsite as teams need
design support for multiple novel interfaces including Pulses, Workspace layouts, GTM Studio
consistency, and DoubleO integration. The team acknowledged they effectively need three of
Ryan but will need to prioritize ruthlessly to prevent quality degradation across all workstreams.

Strategic Insights

Key Learnings & Discoveries

The team learned through painful production experience that MCP integrations introduce
significant platform stability risks. When external MCP servers don't respond, they can cause
cascading failures and platform downtime. This discovery led to improved error handling, better
understanding of MCP session management, and more defensive architecture patterns. The
team now has a clearer mental model of what can go wrong with tool integrations and how to
build resilience, which will be critical as more teams adopt the agentic platform.

Carlos Nunez and Rowan Bailey validated that BigQuery ML with Gemini Flash 2.5 can perform
complex batch inference tasks at remarkable cost efficiency--processing 10,000 company
offerings enrichments for under $100 in 30 minutes. This opens up entirely new possibilities for
large-scale data enrichment using Google's grounding capabilities. The team is exploring using
ZoomInfo data as a grounding set for Google's services, which could become a partnership
motion with customers similar to the Deloitte and PwC consultancy plays, where companies
need high-quality business and contact data to ground their AI initiatives regardless of the
specific use case.

Testing revealed that tool descriptions require much more detail than initially anticipated to help
orchestrators make good decisions about which tools to call and when. Generic tool names and
sparse descriptions led to poor tool selection and confused execution paths. The team found
that explicitly describing the underlying data returned, appropriate contexts for each parameter,
and clear boundaries between similar tools significantly improved agent performance. This
insight is particularly important as the platform scales to support multiple teams building their
own agents and tools.

Cross-Team Dependencies

Work with the GTM Config team on account brief generation and structured data alignment
remains critical for Context Service success. Rowan Bailey made progress defining clearer
requirements for GTM Config to support automated brief population, but coordination remains
complex with multiple teams trying to solve overlapping problems from different angles. The
offerings and competitor data model needs attention before structured and unstructured data
can work together smoothly, requiring continued collaboration between Rowan's team, Robin
Sablosky's data science group, and Carlos' ML team.

Platform team dependencies around Real User Monitoring (RUM) and entitlements represent
the biggest risk to customer launch readiness for Copilot. Lars Vedo has these scoped with
epics and tickets lined up for development, but any delays here directly block the ability to
launch to external customers with proper billing and usage tracking. The team needs continued
prioritization and focus from the platform organization to hit the October 6th milestone.

Looking Ahead

Next week splits focus between final October 6th release preparation and Dreamforce
enablement. For Copilot Workspace, the priorities are tuning the agent with updated prompts to
address user feedback, resolving the remaining regressions around view context and HTML
artifacts, and completing the agent restack to enable Sonnet 4.5 with proper temperature
controls. Ryan Stevens will coordinate the release candidate lockdown while Lars drives the
prompt optimization work.

For Dreamforce preparation, Rowan Bailey will spend the entire week on testing and iteration,
onboarding 50 reps on Monday through a kickoff session, establishing a testing feedback
channel, and making quick-turn improvements based on real rep usage. Adam Smith is
handling marketing and go-to-market assets, demo talk tracks with Carl, and coordinating
provisioning into Anthropic for the demo accounts. The team must balance confidence in what
ships to production versus shiny features that might fail during demos--the bias is toward
stability and reliability over novelty.

The workflows versus plays architectural decision will resolve Monday per Dominic's mandate,
which should unblock Derek Osgood to make rapid progress on DoubleO integration and clear
the path for the December 1st trigger plays milestone. Once this decision is made, any
resources not allocated to roadmap items will be redirected to support roadmap priorities,
making it critical that the team ensures all essential work is captured in the final roadmap that
locks Wednesday of next week.

Source: Team Intelligence Operating Framework entries from September 29 - October 3, 2025,
Monday standup transcript, and Friday reflection transcript
