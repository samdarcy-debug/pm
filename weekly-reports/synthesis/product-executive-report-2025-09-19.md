---
id: synthesis-2025-38-2025
title: "Product Executive Intelligence Brief - September 19, 2025"
type: synthesis-report
status: approved
created: 2025-09-19
updated: 2026-01-06
week_ending: 2025-09-19
reporting_period: "September 15-19, 2025"
tags: ["weekly-report", "synthesis", "Q32025"]
---

# **Product Executive Intelligence Brief - September 15-19, 2025**

*Synthesized from 13 team reports: DAI Executive, SalesOS/Copilot, GTM Studio, Data Executive, Core Data, GTM Data Platform, Context Engineering, Semantic Data, MCP, Integrations, ZIM, Product BI, Product Operations*

*For detailed questions about any item below, reference specific team reports or contact team leads directly.*

## **Executive Summary**

### **Update on Previous Week Blockers**

**Critical privacy compliance issue threatening Canadian contact product:** Core Data Team reports continued work on email deliverability challenges with John Durst confirming \"6% of ZoomInfo\'s emails are marked as risky, confirming we remain above the 5% threshold that triggers enterprise email blocks\" and \"working on identifying paths forward for Canadian privacy concerns through direct legal interaction,\" though no definitive resolution achieved.

**Cross-functional coordination complexity consuming disproportionate development resources:** Mixed progress with some teams achieving breakthrough infrastructure wins while others continue facing systematic alignment challenges across legal, security, and engineering stakeholders.

### **Current Week Update**

**Blockers:**

- **Semantic search scalability blocking enterprise customer demos across multiple products:** GTM Studio Team reports \"semantic search layer continues blocking enterprise demos despite repeated assurances from engineering that issues are resolved. Jagannath escalated this as a technical scalability issue after Silver Fort demo had to be postponed for the second time in two weeks.\"

- **Cross-team coordination gaps consuming engineering resources disproportionate to technical complexity:** Multiple teams report similar patterns where \"communication gaps across teams emerged\" and \"assumptions about integration inclusion created unnecessary friction.\"

**Momentum areas:**

- **Data marketplace strategy achieving major public milestone with GTM.ai launch:** Data Executive Team reports \"GTM.ai successfully launched this week, marking a major milestone in our data marketplace strategy and publicly showcasing our integrated GTM studio experience\" while delivering \"production-ready Form 5500 data to sales teams\" and achieving \"exceptional validation through March Networks\' successful sample evaluation.\"

- **Copilot Workspace achieving strong internal validation with clear path to broader rollout:** SalesOS/Copilot Team reports \"Copilot Workspace launched successfully to 100+ internal users with strong engagement and valuable feedback identifying critical quality-of-life improvements needed for broader rollout.\"

The combination of public marketplace milestones and strong product validation positions us well for Q4 execution while persistent technical and coordination challenges require immediate leadership attention.

### **GTM Studio**

**GTM Studio Team:** \"The GTM Studio agent is rapidly approaching market readiness with 15+ internal users now onboarded and providing overwhelmingly positive feedback, calling it a \'game changer\' for capabilities they previously couldn\'t achieve. Jagannath is targeting a go/no-go decision by Wednesday based on internal validation, while simultaneously preparing for the October 16th Dreamforce demo where every attendee will likely be a ZoomInfo customer. The team faces a technical blocker with semantic search scalability that\'s preventing enterprise customer demos, requiring immediate engineering escalation.\"

### **GTM Copilot Workspace**

**SalesOS/Copilot Team:** \"Copilot Workspace launched successfully to 100+ internal users with strong engagement and valuable feedback identifying critical quality-of-life improvements needed for broader rollout. Ant Cuomo has profiles engineering-ready for 10/6 MVP while mobile V2 prototype work accelerates Q4 launch timeline. Multiple production launches completed including HubSpot CRM prioritization affecting 400+ customers, with Forrester Wave competitive positioning strengthened through comprehensive RFI responses.\"

### **GTM AI Context Service**

**Context Engineering Team:** \"The GTM Store connector architecture reached its design phase this week, unlocking critical signal availability for Workbooks and MCP tools---but completion slipped to next week due to final design complexity. Christine discovered Copilot V1 deprecation extends to September 2026, requiring us to maintain dual support longer than anticipated. Meanwhile, Robyn\'s team achieved breakthrough alignment on product hierarchy ownership with Brandon\'s org, positioning AI/ML to execute the initial scraping while establishing clear ownership boundaries for ongoing maintenance.\"

**Semantic Data Team:** \"Jon discovered and fixed a critical bug causing 6x LLM overcalling in email processing, immediately reducing token costs from 20,000+ to expected ranges. With authentication PRs landing next week, the pipeline achieves production-ready cost attribution per tenant. Meanwhile, sales adoption of semantic data in workbooks drove Rowan to push for batch processing implementation---a strategic move that delivers 50% cost reduction while enabling ZoomInfo to expand historical data coverage from 6 months to 1 year for all prospects and customers.\"

**MCP Team:** \"The team successfully deployed lookup-first functionality with batching that significantly improves search performance, while establishing the foundation for MCP resource management despite discovering Claude Desktop\'s manual resource addition requirement. With Henry\'s meetings now flowing through the system and showing value for meeting prep, the platform is demonstrating tangible executive utility. The distributed system architecture challenge for stateful communication needs solving before November\'s gateway release but doesn\'t block October 14th deliverables.\"

### **Vertical Datasets**

**Excerpt from DAI Report**: Brandon\'s vertical datasets initiative overcame major blockers by delivering production-ready Form 5500 data to sales teams and completing comprehensive enablement materials. The franchise dataset received exceptional validation through March Networks\' successful sample evaluation, while Aflac\'s insurance POC demonstrated substantial business impact with a projected six-figure expansion opportunity and immediate recruiting results.

### **Other Data**

**Data Executive Team:** \"GTM.ai successfully launched this week, marking a major milestone in our data marketplace strategy and publicly showcasing our integrated GTM studio experience. Igor Kyrylenko completed the franchisor dataset deployment in Snowflake with full traceability, while the team advanced franchise data automation and expanded multi-brand owner coverage. Dana Hurtig\'s team exceeded bad data fix targets by 15% and completed UDB matching for franchisees, with EMEA company infusions from Rhetorik data positioned for staging review.\"

**Core Data Team:** \"John Durst received testing results showing 6% of ZoomInfo\'s emails are marked as risky, confirming we remain above the 5% threshold that triggers enterprise email blocks. Magnus is documenting the complete history of our Spamhaus blacklisting that previously reduced throughput from 500,000 to 20,000 daily emails, creating foundational documentation for a solution. The team advanced multiple initiatives: Hayden formalized transparency metrics for Brandon\'s review, Peter defined requirements for scoops classifiers to extract more signals from news, and Heather scoped the Deal Cycle Agent with 1,200 eligible customers manually identified for opportunity data analysis, with Corp IT dependency for SF eligibility flags targeting 10/6 release to automate this customer identification process.\"

### **Other Platform**

**GTM Data Platform Team:** \"The Data Platform team delivered two major completions this week, with Marc Delurgio finalizing data access rules documentation and Menna Rashwan completing detailed identification of all Search-related data access and entitlement rules for third-party data. This foundational work establishes strong data privacy safeguards as we scale Federated Search across 1P, 2P, and 3P data sources. Meanwhile, Linda Johannessen continues advancing the metadata API work that will enable our October marketplace launch, though external API GraphQL support timelines remain a dependency to monitor.\"

**Integrations Team:** \"Prateek Paikray delivered vertical dataset preview functionality for GTM Studio, now live in staging and ready for backend API integration next week - in addition, continued intensive Agentforce testing ahead of Dreamforce to mitigate Salesforce\'s weekly breaking changes to their platform APIs. Meanwhile, Sanyog Rai worked with Agentic/Copilot Workspace team to get Meeting information directly from GTM DM as the first consumer in addition to drafting requirements for auto-creating GTM Accounts from engagements in GTM DM. Andres Perez advanced the CRM Field Mapping Agent POC to reduce dependence on admin config.\"

**ZIM Team:** \"Person-level intent production deployment now delivers 180 million daily signals to ZoomInfo through Brett Elliot\'s infrastructure work, while Path Factory partnership resolution enables continued field marketing lead generation. Forrester Wave demo script preparation progresses with comprehensive responses completed as the team advances toward flywheel data partner self-serve deployment through PLG workflow integration. September domain release deployed successfully while October MCR preparation begins for AI Page Rank and conversions features.\"

### **Other Operations**

**Product BI Team:** \"Copilot Workspace (V2) launched to 100+ internal GTM users this week with external customer rollout planned for early October. AJ Belan and Phoebe Mei identified a P0 instrumentation bug blocking user ID capture in Amplitude, which engineering is actively resolving. The team has strong momentum on renewal predictions, API usage analysis, and partnership metrics while navigating expected data architecture challenges with Coors integrations.\"

**Product Operations Team:** \"The Product Operations team achieved a significant breakthrough this week by establishing a clear pathway for microapps deployment through the connection between semantic data backend and ZI Chat, eliminating months of deployment challenges that have hindered our AI tool rollout. Sam Darcy successfully coordinated with William\'s team to implement MCP connections, while Kristin Gandini secured October roadmap commitment from Jack\'s ZI Chatbot team for LaunchDarkly integration. These infrastructure wins position us to accelerate deployment of the Voice of Customer tool, Knowledge Center agents, and other agentic applications without the networking complications that have slowed progress.\"

*For deeper analysis on any topic above, reference specific team reports or contact team leads directly.*

*Methodology: Analysis of team 1-2-3 Operating Framework reports, prioritizing: (1) Executive decisions needed, (2) Cross-team blockers, (3) Strategic momentum areas, (4) Strategic alignment gaps*

# **📊 Appendix**

### **Individual Team Reports**

## **DAI Executive Team Weekly Report - September 15-19, 2025**

## **Executive Summary**

The Copilot Workspace rollout to 100 internal go-to-market employees marked a pivotal milestone this week, delivering immediate validation of our AI-first platform vision while revealing critical user experience gaps that must be addressed before company-wide deployment. Victor led this rollout with strong early feedback showing users immediately understood the value proposition, though quality-of-life improvements in view creation and prompting are essential for broader adoption success.

## **This Week\'s Progress**

### **Key Momentum Areas**

Victor\'s Copilot Workspace internal rollout achieved significant validation with 100 go-to-market employees, where users consistently recognized the application\'s value in unifying multiple tools and providing account prioritization capabilities. The feedback confirmed strong product-market fit, with leaders like Laser noting this could be \"the stickiest application we\'ve ever built at ZoomInfo\" due to its universal appeal across SDRs, AEs, and managers.

