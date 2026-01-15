---
id:                         # Format: agent-prd-{YYYY}-{NNN} (e.g., "agent-prd-2025-001")
title:
type: agent-prd
status: draft               # draft | review | approved | archived
team:
owner:                      # Wiki-link to person (e.g., "[[people/adam-schoenfeld]]")
created:
updated:
tags: []
related: []

# Agent PRD-specific fields
agent_name:                 # The specific name of the agent
parent_capability:          # Parent capability this agent belongs to
target_ship:                # Target quarter or date (e.g., "Q2 2025" or "2025-06-15")
stakeholders: []            # List of wiki-links to people involved
problem_statement:          # One-line summary of the problem this agent solves
version: 1.0
---

# {Agent Name}

A structured approach to defining agent capabilities with clarity and precision

## 1. The Job to Be Done

Start with the user. What problem are they trying to solve? Write this in their language, not technical language. The goal is to ensure you deeply understand the user need before jumping to solutions.

### Problem Statement
In one or two sentences, what user problem does this agent solve?

[Describe the problem in user language]

### User Stories
Write user stories in standard format. Each story should represent a distinct use case this agent will handle. Aim for 3-5 stories that capture the core jobs.

**Format:** As a [role], I want to [action], so that [outcome]

1. [User story 1]
2. [User story 2]
3. [User story 3]

### Target User
Who specifically is this for? Be precise about persona, role, and context. An agent for SDRs is different from one for AEs, even if the task sounds similar.

[Persona, role, context, and any relevant constraints]

### Current State
How do users solve this problem today without the agent? Understanding the manual process reveals what the agent must replicate and where it can improve.

[Describe the manual workflow]

### Success from the User's Perspective
What does success feel like to the user? Not metrics, but the actual experience. "I got a great email draft in 10 seconds" is more useful here than "90% accuracy."

[Describe what success feels like]

### Forcing Question
**If you had to sell this agent as a standalone product, what would the one-sentence pitch be?**

[One-sentence pitch]

---

## 2. Scope & Decomposition

Right-sizing is critical. Too broad and the agent fails unpredictably. Too narrow and it's not useful. This section forces you to find the right level of decomposition and make boundaries explicit.

### Where This Fits
Place this agent in the hierarchy. What parent capability does it belong to? What are its siblings? This clarifies scope and prevents overlap.

**Parent Capability:** (e.g., "Email Writing")
[Parent capability name]

**Sibling Capabilities:** (e.g., "Cold Outbound, Active Deal, Win-back")
[List sibling capabilities at the same level]

**Why This Level of Decomposition:**
Justify why this is the right scope. Could it be decomposed further? If yes, why aren't you doing that?

[Rationale for this level of decomposition]

### The Boundary
Be explicit about what's in and what's out. If GTM sends you a failed query screenshot, you should be able to immediately say whether it was in-scope or out-of-scope. Ambiguity here causes problems later.

#### In-Scope Queries (15-20 examples)
List specific example queries this agent must handle successfully. These become your test cases.

1. **Query:** [Example query]
   - **Why In Scope:** [Rationale]

2. **Query:** [Example query]
   - **Why In Scope:** [Rationale]

3. **Query:** [Example query]
   - **Why In Scope:** [Rationale]

4. **Query:** [Example query]
   - **Why In Scope:** [Rationale]

5. **Query:** [Example query]
   - **Why In Scope:** [Rationale]

[Continue for 15-20 examples...]

#### Out-of-Scope Queries (15-20 examples)
List specific queries this agent should NOT attempt. Include the graceful rejection response for each.

1. **Query:** [Example query]
   - **Why Out of Scope:** [Rationale]
   - **Graceful Rejection:** [How agent responds]

2. **Query:** [Example query]
   - **Why Out of Scope:** [Rationale]
   - **Graceful Rejection:** [How agent responds]

3. **Query:** [Example query]
   - **Why Out of Scope:** [Rationale]
   - **Graceful Rejection:** [How agent responds]

4. **Query:** [Example query]
   - **Why Out of Scope:** [Rationale]
   - **Graceful Rejection:** [How agent responds]

