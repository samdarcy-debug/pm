# Agent PRD Skill

**Purpose:** Guide Product Managers through creating world-class Agent PRDs for ZoomInfo's Agentic Platform (ZAP) following best practices.

**Target Efficiency:** 30-60 minutes to complete high-quality Agent PRD (vs. 8+ hours manual)

## Quick Start

To use this skill, simply say:

```
I need to create an Agent PRD
```

or invoke it directly:

```
/agent-prd
```

The skill will guide you through a comprehensive interview covering all 13 sections of the Agent PRD template, automatically draft content based on your answers, assess quality immediately after each section, and iterate using targeted questions until you achieve 90+ quality score across all sections.

## What You'll Need

### Before Starting

1. **Context documents** (the more you provide upfront, the faster the process):
   - Existing PRDs or design docs related to this agent
   - User research or feedback that informed this idea
   - Competitive analysis (testing in Claude, ChatGPT, current co-pilot)
   - Similar agents we've built
   - Technical constraints or platform limitations

2. **Time commitment:** 30-60 minutes (use voice-to-text to speed up answers)

3. **Familiarity with:** [Agent Best Practices](../../../teams/intelligence/documentation/agent-best-practices/) (recommended but not required - the skill will reference these throughout)

## How It Works

### 4-Phase Process

#### Phase 1: Context Gathering
- Provide relevant documents upfront (wiki-links, file paths, or paste directly)
- AI ingests and indexes for reference throughout interview

#### Phase 2: Section-by-Section Interview
- 13 sections, each with:
  - Opening context (why this section matters)
  - Batched questions with best practice callouts (answer 3-5 together - use voice-to-text!)
  - Smart expansion (you give 2-3 examples → AI expands to 15-20)
  - Draft generation (AI writes as your brilliant ghostwriter)
  - **Mandatory confirmation checkpoint** (read every word and confirm before proceeding)
  - **Immediate quality assessment** (scored against best practices while fresh)
  - **Quality Improvement iteration** (if <90, targeted questions for better input)

#### Phase 3: Final Verification
- Quick sanity check that all sections still meet 90+ quality bar
- Verify cross-references are consistent
- Check for no obvious gaps or contradictions

#### Phase 4: PR Approval Workflow
- Pre-flight checklist
- Branch creation and PR setup
- Default reviewers: Sneh Kakileti, Victor Oliveros, Adam Smith, Dominik Facher
- PR description with review focus areas

## Key Efficiency Features

### Speed Optimization: Voice-to-Text

**The Key to 30-60 Minutes:**

This interview has comprehensive questions because context is critical for AI to write accurately. Voice-to-text makes answering fast:

- **Windows:** Win + H
- **Mac:** Fn + Fn (or Enable Dictation in System Preferences)
- **Mobile:** Use built-in voice keyboard

**Why this matters:**
- Speaking is 3-4x faster than typing
- Rich answers = AI writes accurately on first draft = minimal editing
- Think of AI as your brilliant ghostwriter: you provide thinking, AI does writing

**Without voice:** Typing detailed answers takes 2-3 hours
**With voice:** Speaking detailed answers takes 30-60 minutes

### You Provide Direction, AI Does Expansion

1. **Context Reuse:** Upload docs once, AI extracts relevant content automatically
2. **Batch Questions:** Answer 3-5 questions at once via voice-to-text, AI generates complete section
3. **Smart Expansion:** Give 2-3 examples, AI expands to 15-20 using patterns
4. **Brilliant Ghostwriter:** You provide thinking, AI does writing
5. **Critical Review Checkpoints:** Specific validation points prevent rubber-stamping

### Example: Section 2 (Scope & Decomposition)

**Traditional approach:**
- PM manually writes 15-20 in-scope examples
- PM manually writes 15-20 out-of-scope examples
- Time: 2-3 hours

**With this skill:**
- PM provides 2-3 in-scope examples via voice
- PM provides 2-3 out-of-scope examples via voice
- AI expands to 15-20 each using patterns
- PM reviews and tweaks
- Time: 5-10 minutes (with voice-to-text)

## Quality Assurance

### Scoring Rubrics

Every section scored on 100-point scale against [quality criteria](references/quality-criteria.md):

- **100:** Exceptional, exceeds all criteria with rich detail
- **90:** Meets all criteria well, ready for review
- **80:** Meets criteria, room for improvement
- **70:** Some criteria weak or missing
- **<70:** Fundamental gaps

### Quality Improvement Iteration

When a section scores <90, the skill asks 2-3 targeted questions to get better input:

```
⚠️  This section scored 75/100 because: The 15 in-scope examples lack diversity -
they're all variations of the same query type.

To improve this section to 90+, I need:
1. Can you give me 2-3 more examples representing different flavors of queries
   within scope?
2. What edge cases within scope should I include?

[PM provides better seed input] → Section regenerated → Re-assessed → 90+ achieved
```

