# 2026 GTM Intelligence Roadmap
**Objective: GTM Execution Runs Through ZoomInfo**

January, 2026. See visual walk-through here.

*Internal Draft. Confidential.*

---

The next 12 months are about whether we can capture a 10x opportunity of becoming the **GTM Intelligence Foundation for AI**. We have to capture this iPhone moment and create the machine-readable foundation for GTM in 2026.

We are starting the year with foundational changes coming together:
1. We have products for AI GTM: Studio, Workspace, and our MCP/APIs
2. They are powered by a new unified data platform for structured and unstructured data
3. Our business model is set up for consumption, tied to an agentic platform that monetizes “work” via AI credits

Success for 2026 means **running critical GTM Execution jobs through the ZoomInfo platform**. That is “workloads” consuming credits. 

**Our North Star is credit consumption growth**. Not seats. Not users. Not adoption. Over the last two years, credit consumption has been essentially flat. A successful 2026 inflects that metric because we shift from monetizing *data access* to monetizing *data work and execution*.

# Status Quo: The GTM Execution Problem

GTM is a massive market in desperate need of AI transformation. Enterprises spend up to 50% of their budgets on sales and marketing. Our average customer uses 42+ tools in their GTM stack. And yet:

**What it's like to prepare for a customer meeting:** When a seller prepares for a meeting, the context they need is scattered across systems: the account record in Salesforce, the opportunity history, the contact list (probably incomplete), last quarter's QBR deck in Google Drive, the support tickets in Zendesk, the product usage data in the data warehouse. Each system has a piece. None talk to each other.  the average account executive has more than 1,000 contact switches a day and spends less than 10 seconds focused in a single place or app.

**What it takes to change a territory:** When a CRO decides to change territory assignments—something that should be simple—it triggers a scramble across disconnected systems. In Salesforce, someone manually reassigns accounts. In LeanData, someone rebuilds routing rules. In Spiff, someone reconstructs commission plans. Then weeks of QA to make sure nothing broke.

Workday shared an 18-month roadmap with us focused entirely on untangling their account data before they'd even consider incorporating intent signals. Enterprise CROs frequently tell us: "We have 40 people whose entire job is data hygiene. And we still don't trust the numbers." Capital One and Uber spend millions annually just to know who their customers actually are.

AI has changed particularly software engineering, but similar results have not manifested in GTM. Our customer's reality is paved with failed "GPT on my CRM" experiments. Most GTM AI is still expensive autocomplete.

These aren't unsophisticated companies. They represent the best in the industry, and they're drowning in data chaos.

Two structural gaps explain why AI has transformed engineering but not GTM:

**1. GTM Architecture doesn't fit AI.** During ZIRP, GTM added a tool for every problem. Gong for calls, Outreach for sequences, a Deal Room, Forecasting—then write some data back into the CRM. The real data lives siloed in point solutions and isn't connected.

The legacy stack has a CRM at the center (the hub) surrounded by point solutions (the spokes). This hub-and-spoke model is fundamentally broken. When your data lives in the spokes, the hub loses context. You end up with:
- 18 Cisco records in the same CRM
- Sarah Chen appearing as "Sarah Chen" in Salesforce, "S. Chen" in Gong, "sarah.chen@cisco.com" in Outreach
- Hierarchy confusion: Is "Cisco WebEx" a subsidiary or separate account?

**2. The Data Model isn't designed for AI Context.** CRM's data model is 25 years old. It captures outcomes—stage, amount, close date—not decision traces: what was tried, what worked, why the deal moved.

Open any deal in your pipeline. The CRM shows: Stage changed from 3 to 4. Close date pushed two weeks. Amount revised down 15%. That's it.

In reality: The CFO joined the last call and asked about ROI within 6 months—that's why the deal accelerated. The VP of Sales went quiet for 8 days fighting an internal battle over budget—that's why it almost died. The 15% discount happened because of competitive pressure. The CRM recorded the state change. It has no record of *why*.

This example shows the difference between a machine readable data foundation with decision traces that agents can use to derive context & patterns. 

There is a reason AI has impacted software engineering the way it did, while GTM is largely still in POC phase. Engineering operates on top of machine readable data and with the tooling/data-structure that supports decision-traces:

