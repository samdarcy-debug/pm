---
id: synthesis-2025-50-2025
title: "Product Executive Intelligence Brief - December 12, 2025"
type: synthesis-report
status: approved
created: 2025-12-12
updated: 2026-01-06
week_ending: 2025-12-12
reporting_period: "December 8-12"
tags: ["weekly-report", "synthesis", "Q42025"]
---

*Synthesized from 15 team reports: Integrations Team, Provisioning & Login Team, Automation Team, Business Intelligence Team, Core Data Team, Data Executive Team, GTM Data Platform Team, GTM Studio Team, GTM Workspace Team, Intelligence Team, MCP Tiger Team, Product Ops Team, Semantic Data Team, ZIM Team, PMM Engine Team*

*For detailed questions about any item below, reference specific team reports or contact team leads directly.*

## **Executive Summary**

### **Roadmap Priorities**

In order to stay aligned and focused on the top priorities, see below for the most important work we've aligned to for this month and next.

![](C:\Users\DanielKong\pm\weekly-reports\synthesis\media/media/image1.png){width="6.584830489938757in" height="4.976653543307086in"}

### **AI Credit Consumption**

Given the importance of driving customer AI Action credit consumption, we will be reporting this each week.

![](C:\Users\DanielKong\pm\weekly-reports\synthesis\media/media/image3.png){width="7.713542213473316in" height="4.284273840769904in"}![](C:\Users\DanielKong\pm\weekly-reports\synthesis\media/media/image2.png){width="7.713542213473316in" height="4.371007217847769in"}

### **Summary of blockers**

Summary of blockers across team reports. For more information, use the navigation bar to look into individual team reports in the appendix.

