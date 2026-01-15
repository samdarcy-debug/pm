---
id: weekly-gtm-studio-2025-45
title: "GTM Studio Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

GTM Studio Executive Roundup Week of

November 3-7, 2025

## Executive Summary

The November 3rd release went live successfully with Studio and Workspace activation now in
production, marking a major milestone as we transition from planning to real-world usage with
sellers actively using the product in live prospecting blocks. Workbooks saw strong field
adoption with revenue leaders activating custom audiences to their sales teams, though
semantic enrichment scalability and data coverage concerns remain open items requiring
continued attention through next week. Plays received critical feedback during the week that the
DoubleO core user experience needs redesign before customer readiness, prompting a pivot in
M2 sequencing to prioritize plays core experience over the original scope, with design
workshops scheduled for next week to align on the new direction. ROI Analytics successfully
completed GTM Data Store validation in staging with the cutover now targeted for November
13th (delayed by 1-2 days for pre-caching), while Arun finalized the Figma prototype for
Milestone 1 instrumentation requirements and began scheduling calls with workspace and
agentic chat engineering counterparts to identify gaps. Data Management made strong
progress with benchmarks complete for the V2 Data Health Scan ready for circulation to
prioritized accounts next week, M3 designs buttoned up with three design partners scheduled
for validation, and M5 steel thread narrative complete showing the end-to-end data
management flow in GTM Studio with AI onboarding designs kicking off next week.

### Key Momentum Areas

November 3rd Release Shipped with Real Seller Adoption: The team successfully launched
GTM Studio and Workspace activation to production on November 3rd, with sellers immediately
putting the product into action during dedicated prospecting blocks. Revenue leaders activated
custom-built workbooks to their sales teams, and the field is now using Studio not just for demos
but as part of actual go-to-market plays. This represents a fundamental shift from building to
delivering measurable business impact, with 47 sales solutions demos already booked in
November alone within one week of prospecting. Sneh noted the tremendous positive energy
from the field and the strong conviction in the problem space we're solving.

Data Management Gaining Commercial Traction: Corina's Data Health Scan prototype
generated immediate pipeline results, with early customer engagement already creating
meetings and advancing $400K+ in active opportunities across prioritized accounts. The team
onboarded approximately 40 AMs who are now equipped with the narrative and data points to
drive upsell conversations, with early wins including meetings secured at Randstad and Palo
Alto Networks based on the scan results. The V2 prototype will validate metrics with real
customer data next week, and M3 (Data Health Scan in GTM Studio) has three design partners
scheduled for feedback on both designs and narrative.

Plays Pivot Toward Better Product Experience: Following the November 3rd release and
deeper evaluation of the DoubleO integration, Mohan and the plays team received feedback
from Sneh and Dominic that the core plays user experience should be the first priority for M2
rather than the original scope. While M1 successfully proved the POC that DoubleO workflows
can run in GTM Studio, the key user flows and experience need redesign before being
customer-ready. This strategic pivot maintains the high-level goal of bringing plays to external
customers in Q1 but re-sequences the execution path to ensure product quality, with design
workshops scheduled for next week to align on the new direction.

## Goals & Progress

Workbooks

Progress - November 3rd Release Deployed with Strong Field Engagement: Jagannath's
team successfully shipped the November 3rd release to production with Studio agentic
capabilities now live, including semantic enrichment (though scalability concerns remain), deep
research enrichment, and the new AI emailer built in-house to replace the original integration.
The release is resonating strongly with customers and internal teams, with the use case artifact
landing particularly well--every customer immediately understands what Studio does when
walking through the three use cases, and the narrative connecting Studio to Workspace
activation is compelling. Tanvi supported the launch by capturing feedback in the backlog sheet,
helping test new create/enrich modals, documenting find contacts problems and user journeys,
and completing discussions with the engineering team on adding APS to workbook enrichment
with a tentative timeline expected next week.

Strategic Challenges - Semantic Data Coverage and Enablement Gaps (Clear path
forward): While semantic enrichment shipped to production, there are open concerns around
data coverage and quality that weren't fully resolved by the November 3rd deadline. The team is
actively working on semantic scaling, but data coverage and quality issues are still being
uncovered. Additionally, enablement across the field, support, and SC teams is weak--there's a
lack of understanding about what semantic is, how it works, and how it's differentiated from
other capabilities. Jagan is continuing to drive improvements in semantic scalability, and the
team recognizes that while these are not blockers to the release, they represent important areas
for rapid iteration based on early production usage. The team also identified that multiple
customers (Udemy, Security Scorecard) have workbook use cases requiring custom CRM fields
but lack the right stakeholders on calls or immediate capacity to configure these fields, creating
friction in early access sessions despite strong customer engagement--once configuration is
completed (as seen with Lucidlink), customers can progress quickly.

