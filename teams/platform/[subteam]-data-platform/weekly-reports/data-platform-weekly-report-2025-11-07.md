---
id: weekly-data-platform-2025-45
title: "GTM Data Platform Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Data Platform Executive Roundup - November 7, 2025**

## **Executive Summary**

The team kicked off GTM Data Model field value normalization this week
with aligned resources and clear ownership between Andres\' team
(canonical values) and the Data team (resolution service). This work
enables clients to easily query and filter on standardized values like
country and opportunity stage. Simultaneously, the December 31st
Federated Search integration continues progressing, though based on
GraphQL moving away from BigQuery, new technical scope was added in the
Engagement Data will need to be added to Solr. Menna Rashwan is
coordinating with Linda Johannessen and engineering leadership to assess
impacts and determine feasibility by 12/31.

## **This Week\'s Progress**

### **Key Momentum Areas**

Marc Delurgio launched the GTM Data Model field value normalization
initiative, building on substantial groundwork completed by the Data
team last spring. The architecture assigns clear ownership: Andres\'
team will maintain canonical standardized values for first-party CRM
data, while the Data team owns the resolution service that maps incoming
values to standards in real-time. Magnus\' new shared services gem under
Casey will handle the service implementation, with delivery timing TBD.

Menna Rashwan completed the schema workshop with the Contacts Data
Producers team, achieving alignment on Phase 1 field lists and
identifying necessary schema changes for GTM Store publishing
post-December 31st. The Architecture Review surfaced critical work
needed to onboard core ZoomInfo Contact and Company data, while
scalar-to-operator-to-search type mapping progressed in coordination
with Enterprise Data Engineering following newly clarified operator
definitions.

Moshik Levin consolidated documentation on location matching strategy,
clarifying the differences between data sets and when to use each. He\'s
preparing to transform the old match deck into a digestible format for
the Data team, planning both a short video overview and a comprehensive
written guide that will help accelerate understanding across the
organization.

### **Goals & Progress**

**GTM Data Model Normalization**: The field value normalization vision
is kicked off with resources aligned, but detailed specs and planning
are to follow. The Data team will leverage their existing resolution
service framework, extending it with an LLM-powered fallback for
unmapped values. When confidence is insufficient, the system will use an
\"other\" value that customers can later update as mappings evolve. The
shared services team is being established under Magnus\' leadership to
own this capability, with detailed specs and timing still being refined
but likely targeting January delivery given current December
commitments.

**Federated Search Schema Alignment**: The team held productive
workshops with Data Producers on Contacts, achieving Phase 1 field
alignment and identifying discrepancies between current Solr fields and
the proposed GTM schema. Key gaps include address structure (currently
single street field, future will break into components) and management
level representation (today consolidated, future will separate board
member as standalone field). While the shim-based approach using
existing Solr typespec remains the pragmatic path to meet December 31st,
these schema differences signal future rework once the new schema
publishes.

**Location Matching Documentation**: Moshik Levin is preparing
comprehensive starter guides on location matching for engineering teams,
working to clearly separate matching from enriching concepts and provide
guidance on which company collections fit different product needs. The
goal is enabling teams across the organization to understand and
leverage location data effectively as planning for 2026 initiatives
accelerates.

### **Strategic Challenges**

Engagement data unexpectedly joined the December 31st Federated Search
scope this week. Menna Rashwan learned about this addition after
returning from a day off, discovering that a eng leadership-level
engineering decision had shifted engagement from BigQuery to Solr as
part of broader architectural changes. While the original December 31st
commitment covered only companies and contacts, engagement is now
included. The lines of ownership between Linda Johannessen\'s roadmap
work and Menna\'s search execution have grown blurry on this topic. A
cross-functional meeting with Marc Delurgio, Ali, Linda, and engineering
leadership is being scheduled to assess impact, evaluate feasibility,
and clarify decision-making authority rather than simply accepting or
refusing the new scope.

