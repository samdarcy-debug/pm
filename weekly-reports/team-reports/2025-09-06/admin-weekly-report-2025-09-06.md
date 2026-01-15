---
id: weekly-admin-2025-36
title: "Admin Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

### B. Huske\'s Executive Roundup - 9/1/2025

#### Executive Summary

This week, the User-Provisioning team finalized the design for the AI
Action Credit system, enabling GTM Studio to charge for AI actions. The
team also completed its goal of defining how the Workbooks and Agentic
teams would interface with the new system, marking the initiative as
complete. A key discovery was the need for a new bulk hold API due to
the way batch actions in workbooks. Moving forward, the team will focus
on an AI Action Credit roadmap to incorporate additional features like
charge caps on specific actions and user AI action credits.

#### This Week\'s Progress

##### Key Momentum Areas

A major achievement was finalizing the design of the AI Action Credit
system, which supports the GTM Studio Release. This included agreeing on
the AI Action Credit system design and implementation details for how
the Workbooks team should interface with it. By completing this, the
team has a path forward to release and charge money for AI actions.

The team also achieved alignment with the Agentic team and Workbooks
team on the bulk hold API, which was a new requirement that surfaced.
The provisioning team has committed to delivering the API so the
Workbooks team can begin integration. This work has been marked as
complete.

##### Goals & Progress

**AI Action Credit System**: The design for the AI Action Credit system
and its integration with GTM Studio Release is complete. The team has an
agreed-upon approach and a path forward for release. The next steps are
to align on what the API will look like and when it can be delivered.

**GTM Studio Release**: Progress was made on the GTM Studio Release,
which aims to charge money for AI actions. The team has achieved
consensus on the necessary steps to move toward the release. There is a
plan to release the G-Team Studio and charge money for AI actions.

**AI Action Features**: Additional features for the AI Action Credit
service have been identified, such as putting caps on specific actions
like AI Action email^19^. This work will be picked up in October or
later due to the tight timeline for GTM Studios.

##### Strategic Challenges

A new bulk hold API is needed because Workbooks teams batch actions in
groups of approximately 2,000 and the current hold API operates at a
single job which is not compatible with how the workbook processes
things. .

An additional challenge is understanding the packaging needs for Copilot
V2. The team needs to determine if user-based AI action credits need to
be packaged with the product. This will require conversations with Mark
Harris and Victor to understand how Copilot V2 will be sold.

#### Strategic Insights

##### Key Learnings & Discoveries

Based on feedback from customers and sales team we are getting
additioanl feature request for AI Action Credits. Examples like charge
caps on specific AI actions to allow increased predictability in spend,
creating user limits on AI Action Credits to better control credit
usage, and cost monitoring systems. With these additional feature. This
insight has led to the plan to build an AI action credit roadmap to show
these future features.

##### Cross-Team Dependencies

The team\'s work is critical to Workbooks and the Agentic team. A new
dependency is the need for a new bulk hold API for the Workflows and
Workbooks teams. This API is required for the Workbooks team to
integrate against the new system. Brannen Huske is in conversations with
Mark Harris and Victor to address the packaging needs for Copilot V2.

#### Looking Ahead

The primary focus for next week will be to take feedback on additional
features and build out an AI action credit roadmap. This roadmap will
detail features such as user limits and charge caps, which are needed
for Copilot V2. The goal is to get alignment with stakeholders on what
is needed and when, and then build out the resourcing for it. A meeting
is also planned with Victor and Mark to get an understanding of the
Copilot V2 sale strategy and what packaging or AI Action Credit features
are needed to support.
