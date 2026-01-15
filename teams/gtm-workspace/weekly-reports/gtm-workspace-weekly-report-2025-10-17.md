---
id: weekly-copilot-2025-42
title: "GTM Workspace (Copilot) Weekly Report - October 17, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-10-17
updated: 2026-01-06
week_ending: 2025-10-17
reporting_period: "October 13-17, 2025"
tags: ["weekly-report", "Q42025"]
---

SalesOS/Copilot Executive Roundup -
[Oct. 13, 2025 - October 16, 2025]

Executive Summary

Copilot Workspace demo readiness for Dreamforce is strong, with over 100 executive meetings
booked and Victor leading product demonstrations alongside the go-to-market team. The
success metric is clear: follow-up meetings generated from these executive demos. Meanwhile,
the November 3 release faces a resourcing challenge on the slides artifact, with Dylan's primary
engineer reassigned to the 00 integration project. Hari completed validation testing on Multi AFS
and Intent Recommendation Phase 2, discovering an entitlement display issue that's being
resolved with provisioning. Adam finalized filter experience designs and launched a user survey
to capture sentiment on chat accuracy and views, while Ant progressed mobile prototypes and
began building a prioritization agent to address the first-time user experience gap that current
logic won't solve.

This Week's Progress

Key Momentum Areas

Gabe advanced the Copilot Workspace convergence strategy by socializing the Chorus
integration roadmap and beginning prototype work on the meeting review experience with
Megan's design team. The DoorDash renewal ($1.2M annually) highlighted strong customer
demand for cross-conversation insights, validating the workspace roadmap's focus on discovery
features that Chorus currently lacks. This convergence work positions workspace as the unified
platform for conversation intelligence while addressing retention needs for high-value accounts.

Hari completed UXR research with three Intent customers, uncovering consistent feedback that
data staleness is becoming a recurring complaint across power users with 6+ years of platform
experience. The research revealed a split in Intent value perception: some customers struggle
to find actionable contacts while others successfully close deals using virtual SDRs and making
100+ calls daily with Intent signals. Testing of Multi AFS and Intent Recommendation Phase 2 is
complete in staging, with only an entitlement display inconsistency requiring resolution before
the planned release.

Dylan aligned with engineering on the slides artifact approach, securing a new resource after
losing the primary engineer to the 00 integration project. The team agreed to start with an
HTML-based slide artifact as the first milestone, with PowerPoint and Google Slides export as a
fast follow. Victor emphasized the HTML version is non-negotiable for November 3, but the
export functionality must be perfect rather than rushed to avoid disappointing customers who've
heard export promises before.

Goals & Progress

Copilot Workspace: Adam finalized designs for foundational view improvements including
unified filter experiences, hover overs, and field selection patterns. The all-chats experience
design sprint with Katya and Whitney is progressing well, focusing on artifact surfacing,
company tagging, and improved search capabilities. Homepage card designs are being refined
to increase engagement beyond the current pattern where users land and immediately hit chat
without noticing the insights. Gabe is drafting detailed requirements for the email agent and
beginning design work on the Saleshub engagement widget, with internal MEDDPIC extraction
pilots launching to validate outputs before broader rollout.

ZoomInfo Intent: Hari's customer research sessions revealed that customers want unified
views of Intent data alongside other platform information, strongly validating the workspace
consolidation strategy. The research also highlighted demand for activity tracking within the
platform to enable sales managers to monitor team productivity on Intent signals and create
gamification opportunities. Multi AFS testing revealed an entitlement caching issue where limits
display correctly in Salesforce but inconsistently in production environments, requiring
coordination between RevOps and provisioning teams to resolve before launch.

Admin Zero Experience: David made progress on Admin Defined Territories by deploying the
workflow solution and completing cleanup to address user state issues that have caused
problems across multiple features. The team added several customers to beta and is finalizing
designs for user reporting capabilities. Priority Accounts work advanced through good progress
prototyping CRM matching rules using the new GraphQL interface from GTM data model, with
design requests being prepared for short-term UI updates needed for the January GTM model
migration deadline.

Additional Initiatives: Ant finalized the mobile prototype and is preparing a demo recording,
with learnings that Okta now has improved React Native support enabling passcode and Face
ID features that weren't available during the original SalesOS launch. He's building a
proof-of-concept prioritization agent to address the gap in serving relevant recommendations to
users, with plans to use it for evaluation and to guide requirements for Robyn and team. Adam
launched a comprehensive user survey to capture sentiment about chat accuracy, view filtering
intuitiveness, and notes functionality, planning to run it through October 24th with incentives
from the enablement team.

Strategic Challenges

The November 3 release timeline for slides artifact is at risk due to engineering resourcing
changes. Dylan's primary senior engineer was reassigned to the 00 integration project, requiring
onboarding of a more junior resource mid-sprint. Victor set a clear threshold: without a build in
staging by end of next week, the feature won't make November 3 given the iteration cycles
required. The team is pursuing a POC for Friday to assess feasibility, but engineering
acknowledges the risk. The path forward requires rapid alignment on whether to ship the HTML
version alone or delay until export functionality is ready.

