# PM Knowledge Repository - Context for Claude

This is a Git-based knowledge management system for Product Management. All product documentation lives here as structured Markdown files with YAML frontmatter, designed to be both human-readable and machine-processable.

## Repository Structure

```
/
├── _templates/              # Document templates (PRD, RFC, one-pager, six-pager, etc.)
├── _utilities/              # Machine-generated indexes (do not edit manually)
├── learnings-memos/         # Quarterly learning memos (cross-team resource)
│   ├── Q3-2025/             # Organized by quarter
│   │   ├── Data/            # Team-specific learnings
│   │   ├── GTM-Studio/
│   │   └── ...
│   ├── FOUNDATIONAL-LEARNINGS.md
│   └── Q3-2025-LEARNINGS-ANALYSIS-SUMMARY.md
└── teams/                   # Team-specific content (see TEAM-MAPPING.md for details)
    ├── {dai-name}/          # DAI-level teams
    │   ├── _people/         # Team member person docs (REQUIRED)
    │   ├── weekly-reports/  # Team status reports (REQUIRED for flat teams)
    │   ├── [subteam]-*/     # Sub-teams (hierarchical structure)
    │   │   └── weekly-reports/  # Sub-team status reports (REQUIRED)
    │   └── [custom]/        # Team-controlled organization (optional)
    └── leadership/          # Cross-team leadership documents
```

**Team Organization**: Teams are organized at the DAI (Directly Accountable Individual) level. Some DAIs have flat team structures (single team), while others have hierarchical structures with multiple sub-teams denoted by the `[subteam]-` prefix. Each team controls their own internal folder organization beyond the two required folders: `_people/` and `weekly-reports/`.

For detailed team organizational structure and conventions, see [TEAM-MAPPING.md](TEAM-MAPPING.md).

### Philosophy: PR-Based Working Documents

**Everything in the main branch is the current source of truth.** There is no distinction between "working documents" and "approved documentation" - all content in main represents our best current understanding, regardless of completeness or polish level.

**The "working document" phase exists entirely within pull requests:**
- Your local environment is your scratch space for experimentation
- Create a PR when you need feedback or want to propose changes
- The PR branch becomes the collaborative working space where iteration happens
- Once approved and merged, the content becomes part of the official repository

**Key implications:**
- All content in main is searchable, citable, and considered current
- Teams control their own folder organization (only `_people/` and `weekly-reports/` are required)
- Updates and changes follow the standard PR workflow
- No automated file movement between folders

**Folder Targeting for New Files:**
When creating new documents, always prompt the user for the destination folder:
- **Default suggestion**: User's team subfolder based on their person profile
- **Custom subfolder**: Allow teams to specify their own organization within their space
- **Global/shared locations**: Explicitly warn if creating in shared areas (e.g., `_templates/`, root-level folders) as these require broader review

This ensures clear ownership, appropriate review paths, and intentional placement from the start.

## Learning Memos System

### Overview
The `learnings-memos/` folder contains quarterly learning memos from all product teams. These are retrospective documents capturing key learnings, hypotheses tested, and go-forward plans from each quarter. Unlike weekly reports (focused on status and progress), learning memos provide deep reflections on what worked, what didn't, and strategic insights for future work.

### Structure
- **Quarterly folders**: Organized by quarter (e.g., `Q3-2025/`)
- **Team subfolders**: Each quarter contains subfolders by team
- **Individual memos**: One memo per PM, documenting their learnings
- **Summary docs**: Cross-team analysis and foundational learnings extraction

### File Organization
Learning memos are kept in a **unified root folder** (`learnings-memos/`) rather than distributed across team folders. This enables:
- Easy browsing of all learnings in one place
- Cross-team pattern recognition
- Quarterly synthesis and comparison

**Team association** is maintained through the `team` field in frontmatter, which connects each memo to its DAI-level team (not sub-teams).

### Frontmatter Schema
Learning memos use the standard document frontmatter with specific conventions:

```yaml
id: learnings-2025-001              # Sequential numbering
title: "Q3 2025 Learnings Memo - [PM Name]"
type: doc
status: approved                     # Historical quarters are approved
team: data                          # DAI-level team (data, gtm-studio, platform, etc.)
owner: "[[teams/data/_people/jody-roberts]]"  # Wiki-link to person doc
created: "2025-12-23"
updated: "2025-12-23"
tags:
  - learnings
  - q3-2025
  - data                            # Team tag for filtering
related: []
```

