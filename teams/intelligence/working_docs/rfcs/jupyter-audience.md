---
id: rfc-jupyter-2026-001
title: "Natural Language Jupyter Notebooks for Data Enrichment"
type: rfc
status: draft
team: intelligence
owner: "[[teams/intelligence/_people/adam-smith]]"
created: "2026-01-12"
updated: "2026-01-12"
tags:
  - data-enrichment
  - jupyter
  - natural-language
  - revops
related: []

# RFC-specific fields
reviewers: []
decision_date:
supersedes:
superseded_by:
---

# Natural Language Jupyter Notebooks for Data Enrichment

## Problem

Revenue teams constantly deal with messy data that requires cleaning, disambiguation, and enrichment before use. Common scenarios:

- Event attendee lists that need enrichment, CRM import, and deduplication
- Landing page URLs that need scraping to extract structured data
- CSV exports with combined fields (e.g., full name) that need parsing

This process isn't fully automatable because it requires iterative decision-making: testing transformations, reviewing results, adjusting approaches. Traditional automation fails because each dataset has unique quirks.

## Proposed Solution

A **web-based Jupyter Notebook interface** designed for natural language instructions, targeting RevOps and GTM engineers who don't code.

### Core Concept

Each "cell" is an AI agent that:
- Accepts natural language instructions
- Can write JavaScript internally if needed
- Processes data row-by-row
- Has access to tools (web search, API calls, etc.)

Like traditional Jupyter Notebooks, users can run one cell at a time, iterate on transformations, and preview results before running on full datasets.

## User Experience

### Layout

```
┌─────────────────────────────────────────────────────────────┐
│  Notebook Cells (1/3)      │    Table Preview (2/3)        │
│                            │                                │
│  [Data Source: CSV]        │    First Name │ Last Name │...│
│                            │    ───────────┼───────────┼───│
│  [Cell 1: Split name...]   │    John       │ Smith     │   │
│                            │    Jane       │ Doe       │   │
│  [Cell 2: Research...]     │    ...        │ ...       │   │
│                            │                                │
│  [+ Add Cell]              │                                │
└─────────────────────────────────────────────────────────────┘
                    [Run Preview (10 rows)] [Run All]
```

### Starting a Notebook (Wizard)

First step is always defining the data source:

1. **CSV/Excel upload** → Renders directly into table
2. **URL input** → Requires natural language instruction describing what to extract (agent handles scraping strategy)

### Cell Types & Instructions

Cells use natural language with `@column` mentions for referencing existing columns:

**Examples:**
- "Split @full_name into first_name and last_name columns"
- "Concatenate @first_name and @last_name into a display_name column"
- "Research whether @company_name has done funding recently using web search"
- "Add a column that looks up @email in ZoomInfo and returns the matched contact ID"

### Two Interaction Modes

Some users think **linearly** (step-by-step process), others think **spatially** (table-first). Support both:

1. **Notebook view**: Add cells sequentially, run in order
2. **Table view**: Click `+` on table grid to add columns with natural language descriptions

Both views modify the same underlying data structure. Adding a column in the table view is equivalent to adding a cell in the notebook view.

### Preview vs. Full Run

- **Preview mode**: Runs on first 10 rows for fast iteration
- **Full run**: Processes entire dataset (can be costly/slow for large datasets)

Users iterate in preview mode, then run the full notebook once transformations are validated.

## Entity Linking

A key goal is disambiguating rows to canonical entities in source systems (ZoomInfo, Salesforce).

### How It Works

Each notebook has an entity type (contact, organization, etc.). Users can configure canonical linking:

```
Link Settings:
  Entity Type: Contact
  Target Systems: [ZoomInfo, Salesforce]
  Match Fields: first_name, last_name, company_name, email
  Confidence Threshold: 0.8
```

The system attempts to match each row to a canonical entity and shows match success rates.

### As a Column Function

Alternatively, linking can be expressed as a column operation:

```
Add column: zi_contact_id
Instruction: "Link to ZoomInfo contact using @first_name, @last_name, @company_name, @email"
```

Returns:
- Matched entity ID (if confidence > threshold)
- "No match" (if below threshold)
- Match confidence score (optional)

## Export Options

- CSV / Excel download
- Google Sheets export
- Direct push to CRM (Salesforce, HubSpot)
- ZoomInfo enrichment writeback

## Technical Considerations

### Data Model

Separate concerns:

1. **Notebook definition** (JSON object):
   - Data source configuration
   - Cell/column definitions (instructions, order)
   - Entity type and linking settings

2. **Data storage**:
   - Raw input data
   - Transformed/enriched data
   - Separate from notebook structure

### Agent Capabilities per Cell

Each cell's agent needs access to:
- JavaScript execution (for transformations)
- Web search tool
- ZoomInfo API (person search, company search)
- Salesforce API (for linking)
- Custom tools as needed

### Execution Model

- Cells execute in order (can't run cell N without cells 1 to N-1)
- Each cell processes rows independently
- Results cached for re-runs without re-execution

## Open Questions

1. **How granular should cell types be?** Pre-built templates vs. fully natural language?
2. **How to handle errors mid-run?** Skip row? Halt? Retry?
3. **Collaboration?** Can multiple users work on same notebook?
4. **Versioning?** Track changes to notebook definitions?
