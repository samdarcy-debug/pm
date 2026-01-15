---
id: weekly-gtm-studio-2025-39
title: "GTM Studio Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

# **GTM Studio Executive Roundup - September 26, 2025**

## **Executive Summary**

The GTM Studio team delivered significant progress across all five
workstreams this week. **Workbooks** achieved major user validation
breakthroughs with Jagannath\'s agent testing revealing enrichment
capabilities working well while identifying UX challenges in query
building, and Tanvi\'s signals work progressing toward September 30th
production release despite operator dependency blockers. **Plays**
advanced with Mohan securing stakeholder alignment on activation
requirements and Neha establishing strategy documentation for top 10
plays with engineering kickoff planned. **ROI Analytics** hit major
milestones as Arun shipped memo and self-serve analytics features to
production while continuing data migration at 70% completion, supported
by a major \$5 million TCV Indeed expansion story demonstrating ROI\'s
business impact. **Data Management** progressed substantially with
Corina completing PRD reviews for Enrich premium plus and deploying Data
health scan proof of concept to account managers for real customer
validation. **GTM Config** initiated active development as Tingting
kicked off engineering work with established timelines for October 3rd
week customer validation and resolved UI scope alignment with
stakeholders.

## **This Week\'s Progress**

### **Key Momentum Areas**

Arun\'s team achieved a significant milestone by releasing memo and
self-serve analytics features to production, positioning the team to
enable customer rollout next week after internal review and testing. The
GTM data store migration continues progressing steadily with issues
identified and being actively addressed by the engineering team. No
major blockers here.

Corina advanced data management initiatives by completing a successful
PRD review for Enrich premium plus on Ringlead for Hubspot support, with
most engineering work already completed under feature flags. The team
handed off Data health Scan (DHS) proof of concept to account managers
for upsell conversations with Ringlead customers, generating valuable
feedback that led to a second iteration now available for testing.Work
being done in partnership with data science/analytics team under Chad
Herring.

Tingting initiated agent development for GTM configure with Monday\'s
kickoff, establishing clear workback plans with granular week-by-week
details. The team achieved important alignment with Rowan on UI scope,
eliminating the GTM context library requirement and focusing on a single
set of visual views, which streamlined the design approach
significantly.

### **Goals & Progress**

**Workbooks**: Jagannath and Tanvi achieved significant validation
milestones with mixed learnings from agent testing. Jagannath onboarded
15 users for agent testing and discovered that enrichment capabilities
work exceptionally well, with users appreciating automated prompt
generation and appropriate data source selection. However, the studio
chat query building experience revealed fundamental challenges with CRM
data model integration, particularly evident when Alex Lazerowich's
struggle with account queries that consistently failed. The team
identified the need to optimize logic for switching between data model
and Salesforce API integration. Tanvi progressed signals work toward
September 30th production release despite operator dependency
challenges, with workarounds enabling limited customer access for
testing. She also advanced amplitude taxonomy work with the BI team,
prioritizing P1 and P2 business questions for engineering handoff.

**Plays**: Mohan and Neha established a strategic foundation and began
execution planning for automation capabilities. Mohan secured
stakeholder alignment with Sean from Copilot and Marc for Route on
activation requirements, completing multiple engineering review rounds
and preparing for next week\'s implementation kickoff. The team defined
two milestones: lift-and-shift of DoubleO workflow capabilities into GTM
studio with light reskinning, followed by workbook integration enabling
direct activation paths. Neha completed strategy documentation for the
top 10 plays identified earlier and planned engineering kickoff to begin
replication work within the platform, documenting current gaps and
defining integration approaches for studio implementation.

**ROI Analytics**: Arun delivered major production milestones while
advancing data infrastructure initiatives. The team successfully
released memo and self-serve analytics features to production, pending
next week\'s internal validation before customer enablement. GTM data
store migration reached 70% completion with active issue resolution
between teams. The workbook ROI initiative advanced with design
readiness approaching completion. ROI analytics gained significant
validation through the \$5 million Indeed renewal story, where ROI
insights directly influenced converting a one-year contract into a
three-year deal with substantially increased spend, demonstrating clear
business impact, when effectively deployed by GTM team members.

