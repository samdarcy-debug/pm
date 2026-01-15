---
id: learnings-2025-049
title: Q3 2025 Learnings Memo - Matt Barnes
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/matt-barnes]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



**North Star Metric: Best GTM Data**



**Increase Company Resolution: +6.32 PPT / +16% Increase in company

identification rate**



COIN created new delivery pipelines for both LiveIntent and 5x5 data,

resulting in the largest resolution increases from third party data seen

to date. This effort contributed to increased visitor resolution in

WebSights, a greater number of Intent signals, and improved targeting

and attribution for Ads.



**Increase Visitor Resolution Rate: +\~2 PPT / +\~400% increase in

person identification rate.**



Inferno and COIN assisted Infra in increasing visitor resolution rate

from about .5% to 2.5% by moving to person-first resolution in the VRS,

integrating LiveIntent, increasing HEM to ZI person mappings, and

completing the transition of WebSights into the VRS.



**IP Bot Identification Rate** (NEW):



In collaboration with Infra, COIN helped develop a new bot dataset to

power a classification model that identifies not only "unknown" bots,

but automated traffic from known companies (e.g. crawlers and

scrappers). Inferno added this filtering to a set of beta customers who

are currently testing it out. This will provide more accurate signals

for all services leveraging IP-based identification from the VRS.



#### **Key Learnings**



We continue to receive strong demand for person-level resolution outside

of Copilot, particularly for large customers that receive a relatively

high number of visits. Supporting person-level resolution in Workbooks

and the WebSights UI (even if it is still restricted to customers who

purchased Copilot), would go a long way to satisfying these customers.

Furthermore, while the first iteration of person-level resolution came

in the form of WebSights Buyer ID (WBID), where we filter by a customer

end user's individual Buying Group, customers such as IBM want ALL

person-level visitors provided without filtering. There is a tendency

for many at ZoomInfo to use WBID and person-level resolution

synonymously, but it is important to not myopically focus on WBID when

delivering signals to customers.



#### **Hypotheses & Results**



**Hypothesis 1**: If we repurpose person-level identification data to

provide IP-to-company pairs, then we could exceed the resolution rate

we've seen from vendors offering IP-to-company data "out of the box".



**Result 1**: While LiveIntent and 5x5 were primarily acquired to

contribute to increasing VRR and for firmographic/contact data, both

vendors provided higher impact than Deduce, which was the only other

third party IP-to-company data implemented. LiveIntent and 5x5 combined

produced 6 PPT lift compared to Deduce's 1 PPT, which cost roughly 300K

when it was implemented in 2023 and was useful only for company

identification and not person identification, firmographic, or contact

data.



**Hypothesis 2**: If we sync our cookies with person-level

identification vendors through their pixels, then we could complement

the Clickagy device graphs and increase VRR potentially several percent

per vendor..



**Result 2**: Only the LiveIntent pixel has been integrated, but it

produced a disappointing fraction of 1 percent of lift for VRR. This is

likely due to the Clickagy device graph and LiveIntent using the same

underlying sources (e.g. bidstream). That said, given our current VRR is

\~2.5%, even a combined +1 or +1.5% from these vendors would be worth

pursuing at this point in the evolution of our identity graph.



**Hypothesis 3**: If we remove bot data, even when associated with an

identified company, then WebSights customers will understand and

appreciate that the total number of companies identified will decrease

from what they are used to seeing



**Result 3**: Nine customers are participating in the beta, and while

there have been some questions, there have not been any objections to

the *perception* that company identification has dropped.



...



#### **Go-forward Changes & Plan**



**COIN**: Continue to prioritize increasing VRR and company-based

resolution. Further investigate quality to determine what can be done to

increase accuracy without significantly lowering resolution rate.

Finally, in collaboration with Inferno, we will be delivering both

WebSights and FormComplete data to the GTM Data Store Engagements schema

near-real time so that downstream applications can consume it and

deliver a wide variety of use cases to customers.



**Inferno**: Deliver a data service that provides company and person

identification data via webhook and API, including the crucial visit

details missing from the current WebSights API. Complete Adobe Analytics

integration capabilities in WebSights. We will also be delivering the

combined data necessary to generate the Website Visitor Journey Signal

for GTM Plays. Finally, Automated Traffic Filtering and AI Page Rank

will go from Beta to GA in Q4.



#### **Leveraging AI**



Our primary investment in AI in Q4 will be in the form of AI Page Rank,

which will provide an automated solution for customers setting up

WebSights to generate visitor intent rankings for each monitored page on

their site. This will result in additional signals to downstream

applications at ZI and will provide a better experience for WebSights

users when filtering visitor events by Page Rank so that more promising

leads can be identified by GTM teams sooner.

