---
id: synthesis-2025-37-2025
title: "Product Executive Intelligence Brief - September 12, 2025"
type: synthesis-report
status: approved
created: 2025-09-12
updated: 2026-01-06
week_ending: 2025-09-12
reporting_period: "September 8-12, 2025"
tags: ["weekly-report", "synthesis", "Q32025"]
---

# **Product Executive Intelligence Brief - September 8-12, 2025**

*Synthesized from 14 team reports: DAI Executive, Data Executive, GTM Studio, Context Engineering, Core Data, GTM Data Platform, Integrations, MCP, Product BI, Product Ops, Semantic Data, ZIM, Automation, Login/Provisioning*

*For detailed questions about any item below, reference specific team reports or contact team leads directly.*

## **Executive Summary**

### **Update on Previous Week Blockers**

**Technical infrastructure performance degradation threatening customer experience:** Context Engineering team resolved APS-V2 production issues with complete rollback to S2A points algorithm, while Semantic Data team addressed the 93% ETL processing speed degradation through database performance fixes - both critical systems are now stable and operational.

**Resource allocation constraints blocking unified profile delivery:** DAI Team confirms Unified Profile delivery remains delayed with engineering resources still allocated to Studio pipeline work, though AI credit pricing system achieved dev-ready status and is now in 4-week sprint to production.

### **Current Week Update**

**Blockers:**

- **Critical privacy compliance issue threatening Canadian contact product:** Core Data Team reports \"John Durst flagged a critical privacy compliance issue with Canadian contacts that warrants attention - legal is requesting EU-like notification requirements that would severely limit or effectively shut down our Canadian contact product affecting 4+ million contacts.\"

- **Cross-functional coordination complexity consuming disproportionate development resources:** DAI Team identifies \"systematic challenges in aligning legal, security, and engineering stakeholders around data initiatives consuming disproportionate time relative to the technical complexity of the work itself, creating bottlenecks that could impact multiple product timelines.\"

**Momentum areas:**

- **Major AI infrastructure breakthroughs demonstrating production readiness:** Context Engineering achieved \"Contact Recommender scaled to support 50x peak traffic with P99 latency dropping from 4 seconds to 1 second, now expanding to 100,000+ users weekly via ReachOut\" while MCP Team \"successfully demonstrated Claude\'s win analysis capabilities to executive leadership, showcasing 10-layer deep semantic data queries that generated comprehensive deal insights.\"

- **Revenue-driving vertical datasets achieving market validation:** Data Executive Team secured \"preliminary legal approval for a blanket contributory network notice covering present and future product activities\" while \"Igor Kyrylenko completed the franchisor dataset in final Snowflake format with full traceability, positioning the team to deliver a unique vertical dataset that sales can immediately leverage with enterprise accounts.\"

**Bottom line:** AI infrastructure is demonstrating transformational capability improvements and production scale, with revenue opportunities converting from proof-of-concept to customer deployment, but systematic coordination challenges and compliance issues require immediate executive intervention to prevent bottlenecks from constraining Q4 growth potential.

### **GTM Studio**

**GTM Studio Team:** \"Defensive Q4 motion established with 100-customer target for GTM Studio renewals. Following last week\'s executive leadership offsite, Sneh has aligned the team on a defensive strategy focused on objection handling against competitors like Clay to protect at-risk renewals. Workbooks advanced with Jagannath integrating question-answering capabilities and Salesforce fallback mechanisms while Tanvi completed AI credit design iterations, though backend process confirmation remains pending amid cross-team coordination challenges. Plays achieved stakeholder alignment as Mohan finalized Copilot activation designs and secured DeltaX ownership transition while Neha progressed Double-O integration strategy documentation. ROI Analytics faces a production issue with Arun discovering users and managers hierarchy that broke after a year of stable operation, requiring platform team investigation before GA readiness. Data Management advanced with Ash and Corina laying out detailed 2025-2026 milestones and generating early prototype on data health scan to drive upsell, though job posting data quality issues highlighted the need for earlier data validation processes. GTM Config achieved alignment as Tingting facilitated coordination between Victor\'s and Rowan\'s teams, clarifying that context service dependencies won\'t block the GTM Config roadmap.\"

### **GTM Copilot V2**

No specific Copilot V2 team report was provided in this week\'s submissions.

### **GTM AI Context Service**

**Context Engineering Team:** \"APS-V2 experienced critical production issues affecting multiple tenants, forcing a complete rollback to S2A points algorithm while the team implements fixes with data science. Despite this setback, the team delivered significant wins: Contact Recommender scaled to support 50x peak traffic with P99 latency dropping from 4 seconds to 1 second, now expanding to 100,000+ users weekly via ReachOut. AFS (Account Fit Score) is on track for October release in Zim with personalized tenant-specific scoring.\"

**Semantic Data Team:** \"Jon Seller delivered a breakthrough in cost accounting infrastructure, enabling precise forecasting of tenant onboarding costs before pipeline execution - transforming our ability to make data-driven pricing and capacity decisions. The team achieved critical milestones in pipeline efficiency with 4 major concurrency improvements merged and a clear path to 32x batch processing optimization. However, the Airflow integration hit a Python version compatibility issue (3.11 vs 3.12) that Matt Kowalczyk is actively resolving, while data access dependencies continue to impact evaluation workflows.\"

**MCP Team:** \"The MCP team successfully demonstrated Claude\'s win analysis capabilities to executive leadership, showcasing 10-layer deep semantic data queries that generated comprehensive deal insights---a critical validation of our AI context layer strategy.\"

### **Vertical Datasets**

From the Data Executive Roundup: \"Igor Kyrylenko completed the franchisor dataset in final Snowflake format with full traceability, positioning the team to deliver a unique vertical dataset that sales can immediately leverage with enterprise accounts. The dataset includes successful ZoomInfo company and person record matching, providing immediate value for enterprise accounts seeking visibility into franchise ownership structures. Brandon Tucker successfully delivering franchise samples to March Networks and building a reusable foundation for future customer requests.\"

### **Data**

**Data Executive Team:** \"Rob Priore secured preliminary legal approval for a blanket contributory network notice covering present and future product activities, eliminating the need for individual approvals on each new CN-driven product like benchmarking and recommendations. This breakthrough will accelerate development cycles for new customer-facing tools while maintaining compliance. Additionally, Igor Kyrylenko completed the franchisor dataset in final Snowflake format with full traceability, positioning the team to deliver a unique vertical dataset that sales can immediately leverage with enterprise accounts.\"

**Core Data Team:** \"John Durst flagged a critical privacy compliance issue with Canadian contacts that warrants attention - legal is requesting EU-like notification requirements that would severely limit or effectively shut down our Canadian contact product affecting 4+ million contacts. Meanwhile, Hayden Cowell successfully connected the Data tools and Polaris teams for review room integration, establishing a clear API path that will enable systematic data quality improvements through research validation. The team discussed and agreed to follow-up on reviewing opportunities to automate review room processes given in some cases we have 2+ years of annotated gold standard data that can be used to train models and could free up significant researcher capacity.The Contributory Network team advanced from POC to production-ready scope on two AI agents following CPO demo - Deal Cycle Insights and Org Chart agents that will integrate into Copilot V2 to deliver sales intelligence and organizational mapping using cross-tenant network data, while also deploying a CN Data Advisor for internal testing to streamline data compliance and implementation guidance.\"

### **Platform**

**GTM Data Platform Team:** \"The Data Platform team has achieved a significant milestone with the release of the GraphQL Query API, which is already being tested by agentic platforms using MCP. Marc Delurgio has expanded the data access spec to include Suppression Lists, now 50% complete with the additional requirements. The team is actively preparing for next week\'s DaaS leads meeting while investigating newly discovered RingLead usage in the match api of deprecated fields that will require attention.\"

