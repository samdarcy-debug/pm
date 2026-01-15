---
id: learnings-2025-047
title: Q3 2025 Learnings Memo - Marc Delurgio GTM Data Platform
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/marc-delurgio-gtm-data-platform]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **QBR - GTM Data Platform Team**



Lead: Marc Delurgio



This Quarterly Business Review (QBR) covers the Q3 , summarizing the

performance and strategic trajectory of the GTM Data Platform team.



**Metric Alignment**



Credits per Record under Management is the key front end metric that is

served by the GTM Data Platform. Everything the GTM Data Platform does

regarding 1st party data (GTM Data Model), 3rd party data (hosted on GTM

Store), Search, Match, and Unified Profile supports customers in driving

their business on the GTM Intelligence Platform, whether accessed

through apps, agents, or APIs.



#### **Key Learnings**



The top 3 priorities for all PMs should be Agent First, Agent First, and

Agent First. Disruption doesn't happen by taking a thing and making it

better. It happens by making something different. Agents are different,

and all apps, configs, and platform plays must think Agent First. If we

don't think Agent First, we will be disrupted by someone who does.



This is an incredibly exciting time to work in technology - a

fundamental shift in how humans interact with computers. Let's stop

copying app competitors and let's envision and build for an Agent First

world.



#### **Key Accomplishments**



- **GraphQL Query API Launch:** Linda Johannessen successfully released

  the GraphQL Query API v1 (internal), delivering the first stable,

  agent-ready interface for cross-entity GTM data. This architectural

  achievement was immediately validated by agentic platforms already

  testing MCP integration on top of the API.



- **Engagement Data Pipeline Completion:** Linda Johannessen supported

  Sanyog Rai in successfully onboarding Email ingestion for all

  Google/Outlook tenants and Calendar data for 1,000 Google tenants into

  the GTM Data Model. This foundational infrastructure is essential for

  downstream applications like the Copilot V2 Workspace chatbot, which

  demonstrated organic adoption by sourcing meeting information via

  GraphQL queries.



- **External API Commitment Secured:** Linda Johannessen obtained

  commitment from the External API team to support the end-of-November

  externalization of the Query API, removing a critical execution risk

  associated with GraphQL support timelines.



- **Improved Communication Cadence:** Marc Delurgio established the GTM

  Data Platform Monthly Review, which was so successful that it grew to

  encompass the entire platform team the following month. This monthly

  review addresses past communication gaps and establishes a predictable

  milestone cadence to celebrate successes (demos!) and align for the

  month.



#### **Go-forward Changes & Plan**



The **foundational work completed through Q3** positions us for faster

value delivery in the coming quarters. More teams can now onboard data

and signals. Adding new datasets and surfacing them across **Workbooks,

Copilot, and other applications** will soon be limited only by our

upstream data supply chain. With this foundation, we'll be able to

integrate our platform into **Agentic platforms and clients** more

seamlessly---expanding our reach, deepening customer value, and

strengthening our market position.



...



#### **Leveraging AI**



When I identified a critical gap in our roadmap---data

entitlements---that needed to be addressed before the GraphQL API could

reach general availability, I had to document it quickly. I met with key

stakeholders across various groups, and Brannen delivered a rapid-fire

overview of the multiple dimensions of our data entitlement services.

Fortunately, I had recorded the meeting in Chorus (there\'s no way I

could scribe at Brannen's verbal velocity), and I fed the transcript

into Claude along with some solution notes I had mapped out.



Claude gave me a [[really nice

spec]{.underline}](https://docs.google.com/document/d/1wcA5-Evr3bJvrd9seAry7uMtnU1teLfRvH7lg2_WiFU/edit?tab=t.0).

It took 30 minutes to tune and remove some cruft, but the result was

better than what I would have written myself (yes, I typed that out

loud!). The document was well-written, well-structured, and

thorough---and it took 30 minutes instead of \~4 hours!



*How will you expand your use of AI in the coming quarter?*



More of the above!

