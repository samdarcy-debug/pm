---
type: memo
author: Dominik Facher
topic: >-
  GTM Intelligence Platform and unified GTM data foundation (data management +
  AI workflows monetization)
tags:
  - data
  - credits
  - roadmap

---
# Executive Summary

As we evolve ZoomInfo from a 3rd party data provider to a data foundation, this memo outlines how we plan to unlock growth through new data assets and services.

In a typical upmarket deployment, we would sell a combination of user-licenses and credits, e.g. a company modeling their TAM would purchase 1M credits to get access to 1M company records for a year. 

This model has a ceiling. Once a company record is unlocked, we extract no additional value regardless of how much we help the customer. At the same time any given customer isn't going to significantly expand their TAM year-over-year, in other words we don't have an organic upsell path.

We need to stack more value on every record a customer unlocks. Our model needs to scale from access to data into monetizing "work" performed on their data. Instead of 1 credit per company record, we extract 4+ credits through services, workflows, and specialized data.

Our GTM Intelligence Platform is designed to put us in this position and this memo outlines the opportunity and investments to increase value per credit.

# GTM Intelligence expands our scope to the full GTM Data Foundation

The most significant change in our value proposition is the move from providing a single third-party data asset to providing a customer's unified (=unique) GTM data foundation.

Today, GTM execution stalls because incomplete, outdated and wrong data is scattered across a number of siloed GTM applications. A human or agent gets stuck at every step when there are 18 different "Cisco" accounts, orphaned contacts, broken hierarchies in the CRM, product data unmatched in the data warehouse, engagement data lost in people's inboxes.

This is an expensive problem to solve. Workday shared an 18-month roadmap with us focused entirely on untangling and unifying their accounts before they'd even consider incorporating something as basic as signals into their sales motions. Companies like ServiceNow, Uber, and Capital One have dozens of highly paid technical people dedicated full-time to this challenge. These are world-class GTM orgs spending millions annually just to maintain a coherent view of their customers & addressable market.

Solving this problem required building our GTM Intelligence Platform that treats customer's 1st party data as a first-class citizen. We need to unify, clean, and quickly onboard new data assets (ZI and Partners) to earn the right to execute & monetize a customer's GTM workflows.

This expands the value we deliver to a customer along the following dimensions:

| Value | Type | Examples | Status |
| --- | --- | --- | --- |
| **Company Contact Data Foundation** | 3rd Party | Company Record for Cisco | Live |
| **Signal Data** | 3rd Party | Buyers at Cisco are showing Intent | Live |
| **Vertical Datasets** | 3rd Party | Form 5500 filings at Cisco (Employee benefits, assets, ...) | Q1 |
| **Data Management** | 1st party | Merge 18 Ciscos into unified profiles with accurate account hierarchies and territories (dedupe, normalize, partition) | Focus Q2/<br>Q3 |
| **AI Workflows** | 1st + 3rd party | When inbound lead comes in, research, qualify and route. Create email response and track conversion. | Focus Q1/Q2 |
| **Partner integration** | 3rd party | Pull Reviews for a product/business from G2 or Yelp. | Focus Q3/Q4 |

Data management and AI workflows have the highest upside. They both represent a form of monetizing the work that we do on a given record as opposed to the raw data itself. Data management keeps the foundation clean, and AI workflows are executing outcomes. Both are evergreen, always-on systems.

Example: Every time a rep has a meeting with a customer, Data Management makes sure that the activity is attributed to the right opportunity (1 Data Management credit), participants are extracted and mapped to the buying group, contacts are created & enriched in the CRM (1+ data credits).

After the meeting, an AI workflow creates a follow-up email (1 AI credit), summarizes the meeting, refreshes the account plan (1+ AI credits) and updates forecast fields in the CRM (1 AI credit).

In this example, we've extracted several credits of value for a single company record during a single meeting, as an example of a high frequency & value workflow.
# Roadmap & Execution

Owning the data foundation earns us the right for GTM Execution to run through ZoomInfo and monetize. 

An estimate across 13k of our customers with CRM or engagement systems connected shows the scale of the opportunity for basic activity enrichment. Full potential annualized is >400 million credits (~240 million from contact & company extraction through meetings/emails and ~180 million from engagement tracking & attribution). We are already running this in the background to create the data foundation. It's our opportunity to monetize. 

We prioritize usecases that drive credit consumption due to high-value, high frequency and high data-foundation-need:

- **Q1: Plays. Maximize AI Credit Consumption** through agentic automation. When a signal fires, Plays triggers the action: research, prioritize, route, draft the email, update the CRM. This allows us to grow our AI credit consumption. Key usecases: inbound acceleration, outbound execution, account prioritization.
- **Q2: Scale Distribution:** We make our data foundation accessible everywhere sellers work. MCP and APIs connect to Slack, OpenAI, Anthropic, Vertex and Agentforce. More surface area means more credit consumption. Our [GTM.ai](http://GTM.ai) marketplace creates self-service access to accelerate growth
- **Q3/Q4: Enterprise Data Management. Monetize Cleaning 1P Data:** H2 brings our enterprise-grade data management services online. We run the basics in GTM Studio today but this set of upgrades allows us to monetize on every CRM update, meeting, activity that runs in GTM.
- **Ongoing: New Datasets.** We add net-new data throughout the year.  Modern GTM similar to finance will need to identify "alpha" that drives conversion above what the rest of the market is doing. New and highly custom datasets that are easy to operationalize is gold in this environment.

GTM does not have a machine readable data foundation or a data standard in a way that other successful B2B systems of record have. Jira standardized project tracking. ServiceNow standardized support. This is our way to monetize the GTM data foundation.

We expect to 4x credit consumption per record for customers fully on this platform. Whether we capture it depends on pricing and packaging as much as product.