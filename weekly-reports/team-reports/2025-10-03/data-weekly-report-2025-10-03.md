---
id: weekly-data-2025-40
title: "Data Weekly Report - October 03, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-10-03
updated: 2026-01-06
week_ending: 2025-10-03
reporting_period: "September 29-October 03, 2025"
tags: ["weekly-report", "Q42025"]
---

Data Executive Roundup - [September 29,
2025 - October 2, 2025]

Executive Summary

Brandon Tucker is leading a multi-pronged effort to integrate vertical dataset entities into the
core platform, starting with franchise data as a proof of concept. This foundational work will unify
ZI IDs across platform and cubes, simplifying data management for both internal teams and
customers while unlocking millions of associated contacts. The team successfully identified 114
accounts requiring legal review for post-termination data ingestion compliance, and made
significant progress on the contributory network benchmark agent by resolving a data
architecture issue that now enables statistical analysis across 50-60 tenants per account.

This Week's Progress

Key Momentum Areas

Igor Kyrylenko delivered two production-ready vertical datasets this week: franchise data with
manually researched franchisor coverage and automated QA validation, plus a veterinarian
dataset pulled from federal databases with ZoomInfo matching completed. The franchise work
included identifying 1,000 larger franchisees and establishing an automated match validation
process that will accelerate future dataset releases. Igor also initiated preliminary scoping on 12
states of professional license data and secured a promising call with IDEMI, a $2 billion
company working with federal agencies interested in First Mover Advantage and contractor
datasets.

Dana Hurtig's team completed scraping of 10,000 U.S. private equity firm investment portfolios
with 60% automated capture, successfully pushing 280,000 EMEA Rhetorik companies to
production, and delivering 1.3 million enrichments primarily from Orgimport mobile phones. The
franchise dataset now has all franchisors synchronized with only 35 net-new companies created
from 4,700 records, with location and franchisee work tickets already in flight for complete
integration.

Brandon Wilson achieved a breakthrough on contributory network benchmark data by
discovering and resolving the GTM opportunity table's account ID architecture issue. The team
can now analyze deal cycles across multiple opportunities per account, with some top accounts
showing 50-60 eligible tenants--a significant leap from the previous one-to-one limitation that
made statistical analysis impossible. Shauna is running stage name normalization to prepare
aggregated views for the benchmark agent.
Goals & Progress

Vertical Dataset Integration: Brandon Tucker is executing large-scale entity infusions using
franchise data as the test case to understand gaps in source data quality, platform publishing
requirements, and entity type handling. Dana Hurtig's team synchronized franchise franchisors
with the platform (only 35 new companies from 4,700 records) and has contact, location, and
franchisee integration tickets actively in progress. This work establishes the foundation for
simplified data management through unified ZI IDs and will unlock associated contacts from
vertical datasets.

Compliance & Data Governance: Suresh Putteti completed review of 3,000+ inactive
customer accounts whose data continued ingesting post-termination, identifying 15 accounts
with DPA flags and 99 with non-standard EULA contracts. The consolidated list was delivered to
legal team members Hannah and James Henry to determine notification obligations. Suresh
developed a reusable Snowflake query for future compliance reporting and worked with
integration, ZDP, and GTM teams to implement preventive fixes stopping post-termination
ingestion.

GTM Studio & Benchmark Agents: Brandon Wilson resolved the contributory network data
architecture challenge where account IDs were unique per opportunity rather than per company.
By mapping through the GTM accounts table to external entity IDs and ZI company IDs, the
team now accesses deal cycle data showing 50-60 tenants working with top accounts. Stage
name normalization is in progress to enable statistical analysis on opportunity duration and
sales cycle benchmarking for the CN benchmark agent that Heather Ma is developing.

Strategic Challenges

Email deliverability concerns from PTI have paused 500,000 generated work email infusions
that Dana Hurtig's team had queued. PTI previously halted generated email enrichment due to
deliverability issues, and the Data Enablement team is aligning on a path forward that balances
coverage improvements with email health standards. This coordination ensures the research
team's infusion work supports rather than undermines platform email quality metrics.

The contributory network benchmark agent faces data hygiene obstacles where close dates
precede creation dates and inconsistent CRM data entry by sales reps limits reliable insights.
With only 1,200 eligible tenants connected and minimal account overlap across tenants,
statistical sample sizes remain constrained. Brandon Wilson is exploring the latest GTM
opportunity table and investigating semantic data as an alternative avenue, while Brandon
Tucker suggested bootstrapping with firmographic-based trends as an interim solution if
account-specific benchmarking proves unviable.

