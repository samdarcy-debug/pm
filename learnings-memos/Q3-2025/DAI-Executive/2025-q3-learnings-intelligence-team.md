---
id: learnings-2025-002
title: Q3 2025 Learnings Memo - Intelligence Team
type: doc
status: approved
team: dai executive
owner: '[[teams/dai executive/_people/intelligence-team]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- dai executive
related: []
---
# **Quarterly Business Review (QBR)**



[[Adam Smith]{.underline}](mailto:adam.smith@zoominfo.com)



## **Intelligence Team --- Q3 2025**



The Intelligence team achieved production readiness of the Agentic AI

platform with 2 agents live in production, validated our platform

investment hypothesis with 8+ teams building agents, and reduced agent

development time from weeks to 24 hours. The team deployed a reusable

chat framework across Studio, Copilot Workspace, SalesOS and Chorus. We

launched our external MCP in Anthropic\'s directory with 50 GTM reps

enabled for Dreamforce demonstrations, and delivered Top Contacts with

50x capacity increase and 75% latency reduction.



Sustaining this momentum into 2026 will require executive alignment to

address dependencies. Specifically, we need PM headcount allocation for

Intelligence layer roadmap, and PMM resourcing under Derek Osgood to

build systematic last-mile delivery infrastructure from technically

ready to customer sellable. I also believe we should make an

organizational commitment to quality-over-velocity tradeoffs. This is

not a push to slow down but rather for conscious prioritization, drive

to completion and to a high standard before switching. Do less, do it

better, focus on the high leverage stuff.



**SECTION 1: Progress and Momentum Areas**



### **I. Production Agentic Platform & Team Enablement**



The platform investment enabled distributed team success across ZoomInfo

products this quarter. Lars Vedo\'s team shipped the production-ready

agentic platform including AI Action credits, multi-model support across

Anthropic, OpenAI, and Vertex AI, entitlements, agent-to-agent

communication MVP, MCP integrations, embeddable chat framework, and API

access. This infrastructure delivered immediate value as 8+ teams built

agents including SalesOS, Chorus, Workbooks, Copilot Workspace, Web

Search, Advanced Search, Marketing, and Research. Teams can now embed

chat frameworks and connect agents within 24 hours compared to the weeks

previously required.



Two agents reached production deployment this quarter. Lars Vedo and

Sean Walter launched Copilot Workspace on October 6th to internal

testing with approximately 1,000 sellers. The Chorus agent went live in

production, validating that the platform could support multiple products

simultaneously. This work now guides all teams building on the platform.



The SDK reduced the barrier for teams to build AI capabilities. Ryan

Stevens and the engineering team enabled teams to integrate agents

without requiring deep understanding of the underlying orchestration

complexity. The development velocity improvement from weeks to 24 hours

represents a fundamental shift in how quickly ZoomInfo can deploy new AI

features to customers.



### **II. Copilot Workspace---Zero to Production in One Quarter**



Sean Walter and Lars Vedo (not solely, but within my team) drove Copilot

Workspace from concept to customer-ready product in a single quarter.

The internal beta program with approximately 1,000 sellers provided

real-world feedback.



Ryan Stevens integrated the AI Action Credits system into the agent

runtime, enabling consumption-based billing and usage tracking. The

Platform team delivered the credits infrastructure and pricing

integration. Multi-model orchestration became operational across

Anthropic, OpenAI, and Vertex AI, giving the product resilience against

any single vendor\'s availability issues.



AI credits is a win for cross-functional collaboration (product,

platform, GTM). Working with Mark Harris in revenue, we aligned the

commercial model that now powers consumption-based billing across all

Intelligence products, including Workspace, Studio. This foundational

mechanism enables the business model shift we need for AI.



Ryan McMaster created a design system that enables consistent AI

experiences across GTM Copilot, Studio, and Workspace. This eliminated

duplicate UI development work and established patterns that other teams

now follow. The team resolved context compaction for messages exceeding

300K tokens, reduced P99 latency through Vertex enablement, and

implemented a demo mode toggle that allows sales demonstrations with

redacted data.



### **III. Context Engineering & External AI Positioning**



Danny Pan and Rowan Bailey processed semantic data for 18 Early Access

customers now live in production powering Workbooks. The team reduced

processing costs to approximately 18 cents per call transcript and 8-9

