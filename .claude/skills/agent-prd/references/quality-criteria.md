---
id: doc-2026-002
title: Agent PRD Quality Criteria
type: doc
status: draft
owner: [[teams\ops\_people\brett-jacobs]]
created: 2026-01-13
updated: 2026-01-13
tags: []
related: []
---

# Agent PRD Quality Criteria

Comprehensive scoring rubrics for evaluating Agent PRDs against best practices. Each section has specific pass criteria and scoring guidelines. Target: 90+/100 across all sections.

## Section 1: Job to Be Done (Target: 90+)

### Pass Criteria

- [ ] Problem statement in user language (not technical jargon)
- [ ] 3-5 specific user stories in standard format ("As a [persona], I want to [action] so that [benefit]")
- [ ] Target persona clearly defined with role and context
- [ ] Current state workflow documented (how they solve this manually today)
- [ ] Success described from user's perspective (experiential, not metrics)
- [ ] Forcing question answered with clear one-sentence pitch
- [ ] References best practices: "Understanding User Needs" (building-ai-agents-best-practices.md)

### Scoring

- **100:** All criteria met exceptionally, rich detail, clear user empathy, compelling narrative
- **90:** All criteria met well, sufficient detail, user-centric language
- **80:** All criteria met, some sections could be more specific or user-focused
- **70:** 1-2 criteria weak or missing detail
- **<70:** Multiple criteria weak or missing

### Common Issues

