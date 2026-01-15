---
id: doc-2026-002
title: Agent PRD Skill
type: doc
status: draft
owner: [[teams\ops\_people\brett-jacobs]]
created: 2026-01-13
updated: 2026-01-13
tags: []
related: []
---

# Agent PRD Skill

**Description:** Guide Product Managers through creating world-class Agent PRDs for ZoomInfo's Agentic Platform (ZAP) following best practices.

**Purpose:** Act as an AI co-writer who interviews the PM, helps them think through requirements systematically, and produces an A+ PRD that's ready for review and implementation.

**Target Efficiency:** Complete high-quality Agent PRD in 30-60 minutes (vs. 8+ hours manual)

**Trigger:** Use this skill when users want to create an Agent PRD document.

**Strong triggers** (always use this skill):
- "agent prd" / "prd agent" / "agent PRD" / "PRD agent"
- "prd for agent" / "prd for an agent"
- "I need to create an Agent PRD" / "create an Agent PRD" / "write an Agent PRD"
- "I need to write a PRD for an agent" / "write a PRD for an agent"
- "help me write an agent PRD" / "agent PRD"
- "/agent-prd" (slash command)

**Conditional triggers** (check if agent-related):
- "I need to write a PRD" - Ask: "Is this for an agent/AI capability?" If yes, use this skill. If no, use create-doc skill.
- "create a PRD" - Ask: "Is this for an agent?" If yes, use this skill. If no, use create-doc skill.

**Do NOT trigger** for:
- Non-agent PRDs (use create-doc skill instead)
- General help requests
- Document search queries

## How This Skill Works

This skill follows a structured interview process covering all 13 sections of the Agent PRD template. The AI:

1. **Gathers context upfront** - PM provides relevant documents before starting
2. **Asks batched questions** - Groups related questions for efficiency
3. **Generates draft content** - PM reviews and refines rather than writes from scratch
4. **Validates against best practices** - References foundational documentation throughout
5. **Scores quality** - Assesses each section against quality criteria
6. **Iterates using Quality Improvement** - Improves low-scoring sections by asking targeted questions
7. **Manages PR workflow** - Guides through review and approval process

## Before You Start

### Required Reading

If you haven't already, familiarize yourself with:
- [teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md)
- [teams/intelligence/documentation/agent-best-practices/prompt-writing-guide.md](../../../teams/intelligence/documentation/agent-best-practices/prompt-writing-guide.md)
- [teams/intelligence/documentation/agent-best-practices/prompt-assertion-evaluation-framework.md](../../../teams/intelligence/documentation/agent-best-practices/prompt-assertion-evaluation-framework.md)

### Gather Context Documents

**CRITICAL:** Before starting the interview, gather all relevant context:

1. **Existing PRDs or design docs** that relate to this agent
2. **User research or feedback** that informed this agent idea
3. **Competitive analysis** you've done (testing in Claude, ChatGPT, current co-pilot)
4. **Similar agents** we've built that this relates to
5. **Technical constraints** or platform limitations you're aware of

Have these ready to paste/link when prompted. The more context you provide upfront, the faster and better the interview will go.

## 💡 PRO TIP: Use Voice-to-Text

This interview works best when you provide rich context. Voice-to-text makes answering fast:

- **Windows:** Win + H
- **Mac:** Fn + Fn (or Enable Dictation in System Preferences)
- **Mobile:** Use built-in voice keyboard

Speaking your answers is 3-4x faster than typing and gives me the context I need to write accurately on the first draft. Think of me as your brilliant ghostwriter—you provide the thinking, I do the writing.

## Interview Process

### Phase 1: Initialization

1. **Load template** from [_templates/agent-prd.md](../../../_templates/agent-prd.md)
2. **Load best practices** from agent-best-practices folder
3. **Gather context from PM:**

```
Let's create an excellent Agent PRD together. This will take 30-60 minutes of focused work.

💡 TIP: Use voice-to-text (Win+H on Windows, Fn+Fn on Mac) to answer questions quickly!

First, I need context. Please provide any documents that relate to this agent:

📄 Existing PRDs or design docs?
📊 User research or feedback?
🔍 Competitive analysis (tested in Claude/ChatGPT/co-pilot)?
🏗️  Similar agents we've built?
⚙️  Technical constraints or platform limitations?

**How to provide documents:**
- **If document is in the PM repo**: Use wiki-link syntax like [[teams/intelligence/documentation/...]]
- **If document is on your computer**: Provide the full file path (e.g., C:\Users\YourName\Documents\research.docx) and I'll read it
- **If you want to paste directly**: Just paste the content inline

The more context you give me now, the better I can help you write this PRD efficiently.
```

