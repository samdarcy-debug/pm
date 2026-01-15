# Team Weekly Report Generator

Generate Executive Roundup-style weekly team reports from meeting transcripts and tracker data.

## Overview

This skill helps teams create narrative-driven weekly reports that focus on business impact, strategic insights, and cross-team dependencies. It synthesizes inputs from Monday planning meetings (optional), Friday reflection meetings (required), and weekly tracker data into a cohesive Executive Roundup format.

## How to Use This Skill

When invoked, the skill will:
1. Ask for team name and week ending date
2. Request meeting transcripts (Monday optional, Friday required)
3. Request weekly tracker data (Excel/spreadsheet)
4. Generate a structured weekly report following the Executive Roundup format
5. Validate team names against the canonical list in CONSTRAINTS.md

## Workflow

### Step 1: Gather Basic Information

Ask the user:
```
Please provide:
1. Team name
2. Week ending date (Friday, format: YYYY-MM-DD)
```

Validate team name using the team mapping table in [CONSTRAINTS.md](CONSTRAINTS.md).

### Step 2: Request Meeting Transcripts

Ask the user:
```
Please provide:
1. Monday planning meeting transcript (optional)
2. Friday reflection meeting transcript (required - should cover progress, blockers, learnings)
```

### Step 3: Request Tracker Data

Ask the user:
```
Please provide your weekly tracker data (Excel/spreadsheet) with:
- Goals/initiatives
- Owners
- Progress updates
- Status
```

### Step 4: Generate Report

1. Read [TEMPLATE.md](TEMPLATE.md) for the complete report structure (YAML frontmatter + report body template)
2. Read [CONSTRAINTS.md](CONSTRAINTS.md) for all writing guidelines, quality requirements, and synthesis instructions
3. Synthesize the inputs following the synthesis process in CONSTRAINTS.md:
   - Extract key themes, decisions, blockers, insights from transcripts
   - Identify progress patterns, owner context, status changes from tracker
   - Weave both sources into narrative paragraphs with business impact framing
4. Apply all constraints from CONSTRAINTS.md while populating the template structure from TEMPLATE.md
5. Validate output against the quality checklist in CONSTRAINTS.md

### Step 5: Save Output

Save the generated report to:
```
weekly-reports/team-reports/{YYYY-MM-DD}/{file-identifier}-weekly-report-{YYYY-MM-DD}.md
```

Example: For GTM Workspace week ending 2025-01-17:
```
weekly-reports/team-reports/2025-01-17/gtm-workspace-weekly-report-2025-01-17.md
```

## Key Files

- **TEMPLATE.md**: Complete report structure (YAML frontmatter + body template)
- **CONSTRAINTS.md**: Writing guidelines, team mapping, quality checklist, synthesis process

## Notes

- This skill generates **individual team reports** (inputs to synthesis)
- The separate `weekly-synthesis` skill combines multiple team reports into cross-team executive summaries
- Teams should review and edit the generated draft before submission
- The "draft" status in frontmatter indicates report needs team review before being marked "approved"
