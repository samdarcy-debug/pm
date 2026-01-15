---
id: learnings-2025-054
title: Q3 2025 Learnings Memo - Sanyog Rai
type: doc
status: approved
team: platform
owner: '[[teams/platform/_people/sanyog-rai]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- platform
related: []
---
#### **Metric Alignment**



**Primary North Star Sub-Driver: Core Engagement Records** *At least 1

new Core Engagement record (Email Send/Receive, Calendar Event, Meeting

Recording) ingested in EACH of the prior 4 weeks*



**Key Contributions:**



- **100% Tenant enablement** for email/calendar data flowing into GTM DM

  for tenants that have email/calendar integrations connected



- **\~275K contacts created per week** from GTM Engagements, enabling

  persistence of greater engagement volume without CRM dependency



- **Schema finalization** for Content Interactions and engagement tables

  to support expanded data types



These efforts will directly support the company North Star (Active

Integrations) by building the technical foundation for customers to

derive value from integrated engagement data. We are currently building

foundational infrastructure. Once complete, we\'ll shift focus to

feature development that directly drives customer value and increases

engagement integration adoption.



**Q3 Performance:** Increased from 17% to 20% (+3pp) - representing

progress in engagement data integrations, without even having the

infrastructure work we're working on implemented.



#### **Key Learnings**



**1. Legacy engagement data has severe limitations that constrain

product value.** Chorus doesn\'t retain full meeting attendance (only

speakers), filters out emails without account matches, excludes

cancelled meetings, and lacks Internet Message IDs for deduplication.

These gaps require us to build new infrastructure rather than enhance

legacy systems.



**2. Account/Contact creation from engagements is not optional - it\'s

foundational.** Many customers don\'t have all accounts they\'re

engaging with in their CRMs, some have not connected their CRMs or lack

CRMs entirely. Without the ability to create accounts/contacts from

engagement data, we miss substantial engagement capture opportunities.

This validates the hypothesis that virtual CRM creation is a major

differentiator for GTM DM.



**3. Testing infrastructure is a material risk to expansion.** We lack

robust testing for third-party integrations we don\'t use internally

(Outlook, etc.). Current approaches are insufficient for validating

integrations at scale, directly threatening our timelines and risking

issues in the future.



#### **Hypotheses & Results**



**1. Hypothesis: Unified infrastructure across GTM DM will accelerate

time-to-market for new engagement features**



- **Result:** We are still building out infrastructure but it seems that

  Co-Pilot Chat integrated meetings data in one week using the same

  query API as all other customer data. We're hoping other teams will be

  able to see expedited results as well once we have the infrastructure

  fully built.



- **Impact:** Validates strategy to build all new engagement features in

  GTM Studio/Co-Pilot rather than enhancing legacy products.

  Infrastructure unification is a force multiplier for product velocity.



**2. Hypothesis: Legacy engagement data sources would provide adequate

coverage for customer use cases in the near term**



- **Result:** Discovered significant data gaps: Chorus missing full

  attendance, filtered emails, cancelled meetings; Engage missing

  Internet Message IDs. These limitations prevent us from delivering

  competitive engagement intelligence.



- **Impact:** Infrastructure development has taken longer than expected

  due to these data quality gaps



3\. **Hypothesis:** Customer CRMs are missing many of the contacts they

are engaging with.



- **Result: 270k contacts created in GTM DM per week** across all active

  importing tenants. Once we have account creation this number will be

  even greater.



- **Impact:** Once we enable customers to access and export this data,

  it will be a significant differentiator for GTM DM.



#### **Go-forward Changes & Plan**



1.  **Account Creation from Engagements** - Complete the virtual CRM

    capability that differentiates GTM DM



2.  **Upsert API for Content Interactions** - Enable clean data

    ingestion and deprecate legacy ETL paths



3.  **Recording data in Production** - Complete the third leg of Core

    Engagements (Email, Calendar, Recordings)



4.  **Testing Infrastructure** - De-risk expansion with proper

    validation for integrations



#### **Leveraging AI**



**Most Impactful Use This Quarter:** **Prototypes over PRDs.** Used

Claude for rapid UI/UX prototyping (improved CRM writeback pages),

requirements documentation, BigQuery analysis, schema design, and

customer communications. Prototype creation was most valuable -

validating approaches with stakeholders before committing engineering

resources saved significant time.



**Example:** Claude-assisted prototype for Admin Portal CRM writeback

improvements



Will continue to use AI to improve daily productivity but also try to do

more showing with prototypes and visuals created with AI.

