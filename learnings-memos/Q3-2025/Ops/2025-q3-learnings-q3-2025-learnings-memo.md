---
id: learnings-2025-036
title: Q3 2025 Learnings Memo - Q3 2025 Learnings Memo
type: doc
status: approved
team: ops
owner: '[[teams/ops/_people/q3-2025-learnings-memo]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- ops
related: []
---
# **Ken Elwell - Q3 2025 Learnings Memo**



## **Metric Alignment**



My Q3 work built ZoomInfo\'s AI Marketing Engine from zero to

production, creating the first scalable content generation system for

product releases. This ladders up to **Activation Rate** (customers

discovering and using new features through better product marketing

communications), **Net Retention** (GTM team effectiveness in

renewals/upsells through personalized account intelligence and

consistent product messaging).



Additionally, two more impacted metrics that are difficult to quantify,

are **Product Manager time saved & marketing messaging consistency.**

The system delivered 4 consecutive Monthly Customer Releases while

reducing PM documentation time, eliminating weeks of PM-PMM coordination

cycles that previously required manual stakeholder interviews and

multiple revision rounds. We have created a system that ensures

consistency and speed across all marketing asset creation.



## **Key Learnings**



- **Workflow integration determines adoption, not feature quality or

  executive sponsorship** - Personalized roadmap/release note agents

  achieved low usage (\~5% of GTM team) despite Henry\'s company-wide

  distribution because tools requiring extra workflow steps die

  immediately. The GTM Messaging Agent achieved 18 users in the first

  couple days by meeting teams where they work versus requiring behavior

  change.



- **AI implementation needs specialized \"micro-agents\" with iterative

  prompt tuning** - The Marketing Engine\'s distinct modules (Feature

  Info Pack, Release Notes, Executive Review) proved essential for

  quality over broad automation attempts.



- **Avatar feedback loops eliminate stakeholder coordination

  bottlenecks** - Gathering comprehensive perspectives through AI bots

  (Support, CX, Sales, Executives) removes all coordination upfront

  instead of reactive post-launch questions.



- **Knowledge management requires ongoing curation discipline, not just

  technical solutions** - Built robust infrastructure for knowledge

  graphs with automated conflict detection and update mechanisms, but

  sustainable curation processes remain the critical operational

  challenge to prevent content staleness.



- **Organic AI adoption happens when you meet teams where they work** -

  Building PDFs instead of Google Slides killed personalized AM meeting

  deck adoption. Marketing team creating elevator pitches in 30 seconds

  succeeded because it fit existing workflows.



- **Document curation determines AI output quality more than technology

  choices** - Directly referencing docs fails at scale while summarizing

  creates inferior outputs; proper solution requires thoughtful document

  selection with systematic pruning.



- **AI enablement and change management determine tool success at

  scale** - Personalized features showed capability (74 unique users for

  release notes) but remained underutilized without GTM enablement team

  driving adoption as part of standard workflows.



## **Hypotheses & Results**



### **Hypothesis 1: An AI Marketing Engine could replace traditional PM-PMM collaboration cycles while improving content quality and velocity**



**Going in:** Traditional product marketing required weeks of PM-PMM

back-and-forth per release. Objective was to decentralize the classic

PMM role and build an AI-centric marketing engine. At its core, this is

a data problem---we need a single source of truth about what customers

want, products we\'re building, how they deliver value, and closed

feedback loop.



**Results:** Strong validation with measurable efficiency gains. Built

complete system with 4 modules:



1.  Feature Info Pack/PRFAQ Creator with GTM Colleague Avatars (Support,

    CX, Sales) providing sequential feedback and automatic tier

    classification



2.  Release Note Writer with Executive Avatars (Henry, Alex, Lou,

    Millie)



3.  Source-of-truth document repository



4.  Systematic feedback loop. Delivered 4 consecutive MCRs

    (July-October) with continuous improvement: July (60+ min/feature) →

    August (30 min/feature).



Successfully eliminated PM-PMM collaboration cycles while maintaining

quality. PMs gave positive feedback. AI doesn\'t reduce revision

