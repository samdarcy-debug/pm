---
id: doc-2026-001
title: ZoomInfo Product Organization - Team Mapping
type: documentation
status: approved
team: leadership
owner: "[[teams/ops/people/daniel-kong]]"
created: 2026-01-07
updated: 2026-01-07
tags: [organization, teams, structure]
---

# ZoomInfo Product Organization - Team Mapping

This document defines the organizational structure of the ZoomInfo Product organization, mapping leadership hierarchy to team folders in this repository.

## Leadership Hierarchy

### Chief Product Officer
- **Dominik Facher** - Chief Product Officer
  - Oversees all product DAIs and cross-functional initiatives
  - Team folder: `/teams/leadership/`

## Directly Accountable Individuals (DAIs)

### Data Organization
**Brandon Tucker** - Chief Data Officer

Brandon leads the data organization with the following structure:

#### [Subteam] Data Executive Team
- **Team folder**: `/teams/data/[subteam]-data-executive-team/`
- **Leader**: Brandon Tucker
- **Scope**: Executive-level data strategy, cross-data initiatives, data platform vision
- **Key areas**: Data quality, data governance, data platform roadmap

#### [Subteam] Core Data Team
- **Team folder**: `/teams/data/[subteam]-core-data/`
- **Leader**: Jody Roberts (reports to Brandon)
- **Scope**: Core data products and services
- **Key areas**: Contact data, company data, entity resolution, data enrichment

### GTM Studio
**Sneh Kakileti** - DAI, GTM Studio

- **Team folder**: `/teams/gtm-studio/`
- **Structure**: Flat (single team, no sub-teams)
- **Scope**: GTM Studio product development and strategy
- **Key areas**: Studio features, workflow automation, sales enablement tools

### GTM Workspace (formerly Copilot)
**Victor Oliveros** - DAI, GTM Workspace

- **Team folder**: `/teams/gtm-workspace/` (renamed from `/teams/copilot/`)
- **Structure**: Flat (single team, no sub-teams)
- **Scope**: GTM Workspace product development and strategy
- **Key areas**: Workspace features, AI-powered workflows, productivity tools

### Intelligence Platform
**Adam Smith** - DAI, Intelligence Team

Adam leads the intelligence organization with the following structure:

#### [Subteam] Intelligence Executive Team
- **Team folder**: `/teams/intelligence/[subteam]-intelligence-executive-team/`
- **Leader**: Adam Smith
- **Scope**: Intelligence organization executive team
- **Key areas**: Strategic planning, cross-intelligence coordination

#### [Subteam] Semantic Data Team
- **Team folder**: `/teams/intelligence/[subteam]-semantic-data/`
- **Leader**: Reports to Adam Smith
- **Scope**: Data semantics and knowledge graph
- **Key areas**: Entity resolution, semantic layers, data enrichment

#### [Subteam] Context Engineering Team
- **Team folder**: `/teams/intelligence/[subteam]-context-engineering/`
- **Leader**: Reports to Adam Smith
- **Scope**: Context generation and AI grounding
- **Key areas**: GTM context service, AI context systems

#### [Subteam] MCP Team
- **Team folder**: `/teams/intelligence/[subteam]-mcp/`
- **Leader**: Reports to Adam Smith
- **Scope**: Model Context Protocol implementation
- **Key areas**: MCP servers, protocol development, integrations

### Platform
**Ali Sadat** - DAI, Platform Team

Ali leads the platform organization with the following structure:

#### [Subteam] Integrations Team
- **Team folder**: `/teams/platform/[subteam]-integrations/`
- **Leader**: Andres Perez (reports to Ali)
- **Scope**: Third-party integrations and connectors
- **Key areas**: CRM integrations, API partnerships, connector development

#### [Subteam] Admin Team
- **Team folder**: `/teams/platform/[subteam]-admin/`
- **Leader**: Brannen Huske (reports to Ali)
- **Scope**: Administrative features and user management
- **Key areas**: User admin, permissions, settings management

#### [Subteam] Automation Team
- **Team folder**: `/teams/platform/[subteam]-automation/`
- **Leader**: Marc Frail (reports to Ali)
- **Scope**: Workflow automation and orchestration
- **Key areas**: Automation engine, workflow builder, triggers

#### [Subteam] ZIM Team
- **Team folder**: `/teams/platform/[subteam]-zim/`
- **Leader**: Anwar Mai (reports to Ali)
- **Scope**: ZoomInfo Messaging platform
- **Key areas**: Messaging infrastructure, email/calling features

#### [Subteam] Data Platform Team
- **Team folder**: `/teams/platform/[subteam]-data-platform/`
- **Leader**: Marc Delurgio (reports to Ali)
- **Scope**: Platform data infrastructure
- **Key areas**: Data pipelines, platform databases, data services

### Operations
**AJ Belen** - DAI, Operations/BI/PMM

AJ and Brett lead the operations organization with the following structure:

#### [Subteam] Product Marketing Team
- **Team folder**: `/teams/ops/[subteam]-product-marketing/`
- **Leader**: Reports to AJ Belen
- **Scope**: Product marketing and go-to-market strategy
- **Key areas**: Product positioning, messaging, launch strategy, competitive intelligence

