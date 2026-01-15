---
id: weekly-integrations-2025-46
title: "Integrations Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: integrations
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

# ***Integrations Team Executive Roundup***

***Week of November 10, 2025***

![ZoomInfo](media/image1.png){width="0.6944444444444444in"
height="0.6944444444444444in"}

*Executive Summary: **ZoomInfo is positioned to be showcased at Google
Next with Engine as the customer highlighting our Agentforce solution,
validating our strategic direction in the agent ecosystem.** Prateek
Paikray **is leading the Salesforce Agentforce partnership, which has
flagged a** \$500M Q4 pipeline **and wants ZoomInfo integrated into
their sales motions, though they\'re requesting free Copilot seats for
their sellers---Prateek is coordinating with Adam Sayles and
partnerships on commercial terms. The Field Mapping Agent now works
end-to-end in staging and will be demoed at the Agent Think meeting this
week, while backend improvements for import mapping redesign are
enabling Rayee to start frontend work next week.***

## ***This Week\'s Progress***

### ***Key Momentum Areas***

*Prateek Paikray **secured Engine as a showcase customer for Google
Next, where they\'ll present the ZoomInfo Agentforce solution at a
marketing event hosted by Google. This nomination validates that the
team\'s work is creating measurable market impact and provides concrete
proof points for the go-to-market strategy. The customer selection
demonstrates strong partnership execution and positions ZoomInfo
prominently in the agent ecosystem conversation.***

***The Field Mapping Agent achieved a significant technical milestone
this week, with** Andres Perez **successfully updating the system to
pull admin connectors from FMS and work end-to-end in staging. The agent
now automatically uses the admin\'s CRM access token to check fields,
eliminating a key integration hurdle. This advancement will be
demonstrated at the weekly Agent Think demo meeting, showcasing tangible
progress on the agentic platform.***

*Lareina **delivered simplified import mapping designs with backend work
completed for phase one, allowing** Rayee **to begin frontend
development next week. The redesign introduces more restrictions and
fewer mappable fields initially, streamlining what had become an overly
complex user experience. The approach prioritizes delivering a working
solution quickly while setting up phases two and three for live updates
and additional capabilities.***

### ***Goals & Progress***

*GTM AI Context Service & Vertical Datasets: Prateek Paikray **delivered
UI enhancements for platform readiness on Vertical Datasets and
completed alignment with engineering on multi-instance CRM support
requirements. The engineering team is now preparing the high-level
design before implementation begins. Mock-ups for integrating Vertical
Datasets with workbook data for enrichment are in progress, with designs
focused on job posting and other commonly requested customer use cases
being developed with Peter\'s input.***

*GTM Studio & Copilot V2: Andres Perez **completed new spec docs for
Product and Opportunity Line Item work and reviewed them with MJ and
David Wheeler. However, this initiative will be deprioritized since no
consumers can access this data until GraphQL is live---audiences can\'t
read it, GTM config hasn\'t figured out the web research path, and
Copilot chat would reference offerings anyway. The team is instead
prioritizing Fivetran work requiring one to two sprints from Teams 11
and 6 to unblock ServiceNow and other vendors while delivering custom
objects in parallel.***

*Salesforce Agentforce & MCP Integration: **The team held productive
discussions with Salesforce on their upcoming MCP (Model Context
Protocol) integration, currently in beta.** Prateek Paikray **has been
nominated along with Kuranthi and Adam to attend a partnership session
on November 20, where Salesforce will enable only three participants per
partner. The team learned that accessing MCP tools for external partners
will require new scopes when creating apps via the Developer Portal, and
that MCP tool responses may return text rather than JSON, requiring
investigation into Lightning Web Component presentation strategies.***

### ***Strategic Challenges***

***The SalesOS customer interface gap continues creating friction,
evidenced by escalations from Zoom Video and BBSI this week. Both
customers discovered ZoomInfo had opportunity data when they saw the ROI
dashboard, but since they\'re only on SalesOS, they questioned why
ZoomInfo possesses this data without giving them adequate access. While
engineering delivered a backend feature to block import of certain
objects, the real solution requires giving these customers better
interfaces to access GTM Data Model data---potentially through Audiences
or Workspace without AI credit features. This blocks the Q3 goal of
deprecating SalesOS and needs support from Victor, Philip, and Dominik
to define a path forward that improves experience while paywalling
expensive AI features.***

***Cloud Data Share regression testing uncovered a blocking issue where
audience exports fail entirely if a ZoomInfo ID is missing.** Prateek
Paikray **reached out to the workflows team to understand why this
strict requirement exists, as it prevents customers from exporting valid
audience data to Snowflake and Databricks when records lack ZoomInfo
IDs. The bug needs resolution before implementation guides can be
finalized, and the team is working to complete regression testing and
prepare documentation once the issue is addressed.***

***Marketplace documentation has fallen significantly behind with the
addition of new Data Connectors and OAuth partners. The public
marketplace needs updating to reflect current capabilities, and this
represents a long-overdue housekeeping item. Assuming no higher-priority
work emerges,** Andres Perez **will dedicate time next week to
overhauling the advertising of integrations both internally and
externally, ensuring customers and internal teams have accurate
information about available connectors and partners.***

