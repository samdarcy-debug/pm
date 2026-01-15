---
id: weekly-intelligence-2025-34
title: "Intelligence Weekly Report - August 22, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-08-22
updated: 2026-01-06
week_ending: 2025-08-22
reporting_period: "August 18-22, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Intelligence Team Executive Roundup - August 22, 2025**

## **Executive Summary**

The Intelligence Team achieved a major milestone with Paychex data going
live in production while identifying scaling concerns across multiple
MCP services that need attention before broader rollout. The team
successfully consolidated efforts around the GTM context service with
Ryan Stevens providing immediate team resources for Rowan, but billing
infrastructure for AI credits remains in design phase only, creating
risk for external launches planned for October.

## **This Week\'s Progress**

### **Key Momentum Areas**

Lars Vedo\'s team made significant progress on the no-code agent and
artifact builder, with a demo scheduled to showcase how internal teams
can test agents and toggle embed options in real-time. This directly
addresses the proliferation challenge of having 5+ teams embedding chat
across the organization.

Rowan Bailey successfully orchestrated the GTM context service kickoff,
immediately securing resources from Ryan Stevens (Vinod, Carter, Topher,
and Zheng) and establishing a clear promotion path from internal to
external tool releases with Frank Shaw\'s MCP Gateway service design.
The team exposed three new tools to the internal MCP, with more
scheduled to be made available for use externally (e.g in Claude) by the
end of next week.

Ryan Stevens achieved a 90% resolution of performance reliability issues
by identifying and fixing critical Python layer bottlenecks that were
causing synchronous blocking operations in loops, resulting in
dramatically more consistent performance across staging environments.

### **Goals & Progress**

**Platform Performance & Reliability**: Ryan Stevens identified material
problems in the Python layer where Pydantic initialization in loops was
causing severe performance degradation. By profiling code and removing
hotspots, the team eliminated agent-side throttling issues and achieved
consistent performance. The team intentionally stressed staging to one
server/process to replicate and diagnose issues more effectively.

**Customer Rollout & Data Integration**: Danny Pan successfully moved
Paychex data to production and prepared data for over a dozen tenants in
phases A, B, and C of the EA cohort rollout. However, the team noticed
concerning ETL pipeline slowdowns that need investigation before
full-scale deployment.

**Context Service Architecture**: Rowan Bailey is taking over
requirements for account brief and summary updates and aligning these
requirements with work on the GTM config side. The team established that
admins should validate inferred context and fill gaps that cannot be
determined from other sources, creating a more robust context foundation
for agent responses.

### **Strategic Challenges**

The team faces an emerging scale crisis as Lars Vedo highlighted that
multiple services being integrated via MCP may not be designed for the
200,000+ record volumes the platform will generate. Many endpoint
creators don\'t realize the scale requirements, and there\'s no
systematic review of rate limiting, throttling, or performance
capabilities across integrated services.

Rowan Bailey identified that token monitoring and AI credit billing
infrastructure remains in design phase only, while data access
capabilities are ready for release. This misalignment between technical
readiness and billing capability poses significant risk for the
September/October external launch timeline.

The proliferation of MCP tools presents an orchestration challenge, with
potentially hundreds of individual tool calls that the orchestrator must
choose between. The team needs to solve semantic separation of
descriptions and create dynamic short lists of relevant tools for given
contexts before this becomes unmanageable.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The cross-team learning session between Lars Vedo, Rowan Bailey, Ryan
Stevens and the ZI Chat team revealed that making artifacts and agents
editable by end users has been their biggest unlock, with surprising
insights about which users create the best artifacts. This validates the
team\'s investment in the no-code builder approach.

Ryan Stevens\' performance investigation revealed that seemingly minor
implementation choices in Python can have dramatic compound effects at
scale. The Pydantic initialization issue demonstrates how
language-specific optimizations that don\'t matter in other environments
can become critical bottlenecks in production Python deployments.

The team discovered through the Paychex demo that staging environment
decisions by other teams (Workbooks) can cascade into customer-facing
impacts, highlighting the need for better cross-team coordination on
demo environments and customer data handling protocols.

### **Cross-Team Dependencies**

Our work with the GTM data store team on integrating semantic data
continues to be critical for unlocking context capabilities across the
platform. Danny Pan is coordinating data transfer next week, with the
GDM team excited and actively preparing to receive our data - this
integration will be a major unlock for making our semantic layer
accessible to all GTM services.

The GTM config collaboration with Megan and Richie is progressing well,
with Rowan Bailey aligning account brief and summary requirements to
work backwards from key agent questions like competitive positioning and
win/loss reasons. This coordination ensures admins can validate inferred
context and fill critical gaps, creating a stronger foundation for agent
responses. Ryan McMaster will continue this alignment next week after
receiving Rowan\'s notes from the hour-long planning session.

The design systems team partnership on universal component creation,
particularly around AI credit consumption patterns, is essential for
consistent user experience across all our touchpoints. Ryan McMaster is
addressing their confusion about how new AI credits differ from existing
credit consumption, with a sync scheduled Monday to establish broader
patterns that will benefit all teams implementing AI features.

The emailer team integration represents a successful collaboration
model, with Lars Vedo\'s team unblocking Gabe to create their first
cloned orchestrator agent for email generation. This team is now running
at full speed and will soon demonstrate how our enhanced context layer
improves messaging quality.

## **Looking Ahead**

Next week\'s focus centers on H2 roadmap realignment as Rowan Bailey
noted that significant changes over the past month require clarity on
September/October launch milestones across all teams.

The immediate priorities include conducting a systematic scale review of
all MCP endpoints and services before broader rollout, accelerating the
token monitoring and billing system design with Adam Smith\'s team to
achieve feature parity with technical capabilities, and expanding the
no-code agent builder to enable PMs and other non-technical users to
test new MCP endpoints without engineering involvement.

The team will also prioritize getting semantic data into the GDM store
as Danny Pan coordinates with the excited GDM team, representing a major
unlock for data accessibility across the platform.

*Source: Team 1-2-3 Operating Framework entries from August 18-22, 2025*
