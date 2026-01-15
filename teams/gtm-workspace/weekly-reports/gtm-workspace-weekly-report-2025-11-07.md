---
id: weekly-copilot-2025-45
title: "GTM Workspace (Copilot) Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

SalesOS/Copilot Executive Roundup -
[Nov. 3, 2025- Nov. 6, 2025]

## Executive Summary

Sean Walter delivered a refocused roadmap addressing the GTM Data Model pivot while Adam
Severance pushed significant chat accuracy improvements live behind feature flags for 25% of
users. Workbook activation has emerged as the most requested demo flow from sales teams,
requiring potential scope adjustments as this becomes the primary sales motion. GTM Data
Model integration is absorbing capacity from senior engineers who are also critical for chat
improvements, creating resource tension that needs resolution. Zero Config progress advanced
with Harinath Krishnamoorthy establishing Intent Clusters as the bridge between GTM Offerings
and Copilot configuration, while MCP server development for Intent data began to enable both
Workspace integration and external LLM access.

## This Week's Progress

### Key Momentum Areas

Copilot Workspace chat accuracy received its largest quality improvement to date, with
Adam Severance shipping dozens of prompt refinements addressing semantic ambiguities,
SFDC navigation issues, and tool call failures. The improvements are going live behind feature
flags for a % of users, with expanded testing planned before full GA. This addresses the #1 user
complaint about chat not understanding account/opportunity context correctly, directly impacting
the core Workspace experience that sales teams are now demoing to customers.

ZoomInfo Intent data integration into Workspace advanced through MCP server
architecture, with Harinath Krishnamoorthy completing technical discovery that identified two
implementation paths: MCP server attachment (higher capability) versus direct field addition
(available today). Lars and the Agentic team confirmed MCP as the preferred approach,
enabling both natural language queries for Intent data and external LLM access for customers
wanting to use Intent signals in Claude or ChatGPT. This positions ZoomInfo ahead of
competitors like 6sense by making Intent data accessible across customer workflows.

Zero Config requirements achieved breakthrough architectural clarity when Harinath
Krishnamoorthy identified Intent Clusters as the natural bridge between GTM Offerings and
Copilot configuration. Rowan and the GTM Config team validated this approach, which
eliminates manual topic selection during onboarding by automatically recommending topics
based on what products/services customers sell. This directly addresses the 2-3 week
configuration delay that increases early churn risk and enables day-one value delivery.

## Goals & Progress

Copilot Workspace: Major progress on multiple fronts including chat accuracy overhaul
(dozens of improvements live in staging), CRM update UX finalization (API contracts in
progress), and email sequencing solution alignment (cross-team review scheduled). Dylan
Halladay built five new HTML artifact templates and advanced slides artifact capability with POC
for corporate deck recreation. Sean Walter completed the sales-ready 3-month roadmap and
initiated GTM Data Model requirements documentation with meetings scheduled with Andres'
team. The 2K limit experience improvements and recommended filters work shipped, though
Views functionality remains constrained by API-call architecture pending GTM Data Model
migration.

ZoomInfo Intent: Harinath Krishnamoorthy completed technical discovery for Intent in
Workspace, establishing MCP server as the implementation path with dual benefits: Agentic
platform integration and Enterprise API exposure for customer LLMs. Zero Config architecture
defined using Intent Clusters to bridge Offerings data, enabling hyper-personalized topic
recommendations at first login. Data Science pipeline validation continues after bug fixes, with
LLM Judge evaluation framework in development using production data. Intent
Recommendation Phase 2 validation work partially complete with final feedback summary
delivery pushed to next week.

Admin Zero Experience: David Goulden finalized documentation and info packs for Admin
Defined Territories GA release, though video recording delayed until developer returns from
vacation. MCP development for opening territory definitions to Agentic layer progressing but
slower than desired. Priority Accounts work continues with GTM Data Model query testing
showing some scalability concerns, requiring alternative approach. UI designs for admin tuning
of CRM matching rules completed and ready for circulation. Engineering team remains heavily
constrained by customer escalations and Workbooks-related priorities.

Additional Initiatives: Gabe Pirela advanced multiple initiatives including CRM update designs
(engineering feedback incorporated), email sequencing requirements refinement (cross-team
review scheduled), and Workspace desktop app (security review complete, targeting week of
11/17 for internal release). Ant Cuomo distributed pulses product brief and is sourcing feedback,
with call scheduled with Sri to align on out-of-the-box pulses from signals pipeline. Concept and
UX iterations for pulse continue with Ryan McMaster. Homepage refresh design finalized with
engineering kickoff completed, targeting delivery before 11/18. Mobile prototype socialization
continues ahead of design resource allocation. Profiles NBA agent iterations ongoing to ensure
proper JSON formatting and output rendering.

## Strategic Challenges
Resource contention between short-term UX fixes and GTM Data Model migration is
creating difficult prioritization decisions for the Workspace team. Sean Walter flagged that
temporary improvements to address current direct/API SFDC integration limitations are
absorbing significant capacity from the same senior engineers needed for GTM Data Model
work. The 2K limit issues, grouping improvements, and filter enhancements all require
medium-to-large development efforts, yet the team faces the prospect of "throwaway work"
knowing GTM Data Model migration will replace this architecture. Adam Severance emphasized
users are currently taking the hit while the team debates how much to invest in improvements
that may become obsolete in months.

