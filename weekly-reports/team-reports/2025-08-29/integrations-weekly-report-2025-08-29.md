---
id: weekly-integrations-2025-35
title: "Integrations Weekly Report - August 29, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-08-29
updated: 2026-01-06
week_ending: 2025-08-29
reporting_period: "August 25-29, 2025"
tags: ["weekly-report", "Q32025"]
---

# **\[Integrations Executive Roundup - \[8/25/25\]**

## **Executive Summary**

Sanyog's team reached 500 tenants now enabled for email/calendar with
automatic GTM contact creation. Erica continued end-to-end testing for
GTM custom fields while finalizing grooming for H2 features ahead of
maternity leave (Congrats!). Prateek integrated Account AI Summary with
Agentforce
([[DEMO]{.underline}](https://drive.google.com/file/d/1AsaJxh3g-9Et5M5fl0FtXhBoakEN-Nq6/view?usp=sharing)
Available) and demonstrated significant impact through ADA Bot POC
([[DEMO]{.underline}](https://zoominfo.slack.com/archives/C01NA8B3R28/p1756400408831729)
Available) in addition to driving progress on Vertical Data Set
marketplace.

## **This Week\'s Progress**

### **Key Momentum Areas**

Erica\'s multi-channel [[CRM
update]{.underline}](https://zoominfo.slack.com/archives/C01NA8B3R28/p1756403907005789)
campaign clarified the benefits to all features that migrate to GTM DM,
and started to build clarity into where teams are today, and which teams
are missing a migration plan.

Prateek integrated Account AI Summary with Agentforce
([[DEMO]{.underline}](https://drive.google.com/file/d/1AsaJxh3g-9Et5M5fl0FtXhBoakEN-Nq6/view?usp=sharing)
Available) and demonstrated significant impact through ADA Bot POC
([[DEMO]{.underline}](https://zoominfo.slack.com/archives/C01NA8B3R28/p1756400408831729)
Available), which is available behind a feature flag and should
replicate the success the login support team saw where implementation on
login page drove 80% reduction in support tickets.

Sanyog\'s team enabled email and calendar data for 500 tenants despite
laptop security lockouts and provider API challenges, establishing the
foundation for downstream applications to leverage engagement data in
GTM Data Model for improved ROI reporting and cross-platform analysis.

### **Goals & Progress**

**CRM Data Migration**: Backend infrastructure for custom field to
standard object mapping completed and deployed to production Monday.
End-to-end testing continues with some environmental challenges, but the
system is ready for customer onboarding with manual backend
configuration if needed. Team 6 is transitioning to product and
opportunity line items next sprint while maintaining flexibility to
prioritize custom objects based on customer adoption patterns.

**Dataset Marketplace Development**: Prateek aligned with Linda\'s team
on API requirements for both internal and external marketplace
functionality. Development team has clear directive to create initial
visualization using current APIs within one week, even without complete
metadata, to demonstrate workflow and gather feedback. October delivery
target remains on track despite holiday delays pushing enterprise
customer discovery calls to post-Labor Day.

**GTM Data Model Adoption**: Migration tracker showing improved
visibility into use cases and data source dependencies, though still
primarily text-based rather than dashboard format. Asaf is working on
converting this to actionable metrics with proper tenant counts from
Mongo. The AI account summary team transition is providing cleaner
alignment on GTM data model API usage as the North Star architecture.

### **Strategic Challenges**

Testing environment instability is impacting custom field validation due
to multiple historical Salesforce connections creating data
cross-contamination in workbooks. The challenge stems from inability to
purge old data without breaking existing customer workbooks, requiring
Erica to establish entirely new custom field configurations. This
pattern reveals a broader need for clean environment management and
customer instance migration processes.

Advanced search dependency mapping remains unclear as teams prepare for
Org Import pipeline deprecation. While the migration tracker provides
use case visibility, the transition plan for 40,000 customers currently
using advanced search requires coordinated communication and technical
support.

Cross-team coordination on master suppression lists is surfacing
architectural decisions about whether opt-out data should remain in
separate datasets or integrate directly into GTM Data Model. This
impacts workbook functionality for contacts without ZoomInfo IDs and
requires resolution before advanced search migration can proceed without
customer impact.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Testing revealed that multiple CRM instance connections create
downstream workbook dependencies that prevent data cleanup, highlighting
the need for proactive customer migration processes. Erica\'s discovery
that purging historical Salesforce data would break existing workbooks
demonstrates the importance of designing clean separation between
customer environments from the beginning.

Account matching logic requires fundamental improvement as current
hard-coded rules are failing to associate activities with correct
opportunities, particularly impacting MEDIC data accuracy. The
assumption about latest close dates correlating with newest
opportunities doesn\'t reflect actual sales patterns, where activity
typically intensifies near deal closure rather than at opportunity
creation. Sanyog plans to extend AAT logic to customers to solve this.

The shift from schema service to GTM Store APIs represents a critical
architectural migration that all app teams must complete. Prateek\'s
discussions revealed that workbook team and other application teams
built dependencies on the Global Mapping Service that now need
systematic migration to maintain filtering and relationship
identification capabilities.

### **Cross-Team Dependencies**

Our work with the workbook team on custom field implementation continues
to be critical for September 1st delivery commitments. Current testing
challenges require collaboration on data purging processes and
environment isolation to prevent customer impact during development
phases. The team needs support in establishing cleaner testing workflows
that don\'t interfere with production workbook configurations.

Coordination with Linda\'s GTM Store team is essential for marketplace
API development and broader data architecture decisions about where to
persist GTM config information. The Wednesday meeting with Adi\'s team
will determine storage strategies for messaging, positioning, buyer
personas, and competitor data that impact multiple product development
streams.

## **Looking Ahead**

September 1st represents a critical milestone for custom field delivery
that enables broader Oregon Port deprecation planning and customer
migration communications.

The team will focus on completing custom field end-to-end validation
through new testing configurations. Sanyog will share an Engagement
update mirroring the one Erica shared. Prateek will drive dataset
marketplace UI execution while conducting enterprise discovery calls
with Red Hat and ADP to identify high-value Agentforce use cases. Sanyog
will complete email/calendar enablement for remaining tenants and
develop the account matching PRD that leverages AAT configurability for
improved opportunity association accuracy. The focus on systematic
migration away from legacy pipelines positions the team to deliver on
2025 consolidation goals while maintaining customer experience quality.

*Source: Team 1-2-3 Operating Framework entries from 8/22/25 - 8/29/25*
