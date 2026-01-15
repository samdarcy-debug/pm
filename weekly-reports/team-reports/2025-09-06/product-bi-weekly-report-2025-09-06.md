---
id: weekly-product-bi-2025-36
title: "Product BI Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

**Product BI Team Executive Roundup - September 5, 2025**

**Executive Summary**

Session recordings and heatmaps remain blocked by technical issues with
Amplitude, preventing rollout of critical user behavior analytics to PM
and design teams. While Vermont\'s team advances Copilot V2 tracking
preparation and Nanxi uncovers early churn predictors in integration
customer patterns, AJ\'s primary initiative faces multi-week delays
pending vendor resolution.

**This Week\'s Progress**

**Key Momentum Areas**

Vermont\'s team completed the draft workflow for Copilot V2 CRM data
entry and aligned with Rashan on partner metrics and business questions.
They\'re now developing AI chat flow tracking with Sean to ensure
comprehensive event capture for September\'s feature launches,
positioning analytics readiness ahead of product deployment.

Nanxi discovered a powerful early risk predictor in integration customer
behavior, finding that churn versus renewal patterns diverge as early as
months 4-5 in contracts. Both cohorts show similar onboarding
trajectories, but renewal customers continue engagement growth while
churn customers plateau, validating the \"6 months before contract end\"
churn prediction theory with concrete data evidence.

Ferrell began investigating export volume patterns for integration
customers approaching contract renewal, establishing a new analytical
dimension to complement existing import tracking. This work, once
unblocked from CDP data issues, will provide bidirectional usage
intelligence for the Customer Success team.

**Goals & Progress**

**User Behavior Analytics**: AJ\'s session recording and heatmap
initiative remains blocked by Amplitude technical issues where 80-90% of
recordings capture only 1-3 seconds before disconnecting. Support
tickets are active, but resolution timeline uncertain, preventing
planned PM org enablement and training materials development.

**Copilot V2 Analytics Preparation**: Vermont is systematically mapping
business questions and tracking requirements for upcoming feature
launches, working directly with engineering teams to ensure proper event
instrumentation. Next week involves collaboration with Inbal on
implementation validation and Sean on feature-specific tracking
requirements.

**Integration Customer Analysis**: Nanxi shifted analysis timeframe from
January-July to avoid August data corruption issues caused by irregular
monthly refresh cycles. The team identified accounts showing churn in
August despite active renewals, leading to discovery of data freshness
problems affecting renewal prediction accuracy.

**Strategic Challenges**

CDP data connectivity issues are blocking multiple analytical
workstreams, affecting both Ferrell\'s export analysis and Tableau
integration reporting. The CDP team attributes problems to Tableau
configuration, while Tableau support points to CDP-side issues, creating
a resolution bottleneck that impacts customer usage pattern analysis and
automated reporting pipelines.

Event tracking granularity gaps limit analytical depth for AI chat
engagement, with current instrumentation capturing chat launches but
missing entry point context (homepage, opportunity view, etc.). Vermont
is coordinating with Sean to identify engineering resources for enhanced
property implementation before September feature launches.

Core engagement data contains anomalous patterns showing customer
imports beginning 2+ years before contract start dates, potentially from
demos or trials but requiring investigation to ensure accurate
onboarding timeline analysis. Large pre-contract volumes could indicate
data categorization issues affecting customer lifecycle measurements.

**Strategic Insights**

**Key Learnings & Discoveries**

Customer churn signals emerge much earlier than expected, with
divergence patterns visible in months 4-5 rather than the commonly cited
6 months before renewal. This finding validates early intervention
strategies and suggests Customer Success teams should intensify
engagement during the post-onboarding stabilization period when renewal
customers typically accelerate usage while at-risk accounts plateau.

Data refresh timing significantly impacts analytical accuracy, with
monthly updates creating false positive churn signals when contract
renewals occur between refresh cycles. Nanxi\'s investigation revealed
that seemingly churned customers had actually renewed seamlessly,
highlighting the need for more frequent data updates or buffer periods
in churn analysis methodology.

Session recording quality directly correlates with heatmap reliability,
as Vermont discovered when investigating seemingly nonsensical click
patterns concentrated at page tops. The 1-3 second recording failures
explain heatmap distortions, emphasizing the importance of foundational
data quality before rolling out analytical tools to broader teams.

**Cross-Team Dependencies**

Our work with the engineering teams on Copilot V2 tracking
implementation requires clear prioritization frameworks for event
instrumentation requests. Vermont is developing specific business
justifications for each tracking enhancement to help Sean allocate
development resources effectively while ensuring September launch
readiness.

The CDP and Tableau integration challenges highlight the critical nature
of reliable data pipeline maintenance for ongoing analytical operations.
Multiple team members are blocked pending resolution, suggesting the
need for escalated technical support coordination or alternative data
access strategies.

**Looking Ahead**

Next week focuses on analytical preparation and data quality resolution,
with three parallel workstreams advancing despite current technical
obstacles.

Vermont and Inbal will collaborate on Copilot V2 tracking validation and
business question mapping, ensuring comprehensive event capture for
September features while working with Sean on engineering resource
coordination. AJ will review renewal prediction analysis with Vermont
once fresh data becomes available, then develop presentation materials
for the upcoming ELT meeting with Mary, Whitney, and Victor. Meanwhile,
Nanxi will complete data cleaning and outlier removal for the
integration customer analysis, transforming current visualizations into
executive-ready insights while Ferrell investigates export patterns and
conducts CSM sample checks to understand delayed activation drivers.

The team remains positioned to deliver significant analytical value once
current technical obstacles resolve, with strong preparation work
ensuring rapid deployment of user behavior analytics and comprehensive
Copilot V2 measurement frameworks.

*Source: Data Analytics Team Meeting - September 5, 2025*
