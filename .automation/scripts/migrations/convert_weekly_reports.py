#!/usr/bin/env python3
"""
Convert individual team weekly reports from Word/PDF to Markdown with YAML frontmatter.
Organizes reports into week folders in weekly-reports/team-reports/
"""

import os
import re
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
import sys

# Source and destination directories
SOURCE_DIR = r"C:\Users\DanielKong\Downloads\Weekly Team Reports (copy over from team folders)"
DEST_BASE = r"C:\Users\DanielKong\pm\weekly-reports\team-reports"

# Team name mapping - CRITICAL: use exact slugs
TEAM_MAPPING = {
    # GTM Studio
    r"GTM Studio": "gtm-studio",
    r"Sneh": "gtm-studio",

    # Copilot
    r"GTM Workspace": "copilot",
    r"SalesOS_Copilot": "copilot",
    r"Victor": "copilot",
    r"Apps Team": "copilot",

    # Intelligence
    r"Intelligence": "intelligence",

    # Semantic Data
    r"Semantic Data": "semantic-data",

    # Context Engineering
    r"Context Engineering": "context-engineering",

    # MCP
    r"MCP Team": "mcp",
    r"MCP Tiger Team": "mcp",

    # DAI
    r"DAI": "dai",

    # Data
    r"Data Executive": "data",
    r"Data Team": "data",
    r"V2 Data": "data",

    # Core Data
    r"Core Data": "core-data",

    # Data Platform
    r"GTM Data Platform": "data-platform",
    r"Data Platform": "data-platform",
    r"M\. Delurgio": "data-platform",

    # Integrations
    r"Integrations": "integrations",

    # Admin
    r"Admin Team": "admin",
    r"Team Provisioning": "admin",
    r"Brannen": "admin",
    r"B\. Huske": "admin",

    # Automation
    r"Automation": "automation",

    # ZIM
    r"ZIM": "zim",
    r"Anwar": "zim",
    r"Plays, Campaigns, Audiences": "zim",

    # Product BI
    r"Product BI": "product-bi",
    r"Business Intelligence": "product-bi",
    r"Analytics": "product-bi",

    # Product Ops
    r"Product Ops": "product-ops",
    r"Product Operations": "product-ops",

    # Product Marketing
    r"Product Marketing": "product-marketing",
    r"PMM": "product-marketing",
}

# Teams to skip (no longer exist)
SKIP_TEAMS = [
    "Intent", "AFS", "Advanced Search",
    "Signals and Recommendations",
    "V.kamath", "Veronica Hudson"
]

# Team display names
TEAM_DISPLAY_NAMES = {
    "gtm-studio": "GTM Studio",
    "copilot": "GTM Workspace (Copilot)",
    "intelligence": "Intelligence",
    "semantic-data": "Semantic Data",
    "context-engineering": "Context Engineering",
    "mcp": "MCP",
    "dai": "DAI",
    "data": "Data",
    "core-data": "Core Data",
    "data-platform": "GTM Data Platform",
    "integrations": "Integrations",
    "admin": "Admin",
    "automation": "Automation",
    "zim": "ZIM",
    "product-bi": "Product BI",
    "product-ops": "Product Ops",
    "product-marketing": "Product Marketing",
}


def parse_week_folder_name(folder_name):
    """
    Parse week folder name to determine the Friday date.
    Examples:
      "08-04-25 Weekly Team Reports" -> Monday 08/04/25 -> Friday 08/08/25
      "06-23-25 Weekly Team Reports (copy over from team folders)" -> Monday 06/23/25 -> Friday 06/27/25
    """
    # Extract date portion (MM-DD-YY)
    match = re.match(r"(\d{2})-(\d{2})-(\d{2})", folder_name)
    if not match:
        return None

    month, day, year = match.groups()
    # Assuming 2025 for "25"
    full_year = f"20{year}"

    # Parse as Monday date
    monday_date = datetime.strptime(f"{full_year}-{month}-{day}", "%Y-%m-%d")

    # Calculate Friday (Monday + 4 days)
    friday_date = monday_date + timedelta(days=4)

    return friday_date


def map_filename_to_team(filename):
    """
    Map filename to team slug using the team mapping.
    Returns team_slug or None if should be skipped.
    """
    # Check if should skip
    for skip_term in SKIP_TEAMS:
        if skip_term.lower() in filename.lower():
            return None

    # Try to match against team mapping
    for pattern, team_slug in TEAM_MAPPING.items():
        if re.search(pattern, filename, re.IGNORECASE):
            return team_slug

    return None


def get_week_number(date):
    """Get ISO week number for a date."""
    return date.isocalendar()[1]


def get_quarter(date):
    """Get quarter string (Q1, Q2, Q3, Q4) for a date."""
    quarter = (date.month - 1) // 3 + 1
    return f"Q{quarter}{date.year}"


