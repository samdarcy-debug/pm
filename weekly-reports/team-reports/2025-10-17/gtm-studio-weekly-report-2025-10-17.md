---
id: weekly-gtm-studio-2025-42
title: "GTM Studio Weekly Report - October 17, 2025"
type: weekly-report
status: approved
team: gtm-studio
owner:
created: 2025-10-17
updated: 2026-01-06
week_ending: 2025-10-17
reporting_period: "October 13-17, 2025"
tags: ["weekly-report", "Q42025"]
---

GTM Studio Executive Roundup - October
13-17, 2025

Executive Summary

The November 3rd joint launch of GTM Studio and Copilot Workspaces is locked and loaded,
with all enablement content hitting the runway this week. Workbooks secured our first paying
customer last week using signal-based workbooks for Website Buyer ID activation, while
Dreamforce demos validated strong market resonance across strategic accounts. Plays
completed high-level PRD review for DoubleO M2 integration and closed critical loose ends for
Copilot activation MVP, though the email experience still needs urgent improvement. ROI
Analytics achieved platform alignment on opportunity history data with a short/long-term
solution, which is the GA blocker pending ETA confirmation from the Platform team next week.
Data Management iterated V2 requirements for Data Health Scan based on strong AM
feedback and is already generating sales traction--TK Newman secured a Randstad meeting
while Palo Alto Networks scheduled follow-up conversations. GTM Config completed six
internal feedback sessions revealing critical UX assumptions that need revision, while design
prototyping progresses toward customer validation sessions.

This Week's Progress

Key Momentum Areas

First revenue secured ahead of launch. Lou closed our first paying GTM Studio customer last
week, specifically activating Website Buyer ID signals through signal-based workbooks--the
only scalable list-building path for this use case. This validates our core value proposition before
the November 3rd launch and demonstrates immediate monetization potential.

November launch readiness accelerating with cross-functional alignment. Sneh delivered
pricing and packaging finalization to Mark's team, with enablement materials now in active
production across platform overview, Studio-specific selling, and objection handling tracks. All
content drops into team channels this week for review, ensuring sales and SC teams are
equipped for the joint Studio-Workspace rollout.

The Platform engineering/PM team has identified the ROI GA path. After coordination with
Platform PM/Engineering (Andres, Asaf), and CFA PM/engineering (Brahm/Arun/Ashwani), the
team aligned on short-term (Platform backfills legacy ZDP data into GTM Data Model) and
long-term (full opportunity history ingestion from CRMs) approaches, pending Platform's ETA
confirmation next week for the short-term solution to clear the roadblock to ROI GA.
Goals & Progress

Workbooks: Tanvi completed PRD reviews for create-sheet-from-column and object parsing,
with intent/scoops updates wrapping today and run-single-column/cell review scheduled. On
find contacts enhancements, she kicked off discovery with Sneh to establish user flows and
good-better-best phasing--Sylvia joined as the assigned designer, though Tanvi needs quick
re-assignment coordination after learning the original designer is no longer on the project. She
also outlined a high-level plan to add Account Priority Score (APS) into workbook enrichment,
enabling sorting and prioritization, and connected with the content team to supply information for
Knowledge Center articles and how-to guides. A critical learning emerged from customer calls:
every user instinctively adds recommended signals (they're labeled "recommended" with quick
checkbox UI), but consistently gets zero results due to underlying relevance filtering that's
invisible to users--even internal teams don't fully understand this behavior. Tanvi is partnering
with Srivatsa to address this through KC articles and enablement as immediate mitigation.
Jagan delivered exceptional Dreamforce demos, with the GTM Studio value proposition
resonating strongly across strategic accounts including Chargebee (AI consumption pricing
targeting), Freshworks (HubSpot workflow integration interest), Cisco (conversation intelligence
feedback), S&P Global (CRM hygiene + Studio potential), and Xactly (Clay user impressed by
UX simplicity). The AI Emailer integration shifted to an in-house agent solution (replacing the
problematic external integration) and hit staging this week, targeting Monday production
release. Design resources are now assigned for the data agent migration, inline chat
configuration display, and Studio Chat redesign--prioritized in that order to unify the agentic
experience and improve transparency/control. For next week's focus: November release
readiness to ensure Onboarding and SCs are subject matter experts, plus defining Studio's
December 31st north star.

Plays: Mohan completed high-level PRD and design review for DoubleO M2, identifying
follow-up areas for fine-tuning: AI credit handling, workbook refresh impact on workflows, and
the experience for pulling workflow outputs back into workbooks. On Copilot activation, he
closed several loose ends for a better MVP experience--temporary AI email solution, workbook
refresh impact to route behavior, minor UX enhancements, and demo environment preparation.
He also coordinated with dev and QA teams to kick off testing. A critical gap emerged: the
Copilot email activation experience isn't optimal yet (still requiring emails to be "drafted" rather
than direct integration), requiring an urgent better solution to enhance integration value. Neha
continued collaborating with the workflows team to finalize the supported triggers and actions
library, documenting the events currently supported and identifying gaps for the implementation
plan ahead.

