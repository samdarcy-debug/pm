# Weekly Reports System

A workflow for collecting individual team weekly reports and synthesizing them into cross-team executive intelligence briefs.

## Overview

This system enables:
1. **Teams** to submit weekly status reports in a standardized format
2. **Leadership** to synthesize all team reports into a comprehensive executive brief with strategic analysis

The synthesis process uses Claude Code skills to automatically:
- Analyze reports through a strategic framework lens
- Generate cross-team dependency and blocker tables
- Pull full executive summaries organized by strategic domain
- Create a structured executive intelligence brief

## Folder Structure

```
weekly-reports/
├── team-reports/           # Individual team submissions
│   ├── 2025-01-10/        # Date folders (YYYY-MM-DD format)
│   │   ├── copilot.md
│   │   ├── intelligence.md
│   │   ├── data.md
│   │   └── [team].md      # One file per team
│   └── 2025-01-17/
│       └── ...
└── synthesis/             # Cross-team synthesis reports
    ├── synthesis-2025-01-10.md
    └── synthesis-2025-01-17.md
```

## File Naming Conventions

### Team Reports
- **Location**: `weekly-reports/team-reports/{YYYY-MM-DD}/`
- **Format**: `{team-name}.md` (e.g., `intelligence.md`, `copilot.md`, `data.md`)
- **Example**: `weekly-reports/team-reports/2025-01-10/intelligence.md`

### Synthesis Reports
- **Location**: `weekly-reports/synthesis/`
- **Format**: `synthesis-{YYYY-MM-DD}.md`
- **Example**: `weekly-reports/synthesis/synthesis-2025-01-10.md`

## Workflow

### For Teams: Submitting Weekly Reports

#### Current Process (Manual Collection)
During the transition period, teams continue submitting reports via Google Drive on Fridays. Reports are manually copied into this repository structure.

#### Future Process (Git-based Submission)
Teams will create their weekly reports directly in the repository:

1. **Create a new report** using the weekly report template:
   ```bash
   cp _templates/weekly-report.md weekly-reports/team-reports/2025-01-10/intelligence.md
   ```

2. **Fill out the report** following the template structure:
   - Executive summary
   - Key accomplishments
   - Blockers and dependencies
   - Next week's priorities

3. **Commit and push** by Friday EOD:
   ```bash
   git add weekly-reports/team-reports/2025-01-10/intelligence.md
   git commit -m "Add intelligence team weekly report for 2025-01-10"
   git push
   ```

### For Leadership: Creating Synthesis Reports

Once all team reports for a week are available:

1. **Verify all reports are present** in the date folder:
   ```bash
   ls weekly-reports/team-reports/2025-01-10/
   ```

2. **Run the synthesis skill** using Claude Code:
   - The skill will prompt for the week date
   - It will read all team reports from that date's folder
   - It will generate the synthesis report in two stages:
     - First: Main body (executive summary + strategic sections)
     - After approval: Appendix with full team reports

3. **Review and edit** the generated synthesis:
   - Add screenshots for Roadmap Priorities and AI Credit Consumption sections
   - Review analysis tables for accuracy
   - Adjust bottom line summary if needed

4. **Commit the synthesis** to the repository:
   ```bash
   git add weekly-reports/synthesis/synthesis-2025-01-10.md
   git commit -m "Add weekly synthesis report for 2025-01-10"
   git push
   ```

## Synthesis Report Structure

The synthesis report includes:

### 1. Executive Summary
- **Roadmap Priorities**: Screenshot placeholder (manually inserted)
- **AI Credit Consumption**: Screenshot placeholder (manually inserted)
- **Summary of Blockers**: Table of cross-cutting challenges across teams
- **Relevant Context Across Reports**: Table organized by strategic domain areas
- **Bottom Line**: Paragraph synthesizing key takeaways

### 2. Strategic Category Sections
Reports organized by strategic framework:
- **GTM Studio**: Purpose-built apps and agent workflows
- **GTM Workspace**: Copilot interface and experiences
- **GTM AI Context Service**: Data platform and intelligence layer
- **Vertical Datasets**: Industry-specific data products
- **Other Data**: Additional data initiatives
- **Other Platform**: Platform capabilities
- **Other Operations**: Operational updates

Each section pulls full executive summaries from relevant team reports.

### 3. Appendix
Complete individual team reports for reference.

## Strategic Framework

The synthesis skill applies this framework to analyze and organize information:

- **GTM Studio**: Agent creation platform, workflow orchestration
- **GTM Workspace**: User-facing Copilot interface
- **GTM AI Context Service**: Intelligence platform, entity resolution, context APIs
- **Vertical Datasets**: Healthcare, financial services, technology sector data
- **Other Data**: General data platform, records management
- **Other Platform**: Authentication, APIs, infrastructure
- **Other Operations**: Team operations, processes, tooling

## Screenshot Handling

The synthesis report includes placeholder sections for screenshots:
- **Roadmap Priorities**: Manually insert screenshot after generation
- **AI Credit Consumption**: Manually insert screenshots after generation

These are intentionally left as placeholders for manual insertion since Claude Code generates the text content only.

## Using the Weekly Synthesis Skill

The synthesis skill is invoked through Claude Code:

```
Use the weekly-synthesis skill
```

The skill will:
1. Ask for the week date (YYYY-MM-DD format)
2. Locate all team reports in `weekly-reports/team-reports/{date}/`
3. Read and analyze each team report
4. Apply the strategic framework
5. Generate two analysis tables (Blockers, Relevant Context)
6. Create strategic category sections with full executive summaries
7. Generate main body for review
8. After approval, generate appendix with full team reports

## Formatting Requirements

The synthesis skill follows these formatting standards:

- **Table separators**: Use `<br><br>` (not bullets) for multiple items in table cells
- **Team names**: Bold format in tables: `**Team Name:**`
- **Executive summaries**: Pull full summaries without truncation
- **Section headers**: Bold section headers (no special markdown headings in main body)
- **Workflow**: Main body first, then appendix after approval

## Future Enhancements

Planned improvements to this system:

- **Individual Team Report Skills**: Skills to help teams create their weekly reports
  - System prompt and user prompt for guided report creation
  - Team-specific context and templates
  - Separate from synthesis skill (teams create inputs, synthesis processes outputs)

- **Automated Collection**: GitHub Actions to trigger synthesis on schedule

- **Validation**: Scripts to check team report format and required fields

- **Analytics**: Historical trend analysis and reporting metrics

- **Integration**: Automated import from Google Drive during transition period

## Gradual Transition Plan

The system supports a phased rollout:

1. **Phase 1 (Current)**: Manual collection
   - Teams continue using Google Drive
   - Reports manually copied to repository
   - Synthesis skill used to generate briefs

2. **Phase 2**: Hybrid approach
   - Some teams submit directly to repository
   - Others continue with Google Drive
   - Both workflows supported simultaneously

3. **Phase 3**: Full git-based workflow
   - All teams submit reports via git
   - Automated validation and checks
   - Scheduled synthesis generation

## Questions or Issues?

- **System questions**: Ask in #product-ops
- **Bugs or feature requests**: File an issue in this repository
- **Help with reports**: Contact your team lead or document owner
