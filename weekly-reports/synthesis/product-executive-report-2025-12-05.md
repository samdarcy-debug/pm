---
id: synthesis-2025-49-2025
title: "Product Executive Intelligence Brief - December 05, 2025"
type: synthesis-report
status: approved
created: 2025-12-05
updated: 2026-01-06
week_ending: 2025-12-05
reporting_period: "November 24 - December 5, 2025"
tags: ["weekly-report", "synthesis", "Q42025"]
---

*Synthesized from 16 team reports: DAI Executive Team, Data Executive Team, GTM Studio Team, Intelligence Team, Product BI Team, Provisioning & Login Team, SalesOS/Copilot Team, Automation Team, Core Data Team, GTM Data Platform Team, Integrations Team, MCP Tiger Team, PMM Engine Team, Product Ops Team, Semantic Data Team, ZIM Team*

*For detailed questions about any item below, reference specific team reports or contact team leads directly.*

## **Executive Summary**

### **Roadmap Priorities**

In order to stay aligned and focused on the top priorities, see below for the most important work we've aligned to for this month and next.

![](C:\Users\DanielKong\pm\weekly-reports\synthesis\media/media/image3.png){width="6.776042213473316in" height="5.369408355205599in"}

### **AI Credit Consumption**

Given the importance of driving customer AI Action credit consumption, we will be reporting this each week.

![](C:\Users\DanielKong\pm\weekly-reports\synthesis\media/media/image1.png){width="8.279936570428696in" height="4.681349518810149in"}

![](C:\Users\DanielKong\pm\weekly-reports\synthesis\media/media/image2.png){width="8.297970253718285in" height="4.664288057742782in"}

### **Summary of blockers**

Summary of blockers across team reports. For more information, use the navigation bar to look into individual team reports in the appendix.

+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Challenge/Topic**                                   | **Specific Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Workspace Chat Reliability Crisis**                 | **SalesOS/Copilot Team:** Workspace Chat experienced tool failures reaching 78% for user engagement tools and 43% for transcripts, causing demo volume to collapse and requiring immediate intervention. Victor initiated daily get-well meetings across Workspace, agentic, and platform teams to implement early warning system before broader sales rollout.                                                                                                                                                                                                                                                 |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **Intelligence Team:** Tool failures in semantic data retrieval, person search, and engagement APIs were causing frustrating user experiences. GraphQL endpoints are failing 70% of the time for engagement data retrieval. Multiple breaking changes to GraphQL APIs from platform team occurred with no advance communication, causing MCP tools to fail unexpectedly.                                                                                                                                                                                                                                        |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **GTM Data Platform Team:** The Workspaces integration revealed that while GraphQL API can support arbitrarily complex queries, BigQuery as the backing store won\'t scale for high-volume use cases. Conversely, Solr scales well for volume but wasn\'t designed for deep aggregation and multi-hop joins with aggregation across joins.                                                                                                                                                                                                                                                                      |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM Datastore Data Quality & Pipeline Issues**      | **Semantic Data Team:** January 15th delivery deadline faces elevated risk due to upstream data dependencies in GTM Datastore. Speaker-to-person ID mapping essential for attributing conversation fragments to ZoomInfo contacts is missing from GTM Datastore pipeline. Current estimates push resolution past January. Analysis revealed 50-70% of ingested engagement records lack ZI company ID, severely limiting ability to associate conversations with accounts.                                                                                                                                       |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **Integrations Team:** ZoomInfo meeting recording imports face data model challenge where transcript speaker IDs currently use Chorus person ID which doesn\'t connect to any entity in GTM Data Model or Data Store, rendering it unusable for downstream teams. Proper solution requires using participant ID from GTM Data Model. Chorus engineering team needs to incorporate participant IDs into transcript generation process.                                                                                                                                                                           |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **Core Data Team:** Coordination gaps between Workflow and GTM Store teams regarding schema alignment created inefficiencies, with workbook teams operating without awareness of schema work completed in Q1. Location matching complexities persist with match service encountering difficulties when identifying office locations for companies with multiple child entities in same geographic area.                                                                                                                                                                                                         |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Engineering Resource & Infrastructure Constraints** | **Automation Team:** Analytics infrastructure evolution work extended to January, with BigQuery database migration requiring multi-step process through DevOps coordination including extensive testing to prevent data loss. Holiday timing compresses delivery windows.                                                                                                                                                                                                                                                                                                                                       |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **Data Executive Team:** Infrastructure access disruptions created operational friction - team lost access to frequently-used Snowflake table critical for C-suite moves processing without advance notification when 8,000 records populated review queue. Solr-to-Snowflake processing schedule extended to 48 hours, introducing delays across dependent workflows.                                                                                                                                                                                                                                          |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **SalesOS/Copilot Team:** Backend capacity is stretched thin due to GTM Data Model exploration, creating resource tension with chat accuracy improvements that also require senior engineering attention.                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **Product BI Team:** API dashboard work remains completely blocked due to data location mismatches between BigQuery tables in different workspaces. Engineering timeline extends to mid-January. AI credit Snowflake table was promised as highest priority but hasn\'t materialized, blocking progress on automated credit reporting.                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Legal & Compliance Risk**                           | **ZIM Team:** Major legal concern emerged regarding California consent requirements for device-to-person ID linking, which could severely hamper visitor resolution affecting websites, intent, and all downstream consumers. California represents massive customer concentration and data volume. If unable to guarantee consent for device-to-person linking, filtering out California residents would severely hamper resolution rates                                                                                                                                                                      |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **Data Executive Team:** Suresh Putteti discovered sensitive patient records (SSN, credit card data) in files transferred from DoubleO acquisition that were not intended for ZoomInfo systems. Working with legal, product, and engineering teams to coordinate complete deletion while configuring automated scanning to prevent future occurrences.                                                                                                                                                                                                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Data Credit & Monetization Policy Gaps**            | **Provisioning & Login Team:** Undefined policy for data credit usage in LLM-generated assets requires immediate executive decision to prevent revenue leakage. Currently, data credit charged when data leaves system via CSV or CRM export. However, when ZoomInfo data used to generate new asset (account summary, buying group list) through LLM and that end asset subsequently exported, no established pattern for charging data credits for privileged information contained within. Requires broader conversation on what \"leaving our system\" looks like in context of AI-driven feature creation. |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **GTM Studio Team:** Credit charging requires careful definition for AI-generated content. When customers use ZoomInfo data to generate AI derivative content (talking points, emails) and export that content without exporting underlying contact data, team needs clear rules on whether this incurs bulk credit charges. Represents new class of usage that existing credit definitions don\'t cleanly address.                                                                                                                                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Cross-Team Coordination & Process Gaps**            | **Product Ops Team:** Early access release program introduces complexity in managing release communications and enablement materials. Weekly cadence of freeze, feature flag, information gathering, and release to customers being split into two distinct phases with internal early access as own milestone. Creates questions about how to handle customer-facing roadmaps when early access releases shouldn\'t be communicated externally.                                                                                                                                                                |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **ZIM Team:** Design resource constraints becoming blocker across initiatives. Sylvia, Yoav, and Megan stated they won\'t work on Zoom projects, forcing search for alternative resources. This isn\'t about individual designers but systemic deprioritization of ZIM in resource allocation.                                                                                                                                                                                                                                                                                                                  |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **PMM Engine Team:** New weekly early access release cadence for Studio and Workspace provides better visibility but requires adjusted coordination with product management. Original 24-hour turnaround for feature selection may need adjustment now that review involvement questions are arising about feature prioritization decisions.                                                                                                                                                                                                                                                                    |
|                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                       | **Product BI Team:** Website AI Page Ranking feature launched weeks ago without any tracking instrumentation, costing valuable early adoption data. BI is being brought into launch tracking conversations weeks after products go live, when tracking setup and taxonomy development still require 2-3 weeks of work.                                                                                                                                                                                                                                                                                          |
+=======================================================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+

### **Relevant context across reports**

This section surfaces relevant information from team reports across the organization relevant to the given domain area.

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Domain Area & DAI**             | **Cross-Team Dependencies & References (from OTHER team reports)**                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM Studio (Sneh)**             | **SalesOS/Copilot Team:** Dylan encountered resistance from Audience/Studio engineering team on committing to how-to guide artifact creation epic, with team citing large in-progress project preventing timeline commitment. Victor instructed Dylan to share epic immediately for direct conversation with Sneh.                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Product Ops Team:** Team successfully rolled out weekly release workflow to GTM Studio team, building on established process with GTM Workspace. New weekly early access process for GTM Studio means features deploy weekly, turn on internally for opted-in sellers, and remain in early access until passing go/no-go review approximately week and half later.                                                                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **PMM Engine Team:** Team successfully delivered first objection handling document with stakeholder sign-offs from Victor and Sneh. Secured alignment with Sneh Kakileti on use case tool approach, shifting from Studio to ZI Chat for initial development with plans to productize in Q1.                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Integrations Team:** Product and engineering leadership reached alignment on scalable approach for integrating vertical datasets with audiences, establishing that GraphQL API delivery must precede UI work.                                                                                                                                                                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM Workspace (Victor)**        | **Intelligence Team:** Lars Vedo\'s no-code agent/artifact builder was rebuilt with database-driven architecture and is production-ready for internal rollout next week, enabling PMs like Dylan to build and test agents without engineering bottlenecks.                                                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Data Platform Team:** Workspaces is now enabled to consume first-party engagement data through GraphQL API, establishing unified pattern for how first-party and third-party data flow into any client. Linda Johannessen was on site for integration workshop with Workspaces engineering team.                                                                                                                                   |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Product Ops Team:** Voice of Customer tool successfully deployed to testable state with working micro-app, allowing internal workspace users to retrieve VOC fragments. Polling solution workaround allows removal of constraints to return significantly more fragments.                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **PMM Engine Team:** Jennifer Scharrer delivered customer-facing messaging for December release highlight features and completed first draft of Internal Guide helping sellers understand Workspace\'s positioning in sales tech landscape.                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Product BI Team:** Team successfully launched automated weekly utilization reporting through internal analytics chat agents for both Workbook and Workspace, with first reports scheduled to go live Monday.                                                                                                                                                                                                                           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM AI Context Service (Adam)** | **SalesOS/Copilot Team:** Adam Severance running comprehensive evals on new system prompt built with Caitlin Sanders showing massive improvements in strategic insights and analysis quality. Early testing with sellers reveals new prompt delivers better deal insights, pipeline analysis, and MEDDIC scores compared to current production system                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Automation Team:** Marc Frail deployed website visitor trigger with buyer ID behind feature flag under \"WebSights (Attributed)\" naming, enabling enterprise customers to track website visitor activity with identity resolution                                                                                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Integrations Team:** Sanyog Rai collaborated with Solr and data platform engineering teams to design optimizations for GTM Data Store and GraphQL, proposing junction tables between engagements and accounts as well as engagements and contacts to reduce resource-intensive table scans.                                                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Data (Brandon)**                | **Core Data Team:** Heather Ma participated in full ZI Lite team onsite in Waltham with core data team, achieving strong alignment on roadmap to close data gaps caused by Swapper.exe deprecation. Outcomes driving initiatives including engagement provider contact data acquisition, email signature ingestion from paying customers, and feasibility assessment for GTM data store user data integration from CRM and Slack systems |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Data Platform Team:** Moshik Levin expanding dataset onboarding process framework that Peter established, working to cover all inbound requests with consolidated trackers and playbooks. Discovered significant gaps in understanding of Engagement team\'s actual status and needs                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Data Executive Team:** Dana Hurtig\'s team crushed November targets, processing 5.9M enrichments and fixes - 36% above goal. Research and Data Enablement organization updated twice as many company records in November alone compared to entire 2024 calendar year, demonstrating compounding returns from systematic AI implementation.                                                                                             |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Platform (Ali)**                | **ZIM Team:** Matt Barnes progressed critical infrastructure work with form complete and websites data now flowing to GTM Store in staging (one fix away from production). Gap analysis on workbooks integration revealed fundamental blocker: signal workbooks currently only support website buyer ID, missing 97% of identifications that are company-level.                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Integrations Team:** Prateek Paikray completed implementation guides for both Snowflake and Databricks cloud data share integrations ahead of December 9th product release. These guides enable enterprise customers to configure data exports from GTM Studio audiences directly to cloud data warehouses.                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Automation Team:** Sam Massie delivered form builder to staging environment, completing DoubleO tool creation deep dive. Flexible field mapping expected next sprint, maintaining momentum toward comprehensive no-code automation capabilities.                                                                                                                                                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Operations (AJ)**               | **Intelligence Team:** Ryan McMaster progressed plays and pulses prototypes with updated audience building flows and incorporated latest branding refresh from marketing. End-to-end prototype demonstrates how users move from template creation through play management to pulse generation                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Studio Team:** Mohan facilitated critical onsite with Carlos, Ryan, and engineering leads that brought clarity to January 15 deliverable scope. Team aligned on building complete end-to-end use cases - one inbound (website trigger-based) and one outbound (audience-based).                                                                                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Product Ops Team:** Ken Elwell pivoted strategy on release enablement after discovering fundamental limitations in GTM Studio scaled email generation approach. Now building pull-based framework that structures roadmap and release items using VOC report categories, allowing sales reps to show most relevant updates to specific customers.                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **PMM Engine Team:** Team secured alignment with Sneh Kakileti on use case tool approach. AJ Belen will drive swimlanes documentation to completion and advance H1 planning discussions with Dominik and Adam around AI Context Service launch strategy.                                                                                                                                                                                 |
+===================================+==========================================================================================================================================================================================================================================================================================================================================================================================================================================+

### **Bottom Line**

This period reveals a critical inflection point where strategic ambitions collide with operational reality. Workspace Chat\'s 78% tool failure rate and subsequent demo volume collapse demonstrates the fragility of complex agentic architectures built on unstable foundations, forcing leadership to implement daily cross-functional standups and early warning systems before broader rollout. The January 15th delivery timeline for semantic data and plays functionality faces elevated risk from upstream GTM Datastore dependencies that remain unresolved, with missing speaker-to-person ID mapping and 50-70% of engagement records lacking ZI company IDs creating systemic attribution challenges.

However, the organization is making genuine progress on foundational capabilities that enable the strategic transformation. ROI Analytics launches December 9th for 22,000 Salesforce and HubSpot customers, GTM Data Platform successfully enabled Workspaces to consume first-party engagement data through GraphQL API, and the Data Research and Enablement team demonstrated exponential productivity gains by processing 2x more company updates in November than all of 2024 combined through aggressive AI adoption. The plays framework alignment achieved concrete scope for January 15th with batch run experience, credit charging, and two solid end-to-end use cases, while Brandon Wilson\'s CN Deal Insight Agent reached board-ready status with fully functional aggregate datasets.

The emerging pattern shows velocity in product innovation outpacing infrastructure stability and cross-team coordination capabilities. California consent requirements for device-to-person ID linking represent an existential threat to visitor resolution and persona intent differentiation, infrastructure access disruptions create unnecessary operational friction, and design resource constraints are becoming systemic blockers. Leadership attention is required on establishing architectural decisions (aggregation logic ownership between Solr and BigQuery), resolving GTM Datastore data quality pipeline issues before they cascade further, and creating sustainable coordination mechanisms for the new weekly early access release cadence that balances innovation speed with quality gates.

### **GTM Studio**

**GTM Studio Team:** \"ROI Analytics is launching to GA on December 9 for Salesforce and HubSpot customers, marking a major milestone after months of preparation, though multi-currency issues have surfaced that will exclude some high-value customers from the initial release. Plays completed a productive engineering onsite with Carlos and Ryan\'s teams to finalize the January 15 scope, aligning on batch run experience, credit charging, tools and triggers for building two solid end-to-end use cases (inbound using website triggers, outbound using audiences), though credit reporting requirements and bulk credit definitions need further discussion next week. Workbooks is progressing on duplicate/clone functionality with design discussions underway and nearly completed the signals enrichment side panel UX updates, while demo videos for the December 9 release are wrapping up. Data Management advanced the Data Health Scan with the team in staging validating sample sizes and logic (10% random sample up to 50k emails for invalid emails), though the Enrich approach remains an open question requiring Tuesday\'s meeting with Kasey and Magnus to resolve, and AI Onboarding moved forward with alignment that Data Management will essentially become a Play in the future, with proof-of-concept work starting next week.\"

### **GTM Workspace**

**SalesOS/Copilot Team:** \"Adam Severance is running comprehensive evals on a new system prompt built with Caitlin Sanders that shows massive improvements in strategic insights and analysis quality for Copilot Workspace chat. Early testing with sellers (Shafran, Lou, Tuna) reveals the new prompt delivers better deal insights, pipeline analysis, and MEDDIC scores compared to our current production system - addressing the #1 customer feedback issue we\'re seeing. Victor has called a dedicated Thursday meeting to dive deep on results and implementation strategy, recognizing this as the most important short-term fix available. Separately, Gabe delivered a working conversation intelligence trend discovery prototype that sales leaders validated positively, while Ant achieved system design alignment on the Pulse engine with broader team Nebo and Rakesh - establishing a pub-sub architecture that will handle insights, and agent-generated pulses for the 1/12 release.\"

### **GTM AI Context Service**

**Intelligence Team:** \"The team made solid progress stabilizing the agentic platform ahead of January milestones while addressing critical tool reliability issues. Lars Vedo\'s team achieved key wins with the no-code agent builder moving to production-ready state and resolved multiple blocking tool failures affecting user experience. The week balanced tactical firefighting - fixing broken GraphQL integrations and tool errors - with strategic progress on M3 triggers, user context capabilities, and plays/pulses workflows. Nathan completed knowledge transfer with Noah on doubleO backend integration, unblocking prompt configurability work needed for January 15th delivery.\"

**Semantic Data Team:** \"The January 15th delivery deadline faces elevated risk due to upstream data dependencies in GTM Datastore. The team discovered that speaker-to-person ID mapping - essential for attributing conversation fragments to ZoomInfo contacts - is missing from the GTM Datastore pipeline. Venkata is negotiating with the Chorus backend team and GTM Datastore team to accelerate the fix, but current estimates push resolution past January. Meanwhile, Jon and Inga delivered a breakthrough on account identification, developing a composite key formula that resolves the long-standing Salesforce-to-ZI-company-ID mapping ambiguity. Development continues on extraction and embeddings pipelines, with Sam and Jun making progress despite token limit constraints.\"

**MCP Tiger Team:** \"The team completed several foundational technical milestones this week that advance our MCP infrastructure capabilities. Topher delivered utility tool enhancements and began migration of the GTM Store MCP while Carter completed PubSub work and began end-to-end testing. Zheng created a composite tool proof of concept. The team is positioned to continue tool migrations next week, though we\'re working through SDK limitations around data usage analytics that may require alternative implementation approaches.\"

