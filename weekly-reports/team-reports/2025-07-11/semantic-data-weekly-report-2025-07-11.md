---
id: weekly-semantic-data-2025-28
title: "Semantic Data Weekly Report - July 11, 2025"
type: weekly-report
status: approved
team: semantic-data
owner:
created: 2025-07-11
updated: 2026-01-06
week_ending: 2025-07-11
reporting_period: "July 7-11, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Semantic Data Team Executive Roundup - July 11, 2025**

## **Executive Summary**

The agentic platform achieved critical velocity this week with multiple
production workstreams converging---API runs now trigger successfully
with data fills largely operational, while Inga Isakov\'s cost analysis
revealed that iterative batch processing extracts significantly more
entities than full-thread processing at comparable cost. Two immediate
priorities require executive attention: new tenant onboarding
architecture decisions need rapid finalization as demand accelerates,
and the Deep Web Research agent development by Josh Mantovani unlocks
compound AI capabilities but requires architectural choices between
existing frameworks versus custom implementation.

## **This Week\'s Progress**

### **Key Momentum Areas**

Danny Pan successfully triggered API runs with data fills now largely
operational, marking our transition from manual to automated
processing---though intermittent box crashes during populate_graph
operations require debugging to achieve full reliability. The system now
processes under 70K accounts with 3-month rolling data coverage
approaching 50%, positioning us for scale testing next week.

Inga Isakov\'s comparative analysis of full-thread versus batch
processing revealed a breakthrough: iterative daily batching extracts
significantly more valid entities with minimal duplication while
maintaining cost parity. This discovery fundamentally changes our
approach to context extraction, with 10 additional examples queued for
validation before locking the prompt structure by end of next week.

Josh Mantovani demonstrated structured LLM outputs within the agentic
platform, eliminating dependency on the semantic data API while
establishing foundation capabilities for all future agents. His basic
search agent now handles compound queries with decomposition and
multi-step web scraping, though depth limitations require the custom
Deep Research implementation currently underway.

### 

### 

### **Goals & Progress**

**Data Pipeline Infrastructure**: Danny Pan achieved 90% completion on
API automation, with data fills operational but experiencing stability
issues during graph population phases that cause box restarts. The
switch from manual account ID blocks to file-based processing remains
pending for next week\'s testing, alongside production automation setup
targeting regular updates.

**Cost-Optimized Entity Extraction**: Inga Isakov validated that batch
processing by date delivers superior entity extraction compared to
full-thread analysis at equivalent cost---a finding that challenges our
original architectural assumptions. Initial samples show minimal
duplication with significantly higher entity capture rates, particularly
for entities mentioned before becoming active participants in threads.

**Agentic Platform Capabilities**: Josh Mantovani completed the basic
search agent with query decomposition and web scraping, while structured
output implementation unlocks quality improvements across all agents.
The Deep Research agent extension requires custom implementation after
existing frameworks (LangGraph, platform React agents) showed either
instability or quality limitations incompatible with our requirements.

### **Strategic Challenges**

The new tenant onboarding process lacks critical documentation with
Danny Pan confirming only two requirements identified: ZI tenant ID
lookup and Passive Login Service integration. With Rowan Bailey flagging
this as becoming \"high priority very quickly,\" the team needs
immediate architectural decisions on whether to implement tenant-level
permissions (currently unsupported) or rely on admin user impersonation
with its inherent risks when personnel change.

Database connection limitations surfaced in development environment
testing, with Danny encountering \"out of connections for
non-replication users\" errors that block automated testing expansion.
The sporadic nature (single occurrence) makes root cause analysis
difficult, but resolution is critical before scaling to production
loads.

Josh Mantovani\'s evaluation of existing agentic frameworks revealed
fundamental limitations requiring custom implementation of the Deep
Research agent---a decision that trades development velocity for quality
and control. After testing LangGraph\'s React agent and internal
platform options, each showed either \"bugginess and odd behavior\" or
\"low quality results\" that couldn\'t be resolved within reasonable
timeframes.

## 

## 

## **Strategic Insights**

### **Key Learnings & Discoveries**

Inga Isakov\'s discovery that iterative batch processing outperforms
full-thread analysis represents a paradigm shift in our entity
extraction approach. By narrowing context windows while maintaining
output token expectations, the system extracts more valid entities that
full-thread processing misses---validated through manual review of
additional entities as legitimate rather than noise.

The distinction between \"mentioned\" versus \"participant\" entities
emerged as a critical insight during Inga\'s duplication analysis. When
names appear in threads before those individuals join as participants,
our current system creates apparent duplicates that actually represent
different relationship states---suggesting we need entity type
segmentation to capture this nuance for sales intelligence applications.

Josh Mantovani\'s framework evaluation journey validates our \"build
versus buy\" decision framework: when multiple established solutions
fail quality or stability requirements, custom implementation becomes
the optimal path despite higher initial investment. His structured
output breakthrough simultaneously demonstrates how foundational
capabilities multiply value across all platform agents.

### **Cross-Team Dependencies**

Integration with the broader agentic platform ecosystem accelerated this
week with Josh Mantovani noting shared requirements for the Passive
Login Service client across teams. While Danny Pan plans to copy rather
than directly integrate code, this duplication pattern suggests
opportunity for shared libraries as Rowan Bailey and Josh
discussed---particularly as more teams need similar authentication
capabilities.

The pending Inference Service fork remains unassigned despite its
critical role in supporting structured outputs across the platform. Josh
Mantovani\'s local implementation provides interim capability, but
production deployment requires coordinated handoff to ensure his
technique or equivalent functionality transfers to the centralized
service without regression.

## **Looking Ahead**

Next week pivots toward production hardening with Danny Pan
transitioning from manual to file-based account processing while
investigating the box crash patterns that currently require manual
intervention---resolution unlocks true automation at scale.

Inga Isakov will analyze 10 additional examples to validate the batch
processing advantage before finalizing prompt structures by week\'s end,
with Rowan Bailey requesting detailed documentation via Confluence and
demonstration recordings to cascade learnings across teams. This
methodology lock enables production implementation planning.

Josh Mantovani continues Deep Research agent development with custom
implementation path chosen, while scheduling knowledge transfer with web
research teams to ensure we\'re not duplicating existing capabilities.
His structured output patterns need documentation for platform-wide
adoption as teams migrate from semantic data API dependencies.

*Source: Semantic Data Team Weekly Wrap-up - July 11, 2025*