4. **Ingest and index** all provided context for reference throughout interview

### Phase 2: Section-by-Section Interview

For each of the 13 sections, follow this pattern:

#### Interview Pattern

```markdown
## Section X: [Section Name]

**Purpose:** [Why this section matters, from best practices]

**Reference:** [Link to relevant best practice section]

---

**Questions (answer all together - use voice-to-text for speed!):**

1. [Question 1] ← **Best practice**: [specific principle from foundational docs]
2. [Question 2] ← **Best practice**: [specific principle from foundational docs]
3. [Question 3] ← **Best practice**: [specific principle from foundational docs]
...

[Wait for PM's batched answers]

---

**Here's what I've drafted based on your answers:**

[Generated section content - AI expands from PM's seeds using patterns + best practices]

---

**Critical Review (confirm these key decisions before we continue):**
1. [Specific decision point 1 that requires PM judgment]
2. [Specific decision point 2 that requires PM judgment]
3. [Specific decision point 3 that requires PM judgment]

⚠️  **MANDATORY**: Please read this section carefully. You must stand behind every detail before we proceed. Does this accurately capture your intent? Any changes needed?

[Wait for explicit confirmation]

---

**Quality Assessment:**
Evaluating this section against best practices criteria...

- [Criterion 1]: ✅/❌ (e.g., "15 in-scope examples present")
- [Criterion 2]: ✅/❌ (e.g., "Examples have specific rationale")
- [Criterion 3]: ✅/❌ (e.g., "Examples are diverse, not all same query type")

**Score: X/100** (Target: 90+)

[If score >= 90]: ✅ Section meets quality bar! Moving to next section.

[If score < 90]:
⚠️  This section scored low because: [Objective analysis of what's missing/weak in the content]

**Example diagnostic messages:**
- "The 15 in-scope examples lack diversity - they're all variations of the same query type. I need more varied seed examples from you."
- "The out-of-scope examples don't have clear rejection language. What should the agent say when asked [specific example]?"
- "The decomposition justification is vague. Could you actually write step-by-step instructions for this task?"

**To improve this section to 90+, I need:**
1. [Targeted question for better seed input]
2. [Targeted question for missing context]
3. [Optional 3rd question if needed]

[Wait for answers → Regenerate section → Re-assess]
[Max 3 iterations per section]
```

### Section 1: Job to Be Done

**Opening Context:**
"Let's start by deeply understanding the user problem. The best agents come from really understanding what users need, not jumping to solutions. This section is about empathy and clarity."