cents per email thread through batch processing optimization and

migration to Gemini Flash 2.5. Both represent substantial cost

reductions that make large-scale tenant onboarding economically viable.



Rowan Bailey shipped ZoomInfo\'s MCP to Anthropic\'s public directory

and enabled 50 GTM reps for Dreamforce demonstrations. The reps used

search and enrich capabilities directly in Claude desktop applications,

validating the portable intelligence strategy. The team established an

internal-to-external promotion path for tools using feature flags,

allowing selective access to capabilities before broad customer release.



The semantic data integration into GTM Studio for workbook creation

reached near completion this quarter. The remaining work is blocked by

GTM Studio team resourcing rather than Intelligence dependencies. This

integration will allow customers to query conversation intelligence as a

dataset alongside traditional ZoomInfo data. The team implemented

ReAct-based retrieval agents, improved knowledge graph quality through

duplicate entity prevention, and expanded the GTM Ontology to support

more sophisticated queries.



Carlos Nunez and Rowan Bailey demonstrated successful enrichment of

product offerings data using Google grounding. The team processed 10,000

companies for under \$100 in 30 minutes using BigQuery ML with Gemini

Flash 2.5. This experiment opened possibilities for competitor

relationship mapping, complementary technology identification, and

improved core company data.



### **IV. Predictive Intelligence & Model Performance**



Robyn Sablosky delivered transformation of the Top Contacts model this

quarter. The team achieved 50x capacity increase while reducing P99

latency from 4 seconds to 1 second, representing 75% latency

improvement. The production pipeline stabilized to support multi-hour

runs without performance degradation. This infrastructure can now

support scaled customer deployments without capacity constraints.



The team validated Lookalike Accounts covering 100K companies through

proof of concept work. Lookalike Contacts and the full production

version moved into Q4 roadmap planning. Srivatsa Marthi and the data

science team demonstrated a Momentum Score proof of concept that

predicts deal progression using engagement velocity, stakeholder count,

and interaction medium. The team is now exploring whether semantic data

integration can show that conversational topics predict outcomes more

accurately than interaction frequency alone.



After completing the architectural design for the GSO to GTM Store

connector, Srivatsa Marthi refocused his team on new signal development.

The work includes down-funnel signals, signals based on absence of

events, and contributory network-based signals. These areas align with

the emerging Pulses roadmap concept and had received limited attention

in recent months.



**SECTION 2a: Forward-Looking Challenges We Need to Solve to Unlock the

Next Level**



### **1. Resource and Organizational Bottlenecks**



**Specialized AI Talent Constraint**



The team faces a shortage of engineers capable of solving specialized AI

problems. These problems include agent architecture, evaluation

frameworks, agent decomposition, state management, and agent-to-agent

communication. Only a handful of engineers can work through these

problems end-to-end. Josh Mantovandi exemplifies this constraint. He

moved sequentially across web research agent development to agent

re-architecture for latency reduction to context retrieval optimization

because few others could solve any of these problems completely.



This constraint forces the roadmap to execute in shallow mode rather

than excellent mode. All initiatives progress but few reach

production-quality polish. The quality gaps now surfacing in Copilot

Workspace user feedback trace directly to this velocity-over-excellence

dynamic. When specialized engineers spread across too many problems,

each solution reaches good enough rather than excellent.



The organization has more capable engineers than currently recognized,

but they need systematic enablement. This includes agent SDK training

from Lars Vedo and Ryan Stevens\' team, publishing standards and best

practices from Derek Osgood\'s team, and foundational AI training like

Anthropic\'s agent design pattern curriculum. Investment in systematic

upskilling multiplies the effective engineering capacity for AI-specific

challenges. Without resolution, the team will continue delivering good

enough implementations with a few engineers rather than excellent

products, and user satisfaction and competitive differentiation will

suffer.



**Last Mile Delivery Gap---From Technically Ready to Customer Sellable**



Multiple agents reach technically ready state but lack a systematic path

to production deployment. Technical readiness does not equal production

readiness. The gap includes go-to-market positioning and messaging,

product marketing materials, pricing model integration and credit system

documentation, customer enablement materials, publishing workflows to

move internal tools to customer-facing features, schema documentation

and versioning, and agent or tool marketplace infrastructure.



Eight teams built agents this quarter but only two reached production.

