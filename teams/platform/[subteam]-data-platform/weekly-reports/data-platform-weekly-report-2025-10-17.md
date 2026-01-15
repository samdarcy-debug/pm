---
id: weekly-data-platform-2025-42
title: "GTM Data Platform Weekly Report - October 17, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-10-17
updated: 2026-01-06
week_ending: 2025-10-17
reporting_period: "October 13-17, 2025"
tags: ["weekly-report", "Q42025"]
---

# **GTM Data Platform Executive Roundup - Week of October 13, 2025**

## **Executive Summary**

The GTM Data Platform team reached alignment on Company and Contact
field lists to support the December 31 Federated Search integration with
GraphQL, while also confirming end-to-end metadata flow for automated
dataset onboarding. Platform roadmap was published from executive
onsite, however, tight dependencies across multiple
workstreams---including CDC on Metadata, Schema Registry, and TypeSpec
Migration---present delivery risks that will need to be tracked
diligently to keep the timeline viable.

## **This Week\'s Progress**

### **Key Momentum Areas**

Menna Rashwan and the team achieved product and technical alignment
across App teams, Data Producers, and GraphQL stakeholders on MVP search
field lists, and drafted behavior standards for Federated Search. This
cross-functional effort establishes the foundation for December
integration by standardizing how Person and Company fields will be
searched across the platform, ensuring both scalability and consistent
user experience.

Marc Delurgio secured alignment on spec ownership for search data types
and scalar definitions and facilitated review of Linda's (PTO) scalar
spec, enabling the team to move forward with M1 field specifications
with clearly defined search behavior and scalars.

### **Goals & Progress**

**Federated Search Integration**: Menna Rashwan defined M1 search
behavior for prioritized Person and Company fields to support Federated
Search via GraphQL, mapping M1 fields to proposed GraphQL scalars and
reaching initial alignment with Data Producers on field schema. The team
identified fields without direct scalar mappings and scheduled cross-app
alignment meetings to finalize MVP use cases and search behavior. This
work establishes the technical foundation for a more dynamic, scalable
search platform that can onboard new data types and filters faster while
maintaining consistency across first-party, second-party, and
third-party data.

**Location Matching Strategy**: Moshik Levin started scoping out
Regional HQ Matching and collected territory-management use cases from
location customers and coordinated with the Company Data team, who are
exploring two graph database options to represent relationships between
locations. One option is already implemented and can return rollups
based on address, with a meeting scheduled to discuss options for
regional HQ queries.

**Strategic Challenges**

The December 31 Federated Search integration faces significant
dependency risk. Menna Rashwan identified that cross-platform
dependencies including CDC on Metadata, Schema Registry, TypeSpec
Migration, and Metadata API v2 must all deliver on a compressed timeline
to unblock Search implementation work. Several of these dependencies
appear unlikely to be delivered within the current timeframe, which
could impact the overall integration milestone. An alignment meeting is
scheduled to assess feasibility, identify trade-offs, and determine a
viable path forward. The team needs executive support in prioritizing
these dependencies and potentially adjusting scope if technical
realities require it.

Schema alignment work revealed technical gaps that require resolution
before moving forward. While Menna Rashwan achieved initial alignment
with Data Producers, the mapping exposed coverage gaps including missing
fields and mismatched data types between search requirements and
available schema definitions. Some M1 fields do not map cleanly to
proposed GraphQL scalars, though this gap may be mitigated if Data
Producers can supply the expected data types. A deep dive with Data
Producers is scheduled to resolve these schema discrepancies and
finalize M1 field specifications.

## **Strategic Insights**

### **Cross-Team Dependencies**

Our work with the External API team on GraphQL support continues to be
essential for enabling customer and agent access to Federated Search
capabilities. The team is exploring whether to route through Federated
Search for entitlements since that functionality is already implemented,
which could accelerate delivery.

Coordination with Data Producers remains necessary to resolve schema
discrepancies and finalize M1 field specifications. The deep dive
scheduled with this team will determine next steps for missing scalars
and drive the final field specs needed to unblock GraphQL integration.
Success here depends on Data Producers\' ability to supply expected data
types where gaps currently exist.

## **Looking Ahead**

Next week centers on confirming the order of key priorities and
timelines so engineering refinement can move forward with confidence.
The team will drive priority alignment discussions on the GraphQL path,
assessing trade-offs between federated search integration and
externalized API approaches.

Menna Rashwan will finalize cross-functional alignment with App teams on
prioritized search use cases, field list, and behavior to unblock
Federated Search integration via GraphQL for the December 31 deadline.
This includes conducting a deep dive with Data Producers to resolve
schema discrepancies and finalize M1 field specs, which will determine
the path forward for fields that don\'t currently map to GraphQL
scalars. Moshik Levin will meet with the Company Data team to discuss
graph database options for regional HQ queries and continue
consolidating requirements for location matching from Q4 initiatives
including Workbooks and New Company Creation. The team has built strong
technical alignment and cross-functional consensus this week; next
week\'s priority confirmation work will ensure everyone moves forward
with shared clarity on what matters most and when it needs to happen.

*Source: Team 1-2-3 Operating Framework entries from October 13-17,
2025*
