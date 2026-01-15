---
id: weekly-copilot-2025-46
title: "GTM Workspace (Copilot) Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

SalesOS/Copilot Executive Roundup -
[Nov. 10, 2025- Nov. 13, 2025]

Executive Summary

Sean Walter is preparing for three-week paternity leave (starting Nov. 20th) and completing
handoff documentation for critical Copilot Workspace initiatives. The team achieved important
momentum on Pulses with a 4,000-seller survey launched and Next Best Actions (NBA) agent
now live in production via the Orchestrator. However, backend capacity constraints--particularly
on the apps team absorbed by GTM Data Model POC work--threaten December delivery
timelines for artifacts and chat-to-views functionality that Victor identified as essential for
demonstrating Workspace's 10x value over Copilot V1.

This Week's Progress

Key Momentum Areas

Copilot Workspace Pulses validation accelerates with field research. Ant is planning to
distribute a comprehensive survey to a 4,000 frontline sellers this week covering pulse types,
alert preferences, and configurability requirements. This field validation ensures Pulses--the
keystone initiative for Workspace--solves real seller needs rather than assumed requirements.
The team is using both quantitative survey data and qualitative voice feedback through Vapi to
validate the 40+ out-of-the-box pulse concepts currently defined. Ant also conducted deep-dive
sessions with Sri on signal gaps and with Robyn and Carlos on flexible account prioritization
scoring (APS), addressing major gaps that limited Copilot V1 adoption. He also shared a
comprehensive document framing the problem, gaps, and suggested approaches to take for full
coverage of ownership/territory and signal weighting by persona.

ZoomInfo Intent strategy advances with Zero Config architecture and enablement
materials. Harinath completed a comprehensive one-pager and prototype for AI-powered Sales
Enablement within Copilot Workspace, secured stakeholder alignment on Zero Config
requirements with the GTM Offering team (meeting scheduled with Aditya), and continued
LLM-as-judge validation work for Intent Recommendation quality improvements. While the
primary Data Science contact remains on PTO, Harinath's evaluation framework successfully
identified specific Intent signal categories where recommendations excel versus areas needing
improvement, providing actionable input for Phase 1 enhancements once the team reconvenes.

Admin Zero Experience makes final preparations for production release. David's Admin
Defined Territories feature pushed final UI tweaks to production staging, targeting
Monday/Tuesday feature flag opening for the main November release. The team completed Info
Packs documentation and additional upload templates while working through MCP integration to
open territories into the agentic layer. David also advanced Priority Accounts work with initial UX
designs for CRM rules socialized across the Context team, though progress was slowed by
urgent customer escalations requiring developer attention.

Goals & Progress

Copilot Workspace: The team made significant strides across multiple fronts this week. Gabe
addressed bulk emailer technical dependencies and created a one-pager proposing an
alternative approach after learning the task queue dependency will prevent meeting December
timelines. Adam took over the Workspace Agent standup from Lars, analyzed 20+ failure points
in chat accuracy, and moved Priority Fields work toward completion (targeting hotfix deployment
shortly after the 11/18 release). Dylan built five new artifact templates with Jen's review, made
progress on Brand Fetch POC for corporate slide branding, and navigated Cisco's Gong iframe
escalation by identifying technical limitations requiring Gong product work. The homepage
refresh went live Monday with improved pill adoption, and Ant successfully connected the NBA
sub-agent to the Orchestrator--a major milestone delivering far superior output compared to the
previous implementation.

ZoomInfo Intent: Harinath completed multiple deliverables including the Sales Enablement
one-pager with prototype, Zero Config requirements document, and LLM-as-judge evaluation
framework for Intent Recommendation Phase 2. The main blocker remains the Data Science
contact's PTO preventing final alignment on quality enhancement priorities, but comprehensive
analysis has been completed and shared. Harinath also met with Aditya from the Offerings team
to finalize GTM Config alignment for Intent clusters and Account Fit Score (AFS), identifying key
misalignments around offering limits that require strategic discussion with Victor about how to
support unlimited offerings when downstream features have restrictions.