**Integrations Team:** \"Sanyog successfully completed email ingestion into GTM DM for all tenants (Gmail+Outlook) and calendar data now on GTM DM for 1000 tenants (Google only, Outlook incoming). Prateek advanced multiple strategic AI initiatives, completing Agentforce enablement documentation and progressing vertical datasets marketplace development while coordinating cross-functional solutions for multi-currency support and partner app publishing workflows.\"

**Automation Team:** \"MCP infrastructure shortcuts create technical debt while API versioning scope expansion delays V2 timeline into Q1-Q2. Adam Peretz revealed that the current MCP implementation used API gateway shortcuts to accelerate launch, requiring migration to a dedicated MCP gateway before other teams can publish tools. Meanwhile, API V2 scope has expanded beyond initial estimates with more breaking changes identified, pushing realistic timelines into Q1-Q2 rather than earlier projections. Marc Frail completed comprehensive H2 planning infrastructure while Sam Massie finalized conditional logic requirements but identified field mapping complexity requiring phased delivery approaches.\"

**ZIM Team:** \"Transformational breakthrough in account brief generation achieving 25x efficiency improvement while contact targeting campaigns achieve production deployment with live bidding and impressions. Team delivered 92% goal completion rate with strategic Forrester Wave preparation positioning ZoomInfo as #2 in revenue marketing category behind 6sense. Flywheel data partner self-serve framework established for October launch, enabling exponential cookie pool growth and intent data expansion through partner ecosystem deployment.\"

**Login/Provisioning Team:** This week, the Login and Provisioning team made significant progress on critical projects for the upcoming Copilot V2 release on October 6th. Key deliverables were unblocked, enabling the design and development of the Copilot V2 login experience. Brannen Huske also began building a roadmap for AI Action Credits to support the Copilot V2 launch and other AI monetization models.

### **Operations**

**Product BI Team:** \"Phoebe\'s team successfully secured the August renewal prediction score data today after delays from Tony\'s team, enabling critical ELT meeting preparation. Meanwhile, Nanxi has established a strategic partnership with Enterprise Manager Michael to jointly identify churn and renewal patterns, transforming a simple data request into ongoing collaboration. With Copilot V2 launching October 6th and six new Workbook features rolling out, the team is rapidly scaling analytics infrastructure while managing multiple product launches simultaneously.\"

**Product Ops Team:** \"Caleb Munson successfully achieved sign-off on H2 T2 project milestones for both GTM Studio and Copilot, getting approval from all DAIs after discovering significant misalignment that posed material risk to current plans. This breakthrough week also saw the Product Dossier concept move from idea to working prototype with Kristin Gandini completing a full Advanced Search example, while Sam Darcy overcame months of deployment challenges by securing internal tools environment access through Guy\'s support. The team identified organizational gaps where multiple teams solve similar problems using outdated product information, creating an opportunity for Product Ops to establish itself as the central source of truth.\"

*For deeper analysis on any topic above, reference specific team reports or contact team leads directly.*

*Methodology: Analysis of team 1-2-3 Operating Framework reports, prioritizing: (1) Executive decisions needed, (2) Cross-team blockers, (3) Strategic momentum areas, (4) Strategic alignment gaps*

# **📊 Appendix**

### **Individual Team Reports**

**DAI Executive Team Weekly Report - September 8-12, 2025**

## **Executive Summary**

The team delivered significant progress on partnership strategy with Adobe and Outreach while maintaining strong momentum across data initiatives, but coordination challenges are emerging as we scale multiple AI products simultaneously. Adobe discussions advanced to concrete reselling proposals with potential ZIM integration synergies, while Outreach alignment cleared marketing messaging blockers for their broader launch. However, cross-functional coordination gaps - particularly around legal, security, and engineering alignment on data initiatives - are consuming disproportionate time relative to technical complexity and require immediate attention to prevent development paralysis.

## **This Week\'s Progress**

### **Key Momentum Areas**

Partnership Strategy Gains Traction: Ali Sadat successfully advanced discussions with Adobe, securing a concrete reselling proposal and identifying technical delivery pathways through collaboration with sales and product teams. The Adobe partnership now presents dual opportunities - both platform integration and potential ZIM synergies that weren\'t initially proposed but could drive significant revenue impact.

Franchise Dataset Production Reset Accelerates Delivery: Brandon Tucker completed a comprehensive reset of the franchise dataset production process, establishing new team structures, validation protocols, and order of operations that immediately improved output quality. The team now has a reusable sample covering 20 diverse franchisors and is positioned to complete samples for the top 50 franchisors, with clear plans to leverage Solutions Consultants and Data Services teams for scaled execution.

AI Credits Implementation Maintains September Timeline: Despite ongoing technical discussions, Sneh Kakileti confirmed that AI credits implementation remains on track for end-of-September delivery with little buffer. The team successfully aligned sales leadership and enablement teams on GTM Studio readiness timelines, establishing dedicated Solution Consultant environments for demos and clearing the path for paid proof-of-concept motions.

### **Goals & Progress**

Partnership Development: Ali Sadat achieved 80% completion on Adobe and Outreach partnerships this week. Adobe discussions progressed to commercial negotiations involving sales and partner teams, with clear technical delivery paths identified through Product. Outreach alignment was successfully completed, resolving marketing messaging conflicts that had blocked their broader launch capabilities. The focus shifts to operationalizing ISV partnership processes with Andres to handle the expected influx of partnership opportunities.

Vertical Data Acceleration: Brandon Tucker made substantial progress with 50% goal completion, establishing a complete reset on franchise dataset processes that immediately improved quality and speed. The team successfully transferred work streams to new teams for acceleration, completed a three-hour intensive session, and established clear pathways to leverage Solutions Consultants and Data Services for scaled support. GTM.AI launch preparations are advancing with significant remaining work on existing dataset content.

GTM Studio Sales Readiness: Sneh Kakileti successfully aligned with sales leadership and enablement teams on field readiness timelines and plans, establishing clear coordination with Antuna and AR\'s teams. The team configured dedicated Solution Consultant environments for GTM Studio demos and established clear talk track and demo paths for the Solution Consultant team. September release preparations are on track for production deployment on 9/23, with paid proof-of-concept motions being developed.

### **Strategic Challenges**

Cross-Functional Coordination Complexity: The team\'s work on data ingestion, website key buyer ID requirements, and partnership integration processes reveals systematic challenges in aligning legal, security, and engineering stakeholders around data initiatives. These coordination gaps are consuming disproportionate time relative to the technical complexity of the work itself, creating bottlenecks that could impact multiple product timelines. Brandon Tucker\'s experience with flywheel partner opportunities demonstrates the need for streamlined processes that don\'t overwhelm smaller partners with extensive security and legal requirements.

Multi-Product Positioning Clarity Needs: AJ Belen identified that sales leaders are requesting unified platform narratives that encompass not just AI products like Copilot V2, GTM Studio, and GTM Context Service, but also existing solutions like Ringlead, Chorus, and ZIM. The team needs practical sales motion guidance that clarifies when to lead with which products for specific customer scenarios, personas, and lifecycle stages. This positioning challenge reflects the broader complexity of managing multiple product launches simultaneously while maintaining clear market messaging.

Engineering Resource Allocation Questions: Multiple team members highlighted resource constraints and coordination challenges across engineering teams. Dominik Facher noted that advanced search migration work is creating resource allocation questions about whether to invest in current systems or defer until retirement, while teams need immediate architectural decisions to prevent feature development paralysis. The query layer confusion mentioned by Dominik specifically around federated search capabilities requires clarification to avoid repeated setbacks.

*Source: DAI Executives Operating Framework entries from September 8, 2025 - September 12, 2025*

**Data Executive Team Weekly Report - September 8-11, 2025**

## **Executive Summary**

