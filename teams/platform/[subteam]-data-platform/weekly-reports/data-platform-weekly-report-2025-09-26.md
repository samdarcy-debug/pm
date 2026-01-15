---
id: weekly-data-platform-2025-39
title: "GTM Data Platform Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

## **This Week\'s Progress**

### **Key Momentum Areas**

Linda Johannessen completed a strategic overview for MCP and API
roadmapping for executive review while progressing the externalization
path for GraphQL APIs. Her metadata API work reached a significant
milestone with first-round validation from integration engineering teams
and new schema successfully shared with data producers. Engineers across
multiple teams are now actively requesting GraphQL access, signaling
authentic adoption momentum that validates our platform strategy.

Menna Rashwan defined the initial MVP proposal for search operators and
standardized search behavior across the platform, establishing a
foundation for Federated Search integration with GraphQL. While app
teams remain focused on GA releases, her proactive approach to
identifying and prioritizing common search use cases will accelerate
integration planning without waiting for full app team availability.

Moshik Levin finished the first draft of a comprehensive product brief
for Location Matching that aligns requirements from both New Company
Creation and Workbooks initiatives. His work through milestones and
timelines revealed the necessity of perfectly coordinating the January
Company Cube release with changes to Company Master Data Enrichment API
and Offline Enrichments, providing the roadmap clarity needed for Q4
execution.

### **Goals & Progress**

**API Development and Integration**: Linda continues making strong
progress on the GraphQL and metadata API work, with the staging API now
validated and follow-up sessions scheduled with data producers. The
growing engineering demand for GraphQL access demonstrates real
traction, though tight deadlines and new midstream additions are
creating unresolved priority conflicts that need executive attention.
Her collaboration with Adam\'s team on GraphQL public gateway scoping
and alignment with Frank and Majed on MCP design timing will shape our
external API strategy.

**Search Platform Architecture**: Menna\'s work on search operators
represents solid foundation-building for platform consistency. Her
recognition that search use cases should drive operator behavior, rather
than the reverse, shows strategic thinking. The challenge remains app
team bandwidth limitations, but her decision to take first pass at use
case identification keeps momentum while respecting other teams\' GA
pressures. Next week\'s focus on identifying MVP use cases will directly
inform GraphQL integration priorities.

**Location Matching and Data Consolidation**: Moshik\'s consolidated
product brief brings clarity to a complex multi-initiative challenge
involving Company Cube, Workbooks, and New Company Creation. His
discovery that we must perfectly align January timelines across multiple
systems highlights both constraint and opportunity. The work reveals the
longer-term vision of consolidating into a single endpoint that handles
published/unpublished data with unified location matching capabilities.

### **Strategic Challenges**

The team faces mounting execution pressure from tight deadlines combined
with new requirements being added midstream (eg Salesforce Connector in
GraphQL), creating priority conflicts that risk delivery quality.

**Executive Summary**

Linda Johannessen delivered a comprehensive strategic slide deck for MCP
and API roadmapping while advancing metadata API validation with initial
engineering feedback. However, the team faces mounting pressure from
tight deadlines and midstream priority additions that are creating
execution conflicts. Marc Delurgio initiated record credit management
analysis for GraphQL API, highlighting the need for sharper focus amid
competing demands. The positive signal: engineers are now actively
requesting GraphQL access, indicating growing adoption momentum that
validates our platform direction.

## **This Week\'s Progress**

### **Key Momentum Areas**

Marc Delurgio completed and distributed comprehensive documentation
covering data access rules for both the Query API and Search
functionality. This work received stakeholder review and represents a
significant step toward ensuring adequate data privacy implementation
across the platform. The documentation now provides clear guidelines for
how data access should be managed as we expand platform capabilities.

Menna Rashwan successfully identified and documented all current
Search-related data access and entitlement rules for third-party data
used in ZoomInfo. Working closely with core engineering and product
stakeholders, she validated these rules and discovered that existing
platform-level privacy functionality can potentially be leveraged to
support some of the 3P data access rules within Search, minimizing
duplication and ensuring alignment with broader platform standards.

Linda Johannessen delivered new dataset schema definitions to consumers
and has the staging API targeted for next week. Her work on federated
search metadata mapping into the GraphQL API for proof-of-concept
purposes demonstrates strong progress, and she has begun the Website
Journey Signal model analysis that will inform future funnel-style
insights capabilities.

