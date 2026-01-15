---
id: weekly-gtm-studio-2025-46
title: "GTM Studio Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

GTM Studio Executive Roundup

Week of November 10-14, 2025

Executive Summary

ROI Analytics encountered a DevOps blocker with GTM Data Store migration that pushed the
GA release target to January, while Arun's team is trending red on January delivery for
Workbook, Workspace, Agentic Chat, and AI Credits ROI due to dependency teams not
committing timelines--the Agentic Chat team won't prioritize instrumentation until end of
November, and Workbook/Workspace teams haven't confirmed when they can pick up work
despite having all dependency tickets created in Jira. Workbooks remains on track for January
M4 Data Management Foundation delivery with Ash completing segment and dedupe design
handoffs while kicking off ideal user journey research, plus advancing the Waterfall POC with
second-round designs and legal alignment completed ahead of the Bethesda onsite. Plays
deployed the M1 proof of concept to staging and is pivoting to enhance M2 scope after design
workshops with Sneh, Karthik, and Derek revealed the need for better preview and governance
experiences rather than rushing a half-baked product, with Mohan leading iterations on test run
capabilities and credit consumption controls that don't exist in DoubleO today. Data
Management is progressing across all three active milestones with Corina's team validating the
V2 Data Health Scan with customers while kicking off front-end development, plus advancing
the AI onboarding steel-thread narrative that connects data health visibility, configuration setup,
and ongoing management into an end-to-end experience.

Key Momentum Areas

Plays Infrastructure Proves Technical Foundation While Design Pivots to Enhanced
Experience: The team successfully deployed DoubleO plays proof of concept to staging,
demonstrating that workflows can execute within GTM Studio's interface. Multiple design
workshops this week with Sneh, Karthik, and Derek surfaced valuable feedback leading to a
strategic pivot--rather than rush workbook-to-play activation alone, the M2 scope will include
enhanced preview and governance experiences that DoubleO lacks today. Mohan's team is
iterating on test run capabilities that let users validate plays with dummy inputs before full
execution, plus designing credit consumption controls and notification flows that apply to both
one-off and real-time runs.

Data Management Foundation Completes Design Phase and Kicks Off Development:
Ash's team handed off segment and dedupe designs this week while wrapping resolution screen
wireframes, concluding the generic M4 wireframe phase. The team kicked off ideal user journey
research to optimize the long-term UX after following an "unblock now, refine later" pattern to
maintain January delivery momentum. For Workbooks, engagement-based workbook
requirements are complete and ready for engineering handoff, while the Waterfall POC
advanced significantly with second-round designs, legal clearance from James and the content
team on partnership obligations, and final design review scheduled for Monday ahead of the
Bethesda onsite.

Data Health Scan V2 Validates Metrics with Real Customer Data: Corina's team shipped V2
of the Data Health Scan proof of concept this week, which matches exactly what will be built in
GTM Studio and enables deep validation of metrics with customers before production
development. The team met with multiple customers and internal stakeholders who provided
strong validation with no surprising feedback, while front-end development officially kicked off.
The biggest learning was around filtering capabilities for customers with multiple subsidiaries in
one CRM--Andres' team already built this in Advanced Sync, so once available, the Data
Health Scan will automatically filter to show only relevant records based on tenant ID.

Goals & Progress

Workbooks

Progress - January M4 Foundation on Track with Design Handoffs Complete: Ash's team
remains on track for January M4 Data Management Foundation delivery, completing segment
and dedupe design handoffs this week while beginning ideal user journey research to fine-tune
the UX beyond the "unblock now, refine later" approach that maintained engineering
momentum. Resolution screen wireframes need one more week due to complexity but don't
impact the January timeline since engineering isn't ready to begin that work yet. For Workbooks,
the Waterfall POC progressed significantly with second-round designs complete, legal and
branding alignment secured with James and the content team, and final design review
scheduled for Monday ahead of next week's Bethesda onsite to secure organizational
alignment. Engagement-based workbook requirements are complete and ready for engineering
handoff.

Strategic Challenges - Engagement Data Use Case Requires Clear Scoping Before
Release (Clear path forward): The engagement-based workbook use case being advertised
comes with significant caveats since it won't include User Preferences (UP) functionality at
launch, creating potential data and functionality risks if released without clear constraints
defined. The requirements have been handed off multiple times over the past six months, and
Ash is scheduling a meeting Monday with the engagement data team to establish exactly when
this capability arrives and what limitations exist. The team recognizes that releasing
engagement data workbooks without proper UP integration means users won't have the privacy
controls and data governance they expect, so the path forward is to clearly document these
limitations and determine if the use case should wait for UP or launch with explicit caveats to
customers.

