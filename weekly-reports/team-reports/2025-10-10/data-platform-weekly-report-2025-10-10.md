---
id: weekly-data-platform-2025-41
title: "GTM Data Platform Weekly Report - October 10, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-10-10
updated: 2026-01-06
week_ending: 2025-10-10
reporting_period: "October 6-10, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Data Platform Executive Roundup - Week of October 6, 2025**

## **Executive Summary**

The Data Platform team completed critical dependency mapping across
GraphQL initiatives and finalized the Q4-2026 roadmap for stakeholder
review, establishing the foundation for accelerated delivery on
AgentForce, GTM Studio, and Copilot Pro. Linda Johannessen led the
stakeholder alignment work, identifying potential bottlenecks before
they become execution risks. However, conflicting priority signals
across teams threaten to dilute focus---the team cannot simultaneously
support January workbooks delivery, federated search integration, schema
migrations, and external API release without clear sequencing decisions.
Next week centers on locking in agreed priorities and timelines so
engineering refinement can proceed with confidence.

## **This Week\'s Progress**

### **Key Momentum Areas**

Linda Johannessen completed a comprehensive stakeholder overview mapping
all inbound dependencies across GraphQL, Copilot, and enrichment
initiatives. The work revealed how platform capabilities must sequence
together---workbooks requiring federated search, which in turn requires
schema registry and type migrations---providing the visibility needed to
prevent downstream blockers rather than fixing them reactively.

Marc Delurgio initiated planning for data entitlement and access rules
for GraphQL API, with engineering exploring an efficient path through
federated search for entitlements since that functionality already
exists. This approach could accelerate implementation by leveraging
existing infrastructure rather than building from scratch, though the
team is evaluating whether routing through multiple hops introduces
unacceptable latency.

Moshik Levin finalized external communication assets for the CMD Enrich
API changes, working with Brandon from customer solutions to handle
outreach to affected accounts. The team learned that Master Data API
customers represent a distinct population from other enrichment API
users, requiring targeted communication strategies rather than broad
announcements.

### **Goals & Progress**

**GraphQL & API Development**: The Q4-2026 roadmap and deck are ready
for engineering refinement, with current top focus on Copilot and
enrichment with engagement data. Marc Delurgio reviewed scope for data
entitlement and access rules, confirming that engineering can
potentially hook into well-established entitlement services through
federated search. The open question around how customers would pay for
engagements requires resolution before full implementation planning can
proceed.

**Customer Communication & Migration**: Moshik Levin shared
documentation and communication assets for the Company Master Data
Enrich API transition, preparing customers who still use deprecated
Everstring fields. The team identified affected accounts and drafted
targeted messaging, learning that this customer segment has minimal
overlap with other API users. Brandon from customer solutions will drive
the outreach, with materials emphasizing that fields won\'t be
deprecated but will simply stop receiving new data---a critical
distinction that prevents unnecessary engineering panic.

**Federated Search Integration**: Menna Rashwan identified and
prioritized the initial set of ZoomInfo fields (Company and Person)
required to support the first iteration of federated search integration
via GraphQL. This work unblocks the integration by aligning on priority
use cases and field-level search requirements, establishing the
foundation for standardized, cross-platform operator behavior.

### **Strategic Challenges**

Priority alignment remains the most significant execution risk.
Messaging on priorities, scope, and timelines varies across teams and
documents, creating room for conflicting interpretations that will slow
delivery if not addressed immediately. Linda Johannessen noted that the
team cannot realistically deliver everything requested in the desired
timelines---for example, supporting January workbooks delivery while
simultaneously externalizing the API in parallel would risk failing at
both. The complexity lies in dependency chains: workbooks requires
federated search requires schema migrations, all of which must complete
before external release makes sense.

Resource constraints are becoming more acute as application teams
increase engagement. Marc Delurgio pointed out that the external API
goal was set when app teams weren\'t yet engaged and focused on
workbooks, but now that they\'re actively involved, the platform must
prioritize their needs. The good news is that work needed for external
API will be covered by federated search integration, making a February
2026 external release feasible if workbooks remains the primary focus.
However, this requires explicit prioritization decisions rather than
attempting parallel execution.

The team identified a gap in federated search support for ZoomInfo data
access rules, where record-level suppression is enforced but field-level
suppression is not yet supported. Ownership of field suppression logic
resides with another team, requiring cross-functional coordination to
ensure end-to-end privacy compliance before federated search scales
across first-party, second-party, and third-party data sources.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The metadata and schema work emerging as a strategic lever in an
agent-driven world. As engineers actively ask to use GraphQL---a strong
signal of growing adoption momentum---the team recognizes that Model
Context Protocol (MCP) and metadata aren\'t just technical requirements
but fundamental enablers for both human and AI agent consumption of
platform capabilities.

Communication clarity prevents downstream confusion. Moshik Levin\'s
work on the Everstring transition revealed that the initial messaging
wasn\'t clear enough about the distinction between deprecating fields
versus stopping population of those fields. The team learned to
emphasize that this is not a breaking change---fields remain available,
they just won\'t receive new data---preventing customers from
unnecessarily engaging engineering resources to handle a non-existent
problem.

Federated search architecture decisions have cascading implications. The
team discovered that existing platform-level privacy functionality can
potentially be leveraged to support third-party data access rules within
search, minimizing duplication and ensuring alignment with broader
platform standards. However, the field-level suppression gap requires
attention before federated search can safely scale.

### **Cross-Team Dependencies**

Collaboration with the External API team has surfaced timing and scope
questions for GraphQL support. The external gateway work represents the
primary missing component for public release, but the team can leverage
internal testing with workbooks to validate functionality before
external exposure. Marc Delurgio and Linda Johannessen are working to
ensure the November external release path remains viable while not
compromising January workbooks delivery.

Coordination with application teams has intensified as workbooks
engagement increases. The team is carefully balancing immediate platform
needs with longer-term strategic goals, recognizing that successful
workbooks delivery will validate the platform architecture and create
momentum for external API release in early 2026.

## **Looking Ahead**

Next week focuses on establishing definitive priority sequencing and
confirming timelines so the roadmap can be finalized and engineering
refinement can move forward without ambiguity. Linda Johannessen will
meet with engineering leads to gather high-level effort estimates and
identify potential bottlenecks.

The team will drive toward clear decisions on GraphQL path
prioritization---specifically whether to sequence federated search
integration first, followed by external API exposure, or attempt
parallel execution. The dependency mapping completed this week provides
the foundation for informed trade-off discussions, and stakeholder
alignment on a single agreed reference will enable sharper sequencing
and faster delivery on work that matters most.

Marc Delurgio will continue refining the data entitlement and access
rules scope, ensuring alignment between platform-level privacy controls
and application-specific needs. Moshik Levin will finalize customer
communications with Brandon from customer solutions, ensuring affected
accounts receive clear, accurate information about the CMD Enrich API
transition. The team remains confident in their ability to deliver
high-impact platform capabilities while maintaining the architectural
quality and data governance standards required for long-term success.