The first-time user experience logic for homepage content needs improvement beyond the
current approach of checking for open deals and hierarchy. Victor raised concerns that many
users will slip through the cracks with the existing logic based on deal ownership and team
structure. Adam and Ant are partnering to develop an agent-based prioritization approach that
can be evaluated in parallel to the current implementation. This requires solving both the
immediate November 3 need and building toward an agent that uses email data, calendar data,
account insights, and opportunity insights to intelligently prioritize what users see when they first
open workspace.

Hari discovered through customer research that when users take actions in the Copilot platform
like email outreach or calls, they want tracking and visibility into those activities. Sales managers
specifically want to monitor team productivity and see who has actioned Intent signals. This
requirement for activity tracking and team visibility didn't emerge until customer conversations
revealed the need, suggesting that workspace views and manager-specific features need
development to support this workflow that customers are explicitly requesting.

Strategic Insights

Key Learnings & Discoveries

Hari's Intent customer research revealed a consistent theme across three power users: data is
becoming stale more frequently, especially contact data. This feedback from customers with 6+
years of platform experience suggests a systematic data quality issue that needs attention. The
research also uncovered extreme variation in Intent value perception, with some customers
unable to derive value from signals while others close significant deals using virtual SDRs and
making 100+ calls daily. Understanding what separates successful Intent users from struggling
ones could inform both product improvements and customer success strategies.

Victor's vision for workspace positioning it as the first thing users check at 8am every morning is
crystallizing into a concrete product direction. By pulling email, calendar, account insights, and
opportunity insights into a unified "pulse" feed (rather than calling it a feed), workspace becomes
the universal inbox for go-to-market that doesn't exist today. This isn't about becoming an email
client but rather serving as an intelligent signpost that routes users to Gmail or other tools with
context and recommended actions. Ant's mobile work aligns with this vision through a "today"
concept that separates administrative tasks from research exploration.

Adam's discovery that users land on the homepage and immediately hit chat without noticing
insights reveals a design challenge that goes beyond visual appeal. The underlying logic of
what to surface matters more than the design polish. Homepage content needs to be driven by
intelligent prioritization that considers deal status, hierarchy, email patterns, calendar
appointments, and signals rather than simple rules about open opportunities. This learning
reinforces that agent-based approaches may be necessary to create genuinely useful first-time
experiences rather than trying to capture all edge cases with if-then logic.

Cross-Team Dependencies

Our work with the Israel engineering team on AFS filter functionality in Advanced Search has
been blocked for the past two to three weeks. Hari escalated this issue, and with the team
returning from holidays this Wednesday, we need to prioritize getting the issues resolved.
Multiple Copilot customers are waiting for AFS filter in advanced search, and the development is
complete except for the 3-4 blocking issues. This dependency is holding back customer value
delivery on a completed feature.

Dylan's slides artifact work depends heavily on Lars and the R&D team's availability and
prioritization. The loss of Noah to the 00 integration project mid-stream demonstrates how
platform-level initiatives can disrupt product team execution. We need clearer communication
about resource shifts that affect committed delivery timelines, particularly when those timelines
have been communicated to executive stakeholders. The Friday POC will be an important
checkpoint to assess whether alternate resourcing can recover the schedule.

Looking Ahead

The next week centers on Dreamforce execution and November 3 release finalization. Victor will
be supporting over 100 executive meetings with workspace demos, measuring success by
follow-up meetings generated. On Monday, the team conducts a full November 3 release review
with Dominic and Philip, requiring coordination across all product managers to present a
coherent view of workspace-specific features, profiles improvements, first-time UX, and the
outreach/sales loft actions and workbooks integration that are under pressure.

Mobile development is reaching a key milestone with Ant's prototype ready for broader
stakeholder sharing and the beginning of dependency conversations with Lars' chat team now
that Dreamforce dust has settled. The mobile beta target remains November with January MVP
launch. Prioritization agent development by Ant will be tested in staging this week after code
freeze ends, with plans to share findings with Robin's team to guide production implementation.
Adam's user survey runs through October 24th and will provide data to inform resource
allocation and strategy for the remainder of the year on chat accuracy and view improvements.

The slides artifact timeline will become clear by end of next week based on whether a staging
build materializes. If it doesn't, the team needs to make a call on whether to delay the feature or
ship HTML-only capability. Gabe continues driving email roadmap alignment and Chorus
convergence work, with technical feasibility discussions scheduled with Lars and Ryan on
whether the artifact system can handle the complexity being layered into email sequencing
requirements. David needs to sync with Victor on zero admin setup scope and priorities for the
week, with continued progress expected on territories and priority accounts work.
Source: Team SalesOS/Copilot Operating Framework entries from [Oct. 13, 2025 - Oct. 16,
2025]