def get_reporting_period(friday_date):
    """Get reporting period string (e.g., 'August 4-8, 2025')."""
    monday_date = friday_date - timedelta(days=4)

    # If same month
    if monday_date.month == friday_date.month:
        return f"{friday_date.strftime('%B')} {monday_date.day}-{friday_date.day}, {friday_date.year}"
    else:
        # Different months
        return f"{monday_date.strftime('%B %d')}-{friday_date.strftime('%B %d, %Y')}"


def convert_file_to_markdown(input_file, output_file):
    """Convert Word/PDF file to Markdown using pandoc or pdftotext."""
    file_ext = input_file.suffix.lower()

    try:
        if file_ext == '.pdf':
            # Use pdftotext for PDF files, then convert to markdown format
            # First extract text
            result = subprocess.run(
                ["pdftotext", "-layout", str(input_file), "-"],
                capture_output=True,
                text=True,
                check=True
            )

            # Write the text content as markdown
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result.stdout)

            return True
        else:
            # Use pandoc for Word documents
            result = subprocess.run(
                ["pandoc", str(input_file), "-t", "markdown", "-o", str(output_file)],
                capture_output=True,
                text=True,
                check=True
            )
            return True
    except subprocess.CalledProcessError as e:
        print(f"    ERROR converting {input_file.name}: {e.stderr}")
        return False
    except Exception as e:
        print(f"    ERROR converting {input_file.name}: {str(e)}")
        return False


def create_frontmatter(team_slug, friday_date):
    """Create YAML frontmatter for a weekly report."""
    week_num = get_week_number(friday_date)
    quarter = get_quarter(friday_date)
    reporting_period = get_reporting_period(friday_date)
    team_display_name = TEAM_DISPLAY_NAMES.get(team_slug, team_slug.replace("-", " ").title())

    frontmatter = f"""---
id: weekly-{team_slug}-{friday_date.strftime('%Y')}-{week_num:02d}
title: "{team_display_name} Weekly Report - {friday_date.strftime('%B %d, %Y')}"
type: weekly-report
status: approved
team: {team_slug}
owner:
created: {friday_date.strftime('%Y-%m-%d')}
updated: 2026-01-06
week_ending: {friday_date.strftime('%Y-%m-%d')}
reporting_period: "{reporting_period}"
tags: ["weekly-report", "{quarter}"]
---

"""
    return frontmatter


def process_week_folder(week_folder_path):
    """Process all reports in a week folder."""
    week_folder = Path(week_folder_path)
    folder_name = week_folder.name

    print(f"\n{'='*80}")
    print(f"Processing: {folder_name}")
    print(f"{'='*80}")

    # Parse Friday date from folder name
    friday_date = parse_week_folder_name(folder_name)
    if not friday_date:
        print(f"  SKIP: Could not parse date from folder name")
        return

    print(f"  Week ending (Friday): {friday_date.strftime('%Y-%m-%d')}")

    # Create destination folder
    dest_folder = Path(DEST_BASE) / friday_date.strftime('%Y-%m-%d')
    dest_folder.mkdir(parents=True, exist_ok=True)
    print(f"  Destination: {dest_folder}")

    # Process each file in the week folder
    files = list(week_folder.glob("*.docx")) + list(week_folder.glob("*.pdf"))
    print(f"  Found {len(files)} files to process")

    processed_count = 0
    skipped_count = 0
    error_count = 0

    for file_path in files:
        filename = file_path.name
        print(f"\n  Processing: {filename}")

        # Map filename to team slug
        team_slug = map_filename_to_team(filename)

        if team_slug is None:
            print(f"    SKIP: No team mapping or should skip")
            skipped_count += 1
            continue

        print(f"    Team: {team_slug}")

        # Create temporary markdown file
        temp_md = dest_folder / f"{team_slug}_temp.md"
        final_md = dest_folder / f"{team_slug}.md"

        # Convert to markdown
        if not convert_file_to_markdown(file_path, temp_md):
            error_count += 1
            continue

        # Read converted content
        try:
            with open(temp_md, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"    ERROR reading temp file: {e}")
            error_count += 1
            continue

        # Create frontmatter
        frontmatter = create_frontmatter(team_slug, friday_date)

        # Combine frontmatter and content
        final_content = frontmatter + content

        # Write final file
        try:
            with open(final_md, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"    SUCCESS: Created {final_md.name}")
            processed_count += 1
        except Exception as e:
            print(f"    ERROR writing final file: {e}")
            error_count += 1
            continue

        # Remove temp file
        temp_md.unlink()

    print(f"\n  Summary: {processed_count} processed, {skipped_count} skipped, {error_count} errors")


def main():
    """Main processing function."""
    source_dir = Path(SOURCE_DIR)

    if not source_dir.exists():
        print(f"ERROR: Source directory not found: {source_dir}")
        sys.exit(1)

    # Get all week folders
    week_folders = [f for f in source_dir.iterdir() if f.is_dir()]
    week_folders.sort()

    print(f"Found {len(week_folders)} week folders to process")

    for week_folder in week_folders:
        process_week_folder(week_folder)

    print(f"\n{'='*80}")
    print("Processing complete!")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()
