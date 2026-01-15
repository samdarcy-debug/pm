---
id: synthesis-2025-43-2025
title: "Product Executive Intelligence Brief - October 24, 2025"
type: synthesis-report
status: approved
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "synthesis", "Q42025"]
---

# **Product Executive Intelligence Brief - October 20-24, 2025**

*Synthesized from 13 team reports: DAI Executive Team, GTM Studio team, SalesOS/Copilot team, Intelligence team, Data Executive team, Core Data team, GTM Data Platform team, Integrations team, Automation team, Product BI team, Product Ops team, ZIM team, User Provisioning team*

*For detailed questions about any item below, reference specific team reports or contact team leads directly.*

## **Executive Summary**

### **Summary of blockers**

Summary of blockers across team reports. For more information, use the navigation bar to look into individual team reports in the appendix.

+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Challenge/Topic**                                                                     | **Specific Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Semantic Data Scalability Blocking Enterprise Deployment Across Multiple Products**   | **GTM Studio Team:** Jagannath managed technical readiness assessment for three at-risk agent experience features with semantic search demonstrating scalability concerns and potential one-week delay beyond November 3rd deadline. Deep research achieved only 40% success rate as Google blocked bot-like query patterns with CAPTCHA challenges, requiring human-like query restructuring before production deployment to protect company reputation and IP address standing.                                                                                                                                                                      |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **Intelligence Team:** Carlos Nunez flagged that scaling the semantic service to hundreds of customers will cost millions annually. Workbooks is generating excessive agentic platform calls requiring request queue implementation. Meanwhile, there\'s organizational uncertainty about the value proposition for embedding scores like account priority into applications, with no clear urgency from Workbooks and Workspace teams despite the technical work being largely complete.                                                                                                                                                              |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Agent Infrastructure Scalability & Resource Constraints Threatening November 3rd GA** | **ZIM Team:** Brett Elliot assumes workbooks agent scalability responsibility requiring deployment of production-ready container orchestration by October 31st for November 3rd workbooks GA. Current architecture spawns individual containers per cell causing Kubernetes health check failures and resource exhaustion requiring fundamental infrastructure redesign with Ryan, Grant, Sean, Richard, Cy, and Mehdi coordination.                                                                                                                                                                                                                   |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **Intelligence Team:** Frontend resourcing creating deployment bottlenecks. Derek\'s team has one frontend developer working on 00 staging migration, which is taking longer than expected and putting the December delivery timeline at risk. The team can likely move quickly on tools integration once Andy Harganto is fully onboarded, but having a single developer creates fragility. Additional frontend support would accelerate the critical path to getting plays socialized and tested in real environments.                                                                                                                               |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **Automation Team:** MCP credit consumption unpredictability blocks enterprise adoption, with Adam Peretz discovering that the stateless MCP server architecture prevents cost estimation before queries execute. Beta partners specifically cited concerns about queries that could consume thousands of credits in seconds, refusing to enable access without guardrails that engineering indicates won\'t be easy to implement.                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM Data Model & Schema Dependencies Creating Cascading Delivery Risks**              | **SalesOS/Copilot Team:** Copilot Workspace faces a compound challenge around chat-to-views accuracy that Sean Walter flagged as the top priority for November 3rd. The team is seeing inconsistent results when users ask chat to create views, particularly when mixing CRM and ZoomInfo data. Adam Severance is building out golden query examples to train the orchestrator agent, but the underlying issue stems from limited documentation on the GTM data model\'s GraphQL endpoint.                                                                                                                                                            |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **GTM Data Platform Team:** Schema gaps and technical dependencies continue to require careful coordination across teams. While Menna Rashwan achieved initial alignment with Data Producers, mapping exposed several coverage issues including missing fields and mismatched data types that impact search use case coverage. Some MVP fields do not map cleanly to proposed GraphQL scalars, though this gap may be mitigated if Data Producers supply the expected data types. Additionally, fields that need to be indexed as both code and value for sorting, faceting, and filtering will require coordination through a shared mapping service. |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **Data Executive Team:** Brandon\'s work integrating GTM Store data revealed significant data quality issues in the standard opportunity tables, with deal amounts showing negative numbers, unrealistic values like \$100 million, or missing entirely. The GraphQL API returns more reasonable values for these same opportunities, indicating that direct API integration provides more reliable data than relying solely on ZDP tables.                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Enterprise Partnership & MCP Adoption Blockers Requiring Executive Intervention**     | **Automation Team:** Sales team lacks Claude access for customer demonstrations, with Mike Fawkes and other salespeople unable to demo MCP capabilities to strategic customers. Adam Peretz is working with Rowan Bailey to establish access protocols, but the current infrastructure doesn\'t support sales team demonstration needs.                                                                                                                                                                                                                                                                                                                |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **Data Executive Team:** The Board of Directors and Executive Leadership Team data requests are coming with increasingly varied requirements from different enterprise customers, each with unique nuances around scope, data elements, and delivery formats. While the research team has built a scalable manual process for Barclays, transforming this into a hardened product requires product ownership, clear prioritization, and engineering support to handle multiple employment relationships more gracefully in the platform.                                                                                                               |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Resource Allocation & Engineering Capacity Constraints Across Strategic Initiatives** | **Core Data Team:** Resource allocation emerged as the dominant challenge during onsite discussions. Magnus Herweyer\'s shared services initiative and Heather Ma\'s agent development work both lack dedicated engineering teams, forcing reliance on borrowed resources and creating delivery uncertainty. Without defined engineering velocity or committed resources, these strategic initiatives risk remaining in perpetual prototype status.                                                                                                                                                                                                    |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **ZIM Team:** Anwar Mai manages resource reallocation reducing Inferno to 2.5 engineers and Clickagy to 6-7 engineers requiring cutline establishment across 42 projects for executive presentation. The capacity constraints necessitate difficult prioritization decisions balancing agent infrastructure, GTM Config, DMP development, international expansion, and Connected TV against available engineering bandwidth.                                                                                                                                                                                                                           |
|                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | **GTM Studio Team:** Front-end resourcing gap for data health scan GTM Studios integration being addressed through collaboration with Carlos\'s analytics team. Brahm coordinating with Chad\'s team to onboard analytics engineer effectively into engineering scrum body of work.                                                                                                                                                                                                                                                                                                                                                                    |
+=========================================================================================+========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+

### **Relevant context across reports**

This section surfaces relevant information from team reports across the organization relevant to the given domain area

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Domain Area & DAI**             | **Cross-Team Dependencies & References (from OTHER team reports)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM Studio (Sneh)**             | **Intelligence Team:** Derek Osgood built the first actual plays in the 00 workspace using live tools, providing tangible examples the team can test and refine. While staging deployment is delayed due to frontend resourcing constraints, having working plays demonstrates the vision concretely and will accelerate alignment across teams working on this initiative. Srivatsa Marthi has begun critical architectural planning for signals migration with strong support from Andres and Brandon that will modernize how signals feed into plays and create a more flexible, efficient foundation for the platform going forward. |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **SalesOS/Copilot Team:** Adam Severance confirmed the workbook-to-workspace end-to-end flow is operational and faster than previous iterations, with artifact generation notably improved. This unlocks the ability to demonstrate seamless migration from legacy workbooks during executive demos, supporting the positioning that Workspace represents evolution rather than disruption for existing workflows. Gabe Pirela made critical progress on send via Outreach functionality by identifying the full dependency chain, with contacts must first exist in Outreach before sending, requiring export flow implementation       |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Data Executive Team:** Brandon integrated the GTM Store GraphQL API into the deal cycle analysis pipeline and added company segmentation classification, allowing the agent to group insights by deal size, company segment, and industry. Igor\'s team ingested the complete FINRA dataset into Snowflake with CRD numbers for every U.S. broker and investment advisor, now working with Peter to identify customer-facing fields for productization as a potential PitchBook alternative.                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **ZIM Team:** Aadhitthyaa Hari Gopal advanced identity data partner onboarding coordination across five teams with Privado order form completion scheduled for next week maintaining November 18th GA timeline. GTM Config offerings generation succeeded for SurveyMonkey, SupportLogic, and Cvent while Berlin Packaging site crawling failure reveals technical limitations requiring investigation for production readiness.                                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Product Ops Team:** Ken Elwell completed a V1 version of the Copilot Workspace automated digest that successfully translates PRs and deployments into business language. Sam Darcy achieved strong results on the VOC data quality report with highly accurate and efficient fragment filtering, positioning the system to roll it out to PMs and validate the 2026 roadmap against customer needs.                                                                                                                                                                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Copilot Workspace (Victor)**    | **Intelligence Team:** Lars has two weeks remaining to tune agents for ZoomInfo\'s internal rollout. Following the user survey, priorities include adding Chorus engagements, enabling view creation with ZI data, improving source citations, customizing for ZI\'s Salesforce configuration, and fixing target accounts functionality. Ryan Stevens is coordinating to ship all remaining projects by 11/3, setting up the following week for intensive agent accuracy tuning.                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Studio Team:** Mohan achieved confidence for November 3rd workbook-to-Copilot activation release, creating extensive support materials and working with content team on knowledge articles and how-to guides. Workspace copilot chat can only process top 2,000 rows despite displaying full lists beyond that threshold, creating potential customer friction when sellers request chat to prioritize larger lists.                                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Data Platform Team:** The leadership team set the strategic sequence as Federated Search before External API, validating that the current GraphQL path is extensible for Copilot Workspaces and vertical datasets. Product and engineering achieved top-to-bottom product and engineering alignment on making Federated Search integration with GraphQL a P0 priority, positioning December 31 delivery as achievable if remaining technical work proceeds on schedule                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Automation Team:** Sam Massie completed DoubleO alignment work, revealing that GTM Plays requires deterministic action libraries with user inputs complementing agentic capabilities, with Slack, Outreach, and Salesloft activations prioritized.                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Product Ops Team:** Ken Elwell completed a V1 version of the Copilot Workspace automated digest that successfully translates PRs and deployments into business language using GitHub PRs and Jira tickets. The V1 output caught more than Sean\'s customer-focused release notes, demonstrating potential to finally solve the translation gap that keeps downstream teams hours or days behind engineering velocity.                                                                                                                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **GTM AI Context Service (Adam)** | **GTM Studio Team:** ROI instrumentation requirements for workbooks and workspace need prioritization with Jagannath and Randy\'s engineering teams to enable analytics data collection. Semantic search packaging and provisioning decisions need resolution across product management, with questions on GTM Studio and Copilot inclusion, access controls, entitlement processes, configuration levels, and AI credit charging patterns (pre-processing vs retrieval).                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **SalesOS/Copilot Team:** Adam Severance\'s views work depends heavily on the GTM data model team\'s GraphQL endpoint documentation, which currently has minimal data taxonomy and implementation guidance. This creates downstream problems where the views team must reverse-engineer how to properly query for engagement data, account team objects, and other CRM fields. Ant Cuomo identified that the current agent evaluation process is too slow with agents must be pushed to production before meaningful testing can occur on real data.                                                                                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Automation Team:** Adam Peretz discovered that the stateless MCP server architecture prevents credit estimation before queries execute, with beta partners refusing adoption unless guardrails are implemented to prevent runaway credit consumption. Sales team lacks Claude access for customer demonstrations, with Mike Fawkes and other salespeople unable to demo MCP capabilities to strategic customers.                                                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Data Platform Team:** Menna Rashwan finalized alignment with App teams on MVP search use cases, prioritized fields, and expected behavior, while resolving missing schema fields with Data Producers. The team now has top-to-bottom product and engineering alignment on making Federated Search integration with GraphQL a P0 priority, positioning December 31 delivery as achievable if remaining technical work proceeds on schedule.                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **ZIM Team:** Shuxin Yang progressed ALI data GTM Store ingestion coordination with Linda while completing retroactive intent outage stabilization before sales team messaging deployment. Vendor 20-signal limitation requires intent aggregation strategy development determining signal definition scope and standard topic utilization approach.                                                                                                                                                                                                                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Data (Brandon)**                | **GTM Studio Team:** Platform team\'s GTM data model backfill work critical for ROI December GA timeline, with CFA team validation results determining cutover schedule. Arun\'s team validated short-term solution for backfilling historical opportunity data from legacy BigQuery into GTM data model tables, with CFA engineering team conducting data accuracy verification.                                                                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **SalesOS/Copilot Team:** ZoomInfo Intent discovered an architectural issue where AFS limit checks operate at user-level rather than platform-level, creating confusion for customers with both Copilot and ZIM seats. While Harinath is working with provisioning to build a proper platform-level API, this reveals a broader pattern where entitlement logic was built for single-product customers and breaks down as the portfolio converges.                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Intelligence Team:** Srivatsa secured backing from Andres and Brandon for deprecating the current signals layer, with the plan to have raw data sources feed directly into GTM Store. This architectural shift will eliminate meaningful technical debt and create a more efficient system for how signals trigger plays and provide context to agents                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Data Platform Team:** Dominik and Filip established strategic sequencing clarity this week, prioritizing Federated Search in Graph QL ahead of the Graph QL API public beta release. Menna Rashwan worked through schema discrepancies with Data Producers, identifying that the current schema was missing key fields required for search use cases.                                                                                                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **ZIM Team:** Matt Barnes learned from OO workflow management that connected agents approach provides tremendous data processing flexibility requiring consideration in future signal pipeline architectural decisions. Aadhitthyaa Hari Gopal discovered partner audience match rate optimization potential through firmographic data enhancement beyond current name and domain matching with 20-90% variance suggesting significant improvement opportunities.                                                                                                                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Platform (Ali)**                | **Intelligence Team:** Platform teams (GTM Data Model, RBAC, Integrations) are blocking Copilot V2 progress. Sean Walter has repeatedly flagged that sharing, collaboration, and real-time CRM sync capabilities require commitments from dependent teams. Without these foundations, the Intelligence team risks building temporary solutions internally that create technical debt.                                                                                                                                                                                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **SalesOS/Copilot Team:** Adam Severance\'s views work depends heavily on the GTM data model team\'s GraphQL endpoint documentation, which currently has minimal data taxonomy and implementation guidance. Andres and the platform team are supportive but stretched thin, suggesting we may need dedicated API documentation resources to unblock multiple product teams consuming GTM data model simultaneously.                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Studio Team:** Platform dependencies block multiple Studio capabilities, with Victor noting that waterfall enrichment work transfers to Brandon\'s team and will cascade across products once introduced in Studio. The team discussed that you \"can\'t introduce it in one place and not everywhere else,\" requiring coordination with workspace, copilot, and other surface areas                                                                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Automation Team:** Marc Frail is on track to launch Global Event Bus with initial GTM CDC events by next week\'s end, enabling broader platform event consumption. The team also released backstage tooling that provides UI-based event registration for publishers, simplifying the event publishing workflow significantly                                                                                                                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Data Executive Team:** Suresh successfully implemented the Contributory Network eligibility status flag in Salesforce with values now populated in Snowflake, enabling downstream systems to distinguish between full sharing, partial sharing, and no sharing contracts. Brandon integrated the GTM Store GraphQL API into the deal cycle analysis pipeline and added company segmentation classification.                                                                                                                                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Operations (AJ)**               | **Intelligence Team:** Ryan Stevens and Lars identified fundamental issues with how the agent creates views in Workspace with it evaluating field names and filters but not actual data, leading to poor results when users ask for \"top opportunities\" or similar queries. Additionally, Workbooks\' default sort by create date means large queries return essentially random subsets of results.                                                                                                                                                                                                                                    |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **SalesOS/Copilot Team:** The user survey Adam Severance launched revealed that while 75 respondents feel Workspace has improved their workflows, they rate chat accuracy and speed as neutral, indicating improvement needed before wide release. Dylan Halladay made substantial progress on slides artifact with working PDF download and basic templates, targeting early November internal release before customer rollout                                                                                                                                                                                                          |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **GTM Studio Team:** Corina\'s data health scan proof of concept meetings with over 40 account managers generated concrete results, advancing 3 opportunities totaling \$400K in pipeline for RingLead sales. Account managers found the messaging around invalid emails (\"this TAM is unreachable\") and duplicate impact on AI analysis particularly compelling as conversation starters with customers.                                                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | **Product BI Team:** The team established mandatory analytics review for all feature launches through required Jira tickets, building on the process improvement Phoebe Mei secured with Sean and Adam last week. This ensures event tracking is reviewed before features go live, addressing the longstanding gap where engineering teams shipped features without proper instrumentation.                                                                                                                                                                                                                                              |
+===================================+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+

