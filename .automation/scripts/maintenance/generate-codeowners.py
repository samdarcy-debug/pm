#!/usr/bin/env python3
"""
Generate .github/CODEOWNERS file from person profiles.

This script scans all teams/*/people/*.md files, extracts team and github
information from YAML frontmatter, and generates a hierarchical CODEOWNERS file.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Global admins who can approve anything
GLOBAL_ADMINS = [
    "adam-smith",
    "brett-jacobs",
    "daniel-kong",
    "kristin-gandini",
    "dominik-facher",
    "ken-elwell",
]

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}

    frontmatter_text = match.group(1)
    frontmatter = {}

    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Remove quotes and comments
            value = re.sub(r'#.*$', '', value).strip()
            value = value.strip('"\'')
            if value:
                frontmatter[key] = value

    return frontmatter

def scan_person_profiles(repo_root):
    """Scan all person profiles and extract team/github mappings."""
    teams = defaultdict(list)

    # Find all person markdown files
    people_pattern = Path(repo_root) / "teams" / "*" / "_people" / "*.md"

    for person_file in Path(repo_root).glob("teams/*/_people/*.md"):
        try:
            with open(person_file, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter = parse_frontmatter(content)
            team = frontmatter.get('team')
            github = frontmatter.get('github')

            if team and github:
                teams[team].append(github)
        except Exception as e:
            print(f"Warning: Error reading {person_file}: {e}")

    return teams

def generate_codeowners(teams):
    """Generate CODEOWNERS file content."""
    lines = []
    lines.append("# CODEOWNERS - Auto-generated from person profiles")
    lines.append("# DO NOT EDIT MANUALLY - Run .automation/scripts/maintenance/generate-codeowners.py to update")
    lines.append("")
    lines.append("# Global admins - can approve anything in the repo")
    admin_line = "* " + " ".join(f"@{admin}" for admin in GLOBAL_ADMINS)
    lines.append(admin_line)
    lines.append("")

    if teams:
        lines.append("# Team-specific ownership")
        lines.append("# Team members can approve changes to their team's folder")
        lines.append("")

        for team in sorted(teams.keys()):
            members = sorted(teams[team])
            member_line = " ".join(f"@{member}" for member in members)
            lines.append(f"/teams/{team}/** {member_line}")

    return "\n".join(lines) + "\n"

def main():
    """Main entry point."""
    # Get repository root (go up from .automation/scripts/maintenance/ to root)
    script_dir = Path(__file__).parent  # .automation/scripts/maintenance/
    repo_root = script_dir.parent.parent.parent  # Go up 3 levels to repo root

    print("Scanning person profiles...")
    teams = scan_person_profiles(repo_root)

    print(f"Found {len(teams)} teams with GitHub usernames:")
    for team, members in sorted(teams.items()):
        print(f"  {team}: {', '.join(sorted(members))}")

    print("\nGenerating CODEOWNERS file...")
    codeowners_content = generate_codeowners(teams)

    codeowners_path = repo_root / ".github" / "CODEOWNERS"
    codeowners_path.parent.mkdir(parents=True, exist_ok=True)

    with open(codeowners_path, 'w', encoding='utf-8') as f:
        f.write(codeowners_content)

    print(f"CODEOWNERS file generated at {codeowners_path}")

if __name__ == "__main__":
    main()
