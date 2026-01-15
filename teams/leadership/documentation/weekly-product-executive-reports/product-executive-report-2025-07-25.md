---
id: synthesis-2025-30-2025
title: "Product Executive Intelligence Brief - July 25, 2025"
type: synthesis-report
status: approved
created: 2025-07-25
updated: 2026-01-06
week_ending: 2025-07-25
reporting_period: "Week of July 21-25, 2025"
tags: ["weekly-report", "synthesis", "Q32025"]
---

# **Product Executive Intelligence Brief - Week of July 21-25, 2025**

*Synthesized from 15 team reports: Product DAI Team, Apps Team, Data Team, Context Engineering Team, Core Data Team, Data Platform Team, Intent & Search Team, Product Ops Team, Semantic Data Team, ZIM Team, Automation Team, Admin Team, Integrations Team, Copilot Experience Team, Analytics Team*

*For detailed questions about any item below, reference specific team reports or contact team leads directly.*

## **Executive Summary**

### **Update on Previous Week Blockers**

**Platform Infrastructure Resource Bottlenecks Creating Cascading Delays:** Mixed progress with Semantic Data team resolving critical GCP infrastructure issues enabling 25,000 high-ACV account processing, but Apps team reports \"critical packaging architecture decision threatens Go-to-Market Studio launch success\" with Copilot Enterprise dependency creating artificial TAM limitations.

**AI Pricing Framework Decision Blocking October Launch:** Breakthrough achieved with Admin team successfully securing \"approval for AI credits, enabling their sale and quoting by sellers and through the ZI store\" and completing \"NPI document approval and creating tickets for new AI credit SKUs,\" resolving the major monetization blocker.

**Critical Engineering Resource Allocation Gaps:** Product DAI team escalates urgency with \"Critical Action Required: We have 6 weeks to September launch and scope must be locked with engineering commits by end of this week or initiatives become stretch goals\" while multiple teams report authentication and infrastructure dependencies blocking execution.

### **Current Week Update**

**Blockers:**

- **Packaging architecture dependencies artificially limiting market access:** Apps team reports \"Current requirement for Copilot Enterprise to access GTM Studio features creates artificial TAM limitation and will crush utilization metrics\" while Intent & Search team identifies \"Signal-based workbook architecture requires Copilot Enterprise, potentially blocking our intent tab modernization and advanced search overlay plans for non-Copilot SalesOS customers.\"

- **Infrastructure authentication gaps blocking agentic platform adoption:** Data team reports \"agentic platform infrastructure is fundamentally misaligned with the organization\'s \'move fast\' mandate\" with \"2+ week permission cycle for routine data access creating compound delays across multiple AI initiatives,\" while Automation team faces \"MCP authentication limitations forcing architectural compromises.\"

**Momentum areas:**

- **Multi-tenant semantic processing and data pipeline breakthroughs:** Semantic Data team \"successfully processed 25,000 high-ACV accounts this week while solving critical database scaling issues\" and Context Engineering team secured \"H2 alignment with data science and kicked off the Memory Service build,\" enabling advanced personalization capabilities.

- **Partner integration capabilities reaching production readiness:** Integrations team \"successfully launched API access for Copilot customers, enabling Salesloft and Outreach integrations that will drive upgrades and consumption across our 28,000 non-Copilot sales customers\" while ZIM team achieved \"Strategic partnership expansion with successful Unbounce CEO engagement.\"

**Bottom line:** Technical capabilities are maturing rapidly with semantic processing at scale and partner integrations driving customer value, but packaging architecture decisions and authentication infrastructure gaps are creating artificial constraints that threaten September launch timelines and market addressability without immediate executive intervention.

### **Mission-Critical GTM Jobs (Customer-facing GTM intelligence capabilities)**

**Product DAI Team:** \"Critical Action Required: We have 6 weeks to September launch and scope must be locked with engineering commits by end of this week or initiatives become stretch goals. The early access program execution is gaining momentum, but fundamental blockers around September roadmap clarity, copilot v2 program structure, and cross-team coordination are creating execution risk that demands immediate leadership intervention. Engineering teams are waiting for definitive direction while product teams operate with different sources of truth. Without consolidated program management and clear swim lanes, we risk missing our most critical H2 milestone that directly impacts Q4 revenue targets.\"

**Apps Team:** \"Critical packaging architecture decision threatens Go-to-Market Studio launch success. Current requirement for Copilot Enterprise to access GTM Studio features creates artificial TAM limitation and will crush utilization metrics. This technical dependency can be decoupled and must be addressed immediately with Mark Harris to prevent launch failure.Review required for Go-to-Market Studio launch. The current prerequisite of Copilot Enterprise to access GTM Studio features may unnecessarily limit the total addressable market and impact utilization. While technical dependencies exist, it\'s important to assess if this bundling is truly necessary or if a decoupling is feasible to broaden reach. This should be discussed with Mark Harris. The team achieved strong execution on core deliverables with email agent requirements finalized and GTM Studio PMM content development progressing. However, structural blockers around packaging decisions and resource allocation threaten H2 momentum without immediate executive intervention.Without immediate executive intervention, outstanding questions regarding packaging decisions and resource allocation pose a threat to H2 momentum.\"

**Copilot Experience Team:** \"Strong cross-team alignment achieved on unified experience strategy with clear technical direction established for dynamic profiles and CoPilot Pro onboarding. Ant Cuomo secured alignment with engineering leadership on chat v2 implementation while Adam Severance completed strategic planning for Day 1 user experience. Critical architectural decision made on data resolution approach that unblocks profile loading across platforms.\"

**Intent & Search Team:** \"Critical blocker identified: Signal-based workbook architecture requires Copilot Enterprise, potentially blocking our intent tab modernization and advanced search overlay plans for non-Copilot SalesOS customers. Al Nevarez will setup a call with Victor, Sneh, Nebo, Sean to review technical limitations of enabling Signal based workbook and/or its data processing beyond Copilot customers. Al also checking with Lou Wolf on our large recent deal (needs Dynamics in intent report) to ensure they\'ll be on Copilot, to minimize risk and have path forward for them this year. Meanwhile, Advanced search UXR preparation advanced with new designer onboarding and interviewee candidate list development. Hari\'s topic recommendation research revealed we may need to allow for more topic edits per year for mid/enterprise clients. We\'ll also consider auto-assigning topics our topic recommender feature finds. Phase 1 is based on an expanded version of Guided Intent, which looks beyond assigned topics.\"

**ZIM Team:** \"Strategic partnership expansion achieved with successful Unbounce CEO engagement, while critical August release planning establishes clear go/no-go decisions for customer-facing features. Team delivered 83% goal completion rate with strong progress on H2 planning and notification center preparation for early adopter program launch. Data exhaust strategy breakthrough identified as \'Holy Grail\' opportunity for bidirectional value creation with integration partners, positioning team for expanded partner ecosystem development.\"

**Automation Team:** \"MCP authentication limitations are forcing architectural compromises while GTM Plays alignment accelerates toward execution. Adam Peretz discovered that the current MCP specification only supports Okta-hosted login pages, creating a significant limitation for SSO customers and potentially delaying the board demonstration planned for month-end. Sam Massie successfully transitioned workflow frontend ownership and identified three must-have improvements for GTM Plays, while Marc Frail achieved strong tactical alignment on triggers and actions needed to support the platform.\"

### **Data Foundation & Consumption (Platform capabilities enabling GTM intelligence)**

**Data Platform Team:** \"Enterprise Search is achieving critical milestones for Q3 Workbooks GA with all Phase 1 signal data now available in Solr and ready for app integration. However, architectural decisions around Federated Search vs. GTM Store lookup approaches remain unresolved. The team needs executive alignment on the Query API architecture to unlock parallel workstreams and maintain delivery timelines for key platform capabilities, but this is not a blocker for WB GA.\"

**Integrations Team:** \"Bottom Line: Andres Perez successfully launched API access for Copilot customers, enabling Salesloft and Outreach integrations that will drive upgrades and consumption across our 28,000 non-Copilot sales customers. Prateek Paikray\'s Salesforce AgentForce package is 85% complete despite authentication storage challenges, with the team targeting Tuesday delivery for our October Dreamforce showcase. This positions us to demonstrate real-time data activation capabilities to enterprise customers while creating a scalable model for future partner integrations.\"

**Semantic Data Team:** \"The Semantic Data Team successfully processed 25,000 high-ACV accounts this week while solving critical database scaling issues that were blocking the pipeline. Josh Mantovani identified and fixed a one-line environment setup bug that was plaguing the agentic platform\-\--a breakthrough that unblocks platform development. The team is now positioned to enable multi-tenant support next week, with authentication and orchestration work ready to begin.\"

**Data Team:** \"Rob Priore completed a comprehensive business plan outline for our email deliverability product, positioning us to monetize our abuse desk expertise as an outsourced service for customers. Dana Hurtig\'s team achieved breakthrough operational efficiency with 5x productivity gains on conference automation, while the franchise dataset development hit a major milestone with Igor\'s team processing 12,000 PDF files to extract comprehensive location data for 3,000 US franchises, creating what Brandon Tucker accurately identified as a \'game changer\' product that no competitor offers.\"

**Core Data Team:** \"Rituparna Das drove an increase in person data coverage by infusing 1.2M validated emails with 50% attach rate and validated legal approval to proceed with 8.5M mobile records infusion, to continue closing gaps against competitors like Cognism and Apollo. Meanwhile, Magnus Herweyer\'s comprehensive stakeholder analysis revealed address normalization as the unanimous top priority across all data teams, providing clear strategic direction for the shared services initiative. Multiple team members struggled with AI tool limitations that slow down velocity on Q3 planning completion and overall output.\"

### **Contextual Data Velocity (Learning flywheel creating competitive moat)**

**Analytics Team:** \"The analytics team is on track to deliver a comprehensive customer dashboard next week, with Nanxi Ge completing 80% of the integration work despite data size challenges. Key strategic insights emerged showing renewal accounts significantly outperform new accounts across all engagement metrics, with 10% higher CRM integration rates and 22% more AI feature adoption. Preetham Srinithi resolved critical amplitude attribute automation blockers and will deploy the solution to production by Wednesday.\"

**Context Engineering Team:** \"Christine\'s S2A knowledge transfer documentation is taking significantly longer than anticipated (30% complete vs. planned 100%), revealing critical technical debt that needs addressing before the team can move forward with new account generation features. Despite this delay, the team achieved strong progress on foundational work\-\--Rowan secured H2 alignment with data science and kicked off the Memory Service build, while Robyn completed the AFS PRD draft and uncovered a critical dependency on CRM integration data that will require an aggressive acquisition strategy to make APS/AFS algorithms effective at the product level.\"

### **Operational Velocity (Operating at AI-company speed vs SaaS speed)**

**Product Ops Team:** \"PMs gave positive feedback on the updated feature info pack process, cutting documentation time from 60+ minutes to \~30 minutes through AI optimization. Sam Darcy unblocked VOC deployment by partnering with the semantic data team\'s agentic platform, while the knowledge graph prototype is ready for executive validation. However, we need to better translate and scale learnings from agent building across the AI PMM engine to maximize our infrastructure investments.\"

**Admin Team:** \"This week, the team successfully secured approval for AI credits, enabling their sale and quoting by sellers and through the ZI store. We also finalized designs and backend infrastructure for the new login pricing page flow, addressing a significant number of support tickets and improving user experience. A key strategic challenge addressed was the urgent reprioritization of contributory network work, which Jessie Lindstrom successfully managed by re-shuffling team priorities.\"

*For deeper analysis on any topic above, reference specific team reports or contact team leads directly.*

*Methodology: Analysis of team 1-2-3 Operating Framework reports, prioritizing: (1) Executive decisions needed, (2) Cross-team blockers, (3) Strategic momentum areas, (4) Strategic alignment gaps*

