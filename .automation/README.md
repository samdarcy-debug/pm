# Automation Scripts

This directory contains automation scripts and hooks for the PM Knowledge Repository.

## Directory Structure

```
.automation/
├── scripts/              # Python automation scripts
│   ├── create-metadata.py      # Generates YAML frontmatter for markdown files
│   ├── generate-codeowners.py  # Creates CODEOWNERS from person profiles
│   └── install-gh-cli.py       # Installs GitHub CLI cross-platform
└── husky/                # Git hooks
    └── pre-commit        # Pre-commit hook for validation
```

## Scripts

### create-metadata.py
**Purpose:** Automatically generates YAML frontmatter for markdown content files.

**When it runs:** Pre-commit hook for staged markdown files

**What it does:**
- Extracts metadata from file path (team, document type)
- Gets git history (author, dates)
- Extracts topic from content (using Claude API)
- Generates complete YAML frontmatter (id, title, type, team, owner, dates, topic, tags)
- Skips meta-documents (templates, skills, READMEs, person profiles)

**Requirements:**
- Python 3.x
- `anthropic` package: `pip install anthropic`
- Environment variables:
  - `ANTHROPIC_BASE_URL` (optional): Custom API endpoint
  - `ANTHROPIC_AUTH_TOKEN`: Authentication token

**Usage:**
```bash
# Manually run on a file
python .automation/scripts/create-metadata.py path/to/file.md

# Automatically runs via pre-commit hook
git commit -m "Your message"
```

### generate-codeowners.py
**Purpose:** Generates `.github/CODEOWNERS` file from person profiles.

**When it runs:** Manually when person profiles are updated

**What it does:**
- Scans all person profiles in `teams/*/_people/*.md`
- Extracts GitHub usernames from frontmatter
- Creates hierarchical code ownership rules:
  - Global admins can approve any PR
  - Team members can approve changes to their team's folder
  - Repository admins are defined in the script

**Requirements:**
- Python 3.x
- Standard library only (no external packages)

**Usage:**
```bash
# Generate CODEOWNERS file
python .automation/scripts/generate-codeowners.py

# Commit the generated file
git add .github/CODEOWNERS
git commit -m "Update CODEOWNERS"
```

### install-gh-cli.py
**Purpose:** Cross-platform GitHub CLI installation script.

**When it runs:** During onboarding process

**What it does:**
- Detects OS platform (Windows/macOS/Linux)
- Checks if gh CLI is already installed
- Installs using platform-specific package manager:
  - **Windows**: winget
  - **macOS**: Homebrew
  - **Linux**: apt (with GitHub's official repository)
- Verifies installation success
- Provides fallback instructions if installation fails

**Requirements:**
- Python 3.x
- Platform-specific package managers:
  - Windows: winget (Windows 10 1809+ or Windows 11)
  - macOS: Homebrew
  - Linux: apt (Debian/Ubuntu-based distros)

**Usage:**
```bash
# Run during onboarding (automatic)
python .automation/scripts/install-gh-cli.py

# Or run manually
python .automation/scripts/install-gh-cli.py
```

**Exit codes:**
- `0`: Success (gh CLI installed or already present)
- `1`: Installation failed
- `2`: Platform not supported or package manager not available

## Git Hooks

### pre-commit
**Purpose:** Validates and enriches commits before they're created.

**What it does:**
1. **Metadata Generation**: Runs `create-metadata.py` on staged markdown files
2. **Conflict Detection**: Checks if staged files were modified remotely
3. **Person File Check**: Ensures committer has a person profile

**Location:** `.automation/husky/pre-commit`

**Installation:**
The hook is automatically installed via Husky when you run `npm install`.

**Configuration:**
Husky is configured in `package.json`:
```json
{
  "scripts": {
    "prepare": "husky install .automation/husky"
  }
}
```

## Maintenance

### Adding a New Script

1. Create the script in `.automation/scripts/`
2. Make it executable: `chmod +x .automation/scripts/your-script.py`
3. Document it in this README
4. If it should run automatically, add it to the pre-commit hook
5. If it requires dependencies, document them in the script docstring

### Updating Scripts

When updating automation scripts:
1. Update the script file
2. Test thoroughly on all supported platforms (if applicable)
3. Update this README if behavior changes
4. Update related skills in `.claude/skills/` if they reference the script
5. Update `README.md` if user-facing behavior changes

### Testing

Test scripts before committing:

```bash
# Test create-metadata.py
python .automation/scripts/create-metadata.py teams/ops/documentation/test.md

# Test generate-codeowners.py
python .automation/scripts/generate-codeowners.py
diff .github/CODEOWNERS.expected .github/CODEOWNERS

# Test install-gh-cli.py
python .automation/scripts/install-gh-cli.py
gh --version
```

## Troubleshooting

### create-metadata.py fails
- **Symptom**: Pre-commit hook fails with API error
- **Solution**: Check `ANTHROPIC_AUTH_TOKEN` environment variable is set
- **Workaround**: Manually add YAML frontmatter and commit again

### generate-codeowners.py missing people
- **Symptom**: CODEOWNERS doesn't include everyone
- **Solution**: Ensure all person profiles have `github:` field in frontmatter
- **Check**: Run script with `--verbose` flag for debugging

### install-gh-cli.py fails on Windows
- **Symptom**: "winget is not available"
- **Solution**: Update to Windows 10 (build 1809+) or Windows 11
- **Workaround**: Install gh CLI manually from https://cli.github.com/

### Pre-commit hook is slow
- **Cause**: create-metadata.py makes API calls for topic extraction
- **Expected**: First commit after changes may take 5-10 seconds per new file
- **Note**: Subsequent commits reuse cached metadata

## Environment Variables

Scripts in this directory may use these environment variables:

| Variable | Used By | Required | Description |
|----------|---------|----------|-------------|
| `ANTHROPIC_AUTH_TOKEN` | create-metadata.py | Yes | Authentication for Claude API |
| `ANTHROPIC_BASE_URL` | create-metadata.py | No | Custom API endpoint (defaults to official) |
| `GIT_AUTHOR_NAME` | create-metadata.py | Auto | Git committer name (set by git) |
| `GIT_AUTHOR_EMAIL` | create-metadata.py | Auto | Git committer email (set by git) |

## Related Documentation

- [Repository README](../README.md) - Getting started guide
- [Onboarding Skill](../.claude/skills/onboard.md) - Uses install-gh-cli.py
- [Create Doc Skill](../.claude/skills/create-doc.md) - Creates files processed by create-metadata.py
- [CLAUDE.md](../CLAUDE.md) - Repository context for Claude Code
