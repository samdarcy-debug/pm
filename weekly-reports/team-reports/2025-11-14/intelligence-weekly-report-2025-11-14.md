---
id: weekly-intelligence-2025-46
title: "Intelligence Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

Intelligence Team Executive Roundup -
[November 10, 2025 - November 14, 2025]

Executive Summary

The team achieved a major cost breakthrough this week with 60% reduction in LLM costs
through prompt caching implementation, though this savings isn't yet passed to customers due
to AI Credit Service limitations. Meanwhile, front-end design for the trigger experience is
progressing with a newly assigned designer, and the first version of the orchestration platform
(00) is ready for production deployment Monday with full M1 tool support. Critical architectural
decisions around semantic data scalability are being evaluated with Milvus showing 2-3x
performance gains over current solutions.

This Week's Progress

Key Momentum Areas

Ryan Stevens and Josh delivered a validated 60% cost reduction through prompt caching
implementation in the Workspace agent, representing substantial progress toward board-level
cost optimization commitments. The team established a reproducible methodology for
measuring hallucination rates using Adam Severance's dataset, shifting focus from anecdotal
33% figures to rigorous evaluation frameworks that distinguish between true hallucinations and
tool selection errors.

Derek Osgood shipped PRDs for admin panel, publishing path, and message broker service
while bringing the first version of the orchestration platform (00) to production-ready status. The
platform now supports full M1 tool functionality including ZoomInfo data queries, Outreach
integration, and workbook creation capabilities, with QA validation complete on all core tools.

Ant's NBA (Next Best Action) agent launched in production as a sub-agent on the Copilot
homepage, demonstrating the team's ability to enable PM-led agent development with minimal
integration overhead. The agent analyzes recent account activity and provides one-click
execution of recommended actions, establishing a replicable pattern for the no-code builder
initiative Lars is resuming.

Goals & Progress

GTM Configuration & Context Architecture: Rowan Bailey made headway on GTM Config
migration strategy, achieving alignment on new navigation structure and object model for
transitioning from Copilot V1 to V2. The discussions surfaced philosophical tensions between
target accounts (admin-defined lists) and account priority score (ML-driven recommendations)
which still needs resolving / leadership input. 8% of semantic data records lack ZoomInfo
Company IDs due to upstream Chorus matching limitations, creating retrieval blind spots that
require investigation - these will be resolved by the semantic data team running their own
matching logic & backfill.

Plays & Triggers Development: Srivatsa Marthi advanced trigger experience requirements
with newly assigned designer Yoav, expecting first draft Monday. The architecture now
separates audience definition into the "run play" step rather than trigger definition, clarifying the
build-run-monitor workflow. Critical blocker remains around CDC event attributes--current
WebSights events lack filtering capabilities needed to prevent volume overload, with ZDP team
meeting scheduled to expand attribute schema.

Semantic Data & Intelligence Layer: Carlos Nunez revealed plans for Intelligence Layer API
with Milvus as leading candidate for scalable vector search, supporting quantization schemes
and tier fetching with sub-100ms retrieval even from disk. Venkata identified quick wins reducing
BigQuery Vector Search costs by migrating from external tables to proper partitioned/sorted
tables. The team continues evaluating against Google Vertex Vector Search per IE
requirements, with James Guyer building an abstraction API to enable seamless backend
swapping.

Scoring & Recommendations: Carlos Nunez and Robyn Sablosky will be working with the
Advanced Search Service to expose scores using position-based classification rather than rank,
with the current grading bands set at 90­100 (A+), 80­89 (A), 70­79 (B+), 60­69 (B), 40­59
(C), and 1­39 (D). Applied AI is reviewing global score distributions to confirm that the cutoffs
behave as expected across tenants before finalizing the thresholds.

Strategic Challenges

Semantic data model upgrades face unexpected complexity as the team transitions to Sonnet
4.5 with updated ontology, observing significant drops in entity extraction volume without clear
root cause. This requires investigation to ensure the latest models and ontology deliver
expected improvements in context quality. Previous Haiku limitations around ID tracing and
relationship mapping may warrant reassessment given recent model advances, as Lars
suggested.

