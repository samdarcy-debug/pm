# Weekly Synthesis Report Template

This file contains the complete template structure for generating weekly synthesis reports.

## Main Body Structure

```markdown
# Product Executive Intelligence Brief - [Date]

*Synthesized from [X] team reports: [List team reports (e.g., Product DAI team, GTM Studio team, Data team, etc.)]*

*For detailed questions about any item below, reference specific team reports or contact team leads directly.*

---

## Executive Summary

### Roadmap Priorities

In order to stay aligned and focused on the top priorities, see below for the most important work we've aligned to for this month and next.

[Insert placeholder for roadmap priorities screenshot]

### AI Credit Consumption

Given the importance of driving customer AI Action credit consumption, we will be reporting this each week.

[Insert placeholder for AI Action Credit screenshots]

### Summary of blockers

Summary of blockers across team reports. For more information, use the navigation bar to look into individual team reports in the appendix.

[Insert Table 1: Summary of blockers across team reports]

### Relevant context across reports

This section surfaces relevant information from team reports across the organization relevant to the given domain area.

[Insert Table 2: Relevant Context Across Reports]

### Bottom Line

[Write 1-2 paragraphs in a single paragraph block synthesizing the week's key takeaways. Focus on:
- Strategic progress toward Q2 2025 goals
- Cross-team themes or patterns
- Key risks or opportunities emerging
- Overall health and trajectory]

___________________________________________________________________

[Pull the full executive summaries from each team report and print below based on which strategic category they fall within. Each team should only fall into one of these buckets.]

### GTM Studio

**Team name:** "[Full executive summary from team report (likely will be Sneh Kakileti's GTM Studio team report)]"

**Team name:** "[Full executive summary from team report if any other]"

### GTM Workspace

**Team name:** "[Full executive summary from team report (likely will be Victor Oliveros's GTM Workspace team report)]"

**Team name:** "[Full executive summary from team report if any other]"

### GTM AI Context Service

**Team name:** "[Full executive summary from team report (likely will be Rowan Bailey's Semantic Data, Context Engineering, and MCP team reports)]"

**Team name:** "[Full executive summary from team report if any other]"

### Vertical Datasets

Pull the full paragraph update from Brandon Tucker's Data Team report that reports on the progress that Dow Jones has made on the Vertical Datasets initiative

### Other Data

**Team name:** "[Full executive summary from team report (likely will be Brandon Tucker's Data Team, and Jody Roberts's Core Data team reports)]"

**Team name:** "[Full executive summary from team report if any other]"

### Other Platform

**Team name:** "[Full executive summary from team report (likely will be Ali Sadat's Platform team, Integrations team (Andres Perez's team), Admin team (Brannen Huske's team), Automation team (Marc Frail's team), ZIM team (Anwar Mai's team), and the Data Platform team (Marc Delurgio's team) reports)]"

**Team name:** "[Full executive summary from team report if any other]"

### Other Operations

**Team name:** "[Full executive summary from team report (likely will be AJ Belen's BI team and PMM team, and Brett Jacobs's Product Ops team reports)]"

**Team name:** "[Full executive summary from team report if any other]"

*For deeper analysis on any topic above, reference specific team reports or contact team leads directly.*

*Methodology: Analysis of team 1-2-3 Operating Framework reports, prioritizing: (1) Executive decisions needed, (2) Cross-team blockers, (3) Strategic momentum areas, (4) Strategic alignment gaps*
```

## Table 1: Summary of Blockers

**Format:**
- Use heading level 3: `### Summary of blockers`
- Add descriptive text: "Summary of blockers across team reports. For more information, use the navigation bar to look into individual team reports in the appendix."
- Then create the table

**Table Structure:**
Create a table with 2 columns:
- Column 1: "Challenge/Topic"
- Column 2: "Specific Details"

