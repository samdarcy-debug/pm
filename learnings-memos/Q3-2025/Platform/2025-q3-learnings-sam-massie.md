---
id: learnings-2025-053
title: Q3 2025 Learnings Memo - Sam Massie
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/sam-massie]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### Metric Alignment



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



Despite a crowded field of workflow tools in the market, GTM automation

is still not a solved problem for our customers, and the opportunity is

still open.



VoC analysis shows 3,854 unique accounts mentioned workflows or

workflow-related topics (e.g. automation, manual processes, integration,

enrichment) in 15,797 conversions out of 22,180 total during the sample

period (Jan-Mar 2025), representing \$604M of ACV, showing pervasive

interest in streamlining GTM processes, alongside increasing record

volumes in Q3.



Strikingly, competitive workflow tools like Zapier, Workato, HubSpot

Workflows, and Apollo Workflows were rarely mentioned: just 0.5% of

conversations, almost by SMBs, with a majority mentioning Zapier.

Mentions of "agents" (specifically in the context AI) were even rarer,

with only 15 mentions.



Meanwhile, customers' top challenge remained integrations, mentioned

6,361 times, or 40% of all conversations, a trend that continued into

Q3. While some (17%) brought up missing integrations, a challenge we've

begun to address with extensible data connectors, the majority raised

challenges with "supported" integrations like Salesforce or RingLead.

Large enterprises got bogged down in lengthy approval or provisioning

processes, while other customers struggled with data management or

implementing logic that Workflows doesn't yet support.



All else being equal, revenue teams would prefer a single system for

their GTM automations, because the barriers - organizational, technical,

financial - to adopting and integrating tools remains high. To be this

single system, and keep up in an increasingly commoditized workflow

market, we need to quickly evolve our legacy Workflows product into a

general-purpose automation platform that can incorporate the full range

of GTM data and features in ZoomInfo and handle critical GTM workflows

with help from AI, backed by enterprise-grade controls and auditability.



#### Hypotheses & Results



**Hypothesis 1: Lack of available integrations is one of the key

barriers to greater adoption of ZoomInfo / GTM Studio / Workflows.**

True, but with qualifications. 40% of all workflow conversations (6,361

mentions) did mention integration challenges, making this the most

common pain point, but most mentions (83%) were of integrations we

already support (at least as workflow export destinations). Simply

offering a bigger library of export integrations is only one piece of

the puzzle; supporting the full range of GTM data and APIs for ourselves

and for vendors we already support is more important.



**Hypothesis 2: The main competitors to ZoomInfo Workflows are iPaaS

tools like Zapier and Workato or GTM-tool-specific workflow tools like

HubSpot Workflows and Apollo Workflows** False, from what we can tell.

Customers and prospects barely brought up competitor workflow tools at

all, appearing only in 0.56% of workflow-related conversations. The most

common mentions were Zapier, with 71 mentions, and HubSpot Workflows,

with 15 - mainly among SMB customers - and the rest only had mentions in

the single digits. Instead of adopting general-purpose iPaaS tools,

revenue teams seem to be falling back on trusted, if time-consuming

manual processes, or at larger enterprises, relying on in-house data

pipelines.



**Hypothesis 3: Support for AI agents is one of the most important

things we should be building.** Mixed bag. On the one hand, market

developments like OpenAI's recent AgentKit announcement point to rapid

growth of LLM chat products, with tools (APIs) as the model context

protocol (MCP) standard, as a new way to access GTM intelligence that

bypassing traditional UI-based SaaS products. This highlights the

critical importance of public APIs and MCP for Workflows, to be released

in October. But the value of "AI agents as steps in a workflow" is

unproven, and agents rarely come up in workflow conversations (just 15

mentions).



#### Go-forward Changes & Plan



Deliver on the Workflow automation H2 roadmap: evolve Workflows from a

limited export tool for ZoomInfo reference data only, to a

general-purpose automation infrastructure that can handle any GTM data,

and any API, for GTM automation use cases across ZoomInfo. Up-front

investment in this infrastructure this year will unlock a wide range of

GTM use cases next year. With automation infrastructure in place, we'll

be able to say "yes" to customer requests by default, without lengthy

dev cycles for any particular data point, action, or integration.



That being said, we won't chase full parity with industry-leading

automation/iPaaS tools Zapier or Workato; just parity for critical GTM

workflows. Feedback from our Strat customers like IBM also suggests that

investing in enterprise-grade governance, monitoring, and tracking in

the future will help make our solutions more appealing and stickier to

upmarket customers.



#### **Leveraging AI**



While CLine was useful for prototyping, I actually found that prompting

LLMs in ZI Chat directly often yielded a good-enough UI prototype in a

fraction of the time, without the headache of managing environments,

deployments, or losing my work when the environment changed.



Example 1: Redesigning workflow panel UIs, like the [[export

panel]{.underline}](https://zoominfo-chatbot-ui.zi-ext.com/content/d5b2d281-11ac-4fe4-9c18-9ee2160452e7)

→ this prototype from ChatGPT in ZI Chat helped Engineering and Design

to instantly grasp what otherwise could have a time-consuming

back-and-forth to hand-build and refine mockups.



Example 2:

[[functions]{.underline}](https://zoominfo-chatbot-ui.zi-ext.com/content/b88e2e09-de52-4430-b8ef-9ff669e8067c)

and [[conditional

logic]{.underline}](https://discoverorg.atlassian.net/wiki/spaces/~7120209fc333c5e5e5488299db9c28d2b61c6c/pages/202029106285/Conditional+Operators+Reference)

-\> I used Claude in ZI Chat to rapidly recombine options from across

existing products and industry best practices into consolidated guides,

saving me easily a week of work.



Finally, the VoC analysis tools allowed me to distill literally

thousands of customer conversations in a way that simply would not have

been possible without AI .



I will continue to use AI - a combination of CLine and Claude + Gemini +

ChatGPT custom prompts - to prototype product concepts and features and

help with engineering + design refinement. As a next step for the coming

quarter, I plan to try out pulling working ZoomInfo APIs into

prototypes, as I've seen my teammates do, for higher-fidelity

prototypes.



I look forward to using the new VoC microapp within ZI Chat, when ready,

to get more timely and targeted customer feedback.

