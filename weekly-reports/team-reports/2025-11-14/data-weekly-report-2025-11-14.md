---
id: weekly-data-2025-46
title: "Data Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

Data Executive Roundup - [Nov. 10, 2025 -
Nov. 13, 2025]

Executive Summary

ByteMine mobile phone infusions exceeded targets by 78%, successfully pushing 3.5M records
into production with PTI resolving a critical processing bug that had been causing bottlenecks.
Brandon Tucker is leading a hands-on effort to democratize dataset onboarding through GTM
Studio, walking the GitHub dataset through the process to identify friction points and building AI
agents to automate documentation. The team is addressing a growing confusion among sales
about Company Master vs traditional matching, which is creating unnecessary friction in
customer conversations and requiring immediate enablement with Yixing's team. Ethan Young's
Company 3.0 testing environments are now operational, marking the first phase of validating the
new pipeline's matching capabilities.

This Week's Progress

Key Momentum Areas

Dana Hurtig's team achieved 178% of their ByteMine mobile phone infusion goal, processing
3.5M records and working closely with PTI to resolve source ranking issues for alternate
mobiles and freemails. The collaboration with PTI uncovered and fixed a processing bug that
had been creating queue bottlenecks, enabling faster throughput going forward, and resulting in
a total of 7.7M data infusions (including Bytemine) for the week. The team is also testing two
promising new data sources: a WhatsApp API for mobile validation and Surf, which is delivering
75-80% hit rates on previously missing mobile phones.

Brandon Tucker completed preparation for next week's waterfall hackathon and built the first AI
agent to automate dataset onboarding documentation, successfully generating a
comprehensive one-pager for the GitHub dataset in minutes. This represents a critical step
toward democratizing the onboarding process, potentially enabling the team to add 100+
datasets next year by removing the bottleneck of manual documentation and analysis that
currently lives in the heads of platform team members.

Igor Kyrylenko completed acquisition of 29 states for professional licenses data and initiated
FOIA requests for automotive dealerships and building permits across major jurisdictions. The
team has already received 11 states of automotive dealership data and sent requests to 67 of
the largest municipalities for construction permit data. This represents 72% U.S. population
coverage for professional licenses and establishes a natural competitive barrier, as acquiring
and normalizing data from 50+ disparate state systems requires significant time and resources
that competitors would struggle to replicate.

Goals & Progress

Mobile Phone & Contact Coverage: ByteMine processing reached 178% of weekly targets
with 3.5M mobile phones infused, including successful implementation of alternate mobile and
freemail rankings to prevent overwriting existing data. The team validated source rankings with
PTI and is ramping up processing for the remaining ByteMine dataset. New contact creation
from unpublished ByteMine and 5x5 profiles is under review with testing ongoing for WhatsApp
validation (checking mobile availability for messaging) and Surfe data source (75-80% fill rate
on missing mobiles). 2.7M ProgAI enrichments completed at 100% of goal, with 600K ByteMine
freemails and 300K Rhetorik contact creations pending completion. Bad data fixes reached
1.3M records, 87% of target for the week.

Company 3.0 Pipeline Testing: Ethan Young successfully set up and tested initial Company
3.0 environments with both bootstrapped (pre-populated) and blank Solr indexes operational for
comparative matching analysis. The team identified several infrastructure needs including bulk
record submission scripts, expanded matching traces in BigQuery for both environments, and
pathways to source test records from Company 2.0 and other data sources. Company Master
API replacement testing is progressing well with strong matching logic results, positioning the
team to deprecate EverString API within weeks. The team is building tools to send test sets
efficiently and developing comprehensive test plans for both new company creation flow and
existing profile migration scenarios.

GTM Studio & Dataset Onboarding: Brandon Tucker walked the GitHub dataset through the
onboarding process to identify bottlenecks and documentation gaps, building an AI agent that
generates comprehensive dataset one-pagers by interviewing users through voice recording.
The agent successfully produced a complete reference document in less time than it took to
build, demonstrating a path to scale dataset contributions across teams. Preparation for next
week's waterfall working session is complete, with the goal of producing functional capabilities
rather than just plans. The team is addressing confusion in sales about Company Master vs
traditional ZoomInfo matching, as sellers are inadvertently using both approaches
simultaneously and getting inconsistent results, requiring urgent enablement with Yixing's team.

Strategic Challenges

