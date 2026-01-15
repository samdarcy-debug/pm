---
id: weekly-intelligence-2025-26
title: "Intelligence Weekly Report - June 27, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-06-27
updated: 2026-01-06
week_ending: 2025-06-27
reporting_period: "June 23-27, 2025"
tags: ["weekly-report", "Q22025"]
---

# **Intelligence Team Executive Roundup - June 27, 2025**

## **Executive Summary**

The Intelligence team achieved a critical breakthrough this week with
GCP performance validation for the semantic data service, making data
ingestion dramatically faster. Platform adoption is surging following
our overview video release, with multiple PMs now actively building
agents. We\'ve identified HTML-based artifacts as a strong opportunity
to improve data visualization across the company. Support resources are
becoming stretched as platform usage scales rapidly, requiring immediate
attention.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Platform adoption surge**: Lars\'s overview video to the Products
channel catalyzed immediate interest, with multiple PMs scheduling
meetings this week and more lined up for next week. Teams are exploring
diverse use cases from engagement timelines to buyer journey maps,
validating both our platform strategy and its versatility for different
business needs.

**Semantic data service performance breakthrough**: Danny\'s GCP testing
for the ETL pipeline proved we can achieve the speed we need for data
ingestion, graph building, and embedding generation. Processing directly
within GCP is much faster than our previous approach, eliminating
Zscaler-induced latency penalties. This unlocks our ability to process
directly in production and automate the continuous pipeline.

**New agent development methodology proven**: Eric successfully created
our first new prospecting agent using public APIs as a workaround for
billing constraints. This demonstrates we can rapidly build new
capabilities while working within system limitations, providing a
template for future agent development using bulk credits for user
charging.

### **Goals & Progress**

**Agent Platform Development**: Copilot Chat completed pen testing with
security fixes identified. However, another security review will be
required after fixes are implemented, which is currently blocking
deployment of new Copilot Chat to production. Multiple teams including
Alex Tracy\'s are ready to implement our solutions on company and
profile pages.

**Sales Intelligence Products**: The inbox pipeline concept reached
high-fidelity mock stage with engineering review completed. However,
Sales Hub roadmap work was impacted by urgent State Pre-plays
requirements that absorbed significant time. Sales Hub beta testing
launches next week with progressive rollout planned to account
executives, account managers, and SDRs.

**Semantic Data Service Infrastructure**: GCP performance testing
completed successfully for the ETL pipeline, proving our architectural
approach. Direct production processing can now begin, eliminating the
tedious manual copy process. The automated continuous pipeline work
begins next week.

**Quality Assurance Framework**: Ryan created an agent to test agents,
establishing the foundation for automated testing. However, the full QA
framework remains incomplete due to support demands from newly
onboarding teams. The reporting and test suite components still need
implementation.

### **Strategic Challenges**

**Support capacity hitting limits as adoption accelerates**: Platform
interest is creating support demands that pull Ryan from critical QA
framework development. We lack onboarding materials, forcing manual
support for each new team. Without dedicated support resources or
self-service materials, we risk becoming a bottleneck to our own
platform\'s success.

**Competing priorities disrupting strategic work**: Sean\'s Sales Hub
progress was impacted by urgent State Pre-plays requirements. With Sales
Hub beta launching next week during July 4th holiday period, we face
resource constraints. This pattern of tactical urgencies interrupting
strategic initiatives continues to challenge our team\'s focus.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**HTML artifacts could improve data presentation**: Lars\'s meetings
with Brandon and Heather revealed strong potential for interactive HTML
artifacts. Use cases like engagement timelines, org charts, and buyer
journey maps could make complex data relationships more intuitive and
actionable. This represents an opportunity worth exploring further.

**Simultaneous strategic planning stretches resources**: Rowan noted
that planning for both services and initiatives simultaneously requires
more effort than anticipated. As Ryan experiences with support demands,
our operational maturity must match our platform maturity. The
complexity of managing overlapping initiatives while maintaining quality
is proving challenging.

### **Cross-Team Dependencies**

Our work with the **Workflows team** progresses well, with Lars building
a POC for workflow-agent integration. Mark Freil has documented platform
gaps they need to address. We still need to determine next week whether
workflows is fit for purpose for supporting plays.

The **Search team** collaboration remains important as we navigate
billing constraints through our public API approach. This enables
progress but may need revisiting as usage scales and feature
requirements expand.

**Alex Tracy\'s team** stands ready to implement our code on company and
profile pages, though page redesigns affect timing. This represents
immediate value delivery but requires coordination on implementation
timing.

## **Looking Ahead**

Next week\'s shortened holiday schedule focuses on critical priorities
that maintain momentum while accommodating team time off.

**Sales Hub beta launch** begins our first major user test with
progressive rollout to sales teams. Sean will iterate rapidly based on
feedback while managing the ongoing State Pre-plays requirements. This
validation point will guide our product development through Q3.

**Platform scaling foundations** become urgent as adoption accelerates.
Lars advances the workflows POC to determine fit for plays support while
Ryan pushes to complete the QA framework despite support demands. We
must also address the onboarding gap - Ryan\'s concept of an \"agent
that teaches agent building\" merits exploration as a scalable solution
to our support challenges.
