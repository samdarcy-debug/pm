---
id: weekly-intelligence-2025-28
title: "Intelligence Weekly Report - July 11, 2025"
type: weekly-report
status: approved
team: intelligence
owner:
created: 2025-07-11
updated: 2026-01-06
week_ending: 2025-07-11
reporting_period: "July 7-11, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Intelligence Team Executive Roundup - July 11, 2025**

## **Executive Summary**

The Intelligence Team achieved critical momentum this week on three
fronts: copilot v2 prototype development targeting Monday delivery, 50%
completion of semantic data processing down to \$70K accounts, and
architectural clarity on context engineering that will accelerate agent
development. The decision to defer centralized context service
development in favor of rapid agent prototyping represents a short-term
pivot that will enable faster learning cycles while supporting August &
September release. Cross-functional alignment with workbooks and
profiles teams positions us for unified product demonstration to
leadership next week.

## **This Week\'s Progress**

### **Key Momentum Areas**

Lars Vedo successfully transformed blank canvas to comprehensive swim
lanes with milestones and interdependencies, while the agentic platform
achieved public endpoint deployment enabling chrome plugin distribution.
With 36 open PRs in a shortened week and engineers creating functional
demos, the platform adoption velocity exceeded expectations.

Ryan McMaster\'s copilot prototype merges sales hub functionality with
existing patterns, creating a canvas surface in the middle pane that
mirrors perplexity-style interactions. This convergence of previously
disparate features addresses the fragmentation concerns raised last week
and provides multiple UI patterns for product team evaluation on Monday.

Danny Pan\'s API processing reached 70K ACV accounts despite
infrastructure challenges, revealing sparse engagement data across
customer accounts---e.g. showing only 200 calls for 300 accounts over
three months. This discovery illuminates retention risks and creates
separate opportunities for predictive modeling around engagement
frequency and renewal probability.

### **Goals & Progress**

**Copilot V2 Development**: Ryan\'s prototype development progresses
toward Monday deadline with focus on real data integration using Grok 4
for authentic request/response demonstrations. The workbooks team\'s
chat artifacts pattern will merge with copilot\'s inline display
capabilities, creating optionality between perplexity-style right panel
and integrated canvas approaches. Functional prototype philosophy
ensures robust testing environment beyond typical figma limitations.

**Data Processing & Automation**: Danny\'s team processed over 50% of
target accounts despite API box reset bugs that interrupt automation
flows. Current session architecture enables automatic recovery through
retriggered runs, maintaining progress while root cause investigation
continues. Transition from batch processing to selective account list
reading positions team for automated deployment next week.

**Platform Architecture & Planning**: Lars delivered comprehensive
planning documentation including press release drafts and jira epic
structure for platform and copilot initiatives. SDK adoption shows
strong uptake with demos from both product managers and engineers, while
chorus team reaches production readiness pending access token
resolution. Public endpoint deployment removes VPN requirements,
accelerating adoption timeline.

### **Strategic Challenges**

Rowan identified architectural decision points around context service
design / build, ultimately choosing a decentralized approach to maintain
velocity. Building agents first with simple Python API clients to
understand actual context requirements---rather than anticipating all
potential issues with quality, size, latency, and refresh rates---this
enables empirical learning while avoiding premature optimization and
creating drag. This decision requires careful monitoring to ensure
technical debt doesn\'t accumulate beyond the September GA deadline.

Danny\'s engagement ingestion automation faces persistent API box reset
issues that, while not blocking progress due to session recovery
mechanisms, prevent full automation deployment. The sparse data
discovery---many accounts showing minimal engagement over three-month
periods---raises fundamental questions about customer health monitoring
and proactive intervention strategies. Without quarterly touchpoints
minimum, retention risk increases substantially.

Lars navigates complex dependencies across multiple teams for copilot v2
success: GTM data model alignment progressing but still open questions
there, RBAC integration not yet initiated, and collaboration features
threatening scope creep. The Wednesday PRD review with Dominic and Adam
represents a critical alignment checkpoint where task deprioritization
and new feature additions will face scrutiny.

## 

## **Strategic Insights**

### **Key Learnings & Discoveries**

Rowan\'s context engineering primer provides conceptual clarity
essential for aligned agent development. The revelation that premature
centralization would slow velocity without empirical requirements
validates a more iterative approach, where each agent implementation
informs architectural patterns.

Danny\'s data analysis exposed concerning engagement patterns:
processing 300 accounts yields only 200 calls over three months,
suggesting many customers receive minimal attention post-sale. This
quantitative validation of suspected retention challenges creates a
clear need for Arash and Robyn\'s recommendation engine development
focused on engagement frequency optimization.

Lars and team discovered strong demand for collaborative features in
seller workflows---artifacts, notes, and views require sharing
capabilities or users will resort to Google Docs. Building collaboration
primitives from inception rather than retrofitting represents
architectural decision with long-term implications for platform
adoption.

### **Cross-Team Dependencies**

Our integration with workbooks team on chat artifact patterns continues
evolving through Ryan\'s prototype work, requiring alignment on display
paradigms before Monday\'s demonstration. The profiles team\'s copilot
chat implementation on public URL removes deployment blockers, but
citing sources functionality requires fast-track development over next
three weeks to meet launch requirements.

Platform SDK adoption by chorus team demonstrates successful abstraction
layer, though security requirements around access tokens remain
unresolved. Grant and Asher\'s onboarding to semantic data service
performance work initiates critical scalability effort---multiple
architecture options under RFC review with decision deadline mid-next
week to maintain September multi-tenant readiness.

## **Looking Ahead**

Next week centers on three convergent demonstrations: Ryan\'s copilot
prototype on Monday, comprehensive PRD review Wednesday, and Friday\'s
agentic AI team demos.

Memory service exploration with Josh, Grant, and Ryan next week.\
\
Zero-config philosophy to context in GTM Config was also
discussed---leveraging existing integration data to impress
administrators before they refine or supplement.

Context engineering team requires deliberate use case prioritization to
channel enthusiasm from platform adoption into highest-impact agent
development. Without stack ranking, parallel efforts risk divergence
when convergence drives compound value. September GA timeline demands
disciplined execution balanced with learning velocity that decentralized
architecture enables.

*Source: Team 1-2-3 Operating Framework entries from July 11, 2025
weekly sync*