Sales teams fundamentally misunderstand the distinction between Company Master
(location-based matching) and traditional ZoomInfo matching (HQ-based), leading to sellers
running the same data through both systems and then questioning why results differ. Multiple
instances emerged this week of customers using both approaches simultaneously--integrating
traditional match service through CRM Enrich while doing offline enrichment with Company
Master--creating confusion about data quality and match accuracy. The issue has escalated to
the point where sellers are running name-and-address-only matching through Company Master
while simultaneously enriching on domain through traditional systems, even when domain data
is available. This requires immediate coordinated enablement with Yixing's team and potentially
a company all-hands communication, as the lack of understanding is creating unnecessary
friction in customer conversations and undermining confidence in matching capabilities.
Brandon Tucker noted that sellers need clear guidance on when to use each approach and that
Data Services should begin qualifying use cases before running match requests.

The swapper.exe degradation timeline for April 2026 presents a significant strategic challenge
as Windows 11 and new Outlook versions will no longer support the executable approach,
forcing migration to web-based authentication or Microsoft Store plugins. The plugin option
faces high barriers to entry requiring admin approval for installation, making it largely a
non-starter for scaled adoption. The historical top-of-funnel approach--driving non-customers to
directory pages to install Swapper and contribute signatures--has consistently failed to scale
despite attribution data showing signature sources were historically the largest contributor to
new emails and phones. Jody Roberts is coordinating a multi-team response with Heather Ma
and TPM support from Ina, focusing on a multi-pronged email strategy encompassing validation,
threat detection, send optimization, and new acquisition methods. The team needs creative
solutions for signature data acquisition beyond the legacy PLG model, as AI disruption of search
and inbound traffic is fundamentally changing how people discover and interact with directory
pages. Ethan Young raised concerns about urgency given zippy data's criticality to core contact
data, though Brandon Tucker noted the challenge is less about prioritization and more about
identifying viable alternative approaches when the obvious technical path isn't available.

PTI processing bottlenecks resolved after extended back-and-forth revealed an underlying bug
rather than just capacity constraints, though the discovery process highlighted the need for
more direct escalation paths for high-impact data infusion work. Dana Hurtig's team experienced
delays processing ByteMine data as records sat in queues that appeared as timeouts but were
actually just backlogged. Jody Roberts and Brandon Tucker reinforced with Kristen and Ritu that
mobile phone accuracy and fill rate improvements represent the highest-impact opportunity
available and should receive all-hands support, as this is the easiest and most valuable work
the team can do. The resolution of the bug and increased PTI responsiveness over recent days
suggests the message is landing, though sustained attention will be needed to maintain
momentum as the team processes the remaining 99M ByteMine records and additional data
sources. The situation underscores the organizational challenge of ensuring data quality and
coverage work receives the same urgency as product feature development.

Strategic Insights

Key Learnings & Discoveries

ZoomInfo's search infrastructure and referential dataset represent a massive competitive moat
that the business struggles to articulate to technical buyers, as demonstrated in this week's
conversation with BCG consultants who dismissed GTM Studio as just another tool they could
build themselves via APIs. Brandon Tucker identified that most companies fail to understand
three critical components: the search infrastructure required to query across dozens of disparate
datasets at scale, the 20 years of accumulated alt domains and alt names that power nuanced
matching logic, and the power of having a single authoritative referential dataset that eliminates
the need for exponential cross-matching (matching 30 datasets to each other requires
thousands of match operations versus matching each to one canonical dataset which provides
unified profile automatically). Technical buyers understand that individual matching algorithms
are straightforward but miss the supporting infrastructure around location normalization, address
parsing, and derived geography relationships that enable ZoomInfo to match successfully even
with incomplete input data. The team needs customer-facing materials that can explain this to
MDM-type technical audiences, as the current pitch fails to resonate despite representing
genuine technical advantages competitors would take years and significant investment to
replicate.

Clay's only sustainable advantage in waterfall enrichment is their established integrations, not
their data quality or vendor portfolio, which consists largely of unknown Tier D providers that
customers aren't loyal to. Brandon Tucker's analysis revealed Clay charges 14 credits per
mobile phone enrichment at 1.5-5.5 cents per credit (up to 50 cents per contact), and customers
must pay again for every data refresh. ZoomInfo's record-under-management model provides
free refreshes for a year, creating a massive pricing advantage once waterfall capabilities
launch. Additionally, Clay lacks a frontline activation solution and has weaker core data,
meaning ZoomInfo should win most competitive situations through superior data quality, better
integrations, consumption-friendly pricing, and AI credits at commodity rates. The key learning is
that waterfall isn't about matching Clay's exact vendor list but rather demonstrating superior
match rates at lower cost with better refresh economics and integration into the broader
ZoomInfo platform.

