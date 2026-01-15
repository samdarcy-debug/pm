#!/usr/bin/env python3
"""
Migrate weekly team reports from centralized to distributed structure.
"""
import os
import shutil
from pathlib import Path

# Team slug mapping
TEAM_MAPPING = {
    # Leadership (DAI weekly reports - NOT in documentation/)
    'dai': 'teams/leadership/weekly-reports',

    # Data org
    'data': 'teams/data/data-executive-team/weekly-reports',
    'core-data': 'teams/data/core-data/weekly-reports',

    # Intelligence org
    'intelligence': 'teams/intelligence/intelligence-executive-team/weekly-reports',
    'semantic-data': 'teams/intelligence/semantic-data/weekly-reports',
    'context-engineering': 'teams/intelligence/context-engineering/weekly-reports',
    'mcp': 'teams/intelligence/mcp/weekly-reports',

    # Platform org
    'integrations': 'teams/platform/integrations/weekly-reports',
    'admin': 'teams/platform/admin/weekly-reports',
    'automation': 'teams/platform/automation/weekly-reports',
    'zim': 'teams/platform/zim/weekly-reports',
    'data-platform': 'teams/platform/data-platform/weekly-reports',

    # Operations org
    'product-marketing': 'teams/ops/product-marketing/weekly-reports',
    'product-bi': 'teams/ops/business-intelligence/weekly-reports',
    'product-ops': 'teams/ops/product-ops/weekly-reports',

    # Flat teams
    'gtm-studio': 'teams/gtm-studio/weekly-reports',
    'gtm-workspace': 'teams/gtm-workspace/weekly-reports',
    'copilot': 'teams/gtm-workspace/weekly-reports',  # Legacy name
}

def migrate_team_reports(repo_root):
    """Migrate all team reports from centralized to distributed structure."""
    source_dir = Path(repo_root) / "weekly-reports" / "team-reports"

    if not source_dir.exists():
        print(f"ERROR: Source directory not found: {source_dir}")
        return

    week_folders = sorted([f for f in source_dir.iterdir() if f.is_dir()])
    total_files = 0
    migrated_files = 0
    unknown_teams = set()

    print(f"Found {len(week_folders)} week folders to process\n")

    for week_folder in week_folders:
        print(f"Processing week: {week_folder.name}")

        report_files = list(week_folder.glob("*.md"))
        total_files += len(report_files)

        for report_file in report_files:
            # Extract team slug from filename: {team}-weekly-report-{date}.md
            filename = report_file.name
            team_slug = filename.replace(f"-weekly-report-{week_folder.name}.md", "")

            if team_slug not in TEAM_MAPPING:
                print(f"  WARNING: Unknown team '{team_slug}' in {filename}")
                unknown_teams.add(team_slug)
                continue

            # Determine destination
            dest_dir = Path(repo_root) / TEAM_MAPPING[team_slug]
            dest_file = dest_dir / filename

            # Check if destination directory exists
            if not dest_dir.exists():
                print(f"  ERROR: Destination directory does not exist: {dest_dir}")
                print(f"         Skipping {filename}")
                continue

            # Use git mv to preserve history
            result = os.system(f'git mv "{report_file}" "{dest_file}"')
            if result == 0:
                print(f"  OK {team_slug}: {filename}")
                migrated_files += 1
            else:
                print(f"  FAILED to move {filename}")

    print(f"\n" + "="*60)
    print(f"Migration Summary:")
    print(f"  Total files found: {total_files}")
    print(f"  Successfully migrated: {migrated_files}")
    print(f"  Failed/skipped: {total_files - migrated_files}")

    if unknown_teams:
        print(f"\nUnknown team slugs encountered:")
        for team in sorted(unknown_teams):
            print(f"  - {team}")
        print("\nThese teams are not in the TEAM_MAPPING. Please update the script if needed.")

    print("\nMigration complete!")

if __name__ == "__main__":
    repo_root = Path(__file__).parent
    print(f"Repository root: {repo_root}")
    print(f"Starting migration...\n")
    migrate_team_reports(repo_root)