### **Update on Previous Week Blockers**

**Web research quality degraded severely after vendor switch, threatening workbooks integration:** The Intelligence Team reports resolution in progress with \"Carlos and James are now testing Perplexity against Google Gen AI Search with 1,000-run sample size comparisons\" following the complete performance collapse when switching from Brave to Melifera. The DAI Executive Team confirms \"semantic data scaling presents the most urgent technical blocker, with Sneh reporting the service currently fails beyond 150 records despite being marketed as a core feature\" and notes \"Adam acknowledged the problem differently than Sneh understood it---he focused on cost scaling while the actual issue involves retrieval completely stopping, suggesting coordination gaps.\"

**GTM Data Model gaps continue blocking multiple initiatives:** The GTM Data Platform Team reports breakthrough progress with \"the Platform engineering/PM team has identified the ROI GA path. After coordination with Platform PM/Engineering (Andres, Asaf), and CFA PM/engineering (Brahm/Arun/Ashwani), the team aligned on short-term (Platform backfills legacy ZDP data into GTM Data Model) and long-term (full opportunity history ingestion from CRMs) approaches.\" However, execution timeline remains pending as \"Prateek\'s team committed to ETA delivery next week.\"

**Design resource constraints blocking November 3rd launch readiness:** The GTM Studio Team reports continued challenges with design resourcing though path forward exists through restructuring. The DAI Executive Team notes broader resolution as \"Design work advanced on the November release with Meghan\'s team addressing AI credits UI, embedded chat improvements throughout workspaces, and slide presentation artifacts. The team initiated a light reorganization creating a dedicated Tiger team to examine the end-to-end experience.\"

**DoubleO stack adoption forcing comprehensive roadmap reassessment:** The Intelligence Team reports significant progress with \"Derek Osgood advanced DoubleO tool migration faster than expected, with staging deployment complete and QA underway on all core tools.\" The Automation Team confirms continued alignment as \"Sam Massie completed DoubleO alignment work, revealing that GTM Plays requires deterministic action libraries with user inputs complementing agentic capabilities.\"

### **Current Week Update**

**Blockers:**

- **November 3rd launch faces substantial technical gaps requiring immediate resolution:** The DAI Executive Team reports \"three foundational issues threaten the Studio release: inadequate dataset availability, semantic scaling limitations that prevent enrichment beyond 150 records, and missing connector infrastructure despite six months of development time.\" The Intelligence Team confirms \"semantic search scalability concerns emerging\" with \"Carlos Nunez flagged that scaling the semantic service to hundreds of customers will cost millions annually.\"

- **MCP credit consumption unpredictability blocks enterprise adoption:** The Automation Team reports \"Adam Peretz discovered that the stateless MCP server architecture prevents credit estimation before queries execute, with beta partners refusing adoption unless guardrails are implemented to prevent runaway credit consumption.\" Sales team additionally \"lacks Claude access for customer demonstrations\" with \"Mike Fawkes and other salespeople unable to demo MCP capabilities to strategic customers.\"

**Momentum areas:**

- **Dreamforce delivered strong validation with workbook-to-workspace integration achieving its \'aha moment\':** The DAI Executive Team reports \"Based on Studio enablement sessions and Workspace customer demos, the workbook-to-workspace integration achieved its \'aha moment\' with sellers, though the user experience has a lot of potential for improvement where users go from using Views to having a simple list of actions they need to take.\" The SalesOS/Copilot Team confirms \"Copilot Workspace shipped critical workbook-to-workspace functionality to production this week, completing a major milestone for migrating legacy workflows.\"

- **Platform infrastructure achieving production readiness across multiple teams:** The GTM Data Platform Team reports \"Dominik and Filip established strategic sequencing clarity this week, prioritizing Federated Search in Graph QL ahead of the Graph QL API public beta release\" with \"top-to-bottom product and engineering alignment on making Federated Search integration with GraphQL a P0 priority, positioning December 31 delivery as achievable.\" The Automation Team confirms \"Marc Frail is on track to launch Global Event Bus with initial GTM CDC events by next week\'s end, enabling broader platform event consumption.\"

**Bottom line:** November 3rd launch readiness requires immediate resolution of semantic data scalability and dataset availability issues identified as foundational gaps. Dreamforce successfully validated the workbook-to-workspace orchestration story with sellers and customers, but technical execution gaps threaten to undermine market positioning if not resolved in the next two weeks. Platform infrastructure teams are achieving critical alignment on federated search and event bus capabilities, but MCP enterprise adoption blockers need executive intervention to resolve credit consumption concerns and sales team access issues.

### **GTM Studio**

**GTM Studio Team:** \"November 3rd launch enters final countdown with critical technical decisions needed on semantic search. Sneh is driving launch readiness across enablement sessions and demo hardening, with field foundations training reaching 1,000 sellers and demo deep dives progressing for solution consultants. Workbooks positioned for November launch with Jagannath managing go/no-go decisions on semantic search, deep research, and data agent migrations, while Tanvi focused on launch materials and find contacts enhancement requirements. Plays achieved confidence on workbook-to-Copilot activation readiness with Mohan coordinating enablement content and working Double-O AI credit requirements for M2 scope. ROI Analytics unblocked platform data model tables with Arun validating historical opportunity data backfill and preparing for December GA, while Stephen Antuna\'s staff push creates urgency for sales leadership alignment. Data Management made substantial progress with Corina meeting 40+ account managers and generating \$400K in pipeline advancement using data health scan proof of concept, while Ash drove AI data management toward January POC readiness despite front-end resourcing gaps.\"

### **GTM Copilot Workspace**

**SalesOS/Copilot Team:** \"Copilot Workspace shipped critical workbook-to-workspace functionality to production this week, completing a major milestone for migrating legacy workflows. Sean Walter is leading a quality assessment framework ahead of November 3rd release, identifying chat stability and view performance as top priorities that need attention. Meanwhile, Gabe Pirela confirmed dependencies for outreach integration---a frequently requested feature that was a friction point in V1---with development starting next week targeting fast-follow to 11.3 release.\"

### **GTM AI Context Service**

**Intelligence Team:** \"The team is now two weeks out from full sales enablement for ZoomInfo\'s agentic platform. Following user feedback, Lars Vedo has a prioritized improvement list covering Chorus engagements, ZI data views, source citations, and Salesforce customizations. Derek Osgood is pushing to get the first 2-3 actual plays live in staging, which will enable concrete socialization across teams and reduce abstract conversations about how plays should work. Meanwhile, Srivatsa Marthi has begun critical architectural planning for signals migration---with strong support from Andres and Brandon---that will modernize how signals feed into plays and create a more flexible, efficient foundation for the platform going forward.\"

### **Vertical Datasets**

From **Data Executive Team report:** \"Board of Directors and Executive Leadership Team datasets are attracting significant enterprise attention beyond our initial Barclays deployment. ServiceNow, AlphaSense, RBC, and others are requesting this data with varying requirements, creating an opportunity to transform a one-off custom deliverable into a productized offering. We need product ownership and a clear support framework to scale this demand while maintaining quality.\"

### **Other Data**

**Data Executive Team:** \"Board of Directors and Executive Leadership Team datasets are attracting significant enterprise attention beyond our initial Barclays deployment. ServiceNow, AlphaSense, RBC, and others are requesting this data with varying requirements, creating an opportunity to transform a one-off custom deliverable into a productized offering. We need product ownership and a clear support framework to scale this demand while maintaining quality. Meanwhile, the Contributory Network V2 infrastructure is production-ready with eligibility flags now available in Salesforce and Snowflake, enabling expanded data sharing for opportunities and calendar data.\"

**Core Data Team:** \"The Core Data team conducted their strategic onsite this week, focusing on four key areas: developing big bets for 2026, establishing a waterfall enrichment plan, aligning with analysis and engineering teams, and strengthening team cohesion through team building activities. Jody Roberts successfully facilitated sessions covering these critical planning areas while the team presented strategic initiatives targeting \$10M+ incremental revenue opportunities. The onsite revealed both significant opportunities in data infrastructure and persistent challenges around resource allocation, particularly for Magnus Herweyer\'s shared services vision and Heather Ma\'s agent development initiatives which lack dedicated engineering support.\"

### **Other Platform**

**GTM Data Platform Team:** \"Dominik and Filip established strategic sequencing clarity this week, prioritizing Federated Search in Graph QL ahead of the Graph QL API public beta release. Timing of GQL public beta release will be evaluated down the road, but it\'s not an immediate priority. Menna Rashwan finalized alignment with App teams on MVP search use cases, prioritized fields, and expected behavior, while resolving missing schema fields with Data Producers. The team now has top-to-bottom product and engineering alignment on making Federated Search integration with GraphQL a P0 priority, positioning December 31 delivery as achievable if remaining technical work proceeds on schedule.\"

**Integrations Team:** \"The team made progress this week with steady momentum on GTM Data Manager development and continued focus on Agentforce enablement. Sanyog Rai is advancing self-service configuration capabilities while the team prepares comprehensive documentation for the January 31, 2026 compliance deadline requiring all ZoomInfo teams to access CRM and Engagement data exclusively through GTM Data Manager APIs.\"

**Automation Team:** \"MCP credit consumption concerns threaten enterprise adoption while GTM Plays requirements clarify action library priorities. Adam Peretz discovered that the stateless MCP server architecture prevents credit estimation before queries execute, with beta partners refusing adoption unless guardrails are implemented to prevent runaway credit consumption. Sam Massie completed DoubleO alignment work, revealing that GTM Plays requires deterministic action libraries with user inputs complementing agentic capabilities, with Slack, Outreach, and Salesloft activations prioritized. Marc Frail is on track to launch Global Event Bus with initial GTM CDC events by next week\'s end, enabling broader platform event consumption.\"

**ZIM Team:** \"AI Page Rank early access launched successfully Tuesday with Matt Barnes working with CX recruiting 5-6 beta customers while workbooks agent scalability issues require urgent resolution before November 3rd GA deadline. Brett Elliot transitions to workbooks infrastructure team deploying scalable agent architecture by October 31st as team navigates resource reallocation cutting Inferno to 2.5 engineers and Clickagy to 6-7 engineers. Partner audience match rate optimization opportunities identified ranging 20-90% requiring firmographic enhancement beyond name and domain matching.\"

### **Other Operations**

**Product Ops Team:** \"The team reached an exciting milestone on the Copilot Workspace automated changelog with Ken Elwell delivering a strong V1 (with the help of Guy Levin) that demonstrates AI can effectively track and translate technical releases into business language using GitHub PRs and Jira tickets. Sam Darcy achieved strong results on the VOC data quality report with highly accurate and efficient fragment filtering, positioning the system to roll it out to PMs and validate the 2026 roadmap against customer needs. Kristin Gandini solved the feedback loop challenge by creating a JPD logging mechanism that captures PM decisions in near real-time. However, Caleb Munson has shared that annual planning alignment remains difficult with mixed stakeholder perspectives on what worked and what should change, requiring focused leadership discussion next week.\"

**Product BI Team:** \"The team is maintaining focus on tactical event instrumentation work while preparing for post-launch analytics needs. Inbal Kor created a new dashboard tracking the GTM Studio signal feature and successfully coached Ferrell Tanuwidjaja on building GTM Studio taxonomies independently. The team established mandatory analytics review for all feature launches through required Jira tickets.\"

*For deeper analysis on any topic above, reference specific team reports or contact team leads directly.*

*Methodology: Analysis of team 1-2-3 Operating Framework reports, prioritizing: (1) Executive decisions needed, (2) Cross-team blockers, (3) Strategic momentum areas, (4) Strategic alignment gaps*

# **📊 Appendix**

### **Individual Team Reports**

## **DAI Executive Team Weekly Report - October 20-24, 2025**

**Executive Summary**

