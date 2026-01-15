---
id: weekly-zim-2025-47
title: "ZIM Weekly Report - November 21, 2025"
type: weekly-report
status: approved
team: zim
owner:
created: 2025-11-21
updated: 2026-01-06
week_ending: 2025-11-21
reporting_period: "November 17-21, 2025"
tags: ["weekly-report", "Q42025"]
---

# **ZIM Team Executive Roundup - Week of November 17, 2025**

## **Executive Summary**

We successfully shipped the MCR monthly release Tuesday with AI PageRank
live and automated traffic filtering at 25% rollout, demonstrating
continued delivery despite resource constraints. However, a critical
strategic ambiguity has emerged: Dominik\'s vision for workbooks
integration into websites, form complete, and intent UIs is being
interpreted differently across teams---Matt and Ganesh believe we\'re
bringing ZIM data into workbooks, while Dominik\'s messaging suggests
bringing workbooks into our UIs. This needs immediate clarification
before we invest significant engineering effort in the wrong direction.
Meanwhile, we\'re facing a \$500K churn hit from Equinix and User Agent
choosing Sixth Sense, and Freewill partnership remains blocked on SOC 2
compliance.

## **This Week\'s Progress**

### **Key Momentum Areas**

Matt Barnes delivered the MCR monthly release flawlessly on Tuesday. AI
PageRank is live across all enabled customers with automated traffic
filtering at 25% rollout (remaining 75% deploying in weekly increments).
Early cost data shows 99 domains enabled in 2 days for \$1,500, with
anticipated monthly costs around \$5,000 total---well within acceptable
parameters. Ganesh reported no concerns about the spend, and the only
minor issue is updating a dashboard graph to reflect new resolution
rates.

Brett Elliot achieved a major breakthrough on the web search agent
Temporal migration. After last week\'s timeout failures on 10K row
workbooks, the team implemented smarter chunking and successfully tested
on a 60K workbook. The obstacles were overcome and it\'s now running
reliably. The emailer agent has also been migrated to Temporal but
remains untested due to resource blockers that Tushar and Grant are
working through.

Jesse Miller confirmed the orchestrator is calling the right subagents,
with Troy documenting the trigger questions that route to each agent.
The Applied AI team completed two deep dive sessions and received full
access to data and repos. Bot model identification became priority one
for new team members since better bot detection directly improves
traffic quality, which cascades into better conversion model
performance. Troy is shifting 75% of his focus to the intent agent to
accelerate delivery to the apps team.

### **Goals & Progress**

**Intent Agent & Data Architecture**: Shuxin Yang finalized the approach
to bypass the delayed ClickHouse data stream by calling intent
entitlement endpoints directly from Mongo for real-time data. Troy will
implement this for the intent agent and potentially other agents needing
advanced search capabilities. However, the GTM Store data volume
analysis revealed a significant architectural question: we\'re expecting
7 billion records daily, and while GTM Store can technically handle
billions of signals, the cost implications need deeper discussion about
future architecture and data consumption patterns versus maintaining
dispersed systems that limit scalability.

**Agent Platform & Infrastructure**: Brett completed web search agent
Temporal migration with successful 60K row testing. Emailer agent is
migrated but blocked on testing resources from Tushar (who claims it\'s
quick/easy but has no capacity). Jesse\'s orchestrator work is solid,
and he\'s preparing to deploy the ZI chat Audience Builder Agent to the
zi.com website using a quick API-based approach similar to what Caitlin
is doing with Henry feedback on the homepage. Email notifications remain
close to completion pending Aiden\'s return to finalize two Sprint
Review tickets.

**Webhook & Pipeline Development**: Matt is finalizing the revised
webhook PRD requirements by end of week, leveraging the global event bus
infrastructure (CDC, existing webhook, credit API, enrichment APIs).
He\'s scheduling another meeting with Amesh\'s team the week after
Thanksgiving to maintain momentum. December release feature packs are
complete and submitted.

**GTM Config & Person Briefs**: Aadhi made progress on GTM Config
initiative but had an overall slow week. Roadmaps for both config and
person briefs remain in progress with some items likely rolling into
next week. Goal is to complete these and have final versions ready to
share internally.

### **Strategic Challenges**

The workbooks integration vision is fundamentally unclear and creating
confusion that could derail significant engineering investment.
Dominik\'s messaging suggests bringing workbooks natively into websites,
form complete, and intent UIs. However, Ganesh consistently interprets
this as bringing our data into workbooks---essentially making workbooks
the UI layer. Matt needs a gap analysis of what websites/FormComplete UI
currently supports versus workbooks capabilities (real-time data,
audience size) before we can build a plan. We need Dominik on a call
immediately to clarify his actual vision: are we replacing list features
in websites with workbooks, or are we feeding ZIM data into the
workbooks spreadsheet interface? Harry mentioned working on \"a plan\"
but it\'s unclear what that means.

