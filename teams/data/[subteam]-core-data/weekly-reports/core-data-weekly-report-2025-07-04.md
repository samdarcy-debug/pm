---
id: weekly-core-data-2025-27
title: "Core Data Weekly Report - July 04, 2025"
type: weekly-report
status: approved
team: core-data
owner:
created: 2025-07-04
updated: 2026-01-06
week_ending: 2025-07-04
reporting_period: "June 30-July 04, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Core Data Executive Roundup - Week of 06/30 - 07/03**

## **Executive Summary**

**Rituparna Das led a major boost in contact coverage by completing
infusion of 26 million additional freemails from 5x5 vendor data, which
has so far resulted in 9.1 million new freemails available including 6.7
million attached to previously freemail-less contacts (Additional impact
analysis is pending).** This provides significant expansion of our
contact reachability across all areas of our products including talent
acquisition partners and improved WebSights visitor resolution.
Additionally, Cam Fortin advanced company cube release preparation
toward July 15th update. Hayden Cowell advanced email confidence model
validation by completing testing between an existing regression model
and data science\'s machine learning approach, with initial results
favoring data science\'s approach for API implementation pending final
team discussions. Heather Ma achieved completion on an AI agent
prototype (demo
[[link]{.underline}](https://zoominfo.zoom.us/clips/share/hBp_C30pSp26aaVN4ZfgYA))
that successfully provides buyer engagement map agent on ZI agentic
platform (tier 1 version) with basic relationship info and engagement
data for single tenant. Which will ultimately drive the ability to
showcase the value for customers who opt into Contributory Network
contribution. However, Peter Overman\'s Form 5500 requirements analysis
revealed that existing data storage doesn\'t meet customer use cases,
requiring a ground-up rebuild that could impact Q3 delivery timelines.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Freemail Coverage Expansion**: Rituparna Das completed processing of
26 million remaining freemails from 5x5 vendor data, achieving 9.1
million new freemail additions including 6.7 million attached to
previously freemail-less contacts. The team also initiated mobile phone
pre-validation processes with comprehensive checklists developed for
accurate mobile validation. This expansion improves coverage for talent
acquisition partners and website visitor resolution use cases.

**Company Cube Release Preparation Advances**: Cam Fortin made
substantial progress toward July company cube release readiness,
targeting final metrics completion by Wednesday and coordinating API
testing for master company API and offline enrichment service. The
release timeline creates urgency with Monday sign-off requirements,
particularly given Cam\'s planned time off the following week. This
progress keeps the quarterly release schedule on track despite
complexity in validation processes.

**Email Confidence Model Testing Advanced**: Hayden Cowell completed the
critical bake-off between email confidence models, testing both an
existing regression model and data science\'s machine learning approach
on 100,000 email samples with real deliverability data. Both models
performed well with confidence scores aligning closely to actual
deliverability, though data science\'s machine learning approach showed
stronger negative skew for identifying high-quality emails. The team is
leaning toward the machine learning model for API implementation but
requires additional team discussions to finalize the decision.

### **Goals & Progress**

**Proactive Privacy Compliance Initiative**: John Durst initiated
critical EU ReachOut data purging to proactively address privacy
compliance following competitor legal action. The team is systematically
removing contact information sourced from EU ReachOut accounts while
preserving legally usable public data from other sources. This proactive
approach protects against potential litigation while maintaining
coverage from legitimate data sources, demonstrating forward-thinking
risk management.

**Contributory Network AI Agent Prototype Development**: Heather Ma
achieved completion on an AI agent prototype that uses a real-data CSV
file to temporarily mock ZoomInfo data via custom data hooks, enabling
realistic testing without direct query. The prototype demonstrates sales
intelligence capabilities including organizational chart analysis,
though development revealed significant challenges in data source
integration across ZDP and BigQuery systems that will inform future
platform development priorities. The goal here is to create a compelling
proof point for Contributory Network acceleration strategy - showing
customers the tangible benefits of deeper integration and network
participation, while establishing a clear upgrade path from base product
to single tenant CRM to co-op network intelligence.

**Customer-Specific Data Analysis**: John Durst completed analysis work
with key customers ServiceNow and Verizon, revealing
better-than-expected coverage in specific market segments. However, this
work highlighted the critical need for automated customer-specific data
performance processes rather than one-off analysis efforts, as the
current approach doesn\'t scale practically across the customer base.

### **Strategic Challenges**

**Form 5500 Data Architecture Requires Rebuild**: Peter Overman\'s
requirements analysis revealed that years of analysis team data
collection and storage doesn\'t align with actual customer use cases,
forcing a complete rebuild of data transformation logic. The dataset
contains 15 different sponsor fields and multiple address configurations
depending on US vs international filings, requiring sophisticated logic
development. While Peter has identified all necessary requirements, the
ground-up rebuild approach could impact Q3 delivery timelines.

**Data Platform Integration Complexity**: Heather Ma\'s AI agent
development exposed significant challenges in data source comprehension
across ZDP and BigQuery systems. The distributed nature of data sources
creates integration complexity, with the most challenging aspect being
understanding data relationships rather than AI model implementation.
This discovery highlights the need for clear best-practice guidance
around data architecture --- including when to build APIs, when to
migrate or duplicate data into the ZoomInfo Data Platform (ZDP), and
whether AI systems should query external sources like BigQuery directly.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Vendor Data Integration Impact**: Rituparna Das\'s successful
processing of 26 million freemails demonstrates the value of systematic
vendor data integration. The achievement of 9.1 million new freemails,
with 6.7 million filling previously empty contact records, shows how
strategic vendor partnerships can improve data coverage and customer
value.

**Privacy Compliance Best Practices**: John Durst\'s proactive approach
to EU ReachOut data purging demonstrates the importance of staying ahead
of regulatory risks in the data industry. The systematic removal of
specific data sources while preserving legitimate coverage shows how
compliance can be achieved without sacrificing data quality when
properly executed.

**Machine Learning Model Advantages**: The email confidence model
comparison revealed that while both regression and ML approaches perform
well, the machine learning model\'s pattern recognition capabilities
make it more effective for emails with limited validation data. This
insight suggests prioritizing ML approaches for confidence scoring
across other data types where traditional rule-based systems may be
insufficient.

**Customer Data Performance Patterns**: John Durst's analysis with
ServiceNow and Verizon revealed that large enterprise customers often
focus on highly specific geographic or industry segments that don\'t
align with overall account patterns. This discovery reinforces the need
for automated customer-centric data performance dashboards rather than
resource-intensive one-off analyses.

### **Cross-Team Dependencies**

Our work with the analysis team on Form 5500 data requires immediate
coordination given the discovery that existing data storage doesn\'t
meet customer use cases. Peter Overman needs sustained analysis team
focus to rebuild requirements from scratch, competing with other
initiatives for limited bandwidth and requiring clear prioritization
from leadership.

The AI agent development work reveals the need for stronger
collaboration with Data Platform teams to address data source
integration challenges. Heather Ma\'s prototype progress demonstrates
potential but requires architectural improvements to scale effectively
across the organization.

## **Looking Ahead**

Next week focuses on finalizing this week\'s advanced initiatives while
addressing the Form 5500 data architecture challenges that could impact
Q3 deliverables.

Rituparna Das will work with analysis to finalize comprehensive coverage
numbers for release notes and pricing considerations while completing
mobile validation processes to extend 5x5 data utility beyond freemails.
Cam Fortin will complete final company cube metrics and coordinate
Monday sign-off processes before planned time off. Hayden Cowell will
continue analysis of the two confidence models and finalize which one
advances to API implementation, working with the person team on
integration planning. Peter Overman will accelerate Form 5500
requirements completion despite the ground-up rebuild, coordinating
closely with the data acquisition team for draft review and potentially
escalating to leadership for resource prioritization decisions. Heather
Ma will continue AI agent development while documenting data platform
integration challenges for future architecture planning.

The successful freemail expansion creates opportunity for similar
systematic vendor data integration across other contact attributes,
while the email confidence model advancement provides a roadmap for
expanding ML-powered confidence scoring across additional data types.

*Source: Team 1-2-3 Operating Framework entries from 06/30-07/03*
