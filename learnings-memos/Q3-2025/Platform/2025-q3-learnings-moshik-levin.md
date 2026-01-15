---
id: learnings-2025-051
title: Q3 2025 Learnings Memo - Moshik Levin
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/moshik-levin]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



This quarter, we (Match team) collaborated with the Company Data team to

refactor location matching in offline enrichment and Company Master Data

Enrich API. That work is code-complete and will ship in early Q1, while

we work to bring location matching to more places. Together it directly

ladders to two North Star and driver:



1.  **Credits per Record under Management** -- should rise as higher

    match accuracies and newly enabled location-based enrichments (e.g.

    Workbooks) increase customer trust and eligible enrichments per

    record



2.  **Company Perfect Accuracy Rate** -- will improve via more precise

    company↔location resolution and entity resolution for New Company

    Creation, reducing false merges/splits



#### **Key Learnings**



I only joined this quarter and am still processing these thoughts, so

they are not fully formed yet:



Our customers think in terms of accounts with locations and hierarchies.

Our services and products, however, use a stricter Persons and Companies

taxonomy, which accordingly is the job the match service is designed for

-- it was built for strict Company OR Person matching. That mismatch

affects the experience. To align customer goals with our experiences, we

should all collaborate to connect the layers (experience ↔︎ services ↔︎

data) into a more dynamic matching flow:



1.  Let APIs and experiences dynamically support different matching jobs

    and offer more controls for enrichment outcomes



2.  Update match APIs to support those jobs and controls or be better at

    predicting the job



3.  Adapt the corpus and collections of Persons and Companies to align

    with accounts and company hierarchies



#### **Hypotheses & Results**



1.  Hypothesis: There is a need for a unified matching API to address

    various entity matching requirements in a single service\

    \

    I\'ve learned that there\'s a nuance to this: we don\'t need to

    consolidate every matching capability under a single endpoint.

    People and agents work well with purpose-built APIs (e.g. one for

    people, another for companies, a third for internal entity

    resolution). The problem is ZoomInfo\'s fragmented internal matching

    for the same purpose. We get RingLead escalations because people

    don\'t know it uses different location matching under the hood.

    Additionally, We need to tell Match API clients which corpus of an

    entity they\'re targeting (e.g. with or without low quality results)



2.  Hypothesis: Customers desire finely granular transparency in the

    matching process, with insights into scoring and reasons for

    matches\

    \

    True, but for many customers it\'s not a needed tool; it signals a

    lack of trust in our accuracy. That keeps them from \"leaning

    back\", verifying results instead of saving time. Objectively, they

    want warnings for outcomes needing stewardship, not granular,

    low-level insights



#### **Go-forward Changes &** **Plan**



We need to synthesize all requirements for ZoomInfo\'s matching services

and define the ideal end state: services, controls, and

collections/entities that need matching. Then we can map the unification

paths, and tie it to the larger Data initiative of schema unifications



#### **Leveraging AI**



Two use cases where ZI Chat amazed me were:



1.  Customer segmentation and insights: I used ZI Chat to pull real

    customer feedback and then explored the transcription further in

    Chorus. Starting a new role, I wanted to meet customers who use my

    products but couldn\'t find a joining process. Using ZI Chat instead

    was a game changer that unlocked far more insights for me, and

    helped me ramp up far faster than in previous new roles



2.  SFDC record retrieval: I needed a list of customers still using API

    fields we\'re planning to deprecate. Building a Salesforce report

    wasn\'t working, so I used ZI Chat to pull dozens of records and

    generate a complete and sound table with account IDs, names, and

    owners -- it only took five rounds of prompting to get to the right

    lookup field



In Q4, I want to:



1.  Automate repetitive workflows with agents



2.  Explore an idea to build agents representing different Match Service

    client types so I can test how they perceive proposed changes

