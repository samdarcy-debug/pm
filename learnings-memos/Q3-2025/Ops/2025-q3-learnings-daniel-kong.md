---
id: learnings-2025-035
title: Q3 2025 Learnings Memo - Daniel Kong
type: doc
status: approved
team: ops
owner: '[[teams/ops/_people/daniel-kong]]'
created: '2025-12-23'
updated: '2025-12-23'
tags:
- learnings
- q3-2025
- ops
related: []
---
# **Q3 2025 QBR Learnings Memo - Daniel Kong**



## **Metric Alignment**



**Weekly Operating Model Reports:**



- 250% increase in average monthly comments in weekly reports,

  indicating increased engagement from the entire organization rather

  than just executive leadership (Dominik)



- 20% increase in team-by-team compliance with weekly reporting



**Knowledge Center Automation:**



- KC scanner agent is the top-used agent in the Customer Enablement team

  workspace with 70+ uses, establishing it as the production workflow

  for monthly customer releases



These operational improvements ladder up to organizational velocity and

cross-team coordination effectiveness, enabling faster decision-making

and more consistent product knowledge across GTM teams.



## **Key Learnings**



*What does everyone in the product organization need to know that you

learned about our customers, users, or products this quarter?*



1.  **Cross-team visibility drives engagement when structured for

    action, not reporting.** Weekly operating model reports (covering

    13-15 teams since mid-June) increased engagement from executives and

    ICs after adding analytical tables surfacing cross-team blockers and

    dependencies.



2.  **Knowledge systems require ongoing maintenance to prevent two

    failure modes:** accumulating outdated information and failing to

    disseminate new information across teams.



3.  **Building scalable, batch processes beats individually optimized

    outcomes.** Automated account targeting evaluated entire account

    universes (vs. manual subsets) and batch KB article reviews (25

    articles at once) both proved faster and higher quality than

    sequential individual approaches - the real value is creating

    repeatable processes that improve with scale.



4.  **Product knowledge must be launch infrastructure, not downstream

    documentation.** Batch review processes (upload docs → identify gaps

    → generate articles → bulk review) compressed KC article creation

    from month-long to 1-2 weeks.



5.  **AI-first documentation requires different structuring than

    human-first documentation.** Documents need intentional structure

    for AI consumption (clear sections, consistent formatting) before

    agents can maintain them effectively.



6.  **Report usability determines whether insights drive action.**

    Intelligence requiring effort to extract won\'t be used - adding

    executive summaries and cross-cutting pattern tables increased

    weekly report engagement significantly.



## **Hypotheses & Results**



**Hypothesis 1: Automated agents can maintain knowledge center accuracy

for monthly feature releases at AI-company velocity.** Validated through

two workflows: (1) Monthly feature releases where automated agents scan

existing KC articles against feature information packets, determine

update needs, and generate content changes. (2) New product launches

like Copilot Workspace where PMs provide comprehensive brain dumps and

agents batch-generate 25+ articles, reducing PM time burden while

improving consistency for downstream teams. Real challenge is ongoing

maintenance: need both \"pruning\" (removing outdated content) and

\"broadcasting\" (disseminating updates) layers to complement the

release workflows.



**Hypothesis 2: Building scalable processes from day one creates

compounding value even when initially slower than manual approaches.**

Validated - building agents for scale may be slightly slower for the

first use case than investigating specific problems through non-scalable

approaches (like manually creating one account target list or making

individual KC article updates), but becomes quicker immediately by the

2nd use. Automated account targeting for licensed contractors took

longer upfront to build the scalable process than manual selection would

have, but the second vertical dataset used the same infrastructure

instantly. Similarly, building KC automation agents required more setup

than one-off article updates, but each successive MCR reused the entire

system improving each time.



**Hypothesis 3: Weekly operating model reports drive cross-team

coordination when structured for VP-level decisions.** Required

iteration to validate. Early versions were comprehensive but low

engagement. Adding analytical tables (cross-team blockers, dependency

identification) and strategic framework organization drove adoption from

both executives and ICs. Reports\' value is surfacing patterns requiring

coordination, not tracking tasks.



## **Go-forward Changes & Plan**



**Q4 Priorities:**



1.  **Build a comprehensive knowledge base that maintains accurate

    product knowledge** so that GTM teams can ensure consistent and

    accurate product information as they sell and market our products.



2.  **Improve weekly operating model compliance** to ensure cross-team

    collaboration and visibility.



## **Leveraging AI**



**Most impactful: Knowledge Center scanner and writer tools.** Built

automated agents that the Customer Enablement team now uses during

monthly customer releases to scan existing KC articles, identify which

articles need updates, determine if new articles are needed, and

generate content changes. This system has become the production workflow

for maintaining KC accuracy during the MCR process. More importantly, it

serves as a proof of concept for a more comprehensive knowledge base

system that will extend beyond just the Knowledge Center - enabling

automated pruning, refreshing, and dissemination of product knowledge

across the organization for GTM teams.



**Honorable mention: Weekly operating model report synthesis.** Created

agent prompts that process 13-15 team reports each week to identify

cross-team patterns, surface duplicate blockers, and generate initial

synthesis. These agents have become the standard workflow for producing

weekly executive intelligence briefs.