### Content Structure
Learning memos typically follow this structure:
1. **Metric Alignment**: Connection to north star metrics and results
2. **Key Learnings**: Deep insights and discoveries from the quarter
3. **Hypotheses & Results**: What was tested and validated/invalidated
4. **Go-forward Changes & Plan**: Strategic shifts based on learnings
5. **Leveraging AI**: How AI was used and infrastructure insights

### Special Documents
- `FOUNDATIONAL-LEARNINGS.md`: Extracted cross-cutting learnings formatted as reusable institutional knowledge
- `Q3-2025-LEARNINGS-ANALYSIS-SUMMARY.md`: Executive-level synthesis across all team memos

### Querying and Discovery
- **By team**: Filter using `team` field in frontmatter (e.g., "Show all gtm-studio learnings")
- **By quarter**: Browse folder structure (e.g., `learnings-memos/Q3-2025/`)
- **By tag**: Use tags for cross-cutting themes (e.g., "ai-infrastructure", "customer-trust")
- **By person**: Follow `owner` wiki-links to see all memos by a PM

### Creating New Learning Memos
Use the `_templates/learnings-memo.md` template (if available) or follow the standard structure. New quarterly memos should:
1. Be placed in the appropriate quarter folder
2. Include proper frontmatter with team association
3. Follow the content structure conventions
4. Link to person docs for ownership

## Document Types

All documents use structured YAML frontmatter. Available templates in `_templates/`:

- **PRD** (Product Requirement Document): Detailed feature/initiative specs
- **RFC** (Request for Comments): Technical or product proposals requiring review
- **One-Pager**: Brief proposals or ideas (lighter than PRDs)
- **Six-Pager**: Amazon-style narrative documents for deep thinking
- **Person**: Individual profile and information
- **Weekly Report**: Team weekly status reports

## Weekly Reports System

### Overview
The weekly reports system enables teams to submit individual weekly reports that are synthesized into a cross-team executive intelligence brief.

### Structure
- **Team Reports**: Stored in each team's `weekly-reports/` folder
  - Flat teams: `teams/{team-name}/weekly-reports/{team-slug}-weekly-report-{YYYY-MM-DD}.md`
  - Sub-teams: `teams/{dai}/[subteam]-{subteam}/weekly-reports/{team-slug}-weekly-report-{YYYY-MM-DD}.md`
  - Example: `teams/gtm-studio/weekly-reports/gtm-studio-weekly-report-2025-12-27.md`
  - Example: `teams/intelligence/[subteam]-context-engineering/weekly-reports/context-engineering-weekly-report-2025-12-27.md`

- **Product Executive Reports**: Stored in `teams/leadership/documentation/weekly-product-executive-reports/`
  - Cross-team synthesis combining all team reports
  - File naming: `product-executive-report-{YYYY-MM-DD}.md`
  - Example: `teams/leadership/documentation/weekly-product-executive-reports/product-executive-report-2025-12-27.md`

- **DAI Weekly Reports**: Stored in `teams/leadership/weekly-reports/`
  - Cross-DAI status reports
  - File naming: `dai-weekly-report-{YYYY-MM-DD}.md`

### Using the Weekly Synthesis Skill

When the user wants to create a cross-team synthesis report:

1. Ensure all team reports for the week are in their respective team folders
2. Run the `weekly-synthesis` skill (invoke using Skill tool)
3. The skill will:
   - Discover all team reports using glob pattern: `teams/**/weekly-reports/*-weekly-report-{YYYY-MM-DD}.md`
   - Apply strategic framework analysis
   - Generate executive summary with analysis tables
   - Create main body with strategic category sections
   - Produce appendix with full team reports
   - Save to `teams/leadership/documentation/weekly-product-executive-reports/product-executive-report-{YYYY-MM-DD}.md`

## Key Conventions

