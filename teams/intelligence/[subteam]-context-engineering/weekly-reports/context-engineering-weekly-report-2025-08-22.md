---
id: weekly-context-engineering-2025-34
title: "Context Engineering Weekly Report - August 22, 2025"
type: weekly-report
status: approved
team: context-engineering
owner:
created: 2025-08-22
updated: 2026-01-06
week_ending: 2025-08-22
reporting_period: "August 18-22, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Context Engineering Team Executive Roundup - August 22, 2025**

## **Executive Summary**

The Context Engineering team achieved significant momentum this week
with multiple workstreams converging toward a unified GTM context
service architecture. Rowan Bailey secured the green light to enhance
account brief and summary sections that generate 1.5M monthly views,
while the team officially kicked off the go-to-market context service
with a new engineering team ahead of October\'s Dreamforce showcase.
Critical architectural decisions remain open regarding MCP tool
hierarchy, but Sri Marthi has aligned the implementing team and
established the foundation for signals-as-a-service capabilities.

## **This Week\'s Progress**

### **Key Momentum Areas**

The MCP server initiative for signals gained substantial clarity with
Sri Marthi completing 80% of his goal to draft and review implementation
plans with Yvonne and Pankaj. This work will enable signals to become
accessible and flexibly usable by any agent, addressing Brandon
Tucker\'s feedback that current signal packaging is \"over the head of
customers\" who struggle to understand specific signal applications.

Robyn Sablosky\'s APS (Account Propensity Scoring) API went live 8 days
ago and is being immediately adopted by ZI Labs starting next week,
providing a rapid feedback loop for iterations. The lookalike scoring
models are showing strong early results, positioning the team to deliver
more intelligent contact recommendations across multiple product
surfaces.

The semantic data workstream delivered a successful demo to Paychex in
staging, demonstrating on-the-fly attribute creation that could help
save a potential Chorus churn risk. The customer understood the value
proposition and expressed interest in joining the Early Access program,
with next week\'s focus on getting semantic data into GTM Store to
enable downstream signal generation.

### **Goals & Progress**

**MCP Server Architecture**: Sri Marthi advanced the signals MCP server
documentation and implementation planning, completing initial alignment
with the engineering team. Two critical open items remain: finalizing
the tool hierarchy (how signals map to tools and whether to use a
unified MCP server or separate ones per data type) and coordinating with
Ryan Stevens\' team on division of responsibilities. This foundational
work will determine how effectively signals can be packaged for customer
consumption.

**AI/ML Personalization Strategy**: Robyn Sablosky identified
significant gaps in product-level personalization capabilities,
determining that current data is insufficient for machine learning
approaches and LLM-based solutions would be \"a guess at best.\" She\'s
documenting these limitations and developing a strategy document that
distinguishes between basic personalization (knowing what accounts
customers sell to) and advanced personalization (next best actions and
sophisticated plays).

**GTM Context Service Launch**: Rowan Bailey\'s team received a new
engineering squad to build ZoomInfo\'s MCP Gateway for Claude, with a
mandate to equip as many core tools as possible before Dreamforce. This
service will provide customers direct access to ZoomInfo\'s data
offerings and specialized services through an external-facing MCP,
representing a significant productization of the team\'s capabilities.

### **Strategic Challenges**

The lack of UX resources for Robyn\'s scoring and recommendation models
creates uncertainty about the feedback loop and user experience design.
Without clear understanding of how lookalike scoring will appear in the
product UI, the team risks building capabilities that don\'t integrate
smoothly into existing workflows. Robyn is exploring workarounds through
Copilot chat interfaces as suggested by Rowan.

Cross-team coordination for the MCP architecture remains unresolved,
with Sri needing to meet with Ryan Stevens\' team to clarify
responsibilities between GSO and the platform teams. The decision on
whether to wait for signals data in the GTM store versus building
interim solutions could impact timeline and avoid deprecated work, as
Rowan noted his preference to \"wait until it\'s in the store to avoid
doing work that\'s gonna get deprecated a few weeks later.\"

Data consistency across multiple asset generation touchpoints poses a
risk to user experience, as Christine highlighted concerns about account
briefs, value propositions, and GTM config data potentially providing
conflicting information. The team needs to ensure that scraped website
data, admin-provided configuration, and generated content all align to
maintain credibility.

## **Strategic Insights**

### **Key Learnings & Discoveries**

The team discovered that signal packaging requires a fundamental rethink
from technical capabilities to customer questions. As Sri learned from
Brandon Tucker, current signal cubes are \"too specific\" - customers
don\'t understand what to do with earnings signals presented in
isolation. The solution involves grouping signals into broader business
questions like market readiness, aligning technical tools with the
questions customers actually want answered.

Rowan identified that the convergence of multiple workstreams - semantic
data, GTM config, and account briefs - creates an opportunity for a
unified data enrichment strategy. By treating GTM config as both a data
collection and validation mechanism, the team can present inferred
knowledge to admins and capture corrections, creating a feedback loop
that improves all downstream applications.

Robyn\'s analysis revealed that true personalization will require
cross-product agreement on data collection and experimentation
strategies. The distinction between basic and advanced personalization
provides a framework for prioritizing incremental improvements while
working toward more sophisticated capabilities like next-best-action
recommendations.

### **Cross-Team Dependencies**

Our collaboration with Ryan Stevens\' team on the MCP server
architecture is critical for avoiding duplicate work and ensuring proper
separation of concerns between the GSO team and platform engineering.
Sri needs this coordination to finalize whether signal tools should be
part of a unified MCP server or maintained separately.

The integration with ZI Labs for APS feedback creates a valuable testing
ground for Robyn\'s models, but she also needs engagement from legacy
product experts like Christine to identify and deprecate outdated models
and ensure naming consistency across workbooks and other surfaces. This
cleanup work is essential for creating the \"seamless product\"
experience Robyn envisions.

## **Looking Ahead**

Next week marks a pivotal transition as the team shifts from planning to
execution across multiple fronts, with Rowan re-roadmapping H2
priorities to reflect the rapidly evolving landscape and newfound
alignment across workstreams.

The immediate priorities include getting semantic data into GTM Store to
unlock signal generation capabilities, finalizing the MCP tool hierarchy
with Ryan Stevens\' team, and spinning up new MCP tools for testing in
Claude Desktop. Robyn will focus on completing her AI/ML personalization
strategy document while beginning UX conversations for workbooks
integration, and Christine will develop the plan for transforming
account briefs into comprehensive account plans that serve as a
foundation for the React agent.

The team\'s momentum heading into next week reflects what Rowan
described as \"a lot of these threads aligning\" - with semantic data,
scoring models, MCP architecture, and GTM configuration all converging
toward a cohesive platform that can power both internal tools and
external customer experiences. The team is well-positioned to deliver
meaningful demos and capabilities ahead of the October Dreamforce
showcase.

*Source: Team 1-2-3 Operating Framework entries from August 18-22, 2025*
