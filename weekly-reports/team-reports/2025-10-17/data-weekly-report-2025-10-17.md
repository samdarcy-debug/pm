---
id: weekly-data-2025-42
title: "Data Weekly Report - October 17, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-10-17
updated: 2026-01-06
week_ending: 2025-10-17
reporting_period: "October 13-17, 2025"
tags: ["weekly-report", "Q42025"]
---

Data Executive Roundup - [Oct 13th, 2025
- October 16th, 2025]

Executive Summary

Brandon Wilson and Heather Ma are advancing the CN Deal Cycle Insights agent with statistical
analysis showing deal velocity patterns across 28 tenants, preparing board-ready
demonstrations for the October 27th meeting. The team resolved a matching service bug
affecting Google and LinkedIn accounts that was creating false company associations.
Meanwhile, Igor Kyrylenko completed FINRA dataset ingestion into Snowflake and established
standardized frameworks for 17 states of professional licensing data, expanding beyond
contractors to create a PitchBook replacement offering while securing customer interest from
ID.me for verification use cases.

This Week's Progress

Key Momentum Areas

Brandon Wilson made substantial progress on CN Deal Cycle Analysis by building normalized
stage tables and aggregate datasets showing deal velocity patterns across contributory network
tenants. The team identified and resolved a matching service bug where accounts with
google.com subdomains were incorrectly matched to Google's company ID, ensuring cleaner
data for the board demonstration. Analysis now segments businesses by SMB, mid-market, and
enterprise on both tenant and account sides, enabling comparison of deal closure timelines
against historical patterns.

Igor Kyrylenko delivered two foundational datasets for vertical expansion. The FINRA dataset
completed matching and Snowflake ingestion with schema finalized for productization as a
PitchBook alternative, containing investment advisor and broker licensing data. Professional
Licenses data now covers 17 states with standardized taxonomy across 26 different format
variations, establishing expandable infrastructure for beauty licenses, real estate agents, and
other regulated professions. ID.me expressed strong interest in leveraging this data for identity
verification at scale.

Jody Roberts finalized the org chart agent prototype connecting to BigQuery for GAL and
Google Directory data integration. The agent successfully pulls management association data
covering 100K domains and demonstrates viable org chart visualization capabilities. Jody
documented the prototype's current functionality and limitations, positioning it for transition from
proof of concept to production deployment with dedicated engineering resources.
Goals & Progress

Contributory Network Insights: Brandon Wilson built aggregate tables for Deal Cycle and Win
Rate analysis, creating board-ready examples showing how CN tenants can benchmark their
pipeline velocity against historical closure patterns. The team normalized stage data across
tenants and resolved matching service issues affecting Google and LinkedIn accounts.
Integration with GTM Store API enables accurate deal size segmentation across SMB,
mid-market, and enterprise categories. Meeting scheduled with sales leadership validated the
signal format and confirmed the value proposition for the October 27th board demonstration.

Vertical Dataset Expansion: Igor Kyrylenko completed FINRA dataset ingestion with 286 fields
ready for productization, working with Peter to identify customer-facing data points that position
this as a PitchBook replacement. Professional Licenses framework now standardizes data from
17 major states including Florida, Texas, California, and Ohio, covering an estimated 60-70% of
U.S. licenses. The team developed automated email acquisition tools tested against 50 state
dealership boards, with plans to expand to 285 different license types across various regulatory
boards. Second customer call with ID.me confirmed their $285 million investment in data
acquisition, with professional licenses positioned as a verification solution for registered nurses,
real estate agents, and beauticians.

GTM Data Store & Platform Integrations: Suresh Putteti implemented the Contributory
Network Eligibility Status Flag in Salesforce, replacing the Boolean override flag with a
three-value system supporting no sharing, partial sharing, and vertical sharing under the new
legal framework. This flag will serve as source of truth for downstream systems enabling
expanded CN use cases. Brandon Tucker outlined acceleration plans for GTM Attribute Store
dataset onboarding, addressing the backlog of three dozen datasets awaiting integration and
identifying engineering resources beyond Austin to streamline the process for upcoming Studio
GA launch.

Strategic Challenges

Steve Hutchinson continues converting the Facilitators model from local Python scripts to
scheduled Spark infrastructure for production scale. The team secured approval from machine
learning engineering on the version 1 approach and successfully migrated BigQuery queries to
Spark. Writing model results to development locations is underway, with next steps focusing on
ZDP integration for downstream consumption by copilot and future agents. The shift from
manual local execution to automated scheduled processing removes a significant bottleneck for
user-level points of interest expansion.