count---it reduces TIME per revision and moves coordination upfront via

avatar feedback loops.



### **Hypothesis 2:** **Knowledge graph infrastructure would enable scalable, accurate product information at launch velocity**



**Going in:** Need centralized knowledge infrastructure that AI can

reference for consistent, current messaging across all GTM content.



**Results**: Strong validation with complete infrastructure

breakthrough. Proved that centralized knowledge systems can power

multiple AI agents while maintaining consistency---Marketing content

agent achieved 18 users in the couple days with organic adoption.

July-August focused on proof of concept and architectural decisions.

September delivered a critical breakthrough: secured initial

infrastructure access enabling knowledge graph for agents.



**Hypothesis 3: Personalized account-specific intelligence would drive

rep adoption if delivered at scale**



**Going in:** Reps would dramatically improve customer conversations

with personalized materials at scale - we just needed to build

high-quality, account-specific tools.



**Results:**



- Built 3 capabilities aligned to account-based selling: personalized

  roadmaps (filter features to customer needs), personalized release

  notes (relevant updates only), sales deck automation (Alex

  Lazerowich\'s AM team). Henry sent out to the company.



- The personalized roadmap and release notes saw minor success with 60

  total uses across 39 unique users for the roadmap and 170 total uses

  across 74 unique users for the personalized release notes. Though this

  number is fairly low considering the size of the GTM org. Enabling

  sellers on how/when to use this was a missing piece from the GTM

  enablement team. For this to truly succeed, it needs to be a part of

  the GTM team's workflow.



- Personalized deck creation failed due to the fact that we were

  building PDFs rather than google slides (which is still not possible).

  Essentially we did not meet the AMs where they worked and they would

  not, understandably, adjust their workflow to fit the new motion - we

  need to meet them where they work.



## **Go-forward Changes & Plan**



### **Goal 1: Build account-based selling intelligence that reps use and drives results**



**Focus products:** Vertical Datasets, GTM Studio, Copilot, Context

Service



**Push/Pull context:**



- **Push system** (Copilot tells reps what to sell per account - we

  don\'t own but should connect to it)



- **Pull system** (what we own) - rep-initiated requests



**Frontend vision:** Rep says \"I\'m meeting with Account X about Y. I

will go over top use cases, pitch Contractor Datasets, and GTM Studio\"

→ system provides menu of agents → creates customized deck with

account-specific use cases, talk tracks, objection handling, competitive

positioning, release notes, roadmap → rep can ask follow-up questions in

same interface



**Backend infrastructure:** Product marketing assets (talk tracks, FAQs,

objection handling, competitive positioning) generated from and kept

fresh by knowledge graph. Knowledge graph ingests raw information (VoC

feedback, competitive intelligence, thought leader content, product

facts) and continuously updates assets. Talk tracks improve based on

what worked/didn\'t work, FAQs stay current.



### **Goal 2: Generate monthly release content - focus on release notes that drive adoption and become an inbound motion**



**Focus:** AI-powered content generation system that creates release

notes designed to drive adoption, not just inform.



## **Leveraging AI**



**Most impactful use case:** AI Marketing Engine complete system---4

modules (Feature Info Pack/PRFAQ Creator with GTM Colleague Avatars,

Release Note Writer with Executive Avatars, source-of-truth repository,

systematic feedback loop) replacing PM-PMM collaboration. Delivered 4

consecutive MCRs with PM time reduction, eliminated weeks of

coordination cycles per release. Live in AI Marketing Engine workspace

in ZI Chat.



**Additional high-impact:** GTM Messaging Agent (18 users first couple

days, 30-second elevator pitch creation, organic adoption), Earnings

Call Product Section Agent (analyzes 9 quarters + competitors for

analyst-optimized communications), Personalized Account Agents (proved

capability, revealed workflow integration necessity).



**Q4 expansion:** Deploy gtm.ai release notes and measure inbound

adoption impact, operationalize knowledge graph within AI Marketing

engine, build knowledge refresh system to prevent stale content.

Philosophy shift: from \"ship more AI features\" to \"drive adoption of

shipped features through workflow integration\"

