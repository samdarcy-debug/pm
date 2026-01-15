---
id: weekly-data-platform-2025-37
title: "GTM Data Platform Weekly Report - September 12, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-09-12
updated: 2026-01-06
week_ending: 2025-09-12
reporting_period: "September 8-12, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Data Platform Team Executive Roundup - September 8, 2025**

## **Executive Summary**

The Data Platform team has achieved a significant milestone with the
release of the GraphQL Query API, which is already being tested by
agentic platforms using MCP. Marc Delurgio has expanded the data access
spec to include Suppression Lists, now 50% complete with the additional
requirements. The team is actively preparing for next week\'s DaaS leads
meeting while investigating newly discovered RingLead usage in the match
api of deprecated fields that will require attention.

## **This Week\'s Progress**

### **Key Momentum Areas**

Linda Johannessen delivered the GraphQL Query API release, creating a
stable, agent-ready interface for cross-entity GTM data that has
generated strong early validation with agentic platforms already testing
MCP integration. This represents a foundational shift from just building
tools to creating systems that both humans and AI agents can leverage
effectively.

Adwait Kirtikar successfully aligned the DaaS team around platform
integration, publishing a comprehensive document that outlines current
business state, lessons learned, and roadmap alignment. The DaaS team
has expressed enthusiasm for working with the platform product team to
integrate their workflow, setting up productive collaboration moving
forward.

Menna Rashwan defined initial high-level milestones for Enterprise
Search v2 (Federated Search) to support CDC integration, metadata-driven
indexing, and real-time updates. This work directly enables the
technical foundation needed for advanced search capabilities across the
platform ecosystem.

### **Goals & Progress**

**Data Access & Governance**: Marc Delurgio expanded the original scope
to include Suppression Lists and other data access rules, achieving 50%
completion including the additional requirements. The team is preparing
stakeholder reviews to finalize documentation and move toward
implementation.

**Platform Integration**: Linda Johannessen refined schema and data
definitions through comprehensive syncs with Customer Data Catalog,
Workbook, and DaaS teams, confirming coverage across marketplace and app
scenarios. The work has been organized into executable JIRA stories with
a clear path to API readiness by the October 15 target date, with
stakeholders reinforcing a \"do it right, not fast\" approach
prioritizing metadata-first architecture.

**Legacy System Migration**: Moshik Levin reviewed engine release
consequences with Company leads and PMs, discovering that RingLead is
also using deprecated fields. A larger meeting with DaaS leads is
scheduled for next week to address these dependencies and plan migration
paths.

### **Strategic Challenges**

The technical solutioning for Enterprise Search v2 continues to evolve
as teams work through architectural decisions, with Menna Rashwan noting
that detailed milestones and sequencing remain in flux. The Search team
will need to take ownership of their GraphQL implementation once
federated search integration is in place, requiring careful coordination
between multiple engineering teams.

RingLead\'s usage of deprecated fields presents an additional complexity
for the engine release timeline, as Moshik Levin discovered this
dependency during consequence reviews. The team will need to investigate
the extent of this usage and develop appropriate migration strategies
alongside the planned DaaS transition work.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The GraphQL Query API release revealed that delivery represents only
half the impact equation. Linda Johannessen observed that compounding
value now comes from onboarding both humans and agents with clear
documentation and metadata context, shifting the team\'s focus toward
adoption enablement rather than just technical delivery.

Stakeholder feedback on the data platform approach has consistently
reinforced a metadata-first strategy with hardened architecture, strong
data quality, and cost controls. This validation from Customer Data
Catalog, Workbook, and DaaS teams supports the team\'s architectural
decisions and provides confidence in the October 15 API readiness
timeline.

Adwait Kirtikar\'s work with the DaaS team uncovered strong alignment
and excitement for platform integration, suggesting that the transition
from current delivery processes to platform-based models will have
internal support. The team\'s comprehensive documentation approach has
created clear pathways for stakeholder engagement and technical
implementation.

### **Cross-Team Dependencies**

Our work with the Search team on Enterprise Search v2 requires continued
technical deep-dives to finalize integration paths and architectural
decisions. The Search team must own their side of GraphQL implementation
with federated search, making their technical readiness essential for
overall platform success.

The DaaS leads meeting next week represents an important coordination
point for multiple workstreams, with Moshik Levin preparing consequence
analysis while Adwait Kirtikar continues process documentation. Success
here will determine migration timelines and resource allocation for
deprecated field remediation.

## **Looking Ahead**

Next week focuses on stakeholder alignment and technical deep-dives
across multiple fronts, with the DaaS leads meeting serving as a key
decision point for migration strategies and architectural choices.

Linda Johannessen will share the first version of schema and endpoints,
including logic for core data structures, enabling parallel workstreams
to begin implementation work. Meanwhile, Menna Rashwan will continue
architectural discussions with Search and Enterprise data teams to
refine milestones based on integration decisions. Marc Delurgio will
complete documentation review with stakeholders while Moshik Levin
investigates RingLead usage patterns and prepares for the DaaS leads
discussion.

The team is positioned to accelerate adoption of the released GraphQL
API through targeted onboarding and demonstrations while advancing the
metadata work that will make the platform truly valuable for both human
users and AI agents.

Source: Team 1-2-3 Operating Framework entries from September 8, 2025