Brandon\'s vertical datasets initiative overcame major blockers by delivering production-ready Form 5500 data to sales teams and completing comprehensive enablement materials. The franchise dataset received exceptional validation through March Networks\' successful sample evaluation, while Aflac\'s insurance POC demonstrated substantial business impact with a projected six-figure expansion opportunity and immediate recruiting results.

Brahm\'s GTM Studio workstream advanced multiple fronts simultaneously, achieving 90-95% completion on ROI Analytics milestones while onboarding 10+ internal users to the Studio Chat experience. The team successfully released an agentic chat experience for ROI assistance and completed initial testing on the GTM data model adoption, positioning the platform for end-of-month cutover and GA preparation.

### **Goals & Progress**

**Copilot Workspace:** Victor\'s team successfully deployed to 100 internal users with strong value recognition, though user experience challenges around view creation and chat prompting require immediate attention. Rather than proceeding with company-wide rollout, the team will expand to an additional 100 AE/AM users while implementing quality-of-life improvements including out-of-the-box views for managers and enhanced chat functionality.

**AI Context Service:** Adam\'s PMM narrative development for Dreamforce and broader AI context positioning is progressing with canonical messaging frameworks taking shape. The work addresses the need for clear talk tracks across Studio, Copilot, and AI context services, though coordination with Rowan\'s technical development and clearer service definitions remain ongoing priorities.

**Vertical Datasets:** Brandon\'s team resolved the primary blocker affecting sales teams by delivering Form 5500 production data and enablement materials. Strong validation from franchise samples with March Networks and insurance POC success with Aflac demonstrate clear market demand, while the team approaches GTM.ai launch readiness with infrastructure improvements underway.

### **Strategic Challenges**

The Copilot Workspace rollout revealed that while users grasp the product\'s value immediately, they struggle with the mechanics of creating effective views and crafting productive prompts. This represents a broader challenge in AI user experience design where the gap between understanding value and achieving it creates adoption friction. Victor\'s team is prioritizing enhanced out-of-the-box experiences and improved chat guidance to bridge this gap before broader deployment.

AI Context Service positioning remains fragmented across multiple teams and stakeholders, creating confusion in both product development and go-to-market messaging. Ali\'s assessment highlights the need for clearer service definition, unified ownership models, and better articulation of what specific problems the context service solves for different user types and use cases.

Email notification queue challenges threaten to impact partner onboarding and data delivery capabilities, requiring cross-team coordination between PTI, email delivery teams, and Acton to resolve ownership ambiguities. Brandon\'s team has identified a clear remediation path, but the complexity of multi-vendor coordination poses timing risks for self-serve flywheel partner launches.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The internal Copilot Workspace deployment revealed that product-market fit validation doesn\'t automatically translate to user activation success. Users immediately understood the value proposition but encountered friction in the execution layer, specifically around view creation and effective prompting. This insight reinforces the need for AI applications to provide stronger guidance and scaffolding rather than assuming users can immediately leverage advanced capabilities.

Cross-functional coordination gaps emerged as a significant theme across multiple initiatives, from partnership integration processes to AI credit implementation. The team\'s work on contributory network data ingestion and website key buyer ID requirements revealed systematic challenges in aligning legal, security, and engineering stakeholders that consume disproportionate time relative to technical complexity.

AI artifact creation and chat functionality show promise as differentiating user experiences, with internal teams gravitating toward these capabilities over traditional interface patterns. This suggests the platform\'s future direction should emphasize conversational interfaces and dynamic content generation rather than conventional dashboard approaches.

### **Cross-Team Dependencies**

Our work with the enablement team on Copilot Workspace deployment continues to be essential for successful field adoption. The team requires more prescriptive guidance on cohort targeting, training schedules, and messaging frameworks to ensure sales teams can effectively leverage the platform for Q4 renewals and expansions. Victor and AJ are coordinating closely on demo preparation and talk track development for the critical September 29th enablement session.

Platform infrastructure dependencies around AI credit implementation, semantic search scalability, and prompt service architecture affect multiple product initiatives simultaneously. These foundational elements require coordinated engineering attention to prevent development bottlenecks across Studio, Copilot, and Context Service workstreams.

## **Looking Ahead**

Next week focuses on expanding Copilot Workspace to an additional 100 users while implementing user experience improvements based on initial feedback. The team will prioritize out-of-the-box views for different personas, enhanced chat guidance, and streamlined view creation processes to improve activation rates before broader company deployment.

The critical path centers on finalizing platform narrative development for Dreamforce positioning while ensuring demo readiness for the September 29th enablement session. This requires close coordination between Adam\'s PMM work, Victor\'s product development, and AJ\'s enablement coordination to deliver cohesive messaging and compelling demonstrations that sales teams can immediately operationalize.

Strategic priorities include resolving AI Context Service positioning clarity, advancing vertical datasets toward broader availability, and strengthening the foundation for Q4 renewal and expansion activities. The team\'s ability to maintain current development velocity while managing increasing go-to-market demands will be crucial for achieving year-end objectives and positioning for 2026 growth initiatives.

*Source: DAI Executives Operating Framework entries from September 15th, 2025 - September 19th, 2025*

## **SalesOS/Copilot Executive Roundup - September 15-18, 2025**

## **Executive Summary**

Copilot Workspace launched successfully to 100+ internal users with strong engagement and valuable feedback identifying critical quality-of-life improvements needed for broader rollout. Ant Cuomo has profiles engineering-ready for 10/6 MVP while mobile V2 prototype work accelerates Q4 launch timeline. Multiple production launches completed including HubSpot CRM prioritization affecting 400+ customers, with Forrester Wave competitive positioning strengthened through comprehensive RFI responses.

## **This Week\'s Progress**

### **Key Momentum Areas**

Adam Severance executed a successful Copilot Workspace internal launch to over 100 users, generating extensive feedback that revealed both strong user engagement and specific usability improvements needed for the next wave rollout. The feedback is driving immediate optimizations in view manipulation, filter controls, and chat context accuracy that will strengthen the foundation before expanding to 200+ additional users next week.

Harinath Krishnamoorthy delivered two major production feature launches - HubSpot CRM package prioritization and Date Filter in AFS - impacting 400+ customers while completing comprehensive Forrester Wave RFI responses that strengthen ZoomInfo\'s competitive differentiation in the Revenue Marketing category. His Q4 2025-H1 2026 roadmap now includes 10 strategic initiatives spanning persona-based intent, new data sources, and multi-product support.

Gabe Pirela advanced the email agent architecture to a sub-agent pattern on the agentic platform, enabling more scalable and reliable bulk email capabilities while launching the internal MEDDPIC extraction pilot with 25+ reps receiving automated post-call analysis via Slack. Design work for the deal qualification assistant in Copilot Workspaces is progressing rapidly with engineering validation confirmed.

### **Goals & Progress**

**Profiles & Mobile Development:** Ant Cuomo has GTMC profiles designs finalized and engineering dependencies resolved, ensuring 90% of planned features will be ready for the 10/6 MVP launch. Mobile V2 development gained momentum with two major agents (Pulse for daily priorities and Discover for research insights) in active development, positioning the team ahead of Q4 mobile expansion goals.

**Email & Automation Systems:** The email agent transition to sub-agent architecture unlocked bulk email use cases while improving repeatability and token efficiency across all chat interactions. MEDDPIC extraction automation is generating high-quality outputs for internal validation, with parallel design streams preparing the Copilot Workspace integration for rapid deployment once validation completes.

**Infrastructure & Territory Management:** David Goulden made progress on admin-defined territories despite increasing complexity from enterprise customer requirements for Salesforce integration and bulk upload capabilities. Zero admin setup discussions with Tingting\'s team are clarifying domain ownership and establishing foundation for 5-day onboarding goals, though significant alignment work remains.

### **Strategic Challenges**

Priority accounts API fragmentation continues to create complexity across multiple teams, with engineering dependencies on federated search capabilities still being resolved. David Goulden\'s team needs standardization of the Priority Accounts API and clarity on GTM data model integration to support enterprise CRM setups effectively. The current distributed approach requires coordination across Platform, Enterprise Search, and multiple product teams.

Copilot Workspace feedback reveals fundamental usability issues in view manipulation and filter controls that could impact broader rollout success if not addressed quickly. Adam Severance identified chat hallucination problems, including incorrect ACV calculations that erode user trust, requiring immediate attention to context accuracy and data validation before expanding the user base beyond the current 100-person cohort.

Admin-defined territories faces increasing scope complexity as enterprise customers request Salesforce territory import and bulk upload capabilities that extend beyond the original vision. The integration requirements with CRM data models and ongoing maintenance challenges may require architectural decisions about API approaches versus out-of-the-box solutions for sustainable scaling.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The sub-agent architecture implementation by Gabe Pirela\'s team revealed that the previous monolithic agent approach was causing repeatability issues and excessive token usage. The new coordinator pattern with specialized sub-agents shows early promise for both cost efficiency and response quality, establishing a scalable foundation for future agent development across all product areas.

Internal user feedback from Copilot Workspace launch demonstrated that quality-of-life features matter more than advanced capabilities for driving adoption. Users prioritize reliable filter manipulation, accurate data context, and smooth view transitions over complex AI features, suggesting the product strategy should emphasize foundational user experience excellence before adding sophisticated automation layers.

Enterprise territory management requirements prove significantly more complex than anticipated, with customers using territories for both rule-based matching and CRM segmentation. This discovery challenges the current approach and may require fundamental architectural decisions about whether to extend the GTM data model early in its lifecycle or develop more sophisticated integration patterns.

### **Cross-Team Dependencies**

Our work with the Agentic Platform team on sub-agent architecture continues to be critical for email functionality and overall chat experience reliability. Lars and Ryan\'s team has confirmed feasibility for bulk email use cases while implementing the coordinator pattern that will benefit all future agent development across the platform.

Design team coordination with Megan Cartlidge becomes increasingly important as multiple initiatives (profiles, mobile, MEDDPIC extraction, engagement widgets) require concurrent design work. The team is managing competing priorities while maintaining quality standards across initiatives targeting the 10/6 launch date.

## **Looking Ahead**

Next week focuses on executive go/no-go decisions for expanding Copilot Workspace from 100 to 200+ users based on current feedback resolution and quality improvements. The team will prioritize addressing chat context accuracy, view manipulation issues, and filter controls while preparing persona-specific FTUE for the next wave rollout.

Engineering kickoffs for profiles will accelerate development toward 10/6 MVP delivery while mobile V2 agent development continues with Pulse and Discover prototypes. MEDDPIC extraction pilot feedback will inform rapid iteration cycles leading to Copilot Workspace integration planning. Territory management decisions on Salesforce integration scope and zero admin setup alignment will establish foundation for sustainable enterprise customer onboarding.

