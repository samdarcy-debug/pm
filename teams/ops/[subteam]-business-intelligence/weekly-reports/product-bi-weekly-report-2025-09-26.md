---
id: weekly-product-bi-2025-39
title: "Product BI Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: product-bi
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

**Product BI Team Executive Roundup - September 26, 2025**

**Executive Summary**

Copilot Workspace V2 foundational reporting is now operational with the
second batch of 100 internal GTM users completing training yesterday,
positioning us to capture meaningful adoption metrics as they begin full
utilization. While instrumentation gaps temporarily slowed initial
analysis, Phoebe identified and escalated these issues to engineering
leadership, with fixes expected shortly. The team has established
session replay capabilities through Datadog, enabling deep user behavior
analysis that will inform product optimization decisions.

**This Week\'s Progress**

**Key Momentum Areas**

Phoebe delivered the foundational user-level reporting framework for
Copilot Workspace V2, creating visibility into how the second batch of
100 internal sellers are engaging with the platform. Despite
instrumentation challenges, she successfully established early adoption
tracking and gained access to Datadog session replay functionality,
allowing the team to analyze individual user journeys and identify
friction points in real-time.

Nanxi made substantial progress on API analytics infrastructure by
completely redesigning the approach after discovering significant data
quality issues. She created comprehensive documentation to standardize
terminology across teams, aligned with stakeholders on dashboard
wireframes, and established the foundation for scalable API reporting
that will support strategic decision-making.

The hiring pipeline advanced significantly with one candidate moving to
the third round with stakeholder interview scheduled for next Tuesday,
and another progressing to the second round. Nanxi identified the
current third-round candidate as potentially the strongest seen for this
role, indicating promising talent acquisition momentum.

**Goals & Progress**

**Copilot Workspace V2 Analytics**: Foundational reporting is now
operational despite instrumentation gaps that initially blocked user
cohort filtering for chat engagement events. Phoebe established early
adoption analysis covering the first three days of data and implemented
session replay monitoring. The second batch of 100 users completed
training yesterday, making this week\'s activity data more meaningful
than previous days when users were waiting for training.

**API Dashboard Development**: Nanxi completed approximately half of the
data exploration work and created essential documentation standardizing
terminology between teams. The original timeline extended due to
discovering messy backend data structures, inconsistent terminology
usage, and lack of documentation, but the foundation work ensures
sustainable analytics infrastructure for future phases.

**Team Infrastructure**: Ferrell completed Amplitude data cleaning tasks
and will focus next week on supporting PM upskilling initiatives. The
team established an analytics channel with visibility for Raghu, Nebo,
and Brahm to ensure coordination across product analytics efforts and
prevent duplicated work.

**Strategic Challenges**

Multiple instrumentation gaps are creating recurring delays across
several events, requiring engineering fixes that slow down analysis
workflows. Phoebe identified this pattern affecting 4-5 events and will
work with AJ to escalate to engineering leadership, as the current
reactive approach generates additional work for teams who must revisit
completed tickets. There appears to be a systemic issue where event
properties, particularly user IDs, are not being captured properly
during implementation.

The API analytics work revealed significant technical debt in existing
dashboard infrastructure, including inefficient query structures,
inconsistent terminology, and scattered data sources without
documentation. While this discovery prompted a complete rebuild
approach, it highlights the need for better analytics standards and
documentation practices to prevent similar issues in future product
areas.

Session replay analysis capabilities are newly available but require
validation to ensure comprehensive user coverage rather than just
selected samples. The team needs to establish best practices for sharing
individual user insights with product teams while maintaining the
broader quantitative analysis approach.

**Strategic Insights**

**Key Learnings & Discoveries**

Early Copilot Workspace V2 data reveals that only 22-23 users out of 100
had meaningful engagement before training completion, validating the
decision to prioritize post-training activity analysis. This pattern
suggests users appropriately waited for formal training rather than
exploring independently, indicating good change management practices and
setting realistic expectations for meaningful adoption metrics.

API analytics infrastructure uncovered the need for standardized
approaches to data granularity and source of truth establishment. Nanxi
discovered that different metrics require different data sources and
granularity levels - for example, credits cannot break down to API type
level while requests can, creating filtering inconsistencies that affect
dashboard reliability and user experience.

Session replay functionality provides unprecedented visibility into
individual user behavior patterns, enabling identification of users who
log in but struggle to complete meaningful actions. This capability
allows the team to distinguish between intentional \"window shopping\"
behavior and actual navigation difficulties, informing product team
decisions about interface improvements.

**Cross-Team Dependencies**

Our collaboration with Raghu and Nebo on Copilot Workspace analytics
continues to strengthen with shared visibility in the analytics channel
and coordinated dashboard development. Nebo\'s data-focused approach and
technical depth complement our analysis capabilities, while Raghu\'s
Looker Studio dashboard work provides additional perspective on user
engagement patterns.

The engineering team\'s responsiveness on API analytics questions has
been positive, though the systematic instrumentation issues require
broader leadership attention. Establishing clearer analytics
requirements during feature development could prevent the reactive fixes
currently consuming team bandwidth.

**Looking Ahead**

Next week focuses on capturing meaningful adoption insights from the
newly trained Copilot Workspace V2 cohort while establishing sustainable
analytics practices that prevent recurring instrumentation issues.

The team will prioritize daily utilization reporting for Copilot
Workspace V2 users, measuring what percentage of business days each user
achieves some form of value through views or other engagement metrics.
This foundational metric will support regular leadership reporting while
Phoebe continues session replay analysis to identify specific user
experience friction points that could accelerate adoption.

Nanxi will complete Phase 1 of the API dashboard rebuild, delivering
main KPIs in the agreed wireframe format while documenting the
standardized terminology and data sources for future analytics work. The
hiring process continues with strong momentum, potentially adding
critical capacity to support expanding analytics requirements across
multiple product initiatives.

*Source: Team 1-2-3 Operating Framework entries from September 26, 2025*