AI Credit Service cannot yet consume cached tokens, meaning the team's 60% cost reduction
achievement isn't reflected in customer value or billing. Ryan Stevens initiated a project to
enable proper token reporting, but this represents a gap between engineering wins and
business outcomes that needs near-term resolution to fulfill board commitments on cost
optimization.

Cross-UX orchestration resourcing remains unresolved despite Derek's progress on PRDs and
platform readiness. The alignment needed between Agentic platform and orchestration engine
requires dedicated engineering capacity beyond current allocations, creating potential
bottleneck for December-January roadmap execution as multiple teams prepare to leverage the
shared infrastructure.

Strategic Insights

Key Learnings & Discoveries

The hallucination debate this week surfaced critical insights about evaluation rigor and
organizational communication. Robyn's findings that 33% of failures involve hallucinations was
misrepresented in executive summaries as "33% of chats hallucinate"--a significant distortion.
Adam Smith articulated technical definitions distinguishing true hallucinations (novel tokens not
in input, broken semantic links) from tool selection competency issues, emphasizing that most
problems stem from the latter. The team's pivot to measuring error rates across the
precision-to-hallucination spectrum using Adam Severance's dataset represents a maturation in
evaluation methodology.

The Ant NBA agent integration validated the sub-agent delegation pattern at production scale.
Ant independently built, burned in, and QA'd the entire agent with minimal platform team
involvement, demonstrating that the architecture successfully enables PM-led development.
This model will inform the no-code builder Lars is resuming, where artifact creation automatically
spins up isolated agents with configurable tools, templates, and instructions that integrate as
sub-agents to SalesOS, Workspace, or Studio.

Vector database selection demands careful evaluation given long-term scaling implications.
Adam Smith's experience implementing Pinecone, PGVector, and others highlighted tradeoffs:
PGVector works well for fixed datasets with simple retrieval but struggles with clustering indexes
and operational complexity at scale. Milvus's architecture-specific optimizations (GPU/TPU/x86
SIMD support) and comprehensive FAISS index support make it compelling despite operational
complexity that deterred the IE team. The mandate for comparison against Google Vertex
Vector Search reflects wise diligence before committing to infrastructure that must scale to
millions of tenants.

Cross-Team Dependencies

Robyn's involvement in web search quality improvements adds another coordination point
requiring clear ownership boundaries.

The ZDP team meeting scheduled today addresses the urgent CDC event attribute expansion
needed for trigger filtering. Without additional attributes flowing through change events, the
Plays system cannot filter WebSights visits by page or other criteria, forcing either
unmanageable trigger volume or delayed launch. This dependency affects Srivatsa's front-end
design completion and Derek's overall Plays delivery timeline.
The AI Credits team roadmap became highly pliable post-launch, creating opportunity to inject
prompt caching token reporting requirements. Ryan Stevens' scoping work should receive
prioritization given board-level commitments around cost reduction, making this a strategic
dependency worth elevating if resistance emerges.

Looking Ahead

Next week centers on three critical convergence points: finalizing orchestration platform
integration strategy, completing trigger experience design for engineering handoff, and
advancing the evaluation framework to production readiness.

Lars, Derek, and Adam will clarify how the Agentic platform and orchestration engine unite,
unblocking December-January roadmap execution across multiple dependent teams. Derek
continues M1 tool expansion while Srivatsa closes trigger design with Yoav and resolves CDC
attribute requirements with ZDP. Ryan Stevens delivers hallucination measurement
methodology, Lauren demos evaluation framework capabilities, and the ChatKit team
progresses on human-in-loop implementation after their inaugural week.

The team maintains momentum despite juggling architectural decisions with significant
long-term implications--vector database selection, context service design, orchestration
patterns--while shipping incremental improvements in cost, quality, and capability. The
challenge ahead involves maintaining delivery cadence while ensuring foundational choices set
the stage for scalable, maintainable growth through 2026.

Source: Team Intelligence Operating Framework entries from [November 10, 2025 - November
14, 2025]
