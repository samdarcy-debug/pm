---
id: weekly-product-ops-2025-47
title: "Product Ops Weekly Report - November 21, 2025"
type: weekly-report
status: approved
team: product-ops
owner:
created: 2025-11-21
updated: 2026-01-06
week_ending: 2025-11-21
reporting_period: "November 17-21, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Product Ops Executive Roundup - November 17-21, 2025**

## **Executive Summary**

The team broke through on Voice of Customer data quality, finally
isolating which calls actually pitched Studio and Workspace versus
general conversation mentions. Ken Elwell and Sam Darcy completed solid
VOC analysis reports and datasets, though the final mile of knowing what
presentations or demos were shown will be the breakthrough via Chorus,
to get it working at scale for our customers. Kristin Gandini and Daniel
Kong successfully rolled out the automated weekly release workflow to
both PMs and enablement stakeholders, with the first production cycle
starting next week for the December 2nd release. The roadmap ahead
centers on activating this newly available data in two directions:
downstream for enablement and customers, upstream for PMs to impact
product direction.

## **This Week\'s Progress**

### **Key Momentum Areas**

**VOC Data Quality Breakthrough**: Ken Elwell and Sam Darcy completed
solid VOC analysis, successfully isolating calls where Studio and
Workspace were actually pitched rather than just mentioned in passing.
Ken finalized updated reports while Sam delivered the final CSV dataset
and workflow for GTM Studio pitch analysis, solving relationship mapping
versus keyword filtering challenges. The breakthrough came from querying
summarized data with chapter-by-chapter breakdowns rather than meeting
summaries. Product marketing now has visibility into customer reactions
during actual pitches, though the final mile of knowing which
presentations or demos were shown. Syncing with Gabe Pirela to share
learnings for what we build for customers.

**Automated Release Workflow Launch**: Kristin Gandini and Daniel Kong
rolled out the rapid release system to all impacted stakeholders after
Tuesday\'s enablement session and incorporated immediate feedback
improvements. The streamlined agent now generates release notes, creates
feature deep dive documents, and auto-populates LRT tickets in a single
workflow, eliminating context switching for PMs. Using AI release tech
from Dan DeSwaan\'s Engineering Productivity team, the system transforms
code deployment data into downstream-ready materials, with the first
live production cycle beginning Monday for Workspace and Studio.

### **Goals & Progress**

**Monthly Release Process Maturation**: The team demonstrated continued
execution strength with the monthly content release (MCR) proceeding
smoothly despite tight holiday timing. Ken Elwell completed all MCR
materials, marking sustained process improvements that reduce
last-minute complications. However, attendance at the release session
was roughly half expected numbers, reflecting difficult year-end
scheduling rather than process issues.

**Automated Release Expansion Planning**: The December 2nd release
serves as the first real-world test for weekly cadence sustainability,
with PMs now responsible for gathering release information through the
automated workflow. The system will surface gaps in the first 2-3
cycles, particularly around feature flag discipline and staging data
integration. Kristin Gandini is already exploring expansion
opportunities including longer lead times through staging deployments,
roadmap visualization for downstream teams, and tighter feedback loops.

**Cross-Team SDLC Understanding**: Team members are developing
increasingly interchangeable skill sets across the full software
development lifecycle, enabling better coverage and collaboration. Caleb
Munson continues workshop planning with Dominik focusing the two-day
session on teaching teams to build and think in plays rather than
comprehensive planning coverage. The workshop agenda shifted
substantially to emphasize play construction methodology. Lars Veto
identified a potential Salesforce MCP connection that could resolve
outstanding SFDC data access questions for ongoing analysis work.

### **Strategic Challenges**

**Finding Precise Call Intelligence Remains Hard**: Despite the
breakthrough on Studio and Workspace pitches, extracting exactly what
you need from transcript data continues to be extremely difficult. The
team can find roughly relevant calls but achieving precision requires
iteration and refinement. This challenge represents the biggest unlock
for Studio and Workspace success or failure, as the ability to activate
conversation intelligence directly impacts both products\' trajectories.
The team needs to connect with Gabe Pirella about Chorus improvements
that could close the final mile gap.

