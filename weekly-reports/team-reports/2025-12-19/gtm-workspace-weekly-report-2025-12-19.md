---
id: weekly-copilot-2025-51
title: "GTM Workspace (Copilot) Weekly Report - December 19, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-12-19
updated: 2026-01-06
week_ending: 2025-12-19
reporting_period: "December 15-19, 2025"
tags: ["weekly-report", "Q42025"]
---

# **GTM Workspace Executive Roundup - \[Dec. 15, 2025 - Dec. 19, 2025\]**

## **Executive Summary**

GTM Workspace meetings functionality is on track for its February 9th
release after the team completed a critical resourcing realignment this
week. Gabe led engineering discussions that resulted in redirecting
resources from desktop app development to focus entirely on core
meetings capabilities, positioning the team to deliver the
multi-featured experience customers need. The main technical challenge
centers on migrating to the GTM data model, which will enable team-level
features like consolidated meeting recaps but requires coordination
across multiple systems. Meanwhile, Ant\'s pulses infrastructure reached
a major milestone with the complete system nearing staging deployment,
and Dylan advanced artifact templates that will fundamentally change how
users interact with workspace intelligence.

## **This Week\'s Progress**

### **Key Momentum Areas**

Gabe secured the engineering capacity needed for the February 9th
meetings release by making a strategic trade-off decision. The team
moved developers away from desktop app and granola-style recorder work
to concentrate resources entirely on meetings and workspace
functionality. This swarming approach gives the team the focused
firepower to deliver on the inventory of planned features plus
additional capabilities surfaced through user feedback. The decision
reflects confidence in the core meetings value proposition and
willingness to defer adjacent experiments in favor of executing the
primary use case well.

Dylan pushed artifact capabilities forward on multiple fronts, with the
most significant being the slides artifact prototype that Gabe\'s
engineering team built. Users can now upload their corporate deck, and
the system understands the content and creates reusable templates from
each slide, which then become the default for future slide generation in
workspace. This feature is technically ready for a February deployment,
but requires product decisions about whether to launch as a user-level
capability or wait for tenant-level configuration support. The company
research agent and deal status artifacts also progressed, expanding the
repertoire of intelligence tools available to users.

Ant\'s pulses infrastructure, dubbed PulseForge, achieved near-complete
deployment to staging this week. The system can now ingest pulses from
any source, store them with a strict schema, and apply high-level
filtering. The Insights MCP integration allows the agent to call S2A
insights endpoints to generate pulses, and the team built an impressive
JSON rendering system using Prozmere that displays pulses cleanly in the
workspace feed. This foundational work validates the technical
feasibility of the entire pulse architecture and sets up the feed to
become a central intelligence distribution mechanism across workspace.

### **Goals & Progress**

**GTM Workspace**: The February 9th meetings release moved from planning
into execution mode as Gabe finalized the feature inventory and locked
in engineering resources. The team is tackling the GTM data model
migration as the primary technical challenge, which will unlock
team-level capabilities like creating consolidated recaps of a team\'s
meetings from the previous week. Gabe also continued refining the
semantic trends prototype for conversation intelligence and will present
the latest iteration to Dominic, Victor, and Sean this week to establish
January planning alignment. The emailer experience received attention as
well, with the team investigating how to eliminate the frustrating
10-second delay that occurs when inference runs before the email
interface appears.

**ZoomInfo Intent**: David made progress on the territory MCP by meeting
with Lars to map out integration steps for the GenTech platform. The
team is extending territory functionality beyond user-defined settings
to automatically include admin-defined territories, which will enable
users to open searches and create views through chat interactions. David
also met with Ryan to demo the user settings prototype, establishing
willingness on both sides to coordinate once Ryan returns from PTO. The
territory work is progressing toward a public API, though this requires
another round of discussions with the workflows team to align on what
gets included in that interface.

**Admin Zero Experience**: David continued wrestling with the priority
accounts implementation, specifically how to surface account team member
data from the GTM data model. After three different iteration
suggestions without clear resolution, and with the work not appearing as
a top priority for the search team, David is preparing a slide deck to
force alignment on approach and timeline. This represents a dependency
bottleneck that needs executive attention to unblock, as customer
commitments are waiting on this functionality.

**Additional Initiatives**: Sean returned from paternity leave and
immediately focused on establishing governance structures for the GTM
data store rollout across workspace and workflows. He met with Andres
and Mark Frail to align on the 90-day roadmap and plans to build a
centralized tracking structure using the ServiceNow program model to
monitor all integration points. Dylan advanced the artifact gallery
concept from the hackathon, working with the studio team on dependencies
for the how-to guide flow that SDR leadership has already started using
organically. Ant brought mobile workspace to near-MVP completion with
chat, artifacts, notes, and speech-to-text functionality working, with
conversation mode as a stretch goal for the Christmas timeline.

### **Strategic Challenges**