5. **Query:** [Example query]
   - **Why Out of Scope:** [Rationale]
   - **Graceful Rejection:** [How agent responds]

[Continue for 15-20 examples...]

### Forcing Question
**If GTM sends you a failed query screenshot, can you immediately classify it as in-scope or out-of-scope?**

---

## 3. Opaque Executor Contract

Think of this agent as a vending machine. Clear inputs go in, clear outputs come out. If you can't describe the interface precisely, the agent isn't ready to build. This section defines the contract between the user and the agent.

### Inputs

#### Query Patterns
What types of queries trigger this agent? Be specific about patterns and variations.

[List query patterns that should route to this agent]

#### Required Identifiers
What identifiers must be present? Account ID? Contact ID? User context?

[List required identifiers]

#### Minimum Viable Input
What's the absolute minimum input needed to produce a valid response?

[Minimum input requirements]

### Outputs

#### Output Format
What form does the output take? Message, artifact, structured data, action?

[Describe output format]

#### Required Fields
What fields are always included in the output?

[List required output fields]

#### Conditional Fields
What fields appear only in certain conditions?

[List conditional fields and their conditions]

#### Uncertainty Handling
How does the agent communicate missing data or low confidence?

[Describe how uncertainty is communicated]

---

## 4. Context Requirements

What data enables the output? For each data source, be specific about what you're retrieving and why it matters. "What Context This Provides" is critical: it forces you to articulate what each piece of data actually contributes to the agent's ability to respond.

### Data Sources

