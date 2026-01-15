---
id: weekly-semantic-data-2025-45
title: "Semantic Data Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Semantic Data Team Executive Roundup - November 7, 2025**

## **Executive Summary**

Venkata completed a comprehensive architecture assessment and proposed a
scalable redesign that will cut embedding generation costs by 50%
through Anthropic batch API calls and eliminate multi-cloud complexity
by consolidating the entire pipeline into GCP. The team is now executing
a parallel migration strategy---maintaining current operations while
building a more efficient system that reduces data hops and enables
GPU-accelerated embedding generation through Vertex AI. This 6-8 sprint
initiative positions the semantic data infrastructure for
enterprise-scale deployment while Jon and Inga maintain tenant quality
during the transition.

## **This Week\'s Progress**

### **Key Momentum Areas**

Venkata delivered a detailed migration plan that addresses critical
scalability bottlenecks in the current semantic data pipeline. The
proposal eliminates unnecessary data transfers between clouds and
Postgres intermediaries, moving to a pure GCP architecture using
BigQuery for batch embeddings and exploring Milvus for real-time vector
storage. This consolidation enables 50% cost reduction through batch API
processing while maintaining quality through continued use of Anthropic
models.

Jon focused on operational continuity, conducting knowledge handoffs
from Danny to ensure smooth tenant onboarding and pipeline optimization.
His work maintaining current system stability creates the runway needed
for Venkata\'s architectural migration, preventing any service
degradation while the team executes the parallel build strategy.

Sai made progress provisioning a Milvus cluster for vector database
evaluation, preparing to test whether it outperforms BigQuery for
embedding storage on latency and quality metrics. This evaluation runs
parallel to the main migration path, offering potential operational
improvements that can be adopted through straightforward data migration.

### **Goals & Progress**

**Infrastructure Consolidation**: Venkata mapped the complete migration
path from the current multi-cloud architecture to a GCP-native system.
The plan preserves the existing system intact while building new
pipelines that eliminate Postgres intermediaries and AWS data hops. The
team will run both systems in parallel until confident in the new
infrastructure\'s stability, then gradually migrate agents to the new
BigQuery tables. This approach minimizes risk while delivering
substantial efficiency gains.

**Operational Stability**: Jon maintained pipeline quality and tenant
onboarding processes during significant team transition. His knowledge
transfer work with Danny ensures continuity as the team composition
shifts, while his focus on tenant quality metrics keeps the current
system healthy. This operational discipline creates the stable
foundation required for executing architectural changes without customer
impact.

**Vector Database Evaluation**: Sai advanced Milvus cluster provisioning
and is now pushing evaluation data to test against production
requirements. This parallel workstream provides optionality---if Milvus
demonstrates clear advantages over BigQuery for vector storage on
latency and retrieval quality, the team can migrate with minimal
friction since the data formats remain compatible.

### **Strategic Challenges**

The team identified a potential data quality issue where Claude 4.5 may
be extracting more entities than currently appear in the knowledge
graph. Jon observed that API responses indicate 40 entities and 80
relationships being found, but validation logic prevents storage when
the graph structure isn\'t valid. This creates a blind spot where
apparent volume reduction might actually reflect overly aggressive
validation rather than extraction problems. The team needs to analyze
Datadog logs to understand which entity types trigger validation
failures and adjust either prompting or validation logic accordingly.

The 2048-dimension limit in BigQuery\'s vector implementation raises
concerns about retrieval quality. While this constraint could impact the
semantic matching capabilities that drive agent performance, the team
has contingency options including Rayscale for GPU-accelerated
embeddings or custom model hosting through Vertex AI. The dimensional
limitation isn\'t a blocker since the architecture supports alternative
embedding approaches if evaluation reveals quality degradation.

The 6-8 sprint timeline for complete migration requires careful resource
allocation and sequencing. Venkata needs engineering capacity to execute
multiple parallel workstreams---batch processing migration,
near-real-time pipeline redesign, and BigQuery table schema
implementation. The team is allocating resources aggressively but must
balance migration work against operational maintenance to avoid service
disruption.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The architecture review revealed excessive data movement creating both
cost and latency penalties. Data currently flows from BigQuery to
Postgres to BigQuery in different projects, with multiple cloud
transfers in between. Venkata\'s analysis showed these hops exist due to
historical evaluation of AlloyDB that never concluded decisively.
Eliminating these intermediaries by processing embeddings directly in
BigQuery where source data already lives dramatically simplifies the
system while improving performance.

The team discovered that validation logic may be masking rather than
revealing quality issues with Claude 4.5. Rather than accepting apparent
entity volume reduction at face value, Jon\'s investigation into API
response counts versus stored entities suggests the model is extracting
appropriately but downstream validation rejects valid graphs due to
overly strict matching rules. This insight shifts the diagnosis from
model capability questions to data quality validation tuning.

Consolidating to GCP unlocks capabilities beyond cost reduction. Running
the full pipeline in a single cloud environment enables straightforward
use of Vertex AI for hosting alternative embedding models if needed,
provides access to managed GPU infrastructure through Rayscale for
acceleration, and creates a standardized embedding cookbook that other
Applied AI teams can adopt. This strategic positioning extends beyond
immediate technical benefits to organizational capability building.

### **Cross-Team Dependencies**

Carlos emphasized coordination with Applied AI org on embedding
standards and infrastructure patterns. The Milvus evaluation and
potential Rayscale integration represent opportunities to establish
common tooling across multiple teams working on semantic and vector
search problems. Venkata\'s migration plan deliberately preserves
flexibility to adopt shared infrastructure decisions rather than locking
the semantic data team into isolated technical choices.

## **Looking Ahead**

The team enters an 8-12 week migration period focused on building the
new GCP-native pipeline while maintaining operational quality in the
existing system. Success requires parallel execution across multiple
fronts---Venkata architecting the new data flows, Jon maintaining tenant
quality and addressing the entity validation issue, and Sai completing
vector database evaluation to inform storage layer decisions.

Next week, Jon and Inga will investigate the entity extraction
validation mismatch by analyzing Datadog logs to identify which entity
types and relationships trigger failures. This analysis should reveal
whether prompting adjustments or validation logic changes can unlock the
full extraction capability that API responses suggest exists. Sai will
complete Milvus evaluation metrics and coordinate with Venkata on batch
processing architecture decisions---specifically whether embeddings
should flow directly to Milvus or through intermediate BigQuery storage.

The team\'s ability to execute this transition smoothly while
maintaining service quality will establish the scalable foundation
needed for enterprise semantic data deployment. Venkata\'s phased
migration approach minimizes risk by keeping current systems operational
until new infrastructure proves stable, giving the team confidence to
move deliberately rather than rushing changes that could impact customer
experience.
