---
id: learnings-2025-050
title: Q3 2025 Learnings Memo - Menna Rashwan
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/menna-rashwan]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
*This quarter centered on executing against the Enterprise Search

strategy --- operationalizing the customer pain points and hypotheses

[[identified

earlier]{.underline}](https://docs.google.com/document/d/1_YtN8N8Z6m79aXc7REJHaRzltIzMGjLkWhWsX1_yaHc/edit?usp=sharing)

into tangible platform capabilities.*



#### **Metric Alignment**



Our Q3 Enterprise Search work contributes to the Data Flywheel by

creating infrastructure that drives data contribution and consumption.

Improving the 1P data search (GTM Data Model as a source of truth,

enabling search across both matched AND unmatched CRM records), we\'re

incentivizing customers to contribute more complete datasets (#1 Data

Contribution → Best GTM Data). The Workbooks integration with Signals

and Partner Data feeds into Best Models (#2 Workflow Data Contribution),

as these signals enrich customer workflows and generate actionable

insights.



This foundational work sets up future consumption growth---once Q4 GA

enables platform-wide search, customers will be able to discover and

action more data through unified search experiences, driving Higher

Copilot Activation and ultimately More Consumption. The standardized

filtering and cross-CRM search capabilities remove friction from data

discovery, making it easier for customers to integrate more data sources

(Integrations).



#### **Key Learnings**



+----------------+-----------------------------------------------------+

| **Dual-track   | Q3\'s biggest success was enabling Workbooks        |

| delivery**     | September GA and advancing federated search         |

|                | platform work by decoupling from platform           |

| Shipping       | dependencies (Metadata Service, CDC, Schema         |

| customer value | Registry). By implementing interim solutions, we    |

| while building | delivered customer value months earlier through     |

| platform       | Workbooks GA while simultaneously building the      |

| foundations    | foundational infrastructure for scalable Enterprise |

|                | Search (Federated Search) for 1P CRM data. This     |

| Requires       | wasn\'t just about speed; it demonstrated we could  |

| accepting and  | make progress on both customer-facing features and  |

| managing       | platform capabilities in parallel without waiting   |

| technical debt | for perfect architecture.                           |

| strategically. |                                                     |

|                | **The tradeoff:** we knowingly accepted technical   |

|                | debt that requires Q4 refactoring to support        |

|                | federated search at a platform level. This was      |

|                | communicated and aligned upfront, not a surprise.   |

|                | However, as major dependencies are completed in Q4, |

|                | the team should be laser-focused on integrating     |

|                | with the necessary APIs as they become available to |

|                | deliver ultimate value.                             |

+----------------+-----------------------------------------------------+

| **API          | Initial Enterprise Search scope focused on 1P CRM   |

| integration    | data, which we successfully delivered. However, as  |

| scope can      | we began GraphQL integration planning (GraphQL      |

| expand         | being the customer-facing API layer for Enterprise  |

| dramatically   | Search), the scope expanded significantly. GraphQL  |

| when bridging  | requires both 1P CRM data and 3P ZoomInfo data      |

| platform       | available in the GTM Data Model. Adding 3P data     |

| layers**       | introduces a substantial new workstream: defining   |

|                | schemas and standardization across the platform for |

| Surface these  | ZoomInfo company and person data. This was not      |

| gaps early.    | originally scoped and lacks a clear long-term       |

|                | owner. Search is temporarily driving this work,     |

|                | focused on priority use cases to unblock federated  |

|                | search, until permanent ownership is established.   |

|                |                                                     |

|                | **Learning:** When defining API integration scope,  |

|                | map the entire data flow end-to-end including all   |

|                | required data sources upfront, and identify         |

|                | ownership gaps before they become blockers.         |

+================+=====================================================+



**Hypotheses & Results** [[Federated Search Use

Cases]{.underline}](https://docs.google.com/spreadsheets/d/1ctx0gbmJcUogecNORiqhcnUJz2j0a01j4JOoxmSzw_k/edit?gid=604006857#gid=604006857)



+------------------------------------------------------------------------------------------+----------------------------------------------+

| **Building Federated Search Infrastructure for 1P CRM Data Will Establish the Foundation | We successfully built the core federated     |

| for Platform-Wide Search Capabilities Across Applications**                              | search infrastructure focused on improving   |

|                                                                                          | 1P CRM data. However, to unlock broader      |

| [[Federated Search                                                                       | platform value and enable truly dynamic,     |

| Demo]{.underline}](https://hello.chorus.ai/listen?guid=c301aee6e60140769a901c858145a7a9) | real-time search at scale, Q4 work must      |

| (31:37 - 39:30)                                                                          | complete critical integration layers (CDC,   |

|                                                                                          | Metadata Registry, Schema Registry) and      |

|                                                                                          | enable application teams across the platform |

|                                                                                          | to consume federated search capabilities     |

|                                                                                          | through a standardized customer-facing API ( |

|                                                                                          | via GraphQL integration).                    |

|                                                                                          |                                              |

|                                                                                          | *We built the engine; now we need to connect |

|                                                                                          | it to the rest of the platform ecosystem.*   |

+------------------------------------------------------------------------------------------+----------------------------------------------+

| **Enabling Search Across Matched and Unmatched 1P CRM Data with Standardized Filtering   | We successfully delivered search across both |

| Will Unlock Previously Hidden Customer Data and Improve Workflow Efficiency**            | matched and unmatched CRM records with       |

|                                                                                          | standardized filtering across Salesforce,    |

|                                                                                          | HubSpot, and Dynamics.                       |

|                                                                                          |                                              |

|                                                                                          | True workflow efficiency gains await Q4      |

|                                                                                          | GraphQL integration for platform-wide        |

|                                                                                          | access.                                      |

+------------------------------------------------------------------------------------------+----------------------------------------------+

| **Signals & Partner Data Integration Through Enterprise Search Will Drive Workbooks      | We successfully delivered Phase 1 Signals    |

| Adoption and validate federated search**                                                 | (Websights, Technologies Added/Dropped,      |

|                                                                                          | Intent, Employment Changes, Scoops, Funding) |

| [[Workbooks signals+Job postings                                                         | and Partner Data (Job Postings) through      |

| Demo]{.underline}](https://hello.chorus.ai/listen?guid=693a9a9e53dd4321952ae49d7d50ddad) | Enterprise Search for Workbooks September    |

| (16:30 - 19:33)                                                                          | GA. Customers can now create signal-based    |

|                                                                                          | workbooks and perform enrichments for both   |

|                                                                                          | signals and job postings. This validated our |

|                                                                                          | federated search technical foundation while  |

|                                                                                          | identifying gaps needed for platform-wide    |

|                                                                                          | scaling.                                     |

+==========================================================================================+==============================================+



#### **Go-forward Changes & Plan**



*\'We built the engine; now we need to connect it to the rest of the

platform ecosystem.\'*



[[Expanded milestone

view]{.underline}](https://docs.google.com/spreadsheets/d/1L7m4e3D6Ym2xfxob8j_RKb2uzSL6rLtLG1Ete3OEwkI/edit?gid=1448180808#gid=1448180808)



+-----------------+----------------------+-----------------------------+

| **Theme**       | **Pain-Points**      | **Q4 Milestones**           |

+-----------------+----------------------+-----------------------------+

| **Enable        | Newly introduced     | **#1** Building Indexer     |

| dynamic,        | first-party data     | Pipeline (foundation work)  |

| real-time, and  | attributes are not   |                             |

| configurable    | instantly searchable |                             |

| indexing by     | or filterable        |                             |

| utilizing       |                      |                             |

| schema metadata | \- Reduces           |                             |

| and CDC-based   | effectiveness for    |                             |

| data flow.**    | customers in         |                             |

|                 | prospecting,         |                             |

| *(integration   | segmentation, and    |                             |

| with CDC,       | prioritization       |                             |

| metadata        |                      |                             |

| service and     | \- Increases         |                             |

| schema          | internal development |                             |

| registry)*      | cost                 |                             |

|                 |                      |                             |

|                 | \- Predefined search |                             |

|                 | filters do not       |                             |

|                 | support unique       |                             |

|                 | business-specific    |                             |

|                 | criteria, forcing    |                             |

|                 | users to work around |                             |

|                 | system limitations.  |                             |

|                 |                      +-----------------------------+

|                 |                      | **#2** Federated Search     |

|                 |                      | integration with CDC to     |

|                 |                      | capture data level changes  |

|                 |                      | in real-time                |

|                 |                      |                             |

|                 |                      | \- New Records              |

|                 |                      | Added/Records Deleted       |

|                 |                      |                             |

|                 |                      | \- Value changes on a       |

|                 |                      | Record                      |

|                 |                      |                             |

|                 |                      | \- Publishes change events  |

|                 |                      | to Kafka for indexing       |

|                 |                      +-----------------------------+

|                 |                      | **#3** Federated Search     |

|                 |                      | integration with schema     |

|                 |                      | registry/meta data to       |

|                 |                      | detect structural changes   |

|                 |                      | (H2)                        |

|                 |                      |                             |

|                 |                      | \- New Fields/attributes    |

|                 |                      | added to objects            |

|                 |                      |                             |

|                 |                      | \- Field type modifications |

|                 |                      |                             |

|                 |                      | \- Provides single source   |

|                 |                      | of truth for schema         |

|                 |                      | definitions                 |

|                 |                      +-----------------------------+

|                 |                      | **#4** CRM Custom Fields →  |

|                 |                      | Make it a platform solution |

|                 |                      | and not only a workbooks    |

|                 |                      | app solution                |

+-----------------+----------------------+-----------------------------+

| **Enable        | Customers can't      | **#5** Federated search     |

| federated       | access GTM           | foundational work           |

| search          | intelligence through |                             |

| capabilities    | a single, consistent |                             |

| via Graphql     | interface.           |                             |

| API**           |                      |                             |

|                 | \- Data is spread    |                             |

| *(integration   | across first-party,  |                             |

| with graphQL)*  | third-party, and     |                             |

|                 | partner systems,     |                             |

|                 | each with its own    |                             |

|                 | query patterns,      |                             |

|                 | filters, and APIs.   |                             |

|                 |                      |                             |

|                 | \- This forces       |                             |

|                 | customers (and apps) |                             |

|                 | to stitch data       |                             |

|                 | together manually,   |                             |

|                 | creating             |                             |

|                 | inefficiencies,      |                             |

|                 | broken workflows,    |                             |

|                 | and incomplete       |                             |

|                 | insights.            |                             |

|                 |                      +-----------------------------+

|                 |                      | **#6** ZI Company & Contact |

|                 |                      | data collection (Defined    |

|                 |                      | and standardized schema,    |

|                 |                      | available in the GTM DM)    |

|                 |                      +-----------------------------+

|                 |                      | **#7** Make the new ZI      |

|                 |                      | company and contact data    |

|                 |                      | collection searchable       |

+=================+======================+=============================+



#### **Leveraging AI**



- **Conceptualization:** Used AI to generate quick **conceptual mocks**

  that helped articulate product ideas like NLP and Federated Search,

  improving cross-team understanding and alignment.



- **Knowledge Capture:** Used AI to summarize **meeting transcripts**,

  surface key decisions and asks, and quickly extract product

  requirements.



- **Simplification:** Leveraged AI to **translate technical artifacts**

  (schemas, architecture docs) into consumable PM content.



  - Example: mapped a **Solr schema with 350+ fields** by type and

    behavior in minutes---work that previously took hours or days and

    engineering support.

