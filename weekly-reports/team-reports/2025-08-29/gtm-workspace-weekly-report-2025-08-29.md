---
id: weekly-copilot-2025-35
title: "GTM Workspace (Copilot) Weekly Report - August 29, 2025"
type: weekly-report
status: approved
team: copilot
owner:
created: 2025-08-29
updated: 2026-01-06
week_ending: 2025-08-29
reporting_period: "August 25-29, 2025"
tags: ["weekly-report", "Q32025"]
---

SalesOS/Copilot Executive Roundup -
[August 25th - August 28th, 2025]

Executive Summary

The team successfully launched Intent Topic AI Recommendation to production while
uncovering critical revenue leakage worth potentially $1M+ annually from uncontrolled custom
topics. Harinath Krishnamoorthy identified multiple production issues in the recommendation
system and secured buy-in from Carlos (GTM Strategy) to prioritize automated deprovisioning
fixes. Meanwhile, profiles for GTMC are progressing strongly with Ant Cuomo and new designer
Lindsay Bongo creating a clean-slate approach focused on bird's-eye intelligence views, while
mobile Chat V2 prototyping begins in September to surface gaps and dependencies early.

This Week's Progress

Key Momentum Areas

Intent Recommendation Launch Reveals System Gaps: Harinath Krishnamoorthy completed
a comprehensive analysis of Intent Topic AI recommendations across enterprise customers
(Brex, Monday.com, Twilio, Freshworks, JFrog, Neo4j), discovering the feature achieved
30-60% relevancy while uncovering three critical production bugs that had bypassed QA testing.
The investigation revealed unauthorized platform runs, incorrect scheduling frequencies, and
data discrepancies that were immediately escalated as P1 issues to engineering and data
science teams.

GTMC Profiles Architecture Breakthrough: Ant Cuomo partnered with designer Lindsay
Bongo to create a foundational design approach that prioritizes information architecture and
bird's-eye intelligence over traditional module-heavy interfaces. The team established "follow
contact" functionality that integrates with S2A engine for breaking alerts, creating a competitive
advantage in contact-level signals that can automatically generate targeted contact views for
users.

Mobile V2 Agentic Explorations: The mobile team secured dedicated September sprint
capacity to prototype Chat V2 integration, specifically identifying gaps and dependencies in the
agentic platform for native mobile experiences. Ant Cuomo structured this as a two-sprint
exploration to build field sales-specific agents while creating a comprehensive dependency list
for Lars's team, positioning mobile as a critical early adopter rather than an afterthought.

Goals & Progress
Intent Platform Stabilization: Production quality issues were systematically addressed with
three P1 tickets filed covering unauthorized tenant runs, daily vs. weekly scheduling conflicts,
and data pipeline discrepancies. Engineering and data science teams acknowledged these
issues with fixes scheduled for early next week, while a comprehensive 16-section support
document was created to prevent downstream customer escalations and enable smoother
adoption.

Revenue Leak Mitigation: Custom topic deprovisioning automation gained executive support
from Carlos (GTM Strategy team), who confirmed the potential $1M+ annual revenue leak and
committed to prioritizing the initiative. Harinath Krishnamoorthy is working with Josh from the
custom topic team and Salesforce engineers to quantify exact revenue impact through data
analysis, building a compelling case for immediate implementation of package-level cluster
limits.

Copilot V2 Onboarding Foundation: Adam Severance progressed the GTMC onboarding prod
review to 70% completion, focusing on persona-based homepages and first-time user
experience design. However, design resource constraints required strategic prioritization of
emailer functionality over advanced search capabilities for the November timeline, creating a
more focused but potentially limited initial V2 experience.

Strategic Challenges

Design Resource Bottleneck: Multiple teams are converging on GTMC development
simultaneously, creating significant design capacity constraints that forced difficult prioritization
decisions. Adam Severance encountered multiple handoffs between Megan, Whitney, and
Katya before securing design support, while the team had to deprioritize advanced search V2
development to focus resources on higher-impact emailer functionality. This bottleneck
threatens November delivery timelines and may require executive intervention to reallocate
design resources or adjust scope expectations.

