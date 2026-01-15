---
id: learnings-2025-020
title: Q3 2025 Learnings Memo - Neha
type: doc
status: approved
team: gtm studio
owner: '[[teams/gtm studio/_people/neha]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm studio
related: []
---
#### **Metric Alignment**



My Q3 work has directly contributed to three key metrics that drive

business outcomes:



**GTM Studio Active Users & Engagement** - DoubleO (ZI acquired product)

integration addresses the critical \"activation gap\" for GTM studio

where users build Workbooks but cannot execute on them. By embedding

natural language automation, custom workflow builder, and GTM templates

directly into Studio, we transform the platform from intelligence only

to complete execution, creating workflow dependencies that increase

daily active usage and platform stickiness.



**Customer Retention & Expansion Revenue -** DoubleO integration solves

the #1 pain point from GTM Studio user surveys: \"We haven\'t been able

to act on anything yet because the connection isn\'t there yet\" (Prelim

Survey). Additionally, proactive resolution of [[ZI

Chat]{.underline}](https://www.zoominfo.com/products/chat) privacy

issues prevented compliance-related churn risk.



**Credits per Activated Workflow-** Plays leverage existing ZI

capabilities as native tools, multiplying workflow value and credit

utilization.



#### **Key Learnings**



**The \"activation gap\" represents our biggest retention risk.**

Customer

[[VOC]{.underline}](https://docs.google.com/document/d/1q-84R-cG_w-uCsZrRAscCL7sd2W0uUSGMcyO3ZQutFc/edit?usp=sharing)

revealed users excel at building targeted audiences but struggle with

execution: \"1,537 accounts in this workbook\...how do I find those

records in Salesforce? I have no way of isolating these\" (Nicholas

Tessier, SurveyMonkey). This manual workflow prevents value realization

and creates a churn vulnerability that DoubleO integration directly

addresses.



**Navigation changes disproportionately harm casual users, not power

users.** The navigation update across Sales,ZIM and copilot offered

valuable insights into how different user groups interact with the

platform. Post-beta analysis showed that while power users adapted

seamlessly, casual users experienced 2.7x higher exit rates, emphasizing

that there is a learning curve for any key UX changes. This highlights

an opportunity for future UX improvements: to balance familiarity for

experienced users with intuitive navigation for new ones through

segmented testing based on user maturity.



**Frontend technology choices directly influence delivery timelines.**

GTM Studio is built on Angular, whereas DoubleO uses React, adding

integration effort. For M1, the focus will primarily be on CSS design

updates and a light reskin- a decision to move quickly. Moving forward,

aligning on a clear frontend strategy will be essential to balance

speed, engineering capacity, and user experience quality for

customer-facing milestones.



**Reactive compliance fixes are 10x more expensive than proactive

audits.** For acquired products like ZI Chat(Insent),vendor data-sharing

compliance reviews at partnership evaluation level are required to be

documented and accessible. Example for chat, Pusher data sharing issue

surfaced through customer escalation threatening lawsuit, not proactive

vendor audit



#### **Hypotheses & Results**



**Hypothesis:** Integrating DoubleO\'s natural language automation

directly into GTM Studio would transform it from intelligence tool to

end-to-end execution platform, creating competitive differentiation that

competitors (like Clay) cannot replicate without our data foundation.



**Results:** We successfully moved from strategy to execution,

completing the M1 PRD that defines three activation paths- natural

language chat, custom visual builder, and one-click templates. Top GTM

workflow templates prioritize inbound routing, ABM sequences, and

competitive displacement, with ongoing work on integrations across CRM

integrations (Salesforce, HubSpot), communication tools (Slack), and

email ingestion(Chorus)



**Hypothesis**: Providing three paths to workflow creation (natural

language chat, custom visual builder, one-click templates) would

dramatically reduce time-to-value and would prepare us for M2 where the

focus is on Workbook-to-workflow activation that will enable

non-technical users to activate Workbook audiences.



**Results: Hypothesis remains unvalidated until beta** (internal ZI

users + 5 early-access partners from Enterprise segment). Completed

end-to-end design flows covering all three activation paths,\

\

\

**Go-forward Changes & Plan**



Q4 priorities:\

**1. DoubleO M1 Delivery:** Embed plays within the GTM Studio UI and

resolve any backend or app integration blockers to enable seamless

workflow execution. By the end of M1, internal users should be able to

experience DoubleO plays seamlessly



**2. Exploring & Prioritising GTM workflow usecases** - Identify,

evaluate, and prioritize high-impact GTM workflow use cases that can be

supported in plays and can deliver immediate value to users.



**Leveraging AI**



1.  [[PRD]{.underline}](https://docs.google.com/document/d/1EI7lNMcOgMgmjxMYfX7z7r6QPFvml2pXQAioTYo0Wqk/edit?usp=sharing)

    Refinement & VOC Analysis: Leveraged AI to incorporate inputs and

    enhance PRDs.



2.  DoubleO M1 Prototyping: Cline for creating the M1 concept prototype

    for Double M1



3.  Navigation Impact Analysis: analyzed 20,000 users over 91 days,

    performing statistical significance testing, user segmentation, and

    business impact synthesis. Identified the light vs. power user

    dichotomy and the "quality vs. quantity" effect explaining stable

    credit volumes despite deactivations.

