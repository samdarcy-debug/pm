---
id: weekly-dai-2025-39
title: "DAI Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: dai
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

DAI Executive Roundup - [Monday
September 22nd, 2025 - Friday September
26th, 2025]

Executive Summary

Copilot Workspace achieves 45% activation rate among newly enabled AEs/AMs, with
foundational chat-view functionality now fixed and ready for broader internal rollout.
Victor's team successfully pushed critical user experience fixes to production, resolving trust
issues where chat was incorrectly accessing multiple views instead of focusing on the user's
current context. The recommendation is to activate all AEs and AMs company-wide on October
1st, expecting 400-500 active users based on current engagement patterns. Salesforce
partnership momentum accelerates with an MOU in hand for their new prospecting application,
positioning ZoomInfo data as a core component of their AI-first sales cloud strategy.

This Week's Progress

Key Momentum Areas

Copilot Workspace rollout validation exceeded expectations with strong user
engagement and rapid iteration cycles. Victor's team added 100 AEs/AMs to the platform this
week, achieving a 45% open rate despite end-of-quarter timing. The most valuable discovery
was that users consistently gravitate toward three fundamental use cases: prospecting through
chat, creating views via natural language, and cross-account opportunity analysis. Sean and
Lars prioritized fixing the core chat-to-view communication issue, ensuring users can trust that
their queries focus on their specific book of business rather than pulling data from irrelevant
views.

Salesforce partnership reached significant milestone with signed MOU and Dreamforce
announcement potential. Ali's team secured formal partnership documentation for integrating
ZoomInfo data into Salesforce's new AI-powered prospecting capability, replacing their failed
Prospecting Center product. The collaboration involves building a workspace-like experience
directly into Salesforce's sales cloud, with OAuth integration and freemium model starting at
10,000 credits. This positions ZoomInfo as the primary data source for Salesforce's agent-first
sales strategy while opening new distribution channels.

Product marketing engine demonstrates cross-product asset generation capability
through real GTM team deployment. AJ's team launched a sophisticated content creation
agent that synthesizes foundational messaging from Adam's context service materials, Molly's
brand narrative, and product-specific positioning documents. Carl's marketing team began using
the system immediately, enabling self-service content creation while maintaining message
consistency. The agent reduces manual context gathering that previously consumed significant
PM and marketing resources, with built-in quality controls through dedicated content hub
channels for each Tier 1 product.

Goals & Progress

GTM Studio: Major validation wins emerged from early access customers, with Indeed
expanding from $1M to $1.7M ACV and committing to a $5M three-year deal based on ROI
analytics capabilities. Brahm's team completed GTM data store migration with only minor issues
identified, bringing GA timeline within reach. The semantic enrichment agent shows strong
performance for data enhancement tasks, though list-building capabilities require constraint
refinement. Core September release features including CRM unblocking, signal-based
workbooks, and job postings data are on track for production deployment September 23rd.

AI Context Service: Adam completed comprehensive narrative packages including talk tracks,
demo flows, and AI credits positioning for Dreamforce readiness. The messaging emphasizes
context service as the foundation enabling intelligent agent behavior across ZoomInfo products,
with clear pricing structure through usage-based AI credits. Secondary focus on unified
roadmap alignment with Derek and Karthik for 00 plays integration, establishing clear milestone
delivery through December steel threads.

Vertical Datasets: Brandon's team achieved production readiness for franchise dataset with
strong customer validation from March Networks and Aflac, the latter budgeting $500K
expansion after successful pilot results. Self-serve flywheel partner onboarding flow nears
completion with Audi delivering strong PRD and process documentation. Target pipeline
suggests 50-100 partners by year-end could significantly expand data acquisition capabilities
and improve person resolution rates across the platform.

Strategic Challenges

Cross-functional coordination complexity emerges as systematic bottleneck requiring
process standardization. Multiple teams report extended timelines when navigating legal,
security, and engineering stakeholder alignment, particularly for data partnerships and API
externalization efforts. Brandon's analysis shows current partner onboarding takes 6+ weeks
from intent to signature, overwhelming smaller partners with enterprise-focused security
processes that may not match the risk profile of data acquisition partnerships. The pattern
repeats across multiple workstreams, suggesting need for centralized escalation pathways and
risk-appropriate process frameworks.

Agent-based list building capabilities face fundamental UX challenges that require
architectural resolution. Both Copilot Workspace and GTM Studio teams independently
discovered that users struggle with open-ended natural language queries for data discovery,
despite strong performance on enrichment and analysis tasks once lists exist. Brahm's team
found that seemingly simple requests like "show me accounts good fit for data cube X" involve
complex multi-dataset operations that current agent planning cannot effectively decompose. The
solution requires iterative plan validation with users before execution, fundamentally changing
the interaction model from single-shot queries to multi-step workflows.

