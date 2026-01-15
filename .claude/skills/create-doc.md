# Create Document

**Description**: Interactive, conversational document creation for the PM knowledge repository. Create PRDs, RFCs, one-pagers, six-pagers, or any custom document type. Works with existing templates when available, or creates flexible custom documents when no template exists. After creation, offers to templatize custom documents for team reuse.

**Triggers (Strong)**: Use this skill when the user explicitly requests document creation:
- "Create a PRD for [topic]"
- "Write an RFC about [topic]"
- "Draft a one-pager on [topic]"
- "Start a six-pager for [topic]"
- "Create a document about [topic]"
- "Write a [doc-type] for [topic]"

**Triggers (Conditional)**: May use this skill if context suggests document creation:
- User provides extensive content and mentions wanting to "save it" or "create a doc"
- User asks "how do I create a PRD?" (explain + offer to help create one)

**Do NOT Trigger**:
- User is just asking questions about the repository (use search skill)
- User wants to convert an existing file (use convert skill)
- User wants content synthesis (use oracle skill)
- User is setting up for the first time (use onboard skill)

---

## Instructions

You are an interactive document creation assistant for the PM knowledge repository. Your job is to guide users through creating structured documents in a conversational, non-tedious way. The system uses a two-tier approach:

**Tier 1 (Template Exists)**: Use existing template structure for well-defined doc types (PRD, RFC, one-pager, six-pager)
**Tier 2 (No Template)**: Create flexible custom document with just frontmatter + user's content

After successfully creating a custom document, always offer to templatize it so the team can reuse the structure.

---

## Step-by-Step Process

### Step 1: Check for Person Doc

**Before doing anything else**, verify the user has a person doc:

```bash
# Get git username
git config user.name

# Search for their person doc
find teams/ -path "*/people/*.md" -type f -exec grep -l "title: [their name]" {} \;
```

**If no person doc found**:
- Tell user: "I don't see your person doc yet. Let's set that up first before creating documents."
- Suggest they run the onboard skill: "Say 'onboard me' to get started."
- **STOP** - do not proceed with document creation

**If person doc found**:
- Note the path (e.g., `teams/ops/_people/brett-jacobs.md`)
- Read the person doc to extract:
  - `team`: DAI-level team (e.g., `ops`)
  - `subteam`: Sub-team folder name (e.g., `product-ops`) - only present for hierarchical teams
- Store both values for path construction
- Continue to Step 2

---

### Step 2: Detect Document Type

Ask the user what type of document they want to create, or infer from their request:

**Common types with templates**:
- `prd` - Product Requirement Document
- `rfc` - Request for Comments
- `one-pager` - Brief proposal
- `six-pager` - Amazon-style narrative
- `agent-prd` - AI agent specification
- `doc` - Generic documentation

**Custom types**: Any other type the user mentions (e.g., "weekly report", "strategy memo", "postmortem")

Check if template exists:
```bash
# Check for template
ls _templates/ | grep -i "{doc-type}"
```

**If template exists**: Proceed with Tier 1 (Template-Based Creation)
**If no template**: Proceed with Tier 2 (Flexible Creation)

---

### Step 3A: Template-Based Creation (Tier 1)

When a template exists, offer the user **three creation modes**:

**Mode 1: Context-First (Recommended)**
- "Have you already written content for this? You can paste it and I'll structure it for you."
- User pastes existing content (from notes, draft, email, etc.)
- You map their content to template sections intelligently
- Fill gaps conversationally

**Mode 2: Guided**
- "Let's build this step by step."
- Walk through each major section of the template
- Ask questions, gather input, build incrementally

**Mode 3: Hybrid**
- "Give me what you have, and I'll ask about the rest."
- User provides partial content
- You fill template sections they covered
- Ask about remaining sections

**For each mode**:

1. **Gather metadata** (conversational, not a form):
   - Title: "What's the title of this {doc-type}?"
   - Team: Default to their team, confirm: "I'll create this for the {team} team. Sound good?"
   - Tags: "Any tags for discoverability? (e.g., agents, Q1-2025, entity-resolution)"
   - Related docs: "Is this related to any existing documents?" (optional)

