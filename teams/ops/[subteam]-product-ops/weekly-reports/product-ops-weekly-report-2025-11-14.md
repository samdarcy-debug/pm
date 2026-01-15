---
id: weekly-product-ops-2025-46
title: "Product Ops Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: product-ops
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Product Ops Executive Roundup - November 10, 2025**

## **Executive Summary**

The team achieved a major breakthrough in automated release processes
this week, successfully creating the first version of automated product
information extraction from code that will fundamentally change how
product releases work. Daniel Kong and Kristin Gandini proved out the
automated changelog system can work in production, processing
engineering\'s AI release tech output into deployment summaries that
generated release notes with PM demo videos for the November 18 release.
Ken Elwell successfully built the Voice of Customer pitch analysis
system in GTM Studio, demonstrating a compelling use case that connects
customer call analysis at scale with Workspace execution capabilities.
The week\'s ELT session on Workspace and GTM Studio pitches revealed
that while the semantic pipeline has the right components, filtering
data to solve specific GTM Studio use cases remains challenging and
requires focused attention.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Automated Release System Breakthrough**: Daniel Kong and Kristin
Gandini successfully created the first automated product information
output from code, proving the system can streamline the product release
process. The team processed engineering\'s AI release tech from Dan
DeSwaan and Shirhen\'s team, converting raw code changes into deployment
summaries that fed into release notes generation with PM demo videos for
the November 18 release. This POC demonstrates the feasibility of
cutting PM time significantly and enabling weekly or bi-weekly releases
that bring downstream teams along with product velocity.

**Voice of Customer Analysis at Scale**: Ken Elwell completed the Voice
of Customer pitch analysis system in GTM Studio, establishing the
process and tools for analyzing customer calls at scale. The system
creates a compelling use case that connects to Workspace for execution,
delivering capabilities no other company currently offers. This work
positions the team to provide actionable insights from customer
conversations with minimal manual effort.

**Workspace and Studio Learning Session**: Brett Jacobs led an ELT
session reviewing the first few weeks of Workspace and Studio pitches,
surfacing valuable learnings about the semantic pipeline\'s capabilities
and limitations. The session confirmed that while the semantic pipeline
contains the right components, the challenge lies in filtering data down
to answer specific GTM Studio use cases---a finding that Ken and Sam\'s
VOC work validated and that now requires focused problem-solving.

### **Goals & Progress**

**Automated Release Pilot Expansion**: Kristin Gandini will circulate a
proposal to expand the automated MCR process pilot for Workspace and
Studio through end of year. The proposal requires buy-in from TPM and PM
leads to make this the standard motion, with plans to scale to other
products in Q1. The pivot from VOC agents to MCR automation addressed an
immediate gap created by Workspace not using the standard release
tracking process, demonstrating the team\'s ability to adapt to business
needs while advancing automation capabilities.

**Planning Workshop Redesign**: Caleb Munson is building out a
fundamentally different planning approach based on Dominik\'s feedback,
shifting from traditional capacity planning to play-based planning. The
new model will have teams build out plays over one to two days,
estimating both build costs and AI consumption value, with expanded
participation to team leads and managers. Caleb is working through the
mechanics of play definition and estimation approaches, with stakeholder
communication and deliverable finalization planned for next week.

**MCP Platform Technical Resolution**: Sam Darcy encountered friction
with the agentic MCP team, who flagged that MCP\'s external-facing
platform isn\'t ideal for internal tools. After discussion with Carter
Van Huss, Sam and the MCP team agreed that whitelisting the agentic
platform within ZI Chat would provide the cleanest solution. Sam reached
out to William and Jack to restart that approval process, with plans to
remove the MCP component entirely once whitelisting is secured.

### **Strategic Challenges**

**Voice of Customer Data Filtering**: Brett Jacobs identified a
significant challenge in filtering the semantic pipeline data to
identify which calls actually had pitches completed. The issue is
substantial enough that Dominik raised it to Rowan and the GTM Studio
team. While Ken and Brett achieved good results in their analysis, the
underlying difficulty of getting the right data set filtered properly
represents a blocker that needs resolution to make VOC analysis
consistently reliable and scalable.

