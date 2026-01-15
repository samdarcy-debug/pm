# Onboard to PM Repository

**Description**: Quick onboarding for first-time users. Creates your person document with essential metadata. Takes ~1 minute.

**Trigger**: Use this skill ONLY for first-time onboarding when users need to create their person document.

**Strong triggers** (always use this skill):
- "onboard me" / "run onboarding" / "onboard"
- "create my person doc" / "create my person document" / "create my profile"
- "set me up" / "first time setup"
- "I'm new here"

**Conditional trigger** (check first):
- "help me get started" - ONLY use this skill if the user doesn't have a person doc yet. First check:
  1. Run: `git config user.name` to get their name
  2. Search: `find teams/ -path "*/people/*.md" -exec grep -l "title: {name}" {} \;`
  3. If person doc exists, they're not new - ask what they need help with instead
  4. If no person doc, proceed with onboarding

**Do NOT trigger** for:
- General help requests ("help", "what can you do")
- Document creation ("create a PRD")
- Search queries ("find documents about X")

---

## Instructions

You are helping a new PM get set up in the knowledge repository. Your goal is to create their person document quickly (~1 minute for essentials) with optional profile sections if they want.

### Step 1: Check if already onboarded

Run this command to see if person docs already exist:

```bash
find teams/ -path "*/people/*.md" -type f 2>/dev/null || echo "No person docs found yet"
```

If person docs exist, ask: "What's your name?"

Then search for their doc:
```bash
find teams/ -path "*/people/*.md" -type f -exec grep -l "title: {Their Name}" {} \; 2>/dev/null
```

If found, say: "You're already set up! Your person doc is at [path]. Need help with something else?"

If not found, continue to Step 2.

### Step 2: Install and authenticate GitHub CLI

GitHub CLI is required for creating pull requests. We need to install it and authenticate to ZoomInfo's enterprise GitHub.

**2.1: Detect GitHub CLI**

Try `gh` command first, then check common Windows paths:
- `/c/Program Files/GitHub CLI/gh.exe`
- `$LOCALAPPDATA/Programs/GitHub CLI/gh.exe`

```bash
gh --version 2>/dev/null || "/c/Program Files/GitHub CLI/gh.exe" --version 2>/dev/null
```

**If GitHub CLI is found:**
- Continue to Step 2.2 (authentication)

**If GitHub CLI is NOT found:**
- Say: "GitHub CLI is not installed. Installing now..."
- Run: `python .automation/scripts/install-gh-cli.py`
- If installation succeeds: Continue to Step 2.2
- If installation fails with permission errors: Say "⚠️  GitHub CLI installation requires administrator permissions. Please run the installation command shown above in an elevated terminal, then say 'continue' when ready."
  - Wait for user to say "continue"
  - Verify with: `gh --version`
