---
id: learnings-2025-004
title: Q3 2025 Learnings Memo - Unknown PM
type: doc
status: approved
team: dai executive
owner: '[[teams/dai executive/_people/unknown-pm]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- dai executive
related: []
---
# **Quarterly Business Review (QBR): Ops and Analytics**



## **Opening Context Paragraph**



Over the past quarter, Product Operations has driven a step-change in

how ZoomInfo builds, launches, and scales products by embedding AI

deeply into GTM workflows, maturing foundational data infrastructure,

and accelerating operational rigor. We operationalized an AI-powered

content and enablement engine that transforms talk tracks, marketing

materials, and customer-facing assets into personalized,

account-specific agents - reducing manual lift for sellers and PMMs

while improving impact on critical Q4 renewals. Foundational analytics

and instrumentation for Copilot Workspace and GTM Studio are now in

place, enabling visibility into adoption, workflow performance, and API

usage far earlier than previous launches. In parallel, we delivered

major advancements in our knowledge infrastructure - including a

neo4j-powered Knowledge Graph and automated documentation workflows -

creating a scalable source of product truth for both humans and AI

agents. Operationally, we increased launch execution maturity through

consistent Monthly Customer Releases, formalized off-cycle processes,

and removed blockers for key tools like the Voice of Customer agent and

account-level product visibility. Underpinning all of this, we

modernized core infrastructure - from enriched historical analytics in

Amplitude to microapp connections for ZI Chat and Tableau optimization -

laying the groundwork for scalable AI applications, trusted data, and

faster decision-making across the business.



## **Section 1: Progress and Momentum Areas**



## 1. Product Operations and GTM Automation Efficiency



> The team achieved a strategic shift by embedding AI agents into the

> sales and product marketing workflows, creating highly personalized,

> cross-product content and establishing foundational infrastructure to

> accelerate Go-to-Market (GTM) execution.



- **Comprehensive GTM Talk Track Agents:** **Copilot V2 talk tracks and

  Q&A documentation** were delivered with approval from leadership

  (Dominik and Victor) and converted immediately into

  **account-customized agents**. This agentic foundation is crucial for

  arming sellers with the right messaging for Tier 1 products (such as

  Copilot V2, GTM Studio, and Context Service, where API usage analysis

  is advancing) and impacting critical Q4 renewals.



- **Foundational Cross-Product Marketing Content Engine:** The **AI

  Product Marketing Management (PMM) engine** was streamlined by

  consolidating previous modules (1-3) into a single interface, which

  takes less time and produces similar or better content results. This

  PMM engine is designed to generate personalized sales content,

  marketing copy, content, and assets by synthesizing data from sources

  like calls, signals, and web research, ensuring alignment with brand

  narrative and key product messaging.



- **Personalized Account-Based Sales Agents:** Multiple **personalized

  account-based agents** were shipped to provide sales representatives

  with custom documents for client interactions, directly addressing

  massive time sinks for Account Managers. This included

  **account-specific roadmaps and release notes agents** delivered as

  part of the Monthly Customer Release (MCR). Furthermore, the **AM

  slide generator** was tested as a working text prototype that aims to

  reclaim significant time for AMs by creating customized **meeting prep

  decks**.



- **Adoption Driven by Delivery Method:** Testing revealed that the

  **delivery method significantly impacts adoption**, with actual slides

  performing much better than PDF documentation when presented to

  stakeholders. This reinforced the need to integrate these tools

  seamlessly into existing GTM workflows, as initial usage of agents

  like the personalized account roadmap remained low despite high

  expressed demand.



## 2. Tier 1 Analytics and Instrumentation (Workspace and Studio)



> Foundational analytics infrastructure was built and deployed for

> Workspace and Studio products, enabling initial understanding of user

> behavior and adoption patterns necessary for feature optimization and

> launch readiness (note: despite implementation gaps, foundational

> reporting is available much faster than with Copilot 1.0 last May)



