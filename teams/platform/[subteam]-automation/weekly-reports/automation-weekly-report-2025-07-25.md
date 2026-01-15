---
id: weekly-automation-2025-30
title: "Automation Weekly Report - July 25, 2025"
type: weekly-report
status: approved
team: automation
owner:
created: 2025-07-25
updated: 2026-01-06
week_ending: 2025-07-25
reporting_period: "July 21-25, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Automation Executive Roundup - 7/25/2025**

## **Executive Summary**

**MCP authentication limitations are forcing architectural compromises
while GTM Plays alignment accelerates toward execution.** Adam Peretz
discovered that the current MCP specification only supports Okta-hosted
login pages, creating a significant limitation for SSO customers and
potentially delaying the board demonstration planned for month-end. Sam
Massie successfully transitioned workflow frontend ownership and
identified three must-have improvements for GTM Plays, while Marc Frail
achieved strong tactical alignment on triggers and actions needed to
support the platform.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Sam Massie completed the workflow frontend transition**, successfully
taking ownership of core workflow experience items and identifying the
critical path for GTM Plays readiness. Through coordination with design
and engineering, three must-have improvements were prioritized: data
mapping from previous steps, extensible trigger/action library with
forms capability, and generic filtering/branching functionality.

**Marc Frail achieved 80% completion on GTM Plays JIRA organization**,
making substantial progress on transferring the prioritized initiative
list from Google Sheets into JIRA and linking it to the broader GTM
Studio program. Strong tactical alignment was maintained on workflow
capabilities needed to support GTM Plays, including a socialized
definition of required triggers and actions.

**Cross-functional alignment strengthened on GTM Plays requirements**,
with the GTM Plays team sharing a comprehensive list of triggers and
actions they believe are needed, most of which depend on other teams.
This visibility into dependencies enables better coordination and
prevents duplicate work across the platform.

### **Goals & Progress**

**MCP Authentication**: Adam Peretz achieved 50% completion due to
discovering fundamental limitations in the MCP specification. While
authentication functionality can be implemented, the requirement to use
Okta-hosted login pages instead of self-hosted pages eliminates SSO
support for enterprise customers, affecting meaningful adoption for the
highest-value customer segment.

**GTM Plays Execution Planning**: Marc Frail reached 80% completion on
JIRA board population, successfully organizing the tactical aspects of
workflow support for GTM Plays. The work establishes clear tracking for
execution priorities while maintaining alignment on capabilities needed
across the platform.

**Workflow Frontend Ownership**: Sam Massie completed the transition of
workflow frontend responsibilities, establishing clear understanding of
the must-have improvements needed for GTM Plays success. The
prioritization focuses development efforts on the highest-impact
capabilities rather than spreading resources across nice-to-have
features.

### **Strategic Challenges**

**MCP authentication constraints threaten enterprise adoption**, with
the protocol\'s limitation to Okta-hosted pages preventing SSO
integration that enterprise customers require. This represents a
fundamental platform limitation rather than an implementation choice,
forcing the team to choose between launching with limited enterprise
functionality or waiting for MCP protocol maturation.

**Board demonstration timeline creates execution pressure**, with
Dominic planning to present MCP functionality to the board of directors
by month-end. The authentication limitations discovered this week make
the demo timeline aggressive and potentially unrealistic, requiring
careful expectation management with leadership.

**Ownership alignment remains incomplete for complex GTM Plays flows**,
despite strong tactical agreement on required capabilities. Marc Frail
noted that broader alignment sessions are still needed on ownership of
complex workflows and socialization of how these flows will function
between workflows and plays.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**MCP protocol maturity lags enterprise integration requirements**, with
current authentication limitations preventing the self-hosted login
pages necessary for SSO functionality. While 80% of customers can be
served with Okta-hosted authentication, the limitation excludes
enterprise customers who represent the highest value segment for API
adoption.

**GTM Plays dependencies are largely external to the automation team**,
based on the trigger and action list shared by the GTM Plays team. This
insight suggests the automation team\'s role is more integrative than
developmental, focusing on enabling capabilities built by other teams
rather than creating new automation primitives.

**Frontend workflow improvements have clear prioritization for GTM
Plays**, with data mapping, extensible triggers/actions, and
filtering/branching identified as must-haves versus nice-to-haves. This
clarity enables focused development rather than attempting to improve
all workflow capabilities simultaneously.

### **Cross-Team Dependencies**

Frank\'s authentication research is critical for determining MCP launch
feasibility, with potential workarounds being investigated to overcome
Okta-hosted page limitations. The timeline pressure from the board
demonstration adds urgency to finding viable solutions.

Design and engineering coordination was essential for Sam Massie\'s
successful transition of workflow frontend ownership, demonstrating
effective cross-functional collaboration when clear scope and priorities
are established.

## **Looking Ahead**

Next week focuses on resolving MCP authentication constraints while
advancing GTM Plays execution planning despite upcoming PTO schedules.

Adam Peretz will continue investigating authentication options with
Frank to determine how closely the Okta-hosted experience can
approximate current functionality, aiming to maximize initial launch
impact while planning for long-term protocol improvements. Marc Frail
will complete JIRA organization and continue broader alignment sessions
on complex workflow ownership patterns.

Sam Massie will review remaining H2 initiatives to clarify ownership
before going on leave Wednesday through Friday, ensuring continuity of
workflow frontend development while he\'s out. The authentication
investigation represents a critical decision point for MCP launch
strategy, determining whether to proceed with limited enterprise
functionality or adjust timeline expectations for the board
presentation.

*Source: Team 1-2-3 Operating Framework entries from 7/21 - 7/25*