This represents massive sunk engineering cost with no revenue

realization from the remaining six. Engineering delivers technical

capabilities that sit unused because GTM infrastructure does not exist

to bring them to market. Derek Osgood\'s entire Q4 scope addresses this

challenge through the Unified AI Service Registry, Internal Tooling and

Publishing Admin Panel, and Play Library templates. This shows the

organization is treating the challenge seriously, but it requires

dedicated PMM and GTM resourcing under Derek to systematize the

last-mile delivery infrastructure and consultative agent marketplace

model.



### **2. Scaling Challenges for Architecture**



**Context Quality vs. Context Quantity**



The team discovered through production experience that more context

degrades LLM performance, contrary to initial assumptions. Precision in

information provided is critical. Irrelevant information distracts LLMs,

increasing both error rates and inference costs. Overstuffed agent

context causes measurable performance degradation in production

deployments.



This learning directly informs the Base Context Acquisition Pipelines

initiative in the Q4 roadmap. The focus is achieving context parity with

market leaders like Google and Claude rather than context volume. Rowan

Bailey\'s Q4 work addresses this through context engineering discipline,

systematic context pruning, and retrieval strategy optimization.



## **SECTION 2b: How Do Forward Looking Challenges Compare To Our Plans And Roadmap For The Next 1-2 Quarters**



The Q4 2025 roadmap is locked in and underway across three workstreams.

Derek Osgood owns AI Orchestration including the transition of DoubleO

to Plays, the Unified AI Service Registry, and publishing tooling. Lars

Vedo owns Applied AI including SDK and Runtime v1, Essential Shared

Agents, Embeddable UI Foundation, and Basic Testing Infrastructure.

Rowan Bailey owns Context Engineering including context acquisition

pipelines, External MCP Gateway, event-driven architecture, Memory

Service, Momentum Score, and Custom Signals.



The last-mile delivery gap is directly addressed by Derek\'s entire AI

Orchestration scope. The Unified AI Service Registry creates a

centralized framework for building agentic and non-agentic actions. The

Internal Tooling and Publishing Admin Panel exposes action publishing

tools as an internal admin panel for deploying workflows, agents, and

tools into existing products through a no-code interface. The Play

Library provides ten published templates as a starting point. This work

systematizes the path from technically ready to customer sellable. The

challenge was anticipated and is being addressed..



The specialized AI talent constraint affects execution quality for SDK

and Runtime v1, Essential Shared Agents, and Basic Testing

Infrastructure. Roadmap progress depends on resolving the talent and

upskilling gap through executive action on headcount and training

investment. Without this, deliverables will reach adequate state rather

than excellent state.



The context quality versus quantity challenge is incorporated into

roadmap priorities. The External MCP Gateway launching mid-November and

the context pipeline work directly address this learning. The team

shifted strategy based on production experience.



Design resource fragmentation affects multiple Q4 initiatives. The

Embeddable UI Foundation, Plays UX, and Memory Service interfaces all

require Ryan McMaster\'s design support. His bandwidth is stretched

across multiple workstreams. This may require prioritization decisions

or additional design resources to maintain quality standards.



Several initiatives remain on track despite challenges. The External MCP

Gateway is proceeding on schedule toward mid-November launch with 50

reps already enabled for Dreamforce validation. Copilot Workspace

adoption continues after the successful October 6th launch with

infrastructure complete for customer expansion. The DoubleO to Plays

transition benefits from Derek\'s systematic approach to publishing

infrastructure, which addresses the root cause of past deployment

friction.



The roadmap should accelerate engineering upskilling by front-loading AI

fundamentals training in Q4 to expand the talent pool for specialized

problems. The team should prioritize Ryan McMaster\'s design focus by

identifying which of Embeddable UI, Plays UX, or Memory Service delivers

highest impact for Q4 customer adoption. The organization should monitor

talent constraint impact closely, and if SDK and Runtime v1 or Essential

Shared Agents slip, escalate immediately for additional specialized

engineering resources.



## **SECTION 3: How Did We Measure Success This Quarter (KPIs And Impact On Customer Behavior)?**



### **Part A: Key Performance Indicators**



**Platform Adoption & Velocity**



Agent teams enabled increased from zero to 8+ this quarter. The platform

investment hypothesis was validated as teams built independently with

minimal support. The target is to continue enabling product teams as the