Plays
Progress - M1 POC Deployed to Staging While M2 Scope Pivots to Enhanced Experience:
Mohan's team successfully deployed the DoubleO plays proof of concept to staging this week,
demonstrating that the technical foundation works--users can execute DoubleO workflows
directly within GTM Studio's interface. The team conducted multiple design workshops with
Sneh, Karthik, and Derek that surfaced valuable feedback leading to a strategic pivot for M2
scope. Rather than rushing workbook-to-play activation alone to early access customers in
January, the team will include enhanced preview and governance experiences that DoubleO
lacks today. Neha's team finalized the November tools priority list, resolved all P0 bugs in
staging testing, and successfully onboarded the DoubleO service into Backstage for proper
release ticket approval workflow. The team is also working through React versus Angular
front-end implementation approach, with clearer direction emerging after the decision to send
users to a dedicated plays area rather than using an overlay experience.

Strategic Challenges - Preview and Governance Experiences Need Iteration Before
January Launch (No additional action required): The design workshops revealed that DoubleO
workflows don't support true test run capabilities today, creating a wonky experience when
customers want to validate plays with dummy inputs and make changes before full execution.
Mohan's team is actively iterating on preview flows that let users see results for the first 10
records before running jobs on full workbooks, plus designing governance experiences around
notifications, credit consumption controls, and audit trails that apply to both one-off and real-time
runs. The team is also working through where filtering capabilities should live--the current
thinking is that filtering stays on the input side (workbooks) while plays focus purely on
orchestration steps. These iterations are happening now with continued design reviews
scheduled with product leaders to lock in the enhanced M2 scope, keeping the team on track for
meaningful early access readiness in January without rushing incomplete functionality.

ROI Analytics

