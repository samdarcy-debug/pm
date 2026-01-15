#!/usr/bin/env python3
"""
Fix markdown formatting for reports that were converted from PDF using pdftotext.
Adds proper heading markers based on common section patterns.
"""

import re
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
    print(f"Processing: {file_path.name}")

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter from content
    parts = content.split('---\n', 2)
    if len(parts) != 3:
        print(f"  WARNING: Could not parse frontmatter in {file_path.name}")
        return False

    frontmatter = f"---\n{parts[1]}---\n"
    body = parts[2]

    # Fix headings in the body
    fixed_body = fix_markdown_headings(body)

    # Check if any changes were made
    if fixed_body == body:
        print(f"  No changes needed")
        return False

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter + fixed_body)

    print(f"  SUCCESS: Fixed headings")
    return True


def main():
    """Main processing function."""
    # Process the specific week folder with known issues
    week_folder = Path(r"c:\Users\DanielKong\pm\weekly-reports\team-reports\2025-11-07")

    if not week_folder.exists():
        print(f"ERROR: Week folder not found: {week_folder}")
        return

    print(f"Processing reports in: {week_folder}\n")

    # Known problematic reports (originally PDFs)
    problem_reports = [
        "dai-weekly-report-2025-11-07.md",
        "gtm-workspace-weekly-report-2025-11-07.md",
        "gtm-studio-weekly-report-2025-11-07.md",
    ]

    fixed_count = 0
    for report_name in problem_reports:
        report_path = week_folder / report_name
        if report_path.exists():
            if process_report(report_path):
                fixed_count += 1
        else:
            print(f"WARNING: File not found: {report_name}")

    print(f"\n{'='*60}")
    print(f"Fixed {fixed_count} report(s)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
