---
id: weekly-zim-2025-46
title: "ZIM Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: zim
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

# **ZIM Team Executive Roundup - Week of November 10, 2025**

## **Executive Summary**

Big win: Zoominfo was named an ABM(Account based marketing) leader for
the second year in a row by Gartner! We\'re facing a critical inflection
point: ZIM achieved 92% net retention in October, but 47% ACV
churn---our highest in a year---with \$4M in December renewals at risk
(60% unknown status). This is the result of engineering reallocation to
GTM Studio and the Agentic platform. Filip has escalated to Sneh and
Dominik, and we\'ve scheduled a bug bash for Sprint 25.25 (first week of
December) to address customer-facing issues before these renewals close.
Meanwhile, our infrastructure work continues to progress with Matt
Barnes\' website identity pipeline back on track and MCR launching
Tuesday.

## **This Week\'s Progress**

### **Key Momentum Areas**

Matt Barnes recovered critical momentum on the website identity pipeline
after earlier setbacks. The team developed a plan to get all required
website data delivered by January, with website data expected by end of
sprint and form-complete PubSub available early-mid next week. This
unblocks the webhook delivery work that Dominik has been tracking and
enables website buyer ID to flow into GTM audiences.

Jesse Miller successfully onboarded the Yoda team to the audience agent
with orchestrators now live in the demo environment, allowing the team
to test context injection and subagent routing. He pivoted the Applied
AI planning approach from premature ticket creation to focused knowledge
transfer sessions, preventing wasted effort and ensuring Q4 execution
stays on track.

Shuxin Yang achieved alignment on the intent agent approach for co-pilot
requirements and finalized the strategy for getting account-level intent
into GTM Store. Despite this not being the ideal long-term solution, it
provides a pragmatic path forward. Resources are now secured to start
Persona Intent this sprint, with Yoda picking up quick wins next sprint.

### **Goals & Progress**

**Agent Platform & Migrations**: Brett Elliot is wrestling with the web
search agent Temporal migration(Agent Infra), discovering timeout issues
when processing 10K row workbooks. The team is exploring smarter job
chunking strategies, with a fix expected tonight. The good news is that
the emailer agent migration started in parallel and appears to be a
simpler lift. Both migrations remain on staging until these issues are
resolved.

**Website Identity & Infrastructure**: Matt Barnes completed 75% of the
webhook delivery PRD with an end-to-end walkthrough scheduled Monday
with Mesh. The websites API blocker for flywheel data partners is
resolved with a manual provisioning approach (Eli Greenstein assisting).
**Tuesday launch: AI PageRank and automated bot filtering via MCR.**

**LinkedIn Campaign Management & Agents**: Jesse Miller delivered
requirements to Sylvia for LinkedIn campaign management UI mocks (V1
expected next week), which will be 90% reusable for Meta versions. Troy
is leading agent architecture with Applied AI eager to contribute once
knowledge transfer is complete, targeting demoable MVP agents for sales
and CX showcase.

**GTM Config & Person Briefs**: Aadhitthyaa completed schema design for
offerings data changelogs and made 50% progress on AFS onboarding flow.
A Spectra customer call revealed a significant gap: Boardroom Insider\'s
person briefs substantially outperform ours. Aadhi is adding podcast
mentions, personal interests, and moving beyond the single XVRM vendor
dependency to the roadmap.

**Intent & Persona**: Shuxin Yang secured alignment on creating one
intent agent and finalized the approach for account-level intent in GTM
Store. He\'s investigating volume and cost implications with Caleb (GTM
Store can handle billions of signals). A visit with Staples uncovered
that their engagement data could identify high-potential
opportunities---a potential new intent source for enterprise customers
that Shuxin will explore with Sanyog.

### **Strategic Challenges**

The 47% ACV churn is a direct consequence of deprioritizing ZIM to staff
GTM Studio and the Agentic platform. With \$4M in December renewals (60%
status unknown), we need the bug bash in Sprint 2525 to address
customer-facing issues. This resource allocation tradeoff was necessary
for strategic priorities, but we must demonstrate value to at-risk
customers immediately. Filip is aware and has escalated appropriately.

