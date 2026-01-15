# Team Weekly Report Template

This file contains the complete template structure for generating team weekly reports.

## YAML Frontmatter

```yaml
---
id: weekly-{file-identifier}-{YYYY}-{WW}
title: "{Display Name} Weekly Report - {Month DD, YYYY}"
type: weekly-report
status: draft
team: {file-identifier}
owner:
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
week_ending: {YYYY-MM-DD}
reporting_period: "{Month DD-DD, YYYY}"
tags: ["weekly-report", "Q{Q}{YYYY}", "{team-tag}"]
---
```

**Example for GTM Workspace**:
```yaml
---
id: weekly-gtm-workspace-2025-03
title: "GTM Workspace Weekly Report - January 17, 2025"
type: weekly-report
status: draft
team: gtm-workspace
owner:
created: 2025-01-17
updated: 2025-01-17
week_ending: 2025-01-17
reporting_period: "January 13-17, 2025"
tags: ["weekly-report", "Q12025", "gtm-workspace"]
---
```

## Report Body Template

```markdown
# [Team Name] Executive Roundup - [Date]

## Executive Summary

[Start with the bottom line - the single most important thing executives need to know. Could be a major win, a blocker needing attention, a strategic pivot, or a key decision needed. Then provide essential context in 2-3 more sentences max. Make it punchy and action-oriented.]

## This Week's Progress

### Key Momentum Areas

[First achievement narrative - what was accomplished and why it matters, connecting to business impact. Include specific metrics or outcomes where relevant. 2-3 sentences.]

[Second achievement narrative - building on themes if possible, showing how different work streams are creating compound effects. Mention team members by name when highlighting exceptional contributions.]

[Third achievement narrative - potentially highlighting cross-functional wins or unexpected breakthroughs that changed our trajectory.]

### Goals & Progress

**[Initiative Category 1]**: [Current status narrative describing what moved forward, current state, and any notable milestones. 2-3 sentences showing progression and current position.]

**[Initiative Category 2]**: [Progress narrative that might acknowledge both advances and delays, maintaining transparency while focusing on forward momentum. Connect to broader objectives and explain why this matters.]

**[Initiative Category 3]**: [Status update that could include technical achievements explained in business terms, making complex work accessible to executive audience.]

### Strategic Challenges

[First challenge presented as a narrative: what the problem is, how it's impacting the work, and what we've discovered through root cause analysis. Include specific examples and explain what support or decisions are needed.]

[Second challenge woven into a story about attempted solutions and remaining obstacles. Explain cross-functional impacts and why executive awareness or intervention might be necessary. Be candid but constructive.]

[Third challenge if needed, potentially connecting to resource constraints or external dependencies. Frame as opportunity for strategic discussion rather than just a complaint.]

## Strategic Insights

### Key Learnings & Discoveries

[First insight narrative explaining what was discovered, how it challenges previous assumptions, and what it means for our strategy going forward. Connect to specific examples from the week's work.]

[Second learning presented as a story of discovery - what prompted the investigation, what was found, and how it should influence future decisions. Include validation method if relevant.]

[Additional insights woven together, potentially showing patterns across team members' observations. Explain implications rather than just stating facts.]

### Cross-Team Dependencies

Our work with [Team Name] on [initiative] continues to be important for [business reason]. [Describe current status, any friction points, and specific needs in a diplomatic but clear way.]

[Additional dependency narrative if needed, focusing on collaboration opportunities or explaining why certain coordination is essential. Maintain objectivity while advocating for necessary support.]

## Looking Ahead

[Opening statement about overall direction and main focus for next week, connecting to strategic objectives.]

[Detailed narrative about top 2-3 priorities, explaining not just what will be done but why it matters now, what success looks like, and what could accelerate or impede progress. Weave in dependencies and risks naturally.]

[Closing forward-looking statement that maintains momentum while being realistic about challenges. End on a confident note about the team's ability to deliver value.]

---

*Source: Team 1-2-3 Operating Framework entries from [date range]*
```

## Template Usage Notes

- All bracketed placeholders `[...]` should be replaced with actual content
- Follow all writing guidelines and constraints from CONSTRAINTS.md
- Use specific names throughout (not "the team")
- Write in narrative paragraphs, not bullets
- Integrate metrics naturally into text flow
