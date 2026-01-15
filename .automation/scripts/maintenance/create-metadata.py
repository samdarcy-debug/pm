#!/usr/bin/env python3
"""
Automatic metadata generator for PM knowledge repository.

This script:
1. Checks that the git author has a person file (blocks commit if missing)
2. Generates/updates YAML frontmatter from context (path, git history, content)

Usage:
    python scripts/maintenance/create-metadata.py path/to/file.md
"""

import sys
import os
import re
import subprocess
import json
from datetime import datetime
from pathlib import Path
import glob

def should_skip_file(filepath):
    """Check if file should be excluded from formatting."""
    path_str = str(filepath).replace('\\', '/')

    # Exclude templates and skills
    if path_str.startswith('_templates/'):
        return True, "meta-document (template)"
    if '.claude/skills/' in path_str:
        return True, "meta-document (skill)"

    # Exclude root documentation
    if path_str in ['README.md', 'CLAUDE.md']:
        return True, "meta-document (root doc)"

    # Exclude process documentation READMEs
    if 'README.md' in path_str and 'teams/' not in path_str:
        return True, "meta-document (process doc)"

    # Exclude person docs (onboard skill handles these)
    if '/_people/' in path_str and path_str.endswith('.md'):
        return True, "person doc (managed by onboard skill)"

    return False, None

# Simplified tag vocabularies for consistent document clustering
# Tags answer: "What bucket does this go in?"
# Topic field handles: "What's inside?"

# Product tags (major products only)
PRODUCT_TAGS = [
    'gtm-workspace',
    'copilot',
    'gtm-studio',
    'ringlead',
    'zi-marketing',
    'chorus',
    'data'  # contact data, company data, signal data
]

# Document type tags (evolve as needed)
DOC_TYPE_TAGS = [
    'voc-feedback',        # Voice of customer analysis
    'weekly-report',       # Weekly status reports
    'strategy-memo',       # Strategic memos
    'feature-request',     # Customer feature requests
    'competitive-intel'    # Competitor analysis
]