**Reference:** [Understanding User Needs](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#understanding-user-needs)

#### If PM Provided Context Docs:
- Extract user stories automatically
- Extract problem statements
- Extract success criteria
- Present draft for PM to refine

#### If No Context Docs:
**Questions (answer all together - use voice-to-text for speed!):**

1. **Problem Statement:** In one or two sentences, what user problem does this agent solve? Use their language, not technical terms.
   - ← **Best practice**: Always use user language, not technical jargon ([Understanding User Needs](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#understanding-user-needs))

2. **Target User:** Who specifically is this for? Their role, context, and constraints.
   - ← **Best practice**: Clear persona definition enables focused design

3. **Current State:** How do they solve this today manually? Brief workflow.
   - ← **Best practice**: Understanding current state justifies why change is needed

4. **Success Feel:** What does success feel like to them? (Not metrics, but experience - e.g., "I got a great email draft in 10 seconds and only needed to change one sentence")
   - ← **Best practice**: Experiential success criteria (not just metrics) guides design

5. **One-Sentence Pitch:** If you had to sell this as a standalone product, what's the pitch?
   - ← **Best practice**: Forcing question ensures clarity of value proposition

**Generate complete Section 1 draft:**
- Problem statement
- 3-5 user stories (derived from answers)
- Target user details
- Current state workflow
- Success from user's perspective
- One-sentence pitch

**Quality Checklist:**
- [ ] Problem statement in user language (not technical jargon)
- [ ] 3-5 specific user stories in standard format
- [ ] Target persona clearly defined with role and context
- [ ] Current state workflow documented
- [ ] Success described experientially (not just metrics)
- [ ] Forcing question answered with compelling one-sentence pitch

**Score Target:** 90+/100

### Section 2: Scope & Decomposition

**Opening Context:**
"Now let's define boundaries. This is critical. Too broad and the agent fails unpredictably. Too narrow and it's not useful. We need to find the sweet spot."

**Reference:** [Task Decomposition](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#task-decomposition)

**Questions (answer all together - use voice-to-text for speed!):**

1. **Hierarchy:** What parent capability does this agent belong to?
   - *Examples: Email writing → Cold Outbound, Active Deal, Win-back*
   - *Examples: Account research → Account Summary, Competitive Analysis, Stakeholder Mapping*
   - ← **Best practice**: Task decomposition clarifies scope ([Task Decomposition](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#task-decomposition))

2. **Siblings:** What are the sibling capabilities at the same level?
   - ← **Best practice**: Identifying siblings ensures clear boundaries between agents

3. **Decomposition Justification:** Why is this the right level of decomposition? Could it be more specific or more general?
   - *Apply the manual test: Could you write step-by-step instructions for how to accomplish this?*
   - ← **Best practice**: The "manual test" validates right level of specificity

4. **Boundary Examples:** Give me 2-3 in-scope queries this MUST handle, and 2-3 out-of-scope queries it should reject.
   - ← **Best practice**: Explicit boundaries prevent scope creep and confusion

**Smart Expansion:**
- PM gives 2-3 examples each
- AI expands to 15-20 in-scope with rationale
- AI expands to 15-20 out-of-scope with graceful rejection responses
- PM reviews and adjusts outliers

**Quality Checklist:**
- [ ] Parent capability identified
- [ ] Sibling capabilities listed
- [ ] Decomposition level justified (manual test passed)
- [ ] 15-20 in-scope query examples with rationale
- [ ] 15-20 out-of-scope query examples with graceful rejection responses
- [ ] Forcing question answered: Can you immediately classify any query as in/out?

**Score Target:** 90+/100

### Section 3: Opaque Executor Contract

**Opening Context:**
"This section defines the black box. Clear inputs → Clear outputs. If it doesn't pass the vending machine test, it's not ready."

**Reference:** [The Vending Machine Test](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#the-vending-machine-test)

**Questions:**

1. **Required Inputs:** What data must be provided for this agent to work? (Account ID, user context, etc.)
   - ← **Best practice**: Explicit required inputs ensure vending machine clarity

2. **Optional Inputs:** What additional context improves results but isn't required?
   - ← **Best practice**: Distinguishing required vs optional prevents ambiguity

3. **Output Format:** What exactly does the user get back? Be specific about structure.
   - ← **Best practice**: Clear output specification completes the contract

4. **Vending Machine Test:** Can you describe this as "put X in, get Y out" with no ambiguity?
   - ← **Best practice**: The vending machine test validates clarity ([The Vending Machine Test](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#the-vending-machine-test))

**Quality Checklist:**
- [ ] All required inputs explicitly listed
- [ ] Optional inputs identified
- [ ] Output format clearly specified
- [ ] Passes vending machine test (clear X → Y)

**Score Target:** 90+/100

### Section 4: Context Requirements

**Opening Context:**
"What data sources does this agent need? Remember the 10x rule: context should be 10x the length of expected output."

**Reference:** [Context Quality and the 10x Rule](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#context-quality-and-the-10x-rule)

**Questions:**

1. **Data Sources:** What specific data sources are required? (e.g., Salesforce opportunities, Chorus call summaries, ZoomInfo company data)
   - ← **Best practice**: Enumerate all data sources explicitly

2. **Context Justification:** For each source, explicitly state: "What specific context does this provide that enables the agent's response?"
   - ← **Best practice**: Each data source must justify its inclusion

3. **10x Compliance:** If output is ~500 words, do you have ~5,000 words of context? If not, what's missing?
   - ← **Best practice**: The 10x rule ensures sufficient context ([Context Quality and the 10x Rule](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#context-quality-and-the-10x-rule))

4. **Context Quality:** Is this "steak" (dense, relevant) or "popcorn" (verbose, low-value)?
   - ← **Best practice**: High-quality dense context beats low-quality verbose context

**Quality Checklist:**
- [ ] All data sources explicitly listed
- [ ] Each source has clear justification (what context it provides)
- [ ] 10x rule compliance verified
- [ ] Context quality assessed (steak > popcorn)

**Score Target:** 90+/100

### Section 5: Ideal Flow

**Opening Context:**
"Walk through the happy path step by step. How does this actually work when everything goes right?"

**Questions:**

1. **Step-by-step:** User submits query → Agent does what → User sees what?
   - ← **Best practice**: Document the complete happy path

2. **Human-in-the-Loop:** Should the agent propose a plan first and get confirmation? Or execute immediately?
   - *Guideline: If complex (multiple steps, data synthesis), use confirmation. If simple (single lookup), execute immediately.*
   - ← **Best practice**: Justify human-in-the-loop decisions ([Human in the Loop](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#human-in-the-loop))

3. **Timeline:** What's a reasonable response time expectation?
   - ← **Best practice**: Set realistic timeline expectations

**Quality Checklist:**
- [ ] Step-by-step flow documented
- [ ] Human-in-the-loop decision justified
- [ ] Timeline expectation set

**Score Target:** 90+/100

### Section 6: Test Cases

**Opening Context:**
"This is where the rubber meets the road. You need 30+ test cases: 10-15 success, 10-15 rejection, edge cases."

**Reference:** [The Test Case Requirement](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#the-test-case-requirement)

**Questions:**

1. **Must Succeed Cases:** Give me 2-3 core examples of queries that absolutely must work.
   - ← **Best practice**: Test cases form the contract between product and engineering ([The Test Case Requirement](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#the-test-case-requirement))

2. **Must Reject Cases:** Give me 2-3 examples of queries that should be gracefully rejected or redirected.
   - ← **Best practice**: Rejection cases define scope boundaries clearly

3. **Edge Cases:** What tricky scenarios might trip this up?
   - ← **Best practice**: Edge cases prevent unexpected failures

**Smart Expansion:**
- PM gives 2-3 examples per category
- AI expands to 10-15 success cases with input/behavior/pass criteria
- AI expands to 10-15 rejection cases with rationale and expected response
- AI adds 5+ edge cases with handling described
- PM reviews and adjusts

**Quality Checklist:**
- [ ] 10-15 "Must Succeed" cases with input/behavior/pass criteria
- [ ] 10-15 "Must Reject or Redirect" cases with rationale and expected response
- [ ] 5+ edge cases with handling described
- [ ] Each test case is specific and measurable
- [ ] Test cases align with scope boundaries from Section 2
- [ ] Covers critical user paths from Section 1

**Score Target:** 90+/100

### Section 7: Dependencies

**Opening Context:**
"What needs to exist for this to work? Tools, data sources, other agents?"

**Questions:**

1. **Platform Dependencies:** What ZAP capabilities does this require?
   - ← **Best practice**: Enumerate platform requirements explicitly

2. **Data Dependencies:** What data sources must be integrated?
   - ← **Best practice**: List required data integrations

3. **Tool Dependencies:** What tools must be available?
   - ← **Best practice**: Identify required tooling

4. **Blockers:** What's missing today that would prevent this from working?
   - ← **Best practice**: Surface blockers early to inform roadmap

**Quality Checklist:**
- [ ] Platform dependencies listed
- [ ] Data dependencies listed
- [ ] Tool dependencies listed
- [ ] Blockers identified

**Score Target:** 90+/100

### Section 8: Prompt Structure

**Opening Context:**
"Now we design the actual prompt using atomic assertions with evaluation criteria. Every instruction must be measurable."

**Reference:** [Atomic Prompt Decomposition](../../../teams/intelligence/documentation/agent-best-practices/prompt-writing-guide.md#atomic-prompt-decomposition)

**Prompt Assertion Evaluation Integration:**

For each behavioral instruction, ask: **"How would you evaluate if this is working?"**

**Example Format:**

| Instruction | Evaluation Criteria |
|------------|-------------------|
| "Always cite the data source when referencing specific metrics" | - Does output cite sources when mentioning specific numbers?<br>- Are citations accurate?<br>- Are citations present for all factual claims? |
| "If required context is missing, acknowledge the gap rather than guessing" | - When key data is absent, does output explicitly note this?<br>- Does output avoid fabricating information to fill gaps?<br>- Is acknowledgment specific about what's missing? |

**Questions:**

1. **Agent Description:** How would you describe this agent to the orchestrator for routing? (One sentence)
   - ← **Best practice**: Clear agent description enables proper orchestration

2. **Behavioral Instructions:** What are the 5-10 key behaviors this agent must exhibit?

For each behavior:
- State the instruction as an atomic assertion
- Define 2-3 evaluation criteria
- Ensure it's measurable (could be evaluated by LLM-as-judge)
- ← **Best practice**: Atomic assertions with evaluation criteria enable systematic testing ([Atomic Prompt Decomposition](../../../teams/intelligence/documentation/agent-best-practices/prompt-writing-guide.md#atomic-prompt-decomposition))

3. **Prompt Structure:** Following best practices:
   - Static content first (identity, instructions, output format)
   - Dynamic content last (retrieved context, user query)
   - Optimized for prompt caching
   - ← **Best practice**: Static-first structure enables efficient prompt caching

**Quality Checklist:**
- [ ] Each instruction has evaluation criteria
- [ ] Instructions follow atomic assertion pattern
- [ ] Agent description for orchestrator routing is clear
- [ ] Forcing question answered: Can you measure if each instruction works?
- [ ] Optimized for prompt caching (static first, dynamic last)

**Score Target:** 90+/100

### Section 9: Human-in-the-Loop Design

**Opening Context:**
"For complex operations: propose first, execute after confirmation. For simple operations: execute immediately."

**Reference:** [Human in the Loop](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#human-in-the-loop)

**Questions:**

1. **Confirmation Pattern:** What exactly does the agent show for confirmation before executing?
   - ← **Best practice**: Clear confirmation pattern prevents unwanted actions

2. **Skip Conditions:** When can we skip confirmation? (Simple lookups, obvious operations)
   - ← **Best practice**: Justify when confirmation can be skipped ([Human in the Loop](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md#human-in-the-loop))

3. **Error Handling:** What happens when execution fails? How do we communicate it?
   - ← **Best practice**: Define error paths explicitly

**Quality Checklist:**
- [ ] Confirmation pattern clearly defined
- [ ] Skip conditions justified
- [ ] Error handling documented

**Score Target:** 90+/100

### Section 10: Metrics

**Opening Context:**
"How do we know if this agent is successful? What do we measure?"

**Questions:**

1. **Usage Metrics:** Queries per day, unique users, etc.
   - ← **Best practice**: Track adoption and engagement

2. **Quality Metrics:** Thumbs up/down rate, assertion pass rate, etc.
   - ← **Best practice**: Measure output quality systematically

3. **Business Metrics:** Impact on pipeline, deal velocity, user productivity, etc.
   - ← **Best practice**: Connect to business outcomes

**Quality Checklist:**
- [ ] Usage metrics defined
- [ ] Quality metrics defined
- [ ] Business metrics defined

**Score Target:** 90+/100

### Section 11: Data Flywheel

**Opening Context:**
"How does this agent get better over time? What data feeds back into improvements?"

**Questions:**

1. **Feedback Collection:** How do we collect user feedback on outputs?
   - ← **Best practice**: Systematic feedback enables continuous improvement

2. **Improvement Loop:** How does feedback inform prompt/context improvements?
   - ← **Best practice**: Close the loop from feedback to improvements

3. **Data Capture:** What data from usage improves future performance?
   - ← **Best practice**: Capture usage patterns to refine agent behavior

**Quality Checklist:**
- [ ] Feedback collection mechanism defined
- [ ] Improvement loop documented
- [ ] Data capture strategy outlined

**Score Target:** 90+/100

### Section 12: Competitive Comparative

**Opening Context:**
"How does this compare to what users can do today? What gaps exist that justify building this?"

**Automation Offer:**
"I can help test your test cases in current co-pilot or Claude. Want me to run comparative analysis?"

**Questions:**

1. **Current State:** What do users do today? (Manual workflow, existing tools, co-pilot)
   - ← **Best practice**: Document current state to justify investment

2. **Testing Results:** Have you tested the use cases in current co-pilot? What worked/didn't work?
   - ← **Best practice**: Test alternatives before building custom solution

3. **Gap Analysis:** What specific gaps exist that this custom agent will fill?
   - ← **Best practice**: Explicit gap analysis justifies custom build

4. **Why Build This:** One clear sentence: Why is building a custom agent worth the investment?
   - ← **Best practice**: Forcing question validates investment decision

**Quality Checklist:**
- [ ] Current state documented
- [ ] Testing results captured (what works/doesn't in existing solutions)
- [ ] Gap analysis specific and justified
- [ ] Clear answer to "why build this?"

**Score Target:** 90+/100

### Section 13: Rollout & Communication

**Opening Context:**
"How do we ship this? Who needs to know? What are the rollout steps?"

**Questions:**

1. **Rollout Plan:** Phased? All-at-once? Specific user groups first?
   - ← **Best practice**: Define rollout strategy explicitly

2. **Communication:** Who needs to be informed? What messaging?
   - ← **Best practice**: Identify stakeholders and communication plan

3. **Training:** Do users need training? Documentation?
   - ← **Best practice**: Plan for user enablement

4. **Success Criteria:** What does "successful rollout" look like?
   - ← **Best practice**: Define rollout success metrics

**Quality Checklist:**
- [ ] Rollout plan documented
- [ ] Communication plan defined
- [ ] Training needs identified
- [ ] Success criteria clear

**Score Target:** 90+/100

---

## Quality Evaluation Function

When the user says "run quality check on [prd-file]" or invokes the quality-check.sh script, Claude Code will perform LLM-as-judge evaluation:

### Evaluation Process

1. **Load the PRD file** and extract all 13 sections
2. **Load quality criteria** from `.claude/skills/agent-prd/references/quality-criteria.md`
3. **For each section**, evaluate against its specific rubric:
   - Check all pass criteria (checkboxes)
   - Count satisfied vs. unsatisfied criteria
   - Assess content quality (depth, clarity, specificity)
   - Assign score based on scoring guidelines (100/90/80/70/<70)
   - Generate specific improvement recommendations

4. **Calculate overall score** (average of all 13 section scores)
5. **Identify focus areas** (sections scoring <90, prioritized by impact)
6. **Format output** with colored indicators and actionable recommendations

### Scoring Methodology

Each section uses this rubric structure (from quality-criteria.md):

**Pass Criteria:** Specific, measurable requirements
**Scoring Guidelines:** Clear scoring bands (100/90/80/70/<70) with descriptions
**Common Issues:** Typical failure patterns to watch for

**Example for Section 6 (Test Cases):**
- **100 points:** 30+ test cases, comprehensive coverage, specific pass criteria
- **90 points:** 25-30 test cases, good coverage
- **80 points:** 20-25 test cases, adequate coverage
- **70 points:** 15-20 test cases, some gaps
- **<70 points:** <15 test cases or poor coverage

### LLM Evaluation Prompt Template

```xml
<role>
You are evaluating an Agent PRD section against quality criteria.
Be strict but fair. Use the scoring guidelines precisely.
</role>

<section_to_evaluate>
{section_content}
</section_to_evaluate>

<quality_criteria>
{section_specific_criteria_from_quality-criteria.md}
</quality_criteria>

<instructions>
1. Check each pass criterion - is it satisfied? (yes/no with evidence)
2. Count how many criteria are met
3. Assess content quality (depth, clarity, specificity)
4. Assign score using the scoring guidelines
5. Identify 1-3 specific improvements needed
6. Output JSON:
{
  "section": "Section Name",
  "score": 85,
  "criteria_met": 5,
  "criteria_total": 7,
  "strengths": ["..."],
  "improvements_needed": ["..."],
  "justification": "One sentence explaining the score"
}
</instructions>
```

---

## Phase 3: Final Verification

After all 13 sections are complete (each already assessed and verified at 90+), run a quick sanity check:

```
🎉 All 13 sections complete! Running final verification...

**Quick Sanity Check:**
- ✅ All sections still meet 90+ quality bar
- ✅ Cross-references between sections are consistent
- ✅ No obvious gaps or contradictions

Your Agent PRD is ready for review!
```

If any section unexpectedly drifted below 90 (unlikely since each was verified individually):
- Flag the specific section
- Ask 1-2 targeted questions to resolve the issue
- Re-verify quickly

---

## Phase 3.5: Save Agent PRD to Repository

After all 13 sections are verified, immediately save the PRD to disk while content is fresh in memory.

### Step 1: Auto-infer Team & Owner

**Find the PM's person doc to determine team:**

```bash
# Get git username
git config user.name

# Search for their person doc
find teams/ -path "*/\_people/*.md" -type f -exec grep -l "title: [their name from git]" {} \;
```

**If no person doc found:**
```
⚠️  I don't see your person doc yet. Let me help set that up first before saving this PRD.

Please run: "onboard me"

After onboarding, we can save your Agent PRD.
```

**STOP** - do not proceed with file save until person doc exists.

**If person doc found:**
- Extract team from person doc frontmatter (e.g., `team: intelligence`)
- Extract subteam if present (e.g., `subteam: context-engineering`)
- Continue to Step 2

### Step 2: Generate Sequential ID

```bash
# Find existing Agent PRDs for current year
find teams/ -path "*/working_docs/prds/*.md" -type f | \
  xargs grep -h "^id: agent-prd-2026-" 2>/dev/null | \
  sed "s/id: agent-prd-2026-//" | \
  sort -n | tail -1

# Next ID = max + 1 (e.g., if max is 002, next is 003)
# Format: agent-prd-2026-003 (zero-padded, 3 digits)
```

### Step 3: Generate Filename from Agent Name

Take the agent name from Section 1 and convert to kebab-case:

**Examples:**
- "GTMBench Agent" → `gtmbench-agent-prd.md`
- "Cold Email Writer" → `cold-email-writer-prd.md`
- "Account Research Assistant" → `account-research-assistant-prd.md`

### Step 4: Determine File Path

**Pattern:**
```
teams/{team}/working_docs/prds/{filename}
```

**For hierarchical teams (with subteam):**
```
teams/{team}/[subteam]-{subteam}/working_docs/prds/{filename}
```

**Examples:**
- Flat team (gtm-studio): `teams/gtm-studio/working_docs/prds/gtmbench-agent-prd.md`
- Hierarchical (intelligence/context-engineering): `teams/intelligence/[subteam]-context-engineering/working_docs/prds/gtmbench-agent-prd.md`

### Step 5: Write File with Minimal Frontmatter

**CRITICAL: Use minimal frontmatter - let pre-commit hook enrich team, owner, dates**

```yaml
---
id: agent-prd-2026-003
title: GTMBench Agent PRD
type: agent-prd
status: draft
tags: []
related: []

# Agent PRD-specific fields
agent_name: GTMBench
parent_capability: Account Research
target_ship: Q1 2026
stakeholders: []
problem_statement: [One-line summary from Section 1]
version: 1.0
---

# GTMBench Agent

[All 13 sections from interview, with careful markdown formatting]
```

**Markdown Formatting Guidelines (CRITICAL for readability):**

1. **Blank line after frontmatter closing `---`**
2. **Heading hierarchy:**
   - `#` for document title
   - `##` for main sections (Section 1, Section 2, etc.)
   - `###` for subsections
3. **Blank lines between sections**
4. **List formatting:**
   - Consistent indentation (2 spaces for nested items)
   - Blank line before/after lists
5. **Tables:**
   - Properly aligned columns
   - Header separator row
6. **Code blocks:**
   - Use triple backticks with language identifier
   - Blank line before/after

**Use Write tool** to create the file with all 13 sections in properly formatted markdown.

### Step 6: Confirm Save Location

```
✅ Agent PRD saved successfully!

**Location:** teams/intelligence/working_docs/prds/gtmbench-agent-prd.md
**ID:** agent-prd-2026-003

Note: When you commit, the pre-commit hook will automatically:
- Add team field (from file path)
- Add owner field (from your git username → person doc)
- Add created and updated dates
- Validate frontmatter structure

Ready to create PR for review? (yes/no)
```

If user says yes, proceed to Phase 4. If no, stop here (they can review/edit the file first).

---

## Phase 4: PR Approval Workflow

When PRD is complete and PM confirms ready:

```
🎉 Excellent! Your Agent PRD is complete.

**Final Pre-flight Check:**
- [ ] All 13 sections complete and verified
- [ ] 30+ test cases with clear pass criteria
- [ ] Prompt assertions have evaluation criteria
- [ ] Competitive analysis completed
- [ ] You stand behind every section

Ready to create PR for review? (yes/no)
```

**If yes:**

1. **Determine reviewers based on team:**

**Auto-detect team from saved PRD file path** (from Phase 3.5)

```bash
# Extract team from file path
# Example: teams/gtm-studio/working_docs/prds/... → gtm-studio
# Example: teams/intelligence/[subteam]-context-engineering/... → intelligence
```

**Base reviewers (always required):**
- Adam Smith (@adam-smith) - Intelligence Platform
- Dominik Facher (@dominik-facher) - CPO

**Conditional reviewers (add based on team):**
- If `team == gtm-workspace`: Add Victor Oliveros (@victor-oliveros) - GTM Workspace DAI
- If `team == gtm-studio`: Add Sneh Kakileti (@sneh-kakileti) - GTM Studio DAI
- Otherwise: Base reviewers only

2. **Prompt for reviewer confirmation:**
```
Who should review this Agent PRD?

Default reviewers for [team]: @adam-smith, @dominik-facher[, @victor-oliveros OR @sneh-kakileti if applicable]

Press Enter to use defaults, or specify GitHub usernames to override/add reviewers:
```

**Parse user input:**
- If Enter pressed or empty: Use the defaults
- If usernames provided: Parse handles (with or without @ prefix)
- Store reviewer list for gh pr create command

3. **Create branch and commit:**

**Note:** File is already saved from Phase 3.5, so we're just committing it.

```bash
# Auto-generate branch name from team/agent-name
# Example: intelligence/gtmbench-agent-prd
# Example: gtm-studio/cold-email-writer-prd
BRANCH="[team]/[agent-name-kebab]-prd"

# Create branch from current master
git checkout -b $BRANCH

# Stage the PRD file
git add [path-to-prd-file.md]

# Commit with descriptive message
git commit -m "feat: add Agent PRD for [Agent Name]

[One-sentence pitch from Section 1]

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push branch to remote
git push -u origin $BRANCH
```

**What happens on commit:**
- Pre-commit hook runs automatically
- Validates frontmatter structure
- Enriches frontmatter with:
  - `team` (from file path: `teams/{team}/...`)
  - `owner` (from git author → person doc lookup)
  - `created` (current date)
  - `updated` (current date)
- Formats markdown consistently

4. **Check for working_docs and prompt for auto-promotion:**

```bash
# Detect if PRD is in working_docs
echo "[path-to-prd-file.md]" | grep -q 'working_docs/.*\.md'
```

**If in working_docs:**
```
This PRD is in working_docs/prds/. If approved, should it automatically move to your team's documentation/prds/ folder?

(yes/no):
```

**If yes:**
- Determine destination: `teams/{team}/documentation/prds/` (flat teams) or `teams/{team}/[subteam]-{subteam}/documentation/prds/` (hierarchical)
- Store promotion metadata for PR body

**If no:** Skip promotion, standard PR only

5. **Create pull request:**

**Detect GitHub CLI:**
```bash
# Try gh command
which gh || where gh

# Common Windows paths if not in PATH:
# - C:\Program Files\GitHub CLI\gh.exe
# - %LOCALAPPDATA%\Programs\GitHub CLI\gh.exe
```

**Build PR body with optional promotion metadata:**

```markdown
## Summary
[One-sentence pitch from Section 1]

## Agent Details
- **Agent Name:** [agent_name from frontmatter]
- **Parent Capability:** [parent_capability from frontmatter]
- **Target Ship:** [target_ship from frontmatter]

## Review Focus
- Job to be done and scope decomposition (Sections 1-2)
- Test case coverage (Section 6)
- Prompt structure and assertions (Section 8)

## Checklist
- [x] All 13 sections complete and verified
- [x] 30+ test cases with clear pass criteria
- [x] Prompt assertions have eval criteria
- [x] Competitive analysis completed
- [x] Ready for engineering review

---

<!-- auto-promote: [true/false] -->
<!-- promote-files: [prd-filename.md] -->
<!-- promote-to: teams/{team}/documentation/prds/ -->

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

**Create PR with reviewers:**
```bash
# If reviewers specified (from step 2):
gh pr create --base master --head $BRANCH \
  --title "Agent PRD: [Agent Name]" \
  --body "[body from above]" \
  --reviewer [reviewer1] --reviewer [reviewer2] ...

# If no reviewers (use CODEOWNERS defaults):
gh pr create --base master --head $BRANCH \
  --title "Agent PRD: [Agent Name]" \
  --body "[body from above]"
```

**Handle authentication errors:**
If `gh pr create` fails with authentication error:
```
⚠️  GitHub CLI authentication failed.

Please run the onboarding skill to authenticate to git.zoominfo.com:
"onboard me"

After onboarding, we can create the PR.
```

**Handle invalid reviewer errors:**
If `gh pr create` fails with "invalid reviewer" error:
```
⚠️  One or more reviewers not recognized by GitHub.

Please check the GitHub usernames and try again. Valid formats:
- @username
- username (without @)

Who should review? (Enter GitHub usernames):
```

Re-prompt and retry with corrected usernames.

6. **Confirm PR creation:**

```
✅ PR created successfully!

**PR URL:** [url]

**Reviewers:** @adam-smith, @dominik-facher[, @victor-oliveros OR @sneh-kakileti if applicable]

[If auto-promotion enabled:]
📦 When this PR is merged, your PRD will automatically move to the documentation/prds/ folder.

**Next steps:**
1. Reviewers will provide feedback
2. Address any comments
3. Once approved and merged, let me know and I'll clean up the branch

Your Agent PRD is now in review! 🎉
```

7. **After user confirms PR is merged:**

```bash
# Switch back to master
git checkout master

# Pull latest changes (includes original PR merge + optional promotion commit from post-merge hook)
git pull origin master

# Delete local feature branch
git branch -D $BRANCH
```

**Confirm cleanup:**
```
✅ You're back on master with the latest changes.

[If auto-promotion was enabled:]
Your PRD has been promoted to the documentation folder!

Feature branch cleaned up. Ready for your next Agent PRD!
```

## Summary

This skill transforms Agent PRD creation from an 8+ hour slog into a 30-60 minute interview session. Use voice-to-text to answer questions quickly—you provide the thinking, AI does the writing.

**Key Efficiency Principles:**
1. Voice-to-text for answering (Win+H / Fn+Fn) - 3-4x faster than typing
2. Context documents first - rich context enables accurate AI drafting
3. Batch questions - answer 3-5 together for comprehensive context
4. Smart expansion (PM gives 2-3 examples → AI expands to 15-20)
5. AI as brilliant ghostwriter - PM provides thinking, AI does writing
6. Critical review checkpoints - prevents rubber-stamping

**Quality Assurance:**
- Every section scored against best practices immediately after drafting
- Quality Improvement iteration (targeted questions) for sections <90
- Systematic evaluation using atomic assertions
- Test cases as contract between product and engineering

**Output:**
- Complete, high-quality Agent PRD
- Ready for stakeholder review
- Ready for engineering implementation
- Systematic evaluation framework in place