**Requirements:**
- Read the ZoomInfo Product Offsite Q2 2025 Memo, Outline 2026 Roadmap document, and the Roadmap Next 90 Days CSV (in REFERENCE.md) to understand strategic priorities
- Identify the TOP 5 cross-cutting challenges or themes that appear across multiple team reports
- For each challenge, group related blockers from different teams together
- Format each team's blocker as a separate paragraph starting with bold team name (e.g., **GTM Studio Team:** followed by details)
- Separate paragraphs with `<br><br>` (NOT bullets or line breaks)
- **Do NOT include information from the DAI Executive Team report** (it's a rollup, not an IC report)
- Focus on systemic issues that require executive coordination, not isolated team problems

**Challenges may include:**
- Engineering resource constraints
- Data quality and pipeline issues
- DevOps and infrastructure blockers
- User experience and product gaps
- Compliance and security issues
- Testing and QA infrastructure
- Cross-team coordination challenges
- Concurrency and scalability issues

**Example Format:**
```markdown
| Challenge/Topic | Specific Details |
|-----------------|------------------|
| Data pipeline performance issues | **Intelligence Team:** Entity resolution pipeline experiencing 2-3s latency affecting Studio agent quality<br><br>**GTM Workspace Team:** Context loading delays impacting user experience in Copilot |
```

## Table 2: Relevant Context Across Reports

**Format:**
- Use heading level 3: `### Relevant context across reports`
- Add descriptive text: "This section surfaces relevant information from team reports across the organization relevant to the given domain area"
- Then create the table

**Table Structure:**
Create a table with 2 columns:
- Column 1: "Domain Area & DAI"
- Column 2: "Cross-Team Dependencies & References (from OTHER team reports)"

**Requirements:**
- Create one row for each of these domain areas:
  - GTM Studio (Sneh)
  - GTM Workspace (Victor)
  - GTM AI Context Service (Adam)
  - Data (Brandon)
  - Platform (Ali)
  - Operations (AJ)

- For each domain area, identify what OTHER team reports say that's relevant to that domain
- **Do NOT include the domain's own team report** (e.g., for GTM Studio row, don't include GTM Studio team report)
- **Do NOT include the DAI Executive Team report** (it's a rollup that repeats other work)
- Format each reference as a paragraph starting with bold team name followed by specific details
- Separate paragraphs with `<br><br>`
- Focus on: dependencies, blockers affecting that domain, progress that supports that domain, coordination needs

**Teams to consider:**
- GTM Studio team (owned by Sneh)
- GTM Workspace team (owned by Victor)
- Intelligence team, MCP team, Semantic Data team, Context Engineering team (all under Adam's GTM AI Context Service)
- Data Executive team, Core Data team (under Brandon's Data organization)
- GTM Data Platform team, Integrations team, ZIM team (under Ali's Platform organization)
- Product BI team, Product Ops team (under AJ's Operations)

**Example Format:**
```markdown
| Domain Area & DAI | Cross-Team Dependencies & References (from OTHER team reports) |
|-------------------|----------------------------------------------------------------|
| **GTM Studio (Sneh)** | **Intelligence Team:** Completed entity resolution optimization enabling faster Studio agent responses<br><br>**Platform Team:** Deployed new API endpoints for Studio workbook integrations |
```

## Appendix Structure

```markdown
---

## 📊 Appendix

### Individual Team Reports

## [Team Name] Weekly Report - [Date]
[Full team report content: Start with DAI Executive Team Report]

## [Team Name] Weekly Report - [Date]
[Full team report content: Print GTM Studio team report if included]

## [Team Name] Weekly Report - [Date]
[Full team report content: Print Data Executive Team report if included]

## [Team Name] Weekly Report - [Date]
[Full team report content: Print GTM Workspace Team report if included]

## [Team Name] Weekly Report - [Date]
[Full team report content: Print all other remaining team reports in same format]
```

**Important:** The DAI Executive Team report must come first in the appendix, followed by other key teams, then all remaining teams.

## Formatting Notes

- For main body report sections, use `### GTM Studio` (heading level 3), not `## GTM Studio`
- Each executive summary must be separated by a blank line
- Use direct quotes from team reports
- Bold team names when attributing content: **Team Name:**
- Use `<br><br>` in tables to separate items (not bullets)
- NEVER truncate executive summaries - include them in full
- Do NOT include DAI Executive Team in the analysis tables (Table 1 and Table 2)
- Table 1 uses 2 columns: "Challenge/Topic" and "Specific Details"
- Table 2 uses 2 columns: "Domain Area & DAI" and "Cross-Team Dependencies & References (from OTHER team reports)"
