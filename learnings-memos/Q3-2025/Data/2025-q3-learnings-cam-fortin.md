---
id: learnings-2025-005
title: Q3 2025 Learnings Memo - Cam Fortin
type: doc
status: approved
team: data
owner: '[[teams/data/_people/cam-fortin]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- data
related: []
---
## **Metric Alignment**



Our Q3 work (June-October) directly advanced both **Company Coverage

Rate** and **Company Perfect Accuracy Rate** north star metrics through

major initiatives across both cube releases:



**Coverage expansion:** Added 2.4M total companies (1.15M Tier A) across

July and October releases. July delivered 500K companies (200K Tier A)

from customer search patterns, while October added 1.9M companies (950K

Tier A) through continued customer-driven expansion (1.4M total) and

international partnerships (500K). Customer calls with Uber, Palo Alto

Networks, and RedHat confirmed this directly addressed their most

frequent pain point---missing prospects in LATAM, EMEA, and APAC markets

they knew existed but couldn\'t find in ZoomInfo.



**Accuracy improvements:** Executed our largest location quality

initiative ever, impacting 10M+ location records across both releases.

July systematically removed 3.3M problematic locations across 883K

companies and corrected 750K company records with address quality

issues. October achieved 95%+ accuracy for Fortune 1000 company

locations through human validation, corrected 68K addresses via

LLM-based normalization, and removed 1.3M duplicate/problematic company

records. Optimum\'s feedback (\"Ultimate Test: can your locations be

spot on?\") validated this as critical blocking issue for enterprise

territory planning.



**Quality foundation:** Separated 602K overcombined source records (96%

accuracy), corrected 16K invalid phone numbers, and updated corporate

hierarchies for 50K companies. Completed enhanced tiering rollout in

July affecting 2.15M companies (150K from Tier A→C in \>50 employee

cohort, 1M from Tier B→C through improved inactive identification).

These changes represent fundamental shift toward systematic quality

maintenance rather than reactive cleanup---addressing Autodesk\'s

concern about companies incorrectly profiled across unrelated

industries.



## **Key Learnings**



**What everyone in product needs to know about our customers this

quarter:**



1.  **Industry misclassification undermines trust in all other data.**

    Autodesk showed manufacturing companies classified as \"Photography

    Studios\"---when core taxonomies are wrong, customers question

    everything else. Industry accuracy is a trust foundation, not just a

    targeting feature.



2.  **Customers are building AI tools that could commoditize our

    value.** Autodesk built \"AI Based Prospect Qualification

    Automation\" using our name/website then generating everything else

    with LLMs. If our core data isn\'t demonstrably superior to what

    customers can scrape, we risk becoming an expensive directory.



3.  **International coverage is market-specific, not universal.**

    Customers want strategic depth in their expansion markets (APAC for

    Palo Alto, LATAM for Uber, Japan/developing EMEA for Autodesk), not

    broad shallow coverage.



## **Hypotheses & Results**



**H1: Cross-functional collaboration can overcome technical constraints

to deliver company creation at scale**



- **Hypothesis:** If we get the right group of people together we can

  add significant companies to the database even with sources frozen and

  \"boil the ocean\" merge creating issues that caused us to pause

  company creation



- **Result:** VALIDATED. Despite frozen sources and merge complications,

  collaboration between company team, WDA, research, and analysis teams

  delivered 2.4M new companies (1.15M Tier A) across July and October

  releases. July\'s 500K companies (200K Tier A) from unmatched domains

  proved the concept, October\'s 1.9M (950K Tier A) scaled it.



- **Nuance:** Success required significant manual coordination and

  \"babysitting\" throughout pipeline. This isn\'t sustainable long-term

  but proved we could deliver results while waiting for infrastructure

  improvements. International expansion (500K companies via

  partnerships) showed different collaboration model also

  works---strategic data acquisition with external partners, not just

  internal processes.



**H2: Web-based location extraction can replace most existing location

sources**



- **Hypothesis:** Automated crawling and extraction could systematically

  verify and replace locations for majority of our database, quickly

  improving data quality through owned technology



- **Result:** PARTIALLY VALIDATED. Successfully processed 3.7M of 20M

  Tier A companies (18.5% of target) with excellent cleanup

  results---added 1M verified locations while removing 4.8M problematic

  ones we knew were bad (net -3.8M was actually positive outcome). The

  validation and cleanup worked as hoped for the 3.7M cohort. However,

  couldn\'t expand beyond small company segment (\<50 employees, \<10

  locations) due to technical extraction limitations: 12% of

  \"HQ-tagged\" locations in multi-address extractions were unrelated

  addresses on websites (contact forms, press mentions, partner

  locations), and crawl capabilities insufficient for

  large/complex/JavaScript-heavy websites.



