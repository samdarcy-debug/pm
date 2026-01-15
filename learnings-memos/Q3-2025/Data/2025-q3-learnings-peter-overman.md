---
id: learnings-2025-011
title: Q3 2025 Learnings Memo - Peter Overman
type: doc
status: approved
team: data
owner: '[[teams/data/_people/peter-overman]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
#### **Metric Alignment**



My work contributes to Data ROI and each of its sub-driver metrics. On

*Company Coverage*, we supported July and October company cube releases

(+0.5MM and +1.9MM new companies respectively) with even greater impact

expected in January (via 'orphaned companies' and Predict Leads). On *CN

Contact Contribution*, we released CN Milestone 5---using partial CN

records as seeds to run WDoD which has already added 2.5M+ person

attributes and 100K+ new contacts with full estimated yield of +4MM net

new contacts and +12MM publishable contacts (once fully run in Q4-Q1).

On *Company Accuracy*, we recently released changes to our domain

vitality crawler to identify the estimated 4.8MM companies with an

inactive website. Other releases include improvements to location data

extraction and location data accuracy. Other north star goals supported

include *Credits per Record under Management* via our work integrating 8

(and counting) datasets into GTM attribute store and *Seller AI

inferences per record under management* via embedded support to

integrate Mellifera crawling capabilities into the agentic platform

(i.e., the service to power agentic search).



#### **Key Learnings**



We aren't squeezing enough juice out of the data that's available to us.

First, our only production crawler pipeline (M5) serves a maintenance

role only (name, description, domain status) but does not improve

profile depth and 'new domain' crawls are supported manually (about 15%

of team time). We have better extraction techniques and we need to use

them. We also lack a centralized metadata repository meaning analysis

can't determine if/when domains were crawled, engineering can't trace

data provenance for debugging, and match service has no real-time status

lookup.



Second, downstream pipelines aren't leveraging everything we can

provide. We have multiple 3P sources with millions of company records

that we haven't touched (e.g., Predict Leads) and other datasets which

could improve attribute coverage (e.g., EINs via Form 5500). If we have

a source validated, and high-confidence matches, it should be easy to

fill in core company/person attributes.



Third, we need more flexible schemas which support new dataset

opportunities. Locations, for example, must be tied to a company when

they should be their own independent entity; an office building doesn't

disappear when a tenant moves out but that's how we treat it. Making

this change would allow us to add attributes that better represent

relationships e.g., owner(s), lessor(s), service provider(s). Similar

challenge with job roles---people can have multiple jobs but we require

a single primary job. This leads to duplicate person profiles (e.g.,

multiple Elon Musk's).



#### **Hypotheses & Results**



[Hypothesis:]{.underline} We can use DNS signatures from major parking

services (e.g. GoDaddy, Sedo) including their known IP addresses to

identify inactive websites to improve data quality.



- [Results:]{.underline} Validated. We built a reference table of these

  signatures and confirmed that (i) a large number of active company

  profiles had websites with matching signatures (\~8% of total)

  and (ii) 9 out of the top 10 signatures had no false positives (100%

  of sites were indeed parked).



- [Action:]{.underline} Added parked domain identification to our domain

  vitality crawler (released in October).



[Hypothesis:]{.underline} There is a meaningful opportunity to improve

how we collect scoops/signals from news. Specifically, we can increase

yield, and improve efficiency by using the data researchers have already

annotated in 'Review Room'.



- [Results:]{.underline} \~80% of signals are derived from scoops-based

  data (high value). \~75% of snippets are discarded (duplicates, not

  relevant) and little automation exists today (top-of-funnel). Cost per

  scoop exceeds \$3.00. The data is available (snippet, types, topics,

  reject reason, etc.).



- [Action:]{.underline} PRD created for data science to develop

  classifier/ML models to improve the amount of data we collect from

  news and reduce the cost per data point. Data science will begin

  scoping this work in October (we will present the biz case before

  investment).



  - Identify all scoop candidate types within an article → *improve

    yield*



  - Determine relevancy w/ same discretion as a human → *increase

    throughput*



  - Determine if a scoop already exists → *reduce cost per scoop*



*\[A bunch more i can add but writeup was too long so removed\]*



#### **Go-forward Changes & Plan**



First, I want build automation into our crawler system to (i) improve

transparency through a centralized repository which ingests URLs from

every source (3P, match service, batch) and has crawl metadata (domain

status, last crawl/next crawl date, crawl/extraction method, etc.) to

enable self-service debugging and reduce support needed from our team,

(ii) make it easier to submit domains to our crawler queues via

standardized REST/streaming APIs so teams can do it programmatically,

(iii) add intelligent scheduling using ML-based recrawl logic to

prioritize high-value Tier A/B companies and reduce frequency for

low-value domains and (iv) implement multi-agent extraction starting

with our most-pressing gaps (locations, leadership).



Second, I want to execute the remaining low-hanging-fruit opportunities.

This includes 1) coverage enhancements---'orphaned companies' (1.4MM

est. new companies + many attribute additions), Predict Leads (151MM

URLs), CN5 (80M+ remaining partial records, in-progress) and 2)

completeness improvements (i.e., leveraging the 3P data we are ingesting

in GTM store in our core company/person datasets).



Finally, I want to improve how/what we capture from news and non-company

websites. This would include migrating off of our Nutch/Cogilex-based

crawlers ("Legacy Crawlers"), increasing coverage of news sources (not

comprehensive today) and piloting the collection of 'notable events'

(see pic below). Somewhat parallel to this would be improvements to our

financial datasets---adding dedicated crawlers to capture portfolio

companies from investor websites

([[example]{.underline}](https://www.norwest.com/companies/?_sft_companies_status=active))

and creating the pipelines to ingest IAPD (investors), Form ADV (private

funds) and Form D (actively fundraising). A first step towards eating

PitchBook's lunch.



*Notable events & example news snippets:*



![](media/image1.png){width="6.5in" height="1.3888888888888888in"}



#### **Leveraging AI**



AI is integrated in almost every part of my work. Personally, the

greatest value has been using ZI Chat to extract relevant information

from our internal knowledge base---specifically answering questions

about tech/services (e.g., normalization), data pipelines, schemas and

how/where data is stored. Some specific examples include Data tZar agent

for GTM store schema creation and an agent I created to monitor the 20+

slack channels we have with external 3P data providers to identify any

potential risks to our pipelines (e.g., changes to schemas, fields).

It's been especially useful with voice dictation to rattle off all the

necessary context. Outside of personal efficiency, there is a big

opportunity in data extraction via multi-agent orchestration (chain of

specialized agents). You can learn more about an initial application of

that

[[here]{.underline}](https://discoverorg.atlassian.net/wiki/spaces/MLE/pages/202086318472/Agentic+Address+Extractor+AAE+Design+Document).