Admin Zero Experience: David completed final Admin Portal UI tweaks for Admin Defined
Territories, which are now in staging and ready for Monday/Tuesday feature flag opening. The
MCP work to open territories into the agentic layer continues but faced delays due to urgent
Workbooks tasks and KTLO issues--expected to resume next week. On Priority Accounts,
David made meaningful progress prototyping CRM matching rules using the new GraphQL
interface from GTM Data Model, though the Context team (Robyn, Ardi) is pursuing a different
approach using AI to work through CRM data, creating a need to align on how both approaches
work together for customers with and without CRM data.

Additional Initiatives: Mobile development continues progressing toward the December 1st
internal alpha, with native chat implementation nearly complete and the team making strong
design progress with Katya. Gabe's sequences work hit a temporary slowdown due to platform
dependencies on Plays/Pulses, but he's coordinating with Adam Smith on roadmap
reassessment. Dylan advanced forecasting prototypes based on last week's session with Jen
and initiated conversations about CSS branded guides for artifacts leveraging the Brand Fetch
API. Victor spent significant time demoing to customers and sales leaders, gathering firsthand
friction points--the key insight being that Workspace must demonstrably show 10x improvement
over Copilot V1 to justify AI action credit expansion, with studio-to-workspace activation
emerging as the most successful demo despite not being polished yet.

Strategic Challenges

Backend engineering capacity constraints threaten December artifact and chat-to-views
delivery. The apps team's most senior engineers are heavily absorbed by the GTM Data Model
POC, creating a significant bottleneck for critical Workspace features. Ryan Stevens' team is
working on bulk emailer, chat-to-views, and other initiatives that Victor identified as essential for
demonstrating Workspace's value, but capacity limitations forced Sean to pull back on some
view improvements and non-urgent user feedback. The chat-to-views functionality is particularly
important since "the feed" continues to be the most coveted demo path despite known utilization
issues, and while Pulses represents the long-term solution, an intermediate "feed/artifact" view
of Views could address sales team feedback in the near term. Sean will need conversations with
Nebo and Ryan to clarify what can conceivably be delivered by year-end.

Orchestrator platform transition introduces latency concerns for chat accuracy
improvements. The 00 team's supervisor agent architecture with sub-agents is expected to
deliver quantum leap improvements in chat accuracy and reasoning, but this comes at the cost
of increased latency due to the additional supervisor step. Sean shared Workspace's set of key
queries with the 00 team, but the team needs to understand latency expectations for common
queries like "tell me about Dominic Fasher"--will responses take 10 seconds, 35 seconds, or
longer? Adam is working to establish current baseline performance and will need to collaborate
closely with the 00 team to ensure the UI experience remains best-in-class as accuracy
improves. This tradeoff between reasoning capability and response speed requires careful
product decisions about which queries warrant the supervisor overhead.

Data Science program management gaps slow Intent AI improvement velocity. Both Ant
and Harinath noted difficulties with Data Science follow-ups and tracking, with Harinath
specifically blocked this week by a key contact on PTO. Sean suggested exploring program
management support to help coordinate the numerous Data Science initiatives (Intent
recommendations, APS integration, chat accuracy improvements, NBA quality) without creating
a heavyweight process. The team needs someone to help manage the growing backlog of Data
Science requests, track deliverables, and maintain momentum across multiple workstreams.
Harinath's successful LLM-as-judge evaluation framework and comprehensive Phase 3 Intent AI
requirements demonstrate the quality of product-side preparation, but execution velocity
depends on Data Science capacity and coordination.

Strategic Insights

Key Learnings & Discoveries
Studio-to-Workspace activation resonates strongly with customers despite lacking
polish. Victor's field research this week revealed that the most successful demo is the
studio-to-workspace activation flow, which generated over 100 meetings booked in Laser's org
alone. Sales leaders are "incredibly excited" about this capability not because it's flashy or
polished--it's not yet--but because it resonates with their customers' actual workflows. This
validates the platform convergence strategy and suggests the team should prioritize making this
activation path reliable and repeatable over investing in purely cosmetic improvements. The
customer resonance indicates this workflow solves a real pain point around operationalizing
GTM intelligence, making it a higher-leverage investment than many other features currently in
flight.

