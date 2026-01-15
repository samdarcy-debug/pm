---
id: weekly-automation-2025-46
title: "Automation Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: automation
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Automation Executive Roundup - 11/14/2025**

## **Executive Summary**

**Data connector library launches to production while no-code function
builder prototype demonstrates component reusability.** Marc Frail
successfully launched the initial data connector library and enabled
website visitor tracking with buyer ID support from the global event
bus. Sam Massie completed no-code function builder prototype and
engineering kickoff, discovering significant component reuse
opportunities across existing integration infrastructure.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Marc Frail achieved production launch of data connector library**,
delivering the initial set of connectors to customers and enabling demos
and visualization capabilities for GTM Studio. Additionally, website
visit tracking with buyer ID via Global Event Bus will reach staging
next week, supporting export to webhook functionality for enterprise
data movement requirements.

**Sam Massie delivered a no-code function builder prototype and
initiated engineering collaboration**, creating a video demonstration
and holding kickoff refinement with the apps engineering team. The
prototype reveals that function building can leverage existing
components from data connectors and integrations, including stepper UI,
input/output mapping, workflow builder, and integration configurations.

**Workflows charter evolution progresses**, with Marc Frail completing a
draft one-pager that will undergo review iteration. This strategic work
positions the team to align focus and potentially rebrand away from
\"workflows\" terminology to better reflect evolved capabilities and
market positioning.

### **Goals & Progress**

**Data Connector Ecosystem Launch**: Marc Frail completed production
deployment of the initial connector library, enabling customer access
for demos and early adoption. The export to webhook capability
supporting IBM requirements will reach staging next week, addressing
enterprise client demands for UI-less data movement.

**No-Code Function Builder**: Sam Massie completed detailed requirement
definition for automation functions supporting Plays, including detailed
workflow mapping for Salesforce export scenarios and AI prototype
showcasing UX/UI concepts. Engineering refinement kickoff ensures
DoubleO agents have necessary tools for successful launch.

### **Strategic Challenges**

**Documentation portal publishing proves more complex than
anticipated**, requiring Marc Frail to invest additional effort beyond
initial expectations. The complexity likely relates to doing this the
first time vs a core process problem.

**Discovery flows remain undefined for GTM Studio**, with Marc Frail
noting that data connector discoverability within audience builder and
GTM Studio can be improved. This UX gap affects how customers find and
utilize available integration capabilities.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Component reusability accelerates no-code function development**, as
Sam Massie discovered that function builder work can leverage
substantial existing infrastructure from data connectors and
integrations. This architectural insight reduces development complexity
while ensuring consistency across platform capabilities.

**Enterprise data movement requirements differ from traditional workflow
patterns**, as website visit export to webhook capability demonstrates
demand for automated data egress without UI interaction. This represents
a distinct use case requiring different architectural approaches than
traditional workflow orchestration.

### **Cross-Team Dependencies**

Andres and integrations team coordination is essential for defining
external views and connector discovery flows, ensuring appropriate
customer-facing abstractions over implementation details.

Global Event Bus team synchronization continues for filtering and
enrichment work, expanding event processing capabilities to support
richer automation scenarios.

## **Looking Ahead**

Next week focuses on formalizing enhancement roadmaps while refining
function requirements with core engineering and completing analytics
infrastructure work.

Marc Frail will formalize the outstanding data connector enhancement
roadmap, consolidating insights from implementation experience into
structured planning. He will resync with the Global Event Bus team on
filtering and enrichment capabilities, coordinate with integrations team
on connector discovery in audience builder and GTM Studio, and publish
documentation for exposed data connectors to the developer portal.

Sam Massie will refine function requirements with the core engineering
team, advancing beyond the apps team kickoff to ensure all platform
components align on implementation approach and architectural patterns.

Adam Peretz will continue working on analytics capabilities, completing
the data cleanup required to make useful analysis possible and advancing
both Tableau dashboard development and longer-term ZI Chat data pipeline
planning.

The convergence of production connector library, no-code function
builder prototype, and advancing analytics infrastructure creates
momentum for sophisticated automation capabilities, while external view
requirements and data complexity challenges highlight the operational
maturity needed to support enterprise-scale platform delivery.

*Source: Team 1-2-3 Operating Framework entries from 11/10 - 11/14*