2. **Map/gather content** based on mode:
   - Context-first: Intelligently map their content to template sections
   - Guided: Walk through major sections (Problem, Solution, Success Metrics, etc. for PRD)
   - Hybrid: Fill what they provided, ask for the rest

3. **Generate ID**:
   ```bash
   # Find existing docs of this type for current year
   find teams/ -path "*/{type}s/*.md" -o -path "*/documentation/*.md" -type f | \
     xargs grep -h "^id: {type}-2026-" 2>/dev/null | \
     sed "s/id: {type}-2026-//" | \
     sort -n | tail -1
   # Next ID: {type}-2026-{max+1}, e.g., prd-2026-003
   ```

4. **Prompt for destination folder**:

   Ask the user where this document should be placed:

   ```
   Where should I create this document?

   [1] teams/{team}/prds/ (Default - team PRDs folder)
   [2] teams/{team}/{custom-folder}/ (Specify custom subfolder)
   [3] {other-path} (Specify full path)

   Note: Creating in global/shared folders (like _templates/) will require approval
   from global CODEOWNERS.
   ```

   **Default suggestions based on doc type**:
   - prd, agent-prd → `teams/{team}/prds/`
   - rfc → `teams/{team}/rfcs/`
   - one-pager → `teams/{team}/one-pagers/`
   - six-pager → `teams/{team}/six-pagers/`
   - doc → `teams/{team}/documentation/`

   **For hierarchical teams**, use the subteam folder:
   - `teams/{team}/[subteam]-{subteam}/{folder}/`

   **Examples**:
   - Flat team (gtm-studio): `teams/gtm-studio/prds/feature-name.md`
   - Hierarchical team (ops/product-ops): `teams/ops/[subteam]-product-ops/prds/feature-name.md`

   **If user chooses custom location**:
   - Accept their path
   - Warn if it's a global/shared folder: "This is a shared folder. Your PR will need approval from global CODEOWNERS (Product Ops team)."
   - Confirm: "Got it, I'll create at: {custom-path}. Proceed?"

5. **Preview and confirm**:
   ```
   I'll create this document:

   ID: prd-2026-003
   Title: Entity Resolution Engine
   Type: PRD
   Team: intelligence
   Subteam: context-engineering (if hierarchical team structure)
   Path: teams/intelligence/[subteam]-context-engineering/prds/entity-resolution-engine.md

   Look good? (yes/adjust title/change location)
   ```

6. **Write the file** using Write tool with full frontmatter + content

7. **Confirm creation**:
   ```
   Created [Entity Resolution Engine](teams/intelligence/[subteam]-context-engineering/prds/entity-resolution-engine.md)

   Next steps:
   - Review and edit if needed
   - Create a PR when ready to share for review
   - Update status to 'review' or 'approved' as appropriate
   - Link related documents in frontmatter
   ```

---

### Step 3B: Flexible Creation (Tier 2)

When no template exists, create a flexible custom document:

1. **Gather metadata** (same as Tier 1):
   - Title
   - Document type (their custom type, e.g., "weekly-report")
   - Team (default to their team)
   - Tags
   - Related docs (optional)

2. **Gather content** conversationally:
   - "Tell me about this {doc-type}. What should it include?"
   - "Paste any content you have, or describe what you want to cover."
   - Accept free-form content - don't force into predefined structure
   - Organize sensibly with headings based on their content

3. **Generate ID**:
   - If custom type: `{type}-2026-001` (e.g., `weekly-report-2026-001`)
   - Or use generic: `doc-2026-001`

4. **Prompt for destination folder**:

   Ask the user where this custom document should be placed:

   ```
   Where should I create this {doc-type}?

   [1] teams/{team}/documentation/ (Default - team documentation folder)
   [2] teams/{team}/{custom-folder}/ (Specify custom subfolder)
   [3] {other-path} (Specify full path)

   Note: Creating in global/shared folders will require approval from global CODEOWNERS.
   ```

   **Default for custom docs**: `teams/{team}/documentation/`
   **For hierarchical teams**: `teams/{team}/[subteam]-{subteam}/documentation/`

   **If user chooses custom location**:
   - Accept their path
   - Warn if it's a global/shared folder
   - Confirm: "Got it, I'll create at: {custom-path}. Proceed?"

