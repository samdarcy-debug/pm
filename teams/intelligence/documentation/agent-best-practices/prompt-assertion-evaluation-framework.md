---
id: doc-2026-003
title: PRD: Prompt Assertion Evaluation Framework
type: doc
status: draft
team: intelligence
owner: [[teams\ops\_people\brett-jacobs]]
created: 2026-01-13
updated: 2026-01-13
tags: []
related: []
---

# PRD: Prompt Assertion Evaluation Framework

**Author:** Adam Smith
**Date:** December 17, 2025

## Overview

A framework for evaluating agent outputs against atomic prompt assertions using LLM-as-judge. Given an input, output, and a set of evaluation criteria, the framework returns a structured assessment of whether each assertion was satisfied.

This enables systematic prompt evaluation during development, automated regression testing in CI/CD, and quality monitoring in production.

## The Job

PMs write prompts as collections of atomic assertions, each with evaluation criteria. Currently there's no systematic way to evaluate whether outputs satisfy those assertions. Evaluation is manual, inconsistent, and doesn't scale.

We need a way to:
- Test whether a specific output satisfies each prompt assertion
- Get a quantitative score (% of assertions passed)
- Run this during development (fast feedback for PMs)
- Run this in CI/CD (regression testing before deploy)
- Run this in the no-code builder (inline quality signals)

## Interface

### Input

```json
{
  "agent_input": "The original input/query sent to the agent",
  "agent_output": "The output the agent produced",
  "assertions": [
    {
      "id": "cite_sources",
      "instruction": "Always cite the data source when referencing specific metrics or facts",
      "criteria": [
        "Does the output cite sources when mentioning specific numbers?",
        "Are the citations accurate?",
        "Are citations present for all factual claims?"
      ]
    },
    {
      "id": "acknowledge_gaps",
      "instruction": "If required context is missing, acknowledge the gap rather than guessing",
      "criteria": [
        "When key data is absent, does the output explicitly note this?",
        "Does the output avoid fabricating information to fill gaps?"
      ]
    }
  ]
}
```

### Output

```json
{
  "score": 0.75,
  "passed": 3,
  "failed": 1,
  "total": 4,
  "results": [
    {
      "id": "cite_sources",
      "pass": true,
      "reasoning": "Output cites Salesforce and Chorus as sources for the metrics mentioned. All factual claims reference their data origin."
    },
    {
      "id": "acknowledge_gaps",
      "pass": true,
      "reasoning": "Output explicitly notes that no call data was available for the past 30 days."
    },
    {
      "id": "formal_tone",
      "pass": false,
      "reasoning": "Output uses casual language ('pretty solid quarter') inconsistent with executive communication standards."
    },
    {
      "id": "length_constraint",
      "pass": true,
      "reasoning": "Output is 847 tokens, within the 1000 token limit."
    }
  ]
}
```

## Implementation

### Evaluation Prompt Structure

The evaluator is itself an LLM call. The prompt:

```xml
<role>
You are an evaluation judge. Your job is to assess whether an agent's output satisfies specific behavioral assertions.
</role>

<instructions>
For each assertion, evaluate whether the output satisfies the criteria. Be strict. If any criterion is not met, the assertion fails.

Return your evaluation as a JSON object with the following structure for each assertion:
- id: the assertion identifier
- pass: boolean
- reasoning: one sentence explaining your judgment
</instructions>

<agent_input>
{agent_input}
</agent_input>

<agent_output>
{agent_output}
</agent_output>

<assertions_to_evaluate>
{assertions_json}
</assertions_to_evaluate>
```

**Note:** Static content (role, instructions, output format) comes first for cache efficiency. Dynamic content (input, output, assertions) comes last.

### Scoring

```
score = passed_assertions / total_assertions
```

Simple. A test case passes if `score >= threshold` (default 1.0, configurable per agent).

### Batch Evaluation

For CI/CD, we run evaluation across a test suite:

```json
{
  "agent_id": "account_research_v2",
  "test_suite": "account_research_regression",
  "results": {
    "total_cases": 25,
    "passed_cases": 23,
    "failed_cases": 2,
    "average_score": 0.94,
    "assertion_breakdown": {
      "cite_sources": { "pass_rate": 1.0 },
      "acknowledge_gaps": { "pass_rate": 0.92 },
      "formal_tone": { "pass_rate": 0.88 },
      "length_constraint": { "pass_rate": 1.0 }
    }
  }
}
```

The assertion breakdown surfaces which specific behaviors are failing across the test suite.

## Integration Points

### PM Development Workflow

In the no-code agent builder:

1. PM writes/edits prompt assertions with evaluation criteria
2. PM runs a test query
3. System shows output alongside assertion evaluation
4. PM sees which assertions passed/failed with reasoning
5. Fast iteration loop without involving engineering

**UI:** Sidebar or expandable panel showing assertion results inline with the output.

### CI/CD Pipeline

On PR that modifies an agent:

1. Load agent's test suite (from PRD test cases)
2. Run each test case through the agent
3. Evaluate each output against assertions
4. Block merge if score drops below threshold
5. Surface assertion-level breakdown in PR comments

### Production Monitoring

Sample production traffic:

1. Evaluate random sample of outputs against assertions
2. Track assertion pass rates over time
3. Alert on degradation
4. Feed into quality dashboards

## Model Selection

The evaluator should use a capable model (Claude Sonnet or equivalent). The evaluation task requires:

- Reading comprehension of the output
- Judgment against specific criteria
- Structured output generation

Cost per evaluation is low (small input/output). Even at scale, this is cheap relative to the value of systematic quality measurement.

## Scope

### In Scope

- Single output evaluation against assertions
- Batch evaluation for test suites
- JSON structured output
- Pass/fail per assertion with reasoning
- Aggregate scoring
- API endpoint for programmatic access
- Integration with no-code builder UI

### Out of Scope (for v1)

- Assertion weighting (all assertions equal for now)
- Multi-turn conversation evaluation
- Comparison between outputs (A/B)
- Automatic assertion generation
- Fine-tuned evaluation model

## Dependencies

- LLM API access for the judge model
- Agent platform test case storage (from PRDs)
- CI/CD pipeline hooks
- No-code builder UI component

## Success Metrics

- **PM adoption:** 100% of new agents ship with assertion-based evaluation
- **CI/CD integration:** All agent PRs run automated assertion evaluation
- **Quality signal:** Correlation between assertion scores and user satisfaction (thumbs up/down)
- **Iteration speed:** Time from prompt change to evaluation result <30 seconds in dev workflow

## Open Questions

1. Should we support weighted assertions? (Some behaviors more critical than others)
2. Should assertion evaluation criteria be freeform text or structured templates?
3. How do we handle assertions that are context-dependent? (e.g., "formal tone" might not apply to all user segments)
4. Should we version assertion sets alongside prompt versions?

## Next Steps

1. Build API endpoint for single-output evaluation
2. Integrate into no-code builder as inline evaluation panel
3. Add batch evaluation for test suites
4. Hook into CI/CD pipeline
5. Build/connect dashboard for production monitoring

