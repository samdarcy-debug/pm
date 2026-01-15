# Team Weekly Report Writing Constraints

This file contains all writing guidelines, quality requirements, and synthesis instructions for generating team weekly reports.

## CRITICAL CONSTRAINTS (Read This Multiple Times)

**⚠️ DO NOT USE GOAL % COMPLETED AS A METRIC**

Never write things like "85% complete" or "Task is 90% done". Instead, integrate metrics naturally into narrative text describing actual progress and current state.

**⚠️ AVOID REPETITION - Repetition makes your output weak**

Make sure you don't repeat topics across different sections. Each point should appear once with full context rather than being mentioned multiple times in different sections.

**⚠️ DO NOT EXAGGERATE SEVERITY**

Do not exaggerate the severity of challenges, especially if there is a clear path forward. Avoid words like "crisis" unless explicitly stated in the source transcripts.

## Team Name Validation

Match user input to canonical team identifiers. If uncertain, confirm with the user.

| User Says | File Identifier | Display Name | Tags |
|-----------|----------------|--------------|------|
| GTM Workspace, Workspace, Copilot, SalesOS | gtm-workspace | GTM Workspace | gtm-workspace |
| GTM Studio, Studio | gtm-studio | GTM Studio | gtm-studio |
| Intelligence | intelligence | Intelligence | intelligence |
| Integrations | integrations | Integrations | integrations |
| Data | data | Data | data |
| Core Data | core-data | Core Data | core-data |
| Data Platform | data-platform | Data Platform | data-platform |
| Semantic Data | semantic-data | Semantic Data | semantic-data |
| Context Engineering | context-engineering | Context Engineering | context-engineering |
| DAI | dai | DAI | dai |
| Product Ops, ProductOps | product-ops | Product Ops | product-ops |
| Product Marketing | product-marketing | Product Marketing | product-marketing |
| Product BI | product-bi | Product BI | product-bi |
| MCP | mcp | MCP | mcp |
| Admin | admin | Admin | admin |
| Automation | automation | Automation | automation |
| ZIM | zim | ZIM | zim |

**IMPORTANT**: "Copilot" is retired. Always use "GTM Workspace" as the proper term.

## Voice and Tone

- **Narrative-driven**: Write in flowing paragraphs, not bullets
- **Specific**: Use actual names of people and projects
- **Business-focused**: Emphasize impact and outcomes, not just activities
- **Constructive**: Frame challenges as problems to solve, not complaints
- **Confident but not hyperbolic**: Avoid words like "absolutely essential"
- **Direct**: Use active voice and clear attribution ("Gabe led..." not "Work was done...")

## What to Include

- **Context**: Why does this work matter? What's the business impact?
- **Attribution**: Who drove what? Name specific contributors
- **Progress**: What changed from last week? What unblocked?
- **Dependencies**: How does this connect to other teams' work?
- **Learnings**: What did the team discover or realize?
- **Decisions**: What choices were made and why?
- **Trade-offs**: What was deprioritized to focus on what?

## What to Avoid

- ❌ Bullet-point status updates
- ❌ Mechanical task lists ("completed X, started Y")
- ❌ Goal completion percentages ("85% done")
- ❌ Repetition across sections
- ❌ Exaggerating severity of challenges
- ❌ Overly technical jargon without business context
- ❌ Hyperbolic language ("game-changing," "revolutionary")
- ❌ Vague generalities ("made progress," "continued work")
- ❌ Passive voice ("it was decided," "work was done")
- ❌ Crisis language for normal challenges

## Specific Writing Rules

- Spell "Dominik" with a "k" (not "Dominic")
- Use "GTM Workspace" not "Copilot"
- Use em dashes for parenthetical thoughts (no spaces: "text—like this—text")
- Quote actual customer or team member language when relevant
- Integrate metrics into narrative flow, don't call them out separately
- Frame constraints as context, not excuses

## Synthesis Process

### From Meeting Transcripts

1. **Extract Key Themes**: What were the major discussion topics?
2. **Identify Decisions**: What did the team decide? Who advocated for what?
3. **Surface Blockers**: What challenges came up? Who's working to resolve them?
4. **Capture Insights**: What learnings or discoveries emerged?
5. **Note Attribution**: Who said what? Who's driving which initiatives?

### From Tracker Data

1. **Progress Patterns**: Which initiatives moved significantly? Which stalled?
2. **Owner Context**: Who's responsible for what? Are owners clear?
3. **Status Changes**: What shifted from last week? What accelerated or slowed?
4. **Interdependencies**: Which goals depend on other teams or deliverables?

### Combining Sources

- Use transcripts for **context, decisions, and insights**
- Use tracker for **structure and progress validation**
- Weave both into **narrative paragraphs** with business impact framing
- Don't simply list tracker items - tell the story behind the data

## Quality Checklist

Before outputting the report, verify:

- [ ] YAML frontmatter complete with correct team identifier
- [ ] Team name matches canonical list (GTM Workspace not Copilot)
- [ ] Tags array includes team tag matching file identifier
- [ ] Executive Summary provides leadership-ready synthesis
- [ ] Specific names used throughout (not "the team")
- [ ] Business impact clear for each major item
- [ ] NO GOAL COMPLETION PERCENTAGES ANYWHERE - metrics integrated into narrative naturally
- [ ] NO REPETITION across sections - each point appears once with full context
- [ ] Challenges framed constructively without exaggerating severity
- [ ] Cross-team dependencies identified and described
- [ ] No bullet points in main body (narrative paragraphs only)
- [ ] No hyperbolic language
- [ ] Strategic Insights section includes real learnings
- [ ] Looking Ahead connects to broader context
- [ ] Source attribution at end
- [ ] "Dominik" spelled with "k" throughout
