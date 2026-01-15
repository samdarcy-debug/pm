---
id: weekly-data-2025-41
title: "Data Weekly Report - October 10, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-10-10
updated: 2026-01-06
week_ending: 2025-10-10
reporting_period: "October 6-10, 2025"
tags: ["weekly-report", "Q42025"]
---

Data Executive Roundup - [Oct 6, 2025 -
October 9, 2025]

Executive Summary

The data organization successfully unblocked user-level Points of Interest (POI) deployment to
staging this week, positioning the team to enable enhanced signals across Copilot, Workbooks,
and future AI agents. Steve Hutchinson's work overcame previous DevOps constraints that had
stalled progress for weeks. Simultaneously, Igor Kyrylenko expanded the vertical datasets
program by acquiring professional license data from 17 states, establishing the foundation for a
comprehensive national licensing database that extends well beyond the original contractor-only
focus.

This Week's Progress

Key Momentum Areas

Steve Hutchinson broke through technical blockers to advance user-level POI into staging, with
production deployment expected this week or early next week. This unlocks the ability to add
multiple interest types to POI, immediately improving signal relevancy for Copilot homepage and
Workbooks while establishing the data foundation for future AI agent consumption. The system
is designed to support downstream products as they evolve, eliminating a constraint that had
limited the team's ability to serve personalized signals at scale.

Dana Hurtig made substantial progress synchronizing franchise data with the platform,
uploading approximately 353,000 franchisor locations and developing a four-phase plan to
address franchisee company cleanup. The team completed matching for roughly 350,000
franchisor contacts with a 32% match rate to existing contacts, while delivering 2.8 million
enrichments--exceeding the projected target by 25% through 5x5 freemail data. This work
positions the franchise dataset for full integration and customer delivery.

Brandon Wilson built two aggregated datasets for the board meeting demo focused on Copilot
Next (CN) Benchmark Agent insights--Deal Cycle Insights and Win Rate analytics. The team
successfully produced speed signals (whether accounts lean slow, fast, or mixed) for 28 tenants
and resolved naming and grouping issues to understand full deal cycle patterns. This provides
the data foundation needed to demonstrate differentiated benchmarking capabilities that only
ZoomInfo can offer through contributory network participation.

Goals & Progress
Data Infrastructure & User Signals: Steve Hutchinson's user-level POI deployment represents
a fundamental shift in how person-based signals can be delivered across products. After
resolving DevOps constraints, the system is now configured to write the first interest type
(previous engagement) to staging, with production deployment contingent on ZDP approval.
This architecture enables the team to rapidly add facilitators, recommended contacts, and other
interest types that will dramatically improve signal relevancy for Copilot users while supporting
future GTM products.

Vertical Dataset Expansion: Igor Kyrylenko pivoted the professional license initiative from
contractor-only focus to a comprehensive multi-state licensing database, acquiring datasets
from 17 states and building unified source data layouts to standardize processing across
disparate state formats. The team deployed scrapers targeting states with centralized licensing
systems, which yield 3-4 times faster acquisition than fragmented databases. Work also
advanced on the FINRA dataset as a potential Pitchbook replacement, with schema finalization
and quality checks underway. An automated state data acquisition tool with email monitoring
capabilities is in development to eliminate manual bottlenecks in bulk data requests.

Benchmarking & Board Demo: Brandon Wilson completed the Deal Cycle Insights aggregate
table and Win Rate dataset needed for the CN Benchmark Agent board demonstration. The
team filtered data to closed-won opportunities, worked through account naming and grouping
challenges, and successfully generated insights for 28 tenants regarding their deal velocity
patterns. This work directly feeds the differentiated benchmarking capabilities that will drive
contributory network adoption by providing customers with insights unavailable anywhere else in
the market.

Strategic Challenges

The franchise dataset integration revealed more complexity than initially anticipated, particularly
around franchisee company synchronization with the platform. Many franchisee entities lack
URLs and have limited contact coverage, which causes them to appear as low-quality profiles in
the platform despite being valid businesses. Dana Hurtig is addressing this through a phased
approach that processes entities in tranches based on data completeness. Additionally, the
latest Rhetorik batch is failing in the Data Infusion Platform (DIP), requiring engineering
assistance to diagnose and resolve the processing issues before additional EMEA company
infusions can proceed.