The November 3rd launch faces substantial technical gaps requiring immediate resolution. While workspace activation demos strongly and semantic data shows promise, three foundational issues threaten the Studio release: inadequate dataset availability, semantic scaling limitations that prevent enrichment beyond 150 records, and missing connector infrastructure despite six months of development time. Based on Studio enablement sessions and Workspace customer demos, the workbook-to-workspace integration achieved its \"aha moment\" with sellers, though the user experience has a lot of potential for improvement where users go from using Views to having a simple list of actions they need to take.

**This Week\'s Progress**

**Key Momentum Areas**

Copilot Workspace enablement sessions and Dreamforce demos went well. The Studio to Workspace activation demo flow resonates with both customers and our own sellers. Victor and Sneh will continue to make it a top priority to make the Studio to Workspace experience simpler for sellers. Adam completed the platform narrative with AJ, positioning it for final review with sales leadership and enablement, while Marc\'s platform team maintains green status across all major November deliverables including GraphQL API readiness and the global event bus.

Customer demos for Workspace generated 15 requests over two weeks, with three-quarters responding positively that it\'s exactly what they\'re looking for. Victor noted that cost concerns arise consistently, particularly from customers already invested in OpenAI and Anthropic contracts, though discussions about the go-to-market context and MCP server help pivot conversations from build-versus-buy skepticism toward partnership interest. Sneh ran enablement sessions for GTM Studio Foundations and Demo Deep Dive with positive field feedback, confirming that workspace activation serves as the critical aha moment for sellers.

Design work advanced on the November release with Meghan\'s team addressing AI credits UI, embedded chat improvements throughout workspaces, and slide presentation artifacts. The team initiated a light reorganization creating a dedicated Tiger team to examine the end-to-end experience and develop a design improvement roadmap, while also establishing more effective intake processes between PM and design teams to reduce friction points.

**Goals & Progress**

**Platform Infrastructure:** Marc\'s team progressed all November deliverables to green status, including GraphQL API for workspace enrichment, email/meetings/websights in GTM Store, usage-based pricing for AI credits, and the ZI Revenue Agent for Agentforce. The team plans to release an MVP version of the GraphQL API as a public beta by December 1st, stripped down to exclude entitlements but providing access to first-party data and engagements. Early feedback from apps teams surfaced the need to prioritize GTM data model normalization for customers integrating multiple CRMs with different opportunity stages.

**Workspace Readiness:** Victor\'s team shipped the workbook-to-workspace integration as functional though aesthetically compromised, with Adam noting during demos that while it \"demo\[s\] fine\" and \"sells the platform vision,\" the team is \"doing the very minimum viable version of just clearing that bar.\" The outreach integration remains yellow-to-red status with Gabe working to identify exact barriers, while natural language view creation deployed behind a feature flag Monday will require several weeks of internal testing before customer release. User experience research revealed non-trivial numbers of users failing at basic tasks like setting up views and invoking chat, prompting plans for dedicated UX improvement sprints in December.

**Studio Launch Preparation:** Sneh coordinated enablement sessions targeting November readiness, focusing on agentic creation go/no-go decisions, semantic service availability, dataset lockdown, and connector deployment. The team developed vertical-specific use case content that will convert to template workbooks, with SC demos moving into production and AM-focused templates demonstrating the platform end-to-end from studio to workspace. AJ advanced AI credit assets with Jesse, positioning them as next week\'s priority following the platform narrative completion, while also working to close remaining gaps identified in Monday\'s launch readiness assessment.

**Strategic Challenges**

Semantic data scaling presents the most urgent technical blocker, with Sneh reporting the service currently fails beyond 150 records despite being marketed as a core feature. The team cut \"build workbook from semantic\" entirely from the November scope and now fights to salvage semantic enrichment and deep research endpoints, with engineering promising a Friday go/no-go decision. Adam acknowledged the problem differently than Sneh understood it---he focused on cost scaling while the actual issue involves retrieval completely stopping, suggesting coordination gaps in how problems are being communicated and addressed across teams.

The federated search and GraphQL integration has slipped repeatedly from August through February to now April, despite being identified as the single most important dependency for the entire roadmap. Dominik\'s frustration surfaced during Marc\'s update about potentially releasing a public API by December 1st, emphasizing that every engineering team and product depends on this foundation and that the entire leadership spent two days in Bethesda specifically to align on this priority. The external API work was definitively deprioritized, with Dominik requiring daily progress reports from the entire platform team on federated search advancement.

Dataset availability remains critically insufficient for a November launch, with Dominik noting they\'re launching with essentially two signals (website buyer ID and contact changes) when sellers expect comprehensive ZoomInfo data access. The connector infrastructure shows similar gaps---despite six months claiming the ability to build any connector, the reality is near-zero production connectors. Brandon\'s team works to understand external workbook building patterns to determine whether to prioritize waterfall API enrichment or big table enrichment capabilities, with the answer dependent on how often users lack LinkedIn URLs as enrichment inputs.

**Strategic Insights**

**Key Learnings & Discoveries**

The orchestration-to-execution narrative resonates strongly in customer conversations, with Victor observing that after Sneh\'s Foundations demo, customer requests for Workspace now organically include Studio. This validates the platform vision where Studio and Copilot presented together create significantly more defensible positioning than either product standalone. Early access cohort analysis revealed that of 22 accounts, only four qualify as healthy and getting value, with three additional accounts seeing value but stuck without activation---prompting an extension of early access through November 30 to leverage workspace activation.

Adam\'s architectural review of the workbook-to-workspace integration revealed systematic issues with how artifacts generate and render at scale. The team built workarounds in each area independently rather than creating a unified system, including hard-coded UUIDs in previews, manual inference turns to bring up artifacts in chat, and user context problems where emails generate with the wrong person\'s signature. His concern centers not on technical debt itself but on the likelihood that \"there\'s more things today we need to do net new, than we can revisit old things,\" making temporary solutions effectively permanent.

The pricing conversation gap emerged as a blind spot, with customers consistently asking for translations from AI credit abstractions to concrete capabilities like \"how many emails can I send?\" This validates AJ\'s prioritization of customer-facing AI credit assets for next week, though the team hasn\'t yet solved how to make these translations accessible during sales conversations. Dominik emphasized preferring a simple table on Monday over perfect customer-facing assets on Friday, acknowledging the need for progressive refinement.

**Cross-Team Dependencies**

The semantic team\'s resource volatility creates execution uncertainty, with Danny Pan\'s departure and engineers being pulled back to Newport disrupting committed roadmaps. Adam plans detailed Q4 roadmap reviews to ensure full resourcing and clear individual accountability given the vagueness introduced by these changes. Carlos leads most of the work, but Adam wants specific individuals assigned to each deliverable rather than generic team-level commitments.

Platform dependencies block multiple Studio capabilities, with Victor noting that waterfall enrichment work transfers to Brandon\'s team and will cascade across products once introduced in Studio. The team discussed that you \"can\'t introduce it in one place and not everywhere else,\" requiring coordination with workspace, copilot, and other surface areas. Similarly, Jagan identified multiple aspects of the agentic-to-workbook-to-workspace flow still needing design support for November, prompting Meghan to commit to frequent check-ins ensuring all connections are covered.

The accessibility requirements for Microsoft and USPS contracts create compliance risk that Victor and Vivek discussed offline, with some items qualifying as low-hanging fruit while others represent potentially irrational customer requests requiring product leadership intervention. Microsoft\'s primary push appears focused on demonstrating progress rather than specific technical requirements, suggesting a middle-ground approach balancing genuine accessibility needs against performative compliance theater.

**Looking Ahead**

Next week centers on the final sprint toward November 3rd readiness, with board meeting and off-site preparations mostly complete per Dominik\'s assessment. The platform narrative enablement session Tuesday represents a critical alignment checkpoint, requiring final sign-off from Henry and James before broader field distribution. Victor\'s dedicated sprint on orchestration-to-action user experience begins toward week\'s end, potentially consolidating with AI Compete\'s post-workspace-launch reviews to create cross-platform alignment sessions.

The semantic go/no-go decision arrives Friday with significant downstream implications---if the team cannot reliably process beyond 150 records, it forces either delaying the November launch or releasing with a feature that doesn\'t match its marketing. Adam committed to pulling this thread immediately with Carlos after recognizing he misunderstood whether the problem involves cost scaling versus technical failure. Brandon\'s waterfall enrichment requirements finalize once Tushar provides visibility into workbook creation parameters, determining whether the team prioritizes external API waterfall or big table enrichment based on LinkedIn URL availability in customer data.

Studio positioning crystallizes through next week\'s customer sales motions, with Sneh scheduling 3-4 pricing discussions to test messaging and validate the calculator approach. The team\'s ability to demonstrate clear dataset availability, working semantic enrichment, and published connectors will determine whether the November launch proceeds or requires deferral. Dominik\'s characterization that \"this thing is not ready\" two weeks from launch suggests the executive team may need to make a hard decision about release timing versus delivering a minimum viable product that risks damaging market perception.

*Source: DAI Executives Operating Framework entries from Monday October 20, 2025 - Friday October 24, 2025*

## **GTM Studio Team Weekly Report - October 20-24, 2025**

**Executive Summary**

November 3rd launch enters final countdown with critical technical decisions needed on semantic search. Sneh is driving launch readiness across enablement sessions and demo hardening, with field foundations training reaching 1,000 sellers and demo deep dives progressing for solution consultants. Workbooks positioned for November launch with Jagannath managing go/no-go decisions on semantic search, deep research, and data agent migrations, while Tanvi focused on launch materials and find contacts enhancement requirements. Plays achieved confidence on workbook-to-Copilot activation readiness with Mohan coordinating enablement content and working Double-O AI credit requirements for M2 scope. ROI Analytics unblocked platform data model tables with Arun validating historical opportunity data backfill and preparing for December GA, while Stephen Antuna\'s staff push creates urgency for sales leadership alignment. Data Management made substantial progress with Corina meeting 40+ account managers and generating \$400K in pipeline advancement using data health scan proof of concept, while Ash drove AI data management toward January POC readiness despite front-end resourcing gaps.

**Key Momentum Areas**

**Data Health Scan Driving Tangible Revenue Impact.** Corina\'s data health scan proof of concept meetings with over 40 account managers generated concrete results, advancing 3 opportunities totaling \$400K in pipeline for RingLead sales. Account managers found the messaging around invalid emails (\"this TAM is unreachable\") and duplicate impact on AI analysis particularly compelling as conversation starters with customers.

**Platform Data Model Unblocked for ROI GA.** The platform team completed backfilling historical opportunity data from legacy BigQuery tables into GTM data model tables. CFA engineering team validating data accuracy to make a decision on whether they are good to cutover to GTM DM tables.

**November Launch Technical Readiness Under Review.** Jagannath led go/no-go decision-making on three at-risk capabilities for November 3rd launch: semantic search facing scalability concerns, deep research encountering Google CAPTCHA blocking at 40% success rate due to bot-like query patterns, and data agent migration where user feedback revealed strong preference for maintaining side panel control alongside new chat experience.

**Goals & Progress**

**Workbooks**

**Progress - November 3rd Launch Capabilities Require Critical Decisions:** Jagannath managed technical readiness assessment for three at-risk agent experience features. Semantic search demonstrated scalability concerns with potential one-week delay beyond November 3rd deadline. Deep research achieved only 40% success rate as Google blocked bot-like query patterns with CAPTCHA challenges, requiring human-like query restructuring before production deployment to protect company reputation and IP address standing. Data agent migration feedback showed users valued side panel control and flexibility, prompting decision to offer both chat and traditional side panel interfaces rather than forcing chat migration. Tanvi progressed launch readiness by creating product briefs and finalizing find contacts phased approach, though designer assignment remained needed to begin design work.

**Strategic Challenges - Balancing Innovation with User Control (Clear path forward):** User feedback on data agent chat migration revealed preference for maintaining existing side panel control rather than full chat migration. Solution identified to offer both experiences, allowing users to trigger chat while retaining side panel functionality, enabling organic adoption feedback for November 3rd release. Deep research bot detection issue has clear resolution path through query pattern humanization work underway by engineering team.

**Plays**

**Progress - Copilot Activation and Double-O Integration Advancing:** Mohan achieved confidence for November 3rd workbook-to-Copilot activation release, creating extensive support materials and working with content team on knowledge articles and how-to guides. Double-O integration progressed with M2 scope requiring AI credit requirement definition, with unique needs for GTM plays differing from workbooks and workspaces. Jesse engaged on designing zero credit, low credit, and during-processing scenarios specific to plays workflows. Technical learnings emerged around feature limitations, including inability to match opportunity owner without opportunity ID in CRM, requiring requirement adjustments to use account owner instead.

**Strategic Challenges - Workspace Chat Volume Limitations Identified (No additional action required):** Workspace copilot chat can only process top 2,000 rows despite displaying full lists beyond that threshold, creating potential customer friction when sellers request chat to prioritize larger lists. Issue documented for future prioritization with Lara\'s team after gathering customer feedback post-launch. Opportunity owner matching limitation resolved through requirement adjustment to use account owner.

**ROI Analytics**

**Progress - Platform Blocker Resolved, Sales Leadership Push:** Arun\'s team validated short-term solution for backfilling historical opportunity data from legacy BigQuery into GTM data model tables, with CFA engineering team conducting data accuracy verification. GTM Team\'s success with Indeed, Zendesk, Orkin, Zoom and other customers using ROI prompted request for sales leadership meeting to drive broader usage, creating increased urgency for December GA readiness. Workbook metrics scope finalized, though instrumentation and pipeline discussions with Jagannath and Randy awaiting prioritization. Sales enablement reconnection initiated with Gabe Sweet\'s team to prepare full enablement plan and content readiness for GA approach.

**Strategic Challenges - AI Credits ROI Story Undefined (Clear path forward):** Team lacks comprehensive approach for tying AI credits consumption back to ROI measurement and customer value storytelling. Brahm identified need to define requirements after completing workbooks and workspace ROI requirements. Workspace Q4 scope discussions with Adam Severance revealed open questions around how agent artifacts should update with each load, preventing finalization of engineering execution plan. Traditional account-level value realization storytelling needs expansion for broader AI experience beyond accounts.

**Data Management**