def find_person_file(author_name, author_email):
    """
    Search for a person file matching the git author.
    Returns path to person file if found, None otherwise.
    """
    # Search in teams/*/*/_people/*.md for matching person files
    person_files = glob.glob('teams/*/*/_people/*.md') + glob.glob('teams/*/_people/*.md')

    for person_file in person_files:
        try:
            with open(person_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check if the file contains the author's name in title
                if f'title: {author_name}' in content.lower() or author_name.lower() in content.lower():
                    return person_file
        except Exception:
            continue

    return None

def check_person_file():
    """
    Check if the current git user has a person file.
    Exits with error code 1 if not found (blocks commit).
    """
    try:
        result = subprocess.run(
            ['git', 'config', 'user.name'],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print("WARNING: Could not determine git user. Please configure git user.name and user.email")
            sys.exit(1)
        author_name = result.stdout.strip()

        result = subprocess.run(
            ['git', 'config', 'user.email'],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print("WARNING: Could not determine git user. Please configure git user.name and user.email")
            sys.exit(1)
        author_email = result.stdout.strip()
    except Exception as e:
        print(f"WARNING: Could not determine git user: {e}")
        sys.exit(1)

    person_file = find_person_file(author_name, author_email)

    if not person_file:
        print("""
WARNING: No person file found for you!

Looks like you're new to this repository. Before you can commit,
you need to set up your profile.

Run this command to get started:
-> Say "onboard me" to Claude Code

This takes ~2 minutes and handles everything:
- Creates your person file
- Sets up automatic formatting
- Gets you ready to contribute
""")
        sys.exit(1)

    return person_file

def get_file_creation_date(filepath):
    """Get the creation date of a file from git history."""
    try:
        result = subprocess.run(
            ['git', 'log', '--follow', '--format=%ad', '--date=short', '--', filepath],
            capture_output=True, text=True, check=True
        )
        dates = result.stdout.strip().split('\n')
        if dates and dates[-1]:
            return dates[-1]  # First commit date
    except subprocess.CalledProcessError:
        pass

    return datetime.now().strftime('%Y-%m-%d')

def detect_document_type(filepath):
    """Detect document type from file path."""
    path_str = str(filepath).replace('\\', '/')

    # Path-based type detection
    if '/working_docs/prds/' in path_str:
        return 'prd'
    elif '/working_docs/rfcs/' in path_str:
        return 'rfc'
    elif '/working_docs/one-pagers/' in path_str:
        return 'one-pager'
    elif '/working_docs/six-pagers/' in path_str:
        return 'six-pager'
    elif '/VOC/' in path_str:
        return 'voc-analysis'
    elif 'teams/leadership/documentation/' in path_str:
        return 'memo'
    elif '/documentation/' in path_str:
        return 'doc'
    elif 'weekly-reports/' in path_str:
        return 'weekly-report'

    return 'doc'  # Default fallback

def extract_team_from_path(filepath):
    """Extract team name from file path."""
    path_str = str(filepath).replace('\\', '/')
    match = re.search(r'teams/([^/]+)/', path_str)
    if match:
        return match.group(1)
    return None

def extract_date_range_from_path(filepath):
    """
    Extract period_start, period_end, report_date from filename/path.

    Patterns recognized:
    - YYYYMMDD-YYYYMMDD VOC ANALYSIS → period_start, period_end
    - weekly-report-YYYY-MM-DD → report_date (end of week)
    - synthesis-YYYY-MM-DD → report_date

    Returns dict with keys: period_start, period_end, report_date
    Returns None if no time-bounded date pattern found.
    """
    filename = Path(filepath).name

    # Pattern 1: Date range in filename (VOC reports)
    # Example: "20251103-20251117 VOC ANALYSIS GTM WORKSPACE"
    range_match = re.search(r'(\d{8})-(\d{8})', filename)
    if range_match:
        start_str, end_str = range_match.groups()
        period_start = f"{start_str[:4]}-{start_str[4:6]}-{start_str[6:]}"
        period_end = f"{end_str[:4]}-{end_str[4:6]}-{end_str[6:]}"
        return {
            'period_start': period_start,
            'period_end': period_end,
            'report_date': None
        }

    # Pattern 2: Single date (weekly reports, synthesis reports)
    # Example: "weekly-report-2025-11-17.md" or "synthesis-2025-11-17.md"
    single_date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if single_date_match and ('weekly-report' in filename or 'synthesis' in filename):
        report_date = single_date_match.group(1)
        return {
            'period_start': None,
            'period_end': None,
            'report_date': report_date
        }

    # No time-bounded dates found
    return None

def generate_id(doc_type, team):
    """Generate unique sequential ID for document."""
    year = datetime.now().year

    # Find all existing IDs for this type and year
    pattern = f"{doc_type}-{year}-"
    max_num = 0

    # Search in all markdown files
    for md_file in glob.glob('teams/**/*.md', recursive=True):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Look for id: {type}-{year}-{num}
                matches = re.findall(rf'id:\s*{re.escape(pattern)}(\d+)', content)
                for match in matches:
                    max_num = max(max_num, int(match))
        except Exception:
            continue

    # Generate next ID
    next_num = max_num + 1
    return f"{doc_type}-{year}-{next_num:03d}"

def extract_title_from_content(content):
    """Extract title from first H1 heading in content."""
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return None

def extract_title_from_filename(filepath):
    """Extract title from filename - universal approach."""
    filename = Path(filepath).stem

    # Remove common date prefixes (universal patterns)
    # Pattern 1: "YYYY-MM-DD " prefix
    filename = re.sub(r'^\d{4}-\d{2}-\d{2}\s+', '', filename)

    # Pattern 2: "YYYYMMDD-YYYYMMDD " date range prefix
    filename = re.sub(r'^\d{8}-\d{8}\s+', '', filename)

    # Replace separators with spaces
    title = filename.replace('-', ' ').replace('_', ' ')

    # Smart title case (preserve common acronyms)
    words = title.split()
    title_words = []

    # List of words to keep uppercase
    ACRONYMS = {'VOC', 'GTM', 'API', 'SDK', 'AI', 'ML', 'PRD', 'RFC', 'CEO', 'CTO', 'PM', 'UI', 'UX'}

    for word in words:
        if word.upper() in ACRONYMS:
            title_words.append(word.upper())
        else:
            title_words.append(word.capitalize())

    return ' '.join(title_words)

def extract_topic_from_content(content):
    """Extract topic from HTML comment: <!-- topic: ... -->

    Skills (create-doc, import-doc) generate topic summaries using LLM and add them as
    HTML comments in the document body. This function extracts that topic from the comment.

    If no topic comment is found, returns empty string (graceful fallback - doesn't block commit).
    """
    import re

    # Look for <!-- topic: ... --> comment
    match = re.search(r'<!--\s*topic:\s*(.+?)\s*-->', content, re.IGNORECASE | re.DOTALL)
    if match:
        topic = match.group(1).strip()
        # Clean up any newlines/extra whitespace
        topic = ' '.join(topic.split())
        # Limit to 100 chars
        if len(topic) > 100:
            topic = topic[:100].rsplit(' ', 1)[0] + '...'
        return topic

    # No topic comment found - return empty (graceful fallback)
    return ""

def extract_tags_from_content(content, doc_type):
    """
    Extract minimal, consistent tags for document clustering.

    Strategy:
    1. ONE product tag from title/first paragraph (what product is this about?)
    2. ONE document type tag (what kind of document is this?)

    Result: 1-2 tags total, maximum consistency across similar documents.
    The topic field handles specifics - tags are just for bucketing.
    """
    content_lower = content.lower()
    found_tags = []

    # Step 1: Find PRIMARY product (only from title + first paragraph)
    first_section = content_lower[:500]
    for tag in PRODUCT_TAGS:
        search_term = tag.replace('-', ' ')
        if search_term in first_section or tag in first_section:
            found_tags.append(tag)
            break  # Only one product tag

    # Step 2: Add document type tag based on doc_type
    doc_type_mapping = {
        'voc-analysis': 'voc-feedback',
        'weekly-report': 'weekly-report',
        'memo': 'strategy-memo'
    }

    if doc_type in doc_type_mapping:
        found_tags.append(doc_type_mapping[doc_type])
    elif doc_type in ['prd', 'rfc'] and 'feature request' in content_lower:
        found_tags.append('feature-request')

    return found_tags

def extract_related_links(content):
    """Extract wiki-links from content."""
    # Find all [[wiki-links]]
    links = re.findall(r'\[\[([^\]]+)\]\]', content)
    return links

def parse_frontmatter(content):
    """Parse existing YAML frontmatter if present."""
    if not content.startswith('---\n'):
        return {}, content

    # Find end of frontmatter
    end_match = re.search(r'\n---\n', content[4:])
    if not end_match:
        return {}, content

    frontmatter_text = content[4:end_match.start() + 4]
    body = content[end_match.end() + 4:]

    # Parse YAML-like frontmatter (simple key: value pairs)
    metadata = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Handle lists
            if value.startswith('[') and value.endswith(']'):
                value = [v.strip() for v in value[1:-1].split(',') if v.strip()]

            metadata[key] = value

    return metadata, body


def generate_frontmatter(filepath, existing_metadata, body):
    """Generate complete frontmatter for document."""
    doc_type = detect_document_type(filepath)
    team = extract_team_from_path(filepath)

    # Get or generate core fields
    doc_id = existing_metadata.get('id') or generate_id(doc_type, team)

    # Title: from existing, filename, or first H1
    title = existing_metadata.get('title')
    if not title:
        title = extract_title_from_content(body) or extract_title_from_filename(filepath)

    # Status
    status = existing_metadata.get('status', 'draft')

    # Owner: from existing or person file
    owner = existing_metadata.get('owner')
    if not owner:
        person_file = check_person_file()  # This also validates person file exists
        # Convert to wiki-link format
        owner = f"[[{person_file.replace('.md', '')}]]"

    # Migrate legacy author field
    if 'author' in existing_metadata and not owner:
        # Try to find person file for author
        author_name = existing_metadata['author']
        person_file = find_person_file(author_name, '')
        if person_file:
            owner = f"[[{person_file.replace('.md', '')}]]"

    # Dates (core fields)
    created = existing_metadata.get('created') or get_file_creation_date(filepath)
    updated = datetime.now().strftime('%Y-%m-%d')

    # Time-bounded date fields (optional, auto-detected from filename)
    date_range = extract_date_range_from_path(filepath)
    period_start = existing_metadata.get('period_start')
    period_end = existing_metadata.get('period_end')
    report_date = existing_metadata.get('report_date')

    # Only set time-bounded fields if auto-detected and not already set
    if date_range:
        if not period_start and date_range['period_start']:
            period_start = date_range['period_start']
        if not period_end and date_range['period_end']:
            period_end = date_range['period_end']
        if not report_date and date_range['report_date']:
            report_date = date_range['report_date']

    # Semantic fields
    topic = existing_metadata.get('topic') or extract_topic_from_content(body)

    tags = existing_metadata.get('tags')
    if not tags or tags == []:
        tags = extract_tags_from_content(body, doc_type)  # Pass doc_type for consistency

    related = existing_metadata.get('related')
    if not related or related == []:
        related = extract_related_links(body)

    # Build frontmatter (order matters for readability)
    metadata = {
        'id': doc_id,
        'title': title,
        'type': doc_type,
        'status': status,
        'team': team,
        'owner': owner,
        'created': created,
        'updated': updated,
    }

    # Add time-bounded fields if present
    if period_start:
        metadata['period_start'] = period_start
    if period_end:
        metadata['period_end'] = period_end
    if report_date:
        metadata['report_date'] = report_date

    # Add semantic fields
    metadata['topic'] = topic
    metadata['tags'] = tags
    metadata['related'] = related

    return metadata

def format_frontmatter_to_yaml(metadata):
    """Format metadata dict as YAML frontmatter."""
    yaml_lines = ['---']

    for key, value in metadata.items():
        if value is None or value == '':
            continue

        if isinstance(value, list):
            if not value:
                yaml_lines.append(f'{key}: []')
            else:
                yaml_lines.append(f'{key}: [{", ".join(str(v) for v in value)}]')
        else:
            yaml_lines.append(f'{key}: {value}')

    yaml_lines.append('---')
    return '\n'.join(yaml_lines)

def format_markdown_file(filepath):
    """Main function to format a markdown file."""
    # Read file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    # Parse existing frontmatter
    existing_metadata, body = parse_frontmatter(content)

    # Generate/update frontmatter
    metadata = generate_frontmatter(filepath, existing_metadata, body)

    # Combine frontmatter and body (body remains unchanged)
    formatted_content = format_frontmatter_to_yaml(metadata) + '\n\n' + body + '\n'

    # Write file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python .automation/scripts/create-metadata.py path/to/file.md")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    # Check if file should be skipped
    should_skip, skip_reason = should_skip_file(filepath)
    if should_skip:
        print(f"SKIPPED: {filepath} ({skip_reason})")
        sys.exit(0)  # Exit successfully - this is expected behavior

    # Check person file FIRST (blocks commit if missing)
    check_person_file()

    # Format the file
    success = format_markdown_file(filepath)

    if success:
        print(f"FORMATTED: {filepath}")
        sys.exit(0)
    else:
        print(f"FAILED to format: {filepath}")
        sys.exit(1)

if __name__ == '__main__':
    main()
