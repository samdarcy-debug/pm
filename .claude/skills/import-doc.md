# Convert Document

**Description**: Convert documents from various formats (Word, PDF, PowerPoint, CSV) into structured markdown for the PM knowledge repository. Uses a hybrid approach: pandoc if available for best quality, JavaScript libraries as fallback. Intelligently maps content to templates when possible. After conversion, offers to templatize custom document structures.

**Triggers (Strong)**: Use this skill when the user wants to convert an existing file:
- "Convert [file.docx] to markdown"
- "Import [file.pdf] as a PRD"
- "Turn this Word doc into an RFC"
- "Convert [file.pptx] to markdown"
- "Import [file.csv]"

**Triggers (Conditional)**: May use this skill if:
- User mentions they have an existing document they want to add to the repository
- User asks "how do I import a Word document?"

**Do NOT Trigger**:
- User wants to create a new document from scratch (use create skill)
- User is just asking questions about the repository (use search skill)
- User wants content synthesis (use oracle skill)
- User is setting up for the first time (use onboard skill)

---

## Instructions

You are a document conversion assistant for the PM knowledge repository. Your job is to convert documents from various formats into structured markdown, intelligently mapping content to templates when applicable. The system uses a hybrid conversion approach:

**Pandoc (Preferred)**: Best quality conversion for Word, PDF, PowerPoint
**JavaScript Fallback**: Works out-of-the-box if pandoc not installed
**CSV**: Keep as-is, just add frontmatter

After successfully converting a document with a custom structure, offer to templatize it for team reuse.

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
- Tell user: "I don't see your person doc yet. Let's set that up first before converting documents."
- Suggest they run the onboard skill: "Say 'onboard me' to get started."
- **STOP** - do not proceed with conversion

**If person doc found**:
- Note the path (e.g., `teams/ops/_people/brett-jacobs.md`)
- Extract their team slug from the path (e.g., `ops`)
- Continue to Step 2

---

### Step 2: Check for Pandoc (Hybrid Approach)

Check if pandoc is installed:

```bash
# Check for pandoc
which pandoc || where pandoc
```

**If pandoc found**:
- Note the path
- Set conversion method: "pandoc" (best quality)
- Tell user: "I'll use pandoc for high-quality conversion."

**If pandoc not found**:
- Set conversion method: "fallback" (JavaScript libraries)
- Tell user: "I'll use built-in conversion tools. For better results, you can install pandoc from https://pandoc.org/installing.html"
- Continue with fallback - **don't block the user**

---

### Step 3: Validate File and Detect Format

```bash
# Check if file exists
ls -lh "[file-path]"
```

**Detect format** from file extension:
- `.docx` → Word document
- `.pdf` → PDF document
- `.pptx` → PowerPoint presentation
- `.csv` → CSV file (keep as-is)

**If file not found**:
- Ask user to provide the correct path
- Suggest: "Try dragging the file into the terminal to get the full path."

**If format not supported**:
- List supported formats: Word (.docx), PDF, PowerPoint (.pptx), CSV (.csv)
- Ask if they can export to a supported format

---

### Step 4: Convert to Markdown

#### For Word Documents (.docx)

**If pandoc available**:
```bash
pandoc -f docx -t markdown --wrap=preserve "[file-path]" -o temp-conversion.md
```

**If fallback (no pandoc)**:
```bash
# Use mammoth.js via npx (Node.js)
npx -y mammoth "[file-path]" --output-format=markdown > temp-conversion.md
```

#### For PDF Documents (.pdf)

**If pandoc available**:
```bash
pandoc -f pdf -t markdown --wrap=preserve "[file-path]" -o temp-conversion.md
```

**If fallback (no pandoc)**:
```bash
# Use pdf-parse via Node.js script
node -e "
const fs = require('fs');
const pdfParse = require('pdf-parse');
const dataBuffer = fs.readFileSync('[file-path]');
pdfParse(dataBuffer).then(data => {
  fs.writeFileSync('temp-conversion.md', data.text);
});
" 2>/dev/null || echo "Note: PDF fallback requires pdf-parse npm package. For best results, install pandoc."
```

**Note**: PDF conversion is limited - text-based PDFs only, no images or complex layouts

#### For PowerPoint Documents (.pptx)

**If pandoc available**:
```bash
pandoc -f pptx -t markdown --wrap=preserve "[file-path]" -o temp-conversion.md
```

**If fallback (no pandoc)**:
```bash
# Basic text extraction from PowerPoint XML
# Fallback is limited - just extracts slide text, no formatting
unzip -q -j "[file-path]" "ppt/slides/*.xml" -d temp-pptx/
grep -oh "<a:t>.*</a:t>" temp-pptx/*.xml | sed 's/<[^>]*>//g' > temp-conversion.md
rm -rf temp-pptx/
```

