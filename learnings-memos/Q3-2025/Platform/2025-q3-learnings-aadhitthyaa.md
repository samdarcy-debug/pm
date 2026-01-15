---
id: learnings-2025-038
title: Q3 2025 Learnings Memo - Aadhitthyaa
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/aadhitthyaa]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
## **[Metric Alignment & Business Impact]{.underline}**



### **Initiative 1: Advertising Platform**



**North Star: Total Ad Spend**



- **\$4.35M in Q3** (+144% YoY, +19% QoQ)



- Active advertisers grew to 204 (+14.6% since Q1)



- 5x improvement in contacts reach percentage through continuous

  optimization



- Predictive Clearing delivered 33% cost reduction while increasing CTR

  by 4.73%



### **Initiative 2: GTM Offerings Dataset**



**North Star: Admin Efficiency & Time-to-Market**



- On track for Q4 delivery to solve cold start problem



- Scaling pipeline to 25x capacity for Account Brief Generation



- Targeting 100% fill rate of Account Briefs for top searched companies

  to reduce sales friction



### **Initiative 3: Flywheel Identity Partners**



**North Star: Visitor Resolution Rate**



- Target: 10+ partners in 90 days, each contributing 10K+ unique monthly

  mappings



- Discovered data-for-data exchanges create exponential value vs. linear

  costs



- Self-serve automation will reduce onboarding from 40 hours to 5

  minutes (goal)



## **[5 Key Learnings]{.underline}**



**1. Agent Context Quality Beats Quantity** Overstuffed agent contexts

increased both error rates and costs proportionally. We discovered we

must be super selective about tool exposure - breaking endpoints into

discrete functions (company vs. person vs. features) improved both

performance and test/retest validity.



**2. Evals Frameworks Are as Important as PRDs** The evaluation

framework has become the critical handoff document between PMs and

engineering for agent development, serving as both the testing blueprint

and acceptance criteria - without it, we can\'t validate improvements or

catch regressions.



**3. Product-Level Granularity is Non-Negotiable** Customers expect

recommendations at the product/offering level, not account level.

Restructuring offerings as first-class objects that roll up to accounts

would unlock the precision our enterprise customers demand.



**4. Context Acquisition is the New Data Acquisition** AI experiences

fail without high-quality context at query time - we discovered we must

invest as heavily in context infrastructure as we do in data pipelines.



**5. Early Engagement Breaks the 3-4 Month Adoption Curve** After

learning in Q4/H1 that features typically peak in months 3-4 regardless

of launch excitement, we applied this insight to video ads - embedding

CDMs/CSMs 9 months pre-launch and using Pathmatics data for customer

targeting. Result: adoption spiked by month 2, already exceeding targets

and driving Connected TV requests from enterprise accounts.



## **[Hypothesis Validation]{.underline}**



### **Hypothesis 1: Comprehensive context would improve agent accuracy**



**Expectation:** Providing agents with all available tools and data

endpoints would enable complex query handling\

**Result:** Reversed our thinking completely. Overstuffed contexts

increased error rates and costs proportionally. Breaking endpoints into

discrete functions and limiting tool exposure dramatically improved both

performance and test/retest validity.



### **Hypothesis 2: Account-level data would be sufficient for enterprise GTM motions**



**Expectation:** Sales teams primarily sell at account level, so

account-level briefs would meet their needs\

**Result:** Fundamental rethink required. Customers consistently expect

product/offering-level granularity with competitive relationships

defined at product level. Driving complete restructuring of our data

model.



### **Hypothesis 3: Predictive Clearing would require trade-offs between cost and quality**



**Expectation:** Reducing bid prices through algorithmic optimization

would likely decrease ad relevance or reach\

**Result:** Win-win validated. 33% cost reduction on both clicks and

CPMs while CTR increased 4.73%. The algorithm doesn\'t just save

money---it finds better matches, proving inefficiency was driving higher

costs.



## **[Go Forward Plan]{.underline}**



### **1. Complete GTM Config Dataset Delivery**



Ship datasets to GTM Store with APIs for persistent UI and GTM Config

agent consumption. This directly addresses our learning that context

acquisition is as critical as data acquisition---essential

infrastructure for high-quality AI experiences at query time.



### **2. Launch Offerings as First-Class Objects**



Create the offerings dataset to enable product-level granularity in

recommendations. Q3 taught us account-level data isn\'t

sufficient---customers need product-level precision for competitive

intelligence and targeting.



### **3. Stabilize Account & Person Brief Pipelines**



Enhance pipeline reliability and quality to maintain 100% fill rate for

top companies. With brief quality proving more valuable than quantity,

we\'re doubling down on accuracy and completeness over pure volume.



### **4. Accelerate Advertising Revenue Impact**



Focus on top 3 projects with maximum revenue/retention impact:



- **Beeswax DSP Integration:** Expand programmatic reach beyond Trade

  Desk



- **Connected TV:** Respond to enterprise demand following video ads

  success



- **Conversion Tracking Improvements:** Close attribution loop to prove

  ROI



### **5. Ship Self-Serve Partner Onboarding**



Build lightweight onboarding flow to scale from 5 to 100+ flywheel

partners in Q4. Reducing onboarding from 40 hours to 5 minutes will

unlock the compound network effects validated in Q3.



## **[Leveraging AI]{.underline}**



- V0 for rapid prototyping



- Claude for documentation generation



- Langchain YouTube channel for agent development expertise

