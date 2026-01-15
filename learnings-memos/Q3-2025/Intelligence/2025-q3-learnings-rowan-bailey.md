---
id: learnings-2025-031
title: Q3 2025 Learnings Memo - Rowan Bailey
type: doc
status: approved
team: intelligence
owner: '[[teams/intelligence/_people/rowan-bailey]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- intelligence
related: []
---
#### **Metric Alignment**



**Semantic Data** \[Best GTM Data\]:



Processed semantic data (transcripts) for 16 Early Access GTM Studio

customers ahead of their onboarding---now live in production powering

Workbooks. Reduced cost per thread to \~8-9c with batch mode enabled.

We\'ve been making improvements to how we process emails, to be more

efficient (cost per thread), avoiding duplicate entities from being

extracted over multiple passes of the same thread, and the quality of

the knowledge graph overall. We\'ve also built a semantic data retrieval

agent, which can access the most semantically relevant entities +

relationships to a given query. This is now connected up to Workbooks,

Copilot and available in Claude via the Context Service MCP.



**Context Service** \[More Consumption\]:



Promoted from an internal service that powers our agents to a fully

packaged product---establishing ZoomInfo as core GTM context

infrastructure for any AI orchestrator. Successfully built, registered

and listed our public-facing MCP into Anthropic\'s MCP directory, with

38 internal users now equipped to demo at Dreamforce, supporting

search + enrich use-cases until the MCP Gateway is built out - targeting

mid-November, at which point we\'ll layer in the ability to query

Semantic data, and additional high-quality context sources via

specialized tools. Also took over the account / person brief pipelines,

cleared the processing backlog, and have a clear plan in place to turn

these into section-specific context enrichment pipelines in Q4. In a

similar vein, spent a decent amount of time reshaping the requirements

for GTM Config to align with how context acquisition should work moving

into Q4 and beyond.



**Signals, Scoring & Recommendations** \[Best Models\]:



Updated APS and Top Contacts models moved to production - top contacts

delivered 50x capacity increase with 75% latency reduction (4s to 1s

P99). Lookalike Accounts POC live covering 100K companies, with the full

production version, Lookalike Contacts and AFS scoring following in Q4.

On the signals side, still shipping new signals whilst also laying the

groundwork for a Signals MCP tool and custom signals via GTM Store +

CDC. Momentum POC also looking very promising - using engagement

patterns to predict strong relationships, won deals & renewals. We\'re

currently experimenting with folding in semantic data to see whether the

topics and sentiments covered in engagements provide more predictive

signal. This work will go a long way to earn the right to engage daily

with the AE/AM/Manager personas.



#### **Key Learnings**



*In 10 sentences or fewer: "What does everyone in the product

organization need to know that you learned about our customers, users,

or products this quarter?"*



- A focus to upskill / enable our GTM org on AI fundamentals, so they

  are prepared to sell these products successfully.



- We now need to devote as much attention to context acquisition as we

  do data acquisition - our AI experiences will fall down on the quality

  of the context we pass at query time.



- Some fundamentals need addressing in our core data model. E.g.

  \'Offerings\' as their own object that roll up to Account, with

  competitive relationships defined at the product level. This would

  open the door to rebuilding our models and recommendations at the

  product level, which is the level of detail customers expect.



- Our semantic data retrieval toolbox needs expanding - not all

  questions can be solved with a semantic search + relevancy reranking

  (we knew this already, but needs attention)



- Scaling Workbook requests to 1000\'s of rows per run causes issues as

  anticipated, and we should be mindful of scaling access before we

  scale our systems / capacity.



- The scope creep when designing a system that can answer any question

  and run any workflow is (naturally) huge---without clear constraints,

  teams become stretched and reactive rather than strategic. We could

  all do a better job of defining the capabilities we want to support,

  going deep on those use-cases and solving them really well, and

  communicating what we can and can\'t support via UI.



- As we start to promote tools externally over Q4, we need centralized

  tool management---promotion, descriptions, avoiding semantic overlap.

  This prevents orchestrator confusion and ensures customers paying for

  maximum access don\'t get degraded experiences from tool conflicts or

  unclear functionality at different abstraction levels.



- Related to above, we should be super selective over the number of

  tools we expose to our agents, to avoid complexity and improve

  test/retest validity.



