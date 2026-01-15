# Gap Analysis: Team Weekly Report Skill vs Original System Prompt

## Overview

This document compares the current `skill.md` implementation with the original "System Prompt and Instructions for Weekly Report Generation" document to identify what needs to be updated.

---

## Critical Gaps Requiring Updates

### 1. **Exact Template Format Missing**

**Original System Prompt** (Step 3) contains the exact template with inline instructions:
```markdown
# [Team Name] Executive Roundup - [Date]

## Executive Summary

[Start with the bottom line - the single most important thing executives need to know. Could be a major win, a critical blocker needing attention, a strategic pivot, or a key decision needed. Then provide essential context in 2-3 more sentences max. Make it punchy and action-oriented. Use specific names and owners of workstreams where possible. Avoid hyperbolic AI language. Avoid words like "crisis" or "critical" unless explicitly stated in the transcripts. Do not use goal % completed as a metric]
```

**Current skill.md** has generalized guidance:
```markdown
## **Executive Summary**

[2-3 paragraphs synthesizing the week's most important developments, decisions, and implications. Focus on what leadership needs to know.]
```

**Gap**: The original template has much more specific inline instructions for EACH section with explicit dos and don'ts. The current skill.md is too abstract.

**Fix Needed**: Copy the exact template from the original system prompt into skill.md, preserving all inline instructions.

---

### 2. **Repetition Warnings Missing**

**Original includes** (multiple times):
> "Make sure you don't repeat topics. Repetition makes your output weak."

**Current skill.md**: Does not explicitly warn against repetition.

**Gap**: This is a critical quality instruction that prevents weak output.

**Fix Needed**: Add explicit "avoid repetition" warnings throughout the template sections.

---

### 3. **Section-Specific Instruction Detail**

#### Executive Summary
**Original**:
- "Start with the bottom line - the single most important thing executives need to know"
- "Could be a major win, a critical blocker needing attention, a strategic pivot, or a key decision needed"
- "Then provide essential context in 2-3 more sentences max"
- "Make it punchy and action-oriented"

**Current**: Generic "2-3 paragraphs synthesizing..."

#### Key Momentum Areas
**Original**:
- Exactly 3 achievement narratives specified
- Each 2-3 sentences
- "building on themes if possible, showing how different work streams are creating compound effects"
- "Mention team members by name when highlighting exceptional contributions"
- "potentially highlighting cross-functional wins or unexpected breakthroughs that changed our trajectory"

**Current**: Generic "3-5 momentum areas"

**Gap**: Original is much more prescriptive about structure and content.

---

### 4. **Goals & Progress Structure**

**Original** shows exactly 3 initiative categories with specific guidance:
- **[Initiative Category 1]**: "Current status narrative describing what moved forward, current state, and any notable milestones. Include percentage complete or other metrics naturally within the text."
- **[Initiative Category 2]**: "Progress narrative that might acknowledge both advances and delays, maintaining transparency while focusing on forward momentum."
- **[Initiative Category 3]**: "Status update that could include technical achievements explained in business terms..."

**Current**: "Organized by major workstreams or initiatives. Use bold headers for each initiative, then narrative paragraphs..."

**Gap**: Original provides specific examples of how to write each type of progress narrative.

---

### 5. **Strategic Challenges Detail**

**Original** explicitly states:
- "Do not exaggerate the severity of the challenge especially if there is a clear path forward"
- Each challenge should be "presented as a narrative: what the problem is, how it's impacting the work, and what we've discovered through root cause analysis"
- "Second challenge woven into a story about attempted solutions and remaining obstacles"
- "Third challenge if needed, potentially connecting to resource constraints or external dependencies. Frame as opportunity for strategic discussion rather than just a complaint"

**Current**: Generic "Frame constructively - what's the challenge and what's the path forward?"

**Gap**: Original is much more specific about tone calibration and avoiding exaggeration.

---

### 6. **Cross-Team Dependencies**

**Original** shows exact structure:
```markdown
Our work with [Team Name] on [initiative] continues to be critical for [business reason]. [Describe current status, any friction points, and specific needs in a diplomatic but clear way...]

[Additional dependency narrative if needed, focusing on collaboration opportunities or explaining why certain coordination is essential. Maintain objectivity while advocating for necessary support...]
```

**Current**: Generic guidance about dependencies.

**Gap**: Original provides the exact opening sentence structure.

---

### 7. **Looking Ahead Structure**