Ethan Young is defining Company 3.0 post-match flow requirements to address over and
under-combination issues, working with Hasmik and the DAS team on relationship model
specifications. The team identified gaps in data cube testing automation where changes aren't
always verified for full traction across all affected records. Finance raised concerns about the
company definition impacts requiring additional investigation to ensure alignment on structural
changes for franchise relationships and employment associations at location level.
Dana Hurtig navigated a complex DNV RFP requiring manual review of 500 companies where
two-thirds returned as low-quality matches through Data Services. The team investigated each
case to find valid matches or document why matches weren't possible, delivering contacts
meeting specific criteria. Additionally, DIP staging environment failures blocked 500K mobile
phone infusions from completing on schedule, requiring engineering assistance to resolve the
pipeline issues while maintaining the 3.1M enrichment target including 300K new contacts and
2.2M email updates.

Strategic Insights

Key Learnings & Discoveries

The CN Deal Cycle Analysis revealed that deal velocity insights require careful segmentation by
business size on both sides of the transaction. Brandon Wilson's analysis across 28 tenants
demonstrated that meaningful benchmarking depends on comparing like-to-like scenarios -
SMB tenants closing SMB accounts show different patterns than enterprise sellers pursuing
mid-market deals. The team discovered that stage normalization across disparate CRM
implementations is achievable but requires continuous data quality monitoring, particularly for
accounts using non-standard opportunity management practices.

Igor Kyrylenko's work on professional licenses exposed the complexity hidden within state
licensing systems, where 17 states yielded 26 different data format variations requiring custom
standardization logic. States with centralized licensing systems deliver 3-4x faster data
acquisition than those with fragmented databases, informing prioritization for the automated
email acquisition tool. The discovery that ID.me seeks verification data for multiple professional
categories validates the strategy to build on the contractor dataset foundation rather than
treating each license type as a separate vertical.

Dana Hurtig's DNV RFP experience highlighted a fundamental data quality challenge - external
entities often request matches for records that don't meet the definition of a business entity in
our system. The RFP included telecommunications infrastructure components, family trusts, and
other non-traditional "companies" that fall outside standard matching criteria. This reinforces the
importance of Ethan Young's Company 3.0 definition work and suggests we need clearer
customer education about what types of entities exist in our database versus what we
intentionally exclude.

Cross-Team Dependencies

Work with the data science team on facilitators model productionization demonstrates strong
collaboration between Steve Hutchinson's analysis team and the MLE organization. Getting
approval from Cem on the version 1 approach before investing in production infrastructure
prevented rework and ensured alignment on the rules-based methodology. Similar collaboration
patterns are emerging with Peter supporting Igor's FINRA dataset productization, leveraging
PitchBook competitive intelligence to identify the most valuable of 286 available fields for
customer-facing packaging.

Engineering dependencies continue to pace dataset acceleration efforts. Brandon Tucker
identified that Austin has been the primary resource for GTM Attribute Store integrations,
creating a bottleneck as the backlog grows to three dozen datasets. The team needs to identify
additional engineering capacity and streamline the handoff process to support the upcoming
Studio GA launch and marketplace functionality. DIP staging failures blocking Dana's
enrichment work similarly highlight the need for more robust infrastructure monitoring and faster
engineering response for production-impacting issues.

Looking Ahead

Next week's focus centers on the October 27th board meeting preparation, with Brandon Wilson
delivering polished CN Deal Cycle Insights demonstrations showing 10 tenant examples of
pipeline velocity benchmarking. The team will continue analysis of stage-by-stage deal
progression to expand beyond full-cycle insights into granular breakdown of time spent in
exploratory, negotiation, and closing phases.

Igor Kyrylenko shifts to FINRA dataset productization, working with Peter to identify
customer-facing data points and schema design that positions this as a credible PitchBook
alternative. The automated email acquisition tool launches its first production test against 50
state dealership boards, validating whether programmatic data requests can scale to hundreds
of different licensing boards. Professional Licenses work continues with additional state
expansions and deeper categorization of license types and subtypes to create the standardized
taxonomy. Steve Hutchinson begins ZDP integration for facilitators model results, enabling
downstream consumption by copilot and workbooks while the team prepares multiple interest
types for production deployment. Jody Roberts travels to Waltham for the data product and
engineering onsite, reviewing 2026 big bets and driving alignment on strategic opportunities
including org chart agent transition from prototype to production and GTM Data Store
acceleration priorities.

Source: Data Executive Operating Framework entries from [Oct 13th, 2025 - October 16th,
2025]
