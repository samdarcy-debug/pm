---
id: learnings-2025-040
title: Q3 2025 Learnings Memo - Andres Perez
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/andres-perez]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



1.  **Active Integrations:** the team has made improvements to the

    import pipeline to avoid import issues for CRM, and has added GTM

    Engagement-sourced Contacts (Accounts next) to allow for persisting

    a greater volume of Email and Calendar records. Additionally, we

    have partnered with ROI and other CRM-dependent teams to onboard

    customers with complex setups to use our new tooling, including

    import field mapping and import rules.



2.  **Credits per Record under Management:** The team is onboarding more

    credit consumption from partners (Salesloft, Outreach,

    [[Clay.com]{.underline}](http://clay.com), Chili Piper, Agentforce)

    and more ways to export (Cloud Data Shares to Snowflake and

    Databricks, in production but releasing in November. **However, this

    metric is not being populated in the North Star doc, and our Records

    under management methodology needs to improve to cover Cloud Data

    shares/DaaS. Additionally, we need to start charging "Action"

    credits for partner queries to benefit from more partner consumption

    when data RUM stays** **flat.**



#### **Key Learnings**



1.  Our legacy products are causing a brain drain on the team and

    migrating customers to our new products will open up new consumption

    (AI credits) while ensuring we only build/maintain our new flagship

    products.



2.  We are afraid of moving from "Revenue through Obscurity" to "Revenue

    through value". We prefer to sell data cubes because we worry that

    credits, which are not priced to the right value we offer today and

    are mostly limited to data, wont be fully consumed.



3.  We move faster when we use the same infrastructure. Copilot chat

    brought in the GTM DM meetings in a week, and now has access to all

    customer data from a single query API.



#### **Hypotheses & Results**



1.  **Hypothesis:** We can speed up crm import frequency much faster

    than 48 hours using our Single Import Pipeline.



    a.  **Result: 5K+ tenants importing every hour**, with the other

        \~10K importing every 3 hours.



2.  **Hypothesis:** Customer CRMs are missing many of the contacts they

    are engaging with.



    a.  **Result: 270k contacts created in GTM DM per week** across all

        active importing tenants.



3.  **Hypothesis:** Engagement to CRM data linking and virtual CRM

    creation is a major feature to attract customers and partners to use

    GTM DM



    a.  **Result: ServiceNow and Adobe have both been interested** from

        a partner perspective and noted that they dont have any

        capability like this. We also **continually get requests from ZI

        Sellers to sell SetSail and AAT**, validating the use case

        further. We will monetize through querying GTM Engagement

        sourced Contacts/Accounts, as well as through writeback either

        via GTM Studio Data Management or GTM Studio Plays.



#### **Go-forward Changes & Plan**



Focus on making every important use case work in GTM Studio and Copilot

Workspace from a Platform perspective, while stopping new development on

legacy products and instead focusing on migration paths.



#### **Leveraging AI**



PRDs are dead - we should use prototypes only (other than volume,

backend nuance)\

Example: Embedding Remote/Client MCP in addition to providing out of the

box API tools/endpoints



https://zoominfo.slack.com/archives/C01NA8B3R28/p1751031790817609?thread_ts=1750962995.413159&cid=C01NA8B3R28



In the coming quarter, expect to create more agents, like the

in-progress field mapper. Getting it to work so far has not been easy,

but the no-code functionality on the way will make it more user-friendly

for PMs.

