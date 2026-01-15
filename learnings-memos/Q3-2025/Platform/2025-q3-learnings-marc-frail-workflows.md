---
id: learnings-2025-048
title: Q3 2025 Learnings Memo - Marc Frail Workflows
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/marc-frail-workflows]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



**Records Processed:** The Workflows app processed 125M records in

September 2025, a 7.7% increase from 116M in May, while Workflows

infrastructure ("headless workflows") processed several times that on

behalf of other ZoomInfo apps like Copilot and GTM Studio: 504K

September, up from 191M in May.



In Q3, we kicked off a roadmap to transform Workflows from a limited

export tool for ZoomInfo companies and contacts for 11 integrations, to

a general-purpose automation infrastructure that can handle any GTM data

or API across ZoomInfo products by year-end. We expect this to drive

greater consumption in 2026 as general-purpose automation unlocks more

use cases.



#### **Key Learnings**



**From Linear Flows to Extensible Orchestration**



Over the past several months, I've learned that the power of automation

isn't in chaining triggers and actions --- it's in creating an

orchestration layer that can flex and scale. I've shifted my mindset

from building "workflows" to building *systems* that enable others to

orchestrate across data, tools, and outcomes.



Extensibility --- through composable steps, reusable actions, and

support for external triggers or outputs --- has become the north star.

It's no longer about hard-coding a sequence; it's about designing a

framework that others can build upon.



**Extensibility Scales, Integrations Don't**



I've come to appreciate that every new integration we build adds

short-term value but long-term complexity. The more sustainable approach

is to make the platform itself extensible --- letting users or partners

define their own actions, inputs, and authentication.



That means focusing on primitives like authorization, mapping, and

transformation instead of bespoke one-offs. Building an extensible

system gives us leverage --- every new capability can scale horizontally

instead of being rebuilt per integration.



**Balancing Deterministic and Agentic Automation**



A big realization has been understanding the balance between

deterministic and agentic workflows. Deterministic flows create trust,

governance, and predictability --- things RevOps users depend on.

Agentic workflows, on the other hand, introduce flexibility and

reasoning that are better suited for GTM Studio or Copilot Pro use

cases.



The lesson is that both have a place. It's not about choosing one; it's

about applying the right model for the right context and making sure

they coexist within the same orchestration fabric.



**Data as the Backbone of Automation**



Everything in automation ultimately comes back to data. It's not enough

to move data from one place to another --- the system needs to

understand structure, schema, and transformation rules dynamically.



Supporting operations like field mapping, coalescing, and conditional

logic has made it clear that data consistency is what gives workflows

power and reliability. That's why export schemas, payload

standardization, and webhook-based extensibility have been a major

focus.



**UX is the Real Differentiator**



I've learned that simplicity on the surface hides enormous complexity

underneath --- and that's where good design comes in. The success of

automation tools depends on how clearly users can express intent.



AI-assisted configuration, visual branching, and clear feedback loops

all play a role. The goal isn't just to make something "low-code," but

to make it intuitive --- something that feels effortless while still

powerful.



**Thinking in Systems, Not Silos**



One of the biggest mindset shifts has been thinking beyond product

boundaries. Workflows, Workbooks, Copilot Pro, UNIE --- they're all part

of the same ecosystem.



Every design choice, from how we handle authorization to how we emit

events, has ripple effects. Building alignment across these systems ---

and designing for shared infrastructure like the Global Event Bus --- is

what enables a truly unified platform.



**Automation as the Connective Tissue**



Ultimately, I've started viewing automation as the connective layer of

our GTM ecosystem. It's what brings together data, enrichment, CRM,

analytics, and activation into one cohesive loop.\

This perspective reframes workflows from "process automation" into

"platform orchestration." The goal isn't just to automate tasks --- it's

to enable seamless collaboration between systems, data, and people.



#### **Leveraging AI**



Over the past few months, I've increasingly leaned on AI as a way to

compress the time between idea and alignment. What used to take days of

back-and-forth between Product, Design, and Engineering can now happen

in a single working session. By using AI to turn rough requirements into

tangible prototypes --- whether that's a mocked API schema, workflow

diagram, or UX flow --- I can validate assumptions faster and anchor

conversations in something concrete. This has transformed how I

collaborate across teams: PMs can now articulate intent visually and

interactively, enabling Design to refine sooner and Engineering to weigh

in earlier. The result is tighter feedback loops, fewer revision cycles,

and a shared clarity that accelerates decision-making and delivery.



Example Use Case:



[[Smart Builder Feature for Data Connectors

(WIP)]{.underline}](https://dozi-staging.zoominfo.com/prEnv/PR-176/smart-action-builder/latest/)



Ability to:



1.  Create Data Connector Manually (Advanced Power User)



2.  Create from the Smart Builder



    a.  Post a CURL command



    b.  Let us parse a Developer Portal (Not Functioning yet)



This will supercharge how we at ZI can utilize no-code features to

scale:



1.  Supercharge the ability to create a robust library of the most

    common integrations for GTM Automation



2.  Enable internal teams to register Actions



3.  Scale Partner Enablement