**Progress - Proof of Concept Generating Pipeline, January POC Tracking:** Corina\'s data health scan proof of concept delivered measurable business impact with 40+ account manager meetings resulting in 3 opportunities totaling \$400K in pipeline advancement for RingLead sales. Version 2 development kicked off with backend data science work recalculating metrics and adding new capabilities, leveraging Yoav\'s GTM Studio designs for proof of concept validation. Milestone 3 (data health scan in GTM Studios) finalized PRD and designs with PRD review scheduled for following Monday, targeting January 12th demo-ready date. Ash progressed AI data management M2 testing for RingLead CFA dashboard and changelog development for November release, defined clear MVP scope for January milestone, received high-fidelity wireframe designs, and validated M4 dev start, staging, and production dates. RingLead usage analysis revealed same-object dedupe as primary pattern with account-to-account matching most popular, informing AI onboarding configuration proposals.

**Strategic Challenges - Front-End Resource Gap Creating Risk (No additional action required):** Data health scan GTM Studios integration lacks identified front-end resource, creating potential risk for January 12th demo-ready target. Sequencing discussions between Corina and Ash\'s work given shared engineering team. Brahm working with Carlos\'s analytics team to onboard available analytics engineer to address capacity. ICP gap messaging resonating strongly with account managers, with potential to expand to relationship coverage analysis - account managers may need persona expansion to RevOps and sales ops contacts for data quality discussions rather than traditional new business stakeholders.

**Strategic Insights**

**Key Learnings & Discoveries**

**Data Quality Messaging Finds Sweet Spot in AI Context:** Corina discovered account managers achieved strongest customer reactions when framing duplicates and invalid data through AI analysis lens. Messaging that \"if 20% of your CRM is duplicates, all AI learnings and responses will be built off that duplicate data, giving you wrong business decisions\" created immediate \"aha moments\" more effectively than traditional data quality metrics.

**User Control Preferences Trump Forced Chat Migration:** Jagannath\'s data agent migration feedback revealed users highly value existing side panel control and flexibility despite appreciating chat capabilities. Product decision to offer both experiences rather than forcing migration demonstrates importance of meeting users where they are while gathering organic adoption data.

**ROI Storytelling Evolution Beyond Account-Level:** Arun identified that traditional ROI value realization focused on account-level metrics (accounts researched, signal interactions) doesn\'t fully capture broader AI experience value. Workspace activities not tied to specific accounts require some thinking on if and whether we should show ROI from those activities.

**Semantic Search Production Readiness Requires Rigorous Quality Bars:** Deep research encountering Google bot detection at 60% failure rate highlights need for production-ready quality thresholds beyond internal testing success. Protecting company reputation and IP address standing requires careful consideration of external service dependencies and rate limiting patterns.

**Cross-Team Dependencies**

ROI instrumentation requirements for workbooks and workspace need prioritization with Jagannath and Randy\'s engineering teams to enable analytics data collection. Platform team\'s GTM data model backfill work critical for ROI December GA timeline, with CFA team validation results determining cutover schedule.

Front-end resourcing gap for data health scan GTM Studios integration being addressed through collaboration with Carlos\'s analytics team. Brahm coordinating with Chad\'s team to onboard analytics engineer effectively into engineering scrum body of work.

Semantic search packaging and provisioning decisions need resolution across product management, with questions on GTM Studio and Copilot inclusion, access controls, entitlement processes, configuration levels, and AI credit charging patterns (pre-processing vs retrieval). Brandon and Jesse\'s AI platform team managing credit ledger, namespaces, and deduction services as central dependency for all applications.

**Looking Ahead**

November 3rd launch execution dominates immediate focus with readiness review identifying specific call-outs on job posting operator work, P0 signal defects, and semantic search technical decisions. Enablement sessions beginning this week with foundations and demo deep dives for 1,000 sellers and solution consultants, supported by dry runs and content team coordination with Rochelle and Gabe Sweet\'s team.

Production demo environment hardening continues with solution consultants running all Copilot and Studio demos from production environment. Connector display workflows and write restrictions from demo environment to Salesforce instances represent gotchas requiring refinement, but no show-stopping blockers identified.

Data management momentum accelerates toward January POC with Corina focusing PRD finalization, design completion for milestone 3, and continued AM meetings to track customer successes. Ash driving M4 design work with newly assigned designer Lareina Yap, daily engineering working sessions, and GTM fields dependency resolution. Version 2 proof of concept incorporating Yoav\'s designs to validate layout and metrics feedback.

ROI GA preparation intensifies with Stephen Antuna staff meeting scheduled to lay out rollout plan and scale usage across sales organization. Sales enablement content development with Gabe Sweet\'s identified resource, workbook and workspace instrumentation handoff to engineering teams, and AI credits ROI requirements definition following workbook/workspace completion. Platform data model cutover execution pending CFA validation results determines December GA feasibility.

*Source: GTM Studio Operating Framework and team sync recordings from October 20-24, 2025*

## **SalesOS/Copilot Team Weekly Report - October 20-24, 2025**

**Executive Summary**

Copilot Workspace shipped critical workbook-to-workspace functionality to production this week, completing a major milestone for migrating legacy workflows. Sean Walter is leading a quality assessment framework ahead of November 3rd release, identifying chat stability and view performance as top priorities that need attention. Meanwhile, Gabe Pirela confirmed dependencies for outreach integration---a frequently requested feature that was a friction point in V1---with development starting next week targeting fast-follow to 11.3 release.

**This Week\'s Progress**

**Key Momentum Areas**

Copilot Workspace achieved a significant technical milestone with workbook-to-workspace activation going live in production. Adam Severance confirmed the end-to-end flow is operational and faster than previous iterations, with artifact generation notably improved. This unlocks the ability to demonstrate seamless migration from legacy workbooks during executive demos, supporting the positioning that Workspace represents evolution rather than disruption for existing workflows.

ZoomInfo Intent launched Multi AFS and Intent Recommendation Phase 2 to production in ZIM this week. Harinath Krishnamoorthy validated both features are live and stable, though discovered an entitlement conflict for customers holding both Copilot and ZIM seats that requires platform-level resolution. The team is working with provisioning to deliver a proper API for determining AFS limits at the organizational level rather than user level, eliminating admin confusion about configuration capabilities.

Admin Zero Experience work was deliberately paused by David Goulden given uncertainty about scope and ownership with Tingting\'s team handling broader offerings setup. While this removes immediate November pressure, it reflects strategic alignment that Workspace will inevitably need admin screens but rushing artificial deadlines without organizational readiness creates downstream problems. David is instead focusing Admin Defined Territories toward GA in November with final UI tweaks for user summary reports.

**Goals & Progress**

**Copilot Workspace:** Sean Walter established a quality go/no-go framework identifying four must-have elements for November 3rd: chat accuracy on core AEAM use cases, reliable view creation from chat using CRM and ZoomInfo data, views improvements for quality of life and polish, and first-time user experience optimization. Adam Severance\'s user survey at 75 respondents reveals users rate chat accuracy and speed as neutral, indicating improvement needed before wide release. Dylan Halladay made substantial progress on slides artifact with working PDF download and basic templates, targeting early November internal release before customer rollout.

**ZoomInfo Intent:** Harinath completed validation testing for Intent Recommendation Phase 2 and Multi AFS in production, achieving the October 21st launch target. Demo instance configuration remains blocked pending provisioning team resolution of package setup through fullbox2 system. The team scheduled three enterprise customer interviews next week to gather feedback on intent recommendation quality, continuing the validation approach of testing with real customer scenarios before broader rollout.

**Admin Zero Experience:** Work formally deferred this week as David Goulden confirmed with Victor that artificial rushing of admin portal features without clear organizational alignment on scope and ownership creates more problems than it solves. The team will revisit in 2-4 weeks as Workspace admin requirements become clearer through actual usage patterns. Meanwhile, admin-defined territories continues toward November GA with user summary reports and territory assignment UI refinements in development.

**Additional Initiatives:** Gabe Pirela made critical progress on send via Outreach functionality by identifying the full dependency chain---contacts must first exist in Outreach before sending, requiring export flow implementation. Rather than just adding a send button, the team scoped the complete workflow including contact verification and sequence addition. Ant Cuomo\'s Next Best Actions agent reached production with improved engagement context from GTM data store, though the account prioritization agent missed Monday\'s release and should deploy by end of week.

**Strategic Challenges**

Copilot Workspace faces a compound challenge around chat-to-views accuracy that Sean Walter flagged as the top priority for November 3rd. The team is seeing inconsistent results when users ask chat to create views, particularly when mixing CRM and ZoomInfo data. Adam Severance is building out golden query examples to train the orchestrator agent, but the underlying issue stems from limited documentation on the GTM data model\'s GraphQL endpoint. This creates a scenario where the product technically works but doesn\'t reliably deliver on the core promise of natural language view creation, which multiple sales leaders identified as their primary blocker to running their business in Workspace.

ZoomInfo Intent discovered an architectural issue where AFS limit checks operate at user-level rather than platform-level, creating confusion for customers with both Copilot and ZIM seats. While Harinath is working with provisioning to build a proper platform-level API, this reveals a broader pattern where entitlement logic was built for single-product customers and breaks down as the portfolio converges. The team needs a systematic review of entitlement architecture to prevent similar issues as more features span multiple products.

Admin work is revealing scope ambiguity across teams, with David Goulden, Tingting\'s team, and the GoToMarket Studio group all touching admin-related surfaces without clear domain ownership. Victor and David agreed to defer zero admin setup until this organizational alignment happens, but the underlying challenge remains: as Workspace scales, customers will need robust admin capabilities for user management, territory configuration, and feature entitlements. The decision to pause is pragmatic, but we need a dedicated owner to drive the admin strategy forward before GA.

**Strategic Insights**

**Key Learnings & Discoveries**

The user survey Adam Severance launched revealed that while 75 respondents feel Workspace has improved their workflows, they rate chat accuracy and speed as neutral---a concerning signal for our primary differentiation point. The qualitative feedback frequently references ZI Chat, confirming we\'ll always be compared against the bespoke tool regardless of Workspace\'s broader capabilities. The insight here is that views-plus-chat only creates differentiation if they work seamlessly together; mediocre chat performance undermines the entire value proposition even when views are solid.

Dylan Halladay\'s exploration of slides artifact implementation uncovered a critical tradeoff: Google Slides API approach offers better rendering but has limited functionality, while PPTX approach provides more control but can\'t render in-app without download. Ryan Stevens and Lars are pushing to release behind a feature flag this week for internal testing, demonstrating the value of getting working prototypes in front of users quickly even if not customer-ready. The lesson is that perfect shouldn\'t be the enemy of good enough for internal validation.

Ant Cuomo\'s work on pulses revealed that defining default pulse types requires cross-team alignment on what constitutes a pulse versus other notification types. The team met with Derek from the 00 team and identified that pulses need clear definitions, types, and phasing before the infrastructure work can proceed effectively. This highlights how seemingly simple features require significant upfront design work to prevent scope creep and misaligned expectations across engineering teams.

**Cross-Team Dependencies**

Our work with the agentic platform team on Next Best Actions continues to be essential for profile quality in the December 3rd release. Ant Cuomo identified that the current agent evaluation process is too slow---agents must be pushed to production before meaningful testing can occur on real data. The team needs better guidance on tool selection and context configuration, as Ant discovered he was pulling engagement data from the wrong source initially. The agentic platform is powerful but the developer experience for product managers iterating on prompts and configurations needs improvement to support the pace of experimentation required.

Adam Severance\'s views work depends heavily on the GTM data model team\'s GraphQL endpoint documentation, which currently has minimal data taxonomy and implementation guidance. This creates downstream problems where the views team must reverse-engineer how to properly query for engagement data, account team objects, and other CRM fields. Andres and the platform team are supportive but stretched thin, suggesting we may need dedicated API documentation resources to unblock multiple product teams consuming GTM data model simultaneously.

**Looking Ahead**

The team is laser-focused on November 3rd release readiness, with Sean Walter\'s quality framework providing the checkpoint criteria. Chat accuracy on core AEAM use cases is the single most important element---if we can\'t reliably answer basic CRM questions, nothing else matters. Adam Severance is finalizing golden query examples for the orchestrator agent by end of day today, enabling Ryan Stevens\' team to tune the model before Monday\'s release of chat-to-views improvements.

Gabe Pirela kicks off send via Outreach development next week, targeting completion in 1-2 weeks as fast-follow to 11.3. This addresses one of the most frequently requested features from the sales team and removes a major friction point from V1. Dylan Halladay aims to have slides artifact ready for internal testing by early November, giving the sales team time to provide feedback before any customer release. Ant Cuomo is finalizing mobile prototype by tomorrow and meeting with the chat team to align on dependencies for webview approach.

The strategic priority for the next two weeks is ruthless focus on November 3rd must-haves while preventing scope creep on nice-to-haves. Sean\'s quality framework provides the forcing function to make tough tradeoff decisions. We\'re building a product that can win in market, but only if we nail the fundamentals of chat accuracy, view reliability, and first-time user experience. Everything else is secondary until those foundations are solid.

*Source: Team SalesOS/Copilot Operating Framework entries from Oct. 20, 2025 - Oct. 23, 2025*

## **Intelligence Team Weekly Report - October 20-24, 2025**

**Executive Summary**

The team is now two weeks out from full sales enablement for ZoomInfo\'s agentic platform. Following user feedback, Lars Vedo has a prioritized improvement list covering Chorus engagements, ZI data views, source citations, and Salesforce customizations. Derek Osgood is pushing to get the first 2-3 actual plays live in staging, which will enable concrete socialization across teams and reduce abstract conversations about how plays should work. Meanwhile, Srivatsa Marthi has begun critical architectural planning for signals migration---with strong support from Andres and Brandon---that will modernize how signals feed into plays and create a more flexible, efficient foundation for the platform going forward.

**This Week\'s Progress**

**Key Momentum Areas**

GTM Studio plays reached functional prototype stage. Derek Osgood built the first actual plays in the 00 workspace using live tools, providing tangible examples the team can test and refine. While staging deployment is delayed due to frontend resourcing constraints, having working plays demonstrates the vision concretely and will accelerate alignment across teams working on this initiative.