| Dimension            | Software Engineering                            | Go-To-Market                                                         |
| -------------------- | ----------------------------------------------- | -------------------------------------------------------------------- |
| **Source of truth**  | Machine-readable codebase                       | Scattered data, Proprietary UIs, Manual clicks, hard-coded workflows |
| Structure            | Standardized (version control, test automation) | Not standardized, hard for LLMs to master                            |
| **Feedback loops**   | Fast, Developers for Developers                 | Slow, manual & through alignment meetings                            |
| **Machine-readable** | Yes, by design                                  | No                                                                   |

AI can't transform what it can't read. **GTM lacks a machine-readable foundation.**

**This is our iPhone moment.** CRM is not going to be the platform to run GTM AI on. If you designed a GTM system from scratch to solve this problem, you end up designing ZoomInfo, applied to first-party and third-party data.

*See the memo on Context in GTM for more details.*
# Solution: The GTM Intelligence Platform

What customers need isn't more third-party data pushed into a CRM. They need a unified foundation that makes their own first-party data coherent enough for machines to reason over.

We've spent 20 years building the largest B2B data unification platform in the world. We resolve hundreds of millions of companies and contacts across every variation, misspelling, and format. Now we're applying that capability to the full scope of a customer's GTM.

At the core of our AI strategy is **GTM AI**—the machine-readable data foundation that powers everything we build. On top of that foundation, we have three surface areas for GTM execution:

1. **GTM Workspace** — Where frontline sellers live and execute
2. **GTM Studio** — Where ops orchestrates and activates GTM workflows
3. **MCP/API** — Where enterprises build their own stack and partners integrate

This means we serve customers wherever they work and however they work. But the magic and the differentiation come from the underlying engine.

![[Pasted image 20260107195307.png]]

## Why GTM AI Wins

GTM AI is purpose-built for go-to-market—not a general LLM with a GTM wrapper.

**The best data asset.** We've trained on 100 million companies, 500 million contacts, behavioral signals, identity graphs, and engagement data. No one else has this.

**Deep GTM understanding.** Our models comprehend what matters in GTM: conversation intelligence, corporate hierarchies, territory structures, data unification, reference data access, and context graph construction.

**Best-in-class models for critical jobs.** Pipeline generation, propensity scoring, account prioritization, next best action. Built for GTM work, not general-purpose chat.

| Component                   | What It Does                                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **B2B Reference Data**      | Foundational grounding for companies, contacts & signals. The strongest B2B dataset in the market.         |
| **Unified Data & Matching** | Match, dedupe, link across 1P and 3P. Normalize "Cisco" and "CSCO" and "Cisco Systems" to canonical forms. |
| **GTM Context Graph**       | Connect entities, causal relationships, patterns. Semantic extraction that makes GTM machine-readable.     |
| **GTM AI Models**           | Purpose-built models for GTM jobs: prioritization, propensity, pipeline generation, next best action.      |

## The Execution Surfaces

This foundation earns us the right to execute GTM workflows.

**GTM Workspace — Win against Gong**
Where sellers live. We need an interface sticky enough that sellers spend their working day inside it—this is how we compete against Gong, who owns mindshare because reps live in their app. Context surfaces automatically. Actions flow back into the system. In 2026, Workspace shifts from suggesting to executing: inbound arrives → research, qualify, route, draft. Meeting ends → attribute, update buying group, refresh forecast.

**GTM Studio — Win against Clay**
Where ops builds. Studio connects the datasets built in GTM Place to run workloads on our platform—designed workflows, automation, and execution through our system. Clay captured the "AI data enrichment" narrative. We have what they can't build: 20 years of entity resolution, the reference dataset, enterprise-grade data management.

**MCP/API — Open the Enterprise**
Where we widen the reach. MCP lets customers build their own GTM stack for enterprise use cases and enables our intelligence to run inside other platforms—Anthropic, OpenAI, Slack, Vertex. Every MCP connection is a new surface for credit consumption.

# How will we get there: Quarterly Roadmap
## North Star: Credit Consumption Growth

Credit consumption has been flat for two years. A successful 2026 inflects that metric because we shift from monetizing *data access* to monetizing *GTM execution*.

| Objective | Definition | KPI |
|-----------|------------|-----|
| **Win & Monetize GTM Work** | Capture critical GTM jobs where we have right to win | Job coverage in top 5,000 accounts |
| **Activate the Context Flywheel** | Every interaction makes the next interaction more valuable | Value-per-credit growth rate |
| **Scale Distribution** | MCPs, marketplace, partner ecosystem | Ecosystem credit consumption |


This product roadmap goes hand in hand with upgrading our monetization and business model. The GTM Intelligence platform is built to win and monetize GTM work. Today we sell data access: 1 credit = 1 record. 