Rob Priore secured preliminary legal approval for a blanket contributory network notice covering present and future product activities, eliminating the need for individual approvals on each new CN-driven product like benchmarking and recommendations. This breakthrough will accelerate development cycles for new customer-facing tools while maintaining compliance. Additionally, Igor Kyrylenko completed the franchisor dataset in final Snowflake format with full traceability, positioning the team to deliver a unique vertical dataset that sales can immediately leverage with enterprise accounts.

## **This Week\'s Progress**

### **Key Momentum Areas**

Igor successfully finalized the franchisor dataset with complete lineage tracking to raw data sources across all four tables (franchisor, franchisee, location, contact), enabling sales teams to offer a unique vertical dataset that competitors lack in structured format. The dataset includes successful ZoomInfo company and person record matching, providing immediate value for enterprise accounts seeking visibility into franchise ownership structures.

Rob\'s legal breakthrough establishes a framework for using eligible customer data to develop and test new contributory network products without individual approvals. This streamlined compliance approach will enable faster iteration on benchmarking tools, agent development, and other data-driven innovations while maintaining transparency with customers through comprehensive disclosure.

Dana completed productive deep-dive sessions with the India team on company data infusion processes, significantly improving the team\'s capability to independently manage DIP infusions. This knowledge transfer positions the team to accelerate company additions across priority geographies, with EMEA data currently in staging awaiting final engineering sign-off.

### **Goals & Progress**

Franchise Data Productization: Igor completed the franchisor dataset in production-ready Snowflake format with full traceability from raw source to final tables, achieving 95% of weekly goals. The dataset now supports immediate sales demonstrations and customer samples, with Brandon Tucker successfully delivering franchise samples to March Networks and building a reusable foundation for future customer requests.

Compliance Infrastructure: Rob achieved 100% completion on establishing the simplified data sharing compliance flow, securing preliminary legal approval for blanket contributory network notices. This eliminates previous bottlenecks requiring individual legal review for each new product iteration, while also implementing automated customer compliance monitoring through the Privado tool for CIPA violations.

Data Infrastructure & Quality: Steve identified and began addressing email generation model issues affecting domains with asynchronous bouncing patterns, working with DataPure to implement solutions that should improve overall email deliverability. Dana progressed company data infusion capabilities with successful deep-dive training sessions, positioning the team for accelerated geographic expansion.

### **Strategic Challenges**

Email generation model reliability continues to present challenges, with Steve identifying that 10% of domains show false positive delivery rates due to asynchronous bouncing. While a path forward exists through vendor collaboration and domain filtering, this affects training data quality and requires coordination between data science and vendor teams to implement comprehensive solutions.

Brandon Tucker\'s franchise data development faces scaling challenges as customer demand significantly exceeds initial expectations. Multiple enterprise accounts are requesting immediate samples, creating a bottleneck between high market interest and data processing capacity. The team needs enhanced solution consultant support and potentially automated sampling capabilities to match demand velocity.

Company 3.0 planning requires additional coordination time to ensure proper milestone definition and resource allocation. Ethan Young noted the need for intensive planning sessions to balance quarterly improvements with longer-term architectural changes, particularly around location relationships and employment structures for franchise entities.

*Source: Data Executive Operating Framework entries from September 8th, 2025 - September 11th, 2025*

**GTM Studio Team Weekly Report - September 8-12, 2025**

## **Executive Summary**

Defensive Q4 motion established with 100-customer target for GTM Studio renewals. Following last week\'s executive leadership offsite, Sneh has aligned the team on a defensive strategy focused on objection handling against competitors like Clay to protect at-risk renewals. Workbooks advanced with Jagannath integrating question-answering capabilities and Salesforce fallback mechanisms while Tanvi completed AI credit design iterations, though backend process confirmation remains pending amid cross-team coordination challenges. Plays achieved stakeholder alignment as Mohan finalized Copilot activation designs and secured DeltaX ownership transition while Neha progressed Double-O integration strategy documentation. ROI Analytics faces a production issue with Arun discovering users and managers hierarchy that broke after a year of stable operation, requiring platform team investigation before GA readiness. Data Management advanced with Ash and Corina laying out detailed 2025-2026 milestones and generating early prototype on data health scan to drive upsell, though job posting data quality issues highlighted the need for earlier data validation processes. GTM Config achieved alignment as Tingting facilitated coordination between Victor\'s and Rowan\'s teams, clarifying that context service dependencies won\'t block the GTM Config roadmap.

## **This Week\'s Progress**

### **Key Momentum Areas**

September Launch War Room Delivering Results: Ash led intensive QA sessions this week that identified and resolved multiple P0 blockers for CRM and Snowflake integrations, moving the team closer to production readiness. Job posting functionality pushed to production under feature flag despite data quality challenges around timeout issues and taxonomy normalization.

Agent Experience Capabilities Advancing: Jagannath\'s team integrated the ability to ask questions about workbook data and implemented Salesforce fallback mechanisms when GTM data model gaps occur. QA team onboarded this week to expand testing coverage beyond engineering, with plans to bring in internal users next week for broader feedback.

Multi-Team Alignment on GTM Configure Achieved: Tingting successfully facilitated alignment between Victor\'s team and Rowan\'s team, clarifying that GTM context service won\'t be a milestone dependency for GTM Config. This removes a major coordination blocker and enables clearer roadmap planning moving forward.

### **Goals & Progress**

Workbooks: Jagannath delivered significant agent experience enhancements with the ability to ask questions about workbook data now operational, though some bugs remain under investigation. His team implemented a critical Salesforce fallback mechanism that activates when GTM data model gaps occur, providing redundancy for production reliability. QA team onboarded successfully this week and identified additional issues beyond engineering testing, with internal user feedback sessions planned for next week. Tanvi focused on AI action credit flow finalization, completing design iterations to address backend processing requirements, but continues waiting for confirmation on final backend processes due to ongoing cross-team discussions creating requirement changes.

Plays: Mohan achieved breakthrough stakeholder alignment on Copilot activation experience and requirements, enabling the engineering review kickoff planned for Monday. Early access customer feedback from SurveyMonkey, Newfold, and Spektic validated the straightforward workbook-to-target-list activation path, though customers need clarity on seller actions within Copilot. DeltaX migration testing initiated in production with early validation results available, and ownership transition to Anwar\'s team secured for Q4 handoff. Neha progressed on Double-O platform capability assessment, connecting with Karthik\'s engineering team to understand architecture while supporting their ZoomInfo and GTM Studio learning curve.

ROI Analytics: Arun\'s workstream faces a production issue with User Management System functionality that worked reliably for an entire year broke in the past two weeks, creating customer noise and ROI Beta sentiment decline as this is a key feature for Enterprise scale customers to understand team by team and user by user analytics understanding. Platform team investigation is underway. Multi-currency support approach discussion happened between Brahm, Arun, Andres and Prateek - Platform team will make currency available in GTM DM (already validated), but the conversion piece will be owned by CFA team (service/API identification TBD) as there isn\'t any other team identified for that use case, and will be low on priority for the Platform. Studio Workbook ROI requirements captured as prototype with data discovery progressing to support analytics integration.

Data Management: Ash and Corina made substantial progress establishing the foundation for 2025-2026 execution plan. Detailed milestones aligned with CS team leadership including Mary, Megan, Bishop, and Vinny\'s team, plus sales alignment with Ben and Matt. Analytics generated early data health scan views for customer subsets, preparing to scale across all targeted customers. Job posting functionality reached production under feature flag despite P0 blockers around timeout issues with \'contains\' operators and data quality challenges requiring taxonomy normalization. Ash collected valuable feedback from Brandon on resolution screen interactivity.

