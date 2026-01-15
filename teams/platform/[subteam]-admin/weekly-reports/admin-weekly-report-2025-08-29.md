---
id: weekly-admin-2025-35
title: "Admin Weekly Report - August 29, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-08-29
updated: 2026-01-06
week_ending: 2025-08-29
reporting_period: "August 25-29, 2025"
tags: ["weekly-report", "Q32025"]
---

### Executive Summary

This week, the User-Provisioning team made significant progress on the
solution for estimating, charging, and tracking AI Action Credits. A
major win was the decision to consolidate the AI Pricebook and AI Credit
Service into a single, centralized service, which does add scope, but
simplifies the design for reporting. Meeting the October 1st deadline
with the evolving requirements is aggressive, but the additional time on
design is important to get this right. Additionally, Josh Simon
completed the initial requirements for the new Audit Service, which is a
foundational step toward improving customer trust and security and
sunsetting the current LoginAs solution.

### This Week\'s Progress

#### Key Momentum Areas

A key achievement was the decision to merge the AI Pricebook and AI
Credit Service into a single, unified service. This consolidation allows
for tracking effort at a job level, which is essential for accurate
reporting. While the churn in requirements shortens our development and
testing timeline for October 1st, there has been a lot of focus recently
on how companies have done this poorly (e.g.
[[Cursor]{.underline}](https://techcrunch.com/2025/07/07/cursor-apologizes-for-unclear-pricing-changes-that-upset-users/)),
that investing additional time on the design is necessary.

Josh Simon made progress on the Audit Service by drafting the
requirements for what fields and actions to track. Finalized the
requirements will be included in his product review document.

#### Goals & Progress

**AI Action Credit Management:** Brannen Huske and Jessie Lindstrom\'s
goal was to finalize the requirements, with a specific focus on
reporting. They both reported 90% completion, with the final 10%
dependent on a design review with the Workbook team. This review is
critical to final sign off since the Workbooks team will be the first to
use this new credit charging system.

**Audit Service:** Josh Simon completed his goal of drafting the
requirements for the new Audit Service. The service is intended to
establish customer trust and lay the groundwork for removing the
\"LoginAs\" feature.

### Strategic Challenges

A significant strategic challenge is the timeline for the AI charging
mechanism. With a hard deadline of October 1st, there is no buffer. This
makes the upcoming weeks an \"all-hands-on-deck\" effort for the team.

A second challenge is the ongoing difficulty in testing the HTTP-only
cookie solution for login bounce issues. The team has been unable to
connect with customers, even after reaching out to new contacts at
HubSpot. This has become a blocker for being able to validate the
solution, the team anticipates customers will be more available after
month end.

### Strategic Insights

#### Key Learnings & Discoveries

One key learning this week, shared by both Jessie Lindstrom and Brannen
Huske, was the value of consolidating the AI pricebook and credit
service into a single, centralized service. This change was a result of
a final review with the Agentic team and allows for tracking effort at a
more granular \"job level\". This centralized approach enables the
various reporting views needed to adjust pricing and optimize effort.

A significant insight from Josh Simon\'s LoginAs discovery is the heavy
reliance of internal teams on the feature for their day-to-day work.
Removing it will require retraining these teams to use other tools. A
potential solution discussed with Ali Sadat is to create a \"customer
login sharing capability\" similar to what Salesforce offers, which
would allow admins and users to share access with each other and with
ZoomInfo support. This would also serve as an interim testing ground for
a future solution that could replace LoginAs for some departments.

#### Cross-Team Dependencies

The User-Provisioning team is highly dependent on the Workbook and
Agentic teams to finalize the AI Action Credit management design and
ensure the system can correctly charge for AI actions. A final review
with the Workbooks team is scheduled for Tuesday to get this locked
down. The team is also waiting to connect with customers to validate the
**HTTP-only cookie** solution for login issues, which has been difficult
due to end-of-month sales pushes.

### Looking Ahead

The primary focus for next week will be the final sign off of the AI
Action Credit management design. Brannen Huske will represent the
provisioning team during the final review with the Agentic and Workbook
teams to ensure all use cases for the new centralized charging service
are accounted for and a clear implementation path is established. The
team will also continue efforts to connect with customers to validate
the cookie solution, with Tony and Sagar taking the lead on this while
Josh Simon is out. This work is critical to delivering on key
initiatives for security, monetization, and customer experience.
