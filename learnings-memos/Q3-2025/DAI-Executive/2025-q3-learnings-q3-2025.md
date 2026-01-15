---
id: learnings-2025-003
title: Q3 2025 Learnings Memo - Q3 2025
type: doc
status: approved
team: dai executive
owner: '[[teams/dai executive/_people/q3-2025]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- dai executive
related: []
---
# **QBR Instructions for DAIs**



## **Overview**



Draft executive summaries for each DAI are available in the tabs of this

document for the upcoming QBR covering June - September 2025.



These drafts were created by synthesizing all weekly reports from your

teams over this 4-month period. Each summary follows the standard QBR

format with progress areas, forward-looking challenges, and a beginning

vs. end contrast table. This is simply a starting point from the weekly

reports. All DAIs are responsible for their final QBR output.



## **Next Steps**



- Review your draft summary in the corresponding tab



- Edit and refine as needed for accuracy and completeness



- Submit final version by **Wednesday, October 8th**



## **Additional Resources**



If you want to reference the original source material for more detail,

we\'ve created NotebookLM for each team that contains all weekly reports

from this period.



- [**[GTM

  Studio]{.underline}**](https://notebooklm.google.com/notebook/93eb4b93-e55c-46ec-9973-db520a8759f2)



- [**[Copilot]{.underline}**](https://notebooklm.google.com/notebook/d1775846-13c6-4102-8517-c27dd1061e73)



- [**[Data]{.underline}**](https://notebooklm.google.com/notebook/c1b74b83-700b-4778-814b-a75c82d0aa8d)



- [**[Platform]{.underline}**](https://notebooklm.google.com/notebook/ca952e9d-4130-493d-80e4-c12ffaaa2276)



- [**[Intelligence]{.underline}**](https://notebooklm.google.com/notebook/912e2452-178f-47f1-8169-fcad8b3fb45c)



- [**[Ops/BI]{.underline}**](https://notebooklm.google.com/notebook/ca2196a0-fd5a-4e9a-a715-504f6930f047)



Drafts



GTM Studio



# **Quarterly Business Review (QBR) -- GTM Studio Team**



## **Opening Context Paragraph**



The GTM Studio team secured the foundational infrastructure for the

September GA launch, notably achieving architectural alignment for GTM

Plays activation and establishing the path to unblock ROI Analytics for

over 8,000 HubSpot customers. Significant momentum was generated through

the internal deployment of the AI Agent, which onboarded 15+ users and

delivered breakthrough conversational capabilities. However, immediate

executive intervention is required to resolve systemic scaling

challenges in the AI Agent semantic search layer, finalize the long-term

strategy for critical vendor dependency risks (DeltaX), and address a

fundamental customer activation gap exposed during early access

requiring comprehensive field readiness support.



## **Section 1: Progress and Momentum Areas**



The third quarter focused heavily on delivering foundational

capabilities required for the September GA, validating key architectural

decisions, and securing early customer validation that translates

technical features into significant GTM potential.



### **I. AI & Agentic Capabilities: Customer Validation and Architectural Breakthrough**



The GTM Studio Agent, driven by Jagannath Ramesh and Arun V,

transitioned from prototype to internal production readiness,

demonstrating transformative potential for complex workflows.



- **Internal Validation and Adoption:** The GTM Studio Chat Agent moved

  into production with 15+ active internal users onboarded, exceeding

  the initial user goal and receiving consistently positive feedback.



- **Breakthrough Use Case:** Rob Lauren from sales leadership

  successfully completed a full ICP building workflow through the

  conversational interface alone, confirming the agent\'s ability to

  reshape end-to-end data interaction patterns.



- **Enhanced Enrichment Capabilities:** Jagannath\'s team delivered

  major capabilities expansion, completing multi-column enrichment that

  integrates Data Agent, CRM data, and custom signals (intent spikes,

  tech aggregates, scoops).



- **Architectural Scalability Insight:** A major architectural discovery

  revealed that the Workbook\'s Unified Data Platform (UDP) interface

  can leverage Model Context Protocols (MCP) to enable \"create workbook

  from any source\" capabilities. This paradigm shift resolves previous

  limitations and creates a path for general-purpose AI integration

  across multiple data sources.



- **FAQ Agent Reducing Support Dependency:** Arun\'s team successfully

  developed and staged the FAQ Agent for the ROI Dashboard, addressing

  the overwhelming complexity of presenting 20+ metrics to customers

  through self-service AI assistance.



### **II. ROI Analytics: Unblocking HubSpot Customers and GA Readiness**



The ROI Analytics team, primarily led by Brahm Kohli and Arun V,

achieved critical milestones necessary for GA readiness, specifically

resolving the data blocker that threatened the launch timeline for a

large segment of the customer base.



- **HubSpot Customer Unblock Strategy:** Brahm Kohli secured critical

  alignment with the Platform PM team on a dual-path strategy to unblock

  over 8,000 HubSpot customers whose ROI insights were constrained by

  the missing opportunity data gap.



- **Data Migration Validation:** GTM Data Store migration engineering

  work was completed and deployed to staging. Arun\'s team tested 5 beta

  accounts and validated a 99% data matching rate between the legacy ZDP

  tables and the new GTM Data Store tables.



- **Customer Validation & Feature Delivery:** The team achieved strong

  positive validation for ROI dashboard and FAQ agent capabilities

  through a 150+ CSM LTS session. Key features prepared for release by

  mid-September include the FAQ Agent, Filter by Interaction Type,

  User-Level Interactions Correlation, and enhanced CRM Error Handling

  screens.



- **Competitive Positioning:** Corina Soto successfully leveraged the

  ROI Impact Analysis release notes (rushed by Arun V) to include the

  feature in the Gartner Magic Quadrant review, mitigating risks related

  to previous poor competitive scores.



### **III. Activation and GTM Plays: Architectural Clarity and Market Readiness**



Q3 established the necessary architectural boundaries and activation

pathways to transition GTM Studio insights into seller action, setting

the stage for H2 execution.



- **Plays Architectural Alignment:** Veronica Hudson and Mohan Sun

  resolved a major blocker by finalizing ownership: the Platform team

  will fully own Workflows execution, while GTM Studio will own the

  wrapper object (connecting Workflows to Workbooks, reporting, and

  state management). This moves the initiative into the build stage.



- **Copilot Integration Pivot:** A critical technical decision was made

  to pivot the Studio-to-Copilot data transmission from the incompatible

  Workflow-based approach to a new solution leveraging GraphQL queries

  through the GTM Data Store. This change ensures a direct pipeline from

  GTM Studio to seller-specific Copilot Views, unblocking a key

  activation path.



- **September GA Coordination:** Tanvi Vaidya delivered exceptional

  execution on GA coordination. The production release for Signals

  enrichment and signal-based workbooks is targeted for September 30th.



- **Customer Adoption Momentum:** The team successfully ramped up

  customer engagement, reaching 10 active customers in workbooks. The

  pipeline is projected to accelerate to 25--30 customer accounts by

  mid-September, amplifying urgency to resolve infrastructure blockers

  before the soft launch.



### **IV. Data Management: Revenue Opportunity and Foundational Planning**



The Data Management team, including Brahm Kohli, Ash Lauricella, and

Corina Soto, validated a significant new revenue stream and created a

detailed multi-year roadmap.



- **Identified Revenue Opportunity:** Analysis by the Data Management

  team revealed a cross-sell/upsell opportunity targeting approximately

  4,000 existing ZI customers. This potential revenue stream justifies

  accelerated execution of Data Health Scan initiatives.



- **Strategic Roadmap Foundation:** Ash and Corina completed the

  foundation for the detailed 2025--2026 execution plan, aligning

  milestones with key stakeholders across Customer Success and Sales.

  This framework supports the Data Health Scan POC, designed to drive

  upsell revenue.



- **Job Posting Feature Launch:** Job posting functionality was

  successfully pushed to production under a feature flag in early

  September, despite initial P0 blockers related to data quality and

  operator logic requiring taxonomy normalization.



## **Section 2a: Forward-Looking Challenges We Need to Solve**



To unlock the next level of execution and capitalize on the strong Q3

momentum, executive attention is required to address systemic challenges

related to scaling, infrastructure, and field readiness.



### **I. Scaling Challenges (Architecture for Scale)**



We must resolve key technical bottlenecks that inhibit enterprise

adoption and agent capabilities at scale.



- **Semantic Search Scalability Blockade (Jagannath Ramesh):** The GTM

  Studio Agent\'s most critical technical bottleneck is the semantic

  search layer, which currently limits processing to only a few hundred

  rows. This limitation directly prevents execution for large enterprise

  customers, leading to crucial market validation delays (e.g., the

  Silver Fort demo was postponed twice). This systemic lack of

  scalability undermines market differentiation against competitors like

  Clay.



- **Agent Guardrail Implementation (Arun V):** The implementation of

  essential security and access control guardrails for the Self-Serve

  Analytics Agent remains blocked. This systemic issue prevents

  customers from accessing authorized tables and tenant-filtered data

  via SQL query access control, creating a mandatory security and

  functionality gap that must be closed before the self-serve agent can

  be productionized for GA.



- **Federated Search Limitations (Tanvi Vaidya):** Current workbook

  architecture faces technical limitations where federated search does

  not support layering data points from different sources (e.g., website

  visitor signals with company firmographics). This forces temporary

  workarounds that are not scalable and requires transitioning to a new

  architecture with a timeline extending to the end of the year.



### **II. Infrastructure Gaps Blocking Further Progress**



Critical GA readiness is gated by Platform alignment and vendor risk

mitigation.



- **GTM Data Model Coverage Gap (Brahm Kohli / Andres Perez):** Despite

  the data migration path being defined, the ROI GA remains blocked

  because the GTM Data Model lacks coverage for Opportunity data for

  approximately 50% of HubSpot customers. This gap affects not just ROI

  but all future workbook and Copilot integrations relying on

  opportunity data. Consistent ROI Beta sentiment requires securing

  definitive Platform commitment for data quality validation and

  consistency to prevent cascading delays.



- **Vendor Dependency and Renewal Risk (Mohan Sun):** Vendor

  relationship management with DeltaX presents a strategic business

  continuity risk. The recent production incident caused by DeltaX

  having unrestricted access to internal accounts highlights the

  vulnerability. The migration effort to mitigate this risk is

  significantly under-resourced with only one developer assigned,

  creating renewal and customer continuity risk. A decision is needed to

  either accept locked-in, long-term contracts (3+ years) or directly

  develop LinkedIn API access to eliminate dependency and price

  manipulation risks.



### **III. Cross-Functional Coordination Needs & Organizational Bottlenecks**



Organizational structure challenges and coordination gaps are impeding

both execution velocity and market adoption success.



- **Customer Activation and Field Enablement Gap (Sneh Kakileti):** The

  most critical challenge is the activation barrier faced by customers

  who cannot effectively translate Studio insights into seller actions.

  Customer feedback consistently asks, \"How do I get talking points and

  next best actions to sellers?\". This is a core product-market fit

  concern requiring immediate, high-level strategic alignment between

  Product, Sales, and Customer Success leadership to define and resource

  a comprehensive field readiness and enablement initiative.



- **AI Credit Flow Misalignment (Tanvi Vaidya):** The coordination

  complexity surrounding AI action credit flows, involving multiple

  stakeholder teams, is causing misalignment and continuous requirement

  changes. A unified coordination structure is required to finalize

  backend processing requirements and ensure the design aligns with

  technical capabilities before final implementation.



- **Workflow Integration Limitations (Mohan Sun):** The foundational V1

  workflow system utilized for workbook export cannot support essential

  sales engagement features like add-to-sequence, add-to-campaign, or

  cadence management out-of-the-box. This technical gap impacts all

  downstream activation pathways (Outreach, Salesloft, RingLead) and

  requires additional orchestration capability development.



## **Section 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters**



\[Placeholder\]



## **Section 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?**



\[Also include what success looks like next quarter \]



## **Section 4: Beginning vs. End Contrast Table \[July 2025 vs. September 2025\]**



The table below contrasts the GTM Studio team\'s operational state

across seven key areas at the start of Q3 (July 2025) versus the end of

the period (September 2025), illustrating the transformation journey

from blockers to momentum.



Copilot



# **Quarterly Business Review (QBR): Copilot Team**



## **Opening Context Paragraph**



The most significant achievement this quarter was the successful launch

of Copilot Workspace, which progressed from initial concept to full

internal deployment across all ZoomInfo employees. While foundational

components---Views, Chat, and Notes---are now operational, the critical

work ahead focuses on integrating these features into seamless,

intuitive workflows that deliver the \"magic moments\" for users.



Beyond Copilot Workspace, the quarter marked a pivotal transition from

product concept to delivery, with the team successfully advancing

multiple strategic initiatives from planning to deployment. The team has

transformed the way they work, eschewing traditional product management

practices for AI-native practices. Every product starts with agents and

evals, then prototypes, before design and engineering. Agents built this

quarter are: Profile summaries, next best action, emailer, meddpicc

extraction.



With product delivery well underway, the next step is to translate this

to Copilot renewals. The primary metric of the team is to increase the

renewal rate of Copilot customers with \$61m in renewals left between

now and end of year.



## **Section 1: Progress and Momentum Areas**



The team achieved significant quantifiable milestones across core

strategic initiatives, moving products from planning and prototyping

phases into initial rollout and internal adoption, validating key

technological and market hypotheses.



**Business impact**



The key metric is driving Copilot renewals using Copilot Workspace

customer motivation. We won't see a groundswell effect until November 3

when sales is allowed to sell Workspace, but there have already been

several renewal saves and early renewals centered around Workspace.



### **Strategic Theme: AI Agentic Platform Delivery and Validation**



The Copilot team was both a partner and the first customer of the AI

Agentic Platform. Just as important as delivering agentic products, the

Copilot team completely revamped the product management process. Every

new product started with creating agents using the platform, evals and

user validation, prototyping, and only then was the team allowed to

start designing and building. Below is a list of products that were

created *agent-first*.



- **Next Best Action (NBA) Agent:** Ant Cuomo and team created an NBA

  agent as part of the next gen Company and Contact profiles. This

  allowed the team to immediately do user validation. Ant worked with

  several sales leaders and account executives as eval partners. For

  example: Account executive for the Dell account, Jason Sherman, rated

  ZI Chat outputs A- for immediate executability. This validation proves

  our capability to deliver relevant and actionable intelligence at

  scale using the agentic platform, achieving near-parity performance

  with the \"gold standard\" ZI Chat outputs after prompt engineering.

  It also allowed us to evaluate real world product viability at very

  low resource cost.



- **AI Emailer Agent:** Gabe Pirela delivered a working Copilot Chat

  email prototype using the agentic platform in August, integrating

  multiple data sources and tools for inclusion in the September Copilot

  V2 beta. By mid-September, the team successfully transitioned the

  email agent to a sub-agent pattern architecture, unlocking scalable

  and reliable bulk email use cases while improving repeatability and

  token efficiency across all chat interactions. This model should be

  replicated for other agent development initiatives. The AI Emailer

  agent's output consistently gets praised by Copilot Workspace users.



- **MEDDPICC Extraction Agent:** The internal pilot for automated

  MEDDPICC extraction was kicked off in September, enabling 25+ reps to

  receive automated post-call analysis via Slack integration. This

  feature reached 80% completion in the pilot phase, focusing on

  validating the extraction logic and potential CRM writeback

  functionality before investing heavily in UI.



### **Strategic Theme: GTM Copilot Workspace Launch Readiness**



We successfully executed initial internal product rollouts and defined

the critical user experience path required to drive adoption and

retention in Copilot Workspace. The original go-live data was 10/6, it

has now been moved to 11/3 as a mutually agreed decision between GTM and

product leaders.



- **Foundational Features In Place, The Next Step Is Maniacal Focus on

  Refinement**: Views, chat, notes, navigation, and other foundational

  features are now functional. That's a huge milestone, but the next

  milestone is connecting these features together to deliver easy to

  use, seamless workflows for users. The magic moment for users is when

  these features work together to deliver value. We're not there yet but

  we're not far off. The key is to keep the team focused on delivering

  the top 3 workflows while preventing feature creep.



- **Copilot Workspace Achieves Internal Rollout:** Sean Walter and Adam

  Severance executed a successful internal launch of Copilot Workspace

  in September to over 100 users. They increased that to 200 the

  following week, and then to all employees the week after. This

  operational win builds confidence for the upcoming GTM Copilot launch,

  which is targeting \$61M in renewals through year-end. The internal

  testing is generating extensive feedback, driving immediate

  optimizations in critical areas like view manipulation and chat

  context accuracy before releasing to customers.



- **Company and Contact Profiles Redesign:** Ant Cuomo partnered with

  Lindsay Bongo and delivered significant improvements to these well

  used features. The primary shift was to go from overwhelming the user

  with data to a simple, bird\'s-eye intelligent summary at the top.

  These have gotten constant praise from our GTM leaders and ICs.

  However, there is a part two to this evolution. Ant Cuomo is expanding

  the profile agent to provide context aware summaries for signals,

  engagement, CRM fields, and more. They are also adding the next best

  action agent (Already evaluated by the field) to make profiles

  actionable.



### **Strategic Theme: Intent Platform Modernization and Revenue Protection**



We drove significant product launches for the Intent platform while

identifying and addressing critical long-term revenue and operational

risks.



- **Intent Topic AI Recommendation Launched:** Harinath Krishnamoorthy

  achieved a major milestone by rolling out the Intent Topic AI

  Recommendation feature to 100% of eligible customers in August. The

  feature provided immediate recommendations for approximately \~3,000

  accounts. This launch validated the hypothesis that AI-driven setup

  dramatically improves user experience by providing recommendations

  post-launch rather than requiring manual configuration.



- **\$1M+ Revenue Leak Identified and Mitigated:** Post-launch analysis

  by Harinath Krishnamoorthy uncovered critical production gaps,

  including unauthorized platform runs and incorrect scheduling, which

  also exposed an ongoing revenue leakage issue of potentially \$1M+

  annually from uncontrolled custom topics. Harinath secured buy-in from

  Carlos (GTM Strategy) to prioritize automation of deprovisioning fixes

  and established a plan to manage Intent platform limits through

  configuration-driven entitlements, transforming revenue management

  from error-prone manual code to a scalable system.



- **Enterprise Segmentation Unlocked (Multi-AFS):** Multi-AFS enterprise

  feature validation was completed in September, confirming data

  consistency within a 95% accuracy threshold. This launch is a

  significant competitive differentiator that addresses customer

  requests for expanded Account Fit Score capabilities. It also

  positioned ZoomInfo ahead in the Forrester Wave evaluation and is

  intended to unlock new revenue streams through enterprise package

  upgrades.



- **Automated Migration Framework Designed:** The design framework for

  automating Intent platform migration was completed and validated with

  stakeholders. This directly addresses a major sales objection against

  competitors like 6sense/DemandBase by eliminating migration friction,

  reducing customer onboarding time from weeks to hours and accelerating

  deal cycle length.



### **Strategic Theme: Enterprise Workflows and Competitive Positioning**



Progress was made in delivering foundational enterprise management tools

and enhancing external market positioning.



- **Admin Defined Territories (ADT) Validation:** David Goulden

  progressed ADT to 90% completion on end-user explainability for GA

  readiness. Beta expansion onboarded 5 additional customers in August.

  Crucially, internal analysis validated the strategic approach, showing

  that user-defined territories delivered 50% better conversion rates

  after 6 months compared to baseline. This feature improves adoption of

  the existing Whitespace Suggestions feed.



- **Competitive Positioning Strengthened:** The team successfully

  completed a comprehensive review and enhancement of assigned Forrester

  Wave RFI responses, focusing on GTM data differentiation, Chorus, and

  Copilot V1. Victor Oliveros and Gabe Pirela also executed a strong

  Gartner Magic Quadrant (MQ) demo, positioning us favorably for

  potential \"Leaders\" quadrant placement.



- **Leadership Transition Seamlessly Executed:** Despite operating at

  80% capacity in early July due to simultaneous transitions, Darrell

  Grissen and Vinay Kamath successfully handed off their duties to

  Victor Oliveros by July 18th with minimal disruption and preservation

  of institutional knowledge via comprehensive documentation.



## **Section 2a: Forward-Looking Challenges We Need to Solve**



Systemic issues that require executive resource allocation and

architectural decision-making are threatening our ability to scale GTM

Copilot V2 and meet critical enterprise customer demands.



### **Scaling Challenges**



These issues pertain to product quality and platform reliance that must

be fixed to ensure Copilot Workspace drives adoption across the company

and customers.



- **Copilot Chat Trust and Performance:** The Copilot Workspace internal

  launch revealed important improvement requirements for the core

  conversational interface. The first issue was context - Chat was not

  aware of the View context the user was looking at which caused

  hallucinations. This issue has since been resolved. The next issue is

  View creation and management - users had a difficult time creating

  views. The fix is natural language view creation and should be

  resolved before November 3.



- **Intent Recommendation Relevancy Limit:** The Intent Topic AI

  Recommendation launch provided a strong baseline, but data analysis

  reveals the current relevancy rate is only 30-60% for key enterprise

  accounts. This pattern validates the need for continuous investment in

  Phase 3 development to address fundamental limitations, such as

  incorporating dynamic lookback periods and improving recommendation

  algorithms for power users who represent the majority of our revenue.



### **Resource/Organizational Bottlenecks**



Organizational friction points and resource fragility are compounding

delivery delays and forcing strategic compromises that impact feature

scope.



- **Design Resource Bottleneck:** Multiple teams are converging on GTMC

  development simultaneously (V2 onboarding, Profiles, Mobile, Advanced

  Search), leading to severe design capacity constraints. This systemic

  bottleneck forced Adam Severance to deprioritize Advanced Search V2

  development in favor of focusing resources on higher-impact emailer

  functionality for the November timeline. Executive intervention is

  needed to strategically reallocate or acquire dedicated design

  capacity to secure Q4/H1 2026 delivery timelines.



- **QA Protocol Gaps:** The Intent feature launch exposed structural

  issues in our testing protocols, allowing critical production bugs

  (e.g., unauthorized platform runs, incorrect scheduling) to reach

  customers. Harinath Krishnamoorthy flagged that recent QA team

  reductions are creating pervasive testing bottlenecks across all

  releases, forcing engineers to handle end-to-end testing of their own

  code. A formal testing protocol overhaul and dedicated QA resources

  are required to maintain release quality standards and customer trust.



- **Engineering Capacity and Maintenance Tension:** The Advanced Search

  team is grappling with reduced engineering capacity (due to

  constraints in Israel) while simultaneously needing to deliver

  Microsoft accessibility compliance, natural language search

  capabilities, and GTM data model integration. Current resourcing is

  insufficient to meet both maintenance needs (maintaining legacy

  systems) and next-generation innovation.



### **Infrastructure Gaps Blocking Further Progress**



Critical platform architecture decisions and technical debt are

preventing us from unlocking key enterprise revenue opportunities and

modernizing core experiences.



- **Federated Search Blockage for Enterprise CRM Matching:** The most

  critical infrastructure gap is the blockage of Priority Accounts CRM

  matching capabilities by the federated search architecture, which may

  not deliver until Q1 2026. This failure impacts our ability to support

  custom CRM fields and account team objects required by high-value

  enterprise customers, exemplified by escalations from HPE and Juniper

  Networks who urgently need Account Team Member object integration.

  Immediate alignment from search leadership is required to define an

  interim GraphQL solution or accelerate federated search delivery.



- **Advanced Search Migration Complexity:** The transition of Advanced

  Search (used by 40K SalesOS users) to the GTM data model requires

  immediate architectural decisions. Uncertainty persists regarding

  potential breaking changes to existing CRM filters, saved searches,

  intent features, and alerts functionality. This risk necessitates

  clear ownership boundaries and technical migration alignment across

  Platform, Enterprise Search, and Apps teams to minimize disruption

  during customer renewal periods.



### **Cross-functional Coordination Needs**



These challenges span business strategy, entitlement management, and

architectural handoffs, requiring explicit process redesign and senior

alignment.



- **Packaging Architecture Limiting GTM Studio TAM:** The current

  requirement mandates Copilot Enterprise access for GTM Studio

  features, including signal-based workbooks, which severely constrains

  the addressable market, as most SalesOS customers lack this

  entitlement. This technical bundling, which exists for business rather

  than technical reasons, threatens utilization metrics and prevents

  intent tab modernization for the primary user base. Urgent executive

  alignment with Mark Harris is necessary to make a business decision to

  decouple GTM Studio functionality.



- **Intent Entitlement Clash Technical Debt:** A chronic entitlement

  clash issue blocks efficient Copilot upsells, specifically preventing

  existing customers from receiving newly purchased topic limits (e.g.,

  stuck at 12 topics instead of 500). This technical debt requires

  mediation between two engineering teams and validation via a new

  master user staging environment, threatening customer satisfaction and

  future workbook upsells.



## **Section 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters**



- **Product delivery must translate to sales:** While this quarter was

  focused on product delivery, success moving forward will be measured

  in renewal rates and AI credit driven revenue. The product must go

  through significant refinements to provide self explanatory value and

  show high adoption rates



- **Ruthless prioritization for design resources:** Resource constraint

  is a constant. This does not mean we let it hold back the roadmap.

  Bucket roadmap items into two groups



  - Significant needle movers - Items that clearly differentiate our

    products and have high potential for driving adoption. This should

    receive most design resources



  - Other features - Items that are valuable, but by themselves are not

    adoption drivers. The product managers need to use genAI prototypes

    to get the experience to 80% and then work with design to finish



- **Performance and reliability:** This is the biggest issue with

  Workspace today. There are constant View and Chat regressions with

  every production release. These regressions will not be tolerated by

  customers, especially when value through AI credits must be proven.

  The bar is high and i'm confident we will meet it but it starts with

  holding a high bar for QA



## **Section 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?**



**Success this quarter**



Copilot v1 Renewals



- Tracking Copilot v1 renewal rate vs SalesOS only customers



Agent-first development



- Has resulted in making the correct product decisions early due to

  agent eval as the first step



Success next quarter



AI credits through Workspace



- Workspace must be the vehicle that provides value in exchange for AI

  credits



Copilot enterprise renewals with Workspace add on



- The new SKU must perform better than the original Copilot enterprise

  sku with the promise of AE/AM specific AI productivity



## **Section 4: Beginning vs. End Contrast Table \[July 2025 vs. September 2025\]**



This table contrasts the state of key operational areas at the start of

the quarter (July 2025) versus the end (September 2025), illustrating

the transformation journey from blockers to momentum.



Data



# **Quarterly Business Review (QBR): Data**



This Quarterly Business Review (QBR) draws upon executive reporting from

July through mid-September 2025, detailing significant advancements in

vertical data productization, compliance infrastructure, and geographic

expansion, while highlighting critical architectural and organizational

dependencies that require executive intervention to sustain momentum.



## **Section 1: Progress and Momentum Areas**



### **Vertical Datasets and Go-to-Market (GTM) Acceleration**



The team successfully validated and accelerated the vertical dataset

strategy, positioning the organization to achieve its H2 revenue

targets:



- **Revenue Validation:** Tactical planning confirmed the \$5M H2

  revenue target is realistic through account-to-dataset mapping

  analysis, identifying sufficient high-value customers who can consume

  data in bulk.



- **Dataset Launch Success:** The Contractor Dataset was successfully

  delivered with strong early market signals, including several demos

  booked by the GTM team, providing a proven template for future

  releases. We have been delivering new datasets ahead of schedule.



- **Franchise Productization:** The team processed 12,000 PDF files to

  extract comprehensive location and operator data for 3,000 US

  franchises, creating a product identified as a \"game changer\" that

  no competitor offers.



- **Market Demand Confirmed:** Customer conversations consistently

  demonstrated that vertical datasets address existing pain points,

  supporting aggressive H2 revenue targets. The franchise dataset, in

  particular, generated unexpectedly strong market demand, with

  customers immediately requesting samples. \$11.5M in pipeline has been

  created on vertical datasets, with \$275k closed in H2.



- **GTM Enablement:** Comprehensive vertical dataset training was rolled

  out to all GTM teams, generating hundreds of qualified leads and

  indicating strong market demand for restaurant, contractor, and

  franchise datasets. The GTM.ai site successfully launched, providing

  public access to the new data marketplace and showcasing the

  integrated GTM studio experience.



Current state of datasets against H2 Roadmap:



![](media/image2.png){width="6.5in" height="3.6527777777777777in"}



### **Core Data Asset and Geographic Expansion**



A major breakthrough in data infusion capabilities positions the

organization for rapid geographic scaling:



- **New Company Creation Reaccelerated:** New company profiles are being

  added at scale. The October cube includes 1.9M new company profiles,

  950k are active and marketable (Tier A), and 500k are located outside

  of the US. This comes on top of 500k companies added as a part of the

  July cube, addressing geographical coverage challenges for customers

  like Oracle and Salesforce.



- **Location Data Improvements:** With the October cube, location

  accuracy is also drastically improving. 1.2M new valid locations were

  added, and over 5.2M were removed based on automated and research

  acquisition and validation, focused on the Fortune 1000 companies and

  small businesses (\< 50 employees).



- **Core Data Enhancements:** Coverage of contacts with a supplemental

  email, a key driver in deanonymizing website visitors at the person

  level, increased by 11.1M (20%), another 17.5M emails were added to

  contacts who already had at least one (increasing resolution

  candidates). Coverage of contacts with a mobile phone also increased

  by 16.1M (16%), with a focus on high visibility European contacts. We

  onboarded our first European mobile enrichment partner, and saw over a

  30% increase in mobile coverage for Manager+ contacts in the UK,

  Germany, and France.



- **Local Location Data Improvements:** Increased accuracy of person

  location data improving parity with social media. Xverum was not

  contributing location data to our person pipelines resulting in

  outdated geographic details for contacts, disrupting geo based use

  cases (event invites and recruiting). Over 15M contacts have new

  location attributes that were previously NULL, and another 20M+ saw a

  change in values from what was published already.



- **Global Title Classification Improvements:** Developed an AI based

  title classification solution for non-English titles, resulting in

  classification of 23M non-US contacts. Evaluations with Cognism show

  we have parity on contact coverage of buying groups, but lack of

  classification results in filter based searches creating a parity gap.



### **Compliance, Privacy, and Legal Enablement**



Compliance leadership shifted from resolving blockages to enabling

faster product development:



- **Legal Breakthrough:** Preliminary legal approval for a blanket

  contributory network (CN) notice covering present and future product

  activities was secured. This eliminates the previous bottleneck of

  requiring individual approvals for each new CN-driven tool,

  accelerating development cycles.



- **Compliance Remediation:** Cookie banners were successfully restored

  across all 15+ domains, returning the organization to full regulatory

  compliance after previous setbacks.



- **Automated Compliance:** Automated CIPA compliance scanning via the

  Privado tool achieved 100% accuracy across tested customer websites,

  representing a scalable method for monitoring thousands of customer

  sites and protecting ZoomInfo from potential regulatory exposure.



- **Email Deliverability Asset:** Legal approval was obtained to expand

  usage of the 2 million full email signatures captured monthly from

  Chorus for email deliverability capabilities.



### **AI and Agentic Development**



Foundational work validated the potential for AI-driven data workflows:



- **Agent Coordination:** Multi-agent coordination testing demonstrated

  that current AI capabilities can handle complex data analysis

  workflows, showing promising early results for streamlined analysis

  workflows.



- **Semantic Signals:** Full signal generation automation was achieved

  for semantic-data-enhanced signals, with early Account Manager

  feedback indicating signals are substantially more relevant than

  previous iterations.



- **Contributory Network Insights:** The contributory network benchmark

  agent prototype revealed significant customer appetite for deal cycle

  insights based on aggregated opportunity data, which competitors

  cannot replicate.



## **Section 2a: Forward-Looking Challenges We Need to Solve**



To maintain momentum and unlock full product potential, several critical

architectural and organizational challenges must be addressed:



### **Vertical Dataset Scaling and Complexity**



- **Pipeline Management:** As the team scales from 3 to 10+ vertical

  datasets, there is increasing complexity in managing independent

  pipelines. Without architectural changes to Company 3.0, the current

  approach risks creating unsustainable technical debt as maintenance

  scales non-linearly.



- **GTM Readiness Gaps:** While training confirmed strong demand,

  follow-up questions highlighted the need for standardized messaging

  frameworks and self-service evaluation tools to scale the expanding

  dataset portfolio effectively. Data readiness for Form 5500 and other

  priority datasets requires accelerated development focus to meet field

  demand.



### **Agent Platform Deployment Uncertainty**



- **Infrastructure Blockers:** The path to customer deployment for both

  ZI Chat and the Agentic R&D platform remains unclear.

  BigQuery/Snowflake connectivity limitations currently block several

  high-impact agents. This lack of direct query access requires

  resolution to fully enable analysis workflow agents.



- **Authentication Bottlenecks:** The agentic platform infrastructure is

  currently misaligned with the \"move fast\" mandate, specifically

  citing a 2+ week permission cycle for routine data access due to

  Google IAP authentication requirements, creating compound delays

  across AI initiatives.



### **Core Data Asset and Organizational Gridlock**



- **Infrastructure Neglect:** Critical infrastructure systems, such as

  the CN Admin Panel, have been broken for months due to \"disparate

  ownership and maintenance\". This pattern of neglect creates compound

  reliability issues and requires explicit executive mandate for

  ownership and prioritization.



- **Cross-Functional Coordination:** Systematic challenges aligning

  legal, security, and engineering stakeholders around data initiatives

  consume disproportionate time relative to the technical complexity of

  the work. Establishing clearer decision-making processes is required

  to unlock team capacity.



- **Email Generation and Privacy Notifications:** More active management

  and collaboration across PTI, Deliverability, and Act-On teams are

  required to deliver notifications at scale. Email verification and

  delivery continues to get more challenging, we cannot rely on

  historical processes and technology to keep pace with the evolving

  landscape. This has resulted in the pausing of email generation

  (critical for competitive parity), and notification delivery (critical

  for publishing new European contacts).



## **Section 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters**



### **Vertical Dataset Scaling and Complexity**



- **Entity Integration Acceleration:** We are accelerating the

  integration of entities (contacts, companies, locations) sourced via

  Vertical Datasets into our core offering to simplify data management,

  further the ZI ID value prop, and leverage our core capabilities to

  acquire and enrich supplemental data on these entities from the web

  and third parties.



### **Core Data Asset**



- **Renewed Investment in Email Validation:** Development of a more

  intelligent email validation and queueing mechanism is required to

  maintain low bounce rates of privacy notices. Monthly testing shows

  deliverability of emails based on customer usage remains very high,

  but many customers make buying decisions based on coverage stats. We

  need to optimize for the long tails of contacts to compete for

  unsophisticated buyers.



- **GTM Enablement:** The GTM motion behind vertical datasets has

  resulted in more demos and excitement across the GTM org and our

  customers than our standard offerings have generated from a DaaS

  perspective in two years. We need to find capacity to take the same

  approach with our core offerings positioned to solve common GTM data

  problems. Our asset quality far exceeds current implementation

  sophistication across the base, there is a lot of untapped upside we

  can capture with more R&D led enablement, outreach, and positioning.



- **SMB Contact Coverage:** While new company creation from unmatched

  requests, high visibility sources, and vertical datasets is a

  positive, it opens the door to usability gaps when we do not have

  actionable contacts profiled at these businesses. In Q4 and beyond, we

  must revive and improve our leadership page crawler to close the

  coverage gaps with what appears on the web and what we profile in our

  database.



### **Organizational Gridlock**



- **Accelerated Procurement Process for Data Partners:** It currently

  takes 8 weeks minimum to acquire data from vendors. To compete with

  Clay's marketplace and to continue to improve our core, we need to

  significantly reduce this timeline. We are seeing momentum with the

  self-serve Identity Partner Program, we need to redefine the process

  to close data partnerships faster.



## **Section 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?**



1.  **Company Match Rate:** New company creation is having the desired

    impact on customer match rate.



![](media/image3.png){width="4.614583333333333in"

height="1.7916666666666667in"}



2.  **Qualitative Location Improvements:** Observed via human

    acquisition and corroboration with locations on company websites.

    While more anecdotal than qualitatively evaluated, we can now

    confidently say and show that our process is human verification or

    acquisition and corroboration directly from company sites for these

    segments.



![](media/image6.png){width="6.5in" height="1.7361111111111112in"}



*Note: A sizable portion of the to Add and to Remove overlap, awaiting

on pipeline to handle normalization and entity resolution.*



3.  **RO Actionable Response Rate (Matched Contacts with Contact Info)

    and Data ROI**: Recent mobile and supplemental increases are causing

    a resurgence, but we still need to fix business email generation and

    validation to return to all time highs on RO Actionable Response

    Rate. Data ROI has reached all time highs, with the primary driver

    being a larger impact observed by contributory network data

    integration compared with 3P contact integrations driving RO

    changes. Most 3P partners enrich off of LinkedIn URLs, Data

    ROI/Contributory network sources unlock non-LI based enrichment.\

    ![](media/image4.png){width="5.385416666666667in"

    height="1.4270833333333333in"}\

    ![](media/image5.png){width="5.364583333333333in"

    height="1.78125in"}



4.  **Key Buyer ID Signal Production:** Improvements by the platform

    team alongside supplemental email coverage expansion is producing

    consistent, high volumes of Key Buyer ID signals in Copilot.\

    *Daily Signal Volume in ZI Tenant\*

    ![](media/image1.png){width="6.5in" height="3.2083333333333335in"}



## **Section 4: Beginning vs. End Contrast Table \[July 2025 vs. September 2025\]**



The reporting period demonstrates a critical shift in the team\'s

operating environment, moving from foundational stabilization and

unblocking gridlock to maximizing revenue execution and scaling

validated capabilities.



Platform



# **QBR: Platform Team**



This Quarterly Business Review (QBR) covers the period of Q3 2025 (July

7 to September 19, 2025), summarizing the performance and strategic

trajectory of the integrated Platform, ZIM, Integrations, Automation,

and User-Provisioning teams.



## **Opening Context Paragraph**



Q3 2025 was defined by foundational technical breakthroughs across

Identity Resolution, GTM Data Model infrastructure, and Agentic Platform

readiness, successfully positioning the platform for key Q4 feature

launches including Copilot V2 and GTM Studio. Significant advancements

include a 100% improvement in visitor resolution rates and the

deployment of the internal GraphQL Query API v1, though critical

dependencies persist around cross-functional UI/UX resource allocation

and the need for executive resolution on technical debt migration

(specifically the MCP Gateway and costly legacy data deletion processes)

to unlock the next level of scalable, monetizable platform capabilities.

The team demonstrated strong commitment to meeting aggressive

monetization deadlines, including establishing the hard October 1st AI

Action Credit charging deadline.



## **Section 1: Progress and Momentum Areas**



The team delivered quantified achievements across five major strategic

themes, establishing critical foundations for revenue acceleration and

enhanced technical capabilities.



### **Identity Resolution, Intent, and Advertising Momentum**



The ZIM team delivered world-class B2B identity graph performance and

established clear, scalable paths for advanced targeting capabilities.



- **Visitor Resolution Breakthrough:** Brett Elliot successfully

  deployed person-first logic in the VRS, achieving a 100% improvement

  in visitor resolution rate (VRR). This transformational achievement

  now identifies nearly 2% of all page visitors at the individual

  contact level, representing a significant competitive advantage over

  company-level identification offered by competitors.



- **Revenue Baseline Validation:** Aadhitthyaa Hari Gopal\'s post-pay

  automation initiative achieved immediate market validation,

  maintaining an established \$1M monthly ad spend baseline. A key

  customer (BizLibrary) demonstrated a 20% month-over-month ad spend

  increase in July based on this optimization.



- **Massive AI Efficiency Gain:** Aadhitthyaa Hari Gopal transitioned

  the Account Brief pipeline from custom models to off-the-shelf LLMs,

  resulting in a 25x efficiency improvement in generating comprehensive

  customer intelligence briefs. This enables scalable delivery of

  intelligence across the Copilot platform.



- **Contact Targeting and Intent Deployment:** Brett Elliot achieved

  production deployment of contact targeting campaigns with live bidding

  and impression delivery confirmed. Furthermore, person-level intent

  production deployment now delivers 180 million daily signals to

  ZoomInfo.



- **Intent Volume Recovery:** Shuxin Yang successfully deployed 25%

  intent signal augmentation to production through coordinated

  cross-timezone execution, directly addressing volume decay that was

  affecting key DaaS clients such as Ziff Davis and Deloitte.



### **AI/Agentic Platform and Automation Foundation**



Core infrastructure for agentic tools and workflow orchestration reached

critical milestones, positioning the platform for the forthcoming

Copilot V2 launch.



- **Critical Authentication Resolution:** Adam Peretz developed a proxy

  server solution that resolved the critical MCP authentication

  challenge, enabling most, or potentially all, OAuth login methods

  necessary for enterprise Single Sign-On (SSO) adoption by agentic

  tools. This breakthrough created a viable path forward for the

  high-pressure board demonstration timeline.



- **Agentic Platform Viability:** Jesse Miller successfully migrated the

  AdOps agent from a prototype to the ZI Agentic Platform repository,

  demonstrating 90% code portability and strong architectural alignment.

  ZIM Agent implementation is now advanced, targeting an internal MVP

  delivery by October 15th.



- **Strategic Pivot for Accelerated Value:** Marc Frail successfully led

  the strategic realignment from GTM Plays creation to Workbook-Workflow

  activation. This approach maintains momentum by leveraging existing

  capabilities (Workbooks) to unlock immediate customer value faster

  than building net-new GTM Plays features.



- **Developer Experience Improvement:** Adam Peretz launched the ReadMe

  documentation portal, which received overwhelmingly positive customer

  feedback and directly addressed previous documentation gaps that had

  hampered API adoption.



### **GTM Data Model and Core Infrastructure Maturation**



The Data Platform and Integrations teams stabilized and scaled

foundational data layers essential for cross-product consumption and

agent readiness.



- **GraphQL Query API Launch:** Linda Johannessen successfully released

  the GraphQL Query API v1 (internal), delivering the first stable,

  agent-ready interface for cross-entity GTM data. This architectural

  achievement was immediately validated by agentic platforms already

  testing MCP integration on top of the API.



- **Engagement Data Pipeline Completion:** Sanyog Rai successfully

  onboarded Email ingestion for all Google/Outlook tenants and Calendar

  data for 1,000 Google tenants into the GTM Data Model. This

  foundational infrastructure is essential for downstream applications

  like the Copilot V2 Workspace chatbot, which demonstrated organic

  adoption by sourcing meeting information via GraphQL queries.



- **GTM Config Milestone Lock:** Aadhitthyaa Hari Gopal achieved 100%

  completion on GTM Configuration requirements definition, establishing

  a November 18th customer release target and an October 18th code

  complete deadline. This architecture streamlines data engineering

  execution by consolidating 10-12 datasets into Postgres.



- **External API Commitment Secured:** Linda Johannessen obtained

  commitment from the External API team to support the end-of-November

  externalization of the Query API, removing a critical execution risk

  associated with GraphQL support timelines.



- **Improved Communication Cadence:** Marc Delurgio established the

  inaugural GTM Data Platform Monthly Review, which was enthusiastically

  received by stakeholders and addresses past communication gaps by

  establishing a predictable milestone cadence.



### **Monetization and Strategic Partner Ecosystem Enablement**



The team delivered the critical infrastructure necessary to monetize AI

features and accelerate scalable partner integration capabilities.



- **AI Monetization Infrastructure Finalized:** Brannen Huske secured

  NPI approval and alignment for AI Credits. The team made the decision

  to consolidate the AI Pricebook and AI Credit Service into a single,

  centralized service, simplifying the design for accurate job-level

  tracking and reporting. This positions the platform to meet the hard

  October 1st deadline for AI charging.



- **Customer Retention Success:** Erica Fienman\'s CRM Import Rules

  feature (behind a feature flag) directly prevented a potential

  Apollo-churn risk from Zoom after their previous integration failed,

  demonstrating immediate business value.



- **Agentforce Readiness for Dreamforce:** Prateek Paikray completed

  Agentforce V2 requirements and successfully passed the ZI package

  through security review in a record time of two weeks. Enterprise

  customer beta outreach was initiated with accounts including ADP and

  Salesforce, positioning the team for a strong October market launch.



- **Marketplace Development:** Prateek Paikray delivered the vertical

  dataset preview functionality for the GTM Studio internal marketplace

  (using mock data), setting the stage for the backend API integration

  necessary for the October launch timeline.



- **Legacy Migration Unblocked:** Erica Fienman deployed Conditional

  Importing and Custom GTM DM fields. These features collectively solve

  the Advanced Search requirements that were blocking the migration of

  over a thousand ZI tenants from the legacy import pipeline, which will

  improve the Northstar \"Active Integrations\" metric.



## **Section 2a: Forward-Looking Challenges We Need to Solve**



These systemic issues require executive attention and resource

allocation decisions to unlock scalability and accelerate platform

adoption across the organization.



### **Scaling Challenges (Architecture for Scale)**



To move beyond rapid prototyping and ensure platform longevity, we must

address accumulated technical debt and emerging complexity.



- **MCP Gateway Technical Debt Migration:** Adam Peretz revealed that

  the current MCP implementation used API gateway shortcuts to

  accelerate the initial launch. The team must now develop and migrate

  existing agentic tools to the official MCP gateway infrastructure

  before other internal teams can begin publishing their own agents,

  otherwise scalability will be limited.



- **Legacy Data Deletion Cost:** Legacy systems, such as the 3 petabyte

  Chorus raw table, currently make compliance-driven tenant data

  deletion operations extremely costly, estimated at \$20,000 per run.

  This creates a massive compliance and cost-management risk that

  requires executive prioritization for dropping unused legacy tables

  and automating data lifecycle management.



- **AI Credit Granularity for Copilot V2:** The strategic requirements

  for AI Credits are evolving to be application-specific and user-level

  to support advanced Copilot V2 features. This complex evolution

  requires building a strategic roadmap that includes features like

  charge caps on specific actions and user limits.



### **Resource/Organizational Bottlenecks**



Constraints on specialized resources and cultural dependencies are

limiting velocity and creating execution pressure in critical areas.



- **UI/UX Design Capacity Constraints:** Limited capacity in UI

  engineering and design resources is a consistent bottleneck. Matt

  Barnes identified design resource gaps affecting Bot UI

  implementation, and Sam Massie noted UX/UI bottlenecks delaying

  finalization of the action library framework. These constraints risk

  delaying the delivery of necessary front-end components for

  September/October feature releases.



- **Cultural Dependency on \"LoginAs\" Feature:** Josh Simon\'s

  discovery revealed that \"LoginAs\" has become an ingrained \"crutch\"

  used by most internal organizations, including CX, CSM, and

  Operations, for essential job functions. The required Audit Service

  and retirement of \"LoginAs\" will necessitate significant

  organizational and cultural management, including retraining of these

  departments, beyond just a technical solution.



### **Infrastructure Gaps and Cross-Functional Coordination**



Unresolved architectural decisions and external team dependencies are

threatening November and Q4 delivery timelines.



- **External API GraphQL Dependency:** The External API team currently

  supports REST-only, which limits the planned externalization strategy

  for the Unified Query API. Linda Johannessen secured commitment for a

  November external release, but detailed scope definition is pending

  until October due to external team capacity constraints. Executive

  alignment is critical to resolve the architectural conflict between

  federated search and GTM Store lookups to prevent implementation

  delays.



- **Cross-Timezone Coordination Friction:** Sanyog Rai and other

  engineers continue to experience a recurring pattern where

  coordination issues between West Coast, Israel, and other timezones

  cause cascading delays, sometimes extending issue resolution that

  should take hours to 4+ days. This requires establishing clear

  executive mandates for asynchronous collaboration processes.



- **Agentforce API Access Limits:** Prateek Paikray noted that the

  initial Agentforce V2 integration will be limited because internal

  APIs for key features, like Copilot signals, have not yet been

  published to the Enterprise API Gateway by the respective apps

  engineering teams. This cross-team dependency directly impacts

  Agentforce\'s customer value demonstration ahead of the October launch

  window.



- **AI Price Book Reporting Definition Blockage:** The final technical

  design and implementation of the AI Pricebook---a requirement for the

  October 1st charging deadline---is currently blocked because clear

  reporting must-haves for General Availability (GA) have not been

  defined by the Agentic Platform and Workbook teams.



## **Section 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters**



\[Placeholder\]



## **Section 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?**



\[Also include what success looks like next quarter \]



## **Section 4: Beginning vs. End Contrast Table \[July 2025 vs. September 2025\]**



This table compares the state of key operational areas at the start of

the QBR period (Week of July 7, 2025) versus the end (Week of September

15, 2025), demonstrating concrete progress toward platform maturity.



Intelligence



# **Quarterly Business Review (QBR)**



[[Adam Smith]{.underline}](mailto:adam.smith@zoominfo.com)



## **Intelligence Team --- Q3 2025**



The Intelligence team achieved production readiness of the Agentic AI

platform with 2 agents live in production, validated our platform

investment hypothesis with 8+ teams building agents, and reduced agent

development time from weeks to 24 hours. The team deployed a reusable

chat framework across Studio, Copilot Workspace, SalesOS and Chorus. We

launched our external MCP in Anthropic\'s directory with 50 GTM reps

enabled for Dreamforce demonstrations, and delivered Top Contacts with

50x capacity increase and 75% latency reduction.



Sustaining this momentum into 2026 will require executive alignment to

address dependencies. Specifically, we need PM headcount allocation for

Intelligence layer roadmap, and PMM resourcing under Derek Osgood to

build systematic last-mile delivery infrastructure from technically

ready to customer sellable. I also believe we should make an

organizational commitment to quality-over-velocity tradeoffs. This is

not a push to slow down but rather for conscious prioritization, drive

to completion and to a high standard before switching. Do less, do it

better, focus on the high leverage stuff.



**SECTION 1: Progress and Momentum Areas**



### **I. Production Agentic Platform & Team Enablement**



The platform investment enabled distributed team success across ZoomInfo

products this quarter. Lars Vedo\'s team shipped the production-ready

agentic platform including AI Action credits, multi-model support across

Anthropic, OpenAI, and Vertex AI, entitlements, agent-to-agent

communication MVP, MCP integrations, embeddable chat framework, and API

access. This infrastructure delivered immediate value as 8+ teams built

agents including SalesOS, Chorus, Workbooks, Copilot Workspace, Web

Search, Advanced Search, Marketing, and Research. Teams can now embed

chat frameworks and connect agents within 24 hours compared to the weeks

previously required.



Two agents reached production deployment this quarter. Lars Vedo and

Sean Walter launched Copilot Workspace on October 6th to internal

testing with approximately 1,000 sellers. The Chorus agent went live in

production, validating that the platform could support multiple products

simultaneously. This work now guides all teams building on the platform.



The SDK reduced the barrier for teams to build AI capabilities. Ryan

Stevens and the engineering team enabled teams to integrate agents

without requiring deep understanding of the underlying orchestration

complexity. The development velocity improvement from weeks to 24 hours

represents a fundamental shift in how quickly ZoomInfo can deploy new AI

features to customers.



### **II. Copilot Workspace---Zero to Production in One Quarter**



Sean Walter and Lars Vedo (not solely, but within my team) drove Copilot

Workspace from concept to customer-ready product in a single quarter.

The internal beta program with approximately 1,000 sellers provided

real-world feedback.



Ryan Stevens integrated the AI Action Credits system into the agent

runtime, enabling consumption-based billing and usage tracking. The

Platform team delivered the credits infrastructure and pricing

integration. Multi-model orchestration became operational across

Anthropic, OpenAI, and Vertex AI, giving the product resilience against

any single vendor\'s availability issues.



AI credits is a win for cross-functional collaboration (product,

platform, GTM). Working with Mark Harris in revenue, we aligned the

commercial model that now powers consumption-based billing across all

Intelligence products, including Workspace, Studio. This foundational

mechanism enables the business model shift we need for AI.



Ryan McMaster created a design system that enables consistent AI

experiences across GTM Copilot, Studio, and Workspace. This eliminated

duplicate UI development work and established patterns that other teams

now follow. The team resolved context compaction for messages exceeding

300K tokens, reduced P99 latency through Vertex enablement, and

implemented a demo mode toggle that allows sales demonstrations with

redacted data.



### **III. Context Engineering & External AI Positioning**



Danny Pan and Rowan Bailey processed semantic data for 18 Early Access

customers now live in production powering Workbooks. The team reduced

processing costs to approximately 18 cents per call transcript and 8-9

cents per email thread through batch processing optimization and

migration to Gemini Flash 2.5. Both represent substantial cost

reductions that make large-scale tenant onboarding economically viable.



Rowan Bailey shipped ZoomInfo\'s MCP to Anthropic\'s public directory

and enabled 50 GTM reps for Dreamforce demonstrations. The reps used

search and enrich capabilities directly in Claude desktop applications,

validating the portable intelligence strategy. The team established an

internal-to-external promotion path for tools using feature flags,

allowing selective access to capabilities before broad customer release.



The semantic data integration into GTM Studio for workbook creation

reached near completion this quarter. The remaining work is blocked by

GTM Studio team resourcing rather than Intelligence dependencies. This

integration will allow customers to query conversation intelligence as a

dataset alongside traditional ZoomInfo data. The team implemented

ReAct-based retrieval agents, improved knowledge graph quality through

duplicate entity prevention, and expanded the GTM Ontology to support

more sophisticated queries.



Carlos Nunez and Rowan Bailey demonstrated successful enrichment of

product offerings data using Google grounding. The team processed 10,000

companies for under \$100 in 30 minutes using BigQuery ML with Gemini

Flash 2.5. This experiment opened possibilities for competitor

relationship mapping, complementary technology identification, and

improved core company data.



### **IV. Predictive Intelligence & Model Performance**



Robyn Sablosky delivered transformation of the Top Contacts model this

quarter. The team achieved 50x capacity increase while reducing P99

latency from 4 seconds to 1 second, representing 75% latency

improvement. The production pipeline stabilized to support multi-hour

runs without performance degradation. This infrastructure can now

support scaled customer deployments without capacity constraints.



The team validated Lookalike Accounts covering 100K companies through

proof of concept work. Lookalike Contacts and the full production

version moved into Q4 roadmap planning. Srivatsa Marthi and the data

science team demonstrated a Momentum Score proof of concept that

predicts deal progression using engagement velocity, stakeholder count,

and interaction medium. The team is now exploring whether semantic data

integration can show that conversational topics predict outcomes more

accurately than interaction frequency alone.



After completing the architectural design for the GSO to GTM Store

connector, Srivatsa Marthi refocused his team on new signal development.

The work includes down-funnel signals, signals based on absence of

events, and contributory network-based signals. These areas align with

the emerging Pulses roadmap concept and had received limited attention

in recent months.



**SECTION 2a: Forward-Looking Challenges We Need to Solve to Unlock the

Next Level**



### **1. Resource and Organizational Bottlenecks**



**Specialized AI Talent Constraint**



The team faces a shortage of engineers capable of solving specialized AI

problems. These problems include agent architecture, evaluation

frameworks, agent decomposition, state management, and agent-to-agent

communication. Only a handful of engineers can work through these

problems end-to-end. Josh Mantovandi exemplifies this constraint. He

moved sequentially across web research agent development to agent

re-architecture for latency reduction to context retrieval optimization

because few others could solve any of these problems completely.



This constraint forces the roadmap to execute in shallow mode rather

than excellent mode. All initiatives progress but few reach

production-quality polish. The quality gaps now surfacing in Copilot

Workspace user feedback trace directly to this velocity-over-excellence

dynamic. When specialized engineers spread across too many problems,

each solution reaches good enough rather than excellent.



The organization has more capable engineers than currently recognized,

but they need systematic enablement. This includes agent SDK training

from Lars Vedo and Ryan Stevens\' team, publishing standards and best

practices from Derek Osgood\'s team, and foundational AI training like

Anthropic\'s agent design pattern curriculum. Investment in systematic

upskilling multiplies the effective engineering capacity for AI-specific

challenges. Without resolution, the team will continue delivering good

enough implementations with a few engineers rather than excellent

products, and user satisfaction and competitive differentiation will

suffer.



**Last Mile Delivery Gap---From Technically Ready to Customer Sellable**



Multiple agents reach technically ready state but lack a systematic path

to production deployment. Technical readiness does not equal production

readiness. The gap includes go-to-market positioning and messaging,

product marketing materials, pricing model integration and credit system

documentation, customer enablement materials, publishing workflows to

move internal tools to customer-facing features, schema documentation

and versioning, and agent or tool marketplace infrastructure.



Eight teams built agents this quarter but only two reached production.

This represents massive sunk engineering cost with no revenue

realization from the remaining six. Engineering delivers technical

capabilities that sit unused because GTM infrastructure does not exist

to bring them to market. Derek Osgood\'s entire Q4 scope addresses this

challenge through the Unified AI Service Registry, Internal Tooling and

Publishing Admin Panel, and Play Library templates. This shows the

organization is treating the challenge seriously, but it requires

dedicated PMM and GTM resourcing under Derek to systematize the

last-mile delivery infrastructure and consultative agent marketplace

model.



### **2. Scaling Challenges for Architecture**



**Context Quality vs. Context Quantity**



The team discovered through production experience that more context

degrades LLM performance, contrary to initial assumptions. Precision in

information provided is critical. Irrelevant information distracts LLMs,

increasing both error rates and inference costs. Overstuffed agent

context causes measurable performance degradation in production

deployments.



This learning directly informs the Base Context Acquisition Pipelines

initiative in the Q4 roadmap. The focus is achieving context parity with

market leaders like Google and Claude rather than context volume. Rowan

Bailey\'s Q4 work addresses this through context engineering discipline,

systematic context pruning, and retrieval strategy optimization.



## **SECTION 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters**



The Q4 2025 roadmap is locked in and underway across three workstreams.

Derek Osgood owns AI Orchestration including the transition of DoubleO

to Plays, the Unified AI Service Registry, and publishing tooling. Lars

Vedo owns Applied AI including SDK and Runtime v1, Essential Shared

Agents, Embeddable UI Foundation, and Basic Testing Infrastructure.

Rowan Bailey owns Context Engineering including context acquisition

pipelines, External MCP Gateway, event-driven architecture, Memory

Service, Momentum Score, and Custom Signals.



The last-mile delivery gap is directly addressed by Derek\'s entire AI

Orchestration scope. The Unified AI Service Registry creates a

centralized framework for building agentic and non-agentic actions. The

Internal Tooling and Publishing Admin Panel exposes action publishing

tools as an internal admin panel for deploying workflows, agents, and

tools into existing products through a no-code interface. The Play

Library provides ten published templates as a starting point. This work

systematizes the path from technically ready to customer sellable. The

challenge was anticipated and is being addressed..



The specialized AI talent constraint affects execution quality for SDK

and Runtime v1, Essential Shared Agents, and Basic Testing

Infrastructure. Roadmap progress depends on resolving the talent and

upskilling gap through executive action on headcount and training

investment. Without this, deliverables will reach adequate state rather

than excellent state.



The context quality versus quantity challenge is incorporated into

roadmap priorities. The External MCP Gateway launching mid-November and

the context pipeline work directly address this learning. The team

shifted strategy based on production experience.



Design resource fragmentation affects multiple Q4 initiatives. The

Embeddable UI Foundation, Plays UX, and Memory Service interfaces all

require Ryan McMaster\'s design support. His bandwidth is stretched

across multiple workstreams. This may require prioritization decisions

or additional design resources to maintain quality standards.



Several initiatives remain on track despite challenges. The External MCP

Gateway is proceeding on schedule toward mid-November launch with 50

reps already enabled for Dreamforce validation. Copilot Workspace

adoption continues after the successful October 6th launch with

infrastructure complete for customer expansion. The DoubleO to Plays

transition benefits from Derek\'s systematic approach to publishing

infrastructure, which addresses the root cause of past deployment

friction.



The roadmap should accelerate engineering upskilling by front-loading AI

fundamentals training in Q4 to expand the talent pool for specialized

problems. The team should prioritize Ryan McMaster\'s design focus by

identifying which of Embeddable UI, Plays UX, or Memory Service delivers

highest impact for Q4 customer adoption. The organization should monitor

talent constraint impact closely, and if SDK and Runtime v1 or Essential

Shared Agents slip, escalate immediately for additional specialized

engineering resources.



## **SECTION 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?**



### **Part A: Key Performance Indicators**



**Platform Adoption & Velocity**



Agent teams enabled increased from zero to 8+ this quarter. The platform

investment hypothesis was validated as teams built independently with

minimal support. The target is to continue enabling product teams as the

SDK matures. Production agents increased from zero to two with Copilot

Workspace and Chorus now live. The target is 5+ agents in production by

end of Q4 as Derek Osgood\'s publishing infrastructure work closes the

gap from technically ready to customer sellable.



Development velocity improved from weeks to 24 hours for agent

embedding. This enables rapid experimentation and reduces time-to-market

for new AI capabilities. Teams can now test ideas in production quickly

rather than spending weeks on infrastructure setup.



**Performance & Reliability**



Top Contacts latency decreased from 4 seconds to 1 second P99,

representing 75% reduction. Top Contacts capacity increased 50x versus

baseline. These improvements unlock scaled customer deployment without

infrastructure constraints. The system can now handle production load

that would have crashed the previous architecture.



Semantic data processing costs dropped to approximately 18 cents per

call transcript and 8-9 cents per email thread through batch processing

optimization and Gemini Flash 2.5 adoption. These reductions make

large-scale tenant onboarding economically viable where previous costs

blocked expansion.



**External Adoption & Reach**



MCP reps enabled reached 50 for Dreamforce demonstrations. The target is

20 customers live on MCP gateway by Q1 2026. This represents first

external validation of the portable intelligence strategy and enables

the shift from license-based to consumption-based revenue model.



Semantic data customers reached 18 Early Access customers processed and

live in Workbooks. The target is 250 tenants onboarded with event-driven

processing by end of Q4. Event-driven architecture will process call

transcripts and emails immediately after meetings end or emails send,

providing near-real-time conversation intelligence.



**AI Credits & Consumption**



The credits system framework is defined and integrated into Copilot

Workspace and the agent platform. This enables consumption-based pricing

for all Intelligence products going forward. Volume metrics

infrastructure is being established to track usage patterns and optimize

pricing models.



### **Part B: Customer Behavior Impact**



**Copilot Workspace Adoption**



Approximately 1,000 internal sellers engaged in pre-launch testing

before the November 3rd customer launch. The infrastructure now supports

cross-account analysis, semantic data queries, and multi-format artifact

creation including emails, documents, and buyer engagement maps. Sales

reps now delegate research tasks to AI rather than manually compiling

account intelligence. This represents a workflow shift from active

research to task delegation.



**MCP External Intelligence**



Fifty GTM reps use ZoomInfo intelligence directly in Claude and ChatGPT

desktop applications. The consumption pattern shifted from logging into

the ZoomInfo app to accessing ZoomInfo data wherever work happens. The

Dreamforce validation demonstrated the portable GTM intelligence model

in real-world scenarios with actual customer conversations.



**Semantic Data Integration**



GTM Studio workbook creation from semantic data source is nearly

complete, blocked by GTM Studio resourcing rather than Intelligence

dependencies. When shipped, conversation intelligence becomes a

queryable dataset for custom analysis alongside traditional ZoomInfo

data. This enables customers to build their own views into what their

teams are discussing with prospects and customers.



### **Part C: What Success Looks Like Next Quarter**



**Adoption Targets**



GTM Studio adoption should reach 100 customers live on platform. Play

builders should reach 20 customers actively building custom Plays. Play

templates should include 10 published templates providing instant

time-to-value. MCP customers should establish a path to 20 customers

live on MCP gateway with Q1 2026 as the target, starting foundation work

in Q4.



**Technical Milestones**



Semantic data scale should reach 250 tenants onboarded with event-driven

processing where calls and emails process immediately. Memory Service

should serve all Copilot Workspace users for personalized AI

interactions. Momentum Score should go live in production, enabling

opportunity-level recommendations beyond the APS prospecting focus.



**Quality Indicators**



Context parity should be achieved where base context acquisition

pipelines deliver equivalent quality to Google and Claude for account

and contact research. Testing infrastructure should enable less than one

day turnaround time to evaluate new models or major agent adjustments as

an internal metric. Embeddable UI should provide consistent chat

experience deployed across all ZoomInfo products.



**Enablement**



Play Library should include 10 templates demonstrating high-value

automation workflows. Publishing infrastructure should enable internal

teams to deploy new AI functionality via no-code admin panel. Credit

consumption should establish baseline consumption metrics for

forecasting and pricing optimization.



**SECTION 4: Beginning vs. End Contrast Table \[July vs. October\]**



Product Ops and Analytics



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



- **Personalized Account-Based Sales Agents:** Multiple **personalized

  account-based agents** were shipped to provide sales representatives

  with custom documents for client interactions, directly addressing

  massive time sinks for Account Managers. This included:



  - **Comprehensive GTM Talk Track Agents:** Copilot Workspace and GTM

    Studio talk tracks and Q&A documentation were delivered in

    collaboration with product, sales, and marketing leadership and

    converted into **account-customized agents**. This agentic

    foundation is crucial for arming sellers with the right messaging

    for Tier 1 products and impacting critical Q4 renewals.



  - **account-specific roadmaps and release notes agents** delivered as

    part of the Monthly Customer Release (MCR)



  - **AM slide generator** was tested as a working text prototype that

    aims to reclaim significant time for AMs by creating customized

    **meeting prep decks**.



- 



- **Foundational Cross-Product Marketing Content Engine:** The **AI

  Product Marketing Management (PMM) engine** generates on brand, a wide

  range of marketing assets that are consistently on-brand.



- **Strategic Enablement Infrastructure and Distribution:** The core

  sales enablement platform was enhanced with agent capabilities and

  clear distribution channels. The **discovery bot** was finalized and

  successfully made **product-agnostic** after extensive testing and

  prompt refinement, allowing it to recommend appropriate products based

  on sales discovery responses. Concurrently, the **customer-facing

  roadmap was finalized**, and enablement distribution channels were

  established through CSM Learn to Sell, the monthly product release all

  hands, newsletters, and Slack channels.



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



- 



- **Knowledge Graph Foundation:** The Knowledge Graph met prototype was

  deployed in a dedicated GCP sandbox environment, initially focused on

  GTM Studio. The KG successfully processed **over 100 documents** from

  the AI marketing engine knowledge base, creating a foundation of

  atomic notes, concepts, and relationship mapping.



- .



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



- **VoC Tool** **Deployment Unblocked:** Major blockers for the **Voice

  of Customer (VoC) tool deployment** were eliminated by pivoting to the

  semantic data team\'s existing **agentic platform**, and deploying via

  MCP in the ZI Chatbot



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



# 



# *V1 draft below (disregard)*



# **~~Quarterly Business Review (QBR): Ops and Analytics~~**



## **~~Opening Context Paragraph~~**



~~This quarter has been defined by a strategic pivot toward accelerating

AI-driven adoption and achieving clarity on foundational account health

measurement. Significant advancements include implementing the Amplitude

Profiles feature to unlock historical user data and achieving a

breakthrough in retention analytics by discovering predictable

behavioral signals near contract renewal. However, based on learnings

from the difficulty in getting alignment with GTM leadership on how to

measure and report on account health (during onboarding and

post-onboarding) for Copilot (1.0) accounts, executive intervention may

be needed to align on key health and reporting metrics for Workspace and

Studio. In addition, BI has been slowly significantly reporting and

analyzing emerging usage in Workspace and Studio due to pervasive

instrumentation gaps and bugs. BI is driving an effort to standardize

taxonomy of all events in Workspace and Studio, and implement event and

property guidelines for eng teams (as they are data producers).~~



## **~~Section 1: Progress and Momentum Areas~~**



### **~~Strategic Theme 1: Copilot Workspace Adoption and Launch Readiness~~**



~~The team shifted its analytical focus to solving the largest drop-off

in the Copilot funnel: user provisioning versus activation. This

strategic prioritization, combined with strong readiness for Copilot

Workspace launch, positions the business to capitalize on its core AI

investment.~~



- ~~**Quantified Adoption Opportunity:** Phoebe Mei delivered a

  comprehensive Copilot Analytics Roadmap identifying that only 34% of

  95,000 provisioned users are active, representing a 66% drop-off. Her

  analysis showed that an improvement of just 10 percentage points (pp)

  in this rate could unlock approximately 9,500 additional active

  users.~~



- ~~**AI Feature Engagement Validation:** Inbal Kor\'s analysis

  confirmed that AI feature usage is strongly correlated with customer

  stickiness. AI users demonstrated 4.5x more active days compared to

  non-AI users. Furthermore, renewal accounts are 22% more likely to

  adopt AI features within Copilot Enterprise (66% adoption vs. 54% in

  new accounts).~~



- ~~**Workbook AI Market Validation:** Early insights into external

  entitled users (across 15 companies) showed strong AI adoption among

  sheet creators, with 72% of creators using AI and 56% of created

  sheets including AI features. This active base consumed 2.8K credits

  in a sample period, confirming meaningful engagement and validating

  the product-market fit for cell-level AI functionality.~~



- ~~**Copilot V2 Launch Framework Delivered:** Phoebe Mei achieved 100%

  completion on developing an end-to-end funnel framework for the

  Copilot Pro launch. This scalable template defined measurable stages

  (e.g., Search → Generate AI Email → Send Email) with clear KPIs and

  success metrics for day-one reporting.~~



### **~~Strategic Theme 2: Account Health, Renewal Strategy, and Retention Insights~~**



~~The team advanced account health reporting by pivoting away from the

stalled continuous scoring debate and delivering a major breakthrough in

predictive retention analytics.~~



- ~~**Strategic Pivot to Actionable Reporting:** AJ Belen achieved

  alignment with Dominik and Victor to pivot account health reporting

  away from the contested continuous score model. The immediate focus

  shifted to delivering Renewal Prediction Score (RPS) analysis for the

  September through December expiry cohort for the upcoming October 18th

  ELT meeting. This pragmatic approach provides immediate executive

  visibility into high-risk accounts.~~



- ~~**Retention Breakthrough: Early Behavioral Signals:** Nanxi Ge\'s

  retention analysis challenged core organizational assumptions by

  revealing that customer usage patterns increase toward the end of the

  contract, rather than declining. Critically, renewal customers showed

  a significantly higher adoption spike near contract end compared to

  churn customers, providing actionable intelligence for re-timing

  Customer Success interventions.~~



- ~~**Quantified Renewal Account Uplift:** Analysis demonstrated a

  significant engagement gap between renewed and new accounts. Renewal

  accounts exhibit 60% higher Weekly Active Users (WAU) and take 22%

  more actions per user compared to new accounts. Furthermore, they are

  10pp more likely to be connected to CRM (75% vs. 65%) and 9pp more

  likely to have connected more than one CRM integration (46% vs.

  37%).~~



### **~~Strategic Theme 3: Foundational Infrastructure and Technical Capabilities~~**



~~Key infrastructure milestones were achieved, resolving long-standing

technical blockers that previously hampered deep user behavior analysis

and internal tool deployment.~~



- ~~**Historical Attribute Enrichment Unlocked (Amplitude Profiles):**

  Preetham Srinithi successfully implemented the Amplitude Profiles

  feature with Change Data Capture (CDC) enabled tables. This

  breakthrough resolves a critical capability gap by enabling

  retroactive enrichment of historical events with critical user and

  account attributes (e.g., Segment, Persona, CRM Connected status),

  empowering PMs to run actionable retention analyses and uncover \"Aha

  moments\" across the full customer lifecycle.~~



- ~~**Internal Tools Deployment Bottleneck Eliminated (Microapps):** Sam

  Darcy established a clear path for internal AI tool deployment by

  connecting the semantic data backend to ZI Chat via microapps. This

  architecture solves persistent deployment errors, networking issues,

  and months of delay, creating a scalable platform for future agentic

  application deployment, including the Voice of Customer (VoC) tool.~~



- ~~**Target Account Analysis Deepened:** Ferrell Tanuwidjaja completed

  deep-dive analysis on Target Account (TA) usage, finding that while

  Enterprise accounts utilize TAs, SMB and Mid-Market segments comprise

  the bulk of accounts with TAs set up. This work refined the TA funnel

  (Adoption \> Setup \> Hits) and identified user-level usage patterns

  to optimize Copilot adoption.~~



- ~~**Process Efficiency Gains (Tableau & Integrations):** Ferrell

  identified 250+ unused dashboards and data sources on Tableau Server.

  This cleanup effort improves performance, reduces storage costs, and

  simplifies stakeholder access. Nanxi Ge also successfully aligned

  stakeholders on request prioritization, including API usage analysis,

  without pushback, leading to more focused resource allocation.~~



### **~~Strategic Theme 4: Product Operations and GTM Automation Efficiency~~**



~~The Product Operations team transitioned from process definition to

automated delivery, significantly reducing manual overhead for Product

Managers and GTM teams.~~



- ~~**Quantified PM Productivity Improvement:** Daniel Kong successfully

  automated the knowledge center refresh process and streamlined the PM

  feature info pack process through AI optimization. This reduced the

  time required for PM documentation from 60+ minutes to approximately

  30 minutes, representing a 50% productivity gain in a high-frequency

  workflow.~~



- ~~**MCR Process Maturation and Stability:** Kristin Gandini stabilized

  the Monthly Customer Release (MCR) process and delivered significant

  improvements, including better transparency, clarified requirements,

  and streamlined documentation needs (e.g., replacing complex GIFs with

  simple screenshots). This marked the second consecutive smooth monthly

  release cycle.~~



- ~~**H2 T2 Milestone Risk Mitigation:** Caleb Munson achieved critical

  sign-off from all Domain Accountable Individuals (DAIs) on H2 T2

  project milestones for GTM Studio and Copilot. This alignment process

  uncovered and mitigated substantial misalignment and material risk in

  current execution plans, preventing significant downstream execution

  problems.~~



- ~~**CX Visibility Tool Unblocked:** Kristin Gandini secured a

  commitment from Jack\'s ZI Chatbot team to integrate LaunchDarkly data

  into the October roadmap. This crucial step will provide Customer

  Experience (CX) teams with visibility into which customers are

  impacted by specific beta features, addressing a longstanding

  operational blind spot.~~



## **~~Section 2a: Forward-Looking Challenges We Need to Solve to Unlock the Next Level~~**



~~The following systemic issues require executive attention to unlock

the next level of scaling, operational efficiency, and platform

capability.~~



### **~~Scaling Challenges: Ensuring V2 Analytics are Operational at Scale~~**



~~The primary scaling challenge is ensuring that data generated by the

new Copilot V2/Workspace and GTM Studio can be reliably tracked and

operationalized for external rollout.~~



- ~~**P0 Instrumentation Bug in Copilot Workspace (V2):** Despite the

  internal launch, a P0 instrumentation bug is blocking the capture of

  user IDs in Amplitude for several events, including key Workspace chat

  events (one of three core value pillars identified by Victor). This

  technical failure means we cannot currently tie AI chat engagement

  back to specific user cohorts or reliably measure daily utilization

  and time-to-value for the second batch of 100 internal sellers.

  Resolution requires immediate engineering leadership prioritization

  (Lars) to prevent corrupted data from scaling into the external launch

  planned for October.~~



- ~~**Low Conversion and Utilization Baseline:** Early Copilot adoption

  sits around 10% utilization with conversion restricted to just 1--2

  users per 100 seats across scoped accounts (e.g., SafetyCulture,

  Xactly Corporation). This low conversion rate indicates that current

  deployment and enablement approaches are not yet driving the necessary

  enterprise-scale operationalization required to realize the

  platform\'s full revenue potential. We need architecture to scale

  successful MPOC (Minimum Point of Contact) enablement models.~~



### **~~Resource/Organizational Bottlenecks: Resolving Strategic Deadlocks~~**



~~Organizational friction and philosophical differences are creating

strategic uncertainty and resource waste, requiring explicit executive

direction.~~



- ~~**Account Health Scoring Methodology Conflict:** The disconnect

  between CSM leadership (Whitney/Antuna) and ELT/Product/BI teams on

  account health measurement remains a critical bottleneck. CSM

  leadership is fundamentally opposed to adopting a simple

  Red/Yellow/Green or continuous score, forcing AJ Belen and the team to

  pivot to using basic, delayed Renewal Prediction Scores (RPS) as a

  temporary measure. Executive intervention is required to establish a

  clear, unified measurement philosophy (actionability vs. renewal

  prediction) that aligns GTM incentives and avoids continued resource

  allocation to contested work.~~



- ~~**Low Adoption of High-Value GTM Agents:** Despite successful

  delivery of personalized AI-powered content agents (e.g., personalized

  roadmap and release notes) designed to eliminate manual work, internal

  adoption is critically low. The personalized account roadmap saw only

  4 uses, and Henry\'s company-wide email promoting the tools only

  generated 30--40 additional uses before plateauing. The consensus is

  that GTM teams are overwhelmed by information (25 different links) and

  these tools are not seamlessly integrated into existing workflows.

  This systemic gap threatens the ROI on our AI PMM infrastructure and

  requires a cross-functional enablement strategy overhaul to drive

  workflow integration.~~



### **~~Infrastructure Gaps Blocking Further Progress~~**



~~Critical infrastructure projects are stalled due to resource

allocation constraints and inherent platform complexities, preventing

deployment of key AI-driven capabilities.~~



- ~~**Semantic Layer Implementation Blockade:** The deployment of the

  unified semantic layer, which is essential for AI-powered business

  intelligence (AI Chat functionality) and consistent metric

  definitions, is blocked by resource constraints within the engineering

  team. Despite clear business value and Phoebe Mei completing the data

  requirements, the project requires explicit prioritization from

  Russell/Nir to allocate capacity for pipeline and subnet model

  development.~~



- ~~**Product Information Knowledge Base Deprioritization:** A

  foundational gap exists in the systematic management of Product

  Information Knowledge (technical documentation, feature specs). This

  knowledge is distinct from product marketing content and is critical

  for internal teams (CSM, Support) and feeding AI agents for accurate

  answers. Daniel Kong noted that this strategic imperative continues to

  be displaced by tactical fires. We need to define and protect

  resources to build this central source of truth to prevent multiple

  teams from solving similar problems using outdated information.~~



- ~~**CDP/Data Pipeline Instability:** Multiple analytical workstreams

  are blocked by intermittent CDP data connectivity issues and data

  pipeline deprecation. Nanxi Ge\'s investigation revealed that the

  LaunchDarkly Snowflake tables were deprecated in June without a

  replacement, eliminating the data pathway needed for CX teams to

  identify which customers are impacted by beta releases. This requires

  urgent resolution (API troubleshooting with Guy or formal request to

  restore Snowflake tables) to prevent ongoing support challenges.~~



### **~~Cross-Functional Coordination Needs~~**



~~Coordination gaps require structured engagement models to ensure data

quality and accelerate high-value strategic projects.~~



- ~~**Renewals Prediction Data Latency:** Renewal Prediction Score (RPS)

  data delivery from Tony\'s team is consistently delayed, taking 2+

  weeks monthly to finalize. This structural delay impacts the

  timeliness of executive reporting and strategic planning sessions. We

  need a formal SLA to establish clear second-week delivery expectations

  to manage stakeholder confidence.~~



- ~~**Integration Data Completeness Gaps:** Integration data analysis

  uncovered important coverage gaps, particularly concerning export

  tracking across vendor types and the complete absence of Org Import

  data from current tables. Ferrell Tanuwidjaja also noted that export

  data remains disconnected from the integrations dashboard. This lack

  of comprehensive bi-directional integration reporting necessitates a

  full data audit to ensure executive reporting reflects true customer

  integration patterns.~~



## **~~Section 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters~~**



~~\[Placeholder\]~~



## **~~Section 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?~~**



~~\[Also include what success looks like next quarter \]~~



## **~~Section 4: Beginning vs. End Contrast Table \[July 2025 vs. September 2025\]~~**



~~This table contrasts key operational and analytical areas,

illustrating the transformation journey from identifying blockers in

July to establishing momentum and capabilities by September.~~



