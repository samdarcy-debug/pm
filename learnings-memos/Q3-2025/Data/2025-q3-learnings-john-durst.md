---
id: learnings-2025-009
title: Q3 2025 Learnings Memo - John Durst
type: doc
status: approved
team: data
owner: '[[teams/data/_people/john-durst]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
#### **Metric Alignment**



**Contact Publishability (Coverage)**: Formed and led cross-functional

working group across PTI, NeverBounce, and Privacy Notifications

teams---establishing a coordinated approach to email quality. Recognized

expanding privacy regulatory landscape pattern (Canada + additional

jurisdictions) and shifted from a reactive jurisdiction-by-jurisdiction

approach to scalable multi-jurisdiction infrastructure, defining H1 2026

roadmap strategy.



**Contact Accuracy (Quality):**Drove indistinguishable and undercombined

contact detection from concept through production deployment, scoping

mid-single-digit millions of contacts to be merged/generated. Secured

approval for junk contact detection model identifying 55M+ low-quality

contacts, coordinating threshold optimization strategy across Data

Science and Engineering that balances quality improvement with change

management. Identified multi-job contact handling as critical product

gap through customer engagement (Barclays).



**Classification Accuracy (Quality**): Industry model achieved

measurable accuracy improvements validated through targeted batch

predictions (photography studio, beauty/barber). Model validation

confirmed acceptable precision/recall thresholds for production

deployment, with ongoing Research validation ensuring sustained

accuracy.



**Transparency & Trust (Quality Perception):** Transparency API project

initiated---competitive differentiator surfacing data provenance and

decision logic. Addresses technographics quality perception issues that

cost deals. No other data vendor provides attribute-level transparency.



#### **Key Learnings**



**1. Enterprise customers could leverage a DaaS version of signals:**

Conversations with DaaS customers (e.g., Deloitte) revealed demand for

tech add/drop notifications, contact changes, and scoops-derived signals

as a separate data product. Customers building their own copilot-like

signals also express interest in ZoomInfo\'s version to supplement their

process. Signals are fundamentally different from bulk contact/company

data and warrant exploration as a distinct cube/product delivery.



**2. Multi-Job Contact Handling is a Sophisticated Customer Pain

Point:** Enterprise customers report challenges with contacts having

multiple current jobs, resorting to filtering them out. This is a

significant product gap identified through direct customer engagement.



**3. Email Deliverability is Privacy Compliance Bottleneck:** Cannot

publish 6M+ contacts due to low email throughput (\~25k/day vs needed

capacity). Root cause: high bounce rates on accept-all/unknown emails

trigger Spamhaus blocking. Solution requires email validation

improvements, not just infrastructure scaling.



**4. Transparency Beats Raw Accuracy for Customer Trust:**

Technographics quality concerns from customers suggest surfacing \"why

we chose this data\" builds more trust than claiming higher accuracy.

Expanding the Transparency API to technographics addresses client

evaluation challenges, not just data quality.



**5. Technographics Coverage Gaps Need Systematic Tracking:** Need clear

view into technographics coverage by targeted customer usage (similar to

contact data). Ad-hoc growth creates blind spots in customer-critical

areas.



**6. Privacy Regulatory Landscape Expanding Beyond EU**---Requires

Proactive Infrastructure: Canada implemented privacy notification

requirements similar to EU during Q3, and additional jurisdictions are

considering similar regulations. This pattern shift from reactive (EU)

to proactive planning required H1 2026 roadmap adjustments to build

scalable privacy infrastructure (email validation, notification systems,

risk scoring) rather than jurisdiction-by-jurisdiction solutions. Key

insight: Privacy compliance is becoming a global baseline, not a

regional exception---infrastructure must scale ahead of regulatory

announcements.



#### **Hypotheses & Results**



#### **Hypothesis 1: Undercombination Detection Can Significantly Reduce Contact Fragmentation**



**VALIDATED**. Moved project from concept to production deployment.

Initial testing passed review, demonstrating ability to merge fragmented

contact records into coherent profiles. Scoped for mid-single-digit

millions of new contacts to be generated through mutual systems.

Established review process with Research/Analysis for ongoing quality

assurance. Key learning: Detection thresholds require careful tuning to