User feedback driving targeted improvements for Dreamforce. Sean and Adam collected and prioritized seller feedback from the Copilot and Copilot Chat survey, identifying specific accuracy and tool-calling issues. The team is staying focused on raising response quality rather than adding new features, with new agent versions testing in staging today and production releases planned for the coming days.

Signals architecture modernization gaining organizational support. Srivatsa secured backing from Andres and Brandon for deprecating the current signals layer, with the plan to have raw data sources feed directly into GTM Store. This architectural shift will eliminate meaningful technical debt and create a more efficient system for how signals trigger plays and provide context to agents.

**Goals & Progress**

**GTM Studio:** Derek is working to deploy the first 2-3 plays in staging with tools including search, scrape, research, docs, spreadsheets, ZI Data, CRM, email, Slack, and LinkedIn capabilities. Staging deployment is blocked on frontend resourcing (currently one developer), but tools are being tested in the 00 workspace environment. The Global Event Bus integration looks promising for trigger signals, though some gaps exist between currently available signals and the plays wishlist that will need addressing through scoring and other mechanisms.

**GTM Copilot Workspace:** Lars has two weeks remaining to tune agents for ZoomInfo\'s internal rollout. Following the user survey, priorities include adding Chorus engagements, enabling view creation with ZI data, improving source citations, customizing for ZI\'s Salesforce configuration, and fixing target accounts functionality. Ryan Stevens is coordinating to ship all remaining projects by 11/3, setting up the following week for intensive agent accuracy tuning. The team is balancing stability for 11/3 while testing new agent architecture in staging.

**GTM AI Context Service:** Rowan Bailey completed and shared a PRD for the Account Brief team, detailing section-by-section breakdowns for the updated GTM Store schema, target enrichment sections, and priority ordering for the next few months. This provides more granular account context retrieval for agents and the context service MCP. Srivatsa is working through open architectural questions around how plays should consume content outside GTM Store, including scores, Workbooks, and buying groups.

**Strategic Challenges**

Frontend resourcing creating deployment bottlenecks. Derek\'s team has one frontend developer working on 00 staging migration, which is taking longer than expected and putting the December delivery timeline at risk. The team can likely move quickly on tools integration once Andy Harganto is fully onboarded, but having a single developer creates fragility. Additional frontend support would accelerate the critical path to getting plays socialized and tested in real environments.

View creation reliability hampering user experience. Ryan Stevens and Lars identified fundamental issues with how the agent creates views in Workspace---it evaluates field names and filters but not actual data, leading to poor results when users ask for \"top opportunities\" or similar queries. Additionally, Workbooks\' default sort by create date means large queries return essentially random subsets of results. Robyn documented that competitors like Ocean.io and Clay have similar problems, creating an opportunity to differentiate if ZoomInfo can implement intelligent ranking through APS or other scoring mechanisms.

Context service and semantic data scalability concerns emerging. Carlos Nunez flagged that scaling the semantic service to hundreds of customers will cost millions annually. Workbooks is generating excessive agentic platform calls requiring request queue implementation. Meanwhile, there\'s organizational uncertainty about the value proposition for embedding scores like account priority into applications, with no clear urgency from Workbooks and Workspace teams despite the technical work being largely complete.

**Strategic Insights**

**Key Learnings & Discoveries**

Signals deprecation timing reveals broader architectural debt. The enthusiastic support Srivatsa received from multiple leaders for deprecating the signals layer suggests the team was late in proposing this change. The current architecture creates \"meaningful debt with every passing month\" as stated in the operating documents. Moving to a model where raw data sources feed directly into GTM Store, with processing logic living in plays rather than a separate signals layer, will provide the flexibility needed for custom insights and play triggers while eliminating redundant systems.

Product naming and architecture misalignment creating confusion. The team discussion revealed significant confusion between Workbooks (a database for RevOps to build complex lists) and Workspace (a simpler execution layer for frontline sellers). Ryan Stevens noted that even product people struggle to keep them straight, despite the mental model making logical sense. The underlying architecture diverges sharply---Workbooks uses arbitrary advanced search queries snapshotted into tables, while Workspace dynamically queries Salesforce with ZoomInfo column enrichment. This disconnect between user expectations and implementation reality poses product strategy risks.

Email sequencing can and should live in plays. Derek\'s conversation with Gabe confirmed that doing sequences outside structured tools like Outreach should just be implemented as plays. The team has waiting mechanisms, email sending capabilities, and tracking---the main gap is exit criteria for sequences (like pulling people out when they reply). Ryan noted this is trivial to add with LLMs. Rather than building standalone sequencing infrastructure, using plays as the execution layer provides a cleaner architecture and avoids duplicating capabilities.

**Cross-Team Dependencies**

Our work with the Workbooks team on agentic integration remains critical for GTM Studio adoption. The team needs alignment on how plays consume data and provision work to sellers. Snee\'s team is designing how workbooks get pushed to reps via the \"activate\" button, creating views that sellers can execute through Workspace chat. However, scalability concerns around agentic platform calls require implementing request queuing to throttle volume. Additionally, the Workbooks team needs to handle tokens and cost tracking as they integrate semantic data and other inference-heavy capabilities.

Platform teams (GTM Data Model, RBAC, Integrations) are blocking Copilot V2 progress. Sean Walter has repeatedly flagged that sharing, collaboration, and real-time CRM sync capabilities require commitments from dependent teams. Without these foundations, the Intelligence team risks building temporary solutions internally that create technical debt. The upcoming API Gateway work and GraphQL tooling for unified profile data should help, but explicit prioritization from leadership would accelerate these critical integrations.

**Looking Ahead**

The next two weeks are all about ZI sales enablement. Lars and Ryan Stevens will focus on stability, accuracy improvements, and agent tuning rather than new features.

Derek will continue pushing plays into staging with all available tools, working to demonstrate concrete value and socialize the execution model broadly. Getting even basic plays running will shift conversations from theoretical to practical and help identify remaining tool gaps and architectural needs.

Srivatsa will drive alignment on signals migration architecture, working with Platform (Linda, Majed), S2A (Brian C.), and other teams to answer open questions about how plays consume scores, buying groups, and other non-GTM-Store content. The team will also plan the specific migration path to get from current state to target architecture while supporting immediate use cases, potentially consuming directly from GSO in the short term even if that\'s not the long-term solution. Rowan will focus on getting the MCP gateway, auth, entitlements, and RBAC clear for the Context Service to go live with potentially sensitive sources like engagements and semantic data.

*Source: Team Intelligence Operating Framework entries from October 20, 2025 - October 24, 2025*

## **Data Executive Team Weekly Report - October 20-24, 2025**

**Executive Summary**

Board of Directors and Executive Leadership Team datasets are attracting significant enterprise attention beyond our initial Barclays deployment. ServiceNow, AlphaSense, RBC, and others are requesting this data with varying requirements, creating an opportunity to transform a one-off custom deliverable into a productized offering. We need product ownership and a clear support framework to scale this demand while maintaining quality. Meanwhile, the Contributory Network V2 infrastructure is production-ready with eligibility flags now available in Salesforce and Snowflake, enabling expanded data sharing for opportunities and calendar data.

**This Week\'s Progress**

**Key Momentum Areas**

Dana\'s team delivered over 2 million GitHub social URL enrichments and pushed 280,000 new EMEA companies to production, strengthening international coverage for key enterprise customers. The team also completed 300,000 data fixes while managing multiple high-priority customer projects for ServiceNow, Epicor, Cvent, and Trade Desk scheduled for month-end delivery.

Suresh successfully implemented the Contributory Network eligibility status flag in Salesforce with values now populated in Snowflake, enabling downstream systems to distinguish between full sharing, partial sharing, and no sharing contracts. After legal review, the team resolved edge cases where accounts have multiple contracts by defaulting to the most restricted agreement, providing clear guidance for CN V2 requirements.

Brandon integrated the GTM Store GraphQL API into the deal cycle analysis pipeline and added company segmentation classification, allowing the agent to group insights by deal size, company segment, and industry. This enables tenants to benchmark their deal cycles against similar accounts in the contributory network, with a board meeting demo targeted for Monday despite the compressed timeline.

**Goals & Progress**

**FINRA & Professional Licenses Datasets:** Igor\'s team ingested the complete FINRA dataset into Snowflake with CRD numbers for every U.S. broker and investment advisor, now working with Peter to identify customer-facing fields for productization as a potential PitchBook alternative. Professional licenses data acquisition continues with 18 states processed and additional single-point-of-acquisition states being targeted to expand coverage beyond contractors into regulated professions.

**Privacy Notice Deliverability:** Steve\'s team completed analyses examining NeverBounce valid email performance, discovering that approximately 15-26% of valid privacy notices are bouncing. The investigation revealed that certain buckets of NeverBounce results perform differently, with some Acton-blocked IPs actually delivering through alternative vendors. Next week the privacy notice team will make strategic decisions about email categorization to increase send volume while maintaining acceptable bounce rates.

**Money 2020 Conference Presence:** The team is preparing for Money 2020, a major fintech conference with 13,000 attendees, where Igor, Dow, and Brandon will showcase vertical datasets and GTM Studio to prospective clients. This represents a significant opportunity to generate pipeline for financial services data offerings including FINRA, professional licenses, and other regulated industry datasets.

**Strategic Challenges**

The Board of Directors and Executive Leadership Team data requests are coming with increasingly varied requirements from different enterprise customers, each with unique nuances around scope, data elements, and delivery formats. While the research team has built a scalable manual process for Barclays, transforming this into a hardened product requires product ownership, clear prioritization, and engineering support to handle multiple employment relationships more gracefully in the platform. Dana has documented the current state and requirements for Jody and Peter to assess productization options.

Multiple team members including Dana, Dow, Igor, and Brandon will be traveling next week for either Money 2020 or vacation, creating limited coverage during a period with several month-end customer deliverables. The offshore team in the Philippines has bandwidth to absorb larger projects, with Ashley and Stacy providing U.S.-based coverage, but coordination will require proactive communication to ensure nothing slips through the cracks.

Brandon is racing to complete a board meeting demo for the CN deal cycle agent by Monday with limited time remaining. While the data infrastructure is coming together well with GTM Store integration and company segmentation complete, the compressed timeline creates risk that the demo may not be fully polished for executive presentation.

**Strategic Insights**

**Key Learnings & Discoveries**

The BOD/ELT data opportunity reveals a pattern where initial custom work for one enterprise customer can rapidly generate demand across other large accounts once the value is demonstrated. ServiceNow, AlphaSense, and RBC are all expressing interest after seeing what was built for Barclays, suggesting that packaging executive-level data as a distinct product offering could accelerate enterprise deals. However, each customer\'s unique requirements highlight the need for a flexible data model that can accommodate varying scopes while maintaining a core standardized schema.

Steve\'s privacy notice analysis uncovered that NeverBounce\'s validation categories perform differently in production, with certain \"valid\" classifications showing higher bounce rates than expected. The discovery that Acton marks some emails as \"Blocked IP\" while those same addresses deliver successfully through DataPure suggests that vendor-specific factors may be creating artificial quality issues. This finding opens opportunities to optimize the privacy notice queue by routing different email categories through the most appropriate sending channel.

Brandon\'s work integrating GTM Store data revealed significant data quality issues in the standard opportunity tables, with deal amounts showing negative numbers, unrealistic values like \$100 million, or missing entirely. The GraphQL API returns more reasonable values for these same opportunities, indicating that direct API integration provides more reliable data than relying solely on ZDP tables. This learning suggests other data pipelines may benefit from similar direct API access rather than depending on intermediate data stores.

**Cross-Team Dependencies**

Our ability to scale the BOD/ELT offering depends on engineering work to better handle contacts with multiple simultaneous employments, which currently causes platform issues when someone serves on multiple boards or holds positions at different companies. This platform limitation forces the research team into manual workarounds that aren\'t sustainable at scale. Jody and Peter\'s product ownership will be necessary to prioritize these improvements and define the scope for a productized solution.

Brandon\'s CN deal cycle agent requires the contributory network eligibility flag to be available in ZDP, not just Salesforce and Snowflake. Suresh has confirmed that Ron\'s team is working on populating this field in company data tables, which will enable Brandon to keep his entire pipeline within the ZDP ecosystem. This cross-team coordination between data governance, engineering, and data analysis is proceeding smoothly with clear ticket tracking.

**Looking Ahead**

Next week\'s reduced team presence due to Money 2020 and planned vacations means proactive communication and clear handoffs are necessary to maintain momentum on customer deliverables. Ashley and Stacy will provide U.S.-based coverage for Dana\'s team, while the offshore Philippines team has capacity for larger projects that arise.

The Money 2020 conference represents a significant opportunity to generate pipeline for financial services datasets including FINRA, professional licenses, and other vertical data offerings. Igor, Dow, and Brandon will engage with prospects among the 13,000 attendees, building on last year\'s successful participation. Separately, the board meeting demo on Monday will showcase the CN deal cycle agent\'s ability to provide benchmark insights, though the compressed timeline means the team is working right up to the presentation to finalize examples and polish the output.

Dana\'s work documenting the current state of BOD/ELT datasets and gathering requirements from multiple enterprise customers will enable Jody and Peter to assess productization options when she returns from vacation. This strategic decision on whether to formalize these offerings as distinct products versus continuing with custom deliveries will shape how we approach similar opportunities with other executive-level data requests going forward. The team\'s strong execution on enrichments, company additions, and data fixes continues providing the foundation that makes these higher-value offerings possible.

*Source: Data Executive Operating Framework entries from Oct 20th, 2025 - October 23rd, 2025*

## **Core Data Team Weekly Report - October 20-24, 2025**

**Executive Summary**

The Core Data team conducted their strategic onsite this week, focusing on four key areas: developing big bets for 2026, establishing a waterfall enrichment plan, aligning with analysis and engineering teams, and strengthening team cohesion through team building activities. Jody Roberts successfully facilitated sessions covering these critical planning areas while the team presented strategic initiatives targeting \$10M+ incremental revenue opportunities. The onsite revealed both significant opportunities in data infrastructure and persistent challenges around resource allocation, particularly for Magnus Herweyer\'s shared services vision and Heather Ma\'s agent development initiatives which lack dedicated engineering support.

**This Week\'s Progress**

**Key Momentum Areas**