+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Challenge/Topic**                                            | **Specific Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM Data Store Dependencies Blocking January 15th Delivery** | **Intelligence Team:** GTM Data Store dependencies are preventing semantic data pipeline completion and threatening the January 15th plays launch timeline. Chorus engagement data currently contains Chorus company IDs instead of Chorus person IDs (Sanyog\'s team estimates one week for backfill), and tables lack proper sorting/partitioning (forcing expensive full-table scans of 150GB datasets on every query). Rowan Bailey noted that even with these blockers resolved, the team cannot yet commit to the January 15th date because \"nothing can go wrong\" for the timeline to hold.                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                | **Semantic Data Team:** The GTM Datastore integration presents two infrastructure hurdles. First, the data is partitioned only at tenant level with no temporal partitions or clustering, meaning every query for incremental updates (e.g., \"new meetings since yesterday\") requires scanning 160GB of data - expensive and slow. Second, the GraphQL API that GTM recommended for new data uses user-level authentication tokens rather than service-to-service credentials, making it infeasible for the pipeline. Venkata has raised both issues with Majid and Sanyok, and the teams are actively working on solutions.                                                                                                                                                                                                                                                   |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                | **ZIM Team:** The meeting with 00 revealed they\'re not building the session aggregation service we were counting on. Matt\'s team is back on the hook for creating definitive visitor session end states in GTM Store. This is critical infrastructure for plays in Q1. Matt is scrambling to fine-tune requirements today, tomorrow, and early next week based on known technical direction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Holiday Timeline Compression for January 15th Plays Launch** | **Intelligence Team:** The holiday timeline presents the primary execution risk for the January 15th launch. Ryan Stevens laid out the calendar reality: with most of the company out from December 22nd through January 5th, the team has effectively three full working weeks, not five. To manage this, all work must be 100% known, assigned, and divide-and-conquer ready by December 22nd, enabling asynchronous execution with minimal cross-team coordination during the holiday period. This means the team needs to frontload all major decisions and dependencies into the next 10 days, with engineers immediately moving into heads-down execution mode and being kept out of all non-essential meetings.                                                                                                                                                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **API Contract and Cross-Team Coordination Dependencies**      | **Intelligence Team:** The Pulses API contract remains unavailable from Ant and Nebo\'s team, blocking both Derek Osgood\'s plays implementation and Carlos Nunez\'s work on next best action, Deal Acceleration Sync, and other initiatives. Without this API, there\'s no end-to-end steel thread demo possible in the two weeks before January 15th, eliminating the burndown period entirely. Adam Smith committed to chasing this down immediately after the meeting to understand what help Anne needs and to make him aware of the multiple teams waiting on this dependency.                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                | **GTM Studio Team:** The team needs to resolve two architectural dependencies for agentic audiences to progress. First, semantic query integration requires alignment on how the semantic service will function as a tool within Plays infrastructure now that audience chat is migrating to Plays. Second, the interaction pattern between data processing pipelines and Plays for enrichment workflows needs clarification, specifically how Plays will serve as the engine for operations like web research that currently run through separate pipelines. Jagannath is working with Carlos, Tushar, and Umesh\'s teams to align on the final technical approach.                                                                                                                                                                                                             |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Tool Reliability and Context Window Management**             | **GTM Workspace Team:** Tool reliability is impacting artifact development velocity across Dylan\'s templates. Context window limits hit immediately when the deal status agent attempts to query even a small number of deals, and basic operations like retrieving opportunity IDs from views fail inconsistently. Adam is tracking consistent failures in engagement and transcript tools through a Tiger team with Lars coordinating tool owners. The team is exploring purpose-built tools for core use cases as an alternative to generic tools, and Eric is developing a Salesforce sub-agent to reduce context bloat. Victor noted that 00 is experiencing similar challenges and is wrapping multiple tools into single tool calls, suggesting a pattern the team should consider.                                                                                      |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Legal and Compliance Risk Decisions**                        | **ZIM Team:** The California person-level intent legal memo forces an uncomfortable business decision. Hannah\'s assessment confirms California\'s strict laws create risk if we provide person-level intent without guaranteed consent. The question is stark: do we restrict person-level intent functionality in California, or do we accept the legal risk? This isn\'t theoretical - many tech companies are California-based, so restriction would significantly diminish the feature\'s value to our core customer base. This needs Ali and Dominik\'s executive decision on risk tolerance. Person-level intent is a key differentiator versus competitors, so restriction could hurt competitive positioning while accepting risk could expose the company legally.                                                                                                     |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Customer Data Deletion Process Gap**                         | **Integrations Team:** Sanyog Rai discovered we lack a holistic customer data deletion process that handles tenant churn, GDPR requests, and surprise data discovery scenarios consistently. Deletion requests continue to be handled ad hoc, with maturity differing significantly between CRM data and engagement data. Current deletion is manual and fragmented, with Chorus handling engagement deletions but no automated connection to the GTM data model. Sanyog is drafting requirements for an orchestration service that can handle deletion by tenant ID or individual identifiers and propagate events across storage layers, but needs a product owner from Mark Delurgio\'s Data Platform team to own the service itself since this is fundamentally a platform capability that should send Global Event Bus signals to cascade deletions across all data copies. |
+================================================================+==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+

### **Relevant context across reports**

This section surfaces relevant information from team reports across the organization relevant to the given domain area.

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Domain Area & DAI**             | **Cross-Team Dependencies & References (from OTHER team reports)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM Studio (Sneh)**             | **Intelligence Team:** Derek Osgood delivered the first wave of critical tools for plays, with CRM updates, email, Slack, Outreach, and SalesLoft integrations live in MQA and testing well. The routing tool remains the only outstanding component, and rate limit testing suggests no blocking concerns.                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Automation Team:** Sam Massie achieved engineering alignment on field mapping MVP, coordinating core and app teams around a simple implementation scope that demonstrates ZoomInfo as an open platform for destinations, exports, and enrichments. The alignment establishes clear POC requirements with engineering design sign-off from both teams. Audiences emerge as primary 2026 value drivers, with Sam Massie identifying that bringing more and better third-party enrichments into audiences delivers greater customer value than automation-focused capabilities in early 2026 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **GTM Workspace Team:** Hari delivered the topic migration toolkit to Data Services this week, cutting customer onboarding time from competitor platforms (6sense, Demandbase) from two days to two minutes. The toolkit enables bulk keyword-to-topic mapping that Data Services will now own for pre-sales and customer onboarding scenarios, removing a significant bottleneck in competitive displacement deals.                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **PMM Engine Team:** AJ Belen achieved the week\'s primary objective through yesterday\'s productive conversation with Dominik, Adam, and Rowan about go-to-market flow. The discussion provided sufficient direction to proceed with ELT-level planning next week, enabling other teams to begin their necessary preparation work. Jennifer drafted the ELT slides overnight while the information was fresh, though AJ has not yet reviewed them.                                                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Copilot Workspace (Victor)**    | **Intelligence Team:** Lars Vedo\'s engineering team achieved breakthrough performance improvements. Eric White built a sub-agent for the Salesforce MCP tool that reduced context window bloat by approximately 70%, and the team successfully implemented Human in the Loop functionality now running in production (not yet surfaced to users)                                                                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Business Intelligence Team:** The GTM Workspace Analytics Agent continued progressing toward operational usefulness. AJ Belen and Phoebe Mei advanced agent behavior, usability, and onboarding expectations, enabling internal stakeholders to increasingly use Workspace as the default entry point for BI questions and utilization reporting.                                                                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **ZIM Team:** Anwar identified the need to make Victor\'s responsive marketing agent (from workspaces Tiger team with daily stand-ups) available for chat integration - Jesse confirmed they can just call the sub-agent classes                                                                                                                                                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Integrations Team:** Strategic customer requests for GTM account role restrictions, view generation, and ServiceNow CRM support are being evaluated through Andres Perez\'s collaboration with Arelai. The team is quantifying delivery timelines and engineering effort for both Workspace and Copilot Enterprise paths, preparing data that will inform sales conversations about the 4-5 month delay impact to other roadmap items if pursued in the legacy platform.                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM AI Context Service (Adam)** | **MCP Tiger Team:** Carter Vanhuss stood up the Data API MCP server, establishing the foundation for migrating lookup, search, and enrich tools from their current location into a normalized architecture. This server completes the fifth base-level MCP server in the platform and enables consistent tool access patterns for the agent platform                                                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Automation Team:** Developer portal duplication for MCP applications requires detailed requirements, as Adam Peretz identified the need to work with Rowan Bailey on identifying requirements and trade-offs for enabling OAuth-based MCP application registration and management                                                                                                                                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **PMM Engine Team:** Jennifer Scharrer completed the Context Service/Flow download session yesterday, significantly improving the team\'s understanding of the product direction. She drafted ELT slides immediately following to support next week\'s executive conversation, creating momentum for cross-functional activation before the holiday break.                                                                                                                                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Data (Brandon)**                | **GTM Data Platform Team:** Moshik Levin worked with the Company Data team to resolve accuracy results for the new Company Master Data API, specifically around match reasons and scoring distributions. The team now awaits bug fixes from the company data team before engaging Data Services to test and validate the corrections. This work directly supports the January 15th GA release timeline and ensures customers see consistent, explainable match quality                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Automation Team:** Adam Peretz advanced Company Master API modernization, completing initial review confirming the orchestrator meets requirements for replacing legacy EverString connector. The lift-and-shift effort enables Match Service to deprecate old functionality while progressing toward incorporating Company Master data into a unified company database.                                                                                                                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Platform (Ali)**                | **Intelligence Team:** Marjud\'s GraphQL schema changes in GTM Store continue to cause downstream tool failures. Rowan Bailey reported that while some breaking changes were resolved this week, new ones emerged, causing tools built on MCPs to suddenly break. Lars Vedo emphasized the painful downstream impact: \"The field just changed name or something, and it impacts so much.\" Marjud has spun up a new communication channel to announce changes in advance, which should help, but the team needs more robust handling of breaking changes and upgrades.                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Semantic Data Team:** Venkata has surfaced significant GTM Datastore partitioning and authentication issues to Majid and Sanyok, who are actively working resolutions - these must be resolved before the new pipeline can go live in January.                                                                                                                                                                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Integrations Team:** Sanyog Rai advanced the new engagement junction table requirements and identifier-based processing requirements, which will optimize how engagement data flows to downstream teams. While discussions with the solar team continue, the requirements are nearing sign-off and position the team to better handle the growing focus on engagement data across the organization.                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Provisioning & Login Team:** The finalized approach for AI credit overages will add complications to the credit charging service. This complexity requires ample time for testing, especially since the team will be introducing plays as another new charging mechanism around the same January timeline.                                                                                                                                                                                                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Operations (AJ)**               | **Business Intelligence Team:** Churn and renewal analysis advanced through deeper engagement trend exploration across audience creation, campaign activity, and related workflows. Ferrell Tanvijaja and Christon Joshua identified early signals suggesting that churn is more strongly associated with combined engagement patterns across products rather than isolated feature usage.                                                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **Product Ops Team:** Kristin Gandini built out the complete Early Access infrastructure this week, including LaunchDarkly segments for Phase 1 and Phase 2, plus an automated dashboard that eliminates manual tracking by pulling real-time feature status and LRT estimated dates. The system automatically flags which phase each feature is in based on targeting rules, creating a hands-off go-no-go tracking process that will scale as more features enter the pipeline                                                                                                            |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                   | **PMM Engine Team:** Akshath Dorai\'s objection handling agent launched this week with 58 usage instances, receiving positive feedback from 5 of 6 SDRs and account managers interviewed, though change management and distribution work remain necessary to drive broader adoption.                                                                                                                                                                                                                                                                                                        |
+===================================+=============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+

### **Bottom Line**

The organization is executing toward the January 15th plays launch with critical infrastructure in place, but faces a compressed three-week effective timeline due to holiday schedules and several systemic blockers requiring immediate executive intervention. GTM Data Store dependencies (Chorus engagement data, table partitioning, session aggregation) must be resolved in the next 10 days for the January 15th date to hold. The California person-level intent legal decision needs Ali and Dominik\'s immediate risk assessment. Tool reliability challenges affecting both Workspace and Studio require coordinated resolution across the Intelligence and Platform teams. The customer data deletion process gap identified by Integrations requires a Data Platform owner to design and implement an orchestrated solution. Successfully navigating these blockers while maintaining the divide-and-conquer execution model through the holidays will determine whether we can deliver the complete Unify-Orchestrate-Execute loop that defines our 2026 strategy.

### **GTM Studio**

**GTM Studio Team:** \"Workbooks made major progress preparing for Q1 audiences via Plays, with Jagannath defining the full toolset required after 2026 planning discussions clarified customer use cases, while the team also worked to address AI credit consumption gaps that leave customers operating without visibility. Plays kicked off M2 development for the January 15th delivery with Mohan leading alignment sessions on credit charging and reporting requirements with Ryan, Jesse, Derek, and Karthik, while identifying key M3 priorities including automated manual plays, new triggers, and credit safeguards. ROI Analytics launched to GA for all Salesforce and HubSpot customers with Arun tracking adoption in Amplitude, while Workspace ROI advanced with CFA building data pipelines and Audience ROI faces delays as the engineering team has not yet started scoping work despite committing to deliver before year-end. Data Management finalized shovel-ready requirements for Mask/Unmask and Waterfall Release 2 with Ash and Corina running a cross-functional workshop on GTM Data Model adoption in audiences and rapidly ramping Tools for Plays toward higher-impact use cases.\"

### **GTM Copilot Workspace**

**GTM Workspace Team:** \"GTM Workspace delivered its first production artifact behind feature flag this week while accelerating the Chorus meetings convergence timeline by one month to February. Dylan\'s team shipped the deal status artifact to production and has meeting prep in staging, though tool reliability issues are slowing template expansion. Adam completed a fundamental system prompt rewrite that consolidates instructions and improves opportunity and account handling, positioning us for more predictable quality improvements. Gabe is finalizing requirements to compress the meetings roadmap into February delivery, with CRM updates moving to pilot next week and internal release the week after.\"

### **GTM AI Context Service**

**Intelligence Team:** \"The team finalized the January 15th plays launch plan with high confidence in scope and requirements, but facing tight timeline constraints due to the holiday period. Ryan Stevens established a critical checkpoint: all work must be divide-and-conquer ready by December 22nd to enable asynchronous execution through the holidays, with a functional system required by January 5th for the final two-week burndown. The most significant blocker emerged around GTM Data Store dependencies, where missing Chorus engagement data and improper table partitioning are preventing semantic data pipeline completion. Meanwhile, Derek Osgood successfully deployed critical tools to MQA (CRM updates, email, Slack, Outreach, SalesLoft), and Lars Vedo\'s team achieved a 70% context window reduction through sub-agent patterns.\"

**Semantic Data Team:** \"The team is converging on the new Gemini-based semantic data pipeline, with Jun\'s refactored embedding job now functional and James\'s query API connected and ready for integration testing. The primary focus next week shifts to scaling the embedding migration (currently processing 30 million ZoomInfo records) while Inga completes source data validation on emails. Venkata has surfaced significant GTM Datastore partitioning and authentication issues to Majid and Sanyok, who are actively working resolutions - these must be resolved before the new pipeline can go live in January.\"

**MCP Tiger Team:** \"The team is tracking ahead of original infrastructure timelines, with the Data API MCP server now operational and gateway integration validated in staging. However, the window to complete composite tool construction is compressed - Zheng is out starting Wednesday, making early next week the decisive sprint for that workstream. Rowan\'s discussions with Adam P on MCP app registration confirm alignment with existing API development patterns, reducing implementation complexity for customer onboarding.\"

### **Vertical Datasets**

**Data Executive Team (Vertical Datasets Update):** Igor\'s autodealership initiative is approaching critical mass with acquisitions from Michigan, Arizona, and additional large states completed this week. The team discovered unexpected synergies with professional license datasets that already contained dealership information for states like Pennsylvania. With California being processed through FOIA requests and scraping, we\'ll have comprehensive coverage of major markets. The challenge now shifts from acquisition to cleanup - we need to differentiate legitimate dealerships from the 400,000 auto-adjacent entities currently in our system.

### **Other Data**

**Core Data Team:** \"The Core Data team advanced our 2026 planning initiatives with all product managers delivering consolidated monthly priority roadmaps by week\'s end, positioning us for Brandon\'s final review. Magnus Herweyer secured legal approval for a new Contributory Network technographics initiative that will parse CRM opportunity data to derive technology usage patterns from closed-won deals. Meanwhile, Peter Overman completed the FINRA/Form ADV data schema design with 11 entity collections, accelerating GTM Store integration for early Q1 delivery. Heather Ma advanced the Deal Insights Agent product design post-prototype, conducting interviews with product managers across agent interfaces to define the user experience path forward and establish a timeline for merging the agent into the agentic platform, with the single-account deep dive approach positioned to deliver tangible CN network intelligence value.\"

**Data Executive Team:** \"The Data Research and Enablement team delivered a critical Johnson & Johnson data request in under 24 hours, turning what was originally a 48-hour window into a customer win that\'s directly supporting end-of-year sales opportunities. The Data organization is making significant progress on three fronts: adding over 1 million new tradeable companies to the database, implementing the GTM Studio plays framework to automate sales workflows, and expanding coverage with 2.5 million enrichments this week alone. While year-end GTM requests are creating resource pressure, the team is successfully balancing immediate revenue support with strategic initiatives that will fundamentally improve data coverage and quality heading into 2026.\"

### **Other Platform**

**GTM Data Platform Team:** \"The team made a defining architectural decision on aggregation ownership that removes December 31st delivery risk while setting a clear Q1 path forward. Both Search and Enterprise Data Platform teams aligned that BigQuery will handle near-term aggregation using only current capabilities, while Solr remains focused on its core strengths in search, faceting, and high-performance retrieval. Aggregation at scale moves to Q1, where Linda Johannessen\'s team will evaluate candidate technologies to support flexible, platform-level aggregation (which Solr and BigQuery do not). This approach protects the December 31st Federated Search delivery - focused on delivering performant joins across first-party and third-party data - while preserving architectural quality for the long term.\"

**Integrations Team:** \"Sanyog Rai advanced engagement junction table requirements and identifier-based processing while uncovering a significant gap in our customer data deletion process, leading him to draft cross-platform deletion requirements that need a Data Platform owner. Andres Perez completed the HG Insights and Salesforce connector listings through Partnerfleet, which are now live, but this exposed a scalability challenge requiring a database-driven API solution for the planned 10,000 additional listings. Meanwhile, strategic customer platform requests are being evaluated for delivery in Workspace versus Copilot Enterprise to manage timeline impacts and set realistic expectations with the sales team.\"

**Provisioning & Login Team:** \"A key decision was finalized to allow charges for AI action credit overages up to 10% of a user\'s limit, with an approach that balances cost recoupment and customer protection. This approach, signed off by the Monetization Council, will impact the credit charging service and needs thorough testing before the January release, especially with the simultaneous introduction of \'plays\' as a charging mechanism. Additionally, the upgraded user management UI/UX is ready for release next week, which is a much-needed upgrade to set up future unified user development.\"

**Automation Team:** \"Strategic pivot toward audiences as 2026 value driver while ServiceNow no-code foundation established and Company Master API modernization advances. Sam Massie completed field mapping MVP alignment with engineering teams, identifying that audience-based third-party enrichment will deliver greatest value in early 2026. Marc Frail built a complete ServiceNow no-code flow shell needed for early H1 delivery, though GSuite tools work was deferred due to offsite timing. Adam Peretz achieved 80% completion on Company Master API orchestration analysis, enabling Match Service to deprecate legacy EverString connector while advancing toward unified company data integration.\"

**ZIM Team:** \"The 2026 company theme is plays - making plays successful after 2025\'s data foundation work. We launched Identity Partners program this week with Alioop (an agency Henry signed) as our first major participant, deploying our pixel at scale for significant cookie coverage and intent signals. However, a critical session aggregation service that we thought 00 would handle is back on our plate, requiring urgent requirements work to deliver definitive visitor session end states for GTM Store before Q1 plays launch. Meanwhile, the California person-level intent legal question remains unresolved and needs executive decision from Ali and Dominik about whether we restrict person-level intent in California or accept the legal risk - this is particularly acute since many tech companies are California-based.\"

### **Other Operations**

**Business Intelligence Team:** \"This week, the Business Intelligence team made meaningful progress toward making AI usage, engagement, and adoption patterns more interpretable and actionable across GTM Workspace and GTM Studio. Key advances included strengthening Workspace analytics foundations, validating Studio engagement metrics, and deepening cross-product engagement analysis to better understand churn and renewal behavior. The primary constraint remains incomplete AI credit and entitlement data in Snowflake, which is limiting cohort-level insights and historical comparisons; this is now clearly scoped and actively being addressed by Eran Dayan and AJ Belen.\"

**Product Ops Team:** \"The Early Access release infrastructure is now operational and ready for testing, with automated tracking, phased rollout segments, and quality gates built into LaunchDarkly. Kristin Gandini completed the technical foundation including automated go-no-go tracking that pulls real-time data on feature phases and estimated dates. Meanwhile, Daniel Kong successfully piloted the feature info pack process with Dylan\'s POC in just 30 minutes, demonstrating the efficiency gains from streamlined PM workflows. The team validated their Voice of Customer semantic search approach through the vertical dataset report, proving the entity relationship mapping strategy delivers high-quality results that can be quickly adapted to new product areas.\"

**PMM Engine Team:** \"The team secured a pivotal meeting yesterday with Dominik, Adam, and Rowan on go-to-market flow, generating enough information to move forward with ELT-level conversations next week before the holiday break. Jennifer Scharrer drafted ELT slides overnight following the session, positioning the team to activate cross-functional teams on Context Service/Flow launch planning. Akshath Dorai\'s objection handling agent launched this week with 58 usage instances, receiving positive feedback from 5 of 6 SDRs and account managers interviewed, though change management and distribution work remain necessary to drive broader adoption. The RKO product session skeleton is complete and ready for Dominik\'s structural feedback, acknowledging that ongoing evolution is expected as organizational thinking develops over the next four weeks.\"

*For deeper analysis on any topic above, reference specific team reports or contact team leads directly.*

*Methodology: Analysis of team 1-2-3 Operating Framework reports, prioritizing: (1) Executive decisions needed, (2) Cross-team blockers, (3) Strategic momentum areas, (4) Strategic alignment gaps*

## **📊 Appendix**

### **Individual Team Reports**

## **Automation Team Weekly Report - December 12, 2025**

**Executive Summary**

Strategic pivot toward audiences as 2026 value driver while ServiceNow no-code foundation established and Company Master API modernization advances. Sam Massie completed field mapping MVP alignment with engineering teams, identifying that audience-based third-party enrichment will deliver greatest value in early 2026. Marc Frail built a complete ServiceNow no-code flow shell needed for early H1 delivery, though GSuite tools work was deferred due to offsite timing. Adam Peretz achieved 80% completion on Company Master API orchestration analysis, enabling Match Service to deprecate legacy EverString connector while advancing toward unified company data integration.

**This Week\'s Progress**

**Key Momentum Areas**

Sam Massie achieved engineering alignment on field mapping MVP, coordinating core and app teams around a simple implementation scope that demonstrates ZoomInfo as an open platform for destinations, exports, and enrichments. The alignment establishes clear POC requirements with engineering design sign-off from both teams.

Marc Frail delivered ServiceNow no-code flow foundation, creating shell implementation needed for early H1 2026 delivery. The end-to-end flow definition provides foundation for enterprise service management integration, requiring future ServiceNow meetings to review implementation details.

Adam Peretz advanced Company Master API modernization, completing initial review confirming the orchestrator meets requirements for replacing legacy EverString connector. The lift-and-shift effort enables Match Service to deprecate old functionality while progressing toward incorporating Company Master data into a unified company database.

**Goals & Progress**

**Field Mapping Engineering Coordination**: Sam Massie completed 100% of core and app team alignment on field mapping proof-of-concept scope and implementation. Engineering design received sign-off from both teams, establishing a clear path for demonstrating platform vision through working POC.

**Company Master Orchestration**: Adam Peretz reached 80% completion with successful review of the orchestration layer confirming technical viability. The final task list for completing lift-and-shift effort remains to be finalized, but core architectural validation is complete.

**ServiceNow Integration Foundation**: Marc Frail established no-code flow shell for ServiceNow integration despite not advancing G Suite tools work. The ServiceNow priority reflects early H1 2026 enterprise customer requirements.

**Strategic Challenges**

Developer portal duplication for MCP applications requires detailed requirements, as Adam Peretz identified the need to work with Rowan Bailey on identifying requirements and trade-offs for enabling OAuth-based MCP application registration and management. The functionality duplication should be straightforward but requires careful scoping.

Year-end resource constraints compress delivery windows, with Adam Peretz noting the need to finalize planning for end-of-year outages and set realistic January delivery expectations. The holiday timing affects team capacity and coordination possibilities.

**Strategic Insights**

**Key Learnings & Discoveries**

Audiences emerge as primary 2026 value drivers, with Sam Massie identifying that bringing more and better third-party enrichments into audiences delivers greater customer value than automation-focused capabilities in early 2026. This strategic insight redirects focus while recognizing that automation concepts translate well to audience contexts.

Orchestration layer enables legacy system migration, as Adam Peretz\'s review confirmed that Match Service\'s orchestrator successfully abstracts complexity, allowing customer-invisible transition from EverString connector to modern architecture. This pattern demonstrates how orchestration layers facilitate infrastructure modernization.

ServiceNow integration prioritization reflects enterprise requirements, with Marc Frail\'s focus on complete end-to-end flow shell indicating strong early H1 demand from enterprise customers for service management integration capabilities.

Field mapping MVP demonstrates platform openness, as Sam Massie\'s engineering alignment work positions the POC to showcase ZoomInfo as open platform for integrations rather than closed ecosystem, affecting market positioning and partnership opportunities.

**Cross-Team Dependencies**

Rowan Bailey collaboration is essential for Adam Peretz\'s developer portal duplication work, requiring detailed requirements and trade-off analysis for MCP application OAuth support.

Core and app engineering teams require continued coordination for Sam Massie\'s buzz.ai and Insightly flow refinement, serving as the next milestone for demonstrating forms and field mapping capabilities.

Match Service team coordination continues for Adam Peretz\'s Company Master API lift-and-shift work, enabling deprecation of legacy EverString connector infrastructure.

**Looking Ahead**

Next week focuses on H1 2026 planning while advancing GSuite tools analysis and finalizing year-end delivery expectations.

Marc Frail will prioritize GSuite tools meeting setup and work with engineering on H1 planning.

Adam Peretz will finalize planning for end-of-year outages and set clear expectations for January deliverables, managing team capacity during holiday period while maintaining momentum on Company Master orchestration and developer portal MCP support.

Sam Massie will refine buzz.ai and Insightly flows with core and app teams as next milestone for demonstrating forms and field mapping capabilities, translating the strategic shift toward audiences into concrete delivery plans.

*Source: Team 1-2-3 Operating Framework entries from 12/8 - 12/12*

## **Business Intelligence Team Weekly Report - December 8-12, 2025**

**Executive Summary**

This week, the Business Intelligence team made meaningful progress toward making AI usage, engagement, and adoption patterns more interpretable and actionable across GTM Workspace and GTM Studio. Key advances included strengthening Workspace analytics foundations, validating Studio engagement metrics, and deepening cross-product engagement analysis to better understand churn and renewal behavior. The primary constraint remains incomplete AI credit and entitlement data in Snowflake, which is limiting cohort-level insights and historical comparisons; this is now clearly scoped and actively being addressed by Eran Dayan and AJ Belen.

**This Week\'s Progress**

**Key Momentum Areas**

The GTM Workspace Analytics Agent continued progressing toward operational usefulness. AJ Belen and Phoebe Mei advanced agent behavior, usability, and onboarding expectations, enabling internal stakeholders to increasingly use Workspace as the default entry point for BI questions and utilization reporting.

Churn and renewal analysis advanced through deeper engagement trend exploration across audience creation, campaign activity, and related workflows. Ferrell Tanvijaja and Christon Joshua identified early signals suggesting that churn is more strongly associated with combined engagement patterns across products rather than isolated feature usage.

GTM Studio analytics clarity improved through metric validation and hierarchy alignment. Inbal Kor validated engagement metric logic and enhanced agent messaging structure, improving explainability and trust in Studio reporting while aligning Studio and Workspace definitions.

**Goals & Progress**

**GTM Workspace Analytics**: Foundational enhancements progressed, including adding internal management hierarchy fields (L3-L8) and validating analytics accuracy. Eran Dayan improved SQL reliability and reporting precision, enabling more consistent weekly Workspace performance reporting and clearer persona-level insights.

**Churn & Renewal Analysis**: Engagement trend logic for time-to-engagement and audience creation was refined. Ferrell Tanvijaja identified meaningful behavioral differences between churned and renewing accounts, with early evidence pointing toward multi-product interaction effects rather than single-feature drivers.

**GTM Studio Engagement Metrics**: Metric definitions, dependencies, and denominators were reviewed and validated. Inbal Kor aligned Studio engagement reporting with Workspace standards and improved agent outputs, supporting more confident downstream interpretation by stakeholders.

**Strategic Challenges**

AI credit and entitlement data are still not fully available in Snowflake, preventing the creation of reliable credit-based cohorts and limiting insight into AI-driven behavior over time. Eran Dayan and AJ Belen have identified the specific data gaps, and interim analysis is proceeding with clearly documented assumptions.

Audience-level engagement data lacks a clean active-versus-inactive indicator, complicating trend interpretation over time. Ferrell Tanvijaja has validated that current trends are directionally useful but not yet sufficient for precise time-based attribution without additional modeling.

External stakeholder adoption of chat-based analytics agents remains uneven. Phoebe Mei observed hesitation from some users, indicating a gap between stakeholder expectations and current artifact visibility and export capabilities, which is informing the next round of improvements.

**Strategic Insights**

**Key Learnings & Discoveries**

Incremental improvements to analytics agent structure - such as clearer message formatting and hierarchy context - materially increase stakeholder understanding and willingness to rely on self-serve reporting. Inbal Kor\'s updates demonstrated that usability improvements can unlock adoption without new data changes.

Audience creation trends show promise as an early signal of churn risk, but only when interpreted alongside campaign and account-level signals. Christon Joshua\'s exploration reinforced the need to synthesize multiple datasets to distinguish meaningful patterns from background activity.

**Cross-Team Dependencies**

Our work with Product and Engineering on AI credit ingestion and entitlement accuracy remains essential to unlocking cohort-based AI usage analysis and longitudinal reporting. Alignment with William and AI platform counterparts is improving, but full historical coverage remains a dependency for next-stage insights.

Ongoing collaboration with Solution Consulting continues to add valuable real-world context to engagement patterns, helping refine hypotheses and avoid overfitting purely behavioral signals.

**Looking Ahead**

Next week\'s focus is on converting foundational improvements into more repeatable, executive-ready insights while continuing to close known data gaps.

Top priorities include refining Workspace success metrics within the analytics agent, aligning weekly reporting formats with prompt-to-dashboard workflows, and advancing a combined-signal churn model that synthesizes engagement across products. Progress will depend on continued movement on AI credit data availability and stakeholder feedback on agent usability.

The team is well positioned to build on this momentum, with clearer analytical framing, stronger data foundations, and growing alignment around Workspace as the primary surface for Business Intelligence insights.

*Source: Team Operating Framework entries and end-of-week reflections for the week of December 8-12, 2025*

## **Core Data Team Weekly Report - December 8-12, 2024**

**Executive Summary**

The Core Data team advanced our 2026 planning initiatives with all product managers delivering consolidated monthly priority roadmaps by week\'s end, positioning us for Brandon\'s final review. Magnus Herweyer secured legal approval for a new Contributory Network technographics initiative that will parse CRM opportunity data to derive technology usage patterns from closed-won deals. Meanwhile, Peter Overman completed the FINRA/Form ADV data schema design with 11 entity collections, accelerating GTM Store integration for early Q1 delivery. Heather Ma advanced the Deal Insights Agent product design post-prototype, conducting interviews with product managers across agent interfaces to define the user experience path forward and establish a timeline for merging the agent into the agentic platform, with the single-account deep dive approach positioned to deliver tangible CN network intelligence value.

**This Week\'s Progress**

**Key Momentum Areas**

Peter Overman completed the FINRA/Form ADV data product strategy with 11 entity collections, securing alignment with Dow to accelerate GTM Store integration in early Q1. The comprehensive schema positions us to deliver a more advanced financial services dataset than most competitors in the market.

Magnus Herweyer navigated legal requirements to unlock Contributory Network potential, securing approval for parsing contributed CRM opportunity data while establishing a framework that provides immense flexibility for data usage across PTI, NeverBounce, and C3 consumers. This creates a foundation for differentiated technographic insights derived from actual purchase behavior.

Heather Ma refined the Deal Insights Agent strategy based on cross-team feedback, pivoting to a single-account deep dive approach that emphasizes real data advantages over generic insights. Through interviews with product managers across various agent interfaces, she identified the optimal starting point for agent development with Brandon Wilson, positioning us to deliver tangible CN network intelligence value.

Cam Fortin delivered the consolidated January 15 release communication framework with LRT-356 and draft release notes, coordinating location creation across Analysis, WDA, and engineering teams to ensure alignment on approximately 600K international companies from Rhetorik/WDOD and 1M URL-only companies for the critical ES field deprecation deadline.

**Goals & Progress**

**Data Infrastructure & Quality**: John Durst confirmed Canadian notification process completion with all backlog notifications sent and communication to GTM and Support teams prepared. Waterfall secondary values remain on track for December 15 data availability, though UX implementation may lag. Coverage on personal email alternative values came in lower than expected, requiring continued monitoring.

**Product Development & Integration**: Hayden Cowell built comprehensive status documentation capturing all DQM and Data Tools projects for H1 planning, with Polaris company metrics on track for January completion after removing final blockers. The Board of Directors technical plan progressed with collaboration from Rituparna Das, Anurag, Nat, and Joey, targeting end-of-January completion for backend infrastructure to explicitly set resume records as part-time. The transparency metrics generated strong interest from the DaaS team, though Solr integration requirements add complexity to delivery timeline.

**Strategic Planning & Alignment**: Jody Roberts documented the company schema and attribute cleanup plan with clear ownership and timing, focusing on business value through attribute deprecation while navigating schema unification challenges. The monthly priority process rollout progressed with team-wide alignment scheduled for Monday\'s discussion to meet Brandon\'s end-of-week deadline.

**Customer Data Improvements**: Rituparna Das created targeted audiences for ZoomInfo customers experiencing contact location issues, coordinating with marketing to launch AM-led improvement campaigns. The non-social location improvements one-pager advanced toward Friday delivery, while initial requirements for leadership and Board of Directors golden datasets were refined to focus on top-level company domains for researcher efficiency.

**Strategic Challenges**

Legal requirements for Contributory Network data usage created multiple pivots for Magnus this week, with both the threat detection shared service and calendar data initiatives requiring EULA flags that weren\'t initially identified. The CN EULA flag requirement specifically blocks calendar data delivery to PTI until proper consent verification is in place.

Knowledge transfer complexity emerged as Heather works to transition Contributory Network projects to Magnus, with ongoing initiatives scattered across different JIRA tickets, Slack channels, and documentation requiring consolidation into comprehensive one-pagers for effective handoff. The NeverBounce project ownership and rationale required particular attention as both PMs work to understand the full scope and strategic value.

The DaaS team\'s enthusiasm for transparency metrics highlights a delivery challenge - integration requires adding metrics to both Solr and search service, necessitating careful planning to avoid multiple reindexing cycles. Hayden Cowell is coordinating with Ted to establish a consistent approach for metric delivery.

**Strategic Insights**

**Key Learnings & Discoveries**

Magnus discovered that the Contributory Network legal framework provides significant flexibility once proper EULA agreements (May 2025 version) and admin portal opt-ins are secured. This unlocks immense potential for data usage across multiple consumers without additional legal overhead, fundamentally changing our approach to contributed data utilization.

Peter Overman\'s AI-assisted schema development revealed the importance of proper prompting for business tradeoff decisions, leading to creation of an additional guide that helps determine entity relationships, matching considerations, and derived fields that optimize downstream consumption.

Rituparna Das encountered scaling challenges with GTM Studio audience creation, finding that 2K record enrichment takes 90 minutes and requires precise prompting to manage AI credit constraints effectively. The new location matching feature shows promise for improving match rate accuracy and coverage.

Heather Ma\'s agent interviews revealed that Deal Insights Agent positioning requires emphasizing proprietary network data advantages, with users preferring single-account deep dives over broad signal population across account lists. The feedback highlighted the need for clearer naming beyond \"Deal Insights\" to convey the real data foundation rather than generic insights.

**Cross-Team Dependencies**

Our collaboration with the DaaS team on transparency metrics delivery requires coordination on Solr integration to avoid multiple reindexing cycles. Hayden is working with Ted to establish a delivery plan that balances their enthusiasm for the metrics with our technical constraints.

The transition of WDA under George\'s leadership following Andrew Harris\'s departure (final day December 23) creates an opportunity for aligned acquisition strategy, particularly beneficial for Peter\'s GTM Store integration work where he already collaborates with George. Peter is dedicating extra time with the team, George, and Andrew to ensure smooth knowledge transfer and maintain team support through the transition.

**Looking Ahead**

Next week focuses on finalizing the monthly priority process with team alignment on Monday and Brandon\'s review by week\'s end, establishing our operating rhythm for 2026 execution. John Durst will present technographics investment proposals following the crawlers review while monitoring personal email and direct phone coverage from the recent go-live.

Magnus will accelerate Contributory Network initiatives across multiple fronts - launching the technographics project, initiating the form complete project, and advancing email signature and calendar pipeline initiatives while completing knowledge transfer from Heather. Peter will monitor GTM schema merges and ZDP data loads while pushing forward MSP dataset integration and LinkedIn Professional Profiles production pipeline deployment.

Heather Ma will finalize H1 planning for CN data-driven insights and AI agents by Friday, while completing the one-pager consolidation of ongoing CN projects for smoother transition. Rituparna Das will deliver the non-social location improvements one-pager and advance the location data improvement campaigns with customer AMs through GTM Studio.

The January 15 release preparation intensifies as Cam receives final location tables Monday and monitors ETL runs, with release notes and LRT updates required once location infusion results confirm. The team\'s ability to balance immediate delivery needs with strategic 2026 planning will determine our momentum heading into year-end.

*Source: Team 1-2-3 Operating Framework entries from December 8-12, 2024*

## **Data Executive Team Weekly Report - December 8-12, 2025**

**Executive Summary**

The Data Research and Enablement team delivered a critical Johnson & Johnson data request in under 24 hours, turning what was originally a 48-hour window into a customer win that\'s directly supporting end-of-year sales opportunities. The Data organization is making significant progress on three fronts: adding over 1 million new tradeable companies to the database, implementing the GTM Studio plays framework to automate sales workflows, and expanding coverage with 2.5 million enrichments this week alone. While year-end GTM requests are creating resource pressure, the team is successfully balancing immediate revenue support with strategic initiatives that will fundamentally improve data coverage and quality heading into 2026.

**This Week\'s Progress**

**Key Momentum Areas**

The Johnson & Johnson turnaround exemplified our team\'s ability to deliver under pressure - Dana\'s team compressed a 48-hour data request into 24 hours, providing critical support for a 7AM customer meeting that resulted in positive feedback. This rapid response capability is proving essential as we field 2-3 daily requests from GTM teams working to close year-end deals. The ability to deliver quality data at this velocity is directly enabling revenue capture in Q4.

On-going Company creation initiative is on track for adding over 1 million new companies to our database, with the vast majority being tradeable entities that will immediately expand our addressable market. The crawler-sourced companies come with domains and activity signals, making them immediately valuable for sales teams. Combined with 400,000 location updates and 500,000 location confirmations from ZIPI data, we\'re substantially improving both coverage and accuracy of our core company dataset ahead of the January 15th cube release.

Brandon Wilson successfully integrated BigQuery connections into the Deal Insight Agent, passing all unit tests and positioning us to deploy CN Benchmark capabilities for deal cycle insights. The integration with Heather\'s team on contributory network planning has already generated four additional agent concepts, demonstrating how our proprietary data assets can drive differentiated AI capabilities that go beyond basic deal summarization tools that \"everyone has a crappy version of.\"

**Goals & Progress**

**Company Schema & Attribute Cleanup**: Jody\'s team documented a plan for attribute deprecation that directly enables our vertical dataset strategy by eliminating conflicts between legacy attributes and new specialized data. The cleanup focuses on removing redundant and conflicting attributes that currently prevent clean integration of vertical datasets like auto dealerships and MSP data. While attribute cleanup can proceed immediately with minimal breaking changes, the team is strategically timing the deprecation to align with GTM Studio\'s January-February launch to ensure customers can access vertical data through Studio before losing CRM export capabilities for these attributes.

**Company & Location Expansion**: Our data cube efforts are converging successfully with over 1 million new companies ready for staging tests, predominantly tradeable tier companies with strong attribution. Ethan\'s team validated 400,000 company location updates from the crawler\'s new model and confirmed 500,000 additional locations through ZIPI data, though some cohorts need additional filtering before full deployment. The January 15th cube release is on track with testing scheduled for next week.

**GTM Plays Framework**: The plays initiative is crystallizing around five core automation opportunities: Account Prioritization, Inbound Acceleration, Outbound Automation, Pipeline & Deal Acceleration, and TAM & ICP Development. Brandon Tucker\'s team is designing a no-code interface that will allow GTM teams to automate these workflows, with early roadmap focusing on service and tool integration. The data asset is positioned ahead of the broader R&D roadmap, with 95% company coverage and strong attribute accuracy ready to support these plays.

**Vertical Dataset Development**: Igor\'s autodealership initiative is approaching critical mass with acquisitions from Michigan, Arizona, and additional large states completed this week. The team discovered unexpected synergies with professional license datasets that already contained dealership information for states like Pennsylvania. With California being processed through FOIA requests and scraping, we\'ll have comprehensive coverage of major markets. The challenge now shifts from acquisition to cleanup - we need to differentiate legitimate dealerships from the 400,000 auto-adjacent entities currently in our system.

**Strategic Challenges**

The volume of year-end GTM requests is straining our capacity to advance strategic initiatives, with Dana\'s team fielding 2-3 urgent requests daily that require immediate turnaround. While we\'re successfully supporting revenue-critical deals like Johnson & Johnson, this reactive mode is limiting our ability to address systematic improvements like the rebrand detection issues where crawlers are missing company name changes. The team is exploring Google News search patterns as a workaround but needs dedicated time to implement a proper solution.

Cross-functional alignment on data science projects revealed process gaps that created late-stage friction during evaluation. Ethan discovered that when Core Data isn\'t involved during model development, there\'s often misalignment on evaluation criteria that only surfaces during sign-off. The location extraction model looked problematic initially but proved promising once teams aligned on proper test parameters, highlighting the cost of late coordination.

The flywheel partner program remains blocked on obtaining partner domain lists needed for cookie compliance scanning. Taylor has Privado fully configured but cannot proceed without the domains where partners have embedded pixels. Additionally, the Do Not Call list suppression feature has a technical issue where we\'re relying on person-level country codes rather than phone number analysis, requiring a fix targeted for January-February that affects customer compliance capabilities.

**Strategic Insights**

**Key Learnings & Discoveries**

The AtData email validation analysis revealed mid-90s delivery rates on their cached email opens, providing a strong signal for email quality that could dramatically improve our publish rates. Steve\'s analysis shows this third-party validation could help us reduce unknown rates in NeverBounce verification and provide better coverage for generated emails, though we\'re still evaluating cost implications. This could unlock significant improvements in our contact data quality without requiring additional engineering resources.

The synergy between vertical datasets and existing data sources proved more valuable than anticipated. Igor\'s team discovered that professional license acquisitions already contained automotive dealership data for multiple states, reducing acquisition costs and accelerating coverage. Similarly, Dana identified that our crawler data could be leveraged for rebrand detection through pattern matching in Google News searches, potentially solving a persistent data quality issue that affects major companies.

Taylor\'s investigation into our legacy JIRA privacy review process uncovered that the previous Slack-based system was abandoned due to poor reporting capabilities and organizational challenges. However, Privado\'s new Agentic Assessments tool could provide the exact functionality we need - an AI agent trained on our compliance documentation that automatically flags risks in JIRA tickets. This discovery could streamline legal review from weeks to days while improving compliance coverage.

**Cross-Team Dependencies**

Our work with the GTM organization on year-end deals requires careful balance between immediate support and strategic progress. Dana\'s team is successfully managing 2-3 daily requests but this reactive posture is unsustainable heading into 2026. We need clearer prioritization frameworks and potentially dedicated resources for tactical support to protect our strategic initiatives.

The schema unification and attribute cleanup effort led by Jody is critical for unlocking our vertical dataset potential. The current attribute conflicts actively prevent proper categorization of specialized entities - for instance, auto-adjacent businesses get misclassified as dealerships due to overlapping attributes. Jody\'s plan to decouple MSP attributes from the broader cleanup allows immediate progress on vertical data quality while carefully managing the Studio dependency for customer-facing changes. This surgical approach ensures we can support Dow\'s vertical datasets and Igor\'s autodealership data without disrupting existing customer workflows before alternative consumption methods are available through Studio in January-February.

**Looking Ahead**

Next week\'s focus centers on the January 15th data cube release, with Ethan leading comprehensive testing and sign-off procedures that will validate over 1 million new companies and hundreds of thousands of location updates. This release represents our largest coverage expansion in recent quarters and requires careful coordination across Core Data, Data Science, and Engineering teams.

Jody will execute on the attribute cleanup plan, starting with the MSP-specific attributes that can be immediately deprecated without breaking changes. This cleanup is essential for Igor\'s autodealership categorization work, as it will eliminate the attribute conflicts causing 400,000 auto-adjacent entities to be misclassified. The team will coordinate with Dow on vertical dataset requirements while establishing clear communication timelines for front-end teams to update their workflows. By separating immediate cleanup from Studio-dependent changes, we can improve data quality for vertical datasets now while planning the broader schema unification for Q1 2026.

Brandon Tucker will finalize the top priority process and 2026 strategic bets using a top-down approach after this week\'s bottoms-up analysis. The team will also implement monitoring dashboards for each of the five GTM plays, tracking funnel metrics from form fills through enrichment accuracy to demonstrate data quality in real customer scenarios. This shift from abstract coverage percentages to use-case-specific performance metrics will provide more compelling evidence of our data asset\'s value while identifying specific improvement opportunities for each play.

*Source: Data Executive Operating Framework entries from Dec. 8, 2025 - Dec. 12, 2025*

## **GTM Data Platform Team Weekly Report - December 8, 2025**

**Executive Summary**

The team made a defining architectural decision on aggregation ownership that removes December 31st delivery risk while setting a clear Q1 path forward. Both Search and Enterprise Data Platform teams aligned that BigQuery will handle near-term aggregation using only current capabilities, while Solr remains focused on its core strengths in search, faceting, and high-performance retrieval. Aggregation at scale moves to Q1, where Linda Johannessen\'s team will evaluate candidate technologies to support flexible, platform-level aggregation (which Solr and BigQuery do not). This approach protects the December 31st Federated Search delivery - focused on delivering performant joins across first-party and third-party data - while preserving architectural quality for the long term.

Meanwhile, Moshik Levin\'s Location Matching team identified all remaining gaps in the Company Master Data API\'s matching reasons and scoring. Once bugs are fixed, Data Services will rerun reports to validate accuracy before the January 15th release. The universal dataset onboarding process remains under review, with formalization targeted before the holiday break to improve transparency and stakeholder visibility.

**This Week\'s Progress**

**Key Momentum Areas**

Menna Rashwan and Linda Johannessen secured cross-team alignment on aggregation architecture and ownership strategy. The discussion clarified technical trade-offs and defined a near-term execution plan grounded in current system capabilities. Both teams reinforced the principle of using the right tools for the right job - Solr excels at search and faceting, BigQuery handles the aggregation capabilities it already supports today, and neither should be stretched beyond its design strengths for this milestone.

Moshik Levin worked with the Company Data team to resolve accuracy results for the new Company Master Data API, specifically around match reasons and scoring distributions. The team now awaits bug fixes from the company data team before engaging Data Services to test and validate the corrections. This work directly supports the January 15th GA release timeline and ensures customers see consistent, explainable match quality.

**Goals & Progress**

**Federated Search Integration**: The December 31st immediate goal remains clear - reliable, performant joins across first-party and third-party data, filtering across CRM and ZoomInfo data, and returning results reliably at scale. Aggregation at scale is not feasible for a December target. Menna Rashwan and Linda Johannessen continue working with the team to evaluate architectural options for implementing aggregation logic, with a focus on long-term ownership, technical direction, and trade-offs. This establishes a scalable and maintainable path for enabling aggregation and grouping use cases in Federated Search post-December 31st.

**GraphQL API Platform Capabilities**: Linda Johannessen is defining platform capabilities across the GraphQL API, including Federated Search, MCP, GTM Store, and data needs to support execution in Q1 and scale in Q2 for Audiences (Workbooks), Workspaces, and Agent Plays. This high-level view of what consuming teams need and how the platform will support those needs enables detailed execution planning for Q1 and early scoping for Q2 scale, reducing cross-team ambiguity and sharpening engineering focus.

**Company Master Data API Transition**: Moshik Levin presented impact measurements for switching the location matcher to Data Advisory and Services, working toward alignment on the January 15th GA date. The team believes all gaps in how the new Company Master Data API measures reasons and scoring have been identified. Once bugs are fixed and Data Services reruns their tests, the team can share an update on reasons and score distributions, ensuring customers won\'t feel unexpected changes even as underlying results improve.

**Strategic Challenges**

The universal dataset onboarding process requires formalization before the holiday break. Moshik Levin is updating the process and consolidating trackers into a single backlog and reviewing playbooks to help stakeholders plan the velocity of onboarding new datasets. The team recognizes this work creates the operational foundation that prevents chaotic escalations, even though individual dataset requests currently work smoothly when addressed one by one.

Resource constraints on David, the key engineer supporting dataset onboarding, present ongoing coordination challenges. David remains the go-to engineer for making decisions and providing feedback across several different projects. While his expertise is invaluable and universally trusted, the concentration of knowledge and responsibility creates a bottleneck that needs deliberate management. Moshik Levin is working to support additional engineering involvement where possible, though PM-level contributions can only go so far in addressing this technical dependency.

The Company Data team faces a swamped ticket backlog, which affects the timeline for fixing bugs in the Company Master Data API. These fixes are prerequisites for Data Services to rerun their reports and validate match quality before the January 15th release. While the path forward is clear, execution depends on another team\'s capacity and prioritization, requiring careful coordination to maintain the release schedule.

**Strategic Insights**

**Key Learnings & Discoveries**

The aggregation architecture discussion revealed a fundamental insight about platform design: specialized systems optimized for specific tasks outperform generalized solutions, even when data replication is required. Marc Delurgio validated this pattern independently, noting that big data companies commonly run multiple storage systems - single store for website signals, Solr for search, BigQuery for deep joins, and Bigtable for lookups. GraphQL\'s query resolver layer can route queries to whichever platform is optimal and even stack queries across platforms, making backend choice invisible to consumers. Storage is cheap, processing is expensive, and users want things fast - which justifies replicating data across specialized systems rather than forcing one system to do everything.

The scope expansion challenge with engagement data being added mid-stream to Federated Search highlighted the ongoing tension between delivery timelines and architectural completeness. While the shim-based approach using the current Solr schema enables meeting the December 31st deadline, it creates known technical debt that will require future rework once the new Company and Person schemas are finalized. The team chose delivery over perfection for this milestone, but documented the trade-offs clearly to inform Q1 planning.

**Cross-Team Dependencies**

Our work with Sanyog\'s team on exposing missing engagement data points for grouping use cases remains essential for post-December 31st functionality. Several data points required to support engagement grouping were identified and shared with Sanyog\'s team, who will work on exposing them. Once available, Federated Search will require further updates to incorporate these into the grouping logic. The dependency is well-understood and timing is aligned with the Q1 roadmap, though coordination will be necessary as work progresses.

The Search team partnership continues to drive convergence across the platform. Shared architecture work is reducing future duplication and establishing unified patterns for how applications consume data. Menna Rashwan\'s alignment with Frank\'s and Majed\'s teams on scalar mapping, operator behavior, and schema definitions directly enables the December 31st Federated Search integration with GraphQL. This collaboration model - deep technical alignment paired with clear product requirements - sets the standard for platform team partnerships.

**Looking Ahead**

The holiday season compresses next week\'s schedule, with Moshik Levin taking December 27-29 off and similar time off patterns across the team. The priority is completing documentation and alignment work before the break so execution can resume cleanly in January.

Moshik Levin will finalize the universal dataset onboarding process documentation and share with stakeholders before the holidays. This establishes the operational backbone for 2026 dataset velocity and removes a visibility gap that has created uncertainty for partners. The January 15th Company Master Data API release remains on track, pending bug fixes and Data Services validation. Moshik will establish the final decision date for making the go/no-go call, ensuring adequate buffer for any last-minute issues.

Menna Rashwan and Linda Johannessen will continue driving Q1 planning for aggregation architecture evaluation, focusing on which technologies can support scalable, flexible aggregation across the platform. Early identification of leading candidates - potentially including single store or other specialized systems - will inform resourcing and sequencing discussions. The December 31st Federated Search delivery remains the immediate focus, with aggregation work resuming in early January once core integration is stable.

The team enters the holiday period with clear momentum on platform fundamentals: architectural decisions are made, integration patterns are validated, and Q1 priorities are defined. The focus for January will be scaling what works and addressing technical debt deliberately rather than reactively.

*Source: Team 1-2-3 Operating Framework entries from December 8-12, 2025*

## **GTM Studio Team Weekly Report - December 8-12, 2025**

**Executive Summary**

Workbooks made major progress preparing for Q1 audiences via Plays, with Jagannath defining the full toolset required after 2026 planning discussions clarified customer use cases, while the team also worked to address AI credit consumption gaps that leave customers operating without visibility. Plays kicked off M2 development for the January 15th delivery with Mohan leading alignment sessions on credit charging and reporting requirements with Ryan, Jesse, Derek, and Karthik, while identifying key M3 priorities including automated manual plays, new triggers, and credit safeguards. ROI Analytics launched to GA for all Salesforce and HubSpot customers with Arun tracking adoption in Amplitude, while Workspace ROI advanced with CFA building data pipelines and Audience ROI faces delays as the engineering team has not yet started scoping work despite committing to deliver before year-end. Data Management finalized shovel-ready requirements for Mask/Unmask and Waterfall Release 2 with Ash and Corina running a cross-functional workshop on GTM Data Model adoption in audiences and rapidly ramping Tools for Plays toward higher-impact use cases.

**Key Momentum Areas**

**2026 Planning Crystallized Agent-First Strategy**: The annual planning workshop this week generated breakthrough clarity on how audiences will be built through Plays rather than standalone chat interfaces. Jagannath and the team identified the complete set of tools needed to power agentic audience generation, including CRUD APIs for generic database interactions, alignment between data processing pipelines and Plays architecture, and specialized tools like ETL. The sessions validated that early customer use cases align with the team\'s strategic direction, confirming the business problems being tackled are the right ones.

**ROI Analytics Reached General Availability**: Arun\'s team launched the ROI Analytics Dashboard to all Salesforce and HubSpot customers this week, providing self-serve analytics that enable communication of GTM Studio and Workspace usage to early adopters. The release positions the product for upsell conversations and improved adoption, with usage now being tracked through Amplitude to inform future iterations.

**Critical Shovel-Ready Work Accelerated Across Workstreams**: Tanvi completed clone audiences design feedback and finalized signal enrichment side panel requirements with engineering handoff scheduled, while Ash delivered fully shovel-ready requirements for Mask/Unmask and Waterfall Release 2 with NeverBounce auto-verification. These deliverables maintain a healthy development pipeline as higher-priority initiatives progress, ensuring engineering teams have clear next steps when capacity becomes available.

**Goals & Progress**

**Workbooks**

**Major Planning Breakthroughs Defined Tool Requirements**: Jagannath and Tanvi made significant progress defining the product direction for audiences through Plays following the 2026 planning workshop. The team identified the complete toolset needed to enable agentic audience building, validated that customer use cases align with the strategic approach, and established that moving forward requires adopting an agent-first rather than UI-first development mindset where features are built as tools that agents can invoke before being wrapped in UI patterns.

**Technical Architecture Dependencies Require Cross-Team Alignment** (Clear path forward): The team needs to resolve two architectural dependencies for agentic audiences to progress. First, semantic query integration requires alignment on how the semantic service will function as a tool within Plays infrastructure now that audience chat is migrating to Plays. Second, the interaction pattern between data processing pipelines and Plays for enrichment workflows needs clarification, specifically how Plays will serve as the engine for operations like web research that currently run through separate pipelines. Jagannath is working with Carlos, Tushar, and Umesh\'s teams to align on the final technical approach, with discussions already underway and a clear path forward established.

**Plays**

**M2 Development Kicked Off for January 15th Delivery**: Mohan and the engineering team began M2 development work following last week\'s onsite, focusing on bulk run capabilities, credit charging and reporting, and Websights trigger functionality to support the top inbound and outbound play demos. The dev work is progressing on schedule with concrete assignees identified for all workstreams, and the team held productive alignment sessions with Ryan, Jesse, Derek, and Karthik on credit requirements covering both internal reporting and customer-facing experiences.

**M3 Roadmap Priorities Identified with Clear Trade-offs** (No additional action required): The team aligned on post-January 15th priorities that will enhance customer readiness without blocking the immediate deliverable. M3 will focus on automating manual plays, introducing new triggers including audience action changes and layered schedule triggers, and implementing credit safeguards like pause play and notification functionalities. Mohan is continuing alignment with Derek, Karthik, and Sri on trigger requirements, with the scope for establishing new backend architectures and services to support Plays integration with audiences and other apps being actively monitored to ensure scalability.

**ROI Analytics**

**Dashboard Launched to GA and Workspace Pipeline Established**: Arun successfully released the ROI Analytics Dashboard to all Salesforce and HubSpot customers (Dynamics support planned for upcoming releases), with usage now being tracked in Amplitude to measure adoption. The Workspace Analytics workstream is progressing well with the CFA team building the necessary data pipeline after reviewing the initial dataset, and no blockers are currently impeding progress on this front.

**Audience ROI Delayed Pending Engineering Commitment**: The Audience Analytics workstream is trending toward missing the February release target because the Audience Engineering team has not yet begun scoping or planning the work, despite earlier commitments to publish data before year-end and share an execution plan. Additionally, Chat ROI faces technical gaps as tool-touch data for companies, contacts, and opportunities exists but is not yet in a usable or transformable format. CFA Engineering is actively working with Ryan to finalize a clean output format, and discussions are underway to expose AI Credit consumption at the thread/message-turn level in LangSmith, which currently only surfaces tokens and dollar values.

**Data Management**

**Multiple Initiatives Reached Shovel-Ready Status**: Ash finalized requirements and designs for Mask/Unmask functionality and Waterfall Release 2 with NeverBounce auto-verification, both now fully shovel-ready for engineering handoff. The team also built out Custom Waterfall concepts with Design and ran a successful cross-functional workshop to align on how audiences should adopt the GTM Data Model, with requirements groundwork now underway. Additionally, Ash rapidly reprioritized the Tools for Plays roadmap toward higher-impact use cases, incorporating learnings from GTM DM and CRM adoption in audiences.

**2026 Planning Shaped High-Priority Roadmap** (No additional action required): The team achieved alignment with leadership on Audience\'s top four initiatives for 2026, including the improved query layer interface, and began shaping next steps for requirements development. Corina progressed the Data Health Scan initiative by updating benchmarks and finalizing the account manager notification flow that will trigger Salesforce campaigns, while building proof of concept work for the AI onboarding dedupe agent and drafting a new steel thread showing how Plays will integrate with Data Management for use cases ranging from standalone CRM cleanup to multi-step plays like TAM Expansion.

**Strategic Insights**

**Key Learnings & Discoveries**

**Agent-First Development Must Replace UI-First Patterns**: The team recognized that building features agent-first is not just a nice-to-have approach but a fundamental shift in how Studio products must be developed. Current patterns like Find Contacts are built as hard-coded UI paths that agents cannot decompose into reusable steps, forcing redundant rebuilds for similar features like Find Companies. The new approach requires first building tools and APIs that agents can invoke to complete jobs, proving the use case works through agent orchestration, and only then wrapping common patterns into UI speedruns for user convenience.

**Plays Architecture Provides Supervisor Agent Orchestration**: The migration from Studio Chat to Plays unlocks a supervisor-agent architecture that current audience building lacks. Studio Chat relies on a single 85-page prompt executing one step without validation or self-correction, while Plays enables a system where a central supervisor agent delegates to specialized sub-agents with access to purpose-built tools. This decomposition prevents context window overload, enables quality evaluation at each step, and dramatically improves outcomes for multi-step use cases that are common in real customer workflows.

**Data Health Scan Drives Contributor Network Growth**: Corina\'s team discovered that CRM connections automatically enable data sharing to the contributory network by default, meaning the free Data Health Scan offering will prompt net new customers to connect CRMs and offset the cost of providing the feature without charge. This product-led growth motion creates a win-win where customers gain value through data quality insights while ZoomInfo expands its data network, making the free offering strategically valuable beyond its immediate customer benefits.

**Manual Trigger Capability Required for Automated Plays**: Mohan identified that customers need the ability to manually kick off trigger-based plays even when they have scheduled or automated runs configured. This flexibility supports testing scenarios and achieves use cases that purely automated motions cannot handle, requiring the Plays trigger design to accommodate both automated and manual invocation patterns for the same play configuration.

**Cross-Team Dependencies**

**Semantic Query Service Integration** (Clear path forward): The semantic team understands the service requirements for conversational queries that return company or contact lists for audience building, but the migration from chat-based to structured query and back to chat interfaces requires alignment on how the semantic service will function as a tool within Plays infrastructure. Jagannath and Sneh are working with the semantic team to establish the end-to-end flow, with discussions progressing and a clear path forward identified.

**Data Processing Pipeline and Plays Architecture Alignment** (Clear path forward): Current enrichment workflows run through data processing pipelines that take user input, call services like web research, wait for completion, and return results. The future state requires Plays to serve as the orchestration engine with enrichment happening as steps within plays that write back to audiences. Carlos, Tushar, and Umesh\'s teams are working with Jagannath to finalize the technical architecture, with active discussions underway to resolve how these two systems will interact.

**CRUD APIs for Audience Database Interactions**: The team needs to decouple the workbook database from the pipeline to create APIs that enable generic read, write, update, and delete operations against the audience database. This foundational work will allow Plays and other systems to interact with audiences programmatically, moving beyond hard-coded UI paths to flexible agentic interactions.

**Tools for Plays Prioritization and Development**: Ash is rapidly defining CRM Tools for Audiences requirements and aligning with Derek on separating read and write operations, potentially requiring two distinct tools (one for ingesting from data model, one for direct CRM writes). Next week includes connecting with Sam Massie on audiences adopting the connectors form to ensure proper integration patterns.

**Looking Ahead**

**Immediate Focus on Shovel-Ready Deliverables and GA Support**: The team enters next week with clear priorities to finalize clone and edit audiences requirements for engineering handoff, complete CRM Tools for Audiences specifications, and begin requirements for the improved Query Layer Interface. Arun will finalize designs for AI Credits Engagement and Studio ROI Story while supporting the field with ROI GA launch questions and any issues that surface with the newly released dashboard.

**Critical Architectural Decisions and Cross-Team Alignment**: Jagannath will continue working through the semantic query user flows, CRUD API interactions with audiences, and the Plays engine integration for audience writes and ETL tool operations. The team will maintain focus on decomposing agentic audience work into manageable components while ensuring the 2026 planning outcomes translate into tactical execution with proper cross-functional dependencies mapped and addressed.

**Finishing the Year Strong with Momentum**: With the 2026 planning providing clarity on strategic direction and the ROI GA launch demonstrating delivery capability, the team is well-positioned to close out the year. Next week\'s work will solidify requirements across multiple workstreams, ensure engineering teams have clear shovel-ready work queued, and maintain the momentum established through this week\'s planning and alignment sessions.

## **GTM Workspace Team Weekly Report - December 8-12, 2025**

**Executive Summary**

GTM Workspace delivered its first production artifact behind feature flag this week while accelerating the Chorus meetings convergence timeline by one month to February. Dylan\'s team shipped the deal status artifact to production and has meeting prep in staging, though tool reliability issues are slowing template expansion. Adam completed a fundamental system prompt rewrite that consolidates instructions and improves opportunity and account handling, positioning us for more predictable quality improvements. Gabe is finalizing requirements to compress the meetings roadmap into February delivery, with CRM updates moving to pilot next week and internal release the week after.

**This Week\'s Progress**

**Key Momentum Areas**

Dylan shipped the first artifact template (deal status) to production behind a feature flag, establishing the foundation for expanding the artifact library. The team also finalized designs for artifact pinning and gallery functionality, kicking off engineering work for the 112 release. This infrastructure will improve artifact discoverability and inspection workflows that are central to sales demos.

Adam completed a comprehensive rewrite of the Workspace system prompt that removes View Management instructions (now handled by Eric\'s sub-agent) and strengthens handling of opportunities and accounts in CRM. The new structure, inspired by Kalen\'s prompt design approach, makes the system significantly easier to fine-tune and adjust. Early testing shows consistent improvements in pulling engagement data, properly filtering for open opportunities, and connecting Salesforce context with ZoomInfo company searches.

Hari delivered the topic migration toolkit to Data Services this week, cutting customer onboarding time from competitor platforms (6sense, Demandbase) from two days to two minutes. The toolkit enables bulk keyword-to-topic mapping that Data Services will now own for pre-sales and customer onboarding scenarios, removing a significant bottleneck in competitive displacement deals.

**Goals & Progress**

**GTM Workspace**: The team made substantial progress across multiple fronts. Dylan\'s artifact templates now include deal status in production and meeting prep in staging, though reliability challenges with existing tools are slowing the remaining three templates. Gabe accelerated the meetings convergence timeline, moving from March to February delivery with Nebo committing additional resources. Email functionality progressed with engineering work on send-through-our-pipes capabilities and Outreach integration hitting stage this week for review. Adam\'s system prompt improvements position chat quality for measurable advancement, with the first eval framework run scheduled to complete by end of week. Ant\'s Pulse feed development reached system design completion with the Pulse agent taking shape, establishing the Kafka PubSub architecture that will become Workspace\'s new home screen.

**ZoomInfo Intent**: Hari advanced persona-based intent development by clarifying the 40% coverage reality with the platform team. At the job function level, only 40% of intent signals include persona enrichment, requiring adaptive UX patterns that gracefully handle mixed coverage scenarios. He\'s creating prototypes for advanced search, the intent app, and Copilot feed that account for this constraint. The platform team meeting this week will finalize signal accuracy metrics, distribution patterns, and data freshness expectations that will inform Q1 2026 roadmap execution. Meanwhile, the topic migration toolkit handoff directly supports Intent customer acquisition by streamlining competitive migrations.

**Additional Initiatives**: David\'s territories work crossed 100 activated tenants this week with MCP development progressing to expose territory definitions to the agentic layer. His team is working through complex infrastructure challenges on priority accounts, coordinating across insights, search, and target accounts teams to move from advanced search dependencies to the new filter architecture. The unlimited feed prototype (capped at 1,000 updates per day) is ready for production behind a feature flag, addressing customer requests for longer-tail white space prospecting. Ant completed initial exploration of 00 Studio with Derek and Karthik, discovering more robust triggers and workflow capabilities than the current Agentic platform, particularly for structured, rules-based agent deployment. Mobile development addressed frontend design gaps and is progressing toward internal TestFlight delivery before the holidays, with voice chat, opportunity lists, and CRM data integration taking shape.

**Strategic Challenges**

Tool reliability is impacting artifact development velocity across Dylan\'s templates. Context window limits hit immediately when the deal status agent attempts to query even a small number of deals, and basic operations like retrieving opportunity IDs from views fail inconsistently. Adam is tracking consistent failures in engagement and transcript tools through a Tiger team with Lars coordinating tool owners. The team is exploring purpose-built tools for core use cases as an alternative to generic tools, and Eric is developing a Salesforce sub-agent to reduce context bloat. Victor noted that 00 is experiencing similar challenges and is wrapping multiple tools into single tool calls, suggesting a pattern the team should consider.

David\'s priority accounts infrastructure work is navigating coordination complexity across multiple teams (insights, search, target accounts) with misaligned understanding of how to query the GTM data store and build matching rules. The current Workspace implementation relies on advanced search, which the team is migrating away from, requiring resolution of who owns what components of the new filter architecture. Additionally, querying account team data lacks a UI, complicating the admin experience for setting up appropriate matching rules that filter noise from CRM data.

Hari\'s persona-based intent faces a UX design challenge: 40% signal coverage means the product must elegantly handle scenarios where some signals include persona information while others don\'t. Building experiences that feel consistent despite this coverage gap, without either over-indexing on the feature (disappointing users when persona data is missing) or under-utilizing it (losing competitive differentiation), requires careful design thinking. The platform team meeting should clarify whether this coverage rate is stable or expected to improve.

**Strategic Insights**

**Key Learnings & Discoveries**

Adam\'s system prompt analysis revealed that the current workspace instructions are scattered and duplicative, making incremental improvements nearly impossible. Instructions about artifacts appear at both the top and bottom of the prompt, and mechanical view management details consume 20% of the system prompt. By consolidating into clear sections (product context, user context, tenant context, analysis instructions, frameworks, output handling), the team can now make discernible changes and predict outcomes. This foundational work will accelerate the pace of quality improvements going forward.

The topic migration toolkit demonstrates how eliminating manual processes in the sales cycle creates competitive advantage. By automating keyword-to-topic mapping for 6sense and Demandbase migrations, the team removed a two-day friction point that affects win rates and time-to-value. Data Services taking ownership means Product and Engineering can focus on strategic differentiators like persona-based intent while competitive displacement velocity improves.

Ant\'s 00 Studio exploration surfaced that the Agentic platform lacks true workflow and trigger capabilities that competitors are building. Derek and Karthik showed that 00 provides structured, rules-based agent deployment with triggers that fire based on data changes, whereas the current approach requires manual agent invocation. For use cases like daily territory summaries or engagement roll-ups, 00\'s architecture may be better suited, suggesting the team should evaluate which agents belong on which platform.

**Cross-Team Dependencies**

Our work with Lars and the Agentic platform team remains central to resolving tool reliability issues that affect both artifact development and chat quality. Eric\'s development of sub-agents for Salesforce tools and view management should reduce context window bloat, but timing needs coordination with Dylan\'s artifact template delivery and Adam\'s system prompt iterations. The tool failure Tiger team Lars is coordinating will determine whether the team can meet artifact velocity goals.

David\'s priority accounts infrastructure requires alignment across insights, search, and target accounts teams on the new GTM data store query patterns and filter architecture. The handoff from advanced search dependencies is complicated by ownership questions and incomplete understanding of who builds which components. Resolution here unlocks both priority accounts functionality and territory integration for the broader context services strategy.

**Looking Ahead**

Next week focuses on accelerating Workspace meetings convergence toward February delivery while establishing baseline quality metrics through the first complete eval framework run. Gabe will finalize requirements and secure design and engineering alignment on the compressed timeline following tomorrow\'s review with Victor and Nebo.

Adam\'s eval framework first run completes this week, establishing the baseline against which all future system prompt improvements will be measured. Dylan continues building the remaining artifact templates while troubleshooting tool reliability with the sub-agent approach. Hari completes the platform team meeting on persona-based intent to finalize the 40% coverage strategy and continues sales enablement agent development with eval framework implementation. David progresses MCP territory integration conversations with Lars while navigating priority accounts infrastructure coordination. Ant delivers the first version of the Pulse agent and finalizes system design for engineering handoff, targeting the India hackathon next week for frontend development. Mobile continues addressing MVP gaps (read-aloud functionality, Salesforce data for pipeline views) while progressing security reviews and app store listing preparation.

The team is positioned to show meaningful progress at RKO on January 20th, with meetings convergence, artifact infrastructure, and the Pulse feed as demonstration highlights. Tool reliability remains the pacing factor for expanding artifact templates and chat quality improvements.

*Source: Team GTM Workspace Operating Framework entries from Dec. 8, 2025 - Dec. 12, 2025*

## **Intelligence Team Weekly Report - December 8-12, 2025**

**Executive Summary**

The team finalized the January 15th plays launch plan with high confidence in scope and requirements, but facing tight timeline constraints due to the holiday period. Ryan Stevens established a critical checkpoint: all work must be divide-and-conquer ready by December 22nd to enable asynchronous execution through the holidays, with a functional system required by January 5th for the final two-week burndown. The most significant blocker emerged around GTM Data Store dependencies, where missing Chorus engagement data and improper table partitioning are preventing semantic data pipeline completion. Meanwhile, Derek Osgood successfully deployed critical tools to MQA (CRM updates, email, Slack, Outreach, SalesLoft), and Lars Vedo\'s team achieved a 70% context window reduction through sub-agent patterns.

**This Week\'s Progress**

**Key Momentum Areas**

Derek Osgood delivered the first wave of critical tools for plays, with CRM updates, email, Slack, Outreach, and SalesLoft integrations live in MQA and testing well. The routing tool remains the only outstanding component, and rate limit testing suggests no blocking concerns. Derek also identified a promising path forward: Mark\'s no-code connector tool can serve as a foundation for rapidly standing up new integration-based tools, potentially allowing new tool creation in under 24 hours.

Srivatsa Marthi closed M3 designs and stories for both the January 15th and January 30th launches, with engineering estimates expected by end of day. The team has high confidence in hitting target dates with no anticipated risks. Tree clarified how inputs will work for different trigger types, which will inform the scheduled trigger fast-follow to M3.

Lars Vedo\'s engineering team achieved breakthrough performance improvements. Eric White built a sub-agent for the Salesforce MCP tool that reduced context window bloat by approximately 70%, and the team successfully implemented Human in the Loop functionality now running in production (not yet surfaced to users). The no-code platform reached near-production readiness with RBAC protections in place, though Nathan is completing critical artifact features before final release.

**Goals & Progress**

**Plays Launch Infrastructure**: All critical tools except routing are live in MQA and performing well in testing. Derek Osgood coordinated with Mark on batch export service requirements, identifying that the jobs queue can handle bulk operations by detecting write volume and wrapping exports appropriately. The team discovered website trigger functionality is live and working on backend. Ryan Stevens finalized the project plan with full engineering alignment on material decisions, though several minor items remain to be resolved during execution.

**Semantic Data Pipeline**: Carlos Nunez and Rowan Bailey made progress on the new semantic data ingest pipeline, with James implementing a dramatically faster query layer showing 10x improvement even against the existing architecture. The target remains 100x improvement once the new pipeline is fully deployed. However, the team is currently blocked by GTM Data Store dependencies: Chorus engagement data lacks proper person IDs (backfill estimated at one week), and tables lack proper partitioning, requiring expensive full scans of 150GB datasets on every query.

**Workspace Chat & Agent Orchestration**: Lars Vedo\'s team addressed Victor\'s red alert on tool reliability by spinning up dashboards and establishing SLOs with tool-owning teams. The team is evaluating whether to migrate from the Salesforce MCP tool to GTM Store GraphQL integration, though this transition needs careful coordination given downstream dependencies. Josh is working on a breakthrough approach to retrieve and store data in BigQuery instead of context, which could be transformative for context management.

**Strategic Challenges**

The holiday timeline presents the primary execution risk for the January 15th launch. Ryan Stevens laid out the calendar reality: with most of the company out from December 22nd through January 5th, the team has effectively three full working weeks, not five. To manage this, all work must be 100% known, assigned, and divide-and-conquer ready by December 22nd, enabling asynchronous execution with minimal cross-team coordination during the holiday period. This means the team needs to frontload all major decisions and dependencies into the next 10 days, with engineers immediately moving into heads-down execution mode and being kept out of all non-essential meetings.

GTM Data Store dependencies are blocking semantic data pipeline completion and threatening the January 15th timeline. Carlos Nunez identified two specific issues: Chorus engagement data currently contains Chorus company IDs instead of Chorus person IDs (Sanyog\'s team estimates one week for backfill), and tables lack proper sorting/partitioning (forcing expensive full-table scans). Rowan Bailey noted that even with these blockers, the team cannot yet commit to the January 15th date because \"nothing can go wrong\" for the timeline to hold. The resolution requires coordination with Majed and Sanyog\'s team, potentially pulling them into focused working sessions to dramatically compress the timeline.

The Pulses API contract remains unavailable from Anne and Nebo\'s team, blocking both Derek Osgood\'s plays implementation and Carlos Nunez\'s work on next best action, Deal Acceleration Sync, and other initiatives. Without this API, there\'s no end-to-end steel thread demo possible in the two weeks before January 15th, eliminating the burndown period entirely. Adam Smith committed to chasing this down immediately after the meeting to understand what help Anne needs and to make him aware of the multiple teams waiting on this dependency.

**Strategic Insights**

**Key Learnings & Discoveries**

The sub-agent pattern emerged as a highly effective approach for managing context bloat. Eric White\'s Salesforce MCP sub-agent work, combined with Lars Vedo\'s vibe-coded sub-agent for views, demonstrated that strategically pulling in tools only when needed can reduce context windows by approximately 70%. This pattern is now being adopted across multiple use cases and represents a significant architectural improvement for agent orchestration.

Derek Osgood discovered that Mark\'s no-code connector tool, originally built for the Workflows product refactor, can serve as a foundation for rapidly building new integration-based tools. Mark demonstrated the capability by building a ServiceNow connector in 24 hours. This positions the team well for the inevitable \"do you connect to our platform?\" questions in plays sales cycles, providing a strong competitive differentiator if properly messaged to PMM and sales enablement.

Carlos Nunez\'s investigation of the new semantic data query layer revealed fundamental issues with the current chunking and vectorization strategy. Testing showed that queries like \"what are my customers saying about Clay?\" return fragments with no meaningful signal, including water cooler conversations that mention the word \"clay\" but provide no business intelligence. While re-ranking may address some of these issues, Carlos concluded that the team will need to implement a measure of whether text fragments actually provide signal before embedding them, similar to the knowledge graph approach the team used a year ago.

**Cross-Team Dependencies**

The GTM Data Store team\'s work on Chorus engagement data and table partitioning is the most critical dependency blocking semantic data progress. Rowan Bailey and Carlos Nunez need Sanyog\'s team to provide proper Chorus person IDs in engagement records (currently showing Chorus company IDs) and implement partitioning keys to avoid expensive full-table scans. The team estimates one week for the person ID backfill, but without it, the new pipeline cannot be completed. Rowan committed to working with Majed to get Sanyog and team into focused working sessions to compress this timeline, following Ryan Stevens\' suggestion to \"lock everyone in a room\" rather than wait two weeks.

The Pulses backend API from Anne and Nebo\'s team represents a shared blocker across multiple Intelligence Team initiatives. Derek Osgood emphasized that he\'s repeatedly requested the API schema, stating \"give me an API, and you will have pulses.\" Ryan McMaster\'s V1 pulses feed is ready with the basic interface in Workspace\'s top-level navigation, but without the backend contract, no integration testing or iteration can occur. Adam Smith committed to pinging Anne immediately to chase this down and ensure he understands all three blockers Carlos mentioned.

Marjud\'s GraphQL schema changes in GTM Store continue to cause downstream tool failures. Rowan Bailey reported that while some breaking changes were resolved this week, new ones emerged, causing tools built on MCPs to suddenly break. Lars Vedo emphasized the painful downstream impact: \"The field just changed name or something, and it impacts so much.\" Adam noted the embarrassment of Victor having to explain these failures to sales and go-to-market VPs in leadership meetings. Marjud has spun up a new communication channel to announce changes in advance, which should help, but the team needs more robust handling of breaking changes and upgrades.

**Looking Ahead**

The team enters execution mode with a clear focus on the January 15th plays launch. Adam Smith is canceling all recurring meetings starting in January, working with Sarah on program management to clear the calendar and add back only essential meetings. Ryan Stevens is enforcing a strict policy of keeping engineers out of all meetings starting immediately, with any meeting requests requiring his approval to determine if they\'re truly material.

The next 10 days are critical for establishing divide-and-conquer readiness. By December 22nd, the team must have 100% of known work assigned and parked under specific owners, with minimal required interaction during the holiday period. This enables asynchronous execution through the holidays, with a target of functional plays infrastructure by January 5th. From January 5th to 15th, the team has 10 days for burndown and production-readiness iteration, assuming no major surprises.

Three immediate escalations require executive attention or intervention: securing the Pulses API contract from Anne and Nebo (Adam Smith is driving this directly), coordinating GTM Data Store team focus on Chorus data and partitioning (Rowan Bailey working with Majed to arrange working sessions), and ensuring proper communication protocols for GraphQL breaking changes (ongoing with Marjud\'s team). The success of the January 15th launch depends on resolving these dependencies in the next week, as the holiday period eliminates flexibility for delayed work.

*Source: Team 1-2-3 Operating Framework entries and Friday wrap-up meeting transcript from December 8-12, 2025*

## **MCP Tiger Team Weekly Report - December 12, 2025**

**Executive Summary**

The team is tracking ahead of original infrastructure timelines, with the Data API MCP server now operational and gateway integration validated in staging. However, the window to complete composite tool construction is compressed - Zheng is out starting Wednesday, making early next week the decisive sprint for that workstream. Rowan\'s discussions with Adam P on MCP app registration confirm alignment with existing API development patterns, reducing implementation complexity for customer onboarding.

**This Week\'s Progress**

**Key Momentum Areas**

Carter Vanhuss stood up the Data API MCP server, establishing the foundation for migrating lookup, search, and enrich tools from their current location into a normalized architecture. This server completes the fifth base-level MCP server in the platform and enables consistent tool access patterns for the agent platform.

Topher Dennis validated the GTM store integration with proper specs in staging, proving out the configured service and MCP gateway architecture. The core infrastructure pathway is now demonstrated end-to-end in non-production environments, pending only production resource provisioning from DevOps.

Zheng Zhong completed a PR in the agent platform that combines search and enrich contact functionality, with local testing returning correct responses. This composite tool pattern establishes the template for subsequent tool combinations and moves toward the raw payload return capability by default.

**Goals & Progress**

**MCP Gateway Infrastructure**: Topher\'s control plane and gateway work has progressed the GTM store to full spec compliance in staging. Production deployment awaits DevOps provisioning of the GCS bucket and pub/sub resources. The team identified that internal tool visibility requires manual conversion to external status for proper role validation testing.

**Data API Server Migration**: Carter\'s new server is operational and ready to receive the lookup, search, and enrich tools currently housed elsewhere. This architectural consolidation will provide the agent platform with direct access to these foundational tools while maintaining the same capabilities through existing API paths.

**Composite Tool Development**: Zheng\'s PR for combined search/enrich contact functionality is pending approval and staging validation. The implementation currently returns summarized text responses; the team is working toward configurable raw payload returns based on the prompt pass-through parameter design discussed previously.

**Strategic Challenges**

The primary constraint is timeline compression around Zheng\'s availability. With Zheng out starting Wednesday, Carter and the team have roughly two working days to complete composite tool construction collaboration. This isn\'t a blocking issue if prioritized correctly Monday and Tuesday, but represents a coordination dependency that could create stagnation if missed.

Production deployment remains gated on DevOps resource provisioning for the GCS bucket and pub/sub infrastructure. This is standard operational dependency rather than an impediment - the staging validation gives confidence that production deployment will proceed smoothly once resources are allocated.

The team noted an open item from a prior conversation between Rowan and Brian Chase regarding target account retrieval consolidation into the search/enrich accounts tool. This architectural question - whether to maintain separate \"get accounts\" patterns or unify them with a parameter-based approach - requires scoping work that hasn\'t advanced yet.

**Strategic Insights**

**Key Learnings & Discoveries**

Carter provided clarity on the five base-level MCP servers now comprising the platform: GTM store (Topher), agents server (Carter), Salesforce (Andy), target accounts (Brian Chase), and the new Data API server. These form the foundation layer, with composite tools living one layer above in the agent platform - creating an intentional circular reference pattern where the agents MCP server both provides and consumes tools.

Rowan\'s conversation with Adam P confirmed that MCP app registration will mirror the existing API app development process - same dev portal login, secrets management, with copy changes and optional MCP-specific modifications later. This reduces implementation risk and leverages existing customer familiarity with the platform.

The composite tool architecture pattern emerging from Zheng\'s work demonstrates the intended separation: base tools return raw payloads by default, with prompt pass-through enabling LLM-processed summaries when specified. This gives orchestration layers maximum flexibility in how they consume tool outputs.

**Cross-Team Dependencies**

Our work with DevOps on production resource provisioning (GCS bucket, pub/sub) is the primary external dependency. The infrastructure requests are in queue and represent standard provisioning rather than novel requirements.

The agent platform team\'s consumption of the new Data API server tools will happen organically as the architecture stabilizes. Carter noted the platform will have immediate access but isn\'t expected to leverage these tools directly until composite tool patterns are established.

**Looking Ahead**

Next week\'s focus is singular: complete composite tool construction before Zheng\'s Wednesday departure. Carter will prioritize the lookup/search/enrich tool migration Monday morning to establish the foundation, then pivot to composite tool work with Zheng. Topher will advance composite tool specs in parallel, ensuring the framework is ready for the migrated tools.

Zheng\'s goals center on getting the PR merged, validated in staging, and establishing the ICP configuration for the new agent composite tool wrapper in the MCP server. This creates the template pattern for subsequent composite tools and demonstrates the end-to-end pathway from base tools through composite construction.

The team enters next week with infrastructure ahead of schedule and a clear two-day window to capitalize on that position before the holiday-impacted period. Execution focus Monday and Tuesday determines whether December ends with composite tools operational or deferred to January.

## **Product Ops Team Weekly Report - December 8-13, 2025**

**Executive Summary**

The Early Access release infrastructure is now operational and ready for testing, with automated tracking, phased rollout segments, and quality gates built into LaunchDarkly. Kristin Gandini completed the technical foundation including automated go-no-go tracking that pulls real-time data on feature phases and estimated dates. Meanwhile, Daniel Kong successfully piloted the feature info pack process with Dylan\'s POC in just 30 minutes, demonstrating the efficiency gains from streamlined PM workflows. The team validated their Voice of Customer semantic search approach through the vertical dataset report, proving the entity relationship mapping strategy delivers high-quality results that can be quickly adapted to new product areas.

**This Week\'s Progress**

**Key Momentum Areas**

Kristin Gandini built out the complete Early Access infrastructure this week, including LaunchDarkly segments for Phase 1 and Phase 2, plus an automated dashboard that eliminates manual tracking by pulling real-time feature status and LRT estimated dates. The system automatically flags which phase each feature is in based on targeting rules, creating a hands-off go-no-go tracking process that will scale as more features enter the pipeline.

Daniel Kong\'s redesigned feature info pack proved its value when Dylan completed the entire process in 30 minutes, from start to submission in the LRT ticket with all proper flags. The streamlined format cuts hallucination and unnecessary detail while giving downstream teams exactly what they need. Positive feedback from Dan and Shiran this week on previous recommendations means bigger improvements are coming next week to the deployment summary pulls.

Sam Darcy\'s Voice of Customer tool is now deployed in production for GTM Workspace micro apps and delivering validated results. The vertical dataset report demonstrated that the semantic search and entity relationship mapping approach works exactly as hypothesized, allowing the team to quickly pivot from GTM Studio and Workspace to vertical datasets with strong accuracy. This proves the data flow foundation will scale across product areas.

**Goals & Progress**

**Early Access Process Development**: The team ran Dylan\'s feature through the complete Early Access pipeline, exposing remaining gaps and validating core workflows. Brett Jacobs is refining the end-to-end process based on real-world testing, with particular focus on how Early Access integrates with go-to-market teams. Kristin\'s infrastructure is technically ready, though the team needs an actual feature to reach Internal Early Access phase to fully stress test the system. The LaunchDarkly segments are project-based rather than global, requiring duplicate list maintenance until the platform resolves this limitation.

**Release Automation & Content Generation**: Daniel Kong validated the weekly release pull accuracy and identified specific improvement areas with Dan and Shiran\'s team. The deployment summary received targeted back-end refinements throughout the week that should culminate in meaningful improvements when tested Monday. The feature info pack now strikes a better balance between comprehensive and concise, though the team recognizes downstream teams need clearer guidance on how to use the information rather than just receiving data dumps.

**Voice of Customer Data Activation**: Sam Darcy is preparing automated report generation for GTM Studio and Workspace to hand off to Ken Elwell before paternity leave begins. Ken is developing the release and roadmap agent with supporting communications framework to arm sellers with relevant, accurate product information. The broader challenge is determining how to activate the valuable VOC data across go-to-market teams when adoption remains difficult due to information living in disparate places.

**Strategic Challenges**

The Early Access process represents a significant cultural shift from the current \"ship fast\" mentality to building quality gates into the release process. While the technical infrastructure is complete, the real challenge lies in changing team behaviors and expectations around what constitutes readiness for different release phases. Dylan\'s Internal Early Access threshold taught the team that features need to be truly customer-ready for Phase 1, setting a much higher quality bar on Mondays than previously understood. This behavioral evolution will take time as product teams adjust their internal calibration.

Testing the Early Access system is constrained by the availability of features actually ready for the Internal phase. Without real features moving through the pipeline, the team can\'t fully validate the automated tracking, segment targeting, and downstream workflows. While this isn\'t blocking immediate progress, it does limit confidence in the system\'s resilience before broader rollout. Next week\'s GTM Studio features or Dylan\'s Workspace features may provide the necessary test cases.

Cross-team data activation presents an ongoing coordination challenge. The team has powerful Voice of Customer data and comprehensive release information, but activation remains difficult because tools and information exist in different systems. Ken Elwell and Akshut are working through this for Monday\'s meeting, exploring how to leverage VOC data more effectively rather than letting valuable insights languish in separate objection handling and talk tracking tools with poor adoption.

**Strategic Insights**

**Key Learnings & Discoveries**

Early Access will require more mental and behavioral change than technical implementation. The infrastructure works, but product teams are still calibrated to the old \"ship to GA immediately\" workflow. The realization that Internal Early Access for DAIs requires customer-ready quality means fundamentally rethinking what Monday readiness looks like. This isn\'t a policy change that happens overnight but a gradual recalibration as teams internalize the new quality standards and phased rollout philosophy.

The Voice of Customer semantic search validation through vertical datasets proved the entity relationship mapping strategy delivers consistently strong results. What\'s significant is how quickly Sam pivoted the same data flow from GTM Studio and Workspace to a completely different product area with minimal adjustment. This demonstrates the approach isn\'t narrowly tuned to specific products but represents a scalable foundation for extracting insights across ZoomInfo\'s portfolio.

Feature info pack testing revealed that providing context beats providing raw data. When Daniel just hands information to downstream teams without explaining intended usage, adoption suffers. The insight isn\'t about document format but about change management. Teams need not just artifacts but shared understanding of how those artifacts fit into their workflows. This applies equally to the Early Access communications planning for Phase 2 requirements.

**Cross-Team Dependencies**

Our work with Dan and Shiran\'s team on deployment summary automation continues to yield productive iteration cycles. This week\'s feedback loop resulted in commitment to more substantial improvements coming Monday rather than continued small tweaks. The willingness to make bigger changes shows growing alignment on what quality looks like for automated content generation. These refinements directly impact weekly release accuracy and reduce manual review burden.

The roadmap agent and communications framework Ken is developing with Victor and Snace depends on alignment around what detail level to show externally and rollout sequencing. Both leaders have solid roadmap foundations, so the remaining work centers on standardization and making information accessible in both static and agentic formats. This becomes particularly important as the team considers customer-facing Early Access opt-in infrastructure requiring clear champion communications.

**Looking Ahead**

Next week marks the final full working week of 2025, with the team focused on stress-testing Early Access infrastructure with actual features while scoping customer-facing opt-in requirements for Phase 2. The primary opportunity is finding GTM Studio features or Dylan\'s Workspace features ready for Internal Early Access to validate the automated tracking and segment targeting in production conditions rather than controlled POCs.

Daniel needs to define Phase 2 communications for downstream go-to-market teams and map out all required agents and workflows beyond the current Phase 1 foundation. This includes thinking through not just what information goes where but how to ensure teams understand the intent behind each artifact. Kristin will identify features with DAIs available for Internal Early Access testing while beginning the engineering and communications scoping for customer champion opt-in infrastructure. Ken\'s Monday meeting with Akshut on VOC data activation should clarify how to better leverage the valuable customer insights the team is now capturing systematically.

The team maintains realistic expectations about the cultural transition ahead while building confidence in the technical systems they\'ve constructed. With holiday coverage approaching, establishing clear handoff documentation and automated processes becomes particularly valuable. Sam\'s preparation of automated reporting for Ken before paternity leave exemplifies this focus on sustainable systems that run without constant manual intervention.

*Source: Team 1-2-3 Operating Framework entries from December 9-13, 2025*

## **Semantic Data Team Weekly Report - December 12, 2025**

**Executive Summary**

The team is converging on the new Gemini-based semantic data pipeline, with Jun\'s refactored embedding job now functional and James\'s query API connected and ready for integration testing. The primary focus next week shifts to scaling the embedding migration (currently processing 30 million ZoomInfo records) while Inga completes source data validation on emails. Venkata has surfaced significant GTM Datastore partitioning and authentication issues to Majid and Sanyok, who are actively working resolutions - these must be resolved before the new pipeline can go live in January.

**This Week\'s Progress**

**Key Momentum Areas**

Jon deployed an analyze job to production that identifies problematic account linkages before they enter the system, preventing the bad data quality issues that caused confusion in previous weeks. The production ingestion pipeline, paused for approximately a week to implement these safeguards, is now fully caught up and operational.

Jun completed the refactor of the embedding generation job, confirming the migration path from Titan to Gemini embeddings via the Gen AI API (Vertex AI faces deprecation next year). The job has passed functional testing on a small dataset and is ready for scale optimization. Jun also confirmed that 1024 dimensions will be maintained for consistency with production.

James has the new query API operational and connected to existing database systems. He\'s now wiring it into the semantic data agent and implementing proper error handling for no-data scenarios - a significant improvement that will eliminate the confusion that occurred when workbook users received empty responses without understanding why.

**Goals & Progress**

**Data Pipeline Migration**: Jun\'s embedding job refactor is complete and tested. The ZoomInfo tenant migration presents a scale challenge: 30 million records (65% of production data) would require 3-4 days at current throughput. The team is pursuing parallel optimization strategies including batch size increases (from 100 to 10,000 records) and job parallelization across date ranges. A shorter time window (one month instead of full history) will unblock James\'s testing next week.

**Source Data Validation**: Inga completed validation of recording data against GTM Datastore, uncovering several issues: missing speaker/participant information, transcript utterances being incorrectly merged, missing Chorus recording IDs, and missing unique account identifiers. These discrepancies have been reported to the GTM Datastore team, and Inga has adjusted queries to mitigate impacts. Email validation begins next week.

**Query Layer Development**: James now owns the semantic data agent, resolving previous ambiguity about responsibility. The API is returning data from existing tables, and James is implementing proper status messaging (\"no data available for this ID,\" \"no data in date range\") that will help downstream consumers understand query results. Jon\'s status endpoints - which indicate whether an account is processing, has fragments, has embeddings, or doesn\'t exist - will be integrated into this workflow.

**Strategic Challenges**

The GTM Datastore integration presents two infrastructure hurdles. First, the data is partitioned only at tenant level with no temporal partitions or clustering, meaning every query for incremental updates (e.g., \"new meetings since yesterday\") requires scanning 160GB of data - expensive and slow. Second, the GraphQL API that GTM recommended for new data uses user-level authentication tokens rather than service-to-service credentials, making it infeasible for our pipeline. Venkata has raised both issues with Majid and Sanyok, and the teams are actively working on solutions.

QA testing in staging has been generating confusion rather than actionable findings. The staging environment lacks meaningful data, and when QA (via Fatima) reports issues, the team cannot determine whether findings represent genuine bugs or data artifacts. Rowan will connect with Jargon to clarify the testing brief - the recommendation is to test against ZoomInfo tenant data in production rather than staging, since semantic data generation across multiple environments would be prohibitively expensive.

Token/credit constraints on the shared LLM access are causing 429 rate limit errors. When Jon prioritized the ZoomInfo ingestion pipeline this week, the same token pool that serves entity extraction for the workbook agent ran dry, resulting in failed calls on Wednesday night. The team is working to separate these token pools, and the new architecture will have James\'s agent call dedicated embedding APIs rather than sharing semantic data\'s allocation.

**Strategic Insights**

**Key Learnings & Discoveries**

The ZoomInfo tenant represents 65% of all production semantic data due to the extended lookback period and broader scope enabled for internal testing. This concentration has implications for migration planning: processing ZI first captures the majority of data but also represents the largest single workload. The team is exploring time-windowed migrations to validate the new pipeline incrementally rather than attempting a full historical backfill.

Embedding model consistency between ingestion and retrieval is non-negotiable - James highlighted that using different models for document embeddings versus query embeddings would return zero results. The team has established a \"backend pairs\" pattern where vector store configuration and embedding model are coupled together: old tables use Titan, new tables use Gemini. Jun\'s migration work will enable testing of the full Gemini pathway.

Documentation debt is accumulating during this transition period. Venkata noted that system state is being communicated through conversations rather than written artifacts, making it difficult for team members to track the current source of truth. The team agreed that a dedicated documentation day in January - once the new system stabilizes - will be essential for capturing the updated architecture and enabling future onboarding.

**Cross-Team Dependencies**

Our work with the Chorus and GTM Datastore teams is essential for pipeline completion. The Chorus team has committed to resolving the missing speaker information issue within one week, which will enable end-to-end testing of the new dataflow jobs. The GTM Datastore team is investigating both the partitioning inefficiencies and the GraphQL authentication gap. Venkata is tracking both threads and will escalate if progress stalls.

Coordination with the workbook/agent teams requires clarity on the testing strategy. James\'s API improvements will help, but the broader question of how QA validates semantic data end-to-end remains open. Rowan\'s conversation with Jargon should establish whether production testing against ZI data is acceptable, which would provide much cleaner signal than staging.

**Looking Ahead**

Next week focuses on two parallel tracks: scaling Jun\'s embedding job to process enough ZoomInfo data for meaningful testing (targeting at least one month of history), and completing Inga\'s email validation to ensure source data quality before the pipeline goes live.

Jun will experiment with batch size scaling (10,000 records) and job parallelization to reduce the 3-4 day estimate. Once sufficient embeddings exist in the new tables, James can wire up and test the complete query pathway through the agent. Jon remains available to assist with the ingestion handover once the new pipeline structure stabilizes. Inga\'s email validation is the final data quality gate - any discrepancies she identifies need immediate escalation to upstream teams.

The team is positioned to begin integrated testing in January, assuming Chorus resolves the speaker information gap and GTM Datastore makes progress on partitioning. Venkata will produce a system diagram documenting the new architecture once bandwidth allows, and Jon\'s documentation skills will be valuable for capturing operational procedures.

## **ZIM Team Weekly Report - December 8, 2025**

**Executive Summary**

The 2026 company theme is plays - making plays successful after 2025\'s data foundation work. We launched Identity Partners program this week with Alioop (an agency Henry signed) as our first major participant, deploying our pixel at scale for significant cookie coverage and intent signals. However, a critical session aggregation service that we thought 00 would handle is back on our plate, requiring urgent requirements work to deliver definitive visitor session end states for GTM Store before Q1 plays launch. Meanwhile, the California person-level intent legal question remains unresolved and needs executive decision from Ali and Dominik about whether we restrict person-level intent in California or accept the legal risk - this is particularly acute since many tech companies are California-based.

**This Week\'s Progress**

**Key Momentum Areas**

Jesse Miller achieved a major agent development milestone by successfully connecting to the analytics service endpoint (thanks to Starlow\'s guidance) and getting a reporting sub-agent prototype working. The team is delivering a comprehensive demo to Carlos by the 18th showcasing all sub-agents, which will then be presented to Henry. Email notifications reached code complete status - now just testing and deployment remain. The DeltaX meeting went well reviewing API docs and Figma UI, positioning LinkedIn campaign management for next week\'s timeline discussion with Connor and Richard.

Brett Elliot proved agent scalability at production level with 2 out of 3 agents successfully running 60K row workbooks. The emailer and web search agents are confirmed working at scale on production. The semantic data agent wasn\'t running during testing window but likely works - verification scheduled for next week. This scalability validation is critical as we move toward single agent deployment capability through the Zap Agentic Platform Runtime V2 (ZAPR) that Mehdi designed to enable Carlos\' mid-January goal of versioned agent deployments from the monorepo.

Identity Partners program officially launched this week with Alleyoop joining as a new participant. As an agency that Henry has a relationship with, they\'ll deploy our pixel across their client base, delivering substantial cookie coverage and intent signals at scale. They\'re allocated 5-6K credits monthly (200/day), and once their VP of Technology completes the onboarding flow, they\'ll become our first live identity partner. This validates the program\'s potential for exponential data expansion through agency partnerships.

**Goals & Progress**

**Agent Platform & Development**: Jesse\'s reporting sub-agent is functional with analytics service endpoint integration. Troy is handling MCP and tools while Jesse focuses on ensuring all sub-agents return proper data for the Carlos demo on the 18th. Brett\'s ZAPR work begins next week - translating Mehdi\'s plan into epics and tickets for versioned agent deployment that enables deploying semantic data agent v1 alongside web search agent v1.5 without forcing monorepo-wide updates. Anwar identified the need to make Victor\'s responsive marketing agent (from workspaces Tiger team with daily stand-ups) available for chat integration - Jesse confirmed they can just call the sub-agent classes.

**Intent Agent & Architecture**: Shuxin completed Agentic platform setup for intent and started testing. Gap analysis of intent agent use cases versus current capabilities is underway, requiring adjustments for new datasets, endpoints, and prompt changes. This week focuses on prompt refinement; heavy testing starts next week when endpoints are available to prepare as sub-agent for downstream applications. The GraphQL discussion continues with Shuxin investigating the fundamental question: why do we need GraphQL versus current architecture? Confirmed GTM Store is not viable - too much data volume and cost for bandwidth/storage. Once intent agent is operational, chat can answer complex audience queries combining website activity, intent signals, and ad exposure data.

**Session Aggregation Crisis**: The meeting with 00 revealed they\'re not building the session aggregation service we were counting on. Matt\'s team is back on the hook for creating definitive visitor session end states in GTM Store. This is critical infrastructure for plays in Q1. Matt is scrambling to fine-tune requirements today, tomorrow, and early next week based on known technical direction. The challenge is determining when user sessions definitively end to support accurate visitor journey tracking.

**Adobe Analytics & GTM Store Data**: Adobe Analytics websites integration remains on track for December 16th beta production launch, though both Lumen and NetApp are showing uncertainty about this direction versus alternatives. Matt wants to ship it regardless given the friction it\'s caused in large deals. Form complete and websites data (extra attributes) briefly reached production but caused a CI issue for form complete and required rollback. Ganesh is addressing the problem with plans to get it back into production before end of quarter - essential for Q1 plays readiness.

**GTM Config & Account/Person Context**: Aadhi completed V0 and got it reviewed, plus developed the monetization plan for Account and Person Context (renamed from \"briefs\" for clarity). Jesse L from user management team is collaborating on this. Next week focuses on wrapping the AI-first user experience for config. Account and person context scaling is progressing well - starting to publish data in BigQuery and GTM Store for downstream consumer access, which expands the data\'s utility across teams.

**2026 Planning & Roadmap**: The ZIM roadmap is complete with plays as the primary 2026 focus. You want the first slide to showcase everything launched in 2025 for year-in-review visibility. Q1 planning is advancing - Matt has his JPD populated with all epics, awaiting Q1 structure from you. Tuesday/Wednesday meetings may require adjustments. International expansion could accelerate: once data deletion and consent strings are solved, Trade Desk international ads become viable (no intent from TD, RAMP IDs aren\'t problematic), potentially enabling France, Germany, Italy, Spain plus 18 other Tier 1 countries sooner than current Q3 roadmap/end of Q2 Henry expectation.

**Strategic Challenges**

The California person-level intent legal memo forces an uncomfortable business decision. Hannah\'s assessment confirms California\'s strict laws create risk if we provide person-level intent without guaranteed consent. The question is stark: do we restrict person-level intent functionality in California, or do we accept the legal risk? This isn\'t theoretical - many tech companies are California-based, so restriction would significantly diminish the feature\'s value to our core customer base. This needs Ali and Dominik\'s executive decision on risk tolerance. Person-level intent is a key differentiator versus competitors, so restriction could hurt competitive positioning while accepting risk could expose the company legally.

The session aggregation service returning to our responsibility creates unexpected Q1 delivery risk. We architected around the assumption that 00 would handle definitive visitor session end states. Their confirmation they\'re not doing this work means Matt\'s team must rapidly define requirements and build it themselves. This is foundational infrastructure for plays - without accurate session boundaries, visitor journey tracking fails. The time crunch (must be ready for Q1 plays) means other work may need deprioritization, and the requirements refinement happening this week is critical to avoid downstream delays.

Minimizing tool calls for plays chat requires Agentic team architectural work that\'s currently undefined. Multiple tool calls create latency and cost issues, but the solution approach isn\'t clear. As we prepare agents for chat integration (website agent, intent agent, etc.), the tool call optimization becomes urgent. This ties into Victor\'s Tiger team work and the broader plays readiness, but someone needs to own the architectural solution and implementation timeline.

**Strategic Insights**

**Key Learnings & Discoveries**

The Alleyoop agency partnership model could be transformative for Identity Partners program. Rather than individual companies deploying pixels one-by-one, agencies deploying across their entire client portfolio creates exponential reach. Alleyoop gets 5-6K credits monthly for 200/day usage, and their scale should deliver substantial cookie coverage and intent signals. If this model succeeds, recruiting additional agencies becomes a force multiplier for data expansion. The VP of Technology onboarding flow will be the first real production test of the Identity Partners experience.

International expansion is more achievable than roadmap suggests if we prioritize data deletion and consent strings work. The current Q3 2026 roadmap (end of Q2 to Henry) could accelerate significantly because Trade Desk international doesn\'t require intent data or RAMP IDs - the two biggest compliance challenges. France, Germany, Italy, Spain, and 18 other Tier 1 countries become accessible once consent infrastructure is in place. Legal/outside counsel review is required for any new countries, but the technical path is clearer than expected.

Renaming \"briefs\" to \"Account and Person Context\" reflects better product positioning and clarity. The terminology was ambiguous, and the new naming convention better communicates the value proposition while aligning with monetization strategy. Publishing this data in BigQuery and GTM Store for downstream consumers transforms it from a niche feature to scalable infrastructure that multiple teams can leverage.

**Cross-Team Dependencies**

Victor\'s Tiger team (daily stand-ups) built a responsive marketing agent for workspaces that needs integration with plays chat. Jesse confirmed it\'s technically straightforward (just call sub-agent classes), but coordination between teams is required. This exemplifies the broader pattern: agents built for specific use cases need exposure through chat to maximize value. The architectural discussion about minimizing tool calls affects all agent integrations.

The 00 session aggregation revelation exposes a critical gap in cross-team coordination. We built our Q1 plays architecture assuming 00 would deliver session end state capabilities. Their clarification that it\'s not their responsibility came late enough that Matt is now scrambling to build it ourselves. This suggests we need tighter alignment on foundational infrastructure ownership - assumptions without explicit commitments create delivery risk.

Adobe Analytics integration involves Lumen and NetApp as beta customers, but both are showing ambivalence about the approach. Understanding their hesitation could inform whether we\'re solving the right problem or if alternative integration patterns would serve customers better. The friction this integration has caused in large deals suggests it\'s strategically important, but customer uncertainty raises questions about product-market fit.

**Looking Ahead**

This week is critical preparation for the Carlos demo on the 18th - Jesse needs all sub-agents returning proper data with Troy focused on MCP/tools infrastructure. Next week brings the pivotal Connor/Richard meeting to establish realistic LinkedIn campaign management timelines with API documentation and Figma designs. Email notifications move from code complete to testing/deployment phase.

Matt\'s immediate focus is finalizing session aggregation service requirements to unblock Q1 plays delivery. Getting form complete and websites data into production (fixing the CI issue Ganesh is addressing) must happen before quarter-end. Adobe Analytics beta launch on the 16th provides visibility into whether the integration approach resonates with customers like Lumen and NetApp.

Shuxin transitions from prompt changes to heavy intent agent testing next week when endpoints are available. The GraphQL architectural investigation should yield clarity on whether that\'s the right path or if alternatives better serve intent data access patterns. Brett tests semantic data agent at scale on production and begins translating Mehdi\'s ZAPR plan into actionable epics/tickets for mid-January single agent deployment capability.

Aadhi wraps up AI-first user experience for config while Account and Person Context data publishing to BigQuery/GTM Store enables downstream consumers to start building integrations. The Alioop onboarding (emailing their VP of Technology) makes them the first identity partner through the production flow - critical validation of the program\'s operational readiness.

The California person-level intent decision needs escalation to Ali and Dominik for risk assessment and business decision. You need to prepare the Q1 structure for team planning. International expansion acceleration (data deletion and consent strings prioritization) should be evaluated against Q3 roadmap commitments to Henry for end of Q2 delivery. The year-in-review slide compilation showcasing 2025 launches provides valuable context for 2026 plays-focused strategy.

*Source: Team 1-2-3 Operating Framework entries from December 8-12, 2025*

Perfect! Now I have all three missing reports. Let me add them to the appendix. I\'ll also need to update the main body to include these teams. Let me first add them to the appropriate sections in the main body:

For the main body, I need to:

1.  Add Integrations Team to \"Other Platform\" section

2.  Add Provisioning & Login Team to \"Other Platform\" section

3.  Add PMM Engine Team to \"Other Operations\" section

Here are the three missing appendix entries:

## **Integrations Team Weekly Report - December 8, 2025**

**Executive Summary**

Sanyog Rai advanced engagement junction table requirements and identifier-based processing while uncovering a significant gap in our customer data deletion process, leading him to draft cross-platform deletion requirements that need a Data Platform owner. Andres Perez completed the HG Insights and Salesforce connector listings through Partnerfleet, which are now live, but this exposed a scalability challenge requiring a database-driven API solution for the planned 10,000 additional listings. Meanwhile, strategic customer platform requests are being evaluated for delivery in Workspace versus Copilot Enterprise to manage timeline impacts and set realistic expectations with the sales team.

**This Week\'s Progress**

**Key Momentum Areas**

Sanyog Rai advanced the new engagement junction table requirements and identifier-based processing requirements, which will optimize how engagement data flows to downstream teams. While discussions with the solar team continue, the requirements are nearing sign-off and position the team to better handle the growing focus on engagement data across the organization.

Andres Perez shipped all planned Partnerfleet listings for HG Insights and Salesforce connectors this week, with the Partner Fleet Team adding the necessary JavaScript for product SKU tags. This completes the immediate goal of improving data connector visibility and reducing support questions from prospects and customers browsing the marketplace.

Cross-functional coordination on ServiceNow CRM support is progressing well, with Andres Perez working alongside Arelai to scope what delivery would look like in Workspace versus Copilot Enterprise. This analysis will help sales teams understand the true timeline trade-offs (9 months in Workspace with delays to other initiatives versus faster delivery in Copilot Enterprise) before committing to customer requests.

**Goals & Progress**

**Partnerships**: Andres Perez completed the Partnerfleet listing additions for HG Insights and Salesforce data connectors, meeting with the Partner Fleet Team to coordinate the JavaScript implementation that went live this week. Looking ahead, he\'s designing a database approach where bolded sections become features with vendor names and types that can feed the Partnerfleet API, enabling scalable creation of the remaining 10,000 listings without manual copying.

**GTM Copilot V2 & GTM Platform**: Sanyog Rai made substantial progress on two parallel workstreams - new engagement junction tables and processing based on different identifiers like email and phone number. The junction table requirements are moving through sign-offs with the solar team, while the identifier processing doc is in development and will unblock the AAT team to handle incoming data from partners.

**GTM Studio & Platform**: Strategic customer requests for GTM account role restrictions, view generation, and ServiceNow CRM support are being evaluated through Andres Perez\'s collaboration with Arelai. The team is quantifying delivery timelines and engineering effort for both Workspace and Copilot Enterprise paths, preparing data that will inform sales conversations about the 4-5 month delay impact to other roadmap items if pursued in the legacy platform.

**Strategic Challenges**

The manual Partnerfleet listing process that worked for 20 connectors won\'t scale to thousands. Andres Perez is designing a database solution where features, vendor names, and dataset equivalents feed the Partnerfleet API, but needs to decide whether to build the client UI himself or pull in someone from the Dow Jones team who already has relevant tooling. The requirement is straightforward - a UI that accepts a CSV of new listings with standardized attributes - but resource allocation needs clarification before vacation.

ZoomInfo still lacks a defined timeline for having Copilot Enterprise or GTM Workspace fully functioning from the GTM Data Model perspective - not just Views and Chat, but also Signals, Engaged Contacts, Account Fit Score, and other core features. Arelai Ephraim is supporting a program here, but without clear timelines, the team is evaluating customer platform requests without full visibility into when the foundation will be ready to support them.

Sanyog Rai discovered we lack a holistic customer data deletion process that handles tenant churn, GDPR requests, and surprise data discovery scenarios consistently. Deletion requests continue to be handled ad hoc, with maturity differing significantly between CRM data and engagement data. Current deletion is manual and fragmented, with Chorus handling engagement deletions but no automated connection to the GTM data model. Sanyog is drafting requirements for an orchestration service that can handle deletion by tenant ID or individual identifiers and propagate events across storage layers, but needs a product owner from Mark Delurgio\'s Data Platform team to own the service itself since this is fundamentally a platform capability that should send Global Event Bus signals to cascade deletions across all data copies.

**Strategic Insights**

**Key Learnings & Discoveries**

Andres Perez participated in a GTM Data Model Design workshop on December 11 with Megan Daoedsjah, where the GTM Config initiative revealed plans to restructure the sidepane and build an onboarding wizard that prompts customers to connect and configure key integrations. Andres will lead from the Platform side to ensure all product teams across ZoomInfo contribute to and own their onboarding flows within this new cohesive pattern, creating a more guided experience for customers setting up their integrations.

Sanyog Rai identified that focus on engagements is growing across the organization, which aligns well with the 2026 roadmap priorities. This validation confirms the team is working on the right problems, though it also raises the stakes for quality and completeness as more teams and customers rely on engagement data for their workflows.

The customer data deletion gap runs deeper than initially understood. Sanyog Rai\'s investigation revealed there\'s no clear request mechanism (no administrative front end equivalent to Chorus Global Admin), no approval workflow, and no automated orchestration when customers churn or request deletions. Tenant deletion is the primary use case, but GDPR individual deletions and domain-based bulk deletions also need support. Andres Perez\'s recent work on a customer deletion request highlighted that even with import rules, data persists in unexpected places, making systematic testing necessary to map what gets deleted where. The Data Platform team needs a designated owner for the deletion feature who can design it as a service across all data types.

**Cross-Team Dependencies**

Collaboration with Mark Delurgio\'s Data Platform Products team needs strengthening around the deletion service requirements. While Sanyog Rai can document integration-specific needs and coordinate with Yella on Majed\'s engineering team, this fundamentally requires a Data Platform product owner who can design the service, prioritize it against other platform work, and ensure it serves all consumers (not just integrations). Linda lacks bandwidth, so identifying the right owner is a near-term need.

The Partner Fleet Team provided immediate help by manually creating the 20 listings Andres Perez needed this week, but their API-based approach will be essential for scaling. As Andres Perez develops the database and tooling strategy, maintaining clear communication with Partner Fleet about timing and technical requirements will keep both teams aligned on when the automated approach needs to be ready.

**Looking Ahead**

Andres Perez\'s immediate priority is setting ServiceNow scope details with engineering before vacation, ensuring work can proceed during the break. He\'s coordinating with both engineering and Arelai to confirm that the Fivetran import path has everything needed for execution on the import side, while working with Frill on the export requirements.

Sanyog Rai will finalize requirements for both the new engagement junction collections and the standardized identifier-based processing, then shift into development. The customer data deletion requirements document will be ready for review, positioning the Data Platform team to begin their design work. Andres Perez will continue refining the Partnerfleet database approach, determining whether to build the client UI internally or leverage existing Dow Jones team tooling, while also taking the lead on coordinating product team contributions to the new GTM Config onboarding wizard initiative.

The team has made meaningful progress on both immediate deliverables and uncovering foundational gaps that need attention. With engagement data becoming more prominent, customer data governance requiring systematic solutions, and new onboarding patterns emerging for integration setup, the work ahead balances shipping features with building the platform capabilities that make those features sustainable at scale.

*Source: Team 1-2-3 Operating Framework entries from December 8-12, 2025*

## **Provisioning & Login Team Weekly Report - December 8, 2025**

**Executive Summary**

A key decision was finalized to allow charges for AI action credit overages up to 10% of a user\'s limit, with an approach that balances cost recoupment and customer protection. This approach, signed off by the Monetization Council, will impact the credit charging service and needs thorough testing before the January release, especially with the simultaneous introduction of \'plays\' as a charging mechanism. Additionally, the upgraded user management UI/UX is ready for release next week, which is a much-needed upgrade to set up future unified user development.

**This Week\'s Progress**

**Key Momentum Areas**

Alignment was achieved on the new AI action credit overage handling. The plan allows the charge to go through, but the customer tenant and user limit will only be charged up to a 10% overage of their limit. This \"happy middle ground\" ensures cost recoupment based on median overage amounts while protecting the customer against unexpectedly large overages.

The development for the upgraded user management UI/UX reached a milestone with a successful bug bash. A guest tester from the support team, the program manager over the Ada chatbot, provided positive feedback, stating the upgrade is \"much-needed\" and a \"way better experience,\" which has the support team excited for the release next week.

Planning activities saw good progress on building out and decomposing plays items. The team is now working with the plays team on a governance system to apply privacy and data settings for allowing first-party data that is not enriched into audiences.

**Goals & Progress**

**AI Action Credit Overages**: The decision on how to handle AI action credit overages against a user\'s limit was finalized and signed off. The approved approach is to allow the transaction to proceed but only recoup costs up to 10% of the user\'s limit as an overage, for example, 60 credits on a 600-credit limit. Reporting will be in place to track lost charges over this 10% cap.

**Charging Mechanism PRD/Requirements**: Brandon Tucker was tasked with building out the requirements for third-party data through ZI with data credits while onsite. However, due to the planning onsite going longer, Brannen Huske expects this work to roll over into next week. Brannen Huske also received asynchronous feedback on data and AI credits, which will help move forward with creating a product review document.

**User Management UI/UX**: The upgraded user management UI/UX is set for release next week. Following the bug bash, only tiny things remain to be fixed for the Minimum Viable Product (MVP) release, with some low-priority, quality-of-life bugs to follow. This release is strategic for enabling future unified user development.

**Strategic Challenges**

The finalized approach for AI credit overages will add complications to the credit charging service. This complexity requires ample time for testing, especially since the team will be introducing plays as another new charging mechanism around the same January timeline. Jessie Kain Lindstrom noted this as an awareness point requiring scoping next week to confirm the impact on the timeline.

A governance system will be necessary to apply privacy and data settings when allowing first-party data that is not enriched into audiences. Brannen Huske is working with the plays team on what this governance system will look like.

**Strategic Insights**

**Key Learnings & Discoveries**

The decision on overages was consciously balanced against past customer churn related to data credit limits and instances where users spent over their limit, often due to workflows pulling from the tenant pool instead of the user\'s limit. The new 10% overage limit provides financial responsibility while offering protection to the customer.

A significant evolution for data credits is the perspective that when AI utilizes ZI data, a data credit should be charged. This change makes the need for a combined ledger \"obvious,\" as it prevents a customer from being double-charged for processes that span an AI action that uses data credits and a subsequent export (also using a data credit).

Currently, an AI action can be performed on an audience without spending a single data credit, but the proposed evolution would change this. Brannen Huske anticipates that while more actions would trigger a charge with data credits and combined ledger would ultimately reduce overall spend for the customer, netting out to the same, but modeling is needed to confirm this.

**Cross-Team Dependencies**

The team needs to collaborate with the RevOps group to pass off the responsibility of managing the topping up of ZI Combined platform AI credits. This is a mainline product, and the RevOps group is better positioned to control the process from a business perspective, such as deciding if a large amount of spend (\$10,000 worth of AI actions) is appropriate for a task like enriching a marketing spreadsheet.

Our work with the plays team is critical to define the necessary governance system for applying privacy and data settings to first-party data that is not enriched into audiences.

**Looking Ahead**

The main focus for next week is to ensure stability in the core charging service and to solidify the foundational work for unified user management and the combined credit ledger.

Top priorities include a detailed refinement of the AI action credit overage approach with engineering and scoping its impact on the timeline, ensuring there is ample time for hardening and testing the credit charging service before the January release of user limits and the plays charging mechanism. Concurrently, the team will be releasing the upgraded user management UI/UX, which is essential to set up future unified user development. Brannen Huske will continue digging into how data credits can work in the new model where AI uses ZI data, moving toward the implementation of a combined ledger and performing the necessary modeling. This also includes getting the requirements for consolidated data credits and record center management, dependent on Brandon Tucker\'s return from the onsite.

The team is well-positioned to deliver the key components of user limits, a simplified user experience, and a more coherent credit system. The focus on hardening the charging service now will prevent issues with a growing number of paying customers and the introduction of new charging flows.

## **PMM Engine Team Weekly Report - December 8, 2025**

**Executive Summary**

The team secured a pivotal meeting yesterday with Dominik, Adam, and Rowan on go-to-market flow, generating enough information to move forward with ELT-level conversations next week before the holiday break. Jennifer Scharrer drafted ELT slides overnight following the session, positioning the team to activate cross-functional teams on Context Service/Flow launch planning. Akshath Dorai\'s objection handling agent launched this week with 58 usage instances, receiving positive feedback from 5 of 6 SDRs and account managers interviewed, though change management and distribution work remain necessary to drive broader adoption. The RKO product session skeleton is complete and ready for Dominik\'s structural feedback, acknowledging that ongoing evolution is expected as organizational thinking develops over the next four weeks.

**This Week\'s Progress**

**Key Momentum Areas**

Jennifer Scharrer completed the Context Service/Flow download session yesterday, significantly improving the team\'s understanding of the product direction. She drafted ELT slides immediately following to support next week\'s executive conversation, creating momentum for cross-functional activation before the holiday break. She also built the RKO product session skeleton, providing enough structure for Dominik to react to and contribute his thinking, and completed V2 of the Workspace in Sales Tech Landscape document through her working session with Dylan Howell.

Akshath Dorai finalized AI Action Credits messaging yesterday after reviewing transcripts from Jesse that provided insights into external market conditions. He submitted a design brief for the two required assets - a two-pager and FAQ - after consulting with Emily on enablement needs. Design is expected to pick up the work next week, with delivery of both assets anticipated within the next couple of weeks.

The objection handling agent generated measurable early traction with 58 total interactions this week. Beyond internal testing by AJ and Akshath, approximately 20 external users engaged with the tool. Akshath proactively reached out to six non-enablement users including SDRs and account managers, receiving positive feedback from five who confirmed the agent answered their questions effectively. The team successfully resolved one user complaint about response quality through hands-on support, discovering the issue stemmed from user error rather than agent performance.

**Goals & Progress**

**GTM Studio, GTM Workspace, GTM AI Context Service**: AJ Belen achieved the week\'s primary objective through yesterday\'s productive conversation with Dominik, Adam, and Rowan about go-to-market flow. The discussion provided sufficient direction to proceed with ELT-level planning next week, enabling other teams to begin their necessary preparation work. Jennifer drafted the ELT slides overnight while the information was fresh, though AJ has not yet reviewed them. The team anticipates the RKO product session structure will continue evolving as Dominik\'s thinking develops over the coming weeks, which they view as expected rather than problematic.

**Platform and Workspace Positioning**: Jennifer Scharrer and Dylan Howell completed a working session on the Workspace in Sales Tech Landscape document, building out the full first section with identified categories and vendor recommendations. The session took them through nine years of sales tech evolution, establishing strong foundational context. Dylan committed to documenting his thoughts on each category plus Workspace by end of week, after which Jennifer will transform his input into messaging and talk tracks. The document should reach completion today pending Dylan\'s delivery.

**AI Action Credits and Assets**: Akshath Dorai completed the AI Action Credits messaging work yesterday, incorporating insights from customer transcripts that Jesse shared. He finalized the design brief for enablement assets after confirming with Emily that a two-pager and FAQ would sufficiently meet field needs. The content for these assets is being finalized today, positioning design to begin work next week with anticipated delivery in the next couple of weeks for distribution through Seismic.

**Use Case Library Development**: Akshath Dorai made progress understanding the current use case library landscape, discovering that Ryan Smith created the original documentation and that enablement lacks awareness of or access to the Airtable tool. The library appears to function primarily as a solution consultant tool rather than a broadly distributed enablement resource. A working committee has been established with stakeholders from relevant teams, scheduled to meet next Thursday with Laser and the broader group to define priorities, objectives, and success metrics that remain undefined. The team needs to document how teams should use the tool at a high level and provide tactical guidance on building solution proposals step-by-step following GIP maturity and use case identification.

**Strategic Challenges**

The objection handling agent faces adoption hurdles beyond product quality, requiring active change management to overcome user resistance to new workflows. One user initially reported dissatisfaction but couldn\'t locate her original thread, then received a satisfactory response upon re-running the query - suggesting the barrier was procedural rather than substantive. AJ characterized some resistance as users wanting to be \"spoon-fed\" or preferring familiar methods, emphasizing the need for \"encouraging pressure\" to drive adoption despite confidence in the work quality. The team recognizes that style preferences will vary - some users finding responses too long while concise versions exist - making universal satisfaction impossible.

The use case library replacement project requires foundational work that wasn\'t previously completed. Ryan Smith\'s original documentation and enablement\'s lack of awareness create knowledge gaps about intended usage and reach. The team identified the need for clear documentation explaining what the tool is at a high level, how teams should use it, and tactical step-by-step guidance for building solution proposals. These documentation gaps must be addressed through next Thursday\'s working committee meeting to establish shared understanding of priorities and success criteria before development can proceed effectively.

The compressed timeline before holiday break creates urgency for ELT alignment on Context Service/Flow. Getting executive activation of other teams next week ensures planning momentum doesn\'t stall during the holiday period, though the RKO timeline adds complexity with the event approximately one month away but functionally less given holiday schedules. The team accepted that not everything needs readiness by RKO and committed to phased delivery.

**Strategic Insights**

**Key Learnings & Discoveries**

The objection handling agent incident revealed that user error can masquerade as product failure, highlighting the importance of investigating negative feedback rather than accepting it at face value. The user who initially expressed strong dissatisfaction couldn\'t reproduce her poor experience and received an excellent response upon retry, demonstrating that sellers\' perception of quality may not always reflect agent performance. This reinforces the need for the team to review feedback critically, as sellers\' proposed \"good answers\" might actually be incorrect from a strategic positioning perspective.

The Context Service/Flow download session yesterday significantly clarified product direction and go-to-market implications, validating Jennifer\'s emphasis on skeleton structures for executive feedback rather than over-invested first drafts. AJ\'s explicit acknowledgment that Dominik\'s thinking will continue evolving over the next four weeks sets healthy expectations about iteration being natural rather than problematic, protecting against perfectionism that would slow progress unnecessarily.

The use case library investigation uncovered that a tool created by Ryan Smith operates without enablement awareness or access, functioning primarily for solution consultants rather than as a broadly distributed resource. This discovery fundamentally shapes the replacement strategy, as the team must first establish clear documentation of intended usage, tactical workflows, and success metrics before building the new agent. The lack of foundational knowledge about current state means the project requires more discovery work than initially anticipated.

**Cross-Team Dependencies**

Our work with enablement on AI Action Credits assets depends on Emily\'s input being incorporated into the design brief and subsequent design team capacity next week. The two-pager and FAQ will flow through Seismic for field distribution once completed in the next couple of weeks, requiring enablement coordination on activation timing and communication.

The workspace in sales tech landscape document relies on Dylan Howell delivering his category-by-category analysis by end of week today, which Jennifer will then transform into messaging and talk tracks. She has proactively initiated conversations with enablement about activation plans, scheduling sessions to support field readiness once the document reaches final state.

The ELT conversation scheduled for next week represents a gate for cross-functional activation on Context Service/Flow. Securing executive alignment before the holiday break ensures other teams receive direction to begin their preparation work, preventing momentum loss during the compressed timeline before RKO. Jennifer\'s overnight work on ELT slides positions the team to move quickly once AJ reviews them.

**Looking Ahead**

Next week\'s ELT conversation on Context Service/Flow represents the team\'s highest priority, enabling cross-functional activation before the holiday break and establishing launch planning momentum. Jennifer will finalize the ELT slides for AJ\'s review and incorporate his feedback to ensure the presentation drives the necessary decisions and team activation.

The RKO product session requires evolution from skeleton to first draft, with the understanding that Dominik will need to contribute his thinking and that the structure will continue changing as organizational priorities clarify. The team will finalize the Workspace and Sales Tech Landscape document once Dylan delivers his category analysis today, then coordinate with enablement on activation sessions to ensure field readiness. Jennifer needs to make final decisions on the GIP gifts storyboard, evaluating whether flow considerations require changes beyond terminology for the intelligence-centered narrative, before securing early feedback from Sneh and Dominik to avoid costly late-stage animation revisions.

Akshath will complete the AI Action Credits asset content today, positioning design to begin work next week, while continuing weekly outreach to objection handling agent users to gather feedback and support adoption during the early scaling phase. The working committee meeting next Thursday with Laser and stakeholders aims to establish clear priorities, objectives, and success criteria for the use case library replacement project, addressing the documentation gaps that currently limit shared understanding of intended usage and workflows.
