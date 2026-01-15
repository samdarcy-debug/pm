#!/usr/bin/env python3
"""
Validate person profiles have all required fields.

This script scans all teams/*/_people/*.md files and checks that they have
all required YAML frontmatter fields for CODEOWNERS generation.
"""

import os
import re
import sys
from pathlib import Path

# Required fields for person profiles
REQUIRED_FIELDS = ["id", "title", "type", "team", "domain", "github", "created", "updated"]

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
            frontmatter[key] = value  # Keep even if empty to detect missing values

    return frontmatter

def validate_person_profile(file_path):
    """Validate a single person profile and return list of errors."""
    errors = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"Could not read file: {e}"]

    frontmatter = parse_frontmatter(content)

    if not frontmatter:
        return ["No YAML frontmatter found"]

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"Missing field: {field}")
        elif not frontmatter[field]:
            errors.append(f"Empty field: {field}")

    # Validate specific fields
    if "type" in frontmatter and frontmatter["type"] != "person":
        errors.append(f"Invalid type: {frontmatter['type']} (should be 'person')")

    if "id" in frontmatter and frontmatter["id"]:
        if not frontmatter["id"].startswith("person-"):
            errors.append(f"Invalid id format: {frontmatter['id']} (should start with 'person-')")

    if "github" in frontmatter and frontmatter["github"]:
        # Validate GitHub username format (alphanumeric + hyphens)
        if not re.match(r'^[a-z0-9-]+$', frontmatter["github"]):
            errors.append(f"Invalid GitHub username format: {frontmatter['github']} (should be lowercase alphanumeric + hyphens)")

    return errors

def main():
    """Main entry point."""
    # Get repository root (go up from .automation/scripts/maintenance/ to root)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent.parent

    print("Validating person profiles...")
    print(f"Repository root: {repo_root}")
    print()

    # Find all person profile files
    person_files = list(Path(repo_root).glob("teams/*/_people/*.md"))

    if not person_files:
        print("[WARNING] No person profile files found in teams/*/_people/*.md")
        print("          Check that person profiles exist and are in the correct location.")
        return 1

    print(f"Found {len(person_files)} person profile(s)")
    print()

    has_errors = False
    valid_count = 0

    for person_file in sorted(person_files):
        relative_path = person_file.relative_to(repo_root)
        errors = validate_person_profile(person_file)

        if errors:
            has_errors = True
            print(f"[ERROR] {relative_path}")
            for error in errors:
                print(f"   - {error}")
            print()
        else:
            valid_count += 1
            print(f"[OK] {relative_path}")

    print()
    print("=" * 60)
    print(f"Validation complete: {valid_count} valid, {len(person_files) - valid_count} with errors")

    if has_errors:
        print()
        print("[WARNING] Some person profiles have validation errors.")
        print("          Fix the errors above and run this script again.")
        return 1
    else:
        print()
        print("[SUCCESS] All person profiles are valid!")
        print("          Run generate-codeowners.py to regenerate the CODEOWNERS file.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