The CN-driven agents prototyping faces a resourcing gap--while the agentic platform can
support rapid prototype development, there are no dedicated engineering resources allocated
for moving beyond proof-of-concept stage. Jody Roberts' org chart agent and other data-driven
agents remain constrained to prototypes without more explicit prioritization and engineering
support. This creates a risk that valuable demonstrations will struggle to reach production
deployment and deliver customer value.

Suresh Putteti identified sensitive personal information (social security numbers and credit card
numbers) in assets related to Account AI, specifically within user prompts. While the data owner
is being engaged to develop remediation plans, the discovery highlights ongoing challenges in
preventing SPI from entering systems not designed to handle it. The asset is maintained for
archival purposes, limiting immediate business impact, but establishing a recurring monthly
remediation process will be important for continuous compliance improvement.

Strategic Insights

Key Learnings & Discoveries

The team discovered that centralized state licensing systems provide 3-4 times faster data
acquisition than fragmented databases, fundamentally shifting the professional license
expansion strategy. Rather than pursuing all states uniformly, Igor Kyrylenko is prioritizing states
with consolidated systems, allowing the team to build coverage more rapidly while developing
scrapers and standardized taxonomies. The automated email tool being developed will further
accelerate bulk data requests by eliminating manual attachment collection, creating a scalable
acquisition model for professional licensing data.

Dana Hurtig's franchise work revealed that pre-validation quality checks need significant
improvement to better estimate what constitutes "good" data before infusion. The team
encountered URL inactivity issues affecting approximately 43% of records in LatAM data,
causing profiles to become unpublished despite representing valid businesses. This insight
applies beyond franchise data--many small businesses globally lack working websites but
remain legitimate entities that customers want to reach. The team is developing more
sophisticated validation approaches that assess entity validity beyond simple URL checks.

Brandon Wilson's benchmarking work confirmed that closed-won opportunity data provides
reliable ACV amounts, while open opportunities and closed-lost deals contain unreliable values
that cannot be trusted for analysis. This validation from Steve Hutchinson shapes how the team
approaches deal cycle insights--filtering to closed-won deals ensures data integrity while
accepting some limitations in analyzing in-progress opportunities. The team will need to
leverage GTM Store API datasets for more accurate ACV analysis when expanding beyond
basic deal cycle metrics.

Cross-Team Dependencies

Our work with the DaaS organization on vertical dataset enablement continues to be important
for scaling the motion beyond high-touch strategic accounts. Dow Jones is establishing
recurring one-on-one meetings with sales managers and attending weekly team meetings to
ensure proper enablement and account targeting. The Money 20/20 executive-led outreach
campaign represents a new motion that requires coordination between data, DaaS, and sales
leadership to effectively message vertical dataset value to good-fit accounts. This campaign will
provide important feedback on messaging effectiveness and help refine the repeatable patterns
needed to drive the $10M H2 goal.
The DevOps and ZDP teams were essential partners in unblocking Steve Hutchinson's POI
deployment. After weeks of constraint, their prioritization enabled progress on user-level interest
types that unlock value across multiple products. Going forward, maintaining strong
collaboration with these teams will be necessary as the data organization scales POI to include
facilitators, recommended contacts, and other interest types that power enhanced signals.

Looking Ahead

Next week focuses on three primary areas: advancing POI interest types into production,
continuing franchise dataset integration with full franchisee company processing, and finalizing
professional license data categorization across the 17 acquired states.

Steve Hutchinson will push user-level POI into production for the first interest type while
preparing development work for facilitators and recommended contacts. This progression
enables downstream products to begin consuming enhanced person-based signals while the
team builds out additional interest types. Dana Hurtig will complete franchisee company
infusions following the four-phase plan developed this week, addressing data quality issues
systematically to ensure platform integration doesn't create noise in customer-facing profiles.
The team also needs to resolve Rhetorik DIP failures with engineering support to unblock
additional EMEA company infusions that customers are requesting.

Igor Kyrylenko will categorize and align license types and subtypes across the 17 acquired
states to create a standardized taxonomy, deploy scrapers for 2-4 additional high-priority states
with centralized systems, and finalize the FINRA schema with quality checks and delivery
specifications. The automated acquisition tool for email and attachment functionality will move
into production testing. Brandon Wilson continues refining the Deal Cycle Insights and Win Rate
datasets for the board demonstration, with Dominik requesting sample data. The team is
well-positioned to deliver differentiated benchmarking capabilities that showcase contributory
network value while driving toward customer-facing implementations in Q4.

Source: Data Executive Operating Framework entries from [Oct 6, 2025 - October 9, 2025]
