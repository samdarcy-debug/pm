---
id: weekly-data-platform-2025-44
title: "GTM Data Platform Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Data Platform Executive Roundup - Week of October 27, 2025**

## **Executive Summary**

The team is going with a hardwired approach for Companies and Contacts
in GraphQL to meet the December 31 deadline for GraphQL integration with
Federated Search, accepting a small amount of technical debt to meet the
date. This is primarily due to a lack of time for the data team to build
the integration to GTM Store with typespec metadata. Company and Contact
PM support is still essential to align on schemas and prevent
customer-impacting rework after launch. Linda Johannessen spec'd the
operators for scalars for the Federated Search team to start mapping,
while Marc Delurgio aligned resources to kick off GTM Data Model field
value normalization planning next week.

## **This Week\'s Progress**

### **Key Momentum Areas**

Linda Johannessen delivered the scalar and operator definitions needed
to unblock Federated Search mapping work. She reviewed these
specifications with the Federated Search team and there are follow ups
to finalize discrepancies in operators between Solr and generalized
query operators like "like." She\'s also working with the Copilot team
to confirm expected GraphQL behavior and engagement coverage, with
progress remaining on track for the December milestone. This work
validates that early collaboration with consuming teams surfaces edge
cases faster and prevents downstream delays or blockers.

Marc Delurgio secured resource alignment to begin GTM Data Model field
value normalization planning. Resources are now allocated and planning
will commence next week on normalizing field values, enabling GTM Data
Model consumers to easily search and filter on standardized values for
attributes like Country and Opportunity Stage. While the team discovered
that integrating Company and Contact datasets into GTM Store is larger
than initially expected and will take longer for the data team to
complete, they\'ll hardwire these fields into GraphQL for the December
31 target date so clients shouldn't experience any difference in
functionality.

Menna Rashwan achieved alignment on the temporary schema approach based
on existing Solr fields to meet the December 31 timeline. With new
Person and Company schemas unavailable in GTM Store by year-end, the
team is proceeding with a shim-based approach that allows Federated
Search and GraphQL integration to move forward. Scalar mapping is
underway, though key operator behavior questions remain open and require
resolution. This pragmatic decision balances delivery timeline against
technical architecture considerations.

### **Goals & Progress**

**Federated Search Integration & Schema Strategy**: Menna Rashwan
finalized alignment with Data Producers on a Shim Field Spec based on
existing Solr fields, acknowledging that a full schema migration to
TypeSpec and GTM Store isn\'t feasible by December 31. The shim-based
workaround allows Federated Search and GraphQL integration to proceed
while the team works through field behavior and data type alignment.
Scalar mapping is progressing, though it depends on clarifying operator
support, which is being addressed in scheduled follow-up sessions. Next
week\'s priorities include aligning with Data Producers on the final
list of prioritized fields and their schema, and resolving open
questions around scalar and operator behavior to complete mapping.

**Copilot Platform Scalability & MCP Exploration**: Linda Johannessen is
accelerating Copilot scalability by surfacing and resolving hidden
platform blockers before they delay delivery. Her work on scalar
definitions and GraphQL operator specifications provides the foundation
for faster Copilot iteration and agentic readiness, aligning schema and
operator definitions to GTM API standards.

**Location Matching & Regional HQ**: Moshik Levin continued working
toward getting the Regional HQ proof of concept ready for engineering
review, though this work was pushed to the next sprint. He discovered
that the Sales company view has an existing hierarchy that the team
should aim to align with as much as possible, ensuring customers see a
consistent company view across different parts of the product. The goal
remains to finish the first pass of the Regional HQ proof of concept so
it\'s ready for engineering to pick up in November, with the team
drafting two to three options using company data or heuristics to
determine regional HQ.

### **Strategic Challenges**