## ***Strategic Insights***

### ***Key Learnings & Discoveries***

***Salesforce\'s Agentforce push is creating unexpected partnership
opportunities but also commercial complexities.** Prateek Paikray **is
leading this partnership, where Salesforce is driving a** \$500M Q4
pipeline **and wants to position ZoomInfo\'s Agent for Sales use cases
in their sales motions, but they\'re requesting free Copilot seats for
their sellers to demo the solution. Prateek has been coordinating
internally with Adam Sayles and the partnership team on next steps. Adam
has connections with Salesforce\'s CS services arm who may be interested
in purchasing seats, which represents a more sustainable model. The
discussion surfaced a key strategic question: should ZoomInfo provide
discounted seats to enable Salesforce\'s sales organization, or should
the focus be on paid implementations with their services arm and actual
customers?***

***The MCP integration architecture learned this week could
fundamentally change how ZoomInfo delivers Copilot features in the
future. After leading discussions with the Salesforce team,** Prateek
Paikray **discovered that MCP tools consume bulk credits for data API
access but restrict account intelligence features to upgraded tiers.
This creates a natural monetization path where non-Copilot customers
could access data APIs through MCP if they pay for bulk credits, but
account intelligence capabilities remain paywalled behind Copilot,
Workspace, or Studio. The team is exploring whether to swap existing
capabilities for MCP-based tools once the integration is validated.***

***A significant opportunity emerged with FedEx, valued at** \$1.3M**,
far exceeding the initial \$300-400K estimate.** Ravi**, the strategy
director, reached out after receiving positive feedback on his pitch for
the Agent for Sales solution. This opportunity prompted strategic
thinking about product prerequisites: should customers be required to
have Copilot to access Agentforce integrations, or could Studio serve as
the platform fee? Studio makes more sense because it doesn\'t require
paying elevated per-seat costs for thousands of users, includes one
admin seat, and enables data management app and consumption
capabilities. This could become the standard model for platform access
without forcing expensive Copilot seat requirements.***

***The GTM Data Model record volume dashboard work revealed an
opportunity to build the capability once rather than repeatedly for each
vendor.** Andres Perez **created a bare-bones prototype covering the
data model with Karina and team, showing that the same query filtered by
vendor would work universally. Building it right once prevents technical
debt from accumulating as more vendors get added, and ensures consistent
reporting across all data connectors.***

### ***Cross-Team Dependencies***

***Our work with the User Management team remains essential for
delivering multi-instance CRM support with role-based export controls.
The team needs an API to fetch role information to demonstrate the
proof-of-concept for egress using the existing platform feature.**
Prateek Paikray **coordinated with engineering to leverage this existing
capability rather than building net-new functionality, but
implementation depends on User Management delivering the required API
endpoint. A grooming session is scheduled for next week to finalize
requirements once the API availability is confirmed.***

***The Fivetran work prioritization requires coordination with Teams 6
and 11 for one to two sprints to unblock ServiceNow and other vendor
integrations. This work takes priority over Product and Opportunity Line
Item work since those features have no consumers until GraphQL becomes
available. The sequencing decision ensures engineering resources focus
on removing vendor blockers while maintaining parallel progress on
custom object delivery, but requires buy-in from both teams on the
sprint commitments.***

## ***Looking Ahead***

***Next week centers on three strategic priorities that position the
team for accelerated delivery in subsequent weeks: Salesforce MCP
enablement, Vertical Dataset design completion, and marketplace
documentation overhaul.***

*Prateek Paikray **will attend the November 20 Salesforce MCP partner
session and work to enable the MCP add-on in the ZoomInfo Salesforce
org, allowing hands-on exploration of how Agentforce integrates with MCP
tools. Success means validating whether existing capabilities should be
swapped for MCP-based tools and understanding the technical requirements
for consuming account research and scoring tools that internal teams are
registering. Simultaneously, he\'ll continue driving Vertical Dataset
design work with audiences, coordinating with Peter and the team to mock
up use cases beyond job postings that customers frequently request.
He\'ll also follow up with engineering and QA teams to complete Cloud
Data Share regression testing for Snowflake and Databricks, preparing
implementation guides once the ZoomInfo ID requirement issue is
resolved.***

*Andres Perez **will focus on marketplace documentation, adding Data
Connectors and new OAuth partners to the public marketplace to ensure
customers and internal teams have accurate integration information.
He\'ll also coordinate the Fivetran work prioritization with Teams 6 and
11, ensuring ServiceNow and other vendors get unblocked efficiently. The
Field Mapping Agent demo at Agent Think will showcase the end-to-end
staging environment to stakeholders, demonstrating tangible agentic
platform progress.***

***The team enters next week with strong partnership momentum from
Engine and Salesforce, clear technical achievements in the Field Mapping
Agent, and strategic clarity on product positioning questions around
Copilot versus Studio as platform access points. With the import mapping
redesign enabling Rayee to start frontend work and MCP integration
learnings being applied hands-on next week, the team is positioned to
deliver meaningful customer value while navigating complex partnership
commercial discussions.***

***Source: Integrations Team Operating Framework entries from November
10-14, 2025***
