# Create Skill

**Description**: Helps PMs create new skills for the PM knowledge repository through a hybrid approach - combining interviews with optional example documents. Supports document templates, workflow automation, and hybrid skills. All generated skills require Product Ops review via PR.

**Triggers (Strong)**: Use this skill when the user explicitly requests:
- "Create a skill for [X]"
- "Make a skill for [X]"
- "Build a skill to [X]"
- "Generate a skill for [X]"
- "I want to create a new skill"

**Triggers (Conditional)**: May use this skill if context suggests:
- "Templatize [doc-type]" - If user wants to create a reusable template from an existing document
- "Automate [process]" - If user wants to create a workflow skill
- "How do I create a skill?" - Explain + offer to help create one

**Do NOT Trigger** for:
- User wants to create a document (use create-doc skill)
- User is just asking questions about existing skills
- User wants to modify an existing skill (help them edit directly)
- User is onboarding for the first time (use onboard skill)

---

## Instructions

You are helping a PM create a new skill for the PM knowledge repository. Your goal is to guide them through a hybrid creation process that combines interviews with optional example documents to generate high-quality skill and template files.

**Key Principles**:
1. **Always interview** - Understand purpose, triggers, and structure through conversation
2. **Always offer examples** - Ask for example documents (optional but encouraged)
3. **Hybrid generation** - Combine interview answers with patterns extracted from examples
4. **Three skill types** - Support document templates, workflow automation, and hybrid skills
5. **PR required** - All generated skills must go through Product Ops review

---

### Step 1: Interview the PM

Start with a friendly introduction and then interview the PM to understand their skill requirements.

Say: "I'll help you create a new skill! Let me ask a few questions to understand what you need."

**Ask these questions conversationally** (not as a form):

**Question 1: Purpose**
"What should this skill do? What problem does it solve?"

Wait for answer, then continue.

**Question 2: Skill Type**
"Is this for:
- Creating documents (like PRDs, reports, etc.)
- Automating a workflow or process
- Both (document creation with automation)"

Wait for answer. Based on their response, you'll know what to generate later.

**Question 3: Triggers**
"What phrases should trigger this skill? What would users say to activate it?"

Examples: "create a post-mortem", "review PR for compliance", "synthesize weekly reports"

Wait for answer.

**Question 4: Key Elements**

*For document skills*: "What sections or structure should these documents have?"

*For workflow skills*: "What are the main steps in this process? Walk me through it."

*For hybrid skills*: "Tell me about both the document structure and the workflow steps."

Wait for detailed answer. Take notes on their description.

**Question 5: Tools Needed** (for workflow skills)
"What tools or commands will this skill need to use?"

Examples: Bash, Read, Write, Edit, Grep, Glob, gh CLI, git commands, etc.

---

### Step 2: Request Example Documents

Always ask for examples, even if you don't think they'll have any:

Say: "Do you have any example documents I can learn from? This helps me create a better skill. If you have:
- An example document of the type you want to create
- Documentation showing the workflow
- Reference materials

Please share the file path(s). If you don't have examples yet, that's totally fine - I can work from your description."

Wait for response.

**If they provide path(s)**:
- Read each file they mention
- Note the file paths for later reference
- Continue to Step 3

**If no examples**:
- That's okay! Continue to Step 4 with interview answers only

---

### Step 3: Extract & Analyze Examples (If Provided)

If the PM provided example document(s), read and analyze them:

**For document examples**:

1. **Read the file(s)**:
```bash
cat [file-path]
```

2. **Extract structure**:
   - **Frontmatter fields**: Note field names, types, and patterns
   - **Section headings**: Extract all `##` level headings
   - **Content patterns**: Identify lists, tables, code blocks, writing style
   - **Document flow**: How sections connect and build on each other

3. **Combine with interview**: Merge the structure from the example with what the PM described. If they mentioned sections not in the example, include those too.

**For workflow examples** (checklists, process docs, etc.):

1. **Read the file(s)**:
```bash
cat [file-path]
```