API-first development discipline needs reinforcement to support expanding integration
and MCP roadmap. Ali identified risk that teams are building MCP schemas on top of internal
APIs rather than designing external-grade APIs first. This pattern could create technical debt
similar to historical UI-first development approaches. With GraphQL API gateway requiring data
platform team ownership due to API infrastructure team capacity constraints, the November
timeline for external API availability faces resource allocation challenges. Frank's review
capacity as sole API quality gatekeeper creates additional bottleneck requiring certified
reviewers to scale validation processes.

Strategic Insights

Key Learnings & Discoveries

User behavior patterns reveal fundamental preference for progressive disclosure over
single-shot AI interactions. Victor's analysis shows that Copilot Workspace users consistently
succeed with advanced features like buyer engagement maps and account planning, but
struggle with basic view creation. This counterintuitive finding suggests users need scaffolding
for open-ended tasks while accepting complexity for structured workflows. The pattern extends
to GTM Studio where enrichment agents significantly outperform manual processes, but
list-building requires constraint definition. This insight should inform agent UX design principles
across all products, favoring step-by-step guidance over attempting complete task automation.

Partnership integration velocity becomes competitive differentiator requiring operational
scaling. Brandon's competitive analysis reveals that current partner capacity operates at 10-20x
below required scale for market positioning. The Salesforce partnership demonstrates value of
embedded integration over standalone product approaches, while flywheel partner opportunities
suggest contributory network effects could significantly improve core product capabilities. The
learning emphasizes need for productized partnership flows that can handle high-volume,
low-touch integration requests without overwhelming operational teams.

Context quality trumps context quantity for agent effectiveness across all use cases.
Adam's foundational work on context service messaging reveals that successful agent
implementations depend more on curated, relevant context than comprehensive data access.
This applies to user-specific models like hot leads (requiring sales history and territory
understanding) and enterprise use cases like dynamic ICP scoring (requiring tenant-level
configuration and behavioral data). The implication for GTM data model evolution and user
context storage becomes critical for competitive differentiation as AI-first sales tools proliferate.
Cross-Team Dependencies

Our work with Salesforce on integrated prospecting capabilities requires close coordination
between Ali's partnership team, Adam's context service development, and Victor's workspace
UX patterns. The integration timeline depends on GraphQL API gateway completion by Majed's
data platform team, while demo readiness for Dreamforce requires alignment between Adam's
messaging work and Victor's user experience validation. Success metrics depend on seamless
handoff from partnership development to product engineering to GTM enablement.

Engineering resource allocation across 00 plays development creates critical path
dependencies between Adam's roadmap definition, Ali's workflow platform assessment, and
Sneh's GTM Studio integration requirements. The December delivery timeline requires unified
architectural decisions on deterministic versus AI-driven workflow execution, actions registry
design, and human-in-the-loop automation frameworks. Mark Frail's workflow team capacity and
Derek's integration expertise represent key constraint points requiring careful coordination.

Looking Ahead

October 1st marks pivotal moment for internal Copilot Workspace adoption with
company-wide AE/AM activation planned, contingent on successful resolution of
chat-view communication issues. Victor's team will leverage end-of-quarter timing to
maximize user onboarding when sales team focus returns to daily productivity tools. Success
metrics include 400+ active users within two weeks and positive qualitative feedback on core
use cases, setting foundation for external customer rollout planning.

Dreamforce preparation intensifies with context service positioning as cornerstone of
ZoomInfo's AI platform story. Adam's messaging framework positions context as the enabling
layer that transforms generic AI agents into business-intelligent sales tools, while Ali's
Salesforce partnership provides concrete proof point of integration value. The demonstration will
showcase MCP integration with Claude while maintaining sellable positioning despite product
not being immediately quotable. This balance requires careful message coordination between
partnership potential and current product capabilities.

H2 execution accelerates across multiple fronts with GTM Studio GA timeline firming,
vertical datasets scaling, and foundational infrastructure investments paying dividends.
The combination of strong customer validation (Indeed expansion), partnership momentum
(Salesforce integration), and operational improvements (PMM engine automation) creates
compound effects supporting ambitious year-end targets. Key risks center on resource
coordination and maintaining product quality while scaling multiple initiatives simultaneously,
requiring continued focus on cross-team alignment and systematic process improvement.
Source: DAI Executives Operating Framework entries from [September 22nd, 2025 - September
26th, 2025]