5. **Preview and confirm**:
   ```
   I'll create this document:

   ID: weekly-report-2026-001
   Title: Weekly Report - Jan 6 2026
   Type: weekly-report
   Team: ops
   Subteam: product-ops (if hierarchical team structure)
   Path: teams/ops/[subteam]-product-ops/documentation/weekly-report-jan-6.md

   Look good? (yes/adjust title/change location)
   ```

6. **Write the file**:
   ```yaml
   ---
   id: weekly-report-2026-001
   title: Weekly Report - Jan 6 2026
   type: weekly-report
   status: draft
   team: ops
   owner: [[teams/ops/_people/brett-jacobs]]
   created: 2026-01-06
   updated: 2026-01-06
   tags: []
   related: []
   ---

   # Weekly Report - Jan 6 2026

   [User's content organized sensibly]
   ```

7. **Offer to templatize**:
   ```
   This is a nice structure! Want to make this a template so anyone on the team can create weekly reports?

   If you say yes, I'll:
   - Create a template file in _templates/weekly-report.md
   - Create a skill file in .claude/skills/weekly-report.md
   - Submit as a PR for Product Ops review
   ```

---

### Step 4: Templatization (Optional)

If user wants to templatize a custom doc, delegate to the `create-skill` skill for comprehensive template and skill generation.

**When user says yes to templatization**:

Say: "Great! I'll hand this over to the skill creator to generate a high-quality template and skill for you. The create-skill workflow will interview you to understand the purpose and triggers, then use the document you just created as an example to extract structure."

**Then invoke the create-skill skill**:
```
Use the Skill tool to invoke "create-skill"
```

**Pass context in your delegation message**:
- Mention the document path that was just created
- Note the document type
- Explain that this is for templatizing an existing document

**Example delegation**:
```
The user just created a custom document at teams/ops/documentation/weekly-report-2026-001.md (type: weekly-report) and wants to templatize it for team reuse. Please use this document as an example to generate a template and skill.
```

**After skill completes**:
The create-skill skill will:
- Interview the user about purpose, triggers, and structure
- Use the created document as an example
- Generate template file in `_templates/`
- Generate comprehensive skill file in `.claude/skills/`
- Create branch, commit, and PR for Product Ops review
- Return PR URL to user

---

## Important Notes

1. **Always check for person doc first** - don't proceed without it

2. **Team defaults to user's team** - extracted from their person doc path

3. **Be conversational** - this should feel like a chat, not a form

4. **Context-first is preferred** - most users have content already, just need it structured

5. **Don't force template sections** - if user doesn't have content for a section, either skip it or mark as "TBD"

6. **Flexible for custom docs** - don't constrain users to predefined doc types

7. **Templatization is optional** - only offer if it makes sense (good structure, reusable pattern)

8. **Templatization delegates to create-skill** - when user wants to templatize, hand off to create-skill for comprehensive template+skill generation with PR for Product Ops review

9. **File paths are suggested based on user's team and doc type** - users select from smart defaults or specify custom destination

10. **Folder targeting is explicit** - always prompt user for destination folder to ensure intentional placement

11. **IDs are auto-generated** - sequential numbering per type per year

12. **Wiki-links for people** - always reference people as `[[teams/{team}/people/{slug}]]`

13. **Date format** - always YYYY-MM-DD for created/updated dates

14. **Status defaults to 'draft'** - users can change later

15. **Make it easy** - users should just provide content, answer a few questions about destination, and you handle the rest

---

## Example Interactions

### Example 1: Template-Based (Context-First)

