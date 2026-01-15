---
id: weekly-admin-2025-32
title: "Admin Weekly Report - August 08, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-08-08
updated: 2026-01-06
week_ending: 2025-08-08
reporting_period: "August 4-8, 2025"
tags: ["weekly-report", "Q32025"]
---

## Executive Summary

This week, a key strategic decision was made to centralize the price
book for AI credits to support enterprise readiness and scalability.
However, the ownership of this centralized system is still an open
question. Since the prices are feature dependent and optimizing reduces
ZI and Customer Cost, ownership should be with the team with expertise
to optimize the costs. There is a meeting scheduled for next week to
resolve this. Additionally, new requirements have emerged regarding the
segmentation of AI credits and their impact on revenue reporting, which
requires further discussion with key stakeholders.

## This Week\'s Progress

### Key Momentum Areas

Jessie Kain Lindstrom made progress on the high-leverage goal of
finalizing the decision on the AI credit price book. The team achieved
alignment on a centralized model for scalability and enterprise
readiness, moving the goal to 50% completion. This decision is
significant because it aligns with industry standards for
enterprise-grade companies.

Brannen Huske continued work on closing out superseding contracts and
revenue reporting, with progress made on the next stage of AI credits. A
key discovery was the need to segment AI credits into \"usage-based\"
and \"non-usage-based\" categories, which will be a focus for next
week\'s discussions.

Josh Simon has begun working toward a product review of limiting the
\"login as\" feature, which is an impactful change for the business. He
is working on his goal of gathering more information to limit access and
meet customer trust and up-market goals. This week, he shadowed various
CX organizations to understand how they use the \"login as\" feature.

### Goals & Progress

**AI Credit Price Book**: Jessie Kain Lindstrom has reached 50%
completion on the goal to finalize the decision on where the AI credit
price book should live. The decision was made to centralize it for
enterprise readiness, but the team ownership piece is still an open
question to be addressed next week.

**Revenue Reporting & Contracts**: Brannen Huske\'s goal to close out
superseding contracts and correctly report revenue to SAP is
progressing. A major complication arose this week with the discovery
that AI credits need to be segmented into usage-based and
non-usage-based categories, which will require further discussion with
dependent teams..

**Login as Feature**: Josh Simon has completed initial discovery by
shadowing various CX organizations to see how they use the feature. Next
week, he will continue shadowing different groups to gain a better
perspective on what is needed to restrict access.

### Strategic Challenges

A significant challenge is the ownership of the centralized AI credit
price book. While the team has decided to centralize it, a clear owner
has not been assigned, and this is a blocker that requires a
conversation next week to resolve. Jessie Kain Lindstrom notes that
while a centralized approach is good for scalability and auditability,
it could prevent other teams from moving quickly. A decentralized
approach, conversely, would allow teams to move more quickly but might
create issues with scalability and auditability.

Brannen Huske has identified a complication related to AI credits and
revenue reporting for SAP. The team discovered a need to segment credits
into usage-based (additional credits purchased) and non-usage-based
(included in the base bundle). Additionally, for multi-year deals, the
credits need to be accessible at specific cadences to prevent customers
from spending all their credits upfront and then churning or going into
collections. This complexity requires discussions with Mark Harris,
Garrett Cummins, and the GTM Tech team to determine necessary guardrails
and reporting methods.

Another challenge is an ongoing issue with Snowflake users being logged
out or \"bounced\" from the platform sporadically. Josh Simon is working
with the Dev team and has additional calls scheduled with the customer
next week to understand the problem better. This blind spot is a
priority for the login team.

## Strategic Insights

### Key Learnings & Discoveries

Jessie Kain Lindstrom discovered that there are two schools of thought
in the AI industry regarding architectural design: a \"move fast\"
decentralized approach and a \"scalable, enterprise readiness\"
centralized approach. The team decided to adopt the centralized model,
which is the industry standard for enterprise-grade companies. This
decision, while not irreversible, will have long-term repercussions on
either the speed of development or the scalability and auditability of
the system.

Brannen Huske\'s team learned that superseding contracts and revenue
reporting for usage-based pricing require careful handling to avoid
incorrect reporting of realized revenue to SAP, which could negatively
affect how the company capitalizes. A key finding was the necessity to
segment AI credits based on whether they are included in a base bundle
or purchased additionally, as this affects how revenue is reported. The
team also learned that multi-year deals require the optionality to
mature AI credits at specific cadences to mitigate financial risk.

### Cross-Team Dependencies

**Mark Harris, Garrett Cummins, and the GTM Tech team** on revenue
reporting is critical for ensuring our usage-based pricing model is
correctly handled. Discussions are needed to determine the guardrails,
reporting methods, and impact on skew creation and quote flow. The team
also needs to get alignment on how Copilot v.2 will be enabled to create
the correct packaging, if needed.

## Looking Ahead

The primary focus for next week is to resolve the open questions and
challenges identified this week.

Jessie Kain Lindstrom will be meeting with different engineering and
product teams to get a resolution on who will own the centralized AI
credit price book. This decision is crucial for moving forward with the
engineering scoping. Brannen Huske will continue to talk with Mark
Harris, Garrett Cummins, and the GTM Tech team about the guardrails and
reporting methods needed for the new segmentation of AI credits. This is
a critical step to ensure that revenue is reported correctly to SAP and
to finalize the tickets for a September completion. Josh Simon will
continue to shadow more groups to gain a better perspective on what is
needed to start restricting access to the \"login as\" feature and will
have additional calls with the customer to solve the Snowflake login
issue.