- **Copilot Workspace Launch Readiness:** A complete **end-to-end funnel

  framework for Copilot Workspace launch** was delivered by Phoebe Mei,

  breaking down workflows (e.g., search → generate AI email → send

  email) into measurable stages with defined KPIs. Tracking

  infrastructure was implemented for the internal rollout to 100+ GTM

  users, positioning the team for comprehensive adoption analysis during

  the external launch. Clear alignment from the beginning on target

  workflows to measure with clear alignment with product leadership on

  value drivers.



- **P0 Instrumentation Blockers Resolved:** Despite encountering initial

  issues during the Workspace rollout, the team identified and worked

  with engineering to resolve a **P0 instrumentation bug blocking user

  ID capture** in Amplitude, ensuring clean data for linking AI chat

  engagement to user cohorts. BI has been slowly significantly reporting

  and analyzing emerging usage in Workspace and Studio due to pervasive

  instrumentation gaps and bugs. BI is driving an effort to standardize

  taxonomy of all events in Workspace and Studio, and implement event

  and property guidelines for eng teams (as they are data producers).



- **Unified Workspace Data Source:** Work is actively underway to build

  a **unified data source that combines both frontend and backend data

  for Workspace**, which will enable trusted, end-to-end visibility of

  usage and accelerate answers to critical business questions.



- **API Usage Analysis Foundation:** Phase I of the **API Data

  Exploration** was launched to test and validate essential data points,

  structure queries, and build a scalable dashboard. This ensures

  accurate, reliable data for tracking API usage and performance, which

  is critical for building trust in reporting and informing future

  product decisions.



## 3. Knowledge Infrastructure Development



> The team established the technical foundation and systematic processes

> required to maintain a scalable, accurate source of product truth for

> both internal teams and AI agents.



- **Knowledge Graph (KG) Architectural Breakthrough:** A significant

  infrastructure win was achieved by pivoting the Knowledge Graph system

  to use **neo4j** instead of the original database approach. This pivot

  unlocks out-of-the-box features like document processing, deletion,

  update, and validation that would have otherwise required extensive

  custom development.



- **Knowledge Graph Foundation:** The Knowledge Graph prototype was

  deployed in a dedicated GCP sandbox environment, initially focused on

  GTM Studio. The KG successfully processed **over 100 documents** from

  the AI marketing engine knowledge base, creating a foundation of

  atomic notes, concepts, and relationship mapping.



- **Product Dossier Prototype:** A **V1 Product Dossier template** was

  created and built out with a full example for Advanced Search,

  transforming the Product Knowledge Base from a concept into a

  tangible, human-readable working prototype.



- **Documentation Automation Efficiency:** The updated feature info pack

  process cut PM documentation time by **50%** (from 60+ minutes to

  approximately 30 minutes) through AI optimization. Additionally, AI

  agents were built and piloted to automatically update implementation

  guides and knowledge center documents.



- **Knowledge Base Maintenance Strategy:** The team recognized that

  maintaining a useful product knowledge base requires not only adding

  new knowledge but also **systematically removing incorrect or outdated

  information**. Efforts shifted to building agents that handle the

  automatic updating and pruning motion to keep the source of truth

  fresh.



## 4. Operational and Process Maturity



> The team drove significant improvements in release execution

> consistency, formalized processes for complex off-cycle launches, and

> resolved deployment bottlenecks for critical internal AI tools.



- **Monthly Customer Release (MCR) Consistency:** There has been very

  high compliance with making a clear go/no-go decision 7 days prior to

  the MCR, with only 1-2 features not complying. Process improvements

  included streamlining requirements (making demo videos mandatory but

  how-to guides optional) and simplifying documentation needs (replacing

  complex GIFs with simple screenshots). Despite the massive change to

  this motion from PMM and Launch Ops, PMM and prod ops were able to

  stabilize the ship in very little time and ensure nothing critical

  failed during this time of great transition.