The successful internal launch momentum positions the team well for broader rollout while current feedback provides clear optimization priorities that will strengthen the product foundation before external customer exposure.

*Source: Team SalesOS/Copilot Operating Framework entries from September 15th - September 18th, 2025*

## **GTM Studio Executive Roundup - September 15-19, 2025**

## **Executive Summary**

The GTM Studio agent is rapidly approaching market readiness with 15+ internal users now onboarded and providing overwhelmingly positive feedback, calling it a \"game changer\" for capabilities they previously couldn\'t achieve. Jagannath is targeting a go/no-go decision by Wednesday based on internal validation, while simultaneously preparing for the October 16th Dreamforce demo where every attendee will likely be a ZoomInfo customer. The team faces a technical blocker with semantic search scalability that\'s preventing enterprise customer demos, requiring immediate engineering escalation.

## **This Week\'s Progress**

### **Key Momentum Areas**

Jagannath successfully onboarded 15+ internal users to the GTM Studio agent, exceeding the initial goal of 10 users. The feedback has been consistently positive, with users describing breakthrough moments where they can complete end-to-end journeys through natural conversation alone. Rob Lauren from sales leadership recently completed a full ICP building workflow using only conversational interface, demonstrating the platform\'s potential to reshape how B2B teams interact with data and automation tools.

Mohan made significant progress on Co Pilot activation alignment, establishing clear understanding between the context and configure teams on backend data structure. The team successfully reframed the GTM config work as \"GTM config agent\" rather than onboarding, which clarified scope and priorities across multiple stakeholders. Engineering resources have been identified to begin agent work on Monday.

Tanvi advanced the signals initiative to staging with both signal enrichment and signal-based workbook creation ready for testing. The team completed multiple bug review sessions and made necessary trade-offs to address last-minute technical complexities. Smart sheet\'s early access program reinforced the person-has-moved use case that bridges current Enrich Premium Plus and RingLead capabilities.

### **Goals & Progress**

**Agent Development:** The GTM Studio chat agent moved to production with 15+ active internal users providing validation feedback. Jagannath integrated AI email generation capabilities into GTM Studio using the agent framework, with staging deployment complete and production release planned for next week. The team established product analytics and production readiness frameworks to support wider rollout decisions.

**Data Infrastructure:** Engineering completed GTM Data store migration work and deployed to staging environment. Arun\'s team tested 5 beta accounts with 99% data matching between legacy ZDP tables and new GTM Data store tables. Multiple ROI analytics features launched this week including Q agent enhancements, advanced filtering by interaction types, and improved CRM error handling for better user guidance.

**Workbook Capabilities:** Tanvi pushed signals production release to September 30th to accommodate comprehensive testing and bug fixes. The team discovered federated search limitations when layering data points from different sources, implementing temporary workarounds while planning transition to Raul architecture later this year. Smart sheet validation confirmed dynamic contact search patterns that span multiple data sources.

### **Strategic Challenges**

The semantic search layer continues blocking enterprise demos despite repeated assurances from engineering that issues are resolved. Jagannath escalated this as a technical scalability issue after Silver Fort demo had to be postponed for the second time in two weeks. This capability represents significant market differentiation, and the continued delays are preventing customer validation of key value propositions that distinguish GTM Studio from Clay and other competitors.

Workbook user onboarding revealed consistent patterns where early access customers feel overwhelmed by capabilities and request more guidance, templates, and starter use cases. While the positive overwhelm indicates product-market fit potential, the lack of structured onboarding may limit adoption velocity and engagement retention. Tanvi identified this as similar to historical RingLead implementation challenges that required extensive customer success resources.

Cross-functional dependencies remain complex as the team balances route pricing strategy with GTM Studio integration. The existing \$7 million route revenue stream needs clear packaging decisions as routing capabilities migrate into workbooks. Brahm highlighted the importance of understanding revenue impact as features previously sold separately become integrated platform capabilities.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Clay\'s conference event this week launched competing agent capabilities, prompting immediate competitive analysis needs. Jagannath will build battle cards to address internal questions about differentiation and positioning. The timing suggests the conversational AI space for B2B operations is accelerating rapidly, validating GTM Studio\'s strategic direction while emphasizing execution urgency.

Rob Lauren\'s end-to-end journey completion using only conversational interface provided concrete validation of the agent\'s potential to transform application development patterns. This breakthrough moment demonstrated that complex multi-step workflows requiring various data sources and decision points can be completed through natural language alone, suggesting traditional UI experiences may become secondary interfaces within 2-3 years.

Early access program feedback revealed consistent patterns around guidance and template needs across multiple customer segments. Smart sheet, Silver Fort, and other prospects all requested similar onboarding structures, suggesting scalable solutions for user activation. The pattern mirrors successful implementation approaches but requires proactive design to avoid resource-intensive custom guidance models.

### **Cross-Team Dependencies**

Data management milestone alignment between Corina and Ash continues progressing with M2 requirements handed off to engineering and pre-grooming sessions completed. The Enrich Premium Plus for Microsoft Dynamics integration tested successfully, providing confidence for public launch and capturing pending \$300k upsell opportunity. Health scan dashboard POC development involves ongoing collaboration with account management to ensure sales narrative strength for Q4 revenue capture.

Tingting\'s GTM config agent work requires continued alignment with context team on database structure and postgres integration. The Monday engineering kickoff will determine prototype feasibility and identify any missing tools or endpoints needed for zero-configuration data flows.

## **Looking Ahead**

Next week centers on the critical go/no-go decision for broader GTM Studio agent rollout, with Wednesday as the decision point based on internal user validation. Simultaneously, Dreamforce preparation intensifies with demo environment setup and public workbook sharing capabilities for lead generation.

The team will escalate semantic search resolution while building Clay competitive analysis and battle cards for internal enablement. Mohan leads Co Pilot activation engineering kickoff on Monday, while Tanvi continues signals testing toward September 30th production release. Data management advances both health scan dashboard development and M4-M5 requirement documentation to maintain momentum toward Q4 sales enablement.

Engineering sprint planning will incorporate GTM Data store migration completion, multi-currency support implementation, and taxonomy integration for GA readiness. The convergence of these initiatives positions October as a pivotal month for both internal validation and early customer conversion through paid POC programs.

*Source: Team 1-2-3 Operating Framework entries from September 15-19, 2025*

## **Data Executive Roundup - September 15-18, 2025**

## **Executive Summary**

GTM.ai successfully launched this week, marking a major milestone in our data marketplace strategy and publicly showcasing our integrated GTM studio experience. Igor Kyrylenko completed the franchisor dataset deployment in Snowflake with full traceability, while the team advanced franchise data automation and expanded multi-brand owner coverage. Dana Hurtig\'s team exceeded bad data fix targets by 15% and completed UDB matching for franchisees, with EMEA company infusions from Rhetorik data positioned for staging review.

## **This Week\'s Progress**

### **Key Momentum Areas**

The GTM.ai site went live, providing customers with public access to our new data marketplace and demonstrating the investments we\'re making to improve data coverage while driving awareness of our integrated GTM studio experience. This launch positions us well for expanding our vertical dataset offerings and creates a foundation for more self-service data interactions.

Igor\'s completion of the franchisor dataset in Snowflake delivered four production-ready tables (franchisor, franchisee, location, and contact) with successful ZoomInfo matching and full lineage traceability. This structured, matched format provides customers with unique visibility into franchise ownership structures that competitors cannot offer, directly supporting our custom data acquisition program and enabling sales to pitch differentiated datasets to enterprise accounts.

Steve Hutchinson progressed user-level POI implementation with the first interest type moving toward production next week. This foundational work establishes the framework for bringing multiple new interest types to POI, improving person-level signal relevance and positioning us to better power AI agents for person search functionality.

### **Goals & Progress**

**Vertical Datasets:** Igor Kyrylenko automated franchise data processing pipeline elements and expanded multi-brand owner coverage through AI-generated contacts, while Dana Hurtig completed UDB matching for franchisees and delivered enrichments at 115% of projected targets. Brandon Tucker advanced Form 5500 dataset enablement, ensuring Data Services can pull samples for the top 50+ franchisors to support more proactive customer engagement.

**GTM Platform Integration:** Brandon Wilson generated aggregated views for opportunity data at different sales cycle stages, providing the base dataset for the contributory network benchmark agent that will help customers understand deal cycle patterns and timing benchmarks. This work directly supports Heather Ma\'s development of the benchmark agent prototype demonstrated this week.

**Data Quality & Coverage:** Dana\'s team processed 2.2M enrichments including 2M freemails from 5x5 and resolved 200K bad data records, while EMEA company data from Rhetorik advanced toward staging for production review. These improvements strengthen our core data foundation and expand geographic coverage in key markets.

### **Strategic Challenges**

The Form 5500 dataset requires enhanced Data Services enablement around data dictionaries, as competitors use different column naming conventions that create confusion during customer evaluations. Brandon Tucker is addressing this through improved documentation and sample provision to help go-to-market teams navigate the complexity and respond more effectively to customer queries about data availability and structure.

Translation strategy alignment across data productions remains an open question, with Igor noting complete datasets available in multiple countries (Australia, France, Germany, Sweden, UK) that could be published in native languages. Jody Roberts initiated conversations to establish a coordinated approach for what languages we support, how we store translated information, and prioritization of different geographic markets beyond current focus areas.

Manager attribute integration from GAL and Google Directory data into the PTI pipeline shows promise for improving org chart functionality, but requires additional scoping and prioritization discussions. The potential to leverage data from 100K domains with management association coverage could significantly enhance our org chart agent capabilities, though implementation timeline needs clarification.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The contributory network benchmark agent prototype revealed significant customer appetite for deal cycle insights based on aggregated opportunity data across our network. With 1,200+ companies providing permission to share data, we can deliver unique benchmarking insights that competitors cannot replicate, particularly around stage-by-stage analysis and seasonal buying patterns that provide actionable intelligence for sales teams.

Our franchise data quality validation uncovered that manual verification processes, while thorough, need efficiency improvements to scale effectively. Dana\'s team completed validation for the top 100 franchisors but identified the need for additional resources to process the full list of \~2,500 efficiently, highlighting opportunities to optimize validation workflows for future vertical dataset launches.

The GAL and Google Directory data analysis showed minimal overlap between sources, creating opportunities to use both for comprehensive manager attribute coverage. This discovery supports more robust org chart generation and could significantly improve the accuracy and completeness of organizational hierarchy data available to customers.

### **Cross-Team Dependencies**

Our work with the GTM team on vertical dataset enablement continues to be essential for achieving H2 revenue targets. Current focus on contractor, franchise, and restaurant datasets requires continued collaboration on account targeting, sample provision, and sales enablement to ensure field teams can effectively communicate value propositions and advance opportunities with qualified prospects.