GTM Config: Tingting facilitated crucial alignment between Victor\'s sales team and Rowan\'s Context Service API team, clarifying interdependencies and scope boundaries. Key discovery emerged that GTM context service won\'t be a milestone within GTM Config roadmap, allowing Rowan to progress separately without blocking GTM Config development. Backend prototyping discussions initiated with Carlos as tech lead to begin front-end development alongside design progression.

*Source: Team 1-2-3 Operating Framework entries from September 8-12, 2025*

**Context Engineering Team Weekly Report - September 8-12, 2025**

## **Executive Summary**

APS-V2 experienced critical production issues affecting multiple tenants, forcing a complete rollback to S2A points algorithm while the team implements fixes with data science. Despite this setback, the team delivered significant wins: Contact Recommender scaled to support 50x peak traffic with P99 latency dropping from 4 seconds to 1 second, now expanding to 100,000+ users weekly via ReachOut. AFS (Account Fit Score) is on track for October release in Zim with personalized tenant-specific scoring.

## **This Week\'s Progress**

### **Key Momentum Areas**

Contact Recommender achieved breakthrough performance improvements, with Robyn\'s team opening traffic gates to support 50x our highest historical peak while simultaneously reducing P99 latency from 4 seconds to 1 second. The system is now at 10% deployment on ReachOut and will reach 100% shortly, impacting over 100,000 users weekly and fundamentally changing our ability to deliver real-time recommendations at scale.

AFS (Account Fit Score) secured its October release slot in Zim as V1, with Robyn aligning the algorithm roadmap to deliver personalized, tenant-specific scoring that advances beyond the flat-table lookalikes approach. The UX improvements enabling multi-company selection will significantly enhance user experience while the personalized scoring brings customers closer to their true ICP definition.

Sri completed the signal-to-GTM store schema definition ahead of schedule, establishing the technical foundation for unified signal distribution across all ZoomInfo products. This architectural work unblocks multiple downstream initiatives and positions us to centralize signal intelligence in Q4.

### **Goals & Progress**

Algorithm Alignment & Rollout: Robyn successfully aligned the October algorithm releases. AFS will deploy to ZIM first with Copilot integration following, while lookalikes targets early October for the top 100K companies. The product hierarchy investigation continues with advanced search integration discussions scheduled for next week.

Infrastructure & Performance: The Contact Recommender infrastructure overhaul exceeded expectations, now handling production traffic at 50x capacity with 75% latency reduction. Christine\'s work on APS-V2, while requiring rollback due to calculation issues, revealed critical insights about our dual implementation challenge between data science\'s Kafka-based scoring and S2A\'s real-time rendering requirements.

GTM Store Integration: Sri achieved 100% completion on the schema definition for pushing signals to GTM store, finishing earlier than anticipated. The remaining challenge centers on securing DAP team capacity for building the GSO-to-GTM store connector, with prioritization decisions pending across multiple stakeholder teams.

### **Strategic Challenges**

The APS-V2 rollback exposed a fundamental architectural challenge in our scoring infrastructure where data science\'s Kafka-based implementation (30-60 minute latency) must stay synchronized with S2A\'s real-time calculation for homepage rendering. Christine identified that fixes must be implemented in both places simultaneously, and we lack proper A/B testing infrastructure to validate improvements before full rollout. The team is exploring on-the-fly homepage building to eliminate the synchronization requirement.

Copilot V2\'s backend migration from S2A Engine to Workbooks creates uncertainty around signal prioritization capabilities. Robyn and Christine discovered that without S2A points integration or APS API prioritization, Copilot V2 appears limited to hard filtering on Insights rather than intelligent ranking. This architectural disconnect requires immediate clarification with Sean\'s team to ensure we\'re not losing critical prioritization functionality in the migration.

Resource constraints on the DAP team threaten the GTM store signal integration timeline, with multiple non-signal projects competing for the same engineering capacity. Sri has prepared a comprehensive project list with effort estimates for Brandon, Jody, and leadership to prioritize, but without clear commitment, our Q4 signal centralization goals remain at risk.

*Source: Team 1-2-3 Operating Framework entries from September 8-12, 2025*

**Core Data Team Weekly Report - September 8-12, 2025**

## **Executive Summary**

John Durst flagged a critical privacy compliance issue with Canadian contacts that warrants attention - legal is requesting EU-like notification requirements that would severely limit or effectively shut down our Canadian contact product affecting 4+ million contacts. Meanwhile, Hayden Cowell successfully connected the Data tools and Polaris teams for review room integration, establishing a clear API path that will enable systematic data quality improvements through research validation. The team discussed and agreed to follow-up on reviewing opportunities to automate review room processes given in some cases we have 2+ years of annotated gold standard data that can be used to train models and could free up significant researcher capacity. The Contributory Network team advanced from POC to production-ready scope on two AI agents following CPO demo - Deal Cycle Insights and Org Chart agents that will integrate into Copilot V2 to deliver sales intelligence and organizational mapping using cross-tenant network data, while also deploying a CN Data Advisor for internal testing to streamline data compliance and implementation guidance.

## **This Week\'s Progress**

### **Key Momentum Areas**

Peter Overman improved coordination with the Data Pipelines Israel team through implementing weekly standups and consistent communication channels, resolving friction around status updates and decision-making delays. During testing of the predict leads pipeline, Peter discovered we get approximately 90,000 unmatched URLs per day that yield an estimated \~8,000 company profiles---a potential stream of +2.5MM net new companies annually.

Hayden Cowell achieved a breakthrough on the review room integration by discovering the self-service review room was originally built for accuracy testing, making it perfectly suited for the Polaris use case. The system already has an API that doesn\'t update production data, allowing the Polaris team to submit tasks and check for updates seamlessly. This unlocks the ability to have researchers validate phone number changes systematically, ensuring new values are correct before production updates.

Magnus Herweyer made critical progress on shared services by documenting PRs for the first four services and establishing the product team with Joe Solis, Gabriel from PTI, and Case. More importantly, Magnus uncovered significant email safety gaps beyond basic deliverability - the team has been neglecting spam traps, honeypots, and other dangerous email patterns that can harm customer sender reputation and damage our platform credibility.

The Contributory Network (CN) team achieved significant progress on AI agent development with two major initiatives moving forward. Following a successful POC demo at the CPO\'s AI standup last week, the team locked down scope for two production agents in partnership with Adam/Lars/Rowan\'s team. The Deal Cycle Insights Agent will provide sales cycle timing and process intelligence through a new Copilot Chat button, delivering key insights on sales cycle spectrum, stage-by-stage analysis, and seasonal buying patterns by leveraging cross-tenant network data and pre-computed company similarity cohorts. Meanwhile, the Org Chart Agent will display organizational structure and decision maker hierarchy for target companies by combining GAL (Microsoft) and Google Directory data with legacy org chart systems as fallback. Both agents have established working streams for data preparation and artifact design.

### **Goals & Progress**

Transparency API Development: John Durst got the first tickets into grooming with the team planning to start building immediately. The engineering team already has a POC for transparency data, with Kristen reaching out proactively about the implementation. The phased approach will start with person data where traceability exists, then expand to company data once Company 3.0 provides sufficient trace information.

MAID and HEMs Integration: Rituparna Das completed analysis showing significant coverage improvements - 29 million individuals without MAID will receive MAID associations, while 24 million with existing MAID will get additional coverage. The implementation will take 2.5-3 sprints to complete, with expected improvements to visitor resolution percentages once deployed.

Review Room Automation Discovery: Peter Overman and Hayden Cowell identified that researchers have been annotating data for 2+ years through review rooms for scoops and news classification, creating fully-built gold standard datasets. With modern LLMs understanding context better, the team believes they can achieve 99.9% accuracy in classification, potentially freeing up dozens of researchers currently doing manual QA work.