Brett\'s web search agent timeout issues highlight the complexity of
migrating production workloads to Temporal at scale. None of the 10K row
jobs completed in stress testing. While the team is exploring solutions,
this blocks production deployment and could impact customer-facing agent
performance. We need to ensure the chunking strategy actually solves the
problem before committing to this architecture.

Aadhi\'s gap analysis exposed a competitive vulnerability in person
briefs. Boardroom Insider provides C-level executive and board
information that\'s significantly more comprehensive than our current
XVRM-only approach. With customers like Spectra explicitly requesting
this consolidation, we\'re leaving revenue on the table. Rethinking our
person briefs strategy needs to move from \"nice to have\" to
\"competitive necessity.\"

## **Strategic Insights**

### **Key Learnings & Discoveries**

The target accounts concept needs a strategic decision: should we evolve
the existing feature or deprecate it in favor of account priority score?
This conversation has been ongoing, but it\'s blocking Aadhi\'s ability
to proceed with the onboarding flow work. We need alignment on the
long-term vision to avoid building on a foundation we\'ll abandon.

We should build an agent within the ZI chatbot to evaluate identity
partner data. As we continue testing with partners like Cuspera (who are
requesting more credits), we need systematic analysis of: new users
being identified, verification of existing visitors, and quantification
of the delta. This would help us make data-driven decisions about
partner value rather than intuition-based credit allocation. Sindhu is
tasked with initial Cuspera analysis.

Shuxin\'s Staples visit revealed that enterprise customers have rich
engagement data they don\'t know how to prioritize. Helping them
identify which engagements deserve follow-up to maximize revenue
potential could become a differentiated intent capability. This
generalizes beyond Staples---many enterprise customers likely have
similar untapped data that we could turn into actionable intelligence.

### **Cross-Team Dependencies**

Our work with Adobe is nearing completion on their integration testing
for ZI as a destination. We\'re waiting for approval to launch to DX &
DME teams so their internal teams can use it ASAP, with IBM Red Hat also
planning Q1 usage. Once this closes, we need a 2025 retro to improve the
2026 process for the next integration where ZoomInfo serves as a source
of data---the current approach has been challenging and we should learn
from it.

Matt\'s website identity pipeline work depends on Sneh and Victor\'s
team, who won\'t be ready until January. This timeline is set and
communicated to Dominik. The pipeline feeds multiple consumers (GTM
audiences, App and others), so delays ripple across teams. We\'ve built
the plan around this constraint, but any further slippage from their
side would cascade to our Q1 deliverables.

## **Looking Ahead**

Our immediate focus is protecting the December renewals while
maintaining momentum on infrastructure and agent platform development.
The MCR launch Tuesday (AI PageRank and bot filtering) demonstrates
continued delivery despite resource constraints.

Next week, Jesse\'s team gets V1 LinkedIn campaign management UI mocks
for review, Applied AI deep dives continue for knowledge transfer, and
we push toward demoable MVP agents for sales and CX to showcase on
renewal calls. Matt\'s webhook delivery PRD and end-to-end walkthrough
Monday should unblock that workstream. Brett needs to resolve the web
search agent timeout issues and get both migrations to production.
Aadhdi prioritizes Yoda quick wins with Tomer on Monday and continues
weekly GTM Config reviews with Dominik to develop the long-term roadmap
people keep requesting. Shuxin investigates intent volume/cost
implications with Caleb and explores the Staples engagement data
opportunity with Sanyog.

The bug bash in Sprint 25.25 is our best opportunity to shore up
customer confidence before year-end renewals close. We\'re being
transparent about the impact of resource reallocation while
demonstrating we\'re still shipping value and addressing technical debt
that affects customer experience.

*Source: Team 1-2-3 Operating Framework entries from November 10-14,
2025*