**Note**: PowerPoint fallback is basic - extracts text only, no formatting

#### For CSV Files (.csv)

**No conversion needed** - CSV stays as CSV:
```bash
# Just copy the file - no conversion
cp "[file-path]" temp-conversion.csv
```

**Note**: CSV files are stored as-is with frontmatter added in final step

---

### Step 5: Analyze Structure

Read the converted markdown (or CSV) and analyze:

**For markdown (Word/PDF/PowerPoint)**:

1. **Check for headings**:
   ```bash
   grep "^#" temp-conversion.md
   ```

2. **Classify structure**:
   - **Structured**: Has clear headings (##, ###) that map to sections
   - **Unstructured**: Paragraphs without clear section breaks

3. **Detect potential document type**:
   - Look for keywords in headings/content:
     - "Problem", "Solution", "Requirements" → PRD
     - "Proposal", "Motivation", "Design" → RFC
     - "Context", "Tradeoffs" → One-pager
     - "Introduction", "Goals", "Tenets" → Six-pager

**For CSV**:
- Just note it's tabular data
- No structure mapping needed

---

### Step 6: Ask User for Document Type

**Present findings and ask**:
```
I've converted [filename]. The document appears to be [structured/unstructured] with content about [topic keywords].

What type of document should this be?

Options:
1. PRD - Product Requirement Document
2. RFC - Request for Comments
3. One-pager - Brief proposal
4. Six-pager - Narrative document
5. Custom type - (e.g., "meeting notes", "strategy memo")

Or I can auto-detect based on the content.
```

**If user chooses a template type (PRD, RFC, etc.)**:
- Proceed to Step 7A (Map to Template)

**If user chooses custom type or CSV**:
- Proceed to Step 7B (Flexible Document)

---

### Step 7A: Map to Template

When mapping to a template (PRD, RFC, one-pager, six-pager):

1. **Read the template**:
   ```bash
   cat _templates/{type}.md
   ```

2. **Extract template sections**:
   ```bash
   grep "^##" _templates/{type}.md
   ```

3. **Map content intelligently**:
   - Match headings in converted doc to template sections
   - For unstructured docs: use AI to organize content into template sections
   - Example mapping for PRD:
     - "Problem" or "Background" → Problem Statement
     - "Solution" or "Approach" → Proposed Solution
     - "Goals" or "Metrics" → Success Metrics

4. **Show preview**:
   ```
   Here's how I've mapped the content to the PRD template:

   ✓ Problem Statement (from "Background" section)
   ✓ Proposed Solution (from "Our Approach" section)
   ✓ Success Metrics (from "Goals" section)
   ⚠ Scope - Not found in document (will mark as TBD)
   ⚠ Timeline - Not found in document (will mark as TBD)

   Look good? I can adjust the mapping if needed.
   ```

5. **Gather missing metadata** (see Step 8)

---

### Step 7B: Flexible Document

When creating a flexible document (custom type or CSV):

**For markdown (Word/PDF/PowerPoint)**:

1. **Organize content sensibly**:
   - Keep existing headings if structured
   - Create logical sections if unstructured
   - Clean up formatting issues from conversion

2. **Present preview**:
   ```
   I've organized this as a [custom-type] document with these sections:
   - [Section 1]
   - [Section 2]
   - [Section 3]

   Does this structure work?
   ```

**For CSV**:

1. **Just add frontmatter** - keep CSV data as-is

2. **Present preview**:
   ```
   I'll save this CSV file with metadata in frontmatter.
   The CSV data will remain in its original format.

   Path: teams/{team}/documentation/{filename}.csv
   ```

---

### Step 8: Gather Missing Metadata

Ask for metadata conversationally (similar to create skill):

1. **Title**: "What's the title?" (suggest based on content or filename)

2. **Team**: Default to their team, confirm: "I'll add this to the {team} team folder. Sound good?"

3. **Tags**: "Any tags for discoverability? (e.g., topic keywords)"

4. **Related docs**: "Is this related to any existing documents?" (optional)

5. **Document type**: Already determined in Step 6

6. **Owner**: Default to user (from person doc)

7. **Status**: Default to 'draft'

---

### Step 9: Generate ID and File Path

**Generate ID**:
```bash
# Find existing docs of this type for current year across all team folders
find teams/ -path "*/{type}s/*.md" -o -path "*/documentation/*.md" -type f | \
  xargs grep -h "^id: {type}-2026-" 2>/dev/null | \
  sed "s/id: {type}-2026-//" | \
  sort -n | tail -1
# Next ID: {type}-2026-{max+1}, e.g., prd-2026-003
```

**Determine file path**:

Ask the user where this document should be placed:

[1] teams/{team}/{folder}/ (Default - based on doc type)
[2] teams/{team}/{custom-folder}/ (Specify custom subfolder)
[3] {other-path} (Specify full path)

Note: Creating in global/shared folders (like _templates/) will require approval from global CODEOWNERS.

**Folder mapping defaults**:
- prd, agent-prd → prds/
- rfc → rfcs/
- one-pager → one-pagers/
- six-pager → six-pagers/
- custom types → documentation/
- csv → documentation/

**Title slug**:
```bash
# Convert title to slug
echo "[title]" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g'
```

---

### Step 10: Preview and Confirm

```
I'll create this document from [original-filename]:

ID: prd-2026-003
Title: Product Requirements for Entity Resolution
Type: PRD
Team: intelligence
Path: teams/intelligence/prds/product-requirements-for-entity-resolution.md

Content:
- Converted from Word document
- Mapped to PRD template
- [X sections filled, Y sections marked TBD]

Look good? (yes/adjust title/change location)
```

---

### Step 11: Write the File

**For markdown documents (Word/PDF/PowerPoint)**:

```yaml
---
id: prd-2026-003
title: Product Requirements for Entity Resolution
type: prd
status: draft
team: intelligence
owner: [[teams/intelligence/_people/jane-smith]]
created: 2026-01-06
updated: 2026-01-06
tags: [entity-resolution, data-quality]
related: []
converted_from: entity-resolution-requirements.docx
---

# Product Requirements for Entity Resolution

[Converted and mapped content...]
```

**For CSV files**:

```yaml
---
id: doc-2026-015
title: Customer Data Export
type: data
status: draft
team: intelligence
owner: [[teams/intelligence/_people/jane-smith]]
created: 2026-01-06
updated: 2026-01-06
tags: [data, export]
related: []
original_format: csv
---

# Customer Data Export

[CSV content preserved as-is]
```

**Cleanup**:
```bash
# Remove temp files
rm temp-conversion.md 2>/dev/null
```

---

### Step 12: Confirm and Offer Templatization

```
Converted [filename] to markdown!

Created: [Product Requirements for Entity Resolution](teams/intelligence/prds/product-requirements-for-entity-resolution.md)

Next steps:
- Review the converted content (some formatting may need tweaking)
- Update status to 'review' when ready
- Fill in any TBD sections

[If custom document structure]
This has a nice structure! Want to make this a template so anyone can create [doc-type] documents with this format?
```

**If user wants to templatize** → Same process as create skill (Step 4 in create.md)

---

## Important Notes

1. **Always check for person doc first** - don't proceed without it

2. **Hybrid approach is key** - prefer pandoc, but don't block users if unavailable

3. **Conversion isn't perfect** - set expectations that they may need to review/tweak formatting

4. **Intelligent mapping** - for structured docs, match headings; for unstructured, use content analysis

5. **Preserve original** - note the `converted_from` field in frontmatter

6. **CSV stays CSV** - don't convert to markdown tables, just add frontmatter

7. **Show preview** - always show how content was mapped before writing file

8. **Clean up temp files** - remove conversion artifacts after successful write

9. **Fallback limitations** - be transparent about what fallback conversions can/can't do

10. **Team defaults to user's team** - extracted from their person doc path

11. **File path auto-generated** - users don't need to think about where files go

12. **IDs auto-generated** - sequential numbering per type per year

13. **Templatization optional** - only offer for well-structured custom docs

---

## Conversion Quality Notes

**Pandoc (Best Quality)**:
- ✅ Preserves formatting (bold, italic, links)
- ✅ Converts tables accurately
- ✅ Handles images (references them)
- ✅ Maintains document structure
- ✅ Supports complex layouts

**Mammoth.js Fallback (Word)**:
- ✅ Good basic conversion
- ✅ Preserves bold, italic, links
- ⚠️  Tables may lose formatting
- ⚠️  Images become references
- ❌ Complex layouts simplified

**PDF Fallback**:
- ⚠️  Text extraction only
- ❌ No formatting preserved
- ❌ No images
- ❌ Tables become plain text
- Note: Recommend pandoc for PDFs

**PowerPoint Fallback**:
- ⚠️  Text extraction only
- ❌ No formatting
- ❌ No images
- ❌ Slide structure simplified
- Note: Recommend pandoc for presentations

**CSV**:
- ✅ No conversion needed
- ✅ Perfect preservation
- Note: Keep as-is, just add frontmatter

---

## Example Interactions

### Example 1: Word Document with Pandoc

```
User: "Convert product-spec.docx to a PRD"

Agent:
✓ Checks person doc - found: teams/intelligence/_people/jane-smith.md
✓ Team detected: intelligence
✓ Pandoc found - using high-quality conversion

"Converting product-spec.docx using pandoc..."

[Runs: pandoc -f docx -t markdown --wrap=preserve product-spec.docx -o temp-conversion.md]

"Done! The document is structured with these sections:
- Background
- Requirements
- Technical Approach
- Success Metrics

This looks like a PRD. I can map it to our PRD template. Sound good?"

User: "yes"

Agent:
"Here's how I've mapped the content:

✓ Problem Statement (from 'Background' section)
✓ Proposed Solution (from 'Technical Approach' section)
✓ Success Metrics (from 'Success Metrics' section)
✓ Requirements (from 'Requirements' section → Scope)
⚠ Timeline - Not found (will mark as TBD)

A few quick questions:
1. Title? (Suggestion: 'Product Specification for Entity Resolution')
2. Any tags? (e.g., 'entity-resolution', 'data-quality')
3. Related documents?"

User: [answers]

Agent:
"Creating:

ID: prd-2026-003
Title: Product Specification for Entity Resolution
Team: intelligence
Path: teams/intelligence/prds/product-specification-for-entity-resolution.md

Proceed?"

User: "yes"

Agent:
[Writes file]

"Converted product-spec.docx to markdown!

Created: [Product Specification for Entity Resolution](teams/intelligence/prds/product-specification-for-entity-resolution.md)

I've mapped the content to the PRD template. You may want to:
- Review formatting (tables, images)
- Fill in the Timeline section (marked TBD)
- Update status when ready for review"
```

### Example 2: PDF without Pandoc

```
User: "Import meeting-notes.pdf"

Agent:
✓ Checks person doc - found: teams/ops/_people/brett-jacobs.md
✓ Team detected: ops
✗ Pandoc not found - using fallback

"I'll convert meeting-notes.pdf using the built-in text extractor.

Note: For better quality (preserving formatting, tables, etc.), you can install pandoc from https://pandoc.org/installing.html

Converting..."

[Extracts text from PDF]

"Done! The document contains meeting notes from Jan 5.

What type of document should this be?
1. Custom type (e.g., 'meeting-notes')
2. RFC
3. One-pager
4. Other"

User: "meeting-notes"

Agent:
"I'll create this as a 'meeting-notes' document.

Title? (Suggestion: 'Meeting Notes - Jan 5 2026')"

User: "Team Sync - Jan 5"

Agent:
"Creating:

ID: meeting-notes-2026-001
Title: Team Sync - Jan 5
Type: meeting-notes
Team: ops
Path: teams/ops/documentation/team-sync-jan-5.md

Proceed?"

User: "yes"

Agent:
[Writes file]

"Converted meeting-notes.pdf to markdown!

Created: [Team Sync - Jan 5](teams/ops/documentation/team-sync-jan-5.md)

Note: The text was extracted without formatting. You may want to review and add section headings for better structure.

This is a nice format for meeting notes! Want to make this a template so anyone can create meeting notes with this structure?"
```

### Example 3: CSV File

```
User: "Import customer-data.csv"

Agent:
✓ Checks person doc - found: teams/data/_people/alex-chen.md
✓ Team detected: data

"I'll import customer-data.csv. CSV files are kept in their original format - I'll just add metadata.

Title? (Suggestion: 'Customer Data Export')"

User: "Q4 Customer Data"

Agent:
"Any tags? (e.g., 'data', 'customers', 'q4-2025')"

User: "data, export, q4"

Agent:
"Creating:

ID: doc-2026-015
Title: Q4 Customer Data
Type: data
Team: data
Path: teams/data/documentation/q4-customer-data.csv

The CSV will be preserved exactly as-is.

Proceed?"

User: "yes"

Agent:
[Copies CSV with frontmatter]

"Imported customer-data.csv!

Created: [Q4 Customer Data](teams/data/documentation/q4-customer-data.csv)

The CSV data is preserved in its original format."
```

---

## Conversion Command Reference

### Pandoc Commands

```bash
# Word to Markdown
pandoc -f docx -t markdown --wrap=preserve input.docx -o output.md

# PDF to Markdown
pandoc -f pdf -t markdown --wrap=preserve input.pdf -o output.md

# PowerPoint to Markdown
pandoc -f pptx -t markdown --wrap=preserve input.pptx -o output.md

# Check pandoc version
pandoc --version
```

### Fallback Commands

```bash
# Word: mammoth.js (via npx)
npx -y mammoth input.docx --output-format=markdown > output.md

# PDF: pdf-parse (requires Node.js + npm package)
# Note: More complex - recommend pandoc instead

# PowerPoint: Basic XML text extraction
unzip -q -j input.pptx "ppt/slides/*.xml" -d temp-pptx/
grep -oh "<a:t>.*</a:t>" temp-pptx/*.xml | sed 's/<[^>]*>//g' > output.md
rm -rf temp-pptx/

# CSV: Just copy
cp input.csv output.csv
```
