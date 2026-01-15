---
id: weekly-integrations-2025-36
title: "Integrations Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Integrations Team Executive Roundup**

Week of September 1, 2025

![ZoomInfo Logo](media/image1.png){width="0.6944444444444444in"
height="0.6944444444444444in"}

Erica Fienman\'s CRM Import Rules feature (behind FF in Production)
removed "free-trial" accounts for our internal GTM Studio instance,
deflected a Apollo-churn risk from Zoom, and should simplify the
Workbooks "Owner Manager" issue. Prateek Paikray successfully
demonstrated the Dataset Marketplace UI to product and engineering
leadership and passed ZI's Agentforce package through security review in
record time (2 weeks). Sanyog Rai finalized an engagement roadmap and
migrated another 200 tenants with Outlook Email to GTM DM.

## **This Week\'s Progress**

### **Key Momentum Areas**

Customer Retention Win: Import Rules functionality directly prevented
Zoom from churning to Apollo after their Salesforce integration failed
two years ago. Andres Perez is working with the customer to configure
the logic properly, demonstrating immediate business impact from our GTM
data model infrastructure investments.

AI Solutions Foundation: Prateek Paikray successfully demonstrated the
Dataset Marketplace UI using mock data to product and engineering
leadership on Wednesday and gathered critical feedback for the
Agentforce solutions. This positions us well for Dreamforce with
concrete AI use cases validated by enterprise customers.

Strategic Alignment: Sanyog Rai completed an engagement roadmap,
creating clear 6-8 month visibility for engineering teams and
establishing monthly leadership meetings to empower engineers with
product decision-making authority. This structural change addresses
historical gaps in engineering team empowerment.

### **Goals & Progress**

#### **GTM Data Model Migration**

Engagements pipeline consolidation is progressing with clear roadmap
artifacts completed by Sanyog Rai and alignment achieved with
engineering teams. The team identified that Import Rules will also solve
internal tenant data quality issues by filtering non-sales users from
Salesforce ingestion, addressing the Owner-Manager hierarchy problems
discovered in workbooks implementation.

#### **Agentforce & AI Solutions**

Dataset Marketplace demonstration was successful with product leadership
providing feedback on the UI experience. Prateek Paikray is actively
conducting enterprise customer discovery calls, with one major software
provider expressing interest in 5 different AI use cases, particularly a
\"deal assistant agent\" that leverages engagement summary data tied to
CRM opportunities.

#### **Partnership & Integration Efficiency**

ChiliPiper announcing a new integration as more partner build to our ZI
API in record time.

### **Strategic Challenges**

Chorus Engineering Focus: The team identified that Chorus engineering
continues receiving requests for Chorus-specific functionality that
doesn\'t advance GTM data model migration or app deprecation goals.
Sanyog Rai and Andres Perez are implementing clearer escalation
processes to empower the engineering team to decline non-strategic work
that causes context switching and delays core objectives.

Data Compliance Process Gaps: Prateek Paikray discovered that churned
customer data continues being ingested into ZDP after cancellation, with
no clear automated deletion process. Current manual deletion costs
approximately \$1,000 per tenant, highlighting the need for improved
churn status definitions and automated data lifecycle management
processes.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Owner-Manager Implementation Reality: Workbooks implementation revealed
that recursive user hierarchy queries break due to non-sales user
ingestion from Salesforce. Users without manager IDs (chatter,
marketplace users) are incorrectly classified as C-suite, causing system
failures. This validates the Import Rules approach for filtering
relevant users at ingestion.

Engineering Team Empowerment Value: Sanyog Rai\'s establishment of
monthly engineering leadership meetings is already showing benefits,
with engineering leads providing more strategic product insights.
Historical lack of empowerment in the Chorus team specifically has
limited their ability to contribute to product decisions despite having
deeper technical context.

AI Use Case Validation: Enterprise customer conversations consistently
center on engagement summary data linked to CRM opportunities, not just
accounts. This insight from Prateek Paikray\'s customer discovery work
highlights the importance of improving our opportunity-engagement
linkage logic to support AI agent functionality effectively.

### **Cross-Team Dependencies**

Our work with the Data Platform team on GDPR-compliant data deletion
APIs remains critical for scaling compliance processes efficiently. The
current manual approach is both expensive and operationally intensive,
requiring automated solutions to handle churned customer data lifecycle
management.

Collaboration with GTM Store Engineering continues smoothly for Dataset
Marketplace backend API development, with Prateek Paikray providing
clear requirements based on product leadership feedback and enterprise
customer use cases.

## **Looking Ahead**

Andres Perez will work on a POC for auto-mapping custom fields to
minimize admin dependencies for Workbooks launch on September 23rd.

Prateek Paikray will continue enterprise customer discovery while
collaborating with GTM Store Engineering on Dataset Marketplace backend
development. The goal is establishing clear API specifications that
support the deal assistant agent use case identified by enterprise
customers. Success metrics include having functional API endpoints and
at least two additional customer validation sessions completed.

The team maintains strong momentum with clear strategic alignment and
demonstrated business impact. The combination of immediate customer
retention wins, infrastructure progress, and validated AI use cases
positions the Integrations team to deliver significant value across
multiple strategic initiatives simultaneously.
