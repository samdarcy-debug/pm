---
id: weekly-automation-2025-43
title: "Automation Weekly Report - October 24, 2025"
type: weekly-report
status: approved
team: automation
owner:
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Automation Executive Roundup - 10/24/2025**

## **Executive Summary**

**MCP credit consumption concerns threaten enterprise adoption while GTM
Plays requirements clarify action library priorities.** Adam Peretz
discovered that the stateless MCP server architecture prevents credit
estimation before queries execute, with beta partners refusing adoption
unless guardrails are implemented to prevent runaway credit consumption.
Sam Massie completed DoubleO alignment work, revealing that GTM Plays
requires deterministic action libraries with user inputs complementing
agentic capabilities, with Slack, Outreach, and Salesloft activations
prioritized. Marc Frail is on track to launch Global Event Bus with
initial GTM CDC events by next week\'s end, enabling broader platform
event consumption.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Sam Massie achieved comprehensive DoubleO alignment**, completing
synchronization with the team on Plays requirements and reordering the
Workflows/Automations H2 backlog to support GTM Plays priorities. The
clarity on deterministic actions versus agentic steps enables focused
execution on the most valuable integration points.

**Marc Frail advanced Global Event Bus toward production launch**,
maintaining schedule for initial GTM CDC events to go live by end of
next week. The team also released backstage tooling that provides
UI-based event registration for publishers, simplifying the event
publishing workflow significantly.

**Adam Peretz pivoted to high-priority partnership automation**,
deprioritizing original week goals to focus on Developer Portal
enhancements that enable automated partner application publishing. The
partnerships team is ready for enhanced data collection and cross-team
API integration to streamline marketplace presence.

### **Goals & Progress**

**DoubleO Integration Alignment**: Sam Massie completed 100% of
understanding how ZoomInfo automation supports Plays and DoubleO
roadmap, establishing clear prioritization frameworks. The discovery
that activations like Slack, Outreach, and Salesloft are high priority
informs immediate execution focus.

**Global Event Bus Production Launch**: Marc Frail made substantial
progress with GTM CDC on track for next week\'s production launch. The
namespace-based CDC architecture continues positive progression through
staging, representing improved scalability over monolithic CDC
approaches.

**Enterprise API Migration Planning**: Adam Peretz shifted to scoping
Bulk Search/Enrich API migration to ZI API Platform and drafting new
monetization models. This work addresses the largest revenue-driving
enterprise customers who require greater scale than synchronous REST
APIs provide.

### **Strategic Challenges**

**MCP credit consumption unpredictability blocks enterprise adoption**,
with Adam Peretz discovering that the stateless server architecture
prevents cost estimation before queries execute. Beta partners
specifically cited concerns about queries that could consume thousands
of credits in seconds, refusing to enable access without guardrails that
engineering indicates won\'t be easy to implement.

**Sales team lacks Claude access for customer demonstrations**, with
Mike Fawkes and other salespeople unable to demo MCP capabilities to
strategic customers. Adam Peretz is working with Rowan Bailey to
establish access protocols, but the current infrastructure doesn\'t
support sales team demonstration needs.

**API versioning policy requires leadership decision**, as Adam Peretz
identified multiple viable approaches with distinct trade-offs around
versioning granularity and legacy support timelines. The decision
affects platform evolution flexibility and customer migration
complexity.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Deterministic actions complement rather than replace agentic
capabilities**, as Sam Massie discovered that GTM Plays requires a
library of functions with explicit user inputs alongside agentic steps.
This architectural clarity enables focused development on the right
abstraction layers.

**MCP cost control becomes adoption blocker for enterprise segment**,
with beta partner feedback revealing that unpredictable credit
consumption creates unacceptable risk for enterprise customers. The
stateless architecture optimizes for simplicity but creates cost
management challenges requiring engineering investment.

**Backstage tooling democratizes event publishing**, with Marc Frail
noting that UI-based event registration simplifies the publisher
experience significantly. This platform investment reduces friction for
teams contributing to the event ecosystem.

**Partnership automation readiness drives developer portal evolution**,
as Adam Peretz identified that partnerships team needs enhanced data
collection and automated publishing workflows. The developer portal
becomes the integration point for marketplace presence management.

### **Cross-Team Dependencies**

DoubleO team coordination continues with onsite meeting scheduled in
Waltham next week for Sam Massie to narrow Plays requirements further,
ensuring continued alignment on action library priorities and
integration patterns.

Rowan Bailey collaboration is essential for resolving Claude access
issues that prevent sales demonstrations, affecting the team\'s ability
to showcase MCP capabilities to strategic enterprise customers.

Partnership team integration requires Developer Portal API enhancements
that enable automated data transmission for marketplace publishing, with
Andres coordinating cross-team workflows.

## **Looking Ahead**

Next week focuses on finalizing API versioning proposals while advancing
Global Event Bus production launch and deepening DoubleO integration
planning.

Adam Peretz will finalize the API versioning proposal for leadership
review when Ali returns, addressing critical policy questions about
versioning granularity and legacy support timelines. Marc Frail will
continue building the initial library of data connectors for GTM Studio,
expanding the action ecosystem that supports GTM Plays requirements.

Sam Massie will attend the onsite meeting with DoubleO in Waltham to
narrow Plays requirements, deferring workflow micro front end work to
focus on action forms that directly support strategic objectives. The
MCP credit consumption challenge requires engineering coordination to
develop guardrails that enable enterprise adoption while maintaining the
simplicity benefits of stateless architecture.

*Source: Team 1-2-3 Operating Framework entries from 10/20 - 10/24*
