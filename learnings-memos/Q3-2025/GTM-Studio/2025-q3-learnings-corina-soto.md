---
id: learnings-2025-016
title: Q3 2025 Learnings Memo - Corina Soto
type: doc
status: approved
team: gtm studio
owner: '[[teams/gtm studio/_people/corina-soto]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm studio
related: []
---
#### **Metric Alignment**



My work this quarter directly contributed to **Credits per Record Under

Management (RUM)**, GTM Studio\'s north star metric for driving data

consumption through credits.



The Data Health Scan initiative creates qualified upsell opportunities

by revealing data quality issues that drive RingLead adoption, directly

increasing records under management and the credit consumption required

to maintain them. The Job Posting enrichment feature demonstrates GTM

Studio\'s value as a data intelligence partner rather than a raw data

dump, driving workbook usage and credit consumption through enriched,

actionable data. Both initiatives ladder up to our north star.

Specifically, the Data Health Scan targets a TAM of 12,000+ whitespace

customers who could become data management users, each consuming credits

for deduplication, normalization, enrichment, and ongoing data quality

maintenance.



#### **Key Learnings**



This quarter reinforced that data cleanliness is critical to our

competitive positioning. The Job Posting enrichment project demonstrated

this: raw third-party data creates fragmented results with \"KS\" vs

\"Kansas\" variations and Ireland as a \"state,\" requiring expensive

manual cleanup. ZoomInfo\'s intelligent normalization ensures customers

filter by \"Kansas\" and get ALL companies hiring there---we give better

decisions, not just more data. However, delivering this requires complex

orchestration across 6 engineering teams, with each handoff introducing

failure points. Our solution: dedicated end-to-end PM ownership for

partner data workflows---one PM obsessing over the entire data journey

from ingestion through normalization to UI implementation, ensuring

details like \"VP-level\" (matching all ZI surfaces) not \"Vp-Level.\"

While established for Job Postings, this approach needs replication

across other data areas.



**Hypotheses & Results**



#### Hypothesis 1: CRM Data Health Scan Drives Upsell Conversations



**What we tested:** Can analyzing existing CRM data health and providing

specific improvement recommendations create qualified RingLead data

management upsell opportunities?



**Results:** We delivered over 1,200 Data Health Scans to AMs out of

3,900 Enterprise, Strategic, and Mid-Market customers to enable outbound

cross-sell motion. **This hypothesis still needs validation**---while

we\'ve completed initial AM calls and early feedback is promising (TK

Newman noted \"the data health scan for Palo Alto Networks would really

help me sell Enrich Premium Plus\"), we haven\'t yet proven whether this

actually converts to closed upsell deals since the Data Health Scan

reports just went out the week of Oct 1st. The goal is to enable

outbound upsell conversations using data health insights immediately,

while building this capability into GTM Studio for self-service access

longer-term. We\'ll need to track conversion metrics through Q4 to

validate whether data health visibility truly drives pipeline and

revenue.



**Key learning:** Customers don\'t know they need data management until

you show them their specific problems. Personalized health insights

create urgency and give AMs concrete talking points for previously

difficult upsell conversations.



#### Hypothesis 2: Implementation Complexity Limits Data Management Growth



**What we tested:** Can we scale data management adoption by using AI to

address the implementation bottleneck that currently requires 3-6 month

timelines with dedicated technical delivery managers?



**Approach:** Designed a crawl-walk-run roadmap transforming RingLead\'s

complex legacy experience into GTM Studio\'s guided, AI-assisted

implementation model. We started with essential revenue retention

enhancements (credit utilization alerts, Enrich Premium+ expansion),

progressed to self-service data foundation management (dedupe,

normalize, segment), and are working toward AI-assisted onboarding

targeting 2-week implementation timelines.



**Results:** Validated that our technical delivery team---while not

exclusively dedicated to RingLead---operates at capacity supporting

multiple products and cannot scale to capture the potential 12,000+

customer whitespace for RingLead. **The general takeaway**: we need

significant CX/CS resourcing to support RingLead implementation and

maintenance. Current customers show strong dependency (106% Retention in

August, up 26pts YoY) once implemented, confirming value isn\'t the

barrier---complexity is. The roadmap now provides a clear path from for

AI-driven self-service implementation, eliminating the technical

delivery bottleneck that prevents the potential customer whitespace

capture.



**Key learning:** We have proven product-market fit (\$125M+ ACV, 20%

YoY growth, minimal churn) trapped behind implementation friction.

We\'re leaning into an AI-native approach to address this barrier and

unlock TAM capture.



#### Hypothesis 3: Partner Data Integration Differentiates Through Platformization and Intelligence



**What we tested:** Can we platformize all partner data using Job

Postings as the first data source, creating a repeatable system that

eliminates UX lift for future datasets?



**Results:** Identified a critical scalability problem---when the data

team adds new datasets, they require significant UX lift to integrate

into the application, creating delays and inconsistent user experiences.

Our solution: standardize all Partner Data so any future data source

automatically works with the Workbooks experience without additional UX

development. The team built a data set schema that classifies each data

field, applies matching operators accordingly, and runs data through

normalization services so \"KS,\" \"Kansas,\" and \"KANSAS\" all

normalize to \"Kansas.\" This creates a repeatable platform where future

partner datasets plug in seamlessly.



**Key learning:** Multi-team coordination revealed we need a dedicated

end-to-end PM owner for partner data. Our competitive moat isn\'t just

having more data sources---it\'s the normalization and platformization

infrastructure that makes every dataset trustworthy and immediately

usable without custom engineering work.



#### **Go-forward Changes & Plan**



Q4 priorities focus on **1) Revenue Acceleration in RingLead** and **2)

Planning, dependency mapping, and beginning development for MVP Sellable

Product in GTM Studio**.



**Revenue Acceleration (M1-M3):** Deploy POC Data Health Scan enabling

targeted outbound motion across 3,900 accounts to drive qualified upsell

conversations. Deliver RingLead retention enhancements---credit

utilization visibility, Enrich Premium+ expansion to HubSpot/Dynamics,

and route improvements---protecting our \$28M+ renewal base.\

\

**MVP Foundation Building (M4):** Complete planning, dependency mapping,

and start development work for Data Foundation Management---dedupe,

normalize, segment capabilities for both CRM bulk operations and

workbooks. This delivers table-stakes functionality that enables future

AI capabilities while immediately reducing manual routing effort,

forming the core of our sellable GTM Studio product.



**Future Scaling (M5-M6):** Plan AI-assisted onboarding targeting 2-week

implementation timelines versus today\'s 3-6 months. Design proactive

data quality protection preventing issues at entry points rather than

reactive cleanup.



#### **Leveraging AI**



**Q4 expansion:** AI-assisted configuration recommendations for data

management setup. We\'ll analyze patterns from similar customers in each

industry vertical, providing intelligent starting points for dedupe

rules, normalization standards, and segmentation logic. This reduces

setup complexity while maintaining safety through graduated human

involvement---low-risk configurations get automated recommendations,

high-impact changes (affecting large record volumes or critical

workflows) require human review and approval.



Specifically for Proactive Data Quality Protection workflows (list

imports, web submissions, triggers), AI will suggest validation rules

based on existing CRM patterns and industry standards, but humans

approve before rules prevent data entry. This balances scaling

implementation speed with protecting against unintended consequence.