**Release Tech Data Completeness**: Daniel Kong is waiting on the most
recent dataset from Dan DeSwaan\'s team to ensure the automated release
system is capturing all relevant code changes. Some product updates may
have been missed based on date and keyword capture logic, requiring
closer collaboration with engineering productivity to validate
comprehensive coverage before scaling the automation approach beyond
Workspace and Studio.

**Planning Model Knowledge Gaps**: Caleb Munson faces uncertainty about
the relationship between AI credits, Plays, and Play
Components---knowledge needed to design effective estimation models.
He\'s meeting with Derek Osgood next week to discuss AI consumption
calculations and is working to find the middle ground between estimation
that\'s useful and estimation that creates excessive administrative
burden. The expanded scope to team leads and managers adds complexity to
workshop design and facilitation.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Automated Release Tech Is Comprehensive**: Kristin Gandini\'s work
with Dan DeSwaan and Shirhen\'s team revealed that the AI release tech
from engineering productivity is more comprehensive than initially
understood. The team is making some assumptions about what was missed
based on date and keyword capture, but the foundational data quality
suggests strong potential for expanding to more products if the capture
methodology can be refined and validated.

**GTM Studio\'s Unique Competitive Position**: Ken Elwell\'s discovery
that analyzing customer call data at scale in GTM Studio, combined with
Workspace for execution, represents something no other company currently
offers. This insight positions the team to develop a differentiated
capability that connects customer intelligence gathering directly to
action, though realizing this potential depends on solving the data
filtering challenges identified this week.

**External vs Internal Tool Architecture**: Sam Darcy learned that the
agentic MCP server is designed for external users, not a sustainable
solution for internal tools. This architectural mismatch surfaced
through the PR review process and led to identifying a better approach
through ZI Chat whitelisting. The learning highlights the importance of
understanding platform design intent when selecting technical
infrastructure for team tools.

### **Cross-Team Dependencies**

The collaboration with Dan DeSwaan and Shirhen\'s engineering
productivity team is advancing well, with clear mutual interest in
making the automated release tech work. Daniel Kong needs closer
coordination to ensure comprehensive data capture and validate nothing
significant is being missed in the current extraction logic.

The GTM Studio team\'s involvement in resolving Voice of Customer data
filtering issues is now escalated through Dominik to Rowan, indicating
executive awareness of the challenge. Sam Darcy\'s path forward depends
on Jack and William\'s approval for whitelisting the agentic platform in
ZI Chat, removing the MCP dependency that\'s creating friction with
Carter Van Huss\'s team.

## **Looking Ahead**

Next week centers on scaling proven systems while resolving data
infrastructure challenges that enable broader deployment.

**Voice of Customer Data Resolution**: Brett Jacobs and Ken Elwell need
to nail the VOC dataset filtering issue to make customer call analysis
reliable and repeatable. This work connects directly to demonstrating
GTM Studio\'s unique competitive advantage and requires resolution of
the technical challenges in identifying relevant calls from the semantic
pipeline.

**Automated Release Motion Standup**: Daniel Kong and Kristin Gandini
will pilot the first automated release summary for Workspace, proving
out the end-to-end workflow before proposing expansion. Kristin will
circulate the proposal to extend MCR automation through end of year,
requiring TPM and PM lead buy-in to make this the standard approach.
Success here depends on validating data completeness with Dan DeSwaan\'s
team and confirming the system captures all relevant product changes.

**Planning Workshop Launch Preparation**: Caleb Munson will finalize
workshop deliverables and templates, draft the AI consumption model
after meeting with Derek Osgood, and begin stakeholder communication
about the new play-based planning approach. He\'ll also work on defining
support for non-play work curation and drafting an engineering
estimation model that balances utility with administrative efficiency.
The expanded scope to team leads requires careful design to ensure the
workshop delivers value at scale.

The team demonstrated strong execution this week with breakthrough
achievements in automated releases and Voice of Customer analysis, while
surfacing technical challenges that now have clear paths to resolution
through cross-team coordination and executive awareness.

*Source: Team 1-2-3 Operating Framework entries from November 10, 2025*
