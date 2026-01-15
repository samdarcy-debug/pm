---
id: weekly-data-platform-2025-43
title: "GTM Data Platform Weekly Report - October 24, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Data Platform Executive Roundup - Week of October 20, 2025**

## **Executive Summary**

Dominik and Filip established strategic sequencing clarity this week,
prioritizing Federated Search in Graph QL ahead of the Graph QL API
public beta release. Timing of GQL public beta release will be evaluated
down the road, but it's not an immediate priority. Menna Rashwan
finalized alignment with App teams on MVP search use cases, prioritized
fields, and expected behavior, while resolving missing schema fields
with Data Producers. The team now has top-to-bottom product and
engineering alignment on making Federated Search integration with
GraphQL a P0 priority, positioning December 31 delivery as achievable if
remaining technical work proceeds on schedule.

## **This Week\'s Progress**

### **Key Momentum Areas**

Menna Rashwan achieved comprehensive cross-functional alignment on the
foundation for Federated Search integration. She finalized MVP search
use cases, prioritized field lists, and expected search behavior with
App teams, then worked closely with Data Producers to resolve missing
fields from the shared schema and agree on next steps for datatype
mismatches. She initiated mapping between MVP search fields and GraphQL
scalars, standardizing how Person and Company data will be searched
across the platform to ensure scalability and consistent user experience
for the December 31 integration deadline.

The leadership team set the strategic sequence as Federated Search
before External API, validating that the current GraphQL path is
extensible for Copilot Workspaces and vertical datasets. They also
confirmed that entitlement and credit models are required before
external or monetized dataset access, establishing clear guardrails for
what must be delivered first and what can follow later.

### **Goals & Progress**

**Federated Search Integration & Schema Alignment**: Menna Rashwan
worked through schema discrepancies with Data Producers, identifying
that the current schema was missing key fields required for search use
cases. These fields are now being added, though datatype mismatches
still need resolution. Some fields will need to be indexed as both code
and value to support sorting, faceting, and filtering use cases,
requiring coordination with the data team via a shared mapping service.
While use cases, field lists, and behavior are finalized, additional
work is needed to capture and align on sorting and faceting requirements
with App teams to fully enable the end-to-end search experience. The
scalar mapping work is actively progressing, with two remaining areas
expected to be resolved: clarifying which operators are supported by
each scalar type to ensure compatibility with intended search behaviors,
and finalizing schema updates from Data Producers to address current
datatype mismatches.

**Location Matching & Regional HQ**: Moshik Levin gained access to
Company Data\'s proof of concept and tested the company hierarchy graph,
exploring ways to leverage the \"Domestic HQ\" flag for regional
matching. He\'s continuing to workshop which data points are required
and which heuristics can run on the fly for the proof of concept, with
the goal of adding options for using Company Data instead of only
resolving locations on-the-fly. The team wants engineering to pick up
this work in November.

### **Strategic Challenges**

Schema gaps and technical dependencies continue to require careful
coordination across teams. While Menna Rashwan achieved initial
alignment with Data Producers, mapping exposed several coverage issues
including missing fields and mismatched data types that impact search
use case coverage. Some MVP fields do not map cleanly to proposed
GraphQL scalars, though this gap may be mitigated if Data Producers
supply the expected data types. Additionally, fields that need to be
indexed as both code and value for sorting, faceting, and filtering will
require coordination through a shared mapping service. An alignment
meeting originally scheduled for this week was pushed to next week due
to a data team offsite, creating a slight delay in resolving these
technical details.

App team alignment work revealed an additional layer of requirements
beyond initial MVP scope. While Menna Rashwan finalized use cases, field
lists, and basic search behavior with App teams, additional work emerged
around capturing and aligning on sorting and faceting requirements
across prioritized Person and Company fields. These capabilities are
necessary to fully enable the end-to-end search experience that users
expect, expanding the scope slightly from the original MVP definition.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Dominik and Filip's decision to prioritize Federated Search before
External API provides the strategic clarity the team needed to focus
execution. This sequencing decision validates that the current GraphQL
path is extensible for future use cases including Copilot Workspaces and
vertical datasets, confirming the architectural approach is sound. The
decision also establishes that entitlement and credit models must be in
place before external or monetized dataset access, ensuring proper
business controls are built into the foundation rather than retrofitted
later.

Product and engineering achieved top-to-bottom alignment on making
Federated Search integration with GraphQL a P0 priority. This level of
organizational commitment is a significant shift that removes ambiguity
about resource allocation and competing priorities. When both product
and engineering leadership agree on top priority status, teams can move
forward with confidence that their work won\'t be deprioritized for
other initiatives, accelerating execution velocity.

The schema alignment work revealed that some fields need dual indexing
strategies to support the full range of user behaviors. Fields that need
to support sorting, faceting, and filtering require indexing as both
code and value, which necessitates coordination with the data team via a
shared mapping service. This discovery shapes the technical approach and
highlights a dependency that must be managed to deliver complete search
functionality rather than just basic filtering capabilities.

### **Cross-Team Dependencies**

Coordination with Data Producers remains essential for resolving schema
discrepancies and finalizing MVP field specifications. Next week\'s deep
dive with Data Producers will address datatype mismatches and finalize
the approach for fields requiring dual indexing. The alignment meeting
was pushed due to the data team offsite, so maintaining momentum on this
workstream depends on productive outcomes when teams reconvene.

App teams need to remain engaged on sorting and faceting requirements to
ensure the search experience meets user expectations. While basic search
behavior is finalized, these additional capabilities are necessary for
the end-to-end experience, requiring continued collaboration beyond the
initial MVP alignment to capture complete requirements.

## **Looking Ahead**

Next week centers on finalizing the technical details that will unblock
implementation work and securing the remaining alignment needed for
December 31 delivery. The team will complete phase 1 company and contact
field scalar definitions and their related operators, establishing
precise behavior models with engineering.

Menna Rashwan will finalize schema updates with Data Producers,
resolving datatype mismatches and determining the approach for using the
shared mapping service for code-to-value translation. She\'ll align with
App teams on sorting and faceting requirements across prioritized Person
and Company fields, then revisit scalar mapping to validate operator
compatibility and address any missing or mismatched scalar types. This
work completes the foundation needed to unblock Federated Search
implementation. Moshik Levin will continue exploring proof of concept
options for Regional HQ matching, workshopping required data points and
on-the-fly heuristics to prepare for engineering pickup in November.
Linda Johannessen will finalize the three executable sequencing
options---External-first, Federated Search-first, or Hybrid---with clear
scope, effort, validated engineering impact, and documented trade-offs,
enabling leadership to choose a single path forward instead of splitting
capacity. With strategic direction now set and cross-functional
alignment achieved, the team is positioned to convert planning into
execution, delivering the platform capabilities that Copilot Workspaces,
vertical datasets, and federated search require.

*Source: Team 1-2-3 Operating Framework entries from October 20-24,
2025*