Some customers may highlight `they were unaware if opportunity data was being shared
with ZoomInfo': ROI analytics is a product that makes it very obvious to the admins of our
customers that we are looking at their Opportunity data from the CRM sync. Brahm and Andres
got pulled into a customer escalation this week (BBSI), where the customer highlighted that they
do not like the fact that ZoomInfo is looking at their Opportunity data (as a public company, that
can carry risks). Based on an investigation from the platform team, we realized that this
customer was in the cohort of `auto-on' email messages that were sent out earlier in the year.
This specific admin had not received the email apparently. They requested for opportunity data
to be immediately deleted from our GTM DM tables and Analytics tables (resolution in
progress). The key learning here is that some customers may not be aware that their CRM
Advanced Sync was `auto turned on', but the ROI product will make this obvious. This is
something for us to be mindful of and ensure that we are covered from a legal perspective on
what we sync and how.

Progress - GTM Data Store Migration Issue Resolved But Testing Timeline Extended:
Arun's team fixed the DevOps issue blocking GTM Data Store migration--the problem was with
loading data into SingleStore after 20-30 minute runs, and the team now has the data
pre-aggregating correctly. The cutover for beta customers is planned for mid-next week, but the
extended troubleshooting means the team needs about a month of validation testing after
cutover, pushing the GA release target to January instead of the original December 9 timeline.
For the M4 Self-Serve Analytics work, Arun enabled the capability in two tenants in the
pre-production environment and is collecting feedback from AMs and CSMs.

Strategic Challenges - Workbook, Workspace, and AI Credits ROI Trending Red for
January Due to Dependency Team Prioritization: The team is trending red on January
delivery for ROI across Workbook, Workspace, Agentic Chat, and AI Credits because four
dependency teams haven't committed timelines despite having complete gap analysis and all
dependency tickets created in Jira. The Agentic Chat team explicitly confirmed they can't
prioritize the instrumentation work until end of November, while Workbook and Workspace
teams haven't provided any timeline for when they can pick up their portions. The P0 blockers
are clear: for Workbooks, the team needs a copy of BigTable data moved to Snowflake or ZDP
(resolving this would unblock 99% of the work), and for Workspace, more than half of the CTAs
are missing Amplitude instrumentation while views-related data needs moving to
Snowflake/ZDP. Additionally, 60% of workspace metrics aren't persisted in the backend, forcing
reliance on Amplitude events which creates hit-or-miss data quality. Arun is scheduling a call
with Adam, Lars, Ryan, and Jessie this week to review requirements for Agentic Chat, Credits,
and Workspace, which should surface remaining gaps and drive commitment from source PM
and engineering teams for CFA to meet the January timeline.

Data Management

Progress - V2 Data Health Scan Validates with Customers While Front-End Development
Kicks Off: Corina's team shipped V2 of the Data Health Scan proof of concept this week, which
matches exactly what will be built in GTM Studio and enables deep metric validation with real
customer data before production development. The team met with multiple customers and
internal stakeholders, receiving strong validation with no surprising feedback--customers
confirmed the metrics are directionally correct, and the focus shifted to QA-ing the actual data
calculations against what customers see in their CRMs. Front-end resources from Denis
Levkov's team are now identified and kicked off development work for the Data Health Scan in
GTM Studio. For Milestone 5 (AI Onboarding), Corina finalized the steel-thread narrative
showing the end-to-end flow where customers see the Data Health Scan, purchase data
management, experience AI-assisted onboarding for initial configuration setup, then return
weeks later to see new issues in the Data Health Scan and get AI help addressing them--all
connecting with Ash's M4 configuration and job execution work.

Strategic Challenges - Filtering Capability Already Being Built by Platform Team for
Multi-Subsidiary Customers (No additional action required): The biggest learning from
customer validation was that some customers like Randstad have multiple subsidiaries
(Randstad Nevada, Randstad Canada, Pareto Law) using the same CRM but with different
ZoomInfo tenant IDs, and they only want to see data for their specific subsidiary in the Data
Health Scan. Andres' team is already building this filtering capability in the Advanced Sync
section, so once available, the Data Health Scan will automatically show only companies and
contacts related to the customer's specific tenant based on their filtering configuration. The team
just needs to QA and test this capability when it ships, but no additional work is required since
the platform team has this handled. This reinforces that as the product scales, having robust
filtering at the platform level prevents each feature team from building one-off solutions.

Strategic Insights

Key Learnings & Discoveries

Enterprise Customers Want More Flexibility, Not Less, as They Scale with Data
Management: Meeting with internal RingLead users and Matt Williams this week revealed that
as customers become more confident with data management capabilities, they actually want to
fine-tune their matching logic more precisely rather than accept out-of-the-box configurations.
This contradicts the common assumption that RingLead is "too flexible" and challenges
suggestions to make everything completely automated with no configuration options. IBM
discussions reinforced this pattern--the most sophisticated enterprise data management teams
at companies investing millions into their data practice appreciate the ability to perfect their
matching rules. The implication for AI Data Management is clear: the MVP onboarding can
guide mid-market customers through best-practice configurations, but the long-term product
must preserve flexibility for enterprise customers to customize as they mature, balancing
complexity with usability rather than sacrificing one for the other.

Plays Must Solve Orchestration, Not Just Provide Another AI-Powered Spreadsheet:
Running numerous sales calls over the past two weeks with the new platform narrative validated
that the go-to-market AI platform story is landing well with customers, but a clear gap emerged
on the operations side. Sneh observed that when the team shows up with Studio's
audience-building capabilities, customers see another AI-powered spreadsheet rather than true
orchestration capabilities that close the loop on their workflows. The feedback reinforces why
getting plays into production quickly matters--customers need to see how Studio doesn't just
build lists but actually orchestrates actions across their go-to-market systems. This insight is
driving the team's focus on ensuring the January early access release includes meaningful
activation patterns beyond basic exports, with preview and governance experiences that
demonstrate true workflow automation rather than just data preparation.

DoubleO Workflows Don't Support True Test Runs, Requiring New Preview Experience
Design: Design workshops for plays revealed that DoubleO workflows lack proper test run
capabilities today, creating a wonky experience when customers want to validate automation
with dummy inputs before executing on full datasets. Mohan's team is designing new preview
flows that show results for the first 10 records so users can fine-tune play configurations before
committing credits and running full-scale jobs. Additionally, the team decided that for one-off
workflows with fixed datasets, filtering capabilities should remain on the input side (workbooks)
while plays focus purely on orchestration steps, rather than mixing data preparation with
execution logic. This architectural decision keeps concerns properly separated and ensures
plays can scale to support multiple input sources beyond workbooks without creating tangled
dependencies.

Cross-Team Dependencies

ROI Analytics Needs Source Team Prioritization for January Workbook, Workspace, and
AI Credits Instrumentation: Arun's team has complete gap analysis done and all dependency
tickets created in Jira for Workbook, Workspace, Agentic Chat, and AI Credits ROI, but four
source teams haven't committed timelines for the instrumentation work needed to hit the
January release. The Agentic Chat team explicitly stated they can't prioritize until end of
November, while Workbook and Workspace teams haven't provided any dates. The specific P0
blockers are: (1) Workbooks needs BigTable data copied to Snowflake/ZDP which would
unblock 99% of the work, (2) Workspace needs Amplitude instrumentation for more than half of
CTAs plus views-related data moved to Snowflake/ZDP, and (3) 60% of workspace metrics
aren't persisted in backend, forcing reliance on hit-or-miss Amplitude events. Arun is scheduling
a meeting this week with Adam, Lars, Ryan, and Jessie to review requirements and surface
remaining gaps, but the team needs explicit prioritization commitments from Jagannath for
Workbooks, Sean and Adam for Workspace, and Lars for Agentic Chat to meet the January
timeline.

Semantic Enrichment Coverage Issues Require Root Cause Investigation from Search
Team: Jagannath's team continues encountering coverage problems with semantic enrichment
where only 50-60% of requests return results, even for accounts where conversation
intelligence data definitely exists (like Alex Lazer's accounts that have documented
conversations but semantic queries came back empty). The team spent 6-7 hours building the
studio-on-studio marketing campaign list for RNG and encountered numerous blockers with
semantic not returning expected results, forcing workarounds through the UI. The technical
troubleshooting is complex and visibility into root causes remains limited, creating concern that if
the product team struggles to understand why semantic fails, customers will find it even harder
to diagnose. Jagannath needs Rowan's search engineering team to investigate the pipeline and
surface where coverage breaks down, plus define clear expectations for what match rates
customers should expect so the product team can set proper expectations rather than promising
capabilities that don't consistently deliver.

Looking Ahead

Next Week Centers on Bethesda Onsite to Align Plays Architecture and Audience
Building Integration: The team is converging in Bethesda for a focused working session to
drive alignment on two foundational questions for plays: (1) the technical architecture for how
agentic platforms come together to support orchestration, and (2) the product experience for
audience building through plays where list creation should always route through Studio's
workbook capabilities rather than plays pulling data directly from sources like CRM reports.
Jagannath, Mohan, Karthik, Ryan, and Adam will workshop the agentic orchestration engine
integration, while the broader team will prototype how audience building interfaces with plays to
create an end-to-end flow from list creation through activation. Sneh is focused on getting
crystal clear sign-off on exactly which plays the team will support first and ensuring everyone is
locked in on those priorities coming out of the onsite.

ROI Analytics Dependency Alignment and Data Management Design Reviews Dominate
the Week: Arun is driving meetings with Adam, Lars, Ryan, and Jessie to review
instrumentation requirements for Agentic Chat, Workspace, and AI Credits, with the goal of
surfacing all remaining gaps and securing timeline commitments from source teams to unblock
the January delivery. For Data Management, Brahm's focus is conducting design reviews across
both M4 foundational capabilities with Ash and M5 AI onboarding with Corina, ensuring Brandon
Tucker's team and other internal stakeholders provide feedback on the resolution screen and
ideal user journey work. Corina continues circulating the V2 Data Health Scan to prioritized
accounts and AMs for validation, while front-end development progresses on bringing the scan
into GTM Studio for the January demo date.

Plays M2 Scope Finalization and Front-End Implementation Approach Drive Toward
January Readiness: Mohan's team is iterating on preview and governance experience designs
based on workshop feedback, with continued design reviews scheduled with product leaders to
lock in the enhanced M2 scope that includes test run capabilities, credit consumption controls,
and notification flows beyond basic workbook-to-play activation. The team is also finalizing the
front-end implementation approach (React versus Angular) now that the decision to send users
to a dedicated plays area rather than an overlay experience provides clearer technical direction.
Architecture reviews continue with Tushar, Michael, and the DoubleO dev team to ensure the
design scales beyond early milestones to support data orchestration across different app areas.
Neha is working through the outreach integration to have it in staging by Tuesday, completing
the framework for adding prospects to sequences and enabling email functionality that rounds
out the M1 tools library.
