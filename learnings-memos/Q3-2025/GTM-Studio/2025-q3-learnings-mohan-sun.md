---
id: learnings-2025-019
title: Q3 2025 Learnings Memo - Mohan Sun
type: doc
status: approved
team: gtm studio
owner: '[[teams/gtm studio/_people/mohan-sun]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm studio
related: []
---
#### **Metric Alignment**



My Q3 work has directly contributed to two key metrics that drive

ZoomInfo\'s business outcomes:



- **Credits per Record under Management (North Star)** - By enabling

  seamless activation paths from GTM Studio to Copilot Workspace, we

  will create a direct incentive for customers to build and manage more

  target lists within the ZI ecosystem. Each activated list contributes

  to credit consumption as customers engage with more records. The

  workbook-to-workspace integration removes activation barriers, which

  should increase record utilization and management, driving the median

  number of credits per tenant.



- **Automated AI inference per record under management (Driver)** - The

  GTM play/workflow capabilities for sales and marketing motions will

  increase the value of AI-powered content generation. By streamlining

  the process from list building to personalized outreach, we will

  create natural opportunities for customers to leverage automated AI

  enrichments across their managed records. This directly impacts the

  number of automated AI inferences per record, which is a primary

  driver for credit consumption.



#### **Key Learnings**



Q3 work on GTM Studio activation revealed insights that drive both user

adoption and credit consumption:



1.  **Copilot technical design requires unique integration flow** -

    Copilot workspace was not designed to support database read/write

    capabilities, requiring us to create a new querying pathway for

    shared workbook views rather than using workflows to pass data

    directly. This architectural design requires this unique activation

    pathway until Copilot moves to a database approach.



2.  **Route ownership is critical for adoption** - Early access

    customers consistently prioritize CRM-based ownership routing, with

    80% citing this as essential for aligning with their operations.

    Without straightforward rep assignment capabilities, activation

    suffers regardless of other features.



3.  **Orchestration capabilities drive engagement tool selection** -

    Analysis shows Outreach has \~24% usage among early access

    customers. Sales engagement orchestration capabilities should be

    considered \"must-have\" requirements from the beginning.



4.  **Frontend technology decisions impact delivery timelines** - GTM

    Studio uses Angular while DoubleO uses React, creating additional

    integration scope. Future customer-facing milestones require clear

    frontend strategy alignment to balance speed, engineering capacity

    and UX quality.



#### **Hypotheses & Results**



1.  **Direct GTM Studio to Copilot activation will streamline seller

    workflows.** *Results:* We are working toward an October delivery

    date to enable this activation. Early feedback (SurveyMonkey, Brex,

    ZI Labs) showed strong interest but concerns about email cadence

    sharing and rep assignment capabilities.



2.  **Territory-based routing will satisfy customer requirements.**

    *Results:* CRM-based ownership routing proved essential for

    enterprise adoption. Current round robin options don\'t meet

    expectations, as customers need to modify assignments to align with

    existing operations. This required integration between Route Service

    and GTM Data Store.



3.  **Unified interface will create seamless experience across

    products.** *Results:* Angular (GTM Studio) vs. React (DoubleO)

    created technical challenges. This revealed the need for a cohesive

    frontend strategy balancing speed, engineering capacity, and UX

    quality across customer-facing components for new features.



4.  **Export capabilities can extend using existing system workflows.**

    *Results:* Usage data showed Outreach and Salesloft as top

    activation platforms, but existing export workflows couldn\'t

    support \"add to sequence\" OOTB. Every new integration platform

    requires a bespoke system workflow to be created. Orchestration

    features need a more scalable approach.



#### **Go-forward Changes & Plan**



1.  **Route Experience Enhancement.** We\'ll complete the integration

    between Route Service and GTM Data Store to retrieve ZI user

    information. But we will need to prioritize the ability for RevOps

    to modify routing to address the clear customer need for rep

    assignment flexibility.



2.  **Frontend Technology Strategy.** Align on a cohesive frontend

    approach for GTM Studio and DoubleO integration for H2 milestones &

    beyond that balances immediate delivery needs with long-term

    maintainability. We need to evaluate options for bridging Angular

    and React components while ensuring consistent UX. This technology

    decision can serve as a reference for future cross-app experiences.



3.  **Orchestration Capabilities Expansion.** Enhance the existing

    workbook export capabilities to fully support \"add to sequence"

    functionality for Outreach (24% usage) and Salesloft. We need to

    build this using a scalable solution (i.e., DoubleO plays) rather

    than an add-on feature.



4.  **Measurement Focus.** Implement tracking to measure the impact of

    activation on both credit consumption and AI inference usage. We

    should establish baseline metrics for target list creation and

    activation rates, then monitor how our integrated workflow

    experiences drive increases in both metrics.



> **Leveraging AI**



**Most Impactful AI Use Cases**



1.  **PRD Development** - Generated comprehensive product

    [[requirements]{.underline}](https://docs.google.com/document/d/1gccHD3o_baUAs4_02DDc2bOqSC-7VY6EO2N1fhfyCqM/edit?tab=t.b3e2eemzm0so#heading=h.3bwbu8fouw0k)

    and user flows for GTM Studio activation, accelerating design and

    engineering reviews. This was particularly valuable for complex

    cross-product integration requirements between CoPilot, Route, and

    GTM Studio.



2.  **GTM Workflow Research** - Analyzed workflow creation best

    practices and most frequently implemented play templates to

    understand what customers typically build. This will help inform the

    DoubleO play activation paths and help prioritize the workflows most

    valued by customers.



3.  **Competitor Analysis** - Used ZI Chat (Crayon) to generate detailed

    competitor

    [[reports]{.underline}](https://zoominfo-chatbot-ui.zi-ext.com/content/41e240b2-3747-47cc-852a-9c2530cbcfc2).

    This produced comprehensive PDFs that informed our feature

    prioritization.



4.  **Test Case Prioritization** - Leveraged Claude to build testing

    [[plans]{.underline}](https://docs.google.com/spreadsheets/d/1R-3pb1tdZiyWg1CDPy05xX9o0BdT_vxu-wBpzcYjCdE/edit?gid=805675434#gid=805675434)

    that facilitated QA prioritization, ensuring high-quality feature

    releases despite complex dependencies and timeline restrictions.



**AI Expansion Plans for Q4**



- **Launch Readiness Testing (LRT)** - Implement GTM enablement for

  upcoming feature releases, particularly CoPilot activation and DoubleO

  plays. This will streamline launch documentation and training

  materials creation.



- **Customer Insight Synthesis** - After feature release, use ZI

  Chat/Slack tools to analyze and synthesize customer feedback, feature

  requests, and reported issues. This will create a more data-driven

  approach to feature iteration and help identify patterns in user

  adoption challenges.

