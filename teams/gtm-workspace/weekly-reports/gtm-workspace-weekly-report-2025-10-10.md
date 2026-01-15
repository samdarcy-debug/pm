---
id: weekly-copilot-2025-41
title: "GTM Workspace (Copilot) Weekly Report - October 10, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-10-10
updated: 2026-01-06
week_ending: 2025-10-10
reporting_period: "October 6-10, 2025"
tags: ["weekly-report", "Q42025"]
---

SalesOS/Copilot Executive Roundup -
[Oct. 6, 2025 - October 9, 2025]

Executive Summary

Copilot Workspace achieved a major milestone this week with internal Frontline GTM team
launch, revealing valuable user feedback that will shape GA readiness. The team is addressing
a key disconnect between chat and views experiences, with Adam Severance leading
foundational improvements to views, chat, and first-time user experience--all design complete
with scoping targeted for November 3 release. Gabe Pirela delivered the draft Copilot/Chorus
convergence roadmap targeting February customer migrations, establishing a strategic
foundation for reducing surface area through agents and artifacts rather than brick-by-brick
rebuilding. On ZoomInfo Intent, Harinath Krishnamoorthy completed a functional Cline prototype
for Persona-Based Intent in Copilot, ready for Pre-Sales and PM validation sessions that will
enable engineering handoff. For Admin Zero Experience, David Goulden finalized enablement
packs for Admin-Defined Territories GA (now targeting mid-November), with four additional beta
customers onboarded and workflow robustness solutions implemented.

This Week's Progress

Key Momentum Areas

Copilot Workspace Internal Launch and User Feedback: The Frontline GTM team began
using Workspace this week, generating immediate actionable feedback through one-off
sessions with Ant Cuomo. The primary discovery reveals users struggle to understand the
relationship between chat and views--they don't recognize what's possible with the tool or how
table artifacts from chat could integrate with views. This early feedback from actual go-to-market
users is accelerating product refinement ahead of GA, with the team documenting gaps in user
experience that will inform November release priorities.

ZoomInfo Intent Persona-Based Prototype Validation: Harinath Krishnamoorthy delivered a
working Cline prototype demonstrating persona-based Intent topic configuration in Copilot,
compressing the traditional PRD-to-prototype timeline from six weeks to one week using
AI-powered development tools. The prototype brings to life the hypothesis that role-based
default configurations will increase users moving beyond defaults from 15% to 35%. Pre-Sales
validation sessions scheduled this week will gather feedback on customer-facing usability and
implementation feasibility before engineering handoff, ensuring the team solves the right
problem before costly development begins.
Admin Zero Experience Territories GA Preparation: David Goulden completed enablement
pack creation for Admin-Defined Territories GA release, implementing workflow robustness
solutions that automatically reassign workflows when user permissions change or users leave
the organization. The team added four additional beta customers eager to access the feature
before GA, while also addressing retention challenges through root cause analysis--revealing
that while initial onboarding engagement is strong, sustained adoption requires both feature
improvements and customer change management support.

Goals & Progress

Copilot Workspace: Adam Severance made significant progress on foundational views and
chat improvements driven by persistent first-time user experience problems. The team identified
two critical friction points: users get confused when creating views or configuring fields/filters,
and after sending one chat message, users become lost and can't find past chats or artifacts.
Adam built comprehensive requirements in Replit over the weekend, secured directional
alignment from Sean Walter and Megan Cartlidge, and is moving forward with design complete
and LOE scoping targeted for November 3 release. The improvements will surface past artifacts
at the same level as chat threads (or higher), introduce a table format allowing users to search
artifacts by company with logos visible, and fundamentally improve how first-time users
understand view functionality.

ZoomInfo Intent: Harinath Krishnamoorthy advanced three parallel Intent initiatives this week.
He completed a comparative analysis document on Multi-AFS configuration approaches
(account-level vs. user-level), awaiting clear problem definition from the Data Science team led
by Robyn before finalizing recommendations. He aligned with Tanvi from GTM Studio on Intent
signal integration for Workbook Creation and Enrichment workflows, establishing tentative
November implementation timeline. The persona-based Intent prototype is now ready for
stakeholder validation, with Pre-Sales and PM review sessions enabling feedback before
platform team handoff. The fourth planned initiative--comprehensive quality analysis of Data
Science Intent Recommendation improvements across SMB, MidMarket, and Enterprise
segments--did not progress this week due to competing priorities.