The interim schema approach creates downstream risk that requires
careful management. Menna Rashwan noted that while the shim-based
approach using current Solr schema enables December 31 delivery, this
interim schema may not align with the long-term data architecture or the
upcoming Company and Person schemas still under development. Once the
new schema is finalized, there\'s a risk it will introduce breaking
changes that require rework or fundamental changes to how Federated
Search integrates with GraphQL. The team needs Company and Contact PM
support as a top priority to align on schemas for the Federated Search
and GraphQL solution, preventing customer-impacting changes after
launch.

Marc Delurgio discovered that integrating Company and Contact datasets
into GTM Store is bigger than expected and will take longer for the data
team to complete. The team\'s decision to hardwire these fields into
GraphQL for the December 31 target date is a pragmatic workaround that
maintains the delivery timeline while acknowledging the underlying
complexity. This technical debt will need to be addressed in future
iterations once the full GTM Store integration is complete.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Early validation with consuming teams surfaces edge cases faster and
prevents downstream delays or blockers, as Linda Johannessen observed
through her work with the Copilot team. This pattern of continuous
engagement with teams that will use the platform capabilities helps
identify issues while they\'re still easy to fix, rather than
discovering problems late in the integration process when changes are
more expensive and disruptive.

The team learned that maintaining delivery pace sometimes requires
accepting interim technical solutions with clear migration paths. The
shim-based approach acknowledges reality---new schemas won\'t be ready
by December 31---while still enabling the integration to proceed. This
pragmatic decision balances competing priorities of delivery timeline,
technical architecture quality, and customer experience. However, the
team recognizes that getting schema definitions right is non-negotiable,
as schema changes post-launch will impact customers while pipeline
changes can happen transparently.

Moshik Levin\'s discovery that the Sales company view already has an
established hierarchy shapes how the Regional HQ proof of concept should
be designed. Rather than creating a new hierarchy model, the team should
align with existing patterns so customers experience consistency across
the product. This insight prevents the team from introducing
inconsistencies that would confuse users and create support burden.

### **Cross-Team Dependencies**

Company and Contact PM support is a crucial dependency for successful
December 31 delivery. Both Linda Johannessen and Menna Rashwan
identified the need for these product managers to engage on schema
alignment for the Federated Search and GraphQL solution. Without this
alignment, the interim shim-based approach risks introducing breaking
changes when permanent schemas are finalized, creating rework and
potentially impacting customers. This dependency needs executive
attention to ensure the right resources are engaged.

Coordination with Data Producers remains necessary to finalize the
prioritized field list and resolve open questions around scalar and
operator behavior. Menna Rashwan needs to complete this alignment next
week to finish scalar mapping and unblock implementation work. The
scheduled follow-up sessions on operator support need to produce clear
decisions that enable the Federated Search team to complete their
integration work.

## **Looking Ahead**

Next week centers on finalizing the technical specifications and
resource planning needed to execute the December 31 delivery. The team
will tie up loose ends for November 3rd deliverables and kick off
planning for normalizing field values in GTM Store, establishing the
foundation for consistent data representation across the platform.

Menna Rashwan will align with Data Producers on the final list of
prioritized fields and their schema, then resolve open questions around
scalar and operator behavior to complete mapping work. This finalization
is essential to enable the Federated Search team to complete their
integration without ambiguity about how fields should behave. Linda
Johannessen will continue her focus on Copilot Workspaces and Federated
Search integration to the GraphQL API, with multiple key datasets under
review. Her work on surfacing and resolving hidden platform blockers
will accelerate Copilot iteration by removing friction before it impacts
delivery timelines. Moshik Levin will continue preparing the Regional HQ
proof of concept for engineering review, though this work has shifted to
the next sprint. The team has made pragmatic decisions to maintain
December delivery momentum while acknowledging technical trade-offs, and
securing Company and Contact PM engagement on schema alignment will
determine whether these interim solutions can transition smoothly to
permanent architecture without impacting customers.

*Source: Team 1-2-3 Operating Framework entries from October 27-31,
2025*