Workspace value demonstration requires showing 10x improvement over Copilot V1 to
justify AI action credits. Victor's customer conversations revealed the core challenge: Copilot
Enterprise customers aren't charged AI action credits for V1 functionality (creating emails,
asking account questions), which enabled many deals to close. Now that Workspace requires AI
action credits, customers and sellers need to see dramatically better capabilities to justify both
the new cost model and the risk of adopting AI in enterprise contexts. Victor emphasized this
isn't about incremental improvement--it requires side-by-side screenshots where users say "this
is 10x better, totally worth the AI action credits." This frames December roadmap prioritization:
features must demonstrably advance the "why Workspace is 10x better than V1" narrative or
address critical workflow blockers preventing users from experiencing that value.

Early chat accuracy improvements show promise but require systematic testing
frameworks. Adam's takeover of the Workspace Agent standup and analysis of 20+ failure
points revealed that current testing relies heavily on "vibe testing" rather than robust evaluation
frameworks. While Carlos and Ryan's eval framework should be finalized within days, the lack
of production testing access creates inefficiencies. Adam noted that many problems only
manifest with real production data and complex CRM scenarios, suggesting the team needs
better tooling for engineers and PMs to test against realistic customer configurations. The move
toward giving Adam direct access to Langsmith playgrounds for rapid prompt iteration
addresses this, but it highlights a broader need for production-representative testing
environments.

Cross-Team Dependencies

Our work with Data Science on Intent AI improvements and APS integration continues to be
essential for competitive differentiation against 6sense and DemandBase. Harinath shared
comprehensive LLM-as-judge evaluation results identifying specific quality improvement
opportunities, but final alignment on Phase 2 implementation roadmap is blocked by the primary
contact's PTO. Ant's work on account prioritization for Pulses requires close coordination with
Robyn's team, whose APS approach that may not fully address Workspace use cases spanning
territory managers with 2,000 accounts to named account managers with 15 enterprise
accounts. Sean suggested exploring dedicated sync time or program management support to
improve Data Science coordination velocity without creating heavyweight process overhead.
The GTM Data Model integration represents both a major opportunity and a significant
capacity constraint. Andres and the platform team showed enthusiasm for solving previously
discussed gaps around write-backs and field access, with the POC appearing feasible for
December delivery. However, this work is absorbing the apps team's most senior
engineers--the same people on the critical path for chat improvements, bulk emailer, and
chat-to-views. Sean, Gabe, and Adam all noted this bottleneck, with Sean emphasizing the
need for a consolidated list of GTM Data Model requirements and a view of how this looks
across the application. David's Priority Accounts work depends on understanding how to
federate GTM Data Model with Advanced Search, adding another layer of coordination
complexity.

Looking Ahead

Next week's primary focus centers on finalizing November 18th release preparations while
managing Sean's upcoming paternity leave handoff. The team will complete final testing and
smoke checks for Admin Defined Territories production deployment, finish Priority Fields work
for post-release hotfix, and ensure Dylan's artifact templates and Brand Fetch integration are
ready for customer-facing release.

Critical path items include: (1) Sean completing his three-week handoff documentation by end of
week with individual PM conversations already scheduled; (2) Ant delivering the end-to-end
Pulses steel thread showing day-one experience, system learning, user pulse creation, and
admin pulse integration from Studio; (3) Adam finalizing the create view experience designs for
engineering handoff; (4) Gabe's one-pager on bulk emailer alternative approach to enable quick
proof-of-concept work; and (5) Victor, Ant, and the broader team aligning on the Pulses vision in
tomorrow's meeting to ensure unified execution.

December delivery depends on resolving backend capacity constraints and making hard
prioritization decisions. Sean's conversations with Nebo and Ryan about feasible December
scope need to happen soon, particularly around artifacts/aha moments, workbook activation,
and chat-to-views--the features Victor identified as most important for renewal conversations.
The team must balance the long-term architectural work (GTM Data Model integration,
Orchestrator platform migration) against near-term features that demonstrate Workspace's 10x
value proposition. With Sean out for three weeks starting November 20th, clear ownership of
these prioritization decisions and the ability to make pragmatic scope tradeoffs will be essential
for maintaining momentum through year-end.

Source: Team SalesOS/Copilot Operating Framework entries from [Nov. 10, 2025- Nov. 13,
2025]