- Using technical language instead of user language ("optimize latency" vs. "get results faster")
- Vague success criteria ("improve productivity" vs. "save 30 minutes per day on email drafting")
- Missing target persona specifics (role, constraints, context)
- Current state not documented (can't justify why change is needed)

---

## Section 2: Scope & Decomposition (Target: 90+)

### Pass Criteria

- [ ] Parent capability identified
- [ ] Sibling capabilities listed
- [ ] Decomposition level justified (why this scope vs. broader/narrower)
- [ ] 15-20 in-scope query examples with rationale
- [ ] 15-20 out-of-scope query examples with graceful rejection responses
- [ ] Forcing question answered: Can you immediately classify any query as in/out?
- [ ] References best practices: "Task Decomposition" (building-ai-agents-best-practices.md)

### Scoring

- **100:** 20+ in-scope, 20+ out-of-scope, crystal clear boundaries, excellent decomposition rationale
- **90:** 15+ each, clear boundaries, solid decomposition justification
- **80:** 10-15 each, mostly clear boundaries, adequate justification
- **70:** <10 each or boundaries ambiguous in places
- **<70:** Insufficient examples or no clear boundary

### Common Issues

- Scope too broad ("email writing" without decomposing into cold outbound vs. active deal vs. customer success)
- Insufficient out-of-scope examples (boundary isn't clear without negative examples)
- No graceful rejection language for out-of-scope queries
- Can't pass the forcing question (ambiguous queries at the boundary)

---

## Section 3: Opaque Executor Contract (Target: 90+)

### Pass Criteria

- [ ] All required inputs explicitly listed with types
- [ ] Optional inputs identified and justified
- [ ] Output format clearly specified (structure, always-included fields, optional fields)
- [ ] Passes vending machine test (clear X → Y, no ambiguity)
- [ ] References best practices: "The Vending Machine Test" (building-ai-agents-best-practices.md)

### Scoring

- **100:** Perfect black box definition, zero ambiguity, passes vending machine test with flying colors
- **90:** Clear inputs and outputs, passes vending machine test
- **80:** Mostly clear, minor ambiguities in optional inputs or output structure
- **70:** Some ambiguity in required inputs or output format
- **<70:** Vague inputs/outputs, fails vending machine test

### Common Issues

- Required vs. optional inputs not distinguished
- Output format vague ("returns relevant information")
- Missing error cases (what happens when required data unavailable?)
- Can't describe as "put X in, get Y out" precisely

---

## Section 4: Context Requirements (Target: 90+)

### Pass Criteria

- [ ] All data sources explicitly listed
- [ ] Each source has clear justification: "What context this provides"
- [ ] 10x rule compliance verified (if output is 500 words, context is 5,000 words)
- [ ] Context quality assessed (dense/relevant vs. verbose/low-value)
- [ ] References best practices: "Context Quality and the 10x Rule" (building-ai-agents-best-practices.md)

### Scoring

- **100:** Perfect justification for each source, 10x rule met, high-quality context plan
- **90:** All sources justified, 10x rule met, good context quality
- **80:** Most sources justified, close to 10x rule
- **70:** Some sources lack justification or 10x rule not met
- **<70:** Vague data requirements or poor context quality plan

### Common Issues

- Listing data sources without explaining what context they provide
- Violating 10x rule (expecting detailed output from minimal context)
- Including low-value "popcorn" data instead of high-value "steak"
- Missing critical data sources for the stated use case

---

## Section 5: Ideal Flow (Target: 90+)

### Pass Criteria

- [ ] Step-by-step flow documented from user input to user output
- [ ] Human-in-the-loop decision justified (why confirm or why skip confirmation)
- [ ] Timeline expectation set (reasonable response time)
- [ ] Error paths considered (what happens when things fail)

### Scoring

- **100:** Crystal clear flow, excellent human-in-the-loop justification, realistic timeline
- **90:** Clear flow, justified human-in-the-loop, reasonable timeline
- **80:** Flow documented, human-in-the-loop addressed, timeline set
- **70:** Flow vague or human-in-the-loop decision unjustified
- **<70:** Missing flow steps or no consideration of confirmation pattern

### Common Issues

- Not justifying human-in-the-loop vs. immediate execution choice
- Unrealistic timeline expectations (complex synthesis in 5 seconds)
- Missing error paths (what if data unavailable, ambiguous query, etc.)

---

## Section 6: Test Cases (Target: 90+)

### Pass Criteria

- [ ] 10-15 "Must Succeed" cases with input/behavior/pass criteria
- [ ] 10-15 "Must Reject or Redirect" cases with rationale and expected response
- [ ] 5+ edge cases with handling described
- [ ] Each test case is specific and measurable
- [ ] Test cases align with scope boundaries from Section 2
- [ ] Covers the most critical user paths from Section 1
- [ ] References best practices: "The Test Case Requirement" (building-ai-agents-best-practices.md)

### Scoring

- **100:** 30+ total test cases, comprehensive coverage, specific and actionable, clear pass criteria
- **90:** 25-30 test cases, good coverage, clear pass criteria
- **80:** 20-25 test cases, adequate coverage, mostly clear criteria
- **70:** 15-20 test cases, some gaps in coverage
- **<70:** <15 test cases or poor coverage

### Common Issues

- Insufficient test cases (need 30+)
- Vague test cases ("test if it works for accounts")
- No pass criteria (how do you evaluate success?)
- Missing rejection/redirect cases (only happy path tested)
- Missing edge cases (data unavailable, ambiguous input, etc.)

---

## Section 7: Dependencies (Target: 90+)

### Pass Criteria

- [ ] Platform dependencies listed (ZAP capabilities required)
- [ ] Data dependencies listed (what must be integrated)
- [ ] Tool dependencies listed (what tools must be available)
- [ ] Blockers identified (what's missing today that would prevent this from working)

### Scoring

- **100:** Comprehensive dependency list, blockers clearly identified, mitigation plans included
- **90:** All dependencies listed, blockers identified
- **80:** Most dependencies listed, major blockers identified
- **70:** Some dependencies missing or blockers unclear
- **<70:** Vague or incomplete dependency list

### Common Issues

- Missing critical dependencies (tool doesn't exist yet)
- No blocker identification (assuming everything is ready)
- No mitigation plan for blockers

---

## Section 8: Prompt Structure (Target: 90+)

### Pass Criteria

- [ ] Each instruction has evaluation criteria (atomic assertions)
- [ ] Instructions follow atomic assertion pattern (one claim per instruction)
- [ ] Agent description for orchestrator routing is clear
- [ ] Forcing question answered: Can you measure if each instruction works?
- [ ] Optimized for prompt caching (static content first, dynamic last)
- [ ] References best practices: "Atomic Prompt Decomposition" (prompt-writing-guide.md)

### Scoring

- **100:** All assertions atomic with clear eval criteria, perfect structure, cache-optimized
- **90:** All assertions have eval criteria, good structure, cache-optimized
- **80:** Most assertions have eval criteria, minor structural issues
- **70:** Some assertions lack eval criteria or structure sub-optimal
- **<70:** Many assertions unevaluable or poorly structured

### Common Issues

- Vague instructions without evaluation criteria ("be helpful")
- Bundled assertions (multiple claims in one instruction)
- Not cache-optimized (dynamic content first instead of static)
- Can't measure if instructions are being followed

---

## Section 9: Human-in-the-Loop Design (Target: 90+)

### Pass Criteria

- [ ] Confirmation pattern clearly defined (what user sees before execution)
- [ ] Skip conditions justified (when can we skip confirmation)
- [ ] Error handling documented (what happens when execution fails)
- [ ] References best practices: "Human in the Loop" (building-ai-agents-best-practices.md)

### Scoring

- **100:** Perfect confirmation pattern, well-justified skip conditions, comprehensive error handling
- **90:** Clear confirmation pattern, justified skip conditions, error handling documented
- **80:** Confirmation pattern defined, skip conditions addressed, basic error handling
- **70:** Confirmation pattern vague or skip conditions unjustified
- **<70:** Missing confirmation pattern or no error handling

### Common Issues

- No justification for skipping confirmation (should almost always confirm for complex ops)
- Vague confirmation message (user doesn't understand what will happen)
- No error handling plan

---

## Section 10: Metrics (Target: 90+)

### Pass Criteria

- [ ] Usage metrics defined (queries per day, unique users, etc.)
- [ ] Quality metrics defined (thumbs up/down rate, assertion pass rate, etc.)
- [ ] Business metrics defined (impact on pipeline, deal velocity, user productivity, etc.)

### Scoring

- **100:** Comprehensive metrics across usage, quality, and business impact with targets
- **90:** All three metric types defined with targets
- **80:** All three metric types defined, some targets missing
- **70:** One metric type missing or no targets
- **<70:** Vague or incomplete metrics

### Common Issues

- Only usage metrics, no quality or business metrics
- No targets or success thresholds defined
- Metrics not tied to Section 1 success criteria

---

## Section 11: Data Flywheel (Target: 90+)

### Pass Criteria

- [ ] Feedback collection mechanism defined (how we capture user feedback)
- [ ] Improvement loop documented (how feedback improves prompts/context)
- [ ] Data capture strategy outlined (what data from usage improves future performance)

### Scoring

- **100:** Comprehensive flywheel with clear feedback → improvement path
- **90:** All three components defined (feedback, improvement, data capture)
- **80:** All components addressed, some detail missing
- **70:** One component weak or missing detail
- **<70:** Vague or incomplete flywheel plan

### Common Issues

- No clear path from feedback to improvement
- Passive data collection without active improvement loop
- Not tied to assertion-based evaluation framework

---

## Section 12: Competitive Comparative (Target: 90+)

### Pass Criteria

- [ ] Current state documented (how users solve this today)
- [ ] Testing results captured (what works/doesn't in existing solutions like co-pilot, Claude, manual)
- [ ] Gap analysis specific and justified (what this custom agent provides that alternatives don't)
- [ ] Clear answer to "why build this?" (investment justification)

### Scoring

- **100:** Comprehensive testing, specific gap analysis, compelling justification
- **90:** Testing done, gaps identified, justification clear
- **80:** Basic testing, gaps identified, justification present
- **70:** Testing incomplete or gaps vague
- **<70:** No testing or weak justification

### Common Issues

- No actual testing of alternatives (assumptions instead of data)
- Gaps not specific ("it'll be better")
- Weak justification for building custom agent

---

## Section 13: Rollout & Communication (Target: 90+)

### Pass Criteria

- [ ] Rollout plan documented (phased, all-at-once, specific user groups)
- [ ] Communication plan defined (who needs to know, what messaging)
- [ ] Training needs identified (documentation, training sessions)
- [ ] Success criteria clear (what does successful rollout look like)

### Scoring

- **100:** Comprehensive rollout plan with communication, training, and success criteria
- **90:** All components defined (rollout, communication, training, success)
- **80:** All components addressed, some detail missing
- **70:** One component weak or missing
- **<70:** Vague or incomplete rollout plan

### Common Issues

- No phased rollout plan (trying to ship to everyone at once)
- Missing communication to key stakeholders
- No training plan for users
- Success criteria vague or unmeasurable

---

## Aggregate Scoring

**Overall Score = Average of all 13 section scores**

**Pass Thresholds:**
- **90+ Overall:** A+ PRD, ready for review and implementation
- **80-89 Overall:** Good PRD, needs improvement in weak sections
- **70-79 Overall:** Needs significant work in multiple sections
- **<70 Overall:** Not ready, fundamental gaps

**Section-Level Targets:**
- Every section should score 90+ before considering PRD complete
- If any section scores <90, focus Quality Improvement iteration on that section
- Address lowest-scoring sections first (highest impact)

**Quality Improvement Iteration Strategy:**
1. Assess section quality immediately after drafting
2. If <90, identify what's missing/weak in the content
3. Ask PM 2-3 targeted questions for better seed input
4. Regenerate section with improved input
5. Re-assess quality
6. Repeat until section reaches 90+ (max 3 iterations per section)

---

## Quality Check Command

To run quality assessment on an Agent PRD:

```bash
./.claude/skills/agent-prd/scripts/quality-check.sh [path-to-prd.md]
```

**Output:**
- Overall score
- Section-by-section breakdown
- Specific improvement recommendations
- Focus areas for Quality Improvement iteration

