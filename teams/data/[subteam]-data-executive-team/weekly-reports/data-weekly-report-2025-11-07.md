---
id: weekly-data-2025-45
title: "Data Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: data
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

Data Executive Roundup - [Nov. 3, 2025 -
Nov. 6, 2025]

Executive Summary

Dana's team exceeded mobile phone enrichment targets by 45%, successfully attaching 5.5
million ByteMine mobile phones to U.S. contacts against a goal of 5 million--with the full 7.25
million records processed ahead of schedule. This substantial lift in mobile coverage positions
the team well for the remaining 99 million ByteMine records awaiting processing. Meanwhile,
Dow secured the complete S&P fleet data file and expects delivery to Valvoline by week's end
despite ongoing legal agreement negotiations, unblocking multiple Q4 opportunities.
Engineering teams made solid progress defining Company 3.0 profiler requirements, and
Suresh deployed a Contributory Network eligibility agent that consolidates compliance data
across multiple Salesforce screens into a single view.

This Week's Progress

Key Momentum Areas

Dana's Research and Data Enablement team processed 7.25 million ByteMine mobile phone
records this week, successfully attaching 5.5 million to U.S. contacts--a 45% improvement over
the 5 million target. The team also completed 1.1 million bad data fixes, a significant increase
over typical production, enabled by dedicated team resources. This momentum continues with
an additional 2 million 5x5 freemail records queued for infusion this week, steadily expanding
contact coverage in high-demand markets.

Dow received the complete S&P fleet data file and has matching results returning by end of
week, positioning the team to deliver productized fleet data to Valvoline by next week. The
franchise webinar drew over 15 external participants including prospects like Toast and
customer BBSI, with a $100K proposal moving forward. These vertical dataset motions are
generating substantial pipeline, with the team ending October at over $2 million in new
opportunities.

Suresh implemented the Contributory Network Eligibility Status Lookup Agent, now available in
legal and compliance workspaces. The agent consolidates contract details, DPA indicators, and
data sharing settings into a single consolidated view, eliminating the need to navigate multiple
Salesforce and Snowflake screens. Early feedback from compliance teams has been positive,
and the platform team has tickets in place to sync eligibility data from Snowflake to ZDP for
downstream system access.
Goals & Progress

Company 3.0 Pipeline Development: Ethan completed requirements documentation for the
final three MVP profilers (description, industry, and phone), bringing all MVP profiler
requirements to completion. The profiler system includes configurable source weights, validation
rules, and value-based boosts, providing unprecedented no-code control for understanding,
modifying, and testing data quality improvements. Engineering design reviews are underway,
with initial testing of matching and indexing components scheduled for next week to evaluate
source migration strategies from Company 2.0 to 3.0.

Fleet Data Productization: The complete S&P fleet data file arrived this week with matching
results expected by end of week, enabling delivery to Valvoline by next week and supporting
additional Q4 opportunities with WEX and Lytx. The team plans to enhance match rates through
UDB matching, potentially reaching 60-70% for prospect files. The main remaining blocker is
executing the legal agreement with S&P, though the team secured data access to maintain
momentum on productization work.

Email Validation and Generation: Steve's team completed testing of Clickagy data as a source
for email generation, achieving 87-90% deliverability for catch-alls and unknowns when Clickagy
hashed emails were seen on cookies within the past 60 days. This strong performance validates
Clickagy as a valuable new source for international email publishing and improved email
coverage. The team is designing a collaborative test with NeverBounce to evaluate whether
Web Data on Demand results can predict email validity, though initial skepticism about the
approach led to scaled-back validation before committing full resources.

Strategic Challenges

Brandon raised concerns about GTM Data Store resourcing and the reliance on Peter to
complete schema design work for four additional datasets. While Peter's dedication to the work
is appreciated, the approach doesn't scale for ongoing dataset onboarding needs. The team
lacks clear documentation or templates that would enable broader participation across the data
organization or even allow partners to self-serve schema design. Multiple stakeholders need
sign-off on each dataset, creating bottlenecks that will slow future dataset launches unless the
process is streamlined and commoditized.

The Waterfall enrichment project needs validation through sample data to ensure the team is
making correct decisions about which data to return and which to exclude. Engineering teams
are already building based on requirements documents, but without concrete examples to
evaluate against expected application behavior, there's risk of misalignment between data layer
decisions and downstream product needs. Brandon emphasized the need for samples by end of
week to validate assumptions with Amesh's platform team and Snee's applications team.

