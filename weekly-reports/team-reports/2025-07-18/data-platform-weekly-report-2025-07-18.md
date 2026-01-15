---
id: weekly-data-platform-2025-29
title: "GTM Data Platform Weekly Report - July 18, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-07-18
updated: 2026-01-06
week_ending: 2025-07-18
reporting_period: "July 14-18, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Data Platform Team Executive Roundup - 7/14/25**

## **Executive Summary**

We reached a decision this week on field-level encryption, strategically
deferring implementation to accelerate our Query API delivery. Marc
Delurgio\'s analysis confirmed encryption requirements should be opt-in,
and not applied to all customers since, with encryption, there will be
functional limitations for things like search. This decision, combined
with Adwait Kirtikar\'s successful alignment with the UI Design team on
Unified Profile portal scope, positions us to progress Unified Profiles
in Q3.

## **This Week\'s Progress**

### **Key Momentum Areas**

Marc Delurgio deferred field or table-level encryption so as not to put
the Query API at risk for Workbooks GA. This clarity enables us to move
forward with GTM platform development without compromising future
enterprise capabilities.

Adwait Kirtikar achieved breakthrough alignment with the UI Design team
on Unified Profile scope, securing Yoav Broum\'s commitment to detailed
ticket-level scoping that directly enables Q3 planning. The portal
design will allow tenants to configure survivorship workflows and
account matching preferences, delivering the foundational customization
capabilities that are the functional foundation of our Unified Profile
offering.

Menna Rashwan advanced Enterprise Search platform readiness by defining
the integration path for Account Fit Score (AFS) and pushed forward
cross-surface UX alignment between Advanced Search and Workbooks. Her
work with Engineering on H2 priorities established shared understanding
of technical feasibility and key dependencies, setting the stage for
coordinated execution across multiple product surfaces.

### **Goals & Progress**

**Security Architecture & Compliance**: Request from the security team
for Linda Johannessen\'s to do encryption requirements definition was
deferred while we focus on Query API in support of Workbooks GA.

**Unified Profile Development**: Milestone 1.6 planning reached full
alignment with Adwait Kirtikar securing UI Design team commitment for
portal development that enables tenant configuration of survivorship
workflows and account matching preferences. The design team\'s ability
to scope detailed tickets represents a critical step toward Q3 delivery,
with clear ownership boundaries established across engineering and
design teams.

**Enterprise Search Platform**: Menna Rashwan completed the H2 Product
Review with Engineering, identifying technical feasibility and key
dependencies while defining the path to consume and expose Account Fit
Score within Enterprise Search. The cross-surface UX design alignment
for Advanced Search and Workbooks creates a unified Enterprise Search
experience that reduces fragmentation and improves adoption potential.

### **Strategic Challenges**

Our dependency on Legal, Security, and GTM Store API engineering leads
for security requirements definition continues to create uncertainty
around our compliance architecture, with Linda Johannessen requiring
input from Sales and Customer Success contract insights to properly
scope customer expectations. The decision to defer field-level
encryption helps in the short term, but we need executive clarity on the
timeline for comprehensive security architecture implementation to
maintain enterprise sales momentum.

Resource allocation for H2 planning is creating bottlenecks as multiple
initiatives require engineering lead input simultaneously, with Linda
Johannessen\'s Query and Metadata API initiative definition dependent on
the same engineering resources that Menna Rashwan needs for Enterprise
Search technical feasibility assessments. The Step 3 Product &
Engineering Execution Playbook process is thorough but
resource-intensive during planning cycles.

Cross-functional coordination complexity is emerging as Menna Rashwan\'s
Enterprise Search integration spans multiple product surfaces, requiring
synchronized execution between Advanced Search, Workbooks, and core data
platform teams. While alignment is strong, the execution risk increases
with the number of dependent teams and the need for unified UX design
across different product areas.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Account Fit Score integration research uncovered opportunities to
accelerate the deprecation of fragmented ICP features by positioning AFS
as the unified, ML-powered scoring signal within Enterprise Search.
Menna Rashwan\'s analysis shows this approach reduces manual
configuration burden while delivering more intelligent account
prioritization, aligning with our strategy to unify prospecting
workflows through data-driven targeting.

The H2 planning process is revealing the interconnected nature of our
platform initiatives, with Linda Johannessen\'s API strategy work
directly enabling Menna Rashwan\'s Enterprise Search integration and
Adwait Kirtikar\'s Unified Profile development. This interconnectedness
suggests opportunities for accelerated delivery through coordinated
execution, but also highlights the risk of cascading delays if key
dependencies are not properly managed.

### **Cross-Team Dependencies**

Our work with the UI Design team on Unified Profile portal development
represents a critical partnership for Q3 delivery, with Yoav Broum\'s
design team commitment enabling detailed scoping and timeline
integration. Adwait Kirtikar\'s successful alignment creates a template
for engaging design resources on complex platform initiatives, though we
need to ensure design capacity allocation matches our H2 delivery
timeline.

The Enterprise Search platform integration spans multiple engineering
teams, with Menna Rashwan coordinating across Advanced Search,
Workbooks, and core data platform teams to deliver unified UX design.
This cross-functional approach accelerates platform adoption but
requires careful coordination to prevent integration complexity from
delaying individual product deliverables.

## **Looking Ahead**

Next week\'s focus centers on completing H2 initiative definitions and
securing engineering commitment for our core platform layers, with
particular emphasis on Query and Metadata APIs that enable downstream
product development.

Linda Johannessen will finalize Step 3 initiative definitions for Query
and Metadata API layers, working with engineering leads to establish
clear problem statements, approaches, and completion criteria that
enable accurate effort estimation and cross-team alignment. The
completion of these definitions unlocks planning clarity for one of our
most critical GTM platform layers and prevents downstream ambiguity that
could compress execution timelines.

Menna Rashwan will continue advancing Enterprise Search platform
readiness by deepening the Account Fit Score integration planning and
coordinating UX design alignment across Advanced Search and Workbooks.
Her work establishing shared understanding with Engineering on H2
priorities positions us for clear milestone planning and coordinated
execution that reduces fragmentation across our search capabilities.

Source: Operating Document entries from 7/14/25-7/18/25
