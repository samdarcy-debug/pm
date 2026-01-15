---
id: weekly-data-2025-36
title: "Data Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

Data Executive Roundup - [September 2nd
- September 4th, 2025]

Executive Summary

Dana Hurtig completed franchise validation work and delivered results to Igor and
Brandon, positioning us for the next phase of vertical data expansion. The team
successfully processed 450K EMEA companies through the DIP platform with ~80% creation
rate expected, while infusing 488.6K mobile phones and completing 650K bad data fixes.
Brandon Wilson made significant progress integrating GTM store data into semantic signals
architecture, and Rob Priore finalized opt-out process improvements that reduce abuse potential
while maintaining regulatory compliance.

This Week's Progress

Key Momentum Areas

Franchise validation milestone achieved with 85% successful verification rate, as Dana's
team completed the comprehensive review of franchise counts and delivered actionable results
to Igor and Brandon. This validation work directly supports our vertical data expansion strategy
and provides the foundation for continued franchise dataset development.

Major data quality improvements delivered through systematic cleanup efforts, with the
team completing 650K bad data fixes including duplicate mobile phone resolution, contact
cleanup, and director-level seniority corrections. Additionally, 488.6K mobile phones were
successfully infused from Orgimport, significantly expanding our contact coverage.

Semantic signals architecture advancement through GTM store integration, as Brandon
Wilson successfully pivoted from DRS to GTM store data access, resolving authentication
challenges and positioning the New Rep Summary, Won Deal in Similar Account, and Upcoming
Renewal signals for production deployment.

Goals & Progress

Data Quality & Coverage: Dana's team achieved 100% completion on franchise validation
while simultaneously executing a major EMEA company expansion, infusing 450K companies
via DIP platform with strong tier-one quality targeting. The team expects ~80% creation rate,
representing significant geographic expansion in key markets. These efforts directly support
customer coverage concerns in non-US geographies while establishing scalable processes for
future infusions.

Vertical Data Acceleration: Dow Jones delivered well-received leadership offsite presentation
on vertical datasets, securing continued executive alignment on the $10M H2 goal. The team
focused on FMA, Restaurants & Franchises, and Fleet dataset collateral development, with
strong emphasis on enabling reps for first-call discovery and reducing dependency on
specialized support. Multiple account targets were successfully rolled out across GTM teams.

Privacy & Compliance Infrastructure: Rob Priore completed design of streamlined opt-out
process that reduces abuse potential while maintaining CA and OR regulatory compliance. The
new flow eliminates complex validation steps for manual processing while building in feedback
loops for abuse monitoring. Additionally, automated CIPA compliance scanning via Privado tool
showed 100% accuracy across 38 tested customer websites.

Strategic Challenges

Agent development facing data access limitations, as Ethan Young identified that ZI Chat
needs Snowflake and BigQuery integration capabilities to fully enable the analysis workflow
agents the team requires. Current system limitations prevent direct querying access, which
constrains the automation potential for routine analysis tasks like debugging data issues and
exploration workflows. Engineering collaboration needed to prioritize database connectivity for
agentic platform.

GTM.ai launch timeline competing with immediate revenue opportunities, as Dow Jones
highlighted tension between getting the rebrand site live versus supporting urgent franchise and
restaurant dataset opportunities that directly impact the $10M goal. The team is managing
trade-offs between important foundational work and immediate pipeline creation, requiring clear
prioritization guidance.

Company 3.0 implementation requiring cross-functional coordination, as Ethan Young
outlined two critical requirements for domain lifecycle management and Tier D company
classification. These foundational changes will improve company definition consistency but
require alignment across Product, Engineering, and Data teams to ensure smooth
implementation without disrupting existing workflows.

Strategic Insights

Key Learnings & Discoveries

DIP platform proving highly effective for targeted geographic expansion, with the EMEA
company infusion demonstrating ~80% creation rate for tier-one quality companies. Dana's
team refined pre-validation processes to better estimate data quality upfront, discovering that
systematic quality checks before infusion significantly improve outcomes and reduce
post-processing cleanup.

Semantic signals architecture benefits from consolidated data access, as Brandon
Wilson's experience integrating GTM store revealed that centralizing data sources reduces
processing complexity, cost, and latency compared to parallel pipeline approaches. This insight
will inform future signal development and help avoid duplicative data processing across teams.

Customer compliance automation reaching production readiness, with Rob Priore's team
achieving 100% accuracy in automated CIPA scanning across customer websites. The Privado
tool eliminated need for manual console checking, representing significant operational efficiency
gain while improving compliance monitoring coverage and consistency.

Cross-Team Dependencies

Our work with Engineering teams on Company 3.0 requirements continues to be critical for
implementing domain lifecycle policies and Tier D classification systems. Ethan Young needs
dedicated time from Cam and engineering stakeholders to finalize specification documents and
establish clear implementation timeline that balances definition consistency with operational
continuity.

Brandon Wilson's semantic signals deployment depends on continued collaboration with Pankaj
and Ivan for GTM store integration and production deployment. The architecture pivot to GTM
store data access requires engineering support to resolve authentication issues and establish
reliable data pipeline for the three priority signals.

Looking Ahead

Next week centers on validating this week's major data infusions and establishing
roadmap for continued geographic expansion. With Dana traveling to India for deep-dive
DIP platform collaboration, the team will focus on verifying the 450K EMEA company creation
results and developing systematic approach for additional targeted infusions.

Brandon Wilson will complete GTM store authentication resolution and finalize semantic
data search capabilities for non-account-specific queries, enabling pipeline-style
opportunities like franchise data outreach to previously unserviced accounts. This work directly
supports the broader revenue acceleration goals by identifying prospects who match newly
available dataset criteria.

Rob Priore will advance opt-out process improvements through technical vetting and
legal review, with final process ready for implementation pending Hannah's approval.
Simultaneously, the team will continue automated customer compliance scanning and
investigate scope of post-churn data sharing cases to ensure comprehensive remediation.**
The team maintains strong momentum on both operational improvements and revenue-driving
initiatives, with clear execution priorities established for maximizing H2 goal achievement while
strengthening foundational data infrastructure.

Source: Team Data Operating Framework entries from [September 2nd - September 4th, 2025]