- **Off-Cycle Release Process Formalization:** Work is underway to

  **document and systematize the off-cycle release process**

  (specifically for GTM Studio and Copilot Workspace releases) to

  eliminate confusion and manual coordination for future launches and

  ensure consistent execution. For the remainder of H2 and through Q1,

  there will be a formal off cycle process for Studio and Workspace so

  that specific dates are pre-determined. This predictability

  significantly helps our enablement and CX/CS partners.



- **VoC Tool Deployment Unblocked:** Major blockers for the **Voice of

  Customer (VoC) tool deployment** were eliminated by pivoting to the

  semantic data team\'s existing **agentic platform**. This strategic

  pivot provided immediate deployment capabilities, leveraging pre-built

  optimizations for transcript searching.



- **Single Source of Truth for Account Level Product Characteristics:**

  Today there is no source of truth to identify product level

  characteristics for an account, i.e., which specific features and

  in-platform experiences a given account has based on which alphas,

  betas, early access features, packages, SKUs, experiments, etc they

  are in. We made significant progress in establishing this by

  integrating LaunchDarkly feature flagging data into the chatbot,

  thereby enabling all teams (specifically Customer Experience (CX)

  teams), to access this data in real time. This will provide CX teams

  visibility into which features are impacting specific customers,

  enabling better support. We will work through integrating other

  necessary data in Q4.



## 5. Foundational Infrastructure and Tech Capabilities



> Key infrastructure projects were completed or significantly advanced,

> providing the platform capabilities necessary to scale advanced

> analytics, AI tools, and data accessibility across the organization.



- **Amplitude Historical Attribute Enrichment:** The team successfully

  implemented the **Amplitude Profiles** feature with Change Data

  Capture (CDC), resolving the challenge of attributing user/account

  data retroactively to historical events. This capability allows for

  the creation of rich, granular cohorts based on attributes like

  Segment, Persona, and CRM Connected, unlocking robust historical

  analysis. This data is automatically updated and does not rely on

  manual refreshes, as it had previously.



- **Semantic Data to ZI Chat Microapps Connection:** A critical

  breakthrough was achieved by establishing **MCP connections between

  the semantic data backend and ZI Chat**. This microapps deployment

  approach resolves persistent deployment errors and networking issues,

  creating a robust foundation for all future AI application

  deployments.



- **Chatbot Data Accessibility:** Work advanced to make core account

  setup data available in the ZI Chatbot, allowing users to quickly

  access account setup status details and improving visibility for GTM

  and Product teams. This was the first set of product data we partnered

  with PMs and eng leads on to push into the chatbot. Learnings from

  this experience will help us as we push to have key data on Workspace

  and Studio pushed into the chatbot in Q4.



- **Tableau Server Optimization:** A strategic project was completed to

  streamline and optimize the **Tableau Server environment** by

  identifying over 250 unused or non-functioning dashboards/workbooks

  and data sources, which will reduce storage costs, improve

  performance, and simplify stakeholder access.



## **Section 2a: Forward-Looking Challenges We Need to Solve to Unlock the Next Level**



The following systemic issues require executive attention to unlock the

next level of scaling, operational efficiency, and platform capability.



### **Scaling Challenges: Ensuring Workspace Analytics are Operational at Scale**



The primary scaling challenge is ensuring that data generated by the new

Copilot Workspace and GTM Studio can be reliably tracked and

operationalized for external rollout.



- **P0 Instrumentation Bug in Copilot Workspace:** Despite the internal

  launch, a P0 instrumentation bug is blocking the capture of user IDs

  in Amplitude for several events, including key Workspace chat events

  (one of three core value pillars identified by Victor). This technical

  failure means we cannot currently tie AI chat engagement back to

  specific user cohorts or reliably measure daily utilization and

  time-to-value for the second batch of 100 internal sellers. Resolution

  requires immediate engineering leadership prioritization (Lars) to

  prevent corrupted data from scaling into the external launch planned

  for October.



