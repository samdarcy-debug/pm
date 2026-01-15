---
id: learnings-2025-007
title: Q3 2025 Learnings Memo - Heather Ma
type: doc
status: approved
team: data
owner: '[[teams/data/_people/heather-ma]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
#### **Metric Alignment**



**CN Contact Contribution** (% of Closed Won Deals where buying

committee contact info influenced by CN): This measures how often

CN-sourced contacts appear in Closed Won deals through new records,

refreshed values, and newly assigned data.



**CN Intelligence Contribution** (Contributed Customers X Avg. \# of

Integrated Opt-in System Types per Customer): This metric tracks the

volume and diversity of data inputs (CRM, engagement tools,

collaboration tools) into our intelligence layer, a leading indicator

for more signals and recommendations.



#### **Key Learnings**



This quarter, I gained a comprehensive understanding of CN\'s data

collection and usage mechanisms through collaboration with a dedicated

architect. Previously, I couldn\'t clearly answer **what data we

collect, what we\'re missing, or how we use it** without consulting

multiple teams. I now understand that CN data usage operates on three

levels: (1) obtaining permission for a data source, (2) defining clear

usage, and (3) building collection pipelines.



To illustrate this framework: for contact data improvement (CN\'s

primary use case), we have permission and active pipelines for CRM

contacts (though only a few popular CRM types flow data into GTM Store),

but for Engagement tools like email signatures and calendar

participants, we only have frontend tiles without backend pipelines. We

also have permissions for Slack and MS Teams usernames, but no pipelines

or GTM Store integration since these tools currently only push

notifications. Opportunity data (used in Benchmark Insights)

demonstrates a different pattern: data exists in GTM Store but serves

on-demand analysis rather than feeding a destination database, so

traditional pipeline concepts don\'t apply. AI agents query directly

with eligibility filters.



We\'re building a ZI chat agent to ingest this knowledge and answer CN

data advisory questions.



#### **Hypotheses & Results**



**Hypothesis 1:** Developing a production-ready CN data-powered AI agent

would be straightforward



**Result**: Partially validated, with significant complexity uncovered.



Building a prototype with vibe coding was indeed quick and accessible.

However, the gap between prototype and production proved larger than

anticipated. Data connection issues emerged that vibe coding couldn\'t

resolve, and uncertainty around best practices persisted throughout

development. The critical question remains unanswered: how do we bridge

from a vibe-coded prototype to a production-ready agent without

dedicated engineering resources? This represents a scalability challenge

for PM-led innovation.



**Hypothesis 2:** Collecting eligible Opportunity data would be

straightforward with identified dependencies



**Result**: Invalidated - timeline significantly underestimated



We identified dependencies early (Corp IT team implementing May 2025

EULA version customer flags), established a plan, and expected

completion within the quarter. Reality proved far more complex: no

available Salesforce fields for implementation, extended cross-team

coordination cycles, and cascading blockers. Four months later

(October), we\'re still awaiting full implementation. While manual

workarounds exist, this validates a critical lesson: cross-team

dependencies consistently take 2-3x longer than estimated, regardless of

early planning.



**Hypothesis 3**: Raw CN Opportunity data would be sufficient for

generating insights



**Result**: Invalidated - data normalization is essential



CRM data messiness is well-documented, but the extent of normalization

required for meaningful insights exceeded expectations. Fields like deal

type, stages, dates, and other key attributes require data science

partnership to standardize before analysis. Simple LLM queries against

raw data produce unreliable results. Learning: Data collection is only

\[\~20%\] of the value equation- normalization and enrichment are

prerequisites for usability. Without this investment, most collected

data remains untapped potential rather than actionable intelligence.



#### **Go-forward Changes & Plan**



Maximize existing permissions first: Build pipelines for Calendar, Email

Signature, and Slack/MS Teams data we\'re already permitted to collect

before pursuing new sources.



Solve the prototype-to-production gap: Create a repeatable playbook for

taking PM-built AI agents from vibe coding to production without

dedicated engineering resources.



Normalize data at ingestion, not analysis: Partner with Data Science to

build data quality and normalization into CN pipelines upfront, ensuring

collected data is immediately usable.



Plan for dependency reality: Apply 3x timeline multipliers to cross-team

dependencies and build contingency plans earlier.



...**Leveraging AI**



*What is the most impactful tool / prompt / usecase you used AI for to

build better products? (use links/demos where you can)*



**Vibe Coding for AI Agent Prototyping**



I used AI coding assistants Cline to independently build a functional CN

data-powered AI agent prototype without engineering resources. This

compressed validation from months to days and revealed critical insights

that specs couldn\'t surface:



- Data reality check: Exposed that raw Opportunity data requires

  normalization before it\'s useful - LLMs alone can\'t handle messy CRM

  data



- Production gap visibility: Identified the significant delta between

  prototype and production-ready (data connections, best practices,

  scalability)



- Faster stakeholder alignment: Working demos secured buy-in and

  surfaced concerns far better than documentation



*How will you expand your use of AI in the coming quarter?*



**Productionize the ZI Chat-Powered CN Data Advisory Agent**



This quarter I finally understood the complete CN data ecosystem - what

we collect, where it flows, what we use it for, and where the gaps are.

This complex knowledge shouldn\'t live only in my head. Next quarter,

I\'ll finish building the CN Data advisory agent in ZI Chat to serve as

the central knowledge hub, enabling cross-functional teams to self-serve

answers like \"What CN data sources are available?\" or \"Why isn\'t

Email Signature data flowing yet?\" Goal: Scale CN architectural

knowledge across Product, Engineering, Sales, and CS teams.



**AI-Powered Data Quality Analysis**



Use AI to audit CN data sources at scale, identify normalization needs,

and generate quality scorecards before building pipelines---ensuring we

collect analysis-ready data, not just raw data. This addresses the key

learning that LLMs can\'t compensate for messy CRM data; normalization

must happen upfront.

