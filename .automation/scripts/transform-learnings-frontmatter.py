#!/usr/bin/env python3
"""
Transform frontmatter in learning memos to match PM repo schema.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional

# Team name mappings from source to repo structure
TEAM_MAPPINGS = {
    "Data": "data",
    "GTM-Studio": "gtm-studio",
    "GTM-Workspace": "gtm-workspace",
    "Intelligence": "intelligence",
    "Platform": "platform",
    "Ops-Strategy": "ops",
    "DAI-Executive": "leadership",
}

def slugify_name(name: str) -> str:
    """Convert PM name to person doc slug (e.g., 'Jody Roberts' -> 'jody-roberts')"""
    if name.lower() == "unknown-pm" or not name:
        return None
    # Handle special cases
    name = name.replace(".", "")
    # Convert to lowercase and replace spaces with hyphens
    slug = name.lower().strip().replace(" ", "-")
    # Remove any non-alphanumeric characters except hyphens
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    return slug

def transform_frontmatter(content: str, filename: str, file_index: int) -> str:
    """Transform frontmatter from source schema to target schema"""

    # Extract frontmatter and body
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        # No frontmatter - handle special case files
        return add_frontmatter_to_summary(content, filename, file_index)

    frontmatter_str, body = match.groups()

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {filename}: {e}")
        return content

    # Create new frontmatter
    new_frontmatter = {}

    # Generate ID
    new_frontmatter['id'] = f"learnings-2025-{file_index:03d}"

    # Keep title
    new_frontmatter['title'] = frontmatter.get('title', filename)

    # Transform type
    doc_type = frontmatter.get('type', 'learnings-memo')
    new_frontmatter['type'] = 'doc'

    # Set status
    new_frontmatter['status'] = 'approved'

    # Transform team
    source_team = frontmatter.get('team', '')
    new_frontmatter['team'] = TEAM_MAPPINGS.get(source_team, source_team.lower())

    # Transform owner
    pm_owner = frontmatter.get('pm_owner', frontmatter.get('pm_name', ''))
    owner_slug = slugify_name(pm_owner)

    if owner_slug:
        team_slug = new_frontmatter['team']
        new_frontmatter['owner'] = f"[[teams/{team_slug}/_people/{owner_slug}]]"
    else:
        # Fallback to Brett Jacobs for unknown/missing owners
        new_frontmatter['owner'] = "[[teams/ops/_people/brett-jacobs]]"

    # Transform dates
    date = frontmatter.get('date', frontmatter.get('last_updated', '2025-12-23'))
    new_frontmatter['created'] = date
    new_frontmatter['updated'] = date

    # Add tags
    team_tag = new_frontmatter['team']
    new_frontmatter['tags'] = ['learnings', 'q3-2025', team_tag]

    # Add empty related
    new_frontmatter['related'] = []

    # Reconstruct file
    new_frontmatter_str = yaml.dump(new_frontmatter, default_flow_style=False, sort_keys=False)
    return f"---\n{new_frontmatter_str}---\n{body}"

def add_frontmatter_to_summary(content: str, filename: str, file_index: int) -> str:
    """Add frontmatter to files that don't have any"""

    # Extract title from first heading
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filename.replace('.md', '').replace('-', ' ').title()

    frontmatter = {
        'id': f"learnings-2025-{file_index:03d}",
        'title': title,
        'type': 'doc',
        'status': 'approved',
        'team': 'ops',
        'owner': '[[teams/ops/_people/brett-jacobs]]',
        'created': '2025-12-23',
        'updated': '2025-12-23',
        'tags': ['learnings', 'q3-2025', 'analysis'],
        'related': []
    }

    frontmatter_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    return f"---\n{frontmatter_str}---\n{content}"

def process_directory(base_path: Path):
    """Process all markdown files in the learnings-memos directory"""

    md_files = sorted(list(base_path.rglob("*.md")))
    print(f"Found {len(md_files)} markdown files to process")

    file_index = 1
    processed = []
    errors = []

    for md_file in md_files:
        try:
            print(f"Processing {md_file.relative_to(base_path)}...")

            # Read file
            content = md_file.read_text(encoding='utf-8')

            # Transform frontmatter
            new_content = transform_frontmatter(content, md_file.name, file_index)

            # Write back
            md_file.write_text(new_content, encoding='utf-8')

            processed.append(str(md_file.relative_to(base_path)))
            file_index += 1

        except Exception as e:
            error_msg = f"Error processing {md_file}: {e}"
            print(error_msg)
            errors.append(error_msg)

    print(f"\n✅ Successfully processed {len(processed)} files")

    if errors:
        print(f"\n❌ Encountered {len(errors)} errors:")
        for error in errors:
            print(f"  - {error}")

    return processed, errors

def main():
    # Get base path
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    learnings_path = repo_root / "learnings-memos"

    if not learnings_path.exists():
        print(f"❌ Directory not found: {learnings_path}")
        return

    print(f"Processing files in: {learnings_path}\n")

    # Process all files
    processed, errors = process_directory(learnings_path)

    print(f"\nTransformation complete!")
    print(f"Files processed: {len(processed)}")

    if errors:
        print(f"\n⚠️ Review errors above and fix manually if needed")

if __name__ == "__main__":
    main()