Admin Zero Experience: David Goulden pushed Admin-Defined Territories GA to
mid-November (from October 20) to accommodate UI refinements for admin experience, since
workbooks activation isn't blocking the release. The team implemented workflow robustness
scripting that finds the next best user (based on admin status, workflow permissions, and signal
visibility entitlements) when workflow owners lose permissions or leave the organization. Beta
rollout continues with strong initial engagement but concerning retention patterns requiring
further investigation into whether issues stem from feature gaps, customer change
management, or signal quality. On Priority Accounts based on GTM Data Model, testing of new
APIs continues with the goal of making target accounts, whitespace with signals, and
activity-based suggestions available as out-of-the-box lists in Workspace, though data
harmonization across ZDP, BigQuery, and legacy Solar remains a challenge with December
proof-of-concept timeline pushing actual release to Q1 2026.
Additional Initiatives: Dylan Halladay progressed significantly on slides artifact planning and
requirements, completing a strategic document framing feature importance and development
sequencing. The team explored Google Slides API vs. PowerPoint approaches, with major
trade-offs requiring executive decision. Regardless of path chosen, a critical dependency
emerged: integrating and authenticating users to Google Drive and Google Workspaces to
enable adding presentations to user drives--engineering called this out of scope for first
milestone but Dylan argues Workspace fundamentally needs this capability for document
artifacts and unified go-to-market hub positioning. Ant Cuomo kicked off company profiles
development with focus on phasing and dependencies, coordinating with Andres (per Sarah
Heritage, Victor Oliveros, and Dominik Facher's request) to march toward GTM Data Model as
the source of truth and avoid repeating Workspace tech debt from chapter one. The team is
identifying data source gaps across prompt service, agents, and legacy APIs. On mobile, Ant
progressed toward November 3 internal beta with concepts for January MVP complete,
requiring partnership with Derek and the 00 team on feed support. Gabe Pirela supported
multiple Q4 Chorus renewal meetings this week while finalizing the Copilot/Chorus convergence
roadmap with updates based on Victor's feedback and Sarah Heritage's requirements.

Strategic Challenges

Copilot Workspace Chat and Views Disconnection: Users fundamentally don't understand
the relationship between chat and views experiences in Workspace, creating a barrier to feature
adoption. The immediate manifestation is users cannot add table artifacts generated in chat to
views, leaving them with fragmented data across the product. Adam Severance spent the
weekend building comprehensive requirements to address this through foundational
improvements that surface artifacts at the same level as threads, enable searching by company
with logo visibility, and simplify view creation. While the path forward is clear with design
complete and scoping underway for November 3, this represents a make-or-break moment for
GA adoption since the Frontline GTM team using Workspace this week will inform whether
go-to-market leaders confidently sell the product at Dreamforce and post-11.3 launch.

ZoomInfo Intent Multi-AFS Configuration Clarity: Harinath Krishnamoorthy created a
comprehensive pros and cons analysis comparing account-level versus user-level AFS
configuration approaches but encountered difficulty obtaining clear problem definition from the
Data Science team. Multiple conversations with Robyn yielded shifting
explanations--sometimes citing model-level improvements, sometimes explainability
challenges, sometimes configurability concerns--preventing confident architectural
decision-making. The team is waiting for Robyn to articulate the exact problem being solved
before proceeding, as this configuration choice will impact how thousands of customers interact
with Multi-AFS capabilities and could require costly rework if decided incorrectly. Harinath will
review the comparative analysis document with Victor Oliveros before surfacing final
recommendations to the Data Science team once problem clarity emerges.

Admin Zero Experience Workbooks Demo Path OAuth Blocker: Ant Cuomo identified a
technical blocker for the critical workbooks-to-workspace demo path needed for October launch
demonstrations. The intended flow--logging into Workspace production, logging out of
Salesforce production, and logging into Salesforce demo instance--currently fails with OAuth
errors because Workspace hasn't been configured as an app in the Salesforce demo
environment. Kristen initiated a thread last week with a Salesforce admin who appeared
deactivated this morning, requiring immediate escalation up the chain. Ant needs validation that
this works today or tomorrow at latest, as this demo path is fundamental for October
demonstrations. The resolution path is clear (configure Workspace in Salesforce demo
environment) but requires urgent cross-functional coordination with Salesforce administrators
who may lack bandwidth or context on the priority.

Strategic Insights

Key Learnings & Discoveries

User Mental Model Mismatch on Context Persistence: Adam Severance discovered through
user interviews this week that many users believe opening a chat thread over a specific profile
maintains ongoing context and superior information about that company compared to general
chat queries. This reveals a fundamental misunderstanding of how Workspace chat
works--users expect spatial context (where they opened chat) to create persistent
conversational context, similar to how profile pages maintain company-specific information. This
insight suggests the product needs clearer communication about when and how context gets
passed to chat, potentially through visual indicators or explicit context confirmation when users
open chat from specific locations. The finding also reinforces the importance of ensuring chat
actually does receive and utilize context from where it's invoked, making the implicit user
expectation match actual product behavior.

Copilot Pulse as Differentiated Value Proposition: Victor Oliveros shared that the Copilot
Pulse concept (ChatGPT Pulse adapted for go-to-market) received significant attention during
the product offsite, with executives recognizing organic value for AMs, managers, and leaders
receiving weekly updates. Unlike consumer ChatGPT Pulse which lacks clear use cases, the
go-to-market application addresses a fundamental need for account and pipeline intelligence
delivered proactively. The first phase targets December delivery, allowing users to prompt and
create pulses in Workspace (as artifacts or from prompts) and receive them on
mobile--establishing single-player value before expanding to RevOps-created pulses pushed
from GTM Studio plays. This insight reinforces that the same AI capabilities packaged for
business contexts can unlock differentiated value that consumer applications cannot, and that
mobile may find its killer use case through proactive intelligence delivery rather than trying to
replicate desktop functionality.

Early Prototype Validation Prevents Costly Development Rework: Harinath
Krishnamoorthy's experience with persona-based Intent prototyping reinforced the power of
rapid AI-assisted development to compress validation timelines. By using Cline to build a
functional demonstration in one week (versus the traditional six-week PRD-to-prototype cycle),
the team can gather Pre-Sales and PM feedback before engineering handoff--ensuring they
solve the right problem before significant development investment. This pattern of "build to
learn" rather than "document to build" is proving especially valuable for novel AI features where
user expectations and product capabilities need alignment through tangible experience rather
than written specifications. The broader implication is that product teams should default to rapid
prototyping for new experiences, reserving comprehensive documentation for features where
requirements are well-understood and unlikely to change based on user interaction.

Cross-Team Dependencies

Our work with the GTM Data Model team on company and contact profiles continues to be
essential for avoiding tech debt accumulation. Ant Cuomo is coordinating with Andres this week
to ensure profiles are built on the GTM Data Model as the source of truth rather than repeating
the pattern from Workspace chapter one where the team accumulated technical debt through
expedient but unsustainable architectural decisions. The conversation centers on identifying
gaps in timing and data source availability across prompt service, agents, and legacy APIs. This
dependency is particularly acute because company profiles will reach hundreds of thousands of
users, making it a high-visibility test case for whether the GTM Data Model can support
production-scale product experiences, and the team needs clear commitment on what data will
be available when to make informed phasing decisions.

The Salesforce administration team dependency for the workbooks-to-workspace demo path
requires immediate resolution. Ant Cuomo escalated this morning after discovering the west
coast Salesforce admin who Kristen contacted last week appears deactivated, blocking
validation of the critical demo flow needed for October launch. The team needs Workspace
configured as an app in the Salesforce demo environment to enable OAuth authentication when
users switch from production to demo instances. This is diplomatically a coordination and
prioritization challenge rather than a technical barrier, requiring executive air cover to ensure
Salesforce administrators understand the urgency and business impact of enabling this
configuration immediately.

Looking Ahead

The team's primary focus next week centers on Dreamforce preparation and Workspace
production readiness, with 56 executive meetings booked (targeting 100) at the W Hotel Lounge
where Workspace will be demonstrated as the primary product. Go-to-market leaders including
Tuna, Breyers, and AR are training to demo Workspace themselves this week--if they have a
positive experience and customers respond well at Dreamforce, that evidence will determine
whether leadership fully backs the product post-11.3 launch. This makes production testing and
cherry-picking what gets pushed versus held back absolutely critical.

On Copilot Workspace, Adam Severance will finalize design and LOE scoping for foundational
views and chat improvements, sharing screen recordings and documentation with Victor
Oliveros to assess A-B testability and tracking from Phoebe's analytics perspective. Ant Cuomo
must resolve the Salesforce demo environment OAuth blocker immediately to validate the
workbooks-to-workspace demo path, while continuing profiles development with clear data
source identification and Recommendation Agent (formerly NBA) iteration focused on
demonstrating value with both complete and imperfect context. Dylan Halladay will complete the
slides artifact requirements document and make progress on the ReachOut Gmail integration
POC, enabling the team to summarize or propose email drafts when users open Gmail threads.
For ZoomInfo Intent, Harinath Krishnamoorthy will conduct Pre-Sales and PM validation
sessions on the persona-based Intent prototype, review the Multi-AFS configuration analysis
with Victor Oliveros once the Data Science team provides clear problem definition, and work
with Tanvi on GTM Studio Intent filter requirements. David Goulden will focus on Priority
Accounts API testing and finalizing admin UI refinements for Admin-Defined Territories
mid-November GA. The team demonstrated aggressive positioning at the product offsite with a
roadmap targeting AE and AM market capture this year, sales-adjacent personas by June, and
initial CRM customers by end of next year--now the execution against these commitments
begins with Dreamforce as the first major external validation point.

Source: Team SalesOS/Copilot Operating Framework entries from [Oct. 6, 2025 - Oct. 9, 2025]