The benchmark agent development depends on coordination between Brandon Wilson\'s data aggregation work and Heather Ma\'s agent implementation, with both teams working to refine opportunity data analysis and user interface design. Success here requires ongoing alignment on data requirements and presentation formats to ensure the agent delivers actionable insights rather than just informational summaries.

## **Looking Ahead**

Next week\'s primary focus centers on advancing production readiness across multiple fronts while maintaining momentum on customer-facing capabilities. The team will push user-level POI data to production, complete franchise dataset automation, and continue EMEA company infusion validation.

Igor will publish FINRA data to Snowflake with schema documentation while completing QA verification for the franchise automation pipeline. Steve\'s team will move from staging to production for the first POI interest type, establishing the foundation for additional interest types in subsequent weeks. Dana will finalize EMEA company data review and initiate the next phase of geographic expansion, while Brandon Wilson continues benchmark agent data model development to support Heather\'s agent implementation work.

The convergence of these efforts positions us well for Q4, with vertical datasets gaining market traction, contributory network capabilities demonstrating clear value, and core data quality improvements supporting all downstream applications. Our ability to deliver unique, high-quality datasets while providing innovative tools for customers to understand and leverage that data creates a compelling competitive advantage in the evolving data marketplace.

*Source: Data Executive Operating Framework entries from September 15th, 2025 - September 18th, 2025*

## **Core Data Executive Roundup - Week of September 15-19, 2025**

## **Executive Summary**

John Durst received testing results showing 6% of ZoomInfo\'s emails are marked as risky, confirming we remain above the 5% threshold that triggers enterprise email blocks. Magnus is documenting the complete history of our Spamhaus blacklisting that previously reduced throughput from 500,000 to 20,000 daily emails, creating foundational documentation for a solution. The team advanced multiple initiatives: Hayden formalized transparency metrics for Brandon\'s review, Peter defined requirements for scoops classifiers to extract more signals from news, and Heather scoped the Deal Cycle Agent with 1,200 eligible customers manually identified for opportunity data analysis, with Corp IT dependency for SF eligibility flags targeting 10/6 release to automate this customer identification process. She secured Legal approval to expand contact enrichment beyond CRM integration to include Calendar and Email data sources, while progressing the CN Data Advisor agent with workarounds for Google Sheets integration limitations. A NeverBounce credit expiration fix deployed over the weekend is causing API degradation that the team is monitoring.

## **This Week\'s Progress**

### **Key Momentum Areas**

Peter delivered a PRD for scoops classifier models, explaining the opportunity to leverage years of researcher-annotated data to improve news extraction. His analysis revealed that current review rooms focus on single scoop types per article (missing others) and take up \~50% researcher time for \~10% of scoops volume. His work highlighted the opportunities for automation including multi-type classification, topic tagging and relevance scoring. He believes these are very attainable because Research has already annotated the model training data. He also analyzed the \"orphaned company\" opportunity (39MM URLs in total) where a 5K record suggests +225,000 net new companies and +36MM million new attributes.

Magnus finished a 6-page document explaining ZoomInfo\'s email throughput issues, incorporating feedback from PTI engineering, legal, and NeverBounce teams. His work documents why we can\'t send more privacy notices and outlines solutions based on Kevin\'s identification of park domains, hard bounces, and spam traps as root causes. This creates the first comprehensive starting point for building a PRD and doing product discovery.

Hayden converted last week\'s transparency metrics brainstorming into a formal proposal artifact, reviewing it with Jody and John before Friday\'s scheduled presentation to Brandon. Cam completed the October cube release notes draft and began work on Brandon\'s specific request to predict industry values where \"photography studio\" is currently over-represented as a catch-all category.

### **Goals & Progress**

**Email Validation Strategy:** John\'s formal review of risk testing confirmed the 6% risk rate, while working on identifying paths forward for Canadian privacy concerns through direct legal interaction. The team discovered the 25,000 daily email limit is self-imposed rather than system-mandated, with John noting they have \"high enough reputation\" to potentially increase volumes carefully using the Impression Wise POC for additional breathing room.

**Deal Cycle Agent Development:** Heather progressed on the benchmark agent initiative, scoping the first agent in this category as the \"Deal Cycle Agent,\" which provides cycle length insights for target companies based on network data. The team revisited eligible customers who can share opportunity data and identified the current manual process challenges. Since the condition to determine whether a customer is on the most recent 05_01_2025 EULA contract exists in Salesforce rather than ZDP, implementing a new eligibility flag in SF is required. This dependency is currently in progress with the Corp IT team, targeting release by 10/6.

Despite the manual limitations, the team identified 1,200 eligible customers who are on the most recent license and have the CRM opportunity data sharing tile toggle enabled. This represents the starting point for running further analysis of the Deal Cycle Insights agent. Initial eyeballing analysis revealed expected challenges including data hygiene issues, duplication, and low sample counts. A comprehensive report is planned for next week to better estimate data quality and quantity.

**CN Data Collection Expansion:** Heather conducted a deeper review with the Legal team on the current data sharing page use case list. Legal agreed to modify the language around \"Contacts Enrichment\" to include non-CRM integration vendors, expanding beyond the previously strict \"CRM Mismatch Contact Enrichment\" language. This approval enables the team to start ingesting participant data from Calendar, Email, and other sources, and continue exploring email signatures from Chorus. The \"Umbrella\" use case phrasing for collecting additional customer data remains under legal review.

**ZI Chat CN Data Advisor Agent:** Work continues on providing an overall view of data flowing into CN, supported vendors, and legal review status. However, since the current toolset doesn\'t support Google Sheets (the main format for this type of knowledge), the team is implementing a workaround by converting Google Sheets to CSV or PDF format until Google Sheets integration is supported in October.

**Operational Excellence:** Jody made progress across multiple initiatives, including reviewing the Forrester questionnaire for data inputs and demonstrating org chart capabilities to Brandon\'s staff Thursday. The translation strategy meeting aimed to align on international data support beyond the current \"take what we get\" approach, with Magnus joining to represent Shared Services\' interest in languages and titles.

### **Strategic Challenges**

The NeverBounce credit expiration created immediate operational risk when implemented without coordination. For 3.5 years, terms of service stated credits expire after one year, but the code didn\'t exist---raising finance concerns about revenue misrepresentation. The weekend deployment by the Israeli team is causing API degradation, which led to VP\'s of engineering rolling back the implementation. The NeverBounce back end team created a short term solution until the app team can fix the latency issues long term.

Engineering teams in Israel have 2+ holiday days off during each of the next 4 weeks. Because their week starts Sunday, and many of these holidays are Mon/Tues, only Wednesday morning is available for working hours overlap. The team is working on ways to avoid potential delays to key releases.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The 6% email risk rate confirms what Magnus describes as potentially catastrophic---crossing the 5% threshold means enterprises block all communications. Kevin\'s analysis identified the specific triggers (park domains, hard bounces, spam traps), while the realization that 25,000 daily sends is self-imposed rather than technically required provides immediate expansion opportunity through careful testing.

Peter\'s scoops analysis quantified the inefficiency of current review rooms: articles with 8+ potential scoops get processed for just one type. His PRD proposes using validated historical data to train classifiers for automation, freeing up the team to annotate new datasets such as awards, ratings, user counts, contracts, and product launches. Next steps include reviewing with Nilesh\'s team and establishing LLM baselines before Data Science roadmap inclusion.

The disconnect between NeverBounce\'s legal terms and technical implementation for 3.5 years highlights systemic gaps in product-engineering alignment. Similarly, the industry model\'s \"photography studio\" over-classification demonstrates how data quality issues compound over time without systematic correction.

The Deal Cycle Agent development revealed infrastructure gaps in customer eligibility determination, highlighting the manual processes that currently limit automated data pipeline operations. The dependency on Corp IT for SF implementation demonstrates the cross-functional coordination required for CN expansion.

### **Cross-Team Dependencies**

Email deliverability requires coordination with Legal on Canadian privacy paths and Marketing on sending practices affecting reputation scores. John works directly with Legal while the broader team needs alignment on whether to remove risky emails or implement different cutoffs based on testing results.

The benchmark agent depends on Brandon Wilson\'s analysis team exploring opportunity data, with integration requirements being validated through office hours with the chat team. Translation strategy involves multiple data production teams, requiring alignment on regional prioritization and language support capabilities.

## **Looking Ahead**

Friday\'s meeting with Brandon will determine engineering priorities for the transparency metrics MVP, with Jody noting \"Brandon is very excited slash anxious to make progress here.\" Thursday\'s staff meeting demonstration of Cam-related agents represents a key milestone for proving value to executive leadership.

The email workstream continues with decisions on remediation approach---whether removing risky emails and testing recurringly or implementing different cutoffs. Magnus\'s documentation provides the foundation for product discovery while John explores expanding volumes through Impression Wise validation.

For the CN agent initiatives, next week will focus on delivering the comprehensive data quality report for the Deal Cycle Agent analysis and continuing work on the CN Data Advisor agent workarounds until Google Sheets integration is available. The Corp IT SF eligibility flag remains a critical dependency to watch for the 10/6 target date.

Peter will review the scoops PRD with Nilesh\'s team to establish baselines before Data Science roadmap inclusion, while continuing to support David on Form 5500 schema and pushing SEC filings to GTM Store production. Resolution of the NeverBounce API issues remains immediate priority, with John suggesting PI team monitoring though noting it\'s \"probably not\" a major risk.

*Source: Core Data Team 1-2-3 Operating Framework entries and team sync transcript from September 15-19, 2025*

## **Data Platform Team Executive Roundup - September 19, 2025**

## **Executive Summary**

The Data Platform team delivered two major completions this week, with Marc Delurgio finalizing data access rules documentation and Menna Rashwan completing detailed identification of all Search-related data access and entitlement rules for third-party data. This foundational work establishes strong data privacy safeguards as we scale Federated Search across 1P, 2P, and 3P data sources. Meanwhile, Linda Johannessen continues advancing the metadata API work that will enable our October marketplace launch, though external API GraphQL support timelines remain a dependency to monitor.

## **This Week\'s Progress**

### **Key Momentum Areas**

Marc Delurgio completed and distributed comprehensive documentation covering data access rules for both the Query API and Search functionality. This work will receive stakeholder review and represents a significant step toward ensuring adequate data privacy implementation across the platform. The documentation now provides clear guidelines for how data access should be managed as we expand platform capabilities.

Menna Rashwan successfully identified and documented all current Search-related data access and entitlement rules for third-party data used in ZoomInfo. Working closely with core engineering and product stakeholders, she validated these rules and discovered that existing platform-level privacy functionality can potentially be leveraged to support some of the 3P data access rules within Search, minimizing duplication and ensuring alignment with broader platform standards.