The team successfully executed their strategic onsite with comprehensive coverage of 2026 planning priorities. Big bet presentations from each team member outlined transformational opportunities across data enrichment, infrastructure modernization, and platform capabilities. The waterfall enrichment plan emerged as a unifying strategy to cascade data improvements across multiple products, maximizing the value of each enrichment investment.

Engineering and analysis alignment sessions on Wednesday created crucial bridges between product vision and technical execution. These cross-functional discussions surfaced both opportunities and constraints, enabling more realistic planning for Q4 deliverables and 2026 initiatives. The structured dialogue helped identify where dedicated resources are essential versus where shared services can provide leverage.

Team building components strengthened relationships and collaboration patterns essential for executing ambitious goals. As the team prepares to tackle increasingly complex cross-functional initiatives, these interpersonal connections become critical for navigating organizational challenges and driving consensus on shared priorities.

**Goals & Progress**

**Strategic Planning Execution**: The onsite successfully covered all four planned areas - big bets for 2026, waterfall enrichment planning, engineering/analysis alignment, and team building. Each team member presented 2-3 revenue-generating initiatives with clear business cases, though resource constraints emerged as a consistent theme requiring executive attention.

**Waterfall Enrichment Framework**: The team established a comprehensive plan for cascading data enrichments across the platform, ensuring improvements in one area systematically benefit downstream applications. This approach promises to multiply the impact of individual enrichment investments while reducing redundant efforts across teams.

**Cross-Functional Alignment**: Wednesday\'s engineering sessions revealed both alignment opportunities and resource gaps. While engineering partners expressed support for proposed initiatives, the lack of dedicated resources for several key projects, particularly shared services and agent development, requires escalation to secure necessary commitments.

**Strategic Challenges**

Resource allocation emerged as the dominant challenge during onsite discussions. Magnus Herweyer\'s shared services initiative and Heather Ma\'s agent development work both lack dedicated engineering teams, forcing reliance on borrowed resources and creating delivery uncertainty. Without defined engineering velocity or committed resources, these strategic initiatives risk remaining in perpetual prototype status.

The complexity of managing multiple parallel initiatives while maintaining operational excellence became evident through team discussions. Several team members struggle to balance immediate delivery requirements with forward-looking strategic work, highlighting the need for clearer prioritization frameworks and potentially additional product management resources.

Integration and adoption challenges for shared services require careful navigation. Building consensus across teams accustomed to custom solutions demands incremental value demonstration and significant change management effort. The onsite discussions revealed varying levels of enthusiasm for standardization, necessitating a phased approach to drive adoption.

**Strategic Insights**

**Key Learnings & Discoveries**

The waterfall enrichment strategy represents a paradigm shift from isolated improvements to systematic value multiplication. By designing enrichments to cascade through the data platform, the team can achieve compound returns on investment, making each improvement benefit multiple downstream applications and use cases.

Resource constraints aren\'t just limiting factor - they\'re forcing strategic clarity. The gap between ambitious vision and available resources compelled sharper prioritization discussions during the onsite, helping identify which initiatives truly merit investment versus those that should be deferred or descoped.

Cross-functional alignment sessions revealed that engineering capacity, not technical feasibility, represents the primary constraint on innovation. Most proposed initiatives are technically achievable, but the organization lacks sufficient engineering resources to execute on all high-value opportunities simultaneously.

**Cross-Team Dependencies**

Engineering partnership remains critical for all major initiatives, with the onsite sessions highlighting specific resource needs for shared services, agent development, and data acquisition improvements. Clear commitments from engineering leadership will be essential for 2026 success.

Analysis team collaboration on the waterfall enrichment plan creates dependencies but also opportunities for leveraged impact. Their involvement ensures enrichments align with measurement frameworks and customer value metrics, maximizing return on investment.

**Looking Ahead**

Following this week\'s onsite, the team must translate strategic discussions into concrete resource requests and project plans. Priority actions include securing dedicated engineering resources for shared services and agent initiatives, finalizing the waterfall enrichment implementation roadmap, and establishing clear Q4 deliverables that build toward 2026 goals.

The big bets presented during the onsite require executive sponsorship to move from vision to reality. Each initiative\'s \$10M revenue potential justifies investment, but organizational commitment to fund and staff these projects will determine whether the team can deliver on ambitious targets. The waterfall enrichment framework provides a unifying strategy that should help prioritize investments for maximum compound impact.

Success in 2026 will depend on the organization\'s willingness to invest in foundational data infrastructure alongside visible customer features. The onsite discussions positioned the Core Data team to drive transformational value, but execution requires resolving the resource constraints and organizational alignment challenges identified during this week\'s sessions.

*Source: Core Data Team Onsite sessions, Week of 10/20-10/24*

## **GTM Data Platform Team Weekly Report - October 20-24, 2025**

**Executive Summary**

Dominik and Filip established strategic sequencing clarity this week, prioritizing Federated Search in Graph QL ahead of the Graph QL API public beta release. Timing of GQL public beta release will be evaluated down the road, but it\'s not an immediate priority. Menna Rashwan finalized alignment with App teams on MVP search use cases, prioritized fields, and expected behavior, while resolving missing schema fields with Data Producers. The team now has top-to-bottom product and engineering alignment on making Federated Search integration with GraphQL a P0 priority, positioning December 31 delivery as achievable if remaining technical work proceeds on schedule.

**This Week\'s Progress**

**Key Momentum Areas**

Menna Rashwan achieved comprehensive cross-functional alignment on the foundation for Federated Search integration. She finalized MVP search use cases, prioritized field lists, and expected search behavior with App teams, then worked closely with Data Producers to resolve missing fields from the shared schema and agree on next steps for datatype mismatches. She initiated mapping between MVP search fields and GraphQL scalars, standardizing how Person and Company data will be searched across the platform to ensure scalability and consistent user experience for the December 31 integration deadline.

The leadership team set the strategic sequence as Federated Search before External API, validating that the current GraphQL path is extensible for Copilot Workspaces and vertical datasets. They also confirmed that entitlement and credit models are required before external or monetized dataset access, establishing clear guardrails for what must be delivered first and what can follow later.

**Goals & Progress**

**Federated Search Integration & Schema Alignment**: Menna Rashwan worked through schema discrepancies with Data Producers, identifying that the current schema was missing key fields required for search use cases. These fields are now being added, though datatype mismatches still need resolution. Some fields will need to be indexed as both code and value to support sorting, faceting, and filtering use cases, requiring coordination with the data team via a shared mapping service. While use cases, field lists, and behavior are finalized, additional work is needed to capture and align on sorting and faceting requirements with App teams to fully enable the end-to-end search experience. The scalar mapping work is actively progressing, with two remaining areas expected to be resolved: clarifying which operators are supported by each scalar type to ensure compatibility with intended search behaviors, and finalizing schema updates from Data Producers to address current datatype mismatches.

**Location Matching & Regional HQ**: Moshik Levin gained access to Company Data\'s proof of concept and tested the company hierarchy graph, exploring ways to leverage the \"Domestic HQ\" flag for regional matching. He\'s continuing to workshop which data points are required and which heuristics can run on the fly for the proof of concept, with the goal of adding options for using Company Data instead of only resolving locations on-the-fly. The team wants engineering to pick up this work in November.

**Strategic Challenges**

Schema gaps and technical dependencies continue to require careful coordination across teams. While Menna Rashwan achieved initial alignment with Data Producers, mapping exposed several coverage issues including missing fields and mismatched data types that impact search use case coverage. Some MVP fields do not map cleanly to proposed GraphQL scalars, though this gap may be mitigated if Data Producers supply the expected data types. Additionally, fields that need to be indexed as both code and value for sorting, faceting, and filtering will require coordination through a shared mapping service. An alignment meeting originally scheduled for this week was pushed to next week due to a data team offsite, creating a slight delay in resolving these technical details.

App team alignment work revealed an additional layer of requirements beyond initial MVP scope. While Menna Rashwan finalized use cases, field lists, and basic search behavior with App teams, additional work emerged around capturing and aligning on sorting and faceting requirements across prioritized Person and Company fields. These capabilities are necessary to fully enable the end-to-end search experience that users expect, expanding the scope slightly from the original MVP definition.

**Strategic Insights**

**Key Learnings & Discoveries**

Dominik and Filip\'s decision to prioritize Federated Search before External API provides the strategic clarity the team needed to focus execution. This sequencing decision validates that the current GraphQL path is extensible for future use cases including Copilot Workspaces and vertical datasets, confirming the architectural approach is sound. The decision also establishes that entitlement and credit models must be in place before external or monetized dataset access, ensuring proper business controls are built into the foundation rather than retrofitted later.

Product and engineering achieved top-to-bottom alignment on making Federated Search integration with GraphQL a P0 priority. This level of organizational commitment is a significant shift that removes ambiguity about resource allocation and competing priorities. When both product and engineering leadership agree on top priority status, teams can move forward with confidence that their work won\'t be deprioritized for other initiatives, accelerating execution velocity.

The schema alignment work revealed that some fields need dual indexing strategies to support the full range of user behaviors. Fields that need to support sorting, faceting, and filtering require indexing as both code and value, which necessitates coordination with the data team via a shared mapping service. This discovery shapes the technical approach and highlights a dependency that must be managed to deliver complete search functionality rather than just basic filtering capabilities.

**Cross-Team Dependencies**

Coordination with Data Producers remains essential for resolving schema discrepancies and finalizing MVP field specifications. Next week\'s deep dive with Data Producers will address datatype mismatches and finalize the approach for fields requiring dual indexing. The alignment meeting was pushed due to the data team offsite, so maintaining momentum on this workstream depends on productive outcomes when teams reconvene.

App teams need to remain engaged on sorting and faceting requirements to ensure the search experience meets user expectations. While basic search behavior is finalized, these additional capabilities are necessary for the end-to-end experience, requiring continued collaboration beyond the initial MVP alignment to capture complete requirements.

**Looking Ahead**

Next week centers on finalizing the technical details that will unblock implementation work and securing the remaining alignment needed for December 31 delivery. The team will complete phase 1 company and contact field scalar definitions and their related operators, establishing precise behavior models with engineering.

Menna Rashwan will finalize schema updates with Data Producers, resolving datatype mismatches and determining the approach for using the shared mapping service for code-to-value translation. She\'ll align with App teams on sorting and faceting requirements across prioritized Person and Company fields, then revisit scalar mapping to validate operator compatibility and address any missing or mismatched scalar types. This work completes the foundation needed to unblock Federated Search implementation. Moshik Levin will continue exploring proof of concept options for Regional HQ matching, workshopping required data points and on-the-fly heuristics to prepare for engineering pickup in November. Linda Johannessen will finalize the three executable sequencing options---External-first, Federated Search-first, or Hybrid---with clear scope, effort, validated engineering impact, and documented trade-offs, enabling leadership to choose a single path forward instead of splitting capacity. With strategic direction now set and cross-functional alignment achieved, the team is positioned to convert planning into execution, delivering the platform capabilities that Copilot Workspaces, vertical datasets, and federated search require.

*Source: Team 1-2-3 Operating Framework entries from October 20-24, 2025*

## **Integrations Team Weekly Report - October 20, 2025**

**Executive Summary**

The team made progress this week with steady momentum on GTM Data Manager development and continued focus on Agentforce enablement. Sanyog Rai is advancing self-service configuration capabilities while the team prepares comprehensive documentation for the January 31, 2026 compliance deadline requiring all ZoomInfo teams to access CRM and Engagement data exclusively through GTM Data Manager APIs.

**This Week\'s Progress**

**Key Momentum Areas**

The team maintained steady progress on GTM Data Manager development, with Sanyog Rai advancing configuration capabilities that will enable teams to manage their own integrations. The work lays the foundation for the January 2026 transition where all ZoomInfo products must migrate to GTM Data Manager APIs for CRM and engagement data access.

Prateek Paikray continues supporting Agentforce functionality following the successful Dreamforce delivery. The comprehensive enablement materials developed pre-conference continue serving both internal teams and external customers, with the team maintaining readiness to address implementation questions or technical challenges.

**Goals & Progress**

The team initiated comprehensive use case documentation to prepare for the January 31, 2026 compliance deadline. This foundational work ensures smooth transition away from legacy data access patterns while maintaining operational continuity across the organization. Early documentation efforts are revealing the complexity of migrating existing workflows and the need for comprehensive change management across product, engineering, and customer-facing teams.

**Strategic Challenges**

The January 31, 2026 compliance deadline for GTM Data Manager API-only access represents a fundamental organizational shift that will require extensive coordination across teams. While the team has initiated use case documentation, the scale of migration planning and execution support needed across the organization will likely exceed current resource allocation. Early identification of affected workflows and clear migration paths will be essential to prevent last-minute scrambles.

**Strategic Insights**

**Key Learnings & Discoveries**

The use case documentation work is revealing that the January 2026 API migration affects more teams and workflows than initially anticipated. Each product team has unique integration patterns and dependencies that require individual assessment and migration planning, suggesting the need for dedicated migration support resources.

**Cross-Team Dependencies**

The organization-wide shift to GTM Data Manager API-only access by January 31, 2026 requires coordination across product, engineering, and operations teams. The Integrations team\'s use case documentation work will serve as the foundation for broader migration planning, but successful execution will depend on clear communication channels and dedicated resources across multiple organizations.

**Looking Ahead**

Next week focuses on accelerating use case documentation for the January 2026 API migration deadline. The team will continue mapping current data access patterns across ZoomInfo products to establish comprehensive scope for the migration project.

Sanyog Rai will continue advancing self-service configuration capabilities that reduce operational overhead and give teams direct control over their data integration workflows. Prateek Paikray maintains post-Dreamforce Agentforce support while the team prepares for increased engagement as customers implement the solutions demonstrated at the conference.

*Source: Integrations Team 1-2-3 Operating Framework entries from October 20, 2025*

## **Automation Team Weekly Report - October 24, 2025**

**Executive Summary**

MCP credit consumption concerns threaten enterprise adoption while GTM Plays requirements clarify action library priorities. Adam Peretz discovered that the stateless MCP server architecture prevents credit estimation before queries execute, with beta partners refusing adoption unless guardrails are implemented to prevent runaway credit consumption. Sam Massie completed DoubleO alignment work, revealing that GTM Plays requires deterministic action libraries with user inputs complementing agentic capabilities, with Slack, Outreach, and Salesloft activations prioritized. Marc Frail is on track to launch Global Event Bus with initial GTM CDC events by next week\'s end, enabling broader platform event consumption.