The GTM data model migration represents the critical path item for
delivering the full meetings experience in February. Gabe identified
specific risk around whether all necessary components will be ready and
functional to support the shift. Without the migration, any team-level
features become problematic because the team doesn\'t want to build on
top of the legacy team structure that exists in the current system. This
creates a binary outcome scenario where either the migration succeeds
and unlocks powerful team-centric capabilities, or it encounters delays
that force scope cuts to the February release. The good news is that a
clear path forward exists, but the timeline dependency makes this a
high-attention item.

Sean surfaced an operational challenge around demo environments that\'s
creating friction for go-to-market teams. Users trying to demonstrate
workspace capabilities are getting confused switching between the demo
environment, Copilot V1, and Workspace in production, leading to
suboptimal demo experiences. This wasn\'t unexpected going into the
transition period, but the volume of complaints suggests it\'s impacting
sales effectiveness more than anticipated. Sean plans to work with
engineering and Brandon to explore mitigation options, since the problem
will likely intensify as workspace adoption grows in the new year.

David\'s priority accounts work hit a dependency stalemate with the
search team around account team member data from the GTM data model.
Despite three proposed approaches and customer commitments waiting on
this functionality, there\'s no clear timeline or agreed-upon
implementation path. The challenge stems from this work not ranking as a
top priority for the search team, creating a classic cross-team
coordination problem where one team\'s critical dependency is another
team\'s backlog item. David is escalating through a formal alignment
deck to force resolution, but this highlights a broader need for tighter
coordination on GTM data model dependencies across teams.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The emailer user experience revealed an important principle about
agent-based tools: users will tolerate inference delays during content
generation but have extremely low patience for delays before the
interface even appears. Gabe observed that clicking a button to send an
email currently opens chat first, and if the system is slow, users sit
watching a blank screen for up to 10 seconds before the emailer loads.
Even though the actual email generation might take longer, that initial
wait destroys the experience because users don\'t see progress or have
any indication that something is happening. This insight is driving the
team toward architectural changes where interfaces load immediately and
inference happens visibly in the background.

Dylan\'s discovery that SDR leadership already created their own how-to
guides using workspace chat and shared them in Slack channels validates
a major use case assumption. When the team deployed audiences to SDRs,
the leadership independently used workspace to generate instructional
artifacts and distributed them through existing communication channels.
This organic adoption pattern suggests that the formal how-to guide flow
the team is building addresses a real workflow need that users are
already improvising solutions for. It also demonstrates that
workspace\'s value extends beyond individual contributor use into team
enablement and knowledge distribution.

The pulses infrastructure work demonstrated that rendering complex
structured data as readable, actionable feed items is technically
feasible using modern web components. Ant\'s team built a system using
Prozmere that converts JSON pulse data into clean, visually distinct
feed entries without requiring custom UI code for each pulse type. This
architectural pattern has implications beyond just pulses, as it
establishes a reusable approach for displaying any kind of structured
intelligence in workspace. The validation that this works well gives
confidence to expand the types of insights and notifications that can
flow through the workspace feed without creating maintenance burden.

### **Cross-Team Dependencies**

Our work with the search team on priority accounts functionality
continues to need attention for delivery timeline clarity. David\'s
progress on account team member data from the GTM data model depends on
search team capacity and prioritization, and despite multiple proposed
approaches, there\'s no committed path forward. This creates risk for
customer commitments that are waiting on this capability. The team is
preparing formal alignment materials to establish shared understanding
of the business impact and secure concrete delivery commitments.

The GTM data model migration work spans multiple teams and represents
the foundation for several February capabilities. Gabe\'s meetings
functionality, Sean\'s broader workspace integration work, and David\'s
territory and priority accounts features all have dependencies on
various aspects of the data model being ready and stable. Sean is
establishing centralized tracking using the ServiceNow program structure
to maintain visibility across all integration points, which should help
the team identify conflicts and bottlenecks before they impact
deliveries.

## **Looking Ahead**

The team heads into the holidays with clear momentum on core workspace
capabilities and strong technical validation that the major
architectural bets are sound. The focus for the final days of December
centers on buttoning up the pulses infrastructure for January
activation, completing Sean\'s RFC on workspace core ownership, and
finalizing product decisions on artifact template deployment approaches.

Coming out of the break, the team faces a packed January with multiple
workstreams converging. Gabe will drive the GTM data model migration
alongside meetings functionality development, requiring tight
coordination with engineering to manage the interdependencies. Ant plans
to deploy pulses to beta users and begin the more complex work of pulse
preferences and notification management with David. Dylan needs to make
the call on whether to launch slides artifact with user-level controls
or hold for tenant configuration, and the team expects to have mobile
workspace in users\' hands for real-world testing. Sean\'s centralized
tracking structure for GTM data store integrations should provide the
visibility needed to orchestrate these parallel efforts while David
pushes for resolution on the priority accounts dependency with the
search team.

The foundation is solid. The team demonstrated this week that they can
make tough resource trade-off decisions, ship meaningful capability
improvements, and tackle complex technical challenges across the stack.
The path to February is clear even if the execution will be intense.

*Source: Team SalesOS/Copilot Operating Framework entries from \[Dec.
15, 2025 - Dec. 19, 2025\]*