### YAML Frontmatter
All documents must include standardized frontmatter fields:
- `id`: Unique identifier (format: `{type}-{YYYY}-{NNN}`)
- `title`: Human-readable title
- `type`: Document type (prd, rfc, one-pager, six-pager, person, weekly-report)
- `status`: Lifecycle state (draft, review, approved, archived)
- `team`: DAI-level team slug (e.g., "intelligence", "platform", "ops")
- `owner`: Wiki-link to person (e.g., `[[_people/adam-schoenfeld]]`)
- `created`: ISO 8601 date (YYYY-MM-DD)
- `updated`: ISO 8601 date (YYYY-MM-DD)
- `tags`: List of tags for discovery
- `related`: List of related document IDs

**Person document fields**:
- `team`: DAI-level team (e.g., "intelligence")
- `subteam`: Sub-team folder name (e.g., "context-engineering") - optional, only for hierarchical teams
- `role`: Role/specialization (e.g., "Company Data", "GTM context service")
- `github`: GitHub username

### Wiki-Links
Reference other documents using wiki-link syntax:
```markdown
[[teams/intelligence/_people/adam-schoenfeld]]
[[teams/intelligence/prds/gtmbench-v1]]
```

### File Naming
- **PRDs/RFCs/One-Pagers/Six-Pagers**: Descriptive kebab-case (e.g., `entity-resolution.md`)
- **Team Weekly Reports**: `{team-slug}-weekly-report-YYYY-MM-DD.md` (e.g., `gtm-studio-weekly-report-2025-12-27.md`)
- **Product Executive Reports**: `product-executive-report-YYYY-MM-DD.md` (synthesis reports)
- **DAI Weekly Reports**: `dai-weekly-report-YYYY-MM-DD.md` (cross-DAI status)
- **Person Docs**: `{first-name-last-name}.md` (e.g., `adam-schoenfeld.md`)

## Teams

Current teams in the repository:

### DAIs (Directly Accountable Individuals)
- **gtm-workspace**: GTM Workspace (Victor Oliveros) - Flat structure
- **data**: Data organization (Brandon Tucker, CDO) - Hierarchical structure:
  - `[subteam]-data-executive-team`: Brandon's executive team
  - `[subteam]-core-data`: Jody Roberts' core data team
- **gtm-studio**: GTM Studio (Sneh Kakileti) - Flat structure
- **intelligence**: Intelligence platform (Adam Smith) - Hierarchical structure:
  - `[subteam]-context-engineering`: Context engineering team
  - `[subteam]-semantic-data`: Semantic data team
  - `[subteam]-mcp`: MCP team
  - `[subteam]-intelligence-executive-team`: Executive team
- **platform**: Platform services (Ali Sadat) - Hierarchical structure:
  - `[subteam]-admin`: Admin team
  - `[subteam]-automation`: Automation team
  - `[subteam]-data-platform`: Data platform team
  - `[subteam]-integrations`: Integrations team
  - `[subteam]-zim`: ZIM team
- **ops**: ProductOps, BI, PMM (AJ Belen, Brett Jacobs) - Hierarchical structure:
  - `[subteam]-product-ops`: Product operations team
  - `[subteam]-business-intelligence`: BI team
  - `[subteam]-product-marketing`: PMM team

### Leadership
- **leadership**: Cross-team leadership documents (Dominik Facher, CPO)

For detailed team mapping and organizational structure, see [Team Mapping](TEAM-MAPPING.md)

## Global Knowledge Base

The ProductOps team (`teams/ops/`) manages organization-wide resources:
- Canonical buyer and user personas
- Shared terminology and glossary
- JTBD frameworks
- Process documentation

## Best Practices

When working with this repository:
- Always use templates from `_templates/` for new documents
- Fill out all required frontmatter fields
- Use wiki-links to reference other documents and people
- Keep `status` and `updated` fields current
- Commit with clear, descriptive messages
- Never edit files in `_utilities/` (machine-generated)

## Git Workflow Best Practices

### Staying Current
Since multiple PMs work in this repository simultaneously, staying current with latest changes reduces conflicts:

**Before starting a new document or making changes:**
- If it's been more than 4 hours since you last pulled, suggest: "Want me to pull the latest changes first?"
- This is especially important if working on a document someone else might touch