# **📊 Appendix**

### **Individual Team Reports**

# **Product DAI Executive Roundup - Monday July 21st - Friday July 25th**

## **Executive Summary**

Critical Action Required: We have 6 weeks to September launch and scope must be locked with engineering commits by end of this week or initiatives become stretch goals. The early access program execution is gaining momentum, but fundamental blockers around September roadmap clarity, copilot v2 program structure, and cross-team coordination are creating execution risk that demands immediate leadership intervention.

Engineering teams are waiting for definitive direction while product teams operate with different sources of truth. Without consolidated program management and clear swim lanes, we risk missing our most critical H2 milestone that directly impacts Q4 revenue targets.

## **This Week\'s Progress**

### **Key Momentum Areas**

Early Access Program Execution Breakthrough: Sneh\'s team successfully transitioned from recruitment to execution mode, locking in 30 itemized accounts across the next 3 weeks with kickoff calls booked. The team simplified the overwhelming GTM Studio vision into two clean use cases - AI audience building for new business and AI enrichment for cross-sell opportunities - dramatically improving onboarding team confidence and customer ramp velocity.

PMM Engine Foundation Established: Despite automation complexity requiring more prototyping than expected, the team achieved 80% completion on knowledge graph infrastructure with Sam. The discovery revealed that effective AI implementation requires many specialized \"micro-agents\" with highly iterative prompt engineering rather than broad automation, establishing a more realistic framework for scaling content production.

Design System Modernization: The design team delivered three comprehensive concepts for GTM Studio and Copilot Pro\'s overall look and feel, moving beyond fragmented prototypes to establish scalable design foundations. This unlocks the engineering team to begin building cohesive user experiences rather than disjointed feature sets.

### **Goals & Progress**

September Launch Scope: Currently at 50% completion with critical dependencies still unresolved. While the steel thread narrative framework exists, open areas including activation to copilot, custom datasets integration, and direct CRM retrieval approaches remain without engineering commits. The team has identified specific alignment needs across multiple engineering groups but lacks consolidated program management to drive resolution.

Copilot v2 Architecture: Made significant progress on core use case definition and engineering collaboration, but the program lacks the structured tracking and dependency management that made GTM Studio successful. Engineering leadership is requesting clarity on program execution model and resource allocation before committing to September timelines.

Custom Data Pipeline: Achieved 25% completion with basic working version for contractor dataset, but scaling challenges revealed infrastructure gaps. The team discovered that current identity graph partners and public data sources require optimization upgrades that weren\'t initially scoped, creating potential delivery risk for H2 revenue targets.

### **Strategic Challenges**

Program Management Fragmentation: Multiple teams are building toward convergent goals using different tracking systems and sources of truth, creating alignment friction that slows execution velocity. The successful GTM Studio program management model exists but hasn\'t been replicated for Copilot v2, leaving engineering teams without clear direction on dependencies and timelines.

September Deadline Reality: With 6 weeks remaining, any scope items without engineering commits by week\'s end will become stretch goals. Historical data shows stretch goals rarely deliver, yet critical platform dependencies like query API, CRM enhancements, and custom field support remain in requirements stage rather than development. This creates cascading risk for Q4 revenue commitments.

Cross-Functional Coordination Gaps: Security requirements appeared sideways causing escalation, pricing model implementation needs architecture decisions, and data pipeline teams operate in silos despite building complementary capabilities. These coordination breakdowns suggest need for stronger platform-level orchestration to prevent future execution disruption.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Simplified User Journey Validation: The early access program\'s shift from grandiose vision to focused use cases proved immediately effective with internal teams and customer onboarding. This validates the hypothesis that clear, constrained problem-solving drives faster adoption than broad platform capabilities, suggesting similar simplification could accelerate other product areas.

AI Implementation Complexity Realism: PMM engine work revealed that effective AI requires specialized micro-agents with iterative prompt engineering rather than broad automation. This insight should inform scoping decisions across all AI initiatives, as the implementation effort exceeds initial estimates but delivers higher quality outputs when done correctly.

Engineering Readiness Gaps: Multiple workstreams discovered that foundational platform capabilities assumed to be ready require additional development cycles. Query layer blockers affect CRM enhancements, custom fields, and signals integration simultaneously, highlighting the need for clearer platform roadmap visibility to prevent future surprise dependencies.

### **Cross-Team Dependencies**

Platform Infrastructure Criticality: GTM Studio, Copilot v2, and custom data initiatives all depend on query layer enhancements that remain uncommitted by engineering. This single dependency affects multiple H2 revenue drivers and requires immediate escalation to platform leadership for prioritization and resourcing decisions.

Integration Team Coordination: Data pipeline success requires tight coordination between integrations team, platform team, and various product teams, but current communication patterns are reactive rather than proactive. Establishing weekly cross-team tactical sessions could prevent the surprise blockers that have emerged repeatedly this quarter.

## **Looking Ahead**

September Scope Finalization: Next week represents the final opportunity to secure engineering commits for September launch scope. Any remaining open items in activation to copilot, custom datasets, and CRM integration must be resolved or explicitly moved to stretch status with alternative plans developed.

Program Management Scaling: The Copilot v2 initiative needs immediate program management structure replication from GTM Studio\'s successful model, including dedicated tracking resources, weekly tactical rhythms, and clear dependency mapping. Without this structure, engineering leadership cannot provide reliable delivery commitments.

Platform Dependency Resolution: Query layer and CRM enhancement blockers require immediate escalation to resolve the cascading impacts across multiple product initiatives. This represents the highest leverage intervention point for ensuring H2 execution success, as multiple teams are currently blocked waiting for these foundational capabilities.

# **Apps Executive Roundup - Monday July 21st - Friday July 25th**

## **Executive Summary**

Critical packaging architecture decision threatens Go-to-Market Studio launch success. Current requirement for Copilot Enterprise to access GTM Studio features creates artificial TAM limitation and will crush utilization metrics. This technical dependency can be decoupled and must be addressed immediately with Mark Harris to prevent launch failure.Review required for Go-to-Market Studio launch. The current prerequisite of Copilot Enterprise to access GTM Studio features may unnecessarily limit the total addressable market and impact utilization. While technical dependencies exist, it\'s important to assess if this bundling is truly necessary or if a decoupling is feasible to broaden reach. This should be discussed with Mark Harris.

The team achieved strong execution on core deliverables with email agent requirements finalized and GTM Studio PMM content development progressing. However, structural blockers around packaging decisions and resource allocation threaten H2 momentum without immediate executive intervention.Without immediate executive intervention, outstanding questions regarding packaging decisions and resource allocation pose a threat to H2 momentum.

## **This Week\'s Progress**

### **Key Momentum Areas**

Email agent strategy crystallized with executive alignment achieved. Gabe successfully drafted and socialized high-level requirements for the draft email agent, securing consensus from Victor and Dominik on direction. The key strategic insight was accelerating the coaching/continuous improvement component from milestone 6-7 into the initial release, ensuring the learning capability doesn\'t get deprioritized. Engineering and design teams now have clear direction to begin implementation work targeting the August Chat 2.0 release.

GTM Studio enablement engine gains traction through AI-first content development. Lauren completed comprehensive SME interviews with Sneh, Jagan, Millie, and Brandon, generating substantial knowledge base content for discovery questions and objection handling. This will feed into a set of discovery questions built by an AI agent for use with SE team. The team discovered significant value in building specialized agents, including a Solutions Consultant bot that will enhance seller enablement across AI platforms. This work directly supports the critical GTM Studio launch readiness.

Advanced search roadmap alignment progresses despite technical complexities. Al completed advanced search prototyping and initiated UXR planning with new designer onboarding. The team made strategic progress on intent tab modernization through signal-based workbooks concept, though packaging limitations emerged as a significant constraint. The team made strategic progress on intent tab modernization through signal-based workbooks concept, though packaging limitations emerged as a significant constraint. The team also made progress on the need for alignment on signal-based tabular views, but further discovery is needed between engineering and applications on decoupling the backend so it can be used in Sales Hub and GTM Studio. We should not tie it to workbooks explicitly in order to retire Intent and Websights search but rather run it through Sales Hub. Intent topic recommendation analytics framework was established, setting foundation for improved customer intent selection guidance.

### **Goals & Progress**

Email Agent Development: High-level requirements completed and reviewed with stakeholders, achieving 100% goal completion. Engineering team received clear specifications for data sources (semantic layer, person briefs, account summaries, engagement history) and output requirements. Next phase focuses on building functional prototype to demonstrate email quality comparable to internal chat bot within 1-2 sprints.