- **Nuance:** The hypothesis succeeded for its target cohort but failed

  on \"most existing location sources\" ambition. Extraction works

  excellently for simple websites (95%+ accuracy for single-location

  companies with clear address listings), enabling systematic cleanup we

  were excited to execute. Three barriers prevented broader

  application: 1) Over-extraction from complex sites (franchise

  networks, healthcare systems) made us conservative about expanding, 2)

  Under-extraction from JS-heavy modern websites limited complete

  coverage even where we tried, 3) Ambiguity in determining which

  extracted addresses actually represent company locations vs.

  incidental mentions. We proved the concept works for straightforward

  cases but can\'t yet scale to comprehensive database replacement.



**H3: Targeted data acquisition paired with tool upgrades enables

international company creation**



- **Hypothesis:** Strategic regional partnerships combined with DIP

  platform improvements and process optimization would unlock systematic

  international company creation



- **Result:** VALIDATED. Added 500K international companies (260K

  Tier A) through LATAM and EMEA partnerships---220K LATAM (70K Tier A)

  and 290K EMEA (190K Tier A). DIP integration with research team

  enabled streamlined workflow from source acquisition → validation →

  creation without requiring manual ETL intervention for each batch.



- **Nuance:** Success heavily dependent on data partner quality and

  regional market characteristics. Brazil and Germany partnerships

  delivered 75%+ Tier A conversion, while Eastern Europe and some LATAM

  countries dropped to 30-40%. Customer calls (Autodesk, Uber, Palo

  Alto) revealed we\'re still missing strategic depth in key markets:

  Japan needs 20-30K companies but we have 3K (85% gap). Tool upgrades

  necessary but not sufficient---market selection and partner vetting

  are equally critical.



**H4: Industry misclassification is primarily a model accuracy problem

solvable through better ML approaches**



- **Hypothesis:** New DS-powered industry model could systematically

  improve classification accuracy across ZI Industry, SIC, and NAICS

  taxonomies, addressing customer complaints about misclassifications



- **Result:** PARTIALLY VALIDATED. New model shows strong improvement

  potential (targeting 80% ZI Industry precision, 70% NAICS precision),

  but implementation complexity exceeds initial expectations. Discovered

  that rolling out improvements requires careful phasing to minimize

  customer disruption---even accurate changes create workflow issues for

  enterprise customers with planning built on existing values. Also

  revealed data source quality issues (overcombined companies, incorrect

  source attributions) contribute significantly to misclassifications

  beyond pure model accuracy. More details in Q4 plan below, but we have

  a phased implementation plan that enables us to use the model on new

  companies and also address the most urgent cohorts of existing

  companies quickly without shifting values "too much too fast".



**H5: Fixing overcombination through source removal will improve match

accuracy and unlock \"trapped\" domains**



- **Hypothesis:** Systematic removal of low-quality sources causing

  overcombination would both clean up existing company profiles AND

  liberate domains for future company creation



- **Result:** MIXED. Successfully cleaned up 602K source records

  affecting 280K companies (96% accuracy in identifying problematic

  sources). Match accuracy improved as duplicate/incorrect domain

  associations were removed. However, liberated domain→new company

  creation underperformed expectations---couldn\'t create many new

  companies from separated URLs due to inactive domains and crawl

  limitations. Cleanup value was real and substantial, but

  forward-looking \"unlock trapped domains\" benefit didn\'t materialize

  at anticipated scale.



- **Nuance:** Overcombination patterns concentrated in specific

  industries (real estate, healthcare, franchises = 60% of issues

  despite \<20% of database), suggesting systematic problems with how we

  define \"company\" for certain business models. The separation work

  was valuable for data quality even without new company

  creation---proper company profiles matter for matching, targeting, and

  customer trust. But hypothesis that cleanup would fuel significant

  company creation proved too optimistic about domain viability and our

  extraction capabilities.



## **Go-Forward Changes & Plan**



**Q4 Priorities (based on customer feedback and Q3 learnings):**



1.  **Industry classification deployment and integration.** Complete

    Phase 1.1 integration into DIP for automated batch predictions on

    new companies and manual industry updates for existing company

    cohorts. Target problematic industries first (Photography Studios,

    Fitness Centers appearing for manufacturing companies) through batch

    reclassification files. Integrate model into Company 3.0/M8 pipeline

    to ensure new model is live when M8 launches in January.