**Data Management**: Corina advanced multiple customer-facing
initiatives with strong validation focus. The team completed a
successful PRD review for Enrich premium plus on Ringlead for Hubspot
support, with most engineering work already completed under feature
flags. Data health scan proof of concept moved into real-world testing
as account managers began using it for upsell conversations with
Ringlead customers, generating valuable feedback that led to a second
iteration now available. Next week targets deployment to priority
customers (Q4/Q1 renewals, strategic enterprise and mid-market segments)
before expanding to the remaining 3,700 customers identified for
cross-sell/upsell. Job posting data remains blocked pending operator
updates affecting signals and CRM data across workbooks.

**GTM Config**: Tingting initiated active development phase with clear
validation strategy and timeline. The team completed engineering kickoff
on Monday with development beginning this week, supported by established
PRD and granular week-by-week workback plans. First customer validation
is scheduled for October 13th week, combining design prototypes with
initial functionality for customer review. The team achieved important
alignment with Rowan on UI scope, eliminating GTM context library
requirements and focusing on single visual views. Tingting also
established evaluation frameworks for measuring agent impact and
accuracy, with plans to test different integration flows and narratives
with customers to determine optimal user journey approaches.

### **Strategic Challenges**

Jagannath\'s agent testing with 15 internal users revealed fundamental
UX challenges in the studio chat experience where users struggled with
CRM data model queries. Alex Lazerowich's testing specifically
highlighted issues with account queries where the data model
consistently failed to return results, requiring fallback to Salesforce
API integration. The team needs to optimize the decision logic for when
to switch between data model and direct CRM integration based on user
frustration signals.

Engineering resource allocation across multiple high-priority
initiatives creates scheduling tensions, particularly affecting signals,
job posting data, and activation workstreams. The same engineering teams
support all GTM initiatives, requiring careful prioritization and stack
ranking. Mohan noted this impacts timeline predictability for
later-priority items.

Tanvi\'s signals work faces partial blocking due to operator updates
required across multiple data types. While the team identified
workarounds enabling next week\'s release, the dependency on operator
updates affects both signals and job posting data initiatives, requiring
contingency plans for customer access with known limitations.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Agent enrichment capabilities demonstrated strong user adoption and
satisfaction during internal testing, with users appreciating the
automated prompt generation and appropriate data source selection.
However, the initial query building experience in studio chat revealed
significant gaps between user expectations and current data model
capabilities. Users expect seamless preview-to-enrichment workflows
similar to workbook patterns, but current UX creates confusion about
preview versus execution phases.

Testing revealed that users don\'t naturally distinguish between
agent-created previews and enrichment execution, mirroring early
workbook adoption patterns. The team identified need for enhanced user
guidance, potentially implementing a plan-then-execute model similar to
deep research tools that build visible execution plans before proceeding
with analysis.

The \$5 million Indeed renewal story validates the outcome-oriented
product approach for driving customer value. The GTM team leveraged ROI
insights to convert a one-year deal into a three-year contract with
significantly increased spend, demonstrating how product capabilities
directly influence enterprise sales outcomes. This reinforces the
importance of designing backward from customer value outcomes rather
than feature functionality.

### **Cross-Team Dependencies**

Engineering capacity constraints require coordination across multiple
Studio initiatives since the same teams support multiple GTM projects.
The team established weekly prioritization discussions to stack rank
work, with expectation that post-October 6th should unlock additional
capacity for Q4 initiatives.

Signals and job posting data depend on operator updates affecting
multiple data types across workbooks platform. Until these foundational
updates complete, both initiatives face partial blocking despite
workaround solutions enabling limited customer access for testing
purposes.

## **Looking Ahead**

Next week focuses on customer enablement and validation across multiple
workstreams while continuing internal testing refinements. The team will
prioritize getting production features into customer hands and gathering
real-world feedback to guide development decisions.

Arun will complete enablement materials for memo and self-serve
analytics features while continuing data migration testing and expanding
workbooks ROI development. Corina plans to expand Data health scan
deployment to 270 priority customers and advance Enrich premium plus
milestone deliverables for Hubspot and Microsoft Dynamics. Tingting will
focus on engineering team coordination and customer validation strategy
development, while Jagannath makes the go/no-go decision on agent
capabilities based on testing insights. The team will also address data
model versus Salesforce API integration logic and consider implementing
plan-then-execute UX patterns for improved user experience.

Engineering resource availability should improve after October 6th,
enabling acceleration of Q4 delivery timelines across all initiatives.
The team remains confident in delivering substantial customer value
through the combination of production features, validated agent
capabilities, and enhanced data management tools.

*Source: Team 1-2-3 Operating Framework entries from September 22-26,
2025*
