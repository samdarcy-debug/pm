---
id: weekly-admin-2025-31
title: "Admin Weekly Report - August 01, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-08-01
updated: 2026-01-06
week_ending: 2025-08-01
reporting_period: "July 28-August 01, 2025"
tags: ["weekly-report", "Q32025"]
---

#### Executive Summary

This week, a significant pivot was made by Jessie Lindstrom\'s team to
assist with the AI Credit consumption work, which is critical for
launching Copilot v.2 and GTM Studio. The team is making progress on
getting tickets ready for the AI credit work, but key decisions still
need to be made regarding the AI Action Price book and revenue
reporting. An open quest remains on how we intend to package and enable
customers on Copilot v.2, which needs to be resolved before the feature
can be released to customers.

#### This Week\'s Progress

#### Key Momentum Areas

- Jessie Lindstrom\'s team has shifted focus to support Brannen Huske\'s
  AI credit consumption work. This is a strategic pivot as the original
  goal to scope requirements for user entitlements on the agentic
  platform is no longer needed for the August 5th deadline, but is still
  required for Beta.

- The login team, led by Josh Simon, successfully launched a new banner
  for the \"login as\" feature, which is a win for compliance. This
  banner, which appears as a red warning, notifies users when they are
  impersonating a customer, which helps prevent mistakes. Additionally,
  email was shut off as a two-factor authentication (2FA) method for new
  users, which is another significant security improvement.

- Progress has been made on the AI credit architecture and revenue
  reporting. Brannen\'s team has clarified the process for creating
  SKUs, loading AI credits into wallets, and managing charges and holds.
  A kickoff meeting has also taken place with the Revenue Recognition
  and Go-to-Market Studio teams to discuss how to report revenue to SAP
  as it is used.

#### Goals & Progress

- **AI Credit Architecture and Revenue Reporting**: The goal is to
  complete the AI Credit architecture and determine how to report
  usage-based revenue to SAP. Brannen Huske\'s team is 70% done with
  this goal, as they have conducted two rounds of technical requirement
  reviews and have defined how to manage credits and holds. There are
  still some open items, such as deciding where the AI Action Price book
  will live and working with the CFA team on reporting AI usage to
  customers.

- **Login & Privacy Initiatives**: Josh Simon finalized second-half
  goals for the login and privacy teams, and has gotten sign-off from
  engineering. The team is starting work on login milestones and has
  completed a prototype for Data Password Control v.3, which uses a
  manager hierarchy for assigning roles. Josh is meeting with the design
  team next week to kick off the design work.

- **User Entitlements for Agentic Platform**: Jessie Lindstrom\'s
  original goal was to scope and estimate the requirements for agents to
  respect user entitlements. Development was the completion criteria.
  Due to a shift in priorities, this work is being pushed back, but
  Jessie plans to dedicate time next week to scope out the requirements.

#### Strategic Challenges

- A major challenge is the lack of a defined solution for the agentic
  platform to respect user entitlements. This is a critical security
  concern, as copilot v.2 and the new platform cannot be released to
  customers if agents can perform actions a user is not entitled to. The
  team needs help from the agent platform team to determine the
  necessary work.

- The packaging and selling strategy for Copilot v.2 remains a blind
  spot. It\'s unclear if it will be a free upgrade or have new
  entitlements. A meeting is scheduled with Sean and Carlos to review
  the New Product Introduction (NPI) document and make a decision, which
  will inform the next steps for development. The outcome of this
  meeting will impact revenue targets and requires a decision from the
  packaging team.

- The team is still investigating a persistent issue where some
  Snowflake users are being logged out or \"bounced out\" of the
  platform daily or weekly. The team has met with three users this week
  and has more meetings scheduled to understand the problem. This
  unknown issue is a key focus for the team.

#### Strategic Insights

- The login team has identified an ongoing problem with marketing and
  talent teams not respecting privacy controls. A customer issue arose
  where Do Not Call (DNC) was not being respected in the talent feature.
  Dan Skellen, the product manager for talent, already has a ticket for
  this issue. This highlights the need for dedicated time to be put
  aside to go through features on a case-by-case basis to ensure privacy
  controls are being respected across all teams.

- It was discovered that a decision needs to be made on where the AI
  Action Price book will reside. The agentic group originally discussed
  it being on their side, but they are now making the case that it could
  also live on the AI credit team\'s side. This is an important decision
  to be made to finalize the architecture and move forward with the
  work.

- A key learning for Jessie Lindstrom was the need for flexibility and
  the ability to pivot, especially during times of stress. The original
  goal of scoping user entitlements was deprioritized because it wasn\'t
  needed for a fast-approaching deadline, allowing the team to shift
  focus to the AI credit work.

#### Cross-Team Dependencies

- Our work with the **Revenue Reporting Team**, owned by Garrett, is
  critical for completing the AI Credit architecture. We need to work
  with his team to determine how to report revenue as usage-based, which
  will influence the final architecture. A kickoff call with relevant
  business units has already occurred.

- Coordination with the **Agent Platform Team** is essential for
  determining the solution for agents to respect user entitlements. The
  level of effort and the solution for this are currently unknown, which
  is a major blind spot.

#### Looking Ahead

The primary focus for next week will be to make key decisions to unblock
the AI credit consumption work and the Copilot v.2 and GTM Studio
launch.

Our top priorities include:

- **Finalizing AI Credit Architecture Decisions:** We have a meetings
  next week with contracts team, Rev Req team ,and Agentic team to
  finalize decision on Usaged Base Pricing. These decisions will allow
  us to complete the AI Credit architecture and get the tickets to 100%
  shovel-ready.

- **Defining Copilot v.2 Enablement:** Brannen will meet with Sean and
  Carlos on Monday to review the NPI document to get a decision on the
  packaging and entitlements for Copilot v.2. This is a critical step,
  as it will determine the necessary development work.

- **Addressing AI Usage Reporting:** Jessie will be taking on the
  conversation with the CFA team on Monday to discuss how to report AI
  usage to customers. This is one of the final pieces of the AI credit
  work that needs to be addressed before a general availability (GA)
  launch.

These meetings and conversations are crucial for maintaining momentum
and getting the necessary alignment to move forward with both the AI
credit work and the GTM Studio launch. We are confident that by tackling
these open items, the team will be able to deliver on its commitments.