### **Vertical Datasets**

From **Data Executive Team:** Igor Kyrylenko reached 80% national coverage on professional licenses data and delivered comprehensive counts to a prospective customer, establishing the dataset as commercially viable. Auto dealer data advanced to 30 states with schema validation underway, while building permits data from 20 major cities revealed that only 7 states include contractor company names - an important constraint for future matching strategies.

### **Other Data**

**Data Executive Team:** \"The Data Research and Enablement team delivered exceptional November performance, completing 2x more company updates than all of 2024 combined through aggressive AI and automation adoption. Suresh Putteti identified and remediated sensitive patient records from the DoubleO acquisition that were improperly transferred to ZoomInfo, working with legal and engineering to ensure complete deletion. Meanwhile, Brandon Wilson progressed the CN Deal Insight Agent to board-ready status with fully functional aggregate datasets, positioning the team to showcase strategic benchmarking capabilities this week. Australian Business Registry matching expanded coverage by 25% to 700K active companies, though infrastructure disruptions around Snowflake access created operational friction for several workflows.\"

**Core Data Team:** \"John Durst supported the waterfall initiative with a successful demo demonstrating enhanced data enrichment capabilities across the platform. Magnus Herweyer began his onboarding for Contributory Network, rapidly gaining understanding of enterprise data sharing architecture while also facilitating a long awaited important alignment between AI Data Management and Data Engineering on shared services strategy. Heather Ma participated in the full ZI Lite team onsite in Waltham alongside the core data team, achieving strong alignment on the roadmap to close data gaps caused by Swapper.exe deprecation, with outcomes driving initiatives including engagement provider contact data acquisition, email signature ingestion from paying customers, and feasibility assessment for GTM data store user data integration from CRM and Slack systems. She also progressed Deal Insights Agent development by meeting with counterpart PMs to prioritize interface options across homepage Chat, workbook, and worksheet environments. Meanwhile, Cam Fortin secured the M8 timeline for automated new company creation with an end-of-April MVP target, providing engineering teams clear execution roadmap for H1 2025.\"

### **Other Platform**

**GTM Data Platform Team:** \"The team delivered a significant milestone this week: Workspaces is now enabled to consume first-party engagement data through the GraphQL API, establishing the unified pattern for how first-party and third-party data flow into any client. Linda Johannessen was on site for this integration workshop with the Workspaces engineering team, while Menna Rashwan finalized the MVP scope for Federated Search\'s December 31st delivery. The team remains on track for the year-end milestone, though architectural decisions around aggregation logic ownership need resolution next week to define the long-term implementation path.\"

**Integrations Team:** \"The team shipped foundational platform capabilities this week that unlock major enterprise opportunities. Prateek Paikray completed implementation guides for the Snowflake and Databricks Audience Export release launching December 9th, enabling customers to export GTM Data Model audiences directly to cloud data warehouses. Sanyog Rai supported the Workspace team\'s onboarding to GTM Data Model by proposing junction tables for engagement data optimizations, allowing downstream teams to query account and contact engagement relationships more efficiently. The engineering and product leadership teams aligned on a scalable GraphQL-first approach for vertical datasets and GTM Data Model Engagement data.\"

**Automation Team:** \"Form builder reaches staging and website tracking launches to production while analytics infrastructure work extends into January. Sam Massie completed DoubleO tool creation deep dive and released form builder to staging with flexible field mapping expected next sprint. Marc Frail deployed website visitor trigger with buyer ID behind feature flag and rapidly addressed missing Snowflake documentation, while beginning Google integration scope analysis. Adam Peretz made significant analytics progress but identified multi-step database migration requirements pushing completion to the second week of January due to holiday timing and infrastructure testing needs.\"

**Provisioning & Login Team:** \"The primary focus this week was preparing for monetizing third-party data and setting the final requirements for Records Under Management and Data Credits. The most critical item for executive awareness is the unclear strategy regarding data credit consumption when ZoomInfo data is processed and exported via LLMs (Large Language Models), which requires an immediate position to prevent revenue leakage and clarify data ownership. The team is ready to release user management UI/UX upgrade and intelligent username deduplication logic to streamline user provisioning for paid accounts and reduce support calls.\"

**ZIM Team:** \"Forrester scored us with 5 in Data, Fit Modeling, Anonymous Audience Segmentation, leads & contact segmentation and others. Forrester scored us unfavorably in some areas - 1s in community, self-service, reporting/analytics, and agents - with our response due Monday. This competitive vulnerability comes as Hillary Marks departed, leaving analyst relations without a lead. Meanwhile, a major legal concern emerged: California consent requirements for device-to-person ID linking could severely hamper visitor resolution, affecting websites, intent, and all downstream consumers. Hannah is writing a risk assessment, but Matt correctly identified this as a significant issue that needs immediate attention, not a \'small side issue.\' On the positive side, we\'re making progress on Freewheel (SOC 2 report expected next week) and architectural decisions that route 7 billion daily intent records directly to GEB instead of overwhelming GTM Store. Identity partners Self Service workflow has also completed E2E testing and ready for the first partners to onboard.\"

### **Other Operations**

**Product BI Team:** \"The team successfully launched automated weekly utilization reporting through internal analytics chat agents for both Workbook and Workspace, with the first reports scheduled to go live Monday. However, a critical process gap emerged: the Website AI Page Ranking feature launched weeks ago without any tracking instrumentation, costing us valuable early adoption data. With the API dashboard still blocked until mid-January and Nanxi out next week, the immediate focus shifts to strengthening BI involvement in launch planning and enriching agent capabilities with onboarding milestone data.\"

**PMM Engine Team:** \"The team successfully delivered the first objection handling document with stakeholder sign-offs from Victor and Sneh, marking completion of a foundational enablement tool for GTM Studio and Workspace. Jennifer Scharrer delivered customer-facing messaging for December release highlight features and completed the first draft of an Internal Guide helping sellers understand Workspace\'s positioning in the sales tech landscape. AJ Belen and Jennifer Scharrer supported the Forrester Wave talk track, with Brandon providing positive feedback on readiness. Akshath Dorai finalized AI Action Credits messaging and is preparing the objection handling agent for enablement handoff, while AJ Belen secured alignment with Sneh Kakileti on the use case tool approach, shifting from Studio to ZI Chat for initial development with plans to productize in Q1. The team is now navigating a new weekly early access release cadence for Studio and Workspace that will provide better visibility into product changes but requires adjusted coordination with product management.\"

**Product Ops Team:** \"The team successfully deployed the Voice of Customer tool to a testable state and rolled out the weekly release workflow to the GTM Studio team, marking significant progress in establishing repeatable processes. However, the introduction of Dominik\'s early access release program requires adjustments to our communication and enablement workflows, creating some near-term complexity as we decouple the weekly deployment cadence from customer-facing releases. Brett Jacobs is managing the transition with support from Kristin Gandini and Daniel Kong, while the team maintains focus on automation and tooling improvements that will support both internal and external release communications.\"

*For deeper analysis on any topic above, reference specific team reports or contact team leads directly.*

*Methodology: Analysis of team 1-2-3 Operating Framework reports, prioritizing: (1) Executive decisions needed, (2) Cross-team blockers, (3) Strategic momentum areas, (4) Strategic alignment gaps*

## **📊 Appendix**

### **Individual Team Reports**

## **DAI Executive Team Weekly Report - December 2-5, 2025**

**Executive Summary**

Workspace Chat experienced a trust-breaking reliability crisis this week, with tool failures reaching 78% for key functions, causing demo volume to collapse and requiring immediate intervention. Victor has initiated daily get-well meetings across Workspace, agentic, and platform teams to implement an early warning system before the broader sales rollout. Meanwhile, the team successfully consolidated planning for next week\'s on-site, with strong alignment on the plays framework and concrete prototypes emerging from the design team\'s AI-assisted data workflow initiative.

**This Week\'s Progress**

**Key Momentum Areas**

Victor\'s team uncovered and began addressing critical tool failures in Workspace Chat that were causing 78% failure rates for user engagement tools and 43% for transcripts, directly impacting sales confidence. The silver lining: these failures have been improved in the past week, and the identification process revealed exactly where monitoring gaps exist. This painful discovery will ultimately make the product more resilient through the early warning system now being built with Ali and Adam\'s teams.

The design team, led by Meghan, made substantial progress on the AI-assisted data workflows framework that emerged from the Bethesda session. Working with Sneh\'s team, they\'ve validated that this design pattern works across plays, audiences, and data management use cases, with prototypes ready to showcase next week. This represents a scalable foundation that multiple teams can leverage rather than building one-off solutions.

Brandon\'s team advanced the data flywheel and waterfall capabilities, adding 5 million secondary mobile phones from new vendors this week. More significantly, they\'ve identified that approximately one-third of \"valid\" emails don\'t actually reach real inboxes despite not bouncing---a discovery that positions ZoomInfo to differentiate on data quality if handled correctly through their traceability approach.

**Goals & Progress**

Workspace Reliability & Trust Recovery: Victor\'s team has identified the root causes of chat failures and initiated cross-functional daily standups to implement monitoring before users discover issues. The no-code agent builder, led by Lars with early adoption from Dylan, is progressing well and will enable faster artifact creation for the January feature set. Demo volume remains concerning at very low levels as sales has lost confidence, making the next two weeks critical for rebuilding trust internally before any external rollout.

On-Site Planning & Plays Framework: The team has aligned on 3-5 prioritized plays that will anchor next week\'s planning sessions, with Derek and Sneh coordinating the steel thread narratives. AJ and Brett have refined the weekly release motion for Studio and Workspace, establishing clearer timelines and expectations that reduce friction with enablement teams. The infrastructure discussions around plays have clarified that Platform owns workflow execution while GTM Studio owns the wrapper object and reporting.

Design System & Mobile Readiness: Meghan\'s team completed the foundation for pulses architecture in Workspace, based on signals, insights, and play-related pulses. They\'ve also made mobile app designs mobile-native rather than web-responsive, with Dima on Vivek\'s team structuring front-end code using tokens so color changes don\'t require heavy engineering lift. Navigation improvements are backed by research across AI tools and user interviews, with a data-backed proposal expected next week.

**Strategic Challenges**

The Workspace Chat reliability issues, while being addressed, highlight the brittleness of the current agentic system architecture. Tool owners weren\'t aware when their changes caused downstream failures, and there was no systematic way to catch these issues before users encountered them. Victor has correctly framed this as a partnership challenge across Workspace, agentic, and platform teams. The daily meetings and early warning system are the right response, but the underlying architectural decisions around tool composition and error handling need attention from Adam and Ali\'s teams to prevent recurrence.

Brandon\'s data team is wrestling with a competitive positioning challenge around email validation. They\'ve discovered that roughly one-third of email domains return valid results for all email addresses, meaning sends don\'t bounce even when emails aren\'t reaching real inboxes. Competitors like Apollo and Cognism include these emails, so removing them would make ZoomInfo look like it has inferior coverage. The team is developing proposals to surface this through traceability data and potentially move these to secondary values, but the right customer communication strategy remains unresolved.

Data management strategy for GTM Studio requires alignment between Sneh and Brandon\'s teams on whether to prioritize distribution-focused mid-market use cases or enterprise data structure requirements. The distinction matters: supporting plays like inbound lead acceleration for enterprises requires understanding subsidiary relationships, while full enterprise data management starts to overlap with MDM/Reltio use cases. The team needs to clarify which problem they\'re solving to avoid building the wrong thing or spreading too thin.

**Strategic Insights**

**Key Learnings & Discoveries**

The Forrester Data Wave timing, with Hilary\'s departure on the same day as the deadline, exposed a gap in succession planning for analyst relations functions. AJ and Jen stepped in to complete the talk track review, but this highlights the need for clearer ownership and documentation of these high-stakes external commitments. The friction in this function that everyone was aware of should have triggered earlier action on knowledge transfer and backup planning.

The convergence of use case requests around product selection and content recommendation---from both internal field teams and customers---validates that there\'s a genuine pattern here. AJ\'s discovery that 14 use cases with sub-use cases exist in the field, currently managed through slide automation tools, suggests an opportunity for systematic product support. Sneh\'s insight that this is really about ZI platform agents available in different workflows (centralized in Studio for some use cases, distributed to sellers in Workspace for others) provides the right framing.

Google\'s approach to AI agent distribution reveals important strategic constraints: they won\'t support MCP in Gemini the way OpenAI and Anthropic will, instead requiring vendors to use their A2A framework. Adam\'s meetings this week clarified that while there\'s no clean path for white-label data grounding with Google (unlike the potential with OpenAI and Anthropic), there is a path to publish to their agent marketplace. This means Q1 needs to include A2A development alongside the MCP work already underway, expanding the agent platform\'s scope.

**Cross-Team Dependencies**

The unified roadmap motion that the team invested heavily in 4 weeks ago is at risk of being abandoned as plays-based planning takes over. Adam and Sneh raised the important question of whether the unified roadmap continues as an artifact, and AJ confirmed it should remain as the execution view that stems from prioritized plays. The relationship needs to be explicit: plays provide the prioritization framework, unified roadmap provides the detailed execution view across teams, and both are necessary for the organization to function effectively.

Ali\'s team is surfacing critical alignment needs around how Zim fits into the broader platform strategy. The pricing and packaging misalignment with Studio, the lack of event-driven activation paths parallel to Workspace, and the absence of shared concepts like buying groups across applications all point to Zim operating too independently. Dominik\'s statement that \"there is no ZIM Plays different from Plays, Plays is ZoomInfo-wide. We need advertising APIs in Plays\" and the aspiration that \"in 2026 we need to consolidate onto our platform\" clarifies the strategic direction.

**Looking Ahead**

Next week\'s on-site in Waltham represents a pivotal moment for aligning the organization around plays-based execution. The team will use the first day to ensure shared understanding of the roadmap and plays framework across the broader organization, then dig into the 3-5 prioritized plays to map dependencies, gaps, and engineering requirements. Success means leaving with clear ownership of play components, understood cross-team dependencies, and confidence in the technical feasibility of the December and Q1 deliverables.

The immediate priority is stabilizing Workspace Chat reliability before broader internal rollout. Victor\'s daily standups with Ali and Adam\'s teams need to quickly implement monitoring for the most critical tools and establish the pattern for tool owners to understand their downstream dependencies. Simultaneously, the team should maintain development velocity on the January feature set---pinning artifacts, mobile improvements, and navigation changes---to demonstrate continued momentum even while addressing quality issues.

The plays framework discussions will naturally surface the need for clarity on how the agent platform, GTM Studio activation, and Workspace execution tie together. Rather than trying to resolve all architectural questions before starting, the team should focus on getting 1-2 plays working end-to-end in Q1, using those as forcing functions to drive the necessary platform decisions. The appetite for moving fast is high across the organization; channeling that energy into concrete deliverables while building the right abstractions will determine whether this motion succeeds or fragments into siloed efforts.

*Source: DAI Executives Operating Framework entries from Tuesday Dec. 2nd, 2025 - Friday Dec. 5th, 2025*

## **Data Executive Team Weekly Report - December 1-5, 2025**

**Executive Summary**

The Data Research and Enablement team delivered exceptional November performance, completing 2x more company updates than all of 2024 combined through aggressive AI and automation adoption. Suresh Putteti identified and remediated sensitive patient records from the DoubleO acquisition that were improperly transferred to ZoomInfo, working with legal and engineering to ensure complete deletion. Meanwhile, Brandon Wilson progressed the CN Deal Insight Agent to board-ready status with fully functional aggregate datasets, positioning the team to showcase strategic benchmarking capabilities this week. Australian Business Registry matching expanded coverage by 25% to 700K active companies, though infrastructure disruptions around Snowflake access created operational friction for several workflows.

**This Week\'s Progress**

**Key Momentum Areas**

Dana Hurtig\'s team crushed November targets, processing 5.9M enrichments and fixes---36% above goal---including 4.1M alternate mobile phones from ByteMine. The Research and Data Enablement organization updated twice as many company records in November alone compared to the entire 2024 calendar year, demonstrating the compounding returns from systematic AI implementation and process automation throughout the year.

Igor Kyrylenko reached 80% national coverage on professional licenses data and delivered comprehensive counts to a prospective customer, establishing the dataset as commercially viable. Auto dealer data advanced to 30 states with schema validation underway, while building permits data from 20 major cities revealed that only 7 states include contractor company names---an important constraint for future matching strategies.

Brandon Wilson completed local integration of the CN Deal Insight Agent with BigQuery aggregate tables replacing CSV files, positioning the demo for board presentation readiness. The team confirmed mid-December delivery of the CN eligibility flag in ZDP, unblocking multiple downstream initiatives including automated deal cycle benchmarking and strategic account insights.

**Goals & Progress**

Data Quality & Compliance: Suresh Putteti discovered sensitive patient records (SSN, credit card data) in files transferred from the DoubleO acquisition that were not intended for ZoomInfo systems. Working with legal, product, and engineering teams, he verified these were DoubleO customer records and coordinated complete deletion while configuring automated scanning to prevent future occurrences. Separately, he completed DNC coverage gap analysis and prioritized registry acquisitions in comparison with Cognism, with Sweden flagged for Q4 delivery per Amazon\'s request. Jody Roberts will support the procurement process for new DNC subscriptions.

Email Data Quality: Steve Hutchinson analyzed \"accept all\" email domains and discovered concerning patterns---33% of DOSI domains never immediately bounce any email, with 60% of those delivering all generated emails without bouncing and 40% showing delayed asynchronous bounces. This creates false positives in email generation training data and likely means many published emails deliver successfully but reach incorrect recipients. The team is testing whether vendors like Revenue Base and Allegro can programmatically authenticate with Google and Outlook to identify truly invalid addresses at these domains, with sample results expected soon.

International Coverage: Dana Hurtig expanded Australian Business Registry matching by approximately 25%, reaching around 700K active company matches from the original 550K. The registry contains 19-20M total records, but most are non-business entities like trusts and individuals. Additional fuzzy matching logic is being explored to maximize extraction value, though the team learned that limited standardized data fields in the registry constrain matching opportunities compared to other national registries.

**Strategic Challenges**

Infrastructure access disruptions created unexpected operational friction this week. The team lost access to a frequently-used Snowflake table critical for C-suite moves processing without advance notification, grinding that workflow to a halt when 8,000 records suddenly populated the review queue. Data engineers cited expense concerns but should have detected active usage patterns before restricting access. Additionally, the Solr-to-Snowflake processing schedule extended to 48 hours, introducing delays across dependent workflows. While Project Polynya (a new data lake using Iceberg) may address democratization needs longer-term, near-term coordination gaps are creating unnecessary blockers. Brandon Tucker requested specific table details to resolve with engineering leadership.

