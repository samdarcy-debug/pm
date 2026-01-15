---
id: doc-2026-001
title: Agent Development Best Practices
type: doc
status: draft
team: intelligence
owner: "[[teams/ops/_people/brett-jacobs]]"
created: 2026-01-13
updated: 2026-01-13
tags: []
related: []
---


# Agent Development Best Practices

Foundational guidance for building AI agents on ZoomInfo's Agentic Platform (ZAP).

## Core Documents

- **[Building AI Agents: Challenges & Best Practices](building-ai-agents-best-practices.md)** - Comprehensive guide on agent design fundamentals, from shaping probability space to writing requirements. Covers the mental models and practices needed to build reliable AI agents.

- **[Prompt Writing Guide for Product Managers](prompt-writing-guide.md)** - Practical guide to writing effective prompts using atomic decomposition, proper structure, and evaluation criteria. Covers the three components of prompts (context, attention, instruction) and how to optimize for caching.

- **[Prompt Assertion Evaluation Framework](prompt-assertion-evaluation-framework.md)** - LLM-as-judge framework for systematically evaluating agent outputs against atomic prompt assertions. Enables automated testing during development, CI/CD integration, and production quality monitoring.

## Using These Guides

When creating an Agent PRD, use the `/agent-prd` skill which automatically references these best practices throughout the interview process.

The skill will guide you through:
- Defining clear boundaries and scope (using decomposition principles)
- Writing test cases with proper coverage
- Structuring prompts with atomic assertions and evaluation criteria
- Creating human-in-the-loop patterns where appropriate
- Validating against the "vending machine test" and "intern test"

## Key Concepts

### Shaping Probability Space
Unlike traditional software that either works or doesn't, agents operate probabilistically. Your job as a PM is to design the boundary: where must the agent succeed? Where is failure acceptable?

### Task Decomposition
Break broad capabilities into constituent jobs, each with clear inputs, outputs, and success criteria. If you can't write 20 test cases, you haven't decomposed far enough.

### The 10x Rule
For reliable output, provide context that's at least 10x the length of your expected output. LLMs excel at compression, not generation.

### Atomic Assertions
Every behavioral instruction should have explicit evaluation criteria. If you can't measure whether it's working, it's too vague to be useful.

### Human-in-the-Loop
For complex requests: propose a plan first, get user confirmation, then execute. Users prefer quick confirmation to long waits followed by wrong results.

## Process

1. **Define the job** using the vending machine test (clear inputs → clear outputs)
2. **Decompose** until you can write specific test cases
3. **Write test cases** before building (10-15 success, 10-15 rejection, edge cases)
4. **Structure prompts** with atomic assertions and evaluation criteria
5. **Validate** using the Prompt Assertion Evaluation Framework
6. **Iterate** based on systematic evaluation

## Quick Reference

| If you're asking... | See... |
|-------------------|--------|
| "How do I scope this agent?" | [Task Decomposition](building-ai-agents-best-practices.md#task-decomposition) |
| "What test cases do I need?" | [Writing Requirements](building-ai-agents-best-practices.md#writing-requirements-for-agents) |
| "How do I write better prompts?" | [Prompt Writing Guide](prompt-writing-guide.md) |
| "How do I evaluate quality?" | [Evaluation Framework](prompt-assertion-evaluation-framework.md) |
| "Should this be human-in-the-loop?" | [Human in the Loop](building-ai-agents-best-practices.md#human-in-the-loop) |
| "Is my scope too broad?" | [The Manual Test](building-ai-agents-best-practices.md#task-decomposition) |

---

**For questions or feedback:** Contact the Intelligence team or Adam Smith