GTM Studio Content & Enablement: 90% completion with final SME interview pending. Discovery questions framework developed through comprehensive stakeholder interviews, revealing critical insights about sales terminology clarity (specifically around \"plays\" concept that may confuse field teams). Solutions consultant agent prototype in development to automate future enablement content creation.

Advanced Search & Intent Modernization: Mixed progress with 100% completion on intent admin analysis but confusion and misalignment discovered around packaging dependencies. Intent topic recommendation feature near launch-ready with new admin interface, though implementation approach needs refinement to drive actual adoption rather than just recommendations.

### **Strategic Challenges**

Packaging architecture creates artificial market limitations that could hinder GTM Studio success. Current requirement for Copilot Enterprise to access any GTM Studio functionality, including signal-based workbooks, severely constrains addressable market. Most SalesOS customers lack Copilot Enterprise, making the intent tab modernization impossible for primary user base. This technical dependency appears solvable through entitlement decoupling but requires further alignment.

Resource allocation misalignment between innovation needs and maintenance requirements. Advanced search team faces reduced engineering capacity due to Israeli team constraints while simultaneously needing to deliver Microsoft accessibility compliance, natural language search capabilities, and GTM data model integration. The team must choose between maintaining legacy systems and building next-generation capabilities, with current resourcing insufficient for both paths.

Topic recommendation adoption challenge reveals deeper packaging model problems. New guided intent recommendation system demonstrates superior topic selection but relies on admin interface that historically sees low engagement. Analysis shows most customers never modify zero-config settings, yet current packaging model assumes active topic management. This suggests fundamental misalignment between product capabilities and customer behavior patterns. Next steps are to revisit with GTM Strategy team.

## **Strategic Insights**

### **Key Learnings & Discoveries**

AI-first content development dramatically accelerates iteration cycles while maintaining quality standards. Team discovered that while AI reduces revision count, it doesn\'t reduce time per revision, requiring 2-3 hours for comprehensive updates. However, the ability to rapidly generate initial frameworks and incorporate complex stakeholder feedback has proven invaluable for GTM Studio content development. This approach enables more frequent iteration cycles with executive stakeholders.

Signal-based workbook architecture offers unified solution for disparate data views but requires packaging strategy alignment. Technical investigation revealed opportunity to consolidate intent tab, website buyer ID, and advanced search into single tabular interface using GTM data model pipeline. This approach would eliminate maintenance burden on legacy systems while providing modern user experience, but current packaging restrictions prevent implementation for core user base.

Customer intent topic selection behavior contradicts product packaging assumptions. Data analysis revealed midsize and enterprise customers regularly hit 12-topic change limits while SMB customers make 1-3 changes annually. Most customers rely on zero-config selections rather than active management, suggesting need for more intelligent auto-selection rather than increased manual configuration options.

### **Cross-Team Dependencies**

Our collaboration with the GTM Studio team on packaging strategy requires alignment to resolve technical dependencies that artificially limit market addressability. Current entitlement architecture ties workbook functionality to Copilot Enterprise for business rather than technical reasons, creating solvable problem that also relates to intent tab modernization and advanced search enhancement.

Platform engineering coordination essential for email agent data source integration, with August 1 timeline confirmed for engagement history API availability. This dependency management proves critical for maintaining sprint commitments while ensuring production-ready data access patterns.

## **Looking Ahead**

Email agent prototype development takes priority with aggressive timeline to prove capability superiority. Next week targets functional email generation comparable to internal chat bot, requiring coordination with Rowan on coaching components and detailed data source requirement documentation. Success here builds confidence for broader agentic roadmap while providing competitive differentiation against internal tool adoption.

Packaging architecture discussion with Mark Harris becomes urgent priority to unblock GTM Studio launch strategy. Lauren, Sneh, and Victor must engage revenue operations leadership to evaluate decoupling GTM Studio features from Copilot Enterprise requirement. Technical solutions exist but require business decision to separate packaging from technical capabilities, enabling broader market access and improved utilization metrics.

Advanced search and intent modernization pivot toward unified sales hub integration to avoid interface proliferation. Al and Victor will coordinate with Sean, Sneh, and Nebo to align signal-based views with copilot v2 data processing pipeline, eliminating need for separate workbook interface while maintaining modern functionality. This consolidation strategy reduces engineering overhead while providing consistent user experience across sales tools.

# **Data Team Executive Roundup - Monday July 21st - Thursday July 24th**

## **This Week\'s Progress**

### **Key Momentum Areas**

Rob Priore completed a comprehensive business plan outline for our email deliverability product, positioning us to monetize our abuse desk expertise as an outsourced service for customers. This represents a genuine new revenue channel that leverages our unique data position to help customers avoid spam folder issues - a critical pain point when using our data at scale.

Dana Hurtig\'s team achieved breakthrough operational efficiency with 5x productivity gains on conference automation, effectively eliminating nearly 2 FTE worth of manual work while simultaneously cleaning 160,000 junk executive profiles from top 500 companies. The mobile phone infusion from Statara delivered 8.9M additional contacts with 89% attachment rates, demonstrating our data enhancement capabilities are scaling effectively.

The franchise dataset development hit a major milestone with Igor\'s team processing 12,000 PDF files to extract comprehensive location data for 3,000 US franchises, creating what Brandon Tucker accurately identified as a \"game changer\" product that no competitor offers. Early validation shows this could command premium pricing across Fortune 500 accounts.

### **Goals & Progress**

Agentic Development: Jody Roberts achieved 90% completion on roadmap consolidation and successfully deployed a working data insights agent to staging, though production deployment remains blocked by authentication infrastructure gaps. The team also built a presentation agent capable of generating branded HTML presentations, showing the platform\'s versatility for internal tooling.

Signal Enhancement: Brandon Wilson refined the \"Won Deal in Similar Account\" signal generation process and delivered feedback-ready signals to account managers, advancing our semantic data integration capabilities. Steve Hutchinson completed analysis planning for contact recommender signal lift testing, potentially unlocking significant improvements in signal relevancy.

Data Products: Dow Jones shifted strategic focus from individual dataset releases to foundational enablement framework development, recognizing that vertical dataset success requires differentiated go-to-market approaches. This pivot, while delaying restaurant dataset launch, addresses critical seller enablement gaps that could determine long-term adoption success.

### **Strategic Challenges**

Our agentic platform infrastructure is fundamentally misaligned with the organization\'s \"move fast\" mandate. Jody\'s data insights agent has been technically ready for weeks but remains blocked by Google IAP authentication requirements that demand custom development and multi-team coordination. This 2+ week permission cycle for routine data access is creating compound delays across multiple AI initiatives and signals a systemic issue that requires C-level attention.

ZoomInfo\'s internal chatbot platform has severe context window limitations that prevent sophisticated data use cases. Multiple team members hit these constraints when attempting to build comprehensive data agents, forcing workarounds through external platforms like Claude. This architectural limitation undermines our ability to leverage our own AI infrastructure for competitive advantage.

Customer identification and engagement processes for critical initiatives like \"definition of a company\" remain ad hoc and resource-intensive. Ethan Young continues struggling to secure appropriate customer conversations despite this being fundamental to our data model evolution. This suggests we need formalized customer research processes that don\'t rely on individual relationship networks.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The gap between enterprise customers\' data needs and their ability to articulate solutions is massive. Brandon Tucker\'s meeting with Walmart\'s third-party data manager revealed she oversees 20+ vendors with 100+ products but lacks systematic ways to match capabilities to use cases. When Adobe requested \"email activity data\" for Marketo qualification, there were multiple better solutions than raw email volume - but no mechanism exists to surface these alternatives. This insight validates our hypothesis that intelligent data recommendation systems could dramatically expand deal sizes and customer satisfaction.

Vertical datasets require fundamentally different enablement approaches than core platform data. Dow Jones\'s strategic pivot to focus on enablement frameworks rather than rushing additional dataset releases demonstrates mature recognition that first impressions with GTM teams will determine long-term success. The contractor dataset\'s early positive signals validate this approach, but we need systematic processes to avoid repeating one-off enablement cycles.

Our operational efficiency gains are compounding faster than expected. Dana\'s team achieved 5x improvements on conference automation while simultaneously maintaining quality improvements across multiple data streams. This suggests we\'re hitting an inflection point where AI-driven automation is becoming multiplicative rather than additive - a competitive moat if we can maintain velocity.

### **Cross-Team Dependencies**

Our agentic development success depends critically on DevOps and Security teams establishing streamlined authentication frameworks that don\'t require custom engineering for each use case. The current model where every agent needs individual permission architecture is unsustainable for scaling AI initiatives.

The franchise dataset commercialization requires coordinated execution between Data Engineering for processing, GTM for enablement, and potentially Marketing for SEO-driven discovery pages. Igor\'s insight about creating ZoomInfo franchise landing pages for organic search positioning could drive significant top-of-funnel acquisition.

## **Looking Ahead**

Next week\'s focus must prioritize infrastructure unblocking over feature development. While the team continues advancing on franchise data processing, signal enhancement, and dataset enablement, the highest-leverage activity is resolving authentication and access control bottlenecks that are constraining our entire agentic roadmap.

The franchise dataset represents our best near-term opportunity for market-moving revenue impact. With 200,000 individual franchise locations mapped to parent companies and complete contact data, this addresses a genuine market gap that Fortune 500 companies will pay premium prices to access. We should expedite go-to-market preparation and consider aggressive pricing strategies that reflect the dataset\'s uniqueness.

We need systematic customer research processes that don\'t rely on ad hoc relationship management. The definition of a company initiative\'s customer engagement challenges highlight a broader organizational gap in structured customer feedback loops. Success with vertical datasets and advanced data products requires consistent customer input that current processes cannot reliably deliver.

# **Context Engineering Team Executive Roundup - July 25, 2025**

## **Executive Summary**

Christine\'s S2A knowledge transfer documentation is taking significantly longer than anticipated (30% complete vs. planned 100%), revealing critical technical debt that needs addressing before the team can move forward with new account generation features. Despite this delay, the team achieved strong progress on foundational work\-\--Rowan secured H2 alignment with data science and kicked off the Memory Service build, while Robyn completed the AFS PRD draft and uncovered a critical dependency on CRM integration data that will require an aggressive acquisition strategy to make APS/AFS algorithms effective at the product level.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Foundation Setting for H2**: Rowan successfully aligned scoring and recommendations milestones with data science, getting all semantic, memory, and context epics into Jira. The Memory Service project kicked off with engineering alignment on architecture, positioning the team to begin building next week. This creates the infrastructure needed for advanced agent capabilities.

**Algorithm Strategy Crystallization**: Robyn completed Draft 1 of both the AFS PRD and IMS PRD, working closely with data science to define how AFS + IMS = APS. Through deep discovery work, she identified that achieving product-level recommendations will require significantly more CRM data than currently available, leading to three proposed workaround strategies.

**Critical Documentation Progress**: Christine\'s deep dive documentation work, while slower than planned, is uncovering essential context about features like block list and dismiss functionality that will inform future development decisions.

### **Goals & Progress**

**Knowledge Transfer & Documentation**: Christine achieved 30% of her documentation goal, completing Chapter 1 (13 pages) with Chapter 2 expected to be even longer. The extended timeline reflects the complexity of explaining how account generation has worked to date, including forgotten features that proved more important than initially thought. She needs the first two days of next week to complete the work.

**Algorithm Product Definition**: Robyn completed her goal of drafting the AFS PRD and advanced the IMS PRD to Draft 1. She successfully navigated the ambiguity around workbooks, plays, and copilot workflows\-\--identifying that these core workflows are still being shaped presents an opportunity to design algorithmic support in parallel. The CRM data analysis revealed significant gaps that will require strategic intervention.

**Infrastructure & Scaling**: Rowan achieved 100% of his goals, establishing clear H2 planning for signals and recommendations while kicking off the momentum score POC with Tamiro and Arash. Srivatsa completed his work on Websights integration, though complexity remains around data volumes and whether to combine Websights with Buyer ID signals.

### **Strategic Challenges**

**CRM Data Dependency Crisis**: Robyn\'s analysis revealed that effective APS/AFS algorithms require deep CRM activity and opportunity data, which is likely incomplete or inconsistent across customers. Without product-level understanding of customer environments, the team cannot deliver accurate scoring and prioritization. This requires immediate strategic discussion about integration incentives and in-product workflows to encourage data capture. The team has developed three workaround strategies but needs executive alignment on the path forward.

**Scaling Engineering Resources**: The semantic data service investigation was delayed when Grant was pulled into the Agentic demo push. This blocker affects the team\'s ability to determine whether CloudSQL can support up to 100 tenants or if immediate architectural changes are needed. With H2 planning underway, this technical uncertainty could impact delivery timelines.

**Cross-Team Workflow Ambiguity**: The evolving definitions of workbooks, plays, and copilot workflows create integration challenges for the algorithms team. Without clear product design direction and tighter integration, Robyn cannot finalize how APS algorithms will surface in user workflows. This dependency on product design decisions risks delaying the user-facing implementation of backend capabilities.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Technical Debt Reality Check**: Through Christine\'s documentation effort and a knowledge transfer call with Daryl and Victor, the team confirmed that S2A was a POC that should never have reached production. Market dynamics forced rapid productionization without proper infrastructure planning, leading to feature decay over time. This validates the team\'s decision to rebuild rather than iterate on the existing foundation.

**Data Strategy Imperative**: Robyn\'s investigation into CRM data availability exposed a fundamental challenge: the team\'s algorithmic ambitions exceed current data collection capabilities. Her finding that past experiments in sentiment analysis and deal closure correlation may have been attempted at Gong (but institutional knowledge is lost) suggests the need for better experiment documentation going forward. The team needs to decide between building with current limitations or implementing an aggressive data acquisition strategy first.

**Context Service Evolution**: Through mapping existing agents and their data requirements, Rowan discovered that 20-30 agents have been built, each creating individual connections to ZDP and GTM models. This proliferation of uncoordinated data access patterns validates the need for a centralized context service that can pre-aggregate and optimize data delivery to improve agent performance.

### **Cross-Team Dependencies**

Our work with Product Design on workbooks and copilot integration remains critical for delivering user-facing algorithm capabilities. The lack of clarity on personas (is workbooks only for analysts?) and workflow definitions prevents Robyn from finalizing the UX for algorithm explanations and recommendations. With design team members heading to Europe for two weeks, the team needs to prepare concrete proposals now to avoid further delays.

The dependency on Data Science for the momentum score POC and APS architecture is progressing well, with strong alignment from Arash and clear enthusiasm for the exploratory work. This collaboration model\-\--where product and data science iterate together on early concepts\-\--is proving effective and should be replicated for future algorithm development.

## **Looking Ahead**

Next week\'s focus centers on three critical paths that will determine H2 execution success. Christine will complete the S2A knowledge transfer documentation, with particular emphasis on batch and real-time signal generation infrastructure. This documentation can be used to inform rebuild efforts.

Robyn will shift to deep investigation of AFS implementation details, including scaling considerations for Top Contacts and designing for peaks around ReachOut functionality. She\'ll work with Brandon on Clickagy legal documentation to clarify data usage boundaries while continuing to map CRM data availability across the customer base. The goal is to present a clear recommendation on whether to proceed with current data limitations or pivot to data acquisition first.

Rowan will conduct his planned deep dive into agent context requirements, mapping specific data needs to production agents and identifying where context is the bottleneck to performance. With the semantic data service scaling investigation finally scheduled, the team will have clarity on infrastructure constraints by week\'s end. This positions the Context Engineering team to enter August with clear technical boundaries and strategic direction for delivering the promised intelligent experiences.

*Source: Team 1-2-3 Operating Framework entries from July 21-25, 2025*

# **Core Data Executive Roundup - Week of 07/21 - 07/25**

## **Executive Summary**

Rituparna Das drove an increase in person data coverage by infusing 1.2M validated emails with 50% attach rate and validated legal approval to proceed with 8.5M mobile records infusion, to continue closing gaps against competitors like Cognism and Apollo. Meanwhile, Magnus Herweyer\'s comprehensive stakeholder analysis revealed address normalization as the unanimous top priority across all data teams, providing clear strategic direction for the shared services initiative. Multiple team members struggled with AI tool limitations that slow down velocity on Q3 planning completion and overall output.

## **This Week\'s Progress**

### **Key Momentum Areas**

Magnus Herweyer completed 65% of his shared services roadmap creation through systematic interviews across internal teams and external Chorus calls, discovering unanimous agreement that address normalization represents the highest-impact first service. This consensus across PTI, company, data tools, and monitoring teams provides rare organizational alignment and clear direction for resource allocation.

Rituparna Das delivered exceptional results on her goal to increase mobile and business email coverage, infusing 1.2M Revenue Base validated emails with a strategic 50% attach rate while preventing duplicates. After navigating an unexpected legal review, she secured approval for the 8.5M mobile infusion, with 70% completion achieved by Thursday and full delivery expected by next week Tuesday.

Peter Overman achieved 70% completion on locking down roadmaps for both web data acquisition and data pipelines teams, completing engineering manager reviews and establishing frameworks for living documentation. His work with Corina on platform application enablement for datasets in GTM Studio continues to navigate complex multi-stakeholder discussions while maintaining focus on customer use cases.

### **Goals & Progress**

**Roadmap Finalization**: Jody Roberts made substantial progress on the H2 (Q3/Q4) roadmap finalization using the HTML presentation agent, while advancing the data insights agent to the point of PTI team handoff. Critical achievement: securing permissions for traceability API access, removing a key technical barrier. Discovery of low-hanging fruit opportunities to leverage agent platform capabilities for common data questions suggests potential for rapid value creation.

**Cross-Team Coordination**: John Durst executed \"horse trading for H2 on cross team objectives,\" establishing the technographics channel as the single source for all technographic questions. His collaboration with Hayden Cowell on validation analysis revealed that Zippy achieves 92% accuracy versus 50% for manually researched phones - a finding that fundamentally challenges data quality assumptions.

**Research Enablement**: Hayden Cowell worked to pull research samples for Polaris metrics and update researcher instructions to include Brandon\'s subjective scoring methodology for SMB/mid-market segments. While sample pulling was delayed due to Valerie\'s absence, the methodology updates position the team to model customer perception where objective data doesn\'t exist.

### **Strategic Challenges**

Cam Fortin\'s goal to create high-level project documents for team alignment revealed a systematic challenge: the Thursday reflection meeting creates uncertainty in goal completion reporting since Friday is often when substantial work gets completed. This timing misalignment affects accurate status reporting and mirrors sprint estimation challenges, potentially undermining executive visibility.

Magnus Herweyer faces complex implementation decisions to address normalization without dedicated engineering resources (Casey out for two weeks). The choice between leveraging existing PTI or company solutions versus building new infrastructure that supports both batch and streaming has significant technical debt implications for the shared services foundation.

Multiple team members encountered AI tool reliability issues, with Cam Fortin losing 6 hours to chatbot errors that \"constantly errors out.\" This forced reversion to manual processes at a critical planning juncture, highlighting the gap between AI tool promise and current reality while potentially delaying Q3 commitment finalization.

## **Strategic Insights**

### **Key Learnings & Discoveries**

John Durst\'s identification of a critical blind spot - \"we should have better analysis around individual sources of information and their accuracy\" - gained immediate validation through his phone validation work. The discovery that ZIPI (automated email signatures) achieves 92% accuracy versus 50% for human-validated phones suggests the organization lacks systematic source quality measurement and may be misallocating validation resources.

Legal\'s unexpected intervention on mobile data usage, as noted by Rituparna Das, exposed process gaps in cross-functional coordination. While she successfully navigated to approval, the last-minute nature reveals the need for proactive legal partnership in data expansion initiatives to prevent delays that could impact competitive positioning against Apollo and Cognism.

The universal emergence of address normalization as top priority across all stakeholder interviews conducted by Magnus Herweyer provides rare organizational consensus. This alignment creates an opportunity to deliver immediate value through shared services while building credibility for the broader platform vision.

### **Cross-Team Dependencies**

Our collaboration with the PTI team reaches a critical milestone with Tuesday\'s scheduled handoff of Jody Roberts\' data insights agent. With traceability API permissions now granted, organizational readiness for agent-powered workflows faces its first real test.

Peter Overman\'s work with data pipelines teams under Brian and Roi continues to require careful navigation through 40+ JIRA items and confusing nomenclature (teams calling themselves both \"data acquisition\" and \"data pipelines\"). His focus on protecting customer use cases while managing multi-stakeholder complexity remains essential for Q3 success.

Rituparna Das identified a blind spot where \"same mobile used by multiple contacts\" creates data quality challenges, particularly as the Data Enablement team conducts parallel mobile infusions without following the pre-validation processes her team established for 5x5 data.

## **Looking Ahead**

Next week centers on converting planning progress into executable Q3 commitments while addressing the systematic challenges uncovered this week.

Magnus Herweyer will complete his shared services roadmap by merging internal and external feedback, with specific implementation recommendations for address normalization. Rituparna Das finalizes the 8.5M mobile infusion and socializes coverage improvements while reviewing local address engineering findings. Peter Overman pushes to 100% completion on both roadmaps while establishing review cadences with leadership.

Critical process improvements take priority as the team addresses the Thursday/Friday reporting disconnect and establishes fallback procedures for AI tool failures. Hayden Cowell\'s research sample pull proceeds with Valerie\'s return, enabling subjective scoring methodology implementation. John Durst advances development of systematic source accuracy measurement to address the critical blind spot identified this week.

The convergence of operational lessons with strategic discoveries positions the team to enter Q3 with clarity of purpose, realistic tool expectations, and renewed focus on data quality fundamentals that drive competitive advantage.

*Source: Team 1-2-3 Operating Framework entries from 07/21-07/25*

# **Data Platform Team Executive Roundup - 7/21/25**

## **Executive Summary**

Enterprise Search is achieving critical milestones for Q3 Workbooks GA with all Phase 1 signal data now available in Solr and ready for app integration. However, architectural decisions around Federated Search vs. GTM Store lookup approaches remain unresolved. The team needs executive alignment on the Query API architecture to unlock parallel workstreams and maintain delivery timelines for key platform capabilities, but this is not a blocker for WB GA.

## **This Week\'s Progress**

### **Key Momentum Areas**

Menna Rashwan completed comprehensive alignment on Enterprise Search milestones required for signal-based workbook creation, with all Phase 1 signal data successfully deployed to Solr and validated for app team integration. The UX session for signal enrichment flows reached completion, enabling the Workbooks team to proceed with their Q3 GA timeline.

Linda Johannessen drove significant progress on Query API scope definition and finalized the Metadata API specification, creating clear technical boundaries for downstream implementation. Her work on GraphQL GTM Store requirements and OpenAI agent/connector analysis is positioning the platform for future agentic capabilities and competitive differentiation.

Marc Delurgio achieved 70% completion on lookup API alignment. Moshik evaluated Match A/B testing frameworks, discovering that ZI Chat demonstrates exceptional performance in retrieving relevant Confluence pages, indicating strong potential for knowledge management applications.

### **Goals & Progress**

**Enterprise Search Integration**: Menna Rashwan reached 100% completion on Enterprise Search milestone definition and signal data availability, with comprehensive working sessions completed with the Co-Pilot Priority Accounts team identifying two clear integration paths. The team successfully navigated complex dependencies around CRM custom fields and established fallback strategies for platform component delivery timing.

**Query API Architecture**: Linda Johannessen achieved 80% progress on architecture alignment, with Query API scope now clearly defined and Metadata API definition completed. However, interface boundaries between federated search and query API layers require final resolution before implementation can proceed at full velocity.

**Customer Analysis & Documentation**: Moshik Levin completed most of the planning documentation for Automated Match A/B testing while conducting deep analysis of current A/B testing approaches, shifting focus to comprehensive documentation of current state systems to inform future customer segmentation and location matching use cases.

### **Strategic Challenges**

Architectural alignment across federated search versus direct GTM Store lookup approaches is still being evaluated. The decision impacts Linda Johannessen\'s Query API boundaries, and downstream team integration strategies.

Cross-team dependency management presents ongoing coordination challenges, particularly around Enterprise Search integration timing with Co-Pilot and Advanced Search migration sequences. Menna Rashwan identified critical blind spots where end-to-end flows could break if migration timing isn\'t synchronized, requiring proactive coordination to prevent system disruptions.

Resource coordination and timeline alignment across App teams and Platform engineering is creating scope uncertainty for H2 roadmap execution. App team re-prioritization is impacting Enterprise Search milestones, requiring leadership alignment to clarify shared dependencies and ensure coordinated delivery sequencing.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team discovered that Enterprise Search can only support CRM custom fields once all platform dependencies including Metadata Registry, CDC, and GTM Store are fully delivered and configured. However, the Workbooks exception demonstrates that alternative architectural approaches can unblock critical use cases when needed, providing a template for future dependency management strategies.

Co-Pilot team integration analysis revealed that teams without fixed phase 2 dates are more likely to wait for the complete Query API solution rather than accepting interim integration work, indicating that delivery timeline uncertainty creates natural adoption delays that should be factored into platform rollout strategies.

ZI Chat\'s exceptional performance in retrieving relevant Confluence pages suggests that current Match capabilities have strong potential for knowledge management applications, potentially opening new use case opportunities beyond traditional data platform scenarios that Moshik Levin\'s analysis is beginning to uncover.

### **Cross-Team Dependencies**

Our work with AI Enterprise on Query API delivery timelines remains critical for enabling multiple downstream integrations including Co-Pilot and Enterprise Search consumers. Current discussions focus on Metadata Registry and CDC delivery coordination to guide integration decisions and prevent duplicate technical work across teams.

The Workbooks team dependency continues to drive platform prioritization with their Q3 GA timeline creating firm delivery constraints for Enterprise Search capabilities. Ongoing collaboration on signal-based workbook UX flows and technical integration support is proceeding on schedule with clear milestone alignment established.

## **Looking Ahead**

Next week\'s primary focus centers on resolving the fundamental architectural decision between Federated Search and direct GTM Store lookup approaches, which will unlock parallel development across multiple platform components and clarify integration specifications for downstream consumers.

Linda Johannessen will finalize the lookup approach decision while she completes architecture alignment across query and search layers, with GraphQL GTM Store work decomposition beginning once interface boundaries are established. Menna Rashwan will continue Workbooks collaboration on signal-based UX flows while supporting app teams in Phase 1 signal integration work. Moshik Levin will shift from current state documentation to customer-focused analysis, beginning with location matching use cases that leverage the documented Match A/B testing framework insights.

The team is well-positioned to accelerate delivery once architectural decisions are locked, with strong momentum on Enterprise Search capabilities and clear visibility into cross-team coordination requirements for successful platform adoption.

*Source: Operating Document entries from 7/21/25*

# **Intent & Search Team Executive Roundup - July 21, 2025**

## **Executive Summary**

Critical blocker identified: Signal-based workbook architecture requires Copilot Enterprise, potentially blocking our intent tab modernization and advanced search overlay plans for non-Copilot SalesOS customers. Al Nevarez will setup a call with Victor, Sneh, Nebo, Sean to review technical limitations of enabling Signal based workbook and/or its data processing beyond Copilot customers. Al also checking with Lou Wolf on our large recent deal (needs Dynamics in intent report) to ensure they\'ll be on Copilot, to minimize risk and have path forward for them this year. Meanwhile, Advanced search UXR preparation advanced with new designer onboarding and interviewee candidate list development. Hari\'s topic recommendation research revealed we may need to allow for more topic edits per year for mid/enterprise clients. We\'ll also consider auto-assigning topics our topic recommender feature finds. Phase 1 is based on an expanded version of Guided Intent, which looks beyond assigned topics.

## **This Week\'s Progress**

### **Key Momentum Areas**

Al successfully onboarded the new designer to advanced search vision and UXR orchestration plans, establishing clear handoff for user research coordination. This strategic delegation positions the team for accelerated UXR execution while freeing Al for higher-level coordination.

Hari completed foundational studies on topic recommendation adoption patterns, discovering that customers rarely modify intent topics after initial setup, with only enterprise customers hitting the 12-topic annual change limit. This insight opens pathways for automated topic assignment and increased intent topic modification limits.

UXR candidate pipeline strengthened with Vivek providing new interview candidate list targeting balanced user segments including daily, monthly, and less-than-monthly users to ensure comprehensive needs assessment for advanced search development.

### **Goals & Progress**

**Advanced Search UXR**: Progression with designer training / onboarding to adv search completion and candidate review scheduled for next week. Al established clear vision communication and orchestration framework, positioning for user outreach phase targeting diverse usage patterns to inform advanced search design decisions. The designer is also now experimenting with v0/cline prototypes for adv search.

**Topic Recommendation Framework**: Hari advanced co-occurrence analysis and general adoption studies while building specialized MCP for deep keyword analysis. Research revealed automation opportunities with Daryl suggesting automatic topic assignment based on low customer modification rates and enterprise limit constraints.

**Intent Tab Modernization**: Technical architecture planning progressed but encountered Copilot Enterprise dependency blocker. Team identified signal-based workbook requirements that could limit feature availability to Copilot customers, potentially forcing retention of legacy intent tab for broader SalesOS user base.

### **Strategic Challenges**

Signal-based workbook architecture presents significant deployment constraints as it requires Copilot Enterprise integration, yet substantial SalesOS customer base remains on non-Copilot plans. This dependency threatens our intent tab modernization strategy and advanced search overlay implementation, potentially forcing maintenance of legacy systems we planned to deprecate. Al is coordinating with Snay to explore technical workarounds while awaiting Lou\'s confirmation on major sales deal Copilot requirements.

Multi-AFS launch timing creates strategic decision point as engineering completion coincides with workbook transition planning and data science team\'s new APS framework exploration. Hari\'s analysis highlighted marketing customer demand and completed engineering investment, but workbook migration timing may require launch pause despite customer expectations and development investment.

Go-to-market data model integration complexity emerges as modern user experiences become tied to Copilot Enterprise, creating potential feature fragmentation between customer tiers. This architectural constraint could limit our ability to deliver consistent advanced search and intent capabilities across the full customer base while maintaining our deprecation timeline.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Topic modification behavior analysis revealed customers typically maintain default configurations with minimal changes, contradicting assumptions about active topic management. This discovery suggests automation opportunities and validates Daryl\'s automatic assignment proposal, potentially simplifying user experience while reducing support overhead.

Copilot Enterprise dependency introduces broader architectural considerations for feature deployment strategy. The requirement creates potential customer tier fragmentation that could impact our unified product vision and force parallel development paths for equivalent functionality.

Customer demand signals from marketing teams awaiting Multi-AFS launch demonstrate market readiness despite internal technical transitions. Hari\'s impact analysis highlighted substantial customer investment in pending features, suggesting delivery timing sensitivity beyond internal architectural preferences.

### **Cross-Team Dependencies**

Coordination with Sneh\'s team critical for resolving signal-based workbook technical limitations affecting non-Copilot customer access. This dependency directly impacts our modernization timeline and may require architectural compromise or alternative implementation paths.

Data science team\'s APS framework development creates parallel technical direction requiring alignment with current Multi-AFS completion. Their new approach could influence our launch timing decisions and long-term technical strategy integration.

Lou\'s large sales deal Copilot status confirmation needed to validate customer readiness for signal-based workbook features including dynamic CRM integration with HubSpot and Salesforce through modern go-to-market data model approach.

## **Looking Ahead**

Next week focuses on resolving architectural blockers while maintaining momentum on user research and feature completion priorities.

Al will conduct UXR candidate review ensuring balanced user segment representation for advanced search needs assessment while coordinating technical limitation discussions with Snay regarding non-Copilot workbook access. Multi-AFS launch decision requires data science alignment on APS framework timing and customer impact assessment from Hari\'s analysis. Lou\'s Copilot confirmation will inform signal-based workbook deployment feasibility for major customer engagements.

Technical architecture decisions this week will establish our deployment strategy for modern features while balancing customer tier considerations and legacy system maintenance requirements.

*Source: Intent & Search Team Operations Review - Week of July 21, 2025*

# **Product Ops Executive Roundup - July 21, 2025**

## **Executive Summary**

PMs gave positive feedback on the updated feature info pack process, cutting documentation time from 60+ minutes to \~30 minutes through AI optimization. Sam Darcy unblocked VOC deployment by partnering with the semantic data team\'s agentic platform, while the knowledge graph prototype is ready for executive validation. However, we need to better translate and scale learnings from agent building across the AI PMM engine to maximize our infrastructure investments.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Release Process Optimization**: PMs testing the updated feature info pack and PRfaq process delivered overwhelmingly positive feedback, with documentation time cut from over 60 minutes to approximately 30 minutes. This represents a 50% productivity improvement in one of our most frequent PM workflows, validating our AI-first approach to process automation.

**VOC Infrastructure Breakthrough**: Sam Darcy eliminated major blockers by partnering with Josh semantic data team to rebuild the VOC tool on their existing agentic platform. This strategic pivot provides immediate deployment capabilities without procurement delays and leverages pre-built optimizations for transcript searching and text fragment creation.

**Knowledge Graph Foundation**: The knowledge graph prototype successfully processed 111 documents from our AI marketing engine knowledge base, creating a postgres database with atomic notes, concepts, and relationship mapping. Brett and Sam have scheduled a demonstration to validate the foundational architecture before expanding to additional use cases.

### **Goals & Progress**

**AI Documentation Automation**: Daniel Kong advanced work on AI-powered updating of existing implementation and knowledge center documents, evolving from a simple document inventory to creating automatic ingestion rules for the 700+ files in our knowledge center. This includes developing systems to determine whether new releases require net new articles or updates to existing content.

**Cline Integration & Agentic Platform**: Kristin Gandini made progress integrating Lars\' agentic platform repository into the Cline starter kit, with Mike successfully building agents using Guy\'s components. However, Jira ticket creation instructions remain pending from Guy\'s team, requiring prioritization discussion given competing engineering demands.

**Team Onboarding Systematization**: Christine Ward identified critical gaps in PM onboarding automation, highlighting challenges with Victor\'s rapid integration and the need for AI-first onboarding experiences. Collaboration with Saif\'s team, who developed comprehensive PM role documentation, offers a path forward for systematic new hire integration.

### **Strategic Challenges**

**Engineering Resource Prioritization**: Multiple initiatives depend on Guy\'s team, creating a bottleneck across VOC deployment, Cline infrastructure, and Jira automation. We need clearer prioritization frameworks to help Guy\'s team sequence competing demands from our various workstreams without constant escalation.

**Agent Development Knowledge Transfer**: While individual team members successfully build agents for specific use cases, we lack systematic approaches to translate and scale these learnings across the AI PMM engine. This creates risk of redundant development and missed opportunities to leverage existing platform capabilities.

**Cross-Functional Coordination Complexity**: The OP model reporting deadline required extension from 2pm to 4pm to accommodate team submissions, highlighting ongoing coordination challenges as our AI tooling scales across more teams and stakeholders.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Platform Leverage Over Custom Development**: Sam\'s pivot to the semantic data team\'s agentic platform demonstrates the value of leveraging existing infrastructure over custom builds. Their pre-built transcript processing and chat interface capabilities eliminated weeks of development work while providing superior functionality.

**Process Optimization Yields Immediate ROI**: The feature info pack improvements show concrete productivity gains from AI optimization, validating our approach of systematically improving high-frequency PM workflows. This success model should guide prioritization of additional process automation initiatives.

**Documentation at Scale Requires Automation**: Daniel\'s analysis of 700+ knowledge center files reinforces that manual documentation management cannot scale with our release velocity. Automated ingestion and updating systems are prerequisites for maintaining current and accurate product information.

### **Cross-Team Dependencies**

Our work with Guy\'s engineering team spans multiple critical initiatives including Cline infrastructure, VOC deployment, and Jira automation. Brett emphasized the need for better prioritization coordination to prevent engineering bottlenecks from blocking multiple product ops workstreams simultaneously.

Collaboration with the semantic data team proved transformative for VOC development, suggesting opportunities to identify and leverage additional platform capabilities across other teams rather than building custom solutions.

## **Looking Ahead**

Next week focuses on scaling our successful AI implementations while addressing infrastructure dependencies. The VOC tool moves into PM testing phase, the knowledge graph undergoes executive validation, and we systematize agent development learnings.

**Immediate Priorities**: Sam will finalize VOC testing preparation and work with Brett on knowledge graph demonstration materials. Kristin will coordinate with Lars on Cline-agentic platform integration strategy while pursuing Guy\'s team prioritization. Daniel will advance automated documentation ingestion with Russell\'s team input on scaling approaches.

**Strategic Focus**: We\'re shifting from proof-of-concept development to systematic scaling of AI capabilities. This requires better coordination frameworks with engineering teams, standardized approaches to agent development, and clearer documentation automation workflows that support our accelerating release cadence.

The team demonstrated strong execution this week across multiple complex initiatives. With VOC infrastructure resolved and knowledge graph foundations solid, we\'re positioned to deliver significant productivity improvements across PM workflows while building scalable AI-driven go-to-market capabilities.

*Source: Product Ops Team Meeting July 21, 2025*

# **Semantic Data Team Executive Roundup - July 25, 2025**

## **Executive Summary**

The Semantic Data Team successfully processed 25,000 high-ACV accounts this week while solving critical database scaling issues that were blocking the pipeline. Josh Mantovani identified and fixed a one-line environment setup bug that was plaguing the agentic platform\-\--a breakthrough that unblocks platform development. The team is now positioned to enable multi-tenant support next week, with authentication and orchestration work ready to begin.

## **This Week\'s Progress**

### **Key Momentum Areas**

Rowan Bailey drove strategic alignment on H2 Planning, securing agreement from data science teams on goals and epics for transitioning from rigid heuristic systems to dynamic ML models. The new account fit and in-market scoring models will update by tenant, representing a significant maturation in organizational capabilities. This positions us to better serve both prospecting and account management use cases.

Jon Seller solved critical database connection scaling issues that were blocking the high-ACV account pipeline, enabling the team to process 90 days of data for 25,000 accounts. The fix allows the full pipeline to run at scale in the dev environment with minimal errors, where it previously would \"blow up.\" This unblocks the path to multi-tenant support and positions us for rapid customer onboarding.

The momentum score initiative was successfully kicked off with two productive meetings, addressing a critical gap in helping AEs and AMs prioritize their active deals. Unlike account fit scores for prospecting, momentum scoring will tell sellers which of their 20 active opportunities are trending toward closure versus those needing revival. This directly supports our strategic shift toward selling to AEs and AMs through the platform.

### **Goals & Progress**

**Data Pipeline & Infrastructure**: Jon Seller achieved 90% completion on high-ACV account processing (25,000 of \~27,500 accounts), solving core database connection issues that were causing pipeline failures. The correction script for fragment processing mismatches is ready to run over the weekend, addressing data quality issues reported by support. Multi-tenant PR is complete pending passive login integration.

**Extraction Quality & Evaluation**: Inga Isakov completed 5 email thread evaluations, uncovering critical edge cases including LLM hallucination issues where ABC was incorrectly extracted as an entity in Disney/ESPN communications despite no mention in the source data. This finding highlights the importance of controlling general knowledge injection in our extraction pipeline. Weekend work will complete the remaining evaluations and begin data source analysis.

**Memory Service & Agentic Platform**: Josh Mantovani\'s breakthrough fix for the environment setup issue unblocks agentic platform development after weeks of troubleshooting. The Memory service project was successfully kicked off with Grant, Asher, and Eric, establishing the actions log concept for tracking high-value copilot interactions. Josh will lead this implementation starting next week.

### **Strategic Challenges**

Authentication complexity for multi-tenant support is creating networking challenges between GCP and dev containers, preventing Jon from completing the passive login integration. The team is exploring local setup workarounds to maintain momentum on multi-tenant delivery. Resolution requires either DevOps support to fix networking or completion of local environment setup as a temporary measure.

Data source prioritization remains unresolved, with stakeholders pushing for job posting data integration despite fundamental misalignment with our current extraction pipeline. Rowan correctly identified that job postings require different ontology and processing than interpersonal communications. The team needs executive alignment on whether to build a separate pipeline for structured data sources or focus on expanding interpersonal communication sources first.

Grant\'s availability for orchestration RFC review was blocked by agentic demo priorities, delaying critical architectural decisions for the scalable pipeline. While the demo takes precedence, this pushes orchestration design discussions to next week, potentially impacting our ability to handle dynamic account filtering and priority queuing for the growing pipeline demands.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The LLM hallucination discovery by Inga reveals a critical vulnerability in our extraction pipeline where models inject general knowledge even when explicitly processing isolated email threads. The ABC/Disney/ESPN case demonstrates that our current approach allows unwanted entity associations based on real-world relationships rather than document content. This finding will drive prompt engineering improvements and stricter context controls.

Josh and Rowan\'s analysis confirmed that our current pipeline architecture is fundamentally incompatible with structured data sources like job postings. The extraction ontology designed for interpersonal communications produces \"garbage\" when applied to job listings. This validates the need for multiple pipeline architectures rather than forcing all data through a single processing model.

The database scaling solution reveals that half the pipeline issues stemmed from misunderstanding Google Cloud Proxy connection patterns rather than code problems. Jon\'s deep investigation into connection pooling and error patterns provides a template for avoiding similar scaling issues as we onboard new tenants and increase data volumes.

### **Cross-Team Dependencies**

Our work with Data Science on the momentum score and enhanced scoring models requires tight coordination as they begin model development. The success of these initiatives depends on clear API contracts and data availability timelines from our pipeline. Weekly syncs with Arash and Nilesh will be critical to ensure model requirements align with our extraction capabilities.

The Memory service implementation requires close collaboration with Grant\'s team on the agentic platform, though his demo commitments are limiting availability. Josh\'s leadership on this project will need to balance independence with necessary architectural alignment once Grant becomes available next week.

## **Looking Ahead**

Next week\'s primary focus is enabling multi-tenant authentication to unblock customer onboarding, with Jon working through networking issues while preparing the orchestration RFC for dynamic pipeline management. This positions us to handle multiple customers while maintaining data isolation and quality.

The team will complete extraction evaluations and begin detailed scoping of new data sources, with particular attention to the job posting question that requires executive alignment on strategic direction. Inga\'s analysis will inform whether we pursue a separate structured data pipeline or double down on interpersonal communication sources that align with our current architecture.

Josh will lead Memory service implementation while the broader team reviews orchestration patterns for scalable pipeline management. Success requires balancing immediate multi-tenant needs with longer-term architectural decisions that will determine our ability to scale to dozens of customers and data sources.

*Source: Team 1-2-3 Operating Framework entries from July 21-25, 2025*

# **ZIM Team Executive Roundup - Week of July 21, 2025**

## **Executive Summary**

Strategic partnership expansion achieved with successful Unbounce CEO engagement, while critical August release planning establishes clear go/no-go decisions for customer-facing features. Team delivered 83% goal completion rate with strong progress on H2 planning and notification center preparation for early adopter program launch. Data exhaust strategy breakthrough identified as \"Holy Grail\" opportunity for bidirectional value creation with integration partners, positioning team for expanded partner ecosystem development.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Strategic Partnership Development**: Anwar Mai successfully completed high-level Unbounce integration presentation to CEO and leadership team, establishing foundation for flywheel vendor partnership that will enhance identity resolution and intent data through contributory network expansion. Meeting demonstrated proven integration patterns for visitor resolution and intent capabilities.

**August Release Clarity**: Matt Barnes delivered comprehensive go/no-go assessment for August customer releases, with 5x5 IP-to-company data integration (11% identification improvement) approved for August deployment. AI Page Rank and bot filtering moved to September release to ensure quality delivery and proper impact assessment.

**H2 Planning Excellence**: Jesse Miller finalized H2 goals focusing on feature iteration improvements and ZIM Agent development, positioned for Workday submission before August 1st deadline. Notification Center preparation on track for Early Adopter Program launch August 5-19 with comprehensive enablement materials completed.

### **Goals & Progress**

**Integration Process Documentation**: Aadhitthyaa Hari Gopal completed comprehensive ISV onboarding process documentation, streamlining future partner integration workflows and eliminating time waste across team coordination. Process improvements establish stronger foundation for scaled partner ecosystem development.

**Compliance Framework Development**: Brett Elliot progressed bidder compliance planning to 33% completion, systematically cataloguing browser signals and header request requirements for international ad delivery compliance. Two additional weeks required for comprehensive legal submission covering do-not-track signals and bid request compliance.

**Topic Setup Innovation**: Shuxin Yang achieved 50% completion on Topic Setup Accelerator roadmap, with foundational exploratory work scheduled for Q3 execution due to resource priorities. Initiative targets competitive differentiation in intent topic setup speed versus other GTM platforms.

**Infrastructure Preparation**: Matt Barnes established LRT process for approved August releases while identifying AI Page Rank impact assessment needs for S2A signal processing systems.

### **Strategic Challenges**

**Data Exhaust Strategy Gap**: Critical blind spot identified in bidirectional data flow from partners using ZoomInfo data. Current inability to receive usage analytics from DSPs, DMPs, and integration partners limits value realization and funding opportunities for visitor resolution and intent initiatives.

**Technical Access Constraints**: Matt Barnes experiencing staging access delays for Admin Portal, creating medium-impact blocker for Domains and AI Page Rank testing workflows. Multiple team members affected by provisioning backlog requiring escalation support.

**Resource Allocation Pressures**: Shuxin Yang\'s Topic Setup Accelerator requires foundational exploratory work that competes with Q3 priorities, highlighting need for strategic resource allocation across innovation initiatives and operational excellence.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Data Exhaust \"Holy Grail\"** **Opportunity**: Anwar Mai identified transformational potential in solving bidirectional data flow challenges. Establishing pathways to receive usage data from partners using ZoomInfo audiences would enable identification value delivery while capturing intent signals and identity enhancement, creating sustainable funding model for visitor resolution investments.

**Partnership Integration Patterns**: Unbounce engagement demonstrated repeatable integration patterns applicable across flywheel vendor ecosystem. Success requires addressing fundamental question of data ingestion methods - script deployment, visit data ingestion, or web analytics platform integration - with mandated pathways for value capture.

**Release Quality Framework**: Matt Barnes\' August release assessment reveals importance of preliminary forecasting and customer beta testing for features generating high-volume signal data. AI Page Rank moved to September with beta option for controlled volume assessment and S2A impact evaluation.

**Agent Platform Prioritization**: Jesse Miller\'s ZIM Agent becomes top H2 priority, expanding from AdOps focus to comprehensive solution incorporating custom reporting use cases, demonstrating platform approach to automation capabilities.

### **Cross-Team Dependencies**

Our work with Unbounce partnership requires systematic integration process execution, with Aadhitthyaa Hari Gopal\'s documented workflows enabling efficient onboarding and legal pathway establishment through Beeswax DSP evaluation by July 31st.

Data exhaust strategy development necessitates collaboration across customer success, legal, and engineering teams to establish mandated data sharing frameworks with partners using ZoomInfo data for identification and intent enhancement.

GTM Data Model team coordination essential for Aadhitthyaa Hari Gopal\'s \"plays\" development, requiring alignment on data store architecture and prioritization frameworks for customer workflow automation.

## **Looking Ahead**

Next week focuses on H2 goal finalization and ZIM Agent kickoff, with team positioned to leverage established partnership foundations for expanded ecosystem development and data exhaust strategy implementation.

Key priorities include completing H2 goal submissions before August 1st deadline, initiating ZIM Agent development with OPT team coordination, and advancing LinkedIn end-to-end campaign capabilities discovery through DeltaX partnership options. Notification Center enters critical QA and testing phase for Early Adopter Program launch preparation.

Strategic partnership development continues with Adobe release architecture documentation and Beeswax DSP legal review completion, while Matt Barnes addresses staging access escalation for August release testing workflows. Data exhaust strategy development begins with framework definition for mandated partner data sharing agreements.

Team maintains strong execution momentum with clear release planning, partnership expansion, and platform capability development supporting continued investment in visitor resolution and intent data market leadership.

*Source: ZIM Team 1-2-3 Operating Framework entries and meeting transcript from July 21, 2025*

# **Automation Executive Roundup - 7/25/2025**

## **Executive Summary**

MCP authentication limitations are forcing architectural compromises while GTM Plays alignment accelerates toward execution. Adam Peretz discovered that the current MCP specification only supports Okta-hosted login pages, creating a significant limitation for SSO customers and potentially delaying the board demonstration planned for month-end. Sam Massie successfully transitioned workflow frontend ownership and identified three must-have improvements for GTM Plays, while Marc Frail achieved strong tactical alignment on triggers and actions needed to support the platform.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Sam Massie completed the workflow frontend transition**, successfully taking ownership of core workflow experience items and identifying the critical path for GTM Plays readiness. Through coordination with design and engineering, three must-have improvements were prioritized: data mapping from previous steps, extensible trigger/action library with forms capability, and generic filtering/branching functionality.

**Marc Frail achieved 80% completion on GTM Plays JIRA organization**, making substantial progress on transferring the prioritized initiative list from Google Sheets into JIRA and linking it to the broader GTM Studio program. Strong tactical alignment was maintained on workflow capabilities needed to support GTM Plays, including a socialized definition of required triggers and actions.

**Cross-functional alignment strengthened on GTM Plays requirements**, with the GTM Plays team sharing a comprehensive list of triggers and actions they believe are needed, most of which depend on other teams. This visibility into dependencies enables better coordination and prevents duplicate work across the platform.

### **Goals & Progress**

**MCP Authentication**: Adam Peretz achieved 50% completion due to discovering fundamental limitations in the MCP specification. While authentication functionality can be implemented, the requirement to use Okta-hosted login pages instead of self-hosted pages eliminates SSO support for enterprise customers, affecting meaningful adoption for the highest-value customer segment.

**GTM Plays Execution Planning**: Marc Frail reached 80% completion on JIRA board population, successfully organizing the tactical aspects of workflow support for GTM Plays. The work establishes clear tracking for execution priorities while maintaining alignment on capabilities needed across the platform.

**Workflow Frontend Ownership**: Sam Massie completed the transition of workflow frontend responsibilities, establishing clear understanding of the must-have improvements needed for GTM Plays success. The prioritization focuses development efforts on the highest-impact capabilities rather than spreading resources across nice-to-have features.

### **Strategic Challenges**

**MCP authentication constraints threaten enterprise adoption**, with the protocol\'s limitation to Okta-hosted pages preventing SSO integration that enterprise customers require. This represents a fundamental platform limitation rather than an implementation choice, forcing the team to choose between launching with limited enterprise functionality or waiting for MCP protocol maturation.

**Board demonstration timeline creates execution pressure**, with Dominic planning to present MCP functionality to the board of directors by month-end. The authentication limitations discovered this week make the demo timeline aggressive and potentially unrealistic, requiring careful expectation management with leadership.

**Ownership alignment remains incomplete for complex GTM Plays flows**, despite strong tactical agreement on required capabilities. Marc Frail noted that broader alignment sessions are still needed on ownership of complex workflows and socialization of how these flows will function between workflows and plays.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**MCP protocol maturity lags enterprise integration requirements**, with current authentication limitations preventing the self-hosted login pages necessary for SSO functionality. While 80% of customers can be served with Okta-hosted authentication, the limitation excludes enterprise customers who represent the highest value segment for API adoption.

**GTM Plays dependencies are largely external to the automation team**, based on the trigger and action list shared by the GTM Plays team. This insight suggests the automation team\'s role is more integrative than developmental, focusing on enabling capabilities built by other teams rather than creating new automation primitives.

**Frontend workflow improvements have clear prioritization for GTM Plays**, with data mapping, extensible triggers/actions, and filtering/branching identified as must-haves versus nice-to-haves. This clarity enables focused development rather than attempting to improve all workflow capabilities simultaneously.

### **Cross-Team Dependencies**

Frank\'s authentication research is critical for determining MCP launch feasibility, with potential workarounds being investigated to overcome Okta-hosted page limitations. The timeline pressure from the board demonstration adds urgency to finding viable solutions.

Design and engineering coordination was essential for Sam Massie\'s successful transition of workflow frontend ownership, demonstrating effective cross-functional collaboration when clear scope and priorities are established.

## **Looking Ahead**

Next week focuses on resolving MCP authentication constraints while advancing GTM Plays execution planning despite upcoming PTO schedules.

Adam Peretz will continue investigating authentication options with Frank to determine how closely the Okta-hosted experience can approximate current functionality, aiming to maximize initial launch impact while planning for long-term protocol improvements. Marc Frail will complete JIRA organization and continue broader alignment sessions on complex workflow ownership patterns.

Sam Massie will review remaining H2 initiatives to clarify ownership before going on leave Wednesday through Friday, ensuring continuity of workflow frontend development while he\'s out. The authentication investigation represents a critical decision point for MCP launch strategy, determining whether to proceed with limited enterprise functionality or adjust timeline expectations for the board presentation.

*Source: Team 1-2-3 Operating Framework entries from 7/21 - 7/25*

# **Admin Team Executive Roundup - 7/21/2025**

## **Executive Summary**

This week, the team successfully secured approval for AI credits, enabling their sale and quoting by sellers and through the ZI store. We also finalized designs and backend infrastructure for the new login pricing page flow, addressing a significant number of support tickets and improving user experience. A key strategic challenge addressed was the urgent reprioritization of contributory network work, which Jessie Lindstrom successfully managed by re-shuffling team priorities.

## **This Week\'s Progress**

### **Key Momentum Areas**

This week, Brannen Huske successfully moved forward with AI credits by getting NPI document approval and creating tickets for new AI credit SKUs, allowing them to be quoted and sold. This is crucial for the monetization of GTM Studio.

Josh Simon finalized the account information that can be pulled from Salesforce to the login landing pages and created stories for the new login pricing page flow. This pushes forward a main goal of the partnership with the support team and integrates the login flow for unassigned users with the leads team. He also confirmed that reference users will be handled within SCIM provisioning, which will unblock new reference user creation and boost SCIM adoption.

Jessie Lindstrom effectively managed priorities to handle the urgent reprioritization of Contributory Network work. She was able to adapt and prioritize this critical initiative, which supports the Contributory Network\'s ability to add more data to the flywheel.

### **Goals & Progress**

**Login Experience:**: Josh Simon finalized the account information pull from Salesforce to login landing pages and created stories for the new login pricing page flow, ensuring all designs are feasible for relevant information. This is 100% complete for the week.

**AI Credits:**: Brannen Huske completed the creation of AI Credit tickets for the dev team, RevOps, and dependent teams, submitting the NPI ticket and scheduling meetings. The dev tickets have been created and refined. This goal is 100% complete for the week.

**Org Hierarchy**: Jessie Lindstrom successfully informed GTM Studio dependencies at risk due to the urgent reprioritization of Contributory Network dependencies, with a mitigation plan in place. Team agreed with the trade-off with the mitigation plan is crucial for supporting the Contributory Network\'s ability to contribute additional data to the flywheel. This Contributory Network work will be complete for this sprint..

### **Strategic Challenges**

A primary challenge this week, as highlighted by Jessie Lindstrom and Brannen Huske, was the urgent reprioritization of contributory network work. The effort required for this work and its timeline could impact the timeline to resolve username collisions, delaying progress on unified users and the Golden Org Hierarchy. It also had the potential to impact AI Credit work and the larger GTM Studio timeline. This situation necessitated flexible prioritization to ensure the team could meet the contributory network\'s requirements.

Another challenge is figuring out how reference users will work within SCIM provisioning, as identified by Josh Simon. This unblocks new reference user creation with SCIM provisioning and will work in conjunction with the drive to boost SCIM adoption. Currently, collision issues are occurring with trials being upgraded to paid accounts, causing errors when trying to provision existing users through SCIM.

Additionally, Brannen Huske has identified a blind spot regarding ensuring correct reporting of AI credit usage to SAP, particularly with the shift from reporting bulk credit purchases immediately as closed revenue to reporting usage-based AI credits as open revenue that closes as it is spent.

## **Strategic Insights**

### **Key Learnings & Discoveries**

A key learning from Jessie Lindstrom\'s work is the importance of proactive dependency identification and flexible prioritization for the provisioning team, as last-minute requirements frequently necessitate a rapid reshuffling of planned work.

Josh Simon\'s efforts revealed that the PMM work is now much more streamlined, with significant improvements to the ZI Chatbot based on feedback.

Brannen Huske\'s work on AI credits has provided a clear understanding of the revenue reporting process for usage-based credits, moving from immediate closed revenue for bulk purchases to revenue being recognized as credits are spent down.

### **Cross-Team Dependencies**

Our work with the Salesforce team and RevOps was critical for finalizing the login pricing page flow, enabling us to trigger leads and campaigns in Salesforce.

The provisioning team and Contributory Network team are closely intertwined, as urgent reprioritization for the Contributory Network directly impacts the provisioning team\'s timeline and ability to resolve other critical initiatives like username collisions and unified user progress.

Coordination with Garrett Cummins\' team is essential to ensure AI credit usage revenue is correctly reported to SAP, given the new model of reporting revenue as credits are spent rather than at the point of purchase.

## **Looking Ahead**

Next week, the team will continue to build on this week\'s progress with a focus on finalizing key architectural and reporting elements.

Josh Simon will focus on locking in second-half goals and aligning for \"login as\" and privacy work. He will also follow up with Sean and Lars to discuss handling public and customer data in conjunction with agentic deep research, aiming to be proactive rather than reactionary.

Brannen Huske\'s primary goal for next week is to review the AI credit dev solution put together by the team and William Lam. This review will inform the creation of development tickets. Additionally, Brannen will collaborate with Garrett Cummins\' team to ensure accurate reporting of AI credit usage revenue to SAP.

Jessie Lindstrom will collaborate with the agentic platform teams to ensure that agents respect and enforce user entitlements, covering both packaging (ensuring users only access what they\'ve paid for) and role-based access control. This is crucial for maintaining data security and adherence to product offerings.

# **Integrations Executive Roundup - Week of July 21, 2025**

## **Bottom Line:**

Andres Perez successfully launched API access for Copilot customers, enabling Salesloft and Outreach integrations that will drive upgrades and consumption across our 28,000 non-Copilot sales customers. Prateek Paikray\'s Salesforce AgentForce package is 85% complete despite authentication storage challenges, with the team targeting Tuesday delivery for our October Dreamforce showcase. This positions us to demonstrate real-time data activation capabilities to enterprise customers while creating a scalable model for future partner integrations.

## **This Week\'s Progress**

### **Key Momentum Areas**

Andres Perez delivered the complete API for Copilot launch, shipping the press release and enabling our internal sales team with targeted customer lists for Salesloft and Outreach beta programs. This marks the first time our sales team received actionable account lists rather than starting from zero, with Marcella Wong noting this as a significant improvement in our go-to-market execution. The launch establishes our new partner integration model where API access drives Copilot upgrades and increased consumption.

Sanyog Rai achieved 90% completion on getting engagement data into the GTM Data Model, successfully pushing email and calendar data through the infrastructure pipeline. Despite some testing issues discovered on stage, the team is working through final bugs with engagement data expected in production between midweek and end of next week. This foundational work enables the flow of provider ingestion data directly into our GTM system.

The team demonstrated strong cross-functional collaboration, with Andres leveraging Crossbeam data to identify mutual customers and provide sales teams with pre-qualified prospect lists including Copilot status and enterprise indicators. This data-driven approach to partner enablement shows how our integration capabilities can enhance internal sales effectiveness beyond just customer-facing features.

### **Goals & Progress**

**Salesforce AgentForce Integration**: Prateek Paikray\'s team reached 85% completion on the managed package development, overcoming initial access issues that caused delays. The primary remaining challenge involves Salesforce\'s text field limitations for storing encrypted access tokens, which the team resolved by implementing a 15-field splitting solution recommended by Salesforce. While not ideal, this approach will enable security review passage and package submission by the August 15th deadline.

**Custom Field Infrastructure**: Erica Fienman achieved 70% completion on custom field support, with testing revealing several bugs currently being addressed. The LRT information packet is due Tuesday, positioning this capability to unlock major blockers for early access customers who need to extend our GTM schema with their own custom fields surfaced in Workbooks.

**Partner API Ecosystem**: The Copilot API launch creates a template for future partner integrations, with Zapier as the next priority to migrate to OAuth endpoints before customer complaints arise from increased awareness. This systematic approach to partner enablement will scale our integration capabilities while maintaining proper authentication and usage tracking.

### **Strategic Challenges**

Salesforce\'s authentication storage limitations forced an inelegant workaround where access tokens must be split across 15 separate fields before encryption and storage. While Salesforce indicated they have a bug on their end for the preferred OAuth flow, they haven\'t prioritized a fix, leaving Prateek\'s team to implement this temporary solution. The team plans to build proper service account user logic in v1 to eliminate per-user authentication requirements, but this adds complexity to the current timeline.

The new API access model creates potential seat compression risks as partners like FreshWorks rebuild ZoomInfo UI functionality within their platforms, allowing multiple users to access data through a single integration. While this drives usage and puts pressure on our credit pricing model, it requires careful monitoring to ensure we\'re capturing appropriate value from enterprise customers who might circumvent individual seat purchases.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Andres discovered that \"Active Packages with ACV\" provides the most accurate field for determining Copilot customers, enabling precise targeting for upgrade campaigns. This insight came from working with Crossbeam data and cross-referencing customer status, providing a reliable foundation for future partner enablement and sales targeting efforts.

The team learned that providing pre-qualified prospect lists significantly improves sales team effectiveness, with this being the first time such targeted enablement was provided according to Marcella Wong. This approach of combining integration capabilities with sales intelligence creates compound value beyond just technical functionality.

Sanyog\'s work revealed the importance of building buffer time into testing estimates, as engagement data integration uncovered unexpected issues during stage testing. This learning will inform future sprint planning and help set more realistic expectations for complex data pipeline work.

### **Cross-Team Dependencies**

Our work with the Data Team on engagement table schema design continues to be critical for GTM Data Model success. Sanyog coordinated with the team to review engagement tables and address developer experience concerns around table joins and indexing, ensuring the schema supports both contact-to-engagement and engagement-to-contact query patterns that partners will need.

Collaboration with Lars on agent platform APIs remains essential for the AgentForce v1 version, where managed actions will point to new agentic platform endpoints rather than current API-based implementations. This dependency will become critical as we move from the current authentication-focused v0 to the full-featured v1 experience.

## **Looking Ahead**

Next week focuses on completing foundational deliverables while preparing for Q3 sprint planning and H2 epic refinement.

Prateek will finalize the AgentForce package by Tuesday and begin grooming epics for ZI-managed and custom-managed actions across Salesforce, HubSpot, and Dynamics. Andres prioritizes migrating Zapier to OAuth endpoints before customer complaints arise from the API announcement, while Erica completes custom field testing and the LRT information packet. Sanyog targets engagement data production deployment between midweek and week-end, establishing the foundation for provider data flow into GTM systems. These deliverables position the team to demonstrate significant enterprise value at Dreamforce while scaling our partner integration model across the ecosystem.

The team maintains strong momentum on strategic initiatives that directly impact revenue growth through Copilot upgrades, enterprise customer retention through custom field flexibility, and ecosystem expansion through standardized partner integration patterns.

*Source: Team 1-2-3 Operating Framework entries from July 21-25, 2025*

# **Copilot Experience Team Weekly Report - July 21, 2025**

## **Executive Summary**

Strong cross-team alignment achieved on unified experience strategy with clear technical direction established for dynamic profiles and CoPilot Pro onboarding. Ant Cuomo secured alignment with engineering leadership on chat v2 implementation while Adam Severance completed strategic planning for Day 1 user experience. Critical architectural decision made on data resolution approach that unblocks profile loading across platforms.

## **This Week\'s Progress**

### **Key Momentum Areas**

Ant Cuomo established comprehensive alignment on unified experience plan, making substantial progress on dynamic profiles that will deliver seamless UX across both main application and browser extension. This foundational work directly supports our goal of reducing user friction and context switching between platforms.

Adam Severance achieved full alignment with Sean and Ant on first-time user experience for CoPilot Pro, completing the strategic planning phase for both \"Aha moment\" delivery and Day 1 onboarding flow. His expanded vision for target account concepts represents a significant evolution in how we present prospect intelligence to users.

Technical architecture clarity emerged from Ant\'s session with Rowan, where the team decided on data resolution service approach over pure agentic implementation for page load profiles and extension functionality. This decision provides predictable performance characteristics while maintaining intelligence depth where it matters most.

### **Goals & Progress**

**Dynamic Profiles & Unified Experience**: Ant Cuomo\'s work is 50% complete with strong technical foundation established and cross-team alignment secured with Adam and Lars on chat v2 plan and artifacts approach. The seamless UX integration between app and extension now has clear implementation path, directly enabling our strategic goal of unified user experience across touchpoints.

**CoPilot Pro User Experience**: Adam Severance has completed 100% of the planning phase for CoPilot Pro\'s onboarding experience, with clear alignment established on first-time user experience flow and \"Aha moment\" delivery. The expanded target account concept moves beyond individual contact intelligence to comprehensive account-level insights, potentially reshaping how sales teams approach prospect research.

**Agentic Profiles Architecture**: Technical approach for agentic profiles across both SalesOS and CoPilot Pro is moving into detailed design phase following the architectural decision on data resolution service implementation. This approach balances response time with intelligence depth, ensuring consistent user experience while maintaining valuable insights.

### **Strategic Challenges**

Cross-platform consistency requires careful coordination as the unified experience implementation spans web application, browser extension, and mobile platforms. While alignment is strong, the technical integration points where user context must be preserved seamlessly need continued attention to ensure consistent experience delivery.

Performance versus intelligence trade-offs emerged during architectural discussions, with the team choosing data resolution service over agentic approaches for profile loading scenarios. This decision prioritizes user experience speed, but ongoing monitoring will be needed to ensure valuable insights aren\'t sacrificed for performance gains.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Target account evolution discovered through Adam\'s CoPilot Pro work reveals opportunities to expand beyond individual contact intelligence to strategic account-level planning. This shift could fundamentally change how sales teams approach prospect research, moving from contact-by-contact discovery to comprehensive account strategy.

Technical architecture clarity achieved through Ant and Rowan\'s collaboration on data resolution approaches provides crucial understanding of performance versus capability trade-offs. The decision to prioritize data resolution service for page load scenarios ensures predictable user experience while maintaining intelligence depth in appropriate contexts.

Cross-team alignment benefits demonstrated through strong coordination between Ant, Adam, Lars, and Sean on chat v2 and artifacts implementation. This early collaborative planning prevents typical integration challenges that arise when teams develop features in isolation, creating compound effects across workstreams.

### **Cross-Team Dependencies**

Our work with Engineering on chat v2 implementation continues to be critical for unified experience delivery. Lars and Adam have established clear technical specifications with the artifacts approach providing solid foundation for cross-platform consistency. The collaboration with Rowan on data resolution architecture ensures backend services can support the user experience vision without performance degradation.

## **Looking Ahead**

Next week focuses on transitioning from strategic alignment to detailed implementation planning, with comprehensive design reviews for agentic profiles across both SalesOS and CoPilot Pro platforms.

Ant will lead PRD and design review sessions for agentic profiles, ensuring technical specifications align with user experience goals across both platforms. Success means clear implementation roadmap with defined milestones, resource requirements, and integration points that maintain the unified experience vision. Adam will refine the Day 1 brief incorporating feedback from alignment sessions with Sean and Ant, establishing the foundation for CoPilot Pro\'s onboarding experience and setting clear expectations for user engagement metrics.

The team is positioned to deliver meaningful progress on unified experience goals with strong cross-functional alignment and clear technical direction established. Focus on user experience consistency while maintaining technical performance will drive measurable improvements in product adoption and user satisfaction.

# **Analytics Team Executive Roundup - July 25, 2025**

## **Executive Summary**

The analytics team is on track to deliver a comprehensive customer dashboard next week, with Nanxi Ge completing 80% of the integration work despite data size challenges. Key strategic insights emerged showing renewal accounts significantly outperform new accounts across all engagement metrics, with 10% higher CRM integration rates and 22% more AI feature adoption. Preetham Srinithi resolved critical amplitude attribute automation blockers and will deploy the solution to production by Wednesday.

## **This Week\'s Progress**

### **Key Momentum Areas**

Phoebe Mei\'s analysis revealed that renewal accounts demonstrate substantially higher engagement than new accounts, with 75% vs 65% CRM integration rates, 92% vs 85% provisioning rates, and 68% vs 54% AI feature adoption rates. This data provides clear direction for account management strategies and resource allocation priorities.

Inbal Kor completed comprehensive workbook AI analysis showing dramatic retention improvements, with AI users maintaining above 50% retention in week one while non-AI users dropped to 50%. AI workbook users create 3.5x more sheets and generate 2x more columns per sheet, demonstrating clear product-market fit for AI features.

Preetham Srinithi successfully implemented amplitude profiles feature with change data capture, resolving the historical event attribution challenge that has been blocking user behavior analysis. This breakthrough enables retroactive analysis of user engagement patterns across the entire customer lifecycle.

### **Goals & Progress**

**Dashboard Development**: Nanxi Ge advanced customer dashboard to 80% completion, integrating data from multiple sources including website intent, form completions, and campaign attribution. Despite encountering performance issues with large datasets requiring optimization strategies, the core functionality is operational and ready for stakeholder review next week.

**Data Infrastructure**: Preetham Srinithi resolved amplitude attribute automation challenges by implementing the profiles feature with change data capture enabled tables. Production deployment is scheduled for Wednesday following staging tests Monday and Tuesday, eliminating manual data pipeline maintenance.

**Customer Analytics**: Ferrell Taruwendaja shifted focus from churn data discrepancy investigation to target account analysis after identifying data source alignment issues. The decision to proceed with Phoebe\'s standardized dataset enables faster progress on high-impact conversion rate analysis.

### **Strategic Challenges**

Data source inconsistencies continue impacting analysis velocity, particularly around churn metrics where customer status differs between internal systems and Salesforce records. Ferrell spent significant time investigating discrepancies between growing accounts in internal tables and renewed contracts in Salesforce, highlighting the need for unified data governance protocols.

Large dataset performance creates bottlenecks in dashboard development, with Nanxi experiencing system crashes when loading comprehensive customer data. The team is implementing file-based joins for signal-to-action data and exploring CDP integration alternatives to maintain system stability while preserving analytical depth.

Technical complexity in amplitude integration required multiple implementation approaches before identifying the viable profiles solution. While Preetham resolved the core challenge, the extended timeline highlights dependencies on external platform capabilities that could impact future feature development velocity.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The renewal vs new account analysis exposed significant engagement gaps that weren\'t previously quantified, with renewal accounts showing 60% higher weekly active users and 22% more actions per user. This data validates focusing retention efforts on existing customers while investigating why new account onboarding produces lower engagement rates.

Dashboard definition alignment proved critical for stakeholder adoption, with Nanxi discovering that form completion metrics requiring 10+ submissions may not reflect actual usage patterns. Early stakeholder communication prevented downstream confusion and ensures metrics align with business objectives rather than technical convenience.

Amplitude\'s reverse ETL approach limitations became apparent through testing, revealing that historical event enrichment requires specific infrastructure configurations not available through standard implementation paths. This learning informs future data architecture decisions and vendor evaluation criteria.

### **Cross-Team Dependencies**

Our work with the EDNA team on amplitude table sharing remains critical for historical attribute analysis. Preetham requires specific permissions to share newly created change data capture tables from the ZI_Playground environment, with coordination needed early next week to prevent deployment delays.

The customer success team\'s account review meetings depend on Iran\'s analysis of account utilization changes over the past six months. While Iran will be offline next week, meetings are pre-scheduled and his comparative slides provide sufficient foundation for productive discussions about co-pilot engagement strategies.

## **Looking Ahead**

Next week focuses on delivery and stakeholder enablement, with three major milestones converging simultaneously.

Nanxi will complete dashboard development and launch comprehensive stakeholder onboarding including video documentation, 2-3 strategic insights presentation, and office hours for questions. This multi-channel approach ensures adoption while gathering feedback for iterative improvements. Preetham\'s production deployment of amplitude automation eliminates manual processes and enables real-time user behavior analysis. Phoebe begins developing the co-pilot analytics roadmap, synthesizing recent findings into prioritized opportunities for driving adoption across the customer funnel.

The convergence of completed infrastructure, validated insights, and strategic roadmap development positions the team to shift from foundational work to high-impact optimization initiatives, with clear data-driven direction for product and customer success investments.

*Source: Team 1-2-3 Operating Framework entries from July 21-25, 2025*