**The repository has automated protections:**
- Auto-rebase on push: If master has moved ahead, git automatically rebases your changes on top
- Pre-commit conflict detection: Warns if file was modified remotely before you commit
- Conflict resolution skill: If conflicts occur, use the `resolve-conflicts` skill to guide user through resolution

**When conflicts happen:**
- Don't panic - conflicts are normal when teams collaborate
- Trigger the `resolve-conflicts` skill to walk through resolution conversationally
- The skill will show both versions clearly and help user choose which to keep

### For Claude Code

**CRITICAL: Default Workflow - Branch-Based PR**
- **NEVER push directly to master** unless user explicitly asks (and is admin)
- **DEFAULT workflow**: Work on local master, then create branch + PR when ready to share
- Users work on master locally (simple, familiar)
- When ready: create ephemeral branch, push, and open PR for review

**Branch Protection:**
- Repository has branch protection rules that prevent direct pushes to master for non-admin users
- PRs are required for all changes (GitHub enforces this)
- Only admins can push directly to master (and should only do so when explicitly requested)

**Starting a session:**
- Check last pull time: `git log -1 --format=%cr origin/master`
- If >4 hours, suggest pulling: "I see it's been X hours since the last pull. Want me to fetch the latest changes?"

**Before committing:**
- Pre-commit hook checks for remote changes
- Guide user to pull if conflicts detected

**When user is ready to share (says "create PR", "ready to share", "open PR"):**

1. **Auto-generate branch name** using pattern: `{team-or-area}/{brief-description}`
   - Infer from: files changed (team folder), commit messages (subject)
   - Examples: `intelligence/gtmbench-prd`, `weekly-reports/2026-01-08`, `ops/voc-analysis-q1`

2. **Confirm with user:** "I'll create branch `intelligence/gtmbench-prd` and open a PR. Want to rename the branch?"
   - If yes: accept new name and proceed
   - If no: proceed with auto-generated name

3. **Prompt for reviewers:**
   - Ask: "Who should review this PR? (You can specify GitHub usernames like @adam-smith @brett-jacobs, or press Enter to use team defaults from CODEOWNERS)"
   - Parse user input:
     - Extract GitHub handles (with or without @ prefix)
     - If user presses Enter or says "defaults" or "skip", use CODEOWNERS defaults
   - Store reviewer list for PR creation command

4. **Execute PR creation:**
   ```bash
   git checkout -b {branch-name}              # Create branch from current master
   git push -u origin {branch-name}           # Push branch to remote
   ```

   **Create pull request:**
   - Detect GitHub CLI:
     - Try `gh` command first
     - If not found, check common Windows paths:
       - `/c/Program Files/GitHub CLI/gh.exe`
       - `$LOCALAPPDATA/Programs/GitHub CLI/gh.exe`

   - Build PR body with standard format:
     ```markdown
     ## Summary
     {auto-generated or user-provided summary}

     ## Changes
     {list of changed files}
     ```

   - Create PR with reviewers if specified:
     - If reviewers provided: `gh pr create --base master --head {branch-name} --title "..." --body "..." --reviewer {reviewer1} --reviewer {reviewer2}`
     - If no reviewers (use CODEOWNERS): `gh pr create --base master --head {branch-name} --title "..." --body "..."`

   - If authentication fails: User needs to run onboarding skill to authenticate to `git.zoominfo.com`

5. **After PR is created:**
   - Display PR URL for user to review/merge
   - Remind user: "Once the PR is merged, let me know and I'll clean up the branch and switch you back to master"

6. **After user confirms PR is merged:**
   - Switch back to master: `git checkout master`
   - Pull latest changes: `git pull origin master`
   - Delete local branch: `git branch -D {branch-name}`
   - Confirm: "You're back on master with the latest changes, and the feature branch has been cleaned up"

**If push fails with conflict:**
- Invoke `resolve-conflicts` skill automatically
- Walk through resolution conversationally

**Remember:** The goal is to make git invisible. Users work on master locally for simplicity, but PRs provide a review gate before changes go live. Branches are ephemeral and only exist for the PR lifecycle. Always clean up and return to master after PR merge.

## Additional Resources

- [Repository README](README.md) - Getting started guide
- [Team Mapping](TEAM-MAPPING.md) - Organizational structure and folder conventions
- [Templates Directory](_templates/) - All available templates