The architectural shift from BigQuery to Solr represents a fundamental
platform decision made by eng leadership including Filip. While Marc
Delurgio welcomes decisive calls that end months of circling
discussions, this change affects working implementations. Engagement
currently functions in GraphQL hitting BigQuery, and the switch to Solr
doesn\'t magically manifest equivalent functionality, especially for
aggregations. Even if the metadata-driven architecture eventually
reduces implementation effort, any additional work at this stage
compresses an already tight timeline. The team is empowered to assess
impacts transparently and communicate what this architectural pivot
means for delivery commitments.

Schema alignment continues revealing mismatches between interim and
target states. The shim-based approach using current Solr fields enables
December 31st delivery, but discrepancies with the evolving Company and
Person schemas risk requiring breaking changes and rework post-launch.
Data Producers support remains necessary to finalize MVP field
specifications and resolve datatype mismatches. The team needs Company
and Contact product management partnership as P0 to properly align
schemas before launch, since schema changes impact customers while
pipeline changes can happen transparently.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The value normalization architecture elegantly distributes ownership
according to data domains. Andres\' team managing canonical standardized
values for first-party CRM-oriented data makes sense given their
proximity to those systems, while the Data team owning resolution
services and broader standardization aligns with their platform
responsibilities. Including an LLM-powered fallback for uncertain
mappings plus an \"other\" category for genuinely unmapped values
creates flexibility for customers whose data doesn\'t fit predefined
buckets. The approach balances immediate utility with evolution over
time.

Engineering leadership made a significant architectural call this week:
Solr for queries, moving away from BigQuery. While the decision creates
work for the team, having leadership definitively resolve an issue that
generated months of swirling discussion represents progress. The key now
is ensuring everyone understands the implications and that downstream
teams can execute within existing commitments. Functional concerns
remain regarding aggregations and Marc will work with Linda to follow up
on these.

The scalar-to-operator-to-search type mapping accelerated substantially
once operator definitions clarified. Menna\'s team made visible progress
after definitions solidified in working sessions, demonstrating how
ambiguity at the foundational level cascades into execution delays.
Early validation with consuming teams surfaces edge cases faster,
preventing downstream blockers---a pattern consistently validated across
multiple workstreams.

### **Cross-Team Dependencies**

Our work with the Contacts Data Producers team proved highly productive,
achieving Phase 1 field list alignment and surfacing schema requirements
for post-December 31st GTM Store publishing. However, the broader
Company and Contact product management support remains essential for
finalizing schemas before Federated Search launches. Schema changes
directly impact customers while pipeline adjustments happen invisibly,
making pre-launch alignment non-negotiable. The Architecture Review
conducted this week outlined substantial work needed to onboard core
ZoomInfo data properly.

Magnus\' new shared services team under Casey represents an important
partnership forming at exactly the right moment. As they build their
backlog from various product managers\' requirements, the timing aligns
well for the value normalization work. Marc confirmed that the codes and
values work for mapping with Menna\'s team falls under this umbrella. A
Monday meeting will help ensure Magnus has full visibility into
requirements, though the team needs to determine if the existing
specifications need polishing before handoff.

## **Looking Ahead**

Next week centers on finalizing schema alignment with the Company Data
Producers team and completing scalar-to-operator-to-search type mapping
for MVP Person and Company fields. The engagement scope question needs
resolution through the cross-functional leadership meeting being
scheduled.

Marc will work with Menna to set up alignment discussions between her
team, Linda\'s team, engineering leadership, to clarify the engagement
data addition and its implications. The goal is to transparently assess
what adding engagement means for December 31st commitments made under
different technical scope assumptions. Meanwhile, Moshik will publish
his location matching starter guide, improving transparency as teams
prepare 2026 planning. The field value normalization work continues with
Magnus\' team as detailed specifications get refined and integration
approaches solidify. The team maintains strong bias toward protecting
the December 31st delivery date while pragmatically addressing scope and
architectural changes through proper impact assessment rather than
idealistic approaches that risk pushing timelines.

*Source: Team 1-2-3 Operating Framework entries from November 3-7, 2025*