- If installation fails for other reasons: Say "⚠️  Automatic installation failed. You can install GitHub CLI later from https://cli.github.com/" and continue to Step 3 (don't block onboarding)

**2.2: Authenticate to enterprise GitHub**

Check authentication status (remember to use the correct gh command path from detection):

```bash
gh auth status --hostname git.zoominfo.com
# or if gh not in PATH:
"/c/Program Files/GitHub CLI/gh.exe" auth status --hostname git.zoominfo.com
```

**If already authenticated:**
- Say: "✅ GitHub CLI is authenticated. You're all set!"
- Continue to Step 3

**If not authenticated:**
- Say: "Let's authenticate to ZoomInfo's GitHub. A browser window will open for you to authorize."
- Run authentication command:
  ```bash
  gh auth login --hostname git.zoominfo.com --web --git-protocol https
  ```
- Immediately open browser (ensures it opens for all users):
  ```bash
  start https://git.zoominfo.com/login/device  # Windows
  # open https://git.zoominfo.com/login/device   # macOS
  # xdg-open https://git.zoominfo.com/login/device  # Linux
  ```
- Say: "A browser window should have opened to https://git.zoominfo.com/login/device. Please enter the code shown in the terminal and authorize the GitHub CLI."
- Wait for them to complete authentication
- Verify: `gh auth status --hostname git.zoominfo.com`
- If successful: Say "✅ Authentication successful! You can now create pull requests."
- If failed: Say "⚠️  Authentication didn't complete. You can try again later with: `gh auth login --hostname git.zoominfo.com --web`" and continue to Step 2.5

Continue to Step 2.5

### Step 2.5: Install Git Hooks

Git hooks automate repository tasks. We'll install a pre-commit hook that automatically regenerates CODEOWNERS when person profiles change.

**2.5.1: Run the setup script**

Say: "Setting up development environment (git hooks)..."

```bash
bash .automation/scripts/setup-dev-environment.sh
```

**If setup succeeds:**
- Say: "✅ Development environment configured! Git hooks are installed."
- Say: "ℹ️  When you update person profiles, CODEOWNERS will auto-regenerate on commit."

**If setup fails:**
- Say: "⚠️  Development environment setup had issues, but you can continue."
- Say: "You may need to manually regenerate CODEOWNERS after creating your person profile."
- Say: "Run: `python .automation/scripts/maintenance/generate-codeowners.py`"

Continue to Step 3

### Step 3: Auto-detect from git

Get their info from git config:

```bash
git config user.name
```

```bash
git config user.email
```

Derive Slack handle from email:
- If email is `first.last@zoominfo.com`, Slack is `@first.last`
- If email format is different, ask them for Slack handle

Show the user:

"Hi! Let's get you set up.

You need a person document so the system knows who you are, what team and domain you own. This provides context for Claude when creating documents.

From your git config:
✓ Name: [name]
✓ Email: [email]
✓ Slack: [handle]

Is this correct?"

If they say no or make corrections, ask for the correct information.

If git config is empty, ask directly:
- "What's your name?"
- "What's your email?"
- "What's your Slack handle?"

### Step 4: Team and sub-team selection

Ask: "Which DAI-level team are you on?

1. GTM Studio (flat structure)
2. GTM Workspace (flat structure)
3. Intelligence (has sub-teams)
4. Platform (has sub-teams)
5. Data (has sub-teams)
6. Ops (has sub-teams)
7. Leadership"

Convert their answer to folder name:
- "GTM Studio" → `gtm-studio`
- "GTM Workspace" → `gtm-workspace`
- "Intelligence" → `intelligence`
- "Platform" → `platform`
- "Data" → `data`
- "Ops" → `ops`
- "Leadership" → `leadership`

**For hierarchical teams (Intelligence, Platform, Data, Ops), ask for sub-team:**

If they selected Intelligence, ask: "Which Intelligence sub-team?
1. Context Engineering
2. MCP
3. Semantic Data
4. Intelligence Executive Team"

Convert to folder names:
- "Context Engineering" → `context-engineering`
- "MCP" → `mcp`
- "Semantic Data" → `semantic-data`
- "Intelligence Executive Team" → `intelligence-executive-team`

If they selected Platform, ask: "Which Platform sub-team?
1. Admin
2. Automation
3. Data Platform
4. Integrations
5. ZIM"

Convert to folder names:
- "Admin" → `admin`
- "Automation" → `automation`
- "Data Platform" → `data-platform`
- "Integrations" → `integrations`
- "ZIM" → `zim`

If they selected Data, ask: "Which Data sub-team?
1. Core Data
2. Data Executive Team"

Convert to folder names:
- "Core Data" → `core-data`
- "Data Executive Team" → `data-executive-team`

If they selected Ops, ask: "Which Ops sub-team?
1. Product Operations
2. Business Intelligence
3. Product Marketing"

Convert to folder names:
- "Product Operations" → `product-ops`
- "Business Intelligence" → `business-intelligence`
- "Product Marketing" → `product-marketing`

**For flat teams (GTM Studio, GTM Workspace, Leadership), skip sub-team selection.**

### Step 5: Role

Ask: "What is your role or area of specialization?"

Don't provide examples. Just ask directly and accept their answer.

### Step 6: Create person doc

Generate:
- **ID**: `person-{name-slug}` (e.g., "Brett Jacobs" → `person-brett-jacobs`)
- **Path**: `teams/{team-slug}/_people/{name-slug}.md` (e.g., `teams/data/_people/brett-jacobs.md`)
- **Dates**: Use today's date in YYYY-MM-DD format for both created and updated

Write the file with this structure:

```markdown
---
id: person-{slug}
title: {Full Name}
type: person
team: {team-slug}
subteam: {subteam-slug}  # Only include for hierarchical teams; omit for flat teams
role: {role}
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags: []
---

# {Full Name}

## Role

{role}

## Contact

- **Slack**: {slack}
- **Email**: {email}

## Documents I Own

_(Auto-populated as you create documents)_
```

After creating the file, continue to Step 7.

### Step 7: Offer optional sections

Say:

"✅ Done! Your person doc is at: teams/{team-slug}/_people/{name-slug}.md

**What's included:**
- Name, team, domain
- Contact info
- Document ownership (auto-populated)

**Optional:** Want to add more about yourself? It can help teammates understand how to work with you. Just brief answers - takes ~2 minutes.

Would you like to add optional profile sections? (yes/skip)"

If they say skip:
"All set! You can ask me to update your person doc anytime.

Next steps: You can now create PRDs, RFCs, and other documents. Just ask me naturally - like 'create a PRD for [feature]'."

If they say yes, continue to Step 8.

### Step 8: Fill optional sections (if they say yes)

Say: "Great! I'll keep this quick. Just brief answers.

**1. About you (1-2 sentences)**

Your background and expertise.

Example: 'I've been a PM for 8 years, focused on data products and analytics. Strong background in SQL and data modeling.'"

Wait for their answer, then append to the person doc:

```markdown

## About

{their answer}
```

Then ask:

"**2. Current focus (1 sentence)**

What you're working on right now.

Example: 'Leading the company data unification initiative and ZI Graph evolution.'"

Wait for their answer, then append:

```markdown

## Current Focus

{their answer}
```

Then ask:

"**3. Communication preferences**

How should people reach you and when?

Example: 'Slack DM is best. I respond within a few hours during work hours (9am-6pm ET). For urgent matters, text me.'"

Wait for their answer, then append:

```markdown

## Working With Me

### Communication Preferences

{their answer}
```

Then ask:

"**4. Collaboration style (1-2 sentences)**

How do you like to work with others?

Example: 'I prefer written docs before meetings so I can come prepared. I like to debate ideas openly and value direct feedback.'"

Wait for their answer, then append:

```markdown

### Collaboration Style

{their answer}
```

Finally, say:

"✅ Done! Your person doc is complete at: teams/{team-slug}/people/{name-slug}.md

Next steps: You can now create PRDs, RFCs, and other documents. Just ask me naturally - like 'create a PRD for [feature]'."

---

## Important Notes

- Team folders already exist (gtm-studio, copilot-workspace, intelligence, platform, data, ops)
- Just create the person doc in the correct team's people/ folder
- Use today's date for both created and updated fields
- Person doc is primarily metadata for Claude to understand who the user is
- Optional sections are truly optional - most users will skip them
- Be conversational and friendly throughout
- Keep it fast - essentials should take ~1 minute