- If you want to ensure the quality of the context feeding your agent,

  trace the data pipeline all the way back to the source, and identify

  opportunities for noise reduction or compression before it hits the

  orchestrator.



- Processing emails revealed far higher redundant content than

  calls---multi-pass email threading exposed immediate duplication

  issues that batch call processing masked. This fundamentally changes

  our entity extraction strategy - we require fail-safes to prevent

  duplicates, and classifiers to determine whether specific emails are

  worth processing entirely.



#### **Hypotheses & Results**



*Walk through 3-5 hypotheses you had going into the quarter and the

learnings for each. Be specific & nuanced.*



**Semantic Data:**



**Hypothesis:** Processing new emails iteratively as they come in

alongside the existing graph should yield higher quality entities than

batch-processing entire threads in one go.



**Result:** ⚠️ Mixed---Higher volume and higher quality of entities

processing emails this way, but also introduces duplicates as we\'re

effectively running a multi-pass setup. Learned that email content has

far higher redundancy than call transcripts; multi-pass threading from

day 1 exposed duplication challenges that batch processing masked. We

need a duplicate prevention / checker step before saving new entities to

the graph.



**Context Service:**



**\

Hypothesis:** Exposing ZI context & data tools in an external

orchestrator via MCP would produce comparable results to native

integrations into Copilot.



**Result:** ✅ Exceeded expectations---Claude as an orchestrator tends

to reason well over the tools, query them correctly, and produces good

results/artifacts where data is available. Positioned a new revenue

stream via AI credits & consumption-based pricing while establishing

ZoomInfo as infrastructure layer for GTM AI workflows. There is still

plenty of work to do here, and we\'ll need to maintain quality /

consistency as we add tools - but this is a very promising start.



**Signals, Scoring & Recommendations:**



**Hypothesis:** Momentum Score based on engagement volume & velocity is

a better predictor of an opportunity closing than traditional

stage-based forecasting.



**Result:** ✅ POC with data science (Tamiro/Nilesh) validated core

concept---that combining engagement velocity with additional factors

such as number of stakeholders, medium (call, email) is indeed

predictive. We are folding in semantic data next, to test whether

conversational topics prove more predictive than interaction frequency

alone in forecasting deal progression / relationship strength.



...



#### 



#### **Go-forward Changes & Plan**



*Outlook: Based on your learnings & insights, what will you prioritize

next quarter?*



**1. Scale Semantic Data Foundation** - Scale semantic data extraction

to handle new tenant onboarding with improved entity deduplication.

Upskill AEs/AMs/CSMs on proprietary semantic approach and competitive

differentiation. Expand the Semantic Data retrieval toolbox to provide

more efficient ways to narrow the search space, bias for recency and

handle compound/complex questions. Expand the GTM Ontology to cover 1st

and 3rd party sources, deprecate entity types that aren\'t adding value

to retrieval, and add new ones that might.



**2. Establish Context Service as Infrastructure** - Continue to develop

and position the GTM Context Service as market-leader for grounding GTM

AI workflows. Expand MCP Gateway capabilities mid-November to layer in

semantic data queries and specialized tools. Break the account & person

brief generation pipelines into dedicated ETL for each section, with

enrichment where appropriate and clear feedback to data producers for

any high priority gaps.



**3. Accelerate Predictive Intelligence** - Integrate models more

tightly across product suite---prioritize Momentum score production

deployment via Copilot Workspace. Continue enabling custom signals and

investing in underlying datasets from which we can derive high quality

signals/insights. Fold semantic data into Momentum POC to test whether

conversational topics prove more predictive than interaction frequency

alone.



...



#### **Leveraging AI**



- Claude Code is a beast, vibe coding to refine & communicate

  requirements works very well, everyone should be doing it.



- [[Langchain youtube

  channel]{.underline}](https://www.youtube.com/@LangChain/videos) has

  some great stuff on agents.



- [[Anthropic research]{.underline}](https://www.anthropic.com/research)

  always good reads.



- [[A helpful

  primer]{.underline}](https://blog.google/products/search/introducing-knowledge-graph-things-not/)

  for the power of semantic data & knowledge graphs from 2012, and why

  we should all be thinking about our data and context as a graph.



- I *would* like to carve out more time to keep up with the latest

  papers / research and how to fold some of those findings into what we

  are building here.