2. **Extract workflow patterns**:
   - **Commands used**: Any bash commands, git operations, tools mentioned
   - **Decision points**: If/then logic, branching, conditionals
   - **Error handling**: How errors are handled or prevented
   - **Steps sequence**: The order of operations

3. **Combine with interview**: Merge workflow patterns from examples with PM's description

**Document your findings** - You'll use this analysis in Step 4.

---

### Step 4: Generate Skill Files

Now generate the appropriate files based on skill type. Use the analysis from Steps 1-3.

#### For Document Skills (Template + Skill)

**4A: Generate Template File**

Create `_templates/{skill-name}.md`:

```markdown
---
id:                         # Format: {type}-{YYYY}-{NNN}
title:
type: {doc-type}
status: draft               # draft | review | approved | archived
team:
owner:                      # Wiki-link to person
created:
updated:
tags: []
related: []

# {Any custom fields from examples or interview}
{field-name}:              # {description}
---

# {Title}

## {Section 1 Heading}

{Placeholder content with guidance on what goes here}

## {Section 2 Heading}

{Placeholder content}

## {Continue with all sections...}
```

**Guidelines**:
- Use field names from example docs OR standard fields if no example
- Include section headings from example OR PM's described structure
- Add helpful placeholder content explaining what each section should contain
- Include comments for any custom or non-obvious fields

**4B: Generate Skill File for Document Creation**

Create `.claude/skills/{skill-name}.md`:

Use this structure (following the _skill-template.md format):

```markdown
# Create {Doc Type}

**Description**: {1-2 sentence description from interview}

**Triggers (Strong)**:
- "{trigger phrase 1 from interview}"
- "{trigger phrase 2}"
- "{alternative phrase}"

**Triggers (Conditional)**:
- "create a document about {topic}" - Check if user means this doc type

**Do NOT Trigger**:
- User wants a different doc type
- User is just asking about the template
- User wants to search for existing docs

---

## Instructions

You are helping create a {doc-type} document for the PM knowledge repository.

### Step 1: Check for Person Doc

[Standard person doc check - copy from create-doc.md]

### Step 2: Gather Metadata

Ask conversationally:
- Title
- Team (default to user's team)
- Tags
- Related docs
- {Any custom fields from template}

### Step 3: Gather Content

{Instructions based on template structure}

For each major section:
- {Section name}: Ask "{question to elicit content}"
- {Section name}: Ask "{question to elicit content}"

### Step 4: Generate ID

```bash
# Find existing docs of this type across all team folders
find teams/ -path "*/{pluralized-type}/*.md" -o -path "*/documentation/*.md" -type f | \
  xargs grep -h "^id: {type}-2026-" 2>/dev/null | \
  sed "s/id: {type}-2026-//" | \
  sort -n | tail -1
# Next ID: {type}-2026-{max+1}
```

### Step 5: Determine File Path

Ask the user where this document should be placed:

[1] teams/{team}/{pluralized-type}/ (Default - team folder)
[2] teams/{team}/{custom-folder}/ (Specify custom subfolder)
[3] {other-path} (Specify full path)

Note: Creating in global/shared folders (like _templates/) will require approval from global CODEOWNERS.

**Default suggestion**: teams/{team}/{pluralized-type}/

### Step 6: Preview & Confirm

Show user the plan, confirm before creating.

### Step 7: Write File

Use Write tool with full template structure filled in.

### Step 8: Confirm Creation

Provide file path link and next steps.

---

## Important Notes

- {Any special considerations from interview}
- {Document best practices}

---

## Example Interactions

{Generate 2-3 examples based on interview and template structure}
```

---

#### For Workflow Skills (Skill Only)

**Generate Skill File**

Create `.claude/skills/{skill-name}.md`:

```markdown
# {Skill Name}

**Description**: {Description from interview}

**Triggers (Strong)**:
- "{trigger phrase 1}"
- "{trigger phrase 2}"

**Triggers (Conditional)**:
- "{conditional trigger}"

**Do NOT Trigger**:
- {Anti-patterns}

---

## Instructions

{Purpose statement from interview}

### Step 1: {First Step from Interview}

{Detailed instructions}

```bash
# Commands from examples or interview
{commands}
```

{Continue with all workflow steps...}

### Step N: {Final Step}

{Completion instructions}

---

## Important Notes

- **{Tool}: {How to use it}
- **{Error handling}: {How to handle errors}
- **{Best practice}: {From examples or interview}

---

## Example Interactions

{Generate examples based on workflow description}
```

---

#### For Hybrid Skills (Template + Workflow Skill)

Generate both:
1. Template file (as in 4A)
2. Skill file that combines document creation logic with workflow automation (merge approaches from 4B and workflow skills)

---

### Step 5: Preview & Confirm

Show the PM what you're about to create:

"I'll create these files:

**{For document skills}**:
- Template: `_templates/{skill-name}.md`
  - Frontmatter fields: {list key fields}
  - Sections: {list main sections}

- Skill: `.claude/skills/{skill-name}.md`
  - Triggers: {list triggers}
  - {Purpose summary}

**{For workflow skills}**:
- Skill: `.claude/skills/{skill-name}.md`
  - Triggers: {list triggers}
  - Steps: {list main workflow steps}

The skill will be submitted as a PR for Product Ops review before becoming available.

Shall I proceed? (yes/adjust)"

**If user says adjust**: Ask what they want to change, then regenerate.

**If user says yes**: Continue to Step 6.

---

### Step 6: Create Branch & Commit

Create a new branch and commit the generated files.

**Determine branch name**:
```
add-{skill-name}-skill
```

Convert skill name to kebab-case (e.g., "post-mortem" → "add-post-mortem-skill")

**Create branch**:
```bash
git checkout -b add-{skill-name}-skill
```

**Stage files**:
```bash
# For document skills
git add _templates/{skill-name}.md .claude/skills/{skill-name}.md

# For workflow skills
git add .claude/skills/{skill-name}.md
```

**Commit**:
```bash
git commit -m "$(cat <<'EOF'
feat: add {skill-name} skill

{Brief description of what this skill does}

Skill type: {document | workflow | hybrid}
Created through create-skill workflow.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

### Step 7: Push & Create PR

**Push branch**:
```bash
git push -u origin add-{skill-name}-skill
```

**Create PR**:

Use the gh CLI to create the PR:

```bash
# Detect gh CLI path
gh --version 2>/dev/null || "/c/Program Files/GitHub CLI/gh.exe" --version 2>/dev/null
```

```bash
gh pr create --base master --head add-{skill-name}-skill \
  --title "feat: add {skill-name} skill" \
  --body "$(cat <<'EOF'
## Summary

New skill: `{skill-name}` - {brief description}

## Purpose

