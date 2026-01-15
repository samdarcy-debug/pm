---
id: weekly-integrations-2025-37
title: "Integrations Weekly Report - September 12, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-09-12
updated: 2026-01-06
week_ending: 2025-09-12
reporting_period: "September 8-12, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Integrations Team Executive Roundup - Week of September 8, 2025**

## **Executive Summary**

Sanyog successfully completed email ingestion into GTM DM for all
tenants (Gmail+Outlook) and calendar data now on GTM DM for 1000 tenants
(Google only, Outlook incoming). Prateek advanced multiple strategic AI
initiatives, completing Agentforce enablement documentation and
progressing vertical datasets marketplace development while coordinating
cross-functional solutions for multi-currency support and partner app
publishing workflows.

## **This Week\'s Progress**

### **Key Momentum Areas**

The team made important discoveries about email data processing that
will improve customer value delivery. Sanyog identified that
engagement-generated GTM contacts and accounts will help capture
significantly more email volume for tenants without CRM connections,
addressing a data gap that has been causing customer confusion about low
email counts (Chorus only ever persisted emails when a CRM was
connected, unless the email was sent from ZI Copilot or Engage).

Sanyog delivered the long-awaited email and calendar data processing
rollout, successfully onboarding all Google/Outlook tenants to receive
email engagement data in GTM Data Model. This infrastructure achievement
enables downstream teams to leverage email and calendar engagement data
for customer workflows via the new GraphQL endpoint, representing a
foundational capability that multiple product teams have been waiting
for.

Prateek completed the Agentforce integration enablement document and
coordinated with creative marketing for demo video production at the
Waltham office. His systematic approach to cross-functional
collaboration advanced multiple H2 priorities simultaneously, from AI
context layer marketing to vertical datasets API requirements gathering
with the ZDP engineering team.

### **Goals & Progress**

**Data Processing Infrastructure**: Sanyog successfully enabled email
and calendar data processing for all Google tenants and email for 1000
Outlook tenants, with only Outlook calendar integration pending final
edge case testing. The rollout proceeded gradually with 500 tenants at a
time to monitor for scaling issues, demonstrating careful operational
management. This foundational work allows downstream application teams
to access engagement data in GTM Data Model.

**AI Integration & Marketplace**: Prateek completed the Agentforce
enablement documentation and submitted the app listing for Salesforce
review. The team coordinated with Ben Davis from partner marketing and
Ryan O\'Connor for demo video creation, positioning the integration for
broader market announcement. Work on vertical datasets progressed
through requirements refinement with Workbook and GTM Store teams for
metadata API development.

**Strategic Platform Development**: Prateek partnered with the CFA team
to identify multi-currency support solutions and discussed roadmap
integration for Agentforce with ROI data capabilities. His collaboration
with the Dev Portal team advanced the end-to-end experience for
partner-registered apps publishing to both internal and external
marketplaces, supporting the broader partner ecosystem strategy.

### **Strategic Challenges**

API development timelines for vertical datasets face potential delays
due to Israeli holidays in late September and early October, which may
impact the October 15 delivery target. The ZDP engineering team\'s
confidence in delivering interface APIs provides some mitigation, but
the compressed timeline requires careful monitoring and potentially
adjusted expectations.

Multi-currency support requirements emerged through customer feedback,
necessitating short-term solutions while longer-term platform service
integration is planned. This pattern of customer requirements outpacing
platform capabilities highlights the need for more proactive
requirements gathering in the sales and onboarding process.

The team discovered complexity in building unified MCP (Model Control
Protocol) solutions that balance vendor-specific limitations with
seamless user experience. While the 2026 roadmap includes comprehensive
solutions, near-term workarounds require careful architecture decisions
to avoid technical debt.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Sanyog uncovered an undocumented rule in email processing where only
emails linked to CRM entities are persisted, explaining why some tenants
show surprisingly low email volumes. This restriction originated from
Chorus app's legacy requirements but now creates customer confusion. The
solution involves automatic GTM account and contact generation to create
virtual CRM connections for better data capture.

The team identified that only Copilot customers currently have access to
email and calendar integrations, even though the infrastructure could
support broader customer segments. This represents a potential revenue
opportunity and customer satisfaction improvement that may warrant
product strategy discussion.

Prateek\'s collaboration across multiple teams revealed the importance
of early API design alignment and systematic requirements documentation.
His approach of providing comprehensive vendor mapping documentation and
transformation specifications is proving essential for avoiding
integration backtracking and ensuring successful cross-team
coordination.

### **Cross-Team Dependencies**

Collaboration with the ZDP engineering team on vertical datasets APIs
remains essential for marketplace launch timing. The team worked through
metadata API and query layer requirements, but Israeli holidays may
compress development timelines. Backup planning and clear milestone
checkpoints will be important for managing delivery expectations.

Partnership with CFA on multi-currency support produced workable
short-term solutions while platform service integration is planned for
longer-term scalability. This relationship demonstrates the value of
proactive cross-functional engagement on emerging customer requirements
before they become blockers.

## **Looking Ahead**

Next week focuses on completing Outlook calendar integration testing to
achieve full email and calendar coverage across all tenants, building on
the successful Google rollout foundation.

Prateek will conduct final testing and optimization of the Agentforce
integration beta version before AppExchange publication, while
continuing vertical datasets marketplace UI development. The team will
also advance the unified MCP proof of concept discussions with Uni
Services to enable seamless vendor integrations through a single service
layer.

The team is positioned to deliver on multiple H2 strategic initiatives
while maintaining operational excellence. Key priorities include
finalizing the Agentforce go-to-market assets, completing email and
calendar infrastructure rollout, and establishing scalable processes for
partner app marketplace integration that support the broader platform
ecosystem vision.

*Source: Team 1-2-3 Operating Framework entries from September 8-12,
2025*