Freewill partnership remains blocked on compliance hurdles that are
proving more difficult than anticipated. They don\'t have a SOC 2 report
for 2025 and don\'t expect one until December. Our IE team (James Grant)
still wants security questionnaires completed. We\'re trying to drive
for an exception---if Trade Desk didn\'t require this level of scrutiny,
why should Freewheel/ Beeswax?---but this is dragging on longer than
expected and impacting our identity partner expansion timeline.

The churn impact from October is materializing: \$1M of the \$2.2M
expiring ACV represents the 47% churn we saw. Specifically, Equinix and
UserAgent chose 6Sense over us for approximately \$500K combined. This
validates the concern that resource reallocation away from ZIM is
costing us competitive positioning. The December renewals remain
critical, and losing half a million to a competitor like Sixth Sense
should inform our bug bash priorities.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Shuxin added numerous quick wins tickets sourced directly from CX teams,
bug batch, and support teams. This direct pipeline from customer-facing
teams to engineering prioritization should become standard practice---it
ensures we\'re addressing pain points that actually affect retention
rather than theoretical improvements. As we approach the Sprint 2525 bug
bash, this CX-driven ticket pipeline becomes even more valuable for
identifying high-impact fixes.

The identity partners intent scanning question has legal and product
implications that need resolution. When partners fire on pages
containing healthcare data (like diabetes medication information), we
collect the URL and link it to visitor ID/cookie even when there are no
relevant intent topics configured. Shuxin\'s agent reviews intent topics
daily and removes inappropriate ones, but the question remains: is
having URLs mapped to user IDs itself a legal problem? This needs
clarity from Hannah and legal before we scale identity partner
integrations further.

The 7 billion daily records for GTM Store forces an architectural
philosophy decision. Yes, cost matters, but Shuxin correctly identifies
that we need to evaluate future data consumption needs and application
architecture. Maintaining dispersed systems prevents the scaling and
acceleration that GTM Studio requires. This is a classic
build-for-scale-now versus optimize-costs-today tradeoff that needs
executive alignment, not just engineering debate. The discussion
scheduled for early next week needs clear decision-making authority.

### **Cross-Team Dependencies**

The workbooks integration confusion highlights a critical breakdown in
requirements gathering. When Dominik, Ganesh, Matt, and Brett all have
different interpretations of the same initiative, we\'re setting up for
wasted cycles and misaligned execution. This isn\'t a technical
dependency issue---it\'s a leadership alignment gap. We need Dominik to
provide written requirements describing exactly what he envisions, not
just verbal direction that people interpret differently. The timing is
especially problematic since workbooks isn\'t at parity with websites
capabilities, making the gap analysis even more critical before we
commit resources.

Applied AI team enablement is progressing well with bot model as
priority one, but we\'re still managing limited resourcing challenges.
Email notification support has been difficult to get over the line due
to resource constraints, though it\'s close to completion and will free
up team bandwidth once deployed. The short week ahead (Thanksgiving)
compounds these resource limitations, so we\'re pausing weekly goal line
items until the following week when people return.

## **Looking Ahead**

No formal weekly goals due to Thanksgiving week, but key momentum
continues. Jesse is figuring out deployment path for the ZI chat
Audience Builder Agent to zi.com website using the quick API approach.
Brett\'s singular focus is getting emailer agent successfully migrated
to Temporal once testing blockers are resolved. Aadhi wraps up GTM
Config and person briefs roadmaps for internal sharing. Matt schedules
the Amesh team meeting for post-Thanksgiving to keep webhook work
moving.

The most critical action item is scheduling the Dominik call to clarify
workbooks integration vision. Matt needs to understand whether we\'re
replacing websites list features entirely, bringing our data into
workbooks spreadsheet UI, or something else entirely. This blocks
significant 2026 planning and resource allocation decisions. We cannot
guess wrong and invest engineering effort in the wrong
direction---especially given current resource constraints and the
December renewals situation.

Shuxin\'s conversation about GTM Store architecture and the 7 billion
daily records needs resolution early next week. This isn\'t just a cost
discussion but a fundamental question about how we architect for scale
versus maintaining dispersed systems. The team should come prepared with
cost projections, scalability analysis, and recommendations rather than
just presenting the problem.

Post-Thanksgiving, we resume normal operating cadence with accumulated
updates from the short week. The bug bash in Sprint 25.25 remains our
next major milestone for addressing customer-facing issues before
December renewals close.

*Source: Team 1-2-3 Operating Framework entries from November 17-21,
2025*
