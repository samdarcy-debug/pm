---
id: weekly-product-ops-2025-44
title: "Product Ops Weekly Report - October 31, 2025"
type: weekly-report
status: approved
team: product-ops
owner:
created: 2025-10-31
updated: 2026-01-06
week_ending: 2025-10-31
reporting_period: "October 27-31, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Product Operations Team Executive Roundup - October 27, 2025**

## **Executive Summary**

Brett Jacobs identified a flaw in how the company has approached release
automation: downstream teams are still manually summarizing AI-generated
content the same way they did before, just faster. The feature info
packs contain rich information and use AI, but enablement, customer
success, and field teams take that output and summarize it again for
their audiences - building \"a better typewriter instead of a computer\"
as Brett described it. This realization came as Kristin Gandini and Sam
Darcy brought both the VOC tool and Agent Builder to launch-ready state,
and Ken Elwell moved the workspace changelog to near-final status. The
team now has clarity on priorities through Brett\'s focus document, with
VOC rollout and knowledge management taking center stage while mid-tier
initiatives move to maintenance mode.

## **This Week\'s Progress**

### **Key Momentum Areas**

Brett clarified strategic priorities across the team through a focus
document that emphasizes getting the VOC tool launched and establishing
regular cadences, primarily driven by Kristin Gandini and Sam Darcy. The
middle initiatives are effectively deprioritized or moved to maintenance
mode, creating clarity on where the team invests energy. For Ken, the
focus is pushing forward the launch assets and release process work. For
Daniel Kong, it\'s closing the knowledge loop so that foundational
information exists, end assets are ready, and questions get answered
efficiently for GTM Studio and Copilot Workspace.

Ken Elwell moved the workspace changelog significantly closer to final
and initiated the GTM Studio release tracking work. The key insight from
the week is that sending changelogs out to the GTM team feels like the
wrong use case - there isn\'t real demand for it. The higher-value
application is automating release tracking as an input to other
workflows, particularly the MCR process. The release notes site at
gtm.ai/release-notes is live, with zoominfo.com tracking toward November
18.

Kristin Gandini has both the VOC tool and the Agent Builder for
prototyping ready to roll out, with the Agent Builder held up only by a
final PR approval. The challenge now is sequencing these launches
effectively without overwhelming PM teams, especially with planning
season approaching. The Agent Builder enables rapid prototyping of new
agents, while the VOC tool needs to expand beyond just the initial use
cases into regular workflows and rituals for tracking progress on top
customer issues.

### **Goals & Progress**

**Release Process Automation**: Brett and Ken worked through technical
requirements for getting PR data from Dan and Guy\'s system. The ideal
state is having saved filters for Copilot Workspace and GTM Studio that
automatically populate with PR descriptions and associated Jira tickets,
exportable to CSV on demand. This avoids relying on the engineering team
to run and maintain prompts, giving the Product Ops team control over
tuning the changelog generation process. Guy suggested they could
automate the LLM output on the backend, but Brett rejected this approach
because the prompt will need too much tuning over time and shouldn\'t be
dependent on engineering resources. The solution is either a saved
search that updates as PRs come in, or a weekly batch process that
generates the data for export.

**Strategic Release Vision**: Brett articulated the \"driverless
carriage\" problem with current release processes - the team has feature
info packs with rich information and uses AI to generate summaries,
which is faster than before. But downstream teams (enablement, customer
success, field) still consume it the same way by manually summarizing
and redistributing it. This is like building a better typewriter when
computers exist. The breakthrough is recognizing that products like GTM
Studio and Workspace enable mass personalization, which is exactly what
release communications need. Brett proposed running release information
through these products to blend it with account intelligence, but
acknowledged this is primarily product question marks that need
discovery work.

**Voice of Customer Infrastructure**: Brett nearly completed the VOC
analysis for the 2026 roadmap but ran out of Claude credits before
finishing. Kristin and Sam are preparing to roll out the VOC tool to PM
teams, but need to think through positioning and timing carefully.
There\'s a dual challenge: shipping the initial tool with core use
cases, and establishing the second layer of workflows and rituals around
how teams will use VOC on a regular cadence to track progress on top
issues and drive action. The rollout strategy needs to avoid
overwhelming PMs while ensuring each capability gets proper attention
and adoption.

**Knowledge Management**: The Docket knowledge base is currently a
\"shitshow\" according to both Brett and Ken, with people dumping
unstructured content including poorly transcribed meeting recordings.
Ken gained access and cleaned up bad documents. Daniel Kong needs to
focus heavily on closing the knowledge loop when he returns -
establishing clear processes for how questions come in, how the team
supports sellers, and how to create new assets from existing
foundational information. The pieces exist but need systematic
organization for GTM Studio and Copilot Workspace pods.

### **Strategic Challenges**

