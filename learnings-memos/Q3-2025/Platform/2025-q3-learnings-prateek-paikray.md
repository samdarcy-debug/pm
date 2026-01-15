---
id: learnings-2025-052
title: Q3 2025 Learnings Memo - Prateek Paikray
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/prateek-paikray]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



**1. Active Integrations*\***

We made strong progress in improving GTM Studio's integration experience

and flexibility.



- Released the new GTM Object Viewer and Custom Field Extension

  capabilities, allowing customers to bring in additional fields from

  external systems when standard mappings don't exist.



- Launched the enhanced Import Mapping Experience, giving customers more

  control over which data points are imported into GTM Studio.



**2. Credits per Record under Management (RUM)**



**a. Expanding Data Activation Capabilities\**

Delivered an in-app product experience that lets customers create Cloud

Data Shares directly from GTM Studio, powered by Bobsled and our

workflow infrastructure.

[[\[Demo\]]{.underline}](https://zoominfo.slack.com/archives/C01NA8B3R28/p1754487127270669)



- Snowflake support is now live behind a feature flag.



- Databricks support is planned for November, with Engagement Data

  Shares expected by the end of the year or early January 2026, aligned

  with monthly release cycles.



**b. Extending Credit Consumption via new products :**



With the launch of the GTM Intelligence Layer (AI Context Service) via

MCP, we're expanding credit consumption through new products and

services. At Dreamforce (Oct 14), we'll launch Salesforce Agentforce on

the AppExchange

[[Listing]{.underline}](https://appexchange.salesforce.com/appxListingDetail?listingId=b8475d03-96ab-4bb2-b350-93074d1f6def),

giving Copilot customers a natural-language way to access ZoomInfo data,

insights, and AI summaries directly within Salesforce.



\[Demo 1 \]:

[[https://video.zoominfo.com/watch/Btd1yNS8zbWJEBUPBQ5dHw]{.underline}](https://video.zoominfo.com/watch/Btd1yNS8zbWJEBUPBQ5dHw)



\[Demo 2\]**:**

[[https://video.zoominfo.com/watch/gn657VEQexBWZQZNsqQSSe]{.underline}](https://video.zoominfo.com/watch/gn657VEQexBWZQZNsqQSSe)**\**



**c. Building the Internal Dataset Marketplace:\**

Work is in progress on an Internal Dataset Marketplace, where GTM Studio

users will be able to browse, preview, and request datasets. This will

serve as a core foundation for a unified, self-service data discovery

and activation experience across the platform.



#### **Key Learnings**



As part of the GTM AI Context initiative, we conducted discovery calls

with enterprise customers, including Red Hat, Intuit, ADP, Juniper

Networks, IBM, and ABM Industries, while building the Agentforce

solution. A consistent theme was the desire to create a unified

experience for sellers, with AI viewed primarily as a productivity

enabler. However, many customers are still exploring how AI can drive

true differentiation and transform core workflows. ZoomInfo is

well-positioned to meet these evolving needs through Agentforce, MCP

integrations, and Copilot Workspace / GTM Studio.



We learned from partner sellers that several enterprise customers using

BigQuery want direct access to ZoomInfo company and contact data within

their data warehouse via Data Share, without the need to copy data. This

represents a strong opportunity aligned with our 2025+ roadmap,

leveraging Bobsled and its Data Product offering to support such

customers.



With the launch of vertical datasets (e.g., Licensing Dataset), ZoomInfo

is positioned to complement SaaS-based solutions in vertical markets ---

such as

[[ServiceTitan]{.underline}](https://app.zoominfo.com/#/apps/profile/company/358474455/overview?url=%2Fapps%2Fhome-page&titleText=Homepage&profileId=358474455&checkProfileAccess=true)

[[(valuation:

\~\$8B)]{.underline}](https://finance.yahoo.com/quote/TTAN/) by

delivering differentiated, data-driven intelligence tailored to specific

industries.



Internally, it became clear that educating app teams on how to leverage

core platform services, including the GTM Data Model and GraphQL Query

capabilities built over the past year, is critical for reducing

redundant efforts, retiring technical debt, and accelerating delivery of

scalable products. Customers continue to ask for integrated, flexible,

and intelligent experiences, and strengthening our platform enablement

strategy will be key to delivering on that vision.



#### **Hypotheses & Results**



**1. Hypothesis:\**

Enterprise customers are looking for AI solutions that improve seller

productivity while integrating seamlessly into their existing workflows.



**Result:\**

Discovery calls with Red Hat, Intuit, ADP, Juniper Networks, IBM, and

ABM Industries confirmed that AI is viewed primarily as a productivity

enabler, with strong interest in unified seller experiences. This

validated our decision to embed the GTM Context AI Service into

Agentforce, aligning directly with how customers plan to operationalize

AI in 2026.



**2. Hypothesis:\**

AI differentiation will come not just from model performance, but from

contextual data and workflow integration.



Result:\

During the discovery call, enterprise customers like Mastercard have

consistently questioned the defensibility of standalone AI solutions as

they experiment with various POCs, whether through Agentforce, Power BI

Agentic offerings, or ZoomInfo Copilot for their business needs. Their

responses reinforce that ZoomInfo's true advantage lies in its

data-driven context and deep integration capabilities delivered through

MCP, Agentforce, or selling our own products, whether it is Copilot,

Copilot workspace or GTM Studio.



**3. Hypothesis:** Customers using modern data stacks (BigQuery,

Snowflake, Databricks) will prefer direct data access models over

traditional exports or syncs.



**Result:\**

Partner sellers confirmed that BigQuery customers want access to

ZoomInfo data via Data Share, eliminating the need to copy or replicate

data. This validates our investment in Bobsled's Data Product and the

roadmap for Engagement Data Shares across Snowflake and Databricks.



#### **Go-forward Changes & Plan**



My focus for Q4 is centered around three key initiatives:



1.  Launch the Internal Dataset Marketplace -- Enable GTM Studio users

    to browse, preview, and request datasets, creating a unified

    discovery and activation experience.



2.  Expand AI Capabilities within Agentforce -- Integrate the GTM

    Context AI Service to enhance existing Agentforce functionality and

    deliver richer, context-aware insights directly within Salesforce.



3.  Extend Data Activation through Bobsled -- Add support for creating

    Engagement Data Shares with Snowflake and Databricks, allowing

    customers to access and activate their data seamlessly across cloud

    ecosystems.



Together, these initiatives strengthen our platform foundation and

position Zoominfo for broader scalability and AI-driven growth heading

into 2026.



#### **Leveraging AI**



I plan to try a new approach by building agents using the **ZI Chatbot**

for the initial internal feature launch. The goal is to onboard the

internal tech support team faster by reducing dependencies on SMEs and

the engineering team, accelerating onboarding, and ensuring consistent

communication across teams. Additionally, will work on expanding the

initiative by integrating the existing toolset AI capabilities

[[\[Demo\]]{.underline}](https://zoominfo.slack.com/archives/C01NA8B3R28/p1756400408831729),

like ADA bot AI, into our product, enabling users to self-serve

integration issues and significantly reduce support inquiries to the

engineering team. In essence, AI will act as a virtual enablement and

support layer, helping teams learn, adopt, and troubleshoot faster

across the product ecosystem.