This model has a ceiling. Once a company record is unlocked, we extract no additional value regardless of how much we help the customer. At the same time any given customer isn't going to significantly expand their TAM year-over-year, in other words we don't have an organic upsell path.

We need to stack more value on every record a customer unlocks. Data management and AI workflows have the highest upside. They both represent a form of monetizing the work that we do on a given record as opposed to the raw data itself. Data management keeps the foundation clean, and AI workflows are executing outcomes. Both are evergreen, always-on systems.

*See the memo on ZoomInfo's Data & Credit System evolution for more details.*
## Quarterly Themes

### Q1: Plays—Complete the Unify-Orchestrate-Execute Loop

We've had data (Unify) and execution (GTM Workspace), but Plays is the orchestration layer connecting them. We move to event-driven infrastructure with live updates at scale, focused on conversational signals. Plays capture decision triggers and outcomes—the beginning of the context flywheel.

- **Jobs:** Account prioritization, cross-sell expansion, pipeline management
- **Launches:** Plays, GTM Flow 1
- **Competing Against:** Chorus, Copilot, Gong
- **Distribution:** No-code plays builder, data and audience marketplace, ROI and health scans

---

### Q2: Win Inbound/Outbound—Scale Distribution

We nail the most critical GTM problems: Inbound and Outbound Acceleration. Pulse frontline activation goes live with agents that do the work for sellers, not just suggest it. Tasks and Plays are fully tracked and power GTM reporting. We turn on distribution via the [GTM.ai](http://GTM.ai) marketplace and ZoomInfo agents running across major platforms.

- **Autonomy:** Autonomous agents (2/4)
- **Jobs:** Inbound acceleration, outbound automation
- **Launches:** Pulse
- **Competing Against:** 6Sense, Outreach, Salesloft
- **Distribution:** MCP/API for Slack, OpenAI, Vertex; PLG motion for GTM Studio

---

### Q3: Enrich 3.0—Enterprise Data Management

Our AI-native solution that automatically cleans, enriches, and synchronizes data across all GTM systems goes live. GTM Data Model reaches full coverage—we can map, normalize, and unify any GTM data source. We monetize cleaning 1st party data through credits. We solve the hardest enterprise data problems: account hierarchies and location-level data with flexible matching.

- **Autonomy:** Always-on agents (3/4)
- **Jobs:** TAM and ICP build, territory and account planning
- **Launches:** Enrich 3.0
- **Competing Against:** RingLead, Clay
- **Distribution:** PLG GTM Workspace

---

### Q4: Win the CRO—Own the Stack

Per-account agents with full lifecycle context. Goal-oriented systems that see every handoff, recognize patterns that lead to revenue outcomes, and compound organizational learning. The marketplace matures with third-party plays and agents. We solidify our position as the indispensable platform for AI-driven GTM.

- **Autonomy:** Long-running, goal-oriented agents (4/4)
- **Jobs:** Forecasting, TAM optimization, account health
- **Launches:** Forecast, GTM Flow 2, Sequencing
- **Competing Against:** Gong
- **Distribution:** Ramped affiliates, expanded partner ecosystem


# What We Have to See
For this strategy to succeed, three bets must pay off:
### Bet 1: The foundation wins, not the features

Companies will pay more for machine-readable GTM infrastructure than for point solutions, even if those solutions have superior UX.  

Vercel moved from 10 SDRs to 1 + AI agent—$1M/year savings—but only after building their own data foundation. They explicitly said they "couldn't just take off-the-shelf parts." Square won payments by building the whole product, not by having the best feature.

We have to see deals winning on platform narrative by Q2, competitive displacements by Q3 and increasing Studio+Workspace attach rate throughout the year. Gong, Outreach, and 6sense have sticky deployments. Gong was just named Gartner Leader in Revenue Action Orchestration with highest "Ability to Execute" score.

### Bet 2: Customers will trust us with first-party data

Enterprises will share their most sensitive GTM data (calls, emails, CRM) if we demonstrate superior value.

Enterprise customers already share CRM access via integrations. Capital One-type data chaos creates urgent buyer need. 

We have to see integrations into our GTM Data Model with 1st party data growing q/q.

### Bet 3: Consumption beats seats

Our credit model creates sustainable advantage—we can give away capabilities competitors must charge for, because we make money when data runs through our platform.

We're the only business with contractual rights to use customer data to improve our models. Salesforce can't do this. Gong can't do this.
