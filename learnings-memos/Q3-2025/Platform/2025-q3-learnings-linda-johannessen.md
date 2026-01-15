---
id: learnings-2025-046
title: Q3 2025 Learnings Memo - Linda Johannessen
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/linda-johannessen]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



Unfortunately, we don't yet have a direct platform metric. The most

relevant drivers are Time-to-Data and % of Accounts with Active CRM/Core

Engagement, both of which ladder to Data ROI. The core value remains

delivering the Best GTM Data: canonical, connected, and joinable across

first- and third-party datasets to produce the best cut for each use

case.



Time-to-Data (Data ROI): Once data is published to the GTM Data Model

and Store, it automatically appears in the UI, becomes discoverable via

Metadata, and is queryable through GraphQL with configuration only.

Currently in staging, releasing in October.



\% of Accounts with Active CRM/Core Engagement (Enablement): Engagement

and CRM data are now stored, modeled, and accessed through the GTM Store

and GraphQL, providing one reliable, joinable surface that product teams

can adopt to lift activation.



Best GTM Data (Data ROI): Canonical schemas and relationships are

exposed through GraphQL, allowing teams to combine first- and

third-party data on demand and deliver higher-quality, use-case-specific

slices.



#### **Key Learnings**



Over the past quarter, we've built the foundation of a self-defining

GraphQL API that transforms how go-to-market data becomes usable. By

introducing schema introspection and automated metadata propagation,

we've removed the manual steps between data onboarding and API

availability. The system now expands on its own. When a dataset is

published, its schema becomes queryable within hours. This makes the

platform adaptable, fast, and inherently scalable across first-party and

third-party data.



We've seen how critical model quality, metadata consistency, and schema

governance are for enabling this flexibility. The same design principles

that make data instantly accessible also position us for the AI-native

future. GraphQL's composable format has proven especially powerful for

agentic use cases, giving us a strong foundation for MCP and tool-based

automation. This quarter confirmed that the platform can evolve as fast

as our data does, without engineering cycles as a bottleneck.



We've proven that we can build it and that it works, but we can't claim

success until our users say the same. My key takeaway is that our next

phase must focus as much on launch, growth, and adoption as on building,

ensuring that what we've created delivers measurable value in the hands

of our users.



#### **Hypotheses & Results**



**Hypothesis 1: A self-defining GraphQL API could make new datasets

instantly usable without engineering intervention.**\

Learning: The approach works. Once data is published to the GTM Store,

it flows through metadata and becomes queryable within hours. What takes

time now is not the system itself but the thought and design work around

schema readiness. We've proved the technical path, and the focus ahead

is on platform adoption. Adoption takes time, and our goal now is to

build momentum and confidence across teams.



**Hypothesis 2: Investing in canonical schemas and relationships would

simplify cross-dataset joins and speed time to value.**\

Learning: This has proven true. Each new dataset added to the model

connects to multiple existing ones, increasing the overall value of the

graph. As more data becomes available through metadata and GraphQL, the

connected value of every dataset grows. This network effect is becoming

visible as new sources come online.



**Hypothesis 3: A unified API layer could replace fragmented access

paths and make the platform more agent and AI ready.**\

Learning: The GraphQL layer is already proving this out. Its composable

format aligns naturally with MCP and tool-based workflows. The next step

is standardizing how teams expose their data as agent friendly surfaces.



**Hypothesis 4: Platform flexibility would accelerate adoption on its

own.**\

Learning: Flexibility is necessary but not sufficient. Adoption requires

targeted enablement, documentation, and internal evangelism.



#### **Go-forward Changes & Plan**



Next quarter's focus shifts from building core capabilities to driving

usage and reach.



A key priority is integration with Workspaces, enabling enrichment with

engagement data through the GraphQL API. We will continue close

collaboration with the Federated Search team to embed their capabilities

into the GraphQL API, ensuring unified access across data sources while

maintaining entitlement and suppression controls.



We will expand the reach of the GraphQL API and prepare it for public

release. We are introducing the MCP layer for both GraphQL and Metadata

APIs. Unlike the specialized MCPs developed by our apps teams, this MCP

is a thin, foundational layer that makes the APIs and their data

self-explaining. It guides agents on how to use the APIs, interpret

schemas, and understand metadata, while the metadata itself describes

the data it represents. The goal is to make both structure and content

discoverable, understandable, and ready for agent use with minimal

friction.



We will advance the Schema Registry and Metadata Service using TypeSpec

to unify schema definitions, add versioning, and improve consistency

across systems. This work strengthens the GTM Data Model and accelerates

dataset onboarding.



With the GraphQL and MCP foundation in place, the platform can evolve

quickly as data needs and the AI landscape continue to change.



#### **Leveraging AI**



This quarter, I built and deployed a local MCP on top of our

Go-to-Market Store APIs. Using it with Claude Desktop I can interact

directly with the data, ask questions, and explore relationships across

datasets. It's a practical tool that also expands how I think about

creating MCPs and agent experiences. The work deepens my understanding

of how to create value in an AI-native platform and what it takes to

make data and APIs usable by agents and people alike. AI is fully

integrated into how I work, learn, and live.

