---
id: weekly-data-platform-2025-47
title: "GTM Data Platform Weekly Report - November 21, 2025"
type: weekly-report
status: approved
team: data-platform
owner:
created: 2025-11-21
updated: 2026-01-06
week_ending: 2025-11-21
reporting_period: "November 17-21, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Data Platform Executive Roundup - November 21, 2025**

## **Executive Summary**

The team locked in scope for Engagement data in the December 31st
GraphQL-\>Federated Search milestone, though engineering validation
continues and some use cases remain excluded. Marc Delurgio completed a
PM resource realignment to strengthen the dataset onboarding process,
with Moshik Levin taking point December 1st to drive more deliberate use
case reviews and streamlined schema alignment. Menna Rashwan and Linda
Johannessen finalized an initial MVP engagement use case list.

## **This Week\'s Progress**

### **Key Momentum Areas**

Marc completed the realignment plan of PM resources for dataset
onboarding, positioning Moshik to lead starting December 1st. The shift
addresses two pain points: establishing more deliberate use case review
across Data, Platform, and Apps teams, and streamlining schema
definition with faster stakeholder buy-in. Knowledge transfer is
underway from Linda to ensure continuity.

Menna scoped Engagement datasets for the December 31st Federated Search
milestone and defined an initial list of MVP engagement use cases. While
a second round of engineering validation is in progress and some use
cases are still pending product clarity, the foundation is solid. The
federated search milestone plan now reflects the updated scope, giving
teams visibility into what\'s included and what\'s deferred.

Moshik advanced the Regional HQ work by syncing with the Data team on a
shared long-term solution using existing data points for domestic
headquarters. Through ZI Chat, the team identified a better data point
for retrieving the exact location ID for a domestic parent rather than
relying solely on a flag. The first proof of concept should be ready
next week, pending validation with the research team.

### **Goals & Progress**

**GTM Platform - Federated Search Integration**: Menna and Linda
Johannessen finalized the scope of Engagement datasets and MVP use cases
for December 31st delivery, updating the milestone plan to reflect
feasibility and trade-offs. While the initial list provides a strong
foundation, engineering validation continues and the MVP scope may still
evolve. Excluded use cases include recursive search (pending technical
alignment), target accounts, website visit joins, territory data,
engagement sorting on aggregation outputs, and several engagement
aggregation scenarios. The updated plan gives stakeholders clear
visibility into what\'s being delivered and enables informed
prioritization.

**GTM Platform - Resource Planning**: Marc realigned PM resources to
expand capacity and deepen engagement for dataset onboarding, with
Moshik taking ownership December 1st. The transition addresses
longstanding gaps in use case review coordination and schema definition
processes. Cross-team kickoff meetings have been held, and knowledge
transfer is in progress to ensure the handoff strengthens execution
rather than disrupts momentum. Thank you to Linda for her excellent job
on shepherding this process for PM thus far!

### **Strategic Challenges**

The scope of Engagement data for December 31st required more
back-and-forth with Product and Engineering than initially expected to
define what\'s feasible within the delivery window. While Menna
established an initial set of MVP use cases, several remain excluded
pending technical alignment---including recursive search, target
accounts, and certain aggregation scenarios. Engineering validation is
ongoing, and final commitments depend on outcomes from these
evaluations. The team has a proposed path forward, but feasibility,
level of effort, timeline, and technical implications are still under
review.

Moshik\'s work on Regional HQ exposed a data limitation: the \"domestic
hq\" flag in company data doesn\'t consistently reflect what\'s needed
for a regional main office. The team set that approach aside to reassess
the data, though it may be revisable later if it proves useful for the
proof of concept. The next step is drafting a research plan for data
quality and matching, with engineering work planned to kick off once the
first proof of concept is validated.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team discovered a better data source for Regional HQ matching
through ZI Chat---an exact location ID for domestic parents rather than
relying on binary flags. This finding prompted a strategic pivot away
from the original \"domestic hq\" flag approach, which wasn\'t
consistently reflecting regional main offices. The new data point should
improve matching accuracy, though it requires validation through a
research plan for data quality before engineering picks up the work.

Marc\'s resource realignment surfaces a pattern the team has been
addressing: dataset onboarding benefits from more structured use case
review across Data, Platform, and Apps teams, plus faster schema
definition and stakeholder alignment. Moshik\'s December 1st transition
creates dedicated ownership to drive these improvements systematically
rather than reacting to bottlenecks as they emerge.

### **Cross-Team Dependencies**

Work with the Search team on Engagement data integration for December
31st continues to shape delivery scope. The Search team is actively
engaged on bringing over Engagement data and has a plan for UUID
creation, while also evaluating approaches for deep traversals and
aggregations. Menna is refining MVP scope through engineering validation
and communicating timeline implications to stakeholders as technical
constraints become clearer.

Coordination with Data Producers remains necessary for the Regional HQ
proof of concept. The team needs to validate the newly identified
location ID data point with the research team before engineering work
begins. Moshik is drafting a research plan for data quality and matching
to ensure the first proof of concept is on solid footing.

## **Looking Ahead**

The primary focus next week is finalizing the MVP scope for Engagement
use cases in the December 31st Federated Search milestone. Menna will
complete the second round of engineering validation and lock in what can
realistically be delivered, updating stakeholders on any necessary
trade-offs or scope adjustments.

Moshik will complete the first proof of concept for Regional HQ once the
research team validates the data quality of the newly identified
location ID source. This sets up engineering to pick up the work in
early December. Marc will continue knowledge transfer for dataset
onboarding as Moshik prepares to take ownership December 1st, with focus
shifting to establishing more deliberate use case reviews and
streamlined schema alignment processes.

Linda will continue working with Menna\'s team on Federated Search
integration to the GraphQL API, focusing on prioritized use cases and
required data while supporting the December delivery of Workspaces
engagement data.

*Source: Team 1-2-3 Operating Framework entries from November 17-21,
2025*