#### [Subteam] Business Intelligence Team
- **Team folder**: `/teams/ops/[subteam]-business-intelligence/`
- **Leader**: Reports to AJ Belen
- **Scope**: Product analytics and business intelligence
- **Key areas**: Product metrics, dashboards, data analysis, reporting

#### [Subteam] Product Operations Team
- **Team folder**: `/teams/ops/[subteam]-product-ops/`
- **Leader**: Brett Jacobs (reports to AJ Belen)
- **Scope**: Product operations and knowledge management
- **Key areas**: Process documentation, knowledge systems, org-wide resources, tools

## Team Folder Structure Patterns

### Hierarchical Teams (Multiple Sub-teams)

Used when a DAI oversees multiple distinct teams:

```
/teams/{dai}/
├── _people/                      # All team members (DAI-level permissions)
├── [subteam]-{subteam-1}/
│   ├── weekly-reports/           # Required: team status reports
│   └── [custom]/                 # Team-controlled organization
└── [subteam]-{subteam-2}/
    ├── weekly-reports/           # Required: team status reports
    └── [custom]/                 # Team-controlled organization
```

**Current examples**:
- Data team (`/teams/data/`) - 2 sub-teams
- Intelligence team (`/teams/intelligence/`) - 4 sub-teams
- Platform team (`/teams/platform/`) - 5 sub-teams
- Operations team (`/teams/ops/`) - 3 sub-teams

**Note**: Sub-team folders use the `[subteam]-` prefix to visually distinguish them from standard folders like `_people/` and `weekly-reports/`. Beyond the required `weekly-reports/` folder, teams organize content as they see fit (common patterns: `prds/`, `rfcs/`, `documentation/`).

### Flat Teams (Single Team)

Used when a DAI leads a single cohesive team:

```
/teams/{team-name}/
├── _people/                      # Required: team member profiles
├── weekly-reports/               # Required: team status reports
└── [custom]/                     # Team-controlled organization
```

**Current examples**: gtm-studio, gtm-workspace

## Team Naming Conventions

### Folder Naming
- Use kebab-case for folder names
- Keep names concise but descriptive
- Align with how teams refer to themselves

### Document Naming
- **Person profiles**: `{firstname-lastname}.md` in `_people/` folder (e.g., `_people/brandon-tucker.md`)
- **Weekly reports**: `{team-slug}-weekly-report-YYYY-MM-DD.md`
- **Other docs**: Descriptive kebab-case (e.g., `data-quality-framework.md`)

## Adding New Teams or Sub-teams

When organizational structure changes:

1. **For new DAI teams**: Create flat structure under `/teams/{new-team-name}/`
2. **For new sub-teams**: Create subfolder under existing DAI team
3. **Update this document**: Add team mapping details
4. **Create people profiles**: For team members with `team` and `github` fields
5. **Regenerate CODEOWNERS**: Run `python .automation/scripts/maintenance/generate-codeowners.py`

## Person Profile Requirements

All person profiles in `teams/*/_people/*.md` must include these fields in YAML frontmatter:

- **`id`**: Unique identifier in format `person-{slug}` (e.g., `person-brett-jacobs`)
- **`title`**: Full name
- **`type`**: Must be `person`
- **`team`**: Team slug matching folder name (e.g., `ops`, `intelligence`, `gtm-studio`)
- **`domain`**: Area of ownership (e.g., "Product Operations", "Data Semantics")
- **`github`**: GitHub username (required for CODEOWNERS generation)
  - Must match GitHub Enterprise username exactly
  - Format: lowercase alphanumeric + hyphens only
  - Example: `github: brett-jacobs`
- **`created`**: Date in YYYY-MM-DD format
- **`updated`**: Date in YYYY-MM-DD format

The `github` field is critical for automatic CODEOWNERS generation. Without it, team members won't have PR approval rights to their team's folder.

To validate person profiles, run:
```bash
python .automation/scripts/maintenance/validate-person-profiles.py
```

## Team Ownership and Approvals

### Quick Reference
- **Team folders**: PR required, self-approval allowed for team members
- **People profiles**: Automatic CODEOWNERS generation via pre-commit hook
- **Cross-team/leadership docs**: Requires ProductOps + Dominik approval

## Historical Context

### Recent Changes (January 2026)
- **Renamed**: `copilot` → `gtm-workspace` (reflects product naming)
- **Added**: `gtm-studio` team folder
- **Implemented**: Profile-driven CODEOWNERS generation
- **Documented**: This team mapping structure
- **Migrated**: From `working_docs/` folder system to PR-based workflow (January 2026)

### Deprecated Naming
- ~~"Copilot"~~ → Use "GTM Workspace"
- ~~`working_docs/`~~ → Teams now organize folders as they see fit

## See Also

- [CLAUDE.md](CLAUDE.md) - Repository structure and PR workflow
- [README.md](README.md) - Getting started guide
- [CODEOWNERS Generation Script](.automation/scripts/maintenance/generate-codeowners.py)