**Original** specifies:
- "Opening statement about overall direction and main focus for next week, connecting to strategic objectives"
- "Detailed narrative about top 2-3 priorities, explaining not just what will be done but why it matters now, what success looks like, and what could accelerate or impede progress. Weave in dependencies and risks naturally"
- "Closing forward-looking statement that maintains momentum while being realistic about challenges. End on a confident note about the team's ability to deliver value"

**Current**: Generic "2-3 paragraphs on what's coming next week..."

**Gap**: Original is much more structured about opening, middle, closing narrative flow.

---

### 8. **Explicit "Do Not Use % Complete" Instruction**

**Original** repeats throughout:
> "Do not use goal % completed as a metric"

AND at the end adds:
> "(Additional instructions: Do not use the word 'critical'. Use full names when possible throughout. Do not use goal % completed as a metric)."

**Current skill.md**: States "No goal completion percentages" once in "What to Avoid" section.

**Gap**: This instruction is SO important it appears 10+ times in the original. Should be reinforced much more heavily.

---

### 9. **"Dominic" vs "Dominik" Spelling**

**Original** states:
> "Please note that throughout, any references to 'Dominic' should be referred to as 'Dominik'"

**Current**: Has "Spell 'Dominik' with a 'k' (not 'Dominic')" in Specific Writing Rules.

**Status**: ✅ This one is already captured correctly.

---

### 10. **Source Attribution Line**

**Original** ends with:
```markdown
---
*Source: Team 1-2-3 Operating Framework entries from [date range]*
```

**Current**: Has same guidance.

**Status**: ✅ Already captured.

---

## What's Currently BETTER in skill.md

### 1. Team Name Validation Table
The current skill.md has a comprehensive table mapping user inputs to canonical team identifiers. The original document doesn't have this.

**Keep**: This is valuable and should stay.

---

### 2. YAML Frontmatter Specification
Current skill.md has detailed YAML frontmatter with examples. Original document doesn't specify this.

**Keep**: Essential for file system integration.

---

### 3. Quality Checklist
Current skill.md has a comprehensive checklist at the end. Original doesn't have this.

**Keep**: Very helpful for validation.

---

### 4. Synthesis Process Section
Current skill.md has guidance on "From Meeting Transcripts" and "From Tracker Data". Original doesn't break this down.

**Keep**: Helpful operational guidance.

---

## Recommended Changes to skill.md

### Priority 1: Copy Exact Template with Inline Instructions

Replace the generic template section in skill.md (lines 110-146) with the EXACT template from the original system prompt (lines 41-204 in REFERENCE-ORIGINAL.md), including:
- All inline bracketed instructions
- All specific guidance for each section
- All warnings about avoiding hyperbolic language, repetition, "critical" word usage, etc.

### Priority 2: Strengthen "Do Not Use % Complete" Warnings

Add this warning to multiple sections:
- In Executive Summary instructions
- In Goals & Progress instructions
- In Quality Checklist
- In What to Avoid section

Make it appear at least 3-4 times so it's impossible to miss.

### Priority 3: Add "Avoid Repetition" Warnings

Add explicit warnings in:
- Goals & Progress section: "Make sure you don't repeat topics. Repetition makes your output weak."
- Key Momentum Areas
- Strategic Challenges

### Priority 4: Update Section Instructions

For each major section, replace generic guidance with the specific narrative structure from the original:
- Executive Summary: "Start with the bottom line..."
- Key Momentum Areas: Three specific narratives with different focuses
- Goals & Progress: Three initiative categories with specific writing styles
- Strategic Challenges: Three challenge types with specific framing
- Looking Ahead: Opening, detailed middle, confident closing

### Priority 5: Add Challenge Severity Calibration

Add to Strategic Challenges section:
> "CRITICAL: Do not exaggerate the severity of the challenge especially if there is a clear path forward."

---

## Summary

**Main Issue**: The current skill.md provides good structural guidance but lacks the ultra-specific inline instructions that make the original system prompt effective. The original tells you EXACTLY what to write in each section with specific examples and repeated warnings.

**Solution**: Merge the two approaches:
1. Keep the excellent structural elements of skill.md (YAML frontmatter, team validation, quality checklist)
2. Replace the generic template with the exact template from the original system prompt
3. Preserve all inline instructions, warnings, and specific guidance from the original
4. Reinforce critical instructions (no %, avoid repetition, no "critical" word) multiple times

**Expected Outcome**: A skill.md that combines:
- The operational excellence of the current version (YAML, file paths, team mapping)
- The ultra-specific prompt instructions of the original (exact templates, inline guidance, repeated warnings)

This will ensure Claude generates reports that match the exact format and quality standards defined in the original system prompt.