### **Goals & Progress**

**Query API and Metadata Development**: Linda continues making solid
progress on the metadata model and API work, with the new dataset schema
now delivered to consumers and staging API targeted for next week
completion. The federated search metadata has been successfully mapped
into GraphQL API for POC demonstration, showing the technical approach
is sound. However, connecting external sources like Salesforce into
GraphQL for Copilot requires API-level mapping beyond just schema
alignment, raising questions about the complexity of this integration
path.

**Match Service and Location Matching**: Moshik Levin followed up with
stakeholders regarding changes in location matching to ensure minimal
impact on current operations. He has initiated the official release
change management process, targeting November for implementation. The
team will make final decisions on Monday regarding which dispositions to
use for match reasons, then shift focus to consolidating new
requirements for location matching in Q4 initiatives including Workbooks
and New Company Creation.

### **Strategic Challenges**

The External API team\'s support for GraphQL remains a dependency that
could impact externalization timelines for the November release. While
there\'s been progress on establishing milestone plans, the complexity
of supporting GraphQL in the external-facing API requires careful
coordination and may need alternative approaches if timelines become
constrained. This affects our ability to deliver the full metadata API
experience externally as planned.

Connecting external data sources like Salesforce into the GraphQL API
for Copilot applications presents technical complexity beyond initial
expectations. The integration requires API-level mapping rather than
just schema alignment to ensure a clean user experience, which raises
questions about whether this integration path should be pursued or if
simpler alternatives might be more appropriate for initial releases.

The location matching work that Moshik is leading involves careful
change management to minimize impact on existing customers. While
progress is being made toward November implementation, the team must
balance improving matching capabilities with maintaining consistency for
current users, requiring ongoing coordination with DaaS leads and other
stakeholders.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team discovered that existing platform-level privacy functionality
can potentially be leveraged and mapped to support some of the 3P data
access rules within Search. This finding by Menna represents a
significant opportunity to minimize duplication of effort and ensures
better alignment with broader platform standards as we scale Federated
Search capabilities. Rather than building separate privacy controls for
Search, we can build upon existing infrastructure.

Marc\'s comprehensive documentation work revealed the importance of
establishing clear data access rules early in platform development.
Having these guidelines documented and reviewed by stakeholders provides
a foundation for consistent implementation across different platform
components and helps ensure that privacy considerations are built into
the architecture rather than added as an afterthought.

The federated search metadata mapping work has shown that GraphQL
integration is technically feasible, but the complexity of connecting
external sources like Salesforce requires more sophisticated API-level
mapping than initially anticipated. This suggests that we may need to
phase the rollout of different data sources or develop more
sophisticated integration patterns for complex external systems.

### **Cross-Team Dependencies**

Our work with the External API team on GraphQL support continues to be
important for the November externalization timeline. We need clear
commitments on GraphQL scope and delivery timelines to ensure the
metadata API can be properly externalized. The complexity of this
integration may require exploring alternative approaches or adjusting
timelines to ensure successful delivery.

The Unified Profile work requires continued collaboration with
Application product teams and design leadership to ensure proper
integration into ZoomInfo applications. Adwait\'s alignment with Ant
Cuomo provides a good foundation, but broader team engagement will be
needed to ensure the unified profile experience is consistent and
intuitive across applications.

## **Looking Ahead**

Next week focuses on delivering the staging API for Linda\'s metadata
work and completing the final documentation and decision-making for
Moshik\'s location matching changes. The team will also continue
advancing the federated search GraphQL integration and extend the work
into Website Journey Signal analysis.

Marc will work with stakeholders to finalize any remaining data access
rule questions and record credit management and ensure the documentation
is ready to support implementation. Linda will onboard new vertical and
signal datasets while preparing for the October Workbook integration
milestone. The team will also begin extending federated search
capabilities and continue Website Journey Signal analysis to scope model
changes for enhanced funnel-style insights.

The week ahead will be crucial for maintaining momentum on the October
marketplace delivery while ensuring that the foundational data access
and privacy work is properly implemented. Success depends on continued
stakeholder engagement and careful management of external dependencies,
particularly around GraphQL support timelines.

*Source: Team 1-2-3 Operating Framework entries from September 15, 2025*