Professional licenses and vertical datasets create natural competitive barriers because
acquiring data from 50 states plus DC is expensive and time-consuming, making it hard for
competitors to replicate even though individual state data is technically accessible. Igor
Kyrylenko noted that while anyone could theoretically build 100 APIs to collect this data, it would
cost approximately $200,000 in human labor and take 6 months, creating a meaningful
first-mover advantage. The request-based nature of FOIA processes means that once ZoomInfo
establishes collection systems and maintains them, the ongoing effort is significantly lower than
the initial build. These datasets differentiate ZoomInfo in ways that matter to specific customer
segments--professional licenses expanding beyond contractors, automotive dealerships,
construction permits--and the structured nature of government-mandated data ensures
consistency and authority that proprietary datasets lack. The learning reinforces that vertical
dataset strategy should focus on government-mandated or otherwise regulated data sources
where acquisition difficulty serves as a natural moat.

Cross-Team Dependencies

Work with PTI on ByteMine data processing evolved from adversarial to collaborative after
identifying that perceived capacity constraints were actually a bug causing queue backlog. Dana
Hurtig's team maintained constant communication with PTI to surface issues in real-time,
leading to the discovery and resolution of the underlying problem. The experience highlights the
importance of sustained engagement rather than one-time escalation when processing
large-scale data infusions. Going forward, the team needs clear prioritization signals from
leadership when mobile phone and contact data work should receive maximum support, as
Brandon Tucker's message to Kristen and Ritu emphasized this represents the highest-impact
opportunity available. Future large-scale infusions (remaining 99M ByteMine records, 5x5 data,
Surf data) will require similar coordination, and establishing clearer escalation paths would
prevent delays in future processing.

Coordination with Yixing's enablement team is needed immediately to address sales confusion
about Company Master versus traditional ZoomInfo matching, as the problem has escalated
beyond individual cases to a systemic misunderstanding. Multiple sellers are using both
approaches simultaneously without understanding why they get different results or when to use
each approach. The team needs to create clear documentation differentiating location-based
versus HQ-based matching and establish guidelines for Data Services to qualify use cases
before running matches. Brandon Tucker, Dana Hurtig, and Ethan Young will develop materials
for Yixing's team to deploy first to sellers, potentially followed by broader company
communication. The dependency is time-sensitive as ongoing confusion undermines customer
confidence in matching accuracy and creates unnecessary support burden.

Brandon Wilson's deal cycle insights agent requires the contributory network flag to be
accessible in ZDP and stage normalization to be automated, with timelines from Jesse
Lundstrom and Ron Kadneau indicating mid-December for the CN flag. Steve Hutchinson
confirmed that stage normalization is not actively being worked on and is second priority behind
other initiatives, meaning Brandon Wilson will need to manually run Shauna's normalization
process in the near term. The dependency highlights the challenge of building on top of GTM
Store infrastructure that's still being developed, though Brandon Wilson has identified
workarounds to maintain progress. Heather Ma is collaborating on the 100-day-to-production
plan for the agent, with the team developing temporary solutions that can be swapped for
automated processes once dependencies are resolved.

Looking Ahead

Next week centers on the waterfall hackathon working session where the team aims to produce
functional capabilities rather than plans, building on Brandon Tucker's preparation work and
GitHub dataset onboarding documentation. Dana Hurtig's team will continue ramping ByteMine
processing for the remaining dataset, pushing forward with freemail infusions and exploring new
contact creation from unpublished profiles in ByteMine and 5x5. The team is finalizing testing of
WhatsApp validation and Surf data sources to determine whether to integrate them into
production workflows.

Ethan Young will build tools to efficiently send test records to Company 3.0 environments and
identify appropriate test sets for both new company creation and existing profile migration,
writing comprehensive test plans to guide the matching validation work. Brandon Wilson will
implement temporary solutions for the CN flag and stage normalization in his deal cycle insights
agent pipeline, building aggregate tables to support demo scenarios for the upcoming board
meeting. Igor Kyrylenko will complete professional licenses normalization and deliver statistical
breakdowns for waiting clients, while continuing to process incoming automotive dealership data
from FOIA requests across the 67 targeted municipalities.

The team must move quickly on Company Master versus ZoomInfo matching enablement
materials with Yixing, as ongoing confusion in sales is creating friction in customer
conversations and undermining confidence in data quality. Jody Roberts will continue
coordinating the swapper degradation response with Heather Ma and TPM Ina, developing the
multi-pronged email strategy and exploring alternative signature data acquisition approaches.
The waterfall hackathon represents a critical milestone in democratizing dataset onboarding and
accelerating ZoomInfo's ability to compete with Clay's vendor integrations, while the Company
3.0 testing marks the beginning of validating the next-generation pipeline that will ultimately
replace current matching infrastructure.

Source: Data Executive Operating Framework entries from [Nov. 10, 2025 - Nov. 13, 2025]