Advanced Search Migration Complexity Requires Strategic Decision: David Goulden's
priority accounts initiative faces uncertainty around the advanced search migration to GTM data
model, with multiple engineering teams still investigating feasibility and backward compatibility
requirements. The migration affects existing saved searches, CRM filters, and downstream
services, while customer renewal success depends on minimizing disruption to current Sales
OS workflows. This requires immediate architectural decisions to prevent feature development
paralysis.

Production Quality Gaps Exposing Testing Inadequacies: The Intent recommendation
launch revealed systematic QA failures that allowed critical production issues to reach
customers, including unauthorized platform runs and incorrect scheduling logic. While these
specific issues are being addressed, the root cause analysis points to broader testing protocol
gaps that could impact future feature rollouts and customer trust, requiring process
improvements beyond the immediate P1 fixes.
Strategic Insights

Key Learnings & Discoveries

Customer-First Analysis Reveals Hidden System Issues: Harinath Krishnamoorthy's
deep-dive analysis of enterprise customer recommendation quality exposed production
problems that weren't caught during development testing, demonstrating the value of real
customer data validation over synthetic testing scenarios. The discovery process required
piecing together insights from scattered Snowflake data and direct production queries, revealing
that current analytics tooling isn't optimized for rapid customer issue diagnosis during feature
rollouts.

Mobile-First Agent Design Opens New Market Opportunities: Ant Cuomo identified that 30%
of the market represents field/territory sales requiring mobile-first experiences, with specific use
cases like daily summary agents and location-based contact mapping that differentiate from
desktop-centric workflows. The September sprint approach of building native mobile agents
while documenting platform gaps creates a foundation for capturing this market segment that
competitors may overlook.

Template-Based Configuration Consistently Fails Enterprise Adoption: Victor Oliveros
reinforced the pattern that admin-configured templates fail in enterprise software, citing decades
of Salesforce experience where admins lack UX design skills and bandwidth for complex setup
tasks. This insight validates the agentic approach for both company profiles and territory setup,
suggesting that AI-driven configuration could become a key competitive differentiator against
traditional enterprise software approaches.

Cross-Team Dependencies

Our work with Engineering teams on Intent platform stability continues to be critical for
maintaining customer trust during the recommendation feature rollout. Three P1 issues are
currently being addressed by both engineering and data science teams, with production fixes
expected early next week and systematic QA process improvements needed to prevent similar
issues in future releases.

The mobile team's September sprint on Chat V2 integration will provide essential feedback to
Lars and the agentic platform team about native mobile requirements. Early identification of
SDK needs, artifact limitations, and performance requirements will inform platform development
priorities and prevent mobile from becoming a reactive afterthought in the GTMC rollout
timeline.

Looking Ahead

Platform Stability and Process Improvement Focus: Next week prioritizes completing the
Intent recommendation production fixes while implementing systematic QA improvements to
prevent similar issues. The team will finalize revenue leak analysis with Carlos and begin
technical implementation planning for custom topic control mechanisms, turning a discovered
problem into a revenue protection opportunity.

Design Capacity Optimization and Mobile Prototyping: With GTMC profiles entering design
review and mobile prototyping beginning, the focus shifts to optimizing design resource
allocation across competing priorities while ensuring the mobile team's September sprint
generates actionable platform requirements. Adam Severance will complete the GTMC
onboarding prod review template while navigating the advanced search vs. emailer prioritization
decisions that impact November delivery scope.

The team demonstrated strong problem-solving capabilities this week, turning production issues
into improvement opportunities while maintaining forward momentum on strategic initiatives.
The combination of immediate tactical fixes and longer-term architectural planning positions us
well for sustainable growth while protecting existing revenue streams.

Source: Team SalesOS/Copilot Operating Framework entries from [August 25th - August 28th
2025]