**Key difference from end-of-document assessment:**
- Quality assessed **immediately after each section** (while context fresh)
- Sections must reach 90+ **before moving to next section**
- Max 3 iterations per section before proceeding

## File Structure

```
.claude/skills/agent-prd/
├── SKILL.md                           # Main skill instructions (✅ Complete)
├── README.md                          # This file
├── references/
│   ├── quality-criteria.md            # Scoring rubrics for all 13 sections (✅ Complete)
│   ├── interview-framework.md         # Question templates (optional)
│   └── examples/
│       └── example-agent-prd.md       # Annotated example (optional)
└── scripts/
    └── quality-check.sh               # Quality assessment script (✅ Complete - invokes from Claude Code)
```

## Best Practices Referenced

This skill integrates guidance from:

- **[Building AI Agents: Challenges & Best Practices](../../../teams/intelligence/documentation/agent-best-practices/building-ai-agents-best-practices.md)**
  - Shaping probability space
  - Task decomposition
  - The vending machine test
  - The intern test
  - Human-in-the-loop patterns

- **[Prompt Writing Guide for Product Managers](../../../teams/intelligence/documentation/agent-best-practices/prompt-writing-guide.md)**
  - Atomic prompt decomposition
  - Evaluation criteria for every instruction
  - Prompt caching optimization
  - The 10x rule

- **[Prompt Assertion Evaluation Framework](../../../teams/intelligence/documentation/agent-best-practices/prompt-assertion-evaluation-framework.md)**
  - LLM-as-judge evaluation
  - Structured assertion scoring
  - CI/CD integration approach

## Success Criteria

A complete Agent PRD includes:

- [ ] All 13 sections complete and scored 90+
- [ ] 30+ test cases (10-15 success, 10-15 rejection, edge cases)
- [ ] Prompt assertions have evaluation criteria
- [ ] Competitive analysis with actual testing results
- [ ] Final checklist from template verified
- [ ] PR created with proper reviewers

## Template Reference

This skill uses [_templates/agent-prd.md](../../../_templates/agent-prd.md) as the foundation. The template defines the 13-section structure:

1. Job to Be Done
2. Scope & Decomposition
3. Opaque Executor Contract
4. Context Requirements
5. Ideal Flow
6. Test Cases
7. Dependencies
8. Prompt Structure
9. Human-in-the-Loop Design
10. Metrics
11. Data Flywheel
12. Competitive Comparative
13. Rollout & Communication

## Tips for Success

### Before Starting

1. **Gather context documents** - The more you provide upfront, the better
2. **Enable voice-to-text** - Win+H (Windows) or Fn+Fn (Mac) for 3-4x faster answers
3. **Block 30-60 minutes** - Focused time produces better results
4. **Have test case ideas ready** - Think of 2-3 examples that must work and 2-3 that should be rejected

### During Interview

1. **Use voice-to-text** - Speaking is 3-4x faster than typing and gives richer context
2. **Answer questions in batches** - Don't rush, take time to think through answers
3. **Provide specific examples** - "Cold outbound to net-new prospects" > "Email writing"
4. **Engage with critical reviews** - Don't rubber-stamp AI output; validate key decisions
5. **Challenge the AI** - If generated content isn't right, say so and explain why
6. **Reference provided docs** - Point AI to specific sections of docs you uploaded

### After Drafting

1. **Trust the quality scores** - If a section scores <90, it needs work
2. **Provide better seed input when asked** - Quality improvement asks targeted questions
3. **Review final output carefully** - Even at 90+, ensure it matches your intent

## FAQ

**Q: Do I need to know the best practices docs by heart?**
A: No. The skill references them automatically throughout the interview.

**Q: What if I don't have all context documents?**
A: That's okay. The interview will guide you through questions. You'll just do a bit more manual work.

**Q: Can I pause and resume?**
A: Yes. The PRD is saved as you go. You can continue anytime.

**Q: What if I disagree with a quality score?**
A: Challenge it. The scoring is guidance, not gospel. Explain why you think a section is good as-is.

**Q: How long does quality improvement iteration take?**
A: Typically 1-2 iterations per section if needed, 2-3 minutes each. Max 3 iterations per section.

**Q: Who reviews the PR?**
A: Default reviewers are Sneh Kakileti, Victor Oliveros, Adam Smith, and Dominik Facher. You can adjust.

## Support

For questions or feedback:
- **Skill issues:** Contact Intelligence team
- **Best practices questions:** Contact Adam Smith
- **Template questions:** Contact Product Operations
- **Platform questions:** Contact platform team

---

**Ready to get started?**

Just say: **"I need to create an Agent PRD"**
