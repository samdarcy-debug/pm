---
id: weekly-admin-2025-28
title: "Admin Weekly Report - July 11, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-07-11
updated: 2026-01-06
week_ending: 2025-07-11
reporting_period: "July 7-11, 2025"
tags: ["weekly-report", "Q32025"]
---

## Executive Summary

This week, **Jessie Lindstrom** spearheaded significant progress in
establishing clear reporting needs for pricing, packaging, and seating,
culminating in a validated requirements document and a review with
engineering. This critical work, which has identified five key reporting
gaps and secured timing commitments for the top two, is essential for
accurate usage-based pricing and revenue operations, directly supporting
key business decisions. **Josh Simon** has made strides in finalizing
the new pricing flow designs, securing new designs based on stakeholder
feedback, and preparing for Jira ticket creation, which is vital for
maintaining MQL integrity and correct account manager assignment.
**Brannen Huske** achieved 70% completion on finalizing the base pricing
decision, moving forward with building the system around the AI action
price book and getting packaging and pricing for the platform section
into the POC. A key decision needed is continued executive support in
prioritizing these initiatives, especially given cross-functional
dependencies and the need to address data categorization blind spots.

## This Week\'s Progress

### Key Momentum Areas

**Jessie Lindstrom** successfully drafted a comprehensive requirements
document for pricing, packaging, and seating reporting, validating it
with business stakeholders. This is a crucial step in enabling accurate
reporting on usage-based pricing models and ensuring that our revenue
operations are supported by reliable data, directly impacting our
ability to make informed business decisions.

**Josh Simon** led productive meetings with RevOps and SDR stakeholders,
resulting in new designs for the pricing base flow. This progress is
vital for ensuring that the flow correctly assigns account managers and
CSMs, guaranteeing that the right content reaches the right people at
the right time, thus preserving MQL integrity.

**Brannen Huske** advanced the base pricing decision to 70% completion,
progressing on building the system around the AI action price book and
integrating packaging and pricing for the platform section into the POC.
This work is fundamental for the strategic implementation of new pricing
models.

### Goals & Progress

**Brannen Huske**: The goal to finalize the base pricing decision is 70%
complete. While a final decision on currency is pending Adam Smith\'s
return (out until the 16th) and Mark\'s finalization, the team is
proceeding with building the rest of the system around the AI action
price book. Packaging and pricing for the platform section and POC are
being submitted to Melissa today.

**Pricing & Reporting Initiatives**: **Jessie Lindstrom** has advanced
significantly on defining reporting needs for pricing, packaging, and
seats. A requirements document was created and validated with business
stakeholders, identifying five key reporting gaps. A review with
engineering was conducted this week to get estimates for all five and
timing commitments for the top two, putting us on track for accurate
usage-based pricing data.

**New Pricing Flow Design**: **Josh Simon** is nearing finalization of
the designs for the new pricing base flow. Meetings with RevOps and SDR
stakeholder groups provided critical feedback, leading to updated
designs. The next step is to generate Jira tickets, moving this
initiative closer to implementation and ensuring proper MQL handling and
account manager assignments.

### Strategic Challenges

A primary challenge identified by **Jessie Lindstrom** is the **\"blind
spot\" around legal proof of delivery or SKU implications of usage-based
pricing options**. This directly impacts how the usage-based
monetization is built to avoid business issues and requires close
collaboration with the PII committee to understand pricing implications.
Furthermore, there\'s uncertainty about what needs to change upstream in
Salesforce and teams\' capacity to handle technical requirements, making
the engineering review crucial for feedback.

**Josh Simon** highlighted a \"blind spot\" concerning **how things are
categorized in Salesforce and how different forms lead to different
places**. This lack of complete understanding in data categorization
poses a risk to accurate reporting and efficient workflows, as it can
lead to miscategorized login issues or incorrect data routing if not
addressed. Additionally, **Josh Simon** experienced a significant time
stretch due to competing priorities, including planning for H2 login and
privacy goals and spending 5-15 hours reviewing calls for the real NPS
report, which did not move other goals forward.