**GTM Studio Technical Instabilities**: GTM Studio continues
experiencing issues including blank row data population and account
linking crashes that disrupt workflow reliability. The Studio team is
aware but these technical inconsistencies create friction during
critical analysis work. ZoomInfo\'s release notes page remains buggy and
non-functional, blocking certain integration workflows.

**Data Activation Strategy Undefined**: With VOC data now available and
release systems operational, the team faces the challenge of determining
how to activate these insights. Two activation paths need definition:
downstream toward enablement teams and customers, and upstream toward
PMs to influence roadmaps. The product insights reports Kendall shared
show clear patterns in customer thinking during pitches that should
impact product direction, but the activation mechanisms remain unclear.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Chapter Summaries Trump Meeting Summaries**: The most significant
discovery this week was that querying chapter-by-chapter summarized data
dramatically outperforms meeting summary searches for finding specific
conversation intelligence. This insight fundamentally changes the
approach to call analysis and explains why previous attempts at
precision struggled. Meeting summaries lack the granularity needed for
targeted intelligence extraction.

**ZI Chat Streamlines Jira Integration**: Daniel Kong discovered that ZI
Chat can create and update Jira tickets directly, significantly reducing
the context switching burden in LRT processes. This capability removes
administrative lift for work already being completed and tightens the
connection between release detection and ticket management.

**Engineering Productivity Tech Enables Weekly Cadence**: The AI release
technology from Dan DeSwaan and Shirhen\'s team proved comprehensive
enough to support weekly or bi-weekly releases rather than monthly
cycles. The system captures deployment data with sufficient detail that,
despite some assumptions about missed items based on dates and keywords,
it provides a solid foundation for scaling automated releases to
additional products in Q1.

### **Cross-Team Dependencies**

Product marketing collaboration on activating customer insights is
advancing well, with leadership recognizing the value of real-time pitch
intelligence. The team needs to establish systematic approaches for
feeding VOC data upstream to PMs while the roadmap visibility piece lags
slightly behind customer feedback and release tracking capabilities.

Engineering Productivity\'s continued development of AI release tech
directly enables Product Ops expansion plans. The team needs alignment
with TPM and PM leads to make automated release workflows the standard
motion before scaling to additional products beyond Studio and
Workspace.

## **Looking Ahead**

Next week focuses on executing the first production release cycle while
determining how to systematically activate the customer intelligence and
release data now available.

**First Production Release Cycle**: Kristin Gandini drives PM adoption
of the automated workflow for the December 2nd release, the first true
test of weekly cadence sustainability. Expect 2-3 rounds to refine
feature flag discipline and identify process gaps. Daniel Kong is out of
office but the workflow is positioned to run independently Monday
morning.

**Data Activation Strategy Development**: Brett Jacobs will think
through systematic approaches for activating VOC and release data in
both directions - enablement and customer-facing downstream, and PM
roadmap input upstream. The insights from pitch analysis are sharp
enough to influence product direction if properly channeled to
decision-makers.

**VOC PM Interface Testing**: Sam Darcy will prioritize getting the VOC
front-end interface ready for Brett Jacobs and Chris to test next week,
barring major blockers. The goal is to enable PM self-service access to
customer intelligence, with potential rollout the following week if
testing goes smoothly. Sam will also work on automating the CSV creation
process for ongoing pitch analysis.

The team demonstrates operational maturity with systematic execution
replacing firefighting. The transition from building capabilities to
activating them represents the next phase, requiring strategic thinking
about how downstream teams consume product intelligence and how customer
feedback systematically influences roadmaps.

*Source: Team meeting transcript from November 17, 2025 and Friday
Reflection entries from November 17, 2025*