Linda Johannessen delivered new dataset schema definitions to consumers and has the staging API targeted for next week. Her work on federated search metadata mapping into the GraphQL API for proof-of-concept purposes demonstrates strong progress, and she has begun the Website Journey Signal model analysis that will inform future funnel-style insights capabilities.

### **Goals & Progress**

**Query API and Metadata Development:** Linda continues making solid progress on the metadata model and API work, with the new dataset schema now delivered to consumers and staging API targeted for next week completion. The federated search metadata has been successfully mapped into GraphQL API for POC demonstration, showing the technical approach is sound. However, connecting external sources like Salesforce into GraphQL for Copilot requires API-level mapping beyond just schema alignment, raising questions about the complexity of this integration path.

**Match Service and Location Matching:** Moshik Levin followed up with stakeholders regarding changes in location matching to ensure minimal impact on current operations. He has initiated the official release change management process, targeting November for implementation. The team will make final decisions on Monday regarding which dispositions to use for match reasons, then shift focus to consolidating new requirements for location matching in Q4 initiatives including Workbooks and New Company Creation.

**Unified Profile Integration:** Adwait Kirtikar aligned with the Application product team on how to partner and progress on Unified Profile (Account) integration into front-end applications. There\'s high-level alignment with Ant Cuomo on initial use cases that could be candidates for Unified Profile integration on Applications. The next phase involves publishing a transition document focusing on core Unified Profile service, UI components, design mockups, and product discovery interviews with Copilot V2 customers.

### **Strategic Challenges**

The External API team\'s support for GraphQL remains a dependency that could impact externalization timelines for the November release. While there\'s been progress on establishing milestone plans, the complexity of supporting GraphQL in the external-facing API requires careful coordination and may need alternative approaches if timelines become constrained. This affects our ability to deliver the full metadata API experience externally as planned.

Connecting external data sources like Salesforce into the GraphQL API for Copilot applications presents technical complexity beyond initial expectations. The integration requires API-level mapping rather than just schema alignment to ensure a clean user experience, which raises questions about whether this integration path should be pursued or if simpler alternatives might be more appropriate for initial releases.

The location matching work that Moshik is leading involves careful change management to minimize impact on existing customers. While progress is being made toward November implementation, the team must balance improving matching capabilities with maintaining consistency for current users, requiring ongoing coordination with DaaS leads and other stakeholders.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team discovered that existing platform-level privacy functionality can potentially be leveraged and mapped to support some of the 3P data access rules within Search. This finding by Menna represents a significant opportunity to minimize duplication of effort and ensures better alignment with broader platform standards as we scale Federated Search capabilities. Rather than building separate privacy controls for Search, we can build upon existing infrastructure.

Marc\'s comprehensive documentation work revealed the importance of establishing clear data access rules early in platform development. Having these guidelines documented and reviewed by stakeholders provides a foundation for consistent implementation across different platform components and helps ensure that privacy considerations are built into the architecture rather than added as an afterthought.

The federated search metadata mapping work has shown that GraphQL integration is technically feasible, but the complexity of connecting external sources like Salesforce requires more sophisticated API-level mapping than initially anticipated. This suggests that we may need to phase the rollout of different data sources or develop more sophisticated integration patterns for complex external systems.

### **Cross-Team Dependencies**

Our work with the External API team on GraphQL support continues to be important for the November externalization timeline. We need clear commitments on GraphQL scope and delivery timelines to ensure the metadata API can be properly externalized. The complexity of this integration may require exploring alternative approaches or adjusting timelines to ensure successful delivery.

The Unified Profile work requires continued collaboration with Application product teams and design leadership to ensure proper integration into ZoomInfo applications. Adwait\'s alignment with Ant Cuomo provides a good foundation, but broader team engagement will be needed to ensure the unified profile experience is consistent and intuitive across applications.

## **Looking Ahead**

Next week focuses on delivering the staging API for Linda\'s metadata work and completing the final documentation and decision-making for Moshik\'s location matching changes. The team will also continue advancing the federated search GraphQL integration and extend the work into Website Journey Signal analysis.

Marc will work with stakeholders to finalize any remaining data access rule questions and ensure the documentation is ready to support implementation. Linda will onboard new vertical and signal datasets while preparing for the October Workbook integration milestone. The team will also begin extending federated search capabilities and continue Website Journey Signal analysis to scope model changes for enhanced funnel-style insights.

The week ahead will be crucial for maintaining momentum on the October marketplace delivery while ensuring that the foundational data access and privacy work is properly implemented. Success depends on continued stakeholder engagement and careful management of external dependencies, particularly around GraphQL support timelines.

*Source: Team 1-2-3 Operating Framework entries from September 15, 2025*

## **Context Engineering Team Executive Roundup - September 19, 2025**

## **Executive Summary**

The GTM Store connector architecture reached its design phase this week, unlocking critical signal availability for Workbooks and MCP tools---but completion slipped to next week due to final design complexity. Christine discovered Copilot V1 deprecation extends to September 2026, requiring us to maintain dual support longer than anticipated. Meanwhile, Robyn\'s team achieved breakthrough alignment on product hierarchy ownership with Brandon\'s org, positioning AI/ML to execute the initial scraping while establishing clear ownership boundaries for ongoing maintenance.

## **This Week\'s Progress**

### **Key Momentum Areas**

Sri\'s GSO -\> GTM Store connector will create the foundation for exposing all signals through Workbooks as well to agents via MCP tools. The schema is defined, but the connector still needs to be designed \-- aiming to complete this next week.

Robyn secured organizational alignment on the product hierarchy initiative, with AI/ML team taking ownership of initial web scraping while Brandon\'s team commits to ongoing maintenance. This division of labor leverages each team\'s strengths---AI/ML\'s scraping expertise for the heavy lift, and Brandon\'s team\'s product knowledge for sustained accuracy. The hierarchy directly enables account brief generation to produce product-specific positioning rather than generic company messaging.

Christine\'s ZI API for insights reached staging deployment, providing the critical infrastructure needed for AgentForce demo integration by mid-October. This API advancement, combined with the bulk endpoint work for Workbooks, positions us to hydrate full insight lists beyond the current 50-item limit while supporting external agent integrations.

### **Goals & Progress**

**Signal Infrastructure:** Sri\'s GSO to GTM Store connector advanced to schema completion, with the design now incorporating one namespace per signal type architecture based on stakeholder feedback. The 50% completion reflects schema finalization while connector design remains in review with the architecture team. This foundational work directly unblocks signal availability for both Workbooks and MCP tools, with early next week targeted for design lock.

**AI/ML Integration:** Robyn achieved 100% completion on establishing AI/ML use cases for Copilot, though product requirements remain unclear regarding insight aggregation versus raw signal exposure. The team validated Lookalikes readiness for top 100K queries at ZoomInfo scale, with MCP tool development proceeding in parallel. Critical alignment achieved on using Account Priority Score (APS) within agents for universal prioritization logic.

**Transition Management:** Christine completed her transition planning documentation, capturing in-flight projects and proposed initiatives while ensuring continuity through her September 24th departure. Priority Accounts feature has always lacked staging data, and has to be tested on production. The competitor intent signal improvement plan, coordinated with Shuxin, addresses the current reliance on noisy intent topics rather than ALI-adjusted data.

### **Strategic Challenges**

The Copilot V1 deprecation extension to September 2026 creates unexpected technical debt, requiring the homepage and supporting infrastructure to remain operational for another year while V2 development proceeds.

Product hierarchy alignment revealed cross-functional coordination gaps, with Rowan discovering parallel efforts across Cam Fontin\'s data team, Nila\'s interaction code team, and Carlos\'s engineering org. While Robyn\'s proposal to leverage existing supply chain hierarchies for traditional industries provides a starting point, the lack of unified taxonomy threatens to fragment our account brief generation and competitive analysis capabilities. Immediate alignment meetings are needed to prevent duplicated effort.

MCP routing complexity emerged as Robyn\'s team dug into implementation details, with the seemingly straightforward advanced search and lookalike queries requiring sophisticated routing rules. Andrew\'s team identified that query patterns vary significantly based on context, necessitating more nuanced routing logic than initially scoped. This complexity directly impacts our Dreamforce demo timeline, though the top 100K queries will ship as planned.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Sri\'s realization that signal-based Workbooks represents a more central feature than previously understood reshapes our prioritization framework. The discovery that Scoops contains multiple sub-signals presents an immediate opportunity to improve perceived signal coverage simply through disaggregation, buying time for deeper signal integration work. This insight suggests we\'ve been undervaluing the psychological impact of signal quantity on user confidence.

The staging data reliability issue Christine uncovered extends beyond signals to Priority Accounts, forcing production testing that increases deployment risk. Victor Dubinsky\'s initiative to improve staging data consistency represents infrastructure investment, but the current state where multiple data sets lack reliable test environments creates unnecessary friction in our development velocity.

Robyn\'s discovery that current user data cannot support basic personalization experiences for Copilot reveals a fundamental gap in our data strategy. While Lookalike scoring shows 53-64% relative lift over buying groups in tech and pharma verticals, the inconsistent performance across other verticals points to the need for a hybrid LLM plus proprietary model approach rather than pure algorithmic solutions.

### **Cross-Team Dependencies**

Our collaboration with Brandon\'s team on product hierarchy requires immediate synchronization to prevent the fragmented approach Rowan identified. The AI/ML team\'s scraping capabilities combined with Brandon\'s team\'s domain expertise creates a powerful partnership, but without agreed-upon taxonomy by next week, we risk building incompatible systems that will require expensive reconciliation later.

The dependency on Shuxin\'s team for competitor intent signal improvements represents a longstanding coordination challenge---Christine noted these teams have never successfully aligned schedules to transition the competitor alert signal to ALI instead of classic intent.

## **Looking Ahead**

Next week\'s focus centers on finalizing the GSO to GTM Store connector design with Sri targeting Monday completion to unblock signal proliferation across Workbooks. This enables the critical disaggregation of compound signals like Scoops while establishing the pipeline for new signal types.

Robyn will deliver the product hierarchy proposal despite being out most of the week for holidays, recognizing this as the critical path item for preventing fragmented taxonomy development. The validation of SMB lookalike results proceeds in parallel, with metrics sampling coordinated through ZI sellers to ensure vertical coverage beyond tech and pharma strengths.

*Source: Team 1-2-3 Operating Framework entries from September 15-19, 2025*

## **Semantic Data Team Executive Roundup - September 19, 2025**

## **Executive Summary**

Jon discovered and fixed a critical bug causing 6x LLM overcalling in email processing, immediately reducing token costs from 20,000+ to expected ranges. With authentication PRs landing next week, the pipeline achieves production-ready cost attribution per tenant. Meanwhile, sales adoption of semantic data in workbooks drove Rowan to push for batch processing implementation---a strategic move that delivers 50% cost reduction while enabling ZoomInfo to expand historical data coverage from 6 months to 1 year for all prospects and customers.

