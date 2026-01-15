# Weekly Synthesis

**Description**: Synthesizes individual team weekly reports into a comprehensive cross-team executive intelligence brief for ZoomInfo CPO and VP Product Management staff.

**Trigger**: Use this skill when the user wants to create a weekly synthesis report combining all team reports for a specific week.

---

## Overview

You are creating a weekly executive intelligence brief for the ZoomInfo CPO and VP Product Management staff. Your role is to synthesize individual team reports into actionable insights for product leadership decision-making and coordination.

## Strategic Context

Read the ZoomInfo Product Offsite Q2 2025 Memo, Outline 2026 Roadmap document, and the Roadmap Next 90 Days CSV thoroughly to understand the strategic priorities and operational goals (available in [REFERENCE.md](REFERENCE.md)).

The Q2 2025 Memo outlines ZoomInfo's strategic transformation from a SaaS to an AI-company operating model. Use the memo as your strategic filter - prioritize synthesis around progress toward the strategic transformation and the foundational elements that enable it.

## Workflow

### Step 1: Collect Inputs

1. **Ask the user for the week ending date** (format: YYYY-MM-DD, should be a Friday)
2. **Discover all team reports for this week**:
   - Use glob pattern: `teams/**/weekly-reports/*-weekly-report-{YYYY-MM-DD}.md`
   - This will find reports at any depth (flat teams and sub-teams)
   - Excludes product-executive-report files (synthesis output, not input)
3. **Read all discovered report files**
4. **Load reference context** from [REFERENCE.md](REFERENCE.md) (Q2 2025 Memo)

### Step 2: Analyze Reports

For each team report, extract:
- **Executive summary**: The team's high-level summary
- **Key accomplishments**: What shipped or was completed
- **Blockers**: What's blocking progress
- **Dependencies**: Cross-team dependencies
- **Strategic alignment**: Which strategic framework areas this work impacts

### Step 3: Generate Analysis Tables

Read [TEMPLATE.md](TEMPLATE.md) for the exact specifications for:
- **Table 1**: Summary of blockers across team reports (TOP 5 cross-cutting challenges)
- **Table 2**: Relevant context across reports (cross-team dependencies by domain area)

Follow the detailed table generation requirements in TEMPLATE.md, including:
- Column structure and naming
- Formatting with `<br><br>` separators
- Which teams to include/exclude
- How to group and present information

### Step 4: Organize by Strategic Categories

Read [CONSTRAINTS.md](CONSTRAINTS.md) for:
- Strategic framework definitions (GTM Studio, GTM Workspace, GTM AI Context Service, etc.)
- Team ownership mapping to strategic categories
- Analysis approach and quality standards

Pull FULL executive summaries from team reports and organize them by strategic category following the team ownership mapping in CONSTRAINTS.md.

### Step 5: Generate and Save Main Body

Generate the main body using the complete report structure from [TEMPLATE.md](TEMPLATE.md):
- Executive Summary with roadmap priorities, AI credit consumption, analysis tables, and bottom line
- Strategic category sections with full executive summaries
- Proper formatting and attribution

Apply all quality standards from [CONSTRAINTS.md](CONSTRAINTS.md).

**Write the main body directly to file:**
```
teams/leadership/documentation/weekly-product-executive-reports/product-executive-report-{YYYY-MM-DD}.md
```

Do NOT output the main body to chat. Write it directly to the file.

### Step 6: Request User Review

Ask the user to review the file you just created at:
```
teams/leadership/documentation/weekly-product-executive-reports/product-executive-report-{YYYY-MM-DD}.md
```

Ask if they approve the main body before generating the appendix. Provide the file path so they can open and review it.

**Do NOT generate the appendix yet. Wait for user approval of the main body.**

### Step 7: Generate and Append Appendix

After user approval, create the appendix with all full team reports following the appendix structure in TEMPLATE.md.

**Important: Use sequential reading to prevent context exhaustion**

Read team reports ONE AT A TIME and append each to the file before reading the next. This prevents context exhaustion even if earlier steps caused compaction.

**Appendix generation order:**
1. Read DAI Executive Team report
2. Append to file
3. Read next team report (prioritize: GTM Studio, GTM Workspace, Data Executive Team, Intelligence Team, then remaining teams)
4. Append to file
5. Repeat for all remaining team reports

**Append the appendix to the existing file** at:
```
teams/leadership/documentation/weekly-product-executive-reports/product-executive-report-{YYYY-MM-DD}.md
```

### Step 8: Confirm Completion

Confirm the final synthesis report is saved at:
```
teams/leadership/documentation/weekly-product-executive-reports/product-executive-report-{YYYY-MM-DD}.md
```

## Key Files

- **TEMPLATE.md**: Complete synthesis report structure, table specifications, appendix format
- **CONSTRAINTS.md**: Strategic framework definitions, team ownership mapping, analysis rules, quality standards
- **REFERENCE.md**: Q2 2025 Memo and strategic context (already exists)

## Notes

- This skill synthesizes **multiple team reports** into executive intelligence briefs
- The separate `team-weekly-report` skill generates individual team reports
- Pull FULL executive summaries without truncation
- Do NOT include DAI Executive Team in analysis tables (it's a rollup, not an IC report)
- Focus on strategic relevance rather than urgency of language
