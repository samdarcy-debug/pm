---
id: weekly-admin-2025-29
title: "Admin Weekly Report - July 18, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-07-18
updated: 2026-01-06
week_ending: 2025-07-18
reporting_period: "July 14-18, 2025"
tags: ["weekly-report", "Q32025"]
---

# B. Huske\'s Executive Roundup - 7/14/2025

## Executive Summary

This week, the User Provisioning team successfully clarified the

**AI Usage Pricing model**, opting for **AI Credits** as the
intermediary currency, which is crucial for monetizing AI features and
accelerating Q3 goals for GTM Studio. This decision resolves a major
blocker and paves the way for scalable revenue streams. Additionally,
significant progress was made in finalizing

**RBAC export control requirements** for GTM Studio, addressing key
customer adoption barriers related to data quality concerns.

## Key Progress & Strategic Highlights

- **AI Usage Pricing Unblocked**: Brannen Huske\'s team finalized Q3
  planning by securing alignment on AI usage-based pricing, with AI
  Credits as the chosen currency. Adam\'s team will manage cost and
  value per feature, enabling the creation of necessary Salesforce SKUs
  for selling AI functionalities.

- **RBAC Export Control for GTM Studio**: Jessie Lindstrom achieved 100%
  completion on finalizing RBAC export control requirements and
  prototyping. This crucial work, addressing customer feedback about
  data quality concerns with CRM exports, has tickets scheduled for the
  next sprint, supporting GTM Studio\'s early access adoption.

- **\"Login As\" Work Advanced**: Josh Simon initiated stakeholder
  discussions for \"login as\" work, a key H2 goal. These discussions
  helped define scope and understand requirements, leading to plans for
  a pop-up box to gather data on \"login as\" usage, aiming to improve
  user experience and reduce support tickets.

## Challenges & Insights

- **Pricing Page Flow Complexity**: The team faces ongoing challenges in
  finalizing the pricing page flow due to diverse data requirements from
  lead generation and support stakeholders. Ensuring the feasibility of
  gathering all necessary data points is a current focus for engineering
  teams.

- **AuthZ Infrastructure Readiness**: Jessie Lindstrom identified a
  blind spot regarding the readiness of AuthZ for RBAC export control.
  While AuthZ could simplify implementation, its migration path and
  timeline are unclear, posing a risk of rework given the late
  July/early August launch target. Further investigation with
  engineering is required.

- **Chrome Extension API Issues**: A key learning was the discovery that
  the Chrome extension\'s loading behavior was causing excessive API
  calls by continually initializing itself on CRMs, leading to users
  hitting API limits. A flag was turned off to mitigate this.

- **SCIM User Provisioning Challenges**: It was learned that users
  created during trials are not automatically ported to paid versions,
  causing rejections during SCIM provisioning. This issue, currently
  under investigation, impacts the seamless transition of trial users to
  paid accounts.

## Looking Ahead

Next week, Josh Simon will connect with Sean to ensure Copilot v2
respects privacy settings. Brannen Huske will finalize AI Credit usage
with Ali Sadat and prepare NPI materials for the new AI Credits. Jessie
Lindstrom will continue investigating AuthZ infrastructure for RBAC
export control to ensure a smooth launch. These efforts are crucial for
GTM Studio monetization, user experience, and managing strategic
dependencies.