## **This Week\'s Progress**

### **Key Momentum Areas**

Jon\'s cost optimization breakthrough emerged from a systematic test script processing 10,000 email threads with Inga, revealing not just accurate pricing but two core concurrency bugs in the ETL pipeline. The fragment handling bug alone was inflating costs by 600% through redundant LLM calls, now fixed with fast, accurate ingestion restored. This positions the team to deliver production-grade cost tracking within days.

Matt\'s Airflow implementation reached deployment readiness after performance validation confirmed suitability for expected tenant scale. The DAG architecture for incremental and backfill processing creates the foundation for automated data pipelines, with SBX deployment targeted for next week pending DevOps coordination on the dev environment setup.

Rowan\'s strategic pivot redirected Inga from G2 reviews to earnings call transcripts after analysis revealed reviews average under 100 words versus earnings calls\' 15-30 minutes of dense strategic content. This shift aligns perfectly with the pipeline\'s semantic compression strengths while addressing the 2,000-word account brief payloads currently overwhelming context windows in production.

### **Goals & Progress**

**Cost Infrastructure:** Jon achieved complete cost transparency for email and meeting processing through the test harness, fixing the 6x overcalling bug that was masking true operational costs. The three remaining authentication PRs will enable per-tenant cost attribution, completing the commercial viability requirements. With embeddings integration as the final piece, full pipeline cost tracking arrives next week.

**Orchestration Platform:** Matt progressed Airflow from architecture design through performance validation to DAG implementation in a single sprint. Following productive discussions with Danny on tenant scaling requirements, the team confirmed Airflow\'s capability to handle projected growth. The platform now awaits DevOps deployment to begin automating the currently manual ingestion workflows.

**Data Quality & Sources:** Inga completed thread processing calculations while developing ontology-based prompts for structured data extraction. The pivot from G2 reviews to earnings calls represents a 200x increase in processable content per record, directly addressing the semantic compression use case. Initial methodology for earnings call analysis launches immediately.

### **Strategic Challenges**

DevOps deployment delays for Airflow in dev environment risk pushing back automation timeline, though Matt\'s proactive escalation through Danny and potential direct engagement should resolve within days. The team needs clarity on deployment schedule to maintain momentum toward automated tenant onboarding at scale.

GTM store identifier complexity blocks Danny\'s progress on unifying multiple record IDs into single system-of-record entities. While requiring only an hour of focused analysis to resolve, this architectural decision impacts downstream data flow and needs immediate attention to prevent cascading delays.

Batch processing absence forces ZoomInfo to pay full price for semantic data processing even as sales teams dramatically increase usage through workbooks and workspaces. With initial tenant ingestion requiring 6+ months of historical data and ongoing processing accumulating rapidly, the 50% cost savings from batch mode transitions from nice-to-have to critical requirement.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The fragment handling bug discovery revealed how architectural assumptions about LLM calling patterns can exponentially inflate costs---Jon\'s fix dropping token usage from 20,000 to expected ranges proves the value of systematic cost analysis. This finding likely impacts other teams building LLM pipelines who may have similar multiplicative inefficiencies hiding in their code.

Earnings calls emerged as the optimal initial data source for semantic compression after Inga and Rowan\'s analysis showed G2 reviews\' sub-100 word format defeats the pipeline\'s purpose. The 200x content density difference validates focusing engineering effort on sources that actually require semantic compression rather than forcing all data types through the same pipeline.

Sales team adoption patterns from Henry and other executives querying their upcoming meetings revealed immediate product-market fit for semantic-powered meeting preparation. Rowan\'s demo showing calendar integration with historical interaction analysis proves the pipeline delivers tangible business value beyond theoretical capabilities---though privacy considerations around executive email access require careful governance.

### **Cross-Team Dependencies**

Our integration with DevOps for Airflow deployment requires escalation to maintain next week\'s automation timeline. Matt\'s coordination through semantic-dev DevOps channel, potentially with Rowan\'s support, aims to unlock the blocker preventing DAG deployment in development environment.

The authentication implementation crossing Jon\'s pipeline work with platform identity services reaches completion through three remaining PRs, enabling the critical capability to attribute costs per tenant rather than globally to ZoomInfo. This unlocks commercial viability for external customer billing through AI credits.

## **Looking Ahead**

Authentication completion next week transforms the pipeline from internal tool to commercial product, with per-tenant cost attribution enabling AI credit billing models. Jon\'s three PRs represent the final technical barrier to production readiness.

Batch processing implementation becomes the team\'s next major focus, offering 50% cost reduction while enabling expanded historical coverage from 6 to 12 months. With Danny and Jon\'s February groundwork plus Matt\'s Airflow orchestration, the technical path is clear---execution determines whether ZoomInfo can afford to scale semantic data across its customer base. Inga\'s earnings call methodology will prove the pipeline\'s value on high-density content while the team builds toward the Q4 target of automated multi-tenant operations at scale.

*Source: Team 1-2-3 Operating Framework entries from September 16-19, 2025*

## **MCP Team Roundup - September 19th, 2025**

## **Executive Summary**

The team successfully deployed lookup-first functionality with batching that significantly improves search performance, while establishing the foundation for MCP resource management despite discovering Claude Desktop\'s manual resource addition requirement. With Henry\'s meetings now flowing through the system and showing value for meeting prep, the platform is demonstrating tangible executive utility. The distributed system architecture challenge for stateful communication needs solving before November\'s gateway release but doesn\'t block October 14th deliverables.

## **This Week\'s Progress**

### **Key Momentum Areas**

Zheng completed the lookup-first search implementation with intelligent batching, reducing API calls and improving response times by processing multiple lookups simultaneously rather than sequentially. The system now validates all required attributes before executing searches, preventing errors and creating more reliable query execution.

Carter established MCP SDK integration and resource management infrastructure, successfully wiring tenant briefs into the ICP resources system despite discovering Claude Desktop\'s counterintuitive requirement for manual resource addition. This foundational work enables future prompt engineering and context management capabilities that will significantly improve user experience once the manual addition friction is resolved.

Henry\'s meetings and external participant data are now flowing through the platform after resolving the 100-record import limitation, enabling real-time meeting prep and company research capabilities. Rowan demonstrated pulling upcoming meetings with external participants and cross-referencing previous engagements, validating the executive use case for intelligent meeting preparation.

### **Goals & Progress**

**Search & Lookup Infrastructure:** Zheng\'s lookup-first implementation now handles batch processing with 5-record chunks, intelligently validating VP-level titles, tech industry classifications, and geographic filters before executing searches. The system maintains efficiency by constraining lookup result sizes while ensuring all necessary attribute mappings are available for downstream queries.

**MCP Resource Management:** The official MCP SDK is integrated and operational in local development, with tenant brief resources successfully exposed through the standard interface. Carter identified that while resources are available, Claude Desktop\'s design requires users to manually add them per session - a limitation shared across the developer community that we\'ll address through a complementary tool-based approach.

**Platform Data Flow:** Resolution of the GTM store configuration issue late Thursday restored normal data ingestion rates for users, meetings, and transcripts. The team identified and corrected the 100-record limitation that was constraining import jobs, with production data now flowing at expected volumes and Henry\'s executive instance serving as proof of concept.

### **Strategic Challenges**

The distributed system architecture presents a fundamental challenge for server-initiated communication patterns, as maintaining conversation state across multiple pods requires session affinity that our current infrastructure doesn\'t support. Zheng and Carter outlined that while current stateless tools work fine with distributed servers, any future functionality requiring server-side context awareness or user input elicitation will need architectural changes before we can scale to production durability standards.

Claude Desktop\'s manual resource addition requirement creates unexpected user friction that contradicts MCP specification expectations, forcing us to design around this limitation. The community-wide frustration with this design choice suggests potential future improvements, but we need to implement tool-based workarounds to ensure users can access grounding context without remembering manual steps each session.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The lookup-first pattern with batching proved significantly more efficient than error-driven lookup attempts, validating Topher\'s architectural recommendation and establishing a pattern for future tool implementations. This approach prevents wasted API calls and provides cleaner error handling by validating requirements upfront rather than recovering from failures.

Account brief payloads at 20,000 characters are exploding context windows across all orchestrators, revealing the critical need to decompose these into filterable sections. Rowan\'s analysis shows clear markdown sections within briefs that can become individual tool calls, enabling precise context retrieval without overwhelming token limits.

The distinction between account summaries (first-person interaction data) and account briefs (third-party public information) remains conceptually confusing across teams, indicating need for clearer terminology. This confusion impacts tool design and user expectations, suggesting we should align language with user mental models rather than internal data structures.

### **Cross-Team Dependencies**

Our collaboration with Frank on the SAP gateway design involves implementing his more secure approach to internal server exposure while maintaining the core tagging system concept. Zheng will focus next week on aligning our implementation with Frank\'s security requirements while ensuring the solution handles both stateless and future stateful scenarios.

The GTM store team\'s configuration fix restored expected data flow rates, but ongoing monitoring is needed to prevent similar throttling issues. We need clearer communication channels with the data infrastructure team to catch configuration issues before they impact downstream systems for multiple days.

## **Looking Ahead**

Next week centers on MCP gateway implementation to meet October 14th demo requirements, with Zheng working directly with Frank to implement the secure design while maintaining our tagging system approach. Rowan will conduct comprehensive end-to-end testing across multiple use cases to identify context optimization opportunities and develop prompt sequences for common user journeys.

The team will also implement tool-based workarounds for Claude Desktop\'s resource limitations and begin decomposing account briefs into manageable sections that prevent context window explosion. With Vinod returning Monday, we expect accelerated progress on distributed system architecture planning and state management solutions for the November gateway release timeline.

*Source: Team 1-2-3 Operating Framework entries from September 15-20, 2025*

## **Integrations Team Executive Roundup - Week of September 15, 2025**

## **Executive Summary**

Prateek Paikray delivered vertical dataset preview functionality for GTM Studio, now live in staging and ready for backend API integration next week - in addition, continued intensive Agentforce testing ahead of Dreamforce to mitigate Salesforce\'s weekly breaking changes to their platform APIs. Meanwhile, Sanyog Rai worked with Agentic/Copilot Workspace team to get Meeting information directly from GTM DM as the first consumer in addition to drafting requirements for auto-creating GTM Accounts from engagements in GTM DM. Andres Perez advanced the CRM Field Mapping Agent POC to reduce dependence on admin config.

## **This Week\'s Progress**

### **Key Momentum Areas**

Prateek Paikray completed the vertical dataset preview functionality for the internal marketplace, delivering a working solution using mock data that\'s now available in the GTMS staging org behind a feature flag. This achievement sets the stage for the GTM store team to integrate with backend APIs next week, moving the data marketplace closer to production readiness.