- **Low Conversion and Utilization Baseline:** Early Copilot adoption

  sits around 10% utilization with conversion restricted to just 1--2

  users per 100 seats across scoped accounts (e.g., SafetyCulture,

  Xactly Corporation). This low conversion rate indicates that current

  deployment and enablement approaches are not yet driving the necessary

  enterprise-scale operationalization required to realize the

  platform\'s full revenue potential. We need architecture to scale

  successful MPOC (Minimum Point of Contact) enablement models.



### **Resource/Organizational Bottlenecks: Resolving Strategic Deadlocks**



Organizational friction and philosophical differences are creating

strategic uncertainty and resource waste, requiring explicit executive

direction.



- **Account Health Scoring Methodology Conflict:** The disconnect

  between CSM leadership (Whitney/Antuna) and ELT/Product/BI teams on

  account health measurement remains a critical bottleneck. CSM

  leadership is fundamentally opposed to adopting a simple

  Red/Yellow/Green or continuous score, forcing AJ Belen and the team to

  pivot to using basic, delayed Renewal Prediction Scores (RPS) as a

  temporary measure. Executive intervention is required to establish a

  clear, unified measurement philosophy (actionability vs. renewal

  prediction) that aligns GTM incentives and avoids continued resource

  allocation to contested work.



- **Low Adoption of High-Value GTM Agents:** Despite successful delivery

  of personalized AI-powered content agents (e.g., personalized roadmap

  and release notes) designed to eliminate manual work, internal

  adoption is critically low. The personalized account roadmap saw only

  4 uses, and Henry\'s company-wide email promoting the tools only

  generated 30--40 additional uses before plateauing. The consensus is

  that GTM teams are overwhelmed by information (25 different links) and

  these tools are not seamlessly integrated into existing workflows.

  This systemic gap threatens the ROI on our AI PMM infrastructure and

  requires a cross-functional enablement strategy overhaul to drive

  workflow integration.



### **Infrastructure Gaps Blocking Further Progress**



Critical infrastructure projects are stalled due to resource allocation

constraints and inherent platform complexities, preventing deployment of

key AI-driven capabilities.



- **Semantic Layer Implementation Blockade:** The deployment of the

  unified semantic layer, which is essential for AI-powered business

  intelligence (AI Chat functionality) and consistent metric

  definitions, is blocked by resource constraints within the engineering

  team. Despite clear business value and Phoebe Mei completing the data

  requirements, the project requires explicit prioritization from

  Russell/Nir to allocate capacity for pipeline and subnet model

  development.



- **Product Information Knowledge Base Deprioritization:** A

  foundational gap exists in the systematic management of Product

  Information Knowledge (technical documentation, feature specs). This

  knowledge is distinct from product marketing content and is critical

  for internal teams (CSM, Support) and feeding AI agents for accurate

  answers. Daniel Kong noted that this strategic imperative continues to

  be displaced by tactical fires. We need to define and protect

  resources to build this central source of truth to prevent multiple

  teams from solving similar problems using outdated information.



- **CDP/Data Pipeline Instability:** Multiple analytical workstreams are

  blocked by intermittent CDP data connectivity issues and data pipeline

  deprecation. Nanxi Ge\'s investigation revealed that the LaunchDarkly

  Snowflake tables were deprecated in June without a replacement,

  eliminating the data pathway needed for CX teams to identify which

  customers are impacted by beta releases. This requires urgent

  resolution (API troubleshooting with Guy or formal request to restore

  Snowflake tables) to prevent ongoing support challenges.



### **Cross-Functional Coordination Needs**



Coordination gaps require structured engagement models to ensure data

quality and accelerate high-value strategic projects.