**This Week\'s Progress**

**Key Momentum Areas**

Sam Massie achieved comprehensive DoubleO alignment, completing synchronization with the team on Plays requirements and reordering the Workflows/Automations H2 backlog to support GTM Plays priorities. The clarity on deterministic actions versus agentic steps enables focused execution on the most valuable integration points.

Marc Frail advanced Global Event Bus toward production launch, maintaining schedule for initial GTM CDC events to go live by end of next week. The team also released backstage tooling that provides UI-based event registration for publishers, simplifying the event publishing workflow significantly.

Adam Peretz pivoted to high-priority partnership automation, deprioritizing original week goals to focus on Developer Portal enhancements that enable automated partner application publishing. The partnerships team is ready for enhanced data collection and cross-team API integration to streamline marketplace presence.

**Goals & Progress**

**DoubleO Integration Alignment**: Sam Massie completed 100% of understanding how ZoomInfo automation supports Plays and DoubleO roadmap, establishing clear prioritization frameworks. The discovery that activations like Slack, Outreach, and Salesloft are high priority informs immediate execution focus.

**Global Event Bus Production Launch**: Marc Frail made substantial progress with GTM CDC on track for next week\'s production launch. The namespace-based CDC architecture continues positive progression through staging, representing improved scalability over monolithic CDC approaches.

**Enterprise API Migration Planning**: Adam Peretz shifted to scoping Bulk Search/Enrich API migration to ZI API Platform and drafting new monetization models. This work addresses the largest revenue-driving enterprise customers who require greater scale than synchronous REST APIs provide.

**Strategic Challenges**

MCP credit consumption unpredictability blocks enterprise adoption, with Adam Peretz discovering that the stateless server architecture prevents cost estimation before queries execute. Beta partners specifically cited concerns about queries that could consume thousands of credits in seconds, refusing to enable access without guardrails that engineering indicates won\'t be easy to implement.

Sales team lacks Claude access for customer demonstrations, with Mike Fawkes and other salespeople unable to demo MCP capabilities to strategic customers. Adam Peretz is working with Rowan Bailey to establish access protocols, but the current infrastructure doesn\'t support sales team demonstration needs.

API versioning policy requires leadership decision, as Adam Peretz identified multiple viable approaches with distinct trade-offs around versioning granularity and legacy support timelines. The decision affects platform evolution flexibility and customer migration complexity.

**Strategic Insights**

**Key Learnings & Discoveries**

Deterministic actions complement rather than replace agentic capabilities, as Sam Massie discovered that GTM Plays requires a library of functions with explicit user inputs alongside agentic steps. This architectural clarity enables focused development on the right abstraction layers.

MCP cost control becomes adoption blocker for enterprise segment, with beta partner feedback revealing that unpredictable credit consumption creates unacceptable risk for enterprise customers. The stateless architecture optimizes for simplicity but creates cost management challenges requiring engineering investment.

Backstage tooling democratizes event publishing, with Marc Frail noting that UI-based event registration simplifies the publisher experience significantly. This platform investment reduces friction for teams contributing to the event ecosystem.

Partnership automation readiness drives developer portal evolution, as Adam Peretz identified that partnerships team needs enhanced data collection and automated publishing workflows. The developer portal becomes the integration point for marketplace presence management.

**Cross-Team Dependencies**

DoubleO team coordination continues with onsite meeting scheduled in Waltham next week for Sam Massie to narrow Plays requirements further, ensuring continued alignment on action library priorities and integration patterns.

Rowan Bailey collaboration is essential for resolving Claude access issues that prevent sales demonstrations, affecting the team\'s ability to showcase MCP capabilities to strategic enterprise customers.

Partnership team integration requires Developer Portal API enhancements that enable automated data transmission for marketplace publishing, with Andres coordinating cross-team workflows.

**Looking Ahead**

Next week focuses on finalizing API versioning proposals while advancing Global Event Bus production launch and deepening DoubleO integration planning.

Adam Peretz will finalize the API versioning proposal for leadership review when Ali returns, addressing critical policy questions about versioning granularity and legacy support timelines. Marc Frail will continue building the initial library of data connectors for GTM Studio, expanding the action ecosystem that supports GTM Plays requirements.

Sam Massie will attend the onsite meeting with DoubleO in Waltham to narrow Plays requirements, deferring workflow micro front end work to focus on action forms that directly support strategic objectives. The MCP credit consumption challenge requires engineering coordination to develop guardrails that enable enterprise adoption while maintaining the simplicity benefits of stateless architecture.

*Source: Team 1-2-3 Operating Framework entries from 10/20 - 10/24*

## **User Provisioning Team Weekly Report - October 20, 2025**

**Executive Summary**

The User Provisioning team continues monitoring AI Action Credit usage in production following the successful October 8th go-live. The team is ensuring system stability and accurate usage reporting to SAP while preparing for financial reviews to validate that AI usage margins align with the 30-40% business target set by leadership.

**This Week\'s Progress**

**Key Momentum Areas**

The production environment for AI Action Credit reporting continues operating stably, with usage data flowing correctly to SAP for billing purposes. This validates the technical foundation needed to support GTM Studio and Copilot Workspace customers at scale as the November 3rd launch approaches.

The team is monitoring system performance closely to identify any edge cases or unexpected usage patterns that could impact billing accuracy. Early production data provides valuable insights into actual customer consumption behaviors compared to projected usage models.

**Goals & Progress**

The team maintains vigilant oversight of the AI Action Credit reporting system, ensuring that all usage accurately reflects in SAP for proper customer billing. The monitoring includes validation that credit consumption aligns with actual feature usage across both GTM Studio and Copilot Workspace.

The team is preparing for upcoming financial reviews with key stakeholders including Adam Smith and Mark Harris to ensure net margin across AI usage aligns with the 30-40% target. This involves analyzing actual consumption patterns against pricing models to validate that the business achieves desired profitability thresholds.

**Strategic Challenges**

As customer usage scales beyond early access cohorts toward general availability on November 3rd, the team must ensure that monitoring and alerting systems can handle increased volume while maintaining accuracy. Any discrepancies in usage reporting or billing could impact customer trust and require rapid resolution.

The margin validation work requires coordination across multiple stakeholders to review namespaces, markup, and weighted usage of AI. Ensuring alignment on these financial parameters before broader customer adoption prevents potential repricing conversations or margin compression issues later.

**Strategic Insights**

**Key Learnings & Discoveries**

The successful production operation of AI Action Credit reporting validates the intensive cross-functional collaboration that delivered the October 8th go-live. The system\'s stability under initial production load provides confidence for scaling to support the November 3rd general availability launch.

Early production data is revealing actual customer consumption patterns that can inform future pricing and packaging decisions. Understanding how different customer segments use AI credits will enable more accurate forecasting and potentially segmented pricing strategies.

**Cross-Team Dependencies**

Ongoing collaboration with GTM Tech and RevOps remains essential for packaging and pricing coordination as the team moves toward November 3rd general availability. The financial review process will require close partnership with Adam Smith\'s team to ensure margin targets translate into appropriate pricing structures.

The Product Operations and Product Marketing teams\' work on customer communication about AI credits depends on the Provisioning team\'s accurate usage tracking and reporting. Any changes to credit consumption models or billing approaches will require coordinated updates across multiple customer-facing materials.

**Looking Ahead**

Next week focuses on completing the financial review to validate that net margin across AI usage aligns with the 30-40% target. The team will meet with key stakeholders to review namespaces, markup, and weighted usage of AI to lock in the target margin before the November 3rd general availability launch drives increased customer consumption.

The team continues monitoring production environment stability and usage reporting accuracy as the foundation for scaling AI Action Credit billing across the broader customer base. Maintaining system reliability through the launch period will be critical for customer trust and business success.

*Source: Team 1-2-3 Operating Framework entries from week of October 20, 2025*

## **Product BI Team Weekly Report - October 20-24, 2025**

**Executive Summary**

The team is maintaining focus on tactical event instrumentation work while preparing for post-launch analytics needs. Inbal Kor created a new dashboard tracking the GTM Studio signal feature and successfully coached Ferrell Tanuwidjaja on building GTM Studio taxonomies independently. The team established mandatory analytics review for all feature launches through required Jira tickets.

**This Week\'s Progress**

**Key Momentum Areas**

Inbal Kor created a new dashboard tracking the GTM Studio signal feature (which allows users to create worksheets and enrich columns using signals) and successfully coached Ferrell Tanuwidjaja on building GTM Studio taxonomies independently. This knowledge transfer expands the team\'s capacity to support multiple product initiatives simultaneously and ensures consistent taxonomy application across GTM Studio features.

The team established mandatory analytics review for all feature launches through required Jira tickets, building on the process improvement Phoebe Mei secured with Sean and Adam last week. This ensures event tracking is reviewed before features go live, addressing the longstanding gap where engineering teams shipped features without proper instrumentation.

Phoebe Mei secured alignment with Sean and Adam on requiring analytics requirement tickets for every new feature launch. This concrete process improvement ensures event tracking is reviewed before features go live, preventing the instrumentation gaps that have historically required extensive retroactive work.

**Goals & Progress**

**Event Instrumentation & Taxonomy:** The mandatory analytics review process is now operational, with engineering teams coordinating through Sean and Adam to assign implementation owners for each feature\'s tracking requirements. While new events using the taxonomy are currently in staging (not yet in production), the framework is established and being applied to features like share view.

Phoebe continues requiring extensive follow-up to ensure adoption, but the structural process improvement should reduce this burden going forward. The team acknowledges that if the instrumentation issue is not fixed soon through this new process, escalation through engineering leadership will be necessary.

**GTM Studio Instrumentation:** Inbal Kor implemented tracking for the new signal data source feature and added it to the high-level engagement dashboard. Ferrell Tanuwidjaja reviewed general enrichment and signal events for GTM Studios, compared amplitude and snowflake data sources, and is moving to the workbook landing page review before meeting with stakeholders on priority business questions and event taxonomy best practices.

The team is building out comprehensive tracking infrastructure that will enable detailed analysis of how customers discover, configure, and use signals within GTM Studio workflows. This foundation will be essential for understanding adoption patterns and identifying optimization opportunities post-launch.

**Workspace Analysis Preparation:** The team is preparing for increased analytical support needs as Copilot Workspace approaches general availability on November 3rd. The focus remains on ensuring proper event instrumentation is in place to support future analysis rather than building extensive dashboards before the product has stabilized.

**Strategic Challenges**

The team faces ongoing tension between building comprehensive dashboards versus ensuring foundational instrumentation is correct. With the November 3rd launch approaching, the priority is confirming that all events are properly tracked rather than creating sophisticated analysis that may need revision as the product evolves.

Engineering adoption of the new mandatory analytics review process will determine whether instrumentation gaps finally close or continue requiring extensive BI team follow-up. The team needs to see events released moving forward actually have the right instrumentation and eventing to validate the process improvement.

**Strategic Insights**

**Key Learnings & Discoveries**

The successful knowledge transfer from Inbal Kor to Ferrell Tanuwidjaja on GTM Studio taxonomies demonstrates the value of investing in team capability building rather than centralizing all expertise. This approach creates resilience and enables the team to support multiple product initiatives without becoming a bottleneck.

The mandatory analytics review process represents a maturation in how analytics integrates with the product development process. By shifting from voluntary best practice to required checkpoint, the team is establishing the structural foundation needed to prevent instrumentation gaps at scale.

**Cross-Team Dependencies**

The team\'s work with Sean and Adam on event instrumentation governance continues to be essential for ensuring analytics can effectively track product usage. The newly established process requiring analytics Jira tickets for feature launches formalizes this dependency and should reduce friction, though it requires buy-in from engineering teams and TPM coordination to enforce consistently.

Coordination with the GTM Studio team on signal feature tracking and taxonomy ensures that analytical infrastructure keeps pace with product development. Inbal Kor\'s work with stakeholders on priority business questions will inform what metrics and dashboards are most valuable post-launch.

**Looking Ahead**

Next week focuses on validating that the mandatory analytics review process is being followed for features approaching the November 3rd launch. The team will monitor whether engineering teams are creating required Jira tickets and whether the instrumentation being implemented matches the taxonomy standards.

Ferrell Tanuwidjaja will complete the workbook landing page review and meet with stakeholders to align on priority business questions and taxonomy best practices. Inbal Kor will continue GTM Studio work while monitoring the signal feature dashboard for any early adoption signals from the current user base.

The team is positioning itself to provide valuable post-launch analysis by ensuring foundational instrumentation is correct, recognizing that sophisticated analytics on poorly tracked events delivers little value. Success is measured by clean, complete event data flowing from day one of general availability.

*Source: Team 1-2-3 Operating Framework entries from October 20-24, 2025*

## **Product Ops Team Weekly Report - October 20, 2025**

**Executive Summary**

The team reached an exciting milestone on the Copilot Workspace automated changelog with Ken Elwell delivering a strong V1 (with the help of Guy Levin) that demonstrates AI can effectively track and translate technical releases into business language using GitHub PRs and Jira tickets. Sam Darcy achieved strong results on the VOC data quality report with highly accurate and efficient fragment filtering, positioning the system to roll it out to PMs and validate the 2026 roadmap against customer needs. Kristin Gandini solved the feedback loop challenge by creating a JPD logging mechanism that captures PM decisions in near real-time. However, Caleb Munson has shared that annual planning alignment remains difficult with mixed stakeholder perspectives on what worked and what should change, requiring focused leadership discussion next week.

**This Week\'s Progress**

**Key Momentum Areas**

**Automated Changelog Reaches Viable State**: Ken Elwell completed a V1 version of the Copilot Workspace automated digest that successfully translates PRs and deployments into business language. While refinements are needed around JTBDs, feature flag status, and upcoming versus released features, the output demonstrates AI can capture changes that even manual processes miss. Sean\'s review next week will validate the approach, with the goal of having PMs comfortable sending it to the field by end of next week.