{What this skill does and why it's useful - from interview}

## Skill Type

{document-creation | workflow-automation | hybrid}

## Usage

Users can trigger this skill by saying:
- "{trigger 1}"
- "{trigger 2}"
- "{trigger 3}"

## Files Created

{List files created}

## Based On

{If examples were used}
- Example document(s): {file paths}
- Interview with: {PM name}

{If no examples}
- Interview-based generation
- PM description: {brief summary}

## Review Needed

Product Ops team: Please review this skill for:
- [ ] Trigger phrases are clear and don't conflict with existing skills
- [ ] Instructions are comprehensive and easy to follow
- [ ] Template structure makes sense (if applicable)
- [ ] Proper error handling is included
- [ ] Example interactions are helpful
- [ ] Documentation is complete

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

**If gh CLI not found**:
Tell user: "GitHub CLI not found. Please install it or create the PR manually at the URL shown above."

---

### Step 8: Confirm Success

Tell the user:

"✅ Created PR #{number}: [PR URL]

Your skill has been submitted for Product Ops review. Here's what happens next:

1. **Product Ops reviews** - They'll check the skill for quality and conflicts
2. **Feedback or approval** - They may request changes or approve as-is
3. **Merge** - Once approved, the skill becomes available to everyone
4. **Usage** - PMs can then use your skill by saying: '{main trigger phrase}'

You can view the PR here: [PR URL]

Want to create another skill?"

---

## Important Notes

- **Always interview first** - Don't skip the interview even if examples are provided
- **Examples are optional** - Generate from interview if no examples available
- **Combine sources** - Merge interview + examples for best results
- **Three skill types** - Detect whether document, workflow, or hybrid
- **PR required** - Never push directly to main, always create PR
- **GitHub CLI required** - For PR creation (help install if missing)
- **Quality over speed** - Take time to generate comprehensive, clear skills
- **Follow conventions** - Use existing skills as models for structure
- **Helpful placeholders** - Template placeholders should guide users
- **Clear triggers** - Triggers should be unambiguous and not conflict
- **Test-driven examples** - Example interactions should show real usage

---

## Example Interactions

### Example 1: Document Skill with Example

```
User: "Create a skill for post-mortems"

Agent: "I'll help you create a skill for post-mortems. Let me ask a few questions:

1. What should this skill do? What problem does it solve?"

User: "It should help engineers write post-mortems after incidents"

Agent: "2. Is this for creating documents, automating a workflow, or both?"

User: "Creating documents"

Agent: "3. What phrases should trigger this skill?"

User: "create a post-mortem, write a post-mortem, incident post-mortem"

Agent: "4. What sections should post-mortem documents have?"

User: "Timeline of events, root cause analysis, impact assessment, action items"

Agent: "Great! Do you have any example post-mortem documents I can learn from? This helps me create a better skill."

User: "Yes, teams/platform/documentation/postmortem-search-outage.md"

Agent: [Reads example]
"Perfect! I can see your example has:
- Timeline section with timestamps
- Root cause with technical details
- Impact with metrics
- Action items with owners

I'll combine this structure with the sections you mentioned. Let me generate the files."

[Generates template with sections: Incident Overview, Timeline, Root Cause, Impact Assessment, Action Items, Lessons Learned]

[Generates skill file with triggers and instructions]

"I'll create these files:

- Template: `_templates/post-mortem.md`
  - Frontmatter: id, title, type, incident_date, severity
  - Sections: Incident Overview, Timeline, Root Cause, Impact, Action Items, Lessons Learned

- Skill: `.claude/skills/post-mortem.md`
  - Triggers: create/write/document a post-mortem
  - Guides users through incident documentation

Shall I proceed?"

User: "Yes"

Agent: [Creates branch, commits, pushes, creates PR]

"✅ Created PR #42: https://git.zoominfo.com/dozi/pm/pull/42

Your post-mortem skill has been submitted for Product Ops review!"
```

### Example 2: Workflow Skill without Examples

```
User: "Create a skill to help me review PRs for compliance"

Agent: "I'll help you create a PR compliance review skill. Let me ask a few questions:

1. What should this skill do?"

User: "It should check PRs against our compliance requirements - proper reviewers, commit format, CODEOWNERS updates, test passing"

Agent: "2. What phrases should trigger this skill?"

User: "review PR, check PR compliance, validate pull request"

Agent: "3. Walk me through the workflow steps - what should it check and in what order?"

User: "First check if required reviewers are assigned, then verify commit messages follow our format, then check if CODEOWNERS was updated if needed, finally confirm tests passed"

Agent: "4. What tools will this need?"

User: "gh CLI for PR info, git commands for commit messages, grep for CODEOWNERS"

Agent: "Perfect! Do you have any example documents I can learn from - like a compliance checklist?"

User: "No, just what I described"

Agent: "No problem! I'll create a workflow skill based on your description."

[Generates skill file with 4 main steps matching the described workflow]

"I'll create:

- Skill: `.claude/skills/pr-compliance-review.md`
  - Triggers: review/check/validate PR
  - Steps:
    1. Check required reviewers (gh pr view)
    2. Verify commit message format (git log)
    3. Check CODEOWNERS updates (git diff)
    4. Confirm tests passed (gh pr checks)
  - Tools: gh, git, grep

Shall I proceed?"

User: "Yes"

Agent: [Creates branch, commits, pushes, creates PR]

"✅ Created PR #43: https://git.zoominfo.com/dozi/pm/pull/43"
```

### Example 3: Hybrid Skill with Examples

```
User: "Create a skill for weekly team reports that pulls data from GitHub"

Agent: "I'll help you create a weekly report skill with GitHub automation. Let me ask a few questions:

1. What should this skill do?"

User: "It should create a weekly report document with our standard sections, but also automatically pull PR and issue data from GitHub to populate the metrics section"

Agent: "2. What phrases should trigger this skill?"

User: "create weekly report, generate weekly report"

Agent: "3. What sections should the report have?"

User: "Executive Summary, Accomplishments, Metrics, Blockers, Next Week Plan"

Agent: "4. What GitHub data should it pull?"

User: "PRs merged this week, issues closed, new issues opened"

Agent: "Perfect! Do you have example weekly reports?"

User: "Yes, teams/intelligence/weekly-reports/context-engineering-weekly-report-2025-12-27.md"

Agent: [Reads example]
"Great! Your example shows a nice structure. I'll create:
- A template with your 5 sections
- A skill that creates the document AND pulls GitHub metrics

The skill will use gh CLI to fetch:
- PRs merged (gh pr list --state merged)
- Issues closed (gh issue list --state closed)
- New issues (gh issue list --state open)

And populate the Metrics section automatically.

Shall I proceed?"

User: "Yes"

Agent: [Generates template + hybrid skill with both document creation and automation]
Agent: [Creates PR]

"✅ Created PR #44: https://git.zoominfo.com/dozi/pm/pull/44"
```

---

## Error Handling

### Common Errors

**Error 1: GitHub CLI not found**
- Cause: gh CLI not installed or not in PATH
- Solution: Offer to install using `.automation/scripts/install-gh-cli.py`
- User message: "GitHub CLI is required for creating PRs. Want me to install it?"

**Error 2: Example file not found**
- Cause: User provided invalid file path
- Solution: Ask user to verify path or continue without examples
- User message: "I couldn't find that file. Can you double-check the path? Or we can continue without examples."

**Error 3: Branch already exists**
- Cause: Branch name collision from previous attempt
- Solution: Suggest different branch name or delete old branch
- User message: "A branch with that name already exists. Delete it or want me to use a different name?"

**Error 4: Interview answers too vague**
- Cause: PM didn't provide enough detail
- Solution: Ask follow-up clarifying questions
- Example: "Can you tell me more about {vague area}? What specifically should happen?"

**Error 5: Conflicting trigger phrases**
- Cause: Triggers overlap with existing skills
- Solution: Suggest alternative trigger phrases
- User message: "That trigger might conflict with {existing-skill}. How about: {alternative}?"

---

## Related Skills

- **create-doc**: Use this for creating individual documents, not skills
- **onboard**: New users should onboard before creating skills
- **search-repo**: Use to find existing skills before creating new ones

---

## Validation Checklist

Before committing, verify:

**Template file** (if generated):
- [ ] Valid YAML frontmatter
- [ ] All required fields present
- [ ] Placeholders are clear and helpful
- [ ] Section structure makes logical sense
- [ ] Comments explain non-obvious fields

**Skill file**:
- [ ] Has Description section
- [ ] Has Triggers (Strong, Conditional, Do NOT Trigger)
- [ ] Has Instructions with numbered steps
- [ ] Has Important Notes section
- [ ] Has Example Interactions (2-3 examples)
- [ ] Markdown syntax is valid
- [ ] No placeholder text left in (replace all {})

**PR**:
- [ ] Branch name follows convention
- [ ] Commit message is descriptive
- [ ] PR body has all required sections
- [ ] Requests Product Ops review
- [ ] Links to example docs if used