Publishing logic currently prevents enrichment for contacts who have valid mobile phones and
emails but lack current employment information, putting ZoomInfo at a disadvantage when
competitors return this data. Dominik's recent studio analysis revealed numerous valuable
contacts--investors, limited partners, and others between roles--who remain unpublished
despite having accurate contact information. The team identified that the reach-out functionality
built for the Canada index provides a template for solving this, potentially just requiring
applications teams to invoke the same call, though clarity is needed on whether additional
scenarios require different handling.

Strategic Insights

Key Learnings & Discoveries

Brandon observed that the Enterprise New Business Sales Team signed more deals in October
than any previous quarter at higher average ACV, with many customers targeting SMB and
non-tech companies rather than traditional tech buyers. Companies like Suncoast Rentals (truck
and forklift rental) need coverage of small businesses across diverse industries where
ZoomInfo's data is better than competitors but still has significant gaps. This shift in customer
profile highlights the strategic importance of accelerating leadership page crawling and
employee page scraping to unlock hundreds of millions of contacts at smaller companies.

Ethan's preliminary analysis of leadership, board, and employee page crawling opportunities
suggests hundreds of millions of potential contacts could be added through systematic website
scraping. Combined with faster domain addition from customer contributions, improved crawling
capabilities, and incentives for large customers in new industries to contribute their email data,
the team sees a convergence of three capabilities that could dramatically improve SMB contact
coverage. This approach is particularly powerful because new customer segments likely
possess significant email data for small companies that ZoomInfo hasn't historically covered
well.

Jody's key reflection emphasized the need for more ruthless prioritization across the Core Data
team, acknowledging that there will never be a shortage of work but the team can achieve more
impact by focusing efforts rather than keeping a hundred plates spinning simultaneously. The
first step involves documenting all work on each team member's plate and explicitly identifying
items that are known needs but not current priorities. This shift in approach aims to drive better
alignment on outcomes and reduce the tendency to start solutions before clearly defining the
problem being solved.

Cross-Team Dependencies

Our collaboration with Ali's platform engineering team on GTM Data Store onboarding revealed
significant process gaps that need resolution before dataset onboarding can scale efficiently.
While the platform team is driving toward standardization, unclear handoffs and multiple
required sign-offs create friction. Brandon observed that if five different people need to approve
each new data source, the process simply won't work. The team is exploring whether a
comprehensive playbook could enable the broader data organization--or even partners--to
define schemas and make data available without extensive engineering coordination.
The applications and platform teams need clarity on reach-out functionality to enable
enrichment for unpublished contacts with valid contact information. Ethan noted that the Canada
index implementation already provides the necessary infrastructure, potentially requiring just a
configuration change to expand availability. Brandon requested that Ethan connect with Casey
and John to understand current plans and ensure alignment on whether the existing reach-out
approach handles all necessary scenarios or requires modifications for broader unpublished
contact access.

Looking Ahead

Next week's primary focus continues the momentum on ByteMine, planning for the broader 99
million record dataset. Dana's team will coordinate with George to scale up throughput for
adding all 5x5 and ByteMine emails and mobiles--even for contacts where ZoomInfo already
has data--to support the Waterfall enrichment capability with comprehensive secondary values
for business email, supplemental email, and mobile attributes.

Fleet data delivery to Valvoline by week's end remains the top vertical dataset priority, followed
by continued productization work to support WEX and Lytx opportunities. Dow's focus includes
securing execution of the S&P legal agreement while maintaining momentum on entity
resolution and calculated fields based on the matched data. The franchise dataset continues
generating pipeline with multiple customer conversations in flight, and the team is refining
marketing approaches to run more targeted vertical campaigns to specific accounts and
personas.

Ethan begins testing the Company 3.0 pipeline matching and indexing components next week
with newly established environments, evaluating both complete company reshuffling and
bootstrapping approaches to determine the optimal source migration strategy. The profiler
requirements are progressing through engineering design review, positioning the team to
integrate these no-code configurable systems into the pipeline as development continues.
Brandon will lead the team through GTM Data Store schema design working sessions to
accelerate readiness for four additional datasets while developing better documentation to
enable future scaling.

Source: Data Executive Operating Framework entries from [Nov. 3, 2025 - Nov. 6, 2025]