Workbook activation flow has emerged as the critical demo motion but lacks the polish
needed for consistent success, according to Sean Walter's assessment after observing
multiple sales demonstrations. This workflow--where users activate Studio workbooks into
Workspace--is increasingly what prospects want to see, yet current implementation has friction
points affecting demo quality. Sean noted this may require bumping priority higher and making
compromises elsewhere, though he explicitly wouldn't compromise on chat improvements or
pulses work. Victor Oliveros confirmed this is being demoed heavily by the enterprise sales
team but questioned breadth of adoption across the broader field organization.

Evaluation framework gaps are stifling Chat Accuracy improvements, as Adam Severance
discovered during this week's improvement sprint. An evaluation framework exists but isn't
scaled to comprehensively test all edge cases, and isn't accessible to the Workspace Product
team. Ryan Stevens and Carlos Nunez's teams are making rapid improvements-- with new
data science hires now in the mix-- but timeline for product team access is still unknown. This
has created a "death by a thousand cuts" scenario where small failure points are getting through
to Production (e.g. semantic ambiguity handling, tool call failures, drift, SFDC navigation issues),
oftentimes only visible with live SFDC data. To help resolve, the team has flagged the new
agent and is slowly expanding internal access to facilitate A/B testing between old and new.

## Strategic Insights

### Key Learnings & Discoveries

Intent Clusters function as a natural "Rosetta Stone" between products, a key architectural
insight from Harinath Krishnamoorthy's Zero Config work this week. Rather than building
separate mapping tables for each offering-to-topic relationship, Intent Clusters already represent
"collections of topics for business interests"--exactly what GTM Offerings describe. This pattern
of finding existing abstractions that capture relationship semantics rather than creating
integration-specific data structures could apply to other cross-product scenarios like AFS
models mapping to CRM fields. The GTM Config team's immediate enthusiasm for this
approach validates that manual configuration is a friction point affecting multiple teams,
strengthening the business case for Zero Config investment.
MCP server architecture provides dual strategic value: internal Workspace integration
plus external customer LLM access. Harinath Krishnamoorthy's technical discovery revealed
that building MCP for Intent solves two problems simultaneously: enabling natural language
Intent queries in Workspace while allowing customers to access ZoomInfo Intent data in Claude,
ChatGPT, or other LLM environments. This transforms ZoomInfo from a destination application
to an embedded intelligence layer, directly addressing the "AI-native enterprise software"
competitive landscape where customers expect tools to work in their preferred AI workflows.
ZoomInfo already published MCP servers for contact and company data; adding Intent creates
a powerful arsenal while 6sense and DemandBase remain walled gardens.

Workbook activation represents a fundamental shift in how customers want to
experience Workspace, per Sean Walter's observation after watching multiple demos. Rather
than starting fresh in Workspace, prospects want to see how their existing Studio workflows
translate and activate. This validates the platform convergence strategy but also exposes that
the current implementation isn't demo-ready for this primary use case. Victor Oliveros' question
about breadth of adoption (is it just the enterprise sales team or the entire field?) is critical--if
this becomes the standard demo motion, resource allocation must adjust accordingly even if it
means compromising other initiatives.

## Cross-Team Dependencies

Our work with the GTM Data Model team on Workspace integration continues to be critical for
eliminating current SFDC limitations. Sean Walter documented comprehensive requirements
covering data needs (objects, SLAs, filtering, sorting), integrations (write-backs, reads), and
initiated conversations with Andres, Mark, and others for a December POC. However, this work
is pulling the same senior engineers who are critical path for chat accuracy improvements,
creating resource tension that Victor Oliveros and engineering leadership need to resolve. The
team cannot sacrifice chat quality for data model work, yet both are essential for Workspace
success.

David Goulden's Priority Accounts work with the Platform and Enterprise Search teams revealed
fragmentation in how Target Accounts and Priority Accounts APIs are currently structured.
Cross-team discussions continue on how to access GTM Data Model CRM data in Search, with
potential need for API wrapper simplification. The broader vision involves AI-assisted setup to
reduce admin manual work while maintaining configurability, requiring alignment between
David's work, the Platform team, and Enterprise Search. Territories as a cross-platform object
for Search/Intent/WebSights also needs decision framework, as customers continue requesting
this expansion.

## Looking Ahead

Next week's focus centers on finalizing the 11/18 release while advancing foundational work for
December's GTM Data Model integration POC. Sean Walter will complete the internal roadmap
artifact for downstream teams and finalize GTM Data Model requirements through Friday's
meeting with Andres' team--critical since this affects all Workspace areas from views to profiles
to chat.

Key priorities include: Dylan Halladay finalizing slides artifact release plan and gathering internal
user feedback on current feature-flagged version; Gabe Pirela completing CRM update designs
handoff to engineering and driving email sequencing solution alignment through cross-team
review; Ant Cuomo advancing pulses definition through call with Sri on out-of-the-box signals
coverage and collecting survey feedback on alert types/frequency/configurability; Adam
Severance expanding chat accuracy improvements to 25% of users while continuing work on
views improvements and GTM expansion conversations. Harinath Krishnamoorthy will finalize
Intent MCP server requirements, complete Data Science pipeline validation after bug fixes, and
advance Zero Config implementation plan with offerings-based recommendations.

The team faces a critical balancing act between delivering visible 11/18 improvements (artifacts,
views polish, homepage refresh) that counter customer objections as sales begins demoing to
prospects, while not losing momentum on foundational work (GTM Data Model integration, MCP
architecture, Zero Config) that enables the world-class experience Victor Oliveros emphasized
the product must achieve. Resource constraints remain the primary limiting factor, particularly
around senior engineers pulled between immediate UX fixes and architectural migrations.

Source: Team SalesOS/Copilot Operating Framework entries from [Nov. 3, 2025- Nov. 6, 2025]