Plays
Progress - M1 Delivered to Staging with Pivot to Core Experience Redesign: Karthik and
the plays team successfully delivered M1 to staging, making plays navigation available in GTM
Studio for internal users to test, which represents an exciting milestone for integrating the
acquired DoubleO product into GTM Studio within just a couple of months of acquisition. Mohan
completed enablement materials for the November 3rd Copilot activation release including
PRFAQ, release notes, demo videos, and how-to guides, and all P1/P0 bugs were addressed
for the 11/3 readiness. However, following the release and deeper evaluation, the team received
feedback that the DoubleO core user experience needs significant redesign before being ready
for customers--while M1 proved the POC that workflows can run in GTM Studio, key user flows
around selecting input data sources, designing workflows, and running workflows need
substantial polish and enhancement.

Planning Update - M2 Scope Re-Sequencing for Better Product Experience (Clear path
forward): Following PRD review feedback from Sneh and Dominic, the team is extending the
M2 milestone to Jan to prioritize improving the core plays experience rather than the original
scope. The DoubleO team doesn't have sufficient time to polish the user experience before
moving to other work, leaving several UX gaps around input data source selection, workflow
design, and workflow execution that need addressing. Mohan is scheduling design workshops
for next week to document enhancement areas and align on a new direction for what feels
satisfactory to deliver in M2. This represents a re-sequencing of work rather than a major
strategic pivot--the high-level goal of bringing plays to external customers in Q1 remains
unchanged, but the stepping stones to get there are being re-evaluated to ensure product
quality. The team also identified that AI credit charging behavior for workflow previews needs
further discussion and alignment, as there's a requirement to generate previews free of charge
for the first 10 records but current architecture charges credits when data leaves the system.
We'll parallel path M2 and M3 towards a Jan deliverable date. There are three areas of work:
Backend - scalability (running thousands of workflows in parallel) and infrastructure work
continues as planned; Frontend - we'll prioritize batch run experience in Plays first, then work on
workbook connectivity; M3 - Triggers and Actions has very little dependence on M2 and runs in
parallel.

ROI Analytics

Progress - GTM Data Store Cutover Validation Complete with December GA on Track:
Arun's team successfully completed validation of the GTM Data Store in the staging
environment with no critical issues identified, positioning the cutover for November 13th
(delayed by 1-2 days from the original November 12th target due to pre-caching job
requirements). The team started working on LRT ticket requirements to support the December
9th GA release and made significant progress on instrumentation requirements for Milestone 1,
which covers ROI reporting across Workbooks, Workspace, Agentic Chat, and AI Credits. Arun
finalized a Figma prototype showing the full instrumentation framework and reviewed it with
William Lam for workbooks, with CFA now identifying gaps in workbook instrumentation.
Scheduling is underway with Adam, Lars, Jesse, and other engineering counterparts to review
requirements for agentic chat, credits, and workspace and identify any remaining gaps.
Strategic Challenges - Instrumentation Prioritization and Enablement Message Clarity (No
additional action required): The primary challenge this week centered on getting
instrumentation and pipeline setup prioritized with source teams for both Workspace and
Workbooks, though Brahm is actively working with the relevant teams to ensure these efforts
move forward. Jagan will be prioritizing the instrumentation requirements, and Lars will review
the proposal to confirm feasibility of embedding workbook analytics. Separately, Brahm
identified confusion in early enablement around attribution versus correlation in how the ROI
product is built--the product is designed to show correlation rather than claim attribution of ROI
to ZoomInfo, but many AMs and CSMs new to the product misunderstand this positioning
because most past ROI attempts at ZoomInfo were focused on claiming attribution. This
represents an unlearning challenge that's being addressed through talk tracks with Gabe
Sweet's enablement team, making sure the messaging is crystal clear to avoid defensive "claim
the numbers" discussions that aren't the intent of the product.

Data Management

Progress - V2 Prototype Ready and M3 Design Partners Scheduled: Corina's team
completed benchmarks for the V2 Data Health Scan prototype, incorporating ZoomInfo CRM
data to show customers their current fill rates, benchmark those against industry standards, and
demonstrate potential uplift from enrichment--these benchmarks will be used in both the PDF
V2 version and the GTM Studio M3 design. The V2 prototype is launching next week to
approximately 20 prioritized accounts to validate that metrics align with what customers see in
their CRM, essentially functioning as an in-depth QA session with real customer data. For M3
(Data Health Scan in GTM Studio), Corina updated all requirements to include exact logic so
engineering can pick up the work in a shovel-ready state, and three design partners are
scheduled for next week to validate designs and narrative. For M5 (AI Onboarding), the team
completed analysis of the most common rules used in Ringlead to use as suggestions in the AI
onboarding flow and has a complete steel thread showing the end-to-end user flow from when a
new user clicks on data management through data health scan, purchase, AI onboarding, rule
configuration, and job execution.

Strategic Challenges - Front-End and QA Resourcing Still Open: While engineering
alignment is progressing well with Yamesh identifying names along with Noam and Aran from
different engineering teams, and Guy Levine helping on the QA side with front-end support
being sought from Nebo's team, the specific front-end and QA resources still need to be
confirmed. Brahm noted these are being actively solved for and it's just a matter of identifying
the specific people, but until those resources are locked in, there's some risk to M3 (Data Health
Scan in GTM Studio) timeline execution. The team needs to confirm who exactly will be helping
on the front-end and QA sides so they can be brought into development conversations. That
said, there is a clear path forward with active work underway to resolve this, and no additional
action is required beyond the resourcing discussions already in progress.

