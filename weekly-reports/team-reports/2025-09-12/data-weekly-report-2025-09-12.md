---
id: weekly-data-2025-37
title: "Data Weekly Report - September 12, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-09-12
updated: 2026-01-06
week_ending: 2025-09-12
reporting_period: "September 8-12, 2025"
tags: ["weekly-report", "Q32025"]
---

Data Executive Roundup - [September 8th
- September 11th, 2025]

Executive Summary

Rob Priore secured preliminary legal approval for a blanket contributory network notice covering
present and future product activities, eliminating the need for individual approvals on each new
CN-driven product like benchmarking and recommendations. This breakthrough will accelerate
development cycles for new customer-facing tools while maintaining compliance. Additionally,
Igor Kyrylenko completed the franchisor dataset in final Snowflake format with full traceability,
positioning the team to deliver a unique vertical dataset that sales can immediately leverage
with enterprise accounts.

This Week's Progress

Key Momentum Areas

Igor successfully finalized the franchisor dataset with complete lineage tracking to raw data
sources across all four tables (franchisor, franchisee, location, contact), enabling sales teams to
offer a unique vertical dataset that competitors lack in structured format. The dataset includes
successful ZoomInfo company and person record matching, providing immediate value for
enterprise accounts seeking visibility into franchise ownership structures.

Rob's legal breakthrough establishes a framework for using eligible customer data to develop
and test new contributory network products without individual approvals. This streamlined
compliance approach will enable faster iteration on benchmarking tools, agent development,
and other data-driven innovations while maintaining transparency with customers through
comprehensive disclosure.

Dana completed productive deep-dive sessions with the India team on company data infusion
processes, significantly improving the team's capability to independently manage DIP infusions.
This knowledge transfer positions the team to accelerate company additions across priority
geographies, with EMEA data currently in staging awaiting final engineering sign-off.

Goals & Progress

Franchise Data Productization: Igor completed the franchisor dataset in production-ready
Snowflake format with full traceability from raw source to final tables, achieving 95% of weekly
goals. The dataset now supports immediate sales demonstrations and customer samples, with
Brandon Tucker successfully delivering franchise samples to March Networks and building a
reusable foundation for future customer requests.

Compliance Infrastructure: Rob achieved 100% completion on establishing the simplified data
sharing compliance flow, securing preliminary legal approval for blanket contributory network
notices. This eliminates previous bottlenecks requiring individual legal review for each new
product iteration, while also implementing automated customer compliance monitoring through
the Privado tool for CIPA violations.

Data Infrastructure & Quality: Steve identified and began addressing email generation model
issues affecting domains with asynchronous bouncing patterns, working with DataPure to
implement solutions that should improve overall email deliverability. Dana progressed company
data infusion capabilities with successful deep-dive training sessions, positioning the team for
accelerated geographic expansion.

Strategic Challenges

Email generation model reliability continues to present challenges, with Steve identifying that
10% of domains show false positive delivery rates due to asynchronous bouncing. While a path
forward exists through vendor collaboration and domain filtering, this affects training data quality
and requires coordination between data science and vendor teams to implement
comprehensive solutions.

Brandon Tucker's franchise data development faces scaling challenges as customer demand
significantly exceeds initial expectations. Multiple enterprise accounts are requesting immediate
samples, creating a bottleneck between high market interest and data processing capacity. The
team needs enhanced solution consultant support and potentially automated sampling
capabilities to match demand velocity.

Company 3.0 planning requires additional coordination time to ensure proper milestone
definition and resource allocation. Ethan Young noted the need for intensive planning sessions
to balance quarterly improvements with longer-term architectural changes, particularly around
location relationships and employment structures for franchise entities.

Strategic Insights

Key Learnings & Discoveries

The franchise dataset is generating unexpectedly strong market demand, with customers
immediately requesting samples upon hearing about the offering rather than requiring extensive
sales cycles. This validates the strategic focus on vertical datasets but highlights the need for
more scalable demo and sampling processes to capitalize on market readiness.
Rob's implementation of automated compliance monitoring through Privado has proven 100%
accurate in identifying customer CIPA violations across initial testing. This capability not only
protects ZoomInfo from regulatory exposure but provides a scalable method for monitoring
thousands of customer websites rather than manual review processes that previously limited
scope.

Dana's analysis of company data infusion processes revealed opportunities for significant
automation improvements. The successful knowledge transfer to the India team demonstrates
that complex data operations can be systematized and distributed, enabling faster geographic
expansion while maintaining quality standards.

Cross-Team Dependencies

Our work with engineering teams on company data staging requires timely sign-off to maintain
momentum on EMEA infusions and subsequent geographic expansions. Dana's coordination
with the company team is essential for converting staging data to production, with several
customer requests pending completion of this process.

The semantic signals enhancement work led by Brandon Wilson depends on GTM store API
stability and engineering prioritization from Pankaj and Ivan's teams. Architecture diagrams are
ready for implementation once engineering schedules align, representing a significant
improvement in signal quality and relevance for sales teams.

Looking Ahead

Next week focuses on converting completed development work into customer-facing value, with
franchise dataset samples ready for immediate deployment and company data infusions moving
from staging to production.

Priority initiatives include accelerating franchise data automation to reduce manual intervention
while expanding multi-brand owner coverage, implementing the simplified contributory network
compliance framework to unlock new product development, and finalizing EMEA company
infusions to address customer geographic coverage requests. Success metrics center on
converting franchise dataset interest into confirmed sales opportunities and establishing
consistent company infusion throughput across target geographies.

The team is well-positioned to deliver significant value in Q4, with core infrastructure
improvements enabling faster iteration on customer-facing products while maintaining the data
quality and compliance standards that differentiate ZoomInfo's offerings. Key execution focuses
on scaling proven processes rather than building new capabilities, leveraging the foundation
work completed over the past quarter.
Source: Data Executive Operating Framework entries from [September 8th, 2025 - September
11th, 2025]