SDK matures. Production agents increased from zero to two with Copilot

Workspace and Chorus now live. The target is 5+ agents in production by

end of Q4 as Derek Osgood\'s publishing infrastructure work closes the

gap from technically ready to customer sellable.



Development velocity improved from weeks to 24 hours for agent

embedding. This enables rapid experimentation and reduces time-to-market

for new AI capabilities. Teams can now test ideas in production quickly

rather than spending weeks on infrastructure setup.



**Performance & Reliability**



Top Contacts latency decreased from 4 seconds to 1 second P99,

representing 75% reduction. Top Contacts capacity increased 50x versus

baseline. These improvements unlock scaled customer deployment without

infrastructure constraints. The system can now handle production load

that would have crashed the previous architecture.



Semantic data processing costs dropped to approximately 18 cents per

call transcript and 8-9 cents per email thread through batch processing

optimization and Gemini Flash 2.5 adoption. These reductions make

large-scale tenant onboarding economically viable where previous costs

blocked expansion.



**External Adoption & Reach**



MCP reps enabled reached 50 for Dreamforce demonstrations. The target is

20 customers live on MCP gateway by Q1 2026. This represents first

external validation of the portable intelligence strategy and enables

the shift from license-based to consumption-based revenue model.



Semantic data customers reached 18 Early Access customers processed and

live in Workbooks. The target is 250 tenants onboarded with event-driven

processing by end of Q4. Event-driven architecture will process call

transcripts and emails immediately after meetings end or emails send,

providing near-real-time conversation intelligence.



**AI Credits & Consumption**



The credits system framework is defined and integrated into Copilot

Workspace and the agent platform. This enables consumption-based pricing

for all Intelligence products going forward. Volume metrics

infrastructure is being established to track usage patterns and optimize

pricing models.



### **Part B: Customer Behavior Impact**



**Copilot Workspace Adoption**



Approximately 1,000 internal sellers engaged in pre-launch testing

before the November 3rd customer launch. The infrastructure now supports

cross-account analysis, semantic data queries, and multi-format artifact

creation including emails, documents, and buyer engagement maps. Sales

reps now delegate research tasks to AI rather than manually compiling

account intelligence. This represents a workflow shift from active

research to task delegation.



**MCP External Intelligence**



Fifty GTM reps use ZoomInfo intelligence directly in Claude and ChatGPT

desktop applications. The consumption pattern shifted from logging into

the ZoomInfo app to accessing ZoomInfo data wherever work happens. The

Dreamforce validation demonstrated the portable GTM intelligence model

in real-world scenarios with actual customer conversations.



**Semantic Data Integration**



GTM Studio workbook creation from semantic data source is nearly

complete, blocked by GTM Studio resourcing rather than Intelligence

dependencies. When shipped, conversation intelligence becomes a

queryable dataset for custom analysis alongside traditional ZoomInfo

data. This enables customers to build their own views into what their

teams are discussing with prospects and customers.



### **Part C: What Success Looks Like Next Quarter**



**Adoption Targets**



GTM Studio adoption should reach 100 customers live on platform. Play

builders should reach 20 customers actively building custom Plays. Play

templates should include 10 published templates providing instant

time-to-value. MCP customers should establish a path to 20 customers

live on MCP gateway with Q1 2026 as the target, starting foundation work

in Q4.



**Technical Milestones**



Semantic data scale should reach 250 tenants onboarded with event-driven

processing where calls and emails process immediately. Memory Service

should serve all Copilot Workspace users for personalized AI

interactions. Momentum Score should go live in production, enabling

opportunity-level recommendations beyond the APS prospecting focus.



**Quality Indicators**



Context parity should be achieved where base context acquisition

pipelines deliver equivalent quality to Google and Claude for account

and contact research. Testing infrastructure should enable less than one

day turnaround time to evaluate new models or major agent adjustments as

an internal metric. Embeddable UI should provide consistent chat

experience deployed across all ZoomInfo products.



**Enablement**



Play Library should include 10 templates demonstrating high-value

automation workflows. Publishing infrastructure should enable internal

teams to deploy new AI functionality via no-code admin panel. Credit

consumption should establish baseline consumption metrics for

forecasting and pricing optimization.



**SECTION 4: Beginning vs. End Contrast Table \[July vs. October\]**