## Strategic Insights
### Key Learnings & Discoveries

Use Case Artifacts Drive Customer Understanding: Jagan discovered through customer and
internal team sessions that the use case artifact--which outlines the three primary use cases for
the November 3rd release and maps features to each use case--lands extremely well in every
conversation. Customers immediately understand what GTM Studio delivers when presented
with this structured narrative, and the approach of switching between the artifact and live
product demo while having customers work through examples in real-time creates an effective
training experience. This validates that leading with business outcomes and use cases rather
than features creates much stronger comprehension and engagement, particularly as the
product grows in complexity.

Studio Chat Full-Page Experience is Actually Plays: Jagan had a significant realization
during the week that the full-page Studio Chat experience the team has been exploring is
fundamentally the same problem that plays is solving. Customers go through a series of steps in
their go-to-market work--building exploratory audiences, refining them, moving to actual
audience creation, performing enrichment--and this step-by-step rinse-and-repeat journey is
exactly what plays orchestrates. Rather than having Studio Chat as a separate capability and
plays as another separate thing, these should be unified into one product where the agentic
interface helps users navigate through their go-to-market plays. This insight has major
implications for how the team thinks about the product framework going forward and will be
shared visually with the broader team next week.

Multiple Customers Blocked by CRM Field Configuration Capacity: Tanvi observed across
multiple early access sessions (Udemy, Security Scorecard) that customers have strong
workbook use cases requiring custom CRM fields like "opp score" but consistently lack the right
stakeholders on calls or immediate internal capacity to configure these fields with their CRM
teams. This creates a blocker in progressing during early access sessions despite customer
engagement and interest in the product. Once configuration is completed (as demonstrated with
Lucidlink), customers can move forward fairly quickly. This pattern highlights a customer
behavior and capacity constraint rather than a product issue, but it impacts the efficiency of the
early access program and requires consideration in how the team structures customer
onboarding and enablement going forward.

## Cross-Team Dependencies

Workspace and Agentic Chat Instrumentation (No additional action required): Arun needs
to schedule and complete calls with Adam, Lars, Jesse, and other engineering counterparts
next week to review Milestone 1 requirements for workspace analytics, agentic chat, and AI
credits instrumentation to identify any gaps. Jagan will be prioritizing the instrumentation
requirements, and Lars will review the proposal to confirm feasibility of embedding workbook
analytics. This is actively being worked on with clear next steps, so no additional action is
required.
Semantic Data Coverage and Scaling (No additional action required): While semantic
enrichment shipped to production, Jagan's team is continuing to work on scaling improvements
and addressing data coverage and quality concerns that remain open items. The team is
actively iterating on semantic scaling, so no additional action is required, though this remains an
area of focus for continued improvement through next week and beyond.

## Looking Ahead

Production Feedback Cycles and Field Support: This week marks the shift from building to
operating in production with real customers using GTM Studio and Workspace as part of their
sales motions. The team expects significant product feedback from sellers during their
prospecting blocks and from the broader field as they demo and use the product with
customers. Fast feedback cycles with quick wins and bug fixes will be essential to maintain
momentum and keep confidence high with the sales team who are effectively selling the product
they're using. Sneh emphasized the importance of not being reactive but proactively anticipating
the questions and feedback that will emerge, particularly around ROI reporting and usage
visibility.

Hardening December Release Planning and Plays Core Experience: With the November 3rd
release successfully shipped, the team can now shift focus back to planning and hardening the
December path, which was cooled off during the final weeks of November 3rd preparation. For
plays specifically, next week's design workshops will be critical to align on the new direction for
M2 core experience improvements, determining which enhancement areas to tackle, and
establishing what scope feels satisfactory for delivery. Mohan, Neha, and the plays team will
work through detailed user flows to get M2 scoped at least 80-90% of the way so execution can
start quickly the following week.

ROI and Plays Pressure Points in Demo Narrative: As the team ramps customer
conversations and demos, two specific areas will require focused attention. First, ROI reporting
and usage analytics are consistently the immediate follow-up question after showing the Studio
to Workspace journey--customers want to know how they'll see if their sellers are doing
anything with the activated audiences. Arun and Brahm need to get crisp about the
now/next/later roadmap and potentially leverage early Figma mocks with the solution consultant
team so they have something to show prospects even before features ship, similar to how the
team successfully used design mocks for ROI before product availability. Second, plays
naturally comes up in seller conversations as they discuss workspace activation--the framing
that sales naturally landed on is that pushing audiences to workspace "is plays"--but View
publishing alone isn't the right product for what sellers need, which is tasks and to-dos. The
team needs to be very clear about what use cases View publishing solves versus what will
come with play automation to set proper expectations while selling what currently exists.