ROI Analytics: Arun advanced ROI Memo to internal pre-prod release this week, enabling AMs
and CSMs to preview and provide feedback before customer rollout. The team finalized
embedded workbook analytics scope with leadership sign-off and continued self-serve analytics
enablement across 5-6 accounts. Brahm validated the GTM Data Model bridge solution with
Platform and CFA teams--Platform will backfill opportunity history data short-term. Prateek's
team committed to ETA delivery next week, after which CFA can establish the GA timeline.
Dominik reviewed Arun's workspace ROI analytics prototype with positive directional feedback
on the agentic integration approach. The main blocker for ROI GA remains the missing
opportunity history data that was available in legacy ZDP bigquery tables and low company ID
matching (2.59M rows with empty company IDs), both of which may underreport influenced
pipeline metrics.

Data Management: Corina iterated Data Health Scan requirements for V2 based on strong AM
feedback, incorporating enhanced benchmarking, before/after views, and noise filtering (e.g.,
excluding accounts with no activity or open opportunities in 12+ months). The team prioritized
10-15 high-value accounts with poor data health and upcoming renewals for targeted AM
outreach--TK Newman already secured a Randstad meeting using the scan, while Palo Alto
Networks scheduled a follow-up meeting post-VP review. Corina drafted a learning document
capturing V1 insights and AM feedback to inform M3 requirements for bringing Data Health
Scan into GTM Studios. On Milestone 2, she completed Microsoft Dynamics and HubSpot
feature testing in RingLead and prepared enablement materials for November release. Ash
finalized MVP requirements for AI Data Management core patterns, narrowing scope
significantly to accelerate delivery while maintaining clear post-MVP roadmap. Detailed
requirements for normalize and segment are complete, with dedupe finishing by Monday. The
team established JIRA structure and kicked off daily working sessions with Engineering to drive
momentum, though design work was delayed due to designer reassignments--officially starting
Monday. A critical risk emerged around GTM Fields integration: Engineering is evaluating
whether configuration reuse across CRM, MAP, Workbooks, and other systems is feasible, as
current limitations may require unique configurations per task (CRM mapping only), potentially
delaying Workbook integration in MVP.

GTM Config: Tingting's team completed six internal user feedback sessions with OMs and TIMs
on the zero-config flow, with unmoderated UserTesting sessions launching Thursday to gather
additional UX validation. However, early feedback revealed significant bias--OMs/TIMs
anchored on existing Admin Portal onboarding flows rather than evaluating GTM Config as a
standalone context/control layer. The team identified a critical gap: the proposed experience
doesn't scale across all industries (e.g., a seller focused only on Ads shouldn't be asked about
their company's full Radio/Podcast/Events offerings). On the development side, BE/FE teams
finalized available APIs for the November V1 release and scoped the agent's initial
capabilities--it will guide users but won't support config editing via chat in the first version.
Tingting is expanding customer outreach beyond the initial 11 contacts, partnering with the
Research team to secure 5+ validation sessions. The main challenge remains getting strong
positive reception from AMs and CSMs for customer feedback sessions--the team will rethink
the outreach strategy next week to improve engagement.

Strategic Challenges

Customer validation and designer resourcing creating friction across multiple initiatives.
Despite expressing interest, AMs and CSMs haven't provided strong positive reception for GTM
Config zero-config customer feedback sessions--Tingting needs to rethink the customer
outreach strategy when she returns next week. Separately, Tanvi's find contacts enhancement
work hit a snag when her assigned designer was pulled mid-project, requiring re-coordination
with Megan. These resourcing and stakeholder engagement challenges aren't blocking
immediate progress but create velocity drag that compounds across the team's parallel
workstreams. Clear paths forward exist (Tingting's revised validation approach, Megan's
designer reassignment), but the pattern suggests we need tighter upfront commitment and
resource allocation discipline.

Platform dependencies on GTM Data Model still gating critical milestones despite
alignment. While Brahm's team achieved alignment with Platform on the opportunity history
approach, ETA on delivery is will come in next week--until those timelines arrive, ROI GA dates
remain undefined. Similarly, Ash's AI Data Management work identified potential risks with GTM
Fields integration, where Engineering foresees challenges enabling configuration reuse across
CRM, MAP, Workbooks, and other systems. Current limitations may force unique configurations
per task (CRM mapping only), restricting scalability and potentially delaying Workbook
integration in the MVP. Both threads share a common pattern: strategic alignment achieved, but
execution timelines and technical feasibility still uncertain. The teams are pursuing right
mitigation paths (Ash's translation layer exploration, Arun's Platform follow-up).