The automated release tech meeting on Tuesday has become complicated
with multiple stakeholders and confusion about two different tools being
discussed. Emmy and Josh added Emily from enablement plus other people
to a meeting that was meant to align on technical requirements. Kristin
plans to clearly delineate which tool is ready for enablement handoff
(the CX-focused one) versus which one Ken is working on, since Dan and
Guy keep getting confused about where one ends and the other begins.
Brett suggested potentially repurposing that meeting time for the
release changelog work after the CX tool discussion wraps.

The knowledge management situation with Docket represents a broader
challenge around too many cooks in the kitchen without clear ownership
or standards. People are uploading random content without structure,
making it difficult for the chatbot and other tools to surface relevant
information. The team has all the necessary pieces - knowledge bases are
set up, exploration with Docket is done, conversations with specific
teams have happened - but there isn\'t a systematic process that Daniel
can enforce for the GTM Studio and Workspace domains. This becomes more
critical as the chatbot potentially replaces Docket within the next 6
months.

Product Management Ops ownership of the release process isn\'t clearly
established. Brett identified that PMOs should be the anchor point for
holistically saying what shipped for a given product universe, but they
don\'t totally know currently and are asking to be included in meetings.
The PMs need to define how releases should be structured, but there\'s
ambiguity about who ultimately owns the changelog and how it gets
maintained. This creates coordination challenges as the team tries to
automate more of the process.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Brett\'s realization about the \"driverless carriage\" problem
fundamentally reframed the release work. The team has most of the
information in feature info packs and is using AI to generate summaries,
which is faster than before. But downstream teams still consume it the
same way - by manually summarizing and redistributing it. This is like
building a better typewriter when computers exist. The breakthrough
insight is that products like GTM Studio and Workspace enable mass
personalization, which is exactly what release communications need.
Instead of one-size-fits-all summaries, the team should explore whether
these products can blend release information with account intelligence
so field teams see only what\'s relevant to their specific accounts.

The PMO anchor point insight clarifies ownership questions that have
been creating coordination overhead. If PMOs are responsible for
holistically tracking what shipped in their product domain, then they
should be the primary consumer and validator of automated changelogs.
This gives the team a clear stakeholder to work with on structure and
content rather than trying to serve too many audiences simultaneously.
The challenge is that PMOs don\'t currently have full visibility, which
is why they\'re requesting inclusion in various meetings.

Kristin\'s observation about the dual nature of the VOC rollout is
important for preventing failure. The team can\'t just ship a tool and
expect adoption - they need to establish workflows and rituals around
how PMs will use it regularly to track progress and drive action. This
is the difference between a demo that impresses and a capability that
changes behavior. The sequencing and positioning of the rollout needs to
account for both the initial \"here\'s what it can do\" launch and the
ongoing \"here\'s how you integrate it into your work\" adoption
process.

### **Cross-Team Dependencies**

The automated release work depends heavily on Dan and Guy\'s engineering
team delivering the right data structure in an exportable format. Brett
is very clear that the Product Ops team cannot rely on engineering to
run and maintain prompts for changelog generation - they need raw data
they can process themselves. This means getting agreement on saved
filters or batch processes that populate PR descriptions and Jira ticket
associations for Copilot Workspace and GTM Studio separately.

Kristin\'s VOC and Agent Builder rollouts need careful coordination with
planning timelines and PM capacity. Launching powerful new tools right
as teams enter planning season could either be perfect timing or create
overload. The team needs to think through not just the tools themselves
but how PMs will incorporate them into planning workflows versus ongoing
product development rhythms. The Tuesday automated release tech meeting
has become crowded with enablement and other stakeholders, requiring
clear communication about which tool is ready for handoff versus still
in development.

## **Looking Ahead**

Brett\'s immediate priority is finishing the VOC analysis for the 2026
roadmap, assuming he can get more Claude credits. This foundational work
needs to close out so Kristin and Sam can roll out the VOC tool to PM
teams next week. The rollout strategy needs to address both the initial
tool capabilities and the ongoing workflows and rituals for how teams
will use it regularly.

Ken\'s focus shifts to discovery work on whether GTM Studio and
Workspace can actually deliver on personalized release communications.
This means trying to run real release data through the product and
identifying where it breaks. The concept is piloting with a few CSMs to
validate whether the team can blend release information with account
intelligence to show field teams only what\'s relevant to their
accounts. Daniel Kong will support the changelog work when he returns,
as that falls more naturally in his domain of knowledge management.

Kristin needs to finalize the Agent Builder PR approval and determine
the best sequencing for rolling out both the Agent Builder and VOC tool
without overwhelming PM teams. The automated release tech meeting on
Tuesday will be the venue for clearly separating the CX-focused tool
(ready for enablement) from the changelog work (still in development),
preventing further confusion between Dan, Guy, and the growing list of
stakeholders. The team is building toward a future where release
planning is automated and personalized, knowledge management is
systematic, and PM teams have powerful VOC capabilities embedded in
their workflows.
