---
id: learnings-2025-045
title: Q3 2025 Learnings Memo - Jesse Miller
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/jesse-miller]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
## **Metric Alignment**



**Primary North Star Driver:** Ad Spend on Platform\

Q3 delivered infrastructure and optimization capabilities that directly

enabled increased spend



**Key Sub-Drivers:**



- **CTR Model Impact:** 10% improvement in click-through rates for

  campaigns



- **Notification Center:** Customer comms engine enabling proactive

  account management



- **Forecasting Expansion:** International and video ad support unlocks

  new advertiser segments



**Secondary Impact:** Visitor Resolution Rate (VRR). In Q3 we shipped

Bot ID Model into VRS, and instrumented a telemetry endpoint for the ZI

tag. VRR drives '**Best GTM Data'**, every resolved visitor feeds

contact enrichment, intent signals, and advertising attribution.



## **Key Learnings**



Infrastructure debt compounds silently without instrumentation. Q3

telemetry work exposed **10-15% of ZI Tag events never reach our

database**. The hypothesis is our CDN Cloudflare is the root cause. Head

to head test confirmed: \<1% drop rate going direct vs. 10-15% through

Cloudflare. Every dropped event is a visitor we can\'t resolve, a

contact we can\'t enrich, a signal we can\'t generate. This is a tax on

VRR.



Bot Model implemented into VRS, increasing VRR accuracy. No more wasting

compute on non-human traffic upstream. Fixing bots won't matter much if

we\'re losing 10-15% of good traffic to infrastructure. Telemetry was an

unlock, you can\'t optimize what you can\'t measure.



Customer communications and forecasting improvements are force

multipliers, not isolated features. Notification Center gives us a

direct channel when campaigns/ad sets/budgets need attention.

International and video forecasting removed major sales objections.

Better forecasting = fewer failed campaigns = less support load = more

time for optimization instead of firefighting.



**Hypotheses & Results**



**Hypothesis 1:** Cloudflare proxy routing is causing significant event

loss in ZI Tag pipeline, directly impacting VRR.



**Result:** Validated via telemetry endpoint and head-to-head

experiment. 10-15% drop rate with Cloudflare, \<1% direct. This is 10M+

lost resolution opportunities monthly. James Guyer completed a 70-page

ZI Tag audit identifying additional optimizations beyond Cloudflare

removal. Root cause confirmed, InfoSec approval required to fix.



**Hypothesis 2:** ML-based bot classification in VRS would improve

resolution quality by filtering non-human traffic upstream.



**Result:** Bot Model shipped to VRS in production, replacing legacy

is_bot flag. Early signals show improved data quality. Real win: proved

we can deploy ML models into VRS pipeline, opens door for additional

classification models (high-value visitor prediction, fraud detection).



**Hypothesis 3:** Building customer communication infrastructure and

expanding forecasting capabilities would reduce support friction and

remove deal blockers.



**Result:** Both shipped to GA. Notification Center integrated with

PubSub for real-time campaign, ad set, budget alerts. Forecasting

expanded to international markets and video formats. Sales confirms

these removed objections in deals. Haven\'t instrumented support ticket

reduction yet, but CX feedback is strong.



## **Go-forward Changes & Plan**



**Q4 Priorities:**



**1. Remove Cloudflare Proxy from ZI Tag Endpoint\**

Submit InfoSec proposal Q4 W1, complete migration by EOQ. Recover 10M+

events monthly, 10-14% VRR improvement. Owner: Jesse + James Guyer.



**2. ZIM UX Improvements\**

Expand Notification Center via email delivery+queue/banner system

integration. Ship Adaptive CPM Bidding, Enable Campaign

Objective-to-Model automation (Conversion model in development).



**3. DMP API / Audience Syndication (Decision + Execution)\**

M1: Document process, APIs, monetization. M2: Build usage tracking

infrastructure. M3: Choose path (Workbook-\>Workflows integration).

Target H1 2026 revenue goals if resourced.



**4. AI-Powered Optimization Suite\**

ZIM Agent internal beta (Oct/Nov). AI-driven publisher expansion

automation. Conversion Model Suite completion. Goal: 50%+ reduction in

manual optimization work.



## **Leveraging AI**



**Q3 Impact:** Using AI on a daily basis across documentation, workflow

and productivity, and dev/prototyping. I used **Cline** to prototype a

ZIM Agent UI. I built a custom service that every monday hits the Chorus

API and summarizes all my chorus calls and pushes updates to a google

doc. Leveraged ZI Chat to build audience recommendation agents with Ben

Goldman for agencies interested in ZI audiences. Also use GPT / Claude

daily with data analysis and SQL query optimization.



**Q4 Building:**



- **ZIM AdOps Agent:** Natural language campaign troubleshooting via

  MCP + Analytics/Tower/MOS APIs. Internal beta October. Building this

  creates the structured API surface ZIM needs, compounds across all

  future automation.



- **AI Publisher Expansion:** Automate DSP/SSP evaluation and

  integration prioritization using performance data. Publisher expansion

  decisions down from weeks to hours.



- **Conversion Model:** Jenny leading EDA on conversion likelihood

  prediction. Completes objective-to-outcome automation.



- **Bot Detection v3:** Improve ML classification precision via better

  training data.



**Leverage Thesis:** Every optimization problem benefits from ML. Q3

proved we ship models to production (BotID, CTR). Q4 systematizes this,

building agent infrastructure, instrumenting data pipelines, and

creating feedback loops. The endgame is autonomous advertising that

feeds into GTM plays: users define outcomes, AI figures out execution.