Steve Hutchinson\'s \"accept all\" domain analysis reveals a deeper email accuracy problem requiring vendor solution evaluation. With 33% of domains affected and 60% of those never bouncing invalid emails, the team needs to balance competitive parity concerns (Apollo and competitors publish these emails) against accuracy goals. The challenge is determining whether to flag these as lower-confidence, move them to \"potential emails\" columns in waterfall implementations, or remove them entirely. Revenue Base and Allegro testing will inform the path forward, but the team must avoid creating perceived coverage gaps versus competitors while improving actual deliverability.

Building permits data from 20 major cities shows only 7 of 20 states include contractor company names in permit records, limiting company matching potential. The team receives address pairs (permit location and contractor location) but without company names, matching relies entirely on address resolution. Igor Kyrylenko will deliver concrete volume statistics next week to determine dataset viability, though geographic coverage will remain inherently limited compared to competitors who may have alternative acquisition strategies.

**Strategic Insights**

**Key Learnings & Discoveries**

Dana Hurtig\'s team demonstrated that AI-driven automation delivers exponential rather than linear productivity gains. November\'s company update volume exceeded all of 2024 through systematic process improvements, offshore team reorganization, and aggressive AI tool adoption throughout the year. This validates the strategic bet on automation infrastructure and suggests similar approaches could dramatically accelerate other data domains in 2026.

The Australian Business Registry analysis revealed that most national registries contain far more non-business entities than operating companies---the ABR\'s 19-20M records compress to just a few million potentially viable businesses after filtering trusts, individuals, cancelled registrations, and inactive entities. This pattern likely applies to the 200+ national registries globally accessible to ZoomInfo. Brandon Tucker noted the team should develop repeatable classification processes for entity type identification, domain discovery, and many-to-one resolution that can become standard ingestion logic for Company 3.0, turning what is currently manual detective work into automated intelligence.

Ethan Young identified promising CN flywheel opportunities by analyzing customer CRM account presence patterns. Examining how frequently customers create accounts for entities like \"Hilton\" versus \"Doubletree by Hilton\" or \"Google\" versus \"Alphabet\" reveals which business entity structures align with actual buying patterns. Tenants with high win rates against YouTube as a separate account from Google could inform recommendations to other tenants still consolidating everything under the parent company. This aggregated intelligence---showing which account segmentation strategies correlate with success---creates differentiated value from shared CRM data while potentially falling under legacy EULA enrichment use cases rather than requiring new data sharing permissions.

**Cross-Team Dependencies**

Brandon Wilson\'s CN Deal Insight Agent requires the contributory network eligibility flag in ZDP, confirmed for mid-December delivery by Jesse Lindstrom. Multiple projects depend on this infrastructure, including automated benchmarking and strategic account recommendations. Suresh Putteti confirmed that while the flag exists in Salesforce Account objects and Snowflake, Heather Ma is coordinating with data engineering to replicate to ZDP for broader accessibility.

Steve Hutchinson\'s \"accept all\" domain investigation requires collaboration with Revenue Base, Allegro, and potentially other email validation vendors to test programmatic authentication approaches. The team also needs apps product leadership input on UI treatment options---whether to surface these as lower-confidence emails in waterfall implementations, relegate to \"potential emails\" columns, or maintain current publishing to preserve competitive parity. Brandon Tucker committed to flagging the issue to apps leaders and coordinating cross-functional resolution.

**Looking Ahead**

Next week brings 2026 planning sessions focused on end-to-end AI play enablement, data credit optimization, and enterprise data management capabilities. Brandon Tucker emphasized the data organization is well-positioned to support scaled play execution, though some tuning around CRM data integration and firmographic optimization will be needed.

The team will finalize new company creation testing with an estimated 1M net-new profiles from the staging environment run, alongside location data infusion from either Zippy or Crawler sources. Ethan Young is working urgently to ensure the data cube release includes both initiatives. Separately, the team must document a legal framework for using aggregated CRM account presence data to inform company definitions and account recommendations, determining whether this falls under legacy EULA enrichment provisions or requires new data sharing permissions. Brandon Tucker requested a brief paragraph for Hannah\'s legal review to resolve this question early rather than discovering constraints later.

The board demonstration of the CN Deal Insight Agent represents a watershed moment for showcasing ZoomInfo\'s ability to deliver differentiated benchmarking insights from contributory network data. Brandon Wilson confirmed the agent responds effectively to various question types and feels comfortable proceeding with live demonstration rather than recorded video. Success here will likely generate significant stakeholder interest and follow-on requirements, positioning the team to expand strategic analytics capabilities throughout 2026 as the CN flag infrastructure becomes widely available and aggregate datasets mature.

*Source: Data Executive Operating Framework entries from Dec. 1, 2025 - Dec. 5, 2025*

## **GTM Studio Team Weekly Report - December 1-5, 2025**

**Executive Summary**

ROI Analytics is launching to GA on December 9 for Salesforce and HubSpot customers, marking a major milestone after months of preparation, though multi-currency issues have surfaced that will exclude some high-value customers from the initial release. Plays completed a productive engineering onsite with Carlos and Ryan\'s teams to finalize the January 15 scope, aligning on batch run experience, credit charging, tools and triggers for building two solid end-to-end use cases (inbound using website triggers, outbound using audiences), though credit reporting requirements and bulk credit definitions need further discussion next week. Workbooks is progressing on duplicate/clone functionality with design discussions underway and nearly completed the signals enrichment side panel UX updates, while demo videos for the December 9 release are wrapping up. Data Management advanced the Data Health Scan with the team in staging validating sample sizes and logic (10% random sample up to 50k emails for invalid emails), though the Enrich approach remains an open question requiring Tuesday\'s meeting with Kasey and Magnus to resolve, and AI Onboarding moved forward with alignment that Data Management will essentially become a Play in the future, with proof-of-concept work starting next week.

**Key Momentum Areas**

ROI Analytics GA Launch Locked for December 9: Arun and Brahm successfully navigated the final pre-launch hurdles to confirm ROI Analytics will go live next week for Salesforce and HubSpot customers---representing roughly 22,000 connected customers. The team completed multiple Learn to Sell sessions, finalized enablement materials, and conducted additional CSM sessions to ensure field readiness. This launch represents a significant step toward demonstrating measurable value from GTM Studio and Workspace investments, creating a foundation for upsell conversations and adoption tracking.

Plays Engineering Alignment Achieved for January 15: Mohan facilitated a critical onsite with Carlos, Ryan, and engineering leads that brought clarity to the January 15 deliverable scope. The team aligned on building complete end-to-end use cases---one inbound (website trigger-based) and one outbound (audience-based)---with the batch run experience, credit charging mechanisms, and a defined set of tools (self, Outreach, Slack, Gmail) all mapped out. While nuances around credit reporting and bulk credit definitions require follow-up discussions, the fundamental architecture and use cases are now locked, enabling focused execution.

Data Management Foundation Taking Shape: Corina progressed the Data Health Scan to staging with validated logic for sample sizes and limits, positioning the team to begin broader testing with prioritized accounts next week. The AI Onboarding work reached a critical strategic milestone with stakeholder alignment that Data Management will be integrated as a Play, clarifying the information architecture questions and enabling the team to focus on proof-of-concept development. This week\'s design discussions and stakeholder alignment sessions removed ambiguity about how Data Management fits into the broader GTM Studio experience.

**Goals & Progress**

Workbooks: Duplicate Workbook and Signals Enrichment Progress: Tanvi initiated design discussions for cloning/duplicating workbooks with requirements conversations scheduled, positioning this capability for feedback and iteration next week. The signals enrichment side panel UX received final alignment from the design and content teams, with Sneh providing approval to move forward. Demo videos for the December 9 release items progressed, with most content recorded and only a couple remaining items to finalize.

Signal-Based Workbooks Scope Clarity Needed (Clear path forward): The find contacts enhancement work requires scope finalization and planning before engineering handoff can occur. Tanvi needs to connect with Sneh to establish the phased approach and prioritization for this capability, which has been identified as important for early access customers but hasn\'t been fully scoped. The path forward is clear---schedule alignment with Sneh and establish the crawl/walk/run phases---but needs dedicated time next week to lock in direction.

Plays: January 15 Scope and Architecture Finalized: Mohan and the engineering team completed a productive onsite that established the full scope for the January 15 internal customer-facing readiness milestone. The team reviewed and aligned on the batch run experience, credit charging logic for both AI and ZI credits, and identified the specific tools (self, Outreach, Slack, Gmail) and triggers (website for inbound, audience for outbound) needed to support two complete use cases. The engineering team began thinking through the architecture and data pipeline design to support long-term success of GTM Plays and beyond, moving from concept to concrete implementation planning.

Credit Requirements Refinement in Progress (No additional action required): The team identified nuances in credit charging that require further definition, specifically around reporting requirements for internal and customer-facing dashboards and clarifying which Play actions will incur bulk credit charges (beyond simple exports). Mohan noted that when customers use ZoomInfo contact data to generate AI content like emails and export only the content (not the contact), the team needs to define whether this incurs credit cost. These discussions are actively scheduled for next week with clear ownership, and both Jesse and the credit team are engaged in working through the requirements. The questions are known, the right people are involved, and resolution is being actively worked on.

ROI Analytics: December 9 GA Confirmed with Field Enablement Complete: Arun finalized all components needed for the December 9 GA launch for Salesforce and HubSpot customers. The team completed Learn to Sell sessions with 150+ participants, delivered enablement materials to the GTM team, and conducted additional CSM sessions as needed. The engineering team resolved the primary DevOps blocker and successfully completed the GTM Data Store migration validation in staging. Workspace and Chat ROI work progressed with both teams sharing initial datasets, and the CFA team is currently reviewing the published data ahead of next week\'s deeper alignment sessions.

Dynamics Support Delayed and Currency Issues Surface (No additional action required): Support for Dynamics customers has been pushed to a future release, and multi-currency conversion issues emerged that affect nearly all Dynamics customers and some Salesforce/HubSpot customers. When the team encounters currencies that aren\'t cleanly converted, the numbers can reach extreme values (trillions of dollars in some cases), making the ROI data misleading. The team made the decision not to show ROI to these customers---fewer than 100 accounts but including some of the largest customers---until proper fixes are identified. The engineering team is actively working on solutions, including exploring a currency conversion service approach since the Platform team won\'t prioritize multi-currency support in the near term. Arun and Brahm are driving this work forward with clear ownership and a path to resolution.