## Strategic Insights

### Key Learnings & Discoveries

**Jessie Lindstrom**\'s work on reporting highlighted the critical need
for accurate package and usage reporting, especially for usage-based
pricing. The discovery of five specific reporting gaps, with a focus on
gaining engineering estimates and timing commitments for the top two,
emphasizes that data infrastructure is paramount for strategic pricing
decisions. A key learning from the engineering review is the \"blocker\"
of ownership regarding business logic and data transformation for
definitive packaging.

**Josh Simon**\'s efforts to finalize new pricing flow designs revealed
the deep investment of RevOps and SDR stakeholders in maintaining MQL
integrity and ensuring correct account manager/CSM assignment. This
reinforced the importance of user flow accuracy and careful
categorization within Salesforce to avoid lost MQLs and ensure timely
content delivery. **Josh Simon** also learned about significant
miscommunication and lack of coordination for customer communications
amongst marketing teams, particularly regarding SSO adoption and 2FA
pushes, indicating a lack of a single process for these non-code
releases. This leads to him having to individually follow up with
parties, which is time-consuming and leads to dropped balls. He also
realized that when making UI changes on the login page, marketing and
leads stakeholders need to be involved earlier to avoid back and forth
at the end of the process.

**Brannen Huske** learned that revenue reporting depends on whether a
customer budget expires at the end of a subscription or rolls over, a
question Mark is currently addressing with the ELT group. Additionally,
Commerce Services is building a revenue reporting service through
Stripe, and there is a need to align on whether to use Stripe or report
directly to SAP, with pros and cons to both, likely depending on the
budget expiration decision.

### Cross-Team Dependencies

Our work with the **engineering team** on reporting needs, specifically
for pricing, packaging, and seats, continues to be critical for enabling
accurate usage-based pricing and revenue operations. **Jessie
Lindstrom**\'s upcoming review with engineering for estimates and timing
commitments on the five identified reporting gaps is essential.
Resolving the ownership of business logic and data transformation for
definitive packaging is a critical dependency, with Jessie pushing for
the data team to own this transformation.

Collaboration with the **PII committee** is crucial for understanding
the legal proof of delivery or SKU implications of usage-based pricing
to avoid business issues. **Brannen Huske** needs to meet with **Andrew
Levy**, who owns Stripe, and **Garrett Cummins**, who owns the SAP
connection, to align on revenue reporting methods. **Josh Simon**
highlighted dependencies on marketing and leads teams for UI changes on
the login page, emphasizing the need for earlier stakeholder involvement
to avoid late-stage back and forth.

## Looking Ahead

Next week, the team will primarily focus on translating finalized
designs into actionable development tickets, securing critical
engineering commitments, and addressing key alignment issues for pricing
and reporting.

**Brannen Huske** aims to secure alignment on the AI budget early next
week, with Mark expected to have an answer today. He will also meet with
Andrew Levy and Garrett Cummins to align on revenue reporting, and work
with Brenna and Lauren McHugh on NPI and tickets to advance packaging.

**Jessie Lindstrom** will focus on getting alignment and ownership for
the data transformation of product and add-on data to actual packages.
She created a diagram to articulate her POV of the source of truth for
the 5 reporting gaps, which will be reviewed today within the platform
team. The goal is to ensure each system acts as a source of truth
feeding into the BI tool, rather than solely relying on the platform for
all transformations.

**Josh Simon** will concentrate on finalizing Jira tickets and designs
for the pricing page flow, with the goal of getting it into the next
sprint. This will enable the team to start development work and address
the categorization blind spot in Salesforce.

The team remains confident in delivering significant value, but
continued executive awareness and support for cross-functional
dependencies, especially with engineering, legal, and marketing teams,
will be crucial in accelerating progress.