2.  **Strategic international expansion with language capabilities.**

    Target customer-specified markets: Japan (85% coverage gap),

    developing EMEA (Estonia, Luxembourg, Latvia, Lithuania, Romania,

    Slovakia, Croatia, Slovenia), and APAC depth (India, Australia/NZ,

    rest of Asia). Add 600K-1M companies through Rhetorik and WDOD

    partnerships. Partner with WDA on non-English language support and

    translation capabilities---critical unblocking work for markets

    where we \"Cannot Translate/Match Non-Latin Characters.\"



3.  **Expand location quality through new verified sources and targeted

    cohort expansion.** Pivoted from automated WDA location ingestion

    across entire database to strategic approach combining new

    deterministic sources (Mastercard retail locations, Zipi

    verification data) with careful cohort-by-cohort WDA application. Q3

    revealed extraction technology works well for simple company

    websites but over/under-extracts for complex cases, requiring

    analysis-driven identification of which company segments can

    reliably use automated extraction. Continue Fortune 1000 human

    validation while building infrastructure for verified location

    confidence scoring.



4.  **Systematize customer-driven company creation through DIP

    automation.** Build automated pipeline from unmatched search domains

    → WDA crawling → validation → DIP creation, moving away from

    quarterly manual batches. Implement parallel job processing, crawler

    automation with queue prioritization, and standardized scoring

    framework. Q3 proved customer search patterns convert at 49% Tier A

    rate (2-3x other sources)---automation will scale this capability.



5.  **Company 3.0 foundation and M8 launch preparation.** Complete

    remaining profiler definitions and C2/C3 usage breakpoints

    documentation. Finalize M8 automated new company creation

    integration and ensure feature continuity from 2.0. Launch

    incremental cube (M7.2) with location-based search and clean cube

    schema for new customers without deprecated fields.



**Additional Strategic shifts based on customer intelligence:**



- **Revisit HQ tiering and certified active logic.** Decouple website

  status (vitality) from description requirements to increase

  description fill rates. Add verified location sources (WDA crawl,

  Zipi, Mastercard) as inputs to certified active date with 365-day

  cutoff. Don\'t mark companies Tier A if we have no way of validating

  they exist.



- **Transfer model ownership to Data Science.** EGR rollback

  demonstrated urgent need---move responsibility for EGR, headcount,

  revenue, and similar company models to DS team with proper maintenance

  cycles.



## **Leveraging AI**



**Most impactful use:** Built custom industry model validation tool that

queries Snowflake for company data, processes it through new DS model

endpoint, and enables side-by-side comparison of new vs. existing

industry classifications with interactive exploration capabilities. This

dramatically accelerated model validation and helped identify specific

misclassification patterns (like Photography Studios issue) that would

have taken weeks to discover through manual analysis.



**Critical deployment constraint discovered:** Tool only runs locally,

which severely limited value. Couldn\'t share with research team for

distributed validation, couldn\'t run automated nightly comparisons,

couldn\'t enable stakeholders to explore results themselves. We lack

internal infrastructure to deploy apps with necessary capabilities

(Snowflake access, API endpoints, interactive visualization). I believe

these challenges will be solved in Q4.



**Key insight from customer behavior:** Autodesk built \"AI Based

Prospect Qualification Automation\" that scrapes websites and uses LLMs

to qualify prospects---essentially using us for \"name and website\"

then generating everything else themselves. This revealed AI is

commoditizing basic data enrichment. Our competitive advantage isn\'t AI

capabilities (customers can build those), it\'s systematic validation at

scale that customers can\'t replicate: deterministic verification

infrastructure, comprehensive quality checks across millions of records,

and training data customers don\'t have access to.



**Q4 expansion plans:**



1.  **DQI triage agent:** Automatically categorize and route data

    quality issues, reducing research team manual work by 40-50%.

    Particularly important as customer feedback volume increases.

    (Dependent on new ZI Agentic capabilities I think will be coming

    online in Q4)



2.  **Industry classification batch validation:** Productionize local

    tool into shared service. Use LLM to review company descriptions +

    web content, flag potential misclassifications for research review.

    Prioritize Autodesk\'s problematic industries (Photography Studios,

    Fitness Centers appearing for manufacturing companies) for rapid

    correction.



3.  **Non-English content extraction:** Partner with WDA on LLM-based

    translation and entity extraction for Japanese, Eastern European

    markets. Autodesk feedback that we \"Cannot Translate/Match

    Non-Latin Characters\" shows language processing blocks

    international expansion more than data availability.



**Strategic lesson** **learned:** AI\'s value multiplies when tools are

shareable. My industry validation tool would have 10x impact if research

team could run their own analyses, stakeholders could explore results

directly, and automated jobs could run nightly comparisons. Q4 priority

is solving deployment/sharing infrastructure, not just building more

local prototypes. The bottleneck shifted from \"can we build AI tools?\"

to \"can we operationalize them?\"