Sanyog Rai completed the requirements document for account creation through engagements, with Majed\'s review showing no issues. This foundational work opens the path for managing engagements from customers who provide engagement data but haven\'t connected their CRMs, expanding our platform\'s reach and utility.

The team discovered an unexpected win when Rowan\'s team began using the GTM data model for Copilot V2 and Workspace chatbot functionality without any prodding from the Integrations team. This validates the GTM data architecture and demonstrates organic adoption, with Upcoming meeting responses in Copilot Workspace now sourced from GTM engagements using GraphQL queries.

### **Goals & Progress**

**AgentForce Integration:** Prateek continues intensive testing with the engineering team, addressing functionality issues caused by Salesforce\'s weekly platform updates. Despite challenges with prompts that previously worked now giving random responses or invoking wrong APIs, the team remains on track for Dreamforce readiness with a new beta package deployed to the demo instance.

**GTM Studio & Solutions for ROI / Advanced Search:** Andres progressed on the auto-mapping agent POC, working with Lars to access the MCP server and building direct Salesforce calls to handle page layout limitations. Monday\'s rollout of Erica\'s recent releases via a new feature flag and entitlement will give all GTM Studio customers access to import rules, custom field creation, and field mapping on CRM connections, with the new feature flag ready for ROI and Advanced Search customers who have long-asked for support to swap CRM filter fields.

**Data Platform Enhancement:** The team addressed the GTM Contacts created from engagements issue, confirming they\'re currently only in Bigtable and not yet pushed to GTM tables in BigQuery. Maied is working on timeline clarification while the team continues building on the foundation that\'s attracting downstream adoption.

### **Strategic Challenges**

Agent Force entitlement checks cannot be performed using the new partner OAuth flow through the Developer Portal, requiring coordination with Adam and Vinod to identify a solution before the Dreamforce launch. This represents a platform-level constraint rather than a team execution issue, but needs resolution for broader customer access.

Calendar complexity for Outlook integration continues to exceed expectations, with Sanyog finding the processing more challenging than anticipated. However, the team has adopted a pragmatic approach: \"Take what we can and move forward, keep adding as things become available,\" allowing them to maintain momentum on recordings development using the stronger email foundation.

Legacy data architecture is creating cost challenges, with tenant data deletion operations costing \$20,000 per run due to historical raw sources that store every value change. The raw chorus table alone contains 3 petabytes of data, suggesting potential savings of \$5,000-\$10,000 by dropping unused legacy tables as customers migrate to GTM tables and APIs.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The Copilot Insights API became available on the new OAuth Enterprise API infrastructure in staging, with production release scheduled for September 22nd. This creates an integration opportunity with Agent Force for early October, potentially expanding the solution\'s data access capabilities just as it reaches broader market availability.

Communication gaps across teams emerged as a pattern, with team leadership knowledge not always reaching all team members. The discovery that some data platform team members were unaware of contact creation from GTM engagements highlights the need for broader information sharing, while assumptions about integration inclusion in onboarding launch buttons created unnecessary friction.

The organic adoption of GTM data model by Rowan and Lars\' team represents validation of the platform architecture and demonstrates that well-designed systems can drive usage without active promotion. This first downstream customer success using GraphQL for GTM store access provides a golden demonstration opportunity for other products.

### **Cross-Team Dependencies**

Our collaboration with the GTM store team on dataset preview functionality continues to be essential for marketplace completion. With UI work finished by Prateek, next week\'s focus shifts to backend API integration once they\'re enabled, requiring close coordination to ensure seamless functionality transition.

Workbook team coordination remains necessary as they continue using deprecated GTM fields for core functionality. The team successfully navigated recent changes through testing with Sunita, confirming that lookup functionality works correctly with the proper field implementations while maintaining backward compatibility during the transition.

## **Looking Ahead**

Next week centers on Agent Force readiness and expanding testing access, with Prateek creating sandbox users for SC testing while resolving package issues on the demo org with Salesforce\'s team.

Andres targets completing the end-to-end auto-mapping agent demo, stringing together the nine required endpoints to showcase reduced GTM admin overhead. Sanyog advances recordings development by leveraging the completed email foundation while continuing parallel work on Outlook calendar integration. The team will also explore the new Context AI Service APIs, requiring 2-3 weeks to understand responses and integrate with existing LWC components, positioning for subsequent version enhancements that could significantly expand agent capabilities.

With Monday\'s GTM Studio release enabling import rules across Salesforce, HubSpot, and upcoming Dynamics support, the team is well-positioned to demonstrate compound value across multiple product lines while maintaining the momentum that\'s already attracting organic adoption from other teams.

*Source: Team 1-2-3 Operating Framework entries from September 15-19, 2025*

## **ZIM Team Executive Roundup - Week of September 15, 2025**

## **Executive Summary**

Person-level intent production deployment now delivers 180 million daily signals to ZoomInfo through Brett Elliot\'s infrastructure work, while Path Factory partnership resolution enables continued field marketing lead generation. Forrester Wave demo script preparation progresses with comprehensive responses completed as the team advances toward flywheel data partner self-serve deployment through PLG workflow integration. September domain release deployed successfully while October MCR preparation begins for AI Page Rank and conversions features.

## **This Week\'s Progress**

### **Key Momentum Areas**

Brett Elliot completed person-level intent deployment delivering 180 million daily signals to ZoomInfo with monitoring and alerting infrastructure in place. The Clickagy system processes individual-level intent data enabling enhanced targeting capabilities while hedge fund POC deliveries continue flowing through Bobsled with Citadel confirmation still pending.

Matt Barnes resolved Path Factory identification issues through API configuration adjustments accounting for Zscaler IP shifting, achieving partner satisfaction and enabling continued marketing team lead generation. The September MCR domains release deployed successfully with necessary hot fixes addressed, positioning Inferno team attention toward AI Page Rank and conversions projects for October release.

Aadhitthyaa Hari Gopal delivered agent demonstration recordings for both websites and intent capabilities, receiving feedback from Dominik and Ryan for iterative improvements. The self-serve flywheel data partners PRD progresses with Tuesday review scheduled including PLG team and ads infrastructure coordination.

### **Goals & Progress**

**Infrastructure Development:** Matt Barnes completed website identity data pipeline development with successful coordination through Andres Perez and Sanyog Rai for data store mapping. The website identity API PRD revisions near completion requiring stakeholder and engineering review, while cross-organizational website visitor journey signal requirements clarification scheduled for Wednesday with Sneh\'s team.

**Agent Platform Advancement:** Jesse Miller progressed ZIM agent development through backend-for-frontend endpoint creation and SendGrid email template completion with four templates ready for Vulcan team implementation. Agent UI ticket preparation for Michael Kelly prioritization enables production testing environment setup while forecasting UI GA feedback from Carlos requires one treatment adjustment.

**Partnership Ecosystem:** Anwar Mai completed Forrester Wave draft responses with comprehensive coverage across team capabilities while coordinating flywheel data partner ELT follow-up and PLG team integration. Path Factory data taxonomy submission enables Snowflake ingestion planning while Kaspera partnership introduction advances contract review and pixel testing phases.

### **Strategic Challenges**

Matt Barnes manages potential resource constraints as Inferno team attention shifts toward AI Page Rank and conversions projects for October MCR while maintaining website identity data pipeline delivery timelines. The cross-organizational website visitor journey signal requirements need clarification from Sneh\'s team to prevent delays in Q4 high-profile signal delivery.

Jesse Miller identifies RampID mapping process modifications needed following Brett Elliot\'s guidance on keeping specific data within ZoomInfo infrastructure while sending only anonymous RampIDs to Clickagy systems. This affects DMP API development dependencies and requires COIN team coordination for FBR pipeline rebuild to maintain legal compliance.

Aadhitthyaa Hari Gopal coordinates prepay automation discovery requiring better understanding of current SFDC to SAP to Boomi flow processes before building automation solutions. The September 22nd bot elimination deployment requires conversion data backfill and reprocessing coordination with Zai for data quality maintenance.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Anwar Mai\'s coordination revealed that flywheel data partner self-serve deployment will follow the websites PLG validation workflow, enabling partner classification and data sharing validation while preventing company cannibalization. The approach includes self-attestation for privacy compliance and quarterly scanning through Pravado at \$50K annual cost for unlimited partner monitoring.

Matt Barnes discovered two primary options for streaming data to GTM Store through either API Upsert or the Chorus pipeline actively streaming data to Store. This architectural finding enables flexible data delivery approaches while the GTM Store team determines optimal mechanisms for websites identification data integration.

Brett Elliot identified that Sovrn bidding infrastructure lacks RampID decoding capabilities, requiring LiveRamp and Sovrn coordination to enable envelope decoding and RampID delivery in bid streams. This technical gap affects contact targeting optimization requiring both code modification and infrastructure enhancement for improved bidding performance.

### **Cross-Team Dependencies**

Our work with Sneh\'s team on website visitor journey signals requires requirements clarification following the Wednesday cross-organizational walkthrough that identified gaps in specifications. Matt Barnes coordinates with stakeholders to prevent Q4 signal delivery delays while ensuring proper data asset delivery to designated platforms.

Partnership development with Path Factory advances through data taxonomy submission enabling Snowflake ingestion coordination with Lynda while considering Upsert API alternative for streamlined GTM Datastore integration. This approach eliminates custom development requirements while leveraging existing infrastructure capabilities.

Forrester Wave preparation requires continued coordination across sales, customer experience, product, and engineering teams for revenue marketing evaluation positioning. The demo script development following standardized analyst questioning format ensures comprehensive platform capability representation.

## **Looking Ahead**

Next week focuses on Forrester demo script completion and October release preparation, with the team positioned to advance flywheel partner deployment and maintain production platform excellence.

Anwar Mai leads Forrester demo script development for revenue marketing evaluation while coordinating website visitor journey signal requirements with Sneh and Tanvi. Jesse Miller advances ZIM agent production testing through Michael Kelly UI ticket prioritization while coordinating COIN team FBR pipeline rebuild discussions. Aadhitthyaa Hari Gopal progresses GTM Config schema documentation for ZDP team review while initiating prepay automation discovery and conversion data backfill coordination.

Matt Barnes focuses on website identity data NRT pipeline advancement toward end-of-September GTM Store delivery while managing AI Page Rank and conversions project preparation for October MCR. Brett Elliot continues hedge fund POC delivery confirmation while coordinating LiveRamp and Sovrn technical resolution for RampID bidding enhancement. Shuxin Yang advances ZIM UX priority analysis and intent vendor partner evaluation following data science team alignment.

The team maintains steady execution momentum with production deployments advancing and partnership frameworks developing to support platform expansion and competitive positioning in the revenue marketing evaluation.