CN Data Advisor Internal Testing: The team deployed a CN Data Advisor ZI Chat Agent for internal use, currently in testing within the data team. The agent assists with data source status inquiries (\"Is CN ingesting Slack data?\"), legal compliance questions (\"What are the legal requirements for CN email data?\"), use case guidance, and implementation requirements. This internal tool addresses common questions about CN data ingestion, customer eligibility, and required notifications, streamlining internal support processes.

AI Agent Partnership Development: Following CPO approval, the CN team established two agent specifications with clear data requirements and implementation strategies. The Deal Cycle Insights Agent requires company opportunity data (Account_ID, Amount, stages, timing) combined with cross-tenant network intelligence, while the Org Chart Agent leverages manager relationship data from multiple directory sources. Both agents are designed to integrate seamlessly into Copilot V2 with transparent confidence scoring and fallback data handling.

### **Strategic Challenges**

John Durst escalated a critical privacy compliance issue where legal is requesting Canadian contacts follow EU-style notification requirements. With 4+ million Canadian contacts and existing notification bandwidth constraints preventing publication of millions of EU contacts, implementing this would mean shutting down the Canadian contact product entirely. John is pushing back with legal but may need Brandon\'s sign-off if they insist on proceeding, as this would severely damage the business despite potential legal compliance benefits.

The team discovered significant email safety issues beyond deliverability metrics. Magnus Herweyer, working with email expert Kevin H, identified that the platform currently publishes dangerous emails including spam traps, honeypots, and blacklisted domains that can harm customer sender reputation. Never Bounce was underfunded for 6 years after acquisition, and the team is now developing a comprehensive risk scoring model from 0-100 with full traceability to explain why emails are flagged as risky.

Review room automation remains blocked by prioritization decisions despite clear ROI. While Cam Fortin noted that using review rooms to feed models should be a default workflow rather than project-specific, John Durst pointed out that previous automation attempts showed mixed results - some processes were successfully automated while others remained more cost-effective with human review. The team needs executive alignment on whether to prioritize engineering resources for automation that could save \$50,000+ annually per process.

*Source: Core Data Team Operating Framework entries from September 8-12, 2025*

**GTM Data Platform Team Weekly Report - September 8, 2025**

## **Executive Summary**

The Data Platform team has achieved a significant milestone with the release of the GraphQL Query API, which is already being tested by agentic platforms using MCP. Marc Delurgio has expanded the data access spec to include Suppression Lists, now 50% complete with the additional requirements. The team is actively preparing for next week\'s DaaS leads meeting while investigating newly discovered RingLead usage in the match api of deprecated fields that will require attention.

## **This Week\'s Progress**

### **Key Momentum Areas**

Linda Johannessen delivered the GraphQL Query API release, creating a stable, agent-ready interface for cross-entity GTM data that has generated strong early validation with agentic platforms already testing MCP integration. This represents a foundational shift from just building tools to creating systems that both humans and AI agents can leverage effectively.

Adwait Kirtikar successfully aligned the DaaS team around platform integration, publishing a comprehensive document that outlines current business state, lessons learned, and roadmap alignment. The DaaS team has expressed enthusiasm for working with the platform product team to integrate their workflow, setting up productive collaboration moving forward.

Menna Rashwan defined initial high-level milestones for Enterprise Search v2 (Federated Search) to support CDC integration, metadata-driven indexing, and real-time updates. This work directly enables the technical foundation needed for advanced search capabilities across the platform ecosystem.

### **Goals & Progress**

Data Access & Governance: Marc Delurgio expanded the original scope to include Suppression Lists and other data access rules, achieving 50% completion including the additional requirements. The team is preparing stakeholder reviews to finalize documentation and move toward implementation.

Platform Integration: Linda Johannessen refined schema and data definitions through comprehensive syncs with Customer Data Catalog, Workbook, and DaaS teams, confirming coverage across marketplace and app scenarios. The work has been organized into executable JIRA stories with a clear path to API readiness by the October 15 target date, with stakeholders reinforcing a \"do it right, not fast\" approach prioritizing metadata-first architecture.

Legacy System Migration: Moshik Levin reviewed engine release consequences with Company leads and PMs, discovering that RingLead is also using deprecated fields. A larger meeting with DaaS leads is scheduled for next week to address these dependencies and plan migration paths.

### **Strategic Challenges**

The technical solutioning for Enterprise Search v2 continues to evolve as teams work through architectural decisions, with Menna Rashwan noting that detailed milestones and sequencing remain in flux. The Search team will need to take ownership of their GraphQL implementation once federated search integration is in place, requiring careful coordination between multiple engineering teams.

RingLead\'s usage of deprecated fields presents an additional complexity for the engine release timeline, as Moshik Levin discovered this dependency during consequence reviews. The team will need to investigate the extent of this usage and develop appropriate migration strategies alongside the planned DaaS transition work.

*Source: Team 1-2-3 Operating Framework entries from September 8, 2025*

**Integrations Team Weekly Report - September 8, 2025**

## **Executive Summary**

Sanyog successfully completed email ingestion into GTM DM for all tenants (Gmail+Outlook) and calendar data now on GTM DM for 1000 tenants (Google only, Outlook incoming). Prateek advanced multiple strategic AI initiatives, completing Agentforce enablement documentation and progressing vertical datasets marketplace development while coordinating cross-functional solutions for multi-currency support and partner app publishing workflows.

## **This Week\'s Progress**

### **Key Momentum Areas**

The team made important discoveries about email data processing that will improve customer value delivery. Sanyog identified that engagement-generated GTM contacts and accounts will help capture significantly more email volume for tenants without CRM connections, addressing a data gap that has been causing customer confusion about low email counts (Chorus only ever persisted emails when a CRM was connected, unless the email was sent from ZI Copilot or Engage).

Sanyog delivered the long-awaited email and calendar data processing rollout, successfully onboarding all Google/Outlook tenants to receive email engagement data in GTM Data Model. This infrastructure achievement enables downstream teams to leverage email and calendar engagement data for customer workflows via the new GraphQL endpoint, representing a foundational capability that multiple product teams have been waiting for.

Prateek completed the Agentforce integration enablement document and coordinated with creative marketing for demo video production at the Waltham office. His systematic approach to cross-functional collaboration advanced multiple H2 priorities simultaneously, from AI context layer marketing to vertical datasets API requirements gathering with the ZDP engineering team.

### **Goals & Progress**

Data Processing Infrastructure: Sanyog successfully enabled email and calendar data processing for all Google tenants and email for 1000 Outlook tenants, with only Outlook calendar integration pending final edge case testing. The rollout proceeded gradually with 500 tenants at a time to monitor for scaling issues, demonstrating careful operational management. This foundational work allows downstream application teams to access engagement data in GTM Data Model.

AI Integration & Marketplace: Prateek completed the Agentforce enablement documentation and submitted the app listing for Salesforce review. The team coordinated with Ben Davis from partner marketing and Ryan O\'Connor for demo video creation, positioning the integration for broader market announcement. Work on vertical datasets progressed through requirements refinement with Workbook and GTM Store teams for metadata API development.

Strategic Platform Development: Prateek partnered with the CFA team to identify multi-currency support solutions and discussed roadmap integration for Agentforce with ROI data capabilities. His collaboration with the Dev Portal team advanced the end-to-end experience for partner-registered apps publishing to both internal and external marketplaces, supporting the broader partner ecosystem strategy.

### **Strategic Challenges**

API development timelines for vertical datasets face potential delays due to Israeli holidays in late September and early October, which may impact the October 15 delivery target. The ZDP engineering team\'s confidence in delivering interface APIs provides some mitigation, but the compressed timeline requires careful monitoring and potentially adjusted expectations.

Multi-currency support requirements emerged through customer feedback, necessitating short-term solutions while longer-term platform service integration is planned. This pattern of customer requirements outpacing platform capabilities highlights the need for more proactive requirements gathering in the sales and onboarding process.

The team discovered complexity in building unified MCP (Model Control Protocol) solutions that balance vendor-specific limitations with seamless user experience. While the 2026 roadmap includes comprehensive solutions, near-term workarounds require careful architecture decisions to avoid technical debt.

*Source: Team 1-2-3 Operating Framework entries from September 8-12, 2025*

**MCP Team Weekly Report - September 8-12, 2025**

## **Executive Summary**

The MCP team successfully demonstrated Claude\'s win analysis capabilities to executive leadership, showcasing 10-layer deep semantic data queries that generated comprehensive deal insights---a critical validation of our AI context layer strategy.

## **This Week\'s Progress**

### **Key Momentum Areas**

Topher Dennis completed GraphQL migration for product reviews, financial filings, and engagement tools, establishing the foundation for real-time meeting intelligence within our AI agents. The engagement tools now support sophisticated filtering by user, meeting topic, and timeframe---enabling the \"prepare for my next meeting\" use case that sales has been requesting for Q4.

Carter Vanhuss advanced the transition to ICP\'s official SDK, which will reduce onboarding friction from 2 weeks to 2 days for new developers while automatically inheriting protocol updates. This architectural shift positions us to rapidly scale MAP server integrations across the organization without maintaining custom implementations.

### **Goals & Progress**

GraphQL Tool Migration: Topher completed 3 of 5 remaining tool migrations this week, with engagement tools now fully operational pending test data availability. Launch Darkly feature flagging integration remains in progress for selective tool exposure based on customer tier.

MAP Server Architecture: Carter\'s SDK transition is 60% complete, with resources section functionality enabling static data queries for user briefs and tenant information. The discovery of predefined prompt capabilities opens new possibilities for structured workflows like win analysis templates.

GenAI Prompt Optimization: Zheng encountered sequencing issues where the system bypasses lookup calls, impacting data accuracy. Batch enrich card development was delayed due to illness but remains targeted for next week\'s sprint.

### **Strategic Challenges**

The GTM Graph QL team\'s staging environment contains zero users with meeting data, forcing Topher to test in production with a single user added at 8pm last night. This data vacuum blocks comprehensive testing of engagement tools and could delay the Q4 sales enablement feature launch if not resolved by early next week.

Zheng\'s prompt sequencing challenge reveals a deeper architectural issue: our GenAI layer doesn\'t enforce tool calling order, causing inefficient API consumption and potentially inaccurate results. Root cause analysis points to missing orchestration logic in the prompt framework that needs engineering intervention.

The resources versus tools architectural decision for company ID fetching remains unresolved between Carter and Zheng. Since company ID requirements are entirely context-dependent, placing this in static resources may create performance bottlenecks for dynamic use cases.

*Source: Team 1-2-3 Operating Framework entries from September 8-12, 2025*

**Product BI Team Weekly Report - September 12, 2025**

## **Executive Summary**

Phoebe\'s team successfully secured the August renewal prediction score data today after delays from Tony\'s team, enabling critical ELT meeting preparation. Meanwhile, Nanxi has established a strategic partnership with Enterprise Manager Michael to jointly identify churn and renewal patterns, transforming a simple data request into ongoing collaboration. With Copilot V2 launching October 6th and six new Workbook features rolling out, the team is rapidly scaling analytics infrastructure while managing multiple product launches simultaneously.

## **This Week\'s Progress**

### **Key Momentum Areas**

Nanxi turned a routine enterprise manager request into a strategic partnership opportunity, discovering shared goals around churn prediction and creating a collaborative framework where both teams provide complementary insights - the enterprise team conducting customer interviews while analytics provides data-driven patterns.

Phoebe\'s team advanced critical launch preparations by establishing unified data tracking across Copilot V1 and V2, ensuring seamless user journey analysis and enabling questions about whether V1 chat users are engaging with V2 features through a single source table approach.

The team overcame technical infrastructure challenges as Ferrell connected with the CDP team to manage the deprecation of two key integration import tables, proactively scheduling table swaps to prevent disruption to current dashboards and analytics capabilities.

### **Goals & Progress**

Renewal Prediction Analytics: Phoebe completed initial analysis of August renewal prediction scores after receiving delayed data from Tony\'s team, with insights expected by end of day to support ELT meeting preparation. The team confirmed this delay pattern will likely recur monthly, establishing second-week expectations for future reporting cycles.

Product Launch Analytics: Preparation for six new Workbook features and Copilot V2 is advancing through structured weekly meetings with product managers Sean and Inbal, where requirements translate into engineering tickets under launch epics. Internal user enablement begins next week with 100-200 users, growing to full internal deployment by end of September.

Integration Data Infrastructure: Nanxi\'s team addressed integration data reliability questions from Mark Harris, confirming strong accuracy for import data and partial coverage for export data, with some vendor types still missing from export tables. The team clarified that current import tracking covers only advanced sync, not org import customers.

### **Strategic Challenges**

Tal\'s unresponsiveness to multiple requests from Phoebe, Wagun, and Dipti regarding semantic layer reviews is creating bottlenecks in chatbot development work. Despite reporting to Nir and having no visible PTO status, Tal hasn\'t responded to urgent review requests, potentially indicating shifted priorities or resource constraints that may require management intervention.

Hiring momentum remains slower than anticipated due to recruiter-side delays, with Nanxi\'s expected interview schedule pushed to next week after originally planning significant time allocation this week. While screening continues, the delayed timeline may impact team scaling plans and workload distribution.

Technical infrastructure transitions require careful coordination as both CI playground and existing import tables face deprecation, necessitating proactive migration planning to maintain analytics capabilities while supporting ongoing business operations and reporting requirements.

*Source: Team 1-2-3 Operating Framework entries from September 12, 2025*

**Product Ops Team Weekly Report - September 8-12, 2025**

## **Executive Summary**

Caleb Munson successfully achieved sign-off on H2 T2 project milestones for both GTM Studio and Copilot, getting approval from all DAIs after discovering significant misalignment that posed material risk to current plans. This breakthrough week also saw the Product Dossier concept move from idea to working prototype with Kristin Gandini completing a full Advanced Search example, while Sam Darcy overcame months of deployment challenges by securing internal tools environment access through Guy\'s support. The team identified organizational gaps where multiple teams solve similar problems using outdated product information, creating an opportunity for Product Ops to establish itself as the central source of truth.

## **This Week\'s Progress**

### **Key Momentum Areas**

Caleb delivered the H2 T2 milestone alignment that had been blocking progress for weeks, achieving 90% completion by getting GTM Studio and Copilot milestones approved and shared across all DAI teams. The process revealed substantial misalignment between teams and identified material risk in current execution plans, making this alignment work invaluable for preventing larger downstream issues.

Kristin transformed the Product Knowledge Base from concept to reality by creating a V1 Product Dossier template and building a complete example for Advanced Search using real support questions and existing documentation. This tangible prototype provides the foundation for scaling product knowledge capture without waiting for hackathon outcomes, though it positions well for complementary development if hackathon progresses.

Sam achieved a major breakthrough on VoC deployment by securing access to the internal tools environment through Guy\'s partnership, complete with GitHub repository and CI/CD pipeline setup. This resolved months of deployment obstacles and enabled progress on both the core VoC application and a new metadata-based search agent that will provide broader account impact analysis beyond the current top 15-20 result format.

### **Goals & Progress**

H2 T2 Initiative Alignment: Caleb successfully obtained DAI sign-off on customer-facing milestones for GTM Studio and Copilot, revealing significant team misalignment that required resolution. The remaining work focuses on mapping dependencies so platform teams understand their specific requirements and timelines, plus determining optimal distribution channels for broad organizational communication.

Product Knowledge Systems: Kristin completed the V1 Product Dossier template with a full Advanced Search implementation, using real support data and existing documentation to create a human-readable knowledge capture system. The template provides clear structure for scaling across additional product areas, with next steps focused on update system design and broader implementation strategy.

Customer Onboarding Enhancement: Daniel connected with the Ada team and identified EverAfter as a promising solution for low-touch customer onboarding, moving beyond Ada\'s reactive question-answer model toward proactive step-by-step guidance. His discovery work revealed EverAfter\'s kit-based project management approach offers opportunities to integrate product source of truth content with automated customer journey tracking.

### **Strategic Challenges**

Sam\'s VoC progress now depends on Guy for all code approvals and deployment issue resolution, creating a bottleneck that slows iteration cycles despite finally having a deployment path. While this dependency isn\'t ideal, it represents the best available solution for moving forward and Guy has been responsive to support needs.

Ken identified process gaps around off-cycle releases where enablement teams don\'t systematically evaluate whether small releases warrant off-cycle treatment, leading to last-minute decisions on communication timing. A small blocker on GTM Studio release timing exemplifies this challenge, though resolution is expected by end of day and overall September MCR materials are complete.

Daniel discovered organizational coordination issues where multiple teams independently solve similar problems using potentially outdated product information rather than current source of truth materials. While these teams often make good progress, their work could be more effective with access to automated, up-to-date product knowledge, creating an opportunity for Product Ops to provide value through better integration.

*Source: Product Ops Team 1-2-3 Operating Framework entries from September 8-12, 2025*

**Semantic Data Team Weekly Report - September 8-12, 2025**

## **Executive Summary**

Jon Seller delivered a breakthrough in cost accounting infrastructure, enabling precise forecasting of tenant onboarding costs before pipeline execution - transforming our ability to make data-driven pricing and capacity decisions. The team achieved critical milestones in pipeline efficiency with 4 major concurrency improvements merged and a clear path to 32x batch processing optimization. However, the Airflow integration hit a Python version compatibility issue (3.11 vs 3.12) that Matt Kowalczyk is actively resolving, while data access dependencies continue to impact evaluation workflows.

## **This Week\'s Progress**

### **Key Momentum Areas**

Jon Seller\'s cost accounting framework represents a fundamental shift in operational visibility - we can now predict token usage and costs for any tenant before onboarding, with accurate tracking showing 27,000 embedding requests processed successfully on Wednesday. This capability directly enables sales conversations with concrete cost-per-tenant metrics and prevents budget surprises during large-scale onboarding initiatives.

The concurrency improvements Jon deployed through 4 major PRs are already showing results in production, with the system successfully handling batch requests at 32x load during staging tests. Danny Pan confirmed performance metrics remain strong even under this increased load, validating our architectural approach to scaling.

Rowan Bailey\'s work on tenant brief generation identified a critical optimization opportunity - the team discovered they were using Gemini Flash 2.0 instead of 2.5, potentially leaving significant cost savings and quality improvements on the table. The shift to batch processing will reduce API calls from 27,000 individual requests to approximately 844 batched calls.

### **Goals & Progress**

Pipeline Infrastructure: Matt Kowalczyk successfully ported the application to Python 3.11 with minimal changes - only 2 files required type definition updates and all dependencies remained compatible. The Airflow integration is progressing despite the version mismatch, with a clear path forward that maintains security compliance while enabling workflow orchestration.

Cost Optimization: Jon Seller completed the full cost accounting implementation, delivering capabilities for tenant-level cost tracking, date-range analysis, and pre-onboarding estimates. The system now provides token counts for embeddings and full cost visibility across all pipeline runs, with accurate accounting replacing previous \"eyeballing\" approaches.

Data Enrichment: Inga Isakov and Jon evaluated product review processing workflows while navigating G2 data access challenges. Danny Pan secured commitment from the ingestion team that ZDB tables will be available by end of day, unblocking the product reviews filter functionality that\'s been stalled.

### **Strategic Challenges**

The Python version incompatibility between Airflow (3.11) and our application (3.12) requires either backporting our code or finding alternative deployment strategies. Matt identified the risk of security concerns from DevOps about downgrading versions, though initial testing shows all current packages are compatible with 3.11. The team needs to decide between backporting, containerization, or accepting version differences.

G2 data accessibility remains blocked due to GraphQL ID requirements with no discovery mechanism. While the ingestion team committed to creating the necessary tables in ZDB by today, Inga\'s evaluation work has been delayed for multiple days. This impacts our ability to incorporate product review signals into enrichment pipelines.

Budget constraints for Anthropic API usage are forcing immediate decisions about rate limits and token allocations. Danny Pan is working with finance to establish three tiers of usage - current needs, scaling requirements, and steady-state operations - but the complexity of backfill versus ongoing processing makes accurate forecasting challenging.

*Source: Team 1-2-3 Operating Framework entries from September 8-12, 2025*

**ZIM Team Weekly Report - September 8, 2025**

## **Executive Summary**

Transformational breakthrough in account brief generation achieving 25x efficiency improvement while contact targeting campaigns achieve production deployment with live bidding and impressions. Team delivered 92% goal completion rate with strategic Forrester Wave preparation positioning ZoomInfo as #2 in revenue marketing category behind 6sense. Flywheel data partner self-serve framework established for October launch, enabling exponential cookie pool growth and intent data expansion through partner ecosystem deployment.

## **This Week\'s Progress**

### **Key Momentum Areas**

Account Brief AI Revolution: Aadhitthyaa Hari Gopal achieved 100% completion on account brief pipeline redesign, delivering 25x efficiency improvement over previous custom-built models. New pipeline generates millions of daily briefs using off-the-shelf LLMs while maintaining quality standards, positioning Copilot for enhanced customer intelligence delivery at scale.

Contact Targeting Production Success: Brett Elliot completed comprehensive contact targeting deployment with live campaigns achieving bidding success and impression delivery in production environment. Privacy cluster VRS integration advancement positions enhanced visitor resolution capabilities for Firefox/Safari users, while hedge fund POC deliveries flow through Bobsled with Citadel confirmation pending.

ZIM Agent Development Acceleration: Jesse Miller progressed agent capabilities to 80% completion with backend-for-frontend endpoint identification and SendGrid access resolution. Email template development framework established while forecasting UI preparation advances toward Tuesday GA release with comprehensive rollout coordination.

Forrester Wave Strategic Positioning: Anwar Mai initiated comprehensive demo script development with cross-functional team coordination across sales, customer experience, product, and engineering teams. Strategic positioning as #2 revenue marketing platform (behind 6sense) validates 3-year market entry success and competitive differentiation.

### **Goals & Progress**

Infrastructure Architecture Excellence: Matt Barnes achieved exceptional completion on website identity data pipeline development with comprehensive mapping session coordination through Andres Perez and Sanyog Rai. Adobe Analytics UX design completed in 1.5 days while Path Factory API investigation reveals 96% resolution success despite 17% overlap claims.

Intent Platform Optimization: Shuxin Yang achieved 60% completion on intent roadmap synchronization with front-end team coordination and ZIM UX feedback analysis. Platform and app initiative alignment progressing with GTM Config integration planning and amplitude event analysis for priority development.

Partnership Ecosystem Development: Anwar Mai coordinated flywheel data partner self-serve framework development with legal and security mitigation planning. TypeForm relationship advancement and Adobe product roadmap review scheduled while 5x5 Trade Desk case study parameters established for resolution enhancement validation.

Agent Demo Preparation: Aadhitthyaa Hari Gopal completed comprehensive agent development coordination with James Geyer, Sardlow, and Michael Kelly, targeting Tuesday demo recording delivery. Action item resolution progressing across engineering team with enhanced functionality demonstration preparation.

### **Strategic Challenges**

Path Factory API Resolution: Matt Barnes managing critical investigation of 17% overlap discrepancy between API calls and UI results, requiring urgent resolution due to sales and marketing team dependency for lead generation partnership value.

Legal and Security Coordination: Anwar Mai navigating complex legal hurdles for flywheel data partner self-serve deployment requiring Brennan team security coordination and comprehensive compliance framework development for October launch.

Jury Duty Resource Impact: Matt Barnes facing potential availability constraints affecting September 16th release coordination, bot filtering beta recruitment, and mid-quarter delivery assessments across COIN and Inferno teams.

*Source: ZIM Team 1-2-3 Operating Framework entries and meeting transcript from September 8, 2025*

**Automation Team Weekly Report - September 12, 2025**

## **Executive Summary**

MCP infrastructure shortcuts create technical debt while API versioning scope expansion delays V2 timeline into Q1-Q2. Adam Peretz revealed that the current MCP implementation used API gateway shortcuts to accelerate launch, requiring migration to a dedicated MCP gateway before other teams can publish tools. Meanwhile, API V2 scope has expanded beyond initial estimates with more breaking changes identified, pushing realistic timelines into Q1-Q2 rather than earlier projections. Marc Frail completed comprehensive H2 planning infrastructure while Sam Massie finalized conditional logic requirements but identified field mapping complexity requiring phased delivery approaches.

## **This Week\'s Progress**

### **Key Momentum Areas**

Marc Frail delivered comprehensive H2 planning foundation, completing JIRA ticket creation for MCP and Public API workflows, finalizing the H2 tracker draft for team socialization, and scheduling Monday morning communications to highlight upcoming Workflows capabilities. This planning infrastructure provides visibility and coordination frameworks for complex multi-team initiatives.

Adam Peretz established API versioning process framework, finalizing documentation that enables breaking changes while discovering additional scope that requires careful prioritization. The versioning foundation unlocks accumulated technical improvements that have been deferred due to backward compatibility constraints.

Sam Massie resolved conditional logic complexity, completing requirements alignment with the Workbooks team on supported conditions and design recommendations. However, field mapping implementation may require phased delivery based on engineering capacity constraints, starting with single fields before expanding to mixed fields and multiple field support.

### **Goals & Progress**

H2 Planning Infrastructure: Marc Frail completed 100% of JIRA and tracker creation work, establishing the foundation for coordinated execution across MCP and Public API initiatives. The Monday morning Slack communication will socialize H2 Workflows capabilities to the broader team.

API Versioning Foundation: Adam Peretz completed versioning process documentation but identified additional breaking changes requiring level-of-effort investigation before timeline commitment. The expanded scope necessitates Q1-Q2 targeting rather than more aggressive timelines.

Conditional Logic Framework: Sam Massie finalized conditional filter and branching logic requirements, including Workbooks team alignment on supported conditions. The work will be revisited in 1-2 sprints for engineering handoff once higher-priority items are completed.

### **Strategic Challenges**

MCP gateway technical debt requires infrastructure migration, with Adam Peretz revealing that current MCP tools run on API gateway shortcuts rather than dedicated infrastructure. The team must complete official MCP gateway development and migrate existing tools before enabling broader team publishing capabilities.

Field mapping phasing complexity affects user experience continuity, as Sam Massie identified that engineering constraints may require starting with basic field mapping capabilities before adding Excel-style formulas and hierarchy mapping support. This phased approach balances delivery realities with user expectations.

API V2 scope creep threatens timeline predictability, with Adam Peretz discovering more desired breaking changes than initially anticipated. Careful prioritization against other roadmap commitments is required to establish realistic delivery expectations.

*Source: Team 1-2-3 Operating Framework entries from 9/8 - 9/12*

**Login/Provisioning Team Weekly Report - September 8, 2025**

## **Executive Summary**

This week, the Login and Provisioning team made significant progress on critical projects for the upcoming Copilot V2 release on October 6th. Key deliverables were unblocked, enabling the design and development of the Copilot V2 login experience. Brannen Huske also began building a roadmap for AI Action Credits to support the Copilot V2 launch and other AI monetization models.

## **This Week\'s Progress**

### **Key Momentum Areas**

Josh Simon successfully unblocked the GTM Copilot V2 team by getting the design for the app launcher tile finalized and the necessary platform array in place. This allows the Copilot team to prepare for the October 6th launch by enabling users to find the application via the waffle menu and app launcher after they log in.

Brannen Huske continued to make progress on the AI Action Credit roadmap, gathering input from key stakeholders like Adam, Mark, and Carlos to define the requirements for Copilot V2. This effort is crucial for creating a strategic roadmap that outlines what features are needed to unlock the market and when they need to be built.

### **Goals & Progress**

**Copilot V2 Readiness:** The team is focused on ensuring a smooth launch for Copilot V2. Josh Simon\'s main goal for the week was to finalize the GTM Copilot login tile, which is now design- and development-ready for the October 6th launch date. Brannen Huske\'s work on defining AI Action Credits for Copilot V2, with a roadmap being developed to support the sales motion and monetization of the new features.

**SSO Support:** Josh Simon continued to address SSO support issues, specifically for customers who want to use multiple tenants with the same SSO product. The team is working on documenting a more scalable and structured workaround to replace the current process and has two meetings scheduled to finalize it.

**AI Action Credits:** Brannen Huske is building out the AI Action Credit roadmap to plan for the evolution of different features, including what\'s needed for Copilot V2. The team realized that with the shift to Copilot V2, the needs for AI Credits are different and that credits will need to be app-specific. The roadmap will define the cadence for features like personal AI credits and usage limits to last through the end of the year.

### **Strategic Challenges**

Brannen Huske identified a need to understand the packaging requirements for Copilot V2, noting that this could require personal AI Action Credits, different seat types, or other features to support the sales motion. This is a strategic challenge that needs to be resolved by working with Mark Harris and Victor Oliveros to align on the packaging for the new product.

The team is also still actively reaching out to customers to solve ongoing login issues where they are getting logged out of the platform. This is an ongoing process that causes user frustration. Josh Simon is specifically investigating if an HTTP-only cookie will solve the bounce-out problem for some users, which is a promising solution that will require coordination with several teams to implement.

### **Strategic Insights**

**Key Learnings & Discoveries:** A key learning from the AI Credit work this week is that with the shift to Copilot V2, the needs for AI Credits are different from what was initially planned, and they will need to be application-specific and at the user level. We are still releasing the current AI Credit system work but going to continue on the AI Credit roadmap throughout October.

Josh Simon\'s investigation into the persistent login issues revealed that many departments at ZoomInfo rely on the \"LoginAs\" feature to do their jobs, and that a technical solution alone may not be enough. This issue is so ingrained in the daily workflow of teams like Customer Experience, Operations, and Customer Success Management that an organizational change and re-training will be necessary to help these teams rely less on the feature as a crutch.

**Cross-Team Dependencies:** The team also needs to work with the Agentic team and the Workbook team to ensure that the AI Action Credit service can charge credits correctly. This is a cross-functional effort that requires a detailed design review to account for jobs composed of multiple agents, ensuring all use cases are considered for a clear path to integration.

## **Looking Ahead**

The team will continue its focus on delivering key components for the October 6th Copilot V2 launch. Brannen Huske will work with Jessie Lindstrom to get her up to speed on the AI Action Credit roadmap and split the delivery work with her, focusing on SKU creation and revenue needs for Copilot V2. This will be a critical step in finalizing the monetization and packaging of the new features.

Additionally, Josh Simon will continue his login discovery work, preparing for a product review to gain alignment and a path forward on the LoginAs project. He will also move forward with the design kickoff for Data Passport Controls Version 3, which is a key initiative to improve privacy features for customers.

*Source: Team 1-2-3 Operating Framework entries from September 8, 2025*
