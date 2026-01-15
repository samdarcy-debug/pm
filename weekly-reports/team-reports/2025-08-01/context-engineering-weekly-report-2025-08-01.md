---
id: weekly-context-engineering-2025-31
title: "Context Engineering Weekly Report - August 01, 2025"
type: weekly-report
status: approved
team: context-engineering
owner:
created: 2025-08-01
updated: 2026-01-06
week_ending: 2025-08-01
reporting_period: "July 28-August 01, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Context Engineering Team Executive Roundup - August 1st, 2025**

## **Executive Summary**

The Context Engineering team made critical progress on custom signals
architecture while uncovering fundamental data quality issues that
require strategic resolution. Srivatsa Marthi successfully validated the
custom signals approach with key partner teams, positioning us to
finalize the product review next week. However, Christine Sugimoto\'s
analysis revealed that G2, TrustRadius, and ALI signals have
architectural flaws causing noise and missed insights---issues that will
cascade to any products consuming these signals. With Rowan Bailey\'s
agentic platform demo to executive leadership on August 11th, the team
is balancing immediate sprint needs with longer-term architectural
decisions.

## **This Week\'s Progress**

### **Key Momentum Areas**

Srivatsa Marthi\'s cross-functional alignment on custom signals created
breakthrough clarity, with particularly productive sessions with Mark
from workflows and Sean on copilot V2. This validation work ensures our
architecture will integrate smoothly with partner teams\' roadmaps,
preventing costly rework down the line. The meetings confirmed that
migrating to the go-to-market data model will eliminate many current
flow problems.

Robyn Sablosky made a strategic pivot on explainability architecture,
deciding to embed it within IMS and AFS rather than APS. This
architectural decision better aligns with how customers will actually
interact with our scoring system---when users see an APS score, they\'ll
have full signal visibility through IMS, creating a more intuitive
experience. Despite being under the weather, Robyn advanced critical
groundwork on clickagy table structures.

Rowan Bailey shifted from \"manager mode\" to \"builder mode,\" directly
integrating new data sources into the agentic platform. This hands-on
approach accelerated development as the team sprints toward the August
11th executive demo, demonstrating the platform\'s capabilities to sales
leadership and C-suite stakeholders.

### **Goals & Progress**

**Custom Signals Architecture**: Srivatsa completed 80% of partner team
reviews, with workflows and copilot V2 alignment confirmed. The
remaining admin team sync with Ting Ting isn\'t blocking progress. The
approach validation positions us to conduct the formal product review
and frame the leadership decision on custom signals implementation next
week.

**AI Model Data Strategy**: Robyn identified all PMs involved in
customer onboarding processes while working through clickagy table
outputs. The explainability repositioning to IMS/AFS creates cleaner
architecture but shifts prioritization slightly. Critical questions
remain about data coverage for our models, with mixed reports across the
business about actual availability.

**Signals Documentation & Quality**: Christine progressed on the signals
primer, documenting critical flaws in G2, TrustRadius, and ALI signal
processing. Her analysis revealed that treating continuous data as
discrete creates noise, while timestamp-based selection in ALI causes us
to miss high-magnitude changes---fundamental issues affecting signal
reliability.

### **Strategic Challenges**

Our signals architecture faces a fundamental tension between workbooks\'
need for raw data and copilot\'s need for processed scores. As Srivatsa
noted, \"I understand how to solve for each use case individually. I
don\'t understand the architecture of how to solve for both at once.\"
This architectural challenge requires resolution before we can scale
custom signals across products without creating technical debt or
degraded user experiences.

Data quality issues in core signals threaten downstream product
reliability. Christine\'s discovery that G2 and TrustRadius page visits
are treated as discrete rather than continuous data means a single hit
from a massive enterprise gets the same weight as one from a sole
proprietor. Similarly, ALI\'s timestamp-based selection misses critical
high-magnitude changes, creating blind spots in our intelligence layer.

The uncertainty around actual data coverage for AI models blocks
strategic planning. Despite Nilash and Rowan both noting \"very mixed
reports from across the business of what our coverage actually is,\"
Robyn needs this clarity to design a 12-18 month model strategy. Without
accurate coverage data, we risk building models that can\'t deliver on
customer expectations.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The migration to the go-to-market data model represents a strategic
inflection point for custom signals. Srivatsa\'s investigation revealed
that \"a lot of the problems that we have in the current flow for custom
signals will essentially go away\" with this migration. While not the
long-term happy path due to UX complexity in workflows, it provides a
fast learning path.

Signal literacy emerges as a critical adoption barrier. Robyn\'s
observation that \"most customers will go to IMS first---they\'re not
going to know enough to say \'I want this custom thing\'\" fundamentally
challenges our product strategy. The parent-child relationship between
IMS and individual signals needs careful UX consideration to avoid
overwhelming less data-literate users.

Christine\'s systematic signal analysis revealed that \"every
signal/insight is its own special, sad snowflake\"---each uniquely
problematic. This insight suggests we need signal-specific processing
strategies rather than one-size-fits-all approaches, especially as we
expose raw data through workbooks where RevOps users will unknowingly
create noisy signals.

### **Cross-Team Dependencies**

Our work with the workflows team on custom signals integration remains
critical for Q3 delivery. Mark\'s collaboration with Srivatsa confirmed
technical feasibility, but the UX complexity of the workflows approach
means it can\'t be our primary customer path. We need continued
alignment as both teams evolve their approaches.

The workbooks team\'s AI attributes feature creates both opportunity and
complexity for signals architecture. The fuzzy boundary between custom
signals and AI attributes---both potentially listening for data
changes---requires careful product definition to avoid customer
confusion and technical redundancy.

## **Looking Ahead**

Next week marks a critical convergence of strategic planning and
tactical execution as we finalize the custom signals product review
while supporting the August 11th agentic platform demo.

Srivatsa will complete the custom signals product review, framing the
leadership decision with full partner team input, then pivot to planning
phase 2 signals for the September GA workbooks release. Robyn will
finalize the IMS draft while pursuing clarity on data coverage---without
this, our 12-18 month model strategy remains blocked. Christine will
complete Chapter 2 of the signals primer, providing the definitive
reference for signal quality issues that will guide architectural
decisions.

The team\'s ability to balance immediate demo pressures with
foundational architecture work will determine whether we build lasting
competitive advantage or accumulate technical debt that constrains
future innovation.