*Source: Team 1-2-3 Operating Framework entries from September 15, 2025*

## **Product BI Team Executive Roundup - September 19, 2025**

## **Executive Summary**

Copilot Workspace (V2) launched to 100+ internal GTM users this week with external customer rollout planned for early October. AJ Belan and Phoebe Mei identified a P0 instrumentation bug blocking user ID capture in Amplitude, which engineering is actively resolving. The team has strong momentum on renewal predictions, API usage analysis, and partnership metrics while navigating expected data architecture challenges with Coors integrations.

## **This Week\'s Progress**

### **Key Momentum Areas**

AJ Belan finalized renewal prediction scoring analysis with Phoebe Mei ahead of the October 18th ELT meeting, establishing a foundation for account health reporting that can be efficiently updated as new data becomes available. This positions leadership with data-driven insights for strategic account discussions.

Phoebe Mei delivered comprehensive Workspace adoption tracking implementation, identifying event tracking gaps and working directly with engineering to resolve the user ID instrumentation issue. Her proactive debugging ensures the team will have clean analytics once the external rollout begins in October.

Nanxi Ge successfully aligned all stakeholders on request prioritization without pushback, including partnerships with Albert, Xuxian, and pending Ali alignment. This strategic coordination enables the team to focus resources on high-impact initiatives like API usage analysis and partnership network development.

### **Goals & Progress**

**Copilot Workspace Analytics:** Phoebe Mei implemented tracking infrastructure for the internal rollout to 100+ GTM users, with expansion planned next week and external customer access starting early October. The P0 user ID bug is actively being resolved with engineering support, clearing the path for comprehensive adoption and engagement analysis.

**Account Health & Renewals:** AJ Belan completed renewal prediction score analysis supporting the October 18th ELT presentation, with streamlined update processes established for future iterations. The analysis identifies large C and D tier accounts requiring attention, providing actionable insights for account management.

**Integration & API Analytics:** Ferrell Tanuwidjaja and Eran Dayan are building unified data sources combining frontend and backend workspace data while advancing API usage analysis. The team discovered valuable insights about GTM table consolidation requirements and semantic layer development for more accurate business logic representation.

### **Strategic Challenges**

Coors integration historical data remains difficult to access due to the product\'s separate data architecture from acquisition, with accuracy concerns between settings and import tables. Nanxi Ge is working with data engineering to leverage CDP import tables as the most reliable source, though this requires complex multi-table joins for comprehensive analysis.

Amplitude event archiving capabilities are unclear despite admin access, with Ferrell awaiting support resolution on whether certain event types can be properly archived. This impacts cleanup efforts but doesn\'t block current workspace tracking implementation.

The Israel team will have limited availability next week (only Thursday-Friday) due to Rosh Hashanah, which may affect integration metrics development timeline but has been factored into project planning.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Partnership network initiative revealed an interesting contribution model where the company exchanges site visitor intelligence with partners for enhanced customer targeting. This creates a data-rich environment for measuring partner value through visitor quality, conversion rates, and mutual referral effectiveness, though data won\'t be available until mid-to-late October.

API usage analysis uncovered previously unexplored data sources that could provide deeper insights into product utilization patterns. This discovery positions the team to deliver more comprehensive usage analytics than initially scoped, potentially revealing optimization opportunities across the platform.

Workspace rollout feedback collection through enablement forms shows limited initial volume (only 3 entries) but establishes qualitative feedback infrastructure to complement quantitative Amplitude data. This dual approach will provide richer user experience insights as adoption scales.

### **Cross-Team Dependencies**

Our work with engineering on the Workspace P0 instrumentation bug is moving efficiently, with Phoebe Mei actively participating in resolution threads. The quick engineering response demonstrates strong collaboration for launch-related analytics needs.

Data engineering coordination with Linda on new CDP table structures will require combining multiple object tables (accounts, users, opportunities) rather than unified views. While not ideal architecturally, this approach is understood and planned for in upcoming integration analysis work.

## **Looking Ahead**

Next week focuses on scaling Workspace analytics capabilities as internal rollout expands and external customer access begins, with particular emphasis on early adoption patterns and user experience insights.

Phoebe Mei will continue analyzing early Workspace adoption once the user ID issue resolves, enabling detailed AE and AEM usage path analysis with drop-off identification. Ferrell will join the tracking implementation effort with full tool access configured. Meanwhile, Nanxi Ge begins two-week API usage data exploration while maintaining chatbot development momentum with Jack through weekly or bi-weekly sync establishment.

The team is well-positioned to provide comprehensive Workspace launch analytics, deliver actionable renewal insights to ELT, and advance partnership measurement strategy development as data becomes available in Q4.

*Source: Team 1-2-3 Operating Framework entries from September 15-19, 2025*

## **Product Operations Team Executive Roundup - September 15, 2025**

## **Executive Summary**

The Product Operations team achieved a significant breakthrough this week by establishing a clear pathway for microapps deployment through the connection between semantic data backend and ZI Chat, eliminating months of deployment challenges that have hindered our AI tool rollout. Sam Darcy successfully coordinated with William\'s team to implement MCP connections, while Kristin Gandini secured October roadmap commitment from Jack\'s ZI Chatbot team for LaunchDarkly integration. These infrastructure wins position us to accelerate deployment of the Voice of Customer tool, Knowledge Center agents, and other agentic applications without the networking complications that have slowed progress.

## **This Week\'s Progress**

### **Key Momentum Areas**

Sam Darcy broke through a major deployment bottleneck by establishing MCP connections between the semantic data backend and ZI Chat, creating a foundation for all future AI application deployments. This microapps approach solves persistent deployment errors and networking issues that have delayed several initiatives, particularly the VoC tool that has been stalled due to infrastructure challenges.

Kristin Gandini secured concrete timeline commitment from the ZI Chatbot team, with Jack adding LaunchDarkly integration to October roadmap (potentially earlier). This removes uncertainty around the Release Impact tool for Customer Experience teams, providing them visibility into which features affect specific customers and enabling better support delivery.

Daniel Kong pivoted effectively from EverAfter discussions to focus on the foundational challenge of product knowledge freshness, beginning development of agents that will automatically update and prune outdated information. His insight that knowledge bases fail because we \"layer things on top without taking anything out\" directly addresses longstanding Knowledge Center accuracy issues.

### **Goals & Progress**

**AI Tool Infrastructure:** Sam Darcy completed the critical semantic data to ZI Chat connection, establishing microapps as the deployment standard for all future agentic tools. This infrastructure foundation eliminates the deployment hassles that have plagued multiple initiatives and provides a clear path forward for VoC, Knowledge Graph applications, and other AI tools currently in development.

**Early Access Program:** Caleb Munson successfully engaged with all PMs except one regarding October release Early Access participation, though discovered concerning low engagement rates below 10% of eligible tickets. His systematic approach to understanding PM objections revealed that incentive systems favor quick launches over gathering feedback, requiring strategic intervention to improve program effectiveness.

**GTM Personalization:** Ken Elwell and Brett Jacobs advanced the Copilot talk track to a solid foundation, though work remains dependent on Henry\'s industry group presentation scheduled for next Thursday. The team learned valuable lessons about building flexibility into AI agents, as use cases consistently evolve beyond initial specifications, requiring more adaptable prompt engineering approaches.

**Release Operations:** Kristin Gandini conducted an MCR refresher session for PMs that addressed confusion points around the process, while continuing to formalize off-cycle release procedures and beta best practices. Her work on automating release coordination reduces PM burden and ensures more consistent execution across product teams.

### **Strategic Challenges**

The Early Access program faces systemic engagement challenges that go beyond individual PM preference, with current participation rates suggesting fundamental misalignment between program goals and team incentives. Caleb\'s discovery that PMs prioritize launch deadlines over feedback cycles indicates we may need leadership reinforcement to change behavior, as the current \"available to PMs\" positioning lacks the urgency needed for meaningful adoption.

Knowledge base accuracy remains a persistent challenge across multiple initiatives, with Daniel\'s insight highlighting our tendency to add new information without systematically removing outdated content. This pattern creates confusion for both internal teams and AI agents trying to provide accurate information, requiring process changes around knowledge lifecycle management rather than just better content creation.

Google Slides functionality continues to block GTM team adoption of personalization tools, with William\'s team improvements still pending and no clear delivery timeline. This dependency particularly affects Account Managers who require slide generation capabilities for their workflow, limiting the practical impact of otherwise ready personalization features.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Brett Jacobs identified a fundamental challenge in AI agent design: we consistently underestimate use case flexibility, building agents for specific workflows that users then adapt in unexpected ways. The Copilot talk track agent, originally designed for standard presentations, gets used differently across discovery calls, demos, and various meeting types, highlighting the need for more adaptable agent architecture that balances structure with user customization.

Daniel Kong\'s work revealed that successful knowledge bases require equal focus on content removal and addition, with automatic pruning becoming as important as fresh content ingestion. This insight challenges our current approach of continuously layering new information and suggests we need sophisticated content lifecycle management to maintain accuracy over time.

The team discovered that microapps represent more than just a deployment solution but a fundamental shift in how we build and scale AI tools. Sam\'s success connecting semantic data to ZI Chat creates opportunities for rapid prototyping and deployment that could accelerate our entire product development cycle.

### **Cross-Team Dependencies**

Our work with William\'s ZI Chat team on microapps infrastructure continues to be essential for resolving deployment challenges across multiple initiatives. The MCP connection Sam established provides immediate relief, though continued collaboration will be needed to fully optimize the platform for our use cases and ensure stability as we scale AI tool deployment.

Jack\'s ZI Chatbot team commitment to October LaunchDarkly integration represents crucial progress for Customer Experience tool requirements, though success depends on DevOps team coordination for accessing LaunchDarkly data feeds. Kristin\'s proactive communication with the CX brain trust has set appropriate expectations for end-of-month delivery.

## **Looking Ahead**

Next week focuses on capitalizing on infrastructure breakthroughs to accelerate AI tool deployment while addressing engagement challenges in our release processes.

Sam will implement the first microapps using the new ZI Chat connection, starting with the VoC tool that can finally move beyond deployment obstacles. Ken and Daniel will align on knowledge graph architecture, using the Copilot FAQ as a proof of concept for automated content management. Kristin will map user workflows and data requirements to prepare for the LaunchDarkly integration while continuing MCR process improvements. Caleb will shift from identification to activation, working to boost Early Access engagement through both PM education and potential leadership reinforcement of program importance. The team will also finalize Brett\'s Copilot talk track and demo agent in preparation for GTM team training sessions.

These combined efforts position us to demonstrate significant progress on customer-facing AI tools while building the operational foundation for sustainable AI product development across the organization.

*Source: Team 1-2-3 Operating Framework entries from September 15, 2025*
