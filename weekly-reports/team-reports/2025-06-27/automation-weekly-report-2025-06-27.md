---
id: weekly-automation-2025-26
title: "Automation Weekly Report - June 27, 2025"
type: weekly-report
status: approved
team: automation
owner:
created: 2025-06-27
updated: 2026-01-06
week_ending: 2025-06-27
reporting_period: "June 23-27, 2025"
tags: ["weekly-report", "Q22025"]
---

# **Automation Executive Roundup - 6/27/2025**

## **Executive Summary**

**Strategic pivot to GTM Plays is accelerating our workflow
extensibility timeline.** Marc Frail has identified that this extension
of GTM Studio doesn\'t drastically alter our roadmap but elevates
previously secondary technical requirements to mission-critical status.
Meanwhile, Sam Massie completed the form builder design ahead of
schedule, creating our first building block for workflow extensibility.
Adam Peretz overcame documentation strategy challenges and is 70%
complete on new API endpoint documentation that will enable partner
integrations.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Sam Massie delivered the form builder UI design on target**,
completing high-fidelity mockups in Figma that provide the foundation
for custom data connectors as workflow steps. This represents a critical
building block in our automation extensibility strategy, enabling
workflows to connect to any external system rather than being limited to
current integrations.

**Adam Peretz pivoted documentation strategy mid-week and recovered
strong momentum**, developing a unified approach to handle shared
resources across API endpoints. After recognizing that duplicate field
definitions were creating maintenance challenges, the team established a
shared resource model that will streamline both internal development and
customer-facing documentation.

**Cross-team alignment accelerated on workflow data architecture**, with
Marc Frail making substantial progress on requirements gathering despite
competing priorities. The data mapping model work directly supports both
current workflow needs and the emerging GTM Plays requirements, creating
leverage across multiple strategic initiatives.

### **Goals & Progress**

**Workflow Extensibility**: Sam Massie achieved 95% completion on form
builder design, successfully creating mockups that will enable custom
data connectors to function as workflow steps. Engineering refinement is
scheduled for next week with Team 12, positioning this work to be
shovel-ready by week\'s end. The design accommodates both current API
integration needs and future query builder functionality being developed
by the workbook team.

**Data Architecture**: Marc Frail made partial progress on data mapping
model requirements due to GTM Plays priority shift, but critical
alignment meetings are scheduled for next week. The work focuses on
enabling dynamic field referencing between workflow steps, which becomes
essential for both standard workflows and the more complex GTM Plays use
cases.

**API Documentation**: Adam Peretz reached 70% completion on new ZI API
endpoint documentation despite mid-week strategy change. The unified
documentation model addresses a large volume of shared resources across
endpoints, creating more maintainable documentation that will better
serve partners building on our API.

### **Strategic Challenges**

**The GTM Plays initiative surfaced suddenly as a competing priority**,
requiring Marc Frail to balance data mapping requirements with
preliminary gap analysis for this new capability. While GTM Plays
doesn\'t fundamentally change our workflow roadmap, it elevates certain
technical blockers from nice-to-have to must-have status, particularly
around data flow complexity and cross-step referencing.

**Documentation tooling limitations are hampering API adoption**, with
Sam Massie noting that current Swagger docs provide insufficient detail
for developers. This impacts partner onboarding velocity and may require
investment in better documentation infrastructure or processes to
support our extensibility goals.

**Workflow sub-flows and functions present both opportunity and
complexity**, as Sam Massie\'s competitive analysis revealed that while
sub-flows are common in workflow tools, the form-based packaging
approach being developed appears unique. This raises questions about
whether the team is innovating in a valuable direction or
over-engineering a solution.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Form builder concepts extend beyond initial API integration scope**,
with Sam Massie discovering that the proposed workbook query builder
(potentially owned by Tushar\'s team) could leverage the same form-based
interface patterns. This suggests the form builder work has broader
platform implications and could become a standardized approach for
configurable integrations across multiple product areas.

**Output schema definition emerged as a missing component** in the form
builder flow, requiring addition of a view where users can define
expected API response formats. This discovery prevents potential rework
later and ensures the form builder provides complete action definition
capabilities from the start.

**Competitive differentiation opportunity identified in function
packaging**, as analysis of Power Automate, Workato, Make.com, and
Zapier revealed that while sub-flows are common, none offer the
form-based reusable step packaging being developed. This could position
the platform uniquely for complex automation scenarios.

### **Cross-Team Dependencies**

Our work with the Workflow core team remains critical for data mapping
model validation and GTM Plays gap analysis. Marc Frail needs continued
engineering alignment to finalize cross-step data requirements and
assess GTM Plays technical feasibility.

Coordination with Team 12 on form builder engineering refinement is
scheduled for next week, representing a key milestone for workflow
extensibility delivery. The design team\'s input will be essential for
finalizing the sub-flows and functions conceptual work that Sam Massie
is developing.

## **Looking Ahead**

Next week focuses on converting design work into engineering-ready
specifications while simultaneously addressing the GTM Plays
requirements that have elevated several technical priorities.

Marc Frail will complete data mapping requirements documentation with
engineering while conducting preliminary gap analysis for GTM Plays
capabilities. Sam Massie aims to achieve shovel-ready status for the
form builder through engineering refinement, sync with product and
design teams on sub-flows concepts, and conduct a comprehensive backlog
prioritization review. Adam Peretz will finalize the unified API
documentation model and create user-friendly endpoint guides leveraging
the shared resource framework.

The team is well-positioned to deliver foundational workflow
extensibility capabilities while adapting to emerging GTM Plays
requirements, with strong momentum on core deliverables and clear
visibility into remaining technical challenges.

*Source: Team 1-2-3 Operating Framework entries from 6/23 - 6/28*