- **Renewals Prediction Data Latency:** Renewal Prediction Score (RPS)

  data delivery from Tony\'s team is consistently delayed, taking 2+

  weeks monthly to finalize. This structural delay impacts the

  timeliness of executive reporting and strategic planning sessions. We

  need a formal SLA to establish clear second-week delivery expectations

  to manage stakeholder confidence.



- **Integration Data Completeness Gaps:** Integration data analysis

  uncovered important coverage gaps, particularly concerning export

  tracking across vendor types and the complete absence of Org Import

  data from current tables. Ferrell Tanuwidjaja also noted that export

  data remains disconnected from the integrations dashboard. This lack

  of comprehensive bi-directional integration reporting necessitates a

  full data audit to ensure executive reporting reflects true customer

  integration patterns.



## **Section 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters**



Based on the above forward looking challenges generated from the LLM,

these are overall correct. However, there are a couple of gaps that i

would call out:



1)  Need to drive motion to have **PMs be more intentional and robust

    about *how* features will impact customers and *what* is needed to

    drive desired outcomes**. This was a key responsibility of product

    marketing previously, and with the June changes, PMs now are

    responsible and accountable for this work. Often times the execution

    and operational work needed to make a feature achieve customer

    impact is not thought through by PMs, potentially due to lack of

    time & prioritization, and/or training and experience.



2)  Need to create an objection handling agent to support sales (new

    business and R&G) for **Workspace** in particular, and also

    **Studio** (and eventually Context Service). This will serve as a

    critical feedback loop for the talk track agents we have created and

    the other assets and motions put in place to support these roll outs



3)  Need to **drive usage of the agents**, having a **mindset of a

    product manager**, i.e., creating the agent is not enough. Instead,

    what we've created is a MVP; now we get feedback, analyze how

    customers use it, and use the input to prioritize highest value

    enhancements.



4)  Need to be more proactive in terms of **instrumentation readiness**

    by creating a standard taxonomy for Workspace and Copilot events,

    getting alignment with PM owners, and then working with PM and eng

    leads to implement. We are wasting resources and delaying analysis

    by releasing features with events that have missing or inaccurate

    event and property information. Needs to be done correctly the first

    time



## **Section 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?**



## [Overall across our initiatives KPIs have not been established upfront and measured systematically. We need to do a better job of this morning forward, and expect this QBR motion (new for prod ops) to help with that.]{.mark}



1.  Product Operations and GTM Automation Efficiency



    a.  PM Productivity gain (e.g., PRFAQ process now takes less than

        50% of the time it did previously)



    b.  PMM and GTM team productivity gain (i.e., reducing time needed

        to create foundational assets for tier 1s as well as additional

        assets / copy / collateral for various marketing motions related

        to these Tier 1s)



    c.  Agent adoption rate and usage



2.  [Tier 1 Analytics and Instrumentation (Workspace and Studio)]{.mark}



    a.  [Ability to support key product decisions (e.g., go/no go for

        release to all internal reps for workspace) and drive product

        investment decisions (i.e., which pain points or unmet needs to

        focus on and potentially how)]{.mark}



3.  [Knowledge Infrastructure Development]{.mark}



    a.  PM Productivity gain (e.g., reduced time to update knowledge

        center articles)



    b.  Established MCP connections between semantic data backend and ZI

        chat



4.  [Operational and Process Maturity]{.mark}



    a.  [Process integrity and consistency (e.g., MCRs with few to no

        features pushed at the last minute)]{.mark}



    b.  [Offcycle releases that release successfully, with CX/CS and

        enablement support and no gaps]{.mark}



5.  [Foundational Infrastructure and Tech Capabilities]{.mark}



    a.  [Getting key data into the chatbot (e.g., Copilot setup). Need

        to focus on driving usage of this data in Q4]{.mark}



    b.  [Update of A/B testing framework by BI needs to drive increased

        experimentation by PMs (with AND withOUT BI support)]{.mark}



## **Section 4: Beginning vs. End Contrast Table \[July 2025 vs. September 2025\]**