Lost deal slice development by Steve Hutchinson requires cross-functional coordination with
multiple product teams beyond the initial S2A homepage implementation. The conservative V1
definition (former account owners of lost opportunities with no wins or open opportunities) will
serve only a small user subset initially, though deeper research is already exploring looser
definitions for V2. Steve is connecting with Sean Walter to understand consumption patterns for
future applications while the data analysis team builds local pipeline writes to priority accounts.

Strategic Insights

Key Learnings & Discoveries

Brandon Tucker identified that tiering work combined with custom dataset corroboration creates
highly actionable vertical datasets, evidenced by confidently delivering a sample to Angi (a
mid-six-figure opportunity) with no additional QA required. The team should proactively
incorporate vertical attributes into data evaluations, samples, and eventually GTM Studio to
simplify discovery of high-quality data rather than requiring manual work for large opportunities.
This approach transforms complex adhoc pulls into scalable self-service capabilities.

Ethan Young's work on Company 3.0 post-match flow design revealed significant opportunities
to prevent rather than fix data quality issues. The new system includes multiple validation
categories with specific checks to filter junk early, prevent duplicate creation at ingestion rather
than resolving later, and handle domain ownership to reduce under and overcombination. The
company definition framework aligns well with franchise vertical requirements, providing
confidence that structural needs for business relationships are properly addressed.

Brandon Wilson's investigation into the GTM accounts table structure uncovered that the
seemingly unintuitive architecture was masking valuable deal cycle data. The realization that
account IDs were opportunity-specific rather than company-specific explained the one-to-one
tenant limitations. By enriching external entity mappings with tenant name, industry, revenue,
and employee size, the team can now bucket which types of companies do business with
specific accounts--unlocking firmographic patterns previously invisible in the data.

Cross-Team Dependencies

Our work with the PTI and product teams on email deliverability standards is essential for
maintaining platform health while maximizing coverage. Dana Hurtig's team paused 500,000
generated email infusions to align on deliverability thresholds and validation processes. This
coordination ensures research-driven enrichments support rather than undermine email quality
metrics that affect customer trust. Clear guidelines from PTI on acceptable generation practices
will accelerate the path forward for work email coverage improvements.

Jody Roberts is coordinating with the PTI team and Heather Ma's group to productionize board
of directors data delivery and integrate manager attributes from Google Directory and GAL data.
With over 100,000 companies covered in these sources, the org chart agent shows promise, but
requires engineering support to determine optimal data connectivity and combination
approaches. Lars and the agentic platform team are evaluating whether org chart should
function as a callable subagent in Copilot and SalesOS or as an MCP connection.
Looking Ahead

Next week focuses on three critical integration workstreams that will accelerate vertical dataset
value and contributory network capabilities while strengthening our compliance posture.

Brandon Tucker will partner closely with Dana Hurtig's team to test franchise entity
integration--adding locations, contacts, and companies to understand platform publishing gaps,
address quality issues, and create dataset-specific integration plans. This foundational work
establishes patterns for efficient vertical data management with unified ZI IDs across platform
and cubes. Simultaneously, Brandon will push S&P legal and procurement processes forward
and launch new GTM enablement programs to ensure sales teams recognize the rapid
improvements being made to vertical datasets. Igor Kyrylenko continues advancing professional
license data acquisition while finalizing veterinarian dataset delivery and building detailed
roadmaps for the next eight vertical projects with schema complexity assessments.

Brandon Wilson will analyze the latest GTM opportunity table to determine viability for
benchmark insights, exploring both account-specific deal cycle statistics and firmographic-based
trends as fallback options if data hygiene issues prove too constraining. Steve Hutchinson's
team expects to write lost deal data to staging for S2A consumption while connecting with
additional product teams to expand future use cases beyond the Copilot homepage. Dow Jones
is refining Q4 plans for priority dataset improvements and GTM enablement, identifying specific
data coverage gaps and friction points that sellers encounter in this new motion.

The team's ability to simultaneously advance vertical dataset integration, contributory network
benchmarking, and compliance remediation while maintaining data quality standards
demonstrates strong execution velocity heading into Q4. With clearer integration patterns
emerging from franchise work and breakthrough progress on CN data architecture, we're
positioned to scale both internal efficiency and customer value delivery.

Source: Data Executive Operating Framework entries from [September 29, 2025 - October 2,
2025]
