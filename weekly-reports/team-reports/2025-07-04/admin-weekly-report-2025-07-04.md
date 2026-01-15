---
id: weekly-admin-2025-27
title: "Admin Weekly Report - July 04, 2025"
type: weekly-report
status: approved
team: admin
owner:
created: 2025-07-04
updated: 2026-01-06
week_ending: 2025-07-04
reporting_period: "June 30-July 04, 2025"
tags: ["weekly-report", "Q32025"]
---

## Executive Summary

This week, the User-Provisioning team made significant strides in
defining the approach for Usage-Based Pricing and advanced crucial
privacy features. A critical decision regarding the currency and pricing
of AI features, with divergent opinions among leadership, needs final
alignment by July 11th to avoid further delays. Additionally, the team
successfully tested enhanced Data Privacy Controls, ensuring readiness
for release and expanding support for customers.

## This Week\'s Progress

### Key Momentum Areas

Jessie Lindstrom successfully achieved stakeholder sign-off from Product
Operations and GTM Strategy teams on product package reporting
requirements, including stack-ranked priorities. This is a critical step
towards resolving data inconsistencies and improving accurate tracking
of Copilot packages. Josh Simon successfully tested the Data Privacy
Controls (DAAC) rules expansion from 10 to 20 rules in staging, which is
now ready for release. This expansion will enhance support for customer
adoption of DAAC and remove ongoing blockers. Brannen Huske continued to
drive alignment on Usage-Based Pricing for GTM Studio, a crucial step
for the October release.

### Goals & Progress

**Usage-Based Monetization**: Brannen Huske is in progress with
requirements for Usage-Based Monetization, having completed the
Usage-Based Pricing PRD. This effort is crucial for enabling GTM Studio
Monetization. While significant progress has been made, the team is
still working to finalize alignment on the specific currency and pricing
model for AI features, with a target decision date of July 11th. The
customer survey results on pricing options are also pending to help
inform this decision.

**Product Package Reporting**: Jessie Lindstrom has finalized and
prioritized product package reporting requirements with key
stakeholders, including Product Ops and GTM Strategy, addressing issues
such as conflicting Copilot package identification, inconsistent seat
data, and reporting performance. These requirements have been handed off
to the Data and Provisioning engineering teams for scoping.

**Privacy Features & Login Methods**: Josh Simon completed staging
testing for DAAC rules expansion (10 -\> 20 rules). Efforts are ongoing
to determine whether to support LinkedIn OpenID Connect and Salesforce
SAML as social login methods, aiming to enhance user experience and
reduce support cases by transitioning customers away from
credential-based logins.

### Strategic Challenges

A significant challenge remains the divergent opinions from leadership
regarding the currency and pricing of AI features. Brannen Huske has
identified this as a critical blocker, with differing views on whether
to offer value-based pricing versus cost-plus-margin. A critical meeting
on July 1st with Mark Harris and Adam Smith is set to align on this
strategy, which is essential for the October release. Another critical
issue is the P&P team\'s stance on charging margin on Bring-Your-Own-Key
(BYOK) customers, which contradicts the desired approach. Brannen is
working with Ali to ensure commitment to the previously made decision.

Jessie Lindstrom is facing a medium-impact blocker due to reliance on
manual, downstream fixes for data inconsistencies rather than proactive,
upstream sales process improvements^18^. This stems from a systemic lack
of integrated upstream data governance, unclear ownership for source
data integrity, and historical prioritization of sales process
flexibility over preventing downstream data inconsistencies. This
complex issue requires compromise across all stakeholders for
sustainable change.

Josh Simon\'s team faces ongoing challenges with customer communications
for login SSO adoption and 2FA removal^21^. While seeking to reduce poor
login sentiment and increase SSO adoption, identifying the right
customer communications team amidst recent restructures is a current
hurdle. Additionally, re-visiting support for LinkedIn and Salesforce
SAML as login methods is proving complex due to past security concerns,
where a Salesforce SAML implementation led to unfettered access due to a
large security gap with Okta support of Salesforce.

## Strategic Insights

### Key Learnings & Discoveries

A key learning from Jessie Lindstrom\'s work is that while getting
everyone in a room to solve a problem can feel efficient, taking upfront
time with a smaller group to get clear, prioritized requirements keeps
downstream teams focused on solving the problem effectively. This
approach was successful in getting sign-off on product package reporting
requirements.

Brannen Huske\'s team discovered that utilizing current bulk credits for
usage-based pricing is not a viable option. While there\'s broad
agreement on the overall approach for usage-based pricing, a final
alignment is needed on whether the currency should be preloaded USD or a
new AI credit.

Josh Simon\'s team learned that SCIM setup can be more chaotic than
anticipated on the Okta side, highlighting the need to identify how to
provide the best experience for SCIM users to boost adoption. They also
observed that leveraging Workflows for Opt-out page integrations with
CRM could be highly beneficial. Furthermore, their experience with
Salesforce SAML revealed a critical security gap that led to its
rollback, emphasizing the need for thorough security evaluations before
implementing new login methods^30^.

### Cross-Team Dependencies

Brannen Huske\'s progress on Usage-Based Pricing for GTM Studio is
critically dependent on alignment from Packaging & Pricing, Product,
PMM, and Leadership on the pricing model. The conflicting opinions from
Mark Harris and Adam Smith require resolution.

Jessie Lindstrom\'s work on product package reporting relies on capacity
for review from Product Operations, GTM Strategy, Data Engineering, and
the Provisioning team. The qualitative understanding of customer
behavior around credit management also requires access to credit
utilization data across tenants^34^.

Josh Simon\'s efforts to expand the usefulness of privacy features
(DAAC, CCIS) are dependent on integration with MOS, CRMs, and Workflows.
Discussions with Marc Frail regarding workflows and reaching out to the
ZIM team are necessary to address core questions about privacy feature
compatibility^36^.

## Looking Ahead

The primary focus for Brannen\'s team next week will be to drive final
alignment on the Usage-Based Pricing model for AI features by the July
11th deadline, incorporating customer survey results to inform the
decision. This is crucial to unblock the GTM Studio monetization
strategy.

Jessie Lindstrom will be reviewing the prioritized product package
reporting requirements with engineering and documenting the technical
needs and owners for each workstream^3838^. This will translate the
stakeholder alignment into actionable engineering tasks to improve
reporting accuracy and consistency^39393939^.

Josh Simon\'s team will prioritize H2 planning and provide feedback on
the RealNPS report v2. This includes re-validating calls based on the
new labeling to ensure accurate identification of login
issues^40404040^. Additionally, syncing with the communications teams
for SSO adoption and conversion will be a key focus to improve the
customer experience and reduce support cases^41^. The team also plans to
continue investigating the feasibility and security implications of
supporting LinkedIn OpenID Connect and Salesforce SAML as login methods.

The team is confident that by focusing on these key priorities and
actively resolving the identified blockers, they will continue to
deliver significant value and enable strategic initiatives like GTM
Studio monetization and enhanced privacy capabilities.
