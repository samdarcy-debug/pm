---
id: weekly-integrations-2025-34
title: "Integrations Weekly Report - August 22, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-08-22
updated: 2026-01-06
week_ending: 2025-08-22
reporting_period: "August 18-22, 2025"
tags: ["weekly-report", "Q32025"]
---

Integrations Executive Roundup -
August 18, 2025

  Executive Summary

   Prateek Paikray successfully completed Agentforce V2 requirements, began
   reaching out to onboard enterprise beta customers (ADP, Salesforce), and
   worked with Salesforce to upgrade ZI's SFDC Demo instance to support
   Agentforce demos (in progress). Sanyog Rai led an onsite across all engagement
   engineering stakeholders to finalize architecture decisions, near term priorities,
   and work live on GTM DM blockers which included identifying that Outlook
   meeting cancelation events were being omitted from the Chorus ETL process.
   Erica Fienman continued discovery on GTM Copilot requirements and began
   grooming on Custom Object import from CRM with engineering. Andres Perez
   completed scoping for partner attributes where GTM DM can have a consistent
   schema for certain partner fields pushed to ZI via API.

This Week's Progress

Key Momentum Areas

   Agentforce Customer Pipeline Activated: Prateek Paikray delivered complete V2
   requirements for the Agentforce integration and initiated direct customer outreach to
   enterprise accounts including ADP and Salesforce for early adoption testing. The team is
   also upgrading ZI's SFDC demo instance to support Agentforce demonstrations, positioning
   us for strong customer validation ahead of the October market launch.
   Engagement Architecture Breakthrough: Sanyog Rai led a cross-functional onsite in
   Toronto that delivered critical architectural alignment across all engagement engineering
   stakeholders and resolved longstanding technical blockers. The team identified and
   addressed the root cause of Outlook meeting cancellation data gaps in the Chorus ETL
   process, directly unblocking engagement data scaling efforts.

   Core Product Integration Foundation Advanced: Erica Fienman made significant progress
   on GTM Copilot requirements discovery while simultaneously initiating custom object
   import grooming sessions with engineering teams. This parallel advancement on both core
   product initiatives ensures readiness for the November Copilot V2 launch while addressing
   critical customer requests for custom object support.

Goals & Progress

   Agentforce Integration & Customer Validation:
   Prateek Paikray achieved full completion of V2 requirements definition 100% Complete
   and successfully launched enterprise customer beta outreach. Work with Salesforce on
   demo instance upgrades is progressing, with the package installation complete and
   licensing updates underway to enable seller access for internal demonstrations and
   customer validation.

   Engagement Data Scaling:
   Sanyog Rai made significant progress on tenant enablement 60% Complete through the
   Toronto onsite, which resolved critical architectural questions and identified specific
   technical blockers. Recording data is now live on stage, with email and calendar data flowing
   into GTM data model for existing integration customers, and the Outlook cancellation bug
   resolution clearing the path for full deployment.

   GTM Copilot V2 & Custom Objects:
   Erica Fienman advanced requirements finalization and engineering coordination
     60% Complete despite team capacity constraints from vacations and illness. Custom

   object requirements are complete and grooming sessions with engineering have begun,
   while GTM Copilot requirements discovery continues with stakeholder review sessions
   planned for next week following Sean's latest requirements delivery.

   Partner Data Integration:
   Andres Perez completed partner attributes scoping work 100% Complete and
   successfully defined the technical approach for both standard and custom partner
   schemas. All required work has been ticketed across data platform teams, with clear
   specifications for namespace management and API validation requirements.

Strategic Challenges

   Engineering partnership gaps continue to impact engagement data delivery speed, with
   Sanyog Rai needing clearer engineering DRI support for engagement-specific work. The
   Toronto onsite helped resolve immediate technical blockers, but small issues that require
   deep domain knowledge still create debugging delays that could be accelerated with
   dedicated engineering partnership and clearer TPM support.

   The Agentforce V2 integration capabilities will be limited in the first iteration due to OAuth
   authentication restrictions preventing access to internal APIs. Prateek Paikray identified
   that features like Copilot signals require apps engineering teams to publish APIs to the
   Enterprise API Gateway before they can be accessed, creating dependencies that may
   impact initial customer value demonstrations.

Strategic Insights

Key Learnings & Discoveries
   Cross-Team Onsite Impact: The Toronto engagement with Chorus engineering
   stakeholders proved highly effective for resolving complex technical issues that were
   difficult to debug remotely. The in-person collaboration identified hidden system behaviors
   (like message filtering for meeting cancellations) and established clearer architectural
   alignment that accelerates development velocity going forward.

   Custom Object Integration Complexity: Erica Fienman discovered through engineering
   grooming sessions that custom object ingestion requires careful balance between user
   flexibility and admin control. The team identified multiple ingestion approaches including
   SIP and query-based methods, with decisions needed on how to handle user-specific field
   requests while maintaining platform-wide data governance.

   Customer Permission Requirements: Juniper Networks (260K ACV customer) raised
   critical concerns about Salesforce permission respect within our products, specifically
   wanting to prevent sellers from viewing opportunities owned by others. This highlights a
   broader need for user-level visibility controls in the GTM data model that will become
   increasingly important as we scale enterprise usage.

Cross-Team Dependencies

   Our collaboration with the data platform team on namespace management and partner API
   implementation remains critical for successful partner integration scaling. The team has
   clear specifications and ticketed work, with coordination needed on implementation
   timelines and automation roadmap planning to support strategic partnership expansion.

   The apps engineering teams' timeline for publishing internal APIs to the Enterprise API
   Gateway will directly impact Agentforce V2 capabilities and customer demonstration value.
   Prateek Paikray is coordinating with multiple teams to prioritize Copilot signals and other
   critical features for the October launch window.
Looking Ahead

Next week's focus centers on customer validation, engineering execution, and technical delivery,
building on the architectural breakthroughs and product development momentum established this
week.
Prateek Paikray will advance enterprise customer conversations with Salesforce and ADP while
completing the SFDC demo instance upgrades to support live Agentforce demonstrations.
Sanyog Rai will capitalize on the Toronto onsite outcomes by pushing through the identified
integration bug fixes to complete engagement data scaling, targeting full deployment across all ZI
tenants by week's end. Erica Fienman will conduct stakeholder review sessions for GTM Copilot
requirements while completing custom object grooming with engineering teams, ensuring both
initiatives remain on track for their respective launch timelines. Andres Perez will work with
integrations and data platform teams to get committed dates for Partner Attributes and
determine whether the beta GTM APIs on public docs need to be amended to avoid unintended
access.
The team is well-positioned to deliver customer-facing capabilities and technical infrastructure
improvements, with strong momentum from architectural alignment, customer engagement
initiatives, and product development coordination setting the foundation for successful market
demonstrations and enterprise integrations.

                Source: Team 1-2-3 Operating Framework entries from August 18-22, 2025