```
User: "Create a PRD for entity resolution"

Agent:
✓ Checks person doc - found: teams/intelligence/_people/jane-smith.md
✓ Team detected: intelligence
✓ Template found: _templates/prd.md

"I'll help you create a PRD for entity resolution.

Have you already written any content for this? If so, paste it and I'll structure it into the PRD template. If not, I can guide you step by step."

User: [pastes 3 paragraphs about the problem and proposed solution]

Agent:
"Great! I can see you've covered:
- Problem statement ✓
- Proposed solution ✓

Let me map this to the PRD template. A few quick questions:

1. What's the title? (suggestion: 'Entity Resolution Engine')
2. Any tags for searchability? (e.g., 'entity-resolution', 'data-quality')
3. What's the target ship date? (optional)
4. Success metrics? (What does good look like?)"

User: [answers questions]

Agent:
"Perfect! I'll create:

ID: prd-2026-003
Title: Entity Resolution Engine
Team: intelligence
Subteam: context-engineering
Path: teams/intelligence/[subteam]-context-engineering/prds/entity-resolution-engine.md

Proceed?"

User: "yes"

Agent:
[Writes file]

"Created [Entity Resolution Engine](teams/intelligence/[subteam]-context-engineering/prds/entity-resolution-engine.md)

Your PRD is ready! I've structured your content into:
- Problem Statement (from your description)
- Proposed Solution (from your description)
- Success Metrics (from your answers)
- Scope (marked as TBD - you can fill this in)

Feel free to open and edit directly if you want to add more detail."
```

### Example 2: Flexible Creation (Custom Doc Type)

```
User: "Create a post-mortem for the search outage"

Agent:
✓ Checks person doc - found: teams/platform/_people/alex-chen.md
✓ Team detected: platform
✗ No template found for 'post-mortem'

"I don't see a template for post-mortems yet, but I can create a flexible document for you.

What should this post-mortem include? Tell me about the outage and what you want to document."

User: [describes outage, impact, root cause, action items]

Agent:
"Got it. I'll create a post-mortem with these sections:
- Incident Overview
- Timeline
- Root Cause
- Impact
- Action Items

Title: 'Post-Mortem: Search Outage - Jan 6 2026'

Any tags? (e.g., 'incident', 'search', 'postmortem')"

User: "yes those tags"

Agent:
"Creating document:

ID: doc-2026-015
Title: Post-Mortem: Search Outage - Jan 6 2026
Type: postmortem
Team: platform
Path: teams/platform/documentation/postmortem-search-outage-jan-6.md

Proceed?"

User: "yes"

Agent:
[Writes file]

"Created [Post-Mortem: Search Outage - Jan 6 2026](teams/platform/documentation/postmortem-search-outage-jan-6.md)

This is a nice structure! Want to make this a template so anyone can create post-mortems with this format?

If yes, I'll create a template and skill, then submit a PR for Product Ops review."

User: "yes please"

Agent:
"Great! I'll hand this over to the skill creator to generate a high-quality template and skill for you. The create-skill workflow will interview you to understand the purpose and triggers, then use the document you just created as an example to extract structure."

[Invokes create-skill skill via Skill tool]
[create-skill conducts interview, reads the created document, generates template + skill, creates PR]

"The create-skill workflow has created PR #42: https://github.com/org/pm/pull/42

The Product Ops team will review the post-mortem template before it's available to everyone."
```

---

## Template Reading Reference

When working with template-based creation, you'll need to read the template to understand its structure:

```bash
# Read template
cat _templates/prd.md

# Extract section headings
grep "^##" _templates/prd.md

# Get frontmatter fields
sed -n '/^---$/,/^---$/p' _templates/prd.md
```

Key templates and their major sections:

**PRD**:
- Problem Statement
- Proposed Solution
- Success Metrics
- Scope
- Timeline
- Stakeholders

**RFC**:
- Summary
- Motivation
- Detailed Design
- Alternatives Considered
- Rollout Plan

**One-Pager**:
- Context
- Proposal
- Tradeoffs
- Success Criteria

**Six-Pager**:
- Introduction
- Goals
- Tenets/Principles
- Current State
- Proposal
- Alternatives Considered
