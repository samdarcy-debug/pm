---
id: weekly-gtm-studio-2025-44
title: "GTM Studio Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

GTM Studio Executive Roundup

Week of October 27 - October 31, 2025

Executive Summary

The week before our November 3rd launch proved decisive as all workstreams converged on
release readiness. Workbooks completed field enablement sessions covering foundations,
competitive positioning, and demo deep dives while finalizing product briefs, demo videos, and
new import/enrich modals to showcase our data ecosystem breadth. Plays pushed the initial
release to staging with workflow creation flows operational and began finalizing the M1 testing
plan, though front-end restyling work stands at 50% complete heading into the final week. ROI
Analytics verified GTM Data Store backfilled historical data in the dev environment, with the
CFA team planning cutover to the new data store by November 12th--giving three weeks to
validate everything ahead of the December 9th GA release--while multi-currency support
completed testing in staging and moved toward production deployment. Data Management
prioritized the next batch of 10 accounts with account managers for data health scan outreach,
completed PRD review for the M3 GTM Studio version, and kicked off development work,
though front-end resource allocation from Denis' team remains the primary execution
dependency.

Key Momentum Areas

Field enablement accelerated GTM readiness across all customer-facing teams:
Jagannath, Tanvi, and Sneh ran comprehensive enablement sessions this week covering GTM
Studio foundations for the broader field, competitive positioning with dedicated Clay objection
handling, and SC/CX demo deep dives. The sessions equipped solutions consultants with
production-ready demo paths and gave account managers the narrative and data points needed
for customer conversations. Customer cohort workbooks analyzing use case fit went live, with
VPs activating these to their teams alongside a dedicated prospecting block on Monday,
November 3rd--moving strategy directly into execution.