1. **Data Source:** [e.g., Salesforce]
   - **Objects/Fields:** [e.g., Account.Name, Account.Industry, Opportunity.Stage]
   - **What Context This Provides:** [How this data enables the agent's response]
   - **Required?** [Yes/No]
   - **Fallback:** [What happens if unavailable]

2. **Data Source:** [e.g., Chorus]
   - **Objects/Fields:** [Specific fields]
   - **What Context This Provides:** [How this data enables the agent's response]
   - **Required?** [Yes/No]
   - **Fallback:** [What happens if unavailable]

3. **Data Source:** [e.g., User context]
   - **Objects/Fields:** [Specific fields]
   - **What Context This Provides:** [How this data enables the agent's response]
   - **Required?** [Yes/No]
   - **Fallback:** [What happens if unavailable]

[Continue for all data sources...]

### Minimum Context for Valid Response
What's the minimum data needed to produce something useful? If Salesforce is down but Chorus is available, can you still respond?

[Describe minimum context requirements]

### Ideal Retrieval Order
If order matters (e.g., for efficiency or logic), specify it here.

[Describe retrieval order if applicable]

---

## 5. Ideal Flow

This is not a rigid workflow. Agents are not deterministic. But you should be able to describe what a typical successful run looks like. If you can't walk through this step by step, you don't understand the problem well enough to build a solution.

### Typical Successful Run
Walk through what the agent probably does in a representative case. Use a concrete example.

1. **User submits:** [example query]

   [Example user input]

2. **Agent interprets:** [what it understands from the query]

   [What the agent understands]

3. **Agent retrieves:** [context gathering steps]

   [Context retrieval steps]

4. **Agent reasons:** [key decisions and transformations]

   [Reasoning and transformation steps]

5. **Agent responds:** [output to user]

   [Example output]

### Key Decision Points
Where might the agent need to branch? What conditions change the path?

[Describe branching logic and conditions]

### Failure Handling
At each step, what could go wrong? How should the agent handle it?

[Describe failure modes and handling]

### Forcing Question
**Could a smart person with no prior context follow this flow and complete the task manually?**

---

## 6. Test Cases

Test cases are the contract between product and engineering. If the agent passes these tests, it's done. If it fails, we know exactly what's broken. Write these before engineering begins. If you can't write test cases, you don't understand the problem well enough.

### Must Succeed (10-15 cases)
These are inputs where the agent must produce a correct response. Be specific about expected behavior and output.

1. **Input:** [Test case input]
   - **Expected Behavior:** [What the agent should do]
   - **Pass Criteria:** [How to verify success]

2. **Input:** [Test case input]
   - **Expected Behavior:** [What the agent should do]
   - **Pass Criteria:** [How to verify success]

3. **Input:** [Test case input]
   - **Expected Behavior:** [What the agent should do]
   - **Pass Criteria:** [How to verify success]

4. **Input:** [Test case input]
   - **Expected Behavior:** [What the agent should do]
   - **Pass Criteria:** [How to verify success]

5. **Input:** [Test case input]
   - **Expected Behavior:** [What the agent should do]
   - **Pass Criteria:** [How to verify success]

[Continue for 10-15 cases...]

### Must Reject or Redirect (10-15 cases)
These are inputs the agent should recognize as out of scope and handle gracefully.

1. **Input:** [Test case input]
   - **Why Out of Scope:** [Rationale]
   - **Expected Response:** [How agent should handle]

2. **Input:** [Test case input]
   - **Why Out of Scope:** [Rationale]
   - **Expected Response:** [How agent should handle]

3. **Input:** [Test case input]
   - **Why Out of Scope:** [Rationale]
   - **Expected Response:** [How agent should handle]

4. **Input:** [Test case input]
   - **Why Out of Scope:** [Rationale]
   - **Expected Response:** [How agent should handle]

5. **Input:** [Test case input]
   - **Why Out of Scope:** [Rationale]
   - **Expected Response:** [How agent should handle]

[Continue for 10-15 cases...]

### Edge Cases
What happens in unusual situations? Missing data, ambiguous intent, partial information?

1. **Scenario:** [Edge case description]
   - **Expected Behavior:** [How agent should handle]

2. **Scenario:** [Edge case description]
   - **Expected Behavior:** [How agent should handle]

3. **Scenario:** [Edge case description]
   - **Expected Behavior:** [How agent should handle]

4. **Scenario:** [Edge case description]
   - **Expected Behavior:** [How agent should handle]

5. **Scenario:** [Edge case description]
   - **Expected Behavior:** [How agent should handle]

---

## 7. Dependencies

Surface blockers early. Nothing derails a project faster than discovering halfway through that a required integration doesn't exist.

### Tools & Integrations

1. **Tool/Integration:** [e.g., Salesforce API]
   - **Currently Available?** [Yes/No]
   - **Lift if Not Available:** [What work is needed]

2. **Tool/Integration:** [e.g., Email service]
   - **Currently Available?** [Yes/No]
   - **Lift if Not Available:** [What work is needed]

3. **Tool/Integration:** [e.g., Analytics platform]
   - **Currently Available?** [Yes/No]
   - **Lift if Not Available:** [What work is needed]

[Continue for all required tools...]

### Data Sources
What happens for users who don't have required data sources connected?

[Describe handling for disconnected data sources]

### Other Teams
Who else needs to be involved? What are we waiting on?

[List cross-team dependencies]

### Blockers
What must be true before this can be built?

[List hard blockers]

---

## 8. Prompt Structure

Every instruction in a prompt should be measurable. If you can't articulate how you'd evaluate whether an instruction is working, why is it in the prompt? This section forces logical thinking about agent behavior.

### Core Instructions
List each key instruction with its evaluation criteria. Format: What you're telling the agent to do, and how you'd verify it's doing it.

1. **Instruction:** [e.g., "Always cite the data source when referencing specific information"]
   - **Evaluation Criteria:** [e.g., "Does output cite sources? Are citations accurate?"]

2. **Instruction:** [Agent instruction]
   - **Evaluation Criteria:** [How to measure if it's working]

3. **Instruction:** [Agent instruction]
   - **Evaluation Criteria:** [How to measure if it's working]

4. **Instruction:** [Agent instruction]
   - **Evaluation Criteria:** [How to measure if it's working]

5. **Instruction:** [Agent instruction]
   - **Evaluation Criteria:** [How to measure if it's working]

[Continue for all key instructions...]

### Agent Description
How does this agent describe itself to the orchestrator? This is used for routing.

[Draft agent description for registry]

### Forcing Question
**For each instruction, can you articulate how you'd measure whether it's working? If not, why is it in the prompt?**

---

## 9. Human-in-the-Loop Design

Users prefer quick confirmation dialogs to long waits followed by wrong results. This section defines when and how the agent should involve the user.

### Confirmation Required?
Does this agent execute immediately or present a plan first?

[Yes/No and rationale]

### Plan Presentation
If confirmation is required, what does the "plan" look like that we show users?

[Describe the plan format]

### Check-in Points
At what points should the agent pause and ask for input?

[List check-in points]

### User vs Agent Decisions
What decisions should the user make vs. the agent?

[Describe decision ownership]

---

## 10. Metrics

Unit economics matter. If we can't forecast cost and value, we can't make good decisions. This section requires you to think through performance, cost, and value.

### Performance

- **Expected Latency:** [e.g., "2-3 seconds"]
- **Expected Input Tokens:** [e.g., "~500 tokens"]
- **Expected Output Tokens:** [e.g., "~300 tokens"]
- **Model(s) Used:** [e.g., "Claude 3.5 Sonnet"]

### Cost & Credits

- **Expected AI Credits per Run:** [e.g., "5 credits"]
- **Recommended Margin:** [High / Medium / Low]
- **Margin Rationale:** [Why this margin level]

### Market Comparable
What's the next best alternative? How does our value compare?

**Alternative Solution:**
[Competitor tool, manual labor, or other alternative]

**Alternative Cost:**
[What users pay for the alternative]

**Value Comparison:**
[How our unit economics compare]

### Monitoring
How do we know it's working in production?

[Describe monitoring approach, success signals, and failure indicators]

---

## 11. Data Flywheel

ZoomInfo's value compounds when customer interactions generate data that benefits other customers. This section asks: what exhaust does this agent create, and how does it contribute to our data assets? Not every agent will have a flywheel contribution, but the question should always be asked.

### Data Generated
What data does this agent create through usage?

[Describe data generated]

### Flywheel Contribution
How could this data benefit other customers or improve our data assets?

[Describe flywheel contribution (or "N/A" if not applicable)]

---

## 12. Competitive Comparative

Before building, understand the baseline. What happens if you try this today? What do competitors do? This grounds your design in reality and clarifies where you're adding value.

### Current State (Copilot Chat)
Run your test cases against current co-pilot chat. Document what happens.

[Results from testing in current co-pilot]

**Why is this unsatisfactory?**

[Gaps and limitations in current state]

### Claude / ChatGPT
Run your test cases against Claude and/or ChatGPT. Document results.

[Results from testing in Claude/ChatGPT]

**What do they get right?**

[Strengths of general-purpose models]

**What do they miss?**

[Gaps that our agent addresses]

### Forcing Question
**What does our agent do that a user couldn't accomplish by just asking Claude with the right context?**

---

## 13. Rollout & Communication

Users need to know what this does and doesn't do. Implicit boundaries become explicit frustrations. This section ensures you've thought through how to set expectations.

### What We Tell Users It Does
[User-facing capability description]

### What We Tell Users It Doesn't Do
[Explicit limitations to communicate]

### Release Notes Draft
[Draft release notes]

### Enablement Needs
[Training, documentation, or support requirements]

---

## Final Checklist

Complete this checklist before requesting PRD review. Every item should be checked.

- [ ] I can state the job to be done in one sentence
- [ ] I've confirmed this is the right level of decomposition
- [ ] I can immediately classify any query as in-scope or out-of-scope
- [ ] A smart person with no prior context could follow my ideal flow manually
- [ ] I have 30+ test cases written (in-scope, out-of-scope, and edge cases)
- [ ] All dependencies are identified and accounted for
- [ ] Every prompt instruction has evaluation criteria
- [ ] I've estimated credits per run and recommended margin
- [ ] I've documented market comparables for unit economics
- [ ] I've tried this in current co-pilot chat and documented results
- [ ] I've tried this in Claude/ChatGPT and documented results
- [ ] I've considered data flywheel contribution
- [ ] I've tried to build this myself on the platform and documented what happened

---

## Approval

- **PM Author:** [Name] - [Date]
- **Engineering Lead:** [Name] - [Date]
- **Product Leadership:** [Name] - [Date]