Data Management: Data Health Scan Staging Validation Underway: Corina and the team successfully moved the Data Health Scan to staging and began validating the logic and sample sizes needed for the metrics. The team established a 10% random sample approach with a 50,000 email limit for invalid email detection using Neverbounce. Backend work has commenced, and the FE team (from Denis\'s group) has been assigned and is ready to begin development. Version 2 of the Data Health Scan POC is being prepared to send to prioritized accounts, incorporating the same metrics that will be used in GTM Studio for validation with real customer data.

Enrichment Approach Requires Decision (Clear path forward): The team still needs to finalize the best approach for using Enrich to get percentage fill rate and data correctness. A meeting is scheduled for early next week (Tuesday) with Kasey and Magnus to confirm the optimal way to leverage Enrich for these metrics. This isn\'t blocking current development work since the Neverbounce logic is proceeding, but it\'s the last missing piece of information needed before the backend can be fully finalized. There\'s a clear path forward with the meeting scheduled and the right stakeholders identified.

**Strategic Insights**

**Key Learnings & Discoveries**

Credit Charging Requires Careful Definition for AI-Generated Content: Mohan surfaced an important question during the Plays engineering sessions: when customers use ZoomInfo data to generate AI derivative content (like talking points or emails) and export that content without exporting the underlying contact data, the team needs clear rules on whether this incurs bulk credit charges. This represents a new class of usage that existing credit definitions don\'t cleanly address, and getting the definition right is important for both customer trust and revenue recognition. The team is working through these scenarios with the credit team next week.

Operator vs. Revenue Leader Product-Market Fit Requires Clear Distinction: Sneh identified an important tension over the past 3-4 months where revenue leaders (like Rob Laser and LinkedIn VPs) have shown strong interest in using GTM Studio to analyze their books of business, but the product\'s complexity makes it too challenging for that persona. The realization is that GTM Studio should continue to serve the sophisticated operator persona who needs complex workflow capabilities, while Workspace should handle the simpler, non-technical needs of sales and sales leaders. The team shouldn\'t simplify Studio to accommodate revenue leaders---that would compromise the ability to win against competitors like Clay in complex use cases.

Data Health Scan Sample Logic Needs Business Intelligence: During discussions about the Data Health Scan sampling approach, Sneh raised valuable questions about whether the team should apply business logic to the sampling rather than pure randomness. For example, should the scan prioritize showing the health of recently created emails (last 2 months) versus older data, since customers likely care more about the quality of their newest leads? The team recognized that there\'s opportunity to make the sampling more strategically valuable by tying it to customer business priorities rather than just statistical representation, and this thinking will continue as the feature develops.

**Cross-Team Dependencies**

Enrichment API and Limits Alignment Required: The Data Management team needs to meet with Kasey and Magnus on Tuesday to confirm the approach for using Enrich to calculate fill rate percentages and data correctness. This meeting will determine how to leverage Enrich within the Data Health Scan and establish what limits should be applied. The meeting is scheduled with clear attendees and objectives.

Workspace and Chat Instrumentation for ROI (Clear path forward): Arun identified that Workspace and Chat ROI Analytics are trending red for January/February releases because source teams haven\'t yet prioritized or begun the instrumentation work required. The Workspace and Chat teams have shared initial datasets, and the CFA team is reviewing them ahead of next week\'s alignment sessions where the full requirements will be discussed. Arelai is arranging weekly calls to accelerate progress. While timelines are tight, there\'s a clear engagement plan with the right stakeholders involved, and work is actively progressing toward resolution.

**Looking Ahead**

Launch Week Focus and 2026 Planning Sessions: Next week brings two major focus areas for the GTM Studio team. The December 9 customer release for ROI Analytics and Workbooks features requires final preparation, including completion of remaining demo videos and ensuring all enablement content is ready for the field. Simultaneously, Sneh will lead a two-day 2026 planning session with Dominic\'s staff and product leadership on Tuesday and Wednesday, using Plays as the steel thread to walk through the entire GTM Studio product suite and establish clear roadmaps for the year ahead.

Plays Credit Requirements and JIRA Structure Establishment: Mohan will work with the credit team and Jesse to close out the remaining credit charging questions, specifically around reporting requirements (internal and customer-facing dashboards) and defining which Play actions will cost bulk credits. Once these requirements are finalized, the team will establish the JIRA structure with Randy and officially kick off development work toward the January 15 deliverable. This represents the transition from planning to execution for Plays.

Data Management Proof-of-Concept Work and Engineering Coordination: Corina will focus on running cost analysis for both Enrich and Neverbounce to understand the scaling implications of the Data Health Scan, and the team will begin the first working session for the AI Onboarding proof-of-concept. The goal is to validate whether the dual-interface hypothesis (visual canvas plus interactive chat) is the right approach and identify any gaps in current capabilities or team dependencies. This exploratory work will inform the information architecture decisions for how Data Management integrates with Plays, setting the foundation for development work in January.

*Source: GTM Studio Team 1-2-3 Operating Framework entries from December 1-5, 2025*

## **Intelligence Team Weekly Report - December 1-5, 2025**

**Executive Summary**

The team made solid progress stabilizing the agentic platform ahead of January milestones while addressing critical tool reliability issues. Lars Vedo\'s team achieved key wins with the no-code agent builder moving to production-ready state and resolved multiple blocking tool failures affecting user experience. The week balanced tactical firefighting---fixing broken GraphQL integrations and tool errors---with strategic progress on M3 triggers, user context capabilities, and plays/pulses workflows. Nathan completed knowledge transfer with Noah on double-zero backend integration, unblocking prompt configurability work needed for January 15th delivery.

**This Week\'s Progress**

**Key Momentum Areas**

Lars Vedo\'s team shipped critical reliability improvements across the agentic platform, fixing tool failures in semantic data retrieval, person search, and engagement APIs that were causing frustrating user experiences. The no-code agent/artifact builder was rebuilt with database-driven architecture and is production-ready for internal rollout next week, enabling PMs like Dylan and Ant to build and test agents without engineering bottlenecks. Nathan completed knowledge transfer sessions with Noah on double-zero backend integration, positioning the team to deliver prompt configurability and agent template extensions needed for plays workflows.

Rowan Bailey advanced the user context and preferences PRD to approximately 50% complete, defining how user-level preferences will integrate with tenant configuration and memory service. This work addresses the \"cold start\" problem in agentic interactions where the critical context tool lacks sufficient personalization. Carlos Nunez\'s team expanded offerings data from 100K to 3 million companies using a cost-optimized approach after disputes with Google\'s GenAI Search pricing, while simultaneously deploying a fast, cheap model for competitor identification that avoids expensive LLM calls.

Ryan McMaster progressed plays and pulses prototypes with updated audience building flows and incorporated the latest branding refresh from marketing. The end-to-end prototype now demonstrates how users move from template creation through play management to pulse generation, with signal-based examples from Victor and Ant baked in. Srivatsa Marthi finalized M3 design iterations with better alignment to run-plays workflows and existing double-zero patterns, scoping down to document view only (hiding canvas view) to ensure January 15th delivery remains achievable.

**Goals & Progress**

Agentic Platform Stability: Lars Vedo\'s team resolved approximately 8-10 critical tool failures including get_user_engagements, person_search, semantic/Chorus transcript retrieval, and HTML artifact loading issues. Human-in-the-loop functionality reached PR review stage and will demo next session. The team created comprehensive tool inventory and established SLO requirements with tool owners to enable proactive monitoring and pager duty alerts. Chat history page designs kicked off, and deal status agent (built with Dylan) integrated into workspace with novel artifact patterns. Progress represents critical foundation work for reliable January launches---approximately 85% complete on core stability requirements.

Double-Zero Integration: Nathan completed knowledge transfer with Noah on double-zero backend systems, unblocking work to extend no-code platform templates for plays workflow requirements. Lars Vedo scoped three-phase approach with Derek\'s PRD as foundation, covering prompt management with variable support, tools/skills registry unification, and agent template configuration for context passing. The architectural approach extends existing React and orchestrator templates to support what plays needs for giving/receiving context during workflow execution. Engineering kickoff targeted for next week with Al assigned to front-end implementation---approximately 20% complete with clear path forward established.

User Context & Preferences: Rowan Bailey advanced PRD development to address critical gaps in user-level and tenant-level context that feeds the \"critical context\" tool in agentic interactions. Key remaining work focuses on how user preferences override tenant-level GTM configuration (e.g., if a rep knows they don\'t sell a configured offering), and integration points with memory service designs. This work directly improves the starting point for most agentic interactions where agents call critical context first to understand who\'s on the keyboard. Need input from Lars Vedo on interaction patterns and Dylan on workspace preferences next week---approximately 50% complete on PRD with implementation path being defined.

**Strategic Challenges**

Rowan Bailey\'s team encountered multiple breaking changes to GraphQL APIs from the platform team this week with no advance communication, causing MCP tools like get_engagements to fail unexpectedly. The pattern repeated 2-3 times during the week where the MCP team discovered tools stopped working and had to triangulate the cause retroactively. Even the platform team wasn\'t always aware changes had shipped. This highlights a process gap in dependency management and change communication that becomes more critical as more teams build on these shared services. Clear resolution path exists through better comms protocols and advance notice requirements---Rowan will coordinate with platform team leads on establishing these patterns.

Tool ownership and SLA clarity emerged as a blocker affecting user experience quality, with Lars Vedo identifying that mission-critical tool failures create the most frustrating user experiences. The team created a comprehensive inventory across the agentic platform and initiated conversations with tool owners about error handling improvements, monitoring dashboards, and pager duty setup. Several tool owners updated error messages to enable LLM self-correction. Path forward includes establishing formal SLOs and automated alerting, but requires coordination across multiple teams. This is solvable but needs executive alignment on ownership model and response expectations.

Srivatsa Marthi\'s call with sales revealed significant usability concerns for the January 15th plays configurability release. While the team is solving for technical completeness---migrating all signals, building full configurability---sales highlighted that non-technical users will struggle with the complexity. The feedback reinforced the need to invest quickly in templated plays library and AI-assisted play building rather than expecting users to configure from scratch. There\'s clear path forward through templating and prompting but requires prioritization discussion with Derek for post-January 15th roadmap. Not a delivery blocker but important strategic consideration for adoption.

**Strategic Insights**

**Key Learnings & Discoveries**

Lars Vedo\'s observation about tools being \"mission critical\" validated through this week\'s firefighting---tool failures create the worst user experiences because they break the agent\'s ability to complete tasks users requested. The team\'s shift toward treating each tool as a potential sub-agent with independent context windows (Rowan Bailey and Zhang\'s composite tools work) represents important architectural evolution. This pattern gives flexibility to handle large result sets, apply compression before passing to orchestrator, and enable graceful degradation when tools fail. The convergence between Lars\'s sub-agent work and Rowan\'s composite tool experiments suggests this should become standard pattern across the platform.

Carlos Nunez\'s team discovered that running semantic data and web search from workbooks at scale (60K+ rows) works functionally but fails silently when customers lack semantic data, creating poor user experience with no visual indication. This revealed gap between technical capability and user-facing experience design. The team coordinated with Jagan\'s group to improve column enrichment UX, but the broader learning is that batch operations need graceful degradation and clear status communication. Similar pattern likely exists elsewhere in the platform where technical success doesn\'t translate to user confidence.

Adam Smith\'s question about signals feeding pulses into Workspace highlighted architectural gap that team hadn\'t fully resolved: if plays run at tenant level but a customer has Workspace without Studio, how do out-of-box signal-driven pulses work? Running same computation 30K times across tenants for identical signals is non-starter. The discussion revealed this wasn\'t just Adam\'s knowledge gap but genuine unresolved design question requiring cross-team alignment. Srivatsa Marthi added to pulse/plays meeting to help solve. This represents classic integration challenge where individual pieces work but cross-product flows need explicit design attention.

**Cross-Team Dependencies**

Carlos Nunez\'s work with the workbooks team (Tushar, Jagan) on batch column enrichment continues progressing well with semantic data and web search working at 60K row scale. The team needs tighter coordination on user experience improvements around error states and status indication, but technical foundation is solid. Scoring data ready for workbooks team to consume in Studio audiences---IMS and IFS bucketing unchanged but calculation method improved underneath, already available in HBASE for Tushar\'s team to surface as filterable attributes in GTM Studio.

Ryan Stevens and Derek\'s agentic audience building work in Bethesda this week represents critical dependency for plays-to-agents and agents-to-plays bidirectional calling. This work unblocks January milestones but requires Ryan McMaster\'s design work on audience building UX to align. The prototype incorporating audience management flows directly supports this technical implementation. Coordination working well with Victor traveling to Bethesda for alignment sessions.

**Looking Ahead**

Next week focuses on productionizing the no-code builder for internal PM usage, completing user context PRD for team review, and finalizing M3 trigger designs. Lars Vedo will roll out agent builder to friendly tire-kickers including Dylan and Ant, enabling rapid prototyping without staging limitations. Rowan Bailey needs input from Lars on interaction patterns and Dylan on workspace preferences to close remaining PRD sections, then will shift focus to external MCP tooling and context service work ahead of the Waltham product leadership on-site.

The Waltham on-site Sunday-Wednesday will pull Rowan Bailey and others away for 2-3 days but represents important strategic alignment opportunity. Srivatsa Marthi will take on additional project work since M3 triggers are tracking well for January 15th---Derek identifying specific assignment. Ryan McMaster continues plays/pulses prototype refinement and will share updated designs for annual planning discussions. Tool reliability work continues with Lars coordinating formal SLO establishment with tool owners and implementing comprehensive monitoring dashboards.

Carlos Nunez\'s team begins QA on offering-competitor relationships with research team while continuing to iron out GTMDS consumption patterns and partition key optimization. The 500GB to 5GB query optimization from James Geyer should deploy soon even before Venkata completes BigQuery materialized tables work. Team confidence remains high for January milestones despite typical end-of-year coordination challenges.

*Source: Team Intelligence Operating Framework entries, meeting transcripts, and Friday reflections from December 1-5, 2025*

## **Product BI Team Weekly Report - December 5, 2025**

**Executive Summary**

The team successfully launched automated weekly utilization reporting through internal analytics chat agents for both Workbook and Workspace, with the first reports scheduled to go live Monday. However, a critical process gap emerged: the Website AI Page Ranking feature launched weeks ago without any tracking instrumentation, costing us valuable early adoption data. With the API dashboard still blocked until mid-January and Nanxi out next week, the immediate focus shifts to strengthening BI involvement in launch planning and enriching agent capabilities with onboarding milestone data.

**This Week\'s Progress**

**Key Momentum Areas**

Phoebe\'s team delivered automated weekly utilization reporting through the internal analytics chat agents, standardizing metric naming and report formats across both Workbook and Workspace applications. The system will push reports to analytics channels every Monday morning, eliminating manual reporting overhead while providing consistent visibility into product usage patterns. The agents now include hierarchy segments, with work underway to join the two agents so users can query across both products simultaneously.

Christon completed all onboarding training and immediately dove into practical work, partnering with Ferrell to identify churned accounts from Finance\'s data. The collaboration is serving dual purposes: advancing the ZIM churn analysis while building Christon\'s familiarity with the marketing data ecosystem. Early findings reveal that audience creation timing matters more than the activity itself---accounts creating audiences within 30 days show different retention patterns than those waiting 90 days.

Ferrell completed initial exploration of ZIM churn patterns comparing churned versus renewal accounts over the past year. The analysis uncovered that 31% of accounts with renewals in that window ultimately churned, with 21 of those accounts never creating audiences despite engagement with the product. The next phase will examine usage trends across the full customer journey to understand what differentiates successful accounts from those at risk.

**Goals & Progress**

GTM Workspace Analytics: The agent infrastructure is expanding beyond basic utilization metrics. AJ and Phoebe are refining the data presentation format for leadership visibility, with plans to incorporate AI Action Credit usage data once the Snowflake table becomes available next week. The team is also working with Nate Alcorn to integrate onboarding milestone data from Salesforce, which will provide critical context about why early-stage customers may not yet be consuming credits---addressing questions that arose this week when reviewing adoption patterns with Dominik.

AI Action Credit Reporting: The engineering team confirmed the AI credit Snowflake table remains their highest priority this week, alongside a second table for AI prompt details. Once available, these tables will link directly to the agent for automated credit usage reporting by account. This represents a significant step toward self-service analytics for product teams, though the timeline remains dependent on engineering bandwidth.

Launch Analytics Infrastructure: Nanxi initiated conversations with the PM and engineering team to establish tracking taxonomy for the Website AI Page Ranking feature, which launched several weeks ago without instrumentation. The taxonomy development process will extend into the holidays, meaning the first tracked data won\'t be available until January---representing over six weeks of lost early adoption signals. Concurrently, Nanxi automated portions of the Tableau reporting workflow and investigated API data structure issues, proposing solutions to the engineering team.

**Strategic Challenges**

The Website AI Page Ranking launch revealed a recurring process breakdown: BI is being brought into launch tracking conversations weeks after products go live, when tracking setup and taxonomy development still require 2-3 weeks of work. The timing means we\'re systematically missing the most valuable adoption window---those critical first weeks when customers activate new features. Alward reached out this week requesting tracking support, but the feature had already been live long enough that we\'re now crossing into the holiday period, further delaying implementation. Phoebe\'s team encountered this same issue previously and developed standardized taxonomy templates for common event properties, yet PMs continue reaching out only after launch rather than during planning phases.

The API dashboard work remains completely blocked due to data location mismatches between BigQuery tables in different workspaces. While the solution is straightforward---build a new table in the correct location enabling joins---the engineering timeline extends to mid-January. Adam worked with DevOps to scope the effort, but when questioned whether the delay stems from technical complexity or competing priorities, no clear answer emerged. This leaves Nanxi\'s API analysis work stalled for over a month, with no alternative path forward.

Engineering capacity constraints are creating cascading delays across multiple workstreams. The AI credit Snowflake table was promised as highest priority this week but hasn\'t materialized, blocking progress on automated credit reporting. The API table rebuild faces similar resource competition. While individual engineering partners like Harsh are responsive, the broader bandwidth picture suggests we may need executive intervention to secure dedicated resources for analytics infrastructure that multiple teams depend on.

**Strategic Insights**

**Key Learnings & Discoveries**

There\'s a fundamental misalignment between how product launches happen and when BI becomes involved. The current pattern---PMs reaching out weeks post-launch requesting tracking---stems partly from knowledge gaps about taxonomy creation, but more critically from missing organizational norms about when analytics must be at the table. While taxonomy templates exist for standardized properties, and tools like ChatGPT can generate basic event structures, the real issue is strategic: without early involvement, BI cannot advise on which signals matter most for measuring success, cannot prepare baseline comparisons, and cannot validate instrumentation before launch. The six-week data gap for Website AI Page Ranking demonstrates the cost of this reactive approach.

Cross-functional dependencies consistently surface as the rate-limiting factor in analytics work. The API dashboard depends on DevOps table creation. Credit reporting depends on engineering\'s Snowflake implementation. Launch tracking depends on engineering\'s instrumentation deployment. While the team has built workarounds---agents for automation, templates for standardization, direct PM partnerships---these tactical solutions don\'t address the structural reality: analytics infrastructure requires sustained engineering investment, and current prioritization processes don\'t reliably secure that investment. Nanxi\'s observation that she couldn\'t get a straight answer about whether the API table delay is technical or priority-based suggests this tension isn\'t being resolved transparently.

The analytics agents are proving their value beyond automation---they\'re changing how teams think about data access. AJ\'s example of needing to explain to Dominik why workspace customers aren\'t consuming credits yet highlights a broader pattern: context matters as much as metrics. By incorporating onboarding milestone data into the agent, the team can shift conversations from \"why isn\'t this number higher\" to \"here\'s where this account is in their journey and what we\'d expect at this stage.\" This represents a maturation from reporting what happened to enabling interpretation of why it happened.

**Cross-Team Dependencies**

Our ability to deliver on multiple commitments hinges on engineering teams prioritizing analytics infrastructure requests. The AI credit table, API data migration, and launch tracking instrumentation all require engineering resources that appear oversubscribed. While individual engineers are responsive and engaged---Adam worked through the API solution, Harsh scoped the technical approach---the timeline slippage suggests these requests aren\'t winning prioritization battles against other work. Without clearer communication from product leadership about which launches are strategic priorities requiring BI involvement upfront, we\'ll continue this reactive pattern of post-launch tracking requests that deliver limited value.

The emerging Amplitude transition planning requires coordination with Tal\'s team and potentially Russell\'s organization, based on AJ\'s meetings this week. This represents both opportunity and risk: migrating platforms mid-stream on active projects could compound existing delays, but continuing on a tool the organization may sunset creates technical debt. AJ is waiting for Tal to reach out to Nanxi to advance these conversations, but the decision timeline and transition approach need clarity before year-end.

**Looking Ahead**

Next week\'s focus centers on enriching the agent capabilities while Nanxi is out, with Phoebe and Eran leading the technical implementation. The team will validate that automated reports land as expected Monday morning, then iterate on the data presentation format based on AJ\'s leadership reporting needs.

The immediate priorities include resolving the agent hierarchy issue, incorporating onboarding milestone context from Nate Alcorn\'s Salesforce data, and---if engineering delivers---integrating AI credit usage data into the agent. AJ will verify the agent can handle target use cases before declaring success, rather than simply dumping data in. Phoebe will also advance the workspace prompt categorization analysis using the AI usage quadrant framework, searching for patterns that explain why some customers become high AI users while others remain low utilization.

Ferrell and Christon will continue the ZIM churn analysis collaboration, with Christon sending AJ a mid-week summary covering any blockers or difficulties. Nanxi emphasized the importance of immediate escalation when stuck---a pattern she\'s seeing across newer analysts who sit on blockers trying to self-resolve rather than seeking help quickly. The churn work should progress from audience creation analysis toward broader usage trends and campaign patterns by week\'s end. When Nanxi returns the following week, she\'ll follow up on the launch tracking conversation to ensure BI gets positioned earlier in the product development cycle for future releases.

*Source: Team 1-2-3 Operating Framework entries from December 5, 2025*

## **SalesOS/Copilot Team Weekly Report - December 1-4, 2025**

**Executive Summary**

Adam Severance is running comprehensive evals on a new system prompt built with Caitlin Sanders that shows massive improvements in strategic insights and analysis quality for Copilot Workspace chat. Early testing with sellers (Shafran, Lou, Tuna) reveals the new prompt delivers better deal insights, pipeline analysis, and MEDDIC scores compared to our current production system---addressing the #1 customer feedback issue we\'re seeing. Victor has called a dedicated Thursday meeting to dive deep on results and implementation strategy, recognizing this as the most important short-term fix available. Separately, Gabe delivered a working conversation intelligence trend discovery prototype that sales leaders validated positively, while Ant achieved system design alignment on the Pulse engine with broader team Nebo and Rakesh---establishing a pub-sub architecture that will handle insights, and agent-generated pulses for the 1/12 release.

**This Week\'s Progress**

**Key Momentum Areas**

Adam completed side-by-side artifact comparisons of our current production system prompt versus the Caitlin Sanders-designed prompt across 15+ test scenarios, measuring quality, depth of insight, token usage, cost, and latency. The new prompt consistently surfaces conversational insights from engagement data that our current system misses---calling Transcript Insight and Chorus Insights far more frequently when analyzing deals and preparing for calls. This directly addresses the persistent feedback that chat isn\'t mining meeting intelligence effectively, with sellers scheduled throughout the week to validate the improvements demonstrate genuine value in their workflows.

Gabe shared high-level requirements and a working prototype for conversation intelligence trend discovery after positive feedback from sales leader discovery sessions. The prototype demonstrates semantic analysis of call patterns, with engineering estimates suggesting many underlying components already exist to support December delivery. Dylan noted that hierarchy will be an important dimension for the insights, identifying a gap where Workspace currently relies on CRM hierarchy data that may not cover all needed scenarios.

Ant distributed an end-to-end Pulse narrative and completed architecture alignment with Nebo, Rakesh, and Brian Chase on a pub-sub system where a Pulse agent processes insights what pulses are delivered to a user. Engineering kicks off platform development next week, with Ant building the Pulse agent alongside bespoke agents for territory roll-ups and utilization risk. The design represents consensus that out-of-the-box pulses need a Workspace engine rather than relying entirely on the Plays platform, with Studio and agent-created content flowing in as additional sources.

**Goals & Progress**

Copilot Workspace: Adam shipped hierarchy improvements expanding SFDC manager lookups from 50 to 100+ levels as a holdover before GTM Store migration, with Laser account testing scheduled to validate the change opens up senior and leadership-oriented prompts. The eval framework with 40 test queries awaits final Data Science deployment to production, delayed from last week but positioned to establish ongoing baseline quality metrics. Workspace Views UI improvements including filter experience rebuilds progressed through engineering refinement, though timeline uncertainty around the 2K limit architectural decisions is slowing some medium-effort work on grouping and row behavior.

Mobile: Ant shipped new release of mobile app in staging with chat and notes fully functional as well as speech to text. The team is working in partnership with the agentic platform team to upgrade from APIs to a headless component of chat which will allow for optimized loading and rendering of chat content and components. UI overhaul is in progress, and still on track for a December alpha in TestFlight.

ZoomInfo Intent: Harry completed gap analysis documenting 10 distinct feature differences between Legacy Intent UI and Workbook Components, with Friday presentation scheduled to Intent, WebSights, and ZIM teams. The analysis reveals architectural challenges including Workbooks\' 200K record limit versus Legacy Intent\'s larger dataset support, alongside missing features like Intent Topic AND/OR filtering, saved searches, and streaming Intent capabilities. David released Admin Defined Territories feature flag with 90 tenants enabled since launch, continuing MCP work to expose territory definitions to the agentic layer while addressing customer requests for broader territory usage across Search, WebSights, and Intent.

Admin Zero Experience: David prototyped Priority Accounts configurations in Replit and reviewed with the Context team, discovering some results missing expected data requiring underlying dataset changes. Infinite scrolling testing for Copilot V1 feed (removing 50-update cap) can only begin next week pending developer availability, with CFA team expressing concerns about dashboard overload once users access significantly more target account signals. Harry delivered MS Dynamics CRM filter completing staging testing, achieving CRM parity with Salesforce filtering to unblock Packaging Corporation of America\'s workflow.

Additional Initiatives: Dylan built two new artifact template agents in staging, spending the week debugging tool calls and prompt iterations while discovering that requiring company IDs for every tool (without native opportunity-to-company mapping) increases agent failure rates. The no-code agent builder will dramatically improve velocity versus the current vibe coding approach requiring local platform setup. Gabe met with Derek and Tomer reviewing how Plays platform can handle bulk email generation through custom workflows, with Derek sharing video examples of payload-based UI manipulation that Gabe needs time to digest before defining an MVP scope.

**Strategic Challenges**

Adam\'s eval work exposed that GraphQL endpoints are failing 70% of the time for engagement data retrieval---a problem Lauren Cherkis recently joined to analyze through tool call failure reporting. The team didn\'t discover the magnitude of these failures until way too late, highlighting the need for better monitoring and alerting when customers are experiencing degraded agentic capabilities. Victor called for team-wide reporting mechanisms and regular visibility into tool reliability since Workspace inherently depends on multiple teams\' services functioning correctly.

Dylan encountered resistance from the Audience/Studio engineering team on committing to the how-to guide artifact creation epic, with the team citing a large in-progress project preventing timeline commitment. Victor instructed Dylan to share the epic immediately for direct conversation with Snee, recognizing that without committed delivery dates, cross-team dependencies remain effectively blocked. The pattern suggests clearer escalation paths are needed when product requests to platform teams don\'t receive definitive scheduling.

Ant identified that Notes API flexibility is insufficient for mobile requirements, with additional gaps around pipeline view API support blocking native implementation progress. The mobile team made significant front-end advances and completed text-to-speech integration, but addressing workspace backend limitations will be necessary to avoid janky experiences when internal testing begins. The December 1st target for team access remains achievable if backend gaps get resolved quickly.

**Strategic Insights**

**Key Learnings & Discoveries**

Adam\'s system prompt evaluation revealed our agent rarely calls engagement insights tools, instead defaulting to Salesforce queries even when deal risk analysis and call prep should mine conversational data. The root cause investigation with Josh (who built most SDKs) exposed that engagement tools weren\'t designed for the quick insight patterns chat needs, creating both technical failures and architectural mismatches. This discovery explains persistent customer complaints that chat doesn\'t leverage meeting intelligence, pointing toward both immediate tool reliability fixes and medium-term SDK redesign as parallel workstreams.

Victor emphasized during Monday\'s standup that Workspace is winning and losing based on fundamentals---chat quality, views usability, and action layer functionality. The field feedback consistently surfaces these three areas, with people attempting simple workflows that fail too frequently. The team needs hyper-focus on getting these basics right over the next two months to earn go-to-market expansion opportunities, rather than continuing to build advanced capabilities atop unreliable foundations.

Gabe\'s meetings with the Plays team clarified that \"using Plays\" means two different things: customers buying the Plays product versus using the Plays engine for Workspace automation. Victor called for team strategy alignment on whether the Plays engine should be prepackaged with Workspace for features like automated CRM updates post-meeting, noting the need for Dominic-level conversation about product bundling if that\'s the recommended technical direction. The ambiguity is blocking tactical implementation decisions across multiple workstreams.

**Cross-Team Dependencies**

Our work with the Agentic platform team on chat quality improvements continues to be critical for addressing the #1 customer pain point. Lars and Eric are supporting Adam\'s prompt experimentation in Langsmith, with production releases needed to truly eval against real customer data creating dependency on Monday release timing. The team needs better guidance on tool contexts after discovering engagement data was being pulled from incorrect tools, highlighting documentation gaps that slow agent development velocity.

GTM Data Model integration discussions with Andres show high enthusiasm for solving previously intractable problems like write-backs and field access through December POC work. Sean documented that backend capacity is stretched thin due to GTM DM exploration, creating resource tension with chat accuracy improvements that also require senior engineering attention. We need a consolidated requirements document for what Workspace demands from GTM DM, with clarity on how this looks across chat, views, notes, and pulses to avoid fragmented asks.

**Looking Ahead**

Next week centers on Adam\'s Thursday deep-dive presenting system prompt eval results to the full team, with the goal of deciding whether to adopt Caitlin\'s cognitive architecture wholesale or extract specific improvements into our current prompt. This represents the highest-leverage short-term chat quality improvement available, with Victor emphasizing we need to move decisively since fundamentals determine our expansion prospects.

Gabe will share conversation intelligence trend discovery requirements after finalizing them post Adam Smith\'s input, scheduling a group review to formalize design and development kickoff targeting December delivery. Dylan aims to complete three additional artifact template agents using the no-code platform, with eng resources confirmed but November 3rd release timeline at risk due to senior engineer transition. Ant kicks off Pulse engine development with platform teams while moving from prototype to dev-ready designs with Ryan McMaster, targeting the 1/12 release with the top 5 pulse types defined through ongoing stakeholder validation.

Harry presents Legacy Intent to Workbook migration recommendations Friday evening, with executive decision-ready options addressing the 200K limit architectural constraint and 10 feature gaps documented. David continues MCP territory work with Lars to expose definitions into the agentic layer, while finalizing Priority Accounts common API testing and addressing null values in Account Team Member roles before broader release. The team maintains confidence in hitting December milestones while acknowledging backend capacity constraints require careful prioritization across competing platform dependencies.

*Source: Team SalesOS/Copilot Operating Framework entries from Dec. 1, 2025- Dec. 4, 2025*

## **Automation Team Weekly Report - December 5, 2025**

**Executive Summary**

Form builder reaches staging and website tracking launches to production while analytics infrastructure work extends into January. Sam Massie completed DoubleO tool creation deep dive and released form builder to staging with flexible field mapping expected next sprint. Marc Frail deployed website visitor trigger with buyer ID behind feature flag and rapidly addressed missing Snowflake documentation, while beginning Google integration scope analysis. Adam Peretz made significant analytics progress but identified multi-step database migration requirements pushing completion to the second week of January due to holiday timing and infrastructure testing needs.

**This Week\'s Progress**

**Key Momentum Areas**

Marc Frail achieved production deployment of website visitor tracking, launching the new websights trigger with buyer ID behind feature flag under the \"WebSights (Attributed)\" naming. This enables enterprise customers to track website visitor activity with identity resolution, supporting data export workflows that bypass UI interaction requirements.

Sam Massie delivered form builder to staging environment, completing DoubleO tool creation deep dive and handing off connector requirements for dropdown support to engineering. Flexible field mapping is expected next sprint, maintaining momentum toward comprehensive no-code automation capabilities.

Documentation gaps identified and rapidly remediated, with Marc Frail quickly creating and uploading missing Snowflake connector documentation for import and enrichment workflows. This responsiveness to documentation needs demonstrates operational maturity in supporting customer adoption.

**Goals & Progress**

Website Visitor Tracking Launch: Marc Frail completed production deployment behind feature flag, enabling controlled rollout of websights attributed tracking capabilities. The feature flag approach allows validation before broad customer access.

Form Builder and Field Mapping: Sam Massie achieved form builder staging release with flexible field mapping targeted for next sprint. Connector dropdown requirements were handed to engineering, expanding form capabilities for more sophisticated user interactions.

Analytics Infrastructure Evolution: Adam Peretz made significant progress but realistic assessment of database migration complexity, holiday timing, and testing requirements led to the second week of January target. The infrastructure work involves migrating databases across BigQuery locations to enable critical table joins.

**Strategic Challenges**

DoubleO tool creation still requires engineering effort despite no-code vision, with Sam Massie discovering that PM provides description and schema but engineers must write Python wrapper code before PM manually QA outputs. This workflow reveals engineering dependencies that limit the \"no-code\" benefits for internal tool creation.

BigQuery data location constraints complicate analytics, as Adam Peretz identified that two critical data elements reside in separate BigQuery locations that GCP now allows joining. However, achieving this requires multi-step database migration through DevOps coordination with Pat Whitney, including extensive testing to prevent data loss.

OAuth implementation patterns need standardization, with Marc Frail raising questions about how to handle custom query parameters like \"prompt=consent\" and whether offline_access scope is automatically added.

Holiday timing compresses delivery windows, with Adam Peretz noting that upcoming holidays factor into realistic January completion estimates. The constrained timeline affects ability to complete infrastructure work requiring careful testing and validation.

**Strategic Insights**

**Key Learnings & Discoveries**

GCP BigQuery cross-location joins now possible but require migration, with Adam Peretz discovering that while Google Cloud Platform now supports joining tables across data locations, leveraging this capability requires migrating databases to common locations. The migration complexity involves DevOps coordination and extensive testing to ensure data integrity.

Manual QA requirements persist in tool creation, as Sam Massie\'s DoubleO deep dive revealed that despite no-code aspirations, PM must manually QA outputs after engineering writes Python wrappers. This human-in-the-loop requirement affects scaling and suggests a need for automated validation approaches.

Documentation responsiveness supports adoption, with Marc Frail\'s rapid creation of missing Snowflake documentation demonstrating that quick response to documentation gaps enables customer success. The operational pattern of identifying and filling documentation holes prevents adoption friction.

Google integration scope analysis reveals complexity, as Marc Frail begins unpacking required scopes and actions for Gmail, Calendar, Drive, Docs, and Sheets. The analysis across multiple Google services highlights integration breadth needed to support comprehensive tool capabilities.

**Cross-Team Dependencies**

DevOps coordination with Pat Whitney is essential for BigQuery database migration, requiring careful planning and testing to enable analytics capabilities without data loss risks.

Workbooks and audience team collaboration becomes priority for Adam Peretz next week, focusing on prioritizing public-facing APIs and identifying next steps for lighthouse product delivery.

Engineering collaboration continues for Sam Massie\'s field mapping completion work, ensuring forms and flexible mapping capabilities reach production on expected timelines.

**Looking Ahead**

Next week focuses on Google integration unpacking while advancing field mapping completion and initiating audience API prioritization work.

Marc Frail will continue analyzing Google integration requirements, understanding scopes and actions for Gmail, Calendar, Drive, Docs, and Sheets to support comprehensive tool capabilities through the data connector framework. This foundational work enables sophisticated Google workspace integrations.

Sam Massie will work with engineering to drive field mapping to completion, ensuring flexible mapping capabilities reach production. If time permits, he will begin exploring new features for testing connectors, forms, and automations, expanding validation approaches beyond manual PM QA.

Adam Peretz will work with workbooks and audience teams to prioritize public-facing APIs, identifying next steps for making this a lighthouse product delivery. The analytics infrastructure work continues through database migration coordination with DevOps, targeting second week of January completion.

The convergence of production-deployed website tracking, staging form builder capabilities, and advancing Google integration analysis creates momentum for a comprehensive automation platform, while realistic assessment of infrastructure complexity and holiday timing ensures delivery commitments remain achievable rather than aspirational.

*Source: Team 1-2-3 Operating Framework entries from 12/1 - 12/5*

## **Core Data Team Weekly Report - December 1-5, 2025**

**Executive Summary**

John Durst supported the waterfall initiative with a successful demo demonstrating enhanced data enrichment capabilities across the platform. Magnus Herweyer began his onboarding for Contributory Network, rapidly gaining understanding of enterprise data sharing architecture while also facilitating a long awaited important alignment between AI Data Management and Data Engineering on shared services strategy. Heather Ma participated in the full ZI Lite team onsite in Waltham alongside the core data team, achieving strong alignment on the roadmap to close data gaps caused by Swapper.exe deprecation, with outcomes driving initiatives including engagement provider contact data acquisition, email signature ingestion from paying customers, and feasibility assessment for GTM data store user data integration from CRM and Slack systems. She also progressed Deal Insights Agent development by meeting with counterpart PMs to prioritize interface options across homepage Chat, workbook, and worksheet environments. Meanwhile, Cam Fortin secured the M8 timeline for automated new company creation with an end-of-April MVP target, providing engineering teams clear execution roadmap for H1 2025.

**This Week\'s Progress**

**Key Momentum Areas**

John Durst led the waterfall enhancement initiative through successful demo completion, establishing new data enrichment workflows that improve match rates and coverage. The team completed roadmap development for onboarding additional alternative value sources and advanced department technographic capabilities, with proof of concept validation underway. Brandon\'s feedback on technographics investment introduced a strategic reframing - viewing this as a potential \$100M business opportunity rather than just platform enhancement, which shifts the investment approach from technical requirements to market opportunity assessment.

Heather Ma joined the complete ZI Lite team onsite session in Waltham with the core data team, successfully establishing alignment on the plan to address data gaps resulting from Swapper.exe deprecation. The onsite outcomes now shape the coming roadmap across multiple workstreams: continuing contact data acquisition from engagement providers, advancing email signature ingestion from paying customers, and exploring feasibility of user data integration in GTM data store from CRM and Slack sources. The Workspace team will initiate Audience features requiring CRM user data or Slack hierarchy, creating customer value that incentivizes data integration with ZI, while CN develops the legal frameworks and pipelines for ingestion. Her Deal Insights Agent work advanced through meetings with counterpart PMs to understand different surface options---homepage Chat, workbook, worksheet---and determine prioritization for agent shipping and integration across various plays.

Peter Overman achieved significant GTM Store integration progress with contractors, MSPs, and LinkedIn profiles advancing to staging, while SEC filings and Form 5500 data reached production readiness. The successful training of research analysts Austin and Andy on quarterbacking GTM Store integrations establishes sustainable knowledge transfer processes. Ethan\'s analysis of 17M new company candidates identified approximately 1M net new companies for addition, with location tagging infrastructure prepared for immediate processing.

**Goals & Progress**

Platform Strategy & AI Development: Heather Ma participated in the full ZI Lite team onsite in Waltham, working with the core data team to establish clear alignment on closing data gaps from Swapper.exe deprecation. The onsite produced a roadmap driving multiple initiatives: ongoing contact data acquisition from engagement providers, email signature ingestion from paying customers already underway, and feasibility exploration for GTM data store user data including CRM users and Slack users. The Workspace team plans Audience features leveraging CRM user data or Slack hierarchy to provide customer value justifying data integration, enabling CN to build supporting legal agreements and ingestion pipelines. Research into optimal interface delivery for the Deal Insights Agent progressed through meetings with counterpart PMs, evaluating homepage Chat, workbook, and worksheet options to prioritize where to ship the agent and how it integrates across different customer plays.

Data Infrastructure & Quality: Rituparna Das encountered processing challenges with waterfall data enrichment when DIP rules didn\'t function as expected, temporarily delaying ingestion of prepared 5x5 mobile and business email datasets. The team identified untapped FormComplete data containing valuable contact information requiring volume analysis and utilization planning. Non-social location coverage gaps emerged as an area needing attention for contacts lacking Xverum data, prompting engineering assessment and proposal development for Brandon\'s review.

New PM Onboarding & Shared Services: Magnus Herweyer achieved strong initial comprehension of Contributory Network in his first week onboarding as the new CN Product Manager overseeing CN data sourcing, understanding the distinction between enterprise and free customer architectures, integration flows, and competitive dynamics with Swapper.exe. His facilitation of long-awaited shared services\<\> AIDM alignment discussions with Hasmik and Imesh identified the need for dual-approach data normalization - maintaining both customer-configured values and canonical versions to balance GTM Studio functionality with ZI-normalized values in GTM Data Store.

Release Management & Automation: Cam Fortin\'s M8 planning session delivered strong results with Inna\'s structured framework establishing clear milestones toward end-of-April MVP for automated new company creation and new pipeline implementation. This transitions from batch processing with merge to streaming match service architecture. Location updates for January 15 cube may be limited due to analysis resourcing and timing constraints, highlighting need for more strategic quarterly planning for cross-team initiatives. Jody Roberts advanced microapp automation for GTM Dataset onboarding, recognizing that while ZI Chat\'s new agent orchestration capabilities show promise, current throughput gains don\'t justify additional investment until GTM data store infrastructure matures.

**Strategic Challenges**

Coordination gaps between Workflow and GTM Store teams regarding schema alignment created inefficiencies, with workbook teams operating without awareness of schema work completed in Q1. John Durst and Peter identified this communication issue after discovering teams weren\'t collaborating despite working on interconnected systems. Jody is working to improve cross-team coordination after noting customer concerns about progress pace.

Location matching complexities persist with match service encountering difficulties when identifying office locations for companies with multiple child entities in the same geographic area. Rituparna\'s team identified specific scenarios where contacts in St. Paul working for 3M couldn\'t be matched to parent locations due to 200+ child companies creating ambiguity. This requires collaboration with Mike\'s match service team to improve location-based matching logic.

Technographics infrastructure investment requires strategic reassessment as costs increase. Brandon\'s reframing of technographics as a potential \$100M business opportunity rather than platform enhancement necessitates different investment approach and business case development, shifting focus from technical requirements to market opportunity validation.

**Strategic Insights**

**Key Learnings & Discoveries**

Enterprise Data Architecture Evolution: Magnus\'s discovery that Contributory Network splits between enterprise and free customers with different user experiences, legal agreements, and interfaces reveals complexity in data sourcing strategies. The need to balance customer-configured data views with canonical ZI-normalized values for search and entity resolution demonstrates sophisticated requirements for maintaining data integrity while enabling customer flexibility.

Infrastructure Modernization Impact: Cam\'s M8 planning revealed that moving from batch to streaming architecture with match service replacing merge processes represents fundamental platform evolution. The structured milestone approach Inna developed provides template for managing other large-scale initiatives, demonstrating value of clear execution frameworks for complex technical transformations.

Cross-Functional Visibility Gaps: Multiple team members independently discovered coordination failures between teams working on related initiatives. Peter\'s use of ZI Chat to recreate customer use cases from schema to SQL to Snowflake to workbooks demonstrated potential for AI-powered workflow automation while highlighting gaps in team communication that manual processes would have caught earlier.

**Cross-Team Dependencies**

Our work with Analysis team on location processing requires immediate attention as limited resources may prevent location updates from making January 15 cube release. Cam\'s recognition that quarterly-level goals need better definition for initiatives requiring cross-team collaboration highlights systemic planning improvements needed.

The match service integration for new company pipeline critically depends on Mike\'s team achieving company and location matching accuracy. Without successful entity resolution in streaming architecture, the entire automated company creation initiative risks failure, making this collaboration essential for H1 2025 success.

**Looking Ahead**

Next week focuses on resolving waterfall data ingestion issues while advancing shared services architecture decisions and AI agent development that will shape platform capabilities for 2025.

Magnus Herweyer will facilitate alignment meetings between AI Data Management and Data Engineering teams to finalize the dual-approach for data normalization, determining implementation for separate customer-configured and canonical columns. He\'ll continue Contributory Network onboarding with Masha\'s enterprise experience demos while building comprehensive data sourcing roadmap.

Heather Ma will continue meetings with counterpart PMs to finalize Deal Insights Agent interface prioritization and integration strategy across homepage Chat, workbook, and worksheet environments. She\'ll advance execution on the ZI Lite onsite outcomes, coordinating with Workspace team on Audience feature development requiring CRM and Slack user data while working with CN on legal frameworks and pipeline requirements for user data ingestion into GTM data store.

John Durst will advance proof of concept for department technographics to validate investment approach, coordinate the first working example of source onboarding process using new documentation, and continue 2026 planning with expanded stakeholder engagement. Rituparna Das will address DIP rule processing to unblock waterfall enrichment data ingestion, complete FormComplete data volume analysis, and develop proposals for non-social location coverage improvements.

Peter Overman will complete analysis QA for 1M net new companies ahead of January cube deadline while finalizing web data acquisition POC feedback for URL Discovery and WhoIs capabilities. Cam Fortin will draft January 15 release notes acknowledging location update limitations, refine H1 initiatives based on M8 timeline, and establish more strategic quarterly goals for initiatives requiring cross-team coordination.

The waterfall demo success provides foundation for expanded data enrichment capabilities, while shared services alignment and M8 timeline clarity position the team to deliver platform improvements that balance customer flexibility with data integrity requirements.

*Source: Team 1-2-3 Operating Framework entries from 12/01-12/05*

## **GTM Data Platform Team Weekly Report - December 6, 2025**

**Executive Summary**

The team delivered a significant milestone this week: Workspaces is now enabled to consume first-party engagement data through the GraphQL API, establishing the unified pattern for how first-party and third-party data flow into any client. Linda Johannessen was on site for this integration workshop with the Workspaces engineering team, while Menna Rashwan finalized the MVP scope for Federated Search\'s December 31st delivery. The team remains on track for the year-end milestone, though architectural decisions around aggregation logic ownership need resolution next week to define the long-term implementation path.

**This Week\'s Progress**

**Key Momentum Areas**

The enterprise data platform onsite workshop with the Workspaces engineering team validated the end-to-end integration pattern for engagement data through GraphQL. The team worked through heated but productive technical discussions that surfaced edge cases and tightened the modeling and join strategy. Workspaces can now use engagement data for last touchpoint analysis, volume aggregations within timeframes, and filtering views---all through the unified GraphQL API.

Menna Rashwan locked down the December 31st Federated Search scope after extensive validation with engineering and product stakeholders. The MVP now has clear boundaries: engagement use cases are defined and aligned with Sanyog\'s team on the missing data dependencies needed for grouping logic. Both the GraphQL API team and Search team have confirmed their current state can deliver within the timeline, though each faces scaling challenges that require Q1 attention.

Marc Delurgio completed his review of the Data Normalization epics that Linda had drafted, signing off with only minor questions remaining. The epics are ready for broader engineering review with Magnus and other stakeholders next week, putting the normalization pipeline work on track to begin shortly. Moshik Levin is expanding the dataset onboarding process framework that Peter established, working to cover all inbound requests with consolidated trackers and playbooks.

**Goals & Progress**

Federated Search December 31st Delivery: The scope is finalized and the team remains on track despite pushing aggregation and grouping use cases out of scope. These capabilities depend on missing engagement data points that Sanyog\'s team will expose, with Federated Search picking up the implementation work post-December 31st. An architecture conversation is scheduled for next week to determine whether aggregation logic should reside in Solr or BigQuery, which will define long-term ownership and technical direction. The Search team can handle complex queries at any depth, but BigQuery won\'t scale to thousands of requests per second---a problem anticipated for Q2 that needs solving before it becomes operational.

GraphQL API Integration & Scaling: The Workspaces integration revealed both the power and limitations of the current architecture. While the GraphQL API can support arbitrarily complex queries, BigQuery as the backing store won\'t scale for high-volume use cases. Conversely, Solr scales well for volume but wasn\'t designed for deep aggregation and multi-hop joins with aggregation across joins. The team has broad agreement on these constraints, and Linda\'s onsite work with the Workspaces and Search teams advanced shared architecture planning that will reduce future duplication and drive platform convergence. Phase 2 work is underway focusing on scale, stability, and operational readiness for 2026.

Dataset Onboarding Process Expansion: Moshik is ramping up on managing GTM Store dataset onboarding, expanding the trackers and playbooks Peter created to cover all teams and requests. This week surfaced how much coordination is required---Moshik discovered significant gaps in his understanding of the Engagement team\'s actual status and needs. While initially believing extensive onboarding facilitation was still needed, he learned they\'re already live with some data while simultaneously having more coming and reconsidering what\'s already in place. A meeting with Peter this week will clarify the current state and next steps.

**Strategic Challenges**

The architectural decision on where aggregation logic should live---Solr versus BigQuery---needs resolution next week. This isn\'t just a technical implementation detail; it defines long-term ownership between teams and determines how the platform scales for high-complexity, high-volume use cases. Both Linda\'s GraphQL team and Menna\'s Search team have clear perspectives on their respective system constraints, and the decision will likely result in a hybrid approach that plays to each system\'s strengths. The team needs to move quickly on this to avoid blocking Q1 delivery planning.

The December 31st timeline for Federated Search remains achievable but tight. While the MVP scope is now locked, several engagement data dependencies lie outside the team\'s control. Sanyog\'s team must expose the missing data points needed for grouping logic, and any delays there cascade directly to post-December 31st capabilities. The team has built the right relationships and established clear communication channels, but external dependencies always carry risk.

While Peter\'s playbook provides a solid foundation for dataset onboarding, scaling it across all teams requires more deliberate process design. Moshik is addressing this by creating a standardized process for all data producing teams, consolidated trackers, and a unified backlog that will give dataset stakeholders better visibility into onboarding velocity and priorities.

**Strategic Insights**

**Key Learnings & Discoveries**

The Workspaces integration validated a truth that will shape 2026 planning: early integration into consuming applications reveals edge cases that tighten modeling decisions. Linda\'s onsite work exposed specific join strategy issues and data structure assumptions that wouldn\'t have surfaced through design reviews alone. This reinforces the value of getting working code into production environments as quickly as possible, even when some capabilities are still incomplete.

The team discovered through the Agent platform engineers that domain-specific MCPs (Model Context Protocol implementations) are the right architectural pattern rather than trying to build one umbrella MCP. Ryan Stevens\' team built and deployed a GraphQL MCP after dinner one evening, demonstrating both the velocity possible and the value of team-owned MCPs that can be tuned to specific use cases and patterns. This aligns with how documentation works---every team should document their service for agents, not rely on one team to document everything. The notion of an umbrella MCP that routes to specialized MCPs solves the customer discovery problem without forcing centralized ownership.

**Cross-Team Dependencies**

Work with the Workspaces engineering team proved the value of dedicated onsite time for complex integration work. Linda\'s week in Wisconsin compressed weeks of potential back-and-forth into productive, real-time problem-solving sessions. The team should look for similar opportunities in Q1 as other applications integrate with the GraphQL API. The shared architecture work with the Search team is reducing future duplication across both teams and establishing patterns that will accelerate subsequent integrations.

Coordination with Sanyog\'s team on engagement data dependencies is proceeding well, with clear alignment on which data points need exposure and realistic expectations about when they\'ll be available. The relationship here is strong, and both teams understand how their work connects. The December 31st scope explicitly accounts for this dependency by pushing grouping logic to post-year-end delivery, giving Sanyog\'s team the time they need without creating false urgency.

**Looking Ahead**

Next week centers on resolving the aggregation logic architecture decision and driving the Data Normalization work into engineering execution for Q1. The architecture conversation will determine where aggregation capabilities live long-term and define the ownership model between teams. This decision unblocks Q1 planning and removes ambiguity about how the platform handles complex analytical queries at scale.

Linda will continue advancing Phase 2 GraphQL work focused on performance improvements, scalable storage patterns, and clear adoption pathways for new datasets. The team is preparing sequencing for Q1 2026 deliverables while maintaining momentum on the December 31st commitments. Moshik meets with Peter to get fully ramped on dataset onboarding status and will begin socializing the expanded process framework across stakeholder teams. He\'s also shifting focus to location matching to address mounting feedback and relieve pressure on that workstream.

The Federated Search and GraphQL integration work remains the top priority, with both teams executing against well-defined plans. The December 31st delivery is achievable with the locked scope, and the architectural decisions being made now set up the platform for the scaling challenges coming in 2026. The team has built the right cross-functional relationships and established clear communication patterns that turn complex coordination into executable work.

*Source: Team 1-2-3 Operating Framework entries from 12/1/2025 - 12/5/2025*

## **Integrations Team Weekly Report - December 1, 2025**

**Executive Summary**

The team shipped foundational platform capabilities this week that unlock major enterprise opportunities. Prateek Paikray completed implementation guides for the Snowflake and Databricks Audience Export release launching December 9th, enabling customers to export GTM Data Model audiences directly to cloud data warehouses. Sanyog Rai supported the Workspace team\'s onboarding to GTM Data Model by proposing junction tables for engagement data optimizations, allowing downstream teams to query account and contact engagement relationships more efficiently. The engineering and product leadership teams aligned on a scalable GraphQL-first approach for vertical datasets and GTM Data Model Engagement data.

**This Week\'s Progress**

**Key Momentum Areas**

Sanyog Rai collaborated with Solr and data platform engineering teams to design optimizations for GTM Data Store and GraphQL, proposing junction tables between engagements and accounts (account_engagement_role) as well as engagements and contacts (contact_engagement_role). These additions will reduce resource-intensive table scans that currently slow down downstream teams when connecting engagement participants to accounts and contacts, with the optimizations now entering the engineering review phase.

Prateek Paikray delivered a working proof-of-concept for enriching Salesforce lists using Agentforce, demonstrating that users can navigate to a Salesforce list and invoke the agent flow to enrich records directly within Salesforce. This capability addresses enterprise customer demands for AI-driven workflows beyond current offerings, though full deployment depends on Salesforce releasing their Model Context Protocol (MCP) feature, which their business development team is currently delaying.

Andres Perez established a project plan with Dominik and Philip to serve Adobe, ServiceNow, HPE, and IBM using GTM Data Model, GTM Workspace, and unified export functionality. This initiative, branded as \"Workspace Platform Leap\" for 2026 planning, targets 10 million in strategic ACV for enhanced service delivery while simultaneously addressing 30 million in ACV from customers connected to the three supported CRM vendors who could upgrade once their platforms are fully supported in Workspace.

**Goals & Progress**

Cloud Data Shares: Prateek Paikray completed implementation guides for both Snowflake and Databricks cloud data share integrations ahead of the December 9th product release. These guides will enable enterprise customers to configure data exports from GTM Studio audiences directly to their cloud data warehouses, addressing long-standing customer frustration about data that already exists in GTM Data Model but requires cumbersome export flows.

Engagement Data Optimization: Sanyog Rai worked through technical specifications with downstream teams to add ZoomInfo company IDs to the account engagement role table and ZoomInfo contact IDs to the contact and participant engagement role tables. While the Solr team emphasized the primary and secondary ID matching approach should prevent data mismatches, Sanyog is preparing a formal write-up requiring sign-off from Asaf, Rajesh, and MJ to validate this assumption before implementation proceeds.

Vertical Dataset Integration: Product and engineering leadership reached alignment on the scalable approach for integrating vertical datasets with audiences, establishing that GraphQL API delivery must precede UI work. This decision, which also applies to engagement data integration (no BigQuery shortcuts), resolves the confusion from three different teams pulling Prateek in conflicting directions and provides a clear technical path forward for all dataset integrations.

**Strategic Challenges**

ZoomInfo meeting recording imports face a data model challenge where transcript speaker IDs currently use the Chorus person ID, which doesn\'t connect to any entity in the GTM Data Model or Data Store, rendering it unusable for downstream teams. Sanyog Rai identified that the proper solution requires using the participant ID from GTM Data Model, as this would consistently represent every speaker regardless of whether they have a CRM user profile or ZoomInfo contact record. The Chorus engineering team will need to incorporate participant IDs into their transcript generation process, which connects to the broader Chorus-Workspace convergence work scheduled for February 2026.

Integration disconnection notifications are currently limited to service account connections, leaving user-level and no-code marketplace integrations without automated alerts when they fail. Sanyog raised this gap with Prateek, noting that customers experiencing security breaches disconnect service-level integrations but remain exposed through active user-level connections because the system doesn\'t provide unified controls. The team needs to extend the existing notification framework to cover all integration types while clarifying the relationship between service and user-level connections, including implementing automatic disconnection of user connections when service accounts are disabled.

The Cisco iframe solution for exporting companies and contacts from Gong encounters a technical limitation where the SFNA team needs to look up CRM IDs. Prateek proposed getting these from GTM Data Model from the Gong iFrame, which would enable the demo showcasing while potentially accelerating Copilot sales to Cisco. This workaround also reinforces the requirement that all Gong customers must connect their CRM with ZoomInfo for the feature to function correctly.

**Strategic Insights**

**Key Learnings & Discoveries**

Enterprise customers implementing AI initiatives consistently request agent capabilities beyond current offerings, specifically wanting account-focused interactions like \"show me my target account list\" within Agentforce. The team can deliver these capabilities using Model Context Protocol once Salesforce enables the feature, but business development delays on Salesforce\'s side currently block progress. This customer demand validates the strategic direction of building agentic platform capabilities while highlighting external dependency risks.

Salesforce announced that new connected apps and OAuth applications will soon require installed managed packages rather than standalone integrations, representing a significant platform policy shift. While this change doesn\'t affect ZoomInfo\'s existing grandfathered connected apps, it appears designed to increase Salesforce\'s revenue participation in integration ecosystems following recent security breaches at Drift and Gainsight. The team developed a talk track explaining to customers like IBM (who inquired about compliance) that existing connections remain secure and that proxy service offers additional protection without requiring managed package migration.

The vertical dataset integration alignment revealed that the engineering approach of delivering GraphQL APIs before UI implementation creates a more scalable foundation than the shortcuts some teams initially proposed. This architectural decision, which required coordination across product and engineering leadership, prevents technical debt accumulation and ensures consistent data access patterns across all dataset types. The same principle now applies to engagement data, eliminating the temptation for teams to build direct BigQuery connections that would fragment the data access layer.

**Cross-Team Dependencies**

Our work with the Solr team and data platform engineers on GTM Data Model optimizations requires careful validation from Asaf, Rajesh, and MJ to ensure the proposed junction tables with ZoomInfo IDs won\'t create data mismatch scenarios. The Solr team\'s confidence in their primary and secondary ID matching approach needs verification from our engineering team, particularly regarding first-party data scenarios that the Solr team hasn\'t historically considered in their ZoomInfo Global data focus.

The Workspace team\'s platform feature gaps are preventing customer-facing conversations about migrating high-value accounts from Copilot to Workspace-based solutions. Andres is collaborating with Sean and Rakesh through the 2026 planning workshop to identify which missing capabilities must ship before engaging Adobe, ServiceNow, HPE, and IBM about the transition, balancing the \$10 million in strategic ACV upside against the migration friction these customers would experience.

Coordination with the user management team on Chorus-Workspace convergence remains challenging as they prioritize other initiatives. The February 2026 timeline for delivering a Chorus-like experience in Workspace depends on resolving both front-end viewing capabilities and back-end platform work including the switch to Engagement Intelligence (Formerly Advanced Activity Tracking) and participant ID implementation that Sanyog identified as necessary for transcript speaker identification.

**Looking Ahead**

Next week focuses on securing engineering validation for proposed optimizations while advancing multi-CRM capabilities and platform export features. Prateek Paikray will review the High-Level Design Document for multi-CRM that Guy prepared, with the review session scheduled for Monday. This design work shifts focus from the cloud data share project that was originally planned for Q4 based on the 90-day CTO roadmap priorities.

Sanyog Rai will complete the write-up for engagement data optimizations including junction tables and ZoomInfo ID additions, securing sign-offs from Asaf, Rajesh, and MJ before implementation begins. He\'s also working to establish a timeline for querying GTM engagement source records, following up with Majid to clarify the current blockers and delivery schedule. Additionally, Prateek needs to address the two integration infrastructure items Sanyog flagged: extending disconnection notifications to all marketplace and no-code integrations, and documenting the relationship between service-level and user-level connections with clear rules for ignore/block domain configurations and automatic user connection cleanup when service accounts disconnect.

Andres will finalize the Workspace Platform Leap initiative proposal before the 2026 planning workshop next week (though he\'ll be on vacation Tuesday and Wednesday). He\'s also advancing the partner fleet work to create 10,000 generic listings for GTM SaaS companies and accelerate listings for data connectors, with the previously postponed meeting now rescheduled. The team maintains strong momentum on foundational platform work while navigating external dependencies and cross-functional coordination requirements that remain manageable with clear ownership and escalation paths.

*Source: Team 1-2-3 Operating Framework entries from December 1-5, 2025*

## **MCP Tiger Team Weekly Report - December 1-5, 2025**

**Executive Summary**

The team completed several foundational technical milestones this week that advance our MCP infrastructure capabilities. Topher delivered utility tool enhancements and began migration of the GTM Store MCP while Carter completed PubSub work and began end-to-end testing. Zheng created a composite tool proof of concept. The team is positioned to continue tool migrations next week, though we\'re working through SDK limitations around data usage analytics that may require alternative implementation approaches.

**This Week\'s Progress**

**Key Momentum Areas**

Carter completed PubSub work, providing essential infrastructure components for the MCP platform. These enhancements create the foundation for more sophisticated tool interactions and enable better message handling across the system.

Topher successfully completed utility tool enhancements and is working on tools migration and end-to-end testing.

Zheng delivered a composite tool proof of concept, demonstrating how multiple tools can work together effectively. This POC validates our approach to building more complex tool interactions and provides a working model for future implementations.

The team submitted specs PRs for both agents MCP and GTM store MCP, moving these components closer to testing readiness. Zheng made progress on the ZI API MCP migration tool, advancing our ability to transition existing tools to the new architecture.

**Goals & Progress**

MCP Infrastructure Development: The team advanced core infrastructure with completed utility tool enhancements and PubSub functionality from Topher & Carter. End-to-end testing validated system integration points, while the composite tool POC demonstrated multi-tool orchestration capabilities from Zheng. These achievements establish the technical foundation needed for the upcoming migration phase.

Specifications and Schema Work: Specs PRs for agents MCP and GTM store MCP have been submitted and are awaiting the final specs repository update before merging. The team is ready to migrate to the new schema once the repository update is complete, which will standardize how tools are defined and documented across the platform.

Tool Migration Progress: Team is working on completing the migration of existing ZI API tools to the new MCP architecture. It is essential for transitioning our current toolset without manual rework of each individual tool.

**Strategic Challenges**

The team discovered that custom response headers for data usage analytics are not currently supported by the Anthropic SDK. This creates a gap in our ability to track how tools are being used and measure data consumption patterns. The team is exploring alternative approaches to capture analytics data through the SDK, but this may require additional architectural discussions to ensure we can properly monitor and optimize tool usage going forward.

The specs repository update is blocking the merge of submitted PRs for agents MCP and GTM store MCP. While the team has completed their work and submitted the necessary changes, they cannot proceed with migration to the new schema until this dependency is resolved. This is a minor timing issue rather than a major obstacle, but it does affect the sequencing of next week\'s work.

**Strategic Insights**

**Key Learnings & Discoveries**

The team discovered potential to support streaming responses using persistent connections, which could significantly improve the user experience for long-running tool operations. This finding emerged from deeper investigation into the SDK capabilities and wasn\'t part of the original planned work. Supporting streaming would allow users to see progressive results rather than waiting for complete responses, particularly valuable for data-heavy operations.

Team members gained substantially deeper familiarity with the specs repository structure this week through hands-on work with PRs and schema definitions. This knowledge will accelerate future development work as the team better understands how components fit together and where to make changes efficiently.

The team clarified the architectural decision that composite tools will live in the agent platform and be exposed as tools to other systems. This design choice simplifies the overall architecture by centralizing complex tool orchestration logic rather than distributing it across multiple services.

**Cross-Team Dependencies**

The specs repository update remains a dependency for completing the agents MCP and GTM store MCP work. Once this update is available, the team can merge their PRs and proceed with schema migration. This appears to be a straightforward dependency with a clear path forward.

**Looking Ahead**

Next week focuses on tool migrations and consolidating the proof of concept work into the agent platform. The team will transition from building foundational components to systematically migrating existing tools to the new MCP architecture.

With the composite tool POC validated, the team will integrate this capability into the agent platform where it can be exposed as a standard tool interface. Zheng will continue advancing the ZI API MCP migration tool to enable efficient migration of the existing tool inventory. The team will also continue exploring alternative approaches for capturing data usage analytics given the SDK limitations, potentially bringing this topic to broader architectural discussions if needed.

The completion of utility enhancements, PubSub work, and end-to-end testing this week positions the team well to accelerate migration work. As the specs repository update becomes available, the team can quickly merge pending PRs and move forward with schema standardization across all MCP components.

*Source: MCP Tiger Team 1-2-3 Operating Framework entries from December 1-5, 2025*

## **PMM Engine Team Weekly Report - December 1-5, 2025**

**Executive Summary**

The team successfully delivered the first objection handling document with stakeholder sign-offs from Victor and Sneh, marking completion of a foundational enablement tool for GTM Studio and Workspace. Jennifer Scharrer delivered customer-facing messaging for December release highlight features and completed the first draft of an Internal Guide helping sellers understand Workspace\'s positioning in the sales tech landscape. AJ Belen and Jennifer Scharrer supported the Forrester Wave talk track, with Brandon providing positive feedback on readiness. Akshath Dorai finalized AI Action Credits messaging and is preparing the objection handling agent for enablement handoff, while AJ Belen secured alignment with Sneh Kakileti on the use case tool approach, shifting from Studio to ZI Chat for initial development with plans to productize in Q1. The team is now navigating a new weekly early access release cadence for Studio and Workspace that will provide better visibility into product changes but requires adjusted coordination with product management.

**This Week\'s Progress**

**Key Momentum Areas**

Akshath Dorai completed the first iteration of the objection handling document delivery after securing stakeholder sign-offs, establishing a scalable framework for ongoing objection handling support. The document was distributed to the enablement team and marks a shift from static content to more dynamic, agent-powered support tools.

Jennifer Scharrer delivered customer-facing messaging for December release highlight features and completed the first draft of an Internal Guide to help sellers understand Workspace\'s positioning in the sales tech landscape. This positioning work provides the field with strategic context for differentiation conversations. AJ Belen and Jennifer Scharrer supported the Forrester Wave talk track development, with Brandon reporting positive feedback and only minor adjustments needed from Carl\'s review.

AI Action Credits messaging reached final draft status with feedback incorporated from stakeholders, positioning the team to support enablement activation plans. Jennifer Scharrer and Akshath Dorai are coordinating on enablement guidance to ensure effective field distribution of these foundational materials.

The team secured alignment on use case tool development strategy following discussions with Sneh Kakileti. Rather than building in Studio initially due to internal access restrictions around credit consumption, the team will develop a proof of concept in ZI Chat with plans to productize within Studio during Q1 once feasibility is validated.

**Goals & Progress**

GTM Studio & Workspace Enablement: Akshath Dorai is finalizing the objection handling agent with Solutions Consultants conducting testing this week. The agent functionality is nearly complete with troubleshooting focused on consistent Slack message delivery. Once testing concludes, the agent will be handed over to enablement for broader distribution. Additionally, Akshath is refreshing existing objection handling content created by enablement prior to his work, running it through the agent to update materials on Seismic.

AI Messaging & Positioning: Jennifer Scharrer is incorporating final feedback on AI messaging frameworks, with completion expected by end of week. This work includes supporting Akshath on AI Action Credits messaging finalization and developing a V1 platform messaging document. The team is now planning activation and enablement guidance to accompany these messaging assets.

Forrester Wave Preparation: AJ Belen and Jennifer Scharrer supported Forrester Wave talk track development, with Brandon providing positive feedback on overall readiness. Only minor adjustments were needed from discussions with Carl. The rehearsal took place December 5th, with the team maintaining focused involvement given the strong preparation already completed.

**Strategic Challenges**

The team is working through project planning for the use case tool following the pivot from Studio to ZI Chat. Akshath Dorai and AJ Belen need to build out a detailed project plan that includes creating nuanced tables with use case hierarchies, sub-use cases by platform, and persona-specific variations. Jennifer Scharrer suggested exploring whether Russell Levy\'s team could support Airtable integration with chat, given teams already use Airtable and it could accelerate adoption.

Release cadence management is emerging as a coordination area requiring attention. A new weekly early access process for Studio and Workspace means all features will go through internal early access for at least 8 days before potential GA release. Jennifer Scharrer noted the original 24-hour turnaround for LRT ticket feature selection may need adjustment now that Sneh has requested review involvement and questions are arising about feature prioritization decisions. The new process provides better visibility but requires clearer decision-making frameworks around feature selection.

Platform messaging framework development is behind schedule this week, with Jennifer pushing V1 completion to next week. This connects to broader needs around understanding go-to-market flows for AI Context Service launch planning, with meetings scheduled to build that understanding.

**Strategic Insights**

**Key Learnings & Discoveries**

The objection handling agent development revealed complexity in agent task management. Akshath Dorai discovered that when the agent handles multiple responsibilities simultaneously, it becomes inconsistent in executing specific actions like Slack message delivery. This points to the need for thoughtful scoping when building automated tools that balance capability breadth with execution reliability.

The competitive positioning narrative around vendors racing to the bottom on data cost resonated strongly internally, creating the type of energizing response the field needs. This messaging proved effective during RKO discussions and demonstrates the power of clear competitive framing that drives field motivation.

Internal access restrictions for Studio due to credit consumption concerns create real constraints on tool selection for internal GTM use cases. While Studio is the most capable tool for the use case functionality needed, the team must develop alternative approaches that balance functionality with internal cost management, highlighting tension between product capabilities and internal adoption constraints.

**Cross-Team Dependencies**

Our work with Sneh Kakileti on the use case tool revealed important architectural considerations around Studio\'s current capabilities and limitations. Sneh recommended validating the approach in chat first before committing to Studio productization, setting a path for Q1 alignment meetings once the proof of concept demonstrates feasibility. This dependency requires ongoing coordination as the team builds out the project plan.

Product Management teams will need to adapt to the new weekly early access release process, with PMs required to complete demo creation, release notes, and info packs by end of day Tuesday for Wednesday early access releases. Brett Jacobs and AJ Belen are defining what go-no-go decision criteria will look like, which will establish standards for feature readiness and impact assessment.

Enablement coordination continues as a priority dependency, with Emily facilitating Solutions Consultant testing of the objection handling agent and planning distribution strategies. The team is also gathering data on static objection handling document usage in Seismic to establish adoption benchmarks for the new agent-powered approach.

**Looking Ahead**

Next week focuses on completing messaging foundations and initiating customer-facing asset development. With AI messaging frameworks nearing completion, the team can shift toward creating two-pagers and customer-facing materials that translate internal positioning into field-ready content.

Jennifer Scharrer will advance platform messaging V1 completion, document AI Context Service go-to-market flow timelines, and develop the RKO product session outline. She and Akshath plan to collaborate on translating completed messaging frameworks into customer-facing materials. AJ Belen will drive swimlanes documentation to completion and advance H1 planning discussions with Dominik and Adam around AI Context Service launch strategy, including exploration of whether Contact Service and Plays could launch together as a cohesive story. Akshath Dorai will focus on use case tool project planning with AJ to define the technical architecture and data structure requirements.

The team enters next week with strong momentum on foundational work, positioned to shift from internal positioning development toward external enablement and customer-facing asset creation. The new early access release process will provide better visibility into product changes, supporting more proactive launch coordination once initial process adjustments settle into rhythm.

*Source: PMM Engine Team 1-2-3 Operating Framework entries from December 1-5, 2025*

## **Product Ops Team Weekly Report - December 5, 2025**

**Executive Summary**

The team successfully deployed the Voice of Customer tool to a testable state and rolled out the weekly release workflow to the GTM Studio team, marking significant progress in establishing repeatable processes. However, the introduction of Dominik\'s early access release program requires adjustments to our communication and enablement workflows, creating some near-term complexity as we decouple the weekly deployment cadence from customer-facing releases. Brett Jacobs is managing the transition with support from Kristin Gandini and Daniel Kong, while the team maintains focus on automation and tooling improvements that will support both internal and external release communications.

**This Week\'s Progress**

**Key Momentum Areas**

Sam Darcy successfully deployed the Voice of Customer tool to a testable released state with a working micro-app, allowing internal workspace users to retrieve VOC fragments. While current results have built-in limiters due to initial timeout concerns, the polling solution workaround now allows Sam to remove these constraints and return significantly more fragments, dramatically improving result quality for the data team and other high-value use cases.

Kristin Gandini and Daniel Kong collaborated to roll out the weekly release workflow to the GTM Studio team, building on the established process with GTM Workspace. Daniel significantly streamlined the feature info pack release agent based on feedback, integrating it with LRT ticket creation so teams can now access all instructions within the agent itself. This consolidation reduces friction and makes the weekly cadence more sustainable across multiple product teams.

Ken Elwell pivoted strategy on release enablement after discovering fundamental limitations in the GTM Studio scaled email generation approach. Rather than pushing release information to account owners, Ken is now building a pull-based framework that structures roadmap and release items using VOC report categories, allowing sales reps to show the most relevant updates to their specific customers. This approach mirrors the success of the release note agent, which reached 35 unique users in the last release cycle.

**Goals & Progress**

Early Access Release Process: The team is implementing Dominik\'s early access program for GTM Studio and Workspace, which introduces a quality gate between weekly deployments and customer releases. Features will now deploy weekly, turn on internally for opted-in sellers, and remain in early access until passing a go/no-go review approximately a week and a half later. Kristin and Daniel are working through the communication implications, particularly around how internal versus external release notes will be structured and how this decoupling affects downstream enablement. The team has breathing room to work through implementation details since no customer releases are planned until the new year.

VOC Automation: Sam successfully called the Agentic platform from N8N and fixed the final bug in the GTM Studio Voice of Customer report agent, which is now moving through the staging to production approval process. Once merged, the weekly VOC report will be semi-automated, requiring only a form submission to kick off rather than running on Sam\'s local machine. The remaining manual step involves providing a bearer token (ZI access token), as there\'s currently no way to automatically generate this credential. Sam is also adding a description column to VOC results to help Claude better select relevant fragments when generating reports.

Roadmap and Release Framework: Ken aligned with Brett on using VOC report categories as the structural framework for organizing roadmap and release items across Studio and Workspace. The next step is securing alignment from Snee and Dominik, then collecting roadmap items at an appropriate level of granularity to ensure consistency across products. This framework will enable any sales rep to pull the most relevant releases and roadmap items for their customers rather than receiving pushed content that may not fit their specific needs.

**Strategic Challenges**

The early access release program introduces complexity in how the team manages release communications and enablement materials. Right now, the weekly cadence of freeze, feature flag, information gathering, and release to customers is being split into two distinct phases, with internal early access becoming its own milestone. This creates questions about how to handle customer-facing roadmaps when early access releases shouldn\'t necessarily be communicated externally, and how to structure the newsletter and release notes to reflect both internal and external audiences. Brett noted this will require coordination across 13-15 teams and careful attention to how demos and release materials are timed and communicated.

The GTM Studio product has fundamental limitations that prevent the scaled email generation use case from working as originally envisioned. Ken discovered that the tools break when trying to operate at scale, the platform can\'t create the necessary artifacts, and the workflow doesn\'t provide sales reps with the flexibility they need to customize messaging for their specific customers. While these technical constraints led to the pivot toward a pull-based framework, they also reveal gaps in how Studio and Workspace connect for basic release enablement flows. The inability to take release notes, generate personalized relevance summaries in Studio, and push communications through Workspace means sales plays around new releases may not function as intended.

**Strategic Insights**

**Key Learnings & Discoveries**

The team validated that pull-based systems work significantly better than push-based approaches for release enablement. Ken\'s release note agent has grown to 35 unique users precisely because it gives sales reps control over which releases to highlight and how to articulate them to their customers. Reps understand their customer contexts far better than any centralized team can, so providing them with flexible tools to access and customize information yields higher adoption than pre-generated content pushed through Workspace. This insight is reshaping how the team thinks about roadmap and release communication across all products.

The distinction between rapid development velocity and rapid customer release velocity has emerged as a fundamental principle for the early access program. Dominik\'s vision is to maintain very high velocity to early access while deliberately slowing velocity to general availability, ensuring customer-facing releases meet quality standards without rushing. This philosophy changes how the team structures communication and sets expectations, with early access serving as both a testing ground and a way for power users to get the latest features quickly while protecting the broader customer base from immature capabilities.

**Cross-Team Dependencies**

The team\'s VOC tool work has the highest return on investment for Jody\'s data team, given the substantial amount of customer feedback related to data quality issues. Brett plans to start the rollout with John Durst and coordinate with Jody on the appropriate way to introduce the tool to their team. This represents a strategic opportunity to demonstrate value with a team that has clear, measurable pain points rather than attempting broader rollout across groups where the use cases are less mature.

The roadmap and release framework work requires alignment with Sneh and Dominik on both structure and content. Ken needs their buy-in on using VOC categories as the organizing principle, plus their input on the appropriate level of granularity for roadmap items to ensure consistency across Studio and Workspace. This dependency is straightforward but time-sensitive, as Ken plans to send alignment materials and receive roadmap items by Monday to maintain momentum on the pull-based enablement approach.

**Looking Ahead**

Next week focuses on solidifying the early access release process while continuing to refine automation and enablement tools. The team will run GTM Studio through the full weekly release cadence for the first time, providing real-world validation of the process changes and surfacing any gaps in communication or coordination.

Sam will remove the limiters from the VOC tool based on testing feedback, significantly improving the volume and quality of fragments returned to users. The GTM Studio VOC automation should complete its production deployment, moving the weekly report generation from Sam\'s local machine to a more sustainable semi-automated state. Ken will secure alignment from Snee and Dominik on the roadmap/release framework, load the items into the system, and prepare the agent for field rollout. Kristin and Daniel will continue building out the early access flow for both Studio and Workspace while managing the December MCR on Tuesday. The team anticipates surfacing implementation details and friction points as they move through this first full cycle, but the lack of customer releases until the new year provides valuable runway to iterate without external pressure. By year end, the goal is having stable, repeatable processes in place that support both rapid internal innovation and measured, high-quality customer releases.

*Source: Team 1-2-3 Operating Framework entries from December 1-5, 2025*

## **Semantic Data Team Weekly Report - December 1-5, 2025**

**Executive Summary**

The January 15th delivery deadline faces elevated risk due to upstream data dependencies in GTM Datastore. The team discovered that speaker-to-person ID mapping---essential for attributing conversation fragments to ZoomInfo contacts---is missing from the GTM Datastore pipeline. Venkata is negotiating with the Chorus backend team and GTM Datastore team to accelerate the fix, but current estimates push resolution past January. Meanwhile, Jon and Inga delivered a breakthrough on account identification, developing a composite key formula that resolves the long-standing Salesforce-to-ZI-company-ID mapping ambiguity. Development continues on extraction and embeddings pipelines, with Sam and Jun making progress despite token limit constraints.

**This Week\'s Progress**

**Key Momentum Areas**

Account ID Resolution Breakthrough: Jon and Inga completed extensive analysis revealing that Salesforce account IDs are not uniquely mapped to ZI company IDs---a gap that has caused data attribution errors for 8 months. They developed a composite key formula using Salesforce ID, Chorus ID, and ZI company ID to reliably identify unique accounts. A correction script is ready to run over the weekend to validate and remediate current production data.

Batch Processing Redesign: Jun redesigned the embeddings batch processing job to support proper batch splitting and Gemini model integration. The new architecture handles exception cases gracefully by writing failed record IDs to a separate table for reprocessing. This work directly enables the historical data migration to Gemini embeddings and improves pipeline resilience.

Extraction Pipeline Progress: Sam\'s extraction layer is now successfully running in Dataflow and writing to BigQuery. The core pipeline mechanics are operational, with remaining work focused on resolving token limit handling for longer transcripts that cause JSON structure breaks.

**Goals & Progress**

GTM Datastore Integration: The pipeline architecture to consume data from GTM Datastore is designed and ready, but upstream data quality blocks implementation. Venkata has staged raw data ingestion to isolate upstream issues from transformation logic. The team can proceed with development using mock person IDs while awaiting the fix from Chorus and GTM Datastore teams.

Data Validation Framework: Inga is validating the preprocessing tables generated by Venkata\'s GTM2R pipeline. The validation approach samples 10 ZoomInfo tenant calls to verify participant mapping, transcript integrity, and metadata completeness. This systematic validation will catch data quality issues before they propagate downstream.

Production Data Remediation: Jon developed an analysis job to identify and correct problematic account linkages in production. The script will run over the weekend to ensure existing tenants have healthy account-to-engagement mappings, enabling accurate search results across Salesforce account ID, Chorus ID, and ZI company ID queries.

**Strategic Challenges**

GTM Datastore Data Gap: The primary blocker is a missing link in GTM Datastore between speaker IDs and person IDs. Without this mapping, conversation fragments cannot be attributed to ZoomInfo contacts---a core requirement for semantic data. The Chorus backend team estimates a one-week fix, but the GTM Datastore team must then consume those changes, creating a multi-dependency chain. Venkata is pushing for upstream teams to prioritize this defect given the January 15th deadline. The team has identified a potential path forward: replacing speaker IDs with ZI person IDs directly, which aligns with the canonical identity model.

Account ID Fill Rate: Analysis revealed that 50-70% of ingested engagement records lack a ZI company ID, severely limiting the ability to associate conversations with accounts. This upstream gap from Chorus means engagements often arrive with only Salesforce IDs or Chorus IDs, without the ZI company ID needed for accurate account-level intelligence. Jon is adding logging to quantify the fill rate precisely, which will inform the defect ticket to Chorus.

Token Limit Constraints: Sam identified that longer transcript extractions hit the 8,000 output token limit, causing JSON responses to truncate mid-structure and fail BigQuery writes. The team is investigating whether this is a hard model limit or a configurable parameter. Resolution is needed before the extraction pipeline can handle production-scale transcripts reliably.

**Strategic Insights**

**Key Learnings & Discoveries**

The assumption that Salesforce account IDs uniquely identify companies was incorrect. This has been causing silent data quality issues for 8 months. The discovery emerged from testing validation when the same Salesforce ID appeared mapped to different ZI company IDs. Root cause: Salesforce IDs can represent personal accounts or shared accounts used across multiple companies. The fix---a composite key approach---is now well-defined and ready for implementation in the new pipeline.

Testing environment coordination requires improvement. Multiple incidents this week involved testers using incorrect tenant IDs or testing against the wrong environment, triggering escalations that pulled engineers into late-night debugging sessions. An API to validate tenant existence has been available for months but isn\'t being utilized. Better logging and clearer error messages at each stack layer would prevent these false alarms.

The team\'s strategy to isolate upstream data issues from application logic is proving valuable. By staging raw data first, then transforming, the team can clearly attribute failures to either upstream data quality or transformation bugs. This architectural decision enables parallel progress: development continues with mock data while upstream fixes are negotiated.

**Cross-Team Dependencies**

Collaboration with the Chorus backend team and GTM Datastore team is essential for the January delivery. Venkata met with Majid and the Chorus team this week to negotiate data structure changes. The proposed fix---replacing speaker ID with ZI person ID---aligns with the canonical identity model and would benefit multiple consumers. Rowan and Venkata will follow up to escalate and align stakeholders on priority.

The QA team\'s testing approach needs coordination. Invalid test data and incorrect environment targeting have caused unnecessary production incident responses. Establishing a shared understanding of valid tenant IDs and environment configurations would reduce noise and allow engineers to focus on actual issues.

**Looking Ahead**

Next week focuses on two parallel tracks: resolving upstream blockers and continuing pipeline development. Venkata will escalate the GTM Datastore data gap to ensure appropriate urgency given the January 15th deadline. Jon\'s correction script will run over the weekend to validate production data integrity, with results informing Monday\'s planning.

Sam will resolve the token limit issue in the extraction pipeline, either by increasing the output token limit or implementing chunked processing for longer transcripts. Jun will complete testing on the batch processing redesign and prepare for the historical embeddings migration. Inga will finish data validation on the preprocessing tables, providing a green light for downstream consumption once upstream data is available.

The team remains confident in delivering the core functionality, but the January 15th date depends on upstream teams prioritizing the speaker-to-person ID mapping fix. Rowan will work with leadership to ensure this dependency is visible and appropriately escalated.

*Source: Semantic Data Team 1-2-3 Operating Framework entries from December 1-5, 2025*

## **ZIM Team Weekly Report - December 1, 2025**

**Executive Summary**

Forrester scored us with 5 in Data, Fit Modeling, Anonymous Audience Segmentation, leads & contact segmentation and others. Forrester scored us unfavorably in some areas---1s in community, self-service, reporting/analytics, and agents---with our response due Monday. This competitive vulnerability comes as Hillary Marks departed, leaving analyst relations without a lead. Meanwhile, a major legal concern emerged: California consent requirements for device-to-person ID linking could severely hamper visitor resolution, affecting websites, intent, and all downstream consumers. Hannah is writing a risk assessment, but Matt correctly identified this as a significant issue that needs immediate attention, not a \"small side issue.\" On the positive side, we\'re making progress on Freewheel (SOC 2 report expected next week) and architectural decisions that route 7 billion daily intent records directly to GEB instead of overwhelming GTM Store. Identity partners Self Service workflow has also completed E2E testing and ready for the first partners to onboard.

**This Week\'s Progress**

**Key Momentum Areas**

Shuxin Yang resolved the GTM Store data volume crisis through architectural redesign. Instead of sending 7 billion daily intent records to GTM Store, the team will send deltas directly to Global Event Bus while making data available to other apps via GraphQL with federated search. This pragmatic solution preserves scalability without the crushing cost implications while Shuxin explores whether intent should be part of the federated search initiative. The intent roadmap first draft is complete, focusing on higher quality intent, self-serve capabilities, and expanded topic coverage.

Jesse Miller achieved impressive agent orchestration progress with just 6-8 hours of prompt refinement work. The agent demos are 90% recorded locally and waiting for Troy\'s merged PR deployment to staging for broader team interaction. The team has established a solid timeline targeting January customer-facing release for open beta with feature-flagged sub-agents. Jesse worked with Nilesh on a 5-milestone roadmap and is securing Andrew as an additional resource. The DeltaX call for LinkedIn campaign management revealed many required endpoints already exist, with V1 designs expected from Sylvia by the 10th.

Matt Barnes progressed critical infrastructure work with form complete and websites data now flowing to GTM Store in staging (one fix away from production). However, the gap analysis on workbooks integration revealed the fundamental blocker: signal workbooks currently only support website buyer ID, missing the 97% of identifications that are company-level. This validates the concerns raised last week about workbooks not being at parity with websites capabilities and underscores why the Dominik clarification meeting tomorrow is essential.

**Goals & Progress**

Freewheel Partnership Advancement: Aadhi delivered the log-level requirements for legal review---checking off 1 of 5 remaining blockers. The SOC 2 report should be available week of 12/18, removing another major hurdle. Anwar Mai to email David Madrid as a heads-up before legal approaches with contract additions. This partnership is finally moving toward a signing date after weeks of compliance delays.

Intent Data Architecture & Legal Challenges: Shuxin finalized the GEB direct integration approach and completed the first intent roadmap draft. Persona intent data will be available by end of quarter with apps leveraging it in Q1. However, legal raised a critical California consent issue: linking device IDs to person IDs without guaranteed user consent creates risk for websites, intent, and all data consumers. Hannah is preparing a risk profile with mitigation options. You suggested exploring persona-level reporting (job title/function) instead of person-level as a potential workaround---similar to how LinkedIn, Sixth Sense, and Demandbase handle this. Legal\'s response was that if identification happens at person level first, then aggregating to persona still violates consent requirements.

Agent Platform Development: Jesse\'s orchestrator work is 90% complete pending Troy\'s deployment. Troy is shifting focus to the MCP server while Jesse handles prompt refinement and orchestration. Email notifications remain frustratingly close to completion---Jesse reached out to Connor expressing that engineering needs to take ownership since he\'s given extensive requirements and is the only one pushing it forward. Late-night responses from Israel aren\'t sustainable. Andrew joining as an additional resource should help accelerate agent work.

Webhook & Signal Aggregation: Matt\'s signal aggregation work is staging-ready pending one production fix. The robust user session management needed for GTM Plays requires a separate aggregation service---Monday\'s architecture meeting with 00 and Carlos should finalize the technical direction. Once complete, everything necessary for GTM Plays website journey signals will be delivered. Webhook delivery meeting moved to Thursday (Israel availability issue) to secure commitments from NOM, CDC, and Global Event Bus teams for productizing the solution IBM needs.

GTM Config & Planning: Aadhi completed the document on expanding GTM config through public contribution and made important ICP/AFS future decisions. All schemas now include token input/output for AI credit consumption calculation. User settings versus admin settings relationship remains unresolved and rolls to next week. Zoom roadmap and ICP/buying group migration are next week\'s focus.

Workbooks Integration Gap Analysis: Matt started the gap analysis document with meetings scheduled for tomorrow including your workbooks clarification session with Dominik. The immediate discovery: workbooks only support website buyer ID (3% of identifications) versus the 97% company-level identifications that websites UI handles. Significant work required to reach parity, confirming last week\'s concerns about premature commitments.

**Strategic Challenges**

The Forrester scores expose competitive vulnerabilities that directly threaten our market positioning. Scoring 1s in community, self-service, reporting/analytics, and agents while competitors presumably score higher validates customer feedback about ZIM\'s limitations. With Hillary Marks gone and no analyst relations lead, Ben and you are scrambling with a contractor to craft a response due Monday. This isn\'t just optics---these are the exact areas where customers churn, including the \$500K we lost to Sixth Sense. The self-service gap particularly stings given it\'s on the roadmap but not delivered.

The California consent issue could fundamentally break visitor resolution and persona intent---our key differentiators. Matt\'s reaction (\"that\'s a significant issue, not something we should view as a small side issue\") captures the severity. California represents massive customer concentration and data volume. If we can\'t guarantee consent for device-to-person linking, filtering out California residents would severely hamper resolution rates. The challenge is that competitors like LinkedIn, Sixth Sense, and Demandbase provide persona-level reporting, suggesting they\'ve solved this. Hannah\'s risk assessment needs to include concrete competitor analysis and viable mitigation paths beyond just \"don\'t identify California residents.\"

Adobe went radio silent after missing the November 30th target date during Thanksgiving week, leaving relationship management in limbo. Worse, the Adobe Analytics websites integration delay (pushed from 9th to 16th) put a \$100K NetApp deal at risk because sales committed to the integration without engineering confirmation. Ravi Shwarma intervened saying beta launch would save the deal, but this reveals a broader pattern: sales over-committing on unconfirmed timelines, especially in Q4. You correctly flagged this as a learning opportunity for account management---they need to understand engineering priorities (Ganesh was pulled for identity partners work) and get proper contingency visibility.

**Strategic Insights**

**Key Learnings & Discoveries**

The workbooks gap analysis immediately revealed that 97% of our identifications (company-level) aren\'t supported by signal workbooks, which only handle website buyer ID. This fundamentally validates the confusion from last week---bringing workbooks into our UIs would require massive feature parity work that workbooks doesn\'t have on their 2026 roadmap. Tomorrow\'s Dominik meeting needs to surface whether he understands this constraint or expects us to build it. If the vision is \"workbooks becomes the spreadsheet UI for all ZIM data,\" then someone needs to commit engineering resources to close that 97% gap.

Design resource constraints are becoming a blocker across initiatives. Sylvia, Yoav, and Megan stated they won\'t work on Zoom projects, forcing you to add David Chan to tomorrow\'s meeting to secure alternative resources. Jesse needs Sylvia for LinkedIn campaign management (V1 by the 10th), and Shuxin needs design support for the intent roadmap. This isn\'t about individual designers---it\'s systemic deprioritization of ZIM in resource allocation. If design leadership views ZIM work as lower priority than other initiatives, we need executive intervention or formal reprioritization.

The 2026 planning exercise revealing actual ad spend will create \"sticker shock\" according to you---TradeDesk, OpenX, Sovereign, LiveRamp costs aren\'t trivial. However, the 40% blended margin justifies the investment. This needs clear articulation in planning materials: these aren\'t discretionary expenses but cost-of-goods-sold for maintaining the platform that generates those margins. Christine Ward and planning stakeholders need the business case framed as margin preservation, not just spend increase.

**Cross-Team Dependencies**

The webhook delivery now depends on CDC, Global Event Bus, and NOM team commitments that Thursday\'s meeting must secure. Matt\'s done his part getting data into GTM Store, but productizing for IBM and identity partners requires cross-team coordination. The domain verification issue for identity partners (needing setup before using webhook) adds another layer---you\'re pushing to rethink domain restrictions entirely, potentially using AI for validation or BigQuery staging zone scanning as Aadhi and Ganesh suggested.

Tomorrow\'s architecture meeting with 00 and Carlos for user session aggregation service is critical for unblocking GTM Plays. This isn\'t Matt\'s decision alone---it requires architectural alignment and resource commitments from platform teams. The meeting represents the final piece for delivering everything GTM Plays needs for website journey signals.

The California consent legal issue affects every team consuming visitor data---websites, intent, forms, identity partners, downstream analytics. Hannah\'s risk assessment needs distribution to all stakeholders, and the mitigation strategy requires coordinated product decisions about whether we\'re willing to filter California residents, pivot to persona-level aggregation, or pursue some other approach. This can\'t be solved in silos.

**Looking Ahead**

Monday is critical: Forrester response is due, requiring weekend work to finalize with Ben and the contractor. Tuesday brings the pivotal Dominik meeting clarifying workbooks integration vision---bring the gap analysis showing 97% of identifications aren\'t supported to ground the conversation in technical reality. The 00/Carlos architecture meeting Monday should finalize user session aggregation direction.

Jesse continues agent development with Troy focusing on MCP server deployment to get staging environment interactive for broader team testing. Email notifications need Connor\'s intervention to get engineering ownership rather than relying on late-night Israel responses. LinkedIn campaign management advances with V1 designs due the 10th from Sylvia (pending David Chan\'s success securing design resources).

Aadhi completes Zoom roadmap early week and tackles ICP/buying group migration. Matt\'s Thursday webhook meeting with NOM/CDC/Global Event Bus teams must secure delivery commitments for IBM and identity partners. Freewill signing should advance with SOC 2 report arrival and legal review of Aadhi\'s log-level requirements.

R&D 2026 planning is scheduled next week---come prepared with the ad spend business case framed around 40% blended margin preservation. Hannah\'s California consent risk assessment distribution and team discussion about mitigation approaches needs scheduling. The design resource issue requires resolution before it blocks multiple workstreams further.

*Source: Team 1-2-3 Operating Framework entries from December 1-5, 2025*

## **Provisioning & Login Team Weekly Report - December 1, 2025**

**Executive Summary**

The primary focus this week was preparing for monetizing third-party data and setting the final requirements for Records Under Management and Data Credits. The most critical item for executive awareness is the unclear strategy regarding data credit consumption when ZoomInfo data is processed and exported via LLMs (Large Language Models), which requires an immediate position to prevent revenue leakage and clarify data ownership. The team is ready to release user management UI/UX upgrade and intelligent username deduplication logic to streamline user provisioning for paid accounts and reduce support calls.

**This Week\'s Progress**

**Key Momentum Areas**

Third-Party Data Monetization Planning: Initial conversations with Mark Harris were started regarding better price control for data credits, which is foundational for supporting third-party and vertical data sets. This timing is especially relevant given the price control and margin visibility we have with AI Action Credits.

Username Collision Resolution: The intelligent username deduplication logic is ready for release to automate the process of making usernames unique in inactive tenants, resolving a long-standing complication with user setup that often resulted in support calls when trial users transitioned to paid accounts. This will improve the onboarding experience and reduce support overhead.

User Management UI/UX Upgrade Preparation: The team is on track for the release of the upgraded user management UI/UX. Artifacts were created to support internal/customer facing teams, including details on the above parallel release of username collision logic.

**Goals & Progress**

User Provisioning & Experience: The high-leverage goal of supporting enablement and signing off on QA for the upgraded user management experience and the release of username collision logic is nearing completion. The enablement team and knowledge center documentation are being updated. The immediate UI improvements include introducing filtering for role and seat type, with fast-follows planned for filtering on subscription and last login.

Records Under Management & Data Credits: Work continued on the PRD (Product Requirements Document) for Record Center Management and Data Credit. The focus has been working with Prateek on third-party data sets to allow for monetization. This effort is currently waiting on final requirements from Brendan Tucker regarding the system to sell data directly, similar to the Clay model, which he plans to finish during the offsite next week.

Third-Party Data Strategy: A significant effort was dedicated to understanding the requirements for reselling other customers\' data through our system (like Clay) and creating the necessary monetization/attribution framework using data credits and records under management. This is currently an open question requiring executive input.

**Strategic Challenges**

The single most pressing challenge is the undefined policy for data credit usage in LLM-generated assets. Currently, a data credit is charged when data leaves the system via CSV or CRM export. However, when ZoomInfo data is used to generate a new asset (like an account summary or a buying group list) through an LLM, and that end asset is subsequently exported, there is no established pattern for charging data credits for the privileged information contained within. This requires a broader conversation on what \"leaving our system\" looks like in the context of AI-driven feature creation to prevent revenue gaps.

A second challenge is the blind spot regarding the technical implementation of reselling third-party customer data through ZoomInfo. This involves creating a system to attribute and pay the reseller based on a \"record sold\" calculation using data credits and records under management. Follow-up is required with Brandon Tucker, Mark Frail, and Andres to define this critical system.

**Strategic Insights**

**Key Learnings & Discoveries**

The rise of LLMs challenges the existing data ownership model: The current model charges data credit for direct exports. The emergence of AI-generated assets, like a buying group created through a \"play\" that includes contact information, means that the privileged data is leaving our system indirectly through an asset export. This highlights that the concept of data leaving the system needs to be redefined to include AI-inferred assets, which must also incur a data credit charge upon export.

The user management UI/UX was long overdue for modernization: The user management UI had \"not been touched in many, many years\", making the introduction of filtering on role and seat type, plus the modernized fly-out modal for user editing and creation, an immediate, high-value improvement for admins.

**Cross-Team Dependencies**

Our work on the user management experience with the CS (Customer Success) and Support teams continues to be critical for ensuring a smooth launch. The enablement materials and documentation also require coordination with the knowledge center team and enablement team to ensure all customer-facing and internal teams are aware of the changes.

The ability to finalize the Records Under Management and Data Credits requirements is dependent on receiving the finished requirements from Brendan Tucker regarding the new system to sell data directly through ZoomInfo.

**Looking Ahead**

Next week will be entirely focused on the Plays planning session and defining the core architecture for monetization.

Top priorities for the coming week are:

Finalizing Requirements: Utilizing the planning offsite to get the final requirements for Records Under Management and Data Credits. This includes uncovering the blind spot for how to sell third-party data through ZoomInfo.

Plays Workshop: Supporting the planning workshop focused on \'Plays\' to help internal teams understand how we charge for AI, the infrastructure of the AI credit system, and how to think long-term about AI credit consumption and revenue generation. This includes a scheduled follow on with Plays team to create a framework for credit consumption and data ownership.

Non-Play Item Planning: Ensuring that critical non-play items like Project Soul, login improvements (including biometric multi-factor), and SKIM improvements are correctly counted and planned during the session.

*Source: Provisioning & Login Team 1-2-3 Operating Framework entries from December 1, 2025*