avoid false positives while maximizing merge opportunities.



#### **Hypothesis 2: Privacy Notification Backlog Can Be Cleared Through Infrastructure Scaling**



#### **INVALIDATED. MORE COMPLEX**. Deep analysis revealed 6M contact backlog isn\'t just an infrastructure problem. Root cause: email bounce rates \>15% (vs required 3-5%) prevent ESP from scaling throughput. Spamhaus blocking risk if we send to spam traps, parked domains, or maintain high bounce rates. Solution requires: 1) Email validation improvements (NeverBounce, RevenueBase, SMTP calls), 2) Risk scoring for email safety, 3) Catch-all/unknown email handling improvements. Cannot simply \"send more emails\"---must improve email quality first. This finding reshaped H2 roadmap priorities.



#### **Hypothesis 3: Technographics Quality Perception Can Be Improved Through Transparency**



#### **VALIDATED.TRANSPARENCY OVER ACCURACY**. Customer feedback revealed that technographics quality concerns are often evaluation challenges, not pure accuracy issues. Customers struggle to assess data quality without understanding our decision-making logic. This insight drove the Transparency API scope expansion---surfacing \"why we chose this data\" (source provenance, tiering, decision logic) builds more trust than claiming higher accuracy percentages. Scoped technographics crawler definition and coverage tracking by customer usage to address systematic gaps. Key learning: Quality perception problems require transparency solutions, not just data improvements.



#### **Go-forward Changes & Plan**



***Drive Cross-Team Email Validation Strategy with Business Case**:

Continue leading coordination across PTI, NeverBounce, and Privacy

Notifications teams to address root cause of 6M contact backlog. Drive

email quality improvements (bounce rate reduction from 15% to 5-10%)

through integrated strategy across email validation, notification

infrastructure, and contact publishing. Connect email quality metrics to

contact publishability and revenue impact---prepare business case for H1

2026 engineering commitment demonstrating ROI. Success metric: Email

validation roadmap approved, H1 2026 engineering commitment secured

across all three teams, business case presented to leadership.*



***Indistinguishable Contact Detection Scaling:** Move from initial

production deployment to scaled rollout. Target mid-single-digit

millions of contacts to be merged/generated. Establish ongoing

Research/Analysis review cycles for quality assurance. Success metric:

Production deployment scaled, quality metrics established.*



***Multi-Job Contact Product Requirements:** Address sophisticated

customer pain point identified through Barclays and other engagements.

Define a product solution for contacts with multiple current positions

(customers currently filter these out). Success metric: Requirements

documented, engineering feasibility assessed.*



***Technographics Coverage Baseline & Roadmap:** Establish systematic

tracking of technographics coverage by customer usage patterns (similar

to contact data approach). Define crawler upgrade requirements.

Implement proactive quality reviews for key accounts. Success metric:

Coverage baseline established, upgrade roadmap defined.*



**Leveraging AI**



***Most Impactful AI Use Case: Data Quality Issue Detection Across Model

Deployments***



*Used AI directly to identify quality issues and edge cases across three

major model deployments---junk contact detection,

undercombination/indistinguishable contacts, and industry

classification. Rather than relying solely on traditional statistical

analysis, leveraged AI to surface patterns in model failures and data

quality gaps that would be difficult to detect manually.*



***AI Expansion Plans:***



*Transparency Metrics Automation: Explore using AI (Ivan\'s context

generation model) to automatically generate transparency explanations

for data attribute selections, reducing manual analysis burden and

enabling scale across all data types (contact, company, technographics)*



***Customer Feedback Loop Systematization:** Use ZI Chat to

systematically analyze customer calls (Barclays-style engagements) and

extract product insights, creating structured feedback loop from

customer conversations to roadmap priorities. Automate insight

extraction from DaaS customer conversations about signals data demand.*



***Technographics Coverage Gap Analysi**s: Leverage AI to analyze

technographics usage patterns by customer segment, identifying coverage

gaps and prioritization opportunities based on customer value and deal

risk (e.g., preventing Google-style losses)*



***H2 Roadmap Communication Scaling**: Use AI to generate

stakeholder-specific roadmap views and status updates, reducing manual

communication overhead while maintaining alignment across Engineering,

Analysis, Product, and DaaS teams*

