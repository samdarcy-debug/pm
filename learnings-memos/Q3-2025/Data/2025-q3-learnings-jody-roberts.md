---
id: learnings-2025-008
title: Q3 2025 Learnings Memo - Jody Roberts
type: doc
status: approved
team: data
owner: '[[teams/data/_people/jody-roberts]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
## **Metric Alignment**



**Company Coverage Rate:** Delivered net +1.1M companies through team

coordination. Cam added 2.4M (1.15M Tier A) while removing 1.3M for

quality---July\'s 500K from customer search patterns, October\'s 1.9M

from continued expansion plus international partnerships (500K).

Peter\'s orphaned companies pipeline positioned for +1.4MM January

additions. Customer validation from Uber, Palo Alto, RedHat confirmed

we\'re addressing LATAM/EMEA/APAC gaps.



**Company Perfect Accuracy Rate:** Systematic quality improvements

across teams. Cam impacted 10M+ location records achieving 95% Fortune

1000 accuracy, separated 602K overcombined sources. John identified 55M

junk contacts, launched undercombination detection. Rituparna added

20.5M personal emails, 2.6M mobile phones, expanded department

classification 57%→62%. Combined efforts reduced complaints 80%,

validating Q1\'s quality-over-volume approach.



**CN Contact Contribution:** Peter\'s CN Milestone 5 leveraging partial

records delivered 2.5M+ attributes, projecting 4MM net new contacts.

Calendar pipeline scoping unlocks existing contributions in the GTM

store for Q4 implementation.



## **Key Learnings**



**Customer Search Behavior Identifies Highest-Quality Targets:** When

customers search for companies not in our database, these unmatched

domains convert to Tier A at 49% rate versus 15-20% from other sources.

This behavioral signal loop---customers search → we create → searches

succeed → more searches---proved most efficient growth path. Moving from

quarterly manual processing to 48-hour automation will scale this

advantage.



**Email Validation Bottleneck Constrains Multiple Teams:** Analysis

revealed 6M contact backlog stems from email quality. Current 10% bounce

rates (target: 3%) risk Spamhaus blocking and prevent scaling privacy

notifications for expanding regulations (Canada added Q3). John and

Magnus findings show this blocks contact publication and CN expansion.

Solution requires validation improvements beyond infrastructure scaling:

RevenueBase integration, risk scoring, catch-all handling.



**Customers Building AI Tools Validates Need for Quality Moat:**

Autodesk revealed they built AI automation using our names/websites,

then generating everything else with LLMs. This pattern confirms our

differentiation isn\'t data availability but systematic validation at

scale: John\'s 55M junk detection, Cam\'s 96% overcombination accuracy,

Peter\'s proprietary CN contributions. Without validated accuracy, we

become an expensive directory customers will replace.



**International Expansion Needs Market-Specific Depth with Language

Support:** Added 500K international companies but gaps remain in

strategic markets. Autodesk needs 20-30K Japan companies (we have 3K),

flagged \"Cannot Translate/Match Non-Latin Characters\" as blocker. Uber

prioritizes LATAM depth, Palo Alto needs APAC. Rituparna\'s department

classification work improved coverage from 57% to 62% with 15.9M total

contacts classified with department mapping across 12.5M international

contacts and improved coverage across 17 countries but 38% of

international contacts still lack department classification, making them

undiscoverable through primary search filters.



**Quality Improvements Through Deletion Generate Positive Response:**

Cam removed 4.8M locations while adding 1M verified (net -3.8M),

achieving 95% Fortune 1000 accuracy---customers responded positively.

John\'s 93% duplicate email reduction (15M→1M) improved match rates and

routing. This continues Q1\'s paradigm shift: strategic removal of bad

data creates more value than adding questionable records.



## **Hypotheses & Results**



**H1: Cross-functional collaboration overcomes technical constraints**

**Validated.** Despite frozen sources and merge complications, team

coordination delivered 2.4M new companies (1.15M Tier A).

Customer-requested domains proved concept at scale. Manual coordination

is unsustainable but demonstrates an automation path.



**H2: Contact uniqueness drives trust more than coverage expansion**

**Validated.** John\'s 93% duplicate email reduction and 5M+ duplicate

contact removal improved customer satisfaction despite lower totals.

Rituparna added 20.5M emails but prioritized deliverability. Clear

signal: unique, validated contacts beat raw volume.



**H3: Email quality issues block downstream processes** **Validated.**

John and Magnus analysis confirmed the 6M backlog isn\'t

infrastructure---it\'s validation. High bounce rates prevent ESP

scaling, risk Spamhaus blocking, constrain privacy compliance. Requires

a comprehensive quality approach, not just capacity.



**H4: Web extraction works selectively, not universally** **Partially

validated.** Location extraction achieved 95% accuracy for simple sites

(\<50 employees, \<10 locations) but failed on complex/JS-heavy sites.

Over-extraction and ambiguity issues forced pivot to hybrid approach:

deterministic sources (Mastercard, Zipi) plus targeted extraction.



**H5: Platform architecture enables dataset velocity** **Partially**

**Validated.** Peter\'s efforts enabling GTM Store shipped 4 datasets

Q3. The first dataset took 3 months, subsequent ones \<4 weeks each.

Vertical markets (contractors, franchises, restaurants) reach prospects

B2B databases miss. Architecture proven but requires organizational

alignment for broader platform investments and unlocking value to

customer more quickly.



## **Go-forward Changes & Plan**



**Critical Blockers:** Email validation improvements (John/Magnus)

reducing bounce rates 10%→3% through RevenueBase, risk scoring, expanded

proxies---clearing 6M backlog for privacy compliance. Industry

classification careful rollout targeting problematic cohorts first

(Photography Studios), integrating with M8 January launch.



**Scale What Works:** Automate customer-driven creation pipeline (Cam)

from quarterly to 48-hour continuous cycle, leveraging 49% Tier A

conversion. Implement CN calendar extraction (Q4) for proprietary

meeting participant signals. Continue contact uniqueness momentum (John)

with validation framework before new sources, targeting 80-90% email

deliverability.



**Strategic Expansion:** International depth in customer

priorities---Japan (Autodesk), LATAM (Uber), APAC (Palo Alto)---adding

600K-1M companies with language support. Continue driving toward Company

3.0/ and launch M8 (January) codifying entity resolution rules and clean

schema.



## **Leveraging AI**



**Q3 Implementations:** John\'s junk contact ML model (55M identified).

Rituparna\'s international title classification (+1M contacts with

department). Leveraging AI in many areas to improve speed to value

across team with prototypes, agentic solutions and data unlocks (Data

Insights Agent, CN Agents, etc).



**Infrastructure Gap Identified:** Cam called out critical

limitations---AI tools run locally only, preventing research team

sharing and automation. Lack of deployment infrastructure for

Snowflake/API apps limits value multiplication.



**Q4 Expansion:** Focus on operationalizing existing tools versus

building new prototypes. Priority: solving deployment infrastructure to

enable team-wide tool sharing and automation.

