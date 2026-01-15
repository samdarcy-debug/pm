---
id: weekly-integrations-2025-28
title: "Integrations Weekly Report - July 11, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-07-11
updated: 2026-01-06
week_ending: 2025-07-11
reporting_period: "July 7-11, 2025"
tags: ["weekly-report", "Q32025"]
---

# ***Integrations Executive Roundup - Week of July 7, 2025***

## ***Executive Summary***

*The Integrations team delivered critical progress on three strategic
fronts this week, with Prateek Paikray achieving 100% completion on
Salesforce Agent Force requirements and Erica Fienman advancing dynamic
mapping designs to 90% completion with engineering review. Engineering
teams are aligned with the Upsert API requirements, but need to confirm
what additional product deliverables are required before committing the
work to specific sprints. The team maintains strong momentum across H2
deliverables including the August 1st engagement data availability
commitment.*

## ***This Week\'s Progress***

### ***Key Momentum Areas***

*Prateek Paikray completed all functional requirements and lucid chart
documentation for the Salesforce Agent Force integration, successfully
navigating authentication challenges and establishing bi-weekly
collaboration calls with Salesforce\'s principal architect team. This
positions us well for the critical July 31st package submission deadline
required for Dreamforce availability.*

*Erica Fienman achieved a significant breakthrough on dynamic mapping
with 90% completion of requirements and preliminary designs reviewed
with engineering, covering three key use cases: creating records from
custom fields, appending custom objects to existing GTM records, and
full custom-to-GTM object mapping. The designs provide sufficient
context for engineering sizing conversations scheduled for next week.*

*Sanyog Rai reached 90% completion on both engagement data upsert API
requirements and schema finalization for content interactions table,
with all main requirements completed and reviewed with engineering
teams. The remaining 10% focuses on securing final engineering sign-offs
and timeline commitments.*

### ***Goals & Progress***

***Salesforce Integration Initiatives**: Andres Perez made substantial
progress on the prototype for direct Salesforce API access through agent
layer, successfully identifying all team dependencies and creating
[[JIRA tickets for four separate
teams]{.underline}](https://discoverorg.atlassian.net/jira/polaris/projects/ZIDEAS/ideas/view/7432510?selectedIssue=ZIDEAS-1613&issueViewLayout=sidebar&issueViewSection=overview&atlOrigin=eyJpIjoiMmI3NTBmZjIwOTQxNGZjNWFjY2FmMDM1MDA1MTk2MGMiLCJwIjoiaiJ9).
The technical approach is validated and the team is working to secure
engineering commitment from the right stakeholders across prompt
service, agent service, and MCP server teams.*

***Upsert API Development**: Both CRM accounts endpoint (Erica) and
content interactions endpoint (Sanyog) reached 90% completion with
requirements finalized and engineering reviews completed. Engineering
teams are aligned on the requirements and working to confirm what
additional product deliverables are needed before sprint commitment,
with a dedicated alignment meeting scheduled for Wednesday.*

***GTM Data Model Enhancement**: Prateek achieved 100% completion on
UUID field implementation with workflow complete and ZDP team deployment
scheduled for Tuesday. Schema updates for engagement tables are 90%
complete pending final engineering counterpart sign-offs from David and
Jerome on field definitions and table creation timelines.*

### ***Strategic Challenges***

*Cross-timezone coordination continues impacting velocity, particularly
between Israel-based and West Coast engineering teams. Sanyog noted this
disconnect is creating communication gaps in the upsert API project
despite clear requirements, suggesting need for more structured
engineering-to-engineering communication protocols rather than
product-to-product handoffs.*

*Resource allocation pressure is emerging with Prateek being pulled into
the new Salesforce Agent Force package development while maintaining
existing marketplace and integration responsibilities. This creates
potential focus dilution across critical Q3 deliverables, though the
Agent Force work aligns with broader integration strategy.*

*Platform development timing continues to challenge downstream
application teams who are building on capabilities that aren\'t fully
mature yet. The team identified this pattern in recent sprint
retrospectives, where the natural tension between platform stability and
feature velocity requires careful coordination to avoid rework.*

## ***Strategic Insights***

### ***Key Learnings & Discoveries***

*Engineering-to-engineering communication proves more effective than
product-to-product handoffs for complex technical requirements.
Sanyog\'s observation about workbooks team requesting date fields versus
datetime fields revealed that product teams are making technical
decisions without engineering validation, creating downstream
implementation issues that could be avoided with direct technical
consultation.*

*The Salesforce prospecting center integration revealed market reality
with fewer than 20 Salesforce customers actually using the feature,
despite significant development investment. This learning reinforces the
importance of market validation before major integration investments and
supports our pivot toward Agent Force as the primary Salesforce
strategy.*

*Ferrell and Nanxi Onboarding analysis revealed that the biggest driver
for CRM and Core Engagement adoption revolves more around the SKU than
high-touch/low-touch onboarding. Copilot Enterprise and Chorus the only
plan with a compelling use case for Email, Calendar, and Meeting
Recording Integration, however Copilot Enterprise is only 1400 Mid
Market+ customers compared to 15,000 Mid Market+ customers [[per this
dashboard]{.underline}](https://10ay.online.tableau.com/#/site/discoverorgllc/views/ActiveIntegrations/PackageandAccountListDownload?:iid=1).*

### ***Cross-Team Dependencies***

*Our work with engineering teams on upsert API delivery is progressing
well with requirements alignment complete. Erica is leading a Wednesday
alignment meeting with Rayee's team to clarify remaining product
deliverables needed for sprint commitment. The August 1st engagement
data availability promise remains on track with this coordination.*

*Collaboration with the search team on UUID field requirements needs
direct engineering coordination. Prateek identified that the enterprise
search team\'s specific format requirements for GTM object querying
haven\'t been fully validated against our current engagement ID
implementation, requiring immediate technical alignment to avoid
rework.*

## ***Looking Ahead***

*Next week focuses on finalizing engineering commitments across all
major initiatives through direct stakeholder coordination. Our primary
objective is securing sprint commitments for Salesforce connector
actions, upsert API endpoints, and schema updates to maintain Q3
delivery momentum.*

*Andres will coordinate with engineering stakeholders for the Salesforce
Agent Force prototype, working across prompt service, agent service, and
MCP server teams to validate the agent-based integration approach.
Success here enables the workbooks beta customer use cases and
establishes our technical foundation for broader agent integrations.
Simultaneously, Erica and Sanyog will leverage their Wednesday
engineering meeting to clarify remaining product requirements for upsert
API sprint commitment, directly supporting the August 1st engagement
data timeline.*

*The team maintains strong momentum with multiple initiatives at 90%+
completion, positioning us well for Q3 delivery as engineering
coordination resolves remaining commitment questions. Our focus on
stakeholder alignment over requirements refinement reflects lessons
learned about converting technical feasibility into delivery certainty.*

*Source: Team 1-2-3 Operating Framework entries from July 7, 2025 and
team meeting transcripts*
