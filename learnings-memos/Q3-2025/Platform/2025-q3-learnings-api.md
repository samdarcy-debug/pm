---
id: learnings-2025-041
title: Q3 2025 Learnings Memo - API
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/api]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



My work has contributed the Integrations driver metrics of % of Accounts

with Active CRM and to a lesser extent the More Consumption North Star

metric of Credits per Record under Management.



In both cases, my team\'s work to improve our API capabilities has

expanded the number of customers who can link external tools to

ZoomInfo, and the types/volume of ZI data that can be pulled into those

external tools.



#### **Key Learnings**



The biggest thing I've heard over and over (not surprisingly) is that

figuring out how to ensure our features and tools can work well AI and

Agentic Tools. Doing this properly will require infrastructure upgrades

to accommodate the different style and volume of usage that these

agentic tools drive. Security will be a critical enhancement as these

agentic tools are notorious for finding new ways to exploit access

controls and other restrictions. There will be a lot of cost associated

with doing this properly, but the cost of doing it wrong could be

significantly higher.



#### **Hypotheses & Results**



Hypothesis: Most customers will require significant motivation to

migrate existing tools over to the new OAuth API



Results: Hypothesis confirmed. A few customers have migrated just due to

OAuth differentiator, but the majority of customers have chosen to keep

their integrations on the legacy API. We will continue to enhance the

feature set in the new API as the "carrot" to get people to migrate, and

once we have full feature parity we will announce an end of support date

as the "stick" to ensure everyone migrates.



Hypothesis: The existing authentication gateway built for ZI API will be

sufficient for releasing MCP tools for agentic access.



Results: False. The existing gateway will not work for MCP tools at

scale. The security requirements, usage limits, and authentication

methods are all significantly different and will require the creation of

an updated gateway before additional tools can be released.



#### **Go-forward Changes & Plan**



In the coming quarter we are focused on releasing an authentication

gateway to support the release of additional MCP tools, adding support

for GraphQL to the ZI API Platform, and releasing Version 2.0 of the

Data API.



#### **Leveraging AI**



In the past quarter I mostly used Claude to test the MCP capabilities we

were launching to ensure they worked properly. As my team is focused on

building out platform tools the opportunity to use AI to design these

tools is more limited than with front end features, but I will continue

looking for ways to leverage AI in designing the updates we are

prioritizing for next quarter.

