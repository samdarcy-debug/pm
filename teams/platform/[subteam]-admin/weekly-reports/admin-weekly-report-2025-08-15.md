---
id: weekly-admin-2025-33
title: "Admin Weekly Report - August 15, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-08-15
updated: 2026-01-06
week_ending: 2025-08-15
reporting_period: "August 11-15, 2025"
tags: ["weekly-report", "Q32025"]
---

### Executive Summary

This week, the team secured a significant win with the London Stock
Exchange Group (LSEG) and made key progress on AI credit mechanics and
user entitlements. We\'ve successfully onboarded LSEG to the data
privacy controls (DAC) and hope this will lead to a contract win over
LinkedIn Sales Navigator. On the AI side, the team has gained consensus
on the mechanics of non-usage-based AI credits and usage-based customer
bulk AI action credits. We also advanced the user entitlement tickets
for the Agentic platform, with Jessie Lindstrom handing off the
requirements document to Lars for review.

### This Week\'s Progress

#### Key Momentum Areas

The London Stock Exchange Group was successfully onboarded to the data
privacy controls. Josh Simon believes this could lead to a contract win
over LinkedIn Sales Navigator and serve as a key logo for privacy, as it
would prove that the company's privacy controls are adequate for one of
the most regulated customers.

Brannen Huske focused on finalizing the requirements for AI action
credits, specifically locking down the mechanics for drawing down
credits. The team reached a consensus on the difference between
recurring non-usage-based and non-recurring usage-based credits, which
will affect revenue reporting.

Jessie Lindstrom\'s high-leverage goal was to get user entitlement
tickets for the Agentic platform reviewed with engineering. She wrote a
requirements document and handed it off to Lars for review, marking the
task as 75% complete.

### Goals & Progress

**AI Credits**: Brannen Huske\'s goal this week was to lock down the
requirements for AI credits. The team achieved consensus on recurring
versus non-recurring credits and how they will impact revenue reporting.
The value of recurring, non-usage-based AI credits will be summed up
with the ACV in the initial contract, while usage-based bulk AI action
credits will be sent to the RevRec team for recognition with SAP at a
regular interval.

**Data Privacy & Login**: Josh Simon aimed to onboard LSEG and Microsoft
to data privacy controls. LSEG was successfully onboarded and
demonstrated great interest, but Microsoft had layoffs, which delayed
their implementation. Additionally, Josh is investigating why users from
Palo Alto Networks and Snowflake are being logged out of their sessions
overnight. The leading theory is that session cookies should be stored
as HTTP only.

**Agentic Platform User Entitlements**: Jessie Lindstrom\'s goal was to
get user entitlement tickets for the Agentic platform reviewed by
engineering. She wrote a requirements document and shared a one-pager
with Lars, who is now reviewing the tickets. Jessie will work with him
to ensure the tickets are reviewed and to determine who on the team
needs to consult with the Agentic team.

### Strategic Challenges

Microsoft\'s recent layoffs have caused a delay in implementing the data
passport control, despite the team proving they could support the use
case. This situation will be monitored, and the team will continue
working with their internal account team^22^.

A persistent challenge involves users being bounced out of their
sessions overnight. The team is investigating this issue with users from
Palo Alto Networks and Snowflake. The current leading theory is that
session cookies should be better stored as HTTP only, but converting
them would be a significant amount of work for all downstream teams.

The implementation of the AI Price Book is a complex issue. Jessie Kain
Lindstrom noted that no one has figured out how to price for platforms
dependent on external large language models (LMs) and external costs.
There are \"a million different ways\" to implement this, and the team
needs to align on a path forward.

### Strategic Insights

**AI Pricing**: The AI Price Book is an interesting and challenging
space because there is no established method for pricing platforms that
rely on external large language models and associated costs^29^. Jessie
Kain Lindstrom has put together a requirements document for review by
engineering to set the stage for future discussions. The team will need
to align on an implementation plan and identify the team to build it.

**Data Privacy**: The successful onboarding of LSEG validates the team's
privacy controls and positions ZoomInfo as a market leader in privacy.
This success provides a strong narrative for winning over other highly
regulated customers.

**Session Cookies**: After meeting with users from Palo Alto Networks
and Snowflake, the team\'s leading theory is that converting session
cookies to HTTP only could solve the issue of users being logged out
overnight. This potential solution is considered the closest they\'ve
come to finalizing a solution.

### Cross-Team Dependencies

Work with the engineering team is critical for getting the user
entitlement tickets for the Agentic platform reviewed and fleshed out.
Jessie Lindstrom will be working with Lars to ensure the tickets are
reviewed and to figure out which team members need to consult with the
Agentic team.

The RevRec team will be responsible for recognizing revenue from the
usage-based bulk AI action credits, which will be sent to them at a
regular interval via Boomi. This is a new process that is essential for
driving usage-based revenue.

### Looking Ahead

Next week, the team will continue to focus on a number of key
initiatives. Josh Simon plans to pivot back to his \"logging in as\"
workstream. He intends to send out a survey to product and engineering
to understand their reasons for logging in as other users, and then set
up a product review..

Jessie Lindstrom's next steps for the Agentic platform involve working
with Lars to ensure the user entitlement tickets are reviewed and
identifying which team members need to help with the consultation. For
the AI Price Book, the team will have another meeting to align on an
implementation plan and figure out who will build it.

Brannen Huske\'s goal for next week is to pivot to verticalized data
sets. He has a few meetings scheduled to determine how to package,
price, and load this data into GTM Studio.
