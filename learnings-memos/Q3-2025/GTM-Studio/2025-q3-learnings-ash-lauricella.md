---
id: learnings-2025-014
title: Q3 2025 Learnings Memo - Ash Lauricella
type: doc
status: approved
team: gtm studio
owner: '[[teams/gtm studio/_people/ash-lauricella]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm studio
related: []
---
#### **Metric Alignment:** Credits per Record Under Management (RUM) per Tenant



**GTM Studio Workbooks (Q3 Delivered):** Unblocking CRM data directly

expands enrichable records by providing access to business-critical

custom fields and filtering capabilities. Customers previously had

limited CRM data access, but now they can work with familiar workflows

using the same filtering capabilities from their CRMs. Snowflake import

adds data warehouse records as a new, enrichable data source beyond CRM

systems. This drives credit utilization by creating more first-time

enrichments and increasing credit utilization as customers export more

companies and contacts.



**AI Data Management (Future Impact):** Credit/Vendor Notifications

delivered in RingLead enable confident large-scale enrichment scheduling

by alerting on credit thresholds and vendor failures. AI Data management

roadmapping and strategy sets the foundation for systematic RUM

expansion. When released, DHS will surface unenriched records,

AI-assisted onboarding will reduce setup from 6 months to 2 weeks, and

bulk deduplication will increase quality confidence, driving broader

enrichment adoption.



#### **Key Learnings**



**CRM functionality must match the familiar workflows of sales and

revenue operation leaders.** Internal sales leaders like Rob Lotterman,

Alex Lazerowich, Steve Lincoln, and Lou Wolf spend their days working

inside CRMs, building reports, running pipeline reviews, and managing

their books of business. Their expectations are shaped by years of using

those systems, from field naming conventions to the ability to build

custom queries. When we onboarded them to the early access program for

Workbooks, the friction surfaced as they couldn't access custom fields,

owner or manager filters, or familiar data structures. As a result, they

were unable to effectively adopt the Workbooks product and had to

continue relying on their existing Salesforce reports to manage their

teams. External customers, such as Stensul, voiced the same frustration,

reinforcing that these capabilities are essential to how sales

organizations operate

([[snippet]{.underline}](https://hello.chorus.ai/listen?guid=dd8566e48fcc499695836484a57028bc)).

Once we introduced custom field support and hierarchy-based filtering,

users could replicate their core workflows seamlessly, leading to higher

adoption and satisfaction. The takeaway is simple: our CRM capabilities

must empathize with users' existing habits and expectations, matching

the flexibility and familiarity of the tools they rely on daily.



**Advanced and flexible capabilities like complex matching logic are

table stakes for enterprise data management.** Enterprise customers view

complex matching logic as table stakes for data management. During GTM

Studio onboarding, many early access customers reinforced this point

with Engine stating, "That's the reason we don't use ZoomInfo and use

RingLead," directly referencing the lack of customizable matching logic

in GTM Studio workbook exports.. This feedback validated the urgency of

bringing RingLead's advanced data management capabilities, including

sophisticated matching rules, deduplication, and normalization, into GTM

Studio. Without them, we cannot compete in enterprise data management

use cases.



**Building Data Trust is Foundational for** **Enterprise Adoption.** As

we expand into enterprise segments, a critical learning from onboarding

**USPS** to RingLead (our Data Management product) and from early access

onboarding with **LSEG** in GTM Studio is the importance of building

data trust. These organizations undergo rigorous security reviews to

ensure data retention, transit, and encryption policies meet their

standards before allowing any processor access. Unlike Salesforce, which

has already earned that trust through years of validation, ZoomInfo is

still in the process of establishing the same level of confidence. To

serve enterprise and regulated industries effectively, we need to

implement strict data protection and retention policies that make

customers comfortable entrusting us with their data.



In the meantime, while we work toward that level of trust, we need to

support both integrations, the GTM Data Model and direct CRM

connections, to meet customer needs today. From there, both delivery

paths can coexist under a unified strategy grounded in enterprise-grade

trust and governance, guiding our M4 approach to AI data management.



#### **Hypotheses & Results**



**Enhanced CRM data access enables customers to more efficiently build

audiences that match their CRM workflows**



We validated demand by expanding CRM support, with Early Access

confirming enterprise-scale performance. Adoption improved, but each

release surfaced new needs such as engagement data, lookup fields in

filters, and advanced query logic, showing that customers expect no

limitations.



**Hypothesis 2: AI-assisted configuration and guidance reduce setup

time, complexity, and reliance on support**



Strong validation. Conversational configuration makes setup easier by

translating business requirements into auto-generated rules, similar to

working with an implementation manager. Prototype feedback from Sales,

CX, and Engineering confirmed that AI guidance and interactive workflows

would drive adoption more than automation alone, with strong demand for

troubleshooting that explains errors and suggests fixes, task and play

recommendations, "art of the possible" discovery, and interactive

resolution screens. Users want guidance alongside automation, not

black-box execution, and embedding AI that explains, guides, and assists

throughout the workflow removes dependency on support tickets and

enables true self-service. This insight shapes our M4--M5 strategy:

embedding intelligence that explains, guides, and assists throughout the

workflow.



**Hypothesis 3: Multi-platform CRM support expands market and drives

consumption**



Validated through Concentra's purchase, a \$526K, 3-year deal and one of

New Business's top 10 largest wins ever in both ACV and TCV, and the

\$300K upsell opportunity with IWG PLC, we confirmed strong enterprise

demand. M2 testing with Concentra further proved that we can execute the

same use cases previously only possible in Salesforce. Expanded CRM

access through Discover has increased exports of companies and contacts,

driving higher credit utilization and RUM. Platform diversity is proving

critical for both enterprise penetration and ongoing consumption growth.



#### **Go-forward Changes & Plan**



**GTM Studio Workbooks:** The learning that customers expect parity or

similar experiences with their CRM reporting when working with CRM data

in workbooks drives our focus on completing September cut scope. We will

deliver lookup fields in query filters, engagement data, and advanced

query logic to meet expectations for CRM reporting parity.



**AI Data Management:** The validation that AI guidance resonates more

than automation alone shapes our M4-M5 execution. We\'re building

conversational configuration and intelligent troubleshooting that

eliminates support dependency. The discovery that enterprises split into

two groups (those requiring direct CRM for security/compliance versus

those needing GTM DM for unified intelligence) drives our two-part

architecture with unified configurations. RingLead usage analysis in Q4

will inform prioritization and train AI models. M2 deliverables (Change

Logs and Performance Dashboard) will generate customer feedback that

fuels our roadmap. DHS development continues as a product-led growth

entry point.



#### **Leveraging AI**



We leveraged ZI Chat with Anne Fajkus to experiment with AI-assisted

matching logic as an addition to deterministic configurations. This

validated that AI can help with pattern recognition in complex matching

cases, informing future hybrid approaches that combine deterministic

logic with AI intelligence. This directly informed our prototype

approach, confirming that users want AI for understanding and guidance,

not just automation.



We plan to build conversational configuration that translates business

requirements into technical rules, intelligent troubleshooting that

eliminates support tickets, \"companies like yours\" recommendations

trained on RingLead usage analysis, context-aware guidance with

progressive disclosure, hybrid matching approaches building on ZI Chat

experimentation, and DHS intelligence that quantifies business impact.

