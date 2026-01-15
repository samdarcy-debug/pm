---
id: weekly-data-2025-38
title: "Data Weekly Report - September 19, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-09-19
updated: 2026-01-06
week_ending: 2025-09-19
reporting_period: "September 15-19, 2025"
tags: ["weekly-report", "Q32025"]
---

Data Executive Roundup - [September
15th - September 18th, 2025]

Executive Summary

GTM.ai successfully launched this week, marking a major milestone in our data marketplace
strategy and publicly showcasing our integrated GTM studio experience. Igor Kyrylenko
completed the franchisor dataset deployment in Snowflake with full traceability, while the team
advanced franchise data automation and expanded multi-brand owner coverage. Dana Hurtig's
team exceeded bad data fix targets by 15% and completed UDB matching for franchisees, with
EMEA company infusions from Rhetorik data positioned for staging review.

This Week's Progress

Key Momentum Areas

The GTM.ai site went live, providing customers with public access to our new data marketplace
and demonstrating the investments we're making to improve data coverage while driving
awareness of our integrated GTM studio experience. This launch positions us well for
expanding our vertical dataset offerings and creates a foundation for more self-service data
interactions.

Igor's completion of the franchisor dataset in Snowflake delivered four production-ready tables
(franchisor, franchisee, location, and contact) with successful ZoomInfo matching and full
lineage traceability. This structured, matched format provides customers with unique visibility
into franchise ownership structures that competitors cannot offer, directly supporting our custom
data acquisition program and enabling sales to pitch differentiated datasets to enterprise
accounts.

Steve Hutchinson progressed user-level POI implementation with the first interest type moving
toward production next week. This foundational work establishes the framework for bringing
multiple new interest types to POI, improving person-level signal relevance and positioning us to
better power AI agents for person search functionality.

Goals & Progress

Vertical Datasets: Igor Kyrylenko automated franchise data processing pipeline elements and
expanded multi-brand owner coverage through AI-generated contacts, while Dana Hurtig
completed UDB matching for franchisees and delivered enrichments at 115% of projected
targets. Brandon Tucker advanced Form 5500 dataset enablement, ensuring Data Services can
pull samples for the top 50+ franchisors to support more proactive customer engagement.

GTM Platform Integration: Brandon Wilson generated aggregated views for opportunity data at
different sales cycle stages, providing the base dataset for the contributory network benchmark
agent that will help customers understand deal cycle patterns and timing benchmarks. This work
directly supports Heather Ma's development of the benchmark agent prototype demonstrated
this week.

Data Quality & Coverage: Dana's team processed 2.2M enrichments including 2M freemails
from 5x5 and resolved 200K bad data records, while EMEA company data from Rhetorik
advanced toward staging for production review. These improvements strengthen our core data
foundation and expand geographic coverage in key markets.

Strategic Challenges

The Form 5500 dataset requires enhanced Data Services enablement around data dictionaries,
as competitors use different column naming conventions that create confusion during customer
evaluations. Brandon Tucker is addressing this through improved documentation and sample
provision to help go-to-market teams navigate the complexity and respond more effectively to
customer queries about data availability and structure.

Translation strategy alignment across data productions remains an open question, with Igor
noting complete datasets available in multiple countries (Australia, France, Germany, Sweden,
UK) that could be published in native languages. Jody Roberts initiated conversations to
establish a coordinated approach for what languages we support, how we store translated
information, and prioritization of different geographic markets beyond current focus areas.

Manager attribute integration from GAL and Google Directory data into the PTI pipeline shows
promise for improving org chart functionality, but requires additional scoping and prioritization
discussions. The potential to leverage data from 100K domains with management association
coverage could significantly enhance our org chart agent capabilities, though implementation
timeline needs clarification.

Strategic Insights

Key Learnings & Discoveries

The contributory network benchmark agent prototype revealed significant customer appetite for
deal cycle insights based on aggregated opportunity data across our network. With 1,200+
companies providing permission to share data, we can deliver unique benchmarking insights
that competitors cannot replicate, particularly around stage-by-stage analysis and seasonal
buying patterns that provide actionable intelligence for sales teams.
Our franchise data quality validation uncovered that manual verification processes, while
thorough, need efficiency improvements to scale effectively. Dana's team completed validation
for the top 100 franchisors but identified the need for additional resources to process the full list
of ~2,500 efficiently, highlighting opportunities to optimize validation workflows for future vertical
dataset launches.

The GAL and Google Directory data analysis showed minimal overlap between sources,
creating opportunities to use both for comprehensive manager attribute coverage. This
discovery supports more robust org chart generation and could significantly improve the
accuracy and completeness of organizational hierarchy data available to customers.

Cross-Team Dependencies

Our work with the GTM team on vertical dataset enablement continues to be essential for
achieving H2 revenue targets. Current focus on contractor, franchise, and restaurant datasets
requires continued collaboration on account targeting, sample provision, and sales enablement
to ensure field teams can effectively communicate value propositions and advance opportunities
with qualified prospects.

The benchmark agent development depends on coordination between Brandon Wilson's data
aggregation work and Heather Ma's agent implementation, with both teams working to refine
opportunity data analysis and user interface design. Success here requires ongoing alignment
on data requirements and presentation formats to ensure the agent delivers actionable insights
rather than just informational summaries.

Looking Ahead

Next week's primary focus centers on advancing production readiness across multiple fronts
while maintaining momentum on customer-facing capabilities. The team will push user-level POI
data to production, complete franchise dataset automation, and continue EMEA company
infusion validation.

Igor will publish FINRA data to Snowflake with schema documentation while completing QA
verification for the franchise automation pipeline. Steve's team will move from staging to
production for the first POI interest type, establishing the foundation for additional interest types
in subsequent weeks. Dana will finalize EMEA company data review and initiate the next phase
of geographic expansion, while Brandon Wilson continues benchmark agent data model
development to support Heather's agent implementation work.

The convergence of these efforts positions us well for Q4, with vertical datasets gaining market
traction, contributory network capabilities demonstrating clear value, and core data quality
improvements supporting all downstream applications. Our ability to deliver unique, high-quality
datasets while providing innovative tools for customers to understand and leverage that data
creates a compelling competitive advantage in the evolving data marketplace.
Source: Data Executive Operating Framework entries from [September 15th, 2025 - September
18th, 2025]
