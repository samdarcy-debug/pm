#!/usr/bin/env python3
"""
Fix markdown formatting for reports that were converted from PDF using pdftotext.
Adds proper heading markers based on common section patterns.

Usage:
    python .automation/scripts/fix-pdf-markdown.py path/to/file.md
    python .automation/scripts/fix-pdf-markdown.py path/to/file1.md path/to/file2.md
"""

import re
import sys
from pathlib import Path

# Common heading patterns in the reports
HEADING_PATTERNS = {
    # Level 1 headings (main sections)
    r'^(Executive Summary)$': '##',
    r'^(This Week\'s Progress)$': '##',
    r'^(Strategic Challenges)$': '##',
    r'^(Strategic Insights)$': '##',
    r'^(Cross-Team Dependencies)$': '##',
    r'^(Looking Ahead)$': '##',
    r'^(Goals & Progress)$': '##',

    # Level 2 headings (subsections)
    r'^(Key Momentum Areas)$': '###',
    r'^(Key Learnings & Discoveries)$': '###',
}


def should_be_heading(line):
    """Check if a line should be a heading and return the heading level."""
    line_stripped = line.strip()

    if not line_stripped:
        return None

    # Check against known patterns
    for pattern, marker in HEADING_PATTERNS.items():
        if re.match(pattern, line_stripped):
            return marker, line_stripped

    return None


def fix_markdown_headings(content):
    """Add markdown heading markers to plain text content."""
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        result = should_be_heading(line)
        if result:
            marker, text = result
            fixed_lines.append(f"{marker} {text}")
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def process_report(file_path):
    """Process a single report file."""
    print(f"Processing: {file_path}")

    # Read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"  ERROR: File not found: {file_path}")
        return False
    except Exception as e:
        print(f"  ERROR: Could not read file: {e}")
        return False

    # Split frontmatter from content (if present)
    parts = content.split('---\n', 2)
    if len(parts) == 3:
        # Has frontmatter
        frontmatter = f"---\n{parts[1]}---\n"
        body = parts[2]
    else:
        # No frontmatter - process entire content
        frontmatter = ""
        body = content

    # Fix headings in the body
    fixed_body = fix_markdown_headings(body)

    # Check if any changes were made
    if fixed_body == body:
        print(f"  No changes needed")
        return False

    # Write back
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + fixed_body)
        print(f"  SUCCESS: Fixed headings")
        return True
    except Exception as e:
        print(f"  ERROR: Could not write file: {e}")
        return False


def main():
    """Main processing function."""
    if len(sys.argv) < 2:
        print("ERROR: No file path provided")
        print()
        print("Usage:")
        print("    python .automation/scripts/fix-pdf-markdown.py path/to/file.md")
        print("    python .automation/scripts/fix-pdf-markdown.py file1.md file2.md file3.md")
        sys.exit(1)

    file_paths = [Path(arg) for arg in sys.argv[1:]]

    print(f"Processing {len(file_paths)} file(s)...\n")

    fixed_count = 0
    for file_path in file_paths:
        if process_report(file_path):
            fixed_count += 1
        print()  # Blank line between files

    print(f"{'='*60}")
    print(f"Fixed {fixed_count} of {len(file_paths)} file(s)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
