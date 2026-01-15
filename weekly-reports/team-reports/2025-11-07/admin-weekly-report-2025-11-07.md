---
id: weekly-admin-2025-45
title: "Admin Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

## Executive Summary 🚀

The high-leverage goal of cutting over to **AI action credits** in
production was a success, with both internal teams and Early Access (EA)
customers now generating actual usage data on the AI platform. The
immediate challenge is a security and billing risk identified with the
**\"login as\" feature**, where internal users inadvertently charge
customer credit lots after impersonating a customer. Jessie Kain
Lindstrom is prioritizing a plan next week to deprecate the current
\"login as\" functionality and implement the new **admin impersonation
feature**. Concurrently, Brannen Huske is strategically leveraging the
impending 2026 cost increase for **Legacy SSO infrastructure** to create
a pricing \"wedge,\" incentivizing customers to migrate to the newer,
more secure infrastructure.

## This Week\'s Progress

### Key Momentum Areas

Jessie Kain Lindstrom successfully deployed the AI action credits in
production, which is crucial for tracking utilization and is already
capturing real usage from internal teams and EA customers. This
milestone is the first step toward validating the platform\'s value and
supporting the upcoming billing structure.

Brannen Huske advanced the **SCIM implementation** by meeting with
Zscaler, establishing a satisfactory path forward for moving to a
reporting structure user group and defining basic reporting standards.
This progress on identity and access management is essential for
improving the GTM Studio and GTM Workspace login experiences.

A strategic breakthrough was the formulation of a pricing strategy to
drive the migration off **Legacy SSO**. Brannen Huske initiated
conversations with the packaging and pricing group to utilize the extra
infrastructure costs starting in 2026 as a tool to incentivize customers
to move to a newer, more secure and feature-rich login experience.

### Goals & Progress

**AI Credit Provisioning**: Jessie Kain Lindstrom successfully cut over
to **AI action credits** in production, achieving the high-leverage goal
for the week. The platform is now capturing actual usage data, though no
customers have paid for the credits yet. A short-term solve is being
implemented to address the \"login as\" issue by adding the existing
banner to Workspace.

**Login Experience Modernization**: Brannen Huske refocused on improving
GTM Studio and GTM Workspace login items. The team made progress on
**SCIM implementation** by aligning with Zscaler, which involved moving
to groups for management and defining a basic API for license reporting.
Brannen also began work to create options to push people off **Legacy
SSO** to enable improved features like passkeys and biometrics.

**AI Credit Promo Definition**: A blocker related to the unlimited AI
credit promotion was addressed by defining how the credit lots and SKUs
can work for tracking. Brannen Huske\'s next step is to collaborate with
the Agentic team, RevOps, and other stakeholders to create a
simple-to-implement promo structure, consciously avoiding
over-engineering for a short-term offering.

### Strategic Challenges

A critical security and billing gap was identified with the **\"login
as\"** feature immediately following the AI credits go-live. The issue
arose when internal users, logged in as customers, inadvertently
attempted to charge customer credit lots when engaging with chat in
Workspace. While there was no customer impact this week as no AI credits
had been purchased, this poses a major risk of accidentally billing
customers in the near future.

Pushback on moving customers off **Legacy SSO** remains a persistent
challenge, as customers lack a strong friction point to motivate a move
to the newer infrastructure. Legacy SSO also has a bug where it fails to
expire certificates, creating a security and management overhead that
requires \"weird solutions\" to support. Brannen Huske is addressing
this by using the upcoming 2026 infrastructure cost as leverage for a
pricing incentive.

The team has not yet found the root cause or pattern for users being
**signed out in certain situations**. The development team is continuing
to investigate and is actively trying to gather survey results and talk
to customers to identify underlying patterns for this disruptive login
bug.

## Strategic Insights

### Key Learnings & Discoveries

The successful cutover to AI credit charging immediately highlighted the
unforeseen liability of the existing **\"login as\"** feature. This
demonstrated that seemingly minor utility features can become major
billing risks once a paid consumption model is introduced, mandating a
fast follow to deprecate the functionality.

The discovery that **Adobe** is a high-quality partner for Zscaler in
returning useful usage information via **SCIM** provides an industry
standard to aim for. Brannen Huske and the team will now analyze
competitor offerings to ensure the SCIM implementation hits industry
best practices, moving beyond the current, basic offering.

The impending cost increase for **Legacy SSO** infrastructure in 2026 is
a valuable strategic lever for driving customer behavior. The insight is
that without a financial or operational friction point, customers will
not voluntarily transition to a better login experience, such as one
supporting passkeys and biometrics. Pricing the legacy option and
offering the modern solution for free is the proposed incentive.

### Cross-Team Dependencies

Our work with the **Packaging and Pricing group** is critical for
creating the necessary pricing strategy to drive the migration off
Legacy SSO. Continued collaboration is needed to finalize the pricing
structure that will effectively incentivize customers to move from the
paid Legacy SSO to the free, modern SSO starting in 2026.

The **Agentic Team** and **Semantic Data API team** are essential for
advancing the Converstaion Intelligence tool and other roadmap items.
Specifically, the Agentic team is needed for resource allocation to
support Contact ID for the Converstaion Intelligence tool. Additionally,
the Agentic team and **RevOps** will be key partners for Brannen Huske
to define a simple, implementable structure for the unlimited AI credit
promotion.

## Looking Ahead

The primary focus for next week is to rapidly address the \"login as\"
security risk while continuing to modernize the login experience and
advance the AI credit promotion structure.

Jessie Kain Lindstrom\'s immediate priority is to kick off the plan to
**deprecate the existing \"login as\"** feature and begin implementation
of the new **admin impersonation feature**. This will eliminate the
significant risk of accidentally charging customers and is an essential
fast-follow to the AI credits launch. Brannen Huske will be **working
with the Agentic team, RevOps, and other stakeholders** to finalize a
simple plan to implement the unlimited AI credit promotion. This work is
necessary to enable a key sales motion without over-engineering a
solution for a short-term offering. The team will also focus on
**benchmarking competitors** like Adobe to ensure the SCIM
implementation achieves industry best-in-class standards, supporting the
goal of a better GTM Workspace login experience.
