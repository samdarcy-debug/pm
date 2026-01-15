---
id: weekly-product-ops-2025-29
title: "Product Ops Weekly Report - July 18, 2025"
type: weekly-report
status: approved
team: product-ops
owner:
created: 2025-07-18
updated: 2026-01-06
week_ending: 2025-07-18
reporting_period: "July 14-18, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Product Ops Team Executive Roundup - July 14, 2025**

## **Executive Summary**

The team delivered significant process improvements this week with
Kristin completing the LRT automation streamline and Ken advancing the
PMM engine consolidation, while Daniel created a solid proof-of-concept
for demo-to-documentation with GIFs that needs PM testing. Sam finally
secured a path forward for VOC tool deployment after major blockers,
though gaps remain in the semantic data pipeline\'s ability to query
only 100 accounts at a time. AJ & Brett\'s marketing engine presentation
was very well received by leadership, with Henry highlighting it as an
example of desired company innovation. The team also identified the
knowledge graph as a critical missing piece and aligned on a development
path forward, though progress on building the knowledge base remains
slower than needed and requires doubling down efforts.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Process Automation Complete**: Kristin delivered on her week\'s goal
by setting up all LRT automations and change notifications. The new
dashboard and notification channels are running and tested, streamlining
the release process workflow.

**Documentation Innovation**: Daniel identified and tested Clueso
software for converting demo videos into step-by-step documentation with
embedded GIFs. This addresses a key need for creating compelling how-to
guides that draw user attention through visual movement.

**Marketing Engine Recognition**: Brett successfully presented the AI
marketing engine to the leadership team on Tuesday, receiving strong
positive feedback. Henry is actively promoting this work as a model for
company innovation, creating significant internal momentum and
validation for the team\'s approach.

### **Goals & Progress**

**AI Product Development**: Ken made progress consolidating the previous
PMM engine modules 1-3 into a single interface while updating release
notes functionality. However, he encountered significant challenges with
bot training - minor changes to system prompts or documentation often
degraded output quality substantially, requiring rollbacks and restarts.

**Client Platform Integration**: Kristin focused on agentic platform
integration work, with the team beginning to combine repositories and
bringing Lars into coordination discussions. The emphasis shifts to
engineering readiness as teams prepare to move into Jira for ticket
creation using prototype-based instructions.

**Data Pipeline Progress**: Sam secured Guy\'s approval to use ZDP in
the short term, removing a major blocker. The team also identified an
agentic API as a potential workaround with fresher data, though they\'re
still waiting for newer data to be pulled into ZDP for broader account
coverage.

### **Strategic Challenges**

**AI Training Complexity**: Ken\'s experience with the PMM engine
reveals the fragility of AI system tuning - small prompt changes cause
significant output degradation. This highlights the need for more robust
training approaches or potentially shifting to an agents workflow model
that reduces iteration costs.

**Deployment Bottleneck**: Despite approval, Sam\'s VOC tool deployment
remains stuck due to unresolved technical issues with large account
selection. This blocks the knowledge graph work that Daniel and Sam need
to begin, creating downstream impact on multiple initiatives.

**Communication Fragmentation**: Feedback highlighted that multiple
Slack channels and parallel requests create confusion for stakeholders.
The team identified this as a systematic issue requiring centralized
coordination rather than just additional messaging.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Holistic Release Planning**: Kristin\'s discussions with team members
reinforced the importance of thinking about releases as part of the
broader SDLC rather than isolated events. This suggests need for better
integration between planning, prototyping, and release phases to
optimize the entire development cycle.

**AI Documentation Potential**: Daniel\'s testing of Clueso reveals a
viable path for creating engaging, visual documentation that addresses
PM feedback needs. While the software requires some editing work, it
offers a scalable solution for the recurring documentation challenge at
an acceptable cost point (maximum \$10K annually for the team).

**Report Quality Control**: Daniel noted that Andres called attention to
the transparency of DAI reports, emphasizing that leadership closely
reviews these appendices. This reinforces the need for careful review of
AI-generated content before distribution.

### **Cross-Team Dependencies**

The technical CX bar development requires Guy\'s return and input,
creating a bottleneck for the knowledge base components. This missing
piece impacts the broader knowledge graph initiative that spans multiple
team members\' work.

Emily\'s enablement team meeting on Tuesday needs clear requirements
documentation rather than just discussion. The team must provide
specific timelines and deliverables to avoid unproductive coordination
meetings.

## **Looking Ahead**

**Primary Focus**: Knowledge graph development emerges as the central
priority, with Brett creating an outline document today and Sam
targeting a proof-of-concept with even five documents by mid-week.
However, progress on building the comprehensive knowledge base remains
slower than needed, requiring the team to double down efforts and
accelerate this foundational work that will enable multiple downstream
initiatives.

**Immediate Actions**: VOC deployment needs resolution Monday morning
through direct coordination with Guy. Daniel will complete the OP model
reports by 3:30 PM today with explicit callouts for missing submissions.
Ken will time-box his AI training work through noon today before
exploring alternative approaches.

**Strategic Coordination**: The team implements a three-part
communication solution - a centralized canvas for upcoming work,
calendar invites with embedded instructions, and consolidated release
notes. This addresses stakeholder feedback while maintaining development
momentum without adding coordination overhead.
