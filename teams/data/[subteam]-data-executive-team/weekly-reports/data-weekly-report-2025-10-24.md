---
id: weekly-data-2025-43
title: "Data Weekly Report - October 24, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-10-24
updated: 2026-01-06
week_ending: 2025-10-24
reporting_period: "October 20-24, 2025"
tags: ["weekly-report", "Q42025"]
---

Data Executive Roundup - [Oct 20th, 2025
- October 23rd, 2025]

Executive Summary

Board of Directors and Executive Leadership Team datasets are attracting significant enterprise
attention beyond our initial Barclays deployment. ServiceNow, AlphaSense, RBC, and others
are requesting this data with varying requirements, creating an opportunity to transform a
one-off custom deliverable into a productized offering. We need product ownership and a clear
support framework to scale this demand while maintaining quality. Meanwhile, the Contributory
Network V2 infrastructure is production-ready with eligibility flags now available in Salesforce
and Snowflake, enabling expanded data sharing for opportunities and calendar data.

This Week's Progress

Key Momentum Areas

Dana's team delivered over 2 million GitHub social URL enrichments and pushed 280,000 new
EMEA companies to production, strengthening international coverage for key enterprise
customers. The team also completed 300,000 data fixes while managing multiple high-priority
customer projects for ServiceNow, Epicor, Cvent, and Trade Desk scheduled for month-end
delivery.

Suresh successfully implemented the Contributory Network eligibility status flag in Salesforce
with values now populated in Snowflake, enabling downstream systems to distinguish between
full sharing, partial sharing, and no sharing contracts. After legal review, the team resolved edge
cases where accounts have multiple contracts by defaulting to the most restricted agreement,
providing clear guidance for CN V2 requirements.

Brandon integrated the GTM Store GraphQL API into the deal cycle analysis pipeline and added
company segmentation classification, allowing the agent to group insights by deal size,
company segment, and industry. This enables tenants to benchmark their deal cycles against
similar accounts in the contributory network, with a board meeting demo targeted for Monday
despite the compressed timeline.

Goals & Progress

FINRA & Professional Licenses Datasets: Igor's team ingested the complete FINRA dataset
into Snowflake with CRD numbers for every U.S. broker and investment advisor, now working
with Peter to identify customer-facing fields for productization as a potential PitchBook
alternative. Professional licenses data acquisition continues with 18 states processed and
additional single-point-of-acquisition states being targeted to expand coverage beyond
contractors into regulated professions.

Privacy Notice Deliverability: Steve's team completed analyses examining NeverBounce valid
email performance, discovering that approximately 15-26% of valid privacy notices are
bouncing. The investigation revealed that certain buckets of NeverBounce results perform
differently, with some Acton-blocked IPs actually delivering through alternative vendors. Next
week the privacy notice team will make strategic decisions about email categorization to
increase send volume while maintaining acceptable bounce rates.

Money 2020 Conference Presence: The team is preparing for Money 2020, a major fintech
conference with 13,000 attendees, where Igor, Dow, and Brandon will showcase vertical
datasets and GTM Studio to prospective clients. This represents a significant opportunity to
generate pipeline for financial services data offerings including FINRA, professional licenses,
and other regulated industry datasets.

Strategic Challenges

The Board of Directors and Executive Leadership Team data requests are coming with
increasingly varied requirements from different enterprise customers, each with unique nuances
around scope, data elements, and delivery formats. While the research team has built a
scalable manual process for Barclays, transforming this into a hardened product requires
product ownership, clear prioritization, and engineering support to handle multiple employment
relationships more gracefully in the platform. Dana has documented the current state and
requirements for Jody and Peter to assess productization options.

Multiple team members including Dana, Dow, Igor, and Brandon will be traveling next week for
either Money 2020 or vacation, creating limited coverage during a period with several
month-end customer deliverables. The offshore team in the Philippines has bandwidth to absorb
larger projects, with Ashley and Stacy providing U.S.-based coverage, but coordination will
require proactive communication to ensure nothing slips through the cracks.

Brandon is racing to complete a board meeting demo for the CN deal cycle agent by Monday
with limited time remaining. While the data infrastructure is coming together well with GTM Store
integration and company segmentation complete, the compressed timeline creates risk that the
demo may not be fully polished for executive presentation.

Strategic Insights

Key Learnings & Discoveries
The BOD/ELT data opportunity reveals a pattern where initial custom work for one enterprise
customer can rapidly generate demand across other large accounts once the value is
demonstrated. ServiceNow, AlphaSense, and RBC are all expressing interest after seeing what
was built for Barclays, suggesting that packaging executive-level data as a distinct product
offering could accelerate enterprise deals. However, each customer's unique requirements
highlight the need for a flexible data model that can accommodate varying scopes while
maintaining a core standardized schema.

Steve's privacy notice analysis uncovered that NeverBounce's validation categories perform
differently in production, with certain "valid" classifications showing higher bounce rates than
expected. The discovery that Acton marks some emails as "Blocked IP" while those same
addresses deliver successfully through DataPure suggests that vendor-specific factors may be
creating artificial quality issues. This finding opens opportunities to optimize the privacy notice
queue by routing different email categories through the most appropriate sending channel.

Brandon's work integrating GTM Store data revealed significant data quality issues in the
standard opportunity tables, with deal amounts showing negative numbers, unrealistic values
like $100 million, or missing entirely. The GraphQL API returns more reasonable values for
these same opportunities, indicating that direct API integration provides more reliable data than
relying solely on ZDP tables. This learning suggests other data pipelines may benefit from
similar direct API access rather than depending on intermediate data stores.

Cross-Team Dependencies

Our ability to scale the BOD/ELT offering depends on engineering work to better handle
contacts with multiple simultaneous employments, which currently causes platform issues when
someone serves on multiple boards or holds positions at different companies. This platform
limitation forces the research team into manual workarounds that aren't sustainable at scale.
Jody and Peter's product ownership will be necessary to prioritize these improvements and
define the scope for a productized solution.

Brandon's CN deal cycle agent requires the contributory network eligibility flag to be available in
ZDP, not just Salesforce and Snowflake. Suresh has confirmed that Ron's team is working on
populating this field in company data tables, which will enable Brandon to keep his entire
pipeline within the ZDP ecosystem. This cross-team coordination between data governance,
engineering, and data analysis is proceeding smoothly with clear ticket tracking.

Looking Ahead

Next week's reduced team presence due to Money 2020 and planned vacations means
proactive communication and clear handoffs are necessary to maintain momentum on customer
deliverables. Ashley and Stacy will provide U.S.-based coverage for Dana's team, while the
offshore Philippines team has capacity for larger projects that arise.
The Money 2020 conference represents a significant opportunity to generate pipeline for
financial services datasets including FINRA, professional licenses, and other vertical data
offerings. Igor, Dow, and Brandon will engage with prospects among the 13,000 attendees,
building on last year's successful participation. Separately, the board meeting demo on Monday
will showcase the CN deal cycle agent's ability to provide benchmark insights, though the
compressed timeline means the team is working right up to the presentation to finalize
examples and polish the output.

Dana's work documenting the current state of BOD/ELT datasets and gathering requirements
from multiple enterprise customers will enable Jody and Peter to assess productization options
when she returns from vacation. This strategic decision on whether to formalize these offerings
as distinct products versus continuing with custom deliveries will shape how we approach
similar opportunities with other executive-level data requests going forward. The team's strong
execution on enrichments, company additions, and data fixes continues providing the
foundation that makes these higher-value offerings possible.

Source: Data Executive Operating Framework entries from [Oct 20th, 2025 - October 23rd,
2025]