This table contrasts key operational and analytical areas, illustrating

the transformation journey from identifying blockers in July to

establishing momentum and capabilities by September.



  --------------------------------------------------------------------------------------------------

  **Operational Area** **START MONTH: July 2025    **END MONTH:         **Transformation /

                       Blockers / Status Quo**     September 2025       Progress**

                                                   Momentum /           

                                                   Achievement**        

  -------------------- --------------------------- -------------------- ----------------------------

  **Account Health     Philosophical dispute over  Pivot established to Shifted from philosophical

  Scoring**            continuous scoring; CSM     use basic Renewal    deadlock to a pragmatic,

                       leadership (Whitney)        Prediction Scores    actionable executive

                       resistance to R/Y/G         (RPS) for            reporting framework,

                       methodology.                September-December   mitigating strategic

                                                   expiries for ELT     uncertainty.

                                                   reporting.           



  **User Attribute     Historical Amplitude        Amplitude Profiles   Resolved critical technical

  Data Pipeline**      attribute tracking blocked  with Change Data     debt, unlocking rich,

                       due to immutable event      Capture (CDC)        granular historical user

                       model, preventing           successfully         behavior analysis for PMs

                       retroactive analysis.       implemented by       across the full customer

                                                   Preetham Srinithi,   lifecycle.

                                                   resolving historical 

                                                   attribution.         



  **AI Agent           Internal tools (VoC,        Sam Darcy            Broke a critical

  Deployment           Knowledge Graph) deployment established          infrastructure bottleneck,

  Infrastructure**     blocked by                  microapps deployment creating a scalable,

                       infrastructure/networking   foundation via       permanent platform

                       issues, requiring manual    semantic data        (microapps) for rapid AI

                       workarounds.                backend connected to agent deployment for all

                                                   ZI Chat, eliminating future tools.

                                                   persistent           

                                                   deployment errors.   



  **GTM Enablement     PMs spending 60+ minutes    PM feature info pack Achieved quantified 50%

  Content Creation**   creating feature info       time cut by 50% (to  productivity gains in core

                       packs; knowledge center     \~30 mins) via AI    PM workflows through

                       updates manual and stale.   optimization. Daniel AI-powered content

                                                   Kong automated       automation and process

                                                   knowledge center     streamlining.

                                                   refreshes, reducing  

                                                   update time to \~30  

                                                   mins.                



  **Retention Insight  Analytical focus on         Discovery            Shifted retention focus from

  Strategy**           standard renewal predictors breakthrough: Nanxi  lagging indicators to a

                       (CRM connection,            Ge revealed that     predictive, behavioral

                       provisioning rate).         customer usage       signal (end-of-contract

                                                   spikes at contract   usage spike) for earlier CS

                                                   end, with renewers   intervention.

                                                   showing dramatically 

                                                   higher adoption      

                                                   rates than churners. 



  **Copilot Workspace  Readiness planning ongoing; V2 launched          Moved from planning to

  (V2) Tracking**      core product utilization    internally to 100+   tactical, real-time

                       low at 10% and conversion   GTM users; P0 user   debugging of V2 launch

                       restricted to 1--2 users    ID instrumentation   metrics, securing a cleaner

                       per 100 seats.              bug immediately      data foundation for the

                                                   identified and       external rollout planned for

                                                   escalated for        early October.

                                                   resolution.          



  **Cross-Functional   No single source of truth   Caleb Munson         Transformed fragmented

  Project Alignment**  for Tier 1 project          achieved DAI         planning into a unified,

                       dependencies; multiple      sign-off on H2 T2    risk-mitigated H2 execution

                       teams working in isolation. project milestones   plan, establishing Product

                                                   (GTM                 Ops as a critical

                                                   Studio/Copilot),     coordination function.

                                                   mitigating           

                                                   substantial          

                                                   misalignment and     

                                                   material risk.       

  --------------------------------------------------------------------------------------------------