November 3rd release scope locked with go/no-go decisions finalized: Jagannath and the
team made critical scope decisions on semantic enrichment (go--scalability achieved), deep
research (go as available but limited scale), and studio chat enhancements (complete and in
production). The clarification step improvement now forces the agent to present multiple solution
options when user intent is unclear, significantly improving UX based on early user feedback. All
P0/P1 bugs for copilot activation were addressed for release readiness, with enablement
materials delivered to the GTM team.
Data management feedback driving rapid POC iteration: Corina and the team iterated the
Data Health Scan POC to v2.0 based on feedback, adding key enhancements including
benchmark comparisons, business impact explanations for each metric (e.g., "21.1% missing
job titles prevents decision-maker segmentation"), and person-moved tracking. Customer
Success showed strong interest in using these reports for churn prevention, creating a dual
motion: account management for upsells and customer success for retention and increased
adoption.

Goals & Progress

Workbooks

Progress - Launch readiness materials finalized and production demos operational: All
product briefs, walkthrough videos for signals, pitch content, compete objection handling, and
how-to guides reached near-completion status requiring only final polish. Sneh, Tanvi, and the
enablement team ran field-wide sessions while solutions consultants confirmed
production-ready demo paths with template workbooks created specifically for customer use
cases. New import and enrich modals were finalized with Alex and the design team to better
showcase ZoomInfo's data ecosystem breadth, while the team began incorporating account
priority score (APS) into the enrichment flow through quick-turnaround requirements and design
collaboration.

Strategic Challenges - Semantic enrichment coverage and enablement depth require
continued attention (Clear path forward): While semantic enrichment achieved the scalability
needed for go-live, data coverage and quality concerns remain for post-launch iteration, with
identified gaps in how the feature handles four distinct states: data available with answer, data
available but no answer found, semantic data unavailable, and downstream service failures.
The last two states create user confusion by returning empty cells with no differentiation.
Enablement across field, support, and SC teams needs strengthening as many lack clear
understanding of what semantic enrichment is, how it works, and how it differentiates from
standard enrichment. AI credits releasing on November 3rd means the first real-world
production testing happens on launch day itself, creating unknown unknowns. The redesigned
enrich catalog will deploy behind a feature flag with 20+ connectors available in the production
tenant, with global publishing timeline still to be determined. Workspace activation delivers the
core story but remains bare bones, requiring rapid iteration cycles post-launch to maintain seller
confidence.

Plays

Progress - M1 milestone deployed to staging with core workflows operational: Neha and
the engineering team successfully pushed the PR to staging, making GTM Plays accessible
with the feature flag enabled. Core user flows including creating workflows from scratch, adding
tools and custom agents as workflow nodes, and running for single inputs are functioning
properly. End-to-end testing for M1-supported tools shows Salesforce and CRM tools fully
operational, while Gmail sending works though read/search remain blocked, and web search
tools function correctly. The team finalized the testing plan covering all M1 functional flows and
began QA coordination, while front-end CSS and styling changes progressed to approximately
50% completion with Wednesday as the target date for completion.

Strategic Challenges - Tool completeness and front-end restyling pace require close
management through launch week (No additional action required): While core functionality
reached staging successfully, end-to-end tool testing revealed mixed results requiring continued
attention. LinkedIn scraper needs additional work to fetch company and contact profile
URLs--estimated at roughly one day of effort but not yet complete. The team also identified
routing as a new tool requirement critical for supporting inbound and outbound use cases,
kicking off early discovery work that must be carefully managed against the November 3rd
timeline. Front-end restyling work standing at 50% with a Wednesday deadline means the final
48 hours will be tight. Tool documentation for QA and internal users is being collated to ensure
alignment on supported operations and use cases, critical for smooth production deployment
planned for early November with phased rollout starting with product team testing.

ROI Analytics

Progress - GTM Data Store migration validation on track for December GA with
multi-currency testing complete: Arun and the platform team completed verification of
backfilled historical data in the dev environment, with the CFA team planning cutover to the new
GTM Data Store by November 12th. This timeline provides three weeks to validate everything
comprehensively ahead of the December 9th GA release. Multi-currency support completed
exhaustive testing in the staging environment and is ready for production deployment, initially
rolling out to beta customers next week. Discovery work began on unifying workbook,
workspace, plays, and AI credits into a consolidated ROI framework, with discussions held with
the DoubleO team and Adam's team to understand how to correlate everything to sales
outcomes and efficiency metrics.

Strategic Challenges - Workbook instrumentation prioritization blocks embedded
analytics progress (Clear path forward): The instrumentation and pipeline setup process from
workbook data sources has not yet been prioritized by Jagannath and Randy, creating a
dependency that must be resolved this week to maintain forward momentum on the M3
milestone for Studio and Workspace ROI analytics. Several open questions remain around how
the embedded workbook analytics agent artifact should update each time it loads, preventing
finalization of the engineering execution plan. The team continues discussions with Jesse and
others to establish the unified framework for communicating ROI more effectively across all
GTM Studio components, with next steps requiring clearer scope definition around workspaces
Q4 analytics following Adam's roadmap clarification.

Data Management
Progress - M1 prototype refinement and M3 development kickoff advance dual-track
execution: Corina and the team completed version 2 of the data health scan proof of concept
incorporating customer and account manager feedback including person-moved metrics,
benchmarks showing comparison against ZoomInfo's internal CRM data, and enrichment match
rate projections demonstrating potential fill rate improvements. The team prioritized the next
batch of 10 accounts with high renewal potential in H1 for targeted outreach, using projected
upsell value based on record counts to focus on strategic accounts first. Customer Success
showed strong interest in using reports for churn prevention and increased adoption, creating a
new retention-focused motion alongside the upsell strategy. For M3, Corina completed the PRD
review for bringing data health scan into GTM Studio, kicked off development work, and secured
front-end resources from Denis' team.

Strategic Challenges - Front-end resource confirmation and logic specification need final
validation (Clear path forward): While Denis' team assigned front-end resources, final
confirmation is still needed to ensure no execution gaps as development ramps up. The team is
working this week to button up the exact logic and requirements for benchmarks, enrichment
match rates, and other calculations to ensure engineering teams have precise specifications
matching what's already built and tested on the data services side. Brandon Tucker's Friday
feedback session surfaced valuable input on person-moved metrics and other enhancements
that Corina is documenting and incorporating where feasible for the January release. The
narrative validation with account managers and customers continues to ensure messaging
resonates and clearly articulates business impact, with version 2 of the prototype expected this
week followed by a larger 600-customer run primarily for Customer Success to use in churn
prevention conversations.

Strategic Insights

Key Learnings & Discoveries

Customer Success identified churn prevention application creating dual revenue motion:
Customer Success teams expressed strong interest in using data health scan reports for
accounts approaching renewal, discovering a use case beyond the original account
management upsell strategy. They want to understand what packages customers purchased,
track credit usage and remaining balance, then use the data health scan to spot gaps--for
example, showing a customer with 40% job title fill rates and a million unused credits, then
helping them enrich that data to increase adoption. This creates complementary motions:
account management for upsells to new customers, and customer success for retention and
deeper adoption with existing customers.

Workspace activation naturally connects to Plays in seller conversations but requires
clear product distinction: During enablement sessions, account managers organically began
framing workspace activation as "Plays" when talking to customers, validating the strategic
direction but creating pressure to clarify product positioning. View publishing solves specific use
cases around making data available to sellers, but the Plays automation engine addresses
fundamentally different needs around process orchestration with actions and real-time
execution. Sellers need tasks and to-dos, not just published views. The team must establish
clear delineation between when customers use view publishing versus when they need full Play
automation, ensuring these capabilities complement rather than compete with each other as
both move toward production.

Early access program reveals need for use case templates and starter guidance:
Customers consistently request more guidance on workbook use cases and starter templates,
with many feeling overwhelmed by available data and functionality without clear starting points.
Of the 22 early access accounts, only 4 are healthy and getting value, with an additional 3
seeing value but stuck without activation paths. Users want to see what other customers are
building for creative ideas and need structured onboarding showing them what's possible. The
request for use case templates emerged strongly across multiple customer conversations,
indicating a gap between product capability and customer ability to ideate and execute
independently.

Cross-Team Dependencies

GTM Data Store opportunity history data validation remains in progress (No additional
action required): Andres Perez and Asaf's platform team completed the backfill of historical
opportunity data, which Arun verified in the dev environment. The CFA team continues
validation work on data accuracy and quality, with results expected by Monday and a switchover
plan to be finalized by end of week. This dependency is actively being worked through
established channels with clear ownership and timeline, enabling the December 9th GA target.

Semantic enrichment infrastructure migration to Google Deep Search service (Clear path
forward): Deep research infrastructure needs to move from Mellifera to Google's Deep Search
service to improve coverage beyond the current 60-70% result rate. Ryan Steven indicated this
is minimal work, with the team planning to execute the migration next week while early users
continue getting value from the MVP version. No additional intervention required as the path
forward is established and scheduled, though the team will monitor whether 60-70% coverage
proves sufficient for initial launch based on customer feedback.

Front-end resource allocation for M3 Data Health Scan in GTM Studio: While Denis' team
assigned front-end developers, final confirmation of resource availability and allocation is
needed to ensure development work can progress without gaps. Corina is working directly with
Denis and the assigned developers to lock in capacity and timelines, with resolution expected
this week to maintain the January delivery target for bringing data health scan into GTM Studio.

Looking Ahead

November 3rd launch week demands field focus and rapid iteration cycles: With product
going live Monday, the entire team shifts focus to supporting customers, sales teams, and
solutions consultants as they begin using GTM Studio in production at scale. This means
maintaining tight feedback loops with the field, triaging incoming bugs and issues quickly,
coordinating fixes across engineering teams, and identifying quick wins that can be deployed
rapidly to address friction points. Tanvi will focus on UI stories for queue management, stopping
runs, and running single row/column/cell operations while continuing design progress on find
contact enhancements. Jagannath prioritizes onboarding early access customers to new
capabilities, migrating deep research to new infrastructure if not completed this week, and
locking in December 1st release scope with engineering.

ROI and Data Management execution accelerates toward year-end milestones: Arun will
finalize the approach for workflow embedded analytics POC and start instrumentation
discussions with the Workspace team while monitoring GTM Data Store validation results.
Brahm connects with Gabe Sweet's enablement team to ensure all materials are ready for
December rollout and follows up with Mary's implementation team on their role in customer
onboarding. Corina circulates version 2 of the data health scan to the prioritized account list,
validates narrative and benchmarks with account managers and customers, and begins fleshing
out requirements for M5 AI onboarding in collaboration with Urmzd from the machine learning
engineering team. For M3, she works with engineering to finalize logic specifications matching
the tested data services implementation.

December planning and backlog grooming ensure sustained delivery momentum: With
November 3rd scope locked and launching, the team must complete shovel readiness for
December 1st capabilities to maintain engineering velocity. Jagannath leads Jira cleanup and
alignment on prioritized items, ensuring all descoped work from quality focus is revisited and
properly sequenced. Mohan continues driving copilot activation support including bug
identification and quick wins, while finalizing M2 scope for GTM Plays through front-end and
back-end engineering alignment calls focused on December timeline feasibility. Neha onboards
new engineering team members with knowledge transfer sessions alongside Derek and Kartik,
documenting nuanced context to align everyone including product and QA members not
originally from the DoubleO team, critical as the platform scales and more teams contribute.
