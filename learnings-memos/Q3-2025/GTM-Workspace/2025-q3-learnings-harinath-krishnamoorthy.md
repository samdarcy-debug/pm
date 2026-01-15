---
id: learnings-2025-028
title: Q3 2025 Learnings Memo - Harinath Krishnamoorthy
type: doc
status: approved
team: gtm workspace
owner: '[[teams/gtm workspace/_people/harinath-krishnamoorthy]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- gtm workspace
related: []
---
#### Metric Alignment



**Converting Actions per User per Month:** Measures Intent & AFS user

engagement depth by tracking how many meaningful actions (exports, saves

to CRM, workflow triggers, etc.) each active user takes monthly



##### Driver



**% of Accounts with Active CRM:** Actively advocating CRM connectivity

as gateway to AI-powered account discovery - customers connecting CRM

unlock both \"who to target\" (AFS) and \"what topics to track\" (Intent

Recommendations) based on their actual win patterns, transforming

prospecting from guesswork to data-driven expansion



*(yet to measure metric influenced by Intent, AFS)*



#### Key Learnings



1.  **Customer interviews(UXR) revealed unanimous pain points in Intent

    -** all 10 customers across \$836K to \$5.2B revenue range cited

    lack of transparency (100%) in Intent Signal, and signal quality

    concerns as primary barriers to Intent adoption -

    [[LINK]{.underline}](https://docs.google.com/document/d/1NG9cP-A4SJFmMTnaCKcvpW5_xMUSbwAPQDyMQUQiRyk/edit?tab=t.ufrsnkardubl)



2.  **\"Person-level intent\" requests mask the real problem** - every

    customer asked for individual identification despite legal

    challenges, but deeper probing revealed they actually need better

    context about **WHY companies appear** and WHICH role/department was

    searching, not literal person names.



3.  **"Intent Technical Debt"** - Legacy hardcoded entitlements and

    limit checks in Intent codebase (accumulated from rapid feature

    shipping) create manual engineering dependencies for provisioning

    teams when creating new bundles, slowing go-to-market and increasing

    error risk.



4.  **Custom Intent Topic lifecycle management \$1M+(approx) annual

    revenue leakage** - discovered that customers who create custom

    topics continue receiving signals even after contract expiry or

    non-renewal, with no automated deprovisioning; given custom topics

    represent \$10M+ annual revenue stream, this manual process creates

    estimated \$1M+ revenue leakage annually



5.  **Intent Topic Purchase across 44,087 Sales customers shows 70/25/3

    pattern:** 70.8% use ≤10 topics, 25.4% use 11-25 topics (core base

    for account management), 3.8% use 26+ topics (high-value with top

    0.74% using 100+ topics representing strategic revenue

    concentration)



6.  **Strategic Accounts Drive Disproportionate Value:** Top 0.74% (332

    accounts using 100+ topics) likely represent majority of Intent

    revenue



7.  **Geographic and segment patterns reveal targeting opportunities** -

    MidMarket dominates across all intent users. MidMarket \> SMB \>

    Enterprise



8.  **AFS Customization** - Customer are looking to customize the AFS

    output and also looking for way to influence the parameter which

    model learns, only see the account matters to them in their Sales

    territories



#### Hypotheses & Results



### **Hypothesis 1: Customer Pain Points Are Universal Across Segments**



**Hypothesis:** Intent pain points would vary significantly across

company size, industry, and use case, requiring segment-specific

solutions.



**Test Method:** Conducted customer interviews spanning \$836K (ArcaSys)

to \$5.2B revenue (Juniper Networks) across diverse industries:

cybersecurity, education, networking, distribution, marketing services -

[[DETAILED

DOC]{.underline}](https://docs.google.com/document/d/1NG9cP-A4SJFmMTnaCKcvpW5_xMUSbwAPQDyMQUQiRyk/edit?tab=t.ufrsnkardubl)



**Result:** **VALIDATED**



**Universal Pain Points (100% of Customers):**



1.  **Lack of Transparency:** All customers want to know WHY companies

    appear in intent results



2.  **Person-Level Intent Demand:** All requested individual

    identification (despite legal challenges)



3.  **Signal Quality Concerns:** All questioned whether intent signals

    represent real buying behavior



**Learning:** Pain points are remarkably consistent regardless of

company size or industry. This validates building universal transparency

and explainability features rather than segment-specific solutions.



### **Hypothesis 2: Admin Portal is managed by Ops and Admin Team**



**Hypothesis:** Common product assumption that Intent admin portal is

managed by operational or administrative roles would be validated

through user data analysis.



**Test Method:** Analyzed job titles across Intent page in Admin portal

through amplitude events:



**Result:** **ASSUMPTION COMPLETELY WRONG**



**Actual User Distribution:**



- **Marketing Leadership:** 55.8% of Marketer Topic users



- **Sales Leadership:** 30% of Sales Topic users



- **Executive Leadership:** 29.5% (Marketer) and 30% (Sales) are

  business owners/C-level



- **VP+ Level:** 50% of all users



- **C-Suite:** 30% direct involvement



**Learning:** Intent admin portal users are strategic decision-makers,

not operational staff. This fundamentally changes product requirements -

we need executive-level dashboards, strategic insights, and

decision-support features rather than configuration complexity. Platform

must shift from operational tool to executive platform.



### **Hypothesis 3: Intent Infrastructure Technical Debt Creates Provisioning Bottlenecks**



**Hypothesis:** Legacy hardcoded entitlements and limit checks in Intent

codebase (accumulated from rapid feature shipping) create manual

engineering dependencies for provisioning teams when creating new

bundles, slowing go-to-market and increasing error risk.



**Test Method:**



- Audited Intent provisioning workflows with RevOps and provisioning

  teams



- Identified hardcoded entitlements requiring code changes for each new

  bundle configuration



- Documented manual intervention points blocking self-service

  provisioning



**Solution Implemented:**



- Partnered with RevOps team to design proper entitlement framework



- Hardcoded logic to dynamic entitlement and limit check system



#### Q1 2025 Quick Rewind



Building on our H1 roadmap and [[Q1 learning memo

2025]{.underline}](https://docs.google.com/document/d/17WJnaGVo2CFSmy0_3PtZqfgjMJucPdURV_syYJdp-ZQ/edit?tab=t.altayem9xk5s),

I have successfully delivered following features



+---------------+------------------------------------------------------+

| **Item**      | **Description**                                      |

+---------------+------------------------------------------------------+

| **Intent      | Intent Recommendation is available to Copilot and    |

| Phase 1**     | ZIM customer in admin portal - generates weekly      |

|               | recommendation                                       |

+---------------+------------------------------------------------------+

| **Intent      | Intent Recommendation can be generated by uploading  |

| Phase 2**     | Sales, Marketing Brief - this would be helpful for   |

|               | customer who don't have CRM and customers entering   |

|               | new segment                                          |

+---------------+------------------------------------------------------+

| **Intent      | Ability to select multiple Intent Topics, Intent     |

| Advanced      | Location in Advanced Search for better targeting     |

| Search**      | using Intent Signal                                  |

+---------------+------------------------------------------------------+

| **Account Fit | Ability to filter account or opportunity in CRM by   |

| Score**       | introducing date filters                             |

|               |                                                      |

|               | Functionality to download the data uploaded by the   |

|               | customers along with matched company status which    |

|               | provides transparency what data went to model        |

+---------------+------------------------------------------------------+

| **Prioritize  | Introduced Campaign and Account Level Campaign       |

| Package**     | metric for Salesforce CRM customer which was highly  |

|               | requested feature among customers and sync status    |

+---------------+------------------------------------------------------+

| **Prioritize  | Prioritize Package expanded to HubSpot CRM, 400      |

| Package**     | customers gets direct benefit through single click   |

|               | activation                                           |

+===============+======================================================+



#### Go-forward Changes & Plan



#### 1. Persona-Based Intent in Copilot & GTM Studio



**Rationale:** Persona analysis revealed 55.8% Marketing Leadership, 30%

Sales Leadership, 14.4% RevOps need role-specific intent signals



**Deliverables:**



- Frontline seller enablement with Workbook/Workspace integration



- Persona-based filtering for AEs, SDRs, CSMs



- Redesigned intent discovery flow based on persona insights



- Role-specific default configurations



**Success Metrics:**



- Increase intent filter usage



- Measure persona-specific engagement rates



**2. Intent Recommendation - Phase 2 Enterprise Focussed**



**Rationale:** Current Intent Recommendation serves single-product

Copilot customers with CRM integration; enterprise segment blocked by:

multi-product portfolio needs, CRM integration resistance and (4)

competitive migration friction (2-3 week manual keyword mapping).



**Deliverables:**



- **Multi-Product Configuration:** Product-level recommendation engine

  supporting separate Intent topic sets per business unit/offering



- **Flexible Data Integration:** Secure CSV upload alternative to CRM

  integration for security-sensitive/non-CRM enterprises



- **AI Feedback Loop:** Human-in-the-loop refinement: customer feedback

  automatically improves future recommendations



- **Competitive Migration Assistant:** Automated keyword-to-topic

  mapping for 6sense/Demandbase migrations via CSV bulk upload



**Success Metrics:**



- Enable 100+ enterprise customers



- Reduce setup time from 2-3 weeks (CRM) to same-day (CSV)



- Increase competitive win rate vs 6sense/Demandbase



- Improve recommendation relevance



#### 3. Intent Type Consolidation - Account Level Intent



**Rationale:** Fragmentation across 6+ intent types creates customer

confusion and data discrepancy issues



**Deliverables:**



- Migrate all Copilot customers from Legacy Intent → Account Level

  Intent



- Deprecate redundant intent variations



- Establish one core intent types as single source of truth



- Update all documentation and training materials



**Success Metrics:**



- Eliminate \"data discrepancy\" support tickets by 80%



- Improve data consistency scores across platforms



- Reduce customer confusion measured through support ticket analysis



#### 4. Custom Intent Topic Lifecycle Management & Revenue Protection



**Rationale:** \$1M+ annual revenue leakage identified from customers

receiving custom topics beyond contract entitlement; \$10M+ total custom

topic revenue requires systematic protection



**Deliverables:**



- Automated lifecycle management system with contract-based access

  control



- Package-level entitlement enforcement (3 for Copilot Enterprise, 25

  for ZIM Demand, 100 for ABM Lite, unlimited for ABM Enterprise)



- Automated deprovisioning on contract expiry or non-renewal



- Customer communication workflow for expiration notifications and

  renewal options



- Utilization and revenue attribution dashboard for finance visibility



**Success Metrics:**



- Recover \$1M+ annual revenue through proper entitlement enforcement



- Reduce AM/CSM manual overhead by 80% for topic lifecycle management



- Achieve \<5% exception rate requiring manual intervention



- Decrease infrastructure costs by deprovisioning unused topic



#### Leveraging AI - Current



**1. AI-Powered Product Intelligence Platform (MCP Server)**



- **Innovation:** Built custom Model Context Protocol (MCP) server

  creating \"ChatGPT for ZoomInfo Production Data\" - enabling natural

  language queries against live product metrics



- **Business Impact:** Transformed data access from \"submit ticket →

  wait for analyst → get dashboard → ask follow-up → wait again\" to

  instant conversational answers



- **Capability:** Ask any Intent product question in plain English; get

  immediate answers with supporting data



- **Example Queries Enabled:**



  - \"Which customer segments show highest Intent adoption? Why?\"



  - Ad-hoc analysis of customer segments and behavior patterns



  - Rapid validation of hypotheses against production data



  - Democratized data access for non-technical stakeholders



**2. Intent Keyword Migration Utility**



- **Tool Used:** Cline-powered prototype for competitor

  keyword-to-ZoomInfo Topics crosswalk



- **Impact:** Created functional migration utility enabling seamless

  6sense/Demandbase customer onboarding



#### Leveraging AI - Future



**Continuous Intent Recommendation Quality Monitoring**



- Deploy AI-powered recommendation quality analysis running weekly

  across all segments



- Automated precision scoring comparing recommendations against

  historical performance



- **Goal:** Catch quality degradation before customer impact; maintain

  quality thresholds



## Reference



+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

| Previous Learning Memo | [[1Q25 Learnings Memo-                                                                                                                            |

|                        | Harinath]{.underline}](https://docs.google.com/document/d/17WJnaGVo2CFSmy0_3PtZqfgjMJucPdURV_syYJdp-ZQ/edit?tab=t.altayem9xk5s)\                  |

|                        | [[Q4 Learnings Memo - Harinath                                                                                                                    |

|                        | Krishnamoorthy]{.underline}](https://docs.google.com/document/d/1Ty2i_IowMVQi_RS1FqAeh3Tsr6WvBAi14iCQZtyPSik/edit?tab=t.0#heading=h.du8rc28wk4sg) |

|                        |                                                                                                                                                   |

|                        | [[Q3 Learnings Memo -                                                                                                                             |

|                        | Harinath]{.underline}](https://docs.google.com/document/d/1gPeoF-s8r9l7TvrWlBF0lSzKWNA2TD2QXqOihGXoxeI/edit?tab=t.0#heading=h.du8rc28wk4sg)\`     |

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

| Intent User Interview  | [[User Interview - Intent - Phase                                                                                                                 |

|                        | 1]{.underline}](https://docs.google.com/document/d/1NG9cP-A4SJFmMTnaCKcvpW5_xMUSbwAPQDyMQUQiRyk/edit?usp=drive_web&ouid=105637355082790640372)    |

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

| Custom Topic           | [[PRD Custom Intent Topics Lifecycle                                                                                                              |

|                        | Management]{.underline}](https://docs.google.com/document/d/1oVNsJuID7JMAj-l0hGflp5K00wSZ7UUU5ylhG_v2NrM/edit?tab=t.0)                            |

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

| Intent Recommendation  | [[PRD - Intent                                                                                                                                    |

| PRD                    | Recommendation]{.underline}](https://docs.google.com/document/d/1QsRk4WxHwC0qMffgwCFTncuJjzmhPkXZB_2U-c6qnwQ/edit?tab=t.dxgy8ouxt63e)             |

+========================+===================================================================================================================================================+