**VOC System Delivers Strong Initial Results**: Brett Jacobs produced a V1 data quality report that exceeded expectations, demonstrating the system can filter massive fragment sets down to highly relevant customer insights. Dominic received the report and plans to test the 2026 roadmap against VOC data. The fragments being pulled are showing strong accuracy, building confidence the system will effectively support both top-down strategic validation and bottom-up PM workflows.

**Discovery Engine Closes the Feedback Loop**: Kristin Gandini solved a critical workflow challenge by building a JPD logging mechanism that captures PM decisions on support tickets and NPS feedback. The system now remembers whether PMs created new tickets, linked to existing ones, or decided not to act, then references those decisions in future reports. This creates a near real-time feedback loop that prevents duplicate work and maintains decision history across the three report types: holistic for leadership, product-specific for PMs, and account-specific for AMs.

**Goals & Progress**

**Release Notes Infrastructure Expansion**: Ken Elwell met with Yamit\'s team, who confirmed dev work started this week on zoominfo.com release notes ahead of the November 18 release. GTM AI release notes continue in parallel with Ken\'s local file updates nearly complete. The dual-platform approach ensures both speed through gtm.ai and SEO/compliance benefits through zoominfo.com, with the team focused on zero-friction update processes that don\'t depend on CMS bottlenecks.

**Knowledge Base Consolidation**: Daniel Kong completed the GTM Studio knowledge base buildout, bringing it to parity with the Copilot Workspace knowledge base. All agents now reference the same core knowledge documents, creating consistency across products. The main challenge is managing file updates across multiple agents as the chatbot\'s upload system requires careful coordination to ensure the right agents get updated with the right documents.

**VOC Methodology Refinement**: Brett Jacobs acknowledged getting too deep in methodology details this week rather than focusing on results validation. The learning is to test outputs first, identify gaps, then iterate on methodology. Next week shifts to practical application: validating the 2026 roadmap and creating focused reports for the 750K+ customer segment to build the top-down strategic ritual.

**Agent Testing and Refinement**: Kristin Gandini rebuilt the LaunchDarkly impact agent to have users define parameters upfront, which prevents hitting chat maximums and makes searches dramatically more efficient. Both the Discovery Engine and LaunchDarkly agents are ready for real-world testing with users to gather feedback and refine functionality before broader rollout.

**Strategic Challenges**

**Annual Planning Alignment Difficulty**: Caleb Munson met with stakeholders but found consensus harder than expected. People see the same symptoms---too many simultaneous initiatives, unclear priorities, team conflicts---but disagree on root causes and solutions. Some argue for more detailed dependency planning, others say excessive planning wastes time on work that never gets done. The challenge reflects a fundamental tension between wanting smooth execution without investing in planning time, especially when unknowns only emerge during execution. Caleb is meeting with DAIs next week to gather additional perspectives.

**AI Application in Strategic Planning**: Caleb Munson expressed uncertainty about how AI can help with planning beyond tactical analysis. While AI excels at VOC-driven bug identification and usage analysis, the company is at a pivot point where looking backward may not provide the best inputs for forward strategy. Dominic\'s goal to significantly compress planning timelines with AI requires clarity on which decisions AI can support versus which require human strategic judgment on fundamental direction.

**Docket Integration Planning**: The team identified a gap in handling the expected volume of seller questions when products launch. While talk track agents and product capability content are solid, the system for processing Docket questions needs technical setup, PM training, and clear workflows. Daniel Kong will drive this with Kristin Gandini providing Docket expertise and coordination with Cindy and Kayla. Success requires figuring out both the technical integration and the cultural shift away from ad-hoc Slack responses.

**Strategic Insights**

**Key Learnings & Discoveries**

**Agent Scope Definition Matters**: Kristin Gandini discovered that having users define search parameters upfront, before executing queries, dramatically improves efficiency and prevents cost issues. The LaunchDarkly rebuild demonstrated this principle---refining scope through conversation first, rather than after running expensive searches, cuts processing costs and produces better results. This learning applies across agent design.

**AI Understands Technical Changes**: Ken Elwell found that AI does more than write code---it genuinely understands the business implications of technical changes. When combined with additional context from Jira tickets, the system can produce automated changelogs that capture details manual processes miss. The V1 output caught more than Sean\'s customer-focused release notes, demonstrating potential to finally solve the translation gap that keeps downstream teams hours or days behind engineering velocity.

**JPD as Decision History**: The insight to use JPD as a logging mechanism for PM decisions creates persistent memory across VOC analysis cycles. Rather than treating each Discovery Engine report as isolated, the system now maintains context about what was already addressed, why certain issues were dismissed, and which tickets link to which customer feedback. This transforms the tool from a reporting system into a decision management platform.

**VOC is Problem Identification, Not Solution Design**: Brett Jacobs clarified that VOC serves as a problem identification tool showing the magnitude of customer pain points, not a solution ideation system. While it\'s inherently backward-looking and wouldn\'t have predicted breakthrough products like Copilot Workspace, it provides critical objectivity for understanding which customer problems matter most. The ability to quantify that a feature was mentioned by 500 customers worth \$200M ACV versus 10 customers provides crucial prioritization data, even if solutions require forward-looking strategic thinking.

**Cross-Team Dependencies**

Guy Levin\'s commitment to help build the automated weekly digest is accelerating the Copilot Workspace changelog significantly. His confirmation that existing infrastructure---the release dashboard with AI summaries per PR---makes this use case \"much easier\" than previous attempts is removing a major technical barrier. The target of Monday or Tuesday next week for first iteration puts the team ahead of schedule.

The CX team continues collaborating well on knowledge center workflows, though the team needs to establish clear processes for Docket question handling before launch. Tal\'s team delivering release notes on zoominfo.com before the November release creates the dual-platform foundation, while Ryan adding Ken to the GitHub repo enables direct HTML updates for gtm.ai without CMS dependencies.

**Looking Ahead**

Next week focuses on validating VOC capabilities with real strategic decisions while solving the planning alignment challenge that\'s blocking annual planning progress.

**VOC Strategic Validation**: Brett Jacobs, Caleb Munson, and Simon will schedule focused time to map how VOC flows through planning and prioritization. The immediate test is running the 2026 roadmap through VOC analysis and creating the focused large enterprise customer report. Success means demonstrating VOC can provide objective prioritization data even if it doesn\'t solve dependency mapping or solution ideation. This work connects directly to Caleb\'s planning process by providing the problem identification layer that AI can genuinely support.

**Planning Process Clarity**: Caleb Munson meets with DAIs to gather broader perspectives on what planning should deliver, then works with Brett Jacobs and Kristin Gandini to define AI\'s role in the process. The goal is finding the middle ground between detailed dependency planning that wastes time and insufficient planning that creates execution chaos. The discussion must address both capacity planning---where AI can help with data-driven puzzle-solving---and strategic direction-setting where human judgment remains critical.

**Agent Deployment Readiness**: Ken Elwell gets Sean\'s feedback on the Copilot Workspace digest and makes final refinements for PM rollout. Daniel Kong establishes the Docket question collection system and gets PMs into the knowledge center update rhythm. Kristin Gandini tests both Discovery Engine and LaunchDarkly agents with real users and finalizes the Agentic Platform for Prototyping so teams can start creating and validating their own agents.

The team is delivering on infrastructure that enables product velocity while confronting the harder organizational questions about how to plan effectively in a rapidly changing environment. The VOC validation next week will demonstrate whether AI-powered systems can provide the objectivity that planning discussions currently lack.

*Source: Team operating document entries from 10/20/2025 and weekly team meeting transcript*

## **ZIM Team Weekly Report - October 20, 2025**

**Executive Summary**

AI Page Rank early access launched successfully Tuesday with Matt Barnes working with CX recruiting 5-6 beta customers while workbooks agent scalability issues require urgent resolution before November 3rd GA deadline. Brett Elliot transitions to workbooks infrastructure team deploying scalable agent architecture by October 31st as team navigates resource reallocation cutting Inferno to 2.5 engineers and Clickagy to 6-7 engineers. Partner audience match rate optimization opportunities identified ranging 20-90% requiring firmographic enhancement beyond name and domain matching.

**This Week\'s Progress**

**Key Momentum Areas**

Matt Barnes launched AI Page Rank early access and beta program Tuesday with Katie\'s CSM team recruiting 5-6 additional enterprise and mid-market customers beyond two current small customer testers. Q4 planning reaches 80% completion with all epics for Aadhitthyaa, Shuxin, and Matt\'s teams targeting end-of-day Friday delivery pending capacity estimate finalization through Ganesh and Venkata coordination.

Aadhitthyaa Hari Gopal advanced identity data partner onboarding coordination across five teams with Privado order form completion scheduled for next week maintaining November 18th GA timeline. GTM Config offerings generation succeeded for SurveyMonkey, SupportLogic, and Cvent while Berlin Packaging site crawling failure reveals technical limitations requiring investigation for production readiness.

Shuxin Yang completed retroactive intent delivery exceeding minimal requirements while advancing persona intent signal development with data science team ticketing for Q4 execution. Intent agent table clarification with Amy supports ALI data consumption while intent usage complexity determination defers offerings integration to future versions.

**Goals & Progress**

**Agent Infrastructure**: Brett Elliot assumes workbooks agent scalability responsibility requiring deployment of production-ready container orchestration by October 31st for November 3rd workbooks GA. Current architecture spawns individual containers per cell causing Kubernetes health check failures and resource exhaustion requiring fundamental infrastructure redesign with Ryan, Grant, Sean, Richard, Cy, and Mehdi coordination.

**Partnership Development**: Aadhitthyaa Hari Gopal identified partner audience match rate variance from 20% to 90% based on company name and domain matching revealing optimization opportunities through firmographic enhancement including revenue and location data. Path Factory insights documentation review questions value proposition overlap with existing WebSights capabilities requiring strategic rationale clarification.

**Platform Integration**: Shuxin Yang progressed ALI data GTM Store ingestion coordination with Linda while completing retroactive intent outage stabilization before sales team messaging deployment. Vendor 20-signal limitation requires intent aggregation strategy development determining signal definition scope and standard topic utilization approach.

**Strategic Challenges**

Anwar Mai manages resource reallocation reducing Inferno to 2.5 engineers and Clickagy to 6-7 engineers requiring cutline establishment across 42 projects for executive presentation. The capacity constraints necessitate difficult prioritization decisions balancing agent infrastructure, GTM Config, DMP development, international expansion, and Connected TV against available engineering bandwidth.

Brett Elliot faces compressed timeline deploying scalable workbooks agent infrastructure by October 31st addressing container orchestration failures where Python agents don\'t respond to Kubernetes health checks causing pod destruction and recreation cycles. The architectural redesign requires three separate components coordinating successfully preventing November 3rd workbooks GA failure.

Aadhitthyaa Hari Gopal addresses domain data gaps affecting 7-8% of evaluated companies (45,000 of 620,000) preventing offerings generation requiring empty state UI development for customer-provided information. ZoomInfo company ID appending process clarity remains needed from Anne Fajkus and Matthew Williams for tenant onboarding workflow validation.

**Strategic Insights**

**Key Learnings & Discoveries**

Matt Barnes learned from OO workflow management that connected agents approach provides tremendous data processing flexibility requiring consideration in future signal pipeline architectural decisions. The team recommends additional knowledge transfer sessions with OO team informing design patterns for workflow orchestration capabilities.

Aadhitthyaa Hari Gopal discovered partner audience match rate optimization potential through firmographic data enhancement beyond current name and domain matching. The 20-90% variance suggests significant improvement opportunities supporting Adobe partnership value delivery while enabling more accurate audience creation for buying group completeness workflows.

Anwar Mai\'s coordination with Sneh and Marc Frail established website journey data January 2026 delivery timeline enabling resource reallocation while maintaining stakeholder commitment clarity. The contract development for WebSights and FormComplete data availability requires definition specifications including session duration constraints for workflow trigger integration.

**Cross-Team Dependencies**

Our work with Katie\'s CSM team advances AI Page Rank beta recruitment targeting enterprise and mid-market customers for comprehensive testing beyond current small customer base. Matt Barnes coordinates early access program expansion through Tuesday CX team presentation demonstrating capabilities and recruitment support.

Partnership coordination with Privado advances order form completion for identity partner scanning capabilities at \$50K annual investment enabling November 11th manual scanning launch. Aadhitthyaa Hari Gopal manages five-team coordination maintaining November 18th production timeline through meticulous dependency planning.

Agent infrastructure requires urgent Brett Elliot coordination with Ryan, Grant, Sean, Richard, Cy, and Mehdi deploying scalable container orchestration preventing workbooks November 3rd GA failure. The compressed timeline demands focused execution addressing Kubernetes pod lifecycle management and resource contention issues.

**Looking Ahead**

Next week emphasizes resource cutline presentation and November release preparation while Brett addresses workbooks infrastructure scalability before GA deadline.

Anwar Mai presents resource allocation plan to Carlos demonstrating cutline impacts across 42 projects with reduced engineering capacity requiring executive prioritization decisions on agent infrastructure, GTM Config, international expansion, and Connected TV initiatives. Jesse Miller advances DeltaX campaign management path development while progressing DoubleO audience activation workflow integration and VRS is_bot flag person-level logic enhancement.

Matt Barnes completes website visitor journey signal PRD expansion while advancing FormComplete and visitor journey attribute mappings for data store integration. AI Page Rank early access monitoring continues with beta customer feedback collection informing production readiness assessment. Aadhitthyaa Hari Gopal progresses partner audience integration while advancing account AI toward November 14th target and coordinating November release end-to-end testing across custom reporting, conversion tracking, and identity partner onboarding.

Brett Elliot deploys scalable workbooks agent infrastructure by October 31st coordinating three-component solution enabling November 3rd GA while managing LiveIntent and 5x5 extended analysis for vendor continuation decisions. Shuxin Yang advances ALI data GTM Store ingestion coordination with Linda while creating organizational awareness of workbooks integration requirements and intent quality prioritization planning.

The team navigates substantial resource constraints requiring strategic trade-offs while maintaining November release commitments and addressing urgent infrastructure scalability challenges preventing platform capability degradation.

*Source: Team 1-2-3 Operating Framework entries from October 20, 2025*