Signal discoverability and user education gaps creating adoption friction in Early
Access. Tanvi's customer calls revealed users instinctively select recommended signals (clear
labeling + easy checkboxes), only to consistently get zero results due to invisible relevance
filtering that even internal teams don't fully understand. Separately, users are attempting
sophisticated AI Data Agent use cases (full sheet analysis, priority ranking, similarity analysis,
even Salesforce export requests) that exceed current capabilities, creating expectation
mismatches. The broader pattern: customers find signals variations across product areas (web
visit signals, ALI vs regular intent, recommended vs raw signals) confusing and inconsistent,
raising "is this working?" concerns. While Tanvi's partnering with Srivatsa on KC articles and
enablement as immediate fixes, the underlying issue is deeper--we're surfacing powerful
capabilities without sufficient guardrails, education, or consistency across the platform. This is
coachable rather than product-breaking, but it's consuming support capacity and creating friction
in the critical Early Access cohort ahead of GA.

Strategic Insights

Key Learnings & Discoveries

Early paying customer validates signal-based workbooks as immediate monetization
path. Lou's customer specifically sought Website Buyer ID signal activation, which only
signal-based workbooks can deliver at scale in a list-building context. This validates the core
use case hypothesis before the November 3rd launch and demonstrates clear
willingness-to-pay for advanced signal capabilities. The win also confirms that our technical
execution on signal-based workbooks (despite the requirement complexity Tanvi's been
navigating) is solving real customer pain points. This early revenue signal should inform
go-to-market prioritization and sales enablement emphasis.
Dreamforce validated Studio's competitive positioning but surfaced critical activation
gap. Jagan's demos resonated exceptionally well with strategic accounts, particularly the
conversation intelligence capability that Cisco highlighted as a longstanding pain point.
However, multiple customers (Chargebee, Freshworks) expressed interest in direct
CRM/workflow integration (HubSpot, consumption pricing models), reinforcing that our activation
story is incomplete. The positive reception proves the audience-building value prop works; the
integration questions prove customers immediately think downstream about "how do I activate
this?" This aligns with Sneh's observation that customers struggle with "how do I get talking
points and next best actions to sellers?"--the Workspace activation integration in November
becomes even more critical given this feedback.

Data Health Scan creating immediate sales traction despite POC status. TK Newman's
Randstad meeting and Palo Alto Networks' VP follow-up prove the Data Health Scan concept
resonates with high-value accounts even in rough POC form. The team prioritized 10-15
accounts with bad data health, upcoming renewals, and high upsell potential (some sub-$100K
ACV with $200K+ upsell opportunity due to record volume). The #1 AM question--"how did you
get this data?"--revealed a gap in proactive trust-building that Corina's addressing in the V2
narrative by leading with CRM Advanced Sync value (ROI, Target Accounts, Health Scan).
However, the broader learning is that data quality storytelling creates urgency even without
perfect product execution. This suggests accelerating the analytics work with Spencer's team
and design iteration with Yoav could unlock significant near-term revenue rather than waiting for
M3 productization.

Cross-Team Dependencies

Platform engineering alignment on GTM Data Model critical for multiple Q4 deliverables.
CFA team aligned with Platform team on opportunity history backfill to help unblock ROI GA ­
actual timeline delivery is pending and Platform team will come back next week with ETAs.
Separately, Ash's AI Data Management work depends on GTM Fields integration feasibility,
which Engineering is still evaluating i.e. strategic alignment exists, but execution timelines and
technical constraints remain to be evaluated.

Design and research resourcing becoming a velocity constraint across initiatives.
Tingting needs expanded customer validation support beyond her initial 11 contacts, Tanvi
requires quick designer reassignment after mid-project changes, and Jagan's agentic
experience improvements are sequenced around design resource availability (data agent
migration first, configuration display second, Studio Chat redesign third). While none of these
are hard blockers, the pattern suggests design capacity is stretched across too many parallel
workstreams. Recommended action: Megan's team and Sneh align on design resource
allocation priorities for November push, potentially consolidating efforts or staggering less critical
work to H1.

Looking Ahead
November 3rd launch readiness is our overriding priority. Sneh's enablement content drops
this week for team review, covering platform overview, Studio-specific selling, and objection
handling. The joint Studio-Workspace launch requires tight coordination across sales, SCs, and
customer success--any gaps in positioning or demo capabilities will directly impact our ability to
hit the 100-customer-by-EOY target. Jagan's focus on release readiness materials and SC
subject matter expertise, combined with Mohan's Copilot activation timeline push, ensures we're
not just shipping product but equipping teams to sell and support it effectively.

Platform ETA delivery next week determines ROI GA timeline and downstream planning.
Pratik's team committed to providing short-term (backfill) and long-term (CRM-native) timeline
estimates for opportunity history data next week. Once those arrive, CFA can lock the GA date
and the team can sequence downstream work (multi-currency support, export capabilities,
workspace analytics integration).

Customer validation and design iteration critical for Data Management and Config
initiatives. Tingting returns next week to rethink customer research strategy after lukewarm
AM/CSM response, while Corina's Data Health Scan V2 incorporates strong AM feedback to
support the 10-15 prioritized account outreach. These aren't just product polish
activities--they're validation gates for multi-quarter investments in Data Management (M3-M5)
and GTM Config (UI for foundational context layer). Success here means confident engineering
commitments and clear revenue projections.

Source: GTM Studio Operating Framework entries and team meeting transcripts from October
13-17, 2025
